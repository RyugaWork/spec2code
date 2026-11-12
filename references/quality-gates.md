# Spec-to-Code Quality Gates

Use as a review checklist; report `PASS`, `FAIL`, `BLOCKED`, or `NOT RUN` with evidence.

## Before implementation
- [ ] Root AGENTS and all applicable specialized policies read.
- [ ] Approved authoritative business requirements and contracts located; speculative rules separated.
- [ ] `session_guard.py start` completed with unique Session ID; previous local commits and outside-session drift checked; placeholders not mistaken for code.
- [ ] Actors, authorization, privacy classification, normal/error flows, AC IDs mapped.
- [ ] No unresolved business, security, data-loss, or API contract blockers in affected scope.
- [ ] Specific implementation scope authorized, independent of Git branch/commit/push authorization.

## During implementation
- [ ] Code placed under `.source/backend/` or `.source/web/` and follows boundary conventions.
- [ ] Authentication scheme correct: Identity Cookie Web vs approved JWT non-Web; CSRF on cookie mutations.
- [ ] Actor ownership, role/permission and current business rules checked server-side.
- [ ] SQL parameters and allowlisted dynamic identifiers used; row-level ownership filtering before paging.
- [ ] `DbContext` never shared across concurrent tasks; cancellation and bounded fan-out where needed.
- [ ] PII protected, errors/logs do not leak secrets, auth tokens not stored in browser localStorage.
- [ ] Caches are isolated by actor/permission and invalidated appropriately.
- [ ] Existing integrations/contracts preserved or compatibility change explicitly approved.
- [ ] Each authored change registered in `.handoffs/.details/.specChange.{SessionID}.md` using `record` with current session and requirement ID; outside-session change goes only to `.handoffs/.details/.visualChange.{SessionID}.md`.

## Before claiming done
- [ ] Each AC maps to code paths and a real test/check result.
- [ ] New test source (if authorized) kept in its separate work/commit phase.
- [ ] Applicable build/lint/typecheck/tests executed or explicitly NOT RUN with reason.
- [ ] Database migration/backfill, regression and rollback reviewed when relevant.
- [ ] `checkpoint` run after incoming commits; `finish` succeeded without unclassified final paths. No unauthorized Git action, silent business approval, secrets commit or version bump.
- [ ] Handoff lists files changed, unresolved blockers, evidence and exact Git status.
