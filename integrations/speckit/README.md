# Official GitHub Spec Kit adapter (Spec2Code v0.6.1)

This integration uses the **upstream GitHub Spec Kit**, not a fork or copied process prompts. The local adapter is `scripts/speckit_bridge.py`. No Spec Kit source code is vendored into this repository.

## Install (in the target project, not the skill source repo)

1. Install the official `specify-cli` following https://github.github.com/spec-kit/installation.html (Python 3.11+).
2. For a new project, run `specify init --here --integration codex --script py`. If an **existing non-empty project** requires `--force`, make a reviewable branch/backup and inspect all generated diffs first.
3. Run `specify version` to check the CLI is available and `specify integration list` to verify the agent integration.
4. Invoke the real Spec Kit stages in your agent. In Codex skills mode the official syntax is `$speckit-specify`, `$speckit-plan`, `$speckit-tasks`, `$speckit-analyze`, `$speckit-implement`, `$speckit-converge` (plus `$speckit-clarify` when needed). Other agents use their own syntax. Do **not** run these as ordinary shell commands.

## Spec Kit → Spec2Code bridge

The official feature selection order is `SPECIFY_FEATURE_DIRECTORY` then `.specify/feature.json` (`{"feature_directory":"specs/001-feature"}`). Git checkout alone does **not** select a feature. This adapter reads that selection, requires a **local, non-symlinked** feature directory and identifies existence/size/hash of `spec.md`, `plan.md`, `tasks.md`. It returns bounded task IDs from `tasks.md` with **no task descriptions**, and checks optional constitution presence. No source or spec body is returned.

```sh
python .agents/skills/spec-to-code/scripts/speckit_bridge.py --root . --stage status
python .agents/skills/spec-to-code/scripts/speckit_bridge.py --root . --stage plan
python .agents/skills/spec-to-code/scripts/speckit_bridge.py --root . --stage implement
python .agents/skills/spec-to-code/scripts/context_router.py --root . --task-id T001 --task 'Implement task' --paths src/feature.py --mode auto --speckit-stage implement
```

`--stage implement` blocks if any of `spec.md`, `plan.md`, `tasks.md` is missing. `--stage plan` requires the spec. `--stage status` works before initialization, returning `NOT_INITIALIZED` or `NO_ACTIVE_FEATURE` rather than fabricating a feature.

## Boundaries and limitations

- The bridge never executes `specify init`, process commands, or arbitrary shell; never copies, modifies or overwrites Spec Kit's own files.
- A READY result only proves required artifacts exist and are statically accessible, **not** that their content is approved, consistent or complete; official Spec Kit analysis and human review remain mandatory.
- Upstream Spec Kit permits feature directory overrides outside the workspace; this adapter **rejects them** to prevent reading external files without explicit authorization.
- `SPECIFY_FEATURE_NO_PERSIST` behavior is owned by upstream; this bridge is always read-only.
- Spec Kit may offer an experimental MCP server independently. This adapter does **not** implement or expose MCP transport; that work is separate.

Official references: https://github.github.com/spec-kit/quickstart.html , https://github.github.com/spec-kit/integrations/cli.html , https://github.github.com/spec-kit/how-to/existing-projects.html .
