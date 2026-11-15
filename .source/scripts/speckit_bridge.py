#!/usr/bin/env python3
"""Read-only bridge from official Spec Kit artifacts to Spec2Code context routing.

Never installs, initializes, invokes Spec Kit agent steps, modifies artifacts, or
reads specification body into a tool response. Requires local in-repo feature.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import path_guard as guard
import scope_io
import config_loader
import governance_schema as schema

SPECKIT_CONFIG = config_loader.load('speckit')
ARTIFACTS = tuple(SPECKIT_CONFIG['artifacts'])
STAGES = tuple(SPECKIT_CONFIG['stages'])
NEEDED = {stage: tuple(names) for stage,names in SPECKIT_CONFIG['stage_prerequisites'].items()}
MAX_POINTER_BYTES = SPECKIT_CONFIG['limits']['feature_pointer_bytes']
MAX_ARTIFACT_BYTES = SPECKIT_CONFIG['limits']['artifact_bytes']
MAX_TASK_IDS = SPECKIT_CONFIG['limits']['task_ids']
TASK_RE = re.compile(SPECKIT_CONFIG['task_id_pattern'], re.M)


def _safe_file(root: Path, path: Path) -> bool:
    """Disallow symlinks and directory escapes, including symlinked parents."""
    try:
        rel = path.relative_to(root)
    except ValueError:
        return False
    if not rel.parts:
        return False
    cur = root
    for part in rel.parts:
        cur = cur / part
        if cur.is_symlink() or (hasattr(cur, 'is_junction') and cur.is_junction()):
            return False
    return path.is_file()


def _feature_path(root: Path, value: str) -> Path:
    if not isinstance(value, str) or not value.strip() or len(value) > 240:
        raise RuntimeError('INVALID_FEATURE_POINTER')
    try:
        relative = schema.safe_path(value, suffixes=())
    except (ValueError, RuntimeError) as exc:
        raise RuntimeError('EXTERNAL_FEATURE_DIRECTORY_BLOCKED') from exc
    if not relative.startswith('specs/'):
        raise RuntimeError('EXTERNAL_FEATURE_DIRECTORY_BLOCKED')
    full = guard.check_path(root, relative)
    if not full.is_dir():
        raise RuntimeError('FEATURE_DIRECTORY_NOT_FOUND_OR_UNSAFE')
    return full


def active_feature(root: Path) -> Path | None:
    """Resolve the validated pointer for both inventory and workflow evidence."""
    override = os.environ.get('SPECIFY_FEATURE_DIRECTORY', '')
    pointer = root / '.specify/feature.json'
    if not _safe_file(root, pointer):
        if pointer.exists() or pointer.is_symlink() or guard._has_reparse_ancestor(pointer):
            raise RuntimeError('UNSAFE_FEATURE_POINTER')
        if override:
            raise RuntimeError('FEATURE_OVERRIDE_REQUIRES_POINTER')
        return None
    if pointer.stat().st_size > MAX_POINTER_BYTES:
        raise RuntimeError('FEATURE_POINTER_TOO_LARGE')
    try:
        data = json.loads(scope_io.read_bytes(root, pointer, max_bytes=MAX_POINTER_BYTES),
                          object_pairs_hook=config_loader._pairs_without_duplicates)
    except (UnicodeError, ValueError) as exc:
        raise RuntimeError('INVALID_FEATURE_POINTER_JSON') from exc
    if not isinstance(data, dict):
        raise RuntimeError('INVALID_FEATURE_POINTER')
    feature = _feature_path(root, data.get('feature_directory', ''))
    if override and _feature_path(root, override) != feature:
        raise RuntimeError('FEATURE_OVERRIDE_MISMATCH')
    return feature


def discover(root: Path, stage: str = 'status') -> dict:
    if stage not in STAGES:
        raise RuntimeError('UNKNOWN_SPECKIT_STAGE')
    root = guard.validate_root(root)
    feature = active_feature(root)
    specify_dir = guard.check_path(root, '.specify')
    if not specify_dir.is_dir():
        if stage != 'status':
            raise RuntimeError('SPEC_KIT_NOT_INITIALIZED')
        return {'status': 'NOT_INITIALIZED', 'cli_available': bool(shutil.which('specify')),
                'feature_directory': None, 'artifacts': {}, 'missing': []}
    if feature is None:
        if stage not in {'status', 'specify'}:
            raise RuntimeError('NO_ACTIVE_SPEC_KIT_FEATURE')
        return {'status': 'NO_ACTIVE_FEATURE', 'cli_available': bool(shutil.which('specify')),
                'feature_directory': None, 'artifacts': {}, 'missing': []}
    infos = {}
    needed = NEEDED[stage]
    for name in ARTIFACTS:
        path = guard.check_path(root, feature / name)
        if path.exists() and not _safe_file(root, path):
            raise RuntimeError('UNSAFE_SPEC_KIT_ARTIFACT')
        if not path.is_file():
            infos[name] = {'exists': False}
            continue
        size = path.stat().st_size
        if size > MAX_ARTIFACT_BYTES:
            raise RuntimeError('SPEC_KIT_ARTIFACT_TOO_LARGE')
        data = scope_io.read_bytes(root, path, max_bytes=MAX_ARTIFACT_BYTES)
        try:
            artifact_text = data.decode('utf-8-sig')
        except UnicodeError as exc:
            raise RuntimeError('INVALID_SPEC_KIT_ARTIFACT_ENCODING: ' + name) from exc
        if name in needed and not artifact_text.strip():
            raise RuntimeError('SPEC_KIT_GATE_BLOCKED: empty ' + name)
        infos[name] = {'exists': True, 'path': path.relative_to(root).as_posix(),
                       'sha256': hashlib.sha256(data).hexdigest(), 'size': len(data)}
        if name == 'tasks.md':
            ids = TASK_RE.findall(artifact_text)
            if len(ids) != len(set(ids)):
                raise RuntimeError('DUPLICATE_SPEC_KIT_TASK_ID')
            infos[name]['task_count'] = len(ids)
            infos[name]['task_ids_sample'] = ids[:MAX_TASK_IDS]
            infos[name]['task_ids_truncated'] = len(ids) > MAX_TASK_IDS
    missing = [name for name in needed if not infos[name]['exists']]
    if missing:
        raise RuntimeError('SPEC_KIT_GATE_BLOCKED: missing ' + ', '.join(missing))
    constitution = root / '.specify/memory/constitution.md'
    if constitution.exists() and not _safe_file(root, constitution):
        raise RuntimeError('UNSAFE_CONSTITUTION_PATH')
    return {'status': 'READY' if not missing else 'INCOMPLETE',
            'cli_available': bool(shutil.which('specify')), 'pointer_source': '.specify/feature.json',
            'feature_directory': feature.relative_to(root).as_posix(),
            'feature_id': feature.name, 'stage': stage, 'artifacts': infos, 'missing': missing,
            'constitution_path': constitution.relative_to(root).as_posix() if constitution.is_file() else None,
            'note': 'Static artifact inventory only; not human approval or full Spec Kit stage execution.'}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', default='.')
    parser.add_argument('--stage', choices=STAGES, default='status')
    args = parser.parse_args()
    try:
        result = discover(Path(args.root), args.stage)
        print(json.dumps(result, ensure_ascii=False, separators=(',', ':')))
        return 0
    except (RuntimeError, OSError) as exc:
        print('SPEC_KIT_BRIDGE_BLOCKED | ' + str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
