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
import scope_io
import config_loader

ARCH_CONFIG = config_loader.load('architecture')
LAYER_DIRS = ARCH_CONFIG['layer_directories']
OUTPUT_ROOT = Path(ARCH_CONFIG['output_root'])
SUMMARY_NAME = ARCH_CONFIG['summary_name']  # The historical spelling is retained in config.
STATE_FILE = Path(ARCH_CONFIG['paths']['state_file'])
SYMBOL_CACHE = Path(ARCH_CONFIG['paths']['symbol_cache'])
GENERATED = ARCH_CONFIG['managed_marker']
VERSION = 1  # persisted schema, not a policy setting
MAX_COMPONENTS = ARCH_CONFIG['limits']['components']
MAX_METHODS = ARCH_CONFIG['limits']['functions']
MAX_SOURCE_BYTES = ARCH_CONFIG['limits']['source_bytes']
MAX_VISIBLE_COMPONENTS = ARCH_CONFIG['limits']['visible_components']
MAX_VISIBLE_FUNCTIONS = ARCH_CONFIG['limits']['visible_functions']


def safe_name(name: str) -> str:
    """Safe, portable component path; no path separators or dot traversal."""
    s = re.sub(r'[^A-Za-z0-9_-]', '_', name.strip())[:52].strip('_.-')
    if not s or s.lower() in {'con','nul','prn','aux','com1','lpt1'}:
        return 'Component_' + hashlib.sha256(name.encode()).hexdigest()[:8]
    return s


def layer_for_path(p: str) -> str:
    """Ordered conservative mapping from bundled architecture classification data."""
    rules = ARCH_CONFIG['classification']
    s = p.lower().replace('\\', '/')
    name = Path(s).name
    has = lambda key: any(t in s for t in rules[key])
    prefix = lambda key: s.startswith(tuple(rules[key]))
    suffix = lambda key: s.endswith(tuple(rules[key]))
    named = lambda key: name in rules[key]
    named_prefix = lambda key: name.startswith(tuple(rules[key]))
    named_suffix = lambda key: name.endswith(tuple(rules[key]))
    regex = lambda key: any(re.search(pattern,s) for pattern in rules[key])
    if s in rules['governance_exact'] or prefix('governance_prefixes'):
        return 'governance'
    if prefix('quality_prefixes') or has('quality_contains') or named_prefix('quality_name_prefixes') or named_suffix('quality_name_suffixes'):
        return 'quality'
    if prefix('delivery_prefixes') or named('delivery_names') or any(t in name for t in rules['delivery_name_contains']) or suffix('delivery_suffixes'):
        return 'delivery'
    if has('security_contains'):
        return 'security'
    if has('persistence_contains') or suffix('persistence_suffixes'):
        return 'persistence'
    if has('data_contains') or regex('data_regexes'):
        return 'data'
    if has('integrations_contains') or regex('integrations_regexes'):
        return 'integrations'
    if has('api_contains') or named_suffix('api_name_suffixes') or regex('api_regexes'):
        return 'presentation' if prefix('api_presentation_prefixes') else 'api'
    if prefix('presentation_prefixes'):
        return 'presentation'
    if prefix('api_top_prefixes') and (has('api_top_contains') or named('api_top_names')):
        return 'api'
    if prefix('presentation_code_prefixes') and Path(s).suffix.lower() in rules['presentation_extensions']:
        return 'presentation'
    if has('application_contains'):
        return 'application'
    if prefix('governance_late_prefixes'):
        return 'governance'
    if prefix('application_prefixes'):
        return 'application'
    return 'governance' if name.endswith(tuple(rules['governance_suffixes'])) else 'delivery'


def observed_component(path: str, layer: str) -> bool:
    rules = ARCH_CONFIG['component_rules']
    p = Path(path)
    suffix = p.suffix.lower()
    if layer == 'api':
        return p.name.endswith(tuple(rules['api_controller_suffixes'])) or suffix in rules['api_extensions']
    if layer == 'presentation':
        return suffix in rules['presentation_extensions']
    if layer in rules['implementation_layers']:
        return suffix in rules['implementation_extensions'] and not p.name.endswith(tuple(rules['generated_code_suffixes']))
    if layer == 'quality':
        return suffix in rules['quality_extensions']
    if layer in rules['documentation_layers']:
        if path.startswith(tuple(rules['exclude_prefixes'])):
            return False
        return suffix in rules['documentation_extensions'] or p.name in rules['documentation_names']
    return False


def component_name(path: str, layer: str) -> str:
    p = Path(path)
    if layer == 'presentation' and p.stem.lower() in ARCH_CONFIG['component_rules']['presentation_route_names']:
        dirname = p.parent.name if p.parent.name not in ARCH_CONFIG['component_rules']['presentation_generic_parents'] else 'Root'
        return safe_name(dirname + '_' + p.stem.capitalize())
    return safe_name(p.stem)


def extract_symbols(root: Path, path: str, layer: str, fingerprint: str, cached: dict | None) -> dict:
    guard.check_path(root, path)
    if cached and cached.get('fingerprint') == fingerprint:
        return cached
    result = {'fingerprint': fingerprint, 'functions': [], 'imports': [], 'source_status': 'unparsed'}
    p = root / path
    if p.stat().st_size > MAX_SOURCE_BYTES or infra.is_sensitive(p.name) or p.is_symlink():
        result['source_status'] = 'metadata_only'
        return result
    import scope_io
    source = scope_io.read_bytes(root, p, max_bytes=MAX_SOURCE_BYTES).decode('utf-8', errors='replace')
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
        guard.check_path(root, path)  # Cached manifest path must not escape checkout.
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
        old = scope_io.read_bytes(root, path, max_bytes=1024*1024).decode('utf-8')
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
           'Local static evidence only. Documents under s2c/ layer folders are **architecture indexes**, not application code.',
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
    legacy_summary = guard.check_path(root, SUMMARY_NAME)
    if legacy_summary.is_file() and scope_io.read_bytes(root, legacy_summary, max_bytes=1024*1024).startswith(GENERATED.encode('utf-8')):
        raise RuntimeError('LAYOUT_MIGRATION_REQUIRED: old root architecture docs must be reviewed and archived manually')
    old_symbols = infra.read_json(root / SYMBOL_CACHE, root=root) or {}
    components, symbols = evidence_graph(root,manifest,graph,old_symbols)
    old_state = infra.read_json(root / STATE_FILE, root=root) or {'schema_version': VERSION, 'functions':{}}
    if old_state.get('schema_version') != VERSION:
        raise RuntimeError('Architecture version mismatch; manual migration required')
    # Legacy cached paths must never point writes/annotations into old root layer folders.
    historic = old_state.get('generated_paths', [])
    documents = [x.get('document', '') for x in old_state.get('functions', {}).values() if isinstance(x, dict)]
    if any(not isinstance(p, str) or not p.startswith(OUTPUT_ROOT.as_posix() + '/') for p in historic + documents):
        raise RuntimeError('LAYOUT_MIGRATION_REQUIRED: older architecture paths in state; preserve data and migrate explicitly')
    output = guard.check_path(root, OUTPUT_ROOT)
    if output.exists() and (not output.is_dir() or (any(output.iterdir()) and not (output / SUMMARY_NAME).is_file())):
        raise RuntimeError('ARCH_OUTPUT_COLLISION: pre-existing s2c content is not a managed architecture tree')
    if (output / SUMMARY_NAME).is_file() and not scope_io.read_bytes(root, output / SUMMARY_NAME, max_bytes=1024*1024).startswith(GENERATED.encode('utf-8')):
        raise RuntimeError('ARCH_OUTPUT_COLLISION: non-managed s2c root summary')
    old_functions=old_state.get('functions',{})
    funcs_new={}
    old_notes=old_state.get('notes_by_path', {})
    planned=[]
    for (layer, name), c in components.items():
        target = root / OUTPUT_ROOT / LAYER_DIRS[layer] / name
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
            funcs_new[key]={'version':ver,'fingerprint':new_fp,'document':f'{OUTPUT_ROOT.as_posix()}/{LAYER_DIRS[layer]}/{name}/{function_filename(c, fn)}'}
            fname=function_filename(c, fn)
            planned.append((target/fname,render_function(c,fn,ver,change)))
    counts={layer: sum(1 for (l,_) in components if l==layer) for layer in LAYER_DIRS}
    planned.append((root/OUTPUT_ROOT/SUMMARY_NAME, render_root(graph,manifest,focus,counts)))
    for layer in LAYER_DIRS:
        layer_comps=[c for (l,_),c in sorted(components.items()) if l==layer]
        planned.append((root/OUTPUT_ROOT/LAYER_DIRS[layer]/SUMMARY_NAME,render_layer(layer,layer_comps,graph,focus)))
    # All-or-nothing preflight for unsafe collisions or symlinked directories.
    for p,_ in planned:
        a=p
        while a!=root and a!=a.parent:
            if a.is_symlink():
                raise RuntimeError(f'Refusing architecture symlink: {a}')
            a=a.parent
        if p.exists() and (not p.is_file() or not scope_io.read_bytes(root, p, max_bytes=1024*1024).decode('utf-8').startswith(GENERATED)):
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
                if not str(target.relative_to(root).as_posix()).startswith(OUTPUT_ROOT.as_posix() + '/'):
                    raise RuntimeError('ARCH_DOC_SCOPE_BLOCKED: cached document is outside s2c')
                if not target.is_file() or target.is_symlink():
                    raise RuntimeError(f'Missing/unsafe function doc for annotation: {target}')
                prior=scope_io.read_bytes(root, target, max_bytes=1024*1024).decode('utf-8')
                if not prior.startswith(GENERATED):
                    raise RuntimeError(f'Refusing non-managed function annotation: {target}')
                statement=f'- Last change summary: Recorded by session `{session_id}` for requirement `{safe_req}`: {safe_note} (declared authorship, not semantic proof).'
                revised=re.sub(r'^- Last change summary: .*$',lambda m:statement,prior,count=1,flags=re.M)
                guarded_write(root,target,revised)
    infra.atomic_text(root/STATE_FILE,json.dumps(state,ensure_ascii=False,indent=2)+'\n', root=root)
