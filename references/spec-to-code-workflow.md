# Extended Spec-to-Code Methodology (reference only)

Read only when full spec normalization / task breakdown / implementation gates are required. Follow v0.3 `SKILL.md` for session attribution and scanning.

## Required inputs and outputs

**Inputs:** Owner's request; approved requirement identifiers/source documents; relevant repository state; affected stack; existing API/data contracts and tests. Optional: scope, acceptance criteria, priority, nonfunctional targets.

**Outputs:** Current observed infrastructure index and delta log; requirement/decision ledger; implementation plan; dependency-ordered tasks; traceability map; authorized source changes; verification evidence; completion report/handoff. Use the templates in `references/` as needed, not as a requirement to generate paperwork for trivial tasks.

**Default working status:** `DRAFT` until an owner-approved business baseline and actionable acceptance criteria have been confirmed. A technical plan does not constitute business approval.

## Mandatory repository instructions

1. Use root `/AGENTS.md` (repository root); if Codex already supplied it in the active context, **do not re-fetch/re-paste the whole file**. For Git/GitHub work read `.agents/.git.workflow.md`. Remote GitHub access requires a **fresh explicit choice of connected account for each task**, even read-only checks. Do not commit, push, create branches, merge, rebase, or rewrite history without the corresponding owner authorization.
2. Check `.agents/.documents/.businessRequirements.md` for canonical Gymuro business rules and approved actors/permissions. Read `.agents/.documents/.documentGovernance.md` before creating or changing controlled specifications or their versions.
3. Read only applicable technical policies: `.agents/.documents/.apiRequirements.md`, `.backendArchitecture.md`, `.databaseRequirements.md`, `.securityRequirements.md`, `.frontendArchitecture.md`, `.mediaStorage.md`, `.testingAndDelivery.md`, `.envSummery.md` (when environment variables are relevant).
4. Confirm what is actually present using the incremental scanner and short index, followed by only task-relevant files: `AGENTS.md`, app entry points, local Git changes, existing contracts/tests. **Do not infer implementation from `.gitkeep` placeholders, README examples, or proposed file paths.** Preserve unrelated changes.
5. Source code belongs under `.source/`: ASP.NET Core backend in `.source/backend/`, React/TypeScript web in `.source/web/`. Cross-stack suites remain under root `tests/`. No root `backend/` source tree.
6. The skill's analysis/plan/task documents are **derivative working artifacts**. They must never override business rules, API contracts, approved security policies, or the owner's instructions.

## Workflow and gates

### Gate 0 — Resolve scope and provenance

- Identify requested feature, module, actors, UI/API entry points, affected data and integrations. Assign a feature key (use existing project ID if present; otherwise a clear temporary slug).
- Collect exact authoritative requirement IDs and links/paths; mark each statement `VERIFIED`, `INFERRED`, `PROPOSED`, or `UNKNOWN`.
- Run the infrastructure scanner first; consult the compact index/delta and then inspect only in-scope code/local Git changes before any edit. For remote access follow GitHub account-selection policy first.
- Determine whether this request authorizes **planning only**, **implementation**, **new tests**, or **commit/push**. Never infer permission for repository writes from a request to review or plan.
- If input lacks an approved business rule, create a clearly marked **draft specification** and a concise decision log; do not treat it as approved and do not implement the affected business behavior.

**Gate 0 PASS:** Specific, bounded feature scope and authoritative references exist. Otherwise `BLOCKED` for impacted behavior; unaffected analysis may proceed.

### Gate 1 — Spec normalization

Use `references/feature-spec-template.md` when a full artifact is useful.

- Derive actors, role/permission checks, business preconditions, normal/alternative/error flows, state transitions, edge cases, constraints, and out-of-scope behavior.
- Write testable acceptance criteria using `Given / When / Then` (or equivalent), not merely descriptions of buttons or implementation choices.
- Include data ownership and classification (personal, medical, identity, public), retention, audit needs, timezone/locale requirements, and missing decisions where relevant.
- Identify API inputs/outputs, pagination/filter/sort, authorization scope and error behavior **only from authoritative contracts**; flag proposals explicitly.
- Establish stable trace IDs, e.g. `FEAT-XXX-R01` / `FEAT-XXX-AC01`. Reuse existing formal requirement IDs whenever supplied.
- Record contradictions in `Open Decisions`; never silently arbitrate between documents, code, and requirements.

**Gate 1 PASS:** Every requested behavior maps to an approved requirement plus observable acceptance criteria. Otherwise affected implementation remains `BLOCKED`.

### Gate 2 — Design and impact analysis

Use `references/implementation-plan-template.md` when appropriate.

- Use `infrastructure-index.md` to locate existing projects/entrypoints; inspect only relevant implementation, interfaces, migrations, components and tests. Mark absent projects as **not implemented**. If the scanner detects an architecture change, revisit affected assumptions before designing.
- Propose a minimal design that respects API → Business → Repository/DataAccess and Infrastructure adapter boundaries; reuse existing types and contracts when correct.
- For new/changed endpoints detail authentication scheme, authentication → role → permission → current business eligibility/ownership, input validation, server-side filtering, errors, concurrency, and backward compatibility.
- For DB changes define schema evolution, EF Core migration/backfill/rollback considerations, query indices, transaction boundaries, authorization-scoped queries and safe parameter binding; dynamic SQL identifiers must come from a server-owned allowlist.
- For React Web use Identity **cookie** auth, HTTPS/HttpOnly/Secure cookies, CSRF for mutations, secure cache/deduplication, invalidation, loading/error states, accessibility and locale/timezone conventions. Do not store web auth tokens in localStorage. Reserve standard JWT Bearer for separately approved non-Web clients.
- For customer protected data, follow approved classification, authenticated encryption/key-custody policy and least-privilege logging. Do not invent KMS settings or access secrets.
- Optimize query count/indexes before parallel database fan-out. Use `async/await` and cancellation. Never share EF Core `DbContext` across concurrent operations. Parallel independent reads only with separate contexts and bounded concurrency justified by evidence.
- Record API/UI/database/operations/testing impacts, risks, alternatives, dependencies, and release/rollback conditions.

**Gate 2 PASS:** Design is consistent with current repo and approved policies; there is no unresolved high-risk API, data-loss, auth, or business decision.

### Gate 3 — Task decomposition and review

Use `references/tasks-template.md` and `references/traceability-template.md`.

- Order work by dependencies: preconditions → contract/schema → backend business/data → API → frontend → integration/verification → documentation/handoff.
- Each task has an ID, requirements/acceptance IDs, file boundaries, expected observable outcome, prerequisites, validation command, and status.
- Identify separate **feature-source** and **test-source** phases. Do not combine newly authored feature and test source into a single commit; conventional commit subjects are required when committing, but commits require explicit permission.
- Favor incremental vertical slices and smallest changes; don't generate empty stubs merely to make the plan appear complete.
- Highlight approvals and blockers before coding.

**Gate 3 PASS:** Every planned change traces to scope, with an implementation order and checkable completion condition.

### Gate 4 — Controlled implementation

Only when explicitly authorized for implementation and Gates 0–3 pass:

1. Recheck relevant files and diff to avoid overwriting other work.
2. Implement one bounded task/vertical slice at a time. Keep security, error handling, validation, cancellation, and logging consistent with approved patterns.
3. If source edits change architecture/configuration, run session_guard.py checkpoint and record authored edits in `.handoffs/.details/.specChange.{SessionID}.md` before final reporting. Apply data access authorization **before** materialization/pagination; parameterize SQL; never concatenate user-controlled text into query syntax. Use the same per-request authorization checks even with cache/session.
4. Use typed API contracts and validated input, stable error behavior, migration safety, and privacy-preserving logs. Do not assume README or `.gitkeep` scaffolding means runtime code exists.
5. Update traceability as files change. If an unexpected requirement or architectural conflict appears, mark only affected scope `BLOCKED` and report; do not silently enlarge the feature.
6. Do not touch `.env` or credentials; never create committed environment/secret files contrary to repo policies.

### Gate 5 — Verification and release readiness

- Read `.agents/.documents/.testingAndDelivery.md` and follow repository-approved test structure. Author **new test code only when explicitly in scope**, in its separate work phase.
- Run only existing, applicable commands and projects discovered in the repo, e.g., `dotnet build`/`dotnet test` for existing `.sln`/`.csproj`, frontend package manager's defined lint/typecheck/build/test scripts, and approved API/E2E scripts. **Do not claim a test passed without execution.**
- Check acceptance-criteria traceability; positive, negative, boundary, authorization/ownership, cookie/CSRF, SQL injection, concurrent writes/reads, error handling, data encryption, and cache isolation according to impacted scope.
- Confirm migrations, data safety, backwards compatibility, and release/rollback requirements where applicable.
- For each gate use `PASS`, `FAIL`, `BLOCKED`, or `NOT RUN`; include command, result, environment and actual evidence or reason.
- Do not claim build, test, deployment, security certification, or performance improvement solely from a code review.

**Final gate PASS:** Approved behavior is implemented, any infrastructure/config delta is reflected in `infrastructure.json` / `.handoffs/.details/.specChange.{SessionID}.md` (for authored changes), and every in-scope criterion has verifiable evidence. Otherwise clearly state partial completion and blockers.

## Artifact and reporting rules

- Place controlled feature artifacts only where `.agents/.documents/.documentGovernance.md` allows. If no authorized feature-artifact location exists, propose a location for owner approval; do not invent a new official directory standard.
- Keep specs/plans/tasks/traceability readable and linked. Use `references/feature-spec-template.md`, `references/implementation-plan-template.md`, `references/tasks-template.md`, `references/traceability-template.md`, and `references/handoff-template.md` on substantial work.
- Use `references/quality-gates.md` as a final checklist. Confirm `record` for all self-authored paths and a successful `finish`; external changes must not be entered in `.handoffs/.details/.specChange.{SessionID}.md`. Report risk and explicit `NOT RUN` statuses.
- Do not silently update canonical business requirements, API contracts, documentation versions, Git branches, or repository policies.
- Report: feature and approved requirement IDs; modified files; implemented behavior; tests run and results; verification gaps; security/compatibility notes; next blocked decisions; Git actions actually authorized/performed, with commit SHA only when a commit exists.

## Minimal retrieval decision tree

1. `session_guard.py start` reports `NO_CHANGE`: read the short index only if the current task needs architectural context; open only exact requirement and implementation files in task scope.
2. Reports `OUT_OF_SESSION_CHANGE`: inspect the latest relevant `.handoffs/.details/.visualChange.{SessionID}.md` event (external drift only), then read changed paths relevant to the task. If changes are internal to the active session, use `.handoffs/.details/.specChange.{SessionID}.md` instead.
3. Reports `BASELINE`: read index as a **first observed snapshot**, inspect only requested module and authoritative spec; do not attempt a whole-repo content review.
4. Reports `SESSION_FAILED`: report current topology unverified and stop any design requiring accurate infrastructure state until the blocker is resolved; no fabricated snapshot.
5. On unexpected architecture drift during coding, run `session_guard.py checkpoint`, compare with requirements, then either adjust a bounded plan or mark the affected scope `BLOCKED` (do not silently extend work).

## Invocation examples

- `$spec-to-code Implement approved membership renewal requirements from .agents/.documents/.businessRequirements.md; run an incremental infrastructure scan, inspect only relevant changes and dependencies, then implement.`
- `$spec-to-code Turn feature ABC-12 into backend API plus web UI with requirement-to-file traceability; do not commit or push.`
- `$spec-to-code Review this draft feature spec for missing approval and produce a plan only.`

## Non-goals

This skill is not a full autonomous product owner, specification approval system, code generator that ignores the repository, GitHub Spec Kit wrapper, commit authorization, or substitute for executing tests.
