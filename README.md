# Spec2Code

Infrastructure-aware Spec-to-Code agent skill with Git drift detection, layered architecture graph, session tracking, provenance-aware change logs and adaptive token budgets.

**Current release candidate:** v0.6.0. This is a source repository for the portable skill. Its current implementation has Gymuro-oriented defaults; general-purpose adapters and MCP support are not yet implemented.

## Features

- Local session guard: unique Session ID, checkpoint, Git drift attribution, safe handoff merging.
- Incremental infrastructure inventory, architecture graph and layer/component/function `.summerize.md` routing.
- Adaptive task modes: `auto`, `minimal`, `balanced` and `deep`.
- Separation of external `visualChange` and current-session `specChange`.
- Optional Spec Kit integration without duplicating `.specify/` or `specs/`.
- Python standard library only; no AI API or GitHub token required for local scanning.

## Installation in a target project

Copy `SKILL.md`, `scripts/` and `references/` into:

```text
<project>/.agents/skills/spec-to-code/
```

From the target repository root:

```powershell
py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . start
py -3 .agents/skills/spec-to-code/scripts/context_router.py --root . --task-id TASK-001 --task "Update one UI label" --paths <existing-source-path> --mode auto
```

Read [docs/INSTALL.md](docs/INSTALL.md), [docs/INTEGRATION_LAYOUT.md](docs/INTEGRATION_LAYOUT.md) and [SKILL.md](SKILL.md) for lifecycle and safety requirements.

## Test

```sh
python -m unittest discover -s tests -v
```

## Scope and security

Local scanner operations do **not** fetch from remote GitHub, push, make commits, approve requirements, or launch Spec Kit by themselves. They inspect only the checked-out repository. Do not commit runtime session state, logs containing confidential data, secrets, or real customer records. Keep source-of-truth business and technical policies in the host project. Treat `docs/AGENTS_PATCH.md` as a proposed integration patch, **not** an automatically installed policy.

This repository is currently public. Review its visibility and all future commits accordingly.
