# Agent execution runbook — PLAN-081

Applies to development of Spec2Code and, as **guidance only**, to an installed skill in another Git checkout. Select the relevant mode; do not assume every user request authorizes runtime state writes. Examples use `<skill>` as an explanation placeholder, **not** a literal shell path. In a host installation, the actual script path is `.agents/skills/spec-to-code/scripts/`; in this development repository it is `.source/scripts/`.

## 0. Decide what is allowed

| Request type | Permitted initial work | Not implied |
| --- | --- | --- |
| Review/audit/inspect | Read repository, identify exact paths, report findings | Session writes, tests, code edits, PR approval |
| Plan/spec draft | Read sources, draft proposed changes; persist docs only if requested | Running scripts or implementing code |
| Implement/fix | Edit only approved paths after preflight and policies | Commit, push, merge, deploy, delete |
| Verify | Run authorized available checks and report evidence | Modify production environment, grant approval |
| Commit/PR/release | Exact user-authorized Git action with current diff and review | Permission for a broader Git operation |

If there is no local checkout or no execution tool, perform a repository-source review and mark local commands `NOT RUN`. Never claim a remote API check ran `path_guard.py` on a developer machine.

## 1. Read authoritative instructions (DISCOVER)

1. Identify the exact repository and ref/checkout. Read root `AGENTS.md` and only nested `AGENTS.md` files on relevant affected paths; obtain the approved requirements and contract documents required by the task.
2. For S2C development, read `.agents/.spec.md`, `.agents/.features.md`, the specific plan and risks; read `.source/SKILL.md` and relevant configuration/code tests. Never substitute an outdated handoff for current source.
3. For an installed host, read **host-owned** AGENTS and policies. S2C development governance is not deployed host authority.
4. If a host has `.agents/policy-map.json`, inspect the scoped canonical document references. A policy resolver reports applicability/existence only; candidates and `READY` do not establish approval.
5. Preserve git status and existing user modifications. Validate an **exact Git worktree root** with Path Guard before local S2C operations; a nested directory or another worktree is not a substitute.

## 2. Spec Kit branch (only when truly installed)

- Official Spec Kit tools and skills run in the **coding agent's chat**, not as subprocess calls made by S2C. `specify` CLI is for installation/integration management. Confirm the installed agent integration and invoke its native syntax (for Codex skills: `$speckit-specify`, `$speckit-plan`, `$speckit-tasks`, etc.).
- Select the active feature from `SPECIFY_FEATURE_DIRECTORY` or `.specify/feature.json`; never infer it from the Git branch.
- Read-only inspection: `python .agents/skills/spec-to-code/scripts/speckit_bridge.py --root . --stage status`. Use `--stage plan` when `spec.md` is ready; `--stage implement` only when **all three** `spec.md`, `plan.md`, `tasks.md` exist.
- Normal agent sequence: establish constitution when needed; `specify` → optional `clarify` → `plan` → optional `checklist` → `tasks` → optional `analyze` → `implement` → `converge`. The checklist is reviewer-owned evidence, not a way for S2C to approve requirements. Rework only impacted phases when a meaningful change invalidates them.
- S2C does **not** own/write `.specify/` or `specs/` via its bridge. An authorized agent may edit active Spec Kit artifacts using upstream commands, subject to the host's policies and the relevant session provenance.
- If Spec Kit is absent, record `NOT_INITIALIZED` / `NO_ACTIVE_FEATURE` honestly and use the host's own approved requirements. Do not initialize Spec Kit without explicit authorization.

## 3. Plan and authorize (SPECIFY_PLAN)

Establish task ID, exact task description, observed affected repository-relative paths, source authority, accepted AC IDs, plan, dependencies, threat model, rollback and verification strategy. Update development plan/risk records **before runtime code edits**. An unresolved business/security/data/API authority conflict blocks implementation of the affected behavior.

For local tasks needing session state: start/checkpoint the existing validated session with `session_guard.py --root . start` or `checkpoint` as appropriate; never start a new session over an active one. For read-only tasks, do not create session state automatically.

When a real task and files are known, the optional resolver and router can reduce context:

```sh
python .agents/skills/spec-to-code/scripts/policy_resolver.py --root . --task-id T001 --task "Scoped task" --paths src/example.py --operation plan --format json
python .agents/skills/spec-to-code/scripts/context_router.py --root . --task-id T001 --task "Scoped task" --paths src/example.py --mode auto --speckit-stage status
```

These filenames and task are **illustrations**; replace them with observed values. Use the matching `--speckit-stage` for active Spec Kit prerequisites and inspect `routing_status` / governance status. `METADATA_ONLY` sensitive files must never become source-read targets.

## 4. Change, validate, hand off

- IMPLEMENT: edit only authorized code/config/spec paths. Use current source evidence, not lexical graph guesses. A design or new task cannot grant a new permission. Separate self-authored and external drift; use `session_guard.py record --paths ... --note ... --requirement ...` for actual verified authored edits in a local session.
- VERIFY: run the available relevant tests and report exact command, environment, revision and result. S2C development regression is `python -m unittest discover -s .source/tests -v` (Ubuntu 3.10/3.11/3.13, Windows 3.14 in CI). Scope-dependent tests are mandatory where relevant; skipped tests do not prove the skipped controls.
- HANDOFF_REVIEW: checkpoint, finish and merge a session's exact handoff only when all invariants are met and those local actions are authorized. Record changed paths, req/AC trace, tests, unresolved risks, any migration approvals and rollback. Do not delete old logs, force branch changes or self-approve.
- DELIVERY: a GitHub PR review/merge is a **distinct decision** after code+test gates. An authorized commit/push is not permission to merge or deploy.

## 5. Workflow Guard caveats at PR #7

The `workflow_guard.py` five-stage journal is a **pre-release advisory machine gate**, not an orchestrator or approval provider. Use identical `--task` and `--paths` for a scoped task. There are known open findings on the PR #7 head: missing scope in `CLOSE`, VERIFY/HANDOFF operation mapping, missing source/Spec Kit snapshot inputs and scope-free `status` mismatch. Do not represent `CLOSE` as verified, skip a security review, or assert release authorization merely because an event was written. `status` with full scope may be used for diagnosis, but this does not fix the underlying regression.

## 6. Report format

For any finished interaction provide a concise record:

```text
Task / ref: <task ID, exact branch or SHA>
Mode and authorization: READ | PLAN | IMPLEMENT | VERIFY | DELIVERY; approved actions
Authority / scope: <consulted paths and affected paths; UNKNOWN if unverified>
Changes: <paths, or NONE>
Verification: <command, environment, PASS/FAIL/BLOCKED/NOT RUN/SKIPPED>
Known risks and blockers: <IDs or NONE VERIFIED>
Next owner/action: <explicit decision needed, if any>
```

Do not add raw secret values, fabricated approval identities, claimed test sessions or machine state from another checkout.

## 7. STOP/PAUSE/HANDOFF is always available as an agent response

Follow the [workflow specification](workflowSpecification.md) and [STOP/handoff protocol](stopAndHandoff.md). If the user stops a task, **do not finish the planned task first**: cease new changes, report in-flight uncertainty, inspect only safe observed state, and prepare the [STOP handoff template](../../.source/references/stop-handoff-template.md). An authorized, safe file write should use a new reviewed path (never overwrite the machine handoff ledger); otherwise provide the handoff in this conversation explicitly labeled `NOT_PERSISTED`. Preserve the actual ACTIVE/UNKNOWN session state, and never imply that `workflow_guard.py` supports a PAUSED enum or resume transition. Subsequent RESUME needs the user's instruction, fresh repository/path/policy/source validation, attribution reconciliation and refreshed test evidence.

The [RTM](../.traceMatrix.md) maps this agent-level behavior to F37, `S2C-REQ-037` and `S2C-NFR-007`; these are **not** runtime PASS until validated with code and integration tests.
