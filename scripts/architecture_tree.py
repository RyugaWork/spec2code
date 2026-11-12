#!/usr/bin/env python3
"""Create bounded, lazy, evidence-based hierarchical architecture documentation.

Only used by session_guard (never invoke as the writer independently). Generated
architecture documents are NOT source code and do not claim runtime behavior.
"""
from __future__ import annotations

from collections import deque
import hashlib
import json
import posixpath
from pathlib import Path
import re
import os
from typing import Any

import scan_infrastructure as infra
import path_guard as guard

LAYER_DIRS = {
    'governance': 'Governance',
    'presentation': 'Present',
    'api': 'API',
    'application': 'Application',
    'data': 'DataAccess',
    'persistence': 'Persistence',
    'security': 'Security',
    'integrations': 'Integrations',
    'delivery': 'Delivery',
    'quality': 'Quality',
}
SUMMARY_NAME = '.summerize.md'  # Owner-selected spelling, deliberately retained.
STATE_FILE = Path('.agents/state/architecture-docs.json')
SYMBOL_CACHE = Path('.agents/state/symbol-cache.json')
GENERATED = '<!-- spec2code:managed-architecture v1 -->'
VERSION = 1
MAX_COMPONENTS = 300
MAX_METHODS = 1200
MAX_SOURCE_BYTES = 256 * 1024
MAX_VISIBLE_COMPONENTS = 16
MAX_VISIBLE_FUNCTIONS = 18


def safe_name(name: str) -> str:
    """Safe, portable component path; no path separators or dot traversal."""
    s = re.sub(r'[^A-Za-z0-9_-]', '_', name.strip())[:52].strip('_.-')
    if not s or s.lower() in {'con','nul','prn','aux','com1','lpt1'}:
        return 'Component_' + hashlib.sha256(name.encode()).hexdigest()[:8]
    return s


def layer_for_path(p: str) -> str:
    """Conservative path-based classification with no project-specific names."""
    s = p.lower().replace('\\', '/')
    name = Path(s).name
    if s in {'agents.md', 'readme.md', 'pyproject.toml'} or s.startswith(('.agents/.documents/', 'specs/')):
        return 'governance'
    if s.startswith(('tests/', 'test/')) or '/tests/' in s or name.startswith('test_') or name.endswith(('.test.ts', '.spec.ts', 'test.java')):
        return 'quality'
    if s.startswith('.github/') or 'compose' in name or name == 'dockerfile' or s.endswith(('.tf', '.tfvars')):
        return 'delivery'
    if any(t in s for t in ('/security/', '/identity/', '/authentication/', '/auth/')):
        return 'security'
    if any(t in s for t in ('/migrations/', '/database/', '/persistence/')) or s.endswith('.sql'):
        return 'persistence'
    if any(t in s for t in ('/repository/', '/repositories/', '/dataaccess/', '/data/', '/dao/')) or re.search(r'/[^/]+\.dataaccess/',s):
        return 'data'
    if any(t in s for t in ('/integrations/', '/infrastructure/', '/adapters/', '/external/')) or re.search(r'/[^/]+\.infrastructure/',s):
        return 'integrations'
    if any(t in s for t in ('/controllers/', '/routes/', '/endpoints/')) or name.endswith('controller.cs') or re.search(r'/(?:[^/]+\.)?api/', s):
        # Web framework routes can be presentation; API folders remain API.
        if s.startswith(('web/', 'frontend/', 'client/', '.source/web/')):
            return 'presentation'
        return 'api'
    if s.startswith(('web/', 'frontend/', 'client/', '.source/web/', '.source/frontend/')):
        return 'presentation'
    if s.startswith(('api/', '.source/backend/')) and ('/api/' in s or name in ('program.cs','startup.cs')):
        return 'api'
    if s.startswith(('app/', 'src/')) and Path(s).suffix.lower() in {'.tsx', '.jsx', '.vue', '.svelte', '.css', '.scss'}:
        return 'presentation'
    if any(t in s for t in ('/services/', '/domain/', '/business/', '/usecases/')):
        return 'application'
    if s.startswith(('.agents/', '.specify/')):
        return 'governance'
    if s.startswith(('backend/', 'server/', 'api/', '.source/backend/', 'src/', 'app/', 'lib/', 'core/', 'services/')):
        return 'application'
    return 'governance' if name.endswith('.md') else 'delivery'

def observed_component(path: str, layer: str) -> bool:
    p = Path(path)
    if layer == 'api':
        return p.name.endswith('Controller.cs') or p.suffix.lower() in {'.py','.go','.java','.ts','.js'}
    if layer == 'presentation':
        return p.suffix.lower() in {'.tsx', '.jsx', '.ts', '.js', '.vue', '.svelte', '.py'}
    if layer in {'application', 'data', 'persistence', 'security', 'integrations'}:
        return p.suffix.lower() in {'.cs', '.py', '.go', '.rs', '.java', '.kt', '.rb', '.php'} and not p.name.endswith(('.g.cs', '.Designer.cs'))
    if layer == 'quality':
        return p.suffix.lower() in {'.cs', '.ts', '.tsx', '.js', '.jsx', '.py', '.go', '.java'}
    if layer in {'delivery', 'governance'}:
        if path.startswith('specs/'):
            return False
        return p.suffix.lower() in {'.md', '.json', '.yml', '.yaml'} or p.name in {'AGENTS.md','README.md','Dockerfile'}
    return False


def component_name(path: str, layer: str) -> str:
    p = Path(path)
    if layer == 'presentation' and p.stem.lower() in {'page', 'layout', 'index', 'route'}:
        dirname = p.parent.name if p.parent.name not in {'src', 'app', 'pages'} else 'Root'
        return safe_name(dirname + '_' + p.stem.capitalize())
    return safe_name(p.stem)


def extract_symbols(root: Path, path: str, layer: str, fingerprint: str, cached: dict | None) -> dict:
    if cached and cached.get('fingerprint') == fingerprint:
        return cached
    result = {'fingerprint': fingerprint, 'functions': [], 'imports': [], 'source_status': 'unparsed'}
    p = root / path
    if p.stat().st_size > MAX_SOURCE_BYTES or infra.is_sensitive(p.name) or p.is_symlink():
        result['source_status'] = 'metadata_only'
        return result
    source = p.read_text(encoding='utf-8', errors='replace')
    functions = []
    imports = []
    if p.suffix.lower() == '.cs':
        # Declaration-only parsing; avoids inventing method behavior.
        method_re = re.compile(r'^\s*(?:(?:public|private|protected|internal|static|async|virtual|override|sealed|new|partial)\s+){1,6}'
                               r'(?:[\w.<>?,\[\]]+\s+)+(?P<name>[A-Za-z_]\w*)\s*\(', re.M)
        for match in method_re.finditer(source):
            n = match.group('name')
            if n not in {'if', 'for', 'foreach', 'while', 'switch', 'catch', 'using'}:
                functions.append({'name': n, 'line': source.count('\n', 0, match.start()) + 1,
                                  'kind': 'C# method (declaration heuristic)'})
    elif p.suffix.lower() == '.py':
        for match in re.finditer(r'^\s*(?:async\s+)?def\s+(?P<name>[A-Za-z_]\w*)\s*\(', source, re.M):
            functions.append({'name':match.group('name'), 'line':source.count('\n',0,match.start())+1, 'kind':'Python function/method (declaration heuristic)'})
    elif p.suffix.lower() in {'.ts', '.tsx', '.js', '.jsx'}:
        js_patterns = [
            (re.compile(r'^\s*(?:export\s+)?(?:default\s+)?(?:async\s+)?function\s+(?P<name>[A-Za-z_]\w*)\s*\(', re.M), 'function'),
            (re.compile(r'^\s*(?:export\s+)?(?:const|let)\s+(?P<name>[A-Za-z_]\w*)\s*=\s*(?:async\s*)?(?:\([^\n]{0,140}?\)|[A-Za-z_]\w*)\s*=>', re.M), 'arrow function'),
        ]
        for rx, kind in js_patterns:
            for match in rx.finditer(source):
                functions.append({'name': match.group('name'), 'line': source.count('\n', 0, match.start()) + 1,
                                  'kind': kind})
        # Only imports into local source files are considered possible controller connections.
        for match in re.finditer(r'\b(?:from\s*|import\s*\()\s*[\'\"](?P<path>\.[^\'\"]{1,150})[\'\"]', source):
            imports.append(match.group('path'))
    clean = []
    seen = set()
    for fn in sorted(functions, key=lambda x: (x['line'], x['name'])):
        key = (fn['name'], fn['line'])
        if key not in seen:
            clean.append(fn)
            seen.add(key)
    result.update({'functions': clean[:200], 'imports': sorted(set(imports))[:200], 'source_status': 'lexical_evidence'})
    return result


def evidence_graph(root: Path, manifest: dict, graph: dict, old_cache: dict) -> tuple[dict, dict]:
    files = manifest['files']
    symbols = {}
    components = {}
    by_path = {}
    for path in sorted(files):
        layer = layer_for_path(path)
        if not observed_component(path, layer):
            continue
        base = component_name(path, layer)
        name = base
        used_key = (layer, name)
        if used_key in components:
            name = base[:45] + '_' + hashlib.sha256(path.encode()).hexdigest()[:7]
            used_key = (layer, name)
        fp = files[path].get('sha256') or str(files[path].get('size')) + ':' + str(files[path].get('mtime_ns'))
        syms = extract_symbols(root, path, layer, fp, old_cache.get(path))
        symbols[path] = syms
        if len(components) >= MAX_COMPONENTS:
            raise RuntimeError(f'Component cap {MAX_COMPONENTS} exceeded; refine scan scope')
        comp = {'name': name, 'layer': layer, 'source': path, 'fingerprint': fp,
                'functions': syms['functions'], 'links': [], 'source_status': syms['source_status']}
        components[used_key] = comp
        by_path[path] = used_key
    source_paths = set(by_path)
    for (layer, name), comp in components.items():
        for import_path in symbols[comp['source']]['imports']:
            d = posixpath.normpath(posixpath.join(posixpath.dirname(comp['source']), import_path))
            target = next((x for x in (d, d+'.tsx', d+'.ts', d+'.jsx', d+'.js',
                                       d+'/index.tsx', d+'/index.ts', d+'/index.jsx', d+'/index.js') if x in source_paths), None)
            if target:
                target_layer, target_name = by_path[target]
                if target_layer == layer and target_name != name:
                    comp['links'].append({'to': target_name, 'kind': 'observed_relative_import', 'source': target})
    total_funcs = sum(len(c['functions']) for c in components.values())
    if total_funcs > MAX_METHODS:
        raise RuntimeError(f'Function-document cap {MAX_METHODS} exceeded; scope more narrowly')
    return components, symbols


def guarded_write(root: Path, path: Path, content: str) -> None:
    guard.check_path(root, path)
    if path.is_symlink():
        raise RuntimeError(f'Refusing symlinked architecture file: {path}')
    if path.exists():
        if not path.is_file():
            raise RuntimeError(f'Architecture document path occupied: {path}')
        old = path.read_text(encoding='utf-8')
        if not old.startswith(GENERATED):
            raise RuntimeError(f'Refusing to overwrite non-managed architecture document: {path}')
        if old == content:
            return
    parent = path.parent
    while parent != parent.parent:
        if parent.is_symlink():
            raise RuntimeError(f'Refusing symlinked architecture directory: {parent}')
        parent = parent.parent
    infra.atomic_text(path, content, root=root)


def graph_distance(src: str, target: str, edges: list[dict]) -> int | None:
    neighbors = {}
    for e in edges:
        neighbors.setdefault(e['from'], []).append(e['to'])
    q = deque([(src, 0)])
    seen = set()
    while q:
        u, n = q.popleft()
        if u == target:
            return n
        if u in seen:
            continue
        seen.add(u)
        q.extend((v, n+1) for v in neighbors.get(u, []) if v not in seen)
    return None


def matrix_row_matrix(names: list[str], links: set[tuple[str, str]], title: str) -> list[str]:
    out = [f'### {title}', '', 'Rows depend on columns. `D` = direct observed link; `-` = not observed.', '']
    show = names[:MAX_VISIBLE_COMPONENTS]
    if len(names) > len(show):
        out.append(f'Matrix limited to first {len(show)}/{len(names)} components. Use machine index for full set.\n')
    if not show:
        return out + ['No source components discovered.', '']
    out += ['| Component | ' + ' | '.join('`'+x+'`' for x in show) + ' |', '| --- | ' + ' | '.join([':---:']*len(show)) + ' |']
    for a in show:
        out.append('| `' + a + '` | ' + ' | '.join('·' if a == b else ('D' if (a,b) in links else '-') for b in show) + ' |')
    return out + ['']


def render_root(graph: dict, manifest: dict, focus: set[str], counts: dict[str, int]) -> str:
    nodes = {n['id']: n for n in graph['nodes']}
    keys = list(LAYER_DIRS)
    out = [GENERATED, '# Architecture Routing Matrix', '',
           'Local static evidence only. Documents under root layer folders are **architecture indexes**, not application code.',
           f"- Git HEAD: `{manifest['git']['head']}`; branch: `{manifest['git']['branch']}`",
           f'- Changed layers in last scan: {", ".join("`"+LAYER_DIRS[x]+"`" for x in sorted(focus)) or "none"}',
           '', '## Layer routing', '', '| Layer | Source status | Controllers / components | Direct dependencies |', '| --- | --- | ---: | --- |']
    for k in keys:
        deps = [e['to'] for e in graph['edges'] if e['from']==k]
        out.append(f"| [`{LAYER_DIRS[k]}/`](./{LAYER_DIRS[k]}/{SUMMARY_NAME}) | {nodes[k]['status']} | {counts.get(k,0)} | {', '.join(LAYER_DIRS[d] for d in deps) or '—'} |")
    out += ['', '## Layer pathing matrix', '',
            'Row = dependent layer, column = dependency. `D` = direct, `T` = transitive, `·` = same layer, `-` = no declared path. Policy-only connections are **not** proof of runtime wiring.', '',
            '| From / To | ' + ' | '.join(LAYER_DIRS[x] for x in keys) + ' |',
            '| --- | ' + ' | '.join([':---:'] * len(keys)) + ' |']
    for a in keys:
        vals=[]
        for b in keys:
            d=graph_distance(a,b,graph['edges'])
            vals.append('·' if a==b else ('D' if d==1 else ('T' if d is not None else '-')))
        out.append('| ' + LAYER_DIRS[a] + ' | ' + ' | '.join(vals) + ' |')
    out += ['', '## Graph pathing', '', '```mermaid', 'flowchart LR']
    for k in keys:
        out.append(f'  {k}["{LAYER_DIRS[k]}"]')
    for e in graph['edges']:
        edge_type = '==>' if e['evidence_level'] != 'architecture_policy_only' else '-.->'
        out.append(f"  {e['from']} {edge_type} {e['to']}")
    out += ['```', '', 'Solid arrows indicate static evidence; dotted arrows indicate documented intended dependencies.',
            'Read the linked layer summary, then one component summary, then only the required function document. Do not load the entire tree.', '']
    return '\n'.join(out)


def render_layer(layer: str, comps: list[dict], graph: dict, focus: set[str]) -> str:
    name = LAYER_DIRS[layer]
    out=[GENERATED, '# '+name+' — Layer Architecture', '',
         f'- Source layer: `{layer}`',
         f'- Changed in last scan: {"YES" if layer in focus else "NO"}',
         f'- Discovered source components: {len(comps)} (not runtime verified)',
         '', '## Linked layers', '']
    dependencies=[e for e in graph['edges'] if e['from']==layer]
    consumers=[e for e in graph['edges'] if e['to']==layer]
    out += ['- Depends on: '+(', '.join(f'[`{LAYER_DIRS[e["to"]]}`](../{LAYER_DIRS[e["to"]]}/{SUMMARY_NAME}) [{e["evidence_level"]}]' for e in dependencies) or 'none'),
            '- Used by: '+(', '.join(f'`{LAYER_DIRS[e["from"]]}`' for e in consumers) or 'none'),
            '', '## Controller / component index', '', '| Component | Source | Functions indexed | Connections |', '| --- | --- | ---: | --- |']
    for c in comps[:80]:
        out.append(f'| [`{c["name"]}`](./{c["name"]}/{SUMMARY_NAME}) | `{c["source"]}` | {len(c["functions"])} | {len(c["links"])} observed |')
    if len(comps)>80:
        out.append(f'| … | {len(comps)-80} more (use machine index) | | |')
    if not comps:
        out += ['| None observed | — | 0 | — |', '',
                'No controller/function docs were invented for an absent or scaffold-only layer.']
    links={(c['name'],l['to']) for c in comps for l in c['links']}
    out += [''] + matrix_row_matrix([c['name'] for c in comps], links, 'Component connection matrix')
    out += ['**Caution:** A missing direct link may mean static analysis did not identify it, not that the components are independent.', '']
    return '\n'.join(out)


def function_filename(c: dict, fn: dict) -> str:
    same = [x for x in c['functions'] if x['name'] == fn['name']]
    suffix = f'_L{fn["line"]}' if len(same) > 1 else ''
    return f'.{c["name"]}.{safe_name(fn["name"])}{suffix}.md'


def render_component(c: dict, all_comps: list[dict]) -> str:
    out=[GENERATED, '# '+c['name']+' — Component Architecture', '',
         f'- Layer: `{LAYER_DIRS[c["layer"]]}`',
         f'- Source: `{c["source"]}`',
         f'- Source fingerprint: `{c["fingerprint"][:16]}`',
         f'- Source evidence: `{c["source_status"]}`', '',
         '## Function routing', '', '| Function | Declaration line | Evidence |', '| --- | ---: | --- |']
    for fn in c['functions'][:MAX_VISIBLE_FUNCTIONS]:
        filename=function_filename(c, fn)
        out.append(f'| [`{fn["name"]}`](./{filename}) | {fn["line"]} | {fn["kind"]} |')
    if len(c['functions'])>MAX_VISIBLE_FUNCTIONS:
        out.append(f'| … | +{len(c["functions"])-MAX_VISIBLE_FUNCTIONS} | More documents indexed locally |')
    if not c['functions']:
        out.append('| None indexed | — | No supported declaration found |')
    out += ['', '## Observed component links', '']
    if c['links']:
        out += [f'- `{c["name"]}` → `{l["to"]}` (`{l["kind"]}`, `{l["source"]}`)' for l in c['links'][:MAX_VISIBLE_COMPONENTS]]
    else:
        out += ['- No static relative-import links identified. This does not prove isolation.']
    out += ['', 'Architecture descriptions require reviewing the referenced source/spec; this document does not infer function behavior.', '']
    return '\n'.join(out)


def function_key(c: dict, fn: dict) -> str:
    return c['source'] + '#' + fn['name'] + ':' + str(fn['line'])


def render_function(c: dict, fn: dict, version: int, change: str) -> str:
    return '\n'.join([GENERATED, '# '+c['name']+'.'+fn['name'], '',
                      f'- Layer: `{LAYER_DIRS[c["layer"]]}`',
                      f'- Component: [`{c["name"]}`](./{SUMMARY_NAME})',
                      f'- Code declaration: `{c["source"]}:L{fn["line"]}`',
                      f'- Declaration type: `{fn["kind"]}`',
                      f'- Document version: `r{version}` (local index revision, not product release)',
                      f'- Source fingerprint: `{c["fingerprint"][:16]}`',
                      f'- Last change summary: {change}', '',
                      '## Architecture detail', '',
                      'Purpose, input/output contracts, dependencies and side effects: **not yet verified from implementation and approved specification**.',
                      'Review the exact source and relevant approved requirement before asserting behavior.', ''])


def publish(root: Path, manifest: dict, graph: dict, focus: set[str]) -> dict:
    root = guard.validate_root(root)
    old_symbols = infra.read_json(root / SYMBOL_CACHE, root=root) or {}
    components, symbols = evidence_graph(root,manifest,graph,old_symbols)
    old_state = infra.read_json(root / STATE_FILE, root=root) or {'schema_version': VERSION, 'functions':{}}
    if old_state.get('schema_version') != VERSION:
        raise RuntimeError('Architecture version mismatch; manual migration required')
    old_functions=old_state.get('functions',{})
    funcs_new={}
    old_notes=old_state.get('notes_by_path', {})
    planned=[]
    for (layer, name), c in components.items():
        target = root / LAYER_DIRS[layer] / name
        planned.append((target/SUMMARY_NAME,render_component(c,[x for (l,_),x in components.items() if l==layer])))
        for fn in c['functions']:
            key=function_key(c,fn)
            prev=old_functions.get(key, {})
            old_fp=prev.get('fingerprint')
            new_fp=c['fingerprint']
            ver=prev.get('version',0) if old_fp==new_fp else prev.get('version',0)+1
            change='No source fingerprint difference since last indexed revision.' if old_fp==new_fp else (
                f'Source file fingerprint changed `{str(old_fp)[:12]}` → `{new_fp[:12]}`; function-level semantic diff not proven.' if old_fp else 'Initial source-index baseline; no prior change provenance.')
            provenance=old_notes.get(c['source'],{})
            if provenance.get('fingerprint')==new_fp:
                change=f"Recorded by session `{provenance['session']}` for requirement `{provenance['requirement']}`: {provenance['note']} (declared authorship, not semantic proof)."
            funcs_new[key]={'version':ver,'fingerprint':new_fp,'document':f'{LAYER_DIRS[layer]}/{name}/{function_filename(c, fn)}'}
            fname=function_filename(c, fn)
            planned.append((target/fname,render_function(c,fn,ver,change)))
    counts={layer: sum(1 for (l,_) in components if l==layer) for layer in LAYER_DIRS}
    planned.append((root/SUMMARY_NAME, render_root(graph,manifest,focus,counts)))
    for layer in LAYER_DIRS:
        layer_comps=[c for (l,_),c in sorted(components.items()) if l==layer]
        planned.append((root/LAYER_DIRS[layer]/SUMMARY_NAME,render_layer(layer,layer_comps,graph,focus)))
    # All-or-nothing preflight for unsafe collisions or symlinked directories.
    for p,_ in planned:
        a=p
        while a!=root and a!=a.parent:
            if a.is_symlink():
                raise RuntimeError(f'Refusing architecture symlink: {a}')
            a=a.parent
        if p.exists() and (not p.is_file() or not p.read_text(encoding='utf-8').startswith(GENERATED)):
            raise RuntimeError(f'Non-managed architecture path collision: {p}')
    for p, content in planned:
        guarded_write(root,p,content)
    infra.atomic_text(root / SYMBOL_CACHE, json.dumps(symbols,ensure_ascii=False,indent=2)+'\n', root=root) if symbols!=old_symbols else None
    new_state={'schema_version':VERSION,'functions':funcs_new,'notes_by_path':old_notes,
               'component_count':len(components),'function_count':sum(len(c['functions']) for c in components.values()),
               'generated_paths':[str(p.relative_to(root).as_posix()) for p,_ in planned]}
    if new_state!=old_state:
        infra.atomic_text(root / STATE_FILE,json.dumps(new_state,ensure_ascii=False,indent=2)+'\n', root=root)
    return {'components':len(components),'functions':new_state['function_count'],'documents':len(planned)}


def annotate_recorded_change(root: Path, paths: list[str], note: str, requirement: str,
                             session_id: str, current_files: dict) -> None:
    """Annotate the latest *registered* change; do not assert inferred semantics."""
    root = guard.validate_root(root)
    state=infra.read_json(root/STATE_FILE, root=root)
    if not state:
        raise RuntimeError('Missing architecture-docs state for change annotation')
    infos=state.setdefault('notes_by_path',{})
    safe_note=' '.join(note.split()).replace('`', "'").replace('|','/')[:190]
    safe_req=' '.join((requirement or 'UNSPECIFIED').split()).replace('`', "'")[:70]
    for path in paths:
        metadata=current_files.get(path)
        if not metadata:
            continue # a deleted path has no currently callable function docs
        fp=metadata.get('sha256') or str(metadata.get('size'))+':'+str(metadata.get('mtime_ns'))
        infos[path]={'fingerprint':fp,'session':session_id,'requirement':safe_req,'note':safe_note}
        for key,info in state['functions'].items():
            if key.startswith(path+'#') and info.get('fingerprint')==fp:
                target=guard.check_path(root,info['document'])
                if not target.is_file() or target.is_symlink():
                    raise RuntimeError(f'Missing/unsafe function doc for annotation: {target}')
                prior=target.read_text(encoding='utf-8')
                if not prior.startswith(GENERATED):
                    raise RuntimeError(f'Refusing non-managed function annotation: {target}')
                statement=f'- Last change summary: Recorded by session `{session_id}` for requirement `{safe_req}`: {safe_note} (declared authorship, not semantic proof).'
                revised=re.sub(r'^- Last change summary: .*$',lambda m:statement,prior,count=1,flags=re.M)
                guarded_write(root,target,revised)
    infra.atomic_text(root/STATE_FILE,json.dumps(state,ensure_ascii=False,indent=2)+'\n', root=root)
