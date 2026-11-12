# Agent governance configuration

This directory holds **development-governance metadata**, not the Spec2Code runtime policy. Runtime configurations live in `.source/.config/*.json` and must remain adjacent to the packaged `.source/scripts/` directory.

Never store credentials or local machine/session state here. Any future machine-readable governance config must have strict schema validation and no permission to weaken Path Guard or grant execution rights.
