> **Public-safe report.** No private code, no DB rows, no provider keys, no raw VPS detail. Numbers shown are summary-only aggregates from V106.36 read-only audit. No official mutation occurred.



# V10636 PHASE 1 — FRESH SYNC FREEZE

- ts_vn: `2026-05-27T22:49:23`
- sync_manifest: `e:[REDACTED]artifacts\live_sync\latest_manifest.json`
- sync_status: `ok`
- db_sha256: `f22958a62658a6ec71bde5fb413e969cae8102d0f02189f90055139f6c1d11d5` size=321,343,488
- trace_sha256: `98557ca9dedf33cfdc7ad07933a7cfaa3dc849983750a54f08d232f9f302a1f8` size=10,606,484
- tables_total: 164

## Key table counts

| Table | Count |
|---|---|
| `predictions` | 6116 |
| `final_bundles` | 267 |
| `lottery_results` | 14759 |
| `model_daily_eval` | 5980 |
| `du_doan_test_bundles` | 1490 |
| `du_doan_test_results` | 1490 |
| `experimental_preview_shadow` | 1836 |
| `mined_rules` | 105 |
| `candidate_drop_stage_daily` | 143 |
| `shadow_daily_comparison` | 219 |
| `strongest_vs_final_conversion_daily` | 143 |
| `runtime_reliability_daily` | 258 |
| `runtime_reliability_model_daily` | 1714 |
| `cohere_effectiveness_daily` | 121 |
| `freshness_chain_daily` | 707 |
| `lane_test_active_challenger_scoreboard` | 1557 |
| `lane_test_lose_only_audit_daily` | 90 |
| `lane_test_region_profiles` | 3 |
| `shadow_method_scoreboard` | 30732 |
| `shadow_candidates` | 7747 |
| `shadow_activation_registry` | 18 |
| `official_vs_testlane_rescue_daily` | 72 |
| `rule_overlay_pre_register` | MISSING |
| `shadow_rule_d1_comparison` | 123 |
| `mb_experimental_preview_shadow` | 189 |
| `rule_conversion_loss_stage_daily` | 97 |

## Latest dates

| Table | Date col | Max date | Rows @ 2026-05-27 |
|---|---|---|---|
| `predictions` | date | 2026-05-27 | 83 |
| `final_bundles` | date | 2026-05-27 | 3 |
| `lottery_results` | date | 2026-05-27 | 6 |
| `model_daily_eval` | date | 2026-05-27 | 83 |
| `du_doan_test_bundles` | run_date | 2026-05-27 | 39 |
| `du_doan_test_results` | run_date | 2026-05-27 | 39 |
| `experimental_preview_shadow` | date | 2026-05-27 | 29 |
| `candidate_drop_stage_daily` | date | 2026-05-27 | 3 |
| `shadow_daily_comparison` | date | 2026-05-27 | 3 |
| `strongest_vs_final_conversion_daily` | date | 2026-05-27 | 3 |
| `runtime_reliability_daily` | date | 2026-05-27 | 6 |
| `runtime_reliability_model_daily` | date | 2026-05-27 | 39 |
| `cohere_effectiveness_daily` | date | 2026-05-27 | 3 |
| `freshness_chain_daily` | date | 2026-05-27 | 21 |

## Region counts today (2026-05-27)

| Table | Region counts |
|---|---|
| `lottery_results` | {"MB": 1, "MN": 3, "MT": 2} |
| `final_bundles` | {"MB": 1, "MN": 1, "MT": 1} |
| `predictions` | {"MB": 28, "MN": 27, "MT": 28} |
| `model_daily_eval` | {"MB": 28, "MN": 27, "MT": 28} |
| `experimental_preview_shadow` | {"MB": 10, "MN": 10, "MT": 9} |
| `candidate_drop_stage_daily` | {"MB": 1, "MN": 1, "MT": 1} |
| `shadow_daily_comparison` | {"MB": 1, "MN": 1, "MT": 1} |
| `strongest_vs_final_conversion_daily` | {"MB": 1, "MN": 1, "MT": 1} |
| `du_doan_test_bundles` | {"MB": 7, "MN": 18, "MT": 14} |
| `du_doan_test_results` | {"MB": 7, "MN": 18, "MT": 14} |

## Mined rules audit (live DB)

```json
{
  "count_by_region": {
    "MB": 35,
    "MN": 35,
    "MT": 35
  },
  "count_by_activation_status": {
    "active": 99,
    "shadow": 6
  },
  "count_by_production_tier": {
    "LIMITED_WEIGHT": 59,
    "READY_STRONG": 10,
    "READY_WITH_CAUTION": 36
  },
  "active_by_region_weekday": [
    {
      "region": "MB",
      "weekday": 0,
      "n": 5
    },
    {
      "region": "MB",
      "weekday": 1,
      "n": 5
    },
    {
      "region": "MB",
      "weekday": 2,
      "n": 5
    },
    {
      "region": "MB",
      "weekday": 3,
      "n": 5
    },
    {
      "region": "MB",
      "weekday": 4,
      "n": 5
    },
    {
      "region": "MB",
      "weekday": 5,
      "n": 5
    },
    {
      "region": "MB",
      "weekday": 6,
      "n": 5
    },
    {
      "region": "MN",
      "weekday": 0,
      "n": 5
    },
    {
      "region": "MN",
      "weekday": 1,
      "n": 5
    },
    {
      "region": "MN",
      "weekday": 2,
      "n": 5
    },
    {
      "region": "MN",
      "weekday": 3,
      "n": 5
    },
    {
      "region": "MN",
      "weekday": 4,
      "n": 5
    },
    {
      "region": "MN",
      "weekday": 5,
      "n": 5
    },
    {
      "region": "MN",
      "weekday": 6,
      "n": 5
    },
    {
      "region": "MT",
      "weekday": 0,
      "n": 5
    },
    {
      "region": "MT",
      "weekday": 1,
      "n": 5
    },
    {
      "region": "MT",
      "weekday": 2,
      "n": 5
    },
    {
      "region": "MT",
      "weekday": 3,
      "n": 5
    },
    {
      "region": "MT",
      "weekday": 4,
      "n": 5
    },
    {
      "region": "MT",
      "weekday": 5,
      "n": 5
    },
    {
      "region": "MT",
      "weekday": 6,
      "n": 5
    }
  ]
}
```