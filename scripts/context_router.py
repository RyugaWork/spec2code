#!/usr/bin/env python3
"""Local-only, bounded, adaptive context routing for Spec2Code Spec-to-Code.

Reads v0.4 metadata/symbol graph, NOT application source or configuration contents.
Produces path-only .agents/state/context-pack.json; stdout stays compact.
Does not create/close sessions, commit, fetch, or touch handoff logs.
"""
from __future__ import annotations

import argparse
from collections import deque
import datetime as dt
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

import architecture_tree as arch
import scan_infrastructure as infra
import speckit_bridge
import path_guard as guard

POLICY = Path('.agents/state/context-policy.json')
PACK = Path('.agents/state/context-pack.json')
SESSION = Path('.agents/state/session.json')
GRAPH = Path('.agents/state/system-graph.json')
SYMBOLS = Path('.agents/state/symbol-cache.json')
DOC_STATE = Path('.agents/state/architecture-docs.json')
MODES = ('minimal', 'balanced', 'deep')
DEFAULT_POLICY = {
    'schema_version': 1,
    'default_mode': 'balanced',
    'budgets': {'minimal': 500, 'balanced': 1300, 'deep': 3300},
    'max_source_paths': {'minimal': 3, 'balanced': 8, 'deep': 16},
    'max_function_docs': {'minimal': 2, 'balanced': 5, 'deep': 12},
    'max_neighbor_hops': {'minimal': 0, 'balanced': 1, 'deep': 2},
    'high_risk_patterns': [
        'auth', 'authorization', 'identity', 'permission', 'role', 'csrf',
        'login', 'register', 'signup', 'credential', 'otp',
        'jwt', 'cookie', 'password', 'encrypt', 'decrypt', 'kms', 'pii',
        'medical', 'health', 'payment', 'billing', 'financial', 'transaction',
        'migration', 'schema', 'sql injection', 'sqli', 'concurrency',
        'data loss', 'destructive', 'backup', 'secret', 'production',
    ],
    'low_risk_patterns': [
        'documentation', 'readme', 'typo', 'copy', 'label', 'text', 'comment',
        'css', 'style', 'format', 'translation',
    ],
}


def read_json(root: Path, path: Path) -> dict:
    obj = infra.read_json(path, root=root)
    if not isinstance(obj, dict):
        raise RuntimeError(f'Missing or invalid state: {path}')
    return obj


def load_policy(root: Path) -> dict:
    path = root / POLICY
    if not path.exists():
        return DEFAULT_POLICY
    custom = read_json(root, path)
    if custom.get('schema_version') != 1:
        raise RuntimeError('context-policy.json schema mismatch; do not silently replace')
    allowed = set(DEFAULT_POLICY)
    if set(custom) - allowed:
        raise RuntimeError('Unsupported policy fields: ' + ', '.join(sorted(set(custom)-allowed)))
    merged = {**DEFAULT_POLICY, **custom}
    for key in ('budgets', 'max_source_paths', 'max_function_docs', 'max_neighbor_hops'):
        values = {**DEFAULT_POLICY[key], **custom.get(key, {})}
        if not all(isinstance(values[m], int) and 0 <= values[m] <= 20000 for m in MODES):
            raise RuntimeError('Invalid mode parameter: ' + key)
        merged[key] = values
    if merged['default_mode'] not in MODES:
        raise RuntimeError('Invalid default_mode')
    for key in ('high_risk_patterns', 'low_risk_patterns'):
        xs = merged[key]
        if not isinstance(xs, list) or len(xs) > 64 or not all(isinstance(s,str) and 2 <= len(s) <= 60 for s in xs):
            raise RuntimeError('Invalid ' + key)
    return merged


def safe_rel(root: Path, raw: str) -> str:
    value = raw.replace('\\', '/').strip()
    if not value or value.startswith('/') or ':' in value or '\x00' in value:
        raise RuntimeError('Expected safe repository-relative path')
    parts = PurePosixPath(value).parts
    if '..' in parts or any(x in ('.', '') for x in parts):
        raise RuntimeError('Unsafe path traversal')
    guard.check_path(root, value)
    return PurePosixPath(*parts).as_posix()


def safe_id(text: str) -> str:
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,79}', text):
        raise RuntimeError('Invalid task ID; expected 1-80 safe ASCII chars')
    return text


def terms(task: str) -> set[str]:
    return {w.lower() for w in re.findall(r'[A-Za-z][A-Za-z0-9_]{4,}', task) if w.lower() not in {
        'create', 'update', 'change', 'implement', 'current', 'feature', 'existing',
        'function', 'method', 'controller', 'system', 'spec2code', 'using', 'from',
        'with', 'will', 'should', 'please', 'component', 'backend', 'frontend',
        'review', 'apply', 'method', 'fixing', 'record', 'issue',
    }}


def classify(task: str, selected_paths: list[str], touched_layers: set[str],
             observed_outside: bool, policy: dict, requested: str) -> tuple[str,list[str]]:
    text = (task + ' ' + ' '.join(selected_paths)).lower()
    reasons = []
    high = [p for p in policy['high_risk_patterns'] if p.lower() in text]
    if high:
        auto = 'deep'
        reasons.append('high-risk topic/path: ' + ', '.join(high[:4]))
    elif observed_outside:
        auto = 'deep'
        reasons.append('external drift intersects selected source paths')
    elif len(touched_layers) >= 3 or len(selected_paths) >= 6:
        auto = 'deep'
        reasons.append('wide source/layer scope')
    elif len(touched_layers) >= 2 or len(selected_paths) >= 2:
        auto = 'balanced'
        reasons.append('multiple affected layers or files')
    elif any(p.lower() in text for p in policy['low_risk_patterns']) and len(selected_paths) <= 1:
        auto = 'minimal'
        reasons.append('bounded low-risk task')
    else:
        auto = policy['default_mode']
        reasons.append('standard or unresolved implementation risk')
    effective = auto if requested == 'auto' else requested
    if MODES.index(effective) < MODES.index(auto) and auto == 'deep' and (high or observed_outside or len(touched_layers) >= 3 or len(selected_paths) >= 6):
        reasons.append('manual downgrade blocked by high-risk/drift/wide-scope gate')
        effective = 'deep'
    elif requested != 'auto':
        reasons.append('explicit mode request: ' + requested)
    return effective, reasons


def layer_neighborhood(start: set[str], graph: dict, hops: int) -> list[str]:
    valid = {node.get('id') for node in graph.get('nodes', [])}
    connected = {x: set() for x in valid}
    for edge in graph.get('edges', []):
        a, b = edge.get('from'),edge.get('to')
        if a in connected and b in connected:
            connected[a].add(b)
            connected[b].add(a)
    seen = set(start) & valid
    frontier = deque((x,0) for x in sorted(seen))
    while frontier:
        cur, dist = frontier.popleft()
        if dist >= hops:
            continue
        for neighbor in sorted(connected.get(cur,())):
            if neighbor not in seen:
                seen.add(neighbor)
                frontier.append((neighbor, dist+1))
    return sorted(seen)


def route(root: Path, task_id: str, task: str, raw_paths: list[str],
          fn: str, requested: str, limit: int, speckit_stage: str = 'status') -> dict:
    root = guard.validate_root(root)
    task_id = safe_id(task_id)
    if len(task) > 2000 or not task.strip():
        raise RuntimeError('Task description must be non-empty and <= 2000 characters')
    policy = load_policy(root)
    session = read_json(root, root / SESSION)
    if session.get('status') != 'ACTIVE' or not session.get('id'):
        raise RuntimeError('ACTIVE_SESSION_REQUIRED: run session_guard.py start first')
    guard.assert_scope(root, session.get('repository_binding'))
    manifest = read_json(root, root / infra.MANIFEST)
    graph = read_json(root, root / GRAPH)
    symbols = read_json(root, root / SYMBOLS)
    docs = read_json(root, root / DOC_STATE)
    paths_by_manifest = set(manifest.get('files', {}))
    # Require a fresh local HEAD, never contact remote.
    import session_guard as sg
    current_head = sg.git(root, 'rev-parse', 'HEAD')
    manifest_head = manifest.get('git', {}).get('head', '')
    if (current_head != session.get('last_seen_head') or not isinstance(manifest_head,str)
            or len(manifest_head) < 7 or not current_head.startswith(manifest_head)):
        raise RuntimeError('STALE_GIT_HEAD: run session_guard.py checkpoint; never route stale state')
    paths = []
    if len(raw_paths) > 48:
        raise RuntimeError('Too many requested paths; split the task')
    for p in raw_paths:
        rel = safe_rel(root,p)
        if rel not in paths_by_manifest:
            raise RuntimeError('Path not present in scanned manifest: ' + rel)
        paths.append(rel)
    if not paths:
        t = terms(task)
        if fn:
            t |= terms(fn)
        if t:
            matches = []
            for path in paths_by_manifest:
                hay = path.lower() + ' ' + ' '.join(x.get('name','') for x in symbols.get(path,{}).get('functions',[])).lower()
                score = sum(1 for word in t if word in hay)
                if score:
                    matches.append((score,path))
            matches.sort(key=lambda x:(-x[0],x[1]))
            # Only choose a non-ambiguous high scoring candidate set.
            if matches:
                best = matches[0][0]
                paths = [p for score,p in matches if score == best][:8]
    paths = sorted(set(paths))
    for path in paths:
        guard.check_path(root, path)  # May originate from untrusted cached manifest.
    # A new unstaged edit doesn't move HEAD. Compare stat metadata for the exact
    # selected files, not all source bytes, to reject stale in-session routing.
    for path in paths:
        snap = manifest['files'].get(path,{})
        src = root / path
        if not src.is_file() or src.is_symlink():
            raise RuntimeError('STALE_SOURCE_PATH: checkpoint before routing ' + path)
        st = src.stat()
        if (snap.get('size') is not None and snap['size'] != st.st_size) or (snap.get('mtime_ns') is not None and snap['mtime_ns'] != st.st_mtime_ns):
            raise RuntimeError('STALE_SOURCE_METADATA: checkpoint before routing ' + path)
    layers = {arch.layer_for_path(p) for p in paths}
    outside = set(session.get('outside_paths', [])) | set(session.get('startup_external_paths', []))
    intersection = bool(outside & set(paths))
    effective, reasons = classify(task,paths,layers,intersection,policy,requested)
    cap = policy['max_source_paths'][effective]
    selected = paths[:cap]
    truncated = max(0,len(paths) - len(selected))
    restricted = [p for p in selected if infra.is_sensitive(Path(p).name)]
    readable = [p for p in selected if p not in restricted]
    if restricted:
        reasons.append('Sensitive configuration metadata-only; do not read contents')
        effective = 'deep'
        if requested in ('minimal', 'balanced'):
            reasons.append('manual downgrade blocked for sensitive configuration')
        cap = policy['max_source_paths'][effective]
    hop = policy['max_neighbor_hops'][effective]
    linked_layers = layer_neighborhood({arch.layer_for_path(p) for p in selected},graph,hop)
    if not linked_layers and not selected:
        reasons.append('no source match; supply --paths or exact function name before coding')
    doc_paths = []
    function_docs = []
    for layer in linked_layers:
        d = arch.LAYER_DIRS.get(layer)
        if d and (root / d / arch.SUMMARY_NAME).is_file():
            doc_paths.append(f'{d}/{arch.SUMMARY_NAME}')
    doc_state = docs.get('functions',{})
    selected_set = set(readable)
    for key,item in sorted(doc_state.items()):
        if key.split('#',1)[0] in selected_set:
            p = item.get('document','')
            if p and guard.check_path(root, p).is_file():
                if fn and fn.lower() not in key.lower():
                    continue
                function_docs.append(p)
    function_docs = function_docs[:policy['max_function_docs'][effective]]
    comps = {str(PurePosixPath(p).parent / arch.SUMMARY_NAME) for p in function_docs}
    component_docs = sorted(p for p in comps if guard.check_path(root, p).is_file())
    missing = (len(paths) == 0)
    pack = {
        'schema_version': 1,
        'session_id': session['id'],
        'task_id': task_id,
        'git_head': current_head,
        'workspace_fingerprint': hashlib.sha256(
            json.dumps(session['repository_binding'], sort_keys=True).encode('utf-8')
        ).hexdigest()[:16],
        'request_mode': requested,
        'effective_mode': effective,
        'routing_status': 'NEEDS_EXPLICIT_PATH' if missing else ('METADATA_ONLY' if not readable else ('TRUNCATED' if truncated else 'READY')),
        'reasons': reasons,
        'token_budget_target': min(policy['budgets'][effective],limit) if limit else policy['budgets'][effective],
        'source_paths': readable,
        'metadata_only_paths': restricted,
        'direct_layers': sorted({arch.layer_for_path(p) for p in selected}),
        'linked_layers': linked_layers,
        'layer_summary_paths': doc_paths,
        'component_summary_paths': component_docs,
        'function_document_paths': function_docs,
        'root_summary_path': '.summerize.md' if not missing and (root/'.summerize.md').is_file() else None,
        'spec_lookup': '.specify/feature.json (or explicit SPECIFY_FEATURE_DIRECTORY); resolved by speckit_bridge',
        'unselected_matches': truncated,
        'notes': [
            'Path-only routing. Read no files not necessary for current task.',
            'Potential dependencies only; missing static edge does not imply safety.',
            'Use approved business and security requirements independent of token budget.',
        ],
    }
    # Spec Kit artifacts are referenced by path/hash only; no duplicated spec body.
    pack['spec_kit'] = speckit_bridge.discover(root, speckit_stage)
    # Do not include task free text in machine file; it could contain PII/secrets.
    infra.atomic_text(root / PACK, json.dumps(pack, ensure_ascii=False, indent=2) + '\n', root=root)
    return pack


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', default='.', help='Repository root')
    p.add_argument('--task-id', required=True)
    p.add_argument('--task', required=True)
    p.add_argument('--mode', choices=('auto',*MODES), default='auto')
    p.add_argument('--paths', nargs='*', default=[], metavar='PATH')
    p.add_argument('--function', default='', help='Optional exact or distinctive function name for narrow selection')
    p.add_argument('--speckit-stage', choices=speckit_bridge.STAGES, default='status',
                   help='Validate active Spec Kit feature and required artifacts before stage (implement = spec/plan/tasks)')
    p.add_argument('--token-limit', type=int, default=0, help='Override lower than default target budget')
    args = p.parse_args()
    root = Path(args.root).resolve()
    try:
        if args.token_limit < 0:
            raise RuntimeError('Token budget must be nonnegative')
        result = route(root,args.task_id,args.task,args.paths,args.function,args.mode,args.token_limit,args.speckit_stage)
        print(f"CONTEXT_ROUTE | {result['task_id']} | session={result['session_id']} | {result['effective_mode'].upper()} | {result['routing_status']} | source={len(result['source_paths'])} | layers={','.join(result['direct_layers']) or '-'} | target={result['token_budget_target']} tokens")
        print('CONTEXT_PACK | .agents/state/context-pack.json | ' + '; '.join(result['reasons'][:2]))
        if result['routing_status'] == 'NEEDS_EXPLICIT_PATH':
            return 3
        return 0
    except (OSError, RuntimeError, KeyError, ValueError) as exc:
        print('CONTEXT_ROUTE_FAILED | ' + str(exc),file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
