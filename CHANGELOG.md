# Changelog

## [0.6.2] - 2026-11-12

### Security
- Add shared `path_guard.py` to enforce exact Git worktree roots before all CLI actions, including read-only/status/merge calls.
- Reject absolute foreign paths, `..`, UNC/drive paths, symlinked managed paths, and unsafe cache-derived document locations.
- Scrub inherited Git environment overrides during root verification, drift tracking, and inventory Git queries.
- Exclude nested Git checkout/submodule content from repository scanning.
- Guard programmatic session, graph, context, Spec Kit and handoff entrypoints ahead of future MCP integration.

### Verification
- Add adversarial path tests for non-Git roots, symlinks, environment overrides, cache traversal and Git worktrees.
- Preserve existing v0.6.1 session, architecture and handoff behavior within a valid checkout.


## [0.6.1] - 2026-11-12

### Added
- Read-only official GitHub Spec Kit feature/artifact bridge with stage prerequisites, path containment and bounded task metadata.
- `--speckit-stage` on adaptive context router; returns artifact paths/hashes in a compact context pack.
- Generic source directory discovery (`src`, `app`, `backend`, `frontend`, `packages`, and others) and Python declaration indexing.
- Integration documentation and synthetic Spec Kit regression tests.

### Changed
- Removed application-specific source namespace and policy assumptions.
- Session identifiers now use `S2C-...`; commit trailer uses `Spec2Code-Session: ...`.
- Architecture graph does not invent framework-specific layer dependencies.

### Migration
- This change updates generated document management markers. Finish existing sessions using their original version, archive state and rebaseline; no automatic destructive migration.

## [0.6.0] - 2026-11-12

Initial infrastructure-aware source snapshot: session tracking, architecture graph, adaptive context routing and handoff tracking.
