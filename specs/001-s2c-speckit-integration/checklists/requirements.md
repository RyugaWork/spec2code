# Requirements Quality Checklist: Spec Kit Integration for S2C

**Status:** DRAFT / NOT_SIGNED. Check marks indicate a human-reviewed design claim only, never test PASS or A.1 signoff.

## Requirement and provenance review

- [ ] Each SKI-FR-001..012 has a unique statement, authoritative BR/REQ/AC trace, nonfunctional limitations and observed or planned test.
- [ ] All user stories name the actor, preconditions, desired outcome and negative paths; feature requirements do not duplicate the full S2C BRD.
- [ ] Official Spec Kit ownership of `.specify/`, `specs/` and native agent commands remains separate from S2C's root/host AGENTS and Python guards.
- [ ] Feature directory is selected by `.specify/feature.json`, with explicit `SPECIFY_FEATURE_DIRECTORY` override behavior. Git branch does not act as pointer.
- [ ] ChatGPT Web is declared Markdown+connector mode; it never claims CLI/agent skills, session/process execution or six independent workers without a real host.
- [ ] The read-only `speckit_bridge.py` preflight does not become a change permission or an independent validation decision.
- [ ] Path traversal, symlink/junction, unauthorized host write, stale SHA, prompt injection and duplicate authority are explicit negative acceptance cases.
- [ ] Official `specify init` overwrite/collision and scripts/skills compatibility are reviewed in a disposable checkout before source adoption.
- [ ] A.1 independent validation, explicit B authorization, source-specific verification, B.1 and release are distinct evidence-backed gates.
- [ ] Acceptance criteria are actionable and map to test cases that can be executed in actual authorized environments; currently unexecuted cases remain NOT_RUN.

## Blocking decisions

- [ ] Owner(s) and exact authorization of business, host, security and A.1 reviewer are supplied.
- [ ] Approved official Spec Kit release and Codex/Copilot integration, version support and platform matrix documented.
- [ ] Native init collision policy, rollback, feature pointer owner and optional CLI script execution scope documented.
- [ ] CI/host security/QA test plan and source-bound evidence owner documented before B.1.

**Result:** READY_FOR_DESIGN_REVIEW_ONLY until the boxes are actually checked with recorded evidence. This file is a checklist, not a test-result registry.

## PLAN-094 — Requirements-quality evidence queue

The official upstream [Spec Kit v1.2.6 specification template](https://github.com/github/spec-kit/blob/v1.2.6/templates/spec-template.md) expects User Scenarios & Testing, Requirements, Success Criteria and Assumptions. The [plan template](https://github.com/github/spec-kit/blob/v1.2.6/templates/plan-template.md) expects technical context, Constitution Check, project structure and complexity tracking. The feature docs now explicitly include these sections, while preserving the S2C global authority boundary.

**Pending evidence to evaluate checkboxes:** confirm the final Git SHA includes 12 exact SKI-FR rows in RTM, 24 matching P/N acceptance cases, 15 unique tasks, complete links, stakeholder/host permission and a real independent A.1. This checklist intentionally remains unchecked: source writing and its author's self-inspection do not constitute independent quality approval or executed security tests.

**Related artifacts:** [research](../research.md), [logical model](../data-model.md), [Web/Native contract](../contracts/web-native-interface.md), [quickstart](../quickstart.md), [acceptance cases](integrationAcceptance.md).

## PLAN-095 — Explicit pre-implement checks (UNSIGNED)

- [ ] Review [native execution safety gate](../../../.agents/.workflow/specKitNativeExecutionGate.md) on the **current** Git SHA; distinguish written guidance from actual host enforcement.
- [ ] Confirm no `$speckit-implement` or `$speckit-converge` will process mixed T001..T015 owner-approval tasks as executable coding work.
- [ ] Confirm the exact source has a real independent A.1 decision and separate scoped B owner authorization before writing source.
- [ ] Confirm an upstream checklist continuation response cannot bypass root/nested AGENTS, host Path Guard, source-drift detection or explicit B permissions.
- [ ] Confirm a real selected native agent host has the required controls and records actual negative-case test evidence; do not infer safe execution merely because documentation exists.

**All items remain unchecked.** This is a requirements-quality checklist, not a native interception hook or executed security test.
