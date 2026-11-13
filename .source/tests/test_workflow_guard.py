"""PLAN-080 non-autonomous workflow gate and journal tests."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import session_guard
import workflow_guard


class WorkflowGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="s2c-workflow-")
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        for cmd in (("init", "-q"), ("config", "user.name", "Tester"),
                    ("config", "user.email", "test@example.invalid")):
            completed = subprocess.run(["git", *cmd], cwd=self.root,
                                       capture_output=True, text=True)
            self.assertEqual(completed.returncode, 0, completed.stderr)
        (self.root / "AGENTS.md").write_text("# Host rules\n", encoding="utf-8")
        (self.root / "src").mkdir()
        (self.root / "src" / "main.py").write_text("a = 1\n", encoding="utf-8")
        (self.root / ".agents").mkdir()
        (self.root / ".agents" / "policy-map.json").write_text(json.dumps({
            "schema_version": 1, "documents": [{
                "category": "governance", "path": "AGENTS.md",
                "canonical": True, "required_for": ["read", "plan", "implement"],
                "applies_to_prefixes": [], "reason": "host policy"
            }]}), encoding="utf-8")
        for cmd in (("add", "."), ("commit", "-qm", "chore: init")):
            result = subprocess.run(["git", *cmd], cwd=self.root,
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)

    def tearDown(self):
        self.temp.cleanup()

    def request(self, phase="DISCOVER", action="status", task="", paths=()):
        return workflow_guard.WorkflowRequest(
            self.root, "T001", phase, action, task=task, paths=tuple(paths))

    def start(self):
        self.assertEqual(session_guard.run_start(self.root), 0)

    def test_status_is_read_only_without_session(self):
        out = workflow_guard.evaluate(self.request())
        self.assertEqual(out["phase_status"], "UNINITIALIZED")
        self.assertFalse((self.root / ".agents" / "state" / "workflow-state.json").exists())

    def test_begin_writes_managed_state(self):
        self.start()
        out = workflow_guard.transition(self.request(action="begin"))
        self.assertEqual(out["current_phase"], "DISCOVER")
        state = self.root / ".agents" / "state" / "workflow-state.json"
        self.assertEqual(json.loads(state.read_text())["approval_state"], "UNKNOWN")
        self.assertFalse(json.loads(state.read_text())["release_authorized"])

    def test_forward_transition_requires_trusted_review(self):
        self.start()
        workflow_guard.transition(self.request(action="begin"))
        workflow_guard.transition(self.request("SPECIFY_PLAN", "advance"))
        with self.assertRaisesRegex(RuntimeError, "WF_APPROVAL_REQUIRED"):
            workflow_guard.transition(self.request("IMPLEMENT", "advance"))

    def test_illegal_skip_blocked(self):
        self.start()
        workflow_guard.transition(self.request(action="begin"))
        with self.assertRaisesRegex(RuntimeError, "WF_ILLEGAL_TRANSITION"):
            workflow_guard.transition(self.request("VERIFY", "advance"))

    def test_cannot_begin_twice(self):
        self.start()
        workflow_guard.transition(self.request(action="begin"))
        with self.assertRaisesRegex(RuntimeError, "WF_ALREADY_STARTED"):
            workflow_guard.transition(self.request(action="begin"))

    def test_corrupted_journal_rejected(self):
        self.start()
        workflow_guard.transition(self.request(action="begin"))
        path = self.root / ".agents" / "state" / "workflow-events.jsonl"
        path.write_text(path.read_text().replace("DISCOVER", "IMPLEMENT"), encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "EVENT_LOG_CORRUPT"):
            workflow_guard.evaluate(self.request())

    def test_invalidate_and_explicit_resume(self):
        self.start()
        workflow_guard.transition(self.request(action="begin"))
        workflow_guard.transition(self.request("DISCOVER", "invalidate"))
        resumed = workflow_guard.transition(self.request("DISCOVER", "advance"))
        self.assertEqual(resumed["phase_status"], "IN_PROGRESS")

    def test_source_change_blocks_gates(self):
        self.start()
        workflow_guard.transition(self.request(action="begin"))
        (self.root / "AGENTS.md").write_text("# Modified host rules\n", encoding="utf-8")
        result = workflow_guard.evaluate(self.request())
        self.assertEqual(result["gate_status"], "BLOCKED")
        self.assertIn("GT-014", result["blocking_gates"])

    def test_missing_scoped_security_policy_blocks_gate(self):
        self.start()
        policy_map = self.root / ".agents" / "policy-map.json"
        policy = json.loads(policy_map.read_text(encoding="utf-8"))
        policy["documents"].append({
            "category": "security", "path": "missing-security.md",
            "canonical": True, "required_for": ["implement"],
            "applies_to_prefixes": ["src/"], "reason": "Security policy required"
        })
        policy_map.write_text(json.dumps(policy), encoding="utf-8")
        scope = {"task": "Fix authentication", "paths": ("src/main.py",)}
        workflow_guard.transition(self.request(action="begin", **scope))
        decision = workflow_guard.evaluate(self.request("IMPLEMENT", "evaluate", **scope))
        self.assertEqual(decision["gate_status"], "BLOCKED")
        self.assertIn("GT-002", decision["blocking_gates"])

    def test_nested_agents_change_invalidates_workflow(self):
        nested = self.root / "src" / "AGENTS.md"
        nested.write_text("# Before\\n", encoding="utf-8")
        self.start()
        scope = {"task": "Update utility", "paths": ("src/main.py",)}
        workflow_guard.transition(self.request(action="begin", **scope))
        nested.write_text("# After\\n", encoding="utf-8")
        decision = workflow_guard.evaluate(self.request("DISCOVER", "evaluate", **scope))
        self.assertEqual(decision["gate_status"], "BLOCKED")
        self.assertIn("GT-014", decision["blocking_gates"])

    def test_task_scope_change_cannot_reuse_workflow_approval(self):
        self.start()
        scope = {"task": "Update utility", "paths": ("src/main.py",)}
        workflow_guard.transition(self.request(action="begin", **scope))
        decision = workflow_guard.evaluate(self.request(
            "DISCOVER", "evaluate", task="Change authentication", paths=("src/main.py",)))
        self.assertEqual(decision["gate_status"], "BLOCKED")
        self.assertIn("WF_TASK_SCOPE_MISMATCH", decision["blocking_gates"])

    def test_invalidate_unrelated_phase_is_rejected(self):
        self.start()
        workflow_guard.transition(self.request(action="begin"))
        with self.assertRaisesRegex(RuntimeError, "WF_ILLEGAL_TRANSITION"):
            workflow_guard.transition(self.request("VERIFY", "invalidate"))

    def test_missing_task_description_blocks_implementation(self):
        self.start()
        workflow_guard.transition(self.request(action="begin"))
        decision = workflow_guard.evaluate(self.request("IMPLEMENT", "evaluate"))
        self.assertEqual(decision["gate_status"], "BLOCKED")
        self.assertIn("WF_TASK_SCOPE_REQUIRED", decision["blocking_gates"])


if __name__ == "__main__":
    unittest.main()
