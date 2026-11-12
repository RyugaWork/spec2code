---
name: spec-to-code
description: Convert approved Gymuro requirements into minimal verified code changes using a session ID, Git drift checks, a multi-level layer/controller/function graph, impact/pathing matrices and provenance-separated pending handoffs. Use at the start of every coding session or when resuming a task. Independent of GitHub Spec Kit.
---

# Gymuro Spec-to-Code v0.6 — Session-Aware Architecture Graph + Adaptive Context

Root `AGENTS.md`, canonical business requirements and Git workflow always take precedence. This skill is **not** GitHub Spec Kit. It does not grant commit, push or requirement approval.

## Mandatory pre-code session check

From repository root, BEFORE reading feature source:

```powershell
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . start
```

The script creates `GYM-YYYYMMDD-HHMMSS-XXXXXXXX`, verifies local Git HEAD changes since the previous checkpoint, incrementally hashes eligible files, updates evidence graphs and nested architecture documentation, and records **outside-session** changes in a pending visual log. It does **not** fetch remote GitHub commits. If another session is ACTIVE, reconcile it instead of starting over.

Use `checkpoint` when new commits or external edits are suspected; use `--verify` only when timestamps/hash reuse cannot be trusted.

## Adaptive mode selection (mandatory per coding task)

After `session_guard.py start` (or `checkpoint` on resume), run **the local context router** to choose scope and mode without reading source into model context:

```powershell
py -3 .agents/skills/spec-to-code/scripts/context_router.py --root . --task-id TASK-001 --task "Update Member page label" --paths .source/web/src/MemberPage.tsx --mode auto
```

`--mode` accepts `auto` (recommended), `minimal`, `balanced`, `deep`. The selector uses the **existing** graph/index, the active Session ID, source paths/functions and external drift status. It prints a compact result and writes `.agents/state/context-pack.json` with paths only. Read only the selected paths; no duplicate architecture graph, no source content in the pack. Unknown paths or stale Git HEAD block routing. If the router cannot identify the task source, supply the exact `--paths` or `--function`; do not expand to the whole codebase.

Auto chooses Minimal for bounded low-risk UI/docs, Balanced for ordinary code changes and Deep for high-risk/cross-layer/external-drift changes. Manual lowering below an evidenced Deep safety floor is refused. Source content, approved requirements and compulsory verification may exceed target routing budgets; never omit a security gate to save tokens. See `references/adaptive-modes.md` only to tune or troubleshoot routing.

**Spec Kit handoff (when separately installed):** Route first, then pass only selected requirements + architecture paths to the relevant Spec Kit stage. Do not duplicate `.specify/` and `specs/` artifacts in layer summaries or re-run unaffected Spec Kit stages.

## Read-on-demand architecture routing (token budget)

1. Read `./.summerize.md` ONLY if choosing which layer(s) the task affects; otherwise use previous context.
2. Read `./<Layer>/.summerize.md` for changed or directly required layers, and their direct high-impact neighbors only.
3. Read `./<Layer>/<Component>/.summerize.md` for the relevant controller/component.
4. Read **only** `./<Layer>/<Component>/.<Component>.<Function>.md` and the exact source file or bounded source lines necessary for the feature.
5. `infrastructure.json`, `system-graph.json` and symbol cache under `.agents/state/` are machine-only; never paste them into LLM context.
6. If a class/function was not observed, **do not invent** architecture docs. Scaffold directories do not establish implemented code.

Example route: `./.summerize.md` → `./API/.summerize.md` → `./API/MemberController/.summerize.md` → `./API/MemberController/.MemberController.GetMember.md`. `Present/` denotes the frontend/presentation layer; other layers are `API`, `Application`, `DataAccess`, `Persistence`, `Security`, `Integrations`, `Delivery`, `Quality`, `Governance`.

The spelling `.summerize.md` is intentionally retained exactly as the repository owner requested. For human-readable graph semantics and known limitations, read `references/hierarchy-layout.md` only when needed.

## Provenance: one pending log per session and change class

- `./.handoffs/.details/.visualChange.{SessionID}.md` — incoming commits and differences from **other/outside** the active session; never records the current session's declared authored changes.
- `./.handoffs/.details/.specChange.{SessionID}.md` — changes **explicitly recorded** by this skill in the active session. `record` requires actual changed path(s) and an evidence note; do not infer authorship from raw Git diff.
- `./.handoffs/.buildnotes.handoff.md` — compact quick handoff and a verifiable append-only ledger of merged session logs.

During an active session, ambiguous unregistered local edits remain `UNATTRIBUTED`, not automatically reclassified as outside work. `finish` refuses to close if any non-external source changes are unregistered or stale. Never overwrite another developer's edits.

```powershell
# After actual authorized edits:
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . record --paths .source/backend/Gymuro.Api/Controllers/MemberController.cs --note "Apply approved requirement" --requirement GYM-001

# If someone else committed or code unexpectedly changed:
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . checkpoint

# Close only after accounting for all changes:
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . finish

# AFTER closing, archive precisely that session's pending logs and remove only verified merged files:
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . merge --session-id GYM-YYYYMMDD-HHMMSS-XXXXXXXX
```

`merge` requires an existing FINISH audit event for the **exact** ID, validates each pending file's session/type header and SHA-256 content, atomically writes and checks the handoff ledger, then removes only the exact validated filenames. A retry is idempotent. **Never** use broad wildcard deletes, directory deletes, or manual cleanup of unmerged pending logs. If the merge fails, preserve the files for review. The typo `.detials` is **not** used; canonical directory is `.details`.

## Spec to code quality gates

1. Confirm requirement IDs and approved behavior from `.agents/.documents/.businessRequirements.md` plus relevant API/security/architecture policy. Separate known, inferred, proposed and unverified requirements.
2. Use graph/matrix to identify exact impacted layers and component paths. Source evidence is static, not production runtime validation.
3. Plan minimal component/function edits and acceptance tests; read only the linked requirements and affected source.
4. Implement within approved source paths (`.source/`), preserve auth, ownership, SQL parameterization, DbContext lifetime and test separation requirements.
5. Verify with relevant commands; truthfully report `PASS`, `FAIL`, `BLOCKED`, `NOT RUN`. Record your edits, checkpoint, finish and merge only after validation.

Do not automatically commit, push, switch branches, fetch, delete or replace user files. An in-session commit, if separately authorized, uses Conventional Commits and trailer `Gymuro-Session: <ID>` to assist attribution; it is not proof of who authored the code.

See `references/session-lifecycle.md` and `references/hierarchy-layout.md` only for nontrivial recovery and internals. Never read all reference documents by default.
