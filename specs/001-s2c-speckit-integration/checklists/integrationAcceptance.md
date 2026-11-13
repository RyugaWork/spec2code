# Acceptance Design — S2C Spec Kit integration (24 planned cases)

> This is a **feature-level test design catalogue** (not implementation or executed testing). Cases `SKI-TC-001-P/N..SKI-TC-012-P/N` map one-to-one to `SKI-FR-001..012`; they supplement, not replace, the master `TC-S2C-BRxxx` and A1/B1 validations. **All 24 execution outcomes are NOT_RUN.** A few related repository structures can be independently inspected statically; the audit report must name precisely what was inspected.

| Case ID | Feature requirement | Preconditions and input partition | Procedure / action | Expected result | Evidence to collect | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `SKI-TC-001-P` | SKI-FR-001 | In-repo `.specify/feature.json` with valid `specs/001-s2c-speckit-integration` | Parse file and resolve path relative to approved root | Exactly one contained selected feature, not inferred from Git branch | Git SHA, pointer JSON, resolved relative path | DESIGNED/NOT_RUN |
| `SKI-TC-001-N` | SKI-FR-001 | Traversal, absolute, symlink/junction or invalid pointer | Attempt guarded S2C stage lookup in authorized disposable host | Refused with safe error; no outside-file IO | Denial, outside sentinel hash, OS | DESIGNED/NOT_RUN |
| `SKI-TC-002-P` | SKI-FR-002 | Master BRD/AGENTS and feature docs on pinned SHA | Inspect normative ownership and links | Feature refines global BR/REQ; no parallel master | Document ownership map, SHA | DESIGNED/NOT_RUN |
| `SKI-TC-002-N` | SKI-FR-002 | Feature claims to supersede host AGENTS or approved BRD | Attempt interpret contradictory authority | Conflict reported, no silent authority change | Conflicting exact excerpts and gate state | DESIGNED/NOT_RUN |
| `SKI-TC-003-P` | SKI-FR-003 | Valid feature directory | Inspect `spec.md`, `plan.md`, `tasks.md`, checklist | All present with stable IDs/provenance | Tree listing, file hashes, ID audit | DESIGNED/NOT_RUN |
| `SKI-TC-003-N` | SKI-FR-003 | Missing or empty required artifact | Run authorized guarded static stage discovery | Required stage blocks or marks INCOMPLETE; no fake ready | Missing path, stage result | DESIGNED/NOT_RUN |
| `SKI-TC-004-P` | SKI-FR-004 | Authorized GitHub connection and permitted docs | Update a feature Markdown text and record new Git SHA | Only authorized path updated; no CLI execution claim | Commit SHA, change diff, audit | DESIGNED/NOT_RUN |
| `SKI-TC-004-N` | SKI-FR-004 | Connector absent or write scope denied | Request doc write | Refuse or provide read-only handoff; no invented commit | Host permission result, no-write proof | DESIGNED/NOT_RUN |
| `SKI-TC-005-P` | SKI-FR-005 | Approved pinned CLI in authorized detached worktree | Run official `specify version` and `specify init`; inspect generated paths | Actual version/output, unchanged protected files or approved diff | CLI log, exit code, original/after SHA, asset list | DESIGNED/NOT_RUN |
| `SKI-TC-005-N` | SKI-FR-005 | Missing CLI, unsafe old tool, file collision or unauthorized `--force` | Attempt native init gate | STOP/BLOCKED without overwriting source branch | Before/after hashes, refusal log | DESIGNED/NOT_RUN |
| `SKI-TC-006-P` | SKI-FR-006 | Complete feature requirement/task/AC mapping | Traverse each of 12 IDs forward and backward | Each ID has exactly one explicit RTM mapping row and test IDs | RTM ID set comparison and orphan report | DESIGNED/NOT_RUN |
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
