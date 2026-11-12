# Gymuro Architecture Index — v0.6

This is a **schematic** layout, not a claim that these source controllers already exist in Gymuro-Project.

```text
Gymuro-Project/
├── .handoffs/
│   ├── .details/
│   │   ├── .visualChange.GYM-YYYYMMDD-HHMMSS-XXXXXXXX.md   # pending external changes
│   │   └── .specChange.GYM-YYYYMMDD-HHMMSS-XXXXXXXX.md     # pending skill-authored changes
│   └── .buildnotes.handoff.md       # consolidated short handoff + verified history
├── .summerize.md                   # root matrix + graph of layers
├── Present/
│   ├── .summerize.md               # frontend layer and component matrix
│   └── MemberPage/                 # sample observed frontend component
│       ├── .summerize.md
│       └── .MemberPage.MemberPage.md # function doc, version, source and last change
├── API/
│   ├── .summerize.md
│   └── MemberController/           # sample observed API controller
│       ├── .summerize.md
│       └── .MemberController.GetMember.md
├── Application/.summerize.md
├── DataAccess/.summerize.md
├── Persistence/.summerize.md
├── Security/.summerize.md
├── Integrations/.summerize.md
├── Delivery/.summerize.md
├── Quality/.summerize.md
├── Governance/.summerize.md
└── .agents/
    ├── skills/spec-to-code/
    │   ├── SKILL.md
    │   ├── scripts/
    │   ├── references/
    │   └── tests/
    └── state/                       # machine-only snapshots and session IDs
```

## Session lifecycle

`start` → `incremental scan` → `architecture summary/graph` → `spec-to-code` → `record` → `checkpoint` → `finish` → `merge --session-id <ID>`.

Before removing `.visualChange.<ID>.md` or `.specChange.<ID>.md`, `merge` requires the exact finished session, correct pending log header, SHA-256 identity, persisted ledger marker and byte-for-byte recheck. On failure, the pending file must remain.

## Provenance

- **visualChange:** outside-session drift (Git commit without the current session trailer, or change detected between completed sessions).
- **specChange:** changes explicitly registered through the current skill workflow. Non-registered local edits are `UNATTRIBUTED` and can block finish.
- **buildnotes:** merge only after session close. It keeps an eight-session quick summary while retaining full archived event notes in a ledger section.

## Cost constraints

Source metadata and hashes are processed locally. Symbols are extracted and cached from only eligible files; the model should read no full machine JSON by default. Open root `.summerize.md` then only relevant layer/component/function docs. All graph edges are evidence-labeled, and no runtime/deployment verification is claimed.

## Adaptive routing add-on (no hierarchy migration)

`context_router.py` reads existing `.agents/state/infrastructure.json`, `system-graph.json`, `symbol-cache.json`, `architecture-docs.json`, `session.json` after session preflight, and writes just `.agents/state/context-pack.json`. The optional `.agents/state/context-policy.json` is local-only; use `references/context-policy.example.json` to create an override. All `.summerize.md`, controller function docs, `.handoffs/` paths, and source paths remain unchanged.
