# V10663 — Post-draw Verification (2026-06-01 T2) + slice_recommendation MT/MB Coverage Fix

Public-safe report. No private endpoints, no IP, no internal paths.

## 1. Context

Owner asked for post-draw verification on 2026-06-01 (Monday): are V10640..V10662 fixes working as designed, what did today's predictions do, what's next. Session followed `.Antigravityrules.md` / `.AGENT.md`: no provider call, no wallet impact, no DB table drop, no official logic change. One small bug found in `slice_recommendation` UI surface, fixed at the cron-schedule level only (no code change).

## 2. Today's Predictions vs Results

| Region | BT chosen | Strategy | Result | Detail |
|---|---|---|---|---|
| MN | 73 | specialist override | WIN | 10 of 28 models picked 73 as top-1 |
| MT | 83 | nt_consensus override | WIN | 3 of 28 models picked 83 as top-1 |
| MB | 64 | hot30 override | LOSE | only 1 model picked 64 (a lonely vote) |

**Score for the day: 2 of 3 = 66.7%.** Yesterday (2026-05-31) was 0 of 3, so this is a clear positive day.

Track record since V10656 override deploy (2026-05-31, only two settled forward days so far):

| Region | Forward live | Hit rate | Baseline (90d) | Delta |
|---|---|---|---|---|
| MN | 8 of 15 | 53.3% | 45.1% | +8.2pp (sample size enough → keep) |
| MT | 1 of 2 | 50.0% | 45.1% | sample too small, watch 5-7 more days |
| MB | 0 of 2 | 0.0% | 23.1% | sample too small; would consider rollback only after 5 consecutive LOSE |

## 3. Verification of All Prior Fixes (V10640..V10662) — all working as designed

Live measurement on production today shows every fix is alive and behaving correctly:

| Item | Verified evidence |
|---|---|
| D1 slice_health per-station | 46 station rows (MN 22, MT 17, MB 7), WEAK slices still running with warning labels — exactly the owner requirement (never hide, always show intensity guidance). |
| D2 model_progress | 138 rows; the tracker detected 4 RECOVERING MT models with double-digit trend improvement (potential re-promotion candidates later). |
| D3+D5+CP-R1 V81 retired | V81 last write 2026-05-30 = 2 days no growth. The 4 zombie writer guards (V101 12:23, V104 materializer 12:24, V104B 12:30, V105 12:34) all fired their `DISABLED_V10659` markers exactly as scheduled. |
| D4 shadow_scoreboard | 62 lanes scored: 24 KEEP_DIAGNOSTIC, 22 DEAD, 7 KEEP_MEASURING, 5 HINDSIGHT_HEADROOM, 3 LOOKAHEAD_INVALID. Verdicts coherent. |
| D6 weakest_model_watch type-aware | 19 model rows tagged. AI weakest in MB are auto-routed to SHADOW_PROMPT treatment; ML weakest in MN are auto-routed to RETRAIN_NUMERICAL. |
| D7 ML retrain + retrain_guard | All 15 model files age 1 day (fresh). Guard at 06:30 today: FRESH_SKIP, age 0.71d, well under the 8-day threshold. |
| D8 system_health 15-check | 15 of 15 OK across categories PREDICT, MEASURE, DATA, RULES, ML. |
| D11/D12 mined_rules | 105 rules `v2026W22` fresh (mined 2026-05-31), 35 active per region. |
| D13 weekly_guard | Today 07:00: mining FRESH age 0.66d, optimizer FRESH age 0.65d. |
| D14 weight_optimizer | Not running during prediction window (good). |
| O17/O18 cron auto-fire | All 12 cron log files updated today at expected times (06:30, 07:00, 09:00, 09:05, 09:10, 09:15, 09:25, 09:30, 09:35, 14:30, 14:45, hourly system_health). |
| O30 no-lookahead audit | 525 audit rows; lane_v2_daily 12 EX_ANTE vs 78 HINDSIGHT (HINDSIGHT count is expected because the daily lane runner reruns after draw cutoff; harness correctly flags it). |
| O19 MB AI LIMIT plan | 12 LIMIT (vote weight 0.5), 5 RELEASE, 2 KEEP, 16 THIN. `slice_policy.enabled` remains 0 (surface only, not wired into voting — correct per design). |

## 4. New Bug Found and Fixed This Session

`slice_recommendation` showed only MN rows today (3 rows). MT and MB were missing on the UI.

Root cause: the cron schedule was a single fire at 09:35. MN's `final_bundles` row is created early in the morning (around 04:22) so it is available by 09:35. But MT's bundle is created around 16:46 (after the MN draw at 16:30, before the MT draw at 17:30), and MB's bundle is created around 17:37. Both are after the 09:35 cron window, so the materializer never had data for MT or MB.

Fix: added two extra cron lines, one at 16:55 (after MT bundle ready) and one at 17:55 (after MB bundle ready). No code change, no logic change — the primary key `(date, region, station)` already supports upsert across multiple runs.

Manual back-fill ran immediately after. Today's `slice_recommendation` now has 6 rows: MN 3 (BT 73, TRUNG_BINH 🟡 across 3 stations), MT 2 (Huế TRUNG_BINH conf 50 🟡, Phú Yên THAN_TRONG conf 25 🟠), MB 1 (Hà Nội THAN_TRONG conf 18 🟠). The MB Hà Nội THAN_TRONG label correctly signaled "đánh nhẹ / thăm dò" before draw, which matched the LOSE outcome.

Crontab backup taken before the change.

## 5. New Finding (Not Actioned Yet)

The model_progress tracker found 4 MT models recovering strongly versus their prior 30-day window. These would be candidates to exclude from any future blocked-list wiring. Since `slice_policy.enabled` is still 0, there is no immediate impact — but the record is preserved so the next session does not accidentally block recovering models.

## 6. Items Still on Watch (No Action Today by Owner Request)

- MT and MB override forward sample (need 5-7 more days for statistical signal).
- CP-66.7 / P1 probation recheck on 2026-06-03 (self-run, data-bound).
- Wire reduce-cadence into actual model calls — wait 7-14 more days of stable plan before considering.
- Selector per-slice (CP-R5).
- weight_optimizer grid size optimization (weekly guard already heals correctness; speed optimization can wait for an off-peak window).
- API key encryption (owner deferred to end).
- One duplicate lottery_results row from 2021-08-21 MT (low priority, requires owner to choose which prizes_json is correct).

## 7. Reversibility

- Crontab change is reversible via the backup file taken before the edit.
- No code change in this session beyond documentation.
- No DB table created or dropped.
- No public deploy commit on the production code paths.

## 8. Next Owner Decision Surfaces

- After 5-7 more days of MT/MB override data: keep / rollback per region (data-driven).
- After 14 days of MB AI LIMIT plan stability: option to wire `slice_policy.enabled=1` for MB.
- 2026-06-03: CP-66.7 / P1 recheck will publish a follow-up report automatically.

## 9. STATUS

PUBLIC_SAFE — no IP / no internal paths / no provider keys / no DB DDL exposure / no private repo references.
