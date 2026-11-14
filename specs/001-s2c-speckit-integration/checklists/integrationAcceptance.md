# Acceptance Design — S2C Spec Kit integration (24 planned cases)

> This is a **feature-level test design catalogue** (not implementation or executed testing). Cases `SKI-TC-001-P/N..SKI-TC-012-P/N` map one-to-one to `SKI-FR-001..012`; they supplement, not replace, the master `TC-S2C-BRxxx` and A1/B1 validations. **4 scoped Web/Static GitHub positive cases PASS at source SHA `916ed6aa769e1fb9c25d9bd988277275613ae695`; 20 cases NOT_RUN.** See [executed provider evidence](../../../.agents/.documents/specKitWebModeEvidence095.md). These are not native CLI, Python/host security or A.1/B.1 acceptance results. A few related repository structures can be independently inspected statically; the audit report must name precisely what was inspected.

| Case ID | Feature requirement | Preconditions and input partition | Procedure / action | Expected result | Evidence to collect | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `SKI-TC-001-P` | SKI-FR-001 | In-repo `.specify/feature.json` with valid `specs/001-s2c-speckit-integration` | Parse file and resolve path relative to approved root | Exactly one contained selected feature, not inferred from Git branch | Git SHA, pointer JSON, resolved relative path | PASS_STATIC_GITHUB (SHA 916ed6a) |
| `SKI-TC-001-N` | SKI-FR-001 | Traversal, absolute, symlink/junction or invalid pointer | Attempt guarded S2C stage lookup in authorized disposable host | Refused with safe error; no outside-file IO | Denial, outside sentinel hash, OS | DESIGNED/NOT_RUN |
| `SKI-TC-002-P` | SKI-FR-002 | Master BRD/AGENTS and feature docs on pinned SHA | Inspect normative ownership and links | Feature refines global BR/REQ; no parallel master | Document ownership map, SHA | DESIGNED/NOT_RUN |
| `SKI-TC-002-N` | SKI-FR-002 | Feature claims to supersede host AGENTS or approved BRD | Attempt interpret contradictory authority | Conflict reported, no silent authority change | Conflicting exact excerpts and gate state | DESIGNED/NOT_RUN |
| `SKI-TC-003-P` | SKI-FR-003 | Valid feature directory | Inspect `spec.md`, `plan.md`, `tasks.md`, checklist | All present with stable IDs/provenance | Tree listing, file hashes, ID audit | PASS_STATIC_GITHUB (SHA 916ed6a) |
| `SKI-TC-003-N` | SKI-FR-003 | Missing or empty required artifact | Run authorized guarded static stage discovery | Required stage blocks or marks INCOMPLETE; no fake ready | Missing path, stage result | DESIGNED/NOT_RUN |
| `SKI-TC-004-P` | SKI-FR-004 | Authorized GitHub connection and permitted docs | Update a feature Markdown text and record new Git SHA | Only authorized path updated; no CLI execution claim | Commit SHA, change diff, audit | PASS_WEB_CONNECTOR_WRITE (SHA 916ed6a) |
| `SKI-TC-004-N` | SKI-FR-004 | Connector absent or write scope denied | Request doc write | Refuse or provide read-only handoff; no invented commit | Host permission result, no-write proof | DESIGNED/NOT_RUN |
| `SKI-TC-005-P` | SKI-FR-005 | Approved pinned CLI in authorized detached worktree | Run official `specify version` and `specify init`; inspect generated paths | Actual version/output, unchanged protected files or approved diff | CLI log, exit code, original/after SHA, asset list | DESIGNED/NOT_RUN |
| `SKI-TC-005-N` | SKI-FR-005 | Missing CLI, unsafe old tool, file collision or unauthorized `--force` | Attempt native init gate | STOP/BLOCKED without overwriting source branch | Before/after hashes, refusal log | DESIGNED/NOT_RUN |
| `SKI-TC-006-P` | SKI-FR-006 | Complete feature requirement/task/AC mapping | Traverse each of 12 IDs forward and backward | Each ID has exactly one explicit RTM mapping row and test IDs | RTM ID set comparison and orphan report | PASS_STATIC_GITHUB (SHA 916ed6a) |
| `SKI-TC-006-N` | SKI-FR-006 | Unknown or duplicated SKI-FR/task | Run trace audit | Duplicate or missing link disclosed and gate not passed | Failure/duplicate IDs | DESIGNED/NOT_RUN |
| `SKI-TC-007-P` | SKI-FR-007 | Real guarded checkout with active feature and scripts | Run read-only S2C bridge `status`, `plan`, `analyze` | Bounded paths/hashes/task IDs, no content body or writes | Output, file hashes and exit codes | DESIGNED/NOT_RUN |
| `SKI-TC-007-N` | SKI-FR-007 | Out-of-scope pointer or untrusted artifact with prompt injection | Request guarded bridge access | Reject unsafe pointer; no untrusted instruction execution or secret output | Denial, sentinel and redaction evidence | DESIGNED/NOT_RUN |
| `SKI-TC-008-P` | SKI-FR-008 | Existing root/host AGENTS and separate Constitution | Resolve authority before an approved file operation | Owner/host policy preserved; no auto-override | Policy refs, diff, owner | DESIGNED/NOT_RUN |
| `SKI-TC-008-N` | SKI-FR-008 | Upstream init would overwrite owned file or change host AGENTS | Simulate collision in disposable copy, inspect proposed files | STOP until owner authorizes specific migration; originals retained | Collision list, restore evidence | DESIGNED/NOT_RUN |
| `SKI-TC-009-P` | SKI-FR-009 | Active task, readable SHA and safe handoff path | Request STOP, record and verify persistence; RESUME after recheck | Original refs/unknown state preserved; new authorization checked | Signed path + source/policy fingerprints | DESIGNED/NOT_RUN |
| `SKI-TC-009-N` | SKI-FR-009 | Source/policy/feature pointer drift after STOP | Attempt RESUME without revalidation | STALE/BLOCKED, no silent COMPLETE | Old/current hashes, denial journal | DESIGNED/NOT_RUN |
| `SKI-TC-010-P` | SKI-FR-010 | Complete draft docs and independent review owner | Apply distinct A1, B, B1 checks on exact source | No B without accepted A1 + separate B permission; no release without B1 decision | Gate/signature/evidence chain | DESIGNED/NOT_RUN |
| `SKI-TC-010-N` | SKI-FR-010 | One-model synthetic vote or Spec Kit Analyze claims A1_PASS | Attempt promote implementation/release | Gate remains NOT_RUN/BLOCKED/NOT_AUTHORIZED | No-approval trace | DESIGNED/NOT_RUN |
| `SKI-TC-011-P` | SKI-FR-011 | Disposable host without `.specify/` | Run S2C bridge `status`, standalone docs path | Honest NOT_INITIALIZED and standalone allowed | Exit/output, no-write hashes | DESIGNED/NOT_RUN |
| `SKI-TC-011-N` | SKI-FR-011 | Spec Kit uninitialized while stage `implement` requested | Run guarded stage discovery | Explicit missing Spec Kit block, not fake READY | Error code/output | DESIGNED/NOT_RUN |
| `SKI-TC-012-P` | SKI-FR-012 | User selected one existing working branch | Use `feature.json` to switch/inspect feature, inventory Git branches | Feature selection independent; no new auto-branch | Tree, branch list, pointer SHA | DESIGNED/NOT_RUN |
| `SKI-TC-012-N` | SKI-FR-012 | Opt-in Git extension not authorized | Attempt enable branch-per-feature from automated stage | No automatic branch or extension installation | Branch list and refusal log | DESIGNED/NOT_RUN |

## Execution record schema (planned, not implemented)

For each actual run capture `caseId`, `SKI-FR`, exact Git SHA, approved feature pointer, Constitution/policy revision, platform/OS/Python, runner/method, fixture and outside sentinel if needed, action, expected, **observed**, result (PASS/FAIL/BLOCKED/NOT_RUN/N/A), stdout/stderr/exit code when present, evidence ref, reviewer/owner and timestamp. Do not fill observed results by assumption; static GitHub checks may be separately labelled `STATIC_INSPECTED` but are not native/host acceptance.

## Scope and dependencies

- Positive doc integrity checks may be performed now without changing `.source/`.
- Native CLI integration SKI-TC-005/007 and platform-specific negative cases require a real disposable host, correct installer and authority.
- A.1 and B.1 require actual independent approval; QA test authors cannot self-certify.
- Cross-reference [master RTM Section L](../../../.agents/.traceMatrix.md), [feature research](../research.md) and [native pilot](../../../.agents/.documents/specKitNativePilot.md).

## PLAN-095 — Actual Web/GitHub scoped case execution and remaining gates

[Reproducible source-bound evidence](../../../.agents/.documents/specKitWebModeEvidence095.md) reports **four** narrow positive cases at `916ed6aa769e1fb9c25d9bd988277275613ae695`:

- `SKI-TC-001-P` — JSON pointer parses and resolves to expected in-repository tracked feature paths (GitHub JSON+tree only).
- `SKI-TC-003-P` — required tracked artifacts present and 15 unique task IDs match current source config regex.
- `SKI-TC-004-P` — real authorized GitHub Contents edit of one `quickstart.md` file from `1709037a...` to `916ed6a...`; diff only that file, commit/branch/blob rereads match.
- `SKI-TC-006-P` — 12 distinct requirement rows map to 12 exact RTM rows and 24 expected unique P/N acceptance IDs, none missing.

**Totals:** 4/24 `PASS` in strictly scoped Web/Static GitHub operation; 20/24 `DESIGNED/NOT_RUN`. All host-negative cases, S2C Python guard tests, official native CLI/skills, independent A.1, explicit B, B.1 and release remain `NOT_RUN`/`NOT_AUTHORIZED`. `SK95-GATE-01..08` are **additional design-only** native approval checks, all `NOT_RUN`. Historical PASS is pinned to the tested SHA and not silently promoted after source/policy drift.


## PLAN-096 — Four additional bridge negative partitions (all NOT_RUN)

These four proposed cases are **additional to**, not substitutes for, the original 24 `SKI-TC-xxx-P/N` feature cases (4 narrow Web/static PASS, 20 NOT_RUN at the PLAN-095 source snapshot). They are based on [source-line audit SK96-01..04](../../../.agents/.documents/specKitBridgeSourceAudit096.md); **no real S2C bridge, guard dependency or native CLI test was executed**.

| ID | Feature requirement | Negative fixture | Expected decision / output | Status |
| --- | --- | --- | --- | --- |
| `SK96-NEG-01` | `SKI-FR-001` | Existing in-root non-`specs/` feature directory and env override | Owner-approved feature namespace policy enforced; reject if strict; preserve scope | NOT_RUN; POLICY_DECISION_PENDING |
| `SK96-NEG-02` | `SKI-FR-001`, `SKI-FR-008` | Duplicate `feature_directory` JSON keys | Ambiguous pointer rejected before last-key-wins selection | NOT_RUN |
| `SK96-NEG-03` | `SKI-FR-003`, `SKI-FR-007` | Zero-byte/whitespace mandatory artifacts | Structural/quality gate blocks or explicitly identifies incomplete artifact | NOT_RUN; SEMANTIC_RULE_PENDING |
| `SK96-NEG-04` | `SKI-FR-006`, `SKI-FR-007` | Duplicate `T001` across story labels | Duplicate reported, never silently counted as two unique tasks | NOT_RUN |

**Supporting smoke only:** Python stdlib demonstrates last JSON duplicate key wins, a zero-byte file is still `is_file()`, and regex matches duplicate task IDs. This did **not** invoke S2C's real bridge or establish a negative-test PASS. All original 4/24 Web/static PASS remain source-pinned; no native security acceptance, A.1, B or B.1 approval.


## PLAN-097 — Native upstream environment and pointer-persistence tests (all NOT_RUN)

Five additional cases from [v1.2.6/v1.4.0 upstream source review](../../../.agents/.documents/specKitUpstreamEnvAudit097.md); not part of the original 24-case feature denominator or four PLAN-096 bridge negatives:

| Case | Negative partition / operation | Expected controlled result | Status |
| --- | --- | --- | --- |
| `SK97-NEG-01` | Absolute out-of-repo `SPECIFY_FEATURE_DIRECTORY` into owned outside sentinel | S2C preflight denies before calling upstream; no outside write | DESIGN_NOT_RUN |
| `SK97-NEG-02` | Valid in-repo selected feature, no-persist=1, real read-only prerequisite call | Pointer bytes unchanged; exact observed output recorded | DESIGN_NOT_RUN |
| `SK97-NEG-03` | Different valid feature override without no-persist, ostensibly read-only call | Detect upstream pointer write risk; S2C read-only policy refuses unsafe invocation | DESIGN_NOT_RUN |
| `SK97-NEG-04` | Symlink/junction ancestor in feature override | Deny before native script; outside sentinel unchanged | DESIGN_NOT_RUN |
| `SK97-NEG-05` | Owner-authorized detached worktree running `setup_plan.py` | Exact generated artifacts/changed paths constrained to reviewed owned scope | DESIGN_NOT_RUN |

A local S2C guard or GitHub static path check cannot be substituted for actual upstream native-script execution. All five require authorized host and negative evidence; A.1/B/B.1 remain outstanding. Original feature cases remain 4 narrow Web/static PASS, 20 NOT_RUN; SK96-NEG cases remain 4 NOT_RUN.

## PLAN-108 / K07 — Spec Kit acceptance evidence audit

Review each previously recorded narrow Web PASS against its **exact historical SHA, fixture and observed output**; do not extrapolate to unexecuted native cases, different versions or a different source pair. Maintain distinct counts for scoped Web/static cases, native feature cases, bridge negative partitions `SK96-NEG-01..04` and upstream pointer/override negatives `SK97-NEG-01..05`.

Before any native case can pass, record actual OS, checkout root, command line, feature selection environment, hash of `.specify/feature.json`, whole target-tree inventory before/after, symlink/junction external sentinel and observed stderr/exit. Missing proof is `NOT_RUN`, not a waiver. Protected-file mutation or out-of-root access is P0 FAIL requiring security owner decision. No checkbox in this checklist is automatically approved by this document-only batch.
