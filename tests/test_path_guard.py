"""Path Guard boundaries: fail closed before reads, writes, or handoff deletion."""
from __future__ import annotations
import json
import os
import shutil
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import path_guard
import scan_infrastructure as scanner
import architecture_tree as arch


class RepositoryBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='spec2code-path-guard-')
        self.repo = Path(self.tmp.name) / 'workspace'
        self.repo.mkdir()
        (self.repo / 'src').mkdir()
        (self.repo / 'src/app.py').write_text('def sample(): return 1\n')
        self.git('init', '-q')
        self.git('config', 'user.email', 'ci@example.invalid')
        self.git('config', 'user.name', 'CI')
        self.git('add', '.')
        self.git('commit', '-qm', 'chore: initialize')
        self.outside = Path(self.tmp.name) / 'outside'
        self.outside.mkdir()
        (self.outside / 'keep.txt').write_text('DO-NOT-TOUCH')

    def tearDown(self):
        self.tmp.cleanup()

    def git(self, *args):
        result = subprocess.run(['git', *args], cwd=self.repo, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def cli(self, script, root, *args, env=None):
        e = os.environ.copy()
        if env: e.update(env)
        return subprocess.run([sys.executable, str(SCRIPTS / script), '--root', str(root), *args],
                              text=True, capture_output=True, env=e, timeout=25)

    def test_exact_root_succeeds_and_subfolder_is_blocked(self):
        self.assertEqual(path_guard.validate_root(self.repo), self.repo)
        with self.assertRaisesRegex(RuntimeError, 'PATH_GUARD_BLOCKED'):
            path_guard.validate_root(self.repo / 'src')

    def test_non_git_is_blocked_for_every_entrypoint(self):
        commands = [
            ('session_guard.py', ('start',)),
            ('session_guard.py', ('status',)),
            ('session_guard.py', ('merge', '--session-id', 'S2C-20261112-120000-AABBCCDD')),
            ('scan_infrastructure.py', ()),
            ('speckit_bridge.py', ('--stage', 'status')),
            ('context_router.py', ('--task-id', 'X1', '--task', 'Review', '--mode', 'auto')),
        ]
        for script, argv in commands:
            with self.subTest(script=script, argv=argv):
                out = self.cli(script, self.outside, *argv)
                self.assertNotEqual(out.returncode, 0, (out.stdout, out.stderr))
                self.assertIn('PATH_GUARD_BLOCKED', out.stderr)
        self.assertFalse((self.outside / '.agents').exists())
        self.assertFalse((self.outside / '.handoffs').exists())
        self.assertEqual((self.outside / 'keep.txt').read_text(), 'DO-NOT-TOUCH')

    def test_nested_git_directory_rejected_for_status_and_scan(self):
        for script, args in [('session_guard.py', ('status',)), ('scan_infrastructure.py', ())]:
            out = self.cli(script, self.repo / 'src', *args)
            self.assertNotEqual(out.returncode, 0)
            self.assertIn('PATH_GUARD_BLOCKED', out.stderr)

    def test_git_dir_environment_override_is_ignored(self):
        # A caller cannot fake a repository by pointing GIT_DIR at another repo.
        out = self.cli('session_guard.py', self.outside, 'status', env={'GIT_DIR': str(self.repo / '.git')})
        self.assertNotEqual(out.returncode, 0)
        self.assertIn('PATH_GUARD_BLOCKED', out.stderr)
        self.assertFalse((self.outside / '.agents').exists())

    def test_symlinked_state_directory_refused_before_start(self):
        (self.repo / '.agents').mkdir()
        try:
            (self.repo / '.agents/state').symlink_to(self.outside, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest('Filesystem does not support symlinks')
        out = self.cli('session_guard.py', self.repo, 'start')
        self.assertNotEqual(out.returncode, 0)
        self.assertIn('PATH_GUARD_BLOCKED', out.stderr)
        self.assertFalse((self.outside / 'session.json').exists())

    def test_symlinked_buildnotes_and_layer_refused_even_on_status(self):
        for link in ('.handoffs/.buildnotes.handoff.md', 'Present'):
            with self.subTest(link=link):
                p = self.repo / link
                p.parent.mkdir(exist_ok=True, parents=True)
                try:
                    p.symlink_to(self.outside, target_is_directory=(link == 'Present'))
                except (OSError, NotImplementedError):
                    self.skipTest('Filesystem does not support symlinks')
                out = self.cli('session_guard.py', self.repo, 'status')
                self.assertNotEqual(out.returncode, 0)
                self.assertIn('PATH_GUARD_BLOCKED', out.stderr)
                p.unlink()

    def test_symlinked_skill_directory_is_rejected(self):
        (self.repo / '.agents').mkdir()
        try:
            (self.repo / '.agents/skills').symlink_to(self.outside, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest('Filesystem does not support symlinks')
        out = self.cli('session_guard.py', self.repo, 'status')
        self.assertNotEqual(out.returncode, 0)
        self.assertIn('PATH_GUARD_BLOCKED', out.stderr)

    def test_root_symlink_is_blocked(self):
        alias = Path(self.tmp.name) / 'alias'
        try:
            alias.symlink_to(self.repo, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest('Filesystem does not support symlinks')
        out = self.cli('session_guard.py', alias, 'status')
        self.assertNotEqual(out.returncode, 0)
        self.assertIn('PATH_GUARD_BLOCKED', out.stderr)

    def test_relative_absolute_and_symlink_path_escape(self):
        for value in ('../outside/keep.txt', '../../etc/passwd', 'C:\\Windows\\win.ini',
                      '//server/share/file', 'src/../../outside/file', 'src//x.py'):
            with self.subTest(value=value), self.assertRaisesRegex(RuntimeError, 'PATH_GUARD_BLOCKED'):
                path_guard.check_path(self.repo, value)
        with self.assertRaisesRegex(RuntimeError, 'PATH_GUARD_BLOCKED'):
            path_guard.check_path(self.repo, self.outside / 'keep.txt')
        try:
            (self.repo / 'src/link').symlink_to(self.outside, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest('Filesystem does not support symlinks')
        with self.assertRaisesRegex(RuntimeError, 'PATH_GUARD_BLOCKED'):
            path_guard.check_path(self.repo, 'src/link/keep.txt')

    def test_cache_document_path_escape_rejected(self):
        started = self.cli('session_guard.py', self.repo, 'start')
        self.assertEqual(started.returncode, 0, started.stderr)
        state_file = self.repo / '.agents/state/architecture-docs.json'
        data = json.loads(state_file.read_text())
        data['functions'] = {'src/app.py#sample:1': {'document': '../outside/keep.txt'}}
        state_file.write_text(json.dumps(data))
        out = self.cli('context_router.py', self.repo, '--task-id', 'T001', '--task', 'Change sample function',
                       '--paths', 'src/app.py', '--mode', 'balanced')
        self.assertNotEqual(out.returncode, 0)
        self.assertIn('PATH_GUARD_BLOCKED', out.stderr)
        self.assertFalse((self.repo / '.agents/state/context-pack.json').exists())
        self.assertEqual((self.outside / 'keep.txt').read_text(), 'DO-NOT-TOUCH')

    def test_low_level_symbol_and_inventory_readers_reject_external_path(self):
        malicious = Path('../outside/keep.txt')
        with self.assertRaisesRegex(RuntimeError, 'PATH_GUARD_BLOCKED'):
            scanner.describe_file(self.repo, malicious, None, True)
        with self.assertRaisesRegex(RuntimeError, 'PATH_GUARD_BLOCKED'):
            scanner.extract_facts(self.repo, {'../outside/package.json': {'sha256': 'fake'}}, None)
        with self.assertRaisesRegex(RuntimeError, 'PATH_GUARD_BLOCKED'):
            arch.extract_symbols(self.repo, '../outside/keep.txt', 'application', 'fake', None)
        self.assertEqual((self.outside / 'keep.txt').read_text(), 'DO-NOT-TOUCH')

    def test_nested_git_repo_not_scanned(self):
        sub = self.repo / 'src/vendor'
        sub.mkdir()
        (sub / '.git').mkdir()
        (sub / 'data.py').write_text('TOP_SECRET = "nested repo"')
        self.assertNotIn(Path('src/vendor/data.py'), scanner.all_files(self.repo))

    def test_symlinked_source_is_not_read(self):
        try:
            (self.repo / 'src/outside.py').symlink_to(self.outside / 'keep.txt')
        except (OSError, NotImplementedError):
            self.skipTest('Filesystem does not support symlinks')
        self.assertNotIn(Path('src/outside.py'), scanner.all_files(self.repo))

    def test_installed_skill_cannot_target_another_valid_git_repository(self):
        installed = self.repo / '.agents/skills/spec-to-code/scripts'
        installed.mkdir(parents=True)
        shutil.copy2(SCRIPTS / 'path_guard.py', installed / 'path_guard.py')
        other = Path(self.tmp.name) / 'other-repo'
        other.mkdir()
        subprocess.run(['git', 'init', '-q'], cwd=other, check=True)
        snippet = ('import path_guard; path_guard.validate_root(' + repr(str(other)) + ')')
        env = os.environ.copy()
        env['PYTHONPATH'] = str(installed)
        out = subprocess.run([sys.executable, '-c', snippet], capture_output=True, text=True, env=env)
        self.assertNotEqual(out.returncode, 0)
        self.assertIn('PATH_GUARD_BLOCKED: installed skill belongs to a different checkout', out.stderr)
        snippet = ('import path_guard; path_guard.validate_root(' + repr(str(self.repo)) + ')')
        allowed = subprocess.run([sys.executable, '-c', snippet], capture_output=True, text=True, env=env)
        self.assertEqual(allowed.returncode, 0, allowed.stderr)

    def test_valid_git_worktree_supported(self):
        extra = Path(self.tmp.name) / 'linked-worktree'
        self.git('worktree', 'add', '--detach', str(extra), 'HEAD')
        self.assertEqual(path_guard.validate_root(extra), extra)
        out = self.cli('session_guard.py', extra, 'status')
        self.assertEqual(out.returncode, 0, out.stderr)


if __name__ == '__main__':
    unittest.main()
