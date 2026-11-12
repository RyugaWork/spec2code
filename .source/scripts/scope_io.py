#!/usr/bin/env python3
"""Directory-relative, no-follow filesystem operations for Spec2Code-managed files.

On POSIX with openat/renameat support, writes are anchored to directory handles.
On platforms without dir_fd or O_NOFOLLOW (notably Windows), operations perform
repeated Path Guard checks but ARE NOT an OS-level TOCTOU sandbox. Use trusted
workspaces and OS ACLs in those environments.
"""
from __future__ import annotations

from contextlib import contextmanager
import hashlib
import os
from pathlib import Path
import secrets
import stat
import tempfile

import path_guard as guard


def _verified_local_root(root: Path) -> Path:
    """Fast path for *internal* filesystem calls after entrypoint Git validation.

    CLI/MCP entrypoints validate Git identity once per request. Per-file operations
    still reject root symlinks, traversal and directory substitution using handles.
    """
    raw = Path(os.path.abspath(os.fspath(root)))
    if not raw.is_dir() or guard._has_reparse_ancestor(raw):
        raise RuntimeError('SCOPE_VIOLATION: invalid local filesystem root')
    return raw


def _supports_anchoring() -> bool:
    return (hasattr(os, 'O_NOFOLLOW') and hasattr(os, 'O_DIRECTORY')
            and os.open in os.supports_dir_fd and os.mkdir in os.supports_dir_fd
            and os.rename in os.supports_dir_fd and os.unlink in os.supports_dir_fd)


@contextmanager
def _parent_fd(root: Path, path: Path, *, create: bool):
    """Obtain an anchored descriptor for the parent without following symlinks."""
    expected = os.stat(root, follow_symlinks=False)
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    fd = os.open(root, flags)
    try:
        got = os.fstat(fd)
        if (got.st_dev, got.st_ino) != (expected.st_dev, expected.st_ino):
            raise RuntimeError('SCOPE_VIOLATION: root replaced during operation')
        for segment in path.relative_to(root).parts[:-1]:
            if create:
                try:
                    os.mkdir(segment, 0o700, dir_fd=fd)
                except FileExistsError:
                    pass
            nxt = os.open(segment, flags, dir_fd=fd)
            os.close(fd)
            fd = nxt
        yield fd, path.name
    finally:
        os.close(fd)


def atomic_text(root: Path, destination: Path | str, content: str) -> None:
    """Atomic in-root text replacement. Does not follow symlink targets."""
    root = _verified_local_root(root)
    path = guard.check_path(root, destination)
    if not _supports_anchoring():
        path.parent.mkdir(parents=True, exist_ok=True)
        guard.check_path(root, path)
        with tempfile.NamedTemporaryFile('w', dir=path.parent, encoding='utf-8', newline='\n',
                                         prefix='.s2c-', delete=False) as stream:
            temp = Path(stream.name)
            stream.write(content)
        try:
            guard.check_path(root, path)
            os.replace(temp, path)
        finally:
            temp.unlink(missing_ok=True)
        return
    with _parent_fd(root, path, create=True) as (fd, name):
        try:
            old = os.stat(name, dir_fd=fd, follow_symlinks=False)
            if not stat.S_ISREG(old.st_mode):
                raise RuntimeError('PATH_GUARD_BLOCKED: target is not regular file')
        except FileNotFoundError:
            pass
        tmp = '.s2c-' + secrets.token_hex(12) + '.tmp'
        handle = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                         0o600, dir_fd=fd)
        try:
            with os.fdopen(handle, 'w', encoding='utf-8', newline='\n') as stream:
                stream.write(content)
                stream.flush()
                os.fsync(stream.fileno())
            # Re-check exact leaf before replacement; renameat replaces a link,
            # never follows its target even in a concurrent swap.
            try:
                old = os.stat(name, dir_fd=fd, follow_symlinks=False)
                if not stat.S_ISREG(old.st_mode):
                    raise RuntimeError('PATH_GUARD_BLOCKED: target replaced by non-file')
            except FileNotFoundError:
                pass
            os.rename(tmp, name, src_dir_fd=fd, dst_dir_fd=fd)
            os.fsync(fd)
        finally:
            try:
                os.unlink(tmp, dir_fd=fd)
            except FileNotFoundError:
                pass


def append_text(root: Path, destination: Path | str, content: str) -> None:
    """Append through O_NOFOLLOW using an anchored parent on supported systems."""
    root = _verified_local_root(root)
    path = guard.check_path(root, destination)
    if not _supports_anchoring():
        path.parent.mkdir(parents=True, exist_ok=True)
        guard.check_path(root, path)
        with path.open('a', encoding='utf-8', newline='\n') as stream:
            stream.write(content)
        return
    with _parent_fd(root, path, create=True) as (fd, name):
        out = os.open(name, os.O_WRONLY | os.O_APPEND | os.O_CREAT | os.O_NOFOLLOW,
                      0o600, dir_fd=fd)
        with os.fdopen(out, 'a', encoding='utf-8', newline='\n') as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise RuntimeError('PATH_GUARD_BLOCKED: append target is not a regular file')
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())


def unlink_verified(root: Path, target: Path | str, expected_sha256: str) -> None:
    """Remove an exact, hash-verified file, never following a symlink."""
    root = _verified_local_root(root)
    path = guard.check_path(root, target)
    if not _supports_anchoring():
        if not path.is_file() or path.is_symlink() or hashlib.sha256(path.read_bytes()).hexdigest() != expected_sha256:
            raise RuntimeError('SCOPE_VIOLATION: pending file changed before deletion')
        guard.check_path(root, path)
        path.unlink()
        return
    with _parent_fd(root, path, create=False) as (fd, name):
        handle = os.open(name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=fd)
        with os.fdopen(handle, 'rb') as stream:
            observed = os.fstat(stream.fileno())
            if not stat.S_ISREG(observed.st_mode):
                raise RuntimeError('SCOPE_VIOLATION: pending entry is not a regular file')
            digest = hashlib.sha256()
            for chunk in iter(lambda: stream.read(131072), b''):
                digest.update(chunk)
        if digest.hexdigest() != expected_sha256:
            raise RuntimeError('SCOPE_VIOLATION: pending file hash changed')
        current = os.stat(name, dir_fd=fd, follow_symlinks=False)
        if ((current.st_dev, current.st_ino, current.st_size, current.st_mtime_ns)
                != (observed.st_dev, observed.st_ino, observed.st_size, observed.st_mtime_ns)):
            raise RuntimeError('SCOPE_VIOLATION: pending file replaced before deletion')
        os.unlink(name, dir_fd=fd)


def read_bytes(root: Path, target: Path | str, *, max_bytes: int = 4 * 1024 * 1024) -> bytes:
    """Read a single regular file without following symlinks (POSIX anchored)."""
    root = _verified_local_root(root)
    path = guard.check_path(root, target)
    if not _supports_anchoring():
        guard.check_path(root, path)
        with path.open('rb') as stream:
            raw = stream.read(max_bytes + 1)
    else:
        with _parent_fd(root, path, create=False) as (fd, name):
            handle = os.open(name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=fd)
            with os.fdopen(handle, 'rb') as stream:
                if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                    raise RuntimeError('PATH_GUARD_BLOCKED: read target is not regular file')
                raw = stream.read(max_bytes + 1)
    if len(raw) > max_bytes:
        raise RuntimeError('SCOPE_VIOLATION: read cap exceeded')
    return raw
