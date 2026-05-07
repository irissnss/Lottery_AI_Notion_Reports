# READ THIS FIRST — V77 Post-Closeout Incident Audit (2026-05-07)

## Context

Owner báo: dự đoán hôm nay rất tệ, MN đã tệ 4 ngày liên tục, MB cũng tệ. Yêu cầu emergency audit sau chu kỳ xổ số 2026-05-07 đã kết thúc.

Đây là post-closeout incident audit + root cause analysis + safe test-lane fix, KHÔNG chạm production.

## TL;DR — One-Paragraph Summary

V77 đã chạy emergency audit sau khi 3 miền MN/MT/MB đã closeout 2026-05-07. **Owner verdict đúng cho MN và MB**: OFFICIAL **MN 0/4 ngày**, **MB 0/4 ngày** trong 4 ngày liên tiếp 2026-05-04..05-07 — đây là cold streak có thật (regime shift), KHÔNG phải lỗi hệ thống. **MT vẫn ổn**: OFFICIAL 4/4 ngày perfect. Audit phát hiện 1 lỗi timing trong test-lane: V70 CONSENSUS cron 23:45 thực tế fire lúc 01:50 VN (delayed) — TRƯỚC khi daily `/du-doan-test` runner ghi BUDGET/AI_CHAIN/SPECIALIST/NO_TOKEN_HERD picks → V70 chỉ thấy 1 vote V67 → `agreement_count=1` < `MIN_AGREEMENT=3` → không có consensus row → V73 HYBRID fallback về V67-only → MT hôm nay V73=95 ❌ trong khi consensus thật ra là 88 ✅. Sau backfill với pool đầy đủ: V70 hit MT 4/4 last 4d; V73 would-save=1 (MT today) would-break=0 vs OFFICIAL. **V77 đã deploy** 2 cron mới: (1) 19:00 VN re-run V70+V73 sau khi MB runner xong, (2) 19:05 VN fast incident monitor (5 alert classes RED_FAST/ORANGE_FAST/YELLOW_FAST/EXPLOIT_FAIL_FAST/BUDGET_FAIL_FAST). 2026-05-07 alerts: 5 RED_FAST (đa số là MB cold) + 1 BUDGET_FAIL_FAST + 9 GREEN. Hash 4 official tables UNCHANGED.

## Files in this package

| File | Purpose |
| ---- | ------- |
| `READ_THIS_FIRST.md` | This file — TL;DR & navigation |
| `V77_REPORT.md` | Full incident audit (15 sections, all owner-required tables) |
| `REPORT_MANIFEST.json` | Machine-readable manifest (paths, hashes, key metrics) |
| `evidence/4d_regression_table.md` | 4-day per-region per-method hit table |
| `evidence/v70_v73_timing_root_cause.md` | Detailed timing bug analysis |
| `evidence/fast_incident_alerts_20260507.md` | All 15 fast-incident alerts |
| `evidence/v77_audit_output.txt` | Raw audit log |
| `evidence/v77_backfill_log.txt` | Raw backfill log |

## What's the action item?

**For owner (read order):**

1. Read `V77_REPORT.md` Section 1 (Owner Verification) and Section 2 (4-Day Regression Table).
2. Read Section 5 (Root Cause: V70/V73 Timing Bug) for the technical fix.
3. Read Section 9 (Action Plan) for what to expect tomorrow at 19:00 VN.

**For the agent (next session):**

- 2026-05-08 19:00 VN cron should fire and produce a CONSENSUS row with `agreement_count >= 3` for MN/MT/MB.
- 2026-05-08 19:05 VN cron should fire and write fast incident alerts.
- Verify in `journalctl -u lottery -n 100 | grep V77`.

## Hard locks (verified)

- ✅ NO mutation to `predictions`, `final_bundles`, `lottery_results` (only natural growth).
- ✅ NO mutation to `generate_final_bundle()`, scoring, voting, model roster, prompts.
- ✅ V77 jobs marked `test-lane only` and `alert-only`. `auto_rollback_triggered=0` enforced.
- ✅ V70/V73 cron timing change is purely additive (new 19:00 + 19:05 jobs); 23:45/23:48 jobs retained for tomorrow-target prep.
