# Owner decision handoff — requester design approvals APP-01..APP-06

**Captured:** 2026-11-14, Asia/Ho_Chi_Minh. **Decision source:** explicit requesting user's statement in this conversation, author-recorded; real-world identity/authority and independent signature were **not externally verified**. **Scope:** six *design/policy directions* only, no per-host or per-risk technical acceptance.

**Repository:** `RyugaWork/spec2code`; existing branch `docs/plan-089-a1-readiness`; **input SHA:** `8e51a830a4851884a5117e5d4cd992688e8eda37`; **output SHA:** the single commit containing this handoff; fetch and read back actual branch HEAD after publishing. **Google stakeholder Draft:** document `1M3_2tNUxOXci83pcpPCzBkxwvRvixeT7FYeGyIsFOa4`, tab `t.0`, subsection 36.4, read-back revision `AHj4eMTdxz9faEGekJ6K64QZYAAiN9gm_lw3-e2Elr9Xb-C-P8vgw4DW7ruh8vbFAyA5AGE6eUmsE15P_0A919N0k01i_-voOs5l4QH1Yw`.

| Requester decision | Captured status | Non-approval boundary |
| --- | --- | --- |
| APP-01 business scope BRD/F43..64 | DESIGN_DIRECTION_APPROVED | Per-BR measurable AC, exact Git/Google parity and 44 test outcomes pending |
| APP-02 architecture + Spec Kit/optional adapters | DESIGN_DIRECTION_APPROVED | Detailed ADR/host/provider/version acceptance pending |
| APP-03 Manual/Safe Auto/Sandbox/Full Auto sandbox-only policy | POLICY_APPROVED | No running permission, no YOLO/OS bypass, no CLI/MCP enablement |
| APP-04 P0 treatment-before-danger policy | POLICY_APPROVED | Every open P0 and residual remain OPEN/UNKNOWN without tests and explicit acceptance |
| APP-05 A→A.1→B→B.1, STOP/RESUME, review and RTM | PROCESS_DESIGN_APPROVED | A1-VAL-01..09 formal NOT_RUN, B unauthorized, B.1 not run |
| APP-06 stable supported technology + official style + overrides | POLICY_APPROVED | No selected runtime version/actual migration/override/test authorized |

**Canonical register:** `/.agents/.documents/systemSpecificationPlan.md`, section APP-20261114; subordinate references in master SRS, architecture, risk, RTM, validation, technology policy, document governance and plans. No new feature identifiers, no per-ADR signature, no risk score changes, no runtime code/config/CI or host execution.

**Post-commit check:** confirm expected fast-forward parent, changed files all Markdown, correct APP-01..06 table, source/Google revision and all A.1/P0/B/B.1 boundary text. If branch has moved, STOP, reconcile and never force-update. Earlier `.agents/.handoffs/a1-author-preflight-20261114.md` remains a historical author-only report, not retrospectively approved. PR #10 remains Draft and unmerged unless separately authorized.

## A1 source-provenance erratum (2026-11-14)

Original user statement in this chat: **“duyệt hết đi”** after a four-group approval checklist. The six APP items are a document-author mapping and conservative interpretation, **not literal six separately given approvals**. An earlier canonical passage misquoted the requester; the current [canonical register](../.documents/systemSpecificationPlan.md#app-20261114--owner-requester-design-approvals-app-01app-06-scope-limited) now corrects it. Google Draft 36.4 received the corresponding single-paragraph correction, verified at revision `AHj4eMSKkbKTc9Zi1U5aJD5rk8h3Wr1Feq5a3PffqRhb_JMd-unznzxEfoJkKG4KQTOEK2I5SWHHOp91UOVnGCMONc3Wd4i5pdVnAD76ig`. The prior handoff is historical; this erratum supersedes only its quotation/authority representation.

The source comparison is in [document governance](../.documents/.documentGovernance.md#a1-src-20261114--gitgoogle-brd-semantic-screening-and-provenance-correction). Formal reviewer, security host authority and AC signatures are still absent; no P0 waived, no A1_PASS and no B permission.
