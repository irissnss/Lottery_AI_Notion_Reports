# V10667 Rules cho TARGET = MT (Đích = Miền MT)

> **Generated**: 2026-06-02T01:27:09+07:00
> **Target region**: MT
> **Audit window**: Forward 90d, anchor 2026-06-02 → earliest closeout 2026-08-31

## ⚠️ Đọc trước: Quy ước Đánh Số Bộ Số

Rule sử dụng ký hiệu `Giải X bộ Y` (hoặc `GX#Y`). Bộ được đếm theo vị trí trên bảng kết quả.

**Nguồn MB cho rule này** (có nhiều bộ): G2 (2), **G4 (4 — owner mới bổ sung ⭐)**, G6 (3), G7 (4).
**Nguồn MN/MT G3 (source-only, 2 bộ)**: G3 bộ 1 (trái) + G3 bộ 2 (phải).

**G.4 MB position map** (4 bộ):
```
Giải 4 bộ 1 [top-left]    Giải 4 bộ 2 [top-right]
Giải 4 bộ 3 [bottom-left] Giải 4 bộ 4 [bottom-right]
```

**Xem đầy đủ legend**: [📖 V10667_BO_NUMBERING_LEGEND.md](./V10667_BO_NUMBERING_LEGEND.md)

## Giới thiệu — MT

Miền Trung (2-3 đài/ngày luân phiên theo thứ). Trung gian giữa MN và MB về số stations. Avg ~34 tail/ngày. T5 Thursday và T7 Saturday là 2 "hot days" với rất nhiều BH-pass rule.

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

## MT × Thứ Hai (T2)

**Đài hoạt động ngày này**:
- Huế
- Phú Yên

**Coverage trong cell này**: 116 rule có data, **0 đạt p<0.05**, **0 BH-pass** ⭐.

### Rule #1 — `MT:G1#1:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Hai (T2) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MT** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **331**
- Số ngày trúng (ANY station of MT): **193**
- Hit rate: **58.31%**
- Baseline (random): **55.84%**
- **LIFT: +2.47pp**
- p-value: 0.1980

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Phú Yên | 331 | 117 | 35.35% | [30.4-40.6]% |
| Huế | 0 | 0 | 0.00% | [0.0-0.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-18 | 2026-05-15 | 18, 98 | Phú Yên |
| 2026-04-13 | 2026-04-10 | 59, 62 | Phú Yên |
| 2026-04-06 | 2026-04-03 | 15, 83 | Phú Yên |

---

### Rule #2 — `MB:DB#1:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Hai (T2) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MT): **117**
- Hit rate: **35.78%**
- Baseline (random): **33.75%**
- **LIFT: +2.03pp**
- p-value: 0.2369

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Phú Yên | 327 | 57 | 17.43% | [13.7-21.9]% |
| Huế | 0 | 0 | 0.00% | [0.0-0.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-06-01 | 2026-05-31 | 42 | Phú Yên |
| 2026-05-25 | 2026-05-24 | 04 | Phú Yên |
| 2026-04-20 | 2026-04-19 | 25 | Phú Yên |

---

### Rule #3 — `MB:G7#4:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Hai (T2) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MT): **116**
- Hit rate: **35.47%**
- Baseline (random): **33.75%**
- **LIFT: +1.72pp**
- p-value: 0.2744

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Phú Yên | 327 | 67 | 20.49% | [16.5-25.2]% |
| Huế | 0 | 0 | 0.00% | [0.0-0.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-04-20 | 2026-04-18 | 53 | Phú Yên |
| 2026-04-13 | 2026-04-11 | 80 | Phú Yên |
| 2026-03-23 | 2026-03-21 | 05 | Phú Yên |

---

### Rule #4 — `MB:DB#1:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Hai (T2) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MT): **114**
- Hit rate: **34.86%**
- Baseline (random): **33.75%**
- **LIFT: +1.11pp**
- p-value: 0.3573

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Phú Yên | 327 | 61 | 18.65% | [14.8-23.2]% |
| Huế | 0 | 0 | 0.00% | [0.0-0.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-25 | 2026-05-22 | 39 | Phú Yên |
| 2026-05-18 | 2026-05-15 | 94 | Phú Yên |
| 2026-05-04 | 2026-05-01 | 37 | Phú Yên |

---

### Rule #5 — `MB:G6#1:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Hai (T2) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 1 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MT): **114**
- Hit rate: **34.86%**
- Baseline (random): **33.75%**
- **LIFT: +1.11pp**
- p-value: 0.3573

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Phú Yên | 327 | 66 | 20.18% | [16.2-24.9]% |
| Huế | 0 | 0 | 0.00% | [0.0-0.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-25 | 2026-05-22 | 76 | Phú Yên |
| 2026-05-18 | 2026-05-15 | 88 | Phú Yên |
| 2026-03-30 | 2026-03-27 | 38 | Phú Yên |

---

### Rule #6 — `MB:G2#1:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Hai (T2) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MT): **113**
- Hit rate: **34.56%**
- Baseline (random): **33.75%**
- **LIFT: +0.80pp**
- p-value: 0.4018

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Phú Yên | 327 | 70 | 21.41% | [17.3-26.2]% |
| Huế | 0 | 0 | 0.00% | [0.0-0.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-18 | 2026-05-16 | 24 | Phú Yên |
| 2026-04-27 | 2026-04-25 | 96 | Phú Yên |
| 2026-04-06 | 2026-04-04 | 16 | Phú Yên |

---

### Rule #7 — `MT:G2#1:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Hai (T2) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MT** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **330**
- Số ngày trúng (ANY station of MT): **192**
- Hit rate: **58.18%**
- Baseline (random): **57.73%**
- **LIFT: +0.46pp**
- p-value: 0.4555

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Phú Yên | 330 | 115 | 34.85% | [29.9-40.1]% |
| Huế | 0 | 0 | 0.00% | [0.0-0.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-25 | 2026-05-24 | 00, 06, 11 | Phú Yên |
| 2026-04-20 | 2026-04-19 | 70, 73, 78 | Phú Yên |
| 2026-03-23 | 2026-03-22 | 47, 85, 87 | Phú Yên |

---

### Rule #8 — `MB:G7#2:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Hai (T2) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 2 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MT): **110**
- Hit rate: **33.64%**
- Baseline (random): **33.75%**
- **LIFT: +-0.11pp**
- p-value: 0.5407

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Phú Yên | 327 | 62 | 18.96% | [15.1-23.6]% |
| Huế | 0 | 0 | 0.00% | [0.0-0.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-03-30 | 2026-03-28 | 61 | Phú Yên |
| 2026-02-09 | 2026-02-07 | 17 | Phú Yên |
| 2026-02-02 | 2026-01-31 | 51 | Phú Yên |

---


## MT × Thứ Ba (T3)

**Đài hoạt động ngày này**:
- Đắk Lắk
- Quảng Nam

**Coverage trong cell này**: 116 rule có data, **1 đạt p<0.05**, **0 BH-pass** ⭐.

### Rule #1 — `MT:G1#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MT** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MT): **208**
- Hit rate: **63.22%**
- Baseline (random): **57.68%**
- **LIFT: +5.54pp**
- p-value: 0.0239

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đắk Lắk | 328 | 126 | 38.41% | [33.3-43.8]% |
| Quảng Nam | 329 | 120 | 36.47% | [31.5-41.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-19 | 2026-05-17 | 58, 85, 94 | Đắk Lắk |
| 2026-05-05 | 2026-05-03 | 09, 52, 53 | Đắk Lắk, Quảng Nam |
| 2026-04-28 | 2026-04-26 | 57, 62, 68 | Quảng Nam |

---

### Rule #2 — `MB:G2#1:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Ba (T3) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **123**
- Hit rate: **37.73%**
- Baseline (random): **33.75%**
- **LIFT: +3.98pp**
- p-value: 0.0722

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Nam | 326 | 72 | 22.09% | [17.9-26.9]% |
| Đắk Lắk | 324 | 63 | 19.44% | [15.5-24.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-19 | 2026-05-18 | 97 | Quảng Nam |
| 2026-04-28 | 2026-04-27 | 04 | Quảng Nam |
| 2026-04-21 | 2026-04-20 | 81 | Quảng Nam |

---

### Rule #3 — `MB:G7#3:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Ba (T3) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 3 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **118**
- Hit rate: **36.20%**
- Baseline (random): **33.75%**
- **LIFT: +2.44pp**
- p-value: 0.1910

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Nam | 326 | 73 | 22.39% | [18.2-27.2]% |
| Đắk Lắk | 324 | 53 | 16.36% | [12.7-20.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-26 | 2026-05-25 | 83 | Quảng Nam |
| 2026-03-10 | 2026-03-09 | 65 | Đắk Lắk |
| 2026-02-03 | 2026-02-02 | 74 | Quảng Nam |

---

### Rule #4 — `MB:G2#2:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Ba (T3) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 2 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MT): **118**
- Hit rate: **36.09%**
- Baseline (random): **33.75%**
- **LIFT: +2.33pp**
- p-value: 0.2023

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Nam | 327 | 69 | 21.10% | [17.0-25.9]% |
| Đắk Lắk | 325 | 67 | 20.62% | [16.6-25.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-26 | 2026-05-23 | 94 | Quảng Nam |
| 2026-04-21 | 2026-04-18 | 49 | Đắk Lắk |
| 2026-03-31 | 2026-03-28 | 34 | Quảng Nam |

---

### Rule #5 — `MB:G7#1:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Ba (T3) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MT): **117**
- Hit rate: **35.78%**
- Baseline (random): **33.75%**
- **LIFT: +2.03pp**
- p-value: 0.2369

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đắk Lắk | 325 | 64 | 19.69% | [15.7-24.4]% |
| Quảng Nam | 327 | 61 | 18.65% | [14.8-23.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-04-28 | 2026-04-26 | 30 | Đắk Lắk, Quảng Nam |
| 2026-04-14 | 2026-04-12 | 95 | Đắk Lắk |
| 2026-03-24 | 2026-03-22 | 80 | Đắk Lắk |

---

### Rule #6 — `MB:G4#3:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Ba (T3) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 3 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MT): **116**
- Hit rate: **35.47%**
- Baseline (random): **33.75%**
- **LIFT: +1.72pp**
- p-value: 0.2744

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Nam | 327 | 70 | 21.41% | [17.3-26.2]% |
| Đắk Lắk | 325 | 56 | 17.23% | [13.5-21.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-26 | 2026-05-23 | 55 | Đắk Lắk |
| 2026-05-19 | 2026-05-16 | 60 | Quảng Nam |
| 2026-04-14 | 2026-04-11 | 44 | Quảng Nam |

---

### Rule #7 — `MN:G2#1:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Ba (T3) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MN** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **331**
- Số ngày trúng (ANY station of MT): **236**
- Hit rate: **71.30%**
- Baseline (random): **69.82%**
- **LIFT: +1.48pp**
- p-value: 0.2995

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đắk Lắk | 329 | 160 | 48.63% | [43.3-54.0]% |
| Quảng Nam | 331 | 146 | 44.11% | [38.9-49.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-26 | 2026-05-26 | 09, 34, 88 | Quảng Nam |
| 2026-05-12 | 2026-05-12 | 00, 07, 89 | Đắk Lắk |
| 2026-04-28 | 2026-04-28 | 51, 60, 99 | Quảng Nam |

---

### Rule #8 — `MB:G4#1:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Ba (T3) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 1 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MT): **114**
- Hit rate: **34.86%**
- Baseline (random): **33.75%**
- **LIFT: +1.11pp**
- p-value: 0.3573

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đắk Lắk | 325 | 65 | 20.00% | [16.0-24.7]% |
| Quảng Nam | 327 | 61 | 18.65% | [14.8-23.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-19 | 2026-05-17 | 76 | Đắk Lắk |
| 2026-04-21 | 2026-04-19 | 69 | Đắk Lắk |
| 2026-02-10 | 2026-02-08 | 21 | Đắk Lắk |

---


## MT × Thứ Tư (T4)

**Đài hoạt động ngày này**:
- Đà Nẵng
- Khánh Hòa

**Coverage trong cell này**: 116 rule có data, **0 đạt p<0.05**, **0 BH-pass** ⭐.

### Rule #1 — `MN:DB#1:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Tư (T4) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MN** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **328**
- Số ngày trúng (ANY station of MT): **237**
- Hit rate: **72.26%**
- Baseline (random): **69.92%**
- **LIFT: +2.33pp**
- p-value: 0.1947

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đà Nẵng | 327 | 152 | 46.48% | [41.1-51.9]% |
| Khánh Hòa | 328 | 150 | 45.73% | [40.4-51.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-27 | 2026-05-26 | 34, 56 | Đà Nẵng, Khánh Hòa |
| 2026-05-20 | 2026-05-19 | 27, 50, 84 | Đà Nẵng |
| 2026-05-13 | 2026-05-12 | 10, 48, 85 | Đà Nẵng, Khánh Hòa |

---

### Rule #2 — `MB:G4#4:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Tư (T4) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 4 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **324**
- Số ngày trúng (ANY station of MT): **115**
- Hit rate: **35.49%**
- Baseline (random): **33.75%**
- **LIFT: +1.74pp**
- p-value: 0.2730

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Khánh Hòa | 324 | 67 | 20.68% | [16.6-25.4]% |
| Đà Nẵng | 323 | 54 | 16.72% | [13.1-21.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-27 | 2026-05-26 | 92 | Khánh Hòa |
| 2026-05-06 | 2026-05-05 | 34 | Khánh Hòa |
| 2026-04-29 | 2026-04-28 | 98 | Khánh Hòa |

---

### Rule #3 — `MB:G1#1:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Tư (T4) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MB** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **115**
- Hit rate: **35.28%**
- Baseline (random): **33.75%**
- **LIFT: +1.52pp**
- p-value: 0.3005

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Khánh Hòa | 326 | 68 | 20.86% | [16.8-25.6]% |
| Đà Nẵng | 325 | 66 | 20.31% | [16.3-25.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-13 | 2026-05-13 | 61 | Khánh Hòa |
| 2026-04-08 | 2026-04-08 | 35 | Đà Nẵng |
| 2026-03-25 | 2026-03-25 | 66 | Khánh Hòa |

---

### Rule #4 — `MN:G7#1:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Tư (T4) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1 miền MN** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MT): **231**
- Hit rate: **70.64%**
- Baseline (random): **70.00%**
- **LIFT: +0.65pp**
- p-value: 0.4230

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đà Nẵng | 326 | 146 | 44.79% | [39.5-50.2]% |
| Khánh Hòa | 327 | 144 | 44.04% | [38.8-49.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-27 | 2026-05-24 | 41, 51, 60 | Khánh Hòa |
| 2026-05-20 | 2026-05-17 | 49, 64, 88 | Khánh Hòa |
| 2026-05-13 | 2026-05-10 | 31, 43, 68 | Khánh Hòa |

---

### Rule #5 — `MB:G7#2:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Tư (T4) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 2 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **324**
- Số ngày trúng (ANY station of MT): **111**
- Hit rate: **34.26%**
- Baseline (random): **33.75%**
- **LIFT: +0.51pp**
- p-value: 0.4468

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đà Nẵng | 323 | 67 | 20.74% | [16.7-25.5]% |
| Khánh Hòa | 324 | 57 | 17.59% | [13.8-22.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-27 | 2026-05-24 | 58 | Khánh Hòa |
| 2026-05-13 | 2026-05-10 | 15 | Đà Nẵng |
| 2026-04-29 | 2026-04-26 | 86 | Đà Nẵng |

---

### Rule #6 — `MN:G3#2:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Tư (T4) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 2 miền MN** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **328**
- Số ngày trúng (ANY station of MT): **231**
- Hit rate: **70.43%**
- Baseline (random): **70.15%**
- **LIFT: +0.28pp**
- p-value: 0.4804

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đà Nẵng | 327 | 149 | 45.57% | [40.2-51.0]% |
| Khánh Hòa | 328 | 143 | 43.60% | [38.3-49.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-27 | 2026-05-25 | 58, 73, 74 | Khánh Hòa |
| 2026-05-20 | 2026-05-18 | 30, 77, 81 | Đà Nẵng |
| 2026-05-13 | 2026-05-11 | 23, 44, 97 | Đà Nẵng |

---

### Rule #7 — `MB:G7#2:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Tư (T4) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 2 miền MB** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **110**
- Hit rate: **33.74%**
- Baseline (random): **33.75%**
- **LIFT: +-0.01pp**
- p-value: 0.5250

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đà Nẵng | 325 | 66 | 20.31% | [16.3-25.0]% |
| Khánh Hòa | 326 | 61 | 18.71% | [14.8-23.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-13 | 2026-05-13 | 90 | Đà Nẵng |
| 2026-05-06 | 2026-05-06 | 50 | Khánh Hòa |
| 2026-04-29 | 2026-04-29 | 46 | Đà Nẵng, Khánh Hòa |

---

### Rule #8 — `MB:G4#3:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Tư (T4) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 3 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **324**
- Số ngày trúng (ANY station of MT): **109**
- Hit rate: **33.64%**
- Baseline (random): **33.75%**
- **LIFT: +-0.11pp**
- p-value: 0.5403

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đà Nẵng | 323 | 59 | 18.27% | [14.4-22.8]% |
| Khánh Hòa | 324 | 58 | 17.90% | [14.1-22.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-04-15 | 2026-04-12 | 05 | Đà Nẵng |
| 2026-03-04 | 2026-03-01 | 82 | Khánh Hòa |
| 2026-01-21 | 2026-01-18 | 60 | Khánh Hòa |

---


## MT × Thứ Năm (T5)

**Đài hoạt động ngày này**:
- Bình Định
- Quảng Trị
- Quảng Bình

**Coverage trong cell này**: 116 rule có data, **109 đạt p<0.05**, **85 BH-pass** ⭐.

### Rule #1 ⭐ — `MT:G2#1:D-2`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MT** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **330**
- Số ngày trúng (ANY station of MT): **233**
- Hit rate: **70.61%**
- Baseline (random): **55.78%**
- **LIFT: +14.82pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Trị | 330 | 117 | 35.45% | [30.5-40.8]% |
| Bình Định | 330 | 112 | 33.94% | [29.0-39.2]% |
| Quảng Bình | 330 | 110 | 33.33% | [28.5-38.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-14 | 2026-05-12 | 00, 20 | Quảng Trị |
| 2026-05-07 | 2026-05-05 | 62, 95 | Quảng Trị |
| 2026-04-30 | 2026-04-28 | 30, 94 | Bình Định |

---

### Rule #2 ⭐ — `MB:G4#2:D-1`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 2 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **328**
- Số ngày trúng (ANY station of MT): **158**
- Hit rate: **48.17%**
- Baseline (random): **33.75%**
- **LIFT: +14.42pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Trị | 328 | 71 | 21.65% | [17.5-26.4]% |
| Bình Định | 328 | 66 | 20.12% | [16.1-24.8]% |
| Quảng Bình | 328 | 55 | 16.77% | [13.1-21.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-14 | 2026-05-13 | 89 | Quảng Trị |
| 2026-04-23 | 2026-04-22 | 39 | Quảng Bình |
| 2026-04-09 | 2026-04-08 | 38 | Quảng Trị |

---

### Rule #3 ⭐ — `MB:G7#3:D`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 3 miền MB** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MT): **157**
- Hit rate: **48.01%**
- Baseline (random): **33.75%**
- **LIFT: +14.26pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bình Định | 327 | 66 | 20.18% | [16.2-24.9]% |
| Quảng Trị | 327 | 64 | 19.57% | [15.6-24.2]% |
| Quảng Bình | 327 | 62 | 18.96% | [15.1-23.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-07 | 2026-05-07 | 45 | Quảng Bình |
| 2026-04-30 | 2026-04-30 | 98 | Quảng Bình |
| 2026-04-16 | 2026-04-16 | 33 | Quảng Trị |

---

### Rule #4 ⭐ — `MN:G5#1:D`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1 miền MN** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **332**
- Số ngày trúng (ANY station of MT): **280**
- Hit rate: **84.34%**
- Baseline (random): **70.49%**
- **LIFT: +13.85pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Bình | 331 | 164 | 49.55% | [44.2-54.9]% |
| Quảng Trị | 331 | 159 | 48.04% | [42.7-53.4]% |
| Bình Định | 331 | 152 | 45.92% | [40.6-51.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-28 | 2026-05-28 | 19, 45, 55 | Bình Định, Quảng Trị |
| 2026-05-21 | 2026-05-21 | 21, 26, 55 | Quảng Trị |
| 2026-05-14 | 2026-05-14 | 00, 52, 96 | Quảng Trị |

---

### Rule #5 ⭐ — `MT:DB#1:D-1`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MT** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MT): **229**
- Hit rate: **69.60%**
- Baseline (random): **56.00%**
- **LIFT: +13.60pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Trị | 329 | 112 | 34.04% | [29.1-39.3]% |
| Quảng Bình | 329 | 100 | 30.40% | [25.7-35.6]% |
| Bình Định | 329 | 91 | 27.66% | [23.1-32.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-28 | 2026-05-27 | 12, 99 | Bình Định, Quảng Trị |
| 2026-05-14 | 2026-05-13 | 70, 92 | Bình Định, Quảng Trị, Quảng Bình |
| 2026-05-07 | 2026-05-06 | 04, 69 | Quảng Trị |

---

### Rule #6 ⭐ — `MN:G3#2:D-3`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 2 miền MN** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MT): **274**
- Hit rate: **83.28%**
- Baseline (random): **70.12%**
- **LIFT: +13.17pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Bình | 329 | 145 | 44.07% | [38.8-49.5]% |
| Quảng Trị | 329 | 144 | 43.77% | [38.5-49.2]% |
| Bình Định | 329 | 131 | 39.82% | [34.7-45.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-28 | 2026-05-25 | 58, 73, 74 | Quảng Bình |
| 2026-05-14 | 2026-05-11 | 23, 44, 97 | Bình Định, Quảng Bình |
| 2026-05-07 | 2026-05-04 | 10, 26, 43 | Quảng Bình |

---

### Rule #7 ⭐ — `MB:G2#1:D-3`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MT): **152**
- Hit rate: **46.77%**
- Baseline (random): **33.75%**
- **LIFT: +13.02pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Trị | 325 | 65 | 20.00% | [16.0-24.7]% |
| Quảng Bình | 325 | 59 | 18.15% | [14.3-22.7]% |
| Bình Định | 325 | 54 | 16.62% | [13.0-21.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-14 | 2026-05-11 | 10 | Bình Định, Quảng Trị |
| 2026-04-09 | 2026-04-06 | 61 | Bình Định |
| 2026-03-26 | 2026-03-23 | 25 | Bình Định |

---

### Rule #8 ⭐ — `MT:G7#1:D-3`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1 miền MT** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MT): **226**
- Hit rate: **68.69%**
- Baseline (random): **55.84%**
- **LIFT: +12.85pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bình Định | 329 | 111 | 33.74% | [28.8-39.0]% |
| Quảng Trị | 329 | 107 | 32.52% | [27.7-37.8]% |
| Quảng Bình | 329 | 97 | 29.48% | [24.8-34.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-21 | 2026-05-18 | 65, 83 | Quảng Bình |
| 2026-05-14 | 2026-05-11 | 14, 92 | Bình Định, Quảng Bình |
| 2026-05-07 | 2026-05-04 | 13, 51 | Quảng Trị, Quảng Bình |

---

### Rule #9 ⭐ — `MT:G5#1:D-1`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1 miền MT** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MT): **225**
- Hit rate: **68.39%**
- Baseline (random): **55.56%**
- **LIFT: +12.83pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Bình | 329 | 114 | 34.65% | [29.7-39.9]% |
| Bình Định | 329 | 108 | 32.83% | [28.0-38.1]% |
| Quảng Trị | 329 | 88 | 26.75% | [22.2-31.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-21 | 2026-05-20 | 13, 33 | Quảng Bình |
| 2026-05-14 | 2026-05-13 | 19, 74 | Quảng Bình |
| 2026-04-30 | 2026-04-29 | 02, 98 | Quảng Bình |

---

### Rule #10 ⭐ — `MT:G1#1:D-1`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MT** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MT): **225**
- Hit rate: **68.39%**
- Baseline (random): **55.73%**
- **LIFT: +12.66pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Trị | 329 | 110 | 33.43% | [28.6-38.7]% |
| Quảng Bình | 329 | 105 | 31.91% | [27.1-37.1]% |
| Bình Định | 329 | 92 | 27.96% | [23.4-33.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-14 | 2026-05-13 | 45, 96 | Quảng Trị |
| 2026-05-07 | 2026-05-06 | 46, 84 | Quảng Bình |
| 2026-04-30 | 2026-04-29 | 26, 85 | Quảng Bình |

---

### Rule #11 ⭐ — `MT:G5#1:D-2`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1 miền MT** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **330**
- Số ngày trúng (ANY station of MT): **225**
- Hit rate: **68.18%**
- Baseline (random): **55.89%**
- **LIFT: +12.29pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bình Định | 330 | 105 | 31.82% | [27.0-37.0]% |
| Quảng Bình | 330 | 105 | 31.82% | [27.0-37.0]% |
| Quảng Trị | 330 | 100 | 30.30% | [25.6-35.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-21 | 2026-05-19 | 50, 79 | Quảng Trị, Quảng Bình |
| 2026-05-14 | 2026-05-12 | 19, 91 | Bình Định, Quảng Bình |
| 2026-05-07 | 2026-05-05 | 38, 75 | Quảng Trị, Quảng Bình |

---

### Rule #12 ⭐ — `MN:G8#1:D-1`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 8 bộ 1 miền MN** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MT): **270**
- Hit rate: **82.07%**
- Baseline (random): **69.93%**
- **LIFT: +12.14pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bình Định | 329 | 151 | 45.90% | [40.6-51.3]% |
| Quảng Trị | 329 | 141 | 42.86% | [37.6-48.3]% |
| Quảng Bình | 329 | 124 | 37.69% | [32.6-43.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-28 | 2026-05-27 | 64, 94 | Quảng Trị |
| 2026-05-14 | 2026-05-13 | 35, 79, 81 | Quảng Trị, Quảng Bình |
| 2026-05-07 | 2026-05-06 | 15, 78, 94 | Bình Định |

---


## MT × Thứ Sáu (T6)

**Đài hoạt động ngày này**:
- Gia Lai
- Ninh Thuận

**Coverage trong cell này**: 116 rule có data, **0 đạt p<0.05**, **0 BH-pass** ⭐.

### Rule #1 — `MN:G5#1:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1 miền MN** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **332**
- Số ngày trúng (ANY station of MT): **238**
- Hit rate: **71.69%**
- Baseline (random): **69.94%**
- **LIFT: +1.75pp**
- p-value: 0.2625

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Gia Lai | 332 | 157 | 47.29% | [42.0-52.7]% |
| Ninh Thuận | 331 | 152 | 45.92% | [40.6-51.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-29 | 2026-05-29 | 74, 84, 85 | Gia Lai, Ninh Thuận |
| 2026-05-22 | 2026-05-22 | 19, 60, 70 | Ninh Thuận |
| 2026-05-15 | 2026-05-15 | 33, 39, 58 | Gia Lai, Ninh Thuận |

---

### Rule #2 — `MN:G1#1:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MN** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **332**
- Số ngày trúng (ANY station of MT): **234**
- Hit rate: **70.48%**
- Baseline (random): **69.94%**
- **LIFT: +0.55pp**
- p-value: 0.4377

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Gia Lai | 332 | 154 | 46.39% | [41.1-51.8]% |
| Ninh Thuận | 331 | 152 | 45.92% | [40.6-51.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-22 | 2026-05-22 | 11, 48, 93 | Gia Lai |
| 2026-05-15 | 2026-05-15 | 07, 21, 59 | Ninh Thuận |
| 2026-05-08 | 2026-05-08 | 26, 35, 99 | Ninh Thuận |

---

### Rule #3 — `MT:G3#1:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1 miền MT** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **330**
- Số ngày trúng (ANY station of MT): **186**
- Hit rate: **56.36%**
- Baseline (random): **55.84%**
- **LIFT: +0.52pp**
- p-value: 0.4457

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Gia Lai | 330 | 109 | 33.03% | [28.2-38.3]% |
| Ninh Thuận | 329 | 104 | 31.61% | [26.8-36.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-22 | 2026-05-19 | 41, 76 | Ninh Thuận |
| 2026-05-15 | 2026-05-12 | 23, 79 | Ninh Thuận |
| 2026-05-08 | 2026-05-05 | 10, 89 | Gia Lai, Ninh Thuận |

---

### Rule #4 — `MB:G6#2:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 2 miền MB** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **328**
- Số ngày trúng (ANY station of MT): **111**
- Hit rate: **33.84%**
- Baseline (random): **33.75%**
- **LIFT: +0.09pp**
- p-value: 0.5098

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Gia Lai | 328 | 65 | 19.82% | [15.9-24.5]% |
| Ninh Thuận | 327 | 56 | 17.13% | [13.4-21.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-29 | 2026-05-29 | 78 | Gia Lai |
| 2026-05-15 | 2026-05-15 | 14 | Ninh Thuận |
| 2026-04-24 | 2026-04-24 | 34 | Gia Lai |

---

### Rule #5 — `MB:G7#3:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 3 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **110**
- Hit rate: **33.74%**
- Baseline (random): **33.75%**
- **LIFT: +-0.01pp**
- p-value: 0.5250

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Gia Lai | 326 | 61 | 18.71% | [14.8-23.3]% |
| Ninh Thuận | 325 | 56 | 17.23% | [13.5-21.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-01 | 2026-04-28 | 91 | Gia Lai, Ninh Thuận |
| 2026-04-10 | 2026-04-07 | 10 | Ninh Thuận |
| 2026-01-16 | 2026-01-13 | 25 | Gia Lai |

---

### Rule #6 — `MT:G1#1:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MT** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MT): **183**
- Hit rate: **55.62%**
- Baseline (random): **55.73%**
- **LIFT: +-0.10pp**
- p-value: 0.5373

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Gia Lai | 329 | 110 | 33.43% | [28.6-38.7]% |
| Ninh Thuận | 329 | 107 | 32.52% | [27.7-37.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-29 | 2026-05-27 | 34, 57 | Gia Lai |
| 2026-05-22 | 2026-05-20 | 10, 62 | Ninh Thuận |
| 2026-05-15 | 2026-05-13 | 45, 96 | Gia Lai |

---

### Rule #7 — `MB:G7#2:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 2 miền MB** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **328**
- Số ngày trúng (ANY station of MT): **110**
- Hit rate: **33.54%**
- Baseline (random): **33.75%**
- **LIFT: +-0.22pp**
- p-value: 0.5562

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Ninh Thuận | 327 | 63 | 19.27% | [15.4-23.9]% |
| Gia Lai | 328 | 56 | 17.07% | [13.4-21.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-08 | 2026-05-08 | 25 | Ninh Thuận |
| 2026-04-17 | 2026-04-17 | 27 | Gia Lai |
| 2026-04-10 | 2026-04-10 | 37 | Ninh Thuận |

---

### Rule #8 — `MT:G3#1:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1 miền MT** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **331**
- Số ngày trúng (ANY station of MT): **232**
- Hit rate: **70.09%**
- Baseline (random): **70.56%**
- **LIFT: +-0.47pp**
- p-value: 0.5982

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Gia Lai | 331 | 148 | 44.71% | [39.5-50.1]% |
| Ninh Thuận | 330 | 137 | 41.52% | [36.3-46.9]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-22 | 2026-05-21 | 11, 60, 73 | Gia Lai, Ninh Thuận |
| 2026-05-01 | 2026-04-30 | 17, 79, 93 | Gia Lai, Ninh Thuận |
| 2026-04-24 | 2026-04-23 | 00, 37, 83 | Gia Lai |

---


## MT × Thứ Bảy (T7)

**Đài hoạt động ngày này**:
- Đà Nẵng
- Quảng Ngãi
- Đắk Nông

**Coverage trong cell này**: 116 rule có data, **107 đạt p<0.05**, **90 BH-pass** ⭐.

### Rule #1 ⭐ — `MT:G2#1:D-2`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MT** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MT): **284**
- Hit rate: **86.32%**
- Baseline (random): **70.82%**
- **LIFT: +15.50pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đắk Nông | 329 | 160 | 48.63% | [43.3-54.0]% |
| Quảng Ngãi | 328 | 145 | 44.21% | [38.9-49.6]% |
| Đà Nẵng | 328 | 130 | 39.63% | [34.5-45.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-28 | 06, 24, 52 | Đà Nẵng, Đắk Nông |
| 2026-05-23 | 2026-05-21 | 42, 44, 73 | Đắk Nông |
| 2026-05-16 | 2026-05-14 | 10, 25, 76 | Quảng Ngãi |

---

### Rule #2 ⭐ — `MB:G4#2:D-3`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 2 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **155**
- Hit rate: **47.55%**
- Baseline (random): **33.75%**
- **LIFT: +13.79pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ngãi | 325 | 75 | 23.08% | [18.8-28.0]% |
| Đà Nẵng | 325 | 63 | 19.38% | [15.4-24.0]% |
| Đắk Nông | 326 | 58 | 17.79% | [14.0-22.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-16 | 2026-05-13 | 89 | Đắk Nông |
| 2026-05-09 | 2026-05-06 | 09 | Đà Nẵng, Đắk Nông |
| 2026-05-02 | 2026-04-29 | 84 | Quảng Ngãi |

---

### Rule #3 ⭐ — `MT:G5#1:D-2`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1 miền MT** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MT): **276**
- Hit rate: **83.89%**
- Baseline (random): **70.52%**
- **LIFT: +13.37pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ngãi | 328 | 144 | 43.90% | [38.6-49.3]% |
| Đắk Nông | 329 | 144 | 43.77% | [38.5-49.2]% |
| Đà Nẵng | 328 | 143 | 43.60% | [38.3-49.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-28 | 03, 77, 83 | Đà Nẵng, Quảng Ngãi |
| 2026-05-23 | 2026-05-21 | 14, 75, 91 | Đà Nẵng, Quảng Ngãi, Đắk Nông |
| 2026-05-16 | 2026-05-14 | 10, 22, 69 | Đắk Nông |

---

### Rule #4 ⭐ — `MB:G2#2:D-3`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 2 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **153**
- Hit rate: **46.93%**
- Baseline (random): **33.75%**
- **LIFT: +13.18pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đà Nẵng | 325 | 66 | 20.31% | [16.3-25.0]% |
| Quảng Ngãi | 325 | 61 | 18.77% | [14.9-23.4]% |
| Đắk Nông | 326 | 55 | 16.87% | [13.2-21.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-09 | 2026-05-06 | 31 | Quảng Ngãi |
| 2026-05-02 | 2026-04-29 | 28 | Đà Nẵng |
| 2026-04-25 | 2026-04-22 | 03 | Quảng Ngãi |

---

### Rule #5 ⭐ — `MB:G6#3:D-3`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 3 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **153**
- Hit rate: **46.93%**
- Baseline (random): **33.75%**
- **LIFT: +13.18pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đà Nẵng | 325 | 66 | 20.31% | [16.3-25.0]% |
| Đắk Nông | 326 | 59 | 18.10% | [14.3-22.6]% |
| Quảng Ngãi | 325 | 55 | 16.92% | [13.2-21.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-27 | 13 | Đà Nẵng |
| 2026-05-23 | 2026-05-20 | 80 | Đà Nẵng |
| 2026-05-16 | 2026-05-13 | 08 | Đà Nẵng |

---

### Rule #6 ⭐ — `MB:G2#1:D`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MB** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **152**
- Hit rate: **46.63%**
- Baseline (random): **33.75%**
- **LIFT: +12.87pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ngãi | 325 | 65 | 20.00% | [16.0-24.7]% |
| Đắk Nông | 326 | 61 | 18.71% | [14.8-23.3]% |
| Đà Nẵng | 325 | 55 | 16.92% | [13.2-21.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-23 | 2026-05-23 | 31 | Quảng Ngãi |
| 2026-05-16 | 2026-05-16 | 24 | Đà Nẵng |
| 2026-04-04 | 2026-04-04 | 16 | Đắk Nông |

---

### Rule #7 ⭐ — `MB:G4#1:D`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 1 miền MB** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **151**
- Hit rate: **46.32%**
- Baseline (random): **33.75%**
- **LIFT: +12.57pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đắk Nông | 326 | 63 | 19.33% | [15.4-24.0]% |
| Quảng Ngãi | 325 | 61 | 18.77% | [14.9-23.4]% |
| Đà Nẵng | 325 | 52 | 16.00% | [12.4-20.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-30 | 59 | Đà Nẵng |
| 2026-04-25 | 2026-04-25 | 90 | Quảng Ngãi |
| 2026-04-11 | 2026-04-11 | 68 | Đắk Nông |

---

### Rule #8 ⭐ — `MN:G8#1:D-3`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 8 bộ 1 miền MN** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MT): **271**
- Hit rate: **82.37%**
- Baseline (random): **69.93%**
- **LIFT: +12.44pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ngãi | 328 | 159 | 48.48% | [43.1-53.9]% |
| Đắk Nông | 329 | 140 | 42.55% | [37.3-48.0]% |
| Đà Nẵng | 328 | 135 | 41.16% | [36.0-46.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-27 | 64, 94 | Đắk Nông |
| 2026-05-23 | 2026-05-20 | 61, 94, 98 | Đà Nẵng, Đắk Nông |
| 2026-05-16 | 2026-05-13 | 35, 79, 81 | Đà Nẵng, Quảng Ngãi, Đắk Nông |

---

### Rule #9 ⭐ — `MT:DB#1:D-3`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MT** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MT): **225**
- Hit rate: **68.39%**
- Baseline (random): **56.00%**
- **LIFT: +12.39pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đà Nẵng | 328 | 113 | 34.45% | [29.5-39.8]% |
| Đắk Nông | 329 | 96 | 29.18% | [24.5-34.3]% |
| Quảng Ngãi | 328 | 93 | 28.35% | [23.8-33.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-27 | 12, 99 | Quảng Ngãi |
| 2026-05-23 | 2026-05-20 | 16, 31 | Đà Nẵng, Quảng Ngãi |
| 2026-05-16 | 2026-05-13 | 70, 92 | Đà Nẵng, Quảng Ngãi, Đắk Nông |

---

### Rule #10 ⭐ — `MB:G1#1:D-2`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **150**
- Hit rate: **46.01%**
- Baseline (random): **33.75%**
- **LIFT: +12.26pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Quảng Ngãi | 325 | 66 | 20.31% | [16.3-25.0]% |
| Đà Nẵng | 325 | 62 | 19.08% | [15.2-23.7]% |
| Đắk Nông | 326 | 49 | 15.03% | [11.6-19.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-28 | 10 | Quảng Ngãi |
| 2026-05-16 | 2026-05-14 | 24 | Đà Nẵng |
| 2026-05-02 | 2026-04-30 | 57 | Quảng Ngãi |

---

### Rule #11 ⭐ — `MB:G6#1:D`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 1 miền MB** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **150**
- Hit rate: **46.01%**
- Baseline (random): **33.75%**
- **LIFT: +12.26pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đà Nẵng | 325 | 64 | 19.69% | [15.7-24.4]% |
| Đắk Nông | 326 | 64 | 19.63% | [15.7-24.3]% |
| Quảng Ngãi | 325 | 57 | 17.54% | [13.8-22.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-23 | 2026-05-23 | 72 | Quảng Ngãi |
| 2026-04-25 | 2026-04-25 | 30 | Đà Nẵng, Đắk Nông |
| 2026-04-18 | 2026-04-18 | 72 | Đắk Nông |

---

### Rule #12 ⭐ — `MT:G5#1:D-3`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1 miền MT** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MT): **223**
- Hit rate: **67.78%**
- Baseline (random): **55.56%**
- **LIFT: +12.22pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đắk Nông | 329 | 105 | 31.91% | [27.1-37.1]% |
| Đà Nẵng | 328 | 100 | 30.49% | [25.8-35.7]% |
| Quảng Ngãi | 328 | 96 | 29.27% | [24.6-34.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-27 | 45, 59 | Đà Nẵng |
| 2026-05-23 | 2026-05-20 | 13, 33 | Đắk Nông |
| 2026-05-16 | 2026-05-13 | 19, 74 | Quảng Ngãi, Đắk Nông |

---


## MT × Chủ Nhật (CN)

**Đài hoạt động ngày này**:
- Khánh Hòa
- Kon Tum
- Thừa Thiên Huế

**Coverage trong cell này**: 116 rule có data, **0 đạt p<0.05**, **0 BH-pass** ⭐.

### Rule #1 — `MT:G5#1:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1 miền MT** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **330**
- Số ngày trúng (ANY station of MT): **247**
- Hit rate: **74.85%**
- Baseline (random): **70.74%**
- **LIFT: +4.10pp**
- p-value: 0.0573

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Khánh Hòa | 330 | 156 | 47.27% | [42.0-52.7]% |
| Kon Tum | 330 | 135 | 40.91% | [35.7-46.3]% |
| Thừa Thiên Huế | 32 | 9 | 28.12% | [15.6-45.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-17 | 2026-05-16 | 11, 22, 29 | Khánh Hòa, Kon Tum |
| 2026-05-03 | 2026-05-02 | 23, 53, 99 | Khánh Hòa |
| 2026-04-26 | 2026-04-25 | 43, 47, 98 | Khánh Hòa |

---

### Rule #2 — `MB:G7#4:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **123**
- Hit rate: **37.73%**
- Baseline (random): **33.75%**
- **LIFT: +3.98pp**
- p-value: 0.0722

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Khánh Hòa | 326 | 81 | 24.85% | [20.5-29.8]% |
| Thừa Thiên Huế | 31 | 7 | 22.58% | [11.4-39.8]% |
| Kon Tum | 326 | 52 | 15.95% | [12.4-20.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-24 | 2026-05-21 | 74 | Kon Tum |
| 2026-05-10 | 2026-05-07 | 66 | Khánh Hòa |
| 2026-05-03 | 2026-04-30 | 74 | Thừa Thiên Huế |

---

### Rule #3 — `MT:G1#1:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MT** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **330**
- Số ngày trúng (ANY station of MT): **197**
- Hit rate: **59.70%**
- Baseline (random): **55.89%**
- **LIFT: +3.80pp**
- p-value: 0.0908

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Thừa Thiên Huế | 32 | 15 | 46.88% | [30.9-63.5]% |
| Khánh Hòa | 330 | 120 | 36.36% | [31.4-41.7]% |
| Kon Tum | 330 | 102 | 30.91% | [26.2-36.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-31 | 2026-05-29 | 02, 45 | Khánh Hòa, Kon Tum |
| 2026-05-24 | 2026-05-22 | 48, 67 | Thừa Thiên Huế |
| 2026-05-17 | 2026-05-15 | 18, 98 | Khánh Hòa, Thừa Thiên Huế |

---

### Rule #4 — `MB:G7#2:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 2 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **120**
- Hit rate: **36.81%**
- Baseline (random): **33.75%**
- **LIFT: +3.06pp**
- p-value: 0.1338

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Thừa Thiên Huế | 32 | 8 | 25.00% | [13.2-42.1]% |
| Khánh Hòa | 326 | 67 | 20.55% | [16.5-25.3]% |
| Kon Tum | 326 | 61 | 18.71% | [14.8-23.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-24 | 2026-05-22 | 12 | Thừa Thiên Huế |
| 2026-05-17 | 2026-05-15 | 47 | Kon Tum |
| 2026-05-03 | 2026-05-01 | 39 | Kon Tum |

---

### Rule #5 — `MB:G6#3:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 3 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **118**
- Hit rate: **36.20%**
- Baseline (random): **33.75%**
- **LIFT: +2.44pp**
- p-value: 0.1910

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Khánh Hòa | 326 | 65 | 19.94% | [16.0-24.6]% |
| Kon Tum | 326 | 59 | 18.10% | [14.3-22.6]% |
| Thừa Thiên Huế | 32 | 4 | 12.50% | [5.0-28.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-31 | 2026-05-30 | 68 | Khánh Hòa |
| 2026-02-22 | 2026-02-21 | 36 | Kon Tum |
| 2026-02-08 | 2026-02-07 | 49 | Thừa Thiên Huế |

---

### Rule #6 — `MB:G2#2:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 2 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **117**
- Hit rate: **35.89%**
- Baseline (random): **33.75%**
- **LIFT: +2.14pp**
- p-value: 0.2245

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Kon Tum | 326 | 63 | 19.33% | [15.4-24.0]% |
| Thừa Thiên Huế | 32 | 6 | 18.75% | [8.9-35.3]% |
| Khánh Hòa | 326 | 58 | 17.79% | [14.0-22.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-31 | 2026-05-30 | 02 | Khánh Hòa |
| 2026-05-24 | 2026-05-23 | 94 | Thừa Thiên Huế |
| 2026-05-17 | 2026-05-16 | 31 | Thừa Thiên Huế |

---

### Rule #7 — `MN:G2#1:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MN** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **330**
- Số ngày trúng (ANY station of MT): **268**
- Hit rate: **81.21%**
- Baseline (random): **79.88%**
- **LIFT: +1.33pp**
- p-value: 0.2964

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Kon Tum | 330 | 189 | 57.27% | [51.9-62.5]% |
| Khánh Hòa | 330 | 177 | 53.64% | [48.2-58.9]% |
| Thừa Thiên Huế | 32 | 16 | 50.00% | [33.6-66.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-31 | 2026-05-30 | 30, 33, 44, 95 | Thừa Thiên Huế |
| 2026-05-24 | 2026-05-23 | 35, 47, 90, 98 | Khánh Hòa |
| 2026-05-17 | 2026-05-16 | 41, 67, 85, 86 | Thừa Thiên Huế |

---

### Rule #8 — `MB:G6#1:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MT: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 1 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MT ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MT): **114**
- Hit rate: **34.97%**
- Baseline (random): **33.75%**
- **LIFT: +1.22pp**
- p-value: 0.3425

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Thừa Thiên Huế | 32 | 6 | 18.75% | [8.9-35.3]% |
| Khánh Hòa | 326 | 58 | 17.79% | [14.0-22.3]% |
| Kon Tum | 326 | 57 | 17.48% | [13.8-22.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-31 | 2026-05-30 | 24 | Thừa Thiên Huế |
| 2026-05-17 | 2026-05-16 | 48 | Khánh Hòa, Kon Tum |
| 2026-04-26 | 2026-04-25 | 30 | Khánh Hòa, Thừa Thiên Huế |

---


## Tổng kết

**Tài liệu này liệt kê các rule mạnh nhất cho target = MT** qua 7 thứ trong tuần, mỗi thứ với top 8-12 rules ranked theo lift.

### Disclaimer quan trọng

1. **Rule áp dụng ở mức "ANY station"** — nghĩa là source LAST2 cần xuất hiện trong **bất kỳ đài nào** của MT ngày D.
2. **Per-station breakdown** giúp anh biết đài nào carry nhiều signal nhất, nhưng baseline random thì 1 đài có hit thấp hơn ANY-station.
3. **Worked examples** chỉ là 3 ngày gần nhất. KHÔNG đảm bảo rule sẽ tiếp tục trúng — đang trong forward audit 90 ngày.
4. **BH-pass ⭐ = gold standard** sau multiple-testing correction.
5. Tất cả rule này hiện ở **PRE_REGISTER_FORWARD_AUDIT** — chưa live, chưa được hệ thống dùng. Sau 90 ngày audit em sẽ classify lại.

---
**See also**: V10667_RULES_INDEX.md (hub document)