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
