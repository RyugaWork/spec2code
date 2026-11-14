# PLAN-104 — Batch A: ten-document-task source-bound handoff

2026-11-14 Asia/Ho_Chi_Minh · repository `RyugaWork/spec2code` · branch `docs/plan-089-a1-readiness` · **input Git SHA `deebce3aee5db864f28bdb1f761f93febc0eb711`**. **Output SHA:** the commit containing this file; verify the branch ref before resuming. This handoff is a single batch checkpoint for ten completed **draft-authoring** tasks, not ten mini-commits.

| Task | Existing owner file | Authoring deliverable | Technical-review status |
| --- | --- | --- | --- |
| DOC-A01 | `.agents/.spec.md` | Requirement authority/acceptance states | AUTHORED / STATIC_REVIEW_PENDING |
| DOC-A02 | `.agents/.documents/systemSpecificationPlan.md` | SRS owner decision packet | AUTHORED / STATIC_REVIEW_PENDING |
| DOC-A03 | `.agents/.traceMatrix.md` | RTM edge and gap meanings | AUTHORED / STATIC_REVIEW_PENDING |
| DOC-A04 | `.agents/.workflow/testingAndDelivery.md` | Test execution evidence schema | AUTHORED / STATIC_REVIEW_PENDING |
| DOC-A05 | `.agents/.riskMatrix.md` | P0 risk treatment priority | AUTHORED / STATIC_REVIEW_PENDING |
| DOC-A06 | `.agents/.workflow/validationSpecification.md` | Independent A.1 rubric | AUTHORED / STATIC_REVIEW_PENDING |
| DOC-A07 | `.agents/.documents/featureDesign.md` | Producer-consumer contracts | AUTHORED / STATIC_REVIEW_PENDING |
| DOC-A08 | `.agents/.workflow/agentRoles.md` | Reviewer weighting and correlation | AUTHORED / STATIC_REVIEW_PENDING |
| DOC-A09 | `.agents/.workflow/agentRunbook.md` | Codex CLI preflight/fallback | AUTHORED / STATIC_REVIEW_PENDING |
| DOC-A10 | `.agents/.workflow/specKitNativeExecutionGate.md` | Native Spec Kit mutation guard | AUTHORED / STATIC_REVIEW_PENDING |

## Input evidence, risks and acceptance

Baseline `deebce3aee5db864f28bdb1f761f93febc0eb711` is the last verified PR #10 Draft head. PLAN-103 had explicit 44 candidate F tests across BR-022..027, 12 MM cases, nine A1 gates and open P0; this batch does not add feature/AC/test/risk IDs or run them. Each edited file receives one bounded topic-specific contract rather than a duplicate BRD/SRS or an executable agent. A model using separate analytical perspectives is **one author**, not ten independent workers; no independent A.1 result is claimed.

Review criteria for this batch: exactly ten existing Markdown owner files edited plus this handoff, no deleted historical material, no test checkbox/status promotions, valid links/anchors, source-bound fast-forward Git SHA and recorded pending approvals. Need a second bounded batch only **after this handoff is committed and verified**.

## Explicit blockers and safe resume

`AUTHORING_COMPLETE_CANDIDATE` only. Product/architecture/security owners have not signed BR-022..027, ADR-102 or DEC-091/101; P0 exposure remains open; `A1_NOT_RUN / B_NOT_AUTHORIZED / B1_NOT_RUN`. No local CLI, `git status`, OS Path Guard, Codex `--full-auto`, Gemini/AGY MCP, real Spec Kit native or host regression was run through this connector. The nine prior local changed paths remain untouched by these remote documentation updates.

Resume on verified **output** SHA, inspect this handoff and the new sections, then perform **DOC-B01..B10** with one second handoff. On any branch move, owner/policy conflict, or missing source equivalence, STOP and reconcile; never force-update, merge PR #10 or self-approve a gate.
