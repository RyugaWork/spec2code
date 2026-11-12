# Requirement-to-Code Traceability — <Feature ID>

| Requirement ID | Approval source/version | AC IDs | Design IDs | Task IDs | Changed code paths | Test IDs/evidence | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <R01> | <approved source> | <AC01> | <DES01> | <T001,T002> | <path/line or symbol> | <command/log> | NOT RUN |

Trace rules:
- Every implemented behavior must map to an approved requirement; every in-scope AC maps to implementation and verification evidence.
- Never treat a technical implementation proposal as authority to add a new business rule.
- Use PASS / FAIL / BLOCKED / NOT RUN, not unverified blanket PASS.
- Record change IDs when requirements, design or code diverge.
