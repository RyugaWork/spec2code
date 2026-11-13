# Spec2Code — System Specification Authoring Plan (PLAN-084)

> **Draft plan**, not an approved System Requirements Specification and not permission to implement. The existing `.agents/.spec.md` is a partial acceptance contract. This plan defines how to transform evidence into a coherent, reviewable SRS without changing source code.

## 1. Specification ownership and required evidence

- Development SRS owner: designated Spec2Code project maintainer/stakeholder. The agent may draft, cross-reference and flag conflicts but **cannot approve** a new requirement.
- Sources: [research register](researchRegister.md), [feature register](../.features.md), [system RTM](../.traceMatrix.md), [Path Guard](../../docs/PATH_GUARD.md), [workflow design](../.workflow/workflowSpecification.md), [planning lifecycle](../.workflow/planningSpecificationWorkflow.md) and [risk matrix](../.riskMatrix.md). Host rules and upstream Spec Kit artifacts have independent authority.
- Each FR/NFR requires unique ID, statement, rationale, provenance, owner, priority, acceptance criteria, draft/approved state, impacted feature/agent/interface, risk refs, positive/negative verification design and open decisions.
- A design document is **PROPOSED** until the responsible reviewer approves the exact revision; observable source behavior cannot authorize a business rule.

## 2. Planned SRS chapters and completion criteria

| Section | Content and minimum questions | Supporting evidence | Readiness |
| --- | --- | --- | --- |
| SRS-01 Purpose & scope | Problem, users, installed-host vs development repository, goals, exclusions | SRC-001/002/013 | DRAFT |
| SRS-02 Authority & actors | Requester, host owner, agent role, security/reviewer; who approves what | SRC-001/002/008/016 | NEEDS_REVIEW |
| SRS-03 Use cases & failures | Discovery, planning, routing, implementation later, review, interruption and recovery | SRC-003/004/005, feature designs | DRAFT |
| SRS-04 Functional requirements | F01–F37 and approved behavior, inputs/outputs, error conditions, independent authority | SRC-003/006 | PARTIAL |
| SRS-05 Nonfunctional requirements | Checkout containment, privacy, data integrity, performance bounds, OS/host compatibility, reliability | SRC-007/009/011/014 | PARTIAL |
| SRS-06 Interface and data contracts | CLI/JSON schemas, state/events/handoff records, file ownership, version/compatibility | SRC-008/009/010/011/013 | NEEDS_REVIEW |
| SRS-07 Feature/architecture design | Modules and dependencies, operation boundaries, alternatives, design decisions | featureDesign.md and implementation observations | DRAFT |
| SRS-08 Lifecycle and Spec Kit | Nine-stage planning, separate five-stage implementation workflow, upstream artifact authority | planningSpecificationWorkflow.md, SRC-004/010/015 | DRAFT |
| SRS-09 Risk, safety and recovery | Threat model, risk matrix, STOP design/handoff, authorization and fail closed | riskMatrix.md, SRC-005/014 | PARTIAL |
| SRS-10 Verification and RTM | Requirement→AC→feature→design→task→test, positive/negative cases, CI vs security gate | SRC-006/012 | PARTIAL |
| SRS-11 Migration, rollout, rollback | Legacy sessions and host state, OS concerns, version support, reverse migration and fallback | SRC-009/013/014 | BLOCKED |
| SRS-12 Decision/approval log | Approved source revisions, external reviewer decisions, unresolved assumptions | researchRegister.md, riskMatrix.md | NEEDS_REVIEW |

**Readiness terms describe document completion**, not code test outcomes. Do not silently classify an SRS chapter APPROVED without human/host evidence.

## 3. Planned authoring order

1. Lock scope and source ownership in SRS-01/02, then answer high-priority research questions `RQ-084-01..08`.
2. Consolidate approved requirement statements from the existing spec/feature register; write missing ACs and mark speculative behavior `PROPOSED`.
3. Attach current RTM mapping, avoid creating fictitious tests/tasks; surface all gaps/blocked requirements.
4. Produce feature design cards, API/CLI/state diagrams, and explicit design decisions before implementation.
5. Run separate Risk Discovery and Risk Management, updating priority/residual and the design backlog.
6. Review content for source agreement, internal consistency, testability, security ownership and release restrictions.
7. Create a **design handoff**, preserving remaining decisions, approvals, biggest risks and exact next permitted action.

## 4. Definition of done for the specification package

A SRS is only `READY_FOR_REVIEW` when its 12 chapters are supplied with evidence or explicit `UNKNOWN/BLOCKED` disposition, every active feature has RTM trace, all security/data/OS ownership gates are enumerated, high-priority designs have alternatives and failure cases, and a scored matrix/handoff exists. It becomes `APPROVED_FOR_IMPLEMENTATION` **only** after the responsible human/host approves a revision and treats mandatory P0/P1 risk as blocking or explicitly accepts it.

Current status: `SPEC_PLAN_COMPLETE_AS_DRAFT`; full SRS authorship, host evidence and approval remain open. **No runtime source edits** authorized by this plan.

## 5. A.1 validation after the SRS has been drafted

SRS-01..12 and the system RTM must undergo the [A.1 Design Validation](../.workflow/validationSpecification.md) against `A1-VAL-01..09`: authority, requirement clarity, traceability, feature flows, architecture, security/integration/migration, risk management and handoff. Prepare a [review report](../.workflow/validationReportTemplate.md) identifying source revisions and failed/blocked criteria. A.1 cannot PASS simply because 12 chapters were listed; chapters are still draft, and several P0 risks remain open. On FAIL return to the relevant SRS section and planning step, not to Python code. Current result: `A1_NOT_RUN`.
