# Gymuro Adaptive Context Routing — v0.6

This extension uses **the existing v0.4 hierarchy**, not another architecture store:

- `./.summerize.md` = layer map and pathing matrix.
- `./<Layer>/.summerize.md` = component matrix; `./<Layer>/<Component>/.summerize.md` = function routing.
- `./<Layer>/<Component>/.<Component>.<Function>.md` = source locator, revision, last change (not an implementation specification).
- `.agents/state/{infrastructure.json,system-graph.json,symbol-cache.json,architecture-docs.json,session.json}` = local machine-only indices.
- `.agents/state/context-pack.json` = **path-only**, ephemeral context routing decision for the current task; overwritten on the next route.
- `.agents/state/context-policy.json` = optional local override, schema 1. Do not ship an overwrite of existing state. See `context-policy.example.json`.
- `.handoffs/.details/.visualChange.{SessionID}.md` = external changes; `.specChange.{SessionID}.md` = registered current-session work. The context router never writes either.
- `.handoffs/.buildnotes.handoff.md` = completed, verified handoff; read only Quick handoff unless a specific event is relevant.

## How to use

1. `session_guard.py --root . start` (or `checkpoint` when resuming). This inspects local Git and incrementally updates the current graph before coding.
2. Run `context_router.py --root . --task-id TASK-001 --task "Change Member page label" --paths .source/web/src/MemberPage.tsx --mode auto`.
3. Read the short two-line output; open `context-pack.json` **only if routing details are needed**. Then open selected exact layer/component/function documents. Do not read all referenced paths automatically.
4. If `NEEDS_EXPLICIT_PATH`, supply an observed path or exact function. If `STALE_GIT_HEAD`, run checkpoint first. If `TRUNCATED`, split task or review only the missed relevant paths.
5. If the task changes in a material way (new layer, security policy, database contract, outside commit), re-run the router to elevate/recompute mode. Do not restart Spec Kit phases that are unaffected.
6. For coding, follow existing `record` → `checkpoint` → `finish` → `merge --session-id <EXACT-ID>` protocol. Mode routing is independent of session log provenance.

## Mode decision

| Mode | Common examples | Architecture hop depth | Max source paths | Max function docs | Target routing budget* |
| --- | --- | ---: | ---: | ---: | ---: |
| `minimal` | Single-file label, text, low-risk style/copy | 0 | 3 | 2 | 500 |
| `balanced` | Normal feature change, endpoint/service behavior, two affected files or layers | 1 | 8 | 5 | 1,300 |
| `deep` | Authentication, authorization, PII/encryption, billing, DB migration/schema, unsafe concurrency, cross-session conflicting edits, or broad changes | 2 | 16 | 12 | 3,300 |

*Budgets are **targets for route-associated context**, not enforced or measured model token usage. They exclude full source files, Spec Kit prompt history, model internal context and output. Limits can be overridden in `.agents/state/context-policy.json`. The script never reads source code to make its decision; it uses path names and cached symbol names.

Order of precedence: explicit observed high-risk path/topic or intersecting external changes → `deep` safety floor. Otherwise auto derives mode from scope and low-risk categories, with default `balanced`. `--mode minimal|balanced|deep` allows user override except the **deep safety floor**. Automatic classification is heuristic and may miss risk. Review scope before implementation, particularly when source metadata is incomplete.

**Routing budget cannot override mandatory rules:** Always follow `AGENTS.md` and read authoritative approved requirements/security documents when applicable. Do not hide dependencies or security gates to meet a token target.

## Spec Kit integration

When Spec Kit is installed, run routing at pre-plan and pre-implement gates and let `specs/<active-feature>/spec.md` and `tasks.md` remain Spec Kit's authority. Resolve active feature only from observed workspace metadata. `context-pack.json` points to paths and should not duplicate Specs or the `.summerize.md` hierarchy. When spec/plan/tasks are unchanged, avoid recreating them; an implementation continuation may use its checkpoint. Do not assume Spec Kit is installed when `.specify/` is missing.

## Limitations and security

- `session_guard` sees **local Git only**. It cannot detect remote commits until the user separately authorizes fetching via the proper GitHub account.
- `.agents/state/` belongs to the local working copy; do not treat it as shared authoritative data or automatically commit it.
- File mtime/hash cache and lexical symbol extraction are not compiler-verified semantic dependencies.
- The router never reads config contents, only manifest/graph/symbol metadata. Sensitive config paths are returned as `metadata_only_paths`, not read targets.
- A missing static link is **unknown**, not `SAFE`.
- `context-pack.json` contains no task description, source body, env values or external request payload.
