# Changelog

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
