# Open Issues — as of V105.28 (2026-05-11 23:38 VN)

## V105.28 status

- `FU-V105-28-CLOSED-FILE-NO-TOKEN`: OPEN P0. 86 closed_file errors on 2026-05-11 + 25 on 2026-05-10 in MB no-token rerun. `_safe_stdio_ctx` wraps only AI token path in `_start_timed_model_call`. No-token rerun path (`_run_smart_ensemble` / `_run_smart_ml_ensemble` / `_run_combo_no_token` / `_run_free_model_prediction`) needs the same wrap. Owner OK already granted at V105.27 Decision #10; deploy still pending.
- `FU-V105-28-AI-PRIORITY-ORDER`: OPEN P1. Scheduler iterates `AUTO_AI_MODELS` in static registry order. Owner contract requires region+weekday strongest-first reorder. Shadow proposal `v10528_ai_priority_order_proposal` materialized (24 buckets); needs owner OK before scheduler reorder. Strength tensor anchor stale at 2026-05-05; daily refresh cron also pending.
- `FU-V105-28-SSH-DEPLOY-KEY`: OPEN P1. Owner confirmed PAT revoke; git remote still uses HTTPS. SSH deploy key migration required before next push.
- `FU-V105-28-TENSOR-REFRESH-CRON`: OPEN P1. `model_strength_by_region_weekday_station_daily` latest anchor is 6 days old. Add APScheduler cron at 19:30 VN to materialize the tensor daily.

## V105.27 carry-over

- `FU-V105-27-MN-D2-RANKED-PROMPT-WIRE`: PARTIAL/CLOSED-FOR-SHADOW. 137/137 injected; official prompt untouched.
- `FU-V105-27-TOP2-BUNDLER-AB`: OPEN. Shadow only; promotion math not met.
- `FU-V105-27-MB-D-V2-SHADOW`: OPEN/HOLD. `auto_disable=true`. Do not promote.
- `FU-V105-27-NOTION-PAGES`: CLOSED. V105.25/26/27/28 page IDs recorded in `LATEST_REPORT.json`.
- `FU-V105-27-SECURITY-PAT-SSH`: PARTIAL. PAT revoke owner-confirmed; SSH migration still pending.

## Earlier carry-over

- `FU-V105-25-STATION-ALIAS-FIXUP`: CLOSED under canonical target `Thừa Thiên Huế`. Owner naming decision still open if shorthand `Huế` is preferred.
- `FU-V105-24-SOURCE-POOL-FORMULA`: OPEN. V105.27 refreshed miss matrix; MB `SOURCE_FORMULA_EXCLUSION=1052`, MT `=1013`, MN `=898`.
- `FU-V105-24-V104-PROMPT-WIRING`: PARTIALLY CLOSED for MN D-2 ranked top5 shadow only.
- `FU-V105-24-RELAXED-PROMOTION-RULE`: OPEN. Promotion gate >= 14d, save_ratio >= 0.30, break_ratio <= 0.10, net_save > 0, owner OK.

## Measurement risk

V105.28 does not justify any official promotion. Two real gaps remain (closed-stdio deploy + AI priority order) — both are stability/quality fixes that must not touch `predictions`, `final_bundles`, `lottery_results`, `model_daily_eval`, MT source formula, or production prompt content.
