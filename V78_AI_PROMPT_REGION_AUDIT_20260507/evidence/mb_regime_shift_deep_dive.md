# MB Regime Shift Deep Dive — V78

## Key Finding

MB is the hard region right now: OFFICIAL 0/4 and all test-lane methods 0/N over the 4-day incident window.

| date | official | herd | c16 | v67 | v70 | v73 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-05-04 | 09 MISS | 46 x6 HIT | None MISS | None MISS | 09 MISS | 09 MISS |
| 2026-05-05 | 83 MISS | 41 x10 MISS | 41 MISS | None MISS | 41 MISS | 41 MISS |
| 2026-05-06 | 79 MISS | 49 x7 MISS | 79 MISS | None MISS | 32 MISS | 32 MISS |
| 2026-05-07 | 20 MISS | 37 x5 MISS | 20 MISS | 79 MISS | 20 MISS | 79 MISS |

## Root Cause Hypothesis

MB is not a simple AI prompt miss only. It is an all-method cold regime:

- OFFICIAL misses 4 straight.
- C16 misses all available rows.
- V70 misses all 4 rows after backfill.
- V73 misses all available rows.
- AI herd tails rotate (`46`, `41`, `49`, `37`) and only `46` hit on 2026-05-04, but official/test selectors did not capture it.

This points to a regime/selection mismatch rather than a single selector bug.

## MB Prompt Needs

- Current cold-streak context.
- MB volatility warning tied to today, not only generic MB caution.
- AI herd vs NO_TOKEN herd comparison.
- Cross-region MN(D), MT(D), MB(D-1) context.
- Clear low-confidence reporting when all methods are cold.

## Safe Recovery Plan

1. Keep official locked.
2. Use `MB_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1` for dry-run package only.
3. Watch `MB_ALL_METHODS_COLD_FAST`.
4. If MB stays cold ≥7 additional days, escalate to P0 regime-shift forensic.
