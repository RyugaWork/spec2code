# Quickstart — S2C + Spec Kit development (Web and Native)

> `WEB_MARKDOWN_BOOTSTRAP` is the present verified mode. `specify-cli`/official skills **not installed/NOT_RUN** in this repository. Follow [S2C root AGENTS](../../AGENTS.md) and preserve A.1/B/B.1.

## Path A: ChatGPT Web with connected GitHub

1. Work in the **existing** S2C branch `docs/plan-089-a1-readiness`; fetch the *current* Git SHA, read [root AGENTS](../../AGENTS.md), [S2C master BRD/SRS](../../.agents/.spec.md), [RTM](../../.agents/.traceMatrix.md) and [risk matrix](../../.agents/.riskMatrix.md).
2. Read [Constitution](../../.specify/memory/constitution.md) (DRAFT) and [feature selector](../../.specify/feature.json). This selector points at this folder and is independent of branch name.
3. Follow feature [spec.md](spec.md) → [research.md](research.md) → [plan.md](plan.md) → [data-model.md](data-model.md) → [tasks.md](tasks.md). Use [requirements checklist](checklists/requirements.md) and [acceptance design](checklists/integrationAcceptance.md).
4. Review changes as **Markdown** via authorized GitHub connector. Record requirement IDs, evidence and risks in global RTM; never claim an upstream `/speckit-*` agent command or Python command ran in Web mode.
5. Capture honest handoff and source/provider revisions. A.1 independent validation and separately approved B scope precede code changes; B.1/release separate.

## Path B: Codex / GitHub Codespaces / local native pilot

Before running anything against S2C, obtain authorizations and review the pinned candidate/security delta in [native pilot plan](../../.agents/.documents/specKitNativePilot.md) and [research.md](research.md). Use an explicitly allowed **disposable detached worktree** with its own safe path; never run `--force` against your active project branch.

Example **for a reviewed v1.2.6 disposable candidate only**, not a default production release:

~~~bash
uvx --from 'git+https://github.com/github/spec-kit.git@v1.2.6' specify version
uvx --from 'git+https://github.com/github/spec-kit.git@v1.2.6' specify init \
  --here --force --non-interactive --integration codex --script py
git status --short
git diff --name-status
python .specify/scripts/python/check_prerequisites.py --json --require-spec --require-tasks --include-tasks
~~~

**Check**: inspect **untracked** generated files under `.specify/scripts/` and `.agents/skills/speckit-*/`, preserve original Constitution and active feature pointer byte-for-byte or record resolved conflicts; check exact CLI/version/exit code and scan generated skills. Do not adopt any new file into the working branch without owner review. If installer unavailable, stop and record `BLOCKED_NOT_RUN`. Do not enable optional Spec Kit Git extension (user prefers fewer branches).

After actual native installation, follow the *agent-specific official* Spec Kit skill invocation as supported. The official `/speckit-*`/`$speckit-*` names differ by host; **they are not commands to paste into a shell**.

## Troubleshooting and handoff

- `NO_ACTIVE_FEATURE`: inspect `.specify/feature.json`; do not infer from Git branch.
- `SPEC_KIT_GATE_BLOCKED`: required artifact missing; verify feature files and read-only bridge provenance.
- No `specify` command or DNS: native path unavailable, Web mode still works.
- Policy/host/feature drift: STOP, record old and new ref and risk; do not reuse stale approval.
- An unowned file will be overwritten: STOP, preserve original contents; require explicit owner scope, backup and reviewed diff.

**Status for this iteration:** documentation and static GitHub preflight can be verified; actual native installed-runner acceptance, independent A.1, B and B.1 remain NOT_RUN / NOT_AUTHORIZED.

## PLAN-095 — Controlled Web-mode GitHub edit evidence

This bounded paragraph was added as a **document-only authorized GitHub connector operation**, to be re-fetched and checked against an exact commit in the [Web-mode execution evidence](../../.agents/.documents/specKitWebModeEvidence095.md). It is **not** evidence that upstream `specify`, any native Spec Kit coding-agent skill, a local Python guard, CI or independent A.1/B.1 verification executed.
