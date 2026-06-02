# V10677 — Đợt 1: Cap "đánh mạnh" + MB switched + Post-draw settle (CP-66.7 unblocked)

Public-safe report. No private endpoints, no IP, no internal paths.

## 1. Why these three changes tonight

After today (2026-06-02) saw all 3 regions miss BT, the owner approved a small "wave 1" in order C → B → A (low-risk first, harder last) to stabilize the system gradually rather than ship one big change.

## 2. C — Cap "high-confidence" recommendation when 10-day BT win-rate < 35%

A new region-level guard inside the slice recommendation module: if the regional BT win-rate over the last 10 days is below 35%, any "CAO/đánh mạnh" tier for that region is automatically downgraded to "TRUNG_BINH/đánh vừa", with a transparent note in the reason field.

Live verification just after deploy:
- MB Quảng Ninh: confidence=72 → was CAO → now TRUNG_BINH (MB 10-day BT = 0%)
- MT Quảng Nam: confidence=80 → was CAO → now TRUNG_BINH (MT 10-day BT = 20%)
- MN unaffected (10-day BT = 60%, well above threshold)

This is UI/display only — does not change vote logic, does not touch any model. Display still shows the underlying confidence value so the owner can see why it was capped.

## 3. B — MB BT chooser switched: hot30 → D_w06

Data justification:
- 92-day backtest: hot30=23%, D_w06=24% (+1 pp)
- Recent 30-day: hot30=10%, D_w06=23% (+13 pp recent gap)
- hot30 has been on a 1/21 = 5% streak with 11 consecutive losses.

The D_w06 chooser (top1×1.0 + top2×0.6 weighted aggregation, leveraging the secondary number) was already deployed for MN earlier today (V10676). It is region-agnostic, so this change is a one-line config flip — no new code. Today's MB bundle had already been written this afternoon with the old hot30 (BT=24, lost), so the new chooser takes effect tomorrow's MB cycle.

The hot30 code path is kept intact — rollback is one line.

## 4. A — Post-draw settle (the long-blocked CP-66.7 fix)

Background: a deep dive showed 8 of 10 experiments in the test-lane preview table had `actual_known=0` permanently — only CONSENSUS_V1 and HYBRID_V1 ever closed. Reason: their materializers run BEFORE the draw and write `actual_known=0`; there was no back-fill job after the draw to update them. This blocked CP-66.7 (the 14-day live verification of ADAPTIVE_EXPLOIT_V1) since 2026-05-21 (deadline) with `closed_days = 0` for all three regions.

V10677 is a small standalone script that runs daily at 19:00 (after the last region scrape ~18:30). It scans pending rows in the last 21 days, joins read-only with the lottery results table, and updates only three columns on the preview table: `actual_known`, `candidate_bt_hit`, `candidate_lo2_status`. It does not touch any of the four official prediction tables.

First manual run after deploy: 503 rows scanned, 503 rows settled, 0 errors. CP-66.7 evidence (now available retroactively):

| Experiment | Closed | Hits | Hit-rate |
|---|---|---|---|
| MN_ADAPTIVE_EXPLOIT_V1 | 24 | 13 | **54%** |
| MT_ADAPTIVE_EXPLOIT_V1 | 23 | 10 | **43%** |
| MB_ADAPTIVE_EXPLOIT_V1 | 24 | 5 | 21% |

MN and MT cleared the 14-closed-days requirement of CP-66.7. CP-66.8 (evidence pack) can now be auto-built. Importantly, ADAPTIVE_EXPLOIT_V1 was NOT a flop — its 54% MN hit-rate exceeds the current MN selector (45-48%).

## 5. Verification (no risk to live data)

- All 4 official prediction tables: hash IDENTICAL pre vs post deploy (zero drift).
- The preview-table `actual_known=1` count grew from 1356 to 1859 (+503 rows correctly settled).
- Service active, login + health endpoints return 200.
- Service log post-restart: no error / traceback / failure.
- py_compile PASS for all 3 changed files on local and on the production server.
- Linter: 0 errors.

## 6. Rollback paths

Each of the three changes has its own one-line rollback:
- C: revert the slice recommendation file from the saved `.pre` copy
- B: change MB chooser back to "hot30" or "specialist" (both old code paths are preserved untouched)
- A: disable the new cron line, or restore the saved crontab snapshot

A backup folder containing the pre-deploy file copies and the crontab snapshot was taken at 22:40, before any change.

## 7. What changes for the owner from tomorrow

- T4 04:00: MN AI predict + bundle uses D_w06 (V10676, second day live).
- T4 17:42: MB AI predict + bundle uses D_w06 (first day live for MB).
- T4 19:00: V10677 post-draw settle runs the first natural cron — closing today's 30 pending rows automatically going forward.

I will surface the result each morning for 7 days.

## 8. Status

`PUBLIC_SAFE` — no IP, no internal paths, no provider keys, no DDL exposed, no private repo references.
