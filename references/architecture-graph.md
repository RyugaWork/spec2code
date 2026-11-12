# Linked layers and impact matrix — v0.3

This reference documents the compact graph; normal operation routes via `./.summerize.md` and only the task-relevant child `.summerize.md` files.

## Layers

| Layer | Typical path / evidence | Depends on |
| --- | --- | --- |
| governance | AGENTS.md, .agents/.documents | - |
| presentation | .source/web | api |
| api | .source/backend/Gymuro.Api | application, security |
| application | .source/backend/Gymuro.Business | data, integrations |
| data | .source/backend/Gymuro.DataAccess/Repositories | persistence |
| persistence | DbContext, migrations, persistence / SQL | - |
| security | ASP.NET Identity middleware, auth code/package signals | - |
| integrations | .source/backend/Gymuro.Infrastructure | - |
| delivery | Docker Compose, .github/workflows | presentation, api, data |
| quality | tests/, .source/backend/tests | presentation, api, application, data |

Edges point **consumer -> dependency** and are labeled `architecture_policy_only`: they must not be construed as verified runtime calls, dynamic imports, or transitive dependencies in compiled code.

## Generated files

- `.agents/state/infrastructure.json`: machine index by path, status, SHA-256/metadata, facts, snapshot HEAD.
- `.agents/state/system-graph.json`: machine nodes, evidence paths, dependency edges.
- `.agents/state/infrastructure-index.md`: short architecture clues, entrypoint and manifests.
- `.agents/state/layerSummary.md`: short layer-state/neighbor table for model context.
- `.agents/state/impactMatrix.md`: automatically derived potential impact for the latest detected changed layers.
- `.agents/state/session.json`, `sessions.jsonl`: machine session provenance. Do not paste full content into model context.

## Matrix scoring

If a file in layer B changes, mark B=3 and propagate influence along **reverse** dependency edges. Direct dependents score 3, two hops 2, three or more hops 1, unrelated 0. Only review 2–3 scores by default. This is an **impact heuristic**, not quantitative risk, production criticality or assurance that a particular workflow failed.

## Evidence quality

- `not_observed` means no candidate files detected, **not** confirmed absence from all systems.
- `scaffold_only` means directory exists with no eligible source; `.gitkeep` is never proof of code.
- `observed_files`, `code_indicators`, `configured_not_runtime_verified` describe local static evidence only.
- New real dependencies should be captured by a reviewed graph-generator change, not by silently inventing new edges.

## Multi-level index (v0.4)

The root `./.summerize.md` links to named layer directories, their component/controller summaries and optional function declarations. Read `references/hierarchy-layout.md` for graph matrix semantics and pending handoff merge protocol.
