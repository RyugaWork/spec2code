# AGENTS.md — Spec2Code v0.7.0

This repository develops an independent universal Spec-to-Code agent skill. Do not introduce project-specific hardcoding, credentials or business-domain assumptions.

## Ownership and required records

- Runtime source of truth: `.source/SKILL.md`, `.source/.config/*.json`, `.source/scripts/`, `.source/references/`, `.source/integrations/`, `.source/tests/`.
- Developer policy: `.agents/.spec.md`, `.agents/.features.md`, `.agents/.plans.md`, `.agents/.risk.md`, `.agents/.checklist.md`, `.agents/.structure.md`, `.agents/.workflow/`, `.agents/.handoffs/`, `.agents/.changelog.md`.
- Before writing code, update the plan and risk register. Record feature status as IMPLEMENTED, IN PROGRESS, PLANNED, DEFERRED or DROPPED accurately.
- After coding, update checklist and write a dated handoff recording exact changes, evidence, limits and rollback. Do not label tests PASS without results.
- Follow the existing host repository's `AGENTS.md` and approved requirements when installed; no host source or Spec Kit artifacts may be replaced based on these repository governance files.

## Runtime invariants

- Strict checkout-only `path_guard.py` and `scope_io.py` gates for every entrypoint and managed file access.
- Host `.agents/state/` and `.handoffs/` are runtime output; developer governance `.agents/.handoffs/` is different.
- Config remains within the installed bundle adjacent to scripts. Do not relocate target runtime files to development repo `.agents/`.
- Do not silently relax traversal, symlink/junction, physical worktree identity, MCP capabilities, sensitive-data exclusions or exact-session SHA-256 verification.
- No automatic commit, push, merge, rebase, force push, arbitrary shell, deletion, or Spec Kit stage execution without explicit authorization.
- Path checking is **not** sandbox authorization for unrelated AI-agent tools.

## Change gates

1. Requirements/feature → plan → risks → scoped implementation → tests → checklist → handoff → reviewer approval.
2. Development test command: `python -m unittest discover -s .source/tests -v`.
3. Verify Linux and Windows separately; report skipped security tests explicitly. Keep old Windows failures OPEN until reproduced and fixed.
4. Before upgrading installed skill, finish active sessions with their original version; never erase state or silently migrate.
5. `.source/.config/` stores tunable policy data only. Invariants and permissions remain enforced by code/host.
