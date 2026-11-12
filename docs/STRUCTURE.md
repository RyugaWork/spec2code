# Universal target layout (schematic)

```text
<target-project>/
├── AGENTS.md                            # optional host governance
├── .specify/                            # official Spec Kit files (if installed)
│   ├── feature.json                     # machine-local active feature pointer
│   └── memory/constitution.md
├── specs/<feature-id>/                   # official feature artifacts
│   ├── spec.md
│   ├── plan.md
│   └── tasks.md
├── .agents/
│   ├── skills/spec-to-code/
│   │   ├── SKILL.md
│   │   ├── scripts/speckit_bridge.py
│   │   ├── scripts/session_guard.py
│   │   ├── scripts/context_router.py
│   │   └── references/
│   └── state/                            # machine-generated snapshots, never wholesale prompt context
├── .summerize.md                        # indexed architecture graph, original spelling retained
├── Present/.summerize.md
├── API/.summerize.md
├── Application/.summerize.md
├── DataAccess/.summerize.md
├── Persistence/.summerize.md
├── Security/.summerize.md
├── Integrations/.summerize.md
├── Delivery/.summerize.md
├── Quality/.summerize.md
├── Governance/.summerize.md
├── <Layer>/<Component>/
│   ├── .summerize.md
│   └── .<Component>.<Function>.md
├── .handoffs/
│   ├── .details/.visualChange.<SessionID>.md
│   ├── .details/.specChange.<SessionID>.md
│   └── .buildnotes.handoff.md
└── src/ or app/ or backend/ or web/ or .source/ ...
```

The layer directories are metadata only and are **not** replacements for application source directories. The scanner only emits observed function docs. It will not create fake controllers or infer runtime behavior from the layout alone.
