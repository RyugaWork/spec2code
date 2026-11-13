# Implementation Plan: Spec Kit Integration for S2C

**Feature:** [001-s2c-speckit-integration](spec.md)  
**Status:** DESIGN_DRAFT / IMPLEMENTATION_NOT_AUTHORIZED  
**Scope:** Existing S2C repository only. Project-wide source authority remains [S2C master](../../.agents/.spec.md); this plan is a feature refinement and does not supersede A/P1–P9, A.1, B or B.1.


## Summary

Use the **official Spec Kit feature-level document workflow** to develop S2C itself. Web/GitHub mode maintains native-compatible Markdown, while a separately installed native Codex/Codespaces host may run upstream skills after safety preflight. The S2C global BRD/AGENTS/RTM/risk model remains authoritative. Research compares official versions and security deltas, but no upstream CLI was installed in the current offline terminal.

## Technical Context

| Template field | Existing observed or proposed value |
| --- | --- |
| Language / version | S2C source: Python and Markdown; disposable runner Python 3.13.5 observed; official upstream `v1.2.6` declares Python>=3.11; no version has been approved for the actual host |
| Dependencies | Existing S2C read-only bridge, Path Guard/Scope IO and GitHub connector; optional upstream `specify-cli` only after owner-reviewed install |
| Storage | Versioned Markdown artifacts in Git, selected pointer JSON; no new database or remote agent server |
| Testing | Existing source tests `.source/tests/test_speckit_bridge.py` (not rerun), 24 planned feature acceptance cases, future official native prerequisite tests |
| Platform | GitHub Web; pilot intended Codex/Codespaces/Linux/Windows; actual OS/OneDrive/junction support remains unverified |
| Risk | RM-001..005 OPEN/P0; `--force` collision SK-R01, version SK-R04, privilege and source drift |
| Performance and scale | No owner-approved token/latency/SLO values; no performance promises |
| Project scope | S2C development repo and this one active Spec Kit feature only; host repositories remain independently owned |

## Constitution Check (draft, not formal A.1)

| Principle | Planned design evidence | Remaining gate |
| --- | --- | --- |
| I Evidence first | Exact Git/Google revisions, no fabricated CLI/worker/test outcome | Real host tests and independent source review |
| II Single requirement authority | Master S2C SRS + 12 explicit RTM links | Authoritative stakeholder ratification |
| III Least privilege | Read-only bridge and provider boundary contract | Existing critical Path Guard/host risks OPEN |
| IV A→A.1→B→B.1 | Separate decision state in docs and runbook | Real A.1 signature and B permission |
| V Negative verification | 24 proposed P/N feature cases, collision and STOP tests | Tests NOT_RUN |
| VI Portable mature stack | Web mode available; official version candidates compared | CLI version/OS/agent owner acceptance |
| VII Honest collaboration | Same-model review cannot sign gate; handoffs preserve status | Real independent reviewer |

**Constitution Check outcome:** `DESIGN_PRESENT / RATIFICATION_UNKNOWN / A1_NOT_RUN`, not PASS.

## Project Structure — source ownership map

~~~text
AGENTS.md                       # S2C development agent policy
.agents/.spec.md                # canonical S2C BRD/SRS
.agents/.traceMatrix.md         # bidirectional requirement ownership
.specify/feature.json           # official-style active feature pointer
.specify/memory/constitution.md # feature process constitution (DRAFT)
specs/001-s2c-speckit-integration/
  spec.md                       # feature-level requirements
  plan.md                       # this plan
  research.md                   # upstream/maturity/alternatives
  data-model.md                 # logical artifacts and state
  contracts/web-native-interface.md
  tasks.md
  quickstart.md
  checklists/requirements.md
  checklists/integrationAcceptance.md
.source/scripts/speckit_bridge.py   # actual read-only source adapter
.source/.config/speckit.json        # current source config
~~~

**Not generated:** `.specify/scripts/` and `.agents/skills/speckit-*/` are absent until official native init actually runs in an authorized checkout.

## Complexity Tracking

The preferred architecture deliberately avoids new code/runtime/CI/MCP/agent-daemon complexity in this stage. Rationale: no approved host benchmark or operational constraints justify it, the existing bridge already reads official feature manifests, and changing a security-critical runtime before A.1 would be unsafe. A future B design must document any deviations, compatibility tests, migration and rollback.

## 1. Architectural decisions and constraints

- **DEV-01 — Two operational surfaces:** Web/GitHub connector mode uses Markdown + authenticated GitHub read/write; native local agent mode uses upstream official `specify` CLI and agent skills after a separate reviewed installation. A static Web-mode artifact is not proof a CLI step ran.
- **DEV-02 — One native feature locator:** `.specify/feature.json` selects `specs/001-s2c-speckit-integration`. Selection is independent of Git branch and may be overridden by upstream `SPECIFY_FEATURE_DIRECTORY` only under local S2C scope policy.
- **DEV-03 — Authority:** `AGENTS.md` is the S2C agent operating policy, `.agents/.spec.md` owns global business/SRS, `.specify/memory/constitution.md` owns Spec Kit feature guidance, `specs/.../` owns feature spec/plan/tasks. External host AGENTS and official Spec Kit generated artifacts stay owner-controlled.
- **DEV-04 — Bridge stays read-only:** `.source/scripts/speckit_bridge.py` already reports hashes and task IDs, not bodies. No new worker runtime or CLI modification in initial integration.
- **DEV-05 — Minimal Git workflow:** Keep branch `docs/plan-089-a1-readiness`; the optional Spec Kit Git extension (and automatic feature branches) is deliberately not enabled without user request.
- **DEV-06 — Version adoption:** Official CLI release choice follows S2C conservative technology policy. A pinned, reviewed source tag is preferable to unreviewed latest. Current proposed policy requires explicit acceptance; a code release is NOT_INSTALLED via this commit.

## 2. Architecture and data flow

```text
Requester / ChatGPT Web / native Codex or Copilot
   -> root AGENTS + S2C master BRD/SRS + RTM/risk
   -> active .specify/feature.json
   -> specs/001-s2c-speckit-integration/{spec,plan,tasks}.md
   -> (Web) bounded GitHub file updates + review + handoff
      or
      (Native) official CLI/agent skills after reviewed install
   -> S2C read-only speckit_bridge.py
   -> S2C context/trace/risk and A.1/B/B.1 gates
```

**Existing inputs:** `.source/.config/speckit.json` stage prerequisites and `.source/scripts/speckit_bridge.py`; no undocumented stage operations are added. The existing bridge supports stage names `status/specify/plan/tasks/analyze/implement/converge`. Official `clarify/checklist/constitution` remain external agent steps; missing bridge enums do **not** mean upstream lacks them.

## 3. Delivery stages and acceptance evidence

| Stage | Work | Entry / exit and evidence | Current |
| --- | --- | --- | --- |
| SK-01 | Native-compatible repo bootstrap: constitution + feature selection + spec/plan/tasks | Files exist, valid pointer and relative scope, unchanged host assets | DOC_AUTHORED, verification pending |
| SK-02 | AGENTS/RTM/research/risk and Web+Native guide | All feature and task links resolve, no duplicate normative BRD, honest gating | DOCUMENTATION_DRAFT |
| SK-03 | Local disposable pilot of official `specify init` pinned approved release and reviewed agent integration | Capture CLI/version, generated file inventory, diff/collisions, script/skill hashes, rollback; never force into working repo unreviewed | NOT_RUN |
| SK-04 | Optional adapter enhancements and real regression tests | Only after independent A.1 and separately authorized B, exact source SHA and host matrix | NOT_AUTHORIZED |
| SK-05 | Independent A.1/B.1 and release decisions | Per-check real reviewer/host evidence and owner signoff | NOT_RUN |

## 4. Risks, decisions, rollback

- **Risk SK-R01 (scope):** `specify init --force` may overwrite generated/shared files; bootstrap must not pretend CLI init is already done. Review diff and back up `.specify`, `.agents/skills` and active feature pointer.
- **Risk SK-R02 (integrity):** Using a Git branch as feature locator rather than `.specify/feature.json` can select the wrong work; track both separately and re-check on resume.
- **Risk SK-R03 (authority):** A Spec Kit script/skill must not bypass Path Guard, root/host AGENTS, A.1/B gates or required policy. Treat native tool execution as untrusted until checked.
- **Risk SK-R04 (version):** New upstream changes and unsupported host Python/PowerShell may drift; pin and review versions, migrations, install collision and backward compatibility.
- **Risk SK-R05 (documentation):** Feature spec/plan/tasks can diverge from BRD/RTM and Google revision; re-map impacted BR/AC and STOP if source is stale.
- **Risk SK-R06 (review):** Single-model web review must not be reported as independent agent fleet or security acceptance.

**Decisions still required:** accountable business/security reviewer for A.1, accepted CLI stable release and agent integration (Codex/Copilot), supported host environment, exact integration branch target and approval for any code/host install. Without decisions, documentation bootstrap can be reviewed but no implementation/release is authorized.

**Rollback:** revert only added documentation files in this feature on the authorized branch; do not delete unknown `.specify`/host state. Any later official CLI initialization requires a baseline backup and reviewed diff before applying to development or host.
