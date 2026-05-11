# V105.23 Token-Cost / Once-Daily Guard Audit

Status: **read-only audit, no provider/manual AI call**.

## Guard Flags

Defined in `scheduler.py`:

- `OWNER_MANUAL_PROVIDER_CALLS_ENABLED`: default `0`; manual provider/shadow paths are closed unless explicitly enabled.
- `OWNER_STARTUP_SHADOW_CATCHUP_PROVIDER_ENABLED`: default `0`; startup shadow catch-up provider recovery is closed.
- `OWNER_AI_TOKEN_ONCE_DAILY_ONLY`: default enabled; repeated token/provider AI batch is blocked per date/region.

## Manual Provider / Shadow Lock

Enforced paths:

- `scheduler.run_now(region)` logs `MANUAL_RUN_NOW_BLOCKED` and returns when owner manual gate is off.
- `scheduler.run_shadow_eval_now(region)` returns blocked payload when owner manual gate is off.
- `main.py` `POST /api/scheduler/run-now/{region}` returns HTTP 423 when owner manual gate is off.
- `main.py` `POST /api/scheduler/shadow-eval-now` returns HTTP 423 when owner manual gate is off.

Runtime proof:

- Current VPS process scan matched no manual/provider process.
- Current VPS PID journal scan hit count was 0 for `Traceback`, `I/O operation on closed file`, `AI Predict Job triggered`, `SHADOW_COMPLETION_TRIGGER`, `[API] Attempt`, `KEY_MODE`, `MANUAL_PROVIDER`.

## Once-Daily Guard

`scheduler._run_ai_predict_job(target_region, run_source)`:

- Checks `OWNER_AI_TOKEN_ONCE_DAILY_ONLY`.
- Calls `_owner_ai_token_attempt_exists(date_str, target_region)`.
- Blocks with `[AI_ONCE_DAILY_BLOCK]` when an attempt marker or token prediction rows already exist.
- Logs `[AI_ONCE_DAILY_ATTEMPT]` before executing a natural batch.

`_owner_ai_token_attempt_exists()` checks:

- `scheduler_logs` for `[AI_ONCE_DAILY_ATTEMPT]%` with same date/region/job.
- `predictions` rows where `ai_model` is in `model_registry.TOKEN_MODELS`.

## Save Guard

`database.save_prediction()`:

- Existing verified row with `WIN`, `LOSE`, or `PARTIAL` returns without overwrite.
- TOKEN-class model with existing same `(date, target_region, ai_model)` returns without overwrite.
- Token models force DD Sau routing and do not create DD Trước/cuốn-chiếu duplicate token saves.

## Startup / Completion Trigger

Startup:

- `_startup_catch_up()` can trigger scraper/update catch-up for missing results.
- Partial shadow recovery only calls provider when `OWNER_STARTUP_SHADOW_CATCHUP_PROVIDER_ENABLED=1`.
- When disabled, it logs `SHADOW_CATCH_UP_BLOCKED_OWNER_LOCK`.

Completion-triggered shadow:

- `_run_ai_predict_job()` may trigger `_run_shadow_auto_eval` only after natural production batch completion.
- Fully complete shadow rows are skipped.
- Partial rows are not refilled by default; owner lock prevents token refill.

## Known Gaps / Risks

These are not current provider calls, but are code-risk surfaces for follow-up:

- Admin `POST /api/predict/MN|MT|MB` paths are admin-gated but not gated by `OWNER_MANUAL_PROVIDER_CALLS_ENABLED`; duplicate persistence guard still protects existing TOKEN rows, but this is not the same as global one-batch lock.
- If `model_registry.TOKEN_MODELS` cannot load, scheduler once-daily DB-row check weakens and relies more on attempt markers.
- `auto_daily` relies on once-daily marker + TOKEN rows; SQL duplicate guard is stronger for `ai_chain`/`fallback`.
- Admin delete paths could remove prediction rows; scheduler markers still help natural path, but manual predict paths should be owner-gated in V105.23 follow-up.

## Conclusion

Current runtime evidence is clean and no provider/manual AI verification was run. Token-cost guard is materially present, but V105.23 should add owner-lock to manual `/api/predict/{region}` paths to remove the remaining admin bypass risk.
