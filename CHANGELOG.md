# Changelog

## [0.6.3] - 2026-11-12

### Security
- Bind ACTIVE sessions to physical Git checkout identity and reject session reuse from a different worktree.
- Check boundaries at each command and each file access, with POSIX directory-anchored/no-follow reads, writes, append and verified unlink.
- Invalidate cached context packs on changed commit or selected tracked files at checkpoint.
- Add MCP-ready fixed-workspace authorization gate with read-only default and server-controlled write capability; no remote MCP transport.
- Add continuous-scope adversarial regression tests.

### Migration
- ACTIVE sessions created with an earlier version lack the new binding. Complete them with the original version before upgrading.
- POSIX path operations are hardened; Windows retains repeated checks but cannot promise race-free enforcement without OS isolation.

## [0.6.2] - 2026-11-12

### Security
- Add shared `path_guard.py` to enforce exact Git worktree roots before all CLI actions, including read-only/status/merge calls.
- Bind conventionally installed skills to their own target checkout, including when another valid Git repository is specified.
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
