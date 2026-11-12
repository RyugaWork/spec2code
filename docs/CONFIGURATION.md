# Spec2Code v0.7.0 — Bundled configuration

The skill keeps **policy data** in `.config/*.json`; Python modules implement the algorithms and enforce non-configurable security invariants. The configuration directory is **required**, versioned and deployed *inside the installed skill*, not at an arbitrary home/current working directory.

```text
spec-to-code/
├── SKILL.md
├── .config/
│   ├── scanner.json        # source roots, file-type inventory, exclusions, caps
│   ├── architecture.json   # layer directories, source classification, docs limits
│   ├── routing.json        # adaptive context modes, budgets, task stopwords
│   ├── session.json        # layer descriptions, local state filenames and caps
│   ├── speckit.json        # artifacts, stages, stage prerequisites and limits
│   ├── handoff.json        # paths, event types, output markers and limits
│   ├── mcp.json            # *currently supported* request/action metadata
│   └── security.json       # additional sensitive names and managed paths
├── scripts/
│   ├── config_loader.py
│   └── ...
└── references/
```

## How values are loaded

1. Every Python module loads its section with `config_loader.load('scanner')`, etc.
2. The loader searches **only** `<script-parent>/.config/<section>.json` within the adjacent development `.source/` or installed-skill bundle. It will not walk ancestors, read the target project's root `.config`, or use environment-variable fallback paths.
3. JSON files are versioned (`schema_version: 1`), bounded (64 KiB each), checked for duplicate keys, strict top-level fields, unsafe paths, invalid types, symlinks and contradictory policies. Invalid or missing files fail with `CONFIG_INVALID`.
4. Values are loaded once per process; updating JSON requires restarting the Python process. File-system access still goes through Path Guard/Scope IO where appropriate.

## Configuration vs authorization

- `scanner.json` and `security.json` may **add** indicators and ignore/sensitive paths, but cannot remove the mandatory protection for secrets, credential files or `.git`.
- `architecture.json` cannot direct generated layer state into source directories such as `src/` or `backend/`; all state JSON paths must remain in `.agents/state/` and all handoff paths in `.handoffs/`.
- `routing.json` defines the bundled baseline. The optional target-specific `.agents/state/context-policy.json` may tune budgets or add risk indicators. Its values cannot suppress the bundled high-risk patterns. A requested minimal/balanced mode still cannot override an evidenced Deep risk floor.
- `speckit.json` is **metadata**, not the upstream Spec Kit installer. At least `spec.md`, `plan.md`, `tasks.md` are always required for implementation.
- `mcp.json` documents the fixed implemented action set. Editing JSON **cannot** invent a tool, enable arbitrary shell or grant write permission. A separate trusted MCP host and authorization policy are still required.
- Git checkout identity, physical worktree/session binding, filesystem anti-traversal/symlink handling, session ID format, MCP permission boundaries and handoff integrity checks remain code-level invariants. These are intentionally not configurable, even though most routine data moved to JSON.

## Migrating existing installations

Finish and merge any active session with its original installed version. Copy **all** of `SKILL.md`, `.config/`, `scripts/`, and `references/` together into `.agents/skills/spec-to-code/`. Do not replace only one `.py` file. Preserve the target repository's `.agents/state/`, `.handoffs/`, `.specify/`, and `specs/` directories; they are not bundled defaults. Run:

```sh
python -m unittest discover -s .source/tests -v
python .agents/skills/spec-to-code/scripts/speckit_bridge.py --root . --stage status
```

No new database/service or Python dependency is required. JSON is used instead of arbitrary `.py`/`.env` evaluation so config remains portable and reviewable.

## v0.7.0 development repository

The authoritative runtime JSON files are in `.source/.config/`. The separate `.agents/.config/` directory is for developer governance, not loaded by `config_loader.py`. Both source and installed skill must keep `scripts/` and `.config/` as siblings.
