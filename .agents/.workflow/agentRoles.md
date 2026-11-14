# Agent responsibilities — PLAN-081 (v0.8 candidate)

This is a **role protocol for a single human-directed ChatGPT/Codex agent or explicitly delegated reviewers**. It is not a fleet of running subagents. No role receives new credentials, shell authority, repository access, or an approval signature merely by being named.

## Roles and outputs

| Logical role | Trigger / evidence inputs | Deliverable | Decision boundary |
| --- | --- | --- | --- |
| **Task coordinator** | User request, actual repo scope, available tools | Scope, action permission, phase, task ID, known blockers | Does not infer Git/write consent from a request to read/review |
| **Requirements analyst** | Host requirements, `.agents/.spec.md` (development), relevant Spec Kit `spec.md` | Requirement/AC map, ambiguity list, provenance and approval status | Cannot invent business rules or approve a draft |
| **Architecture & policy analyst** | Root/nested AGENTS, policy map, existing code, graph, API/data/security contracts | Affected-path map, implementation risks, policy conflicts | Policy selection is read-only, not authority |
| **Implementation engineer** | Approved scope, plan/tasks, observed code and configuration, active local session as required | Minimal changed paths with provenance | No auto-commit, migration, shell, external file edits or undeclared scope |
| **Test & evidence reviewer** | AC IDs, actual build/test output, exact revision and platform | PASS/FAIL/BLOCKED/NOT RUN ledger, regressions and unresolved cases | Does not assert a test was run from a proposed command |
| **Security & ownership reviewer** | Path Guard/Scope IO, sensitive paths, permissions, host policy, risk register | Security impact, mitigations, acceptance blockers | Human authorization and independent security signoff remain external |
| **Handoff custodian** | File diff, exact session, approvals, test record, `.agents/.handoffs/` | Reviewed handoff, rollback and pending work | No self-approval or silent deletion/merge |

These roles may be fulfilled sequentially by one agent. For high-risk changes, an **independent human reviewer** must make the acceptance decision; repeating a review in the same model conversation is not independence.

## GOV-20261114 — Executor routing and reviewer independence

Each task has one executor label, [GPTWEB] for requirements, reviews, impact/risk matrix, checkpoints and authorized remote documentation, or [CODEX] for actual local repository inspection/edits, commands, tests, security probes and Git execution. [AUTO] is a routing directive, not a third executor or permission tier. It may dispatch an authorized READY Codex task only through a verified live provider; otherwise issue HANDOFF_REQUIRED, preserving task IDs and evidence. See [root contract](../../AGENTS.md#active-agent-contract--read-first).

The coordinator requires task ID, phase, source SHA, requirements/AC, dependencies, priority, assigned writer, permitted and forbidden paths, action permissions, expected result, failed result/rollback, budgets, evidence and status. Parallel reviewers use immutable source; a single integrator owns shared writes. Independent A.1 review, owner risk acceptance and Phase-B authorization are external decisions, not GPTWEB/CODEX self-certifications. A simulated persona or sequential same-model review has independentWorkers=0.

## Assignment and escalation

1. Classify the request as READ, PLAN, IMPLEMENT, VERIFY or DELIVERY. An ambiguous action cannot be elevated to a write merely to complete a workflow.
2. Collect only the relevant root/nested AGENTS and domain-specific policy/requirement sources. Use the real task description and verified affected paths; classify undocumented assumptions as `UNKNOWN`.
3. Requirements/policy conflicts go back to the responsible host owner. Missing source or an unsafe path blocks the affected operation. Source observations do not grant business approval.
4. Risk changes are checked by the security role even when the context router picks `minimal`; context budget is not a safety waiver.
5. An implementation reviewer may propose code and tests only within the authorized scope. New requirements or new paths require a scope update and fresh gate review.
6. A test reviewer can attest only to logs/output that were actually observed, bound to a source revision. Draft tests and archived logs are not present-tense PASS.
7. Handoff is a transfer of evidence, not a release authorization. A human/host gate owns merges and releases.

## Domain authority matrix

| Question | Look first | Do not substitute |
| --- | --- | --- |
| S2C development requirement | `.agents/.spec.md`, feature register and approved plan | A speculative ticket or source comment |
| Installed host business behavior | Host's approved business spec/requirements | S2C sample templates or inferred code |
| Active Spec Kit feature | Verified `.specify/feature.json` / override, `spec.md`/`plan.md`/`tasks.md` | Git branch guess, generated context pack |
| Code behavior | Exact current source, build/runtime evidence | Architecture hints alone |
| Security/authorization | Host policy, applicable AGENTS, explicit owner/reviewer | `policy-map.json`, `READY`, an agent's assertion |
| Deployment/merge | Explicit user permission, current repo policy and reviewed evidence | Workflow journal, CI green status alone |

## Stage evidence contract

For each decision, preserve: task/requirement IDs; exact repository/ref; observed paths; consulted authority documents and unresolved conflicts; authorized action; stage; test command/platform/exit status when run; result (`PASS`, `FAIL`, `BLOCKED`, `NOT RUN`, `SKIPPED`); external approval source if one exists; unresolved risks and next owner. Avoid copying credentials, raw private task text or full source bodies into machine evidence.

If the agent cannot access a local worktree, say so. A remote GitHub file review is still useful, but cannot be reported as a locally guarded session or successful local test. See [runbook](agentRunbook.md), [source policy](../.documents/.documentGovernance.md), and [delivery](testingAndDelivery.md).

## PLAN-084 planning-only role allocation

During P1–P9, the coordinator frames scope and planned deliverables; research analyst maintains `SRC-ID` provenance; requirement analyst prepares AC/RTM; designer creates feature/architecture decision cards; risk analyst discovers and scores scenarios; independent reviewer can request changes; handoff custodian records stage evidence. **These are sequential human-supervised responsibilities, not live workers.** The implementation engineer and test executor are future-phase roles and must not begin coding or testing merely because a design decision was drafted. See the [planning workflow](planningSpecificationWorkflow.md), [research](../.documents/researchRegister.md), [feature design](../.documents/featureDesign.md) and [risk matrix](../.riskMatrix.md).

## PLAN-085 validation responsibilities

A.1 is checked by a **design/requirements reviewer** independent of the design author wherever external signoff is required; B.1 uses real test/host/security and stakeholder evidence rather than only the implementation author's self-report. The interactive agent may gather sources, prefill a [validation report](validationReportTemplate.md) and map gaps to the [RTM](../.traceMatrix.md); it cannot self-certify approval or fabricate a test runner. Failures reopen the affected prior lifecycle, and both validators preserve the source revision and risk scores. See [gate specification](validationSpecification.md).

## PLAN-086 universal version and override responsibility

The architecture/policy analyst evaluates **Python, PowerShell, named SQL engines/drivers/migrations, .NET, CI/tooling and other stacks** for both **S2C source** and **integrated host code** using [technology policy](../.documents/technologyVersionPolicy.md) and [candidate assessment](../.documents/technologyAssessmentTemplate.md). The requirement analyst links `S2C-NFR-008/009` to affected host/system requirements; the risk analyst scores support/novelty/compatibility/override risks. If the requester explicitly selects another supported stable version/structure, the coordinator captures [OVR-ID](../.documents/technologyOverrideTemplate.md) and passes that exact choice to design rather than ignoring it. The authoring agent cannot approve its own exception, bypass security or convert the override into permission to edit files. A.1/B.1 reviewers validate actual evidence when scheduled; both are currently NOT RUN.


## PLAN-088 — Domain-adaptive review roles and bounded personalities

The role catalogue supports a **future** multi-agent review service and present-day **explicitly labeled sequential lenses**. A named role/persona is a prompt/checklist responsibility, not a real expert credential, new tool permission or independent signoff.

| Artifact/domain | Expert coverage examples | Required assessment |
| --- | --- | --- |
| Software feature/code | Developer, architect, QA/tester, security, SRE/DevOps | Functional correctness, negative cases, architecture, security, deployment compatibility |
| Data pipeline/model | DA, DE, DS, DB/SQL, data quality/privacy | Lineage, schema/drift, correctness, tests, leakage, reproducibility |
| BRD/specification/UX | BA/product, domain specialist, QA, UX/accessibility, compliance | Source authority, AC testability, trace, accessibility, privacy/obligations |
| Mixed artifacts | Union of applicable domains selected from the actual evidence | Mandatory covered risk-specific roles; unsupported competency => GAP/BLOCK |

Review personalities: skeptical (test assumptions), adversarial (find abuse/negative cases), constructive (improve completeness), pragmatic (feasibility/cost), compliance-first (governance/security), exploratory (edge cases). Selection combines expertise fit 35%, task fit 25%, perspective 15%, marginal coverage 15% and budget feasibility 10% **as proposed design defaults**, subject to versioned config and A.1 review. Constraints (mandatory role coverage/security, ownership, permissions, quota) are not traded for score. Worker uniqueness and correlation must be disclosed.

The **Review Coordinator** freezes the policy/source revision, plans n and authenticates constraints; **Reviewer Workers** produce independent source-linked findings without reading each other's draft; the **Synthesis Reviewer** aggregates immutable results while retaining dissent/P0 blockers; the **Human Validator** alone makes A.1/B.1 or approval decisions in the proper gate. No coordinator/workers have been executed from this documented flow. Do not self-grade a simulated reviewer as independent. See [master](../.spec.md#12-weighted-multi-agent-review-requirements-and-design) and [RTM](../.traceMatrix.md#i-plan-088--unified-review-service-requirement-and-evidence-crosswalk-draft).


## PLAN-099 — Multi-worker scheduling versus reviewer roles (design only)

Retain the existing F33 logical responsibilities and proposed weighted F38–F42 profiles. Introduce **no new independent reviewer/coordinator authority**: a `Scheduler` responsibility may distribute ready, scoped units; a `Module Owner` is the sole writer for a shared component; a `Trusted Integrator` performs source-SHA, contract, conflict and regression checks; an `Independent Reviewer` evaluates evidence but cannot self-approve; an `Approval Owner` holds an explicit external human decision. These are **roles, not running services**.

| Role / work type | Concurrency permissions | Output and stop condition |
| --- | --- | --- |
| Discovery/research/QA/security reviewer | Parallel read-only on same pinned source, with independent worker execution explicitly evidenced | Evidence-linked findings; unverified/partial dissent preserved |
| Scoped implementation worker | Parallel only if approved DAG dependencies and nonoverlapping write + transitive impact sets, isolated environment with OS policy | Staged patch, exact source SHA, observed checks, resource budget; no shared master/Protected Core write |
| Integration owner | Serial writes to shared contract, canonical BRD/RTM/AGENTS, workflow journal and merge target | One combined source SHA, regression/contract outcome; BLOCK on conflicts |
| Security/quality gate | Can parallelize isolated checks but cannot be authored/approved by the same untrusted worker | Independent mandatory gate evidence; reject stale or P0 |
| External approver | No automated authority delegation to workers or models | Explicit recorded approval only after independent A.1/B.1 evidence |

The proposed [WorkUnit/WorkerResult contract](../.documents/featureDesign.md#81-bounded-parallel-work-and-worker-compatibility) carries task, parent stage, dependencies, source SHA, read/write/impact sets, budget, expected output and result. Worker count is **bounded by available host, budget and mandatory expert coverage**, not hardcoded globally. If no real worker runtime is available, use serial, explicitly labeled `SEQUENTIAL_NONINDEPENDENT`; fail closed when independence is a mandatory acceptance condition. A stage/task still traverses all nine universal steps, with safe STOP/handoff on collision or worker loss.

## DOC-A08 — Reviewer weighting, independence and veto rules

The existing **proposed** reviewer allocation (expertise 35%, task fit 25%, perspective 15%, marginal coverage 15%, budget 10%) must be computed only among candidates that first meet mandatory role coverage, verified provider availability, approved data-access scope and resource limits. Weights are design defaults, not measured calibration. For each selected review worker or sequential analytical lens, record `reviewerId, actualProvider/sessionOrLens, expertiseEvidence, perspective, scope, inputSha, budget, observedFindings, confidence, correlatedWith`.

If all roles are simulated within one model/context, declare `independentWorkers=0` and `correlatedReview=true`; do not treat different personalities as independent votes. Synthesis retains separate adverse findings, disagreements and unknown coverage; it must not average away a security P0, missing mandatory BA/QA role, data/privacy issue or source revision mismatch. Only a separately authorized real reviewer/owner can sign A.1. Model/provider availability failure becomes `PARTIAL_COVERAGE`, never silent acceptance.

## PLAN-106 / R10 — Reviewer composition and dissent aggregation

Proposed specialist weights only rank candidates **after** hard constraints (authorized scope, actually available provider, required BA/developer/QA/security/data expertise and bounded budget) are satisfied. Report selected `n`, each actor's provider/session evidence, expertise match, personality lens, source SHA and possible correlation. If workers are simulated sequentially inside one conversation, label `independentWorkers=0` regardless of how different their prompts sound.

The synthesis reviewer retains all minority P0 findings as separate issues; it must never remove a veto through weighted averaging or self-appoint the business/security owner. On worker outage or disagreement, return `PARTIAL_REVIEW/UNRESOLVED`, name the missing discipline and assign a human decision owner. Real A.1 identity and accepted risk remain external gates.
