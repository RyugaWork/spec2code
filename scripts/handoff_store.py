#!/usr/bin/env python3
"""Pending change logs + conservative, idempotent, session-scoped handoff merge.

Only file candidates with exact session ID/type, correct header and stable SHA-256
are eligible for removal. No glob-based deletion. No Git or network operations.
"""
from __future__ import annotations

import hashlib
import os
from pathlib import Path
import re
from contextlib import contextmanager

import scan_infrastructure as infra
import path_guard as guard

HANDOFF_DIR=Path('.handoffs')
DETAIL_DIR=HANDOFF_DIR/'.details'  # Owner typo `.detials` normalized.
BUILDNOTES=HANDOFF_DIR/'.buildnotes.handoff.md'
LOCK=HANDOFF_DIR/'.merge.lock'
SESSION_RE=re.compile(r'^S2C-\d{8}-\d{6}-[0-9A-F]{8}$')
EVENT_TYPES={'visualChange','specChange'}
MARKER_RE=re.compile(r'^<!-- SPEC2CODE-MERGED session=(S2C-\d{8}-\d{6}-[0-9A-F]{8}) type=(visualChange|specChange) sha256=([0-9a-f]{64}) -->$',re.M)
HEAD='<!-- spec2code:managed-handoff v1 -->'
LEDGER='<!-- SPEC2CODE-HANDOFF-LEDGER -->'
MAX_BYTES=1024*1024
MAX_LEDGER=24*1024*1024


def validate_session(sid: str) -> None:
    if not SESSION_RE.fullmatch(sid):
        raise RuntimeError('Invalid Spec2Code Session ID format; refusing handoff operation')


def path_for(root: Path, kind: str, sid: str) -> Path:
    validate_session(sid)
    if kind not in EVENT_TYPES:
        raise RuntimeError('Invalid handoff event type')
    return root/DETAIL_DIR/f'.{kind}.{sid}.md'


def header(sid: str, kind: str) -> str:
    return '\n'.join([f'<!-- spec2code:pending-change v1 session={sid} type={kind} -->',
                      f'# {kind}: {sid}', '',
                      f'- Session-ID: `{sid}`',
                      f'- Change-Type: `{kind}`',
                      '- Status: PENDING_MERGE', ''])


def refuse_symlink(root: Path, path: Path) -> None:
    cur=path
    while cur!=root and cur!=cur.parent:
        if cur.is_symlink():
            raise RuntimeError(f'Refusing symlinked handoff path: {cur}')
        cur=cur.parent


def append_event(root: Path, sid: str, kind: str, body: str) -> None:
    root=guard.validate_root(root)
    p=path_for(root, kind, sid)
    guard.check_path(root, p)
    refuse_symlink(root,p)
    p.parent.mkdir(parents=True,exist_ok=True)
    if p.is_file():
        existing=p.read_text(encoding='utf-8')
        if not existing.startswith(header(sid,kind)):
            raise RuntimeError(f'Pending log header mismatch: {p}')
        if len(existing.encode('utf-8'))>MAX_BYTES:
            raise RuntimeError('Pending log too large; manual handoff required')
    else:
        infra.atomic_text(p,header(sid,kind)+'\n', root=root)
    with p.open('a',encoding='utf-8') as stream:
        stream.write(body.rstrip()+'\n\n')


@contextmanager
def merge_lock(root: Path):
    p=guard.check_path(root, LOCK)
    refuse_symlink(root,p)
    p.parent.mkdir(parents=True,exist_ok=True)
    try:
        fd=os.open(p,os.O_CREAT|os.O_EXCL|os.O_WRONLY|getattr(os,'O_NOFOLLOW',0),0o600)
    except FileExistsError:
        raise RuntimeError('Handoff merge already in progress or stale lock present; do not auto-remove lock')
    try:
        with os.fdopen(fd,'w') as f:
            f.write('Spec2Code handoff merge lock. Do not remove during an active merge.\n')
        yield
    finally:
        p.unlink(missing_ok=True)


def is_finished(root: Path, sid: str) -> bool:
    p=guard.check_path(root, '.agents/state/sessions.jsonl')
    if not p.is_file():
        return False
    import json
    with p.open(encoding='utf-8') as f:
        for line in f:
            try:
                e=json.loads(line)
            except json.JSONDecodeError:
                raise RuntimeError('Session audit ledger is invalid; manual recovery required')
            if e.get('session_id')==sid and e.get('event')=='FINISH':
                return True
    return False


def split_ledger(content: str) -> str:
    if LEDGER not in content:
        raise RuntimeError('Buildnotes marker missing: manual reconciliation required')
    return content.split(LEDGER,1)[1]


def quick_summary(ledger: str) -> str:
    """Actual bounded summary of merged changes; never dump archive into agent context."""
    markers = list(MARKER_RE.finditer(ledger))
    sessions = {}  # insertion order = archival merge order
    for i, m in enumerate(markers):
        body = ledger[m.end(): markers[i + 1].start() if i + 1 < len(markers) else len(ledger)]
        sid, kind = m.group(1), m.group(2)
        row = sessions.setdefault(sid, {'visualChange': [], 'specChange': [], 'paths': []})
        path_items = re.findall(r'^\s*- `(?:ADDED|MODIFIED|REMOVED)` `([^`]+)`', body, re.M)
        path_items += re.findall(r'^\s{2}- `([^`]+)` \(`', body, re.M)
        row['paths'].extend(path_items[:20])
        reqs = re.findall(r'^- Requirement: `([^`]+)`', body, re.M)
        note = re.findall(r'^- Change note: ([^\n]+)', body, re.M)
        count = len(path_items)
        if not count and kind == 'visualChange':
            counts = re.findall(r'^- Observed scoped paths: (\d+)', body, re.M)
            count = sum(int(x) for x in counts)
        row[kind].append({'count': count, 'req': reqs[0] if reqs else '', 'note': note[0] if note else ''})
    notes = ['## Quick handoff (read this first)', '',
             f'- Merged bundles: **{len(markers)}** across **{len(sessions)}** sessions.',
             '- Details below are archival; open only the relevant Session ID.',
             '', '| Session | External changes | Spec-to-Code updates | Affected paths (sample) |',
             '| --- | ---: | ---: | --- |']
    for sid, row in list(sessions.items())[-8:][::-1]:
        v = sum(x['count'] for x in row['visualChange'])
        authored = sum(x['count'] for x in row['specChange'])
        unique = list(dict.fromkeys(row['paths']))
        sample = ', '.join('`'+p.replace('|', '／')[:65]+'`' for p in unique[:3]) or '—'
        notes.append(f'| `{sid}` | {v} | {authored} | {sample} |')
    if not sessions:
        notes.append('| None | 0 | 0 | — |')
    # Preserve requirement references for latest merged session only.
    if sessions:
        last_id = next(reversed(sessions))
        reqs = sorted({x['req'] for x in sessions[last_id]['specChange'] if x['req'] and x['req']!='UNSPECIFIED'})
        if reqs:
            notes += ['', f'- Last merged session `{last_id}` requirement IDs: '+', '.join('`'+x.replace('|','／')[:60]+'`' for x in reqs[:8])+'.']
    return '\n'.join(notes)+'\n\n'


def merge(root: Path, sid: str) -> dict:
    root=guard.validate_root(root)
    validate_session(sid)
    if not is_finished(root,sid):
        raise RuntimeError('Handoff merge requires a FINISH event for exact Session ID')
    with merge_lock(root):
        p=guard.check_path(root, BUILDNOTES)
        refuse_symlink(root,p)
        existing=p.read_text(encoding='utf-8') if p.is_file() else ''
        if existing and not existing.startswith(HEAD):
            raise RuntimeError('Non-managed buildnotes: refusing overwrite')
        ledger=split_ledger(existing) if existing else '\n'
        pending=[]
        for kind in ('visualChange','specChange'):
            f=guard.check_path(root, path_for(root,kind,sid))
            refuse_symlink(root,f)
            if f.is_file():
                raw=f.read_bytes()
                if len(raw)>MAX_BYTES:
                    raise RuntimeError('Pending log exceeds safety cap: '+str(f))
                try:
                    content=raw.decode('utf-8')
                except UnicodeDecodeError:
                    raise RuntimeError('Invalid UTF-8 in pending log: '+str(f))
                if not content.startswith(header(sid,kind)):
                    raise RuntimeError(f'Pending log has wrong Session ID or type: {f}')
                digest=hashlib.sha256(raw).hexdigest()
                mark=f'<!-- SPEC2CODE-MERGED session={sid} type={kind} sha256={digest} -->'
                pending.append((kind,f,raw,mark,content))
        if not pending:
            return {'merged':0,'removed':0,'message':'NO_PENDING_SESSION_LOGS'}
        written=0
        for kind,f,raw,mark,content in pending:
            if mark not in ledger:
                ledger+='\n'+mark+'\n\n'+content.rstrip()+'\n\n'
                written+=1
        if len(ledger.encode('utf-8'))>MAX_LEDGER:
            raise RuntimeError('Buildnotes cap exceeded; archive explicitly before merging')
        new=HEAD+'\n# Spec2Code Build Notes Handoff\n\n'+quick_summary(ledger)+LEDGER+ledger
        if new!=existing:
            infra.atomic_text(p,new, root=root)
        # Re-read persisted data before unlinking any exact filename.
        persisted=p.read_text(encoding='utf-8')
        if not persisted.startswith(HEAD):
            raise RuntimeError('Buildnotes post-write verification failed')
        removed=0
        for kind,f,raw,mark,content in pending:
            if mark not in persisted or content.rstrip() not in persisted:
                raise RuntimeError('Handoff evidence not found; refusing pending-log deletion')
            if f.is_symlink() or f.read_bytes()!=raw:
                raise RuntimeError('Pending log changed since merge; refusing deletion: '+str(f))
            f.unlink()  # Exact, hash-verified, session-scoped file only; never glob/rmtree.
            removed+=1
        return {'merged':written,'removed':removed,'message':'VERIFIED_MERGED_AND_REMOVED'}
