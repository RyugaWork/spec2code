# PLAN-093 — SK-03 Native Spec Kit CLI pilot handoff

> Recorded 2026-11-13 Asia/Ho_Chi_Minh. **Source branch**: `docs/plan-089-a1-readiness`, existing Draft PR #10; **base**: `docs/plan-088-unified-s2c`. No additional branch, merge, CI pipeline or host deployment.
>
> **Git HEAD before creating this handoff:** `ca84088dd002b3153040b9db14904a94817014a7` (creating this document advances HEAD; refresh before signing). Google stakeholder BRD Draft v1.5 Section 26, revision `AHj4eMSdTU9jmxfg2_Itr8rHT1ZzmKRGQZ4EBJ57qgiVjtaSS9eomF-B0Aqd2RPp1ETwIbEXEAsRA2VOB92ZAXPv8DD5i2bdwvECw31trQ`.
>
> **Aggregate gate:** `SK3_PILOT_PREPARED_BUT_NATIVE_BLOCKED`. A.1 `NOT_RUN`, B `NOT_AUTHORIZED`, B.1 `NOT_RUN`. No owner-approved CLI version, no official initialized native agent environment and no new production code.

## 1. Durable work actually performed

- Confirmed the official `github/spec-kit` upstream previous-minor release `v1.2.6` published 2026-11-02, requirements `Python>=3.11` and CLI init/Codex integration options from exact upstream source. Compared latest `v1.4.0` dated 2026-11-10; later upstream security hardening must be considered before any non-disposable approval. `v1.2.6` is a **candidate for disposable trial only**, not a product release default.
- Attempted local network access and offline invocation in a container with Python 3.13.5, Git 2.47.3 and uv. `git ls-remote` failed DNS; `uvx --offline --from git+https://github.com/github/spec-kit.git@v1.2.6 specify version` failed **exit 1** due Git dependency resolution. The official `specify` binary is absent, so `specify init` and upstream prerequisite scripts **were NOT executed**.
- Created [SK-03 native pilot guide](../.documents/specKitNativePilot.md) with Linux/Codespaces and Windows PowerShell procedure, detached worktree, asset/owner hashes, force-overwrite collision inventory, pinned version checks and eight real acceptance gates `SK3-01..08`.
- Ran **one actual synthetic Git-worktree smoke test** in a temporary Linux directory with six representative S2C-shaped files: created detached worktree, all original SHA-256 file hashes preserved, both worktrees clean, branch count remained one. The synthetic fixture was disposed. This is **not a native Spec Kit/S2C host test**.
- Updated [feature tasks](../../specs/001-s2c-speckit-integration/tasks.md), [PLAN ledger](../.plans.md), [RTM](../.traceMatrix.md), [risk matrix](../.riskMatrix.md), [.specify adoption guide](../../.specify/README.md) and [.source integration guide](../../.source/integrations/speckit/README.md). Google BRD amended with section 26. All source-code, JSON, CI, native script/skill and host paths remain unchanged.

## 2. Acceptance matrix and truthful task statuses

| Artifact/check | Status | Evidence/owner gap |
| --- | --- | --- |
| Version provenance and source/interface research | DONE_AS_RESEARCH | Official v1.2.6/v1.4.0 metadata + init/Codex source; **no owner-accepted release** |
| T006 — official CLI version/host choice | PENDING_APPROVAL | Candidate release identified, security delta and user host environment unknown |
| T007 — native init in disposable S2C worktree | BLOCKED_NOT_RUN | Network/runner missing, authorization + real checkout environment required |
| T008 — native skills/scripts and CLI tests | NOT_RUN | Official runtime unavailable; no `specify version` |
| T009 — generated asset diff reconciliation | NOT_RUN | No generated files to review |
| SK3-01..08 — **real S2C native acceptance** | NOT_RUN / SK3-02 BLOCKED | No real S2C trial or official CLI output |
| Synthetic mini-repo worktree smoke | PASS_ON_SYNTHETIC_FIXTURE_ONLY | Six SHA-256 files preserved, no branch proliferation; not acceptance of S2C/Spec Kit |
| A.1 / B implementation / B.1 / release | NOT_RUN / NOT_AUTHORIZED | Named owners, P0 risk disposition and independent validation still missing |

## 3. Risks, next permissible step, recovery

**Selected risks:** candidate `SK-R01` (force overwrite); `SK-R04` (version support and newly added upstream hardening); RM-001/002/003/004/005 remain open P0; no measured residual reduction. No auto-adoption of old source for production. Independent A.1 and separately scoped B authorization remain mandatory before S2C runtime changes.

**Next actionable step:** in an owner-authorized network-enabled Codex/Codespaces/local checkout, fetch exact latest S2C SHA and Google revision, accept a reviewed Spec Kit version, create a disposable detached worktree, run the official pinned CLI only there, compare original owner hashes/complete generated file inventory, execute the upstream prerequisite script and preserve its real stdout/stderr, OS, SHA, exit code and diff. Any changed source/policy or file collision is a STOP requiring review. Do not automatically merge generated files or enable Spec Kit's optional git extension.

**Rollback:** only these PLAN-093 docs may be reverted from the existing branch if rejected; retain the prior PLAN-090/091/092 handoffs. Google Doc changes have separate revision history. The failed offline attempt made no user checkout modification and no Spec Kit installation. Synthetic fixture was deleted by its temporary-directory context after the test, not by deleting unowned host files.
