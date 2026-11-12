"""Unit checks for the read-only infrastructure collector. No network or user repo."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import scan_infrastructure as infra


class InventorySafetyTests(unittest.TestCase):
    def test_secrets_excluded_and_config_metadata_only(self):
        self.assertFalse(infra.tracked_candidate(Path('.source/.env')))
        self.assertFalse(infra.tracked_candidate(Path('.source/web/.env.production')))
        self.assertFalse(infra.tracked_candidate(Path('.source/web/node_modules/lib/index.ts')))
        self.assertFalse(infra.tracked_candidate(Path('visualChange.md')))
        self.assertFalse(infra.tracked_candidate(Path('specChange.md')))
        self.assertTrue(infra.metadata_only('appsettings.json'))
        self.assertTrue(infra.metadata_only('appsettings.Production.json'))

    def test_direct_cli_cannot_persist_and_does_not_log_visual(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'AGENTS.md').write_text('# Example\n')
            p = subprocess.run([sys.executable, str(SCRIPTS / 'scan_infrastructure.py'),
                                '--root', str(root)], text=True, capture_output=True)
            self.assertNotEqual(p.returncode, 0)
            self.assertIn('PATH_GUARD_BLOCKED', p.stderr)
            self.assertFalse((root / '.agents/state/infrastructure.json').exists())
            self.assertFalse((root / 'visualChange.md').exists())

    def test_dependency_indicators_are_not_runtime_claims(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            f = root / '.source/backend/Sample.Api/Program.cs'
            f.parent.mkdir(parents=True)
            f.write_text('builder.Services.AddIdentityCore<User>();')
            inventory = {f.relative_to(root).as_posix(): {'sha256': infra.sha256_file(f), 'size': f.stat().st_size}}
            facts = infra.extract_facts(root, inventory, None)
            self.assertIn('AddIdentityCore', facts[f.relative_to(root).as_posix()]['startup_signals'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
