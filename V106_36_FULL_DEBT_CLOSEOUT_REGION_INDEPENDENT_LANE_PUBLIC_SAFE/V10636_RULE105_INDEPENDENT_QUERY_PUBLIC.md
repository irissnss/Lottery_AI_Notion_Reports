> **Public-safe report.** No private code, no DB rows, no provider keys, no raw VPS detail. Numbers shown are summary-only aggregates from V106.36 read-only audit. No official mutation occurred.



# V10636 RULE105 INDEPENDENT QUERY V2

- ts_vn: `2026-05-27T22:58:52`

## V10636 tier distribution per region

| Region | Tier | N |
|---|---|---|
| MB | CONFIRM_ONLY | 12 |
| MB | READY_STRONG_LANE | 1 |
| MB | RECALL_ONLY | 3 |
| MB | REJECT_WINDOW_NOISE | 4 |
| MB | RERANK_ONLY | 13 |
| MB | REVIEW | 2 |
| MN | CONFIRM_ONLY | 11 |
| MN | READY_STRONG_LANE | 3 |
| MN | RECALL_ONLY | 2 |
| MN | RERANK_ONLY | 19 |
| MT | CONFIRM_ONLY | 10 |
| MT | READY_STRONG_LANE | 3 |
| MT | RECALL_ONLY | 4 |
| MT | REJECT_WINDOW_NOISE | 3 |
| MT | RERANK_ONLY | 14 |
| MT | REVIEW | 1 |

## Per-region top 10 rules by composite_score

### MN

| weekday | src_station | src_region | offset | prize_keys | composite | tier_prod | activation | hr_avg | best_w | stable_w | spread_pp | current_noise_pp | V10636_tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Tiền Giang | MN | D-1 | G2+G7 | 100.0 | READY_WITH_CAUTION | active | 1.0 | 4w | 12w_16w_stable | 0.0 | 0.0 | **CONFIRM_ONLY** |
| 0 | Thái Bình | MB | D-1 | G6+G7 | 100.0 | LIMITED_WEIGHT | active | 1.0 | 4w | 12w_16w_stable | 0.0 | 0.0 | **RERANK_ONLY** |
| 1 | Hà Nội | MB | D-1 | GĐB+G7 | 100.0 | LIMITED_WEIGHT | active | 1.0 | 4w | 12w_16w_stable | 0.0 | 0.0 | **RERANK_ONLY** |
| 1 | Hà Nội | MB | D-1 | G6+G7 | 100.0 | LIMITED_WEIGHT | active | 1.0 | 4w | 12w_16w_stable | 0.0 | 0.0 | **RERANK_ONLY** |
| 2 | Quảng Ninh | MB | D-1 | G7 | 100.0 | LIMITED_WEIGHT | active | 1.0 | 4w | 12w_16w_stable | 0.0 | 0.0 | **RERANK_ONLY** |
| 2 | Quảng Ninh | MB | D-1 | GĐB+G7 | 100.0 | LIMITED_WEIGHT | active | 1.0 | 4w | 12w_16w_stable | 0.0 | 0.0 | **RERANK_ONLY** |
| 2 | Quảng Ninh | MB | D-1 | G1+G7 | 100.0 | LIMITED_WEIGHT | active | 1.0 | 4w | 12w_16w_stable | 0.0 | 0.0 | **RERANK_ONLY** |
| 2 | Quảng Ninh | MB | D-1 | G6+G7 | 100.0 | LIMITED_WEIGHT | active | 1.0 | 4w | 12w_16w_stable | 0.0 | 0.0 | **RERANK_ONLY** |
| 4 | Hà Nội | MB | D-1 | G1+G2 | 100.0 | LIMITED_WEIGHT | active | 1.0 | 4w | 12w_16w_stable | 0.0 | 0.0 | **RERANK_ONLY** |
| 4 | Hà Nội | MB | D-1 | GĐB+G2 | 100.0 | LIMITED_WEIGHT | active | 1.0 | 4w | 12w_16w_stable | 0.0 | 0.0 | **RERANK_ONLY** |

### MT

| weekday | src_station | src_region | offset | prize_keys | composite | tier_prod | activation | hr_avg | best_w | stable_w | spread_pp | current_noise_pp | V10636_tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Thái Bình | MB | D-1 | G6+G7 | 100.0 | LIMITED_WEIGHT | active | 1.0 | 4w | 12w_16w_stable | 0.0 | 0.0 | **RERANK_ONLY** |
| 1 | Hà Nội | MB | D-1 | G6+G7 | 100.0 | LIMITED_WEIGHT | active | 1.0 | 4w | 12w_16w_stable | 0.0 | 0.0 | **RERANK_ONLY** |
| 3 | Bắc Ninh | MB | D-1 | GĐB+G7 | 100.0 | READY_WITH_CAUTION | active | 1.0 | 4w | 12w_16w_stable | 0.0 | 0.0 | **CONFIRM_ONLY** |
| 3 | Bắc Ninh | MB | D-1 | G6+G7 | 100.0 | READY_WITH_CAUTION | active | 1.0 | 4w | 12w_16w_stable | 0.0 | 0.0 | **CONFIRM_ONLY** |
| 4 | Hà Nội | MB | D-1 | GĐB+G7 | 97.8 | LIMITED_WEIGHT | active | 0.9844 | 4w | noisy | 6.25 | 3.12 | **RERANK_ONLY** |
| 3 | Bắc Ninh | MB | D-1 | G1+G7 | 93.6 | READY_WITH_CAUTION | active | 0.9636 | 4w | 12w_16w_stable | 8.33 | 7.29 | **CONFIRM_ONLY** |
| 6 | Nam Định | MB | D-1 | GĐB+G7 | 93.6 | READY_WITH_CAUTION | active | 0.9323 | 4w | 12w_16w_stable | 12.5 | 7.29 | **CONFIRM_ONLY** |
| 6 | Nam Định | MB | D-1 | G6+G7 | 93.6 | LIMITED_WEIGHT | active | 0.9323 | 4w | 12w_16w_stable | 12.5 | 7.29 | **RERANK_ONLY** |
| 3 | Đà Nẵng | MT | D-1 | G5+GĐB | 93.4 | READY_STRONG | active | 0.9531 | 4w | noisy | 18.75 | 9.38 | **REVIEW** |
| 0 | Thái Bình | MB | D-1 | GĐB+G6 | 91.5 | LIMITED_WEIGHT | active | 0.9479 | 4w | 12w_16w_stable | 12.5 | 10.41 | **RERANK_ONLY** |

### MB

| weekday | src_station | src_region | offset | prize_keys | composite | tier_prod | activation | hr_avg | best_w | stable_w | spread_pp | current_noise_pp | V10636_tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | Hà Nội | MB | D-1 | G6+G7 | 100.0 | LIMITED_WEIGHT | active | 1.0 | 4w | 12w_16w_stable | 0.0 | 0.0 | **RERANK_ONLY** |
| 6 | Nam Định | MB | D-1 | G6+G7 | 97.8 | LIMITED_WEIGHT | active | 0.9844 | 4w | noisy | 6.25 | 3.12 | **RERANK_ONLY** |
| 6 | Nam Định | MB | D-1 | GĐB+G7 | 89.0 | READY_WITH_CAUTION | active | 0.8542 | 12w | 12w_16w_stable | 16.67 | -14.59 | **CONFIRM_ONLY** |
| 6 | Nam Định | MB | D-1 | G7 | 89.0 | LIMITED_WEIGHT | active | 0.8542 | 12w | 12w_16w_stable | 16.67 | -14.59 | **RECALL_ONLY** |
| 0 | Thái Bình | MB | D-1 | GĐB+G7 | 87.3 | READY_WITH_CAUTION | active | 0.8958 | 4w | 12w_16w_stable | 16.67 | 14.59 | **CONFIRM_ONLY** |
| 5 | TP. TP. HCM | MN | D | G2+G7 | 87.1 | LIMITED_WEIGHT | active | 0.8854 | 4w | noisy | 25.0 | 16.66 | **RERANK_ONLY** |
| 6 | Khánh Hòa | MT | D | G1+G7 | 87.1 | READY_WITH_CAUTION | active | 0.8854 | 4w | noisy | 25.0 | 16.66 | **CONFIRM_ONLY** |
| 0 | Thái Bình | MB | D-1 | G6+G7 | 85.1 | READY_WITH_CAUTION | active | 0.9114 | 4w | 12w_16w_stable | 18.75 | 17.71 | **CONFIRM_ONLY** |
| 0 | Huế | MT | D-1 | G1+G8 | 83.3 | LIMITED_WEIGHT | shadow | 0.875 | 4w | 12w_16w_stable | 16.67 | 16.67 | **RERANK_ONLY** |
| 1 | Hà Nội | MB | D-1 | G6+G7 | 82.6 | LIMITED_WEIGHT | active | 0.7864 | 12w | 12w_16w_stable | 8.33 | -7.29 | **RECALL_ONLY** |
