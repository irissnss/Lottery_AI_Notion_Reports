# V105.29 — Deploy `_safe_stdio_ctx` wide patch to VPS

## When to run

Owner has already approved Decision #10 in V105.27 OWNER_DECISION_REGISTER. V105.28 + V105.29 confirmed the no-token path is still raising `I/O operation on closed file` on production (111 errors in 14d). Local code now has the module-level fix; smoke test PASS. The patch is ready to deploy.

## What changes

`web/backend/scheduler.py`:

- Promotes `_SafeNullWriter` + `_ensure_safe_stdio` from local scope inside `_start_timed_model_call` to **module-level** helpers.
- Adds a module-level **`class _safe_stdio_ctx`** context manager that swaps unusable stdio with a sink for the wrapped block and restores originals on exit.
- Wraps the no-token entry points so each function body runs inside `_safe_stdio_ctx()`:
  - `_run_free_model_prediction` -> calls `_run_free_model_prediction_inner` inside the context manager
  - `_run_smart_ensemble` -> `_run_smart_ensemble_inner`
  - `_run_smart_ml_ensemble` -> `_run_smart_ml_ensemble_inner`
  - `_run_combo_no_token` -> `_run_combo_no_token_inner`
  - `_rerun_free_models_after_scrape` -> `_rerun_free_models_after_scrape_inner`
- Existing `_start_timed_model_call` now reuses `_safe_stdio_ctx()` — no behaviour change for the AI token path (already worked locally).

**No changes to:** model selectors, scoring, BT logic, source pool, prompt, model roster, MT protect mode, official tables, generate_final_bundle, /du-doan or /api/final-bundle semantics, output eligibility, lane-test gate.

## Pre-deploy verification (already performed locally)

- `python -m py_compile web/backend/scheduler.py` → **PASS**.
- `python artifacts/v10529/_v10529_safe_stdio_smoke.py` → 3/3 PASS (case_A absorbed closed-file print; case_B re-raised real exception; case_C wrapped no-token call returned dict).
- All 5 inner functions exposed for testability.
- Official 4-table pre/post hashes IDENTICAL (`artifacts/v10529/v10529_post_hash.json`).
- Provider/manual AI call count session = **0**.

## Exact deploy steps (run on workstation that has SSH to VPS)

> Workstation must already have SSH key registered with the VPS. Owner has confirmed PAT revoked on GitHub; this is unrelated to the VPS SSH key.

```bash
# 1) Take a timestamped backup on the VPS first.
TS=$(date +%Y%m%d_%H%M%S)
ssh root@vietnix "mkdir -p /root/Lottery_AI_Test/backups/v105_29_safe_stdio_${TS} \
  && cp /root/Lottery_AI_Test/web/backend/scheduler.py \
        /root/Lottery_AI_Test/backups/v105_29_safe_stdio_${TS}/scheduler.py.bak"

# 2) Send the patched scheduler.
scp web/backend/scheduler.py \
    root@vietnix:/root/Lottery_AI_Test/web/backend/scheduler.py

# 3) Compile-check on the VPS using the project venv.
ssh root@vietnix "cd /root/Lottery_AI_Test && \
  /root/Lottery_AI_Test/venv/bin/python -m py_compile web/backend/scheduler.py && \
  echo COMPILE_OK"

# 4) Restart the service.
ssh root@vietnix "systemctl restart lottery.service && sleep 5 && \
  systemctl is-active lottery.service && curl -s http://localhost:8000/api/health"

# 5) Watch the journal for the next ~10 minutes; expect no \"I/O operation on closed file\".
ssh root@vietnix "journalctl -u lottery.service -n 200 --no-pager | grep -E 'closed file|SAFE_STDIO|Re-predict|CASCADE_STAGE'"

# 6) After the next natural MN scrape/verify (16:30 VN), confirm:
#    - MT rerun_post_mn: success=7 failure=0
#    - MB rerun_post_mn: success=7 failure=0
#    - journal has zero \"I/O operation on closed file\" entries.
# After the next natural MT scrape/verify (17:30 VN):
#    - MB rerun_post_mt: success=7 failure=0.
```

## Rollback (if anything goes wrong)

```bash
ssh root@vietnix "cp /root/Lottery_AI_Test/backups/v105_29_safe_stdio_${TS}/scheduler.py.bak \
                     /root/Lottery_AI_Test/web/backend/scheduler.py && \
                  systemctl restart lottery.service"
```

## Post-deploy V105.29 verification

```bash
# Workstation:
python web/_sync_live_forensic_inputs.py
python artifacts/v10529/_v10529_master_audit.py
python artifacts/v10529/_v10529_post_hash.py
```

Expected new state:

- `lane2_stdio.live_evidence.closed_file_error_count_14d` should plateau and **stop growing** after the next MN cascade.
- `lane6_gates.official_15_pass` remains stable (no regression).
- `lane8_formula.mt_d2_leak_7d == 0` and `mb_d2_leak_7d == 0`.
- `all_official_tables_unchanged == true`.

## Owner sign-off

This file documents the deploy. After execution, append a line to `docs/AUTOMATION_HISTORY.jsonl` with the new seq, the backup folder path, the post-restart health snapshot, and the closed_file_count delta.
