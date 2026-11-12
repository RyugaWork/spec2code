"""Event-boundary checks, stale-commit invalidation and MCP host authorization."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import mcp_boundary
import path_guard
import scope_io


class ContinuousScopeTests(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory(prefix='spec2code-scope-')
        self.root = Path(self.t.name) / 'repo'
        self.root.mkdir()
        (self.root / 'src').mkdir()
        (self.root / 'src/example.py').write_text('def example(): return 1\n')
        self.git('init', '-q')
        self.git('config', 'user.email', 'test@example.invalid')
        self.git('config', 'user.name', 'Testing')
        self.git('add', '.')
        self.git('commit', '-qm', 'chore: initialize')
        self.other = Path(self.t.name) / 'outside'
        self.other.mkdir()
        (self.other / 'keep.txt').write_text('KEEP')

    def tearDown(self):
        self.t.cleanup()

    def git(self, *args):
        p = subprocess.run(['git', *args], cwd=self.root, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        return p.stdout.strip()

    def cli(self, *args, success=True):
        result = subprocess.run([sys.executable, str(SCRIPTS / 'session_guard.py'),
                                 '--root', str(self.root), *args], text=True,
                                 capture_output=True, timeout=40)
        if success:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
        return result

    def test_session_binding_is_physical_and_detects_substitution(self):
        token = path_guard.capture_scope(self.root)
        self.assertEqual(path_guard.assert_scope(self.root, token), self.root)
        moved = Path(self.t.name) / 'previous-repo'
        self.root.rename(moved)
        self.root.mkdir()
        self.git('init', '-q')
        with self.assertRaisesRegex(RuntimeError, 'SCOPE_VIOLATION'):
            path_guard.assert_scope(self.root, token)

    def test_session_status_denies_missing_binding(self):
        p = self.root / '.agents/state/session.json'
        p.parent.mkdir(parents=True)
        p.write_text(json.dumps({'status': 'ACTIVE', 'id': 'S2C-20261112-120000-AABBCCDD'}))
        res = self.cli('status', success=False)
        self.assertIn('SCOPE_VIOLATION', res.stderr)

    def test_checkpoint_invalidates_old_context_pack_on_new_commit(self):
        self.cli('start')
        pack = self.root / '.agents/state/context-pack.json'
        pack.write_text('{"schema_version":1,"session_id":"stale"}')
        (self.root / 'src/example.py').write_text('def example(): return 2\n')
        self.git('add', 'src/example.py')
        self.git('commit', '-qm', 'feat: new external revision')
        self.cli('checkpoint')
        self.assertFalse(pack.exists())
        state = json.loads((self.root / '.agents/state/session.json').read_text())
        self.assertEqual(state['last_seen_head'], self.git('rev-parse', 'HEAD'))

    def test_scope_atomic_write_rejects_symlink_and_foreign_root(self):
        target = self.root / 'src/escape.txt'
        try:
            target.symlink_to(self.other / 'keep.txt')
        except (OSError, NotImplementedError):
            self.skipTest('Symlink unavailable')
        with self.assertRaisesRegex(RuntimeError, 'PATH_GUARD_BLOCKED'):
            scope_io.atomic_text(self.root, target, 'BROKEN')
        with self.assertRaisesRegex(RuntimeError, 'PATH_GUARD_BLOCKED'):
            scope_io.atomic_text(self.root, self.other / 'keep.txt', 'BROKEN')
        self.assertEqual((self.other / 'keep.txt').read_text(), 'KEEP')

    def test_scope_atomic_write_append_and_read(self):
        dst = self.root / 'src/new/sub/path.txt'
        scope_io.atomic_text(self.root, dst, 'first\n')
        scope_io.append_text(self.root, dst, 'second\n')
        self.assertEqual(scope_io.read_bytes(self.root, dst), b'first\nsecond\n')
        if os.name == 'posix':
            self.assertTrue(scope_io._supports_anchoring())

    def test_verified_unlink_exact_hash_only(self):
        target = self.root / '.agents/.handoffs/.details/pending.md'
        scope_io.atomic_text(self.root, target, 'session-log')
        with self.assertRaisesRegex(RuntimeError, 'SCOPE_VIOLATION'):
            scope_io.unlink_verified(self.root, target, '0' * 64)
        self.assertTrue(target.exists())
        scope_io.unlink_verified(self.root, target, hashlib.sha256(b'session-log').hexdigest())
        self.assertFalse(target.exists())

    def test_read_blocked_for_symlink_and_oversize(self):
        try:
            (self.root / 'src/unsafe.txt').symlink_to(self.other / 'keep.txt')
        except (OSError, NotImplementedError):
            self.skipTest('Symlink unavailable')
        with self.assertRaisesRegex(RuntimeError, 'PATH_GUARD_BLOCKED'):
            scope_io.read_bytes(self.root, 'src/unsafe.txt')
        with self.assertRaisesRegex(RuntimeError, 'SCOPE_VIOLATION'):
            scope_io.read_bytes(self.root, 'src/example.py', max_bytes=1)

    def test_mcp_read_only_host_cannot_mutate_or_choose_repository(self):
        host = mcp_boundary.MCPWorkspaceBoundary(self.root)
        self.assertEqual(host.authorize('status').root, self.root)
        with self.assertRaisesRegex(RuntimeError, 'SCOPE_VIOLATION'):
            host.authorize('start_session')
        with self.assertRaisesRegex(RuntimeError, 'SCOPE_VIOLATION'):
            host.authorize('status', {'root': str(self.other)})
        with self.assertRaisesRegex(RuntimeError, 'SCOPE_VIOLATION'):
            host.authorize('status', {'session_id': 'arbitrary'})
        with self.assertRaisesRegex(RuntimeError, 'SCOPE_VIOLATION'):
            host.authorize('status', {'workspace_id': 'another-workspace'})
        with self.assertRaisesRegex(RuntimeError, 'SCOPE_VIOLATION'):
            host.authorize('status', {'paths': ['../outside/keep.txt']})
        with self.assertRaisesRegex(RuntimeError, 'SCOPE_VIOLATION'):
            host.authorize('exec', {'command': 'pwd'})

    def test_mcp_sensitive_paths_are_denied(self):
        host = mcp_boundary.MCPWorkspaceBoundary(self.root)
        with self.assertRaisesRegex(RuntimeError, 'SCOPE_VIOLATION'):
            host.authorize('record_change', {'paths': ['src/.env']})

    def test_mcp_write_requires_matching_session_and_fresh_head(self):
        host = mcp_boundary.MCPWorkspaceBoundary(self.root, allow_write=True)
        self.cli('start')
        session = json.loads((self.root / '.agents/state/session.json').read_text())['id']
        with self.assertRaisesRegex(RuntimeError, 'SCOPE_VIOLATION'):
            host.authorize('record_change', {'session_id': 'S2C-20261112-120000-DEADBEEF'})
        with self.assertRaisesRegex(RuntimeError, 'SCOPE_VIOLATION'):
            host.authorize('record_change')
        allowed = host.authorize('record_change', {'session_id': session, 'paths': ['src/example.py']})
        self.assertEqual(allowed.session_id, session)
        (self.root / 'src/example.py').write_text('def example(): return 3\n')
        self.git('add', 'src/example.py')
        self.git('commit', '-qm', 'feat: update code')
        with self.assertRaisesRegex(RuntimeError, 'STALE_GIT_HEAD'):
            host.authorize('record_change', {'session_id': session})
        self.assertEqual(host.authorize('checkpoint_session', {'session_id': session}).action,
                         'checkpoint_session')
        self.cli('checkpoint')
        self.assertEqual(host.authorize('record_change', {'session_id': session}).action,
                         'record_change')

    def test_mcp_rejects_active_second_session(self):
        host = mcp_boundary.MCPWorkspaceBoundary(self.root, allow_write=True)
        self.cli('start')
        with self.assertRaisesRegex(RuntimeError, 'ACTIVE_SESSION_EXISTS'):
            host.authorize('start_session')


if __name__ == '__main__':
    unittest.main()
