"""Bundled configuration and security invariant regression checks."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch
import sys
import tempfile

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import config_loader
import context_router
import scan_infrastructure as scanner


class ConfigLoaderTests(TestCase):
    def test_all_bundled_configs_load_and_validate(self):
        for section in sorted(config_loader.CONFIG_NAMES):
            self.assertEqual(config_loader.load(section)['schema_version'], 1)

    def test_scanner_values_come_from_json(self):
        policy = config_loader.load('scanner')
        self.assertEqual(scanner.SOURCE_ROOTS, set(policy['source_roots']))
        self.assertEqual(scanner.FILE_CAP, policy['limits']['file_cap'])

    def test_reject_untrusted_scanner_source_root(self):
        policy=deepcopy(config_loader.load('scanner'))
        policy['source_roots'].append('../outside')
        with self.assertRaisesRegex(RuntimeError,'CONFIG_INVALID'):
            config_loader._validate('scanner', policy)

    def test_reject_downgraded_secret_protection(self):
        policy=deepcopy(config_loader.load('scanner'))
        policy['metadata_only_files'].remove('credentials.json')
        with self.assertRaisesRegex(RuntimeError,'CONFIG_INVALID'):
            config_loader._validate('scanner', policy)

    def test_reject_reserved_runtime_state_destination(self):
        policy=deepcopy(config_loader.load('session'))
        policy['paths']['session']='src/session.json'
        with self.assertRaisesRegex(RuntimeError,'CONFIG_INVALID'):
            config_loader._validate('session', policy)

    def test_reject_source_overwrite_as_architecture_output(self):
        policy=deepcopy(config_loader.load('architecture'))
        policy['layer_directories']['application']='src'
        with self.assertRaisesRegex(RuntimeError,'CONFIG_INVALID'):
            config_loader._validate('architecture', policy)

    def test_target_handoff_layout_cannot_escape_reserved_folder(self):
        policy=deepcopy(config_loader.load('handoff'))
        policy['paths']['buildnotes']='.handoffs/.buildnotes.handoff.md'
        with self.assertRaisesRegex(RuntimeError,'CONFIG_INVALID'):
            config_loader._validate('handoff',policy)

    def test_target_architecture_root_cannot_retarget_source(self):
        policy=deepcopy(config_loader.load('architecture'))
        policy['output_root']='src'
        with self.assertRaisesRegex(RuntimeError,'CONFIG_INVALID'):
            config_loader._validate('architecture',policy)

    def test_reserved_s2c_directory_not_scannable(self):
        policy=deepcopy(config_loader.load('scanner'))
        policy['source_roots'].append('s2c')
        with self.assertRaisesRegex(RuntimeError,'CONFIG_INVALID'):
            config_loader._validate('scanner',policy)

    def test_speckit_implementation_gate_cannot_be_disabled(self):
        policy=deepcopy(config_loader.load('speckit'))
        policy['stage_prerequisites']['implement'].remove('tasks.md')
        with self.assertRaisesRegex(RuntimeError,'CONFIG_INVALID'):
            config_loader._validate('speckit', policy)

    def test_mcp_action_and_permissions_cannot_be_escalated(self):
        policy=deepcopy(config_loader.load('mcp'))
        policy['read_actions'].append('shell')
        policy['action_arguments']['shell']=['command']
        with self.assertRaisesRegex(RuntimeError,'CONFIG_INVALID'):
            config_loader._validate('mcp', policy)

    def test_context_override_cannot_remove_high_risk_floor(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t)
            state=root/'.agents/state';state.mkdir(parents=True)
            (state/'context-policy.json').write_text(json.dumps({
                'schema_version':1,'high_risk_patterns':[], 'default_mode':'minimal',
            }))
            # Mock only the local JSON reading edge: load_policy needs no Git calls.
            with patch.object(context_router, 'read_json', side_effect=lambda _root, path: json.loads(path.read_text())):
                result=context_router.load_policy(root)
            self.assertIn('auth', result['high_risk_patterns'])
            mode,_=context_router.classify('authentication', ['src/auth.py'], {'application'},False,result,'minimal')
            self.assertEqual(mode,'deep')

    def test_missing_bundled_config_fails_closed(self):
        with tempfile.TemporaryDirectory() as t:
            fake=Path(t)/'scripts/config_loader.py';fake.parent.mkdir()
            fake.write_text('')
            with patch.object(config_loader,'__file__',str(fake)):
                config_loader.load.cache_clear()
                with self.assertRaisesRegex(RuntimeError,'CONFIG_INVALID'):
                    config_loader.load('scanner')
            config_loader.load.cache_clear()

    def test_invalid_json_and_duplicate_keys_are_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            scripts=Path(t)/'scripts';scripts.mkdir()
            fake=scripts/'config_loader.py';fake.write_text('')
            bundle=Path(t)/'.config';bundle.mkdir()
            cfg=bundle/'scanner.json'
            cfg.write_text('{"schema_version":1,"schema_version":1}')
            with patch.object(config_loader,'__file__',str(fake)):
                config_loader.load.cache_clear()
                with self.assertRaisesRegex(RuntimeError,'CONFIG_INVALID'):
                    config_loader.load('scanner')
            config_loader.load.cache_clear()

    def test_symlinked_bundled_config_is_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);(root/'scripts').mkdir()
            fake=root/'scripts/config_loader.py';fake.write_text('')
            (root/'.config').mkdir()
            other=root/'outside.json';other.write_text('{}')
            try:
                (root/'.config/scanner.json').symlink_to(other)
            except (OSError,NotImplementedError):
                self.skipTest('symlinks not supported in this test environment')
            with patch.object(config_loader,'__file__',str(fake)):
                config_loader.load.cache_clear()
                with self.assertRaisesRegex(RuntimeError,'CONFIG_INVALID'):
                    config_loader.load('scanner')
            config_loader.load.cache_clear()
