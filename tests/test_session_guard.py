"""Integration tests use a synthetic temporary Git repository. No network."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
GUARD = SCRIPTS / 'session_guard.py'


class SessionGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='spec2code-session-test-')
        self.root = Path(self.temp.name)
        self.write('AGENTS.md', '# Rules\n')
        self.write('.source/backend/Sample.Api/Program.cs', 'app.MapControllers();\n')
        self.write('.source/backend/Sample.Api/Sample.Api.csproj', '<Project />\n')
        self.write('.source/backend/Sample.Business/.gitkeep', '')
        self.write('.source/backend/Sample.DataAccess/.gitkeep', '')
        self.write('.source/web/package.json', '{"dependencies":{"react":"19"}}\n')
        self.write('.source/.env', 'DATABASE_PASSWORD=ULTRA_PRIVATE')
        self.git('init', '-q')
        self.git('config', 'user.email', 'dev@example.local')
        self.git('config', 'user.name', 'Example')
        self.git('add', 'AGENTS.md', '.source/backend', '.source/web')
        self.git('commit', '-qm', 'chore: setup repository')

    def tearDown(self):
        self.temp.cleanup()

    def write(self, path, content):
        p = self.root / path
        p.parent.mkdir(exist_ok=True, parents=True)
        p.write_text(content, encoding='utf-8')
        return p

    def git(self, *args):
        p = subprocess.run(['git', *args], cwd=self.root, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, f'{args}: {p.stderr}')
        return p.stdout.strip()

    def call(self, *args, success=True):
        result = subprocess.run([sys.executable, str(GUARD), '--root', str(self.root), *args],
                                capture_output=True, text=True)
        if success:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
        return result

    def state(self):
        return json.loads((self.root / '.agents/state/session.json').read_text())

    def test_session_baseline_no_change_and_linked_layers(self):
        first = self.call('start')
        self.assertIn('SESSION_START', first.stdout)
        self.assertIn('BASELINE', first.stdout)
        self.assertFalse((self.root / '.handoffs/.details' / f'.visualChange.{self.state()["id"]}.md').exists())
        self.assertFalse((self.root / '.handoffs/.details' / f'.specChange.{self.state()["id"]}.md').exists())
        summary = (self.root / '.agents/state/layerSummary.md').read_text()
        self.assertIn('scaffold_only', summary)
        self.assertIn('api', summary)
        graph = json.loads((self.root / '.agents/state/system-graph.json').read_text())
        self.assertFalse(graph['edges'], 'Do not fabricate dependencies for generic projects')
        self.assertIn('No changed layers', (self.root / '.agents/state/impactMatrix.md').read_text())
        self.assertIn('api |', self.call('inspect', '--layer', 'api').stdout)
        self.assertIn('NO', self.call('checkpoint').stdout.replace('changed=0', 'NO'))
        self.call('finish')
        self.assertEqual(self.state()['status'], 'CLOSED')
        self.assertIn('NO_CHANGE', self.call('start').stdout)

    def test_out_of_session_commit_classification(self):
        self.call('start')
        self.call('finish')
        self.write('.source/backend/Sample.Api/Controllers/MemberController.cs', 'class MemberController {}\n')
        self.git('add', '.source/backend/Sample.Api/Controllers/MemberController.cs')
        self.git('commit', '-qm', 'feat(api): add member endpoint')
        second = self.call('start')
        self.assertIn('OUT_OF_SESSION_CHANGE', second.stdout)
        visual = (self.root / '.handoffs/.details' / f'.visualChange.{self.state()["id"]}.md').read_text()
        self.assertIn('OUT_OF_SESSION', visual)
        self.assertIn('MemberController.cs', visual)
        self.assertIn('external_commits=1', second.stdout)
        self.assertIn('.source/backend/Sample.Api/Controllers/MemberController.cs', self.state()['startup_external_paths'])
        self.assertFalse((self.root / '.handoffs/.details' / f'.specChange.{self.state()["id"]}.md').exists())
        matrix = (self.root / '.agents/state/impactMatrix.md').read_text()
        self.assertIn('| api |', matrix)

    def test_internal_record_is_not_external(self):
        self.call('start')
        self.write('.source/backend/Sample.Api/Program.cs', 'app.MapControllers();\napp.UseAuthorization();\n')
        self.call('record', '--paths', '.source/backend/Sample.Api/Program.cs',
                  '--note', 'Apply approved auth middleware', '--requirement', 'S2C-SEC-02')
        self.assertFalse((self.root / '.handoffs/.details' / f'.visualChange.{self.state()["id"]}.md').exists())
        self.assertIn('S2C-SEC-02', (self.root / '.handoffs/.details' / f'.specChange.{self.state()["id"]}.md').read_text())
        self.call('finish')
        self.assertEqual(self.state()['record_count'], 1)
        self.assertIn('NO_CHANGE', self.call('start').stdout)
        self.assertFalse((self.root / '.handoffs/.details' / f'.visualChange.{self.state()["id"]}.md').exists())

    def test_unattributed_change_blocks_finish(self):
        self.call('start')
        self.write('.source/web/src/Main.tsx', 'export default function Main() {}')
        result = self.call('finish', success=False)
        self.assertIn('BLOCKED_UNCLASSIFIED', result.stdout)
        self.assertEqual(self.state()['status'], 'ACTIVE')
        self.call('record', '--paths', '.source/web/src/Main.tsx', '--note', 'Create entry component')
        self.call('finish')

    def test_modified_after_record_requires_new_record(self):
        self.call('start')
        p = '.source/backend/Sample.Api/Program.cs'
        self.write(p, 'code first\n')
        self.call('record', '--paths', p, '--note', 'First edit')
        self.write(p, 'code second\n')
        self.call('finish', success=False)
        self.call('record', '--paths', p, '--note', 'Second edit')
        self.call('finish')

    def test_incoming_commit_during_session(self):
        self.call('start')
        self.write('compose.yaml', 'services:\n  api:\n    image: test\n')
        self.git('add', 'compose.yaml')
        self.git('commit', '-qm', 'chore: add compose without session trailer')
        result = self.call('checkpoint')
        self.assertIn('external_commits=1', result.stdout)
        self.assertIn('EXTERNAL_COMMIT_DURING_SESSION', (self.root / '.handoffs/.details' / f'.visualChange.{self.state()["id"]}.md').read_text())
        self.call('finish')

    def test_internal_commits_using_trailer(self):
        self.call('start')
        sid = self.state()['id']
        p = '.source/backend/Sample.Api/Program.cs'
        self.write(p, 'code modified\n')
        self.git('add', p)
        self.git('commit', '-qm', f'feat(api): update entrypoint\n\nSpec2Code-Session: {sid}')
        self.call('record', '--paths', p, '--note', 'Entry point update')
        self.call('finish')
        self.assertFalse((self.root / '.handoffs/.details' / f'.visualChange.{self.state()["id"]}.md').exists())

    def test_observed_project_reference_upgrades_graph_evidence(self):
        self.write('.source/backend/Sample.Business/Sample.Business.csproj', '<Project />')
        self.write('.source/backend/Sample.Api/Sample.Api.csproj',
                   '<Project><ItemGroup><ProjectReference Include="../Sample.Business/Sample.Business.csproj" /></ItemGroup></Project>')
        self.call('start')
        graph = json.loads((self.root / '.agents/state/system-graph.json').read_text())
        found = [e for e in graph['edges'] if e['from'] == 'api' and e['to'] == 'application']
        self.assertEqual(found[0]['evidence_level'], 'observed_project_reference')
        self.assertIn('application*', (self.root / '.agents/state/layerSummary.md').read_text())

    def test_session_jsonl_has_valid_records(self):
        self.call('start')
        self.call('finish')
        events = (self.root / '.agents/state/sessions.jsonl').read_text().splitlines()
        parsed = [json.loads(record) for record in events]
        self.assertEqual([r['event'] for r in parsed], ['START', 'FINISH'])
        self.assertEqual(parsed[0]['session_id'], parsed[1]['session_id'])

    def test_secret_exclusion(self):
        self.call('start')
        for name in ('infrastructure.json', 'system-graph.json', 'layerSummary.md', 'impactMatrix.md'):
            text = next((self.root / '.agents/state').glob(name)).read_text()
            self.assertNotIn('ULTRA_PRIVATE', text)
        self.assertNotIn('.source/.env', json.loads((self.root / '.agents/state/infrastructure.json').read_text())['files'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
