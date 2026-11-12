# Gymuro Spec-to-Code v0.6 — Integration with existing v0.4 layout

No restructuring of user-defined `.summerize.md`, layer/component/function documents, `.handoffs/.details/` or `.source/` is needed. Changes in this package are **additive**, aside from targeted updates to `SKILL.md`, the session guard startup state (`startup_external_paths`), reference docs and tests.

## Existing path → role after integration

| Path | Keeps existing meaning | Adaptive mode usage |
| --- | --- | --- |
| `./.summerize.md` | Layer graph and path matrix | Read only to disambiguate routing |
| `./Present/.summerize.md` and other `Layer/.summerize.md` | Layer/controller matrix | Follow only selected layer links |
| `./<Layer>/<Controller>/.summerize.md` | Function path matrix | Read exact component only |
| `./<Layer>/<Controller>/.<Controller>.<Function>.md` | Source locator and change revision | Read exact function only |
| `.agents/state/infrastructure.json` | File fingerprints + discovered components | Router reads locally; LLM does not |
| `.agents/state/system-graph.json` | Layer connection graph | Router computes bounded neighbor hops |
| `.agents/state/symbol-cache.json` | Extracted function names/lines | Router matches task or function |
| `.agents/state/session.json` | Active session and Git state | Router checks active ID and drift |
| `.handoffs/.details/.visualChange.{SessionID}.md` | Outside-session changes | Router never writes; session guard owns |
| `.handoffs/.details/.specChange.{SessionID}.md` | Registered current-session work | Router never writes; session guard owns |
| `.handoffs/.buildnotes.handoff.md` | Safe merged session history | Read quick handoff only when needed |

## New parts (one writer per file)

| New file | Owner | Lifetime |
| --- | --- | --- |
| `.agents/skills/spec-to-code/scripts/context_router.py` | Skill source | Versioned with code |
| `.agents/skills/spec-to-code/references/adaptive-modes.md` | Skill documentation | Versioned |
| `.agents/skills/spec-to-code/references/context-policy.example.json` | Documented example | Versioned |
| `.agents/state/context-policy.json` | Optional local override | Machine-local; never overwrite |
| `.agents/state/context-pack.json` | Router-generated path list | Replaced on each task; never merge into handoff |

## Mode and reading rules

`minimal`: single-file low-risk UI/docs changes, 0 graph hops, up to 3 paths and 2 function docs; routing budget target 500.

`balanced`: ordinary feature/API implementation, 1 graph hop, up to 8 paths and 5 function docs; routing budget target 1300.

`deep`: auth/PII/payment/schema/migrations, three or more affected layers, six or more files, or external source drift; 2 graph hops, up to 16 paths and 12 function docs; routing budget target 3300.

These are target **routing-context** budgets, not token-meter guarantees. Safety-critical approved documents are always read regardless of mode. Large source code changes may require additional context. `--mode auto` picks from task text, observed path/function metadata and drift. `--mode minimal|balanced|deep` allows explicit choice except when a documented Deep floor is triggered.

## Commands

```powershell
# 1. Once per new coding session:
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . start

# 2. For each task, use observed paths and auto mode:
py -3 .agents/skills/spec-to-code/scripts/context_router.py --root . --task-id TASK-001 --task "Update Member page label" --paths .source/web/src/MemberPage.tsx --mode auto

# Optional explicit mode:
py -3 .agents/skills/spec-to-code/scripts/context_router.py --root . --task-id TASK-001 --task "Update Member page label" --paths .source/web/src/MemberPage.tsx --mode minimal

# If HEAD changed, file metadata is stale or an outside commit was detected:
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . checkpoint

# 3. Implement approved task; explicitly record current-session changes:
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . record --paths .source/web/src/MemberPage.tsx --note "Updated approved label" --requirement GYM-UI-001

# 4. Standard v0.4 finish/merge protocol, with exact session ID:
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . checkpoint
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . finish
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . merge --session-id <EXACT_SESSION_ID>
```

Replace example source paths and requirements with observed/approved values. No file in `.agents/state/` needs to be pasted wholesale into model context. The router prints a compact result; it does not read application source bytes, touch external services or modify handoff logs.

## Spec Kit (optional in the current repository)

After separate installation, keep Specs under the Spec Kit-managed `.specify/` and `specs/` paths. Route the active task before `plan` and `implement`, and pass only the approved spec sections and relevant function paths to the agent. Preserve `AGENTS.md` precedence; do not copy spec bodies into `.summerize.md` or context pack. No Spec Kit installation is included in this bundle.
