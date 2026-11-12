# Install Spec2Code v0.6.3 in any Git project

This is a **portable skill + local Python core**, not an installer that can rewrite projects without review.

## Prerequisites

- Python 3.10+ for core scripts; local Git.
- Optional: official GitHub Spec Kit's `specify-cli` (currently Python 3.11+), installed separately. See `integrations/speckit/README.md`.
- An exact, non-bare Git worktree root. Spec2Code v0.6.2 rejects non-repo roots, nested working directories, root aliases and symlinked runtime paths. See [Path Guard](PATH_GUARD.md).
- A clean or reviewable working tree. Check for existing `.agents/skills/spec-to-code`, `.agents/state` and `.handoffs` before installing. Never overwrite an ACTIVE session.

## Install

Copy the top-level `SKILL.md`, `scripts/`, and `references/` folders from this repository into **one** target location:

```text
<target>/.agents/skills/spec-to-code/SKILL.md
<target>/.agents/skills/spec-to-code/scripts/
<target>/.agents/skills/spec-to-code/references/
```

Retain the original target `AGENTS.md`, business/security policies, source layout and Spec Kit files. The optional agent instructions in `docs/AGENTS_PATCH.md` require separate review.

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
- `.agents/state/`, `.summerize.md`, generated layer docs and `.handoffs/` are owned by the target checkout's Spec2Code runtime, not by the portable skill repository.
- Do not switch versions over a live older session. Finish and merge it using the old matching version, back up generated state, and rebaseline before adopting new session formats/managed markers. No wildcard cleanup.
- Existing hand-written `.summerize.md` and layer docs are not silently overwritten; collisions block rather than destroy data.
- Core has no MCP endpoint, arbitrary shell tool, GitHub remote fetch, automatic push or Spec Kit stage executor.

## Test

```sh
python -m unittest discover -s tests -v
```

Regression tests use disposable local repositories. The target project's own build and acceptance tests remain mandatory before code changes are reported as verified.

## Path-bound sessions

From v0.6.3 onward, an ACTIVE session is tied to the exact physical Git worktree. Complete and merge old-version sessions using the original skill before upgrading. See [Continuous Scope Enforcement](CONTINUOUS_SCOPE_ENFORCEMENT.md).
