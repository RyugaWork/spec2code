# S2C Spec Kit adoption — native-compatible Markdown bootstrap

**Current state: WEB_MARKDOWN_BOOTSTRAP. NOT the result of running `specify init`.** This directory was created by scoped GitHub document writes to use official Spec Kit artifact conventions in S2C's *development repository*. The official CLI scripts, templates and agent command/skill bundles have **not** been installed here. Their existence must never be assumed from this README.

## Canonical source and active feature

- [Development AGENTS](../AGENTS.md): agent permissions, Path Guard, phase gates and evidence.
- [Master BRD/SRS](../.agents/.spec.md): system-wide business authority; Google document is a stakeholder review mirror.
- [Spec Kit Constitution](memory/constitution.md): project feature workflow (DRAFT, not ratified).
- [Active feature pointer](feature.json): `specs/001-s2c-speckit-integration`, independent of Git branch. The upstream environment override `SPECIFY_FEATURE_DIRECTORY` may change selection, but the S2C bridge rejects escapes outside the checkout.
- [Feature specification](../specs/001-s2c-speckit-integration/spec.md) / [plan](../specs/001-s2c-speckit-integration/plan.md) / [tasks](../specs/001-s2c-speckit-integration/tasks.md).
- [S2C read-only adapter](../.source/scripts/speckit_bridge.py) and [integration guide](../.source/integrations/speckit/README.md).

## Web/GitHub mode (available as document workflow)

1. Read root AGENTS, master SRS/RTM/risk, Constitution and the selected feature.
2. Use authorized GitHub connector to inspect and update `spec.md`, `plan.md` and `tasks.md`, preserving exact source SHA and all negative/approval gates.
3. Perform draft Specify/Clarify/Plan/Tasks/Analyze reasoning as **Markdown-driven steps**. Do not claim official CLI or coding-agent skill execution in ChatGPT Web.
4. Review diff, RTM/risk and handoff. No additional feature branch is required.
5. Stop at A.1; implementation only after independent approval and separate authorized B task.

## Native agent mode (requires separate official setup)

In a **disposable, backed-up checkout**, after selecting a reviewed release and obtaining owner consent, install the official `specify-cli`, then use the upstream existing-project instructions to run `specify init --here --force --non-interactive --integration <approved-key> --script py`. Review generated/overwritten files before merging. **Do not run init from ChatGPT Web or claim it was run from a GitHub-only edit.** Upstream may produce agent-specific skill files; inspect collisions with `.agents/skills/`.

Spec Kit documentation: https://github.github.com/spec-kit/how-to/existing-projects.html and https://github.github.com/spec-kit/quickstart.html . Native init/execute is a separate follow-up requiring a real terminal/agent host; this bootstrap is deliberately non-executable.

## Support status

`speckit_bridge.py --stage status|plan|tasks|analyze|implement|converge` statically checks artifact presence and returns hashes/task IDs. Its `READY` only means files are present within scope, **not** that A.1 passed or code is authorized. Standalone host repositories without Spec Kit remain supported. Avoid copying development Constitution into unrelated host repositories.
