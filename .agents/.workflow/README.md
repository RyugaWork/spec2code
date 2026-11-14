# Spec2Code workflow index — planning before implementation

> **Current state:** PLAN-103 documentation is an **author-complete candidate for independent A.1**, not an A.1 PASS or code authorization. [Planning & Specification P1–P9](planningSpecificationWorkflow.md) and [design handoff](designHandoffTemplate.md) are the recorded Phase-A process. The implementation flow described below is future and only applicable following independent review, host/security approval and a separately authorized B task. STOP/handoff is an agent procedure, not a newly deployed Workflow Guard machine state.

1. **Requirement:** update `../.spec.md` as required and set the feature's status in `../.features.md`.
2. **Plan first:** record scope, owner, changed files, rollback, acceptance tests in `../.plans.md`.
3. **Threat model:** classify security/data/cross-OS effects in `../.risk.md`; block unsafe writes.
4. **Session:** start/restore an exact Git checkout session via the installed skill's `session_guard.py`; never treat a source-repository document as host-local runtime session.
5. **Code:** implement only approved changes and keep code/config in `../../.source/`.
6. **Tests:** execute `python -m unittest discover -s .source/tests -v`, plus platform and installation checks; update `../.checklist.md` with evidence.
7. **Handoff:** add a dated file in `../.handoffs/` summarizing feature IDs, commits, changed files, tests, risks, rollback and pending work.
8. **Review/merge:** no force push. Merge only after explicit review and required CI results; update changelog and statuses.

All test claims must distinguish PASS, FAIL, SKIPPED, BLOCKED and NOT RUN.

## PLAN-080 controlled lifecycle

1. DISCOVER: validate checkout; read root/nested AGENTS and relevant policy candidates.
2. SPECIFY_PLAN: establish requirement authority, feature spec/tasks, scope, risks and approval needs.
3. IMPLEMENT: use a bound active session and approved code paths; track provenance.
4. VERIFY: record actual test/build evidence; on FAIL return explicitly to IMPLEMENT.
5. HANDOFF_REVIEW: finish exact session, preserve human and machine records, request independent review.

Workflow Guard evaluates requirements and records user-authorized transitions. It does **not** execute Git, tests or code changes. NEEDS_REVIEW is not PASS.

## PLAN-080.1 scope binding and review boundary

- Run `policy_resolver.py` for the actual task ID, description, affected paths and operation. Treat `READY` as discovered policy references only.
- Run `context_router.py` with identical task ID, description and paths. `NEEDS_REVIEW` is non-ready; required-policy conflicts block pack publication.
- Run `workflow_guard.py begin/evaluate/advance` with identical `--task` and `--paths`. A different description or path set cannot reuse recorded workflow state.
- Root and nested AGENTS, scoped policy documents, host policy map and context-pack fingerprints are snapshot inputs. Change invalidation requires explicit reconciliation.
- Workflow Guard never approves a human gate, executes tests, modifies source, pushes Git or certifies Windows TOCTOU resistance. Review requires an independently trusted host decision; CLI stage commands alone cannot self-authorize.

## PLAN-081 agent playbooks and authority

- [Roles](agentRoles.md): coordinator, requirements, architecture/policy, implementation, test, security and handoff responsibilities. These are logical roles; S2C has no daemon or autonomous subagent worker.
- [Runbook](agentRunbook.md): separate read-only, planning, implementation, verification and delivery actions; scoped context routing, local session lifecycle, optional upstream Spec Kit and fail-closed reporting.
- [Domain authorities](../.documents/.documentGovernance.md) and [policy routing](../.documents/.policyRouting.md): identify owners and required operation without turning a discovered reference into permission.
- [Test/delivery gates](testingAndDelivery.md) and [Git rules](../.git.workflow.md): explicit evidence and external acceptance before merge/release.

These agent documents guide ChatGPT/Codex interactions and do not implement missing Workflow Guard controls. PR #7 retains three P0 and one P1 review findings; active Windows TOCTOU, OneDrive and legacy-migration risks are unchanged.

## PLAN-083 interruptible work protocol

- [Workflow specification](workflowSpecification.md) describes the five ordinary phases plus an **agent-level STOP edge** usable at any phase, the minimum evidence for each phase and the gate for re-entry.
- [STOP/handoff protocol](stopAndHandoff.md) requires an immediate freeze of new mutations, bounded observed status, factual handoff with `PERSISTED` or `NOT_PERSISTED`, and explicit RESUME revalidation.
- The [STOP handoff template](../../.source/references/stop-handoff-template.md) is separate from successful session finish/merge evidence. **Do not call `finish`, `merge`, Workflow Guard `invalidate` or `close` merely to stop.**
- The [system RTM](../.traceMatrix.md) tracks F37/`S2C-REQ-037` and NFR-007 as specified but without native runtime STOP tests. Current `.source/.config/workflow.json` has **no PAUSED status**.

## PLAN-084 — authoritative design-phase entrypoints

- [Nine-stage Planning & Specification workflow](planningSpecificationWorkflow.md): scope, specification plan, research, RTM, feature and workflow design, risk discovery, risk management and design handoff.
- [SRS authoring plan](../.documents/systemSpecificationPlan.md), [research register](../.documents/researchRegister.md), [feature design catalogue](../.documents/featureDesign.md), [system RTM](../.traceMatrix.md): evidence and design inputs, including gaps.
- [Scored risk matrix](../.riskMatrix.md) and [risk register](../.risk.md): after every design pass reprioritize and mitigate the largest unresolved risk in documentation; no runtime patch.
- [Design handoff template](designHandoffTemplate.md): preserve exact document revisions, decisions, risks and next stage. Future [implementation workflow](workflowSpecification.md) remains separate and does not start automatically when this document is opened.

## PLAN-085 — validation boundaries

Overall process: **A (P1–P9 planning) → [A.1](validationSpecification.md) (design validation) → separately authorized B (implementation) → [B.1](validationSpecification.md) (system and stakeholder acceptance) → separately authorized release**. A.1 and B.1 have their own [validation report](validationReportTemplate.md) and explicit FAIL/BLOCKED feedback into the impacted previous lifecycle. Current status: **A active, A.1 NOT RUN, B NOT AUTHORIZED, B.1 NOT RUN**. A green CI run or RTM link audit does not constitute A.1 or B.1 PASS.

## Current authoring and review entrypoints — PLAN-103

This page is an **index**, not a new workflow implementation or a replacement for the original nine-stage PLAN-084 planning workflow. For the current **authoring candidate**:

1. Read [master BRD/SRS/architecture §28](../.spec.md#28-plan-103--technical-review-closeout-and-remaining-authority-boundary) and [the existing architecture decisions](../.documents/featureDesign.md#10-plan-102--architecture-decision-records-for-a1-disposition). Preserve the host's own AGENTS and the official Spec Kit ownership of `.specify/` and `specs/`.
2. Read [RTM P](../.traceMatrix.md#p-plan-098--draft-integration-trace-crosswalk-not-implementation) and [test catalogue](testingAndDelivery.md#plan-100-candidate-feature-acceptance-cases); BR-022..027 now have **44 explicitly named designed cases**, not 44 executed or approved outcomes.
3. Read [A.1 validation definitions and PLAN-103 author-review findings](validationSpecification.md#10-plan-103--author-side-technical-review-and-findings-not-independent-a1), [risk matrix](../.riskMatrix.md), and [source-bound handoffs](../.handoffs/plan-103-traceability-review-checkpoint.md). A technical author review is *not* independent approval.
4. On STOP/RESUME, use [the existing protocol](stopAndHandoff.md) and recheck the actual Git SHA, Google Draft revision, source-owner decisions, P0 risk and host/sandbox. Do not convert `NOT_RUN` into `PASS`.

**Current gates:** `AUTHORING_COMPLETE_CANDIDATE`, `A1_NOT_RUN`, `B_NOT_AUTHORIZED`, `B1_NOT_RUN`, provider CLI/MCP and actual host security tests unverified. Any subsequent B work requires a separately scoped approval; no new machine phases, YAML/JSON, automatic CLI or agent worker are created by this index.

## PLAN-110 / Z02 — Reviewer start-to-finish navigation

Start from the [current master](../.spec.md), then use [design](../.documents/featureDesign.md), [RTM](../.traceMatrix.md), [negative/positive tests](testingAndDelivery.md), [risk scoring](../.riskMatrix.md), [role authority](agentRoles.md) and [real A.1 report form](validationReportTemplate.md). Read both existing STOP and feature-specific Spec Kit Web/native gates before asserting a workflow result. The five newest handoffs are `plan-106` through `plan-110` under `.agents/.handoffs/`; verify actual branch SHA before resuming.

A reviewer should first report which documents and external tools were available, whether their assessment is independent, and what remains unexamined. If the source pair, owner BR/AC decision, actual tests or provider capability are absent, assign the correct `BLOCKED/NOT_RUN` value and return a source-linked finding, rather than silently substituting another model or unapproved host operation.
