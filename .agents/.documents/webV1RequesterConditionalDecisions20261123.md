# Web V1.0 — Requester review receipt and conditional design decisions (23 November 2026)

**Decision evidence input:** explicit requester feedback in the current conversation, reviewed against author Git SHA `13a55f37d32c59e132d6c996983afbf133a5bc19`. **Status: PARTIAL_DESIGN_CONSENT / GATE_APPROVAL_PENDING**. This file is an evidence-linked record of *what the requester said*, plus **separately labeled author-proposed clarifications**; it is **not** independently authenticated Product/QA/Security signatures, a write grant, an A.1/B/B.1 PASS or a release. Do not infer the requester's GitHub account handle, reviewer identity or risk acceptance.

Related source: [canonical DEC-WEB-01..06](webV1OwnerDecisionRegister.md), [review packet](webV1AClosureApprovalPacket20261123.md), [AGENTS integration](webV1AgentsIntegrationMatrix.md), [risk](webV1RiskApplicability.md), [A.1 handoff](webV1A1DesignReviewPacket.md).

## 1. Requester disposition — exactly as supported by the response

| Item / linked decision | Explicit requester disposition | What is now fixed at **design-direction level** | What remains an unresolved approval |
| --- | --- | --- | --- |
| **U-01 / DEC-WEB-01** | **PHÊ DUYỆT** | Markdown-first V1, GitHub read/offline ZIP-files-paste/UNKNOWN fallback; pinned Spec Kit v1.4.3 structure at commit `980b3d027f4bd7958c35f97f618d854b41320e3f` | Formalize concurrent Git+ZIP source conflict/precedence rule, product/provider capability evidence, actual owners |
| **U-02 / DEC-WEB-02,03** | **PHÊ DUYỆT CÓ ĐIỀU KIỆN** | Developer-only hidden `.source/`, visible user ZIP, four independent version identities | Reconcile PR #8–#11 and main unique commit, freeze one A.1 SHA, decide distinct Phase B branch from observed oversized current branch |
| **U-03 / DEC-WEB-05 role requirement** | **PHÊ DUYỆT MÔ HÌNH, KHÓA DANH SÁCH PHỤ TRÁCH** | Real accountable roles; no self-signed AI validation; genuinely different human external/peer reviewer required | Named/verified handles of 5 accountable roles and one real independent reviewer; actual reviewer workflow and acceptance |
| **U-04 / DEC-WEB-04** | **PHÊ DUYỆT CÓ ĐIỀU KIỆN** | 21 Web cases/100% of applicable mandatory cases proposed; Google BRD three-level workflow semantic split | Pick technical Git vs stakeholder Google authority after semantic reconciliation; BR-007/008 reference-only vs added assertions; explicit R>99.99% policy amendment, actual QA approval |
| **U-05 / DEC-WEB-01,04,06** | **PHÊ DUYỆT PHẠM VI MÔI TRƯỜNG V1** | Support **only** (1) GPT Web reading uploaded/pasted Markdown/ZIP and (2) separately authorized **remote GitHub API AGENTS.md writes**. Codex/other agent local writes on Windows/Linux/macOS are **outside V1.0** | Security Owner must still attest that remote mode has no delegated local OS IO, assess remote permissions/TOCTOU-equivalent concurrency and other applicable risks; global RM-001 OPEN P0/20 |
| **U-06 / DEC-WEB-06** | **PHÊ DUYỆT CÓ ĐIỀU KIỆN** | Declarative 17-row AGM; authorized agent applies safe changes, with write/readback/version-last | Author requires **conflict-loop kill switch** below; real target-path grants, provider capability, security/negative-test proof and owner identity still pending |

Only U-01 and the two-environment **product scope** of U-05 have unconditional *requester-level* acceptance. Conditional design consent is **not** full owner signoff. U-03 role-model acceptance is not a reviewer appointment. U-06 conflict behavior below captures the requester's condition, but no actual host permission is granted.

## 2. U-01 — concurrent GitHub connector and ZIP/files/paste

**Author-proposed deterministic decision protocol; requester asked to lock this but has not independently selected a precedence rule:**

1. **Identify authority before transport:** approved versioned repository `.agents/.spec.md` is the candidate technical specification master; the Google BRD is a stakeholder review surface, not yet signed normative; uploaded ZIP is evidence/snapshot, not a newer authoritative version simply because uploaded later. Actual owner-approved requirement revisions outrank any technical convenience. Do not treat "live" or "newest" as a business approval.
2. **Pin each actual source:** GitHub owner/repo/branch/commit/file/blob SHA and read timestamp; ZIP filename, observed file list, observed byte SHA-256 (if calculable), declared origin/ref and provenance status `DECLARED_UNVERIFIED` until independently matched. Redact secret paths/content.
3. **Same logical path:** compare actual bytes/content and normalize only with a documented approved method. Matching hashes or verified equivalent content may be joined with `CONSISTENT`; conflicting bytes/IDs/versions => `SOURCE_CONFLICT`, show path, Git commit/blob ref, ZIP observed hash and short bounded redacted diff, and STOP only dependent tasks.
4. **Non-overlapping paths:** each may be cited **with distinct provenance**. Never infer that absence in a partial upload means absence in Git. Do not silently merge duplicate requirements from different sources.
5. **Priority/fallback:** when source conflict cannot be reconciled, **neither connector nor upload auto-wins**. For unaffected Git-native facts use the actually fetched pinned repository; for expressly user-selected offline analysis, the upload can be used as `UPLOAD_ONLY_UNVERIFIED_GIT`, without implying sync/authority. Resolve overlapping normative content only on explicit owner version selection with a recorded decision; then create a change request, not automatic overwrite.
6. **Resume and upgrades:** if Git HEAD, uploaded file hash or approved BRD revision changes, invalidate affected comparisons/approvals and rerun only affected matrix rows. No source auto-refresh claim for ChatGPT upload/Project.
7. **Negative-oracle proposal:** extend existing `WEB-TC-03` with **variant C (both Git and ZIP, same path SHA/content mismatch)** expecting conflict report and no wrong-source write. Preserve the **21 unique test IDs** and all NOT_RUN.

Suggested owner default: **versioned Git technical master for exact repository files + Google BRD owner-approved business revision only after snapshot/semantic signoff; conflict blocks overlap**, not a hard global preference of Git over arbitrary stakeholder approvals.

## 3. U-02 — branch/PR strategy based on the observed large PR

**Observed at `13a55f37d32c59e132d6c996983afbf133a5bc19`:** PR #10 head is on `docs/plan-089-a1-readiness` and its comparison to its stacked PR #9 base (`53575d26fc3a50f5b0edcd256f76326161de6f9d`) contains **175 commits and 135 changed files**. This already meets the reviewability/size trigger; the previous "same branch for B by default" is superseded as an **author recommendation**, not as an approved Git branch decision.

| Source | Proposed action, without performing a merge | Remaining authority |
| --- | --- | --- |
| PR #8 | Retain draft baseline history and review integration dependencies and actual next target | Git integrator |
| PR #9 | Retain as base of current PR #10, not squashed/closed without integrator plan | Git integrator |
| PR #10 | Keep **Phase A documentation and decision authoring** here; no Phase B implementation on giant docs PR by default | Product/Git integrator |
| PR #11 | Treat its 10 findings and 3 unique commits/7 changed paths as **review inputs**; [REV-090 crosswalk](webV1AClosureEvidence20261123.md) already records proposals. Reconcile each unique useful delta against current source, cherry-pick/edit only approved distinct content in a bounded commit, avoid wholesale merge of a stale conflict branch; closing superseded PR requires owner/maintainer action | Reviewer/Git integrator |
| `main` | Review one unique `.gitignore` commit; integrate after explicit choice of final target, with lease and CI; never rewrite protected/shared history | Git integrator |
| `spec2code/InitialVersion_v0` | Keep older merge lineage; no gratuitous branch or duplicate merge | Git integrator |

**Proposed Phase B branch rule:** following approved BRD/risk/owner dispositions, source/PR resolution and actual independent A.1, create **exactly one Phase B implementation branch** from the **approved integrated baseline containing the A.1 source** when separate scoped B authority is granted. If main has already obtained the reviewed design, branch from that main SHA; otherwise explicitly select an owner-reviewed integration base that preserves the frozen A.1 source, never an unrelated old main. Existing docs branch remains the immutable *referenced* A.1 source at its SHA; A.1 finding fixes need rerun if they materially change approved scope. **No new branch now.**

A branch-split review is mandatory if any condition holds: (a) size/change count prevents a bounded review, as it currently does (175/135); (b) code implementation has a different permission/safety gate than Phase A; (c) branch protection or stacked PR lineage conflicts with merge/CI; or (d) reviewer requests separate code-only diff. These are triggers to review/approve **one** branch, not permission to open parallel branches or force push.

**A.1 baseline is not frozen:** it must bind one final Git commit SHA and one approved Google BRD revision/snapshot **after** PR/main findings and owner edits. The original author SHA is historical evidence, not the baseline.

## 4. U-03 — roles and independent reviewer without invented identities

A solo maintainer may hold the five accountable roles Product, Architecture, QA, Security/Host and Git/Release **after explicit name/handle/authority declaration**; current names remain `UNASSIGNED`. Independent reviewer must be a **different actual person** with access to the exact source and evidence. Option 1: external qualified reviewer. Option 2: peer review by a separate named contributor (possibly external to the repo, with delegated review authority), with conflict-of-interest/independence documented. Both are *human-review workflows*, not a waiver. If neither is available, `A1-VAL-09 / B1-VAL` stay `BLOCKED/NOT_RUN`.

Owner must supply 5 roles' person/handle(s), one independent reviewer or explicit `NOT_YET_APPOINTED`, delegation evidence, and exact decision refs. Nothing in the request appoints `RyugaWork`, a model persona, or a previous commit author to these roles.

## 5. U-04 — BRD source, BR-007/008 and quality conditions

**Author recommendation for owner consideration, not signed source parity:**

- Technical Git `.agents/.spec.md` is the **current working technical master**; Google `BRD_Spec2Code` remains stakeholder Draft v1.5 with observed revision `AHj4eMTQo-4II6DrQF5kSGoY8OxDNISChHco-PFSx_OgzuUuEWu4R2qAsiNmlioUDwDF-cYLmUq__B8TxyeB5iOzSa8tL5uDM_9Rqh0Npw`. Normative business authority is the **owner-approved versioned BRD/AC** after semantic reconciliation, not whichever file was read last. If discrepancies exist, log `DRIFT/OWNER_REQUIRED`; do not assume all 27 matching IDs mean matching text. Bind approved source snapshot or immutable reference to a later Git SHA with hash/provenance/permission before A.1.
- **Recommended minimal V1:** BR-007 (risk-grouping semantics) and BR-008 (research-supported mitigations) remain **REFERENCE_ONLY** in V1.0 rather than claiming standalone automated capabilities; standard manual risk/provenance safety floor remains in scope. Alternative for owner: mandate explicit negative variants on existing Web cases, with reviewed added oracles and **no increase in 21 IDs**. Owner must choose one disposition for each BR.
- Proposed Web release criterion is all applicable 21 canonical tests and every approved required subvariant PASS with evidence; inherited `R>99.99%` cannot be deleted or claimed statistically proven from 21 tests. Product+QA must approve an explicit Web-specific measurement/exception and canonical governance update before release.

## 6. U-05 — scope-approved execution modes; security risks still pending

**Product-scope decision recorded from requester: V1.0 ONLY**
- `WEB_UPLOAD_READ`: ChatGPT Web reads expressly supplied ZIP/Markdown/files/paste; no local filesystem writes, CLI, native Spec Kit installer, CI or daemon.
- `WEB_REMOTE_GITHUB_AGENTS_WRITE`: eligible AI agent with verified GitHub remote API capability and separate target-path grant applies only approved root/nested `AGENTS.md` (or expressly scoped managed section) under expected-ref/blob lease, then readback/verify. **No generic code edit, commit/push/merge/deploy entitlement and no hidden local subprocess**.

**EXCLUDED FROM V1**: local Codex/agent host writes on Windows, Linux or macOS, any local path-guard bypass behavior or unverified OS execution. Local agents require their **own future security design and admission gate**.

**Scope acceptance is not RM-001 residual-risk acceptance.** Global RM-001 stays P0 `OPEN`, 4×5=20, with local Windows risks untested. Security Owner must verify that the supported remote provider really performs no delegated local IO, review Git API authorization/path/TOCTOU-equivalent stale-SHA and conflict/no-write tests, and dispose of all 52 risk overlays. A connector *exposing* a write API does not itself grant the right to invoke it on a host project.

## 7. U-06 — conflict kill switch for UPGRADE_MANAGED

The requester **explicitly requires**: whenever a version upgrade encounters a conflict with host-customized `AGENTS.md`, the AI returns only a bounded diff/recommendation and `BLOCKED`; it **must not edit the user's customized section**.

**Normative proposed algorithm for authorized executor** (declarative, no S2C runtime code):

1. Inspect exact old pristine managed section, currently installed host-customized AGENTS (including nested applicable scopes), new pristine proposal and verified path grants.
2. Compute a deterministic **conflict identity** using target path, old profile version, observed target blob hash, target new bundle hash and sorted overlapping clause IDs. Record input material identifiers but never leak secret text.
3. If the three-way merge reports an overlap, malformed/duplicate markers, unknown old pristine version, inconsistent nested policy, stale source/ref or an owner-modified clause, set `BLOCKED_CONFLICT / NO_WRITE`. Emit **proposed diff only**, owner choices, no writes to AGENTS files or version/manifest, and no partial application of the non-conflicting portion of that same approved batch.
4. **No autonomous retry loop on unchanged conflict identity.** Same inputs => return the existing conflict decision; do not re-prompt endlessly, regenerate a new "approved" version, rewrite user custom text, or escalate permission based on Markdown instructions. Re-evaluation is allowed **only** when the actual input/source hash/version changes or a real owner grants a documented conflict-specific resolution, followed by a fresh dry run and authority check. A changed model interpretation alone is not sufficient.
5. If a prior operation was partially committed before conflict was discovered, record `PARTIAL/STOP`, do not bump version, and propose a precise rollback **only for owned verified hunks** after checking for concurrent edits and relevant permissions. Never silently reset user-customized content.
6. After the **entire** conflict-free allowed batch passes independent readback, record the installed version **last**. Do not mark `APPLIED_VERIFIED` until observed readback and no duplicate marker.
7. Add required negative variants to existing cases: `WEB-TC-18` (custom overlap => conflict/no write), `WEB-TC-19` (denied path/repeated prompt => stable no-write) and `WEB-TC-20` (same fingerprint repeat/no duplicate; changed SHA requires new review). **21 original test IDs retained, all NOT_RUN.**

The host must still grant actual GitHub API write scope and select eligible paths/providers. "Approved design" is not authorization to write to someone's AGENTS.md.

## 8. Next reviewer decisions and stop conditions

Required user confirmations before A.1 freeze:
1. **Source precedence:** accept proposed `SOURCE_CONFLICT => STOP, versioned Git technical master, Google owner-approved business authority, ZIP as provenance-bearing snapshot` rule; specify any intentional alternative.
2. **Git integration and B branch:** accept no wholesale PR #11 merge; agree that the 175-commit/135-file current PR triggers a **single** Phase B branch after A.1 and separate permission, with owner-selected integration base.
3. **Roles:** name the five role handles (can be one named maintainer) and one actually independent peer/external reviewer; else gate blocked.
4. **Business source/test:** approve the exact Google revision/snapshot/semantic resolutions, choose BR-007 and BR-008 `REFERENCE_ONLY` or added test assertions, settle inherited reliability KPI with QA.
5. **Security/AGENTS:** name provider/path scope and accountable Security Owner, verify real supported remote API behavior; no independent host write evidence claimed.

**Unchanged gates:** PR stack and main not merged, no single frozen A.1 SHA, A1-VAL-01..09 NOT_RUN, 21 Web tests NOT_RUN, WEB-004/005 blocked pending owner approvals, Phase B NOT_AUTHORIZED, B.1 NOT_RUN, RM-001 P0 OPEN, no V1 release.


## 9. Additional source-verified U-02 review item: PR #11 semantic ID collision

[Detailed reconciliation](webV1Pr11CollisionReconciliation20261123.md) identifies the historical PR #11 F43..50 and RM-034..40 values as **different definitions** from this branch, plus PLAN-091/SRS 18 overlap. This confirms the requester's concern about PR #11 and strengthens the **NO_WHOLESALE_MERGE** recommendation, but **does not itself grant approval** to close, cherry-pick or rename historical identifiers. Git/Architecture/Security Owners must review PR11-C01..05 and main's unique `.gitignore` before one A.1 integration baseline. All previous conditional statuses and A.1/B hard gates remain.

## D01–D06 requester decision supersession (2026-11-23)

**Requester design decisions now recorded:** D01 = **Git alone normative**. Previous Google `BRD_Spec2Code` v1.5 is a *historical Gemini-era source*, imported in its entirety into Git as [source archive](legacyGoogleBrdSourceArchive20261123.md); **do not require future Google revision matching or treat Google as a second current business authority**. Source conflict checks still apply to other differing Git/ZIP/snapshot inputs. D02 = **all BR-001..016 receive individual dedicated Web AC and TC**: [16 pairs](phaseAD02BrDedicatedWebCoverage20261123.md); BR-007 and BR-008 are **not** REFERENCE_ONLY for Web acceptance. D03 = BR-017..021 accepted as architecture/requirements **design scope**, automated reviewer fleet deferred. D04 = BR-022..027 retained in roadmap, **not mandatory V1 implementation**. D05 = **100% PASS of applicable mandatory Web AC/test P/N variants** required for V1 release; inherited `R>99.99%` and BR-027 `>95%` scoped coverage await approved measurement/denominator rather than an invented waiver. D06 = read/upload in ChatGPT Web plus only **individually authorized remote GitHub API host AGENTS.md-only writes**; local OS/native agent writes excluded. Full dispositions: [decision register](phaseAD01D06RequesterDecisionRegister20261123.md).

**Current suite: 37 AC + 37 planned TC (21 baseline + 16 BR-dedicated), 37/37 NOT_RUN.** No actual host permission, A.1/B/B.1 gate, risk acceptance or release is implied. Historic notes above remain dated source evidence and are **superseded where they contradict D01–D06**.
