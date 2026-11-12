#!/usr/bin/env python3
"""Spec2Code infrastructure inventory: stdlib-only metadata scan + snapshot writes.

No source content, environment-variable values, API responses, or secrets are
sent to an LLM. The scanner hashes changed, permitted files and persists only
metadata and a small, evidence-grounded architecture summary.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import path_guard as guard
import sys
import tempfile
from typing import Any

SCHEMA = 2
STATES_DIR = Path('.agents/state')
MANIFEST = STATES_DIR / 'infrastructure.json'
INDEX = STATES_DIR / 'infrastructure-index.md'
CHANGELOG = Path('.handoffs/.details')  # pending logs are session-scoped; not written by direct scanner

# Files examined as repository architecture and implementation evidence.
ROOT_FILES = {'AGENTS.md', 'README.md', '.gitignore', 'global.json',
              'Directory.Build.props', 'Directory.Packages.props',
              'docker-compose.yml', 'docker-compose.yaml', 'compose.yml',
              'compose.yaml', 'Dockerfile', 'Makefile', 'package.json',
              'pnpm-workspace.yaml', '.dockerignore', 'pyproject.toml', 'go.mod',
              'Cargo.toml', 'pom.xml', 'build.gradle', 'build.gradle.kts',
              'requirements.txt', 'Gemfile', 'composer.json'}
CODE_EXTS = {'.cs', '.csproj', '.fsproj', '.sln', '.slnx', '.props', '.targets',
             '.ts', '.tsx', '.js', '.jsx', '.mjs', '.cjs', '.json', '.yml', '.yaml',
             '.sql', '.ps1', '.sh', '.md', '.toml', '.config', '.py', '.go', '.rs', '.java',
             '.kt', '.swift', '.rb', '.php', '.vue', '.svelte', '.html', '.css', '.scss', '.tf', '.xml'}
SKIP_DIRS = {'.git', 'node_modules', '.next', '.nuxt', '.venv', 'venv', '__pycache__',
             'bin', 'obj', 'dist', 'build', 'coverage', 'test-results',
             'playwright-report', '.turbo', '.cache', '.idea', '.vs',
             '.angular', '.gradle', 'vendor'}
SKIP_SUFFIX = {'.pem', '.key', '.pfx', '.p12', '.cer', '.crt', '.db', '.sqlite',
               '.sqlite3', '.bak', '.dump', '.zip', '.pdf', '.docx', '.xlsx',
               '.lockb'}
# Secrets may be in configuration files; metadata-only and never read contents.
METADATA_ONLY = {'appsettings.json', 'nuget.config', '.npmrc', '.pypirc',
                 'credentials.json', 'secrets.json', 'appsettings.development.json',
                 'appsettings.production.json', 'appsettings.staging.json',
                 'web.config'}
FILE_CAP = 12000  # explicit safety cap: fail rather than partial deletion claims
MAX_SIZE_HASH = 2 * 1024 * 1024
MAX_INDEX_PATHS = 10
MAX_CHANGE_PATHS = 35


# Enumerate conventional source roots; no assumption about a framework, language or .source/ layout.
SOURCE_ROOTS = {'.source', 'src', 'app', 'lib', 'libs', 'packages', 'services',
                'backend', 'frontend', 'web', 'client', 'api', 'server', 'internal',
                'cmd', 'pkg', 'core', 'tests', 'test', 'specs'}
SCAN_ROOTS = tuple(sorted(SOURCE_ROOTS | {'.agents/.documents', '.github/workflows'}))

def iso_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')


def path_normal(path: Path) -> str:
    return path.as_posix()


def is_excluded(name: str) -> bool:
    """Never traverse or inventory secrets, local tokens and environment files."""
    l = name.lower()
    return (l == '.env' or l.startswith('.env.') or l.endswith(tuple(SKIP_SUFFIX))
            or 'privatekey' in l or l in {'id_rsa', 'id_ed25519'})


def metadata_only(name: str) -> bool:
    """Track existence/metadata for config files, never read or hash their contents."""
    l = name.lower()
    return (l in METADATA_ONLY or (l.startswith('appsettings.') and l.endswith('.json'))
            or 'secret' in l or 'credential' in l or l.startswith('nuget.config'))


def is_sensitive(name: str) -> bool:
    return is_excluded(name) or metadata_only(name)


def tracked_candidate(rel: Path) -> bool:
    parts = rel.parts
    if not parts:
        return False
    if any(p in SKIP_DIRS for p in parts[:-1]):
        return False
    name = rel.name
    if is_excluded(name) or name in {'.gitkeep', '.DS_Store'}:
        return False
    if rel in {Path('visualChange.md'), Path('specChange.md')} or parts[:2] in [('.agents', 'state'),
                                                         ('.agents', 'skills'),
                                                         ('.agents', '.skills')]:
        return False
    if len(parts) == 1:
        return name in ROOT_FILES or (name.startswith('docker-compose') and
              name.endswith(('.yml', '.yaml')))
    if parts[0] == '.agents':
        return len(parts) >= 3 and parts[1] == '.documents' and rel.suffix.lower() == '.md'
    if parts[0] == '.github':
        return len(parts) >= 3 and parts[1] == 'workflows' and rel.suffix.lower() in {'.yml', '.yaml'}
    if parts[0] in SOURCE_ROOTS:
        return rel.suffix.lower() in CODE_EXTS or name in {'Dockerfile', 'Makefile', '.gitignore'}
    return False


def all_files(root: Path) -> list[Path]:
    result = []
    for top in SCAN_ROOTS:
        base = root / top
        if not base.is_dir() or base.is_symlink() or (base / '.git').exists():
            continue
        # os.walk never follows symlinked directories.
        for directory, dirs, files in os.walk(base, followlinks=False):
            # Nested Git checkout/submodule belongs to another repository.
            if Path(directory) != base and (Path(directory) / '.git').exists():
                dirs[:] = []
                continue
            dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and
                             not (Path(directory) / d).is_symlink())
            for f in sorted(files):
                p = Path(directory) / f
                rel = p.relative_to(root)
                if tracked_candidate(rel) and not p.is_symlink() and p.is_file():
                    result.append(rel)
                    if len(result) > FILE_CAP:
                        raise RuntimeError(f'Exceeded file cap ({FILE_CAP}); refusing incomplete inventory')
    for p in sorted(root.iterdir()):
        if p.is_file() and not p.is_symlink() and tracked_candidate(p.relative_to(root)):
            result.append(p.relative_to(root))
    return sorted(set(result), key=path_normal)


def sha256_file(path: Path, *, root: Path) -> str:
    # Files above MAX_SIZE_HASH are metadata-only; bounded anchored read.
    import scope_io
    return hashlib.sha256(scope_io.read_bytes(root, path, max_bytes=MAX_SIZE_HASH)).hexdigest()


def describe_file(root: Path, rel: Path, old: dict | None, verify: bool) -> dict:
    p = guard.check_path(root, rel)
    st = p.stat()
    out = {'size': st.st_size, 'mtime_ns': st.st_mtime_ns}
    if metadata_only(p.name):
        out['digest_status'] = 'metadata-only:sensitive-config'
        return out
    if (not verify and old and old.get('size') == st.st_size
            and old.get('mtime_ns') == st.st_mtime_ns):
        if old.get('sha256'):
            out['sha256'] = old['sha256']
        if old.get('digest_status'):
            out['digest_status'] = old['digest_status']
        return out
    if st.st_size > MAX_SIZE_HASH:
        out['digest_status'] = 'metadata-only:large'
    else:
        out['sha256'] = sha256_file(p, root=root)
    return out


def fingerprint(item: dict) -> tuple:
    if item.get('sha256'):
        return ('sha256', item['sha256'])
    return ('metadata', item['size'], item['mtime_ns'])


def repo_git(root: Path) -> dict:
    def run(*args):
        try:
            p = subprocess.run(['git', *args], cwd=root, timeout=3,
                               capture_output=True, text=True, check=False, env=guard.git_env())
            return p.stdout.strip() if p.returncode == 0 else None
        except (OSError, subprocess.TimeoutExpired):
            return None
    return {'branch': run('branch', '--show-current'),
            'head': run('rev-parse', '--short=12', 'HEAD')}


def read_json(path: Path, *, root: Path) -> dict | None:
    guard.check_path(root, path)
    if not path.is_file():
        return None
    try:
        import scope_io
        obj = json.loads(scope_io.read_bytes(root, path, max_bytes=24 * 1024 * 1024).decode('utf-8'))
        return obj if isinstance(obj, dict) else None
    except (OSError, json.JSONDecodeError):
        raise RuntimeError(f'Invalid inventory at {path}; no overwrite was performed')


def safe_text(path: Path, max_bytes: int = 131072, *, root: Path) -> str | None:
    # No arbitrary source reading: used only on known, explicitly allowed manifest names.
    try:
        if path.stat().st_size > max_bytes or is_sensitive(path.name):
            return None
        import scope_io
        return scope_io.read_bytes(root, path, max_bytes=max_bytes).decode('utf-8', errors='replace')
    except OSError:
        return None


def extract_facts(root: Path, files: dict, old: dict | None) -> dict:
    """Tiny allowlisted manifest/entrypoint reads, cached by file fingerprint."""
    old_files = (old or {}).get('files', {})
    old_facts = (old or {}).get('file_facts', {})
    out = {}
    markers = ('AddIdentity', 'AddDefaultIdentity', 'AddIdentityCore',
               'AddJwtBearer', 'AddAuthentication', 'UseAuthentication',
               'UseAuthorization', 'UseAntiforgery', 'AddAntiforgery',
               'AddDbContext', 'UseNpgsql', 'UseSqlServer',
               'AddStackExchangeRedisCache', 'AddMemoryCache',
               'MapControllers', 'AddControllers', 'MapGroup',
               'UseRateLimiter', 'AddRateLimiter')
    for path, details in files.items():
        guard.check_path(root, path)  # Never trust cached or caller-provided path keys.
        name = Path(path).name
        if not (name in {'package.json', 'Program.cs', 'Startup.cs'}
                or name.endswith('.csproj')
                or name in {'compose.yml', 'compose.yaml', 'docker-compose.yml', 'docker-compose.yaml'}
                or name.startswith('docker-compose.') and name.endswith(('.yml', '.yaml'))):
            continue
        if (path in old_facts and path in old_files
                and fingerprint(old_files[path]) == fingerprint(details)):
            out[path] = old_facts[path]
            continue
        data = safe_text(root / path, root=root)
        if data is None:
            continue
        if name == 'package.json':
            try:
                pkg = json.loads(data)
            except json.JSONDecodeError:
                continue
            if not isinstance(pkg, dict):
                continue
            scripts = pkg.get('scripts', {})
            deps = {**(pkg.get('dependencies') or {}), **(pkg.get('devDependencies') or {})}
            if not isinstance(deps, dict) or not isinstance(scripts, dict):
                continue
            out[path] = {
                'framework_indicators': sorted(k for k in deps if k in
                    {'react', 'next', 'vite', 'typescript', 'react-dom', '@angular/core'}),
                'script_names': sorted(k for k in scripts if k in
                    {'dev', 'build', 'start', 'lint', 'typecheck', 'test'})}
        elif name.endswith('.csproj'):
            packages = re.findall(r'<PackageReference\b[^>]*\bInclude="([A-Za-z0-9_.-]+)"', data)
            refs = re.findall(r'<ProjectReference\b[^>]*\bInclude="([^"]+)"', data)
            out[path] = {'package_indicators': sorted(set(x for x in packages if
                x.startswith(('Microsoft.AspNetCore.Identity', 'Microsoft.AspNetCore.Authentication',
                              'Microsoft.EntityFrameworkCore', 'Npgsql.EntityFrameworkCore',
                              'Microsoft.Extensions.Caching', 'StackExchange.Redis', 'FluentValidation')))),
                         'project_references': sorted(set(refs))}
        elif name in {'Program.cs', 'Startup.cs'}:
            out[path] = {'startup_signals': sorted(k for k in markers if
                re.search(r'\b' + re.escape(k) + r'(?:<[^>\n]{1,200}>)?\s*\(', data))}
        else:
            services = []
            in_services = False
            for line in data.splitlines():
                if re.fullmatch(r'services:\s*(#.*)?', line):
                    in_services = True
                    continue
                if in_services and re.match(r'^[^\s#]', line):
                    in_services = False
                if in_services:
                    m = re.match(r'^  ([A-Za-z_][A-Za-z0-9_.-]*):\s*(?:#.*)?$', line)
                    if m:
                        services.append(m.group(1))
            out[path] = {'declared_services': sorted(set(services))}
    return out


def component_evidence(root: Path, files: dict, file_facts: dict) -> dict:
    """Metadata-level evidence across common monorepo and language layouts."""
    paths = set(files)
    code_exts = {'.cs', '.py', '.go', '.rs', '.java', '.kt', '.rb', '.php', '.swift'}
    web_exts = {'.js', '.jsx', '.ts', '.tsx', '.vue', '.svelte'}
    web_roots = ('web/', 'frontend/', 'client/', '.source/web/', '.source/frontend/', 'app/')
    backend_roots = ('backend/', 'server/', 'api/', 'services/', '.source/backend/', 'cmd/', 'internal/', 'pkg/')
    web = [p for p in paths if p.startswith(web_roots) or p.endswith(('.tsx', '.jsx', '.vue', '.svelte'))]
    backend = [p for p in paths if p.startswith(backend_roots) or Path(p).suffix in code_exts]
    tests = [p for p in paths if p.startswith(('tests/', 'test/')) or '/tests/' in p or
             Path(p).name.startswith('test_') or Path(p).name.endswith(('.test.ts', '.spec.ts', 'Test.java'))]
    bproj = sorted(p for p in paths if p.endswith(('.csproj', '.sln', '.slnx', '.fsproj',
                 'pyproject.toml', 'go.mod', 'Cargo.toml', 'pom.xml', 'build.gradle',
                 'build.gradle.kts', 'requirements.txt')))
    wpackages = sorted(p for p in paths if p.endswith('package.json'))
    bsource = [p for p in backend if Path(p).suffix.lower() in code_exts]
    wsource = [p for p in web if Path(p).suffix.lower() in web_exts]
    compose = sorted(p for p in paths if Path(p).name in {'compose.yml', 'compose.yaml',
                   'docker-compose.yml', 'docker-compose.yaml'} or
                   Path(p).name.startswith('docker-compose.'))
    workflows = sorted(p for p in paths if p.startswith('.github/workflows/'))
    policies = sorted(p for p in paths if p.startswith('.agents/.documents/') or p == 'AGENTS.md')
    services = sorted({svc for p in compose for svc in file_facts.get(p, {}).get('declared_services', [])})
    frontend = [{'path': p, **file_facts.get(p, {})} for p in wpackages]
    bentry = sorted(p for p in backend if Path(p).name in {'Program.cs', 'Startup.cs', 'main.py', 'main.go', 'app.py'})
    dbcontext = sorted(p for p in backend if p.endswith('DbContext.cs'))
    api = sorted(p for p in backend if Path(p).name.endswith(('Controller.cs', 'Controllers.cs')))
    migrations = sorted(p for p in paths if '/migrations/' in p.lower() and Path(p).suffix in {'.cs', '.sql', '.py'})
    pkgs = sorted({k for p in bproj for k in file_facts.get(p, {}).get('package_indicators', [])})
    startup_signals = sorted({k for p in bentry for k in file_facts.get(p, {}).get('startup_signals', [])})
    backend_dirs = ('backend', 'server', 'api', '.source/backend')
    web_dirs = ('web', 'frontend', 'client', '.source/web')
    return {
        'backend': {'status': 'active' if bsource or bproj else 'scaffold' if any((root/x).is_dir() for x in backend_dirs) else 'absent',
                    'project_files': bproj, 'entrypoints': bentry, 'dbcontext_files': dbcontext,
                    'package_indicators': pkgs, 'startup_signals': startup_signals,
                    'controller_count': len(api), 'source_count': len(bsource)},
        'database': {'status': 'code_indicators' if dbcontext or migrations or any('EntityFramework' in x for x in pkgs) else 'not_observed',
                     'dbcontext_files': dbcontext, 'migration_count': len(migrations),
                     'provider_indicators': sorted(k for k in pkgs if 'EntityFramework' in k)},
        'authentication': {'status': 'code_indicators' if any('Identity' in x or 'Authentication' in x or 'JwtBearer' in x for x in pkgs+startup_signals) else 'not_observed',
                           'startup_signals': sorted(k for k in startup_signals if 'Identity' in k or 'Authentication' in k or 'JwtBearer' in k)},
        'web': {'status': 'active' if wsource or wpackages else 'scaffold' if any((root/x).is_dir() for x in web_dirs) else 'absent',
                'package_manifests': frontend, 'source_count': len(wsource)},
        'containers': {'status': 'configured' if compose else 'not_observed',
                       'compose_files': compose, 'declared_service_names': services},
        'tests': {'status': 'present' if tests else 'not_observed', 'tracked_test_files': len(tests)},
        'workflows': {'status': 'configured' if workflows else 'not_observed', 'paths': workflows},
        'policy_docs': {'status': 'present' if policies else 'not_observed', 'paths': policies},
    }

def category(path: str) -> str:
    s = path.lower()
    if s.startswith(('.source/backend/', 'backend/', 'server/', 'api/')):
        return 'Backend'
    if s.startswith(('.source/web/', '.source/frontend/', 'web/', 'frontend/', 'client/')):
        return 'Frontend'
    if s.startswith('.agents/.documents/') or s == 'agents.md':
        return 'Governance'
    if s.startswith(('tests/', 'test/')) or '/tests/' in s:
        return 'Tests'
    if s.startswith('.github/'):
        return 'CI/CD'
    return 'Repository / deployment'

def diff_files(before: dict, after: dict) -> list[dict]:
    changes = []
    for path in sorted(before.keys() | after.keys()):
        if path not in before:
            kind = 'ADDED'
        elif path not in after:
            kind = 'REMOVED'
        elif fingerprint(before[path]) != fingerprint(after[path]):
            kind = 'MODIFIED'
        else:
            continue
        changes.append({'kind': kind, 'path': path, 'area': category(path)})
    return changes


def render_topology(components: dict) -> str:
    return ('```mermaid\nflowchart LR\n'
            '    R["Spec2Code repository"] --> B["Backend: ' + components['backend']['status'] + '"]\n'
            '    R --> W["Web: ' + components['web']['status'] + '"]\n'
            '    B --> DB["Data access: ' + components['database']['status'] + '"]\n'
            '    B --> A["Auth: ' + components['authentication']['status'] + '"]\n'
            '    R --> D["Docker: ' + components['containers']['status'] + '"]\n'
            '    R --> T["Tests: ' + components['tests']['status'] + '"]\n'
            '    R --> C["CI/CD: ' + components['workflows']['status'] + '"]\n'
            '```')


def render_index(manifest: dict) -> str:
    c = manifest['components']
    def items(xs: list, limit=MAX_INDEX_PATHS) -> str:
        if not xs:
            return '_None observed._'
        lines = '\n'.join('- `' + x + '`' for x in xs[:limit])
        return lines + ('\n- … +' + str(len(xs) - limit) + ' more in `infrastructure.json`' if len(xs) > limit else '')
    b = c['backend']
    w = c['web']
    f = w['package_manifests']
    return f'''# Spec2Code Infrastructure Index (auto-generated)

**Evidence:** local repository file scan; **not** proof of deployed/runtime behavior. Do not interpret `.gitkeep` scaffolds as implemented code. The full inventory is stored in `infrastructure.json` (do not paste it into an agent prompt).

- Snapshot: `{manifest['snapshot_at']}` UTC
- Git branch/HEAD: `{manifest['git'].get('branch') or 'unknown'}` / `{manifest['git'].get('head') or 'unknown'}`
- Tracked candidate files inventoried: **{len(manifest['files'])}**
- Last change event: `{manifest.get('last_change_at') or 'baseline'}`

## Observed components

| Component | Evidence status | Minimal facts |
| --- | --- | --- |
| Backend | **{b['status']}** | {len(b['project_files'])} projects/solutions, {b['source_count']} backend-language source files, {b['controller_count']} controllers |
| Web | **{w['status']}** | {len(f)} package manifests, {w['source_count']} web source files |
| Database integration | **{c['database']['status']}** | {len(c['database']['dbcontext_files'])} DbContext files, {c['database']['migration_count']} migration files |
| Authentication | **{c['authentication']['status']}** | {', '.join(c['authentication']['startup_signals']) or 'no startup indicators'} |
| Docker | **{c['containers']['status']}** | {len(c['containers']['compose_files'])} compose files; declared services: {', '.join(c['containers']['declared_service_names']) or 'not observed'} |
| Tests | **{c['tests']['status']}** | {c['tests']['tracked_test_files']} candidate test files |
| CI/CD | **{c['workflows']['status']}** | {len(c['workflows']['paths'])} workflow files |
| Governance | **{c['policy_docs']['status']}** | {len(c['policy_docs']['paths'])} task-scoped policy files |

## Structural diagram (discovery only)

{render_topology(c)}

## Code-based indicators (NOT runtime proof)

- Packages found in project manifests: {', '.join(b['package_indicators']) or 'none observed'}
- Registration/middleware calls found in entrypoints: {', '.join(b['startup_signals']) or 'none observed'}

## Project & entrypoint paths

{items(b['project_files'] + b['entrypoints'] + b['dbcontext_files'])}

## Package manager evidence

{items([f"{x['path']} (framework indicators: {', '.join(x.get('framework_indicators', [])) or 'none'}; scripts: {', '.join(x.get('script_names', [])) or 'none'})" for x in f])}

## Docker & CI references

{items(c['containers']['compose_files'] + c['workflows']['paths'])}

## How to use this index

Read **this file only** to decide which parts exist. Consult `layerSummary.md`, and `impactMatrix.md` only when relevant. `.handoffs/.details/.visualChange.{{SessionID}}.md` holds external evidence; `.specChange.{{SessionID}}.md` in the same directory holds explicitly registered authored work. They are managed by `session_guard.py`. `infrastructure.json` is machine-readable state for the scanner, **not** routine LLM context. Existing architecture documents describe **intent**, not proof of implementation. Use `--verify` for a full rehash when timestamps are unreliable; use `--runtime` only when separately authorized.
'''


def render_event(now: str, changes: list[dict], previous: dict | None,
                 current: dict, initial: bool) -> str:
    if initial:
        return (f'## {now} — BASELINE\n\n'
                f'- Files inventoried: **{len(current["files"])}**. This is an initial snapshot, **not** evidence of newly added infrastructure.\n'
                '- No runtime/deployment verification was performed.\n\n'
                + render_topology(current['components']) + '\n\n')
    added = sum(x['kind'] == 'ADDED' for x in changes)
    removed = sum(x['kind'] == 'REMOVED' for x in changes)
    modified = sum(x['kind'] == 'MODIFIED' for x in changes)
    lines = [f'## {now} — CHANGED', '',
             f'- **{len(changes)}** paths changed: +{added} added / ~{modified} modified / -{removed} removed.',
             '- Source: local files; no claim about production deployments.', '']
    for area in ['Backend', 'Frontend', 'Repository / deployment', 'Governance', 'Tests', 'CI/CD']:
        hits = [x for x in changes if x['area'] == area]
        if not hits:
            continue
        lines.append('### ' + area)
        for x in hits[:MAX_CHANGE_PATHS]:
            lines.append(f'- `{x["kind"]}` `{x["path"]}`')
        if len(hits) > MAX_CHANGE_PATHS:
            lines.append(f'- … +{len(hits) - MAX_CHANGE_PATHS} more paths; see `infrastructure.json` `recent_changes`.')
        lines.append('')
    if previous and previous.get('components') != current.get('components'):
        lines.extend(['### Structural discovery (after change)', '', render_topology(current['components']), ''])
    lines.extend(['**Interpretation:** Changes in tracked files do not prove corresponding runtime behavior. Review affected files before making implementation decisions.', '', ''])
    return '\n'.join(lines)


def atomic_text(path: Path, content: str, *, root: Path) -> None:
    """Use directory-anchored, no-follow atomic replacement where supported."""
    import scope_io
    scope_io.atomic_text(root, path, content)


def runtime_probe(root: Path) -> dict:
    """Explicit opt-in. No container inspect, DB calls, env dumps or networking."""
    versions = {}
    for key, args in {'dotnet': ['dotnet', '--version'], 'node': ['node', '--version'],
                      'python': [sys.executable, '--version']}.items():
        try:
            p = subprocess.run(args, cwd=root, timeout=3, text=True,
                               capture_output=True, check=False)
            if p.returncode == 0:
                versions[key] = (p.stdout or p.stderr).strip().splitlines()[0][:100]
        except (OSError, subprocess.TimeoutExpired, IndexError):
            pass
    return {'observed_at_utc': iso_now(), 'local_tool_versions': versions,
            'note': 'Opt-in local tool probe only; not proof of running services'}


def run(args) -> int:
    root = guard.validate_root(args.root)
    old = read_json(root / MANIFEST, root=root)
    if old is not None and old.get('status') != 'UNINITIALIZED' and old.get('schema_version') != SCHEMA:
        raise RuntimeError('Inventory schema mismatch; migration required, no overwrite')
    initial = old is None or old.get('status') == 'UNINITIALIZED'
    old_files = {} if initial else old.get('files', {})
    files = {}
    for rel in all_files(root):
        rel_str = path_normal(rel)
        files[rel_str] = describe_file(root, rel, old_files.get(rel_str), args.verify)
    changes = [] if initial else diff_files(old_files, files)
    file_facts = extract_facts(root, files, old if not initial else None)
    components = component_evidence(root, files, file_facts)
    structural_change = not initial and old.get('components') != components
    git_state = repo_git(root)
    ref_changed = not initial and old.get('git') != git_state
    # Ignore mtime-only changes for files whose content hashes are unchanged.
    meaningful = initial or bool(changes) or structural_change or ref_changed
    now = iso_now()
    if not meaningful:
        print('NO_CHANGE | files=' + str(len(files)) + ' | no artifact write')
    else:
        manifest = {'schema_version': SCHEMA, 'status': 'VERIFIED_LOCAL_SNAPSHOT',
                    'snapshot_at': now, 'git': git_state, 'files': files,
                    'file_facts': file_facts, 'components': components,
                    'last_change_at': now if (changes or structural_change) else
                        (None if initial else old.get('last_change_at')),
                    'recent_changes': changes if (changes or structural_change) else
                        (old.get('recent_changes', []) if old else [])}
        if not args.dry_run:
            # This standalone scan NEVER writes visualChange.md: attribution to
            # external sessions is owned exclusively by session_guard.py.
            atomic_text(root / MANIFEST, json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', root=root)
            atomic_text(root / INDEX, render_index(manifest), root=root)
        result_status = 'BASELINE' if initial else ('CHANGED' if changes or structural_change else 'CONTEXT_CHANGED')
        print(result_status + ' | files=' + str(len(files)) +
              ' | delta=' + str(len(changes)) + (' | DRY_RUN' if args.dry_run else ''))
        if changes:
            counts = {k: sum(c['kind'] == k for c in changes) for k in ('ADDED', 'MODIFIED', 'REMOVED')}
            print('DELTA | +' + str(counts['ADDED']) + ' ~' + str(counts['MODIFIED']) + ' -' + str(counts['REMOVED']))
            for c in changes[:args.max_stdout]:
                print(c['kind'] + ' | ' + c['path'])
            if len(changes) > args.max_stdout:
                print('... ' + str(len(changes) - args.max_stdout) + ' more: see infrastructure.json recent_changes')
    if args.runtime:
        r = runtime_probe(root)
        if not args.dry_run:
            # Intentionally private, machine-dependent and ignored by the source scanner.
            atomic_text(root / STATES_DIR / '.runtime-status.json', json.dumps(r, indent=2) + '\n', root=root)
        print('RUNTIME | local tooling checked (not a deployment status check)')
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', default='.', help='target-repository repository root')
    p.add_argument('--verify', action='store_true', help='Rehash eligible files, even when metadata is unchanged')
    p.add_argument('--dry-run', action='store_true', help='Compute result without writing state or log')
    p.add_argument('--runtime', action='store_true', help='Opt-in local tool versions; no running service or secret inspection')
    p.add_argument('--max-stdout', type=int, default=12, help='Limit changed file lines shown to agent (default 12)')
    args = p.parse_args()
    # Guard against bypassing session attribution: this public CLI is read-only.
    # The session manager imports collection functions and persists snapshots
    # transactionally with its session/commit checks.
    args.dry_run = True
    if not 0 <= args.max_stdout <= 50:
        p.error('--max-stdout must be 0..50')
    try:
        print('DIRECT_SCAN_READ_ONLY | use session_guard.py start/checkpoint for persisted state')
        return run(args)
    except (OSError, RuntimeError, ValueError) as exc:
        print('SCAN_FAILED | ' + str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
