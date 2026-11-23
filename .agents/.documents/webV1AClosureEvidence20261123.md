# Web v1.0 — A-Closure Git, BRD, REV-090 and static evidence report

Date: 2026-11-23. **A_AUTHOR_EVIDENCE_CLOSURE_CANDIDATE / A1_NOT_RUN / OWNER_PENDING**. Reviewed input HEAD `c0201acaf0639b271cdaba3110894298556d86d6` on `docs/plan-089-a1-readiness`. A later report commit must be read back; this input SHA is **NOT** a frozen A.1 baseline. This is author-side remote/static evidence, not independent reviewer approval or local host validation.

## 1. Git branch, PR and source lineage at reviewed input

| Source | Observed HEAD | Relationship / disposition |
| --- | --- | --- |
| `main` | `76a270ba01c52d06571ffba2e7e2436faa473fcd` | Relative to development input: diverged by **1 unique main commit** that only adds `.gitignore` with `__pycache__/` and `*.py[cod]`; integrate only by reviewed Git owner action |
| PR #8 `feat/agent-governance-v0.8.0` | `ed81320cbd54196334050506eaf087f59ba62993` | Draft; base `feat/governance-integration-v0.8.0` (`8f936e95dc4ff3cc4d936fd5e5167b86e441fbfe`) |
| PR #9 `docs/plan-088-unified-s2c` | `53575d26fc3a50f5b0edcd256f76326161de6f9d` | Draft; base PR #8 head |
| PR #10 `docs/plan-089-a1-readiness` | `c0201acaf0639b271cdaba3110894298556d86d6` | Draft, source of this author-side work; base PR #9 head |
| PR #11 `docs/plan-090-a1-review-findings` | `e119100e17ed138a1bbd1d2b600d9b890d5441b7` | Draft; separately authored from older PR #10 head `1dae9338f4d38518e897212cdf80ba47239a7671`; **3 unique commits, 7 changed paths; GitHub mergeable=false/dirty** at inspection |
| `spec2code/InitialVersion_v0` | `65d469fa7e8cd42cbbe4c8c9ebe98619ab57dd03` | Diverges at `8f936e95dc4ff3cc4d936fd5e5167b86e441fbfe`; its single unique merge commit #7 has **no reverse changed-file delta** relative to development input; do not re-merge based only on history |

GitHub raw compare and files were inspected **read-only**. PR #11's seven changed paths are `.agents/.features.md`, `.agents/.handoffs/plan-090-a1-preflight-review.md`, `.agents/.plans.md`, `.agents/.riskMatrix.md`, `.agents/.spec.md`, `.agents/.traceMatrix.md`, `AGENTS.md`. The historical review report is preserved on its existing branch; this source-bound finding crosswalk **does not** imply those seven files were safely merged or that PR #11 is an independent human signoff. PR stack cannot be auto-merged; one signed eventual target strategy is required.

## 2. Git versus connected Google BRD — observed source pair, not approval

| Field | Git candidate | Google stakeholder source |
| --- | --- | --- |
| Authority | `.agents/.spec.md` is the current technical master, owner approval still needed | [BRD_Spec2Code](https://docs.google.com/document/d/1M3_2tNUxOXci83pcpPCzBkxwvRvixeT7FYeGyIsFOa4/edit), **Draft v1.5** |
| Observed revision | Git `c0201acaf0639b271cdaba3110894298556d86d6` | `AHj4eMTQo-4II6DrQF5kSGoY8OxDNISChHco-PFSx_OgzuUuEWu4R2qAsiNmlioUDwDF-cYLmUq__B8TxyeB5iOzSa8tL5uDM_9Rqh0Npw` |
| BR identifiers | 27 unique `BR-001..027` | 27 unique `BR-001..027` observed in current extracted document text |
| Formal semantic equivalence | NOT_SIGNED | NOT_SIGNED; a live Draft can change again |
| Required owner result | Signed exact Git+Google source pair with differences recorded | Versioned immutable Git-linked stakeholder snapshot/reference, permitted content and fingerprint; no unapproved Doc overwrite |

**Material wording review still needed:**
- Google `BR-003` explicitly describes a *seven-stage business overview* alongside nine task stages and five machine phases; Git BR-003 emphasizes one workflow with manual/runtime mapping. Record the three-level hierarchy explicitly before approving any workflow-state interpretation.
- Google general feature prose in sections 4.6–4.10 describes AST manipulation, RBAC/AI firewall, background drift detection and multi-agent consensus as principles/goals. The Git feature register identifies proposed/deferred runtime capabilities. The owner must label such prose `FUTURE_DESIGN` rather than accept it as a V1 implementation claim.
- Google BR-022..027 and Git's PLAN-A1-AC share proposal groups but AC thresholds and signed revision parity remain `BUSINESS_AC_PENDING`. Matching BR IDs cannot establish semantic or quantitative equality.
- The historical PR #11 Google revision was a **different earlier revision**; no replay of that approval is valid for this current pair.

No Google Doc body was copied into a new public Git source, no Google document was edited, and no unverifiable source checksum was invented.

## 3. PR #11 REV-090-01..10 — current author disposition

The original [review handoff on PR #11](https://github.com/RyugaWork/spec2code/blob/docs/plan-090-a1-review-findings/.agents/.handoffs/plan-090-a1-preflight-review.md) remains **unmodified**. These are fresh author-side dispositions, **not** formal closure of those reviewer findings.

| Finding | Original priority | Current author finding status | Evidence / remaining gap | Responsible decision |
| --- | --- | --- | --- | --- |
| REV-090-01 | P0 | OWNER_BLOCKED | No named Product/Security/Host authority or approved Web BR/AC scope. U-01..06 and owner packet proposed, no signatures. | Product/host/security owner assignment and approved BR/AC; A1-VAL-01/09 |
| REV-090-02 | P0 | GLOBAL_OPEN / WEB_MODE_DECISION_PENDING | RM-001 Windows race remains OPEN P0/20; remote-only read/write boundaries are design proposals. Source guard fixes do not demonstrate hostile Windows containment. | Security per-mode risk signature; local Windows tests remain NOT_RUN |
| REV-090-03 | P1 | GLOBAL_DESIGN_EXISTS / WEB_21_ORACLES_DRAFT | 42 legacy TC-S2C-BR001..021-P/N have preconditions, procedure, expected result and evidence in canonical catalogue, but no observed runs or host adapters. 21 Web TC designed, subvariants need QA approval. | QA owns executable fixture, case thresholds and host/provider assertion method |
| REV-090-04 | P1 | FUTURE_REVIEW_ENGINE_DEFERRED | ReviewManifest/worker quotas/isolated provider API remain proposal; no V1 engine capability. AGENTS matrix does not run a worker fleet. | Architecture + QA approves future contract, no V1 runtime promotion |
| REV-090-05 | P1 | GIT_INVENTORY_AUTHOR_VERIFIED / RELEASE_TARGET_PENDING | PR #8..11 draft stack enumerated; PR #11 diverges (3 unique commits, 7 files), dirty merge state. main unique .gitignore commit identified; InitialVersion_v0 divergent merge #7 but no reverse file delta against current. | Git owner approves exact target/merge strategy; no author merge/force |
| REV-090-06 | P1 | ID_SET_OBSERVED / SEMANTIC_PARITY_PENDING | Google BRD Draft v1.5 current revision and Git v1.5 both include BR-001..027, but 27 matching IDs are not text equivalence. Historical Google v1.4/revision is stale. | Product binds approved Google revision, Git SHA and material-difference decisions |
| REV-090-07 | P1 | INDEPENDENT_REVIEW_NOT_RUN | PR #10/#11 reviewer submissions zero in observed API; six model role-lenses are not independent human validation. | Assign actual independent reviewer and conduct A1-VAL-01..09 after signed scope |
| REV-090-08 | P2 | NARROW_SOURCE_SYMPTOM_ABSENT | No literal A.1-VAL-0x typo in current master .agents/.spec.md source; canonical A1-VAL ID remains. This is narrow source check, not independent review. | Retain history; reviewer confirms rendered ID/links at frozen source |
| REV-090-09 | P2 | NARROW_SOURCE_SYMPTOM_ABSENT | No literal escaped backtick tokens in current master .agents/.spec.md source. Does not prove all Markdown visually renders. | Retain history; markdown rendering review on frozen source |
| REV-090-10 | P1 | WEB_METRIC_OWNER_BLOCKED | 21 deterministic Web cases proposed. Inherited R>99.99% cannot be silently waived or empirically proved by 21 design IDs. Host version/budget support remains owner pending. | Product+QA approve Web-specific denominators/metric treatment and platform matrix |

No ten findings were silently converted to A.1 PASS. REV-090-08/09 only have their **specific original text symptoms** absent from the current master; independent rendered review remains open.

## 4. Pinned upstream Spec Kit structural reference

Public [Spec Kit v1.4.3](https://github.com/github/spec-kit/releases/tag/v1.4.3) released 2026-11-19 14:31:35 UTC: annotated tag `d274613d7469a72d946d61f76b4f2b9bb11b91e2` resolves to commit **`980b3d027f4bd7958c35f97f618d854b41320e3f`**. The remote commit tree contains `.specify/memory/constitution.md`, `templates/spec-template.md`, `templates/plan-template.md`, `templates/tasks-template.md`; `scripts/bash/common.sh` explicitly uses `.specify/feature.json` `feature_directory` and `SPECIFY_FEATURE_DIRECTORY`, and `docs/quickstart.md` describes this active-feature selection. **The generated feature.json may not exist in each host project, so absence/ambiguity must fail closed or use an approved explicit feature selection.** This is verified *upstream structural design*, NOT proof of installed host/native CLI support or compatibility across all upstream presets.

Web v1 maps actual supplied `specs/<feature>/spec.md`, `plan.md`, `tasks.md` read-only; `.specify/` and `specs/` remain upstream-owned. Only an owner can approve the supported upstream tag/provider distribution/manifest contract.

## 5. Static preflight and trace coverage at reviewed source

- Git recursive tree: **131 tracked Markdown blobs** at input SHA. The previous [125-Markdown source/path preflight](webV1StaticMarkdownAudit20261123.md) examined pre-addendum content at `fa2ba44e4a2076cf004160831fdaa7a3f2ec8148`. Git compare from that exact SHA to this input contains **15 changed Markdown paths** (six new and nine modified); these paths were rechecked for relative tracked-file links.
- The 15 paths yielded **435 counted relative link occurrences** with no missing tracked-file target under this bounded line-oriented Markdown check. Prior audit's 11 historical stale links in three v0.6.4 archived handoffs remain historical and intentionally unrepaired. Both scans exclude remote URLs, rich Markdown anchors, inline HTML targets and semantic correctness. This is an **incremental file-target check**, not a full 131-file line-by-line semantic or visual audit.
- Source-grounded IDs: **F01..64 (64 unique), RM-001..052 (52 unique; 35 WEB_APPLIES/12 SPLIT/5 RUNTIME_EXCLUDED), AGM-01..17 (17 unique), WEB-AC-01..21 and WEB-TC-01..21 (each 21 unique), WEB-001..030 (30 unique)**. All 52 Web risk dispositions remain `PENDING_OWNER`, all 21 Web tests `NOT_RUN`.
- Canonical Web test references name only existing task IDs; all 21 proposed AC rows map to exactly one of the canonical 21 test IDs. All 17 AGM rows mention an existing Web case. Nine WEB tasks (`WEB-002/003/004/005/021/026/027/028/030`) do not have a *direct case ID* in the 21-case catalogue: they are primarily author governance, preflight, risk and release-owner gates, so they need **separate owner/evidence oracles**, not fabricated test PASS.
- The [64-F reverse mapping](webV1AClosureFeatureReverseMatrix20261123.md) distinguishes source-level implementation statuses from Web scope and documents BR-007/008's missing direct Web case as owner-choice `REFERENCE_ONLY`/new assertion decision.
- Legacy 42 `TC-S2C-BR001..021-P/N` scenarios exist **as detailed test designs** in the separate canonical catalogue, all NOT_RUN. They are not the 21 Web acceptance cases; no Windows sandbox, runtime or provider test was executed by this preflight.

## 6. Definition of A author-preflight completion and hard STOPs

**Author-owned, source-bound work that can be marked DONE_VERIFIED after commit/readback:** `WEB-001` exact branch/PR/ref/tree inventory and remote/local distinction; `WEB-002` 10-review finding crosswalk plus main and InitialVersion comparisons; `WEB-003` 64 F scope plus reverse task/test proposal. These are documentation subdeliverables only. The approved Web profile, independent A.1 and actual tests are NOT done.

**External hard gates:** WEB-004/005 require Product/Security/Architecture approvals for BR/AC, RM applicability, scope and version; A1-VAL-01..09 independent review at one **later frozen source SHA**; separate explicit B permission; actual WEB-006..030 product/tests/release later. An author-drafted report is not the reviewer. No Go release, no local Windows race test, no host AGENTS write, no Google edit, no Git merge/tag in this A phase.

**Next owner packet:** [U-01..06 and source/risk/branch/reviewer decisions](webV1AClosureApprovalPacket20261123.md) (draft for review, no signed outcome).


## 7. PR #11 semantic collision and whole-tree Markdown follow-up (2026-11-23)

[Full PR #11 base-to-head content crosswalk](webV1Pr11CollisionReconciliation20261123.md) confirms **8 historical feature ID collisions** (F43..50), **7 risk ID collisions** (RM-034..40) and conflicting PLAN-091 / SRS Section 18 assignments. The original PR #11 historical 3 unique commits/7 touched files and its 10-finding report are retained; no branch has been merged. Proposed action is **review-specific semantic mapping**, never auto-cherry-pick colliding IDs. [Read-only all 136 Markdown-file link audit](webV1FullMarkdownLinkAudit20261123.md) expands the earlier 125-file preflight: 1,446 syntactic link occurrences, 11 missing tracked-file paths only in three archived handoffs, 0 missing in the other 133 files (recognized syntax), zero unclosed simple code fences. These are bounded author checks and do not sign A.1. This input audit was made at `e8efc36b78f991efc618d1ca98865609d032bb0d`, not the future commit or frozen baseline.
