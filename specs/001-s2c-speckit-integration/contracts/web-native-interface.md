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
