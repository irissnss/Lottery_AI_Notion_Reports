# V54 C-06 — Loz Stage Trace Result

> Status: `LOZ_STAGE_TRACE_DEPLOYED_MEASUREMENT_ONLY`  
> File: `web/backend/_materialize_loz_stage_trace_shadow.py`  
> Table: `loz_stage_trace_shadow`  
> Anchor: 2026-05-03 (closed day, no 2026-05-04 result used)

## What It Does

For each actual tail in each region/day, trace whether the actual tail:

- appeared in any model output;
- appeared in final bundle candidate pool;
- had candidate rank/score;
- reached official lo2;
- was dropped before final output.

## Drop Labels

- `FINAL_OUTPUT_HIT`
- `NOT_IN_MODEL_OUTPUT`
- `CANDIDATE_POOL_MISS`
- `LOZ_LINE_SELECTION_MISS`
- `MODEL_TOP10_ONLY`
- `BUNDLE_PROMOTION_DROP`

## VPS Backfill Summary

Backfilled 60 closed days through 2026-05-03: 180 date-region jobs.

Rows by region/drop stage:

| Region | NOT_IN_MODEL_OUTPUT | LOZ_LINE_SELECTION_MISS | CANDIDATE_POOL_MISS | FINAL_OUTPUT_HIT |
|---|---:|---:|---:|---:|
| MN | 2229 | 221 | 105 | 59 |
| MT | 1807 | 182 | 90 | 52 |
| MB | 1204 | 121 | 73 | 31 |

## Interpretation

- MT has 182 cases where an actual tail was in candidate pool but line selection missed it.
- MB has fewer total misses than MN/MT because MB actual tail rows are fewer in this 60d set, but its final-output hit rate remains weak.
- `NOT_IN_MODEL_OUTPUT` dominates everywhere, meaning many actual tails are not present in top model outputs at all; this prevents simplistic loz policy swaps.

## Safety

- Reads only `final_bundles`, `predictions`, `lottery_results`.
- Writes only `loz_stage_trace_shadow`.
- Does not call `generate_final_bundle()`.
- Does not mutate official output.
