# V105.58 Root Cause Summary (Public)

Generated: `2026-05-16T23:19:04+07:00`. Diagnostic-only.

## MN
- Actual tail 81 was in the source pool, top5, and lo2; the official selector promoted 55.
- Lane `MN_ADAPTIVE_BUDGET_SELECTOR_V1 -> 19` would have been a winner (diagnostic).

## MT
- Actual tail 19 was in top5 but not in lo2; 12 was outside the pool yet rescued by lane-test.
- Official 76 was voted only by COMBO + NO_TOKEN; token-class providers did not vote 76.
- Possible amplifier: MT weight `rerun_post_mn=1.15` vs `ai_chain=0.95`.

## MB
- Actual tails 48, 81 in top5 dropped before lo2.
- 66, 70 in top20 dropped before lo2.
- 80, 91 voted by TOKEN models; ranker dropped them before top20.
- Official BT 43 still chosen.

Mechanism: aggregation/selector blind-spot, not source supply failure.
