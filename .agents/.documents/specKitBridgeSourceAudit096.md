# PLAN-096 — Source-bound Spec Kit bridge contract and negative-case audit

> **SOURCE_REVIEW / DESIGN ONLY — 2026-11-13.** Reviewed S2C Git commit `72920032a892b8a60c74fbdf2b62847fb5fa771d`, bridge blob `0cd25a4fbe1322710f0492f4036eb83fc27a8282`, current test blob `5e9a84eea8b145b1c93e33dccd8b4ba9185a168c`, config blob `f2a26f3b5e8a18a9b2d19dc48367b287fe790172`. These are static observations of actual code fetched via GitHub, **not** executing S2C's Python bridge. All 4 new negative tests below remain `NOT_RUN`, no verified exploit or risk-score reduction.

## 1. Existing bridge and executable dependency boundary

`.source/scripts/speckit_bridge.py` imports real `path_guard.py`, `scope_io.py` and `config_loader.py` and reads bundled `.source/.config/speckit.json` and `security.json`. `discover()` requires a valid Git checkout via `guard.validate_root`; it enforces artifact byte limits, symlink/junction checks and anchored reads on compatible OS. A response `READY` means **configured static artifact presence**, not semantically approved, safe-to-implement or human-authorized source code.

The available tool container has Python 3.13.5 and Git 2.47.3 but cannot resolve `github.com` (a bounded `git ls-remote` attempt failed DNS) and has no `specify` CLI or full S2C checkout. A test built with mock guard modules would not verify S2C's real Path Guard/Scope IO. **Therefore no bridge regression, Windows/junction negative test, installed-host test or official Spec Kit CLI execution is claimed.**

## 2. Four concrete specification–source discrepancies to decide and test

| ID | Actual source evidence (blob pinned above) | Feature expectation and risk | Decision / evidence status |
| --- | --- | --- | --- |
| `SK96-01` Feature namespace | `_feature_path` at bridge lines 47–60 checks relative/in-root/real-directory/link safety, but has **no `specs/<feature-id>` namespace assertion**. The environment override at lines 76–79 shares the same check. | `SKI-FR-001` requires a contained `specs/<feature-id>` selection. A contained `docs/other` directory may be accepted as a feature location if it exists, violating that feature-level contract (not necessarily escaping the root). | **SOURCE_CONTRACT_GAP / HOST_REPRO_NOT_RUN**. Decide whether official-compatible alternative feature directories are permitted via an explicit override, or enforce strict `specs/` under S2C policy. |
| `SK96-02` Ambiguous pointer JSON | `discover` line 84 uses default Python `json.loads` with no `object_pairs_hook` to reject duplicate JSON keys. By contrast, bundled `config_loader.py` uses `_pairs_without_duplicates`. | `SKI-FR-001/008`: one unambiguous feature authority. Repeated `feature_directory` keys make the effective value dependent on parser behavior and can surprise reviewers. | **SOURCE_CONTRACT_GAP / REAL_BRIDGE_NOT_RUN**. Consider strict JSON shape/duplicate-key checks, with backward compatibility and size bounds. |
| `SK96-03` Empty mandatory artifact | Bridge lines 104–120 treat `path.is_file()` as existence, read size/hash, then gate on `infos[name]['exists']`; no explicit empty/whitespace-only validation. | `SKI-FR-003/007` and `SKI-TC-003-N` expect missing/**empty** mandatory artifacts to be classified as incomplete/blocked. Empty files may otherwise satisfy presence-only stage prerequisites. | **SOURCE_CONTRACT_GAP / REAL_BRIDGE_NOT_RUN**. Decide whether nonempty vs valid-content semantics belong in bridge or a distinct quality gate. |
| `SK96-04` Task duplicates | Bridge lines 115–118 call `TASK_RE.findall`, set `task_count=len(ids)` and sample IDs, with **no `len(set(ids))` integrity assertion**. | `SKI-FR-006/007`, `SKI-TC-006-N` require duplicate/orphan task detection; current static GitHub audit reports 15 unique **today**, but bridge may accept duplicate IDs in a future feature. | **SOURCE_CONTRACT_GAP / REAL_BRIDGE_NOT_RUN**. Prefer a duplicate count/flag or explicit rejection at a quality-gated stage, preserving read-only semantics. |

**Classification discipline:** A source-contract gap is not the same as an observed security exploit or deployed failure. Existing test source contains seven `test_*` methods, covering no-init, manifest/no content, missing plan, external pointer, symlink pointer, generic src inventory and context routing. It does **not** contain specific duplicate-JSON, namespace-conflict, zero-byte or duplicate-task negative tests.

## 3. Small standard-library behavior probe actually executed

On the isolated tool container, without importing S2C, a Python standard-library smoke probe observed:
- `json.loads('{"feature_directory":"specs/001-valid","feature_directory":"docs"}')` returns `{"feature_directory":"docs"}` (last-key-wins).
- `Path(.../spec.md).write_bytes(b'')` yields `is_file() == True` and `stat().st_size == 0`.
- The exact configured T-ID regex matched two `T001` occurrences, count 2 and unique count 1.

These are **supporting language semantics only** and must not be reported as `SK96-NEG-*` bridge test PASS, reproduced attack or S2C source execution. The probe ran outside any user checkout and did not change S2C.

## 4. Proposed actual negative tests for a B-approved disposable host

| Test ID | Precondition / negative partition | Real bridge procedure and expected result | Evidence required |
| --- | --- | --- | --- |
| `SK96-NEG-01` | Real Git worktree, `.specify/feature.json` points to existing `docs/owned-feature` containing `spec.md`, `plan.md`, `tasks.md` | Invoke `discover(root,'analyze')` and compare observed behavior to owner-approved namespace policy; if strict `specs/` required, **BLOCK**, not silent READY. Test env override separately. | Exact SHA, pointer, returned value/error, no outside writes, policy decision |
| `SK96-NEG-02` | Duplicate `feature_directory` keys, both candidate paths existing; malformed JSON control | Invoke `discover(root,'status')`; under strict uniqueness policy **BLOCK** ambiguous pointer before resolving the later path. | JSON bytes, exit/error, root/sentinel hashes |
| `SK96-NEG-03` | Zero-byte `plan.md` and whitespace-only `tasks.md`, other artifacts valid | Invoke `discover(root,'implement')`; agreed stage-quality rules must reject or flag empty mandatory artifact explicitly, never claim human approval from READY. | File sizes and hashes, output, exit code, expected quality-gate rule |
| `SK96-NEG-04` | Two `T001` entries with different `[US1]`/`[US2]` story labels | Invoke `discover(root,'analyze')`; explicit duplicate evidence must be surfaced and prevent quality approval; optionally return count/duplicates flag rather than changing static readiness contract. | Original task text hash, observed IDs/count, duplicate detection, exit result |

**Test preconditions:** authorized disposable checkout, actual unmodified bridge + real bundled guard dependencies, source-specific expected behavior agreed and recorded, no modifications to the active user's branch. Do not simulate a PASS by replacing safety dependencies with mocks. Run on Linux and Windows/OneDrive/junction where applicable under separate host scopes. Before any guard/source patch require genuine independent A.1 and separately approved B scope (T011/T012), then B.1 and release evidence separately.

## 5. Recommended patch order after approval

1. **Contract decision:** adopt either strict `specs/<id>` policy or explicit allowlisted relative feature overrides, including backward compatibility.
2. **Input integrity:** strict pointer JSON duplicate check, bounded shape and untrusted value semantics.
3. **Feature artifact quality:** reject/flag empty mandatory artifacts with clear distinction between structural completeness and semantic review.
4. **Task identity quality:** report duplicate and truncated IDs without leaking specification bodies.
5. **Actual regression:** run all seven existing bridge tests, four new negatives, no-initialization/override/collision cases, and adversarial Path Guard/Scope IO cases in real checkout, recording OS, SHA, stdout/stderr/exit and sentinels.
6. **Review:** independent A.1/B/B.1 ownership and runtime code changes subject to existing S2C gates; no auto-merge.

## 6. Source and risk links

[Feature spec](../../specs/001-s2c-speckit-integration/spec.md), [feature plan](../../specs/001-s2c-speckit-integration/plan.md), [24 existing acceptance cases](../../specs/001-s2c-speckit-integration/checklists/integrationAcceptance.md), [RTM](../.traceMatrix.md), [risk](../.riskMatrix.md), [PLAN-095 real Web evidence](specKitWebModeEvidence095.md). No owner signed these four contract decisions yet.
