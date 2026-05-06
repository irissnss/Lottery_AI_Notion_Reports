# V52 Measurement-Only Implementation

> Date: 2026-05-03  
> Mode: VPS-first / measurement-only / no official mutation  
> Live sync after run: `artifacts/live_sync/20260503_213854/manifest.json`

## Scope

Implemented one standalone materializer:

- `web/backend/_materialize_v52_measurement_surfaces.py`

It writes only:

- `mt_model_hit_output_drop_shadow`
- `loz_selector_shadow`
- `model_latency_cost_audit_daily`

It does not call `generate_final_bundle()` and does not write `final_bundles` or production `predictions`.

## VPS Run Result

Command:

```bash
python web/backend/_materialize_v52_measurement_surfaces.py --date 2026-05-03 --json
```

Result:

```json
{
  "date": "2026-05-03",
  "run_label": "v52_measurement_2026-05-03",
  "mt_model_hit_output_drop_rows": 5,
  "loz_selector_rows": 75,
  "model_latency_cost_rows": 75,
  "official_output": false,
  "output_impact": false,
  "output_eligible": false
}
```

## Hash Guard

Pre: `artifacts/_v52_impl_pre_hash_20260503.txt`  
Post: `artifacts/_v52_impl_post_hash_20260503.txt`

Official/source tables unchanged:

- `predictions`: 4134 -> 4134, hash unchanged
- `final_bundles`: 195 -> 195, hash unchanged
- `lottery_results`: 14603 -> 14603, hash unchanged
- `model_daily_eval`: 4089 -> 4089, hash unchanged
- `scheduler_logs`: 113122 -> 113122, hash unchanged

Measurement tables changed as expected:

- `mt_model_hit_output_drop_shadow`: 0 -> 5
- `loz_selector_shadow`: 0 -> 75
- `model_latency_cost_audit_daily`: 0 -> 75

## Immediate Findings

MT dropped actual-hit tails on 2026-05-03:

| Tail | Drop stage | Model hits | Token | No-token | Shadow | Candidate rank |
|---|---|---:|---:|---:|---:|---:|
| `08` | `AI_SIGNAL_DROPPED` | 5 | 2 | 0 | 3 | 10 |
| `18` | `LOZ_LINE_SELECTION_MISS` | 2 | 0 | 2 | 0 | 3 |
| `43` | `LOZ_LINE_SELECTION_MISS` | 1 | 0 | 1 | 0 | 6 |
| `63` | `LOZ_LINE_SELECTION_MISS` | 1 | 0 | 1 | 0 | 9 |
| `65` | `AI_SIGNAL_DROPPED` | 7 | 1 | 0 | 6 | null |

Loz selector shadow:

- MN: model-top2 better than official `0/25`; official better `8/25`
- MT: model-top2 better than official `15/25`; official better `0/25`
- MB: model-top2 better than official `1/25`; official better `16/25`

Latency/cost audit:

- `75/75` rows still missing duration, cost, and token count.
- Current pruning label remains `PRUNING_NOT_ALLOWED_NO_LATENCY`.

## Final Verdict

This is a real measurement-only implementation. It gives actionable MT/loz/model-cost evidence without any official output mutation.
