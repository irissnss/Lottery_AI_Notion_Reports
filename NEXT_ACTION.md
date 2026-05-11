# NEXT ACTION (V105.28 — 2026-05-11 23:38 VN, Runtime Contract Verify)

V105.28 audit closed. Status PARTIAL — not PASS. Official 4-table hash unchanged. No provider/manual AI call. MT protect tuyệt đối.

Next actions:

1. Owner OK deploy `_safe_stdio_ctx` rộng cho no-token rerun path. V105.27 Decision #10 đã có owner OK; V105.28 chứng minh đã hit thật ngày 2026-05-10 (25 lỗi) + 2026-05-11 (86 lỗi). Kế hoạch:
   - Bổ sung context manager `_safe_stdio_ctx` (export hàm `_ensure_safe_stdio`).
   - Wrap `_run_smart_ensemble`, `_run_smart_ml_ensemble`, `_run_combo_no_token`, `_run_free_model_prediction` ở scheduler.
   - `python -m py_compile` local PASS, lints clean.
   - VPS backup `backups/v105_28_safe_stdio_full_path_<ts>/`.
   - scp + `systemctl restart lottery.service` + `/api/health=200`.
   - Watch chu kỳ verify tiếp theo: kỳ vọng MT/MB rerun success 7/7.
2. Owner OK enable scheduler region+weekday strongest-first reorder cho `AUTO_AI_MODELS`. Shadow proposal đã có (`v10528_ai_priority_order_proposal`, 24 buckets). Sau khi áp:
   - KHÔNG bỏ model nào (vẫn 7 token models).
   - Chỉ reorder.
   - Watch 7d hit rate so với static order.
3. Add APScheduler cron 19:30 VN: materialize `model_strength_by_region_weekday_station_daily` daily để tensor luôn tươi (latest anchor hiện 2026-05-05).
4. Owner setup SSH deploy key + `git remote set-url origin git@github.com:...` (HTTPS sẽ fail sau PAT revoke).
5. Daily 00:05 VN snapshot vẫn owner-gated (carry V105.27).
6. Huế canonical, MB_D_v2 scope, V102 relaxed, Top2/Bundler A/B vẫn HOLD theo V105.27 OWNER_DECISION_REGISTER.

Evidence: `V105_28_RUNTIME_CONTRACT_VERIFY_20260511/evidence/V105_28_RUNTIME_CONTRACT_REPORT.md` (sections 8, 14, 15).
