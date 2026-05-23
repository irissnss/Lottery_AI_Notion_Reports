# V106.06 Methodology

Live sync: `artifacts/live_sync/20260523_230610/manifest.json`. DB: `data/lottery_ai.db`.

Source restriction: low-cardinality prizes only — `DB#1`, `G1#1`, `G2#1`, `G2#2` from MB_BOARD or MN/MT station (cross-region targets only for station sources).

Transforms tested: LAST2, LAST2_REV, FIRST2, FIRST2_REV, HEAD_TAIL, TAIL_HEAD, HEAD_SECOND_LAST, SECOND_HEAD_TAIL, all P{i}P{j} pairs, SUM_LAST2, SUM_UNIT_TAIL, TAIL_SUM_UNIT, SUM_UNIT_HEAD, HEAD_SUM_UNIT.

Lags: D-1..D-7, W-1..W-4. Windows: 30/60/90/180.

Tiering:
- A (global): days >= 60, hit_lift_pp >= +8, db_day_lift_pp >= +3, half_stable >= 1.
- A (scoped): days >= 25, hit_lift_pp >= +12, db_day_lift_pp >= +5, half_stable >= 1.
- B / C: lower thresholds (see report).
- WATCH/REJECT: insufficient sample, negative lift, digit-sum weak, or no half-stability.

Anti-overfit: 153,228 rule keys tested; explicit live verify gate 14-30 days required before any boost.

Public-safe constraints: no DB/jsonl/log/secret/runtime artifact included.
