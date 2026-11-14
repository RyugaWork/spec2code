# Spec2Code — System Specification Authoring Plan (PLAN-084)

> **Current authoring: PLAN-103 documentation candidate, while runtime remains v0.7.0.** The [unified master](../.spec.md), [RTM](../.traceMatrix.md), [test catalogue](../.workflow/testingAndDelivery.md) and [A.1 gates](../.workflow/validationSpecification.md) are the current design sources. Older PLAN-084..102 material is retained for provenance, not approval.


> **Draft plan**, not an approved System Requirements Specification and not permission to implement. The existing `.agents/.spec.md` is a partial acceptance contract. This plan tracks acceptance and review of the 12 SRS chapters now consolidated into [the master Section 15](../.spec.md); it does not create a competing SRS or change source code.

## 1. Specification ownership and required evidence

- Development SRS owner: designated Spec2Code project maintainer/stakeholder. The agent may draft, cross-reference and flag conflicts but **cannot approve** a new requirement.
- Sources: [research register](researchRegister.md), [feature register](../.features.md), [system RTM](../.traceMatrix.md), [Path Guard](../../docs/PATH_GUARD.md), [workflow design](../.workflow/workflowSpecification.md), [planning lifecycle](../.workflow/planningSpecificationWorkflow.md) and [risk matrix](../.riskMatrix.md). Host rules and upstream Spec Kit artifacts have independent authority.
- Each FR/NFR requires unique ID, statement, rationale, provenance, owner, priority, acceptance criteria, draft/approved state, impacted feature/agent/interface, risk refs, positive/negative verification design and open decisions.
- A design document is **PROPOSED** until the responsible reviewer approves the exact revision; observable source behavior cannot authorize a business rule.

## 2. SRS chapter content inventory and open decisions

| Section | Content and minimum questions | Supporting evidence | Readiness |
| --- | --- | --- | --- |
| SRS-01 Purpose & scope | Problem, users, installed-host vs development repository, goals, exclusions | SRC-001/002/013 | CONTENT_DRAFT |
| SRS-02 Authority & actors | Requester, host owner, agent role, security/reviewer; who approves what | SRC-001/002/008/016 | CONTENT_DRAFT; OWNER_UNKNOWN |
| SRS-03 Use cases & failures | Discovery, planning, routing, implementation later, review, interruption and recovery | SRC-003/004/005, feature designs | CONTENT_DRAFT |
| SRS-04 Functional requirements | F01–F37 and approved behavior, inputs/outputs, error conditions, independent authority | SRC-003/006 | CONTENT_DRAFT; AC_REVIEW |
| SRS-05 Nonfunctional requirements | Checkout containment, privacy, data integrity, performance bounds, OS/host compatibility, reliability | SRC-007/009/011/014 | CONTENT_DRAFT; SLO/OS_UNKNOWN |
| SRS-06 Interface and data contracts | CLI/JSON schemas, state/events/handoff records, file ownership, version/compatibility | SRC-008/009/010/011/013 | CONTENT_DRAFT; SCHEMA_PROPOSED |
| SRS-07 Feature/architecture design | Modules and dependencies, operation boundaries, alternatives, design decisions | featureDesign.md and implementation observations | CONTENT_DRAFT; DESIGN_REVIEW |
| SRS-08 Lifecycle and Spec Kit | Nine-stage planning, separate five-stage implementation workflow, upstream artifact authority | planningSpecificationWorkflow.md, SRC-004/010/015 | CONTENT_DRAFT |
| SRS-09 Risk, safety and recovery | Threat model, risk matrix, STOP design/handoff, authorization and fail closed | riskMatrix.md, SRC-005/014 | CONTENT_DRAFT; RISK_OPEN |
| SRS-10 Verification and RTM | Requirement→AC→feature→design→task→test, positive/negative cases, CI vs security gate | SRC-006/012 | CONTENT_DRAFT; TESTS_NOT_RUN |
| SRS-11 Migration, rollout, rollback | Legacy sessions and host state, OS concerns, version support, reverse migration and fallback | SRC-009/013/014 | CONTENT_DRAFT; ROLLOUT_BLOCKED |
| SRS-12 Decision/approval log | Approved source revisions, external reviewer decisions, unresolved assumptions | researchRegister.md, riskMatrix.md | CONTENT_DRAFT; SIGNOFF_UNKNOWN |

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

Current status: `SRS-01..12_CONTENT_DRAFT` in the master; host-specific evidence, owner decisions, exact acceptance targets and A.1 approval remain open. **No runtime source edits** authorized by this plan.

## 5. A.1 validation after the SRS has been drafted

SRS-01..12 and the system RTM must undergo the [A.1 Design Validation](../.workflow/validationSpecification.md) against `A1-VAL-01..09`: authority, requirement clarity, traceability, feature flows, architecture, security/integration/migration, risk management and handoff. Prepare a [review report](../.workflow/validationReportTemplate.md) identifying source revisions and failed/blocked criteria. A.1 cannot PASS simply because 12 chapters were listed; chapters are still draft, and several P0 risks remain open. On FAIL return to the relevant SRS section and planning step, not to Python code. Current result: `A1_NOT_RUN`.

## 6. PLAN-086: support baseline and explicit-request exception requirements

SRS-05/06/07/10/11 shall cover `S2C-NFR-008` (supported mature mainstream technology/structure selection) and `S2C-NFR-009` (explicit user override with scope, risk, evidence and separate authority). Apply to **S2C's own source/tooling plus integrated host source**, including Python versions and wheels, PowerShell edition/module lifecycles, SQL **engine/dialect/driver/migration** support, .NET and other stacks. Use [policy](technologyVersionPolicy.md), [assessment](technologyAssessmentTemplate.md) and [override record](technologyOverrideTemplate.md). No global hardcoded version list is normative; source evidence must be refreshed per proposal.

A supported newly GA stable major may be a user-designated choice when the user explicitly asks; an EOL/preview/high-risk choice needs documented extra security/host approval and may remain BLOCKED. Conservative defaults must not silently override an explicit user requirement. No request for a version alone authorizes changing Python, PowerShell, SQL, host dependencies or data. A.1 and B.1 review gates are NOT RUN; this is a specification plan only.

## 7. PLAN-089 phased document completion report (non-approval)

| Phase | Document deliverable | Current evidence / status |
| --- | --- | --- |
| A0 source/ownership | Existing branch/tree reviewed, unified master, conflicts and separate host ownership | DRAFT_RECONCILED; PR review still required |
| A1 requirements/SRS | Master [SRS-01..12](../.spec.md) contains all 12 substantive chapters with explicit UNKNOWN/BLOCKED | CONTENT_DRAFT, not owner-approved |
| A2 interfaces/workflow | Master Section 16 specifies producers/consumers, data/manifest/finding/synthesis/STOP contracts and negative behavior | DESIGN_DRAFT; implementation API/schema not created |
| A3 acceptance & RTM | [42 planned positive/negative cases](../.workflow/testingAndDelivery.md), [RTM Section J](../.traceMatrix.md) maps 21 BRs | DESIGNED/NOT_RUN; no tests executed |
| A4 risk/recovery | Existing RM-001..033 and historical R risks preserved, priority and decisions in master | MITIGATION_DESIGNED; verified residual UNKNOWN |
| P9 handoff | [PLAN-089 review handoff](../.handoffs/plan-089-a1-readiness-handoff.md), exact branch/evidence and open signoffs | PREPARED, A.1 NOT_RUN |

**Pending owner decisions:** BR-001..021 approval; technical SRS source of truth for production adoption; accepted n/budget/role coverage and support matrix; schema compatibility and review output namespace; Path Guard Windows attack surface; implementation milestone owner and rollout restriction. Current document package is suitable for a **human A.1 review**, not `A1_PASS` or `APPROVED_FOR_IMPLEMENTATION`. Never use a static completeness checklist to assert reviewed security or compatibility.

## 8. PLAN-102 — Authoring exit checklist and ownership queue

The SRS and system planning content is **author-complete as a candidate** when every active design item has one canonical home, a requirement/feature and risk owner (or explicit UNKNOWN), planned positive/negative observables, reverse RTM, version/host assumptions, recovery/STOP and a bounded handoff. [Master Section 27](../.spec.md#27-plan-102--documentation-authoring-closure-and-bounded-implementation-blueprint) contains the unified exit rule; [A.1 packet](../.workflow/validationSpecification.md#9-plan-102--independent-a1-review-packet-and-criteria) contains the independent test.

| Remaining non-authoring decision | Accountable party needed | Current result |
| --- | --- | --- |
| BR-001..027 approval, especially candidate BR-022..027 | Business/product owner | UNKNOWN |
| Git master and Google BRD accepted semantics/revision | Document/product owner | DRIFT OPEN until mirror reviewed |
| Threat model, external data, Windows sandbox and P0 mitigation | Host/security owner | OPEN |
| Proposed ADR-102 and DEC-091/101 ownership, quotas and version selections | Architecture/tool/QA owners | PROPOSED |
| A.1 independently signed report on exact pair | Authorized independent reviewer | NOT_RUN |
| Phase-B work scope, test environment and command authority | Requester + host/security owner | NOT_AUTHORIZED |

Do not treat missing human decisions as unfinished drafting that an agent can invent. If author-side static checks pass and open owner decisions are explicitly registered, label the package `AUTHORING_COMPLETE_CANDIDATE / A1_REVIEW_PENDING`, never `A1_PASS` or `IMPLEMENTATION_READY`.

### 8.1 Owner-ready decision evidence packet (do not self-approve)

The requested *documentation drafting* work is complete as a candidate; the following **external** decisions cannot be inferred or signed by the author-model. Record each as an actual source-bound decision in the existing [validation report template](../.workflow/validationReportTemplate.md) and [PLAN-103 owner handoff](../.handoffs/plan-103-owner-review-packet.md), with `decision=ACCEPT|REVISE|BLOCK`, reviewer identity/authority, Git SHA, Google BRD tab/revision and evidence. PENDING is not ACCEPT.

| Decision area | Minimum observed inputs to request | Accountable role and stop condition |
| --- | --- | --- |
| BRD and acceptance | Current master BR-001..027, proposed BR-022..027, 22 F43..64 rows, 44 candidate TC-F IDs, Google BRD Draft; explicit accepted/excluded scope and numeric owner-selected ACs | Business/product owner; lack of signed ownership → BLOCKED |
| Architecture and technology | ADR-102-01..08, DEC-091/101, runtime/host versions and supported-maturity evidence, requested overrides | Architecture/technology owner; compatibility, policy or ownership UNKNOWN → REVISE/BLOCK |
| Security and data sharing | RM-001..005 and RM-047..052, Windows path/junction and sandbox threat model, secrets/remote-provider disclosure, negative fixtures and residual-risk justification | Host/data/security owner; unaccepted P0 → BLOCK |
| Provider and execution | Actual approved OS/worktree, Codex `--version` and `exec --help`, state DB permissions, MCP server package and tool list, authentication and network/data scope, retry/cost/timeout budget | Host tool operator and security owner; unverified commands/provider or unsafe sandbox → BLOCK |
| Independent A.1 | Exactly pinned Git output SHA + Google tab/revision, BR/AC decisions, A1-VAL-01..09, risk/ADR packet, review report and dissent | Named independent reviewer; NOT_RUN or source drift → no A1_PASS |
| Phase-B / release | A1_PASS evidence and a distinct written implementation scope, test environments, Path Guard restrictions, owners, rollback and later B1-VAL-01..09 evidence | Requester/maintainer/release authority; no separate B and B.1 approvals → no implementation/merge/release |

**This is an owner action queue, not an automatic signature form or a new normative SRS.** [The original report template](../.workflow/validationReportTemplate.md) remains the single place to record a real review, and [handoff](../.handoffs/plan-103-owner-review-packet.md) preserves the current source evidence. No host CLI or Gemini/MCP probe occurred in this documentary pass.

## DOC-A02 — Owner decision completeness for exact-revision A.1

Use the **existing** [validation report template](../.workflow/validationReportTemplate.md) rather than creating a second approval ledger. Each open owner decision must provide: `decisionId`, named owner and proof of scope of authority, `ACCEPT|REVISE|BLOCK`, exact Git SHA, Google doc ID/tab/revision when applicable, the affected BR/REQ/feature IDs, alternatives considered, security/compatibility evidence, date, expiry/revisit trigger and a verifiable signature/reference. A `PENDING` proposal is *not* an `ACCEPT` decision.

For business approval, ask the owner to disposition **each** of BR-022..027 (accept/exclude/reword) and identify quantitative acceptance where the design intentionally leaves host/environment values open. For security, ask the host owner to decide real Windows/macOS/Linux scope, external-provider disclosure, sandbox and negative cases **per P0**. For review, require one independently accountable A.1 reviewer with access to the exact Git/Google pair; the author-model's sequential lenses are not independent. Until all these records exist, record `OWNER_PENDING / A1_NOT_RUN`, not `IMPLEMENTATION_READY`.
