# Spec2Code — Research and Source Discovery Register (PLAN-084)

> Stage P3 design input. **Observed** here means a path/document was inspected in the repository at development source baseline `0278f005e35cc87e735693ce426bb519b5b67186` and/or PLAN-084 continuation; it is **not** independent stakeholder approval. Upstream reference links below were already present in repository guidance, not newly confirmed live versions. Research must remain read-only and within user-authorized scope.

## 1. Source inventory, provenance and authority

| SRC ID | Repository-relative path / external reference | Type and authority | Research use | Status / gap |
| --- | --- | --- | --- | --- |
| `SRC-001` | [Root agent contract](../../AGENTS.md) | Development instructions; not host policy | Current agent permissions, authority and work modes | OBSERVED; candidate, independent review pending |
| `SRC-002` | [Development specification](../.spec.md) | Draft development SRS/acceptance authority | Mission, security constraints, scope, known design gaps | OBSERVED; incomplete signed SRS |
| `SRC-003` | [Feature register](../.features.md) | Current feature inventory | F01–F37 status / exclusions / candidate functionality | OBSERVED; implementation status not release acceptance |
| `SRC-004` | [Existing implementation-stage workflow](../.workflow/workflowSpecification.md) | Proposed agent workflow + observed runtime summary | Identify what belongs to **later implementation**, not current design | OBSERVED; P0/P1 runtime defects OPEN |
| `SRC-005` | [Stop and Handoff Protocol](../.workflow/stopAndHandoff.md) | Draft agent protocol | Capture future runtime STOP requirements and design handoff considerations | OBSERVED; no Python pause/resume |
| `SRC-006` | [System RTM](../.traceMatrix.md) | Draft requirement/evidence mapping | Baseline feature/AC/test and gap trace | OBSERVED; coverage ≠ approval |
| `SRC-007` | [Path and IO safety source](../../.source/scripts/path_guard.py), [Scope IO](../../.source/scripts/scope_io.py) | Actual implementation evidence | Physical root, managed output paths and Windows risks | OBSERVED; OS race-freedom NOT VERIFIED |
| `SRC-008` | [Policy Resolver](../../.source/scripts/policy_resolver.py), [Workflow Guard](../../.source/scripts/workflow_guard.py) | Actual implementation evidence | Task binding and review gate architecture; PR #7 defects | OBSERVED; 3 P0 + 1 P1 open |
| `SRC-009` | [Session Guard](../../.source/scripts/session_guard.py), [Handoff Store](../../.source/scripts/handoff_store.py) | Actual implementation evidence | Attribution, active session, checkpoint/finish/merge behavior | OBSERVED; checkpoint does not mean STOP |
| `SRC-010` | [Spec Kit adapter](../../.source/scripts/speckit_bridge.py), [integration notes](../../.source/integrations/speckit/README.md) | Existing source and integration guidance | Feature selection, upstream artifact ownership and command boundaries | OBSERVED; upstream version requires fresh check before implementation |
| `SRC-011` | [Runtime config schema](../../.source/scripts/config_loader.py), [bundled JSON](../../.source/.config/workflow.json) | Runtime contract evidence | Fixed five phases, statuses and validation boundaries | OBSERVED; no PAUSED state |
| `SRC-012` | [Test modules](../../.source/tests/test_workflow_guard.py), [CI](../../.github/workflows/tests.yml) | Observed test definitions & CI configuration | Current coverage and known missing integration tests | OBSERVED; no end-to-end runtime STOP test |
| `SRC-013` | [Architecture structure](../.structure.md), [install guide](../../docs/INSTALL.md) | Reviewed layout and source ownership | Development vs installed-host namespace and legacy migration | OBSERVED; real host migration still OPEN |
| `SRC-014` | [Risk register](../.risk.md) and [checklist](../.checklist.md) | Development-governance record | Historic risks, acceptance blockers and change gates | OBSERVED; historic CI must not be recast as current |
| `SRC-015` | [Github Spec Kit repository](https://github.com/github/spec-kit) and [quickstart](https://github.github.com/spec-kit/quickstart.html) | External official **reference**, not host-specific approval | Native SDD steps and agent integration | REFERENCED_NOT_REVALIDATED in PLAN-084; verify revision before binding design |
| `SRC-016` | Host-owned approved `AGENTS.md` and requirements, when installed | **External host authority**; only observed in a selected host checkout | Actual host permissions, business rules and security contracts | NOT_AVAILABLE for generic S2C development; do not invent |

## 2. Research questions and gaps to close

| Question ID | Decision to inform | Candidate source(s) | Status and next activity |
| --- | --- | --- | --- |
| `RQ-084-01` | Does the implementation journal model safely bind CLOSE to the real task/scope? | SRC-008, PR #7 inline review | KNOWN_DEFECT; design a fix contract + negative tests, code later |
| `RQ-084-02` | What is the exact precedence and review owner of source/host/root/nested AGENTS? | SRC-001/002/008/016 | NEEDS_REVIEW; design explicit conflict table and host adoption cases |
| `RQ-084-03` | Which source and Spec Kit artifact changes should invalidate VERIFY/HANDOFF decisions? | SRC-004/008/010/011 | OPEN; specify metadata fingerprints and trust boundary |
| `RQ-084-04` | Can STOP be represented as an orthogonal design handoff without machine state changes? | SRC-004/005/009/011 | ANSWER: yes at agent-document level; no runtime support yet |
| `RQ-084-05` | What are the host migration/recovery procedures on Windows/OneDrive/legacy sessions? | SRC-007/009/013/014 | BLOCKED pending real environment evidence and operator decisions |
| `RQ-084-06` | Which external Spec Kit stages/API semantics are current for Codex and other agents? | SRC-010/015 | REVALIDATE upstream version before implementation |
| `RQ-084-07` | Which F01–F37 requirements are business/security approved versus merely documented? | SRC-002/003/006/014/016 | NEEDS_REVIEW; evidence map does not equal signed approval |
| `RQ-084-08` | How will risk scores and residual risk trigger rework vs implementation backlog? | SRC-014, [Risk Matrix](../.riskMatrix.md) | PROPOSED; independent reviewer to accept thresholds |

## 3. Research protocol

- Search **repository tree → authoritative host/development specs → source/test definitions → historical handoffs → official external references** in that order, selecting by the actual question. A handoff is continuity, not normative truth.
- For each substantive claim, record `SRC-ID`, exact document revision or commit, section/line when available, observation date, owner, and whether the content is `OBSERVED`, `PROPOSED`, `APPROVED`, `UNKNOWN` or `CONFLICTING`.
- Read only files needed for the current question. Do not load secrets or clone unrelated host files. Treat generated architecture metadata as pointers, not executable proof.
- Conflicting canonical sources require escalation; no agent may invent missing authority. External upstream version should be refreshed at the point of a concrete integration design decision.
- After new evidence, update [SRS](../.spec.md), [feature design](featureDesign.md), [RTM](../.traceMatrix.md), [risk matrix](../.riskMatrix.md), and the design handoff. No immediate Python change is implied.

## 4. Source sufficiency and present gate

P3 has sufficient **existing internal evidence to draft planning/design documents**; it has **not** established upstream-current integration facts, host-specific authority or signed SRS acceptance. Status: `READY_FOR_DESIGN_DRAFT` with `RQ-084-02,03,05,06,07,08` open. This is not `APPROVED_FOR_IMPLEMENTATION`.
