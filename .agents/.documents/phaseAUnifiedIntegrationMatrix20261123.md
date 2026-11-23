# S2C Phase A — Unified Integration & Traceability Matrix (source-bound)

**Status: AUTHOR_STATIC_MATRIX_VERIFIED / DESIGN_AND_OWNER_GATES_PENDING.** Source branch `s2c/PhaseA`, audit input SHA `4f3f22928673a9c80a2fa0bf9988f2daa1a9cfb4`, Git tree `223c576403dd5a357218f5732caa37665086b5b5`, 2026-11-23. This is a **derived audit snapshot**; normative wording and owners remain in [master SRS](../.spec.md), [canonical RTM](../.traceMatrix.md), [risk register](../.riskMatrix.md), [plans](../.plans.md), [Web feature scope](webV1AClosureFeatureReverseMatrix20261123.md), [QA cases](../.workflow/testingAndDelivery.md), [AC design](webV1AcceptanceAndTraceability.md) and [AGM](webV1AgentsIntegrationMatrix.md). No source/test status is promoted by this report.

## 1. Matrix completeness and invariants

| Integration layer | Observed unique primary IDs | Static check | Remaining gate |
| --- | ---: | --- | --- |
| Feature scope | 64 F01..F64 | One row per ID, valid Web task/test references | Product architecture applicability not signed |
| Business requirement | 27 BR-001..027 | One Web disposition per ID | Google-versus-Git semantics and BR-007/008 choice pending |
| Web tasks | 30 WEB-001..030 | 30 unique, all dependencies exist, DAG no cycles | Only WEB-001..003 author documentation complete |
| Web acceptance | 21 WEB-AC-01..21 | 21 unique; one-to-one TC link | QA must approve fixtures/denominator |
| Web tests | 21 WEB-TC-01..21 | 21 unique; every task ref resolves | All 21 NOT_RUN; not CI Python tests |
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


**Important:** BR-007 and BR-008 are owner-blocked for choosing `REFERENCE_ONLY` or explicit existing-case oracles. The existence of 27 BR labels on Google and Git does not establish approved semantic equivalence.

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

## 5. Web acceptance → mandatory test → related task (21 rows)

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
