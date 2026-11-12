#!/usr/bin/env python3
"""Fail-closed repository and path boundaries shared by all Spec2Code entrypoints.

The guard is local only. Git worktrees are supported; Git administrative files may
reside outside the worktree, but application reads/writes may not. This is not a
security sandbox against an attacker concurrently controlling the same filesystem.
"""
from __future__ import annotations

import os
from pathlib import Path, PureWindowsPath
import subprocess

# These runtime-owned locations must not be symlinks, including symlinked parents.
MANAGED_PATHS = (
    '.agents', '.agents/skills', '.agents/skills/spec-to-code',
    '.agents/skills/spec-to-code/scripts',
    '.agents/skills/spec-to-code/scripts/path_guard.py',
    '.agents/.skills', '.agents/.skills/spec-to-code',
    '.agents/.skills/spec-to-code/scripts',
    '.agents/.skills/spec-to-code/scripts/path_guard.py',
    '.agents/state', '.agents/state/infrastructure.json',
    '.agents/state/infrastructure-index.md', '.agents/state/session.json',
    '.agents/state/sessions.jsonl', '.agents/state/system-graph.json',
    '.agents/state/context-pack.json', '.agents/state/context-policy.json',
    '.agents/state/architecture-docs.json', '.agents/state/symbol-cache.json',
    '.agents/state/layerSummary.md', '.agents/state/impactMatrix.md',
    '.handoffs', '.handoffs/.details', '.handoffs/.buildnotes.handoff.md',
    '.handoffs/.merge.lock', '.summerize.md',
    'Present', 'API', 'Application', 'DataAccess', 'Persistence',
    'Security', 'Integrations', 'Delivery', 'Quality', 'Governance',
)


def check_path(root: Path, value: str | Path) -> Path:
    """Return an in-root, symlink-free path; safe for new paths and existing ones.

    Reject absolute foreign paths, traversal, drive/UNC forms, and symlinked
    ancestors, even if a symlink happens to lead back inside the repository.
    """
    root = Path(root)
    raw = os.fspath(value)
    if not raw or '\x00' in raw or any(ord(c) < 32 for c in raw):
        raise RuntimeError('PATH_GUARD_BLOCKED: invalid path characters')
    # An already-formed absolute Path inside the root is accepted for internal use.
    if Path(raw).is_absolute():
        try:
            rel = Path(raw).relative_to(root).as_posix()
        except ValueError as exc:
            raise RuntimeError('PATH_GUARD_BLOCKED: path outside repository') from exc
    else:
        rel = raw.replace('\\', '/')
    if (not Path(raw).is_absolute() and PureWindowsPath(raw).drive) or rel.startswith('/'):
        raise RuntimeError('PATH_GUARD_BLOCKED: absolute/drive path')
    parts = rel.split('/')
    if not parts or any(p in ('', '.', '..') or ':' in p for p in parts):
        raise RuntimeError('PATH_GUARD_BLOCKED: traversal or invalid path segment')
    dest = root
    for part in parts:
        dest = dest / part
        if dest.is_symlink():
            raise RuntimeError('PATH_GUARD_BLOCKED: symlink in repository path')
    if not dest.resolve(strict=False).is_relative_to(root):
        raise RuntimeError('PATH_GUARD_BLOCKED: resolved path outside repository')
    return dest


def git_env() -> dict[str, str]:
    """Prevent inherited Git overrides from silently switching worktrees/refs."""
    return {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}


def validate_root(root_input: str | Path) -> Path:
    """Require exactly the top-level directory of a non-bare Git worktree."""
    raw = Path(os.path.abspath(os.fspath(root_input)))
    if raw != raw.resolve() or not raw.is_dir():
        raise RuntimeError('PATH_GUARD_BLOCKED: missing or symlinked repository root')
    # When the skill is installed in the conventional target-project layout,
    # bind its executable module to that same checkout. This prevents an
    # installed skill from being aimed at another *valid* Git repository.
    module = Path(os.path.abspath(__file__))
    marker = module.parts[-5:]
    if marker in (('.agents', 'skills', 'spec-to-code', 'scripts', 'path_guard.py'),
                  ('.agents', '.skills', 'spec-to-code', 'scripts', 'path_guard.py')):
        installed_root = module.parents[4]
        if installed_root != raw or module.resolve() != module:
            raise RuntimeError('PATH_GUARD_BLOCKED: installed skill belongs to a different checkout')
    # Ignore caller Git directory overrides: Git must discover this worktree itself.
    env = git_env()
    try:
        p = subprocess.run(
            ['git', 'rev-parse', '--show-toplevel', '--is-inside-work-tree', '--is-bare-repository'],
            cwd=raw, capture_output=True, text=True, timeout=6, check=False, env=env)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise RuntimeError('PATH_GUARD_BLOCKED: Git root verification unavailable') from exc
    values = p.stdout.splitlines()
    if (p.returncode != 0 or len(values) != 3 or values[1:] != ['true', 'false']
            or Path(values[0]).resolve() != raw):
        raise RuntimeError('PATH_GUARD_BLOCKED: require exact non-bare Git worktree root')
    for relative in MANAGED_PATHS:
        check_path(raw, relative)
    return raw
