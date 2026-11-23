# Web v1.0 — A-Closure owner review and independent A.1 decision packet

Date: 2026-11-23. **OWNER_ACTION_REQUIRED — DESIGN ONLY; NOTHING SIGNED.** Evidence input Git `c0201acaf0639b271cdaba3110894298556d86d6` on `docs/plan-089-a1-readiness`; [A-Closure source/findings](webV1AClosureEvidence20261123.md), [64-F + 27-BR reverse trace](webV1AClosureFeatureReverseMatrix20261123.md), [21-case oracle worksheet](webV1AClosureWebTestOracleDesign20261123.md), [52-risk overlay](webV1RiskApplicability.md) and [AGM-01..17](webV1AgentsIntegrationMatrix.md). Source revisions will change after this document commit; the displayed SHA identifies the *observed author input*, **not** a frozen A.1 baseline.

## 1. Proposed design decisions to approve or revise

| Approval ID | Specific proposed choice | Alternatives / hard constraint | Current state |
| --- | --- | --- | --- |
| U-01 / DEC-WEB-01 | V1 Web human-directed read/spec/plan/risk/trace/test design, conditional permissioned GitHub read or offline bounded ZIP/Markdown/paste fallback; read-only Spec Kit v1.4.3 mapping; narrow real-authorization agent-executed AGENTS write path | No default repo write, native CLI, CI, MCP, OS sandbox claim; unsupported source/provider must BLOCK | OWNER_PENDING |
| U-02 / DEC-WEB-02/03 | Keep developer Markdown source `.source/profiles/web/`; release visible `spec2code-web-v1.0.0/` ZIP. Reuse `docs/plan-089-a1-readiness` for **proposed** later B commits after A.1 plus distinct B authorization; Git integrator reviews PR #8–#11/main before exact A.1 freeze/integration | Main has an unintegrated `.gitignore` two-line commit; PR #11 is draft/dirty and must not be auto-merged. A.1 freeze SHA not yet selected | OWNER_PENDING |
| U-03 | Name real Product, Architecture, QA, Security/Host and Git/Release authorities. One solo maintainer may cover multiple accountable owner roles. Independent A.1/B.1 reviewer must be a **different real reviewer**, not the document author or sequential AI personas | No reviewer => A.1/B.1 remain NOT_RUN/BLOCKED; no AI signature | OWNER_PENDING |
| U-04 / DEC-WEB-04 | Approve applicability of 21 designed Web cases (including 6 AGENTS cases) and 7 proposed groups, 100% applicable mandatory deterministic cases+security-negative variants PASS with actual evidence. Approve source pair Git + Google BRD Draft v1.5 revision and material semantic resolutions | Existing `R>99.99%` remains governing until Product+QA explicitly defines scoped metric method/exception and updates canonical rules. BR-007/008 need REFERENCE_ONLY or owner-approved additional Web assertions | OWNER_PENDING |
| U-05 | Approve mode-by-mode RM-001 classification: Web upload/read-only and truly remote connector AGENTS write may exclude S2C Windows local Path Guard when proven; local Windows agent writing host files **does not exclude RM-001** and remains blocked pending actual hostile OS containment tests | Never close/downgrade RM-001 global P0/20 via Web scope decision; other applicable P0 blockers still veto release | OWNER_PENDING |
| U-06 / DEC-WEB-06 | Approve declarative AGM-01..17, new/adopt/upgrade with three-way merge, exact path-grant capability, one-writer ref lease, idempotence, rollback and readback; external AI agent performs authorized host changes, S2C only supplies matrix/content | Without provider authorization/tools, output proposed diff/hand-off only; no implicit Git commit/push/merge/deploy right | OWNER_PENDING |

**Reviewer options for each:** `ACCEPT | REVISE | REJECT | DEFER`, with explicit source SHA/revision, role/identity, rationale, exact scope, accepted alternatives and effective permissions. A short "duyệt tất cả" may approve **design direction** if scoped and authenticated but never signs independent A.1, grants real host file writes, accepts critical risk without evidence or authorizes B/release.

## 2. The three hard decisions and six role assignments

### D-01 — Actual independent reviewer (BLOCKER)

- Product Owner: **UNASSIGNED** (GitHub handle or accountable person, role and decision method required).
- Architecture Owner: **UNASSIGNED** (may be same person if legitimately delegated).
- QA Owner: **UNASSIGNED** (owns test groups/metric denominator and evidence).
- Security/Host Owner: **UNASSIGNED** (signs RM-001 scope per provider and actual OS host permissions).
- Git/Release Owner: **UNASSIGNED** (owns PR #8–#11, `main` integration, release target).
- Independent A.1/B.1 Reviewer: **UNASSIGNED — HARD BLOCKER** (different real accountable reviewer from the author; must inspect exact source revision, risks and evidence).

The connected GitHub account/profile, previous commit author and a model persona cannot by themselves establish the requesting user's legal/organizational review authority. The owner must confirm any role assignment. If solo maintained, appoint an external collaborator; do not replace them with a second model pass. The independent reviewer may document a FAIL/BLOCKED and request revisions; no false PASS.

### D-02 — RM-001 release applicability (BLOCKER)

| Mode the owner may select for V1 | Proposed RM-001 treatment | Required evidence / owner decision |
| --- | --- | --- |
| A. GPT Web using supplied ZIP/pasted Markdown; no host mutation | Local Windows race outside this execution path; global P0 remains OPEN | Demonstrate no delegated local execution; approve no-write/secret/prompt-injection controls |
| B. GPT Web with real authorized remote GitHub **AGENTS-only** writes | Candidate exclusion of S2C *local* Windows Path Guard **only if** operation remains a verified remote API path | Exact provider write/readback permission, expected file SHA, paths, stale/conflicting denial, independent no-effect observations |
| C. Codex/other agent writing local Windows project | RM-001 applicable; blocked | Independently verified guest/OS isolation, junction/reparse/TOCTOU triggers, protected outside-root canary, no privilege leak |
| D. Local agent on Linux/macOS or unverified platform | Separate threat model and host controls required | Real OS/symlink/mount containment, permission and rollback evidence, security acceptance |

The Security Owner must decide **which modes are supported**. Unsupported modes cannot be declared safe by naming a Markdown rule.

### D-03 — Git + Google authoritative baseline and quality policy (BLOCKER)

- Exact examined Git input: `c0201acaf0639b271cdaba3110894298556d86d6`; **not frozen**. PR #10 current HEAD after author commit must be re-read for A.1. Main's sole unique change adds `.gitignore`; InitialVersion_v0 has a unique merge commit but no unique file delta; PR #11 remains a separate findings branch with seven touched files and dirty mergeability. Approve target and whether to integrate only after independent review or before A.1 on a new signed source snapshot.
- Google BRD is a connected **Draft v1.5** with 27 BR IDs. Read-observed revision: `AHj4eMTQo-4II6DrQF5kSGoY8OxDNISChHco-PFSx_OgzuUuEWu4R2qAsiNmlioUDwDF-cYLmUq__B8TxyeB5iOzSa8tL5uDM_9Rqh0Npw`. It has **not** been accepted or byte/semantically reconciled. Product Owner must review differences, especially seven-stage vs nine-stage vs five-machine phase terminology and future-engine wording for AST/RBAC/drift/multiagent, and authorize a versioned immutable Git-linked snapshot/reference. Do not automatically copy an entire external Google Doc into a public repository.
- Upstream Spec Kit initial proposed reference: tag `v1.4.3`, resolved commit `980b3d027f4bd7958c35f97f618d854b41320e3f`. This author checked upstream files/feature pointer docs; formal supported-host/preset schema remains QA/Architecture pending.
- Proposed quality gate: all applicable mandatory **21 canonical Web cases** plus approved subvariants PASS; strict negative cases PASS and zero applicable open P0. The inherited `R>99.99%` requires approved denominator, representative fixtures or an explicit **canonically recorded** Web-profile exception, not an author-level quiet waiver. BR-007/008 manual reference-only applicability needs Product+QA review.

## 3. Independent A.1 source-freeze protocol (preparation, NOT_RUN)

1. Resolve decisions U-01..06, assign reviewers and supported provider/host modes; approve exact BR/AC and per-risk applicability. Record `ACCEPT/REVISE/REJECT` evidence with identity and date.
2. Re-run PR/main/source-drift inventory and ensure all **material** REV-090 owner/finding decisions are resolved or disclosed; reconcile the Google revision/source snapshot without rewriting the draft automatically.
3. Freeze **one exact** Git SHA as `A1_REVIEW_BASELINE_SHA` **only after** final author changes and source alignment. Bind approved Google revision+snapshot hash, upstream Spec Kit commit, test contract, 52-risk row dispositions and reviewer identity to that SHA. If file/source drifts, mark affected evidence STALE and select/review a new baseline.
4. Independent reviewer must evaluate `A1-VAL-01..09` with criterion-specific observations, real reviewer identity/dissent and no blocking applicable risk. Author's preflight/role-lens simulation is NOT independent validation.
5. An actual A.1 PASS permits the owner to consider a **separate** Phase B implementation scope decision. A.1 alone is not B permission. B implementation, observed tests, independent B.1 and Release remain future separate gates.

## 4. Fast owner response template (design decisions, not gate bypass)

```text
Reviewed author report SHA: [exact commit as displayed on GitHub]
U-01: ACCEPT / REVISE / REJECT — supported Web capability + provider/offline fallback:
U-02: ACCEPT / REVISE / REJECT — branch/source strategy and visible package:
U-03: Product=[handle], Architecture=[handle], QA=[handle], Security/Host=[handle], Git/Release=[handle], Independent A.1 reviewer=[different handle]
U-04: ACCEPT / REVISE / REJECT — BR-007/008 disposition, Web metric and Google revision/snapshot:
U-05: ACCEPT / REVISE / REJECT — supported mode(s) A/B/C/D, RM-001 evidence/owner:
U-06: ACCEPT / REVISE / REJECT — allowed AGENTS target path(s), responsible AI agent/provider and grant limits:
Decision role / date:
Material changes or explicit objections:
```

If the user only answers some items, record only those specific decisions; others remain `OWNER_PENDING`. No partial response can be generalized to host security approval, independent review or Git release authority.

## 5. Author work completion record (not product acceptance)

`WEB-001`: source/PR/main/InitialVersion inventory → **A_AUTHOR_DOC_DONE_VERIFIED** after Git commit/readback.

`WEB-002`: 10 REV-090 owner disposition and no silent PR merge → **A_AUTHOR_DOC_DONE_VERIFIED**, outstanding owner actions remain open independently.

`WEB-003`: all 64 F rows with existing source state, Web scope and reverse direct task/test association, explicit gaps → **A_AUTHOR_DOC_DONE_VERIFIED**, individual semantic mappings still need Product/QA approval.

`WEB-004/005`: **OWNER_PENDING / A1_NOT_RUN / B_NOT_AUTHORIZED**, never marked done by this packet. `WEB-006..030` actual profile, tests, acceptance and release remain `PLANNED/NOT_RUN`. [A.1 preparation](webV1A1DesignReviewPacket.md) is an input for the *named independent reviewer*, not a signed report.

## 6. Requester review receipt — narrowed outstanding approvals (2026-11-23)

The [actual requester disposition](webV1RequesterConditionalDecisions20261123.md) has arrived after this packet's initial draft. Treat its U-01 and U-05 scope decisions as **requester-approved design direction**, U-02/U-04/U-06 as **conditional**, and U-03 as **model-accepted/roles unassigned**. This section supersedes the packet's earlier status of *no requester review*, not the independent owner/security/QA signatures. The five remaining decisions are: (a) multiple GitHub+ZIP source precedence; (b) PR #8–11/main target strategy and one eventual B branch (PR #10 presently 175 commits/135 files vs PR #9 base); (c) five named accountable roles + real independent reviewer; (d) versioned BRD authority, BR-007/008 treatment, R>99.99% Web metric; (e) remote AGENTS provider/path/security validation. `UPGRADE_MANAGED` conflict behavior is now explicitly specified BLOCKED/diff-only/no repeated unchanged retries, without host write permission. A.1 and Phase B remain blocked.
