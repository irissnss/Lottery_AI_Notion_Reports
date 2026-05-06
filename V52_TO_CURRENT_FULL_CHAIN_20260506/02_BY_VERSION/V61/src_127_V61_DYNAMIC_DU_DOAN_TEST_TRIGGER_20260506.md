# V61 — Dynamic `/du-doan-test` pre-result trigger

**Date:** 2026-05-06 07:55 VN  
**Scope:** scheduler test-lane automation + dynamic model ordering clarification  
**Official impact:** none

---

## Owner issue

Owner reported that the experiment still had not run on 2026-05-06 and clarified that execution order must be dynamic by `region + weekday + station-set`, not static by model list.

---

## Live state before fix

Synced manifest:

`artifacts/live_sync/20260506_074923/manifest.json`

At 07:49 VN:

### MN

- `predictions`: 15 official `auto_daily` + 13 `shadow_auto_eval`
- `final_bundles`: exists, BT=`95`, lo2=`[95,46]`
- `lottery_results`: 0 rows (pre-result)
- `du_doan_test_*`: 0 rows
- `experimental_preview_shadow`: 0 rows
- C-16 budget: 0 rows

### MT / MB

- only no-token `auto_daily` rows existed
- no official final bundle yet
- no test rows yet

Verdict: Owner was correct. `/du-doan-test` had not auto-run for MN even though it was ready.

---

## Immediate action

Manually ran MN pre-result lane:

```bash
python _materialize_du_doan_test_model_budget.py --date 2026-05-06 --region MN --json
python _du_doan_test_daily_runner.py --date 2026-05-06 --region MN --mode REALTIME_AVAILABLE_ONLY --json
```

Result:

- C-16 budget: pool 29, measured 28, selected 10, watch 18, skipped 1
- station-set inferred for MN bucket:
  - Cần Thơ
  - Sóc Trăng
  - Đồng Nai
  - Khánh Hòa
  - Đà Nẵng
- test lane: 7 runs / 7 bundles / 7 results / 164 candidates / 164 model contributions
- actual rows still 0, so status remains PENDING, no post-result leakage

Current MN test output:

```text
MN_ADAPTIVE_BUDGET_SELECTOR_V1: test_bt=95, official_bt=95, lo2=[95,46], status=PENDING
```

---

## Dynamic trigger implemented

`web/backend/scheduler.py`

Added:

`_run_du_doan_test_pre_result_trigger(trigger_source="interval")`

It runs every 5 minutes and checks each region independently:

1. final bundle exists for today/region
2. predictions exist (`preds >= 7`)
3. target-region actual results do **not** exist yet
4. no `du_doan_test_bundles` exist yet for today/region

Only when all are true:

1. materialize C-16 budget
2. run V52.5.6 test runner in `REALTIME_AVAILABLE_ONLY`
3. write only test/diagnostic tables

Scheduler job:

```text
id="du_doan_test_pre_result_trigger"
name="🧪 /du-doan-test pre-result readiness trigger (5m)"
CronTrigger(minute="*/5")
```

VPS log:

```text
Shadow Auto-Eval: completion-triggered (no CronJob) — 13 models per region
/du-doan-test pre-result trigger: every 5 minutes, readiness-gated
Added job "🧪 /du-doan-test pre-result readiness trigger (5m)"
```

---

## Dynamic model order

No-token models already run first through the existing 04:00 all-region batch.

For shadow token models, V60 ordering remains:

1. C-16 rows for date/region if available
2. latest strength tensor fallback if C-16 not available
3. registry fallback if both unavailable

This makes Monday/Tuesday/station-set differences automatic because C-16/tensor bucket is date+region+weekday+station-set aware.

---

## Verification

```text
systemctl is-active lottery = active
/api/health = 200
manual trigger verification = OK
```

Synced manifest after deploy:

`artifacts/live_sync/20260506_075455/manifest.json`

---

## Remaining caveat

This is now true pre-result automation, but it still depends on official final bundle readiness per region.

Expected sequence:

- MN: after morning official bundle + shadow rows complete
- MT: after MT final bundle exists later today
- MB: after MB final bundle exists later today

The trigger is readiness-gated, not hardcoded to a static clock.

