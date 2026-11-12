"""Target layout regression and legacy migration safety for v0.7.0."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'


class TargetCheckoutLayoutTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='s2c-target-layout-')
        self.root = Path(self.temp.name) / 'repo'
        self.root.mkdir()
        (self.root / 'src').mkdir()
        (self.root / 'src/example.py').write_text('def example():\n    return 1\n', encoding='utf-8')
        for args in [('init','-q'),('config','user.name','Tester'),('config','user.email','test@example.invalid'),
                     ('add','.'),('commit','-qm','chore: init')]:
            result = subprocess.run(['git', *args], cwd=self.root, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)

    def tearDown(self):
        self.temp.cleanup()

    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPTS / 'session_guard.py'), '--root', str(self.root), *args],
                              capture_output=True, text=True, timeout=60)

    def test_new_layout_is_entirely_under_reserved_folders(self):
        started = self.run_cli('start')
        self.assertEqual(started.returncode, 0, started.stderr)
        self.assertTrue((self.root/'s2c/.summerize.md').is_file())
        self.assertTrue((self.root/'s2c/Application/.summerize.md').is_file())
        self.assertFalse((self.root/'.summerize.md').exists())
        self.assertFalse((self.root/'Application').exists())
        state = json.loads((self.root/'.agents/state/architecture-docs.json').read_text())
        self.assertTrue(all(p.startswith('s2c/') for p in state['generated_paths']))
        self.assertTrue(all(v['document'].startswith('s2c/') for v in state['functions'].values()))
        sid=json.loads((self.root/'.agents/state/session.json').read_text())['id']
        source=self.root/'src/example.py'
        source.write_text('def example():\n    return 2\n',encoding='utf-8')
        recorded=self.run_cli('record','--paths','src/example.py','--note','Approved change')
        self.assertEqual(recorded.returncode, 0, recorded.stderr)
        pending=self.root/'.agents/.handoffs/.details'/f'.specChange.{sid}.md'
        self.assertTrue(pending.is_file())
        self.assertEqual(self.run_cli('finish').returncode, 0)
        self.assertEqual(self.run_cli('merge','--session-id',sid).returncode,0)
        self.assertFalse(pending.exists())
        self.assertTrue((self.root/'.agents/.handoffs/.buildnotes.handoff.md').is_file())
        self.assertFalse((self.root/'.handoffs').exists())

    def test_legacy_pending_logs_block_without_source_mutation(self):
        old=self.root/'.handoffs/.details/.specChange.S2C-20261112-010101-AABBCCDD.md'
        old.parent.mkdir(parents=True)
        old.write_bytes(b'legacy protected handoff\r\n')
        snapshot=(self.root/'src/example.py').read_bytes()
        out=self.run_cli('start')
        self.assertNotEqual(out.returncode,0)
        self.assertIn('LAYOUT_MIGRATION_REQUIRED',out.stderr)
        self.assertEqual(old.read_bytes(),b'legacy protected handoff\r\n')
        self.assertEqual(snapshot,(self.root/'src/example.py').read_bytes())
        self.assertFalse((self.root/'.agents/state/session.json').exists())

    def test_nonmanaged_s2c_output_directory_does_not_get_overwritten(self):
        owned=self.root/'s2c/data.txt'
        owned.parent.mkdir()
        owned.write_bytes(b'user data - preserve')
        out=self.run_cli('start')
        self.assertNotEqual(out.returncode,0)
        self.assertIn('ARCH_OUTPUT_COLLISION',out.stderr)
        self.assertEqual(owned.read_bytes(),b'user data - preserve')
        self.assertFalse((self.root/'s2c/.summerize.md').exists())

    def test_legacy_architecture_state_requires_manual_migration(self):
        legacy=self.root/'.agents/state/architecture-docs.json'
        legacy.parent.mkdir(parents=True)
        legacy.write_text(json.dumps({'schema_version':1,'generated_paths':['API/.summerize.md'],
                        'functions':{}}), encoding='utf-8')
        out=self.run_cli('start')
        self.assertNotEqual(out.returncode,0)
        self.assertIn('LAYOUT_MIGRATION_REQUIRED',out.stderr)
        self.assertEqual(json.loads(legacy.read_text())['generated_paths'], ['API/.summerize.md'])
        self.assertFalse((self.root/'s2c/.summerize.md').exists())

    def test_installed_bundle_style_governance_workflow_smoke(self):
        """Exercise actual CLI entrypoints on a disposable host checkout."""
        self.assertEqual(self.run_cli('start').returncode, 0)
        task = 'Update example function'
        route = subprocess.run([
            sys.executable, str(SCRIPTS / 'context_router.py'), '--root',
            str(self.root), '--task-id', 'T001', '--task', task,
            '--paths', 'src/example.py', '--speckit-stage', 'status'],
            capture_output=True, text=True, timeout=60)
        self.assertEqual(route.returncode, 0, route.stderr)
        pack = json.loads((self.root / '.agents/state/context-pack.json').read_text())
        self.assertIn('governance', pack)
        self.assertIn('status', pack['governance'])
        common = ['--root', str(self.root), 'begin', '--task-id', 'T001',
                  '--task', task, '--paths', 'src/example.py']
        begin = subprocess.run([sys.executable, str(SCRIPTS / 'workflow_guard.py'), *common],
                               capture_output=True, text=True, timeout=60)
        self.assertEqual(begin.returncode, 0, begin.stderr)
        initial = json.loads(begin.stdout)
        self.assertFalse(initial['release_authorized'])
        status = subprocess.run([
            sys.executable, str(SCRIPTS / 'workflow_guard.py'), '--root',
            str(self.root), 'evaluate', '--task-id', 'T001',
            '--phase', 'DISCOVER', '--task', task, '--paths', 'src/example.py'],
            capture_output=True, text=True, timeout=60)
        self.assertEqual(status.returncode, 0, status.stderr)
        report = json.loads(status.stdout)
        self.assertEqual(report['gate_status'], 'READY')
        self.assertFalse(report['can_grant_permissions'])


if __name__ == '__main__':
    unittest.main()
