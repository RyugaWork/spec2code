# Spec2Code — User Technology/Version/Structure Override Record

> PLAN-086. Use **only for an explicit user instruction**, not to hide missing research or infer approval. This is a design/decision artifact; by itself it neither modifies source nor changes a runtime guard.

- Override ID: `OVR-<task-id>-<sequence>`
- Recorded UTC/date and instruction provenance:
- Requester exact intended instruction (safe short summary, not raw secrets):
- Permission scope: `S2C_SOURCE`, `HOST_REPOSITORY`, or `BOTH`:
- Exact repository / Git ref / affected paths and user-owned approval boundary:
- Requested technology/engine/edition, version or project structure:
- Whether it overrides **maturity**, **default architecture** or **version selection** (not security control):
- Baseline recommendation and reason (e.g. mature supported LTS):
- Current vendor support source/date, GA maturity and patch strategy:
- Ecosystem/dependency/SQL dialect/PowerShell edition/OS/CI compatibility:
- New-major, preview, EOL, migration/data loss or experimental structure risk:
- Alternatives shown, requester choice and required owner reviews:
- Risk IDs, severity and design mitigation, required tests and rollback:
- Exception expiration/revisit trigger, legacy upgrade plan if needed:
- Related requirements/AC/RTM and proposed design/task IDs:
- Outcome: REQUESTED / ASSESSING / ACCEPTED_FOR_DESIGN / OVERRIDE_REVIEW_REQUIRED / BLOCKED / IMPLEMENTED_VERIFIED (future evidence only):
- Independent security/host approval if required (or `NOT_OBTAINED`):
- A.1 outcome or `NOT_RUN`; future B.1 outcome or `NOT_RUN`:
- Persistence: `PERSISTED` with actual path or `NOT_PERSISTED`:
- Decision handoff, unresolved blockers and next authorized step:

## Override limits

An explicit user choice can waive **the default preference for widely used/mature versions** when within their scope, including freshly GA stable majors and nonstandard but justified layouts. It does **not** override higher-priority instructions, repo/host security controls, privacy, Path Guard, permissions, or requirement for actual testing and independent release approval. EOL/preview/high-risk exceptions require additional review and may remain BLOCKED. No implementation is authorized solely by this record.

## DOC-B04 — Required decision provenance for a user override

When a specific user override is requested, complete the existing form with: `OVR-ID`, the **verbatim preference and its source**, accepted owner authority/scope (S2C source, one named host, or both), target version/structure/dialect/driver, vendor lifecycle as-of date, the supported default alternative, compatibility and security impact, impacted requirement/feature/AC/risk IDs, build/test/rollback plan, decision `ACCEPT|REVISE|BLOCK`, exact source SHA, signature/evidence reference and expiry/re-review condition.

If the requester preference is known but host/security authority is absent, the proper state is `USER_PREFERENCE_RECORDED / APPROVAL_PENDING`; do not auto-select the latest preview, change CI/config, install a runtime, or treat preference as permission to release. If the requirement changes after an approved exception, invalidate the affected tests and restore the owner decision queue. This refines template completeness; it records no actual user override.
