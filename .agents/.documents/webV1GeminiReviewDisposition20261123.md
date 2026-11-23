# Web v1.0 — Gemini review disposition and owner approval addendum (23 November 2026)

**Status: AUTHOR_DESIGN_RECONCILIATION / ALL_DECISIONS_PENDING / A1_NOT_RUN / B_NOT_AUTHORIZED.** Current development branch `docs/plan-089-a1-readiness`. Input to this assessment: `d23e981073a8e4419d992b1b0fe4de0ee11730da` (not a frozen A.1 baseline). Gemini's supplied feedback assessed an earlier owner proposal; this addendum incorporates the later AGENTS matrix and 21-case Web test design. **No human owner/independent reviewer was assigned or signed by this document.** Read [owner register](webV1OwnerDecisionRegister.md), [AGENTS matrix](webV1AgentsIntegrationMatrix.md), [PLAN-116](markdownFirstReleasePlan.md), [Web risk overlay](webV1RiskApplicability.md) and [A.1 packet](webV1A1DesignReviewPacket.md).

## 1. Disposition per owner item

| ID | Reviewer observation | Proposed resolution and exact decision requested | Verification / status |
| --- | --- | --- | --- |
| U-01 / DEC-WEB-01 | GitHub connector absence; Spec Kit supported shape unclear | Approve explicit **read-only offline fallback** (bounded uploaded ZIP/Markdown bundle or pasted required files with file list/hash/source metadata; unknown Git SHA stays UNKNOWN) and pinned **Spec Kit v1.4.3 document mapping**. Preserve the V1 exception for agent-executed AGENTS create/adopt/upgrade using only real path-scoped grants; no implicit CLI/runtime. | WEB-TC-01/03/07 and WEB-TC-16..21 design; OWNER_PENDING |
| U-02 / DEC-WEB-02/03 | Hidden source folder, Phase B branch, exact A.1 baseline | Keep `.source/profiles/web/` **developer-only**; distribute an archive with visible root `spec2code-web-v1.0.0/` and allowlisted Markdown. Keep same existing branch for A documents and **propose** Phase B implementation on it after scoped A.1/B authorization, without opening extra branches by default; reviewed integrator may change branch plan if source/policy conflict. Freeze one exact commit only **after** PR #8..11 findings, main unique change and owner BRD source have reconciled and reviewers are assigned; branch HEAD itself is not approval. | No actual build/release/merge; GIT_OWNER_PENDING, A1_BASELINE_NOT_FROZEN |
| U-03 | Six human roles unassigned and solo independent reviewer impossible to self-sign | Permit one named maintainer to serve Product, Architecture, Git/Release and possibly QA/Security where authorized; **independent A.1/B.1 reviewer must not be the artifact author**, must have distinct identity and review the exact source/evidence. Gemini/Codex sequential role lenses do not qualify. If no real independent reviewer is available, retain BLOCKED rather than waive. | Names/handles, role delegation, review scope and signature still missing |
| U-04 / DEC-WEB-04 | 99.99% threshold inherited from runtime; Google BRD is unversioned Draft | Propose **100% of applicable mandatory deterministic Web cases and every critical negative case PASS** with exact evidence, while retaining the inherited unrounded R>99.99% policy wherever an approved *measurable* group/denominator exists. Do **not** silently delete/waive this inherited policy: Product+QA must approve a scoped metric amendment for Web and update the canonical governance/RTM. Google BRD only becomes a normative Web AC source after the owner accepts an exact revision and commits or references a versioned, access-approved immutable snapshot in Git with traceable hash and provenance. | 21 Web cases are DESIGNED/NOT_RUN; QA metric exception and source snapshot OWNER_PENDING |
| U-05 / DEC-WEB-01/04/06 | RM-001 global P0 versus no-applicable-P0 release rule | Classify by **actual execution surface**: (a) Web reading an upload: no local filesystem execution; (b) host AGENTS update via permissioned remote connector: no S2C local Windows Path Guard, but remote auth/blob-ref/ownership/concurrency risk still applies; (c) Codex/other local agent writing Windows files: RM-001 **applicable** and blocked until independent OS isolation evidence; (d) any newly reachable runtime capability: risk reopened. Global RM-001 remains OPEN/P0/20. Security Owner must sign each supported mode and non-applicability proof; no unconditional P0 waiver. | Decision required **before** separate Phase B; no Web or OS security test PASS claimed |
| U-06 / DEC-WEB-06 | Current Gemini review predates AGENTS integration scope change | Approve the declarative 17-clause AGM matrix, three-way merge, version-last, idempotent readback and denied-write fallback; **executor** is the actually authorized AI agent, not an S2C autonomous installer. Confirm whether V1 may use permissioned remote connector writes or only off-host Codex handoff, and exact AGENTS allowlist. | 17 AGM rows and WEB-TC-16..21; OWNER_PENDING |

**Decision semantics:** owner approval of any U item is approval of *design intent only*. An unassigned mandatory review remains BLOCKED. Independent A.1, separate B approval, independent B.1 and release authorization remain four distinct records.

## 2. Proposed scope of Spec Kit v1 document mapping

Public upstream [GitHub Spec Kit release v1.4.3](https://github.com/github/spec-kit/releases/tag/v1.4.3) is the **initial structure reference** (released 19 November 2026). No official Spec Kit CLI, native commands, migration or host install has been tested by S2C here. Product/Spec Owner must approve the exact upstream commit/tag/archive checksum and compatibility support before shipping.

| Host artifact | V1.0 behavior | Condition / fallback |
| --- | --- | --- |
| `.specify/memory/constitution.md` | Read relevant governance, never overwrite | If absent, note UNKNOWN; no invented constitution |
| `.specify/feature.json` | Read active feature pointer only when supplied/trusted; validate path scoped to host | If absent/stale/unsafe, request explicit feature path or STOP |
| `specs/<feature>/spec.md` | Map current BR/FR/AC IDs to source-bound read-only planning | Missing file => BLOCKED for dependent task |
| `specs/<feature>/plan.md` | Map existing implementation plan and dependencies | No duplication of approved plan |
| `specs/<feature>/tasks.md` | Map existing task IDs/status | Never invent observed execution or replace active task ledger |
| `specs/<feature>/checklists/*.md` | Optional read-only validation/support | May be absent; no automatic generated checklist claim |
| `.specify/templates/`, `.specify/scripts/`, agent integration assets | Upstream-owned implementation surface, **out of V1.0 mapping/write scope** | Documentation only; no CLI invocation |

Later Spec Kit versions, alternative structures or customized presets => `UNVERIFIED_COMPATIBILITY` and review of actual artifact paths/schema; never guess support because an upstream version is newer. Native Spec Kit operations remain a later capability. [Upstream quickstart](https://github.com/github/spec-kit/blob/main/docs/quickstart.md) is reference information, not an exact pinned release or evidence of host behavior.

## 3. Offline ChatGPT Web fallback — normative proposal

- With real authorized GitHub read connector: read the expressly scoped repository/ref, capture fetched source SHA, required paths and evidence actually seen. Read permissions do not imply Git writes.
- Without connector but with complete bounded upload: accept ZIP or Markdown files, record archive/file list and checksum when actually known; obtain branch/commit metadata from the user only as **DECLARED_UNVERIFIED** unless independently corroborated. A complete upload can support document/spec/planning work without inventing live Git facts.
- Without complete source: list missing mandatory `AGENTS.md`, BR/AC, Spec Kit artifact or file references; stop only the affected task as `BLOCKED/UNKNOWN` and request the missing bounded files. A pasted file is scoped to its supplied content, not the entire repository.
- ChatGPT Project files and previously uploaded bundles do not auto-refresh from Git; on upgrade re-import/recheck actual active bundle. Neither an upload nor a suggested patch changes host files. AGENTS writes use the distinct permissioned agent path defined in [AGM](webV1AgentsIntegrationMatrix.md).

WEB-TC-03 must exercise **both** complete offline source (safe read/plan) and missing mandatory source (fail closed) as separately observed subvariants under the same test ID.

## 4. Distribution versus development path

Developer source remains `.source/profiles/web/` so git/prototype history and profile ownership are preserved; this path is not a user installation instruction.

Proposed package delivered to users is **`spec2code-web-v1.0.0.zip`** containing a visible top-level `spec2code-web-v1.0.0/` with `BOOTSTRAP.md`, `SKILL.md`, `RELEASE.md`, `CHANGELOG.md`, `references/`, `templates/`, `migrations/` and manifest/checksums, all allowlisted Markdown. Extract in an ordinary visible folder or attach to ChatGPT Project. Only the authorized host AI agent uses hidden host path `.agents/skills/spec-to-code-web/` if a target installation is approved. No package currently exists or has been built/verified.

## 5. Git baseline and branch execution policy

1. Existing stacked draft PRs: #8 `feat/agent-governance-v0.8.0` → `feat/governance-integration-v0.8.0`; #9 `docs/plan-088-unified-s2c` → #8 head; #10 `docs/plan-089-a1-readiness` → #9 head. PR #11 (`docs/plan-090-a1-review-findings` → #10 head) is an **independent draft finding source**, not implicitly an approved fix/merge.
2. `main` differs from the development chain; review its unique commit and intended final integration target. Do not erase/rewrite shared history, auto-merge stacked drafts, infer PR #11 approval or create new branches for one-line changes.
3. Continue A author documents on `docs/plan-089-a1-readiness` until scope/owner/requirements/risk and PR finding reconciliation. After an approved reviewer-ready snapshot, record `A1_REVIEW_BASELINE_SHA` and source snapshot/Google revision in one signed decision record. This baseline is **NOT_YET_FROZEN**; `d23e981073a8e4419d992b1b0fe4de0ee11730da` was simply a prior observed author HEAD.
4. If A.1 passes and Product+Host authorize B, **default proposal** is reuse the existing development branch for V1 implementation with separate B-scoped commits rather than create a new branch; frozen A.1 evidence must remain referenced to its immutable SHA. Any material design change after freeze triggers A/A.1 rerun. Git integrator may require a reviewed branch/base change as an explicit decision, never a silent rebase.
5. Do not merge to `main`, tag or release merely because A.1 passes. Reconcile reviewed PR stack and main's unique change as a separately authorized release-integration step; B.1/release evidence must bind exact final candidate SHA. If integration changes scope/requirements, revalidate the affected gates.

## 6. Solo-owner role assignment (proposal, not signature)

| Role | Who may cover it | Current decision |
| --- | --- | --- |
| Product Owner / Architecture Owner | Named repository maintainer or delegated decision-maker | UNASSIGNED |
| Git/Release Owner | Named authorized integrator with actual target permissions | UNASSIGNED |
| Security/Host Owner | Named host/security decision-maker; may be the solo owner only if role and scope are explicit | UNASSIGNED |
| QA Owner | Named person accountable for measured AC/test method and evidence | UNASSIGNED |
| Independent A.1/B.1 Reviewer | **Actual distinct reviewer not authoring the exact artifact**; may be outside collaborator with separate Git identity and evidence access | UNASSIGNED — HARD BLOCKER |
| AI/Gemini/Codex | Can draft matrices, review and test when genuinely available; **cannot sign independent human acceptance** | TECHNICAL_ASSISTANCE_ONLY |

Minimum approval record for each owner: identity/handle, role/authority, decision date, exact `A1_REVIEW_BASELINE_SHA` or release SHA, reviewed paths/risks, explicit ACCEPT/REVISE/REJECT, supporting evidence and dissent. If independent reviewer unavailable, do not redefine same-model review as independence; release process remains blocked.

## 7. Security Owner decision matrix for RM-001

| V1 usage mode | Windows local Path Guard / race applicability | Other controls still applicable | Decision |
| --- | --- | --- | --- |
| GPT Web with only uploaded/pasted documents | Local RM-001 attack path **not exercised** by Web itself | Prompt injection, secrets/privacy, provenance and false authority | PROPOSED_NOT_APPLICABLE_TO_WEB_LOCAL_WRITE / OWNER_PENDING |
| GPT Web with approved **remote** GitHub AGENTS file write | S2C Windows local IO is **not invoked if no delegated local process**; proof of execution boundary required | GitHub permissions, expected blob SHA, path ownership, one writer, conflict, secret handling | PROPOSED_SCOPE_EXCLUSION / OWNER_PENDING |
| Codex/other agent writing files on Windows host | **RM-001 APPLIES** if local untrusted/safety-relevant filesystem mutations are in scope | OS-enforced isolation, junction/race/alias controls, synthetic canary and independent audit | BLOCKED_PENDING_HOST_EVIDENCE |
| Local agent on other OS or arbitrary provider | Host-specific filesystem/permission exposure **requires separate threat analysis** | Host policy, sandbox boundary, path symlink/mount and unowned writes | UNKNOWN / OWNER_PENDING |

Global RM-001 remains **P0 L4×I5=20 OPEN / RESIDUAL UNKNOWN**, including for future runtime. **Never write `RM-001 CLOSED` or downgrade its global score merely because a remote-only V1 profile excludes the local attack path.** Web-specific release eligibility requires explicit Security Owner acceptance of tested non-applicability per supported provider/mode and treatment of every other applicable P0. Missing proof means blocker.

## 8. V1 quality metric and release acceptance proposal

- Deterministic acceptance: **all applicable mandatory Web acceptance cases must PASS**, all applicable mandatory security-negative tests PASS with evidence; do not count BLOCKED/NOT_RUN/INCONCLUSIVE as success. Currently **21 cases designed; 0 executed**. Additional representative fixtures may be required for variants and host/provider coverage.
- The inherited `R >99.99%` threshold is **not automatically deleted or waived** by this review. For nonstatistical Markdown planning/AGENTS compatibility checks, Product+QA must approve a separately recorded scope-specific metric/denominator or explicit policy amendment in the canonical governance and RTM before declaring acceptance. In any approved statistically measurable group, retain the exact required threshold and sample method; 21 case labels alone cannot prove a reliability percentage.
- Google BRD mirror is DRAFT until Product Owner approves its exact revision and an authorized, versioned immutable snapshot/reference (with source URL, tab/revision, content fingerprint, approval, mapping and redaction/permission) is bound to a Git commit. Copying a link alone is not semantic parity; changed Google text after approval creates a new candidate and invalidates impacted evidence.

## 9. Must-answer owner questions before independent A.1 and Phase B

- **U-02:** approve visible release archive and same-branch-by-default B strategy; select integrator and final branch/integration method after PR review.
- **U-03:** designate named Product, Architecture, Security/Host, QA, Git/Release and a **real independent A.1/B.1 reviewer** (or leave gates BLOCKED).
- **U-04:** choose actual Web quality KPI and approved treatment of the existing R>99.99% rule; approve BRD source snapshot/AC and test groups.
- **U-05:** sign each supported mode's RM-001 applicability and all applicable P0 decisions, especially local host writes.
- **U-06:** approve which external AI agents and connector/host paths may create/adopt/upgrade AGENTS; whether bounded standing scope covers a whole batch or requires per-diff confirmation.

**No independent A.1 or B.1 is performed by this document.** Do not infer Phase B authorization from these recommendations. Next safe task: owner review and PR/source reconciliation, then freeze one exact A.1 candidate and arrange an actual external independent review.
