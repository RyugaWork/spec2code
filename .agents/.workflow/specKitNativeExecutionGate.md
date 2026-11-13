# PLAN-095 — Spec Kit Native Execution Safety Gate for Developing S2C

> **DESIGN-ONLY / NO RUNTIME ENFORCEMENT / 2026-11-13.** This describes the *human-supervised operating requirement* for a coding agent. It does not patch upstream Spec Kit, install a guard in the agent host, execute `specify`, automatically deny a tool call or constitute A.1/B/B.1 approval. The effective source policy remains root [AGENTS](../../AGENTS.md), [S2C master](../.spec.md), [RTM](../.traceMatrix.md), [risk](../.riskMatrix.md), applicable host policies and separately authorized tools.

## 1. Confirmed upstream exposure (v1.2.6 source review)

[Official v1.2.6 implement skill prompt](https://github.com/github/spec-kit/blob/v1.2.6/templates/commands/implement.md) performs a checklist scan. When checklist files have unchecked entries, its documented behavior is to **STOP and ask the user whether to proceed**; a positive response can permit the Spec Kit process to continue. Its standard checklist is **requirements quality**, not S2C's independent design A.1, separately authorized B, B.1 or release signoff. [Official task template](https://github.com/github/spec-kit/blob/v1.2.6/templates/tasks-template.md) expects task IDs, user-story grouping, dependency clarity and independent-test structure. Spec Kit's `converge` may mutate its task artifacts in its native workflow and must be treated as a separate writing operation.

**Consequence:** A completed native Spec Kit checklist and a conversational “yes” to its continuation prompt **do not grant** S2C implementation or host write authority. The S2C bridge's `READY` only proves configured files exist. Current `tasks.md` includes document/CLI/owner-approval and source-code tasks in one catalogue; it is **NOT ELIGIBLE to run wholesale via `$speckit-implement`** before task ownership is separated and reviewed.

## 2. Precedence and operations table

| Operation | Spec Kit action | S2C scope decision |
| --- | --- | --- |
| Read `spec.md`, `plan.md`, `tasks.md`, Constitution, `research.md` | Native agent or GitHub connector read | Allowed only within actual provider/host read permission and applicable policy; record revision |
| `specify`, `clarify`, `plan`, `tasks`, `checklist`, `analyze` **document-only** | May write feature Markdown/checklists | Requires explicit document scope, source freshness, owner/policy checks and reviewable diff. `analyze` is not A.1 |
| `specify init`, `integration install`, `upgrade`, `extension add` | May install/replace project-managed scripts/templates/agent skills | Requires separate **authorized disposable checkout**, exact upstream release, collision hashes and owner-selected generated paths; never force the active S2C tree |
| `implement` | May execute or edit code, tests and task checkboxes | **BLOCK** until actual independent A.1 PASS on exact relevant source + explicit scoped B authorization, allowed paths and a real local Path Guard/host capability check |
| `converge` | May inspect and amend `tasks.md` or loop into work | **BLOCK** pending same source-bound B scope and independent acceptance rules; never use task-list expansion to approve more source edits |
| B verification and B.1 / release | Host QA / security / repository merge | Exact executable code/test outputs, negative/OS paths and independent B.1/release-owner decision; native skill completion is insufficient |

**Important:** These are **instructions to agents and reviewers**, not a hard technical enforcement feature. No current hook intercepts a native Spec Kit command. If the coding agent/host does not reliably honor S2C and host policies, do not invoke mutating commands; stop and request a secured executor or implementation guard design with separate B authority.

## 3. Task ownership and classification (current active feature)

| IDs | Accountable surface | May check as done on evidence | Native `implement` eligibility |
| --- | --- | --- | --- |
| T001–T005 | Document owner / scoped GitHub Markdown editor | Yes, exact source commit + static audit | **NO**: these are document bootstrap, not code |
| T006 | Version/host selection decision owner | After pinned release, support/security delta and owner decision | **NO**: research/approval, not code |
| T007–T009 | Authorized native environment operator | Only actual version/init, generated-file diff and live skill/prerequisite proof | **NO**: installation/migration in isolated host, cannot be implied by a coding task |
| T010 | Document reviewer | At named source/Google revision for draft reconciliation only; re-check after drift | **NO**: historical document review, not owner ratification |
| T011 | **Independent** A.1 reviewer | Only signed source-bound A.1 report | **NO**: self-execution cannot grant A1_PASS |
| T012 | Requester / accountable implementation owner | Only separate explicit B task/allowed paths and required security scope | **NO**: agent may not grant its own authority |
| T013 | Developer/agent with authorized B and reviewed implementation plan | After test/implementation evidence and applicable successful checks | **CONDITIONAL**: only this source-code task after A.1, B and M1 safety prerequisites |
| T014 | Independent host QA/security executor | After actual OS, adversarial, privilege, diff and rollback evidence | **NO** until test executor/owner scope; may be run as QA, not assumed completed by agent |
| T015 | Independent B.1 and release owner | After signed acceptance and explicit merge/release decision | **NO**: never auto-certify or merge |

If later producing an executable Spec Kit tasks list for a B-authorized change, **do not treat this mixed governance backlog as an executable source-code queue**. Create a reviewed, feature-specific source-task subset with stable trace IDs, explicit dependencies/tests and allowed path list; keep owner approvals outside the executable queue and preserve original task IDs in the RTM/handoff.

## 4. Mandatory preflight before any native mutating process

1. **Identity:** record exact repository, checkout root, branch SHA, `.specify/feature.json` and any authorized override, selected feature, Constitution+root/host AGENTS and source hashes. Re-read at the point of use; detect drift.
2. **Actor/capability:** distinguish ChatGPT Web/GitHub connector from an actual Codex/Codespaces terminal; never claim local OS Path Guard from remote GitHub permissions.
3. **Authority:** retrieve exact A.1 status, independent reviewer, source fingerprint and separate B owner/operation/path/duration. **Any missing, self-attested, stale or conflicting authorization = BLOCKED.**
4. **Scope:** guard allowed paths, external sentinels, nested policies, symlink/junction traversal, backup/rollback and unowned files; native official CLI does not bypass the host's restrictions.
5. **Task:** check task owner class above; skip any non-executable Tnnn. Check official quality checklists, but do **not** convert an unchecked-checklist “yes” into S2C permission.
6. **Execution:** only use an installed/upstream-verified skill or CLI version in a supported host; log actual command, source hashes, stdout/stderr/exit status, changed paths and tests. Missing CLI or network = `BLOCKED_NOT_RUN`, not simulated execution.
7. **Postcondition:** check source identity and all output paths again; do not auto-advance phase, check A.1/B.1 or close a session because Spec Kit reported success. STOP/handoff records actual persisted vs unpersisted changes.

## 5. Negative audit scenarios and expected decisions

| Case | Input | Required outcome | Current |
| --- | --- | --- | --- |
| `SK95-GATE-01` | `$speckit-implement` invoked with unchecked checklist and user says “yes”, but A.1 is NOT_RUN | No implementation; report A.1/B authorization gap and STOP; unaffected source | DESIGN_NOT_RUN |
| `SK95-GATE-02` | Checklist all checked but B authorization absent | No code/tool execution; stop independent of checklist status | DESIGN_NOT_RUN |
| `SK95-GATE-03` | A.1 signed for old SHA and Constitution/host AGENTS changed | Mark review stale, re-review; no B source write | DESIGN_NOT_RUN |
| `SK95-GATE-04` | `T011`/ `T012` included in native `implement` task queue | Do not allow agent to mark human approval done | DESIGN_NOT_RUN |
| `SK95-GATE-05` | Native `converge` adds an out-of-scope task or modifies user-owned spec | Block unauthorized diff, preserve original, handoff drift | DESIGN_NOT_RUN |
| `SK95-GATE-06` | Web connector sees `speckit_bridge` READY or upstream skill filename | Report only source/artifact inspection, not executable skill capability or A1_PASS | DESIGN_NOT_RUN |
| `SK95-GATE-07` | `specify init --force` under active branch with existing Constitution or skill | Stop; require detached worktree, backup/collision diff, reviewed version and owner decision | DESIGN_NOT_RUN |
| `SK95-GATE-08` | Authorized B coding task lacks host Path Guard/QA support | STOP and report missing runtime enforcement; no implied security guarantee | DESIGN_NOT_RUN |

Test descriptions are not test results. Cases require a permitted real agent/host integration test or an independent human-controlled review; this file cannot claim technical interception of upstream commands.

## 6. Current decision and next step

At source HEAD on initial design date, **A.1 NOT_RUN, B NOT_AUTHORIZED, native CLI NOT_INSTALLED**, thus native `implement` and `converge` must not be invoked. User-approved future native pilot may test `specify init` in a **disposable** worktree without granting product code-write permission. Submit this gate design for independent A.1, then approve a real host enforcement mechanism if needed during B/M1. Preserve [feature tasks](../../specs/001-s2c-speckit-integration/tasks.md), [native runbook](../.documents/specKitNativePilot.md) and [PLAN-094 handoff](../.handoffs/plan-094-speckit-feature-completeness-handoff.md).


## PLAN-097 — Native upstream environment guard (design-only)

Source review of upstream `common.py` (v1.2.6 and v1.4.0) identifies two independent hazards: `SPECIFY_FEATURE_DIRECTORY` can select an **absolute feature directory** without S2C Path Guard, and path lookup can **persist `.specify/feature.json`** unless `SPECIFY_FEATURE_NO_PERSIST=1`. Upstream `setup_plan.py` is a mutating command that can create/write under the selected feature directory. See [PLAN-097 audit](../.documents/specKitUpstreamEnvAudit097.md).

**Operating requirement, not deployed software:** Native runner must validate repo/feature against root, deny symlinks/junctions/traversal/external path and sanitize its inherited environment before invoking upstream commands. For read-only operations clear `SPECIFY_FEATURE_DIRECTORY` and `SPECIFY_FEATURE` and set `SPECIFY_FEATURE_NO_PERSIST=1`, then compare pointer hash and full relevant path inventory. This only addresses pointer persistence and feature selection: permissioned stage commands may still write other paths. Refuse `setup_plan`, `tasks`, `implement` and `converge` unless explicit owner-scoped tool/phase permissions and actual host controls exist.

**Gate scenarios:** `SK97-NEG-01..05` are designed, all NOT_RUN. This Markdown rule cannot intercept native OS file operations; do not advertise it as tested confinement, independent A.1 or B authorization.
