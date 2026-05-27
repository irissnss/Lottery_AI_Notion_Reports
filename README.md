# Lottery AI Notion Reports

Latest public-safe package: `V106_35_MB_DB_D2_DEEP_DIVE_PUBLIC_SAFE` (V106.35).

Latest report: `V106_35_MB_DB_D2_DEEP_DIVE_PUBLIC_SAFE/V10635_MB_DB_D2_DEEP_DIVE_REPORT_VN_PUBLIC.md`.

## Latest update (2026-05-27 — V106.35 MB DB D-2 Deep-Dive)

Owner hypothesis: "MB target date D = MB Giải Đặc Biệt at D-2 — anh nhận thấy cũng thường xuyên về lại".

Tested across 2,338 days of MB history (2020-01-01 → 2026-05-26), 28 transforms × 6 windows × 7 weekday breakdown.

**Result: HYPOTHESIS NOT VALIDATED.**

| Window | H1 LOOSE (LAST2 in any MB tail) | H2 STRICT (GĐB → GĐB) |
|---|---|---|
| 60d | 20.00% (lift −3.70pp) | 0.00% (lift −1.00pp) |
| 90d | 20.00% (lift −3.78pp) | 0.00% (lift −1.00pp) |
| 180d | 25.00% (lift +1.10pp) | 0.58% (lift −0.42pp) |
| 365d | 22.97% (lift −0.91pp) | 1.12% (lift +0.12pp) |
| 730d | 24.72% (lift +0.87pp) | 1.12% (lift +0.12pp) |
| ALL (2,268d) | 25.44% (lift +1.65pp) | 0.97% (lift −0.03pp) |

H1 baseline ~24% (random expectation). H2 baseline 1% (uniform random).

Recent 60-90 days show **NEGATIVE lift** −3.7 to −3.78pp — hypothesis worse than random in current regime.

**Recommendation**: do NOT add this rule to any pipeline tier (including SHADOW/PRE_REGISTER). Owner observation likely caused by selection bias and confusion between H1 LOOSE (always sits ~24% by construction) and H2 STRICT (true random 1%).

For previous versions (V106.34 rule pipeline mechanism, V106.33 live control reconcile, ..., V106.26.2 FU4, V107, V106.06, ...), see `REPORT_INDEX.md`.
