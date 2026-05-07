# 4-Day Regression Table (2026-05-04 → 2026-05-07)

## Per-method 4-day BT hit summary

| Region | OFFICIAL | C16_BUDGET | V67_EXPLOIT | V70_CONSENSUS | V73_HYBRID |
| ------ | -------- | ---------- | ----------- | ------------- | ---------- |
| MN     | 0/4 (0.0%) | 1/3 (33.3%) | 1/1 (100%) | 0/4 (0.0%) | 1/4 (25.0%) |
| MT     | 4/4 (100%) | 3/3 (100%) | 0/1 (0.0%) | 4/4 (100%) | 4/4 (100%) |
| MB     | 0/4 (0.0%) | 0/3 (0.0%) | 0/1 (0.0%) | 0/4 (0.0%) | 0/3 (0.0%) |
| ALL    | 4/12 (33.3%) | 4/9 (44.4%) | 1/3 (33.3%) | 4/12 (33.3%) | 4/9 (44.4%) |

## Day-by-day picks (BT only)

| Date | Region | Actuals(n) | OFFICIAL | C16 | V67 | V70 | V73 |
| ---- | ------ | ---------- | -------- | --- | --- | --- | --- |
| 2026-05-04 | MN | 39 | 65 ❌ | — | — | 65 ❌ | 65 ❌ |
| 2026-05-04 | MT | 27 | 29 ✅ | — | — | 82 ✅ | 82 ✅ |
| 2026-05-04 | MB | 22 | 09 ❌ | — | — | 09 ❌ | 09 ❌ |
| 2026-05-05 | MN | 42 | 15 ❌ | 52 ✅ | — | 15 ❌ | 15 ❌ |
| 2026-05-05 | MT | 30 | 44 ✅ | 52 ✅ | — | 44 ✅ | 44 ✅ |
| 2026-05-05 | MB | 22 | 83 ❌ | 41 ❌ | — | 41 ❌ | 41 ❌ |
| 2026-05-06 | MN | 41 | 95 ❌ | 95 ❌ | — | 95 ❌ | 95 ❌ |
| 2026-05-06 | MT | 32 | 11 ✅ | 71 ✅ | — | 71 ✅ | 71 ✅ |
| 2026-05-06 | MB | 24 | 79 ❌ | 79 ❌ | — | 32 ❌ | 32 ❌ |
| **2026-05-07** | **MN** | 40 | **94 ❌** | 94 ❌ | **95 ✅** | 94 ❌ | **95 ✅** |
| 2026-05-07 | MT | 40 | 88 ✅ | 88 ✅ | 95 ❌ | **88 ✅** | 88 ✅ |
| 2026-05-07 | MB | 24 | 20 ❌ | 20 ❌ | 79 ❌ | 20 ❌ | 79 ❌ |

## Notes on data coverage

- V67 EXPLOIT only ran for 2026-05-07 because lag-1 BOOST signal V66.1 had thin data for prior dates. V67 effectively new for production.
- C16 BUDGET row missing for 2026-05-04 (V57 was deployed 2026-05-05). Backfill from earlier dates not feasible.
- V70 CONSENSUS rows for 2026-05-04..05-06 created during V77 backfill; previously missing due to timing bug.
- V73 HYBRID rows for 2026-05-04..05-06 created during V77 backfill (driven by V70).
- All ✅/❌ hit/miss verifications use the union of last-2-digit tails across all stations of that region for that day.

## Would-save vs would-break (V73 vs OFFICIAL, last 4 days)

| Date | Region | OFFICIAL | V73 | Verdict |
| ---- | ------ | -------- | --- | ------- |
| 2026-05-04 | MN | 65 ❌ | 65 ❌ | — |
| 2026-05-04 | MT | 29 ✅ | 82 ✅ | — |
| 2026-05-04 | MB | 09 ❌ | 09 ❌ | — |
| 2026-05-05 | MN | 15 ❌ | 15 ❌ | — |
| 2026-05-05 | MT | 44 ✅ | 44 ✅ | — |
| 2026-05-05 | MB | 83 ❌ | 41 ❌ | — |
| 2026-05-06 | MN | 95 ❌ | 95 ❌ | — |
| 2026-05-06 | MT | 11 ✅ | 71 ✅ | — |
| 2026-05-06 | MB | 79 ❌ | 32 ❌ | — |
| **2026-05-07** | **MN** | **94 ❌** | **95 ✅** | **WOULD_SAVE** ✅ |
| 2026-05-07 | MT | 88 ✅ | 88 ✅ | — |
| 2026-05-07 | MB | 20 ❌ | 79 ❌ | — |

**TOTAL 4-day:** would_save = **1**, would_break = **0**, **net = +1**.
