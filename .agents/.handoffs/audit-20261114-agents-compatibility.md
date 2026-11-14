# S2C — AGENTS compatibility and cleanup audit (2026-11-14)

**Classification:** AUTHOR_STATIC_REVIEW; input SHA df9bc4378c559de842788261adb86d90dbf6e999; branch docs/plan-089-a1-readiness. A distinct audit record, not BRD/RTM authority, formal A.1 review, runtime test result or Phase-B permission. Re-pin the actual output Git SHA from commit receipt after write.

## Evidence and scope

Examined root AGENTS, agentRoles, runbook, workflow index/specification, validation specification/report template, the .source portable skill, five-phase workflow JSON, Spec Kit constitution/pointer/tasks, relevant BRD/RTM/plans/risks and repo tree of 174 entries. Static Markdown file-target checks on inspected primary documents reported no missing file paths. This does not verify all anchor fragments or execute native Codex, Windows hostile path, full regression or independent A.1. PLAN-111 P0 source changes belong to the parallel workstream.

## Pre-update compatibility / risk / remediation matrix

| ID | Source gap | Impact | Expected fix | Failed result and owner |
| --- | --- | --- | --- | --- |
| AC-01 | AGENTS current and historical PLAN directives mixed | P1: ambiguous priority | Active source-bound entrypoint; archive prior G1 matrix | Drift => BLOCKED_REVIEW / GPTWEB |
| AC-02 | Roles/runbook lack synchronized executor routing | P1: wrong execution | GPTWEB/CODEX/AUTO task envelope and dispatch boundary | No provider => HANDOFF_REQUIRED / CODEX |
| AC-03 | Runbook env-versus-pointer selection lacks explicit sanitization | P0: feature escape | Require validated physical checkout and explicit override | Invalid scope => BLOCKED / CODEX |
| AC-04 | Workflow index steps may be mistaken as current B permission | P1: early code | Clearly mark implementation-only path | No B owner approval => NOT_AUTHORIZED |
| AC-05 | PR #7 historical findings read like exact-head defect status | P1: false claim | Label historical, PLAN-111 candidate not validated | Missing current tests => NOT_RUN |
| AC-06 | Phase ledger task counts not linked into runbook | P1: status drift | Unique ID counts including reopened/new and executor splits | Missing source => UNKNOWN |
| AC-07 | 99.99% numeric rule absent from A.1 report | P0: false acceptance | Add strict measurable group results + A1 independent veto | Zero tests/P0/unsigned => NO_GO |
| AC-08 | Parallel writer collision | P0: overwrite | Single writer/file, compare source SHA, fast-forward lease | Changed HEAD => BLOCKED_CONFLICT |

**Expected output:** one reviewable same-branch documentation commit changing AGENTS.md, roles, runbook, workflow README, validation specification, report template and this record; no .source/.specify/specs/.github/runtime config changes. **Rollback:** revert only that scoped commit after reviewing any parallel changes; no force-push. No independent reviewer or runtime test was executed.

## Historical GOV-20261114 G1 matrix (archived from root AGENTS)

**This update's author-side pre-edit review matrix** (all runtime/independent checks remain NOT_RUN):

| ID | Gap / baseline observation | Risk | Planned treatment / acceptance |
| --- | --- | --- | --- |
| RM-GOV-01 | Existing review roles lack a universal pre-edit matrix requirement | P1 | Require matrix and diff comparison; documentation check only |
| RM-GOV-02 | Codex support described but task executor tags inconsistent | P1 | Define GPTWEB/CODEX/AUTO tags and complete task envelope |
| RM-GOV-03 | Codex host/provider dispatch not evidenced working | P1 | Capability-gated dispatch; HANDOFF_REQUIRED on missing capability |
| RM-GOV-04 | A.1 fail-to-A path exists but quantitative cycle gate is unspecified | P0 | A rework, bounded rerun and independent A.1 validation |
| RM-GOV-05 | No strict per-group >99.99% test metric with P0 veto | P0 | Define denominator, no rounding, evidence and NO_GO |
| RM-GOV-06 | Task remaining counts not mandatory after every phase | P1 | Report checkpoint with unique-ID remaining and executor split |
| RM-GOV-07 | Parallel writer/source drift may overwrite another chat | P1 | Single file owner, ref/blob lease, stop on drift |
| RM-GOV-08 | Existing independent review and B authorization must stay intact | P0 | Preserve A1-VAL-01..09 and distinct owner signoff |

## Audited task ledger at pre-write time

| Task | Executor | State |
| --- | --- | --- |
| AA-01 Repo/agent inventory and source pin | GPTWEB | DONE_VERIFIED |
| AA-02 Primary Markdown file path check | GPTWEB | DONE_VERIFIED (selected documents) |
| AA-03 Pre-edit compatibility/risk matrix | GPTWEB | DONE_VERIFIED (author review) |
| AA-04 Root AGENTS cleanup | GPTWEB | PLANNED |
| AA-05 Roles/runbook/index sync | GPTWEB | PLANNED |
| AA-06 A.1/report schema alignment | GPTWEB | PLANNED |
| AA-07 Post-commit diff/branch evidence | GPTWEB | PLANNED |
| AA-08 Native Codex/Windows runtime verification | CODEX | HANDOFF_REQUIRED / NOT_RUN |
| AA-09 Independent A.1/owner decision | Independent reviewer | BLOCKED / NOT_RUN |

Total unique tasks: 9. Verified before modification: 3. Pending at the pre-write checkpoint: 6. Recalculate after confirmed Git output; do not convert plans to PASS.
