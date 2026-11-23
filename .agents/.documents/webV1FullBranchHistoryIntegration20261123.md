# Phase A — consolidated history merge and safe PR #11 resolution

**CONTENT_AND_ANCESTRY_INTEGRATION / NO_A1_SIGNOFF.** Source first parent `fbd56e01daef0029db0aaac844466dde1dfe516e`, historical PR #11 parent `e119100e17ed138a1bbd1d2b600d9b890d5441b7`, and historical `InitialVersion_v0` parent `65d469fa7e8cd42cbbe4c8c9ebe98619ab57dd03`. The final merge has all three commit parents, retaining their complete commit history and original file blobs. This record does not constitute GitHub PR #8–#11 merge/closure or owner approval.

## Coverage of branch tips

| Branch / history | Observed head | Integration status |
| --- | --- | --- |
| `s2c/PhaseA` | `fbd56e01daef0029db0aaac844466dde1dfe516e` | First parent and canonical tree owner |
| `docs/plan-090-a1-review-findings` | `e119100e17ed138a1bbd1d2b600d9b890d5441b7` | Second parent, 3 previously unique commits; archive plus historical reviewer report |
| `spec2code/InitialVersion_v0` | `65d469fa7e8cd42cbbe4c8c9ebe98619ab57dd03` | Third parent for unique merge commit; no file divergence beyond original Phase A tree |
| `main` | `76a270ba01c52d06571ffba2e7e2436faa473fcd` | Already ancestor of PhaseA; comprehensive existing `.gitignore` retained |
| `docs/plan-089-a1-readiness` | `dd78031aa4c0c0f09e0cbb6c03bd1fa885568ba8` | Already ancestor |
| `docs/plan-088-unified-s2c` | `53575d26fc3a50f5b0edcd256f76326161de6f9d` | Already ancestor |
| `feat/agent-governance-v0.8.0` | `ed81320cbd54196334050506eaf087f59ba62993` | Already ancestor |
| `feat/governance-integration-v0.8.0` | `8f936e95dc4ff3cc4d936fd5e5167b86e441fbfe` | Already ancestor |
| `refactor/repository-layout-v0.7.0` | `0d70cd1e899d8df41e8ecda75bfaee84d7fa52be` | Already ancestor; remote branch previously deleted |

## Explicit conflict resolution

- **All new PR #11 content preserved:** the full `.agents/.handoffs/plan-090-a1-preflight-review.md` (original blob) and [180 exact historical added lines](webV1Pr11AddedLinesArchive20261123.md), plus true merge-parent ancestry with the complete source.
- **Canonical content protected:** current `AGENTS.md`, `.agents/.spec.md`, `.agents/.features.md`, `.agents/.riskMatrix.md`, `.agents/.traceMatrix.md`, `.agents/.plans.md` definitions, including F43..64, RM-001..052, PLAN-091 and Web V1 task/AC IDs, are not replaced by colliding PR #11 definitions.
- **Conceptual reuse:** [PR #11 collision mapping](webV1Pr11CollisionReconciliation20261123.md) maps candidate features/risks but does not assert full equivalence or actual execution. Optional CI/adapters/cloud-worker concepts remain historical/future-scope; no CI activation or general permission grant.
- **A.1 baseline still pending:** reviewer, Google BRD semantic authority, BR-007/008, QA metric and risk-owner approvals are unresolved. No Phase B, B.1 or release.

## Branch cleanup notes

This operation integrates history on **only `s2c/PhaseA`**. No other branch is moved, no PR is closed, and no branch is deleted. PR #11 historical source stays intact as an open draft PR until Git Owner explicitly decides the review/closure method. Merging ancestry is not the same as accepting unresolved design identities into the live specification. All applicable tests remain NOT_RUN until actual execution and evidence.
