# Session protocol and provenance — v0.3

Read this file when a session is interrupted, Git diverges, or authorship is disputed. Otherwise rely on SKILL.md and the one-line session_guard output.

## State machine

`NONE / CLOSED -> start -> ACTIVE -> [record, checkpoint]* -> finish -> CLOSED`.

- `start` refuses when another session remains ACTIVE. Retrieve the ID with `status` and continue that session instead; the tool does not guess whether a prior process is still running.
- A new ID follows `S2C-YYYYMMDD-HHMMSS-XXXXXXXX` with UTC start and a random suffix; log the ID in a handoff/commit trailer when authorized.
- First-ever scan creates a `BASELINE`: it never claims all source files are newly authored or externally changed.
- `start` compares the previous snapshot with present files, computes new local commits since the last saved HEAD, and logs differences as `OUT_OF_SESSION` in `.handoffs/.details/.visualChange.{SessionID}.md`.
- `checkpoint` detects commits since the session's last observed HEAD. Commits without matching `Spec2Code-Session:` are external **to the skill session**, and their changed paths appear in `.handoffs/.details/.visualChange.{SessionID}.md`. Other unrecorded local edits remain `UNATTRIBUTED`, not external.
- `record --paths <path...> --note <note> --requirement <id>` asserts this session intentionally authored specific source/config changes. Only actual modified/new/deleted paths since session start are recorded in `.handoffs/.details/.specChange.{SessionID}.md`. Repeat after further edits.
- `finish` refuses if any final difference is neither accounted for by an external commit nor represented by a matching final registered fingerprint. Correct attribution before closure; never auto-register another person's work.
- `sessions.jsonl` is a JSON Lines history of session START/FINISH metadata; state machine's active snapshots remain in `session.json`.

## Commit convention

When the owner independently authorizes a commit, use an existing conventional commit message plus trailer:

```text
feat(api): implement approved endpoint

Spec2Code-Session: S2C-20261112-110500-A3F29C81
```

Matching trailer is an attribution convention, **not** a trusted identity signature. The log preserves hash prefixes and paths but does not expose email, file body, secrets, full diffs or commit message contents.

## Recovery and uncertainty

- **Uncommitted modifications made while ACTIVE:** A timestamp/file delta alone cannot prove which person/editor made them. Record only files the agent itself edited. Unregistered files block `finish` (fail-closed).
- **Unexpected incoming local commits:** Run `checkpoint`, inspect the affected paths, reconcile with your current task. Do not merge, reset, stash or rebase automatically.
- **Non-fast-forward / rewritten HEAD:** Return `HISTORY_DIVERGED`. Preserve state; require explicit human reconciliation and separately authorized Git actions.
- **Power loss / interrupted agent:** `status` shows ACTIVE. Resume the same ID, check its last checkpoint, identify any ambiguous files, then close it; never fabricate an event or start a second concurrent ID.
- **No local Git / no commit:** The guard fails rather than claiming commit comparison. Initialize/restore only with explicit authorization.
- **Remote GitHub commit:** Without an authorized `git fetch` or approved GitHub API read, its presence **cannot** be confirmed; only local refs and local commits are inspected.
- **Read-only request:** Do not create session files for planning/audit-only tasks unless writes are explicitly permitted. Use the standalone scanner's read-only dry run and report history attribution as UNVERIFIED.

## Change-log ownership

- `.handoffs/.details/.visualChange.{SessionID}.md` — external/out-of-session changes only; no scanner baseline, no self-authored source changes.
- `.handoffs/.details/.specChange.{SessionID}.md` — authenticated-by-workflow (declared) implementation edits from this session; no automatic descriptions of other's work.
- Official Spec Kit feature artifact edits (`specs/**/*.md`) are permitted in `specChange` only when deliberately made and explicitly registered in the active session. The adapter itself is read-only.

All records are **local observations**. A file existing or Compose declaring a service never proves an application is running or an integration is operational.

## v0.4 safe handoff merge

After a successful `finish`, call `merge --session-id <ID>` for the exact closed session. This verifies headers and SHA-256, appends content to `.handoffs/.buildnotes.handoff.md` and deletes only exactly matched pending files. See `references/hierarchy-layout.md`. Legacy root logs from v0.3 are not automatically migrated or deleted.
