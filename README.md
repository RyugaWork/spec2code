# Spec2Code v0.7.0

Infrastructure-aware, universal Spec-to-Code agent skill with optional read-only upstream GitHub Spec Kit bridge.

**Status:** repository layout migration candidate; prior Windows/security risks remain open. Requires Python 3.10+ and Git. Spec Kit CLI is separate.

## Repository layout and governance

Development repository is organized under `.agents/` (requirements, features, plans, risks, handoffs, workflow) and `.source/` (portable skill, scripts, tests, references, integrations, JSON configs). Read [structure](.agents/.structure.md), [features](.agents/.features.md), [plan](.agents/.plans.md), [risk register](.agents/.risk.md), [checklist](.agents/.checklist.md) and [handoff](.agents/.handoffs/v0.7.0-layout-handoff.md).

The **installed target project** is different: copy the `.source/` skill bundle into `<target>/.agents/skills/spec-to-code/`; keep target-owned `.agents/state/`, `.handoffs/`, `.specify/` and `specs/` separate. See [INSTALL](docs/INSTALL.md).

## Existing capabilities

Strict JSON config loading, Git root and path containment, physical checkout-bound sessions, static infrastructure inventory and architecture graph, adaptive minimal/balanced/deep context routing, source-change provenance, exact-session handoff, read-only Spec Kit feature bridge and MCP-ready authorization *library*. No real MCP server, arbitrary shell/remote Git operation or automatic authorized code-writing agent exists.

## Development tests

```sh
python -m unittest discover -s .source/tests -v
```

## Portable installed skill example

From the **target Git repository root**, after copying `.source/` contents into `.agents/skills/spec-to-code/`:
```sh
python .agents/skills/spec-to-code/scripts/session_guard.py --root . start
python .agents/skills/spec-to-code/scripts/speckit_bridge.py --root . --stage status
```

The Spec Kit `implement` stage requires active feature `spec.md`, `plan.md`, `tasks.md`. Never treat an artifact's existence as human approval.

## Security and release status

No unconditional overwrite or deletion of host project files is authorized by this layout change. POSIX anchored file operations offer additional containment; Windows TOCTOU, case-folding, path alias, CRLF and generated-document collisions need additional verification. See [risk register](.agents/.risk.md) and [Path Guard](docs/PATH_GUARD.md).
