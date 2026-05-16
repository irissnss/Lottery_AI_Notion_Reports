# V105.59 / V105.60 Fix Readiness (Public)

Generated: `2026-05-16T23:19:04+07:00`. Diagnostic-only. No official mutation.

| fix_id | class | priority | owner_ok_required | runtime_change |
|---|---|---|---|---|
| H-01 cost persistence | MEASUREMENT_FIX | P0 | yes | no (diagnostic table) |
| H-02 final_bundles schema doc | MEASUREMENT_FIX | P0 | no | no (doc applied) |
| H-03 rules vs prompt doc | MEASUREMENT_FIX | P0 | no | no (doc applied) |
| H-04 selector rank 3-5 trace | DIAGNOSTIC_SELECTOR_REPAIR | P1 | yes | no (diagnostic lane) |
| H-05 MT lane weight replay | DIAGNOSTIC_SELECTOR_REPAIR | P1 | yes | no (replay only) |
| H-06 MN D-2 shadow reactivation | DIAGNOSTIC_SELECTOR_REPAIR | P1 | yes | no (shadow only) |
| H-07 prompt herding A/B | DIAGNOSTIC_SELECTOR_REPAIR | P2 | yes | no (proposal) |
| H-08 PP-1 dampener audit | DIAGNOSTIC_SELECTOR_REPAIR | P2 | no | no (read-only) |
| H-09 MB probation day 2 observer | MEASUREMENT_FIX | P1 | no | no (daily observer) |
| H-10 doc index / Notion routing | MEASUREMENT_FIX | P3 | no | no (doc applied) |
