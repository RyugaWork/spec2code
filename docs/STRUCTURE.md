# Universal target project layout — Spec2Code v0.7.0

```text
<target-project>/
├── AGENTS.md                                   # optional host governance
├── .specify/                                   # optional official Spec Kit
│   ├── feature.json
│   └── memory/constitution.md
├── specs/<feature-id>/
│   ├── spec.md
│   ├── plan.md
│   └── tasks.md
├── .agents/
│   ├── skills/spec-to-code/
│   │   ├── SKILL.md
│   │   ├── .config/                            # bundled versioned JSON policy
│   │   ├── scripts/
│   │   │   ├── speckit_bridge.py
│   │   │   ├── session_guard.py
│   │   │   ├── context_router.py
│   │   │   └── ...
│   │   └── references/
│   ├── state/                                  # local machine snapshots
│   └── .handoffs/
│       ├── .details/
│       │   ├── .visualChange.<SessionID>.md
│       │   └── .specChange.<SessionID>.md
│       └── .buildnotes.handoff.md
├── s2c/                                        # generated architecture indexes
│   ├── .summerize.md                           # legacy spelling retained
│   ├── Present/.summerize.md
│   ├── API/.summerize.md
│   ├── Application/.summerize.md
│   ├── DataAccess/.summerize.md
│   ├── Persistence/.summerize.md
│   ├── Security/.summerize.md
│   ├── Integrations/.summerize.md
│   ├── Delivery/.summerize.md
│   ├── Quality/.summerize.md
│   ├── Governance/.summerize.md
│   └── <Layer>/<Component>/
│       ├── .summerize.md
│       └── .<Component>.<Function>.md
└── src/ or app/ or backend/ or web/ or .source/ ...
```

## Ownership and migration

This layout belongs to the **target Git checkout** and must not be confused with the Spec2Code development source layout. The host owns its application source and AGENTS.md; upstream Spec Kit owns `.specify/` and `specs/`. Spec2Code's installed runtime writes only bounded generated outputs inside `.agents/state/`, `.agents/.handoffs/` and `s2c/` after permission and path checks.

Prior releases wrote handoffs in `.handoffs/`, and architecture summaries at root `.summerize.md` and root-level layer folders. Existing data is **never implicitly migrated, overwritten or deleted**. A reviewed backup/migration process is required if old evidence or session state exists. `s2c/` collisions with user-owned content must fail closed.

Generated layer folders are metadata only; they are not replacements for real source directories and do not prove runtime behavior. The historical spelling `.summerize.md` is retained for compatibility.
