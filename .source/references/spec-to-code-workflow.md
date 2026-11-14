# Universal Spec-to-Code workflow (extended reference)

This reference describes the optional workflow when Spec Kit is **actually initialized** in the target repository. No domain-specific architecture, business rules, or source paths are assumed.

## Phases

1. **Preflight:** inspect target `AGENTS.md`/policy, local Git HEAD, current Session ID and external Git drift. Start or resume via `session_guard.py`; do not access remote Git or commit without separate user authorization.
2. **Feature selection:** use `speckit_bridge.py --stage status` to locate `.specify/feature.json` or a deliberately set `SPECIFY_FEATURE_DIRECTORY`. Never select by branch name alone. Reject out-of-workspace and symlinked paths.
3. **Specification:** invoke the official Spec Kit `specify`, optionally `clarify`; check real business approval and testable acceptance criteria. Run `--stage plan` only when `spec.md` exists. Do not have Spec2Code generate a second canonical feature spec.
4. **Plan and tasks:** invoke official `plan` and `tasks`, with `analyze` for artifact consistency. Use the short architecture indexes and exact source evidence to inform the plan. Spec Kit owns `.specify/` and `specs/`.
5. **Context routing:** run `context_router.py --speckit-stage implement` with current task ID, actual source path(s), and mode `auto`. This validates `spec.md`, `plan.md`, and `tasks.md` and emits path/hash pointers only.
6. **Implementation:** invoke official Spec Kit `implement` with already selected small context plus approved requirements and host security rules. Work only on in-scope paths; runtime source edits are still subject to explicit user authorization.
7. **Verification:** run discovered project-specific build, lint, unit/integration/security tests. Use PASS/FAIL/BLOCKED/NOT RUN; never claim a test passed if not executed.
8. **Convergence:** invoke official `converge`, inspect any new tasks or unresolved spec mismatches, and repeat relevant stages only if invalidated.
9. **Provenance/handoff:** register current-session actual source and `specs/**/*.md` edits into `specChange`, record unexpected external commits into `visualChange`, close and safely merge only exact finished session logs.

## Context economy

- Snapshot and Git diff are computed locally; do not send `infrastructure.json` or entire git logs into prompt.
- Read only `s2c/.summerize.md` → relevant layer → component → function; follow observed edges and bounded heuristics.
- Spec Kit artifacts are pointed to by `spec_kit.feature_id`, `artifacts.<name>.path` and `sha256`; load only relevant sections for the task.
- If the feature pointer changes mid-session, re-run bridge and context route; don't silently use a stale context pack.
- Token budgets are targets; required security and requirements evidence must not be truncated to satisfy a budget.

## Non-goals

No automatic feature approval, full-repository source ingestion, Git push, shell execution delegation, MCP transport or silent Spec Kit initialization. See `integrations/speckit/README.md` for upstream agent invocation instructions.

## PLAN-109 / M05 — Nine work steps versus implemented machine phases

The portable skill's DISCOVER, PLAN, RISK DISCOVERY, RISK MANAGEMENT, IMPLEMENT, TEST, VERIFY, OPTIMIZE and HANDOFF/DOCUMENT responsibilities organize agent work; they do **not** imply nine deployed Workflow Guard machine phases. The actual five-phase machine authority and current bugs must be respected. Each task notes `workStep` and `runtimePhaseOrNA`; a Phase-A documentation-only task marks execution phases N/A rather than forging implementation evidence.

Before any dependency advances, check approved source and P0 risk veto, actual mandatory result, budget and explicit scope. A source/plan change triggers downstream impact invalidation; STOP can occur in every step, with the handoff recording last actual observed action. Multi-agent parallel reading may be proposed, but only one trusted writer may integrate changes unless independent isolation and conflict policy are proven.
