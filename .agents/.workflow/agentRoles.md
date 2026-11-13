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
