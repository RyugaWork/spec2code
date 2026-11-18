# PLAN-111 — A.1 findings → P0 guards → return to A

**Date:** 2026-11-14 Asia/Ho_Chi_Minh. **Existing working branch:** `docs/plan-089-a1-readiness`; source input `7a951097d7239cdba3cd54315a86ea9ef423a4cb`; first P0 code/test commit `78c65b278fbd2ec384301c88abfdf6c84d388a29`; next consolidated fix+documentation commit is this file's publishing SHA. **Google stakeholder Draft:** `AHj4eMTpTE_OFxAkB4X-3MXvcz0WSTl4b6D-UptJB7WLJq2Xkac8kDoGH7gDEkqWIJfGQV9wVuMrfbmWlJAdFueAU_exvNrOc-0t5BIIZA` (previously read back). No Google text edit in PLAN-111. **Author:** one ChatGPT review/coding agent via GitHub connector. No local clone or terminal test was possible because remote Git DNS resolution failed. `independentReviewerCount=0`.

## A.1 author-preflight disposition (formal reviewer = NOT_RUN)

| Existing gate | Author finding | Formal result and remediation owner |
| --- | --- | --- |
| A1-VAL-01 source authority | 27 BR IDs identified in Git and Google Draft, no signed semantic equality | NOT_RUN; product/document owner A/P4 |
| A1-VAL-02 AC | BR-022..027 oracles drafted; exact thresholds and denominators pending | NOT_RUN; product/QA A/P4 |
| A1-VAL-03 RTM | Existing requirement/feature/test references including 42 BR, 44 feature, 12 MM test IDs; none represents executed AC | NOT_RUN; BA/QA A/P4 |
| A1-VAL-04 feature | Existing F43–F64 and ADR proposals, unresolved authorized host/provider interfaces | NOT_RUN; architect A/P5 |
| A1-VAL-05 architecture | Workflow/Path Guard candidate patches not yet end-to-end accepted, Windows race remains | NOT_RUN; architect/security A/P6 |
| A1-VAL-06 risk discovery | RM-001..005 and extended threat register retained | NOT_RUN; host/security A/P7 |
| A1-VAL-07 risk management | P0 remains open, no owner-signed residual and no real hostile host tests | NOT_RUN; security A/P8 |
| A1-VAL-08 handoff | Exact source SHAs, task mapping, test outcomes and rollback described here | NOT_RUN; maintainer A/P9 |
| A1-VAL-09 independent signoff | No authorized independent reviewer name/authority/signature | NOT_RUN; independent reviewer |

**A.1 aggregate:** `NOT_RUN / READINESS_BLOCKED`, never `A1_PASS`. Requester instructed targeted P0 source remediation; this was not interpreted as an independent reviewer signature or broad Phase B authorization.

## P0 implementation and first regression

- Existing Python source touched: `.source/scripts/workflow_guard.py` and `.source/scripts/path_guard.py`; tests: `.source/tests/test_workflow_guard.py`, `.source/tests/test_path_guard.py`. No new runtime subsystem, schema status, config version or branch.
- Workflow corrections: real scoped CLOSE, distinct plan/implement/verify/handoff policy operation, source/active feature fingerprint, fail-safe bounded source paths, scope-free status compatibility distinction.
- Path Guard correction: all Windows reparse flags checked statically, not proof of race safety.
- GitHub Actions at `78c65b27...`: Ubuntu 3.10/3.11/3.13 jobs reported `FAIL`, 132 tests / 1 failure / 4 skips on observed Linux job; failure `test_source_change_blocks_gates` due empty-scope global policy drift not blocked. Additional code patch in this follow-up commit corrects that. Windows jobs had not reached final conclusive status when this packet was authored. Exact-head CI of final commit requires readback.

## Return to A — active owner queue

1. **A/P4:** sign explicit source pair and BR/AC definitions, including BR-022..027 scope, exclusions and measurable denominators; update one canonical SRS/RTM.
2. **A/P6:** decide supported Windows/OneDrive/network root policy, OS/sandbox isolation for untrusted workers, native handle approach or explicitly reject unsafe writes. Determine real helper/process trust boundary.
3. **A/P7–P8:** preserve RM-001..005 L/I until real host adverse tests and risk-owner acceptance; repair high-scoring interactions without inventing residual reductions.
4. **A/P9:** obtain actual independent A1-VAL-01..09 report on the final Git+Google pair; hold merge, native Spec Kit/CLI execution, general B and B.1/release.

**Rollback:** revert the two PLAN-111 commits after reviewing exact diff and any intervening changes; do not reset other commits or delete host/handoff state. **Persistence:** this handoff was included in a GitHub commit via expected-head, non-force update; verify SHA and CI separately. **STOP state:** `A_REWORK_REQUIRED / INDEPENDENT_A1_NOT_RUN / WINDOWS_TOCTOU_OPEN / B1_NOT_RUN`.
