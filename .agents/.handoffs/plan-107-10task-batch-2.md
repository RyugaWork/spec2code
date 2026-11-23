# PLAN-107 — Batch 2 of 5: ten security and host-boundary tasks

**Input SHA:** `83e894b58de866cb72f6044b00b034784a8067cb`, branch `docs/plan-089-a1-readiness`. **Output SHA:** commit containing this file; verify through a fresh GitHub read. **Executor:** GitHub connector for Markdown only.

| Task | Canonical file | Delivered design-review topic | Status |
| --- | --- | --- | --- |
| S01 | `docs/PATH_GUARD.md` | Windows and alias threat fixtures | AUTHOR_DRAFTED / HOST_NOT_RUN |
| S02 | `docs/CONTINUOUS_SCOPE_ENFORCEMENT.md` | Continuous guard coverage matrix | AUTHOR_DRAFTED / HOST_NOT_RUN |
| S03 | `docs/CONFIGURATION.md` | Config trust boundary and schema review | AUTHOR_DRAFTED / HOST_NOT_RUN |
| S04 | `docs/AGENTS_PATCH.md` | Host instruction isolation | AUTHOR_DRAFTED / HOST_NOT_RUN |
| S05 | `.agents/.documents/.policyRouting.md` | Policy decision failure states | AUTHOR_DRAFTED / HOST_NOT_RUN |
| S06 | `.agents/.config/README.md` | Governance config schema boundary | AUTHOR_DRAFTED / HOST_NOT_RUN |
| S07 | `.agents/.workflow/agentRunbook.md` | Sandbox Auto run checklist | AUTHOR_DRAFTED / HOST_NOT_RUN |
| S08 | `.agents/.workflow/stopAndHandoff.md` | Partial-write recovery test design | AUTHOR_DRAFTED / HOST_NOT_RUN |
| S09 | `.agents/.risk.md` | Incident vs candidate risk provenance | AUTHOR_DRAFTED / HOST_NOT_RUN |
| S10 | `docs/INTEGRATION_LAYOUT.md` | Layered trust topology | AUTHOR_DRAFTED / HOST_NOT_RUN |

### Risk review and acceptance

The ten additions specify independent OS trust, path aliases, continuous policy, schema and credential denial, host AGENTS adoption, sandbox/CLI capability proof, STOP persistence and provider topology. P0 residual is **UNKNOWN** without a real isolated host/negative sentinel run. No source code, runtime, host config, shell invocation, new branch or Google BRD business approval was performed.

Post-commit: verify ten S01..S10 sections, this handoff, parent/HEAD, changed Markdown scope and new relative Markdown links. Do not report a Codex `--full-auto` success: previous observed CLI 0.169.0-alpha.11.1 rejected the option, and separate state/bootstrap failed. Gemini MCP not verified.

**Next:** PLAN-108 Spec Kit owner contracts and Web/native artifact evidence. All A.1/B/B.1 external gates remain open; the archived local changes are untouched.
