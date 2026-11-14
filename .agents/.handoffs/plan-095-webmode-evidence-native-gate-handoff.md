# PLAN-095 — Spec Kit Web-mode executed evidence and native no-bypass handoff

> **Recorded:** 2026-11-13, Asia/Ho_Chi_Minh. **Existing working branch:** `docs/plan-089-a1-readiness` / Draft PR #10, base `docs/plan-088-unified-s2c`; **no new branch or merge**. Git HEAD immediately before this handoff commit: `02e82b63876c1377748a862c03ce15c00a4538c0`; this handoff itself advances HEAD, so re-fetch current branch SHA before signing any review.
>
> **Google BRD:** Draft v1.5, PLAN-095 Section 28. Batch write returned revision `AHj4eMRdBbsah2dqQ9oIH4Ba7xSJDV1eR_OcDLgnBQssHySDKbFkLtvUFXJN1LpfGl5Ulut2e77tMJ3Jvuw25RSVVyODEEy1FmLKtzh4lw`; a subsequent readback was **429 RATE_LIMITED**, so written revision is acknowledged but independent readback/rendering not verified.
>
> **Aggregate status:** `WEB_MARKDOWN_OPERATION_TESTED` for four scoped positive cases; `NATIVE_SPECKIT_NOT_INSTALLED/NOT_RUN`; `A1_NOT_RUN`; `B_NOT_AUTHORIZED`; `B1_NOT_RUN`; `RM-001..005 OPEN`. No user-authorized CI, host install, source-code mutation, merge or release.

## 1. Concrete work performed

- Compared exact upstream Spec Kit v1.2.6 [implement skill](https://github.com/github/spec-kit/blob/v1.2.6/templates/commands/implement.md) and [task template](https://github.com/github/spec-kit/blob/v1.2.6/templates/tasks-template.md) with S2C's feature workflow. **Observed risk:** native `implement` asks whether to continue if requirements checklists are incomplete; a “yes” does not meet independent S2C A.1 or separate B permission, and current tasks include owner approvals.
- Created [native execution safety gate](../.workflow/specKitNativeExecutionGate.md) as a **procedural Markdown-only design** (8 proposed SK95-GATE-01..08 cases, all NOT_RUN) and [Web/GitHub operating workflow](../.workflow/specKitWebWorkflow.md) mapping documentary Constitution→Specify→Clarify→Checklist→Plan→Tasks→static Analyze, plus GitHub multi-commit non-atomicity and STOP/handoff.
- Annotated all **15** existing T IDs with `[US1..4]` in [feature tasks](../../specs/001-s2c-speckit-integration/tasks.md), with `[US1]=US-01` ... `[US4]=US-04` crosswalk; no IDs or task completion boxes were changed. T001–T005 and T010 remain completed only as documentary work. T011/T012/T015 are human/owner gates and cannot be auto-checked by a coding agent.
- Updated root [AGENTS](../../AGENTS.md), [S2C master](../.spec.md), global [RTM](../.traceMatrix.md), [risk matrix](../.riskMatrix.md), [project plans](../.plans.md), [feature test catalogue](../../specs/001-s2c-speckit-integration/checklists/integrationAcceptance.md), [feature spec](../../specs/001-s2c-speckit-integration/spec.md), [logical data model](../../specs/001-s2c-speckit-integration/data-model.md) and [.specify README](../../.specify/README.md); all changes were Markdown, not runtime Python/JSON/CI.

## 2. Actual test executions and reproducible provider evidence

[Detailed Web/Static execution record](../.documents/specKitWebModeEvidence095.md) is pinned to Git SHA `916ed6aa769e1fb9c25d9bd988277275613ae695`:

| Case | Actual operation | Outcome scope |
| --- | --- | --- |
| `SKI-TC-001-P` | Parse `.specify/feature.json` and confirm selected in-repo feature paths in exact Git tree | PASS_STATIC_GITHUB; no local symlink/junction/Path Guard test |
| `SKI-TC-003-P` | Confirm required tracked feature artifacts, 15 distinct task IDs parsed using real S2C config regex after `[US]` labels | PASS_STATIC_GITHUB; no Python bridge execution |
| `SKI-TC-004-P` | **Real GitHub file write** of only `specs/001-s2c-speckit-integration/quickstart.md` from HEAD `1709037a6975b846478e80151d129fb486a` to commit `916ed6aa769e1fb9c25d9bd988277275613ae695`; compare returned **1 commit / 1 changed path**, exact marker/blob/branch readback matched | PASS_WEB_CONNECTOR_WRITE; not native tool/OS security |
| `SKI-TC-006-P` | Exact FR→RTM→case reverse trace check: 12 unique feature requirements, 12 individual RTM rows and 24 unique P/N case IDs; no orphan | PASS_STATIC_GITHUB; no independent BR correctness signoff |

**Totals:** 4/24 narrow positive cases **PASS on the observed GitHub surface**; 20/24 **NOT_RUN**. All eight `SK95-GATE-01..08` native/approval scenarios **DESIGNED/NOT_RUN**. The actual local Spec Kit CLI, official scripts, S2C Python host checks and independent reviewer signoff were **not executed**.

**Link integrity:** static readback at source `e39f8f41e7b0fc29db8ac23360a6b3c5f61f8fa8` confirmed **282 relative Markdown links across 17 files edited in PLAN-095**, zero missing target paths (163 links in 9 documents + 119 in 8 feature/readme documents). This inspects paths, not fragment anchors/rendered content. After a subsequent canonical SRS Section 21 commit, review its newly added links separately; do not claim the 282 count covered files changed afterward.

## 3. User approval, source drift and next steps

- No registered accountable independent A.1 reviewer, accepted Constitution, owner-approved native version, B task, host Path Guard acceptance or independent B.1 decision. [PLAN-093 native pilot runbook](../.documents/specKitNativePilot.md) remains blocked by this terminal's lack of network access and `specify` tool. Never invoke `$speckit-implement` or `$speckit-converge` on the mixed T001..T015 queue; an upstream checklist continuation question does not change this.
- **Next Web-safe work:** real owner/independent design review of the [native execution gate](../.workflow/specKitNativeExecutionGate.md), current source, risk and global RTM; collect actual approver signatures on a source SHA and record exact source/Google revision comparison. A same-model lens review is not independent authority.
- **Next native test only in an authorized executor:** use an isolated network-enabled Codex/Codespaces checkout, owner-reviewed official version and generated-file collision/rollback plan, capture actual `specify version` / `specify init` / prerequisite outputs and host security tests. Do not import generated files or merge without separately approved scope.

**STOP/PERSISTENCE:** GitHub documentation changes are committed on the existing branch; Google write was acknowledged but readback rate-limited; no native Spec Kit process or S2C Workflow Guard session was started. Re-fetch actual latest HEAD and task/approval states on RESUME, and preserve the original PLAN-090..094 handoffs.
