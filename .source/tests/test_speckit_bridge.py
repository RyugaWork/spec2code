"""Read-only Spec Kit integration against disposable repositories."""
from __future__ import annotations

import json
from pathlib import Path
import os
import subprocess
import sys
import tempfile
import unittest
from platform_support import requires_anchored_io
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import speckit_bridge as bridge
import scan_infrastructure as inventory


class SpecKitBridgeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='s2c-speckit-')
        self.root = Path(self.tmp.name)
        self.write('src/service.py', 'def calculate(value):\n    return value + 1\n')
        self.git('init', '-q')
        self.git('config', 'user.email', 'ci@example.test')
        self.git('config', 'user.name', 'CI Test')
        self.git('add', '.')
        self.git('commit', '-qm', 'chore: baseline')

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, p, content):
        f = self.root / p
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(content, encoding='utf-8')
        return f

    def git(self, *args):
        p = subprocess.run(['git', *args], cwd=self.root, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        return p.stdout.strip()

    def install_feature(self, *, plan=True, tasks=True):
        self.write('.specify/feature.json', json.dumps({'feature_directory': 'specs/001-data'}))
        self.write('.specify/memory/constitution.md', '# Constitution\n')
        self.write('specs/001-data/spec.md', '# Spec\nREQ-001\n')
        if plan:
            self.write('specs/001-data/plan.md', '# Plan\n')
        if tasks:
            self.write('specs/001-data/tasks.md', '- [ ] T001 Implement\n- [x] T002 Test\n')

    def test_uninitialized_read_only(self):
        result = bridge.discover(self.root)
        self.assertEqual(result['status'], 'NOT_INITIALIZED')
        self.assertFalse((self.root / '.agents').exists())

    @requires_anchored_io
    def test_active_feature_static_manifest_without_content(self):
        self.install_feature()
        result = bridge.discover(self.root, 'implement')
        self.assertEqual(result['feature_id'], '001-data')
        self.assertEqual(result['artifacts']['tasks.md']['task_count'], 2)
        self.assertIn('specs/001-data/tasks.md', result['artifacts']['tasks.md']['path'])
        self.assertNotIn('REQ-001', json.dumps(result))

    @requires_anchored_io
    def test_missing_plan_blocks_implement(self):
        self.install_feature(plan=False)
        with self.assertRaisesRegex(RuntimeError, 'SPEC_KIT_GATE_BLOCKED'):
            bridge.discover(self.root, 'implement')
        self.assertFalse((self.root / 'specs/001-data/plan.md').exists())

    @requires_anchored_io
    def test_duplicate_pointer_keys_block_discovery(self):
        self.install_feature()
        self.write('.specify/feature.json',
                   '{"feature_directory":"specs/001-data","feature_directory":"specs/001-data"}')
        with self.assertRaisesRegex(RuntimeError, 'INVALID_FEATURE_POINTER_JSON'):
            bridge.discover(self.root)

    @requires_anchored_io
    def test_each_empty_mandatory_artifact_blocks_implement(self):
        for name in bridge.ARTIFACTS:
            with self.subTest(name=name):
                self.install_feature()
                self.write('specs/001-data/' + name, ' \n\t')
                with self.assertRaisesRegex(RuntimeError, 'SPEC_KIT_GATE_BLOCKED: empty'):
                    bridge.discover(self.root, 'implement')

    @requires_anchored_io
    def test_duplicate_task_ids_beyond_sample_cap_block_discovery(self):
        self.install_feature()
        tasks = [f'- [ ] T{i:03} Task {i}' for i in range(1, bridge.MAX_TASK_IDS + 2)]
        self.write('specs/001-data/tasks.md', '\n'.join(tasks + ['- [x] **T001** Repeated']))
        with self.assertRaisesRegex(RuntimeError, 'DUPLICATE_SPEC_KIT_TASK_ID'):
            bridge.discover(self.root, 'implement')

    @requires_anchored_io
    def test_override_cannot_change_authoritative_feature(self):
        self.install_feature()
        self.write('specs/002-other/spec.md', '# Other spec')
        with patch.dict(os.environ, {'SPECIFY_FEATURE_DIRECTORY': 'specs/002-other'}):
            with self.assertRaisesRegex(RuntimeError, 'FEATURE_OVERRIDE_MISMATCH'):
                bridge.discover(self.root, 'implement')
        with patch.dict(os.environ, {'SPECIFY_FEATURE_DIRECTORY': 'specs/001-data'}):
            self.assertEqual(bridge.discover(self.root, 'implement')['feature_id'], '001-data')

    @requires_anchored_io
    def test_external_feature_pointer_rejected(self):
        self.write('.specify/feature.json', '{"feature_directory":"../secrets"}')
        with self.assertRaisesRegex(RuntimeError, 'EXTERNAL_FEATURE_DIRECTORY_BLOCKED'):
            bridge.discover(self.root)

    def test_symlinked_feature_pointer_rejected(self):
        self.write('external.json', '{"feature_directory":"specs/001-data"}')
        (self.root / '.specify').mkdir(exist_ok=True)
        try:
            (self.root / '.specify/feature.json').symlink_to(self.root / 'external.json')
        except (OSError, NotImplementedError):
            self.skipTest('Filesystem cannot create symlinks')
        with self.assertRaisesRegex(RuntimeError, 'UNSAFE_FEATURE_POINTER'):
            bridge.discover(self.root)

    @requires_anchored_io
    def test_generic_src_inventory_and_function_graph(self):
        self.assertIn(Path('src/service.py'), inventory.all_files(self.root))
        import session_guard
        out = subprocess.run([sys.executable, str(SCRIPTS / 'session_guard.py'),
                              '--root', str(self.root), 'start'], capture_output=True, text=True,
                             timeout=30)
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertTrue((self.root / 's2c/Application/service/.service.calculate.md').exists())
        self.assertTrue((self.root / 's2c/.summerize.md').exists())

    @requires_anchored_io
    def test_router_includes_spec_kit_artifacts(self):
        self.install_feature()
        import session_guard
        p = subprocess.run([sys.executable, str(SCRIPTS / 'session_guard.py'),
                            '--root', str(self.root), 'start'], capture_output=True, text=True,
                           timeout=30)
        self.assertEqual(p.returncode, 0, p.stderr)
        import context_router
        result = context_router.route(self.root, 'T001', 'Implement calculation',
                                      ['src/service.py'], 'calculate', 'auto', 0, 'implement')
        self.assertEqual(result['spec_kit']['feature_id'], '001-data')
        self.assertTrue(result['spec_kit']['artifacts']['spec.md']['exists'])
        self.assertNotIn('REQ-001', (self.root / context_router.PACK).read_text())


if __name__ == '__main__':
    unittest.main()
