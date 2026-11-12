# Incremental infrastructure scan — v0.3 (reference only)

The session guard owns state writes. `scan_infrastructure.py` is a read-only diagnostic CLI and a reusable module for metadata fingerprinting. It **never directly writes** the two root change logs.

- `start`: before every new coding session. Inspect local HEAD and compare previous session snapshot. Produces at most a bounded stdout summary and writes the graph/matrix/short index. Initial state is BASELINE, not fake changes.
- `checkpoint`: re-check if commits may have arrived or after implementation; distinguishes external commits and unclassified local edits.
- `record`: registers only verified self-edited paths (with note, requirement and current session ID) into the session-scoped pending spec log.
- `finish`: validates fingerprints and closes session only if no unclassified final differences remain.
- `start --verify` or `checkpoint --verify`: rehash eligible source files when timestamps/size are unreliable. Default reuses cached SHA-256 when size+mtime are unchanged.
- `inspect --layer api`: query one neighborhood of graph rather than opening the whole system-graph.json.
- Standalone `python .../scan_infrastructure.py --root .`: read-only diagnostic; cannot advance the session baseline and lose provenance.

Safety: exclude `.env*`, private keys, certificates, vendor and generated dependency folders. Potentially credential-bearing config is **metadata-only**. Do not run Docker, fetch GitHub, call APIs, build images, read database credentials, or probe endpoints as part of the scan. Package manifests/entrypoint lines are parsed **locally** only to infer static indicators; the scanner doesn't send them to a model.

Limits: candidate file safety cap 12,000, individual hash cap 2 MiB, Git delta cap 200 commits, default listed path cap 12. A cap exceeded causes a `BLOCKED`/failed scan, never a false complete result.

Known uncertainty: native Git commits and tracked working tree history are local-only; `GitHub-Session` trailers do not authenticate identity; metadata-only configs cannot detect content changes if both size and timestamp are preserved. Graph edges from architecture policy are not tested runtime dependencies. A source folder can contain code while its build/runtime remain unverified.
