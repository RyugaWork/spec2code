# Web–Native Integration Contract (DESIGN ONLY)

This contract connects two **different execution surfaces**, not two independent authority systems. The only existing executable adapter is S2C's [read-only bridge](../../../.source/scripts/speckit_bridge.py); no new API/JSON contract was deployed.

## Operation boundary and capability declaration

| Operation | GitHub/ChatGPT Web | Native Spec Kit + Codex/Codespaces | Mandatory gate |
| --- | --- | --- | --- |
| Identify active feature | Read `.specify/feature.json` through authorized GitHub connector and pin current Git SHA | Read same checked-out file; upstream environment override considered only under current host scope | Root/host AGENTS, no traversal or unowned files |
| Inspect feature requirements and tasks | Read feature Markdown and current BRD/RTM/risk | Use official file/scripts plus S2C bridge for bounded metadata | Exact source revision; provenance preserved |
| Write `spec.md`, `plan.md`, `tasks.md` | Explicit authorized GitHub file update; audit commit SHA | Upstream-generated commands only after actual tool install, host permissions and collision check | Doc scope, source freshness and owner requirements |
| Run native Spec Kit stage | **UNAVAILABLE by default**; only conceptual Markdown review | Supported agent skill runs when installed and invoked; capture execution log | Agent/CLI presence and exact host capability |
| Run static bridge | Cannot claim execution from a GitHub read | S2C `speckit_bridge.py` CLI on guarded local checkout | Local Path Guard and policy; static READY is not permission |
| Edit product source / host repo | No automatic authorization from a document | Requires independent A.1 and separately authorized B task | Scope/policy/secret/Path Guard checks; tests |
| Sign A.1/B.1 or release | Cannot self-certify from one-model review | Cannot self-certify from CLI or synthesis | Actual independent responsible reviewers |

## Logical status exchange (do not implement without B permission)

### Request record

`taskId`, exact `gitSHA`, active `feature_directory`, document and Constitution revisions, allowed read/write scope, requested stage, host capability label `WEB_MARKDOWN` or `NATIVE_CLI_VERIFIED`, permissions and policy refs.

### Result record

`taskId`, original and resulting Git SHA, changed-path list, actual mode, executed command if any, exit status, affected feature/task IDs, evidence refs and explicit persistence status. Each status is one of `DOC_UPDATED`, `STATIC_CHECKED`, `NATIVE_EXECUTED`, `BLOCKED`, `NOT_RUN` or `STALE`; **do not infer approvals from status**. The names are illustrative proposal fields, not live implemented JSON.

### STOP and RESUME

STOP stores last valid source/policy fingerprint, in-flight unknown operations, partial artifacts and next safe step; RESUME requires current authorization and fresh source/policy/feature checks. Do not use S2C Workflow Guard `close` as a substitute. Store no secret body or untrusted instructions in the handoff.

## Version and generated-file compatibility

Only official source/installer may create upstream templates, scripts and coding agent skill packages. In native pilot an exact asset inventory and hash comparison must detect collisions under `.specify/` and `.agents/skills/`; old reviews become stale after changes to relevant source/policy. Read-only `speckit_bridge.py` reports the metadata of `spec.md`/`plan.md`/`tasks.md`, not their semantic approval.

## Compliance cases

See [SKI-TC catalogue](../checklists/integrationAcceptance.md), especially cases 001-N, 005-N, 007-N, 008-N, 009-N, 010-N and 012-N; every actual native test is currently NOT_RUN.

## PLAN-095 — Native mutation caveat

The [native S2C execution safety gate](../../../.agents/.workflow/specKitNativeExecutionGate.md) distinguishes document operations, official CLI installation, source-code implementation, host QA and owner approvals. The current T001..T015 register is mixed; it must not be submitted wholesale to `$speckit-implement`. A continuation answer of “yes” to the upstream incomplete-checklist prompt never grants A.1, B permission, host Path Guard or B.1.

The gate exists **as Markdown guidance only**, not as a deployed runtime hook. Fail closed when a selected coding agent cannot apply host/S2C policies at the point of write, when a source/revision drifts or when `converge` proposes a task outside explicit authorization.


## PLAN-097 — Native environment contract (not implemented)

When transferring from a GitHub Web-selected feature to a real Spec Kit CLI process, **do not pass raw user or inherited environment values** for `SPECIFY_FEATURE_DIRECTORY` or `SPECIFY_FEATURE`. Upstream `get_feature_paths` (v1.2.6 and v1.4.0) resolves absolute feature directories and may persist the feature pointer; it does not call S2C's Path Guard. Native read-only preflight requires real root/feature containment verification, clean environment, `SPECIFY_FEATURE_NO_PERSIST=1`, pointer hash and no-write inventory. Native write commands such as `setup_plan.py` require an explicit scoped executor and approved disposable worktree.

The no-persist setting protects only feature-pointer persistence; the **OS filesystem boundary and authority gate** remain separate. See [source audit](../../../.agents/.documents/specKitUpstreamEnvAudit097.md) and `SK97-NEG-01..05`. All are DESIGN_NOT_RUN.

## PLAN-108 / K06 — Web/native adapter failure contract

Proposed adapter responses distinguish `READY_READ_ONLY`, `UNAVAILABLE`, `STALE_SOURCE`, `SCOPE_DENIED`, `APPROVAL_REQUIRED`, `PARTIAL_OUTPUT` and `HOST_ERROR`. Every response carries a request ID, source SHA, selected feature tuple, actual side effects list, authorization provenance and evidence location. A tool-provided `approved=true` cannot substitute for trusted host approval. Do not assume remote GitHub validation is native OS execution evidence.

Repeat requests must be idempotent for reads and compare-and-set for writes. On timeout after a possible write, first discover the **actual** source/side-effect state instead of blindly retrying; exhausted retry budget stops. Unknown wire fields that may expand authority are rejected. Host-side mutation must be denied unless tool version, sandbox, command allowlist and feature scope are actually verified and accepted.
