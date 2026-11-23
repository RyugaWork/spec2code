# Web v1.0 — source-grounded reverse requirement / feature / task / test map (A author proposal)

Date: 2026-11-23. Input SHA `c0201acaf0639b271cdaba3110894298556d86d6`, branch `docs/plan-089-a1-readiness`. **A_AUTHOR_TRACE_PREFLIGHT / OWNER_PENDING / 0 WEB TESTS EXECUTED**. This is a **reverse trace view** derived from canonical [F01..F64 scope classification](webV1PreflightAndCapabilityMatrix.md), [RTM](../.traceMatrix.md), [WEB-001..030 task aliases](../.plans.md) and [WEB-TC-01..21 canonical cases](../.workflow/testingAndDelivery.md). It is not a second normative requirements/test ledger or a claim that task-alias co-occurrence proves an implemented behavior.

## 1. Audit semantics

- Feature source and disposition are observed from the pinned preflight; each existing F ID appears once. `WEB_MANUAL` / `CONDITIONAL_READ_MAPPING` mean **design proposals**, not installed features.
- Each `WEB task alias` is parsed only from the existing canonical task's alias/trace column; explicit `Fnn..mm` ranges expand to IDs. `WEB-003` is the 64-feature scope audit itself and is not counted as an implementation mapping for every feature.
- `WEB-TC` links below are **indirect task-level associations** (test mentions a task that references the feature) and are deliberately labeled `PROPOSED_ASSOCIATION`; they **do not** prove a feature-specific assertion or PASS. The reviewer must verify semantics before AC authority. A task with no direct test may still have a separate governance decision oracle rather than a missing runtime test.
- `NO_DIRECT_REQ_ROW` / `NO_DIRECT_WEB_TASK` are explicit gaps or out-of-scope references, not fabricated mappings. A deferred/dropped feature with a task alias is never promoted into V1 implementation scope.

## 2. 64-feature reverse trace

| F ID | Existing source state | Proposed Web disposition | Canonical REQ or BR anchor | Direct WEB task alias(es) | Indirect planned Web test association | Meaning |
| --- | --- | --- | --- | --- | --- | --- |
| F01 | IMPLEMENTED_SOURCE | WEB_MANUAL | S2C-REQ-001 | WEB-006, WEB-007, WEB-022 | WEB-TC-01, WEB-TC-03, WEB-TC-04, WEB-TC-05, WEB-TC-06, WEB-TC-08, WEB-TC-09 | Proposed manual/read-only profile scope (owner pending) |
| F02 | IMPLEMENTED_SOURCE | WEB_MANUAL | S2C-REQ-002 | WEB-010, WEB-022 | WEB-TC-01, WEB-TC-03, WEB-TC-04, WEB-TC-05, WEB-TC-06, WEB-TC-08, WEB-TC-09 | Proposed manual/read-only profile scope (owner pending) |
| F03 | IMPLEMENTED_SOURCE | WEB_MANUAL | S2C-REQ-003 | WEB-010, WEB-022 | WEB-TC-01, WEB-TC-03, WEB-TC-04, WEB-TC-05, WEB-TC-06, WEB-TC-08, WEB-TC-09 | Proposed manual/read-only profile scope (owner pending) |
| F04 | IMPLEMENTED_SOURCE | RUNTIME_EXCLUDED | S2C-REQ-004 | WEB-008 | WEB-TC-02, WEB-TC-05, WEB-TC-13, WEB-TC-14, WEB-TC-17, WEB-TC-19, WEB-TC-21 | EXCLUDED runtime; listed tasks only refer to policy/version boundaries |
| F05 | IMPLEMENTED_SOURCE | WEB_MANUAL | S2C-REQ-005 | WEB-009, WEB-015 | WEB-TC-05, WEB-TC-08, WEB-TC-09, WEB-TC-10, WEB-TC-11 | Proposed manual/read-only profile scope (owner pending) |
| F06 | IMPLEMENTED_SOURCE | WEB_MANUAL | S2C-REQ-006 | WEB-015, WEB-017, WEB-024 | WEB-TC-09, WEB-TC-10, WEB-TC-11, WEB-TC-12, WEB-TC-15, WEB-TC-18, WEB-TC-20 | Proposed manual/read-only profile scope (owner pending) |
| F07 | IMPLEMENTED_SOURCE | CONDITIONAL_READ_MAPPING | S2C-REQ-007 | WEB-019, WEB-023 | WEB-TC-02, WEB-TC-07, WEB-TC-16, WEB-TC-17, WEB-TC-19 | Proposed manual/read-only profile scope (owner pending) |
| F08 | IMPLEMENTED_SOURCE | REFERENCE_ONLY | S2C-REQ-008 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | REFERENCE contract only |
| F09 | IMPLEMENTED_SOURCE | RUNTIME_EXCLUDED | S2C-REQ-009 | WEB-008 | WEB-TC-02, WEB-TC-05, WEB-TC-13, WEB-TC-14, WEB-TC-17, WEB-TC-19, WEB-TC-21 | EXCLUDED runtime; listed tasks only refer to policy/version boundaries |
| F10 | IMPLEMENTED_SOURCE | DEFERRED_FUTURE | S2C-REQ-010 | WEB-008 | WEB-TC-02, WEB-TC-05, WEB-TC-13, WEB-TC-14, WEB-TC-17, WEB-TC-19, WEB-TC-21 | DEFERRED; task alias is not implemented scope |
| F11 | IN_PROGRESS | REFERENCE_ONLY | S2C-REQ-011 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | REFERENCE contract only |
| F12 | IN_PROGRESS | WEB_MANUAL | S2C-REQ-012 | WEB-011, WEB-012, WEB-013, WEB-014, WEB-021, WEB-026 | WEB-TC-04, WEB-TC-05, WEB-TC-18 | Proposed manual/read-only profile scope (owner pending) |
| F13 | IMPLEMENTED_SOURCE | RUNTIME_EXCLUDED | S2C-REQ-013 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | EXCLUDED runtime; listed tasks only refer to policy/version boundaries |
| F14 | PLANNED | REFERENCE_ONLY | S2C-REQ-014 | WEB-008, WEB-014, WEB-016, WEB-017, WEB-018, WEB-020, WEB-023 | WEB-TC-01, WEB-TC-02, WEB-TC-04, WEB-TC-05, WEB-TC-07, WEB-TC-12, WEB-TC-13, WEB-TC-14, WEB-TC-15, WEB-TC-16, WEB-TC-17, WEB-TC-18, WEB-TC-19, WEB-TC-20, WEB-TC-21 | REFERENCE contract only |
| F15 | IN_PROGRESS | RUNTIME_EXCLUDED | S2C-REQ-015 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | EXCLUDED runtime; listed tasks only refer to policy/version boundaries |
| F16 | IMPLEMENTED_SOURCE | REFERENCE_ONLY | S2C-REQ-016 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | REFERENCE contract only |
| F17 | PLANNED | WEB_MANUAL | S2C-REQ-017 | WEB-010, WEB-015, WEB-020, WEB-024 | WEB-TC-06, WEB-TC-09, WEB-TC-10, WEB-TC-11, WEB-TC-12, WEB-TC-15, WEB-TC-18, WEB-TC-20 | Proposed manual/read-only profile scope (owner pending) |
| F18 | PLANNED | WEB_MANUAL | S2C-REQ-018 | WEB-008 | WEB-TC-02, WEB-TC-05, WEB-TC-13, WEB-TC-14, WEB-TC-17, WEB-TC-19, WEB-TC-21 | Proposed manual/read-only profile scope (owner pending) |
| F19 | DEFERRED | DEFERRED_FUTURE | S2C-REQ-019 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F20 | PLANNED | DEFERRED_FUTURE | S2C-REQ-020 | WEB-029 | WEB-TC-15 | DEFERRED; task alias is not implemented scope |
| F21 | DROPPED | DROPPED | S2C-REQ-021 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DROPPED; negative/exclusion reference only |
| F22 | DROPPED | DROPPED | S2C-REQ-022 | WEB-019 | WEB-TC-07 | DROPPED; negative/exclusion reference only |
| F23 | DROPPED | DROPPED | S2C-REQ-023 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DROPPED; negative/exclusion reference only |
| F24 | IN_PROGRESS | REFERENCE_ONLY | S2C-REQ-024 | WEB-017, WEB-020 | WEB-TC-12, WEB-TC-15, WEB-TC-18, WEB-TC-20 | REFERENCE contract only |
| F25 | IN_PROGRESS | REFERENCE_ONLY | S2C-REQ-025 | WEB-016, WEB-021 | WEB-TC-01, WEB-TC-16, WEB-TC-21 | REFERENCE contract only |
| F26 | IN_PROGRESS | REFERENCE_ONLY | S2C-REQ-026 | WEB-017, WEB-018, WEB-020, WEB-024 | WEB-TC-02, WEB-TC-10, WEB-TC-11, WEB-TC-12, WEB-TC-15, WEB-TC-16, WEB-TC-17, WEB-TC-18, WEB-TC-19, WEB-TC-20 | REFERENCE contract only |
| F27 | IMPLEMENTED_SOURCE | WEB_MANUAL | S2C-REQ-027 | WEB-006, WEB-008, WEB-012, WEB-018, WEB-022 | WEB-TC-01, WEB-TC-02, WEB-TC-03, WEB-TC-04, WEB-TC-05, WEB-TC-06, WEB-TC-08, WEB-TC-09, WEB-TC-12, WEB-TC-13, WEB-TC-14, WEB-TC-16, WEB-TC-17, WEB-TC-18, WEB-TC-19, WEB-TC-21 | Proposed manual/read-only profile scope (owner pending) |
| F28 | IMPLEMENTED_SOURCE | WEB_MANUAL | S2C-REQ-028 | WEB-006, WEB-008, WEB-022 | WEB-TC-01, WEB-TC-02, WEB-TC-03, WEB-TC-04, WEB-TC-05, WEB-TC-06, WEB-TC-08, WEB-TC-09, WEB-TC-13, WEB-TC-14, WEB-TC-17, WEB-TC-19, WEB-TC-21 | Proposed manual/read-only profile scope (owner pending) |
| F29 | IMPLEMENTED_SOURCE | WEB_MANUAL | S2C-REQ-029 | WEB-006, WEB-010, WEB-022 | WEB-TC-01, WEB-TC-03, WEB-TC-04, WEB-TC-05, WEB-TC-06, WEB-TC-08, WEB-TC-09 | Proposed manual/read-only profile scope (owner pending) |
| F30 | IMPLEMENTED_SOURCE | WEB_MANUAL | S2C-REQ-030 | WEB-009, WEB-013, WEB-015, WEB-022 | WEB-TC-01, WEB-TC-03, WEB-TC-04, WEB-TC-05, WEB-TC-06, WEB-TC-08, WEB-TC-09, WEB-TC-10, WEB-TC-11 | Proposed manual/read-only profile scope (owner pending) |
| F31 | IN_PROGRESS | RUNTIME_EXCLUDED | S2C-REQ-031 | WEB-007, WEB-011, WEB-016, WEB-017, WEB-020, WEB-029 | WEB-TC-01, WEB-TC-03, WEB-TC-12, WEB-TC-15, WEB-TC-16, WEB-TC-18, WEB-TC-20, WEB-TC-21 | EXCLUDED runtime; listed tasks only refer to policy/version boundaries |
| F32 | IMPLEMENTED_SOURCE | WEB_MANUAL | S2C-REQ-032 | WEB-006, WEB-009, WEB-012 | WEB-TC-01, WEB-TC-04, WEB-TC-05, WEB-TC-08 | Proposed manual/read-only profile scope (owner pending) |
| F33 | IMPLEMENTED_SOURCE | WEB_MANUAL | S2C-REQ-033 | WEB-009, WEB-015 | WEB-TC-05, WEB-TC-08, WEB-TC-09, WEB-TC-10, WEB-TC-11 | Proposed manual/read-only profile scope (owner pending) |
| F34 | IMPLEMENTED_SOURCE | WEB_MANUAL | S2C-REQ-034 | WEB-009, WEB-015 | WEB-TC-05, WEB-TC-08, WEB-TC-09, WEB-TC-10, WEB-TC-11 | Proposed manual/read-only profile scope (owner pending) |
| F35 | IMPLEMENTED_SOURCE | WEB_MANUAL | S2C-REQ-035 | WEB-009, WEB-011, WEB-016, WEB-018, WEB-023 | WEB-TC-01, WEB-TC-02, WEB-TC-05, WEB-TC-07, WEB-TC-08, WEB-TC-12, WEB-TC-16, WEB-TC-17, WEB-TC-18, WEB-TC-19, WEB-TC-21 | Proposed manual/read-only profile scope (owner pending) |
| F36 | IN_PROGRESS | WEB_MANUAL | S2C-REQ-036 | WEB-005, WEB-009, WEB-014, WEB-020, WEB-026, WEB-028, WEB-029, WEB-030 | WEB-TC-04, WEB-TC-05, WEB-TC-08, WEB-TC-12, WEB-TC-15, WEB-TC-18, WEB-TC-20 | Proposed manual/read-only profile scope (owner pending) |
| F37 | IN_PROGRESS | WEB_MANUAL | S2C-REQ-037 | WEB-013, WEB-015, WEB-024 | WEB-TC-04, WEB-TC-09, WEB-TC-10, WEB-TC-11, WEB-TC-12, WEB-TC-15, WEB-TC-18, WEB-TC-20 | Proposed manual/read-only profile scope (owner pending) |
| F38 | DESIGN_PROPOSED | DEFERRED_FUTURE | NO_DIRECT_REQ_ROW | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F39 | DESIGN_PROPOSED | DEFERRED_FUTURE | NO_DIRECT_REQ_ROW | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F40 | DESIGN_PROPOSED | DEFERRED_FUTURE | NO_DIRECT_REQ_ROW | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F41 | DESIGN_PROPOSED | DEFERRED_FUTURE | NO_DIRECT_REQ_ROW | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F42 | DESIGN_PROPOSED | DEFERRED_FUTURE | NO_DIRECT_REQ_ROW | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F43 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-022 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F44 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-023 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F45 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-022 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F46 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-022 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F47 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-024 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F48 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-023,BR-027 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F49 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-025 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F50 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-025 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F51 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-025 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F52 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-024,BR-027 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F53 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-022,BR-026 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F54 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-025 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F55 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-022,BR-026 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F56 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-024,BR-026 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F57 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-022,BR-024 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F58 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-023,BR-027 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F59 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-026 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F60 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-026 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F61 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-024,BR-027 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F62 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-023 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F63 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-026 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |
| F64 | DESIGN_PROPOSED | DEFERRED_FUTURE | BR-023,BR-027 | NO_DIRECT_WEB_TASK | NO_DIRECT_WEB_TEST | DEFERRED; task alias is not implemented scope |

## 3. BR-001..027 Web-applicability candidates and acceptance gaps

The canonical [business requirements](../.spec.md) remain authoritative for their words and owners. These are **Web profile applicability suggestions**, not BR approval. The actual Google stakeholder BRD is still Draft and has no signed semantic parity.

| Existing BR | Proposed v1 applicability | Candidate existing Web TC(s) | Scope boundary and missing approval |
| --- | --- | --- | --- |
| BR-001 | SPLIT | WEB-TC-08, WEB-TC-19, WEB-TC-21 | Local OS Path Guard excluded; authority denied-write behavior is Web-visible |
| BR-002 | WEB_APPLIES | WEB-TC-02, WEB-TC-17, WEB-TC-19 | Host root/nested AGENTS ownership |
| BR-003 | WEB_APPLIES | WEB-TC-04, WEB-TC-08 | Manual stages and no unauthorized B promotion |
| BR-004 | WEB_APPLIES | WEB-TC-08, WEB-TC-09 | Separate A.1/B.1 and real evidence |
| BR-005 | WEB_APPLIES | WEB-TC-04, WEB-TC-07, WEB-TC-09 | Bidirectional trace without fabricated status |
| BR-006 | WEB_APPLIES | WEB-TC-09, WEB-TC-11 | Risk/evidence and source drift |
| BR-007 | REFERENCE_ONLY | NO_DIRECT_WEB_TEST | Risk grouping may be handled manually; owner must decide whether dedicated Web oracle is mandatory |
| BR-008 | REFERENCE_ONLY | NO_DIRECT_WEB_TEST | Research provenance manually referenced; owner must decide whether dedicated Web oracle is mandatory |
| BR-009 | WEB_APPLIES | WEB-TC-05, WEB-TC-08 | Prioritize blocker and refuse unsafe scope |
| BR-010 | WEB_APPLIES | WEB-TC-10, WEB-TC-11 | STOP/RESUME/manual checkpoint |
| BR-011 | WEB_APPLIES | WEB-TC-06, WEB-TC-13, WEB-TC-14, WEB-TC-21 | Context, privacy and untrusted document |
| BR-012 | CONDITIONAL_READ | WEB-TC-07 | Pinned upstream Spec Kit read-only mapping |
| BR-013 | WEB_APPLIES | WEB-TC-01, WEB-TC-07, WEB-TC-18 | Version/compatibility and reviewed override |
| BR-014 | WEB_APPLIES | WEB-TC-02, WEB-TC-05, WEB-TC-17 | Owner-preserving documentation |
| BR-015 | SPLIT | WEB-TC-12, WEB-TC-15, WEB-TC-16, WEB-TC-18, WEB-TC-20 | Web manifest and AGENTS migration only; full OS install excluded |
| BR-016 | WEB_APPLIES | WEB-TC-01, WEB-TC-09, WEB-TC-15 | Evidence and release receipt; authority still pending |
| BR-017 | DEFERRED_FUTURE | NO_DIRECT_WEB_TEST | Worker allocation/review fleet excluded from v1 |
| BR-018 | DEFERRED_FUTURE | NO_DIRECT_WEB_TEST | Isolated worker execution excluded |
| BR-019 | DEFERRED_FUTURE | NO_DIRECT_WEB_TEST | Automated synthesis service excluded |
| BR-020 | DEFERRED_FUTURE | NO_DIRECT_WEB_TEST | Multiworker review telemetry excluded; manual evidence rules reused |
| BR-021 | DEFERRED_FUTURE | NO_DIRECT_WEB_TEST | Review-worker service acceptance excluded |
| BR-022 | DEFERRED_FUTURE | NO_DIRECT_WEB_TEST | Advanced source/contract automation deferred |
| BR-023 | DEFERRED_FUTURE | NO_DIRECT_WEB_TEST | Runtime guard/cleanup extensions deferred |
| BR-024 | DEFERRED_FUTURE | NO_DIRECT_WEB_TEST | Advanced DBA/reviewer automated quality deferred |
| BR-025 | DEFERRED_FUTURE | NO_DIRECT_WEB_TEST | SLM/budget engine deferred; manual context retained |
| BR-026 | DEFERRED_FUTURE | NO_DIRECT_WEB_TEST | Cloud/schema deployment pipeline deferred |
| BR-027 | DEFERRED_FUTURE | NO_DIRECT_WEB_TEST | Self-evolution/protected core automation deferred |

**Reverse gaps requiring explicit product/QA consideration:** BR-007 and BR-008 have useful manual reference content but no directly designed Web test oracle. Accept `REFERENCE_ONLY` for v1 or approve a scoped fixture/assertion to an existing canonical case; do not silently claim full behavior acceptance. BR-017..027 are outside the initial Web product boundary (even where manual principles are reused) and retain their original broad system requirements/status. BR-001 and BR-015 are **SPLIT**: only the stated Web surface is proposed, not full local/runtime security and installer coverage.

## 4. AGM integration linkage and owner gates

[AGM-01..17](webV1AgentsIntegrationMatrix.md) maps to the six additional existing tests `WEB-TC-16..21` and task aliases WEB-008/011/016..020/023..025. Every AGM row has at least one canonical Web test **association**, but actual agent write/readback, remote-vs-local scope and root/nested policy are not yet observed. V1 scope includes an **agent-executed host AGENTS integration with real authorized tools**, not an automatic S2C installer.

The canonical test suite has exactly 21 distinct IDs and 21 draft `WEB-AC` IDs, linked 1:1. 30 WEB task IDs remain unchanged. Existing 52 RM IDs remain under their original global risk register; the separate [52-risk applicability overlay](webV1RiskApplicability.md) remains 35 WEB_APPLIES / 12 SPLIT / 5 RUNTIME_EXCLUDED proposals, all PENDING_OWNER. In particular RM-001 remains P0 OPEN and local Windows execution cannot inherit remote Web risk exclusion.

**Author evidence scope:** 64/64 IDs and direct F→task alias→case join **checked in this document**. Approval of individual BR/AC, all feature-level behavioral oracles, independent A.1, B and release remain outstanding.
