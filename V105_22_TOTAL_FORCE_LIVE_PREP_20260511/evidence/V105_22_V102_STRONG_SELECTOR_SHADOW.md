# V105.22 V102 STRONG Selector Shadow

Generated: 2026-05-11T08:59:39+07:00

Safety scope: lane-test / shadow / diagnostic only. No production scoring, selector, bundle voting, official prompt, official roster, `generate_final_bundle()`, `/du-doan`, or `/api/final-bundle` mutation.

Hash guard pre/post for the V105.22 live-prep deploy and access-log stability fix is identical for the four official evidence tables:

```json
{
  "predictions": {
    "rows": 4739,
    "sha256": "a3a6022eda6fadcf244f7b429091d5d6d0a1946d8816ce1266e6fc14584a1b2c"
  },
  "final_bundles": {
    "rows": 217,
    "sha256": "105ed85c01defb3c6407dff87f7ede426afd3f54f137981aeeb6d80ece2aadcf"
  },
  "lottery_results": {
    "rows": 14649,
    "sha256": "379b7b51587bf5c8e2d5fac206099bc2b7ee3fd4feb2fbd68f57a1e230911e87"
  },
  "model_daily_eval": {
    "rows": 4572,
    "sha256": "3f71c595ee87b620182e0f2f28949f33de9916c489dc635167ff066a3e0e6517"
  }
}
```


Method: `V105_21_V102_STRONG_TO_SELECTOR_SHADOW`.

Status from latest materialization:

- `v10522_v102_strong_selector_shadow`: 0 rows for the 30-day target window at this run.
- This is not promoted and does not mean disabled globally. It means no candidate passed the strict V105.22 gate for materialized rows in this run.
- MN and MB profiles keep V102 shadow/forensic enabled; MT remains measure-only/protect.

Acceptance status: official hash unchanged; no MT primary selector alteration; no official table write.
