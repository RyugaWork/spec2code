# PLAN-092 — S2C self-development Spec Kit integration handoff

> **Captured:** 2026-11-13 (Asia/Ho_Chi_Minh). This is a GitHub connector document change, not a local S2C session or native Spec Kit process. Repository `RyugaWork/spec2code`, working branch `docs/plan-089-a1-readiness` (PR #10, Draft, base `docs/plan-088-unified-s2c`). No new branch and no merge.
>
> **Git source snapshot before creation of this file:** `5ab1c13ebbcf56140d03be340535200326bab737`; creating this handoff advances Git HEAD, so refresh exact HEAD before reviewer signoff. **Google stakeholder BRD:** `https://docs.google.com/document/d/1M3_2tNUxOXci83pcpPCzBkxwvRvixeT7FYeGyIsFOa4/edit?tab=t.0`, tab `t.0`, Draft v1.5, revision `AHj4eMRV4ZE9_EiaZyARP1h_ZKw3XsY51u_kGXnV6wJ-J3z7FlnjtRXLioVZfusHKtO0_E-wdwVT_2pvChfnxiCpILdnt3vNG94QqHUAiQ` (Section 25 PLAN-092). Do not use version labels alone to establish source identity.
>
> **Status:** `WEB_MARKDOWN_BOOTSTRAP_VERIFIED`; `NATIVE_SPECKIT_CLI_NOT_INSTALLED/NOT_RUN`; `A1_NOT_RUN`; `B_NOT_AUTHORIZED`; `B1_NOT_RUN`. This handoff is **NOT** a signoff, approved Constitution or runtime test result.

## 1. Scope and committed artifacts

| Artifact | Role | Evidence status |
| --- | --- | --- |
| `.specify/memory/constitution.md` | Draft principles for developing S2C through official Spec Kit; AGENTS and S2C master retain authority | CREATED; NOT_RATIFIED |
| `.specify/feature.json` | Official-style `feature_directory=specs/001-s2c-speckit-integration`; no Git feature branch required | VALID_JSON/CONTAINED in Git static review |
| `specs/001-s2c-speckit-integration/spec.md` | Feature-level problem, four user stories, SKI-FR-001..012, negative/ownership cases | DRAFT |
| `specs/001-s2c-speckit-integration/plan.md` | Two-mode architecture, stage gates, collision/recovery and alternative implementation actions | DRAFT |
| `specs/001-s2c-speckit-integration/tasks.md` | 15 planned tasks T001..T015; T001..T005 marked done **for Markdown bootstrap only** | 5 DOC tasks DONE; 10 CLI/approval/code tasks OPEN |
| `specs/001-s2c-speckit-integration/checklists/requirements.md` | Design quality and authority checklist | DRAFT/NOT_SIGNED |
| `.specify/README.md` and `.source/integrations/speckit/README.md` | Web/GitHub vs native Codex/Codespaces workflow and official setup constraints | DOCUMENTED |
| `AGENTS.md`, `.agents/.spec.md`, `.agents/.traceMatrix.md`, `.agents/.plans.md`, `.agents/.riskMatrix.md`, `.agents/.features.md`, root README and related governance header refs | Integrate feature requirements with S2C risk/trace, phase separation and Draft v1.5 | DOCUMENTED, OWNER_REVIEW_PENDING |

No `.source/scripts/*.py`, `.source/.config/*.json`, GitHub Actions, host AGENTS, Git merge or remote deployment modified. Upstream official scripts/templates/coding-agent skills were **not copied** into this repository.

## 2. Actual static inspection and limitations

- Git tree/source check at SHA `ebdbd03f027a8e65ce5cde8ddc5ea0af5a1cad14`: all expected feature artifacts exist, feature JSON points inside repository, 15 task IDs were distinct and matched the `Tnnn` pattern, 171 relevant internal Markdown links resolved in the tree.
- Subsequent read-only spot check at SHA `5ab1c13ebbcf56140d03be340535200326bab737`: 17 native artifact Markdown links resolved; feature declares 12 unique `SKI-FR` rows; T001..T005 marked completed (document/bootstrap tasks), T006..T015 not completed.
- The existing `.source/scripts/speckit_bridge.py` and `.source/.config/speckit.json` were inspected: the bridge uses `.specify/feature.json`, checks `spec.md`, `plan.md`, `tasks.md` and computes bounded metadata/task IDs. **The Python command was NOT run in an actual S2C checkout**, so readiness is a source/static expectation, not an observed CLI output.
- Native integration files from `specify init` under `.specify/scripts` and `.agents/skills/speckit-*/SKILL.md` are absent, as expected for Web-first bootstrap. The latest official release discovered was `v1.4.0` dated 2026-11-10, too newly released to adopt automatically under conservative S2C policy; **no CLI release has been approved or installed**.
- Google BRD v1.5 was read back and Section 25 plus headings were present; it is a stakeholder review surface, not independent signoff.

## 3. Blockers and next permitted actions

1. **Native installation** T006–T009: choose a supported mature official release, agent key (e.g. Codex/Copilot), approved disposable host and conflict policy; create backup and inspect generated diff. Only then run actual `specify init --here --force --non-interactive --integration <key> --script py`, capture `specify version`, scripts/skills existence, pointer and stage test evidence. Prefer not to use Git extension; no extra branches requested.
2. **Authority** T010–T012: confirm BR owner, draft Constitution ratification, selected host/review policy and specific version/OS support; obtain independent A.1 report and separate B implementation authorization. The bootstrap does not resolve existing RM-001..005 critical risks.
3. **Implementation/validation** T013–T015: if a real bridge or runtime change is required, perform only under B authorization with exact-SHA regression, host security, Windows/OneDrive/junction and negative tests; B.1 independent host validation and release decision remain separate.
4. **Resumption:** re-fetch latest Git HEAD and Google revision, read selected `.specify/feature.json`, AGENTS/Constitution, current RTM/risk and first unchecked task. STOP/handoff may remain in Markdown without calling runtime Workflow Guard `close`.

## 4. Risks and recovery

Known candidates SK-R01..06 include force-overwrite collisions, wrong feature selection, escalation through generated agent commands, version incompatibility, source drift and false multi-agent independence; linked to existing RM risks. No L/I or verified residual was lowered. If rejected, revert the PLAN-092 Git documentation delta without deleting historic PLAN-090/091 reviews or unowned host paths; restore the Google document independently from its revision history. Any native init needs a separate local backup and reviewed rollback before it changes working files.
