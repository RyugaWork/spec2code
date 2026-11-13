# Feature Specification: Spec Kit as S2C's Development Workflow

**Feature ID:** `001-s2c-speckit-integration`  
**Status:** DRAFT_FOR_REVIEW / NOT_APPROVED  
**Origin:** Explicit request to integrate official GitHub Spec Kit into the S2C project for its own coding workflow, usable from ChatGPT Web and native coding agents.  
**Requirement authority:** [S2C BRD/SRS](../../.agents/.spec.md) BR-003/004/005/010/012/014/015 and [RTM](../../.agents/.traceMatrix.md) S2C-REQ-007/012/022/032/037 plus applicable NFRs.  
**Implementation gate:** A.1 NOT_RUN; B NOT_AUTHORIZED.

## Problem and goals

S2C currently has a read-only `.source/scripts/speckit_bridge.py` and JSON stage prerequisites, but its development repository does not yet provide active native Spec Kit feature artifacts. ChatGPT Web must be able to maintain Markdown artifacts through an authorized GitHub connection, while native Codex/Copilot/Codespaces can later run upstream official Spec Kit skills/scripts. Both modes must share **one** feature pointer and artifact set without duplicating BRD/SRS authority or claiming unperformed execution.

## User stories and independently observable acceptance

### US-01 — Browser-based specification authoring (Priority P1)
As a S2C maintainer using ChatGPT Web, I can identify the selected feature, inspect the root constitution and write/review its `spec.md`, `plan.md` and `tasks.md` through GitHub. I can resume in another authorized agent host from the same Git revision.

**Acceptance:** S2C's selected feature pointer resolves within this repository; feature artifact links exist; source SHA and non-executed status are recorded. Without a connector or approved write scope, return a read-only/manual handoff rather than claiming the CLI ran.

### US-02 — Optional official native Spec Kit workflow (Priority P1)
As a developer in Codex/Codespaces, I can install a reviewed official Spec Kit release, initialize/select this existing repository, and use upstream official Constitution, Specify, Clarify, Plan, Checklist, Tasks, Analyze, Implement and Converge steps where supported.

**Acceptance:** Installation is explicitly requested and reviewed for collisions; the CLI version and generated file inventory are captured; upstream scripts/agent skills actually exist before native commands are described as available. This feature's Markdown alone does not satisfy native-install acceptance.

### US-03 — S2C safe read-only bridge (Priority P1)
As a reviewer/agent, I can query the S2C bridge for active feature paths, artifact presence/hashes, bounded task identifiers and missing prerequisite reasons **without returning specification body or modifying files**.

**Acceptance:** The bridge resolves `.specify/feature.json` and returns a bounded artifact inventory for selected stages; traversal, external pointer, symlink/junction and missing mandatory artifact are rejected; `READY` means static preflight only, not approved implementation.

### US-04 — Governance, trace and recovery (Priority P1)
As a project owner, I can trace active Spec Kit feature requirements to S2C BR/REQ/AC, tasks, planned tests and risk; STOP/handoff and source drift cannot silently grant permission to implement.

**Acceptance:** RTM records feature/requirement/task/test mapping or explicit unmapped gap. Missing A.1, changed constitution/policy/source, unsafe host pointer, and unapproved agent code actions block the affected implementation; historical evidence remains intact.

## Functional requirements

| ID | Draft requirement and testable acceptance |
| --- | --- |
| SKI-FR-001 | Provide a feature pointer under `.specify/feature.json` selecting exactly a contained `specs/<feature-id>/` directory, never infer selection from branch name |
| SKI-FR-002 | Preserve one root S2C BRD/SRS and AGENTS; avoid copying or rewriting master requirements into native feature files |
| SKI-FR-003 | Provide feature-local `spec.md`, `plan.md`, `tasks.md` and explicit ownership/provenance |
| SKI-FR-004 | Allow read/write of feature Markdown through authorized GitHub connectors without pretending Spec Kit CLI/skills ran in ChatGPT Web |
| SKI-FR-005 | Support official native CLI/agent skill installation **only with** pinned version, collision review, owner consent and actual execution evidence |
| SKI-FR-006 | Map active Spec Kit feature and task IDs to S2C BR/REQ/AC/RTM and design risks, or flag missing mapping |
| SKI-FR-007 | Reuse existing `speckit_bridge.py` as read-only static inventory and stage preflight; never grant implementation permission |
| SKI-FR-008 | Preserve upstream `.specify/` and `specs/` ownership and root/host AGENTS; fail closed when sources conflict |
| SKI-FR-009 | On STOP or drift record last valid source snapshot, feature pointer, changed paths, incomplete tasks and actual persistence without auto-CLOSE |
| SKI-FR-010 | Keep A.1 and B.1 independent from Spec Kit Analyze and Converge, and keep test execution distinct from planned test cases |
| SKI-FR-011 | Permit Spec Kit absence for a standalone host S2C run; adapter status must report NOT_INITIALIZED/NO_ACTIVE_FEATURE honestly |
| SKI-FR-012 | Do not create an extra Git branch per Spec Kit feature by default; use explicitly selected feature directory, keep branch-management optional |

## Nonfunctional constraints

- Local file operations are bounded by Path Guard only where actual local enforcement is executed; remote provider authorization is separate.
- Pin actual source revisions and protect secrets/private content from worker exposure; imported Spec Kit Markdown is untrusted as executable instruction.
- Do not auto-install the newest GA release or replace mature host tooling without a support/maturity review and optional user override.
- Preserve reproducibility across Linux/Windows with supported platform tests, but do not claim unperformed Windows/OneDrive/junction acceptance.
- No new mandatory MCP, CI, database, daemon or unattended deployments for this feature.

## Negative and edge scenarios

1. Feature pointer is absent, invalid JSON, `../outside`, absolute path or symlink/junction.
2. `spec.md`, `plan.md` or `tasks.md` is missing, empty, stale, or points to an unapproved host location.
3. Git revision, constitution, AGENTS, role/config or Google BRD changes after review.
4. Official `specify init --force` conflicts with local `.specify` or existing agent skill files.
5. One model simulates multiple worker personalities but claims independent A.1 approval.
6. A developer requests implementation before actual A.1 approval; the agent produces a blocked handoff instead.
7. Spec Kit not installed or feature unselected on a host; S2C standalone mode remains available.

## Acceptance and evidence status

- **DESIGNED:** native feature files and repo-side governance/trace mapping.
- **NOT_RUN:** actual upstream CLI initialization, native skill execution, installed-host tests, Python security/regression suite, A.1/B.1 and release.
- **Owner decision pending:** accepted baseline, supported CLI release, candidate host environment and official native agent integration.
