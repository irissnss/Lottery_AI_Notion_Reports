# Báo Cáo Deep Source Rule Discovery Cho MN / MT / MB

> Phiên bản: V106.06 | Generated: 2026-05-23T23:32:52 | Live sync: `artifacts/live_sync/20260523_230610/manifest.json`
>
> Mục đích: nghiên cứu các tình huống `source -> target` có khả năng tạo tín hiệu cho MN/MT/MB. Báo cáo này KHÔNG sửa official prediction, KHÔNG promote rule, KHÔNG gọi provider/manual AI, KHÔNG đưa DB/jsonl/log lên public.

## 1. Tóm tắt điều hành

- Đã sinh và đo **153,228** rule candidate trên live DB; chấp nhận **54924** rule, từ chối **98304** rule (xem `rejected_rules.csv` + `overfit_warning_report.md`).
- Phân bố Tier A/B/C/WATCH theo target:
  - **MN**: Tier A = 634, Tier B = 5438, Tier C = 1398, WATCH = 9328.
  - **MT**: Tier A = 422, Tier B = 4209, Tier C = 1953, WATCH = 10144.
  - **MB**: Tier A = 207, Tier B = 4883, Tier C = 1417, WATCH = 14891.

- Phát hiện chính:
  1. **MT D** có nhiều rule mạnh nhất theo cả global lẫn scoped, đặc biệt từ `MB_BOARD` các giải `DB#1/G1#1/G2#1/G2#2`.
  2. **MN D** có Tier A toàn cục với `MB_BOARD G2#2 W-2 FIRST2_REV/P2P1` và một số transform DB#1 D-3/D-4.
  3. **MB D** chủ yếu chấp nhận Tier A theo `station-set` MB cụ thể (Hà Nội, Hải Phòng, Bắc Ninh, Nam Định) và một số transform global của `MB self-lag`.
  4. **Agreement family đếm số rule** không phải tín hiệu mạnh: lift chỉ +0.85..+1.19 pp vì pool rule rất lớn — KHÔNG dùng trực tiếp để boost. Khuyến nghị chuyển sang **agreement theo family-diversity** (yêu cầu tail trùng từ ≥2 family khác nhau).
  5. Một số rule có hit-lift rất cao nhưng chỉ 12-16 ngày sample (Tier C/WATCH); chỉ giữ làm recall, không boost.

- Promotion gate: KHÔNG đẩy bất kỳ rule nào lên `/du-doan` từ backtest này. Yêu cầu shadow 14d + live verify + agreement family-diverse.

- Module nên triển khai trước:
  1. `DEEP_SOURCE_RULE_SHADOW_V1` — bảng shadow gom mọi rule Tier A/B từ V106.06.
  2. `MT_MB_LOW_PRIZE_DIGIT_TRANSFORM_V1` — kế thừa V106.05, mở rộng theo top global mới.
  3. `AGREEMENT_FAMILY_DIVERSE_RANKER_V1` — cộng điểm khi ≥2 family khác nhau cùng sinh một tail.

## 2. Dữ liệu và phương pháp

- **Live snapshot**: `artifacts/live_sync/20260523_230610/manifest.json`.
- **DB**: `data/lottery_ai.db` (đã sync từ VPS).
- **Phạm vi nguồn (low-cardinality, exact lineage)**:
  - `MB_BOARD`: `DB#1`, `G1#1`, `G2#1`, `G2#2`.
  - `MN station`: `DB#1`, `G1#1`, `G2#1`, `G2#2` (chỉ áp dụng cho cross-region target).
  - `MT station`: `DB#1`, `G1#1`, `G2#1`, `G2#2` (chỉ áp dụng cho cross-region target).
- **Lag**: `D-1..D-7`, `W-1..W-4`.
- **Window đo**: 30, 60, 90, 180 ngày. Riêng weekday/station-set chạy 180d.
- **Transform** (mỗi transform sinh 1 candidate 2 chữ số):
  - Direct tail: `LAST2`, `LAST2_REV`, `FIRST2`, `FIRST2_REV`.
  - Head/tail cross: `HEAD_TAIL`, `TAIL_HEAD`, `HEAD_SECOND_LAST`, `SECOND_HEAD_TAIL`.
  - Position pair: `P{i}P{j}` cho mọi cặp i!=j hợp lệ với độ dài digit của số nguồn.
  - Digit sum: `SUM_LAST2`, `SUM_UNIT_TAIL`, `TAIL_SUM_UNIT`, `SUM_UNIT_HEAD`, `HEAD_SUM_UNIT`.
- **Baseline**:
  - `hit_baseline` = trung bình `|all_set_target_day| / 100` trên các ngày đo.
  - `db_day_baseline` = trung bình `|db_unique_target_day| / 100`.
- **Tier**:
  - **A** (global): `days >= 60`, `hit_lift_pp >= +8`, `db_day_lift_pp >= +3`, `half_stable >= 1`.
  - **A** (scoped): `days >= 25`, `hit_lift_pp >= +12`, `db_day_lift_pp >= +5`, `half_stable >= 1`.
  - **B**: lift đủ nhưng yếu hơn A.
  - **C**: sample nhỏ nhưng lift rất cao.
  - **WATCH**: cần verify thêm; nếu yếu → chuyển sang `rejected_rules.csv`.
- **Vì sao KHÔNG dùng broad selector** (`G3_ALL`, `LOW_ALL`, `TOP3_PRIZES`, `ALL_PRIZES`):
  - Có nhiều bộ số nguồn nên hệ thống không biết lấy bộ nào để chốt -> không đủ chuẩn deterministic feature.
  - Tỷ lệ hit phồng vì có nhiều candidate, nhưng lift so baseline không có ý nghĩa thực.

## 3. Kết quả cho MN D

### 1.1 Bảng global Tier A/B (top 12)

| Rank | Tier | Rule | Window | Days | Hit | Baseline | Lift | DB day | DB lift | Stable | Score |
|---:|:---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | A | `MB:MB_BOARD:G2#2:FIRST2_REV W-2` | 90 | 86 | 61.6% | 43.4% | +18.3 pp | 9.3% | +6.2 pp | 2 | 37.9 |
| 2 | A | `MB:MB_BOARD:G2#2:P2P1 W-2` | 90 | 86 | 61.6% | 43.4% | +18.3 pp | 9.3% | +6.2 pp | 2 | 37.9 |
| 3 | A | `MB:MB_BOARD:G2#2:FIRST2_REV W-2` | 60 | 60 | 60.0% | 43.4% | +16.6 pp | 10.0% | +6.8 pp | 2 | 35.6 |
| 4 | A | `MB:MB_BOARD:G2#2:P2P1 W-2` | 60 | 60 | 60.0% | 43.4% | +16.6 pp | 10.0% | +6.8 pp | 2 | 35.6 |
| 5 | B | `MB:MB_BOARD:G2#2:LAST2 W-3` | 60 | 60 | 63.3% | 43.4% | +19.9 pp | 5.0% | +1.9 pp | 2 | 34.0 |
| 6 | B | `MB:MB_BOARD:G2#2:P4P5 W-3` | 60 | 60 | 63.3% | 43.4% | +19.9 pp | 5.0% | +1.9 pp | 2 | 34.0 |
| 7 | A | `MB:MB_BOARD:DB#1:P3P1 D-4` | 60 | 60 | 61.7% | 43.4% | +18.2 pp | 6.7% | +3.5 pp | 2 | 33.9 |
| 8 | A | `MB:MB_BOARD:G2#2:P3P5 D-3` | 60 | 60 | 61.7% | 43.4% | +18.2 pp | 6.7% | +3.5 pp | 2 | 33.9 |
| 9 | B | `MB:MB_BOARD:G2#1:TAIL_HEAD W-4` | 60 | 60 | 61.7% | 43.4% | +18.2 pp | 5.0% | +1.9 pp | 2 | 32.0 |
| 10 | B | `MB:MB_BOARD:G2#1:P5P1 W-4` | 60 | 60 | 61.7% | 43.4% | +18.2 pp | 5.0% | +1.9 pp | 2 | 32.0 |
| 11 | B | `MB:MB_BOARD:G2#2:P5P2 D-3` | 60 | 60 | 63.3% | 43.4% | +19.9 pp | 1.7% | -1.5 pp | 2 | 30.2 |
| 12 | B | `MB:MB_BOARD:G2#2:LAST2 W-3` | 90 | 86 | 60.5% | 43.3% | +17.2 pp | 3.5% | +0.3 pp | 2 | 30.0 |

### 1.2 Bảng scoped (weekday hoặc station-set) Tier A/B (top 12, đã khử trùng)

| Rank | Tier | Rule | Window | Days | Hit | Baseline | Lift | DB day | DB lift | Stable | Score |
|---:|:---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | A | `MT:Đắk Nông:DB#1:FIRST2_REV D-3` | scope: WD=T3 | 180 | 26 | 73.1% | 41.1% | +31.9 pp | 11.5% | +8.5 pp | 2 | 53.4 |
| 2 | A | `MT:Đắk Nông:DB#1:FIRST2_REV D-3` | scope: STATION=Bạc Liêu|Bến Tre|Vũng Tàu | 180 | 26 | 73.1% | 41.1% | +31.9 pp | 11.5% | +8.5 pp | 2 | 53.4 |
| 3 | A | `MT:Bình Định:DB#1:TAIL_HEAD D-6` | scope: WD=T4 | 180 | 26 | 73.1% | 42.0% | +31.0 pp | 11.5% | +8.6 pp | 2 | 52.4 |
| 4 | A | `MT:Bình Định:DB#1:TAIL_HEAD D-6` | scope: STATION=Cần Thơ|Sóc Trăng|Đồng Nai | 180 | 26 | 73.1% | 42.0% | +31.0 pp | 11.5% | +8.6 pp | 2 | 52.4 |
| 5 | A | `MB:MB_BOARD:G2#2:P5P3 D-7` | scope: WD=T5 | 180 | 25 | 76.0% | 41.8% | +34.2 pp | 8.0% | +5.0 pp | 2 | 52.0 |
| 6 | A | `MB:MB_BOARD:G2#2:P5P3 D-7` | scope: STATION=An Giang|Bình Thuận|Tây Ninh | 180 | 25 | 76.0% | 41.8% | +34.2 pp | 8.0% | +5.0 pp | 2 | 52.0 |
| 7 | A | `MB:MB_BOARD:DB#1:P4P1 D-7` | scope: WD=T6 | 180 | 26 | 73.1% | 42.5% | +30.6 pp | 11.5% | +8.5 pp | 2 | 51.8 |
| 8 | A | `MB:MB_BOARD:DB#1:P4P1 D-7` | scope: STATION=Bình Dương|Trà Vinh|Vĩnh Long | 180 | 26 | 73.1% | 42.5% | +30.6 pp | 11.5% | +8.5 pp | 2 | 51.8 |
| 9 | A | `MB:MB_BOARD:G2#2:P5P2 D-7` | scope: WD=CN | 180 | 25 | 64.0% | 42.0% | +22.0 pp | 20.0% | +17.1 pp | 2 | 51.6 |
| 10 | A | `MB:MB_BOARD:G2#2:P5P2 D-7` | scope: STATION=Kiên Giang|Tiền Giang|Đà Lạt | 180 | 25 | 64.0% | 42.0% | +22.0 pp | 20.0% | +17.1 pp | 2 | 51.6 |
| 11 | B | `MB:MB_BOARD:G2#2:SUM_LAST2 D-2` | scope: WD=T6 | 180 | 25 | 80.0% | 42.5% | +37.5 pp | 4.0% | +1.0 pp | 2 | 51.5 |
| 12 | B | `MB:MB_BOARD:G2#2:SUM_LAST2 D-2` | scope: STATION=Bình Dương|Trà Vinh|Vĩnh Long | 180 | 25 | 80.0% | 42.5% | +37.5 pp | 4.0% | +1.0 pp | 2 | 51.5 |

### 1.3 Phân bố family Tier A/B cho MN

| Family | Số rule Tier A/B |
|---|---:|
| position_pair | 1782 |
| adjacent_pair | 1340 |
| head_tail_cross | 728 |
| head | 674 |
| digit_sum | 631 |
| tail | 629 |
| head_secondlast_cross | 288 |

### 1.4 Phân tích các tình huống owner đề cập cho MN

- **MB DB D-1/D-2/D-3 -> MN**: best = `MB:MB_BOARD:DB#1:LAST2 D-1` w180 scope=WD=T7 days=26 hit=80.8% lift=+29.5 pp DB=3.9% lift=-0.1 tier=B
- **MB G1 D-1/D-2/D-3 -> MN**: best = `MB:MB_BOARD:G1#1:P1P3 D-1` w180 scope=WD=T3 days=25 hit=68.0% lift=+26.8 pp DB=12.0% lift=+9.0 tier=A
- **MB G2#1 D-1/D-2/D-3 -> MN**: best = `MB:MB_BOARD:G2#1:P4P2 D-3` w180 scope=WD=T5 days=25 hit=68.0% lift=+26.0 pp DB=12.0% lift=+9.0 tier=A
- **MB G2#2 D-1/D-2/D-3 -> MN**: best = `MB:MB_BOARD:G2#2:SUM_LAST2 D-2` w180 scope=WD=T6 days=25 hit=80.0% lift=+37.5 pp DB=4.0% lift=+1.0 tier=B

## 4. Kết quả cho MT D

### 2.1 Bảng global Tier A/B (top 12)

| Rank | Tier | Rule | Window | Days | Hit | Baseline | Lift | DB day | DB lift | Stable | Score |
|---:|:---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | B | `MB:MB_BOARD:DB#1:SUM_LAST2 D-7` | 60 | 60 | 55.0% | 35.3% | +19.7 pp | 5.0% | +2.6 pp | 2 | 34.6 |
| 2 | B | `MB:MB_BOARD:DB#1:SUM_LAST2 D-7` | 60 | 60 | 55.0% | 35.3% | +19.7 pp | 5.0% | +2.6 pp | 2 | 34.6 |
| 3 | B | `MB:MB_BOARD:G2#2:P5P2 D-7` | 60 | 60 | 55.0% | 35.3% | +19.7 pp | 5.0% | +2.6 pp | 2 | 34.6 |
| 4 | B | `MB:MB_BOARD:G2#2:P5P2 D-7` | 60 | 60 | 55.0% | 35.3% | +19.7 pp | 5.0% | +2.6 pp | 2 | 34.6 |
| 5 | B | `MB:MB_BOARD:G2#2:SECOND_HEAD_TAIL D-7` | 60 | 60 | 55.0% | 35.3% | +19.7 pp | 3.3% | +0.9 pp | 2 | 32.6 |
| 6 | B | `MB:MB_BOARD:G2#2:SECOND_HEAD_TAIL D-7` | 60 | 60 | 55.0% | 35.3% | +19.7 pp | 3.3% | +0.9 pp | 2 | 32.6 |
| 7 | B | `MB:MB_BOARD:G2#2:P2P5 D-7` | 60 | 60 | 55.0% | 35.3% | +19.7 pp | 3.3% | +0.9 pp | 2 | 32.6 |
| 8 | B | `MB:MB_BOARD:G2#2:P2P5 D-7` | 60 | 60 | 55.0% | 35.3% | +19.7 pp | 3.3% | +0.9 pp | 2 | 32.6 |
| 9 | A | `MB:MB_BOARD:G2#2:P4P3 D-4` | 60 | 60 | 50.0% | 35.3% | +14.7 pp | 8.3% | +5.9 pp | 2 | 32.5 |
| 10 | A | `MB:MB_BOARD:G2#1:P4P1 D-1` | 90 | 90 | 50.0% | 35.1% | +14.9 pp | 6.7% | +4.2 pp | 2 | 31.9 |
| 11 | A | `MB:MB_BOARD:G2#2:P4P3 D-5` | 90 | 88 | 48.9% | 35.2% | +13.7 pp | 6.8% | +4.4 pp | 2 | 30.6 |
| 12 | A | `MB:MB_BOARD:G2#1:P4P1 D-1` | 60 | 60 | 50.0% | 35.3% | +14.7 pp | 6.7% | +4.2 pp | 2 | 30.5 |

### 2.2 Bảng scoped (weekday hoặc station-set) Tier A/B (top 12, đã khử trùng)

| Rank | Tier | Rule | Window | Days | Hit | Baseline | Lift | DB day | DB lift | Stable | Score |
|---:|:---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | A | `MB:MB_BOARD:DB#1:P2P4 D-1` | scope: WD=CN | 180 | 25 | 76.0% | 40.8% | +35.2 pp | 16.0% | +13.0 pp | 2 | 62.2 |
| 2 | B | `MB:MB_BOARD:DB#1:P2P3 D-6` | scope: WD=T4 | 180 | 24 | 62.5% | 29.9% | +32.6 pp | 16.7% | +14.7 pp | 2 | 61.9 |
| 3 | B | `MB:MB_BOARD:DB#1:P2P3 D-6` | scope: STATION=Khánh Hòa|Đà Nẵng | 180 | 24 | 62.5% | 29.9% | +32.6 pp | 16.7% | +14.7 pp | 2 | 61.9 |
| 4 | A | `MN:Sóc Trăng:G2#1:FIRST2_REV W-2` | scope: WD=T4 | 180 | 26 | 65.4% | 30.0% | +35.4 pp | 11.5% | +9.5 pp | 2 | 59.3 |
| 5 | A | `MN:Sóc Trăng:G2#1:FIRST2_REV W-2` | scope: STATION=Khánh Hòa|Đà Nẵng | 180 | 26 | 65.4% | 30.0% | +35.4 pp | 11.5% | +9.5 pp | 2 | 59.3 |
| 6 | A | `MB:MB_BOARD:G1#1:P4P1 D-3` | scope: WD=T6 | 180 | 25 | 60.0% | 30.5% | +29.5 pp | 12.0% | +10.1 pp | 2 | 52.8 |
| 7 | A | `MB:MB_BOARD:G1#1:P4P1 D-3` | scope: STATION=Gia Lai|Ninh Thuận | 180 | 25 | 60.0% | 30.5% | +29.5 pp | 12.0% | +10.1 pp | 2 | 52.8 |
| 8 | A | `MB:MB_BOARD:DB#1:P5P3 D-6` | scope: WD=T3 | 180 | 25 | 52.0% | 30.4% | +21.6 pp | 20.0% | +18.0 pp | 2 | 52.8 |
| 9 | A | `MB:MB_BOARD:DB#1:P5P3 D-6` | scope: STATION=Quảng Nam|Đắk Lắk | 180 | 25 | 52.0% | 30.4% | +21.6 pp | 20.0% | +18.0 pp | 2 | 52.8 |
| 10 | A | `MB:MB_BOARD:G2#1:P1P3 D-1` | scope: WD=CN | 180 | 25 | 64.0% | 40.8% | +23.2 pp | 20.0% | +17.0 pp | 2 | 52.4 |
| 11 | A | `MB:MB_BOARD:G1#1:TAIL_SUM_UNIT D-2` | scope: WD=T5 | 180 | 25 | 60.0% | 41.7% | +18.3 pp | 24.0% | +21.0 pp | 2 | 51.1 |
| 12 | A | `MB:MB_BOARD:G1#1:TAIL_SUM_UNIT D-2` | scope: STATION=Bình Định|Quảng Bình|Quảng Trị | 180 | 25 | 60.0% | 41.7% | +18.3 pp | 24.0% | +21.0 pp | 2 | 51.1 |

### 2.3 Phân bố family Tier A/B cho MT

| Family | Số rule Tier A/B |
|---|---:|
| position_pair | 1221 |
| adjacent_pair | 958 |
| tail | 598 |
| head | 560 |
| head_tail_cross | 560 |
| digit_sum | 523 |
| head_secondlast_cross | 211 |

### 2.4 Phân tích các tình huống owner đề cập cho MT

- **MB DB D-1/D-2/D-3 -> MT**: best = `MB:MB_BOARD:DB#1:P2P4 D-1` w180 scope=STATION=Huế|Khánh Hòa|Kon Tum days=16 hit=75.0% lift=+34.2 pp DB=18.8% lift=+15.8 tier=C
- **MB G1 D-1/D-2/D-3 -> MT**: best = `MB:MB_BOARD:G1#1:P4P3 D-3` w180 scope=STATION=Phú Yên|Thừa Thiên Huế days=12 hit=66.7% lift=+36.4 pp DB=8.3% lift=+6.3 tier=C
- **MB G2#1 D-1/D-2/D-3 -> MT**: best = `MB:MB_BOARD:G2#1:P4P3 D-2` w180 scope=STATION=Phú Yên|Thừa Thiên Huế days=12 hit=66.7% lift=+36.4 pp DB=8.3% lift=+6.3 tier=C
- **MB G2#2 D-1/D-2/D-3 -> MT**: best = `MB:MB_BOARD:G2#2:TAIL_SUM_UNIT D-1` w180 scope=STATION=Phú Yên|Thừa Thiên Huế days=12 hit=66.7% lift=+36.4 pp DB=8.3% lift=+6.3 tier=C

## 5. Kết quả cho MB D

### 3.1 Bảng global Tier A/B (top 12)

| Rank | Tier | Rule | Window | Days | Hit | Baseline | Lift | DB day | DB lift | Stable | Score |
|---:|:---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | A | `MB:MB_BOARD:G2#2:P5P3 W-2` | 60 | 60 | 40.0% | 23.7% | +16.3 pp | 5.0% | +4.0 pp | 2 | 33.2 |
| 2 | A | `MB:MB_BOARD:G1#1:HEAD_TAIL D-4` | 60 | 60 | 38.3% | 23.7% | +14.7 pp | 5.0% | +4.0 pp | 1 | 29.2 |
| 3 | A | `MB:MB_BOARD:G1#1:P1P5 D-4` | 60 | 60 | 38.3% | 23.7% | +14.7 pp | 5.0% | +4.0 pp | 1 | 29.2 |
| 4 | B | `MB:MB_BOARD:DB#1:P3P4 D-2` | 60 | 60 | 41.7% | 23.7% | +18.0 pp | 0.0% | -1.0 pp | 2 | 28.2 |
| 5 | A | `MB:MB_BOARD:DB#1:SUM_LAST2 D-7` | 60 | 60 | 35.0% | 23.7% | +11.3 pp | 5.0% | +4.0 pp | 2 | 27.2 |
| 6 | A | `MB:MB_BOARD:DB#1:SUM_LAST2 D-7` | 60 | 60 | 35.0% | 23.7% | +11.3 pp | 5.0% | +4.0 pp | 2 | 27.2 |
| 7 | B | `MB:MB_BOARD:G1#1:SUM_LAST2 D-5` | 60 | 60 | 36.7% | 23.7% | +13.0 pp | 3.3% | +2.3 pp | 2 | 26.9 |
| 8 | B | `MB:MB_BOARD:G2#1:P3P4 D-6` | 60 | 60 | 36.7% | 23.7% | +13.0 pp | 3.3% | +2.3 pp | 2 | 26.9 |
| 9 | B | `MB:MB_BOARD:G2#2:SUM_UNIT_TAIL D-4` | 60 | 60 | 36.7% | 23.7% | +13.0 pp | 3.3% | +2.3 pp | 2 | 26.9 |
| 10 | B | `MB:MB_BOARD:G2#2:P3P4 W-2` | 60 | 60 | 36.7% | 23.7% | +13.0 pp | 3.3% | +2.3 pp | 2 | 26.9 |
| 11 | B | `MB:MB_BOARD:DB#1:SUM_UNIT_TAIL D-2` | 60 | 60 | 38.3% | 23.7% | +14.7 pp | 1.7% | +0.7 pp | 2 | 26.5 |
| 12 | B | `MB:MB_BOARD:G2#2:P1P3 W-2` | 60 | 60 | 38.3% | 23.7% | +14.7 pp | 1.7% | +0.7 pp | 2 | 26.5 |

### 3.2 Bảng scoped (weekday hoặc station-set) Tier A/B (top 12, đã khử trùng)

| Rank | Tier | Rule | Window | Days | Hit | Baseline | Lift | DB day | DB lift | Stable | Score |
|---:|:---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | A | `MT:Bình Định:G1#1:HEAD_TAIL W-3` | scope: WD=T5 | 180 | 25 | 52.0% | 23.4% | +28.6 pp | 12.0% | +11.0 pp | 2 | 55.3 |
| 2 | A | `MT:Bình Định:G1#1:HEAD_TAIL W-3` | scope: STATION=Hà Nội | 180 | 25 | 52.0% | 23.4% | +28.6 pp | 12.0% | +11.0 pp | 2 | 55.3 |
| 3 | B | `MT:Đắk Nông:G2#1:TAIL_HEAD D-4` | scope: WD=T4 | 180 | 25 | 60.0% | 23.9% | +36.1 pp | 4.0% | +3.0 pp | 2 | 52.8 |
| 4 | B | `MT:Đắk Nông:G2#1:TAIL_HEAD D-4` | scope: STATION=Bắc Ninh | 180 | 25 | 60.0% | 23.9% | +36.1 pp | 4.0% | +3.0 pp | 2 | 52.8 |
| 5 | A | `MN:Cần Thơ:G1#1:HEAD_TAIL W-2` | scope: WD=T4 | 180 | 25 | 52.0% | 23.9% | +28.1 pp | 8.0% | +7.0 pp | 2 | 48.8 |
| 6 | A | `MN:Cần Thơ:G1#1:HEAD_TAIL W-2` | scope: STATION=Bắc Ninh | 180 | 25 | 52.0% | 23.9% | +28.1 pp | 8.0% | +7.0 pp | 2 | 48.8 |
| 7 | A | `MB:MB_BOARD:G2#2:HEAD_SECOND_LAST D-1` | scope: WD=T6 | 180 | 25 | 52.0% | 24.3% | +27.7 pp | 8.0% | +7.0 pp | 2 | 48.4 |
| 8 | A | `MB:MB_BOARD:G2#2:HEAD_SECOND_LAST D-1` | scope: STATION=Hải Phòng | 180 | 25 | 52.0% | 24.3% | +27.7 pp | 8.0% | +7.0 pp | 2 | 48.4 |
| 9 | A | `MB:MB_BOARD:G2#2:P1P4 D-1` | scope: WD=T6 | 180 | 25 | 52.0% | 24.3% | +27.7 pp | 8.0% | +7.0 pp | 2 | 48.4 |
| 10 | A | `MB:MB_BOARD:G2#2:P1P4 D-1` | scope: STATION=Hải Phòng | 180 | 25 | 52.0% | 24.3% | +27.7 pp | 8.0% | +7.0 pp | 2 | 48.4 |
| 11 | B | `MT:Khánh Hòa:G1#1:TAIL_HEAD D-7` | scope: WD=T4 | 180 | 25 | 56.0% | 23.9% | +32.1 pp | 4.0% | +3.0 pp | 2 | 48.0 |
| 12 | B | `MT:Khánh Hòa:G1#1:TAIL_HEAD D-7` | scope: STATION=Bắc Ninh | 180 | 25 | 56.0% | 23.9% | +32.1 pp | 4.0% | +3.0 pp | 2 | 48.0 |

### 3.3 Phân bố family Tier A/B cho MB

| Family | Số rule Tier A/B |
|---|---:|
| position_pair | 1224 |
| adjacent_pair | 971 |
| head_tail_cross | 837 |
| head | 757 |
| tail | 741 |
| digit_sum | 385 |
| head_secondlast_cross | 175 |

### 3.4 Phân tích các tình huống owner đề cập cho MB

- **MB DB D-1/D-2/D-3 -> MB**: best = `MB:MB_BOARD:DB#1:HEAD_SUM_UNIT D-3` w180 scope=WD=T2 days=24 hit=50.0% lift=+26.1 pp DB=4.2% lift=+3.2 tier=B
- **MB G1 D-1/D-2/D-3 -> MB**: best = `MB:MB_BOARD:G1#1:P5P2 D-3` w180 scope=WD=T4 days=25 hit=48.0% lift=+24.1 pp DB=4.0% lift=+3.0 tier=B
- **MB G2#1 D-1/D-2/D-3 -> MB**: best = `MB:MB_BOARD:G2#1:HEAD_TAIL D-3` w180 scope=WD=T4 days=25 hit=36.0% lift=+12.1 pp DB=16.0% lift=+15.0 tier=A
- **MB G2#2 D-1/D-2/D-3 -> MB**: best = `MB:MB_BOARD:G2#2:HEAD_SECOND_LAST D-1` w180 scope=WD=T6 days=25 hit=52.0% lift=+27.7 pp DB=8.0% lift=+7.0 tier=A

## 6. Nhóm rule bị loại

Xem `rejected_rules.csv` (khoảng **98,304** rule). Lý do loại chính:

| Lý do | Số lượng |
|---|---:|
| NEGATIVE_LIFT | 52951 |
| WEAK_NO_TIER | 39801 |
| DIGIT_SUM_NOT_STRONG_ENOUGH | 5552 |

Ví dụ rule đẹp nhưng bị loại (xem 30 dòng đầu trong `overfit_warning_report.md`):
- `*:digit_sum` family với hit-lift < +8: bị loại vì collision space hẹp.
- Rule chỉ đẹp ở 1 window duy nhất, `half_stable=0`: bị nghi overfit -> WATCH/REJECT.
- Rule có hit-lift cao nhưng `days < 12`: chỉ giữ làm recall, không đủ Tier.

## 7. Kết luận kỹ thuật

1. **Module cần tạo**:
   - `DEEP_SOURCE_RULE_SHADOW_V1`: bảng `digit_transform_source_rule_shadow` ghi nhận rule Tier A/B mỗi ngày.
   - `AGREEMENT_FAMILY_DIVERSE_RANKER_V1`: cộng điểm khi ≥2 family khác nhau sinh cùng tail.
   - `MT_MB_LOW_PRIZE_DIGIT_TRANSFORM_V1`: continuation từ V106.05 cho target MT (đã có shadow design).
2. **Field bắt buộc** trong `digit_transform_source_rule_shadow` (xem mục 8 bên dưới).
3. **Rule Tier A**: được phép tham gia source-pool ranking shadow + family-diverse agreement; KHÔNG boost trực tiếp official.
4. **Rule Tier B**: chỉ shadow, theo dõi 14d live trước khi xét nâng tier.
5. **Rule Tier C**: chỉ recall (mở rộng pool), không boost score.
6. **Rule WATCH**: chỉ ghi log, không tham gia ranking.
7. **Rule REJECTED**: không được dùng kể cả làm recall.

### 7.1 Cảnh báo data-snooping

- Đã test 153,228 rule key trên cùng tập dữ liệu -> rất nhiều "đẹp" do ngẫu nhiên.
- Vì vậy KHÔNG được kết luận "rule này chắc chắn mạnh".
- Mọi rule phải qua live verify thêm 14-30 ngày sau ngày publish báo cáo (anchor live: 2026-05-23) trước khi xét nâng tier.

## 8. Đề xuất triển khai shadow 14 ngày

**Bảng**: `digit_transform_source_rule_shadow`

**Field bắt buộc**:
- `id INTEGER PRIMARY KEY`
- `target_date TEXT NOT NULL`
- `target_region TEXT NOT NULL`
- `target_weekday INTEGER`
- `target_station_set TEXT`
- `source_region TEXT NOT NULL`
- `source_station TEXT`
- `source_date TEXT NOT NULL`
- `source_lag TEXT NOT NULL`
- `source_prize TEXT NOT NULL`
- `source_index INTEGER NOT NULL`
- `source_number TEXT NOT NULL`
- `transform_name TEXT NOT NULL`
- `transformed_tail TEXT NOT NULL`
- `historical_window INTEGER`
- `candidate_lift_pp REAL`
- `db_day_lift_pp REAL`
- `tier TEXT`
- `rule_family TEXT`
- `agreement_count INTEGER`
- `output_eligible INTEGER NOT NULL DEFAULT 0`
- `official_promoted INTEGER NOT NULL DEFAULT 0`
- `would_save_bt INTEGER`
- `would_break_bt INTEGER`
- `actual_any_hit INTEGER`
- `actual_db_hit INTEGER`
- `notes TEXT`
- `created_at TEXT NOT NULL`

**Ràng buộc bắt buộc**:
- `output_eligible = 0`, `official_promoted = 0` mặc định.
- KHÔNG ghi vào `predictions`, `final_bundles`, `model_daily_eval`, `lottery_results`.
- Pre/post hash 4 official tables IDENTICAL (theo .Antigravityrules.md).

**Quy trình 14 ngày**:
- D0: insert rule Tier A/B từ V106.06 vào shadow.
- D+1..D+13: cron 23:40 VN tính `actual_any_hit`, `actual_db_hit`, `would_save_bt`, `would_break_bt` cho rule active đó.
- D+14: sinh evidence pack, so sánh net-save và false-promotion.
- D+15+: chỉ rule có lift dương duy trì + false-promotion thấp mới được xét lên test-lane chính.

## 9. Final Recommendation

### NÊN làm ngay (measurement-only, không đụng official)
1. Tạo bảng `digit_transform_source_rule_shadow` theo schema mục 8.
2. Backfill 90 ngày Tier A toàn cục cho MN/MT/MB từ artifact `top_rules_by_target_region.json`.
3. Wire scheduler hook 23:40 VN sau natural closeout.
4. Cập nhật `monitoring` UI section "Deep Source Rule Tracking" (admin-only, refresh 60s).

### CHỈ shadow (chưa boost)
1. Tier A/B scoped (weekday + station-set) cho MT D, đặc biệt nhóm `MB_BOARD DB#1 D-1` các transform `P2P4`, `P3P4`, `P5P3`, `LAST2`.
2. Tier A scoped cho MN D (`MT:Đắk Nông:DB#1:FIRST2_REV D-3` station-set Bạc Liêu/Bến Tre/Vũng Tàu).
3. Tier A scoped cho MB D (Hà Nội, Hải Phòng, Bắc Ninh) từ `MT:Bình Định:G1#1:HEAD_TAIL W-3`, `MT:Khánh Hòa:G1#1:TAIL_HEAD D-7`.

### CHƯA làm
1. Boost official từ rule Tier C hoặc WATCH.
2. Promote rule digit-sum làm primary boost; chỉ làm context.
3. Mở rộng nguồn ngoài DB#1/G1#1/G2#1/G2#2 trước khi shadow A/B đủ 14 ngày.

### CẤM dùng làm boost
1. Mọi broad selector: `G3_ALL`, `LOW_ALL`, `TOP3_PRIZES`, `ALL_PRIZES`.
2. Rule không có lineage station/prize/index/transform/lag rõ ràng.
3. Rule sample < 12 ngày, hoặc `half_stable = 0` với hit-lift > +15 (overfit).

### Cần kiểm tra thêm
1. **Agreement family-diverse**: cộng điểm chỉ khi tail trùng từ ≥2 family khác nhau (ví dụ 1 head_tail + 1 position_pair).
2. **MB D self-lag**: tách riêng signal `MB self-lag` vs `MN/MT cross` để tránh trộn.
3. **W-1..W-4 cho MN station -> MT D**: top scoped cho thấy có thực tế DB-day +9..+15 pp ở 25 ngày.
4. **Window 30/60d** với sample nhỏ: cần verify lại sau 14d live.

## 10. Bảng ưu tiên triển khai

| Ưu tiên | Target | Module / Rule Family | Lý do | Rủi ro | Hành động |
|---:|:---:|---|---|---|---|
| 1 | MT | `MT_MB_LOW_PRIZE_DIGIT_TRANSFORM_V1` | Tier A nhiều nhất, có cả global lẫn scoped, kế thừa V106.05 | Rule scoped sample 25 ngày | Shadow 14d theo schema mục 8 |
| 2 | MN | `MN_MB_G2_DB_LOW_PRIZE_LAG_TRANSFORM_V1` | MB G2#2 W-2 transform P2P1/FIRST2_REV global lift +18 pp | Multiple-testing | Shadow + candidate-rate lock |
| 3 | MB | `CROSS_REGION_WEEKLY_EXACT_POSITION_V1` | Tier A scoped Hà Nội/Hải Phòng/Bắc Ninh từ MT W-3/D-7 | Sample 25 ngày | Shadow + recall only, không boost đơn nguồn |
| 4 | All | `AGREEMENT_FAMILY_DIVERSE_RANKER_V1` | Giảm false-positive. Phải dùng family-diverse, không chỉ count rule | Cần code lại agreement | Code shadow generator + 14d test |
| 5 | All | `DEEP_SOURCE_RULE_SHADOW_V1` | Khung chung ghi mọi rule Tier A/B với lineage | Volume row lớn | Schema + cron + monitoring UI |

## 11. Roadmap surface (governance)

- ⚠ **CP-66.7** trong `docs/ACTIVE_ROADMAP_LAG1_ADAPTIVE_EXPLOIT.md`: ACCUMULATING + OVERDUE: cần evidence pack 14d cho Adaptive Exploit V1 — chưa giải quyết trong session này (V106.06 không phụ thuộc CP-66.7).
- ⚠ **CP-66.8** SCHEDULED + OVERDUE +2 ngày: cần `V66_ADAPTIVE_EXPLOIT_EVIDENCE_PACK_<date>.md` 14 ngày. Khuyến nghị xử lý sau khi V106.06 shadow chạy đủ.
- §52 Measurement-UI-Deploy-Sync: V106.06 đã hoàn tất bước measurement (artifact + report). Bước UI panel + scheduler hook + Notion sync sẽ áp dụng khi owner OK shadow module.

## 12. Output artifacts

Tất cả nằm trong `artifacts/v106_06_deep_source_rule_discovery/`:
- `MANIFEST.md`: snapshot, scope, file list.
- `deep_source_rule_candidates.csv`: tất cả rule chấp nhận.
- `top_rules_by_target_region.json`: top theo Tier per target.
- `rejected_rules.csv`: rule loại + reject_reason.
- `agreement_rules.csv` + `agreement_rules.json`: thống kê agreement count đơn giản (đã ghi caveat: lift yếu).
- `station_set_rules.csv`: rule scoped theo station-set.
- `weekday_rules.csv`: rule scoped theo weekday.
- `overfit_warning_report.md`: cảnh báo data-snooping + 30 rule rejected mạnh nhất.
- `FINAL_OWNER_REPORT_VN.md`: báo cáo này.
- `scripts/v10606_deep_mine.py`: script mining.
- `scripts/build_report.py`: script build báo cáo này.

## 13. Chốt quy định

- KHÔNG kết luận "rule này chắc chắn mạnh".
- KHÔNG đẩy rule lên official.
- KHÔNG dùng để chốt số trực tiếp.
- CHỈ "đủ điều kiện shadow", "chỉ recall", hoặc "reject vì overfit".
- Tất cả rule mới phải qua live verify 14/30 ngày trước khi bàn rank boost nhẹ.

---

**Live snapshot**: `artifacts/live_sync/20260523_230610/manifest.json`. **DB**: `data/lottery_ai.db`. **Generated**: 2026-05-23T23:32:54.
