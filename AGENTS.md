# AGENTS.md — Spec2Code Repository

- This repository develops the portable Spec-to-Code skill; do not confuse it with a target application's code or its approved requirements.
- Preserve compatibility of `SKILL.md`, `scripts/`, `references/` and `tests/`; generated state belongs in the target repository, not here.
- Before changing scanners/session logic, inspect its relevant unit tests and run `python -m unittest discover -s tests -v`.
- Never collect, log, commit or publish credentials, private member information, local `.env` values or transient session state.
- Commits must follow Conventional Commits 1.0.0. Do not rewrite user changes or force-push.
- Repository is public. Ensure that changes contain no proprietary Gymuro data or secrets.
- `docs/AGENTS_PATCH.md` is a proposed patch for downstream Gymuro installations, not authority over this repository.
- Current skill depends on Python 3.10+ and local Git. MCP/remote integration is a separate future feature.
