# Spec2Code change workflow v0.7.0

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
