"""PLAN-080 policy discovery/security regression on disposable Git checkouts."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
import governance_schema
import policy_resolver


class PolicyResolverTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="s2c-policy-")
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        for cmd in (("init", "-q"), ("config", "user.name", "Tester"),
                    ("config", "user.email", "test@example.invalid")):
            p = subprocess.run(["git", *cmd], cwd=self.root, capture_output=True, text=True)
            self.assertEqual(p.returncode, 0, p.stderr)
        (self.root / "src").mkdir()
        (self.root / "src" / "feature.py").write_text("value = 1\n", encoding="utf-8")
        (self.root / "AGENTS.md").write_text("# Host rules\n", encoding="utf-8")
        p = subprocess.run(["git", "add", "."], cwd=self.root, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        p = subprocess.run(["git", "commit", "-qm", "chore: init"], cwd=self.root,
                           capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)

    def tearDown(self):
        self.temp.cleanup()

    def resolve(self, task="Fix authentication", operation="implement", paths=()):
        return policy_resolver.resolve(policy_resolver.PolicyRequest(
            self.root, "T001", task, tuple(paths), operation))

    def host_map(self, docs):
        dest = self.root / ".agents" / "policy-map.json"
        dest.parent.mkdir(exist_ok=True)
        dest.write_text(json.dumps({"schema_version": 1, "documents": docs}), encoding="utf-8")

    @staticmethod
    def doc(path, category="security", required=("implement",), canonical=True):
        return {"category": category, "path": path, "canonical": canonical,
                "required_for": list(required), "applies_to_prefixes": [],
                "reason": "canonical policy"}

    def test_generic_repo_without_policy_map_is_supported(self):
        actual = self.resolve("Update a simple utility", "read")
        self.assertEqual(actual["policy_status"], "READY")
        self.assertEqual(actual["root_agents"][0]["path"], "AGENTS.md")
        self.assertFalse((self.root / ".agents").exists())

    def test_required_policy_found(self):
        (self.root / "security.md").write_text("# Security\n", encoding="utf-8")
        self.host_map([self.doc("security.md")])
        actual = self.resolve()
        self.assertEqual(actual["policy_status"], "READY")
        self.assertEqual(actual["selected_documents"][0]["path"], "security.md")

    def test_missing_required_blocks_implementation(self):
        self.host_map([self.doc("missing.md")])
        actual = self.resolve()
        self.assertEqual(actual["policy_status"], "BLOCKED")
        self.assertIn("POLICY_REQUIRED_MISSING:missing.md", actual["blocking_reasons"])

    def test_missing_required_in_read_requires_review(self):
        self.host_map([self.doc("missing.md", required=("read",))])
        self.assertEqual(self.resolve(operation="read")["policy_status"], "NEEDS_REVIEW")

    def test_duplicate_canonical_blocks(self):
        for f in ("one.md", "two.md"):
            (self.root / f).write_text("# Rules\n", encoding="utf-8")
        self.host_map([self.doc("one.md"), self.doc("two.md")])
        self.assertEqual(self.resolve()["policy_status"], "BLOCKED")

    def test_host_cannot_assert_approval(self):
        value = self.doc("security.md")
        value["approved"] = True
        self.host_map([value])
        with self.assertRaisesRegex(ValueError, "POLICY_MAP_MALFORMED"):
            self.resolve()

    def test_traversal_in_policy_map_rejected(self):
        self.host_map([self.doc("../outside.md")])
        with self.assertRaisesRegex(ValueError, "POLICY_MAP_MALFORMED"):
            self.resolve()

    def test_selected_path_traversal_rejected(self):
        with self.assertRaises(ValueError):
            self.resolve(paths=("../outside.py",))

    def test_nested_agents_selected(self):
        (self.root / "src" / "AGENTS.md").write_text("# Scoped rules\n", encoding="utf-8")
        actual = self.resolve("Update a simple utility", "read", ("src/feature.py",))
        self.assertEqual([x["path"] for x in actual["root_agents"]],
                         ["AGENTS.md", "src/AGENTS.md"])

    def test_no_output_written_by_resolver(self):
        self.resolve()
        self.assertFalse((self.root / ".agents" / "state").exists())

    def test_strict_governance_config_rejects_extra_fields(self):
        cfg = json.loads((SCRIPTS.parent / ".config" / "governance.json").read_text())
        governance_schema.validate_config("governance", cfg)
        cfg["allow_write"] = True
        with self.assertRaises(RuntimeError):
            governance_schema.validate_config("governance", cfg)

    def test_workflow_protocol_cannot_be_reordered(self):
        cfg = json.loads((SCRIPTS.parent / ".config" / "workflow.json").read_text())
        governance_schema.validate_config("workflow", cfg)
        cfg["phases"] = ["IMPLEMENT"]
        with self.assertRaises(RuntimeError):
            governance_schema.validate_config("workflow", cfg)


if __name__ == "__main__":
    unittest.main()
