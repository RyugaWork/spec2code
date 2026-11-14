# PLAN-094 — Spec Kit feature completion and exact draft crosswalk handoff

> Recorded **2026-11-13 (Asia/Ho_Chi_Minh)**. Repo `RyugaWork/spec2code`; **existing** branch `docs/plan-089-a1-readiness`, Draft PR #10, no new branch or merge. **Git source inspected before creating this handoff:** `05e85d4d7c865e421224e3ff334642202123b575`. Saving this record advances HEAD: refresh exact SHA before external reviewer signoff.
>
> **Google BRD mirror**: `https://docs.google.com/document/d/1M3_2tNUxOXci83pcpPCzBkxwvRvixeT7FYeGyIsFOa4/edit?tab=t.0`; Draft v1.5, sections PLAN-092/093/094; revision `AHj4eMRu50FIWgL_K17Wef7cveq_qCIe8Kq-pV-robhc37C8Gu9H5AxWK3QuEPL1cD7P6iFgRJQH2lSraIPO5DPP15fTuHPOmCZwAwFV5g`. Google stakeholder text is a summary, **not byte-identical to master `.agents/.spec.md` and not an owner signature**.
>
> **Disposition:** `DOC_RECONCILED_DRAFT / WEB_MARKDOWN_PREPARED / NATIVE_NOT_RUN / A1_NOT_RUN / B_NOT_AUTHORIZED / B1_NOT_RUN`. No product runtime/host/CI/source-code change was authorized or implemented.

## 1. Work actually completed on the existing branch

- Created native-compatible official Spec Kit feature support documents under `specs/001-s2c-speckit-integration/`: `research.md`, `data-model.md`, `quickstart.md`, `contracts/web-native-interface.md` and `checklists/integrationAcceptance.md`.
- Aligned [feature specification](../../specs/001-s2c-speckit-integration/spec.md) section **ordering** and names with upstream official Spec Kit templates: User Scenarios & Testing, Requirements (Functional Requirements + Key Entities), Success Criteria, Assumptions. [Feature plan](../../specs/001-s2c-speckit-integration/plan.md) includes Summary, Technical Context, Constitution Check, Project Structure, Complexity Tracking plus existing decisions and risk gates.
- Replaced [RTM Section L](../.traceMatrix.md) shorthand grouped identifiers with **12 explicit SKI-FR-001..012 records**, one row each, with exact global BR/S2C-REQ/NFR, task and two `SKI-TC-xxx-P/N` case refs. No new owner-approved global BR/SRS was created.
- Defined [24 individual acceptance cases](../../specs/001-s2c-speckit-integration/checklists/integrationAcceptance.md): positive and negative preconditions, action, expected result and evidence. **24/24 execution results remain NOT_RUN**; an authored case is not a test execution.
- Updated [root AGENTS](../../AGENTS.md), [master SRS Section 20](../.spec.md), [governance ownership](../.documents/.documentGovernance.md), [plans](../.plans.md), [risk matrix](../.riskMatrix.md), [feature status](../.features.md), [integration guide](../../.source/integrations/speckit/README.md), [Spec Kit README](../../.specify/README.md) and root README with links/status without altering runtime.
- Updated Google stakeholder BRD Draft v1.5 Section 27 for PLAN-094, explicitly disclosing pending native installation, owner approval and security acceptance.

## 2. Executed static source observations (not Python or CLI tests)

| Audit operation | Exact source and result | Scope limitation |
| --- | --- | --- |
| Parse selected feature pointer | Git SHA `fce2a8e4c425f9e21b15592e3f5f9e653703c3d9`: `.specify/feature.json` selects `specs/001-s2c-speckit-integration` | JSON/tree only, not local hostile path test |
| SKI-FR/RTM/case reverse mapping | Same SHA: 12 unique feature FR rows, 12 exact RTM mappings, 24 unique positive/negative case rows, zero missing or duplicate expected IDs, all global BR/REQ/NFR refs present | Static text and ID parsing, not requirement quality signoff |
| Task catalogue | Same SHA: 15 unique task IDs; on subsequent Git HEAD `70d38b244585a8c21fd76154f5c5e61d81c91074`, **T001–T005 and T010** recorded documentary completion; T006–T009 and T011–T015 unchecked | No native task tests or B authorization |
| Upstream section completeness | Exact source on `70d38b244585a8c21fd76154f5c5e61d81c91074`: 4 required feature spec section groups and 4 feature plan section groups present | Template-name presence only; upstream CLI Analyze NOT_RUN |
| Internal Markdown link resolution | `70d38b244585a8c21fd76154f5c5e61d81c91074`: **190 relative links across 18 selected feature/governance files (55 feature + 135 governance), zero missing.** Latest master/governance/root README follow-up at `05e85d4d7c865e421224e3ff334642202123b575`: **99 links across 4 edited files, zero missing** | Link existence in Git tree, not rendering/per-file/anchor-level validation |
| Google mirror | Revision `AHj4eMRu50FIWgL_K17Wef7cveq_qCIe8Kq-pV-robhc37C8Gu9H5AxWK3QuEPL1cD7P6iFgRJQH2lSraIPO5DPP15fTuHPOmCZwAwFV5g`: sections 25, 26, 27 and Draft v1.5 header present | Business review/approval still UNKNOWN |
| Branch discipline | Eight original branch names observed; feature selection uses `.specify/feature.json`; continued same Draft PR #10 | No merge/release authorized |

These are **actual connector-based static checks** on named source snapshots, not local S2C Python execution, host security, Spec Kit CLI native workflow, CI or human review. The prior [PLAN-093 blocked native pilot](plan-093-sk03-native-pilot-handoff.md) remains accurate: the terminal cannot resolve github.com and has no `specify` tool; an offline install attempt failed. A synthetic *Git worktree mechanics* check is separate from native acceptance.

## 3. Traceability and specific task completion

**T010:** marked `[x]` only for documentary Git↔Google draft crosswalk, source/Constitution/RTM/risk/feature revision and 12/24 ID consistency. This **does not ratify** the BRD/Constitution, establish a named reviewer, count native CLI as installed, pass A.1, authorize B or accept any risk. Drift after source commits requires source-bound revalidation and owner review.

**Completed as documentation work:** T001–T005, T010 (6/15). **Pending:** T006 version/host choice; T007 real disposable `specify init`; T008 actual native agent skills/scripts and prerequisite outputs; T009 generated collision reconciliation; T011 independent design validation; T012 explicit B authorization; T013 runtime changes if approved; T014 OS/host/negative regression; T015 independent B.1 and release decision.

## 4. Pending owner decisions, risk and next permissible action

- `DEC-SK3-01/02`: choose owner-accepted stable upstream release, consider v1.4.0 security hardening versus v1.2.6 disposable candidate, and identify a real network-enabled Codex/Codespaces/Windows executor.
- `DEC-SK3-03/04`: permit optional `--force` **only** inside an authorized disposable detached checkout with prior hashes and collision/rollback plan; select which upstream-generated templates/scripts/skills can be imported.
- `DEC-091-01/09/10` and `DEC-SK3-05`: actual stakeholder/host/security authority, independent A.1 validation on exact current SHA, explicit B permission, later actual B.1/release. The project Constitution remains DRAFT/NOT_RATIFIED.
- RM-001..005 host scope/authority/TOCTOU P0 risk and native installation risks **remain OPEN** with verified residual UNKNOWN. No risk score was reduced from static artifacts.

**Next safe activity:** conduct genuine independent A.1 on the complete feature plan and current master SRS/RTM/Constitution **without fabricated votes**, then (in parallel for development testing only if authorized) execute [native pilot runbook](../.documents/specKitNativePilot.md) in an isolated network-enabled host. Preserve stdout/stderr, exit code, generated file list, original hashes, OS and exact SHA. Do not run `specify init --force` on the active S2C checkout, auto-create feature branches or merge PR #10.

## 5. STOP, resumption and rollback

No local S2C Workflow Guard session was started/closed here; this GitHub file is the actual durable handoff. When resumed, refresh branch HEAD, Google revision, pointer, policy and task evidence. If the feature, source or owner decisions have changed, mark affected mappings STALE and repeat checks. Roll back the PLAN-094 Markdown commits only through explicit reviewed Git history, preserving historic PLAN-090/091/092/093 evidence; Google Doc rollback requires separate document revision control. Never delete unowned host or upstream-generated files.
