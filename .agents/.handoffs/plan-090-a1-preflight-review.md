# PLAN-090 — A.1 design-document technical review and synthesis (PRELIMINARY)

> Review snapshot: 2026-11-13, branch `docs/plan-089-a1-readiness`, HEAD `1dae9338f4d38518e897212cdf80ba47239a7671` (PR #10, Draft); review report is on a separate branch `docs/plan-090-a1-review-findings` so the assessed source remains unchanged.
>
> External Google BRD: [BRD_Spec2Code Draft v1.4](https://docs.google.com/document/d/1M3_2tNUxOXci83pcpPCzBkxwvRvixeT7FYeGyIsFOa4/edit?tab=t.0), revision `AHj4eMQ4PwYGB8UjYlIVceDr2kOWnUey7AtrxhK_PE6-jRNU_wThO1ZHLdgvmNkschru1iMtpUGdl7S0BXL_ALV9JNVsc0s3nFFC8uTWFg`.
>
> **Review type:** evidence-based single-model sequential six-role lens assessment, NOT six spawned independent worker agents, NOT an independent human review. `actualIndependentWorkers=0`, `analyticalLenses=6`, `executionMode=SINGLE_MODEL_SEQUENTIAL`, `independence=LOW`, `humanApproval=UNKNOWN`. No fake reviewer identity, approval, test execution, host access, token/cost benchmark or API worker orchestration is asserted.
>
> **Recommendation:** `BLOCK` for promotion to approved design / implementation; revise the issues below and commission a real, accountable A.1 reviewer. **Formal A.1 status remains `A1_NOT_RUN`**, not an authorized `A1_FAIL` or `A1_BLOCKED` signed result. This preflight gives actionable technical evidence only.

## 1. Reviewer lenses, weighted selection and coverage

All perspectives were evaluated sequentially by one ChatGPT model using the **same evidence pool**. They have no independent memory, isolated host environment, private credentials, or separate model identity. Therefore agreement between lenses is correlated and **not** a quorum, majority vote or independent attestation.

| Lens | Assigned domain | Persona / review mission | Mandatory scope |
| --- | --- | --- | --- |
| L01 | Business analyst / Product | Skeptical — requirements authority and AC clarity | BRD, stakeholder ownership, SRS-01..04 |
| L02 | Software architect / Integrations | Pragmatic — interfaces, lifetime compatibility, dependency order | module contracts, version/schema, workflow, Spec Kit |
| L03 | QA / Test lead | Adversarial — negative cases, acceptance observability and trace | 21 BR, 42 scenario IDs, A1-VAL criteria |
| L04 | Security / Compliance | Compliance-first — P0, trust boundaries, prompt injection and safe STOP | Path Guard, policy, review isolation, RM matrix |
| L05 | Data/Traceability engineer | Analytical — provenance, unique IDs and exact-source lineage | RTM, evidence, review manifest, revision drift |
| L06 | DevOps / Release & Operations | Constructive — Git integration, host/OS rollout, backups and recovery | branch topology, M0–M5, rollout and handoffs |

Proposed planner policy interpreted from master Section 12: domain expertise 0.35; artifact/task fit 0.25; viewpoint 0.15; marginal coverage 0.15; budget feasibility 0.10 (sum=1). These are **design heuristics**, not an executed optimizer, calibrated competence measurement or actual worker allocation. No quantitative reviewer-competence or cost score is claimed. The mandatory software, QA, security, documentation, integration and trace **perspectives** were examined, but no independent expert certification occurred.

## 2. Reviewed source inventory, scope and reproducibility

- Canonical: `.agents/.spec.md` v1.4 Sections 1–17, including SRS-01..12, BR-001..021 and proposed review contracts.
- Specialization: `.agents/.traceMatrix.md`, `.agents/.features.md`, `.agents/.plans.md`, `.agents/.risk.md`, `.agents/.riskMatrix.md`, `.agents/.documents/systemSpecificationPlan.md`, `.agents/.documents/featureDesign.md`, `.agents/.documents/.documentGovernance.md`, `.agents/.workflow/validationSpecification.md`, `.agents/.workflow/testingAndDelivery.md`, `.agents/.workflow/agentRoles.md`, `.agents/.workflow/workflowSpecification.md`, `.agents/.handoffs/plan-089-a1-readiness-handoff.md`, `AGENTS.md`.
- Source contrast (READ ONLY, static): `.source/scripts/workflow_guard.py`, `.source/scripts/path_guard.py`, `.source/scripts/policy_resolver.py`, `.source/.config/workflow.json`. Historic PR #7 defects were used as an investigation lead, not as evidence of a fresh test run.
- Git source and Google revision were read through connected APIs. No local checkout, command execution, Path Guard session, CI, B.1 pilot or actual subagent runner was exercised.
- Static checks: **21 distinct BR rows**, **12 SRS headings**, **42 unique planned acceptance IDs** present in the test catalogue and RTM, **37 base S2C-REQ** rows plus nine NFR rows, nine new RM-025..033 review risk rows. Source presence and identifier coverage are not acceptance evidence.
- Git has stacked Draft PR #8 → PR #9 → PR #10; the default `main` is README-only, and the governance branch diverges from `spec2code/InitialVersion_v0`.

## 3. Evidence-linked findings and proposed disposition

Priority follows the existing L×I risk policy: P0 critical/mandatory blocker; P1 high; P2 medium; P3 low. This review **does not invent new incident likelihood** or override the original RM scores.

### REV-090-01 — P0 / Business authority is unassigned (L01, L04)

**Source:** `.agents/.spec.md:276-280, 327-329`; `.agents/.documents/systemSpecificationPlan.md:18-31, 46-48`; `.agents/.workflow/validationSpecification.md:40,48`.
**Observed:** Requirement owners and stakeholder/security/host/release signatories are explicitly `UNKNOWN`; BR-001..021 are DRAFT. An author cannot independently sign A.1. Any affirmative A.1 or code-authorization claim would be ungrounded.
**Fix:** Identify accountable owners and approval scope; attach source version, decision record, accepted BR/AC and permitted host constraints. Re-run A1-VAL-01/09 under actual authorized reviewer.
**Trace/risk:** BR-002/004/014/021; RM-006/R59-R60; A1-VAL-01/09. **Status: OPEN, AUTHORITY_BLOCKER, high confidence.**

### REV-090-02 — P0 / Security and workflow risk blockers remain open (L02, L04)

**Source:** `.agents/.riskMatrix.md:14-34,95-120`; `.source/scripts/workflow_guard.py` (evaluate/transition); `AGENTS.md:74-78`; `.source/.config/workflow.json`.
**Observed:** RM-001..005 include Path Guard Windows race, policy phase misrouting, source/Spec Kit fingerprint gaps, CLOSE task-scope loss and unowned data collision. Static source inspection confirms `workflow_guard.py` uses `implement` policy routing for IMPLEMENT/VERIFY/HANDOFF and calls CLOSE evaluation without the original task/paths. The runtime phases list has no PAUSED/RESUME. No security owner acceptance or new adversarial run is recorded.
**Fix:** Keep these release and implementation blockers; define separate signed design/host coverage decisions, correct code only in separately authorized B after A.1, test exact SHA with Windows/host race and workflow regression. Review risk ranking in each pass, retaining original scores until actual evidence.
**Trace/risk:** BR-001/002/003/010/011/015; RM-001..005/007; A1-VAL-05/06/07. **Status: OPEN, SAFETY_BLOCKER, high confidence for source/record; exploitability not re-tested.**

### REV-090-03 — P1 / Acceptance cases lack executable precision (L01, L03)

**Source:** `.agents/.workflow/testingAndDelivery.md:26-57`; `.agents/.spec.md:357-373`; `.agents/.workflow/validationSpecification.md:40-43`.
**Observed:** 42 case IDs cover BR-001..021, but most rows are one-sentence positive/adverse scenarios without per-case explicit precondition/fixtures, step sequence, exact observable expected output, assertion or environment. Traceability **structurally exists**, while measurable testability and implementation readiness remain incomplete.
**Fix:** In the existing test catalogue (no new shadow file), add stable per-case setup, procedure, expected outcome/negative error decision, test type, data partition, environment, source-bound evidence and required owner. Specify representative host fixtures and acceptance thresholds, leave unexecutable cases BLOCKED. Do not claim 42 executed tests.
**Trace/risk:** BR-005/021; AC-REV-01..09; A1-VAL-02/03/04; RM-013. **Status: REVISE, high confidence.**

### REV-090-04 — P1 / Review engine and migration contract decisions unresolved (L02, L05, L06)

**Source:** `.agents/.spec.md:209-221,331-355`; `.agents/.features.md:93-106`; `.agents/.documents/systemSpecificationPlan.md:20-30`.
**Observed:** ReviewManifest/Finding/Synthesis contracts, `n/maxWorkers`, quorum, timeout, cost cap, consistency/partial semantics, host output ownership, schema version and compatibility remain proposals. F38..42 have no executable planner/worker/synthesis code or approved storage namespace. A code task cannot yet infer exact public API or host ownership from a proposal.
**Fix:** Produce owner-reviewed versioned JSON schema and state-transition/error table *as design*, enumerate compatibility and safe fallback, confirm quotas, privacy and isolated execution capability. Keep proposed config/output paths uncreated until B authorization; add negative tests to existing case catalogue.
**Trace/risk:** BR-017..021; S2C-REQ-038..042 (PROPOSED); DES-088-01..05; RM-025..033; A1-VAL-04/05. **Status: REVISE/BLOCKED ON OWNER DECISIONS, high confidence.**

### REV-090-05 — P1 / Branch baseline and release target have no accepted decision (L05, L06)

**Source:** repository branch inventory at snapshot; PR #8/#9/#10 Draft; `.agents/.spec.md:254-264,327-329`; `.agents/.plans.md:175-191`.
**Observed:** Actual work is on stacked feature-document branches, not the default `main`. `spec2code/InitialVersion_v0` diverges from governance. No owner-accepted merge base/integration/release candidate is recorded; a docs commit is not a product approval.
**Fix:** Choose approved integration branch and document one migration/merge sequence; review divergent commits, retain both histories, compare exact HEAD and only merge under separately authorized change. Rebind review/CI evidence to the eventual integrated SHA.
**Trace/risk:** BR-014..016; RM-008/009/013; A1-VAL-08. **Status: OPEN DECISION, high confidence.**

### REV-090-06 — P1 / Source-to-stakeholder review revision binding is manual (L01, L05)

**Source:** `.agents/.spec.md:15-32`; Google Doc Draft v1.4 section 23; `.agents/.documents/.documentGovernance.md:23-36`; PLAN-089 handoff.
**Observed:** Google BRD and Git both use v1.4, but the Google stakeholder text is a summary, not a byte-identical technical master. There is no owner-signed pair of exact Git SHA + Google document revision and authoritative changed-BR list for a formal gate. A simultaneous edit may stale the evaluation.
**Fix:** Pin exact Git + Google revisions in the A.1 decision record, compare BR IDs and material statement/AC differences, record divergence list, and invalidate affected evidence when either revision changes. Do not treat matching version labels as sufficient.
**Trace/risk:** BR-005/014/020; RM-003/013/032; A1-VAL-01/03/08. **Status: REVISE, high confidence.**

### REV-090-07 — P1 / No independent A.1 signoff; lenses cannot replace actual workers (L01, L04, L06)

**Source:** `.agents/.workflow/validationSpecification.md:40-54`; `.agents/.workflow/agentRoles.md:59-72`; `.agents/.handoffs/plan-089-a1-readiness-handoff.md:23-38`.
**Observed:** The prior handoff explicitly says A1_NOT_RUN. This PLAN-090 analysis uses one model and six lenses; treating it as six independent agents or an accountable reviewer signature would violate the documented evidence contract. This is a blocker for promotion, not a failure to write a report.
**Fix:** Appoint actual independent reviewer(s), give them snapshot-bound evidence and unmodified findings, use `.agents/.workflow/validationReportTemplate.md` to record A1-VAL-01..09 with reviewer authority, disposition and residual risk. No self-approved status.
**Trace/risk:** BR-004/017/018/019/021; RM-006/025/030; A1-VAL-09. **Status: APPROVAL_BLOCKER, high confidence.**

### REV-090-08 — P2 / Invalid A.1 requirement identifier in SRS (L03, L05)

**Source:** `.agents/.spec.md:319-322` names `A.1-VAL-01..09`, but the canonical matrix is `.agents/.workflow/validationSpecification.md:40-48` with `A1-VAL-01..09`.
**Observed:** One typo creates an invalid trace ID and can break automatic exact-ID scans. Fix required for documentation integrity, but not an observed runtime failure.
**Fix:** Normalize SRS-10 to `A1-VAL-01..09`; add simple exact-ID/link check in documentation preflight.
**Trace/risk:** BR-004/005; A1-VAL-03; RM-013. **Status: REVISE, high confidence.**

### REV-090-09 — P2 / Escaped inline-code markup affects SRS readability/parsing (L03, L05)

**Source:** `.agents/.spec.md:266-375`. For example, source text contains a backslash before each backtick surrounding `UNKNOWN/BLOCKED` and `.specify/`; the static source scan counted **160 backslash-backtick occurrences**.
**Observed:** Markdown backslash escaping causes backticks to be displayed literally instead of using normal inline-code markup. Intended identifiers and paths are harder to scan and may confuse downstream Markdown parsers or automated style checks. The content itself is not invalidated.
**Fix:** Remove only unintended backslash escapes around inline code in SRS-15..17, preserving actual code identifiers and any intentional escapes; render-check the resulting diff.
**Trace/risk:** BR-014; document preflight quality. **Status: REVISE, high confidence.**

### REV-090-10 — P1 / Missing measurable performance and compatibility acceptance baselines (L02, L03, L06)

**Source:** `.agents/.spec.md:299-306,327-329`; `.agents/.documents/systemSpecificationPlan.md:23-30`; `.agents/.workflow/validationSpecification.md:40-47`.
**Observed:** Supported OS/host matrix, n/maxWorkers, quota/latency, benchmark fixtures, timeout and compatibility thresholds remain `UNKNOWN`, correctly not fabricated. As written, B.1 cannot decide PASS/FAIL for these NFRs using measurable owner-approved thresholds.
**Fix:** Define target-host tiers and applicable OS version support, baseline dataset, representative workloads, cost/latency target and quota policy with named owner and source date. Mark unsupported scenarios explicitly restricted/BLOCKED rather than treating them as N/A by default.
**Trace/risk:** BR-013/015/017/021; NFR-003/008/009; RM-008/033; A1-VAL-02/05/07. **Status: REVISE/OWNER DECISION, high confidence.**

## 4. Synthesis, disagreement and risk prioritization

The six lenses use correlated evidence and **no independent votes exist**. They point to the same gate separation: content structure and IDs are mostly present, but source authority, measurable acceptance, safety constraints and real independent signoff are not. No minority blocker is discarded. Severity P0 is retained for already-open security and approval gate classes even though their mitigation is documented. Findings REV-090-01/02/07 remain non-voting blockers.

**Coverage achieved for document preflight:** BR 21/21, SRS 12/12, planned TC 42/42, proposed review risks RM-025..033 present. **Coverage not established:** actual test execution, independent worker reports, host OS/security compatibility, accepted source authority, independent A.1, B.1, calibrated role quality and cost metrics.

**Priority order for correction within documentation scope:** (1) REV-090-01/07 owner and independent approval boundaries; (2) REV-090-02 safety source/risk blockers and exact host scope; (3) REV-090-03/10 measurable AC/TC and host baselines; (4) REV-090-04 review contracts/quotas; (5) REV-090-05/06 branch and source revision binding; (6) REV-090-08/09 formatting and ID typos. This **does not outrank RM-001 for actual code safety**: M1 Path Guard/authorization precedes M3 worker implementation.

## 5. A1-VAL-01..09 technical preflight matrix

This table is a **single-model technical judgement**, not the required per-criterion result signed by an independent reviewer. The actual authoritative A.1 outcome for all nine criteria remains `NOT_RUN`.

| Criterion | Preflight finding | Underlying evidence | Next action |
| --- | --- | --- | --- |
| A1-VAL-01 Source authority | BLOCKER | REV-090-01/06 | owner, approval and exact revision |
| A1-VAL-02 Requirements/AC | REVISE | REV-090-03/10 | measurable AC and budgets |
| A1-VAL-03 RTM | STRUCTURE_PRESENT_WITH_GAPS | 21 BR + 42 TC links; proposed F38..42, no real test | review reverse coverage and evidence |
| A1-VAL-04 Feature design | REVISE | REV-090-03/04 | review contract and negative states |
| A1-VAL-05 Architecture & workflow | REVISE/BLOCKER | REV-090-02/04/10 | accepted interfaces, Windows/host and migration |
| A1-VAL-06 Risk discovery | COVERED_IN_DESIGN | RM-001..033 and source threat classes | security owner re-evaluates completeness |
| A1-VAL-07 Risk management | BLOCKER | REV-090-02; residual UNKNOWN | risk treatment owner, no false downgrade |
| A1-VAL-08 Handoff | PRESENT_WITH_DECISION_GAPS | PLAN-089 dated handoff; PR divergence | pin exact final baseline and owner |
| A1-VAL-09 Independent signoff | BLOCKER | REV-090-07 | authorized real reviewer required |

**Aggregate:** `technicalRecommendation=BLOCK/REVISE`; `formalA1Outcome=A1_NOT_RUN`; `authorizedImplementation=false`; `B1_NOT_RUN`; no human approval or automated evidence promotion.

## 6. Remediation-to-RTM/handoff linkage

| Work package (proposal, not approved B task) | Findings | Existing artifacts to update | Done condition |
| --- | --- | --- | --- |
| PLAN-091-01 approvals and baselines | 01/05/06/07 | master SRS-02/12, document governance, A.1 report | owner and exact revision, real independent signoff |
| PLAN-091-02 testability | 03/08/10 | existing TC catalogue, SRS-10, RTM | 42 cases with observable outcomes/fixtures and correct A1 IDs |
| PLAN-091-03 review and state design | 04/10 | master SRS-06/07/11, featureDesign, risk matrix | constrained schema, quorum, failure handling, budget/host review |
| PLAN-091-04 source safety and scope | 02 | RM-001..005, M1 plan, test scenarios | code work only after B authorization; independently tested |
| PLAN-091-05 document quality | 06/09 | master, provenance/formatting preflight | no escaped literal backticks, linked revisions correct |

## 7. Review limitations, rollback and next gate

- The review **was performed as source inspection and role-perspective reasoning**, not multiple independent agent processes. No separate verified worker contexts, quorum, privacy-isolation tests or empirical confidence-weight calibration were available.
- No project code or existing BRD/RTM/risk/test document is modified by this report. If findings are corrected later, preserve this pinned report unchanged and issue a new re-review record with new source SHA.
- Rollback of the review artifact is a scoped Git documentation revert; it must not delete handoffs/history or alter external host state.
- The next permissible action is to address the document issues and obtain independent A.1 review of the **new exact revision**. A.1 review cannot approve unknown safety and authority conditions, and an A.1 PASS alone would not grant implementation, merge or release permission.
