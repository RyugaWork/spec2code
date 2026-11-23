# Web v1.0 — Product-owner decision and delegated task packet (draft)

Date: 2026-11-23. Based on source d7fed7bb7d6d791f0c62f4315a66a729bb5f52ea on branch docs/plan-089-a1-readiness. **DECISION_DRAFT / NO_SIGNOFF**. This document records recommendations for an authorized requester; it cannot grant its own approval, mark A.1 PASS, accept residual P0, authorize Phase B, or release a product. Parent design: [PLAN-116](markdownFirstReleasePlan.md). Evidence: [WEB-001..003 preflight](webV1PreflightAndCapabilityMatrix.md).

## Decision records requiring human authority

| ID | Proposed choice for owner consideration | Decision owner and evidence to return | Status |
| --- | --- | --- | --- |
| DEC-WEB-01 | Recommend strictly human-directed GPT Web Markdown read/review/spec/plan/risk/RTM/test-design/handoff. Conditional permitted GitHub reads or bounded uploaded snapshots; no default writes, CLI, OS shell, MCP, automated agents, CI, native Spec Kit or runtime safety claim. | Product Owner plus Security/Provider Owner: approved supported/excluded capability and data-sharing/synthetic fixture policy, exact source and real provider boundary. Reject/change recommendation explicitly if needed. | OWNER_PENDING |
| DEC-WEB-02 | Recommend immutable allowlisted Markdown Web package under .source/profiles/web/ and opt-in host-owned .agents/skills/spec-to-code-web/ and .agents/s2c-web/ mapping only after approval. Version product=1.0.0, schemaVersion=1 candidate; bundleVersion, ownership, compatibility and migration documented separately. Preserve existing AGENTS, Spec Kit and legacy state. | Architecture/Host Owner: approved package paths, conflict ownership, manifest/schema/version compatibility, host install and rollback contract. | OWNER_PENDING |
| DEC-WEB-03 | Recommend keep current docs/plan-089-a1-readiness branch for draft fixes, no new branch, no force push; select main as eventual release target only after reviewed integration of divergent unique main change and stacked PR #8..#11. No merge/tag now. | Git/Release Owner: exact target/ref and source, required reviews, resolution of PR #11, strategy for existing stacked drafts and release permissions. | OWNER_PENDING |
| DEC-WEB-04 | Recommend Web-specific BR/AC and mandatory group acceptance, independent negative tests for prompt injection/secret exposure/false write claims, explicit applicability decision for every RM-001..052 risk and strict no-applicable-P0 rule. A finite 15-case suite alone cannot establish an unrounded R >99.99% reliability estimate. | Product, QA and Security Owners: named roles, approved BR/AC, oracle, representative test denominator/method, provider/data authorization, residual risk decisions and evidence. | OWNER_PENDING |
| DEC-WEB-05 | Require independent Web-scope A1-VAL-01..09 on an exact approved source before product authoring; then separate Phase B implementation permission, actual B1-VAL-01..09 on candidate, and a distinct release approval. | Named independent Reviewer(s) plus Product/Host Owner; explicit evidence/report IDs and actual decisions for each gate. | OWNER_PENDING |

These are **five separate decision records**, not a request for the owner to blindly approve all items. A.1/B/B.1 and release approvals remain separate even if one person holds multiple accountable business roles; the document author cannot be the independent reviewer of their own work.

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

1. **U-01 Scope.** Accept, narrow or amend DEC-WEB-01 (Web Markdown read/plan/review/handoff only for stable 1.0; no Web write/CLI/automation by default). If changing, specify capabilities and permitted providers.
2. **U-02 Source and release target.** Choose eventual release target after conflict/stack review (recommended: main with reviewed integration, not immediate merge); name Git integrator/release owner.
3. **U-03 Ownership.** Identify accountable Product, Security/Host, Architecture, QA, independent A.1/B.1 Reviewer and Release authority, or mark a role UNASSIGNED and leave the relevant gate blocked.
4. **U-04 BR/AC and acceptance.** Accept/revise Web scope-to-requirement mapping, source-of-truth Git/Google treatment and case oracles, with actual QA method for mandatory groups.
5. **U-05 Security and evidence.** Approve data sharing/connector and synthetic fixtures; require every applicable P0 to be resolved before v1; authorize an independent review only when the evidence packet is ready. Do not construe U-01..04 as Phase B or release permission.

All decisions require identity/role, date, exact review SHA, scope, alternatives, explicit ACCEPT/REVISE/REJECT and evidence link. If missing, keep OWNER_PENDING and continue safe A-phase drafting.

## Next execution order

First obtain owner review on this packet and WEB-001..003 crosswalk; author remaining A-phase scope/risk/AC/ADR/checklist corrections; independent scoped A.1; separately authorized B; WEB-006..020 product files; WEB-021..025 actual QA; WEB-026..029 risk/release verification; WEB-030 release owner decision and one immutable reviewed release. Existing canonical [30-task ledger](../.plans.md) remains the sole task-status authority.
