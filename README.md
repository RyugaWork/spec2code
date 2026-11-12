# Spec2Code

**Universal, infrastructure-aware agent skill with official GitHub Spec Kit integration.**

Version: **0.6.3** (development branch). Use with Python 3.10+ and Git. Core scanning and routing require no hosted AI API. Official Spec Kit is optional and installed separately (Python 3.11+ for its CLI).

## Capabilities

- Path Guard: exact Git worktree-root validation, symlink/path traversal protection, nested-repo exclusion, and safe state/handoff boundaries. See [Path Guard](docs/PATH_GUARD.md).
- Multi-repository support: conventional `src/`, `app/`, `backend/`, `frontend/`, `web/`, `packages/`, `.source/`, test and monorepo layouts; no fixed framework, project namespace or business domain.
- Spec Kit bridge: detects active feature from `.specify/feature.json` / explicit environment override, validates `spec.md`, `plan.md`, `tasks.md`, returns bounded artifact fingerprints and task IDs without duplicate text or modifying Spec Kit files.
- Session ID, local Git drift detection, provenance-aware `visualChange`/`specChange` logs and exact-session verified handoff merging.
- Observed architecture graph, compact `.summerize.md` hierarchy and source-to-function routing.
- Adaptive context modes: `auto`, `minimal`, `balanced`, `deep`.
- Continuous Scope Enforcement: bind sessions to physical Git checkouts; verify repository scope at command boundaries and every file path at access; anchored file operations where supported.
- MCP workspace authorization gate (`mcp_boundary.py`): read-only by default, no client-selected root, no arbitrary shell, session-scoped writes and HEAD freshness checks; **MCP transport/server not yet implemented**.
- Local synthetic regression tests and GitHub Actions CI.

## Install into a target Git project

Copy `SKILL.md`, `scripts/`, `references/` to `<target>/.agents/skills/spec-to-code/` (preserve existing project policy and source structure). See [docs/INSTALL.md](docs/INSTALL.md).

```sh
python .agents/skills/spec-to-code/scripts/session_guard.py --root . start
python .agents/skills/spec-to-code/scripts/speckit_bridge.py --root . --stage status
# After Spec Kit feature spec.md/plan.md/tasks.md exist:
python .agents/skills/spec-to-code/scripts/context_router.py --root . --task-id T001 --task 'Implement approved feature' --paths src/feature.py --mode auto --speckit-stage implement
```

**Replace example paths with paths actually present in your checkout.** A `status` call works even without Spec Kit; `--speckit-stage implement` requires its three artifacts. Use [integrations/speckit/README.md](integrations/speckit/README.md) to install/initialize upstream Spec Kit and invoke its agent skills, not shell process commands.

## Tests

```sh
python -m unittest discover -s tests -v
```

## Safety

No auto-fetch, commit, push, shell delegation, feature approval, remote MCP server, credential ingestion or silent deletion of application files. Spec2Code generates architecture docs and local state in the **target checkout**, not in this portable source repository. `visualChange` is for outside-session changes only. A `README` or `.gitkeep` scaffold is never proof of implemented runtime code.

`v0.6.3` uses an additional per-session physical checkout binding; the earlier v0.6.x series also changed session prefixes and document management markers. Finish and merge any ACTIVE earlier-version session with its original version before upgrading; do not force-delete existing state.

## References

[SKILL.md](SKILL.md) · [Install](docs/INSTALL.md) · [Integration layout](docs/INTEGRATION_LAYOUT.md) · [Spec Kit bridge](integrations/speckit/README.md) · [Architecture graph](references/architecture-graph.md)

## Continuous Scope Enforcement

See [docs/CONTINUOUS_SCOPE_ENFORCEMENT.md](docs/CONTINUOUS_SCOPE_ENFORCEMENT.md). This is per-operation enforcement rather than a background watcher.
