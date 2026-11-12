#!/usr/bin/env python3
"""Spec2Code spec-to-code session guard. Git is LOCAL ONLY; no network or secret reads.

Usage: python .agents/skills/spec-to-code/scripts/session_guard.py --root . start
       python ... session_guard.py --root . checkpoint
       python ... session_guard.py --root . record --paths .source/... --note '...' --requirement S2C-123
       python ... session_guard.py --root . finish
       python ... session_guard.py --root . status
       python ... session_guard.py --root . inspect --layer api
"""
from __future__ import annotations

import argparse
from collections import deque
import datetime as dt
import json
import posixpath
from pathlib import Path
import re
import subprocess
import sys
import uuid

import scan_infrastructure as infra
import architecture_tree as arch
import handoff_store as handoffs

SESSION_FILE = Path('.agents/state/session.json')
SESSION_EVENTS = Path('.agents/state/sessions.jsonl')
GRAPH_FILE = Path('.agents/state/system-graph.json')
SUMMARY_FILE = Path('.agents/state/layerSummary.md')
MATRIX_FILE = Path('.agents/state/impactMatrix.md')
# Session-scoped changes live in .handoffs/.details/; legacy root logs are not touched.
SCHEMA = 1
MAX_COMMITS = 200
MAX_CHANGE_LIST = 12

# Directed A -> B means A DEPENDS ON B. An edit to B can impact A.
LAYER_DEFS = [
    ('governance', 'Project requirements and governance', []),
    ('presentation', 'Frontend / presentation', []),
    ('api', 'HTTP API & controllers', []),
    ('application', 'Business logic', []),
    ('data', 'Repository / DataAccess', []),
    ('persistence', 'Database & migrations', []),
    ('security', 'Authentication & authorization', []),
    ('integrations', 'External adapters & services', []),
    ('delivery', 'Docker, CI/CD & deployment', []),
    ('quality', 'Automated tests', []),
]
LAYER_NAMES = {k: name for k, name, _ in LAYER_DEFS}
DEPENDENCIES = {k: deps for k, _, deps in LAYER_DEFS}


def git(root: Path, *argv: str, check: bool = True) -> str | None:
    try:
        p = subprocess.run(['git', *argv], cwd=root, text=True, capture_output=True,
                           timeout=8, check=False)
    except (OSError, subprocess.TimeoutExpired):
        if check:
            raise RuntimeError(f'Git command unavailable: {argv[0]}')
        return None
    if p.returncode != 0:
        if check:
            raise RuntimeError('Local git check failed: ' + ' '.join(argv[:3]))
        return None
    return p.stdout.strip()


def ensure_git_root(root: Path) -> str:
    top = git(root, 'rev-parse', '--show-toplevel')
    if Path(top).resolve() != root:
        raise RuntimeError('Run against repository root; refusing nested-directory scan')
    return git(root, 'rev-parse', 'HEAD')


def fingerprints(files: dict) -> dict:
    # Machine-only: model never needs this full map.
    return {p: (v.get('sha256') or f"{v.get('size')}:{v.get('mtime_ns')}:{v.get('digest_status')}")
            for p, v in files.items()}


def files_diff(before: dict, after: dict) -> list[dict]:
    return infra.diff_files(before, after)


def layer_for_path(p: str) -> str:
    return arch.layer_for_path(p)


def graph_for(root: Path, manifest: dict) -> dict:
    paths = manifest['files']
    cs = manifest['components']
    def matching(layer: str) -> list[str]:
        return sorted(p for p in paths if layer_for_path(p) == layer)

    nodes = []
    for key, name, _ in LAYER_DEFS:
        match = matching(key)
        # A directory containing only .gitkeep is scaffolding, not implementation.
        folders = {
            'presentation': ('web', 'frontend', 'client', '.source/web', 'app'),
            'api': ('api', 'backend', 'server', '.source/backend'),
            'application': ('src', 'services', 'backend', 'server', 'core', '.source/backend'),
            'data': ('data', 'backend', 'server', '.source/backend'),
            'persistence': ('migrations', 'database', 'backend', '.source/backend'),
            'integrations': ('integrations', 'adapters', 'backend', '.source/backend'),
            'quality': ('tests', 'test'),
        }
        folder = folders.get(key)
        present = bool(folder and any((root / candidate).is_dir() for candidate in folder))
        status = 'observed_files' if match else ('scaffold_only' if present else 'not_observed')
        if key == 'security' and cs['authentication']['status'] == 'code_indicators':
            status = 'code_indicators'
        if key == 'persistence' and cs['database']['status'] == 'code_indicators':
            status = 'code_indicators'
        if key == 'delivery' and cs['containers']['status'] == 'configured':
            status = 'configured_not_runtime_verified'
        if key == 'governance' and cs['policy_docs']['status'] == 'present':
            status = 'policy_files_present'
        nodes.append({'id': key, 'name': name, 'status': status,
                      'file_count': len(match), 'evidence_paths': match[:3]})

    # Universal graph: no assumed cross-layer dependencies. Only observed static links.
    edges = {}
    for path, facts in manifest.get('file_facts', {}).items():
        if path.endswith('.csproj'):
            source = layer_for_path(path)
            for ref in facts.get('project_references', []):
                resolved = posixpath.normpath(posixpath.join(posixpath.dirname(path),
                                                           ref.replace('\\', '/')))
                if resolved in paths:
                    target = layer_for_path(resolved)
                    if source != target:
                        edges[(source, target)] = {'from': source, 'to': target,
                                                   'kind': 'depends_on',
                                                   'evidence_level': 'observed_project_reference',
                                                   'evidence_path': path}
        if path.endswith(('/Program.cs', '/Startup.cs')) and layer_for_path(path) in {'api', 'application'}:
            if any('Identity' in x or 'Authentication' in x for x in facts.get('startup_signals', [])):
                edges[('api', 'security')] = {'from': 'api', 'to': 'security',
                                              'kind': 'depends_on',
                                              'evidence_level': 'observed_startup_indicator',
                                              'evidence_path': path}
    return {'schema_version': SCHEMA, 'evidence': 'local static discovery only',
            'nodes': nodes,
            'edges': sorted(edges.values(), key=lambda e: (e['from'], e['to']))}


def graph_dependencies(graph: dict) -> dict[str, list[dict]]:
    out = {k: [] for k in LAYER_NAMES}
    for e in graph['edges']:
        if e['from'] in out and e['to'] in out:
            out[e['from']].append(e)
    return out


def impact(changed: set[str], graph: dict) -> dict[str, dict[str, int]]:
    reverse = {k: [] for k in LAYER_NAMES}
    for e in graph['edges']:
        if e['from'] in reverse and e['to'] in reverse:
            reverse[e['to']].append(e['from'])
    table = {}
    for origin in sorted(changed):
        scores = {k: 0 for k in LAYER_NAMES}
        if origin not in LAYER_NAMES:
            continue
        scores[origin] = 3
        todo = deque([(origin, 0)])
        seen = {origin}
        while todo:
            cur, depth = todo.popleft()
            for next_node in reverse[cur]:
                if next_node in seen:
                    continue
                seen.add(next_node)
                nd = depth + 1
                scores[next_node] = max(1, 4 - nd)
                todo.append((next_node, nd))
        table[origin] = scores
    return table


def render_summary(graph: dict, *, changed: set[str]) -> str:
    deps = graph_dependencies(graph)
    rows = ['# Layer Summary', '',
            'Static evidence, not runtime proof. `*` means observed source reference/registration; otherwise policy-only link.', '',
            '| Layer | State | Files | Depends on |',
            '| --- | --- | ---: | --- |']
    for n in graph['nodes']:
        direct = ', '.join(e['to'] + ('*' if e['evidence_level'] != 'architecture_policy_only' else '')
                           for e in deps[n['id']]) or '—'
        rows.append(f"| `{n['id']}` | {n['status']} | {n['file_count']} | {direct} |")
    focus_scores = impact(changed, graph)
    focus = {layer for row in focus_scores.values() for layer, score in row.items() if score >= 2}
    rows += ['', 'Changed layers: ' + (', '.join(f'`{l}`' for l in sorted(changed)) or 'none'),
             'Read first (potential score ≥2): ' + (', '.join(f'`{l}`' for l in sorted(focus)) or 'none'),
             '', 'Inspect one layer: `session_guard.py inspect --layer <layer>`. Do not open full JSON by default.', '']
    return '\n'.join(rows)


def render_matrix(changed: set[str], graph: dict) -> str:
    # Matrix is impact propagation, not measured production risk.
    table = impact(changed, graph)
    lines = ['# Change Impact Matrix', '',
             'Potential impact from declared layer dependencies only. 3=direct/high, 2=one hop, 1=indirect, 0=none. **Not a runtime risk rating.**', '']
    if not table:
        return '\n'.join(lines + ['No changed layers in the latest scan.', ''])
    cols = [k for k, _, _ in LAYER_DEFS]
    lines += ['| Changed layer \\ Potentially affected | ' + ' | '.join(cols) + ' |',
              '| --- | ' + ' | '.join(['---:'] * len(cols)) + ' |']
    for origin, scores in table.items():
        lines.append('| ' + origin + ' | ' + ' | '.join(str(scores[k]) for k in cols) + ' |')
    return '\n'.join(lines + ['', 'Review only score 2–3 dependent layers unless task scope requires deeper analysis.', ''])


def write_if_changed(path: Path, data: str) -> None:
    if path.is_file() and path.read_text(encoding='utf-8') == data:
        return
    infra.atomic_text(path, data)


def collect(root: Path, old: dict | None, head: str, verify: bool = False) -> tuple[dict, list[dict]]:
    prior = (old or {}).get('files') or {}
    files = {}
    for p in infra.all_files(root):
        key = p.as_posix()
        files[key] = infra.describe_file(root, p, prior.get(key), verify=verify)
    facts = infra.extract_facts(root, files, old)
    components = infra.component_evidence(root, files, facts)
    delta = files_diff(prior, files) if old is not None else []
    return {'schema_version': infra.SCHEMA, 'status': 'VERIFIED_LOCAL_SNAPSHOT',
            'snapshot_at': infra.iso_now(),
            'git': {'head': head, 'branch': git(root, 'branch', '--show-current')},
            'files': files, 'file_facts': facts, 'components': components,
            'recent_changes': delta,
            'last_change_at': infra.iso_now() if delta else (old or {}).get('last_change_at')}, delta


def persist_scan(root: Path, manifest: dict, *, changed: set[str]) -> None:
    write_if_changed(root / infra.MANIFEST, json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    write_if_changed(root / infra.INDEX, infra.render_index(manifest))
    graph = graph_for(root, manifest)
    write_if_changed(root / GRAPH_FILE, json.dumps(graph, ensure_ascii=False, indent=2) + '\n')
    write_if_changed(root / SUMMARY_FILE, render_summary(graph, changed=changed))
    write_if_changed(root / MATRIX_FILE, render_matrix(changed, graph))
    # Materialize layer -> controller/component -> function summaries; no changes to actual source.
    arch.publish(root, manifest, graph, changed)


def append_log(path: Path, header: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as stream:
        if stream.tell() == 0:
            stream.write('# ' + header + '\n\n')
        stream.write(body.rstrip() + '\n\n')


def append_jsonl(path: Path, event: dict) -> None:
    """JSON Lines must contain ONLY valid JSON records; no Markdown headers."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as stream:
        stream.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + '\n')


def read_state(root: Path) -> dict | None:
    return infra.read_json(root / SESSION_FILE)


def save_state(root: Path, state: dict) -> None:
    infra.atomic_text(root / SESSION_FILE, json.dumps(state, ensure_ascii=False, indent=2) + '\n')


def commit_delta(root: Path, previous: str, current: str, own_session: str | None) -> dict:
    result = {'outside_commits': [], 'own_commits': [], 'outside_paths': set()}
    if previous == current:
        return result
    if git(root, 'merge-base', '--is-ancestor', previous, current, check=False) is None:
        raise RuntimeError('HISTORY_DIVERGED: HEAD not descendant of previous checkpoint. Manual reconciliation required')
    ids = git(root, 'rev-list', '--reverse', f'{previous}..{current}').splitlines()
    if len(ids) > MAX_COMMITS:
        raise RuntimeError(f'Git delta exceeds {MAX_COMMITS} commits. Manual review required')
    for sha in ids:
        message = git(root, 'log', '-1', '--format=%B', sha)
        match = re.search(r'^Spec2Code-Session:\s*(S2C-[A-Za-z0-9-]+)\s*$', message, re.M | re.I)
        trailer_id = match.group(1) if match else None
        if own_session is not None and trailer_id == own_session:
            result['own_commits'].append(sha)
        else:
            result['outside_commits'].append(sha)
            for p in git(root, 'diff-tree', '--root', '--no-commit-id', '--name-only', '-r', sha).splitlines():
                if infra.tracked_candidate(Path(p)):
                    result['outside_paths'].add(p)
    return result


def event_text(session_id: str, kind: str, changes: list[dict], shas: list[str], note: str) -> str:
    lines = [f'## {infra.iso_now()} | Session `{session_id}` | {kind}', '',
             f'- Source: {note}. Local Git only; remote not checked.',
             f'- Commits without this session trailer: {len(shas)}' +
             (f' ({", ".join(s[:12] for s in shas[:5])})' if shas else ''),
             f'- Observed scoped paths: {len(changes)}.', '']
    for c in changes[:MAX_CHANGE_LIST]:
        lines.append(f"- `{c['kind']}` `{c['path']}` (`{layer_for_path(c['path'])}`)")
    if len(changes) > MAX_CHANGE_LIST:
        lines.append(f'- ... {len(changes) - MAX_CHANGE_LIST} more paths. See machine manifest.')
    return '\n'.join(lines)


def inspect(root: Path, layer: str | None) -> int:
    if layer:
        layer = next((k for k, label in arch.LAYER_DIRS.items() if label.lower() == layer.lower()), layer.lower())
    graph = infra.read_json(root / GRAPH_FILE)
    if graph is None:
        raise RuntimeError('No graph snapshot. Run start first')
    if layer:
        nodes = [n for n in graph['nodes'] if n['id'] == layer]
        if not nodes:
            raise RuntimeError('Unknown layer: ' + layer)
        item = nodes[0]
        print(f"{layer} | {item['status']} | files={item['file_count']}")
        print('evidence: ' + ', '.join(item['evidence_paths']))
        print('depends_on: ' + ', '.join(e['to'] + '[' + e['evidence_level'] + ']' for e in graph['edges'] if e['from'] == layer))
        dependents = [e['from'] for e in graph['edges'] if e['to'] == layer]
        print('direct_consumers: ' + ', '.join(dependents))
    else:
        s = read_state(root)
        print('SESSION | ' + (s['id'] + ' | ' + s['status'] if s else 'NONE'))
        print('LAYERS | ' + ', '.join(f"{n['id']}:{n['status']}" for n in graph['nodes']))
    return 0


def run_start(root: Path, *, verify: bool = False) -> int:
    old_session = read_state(root)
    if old_session and old_session['status'] == 'ACTIVE':
        raise RuntimeError('ACTIVE_SESSION_EXISTS: finish or resolve before starting another session')
    head = ensure_git_root(root)
    prev = infra.read_json(root / infra.MANIFEST)
    if prev and prev.get('schema_version') != infra.SCHEMA:
        raise RuntimeError('Snapshot schema mismatch; preserve and migrate before proceeding')
    current, changes = collect(root, prev, head, verify=verify)
    previous_head = (prev or {}).get('git', {}).get('head')
    commit_info = commit_delta(root, previous_head, head, own_session=None) if previous_head else {
        'outside_commits': [], 'outside_paths': set(), 'own_commits': []}
    session_id = f"S2C-{dt.datetime.now(dt.timezone.utc):%Y%m%d-%H%M%S}-{uuid.uuid4().hex[:8].upper()}"
    changed_layers = {layer_for_path(x['path']) for x in changes}
    if prev and (changes or commit_info['outside_commits']):
        handoffs.append_event(root, session_id, 'visualChange',
                   event_text(session_id, 'OUT_OF_SESSION', changes,
                              commit_info['outside_commits'],
                              'differences since previous completed snapshot'))
    persist_scan(root, current, changed=changed_layers)
    state = {'schema_version': SCHEMA, 'id': session_id, 'status': 'ACTIVE',
             'started_at': infra.iso_now(), 'start_head': head, 'last_seen_head': head,
             'start_files': current['files'], 'last_seen_files': current['files'],
             'recorded_fingerprints': {}, 'recorded_paths': [],
             'outside_paths': [], 'startup_external_paths': sorted({c['path'] for c in changes} | commit_info['outside_paths']), 'record_count': 0}
    save_state(root, state)
    append_jsonl(root / SESSION_EVENTS,
                 {'event': 'START', 'session_id': session_id, 'at': state['started_at'],
                  'head': head, 'external_commits': len(commit_info['outside_commits']),
                  'out_of_session_delta': len(changes)})
    status = 'BASELINE' if prev is None else ('OUT_OF_SESSION_CHANGE' if changes or commit_info['outside_commits'] else 'NO_CHANGE')
    print(f'SESSION_START | {session_id} | {status} | files={len(current["files"])} | drift={len(changes)} | external_commits={len(commit_info["outside_commits"])}')
    print('Architecture: .summerize.md -> <Layer>/.summerize.md -> <Component>/.summerize.md -> exact function doc; read only relevant paths.')
    return 0


def refresh(root: Path, state: dict, *, print_result: bool = True, verify: bool = False) -> tuple[dict, list[dict], list[str]]:
    head = ensure_git_root(root)
    before = {'files': state['last_seen_files']}
    current, changes = collect(root, infra.read_json(root / infra.MANIFEST), head, verify=verify)
    # Scan manifest can be different from session last_seen_files after manual external scan.
    local_delta = files_diff(before['files'], current['files'])
    git_delta = commit_delta(root, state['last_seen_head'], head, own_session=state['id'])
    ext_shas = git_delta['outside_commits']
    ext_paths = set(git_delta['outside_paths'])
    external_changes = [c for c in local_delta if c['path'] in ext_paths]
    if ext_shas:
        handoffs.append_event(root, state['id'], 'visualChange',
                   event_text(state['id'], 'EXTERNAL_COMMIT_DURING_SESSION',
                              external_changes, ext_shas,
                              'incoming Git commits lack current Spec2Code-Session trailer'))
    state['outside_paths'] = sorted(set(state['outside_paths']) | ext_paths)
    state['last_seen_files'] = current['files']
    state['last_seen_head'] = head
    persist_scan(root, current, changed={layer_for_path(x['path']) for x in local_delta})
    save_state(root, state)
    if print_result:
        ambiguous = [c['path'] for c in local_delta
                     if c['path'] not in ext_paths and c['path'] not in state['recorded_paths']]
        print(f'CHECKPOINT | {state["id"]} | changed={len(local_delta)} | external_commits={len(ext_shas)} | unattributed_local={len(ambiguous)}')
        for p in ambiguous[:MAX_CHANGE_LIST]:
            print('REVIEW_UNATTRIBUTED | ' + p)
    return current, local_delta, ext_shas


def run_checkpoint(root: Path, *, verify: bool = False) -> int:
    state = read_state(root)
    if not state or state['status'] != 'ACTIVE':
        raise RuntimeError('No active session to checkpoint')
    refresh(root, state, verify=verify)
    return 0


def run_record(root: Path, paths: list[str], note: str, requirement: str) -> int:
    state = read_state(root)
    if not state or state['status'] != 'ACTIVE':
        raise RuntimeError('No active session to record')
    if not note.strip():
        raise RuntimeError('Specify nonempty --note for an audited implementation change')
    current, _, _ = refresh(root, state, print_result=False)
    baselines = fingerprints(state['start_files'])
    now = fingerprints(current['files'])
    previous_recorded = state['recorded_fingerprints']
    valid = []
    for text in paths:
        p = Path(text)
        if p.is_absolute() or '..' in p.parts:
            raise RuntimeError('Invalid path outside repository: ' + text)
        key = p.as_posix()
        if not infra.tracked_candidate(p):
            raise RuntimeError('File is not an authorized source/config candidate: ' + key)
        if baselines.get(key) == now.get(key):
            raise RuntimeError('No new difference from session start for ' + key)
        if previous_recorded.get(key) == now.get(key):
            raise RuntimeError('Change already recorded with this fingerprint: ' + key)
        if key in state['outside_paths']:
            raise RuntimeError('External commit touched this path; reconcile attribution manually: ' + key)
        valid.append(key)
    if len(set(valid)) != len(valid):
        raise RuntimeError('Duplicate --paths values are not permitted')
    state['recorded_paths'] = sorted(set(state['recorded_paths']) | set(valid))
    for p in valid:
        state['recorded_fingerprints'][p] = now.get(p, '<REMOVED>')
    state['record_count'] += 1
    save_state(root, state)
    event = [f'## {infra.iso_now()} | Session `{state["id"]}` | SPEC_TO_CODE', '',
             f'- Requirement: `{requirement or "UNSPECIFIED"}`',
             f'- Change note: {note.strip()}',
             '- Attribution: explicitly registered by the active agent session; this is not an external change.',
             '- Paths:']
    event += [f'  - `{p}` (`{layer_for_path(p)}`)' for p in valid]
    handoffs.append_event(root, state['id'], 'specChange', '\n'.join(event))
    arch.annotate_recorded_change(root, valid, note, requirement, state['id'], current['files'])
    print(f'SPEC_CHANGE_RECORDED | {state["id"]} | paths={len(valid)} | total_records={state["record_count"]}')
    return 0


def run_finish(root: Path) -> int:
    state = read_state(root)
    if not state or state['status'] != 'ACTIVE':
        raise RuntimeError('No active session to finish')
    current, _, ext_shas = refresh(root, state, print_result=False)
    session_delta = files_diff(state['start_files'], current['files'])
    final_fingerprints = fingerprints(current['files'])
    unclassified = [x for x in session_delta if
                    (x['path'] not in state['outside_paths'] and
                     (x['path'] not in state['recorded_paths'] or
                      state['recorded_fingerprints'].get(x['path']) !=
                      final_fingerprints.get(x['path'], '<REMOVED>')))]
    if unclassified:
        for x in unclassified[:MAX_CHANGE_LIST]:
            print('BLOCKED_UNCLASSIFIED | ' + x['path'])
        raise RuntimeError('Session has unclassified path changes. Record your own edits or reconcile external changes first')
    state['status'] = 'CLOSED'
    state['finished_at'] = infra.iso_now()
    state['changed_paths_count'] = len(session_delta)
    # Clear bulky per-file snapshots after session closure. Inventory remains canonical.
    for key in ('start_files', 'last_seen_files', 'recorded_fingerprints'):
        state.pop(key, None)
    save_state(root, state)
    append_jsonl(root / SESSION_EVENTS,
                 {'event': 'FINISH', 'session_id': state['id'],
                  'at': state['finished_at'], 'head': state['last_seen_head'],
                  'path_count': len(session_delta), 'record_count': state['record_count']})
    print(f'SESSION_FINISH | {state["id"]} | coded_paths={len(session_delta)} | spec_records={state["record_count"]} | CLOSED; merge --session-id {state["id"]} when ready')
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', default='.', help='Repository root; all Git checks are local')
    sub = p.add_subparsers(dest='action', required=True)
    for action in ('start', 'checkpoint', 'finish', 'status'):
        sp = sub.add_parser(action)
        if action in ('start', 'checkpoint'):
            sp.add_argument('--verify', action='store_true', help='Rehash eligible content rather than trust mtime/size cache')
    r = sub.add_parser('record')
    r.add_argument('--paths', nargs='+', required=True)
    r.add_argument('--note', required=True)
    r.add_argument('--requirement', default='')
    merge_parser = sub.add_parser('merge', help='Merge and safely remove exact pending session files after session FINISH')
    merge_parser.add_argument('--session-id', required=True)
    i = sub.add_parser('inspect')
    i.add_argument('--layer', help='Internal key (api/presentation) or folder label (API/Present)')
    args = p.parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        print('SESSION_FAILED | missing repository root', file=sys.stderr)
        return 2
    try:
        if args.action == 'start':
            return run_start(root, verify=args.verify)
        if args.action == 'checkpoint':
            return run_checkpoint(root, verify=args.verify)
        if args.action == 'record':
            return run_record(root, args.paths, args.note, args.requirement)
        if args.action == 'finish':
            return run_finish(root)
        if args.action == 'inspect':
            return inspect(root, args.layer)
        if args.action == 'merge':
            result = handoffs.merge(root, args.session_id)
            print('HANDOFF_MERGE | ' + args.session_id + ' | ' + result['message'] + ' | archived=' + str(result['merged']) + ' | removed=' + str(result['removed']))
            return 0
        s = read_state(root)
        print('SESSION | ' + (f'{s["id"]} | {s["status"]}' if s else 'NONE'))
        print('HEAD | ' + (git(root, 'rev-parse', '--short=12', 'HEAD', check=False) or 'unverified'))
        return 0
    except (OSError, RuntimeError, ValueError, KeyError) as ex:
        print('SESSION_FAILED | ' + str(ex), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
