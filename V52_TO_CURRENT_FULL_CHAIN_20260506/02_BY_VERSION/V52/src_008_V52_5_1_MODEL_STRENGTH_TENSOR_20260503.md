# V52.5.1 Model Strength Tensor

> Date: 2026-05-03  
> Mode: measurement-only / no official mutation  
> Anchor date: 2026-05-02 (yesterday relative to test target 2026-05-03)  
> Live sync after run: `artifacts/live_sync/20260503_225849/manifest.json`  
> VPS backup: `/root/Lottery_AI_Test/backups/v52_5_1_20260503_2300/` (code + 61 MB DB)

## Goal

Provide a runtime-usable model strength snapshot keyed by `model × region × weekday × station × run_source` so V52.5.x test-lane methods can apply strength-weighted aggregation without leakage.

## Files

- `web/backend/_compute_model_strength_tensor.py` — standalone materializer.

## Schema

```sql
CREATE TABLE model_strength_by_region_weekday_station_daily (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  computed_at TEXT NOT NULL,
  anchor_date TEXT NOT NULL,
  window_days INTEGER NOT NULL,        -- 7, 14, 30, 60
  grain TEXT NOT NULL,                 -- region | region_weekday | region_station
  model_name TEXT NOT NULL,
  model_family TEXT,                   -- TOKEN | NO_TOKEN | SHADOW
  region TEXT NOT NULL,
  weekday INTEGER NOT NULL DEFAULT -1, -- -1 means "all weekdays"
  station TEXT NOT NULL DEFAULT '',    -- '' means "region-level"
  run_source TEXT NOT NULL DEFAULT '', -- '' means "all run_sources"
  total_days INTEGER, predictions_count INTEGER,
  bt_hit_count INTEGER, loz1_hit_count INTEGER,
  loz2_hit_count INTEGER, any_hit_count INTEGER,
  bt_rate REAL, loz1_rate REAL, loz2_rate REAL, any_rate REAL,
  helpful_signal_strength REAL,        -- 0.6*bt_rate + 0.4*loz2_rate
  test_only INTEGER DEFAULT 1,
  output_eligible INTEGER DEFAULT 0,
  diagnostic_only INTEGER DEFAULT 1,
  run_label TEXT NOT NULL,
  UNIQUE(anchor_date, window_days, grain, model_name, region,
         weekday, station, run_source, run_label)
);
```

## Run

VPS command:

```bash
python web/backend/_compute_model_strength_tensor.py --target-date 2026-05-03 --json
```

Result: `9052` rows for anchor `2026-05-02` across 4 windows × 3 grains.

Counts by grain × window:

| Grain | 7d | 14d | 30d | 60d |
|---|---:|---:|---:|---:|
| region | 81 | 101 | 151 | 197 |
| region_weekday | 523 | 589 | 697 | 1104 |
| region_station | 1047 | 1180 | 1380 | 2002 |

## Sample Findings (window=30d, grain=region)

TOKEN family:
- MN top: `combo-super auto_daily` BT `17/30`, helpful `0.5933`; `claude-sonnet-4-6 auto_daily` BT `16/27`, helpful `0.563`.
- MT top from auto_daily: `combo-super` BT `4/10` (rolling sample is thinner because of MT cascade behavior).
- MB top from `ai_chain`: `claude-sonnet-4-6` helpful `0.2815`, BT `8/27`. AI MB is structurally weaker than MN here.

NO_TOKEN family:
- MN top: `smart-ensemble auto_daily` BT `18/30`, `meta-learning auto_daily` BT `18/29`, `combo-no-token auto_daily` BT `19/29`.
- MT top from `rerun_post_mn`: `smart-ml` BT `15/28`, helpful `0.4929`.
- MB top from `rerun_post_mt`: `random-forest` BT `9/28`, helpful `0.3357`.

SHADOW family:
- MN: `glm-5.1 shadow_auto_eval` BT `11/18`, helpful `0.5889`.
- MB: `llama-4-maverick`/`mistral-large-3` shadow_auto_eval BT `3/4` each (sample thin).

## Hash Guard

Pre: `artifacts/_v52_5_1_pre_hash_20260503.txt`  
Post: `artifacts/_v52_5_1_post_hash_20260503.txt`

| Table | Pre | Post | Hash same |
|---|---:|---:|---|
| predictions | 4134 | 4134 | YES |
| final_bundles | 195 | 195 | YES |
| lottery_results | 14603 | 14603 | YES |
| model_daily_eval | 4089 | 4089 | YES |
| scheduler_logs | 113162 | 113162 | YES |
| mt_model_hit_output_drop_shadow | 301 | 301 | YES |
| loz_selector_shadow | 3273 | 3273 | YES |
| model_latency_cost_audit_daily | 3273 | 3273 | YES |
| model_strength_by_region_weekday_station_daily | 0 | 9052 | new |

Official + V52 measurement tables unchanged.

## Verdict

V52.5.1 produces a clean, leakage-safe runtime tensor anchored at `D-1`. V52.5.2 will generalize the experimental preview materializer to multi-region using this tensor.
