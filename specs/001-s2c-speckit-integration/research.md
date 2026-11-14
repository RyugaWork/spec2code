# Research and Alternatives — S2C / Spec Kit integration

> **DESIGN_EVIDENCE / 2026-11-13.** Research is based on inspected public upstream GitHub source/release metadata and S2C development repository at PR #10. It is not a successfully executed installation, an independent security audit, a human A.1 signature or a support certification.

## Decision R-01 — Feature development without shadow BRD

- **Option A (selected for document bootstrap):** Official Spec Kit `.specify/feature.json` and feature-local `spec.md`/`plan.md`/`tasks.md`; S2C master `.agents/.spec.md`, RTM, risk and AGENTS retain cross-project authority. ChatGPT Web uses authenticated GitHub for Markdown edits, native coding agents use official installed skills in a real host.
- **Option B (rejected):** Replicate the entire master BRD/SRS inside each Spec Kit feature; creates two sources of truth and stale approval.
- **Option C (deferred):** Require an MCP server/CI/daemon as entry point; contradicts current S2C Markdown-first design and adds operational trust boundaries without measured need.

## Decision R-02 — CLI version and host selection

| Alternative | Publication evidence | Security/maturity trade-off | Adoption decision |
| --- | --- | --- | --- |
| `v1.2.6` | [Official release 2026-11-02](https://github.com/github/spec-kit/releases/tag/v1.2.6), [Python>=3.11](https://github.com/github/spec-kit/blob/v1.2.6/pyproject.toml) | Earlier stable version; excludes newer FileHelper and URL-hardening changes. Earlier publication alone does not prove more secure or safer. | **DISPOSABLE-PILOT CANDIDATE ONLY**, not accepted for routine host adoption |
| `v1.4.0` | [Official release 2026-11-10](https://github.com/github/spec-kit/releases/tag/v1.4.0) | Latest at research date; may incorporate important security fixes, but newly released and requires compatibility evidence | REQUIRES_OWNER_REVIEW, not auto-installed |
| No native CLI | GitHub Markdown workflows and current read-only `speckit_bridge.py` | Cannot execute official skills/commands; no dependency on installer/network | **ACTIVE WEB MODE** pending authorized native pilot |

**Source-verified interfaces:** [v1.2.6 command_init.py](https://github.com/github/spec-kit/blob/v1.2.6/src/specify_cli/command_init.py) supports `--here`, `--force`, `--non-interactive`, `--integration codex`, `--script py`. Existing `.specify/memory/constitution.md` is intentionally preserved in its specific materialization branch; this is not a general guarantee that init leaves all existing files untouched. [Existing project guidance](https://github.com/github/spec-kit/blob/v1.2.6/docs/guides/existing-projects.md) calls for a reviewable baseline, backups and diff inspection.

**Observed blocker:** terminal has Python 3.13.5 / Git 2.47.3 / uv; `specify` absent and DNS unavailable for GitHub/PyPI. A `uvx --offline` version attempt exited 1 because Git source could not be resolved. No native init or official scripts executed. [Pilot runbook](../../.agents/.documents/specKitNativePilot.md) is documented but not a test report.

## Decision R-03 — Active feature and worktree ownership

Official selection is the contained `.specify/feature.json` (`specs/001-s2c-speckit-integration`), not a Git branch. S2C's bridge may accept `SPECIFY_FEATURE_DIRECTORY` only when it remains inside an authorized checkout; upstream may allow broader usage, which S2C deliberately does not inherit. Do **not** install optional Git extension or create feature branches by default. For native trials use a detached temporary Git worktree and compare tracked **and untracked** changes before importing anything.

## Decision R-04 — Conflict and drift management

Existing S2C-managed paths (`AGENTS.md`, `.agents/.spec.md`, RTM, feature pointer, Constitution, source files and user-owned skill folders) are **protected from silent init overwrite**. Any official installer/generated output affecting them requires original hashes, exact diff, owner approval and rollback. Treat source SHA + Google Doc revision + Constitution/policy/config fingerprints as separate identities. STOP and re-review if any relevant identity changes.

## Decision R-05 — Test and risk acceptance

Feature-local [test design](checklists/integrationAcceptance.md) contains exact `SKI-TC-001-P/N .. SKI-TC-012-P/N`, but all execution remains NOT_RUN. High-risk negative scenarios include traversal/junction, source drift, forged reviewer approval, CLI-generated collision, incomplete artifacts and unapproved host writes. Existing RM-001..005 exposures remain OPEN; document design cannot reduce verified residual risk.

## Open decisions and uncertainties

- Version/OS/agent identity and security release comparison acceptance: `DEC-SK3-01/02` UNKNOWN.
- Native init collision/backup permission and generated-path allowlist: `DEC-SK3-03/04` UNKNOWN.
- Business owner, Constitution ratification and independent A.1/B/B.1 signoff: `DEC-SK3-05` and `DEC-091-01/09/10` UNKNOWN.
- Actual CI and host data are not implicitly authorized; optional Spec Kit workflows are not guaranteed to be available on ChatGPT Web.

**References:** [Spec Kit project](https://github.com/github/spec-kit), [upstream tasks template at v1.2.6](https://github.com/github/spec-kit/blob/v1.2.6/templates/tasks-template.md), [existing-project guide](https://github.com/github/spec-kit/blob/v1.2.6/docs/guides/existing-projects.md), [S2C current source](../../.source/integrations/speckit/README.md).

## PLAN-108 / K04 — Repeatable upstream research decision

When selecting an official Spec Kit release, preserve the exact upstream tag/commit, release date and publication URL, source files inspected (especially feature selection and pointer persistence), supported host/runtime, last security/compatibility check, and a reason for rejecting alternative versions. Previously observed v1.2.6 or v1.4.0 source behavior is **historical evidence**, not proof of a newer installed runtime or a blanket security guarantee.

Record `SOURCE_INSPECTED`, `CLI_INSTALLED`, `HOST_TESTED` and `APPROVED_FOR_B` separately. For uncertain fields (native tool availability, provider authorization, Windows junction behavior), set UNKNOWN and add a bounded negative fixture, not a guessed default. Cite maintainer documentation when a future pilot actually refreshes versions; no external installation is implied by this research update.
