# V10666 — Cron MN Timing Fix + Safety Guard + Verify Lane Test / Timezone / Cross-Region

Public-safe report. No private endpoints, no IP, no internal paths.

## 1. Owner concerns after V10665

After completing the 3-region AI LIMIT triad (V10665), the owner raised 3 deep questions:

1. **Vote risk**: could auto-cron limit planners break the total output UI if vote code reads `slice_policy.blocked_models_json`?
2. **Cron timing**: cron MN AI LIMIT at 09:32 is not aligned with MN predict at 04:00. Useful for day D?
3. **Date semantics + observed pattern**: D/D-1/D-2 quy ước có chuẩn không? Has any timezone bug caused predictions to be marked LOSE in region A while the same number won in region B same day, or LOSE day D while it won day D+1?

This session verifies all 3 with read-only data analysis, fixes the 2 actionable items (A + C), and creates a single source of truth document for date / timezone semantics.

## 2. Verification — vote does NOT read `slice_policy`

Grep audit on the production code path:

- `generate_final_bundle` (official `/du-doan`) filters models via `model_registry.get_output_eligible_ids` (15 canonical models with `output_eligible=True`) + a BT/WR gate using live 30-day rates. It does NOT read `slice_policy.blocked_models_json` anywhere.
- Lane test `/du-doan-test` reads from `experimental_preview_shadow` (a separate measurement table) materialized 3 minutes after each region's predict. It does NOT read `slice_policy` either. Empirical: 23 distinct real ai_model used across last 3 days (not 25 as the owner remembered — likely confusion with the ~24 method/experiment count).
- The 3 AI LIMIT planners (`_v10662_mb_ai_limit.py`, `_v10664_mt_ai_limit.py`, `_v10665_mn_ai_limit.py`) only WRITE the `slice_policy.<region>.blocked_models_json` as an advisory surface with `enabled=0`. No vote-side code reads them.

→ **Auto-cron limit changes have ZERO impact on today's official output or lane-test output.** Independent of the per-region limit planners.

## 3. Action A — Cron MN AI LIMIT moved 09:32 → 03:50

MN predictions are created at 04:00 every day. The previous schedule at 09:32 ran 5+ hours AFTER predictions, so its blocked-list refresh could not influence day D — it only mattered for day D+1.

Moved to 03:50, which is 10 minutes BEFORE MN predict starts at 04:00, so the refresh is available for day D the moment predictions begin. MT and MB cron stay at 09:31 and 09:30 because their predict windows are 16:38 and 17:30 respectively — those 09:xx cron times are safely ahead of their predict windows.

Crontab backup taken before the change.

## 4. Action C — Safety guard added to all 3 planners (MB/MT/MN)

Added a safety condition to the `_refresh_slice_policy` function of each planner: if the corresponding `slice_policy.<region>.enabled=1` (owner has wired the policy into vote), the planner REFUSES to overwrite `blocked_models_json`. The owner has full control once wired; planner self-disables to avoid clobbering owner intent.

Tested live: set MB `enabled=1` + manual list `["owner-manual-1","owner-manual-2"]` → run mb planner → output `slice_policy_updated=False enabled=1 blocked_count=2`. Verified list preserved verbatim. Then restored original state. Safety guard working as designed.

## 5. Verification — no timezone bug affecting predictions

200 random recent predictions checked for consistency between `date` field and the VN-time portion of `created_at`: **0 mismatches**. Cron schedule distribution checked:

- MN: 100% of predictions created at 04:00 VN ✓
- MT: 99% at 16:38 VN ✓
- MB: 100% at 17:30 VN ✓

No outlier hours, no off-by-one date issues observed.

## 6. Investigation — "LOSE region A, WIN region B same day" / "LOSE D, WIN D+1"

Owner observed this pattern frequently on no-token models. Investigated 408 settled no-token predictions over 30 days:

| Result | Count | Percent |
|---|---|---|
| Total | 408 | 100% |
| WIN (own region + own day) | 80 | 19.6% |
| LOSE | 328 | 80.4% |

Among 328 LOSE predictions:

| Sub-case | Count | Percent of LOSE |
|---|---|---|
| LOSE own region but WIN OTHER region same date (cross-region echo) | 185 | 56.4% |
| LOSE day D but WIN day D+1 same region (lag+1) | 139 | 42.4% |
| LOSE day D but WIN day D+2 same region (lag+2) | 51 | 15.5% |
| **Pure LOSE (no echo anywhere)** | **42** | **12.8%** |

### Null hypothesis

Each region per day has ~18-27 distinct 2-digit tails in 100 possible (00-99), so a random number has ~20-27% base rate to appear in one region one day. Across 3 regions × 3 days (D, D+1, D+2) = 9 nearly-independent draws, the probability of any number "echoing" somewhere ≈ 85-90%. Pure LOSE ~10-15% is exactly the random expectation.

→ The pattern is a **natural lottery characteristic** (autocorrelation + cross-region cascade), NOT a timezone bug. The model often picks the right number but commits to the wrong region or wrong day. This is a known phenomenon and the system already measures and exploits it:

- `lag_1_adaptive_exploit` measures lag+1 echo as a potential signal
- `mined_rules` extracts cross-region cascade rules (e.g. MB D-2 → MN D)
- `experimental_preview_shadow PRIOR_REGION_CONTEXT_SAFE_V1` tests prior-region signal usage

The verification semantics for win/lose remain strict (correct region + correct day) because that's how a player places bets in real life.

## 7. New SSOT doc — `TIMEZONE_AND_DATE_SEMANTICS.md`

Created a single source of truth document covering:

- D / D-1 / D-2 definitions
- Date field mapping across all main tables (predictions, final_bundles, lottery_results, etc.)
- Timestamp conventions (Python `vn_now()` vs SQL `datetime('now')`)
- Risk window VN 00:00-06:59 where SQL `date('now')` silently returns the previous day
- Cron audit: which crons currently run in the risk window and whether they touch SQL `date('now')`
- Code style guide for new features
- The 408-sample empirical analysis above

This document is the future reference for any agent / human reviewer working on date / timestamp logic.

## 8. Decided to NOT fix the 40+ SQL `date('now')` usages

A full audit found ~40 places using SQL `date('now')` for filtering or timestamping. Each has different semantics. A bulk fix would carry high regression risk against marginal gain because:

- Critical tables (predictions, lottery_results, slice_health) already use Python `vn_now()` → safe
- No cron currently in the risk window 00:00-06:59 actually uses SQL `date('now')` for filtering
- A blanket find-and-replace would silently shift comparison boundaries by one day in tables used by 30-day / 90-day windows

The audit is now part of the documented playbook so any new code can be vetted at review time. Spot fixes can be done later if needed (e.g. `final_bundles.created_at` timezone marker — cosmetic).

## 9. Safety / Reversibility

- No code change in any official prediction path.
- No DB table dropped or modified beyond the advisory `slice_policy` rows refreshed by planners (and one crontab move).
- Service active, /login HTTP 200, py_compile PASS local + VPS.
- Crontab backup taken before move (recoverable in 1 command if needed).
- Safety guard simulated live, original state restored.

## 10. STATUS

PUBLIC_SAFE — no IP / no internal paths / no provider keys / no DB DDL exposure / no private repo references.
