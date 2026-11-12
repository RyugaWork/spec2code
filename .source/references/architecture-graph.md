# Evidence-based universal layer graph

`./.summerize.md` links to optional layers: Governance, Present, API, Application, DataAccess, Persistence, Security, Integrations, Delivery, Quality. Generated documentation is a routing index, not proof that a fixed stack or dependency exists.

The graph has **no assumed cross-layer edges by default**. Static observations may add edges such as C# `ProjectReference` or entrypoint registration. Symbol extraction supports limited Python, JavaScript/TypeScript and C# declaration patterns, but cannot prove dynamic calls, business behavior or cross-language dependencies.

Graph edges are `from` consumer, `to` dependency, labeled with an evidence level and an evidence path when available. An absent edge means **not observed**, not guaranteed independent.

## Storage

- `.agents/state/infrastructure.json`: source-path metadata and safe file facts.
- `.agents/state/system-graph.json`: observed layer nodes and edges.
- `.agents/state/symbol-cache.json`: bounded lexical declarations.
- `.agents/state/impactMatrix.md`: impact from observed edges; 3 = direct/high, 2 = intermediate, 1 = indirect, 0 = not observed.
- `./.summerize.md` and layer/component/function `.summerize.md` documents: compact navigation only.

## Token controls

Default to Minimal for one low-risk file, Balanced for an ordinary task, and Deep for security, schema, cross-layer or external-drift risk. A mode never certifies missing dependencies or replaces tests. Source body is not copied into machine context packs.
