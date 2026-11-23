# S2C Phase A — Integration Coherence Audit (2026-11-23)

**Audit kind:** read-only GitHub source/branch/CI inspection plus declarative Markdown ID/dependency/path inspection and bounded documentation repair. **Audited input:** `RyugaWork/spec2code@s2c/PhaseA`, SHA `4f3f22928673a9c80a2fa0bf9988f2daa1a9cfb4`, Git tree `223c576403dd5a357218f5732caa37665086b5b5`. This document is an **author-side review**, not an independent A.1 decision or permission to implement B.

## 1. Executive decision

**AUTHOR_STATIC_COHERENCE: PASS_WITH_OPEN_GATES / A1_NOT_RUN / B_NOT_AUTHORIZED.** Git branch histories are consolidated in ancestry and the archived PR #11 source is fully preserved while canonical identifiers remain unchanged. The 64-feature/27-BR/30-task/21-AC/21-test/52-risk/17-AGM static matrix has no duplicated primary IDs, no out-of-range typed WEB-task/test references, and the 30-task dependency DAG has no cycles.

This result **does not** mean the V1 Web product exists or is releasable. Product/QA/Security/Git/Reviewer authority is still required, all 21 Web tests NOT_RUN and RM-001 globally OPEN/P0. The [fully enumerated cross-layer matrix](phaseAUnifiedIntegrationMatrix20261123.md) is a derived report, not a second normative specification.

## 2. Observed Git lineage, remaining administrative state

- At `4f3f22928673a9c80a2fa0bf9988f2daa1a9cfb4`, three merge parents are `fbd56e01daef0029db0aaac844466dde1dfe516e` (Phase A), `e119100e17ed138a1bbd1d2b600d9b890d5441b7` (historical PR #11) and `65d469fa7e8cd42cbbe4c8c9ebe98619ab57dd03` (InitialVersion_v0).
- Git compare against main, docs/plan-088, docs/plan-089, docs/plan-090, feat/agent-governance, feat/governance-integration, InitialVersion_v0 and historical refactor/v0.7 shows each has **0 commits not reachable from Phase A** at observed SHAs. This is history completeness, not semantic acceptance of conflicting PR #11 identifiers.
- Historical PLAN-090 report and 180 inserted PR #11 lines are in [integration history](webV1FullBranchHistoryIntegration20261123.md), [full original review](../.handoffs/plan-090-a1-preflight-review.md) and [non-normative additions archive](webV1Pr11AddedLinesArchive20261123.md). 8 feature aliases `PR11-F43..50` and 7 risk aliases `PR11-RM-034..040` remain distinct from present canonical values. No live F/RM/PLAN ID renaming.
- Current GitHub PR #8, #9, #10, #11 are still **OPEN/DRAFT** with their original bases and heads; even when content ancestry is in Phase A, the PRs have **not** been merged/closed through GitHub's PR mechanism. `main` remains the default branch. Git/Release Owner must settle PR disposition and any future main integration.

## 3. Actual CI evidence — exact audited input

[GitHub Actions run #494](https://github.com/RyugaWork/spec2code/actions/runs/45109840093), workflow `Python tests`, push event, head SHA `4f3f22928673a9c80a2fa0bf9988f2daa1a9cfb4`, completed with **success** (2026-11-23). Five completed jobs: `unittest (ubuntu-latest, 3.10)`, `unittest (ubuntu-latest, 3.11)`, `unittest (ubuntu-latest, 3.13)`, `unittest (windows-latest, 3.14)`, and `security-static` (Ruff security lint `--select S --ignore S603,S607`), **all SUCCESS**. The exact `python -m unittest discover -s .source/tests -v` step passed in each unit job.

**Limits:** No case-level log counts or hostile Windows VM containment/negative fixture report were retrieved; Ruff's selected rules ignore S603/S607; CI PASS is not a security certification. This run does **not** execute the 21 Web profile cases, actual host AGENTS remote write checks, independent A.1/B.1 or V1 package acceptance. Do not count previous Spec Kit pilot reports as a new native pilot on this SHA.

## 4. Entire tracked Markdown path-level static inspection

The complete recursive tree at `4f3f22928673a9c80a2fa0bf9988f2daa1a9cfb4` has **183 tracked files** comprising **141 Markdown** and 42 non-Markdown files. Each **141/141 Markdown blob** was independently fetched by exact blob SHA for this audit. The simple path scanner identified **1,485 `[label](target)`-style link occurrences**, checked relative file path existence against the same tree, and inspected triple-backtick/tilde fence closure. Findings: **11 missing relative paths confined to three known archived `.agents/.handoffs/legacy-v0.6.4-*` files**; 0 missing target paths elsewhere in matched syntax; 0 unterminated simple code fences; 0 unreadable Markdown blobs.

Archived exceptions: `legacy-v0.6.4-handoff.md` (6), `legacy-v0.6.4-plan.md` (2), `legacy-v0.6.4-riskdetail.md` (3). Do not rewrite them silently. **Not covered:** Markdown header fragment slug semantics, external HTTP link validity, full renderer/parser behavior, reference-style/HTML links, runtime code behavior, host filesystem or policy escape, Google Docs semantic parity.

## 5. Findings: repaired documentation versus owner-blocked work

| Finding | Severity | Verified issue | Author disposition | Remaining boundary |
| --- | --- | --- | --- | --- |
| INT-A01 | P1 | Old README still identifies `docs/plan-089-a1-readiness` as current; DEC-WEB-03 proposes staying there | Clarify current working target is `s2c/PhaseA`, preserve old PR branch as history | Git owner still decides PR #8–#11 closure/main strategy |
| INT-A02 | P1 | PR #11 reconciliation header says `PR11_NOT_MERGED` before later historical merge | Mark ancestry integrated while GitHub PR still Draft/Open; preserve original input proof | Architecture Owner must approve concept mapping |
| INT-A03 | P1 | WEB-TC-03/WEB-AC-03 canonical rows predate simultaneous Git+ZIP mismatch negative variant | Add proposed C subvariant without new test ID; still NOT_RUN | Product chooses final source precedence, QA approves oracle |
| INT-A04 | P1 | WEB-TC/AC-18/19/20 original row wording does not fully require conflict-batch no-write/no-loop | Align canonical QA design with U-06 requested kill switch, do not change result states | Provider/host grant + independent security negative test |
| INT-A05 | P1 | `.github/workflows/speckit-pilot.yml` only triggers for `docs/plan-089-a1-readiness` on workflow file changes and pins `9eacc24ffe47eadf035a3af601e4dabfb15b8fde`; proposed Web read-only reference is Spec Kit v1.4.3 at `980b3d027f4bd7958c35f97f618d854b41320e3f` | Record separate pilot provenance/version and branch-trigger drift; do not edit/enable workflow without Git/Host approval | Native pilot on Phase A remains NOT_RUN |
| INT-A06 | P1 | Google BRD Draft v1.5 and canonical Git SRS have 27 observed BR IDs, but approved revision-level semantic parity absent | Keep dual-source drift/owner decision and exact revision requirement | Product Owner signs source-of-truth and BR-007/008 |
| INT-A07 | P0 | RM-001 global Windows Path Guard TOCTOU remains OPEN 4×5=20, residual UNKNOWN | Preserve global risk and Web-only bounded scope; no waiver | Host/Security Owner; hostile local runtime remains excluded |
| INT-A08 | P2 | 11 historical missing links from archived v0.6.4 documents | Record as legacy link exceptions; no silent archive rewrite | Optional separately reviewed archive migration |
| INT-A09 | P1 | 21 Web tests and any real authorized remote AGENTS write negative fixtures not run | Keep `NOT_RUN`, strengthen case design only | A.1/permissioned Phase B and QA evidence |
| INT-A10 | P1 | No checked-in `.source/profiles/web/` distribution profile or V1 ZIP/manifest in current tree | Record planned future delivery, not falsely "installed" | WEB-005/006..020 after actual independent A.1 and explicit B |
| INT-A11 | P1 | 4 Draft PRs still open after branch ancestry merge | Do not close PRs as a side effect of this audit; issue a Git Owner administrative queue | Review PR closure/base/target and preserve discussable history |
| INT-A12 | P1 | Inherited reliability KPI `R > 99.99%` lacks approved Web-specific population/denominator | Do not claim 21 deterministic cases prove statistical reliability | Product + QA policy amendment or approved metric |

Historical documents are not rewritten merely for mentioning an old head SHA; only the active baseline/decision wording is corrected. Findings marked repaired reflect **documentary consistency changes**, not executed Web tests.

## 6. Canonical status and next review matrix

| Checkpoint | Input / dependency | Actual current state | Next action owner |
| --- | --- | --- | --- |
| A-author Git merge | Full ancestry, PR11 archive and integration record | PASS author inspection | Git Owner decides stale PR closure |
| A-author source/static RTM | 64 F, 27 BR, 30 WEB tasks, 21 AC+TC, 52 RM, 17 AGM | PASS ID/reference/DAG checks; semantic owner review pending | Architecture / QA |
| Runtime Python CI | Exact input source SHA and Actions run #494 | 5/5 CI jobs PASS | QA may add security/functional negative coverage later |
| Web V1 behavior | 21 canonical Web cases + required subvariants | 21/21 NOT_RUN | QA/implementation after A.1/B |
| BRD normative scope | Git SRS vs connected Google BRD Draft v1.5 | SEMANTIC_PARITY_NOT_APPROVED | Product Owner |
| Scope-specific RM applicability | RM-001..052 overlay | 52 PENDING_OWNER; global RM-001 P0 OPEN | Security/Host Owner |
| AGENTS integration provider | 17 clauses, remote GitHub write only on exact target grants | DESIGN_ONLY / NO_HOST_WRITE_TEST | Security/Host + QA |
| Native Spec Kit | feature.json + specs artifacts present; workflow trigger/version drift | DOCUMENT_REFERENCE_ONLY / NEW_PILOT_NOT_RUN | Spec Kit / Git Owner |
| Independent A.1 | A1-VAL-01..09, real reviewer and pinned candidate | NOT_RUN / no reviewer identity | Product + independent reviewer |
| Phase B / B.1 / release | Distinct permissions, candidate, test evidence and reviewer | NOT_AUTHORIZED / NOT_RUN / NO_RELEASE | Owner after A.1 |

## 7. Responsible handoff and explicit stop

**No A.1 freeze or B coding** while Product/Architecture/QA/Security/Git owners, independent reviewer, exact Git–Google source equivalence, BR-007/008 and reliability metric remain undecided. Current branch consolidation is a valid working source candidate, not an automatically approved release source. If an external owner changes any source/ref or provider/permission, rerun affected matrix rows and pin a fresh review SHA.

**Audit limitations:** Review is source/static plus observed GitHub Actions metadata. No local checkout execution, fresh native Spec Kit run, browser E2E, independent reviewer signoff or red-team Windows sandbox exercise by this assistant.


## Connected Google BRD semantic source check (2026-11-23)

[27-row BR-by-BR exact source-locator reconciliation](phaseABrdSemanticReconciliation20261123.md) compares native `BRD_Spec2Code` Draft v1.5, revision `AHj4eMTQo-4II6DrQF5kSGoY8OxDNISChHco-PFSx_OgzuUuEWu4R2qAsiNmlioUDwDF-cYLmUq__B8TxyeB5iOzSa8tL5uDM_9Rqh0Npw`, against Git SRS at `79a45e0486ea8792a49fd9e7fa4a85c89ec4ca82`. Author editorial clarifications address BR-003 7/9/5 layers, BR-017 n=1 review independence and BR-027 **draft** threshold language. The current V1 scope explicitly includes read/upload plus authorized **remote GitHub AGENTS-only write**; general Git/OS/CI writing remains excluded. **Semantic parity and AC remain OWNER_PENDING**. Product must accept/revise the specific 27-row matrix, select BR-007/008 reference-only versus existing-test assertions, and approve/reject the inherited R>99.99% Web applicability/measurement with QA. Reading the exact live revision is not a signature. A.1 NOT_RUN, B NOT_AUTHORIZED.

## D01–D06 requester decision supersession (2026-11-23)

**Requester design decisions now recorded:** D01 = **Git alone normative**. Previous Google `BRD_Spec2Code` v1.5 is a *historical Gemini-era source*, imported in its entirety into Git as [source archive](legacyGoogleBrdSourceArchive20261123.md); **do not require future Google revision matching or treat Google as a second current business authority**. Source conflict checks still apply to other differing Git/ZIP/snapshot inputs. D02 = **all BR-001..016 receive individual dedicated Web AC and TC**: [16 pairs](phaseAD02BrDedicatedWebCoverage20261123.md); BR-007 and BR-008 are **not** REFERENCE_ONLY for Web acceptance. D03 = BR-017..021 accepted as architecture/requirements **design scope**, automated reviewer fleet deferred. D04 = BR-022..027 retained in roadmap, **not mandatory V1 implementation**. D05 = **100% PASS of applicable mandatory Web AC/test P/N variants** required for V1 release; inherited `R>99.99%` and BR-027 `>95%` scoped coverage await approved measurement/denominator rather than an invented waiver. D06 = read/upload in ChatGPT Web plus only **individually authorized remote GitHub API host AGENTS.md-only writes**; local OS/native agent writes excluded. Full dispositions: [decision register](phaseAD01D06RequesterDecisionRegister20261123.md).

**Current suite: 37 AC + 37 planned TC (21 baseline + 16 BR-dedicated), 37/37 NOT_RUN.** No actual host permission, A.1/B/B.1 gate, risk acceptance or release is implied. Historic notes above remain dated source evidence and are **superseded where they contradict D01–D06**.
