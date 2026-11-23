# PLAN-116 — Markdown-first v1 release and incremental integration

Date: 2026-11-18 (Asia/Ho_Chi_Minh). Input Git SHA `d743b34092e28a18cdc5b270ed0e282519bd2175`; existing branch `docs/plan-089-a1-readiness`, PR #10. **PLAN_ONLY / OWNER_REVIEW_PENDING**. Requester direction: v0.x is internal documentation/development and prototype work; first product release starts at **v1.0.0**, Markdown-first for GPT Web. This is authorization to record the plan, not to author/release the profile, execute runtime, accept risk, or advance independent gates. No actual installed Web skill is delivered by this plan.

Authoritative sources: [master specification](../.spec.md), [task ledger](../.plans.md#plan-116--web-v100-delivery-task-ledger), [feature register](../.features.md), [RTM](../.traceMatrix.md), [risk matrix](../.riskMatrix.md), [testing](../.workflow/testingAndDelivery.md), [validation](../.workflow/validationSpecification.md), [Git policy](../.git.workflow.md). Keep existing F/BR/REQ/RM/T/TC IDs and exact historical evidence; this elaboration is not a parallel BRD/SRS or second canonical task ledger. Google stakeholder BRD mirror requires separate owner reconciliation; no mirror update claimed.

## 1. Release architecture and profile boundary

| Layer | v1.0.0 outcome | Later reuse |
| --- | --- | --- |
| L0 Governance | Markdown authority, approved requirements, version contract, A/P1–P9, A.1/B/B.1 | Shared policy and schema |
| L1 Context/trace | Manual minimal/balanced/deep, evidence, tasks, risk, RTM, STOP/RESUME | context_router, session/handoff tooling |
| L2 Integration | Conditional GitHub read/uploaded snapshot; **AGENTS.md Integration Matrix** for AI-agent-executed, explicitly authorized host AGENTS create/adopt/upgrade; manual Spec Kit mapping | v1.1 general connector document workflow, v1.2 Spec Kit Web |
| L3 Enforcement | NONE: no local tools or claimed filesystem sandbox | v1.3 separately accepted runtime |
| L4 Review | Manual evidence-grounded review; external independent human authority | v1.4 Codex/Gemini adapter |
| L5 Automation | No S2C background/runtime automation; an already authorized external AI agent may execute the declarative AGENTS matrix with real tools | v1.5 QA optimization; v1.6 MCP; v1.7 CI/CD |

**v1.0 supported scope:** human-directed GPT Web read/review, Markdown design/specification, task planning, risk/RTM, test design, actual supplied evidence review, and explicit handoff. Connector read only if available, selected source pinned and requester permitted; uploaded files are bounded snapshots, not live Git. Web may propose a Markdown diff for a human. Default repository writing, local filesystem, shell, CLI invocation, secrets export, automated workers, MCP, CI, native Spec Kit execution, automated Git merge/deploy and runtime security guarantees are OUT OF PROFILE. Separately authorized developer-side GitHub documentation commits on this S2C repository are not an installed Web capability. Never assume provider permissions from instructions, profile name, file existence, model output, or a prior chat.

**Scope decision:** RM-001 cannot be closed by this plan. Runtime v0.x stays experimental and excluded from v1.0 distribution. Independent Web-specific scope/AC/risk approval must establish that excluded attack surfaces are unreachable within the actual Web profile and that all applicable P0s are resolved. Any unavailable control remains BLOCKED, not a waiver. Full global A.1 remains NOT_RUN/NO-GO and global B NOT_AUTHORIZED; exact-scope profile A.1 and separate profile B authorization are required. Current developer plan authoring remains A, not product implementation. Retain all applicable existing validation rules (including unrounded R > 99.99% for executable mandatory measurable groups). Do not use 15 selected test cases as a statistical reliability estimate or invent a denominator: before A.1 owner/QA must define mandatory groups, representativeness, R calculation and evidence requirements; if unmeasurable/missing, BLOCKED. Require every mandatory negative security oracle PASS and all applicable P0s disposed; no automatic averaging or fabricated signatures.

### Boundary decisions (to be approved under WEB-004/005)
- DEC-WEB-01 exact supported scope, excluded runtime and policy/per-provider enforcement feasibility.
- DEC-WEB-02 artifact ownership, product/schema/bundle versions, migration contract and compatibility commitments.
- DEC-WEB-03 canonical source/release target plus safe reconciliation of stacked PRs and PR #11 separate findings.
- DEC-WEB-04 approved measurable BR/AC and test-group oracles, security/data sharing authorization and named accountable owners.
- DEC-WEB-05 independent profile A.1, separate profile B permission, later independent B.1 and explicit release approval. Scope changes return to A/A.1. None signed by this author.

## 2. Planned portable package and host layout

One profile, implementation deferred to WEB-006..020. Proposed source path `.source/profiles/web/` is a **future** subtree, not a second developer spec. Package only allowlisted Markdown files; never distribute all of `.source/` for v1.0. Runtime installation docs and existing `.source/SKILL.md` remain prototype records. Future hybrid builds must explicitly select their own profile manifest, not recursively install an ambiguous nested skill.

```text
.source/profiles/web/
  SKILL.md
  BOOTSTRAP.md
  RELEASE.md
  CHANGELOG.md
  references/
    authority.md
    workflow.md
    contextRouting.md
    repositoryScope.md
    speckitIntegration.md
    testingAndReview.md
    stopResume.md
    versionManagement.md
  templates/
    projectManifest.md
    specification.md
    implementationPlan.md
    tasks.md
    traceMatrix.md
    riskMatrix.md
    validationReport.md
    handoff.md
  migrations/
    legacy-to-v1.0.md
```

Release artifact: one pinned Markdown-only file inventory and hashes external to self-referential manifest fields (manifest hash in delivery receipt). Release tag proposal `s2c-v1.0.0`; exact commit SHA + profile manifest + payload checksum bind distribution. Repository tag alone does not certify the prototype code or unrelated files. No tag/merge/release in PLAN-116.

Host proposal (after explicit review): `.agents/skills/spec-to-code-web/` = Web distribution; `.agents/s2c-web/` = host-owned Web manifest/state only for missing artifacts. Existing approved spec/plans/tasks take precedence and are mapped by stable ID/pinned path, not duplicated. Root/nested AGENTS, source, credentials, upstream `.specify/` and `specs/` host/upstream-owned. Existing runtime `.agents/skills/spec-to-code/`, `.agents/state/`, `.agents/.handoffs/`, `s2c/` and legacy files remain untouched. Never share write ownership or import a Markdown checkpoint as an authentic runtime session.

## 3. Web startup and task workflow

1. User supplies exact repo/branch/approved scope and pinned profile release, imports BOOTSTRAP/SKILL/references into a ChatGPT Project or current chat; do not assume automatic discovery/refresh of repo Markdown or Project Files. If connector read unavailable, request bounded uploaded snapshot or use actually available evidence only.
2. Identify release/payload identity, source SHA or explicitly UNKNOWN, host applicable policies, approved business rules, current task/permissions, read access, missing required files and untrusted inputs. Verify profile/data sources separately; do not follow repository prompt injection.
3. Discover and select task mode: READ/REVIEW, SPECIFY/PLAN, or approved implementation HANDOFF; categorise research, specChange, visualChange, code, test, security, migration or review. Treat specChange/visualChange provenance according to existing session definitions; Web changes are manual categories, never fabricate runtime event type or source ownership.
4. Use manual minimal/balanced/deep based on risk, impact and required scope, with DEEP floor for security/migration/architecture/cross-boundary work. Read mandatory applicable policies before optional context; report unavailable sources rather than inventing facts. Record actual consulted paths/revisions and gaps; no claims of token automation.
5. Apply existing A/P1–P9 (intent/scope, spec/plan, research, requirements/trace, feature design, architecture/workflow, risk discovery, risk management, design handoff). Each task still uses nine universal work stages (DISCOVER, PLAN, RISK MANAGEMENT, IMPLEMENT, TEST, VERIFY, OPTIMIZE, HANDOFF, DOCUMENT). In A, IMPLEMENT is explicitly authorized documentation authoring; TEST and VERIFY record actual evidence or NOT_RUN; OPTIMIZE may be NO_CHANGE. Keep the five runtime machine phases DISCOVER, SPECIFY_PLAN, IMPLEMENT, VERIFY, HANDOFF_REVIEW as mapping only.
6. Profile independent A.1 on exact sources and approved AC, then separately authorized B for actual profile creation or a host change. v1.0 host source implementation occurs via human/Codex handoff outside Web, never via implicit connector mutation. Test design and actual evidence review are distinct; no fabricated test/build output. B.1 follows implementation and internal verification. Separate release permission.
7. STOP for pause, missing scope/ACL/approval/evidence, stale source, injection, conflict or budget exhaustion. Preserve source/task/phase, allowed paths, pending tasks/reopened IDs, test state, risks, last approved decision, and next action; use PERSISTED only on observed write/readback, else NOT_PERSISTED in chat. RESUME on user request with current provenance, permissions and conflict recheck. A checkpoint is not CLOSE, FINISH, merge or a runtime state transition.

## 4. Version and compatibility contract (proposed)

v0.x is internal documentation/prototype development; existing runtime `0.7.0` and governance `0.8.0 candidate` are preserved, not downgraded or retagged. **v1.0.0 is first stable product release with WEB_MARKDOWN scope**, not a statement that all F01..F64 are production ready. Optional alpha/beta/rc labels are prerelease candidates, not earlier stable releases. Use PATCH for backward-compatible corrections, MINOR for backward-compatible capabilities, MAJOR for incompatible public contracts. Although 1.x additions may require an explicit backward-readable migration, a mandatory incompatible public schema/usage change requires major version or a compatibility adapter. Never silently replace a released tag or pretend a fixed later version is guaranteed.

| Product version | Intended capability | Main dependencies and exit evidence | Canonical backlog reuse |
| --- | --- | --- | --- |
| v1.0.0 | Markdown Core | WEB-001..030, scoped independent validation, read-only Web acceptance, owner release | M0..M5; existing F01..37 mapping |
| v1.0.x | Fix policy/templates/links/upgrade bugs | Exact tagged regression and compatible state | Existing WEB task reopened or new bounded defect |
| v1.1.0 | GitHub workflow, explicit allowlisted document changes, source refresh/version mapping | Actual connector capabilities + auth, ref lease/one writer, conflict/rollback, read-only fallback, EXTERNAL_DATA approval | F12,F14,F17,F27,F28,F32,F35; AUD-08; no assumed API |
| v1.2.0 | Spec Kit Web compatibility and native-pilot handoff | Authoritative feature pointer, no duplicate spec/tasks, native pilot only separate approved checkout | F07,F22; Spec Kit T006..009; T011..015 retained |
| v1.3.0 | Hybrid Runtime / Codex / local native Spec Kit when accepted | T112-05..09, all applicable security/P0 remediation and independent scoped A.1/B/B.1, actual host and migration tests | F04..06,F09,F13..18,F26,F29,F30,F31,F37; T013..014; PLAN-111/112/115 |
| v1.4.0 | Codex/Gemini review adapter | Immutable redacted snapshot, verified agy API/host, queue/dedupe/cost/semantic validation, actual AGY-TC-01..14 and B.1 | F38..42, T088-05..09, T113-07/08, T114-06 |
| v1.5.0 | Quality and optimization | Measured token/latency/recall/precision baseline, test evidence/dashboard, no loss of mandatory policy | F20,F47,F49..52,F56,F61,F63 (candidate scope) |
| v1.6.0 | MCP provider integration | Actual isolated toolserver, reviewed schema/credential/data boundaries and adversarial acceptance | F10,F44,F54; RM-047/048 |
| v1.7.0 | CI/CD / automated checks and delivery proposals | Exact build/skip evidence, least-privilege jobs, signed provenance, rollback; separate merge/release approval | F20,F47,F52,F57,F59..62,F64 (candidate scope) |
| v2.0.0+ | Breaking changes only if approved | Full migration/compatibility/release decision | Existing feature IDs retained or explicit successor mapping |

Later versions are sequencing candidates, not dates or guaranteed inclusion. Maintain per-release supported host/version matrix and independent scope gates. Do not force all proposed F43..64 into any release. Github read permission already can be conditional in v1.0; v1.1 adds governed change workflows, not first-ever read. v1.2 Web does not run native CLI; runtime execution belongs to separately accepted v1.3 capability.

Proposed `projectManifest.md` YAML front matter (human-readable, later parser contract not yet implemented). Example values for a future released package; NOT an observed install:

```yaml
schemaVersion: 1
productVersion: 1.0.0
profile: WEB_MARKDOWN
bundleVersion: 1.0.0
releaseRef: s2c-v1.0.0
releaseCommit: UNKNOWN
distributionManifestRef: UNKNOWN
hostRepository: UNKNOWN
hostBranch: UNKNOWN
hostSourceRevision: UNKNOWN
artifactMapRef: UNKNOWN
migrationStatus: NOT_RUN
capabilities:
  markdownPlanning: {available: UNKNOWN, authorized: UNKNOWN, activated: false}
  githubRead: {available: UNKNOWN, authorized: UNKNOWN, activated: false}
  githubWrite: {available: false, authorized: false, activated: false}
  runtime: {available: false, authorized: false, activated: false}
  gemini: {available: false, authorized: false, activated: false}
  mcp: {available: false, authorized: false, activated: false}
  ci: {available: false, authorized: false, activated: false}
```

Owner adopts schema/type/allowed-value/unknown-field policy before implementation. Use plain Markdown + constrained front matter, not executable scripts/embedded instructions as data. Strictly distinguish distribution version vs product version vs project-state schema vs host source SHA vs historical runtime prototype version. Version is not permission. A capability is activated only if supported by profile, actually available and explicitly authorized. Unknown/disabled falls back to read-only/manual handoff where safe; missing mandatory control blocks. Preserve unknown fields during compatible migration only if safe and reviewed; never interpret unknown as permission. Artifact map records canonical spec/plan/tasks/RTM/risk paths, owner, baseline/template version and observed hash or UNKNOWN; no duplicate document authority.

## 5. Adoption, upgrade and rollback (WEB-016..020)

| Source -> target | Procedure | Acceptance |
| --- | --- | --- |
| New host -> v1.0 | Owner-approved directory map, copy only Web manifest paths, reuse existing docs, manually import/pin Project files/instructions | WEB-TC-01/02/03/07 |
| v0.x development/runtime -> v1.0 Web | Inventory legacy skill/state/active sessions and host authority; read-only evidence crosswalk; add separate Web profile with preserved original IDs and source references | No runtime rewrite, no duplicate task ledger; no fake session; WEB-TC-02/10/15 |
| v1.0.x -> v1.1 | Dry-run old pristine bundle vs customized host vs new; add connector and permission mapping only within approved write scope | WEB-TC-11/12/15 plus connector negative tests |
| v1.1 -> v1.2 | Add Spec Kit mapping; existing `.specify/` and `specs/` remain owner/upstream artifacts | No duplicate task IDs, unsafe pointer/overrides rejected; native remains optional/handoff |
| v1.2 -> v1.3 | Separate authorized runtime installation at established runtime layout; map Web checkpoint refs to new validated local sessions; do not transplant old state/events | Windows/Linux tests, T112 security and runtime scope accepted, migration and rollback validated |
| v1.3 -> v1.4 | Enable Gemini only after sandbox, data approval, manifest/queue and acceptance; preserve manual review fallback | Actual AGY cases and costs; missing mandatory review blocks |
| v1.4 -> v1.5 -> v1.6 -> v1.7 | Adjacent migrations, capability contracts and independent validation; no implicit tool elevation | Version-specific positive/negative tests, owner approvals, no secret access |

Multiple-version upgrades must follow each **supported verified adjacent path**, recording input/output schema, hashes and per-step checkpoint. Do not promise direct jumps without tested compatibility. No unattended or unapproved migration in v1.0. The host AI agent may perform **matrix-guided AGENTS.md-only creation/adoption/version upgrade** after real path-scoped approval, with actual write tools and readback; all other migration remains manual/explicitly authorized. For every installation or migration:
1. Preflight: pin release ref/SHA, verify allowlisted payload provenance/hashes, validate current installed version/schema, supported path, clean/safely frozen authorized scope, effective host policies, current task/active sessions. If source or access cannot be verified STOP. Never treat a chat claim as actual byte backup.
2. Inventory and three-way comparison of old released file, actual host copy, new release. Classify distribution-owned, pristine/customized template, project-owned, host-owned, session state, historical evidence, unknown. Record allowed added/changed paths, owners, hashes, conflicts, unsupported fields. Never overwrite unknown, unowned or customized data without explicit reviewed merge.
3. Obtain approval for exact diff, backup destination and restore procedure; preserve project data in owner-controlled reviewed storage; no secret export. Snapshot before writing; capture case/collision and path semantics with appropriate actual capabilities.
4. Apply in bounded ordered steps by an authorized executor (AI agent with actual scoped host AGENTS write capability and approval, or manual user fallback; broader connector changes remain v1.1, local runtime requires separate verified safety); no deletion of legacy/historical data or automatic git reset. Use staged candidate distribution, reconcile owned docs and preserve IDs/approval provenance; don't edit installed version until completion.
5. Re-read actual files/hashes, validate task/requirement/risk ID equality or explicit mappings, links, schema, policy, capability denial, conflict handling, rollback and old/new behavior. Record actual logs, failed/skipped cases and source revision. If test runner unavailable record NOT_RUN and keep candidate unaccepted.
6. Publish manifest/version last after owner-approved acceptance, refresh ChatGPT Project instructions/uploads manually where needed, verify the active chat actually resolves new profile version and references; old chat dependencies may require explicit bootstrap. Record migration result and Git receipt when authorized. A partial migration is never a new installed version.
7. On failure STOP; preserve logs and current changes, do not change unowned paths or discard collaborators' edits. Restore only reviewed affected files from verified old payload + approved backups; if source drift/conflict stop for owner decision. Verify old profile and state, record rollback result before resuming; if rollback cannot be verified remain BLOCKED. No blanket reset, force push, deletion, or blind downgrade.

## 6. Integration map and future implementation

Reuse current `.source/scripts/` rather than build duplicate engines: path_guard/scope_io = actual local scope/managed IO; config_loader/governance_schema = schema validation; scan_infrastructure/architecture_tree = inventory/static architecture; context_router/policy_resolver = bounded routing; session_guard/handoff_store = runtime session and change history; workflow_guard = five actual phases; speckit_bridge = read-only feature discovery; mcp_boundary = library, not server. Runtime adoption requires verification of AUD-02 (handoff direct IO), AUD-03 (installed config fingerprint), A1-SEC-09/10/11, T112-05..09 plus other applicable open risks. Do not assume ordinary CI certifies a hostile host. PLAN-113/114 review contract remains design-only; use existing worker/synthesis IDs and test cases. No code or configuration edited here.

## 7. Delivery, dependency, quality and change management

Canonical 30-row ledger is [PLAN-116](../.plans.md#plan-116--web-v100-delivery-task-ledger); planned cases [WEB-TC-01..21](../.workflow/testingAndDelivery.md#plan-116--web-profile-acceptance-design). Batches: WEB-001..005 (A/design freeze and actual independent scope A.1/B authorization); 006..010 (core); 011..015 (state/templates); 016..020 (install and migration); 021..025 (verification); 026..030 (acceptance and release). Gating dependency: WEB-005 independent A.1 and separate B approval before any product implementation in WEB-006..020. If drafts required for A.1, author design only in A, rerun applicable A.1 after material change; no retroactive approval. WEB-028 verifies valid previous A.1/B and records independent B.1, not a shortcut. WEB-030 requires distinct release approval. All work packages initially PLANNED/NOT_RUN; record DONE_VERIFIED only with task scope, observed source and actual outcome evidence (documents authored vs executed tests separate), responsible authority, risk and rollback. Reopened task retains ID; count unique open IDs, not aliases or subtests. Phase review checkpoint, after each batch and any failure: report remaining/new/reopened/blocked IDs by owner, actual SHA, scope, test denominators, pending decisions, and next safe action.

Keep one current branch `docs/plan-089-a1-readiness` pending separately approved release target. PR #11 findings and unique main/InitialVersion history require reconciliation under WEB-002; no deletion, automatic merge, rebase, squash of shared history or force update. Use a single writer, expected-head lease, bounded changed files/diff, aggregate related changes into cohesive commits (not one commit per line/task). Review each commit individually; Git write permission does not grant merge, tag, release, deployment or host modification. Future release packages are verified independently of prototype files. Rollback is owner-reviewed revert and verified restoration of owned changes, preserving history/evidence. Release documentation includes support, limitations, version compatibility, migration path and acceptance evidence. No remote or local runtime tests, profile files, releases, or Google updates are part of this plan commit.

## 8. Owner-requested AGENTS.md integration design amendment (2026-11-23, not implemented)

V1.0 must include a **declarative AGENTS.md Integration Matrix** ([AGM-01..17](webV1AgentsIntegrationMatrix.md)) so that an **existing authorized AI agent** can perform new host AGENTS creation, non-destructive adoption and version upgrades. S2C provides matrix rows, proposed text, owner/source/permission requirements, exact diff, three-way merge, conflict handling, idempotence, rollback and verification oracles. **S2C does not execute a separate installer, daemon, local command or background job**. The agent with genuinely available permissioned tools performs the scoped write and readback. With only a snapshot/read-only provider it provides a matrix and patch/handoff; no installed-file claim.

This is a **narrow V1.0 exception to manual-only adoption**, *not* blanket authorization for GitHub code modification, unrestricted repo writing, local OS operations, native Spec Kit, MCP or CI. User-design direction alone does not grant host AGENTS edit permissions. Revise DEC-WEB-01/02/04 and approve DEC-WEB-06, add six designed AGENTS cases WEB-TC-16..21 (21 total, zero executed), and require fresh independent A.1 plus separate B scope before any profile authoring. Existing WEB-008/011/016..020/023..025 carry the implementation and test work: no new WEB task IDs, no F65 and no promotion of old status.
