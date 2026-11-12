# Spec2Code v0.6.1 — Universal layout and Spec Kit integration

## Ownership boundaries

| Location | Primary writer | What is stored |
| --- | --- | --- |
| `AGENTS.md` | Host project owner | Mandatory rules for the target repo |
| `.specify/`, `specs/` | Official GitHub Spec Kit process | Constitution, selected feature, approved specs, plans and tasks |
| `.agents/skills/spec-to-code/` | Spec2Code installer / human reviewer | Portable skill, scripts and references |
| `.agents/state/` | Local Spec2Code scripts | Git snapshot, graph, adaptive mode, active session and context pack |
| `.summerize.md` and `<Layer>/**` | Local architecture index writer | Lightweight layer/component/function routing docs |
| `.handoffs/.details/` | Active session writer | Pending visualChange/specChange journals |
| `.handoffs/.buildnotes.handoff.md` | Safe exact-session merge | Indexed archived changes |
| `src/`, `app/`, `.source/`, etc. | Host application development | Implementation, tests and configuration |

## Token-aware flow

1. `session_guard.py start`: local Git/infrastructure inventory. No model-side source scanning.
2. `speckit_bridge.py --stage status|plan|implement`: validate active feature and artifact existence. No model-side full spec reading.
3. `context_router.py ... --mode auto --speckit-stage implement`: route just the current task's files and dependency neighbors; embed compact Spec Kit artifact locations and hashes into the context pack.
4. Agent invokes official Spec Kit stages in its native command syntax; it reviews actual relevant spec sections and builds/modifies code only when authorized.
5. `record → checkpoint → finish → merge`: preserve change provenance and handoff history.

No duplicate spec bodies, architecture graphs, task lists or Git histories are generated. `context-pack.json` contains path-only pointers, not source or business data.

## Compatibility

- No mandatory `.source` or framework-specific namespace. Static classification uses conventional roots and lexical names; validate unusual monorepo layouts manually.
- Python 3.10+ core. Spec Kit is an external dependency; official process agent skills do not run merely because the bridge finds `spec.md`.
- Spec Kit feature paths outside the checkout and symlinked feature pointers are rejected by this adapter, even though upstream Spec Kit supports broader overrides. This protects tool isolation.
- Do not overlay a live v0.6 installation; complete existing sessions and archive state first. Managed document markers and Session IDs changed in this release.
