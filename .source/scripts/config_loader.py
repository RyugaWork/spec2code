#!/usr/bin/env python3
"""Load versioned, bundled Spec2Code policies from .config/*.json.

Only the installed skill's configuration is read. This module never searches the
current directory, home, environment variables or another repository for a
fallback. Security invariants remain enforced by their respective Python guards.
"""
from __future__ import annotations

from functools import lru_cache
import json
import os
from pathlib import Path, PurePosixPath, PureWindowsPath
import re

CONFIG_NAMES = frozenset({'scanner', 'architecture', 'routing', 'session', 'speckit',
                          'handoff', 'mcp', 'security'})
MAX_CONFIG_BYTES = 64 * 1024  # loader resource ceiling; not configurable


def _pairs_without_duplicates(pairs: list[tuple[str, object]]) -> dict:
    value = {}
    for k, v in pairs:
        if k in value:
            raise ValueError('duplicate JSON key: ' + k)
        value[k] = v
    return value


def _path_value(value: object, name: str) -> None:
    if not isinstance(value, str) or not value or '\\' in value or '\x00' in value:
        raise RuntimeError(f'CONFIG_INVALID: invalid {name}')
    if value.startswith('/') or PureWindowsPath(value).drive or any(
            x in ('', '.', '..') or ':' in x for x in value.split('/')):
        raise RuntimeError(f'CONFIG_INVALID: unsafe path in {name}')


def _str_list(value: object, label: str, *, max_items: int = 300) -> None:
    if (not isinstance(value, list) or len(value) > max_items or
            not all(isinstance(x, str) and x and len(x) <= 240 for x in value)
            or len(value) != len(set(value))):
        raise RuntimeError(f'CONFIG_INVALID: invalid list {label}')


def _bounded_limits(limits: object, label: str) -> None:
    if not isinstance(limits, dict) or not limits:
        raise RuntimeError(f'CONFIG_INVALID: missing limits for {label}')
    for k, v in limits.items():
        if not isinstance(k, str) or type(v) is not int or not 1 <= v <= 100_000_000:
            raise RuntimeError(f'CONFIG_INVALID: invalid limit {label}.{k}')


def _validate(name: str, data: dict) -> None:
    if data.get('schema_version') != 1:
        raise RuntimeError(f'CONFIG_INVALID: unsupported {name} schema_version')
    required = {
        'scanner': {'root_files', 'code_extensions', 'excluded_directories', 'excluded_suffixes',
                    'metadata_only_files', 'source_roots', 'extra_scan_roots', 'limits', 'paths'},
        'architecture': {'layer_directories', 'output_root', 'summary_name', 'paths', 'limits', 'managed_marker', 'classification', 'component_rules'},
        'routing': {'paths', 'modes', 'default_policy', 'task_stopwords'},
        'session': {'paths', 'limits', 'layers'},
        'speckit': {'artifacts', 'stages', 'stage_prerequisites', 'limits', 'task_id_pattern'},
        'handoff': {'paths', 'event_types', 'managed_marker', 'ledger_marker', 'limits'},
        'mcp': {'read_actions', 'write_actions', 'action_arguments'},
        'security': {'managed_paths', 'additional_sensitive_names', 'additional_excluded_suffixes'},
    }[name]
    if set(data) != required | {'schema_version'}:
        raise RuntimeError(f'CONFIG_INVALID: {name} fields mismatch')
    if 'limits' in data:
        _bounded_limits(data['limits'], name)
    if name in {'scanner', 'security'}:
        for field in required - {'limits','paths'}:
            if field in ('source_roots','extra_scan_roots','managed_paths','excluded_directories'):
                _str_list(data[field], name+'.'+field)
                for value in data[field]:
                    _path_value(value, name+'.'+field)
            elif field != 'limits':
                _str_list(data[field], name+'.'+field)
        if name == 'scanner':
            if not isinstance(data['paths'],dict) or set(data['paths']) != {'state_dir','manifest','index','changelog_dir'}:
                raise RuntimeError('CONFIG_INVALID: invalid scanner paths')
            for key,value in data['paths'].items():
                _path_value(value,'scanner.paths.'+key)
                if key!='changelog_dir' and not (value=='.agents/state' or value.startswith('.agents/state/')):
                    raise RuntimeError('CONFIG_INVALID: scanner state outside reserved directory')
                if key=='changelog_dir' and not value.startswith('.agents/.handoffs/'):
                    raise RuntimeError('CONFIG_INVALID: scanner changelog outside reserved directory')
            if not {'.env','.git'}.isdisjoint(data['source_roots']):
                raise RuntimeError('CONFIG_INVALID: scanner cannot use secret or Git source roots')
            if not {'appsettings.json','credentials.json','secrets.json','.npmrc','.pypirc'}.issubset(
                    data['metadata_only_files']):
                raise RuntimeError('CONFIG_INVALID: scanner cannot remove protected metadata-only files')
            if not {'.pem','.key','.pfx','.p12','.db','.sqlite','.sqlite3'}.issubset(
                    data['excluded_suffixes']):
                raise RuntimeError('CONFIG_INVALID: scanner cannot remove secure exclusions')
            forbidden = {'.git', '.handoffs', '.agents/.handoffs', '.agents/state', '.agents/skills', '.config', 's2c'}
            if set(data['source_roots']) & forbidden or set(data['extra_scan_roots']) & forbidden:
                raise RuntimeError('CONFIG_INVALID: scanner cannot inventory internal or Git directories')
    if name in {'architecture','routing','session','handoff'}:
        paths=data['paths']
        if not isinstance(paths,dict) or not paths:
            raise RuntimeError(f'CONFIG_INVALID: missing {name} paths')
        for field,value in paths.items():
            _path_value(value, f'{name}.paths.{field}')
            if name in {'architecture','routing','session'} and not value.startswith('.agents/state/'):
                raise RuntimeError(f'CONFIG_INVALID: {name} state path outside reserved state directory')
            if name == 'handoff' and not (value == '.agents/.handoffs' or value.startswith('.agents/.handoffs/')):
                raise RuntimeError('CONFIG_INVALID: handoff path outside reserved directory')
    if name == 'handoff':
        expected = {'directory': '.agents/.handoffs', 'details': '.agents/.handoffs/.details',
                    'buildnotes': '.agents/.handoffs/.buildnotes.handoff.md',
                    'lock': '.agents/.handoffs/.merge.lock'}
        if data['paths'] != expected:
            raise RuntimeError('CONFIG_INVALID: handoff layout must remain reserved and session-owned')
    if name == 'architecture':
        # Only the fixed reserved target output namespace is permitted; source dirs are never valid.
        if data.get('output_root') != 's2c':
            raise RuntimeError('CONFIG_INVALID: architecture must publish inside s2c')
        dirs = data['layer_directories']
        if not isinstance(dirs, dict) or not dirs:
            raise RuntimeError('CONFIG_INVALID: architecture layers missing')
        for k, v in dirs.items():
            _path_value(v, 'architecture.layer_directories.'+k)
        protected = {'.git','.config','.agents','.handoffs','.specify','specs','src','app',
                     'backend','frontend','server','web','scripts','tests','references'}
        if any('/' in v or v.lower() in protected for v in dirs.values()) or len({v.casefold() for v in dirs.values()}) != len(dirs):
            raise RuntimeError('CONFIG_INVALID: architecture output directory conflicts with source')
        _path_value(data['summary_name'], 'architecture.summary_name')
        for group in ('classification','component_rules'):
            rules=data[group]
            if not isinstance(rules,dict) or not rules:
                raise RuntimeError('CONFIG_INVALID: missing architecture '+group)
            for field, entries in rules.items():
                _str_list(entries, 'architecture.'+group+'.'+field)
    if name == 'routing':
        _str_list(data['task_stopwords'],'routing.task_stopwords')
        _str_list(data['modes'], 'routing.modes', max_items=8)
        policy = data['default_policy']
        if not isinstance(policy, dict) or policy.get('schema_version') != 1 or policy.get('default_mode') not in data['modes']:
            raise RuntimeError('CONFIG_INVALID: routing default_policy')
        for field in ('budgets','max_source_paths','max_function_docs','max_neighbor_hops'):
            values = policy.get(field)
            if not isinstance(values, dict) or set(values) != set(data['modes']) or not all(
                    type(v) is int and 0 <= v <= 20_000 for v in values.values()):
                raise RuntimeError('CONFIG_INVALID: routing '+field)
        for field in ('high_risk_patterns','low_risk_patterns'):
            _str_list(policy.get(field), 'routing.'+field)
    if name == 'session':
        layers = data['layers']
        if not isinstance(layers,list) or not layers or len(layers)>30:
            raise RuntimeError('CONFIG_INVALID: session layers')
        ids=[]
        for entry in layers:
            if not isinstance(entry,dict) or set(entry) != {'id','label','dependencies'}:
                raise RuntimeError('CONFIG_INVALID: session layer entry')
            if not isinstance(entry['id'],str) or not re.fullmatch(r'[a-z][a-z_]{0,40}',entry['id']):
                raise RuntimeError('CONFIG_INVALID: session layer id')
            if not isinstance(entry['label'],str) or len(entry['label'])>120:
                raise RuntimeError('CONFIG_INVALID: session layer label')
            _str_list(entry['dependencies'], 'session layer dependencies', max_items=30)
            ids.append(entry['id'])
        if len(set(ids))!=len(ids) or any(dep not in ids or dep == item['id'] for item in layers for dep in item['dependencies']):
            raise RuntimeError('CONFIG_INVALID: invalid layer dependencies')
    if name == 'speckit':
        _str_list(data['artifacts'],'speckit.artifacts',max_items=30)
        _str_list(data['stages'],'speckit.stages',max_items=30)
        for artifact in data['artifacts']:
            _path_value(artifact,'speckit.artifacts')
        pre = data['stage_prerequisites']
        if not isinstance(pre,dict) or set(pre)!=set(data['stages']):
            raise RuntimeError('CONFIG_INVALID: speckit stage prerequisites')
        for stage,arts in pre.items():
            _str_list(arts, 'speckit.'+stage, max_items=30)
            if not set(arts).issubset(data['artifacts']):
                raise RuntimeError('CONFIG_INVALID: unknown Spec Kit artifact')
        # Do not allow configuration to bypass the official implementation gate.
        if not {'spec.md','plan.md','tasks.md'}.issubset(pre.get('implement',[])):
            raise RuntimeError('CONFIG_INVALID: required Spec Kit implementation artifacts cannot be removed')
        if not isinstance(data['task_id_pattern'],str) or len(data['task_id_pattern']) > 240:
            raise RuntimeError('CONFIG_INVALID: unsafe Spec Kit task pattern')
        re.compile(data['task_id_pattern'])
    if name == 'handoff':
        _str_list(data['event_types'], 'handoff.event_types', max_items=10)
        if set(data['event_types']) != {'visualChange','specChange'}:
            raise RuntimeError('CONFIG_INVALID: handoff events are protocol-locked')
    if name == 'mcp':
        _str_list(data['read_actions'],'mcp.read_actions',max_items=30)
        _str_list(data['write_actions'],'mcp.write_actions',max_items=30)
        if set(data['read_actions']) & set(data['write_actions']):
            raise RuntimeError('CONFIG_INVALID: overlapping MCP permissions')
        args = data['action_arguments']
        if not isinstance(args,dict) or set(args)!=set(data['read_actions']+data['write_actions']):
            raise RuntimeError('CONFIG_INVALID: MCP action argument mapping')
        required_arguments = {
            'status':set(), 'preview_changes':set(), 'architecture_slice':{'layer'},
            'speckit_status':{'stage'},'start_session':set(),
            'checkpoint_session':{'session_id'},'record_change':{'session_id','paths'},
            'finish_session':{'session_id'},'merge_handoff':{'session_id'},
        }
        for action, allowed in args.items():
            _str_list(allowed,'mcp.action_arguments.'+action,max_items=20)
            if set(allowed) != required_arguments.get(action):
                raise RuntimeError('CONFIG_INVALID: MCP parameters are protocol-locked')
            if set(allowed) & {'root','repository','cwd','working_dir','command','shell','allow_write'}:
                raise RuntimeError('CONFIG_INVALID: unsafe MCP argument')
        # Capability list is an adapter protocol, not user-configurable authority.
        if set(data['read_actions']) != {'status','preview_changes','architecture_slice','speckit_status'} or set(data['write_actions']) != {'start_session','checkpoint_session','record_change','finish_session','merge_handoff'}:
            raise RuntimeError('CONFIG_INVALID: unsupported MCP capabilities')


@lru_cache(maxsize=16)
def load(name: str) -> dict:
    """Return a validated bundled configuration; missing/unsafe files fail closed."""
    if name not in CONFIG_NAMES:
        raise RuntimeError('CONFIG_INVALID: unknown configuration section')
    skill_root = Path(__file__).absolute().parent.parent
    if skill_root != skill_root.resolve() or skill_root.is_symlink():
        raise RuntimeError('CONFIG_INVALID: symlinked skill package root')
    config_dir = skill_root / '.config'
    source = config_dir / (name + '.json')
    if config_dir.is_symlink() or source.is_symlink() or not config_dir.is_dir():
        raise RuntimeError(f'CONFIG_INVALID: symlink or missing bundled config for {name}')
    if not source.is_file() or source.stat().st_size > MAX_CONFIG_BYTES:
        raise RuntimeError(f'CONFIG_INVALID: missing/oversized bundled config for {name}')
    try:
        # O_NOFOLLOW protects the final file on POSIX. Ancestor is the bundled,
        # non-symlink config directory above, never a caller-selected directory.
        flags = os.O_RDONLY | getattr(os,'O_NOFOLLOW',0)
        fd=os.open(source,flags)
        with os.fdopen(fd,'rb') as fh:
            content=fh.read(MAX_CONFIG_BYTES+1)
        if len(content)>MAX_CONFIG_BYTES:
            raise ValueError('oversized config')
        data=json.loads(content.decode('utf-8'), object_pairs_hook=_pairs_without_duplicates,
                        parse_constant=lambda v: (_ for _ in ()).throw(ValueError('nonfinite number')))
    except (OSError, ValueError, UnicodeError) as exc:
        raise RuntimeError(f'CONFIG_INVALID: failed to load {name}') from exc
    if not isinstance(data,dict):
        raise RuntimeError(f'CONFIG_INVALID: {name} must be JSON object')
    _validate(name,data)
    return data
