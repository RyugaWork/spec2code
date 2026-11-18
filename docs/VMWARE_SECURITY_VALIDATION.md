# S2C VMware Workstation Pro / Windows 11 security validation — PLAN-115

**DESIGN_ONLY; vmrun/VM/host/ACL/CI experiments NOT_RUN.** [Canonical F01–F64 RTM](../.agents/.traceMatrix.md#w-plan-115--cross-feature-relationship-and-orphan-edge-audit-2026-11-16), [PLAN-112 host security packet](../.agents/.handoffs/plan-112-a1-security-owner-packet.md). No command is authorized by this documentation alone.

## Trust boundary and architecture

GPT/Codex may propose a task manifest and review redacted logs, but do not receive arbitrary host shell, VMware Administrator or guest credentials. An approved S2C Local Controller pins one approved VMX, an allowlisted operation and immutable Git SHA. A separate evaluator controls out-of-checkout canaries/ACL/OS audit. Guest test actor runs as a non-admin user on synthetic data. GitHub-hosted CI handles static/unit/mock tests. A future local controller may use outbound polling of **signed and approved** task manifests, not an unrestricted self-hosted runner for a public repo or inbound VMware API. Gemini is optional read-only reviewer, not VM executor or approver.

## Mandatory command verification before any execution or code

| Gate | Check | Required result |
| --- | --- | --- |
| CMD-01 | Installed VMware Workstation build and exact `vmrun.exe` help/version | `-T ws` and each operation verified on installed release; otherwise STOP |
| CMD-02 | Absolute binary path, signer, SHA-256, directory ownership, PATH/cwd shadowing | Trusted pinned executable; discovery alone is not authentication |
| CMD-03 | Approved VMX path and ownership, snapshot/Tools, physical root, no foreign mount | Approved identity and effect scope; otherwise STOP |
| CMD-04 | Typed operation+argv allowlist, no shell string, unknown flags, injection or secret-bearing arguments | Deny unknown commands and alternate VMX |
| CMD-05 | Side effects: read-only vs start/stop vs snapshot/revert vs guest process vs host share | Independent approval for every mutable or privileged class |
| CMD-06 | Separate Windows user tokens and evaluator canary, ACLs, disconnected guest network, disabled shared-folder/clipboard/drag/drop/USB | Real OS denial evidence, not a prompt-only rule |
| CMD-07 | Deadline/attempt limit, job/process cancellation, independent log/evidence, recovery | Preserve evidence outside snapshot revert, STOP on P0 |

Read-only discovery sample (never starts VMware operations; version/capability still unverified on user's host):

```powershell
$ErrorActionPreference = 'Stop'
$candidates = @(Get-Command vmrun.exe -CommandType Application -All -ErrorAction SilentlyContinue)
if ($candidates.Count -eq 0) { Write-Output 'VMRUN_NOT_FOUND'; return }
$candidates | Select-Object Source
$path = $candidates[0].Source # discovery only; production requires pinned approved binary
Get-Item -LiteralPath $path | Select-Object FullName,Length,@{Name='FileVersion';Expression={$_.VersionInfo.FileVersion}}
Get-AuthenticodeSignature -LiteralPath $path | Select-Object Status,SignerCertificate
Get-FileHash -LiteralPath $path -Algorithm SHA256 | Select-Object Algorithm,Hash
```

Never directly execute `vmrun start`, `snapshot`, `revertToSnapshot`, `runProgramInGuest`, `enableSharedFolders`, `deleteSnapshot` or power-off on a real VM until installed CLI syntax, VMX owner, guest side effects and approved preservation rules have been tested. Do not embed guest passwords in process argv or logs. Host-only networking still reaches a host boundary; prefer disconnected guest networking for hostile tests. A protected canary inside the same guest is not evidence of hypervisor containment.

## Controlled workflow

`VM-G0 TASK/SHA/POLICY → VM-G1 READ-ONLY CLI CHECK → VM-G2 EVALUATOR ISOLATION → VM-G3 APPROVED CLEAN SNAPSHOT → VM-G4 BOUNDED TEST → VM-G5 PROTECTED EVIDENCE → VM-G6 INDEPENDENT OWNER DECISION → VM-G7 AUTHORIZED RESTORE/QUARANTINE`.

On missing ACL/isolation, source drift, actual outside-root read/write, unexpected VMX/host mapping, untriggered race, timeout or unavailable tool, record `BLOCKED/FAIL/INCONCLUSIVE` as appropriate, STOP and handoff. Snapshot does not grant permission to erase guest state. Preserve logs/canaries/audit before any revert; one VM writer at a time; retries have a fixed bound.

## Task dependency and acceptance mapping

| Task | Output | Status |
| --- | --- | --- |
| VM-01 | Discover installed vmrun/VM build | NOT_RUN |
| VM-02 | Host/guest/evaluator threat model | DESIGN |
| VM-03 | Guest isolation profile and negative share checks | DESIGN |
| VM-04 | Typed command allowlist and hash-bound manifest | DESIGN |
| VM-05 | Mock adapter/negative tests after scoped B | NOT_AUTHORIZED |
| VM-06 | Real ACL/canary/evaluator proof | T112-05 BLOCKED_HOST |
| VM-07 | Approved snapshot/retention experiment | NOT_RUN |
| VM-08 | Run existing L1-SC01-A/B/C, L1-SC02-A, L1-SC03-A on synthetic guest | T112-06 NOT_RUN |
| VM-09 | Security Owner review of RM-001 | T112-08 BLOCKED_OWNER |
| VM-10 | Independent A1-VAL-01..09 and CI integration decision | T112-09 NOT_RUN |

Each execution envelope must record exact Git SHA, VMX/guest build, vmrun path/hash/help, argv, accounts/ACL, fixture, actual race trigger, before/after canary and independent read audit, exit/stdout/stderr, deadline/retries, sanitized result, evidence hash, risk and reviewer. A matching hash alone does not prove no secret read. A race that never triggers is INCONCLUSIVE. Actual tests are in [testingAndDelivery](../.agents/.workflow/testingAndDelivery.md#plan-115--vmware-host-and-command-case-matrix).

## Reference boundary

- [GitHub — security hardening for GitHub Actions](https://docs.github.com/en/actions/reference/security/secure-use)
- [GitHub — self-hosted runner overview](https://docs.github.com/en/actions/hosting-your-own-runners)
- [Microsoft Windows Job Objects](https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects)
- [Microsoft icacls](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/icacls)
- Actual installed VMware/Broadcom CLI syntax and feature support must be cross-checked against vendor documentation and executable help before use. Neither command compatibility nor OS containment was tested here.

**Gate state:** RM-001 P0 OPEN 20/25, A_REWORK_REQUIRED, A1_NOT_RUN, B_NOT_AUTHORIZED, B1_NOT_RUN.
