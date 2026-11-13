# Spec2Code v0.7.0

> **Current baseline: PLAN-092 / unified BRD/SRS v1.5 + Spec Kit bootstrap (PLAN-087..091 retained).** Start with [the unified BRD, architecture and M0–M5 implementation plan](.agents/.spec.md). Detailed and historical sections below are supporting references; they do not supersede current scope, evidence or lifecycle mapping.


Infrastructure-aware, universal Spec-to-Code agent skill with optional read-only upstream GitHub Spec Kit bridge.

**Status:** repository layout migration candidate; prior Windows/security risks remain open. Requires Python 3.10+ and Git. Spec Kit CLI is separate.

## Repository layout and governance

Development repository is organized under `.agents/` (requirements, features, plans, risks, handoffs, workflow) and `.source/` (portable skill, scripts, tests, references, integrations, JSON configs). Read [structure](.agents/.structure.md), [features](.agents/.features.md), [plan](.agents/.plans.md), [risk register](.agents/.risk.md), [checklist](.agents/.checklist.md) and [handoff](.agents/.handoffs/v0.7.0-layout-handoff.md).

The **installed target project** is different: copy the `.source/` skill bundle into `<target>/.agents/skills/spec-to-code/`; keep target-owned `.agents/state/`, `.agents/.handoffs/`, `.specify/` and `specs/` separate. See [INSTALL](docs/INSTALL.md).

## Existing capabilities

Strict JSON config loading, Git root and path containment, physical checkout-bound sessions, static infrastructure inventory and architecture graph, adaptive minimal/balanced/deep context routing, source-change provenance, exact-session handoff, read-only Spec Kit feature bridge and MCP-ready authorization *library*. No real MCP server, arbitrary shell/remote Git operation or automatic authorized code-writing agent exists.

## Development tests

```sh
python -m unittest discover -s .source/tests -v
```

## Target project outputs

- `.agents/state/`: local session, inventory, architecture graph and context cache.
- `.agents/.handoffs/.details/`: session-specific pending change logs, and `.agents/.handoffs/.buildnotes.handoff.md`: verified merge ledger.
- `s2c/.summerize.md` and `s2c/<Layer>/...`: generated read-on-demand architecture metadata separate from project source.
- Legacy `.handoffs/`, root `.summerize.md`, and root layer directories are **not** deleted or moved automatically. Finish old sessions, back up and migrate explicitly.

## Portable installed skill example

From the **target Git repository root**, after copying `.source/` contents into `.agents/skills/spec-to-code/`:
```sh
python .agents/skills/spec-to-code/scripts/session_guard.py --root . start
python .agents/skills/spec-to-code/scripts/speckit_bridge.py --root . --stage status
```

The Spec Kit `implement` stage requires active feature `spec.md`, `plan.md`, `tasks.md`. Never treat an artifact's existence as human approval.

## Security and release status

No unconditional overwrite or deletion of host project files is authorized by this layout change. POSIX anchored file operations offer additional containment; Windows TOCTOU, case-folding, path alias, CRLF and generated-document collisions need additional verification. See [risk register](.agents/.risk.md) and [Path Guard](docs/PATH_GUARD.md).

## v0.8.0 candidate — Core + Governance Integration

Development is occurring on `feat/governance-integration-v0.8.0`; the v0.7.0 layout/Windows CI PR #6 was integrated into `spec2code/InitialVersion_v0`. This is **not a stable release**.

The candidate adds task-scoped, read-only host policy discovery, Policy Resolver references in Context Router, and a non-autonomous five-stage Workflow Guard with event integrity checks. The task description and affected paths must be supplied consistently for implementation gates. Evidence references and hash-chained workflow events never constitute independent authorization. Consult `.agents/.plans.md`, `.agents/.risk.md`, and `.agents/.checklist.md` for outstanding acceptance, security and migration risks.

The real MCP server, automatic code execution, unattended Git mutations, Windows filesystem-race protection, and automatic legacy-data migration are **not** provided by this candidate.

## Agent operating documentation (PLAN-081, v0.8.0 candidate)

The [development AGENTS contract](AGENTS.md) routes ChatGPT/Codex work by **authority, task, phase and allowed action**. The [logical agent roles](.agents/.workflow/agentRoles.md) and [agent runbook](.agents/.workflow/agentRunbook.md) cover requirement analysis, policy review, implementation, verification and exact-session handoff without pretending there is an autonomous multi-agent executor. When installed in another project, this repository's AGENTS is **not** copied as that project's root policy; review the [optional host AGENTS guidance](docs/AGENTS_PATCH.md) instead.

Official Spec Kit commands run through the agent's installed integration. Its `.specify/` and `specs/` are never owned by the S2C bridge. The current v0.8 Workflow Guard has unresolved PR #7 correctness blockers; PLAN-081 instructions do not fix them. No stable release or security clearance is implied by the documentation.

## Concrete system RTM and interruptible workflow (PLAN-082/083)

See the [System Requirements Traceability Matrix](.agents/.traceMatrix.md) for F01–F37 requirement/AC, source, test and gap mapping. The [Workflow Specification](.agents/.workflow/workflowSpecification.md) and [STOP & Handoff Protocol](.agents/.workflow/stopAndHandoff.md) require a controlled STOP at any phase, an observed state snapshot, a truthful persisted-or-chat handoff and a checked RESUME. The [STOP Handoff Template](.source/references/stop-handoff-template.md) is bundled with the portable Skill.

This is **interactive agent guidance**; a machine `pause/resume` command is not implemented in Workflow Guard. STOP never silently closes a session, merges a handoff or authorizes Git/release actions. See [PR #8](https://github.com/RyugaWork/spec2code/pull/8) for candidate documentation and [PR #7](https://github.com/RyugaWork/spec2code/pull/7) for unresolved runtime issues.

## Current work phase — PLAN-084: Planning and Specification

Spec2Code is currently refining its **design package**, not implementing STOP/RESUME in Python. Start with the [nine-stage planning workflow](.agents/.workflow/planningSpecificationWorkflow.md), [SRS authoring plan](.agents/.documents/systemSpecificationPlan.md), [source research register](.agents/.documents/researchRegister.md), [feature design catalogue](.agents/.documents/featureDesign.md), [scored risk matrix](.agents/.riskMatrix.md) and [design handoff template](.agents/.workflow/designHandoffTemplate.md). Design passes discover and reprioritize risks, then improve the **specification/design** for the highest-risk open item. Implementation needs a distinct approved phase, and the existing [five-stage specification](.agents/.workflow/workflowSpecification.md) applies to that later lifecycle.

## PLAN-085 — Validation checkpoints A.1 and B.1

Process: **A Planning & Specification → [A.1 Design Validation](.agents/.workflow/validationSpecification.md) → B Implementation (separate permission) → B.1 System/Acceptance Validation → separate release approval**. A.1 verifies design quality, authority, traceability, risk and handoff before implementation; B.1 verifies real behavior, security, host/OS and stakeholder acceptance after implementation. [Validation report template](.agents/.workflow/validationReportTemplate.md) preserves per-check evidence and feedback paths. Neither checkpoint runs automatically or changes Workflow Guard runtime states. Current work remains A/design only.

## Stable technology choices and explicit user override — PLAN-086

For **both Spec2Code's own source/toolchain and any integrated repository**, Agents recommend **supported, mature, widely adopted** Python, PowerShell, named SQL DBMS, .NET and other technology majors and conventional project structures by default, not the newest version. [Universal technology policy](.agents/.documents/technologyVersionPolicy.md), [assessment](.agents/.documents/technologyAssessmentTemplate.md), and [User Override record](.agents/.documents/technologyOverrideTemplate.md) cover official support, maturity, adoption, compatibility, safety, migrations and architecture evidence.

**Explicit user choice can override the conservative default.** For example, a newly released **supported** .NET 11 can be the requested design version with documented compatibility risk; the default .NET 10 LTS remains a dated illustration. EOL .NET 8 (as of 2026-11-13) or another unsupported runtime requires additional safety/legacy acceptance, not false claims of support. For Python, PowerShell and SQL use each product's current vendor lifecycle and actual engine/edition, not .NET-specific version rules. An override records the desired stack, exact S2C/host scope, risk and approvals, but **never automatically modifies code** or bypasses host security, Path Guard, testing or Git permission. Both A.1/B.1 validations remain NOT RUN.


## Design and implementation governance (PLAN-087 + PLAN-088)

The single canonical development BRD, architecture, functional integration model and dependency-based M0–M5 implementation plan is [`.agents/.spec.md`](.agents/.spec.md). It currently covers BR-001..021, including **proposed** weighted multi-agent review, with linked [RTM](.agents/.traceMatrix.md), [risk matrix](.agents/.riskMatrix.md), [features](.agents/.features.md), [task ledger](.agents/.plans.md) and [agent contract](AGENTS.md). [Google BRD](https://docs.google.com/document/d/1M3_2tNUxOXci83pcpPCzBkxwvRvixeT7FYeGyIsFOa4) is the stakeholder-facing mirror; reconcile revisions and BR IDs before treating a new draft as approved.

The S2C portable skill source is in `.source/`; governance records in `.agents/`; documentation and installation guidance in `docs/`. This repository's default `main` may not contain the development tree until an explicitly reviewed integration. Current architecture/runtime and proposed review automation must not be confused: the five-phase `workflow_guard.py`, Path Guard and session tools exist as candidate development code; multi-agent review orchestration and native STOP/RESUME do **not**. A.1/B.1 and actual implementation/merge/release require distinct approvals.

## PLAN-089 — Staged documentation completion toward A.1

The canonical [master specification](.agents/.spec.md) now contains 12 substantive SRS chapters (Sections 15), proposed cross-module contract definitions (Section 16), and phased acceptance design (Section 17). The [test catalogue](.agents/.workflow/testingAndDelivery.md) lists two **planned** cases per BR-001..021 (42 total; no execution claimed), and the [RTM](.agents/.traceMatrix.md) preserves their reverse mappings. The [SRS review inventory](.agents/.documents/systemSpecificationPlan.md) records outstanding decision/owner/evidence gaps. Google BRD Draft v1.4 mirrors the stakeholder-level specification and plan.

This work is documentation and design only: `A1_NOT_RUN`, `B_NOT_AUTHORIZED`, `B1_NOT_RUN`. No actual worker orchestration, runtime STOP/RESUME, merged PR, unit-test PASS or release decision follows merely from writing these chapters. The next required step is independent A.1 and explicit scope approval; code safety M1 must precede new worker implementation M3.


## Spec Kit adoption for S2C development (PLAN-092)

This repository now contains a **native-compatible Markdown bootstrap** for official GitHub Spec Kit, allowing [ChatGPT Web/GitHub mode](.specify/README.md) to maintain a selected feature's [spec](specs/001-s2c-speckit-integration/spec.md), [plan](specs/001-s2c-speckit-integration/plan.md) and [tasks](specs/001-s2c-speckit-integration/tasks.md) while following [root AGENTS](AGENTS.md), [draft Constitution](.specify/memory/constitution.md), [RTM](.agents/.traceMatrix.md) and risk gates. Active feature comes from [`.specify/feature.json`](.specify/feature.json), **not** from Git branch names.

For a coding-agent native workflow, the official `specify-cli` + selected agent integration must still be installed and tested in an authorized **disposable checkout**; scripts and official agent skills have **not** been installed or invoked by these GitHub-only commits. See [Spec Kit integration guide](.source/integrations/speckit/README.md) and [upstream existing-project setup](https://github.github.com/spec-kit/how-to/existing-projects.html). No automatic CI/MCP/new feature branch or implementation permission was added. A.1/B/B.1 still require separate evidence and approval.


## PLAN-094 — Continue Spec Kit development from the selected feature

For **ChatGPT Web**, use [feature quickstart](specs/001-s2c-speckit-integration/quickstart.md) and [official-template feature spec](specs/001-s2c-speckit-integration/spec.md) with [research](specs/001-s2c-speckit-integration/research.md), [plan](specs/001-s2c-speckit-integration/plan.md) and [24 designed test cases](specs/001-s2c-speckit-integration/checklists/integrationAcceptance.md). The authoritative 12-row [RTM](.agents/.traceMatrix.md) and root AGENTS still govern all tasks. T010 draft reconciliation is documented; native SK-03 remains unavailable in this offline runner. Do not treat manually edited Spec Kit files as if `specify init` or official coding-agent skills had run.

### PLAN-095 — Web-mode execution and native safety evidence

[Web/GitHub workflow](.agents/.workflow/specKitWebWorkflow.md) describes browser-based Spec Kit artifact steps without claiming native CLI execution. [Native execution gate](.agents/.workflow/specKitNativeExecutionGate.md) prevents treating upstream checklist continuation or author-executed tasks as S2C A.1/B permission. [Four scoped GitHub/static positive cases](.agents/.documents/specKitWebModeEvidence095.md) are documented with exact Git commit/blob/compare evidence; 20 additional feature cases and every native host/security gate remain unrun. The existing PR stays Draft; no new branch or runtime source file was added.

## PLAN-096 — Actual Spec Kit bridge contract-gap assessment

The [source-bound PLAN-096 bridge audit](.agents/.documents/specKitBridgeSourceAudit096.md) identified four unverified runtime gaps in feature namespace policy, duplicate pointer JSON handling, empty mandatory artifact handling and duplicate task-ID detection. [Feature acceptance catalogue](specs/001-s2c-speckit-integration/checklists/integrationAcceptance.md) adds **four planned, unrun** negative test cases `SK96-NEG-01..04`; the existing 24-case test status remains **4 scoped Web/static PASS / 20 NOT_RUN**. Read the [PLAN-096 handoff](.agents/.handoffs/plan-096-bridge-source-audit-handoff.md) before taking any B-phase action. No S2C Python/JSON/CI file was changed; native Spec Kit CLI/skills and independent A.1/B.1 validation remain NOT_RUN.
