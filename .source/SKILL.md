---
name: spec-to-code
description: Run a repository-independent, evidence-based spec-to-code workflow with optional official GitHub Spec Kit integration. Use for coding sessions, requirement-to-task traceability, architecture graph routing, external Git drift checks, incremental minimal/balanced/deep context selection, and session-scoped change handoffs. Do not use as permission to approve business rules, change Git history, or deploy.
---

# Spec2Code v0.7.0 — Universal + Spec Kit Bridge

The bundled `.config/*.json` files next to `SKILL.md` and `scripts/` in the installed skill are required; a missing or malformed config blocks execution. See `docs/CONFIGURATION.md` in the source repository.

The target repository's `AGENTS.md`, approved requirements, security policies and Git workflow take precedence. Do not assume ASP.NET Core, React, a `.source/` directory, or any business domain. This skill **does not automatically install Spec Kit**, create commits, modify business requirements, or execute unapproved coding actions.

## First: enforce Path Guard and create a coding session

From the **exact target Git repository root**, before coding. All CLI actions, including `status`, `scan`, `context_router`, Spec Kit discovery and handoff `merge`, refuse non-Git or nested roots. Repo-relative paths cannot traverse symlinks or escape the checkout. See `docs/PATH_GUARD.md` in the source repository:

```sh
python .agents/skills/spec-to-code/scripts/session_guard.py --root . start
```

The local script inventories recognized source roots, hashes only eligible changed files, creates a unique `S2C-YYYYMMDD-HHMMSS-XXXXXXXX` Session ID, indexes observable architecture and detects Git commits/outside-session changes. It never runs `git fetch`, sends source to an AI model, or reads environment-secret values. An ACTIVE session blocks a second `start`; checkpoint/resume instead. `status` and `inspect --layer <layer>` are available.

## Spec Kit integration — mandatory gate when a feature uses Spec Kit

Spec Kit is managed by the **official Specify CLI** and the target agent integration, NOT by files copied from this repository. Install and initialize it separately following `integrations/speckit/README.md`; retain Spec Kit ownership of `.specify/` and `specs/`.

- Resolve the active feature from `SPECIFY_FEATURE_DIRECTORY` (explicit override) or `.specify/feature.json`; **do not infer from Git branch**.
- Run the read-only bridge for the relevant stage before reading spec details:

```sh
python .agents/skills/spec-to-code/scripts/speckit_bridge.py --root . --stage implement
```

- For implementation, the bridge requires an in-workspace active feature with `spec.md`, `plan.md`, `tasks.md`; missing files, unsafe pointers and symlinks **block** implementation. It reports paths, SHA-256 fingerprints and bounded task IDs, not spec content or human approval.
- Use the agent's installed Spec Kit skills for `specify → clarify → plan → tasks → analyze → implement → converge` according to task size. Spec2Code does not impersonate or silently invoke those stages. Re-run only the stage invalidated by a relevant change.
- Project policy and approved artifacts must be checked by the agent even when the bridge reports READY. READY means **files exist**, not that a human approved the requirement or that tests pass.

If Spec Kit is not initialized, the bridge's `status` returns `NOT_INITIALIZED`. Do not claim a full Spec Kit workflow succeeded. Non-Spec Kit projects may continue with their own approved requirement documents.

## Adaptive context routing (once per task, after session preflight)

```sh
python .agents/skills/spec-to-code/scripts/context_router.py --root . --task-id T001 --task "Implement scoped task" --paths src/feature.py --mode auto --speckit-stage implement
```

Use paths **actually found in the checkout**, not literal examples. `--mode auto|minimal|balanced|deep` selects a bounded graph traversal based on file count, risk, affected layers and external drift. Manual requests cannot bypass an evidenced Deep safety floor. The router writes only `.agents/state/context-pack.json`, a **path/hash/ID** summary. It also includes the active Spec Kit feature and artifact paths through `speckit_bridge`, not duplicated specification bodies. An invalid Spec Kit gate must not overwrite an existing context pack.

When planning a feature before `plan.md` or `tasks.md` exists, use `--speckit-stage plan` (or `status` for discovery); use `--speckit-stage implement` only once implementation prerequisites exist. Always read the approved security/requirements rules relevant to the task even if the token target is exceeded.

## Read-on-demand architecture

`./s2c/.summerize.md` → `s2c/<Layer>/.summerize.md` → `s2c/<Layer>/<Component>/.summerize.md` → `.<Component>.<Function>.md` → exact source lines. Reuse the machine graph and symbol cache under `.agents/state/` without loading entire JSON files into the model. Generated docs provide **static/lexical evidence only**. Unknown functions, dependencies and runtime behavior must never be invented. The historical `.summerize.md` spelling is deliberately retained for compatibility.

The generic scanner handles conventional roots such as `src/`, `app/`, `backend/`, `web/`, `packages/`, `tests/` and `.source/`; it does not promise full language-semantic or cross-language dependency analysis. Missing graph edges are **unknown**, not proof of independence.

## Provenance and exact-session handoff

- `.agents/.handoffs/.details/.visualChange.{SessionID}.md`: observed outside-session Git changes, **not** current-session authored edits.
- `.agents/.handoffs/.details/.specChange.{SessionID}.md`: actual source/spec changes **explicitly registered** to this active session. Spec Kit-managed `specs/**/*.md` changes can be registered here.
- `.agents/.handoffs/.buildnotes.handoff.md`: quick index plus verifiable merge ledger. Never delete pending files by wildcard.

```sh
# After an authorized edit, and only for paths that actually changed:
python .agents/skills/spec-to-code/scripts/session_guard.py --root . record --paths src/feature.py --note "Implemented approved task" --requirement REQ-001
python .agents/skills/spec-to-code/scripts/session_guard.py --root . checkpoint
python .agents/skills/spec-to-code/scripts/session_guard.py --root . finish
python .agents/skills/spec-to-code/scripts/session_guard.py --root . merge --session-id S2C-YYYYMMDD-HHMMSS-XXXXXXXX
```

`merge` requires a FINISH audit event and validates the exact Session ID, pending type/header, SHA-256 and persisted archive before removing **only** matching pending files. Ambiguous changes remain `UNATTRIBUTED` until reconciled. Never auto-commit/push/rebase/force or delete user source. If explicitly permitted to commit in the target project, use Conventional Commits and `Spec2Code-Session: <exact ID>` trailer for traceability, not proof of authorship.

## Target-output migration (v0.7.0)

The target's runtime journals and ledger now live under `.agents/.handoffs/`, and generated architecture documents under `s2c/`. The old `.handoffs/` and root architecture files are never silently migrated or deleted. If known legacy evidence/state exists, fail with `LAYOUT_MIGRATION_REQUIRED` until old sessions are finished with matching binaries and an explicit backup/migration is reviewed. Unowned `s2c/` content blocks publication.

## Quality gates

Resolve approved requirement → affected nodes → plan/tasks → minimal scoped edits → tests/verification → registered changes → finish/handoff. Report `PASS`, `FAIL`, `BLOCKED` and `NOT RUN` accurately. Use `references/spec-to-code-workflow.md` only for complex features; `references/session-lifecycle.md` for drift and recovery; `references/adaptive-modes.md` to customize the routing policy. Do not indiscriminately load all references or the full Git history.

## Continuous scope (v0.6.3)

Each new session binds its exact canonical Git checkout root, filesystem identity and Git admin directory. Session `status`, `checkpoint`, `record`, `finish`, architecture inspection, and context routing must re-check this binding. If the binding differs, fail closed with `SCOPE_VIOLATION`; do not silently reinitialize or auto-migrate an ACTIVE earlier-version session. Incoming Git HEAD changes invalidate prior context packs at checkpoint; MCP write actions (other than checkpoint) require fresh HEAD.

All file reads/writes use Path Guard; `scope_io.py` anchors file operations to directory handles with no-follow protections on supported POSIX platforms. On Windows, checks are repeated but OS-level race freedom is **not** guaranteed; use a trusted local workspace and filesystem permissions. The `mcp_boundary.py` module is **only** a future-MCP authorization gate, not a running MCP server. See `docs/CONTINUOUS_SCOPE_ENFORCEMENT.md` in the source repository. Never treat path checks as authorization to modify a repository.

## PLAN-080 v0.8.0 candidate: governance and workflow

Before implementation, resolve applicable host AGENTS and policy document references:

```sh
python .agents/skills/spec-to-code/scripts/policy_resolver.py --root . --task-id T001 --task "Review scoped change" --operation plan --format summary
```

Read required host policies independently of token budgets. Resolver READY means references were located, never that approval exists.

Workflow Guard is read-only by default and records explicit authorized stage transitions; it cannot run code, Spec Kit stages, Git operations or tests:

```sh
python .agents/skills/spec-to-code/scripts/workflow_guard.py --root . status --task-id T001
python .agents/skills/spec-to-code/scripts/workflow_guard.py --root . evaluate --task-id T001 --phase DISCOVER
```

Host ownership, Scope IO/Path Guard, session binding, and exact-session handoff remain mandatory.

## PLAN-080.1 task-scoped governance gates

Always supply the real task description and affected repository-relative source paths to Policy Resolver, Context Router, and Workflow Guard. Do not submit generic placeholder text for implementation gates:

```sh
python .agents/skills/spec-to-code/scripts/policy_resolver.py --root . --task-id T001 --task "Fix authentication" --paths src/auth.py --operation implement --format json
python .agents/skills/spec-to-code/scripts/context_router.py --root . --task-id T001 --task "Fix authentication" --paths src/auth.py --speckit-stage implement
python .agents/skills/spec-to-code/scripts/workflow_guard.py --root . begin --task-id T001 --task "Fix authentication" --paths src/auth.py
python .agents/skills/spec-to-code/scripts/workflow_guard.py --root . evaluate --task-id T001 --phase DISCOVER --task "Fix authentication" --paths src/auth.py
```

Use actual paths, not these illustrative filenames. Subsequent Workflow Guard evaluations/transitions must retain the same task and affected paths. Only a task-scope SHA-256, not the raw description, is written to the workflow journal. Changing any selected policy file, nested AGENTS reference, map or context pack invalidates the snapshot. Policy BLOCKED prevents new context pack publication; NEEDS_REVIEW produces a non-ready routing result (CLI exit code 3). Review is not automatic approval: the CLI cannot supply trusted review assertions, tests or deployment authorization.
