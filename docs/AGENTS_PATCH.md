# Optional host AGENTS.md guidance — review before adopting

This file is a **copyable suggestion**, not an installer patch and not an authority to overwrite a host's `AGENTS.md`. First read the host's own AGENTS, nested instructions, approved requirements, security/Git policy, and existing Spec Kit installation. Add only non-conflicting guidance with the host owner's approval. Do not copy Spec2Code's development-root AGENTS into the host.

## Suggested host-owned addition

```md
## Optional Spec2Code workflow

- Keep this repository's own AGENTS, security requirements, API contracts, and Git approval rules authoritative. Existing nested AGENTS apply to their directories.
- The installed portable Spec2Code skill lives at `.agents/skills/spec-to-code/`. Its scripts are local checkout-bound helpers for source inventory, context routing and session provenance; they do not authorize edits, Git operations, code execution or releases.
- For read-only inspection, gather relevant policies and observed paths; do not create a write session just to answer a question.
- For authorized implementation, verify the exact Git root and current session; review the actual task and affected repository-relative paths. Use `session_guard.py`, `policy_resolver.py`, `context_router.py` and `speckit_bridge.py` only for their documented local purposes. Never insert made-up paths or text to satisfy a gate.
- If official GitHub Spec Kit is installed, it owns `.specify/` and `specs/`. Choose its active feature from `.specify/feature.json` or `SPECIFY_FEATURE_DIRECTORY`, never by Git branch. Invoke official Spec Kit skills in the coding agent, not as S2C shell commands. Require reviewed `spec.md`, `plan.md` and `tasks.md` before implementation.
- Do not assume a READY routing/bridge result is approval or test success. Respect METADATA_ONLY redaction and block unsafe/external paths. Keep local `.agents/state/`, `.agents/.handoffs/` and `s2c/` output separate from business source. Preserve legacy evidence until an explicit migration is approved.
- Report observed tests with exact command and result. Any commit/push/merge/deploy needs separate authorization. Windows filesystem races and the current v0.8 Workflow Guard release blockers are not certified away by agent instructions.
```

## Adoption procedure

1. Inspect existing AGENTS and select only non-conflicting lines; do not replace the file wholesale.
2. Verify the actual installed skill path, local Git root and optional Spec Kit integration; check for conflicting installed skills or namespace collisions.
3. Keep the host's business/security documents outside Spec2Code's generated `s2c/` namespace. Do not import this development repository's `.agents/.spec.md`, `.agents/.risk.md` or `.agents/.plans.md` as host policy.
4. Perform a read-only trial on a disposable checkout. Only with explicit permission run a session or edit code; record observed evidence and required follow-up.
5. Do not use an AI-generated AGENTS fragment as evidence of independent human approval.

Spec2Code's dev [AGENTS contract](../AGENTS.md) and [role runbook](../.agents/.workflow/agentRunbook.md) document the intended design; the installed `.source/SKILL.md` is the portable agent-facing description.

## Optional STOP/handoff clause for a reviewed host AGENTS

If approved by the host owner, add a host-specific clause requiring the agent to honor `STOP` at any phase, preserve incomplete source/session state, and create a bounded state snapshot using the installed `references/stop-handoff-template.md`. The handoff must show `PERSISTED` with a verified safe destination or `NOT_PERSISTED` with an in-chat copy. Never overwrite machine pending logs or imply that today's `workflow_guard.py` supports PAUSED/RESUME. A future RESUME request revalidates current host AGENTS, requirements, checkout, session, drift and authorization before further edits. This clause does not give the agent write permission.

## PLAN-107 / S04 — Host AGENTS patch adoption contract

This file is a **human-reviewed suggestion** for a host repository, never an instruction to overwrite its AGENTS. Adoption requires the host owner to inspect its existing root/nested AGENTS precedence, source license, security policy, working-tree changes and selected clauses. Generate a non-mutating proposed diff first; a write needs explicit path-specific approval, current HEAD lease and independent OS containment when executed locally.

Mandatory host text: protect unrelated files, deny unapproved remote/model exfiltration, bound shell/process work, preserve external sentinels, name STOP/handoff output and re-check scope on RESUME. Include a conflict table when S2C guidance disagrees with host policy; the host/security rule wins, and the proposal stays `BLOCKED` until reconciled. A GitHub Markdown example is not a successfully installed host guard.
