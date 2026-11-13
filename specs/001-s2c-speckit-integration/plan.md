# Implementation Plan: Spec Kit Integration for S2C

**Feature:** [001-s2c-speckit-integration](spec.md)  
**Status:** DESIGN_DRAFT / IMPLEMENTATION_NOT_AUTHORIZED  
**Scope:** Existing S2C repository only. Project-wide source authority remains [S2C master](../../.agents/.spec.md); this plan is a feature refinement and does not supersede A/P1–P9, A.1, B or B.1.

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
