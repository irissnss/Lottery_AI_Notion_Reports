# Open issues for 2026-05-07 as of V74 audit

## P0 fix-now flagged
1. **C-05 latency live proof**: 0/83 model_latency_cost_audit_daily rows since 2026-05-06 have latency_available=1.
   - Status: P0_BROKEN_NEEDS_FIX
   - Cause: instrumentation deployed but live model calls have not been captured properly yet.
   - Action: schedule investigation in next session (touches gpt_analyzer; deploy outside live window).
   - Risk: blocks pruning/timeout decisions.

2. **C-17B output_lock_status** column was missing on `du_doan_test_bundles`.
   - Status: FIXED (V74 added column + backfilled 669 rows; READY_PRE_RESULT_LOCKED 39, POST_CLOSEOUT_DIAGNOSTIC_ONLY 569, NOT_READY_NO_PICK 61).

3. **C-03 PENDING rows** in `du_doan_test_results`.
   - Status: REDUCED 37 → 9 (V74 backfill 14 dates ALL regions). Remaining 9 rows are MN-only for future/non-closed dates.

4. **CONSENSUS_V1 14d table empty** at start of V74 audit.
   - Status: FIXED (V74 re-backfilled 15 anchors; 30+ rows now present). Cause unknown (suspect manual cleanup during V72 cycle).

## P1 watch
5. **README stale on public repo** (mentions V62 "latest").
   - Status: FIXING in V74 — README rewrite + new `LATEST_REPORT.json` + `REPORT_INDEX.md` + `CHANGELOG_PUBLIC.md` will be primary discovery surfaces.

6. **C-16 budget for 2026-05-07 was at 15** at start of audit; re-materialized to 20 in V74. Cron will keep this stable from 2026-05-08 onwards.

7. **CONSENSUS gate rejected MT/MB 2026-05-07** (only 2 methods agreed) — natural early-day state, expected to recover post-closeout when other materializers run.

## Always-on (continuous measurement doctrine)
- Daily V66/V67/V70/V73 cron 23:35–23:48 VN.
- Daily evidence pack will be produced (this session bootstrap).
- Window gates 7/14/30/60/90/180 days are CHECKPOINTS, not stop points.
- Drift monitor required for next session.
