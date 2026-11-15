#!/usr/bin/env python3
"""Directory-relative, no-follow filesystem operations for Spec2Code-managed files.

Managed I/O requires directory-handle anchoring with no-follow opens.
Hosts without that support, including native Windows, fail closed.
"""
from __future__ import annotations

from contextlib import ExitStack, contextmanager
import hashlib
import os
from pathlib import Path
import secrets
import stat

import path_guard as guard


def _verified_local_root(root: Path) -> Path:
    """Fast path for *internal* filesystem calls after entrypoint Git validation.

    CLI/MCP entrypoints validate Git identity once per request. Per-file operations
    still reject root symlinks, traversal and directory substitution using handles.
    """
    if not supports_anchoring():
        raise RuntimeError('SCOPE_VIOLATION: anchored filesystem I/O unavailable')
    raw = Path(os.path.abspath(os.fspath(root)))
    if not raw.is_dir() or guard._has_reparse_ancestor(raw):
        raise RuntimeError('SCOPE_VIOLATION: invalid local filesystem root')
    return raw


def supports_anchoring() -> bool:
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


@contextmanager
def exclusive_output(root: Path):
    """Serialize managed publishers using a crash-released directory lock."""
    root = _verified_local_root(root)
    try:
        import fcntl
    except ImportError as exc:
        raise RuntimeError('SCOPE_VIOLATION: output locking unavailable') from exc
    # The path is a placeholder. Only its parent (the root) is opened.
    with _parent_fd(root, root / '.s2c-output-lock', create=False) as (fd, _):
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise RuntimeError('ARCH_OUTPUT_BUSY: retry after the current publisher') from exc
        yield


def atomic_text(root: Path, destination: Path | str, content: str, *,
                staging_dir: Path | None = None) -> None:
    """Atomic in-root text replacement. Does not follow symlink targets."""
    root = _verified_local_root(root)
    path = guard.check_path(root, destination)
    with ExitStack() as stack:
        fd, name = stack.enter_context(_parent_fd(root, path, create=True))
        stage_fd = fd
        if staging_dir is not None:
            staging_path = guard.check_path(root, staging_dir / '.s2c-staging')
            stage_fd, _ = stack.enter_context(_parent_fd(root, staging_path, create=True))
        try:
            old = os.stat(name, dir_fd=fd, follow_symlinks=False)
            if not stat.S_ISREG(old.st_mode):
                raise RuntimeError('PATH_GUARD_BLOCKED: target is not regular file')
        except FileNotFoundError:
            pass
        tmp = '.s2c-' + secrets.token_hex(12) + '.tmp'
        handle = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                         0o600, dir_fd=stage_fd)
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
            os.rename(tmp, name, src_dir_fd=stage_fd, dst_dir_fd=fd)
            os.fsync(fd)
            if stage_fd != fd:
                os.fsync(stage_fd)
        finally:
            try:
                os.unlink(tmp, dir_fd=stage_fd)
            except FileNotFoundError:
                pass


def append_text(root: Path, destination: Path | str, content: str) -> None:
    """Append through O_NOFOLLOW using an anchored parent on supported systems."""
    root = _verified_local_root(root)
    path = guard.check_path(root, destination)
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
    with _parent_fd(root, path, create=False) as (fd, name):
        handle = os.open(name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=fd)
        with os.fdopen(handle, 'rb') as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise RuntimeError('PATH_GUARD_BLOCKED: read target is not regular file')
            raw = stream.read(max_bytes + 1)
    if len(raw) > max_bytes:
        raise RuntimeError('SCOPE_VIOLATION: read cap exceeded')
    return raw
