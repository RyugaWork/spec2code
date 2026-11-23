# Install Spec2Code v0.7.0 in any Git project

This is a **portable skill + local Python core**, not an installer that can rewrite projects without review.

## Prerequisites

- Python 3.10+ for core scripts; local Git.
- Optional: official GitHub Spec Kit's `specify-cli` (currently Python 3.11+), installed separately. See `integrations/speckit/README.md`.
- An exact, non-bare Git worktree root. Spec2Code v0.6.2 rejects non-repo roots, nested working directories, root aliases and symlinked runtime paths. See [Path Guard](PATH_GUARD.md).
- A clean or reviewable working tree. Check for existing `.agents/skills/spec-to-code`, `.agents/state` and `.agents/.handoffs` before installing. Never overwrite an ACTIVE session.

## Install

**Important:** `.source/` is a development-repository directory only. Copy its *contents* (not the `.source` directory itself) to the target skill folder. Preserve its hidden `.config/` folder. This is a manual, reviewable installation; do not overwrite target-owned state or an ACTIVE prior-version skill.


Copy `.source/SKILL.md`, **`.source/.config/`**, `.source/scripts/`, and `.source/references/` from the development repository into **one** target location:

```text
<target>/.agents/skills/spec-to-code/SKILL.md
<target>/.agents/skills/spec-to-code/.config/
<target>/.agents/skills/spec-to-code/scripts/
<target>/.agents/skills/spec-to-code/references/
```

**Do not omit `.config/`: the scripts intentionally fail closed on missing or invalid bundled JSON.** Retain the original target `AGENTS.md`, business/security policies, source layout and Spec Kit files. The optional agent instructions in `docs/AGENTS_PATCH.md` require separate review.

## Example: any checked-out repository

```sh
python .agents/skills/spec-to-code/scripts/session_guard.py --root . start
python .agents/skills/spec-to-code/scripts/session_guard.py --root . inspect --layer application
python .agents/skills/spec-to-code/scripts/speckit_bridge.py --root . --stage status
python .agents/skills/spec-to-code/scripts/context_router.py --root . --task-id T001 --task 'Implement selected function' --paths src/feature.py --mode auto --speckit-stage implement
```

Replace `src/feature.py` with an existing path, and select `--speckit-stage status` if the target does not use Spec Kit. Use `--speckit-stage plan` when only the approved spec exists.

## Data ownership and migration

- `.specify/` and `specs/` are owned by official Spec Kit; the bridge **never writes** these files.
- `.agents/state/`, `s2c/.summerize.md`, generated `s2c/` layer docs and `.agents/.handoffs/` are owned by the target checkout's Spec2Code runtime, not by the portable skill repository.
- Do not switch versions over a live older session. Finish and merge it using the old matching version, back up generated state, and rebaseline before adopting new session formats/managed markers. No wildcard cleanup.
- Existing hand-written `s2c/.summerize.md`, legacy root `.summerize.md` and layer docs are not silently overwritten; collisions block rather than destroy data.
- Core has no MCP endpoint, arbitrary shell tool, GitHub remote fetch, automatic push or Spec Kit stage executor.

## Test

```sh
python -m unittest discover -s .source/tests -v
```

Regression tests use disposable local repositories. The target project's own build and acceptance tests remain mandatory before code changes are reported as verified.

## Path-bound sessions

From v0.6.3 onward, an ACTIVE session is tied to the exact physical Git worktree. Complete and merge old-version sessions using the original skill before upgrading. See [Continuous Scope Enforcement](CONTINUOUS_SCOPE_ENFORCEMENT.md).

## Configuration

See [Configuration](CONFIGURATION.md). The bundled `.config/*.json` belongs **inside** `.agents/skills/spec-to-code/` in each target repository. Do not confuse it with target runtime overrides at `.agents/state/context-policy.json`. Runtime security authority and MCP write privileges cannot be granted by editing JSON.

## v0.7.0 target output migration (review required)

A fresh checkout receives generated architecture documents under `s2c/` and exact-session handoffs under `.agents/.handoffs/`. Existing `.handoffs/` evidence and root-level generated architecture docs **are not automatically migrated or deleted**. Finish/merge ACTIVE older sessions using their matching version, preserve exact bytes and hashes, and approve a manual migration plan before starting the new version. If the host already owns files in `s2c/`, the runtime refuses to overwrite them. The application's own source directories do not move.

## PLAN-080 installation additions

Copy the entire new skill bundle (SKILL.md, .config/, scripts/, references/ and integrations/ where applicable). Do not overlay active v0.7 sessions or replace just one script. Preserve host AGENTS, .specify/, specs/, .agents/state and existing handoffs; perform backup and a reviewed migration if version state changes. Missing new configurations fail closed.

## Optional host AGENTS integration (PLAN-081)

Do **not** install this source repository's root `AGENTS.md` into the target. The existing host's root/nested AGENTS and approved requirements remain authoritative. If the host owner wants S2C operating notes, review [AGENTS_PATCH.md](AGENTS_PATCH.md), confirm the actual installed skill path, current Spec Kit integration and host-specific permissions, then add only compatible lines. A `README` example or `READY` bridge result is never permission to edit, commit or deploy. The role/runbook documents under development `.agents/.workflow/` describe human-directed behavior but are not automatically installed host policy.

## PLAN-116 — First product release installation and upgrade plan (not available yet)

Commands above apply to the existing v0.x **prototype runtime**, not the planned stable v1.0.0 WEB_MARKDOWN profile. Future Markdown distribution proposed at `.source/profiles/web/`, install to host `.agents/skills/spec-to-code-web/` only after review; host-owned project data under mapped existing artifacts or `.agents/s2c-web/` (not duplicate task/spec ledger). Use explicit ChatGPT Project instructions/files or pinned snapshots; connector read only when actual permissions exist. No Python or Spec Kit CLI requirement for Web v1.0; no unattended installation, unapproved file synchronization, implicit write grant or runtime sandbox claim. The approved-path AGENTS integration by an existing capable AI agent is a separately specified proposed exception, not an installer. Legacy runtime files and host state remain intact. Adopt or upgrade by ownership inventory + old/host/new three-way comparison + verified backup + exact approved diff + readback + manifest-version-last + rollback on failure. See [PLAN-116 compatibility and migration contract](../.agents/.documents/markdownFirstReleasePlan.md) and WEB-016..020/024. No actual Web skill/install or migration executed in PLAN-116.

## V1 design amendment — AGENTS.md integration by authorized AI agents (not yet released)

V1.0 additionally **proposes** [AGM-01..17](../.agents/.documents/webV1AgentsIntegrationMatrix.md) as a declarative protocol for new host AGENTS creation, existing AGENTS adoption and later versioned upgrade. An AI agent with actual, host-granted path-scoped write access may perform the bounded matrix comparison, diff, insert/update and readback after V1 design/implementation approvals; without that access, output only the matrix and patch. This is not a local Python installer or unattended sync and does not authorize unrelated repo or Git changes. Preserve nested rules and host customizations, three-way merge old/current/new, stop on conflict, rollback safely and update version last. [WEB-TC-16..21](../.agents/.workflow/testingAndDelivery.md) are planned, not executed; there is still no installed V1 Web distribution.
