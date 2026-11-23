# WEB-001..003 — v1.0 Markdown-first documentation preflight and 64-feature disposition

Date: 2026-11-23 (Asia/Ho_Chi_Minh). Repository: RyugaWork/spec2code. Observed development branch: docs/plan-089-a1-readiness. **Input HEAD: d7fed7bb7d6d791f0c62f4315a66a729bb5f52ea**. Author-side GitHub/Markdown examination only; **OWNER_REVIEW_PENDING / PREFLIGHT_ONLY**. This is not independent A.1, an approved scope, Phase B permission, executed Web tests or a release. Do not mistake a source-level implementation status for Web availability.

## 1. Remote baseline and branch/PR inventory (WEB-001)

- At observation: eight remote branches: main (76a270ba01c52d06571ffba2e7e2436faa473fcd), spec2code/InitialVersion_v0 (65d469fa7e8cd42cbbe4c8c9ebe98619ab57dd03), refactor/repository-layout-v0.7.0, feat/governance-integration-v0.8.0, feat/agent-governance-v0.8.0, docs/plan-088-unified-s2c, docs/plan-089-a1-readiness and docs/plan-090-a1-review-findings. Full SHAs for the first two appear above; fetch current branch refs before any later integration.
- GitHub PR list showed 11 historical PRs: #1..#7 closed (do not infer individually merged), #8..#11 OPEN/DRAFT. Stacked open targets: #8 agent-governance -> governance-integration; #9 plan-088 -> agent-governance; #10 plan-089 -> plan-088; #11 plan-090 findings -> plan-089. Preserve the independent findings review rather than silently merging it into the author baseline.
- Current main and the development branch are DIVERGED: ahead 270 / behind 1 relative to main, common ancestor bbca968eccdf7cb8405a63e68edaede7f5b0c9c2. Reconcile main's unique change through a reviewed non-force integration decision; a 270-commit history is not evidence of v1 approval.
- Git tree at input HEAD: 186 entries, 165 tracked blobs and 123 Markdown blobs; **no .source/profiles/web/ subtree**. The proposed Web package remains unimplemented, not a release payload.
- GitHub releases list: zero entries at observation. No v1 tag/release claim. This inventory is remote-only: no checkout, Windows VM, host installation, Google Doc parity or complete line-by-line static audit observed.

Source: [PLAN-116](../.documents/markdownFirstReleasePlan.md), [canonical task ledger](../.plans.md), [feature register](../.features.md), [PR #10](https://github.com/RyugaWork/spec2code/pull/10), [PR #11](https://github.com/RyugaWork/spec2code/pull/11).

## 2. PR #11 findings: current author disposition (WEB-002)

The following are **current author assessments**, not the PR reviewer's signoff. P0/P1 observations remain open unless an authorized reviewer accepts a verified remedy.

| Finding | Priority in PR #11 | Current assessment | Needed evidence / owner |
| --- | --- | --- | --- |
| REV-090-01 | P0 | OPEN_OWNER | Product/host/security approver and authority for exact Web scope; earlier APP-01..06 cover design direction only. |
| REV-090-02 | P0 | OPEN_GLOBAL; WEB_SCOPE_EXCLUSION_CANDIDATE | Actual Windows Path Guard, Workflow Guard and hostile-host evidence for runtime. Independently demonstrate no reachable runtime in Web-only distribution; do not close RM-001 globally. |
| REV-090-03 | P1 | RECHECK_REQUIRED | 42 legacy BR scenario IDs are designed, not executed; verify individual oracles, fixture feasibility and coverage on final source. Separate from 15 WEB-TC cases. |
| REV-090-04 | P1 | DEFERRED_ENGINE; OPEN_GLOBAL | Worker isolation, review quorum/budgets and artifact ownership are future multi-agent/runtime decisions; Web human-directed review still needs ownership/false-approval checks. |
| REV-090-05 | P1 | OPEN_BRANCH_INTEGRATION | Four stacked draft PRs plus divergent main; review integration graph and choose immutable target/merge policy before v1 release. |
| REV-090-06 | P1 | OPEN_SOURCE_PARITY | Git/Google BRD semantic equivalence was an open finding at this historical preflight. D01 now specifies the reviewed Git SHA as the Web V1 baseline. Cite the archived Google source when relevant to provenance. |
| REV-090-07 | P1 | OPEN_INDEPENDENT_A1 | Same-model sequential lenses are not independent review; real external A1-VAL-01..09 required. |
| REV-090-08 | P2 | NO_MATCH_IN_CURRENT_MASTER | Text scan of current .agents/.spec.md found zero literal A.1-VAL-0x labels and eight canonical A1-VAL-0x matches. This narrow display defect appears corrected; no rendered Markdown or independent review claimed. |
| REV-090-09 | P2 | NO_MATCH_IN_CURRENT_MASTER | Text scan found zero escaped-backtick tokens in current .agents/.spec.md. Narrow source symptom absent; visual rendering not independently verified. |
| REV-090-10 | P1 | OPEN_ACCEPTANCE_BASELINES | Owner/QA must define relevant Web capability, host/provider support, measurable mandatory groups, denominators, security cases and budget/latency scope; deferred local OS/runtime metrics are not silently approved. |

Web-scope test suite remains **15 DESIGNED / 0 EXECUTED** (WEB-TC-01..15). Runtime A.1 is NO-GO/NOT_RUN, Phase B NOT_AUTHORIZED, B.1 NOT_RUN. RM-001 is P0 OPEN (4 x 5 = 20), residual UNKNOWN. Any applicable Web P0 also blocks v1.

## 3. Feature disposition proposal: exactly F01..F64 (WEB-003)

Existing feature-status labels below are preserved as an interpretation of [the feature register](../.features.md), not verified runtime acceptance. IMPLEMENTED_SOURCE means code/document source exists; it is not a released or secure Web feature. F43..64 are DESIGN_PROPOSED; F21..23 remain DROPPED.

Disposition meaning:
- WEB_MANUAL: reusable as human-directed Markdown instructions, planning, document review or gate; not machine automation.
- CONDITIONAL_READ_MAPPING: only a manual, permissioned source/Spec Kit Markdown mapping; actual provider read may be unavailable, native bridge not executed.
- REFERENCE_ONLY: design/reference/ownership rules inform Web docs; original implementation is not distributed or invoked.
- RUNTIME_EXCLUDED: local execution and OS security capabilities explicitly outside Web v1.
- DEFERRED_FUTURE: optional integration/automation/candidate F43..64 must have separately approved future release; no v1 implementation claim.
- DROPPED: prohibited or intentionally abandoned behavior remains out.

| ID | Existing status (author interpretation) | v1 Web disposition proposal |
| --- | --- | --- |
| F01 | IMPLEMENTED_SOURCE | WEB_MANUAL |
| F02 | IMPLEMENTED_SOURCE | WEB_MANUAL |
| F03 | IMPLEMENTED_SOURCE | WEB_MANUAL |
| F04 | IMPLEMENTED_SOURCE | RUNTIME_EXCLUDED |
| F05 | IMPLEMENTED_SOURCE | WEB_MANUAL |
| F06 | IMPLEMENTED_SOURCE | WEB_MANUAL |
| F07 | IMPLEMENTED_SOURCE | CONDITIONAL_READ_MAPPING |
| F08 | IMPLEMENTED_SOURCE | REFERENCE_ONLY |
| F09 | IMPLEMENTED_SOURCE | RUNTIME_EXCLUDED |
| F10 | IMPLEMENTED_SOURCE | DEFERRED_FUTURE |
| F11 | IN_PROGRESS | REFERENCE_ONLY |
| F12 | IN_PROGRESS | WEB_MANUAL |
| F13 | IMPLEMENTED_SOURCE | RUNTIME_EXCLUDED |
| F14 | PLANNED | REFERENCE_ONLY |
| F15 | IN_PROGRESS | RUNTIME_EXCLUDED |
| F16 | IMPLEMENTED_SOURCE | REFERENCE_ONLY |
| F17 | PLANNED | WEB_MANUAL |
| F18 | PLANNED | WEB_MANUAL |
| F19 | DEFERRED | DEFERRED_FUTURE |
| F20 | PLANNED | DEFERRED_FUTURE |
| F21 | DROPPED | DROPPED |
| F22 | DROPPED | DROPPED |
| F23 | DROPPED | DROPPED |
| F24 | IN_PROGRESS | REFERENCE_ONLY |
| F25 | IN_PROGRESS | REFERENCE_ONLY |
| F26 | IN_PROGRESS | REFERENCE_ONLY |
| F27 | IMPLEMENTED_SOURCE | WEB_MANUAL |
| F28 | IMPLEMENTED_SOURCE | WEB_MANUAL |
| F29 | IMPLEMENTED_SOURCE | WEB_MANUAL |
| F30 | IMPLEMENTED_SOURCE | WEB_MANUAL |
| F31 | IN_PROGRESS | RUNTIME_EXCLUDED |
| F32 | IMPLEMENTED_SOURCE | WEB_MANUAL |
| F33 | IMPLEMENTED_SOURCE | WEB_MANUAL |
| F34 | IMPLEMENTED_SOURCE | WEB_MANUAL |
| F35 | IMPLEMENTED_SOURCE | WEB_MANUAL |
| F36 | IN_PROGRESS | WEB_MANUAL |
| F37 | IN_PROGRESS | WEB_MANUAL |
| F38 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F39 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F40 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F41 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F42 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F43 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F44 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F45 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F46 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F47 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F48 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F49 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F50 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F51 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F52 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F53 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F54 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F55 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F56 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F57 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F58 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F59 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F60 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F61 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F62 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F63 | DESIGN_PROPOSED | DEFERRED_FUTURE |
| F64 | DESIGN_PROPOSED | DEFERRED_FUTURE |

Coverage check: WEB_MANUAL=18; RUNTIME_EXCLUDED=5; CONDITIONAL_READ_MAPPING=1; REFERENCE_ONLY=7; DEFERRED_FUTURE=30; DROPPED=3; total 64 unique IDs. This is a **proposed applicability matrix**, not DEC-WEB-01 scope approval. No new F ID or status promotion.

## 4. Evidence and next document actions

- WEB-001: remote branch/PR/tree/reference snapshot authored. Confirm post-commit SHA and review Git main unique diff/local state before integration.
- WEB-002: all 10 REV-090 findings have an explicit author disposition; reviewers must sign or correct findings; do not retrospectively close P0.
- WEB-003: all 64 existing F IDs mapped once. Product/architecture owners review Web inclusion; require reverse RTM mapping for finalized scope.
- WEB-004/005 are external hard gates: approve the scope/risk/owner/source/version decisions in [Web owner decision packet](webV1OwnerDecisionRegister.md), conduct independent Web profile A.1 and provide separate B authorization.
- Until WEB-005 is satisfied, **do not author/distribute the actual v1 Web SKILL/BOOTSTRAP/templates as product implementation**; documentation reviews and owner-ready decision drafts remain A-phase only.
- No test, host OS exercise, Google comparison, profile install, Git merge, tag or release was executed by this preflight. Other historical source claims remain bound to their original revisions.

See [planned test catalogue](../.workflow/testingAndDelivery.md), [risk review](../.riskMatrix.md) and [PLAN-116 handoff](../.handoffs/plan-116-markdown-first-release-handoff.md).
