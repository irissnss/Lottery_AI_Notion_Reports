> **Public-safe report.** No private code, no DB rows, no provider keys, no raw VPS detail. Numbers shown are summary-only aggregates from V106.36 read-only audit. No official mutation occurred.



# V10636 TOP RULES TIER GATE — promotion to lane-test

- ts_vn: `2026-05-27T23:00:43`
- input: V10636_RULE105_INDEPENDENT_QUERY_V2.json (105 rules)
- references: V10626 (58 pre-register, 19 FU3, 13 FU4 STABLE_ALL); V10629R1 materializer; V10634 rule pipeline; V10635 MB GĐB D-2 NOT_VALIDATED

## Tier distribution by region

| Region | TIER_A_LANE_TEST_READY | TIER_B_SHADOW_ONLY | TIER_C_REJECT |
|---|---|---|---|
| MN | 26 | 9 | 0 |
| MT | 18 | 14 | 3 |
| MB | 4 | 26 | 5 |

## TIER A rules (LANE_TEST_READY) per region

### MN

| weekday | src_station | src_region | offset | prize_keys | composite | hr_avg | best_w | stable | spread_pp | reason |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Tiền Giang | MN | D-1 | G2+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 0 | Thái Bình | MB | D-1 | G6+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 1 | Hà Nội | MB | D-1 | GĐB+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 1 | Hà Nội | MB | D-1 | G6+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 2 | Quảng Ninh | MB | D-1 | G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 2 | Quảng Ninh | MB | D-1 | GĐB+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 2 | Quảng Ninh | MB | D-1 | G1+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 2 | Quảng Ninh | MB | D-1 | G6+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 4 | Hà Nội | MB | D-1 | G1+G2 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 4 | Hà Nội | MB | D-1 | GĐB+G2 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 4 | Hà Nội | MB | D-1 | G1+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 5 | Gia Lai | MT | D-1 | GĐB+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 5 | Hải Phòng | MB | D-1 | GĐB+G2 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 5 | Hải Phòng | MB | D-1 | G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 5 | Hải Phòng | MB | D-1 | GĐB+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 5 | Hải Phòng | MB | D-1 | G1+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 1 | Phú Yên | MT | D-1 | G5+G7 | 93.6 | 0.9323 | 4w | 12w_16w_stable | 12.5 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 1 | Hà Nội | MB | D-1 | G7 | 93.6 | 0.9323 | 4w | 12w_16w_stable | 12.5 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 1 | Hà Nội | MB | D-1 | G1+G7 | 93.6 | 0.9323 | 4w | 12w_16w_stable | 12.5 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 3 | Bắc Ninh | MB | D-1 | GĐB+G7 | 93.6 | 0.9323 | 4w | 12w_16w_stable | 12.5 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 3 | Bắc Ninh | MB | D-1 | G6+G7 | 93.6 | 0.9323 | 4w | 12w_16w_stable | 12.5 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 4 | Hà Nội | MB | D-1 | G7 | 93.6 | 0.9636 | 4w | 12w_16w_stable | 8.33 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 4 | Hà Nội | MB | D-1 | GĐB+G6 | 93.6 | 0.9636 | 4w | 12w_16w_stable | 8.33 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 3 | Cần Thơ | MN | D-1 | G1+G8 | 91.5 | 0.9479 | 4w | 12w_16w_stable | 12.5 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 3 | Bắc Ninh | MB | D-1 | G1+G2 | 91.5 | 0.9479 | 4w | 12w_16w_stable | 12.5 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 2 | Bến Tre | MN | D-1 | G7+G8 | 91.1 | 0.8698 | 16w | 12w_16w_stable | 18.75 | CONFIRM_ONLY with hr_avg>=0.85 and stable |

### MT

| weekday | src_station | src_region | offset | prize_keys | composite | hr_avg | best_w | stable | spread_pp | reason |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Thái Bình | MB | D-1 | G6+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 1 | Hà Nội | MB | D-1 | G6+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 3 | Bắc Ninh | MB | D-1 | GĐB+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 3 | Bắc Ninh | MB | D-1 | G6+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 3 | Bắc Ninh | MB | D-1 | G1+G7 | 93.6 | 0.9636 | 4w | 12w_16w_stable | 8.33 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 6 | Nam Định | MB | D-1 | GĐB+G7 | 93.6 | 0.9323 | 4w | 12w_16w_stable | 12.5 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 6 | Nam Định | MB | D-1 | G6+G7 | 93.6 | 0.9323 | 4w | 12w_16w_stable | 12.5 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 0 | Thái Bình | MB | D-1 | GĐB+G6 | 91.5 | 0.9479 | 4w | 12w_16w_stable | 12.5 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 0 | Thái Bình | MB | D-1 | G6 | 91.5 | 0.9479 | 4w | 12w_16w_stable | 12.5 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 0 | Thái Bình | MB | D-1 | G1+G7 | 91.5 | 0.9479 | 4w | 12w_16w_stable | 12.5 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 4 | Hà Nội | MB | D-1 | G6+G7 | 91.5 | 0.9167 | 4w | 12w_16w_stable | 12.5 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 5 | TP. HCM | MN | D | G1+G8 | 91.5 | 0.9167 | 4w | 12w_16w_stable | 12.5 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 5 | Hải Phòng | MB | D-1 | GĐB+G6 | 91.5 | 0.9479 | 4w | 12w_16w_stable | 12.5 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 5 | Hải Phòng | MB | D-1 | G6+G7 | 91.5 | 0.9167 | 4w | 12w_16w_stable | 12.5 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 6 | Đà Lạt | MN | D | GĐB+G7 | 91.5 | 0.9167 | 4w | 12w_16w_stable | 12.5 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 1 | Hà Nội | MB | D-1 | G1+G7 | 91.1 | 0.8698 | 16w | 12w_16w_stable | 18.75 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 5 | Bình Phước | MN | D | GĐB+G1 | 89.0 | 0.8542 | 12w | 12w_16w_stable | 16.67 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 0 | Huế | MT | D-1 | G5+G7 | 85.8 | 0.8928 | 4w | 12w_16w_stable | 14.29 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |

### MB

| weekday | src_station | src_region | offset | prize_keys | composite | hr_avg | best_w | stable | spread_pp | reason |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | Hà Nội | MB | D-1 | G6+G7 | 100.0 | 1.0 | 4w | 12w_16w_stable | 0.0 | RERANK_ONLY with hr_avg>=0.80 + stable + spread<=15 |
| 6 | Nam Định | MB | D-1 | GĐB+G7 | 89.0 | 0.8542 | 12w | 12w_16w_stable | 16.67 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 0 | Thái Bình | MB | D-1 | GĐB+G7 | 87.3 | 0.8958 | 4w | 12w_16w_stable | 16.67 | CONFIRM_ONLY with hr_avg>=0.85 and stable |
| 0 | Thái Bình | MB | D-1 | G6+G7 | 85.1 | 0.9114 | 4w | 12w_16w_stable | 18.75 | CONFIRM_ONLY with hr_avg>=0.85 and stable |

## Owner observation matches: MB G2 D-2 → MN D

| target | weekday | src_station | src_region | offset | prize_keys | composite | v10636_tier | promotion_tier |
|---|---|---|---|---|---|---|---|---|

## V10635 hypothesis link rows (MB self GĐB D-2)

| weekday | src_station | src_region | offset | prize_keys | composite | promotion_tier | reason |
|---|---|---|---|---|---|---|---|
