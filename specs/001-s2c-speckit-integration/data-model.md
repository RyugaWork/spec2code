# Feature Artifact Data Model — Logical contract, not runtime schema

> `DESIGN_DRAFT`. No new JSON schema, persistence layer, external API or Python model was implemented. Existing `.source/.config/speckit.json` and `.source/scripts/speckit_bridge.py` retain their actual observed behavior.

## Model ownership and associations

| Logical entity | Minimum required fields or source | Owner and immutable properties |
| --- | --- | --- |
| `DevelopmentSource` | repository, Git ref, exact commit SHA, root AGENTS and S2C BRD/RTM/risk refs; provider-specific Google revision if consulted | Git SHA and provider revision identify **different** content sources |
| `FeatureSelection` | `feature_directory` in `.specify/feature.json`, optionally authorized `SPECIFY_FEATURE_DIRECTORY`, source identity | Selected folder must be contained within an approved checkout for S2C-managed reads; branch name is not a selector |
| `ConstitutionRevision` | `.specify/memory/constitution.md` content/ref, review status and actual owner decision | DRAFT remains non-ratified; not a replacement for root/host AGENTS |
| `FeatureSpecification` | `spec.md`, user stories, stable `SKI-FR-001..012`, AC, negative paths | Refines global S2C BR/REQs without becoming a parallel master |
| `FeaturePlan` | `plan.md`, alternatives, architecture, source risk, dependencies, rollback | Decisions must be traceable and should not silently permit implementation |
| `FeatureTask` | stable `T001..T015`, description, dependencies, phase, explicit evidence status | Checkbox status represents documented task completion, not executed tests or permission |
| `AcceptanceCase` | stable `SKI-TC-<FR>-P/N`, preconditions, action, expected observable outcome, evidence, actual execution state | All remain NOT_RUN until a real run with source SHA, environment, observed result |
| `NativePilot` | pinned tag+source, host OS, Python, generated file list, before/after hashes, CLI exit/stdout/stderr, collision and rollback review | A CLI trial is not automatically independent A.1 or production host acceptance |
| `HandoffSnapshot` | last exact source/policy/feature pointers, persisted location and truthfulness, open tasks/risks, next safe step | STOP may be documented without a runtime-close; RESUME revalidates all boundaries |

## State constraints

`DocumentDraft` → `DocumentReviewed` only with actual source inspection; `RatifiedConstitution` requires named human decision. `NativePilotRequested` → `PreflightApproved` → `RuntimeExecuted` requires actual host/permissions and tool evidence; on absent network report `BLOCKED`, not `PASS`. `A1_PASS` requires independent real approval and **never implies B authorization**. `B1_PASS` and release remain separate owner gates.

**Invariant:** the S2C bridge may return `READY` when its static file prerequisites are satisfied, but cannot set any A.1/B/B.1 decision. Upstream-generated scripts/skills are separate assets and must never be inferred from a manually authored `.specify/` folder.

## Bidirectional trace keys

`Global BR-xxx / S2C-REQ-xxx / S2C-NFR-xxx` → `SKI-FR-xxx` → `feature spec` → `Txxx` → `SKI-TC-xxx-P/N` → `actual evidence/ref` (currently NOT_RUN). See [master RTM Section L](../../.agents/.traceMatrix.md) and [acceptance catalogue](checklists/integrationAcceptance.md).

## Compatibility and migration

No runtime migration now. A future **B-authorized** adapter addition must define explicit schemaVersion, old/unknown-field behavior, atomic/non-overwriting file ownership, timeout and failure semantics, tests across supported OS and rollback. Connector IO relies on provider permissions; local Path Guard does not secure GitHub-hosted reads/writes.
