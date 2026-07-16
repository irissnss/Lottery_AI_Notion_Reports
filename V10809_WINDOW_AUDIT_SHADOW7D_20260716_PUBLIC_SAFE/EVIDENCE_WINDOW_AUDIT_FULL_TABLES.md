# EVIDENCE V10809 — BẢNG ĐẦY ĐỦ AUDIT MỐC CỬA SỔ (output nguyên văn `_v10809_window_audit.py`)

Dữ liệu: MRE 2921 rows, 2025-12-20 → 2026-07-15. MIN_PRIOR=6 eval. Tercile = 1/3 trailing cao nhất
vs 1/3 thấp nhất (pooled). top2-lift = trung bình (top-2 rule theo trailing − mean toàn bộ rule) mỗi ngày.

## MN / thước CỤM-any (bão hòa — mọi mốc vô nghĩa)

| Scorer | corr | tercile hi/lo | spread | top2-lift | n |
|---|---|---|---|---|---|
| W4 | −0.068 | 96.6/95.7 | +0.9pp | +2.1pp | 353 |
| W6 | −0.107 | 96.6/99.1 | −2.6pp | +1.4pp | 353 |
| miner_12W | −0.095 | 94.9/97.4 | −2.6pp | +1.4pp | 353 |
| W16 | −0.081 | 94.9/98.3 | −3.4pp | +2.1pp | 353 |
| MB_8W_tuned | −0.106 | 94.9/98.3 | −3.4pp | +0.7pp | 353 |
| MNMT_12W_tuned | −0.102 | 94.9/98.3 | −3.4pp | +0.7pp | 353 |
| W8 | −0.112 | 94.9/99.1 | −4.3pp | +2.1pp | 353 |
| W12 | −0.100 | 94.0/99.1 | −5.1pp | +0.7pp | 353 |

## MT / thước CỤM-any (dương yếu)

| Scorer | corr | tercile hi/lo | spread | top2-lift | n |
|---|---|---|---|---|---|
| W16 | +0.103 | 92.4/84.7 | +7.6pp | +1.3pp | 355 |
| W6 | +0.101 | 94.9/88.1 | +6.8pp | +0.6pp | 355 |
| miner_12W | +0.098 | 91.5/84.7 | +6.8pp | +1.3pp | 355 |
| W4 | +0.082 | 94.1/88.1 | +5.9pp | +0.6pp | 355 |
| W8 | +0.053 | 94.9/89.0 | +5.9pp | +0.6pp | 355 |
| MB_8W_tuned | +0.081 | 91.5/85.6 | +5.9pp | −0.1pp | 355 |
| MNMT_12W_tuned | +0.088 | 91.5/85.6 | +5.9pp | −0.1pp | 355 |
| W12 | +0.092 | 90.7/85.6 | +5.1pp | +2.0pp | 355 |

## MB / thước CỤM-any (ĐẢO CHIỀU — chọn theo cụm nóng = chọn ngược)

| Scorer | corr | tercile hi/lo | spread | top2-lift | n |
|---|---|---|---|---|---|
| W16 | −0.088 | 73.3/80.2 | −6.9pp | +0.3pp | 349 |
| miner_12W | −0.103 | 68.1/75.9 | −7.8pp | −1.1pp | 349 |
| W6 | −0.113 | 72.4/81.0 | −8.6pp | +2.4pp | 349 |
| W12 | −0.091 | 68.1/76.7 | −8.6pp | +1.7pp | 349 |
| W8 | −0.120 | 69.0/78.4 | −9.5pp | +0.3pp | 349 |
| **MB_8W_tuned** | −0.117 | 66.4/77.6 | **−11.2pp** | −1.9pp | 349 |
| MNMT_12W_tuned | −0.112 | 66.4/77.6 | −11.2pp | −2.6pp | 349 |
| W4 | −0.133 | 69.0/81.9 | −12.9pp | −0.4pp | 349 |

## MN / thước PER-SỐ (mốc dài SỐNG TỐT)

| Scorer | corr | tercile hi/lo | spread | top2-lift | n |
|---|---|---|---|---|---|
| **W16** | +0.192 | 54.0/41.4 | **+12.6pp** | **+4.5pp** | 353 |
| miner_12W | +0.190 | 54.5/42.1 | +12.4pp | +4.3pp | 353 |
| W12 | +0.196 | 54.5/42.3 | +12.2pp | +4.2pp | 353 |
| MNMT_12W_tuned | +0.190 | 54.2/42.1 | +12.1pp | +3.9pp | 353 |
| MB_8W_tuned | +0.189 | 53.7/42.4 | +11.3pp | +3.7pp | 353 |
| W8 | +0.188 | 53.6/42.6 | +11.1pp | +3.4pp | 353 |
| W6 | +0.193 | 52.2/43.9 | +8.3pp | +2.2pp | 353 |
| W4 | +0.127 | 49.2/45.5 | +3.6pp | +3.0pp | 353 |

## MT / thước PER-SỐ

| Scorer | corr | tercile hi/lo | spread | top2-lift | n |
|---|---|---|---|---|---|
| **W16** | +0.231 | 47.2/35.0 | **+12.3pp** | +3.9pp | 355 |
| W12 | +0.224 | 46.6/35.2 | +11.4pp | +3.9pp | 355 |
| miner_12W | +0.224 | 46.4/35.1 | +11.3pp | +4.1pp | 355 |
| MB_8W_tuned | +0.199 | 46.1/35.4 | +10.7pp | +3.7pp | 355 |
| MNMT_12W_tuned | +0.210 | 45.8/35.2 | +10.6pp | +4.1pp | 355 |
| W6 | +0.201 | 48.4/38.7 | +9.8pp | +3.9pp | 355 |
| W8 | +0.162 | 46.7/38.3 | +8.4pp | +3.4pp | 355 |
| W4 | +0.152 | 45.0/37.3 | +7.7pp | +3.0pp | 355 |

## MB / thước PER-SỐ (yếu hơn 2 miền kia; mốc ngắn ÂM)

| Scorer | corr | tercile hi/lo | spread | top2-lift | n |
|---|---|---|---|---|---|
| **MNMT_12W_tuned** | +0.024 | 38.1/34.2 | **+3.9pp** | +1.9pp | 349 |
| W8 | +0.028 | 38.5/34.8 | +3.7pp | +2.3pp | 349 |
| W12 | +0.037 | 37.6/34.0 | +3.7pp | +1.9pp | 349 |
| miner_12W | +0.025 | 37.2/33.7 | +3.5pp | +1.9pp | 349 |
| W16 | +0.030 | 37.5/34.7 | +2.8pp | +1.8pp | 349 |
| MB_8W_tuned | +0.023 | 37.2/34.8 | +2.4pp | +1.2pp | 349 |
| W6 | −0.008 | 36.8/37.7 | −0.9pp | +1.1pp | 349 |
| W4 | −0.035 | 35.9/38.4 | −2.5pp | +0.5pp | 349 |

## Q3 — THIÊN LỆCH CỤM (rule nhả nhiều số)

| Miền | n_rule | corr(nhả-nhiều-số, HR-any-12W) | corr(nhả-nhiều-số, per-số) |
|---|---|---|---|
| MN | 34 | **+0.58** | **−0.62** |
| MT | 35 | **+0.45** | **−0.72** |
| MB | 29 | **+0.39** | **−0.83** |

## Định nghĩa scorer

- `W4/W6/W8/W12/W16`: trailing hit-rate cửa sổ N lần eval gần nhất (same-weekday ≈ N tuần) TRƯỚC ngày chấm.
- `miner_12W`: 0.50×12W + 0.35×16W + 0.10×4W (công thức `_seed_rules` production).
- `MB_8W_tuned`: 0.40×8W + 0.30×12W + 0.20×16W + 0.10×4W (công thức `mb_rule_ranker` production).
- `MNMT_12W_tuned`: 0.35×12W + 0.30×16W + 0.25×8W + 0.10×4W (công thức `_v10708` production).
- Thước "any" = hit_any cụm (any-of-k đuôi); thước "per-số" = tails_hit/tails_count.
