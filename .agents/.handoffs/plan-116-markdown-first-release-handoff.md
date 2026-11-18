# PLAN-116 — Markdown-first release planning handoff

Date: 2026-11-18 Asia/Ho_Chi_Minh. Input Git SHA `d743b34092e28a18cdc5b270ed0e282519bd2175`; existing branch `docs/plan-089-a1-readiness`; PR #10 draft. Output is the single commit containing this handoff; require exact readback and non-force ref lease. User authorized detailed plan written to Git, then committed; not profile implementation, runtime test, migration, release or Google mirror edit.

## Pre-edit impact and rollback matrix

| Gap | Owner files | Executor | Expected safe result | Failure / rollback |
| --- | --- | --- | --- | --- |
| v0.x prototype vs first v1.0 product | AGENTS, README, master spec, git workflow | GPTWEB + owner | One product scope, repo baseline retained | Stop on drift; reviewed revert |
| Release and migration architecture | detailed plan, INSTALL, checklist | GPTWEB + host owner | Separate distribution/state/host ownership, compatibility/rollback | Stop on missing owner or conflicting paths; restore only reviewed files |
| Overlapping plans | canonical ledger, feature register, RTM | GPTWEB + QA | 30 unique WEB tasks, explicit dependencies and aliases, 64 F IDs preserved | No status promotion; revert docs only |
| Risk and evidence | risk matrix, testing catalogue | GPTWEB + independent reviewers | 15 distinct designed cases NOT_RUN, profile gates not waiver | Block unknown P0/evidence; no real tool tests claimed |

The plan includes v1.0..1.7 targeted roadmap, schema/version contract, manual GPT Web startup, 30 work packages with roles/priorities/dependencies/AC/evidence and 15 planned cases; all 30 planned and 15 NOT_RUN. Scope-specific A.1 and separate B before WEB-006 product implementation; independent B.1 and approval before release. Actual scope/ownership/AC, independent reviewers and Git/Google source reconciliation pending. Existing global T112-05..09 remain open, RM-001 P0/20 OPEN/UNKNOWN residual, global A1_NOT_RUN, B_NOT_AUTHORIZED, B1_NOT_RUN unchanged. Runtime code/test/config/CI, actual host, existing historical records and upstream Spec Kit artifacts untouched.

Next: readback exact Git SHA and changed paths; WEB-001..003 remote preflight, WEB-004/005 actual scope and independent decisions. No fresh local checkout, VM, provider, CLI, test or Google verification in this checkpoint; no false independence. Retain current working branch and use one cohesive non-force commit, no merge/tag. Rollback via approved revert of that commit only, preserving existing history.

[Design](../.documents/markdownFirstReleasePlan.md) · [Canonical task ledger](../.plans.md#plan-116--web-v100-delivery-task-ledger) · [Tests](../.workflow/testingAndDelivery.md#plan-116--web-profile-acceptance-design).
