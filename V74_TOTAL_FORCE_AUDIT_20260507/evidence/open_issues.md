# Open issues for 2026-05-07 as of V74 (updated 11:35 VN)

## ✅ Resolved during V74 session

1. **C-05 latency live proof — RESOLVED, was data lag, not broken**
   - Original concern: 0/83 rows had `latency_available` for 2026-05-06 → looked broken.
   - Root cause: V63 instrumentation deployed 2026-05-06 evening (after most live calls had already happened that day). 2026-05-07 is the first full natural cycle with V63 capture.
   - Verified 2026-05-07: **20/42 rows captured** (avg 69.6s, min 6.4s qwen3-coder, max 190.8s gpt-oss-120b). 0 timeouts. Sum tokens 486,665.
   - Remaining 22 rows are NO_TOKEN local ML models (`combo-no-token`, `lstm`, `meta-learning`, `random-forest`, `smart-ensemble`, `smart-ml`, `xgboost`, `combo-super`) — these run as local Python in <1s and don't go through API instrumentation. NOT a bug; expected by design.
   - Action: cron will continue capturing daily; C-16 latency_score will start using real values from 2026-05-07 onwards.

2. **C-17B output_lock_status / readiness_status columns** added to `du_doan_test_bundles` (669 rows backfilled).

3. **C-03 evaluator PENDING** reduced 37 → 9 (residual MN-only for non-closed dates).

4. **CONSENSUS_V1 14d rows** rebuilt (15 anchors).

5. **C-16 budget for 2026-05-07** re-materialized to 20 voters MN/MT/MB.

6. **README stale at V62** rewritten + 6 new GitHub discovery metadata files.

## 🟡 P1 watch (next session or natural cron)

7. **C-05 historical backfill (2026-04-23 → 2026-05-06)**: trace records for those days have `lat=None token=None` (V63 not deployed yet). Cannot recover historical latency, but rolling 14d window will become valid from 2026-05-21 onwards as new days accumulate with V63 capture.

8. **Slow models flagged** by C-05 first day:
   - `gpt-oss-120b` 190.8s
   - `glm-5.1` 184.4s
   - `deepseek-reasoner` 134.4s
   - `gemma-4-31b` 137.0s
   - `qwen3.6-plus` 136.8s
   - `deepseek-v4-pro` 115.2s
   - Action: collect 14 days of latency history, then C-16 latency_score will down-rank them automatically. NO promotion or pruning yet — pure measurement.

9. **CONSENSUS_V1 SKIP for MT/MB on 2026-05-07** (only 2 method agreement at materialization time). Expected to recover after natural closeout when other materializers fire.

## ⏳ Always-on (continuous measurement)

- Daily V66/V67/V70/V73 cron 23:35–23:48 VN.
- Daily evidence pack auto-generation.
- Window gates 7/14/30/60/90/180 days are CHECKPOINTS, not stop points.
- Drift detector materializer to be added in next session (P1 from CONTINUOUS_MEASUREMENT_DOCTRINE §7).

## 📋 Open P0 next session (only 1 left, was 3)

1. Add `test_lane_signal_drift_monitor` materializer (per region per method rolling 7d-vs-30d alert).

(C-05, C-17B, C-03, C-16 budget — all resolved in V74 session)
