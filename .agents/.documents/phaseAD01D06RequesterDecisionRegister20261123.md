# D01–D06 — Requester-approved Phase A design decisions (source-bound)

**Authority:** explicit requester answer in current conversation on 2026-11-23, after [27-BR briefing](phaseABrdSemanticReconciliation20261123.md), recorded against Git `01a96a28534fa4f32b11800ba64061bd1c4201ef` on `s2c/PhaseA`. This is **requester-level scope/design consent**, not an independent human A.1 reviewer signature, QA execution evidence, host permission to write, security P0 acceptance, permission to start Phase B, or release approval.

## Decision register

| Decision | Subject | Requester status | Binding design choice | Still needed |
| --- | --- | --- | --- | --- |
| D01 | SOURCE_OF_TRUTH | APPROVED_BY_REQUESTER_DESIGN | Git owns all current BRD, requirements, AC, architecture, AGENTS, RTM, tests, risks and release decisions. Google full source archived, historical only. | Do not auto-sync back to Google or require Google revision for new work. Conflicting untrusted uploads still STOP. |
| D02 | BR_001_016_WEB_COVERAGE | APPROVED_BY_REQUESTER_DESIGN | 16 separate Web AC and test pairs, WEB-AC/TC-22..37, positive+negative each. BR-007/008 mandatory Web design checks. | 37 total AC/TC; QA must approve fixtures and execute, not claim native/runtime behavior. |
| D03 | REVIEWER_SCOPE | APPROVED_BY_REQUESTER_DESIGN | BR-017..021 design requirements accepted; independent human A.1 remains mandatory. | Autonomous multi-agent fleet deferred and unverified; persona simulation is not independent acceptance. |
| D04 | ROADMAP_SCOPE | APPROVED_BY_REQUESTER_DESIGN | BR-022..027 retained as future roadmap, not mandatory Web V1 implementation. | No silent deletion; feature IDs/risks retained. Future BR/AC acceptance may require new authorization. |
| D05 | WEB_ACCEPTANCE_POLICY | APPROVED_BY_REQUESTER_DESIGN | Every applicable mandatory Web AC and required P/N variant must have actual PASS, 100% numerator/denominator for approved scope. | R>99.99% reliability and >95% scoped line/branch coverage measurement/exception await QA/Product governance; no release waiver; P0 veto. |
| D06 | WEB_PROVIDER_SCOPE | APPROVED_BY_REQUESTER_DESIGN | GPT Web read/upload/ZIP/paste and separately granted remote GitHub API AGENTS.md-only create/adopt/upgrade. | No local OS writes, no default code/CI/PR edits or unapproved remote host write. Provider grant/expected SHA/readback proof required. |

## Single-source hierarchy (D01)

1. **One normative Git master**: [`.agents/.spec.md`](../.spec.md), [canonical RTM](../.traceMatrix.md), [feature register](../.features.md), [risk matrix](../.riskMatrix.md), [task ledger](../.plans.md), [Web AC](webV1AcceptanceAndTraceability.md) and [Web TC](../.workflow/testingAndDelivery.md), in the **same Git branch/approved SHA**. No second living Google authority.
2. **Full Google historical source imported**: [Gemini-era 475-paragraph/two-table original snapshot](legacyGoogleBrdSourceArchive20261123.md), with exact Google revision; retained as *historical reference*, no mandatory future two-way synchronization. Its older statements are not automatically current Git requirements.
3. **Preexisting Google↔Git comparison** [BR-001..027](phaseABrdSemanticReconciliation20261123.md) is historical audit evidence only. D01 supersedes the earlier *proposed dual-source business signoff rule*. Later Git changes rely on Git SHA, actual requester/owner authorization and reviewed diff, not Google document updates.
4. **Untrusted uploads/ZIP remain separate** provenance: if their content conflicts with authorized Git inputs in an affected task, report `SOURCE_CONFLICT`, prepare diff, do not overwrite or silently give uploaded data higher authority.

## BR and release scope (D02–D06)

- **D02:** [16-BR per-case register](phaseAD02BrDedicatedWebCoverage20261123.md) creates 16 additional independent Web AC/TC IDs, `WEB-AC-22..37` and `WEB-TC-22..37`. Old 21 remain distinct; current totals **37 + 37**. Each mandatory P/N variant requires observed acceptance and evidence; **all 37 NOT_RUN**.
- **D03:** BR-017..021 full design retained, auto reviewer workforce deferred from V1; manual review rules remain, human A.1 independent reviewer still needed.
- **D04:** BR-022..027 retained, roadmap not V1 release obligations. Future planning requires risk/AC/owner gates when promoted.
- **D05:** 100% PASS of applicable mandatory Web AC/test scenarios is **requester-approved criterion**, not proof from documentation. `R>99.99%` and `>95%` require formal measurement/denominator/waiver decision before any promotion, never silent cancellation. All applicable P0 security blockers remain vetoes.
- **D06:** only `WEB_UPLOAD_READ` and separately approved `WEB_REMOTE_GITHUB_AGENTS_WRITE`; a model with only a read provider produces a diff/handoff and `NOT_APPLIED`. Actual external host write requires path grant, expected-SHA and readback, A.1 + scoped B before profile implementation, and observable no-write negative tests.

## Deferred independent gates

- Exact reviewed Git SHA for A.1 is **not frozen** merely by this commit. A1-VAL-01..09 independent actual results `NOT_RUN`; Phase B `NOT_AUTHORIZED`; B.1 `NOT_RUN`.
- Risk applicability RM-001..052 still awaits named Security/Host owners; RM-001 global P0 **4 × 5 = 20 OPEN**, residual unknown.
- Code/runtime or package implementation is **not authorized** by these design choices; real host/security negative oracles remain unexecuted.
- Git PR #8–#11 remain a separate Git Owner administrative queue; no merge to main, force push or branch deletion implied.

## Approved design versus unapproved gate distinctions

`REQUESTER_APPROVED_DESIGN` ≠ `PRODUCT_AC_RUNTIME_VERIFIED` ≠ `INDEPENDENT_A1_PASS` ≠ `PHASE_B_GRANTED` ≠ `RELEASED`. Each needs its own evidence or human decision with exact source SHA and owner.
