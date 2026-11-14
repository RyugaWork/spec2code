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


    def _advance_to(self, destination, *, scope):
        steps = ("SPECIFY_PLAN", "IMPLEMENT", "VERIFY", "HANDOFF_REVIEW")
        for phase in steps[:steps.index(destination) + 1]:
            workflow_guard.transition(
                self.request(phase, "advance", **scope),
                trusted_gate_check=lambda gate, req: True)

    def test_scoped_close_keeps_task_and_requires_trusted_review(self):
        scope = {"task": "Update utility", "paths": ("src/main.py",)}
        self.start()
        workflow_guard.transition(self.request(action="begin", **scope))
        self._advance_to("HANDOFF_REVIEW", scope=scope)
        with self.assertRaisesRegex(RuntimeError, "WF_TASK_SCOPE_MISMATCH"):
            workflow_guard.transition(self.request("HANDOFF_REVIEW", "close"))
        outcome = workflow_guard.transition(
            self.request("HANDOFF_REVIEW", "close", **scope),
            trusted_gate_check=lambda gate, req: True)
        self.assertEqual(outcome["phase_status"], "COMPLETE")
        self.assertFalse(outcome["release_authorized"])

    def test_verify_policy_cannot_be_approver_overridden(self):
        policy_path = self.root / ".agents/policy-map.json"
        mapping = json.loads(policy_path.read_text(encoding="utf-8"))
        mapping["documents"].append({
            "category": "governance", "path": "missing-verify.md",
            "canonical": False, "required_for": ["verify"],
            "applies_to_prefixes": ["src/"], "reason": "verify obligation"
        })
        policy_path.write_text(json.dumps(mapping), encoding="utf-8")
        scope = {"task": "Update utility", "paths": ("src/main.py",)}
        self.start()
        workflow_guard.transition(self.request(action="begin", **scope))
        self._advance_to("VERIFY", scope=scope)
        decision = workflow_guard.evaluate(
            self.request("VERIFY", "evaluate", **scope))
        self.assertEqual(decision["policy_status"], "BLOCKED")
        self.assertIn("GT-002", decision["blocking_gates"])
        with self.assertRaisesRegex(RuntimeError, "WF_EXIT_GATE_BLOCKED"):
            workflow_guard.transition(
                self.request("HANDOFF_REVIEW", "advance", **scope),
                trusted_gate_check=lambda gate, req: True)

    def test_handoff_policy_refuses_scoped_close(self):
        policy_path = self.root / ".agents/policy-map.json"
        mapping = json.loads(policy_path.read_text(encoding="utf-8"))
        mapping["documents"].append({
            "category": "governance", "path": "missing-handoff.md",
            "canonical": False, "required_for": ["handoff"],
            "applies_to_prefixes": ["src/"], "reason": "handoff obligation"
        })
        policy_path.write_text(json.dumps(mapping), encoding="utf-8")
        scope = {"task": "Update utility", "paths": ("src/main.py",)}
        self.start()
        workflow_guard.transition(self.request(action="begin", **scope))
        self._advance_to("HANDOFF_REVIEW", scope=scope)
        decision = workflow_guard.evaluate(
            self.request("HANDOFF_REVIEW", "evaluate", **scope))
        self.assertIn("GT-002", decision["blocking_gates"])
        with self.assertRaisesRegex(RuntimeError, "WF_EXIT_GATE_BLOCKED"):
            workflow_guard.transition(
                self.request("HANDOFF_REVIEW", "close", **scope),
                trusted_gate_check=lambda gate, req: True)

    def test_scoped_source_file_drift_blocks_freshness(self):
        scope = {"task": "Update utility", "paths": ("src/main.py",)}
        self.start()
        workflow_guard.transition(self.request(action="begin", **scope))
        (self.root / "src/main.py").write_text("a = 200\n", encoding="utf-8")
        decision = workflow_guard.evaluate(
            self.request("DISCOVER", "evaluate", **scope))
        self.assertIn("GT-014", decision["blocking_gates"])

    def test_spec_kit_active_tasks_drift_blocks_freshness(self):
        directory = self.root / "specs/001-test"
        directory.mkdir(parents=True)
        pointer = self.root / ".specify/feature.json"
        pointer.parent.mkdir(parents=True)
        pointer.write_text(json.dumps({"feature_directory": "specs/001-test"}),
                           encoding="utf-8")
        for name in ("spec.md", "plan.md", "tasks.md"):
            (directory / name).write_text(f"# {name}\n", encoding="utf-8")
        scope = {"task": "Update utility", "paths": ("src/main.py",)}
        self.start()
        workflow_guard.transition(self.request(action="begin", **scope))
        (directory / "tasks.md").write_text("# changed task\n", encoding="utf-8")
        decision = workflow_guard.evaluate(
            self.request("DISCOVER", "evaluate", **scope))
        self.assertIn("GT-014", decision["blocking_gates"])

    def test_unscoped_status_reports_freshness_unknown_not_mismatch(self):
        scope = {"task": "Update utility", "paths": ("src/main.py",)}
        self.start()
        workflow_guard.transition(self.request(action="begin", **scope))
        decision = workflow_guard.evaluate(self.request("DISCOVER", "status"))
        self.assertNotIn("WF_TASK_SCOPE_MISMATCH", decision["blocking_gates"])
        self.assertIn("WF_SCOPE_REQUIRED_FOR_FRESHNESS",
                      decision["review_gates"])
        self.assertEqual(decision["gate_status"], "NEEDS_REVIEW")

    def test_directory_scope_cannot_claim_recursive_freshness(self):
        self.start()
        scope = {"task": "Update utility", "paths": ("src",)}
        with self.assertRaisesRegex(RuntimeError, "WF_UNBOUNDED_SOURCE_DIRECTORY"):
            workflow_guard.transition(self.request(action="begin", **scope))


if __name__ == "__main__":
    unittest.main()
