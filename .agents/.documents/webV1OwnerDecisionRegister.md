# Web v1.0 — Product-owner decision and delegated task packet (draft)

Date: 2026-11-23. Based on source d7fed7bb7d6d791f0c62f4315a66a729bb5f52ea on branch docs/plan-089-a1-readiness. **DECISION_DRAFT / NO_SIGNOFF**. This document records recommendations for an authorized requester; it cannot grant its own approval, mark A.1 PASS, accept residual P0, authorize Phase B, or release a product. Parent design: [PLAN-116](markdownFirstReleasePlan.md). Evidence: [WEB-001..003 preflight](webV1PreflightAndCapabilityMatrix.md).

## Decision records requiring human authority

| ID | Proposed choice for owner consideration | Decision owner and evidence to return | Status |
| --- | --- | --- | --- |
| DEC-WEB-01 | Recommend Markdown-first human-directed Web workflows, **plus a limited AI-agent-executed AGENTS.md integration/upgrade path when explicit host/path-specific write authorization and real write tools are present**. General repository writes, CLI/MCP/CI, autonomous workers, Git commit/merge and OS sandbox claims remain out of profile. | Product + Security/Provider Owner: exact supported scope, grants, permitted providers, data sharing and deny fallback. | REQUESTER_SCOPE_ACCEPTED; SOURCE_CONFLICT_RULE_PENDING; PROVIDER/ROLE_SIGNOFF_PENDING |
| DEC-WEB-02 | Markdown-only profile .source/profiles/web/, host-owned paths and separate version schema; **17-row AGENTS Integration Matrix** guides create/adopt/upgrade with old/current/new comparison, user-customized content preservation, idempotence and rollback. | Architecture/Host Owner: review matrix, version markers, ownership, effective host paths, approval and recovery. | CONDITIONAL_REQUESTER_ACCEPTANCE; HOST/VERSION/UPGRADE_REVIEW_PENDING |
| DEC-WEB-03 | Recommend keep current docs/plan-089-a1-readiness branch for draft fixes, no new branch, no force push; select main as eventual release target only after reviewed integration of divergent unique main change and stacked PR #8..#11. No merge/tag now. | Git/Release Owner: exact target/ref and source, required reviews, resolution of PR #11, strategy for existing stacked drafts and release permissions. | CONDITIONAL_REQUESTER_ACCEPTANCE; PR_INTEGRATION_AND_B_BRANCH_PENDING |
| DEC-WEB-04 | Web-specific BR/AC and mandatory group acceptance including **WEB-TC-16..21 for AGENTS integration**, 21 proposed tests total, explicit per-risk Web applicability and validated write/no-write boundary; finite tests cannot demonstrate R >99.99% without approved method. | Product/QA/Security Owners: consented fixtures, ACs, measurement method, secrets policy, risk disposition. | CONDITIONAL_REQUESTER_ACCEPTANCE; BRD/BR007-008/KPI_QA_PENDING |
| DEC-WEB-05 | Require independent Web-scope A1-VAL-01..09 on an exact approved source before product authoring; then separate Phase B implementation permission, actual B1-VAL-01..09 on candidate, and a distinct release approval. | Named independent Reviewer(s) plus Product/Host Owner; explicit evidence/report IDs and actual decisions for each gate. | REVIEW_MODEL_ACCEPTED; REAL_INDEPENDENT_REVIEWER_UNASSIGNED |
| DEC-WEB-06 | Approve **agent-executed AGENTS.md create/adopt/upgrade** based only on declarative AGM-01..17, with actual path grants, old/current/new merge, readback, idempotent repeat, denied-write fallback and no incidental Git rights. | Product/Architecture/Host/Security: supported host/provider and exact approved paths; independent review of negative tests. | CONDITIONAL_REQUESTER_ACCEPTANCE; CONFLICT_NO_WRITE_RULE_DOCUMENTED; REAL_WRITE_GRANT_PENDING |

These are **six separate decision records**, not a request for the owner to blindly approve all items. A.1/B/B.1 and release approvals remain separate even if one person holds multiple accountable business roles; the document author cannot be the independent reviewer of their own work.

## What AI can do next without replacing the owner

| Existing task | AI-draftable next deliverable | Evidence / STOP condition |
| --- | --- | --- |
| WEB-001 | Recheck exact HEAD, branch/PR inventory and link/navigation after each documentation commit | Exact SHA and observed GitHub results, local host state UNKNOWN |
| WEB-002 | Maintain source-grounded REV-090-01..10 crosswalk and document corrections | No invented finding closure or external reviewer |
| WEB-003 | Maintain F01..64 Web-specific matrix and reverse trace mapping proposal | No feature promotion or implied release |
| WEB-004 | Draft risk applicability, exclusions, data-handling and owner decision options | Owner signature and applicability remain PENDING |
| WEB-005 | Prepare immutable A.1 review packet, architecture/version/ownership ADR, approval checklist | STOP before WEB-006..020 unless independent A.1 and explicit B scope observed |
| WEB-021 (design-only preflight) | Review Markdown IDs, relative links, package allowlist and stale claims as a preflight | Cannot mark final package static QA complete before package exists |
| WEB-026 (design-only template) | Draft final RTM/test/risk reconciliation checklist | Cannot claim final test PASS or B.1 on unimplemented product |

## User action queue (answer each, delegate drafting if desired)

1. **U-01 Scope.** Accept, narrow or amend DEC-WEB-01 (Web Markdown core plus bounded agent-executed AGENTS integration with real scoped permission; no **default** general Web write/CLI/automation). If changing, specify capabilities and permitted providers.
2. **U-02 Source and release target.** Choose eventual release target after conflict/stack review (recommended: main with reviewed integration, not immediate merge); name Git integrator/release owner.
3. **U-03 Ownership.** Identify accountable Product, Security/Host, Architecture, QA, independent A.1/B.1 Reviewer and Release authority, or mark a role UNASSIGNED and leave the relevant gate blocked.
4. **U-04 BR/AC and acceptance.** Accept/revise Web scope-to-requirement mapping, source-of-truth Git/Google treatment and case oracles, with actual QA method for mandatory groups.
5. **U-05 Security and evidence.** Approve data sharing/connector and synthetic fixtures; require every applicable P0 to be resolved before v1; authorize an independent review only when the evidence packet is ready. Do not construe U-01..04 as Phase B or release permission.

All decisions require identity/role, date, exact review SHA, scope, alternatives, explicit ACCEPT/REVISE/REJECT and evidence link. If missing, keep OWNER_PENDING and continue safe A-phase drafting.

## Next execution order

First obtain owner review on this packet and WEB-001..003 crosswalk; author remaining A-phase scope/risk/AC/ADR/checklist corrections; independent scoped A.1; separately authorized B; WEB-006..020 product files; WEB-021..025 actual QA; WEB-026..029 risk/release verification; WEB-030 release owner decision and one immutable reviewed release. Existing canonical [30-task ledger](../.plans.md) remains the sole task-status authority.

## Subsequent A-phase drafts (2026-11-23; no owner decision implied)

- [Full Markdown source/path preflight](webV1StaticMarkdownAudit20261123.md): 125 tracked Markdown source blobs and limited relative file link coverage; archive exceptions and limitations recorded.
- [52-risk applicability overlay](webV1RiskApplicability.md): every RM-001..052 has a proposed Web applicability, reason and owner; all PENDING_OWNER.
- [15-case AC and group crosswalk](webV1AcceptanceAndTraceability.md): proposed oracles only, no actual Web test execution.
- [Independent A.1 preparation packet](webV1A1DesignReviewPacket.md): nine-gate source/checklist and ADR recommendations, no reviewer signoff or Phase B permission.

These materials are supplemental design evidence, not signed decisions. The original DEC-WEB-01..05 status above remains OWNER_PENDING.

## Amendment — AI-agent-executed AGENTS.md integration (design request, not approval)

The requester identified an essential missing V1.0 use case: **create or update existing host AGENTS.md through AI agents using a declarative integration matrix**, including subsequent version upgrades. The previous five proposed decisions were written for manual-only host AGENTS adoption; **they must be re-reviewed**, not retrospectively declared accepted. [Full 17-clause matrix and safe protocol](webV1AgentsIntegrationMatrix.md).

**U-06 decision required:** approve or revise DEC-WEB-06: (a) exact AGENTS paths/new-file authority, (b) which real AI-agent provider can write them, (c) pre-approved bounded changes versus per-diff approval, (d) host/nested rule conflict authority, (e) backup/readback/rollback and owner signoff. If any is unknown, return a read-only matrix+diff/handoff. This design direction is **not permission to modify a user's real host repository**.

The canonical proposed Web suite now includes **WEB-TC-01..21**, all NOT_RUN. A.1/B/B.1 and RM-001 remain unchanged.

## Gemini review response — owner approvals remain pending (2026-11-23)

[Detailed U-01..U-06 disposition and three mandatory decisions](webV1GeminiReviewDisposition20261123.md) now clarify all six design questions without assigning identities or signing gates: 
- U-01: offline uploaded ZIP/Markdown/paste fallback and v1.4.3 Spec Kit read-only structure candidate (actual compatibility untested).
- U-02: visible ZIP root, existing-branch-by-default B **only after** A.1/B authorization, and a single **not-yet-frozen** A.1 SHA after PR #8..11/main reconciliation.
- U-03: explicitly named roles and a **non-author actual independent reviewer**; solo ownership without that person remains BLOCKED.
- U-04: 21 designed Web test cases, proposal for all applicable mandatory Web/negative cases PASS; inherited R>99.99% metric remains governed until owner-approved scope-specific amendment. Google BRD must be bound to an exact versioned approved Git snapshot/reference.
- U-05: RM-001 applicability separates remote read/connector write from locally executed Windows/other-host agents; global P0 remains OPEN.
- U-06: agent-executed AGENTS updates require actual scoped grants, matrix and three-way diff/readback; no broad git/runtime permission.

**Requester design-level dispositions are now recorded per DEC-WEB-01..06; formal accountable owner/provider/security/QA roles and applicable signatures remain pending as indicated.** This addendum is NOT an A.1 PASS or Phase B authorization. Owner source and reviewer names are intentionally unfilled rather than fabricated.

## A-Closure owner review (2026-11-23)

The precise **six U-item approval form and three blockers** are in [A-Closure Approval Packet](webV1AClosureApprovalPacket20261123.md). Source [Git/Google/PR review](webV1AClosureEvidence20261123.md) and [64-F/27-BR trace](webV1AClosureFeatureReverseMatrix20261123.md) are author-verifiable evidence, not an owner decision. `DEC-WEB-01..06` remain `OWNER_PENDING`. Until identities, supported provider/OS modes, 52-risk decisions, KPI treatment and immutable BRD/branch baseline are approved, there is no actual independent A.1, no B authorization and no release.

## Requester response after A-Closure — explicit approvals versus hard conditions (2026-11-23)

[Precise six-item recorded response and owner clarifications](webV1RequesterConditionalDecisions20261123.md) supersede the earlier blanket statement that all six designs were entirely unreviewed, **without** converting this chat response to a formal A.1/risk/provider signature. U-01 scope accepted; U-05 only `WEB_UPLOAD_READ` and authorized `WEB_REMOTE_GITHUB_AGENTS_WRITE` scope accepted; U-02/04/06 conditional; U-03 model accepted but named roles/reviewer pending. Existing `DEC-WEB-05` independent gate is unchanged. For simultaneous GitHub+ZIP sources, conflict STOP is the author-proposed rule awaiting owner confirmation. For `UPGRADE_MANAGED`, any host customization conflict => **BLOCKED/no write/no retry with unchanged inputs**. The 175-commit/135-file PR #10 author comparison triggers a proposed single separate Phase B branch *after* A.1/B authorization, not a new branch now. See the [source evidence](webV1AClosureEvidence20261123.md).
