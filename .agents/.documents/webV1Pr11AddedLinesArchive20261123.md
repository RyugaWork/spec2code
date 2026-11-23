# PR #11 — archival preservation of all added PLAN-091 content

**HISTORICAL_SOURCE_ONLY / NOT_ACTIVE_POLICY**. Original PR #11 head `e119100e17ed138a1bbd1d2b600d9b890d5441b7`, historical parent baseline `1dae9338f4d38518e897212cdf80ba47239a7671`. This annex captures the exact **180 added source lines** in six originally modified files. PR #11's seventh changed file, the original [150-line independent-review *preflight* report](../.handoffs/plan-090-a1-preflight-review.md), is preserved intact under its original path, source blob `685b14477e9430e6c58270e1c0991e1e737d4ac4`. Historical Git blobs are also retained by the true merge parent.

**Canonical collision guard:** Historical aliases F43..F50, RM-034..040, PLAN-091/T091, SRS Section 18 and AGENTS Section 15 conflict semantically with current Phase A. These quotations have no governance precedence and grant no tool/host/CI permission. Refer to the [PR #11 collision matrix](webV1Pr11CollisionReconciliation20261123.md); NEVER renumber current F/RM IDs from this annex.

| Original file | Exact additions | Historical blob |
| --- | ---: | --- |
| `.agents/.features.md` | 19 | `23d5aba086e28dbc49749477f46581a242c48260` |
| `.agents/.plans.md` | 23 | `012841fba8872cf75c25476f209fb2d2873aa0e0` |
| `.agents/.riskMatrix.md` | 16 | `55d9cc9353b96408633aa446e860728730a6237a` |
| `.agents/.spec.md` | 97 | `1eecaf1aa815090d2147b4ad11f3138682862fe2` |
| `.agents/.traceMatrix.md` | 17 | `806a83d6a7cdfd88d3b6effb4c85543d51dff575` |
| `AGENTS.md` | 8 | `7e14bd1d048946887f4bc8047dfb652d69852d17` |
| **Total** | **180** | |

## Exact inserted text, grouped by historical path

### Historical diff: `.agents/.features.md` (19 inserted lines)

Original blob `23d5aba086e28dbc49749477f46581a242c48260`; exact insertion order as GitHub compare patch. The following is historical text, not active canonical policy.

~~~~~markdown

## PLAN-091 — Modular capability registry and compatibility matrix (PROPOSED)

**Canonical contract + full existing F01–F42 compatibility matrix:** [master Section 18](.spec.md#18-plan-091--modular-capability-compatibility-fallback-and-trusted-integration-design-only). The tables below index **candidate** features only; source-level statuses for F01–F42 above are unchanged. No independent provider, CI admission runtime or new tests exist at this snapshot.

| Proposed feature | Required module | Current status | Depends on / acceptance |
| --- | --- | --- | --- |
| F43 | Capability Registry and verifiable module manifest | PROPOSED | F08/F27, trusted manifest validation; AC-MOD-01 |
| F44 | Adapter contracts and compatibility negotiation | PROPOSED | F43 + source/OS/version/permission policy; AC-MOD-02 |
| F45 | Fail-closed selection, safe fallback and circuit breaker | PROPOSED | F04/F09/F17/F28/F43/F44; AC-MOD-03 |
| F46 | Scoped Auto-Approve and guarded external tool execution | PROPOSED | Path Guard/sandbox/secrets gate, F45; AC-MOD-04/05 |
| F47 | Bounded multi-worker scheduler, independent verification and handoff | PROPOSED | F05/F06/F30/F37/F38–F42; AC-MOD-05/10 |
| F48 | Browser UI/E2E test adapter with independent assertions | PROPOSED | F44/F46/F47; AC-MOD-06 |
| F49 | S2C-controlled CI/CD workflow security admission, evidence and release firewall | PROPOSED | M1 security fixes, F44–F47; AC-MOD-07/08/10 |
| F50 | Cloud-task / Jules adapter constrained to PR proposals | PROPOSED | F44/F45/F47/F49; AC-MOD-09/10 |

**Compatibility states (distinct from feature development state):** `SOURCE_ONLY` code observed, `DOC_ONLY` instruction/design, `EXTERNAL_CANDIDATE` upstream affordance only, `NOT_ADMITTED` no trusted S2C integration, `SANDBOX_TESTED` exact-version negative/positive evidence, `ENABLED` separate approved runtime action, `QUARANTINED` blocked on drift/abnormality. `IMPLEMENTED` in the historical register does **not** imply `ENABLED`.

Proposed requirements S2C-REQ-043..050 and tests AC-MOD-01..10 are recorded in [RTM Section K](.traceMatrix.md) as DRAFT/NOT_RUN. [PLAN-091](.plans.md) is the task ledger; [Risk Matrix](.riskMatrix.md) owns estimated RM-034..040. Existing F19 deferred and F21/F22/F23 DROPPED restrictions are preserved.
~~~~~

### Historical diff: `.agents/.plans.md` (23 inserted lines)

Original blob `012841fba8872cf75c25476f209fb2d2873aa0e0`; exact insertion order as GitHub compare patch. The following is historical text, not active canonical policy.

~~~~~markdown

## PLAN-091 — Modular integration compatibility and controlled CI/CD admission (2026-11-14)

**Scope:** design/traceability only, appended to the approved *document structure* of PLAN-089/090. Full normative architecture and compatibility/admission matrices are in [master Section 18](.spec.md#18-plan-091--modular-capability-compatibility-fallback-and-trusted-integration-design-only); [Features](.features.md), [RTM](.traceMatrix.md) and [Risk Matrix](.riskMatrix.md) hold their respective indexes. Source snapshot `docs/plan-090-a1-review-findings@77df07df`. No CI workflow, runtime JSON, installed host, repository Git branch, third-party account or production configuration is changed by this *design phase*. User approval for actual implementation and CI activation remains a separate gate.

| Task / phase | Depends on | Scope and deliverable | Evidence / exit |
| --- | --- | --- | --- |
| T091-01 / M0 | exact source/feature inventory | reconcile F01–F42 source states, native/external compatibility, candidate F43–F50 | feature matrix, gap list; DOC_DESIGNED |
| T091-02 / M0 | T091-01 | verify manifest/adapter schema, capability taxonomy, failure/cancellation and host ownership, source versions | reviewed contract schemas and fixtures; A.1 REVIEW_REQUIRED |
| T091-03 / M1 (P0) | T091-02 + A.1 + separate B authorization | fix Path Guard Windows/TOCTOU, scope/phase/CLOSE/fingerprint defects, collision safety and redaction | adversarial Windows/POSIX tests and exact SHA; NOT_AUTHORIZED |
| T091-04 / M2 | T091-03 | implement F43 registry + F44 compatibility preflight, no shell by default | static/negative contract tests AC-MOD-01/02; NOT_AUTHORIZED |
| T091-05 / M2 | T091-04 | F45 fallback/health/drift/circuit breaker and F46 permission/sandbox broker | AC-MOD-03/04/05, independent denial tests; NOT_AUTHORIZED |
| T091-06 / M3 | T091-05 + bounded review spec | F47 scheduler, worker budgets, independent evidence & handoff; local CLI adapters | real worker isolation tests, partial/STOP/recovery; NOT_AUTHORIZED |
| T091-07 / M3/M4 | T091-06 | F48 browser adapter, test assertions, screenshots and runtime traces | E2E positive/negative AC-MOD-06; NOT_AUTHORIZED |
| T091-08 / M4 (P0) | T091-03..06 + CI owner | F49 static CI preflight, quarantine, sandbox staging, GitHub policy and digest-bound owner approval | AC-MOD-07/08/10; external dispatch DISABLED |
| T091-09 / M4 | T091-08 | guarded Jules cloud PR proposal F50 (alpha/version-risk), never auto-merge/deploy | API contract, permission/secret/quotas failure tests AC-MOD-09; NOT_AUTHORIZED |
| T091-10 / M4/M5 | T091-07..09 + real host approvals | adversarial host/OS pilot, A.1/B.1 independent evidence and release decision | signed decision for exact SHA, verified rollback and review; NOT_RUN |

**Ordering constraint:** no M3/M4 worker, browser or CI/CD admission may bypass M1 security fixes or M2 capability-policy broker. Feature-specific fallback is allowed only among **pre-admitted** providers with unchanged mandatory guarantees, never via automatically widened permissions. CI/CD staging uses test credentials and a sandbox/isolated repo; production deployment, write-token, release and auto-merge require separate explicit owner authorization.

**Initial red team / stop conditions:** invalid module digest, spoofed manifest, stale policy, out-of-workspace/junction operations, partial CLI success with exit 0, prompt injection, excessive retries, CI YAML implicit privileges, privileged triggers/untrusted PR, dependency/action substitution, unknown token/secret scope, cloud API/version/quota drift, missing independent evidence. Every abnormality => `QUARANTINED`/`BLOCKED` + provenance-bound handoff. Unsupported runtime/host => no false PASS and no downgrade.

**Design readiness:** F43–F50 PROPOSED; AC-MOD-01..10 DESIGNED/NOT_RUN; A.1 NOT_RUN; B NOT_AUTHORIZED; B.1 NOT_RUN; CI dispatch NOT_ENABLED_BY_S2C. The existing push/PR workflow remains operational outside this new controller, so actual pre-merge enforcement must eventually use GitHub-native branch protection, environment protection and restricted workflow triggers; S2C Markdown alone cannot intercept those events. Preserve user preference for few branches/worktrees and consolidated meaningful commits; no automatic Git push/merge.
~~~~~

### Historical diff: `.agents/.riskMatrix.md` (16 inserted lines)

Original blob `55d9cc9353b96408633aa446e860728730a6237a`; exact insertion order as GitHub compare patch. The following is historical text, not active canonical policy.

~~~~~markdown

## 11. PLAN-091 — External module fallback and CI/CD trust-risk register (design estimates)

**BEFORE:** RM-001..033 and their outstanding safety blockers remain unchanged; the observed `.github/workflows/tests.yml` runs pre-existing tests on push/PR but has no S2C admission policy. **ACTION:** designed capability registry, external adapter contracts, fallback rules and CI/CD owner-controlled admission in [master Section 18](.spec.md#18-plan-091--modular-capability-compatibility-fallback-and-trusted-integration-design-only). **AFTER:** risk mitigation is *specified only*, no provider/CI guard has been run or independently accepted; residual `UNKNOWN/OPEN`. Scores below are tentative L×I design estimates, not incident statistics.

| Risk | Threat and shared cause | L | I | Score | Priority | Required negative check | Actual residual |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| RM-034 | Untrusted plugin/manifest supplies wider filesystem, network or tool authority | 4 | 5 | 20 | P0 | manifest signature/digest/contract + host permission tampering rejected | UNKNOWN/OPEN |
| RM-035 | Fallback silently drops Path Guard, tests, security policies or AC coverage | 4 | 5 | 20 | P0 | candidate mismatch/denial forces BLOCK, never downgrade | UNKNOWN/OPEN |
| RM-036 | CI workflow trigger/token/secret/action enables unauthorized dispatch/deploy | 4 | 5 | 20 | P0 | adversarial YAML/reusable-workflow and GitHub staging, no unauthorized trigger | UNKNOWN/OPEN |
| RM-037 | Third-party prompt/tool injection forges approval or test evidence | 4 | 5 | 20 | P0 | pinned provenance and independent validation, minority blocker preserved | UNKNOWN/OPEN |
| RM-038 | CLI soft-denial/exit 0 or incomplete test incorrectly marked PASS | 4 | 4 | 16 | P0 | denial, partial run, missing postcondition cannot pass | UNKNOWN/OPEN |
| RM-039 | Provider API/platform/version drift or contract mismatch | 3 | 4 | 12 | P1 | exact-version handshake and drift invalidation | UNKNOWN/OPEN |
| RM-040 | Cloud worker receives excessive secrets or Git permissions | 4 | 5 | 20 | P0 | least-privilege PR-only sandbox, secret isolation and rollback | UNKNOWN/OPEN |

Do not merge unrelated RM IDs just because they have equal scores. Group by demonstrated root cause, preserve members and original L/I; prioritize RM-001 and other existing P0 release blockers along with these new P0s. A future A.1 review must refine threat owners, likelihood and testability; B/B.1 must record actual BEFORE/action/AFTER and exact evidence, then only an authorized reviewer may re-rank residual risk. No risk score is reduced by writing this table.
~~~~~

### Historical diff: `.agents/.spec.md` (97 inserted lines)

Original blob `1eecaf1aa815090d2147b4ad11f3138682862fe2`; exact insertion order as GitHub compare patch. The following is historical text, not active canonical policy.

~~~~~markdown

## 18. PLAN-091 — Modular capability compatibility, fallback and trusted integration (DESIGN ONLY)

**Authority and status.** This section extends BR-001/002/003/004/005/006/010/011/012/013/014/015/016/017..021; it does not introduce approved business requirements. New F43..F50, S2C-REQ-043..050 and AC-MOD-01..10 are **PROPOSED**. The authoritative inventory/status is [Features](.features.md), trace is [RTM](.traceMatrix.md), prioritization is [Plans](.plans.md), and estimated risks are [Risk Matrix](.riskMatrix.md). No provider has been admitted, no CI/CD controller has been built, and A.1 remains NOT_RUN / B remains NOT_AUTHORIZED / B.1 remains NOT_RUN. Source snapshot inspected: `docs/plan-090-a1-review-findings` at `77df07dffcc9d8b330799cdc8c2c7f29f042339b`, 2026-11-14.

### 18.1 Modular architecture and non-negotiable boundaries

`Task & SpecKit → Capability Registry → Contract/Policy Negotiator → Permission/Path Guard → Selector → Adapter Runner → Independent Verification Gate → Evidence/RTM/Risk/Handoff`.

- **Core/non-substitutable invariants:** repository physical containment, external-connector authorization, secret protection, task/phase policy, ownership-safe writes, bounded execution, independently reviewed approvals and evidence integrity. The host OS/sandbox must enforce access controls; a prompt-only guard or provider-reported success is insufficient. If the enforcement layer is unavailable or inconclusive, **BLOCK**, not fallback to an unguarded runner.
- **Replaceable modules:** analysis/index generation, context/LLM providers, read-only SpecKit interface, build/test tool implementations, browser automation and transport, *only* after identical mandatory guarantees, exact capability contracts and positive admission checks.
- **Opaque external features:** treat an external adapter or MCP tool as untrusted, even if officially published; only the minimum declared operations may cross the boundary. Integration never automatically grants `shell`, `git push`, filesystem write, network, deployment or credential access.
- **Layered version precedence:** user/host policy and safety invariants > S2C signed module admission and contract > adapter capability/versions > provider defaults. User-approved stack overrides cannot bypass the security/CI gates. SpecKit owns `.specify/` and `specs/`; S2C does not vendor or rewrite upstream by default.
- **Runtime isolation:** execution adapters run within separately constrained workspaces; provider processes must not receive authority to edit S2C policy/verification outputs to self-approve. Non-code/Markdown-only ChatGPT usage may report `UNAVAILABLE` rather than claiming command execution.

### 18.2 Existing-source compatibility matrix (snapshot, not test certification)

| Existing features | Native source or design evidence | Compatibility / integration use | Decision / unresolved gate |
| --- | --- | --- | --- |
| F01–F03 | scanner, architecture tree, context router | native discovery and context capabilities | SOURCE_ONLY; host smoke and drift checks needed |
| F04/F09/F13–F16 | path_guard, scope_io and cross-OS security/CI work | mandatory preflight and guarded filesystem operations | CONDITIONAL; Windows TOCTOU / OneDrive and legacy containment OPEN |
| F05/F06/F17/F24–F26 | session_guard, handoff_store and proposed recovery/migration | durable session binding and handoff; no implicit migration | CONDITIONAL; recovery and ownership/collision checks OPEN |
| F07/F22 | speckit_bridge and prohibition on upstream vendoring | optional read-only upstream SpecKit adapter | READ_ONLY; real SpecKit implement commands remain host-owned and separately authorized |
| F08 | config_loader strict JSON loader | schema-backed registry and policy extension point | SOURCE_ONLY; new schemas not yet written |
| F10/F19 | mcp_boundary authorization library / deferred server | optional per-tool authorization preflight | LIBRARY_ONLY; no authenticated MCP server or transport |
| F11/F12/F20/F21/F23 | governance/layout, dashboard plan, dropped auto-shell and hardcoding | preserving owner/source boundaries and roadmap | MIXED; F21/F23 DROPPED must **not** be revived via fallback |
| F18 | secret redaction / Git hygiene planned | mandatory provider-output redaction | MISSING_RUNTIME; block sensitive integration until enforced |
| F27–F31 | host Policy Resolver, context pointers, Workflow Guard, acceptance | phase/action policy checks and state journal | SOURCE_ONLY/CONDITIONAL; known PR #7 scope/phase/CLOSE gaps remain release blockers |
| F32–F37 | operating docs, RTM and STOP/HANDOFF design | agent governance and resumable workflow contract | DOC_ONLY for runtime STOP/RESUME; no native pause/resume |
| F38–F42 | weighted review, isolation, synthesis and acceptance proposals | potential domain review capability supplier | PROPOSED; no independent multi-agent execution or reviewed worker schema |

Do not collapse feature groups into a falsely uniform state; their individual statuses remain in [Features](.features.md). Presence of a script, historic green test or document is not proof of security compatibility or the ability to execute it in this session.

### 18.3 External candidates / provider compatibility matrix

| Adapter candidate | Required capability | Current external basis | S2C admission | Fallback when unavailable |
| --- | --- | --- | --- | --- |
| Existing native source modules | scan, context, session, read-only SpecKit | repository scripts/config observed | SOURCE_ONLY; runtime/security checks pending | read-only or manual checkpoint, never unsafe write |
| Gemini CLI | model task + structured result | upstream CLI, runtime/version not tested | NOT_ADMITTED | Antigravity CLI/Codex only if same contract and isolation verified |
| Antigravity CLI (`agy`) | headless JSON/NDJSON, timeout, sandbox, scoped permissions | upstream documentation supports primitives; local installed version/auth UNKNOWN | NOT_ADMITTED | Gemini CLI/other verified CLI, else BLOCK |
| Antigravity App/IDE | independent workers, browser interaction/artifacts | product capability claimed externally; no S2C protocol observed | NOT_ADMITTED | sandbox browser adapter or manual UI review, status PARTIAL |
| Codex CLI / Claude Code | model execution, tools, structured reporting | provider-dependent; exact versions/settings UNVERIFIED | NOT_ADMITTED | other admitted adapter without policy downgrade |
| Chrome DevTools MCP / Playwright | browser E2E and console/network evidence | external candidate, no S2C integration | NOT_ADMITTED | headless E2E equivalent if tests cover same AC; otherwise UI_UNVERIFIED |
| GitHub Actions | CI tests, job/check evidence | repository has `.github/workflows/tests.yml` on push/PR | EXISTING_CI; **S2C admission controller MISSING** | local/sandbox verified tests only; do not claim remote CI PASS |
| Google Jules / Jules API | cloud task execution and PR proposal | public API documented as alpha, version/permissions may change | NOT_ADMITTED, HIGH_REVIEW | local admitted runner, else PAUSE with handoff |
| External MCP server / third-party plugin | typed tool/transport | F10 is not a server | NOT_ADMITTED | no-op/read-only if AC permits; otherwise BLOCK |

Provider support must be checked against an **exact installed version and environment**, including Windows/macOS/Linux semantics, authentication, entitlement, network, tool permissions and test commands. Online documentation is a discovery hint, not acceptance evidence. CLI success status is not equivalent to requested action success; inspect denial notices, per-tool outcomes, produced diffs, postconditions and independent tests (not just exit code).

### 18.4 Registry and adapter contract (proposed, version 1)

Each module declaration needs: `module_id`, `provider`, `source_uri`, `publisher_identity`, `artifact_digest`, `schema_version`, `contract_version`, `capability_ids`, `input_schema`, `output_schema`, `supported_platforms`, `supported_versions`, `operations`, `permission_profile`, `required_sandbox`, `required_secrets`, `network_scope`, `timeouts`, `retry_budget`, `concurrency_cap`, `side_effects`, `verification_requirements`, `risk_ids`, `last_admitted_revision` and `admission_status`. Missing security fields are a reject, not permissive defaults. Signatures/checksums validate *integrity*; they do not establish author trust alone.

The adapter `run(task, pinned_contract, scoped_capabilities)` must return a canonical `ExecutionResult`: `task_id`, `session_id`, `provider_run_id`, `module_digest`, `source_sha`, `scope_digest`, `status` (`SUCCESS/PARTIAL/ERROR/DENIED/TIMEOUT/INVALID`), `tool_denials`, `changed_paths`, `artifacts`, `independent_verification_refs`, `cost_usage`, `elapsed_ms` and `next_action`. The controller alone assigns `ACCEPTED` after a separate verification run; adapter returns may never set release/owner approval.

Admitted modules transition `DISCOVERED → STATIC_CHECKED → COMPATIBLE → SANDBOX_TESTED → OWNER_APPROVED → ENABLED`. Any provenance mismatch, permission drift, source change, schema incompatibility, unexpected side effect, missing evidence, timeout, abnormal exit or circuit breaker trip moves the module to `QUARANTINED` / `BLOCKED`. Read-only inspection can continue under its own policy; execution must not. Re-admission requires new evidence for the exact digest/config/environment.

### 18.5 Capability selection, fallback and abnormality response

1. Resolve task's required and optional capability IDs and hard invariants from actual BR/REQ/AC plus affected paths; keep policy inputs pinned.
2. Filter to `ENABLED` providers with contract-version compatibility, required semantics, platform/toolchain support, adequate permissions **within** the caller's approved scope, approved trust level, sandbox and resource budget.
3. Rank eligible providers by exact AC coverage and verified reliability, then cost/latency. Never optimize cost before required security/coverage. No compatible candidate means `BLOCKED_CAPABILITY`; do not broaden access or invent test results.
4. Use **bounded** alternatives only: at most two *different* pre-admitted providers for one capability, each with independent postcondition checks; no retries on authorization/policy violations, source drift, secrets, destructive side effects or ambiguous state. Read-only/manual/report-only fallback is acceptable only when the AC explicitly permits degraded service and the final status is `PARTIAL`, never PASS.
5. Validate source/worktree/head, artifact hash and task scope before and after every provider operation. On abnormality isolate provider, stop dependent DAG nodes, preserve evidence, mark affected RTM/CI claims `STALE/UNVERIFIED`, checkpoint and request a human decision when necessary.
6. Bounded loops/retries/timeouts/cancellation must be enforced by outer process/sandbox; use no unbounded `while true` repair loops. A provider cannot approve its own new permissions or rewrite the independent gate.

### 18.6 CI/CD special admission and release firewall

**Existing fact:** `.github/workflows/tests.yml` runs `unittest` on Linux/Windows for push and pull_request. It is a normal pre-existing GitHub workflow, **not** an S2C-controlled CI/CD admission engine. S2C cannot prevent pre-existing GitHub push-trigger execution solely through an `AGENTS.md` rule; GitHub repository policies/branch protection/environment review and workflow trigger changes require separately authorized enforcement. No workflow is changed or dispatched by PLAN-091.

- `CI_DISCOVER`: inventory exact workflow YAML, trigger events, reusable workflows, script entrypoints, third-party actions/versions, effective token permissions, secrets, environments, artifacts and external network destinations. Pin repository/branch/workflow digests.
- `CI_STATIC_SECURITY`: parse workflow semantics conservatively, deny unknown/dynamic privileged actions, `pull_request_target` + untrusted code, unsafe interpolation/command injection, excessive `GITHUB_TOKEN` or PAT scopes, credential disclosure, unpinned or untrusted action dependencies, unapproved deploy/write triggers and external downloads. Use vendor-native GitHub controls; do not claim a YAML string scan is a sandbox.
- `CI_DRY_RUN`: validate equivalent workflow in an isolated staging repository/runner with test secrets, negative fixtures, read-only defaults, exact command logs and resource caps; verify that denied operations fail closed. A local unit test alone cannot prove GitHub Actions trigger/permission behavior.
- `CI_OWNER_GATE`: named human/repository authority explicitly approves exact workflow digest, repository environment, allowed events, execution scope, secret/environment access and rollback. S2C static/semantic checks are necessary but **not sufficient** approval.
- `CI_ENABLE`: separately authorized workflow enablement / dispatch / PR checks using minimal privileges. Default new third-party workflows/adapters to `DISABLED`. Do not auto-deploy, auto-merge, run self-healing `jules-invoke` on arbitrary issues, or elevate permissions after a failed check.
- `CI_VERIFY`: bind actual run ID/check conclusion/job evidence, source SHA and workflow digest; re-run required non-CI tests independently, then B.1/release signoff. Missing/inconclusive checks, partial provider success, stale SHA or an unauthorized trigger => `BLOCKED`, not PASS.
- `CI_DRIFT/ROLLBACK`: disable S2C-managed dispatch on workflow/provider/policy drift; quarantine adapter, revoke/update scoped credentials through an authorized operator, preserve run evidence, use reviewed rollback. A source PR merely proposing a pipeline stays draft until gates pass.

Cloud workers may propose PRs but must not update protected branches or deploy. Verify Jules/API availability, source authorization, plan, quotas and response schema **at run time**; its alpha API is a version-risk input. Browser E2E screenshots alone cannot certify security, functional behavior or safe deploy.

### 18.7 Acceptance design and open authority

| Proposed AC | Required positive and adverse test | Evidence for future B/B.1 |
| --- | --- | --- |
| AC-MOD-01 | module with valid pinned manifest admitted; unknown fields/digest denied | registry schema test and signed-source review |
| AC-MOD-02 | hot-swappable compatible provider; missing required capability BLOCKS | selector contract tests; AC mapping |
| AC-MOD-03 | fallback succeeds under same scope; unauthorized downgrade denied | provider fixture + before/after permissions |
| AC-MOD-04 | symlink/junction/race/checkout drift cannot escape workspace | OS sandbox tests incl. Windows/OneDrive |
| AC-MOD-05 | timeout, cost cap, denial, partial-success and STOP produce factual handoff | bounded-run logs and state replay |
| AC-MOD-06 | browser equivalent AC tested; screenshot without assertion not PASS | E2E traces, console/network and exact test IDs |
| AC-MOD-07 | unsafe workflow trigger/token/action/secret is quarantined | CI static/adversarial and isolated staging run |
| AC-MOD-08 | workflow drift invalidates approval; no unauthorized dispatch/deploy | workflow digest, audit, GitHub policy evidence |
| AC-MOD-09 | cloud API/quota/schema failure blocks without unsafe fallback | mocked Jules failure/permission tests |
| AC-MOD-10 | no simulated A.1/B.1/release approval and no false check PASS | exact SHA, independent reviewer and human decisions |

Owner, approved contract schema, version pinning, platform/sandbox coverage, trusted CI staging and exact acceptance thresholds remain **UNKNOWN** until separate A.1 decisions. New integration scope is **design-only**; all implementation tasks in [PLAN-091](.plans.md) are NOT_AUTHORIZED pending A.1, explicit B scope and M1 safety blockers. No code, CI/CD, shell or provider is enabled by this document.

~~~~~

### Historical diff: `.agents/.traceMatrix.md` (17 inserted lines)

Original blob `806a83d6a7cdfd88d3b6effb4c85543d51dff575`; exact insertion order as GitHub compare patch. The following is historical text, not active canonical policy.

~~~~~markdown

## K. PLAN-091 — Proposed modularity, fallback and CI trust trace (DRAFT)

This design-only appendix extends existing S2C-REQ-001..042/BR-001..021 without editing the accepted business scope. **No new BR is approved**, and the IDs/AC below require independent A.1/owner review. Canonical behavior is [master Section 18](.spec.md#18-plan-091--modular-capability-compatibility-fallback-and-trusted-integration-design-only), statuses [Features](.features.md), task sequencing [Plans](.plans.md), threat scoring [Risk Matrix](.riskMatrix.md). `NOT_MAPPED` means no runtime source/test exists; it is not an implicit PASS.

| Proposed requirement / feature | Related existing BR | Draft acceptance | Plan | Risk | Code and verification |
| --- | --- | --- | --- | --- | --- |
| S2C-REQ-043 / F43 module registry | BR-001/011/014 | AC-MOD-01 | T091-02/04 | RM-034/037/039 | NOT_MAPPED; NOT_RUN |
| S2C-REQ-044 / F44 contract negotiation | BR-012/013/015 | AC-MOD-02 | T091-02/04 | RM-034/039 | NOT_MAPPED; NOT_RUN |
| S2C-REQ-045 / F45 fail-closed fallback | BR-001/002/011 | AC-MOD-03 | T091-05 | RM-035/038 | NOT_MAPPED; NOT_RUN |
| S2C-REQ-046 / F46 scoped auto-approve | BR-001/002/004 | AC-MOD-04/05 | T091-03/05 | RM-001/034/035 | NOT_MAPPED; NOT_RUN |
| S2C-REQ-047 / F47 bounded execution | BR-003/010/017/018/020 | AC-MOD-05/10 | T091-06 | RM-032/037/038 | NOT_MAPPED; NOT_RUN |
| S2C-REQ-048 / F48 browser validation | BR-004/015/021 | AC-MOD-06 | T091-07 | RM-038 | NOT_MAPPED; NOT_RUN |
| S2C-REQ-049 / F49 CI/CD admission firewall | BR-001/004/015/016 | AC-MOD-07/08/10 | T091-08/10 | RM-036/037/038 | NOT_MAPPED; NOT_RUN |
| S2C-REQ-050 / F50 cloud worker adapter | BR-001/010/015/016 | AC-MOD-09/10 | T091-09/10 | RM-039/040 | NOT_MAPPED; NOT_RUN |

**Reverse trace:** F43..F50 map 1:1 to S2C-REQ-043..050; AC-MOD-01..10 resolve to at least one row above, and all RM-034..040 resolve to one or more rows. These are **planned scenario/AC IDs**, not automated tests or replacements for the 42 PLAN-089 planned TC IDs. Future executable tests must be registered in [Testing & Delivery](.workflow/testingAndDelivery.md) only after approved B scope, preserving original evidence. A.1 NOT_RUN, B NOT_AUTHORIZED, B.1 NOT_RUN; release/CI enablement not approved.
~~~~~

### Historical diff: `AGENTS.md` (8 inserted lines)

Original blob `7e14bd1d048946887f4bc8047dfb652d69852d17`; exact insertion order as GitHub compare patch. The following is historical text, not active canonical policy.

~~~~~markdown

## 15. Modular provider integration and CI/CD admission — PLAN-091

All provider, adapter, MCP and CI/CD changes must first be reconciled with [master Section 18](.agents/.spec.md#18-plan-091--modular-capability-compatibility-fallback-and-trusted-integration-design-only), [feature compatibility registry](.agents/.features.md), [RTM](.agents/.traceMatrix.md), [risk matrix](.agents/.riskMatrix.md) and [sequenced plan](.agents/.plans.md). New F43..F50 and AC-MOD-01..10 are **proposed design**, not automatic runtime permissions or A.1/B.1 approval.

When a requested capability is missing, use only a pre-admitted contract-equivalent provider under the **same or stronger** security policy and scope. If no safe equivalent exists, report `BLOCKED_CAPABILITY` or `PARTIAL` with factual handoff. Never replace Path Guard, secret controls, task scope, user permissions or independent verification with provider assurances, simulation or prompt-level instructions. Execution must have bounded time/cost/retries and quarantine abnormal providers.

CI/CD is particularly restricted: do not create, enable, dispatch, expand permissions for, auto-merge or deploy through third-party pipelines merely because configuration or a provider is present. S2C must preflight exact workflow/dependency SHA, triggers, credentials, token scopes, untrusted input, artifact verification, isolated staging and drift, followed by **independent named owner approval** and a real B.1 gate. Pre-existing push/PR GitHub workflow execution is not controllable merely by instructions. PLAN-091 does **not** change any workflows, external accounts, host runtime or Git branch; retain the planning-only phase and current known blockers.
~~~~~
