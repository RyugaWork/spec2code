"""Adaptive mode tests. Synthetic source and metadata; no remote or LLM calls."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

ROOT_SCRIPTS=Path(__file__).resolve().parents[1]/'scripts'
sys.path.insert(0,str(ROOT_SCRIPTS))
import context_router as router
import path_guard as guard


class AdaptiveModeTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='spec2code-adaptive-')
        self.root=Path(self.tmp.name)
        self.paths=[
            '.source/web/src/Status.tsx',
            '.source/backend/Sample.Api/Controllers/LoginController.cs',
            '.source/backend/Sample.Business/Services/MemberService.cs',
        ]
        for p in self.paths:
            t=self.root/p
            t.parent.mkdir(parents=True,exist_ok=True)
            t.write_text('NEVER_SEND_SOURCE_BYTES_TO_CONTEXT_PACK\n')
        self.git('init','-q')
        self.git('config','user.email','dev@example.local')
        self.git('config','user.name','Test')
        self.git('add','.')
        self.git('commit','-qm','chore: baseline')
        head=self.git('rev-parse','HEAD')
        self.write_json('.agents/state/session.json',{'id':'S2C-TEST','status':'ACTIVE', 'last_seen_head':head,'outside_paths':[], 'repository_binding': guard.capture_scope(self.root)})
        self.write_json('.agents/state/infrastructure.json',{'git':{'head':head[:12]},'files':{p:{'sha256':'test'} for p in self.paths}})
        self.write_json('.agents/state/system-graph.json', {'nodes':[{'id':i} for i in ['presentation','api','application','security','quality']],
           'edges':[{'from':'presentation','to':'api'},{'from':'api','to':'application'},{'from':'api','to':'security'}, {'from':'quality','to':'api'}]})
        self.write_json('.agents/state/symbol-cache.json', {self.paths[0]:{'functions':[{'name':'Status','line':1}]}, self.paths[1]:{'functions':[{'name':'Login','line':1}]},self.paths[2]:{'functions':[{'name':'GetMember','line':1}]}})
        self.write_json('.agents/state/architecture-docs.json',{'functions':{f'{self.paths[0]}#Status:1':{'document':'s2c/Present/Status/.Status.Status.md'}}})
        for p in ['s2c/.summerize.md','s2c/Present/.summerize.md','s2c/Present/Status/.Status.Status.md','s2c/Present/Status/.summerize.md','s2c/API/.summerize.md','s2c/Application/.summerize.md','s2c/Security/.summerize.md']:
            t=self.root/p
            t.parent.mkdir(parents=True,exist_ok=True)
            t.write_text('short layer index\n')

    def tearDown(self):
        self.tmp.cleanup()

    def git(self,*args):
        r=subprocess.run(['git',*args],cwd=self.root,text=True,capture_output=True,timeout=8)
        self.assertEqual(r.returncode,0,r.stderr)
        return r.stdout.strip()

    def write_json(self,p,obj):
        dest=self.root/p
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(json.dumps(obj))

    def test_auto_minimal_and_preserve_existing_layout(self):
        pack=router.route(self.root,'TASK-1','Change Status page label',[self.paths[0]],'Status','auto',0)
        self.assertEqual(pack['effective_mode'],'minimal')
        self.assertIn('s2c/Present/.summerize.md',pack['layer_summary_paths'])
        self.assertIn('s2c/Present/Status/.Status.Status.md',pack['function_document_paths'])
        self.assertNotIn('NEVER_SEND_SOURCE_BYTES_TO_CONTEXT_PACK',(self.root/router.PACK).read_text())
        self.assertFalse((self.root/'.agents/.handoffs').exists())

    def test_cache_doc_in_root_layer_blocked(self):
        state = json.loads((self.root / '.agents/state/architecture-docs.json').read_text())
        first = next(iter(state['functions'].values()))
        first['document'] = 'Present/Status/.Status.Status.md'
        self.write_json('.agents/state/architecture-docs.json', state)
        with self.assertRaisesRegex(RuntimeError, 'ARCH_DOC_SCOPE_BLOCKED'):
            router.route(self.root, 'TASK-STALE', 'Review old document', [self.paths[0]], '', 'balanced', 0)

    def test_high_risk_requires_deep_even_manual_minimal(self):
        pack=router.route(self.root,'TASK-2','Change login authentication',[self.paths[1]],'Login','minimal',0)
        self.assertEqual(pack['effective_mode'],'deep')
        self.assertIn('manual downgrade blocked', ' '.join(pack['reasons']))

    def test_balanced_multiple_paths(self):
        pack=router.route(self.root,'TASK-3','Update endpoint response',[self.paths[0],self.paths[2]],'','auto',0)
        self.assertEqual(pack['effective_mode'],'balanced')
        self.assertEqual(len(pack['source_paths']),2)

    def test_external_drift_deep(self):
        state=json.loads((self.root/router.SESSION).read_text())
        state['outside_paths']=[self.paths[0]]
        self.write_json(str(router.SESSION),state)
        pack=router.route(self.root,'TASK-4','Change display label',[self.paths[0]],'','auto',0)
        self.assertEqual(pack['effective_mode'],'deep')

    def test_stale_uncommitted_source_change_is_blocked(self):
        snap=json.loads((self.root/router.infra.MANIFEST).read_text())
        stat=(self.root/self.paths[0]).stat()
        snap['files'][self.paths[0]]['size']=stat.st_size
        snap['files'][self.paths[0]]['mtime_ns']=stat.st_mtime_ns
        self.write_json(str(router.infra.MANIFEST),snap)
        (self.root/self.paths[0]).write_text('changed uncommitted source!')
        with self.assertRaisesRegex(RuntimeError,'STALE_SOURCE_METADATA'):
            router.route(self.root,'TASK-X','Update Status label',[self.paths[0]],'','auto',0)

    def test_stale_git_head_is_blocked(self):
        (self.root/'README.md').write_text('new commit')
        self.git('add','README.md')
        self.git('commit','-qm','docs: drift')
        with self.assertRaisesRegex(RuntimeError,'STALE_GIT_HEAD'):
            router.route(self.root,'TASK-5','Change Status label',[self.paths[0]],'','auto',0)

    def test_ambiguous_route_needs_explicit_paths(self):
        pack=router.route(self.root,'TASK-6','Unspecified work item',[],'','auto',0)
        self.assertEqual(pack['routing_status'],'NEEDS_EXPLICIT_PATH')
        self.assertEqual(pack['source_paths'],[])

    def test_policy_override_is_per_checkout(self):
        self.write_json('.agents/state/context-policy.json',{
            'schema_version':1,'default_mode':'minimal',
            'budgets':{'minimal':350,'balanced':900,'deep':2800}})
        pack=router.route(self.root,'TASK-8','Review a bounded task',[self.paths[0]],'','auto',0)
        self.assertEqual(pack['effective_mode'],'minimal')
        self.assertEqual(pack['token_budget_target'],350)

    def test_sensitive_metadata_never_becomes_read_target(self):
        target='.source/backend/Sample.Api/appsettings.json'
        t=self.root/target
        t.parent.mkdir(parents=True,exist_ok=True)
        t.write_text('{"ConnectionStrings":{"Secret":"NEVER_READ_ME"}}')
        manifest=json.loads((self.root/router.infra.MANIFEST).read_text())
        manifest['files'][target]={'size':t.stat().st_size,'mtime_ns':t.stat().st_mtime_ns,'digest_status':'metadata_only'}
        self.write_json(str(router.infra.MANIFEST),manifest)
        pack=router.route(self.root,'TASK-9','Review config',[target],'','minimal',0)
        self.assertEqual(pack['effective_mode'],'deep')
        self.assertEqual(pack['routing_status'],'METADATA_ONLY')
        self.assertEqual(pack['source_paths'],[])
        self.assertIn(target,pack['metadata_only_paths'])
        self.assertNotIn('NEVER_READ_ME',(self.root/router.PACK).read_text())

    def test_path_traversal_is_rejected(self):
        with self.assertRaisesRegex(RuntimeError,'Unsafe path'):
            router.route(self.root,'TASK-7','Update status',['../secrets.txt'],'','auto',0)


if __name__=='__main__':
    unittest.main()
