# Testing and delivery gates — PLAN-080

Workflow: DISCOVER → SPECIFY_PLAN → IMPLEMENT → VERIFY → HANDOFF_REVIEW.

Each stage has a machine-checkable preflight, explicit transition events, and external approval where necessary. Workflow Guard never invokes shell commands, Spec Kit stage executors, Git writes or tests. It cannot issue approval or PASS evidence for an external system.

Maintain deterministic test evidence with command, exit code, environment/platform, source snapshot and required assertions. Report PASS/FAIL/BLOCKED/SKIP/NOT_RUN accurately. Re-run affected validation if requirements, source or configuration changed. Failure during VERIFY returns to IMPLEMENT only by an explicit recorded transition; retain failure evidence.

Release requires real regression in the development repository and disposable host installations. Test source changes follow the host's policy; Gymuro's separate feature/test commit convention is not universally mandatory. Record rollback steps and preserve machine/human handoff ownership.

## PLAN-081 agent evidence requirements

The agent's own text or a machine event cannot independently certify a test or grant approval. For every verification claim record the exact command, platform, revision, relevant result and skipped scenarios; distinguish `PASS`, `FAIL`, `BLOCKED`, `NOT RUN` and `SKIPPED`. A static GitHub source review is not a local test. CI on the precise commit establishes compatibility only for exercised tests; security and migration risks need separate evidence or explicit authorized risk acceptance.

Do not mark a task closed from `workflow_guard.py` on PR #7: its CLOSE scope, phase policy routing, post-VERIFY input invalidation and scope-free status issues are unresolved. Missing gate integrity means `NEEDS_REVIEW`/BLOCKED or a documented limitation, not a fabricated successful end-to-end transition. Follow the [agent runbook](agentRunbook.md) and [security roles](agentRoles.md).

## STOP evidence is not delivery evidence

A STOP handoff summarizes **partial** work and may leave a local session ACTIVE. It must identify current phase, source revision, actual modified paths, pending ACs, evidence freshness, author/ownership uncertainty, risk and a verified persistence flag. It does not turn incomplete tests into PASS or waive independent approval. Do not call `session_guard finish/merge` or Workflow Guard `close` as a STOP implementation. See the [specification](workflowSpecification.md), [STOP protocol](stopAndHandoff.md), [handoff template](../../.source/references/stop-handoff-template.md) and [RTM](../.traceMatrix.md).

## PLAN-085 independent validation loops

The [validation specification](validationSpecification.md) separates **A.1 design validation** (requirements authority, RTM, design, safety, risk and handoff consistency) from **B.1 system acceptance validation** (actual approved behavior, integration, adversarial security, migration/recovery, user/host acceptance on an exact implementation SHA). The [validation report template](validationReportTemplate.md) tracks PASS/FAIL/BLOCKED/NOT_RUN/N/A per criterion and an independent reviewer. A.1 FAIL blocks B; B.1 FAIL blocks release and returns to B or A when design changes. Current planning-stage document checks and existing Python CI are **not** A.1/B.1 outcomes. No change to machine stage enum or runtime test behavior.


## PLAN-089 — Acceptance case design catalogue (not executed)

Canonical requirement statements live in [the unified BRD](../.spec.md), while the bidirectional links are in [RTM](../.traceMatrix.md). This catalogue is the **single** source for planned test scenarios. All entries are `DESIGNED / NOT_RUN`; existence of current unit-test functions does not prove these acceptance scenarios ran. Use two stable scenario IDs per BR: `TC-S2C-BRnnn-P` (positive) and `TC-S2C-BRnnn-N` (negative or adverse). Each test execution must capture TC ID, exact BR/AC, code SHA, config/policy/Google revision, command or manual method, environment/OS, result, raw evidence pointer, owner, skipped cases and follow-up risk.

| BR | Positive ID and condition | Negative ID and expected denial/visibility | Milestone | Minimum evidence | Current status |
| --- | --- | --- | --- | --- | --- |
| BR-001 | `TC-S2C-BR001-P`: Bounded local checkout permits own paths | `TC-S2C-BR001-N`: Traversal, symlink/junction and foreign root denied | M1 | Path Guard + sentinel evidence | **DESIGNED; NOT_RUN** |
| BR-002 | `TC-S2C-BR002-P`: Applicable host/nested AGENTS selected | `TC-S2C-BR002-N`: Conflicting/missing mandatory policy blocks operation | M1 | policy decision with sources | **DESIGNED; NOT_RUN** |
| BR-003 | `TC-S2C-BR003-P`: Seven business, nine planning and five machine phases map | `TC-S2C-BR003-N`: Unapproved phase skip and CLOSE losing original scope denied | M1 | task-bound workflow journal | **DESIGNED; NOT_RUN** |
| BR-004 | `TC-S2C-BR004-P`: A.1 and B.1 use different evidence/decision | `TC-S2C-BR004-N`: Author self-certification or missing reviewer cannot approve | M0/M4 | signed distinct gate reports | **DESIGNED; NOT_RUN** |
| BR-005 | `TC-S2C-BR005-P`: Requirement traced bidirectionally to planned case | `TC-S2C-BR005-N`: Orphan requirement/AC and invented test evidence reported | M0/M2 | RTM audit output | **DESIGNED; NOT_RUN** |
| BR-006 | `TC-S2C-BR006-P`: Risk records category/cause/L/I BEFORE/AFTER | `TC-S2C-BR006-N`: Invented evidence cannot reduce verified residual | M2 | risk matrix revision and source | **DESIGNED; NOT_RUN** |
| BR-007 | `TC-S2C-BR007-P`: Shared cause risk group preserves all members | `TC-S2C-BR007-N`: Unrelated correlated issues not merged by score | M2 | root-cause link and member ledger | **DESIGNED; NOT_RUN** |
| BR-008 | `TC-S2C-BR008-P`: Verified research linked to mitigation decision | `TC-S2C-BR008-N`: Fabricated/irrelevant citation rejected as hypothesis | M3 | source title/version/applicability | **DESIGNED; NOT_RUN** |
| BR-009 | `TC-S2C-BR009-P`: Highest authorized open risk selected or reason noted | `TC-S2C-BR009-N`: Mandatory P0 bypassed by lower-severity work rejected | M1/M2 | risk priority and owner choice | **DESIGNED; NOT_RUN** |
| BR-010 | `TC-S2C-BR010-P`: STOP records factual snapshot; RESUME rechecks | `TC-S2C-BR010-N`: STOP treated as CLOSE or stale source resumed denied | M2 | handoff/status/scope revisions | **DESIGNED; NOT_RUN** |
| BR-011 | `TC-S2C-BR011-P`: Mandatory policy retained in minimal context | `TC-S2C-BR011-N`: Secrets, stale routing or omission blocked | M1/M3 | context pack and redaction | **DESIGNED; NOT_RUN** |
| BR-012 | `TC-S2C-BR012-P`: Standalone host and optional Spec Kit supported | `TC-S2C-BR012-N`: Ambiguous/partial feature blocks bridge implementation gate | M4 | feature refs and read-only check | **DESIGNED; NOT_RUN** |
| BR-013 | `TC-S2C-BR013-P`: Mature supported stack choice/explicit override recorded | `TC-S2C-BR013-N`: Unsupported/unsafe override cannot waive host security | M0/M4 | vendor support and OVR record | **DESIGNED; NOT_RUN** |
| BR-014 | `TC-S2C-BR014-P`: One BRD owner, links resolve, no history loss | `TC-S2C-BR014-N`: Duplicate authority, shadow SRS or deletion of unowned data rejected | M0/M2 | path/link audit and change record | **DESIGNED; NOT_RUN** |
| BR-015 | `TC-S2C-BR015-P`: Fresh portable host install and safe rollback tested | `TC-S2C-BR015-N`: Legacy collision, active session, unsupported OS fail closed | M4 | host/OS matrix and backup hashes | **DESIGNED; NOT_RUN** |
| BR-016 | `TC-S2C-BR016-P`: Exact revision tested and release decision separate | `TC-S2C-BR016-N`: Green CI or reviewer output cannot auto-merge/release | M5 | release dossier with signoff | **DESIGNED; NOT_RUN** |
| BR-017 | `TC-S2C-BR017-P`: n workers assigned under normalized weights and role coverage | `TC-S2C-BR017-N`: n=1, missing expert, quota/cap or invalid weight flagged | M3 | planner manifest and role gap | **DESIGNED; NOT_RUN** |
| BR-018 | `TC-S2C-BR018-P`: Isolated findings cite real pinned revision | `TC-S2C-BR018-N`: Hallucinated line, peer leak and partial failure cannot PASS | M3 | immutable worker reports | **DESIGNED; NOT_RUN** |
| BR-019 | `TC-S2C-BR019-P`: Synthesis retains dissent and verified duplicates | `TC-S2C-BR019-N`: Minority security P0 cannot be voted away | M3 | dissent ledger/raw mapping | **DESIGNED; NOT_RUN** |
| BR-020 | `TC-S2C-BR020-P`: Review linked to RTM/risk/session and source hash | `TC-S2C-BR020-N`: Drift, STOP/retry and out-of-scope write invalidate review | M2/M3 | manifest, stale flags and handoff | **DESIGNED; NOT_RUN** |
| BR-021 | `TC-S2C-BR021-P`: Independent host/reviewer checks actual AC-REV-01..09 | `TC-S2C-BR021-N`: Simulated independent agent or missing A.1/B.1 self-PASS denied | M4 | real host logs and human gate report | **DESIGNED; NOT_RUN** |

### Review-specific boundary and validation

AC-REV-01→TC-S2C-BR017-P/N and BR021-P; 02→BR017-P/N; 03→BR017-N; 04→BR018-P/N; 05→BR019-P/N; 06→BR020-P/N; 07→BR018-N and BR020-N; 08→BR004-N and BR021-P/N; 09→BR017-P and BR021-P. This is a planning link, not an implemented or exercised assertion. Proposed S2C-REQ-038..042 and F38..42 remain DRAFT. Negative cases must include zero useful evidence, source-pinned citation check, single-reviewer correlation, worker timeout, unsafe document injection, budget limits, mixed software+data+policy sources and stale config.

**Execution progression:** review at A.1 for design testability; write actual `.source/tests/` or host integration tests only in authorized B after M1 safety; verify on exact implementation HEAD; obtain B.1 independent host/user acceptance separately. Do not reclassify a planned TC as `PASS` without actual run artifact and reviewed AC applicability.

**Documentation-only audit at PLAN-089:** check 21 BRs × 2 planned scenarios = 42 proposed TC IDs, not 42 automated tests. If the test catalogue changes, regenerate affected RTM references and inspect both directions for unreferenced BR/TC, while retaining historical test evidence rather than overwriting it.
