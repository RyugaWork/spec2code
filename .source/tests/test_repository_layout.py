"""Protect the development-repository layout and the portable runtime bundle."""
from pathlib import Path
import sys
import unittest

REPO = Path(__file__).resolve().parents[2]
SOURCE = REPO / ".source"
sys.path.insert(0, str(SOURCE / "scripts"))
import config_loader


class RepositoryLayoutTests(unittest.TestCase):
    def test_governance_and_source_ownership(self):
        self.assertTrue((REPO / "AGENTS.md").is_file())
        for item in (".spec.md", ".features.md", ".plans.md", ".risk.md",
                     ".checklist.md", ".structure.md", ".changelog.md"):
            self.assertTrue((REPO / ".agents" / item).is_file(), item)
        for item in ("SKILL.md", "scripts/config_loader.py", "scripts/session_guard.py",
                     "tests/test_path_guard.py", "references/spec-to-code-workflow.md",
                     "integrations/speckit/README.md", ".config/security.json"):
            self.assertTrue((SOURCE / item).is_file(), item)

    def test_runtime_config_comes_from_source_bundle_only(self):
        self.assertEqual(config_loader.load("security")["schema_version"], 1)
        self.assertTrue((SOURCE / ".config" / "security.json").is_file())
        self.assertFalse((REPO / ".config").exists())

    def test_no_obsolete_top_level_skill_directories(self):
        for item in ("scripts", "tests", "references", "integrations", "SKILL.md",
                     ".handoff.md", ".plan.md", ".riskdetail.md", "CHANGELOG.md"):
            self.assertFalse((REPO / item).exists(), item)


if __name__ == "__main__":
    unittest.main()
