# S2C Phase A — Unified Integration & Traceability Matrix (source-bound)

**Status: AUTHOR_STATIC_MATRIX_VERIFIED / DESIGN_AND_OWNER_GATES_PENDING.** Source branch `s2c/PhaseA`, audit input SHA `4f3f22928673a9c80a2fa0bf9988f2daa1a9cfb4`, Git tree `223c576403dd5a357218f5732caa37665086b5b5`, 2026-11-23. This is a **derived audit snapshot**; normative wording and owners remain in [master SRS](../.spec.md), [canonical RTM](../.traceMatrix.md), [risk register](../.riskMatrix.md), [plans](../.plans.md), [Web feature scope](webV1AClosureFeatureReverseMatrix20261123.md), [QA cases](../.workflow/testingAndDelivery.md), [AC design](webV1AcceptanceAndTraceability.md) and [AGM](webV1AgentsIntegrationMatrix.md). No source/test status is promoted by this report.

> **Audit revision scope:** The original evidence inputs (`4f3f229...`, 2026-11-23) apply to the original 21-case snapshot. Requester D01–D06 later approved Git-only requirements and 16 additional dedicated BR-001..016 Web cases at input Git `01a96a28534fa4f32b11800ba64061bd1c4201ef`. This matrix now includes the **proposed revised 37-case source graph**; it does not claim that 37 tests ran on either earlier SHA. [D02 source/fixture detail](phaseAD02BrDedicatedWebCoverage20261123.md).

## 1. Matrix completeness and invariants

| Integration layer | Observed unique primary IDs | Static check | Remaining gate |
| --- | ---: | --- | --- |
| Feature scope | 64 F01..F64 | One row per ID, valid Web task/test references | Product architecture applicability not signed |
| Business requirement | 27 BR-001..027 | One Web disposition per ID | Git-only current authority; Google fully archived as historical source; requester D02 requires BR-001..016 separate AC/test |
| Web tasks | 30 WEB-001..030 | 30 unique, all dependencies exist, DAG no cycles | Only WEB-001..003 author documentation complete |
| Web acceptance | 37 WEB-AC-01..37 | 37 unique; one-to-one TC link (16 dedicated BR variants added) | QA must approve actual fixtures and execution denominator |
| Web tests | 37 WEB-TC-01..37 | 37 unique; every task ref resolves | All 37 NOT_RUN; not CI Python tests |
| Risks | 52 RM-001..052 | 52 unique, every related WEB-TC ID resolves | Every Web risk applicability PENDING_OWNER; RM-001 global P0 OPEN |
| AGENTS clauses | 17 AGM-01..17 | 17 unique, every related WEB-TC resolves | Real path/provider write grants and negative tests pending |
| Cross-collection links | All typed WEB-task/test references in these rows | No out-of-range references observed | Semantic sufficiency of all edges still owner/reviewer work |

**Scope breakdown (64 features):** WEB_MANUAL 18; CONDITIONAL_READ_MAPPING 1; REFERENCE_ONLY 7; RUNTIME_EXCLUDED 5; DEFERRED_FUTURE 30; DROPPED 3. **52 risk categories:** WEB_APPLIES 35; SPLIT 12; RUNTIME_EXCLUDED 5. These are draft classifications, not implementation or residual-risk acceptance.

## 2. Feature → requirement → Web task → planned test (64 rows)

| Feature | Observed source status | Web disposition | BR/REQ linkage | Web tasks | Web tests | Boundary |
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


## 3. Business requirement → proposed Web applicability (27 rows)

| BR | Proposed Web scope | Direct test / absence | Review reason |
| --- | --- | --- | --- |
| BR-001 | SPLIT | WEB-TC-08, WEB-TC-19, WEB-TC-21, WEB-TC-22 | Local OS Path Guard excluded; authority denied-write behavior is Web-visible |
| BR-002 | WEB_APPLIES | WEB-TC-02, WEB-TC-17, WEB-TC-19, WEB-TC-23 | Host root/nested AGENTS ownership |
| BR-003 | WEB_APPLIES | WEB-TC-04, WEB-TC-08, WEB-TC-24 | Manual stages and no unauthorized B promotion |
| BR-004 | WEB_APPLIES | WEB-TC-08, WEB-TC-09, WEB-TC-25 | Separate A.1/B.1 and real evidence |
| BR-005 | WEB_APPLIES | WEB-TC-04, WEB-TC-07, WEB-TC-09, WEB-TC-26 | Bidirectional trace without fabricated status |
| BR-006 | WEB_APPLIES | WEB-TC-09, WEB-TC-11, WEB-TC-27 | Risk/evidence and source drift |
| BR-007 | WEB_APPLIES | WEB-TC-28 | Manually verify risk-group causes and member IDs |
| BR-008 | WEB_APPLIES | WEB-TC-29 | Verify research provenance and unsupported claims |
| BR-009 | WEB_APPLIES | WEB-TC-05, WEB-TC-08, WEB-TC-30 | Prioritize blocker and refuse unsafe scope |
| BR-010 | WEB_APPLIES | WEB-TC-10, WEB-TC-11, WEB-TC-31 | STOP/RESUME/manual checkpoint |
| BR-011 | WEB_APPLIES | WEB-TC-06, WEB-TC-13, WEB-TC-14, WEB-TC-21, WEB-TC-32 | Context, privacy and untrusted document |
| BR-012 | CONDITIONAL_READ | WEB-TC-07, WEB-TC-33 | Pinned upstream Spec Kit read-only mapping |
| BR-013 | WEB_APPLIES | WEB-TC-01, WEB-TC-07, WEB-TC-18, WEB-TC-34 | Version/compatibility and reviewed override |
| BR-014 | WEB_APPLIES | WEB-TC-02, WEB-TC-05, WEB-TC-17, WEB-TC-35 | Owner-preserving documentation |
| BR-015 | SPLIT | WEB-TC-12, WEB-TC-15, WEB-TC-16, WEB-TC-18, WEB-TC-20, WEB-TC-36 | Web manifest and AGENTS migration only; full OS install excluded |
| BR-016 | WEB_APPLIES | WEB-TC-01, WEB-TC-09, WEB-TC-15, WEB-TC-37 | Evidence and release receipt; authority still pending |
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


**Requester D01/D02 resolution:** Git is the sole current BR/SRS authority; Google's complete historical content is archived in Git. BR-007/008 have dedicated Web AC/test cases. All BR-001..016 have 16 distinct Web P/N case pairs (22..37). Product/QA must still review actual executable fixture coverage; the first 21 cross-cutting cases remain unchanged.

## 4. Task dependency → accountable executor → phase/evidence (30 rows)

| Task | Depends on | Executor | Priority | Delivery scope | Observed status |
| --- | --- | --- | --- | --- | --- |
| WEB-001 | — | GPTWEB | P1 | Pin baseline, inventory all refs/PRs, distinguish remote from local state. | A_AUTHOR_DOC_DONE_VERIFIED (remote static; no owner/test/A.1 approval) |
| WEB-002 | WEB-001 | GPTWEB | P0 | Reconcile PR #11 REV-090-01..10 against current source; inspect unique main change and InitialVersion_v0 history without merging. | A_AUTHOR_DOC_DONE_VERIFIED (remote static; no owner/test/A.1 approval) |
| WEB-003 | WEB-001 | GPTWEB | P1 | Classify F01..F64 by Web manual, conditional, prototype/deferred or excluded. | A_AUTHOR_DOC_DONE_VERIFIED (remote static; no owner/test/A.1 approval) |
| WEB-004 | WEB-002, WEB-003 | Product + Security Owner | P0 | Approve precise Web-only supported scope, exclusions and per-risk applicability; freeze release baseline. | PLANNED / NOT_RUN |
| WEB-005 | WEB-004 | Architecture + Product Owner | P0 | Approve product/profile/schema version contract and artifact ownership; choose target branch/release policy. Prepare and obtain independent profile A.1 and separately explicit profile B scope before WEB-006..020 product authoring; if no approval remain blocked. | PLANNED / NOT_RUN |
| WEB-006 | WEB-005 | GPTWEB | P1 | Author portable Web SKILL entrypoint; include bounded start/read/stop behavior. | PLANNED / NOT_RUN |
| WEB-007 | WEB-006 | GPTWEB | P1 | Author bootstrap and Project Instructions import procedure with connector and upload fallback. | PLANNED / NOT_RUN |
| WEB-008 | WEB-006 | GPTWEB + Security Owner | P0 | Author authority, data classification, repository scope and prompt-injection rules. AGENTS integration authority and prompt-injection boundary must also pass WEB-TC-17/19/21. | PLANNED / NOT_RUN |
| WEB-009 | WEB-006 | GPTWEB | P0 | Map existing A/P1–P9, nine task stages, A.1/B/B.1 to manual operation and five machine phases without changing enums. | PLANNED / NOT_RUN |
| WEB-010 | WEB-008, WEB-009 | GPTWEB | P1 | Write minimal/balanced/deep context selection and safety floors. | PLANNED / NOT_RUN |
| WEB-011 | WEB-005 | GPTWEB | P1 | Create projectManifest template and release manifest design. Manifest/managed-section version identity is required for approved AGENTS upgrades, WEB-TC-18. | PLANNED / NOT_RUN |
| WEB-012 | WEB-009 | GPTWEB | P1 | Create specification and implementation plan templates with existing-document reuse. | PLANNED / NOT_RUN |
| WEB-013 | WEB-012 | GPTWEB | P1 | Define task ledger template, statuses, dependency and transition evidence. | PLANNED / NOT_RUN |
| WEB-014 | WEB-013 | GPTWEB | P1 | Create RTM and risk templates with forward/reverse links. | PLANNED / NOT_RUN |
| WEB-015 | WEB-013, WEB-014 | GPTWEB | P0 | Prepare test/review, STOP/RESUME, handoff and approval templates. | PLANNED / NOT_RUN |
| WEB-016 | WEB-007, WEB-015 | GPTWEB + Host Owner | P1 | Design fresh host install and separate distribution/state/host ownership. Include AGENTS NEW_ROOT creation by an external AI agent only with verified host/path-specific grants; WEB-TC-16/21. | PLANNED / NOT_RUN |
| WEB-017 | WEB-016 | GPTWEB + Host Owner | P0 | Design legacy v0.x adoption without touching existing runtime or history. Track old pristine/host customized/new S2C adopted guidance; never migrate unverified legacy AGENTS text, WEB-TC-18/20. | PLANNED / NOT_RUN |
| WEB-018 | WEB-016 | GPTWEB + Host Owner | P0 | Design adoption for project-owned/customized documents and state. Include host root/nested AGENTS adoption matrix and three-way non-destructive merge; WEB-TC-17/18/19. | PLANNED / NOT_RUN |
| WEB-019 | WEB-018 | GPTWEB + Spec Owner | P1 | Integrate Spec Kit existing Markdown artifacts; select active feature without executing native commands. | PLANNED / NOT_RUN |
| WEB-020 | WEB-017, WEB-018, WEB-019 | GPTWEB + Architecture Owner | P0 | Finalize install/upgrade/migration/backup/rollback contract and release/schema compatibility fixtures. Version/rollback contract also covers adopted AGENTS section with manifest-last, idempotence and stale ref checks; WEB-TC-18/20. | PLANNED / NOT_RUN |
| WEB-021 | WEB-020 | GPTWEB + QA | P1 | Static inventory/relative links, unique IDs, dependency graph, distribution allowlist and version text QA. | PLANNED / NOT_RUN |
| WEB-022 | WEB-021 | QA + Host Owner | P1 | Exercise fresh representative synthetic GPT Web project and ordinary read/plan tests. | PLANNED / NOT_RUN |
| WEB-023 | WEB-022 | QA + Host Owner | P1 | Exercise existing host with AGENTS/customized docs/Spec Kit Markdown. Host acceptance includes real authorized AGENTS create/adopt and nested preservation; WEB-TC-16/17/19. | PLANNED / NOT_RUN |
| WEB-024 | WEB-023 | QA + Host Owner | P0 | Exercise distinct-chat STOP/RESUME, drift, interrupted upgrade, conflict and restore. Verify AGENTS version three-way upgrade, repeat and interrupted recovery, WEB-TC-18/20. | PLANNED / NOT_RUN |
| WEB-025 | WEB-022, WEB-023, WEB-024 | Independent Security Reviewer | P0 | Adversarial Web review including untrusted source, secrets, false tool/approval claims and unauthorized writes. Security negative cases include unauthorized AGENTS write and prompt-injection claim, WEB-TC-19/21. | PLANNED / NOT_RUN |
| WEB-026 | WEB-025 | GPTWEB + QA | P1 | Reconcile requirements, traceability, risk and task results for exact release candidate. | PLANNED / NOT_RUN |
| WEB-027 | WEB-026 | Security + Product Owner | P0 | Record supported scope and residual risk decisions on exact candidate. | PLANNED / NOT_RUN |
| WEB-028 | WEB-027 | Independent Reviewer | P0 | Verify previously signed independent profile A.1 and explicit B scope; conduct independent profile B.1 on actual final deliverables. Source/design drift returns to A; do not retrospectively approve B. | PLANNED / NOT_RUN |
| WEB-029 | WEB-028 | Release Engineer | P1 | Prepare exact allowlisted Markdown payload, release notes, manifest, migration guide and checksums. | PLANNED / NOT_RUN |
| WEB-030 | WEB-029 | Release Owner + Integrator | P0 | Obtain explicit release approval and publish one reviewed immutable version/ref + release package. | PLANNED / NOT_RUN |


**Static dependency DAG:** 30 nodes, zero missing prerequisite task IDs and zero cycles. The dependency graph is not authorization: WEB-005 must still obtain independent A.1 and distinct B authorization before Web profile implementation.

## 5. Web acceptance → mandatory test → related task (37 rows after D02)

| Acceptance | Objective | Task references | Test ID | Test observed status | AC approval status |
| --- | --- | --- | --- | --- | --- |
| WEB-AC-01 | Identity and source binding | WEB-001, WEB-006, WEB-007, WEB-016 | WEB-TC-01 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-02 | Host AGENTS precedence | WEB-008, WEB-018, WEB-023 | WEB-TC-02 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-03 | Missing mandatory input | WEB-007, WEB-022 | WEB-TC-03 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-04 | Requirements and task structure | WEB-012, WEB-013, WEB-014, WEB-022 | WEB-TC-04 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-05 | Conflicting requirements | WEB-008, WEB-009, WEB-012, WEB-022 | WEB-TC-05 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-06 | Context safety floor | WEB-010, WEB-022 | WEB-TC-06 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-07 | Spec Kit ownership | WEB-019, WEB-023 | WEB-TC-07 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-08 | No implicit writes or gate approval | WEB-009, WEB-022, WEB-025 | WEB-TC-08 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-09 | Evidence-based test result | WEB-015, WEB-022, WEB-025 | WEB-TC-09 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-10 | STOP/RESUME provenance | WEB-015, WEB-024 | WEB-TC-10 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-11 | Source drift invalidation | WEB-015, WEB-024 | WEB-TC-11 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-12 | Three-way upgrade conflict | WEB-018, WEB-020, WEB-024 | WEB-TC-12 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-13 | Untrusted Markdown injection | WEB-008, WEB-025 | WEB-TC-13 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-14 | Canary and sensitive data | WEB-008, WEB-025 | WEB-TC-14 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-15 | Interrupted migration rollback | WEB-020, WEB-024, WEB-029 | WEB-TC-15 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-16 | New host AGENTS creation | WEB-016, WEB-018, WEB-023 | WEB-TC-16 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-17 | Existing/nested host AGENTS preservation | WEB-008, WEB-018, WEB-023 | WEB-TC-17 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-18 | S2C-adopted section version upgrade | WEB-011, WEB-017, WEB-018, WEB-020, WEB-024 | WEB-TC-18 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-19 | Conflict and denied AGENTS path | WEB-008, WEB-018, WEB-023, WEB-025 | WEB-TC-19 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-20 | Idempotence and source drift | WEB-017, WEB-020, WEB-024 | WEB-TC-20 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-21 | Provider unavailable / untrusted authority | WEB-008, WEB-016, WEB-025 | WEB-TC-21 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-22 | BR-001 dedicated Web acceptance | Refer to canonical BR-001 scoped task links | WEB-TC-22 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-23 | BR-002 dedicated Web acceptance | Refer to canonical BR-002 scoped task links | WEB-TC-23 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-24 | BR-003 dedicated Web acceptance | Refer to canonical BR-003 scoped task links | WEB-TC-24 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-25 | BR-004 dedicated Web acceptance | Refer to canonical BR-004 scoped task links | WEB-TC-25 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-26 | BR-005 dedicated Web acceptance | Refer to canonical BR-005 scoped task links | WEB-TC-26 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-27 | BR-006 dedicated Web acceptance | Refer to canonical BR-006 scoped task links | WEB-TC-27 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-28 | BR-007 dedicated Web acceptance | Refer to canonical BR-007 scoped task links | WEB-TC-28 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-29 | BR-008 dedicated Web acceptance | Refer to canonical BR-008 scoped task links | WEB-TC-29 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-30 | BR-009 dedicated Web acceptance | Refer to canonical BR-009 scoped task links | WEB-TC-30 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-31 | BR-010 dedicated Web acceptance | Refer to canonical BR-010 scoped task links | WEB-TC-31 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-32 | BR-011 dedicated Web acceptance | Refer to canonical BR-011 scoped task links | WEB-TC-32 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-33 | BR-012 dedicated Web acceptance | Refer to canonical BR-012 scoped task links | WEB-TC-33 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-34 | BR-013 dedicated Web acceptance | Refer to canonical BR-013 scoped task links | WEB-TC-34 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-35 | BR-014 dedicated Web acceptance | Refer to canonical BR-014 scoped task links | WEB-TC-35 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-36 | BR-015 dedicated Web acceptance | Refer to canonical BR-015 scoped task links | WEB-TC-36 | NOT_RUN | DRAFT / NOT_RUN |
| WEB-AC-37 | BR-016 dedicated Web acceptance | Refer to canonical BR-016 scoped task links | WEB-TC-37 | NOT_RUN | DRAFT / NOT_RUN |


**Required unresolved negative variants:** WEB-TC-03-C handles simultaneous GitHub+ZIP same-path content drift, with stop/no silent precedence; WEB-TC-18/19/20 handle customized AGENTS conflict no write, stable conflict identity/no loop and stale SHA. These refine existing IDs, not add tests. No WEB case was actually executed.

## 6. Global risk → Web applicability → negative test (52 rows)

| Risk | Web category | Web exposure/exception | Proposed owner | Web test links | Owner status |
| --- | --- | --- | --- | --- | --- |
| RM-001 | SPLIT | Local Windows Path Guard/race excluded; enforce no local runtime in Web bundle | SEC | WEB-TC-08, WEB-TC-13 | PENDING_OWNER |
| RM-002 | SPLIT | Machine VERIFY/HANDOFF operation excluded; manual policy/gate mapping still applies | ARCH | WEB-TC-08, WEB-TC-09 | PENDING_OWNER |
| RM-003 | WEB_APPLIES | Source/spec drift invalidates Web claims and prior review evidence | QA | WEB-TC-11 | PENDING_OWNER |
| RM-004 | SPLIT | Runtime CLOSE excluded; manual STOP must not silently close or authorize | QA | WEB-TC-10 | PENDING_OWNER |
| RM-005 | WEB_APPLIES | Host file ownership, destructive migration and evidence loss | HOST | WEB-TC-02, WEB-TC-12, WEB-TC-15 | PENDING_OWNER |
| RM-006 | WEB_APPLIES | AI authoring falsely described as business/security approval | PRODUCT | WEB-TC-08, WEB-TC-09 | PENDING_OWNER |
| RM-007 | WEB_APPLIES | Web STOP/resume accidentally claims persistent runtime state | QA | WEB-TC-10, WEB-TC-11 | PENDING_OWNER |
| RM-008 | WEB_APPLIES | Version mismatch and active legacy-state upgrade safety | HOST | WEB-TC-12, WEB-TC-15 | PENDING_OWNER |
| RM-009 | WEB_APPLIES | Host AGENTS and upstream Spec Kit ownership precedence | HOST | WEB-TC-02, WEB-TC-07 | PENDING_OWNER |
| RM-010 | WEB_APPLIES | Handoff falsely PERSISTED or leaks private context | SEC | WEB-TC-10, WEB-TC-14 | PENDING_OWNER |
| RM-011 | WEB_APPLIES | Product coding or commit starts without approved Phase B | PRODUCT | WEB-TC-08 | PENDING_OWNER |
| RM-012 | WEB_APPLIES | Manual Spec Kit syntax/feature pointer misapplied | ARCH | WEB-TC-07 | PENDING_OWNER |
| RM-013 | WEB_APPLIES | Historical build/test evidence treated as fresh PASS | QA | WEB-TC-09, WEB-TC-11 | PENDING_OWNER |
| RM-014 | WEB_APPLIES | Missing per-iteration risk re-evaluation and evidence | SEC | WEB-TC-05, WEB-TC-09 | PENDING_OWNER |
| RM-015 | WEB_APPLIES | Missing independently authorized source/AC/RTM A.1 signoff | PRODUCT | WEB-TC-08, WEB-TC-09 | PENDING_OWNER |
| RM-016 | SPLIT | Host adversarial OS tests deferred; Web-specific B.1 security remains mandatory | SEC | WEB-TC-13, WEB-TC-14 | PENDING_OWNER |
| RM-017 | WEB_APPLIES | A.1/B/B.1/release gates collapsed or bypassed | PRODUCT | WEB-TC-08 | PENDING_OWNER |
| RM-018 | WEB_APPLIES | Unreviewed newly released technology recommended as supported default | ARCH | WEB-TC-04 | PENDING_OWNER |
| RM-019 | SPLIT | Runtime EOL install excluded; inaccurate host/tool version guidance remains | ARCH | WEB-TC-04, WEB-TC-07 | PENDING_OWNER |
| RM-020 | WEB_APPLIES | Novel host document structure disrupts established ownership | HOST | WEB-TC-02 | PENDING_OWNER |
| RM-021 | WEB_APPLIES | Stale vendor support facts or version facts become source authority | ARCH | WEB-TC-04 | PENDING_OWNER |
| RM-022 | WEB_APPLIES | Requester override bypasses applicable host/security rules | SEC | WEB-TC-05, WEB-TC-08 | PENDING_OWNER |
| RM-023 | WEB_APPLIES | Version/structure override treated as implicit source edit permission | HOST | WEB-TC-08, WEB-TC-12 | PENDING_OWNER |
| RM-024 | WEB_APPLIES | Conservative default silently hides explicit safe user choice | PRODUCT | WEB-TC-04, WEB-TC-05 | PENDING_OWNER |
| RM-025 | WEB_APPLIES | Sequential model perspectives misrepresented as independent votes | QA | WEB-TC-09 | PENDING_OWNER |
| RM-026 | SPLIT | Automated worker coverage excluded; human independent coverage still required | QA | WEB-TC-09 | PENDING_OWNER |
| RM-027 | RUNTIME_EXCLUDED | Worker weight/persona algorithm not in Markdown Web profile; prohibit false runtime claim | ARCH | WEB-TC-08 | PENDING_OWNER |
| RM-028 | WEB_APPLIES | Citations, files, test outputs or evidence fabricated by Web author | QA | WEB-TC-03, WEB-TC-09 | PENDING_OWNER |
| RM-029 | SPLIT | Cross-worker orchestration excluded; permitted Web provider/context data boundary remains | SEC | WEB-TC-14 | PENDING_OWNER |
| RM-030 | WEB_APPLIES | Risk/approval dissent suppressed in summary or synthesis | SEC | WEB-TC-08, WEB-TC-09 | PENDING_OWNER |
| RM-031 | WEB_APPLIES | Untrusted Markdown prompt injection and sensitive disclosure | SEC | WEB-TC-13, WEB-TC-14 | PENDING_OWNER |
| RM-032 | WEB_APPLIES | Resume loses policy/source/review identity after drift | QA | WEB-TC-10, WEB-TC-11 | PENDING_OWNER |
| RM-033 | WEB_APPLIES | Token/context limits result in missing mandatory policy or unfounded quality claim | QA | WEB-TC-06, WEB-TC-09 | PENDING_OWNER |
| RM-034 | RUNTIME_EXCLUDED | Autonomous self-evolution/config execution excluded from package; verify capability negative | SEC | WEB-TC-08 | PENDING_OWNER |
| RM-035 | RUNTIME_EXCLUDED | Generated-code execution with CI credentials excluded from Web release | SEC | WEB-TC-08, WEB-TC-14 | PENDING_OWNER |
| RM-036 | WEB_APPLIES | Cleanup/upgrade overwrites historical or host-owned artifacts | HOST | WEB-TC-02, WEB-TC-12, WEB-TC-15 | PENDING_OWNER |
| RM-037 | WEB_APPLIES | Source summarization omits business or security authority | QA | WEB-TC-03, WEB-TC-05 | PENDING_OWNER |
| RM-038 | RUNTIME_EXCLUDED | Automated DBA/lint/mutation repair loop is future runtime work | ARCH | WEB-TC-08 | PENDING_OWNER |
| RM-039 | WEB_APPLIES | Context/token optimization loses mandatory policy coverage | QA | WEB-TC-06 | PENDING_OWNER |
| RM-040 | SPLIT | Automated retry/release feature disabled; manual upgrade interruption remains | HOST | WEB-TC-12, WEB-TC-15 | PENDING_OWNER |
| RM-041 | WEB_APPLIES | Same-model check described as external independent acceptance | QA | WEB-TC-08, WEB-TC-09 | PENDING_OWNER |
| RM-042 | RUNTIME_EXCLUDED | Multiworker overlapping code patches excluded; Web cannot auto-commit | SEC | WEB-TC-08 | PENDING_OWNER |
| RM-043 | SPLIT | OS process containment excluded; connector/host authorization still bounded | SEC | WEB-TC-13, WEB-TC-14 | PENDING_OWNER |
| RM-044 | SPLIT | Concurrent worker lease excluded; manual STOP and bounded handoff still required | QA | WEB-TC-10 | PENDING_OWNER |
| RM-045 | WEB_APPLIES | Same-model review and unmeasured quality/cost claims | QA | WEB-TC-06, WEB-TC-09 | PENDING_OWNER |
| RM-046 | WEB_APPLIES | Interface/version/evidence mismatch triggers false READY claim | QA | WEB-TC-09, WEB-TC-11 | PENDING_OWNER |
| RM-047 | SPLIT | MCP server excluded; untrusted-source injection still relevant to Web | SEC | WEB-TC-13 | PENDING_OWNER |
| RM-048 | WEB_APPLIES | Remote source/context sharing or redaction leaks credentials | SEC | WEB-TC-14 | PENDING_OWNER |
| RM-049 | SPLIT | CLI/state DB failures excluded; unavailable Web capability must be stated | QA | WEB-TC-03, WEB-TC-09 | PENDING_OWNER |
| RM-050 | WEB_APPLIES | Git branch/source movement invalidates a later documentation/release action | HOST | WEB-TC-11, WEB-TC-12 | PENDING_OWNER |
| RM-051 | WEB_APPLIES | Stale Git/BRD pair and role lenses treated as independent A.1 | QA | WEB-TC-08, WEB-TC-11 | PENDING_OWNER |
| RM-052 | WEB_APPLIES | Chat interruption or resume loses tasks, policy and provenance | QA | WEB-TC-10, WEB-TC-11 | PENDING_OWNER |


Global risk meaning/severity is owned by [riskMatrix.md](../.riskMatrix.md) and never overwritten by this profile overlay or historical PR #11 aliases. **RM-001 remains P0 OPEN, likelihood 4 × impact 5 = 20, residual UNKNOWN**. Web-only execution modes exclude local-agent host writes but do not authorize remote write or close a global risk.

## 7. AGENTS clause → existing acceptance test (17 rows)

| AGM | Integration behavior | Source / grant input | Proposed rule | Web test cases |
| --- | --- | --- | --- | --- |
| AGM-01 | Inventory root/nested AGENTS | Existing AGENTS paths, Git SHA, owner | Create exact source/policy inventory | WEB-TC-16, WEB-TC-17 |
| AGM-02 | Authority precedence | Host policy, approved BR/AC, nested AGENTS | Respect strongest applicable rules; conflict => BLOCK | WEB-TC-17, WEB-TC-19 |
| AGM-03 | Agent capability and consent | Actual provider tools, scoped authorization | No write without granted path and actual capability | WEB-TC-19, WEB-TC-21 |
| AGM-04 | S2C entrypoint/version | Pinned Web SKILL/BOOTSTRAP and bundle checksum | Link verified S2C profile; no development AGENTS copy | WEB-TC-16, WEB-TC-18 |
| AGM-05 | Agent roles/routing | Verified ChatGPT/Codex/host integration | Describe actual agents; no invented automated fleet | WEB-TC-16, WEB-TC-17 |
| AGM-06 | Nine-stage workflow | Approved process and actual host workflow | Add manual agent workflow, not fake machine phases | WEB-TC-16, WEB-TC-17 |
| AGM-07 | Context selection | Minimal/balanced/deep policy, mandatory sources | Record source/UNKNOWN; security floor not optional | WEB-TC-16, WEB-TC-17 |
| AGM-08 | Git/edit authorization | Host code/commit/merge/deploy rules | Keep distinct write/commit/push/merge permissions | WEB-TC-19, WEB-TC-21 |
| AGM-09 | Secrets/untrusted content | Host privacy/security constraints | Never export secrets or accept tool grants in source text | WEB-TC-19, WEB-TC-21 |
| AGM-10 | Risk and validation | P0, owner decisions, A.1/B/B.1 | Stop on applicable blocker; no self-approval | WEB-TC-17, WEB-TC-19 |
| AGM-11 | Spec Kit ownership | Existing feature pointer/spec/plan/tasks | Reuse native artifacts, never overwrite upstream | WEB-TC-17 |
| AGM-12 | STOP and RESUME | Host-specific evidence path/source hash | Persist only with readback; invalidate stale state | WEB-TC-18, WEB-TC-20 |
| AGM-13 | Test and evidence policy | QA rules, real logs and statuses | PASS requires observation; NOT_RUN otherwise | WEB-TC-17, WEB-TC-20 |
| AGM-14 | Create/adopt/upgrade | Old pristine, current customized, new pristine | Create if absent, else bounded insert/three-way merge | WEB-TC-16, WEB-TC-17, WEB-TC-18 |
| AGM-15 | Nested AGENTS scope | Per-module paths, non-overridable policies | No cross-module propagation or unauthorized nested write | WEB-TC-17, WEB-TC-19 |
| AGM-16 | Idempotence and rollback | Version marker, baseline hashes and approved backup | No duplicated sections; version updated last; **conflict fingerprint blocks repeated automatic attempts; never overwrite customized host clauses** | WEB-TC-18, WEB-TC-20 |
| AGM-17 | Unavailable capabilities | Read-only connector/unknown source/ref | Matrix+diff/handoff NOT_APPLIED, never imaginary host write | WEB-TC-19, WEB-TC-21 |


Host root/nested AGENTS and external provider permission checks are required. Same conflict input => `BLOCKED_CONFLICT / NO_WRITE`, suggested diff only and no automatic retry; only a true newly observed input or independent owner conflict-specific decision permits new dry-run.

## 8. Integration blockers and verification boundary

The [full Phase A coherence audit](phaseAIntegrationCoherenceAudit20261123.md) records Git lineage, observed CI checks, whole-tree Markdown results, PR #11 archived identifiers, current Spec Kit workflow drift, current task/test risk status and owner review queue.

**No false promotion:** `AUTHOR_STATIC_MATRIX_VERIFIED` is a documentation consistency finding only. Four OS/Python unit jobs and one Ruff job had observed PASS on the input source commit, but 21 profile Web tests, real host AGENTS integrations, native Spec Kit smoke on `s2c/PhaseA`, adversarial Windows RM-001 and independent A.1/B.1 remain NOT_RUN.

## D01–D06 requester decision supersession (2026-11-23)

**Requester design decisions now recorded:** D01 = **Git alone normative**. Previous Google `BRD_Spec2Code` v1.5 is a *historical Gemini-era source*, imported in its entirety into Git as [source archive](legacyGoogleBrdSourceArchive20261123.md); **do not require future Google revision matching or treat Google as a second current business authority**. Source conflict checks still apply to other differing Git/ZIP/snapshot inputs. D02 = **all BR-001..016 receive individual dedicated Web AC and TC**: [16 pairs](phaseAD02BrDedicatedWebCoverage20261123.md); BR-007 and BR-008 are **not** REFERENCE_ONLY for Web acceptance. D03 = BR-017..021 accepted as architecture/requirements **design scope**, automated reviewer fleet deferred. D04 = BR-022..027 retained in roadmap, **not mandatory V1 implementation**. D05 = **100% PASS of applicable mandatory Web AC/test P/N variants** required for V1 release; inherited `R>99.99%` and BR-027 `>95%` scoped coverage await approved measurement/denominator rather than an invented waiver. D06 = read/upload in ChatGPT Web plus only **individually authorized remote GitHub API host AGENTS.md-only writes**; local OS/native agent writes excluded. Full dispositions: [decision register](phaseAD01D06RequesterDecisionRegister20261123.md).

**Current suite: 37 AC + 37 planned TC (21 baseline + 16 BR-dedicated), 37/37 NOT_RUN.** No actual host permission, A.1/B/B.1 gate, risk acceptance or release is implied. Historic notes above remain dated source evidence and are **superseded where they contradict D01–D06**.

## Ma trận thống nhất toàn bộ tài liệu tại `28d40a3`

Ngày 2026-11-23 · Nhánh `s2c/PhaseA` · SHA `28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5` · Rà soát tĩnh Phase A.

### Phạm vi và cách đọc

Đọc 147/147 file Markdown và 1/1 con trỏ Spec Kit từ GitHub ở cùng SHA. Tree đệ quy đầy đủ trả về 210 mục, gồm thư mục và tệp. Phạm vi tài liệu gồm 110 mục trong .agents, 15 trong .source, 3 trong .specify (gồm con trỏ), 9 trong docs, 9 trong specs, AGENTS.md và README.md. Toàn bộ tập nguồn được đọc cho kiểm kê và quét cấu trúc. Đối chiếu ngữ nghĩa tập trung vào các nguồn và giao điểm liệt kê dưới đây. Không coi những ghi chép lịch sử là quy tắc hiện hành.

- **LỆCH** — nội dung vận hành hiện hành có chỉ dẫn mâu thuẫn hoặc thiếu điều kiện.
- **KHỚP TĨNH** — cấu trúc hoặc tuyên bố được đối chiếu tại SHA này.
- **CHỜ OWNER** — quyết định hoặc bằng chứng còn thiếu.
- **LỊCH SỬ** — giữ nội dung và SHA gốc. Chỉ sửa đường dẫn hoặc thêm ghi chú dẫn quy tắc hiện hành khi cần.

Các vị trí bên dưới là số dòng trên Git ở SHA gốc. Bản vá cục bộ 9 file `phaseA-review-remediation.patch` được đối chiếu riêng. HEAD GitHub chưa chứa bản vá tại thời điểm rà soát.

### Ma trận thống nhất

| ID | Chủ đề / nguồn chuẩn | Quan sát tại HEAD | Kết quả / xử lý | Owner / tiêu chí đóng |
| --- | --- | --- | --- | --- |
| M01 | D01; .agents/.spec.md §2; sổ D01–D06 | .agents/.workflow/validationReportTemplate.md:64,70 và validationSpecification.md:129,162,168,194 vẫn yêu cầu cặp Git/Google. | LỆCH. Có bản vá cục bộ cho mẫu và quy tắc hiện hành. Dùng một SHA Git và dẫn archive khi cần provenance. | Workflow / Reviewer hoàn tất mẫu mà không cần revision Google. |
| M02 | D01; quyền theo chủ đề | .agents/.spec.md:111 vẫn yêu cầu Git+Google để duyệt AC. .agents/.documents/.documentGovernance.md:25–42 còn mô tả nguồn Google và bắt buộc revision pair cho lần A.1 mới. | LỆCH. Ngoài bản vá 9 file. Sửa ngay các chỉ dẫn đang dùng. Giữ lịch sử PLAN-087/101 và đánh dấu phạm vi lịch sử tại đầu mục nếu cần. | Product / Doc owner. D01 có cùng cách áp dụng ở master, governance và mẫu ký. |
| M03 | D02/D05; catalogue AC/TC và RTM | 37 AC, 37 TC và 16 cặp BR-001–016 hiện diện. Nhóm G1–G7 chỉ chứa 21 case tại webV1AcceptanceAndTraceability.md:51–59. | LỆCH nhóm QA. Bản vá cục bộ có đủ 37 case, mỗi case một nhóm. Xác định mẫu số, fixture và quy tắc kết quả cha khi còn variant thiếu. | Product / QA. Mọi TC-01..37 có nhóm duy nhất và đủ variant áp dụng. |
| M04 | D02/D05; hướng dẫn A.1 và release | webV1A1DesignReviewPacket.md:12–21,65 còn tiêu chí Git/Google và 21 ca; markdownFirstReleasePlan.md:148 vẫn chỉ sang TC-01..21. webV1OwnerDecisionRegister.md:35,67 lưu điều kiện U-04 ban đầu và có D01–D06 ở cuối. | LỆCH hướng dẫn A.1/release. Ngoài bản vá 9 file. Cập nhật dòng dùng cho review. Gắn liên kết thay thế cho U-04 cũ thay vì xóa lịch sử. | Release / Workflow. Người đọc đi theo mỗi entrypoint đều gặp cùng bộ 37 ca và quy tắc D01. |
| M05 | D03/D04; BR catalog và reverse trace | 27 BR duy nhất trong master; sáu dòng BR bổ sung xuất hiện lại trong phần thiết kế chi tiết. Reverse matrix giữ BR-007/008 cùng TC-28/29; BR-017–021 giữ thiết kế và BR-022–027 ở roadmap. AGENTS.md:111 và :119 mô tả phạm vi BR của master khác nhau. | KHỚP TĨNH với phạm vi D03/D04. Làm rõ đoạn PLAN-088 ở AGENTS chỉ mô tả nhóm BR lịch sử của plan; nguồn hiện hành có đủ 27 mã. | Product / Documentation. Duy trì 27 mã và không đưa feature hoãn vào tiêu chí bắt buộc V1. |
| M06 | D06; hợp đồng AGM | AGM §1 cho phép Codex hoặc agent khác làm executor; §6 yêu cầu finalize manifest nhưng chưa chỉ rõ đích trong phạm vi AGENTS-only. | LỆCH. Bản vá cục bộ giới hạn GitHub API từ xa, đưa metadata phiên bản vào khối quản lý và mô tả bằng chứng handoff. | Architecture / Host. Đường ghi và mọi hiệu ứng đều nằm trong grant đã xác minh. |
| M07 | D06; gián đoạn và đối chiếu | TC-20 hiện có lặp và SHA cũ; chưa có oracle riêng cho mất phản hồi sau ghi. RM-040/050 chưa nối tới readback theo path và cập nhật đồng thời. | LỆCH. Bản vá cục bộ bổ sung variant theo TC-20, kèm NOT_APPLIED/PARTIAL/UNVERIFIED, không thêm ID ca. | Architecture / QA / Security. Thực thi đúng các variant được duyệt trong giai đoạn cho phép; lưu ref/blob trước và sau. |
| M08 | D05; release gate và KPI | Master decision yêu cầu 100% tiêu chí bắt buộc và variant áp dụng. Reliability >99.99% và coverage >95% còn thiếu quyết định đo. Các văn bản có nhắc ngưỡng nhưng không thể suy ra KPI từ kết quả của 37 ca thiết kế. | CHỜ OWNER. Tách mẫu số nghiệm thu xác định khỏi cách đo reliability và coverage. | Product / QA. Phê duyệt phương pháp, dữ liệu, ngưỡng và bằng chứng trên SHA cụ thể. |
| M09 | Risk overlay và risk matrix | 52 ID duy nhất: 35 WEB_APPLIES, 12 SPLIT, 5 RUNTIME_EXCLUDED. Cả 52 PENDING_OWNER. RM-001 toàn cục P0 OPEN. | CHỜ OWNER. Xác nhận mode riêng cho upload/read và remote GitHub; giữ trạng thái toàn cục tới khi có bằng chứng. | Security / Host. Mỗi rủi ro áp dụng có owner, control, TC/variant, bằng chứng và disposition. |
| M10 | Spec Kit pointer và feature contract | .specify/feature.json trỏ đến specs/001-s2c-speckit-integration và thư mục có trong Git. Tài liệu Web đề cập v1.4.3 ở mức ứng viên tương thích. specKitWebWorkflow.md:27 còn yêu cầu ghi Google revision khi STOP/RESUME dù nguồn Web V1 đã chuyển sang Git. | KHỚP TĨNH về con trỏ. LỆCH cách ghi provenance trong luồng Web. Sửa mẫu handoff để ghi Git SHA bắt buộc và revision ngoài Git chỉ khi thực sự là input. | Workflow / Architecture. Phân biệt tương thích đọc cấu trúc và bằng chứng chạy native. |
| M11 | Backlog, feature và gate | 30 WEB task duy nhất; 64 feature trong reverse matrix; 17 AGM ID duy nhất. A.1 không có chữ ký độc lập. 37 Web TC mới ở thiết kế. | KHỚP TĨNH về danh mục. CHỜ OWNER về A.1, QA và Security. Giữ B NOT_AUTHORIZED. | Reviewer / Product. Chốt SHA sau sửa, bàn giao tài liệu có đủ owner và chạy A1-VAL-01..09. |
| M12 | Liên kết tài liệu và hồ sơ cũ | Quét đơn giản 1.447 kết quả khớp cú pháp link tương đối trong dòng ngoài khối code. Có 3 ví dụ cú pháp trong inline code và 11 lần tham chiếu không tìm thấy đích, tập trung ở ba handoff legacy v0.6.4. | LỊCH SỬ. Sau khi loại ví dụ, 1.444 link tương đối được kiểm, 1.433 trỏ tới mục trong tree, 11 thiếu đích. Giữ lịch sử; dùng ghi chú hoặc tương thích đường dẫn nếu cần đọc lại. | Documentation. Khi chỉnh, xác nhận các bản lưu đích rồi chạy lại kiểm tra đường dẫn. |

### Thứ tự thống nhất

1. Gộp các sửa đổi đã soạn ở M01, M03, M06, M07 vào một revision tài liệu được phép. Giữ nguyên trạng thái test, rủi ro và các cổng phê duyệt.
2. Trên cùng revision, sửa các điểm còn ngoài bản vá ở M02, M04, M05 và M10. Ưu tiên nguồn quy tắc, gói ký duyệt và release plan. Gắn ghi chú supersession ở tài liệu lịch sử có thể bị dùng lại.
3. Tái kiểm tra 27 BR, 64 feature, 30 task, 37 AC/TC, 16 cặp dành riêng, 52 risk và 17 AGM. Kiểm lại chế độ source/AGENTS và danh sách file đổi. Ghi SHA sau sửa để reviewer có thể tái lập.
4. Giao Product/QA chốt M08, Security/Host chốt M09 và reviewer độc lập đánh giá M11. Phần review kỹ thuật hiện tại là bằng chứng đầu vào, không phải chữ ký A.1.

### Giới hạn bằng chứng

Quét link chỉ kiểm sự tồn tại của đường dẫn trong Git tree cho cú pháp inline đơn giản. Không xác minh heading fragment, URL ngoài Git, link dạng reference, nội dung ẩn sau provider hoặc render. Kiểm kê đầy đủ 148 mục không đồng nghĩa đã ký duyệt ngữ nghĩa từng đoạn. Không chạy Web TC, native Spec Kit, bộ test Python, CI, hành động ghi host hay Phases B/B.1. Hồ sơ Git vẫn A.1 NOT_RUN, 37/37 TC NOT_RUN, RM-001 P0 OPEN và B NOT_AUTHORIZED.

### Nguồn đối chiếu tại commit đã kiểm tra

- [.agents/.spec.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.spec.md)
- [.agents/.documents/.documentGovernance.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/.documentGovernance.md)
- [.agents/.documents/webV1A1DesignReviewPacket.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1A1DesignReviewPacket.md)
- [.agents/.documents/webV1AcceptanceAndTraceability.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1AcceptanceAndTraceability.md)
- [.agents/.workflow/validationSpecification.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.workflow/validationSpecification.md)
- [.agents/.workflow/validationReportTemplate.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.workflow/validationReportTemplate.md)
- [.agents/.documents/webV1RiskApplicability.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1RiskApplicability.md)
- [.agents/.documents/webV1AgentsIntegrationMatrix.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1AgentsIntegrationMatrix.md)
- [.agents/.workflow/testingAndDelivery.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.workflow/testingAndDelivery.md)

### Kiểm kê nguồn đã đọc

| Tài liệu | Blob Git (12 ký tự đầu) |
| --- | --- |
| [.agents/.changelog.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.changelog.md) | `23b1365e4024` |
| [.agents/.checklist.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.checklist.md) | `12b584ced8aa` |
| [.agents/.config/README.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.config/README.md) | `3755cd347ef8` |
| [.agents/.documents/.documentGovernance.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/.documentGovernance.md) | `3e51e2ef25f3` |
| [.agents/.documents/.policyRouting.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/.policyRouting.md) | `85592cd67d07` |
| [.agents/.documents/featureDesign.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/featureDesign.md) | `cb8f884eb265` |
| [.agents/.documents/legacyGoogleBrdSourceArchive20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/legacyGoogleBrdSourceArchive20261123.md) | `3990e82515fc` |
| [.agents/.documents/markdownFirstReleasePlan.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/markdownFirstReleasePlan.md) | `1c221fb59cc4` |
| [.agents/.documents/phaseABrdSemanticReconciliation20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/phaseABrdSemanticReconciliation20261123.md) | `414a0e918236` |
| [.agents/.documents/phaseAD01D06RequesterDecisionRegister20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/phaseAD01D06RequesterDecisionRegister20261123.md) | `52b9a9dfbb95` |
| [.agents/.documents/phaseAD02BrDedicatedWebCoverage20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/phaseAD02BrDedicatedWebCoverage20261123.md) | `0f16e53a4df5` |
| [.agents/.documents/phaseAIntegrationCoherenceAudit20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/phaseAIntegrationCoherenceAudit20261123.md) | `aea0e1a6e0a9` |
| [.agents/.documents/phaseAUnifiedIntegrationMatrix20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/phaseAUnifiedIntegrationMatrix20261123.md) | `77270732b016` |
| [.agents/.documents/researchRegister.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/researchRegister.md) | `1f378c66af43` |
| [.agents/.documents/specKitBridgeSourceAudit096.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/specKitBridgeSourceAudit096.md) | `ed925b81afe8` |
| [.agents/.documents/specKitNativePilot.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/specKitNativePilot.md) | `79a50da69e81` |
| [.agents/.documents/specKitUpstreamEnvAudit097.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/specKitUpstreamEnvAudit097.md) | `ea5be5ed430f` |
| [.agents/.documents/specKitWebModeEvidence095.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/specKitWebModeEvidence095.md) | `6afa690367e0` |
| [.agents/.documents/systemSpecificationPlan.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/systemSpecificationPlan.md) | `d465d14f44e8` |
| [.agents/.documents/technologyAssessmentTemplate.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/technologyAssessmentTemplate.md) | `36a7bebab03d` |
| [.agents/.documents/technologyOverrideTemplate.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/technologyOverrideTemplate.md) | `890f2b66a173` |
| [.agents/.documents/technologyVersionPolicy.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/technologyVersionPolicy.md) | `b88175af494b` |
| [.agents/.documents/webV1A1DesignReviewPacket.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1A1DesignReviewPacket.md) | `b9ab76530085` |
| [.agents/.documents/webV1AClosureApprovalPacket20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1AClosureApprovalPacket20261123.md) | `e8655ae3f8a9` |
| [.agents/.documents/webV1AClosureEvidence20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1AClosureEvidence20261123.md) | `e6415fc32250` |
| [.agents/.documents/webV1AClosureFeatureReverseMatrix20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1AClosureFeatureReverseMatrix20261123.md) | `d4fa0e733d53` |
| [.agents/.documents/webV1AClosureWebTestOracleDesign20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1AClosureWebTestOracleDesign20261123.md) | `b08a864ec605` |
| [.agents/.documents/webV1AcceptanceAndTraceability.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1AcceptanceAndTraceability.md) | `91e1d7d93c8a` |
| [.agents/.documents/webV1AgentsIntegrationMatrix.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1AgentsIntegrationMatrix.md) | `9f18659268a2` |
| [.agents/.documents/webV1FullBranchHistoryIntegration20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1FullBranchHistoryIntegration20261123.md) | `70e2646415f0` |
| [.agents/.documents/webV1FullMarkdownLinkAudit20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1FullMarkdownLinkAudit20261123.md) | `e9fed3f9c7ec` |
| [.agents/.documents/webV1GeminiReviewDisposition20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1GeminiReviewDisposition20261123.md) | `049faba3a923` |
| [.agents/.documents/webV1OwnerDecisionRegister.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1OwnerDecisionRegister.md) | `95b7998abe7e` |
| [.agents/.documents/webV1Pr11AddedLinesArchive20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1Pr11AddedLinesArchive20261123.md) | `c549374ada36` |
| [.agents/.documents/webV1Pr11CollisionReconciliation20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1Pr11CollisionReconciliation20261123.md) | `cfd0dc7d8ce1` |
| [.agents/.documents/webV1PreflightAndCapabilityMatrix.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1PreflightAndCapabilityMatrix.md) | `d18a0a9940eb` |
| [.agents/.documents/webV1RequesterConditionalDecisions20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1RequesterConditionalDecisions20261123.md) | `4ece2a3284b0` |
| [.agents/.documents/webV1RiskApplicability.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1RiskApplicability.md) | `094cb863d609` |
| [.agents/.documents/webV1StaticMarkdownAudit20261123.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.documents/webV1StaticMarkdownAudit20261123.md) | `51bb9ff4a1bc` |
| [.agents/.features.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.features.md) | `f98781e13a97` |
| [.agents/.git.workflow.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.git.workflow.md) | `f124285e3f92` |
| [.agents/.handoffs/a1-author-preflight-20261114.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/a1-author-preflight-20261114.md) | `2586aaa8025c` |
| [.agents/.handoffs/a1-reconciliation-readiness-20261114.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/a1-reconciliation-readiness-20261114.md) | `fe607505301a` |
| [.agents/.handoffs/audit-20261114-agents-compatibility.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/audit-20261114-agents-compatibility.md) | `daea2b3e29d2` |
| [.agents/.handoffs/legacy-v0.6.4-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/legacy-v0.6.4-handoff.md) | `f7a173b9af71` |
| [.agents/.handoffs/legacy-v0.6.4-plan.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/legacy-v0.6.4-plan.md) | `e75a45e56f55` |
| [.agents/.handoffs/legacy-v0.6.4-riskdetail.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/legacy-v0.6.4-riskdetail.md) | `9de6f09ae84a` |
| [.agents/.handoffs/owner-design-approvals-app-01-06-20261114.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/owner-design-approvals-app-01-06-20261114.md) | `587059298d14` |
| [.agents/.handoffs/plan-080-v0.8-governance-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-080-v0.8-governance-handoff.md) | `2e88f09744b0` |
| [.agents/.handoffs/plan-081-agent-governance-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-081-agent-governance-handoff.md) | `065f9146563b` |
| [.agents/.handoffs/plan-082-083-rtm-stop-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-082-083-rtm-stop-handoff.md) | `5af3882640fa` |
| [.agents/.handoffs/plan-084-design-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-084-design-handoff.md) | `62461604fcb0` |
| [.agents/.handoffs/plan-085-validation-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-085-validation-handoff.md) | `8997a983d590` |
| [.agents/.handoffs/plan-086-technology-override-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-086-technology-override-handoff.md) | `a74c71625a2c` |
| [.agents/.handoffs/plan-089-a1-readiness-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-089-a1-readiness-handoff.md) | `6c63febb10d1` |
| [.agents/.handoffs/plan-090-a1-preflight-review.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-090-a1-preflight-review.md) | `685b14477e94` |
| [.agents/.handoffs/plan-091-remediation-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-091-remediation-handoff.md) | `f021d4c16794` |
| [.agents/.handoffs/plan-092-speckit-adoption-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-092-speckit-adoption-handoff.md) | `f36041dd8a39` |
| [.agents/.handoffs/plan-093-sk03-native-pilot-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-093-sk03-native-pilot-handoff.md) | `54b521285e27` |
| [.agents/.handoffs/plan-094-speckit-feature-completeness-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-094-speckit-feature-completeness-handoff.md) | `57266f161b4b` |
| [.agents/.handoffs/plan-095-webmode-evidence-native-gate-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-095-webmode-evidence-native-gate-handoff.md) | `abc33a9d8735` |
| [.agents/.handoffs/plan-096-bridge-source-audit-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-096-bridge-source-audit-handoff.md) | `485e2022113c` |
| [.agents/.handoffs/plan-097-native-env-boundary-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-097-native-env-boundary-handoff.md) | `5d5a3a2e19f0` |
| [.agents/.handoffs/plan-100-documentation-checkpoint-1.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-100-documentation-checkpoint-1.md) | `e7906c5e4c5d` |
| [.agents/.handoffs/plan-100-documentation-checkpoint-2.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-100-documentation-checkpoint-2.md) | `c5d5292a4d98` |
| [.agents/.handoffs/plan-100-l0-readiness-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-100-l0-readiness-handoff.md) | `9fc67e4e1c5c` |
| [.agents/.handoffs/plan-101-documentation-checkpoint-3.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-101-documentation-checkpoint-3.md) | `2fcb43b84e85` |
| [.agents/.handoffs/plan-101-documentation-checkpoint-4.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-101-documentation-checkpoint-4.md) | `2f6bf895fa1e` |
| [.agents/.handoffs/plan-102-documentation-checkpoint-5.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-102-documentation-checkpoint-5.md) | `84a74f91570b` |
| [.agents/.handoffs/plan-102-documentation-checkpoint-6.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-102-documentation-checkpoint-6.md) | `5fd2cd26ee40` |
| [.agents/.handoffs/plan-103-documentation-final-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-103-documentation-final-handoff.md) | `59b894241a84` |
| [.agents/.handoffs/plan-103-documentation-navigation-checkpoint.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-103-documentation-navigation-checkpoint.md) | `6d9d67c452a8` |
| [.agents/.handoffs/plan-103-documentation-review-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-103-documentation-review-handoff.md) | `6c8b6073a81b` |
| [.agents/.handoffs/plan-103-owner-review-packet.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-103-owner-review-packet.md) | `36a3634724aa` |
| [.agents/.handoffs/plan-103-traceability-review-checkpoint.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-103-traceability-review-checkpoint.md) | `de372028de38` |
| [.agents/.handoffs/plan-104-batch-a-documentation-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-104-batch-a-documentation-handoff.md) | `d73707db8673` |
| [.agents/.handoffs/plan-105-batch-b-documentation-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-105-batch-b-documentation-handoff.md) | `91f62d664b2b` |
| [.agents/.handoffs/plan-106-10task-batch-1.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-106-10task-batch-1.md) | `200fef4e1303` |
| [.agents/.handoffs/plan-107-10task-batch-2.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-107-10task-batch-2.md) | `c10ccfd2f9f4` |
| [.agents/.handoffs/plan-108-10task-batch-3.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-108-10task-batch-3.md) | `144d5ffd0396` |
| [.agents/.handoffs/plan-109-10task-batch-4.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-109-10task-batch-4.md) | `a84c45a313e5` |
| [.agents/.handoffs/plan-110-10task-batch-5.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-110-10task-batch-5.md) | `e1eec0525d6c` |
| [.agents/.handoffs/plan-111-a1-p0-return-to-a.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-111-a1-p0-return-to-a.md) | `584f6cee36f7` |
| [.agents/.handoffs/plan-112-a1-security-continuation.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-112-a1-security-continuation.md) | `68e979e45033` |
| [.agents/.handoffs/plan-112-a1-security-owner-packet.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-112-a1-security-owner-packet.md) | `c33dd821164d` |
| [.agents/.handoffs/plan-112-windows-p0-codex.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-112-windows-p0-codex.md) | `9838940a5fb9` |
| [.agents/.handoffs/plan-113-antigravity-gemini-reviewer-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-113-antigravity-gemini-reviewer-handoff.md) | `c7958515401c` |
| [.agents/.handoffs/plan-114-codex-gemini-agent-integration-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-114-codex-gemini-agent-integration-handoff.md) | `b6d3dcb62bc1` |
| [.agents/.handoffs/plan-115-relationship-vmware-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-115-relationship-vmware-handoff.md) | `d0dee784a46c` |
| [.agents/.handoffs/plan-116-markdown-first-release-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/plan-116-markdown-first-release-handoff.md) | `891553e534de` |
| [.agents/.handoffs/v0.7.0-layout-handoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/v0.7.0-layout-handoff.md) | `40efcaa3839a` |
| [.agents/.handoffs/v0.7.0-windows-ci-fix.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.handoffs/v0.7.0-windows-ci-fix.md) | `6a1959f08d39` |
| [.agents/.plans.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.plans.md) | `7c3431c8d797` |
| [.agents/.risk.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.risk.md) | `3bc4455fe859` |
| [.agents/.riskMatrix.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.riskMatrix.md) | `4dc1a6e500fc` |
| [.agents/.spec.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.spec.md) | `ef61bd10bfa8` |
| [.agents/.structure.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.structure.md) | `ef951f82e087` |
| [.agents/.traceMatrix.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.traceMatrix.md) | `206713924a4f` |
| [.agents/.workflow/README.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.workflow/README.md) | `1d8c68d1f015` |
| [.agents/.workflow/agentRoles.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.workflow/agentRoles.md) | `27bc0b1a9c3f` |
| [.agents/.workflow/agentRunbook.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.workflow/agentRunbook.md) | `150e97f46960` |
| [.agents/.workflow/designHandoffTemplate.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.workflow/designHandoffTemplate.md) | `ebb04faa1863` |
| [.agents/.workflow/planningSpecificationWorkflow.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.workflow/planningSpecificationWorkflow.md) | `6a6752adcb48` |
| [.agents/.workflow/specKitNativeExecutionGate.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.workflow/specKitNativeExecutionGate.md) | `457b31785a94` |
| [.agents/.workflow/specKitWebWorkflow.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.workflow/specKitWebWorkflow.md) | `0e5eac473ce3` |
| [.agents/.workflow/stopAndHandoff.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.workflow/stopAndHandoff.md) | `8acfdd4da443` |
| [.agents/.workflow/testingAndDelivery.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.workflow/testingAndDelivery.md) | `dbd1487f19af` |
| [.agents/.workflow/validationReportTemplate.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.workflow/validationReportTemplate.md) | `948e8cb67f7d` |
| [.agents/.workflow/validationSpecification.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.workflow/validationSpecification.md) | `b25c25d1c665` |
| [.agents/.workflow/workflowSpecification.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.agents/.workflow/workflowSpecification.md) | `5a5774a95790` |
| [.source/SKILL.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.source/SKILL.md) | `2c2b64eead0c` |
| [.source/integrations/speckit/README.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.source/integrations/speckit/README.md) | `dd5d6258c723` |
| [.source/references/adaptive-modes.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.source/references/adaptive-modes.md) | `182ba006ec82` |
| [.source/references/architecture-graph.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.source/references/architecture-graph.md) | `368804015613` |
| [.source/references/feature-spec-template.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.source/references/feature-spec-template.md) | `538ed4564adb` |
| [.source/references/handoff-template.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.source/references/handoff-template.md) | `51c69baab782` |
| [.source/references/hierarchy-layout.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.source/references/hierarchy-layout.md) | `a015dd2184d2` |
| [.source/references/implementation-plan-template.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.source/references/implementation-plan-template.md) | `0fe111e9f712` |
| [.source/references/infrastructure-scanning.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.source/references/infrastructure-scanning.md) | `29aa305bf0c8` |
| [.source/references/quality-gates.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.source/references/quality-gates.md) | `5ba1180ada2e` |
| [.source/references/session-lifecycle.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.source/references/session-lifecycle.md) | `cf35788bbe5a` |
| [.source/references/spec-to-code-workflow.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.source/references/spec-to-code-workflow.md) | `b544cdc182ee` |
| [.source/references/stop-handoff-template.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.source/references/stop-handoff-template.md) | `3aeb18ec4aa1` |
| [.source/references/tasks-template.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.source/references/tasks-template.md) | `a8cd3a471011` |
| [.source/references/traceability-template.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.source/references/traceability-template.md) | `de3e1b99903c` |
| [.specify/README.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.specify/README.md) | `dc693febc74c` |
| [.specify/feature.json](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.specify/feature.json) | `8172bcc56b44` |
| [.specify/memory/constitution.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/.specify/memory/constitution.md) | `c91e240bbae2` |
| [AGENTS.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/AGENTS.md) | `4acbe1d463b7` |
| [README.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/README.md) | `8c083d7c81dc` |
| [docs/AGENTS_PATCH.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/docs/AGENTS_PATCH.md) | `05e454495f59` |
| [docs/ANTIGRAVITY_GEMINI_REVIEWER.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/docs/ANTIGRAVITY_GEMINI_REVIEWER.md) | `9ea0e4557bbd` |
| [docs/CONFIGURATION.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/docs/CONFIGURATION.md) | `f63650d5f0aa` |
| [docs/CONTINUOUS_SCOPE_ENFORCEMENT.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/docs/CONTINUOUS_SCOPE_ENFORCEMENT.md) | `341c02481657` |
| [docs/INSTALL.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/docs/INSTALL.md) | `a65a9c51e3b7` |
| [docs/INTEGRATION_LAYOUT.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/docs/INTEGRATION_LAYOUT.md) | `4b0bbf44fc1b` |
| [docs/PATH_GUARD.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/docs/PATH_GUARD.md) | `3b1ed2da76ab` |
| [docs/STRUCTURE.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/docs/STRUCTURE.md) | `812fa36818d4` |
| [docs/VMWARE_SECURITY_VALIDATION.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/docs/VMWARE_SECURITY_VALIDATION.md) | `ea66b838a9ab` |
| [specs/001-s2c-speckit-integration/checklists/integrationAcceptance.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/specs/001-s2c-speckit-integration/checklists/integrationAcceptance.md) | `36ac1e6af41f` |
| [specs/001-s2c-speckit-integration/checklists/requirements.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/specs/001-s2c-speckit-integration/checklists/requirements.md) | `0445118e2e85` |
| [specs/001-s2c-speckit-integration/contracts/web-native-interface.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/specs/001-s2c-speckit-integration/contracts/web-native-interface.md) | `94ece1fc86e7` |
| [specs/001-s2c-speckit-integration/data-model.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/specs/001-s2c-speckit-integration/data-model.md) | `86afb05cb7ed` |
| [specs/001-s2c-speckit-integration/plan.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/specs/001-s2c-speckit-integration/plan.md) | `923a7caf4312` |
| [specs/001-s2c-speckit-integration/quickstart.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/specs/001-s2c-speckit-integration/quickstart.md) | `953fdfc6912d` |
| [specs/001-s2c-speckit-integration/research.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/specs/001-s2c-speckit-integration/research.md) | `37d654d186f4` |
| [specs/001-s2c-speckit-integration/spec.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/specs/001-s2c-speckit-integration/spec.md) | `4de86c531969` |
| [specs/001-s2c-speckit-integration/tasks.md](https://github.com/RyugaWork/spec2code/blob/28d40a3d7cf1741d7b0abb8490d1e538eb1e3cd5/specs/001-s2c-speckit-integration/tasks.md) | `24051a052519` |
