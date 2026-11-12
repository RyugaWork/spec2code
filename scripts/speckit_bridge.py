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

ARTIFACTS = ('spec.md', 'plan.md', 'tasks.md')
STAGES = ('status', 'specify', 'plan', 'tasks', 'analyze', 'implement', 'converge')
NEEDED = {
    'status': (), 'specify': (), 'plan': ('spec.md',),
    'tasks': ('spec.md', 'plan.md'),
    'analyze': ARTIFACTS, 'implement': ARTIFACTS, 'converge': ARTIFACTS,
}
MAX_POINTER_BYTES = 8192
MAX_ARTIFACT_BYTES = 1024 * 1024
MAX_TASK_IDS = 24
TASK_RE = re.compile(r'^\s*-\s*\[[ xX]\]\s*(?:\*\*)?(T\d{3,6})\b', re.M)


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
        if cur.is_symlink():
            return False
    return path.is_file()


def _feature_path(root: Path, value: str) -> Path:
    if not isinstance(value, str) or not value.strip() or len(value) > 240:
        raise RuntimeError('INVALID_FEATURE_POINTER')
    path = Path(value)
    if path.is_absolute() or '..' in path.parts or path.parts[0] in {'.', ''}:
        raise RuntimeError('EXTERNAL_FEATURE_DIRECTORY_BLOCKED')
    full = root / path
    if not full.resolve().is_relative_to(root) or not full.is_dir():
        raise RuntimeError('FEATURE_DIRECTORY_NOT_FOUND_OR_UNSAFE')
    if not full.is_relative_to(root) or any((root.joinpath(*path.parts[:i])).is_symlink()
                                              for i in range(1, len(path.parts) + 1)):
        raise RuntimeError('SYMLINKED_FEATURE_DIRECTORY_BLOCKED')
    return full


def discover(root: Path, stage: str = 'status') -> dict:
    if stage not in STAGES:
        raise RuntimeError('UNKNOWN_SPECKIT_STAGE')
    root = root.resolve()
    if not (root / '.specify').is_dir():
        if stage != 'status':
            raise RuntimeError('SPEC_KIT_NOT_INITIALIZED')
        return {'status': 'NOT_INITIALIZED', 'cli_available': bool(shutil.which('specify')),
                'feature_directory': None, 'artifacts': {}, 'missing': []}
    if (root / '.specify').is_symlink():
        raise RuntimeError('UNSAFE_SPECKIT_DIRECTORY')
    pointer = root / '.specify/feature.json'
    # A caller may use an explicit env override, but never allow escaping the workspace.
    override = os.environ.get('SPECIFY_FEATURE_DIRECTORY', '')
    if override:
        source = 'SPECIFY_FEATURE_DIRECTORY'
        feature_text = override
    elif _safe_file(root, pointer):
        if pointer.stat().st_size > MAX_POINTER_BYTES:
            raise RuntimeError('FEATURE_POINTER_TOO_LARGE')
        try:
            data = json.loads(pointer.read_text(encoding='utf-8'))
        except (UnicodeError, json.JSONDecodeError) as exc:
            raise RuntimeError('INVALID_FEATURE_POINTER_JSON') from exc
        if not isinstance(data, dict):
            raise RuntimeError('INVALID_FEATURE_POINTER')
        feature_text = data.get('feature_directory', '')
        source = '.specify/feature.json'
    else:
        if pointer.exists():
            raise RuntimeError('UNSAFE_FEATURE_POINTER')
        if stage != 'status' and stage != 'specify':
            raise RuntimeError('NO_ACTIVE_SPEC_KIT_FEATURE')
        return {'status': 'NO_ACTIVE_FEATURE', 'cli_available': bool(shutil.which('specify')),
                'feature_directory': None, 'artifacts': {}, 'missing': []}
    feature = _feature_path(root, feature_text)
    infos = {}
    for name in ARTIFACTS:
        path = feature / name
        if path.exists() and not _safe_file(root, path):
            raise RuntimeError('UNSAFE_SPEC_KIT_ARTIFACT')
        if not path.is_file():
            infos[name] = {'exists': False}
            continue
        size = path.stat().st_size
        if size > MAX_ARTIFACT_BYTES:
            raise RuntimeError('SPEC_KIT_ARTIFACT_TOO_LARGE')
        data = path.read_bytes()
        infos[name] = {'exists': True, 'path': path.relative_to(root).as_posix(),
                       'sha256': hashlib.sha256(data).hexdigest(), 'size': size}
        if name == 'tasks.md':
            text = data.decode('utf-8', errors='replace')
            ids = TASK_RE.findall(text)
            infos[name]['task_count'] = len(ids)
            infos[name]['task_ids_sample'] = ids[:MAX_TASK_IDS]
            infos[name]['task_ids_truncated'] = len(ids) > MAX_TASK_IDS
    needed = NEEDED[stage]
    missing = [name for name in needed if not infos[name]['exists']]
    if missing:
        raise RuntimeError('SPEC_KIT_GATE_BLOCKED: missing ' + ', '.join(missing))
    constitution = root / '.specify/memory/constitution.md'
    if constitution.exists() and not _safe_file(root, constitution):
        raise RuntimeError('UNSAFE_CONSTITUTION_PATH')
    return {'status': 'READY' if not missing else 'INCOMPLETE',
            'cli_available': bool(shutil.which('specify')), 'pointer_source': source,
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
