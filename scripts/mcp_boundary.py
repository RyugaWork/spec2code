#!/usr/bin/env python3
"""MCP-ready workspace authorization boundary; NOT an MCP server or transport.

A trusted MCP host constructs one instance for its configured checkout. Client
arguments may refer to approved repository-relative paths but cannot choose the
checkout, grant themselves write permission, or run shell commands.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
from typing import Mapping

import path_guard as guard
import scan_infrastructure as infra
import config_loader

MCP_CONFIG = config_loader.load('mcp')
READ_ACTIONS = frozenset(MCP_CONFIG['read_actions'])
WRITE_ACTIONS = frozenset(MCP_CONFIG['write_actions'])
ACTION_ARGS = {name: frozenset(args) for name,args in MCP_CONFIG['action_arguments'].items()}


@dataclass(frozen=True)
class AuthorizedAction:
    action: str
    root: Path
    paths: tuple[str, ...]
    session_id: str | None


class MCPWorkspaceBoundary:
    """Guard each MCP request against one trusted, immutable workspace binding."""

    def __init__(self, trusted_checkout: str | Path, *, allow_write: bool = False):
        self._root = guard.validate_root(trusted_checkout)
        self._scope = guard.capture_scope(self._root)
        self._allow_write = bool(allow_write)  # Server-side policy, never client-supplied.
        fingerprint = hashlib.sha256(json.dumps(self._scope, sort_keys=True).encode()).hexdigest()
        self.workspace_id = 's2c-' + fingerprint[:16]

    def authorize(self, action: str, arguments: Mapping[str, object] | None = None) -> AuthorizedAction:
        args = dict(arguments or {})
        if action not in (READ_ACTIONS | WRITE_ACTIONS):
            raise RuntimeError('SCOPE_VIOLATION: unsupported MCP action; no arbitrary shell capability')
        # The request cannot change which workspace the server acts on, even if
        # the supplied alternate checkout would separately pass Git validation.
        if any(key in args for key in ('root', 'repository', 'cwd', 'working_dir', 'command', 'shell')):
            raise RuntimeError('SCOPE_VIOLATION: MCP client cannot select root or execute shell')
        if args.get('workspace_id', self.workspace_id) != self.workspace_id:
            raise RuntimeError('SCOPE_VIOLATION: MCP workspace identity mismatch')
        unexpected = set(args) - ACTION_ARGS[action] - {'workspace_id'}
        if unexpected:
            raise RuntimeError('SCOPE_VIOLATION: unsupported MCP action parameters')
        if 'layer' in args and (not isinstance(args['layer'], str)
                                or not args['layer'].isalnum() or len(args['layer']) > 32):
            raise RuntimeError('SCOPE_VIOLATION: invalid layer selector')
        if 'stage' in args and args['stage'] not in ('status','specify','plan','tasks','analyze','implement','converge'):
            raise RuntimeError('SCOPE_VIOLATION: invalid Spec Kit stage')
        guard.assert_scope(self._root, self._scope)
        if action in WRITE_ACTIONS and not self._allow_write:
            raise RuntimeError('SCOPE_VIOLATION: MCP write capability not granted by host')
        raw_paths = args.get('paths', [])
        if not isinstance(raw_paths, list) or len(raw_paths) > 48 or not all(isinstance(x, str) for x in raw_paths):
            raise RuntimeError('SCOPE_VIOLATION: invalid MCP path list')
        paths = tuple(guard.check_path(self._root, p).relative_to(self._root).as_posix() for p in raw_paths)
        if any(infra.is_sensitive(Path(p).name) for p in paths):
            raise RuntimeError('SCOPE_VIOLATION: sensitive paths cannot be routed through MCP')

        state = infra.read_json(self._root / '.agents/state/session.json', root=self._root)
        active = bool(state and state.get('status') == 'ACTIVE')
        if active:
            guard.assert_scope(self._root, state.get('repository_binding'))
        requested_session = args.get('session_id')
        if requested_session is not None and (not isinstance(requested_session, str)
                                              or not state or state.get('id') != requested_session):
            raise RuntimeError('SCOPE_VIOLATION: MCP Session ID mismatch')
        if action == 'start_session' and active:
            raise RuntimeError('ACTIVE_SESSION_EXISTS: checkpoint instead of starting a new session')
        if action in {'record_change', 'finish_session', 'checkpoint_session'}:
            if not active or requested_session != state['id']:
                raise RuntimeError('SCOPE_VIOLATION: active Session ID required')
        if action == 'merge_handoff':
            if not state or state.get('status') != 'CLOSED' or requested_session != state.get('id'):
                raise RuntimeError('SCOPE_VIOLATION: closed exact Session ID required for merge')
        # A commit can arrive between session creation and any operation. Permit
        # checkpoint as the designated revalidation operation; block all other
        # write actions until HEAD has been reconciled.
        if active and action in (WRITE_ACTIONS - {'checkpoint_session'}):
            import session_guard
            head = session_guard.git(self._root, 'rev-parse', 'HEAD')
            if head != state.get('last_seen_head'):
                raise RuntimeError('STALE_GIT_HEAD: checkpoint before MCP writes')
        return AuthorizedAction(action=action, root=self._root, paths=paths,
                                session_id=requested_session if isinstance(requested_session, str) else None)
