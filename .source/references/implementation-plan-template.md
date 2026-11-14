# Implementation Plan — <Feature ID / name>

> Status: DRAFT / REVIEWED | Based on approved spec: <path/version> | Scope: <backend/web/integration>

## 1. Verified baseline
- Current repo branch, status, existing files and lockfiles:
- Applicable AGENTS/technical policies read:
- Existing code entrypoints, tests and project structure:
- Missing/placeholder-only components:

## 2. Design decisions
| Design ID | Requirement IDs | Proposed solution and impacted boundaries | Reason/trade-off | Status |
| --- | --- | --- | --- | --- |
| DES-01 | <R...> | | | PROPOSED |

## 3. Implementation map
| Layer | File/path (verified existing or NEW) | Change | Req / AC IDs |
| --- | --- | --- | --- |
| Backend API | | | |
| Business | | | |
| Repository/EF | | | |
| Web | | | |
| Tests | | | |

## 4. Contract and migration analysis
- API request/response and error shape (refer to canonical contract):
- Authn scheme, role/permission/resource ownership and CSRF:
- Database schema, index, migration/backfill, transaction, rollback:
- Data classification, encryption and secret custody:
- Async/concurrency limits, query plans, caching and invalidation:
- Compatibility with existing clients:

## 5. Delivery
- Dependency order and vertical slices:
- Test strategy (new test code separate phase):
- Local verification commands verified as available:
- Risks/mitigations:
- Rollout/rollback approach:
- Blockers/owner decisions:
- Design gate: PASS / BLOCKED

## PLAN-109 / M10 — Implementation plan exit contract

A proposal may be forwarded for coding only with exact approved requirement/AC, source SHA, architectural owner, official stable technology/version justification, physical sandbox/Path Guard policy, named allowed/denied paths, dependency DAG, one writer, budgets and measured success/negative criteria. List required tests by case ID, fixture and environment plus P0 treatment and rollback. Unavailable CLI/provider or missing host approval must be recorded as a blocker, not silently replaced with unrestricted shell.

Keep explicit status fields `DESIGN_READY|A1_PENDING|A1_PASS|B_AUTHORIZED|TESTED|B1_ACCEPTED`; the author must not advance beyond observed evidence. Distinct external signatures and stable source pairing are prerequisites. An implementation-plan template cannot itself change source, authorize build commands, install a model adapter or approve merge/release.
