# V57 — C-16 Adaptive Model Budget Selector for `/du-doan-test`

**Date:** 2026-05-05 23:00 VN  
**Scope:** test-lane/admin-only model budget selector + UI/API surface  
**Owner intent:** Use all measured components as the pool, but choose the strongest daily voter subset by region/weekday/station to reduce future runtime/token cost while preserving official output.

---

## What changed

### Backend materializer

Added `web/backend/_materialize_du_doan_test_model_budget.py`.

It creates/writes only:

- `du_doan_test_model_budget_daily`
- `du_doan_test_selected_voters`
- `du_doan_test_model_skip_reason`

It does not call `generate_final_bundle()` and does not mutate:

- `final_bundles`
- production `predictions`
- `lottery_results`
- `model_daily_eval`
- official scoring/voting/model roster/prompt/scheduler

### API

Added `_build_du_doan_test_model_budget_summary(region, date_str)` in `web/backend/main.py`.

Both `/api/du-doan-test/mb` and `/api/du-doan-test/{region}` now include:

```json
{
  "model_budget": {
    "status": "READY",
    "budget": {...},
    "selected_voters": [...],
    "watch_only": [...],
    "skipped": [...],
    "controls": [...]
  }
}
```

### UI

Added `/du-doan-test` section:

**“🧠 Model mạnh hôm nay / C-16 Adaptive Budget”**

Shows:

- total pool count
- measured pool count
- selected voters
- watch-only
- skipped today
- station-set / weekday bucket
- model score decomposition
- today's pick and status

---

## C-16 selection logic

The selector ranks the full registry-visible measured pool, excluding non-prediction utility entries.

### Pool

`total_pool_count = 29`

This includes:

- official output-eligible TOKEN/NO_TOKEN/ENSEMBLE components
- SHADOW_AUTO models, including the V55 Google direct cohort
- registered prediction-compatible measurement components where applicable

### Bucket

Per date/region:

```text
region + weekday + station_set + output_type=BT
```

### Grain fallback

The selector chooses the strongest available tensor grain:

1. `region_station` if station sample >= 5
2. `region_weekday` if weekday sample >= 5
3. `region` if region sample >= 10
4. `NO_BUCKET_SAMPLE` otherwise

### Scoring weights

```text
final_budget_score =
  0.55 * strength_score
  + 0.15 * recent_score
  + 0.10 * unique_score
  + 0.10 * region_penalty_score
  + 0.10 * latency_score
```

Notes:

- `latency_score` is currently neutral `0.50` when C-05 latency is missing.
- MB generic AI gets a small structural penalty.
- herd/duplicate/hurt signals from test-lane contribution penalize the unique score.
- A minimum budget fill ensures each region has at least 8 selected voters if there are measured candidates.

### Roles

- `CONTROL`: diversity floor controls (best token/output, best no-token, best ensemble, best shadow).
- `SELECTED_VOTER`: included in the experience/test voter set.
- `WATCH_ONLY`: visible and measured, not selected today.
- `SKIP_TODAY`: low bucket score or no bucket sample/prediction.

---

## VPS materialization result (2026-05-05)

```text
MN: pool=29 measured=28 selected=10 watch=16 skip=3 control=4
MT: pool=29 measured=28 selected=8  watch=14 skip=7 control=4
MB: pool=29 measured=28 selected=8  watch=10 skip=11 control=4
```

### MN selected highlights

- `gpt-oss-120b` CONTROL score 0.5885, pick `[52,41]`, PARTIAL
- `glm-5.1` SELECTED score 0.5860
- `qwen3.6-plus` SELECTED score 0.5495, pick `[52,13]`, PARTIAL
- `combo-super` CONTROL score 0.5176, station-grain sample 5, pick `[52,69]`, PARTIAL
- `lstm` CONTROL, pick `[18,32]`, PARTIAL

### MT selected highlights

- `smart-ml` CONTROL score 0.4898, pick `[08,44]`, WIN
- `combo-no-token` SELECTED score 0.4492, pick `[44,31]`, PARTIAL
- `lstm` CONTROL score 0.4475, pick `[46,09]`, PARTIAL
- `gpt-oss-120b` CONTROL score 0.4463, pick `[52,46]`, WIN
- `grok-4.20-multi-agent` SELECTED score 0.4418, pick `[52,46]`, WIN

### MB selected highlights

- `lstm` CONTROL score 0.4970
- `gpt-5-mini` CONTROL score 0.4757, pick `[71,09]`, PARTIAL
- `deepseek-reasoner` SELECTED score 0.3911, pick `[98,67]`, PARTIAL
- `qwen3.6-plus` CONTROL score 0.3774, pick `[91,14]`, WIN
- `random-forest` SELECTED score 0.3333

Important: `gemini-3-flash` is surfaced in Experience Mode as a shadow win today. C-16 did not auto-select it yet because it lacks tensor history; it remains watchable until more samples arrive.

---

## Verification

### Compile/lint

- `py_compile`: OK for `main.py`, `_du_doan_test_schema.py`, `_materialize_du_doan_test_model_budget.py`
- Lints: no blocking errors (Edge Tools warns about existing inline style only)

### VPS backup

`/root/Lottery_AI_Test/backups/c16_model_budget_20260505_2248/`

Contains:

- `main.py.bak`
- `_du_doan_test_schema.py.bak`
- `du-doan-test.html.bak`

### VPS smoke

```text
systemctl is-active lottery = active
/api/health=200
/du-doan-test unauth=401
/api/du-doan-test/mn unauth=401
/api/final-bundle?region=MN=200
```

### Live sync

`artifacts/live_sync/20260505_230032/manifest.json`

---

## Current limitations

1. C-05 latency is still missing, so latency/cost penalties are neutral. This means C-16 cannot yet be used as a true cost-optimizer.
2. New shadow models with 1-day signal are visible but need tensor history before becoming selected voters automatically.
3. Official output remains unchanged.

---

## Phase 2 completed: C-16 now creates test output rows

After the initial budget surface was verified, C-16 was promoted inside the
**test lane only** as a real experiment method:

`{REGION}_ADAPTIVE_BUDGET_SELECTOR_V1`

This writes a candidate row into `experimental_preview_shadow` and then the
existing V52.5.3 engine materializes it into `du_doan_test_bundles` and
`du_doan_test_results`.

### 2026-05-05 adaptive test output

```text
MB | MB_ADAPTIVE_BUDGET_SELECTOR_V1 | test_bt=41 | official_bt=83 | test_bt_status=LOSE | would_save=0 | would_break=0
MN | MN_ADAPTIVE_BUDGET_SELECTOR_V1 | test_bt=52 | official_bt=15 | test_bt_status=WIN  | would_save=1 | would_break=0
MT | MT_ADAPTIVE_BUDGET_SELECTOR_V1 | test_bt=52 | official_bt=44 | test_bt_status=WIN  | would_save=0 | would_break=0
```

Interpretation:

- MN: C-16 would have rescued official miss on 05/05 (`52` hit).
- MT: C-16 chose `52` while official `44` also won. This is a divergent hit, not a proof to replace official.
- MB: C-16 chose `41`, still missed; MB remains weak.

New per-region `du_doan_test_*` rows were created:

- MN: +1 run/bundle/result, +20 candidates/contributions
- MT: +1 run/bundle/result, +16 candidates/contributions
- MB: +1 run/bundle/result, +16 candidates/contributions

No official tables were touched.

---

## Next step

After 2-3 days of C-16 rows:

1. Add a C-16 experiment method, e.g. `ADAPTIVE_BUDGET_SELECTOR_V1`, to `experimental_preview_shadow`.
2. Use only `SELECTED_VOTER` rows to build the challenger candidate set.
3. Compare against official/test existing methods.
4. Keep as `/du-doan-test` only until 14/30-day proof.

---

## Verdict

`C16_ADAPTIVE_BUDGET_TEST_OUTPUT_READY`

The `/du-doan-test` output now has both:

1. a daily model budget layer showing which models/components are strong enough for the bucket, and
2. an actual `ADAPTIVE_BUDGET_SELECTOR_V1` test method producing BT/lo2 challenger rows.

This is the correct foundation for reducing AI runtime/token cost later without affecting `/du-doan`.
