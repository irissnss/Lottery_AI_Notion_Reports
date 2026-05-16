# Open Issues — V105.60 Controlled Public Sync

## P0 measurement (no official mutation)
- `H-01` Cost persistence diagnostic table: tokens / cost not yet recorded; MB cost-gate decision is blocked. Owner OK required.
- `H-02` `final_bundles` schema documentation: no `verified_station_count` column; documentation must clarify schema introspection. Doc fix applied locally.
- `H-03` Rules-in-prompt clarification: mined rules do not flow through the prompt body since V17.6.27. Doc fix applied locally.

## P1 selector blindspot (diagnostic-only)
- `H-04` Selector rank 3-5 trace: actual tails at model rank 3+ are dropped by the top-2 cap; diagnostic lane proposed.
- `H-05` MT lane weight asymmetry: `rerun_post_mn=1.15` and `ai_chain=0.95` may amplify herd; replay study proposed.
- `H-06` MN D-2 shadow trace reactivation: D-2 lane absent today.
- `H-09` MB probation day 2 of 3: red flag carried from day 1 (clone_rate ~85.71%, would_save=0).

## P2 prompt / rule audit (diagnostic-only)
- `H-07` MT and MB prompt-induced herd: A/B diagnostic lane proposed.
- `H-08` PP-1 convergence dampener audit: confirm whether the 0.85x dampener blocked rescue tails 81, 19, 12.

## P3 sync
- `H-10` Public mirror was stale at V105.41; this release brings it to V105.60. Notion sync remains pending owner OK.

## Hard-lock invariants honored
- No official prompt/scoring/selector/voting/roster/cron/timeout change.
- No provider/manual AI call.
- No accuracy/promotion claim.
- Public push uses an external clone of the public mirror; the private workspace is not pushed.
