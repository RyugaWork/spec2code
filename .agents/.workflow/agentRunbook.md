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

## 8. PLAN-084 current mode — design first

Until a reviewed SRS/design package is explicitly approved for implementation, use the [nine-stage planning workflow](planningSpecificationWorkflow.md). The agent's current activities are read-only evidence discovery and **authorized Markdown design edits**: specification plan, sources, requirements/RTM, feature/architecture models, risk discovery/scoring and design handoff. Do not automatically invoke `session_guard start`, `workflow_guard begin`, Spec Kit implement, code patches or runtime STOP/RESUME based on reaching the next design stage. A design STOP creates a [design handoff](designHandoffTemplate.md) and preserves uncertainties without claiming to close any session. Risk management each pass selects the highest-priority risk and changes **design mitigations**, not runtime files. Current status is `DESIGN_IN_PROGRESS`.

## 9. PLAN-085 validation roles and rework routing

After A/P9, a designated reviewer must use [A.1 Design Validation](validationSpecification.md) and [report template](validationReportTemplate.md) to challenge source authority, ACs, feature/architecture consistency and unaccepted P0/P1 risks. The author may prepare evidence but cannot impersonate an independent reviewer. On failure return to affected A stage(s), preserving the RTM and risk history; **never begin coding because A.1 produced a PASS** without explicit user/host authorization. After a future B is complete, B.1 must independently evaluate real system behavior and host security/acceptance; FAIL returns to B, or A/A.1 for changed requirements. Do not create fictional runtime validation commands or results. During current design, both validation outcomes are **NOT RUN**.

## 10. Versions and structures across S2C and integrated hosts (PLAN-086)

For **all** technology classes, including Python interpreter/requirements, PowerShell runtime/module edition, SQL DBMS+driver+dialect+migrations, .NET, CI images and project layout, complete a [technology assessment](../.documents/technologyAssessmentTemplate.md) using the [cross-stack policy](../.documents/technologyVersionPolicy.md). The **default** is currently supported, mature and widely adopted, not just the latest major. Preserve existing S2C support/CI and a host's approved structure until a separate change is authorized; do not retarget `pyproject.toml`, PowerShell scripts or migrations automatically.

**Explicit User Override** takes priority over the conservative maturity preference: identify the user's exact requested technology/version/structure and scope, and document it with an [override record](../.documents/technologyOverrideTemplate.md), risk and compatibility/upgrade plan. Newly released supported major versions can be accepted as **design choices** if the requester expressly chooses them. Unsupported/EOL/preview/high-risk selections need a further safety/owner review and may remain blocked; higher-priority security, Path Guard and separate Git/write/release authorization cannot be waived. A.1 reviews the decision, B.1 later checks actually installed versions when implementation has been authorized. The current work remains design, not implementation.

## 11. PLAN-101 — Codex AutoRun preflight

**Current fact:** `--full-auto` failed on the tested Codex version, Gemini/AGY is unverified, and the GitHub-only documentation path does not prove local Path Guard.

1. **Discover:** confirm checkout root, current `git status --porcelain=v1`, branch, AGENTS hierarchy, current docs/Spec Kit, and nine prior local modified/untracked files recorded in [checkpoint 1](../.handoffs/plan-100-documentation-checkpoint-1.md). If local checkout is inaccessible, status is NOT_OBSERVED.
2. **Capability:** record observed `codex --version` and `codex exec --help`, exit/stderr, usable sandbox and writable state DB. On known `0.169.0-alpha.11.1` the full-auto flag exited 2; a separate read-only attempt exited 1 during app-server initialization. Do not guess a replacement flag or bypass sandbox.
3. **Provider opt-in:** verify MCP package origin/pin/auth and actual tool names using synthetic read-only fixtures. Reject surprise provider commands, credentials, untrusted instructions and whole-repo data requests.
4. **Plan:** bind approved documents, git/Google revisions and requirement/risk/AC mapping. Do not check Spec Kit T011/T012/T015 or enable B.
5. **Execute only in approved boundary:** enforce OS sandbox, Path Guard, allowlisted Markdown, secrets filter, timeout, retries, token/cost cap, cancellation and one-writer rule. A GitHub connector commit is **not** a local CLI test.
6. **Verify:** document changed-file scope, links, IDs, reverse trace and actual command evidence; keep planned MM-TCs as NOT_RUN unless actually exercised. Gemini independent review is only real when provider call and reviewer identity are evidenced.
7. **Handoff and STOP:** save exact source/commit SHA, source pair, files, validations, blockers and next steps before another part. Stale ref, privilege error, P0, quota or budget exhaustion causes STOP and revalidation on RESUME.
8. **Gate:** only independent A.1 and a separate B approval can authorize source implementation. Refer to [test cases](testingAndDelivery.md#plan-101--codexgemini-mcp-acceptance-design).

No command in this document is claimed to have been newly run.

## DOC-A09 — Host CLI evidence and safe documentation fallback

The operator must capture exact `codex --version`, `codex exec --help`, OS, sandbox policy, writable Codex state location, permitted commands, repository root, and actual stderr/exit **on the approved host** before claiming Auto Run. Prior Codex `0.169.0-alpha.11.1` rejected `--full-auto` (exit 2) and a separate read-only probe failed state/app-server initialization (exit 1). These failures are evidence of **incompatibility in that tested environment**, not successful model execution. Do not guess alternate flags, set unrestricted `--yolo`, auto-install unverified MCP packages or place state outside the approved sandbox without host consent.

If the host cannot run the tool, stop automated execution and publish only independently authorized read/write **documentation through the GitHub connector**, identifying this as a distinct path. Before any remote commit check expected HEAD, allowed files, diff and actual result; never overwrite pre-existing uncommitted local work. Explicitly label `CLI_NOT_RUN / PROVIDER_NOT_VERIFIED / LOCAL_PATH_GUARD_NOT_TESTED` and preserve a per-batch handoff for resume. A GitHub document commit cannot satisfy native OS negative tests.

## PLAN-107 / S07 — Safe Auto versus host sandbox authorization

`Manual` requires permission for each sensitive action; `Safe Auto` is limited to explicitly reviewed docs-only allowlisted operations; `Sandbox Auto` requires a separately approved disposable host, verified OS containment and bounded tool commands; `Full Auto` still requires a sandbox and explicit authorization, not unrestricted host YOLO. These design terms do **not** assert that the tested Codex CLI implements these flags or supports a particular mapping.

Host preflight checklist: actual `codex --version` and `codex exec --help`, writable state directory, process isolation, physical checkout root, current `git status`, allow/deny commands, cumulative deadline/retry/cost/size budgets, provider/MCP capability and auth, cancellation and rollback. Unsupported CLI flag (previous exit 2), failed state bootstrap (previous exit 1) or absent Gemini credentials => `BLOCKED` and handoff. No fallback that weakens permissions; GitHub connector publication is a separate verified pathway.
