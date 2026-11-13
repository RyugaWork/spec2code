# PLAN-084 — Planning & Specification Design Handoff

> **Status: DESIGN_IN_PROGRESS — NOT APPROVED_FOR_IMPLEMENTATION.** This is a planning-stage record, not a local runtime session CLOSE/FINISH or a code implementation certificate.

- **Recorded:** 2026-11-13, Asia/Ho_Chi_Minh.
- **Repository / PR:** `RyugaWork/spec2code`, [stacked Draft PR #8](https://github.com/RyugaWork/spec2code/pull/8) on [Draft PR #7](https://github.com/RyugaWork/spec2code/pull/7).
- **Working branch:** `feat/agent-governance-v0.8.0`.
- **Design audit source SHA:** `72e7926456948bba276269a537093e3c455f2006` (this handoff is added by a subsequent documentation commit).
- **Explicit scope decision:** user clarified **design-first**, consisting of specification plan, content/source discovery, feature design, architecture/workflow design, Risk Discovery, Risk Management and handoff. Runtime STOP/RESUME and coding are **later phase** tasks; no code implementation under PLAN-084.
- **Permissions:** review and authored Markdown design updates on this working branch. No runtime code/config/test mutation, host migration, Spec Kit stage execution, independent review signoff, release/merge approval or deployment.

## 1. Design work completed as draft (not implementation)

| Planning stage | Deliverable and evidence | Status / pending decision |
| --- | --- | --- |
| P1 INTENT_SCOPE | [PLAN-084](../.plans.md) and root [AGENTS](../../AGENTS.md) explicitly identify design-only scope | DRAFT; owner adoption required |
| P2 SPEC_PLAN | [SRS authoring plan](../.documents/systemSpecificationPlan.md), 12 proposed chapters with evidence/gaps | DRAFT; full SRS not approved or complete |
| P3 RESEARCH_DISCOVER | [Research register](../.documents/researchRegister.md), `SRC-001..016` provenance and `RQ-084-01..08` questions | IN_PROGRESS; official upstream/version and host authority need current review |
| P4 REQUIREMENTS_TRACE | Existing [system RTM](../.traceMatrix.md), F01–F37 / seven NFRs plus `DS-084-P1..P9` deliverable trace | DRAFT; coverage not acceptance |
| P5 FEATURE_DESIGN | [Feature catalogue](../.documents/featureDesign.md), D01..D07 areas and DES-084-01..06 proposed choices | IN_PROGRESS; detailed high-risk feature design cards needed |
| P6 ARCHITECTURE_WORKFLOW_DESIGN | [Nine-stage planning lifecycle](../.workflow/planningSpecificationWorkflow.md), separate [later five-stage implementation workflow](../.workflow/workflowSpecification.md) | DRAFT; integration review not signed |
| P7 RISK_DISCOVERY | Initial [risk matrix](../.riskMatrix.md) covering 14 failure scenarios in major categories | DRAFT; threat coverage review pending |
| P8 RISK_MANAGEMENT_REVIEW | Proposed L1–5 × I1–5 model, P0/P1/P2/P3 thresholds; pass 01 prioritization | IN_PROGRESS; estimates not measured, residual mitigation not verified |
| P9 DESIGN_HANDOFF | This design handoff and [reusable template](../.workflow/designHandoffTemplate.md) | RECORDED as draft; no approval for implementation |

## 2. Initial Risk Management pass

| Risk | L × I = E | Priority | Disposition / design mitigation |
| --- | --- | --- | --- |
| `RM-001` Windows junction/path race and unintended external files | 4 × 5 = 20 | P0 | Highest risk pass 01; design requires OS security boundary or isolation and hostile sentinel tests; OPEN |
| `RM-002` VERIFY/HANDOFF policy mapping defect in PR #7 | 5 × 4 = 20 | P0 | Specify operation-specific phase gate and negative cases; OPEN |
| `RM-003` Stale source/Spec Kit evidence accepted after VERIFY | 5 × 4 = 20 | P0 | Specify complete provenance/fingerprint invalidation; OPEN |
| `RM-004` CLOSE loses task/scope | 5 × 4 = 20 | P0 | Specify full-scope CLOSE and end-to-end lifecycle acceptance; OPEN |
| `RM-005` Colliding or migrated generated files cause data/evidence loss | 4 × 5 = 20 | P0 | Require ownership preflight, backups and exact-session safeguards; OPEN |
| `RM-006..014` Other authority, STOP/resume, migration, integration and evidence risks | See matrix | P0–P2 | Mitigation ideas are DESIGNED/OPEN, not VERIFIED |

**Highest-risk mitigation outcome this pass:** a **design-level acceptance requirement** for RM-001 was recorded; no OS containment patch or adversarial runtime test was performed. Original R01 stays OPEN and the residual exposure is **UNKNOWN**, not lowered. Additional P0 risks must be addressed by future design passes before implementation review.

## 3. Evidence and verification

- Source/design audit baseline `72e7926`: planning stage references P1..P9, `SRC-001..016`, `RQ-084-01..08`, risk `RM-001..014`, and existing F01–F37/NFR trace.
- GitHub repository tree link audit on **16 reviewed files** (the seven newly authored/modified core artifacts and nine synchronized source docs): zero missing internal Markdown link destinations.
- This PLAN-084 sequence updates **Markdown only**, not `.source/scripts/*.py`, `.source/tests/*.py`, or `.source/.config/*.json`.
- **Runtime tests:** NOT RUN as part of design; older CI success is neither a signed requirements approval nor a security fix. A PR CI run can report Python regression compatibility only for its exact SHA.
- **Human approval:** NOT OBTAINED. This stage does not approve the design, change machine workflow status, or authorize merging PR #8/#7.
- **Outstanding correctness:** parent PR #7 P0 CLOSE scope, VERIFY/HANDOFF operation and source/spec stale invalidation, P1 status; Windows/OneDrive hostile races and legacy session migration remain OPEN.

## 4. Next design iteration — smallest safe steps

1. Confirm design stakeholders and authority for the 12 SRS chapters; record **approved** versus **proposed** requirements and host-independent invariants.
2. For the highest risk `RM-001`, write a detailed Threat Model / containment alternatives / measurable Windows adversarial acceptance plan. Update any affected S2C-NFR and record the residual risk proposal; **do not change Python**.
3. Develop DES-084 feature design cards for `RM-002..005`, including exact state diagrams, API and compatibility implications and negative test plans.
4. Reevaluate L/I for every changed risk after each research/design pass; keep `P0` blockers as OPEN until independent review and actual later implementation evidence.
5. Reconcile updated design/RTM/SRS, then produce another dated design handoff with exact source revisions.
6. Seek explicit human `READY_FOR_REVIEW` then `APPROVED_FOR_IMPLEMENTATION` decision only when appropriate; no status inferred from a handoff.

**Handoff persistence:** this file is a versioned document in the development branch. Reviewers should use its actual Git commit/ref before treating it as durable; no host session state was created or closed. Do not overwrite previous handoffs.

**Rollback:** revert the PLAN-084 Markdown commits only; never delete host state, original handoffs, `specs/`, `.specify/` or history. Leave Draft PR #7 and PR #8 unmerged.
