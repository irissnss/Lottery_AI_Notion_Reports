# Open issues — V77 audit (updated 2026-05-07 18:55 VN)

## ⚠️ Active P1 — needs owner monitoring

1. **MN OFFICIAL 0/4 cold streak (last 4 days 2026-05-04..05-07)**
   - Confirmed real (not bug). MN official BT missed 65, 15, 95, 94 over 4 days.
   - V73 saved MN today (95 ✅). V67 EXPLOIT was the source.
   - Watch: if MN official remains 0 for 7+ days, escalate to P0 regime-shift investigation.

2. **MB OFFICIAL 0/4 cold streak (last 4 days 2026-05-04..05-07)**
   - Confirmed real. MB official BT missed 09, 83, 79, 20.
   - ALL test methods 0/N also (V73, V70, V67, C16). MB is in deep cold.
   - Watch: if MB stays cold 7+ more days, escalate to P0. May need weekday-specific model rotation in MB.

## ✅ Resolved during V77 session

3. **V70/V73 timing bug** — V70 cron at 23:45 fired before daily test runner populated pool → consensus_v1 always emitted agreement=1 → no consensus row → V73 fell back to V67-only.
   - Root cause: cron timing mismatch with `/du-doan-test` runner (which fires MN=04:30, MT=16:45, MB=17:45 VN dynamically).
   - Fix: V77-1 added cron 19:00 VN re-running V70+V73 for `target_date=today` AFTER all 3 region runners complete. Original 23:45/23:48 cron retained for tomorrow-target prep.
   - Verified: backfill of 4 days × 3 regions with full pool → V70 hit MT 4/4, V73 would_save = 1 vs OFFICIAL.

4. **VPS schema regression** — `du_doan_test_bundles` was missing `output_lock_status` and `readiness_status` columns (V74 fix had not persisted on VPS).
   - Fix: V77-4 added both columns and backfilled 685 existing rows with `POST_CLOSEOUT_DIAGNOSTIC_ONLY`.

5. **Fast incident monitor missing** — V76 drift detector requires n30 ≥ 10 (~14 fresh days) to settle, no immediate signal for 4-day patterns.
   - Fix: V77-2 added `test_lane_fast_incident_monitor` table + materializer + cron 19:05 VN. 5 alert classes (RED_FAST/ORANGE_FAST/YELLOW_FAST/EXPLOIT_FAIL_FAST/BUDGET_FAIL_FAST). Alert-only.

6. **C-03 evaluator residual PENDING** — re-ran for 4 days × 3 regions, all backfilled.

## 🟡 P1 watch (next session or natural cron)

7. **C-05 historical backfill** — V63 deployed 2026-05-06 evening; historical days before that have `lat=None`. Cannot recover but rolling 14d valid from 2026-05-21 onwards.

8. **V67 EXPLOIT thin sample** — only 3 picks across 3 regions (1/3 hit rate). V67 needs more days of lag-1 BOOST data to evaluate properly.

9. **Slow models flagged** by C-05 (V76):
   - `gpt-oss-120b` 190.8s, `glm-5.1` 184.4s, `deepseek-reasoner` 134.4s, etc.
   - Action: 14 days of history needed before any down-rank decision. NO pruning yet.

10. **MT V67 single failure today** — V67=95 missed, OFFICIAL=88 hit. Single-source signal not enough for MT (V67 has 0/1 for MT).

## ⏳ Always-on (continuous measurement)

- Daily V66/V67/V70/V73 cron 23:35–23:48 VN.
- **NEW V77 cron 19:00 + 19:05 VN** (post-cascade rerun + fast incident).
- V76 drift cron 23:50 VN (alerts active after 2026-05-21).
- Daily evidence pack auto-generation.
- Window gates 7/14/30/60/90/180 days are CHECKPOINTS, not stop points.

## 📋 Open P0 (escalation gate)

11. **MB cold streak escalation** — if MB OFFICIAL remains 0/N for 7+ more days (i.e., 11+ total), trigger forensic root-cause investigation with:
    - Per-weekday hit rate analysis for MB
    - Model class breakdown (TOKEN vs NO_TOKEN) in MB
    - Comparison of MB regime pre-2026-05-04 vs post-2026-05-04
    - Possible mitigation: weekday-specific model rotation
    - Owner gate: any selector or model roster change requires owner OK
