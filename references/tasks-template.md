# Implementation Tasks — <Feature ID>

> Scope approved for: PLAN ONLY / IMPLEMENT / TEST / COMMIT / PUSH (explicit, independently authorized)

| Task ID | Stage | Requirement / AC IDs | File boundaries | Dependencies | Done when (observable) | Verification | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T-001 | Review existing contracts | R01 / AC01 | <read-only files> | None | Conflicts recorded | Source check | TODO |
| T-002 | Backend change | R01 / AC01 | .source/backend/... | T-001 | Approved behavior present | Build/static check | TODO |
| T-003 | Frontend integration | R01 / AC01 | .source/web/... | T-002 | UI behavior matches AC | Existing checks | TODO |
| T-004 | New automated tests (separate phase) | R01 / AC01 | tests/... | T-002/T-003 | Tests assert AC | Actual execution | TODO |
| T-005 | Evidence and handoff | All | <approved doc path> | T-002..T-004 | Traceability and limitations reported | Review | TODO |

Allowed task statuses: TODO, IN_PROGRESS, BLOCKED, DONE. Do not mark DONE solely because a file exists. New test source and feature source must not be included in the same commit. Git writes require explicit owner approval.
