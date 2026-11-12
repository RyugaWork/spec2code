# AGENTS.md — Spec2Code

- This repository develops a **portable, universal** Spec-to-Code agent skill. Do not introduce application-specific dependencies, business rules, names, credentials or user data into the core.
- Source of truth: `SKILL.md`, Python `scripts/`, `references/`, `integrations/`, and `tests/`. Target application state is not stored here.
- Keep the official Spec Kit separate and follow upstream artifact ownership for `.specify/` and `specs/`; this repository's bridge is read-only toward those files.
- Before changing session, scanner, graph or handoff behavior, update/execute applicable unit tests. Commands: `python -m unittest discover -s tests -v`.
- `scripts/path_guard.py` is the mandatory repository boundary for **every** CLI and programmatic entrypoint, including new MCP adapters. Never operate outside the exact validated Git worktree. Validate both user paths and cached paths; no fallback on failed checks.
- Do not bypass symlink/path traversal checks, session provenance, sensitive-config exclusions or exact-session SHA-256 handoff verification.
- Git commits use Conventional Commits 1.0.0. Do not commit, push, merge, rebase or force-push without appropriate authorization.
- Generated `.agents/state/`, `.handoffs/` pending files, secrets and test caches must not be committed.
- A context pack is **path-only**, not source/spec text; never claim a static scan proves runtime behavior or project-specific requirements.
