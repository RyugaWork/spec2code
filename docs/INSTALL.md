# Install Gymuro Spec-to-Code v0.6

**Target:** private `Gymuro-Project` checkout. This package is local only and does NOT modify GitHub or `AGENTS.md` automatically.

1. Back up existing agent skill and state; do **not** overwrite another developer's `.agents/state/` inventory.
2. Extract package at repository root. Skill should be `.agents/skills/spec-to-code/SKILL.md` (without the extra dot in `.skills`).
3. Review `AGENTS_PATCH.md` and update root `AGENTS.md` only with repository-owner approval. Existing business/Git policies prevail.
4. Use Python 3.10+ and local Git. No third-party packages, network or API keys required.

PowerShell from the actual Gymuro-Project root:

```powershell
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . start
# Select task-specific context mode. Change observed path to a real path in this checkout:
py -3 .agents/skills/spec-to-code/scripts/context_router.py --root . --task-id TASK-001 --task "Change Member page label" --paths .source/web/src/MemberPage.tsx --mode auto
# Explicit: --mode minimal | balanced | deep
# Read .summerize.md only when required; traverse <Layer>/.summerize.md -> <Component>/.summerize.md -> specific function document.
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . inspect --layer api
# After approved edits:
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . record --paths .source/backend/Gymuro.Api/Program.cs --note "Applied approved scope" --requirement GYM-AUTH-001
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . checkpoint
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . finish
# Copy exact Session ID printed by start/finish; never guess it:
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . merge --session-id GYM-YYYYMMDD-HHMMSS-XXXXXXXX
```

## Outputs

| Path | Role | Read policy |
| --- | --- | --- |
| `./.summerize.md` | Top-level layer routing, path matrix, Mermaid graph | Read if locating layer |
| `./Present/.summerize.md` etc. | Layer definition, component matrix and linked layers | Read only required layers |
| `./<Layer>/<Component>/.summerize.md` | Component/controller path, observed functions and links | Read one relevant component |
| `./<Layer>/<Component>/.<Component>.<Function>.md` | Function declaration, source locator, revision, last change | Read only target function |
| `.handoffs/.details/.visualChange.{SessionID}.md` | Unmerged external/outside-session changes | Relevant pending session only |
| `.handoffs/.details/.specChange.{SessionID}.md` | Unmerged current-session authored changes | Relevant pending session only |
| `.handoffs/.buildnotes.handoff.md` | Quick handoff + verified merged history | Read quick summary first |
| `.agents/state/` | Machine-only graph, snapshots, session evidence, symbol cache | Do not load all files |

**Safety:** `merge` only removes pending logs after exact ID, header, content-hash and durable ledger checks. It cannot be called against an active session. No glob deletion, automatic commit, push, remote fetch, or secret reading. If a merge is blocked, inspect its error and preserve source logs. Human-written architecture files cannot be overwritten by the generator.

**Existing v0.3 logs:** `visualChange.md` and `specChange.md` at repository root are intentionally untouched. If they exist, manually reconcile/migrate them with owner approval; do not delete them based on v0.6 merge operations.

**Generated docs vs Git:** The script writes architecture **indexes**, not runtime implementation. Discuss whether to track or ignore these docs per contributor workflow. Machine-local active state, locks and snapshots under `.agents/state/` should ordinarily not be shared or committed. No policy files are overwritten by installation.

## Test commands

```powershell
py -3 -m unittest discover -s .agents/skills/spec-to-code/tests -v
```

The tests create temporary local Git repositories only, never use GitHub.

## Adaptive mode notes

The mode router uses existing machine indices and requires an ACTIVE session with current Git HEAD. It writes `.agents/state/context-pack.json` (temporary path-only pack). It does **not** change `.handoffs/` files or source. It does not fetch remote commits. For per-developer overrides, copy the `references/context-policy.example.json` into `.agents/state/context-policy.json`; do not overwrite existing local state. See `references/adaptive-modes.md`.
