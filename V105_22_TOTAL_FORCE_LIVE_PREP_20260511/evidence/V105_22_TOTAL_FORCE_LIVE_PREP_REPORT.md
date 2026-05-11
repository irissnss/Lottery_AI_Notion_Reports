# V105.22 Total Force Live-Prep Report

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


## Version Matrix

- Private repo: `Lottery_AI_Test`, VPS head `ceb36c2`, local working tree contains many pre-existing dirty files; V105.22 touched `web/backend/_v10522_live_prep.py`, `web/backend/main.py`, `web/frontend/monitoring.html`, plus docs/reports.
- Public repo: advanced to `V105.22` in `Lottery_AI_Notion_Reports/V105_22_TOTAL_FORCE_LIVE_PREP_20260511`.
- Notion: created under root `Lottery_AI_Test`: `V105.22 — Region-Independent Lane Test Live Prep` (`35d1d385-9bf8-8177-8926-f7c17bb56fe0`), `V105.22 — MN Priority / MT Protect / MB Forensic Strategy` (`35d1d385-9bf8-8106-b94a-e777a575cc1a`), `V105.22 — Tomorrow Live Readiness Checklist` (`35d1d385-9bf8-818f-8ffa-d700ad9f0d5f`).
- VPS runtime: `lottery.service` active after restart; `/api/health=200`, `/api/status=200`, `/du-doan=200`, `/api/final-bundle` MN/MT/MB=200; `/du-doan-test` and `/api/admin/v10522-live-prep` return 401 unauth as expected.
- Drive: local Drive exports from prior V104 ingest were available; Folder 2 status remains `DRIVE_FOLDER_2_EMPTY_OR_NO_ACCESS` unless connector content is later provided.

## Runtime Evidence

- Remote compile: `python3 -m py_compile web/backend/main.py web/backend/_v10522_live_prep.py` passed.
- V105.22 materializer: profiles=3, coverage rows=3076, source-prize rows=3076, rule contract rows=3076, lose-only rows=90, MB forensic rows=30, station identity audit rows=69.
- Current lane probe for `2026-05-11`: MN=`READY 20/20`; MT=`PREVIEW_BELOW_BUDGET 4`; MB=`PREVIEW_BELOW_BUDGET 5`. This is intentionally not mislabeled as all-region main-ready.
- Access-log closed-stream incident found and fixed by running uvicorn with `access_log=False`; current PID journal sample after restart shows no repeated access-log closed-stream traceback.

## Safety Result

PASS for official safety: official hashes unchanged; only shadow/test tables and read-only admin/UI surfaces were created or updated.

CAUTION for live readiness: morning lane state is region-specific. MN is ready at 20/20; MT/MB remain preview until their regional source/model quota becomes available.
