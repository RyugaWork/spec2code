# PLAN-108 — Batch 3 of 5: ten Spec Kit contract tasks

**Input SHA:** `967a6539fd799a06925a39173e85457e4df247f3` on `docs/plan-089-a1-readiness`; **output SHA:** commit containing this handoff, requiring GitHub readback. **Mode:** documentation-only via GitHub connector.

| Task | Existing artifact | Contract reviewed | Status |
| --- | --- | --- | --- |
| K01 | `specs/001-s2c-speckit-integration/spec.md` | Explicit Web/native acceptance boundary | DESIGN_REVIEWED / NATIVE_NOT_RUN |
| K02 | `specs/001-s2c-speckit-integration/plan.md` | Stage dependency and rollback matrix | DESIGN_REVIEWED / NATIVE_NOT_RUN |
| K03 | `specs/001-s2c-speckit-integration/tasks.md` | Human-owned task status preservation | DESIGN_REVIEWED / NATIVE_NOT_RUN |
| K04 | `specs/001-s2c-speckit-integration/research.md` | Upstream provenance and version selection | DESIGN_REVIEWED / NATIVE_NOT_RUN |
| K05 | `specs/001-s2c-speckit-integration/data-model.md` | Immutable feature source tuple | DESIGN_REVIEWED / NATIVE_NOT_RUN |
| K06 | `specs/001-s2c-speckit-integration/contracts/web-native-interface.md` | Typed transport failure and idempotency | DESIGN_REVIEWED / NATIVE_NOT_RUN |
| K07 | `specs/001-s2c-speckit-integration/checklists/integrationAcceptance.md` | Positive and negative evidence separation | DESIGN_REVIEWED / NATIVE_NOT_RUN |
| K08 | `specs/001-s2c-speckit-integration/checklists/requirements.md` | Requirements quality negative review | DESIGN_REVIEWED / NATIVE_NOT_RUN |
| K09 | `.specify/README.md` | Upstream source ownership and installation boundary | DESIGN_REVIEWED / NATIVE_NOT_RUN |
| K10 | `.agents/.workflow/specKitWebWorkflow.md` | Source-pointer verification protocol | DESIGN_REVIEWED / NATIVE_NOT_RUN |

### Scope/acceptance evidence

Ten proposed improvements were written to the existing authoritative feature spec, plan, task register, research, data model, adapter interface, two checklists, the `.specify/` README and Web workflow. Historical feature/task IDs, native checklist states and source evidence are preserved. No task is checked merely because new acceptance text exists.

Required checks: branch SHA and non-force parent, ten section headings and exactly ten handoff rows, Markdown-only diff, relative links to tracked files, unchanged user-owned T011/T012/T015, no new feature branches or code/config/CI, and negative-case statuses remaining NOT_RUN. The previously recorded Web/static PASS cases apply only to their original exact source and cannot authorize native commands.

**Blocked external work:** official Spec Kit CLI not verified installed/running in this connector; Path Guard OS negative tests, owner P0 acceptance, A.1, B and B.1 are pending. Continue to PLAN-109 portable skill/provider and review contracts only after verifying output SHA.
