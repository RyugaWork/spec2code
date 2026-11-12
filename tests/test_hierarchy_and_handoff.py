"""Regression tests: hierarchy and exact-session, hash-verified merge behavior."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest

GUARD = Path(__file__).resolve().parents[1] / 'scripts' / 'session_guard.py'

class HandoffTreeTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='spec2code-v04-')
        self.root=Path(self.tmp.name)
        self.write('AGENTS.md','# AGENTS\n')
        self.write('.source/backend/Sample.Api/Controllers/MemberController.cs',
                   'public class MemberController {\n    public async Task<string> GetMember() { return "ok"; }\n    public string Other() { return "x"; }\n}\n')
        self.write('.source/backend/Sample.Api/Sample.Api.csproj','<Project />')
        self.write('.source/web/src/MemberPage.tsx', 'export function MemberPage() { return null; }\n')
        self.run_git('init','-q')
        self.run_git('config','user.email','test@example.invalid')
        self.run_git('config','user.name','Automated Test')
        self.run_git('add','AGENTS.md','.source')
        self.run_git('commit','-qm','chore: initialize')

    def tearDown(self): self.tmp.cleanup()
    def write(self,name,data):
        p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(data,encoding='utf-8');return p
    def run_git(self,*args):
        p=subprocess.run(['git',*args],cwd=self.root,text=True,capture_output=True)
        self.assertEqual(p.returncode,0,p.stderr);return p.stdout.strip()
    def call(self,*args,success=True):
        p=subprocess.run([sys.executable,str(GUARD),'--root',str(self.root),*args],text=True,capture_output=True)
        if success: self.assertEqual(p.returncode,0,p.stderr)
        else: self.assertNotEqual(p.returncode,0,p.stdout)
        return p
    def sid(self): return json.loads((self.root/'.agents/state/session.json').read_text())['id']
    def pending(self,kind,sid=None): return self.root/'.handoffs/.details'/f'.{kind}.{sid or self.sid()}.md'

    def test_layer_controller_function_tree_and_matrix(self):
        self.call('start')
        self.assertTrue((self.root/'.summerize.md').exists())
        self.assertIn('Present', (self.root/'.summerize.md').read_text())
        for layer in ['Present','API','Application','DataAccess','Persistence','Security','Integrations','Delivery','Quality','Governance']:
            self.assertTrue((self.root/layer/'.summerize.md').exists(),layer)
        comp=self.root/'API/MemberController'
        self.assertTrue((comp/'.summerize.md').exists())
        self.assertIn('GetMember', (comp/'.summerize.md').read_text())
        fun=(comp/'.MemberController.GetMember.md')
        self.assertTrue(fun.exists())
        self.assertIn('Document version: `r1`', fun.read_text())
        self.assertIn('not yet verified', fun.read_text())
        self.assertTrue((self.root/'Present/MemberPage/.MemberPage.MemberPage.md').exists())
        self.call('finish')
        self.assertFalse(self.pending('specChange').exists())

    def test_spec_log_merge_and_safe_removal(self):
        self.call('start')
        sid=self.sid()
        p='.source/web/src/MemberPage.tsx'
        self.write(p,'export function MemberPage() { return 42; }\n')
        self.call('record','--paths',p,'--note','Implement approved view','--requirement','G-1')
        self.assertTrue(self.pending('specChange').exists())
        self.assertFalse(self.pending('visualChange').exists())
        function_doc = self.root / 'Present/MemberPage/.MemberPage.MemberPage.md'
        self.assertIn('Implement approved view', function_doc.read_text())
        self.assertIn(sid, function_doc.read_text())
        self.call('merge','--session-id',sid,success=False)
        self.assertTrue(self.pending('specChange').exists())
        self.call('finish')
        event=self.pending('specChange').read_text()
        sha=hashlib.sha256(event.encode()).hexdigest()
        out=self.call('merge','--session-id',sid)
        self.assertIn('removed=1',out.stdout)
        self.assertFalse(self.pending('specChange').exists())
        notes=(self.root/'.handoffs/.buildnotes.handoff.md').read_text()
        self.assertIn('Implement approved view',notes)
        self.assertIn(sha,notes)
        self.assertIn('## Quick handoff',notes)
        self.assertIn('NO_PENDING_SESSION_LOGS',self.call('merge','--session-id',sid).stdout)

    def test_legacy_crlf_pending_evidence_merges_safely(self):
        self.call('start')
        sid=self.sid()
        p='.source/web/src/MemberPage.tsx'
        self.write(p, 'export function MemberPage() { return 52; }\n')
        self.call('record','--paths',p,'--note','Approved view update')
        self.call('finish')
        pending=self.pending('specChange')
        pending.write_bytes(pending.read_bytes().replace(b'\n', b'\r\n'))
        raw_sha=hashlib.sha256(pending.read_bytes()).hexdigest()
        out=self.call('merge','--session-id',sid)
        self.assertIn('removed=1',out.stdout)
        self.assertIn(raw_sha,(self.root/'.handoffs/.buildnotes.handoff.md').read_text())
        self.assertFalse(pending.exists())

    def test_visual_and_spec_logs_from_separate_sessions(self):
        self.call('start'); old=self.sid(); self.call('finish')
        self.write('.source/backend/Sample.Api/Controllers/MemberController.cs','public class MemberController { public int Ping() => 1; }\n')
        self.run_git('add','.source/backend/Sample.Api/Controllers/MemberController.cs')
        self.run_git('commit','-qm','feat: modify controller externally')
        self.call('start'); new=self.sid()
        self.assertNotEqual(old,new)
        self.assertIn('OUT_OF_SESSION',self.pending('visualChange').read_text())
        self.assertFalse(self.pending('specChange').exists())
        self.call('finish')
        self.call('merge','--session-id',new)
        self.assertFalse(self.pending('visualChange').exists())
        self.assertIn(new,(self.root/'.handoffs/.buildnotes.handoff.md').read_text())

    def test_wrong_id_and_bad_header_do_not_delete(self):
        self.call('start');sid=self.sid()
        self.write('.source/web/src/MemberPage.tsx','export function MemberPage() { return 4; }')
        self.call('record','--paths','.source/web/src/MemberPage.tsx','--note','Approved task')
        self.call('finish')
        p=self.pending('specChange');original=p.read_text()
        p.write_text(original.replace(sid,'S2C-20200101-120000-AABBCCDD'),encoding='utf-8')
        self.call('merge','--session-id',sid,success=False)
        self.assertTrue(p.exists())
        self.assertFalse((self.root/'.handoffs/.buildnotes.handoff.md').exists())
        p.write_text(original,encoding='utf-8')
        self.call('merge','--session-id','S2C-20000101-000000-00000000',success=False)
        self.assertTrue(p.exists())

    def test_handoff_symlink_blocked(self):
        self.call('start');sid=self.sid()
        self.write('.source/web/src/MemberPage.tsx','export function MemberPage() { return 4; }')
        self.call('record','--paths','.source/web/src/MemberPage.tsx','--note','Approved task')
        self.call('finish')
        p=self.root/'.handoffs/.buildnotes.handoff.md'
        target=self.write('safe.txt','do not overwrite')
        try:
            p.symlink_to(target)
        except (OSError,NotImplementedError):
            self.skipTest('Symlinks unsupported')
        self.call('merge','--session-id',sid,success=False)
        self.assertEqual(target.read_text(),'do not overwrite')
        self.assertTrue(self.pending('specChange').exists())

    def test_function_revision_on_source_update(self):
        self.call('start');self.call('finish')
        fun=self.root/'API/MemberController/.MemberController.GetMember.md'
        self.assertIn('`r1`',fun.read_text())
        self.call('start')
        self.write('.source/backend/Sample.Api/Controllers/MemberController.cs',
                   'public class MemberController {\n    public async Task<string> GetMember() { return "change"; }\n    public string Other() { return "x"; }\n}\n')
        self.call('record','--paths','.source/backend/Sample.Api/Controllers/MemberController.cs','--note','approved function edit')
        self.assertIn('`r2`',fun.read_text())
        self.call('finish')

    def test_both_logs_merge_with_one_exact_session_id(self):
        self.call('start'); sid=self.sid()
        self.write('compose.yaml', 'services:\n  app:\n    image: example\n')
        self.run_git('add','compose.yaml')
        self.run_git('commit','-qm','chore: change external compose')
        self.call('checkpoint')
        self.write('.source/web/src/MemberPage.tsx','export function MemberPage() { return 8; }\n')
        self.call('record','--paths','.source/web/src/MemberPage.tsx',
                  '--note','Approved view update','--requirement','REQ-8')
        self.assertTrue(self.pending('visualChange').exists())
        self.assertTrue(self.pending('specChange').exists())
        self.call('finish')
        self.assertIn('removed=2',self.call('merge','--session-id',sid).stdout)
        self.assertFalse(self.pending('visualChange').exists())
        self.assertFalse(self.pending('specChange').exists())
        handoff=(self.root/'.handoffs/.buildnotes.handoff.md').read_text()
        self.assertIn('REQ-8',handoff)
        self.assertIn('External changes',handoff)
        self.assertIn('Spec-to-Code updates',handoff)

    def test_retry_after_ledger_written_does_not_duplicate_bundle(self):
        self.call('start');sid=self.sid()
        self.write('.source/web/src/MemberPage.tsx','export function MemberPage() { return 17; }\n')
        self.call('record','--paths','.source/web/src/MemberPage.tsx','--note','Recorded change')
        self.call('finish')
        original=self.pending('specChange').read_bytes()
        self.call('merge','--session-id',sid)
        first=(self.root/'.handoffs/.buildnotes.handoff.md').read_text()
        self.pending('specChange').write_bytes(original)
        out=self.call('merge','--session-id',sid)
        self.assertIn('archived=0',out.stdout)
        self.assertIn('removed=1',out.stdout)
        self.assertEqual(first,(self.root/'.handoffs/.buildnotes.handoff.md').read_text())
        self.assertFalse(self.pending('specChange').exists())

    def test_overloaded_methods_have_distinct_documents(self):
        p='.source/backend/Sample.Api/Controllers/MemberController.cs'
        self.write(p, 'public class MemberController {\n'
                      '  public int GetMember() { return 1; }\n'
                      '  public int GetMember(int id) { return id; }\n'
                      '}\n')
        self.call('start')
        comp=self.root/'API/MemberController'
        self.assertTrue((comp/'.MemberController.GetMember_L2.md').exists())
        self.assertTrue((comp/'.MemberController.GetMember_L3.md').exists())
        summ=(comp/'.summerize.md').read_text()
        self.assertIn('.MemberController.GetMember_L3.md',summ)

if __name__=='__main__': unittest.main(verbosity=2)
