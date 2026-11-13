# Spec2Code — Planning & Specification Workflow (PLAN-084)

> **Current baseline: PLAN-088 / unified BRD v1.3 (PLAN-087 retained).** Start with [the unified BRD, architecture and M0–M5 implementation plan](../.spec.md). Detailed and historical sections below are supporting references; they do not supersede current scope, evidence or lifecycle mapping.


> **Current project phase: DESIGN_IN_PROGRESS.** This nine-stage **design lifecycle** is distinct from the existing five-phase **runtime-assisted implementation workflow** in [workflowSpecification.md](workflowSpecification.md). This document instructs a human-directed ChatGPT/Codex planning process. It does not add runtime transitions, run tests, modify code or grant permission to merge a PR.

## 1. Purpose and boundary

Plan a universal, repository-scoped S2C agent system from evidence before implementation begins. The planning lifecycle must produce approved, testable requirements; clear feature and interface designs; a traceability matrix; a risk-aware backlog; and a self-contained handoff. Source examples are **observations**, not unreviewed business requirements. Official GitHub Spec Kit owns its feature artifacts; host-owned AGENTS and requirements must not be overwritten.

**Lifecycle A (NOW):** research → specification → design → risks → design review → handoff.

**Lifecycle B (LATER):** authorized code changes → tests → runtime-safe STOP/RESUME implementation → security/OS acceptance → delivery. Existing [five-stage implementation specification](workflowSpecification.md) remains a **design input**, not an instruction to start coding now.

Planning work may be paused and handed off without changing local `.agents/state/workflow-*` or calling `session_guard finish/merge`. A paused design effort is `DESIGN_PAUSED` in human-readable governance only; it is **not** a machine Workflow Guard status.

## 2. Nine planning stages and explicit gates

| # / Stage | Required input | Agent task and minimum output | Exit gate (reviewable) | Rework/stop |
| --- | --- | --- | --- | --- |
| **P1 INTENT_SCOPE** | User goal, selected repository/ref, known permissions | Scope/non-goals, stakeholders, target host vs S2C-dev boundary, working assumptions, version | Task and authorization boundaries recorded; ambiguous requirement labeled OPEN | Scope conflict → stop design decision |
| **P2 SPEC_PLAN** | P1 scope, current S2C specification and feature register | Specification structure, research questions, artifact owners, task plan, definitions of done, acceptance method | Each planned section has owner, deliverable and gate; no coding presumed | Missing authority → NEEDS_REVIEW |
| **P3 RESEARCH_DISCOVER** | P2 questions, observed repository files, relevant official external docs | [Research register](../.documents/researchRegister.md), source provenance and revision, verified facts vs hypotheses vs missing content | Every critical claim traces to a named observed source; uncertainty stated | Conflicting/stale source → reopen source selection |
| **P4 REQUIREMENTS_TRACE** | Approved/observed sources, research gaps | Draft FR/NFR with stable IDs, ACs, priorities, owner, status; [system RTM](../.traceMatrix.md) | Every in-scope requirement has AC/source/feature link or explicitly `NOT_MAPPED` / `PROPOSED`; no inferred approval | Requirements collision → return P2/P3 |
| **P5 FEATURE_DESIGN** | P4 requirement/AC inventory | [Feature design catalogue](../.documents/featureDesign.md): roles, behavior, normal/error flows, inputs/outputs, permissions, alternatives, design trade-offs | Each high-priority feature has coherent boundary and design decision; unresolved decisions owned | Ambiguous behavior → return P4 |
| **P6 ARCHITECTURE_WORKFLOW_DESIGN** | Feature designs, current code contracts and constraints | Component/data/event responsibilities, CLI/JSON contracts, state/transition models, Spec Kit interop, Path Guard constraints, design diagrams | Design covers integration, safety, migration and verification points; no claim of implemented functionality | Unsolvable risk → return P5/P4 |
| **P7 RISK_DISCOVERY** | P1–P6 artifacts plus code/host threat surfaces | Complete candidate risk inventory: scope, security, permissions, data/PII, consistency, OS, integration, governance, provenance, testing and release | Every high-impact design surface considered; risks have scenario, cause, impact and owner | New severe risk → reopen design immediately |
| **P8 RISK_MANAGEMENT_REVIEW** | Risk inventory and draft architecture | [Risk Matrix](../.riskMatrix.md): likelihood 1–5, impact 1–5, exposure, priority, mitigation strategy, residual risk, owner, decision, reopen criteria; design changes and review log | Highest open exposure has actionable mitigation or explicit BLOCKED review; mitigation traced to changed requirement/design | Residual HIGH/P0 → design BLOCKED absent independent acceptance |
| **P9 DESIGN_HANDOFF** | All candidate artifacts and P8 disposition | Design handoff: what was studied, accepted/draft decisions, RTM coverage vs acceptance, open risks, implementation backlog, migration/test plan, rollback and first next step | `READY_FOR_REVIEW` only if package coherent; `APPROVED_FOR_IMPLEMENTATION` only with actual external signoff and remaining risk disposition | Unknown approvals/critical gaps → `DESIGN_IN_PROGRESS` |

Stages are ordered as an **approval dependency**, not a claim that research and risks happen only once. Discovery and Risk Discovery are repeated after material new evidence. Requirements and architecture must not silently change without updating RTM and downstream risk assessment.

## 3. Research and specification contract

Each research claim records `SRC-ID`, path/URL, owner, source type (`AUTHORITATIVE`/`OBSERVED`/`REFERENCE`/`PROPOSED`), version/ref/time, exact question, decision supported and confidence/limitations. Prefer current host/official docs over cached snippets. Do not ingest secrets or raw unnecessary files. A GitHub branch/ref is evidence of observed code, **not** the approval of a requirement.

SRS sections proposed for S2C: mission/scope and exclusions; stakeholder/actor responsibilities; source-of-truth hierarchy; functional requirements; NFRs; state and data model; security boundaries; integration/Spec Kit contract; failure/recovery behavior; observability/test strategy; migration and compatibility; RTM; decision log; risk matrix; approval record. Existing `.agents/.spec.md` is a **draft acceptance contract**, not automatically a complete signed SRS.

For every new functional requirement, use a stable `S2C-REQ-xxx` ID; for nonfunctional use `S2C-NFR-xxx`. Define testable acceptance criteria and record proposed design/task links when created. Do not repurpose Fxx IDs or invent tests. The RTM must remain bidirectional and expose `NOT_MAPPED`, `SPECIFIED` and `BLOCKED` clearly.

## 4. Feature design acceptance

A feature proposal needs: purpose and requirement IDs; actors; permission boundary; observable main path, alternate/error path; inputs/outputs and data classification; impacted existing components/interfaces; candidate design and alternatives; threat model; non-goals; backward compatibility; traceable AC/verification strategy; unresolved decisions and risk IDs. See [catalogue](../.documents/featureDesign.md).

**Agents** at design time are responsibility labels (researcher, analyst, architect, risk assessor, reviewer, handoff owner), not autonomous processes. Their contracts describe read inputs, produced Markdown, policy boundaries and approval needs; there is no implicit delegation, permission or asynchronous executor.

## 5. Risk Discovery and Risk Management are separate

Risk Discovery identifies *what could fail*, including cross-stage failure paths. Risk Management scores *how important it is* and designs a response. Use likelihood `L=1..5`, impact `I=1..5`, `Exposure=L×I`; priority bands: `P0 16..25`, `P1 10..15`, `P2 5..9`, `P3 1..4`. These are **design heuristics**, not measured incident probabilities. Even a small score cannot waive a legally/contractually mandatory security gate.

Every planning pass must: re-evaluate new/changed risks; sort unresolved risks by severity and exposure; select the **highest priority** risk within authorized scope; define mitigation in requirements/design, update affected AC/RTM; re-score **residual risk**, record evidence and owner. Do not mark a risk FIXED merely because a mitigation was written. If mitigation requires Python/host changes, add an implementation backlog item for later approval; do not patch code in the design phase.

For ties, prefer (a) possible repository escape/data loss/unauthorized effects, (b) greater dependency blast radius, (c) lower detectability, (d) less reversible outcomes. Explicit risk acceptance requires an independent authorized reviewer; model analysis alone cannot approve a P0.

## 6. Design decisions and gates

Design statuses are human-document labels: `DRAFT`, `RESEARCHING`, `NEEDS_REVIEW`, `BLOCKED`, `READY_FOR_REVIEW`, `APPROVED_FOR_IMPLEMENTATION`. The last status requires a real human/host signoff with revision and scope; it is not produced by CI, a policy-map entry or this document.

Every stage produces a dated mini-handoff with stage, current doc revisions, evidence, decision IDs, open questions, risk and next stage. A **design STOP** (user stop, time/context limit, risk conflict) produces the same factual handoff, marking `PERSISTED` only if the file really exists. It does not close any local runtime session or authorize coding. At RESUME, recheck the current documents/permissions and revisit stale evidence before advancing.

Do not label a design activity PASS because existing 124 Python tests passed. Tests at a prior SHA verify only exercised runtime test cases. Document validity requires its own structure/trace/authority review.

## 7. Deliverables to hand to the later implementation phase

1. A reviewed SRS with IDs, source owners, ACs, non-goals and authority decisions.
2. RTM with requirement → feature → design → planned task → implementation/test evidence or open gap, and reverse mapping.
3. Feature design catalogue and architecture contracts/diagrams, including failure and recovery/STOP design (only as future runtime requirements).
4. Risk register + scored Risk Matrix, with mitigations, residual P0/P1 and independent decisions.
5. Implementation backlog by dependency and risk priority; test and OS/host migration acceptance plan.
6. Design handoff showing exact source revisions, what is DRAFT vs verified, decisions and first permitted implementation action.
7. Explicit implementation authorization **before** changing `.source/scripts/`, `.source/tests/`, `.source/.config/` or active host state.

## 8. Current baseline and known blockers

PLAN-084 starts with F01–F37 and seven NFR rows already drafted; these do not mean every requirement is approved. Existing five-stage `workflow_guard.py` lacks native PAUSED/RESUME and has open P0/P1 findings in parent PR #7. Windows OneDrive/TOCTOU, host migration and independent approval are OPEN. This design pass prioritizes those gaps in the matrix; it does not fix them.

Related: [plan](../.plans.md), [research](../.documents/researchRegister.md), [feature design](../.documents/featureDesign.md), [risk assessment](../.riskMatrix.md), [RTM](../.traceMatrix.md), [handoff folder](../.handoffs/).

## 9. A.1 Design Validation — mandatory boundary after P9

**Do not enter B from P9 directly.** After A/P1–P9, the separate [A.1 validation process](validationSpecification.md) reviews authoritative requirement sources and approvals, measurable ACs, bidirectional RTM, feature/architecture/STOP designs, security/OS/migration responsibilities, scored P0/P1 risk and handoff completeness. Its [report](validationReportTemplate.md) must record `A1-VAL-01..09` check outcomes with actual evidence/reviewer and a separate implementation authorization decision.

- `A1_PASS` means applicable design checks passed **at an exact document revision**; implementation remains blocked without an actual authorized owner decision `APPROVED_FOR_IMPLEMENTATION`.
- `A1_FAIL` returns to the affected design stage(s), from P2–P9 as appropriate. Update the SRS, RTM, design alternatives, risk priority and handoff; rerun impacted A.1 checks, retaining previous failures.
- `A1_BLOCKED` covers absent source authority, missing approval/evidence, unresolved mandatory P0/P1 or unavailable reviewer; provide a design handoff and stop. `A1_NOT_RUN` is the current state.
- On material source/Spec Kit/host policy changes after A.1 review, invalidate affected A.1 evidence rather than carrying an old PASS forward.

The end-to-end lifecycle is **A → A.1 (validate) → explicit approval → B → B.1 (validate) → explicit release approval**, with risk-based feedback loops. B and B.1 do not become active during PLAN-085. See [B.1 acceptance](validationSpecification.md#3-b1--system-and-acceptance-validation) for the later system validation contract.

## 10. PLAN-086: stack maturity, structure and explicit override in Stage A

At P3 research, inspect **all affected technology types** (Python/runtime/packages, PowerShell editions/modules, SQL **DBMS engine/dialect/driver/migrations**, .NET, containers, other frameworks and CI), whether modifying S2C source or an integrated host. Create `TECH-ID` based on [cross-stack technology policy](../.documents/technologyVersionPolicy.md) and [assessment form](../.documents/technologyAssessmentTemplate.md): official support/EOL, servicing history, production-relevant adoption/toolchain evidence and current project structure. For P5/P6 choose a mature supported mainstream default **unless the user explicitly overrides it**. For override record `OVR-ID`, exact repository/ref, user-selected version/structure, compatibility/security/migration risk, and any required independent approval using [override form](../.documents/technologyOverrideTemplate.md).

P7/P8 risk discovery/management assesses immature major churn, EOL support, dialect/edition mismatch, legacy migration and override misuse. A.1 checks the decision against the host policies and `S2C-NFR-008/009` without requiring a new major merely because one exists. Risk and permission constraints can BLOCK a user-preferred EOL/preview deployment, but a supported newly GA major may be a valid explicit **design target**; it never triggers code changes in the current design phase.
