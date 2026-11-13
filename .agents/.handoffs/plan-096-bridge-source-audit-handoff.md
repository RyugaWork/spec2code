# PLAN-096 — Spec Kit bridge source-contract audit handoff

> **2026-11-13 / Asia/Ho_Chi_Minh.** Active branch `docs/plan-089-a1-readiness`, existing Draft PR #10. Starting source SHA `72920032a892b8a60c74fbdf2b62847fb5fa771d`; the commit that creates this file will have its own new SHA, which must be retrieved before the next review. GitHub main branch/host code is unchanged. No branch creation, merge or release.
>
> **Execution honesty:** source audit on real GitHub blobs + local Python **standard-library** smoke only. The local tool container has no network access to clone S2C; **`speckit_bridge.py` was NOT executed**, bundled Path Guard/Scope IO were not mocked as a replacement test, native Spec Kit CLI was NOT_RUN. Independent A.1 NOT_RUN, B NOT_AUTHORIZED, B.1 NOT_RUN.

## Completed durable work

- [Bridge source audit and future negative test plan](../.documents/specKitBridgeSourceAudit096.md) details `SK96-01` non-`specs/` directory acceptance potential, `SK96-02` duplicate pointer keys, `SK96-03` zero/whitespace artifact handling and `SK96-04` duplicate task-ID integrity.
- [Feature acceptance cases](../../specs/001-s2c-speckit-integration/checklists/integrationAcceptance.md) add **four separate unrun** `SK96-NEG-01..04`, not counted as extra successful tests. Global [RTM Section N](../.traceMatrix.md) maps exact feature/REQ/negative test IDs, [risk Section 16](../.riskMatrix.md) records SK-R08/09 candidates without numerical confidence claims, and [feature plan](../../specs/001-s2c-speckit-integration/plan.md) documents approval-gated remediation.
- Supporting Python standard-library probe *actually run in a temporary directory* confirmed duplicate-key last-wins, 0-byte `is_file()` truth and duplicate regex matches. This is not equivalent to real S2C bridge behavior because full guard/source wasn't executed.
- Existing PLAN-095 result **remains exactly four scoped Web/static PASS out of 24**, 20 NOT_RUN; now four additional planned negative bridge scenarios, all NOT_RUN. No independent host security evidence.

## Key decisions and sequencing

1. Owner defines strict `specs/<id>` namespace or a justified explicit alternate directory allowance (including environment override compatibility).
2. Owner defines duplicate-key rejection, empty vs whitespace content semantics, and duplicate task behavior in the read-only bridge without adding human permission semantics.
3. Obtain actual independent A.1 on exact current source and separately authorized B for Python source, config and regression tests; until then do not modify `.source/scripts` or `.source/tests`.
4. In an actual safe checkout with installed real guard dependencies, run seven existing tests plus `SK96-NEG-01..04`; record OS/git SHA/stdout/stderr/exit and outside sentinel hashes. Native Spec Kit init remains a distinct approved pilot and cannot be inferred from this.
5. Retain original RM scores and independent B.1/merge/release gates; preserve old PLAN-090..095 audit history.

**STOP:** Only documentation and GitHub-derived audit artifacts persist on the existing branch. Need a network-capable authorized S2C checkout for test execution, and owner decisions for behavior. On RESUME refresh exact branch SHA, feature pointer, Google BRD revision, Constitution/AGENTS and task/approval state. No S2C Workflow Guard session was opened or closed.
