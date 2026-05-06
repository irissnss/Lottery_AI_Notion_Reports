# V52.2 Measurement Backfill Rollup

> Date: 2026-05-03  
> Mode: VPS-first / measurement-only / 60 closed-day backfill / no official mutation  
> Live sync after run: `artifacts/live_sync/20260503_214559/manifest.json`

## What Ran

Updated `web/backend/_materialize_v52_measurement_surfaces.py` with `--backfill-days`.

VPS command:

```bash
python web/backend/_materialize_v52_measurement_surfaces.py --date 2026-05-03 --backfill-days 60 --json
```

## Row Counts

- `mt_model_hit_output_drop_shadow`: `301`
- `loz_selector_shadow`: `3273`
- `model_latency_cost_audit_daily`: `3273`

## Hash Guard

Pre: `artifacts/_v52_2_pre_hash_20260503.txt`  
Post: `artifacts/_v52_2_post_hash_20260503.txt`

Official/source unchanged:

- `predictions`: `4134 -> 4134`, hash unchanged
- `final_bundles`: `195 -> 195`, hash unchanged
- `lottery_results`: `14603 -> 14603`, hash unchanged
- `model_daily_eval`: `4089 -> 4089`, hash unchanged
- `scheduler_logs`: `113122 -> 113122`, hash unchanged

## Key Rolling Findings

### MT Drop Matrix

60d:

- `LOZ_LINE_SELECTION_MISS`: 115 rows, 184 model hits, mostly no-token (177).
- `AI_SIGNAL_DROPPED`: 112 rows, 282 model hits, 195 token + 73 shadow.
- `NOT_IN_CANDIDATE_UNIVERSE`: 50 rows.
- `OFFICIAL_LO2_INCLUDED`: 24 rows.

30d:

- `LOZ_LINE_SELECTION_MISS`: 61 rows.
- `AI_SIGNAL_DROPPED`: 55 rows.
- `NOT_IN_CANDIDATE_UNIVERSE`: 35 rows.
- `OFFICIAL_LO2_INCLUDED`: 15 rows.

This is now more than a one-day observation. It is enough for deeper measurement/UI/test-lane work, not enough for official scoring changes by itself.

### Loz Selector Shadow

30d model-top2 vs official:

- MB: model better `122`, official better `156`, rows `652`.
- MN: model better `113`, official better `211`, rows `650`.
- MT: model better `140`, official better `198`, rows `646`.

14d:

- MT model better `107`, official better `81`, rows `366`.

Interpretation: loz signal is strongly window/region conditional. It is not ready for a fixed official loz rule, but it is ready for UI/test-lane surfacing and continued shadow scoring.

### Latency / Cost

All 3273 rows still have:

`NO_PER_MODEL_DURATION,NO_COST_ESTIMATE,NO_TOKEN_COUNT`

Model pruning remains blocked.

## Final Verdict

V52.2 exhausted the immediately available historical data for the new measurement surfaces. The next safe work is UI/test-lane surfacing and latency instrumentation; official output remains locked.
