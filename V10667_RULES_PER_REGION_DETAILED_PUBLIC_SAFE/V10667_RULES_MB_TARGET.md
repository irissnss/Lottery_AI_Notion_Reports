# V10668 Rules cho TARGET = MB (Đích = Miền MB)

> **Generated**: 2026-06-02T11:28:25+07:00
> **Target region**: MB
> **Audit window**: Forward 90d, anchor 2026-06-02 → earliest closeout 2026-08-31
> **Patch**: V10668 TEMPORAL CAUSALITY FIX (đã loại rule vi phạm thứ tự xổ)

## ⚠️ QUAN TRỌNG 1 — Thứ tự xổ & Temporal Causality

Thứ tự xổ Việt Nam: **MN (~16:10) → MT (~17:10) → MB (~18:15)**.

**MB target**: MB xổ CUỐI CÙNG trong ngày (~18:15). Rule cho MB target được dùng MN(D) và MT(D) same-day (cả 2 đã xổ trước MB) + mọi nguồn lag ≥ 1. MB không bị giới hạn temporal nào với same-day source.

Các rule "nguồn xổ SAU đích cùng ngày" (vd MT(D)→MN(D), MB(D)→MN(D), MB(D)→MT(D)) đã được **LOẠI BỎ** khỏi tài liệu này vì không thể dùng để dự đoán forward (data từ tương lai). Xem chi tiết: `V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md`.

## ⚠️ QUAN TRỌNG 2 — Quy ước Đánh Số Bộ Số

Ký hiệu `Giải X bộ Y` (hoặc `GX#Y`): **bộ = vị trí trên bảng kết quả, KHÔNG phải đài**. Owner đánh dấu G.4 MB (4 bộ): Bộ 1=top-left, Bộ 2=top-right, Bộ 3=bottom-left, Bộ 4=bottom-right. Ví dụ MB 31/05/2026: G.4 bộ 1=7717, bộ 2=7829, bộ 3=5183, bộ 4=4559. Xem đầy đủ: `V10667_BO_NUMBERING_LEGEND.md`.

## ⚠️ QUAN TRỌNG 3 — Nguồn nhiều đài (GOM/union)

Khi miền nguồn có nhiều đài cùng ngày, rule **GOM (union)** giá trị của TẤT CẢ đài đó. Mỗi rule dưới đây đã ghi rõ đài nguồn cụ thể trong phần "Mô tả". Lưu ý MB mỗi thứ là 1 đài tỉnh khác nhau (T2=Hà Nội, T3=Quảng Ninh, T4=Bắc Ninh, T5=Hà Nội, T6=Hải Phòng, T7=Nam Định, CN=Thái Bình). Xem đầy đủ lịch đài + cách resolve: `V10670_SOURCE_SEMANTICS_LEGEND.md`.

## Giới thiệu — MB

Miền Bắc (1 đài duy nhất MB_BOARD). Mỗi ngày 1 kết quả. Vì 1 đài/ngày nên evidence mỏng hơn MN/MT ~3-4 lần — V10.3 MB CALIBRATION giảm trần confidence từ 70% xuống 55%.

### Cách đọc bảng dưới

- Mỗi thứ trong tuần (T2-CN) có 1 section riêng
- Trong mỗi thứ, em liệt kê **đài hoạt động** + **top rule mạnh nhất**
- Mỗi rule có:
  - **Mô tả tiếng Việt** (cách áp dụng)
  - **Bảng per-station** (hit rate của từng đài cụ thể) — để anh biết đài nào đóng góp nhiều nhất
  - **3 ngày gần nhất rule trúng** (worked examples để anh hình dung)
  - **p-value + BH-pass** (statistical significance)

### Strength legend

- ⭐ **STRONG (BH-pass)** — pass multiple-testing correction, gold standard
- **STRONG** — p<0.01 lift ≥ +5pp
- **MODERATE** — p<0.05 lift ≥ +3pp
- **MARGINAL** — p<0.05 lift < +3pp
- **WEAK** — p≥0.05 (KHÔNG nên dùng)

---

## MB × Thứ Hai (T2)

**Đài hoạt động ngày này**:
- Hà Nội

**Coverage trong cell này**: 296 rule có data, **17 đạt p<0.05**, **1 BH-pass** ⭐.

### Rule #1 ⭐ — `MN:DB#1:D`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1** từ GOM tất cả 3 đài MN xổ T2 (**TP. HCM, Đồng Tháp, Cà Mau**), ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MN:DB#1:D, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **206**
- Hit rate: **63.19%**
- Baseline (random): **54.76%**
- **LIFT: +8.43pp**
- p-value: 0.0013
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 326 | 206 | 63.19% | [57.8-68.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-11 | 2026-05-11 | 44, 53, 54 | Hà Nội |
| 2026-05-04 | 2026-05-04 | 19, 25, 85 | Hà Nội |
| 2026-04-20 | 2026-04-20 | 06, 22, 54 | Hà Nội |

---

### Rule #2 — `MB:G4#4:D-3`

**Strength**: STRONG

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 4** từ đài **Hải Phòng** (đài MB xổ T6), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G4#4:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **97**
- Hit rate: **29.85%**
- Baseline (random): **23.79%**
- **LIFT: +6.06pp**
- p-value: 0.0062

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 325 | 97 | 29.85% | [25.1-35.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-18 | 2026-05-15 | 14 | Hà Nội |
| 2026-03-30 | 2026-03-27 | 65 | Hà Nội |
| 2026-03-16 | 2026-03-13 | 26 | Hà Nội |

---

### Rule #3 — `MT:G3#1:D`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1** từ GOM tất cả 2 đài MT xổ T2 (**Thừa Thiên Huế, Phú Yên**), ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MT:G3#1:D, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **156**
- Hit rate: **47.85%**
- Baseline (random): **41.82%**
- **LIFT: +6.04pp**
- p-value: 0.0157

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 326 | 156 | 47.85% | [42.5-53.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-04 | 2026-05-04 | 82, 93 | Hà Nội |
| 2026-04-27 | 2026-04-27 | 93, 95 | Hà Nội |
| 2026-04-20 | 2026-04-20 | 73, 81 | Hà Nội |

---

### Rule #4 — `MT:G5#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1** từ GOM tất cả 2 đài MT xổ T6 (**Gia Lai, Ninh Thuận**), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MT:G5#1:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **156**
- Hit rate: **47.71%**
- Baseline (random): **41.77%**
- **LIFT: +5.94pp**
- p-value: 0.0170

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 327 | 156 | 47.71% | [42.4-53.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-06-01 | 2026-05-29 | 40, 80 | Hà Nội |
| 2026-05-11 | 2026-05-08 | 10, 98 | Hà Nội |
| 2026-05-04 | 2026-05-01 | 93, 95 | Hà Nội |

---

### Rule #5 — `MT:G3#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1** từ GOM tất cả 2 đài MT xổ T6 (**Gia Lai, Ninh Thuận**), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MT:G3#1:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **156**
- Hit rate: **47.71%**
- Baseline (random): **41.77%**
- **LIFT: +5.94pp**
- p-value: 0.0170

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 327 | 156 | 47.71% | [42.4-53.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-18 | 2026-05-15 | 14, 70 | Hà Nội |
| 2026-05-11 | 2026-05-08 | 46, 67 | Hà Nội |
| 2026-04-27 | 2026-04-24 | 25, 68 | Hà Nội |

---

### Rule #6 — `MB:G6#2:D-1`

**Strength**: STRONG

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 2** từ đài **Thái Bình** (đài MB xổ CN), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G6#2:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **96**
- Hit rate: **29.45%**
- Baseline (random): **23.79%**
- **LIFT: +5.66pp**
- p-value: 0.0097

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 326 | 79 | 24.23% | [19.9-29.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-04-27 | 2026-04-26 | 28 | Hà Nội |
| 2026-04-13 | 2026-04-12 | 60 | Hà Nội |
| 2026-03-23 | 2026-03-22 | 54 | Hà Nội |

---

### Rule #7 — `MB:DB#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1** từ đài **Hải Phòng** (đài MB xổ T6), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:DB#1:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.62%**
- Baseline (random): **23.79%**
- **LIFT: +4.83pp**
- p-value: 0.0239

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 325 | 93 | 28.62% | [24.0-33.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-06-01 | 2026-05-29 | 54 | Hà Nội |
| 2026-04-13 | 2026-04-10 | 20 | Hà Nội |
| 2026-03-02 | 2026-02-27 | 83 | Hà Nội |

---

### Rule #8 — `MB:G2#2:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 2** từ đài **Thái Bình** (đài MB xổ CN), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G2#2:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.53%**
- Baseline (random): **23.79%**
- **LIFT: +4.74pp**
- p-value: 0.0258

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 326 | 80 | 24.54% | [20.2-29.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-25 | 2026-05-24 | 14 | Hà Nội |
| 2026-05-18 | 2026-05-17 | 69 | Hà Nội |
| 2026-05-11 | 2026-05-10 | 52 | Hà Nội |

---

### Rule #9 — `MB:G6#3:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 3** từ đài **Thái Bình** (đài MB xổ CN), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G6#3:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.53%**
- Baseline (random): **23.79%**
- **LIFT: +4.74pp**
- p-value: 0.0258

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 326 | 82 | 25.15% | [20.8-30.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-18 | 2026-05-17 | 83 | Hà Nội |
| 2026-04-20 | 2026-04-19 | 25 | Hà Nội |
| 2026-03-09 | 2026-03-08 | 84 | Hà Nội |

---

### Rule #10 — `MB:G7#4:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4** từ đài **Hải Phòng** (đài MB xổ T6), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#4:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.31%**
- Baseline (random): **23.79%**
- **LIFT: +4.52pp**
- p-value: 0.0322

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 325 | 92 | 28.31% | [23.7-33.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-06-01 | 2026-05-29 | 83 | Hà Nội |
| 2026-05-25 | 2026-05-22 | 81 | Hà Nội |
| 2026-05-04 | 2026-05-01 | 46 | Hà Nội |

---

### Rule #11 — `MB:G7#4:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4** từ đài **Hải Phòng** (đài MB xổ T6), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#4:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.31%**
- Baseline (random): **23.79%**
- **LIFT: +4.52pp**
- p-value: 0.0322

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 325 | 92 | 28.31% | [23.7-33.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-06-01 | 2026-05-29 | 83 | Hà Nội |
| 2026-05-25 | 2026-05-22 | 81 | Hà Nội |
| 2026-05-04 | 2026-05-01 | 46 | Hà Nội |

---

### Rule #12 — `MB:G7#4:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4** từ đài **Hải Phòng** (đài MB xổ T6), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#4:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.31%**
- Baseline (random): **23.79%**
- **LIFT: +4.52pp**
- p-value: 0.0322

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 325 | 92 | 28.31% | [23.7-33.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-06-01 | 2026-05-29 | 83 | Hà Nội |
| 2026-05-25 | 2026-05-22 | 81 | Hà Nội |
| 2026-05-04 | 2026-05-01 | 46 | Hà Nội |

---


## MB × Thứ Ba (T3)

**Đài hoạt động ngày này**:
- Quảng Ninh

**Coverage trong cell này**: 296 rule có data, **14 đạt p<0.05**, **1 BH-pass** ⭐.

### Rule #1 ⭐ — `MN:G3#2:D-2`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 2** từ GOM tất cả 3 đài MN xổ CN (**Tiền Giang, Kiên Giang, Đà Lạt**), ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MN:G3#2:D-2, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **203**
- Hit rate: **62.46%**
- Baseline (random): **54.83%**
- **LIFT: +7.63pp**
- p-value: 0.0034
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ninh | 325 | 203 | 62.46% | [57.1-67.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-26 | 2026-05-24 | 26, 38, 98 | Quảng Ninh |
| 2026-05-12 | 2026-05-10 | 24, 33, 47 | Quảng Ninh |
| 2026-05-05 | 2026-05-03 | 05, 15, 66 | Quảng Ninh |

---

### Rule #2 — `MN:G3#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1** từ GOM tất cả 3 đài MN xổ T2 (**TP. HCM, Đồng Tháp, Cà Mau**), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MN:G3#1:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **199**
- Hit rate: **61.04%**
- Baseline (random): **54.95%**
- **LIFT: +6.09pp**
- p-value: 0.0155

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ninh | 326 | 199 | 61.04% | [55.6-66.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-26 | 2026-05-25 | 50, 61, 92 | Quảng Ninh |
| 2026-04-28 | 2026-04-27 | 27, 61, 96 | Quảng Ninh |
| 2026-04-21 | 2026-04-20 | 55, 68, 99 | Quảng Ninh |

---

### Rule #3 — `MB:G1#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1** từ đài **Nam Định** (đài MB xổ T7), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G1#1:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **324**
- Số ngày trúng (ANY station of MB): **95**
- Hit rate: **29.32%**
- Baseline (random): **23.79%**
- **LIFT: +5.54pp**
- p-value: 0.0115

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ninh | 324 | 95 | 29.32% | [24.6-34.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-12 | 2026-05-09 | 52 | Quảng Ninh |
| 2026-04-21 | 2026-04-18 | 13 | Quảng Ninh |
| 2026-04-14 | 2026-04-11 | 03 | Quảng Ninh |

---

### Rule #4 — `MB:G4#3:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 3** từ đài **Hà Nội** (đài MB xổ T2), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G4#3:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **95**
- Hit rate: **29.23%**
- Baseline (random): **23.79%**
- **LIFT: +5.45pp**
- p-value: 0.0125

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ninh | 325 | 78 | 24.00% | [19.7-28.9]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-19 | 2026-05-18 | 62 | Quảng Ninh |
| 2026-03-03 | 2026-03-02 | 20 | Quảng Ninh |
| 2026-01-13 | 2026-01-12 | 63 | Quảng Ninh |

---

### Rule #5 — `MB:G7#4:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4** từ đài **Hà Nội** (đài MB xổ T2), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#4:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **94**
- Hit rate: **28.92%**
- Baseline (random): **23.79%**
- **LIFT: +5.14pp**
- p-value: 0.0174

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ninh | 325 | 83 | 25.54% | [21.1-30.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-19 | 2026-05-18 | 55 | Quảng Ninh |
| 2026-03-03 | 2026-03-02 | 00 | Quảng Ninh |
| 2026-02-10 | 2026-02-09 | 67 | Quảng Ninh |

---

### Rule #6 — `MB:G7#4:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4** từ đài **Hà Nội** (đài MB xổ T2), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#4:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **94**
- Hit rate: **28.92%**
- Baseline (random): **23.79%**
- **LIFT: +5.14pp**
- p-value: 0.0174

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ninh | 325 | 83 | 25.54% | [21.1-30.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-19 | 2026-05-18 | 55 | Quảng Ninh |
| 2026-03-03 | 2026-03-02 | 00 | Quảng Ninh |
| 2026-02-10 | 2026-02-09 | 67 | Quảng Ninh |

---

### Rule #7 — `MB:G7#4:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4** từ đài **Hà Nội** (đài MB xổ T2), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#4:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **94**
- Hit rate: **28.92%**
- Baseline (random): **23.79%**
- **LIFT: +5.14pp**
- p-value: 0.0174

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ninh | 325 | 83 | 25.54% | [21.1-30.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-19 | 2026-05-18 | 55 | Quảng Ninh |
| 2026-03-03 | 2026-03-02 | 00 | Quảng Ninh |
| 2026-02-10 | 2026-02-09 | 67 | Quảng Ninh |

---

### Rule #8 — `MB:G6#2:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 2** từ đài **Nam Định** (đài MB xổ T7), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G6#2:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **324**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.70%**
- Baseline (random): **23.79%**
- **LIFT: +4.92pp**
- p-value: 0.0220

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ninh | 324 | 74 | 22.84% | [18.6-27.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-19 | 2026-05-16 | 85 | Quảng Ninh |
| 2026-04-14 | 2026-04-11 | 94 | Quảng Ninh |
| 2026-03-10 | 2026-03-07 | 95 | Quảng Ninh |

---

### Rule #9 — `MB:G7#2:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 2** từ đài **Hà Nội** (đài MB xổ T2), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#2:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.62%**
- Baseline (random): **23.79%**
- **LIFT: +4.83pp**
- p-value: 0.0239

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ninh | 325 | 93 | 28.62% | [24.0-33.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-01-13 | 2026-01-12 | 34 | Quảng Ninh |
| 2025-12-30 | 2025-12-29 | 21 | Quảng Ninh |
| 2025-12-09 | 2025-12-08 | 59 | Quảng Ninh |

---

### Rule #10 — `MB:G7#2:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 2** từ đài **Hà Nội** (đài MB xổ T2), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#2:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.62%**
- Baseline (random): **23.79%**
- **LIFT: +4.83pp**
- p-value: 0.0239

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ninh | 325 | 93 | 28.62% | [24.0-33.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-01-13 | 2026-01-12 | 34 | Quảng Ninh |
| 2025-12-30 | 2025-12-29 | 21 | Quảng Ninh |
| 2025-12-09 | 2025-12-08 | 59 | Quảng Ninh |

---

### Rule #11 — `MB:G7#2:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 2** từ đài **Hà Nội** (đài MB xổ T2), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#2:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.62%**
- Baseline (random): **23.79%**
- **LIFT: +4.83pp**
- p-value: 0.0239

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ninh | 325 | 93 | 28.62% | [24.0-33.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-01-13 | 2026-01-12 | 34 | Quảng Ninh |
| 2025-12-30 | 2025-12-29 | 21 | Quảng Ninh |
| 2025-12-09 | 2025-12-08 | 59 | Quảng Ninh |

---


## MB × Thứ Tư (T4)

**Đài hoạt động ngày này**:
- Bắc Ninh

**Coverage trong cell này**: 296 rule có data, **21 đạt p<0.05**, **1 BH-pass** ⭐.

### Rule #1 ⭐ — `MB:G7#4:D-1`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4** từ đài **Quảng Ninh** (đài MB xổ T3), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#4:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **101**
- Hit rate: **30.98%**
- Baseline (random): **23.79%**
- **LIFT: +7.20pp**
- p-value: 0.0014
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bắc Ninh | 326 | 101 | 30.98% | [26.2-36.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-27 | 2026-05-26 | 81 | Bắc Ninh |
| 2026-05-06 | 2026-05-05 | 50 | Bắc Ninh |
| 2026-04-08 | 2026-04-07 | 77 | Bắc Ninh |

---

### Rule #2 — `MB:G7#4:D-1`

**Strength**: STRONG

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4** từ đài **Quảng Ninh** (đài MB xổ T3), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#4:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **101**
- Hit rate: **30.98%**
- Baseline (random): **23.79%**
- **LIFT: +7.20pp**
- p-value: 0.0014

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bắc Ninh | 326 | 101 | 30.98% | [26.2-36.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-27 | 2026-05-26 | 81 | Bắc Ninh |
| 2026-05-06 | 2026-05-05 | 50 | Bắc Ninh |
| 2026-04-08 | 2026-04-07 | 77 | Bắc Ninh |

---

### Rule #3 — `MB:G7#4:D-1`

**Strength**: STRONG

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4** từ đài **Quảng Ninh** (đài MB xổ T3), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#4:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **101**
- Hit rate: **30.98%**
- Baseline (random): **23.79%**
- **LIFT: +7.20pp**
- p-value: 0.0014

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bắc Ninh | 326 | 101 | 30.98% | [26.2-36.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-27 | 2026-05-26 | 81 | Bắc Ninh |
| 2026-05-06 | 2026-05-05 | 50 | Bắc Ninh |
| 2026-04-08 | 2026-04-07 | 77 | Bắc Ninh |

---

### Rule #4 — `MB:G6#2:D-1`

**Strength**: STRONG

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 2** từ đài **Quảng Ninh** (đài MB xổ T3), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G6#2:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **96**
- Hit rate: **29.45%**
- Baseline (random): **23.79%**
- **LIFT: +5.66pp**
- p-value: 0.0097

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bắc Ninh | 326 | 63 | 19.33% | [15.4-24.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-13 | 2026-05-12 | 47 | Bắc Ninh |
| 2026-04-15 | 2026-04-14 | 65 | Bắc Ninh |
| 2026-04-08 | 2026-04-07 | 77 | Bắc Ninh |

---

### Rule #5 — `MB:G7#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1** từ đài **Thái Bình** (đài MB xổ CN), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#1:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MB): **95**
- Hit rate: **29.41%**
- Baseline (random): **23.79%**
- **LIFT: +5.63pp**
- p-value: 0.0105

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bắc Ninh | 323 | 95 | 29.41% | [24.7-34.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-04-08 | 2026-04-05 | 41 | Bắc Ninh |
| 2026-03-04 | 2026-03-01 | 92 | Bắc Ninh |
| 2026-02-25 | 2026-02-22 | 30 | Bắc Ninh |

---

### Rule #6 — `MB:G7#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1** từ đài **Thái Bình** (đài MB xổ CN), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#1:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MB): **95**
- Hit rate: **29.41%**
- Baseline (random): **23.79%**
- **LIFT: +5.63pp**
- p-value: 0.0105

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bắc Ninh | 323 | 95 | 29.41% | [24.7-34.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-04-08 | 2026-04-05 | 41 | Bắc Ninh |
| 2026-03-04 | 2026-03-01 | 92 | Bắc Ninh |
| 2026-02-25 | 2026-02-22 | 30 | Bắc Ninh |

---

### Rule #7 — `MB:G7#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1** từ đài **Thái Bình** (đài MB xổ CN), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#1:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MB): **95**
- Hit rate: **29.41%**
- Baseline (random): **23.79%**
- **LIFT: +5.63pp**
- p-value: 0.0105

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bắc Ninh | 323 | 95 | 29.41% | [24.7-34.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-04-08 | 2026-04-05 | 41 | Bắc Ninh |
| 2026-03-04 | 2026-03-01 | 92 | Bắc Ninh |
| 2026-02-25 | 2026-02-22 | 30 | Bắc Ninh |

---

### Rule #8 — `MB:G2#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1** từ đài **Quảng Ninh** (đài MB xổ T3), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G2#1:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **95**
- Hit rate: **29.14%**
- Baseline (random): **23.79%**
- **LIFT: +5.36pp**
- p-value: 0.0137

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bắc Ninh | 326 | 79 | 24.23% | [19.9-29.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-27 | 2026-05-26 | 93 | Bắc Ninh |
| 2026-04-29 | 2026-04-28 | 44 | Bắc Ninh |
| 2026-04-22 | 2026-04-21 | 79 | Bắc Ninh |

---

### Rule #9 — `MT:G7#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1** từ GOM tất cả 2 đài MT xổ T2 (**Thừa Thiên Huế, Phú Yên**), ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MT:G7#1:D-2, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **153**
- Hit rate: **46.93%**
- Baseline (random): **41.67%**
- **LIFT: +5.26pp**
- p-value: 0.0307

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bắc Ninh | 326 | 153 | 46.93% | [41.6-52.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-13 | 2026-05-11 | 14, 92 | Bắc Ninh |
| 2026-05-06 | 2026-05-04 | 13, 51 | Bắc Ninh |
| 2026-04-08 | 2026-04-06 | 08, 26 | Bắc Ninh |

---

### Rule #10 — `MN:G3#2:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 2** từ GOM tất cả 3 đài MN xổ T2 (**TP. HCM, Đồng Tháp, Cà Mau**), ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MN:G3#2:D-2, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **196**
- Hit rate: **60.12%**
- Baseline (random): **54.91%**
- **LIFT: +5.21pp**
- p-value: 0.0332

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bắc Ninh | 326 | 196 | 60.12% | [54.7-65.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-27 | 2026-05-25 | 58, 73, 74 | Bắc Ninh |
| 2026-04-29 | 2026-04-27 | 05, 27, 87 | Bắc Ninh |
| 2026-04-22 | 2026-04-20 | 23, 75, 91 | Bắc Ninh |

---

### Rule #11 — `MN:DB#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1** từ GOM tất cả 3 đài MN xổ T3 (**Bến Tre, Vũng Tàu, Bạc Liêu**), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MN:DB#1:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **194**
- Hit rate: **59.33%**
- Baseline (random): **54.57%**
- **LIFT: +4.75pp**
- p-value: 0.0474

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bắc Ninh | 327 | 194 | 59.33% | [53.9-64.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-20 | 2026-05-19 | 27, 50, 84 | Bắc Ninh |
| 2026-05-13 | 2026-05-12 | 10, 48, 85 | Bắc Ninh |
| 2026-05-06 | 2026-05-05 | 09, 46, 93 | Bắc Ninh |

---

### Rule #12 — `MB:DB#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1** từ đài **Quảng Ninh** (đài MB xổ T3), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:DB#1:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.53%**
- Baseline (random): **23.79%**
- **LIFT: +4.74pp**
- p-value: 0.0258

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bắc Ninh | 326 | 78 | 23.93% | [19.6-28.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-27 | 2026-05-26 | 11 | Bắc Ninh |
| 2026-05-13 | 2026-05-12 | 33 | Bắc Ninh |
| 2026-05-06 | 2026-05-05 | 12 | Bắc Ninh |

---


## MB × Thứ Năm (T5)

**Đài hoạt động ngày này**:
- Hà Nội

**Coverage trong cell này**: 296 rule có data, **12 đạt p<0.05**, **2 BH-pass** ⭐.

### Rule #1 ⭐ — `MB:G2#2:D-1`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 2** từ đài **Bắc Ninh** (đài MB xổ T4), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G2#2:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **99**
- Hit rate: **30.28%**
- Baseline (random): **23.79%**
- **LIFT: +6.49pp**
- p-value: 0.0036
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 327 | 99 | 30.28% | [25.6-35.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-04-16 | 2026-04-15 | 78 | Hà Nội |
| 2026-04-02 | 2026-04-01 | 11 | Hà Nội |
| 2026-03-19 | 2026-03-18 | 81 | Hà Nội |

---

### Rule #2 ⭐ — `MB:DB#1:D-3`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1** từ đài **Hà Nội** (đài MB xổ T2), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:DB#1:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MB): **97**
- Hit rate: **30.03%**
- Baseline (random): **23.79%**
- **LIFT: +6.25pp**
- p-value: 0.0051
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 323 | 97 | 30.03% | [25.3-35.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-21 | 2026-05-18 | 61 | Hà Nội |
| 2026-05-14 | 2026-05-11 | 17 | Hà Nội |
| 2026-05-07 | 2026-05-04 | 51 | Hà Nội |

---

### Rule #3 — `MN:G3#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1** từ GOM tất cả 3 đài MN xổ T2 (**TP. HCM, Đồng Tháp, Cà Mau**), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MN:G3#1:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **199**
- Hit rate: **61.23%**
- Baseline (random): **54.95%**
- **LIFT: +6.28pp**
- p-value: 0.0132

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 325 | 199 | 61.23% | [55.8-66.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-28 | 2026-05-25 | 50, 61, 92 | Hà Nội |
| 2026-05-14 | 2026-05-11 | 17, 87, 96 | Hà Nội |
| 2026-04-30 | 2026-04-27 | 27, 61, 96 | Hà Nội |

---

### Rule #4 — `MB:G2#2:D-1`

**Strength**: STRONG

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 2** từ đài **Bắc Ninh** (đài MB xổ T4), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G2#2:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **98**
- Hit rate: **29.97%**
- Baseline (random): **23.79%**
- **LIFT: +6.18pp**
- p-value: 0.0052

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 327 | 99 | 30.28% | [25.6-35.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-04-16 | 2026-04-15 | 78 | Hà Nội |
| 2026-04-02 | 2026-04-01 | 11 | Hà Nội |
| 2026-03-19 | 2026-03-18 | 81 | Hà Nội |

---

### Rule #5 — `MN:G2#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1** từ GOM tất cả 3 đài MN xổ T4 (**Đồng Nai, Cần Thơ, Sóc Trăng**), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MN:G2#1:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **198**
- Hit rate: **60.92%**
- Baseline (random): **54.98%**
- **LIFT: +5.94pp**
- p-value: 0.0180

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 325 | 198 | 60.92% | [55.5-66.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-04-30 | 2026-04-29 | 05, 77, 79 | Hà Nội |
| 2026-04-23 | 2026-04-22 | 19, 46, 75 | Hà Nội |
| 2026-04-09 | 2026-04-08 | 03, 36, 64 | Hà Nội |

---

### Rule #6 — `MT:G3#2:D`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 2** từ GOM tất cả 3 đài MT xổ T5 (**Bình Định, Quảng Trị, Quảng Bình**), ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MT:G3#2:D, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **198**
- Hit rate: **60.55%**
- Baseline (random): **55.25%**
- **LIFT: +5.30pp**
- p-value: 0.0306

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 327 | 198 | 60.55% | [55.2-65.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-28 | 2026-05-28 | 11, 19, 47 | Hà Nội |
| 2026-05-14 | 2026-05-14 | 70, 92, 96 | Hà Nội |
| 2026-05-07 | 2026-05-07 | 25, 79, 94 | Hà Nội |

---

### Rule #7 — `MN:G8#1:D`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 8 bộ 1** từ GOM tất cả 3 đài MN xổ T5 (**Tây Ninh, An Giang, Bình Thuận**), ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MN:G8#1:D, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **198**
- Hit rate: **60.55%**
- Baseline (random): **55.36%**
- **LIFT: +5.19pp**
- p-value: 0.0335

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 327 | 198 | 60.55% | [55.2-65.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-14 | 2026-05-14 | 10, 61, 90 | Hà Nội |
| 2026-04-30 | 2026-04-30 | 10, 49, 51 | Hà Nội |
| 2026-04-23 | 2026-04-23 | 31, 56, 92 | Hà Nội |

---

### Rule #8 — `MB:G4#4:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 4** từ đài **Bắc Ninh** (đài MB xổ T4), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G4#4:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.44%**
- Baseline (random): **23.79%**
- **LIFT: +4.65pp**
- p-value: 0.0279

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 327 | 79 | 24.16% | [19.8-29.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-14 | 2026-05-13 | 46 | Hà Nội |
| 2026-04-16 | 2026-04-15 | 10 | Hà Nội |
| 2026-04-09 | 2026-04-08 | 30 | Hà Nội |

---

### Rule #9 — `MB:G4#2:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 2** từ đài **Hà Nội** (đài MB xổ T2), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G4#2:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MB): **91**
- Hit rate: **28.17%**
- Baseline (random): **23.79%**
- **LIFT: +4.39pp**
- p-value: 0.0370

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 323 | 91 | 28.17% | [23.6-33.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-07 | 2026-05-04 | 45 | Hà Nội |
| 2026-04-23 | 2026-04-20 | 21 | Hà Nội |
| 2026-04-02 | 2026-03-30 | 62 | Hà Nội |

---

### Rule #10 — `MB:G4#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 1** từ đài **Hà Nội** (đài MB xổ T2), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G4#1:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MB): **91**
- Hit rate: **28.17%**
- Baseline (random): **23.79%**
- **LIFT: +4.39pp**
- p-value: 0.0370

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 323 | 83 | 25.70% | [21.2-30.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-21 | 2026-05-18 | 50 | Hà Nội |
| 2026-05-14 | 2026-05-11 | 46 | Hà Nội |
| 2026-04-30 | 2026-04-27 | 98 | Hà Nội |

---

### Rule #11 — `MB:G4#3:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 3** từ đài **Hà Nội** (đài MB xổ T2), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G4#3:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MB): **91**
- Hit rate: **28.17%**
- Baseline (random): **23.79%**
- **LIFT: +4.39pp**
- p-value: 0.0370

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 323 | 83 | 25.70% | [21.2-30.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-14 | 2026-05-11 | 69 | Hà Nội |
| 2026-05-07 | 2026-05-04 | 30 | Hà Nội |
| 2025-12-25 | 2025-12-22 | 19 | Hà Nội |

---

### Rule #12 — `MB:DB#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1** từ đài **Bắc Ninh** (đài MB xổ T4), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:DB#1:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.13%**
- Baseline (random): **23.79%**
- **LIFT: +4.35pp**
- p-value: 0.0374

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hà Nội | 327 | 74 | 22.63% | [18.4-27.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-21 | 2026-05-20 | 68 | Hà Nội |
| 2026-02-26 | 2026-02-25 | 53 | Hà Nội |
| 2025-11-27 | 2025-11-26 | 97 | Hà Nội |

---


## MB × Thứ Sáu (T6)

**Đài hoạt động ngày này**:
- Hải Phòng

**Coverage trong cell này**: 296 rule có data, **13 đạt p<0.05**, **0 BH-pass** ⭐.

### Rule #1 — `MB:G4#3:D-1`

**Strength**: STRONG

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 3** từ đài **Hà Nội** (đài MB xổ T5), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G4#3:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **97**
- Hit rate: **29.75%**
- Baseline (random): **23.79%**
- **LIFT: +5.97pp**
- p-value: 0.0068

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hải Phòng | 326 | 74 | 22.70% | [18.5-27.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-29 | 2026-05-28 | 16 | Hải Phòng |
| 2026-04-17 | 2026-04-16 | 81 | Hải Phòng |
| 2026-03-06 | 2026-03-05 | 85 | Hải Phòng |

---

### Rule #2 — `MN:G7#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1** từ GOM tất cả 3 đài MN xổ T4 (**Đồng Nai, Cần Thơ, Sóc Trăng**), ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MN:G7#1:D-2, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **197**
- Hit rate: **60.62%**
- Baseline (random): **54.98%**
- **LIFT: +5.63pp**
- p-value: 0.0236

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hải Phòng | 325 | 197 | 60.62% | [55.2-65.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-22 | 2026-05-20 | 10, 23, 93 | Hải Phòng |
| 2026-05-01 | 2026-04-29 | 25, 81, 99 | Hải Phòng |
| 2026-04-24 | 2026-04-22 | 19, 42, 75 | Hải Phòng |

---

### Rule #3 — `MT:G1#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1** từ GOM tất cả 2 đài MT xổ T3 (**Đắk Lắk, Quảng Nam**), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MT:G1#1:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **153**
- Hit rate: **46.93%**
- Baseline (random): **41.72%**
- **LIFT: +5.21pp**
- p-value: 0.0320

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hải Phòng | 326 | 153 | 46.93% | [41.6-52.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-15 | 2026-05-12 | 21, 85 | Hải Phòng |
| 2026-05-08 | 2026-05-05 | 32, 93 | Hải Phòng |
| 2026-04-03 | 2026-03-31 | 24, 56 | Hải Phòng |

---

### Rule #4 — `MB:G4#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 1** từ đài **Bắc Ninh** (đài MB xổ T4), ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G4#1:D-2, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **94**
- Hit rate: **28.92%**
- Baseline (random): **23.79%**
- **LIFT: +5.14pp**
- p-value: 0.0174

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hải Phòng | 325 | 68 | 20.92% | [16.9-25.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-22 | 2026-05-20 | 90 | Hải Phòng |
| 2026-05-08 | 2026-05-06 | 46 | Hải Phòng |
| 2026-04-10 | 2026-04-08 | 20 | Hải Phòng |

---

### Rule #5 — `MN:G2#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1** từ GOM tất cả 3 đài MN xổ T4 (**Đồng Nai, Cần Thơ, Sóc Trăng**), ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MN:G2#1:D-2, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **195**
- Hit rate: **60.00%**
- Baseline (random): **54.98%**
- **LIFT: +5.02pp**
- p-value: 0.0390

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hải Phòng | 325 | 195 | 60.00% | [54.6-65.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-29 | 2026-05-27 | 20, 71, 93 | Hải Phòng |
| 2026-05-22 | 2026-05-20 | 15, 29, 90 | Hải Phòng |
| 2026-05-15 | 2026-05-13 | 09, 47, 58 | Hải Phòng |

---

### Rule #6 — `MN:G3#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1** từ GOM tất cả 3 đài MN xổ T3 (**Bến Tre, Vũng Tàu, Bạc Liêu**), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MN:G3#1:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **194**
- Hit rate: **59.51%**
- Baseline (random): **54.65%**
- **LIFT: +4.86pp**
- p-value: 0.0438

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hải Phòng | 326 | 194 | 59.51% | [54.1-64.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-29 | 2026-05-26 | 16, 45, 82 | Hải Phòng |
| 2026-05-08 | 2026-05-05 | 01, 58, 82 | Hải Phòng |
| 2026-05-01 | 2026-04-28 | 61, 80, 81 | Hải Phòng |

---

### Rule #7 — `MB:G7#3:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 3** từ đài **Hà Nội** (đài MB xổ T5), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#3:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.22%**
- Baseline (random): **23.79%**
- **LIFT: +4.44pp**
- p-value: 0.0347

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hải Phòng | 326 | 92 | 28.22% | [23.6-33.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-29 | 2026-05-28 | 51 | Hải Phòng |
| 2026-05-22 | 2026-05-21 | 95 | Hải Phòng |
| 2026-04-10 | 2026-04-09 | 72 | Hải Phòng |

---

### Rule #8 — `MB:G6#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 1** từ đài **Hà Nội** (đài MB xổ T5), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G6#1:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.22%**
- Baseline (random): **23.79%**
- **LIFT: +4.44pp**
- p-value: 0.0347

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hải Phòng | 326 | 69 | 21.17% | [17.1-25.9]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-08 | 2026-05-07 | 56 | Hải Phòng |
| 2026-04-17 | 2026-04-16 | 11 | Hải Phòng |
| 2026-03-20 | 2026-03-19 | 15 | Hải Phòng |

---

### Rule #9 — `MB:G7#3:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 3** từ đài **Hà Nội** (đài MB xổ T5), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#3:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.22%**
- Baseline (random): **23.79%**
- **LIFT: +4.44pp**
- p-value: 0.0347

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hải Phòng | 326 | 92 | 28.22% | [23.6-33.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-29 | 2026-05-28 | 51 | Hải Phòng |
| 2026-05-22 | 2026-05-21 | 95 | Hải Phòng |
| 2026-04-10 | 2026-04-09 | 72 | Hải Phòng |

---

### Rule #10 — `MB:G7#3:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 3** từ đài **Hà Nội** (đài MB xổ T5), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#3:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.22%**
- Baseline (random): **23.79%**
- **LIFT: +4.44pp**
- p-value: 0.0347

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hải Phòng | 326 | 92 | 28.22% | [23.6-33.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-29 | 2026-05-28 | 51 | Hải Phòng |
| 2026-05-22 | 2026-05-21 | 95 | Hải Phòng |
| 2026-04-10 | 2026-04-09 | 72 | Hải Phòng |

---


## MB × Thứ Bảy (T7)

**Đài hoạt động ngày này**:
- Nam Định

**Coverage trong cell này**: 296 rule có data, **7 đạt p<0.05**, **0 BH-pass** ⭐.

### Rule #1 — `MN:G3#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1** từ GOM tất cả 3 đài MN xổ T4 (**Đồng Nai, Cần Thơ, Sóc Trăng**), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MN:G3#1:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **197**
- Hit rate: **60.62%**
- Baseline (random): **54.87%**
- **LIFT: +5.74pp**
- p-value: 0.0214

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Nam Định | 325 | 197 | 60.62% | [55.2-65.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-27 | 24, 84 | Nam Định |
| 2026-05-23 | 2026-05-20 | 45, 57, 96 | Nam Định |
| 2026-05-16 | 2026-05-13 | 34, 68, 83 | Nam Định |

---

### Rule #2 — `MT:G1#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1** từ GOM tất cả 2 đài MT xổ T6 (**Gia Lai, Ninh Thuận**), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MT:G1#1:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **328**
- Số ngày trúng (ANY station of MB): **154**
- Hit rate: **46.95%**
- Baseline (random): **41.67%**
- **LIFT: +5.28pp**
- p-value: 0.0298

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Nam Định | 328 | 154 | 46.95% | [41.6-52.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-29 | 02, 45 | Nam Định |
| 2026-05-23 | 2026-05-22 | 48, 67 | Nam Định |
| 2026-05-09 | 2026-05-08 | 66, 72 | Nam Định |

---

### Rule #3 — `MT:G3#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1** từ GOM tất cả 3 đài MT xổ T5 (**Bình Định, Quảng Trị, Quảng Bình**), ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MT:G3#1:D-2, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **198**
- Hit rate: **60.55%**
- Baseline (random): **55.36%**
- **LIFT: +5.19pp**
- p-value: 0.0335

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Nam Định | 327 | 198 | 60.55% | [55.2-65.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-28 | 01, 24, 96 | Nam Định |
| 2026-05-23 | 2026-05-21 | 11, 60, 73 | Nam Định |
| 2026-05-16 | 2026-05-14 | 09, 65, 81 | Nam Định |

---

### Rule #4 — `MB:G4#4:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 4** từ đài **Hà Nội** (đài MB xổ T5), ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G4#4:D-2, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.62%**
- Baseline (random): **23.79%**
- **LIFT: +4.83pp**
- p-value: 0.0239

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Nam Định | 325 | 87 | 26.77% | [22.2-31.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-23 | 2026-05-21 | 68 | Nam Định |
| 2026-05-09 | 2026-05-07 | 50 | Nam Định |
| 2026-04-25 | 2026-04-23 | 42 | Nam Định |

---

### Rule #5 — `MB:DB#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1** từ đài **Hải Phòng** (đài MB xổ T6), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:DB#1:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.44%**
- Baseline (random): **23.79%**
- **LIFT: +4.65pp**
- p-value: 0.0279

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Nam Định | 327 | 82 | 25.08% | [20.7-30.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-09 | 2026-05-08 | 47 | Nam Định |
| 2026-05-02 | 2026-05-01 | 37 | Nam Định |
| 2026-04-11 | 2026-04-10 | 20 | Nam Định |

---

### Rule #6 — `MB:G4#3:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 3** từ đài **Hải Phòng** (đài MB xổ T6), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G4#3:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.13%**
- Baseline (random): **23.79%**
- **LIFT: +4.35pp**
- p-value: 0.0374

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Nam Định | 327 | 69 | 21.10% | [17.0-25.9]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-04-11 | 2026-04-10 | 80 | Nam Định |
| 2026-03-21 | 2026-03-20 | 16 | Nam Định |
| 2026-03-14 | 2026-03-13 | 21 | Nam Định |

---

### Rule #7 — `MB:G1#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1** từ đài **Bắc Ninh** (đài MB xổ T4), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G1#1:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **324**
- Số ngày trúng (ANY station of MB): **91**
- Hit rate: **28.09%**
- Baseline (random): **23.79%**
- **LIFT: +4.30pp**
- p-value: 0.0398

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Nam Định | 324 | 84 | 25.93% | [21.5-31.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-27 | 73 | Nam Định |
| 2026-04-18 | 2026-04-15 | 68 | Nam Định |
| 2026-03-21 | 2026-03-18 | 70 | Nam Định |

---

### Rule #8 — `MT:G5#1:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1** từ GOM tất cả 2 đài MT xổ T6 (**Gia Lai, Ninh Thuận**), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MT:G5#1:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **328**
- Số ngày trúng (ANY station of MB): **150**
- Hit rate: **45.73%**
- Baseline (random): **41.77%**
- **LIFT: +3.96pp**
- p-value: 0.0809

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Nam Định | 328 | 150 | 45.73% | [40.4-51.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-29 | 40, 80 | Nam Định |
| 2026-05-23 | 2026-05-22 | 05, 47 | Nam Định |
| 2026-05-16 | 2026-05-15 | 85, 99 | Nam Định |

---


## MB × Chủ Nhật (CN)

**Đài hoạt động ngày này**:
- Thái Bình

**Coverage trong cell này**: 296 rule có data, **14 đạt p<0.05**, **0 BH-pass** ⭐.

### Rule #1 — `MB:G2#2:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 2** từ đài **Hải Phòng** (đài MB xổ T6), ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G2#2:D-2, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **96**
- Hit rate: **29.36%**
- Baseline (random): **23.79%**
- **LIFT: +5.57pp**
- p-value: 0.0107

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Thái Bình | 327 | 71 | 21.71% | [17.6-26.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-10 | 2026-05-08 | 93 | Thái Bình |
| 2026-03-22 | 2026-03-20 | 46 | Thái Bình |
| 2026-01-18 | 2026-01-16 | 66 | Thái Bình |

---

### Rule #2 — `MB:G4#3:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 3** từ đài **Hà Nội** (đài MB xổ T5), ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G4#3:D-3, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **94**
- Hit rate: **28.92%**
- Baseline (random): **23.79%**
- **LIFT: +5.14pp**
- p-value: 0.0174

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Thái Bình | 325 | 79 | 24.31% | [20.0-29.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-03 | 2026-04-30 | 84 | Thái Bình |
| 2026-04-19 | 2026-04-16 | 81 | Thái Bình |
| 2026-01-04 | 2026-01-01 | 76 | Thái Bình |

---

### Rule #3 — `MB:G6#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 1** từ đài **Hải Phòng** (đài MB xổ T6), ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G6#1:D-2, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **94**
- Hit rate: **28.75%**
- Baseline (random): **23.79%**
- **LIFT: +4.96pp**
- p-value: 0.0206

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Thái Bình | 327 | 78 | 23.85% | [19.6-28.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-17 | 2026-05-15 | 88 | Thái Bình |
| 2026-04-12 | 2026-04-10 | 37 | Thái Bình |
| 2026-03-15 | 2026-03-13 | 42 | Thái Bình |

---

### Rule #4 — `MB:G1#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1** từ đài **Nam Định** (đài MB xổ T7), ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G1#1:D-1, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **328**
- Số ngày trúng (ANY station of MB): **94**
- Hit rate: **28.66%**
- Baseline (random): **23.79%**
- **LIFT: +4.87pp**
- p-value: 0.0223

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Thái Bình | 328 | 72 | 21.95% | [17.8-26.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-10 | 2026-05-09 | 52 | Thái Bình |
| 2026-05-03 | 2026-05-02 | 57 | Thái Bình |
| 2026-04-19 | 2026-04-18 | 13 | Thái Bình |

---

### Rule #5 — `MN:G1#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1** từ GOM tất cả 3 đài MN xổ T6 (**Vĩnh Long, Bình Dương, Trà Vinh**), ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MN:G1#1:D-2, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **328**
- Số ngày trúng (ANY station of MB): **195**
- Hit rate: **59.45%**
- Baseline (random): **54.73%**
- **LIFT: +4.72pp**
- p-value: 0.0482

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Thái Bình | 328 | 195 | 59.45% | [54.1-64.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-31 | 2026-05-29 | 20, 42 | Thái Bình |
| 2026-05-10 | 2026-05-08 | 26, 35, 99 | Thái Bình |
| 2026-05-03 | 2026-05-01 | 23, 27, 41 | Thái Bình |

---

### Rule #6 — `MB:G7#4:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4** từ đài **Hải Phòng** (đài MB xổ T6), ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G7#4:D-2, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.44%**
- Baseline (random): **23.79%**
- **LIFT: +4.65pp**
- p-value: 0.0279

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Thái Bình | 327 | 77 | 23.55% | [19.3-28.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-31 | 2026-05-29 | 83 | Thái Bình |
| 2026-02-15 | 2026-02-13 | 01 | Thái Bình |
| 2025-12-14 | 2025-12-12 | 76 | Thái Bình |

---

### Rule #7 — `MB:G6#3:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 3** từ đài **Hải Phòng** (đài MB xổ T6), ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G6#3:D-2, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.44%**
- Baseline (random): **23.79%**
- **LIFT: +4.65pp**
- p-value: 0.0279

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Thái Bình | 327 | 86 | 26.30% | [21.8-31.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-04-26 | 2026-04-24 | 71 | Thái Bình |
| 2026-04-12 | 2026-04-10 | 23 | Thái Bình |
| 2026-03-29 | 2026-03-27 | 30 | Thái Bình |

---

### Rule #8 — `MB:G2#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1** từ đài **Hải Phòng** (đài MB xổ T6), ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D. (Nguồn = MB:G2#1:D-2, đếm union nếu nhiều đài.)

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.44%**
- Baseline (random): **23.79%**
- **LIFT: +4.65pp**
- p-value: 0.0279

**Per-station breakdown — đài ĐÍCH (MB) nào trúng nhiều nhất** (source đài đã ghi trong Mô tả; source breakdown chi tiết: `V10670_SOURCE_STATION_BREAKDOWN.json`):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Thái Bình | 327 | 84 | 25.69% | [21.2-30.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-17 | 2026-05-15 | 16 | Thái Bình |
| 2026-04-05 | 2026-04-03 | 58 | Thái Bình |
| 2026-03-29 | 2026-03-27 | 49 | Thái Bình |

---


## Tổng kết

**Tài liệu này liệt kê các rule mạnh nhất cho target = MB** qua 7 thứ trong tuần, mỗi thứ với top 8-12 rules ranked theo lift.

### Disclaimer quan trọng

1. **Rule áp dụng ở mức "ANY station"** — nghĩa là source LAST2 cần xuất hiện trong **bất kỳ đài nào** của MB ngày D.
2. **Per-station breakdown** giúp anh biết đài nào carry nhiều signal nhất, nhưng baseline random thì 1 đài có hit thấp hơn ANY-station.
3. **Worked examples** chỉ là 3 ngày gần nhất. KHÔNG đảm bảo rule sẽ tiếp tục trúng — đang trong forward audit 90 ngày.
4. **BH-pass ⭐ = gold standard** sau multiple-testing correction.
5. Tất cả rule này hiện ở **PRE_REGISTER_FORWARD_AUDIT** — chưa live, chưa được hệ thống dùng. Sau 90 ngày audit em sẽ classify lại.

---
**See also**: V10667_RULES_INDEX.md (hub document)