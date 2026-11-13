# PLAN-081 — Agent instructions and Spec Kit handoff

Date: 2026-11-13 (Asia/Ho_Chi_Minh)
Status: IMPLEMENTED DOCS / ACCEPTANCE PENDING
Repository: RyugaWork/spec2code
Base: PR #7 development head `8f936e95dc4ff3cc4d936fd5e5167b86e441fbfe`
Work branch: `feat/agent-governance-v0.8.0`
Scope: agent instructions and reference Markdown; no Python runtime/control/test modification.

## Input and authority inspected
- Development specification, feature/plan/risk/checklist, structure and workflow policies in `.agents/`.
- Existing `.source/SKILL.md`, Spec Kit integration/read-only bridge, policy resolver, workflow guard, Context Router, Path Guard, Scope IO, session and handoff modules and their test entrypoints/configurations.
- Existing user-facing installation, configuration, AGENTS patch, runtime layout and security reference docs.
- Official GitHub Spec Kit SDD and Codex integration documentation (agent skill commands are distinct from the CLI).

## Delivered
- Root development AGENTS contract separates authority, source ownership, read-only vs write modes, lifecycle stages, security protections and unavailable runtime features.
- `.agents/.workflow/agentRoles.md` defines logical human-directed role responsibilities, outputs and escalations without pretending autonomous subagents exist.
- `.agents/.workflow/agentRunbook.md` defines the actionable preflight, Spec Kit bridge/native skill ordering, scoped implementation, verification, handoff and reporting.
- Portable Skill/integration guidance and optional host AGENTS patch avoid overwriting a host-owned policy or upstream Spec Kit artifacts.
- Agent governance specification, plan, feature, checklist, risk, workflow and authority references aligned.

## Verification ledger (do not convert NOT RUN to PASS)
- Code change in `.source/scripts/`, `.source/tests/` or `.source/.config/`: NONE.
- Local runtime regression: NOT RUN when operating via GitHub-only connector.
- CI on the newly committed final SHA: PENDING; query exact PR/head and record job IDs and skip counts.
- Documentation path/CLI consistency: REVIEW PENDING, then update this handoff with exact findings.
- Human security review, real Windows OneDrive/junction races, legacy runtime migration: NOT RUN / OPEN.
- Parent PR #7 still has three P0 and one P1 open review findings in Workflow Guard; instructions **do not** fix them.

## Safety, rollback and release
No host files, installed sessions, legacy handoffs, `s2c/`, `.specify/` or `specs/` were modified. Revert the focused docs commits from the dedicated branch if rejected; preserve historic data. Do not merge into `spec2code/InitialVersion_v0` or call v0.8 stable until both code and independent acceptance gates are satisfied.
