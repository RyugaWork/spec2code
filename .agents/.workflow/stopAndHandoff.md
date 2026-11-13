# STOP → State snapshot → Handoff → RESUME protocol (PLAN-083)

This is an **agent-level Markdown protocol** usable today in a directed conversation. It is **not** a `workflow_guard.py pause` command, not an auto-save daemon, and not a grant for writing to a host. Use alongside [workflow specification](workflowSpecification.md), [agent runbook](agentRunbook.md) and [handoff template](../../.source/references/stop-handoff-template.md).

## When to stop

Stop on user `STOP`, `pause`, or explicit request to transfer; also stop immediately when scope/path guard fails, secrets or ownership are uncertain, an authoritative requirement is absent/contradictory, a necessary approval is missing, test evidence fails, current code/spec has drifted, tooling is unavailable, context is insufficient, or continuation could cause unreviewed external side effects.

A request to STOP overrides the task's planned next steps. Do not complete one last implementation step, silently commit the current edits, or merge anything merely to make the handoff look tidy. Keep unrelated user changes untouched.

## Safe-stop sequence (ordered)

1. **Freeze:** stop new file edits, process executions with side effects, deployments and Git writes. If a command may still be running, report `IN_FLIGHT_UNKNOWN` rather than guessing completion.
2. **Identify:** task ID, requester-approved mode and scope, exact local Git root if actually checked, ref/SHA, current phase, active session ID if observed, last safe action.
3. **Observe bounded state:** only where safe and permitted, read local status, changed path names, recent real test logs and error codes; revalidate root for local S2C tools. Read-only `session_guard.py --root . status` is available; `workflow_guard.py --root . status --task-id ... --task ... --paths ...` is diagnostic only and has an open scope regression. A `checkpoint` is **optional, state-mutating and authorization-dependent**, not an automatic STOP prerequisite.
4. **Classify work:** `DONE_AND_EVIDENCED`, `IN_PROGRESS`, `BLOCKED`, `NOT_STARTED`, `UNKNOWN`. For each affected requirement/AC, specify source change path, test status and blockers. Separate authored edits, outside commits and unattributed local changes.
5. **Write handoff or fall back:** if an explicitly authorized destination in the verified checkout is safe, create a **new** human-owned STOP document using `stop-handoff-template.md`. Suggested host path: `.agents/.handoffs/.stops/<task-id>/<UTC-time>.md`; use a host-approved different path when ownership is unclear. Never overwrite an existing file; never write directly to machine `.details` journals or the merge ledger. If writing fails, output the same handoff in chat and label `NOT_PERSISTED`. A separate development-repo handoff belongs under its reviewed versioned `.agents/.handoffs/` governance folder.
6. **Return control:** report `STOPPED_WITH_HANDOFF` only after confirming the exact destination; otherwise `STOPPED_UNPERSISTED`. Include what cannot be verified and the next owner/authorization. Leave existing session ACTIVE/unknown; do not call `finish`, `merge` or Workflow Guard `close`.

## Handoff fields (required)

| Field | Value rule |
| --- | --- |
| ID / Created | Unique task + UTC timestamp, actual capture time, not inferred |
| Task / scope | Stable ID, factual task summary, authorized paths and excluded paths |
| Repository | Exact owner/repository or local root; branch, commit SHA and dirty/untracked/unknown classification |
| Phase / stop | Last known normal phase; reason code and human-readable reason; in-flight work uncertainty |
| Session / workflow | Local session ID/status and workflow phase/status only if actually observed; otherwise UNKNOWN |
| Work snapshot | Completed tasks with evidence, partially changed paths, unknown authorship, open tasks and AC IDs |
| Verification | Actual commands, environments and results PASS/FAIL/BLOCKED/SKIPPED/NOT RUN, exact source revision; stale evidence indicated |
| Safety | Secrets redacted; no raw credentials, PII, huge source, unverified remote assumptions |
| Next actions | Ordered smallest safe steps, dependencies, approval decision, verification to re-run |
| Persistence | `PERSISTED` + verified path/ref, or `NOT_PERSISTED` + reason; separate from task completion |

Do not store entire model conversation, raw access tokens, `.env`, unreviewed user data, false test evidence, hidden chain-of-thought or another collaborator's edits presented as agent-authored changes.

## Continuation protocol

1. An explicit user/host RESUME request identifies the STOP record; if multiple records exist, use the **latest verified record for the same task/worktree**, preserving prior history. Do not use one task's session or Git status to resume another.
2. Recheck repository and source ownership, current AGENTS/policies, task scope and active Spec Kit feature. Re-read the current requirement and changed code. Compare with the handoff's reference; changes invalidate affected evidence.
3. Consult current `session_guard.py status` and available read-only `workflow_guard.py status` with proper scope, and distinguish **observed** state from the handoff's historical report. No automatic session start/finish or journal repair.
4. Resume only after requested implementation authority, required external decisions, safe path validation and stale test reruns are satisfied. Otherwise create a new STOP handoff that cites the earlier one, without overwriting it.
5. State the resumed phase and first authorized action. The handoff is context/provenance, **not an independent reviewer decision** or automatic reauthorization.

## Missing or corrupted handoff

If the process crashed before a confirmed write, report `INTERRUPTED_UNKNOWN`. Read from observable Git/status and prior trusted logs; do not synthesize completed steps. If a STOP file is missing, ambiguous or tampered with, never silently select a different workspace or bypass policy. Preserve existing files, declare evidence uncertainty and ask the responsible owner to reconcile before writing.

## Why this is separate from the runtime journal

The current workflow configuration has no `PAUSED` enum and `workflow_guard.py` has no STOP/RESUME action. `session_guard.py checkpoint` updates local session metadata; `finish` marks CLOSED and `merge` archives/deletes exact pending logs. Thus STOP must **not** be mapped to these actions or `invalidate` just to force a pause state. A future implemented pause requires explicit schema, transition and backward-compatibility review plus tests; until then only an **agent-reported** STOP outcome can be claimed.
