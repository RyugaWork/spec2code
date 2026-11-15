# S2C — Antigravity CLI / Gemini Hydrogen Low reviewer (PLAN-113)

**Date:** 2026-11-15 (Asia/Ho_Chi_Minh). **Status:** CLI SMOKE_TESTED_BY_REQUESTER / DOC_OPERATIONAL_GUIDE / AUTO_REVIEW_NOT_IMPLEMENTED / OS_READ_ONLY_NOT_VERIFIED. This is the operator runbook for the existing PLAN-101 optional Codex/Gemini reviewer, not a second orchestration design, a replacement BRD, or a Phase-B implementation approval.

## 1. Choice and non-negotiable boundaries

- **Provider:** installed Google Antigravity CLI `agy`, authenticated interactively with the requester's existing Google account (reported Google AI Pro). No separate Gemini API key is required for the observed CLI smoke tests; subscription entitlement/quotas and additional charging are **not independently verified** by S2C.
- **Routine model ID observed working:** `gemini-4-hydrogen-low`. Resolve actual model capability/version at runtime; if unavailable, report `MODEL_UNAVAILABLE`, not a silent substitute.
- **Role:** second-model **technical reviewer** of a *frozen, redacted, task-relevant diff*. Codex is the only separately authorized writer. Gemini findings are untrusted suggestions, never executable instructions or A.1/B.1 signatures.
- **No `--mode plan` in the headless reviewer command.** On the requester's Windows PowerShell 5.1, that option returned a plan artifact rather than review findings. The subsequent successful CLI invocations omitted `--mode plan`.
- **Do not enable `--dangerously-skip-permissions`, Accept-edits or Auto mode for reviewer automation.** Do not rely on an instruction such as "Do not modify files" or Plan mode as an OS-level read-only boundary. A read-only, disposable, independently enforced host is a prerequisite for automated review of real repository data. RM-001 and Windows hostile-race tests are still open.
- **Phase gate:** read-only isolated reviewer *design/smoke tests* can be documented during A; an S2C queue, Codex notify hook, write-capable process, host integration or production rollout remains B_NOT_AUTHORIZED absent the proper gates.

## 2. Windows PowerShell 5.1 — verified CLI interface

Open a fresh terminal. The requester's installer placed `agy.exe` under `$env:LOCALAPPDATA\agy\bin`, but the operator should **discover**, not hardcode, its final path:

```powershell
Get-Command agy -ErrorAction Stop
agy --version
```

If it is not on the active session's PATH after a successful installation:

```powershell
$env:Path += ";$env:LOCALAPPDATA\agy\bin"
Get-Command agy -ErrorAction Stop
```

Interactive sign-in, if needed: run `agy`, complete the Google account OAuth flow, then exit. **Never put OAuth tokens, cookies, auth files or credentials into repo docs, prompts, CI or handoffs.** Verify the available model with the CLI before adopting it; the supplied smoke tests already establish that `--model gemini-4-hydrogen-low` worked on this operator's session.

**Clean-code smoke test (observed result: zero findings):**

```powershell
agy -p 'Review ONLY this Python code: def add(a,b): return a+b. Identify actual correctness bugs. Do not create plans, edit files, or call tools. Return only JSON with fields review_completed (boolean) and findings (array). Use an empty findings array if no bugs exist.' --model gemini-4-hydrogen-low --output-format json --print-timeout 2m
```

**Known-defect negative control (observed result: one finding):**

```powershell
agy -p 'Review ONLY this Python code: def divide(a,b): return a/b. Requirement: the function must safely handle b=0 without raising an exception. Identify correctness defects. Do not create plans, edit files, or call tools. Return only JSON with fields review_completed (boolean) and findings (array containing severity, issue, and recommendation).' --model gemini-4-hydrogen-low --output-format json --print-timeout 2m
```

Expected finding: `ZeroDivisionError` when `b=0`. Any suggested fallback value needs a separately approved contract. These tests provide no access to real S2C source, no evidence of a read-only OS sandbox and no claim of production-level reviewer accuracy.

## 3. Evidence register — user-provided PowerShell output

| Probe | Invocation | CLI status / semantic review | Duration | Input / output / thinking | Cached | Reported total |
| --- | --- | --- | ---: | --- | ---: | ---: |
| AGY-SMOKE-01 | `--mode plan` / Hydrogen Low / inline add | `SUCCESS` but **REVIEW_INCONCLUSIVE**; response requested approval of `implementation_plan.md` | 9.5084 s | 12,897 / 645 / 196 | 8,171 | 13,542 |
| AGY-SMOKE-02 | No `--mode plan`, inline add | `SUCCESS`, `review_completed=true`, `findings=[]` | 3.5011 s | 10,525 / 137 / 110 | 0 | 10,662 |
| AGY-SMOKE-03 | No `--mode plan`, inline divide with explicit zero rule | `SUCCESS`, one HIGH finding for `ZeroDivisionError` | 3.4591 s | 10,531 / 234 / 107 | 0 | 10,765 |

These numbers are supplied by the requester, **not reproduced by a repo CI runner or this documentation change**. Treat `cache_read_tokens` as an input subset; never add it to `total_tokens`. Output `response` in successful tests was a Markdown-fenced JSON *string inside the outer JSON envelope*. `status=SUCCESS` only means the CLI invocation succeeded; it does not establish that a valid review occurred. The ~10.5k input-token overhead on two tiny prompts makes per-turn reviews unattractive. Input-size caps limit **supplied diff**, not automatically all provider/system-context tokens.

## 4. Minimal PowerShell 5.1 response validation (manual-only demonstration)

Run this only with synthetic code until an independently enforced sandbox and data-sharing permission are approved. Do not add this snippet to global profiles or Codex hooks.

```powershell
$ErrorActionPreference = 'Stop'
$prompt = 'Review ONLY def divide(a,b): return a/b. Requirement: b=0 must not raise. Do not edit files or call tools. Reply ONLY with JSON: {"review_completed":true,"findings":[{"severity":"high","issue":"reason","recommendation":"fix"}]}.'
$rawLines = & agy -p $prompt --model gemini-4-hydrogen-low --output-format json --print-timeout 2m
$exitCode = $LASTEXITCODE
if ($exitCode -ne 0) { throw "REVIEW_INCONCLUSIVE: agy exit=$exitCode" }
try {
    $envelope = ($rawLines -join "`n") | ConvertFrom-Json -ErrorAction Stop
    if ($envelope.status -ne 'SUCCESS' -or [string]::IsNullOrWhiteSpace($envelope.response)) { throw 'Unsuccessful or empty CLI envelope' }
    $payload = $envelope.response.Trim()
    $payload = $payload -replace '(?s)^\s*```(?:json)?\s*', ''
    $payload = $payload -replace '\s*```\s*$', ''
    $review = $payload | ConvertFrom-Json -ErrorAction Stop
    if ($review.review_completed -ne $true -or $null -eq $review.findings -or $review.findings -isnot [array]) { throw 'Missing semantic review fields' }
    [pscustomobject]@{ Status='REVIEW_COMPLETED'; Findings=@($review.findings).Count; InputTokens=$envelope.usage.input_tokens; TotalTokens=$envelope.usage.total_tokens }
} catch {
    throw "REVIEW_INCONCLUSIVE: invalid review envelope or payload. $($_.Exception.Message)"
}
```

**Schema rule for a future adapter:** `{review_completed:boolean, findings:array}` is a *minimum*, not sufficient acceptance. Check source-bound evidence, line/path validity, severity vocabulary, allowed fields, no hallucinated citations, no tool effects, token usage and exact snapshot identity. A valid empty array is `REVIEWED_NO_FINDINGS`, **not** `CODE_ACCEPTED`. Store raw CLI logs only in a reviewed, redacted, collision-safe output area; do not store unredacted prompts that may contain secrets.

## 5. Proposed Codex ↔ Gemini queue (NOT IMPLEMENTED)

```text
Authorized Codex task checkpoint (NOT every agent-turn-complete event)
    -> verify task/phase and capture immutable diff + exact base/HEAD/worktree hashes
    -> exclude secrets/credentials, binary, external/unowned files; enforce allowlist
    -> enqueue review keyed by hash(source snapshot + model + prompt/schema version)
    -> independent OS-restricted disposable read-only reviewer process, concurrency=1
    -> agy --model gemini-4-hydrogen-low --output-format json --print-timeout 2m
    -> validate outer JSON, semantic finding schema, actual evidence, usage and source match
    -> publish immutable review report to approved owner-controlled destination
    -> Codex may *consider* evidence; only authorized integrator may edit/fix
    -> task acceptance/release still blocked on normal S2C risk/QA/A.1/B.1 gates
```

`agent-turn-complete` is only a possible **trigger source** to inspect when an actual Codex version and notify contract are verified; it does not prove task completion. Dispatch only an explicitly marked *completed task checkpoint* with no in-flight writes to the reviewed snapshot. Never enqueue half-written workspace content. The one reviewer may run concurrently with the **next unrelated authorized Codex task**, never with writes to the reviewed snapshot. Guard shared decisions by SHA and an explicit integration barrier.

**Proposed operator defaults (not confirmed CLI options):** 1 reviewer; max diff payload 12 KiB; timeout 120 s; retries 0; max 3–5 high-signal findings; skip unchanged snapshot; escalate to an operator-approved available higher-capability model only on unresolved P0/P1 or low-confidence complex findings; no automatic premium overage. These are *S2C orchestration configuration candidates*, not `agy` flags or a new `.source/.config` schema.

**Proposed provenance:** `reviewId, taskId, sourceSHA, baseSHA, changedPathHashes, diffDigest, policyDigest, requirementsRefs, agyVersion, modelId, observedMode, promptSchemaVersion, CLIExit, CLIStatus, semanticStatus, findings, inputTokens, outputTokens, thinkingTokens, cacheReadTokens, duration, sandboxEvidence, owner, timestamp`. If any mandatory field is missing, label it `UNKNOWN/INCONCLUSIVE` and request evidence; never transform provider output into a valid owner signature.

## 6. Failure handling and risks

- `SUCCESS` + plan-artifact text, code fences without parseable JSON, malformed JSON, missing findings field, unknown SHA, or mismatched evidence → `REVIEW_INCONCLUSIVE`.
- Authentication failure, unknown model, quota, paid-credit request or timeout → `PROVIDER_BLOCKED` without credential extraction, model swapping or uncontrolled retries.
- Host/sandbox failure, Windows junction/reparse/TOCTOU, untrusted prompt tool request or out-of-scope read/write → **STOP/BLOCK**, preserve sentinels, escalate to Security Owner; do not claim tested containment.
- Reviewer suggests a patch, command, release or changes to permissions → treat as **untrusted advice**; only separately authorized Codex integrator may propose edits after checks.
- Source/policy/spec/requirements drift after snapshot → `STALE`, invalidate that review's applicability, require re-capture before gated acceptance.
- No machine config, Codex notify script, CLI wrapper or review service has been added by PLAN-113; current five-phase workflow and source remain unchanged.

## 7. Trace, tests, and next task

Use existing `MM-REQ-003..009`, `MM-TC-03..09`, F38–F42 and risk IDs RM-001, RM-003, RM-025, RM-030, RM-031, RM-041, RM-043, RM-045. The [PLAN-113 test catalogue](../.agents/.workflow/testingAndDelivery.md#plan-113--antigravity-gemini-reviewer-acceptance-design) owns the distinct planned `AGY-TC-01..08` cases; [RTM](../.agents/.traceMatrix.md#plan-113--antigravity-cli-reviewer-evidence-crosswalk) indexes their states.

**Next authorized scope:** operator can repeat *synthetic inline* smoke tests and inspect documented outputs. To make continuous Codex review actually run, request separate B implementation approval *after* independent A.1/security gates, then implement a sandboxed adapter and tests; do not substitute this Markdown file for runtime implementation.

**Not changed:** the canonical master BRD authority, Google Draft mirror, installed-host files, `.source/scripts`, `.source/.config`, `.github/workflows`, actual GitHub Actions, CLI installation or Windows security controls.
