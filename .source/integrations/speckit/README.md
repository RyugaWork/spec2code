# Official GitHub Spec Kit adapter (Spec2Code v0.6.1)

This integration uses the **upstream GitHub Spec Kit**, not a fork or copied process prompts. The local adapter is `scripts/speckit_bridge.py`. No Spec Kit source code is vendored into this repository.

## Install (in the target project, not the skill source repo)

1. Install the official `specify-cli` following https://github.github.com/spec-kit/installation.html (Python 3.11+).
2. For a new project, run `specify init --here --integration codex`. If an **existing non-empty project** requires `--force`, make a reviewable branch/backup and inspect all generated diffs first.
3. Run `specify version` to check the CLI is available and `specify integration list` to inspect the agent integration. For an existing Spec Kit project, inspect the workspace and use `specify integration install codex` when adding Codex; do not overwrite installed files blindly.
4. Review existing `.specify/memory/constitution.md` where applicable, then invoke the real Spec Kit stages in your agent. In Codex skills mode the official syntax is `$speckit-specify`, `$speckit-plan`, `$speckit-tasks`, `$speckit-analyze`, `$speckit-implement`, `$speckit-converge` (plus `$speckit-clarify` when needed). Other agents use their own syntax. Do **not** run these as ordinary shell commands.

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

## PLAN-081 agent integration and upstream process updates

The official upstream SDD workflow includes an initial project **constitution** and optional **clarify**, **checklist** (requirements quality) and **analyze** gates around specify/plan/tasks/implement/converge. The `converge` process can append outstanding work to the active `tasks.md` under upstream ownership; S2C does not invoke or approve that edit. Codex's native `$speckit-<command>` skills live under `.agents/skills/speckit-*/SKILL.md`; other integrations use their own syntax. Validate current commands and multi-install safety against the upstream docs rather than assuming another coding agent uses the same slash/dollar prefix. The official Spec Kit may also supply separate bug-fix and idea-assessment processes; these are not mandatory S2C workflow stages and must not be inferred from a branch or merely from a directory name.

The S2C `.config/speckit.json` and read-only bridge deliberately model only their implemented subset of artifact-existence preflight. A missing optional stage in the S2C stage list is **not** proof that upstream lacks that stage. Do not change bundled stage validation or claim integration support from this documentation edit alone.

References: https://github.github.com/spec-kit/quickstart.html and https://github.com/github/spec-kit/blob/main/docs/integrations/codex.md .


## PLAN-092 — Developing Spec2Code itself using Spec Kit

This guide originally described **optional use inside an installed host**. The S2C development repository now also has [a native-compatible Markdown bootstrap](../../../.specify/README.md), a draft [Constitution](../../../.specify/memory/constitution.md), and active [feature artifacts](../../../specs/001-s2c-speckit-integration/spec.md). They are **not** artifacts generated by `specify init` and do not mean the upstream skills/scripts are installed.

### ChatGPT Web / GitHub mode

1. Read root `AGENTS.md`, the global `.agents/.spec.md`, RTM/risk and `.specify/memory/constitution.md`.
2. Read `.specify/feature.json` and the pointed feature `spec.md`, `plan.md`, `tasks.md`. The official feature pointer is independent from the selected Git branch.
3. Use the connected GitHub app to update scoped Markdown, report source SHA, run a **document-only** consistency review, and maintain a truthful handoff. This imitates the *document workflow*, not native Spec Kit agent skill execution or CLI test status.
4. STOP at A.1/human authority for code tasks; keep independent B.1/release review.

### Native Codex / GitHub Codespaces / Copilot mode

1. Select an **approved, pinned official Spec Kit release** following S2C conservative technology policy. Upstream documentation: https://github.github.com/spec-kit/how-to/existing-projects.html and https://github.github.com/spec-kit/installation.html .
2. In a backed-up disposable checkout, check `specify version` and inspect collisions under `.specify/` and the selected agent skills directory. Installing official CLI and coding-agent skills is a *separate* action from this repository's manual Markdown bootstrap.
3. For an existing checkout, the official pattern is `specify init --here --force --non-interactive --integration <approved-key> --script py`, **only after authorizing the overwrite/collision scope**. Review generated scripts/templates/skills and the preserved active feature pointer; do not silently apply to the working branch.
4. Use the official agent's actual Spec Kit commands after installation, alongside S2C's A.1/B/B.1 gates. Do not enable the optional git extension unless requested; S2C uses one latest working branch.

### Existing bridge preflight (read-only)

On a real local checkout with the portable source available:

```sh
python .source/scripts/speckit_bridge.py --root . --stage status
python .source/scripts/speckit_bridge.py --root . --stage analyze
```

The bridge's **static** `READY` only proves that required native artifacts exist, not that `specify init`, Analyze, Implement, regression tests or approval occurred. This bootstrap does not introduce a new JSON API or alter the existing bridge. For host installs the existing `.agents/skills/spec-to-code/scripts/` path still applies.

**Upstream compatibility note:** the official Constitution is `.specify/memory/constitution.md`, not `.specify/constitution.md`. In all modes feature files remain upstream-owned; S2C only maintains cross-references and gates.

### PLAN-093 — Actual native setup status

[SK-03 pinned official CLI pilot plan](../../../.agents/.documents/specKitNativePilot.md) documents the real environment blocker and safe disposable checkout commands. The CLI `specify` was absent and the attempted offline `uvx` execution failed because no Git dependency could be fetched; therefore no claimed upstream `specify init`, generated skills/scripts, or native prerequisite test. Candidate `v1.2.6` is for **owner-reviewed disposable testing only**, not a universal supported default. Official latest security changes and actual host compatibility must be assessed before adoption.

### PLAN-094 feature design and trace

[Feature spec](../../../specs/001-s2c-speckit-integration/spec.md), [upstream research](../../../specs/001-s2c-speckit-integration/research.md), [plan](../../../specs/001-s2c-speckit-integration/plan.md), [logical model](../../../specs/001-s2c-speckit-integration/data-model.md), [Web/Native logical contract](../../../specs/001-s2c-speckit-integration/contracts/web-native-interface.md), [quickstart](../../../specs/001-s2c-speckit-integration/quickstart.md) and [24-case quality design](../../../specs/001-s2c-speckit-integration/checklists/integrationAcceptance.md) now refine the **S2C-development** feature. [RTM Section L](../../../.agents/.traceMatrix.md) links 12 individual requirements to 24 planned cases. No corresponding runtime schema/worker/CLI change is implemented merely because these Markdown artifacts exist. Actual native CLI, source/host security tests, A.1/B.1 and owner authorization remain pending.


### PLAN-096 — Read-only bridge is NOT a semantic feature validator

[Actual source audit](../../../.agents/.documents/specKitBridgeSourceAudit096.md) found that the existing `speckit_bridge.py` verifies repository containment, basic file presence/hashes and bounded task-ID collection, **but does not** currently enforce the feature-spec `specs/<id>` namespace, reject duplicate `feature_directory` JSON keys, classify zero-byte required artifacts as incomplete or reject duplicate task IDs. These are **source-to-feature contract gaps**, not observed native regressions. The four planned `SK96-NEG-01..04` host tests are NOT_RUN and require real unmodified bundled guard dependencies plus authorized host execution. Do not treat `READY` as requirements-quality PASS or A.1/B permission.

## PLAN-109 / M02 — Upstream bridge evidence equivalence matrix

Differentiate `source_static_validated` (the bridge's current read-only artifact checks), `web_document_committed` (GitHub fast-forward readback), `native_cli_observed` (real official version/help and source/pointer side effects), and `host_containment_verified` (approved OS sandbox with negative external sentinels). None of the earlier levels implies a later one. A bridge `READY` is not upstream Spec Kit or semantic requirements review success.

During an authorized native pilot, pin the exact feature reference and official Spec Kit release, sanitize inherited feature-directory environment, monitor `.specify/feature.json` before/after and record unexpected writes; deny `implement` or convergence without explicit task and Phase-B permissions. On partial output or unavailable native CLI, preserve source-bound logs and mark native cases `NOT_RUN`. T011/T012/T015 remain human decisions, not tool-generated checkboxes.
