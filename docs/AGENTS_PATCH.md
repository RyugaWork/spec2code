# Proposed AGENTS.md Addition — Gymuro Spec-to-Code v0.6

This is an opt-in **proposal**; do not replace the existing root AGENTS.md or weaken its canonical business requirements, scope authority, auth/security, test, Git or account-selection rules.

```markdown
## Spec-to-Code session and architecture routing

For every new coding session, run
`py -3 .agents/skills/spec-to-code/scripts/session_guard.py --root . start`
before reading feature source. The command assigns a unique Gymuro Session ID,
checks local Git drift since the previous snapshot, incrementally indexes source,
and creates an evidence-based architecture pathing graph. No GitHub remote check
is implied or performed.

Read `./.summerize.md` only to select affected layers, then the relevant
`<Layer>/.summerize.md`, `<Layer>/<Component>/.summerize.md`, and the exact
`.<Component>.<Function>.md` for the affected function. Do not scan all docs
or read entire machine snapshots by default. `Present` is the web layer;
other layers have the same hierarchy. The intentional `.summerize.md` spelling
is a stable project path, not a typographic correction.

Change provenance uses per-session **pending** logs:
- `.handoffs/.details/.visualChange.{SessionID}.md` — external/outside-session
  drift, never current session's explicitly authored edits;
- `.handoffs/.details/.specChange.{SessionID}.md` — edits the current session
  explicitly registered with `record`;
- `.handoffs/.buildnotes.handoff.md` — short merged handoff and full audit ledger.

Finish with `session_guard.py finish`; then explicitly run
`session_guard.py merge --session-id <EXACT-ID>` only when the session is closed.
Merge validates session ID, logged content and persisted evidence before
removing only the corresponding pending files. No wildcard cleanup.

Do not auto-commit, push, fetch or rewrite Git state. For a separately approved
in-session commit, use `Gymuro-Session: <ID>` in a Conventional Commit trailer.
Unregistered/unattributed source edits must block finish until reconciled.
```

## Optional .gitignore review

- `.agents/state/` holds local, non-shareable working snapshots, active session state and symbol indexes. Prefer ignoring these in collaborative repositories.
- `.handoffs/.details/` contains unmerged pending logs: decide deliberately whether to version them or keep machine-local; if ignored, preserve them until successfully merged. **Do not** indiscriminately ignore `.handoffs/.buildnotes.handoff.md` if it is intended as shared documentation.
- `.summerize.md`, `<Layer>/.summerize.md` and function architecture docs are generated evidence indexes. Decide whether to track them to provide reviewable snapshots. Generated docs do not replace approved specifications.
- `.handoffs/.merge.lock` is a local temporary lock; do not commit it.
- Review actual repository ignore conventions and contributor permissions before changing anything.

## ADDENDUM — Adaptive context routing v0.6 (owner review before applying)

Before code changes, run the existing Spec-to-Code session guard and the adaptive context router under `.agents/skills/spec-to-code/scripts/`. The router defaults to `--mode auto`, selecting Minimal/Balanced/Deep according to task risk, observed affected source paths/layers, and outside-session drift; manual mode selection is permitted except when it attempts to bypass a Deep security/drift gate. Use the existing `./.summerize.md` → layer → component → function documentation; `.agents/state/context-pack.json` contains only pointers to these documents. Do not make a second graph or copy Specs into architecture summaries. Do not read the full state directory into LLM context. When Spec Kit is installed separately, pass the narrow context pack to its Plan/Implement stages and keep `.specify/` / `specs/` as canonical feature artifacts. Continue to classify external change in `visualChange` and current-session registered change in `specChange`. Local mode decisions do not authorize source modifications or GitHub operations.
