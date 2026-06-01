# V10667 Rules cho TARGET = MN (Đích = Miền MN)

> **Generated**: 2026-06-02T01:27:09+07:00
> **Target region**: MN
> **Audit window**: Forward 90d, anchor 2026-06-02 → earliest closeout 2026-08-31

## Giới thiệu — MN

Miền Nam (3-4 đài/ngày luân phiên theo thứ). Nhiều stations → nhiều tails/ngày (~43 tail/ngày avg) → baseline cao nhưng cũng có nhiều cơ hội hit.

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

## MN × Thứ Hai (T2)

**Đài hoạt động ngày này**:
- TP. HCM
- Đồng Tháp
- Cà Mau

**Coverage trong cell này**: 116 rule có data, **1 đạt p<0.05**, **0 BH-pass** ⭐.

### Rule #1 — `MN:G5#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1 miền MN** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **330**
- Số ngày trúng (ANY station of MN): **307**
- Hit rate: **93.03%**
- Baseline (random): **88.59%**
- **LIFT: +4.44pp**
- p-value: 0.0071

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đồng Tháp | 316 | 181 | 57.28% | [51.8-62.6]% |
| TP. HCM | 316 | 177 | 56.01% | [50.5-61.4]% |
| Cà Mau | 316 | 159 | 50.32% | [44.8-55.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-06-01 | 2026-05-30 | 25, 32, 80, 96 | Đồng Tháp, Cà Mau |
| 2026-05-25 | 2026-05-23 | 16, 26, 36, 61 | Đồng Tháp |
| 2026-05-18 | 2026-05-16 | 10, 46, 96 | Đồng Tháp |

---

### Rule #2 — `MT:G1#1:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Hai (T2) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MT** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **331**
- Số ngày trúng (ANY station of MN): **237**
- Hit rate: **71.60%**
- Baseline (random): **67.26%**
- **LIFT: +4.34pp**
- p-value: 0.0521

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Cà Mau | 316 | 108 | 34.18% | [29.2-39.6]% |
| Đồng Tháp | 316 | 106 | 33.54% | [28.6-38.9]% |
| TP. HCM | 316 | 94 | 29.75% | [25.0-35.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-06-01 | 2026-06-01 | 18, 93 | Đồng Tháp |
| 2026-05-25 | 2026-05-25 | 22, 93 | TP. HCM, Đồng Tháp |
| 2026-05-11 | 2026-05-11 | 32, 44 | TP. HCM, Cà Mau |

---

### Rule #3 — `MT:G3#2:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Hai (T2) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 2 miền MT** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **330**
- Số ngày trúng (ANY station of MN): **241**
- Hit rate: **73.03%**
- Baseline (random): **68.88%**
- **LIFT: +4.15pp**
- p-value: 0.0584

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| TP. HCM | 316 | 118 | 37.34% | [32.2-42.8]% |
| Cà Mau | 316 | 111 | 35.13% | [30.1-40.5]% |
| Đồng Tháp | 316 | 106 | 33.54% | [28.6-38.9]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-25 | 2026-05-24 | 20, 89, 95 | Cà Mau |
| 2026-05-11 | 2026-05-10 | 43, 67, 98 | TP. HCM, Cà Mau |
| 2026-05-04 | 2026-05-03 | 37, 65, 72 | Đồng Tháp |

---

### Rule #4 — `MB:G6#2:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Hai (T2) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 2 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MN): **151**
- Hit rate: **46.18%**
- Baseline (random): **42.83%**
- **LIFT: +3.35pp**
- p-value: 0.1215

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đồng Tháp | 312 | 67 | 21.47% | [17.3-26.4]% |
| TP. HCM | 312 | 60 | 19.23% | [15.2-24.0]% |
| Cà Mau | 312 | 45 | 14.42% | [11.0-18.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-25 | 2026-05-22 | 79 | TP. HCM |
| 2026-05-18 | 2026-05-15 | 14 | TP. HCM, Đồng Tháp, Cà Mau |
| 2026-04-20 | 2026-04-17 | 91 | Cà Mau |

---

### Rule #5 — `MT:G5#1:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Hai (T2) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1 miền MT** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **331**
- Số ngày trúng (ANY station of MN): **233**
- Hit rate: **70.39%**
- Baseline (random): **67.15%**
- **LIFT: +3.24pp**
- p-value: 0.1155

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| TP. HCM | 316 | 110 | 34.81% | [29.8-40.2]% |
| Cà Mau | 316 | 99 | 31.33% | [26.5-36.6]% |
| Đồng Tháp | 316 | 85 | 26.90% | [22.3-32.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-06-01 | 2026-06-01 | 28, 95 | Đồng Tháp |
| 2026-05-25 | 2026-05-25 | 01, 14 | TP. HCM, Cà Mau |
| 2026-05-18 | 2026-05-18 | 17, 24 | TP. HCM, Cà Mau |

---

### Rule #6 — `MB:G7#3:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Hai (T2) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 3 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MN): **150**
- Hit rate: **45.87%**
- Baseline (random): **42.83%**
- **LIFT: +3.04pp**
- p-value: 0.1455

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Cà Mau | 312 | 61 | 19.55% | [15.5-24.3]% |
| TP. HCM | 312 | 59 | 18.91% | [14.9-23.6]% |
| Đồng Tháp | 312 | 45 | 14.42% | [11.0-18.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-06-01 | 2026-05-30 | 96 | Cà Mau |
| 2026-05-25 | 2026-05-23 | 85 | TP. HCM |
| 2026-05-18 | 2026-05-16 | 81 | Đồng Tháp, Cà Mau |

---

### Rule #7 — `MB:G7#4:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Hai (T2) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MN): **150**
- Hit rate: **45.87%**
- Baseline (random): **42.83%**
- **LIFT: +3.04pp**
- p-value: 0.1455

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Cà Mau | 312 | 65 | 20.83% | [16.7-25.7]% |
| Đồng Tháp | 312 | 57 | 18.27% | [14.4-22.9]% |
| TP. HCM | 312 | 46 | 14.74% | [11.2-19.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-06-01 | 2026-05-30 | 44 | TP. HCM, Đồng Tháp, Cà Mau |
| 2026-05-04 | 2026-05-02 | 87 | Cà Mau |
| 2026-04-20 | 2026-04-18 | 53 | Cà Mau |

---

### Rule #8 — `MN:G3#2:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Hai (T2) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 2 miền MN** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **330**
- Số ngày trúng (ANY station of MN): **275**
- Hit rate: **83.33%**
- Baseline (random): **80.54%**
- **LIFT: +2.79pp**
- p-value: 0.1126

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đồng Tháp | 316 | 137 | 43.35% | [38.0-48.9]% |
| TP. HCM | 316 | 136 | 43.04% | [37.7-48.5]% |
| Cà Mau | 316 | 132 | 41.77% | [36.5-47.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-06-01 | 2026-05-31 | 14, 17, 84 | Cà Mau |
| 2026-05-18 | 2026-05-17 | 49, 51 | Đồng Tháp |
| 2026-05-11 | 2026-05-10 | 24, 33, 47 | TP. HCM |

---


## MN × Thứ Ba (T3)

**Đài hoạt động ngày này**:
- Bến Tre
- Vũng Tàu
- Bạc Liêu

**Coverage trong cell này**: 116 rule có data, **2 đạt p<0.05**, **1 BH-pass** ⭐.

### Rule #1 ⭐ — `MT:DB#1:D`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Ba (T3) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MT** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **331**
- Số ngày trúng (ANY station of MN): **246**
- Hit rate: **74.32%**
- Baseline (random): **67.04%**
- **LIFT: +7.28pp**
- p-value: 0.0029
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bạc Liêu | 315 | 113 | 35.87% | [30.8-41.3]% |
| Vũng Tàu | 315 | 100 | 31.75% | [26.9-37.1]% |
| Bến Tre | 315 | 94 | 29.84% | [25.1-35.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-26 | 2026-05-26 | 27, 90 | Bạc Liêu |
| 2026-05-19 | 2026-05-19 | 60, 89 | Bạc Liêu |
| 2026-05-12 | 2026-05-12 | 25, 32 | Bến Tre, Vũng Tàu |

---

### Rule #2 — `MB:G4#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 1 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **157**
- Hit rate: **48.16%**
- Baseline (random): **42.83%**
- **LIFT: +5.33pp**
- p-value: 0.0295

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bến Tre | 310 | 67 | 21.61% | [17.4-26.5]% |
| Bạc Liêu | 310 | 57 | 18.39% | [14.5-23.1]% |
| Vũng Tàu | 310 | 51 | 16.45% | [12.7-21.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-26 | 2026-05-25 | 14 | Bạc Liêu |
| 2026-05-19 | 2026-05-18 | 50 | Bạc Liêu |
| 2026-04-14 | 2026-04-13 | 14 | Bạc Liêu |

---

### Rule #3 — `MB:G4#4:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Ba (T3) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 4 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MN): **152**
- Hit rate: **46.48%**
- Baseline (random): **42.83%**
- **LIFT: +3.65pp**
- p-value: 0.1004

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Vũng Tàu | 311 | 62 | 19.94% | [15.9-24.7]% |
| Bạc Liêu | 311 | 62 | 19.94% | [15.9-24.7]% |
| Bến Tre | 311 | 51 | 16.40% | [12.7-20.9]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-26 | 2026-05-23 | 45 | Bến Tre |
| 2026-05-19 | 2026-05-16 | 87 | Bến Tre |
| 2026-05-12 | 2026-05-09 | 50 | Bạc Liêu |

---

### Rule #4 — `MB:G6#1:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Ba (T3) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 1 miền MB** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MN): **149**
- Hit rate: **45.57%**
- Baseline (random): **42.83%**
- **LIFT: +2.74pp**
- p-value: 0.1726

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Vũng Tàu | 311 | 58 | 18.65% | [14.7-23.4]% |
| Bạc Liêu | 311 | 57 | 18.33% | [14.4-23.0]% |
| Bến Tre | 311 | 52 | 16.72% | [13.0-21.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-26 | 2026-05-26 | 54 | Bến Tre, Vũng Tàu |
| 2026-05-19 | 2026-05-19 | 92 | Bạc Liêu |
| 2026-05-05 | 2026-05-05 | 68 | Bạc Liêu |

---

### Rule #5 — `MB:G2#2:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Ba (T3) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 2 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MN): **148**
- Hit rate: **45.26%**
- Baseline (random): **42.83%**
- **LIFT: +2.43pp**
- p-value: 0.2026

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Vũng Tàu | 311 | 62 | 19.94% | [15.9-24.7]% |
| Bến Tre | 311 | 48 | 15.43% | [11.8-19.9]% |
| Bạc Liêu | 311 | 48 | 15.43% | [11.8-19.9]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-19 | 2026-05-16 | 31 | Bến Tre |
| 2026-05-05 | 2026-05-02 | 54 | Bạc Liêu |
| 2026-04-28 | 2026-04-25 | 12 | Bạc Liêu |

---

### Rule #6 — `MT:G3#1:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Ba (T3) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1 miền MT** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **330**
- Số ngày trúng (ANY station of MN): **229**
- Hit rate: **69.39%**
- Baseline (random): **67.20%**
- **LIFT: +2.19pp**
- p-value: 0.2152

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bạc Liêu | 315 | 112 | 35.56% | [30.5-41.0]% |
| Vũng Tàu | 315 | 104 | 33.02% | [28.1-38.4]% |
| Bến Tre | 315 | 98 | 31.11% | [26.2-36.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-26 | 2026-05-25 | 84, 99 | Vũng Tàu |
| 2026-05-19 | 2026-05-18 | 10, 88 | Bến Tre |
| 2026-05-12 | 2026-05-11 | 03, 87 | Vũng Tàu |

---

### Rule #7 — `MT:G1#1:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Ba (T3) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MT** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **331**
- Số ngày trúng (ANY station of MN): **229**
- Hit rate: **69.18%**
- Baseline (random): **67.09%**
- **LIFT: +2.09pp**
- p-value: 0.2263

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Vũng Tàu | 315 | 112 | 35.56% | [30.5-41.0]% |
| Bạc Liêu | 315 | 96 | 30.48% | [25.6-35.8]% |
| Bến Tre | 315 | 92 | 29.21% | [24.5-34.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-26 | 2026-05-26 | 47, 59 | Bến Tre, Bạc Liêu |
| 2026-05-12 | 2026-05-12 | 21, 85 | Vũng Tàu |
| 2026-05-05 | 2026-05-05 | 32, 93 | Bến Tre, Vũng Tàu, Bạc Liêu |

---

### Rule #8 — `MT:G2#1:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Ba (T3) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MT** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **331**
- Số ngày trúng (ANY station of MN): **228**
- Hit rate: **68.88%**
- Baseline (random): **66.98%**
- **LIFT: +1.90pp**
- p-value: 0.2493

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Vũng Tàu | 315 | 111 | 35.24% | [30.2-40.7]% |
| Bến Tre | 315 | 105 | 33.33% | [28.4-38.7]% |
| Bạc Liêu | 315 | 80 | 25.40% | [20.9-30.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-26 | 2026-05-26 | 07, 69 | Bến Tre |
| 2026-05-19 | 2026-05-19 | 45, 69 | Bến Tre, Vũng Tàu |
| 2026-05-12 | 2026-05-12 | 00, 20 | Bến Tre, Bạc Liêu |

---


## MN × Thứ Tư (T4)

**Đài hoạt động ngày này**:
- Đồng Nai
- Cần Thơ
- Sóc Trăng

**Coverage trong cell này**: 116 rule có data, **2 đạt p<0.05**, **0 BH-pass** ⭐.

### Rule #1 — `MB:G6#2:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 2 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **324**
- Số ngày trúng (ANY station of MN): **154**
- Hit rate: **47.53%**
- Baseline (random): **42.83%**
- **LIFT: +4.70pp**
- p-value: 0.0491

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Cần Thơ | 311 | 67 | 21.54% | [17.3-26.4]% |
| Sóc Trăng | 311 | 61 | 19.61% | [15.6-24.4]% |
| Đồng Nai | 311 | 55 | 17.68% | [13.8-22.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-20 | 2026-05-19 | 74 | Sóc Trăng |
| 2026-05-13 | 2026-05-12 | 47 | Đồng Nai |
| 2026-04-29 | 2026-04-28 | 06 | Cần Thơ |

---

### Rule #2 — `MT:G3#2:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 2 miền MT** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MN): **240**
- Hit rate: **73.39%**
- Baseline (random): **68.84%**
- **LIFT: +4.55pp**
- p-value: 0.0430

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Cần Thơ | 315 | 114 | 36.19% | [31.1-41.6]% |
| Sóc Trăng | 315 | 114 | 36.19% | [31.1-41.6]% |
| Đồng Nai | 315 | 105 | 33.33% | [28.4-38.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-27 | 2026-05-24 | 20, 89, 95 | Cần Thơ |
| 2026-05-20 | 2026-05-17 | 18, 22, 62 | Cần Thơ |
| 2026-05-13 | 2026-05-10 | 43, 67, 98 | Sóc Trăng |

---

### Rule #3 — `MB:G6#3:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Tư (T4) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 3 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MN): **151**
- Hit rate: **46.75%**
- Baseline (random): **42.83%**
- **LIFT: +3.92pp**
- p-value: 0.0857

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Sóc Trăng | 310 | 63 | 20.32% | [16.2-25.1]% |
| Cần Thơ | 310 | 58 | 18.71% | [14.8-23.4]% |
| Đồng Nai | 310 | 51 | 16.45% | [12.7-21.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-27 | 2026-05-25 | 63 | Cần Thơ |
| 2026-05-20 | 2026-05-18 | 20 | Sóc Trăng |
| 2026-04-22 | 2026-04-20 | 61 | Sóc Trăng |

---

### Rule #4 — `MT:G7#1:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Tư (T4) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1 miền MT** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MN): **233**
- Hit rate: **70.82%**
- Baseline (random): **67.04%**
- **LIFT: +3.78pp**
- p-value: 0.0805

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Sóc Trăng | 316 | 100 | 31.65% | [26.8-37.0]% |
| Cần Thơ | 316 | 96 | 30.38% | [25.6-35.7]% |
| Đồng Nai | 316 | 95 | 30.06% | [25.3-35.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-20 | 2026-05-20 | 15, 87 | Đồng Nai, Sóc Trăng |
| 2026-05-06 | 2026-05-06 | 38, 78 | Sóc Trăng |
| 2026-04-29 | 2026-04-29 | 35, 39 | Đồng Nai |

---

### Rule #5 — `MB:G6#1:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Tư (T4) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 1 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **324**
- Số ngày trúng (ANY station of MN): **151**
- Hit rate: **46.60%**
- Baseline (random): **42.83%**
- **LIFT: +3.78pp**
- p-value: 0.0939

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Sóc Trăng | 311 | 79 | 25.40% | [20.9-30.5]% |
| Cần Thơ | 311 | 50 | 16.08% | [12.4-20.6]% |
| Đồng Nai | 311 | 49 | 15.76% | [12.1-20.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-27 | 2026-05-24 | 53 | Sóc Trăng |
| 2026-05-13 | 2026-05-10 | 53 | Sóc Trăng |
| 2026-05-06 | 2026-05-03 | 06 | Cần Thơ, Sóc Trăng |

---

### Rule #6 — `MB:DB#1:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Tư (T4) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **324**
- Số ngày trúng (ANY station of MN): **150**
- Hit rate: **46.30%**
- Baseline (random): **42.83%**
- **LIFT: +3.47pp**
- p-value: 0.1141

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Sóc Trăng | 311 | 65 | 20.90% | [16.8-25.8]% |
| Cần Thơ | 311 | 61 | 19.61% | [15.6-24.4]% |
| Đồng Nai | 311 | 45 | 14.47% | [11.0-18.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-27 | 2026-05-24 | 04 | Đồng Nai |
| 2026-05-20 | 2026-05-17 | 84 | Đồng Nai |
| 2026-05-06 | 2026-05-03 | 64 | Sóc Trăng |

---

### Rule #7 — `MT:G3#2:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Tư (T4) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 2 miền MT** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MN): **232**
- Hit rate: **70.52%**
- Baseline (random): **67.09%**
- **LIFT: +3.42pp**
- p-value: 0.1032

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đồng Nai | 316 | 107 | 33.86% | [28.9-39.2]% |
| Sóc Trăng | 316 | 105 | 33.23% | [28.3-38.6]% |
| Cần Thơ | 316 | 90 | 28.48% | [23.8-33.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-20 | 2026-05-20 | 89, 94 | Cần Thơ, Sóc Trăng |
| 2026-05-13 | 2026-05-13 | 60, 85 | Đồng Nai |
| 2026-05-06 | 2026-05-06 | 34, 59 | Sóc Trăng |

---

### Rule #8 — `MB:G7#2:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Tư (T4) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 2 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MN): **149**
- Hit rate: **46.13%**
- Baseline (random): **42.83%**
- **LIFT: +3.30pp**
- p-value: 0.1266

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Sóc Trăng | 310 | 61 | 19.68% | [15.6-24.5]% |
| Đồng Nai | 310 | 55 | 17.74% | [13.9-22.4]% |
| Cần Thơ | 310 | 51 | 16.45% | [12.7-21.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-04-29 | 2026-04-27 | 46 | Sóc Trăng |
| 2026-04-08 | 2026-04-06 | 33 | Đồng Nai |
| 2026-04-01 | 2026-03-30 | 34 | Đồng Nai |

---


## MN × Thứ Năm (T5)

**Đài hoạt động ngày này**:
- Tây Ninh
- An Giang
- Bình Thuận

**Coverage trong cell này**: 116 rule có data, **3 đạt p<0.05**, **1 BH-pass** ⭐.

### Rule #1 ⭐ — `MT:DB#1:D-1`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MT** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MN): **248**
- Hit rate: **75.38%**
- Baseline (random): **67.20%**
- **LIFT: +8.18pp**
- p-value: 0.0010
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| An Giang | 316 | 120 | 37.97% | [32.8-43.4]% |
| Tây Ninh | 316 | 114 | 36.08% | [31.0-41.5]% |
| Bình Thuận | 316 | 103 | 32.59% | [27.7-38.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-28 | 2026-05-27 | 12, 99 | Tây Ninh |
| 2026-05-21 | 2026-05-20 | 16, 31 | Tây Ninh, Bình Thuận |
| 2026-04-30 | 2026-04-29 | 64, 99 | Tây Ninh |

---

### Rule #2 — `MB:G6#3:D`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 3 miền MB** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MN): **159**
- Hit rate: **48.62%**
- Baseline (random): **42.83%**
- **LIFT: +5.79pp**
- p-value: 0.0196

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bình Thuận | 312 | 67 | 21.47% | [17.3-26.4]% |
| An Giang | 312 | 62 | 19.87% | [15.8-24.6]% |
| Tây Ninh | 312 | 58 | 18.59% | [14.7-23.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-14 | 2026-05-14 | 75 | An Giang |
| 2026-04-02 | 2026-04-02 | 34 | Bình Thuận |
| 2026-03-26 | 2026-03-26 | 36 | Tây Ninh, An Giang, Bình Thuận |

---

### Rule #3 — `MB:G6#1:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Năm (T5) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 1 miền MB** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MN): **155**
- Hit rate: **47.40%**
- Baseline (random): **42.83%**
- **LIFT: +4.57pp**
- p-value: 0.0532

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Tây Ninh | 312 | 64 | 20.51% | [16.4-25.3]% |
| Bình Thuận | 312 | 64 | 20.51% | [16.4-25.3]% |
| An Giang | 312 | 59 | 18.91% | [14.9-23.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-21 | 2026-05-21 | 30 | Tây Ninh |
| 2026-05-07 | 2026-05-07 | 56 | Tây Ninh |
| 2026-04-30 | 2026-04-30 | 06 | Tây Ninh |

---

### Rule #4 — `MT:G5#1:D`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1 miền MT** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **332**
- Số ngày trúng (ANY station of MN): **282**
- Hit rate: **84.94%**
- Baseline (random): **80.93%**
- **LIFT: +4.01pp**
- p-value: 0.0368

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Tây Ninh | 316 | 152 | 48.10% | [42.6-53.6]% |
| An Giang | 316 | 142 | 44.94% | [39.5-50.5]% |
| Bình Thuận | 316 | 136 | 43.04% | [37.7-48.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-28 | 2026-05-28 | 03, 77, 83 | Tây Ninh, An Giang |
| 2026-05-14 | 2026-05-14 | 10, 22, 69 | Tây Ninh, An Giang |
| 2026-05-07 | 2026-05-07 | 56, 75, 89 | Tây Ninh |

---

### Rule #5 — `MB:G4#4:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Năm (T5) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 4 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MN): **152**
- Hit rate: **46.77%**
- Baseline (random): **42.83%**
- **LIFT: +3.94pp**
- p-value: 0.0839

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bình Thuận | 310 | 63 | 20.32% | [16.2-25.1]% |
| Tây Ninh | 310 | 59 | 19.03% | [15.1-23.8]% |
| An Giang | 310 | 54 | 17.42% | [13.6-22.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-21 | 2026-05-18 | 36 | Bình Thuận |
| 2026-05-07 | 2026-05-04 | 17 | An Giang |
| 2026-04-23 | 2026-04-20 | 06 | Tây Ninh |

---

### Rule #6 — `MB:G2#2:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Năm (T5) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 2 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MN): **151**
- Hit rate: **46.46%**
- Baseline (random): **42.83%**
- **LIFT: +3.63pp**
- p-value: 0.1025

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Tây Ninh | 310 | 60 | 19.35% | [15.3-24.1]% |
| An Giang | 310 | 59 | 19.03% | [15.1-23.8]% |
| Bình Thuận | 310 | 55 | 17.74% | [13.9-22.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-21 | 2026-05-18 | 65 | Tây Ninh, An Giang |
| 2026-05-14 | 2026-05-11 | 83 | Bình Thuận |
| 2026-05-07 | 2026-05-04 | 56 | Tây Ninh |

---

### Rule #7 — `MB:G7#3:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Năm (T5) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 3 miền MB** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MN): **151**
- Hit rate: **46.18%**
- Baseline (random): **42.83%**
- **LIFT: +3.35pp**
- p-value: 0.1215

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Tây Ninh | 312 | 66 | 21.15% | [17.0-26.0]% |
| An Giang | 312 | 56 | 17.95% | [14.1-22.6]% |
| Bình Thuận | 312 | 52 | 16.67% | [12.9-21.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-28 | 2026-05-28 | 51 | Tây Ninh, Bình Thuận |
| 2026-05-14 | 2026-05-14 | 62 | An Giang, Bình Thuận |
| 2026-04-30 | 2026-04-30 | 98 | An Giang |

---

### Rule #8 — `MN:DB#1:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Năm (T5) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MN** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MN): **276**
- Hit rate: **83.89%**
- Baseline (random): **80.60%**
- **LIFT: +3.29pp**
- p-value: 0.0751

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Tây Ninh | 316 | 142 | 44.94% | [39.5-50.5]% |
| An Giang | 316 | 141 | 44.62% | [39.2-50.1]% |
| Bình Thuận | 316 | 129 | 40.82% | [35.5-46.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-28 | 2026-05-27 | 09, 38, 40 | Tây Ninh, An Giang, Bình Thuận |
| 2026-05-21 | 2026-05-20 | 58, 74, 97 | Tây Ninh, Bình Thuận |
| 2026-04-30 | 2026-04-29 | 05, 46, 91 | Tây Ninh, Bình Thuận |

---


## MN × Thứ Sáu (T6)

**Đài hoạt động ngày này**:
- Vĩnh Long
- Bình Dương
- Trà Vinh

**Coverage trong cell này**: 116 rule có data, **1 đạt p<0.05**, **0 BH-pass** ⭐.

### Rule #1 — `MT:G1#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MT** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **330**
- Số ngày trúng (ANY station of MN): **236**
- Hit rate: **71.52%**
- Baseline (random): **67.09%**
- **LIFT: +4.42pp**
- p-value: 0.0494

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Trà Vinh | 315 | 108 | 34.29% | [29.3-39.7]% |
| Vĩnh Long | 315 | 102 | 32.38% | [27.4-37.7]% |
| Bình Dương | 315 | 93 | 29.52% | [24.8-34.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-22 | 2026-05-19 | 02, 59 | Trà Vinh |
| 2026-05-15 | 2026-05-12 | 21, 85 | Bình Dương, Trà Vinh |
| 2026-05-08 | 2026-05-05 | 32, 93 | Trà Vinh |

---

### Rule #2 — `MB:G6#2:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 2 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **154**
- Hit rate: **47.24%**
- Baseline (random): **42.83%**
- **LIFT: +4.41pp**
- p-value: 0.0602

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Trà Vinh | 311 | 61 | 19.61% | [15.6-24.4]% |
| Vĩnh Long | 311 | 60 | 19.29% | [15.3-24.0]% |
| Bình Dương | 311 | 49 | 15.76% | [12.1-20.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-29 | 2026-05-26 | 51 | Vĩnh Long |
| 2026-05-08 | 2026-05-05 | 91 | Vĩnh Long |
| 2026-05-01 | 2026-04-28 | 06 | Bình Dương |

---

### Rule #3 — `MT:G5#1:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1 miền MT** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **330**
- Số ngày trúng (ANY station of MN): **233**
- Hit rate: **70.61%**
- Baseline (random): **67.09%**
- **LIFT: +3.51pp**
- p-value: 0.0969

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Vĩnh Long | 315 | 108 | 34.29% | [29.3-39.7]% |
| Bình Dương | 315 | 105 | 33.33% | [28.4-38.7]% |
| Trà Vinh | 315 | 87 | 27.62% | [23.0-32.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-15 | 2026-05-12 | 19, 91 | Bình Dương |
| 2026-05-08 | 2026-05-05 | 38, 75 | Vĩnh Long, Trà Vinh |
| 2026-04-24 | 2026-04-21 | 81, 83 | Vĩnh Long, Trà Vinh |

---

### Rule #4 — `MT:G7#1:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1 miền MT** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MN): **232**
- Hit rate: **70.52%**
- Baseline (random): **67.04%**
- **LIFT: +3.48pp**
- p-value: 0.0995

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Trà Vinh | 316 | 109 | 34.49% | [29.5-39.9]% |
| Vĩnh Long | 316 | 103 | 32.59% | [27.7-38.0]% |
| Bình Dương | 316 | 95 | 30.06% | [25.3-35.3]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-29 | 2026-05-27 | 33, 91 | Vĩnh Long |
| 2026-05-22 | 2026-05-20 | 15, 87 | Trà Vinh |
| 2026-05-15 | 2026-05-13 | 65, 70 | Vĩnh Long |

---

### Rule #5 — `MT:G5#1:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1 miền MT** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **332**
- Số ngày trúng (ANY station of MN): **234**
- Hit rate: **70.48%**
- Baseline (random): **67.15%**
- **LIFT: +3.33pp**
- p-value: 0.1085

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Trà Vinh | 316 | 107 | 33.86% | [28.9-39.2]% |
| Bình Dương | 316 | 98 | 31.01% | [26.2-36.3]% |
| Vĩnh Long | 316 | 91 | 28.80% | [24.1-34.0]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-29 | 2026-05-29 | 40, 80 | Trà Vinh |
| 2026-05-15 | 2026-05-15 | 85, 99 | Vĩnh Long, Bình Dương |
| 2026-05-08 | 2026-05-08 | 10, 98 | Vĩnh Long, Bình Dương, Trà Vinh |

---

### Rule #6 — `MB:DB#1:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **328**
- Số ngày trúng (ANY station of MN): **151**
- Hit rate: **46.04%**
- Baseline (random): **42.83%**
- **LIFT: +3.21pp**
- p-value: 0.1318

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Vĩnh Long | 313 | 70 | 22.36% | [18.1-27.3]% |
| Bình Dương | 313 | 65 | 20.77% | [16.6-25.6]% |
| Trà Vinh | 313 | 49 | 15.65% | [12.1-20.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-22 | 2026-05-20 | 68 | Bình Dương |
| 2026-04-24 | 2026-04-22 | 48 | Vĩnh Long, Bình Dương |
| 2026-04-17 | 2026-04-15 | 14 | Bình Dương |

---

### Rule #7 — `MT:G8#1:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 8 bộ 1 miền MT** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MN): **231**
- Hit rate: **70.21%**
- Baseline (random): **67.15%**
- **LIFT: +3.06pp**
- p-value: 0.1303

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Trà Vinh | 316 | 108 | 34.18% | [29.2-39.6]% |
| Bình Dương | 316 | 105 | 33.23% | [28.3-38.6]% |
| Vĩnh Long | 316 | 92 | 29.11% | [24.4-34.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-29 | 2026-05-27 | 31, 66 | Bình Dương |
| 2026-05-22 | 2026-05-20 | 28, 81 | Trà Vinh |
| 2026-05-15 | 2026-05-13 | 06, 58 | Vĩnh Long |

---

### Rule #8 — `MB:G2#1:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **149**
- Hit rate: **45.71%**
- Baseline (random): **42.83%**
- **LIFT: +2.88pp**
- p-value: 0.1602

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Trà Vinh | 311 | 62 | 19.94% | [15.9-24.7]% |
| Vĩnh Long | 311 | 53 | 17.04% | [13.3-21.6]% |
| Bình Dương | 311 | 51 | 16.40% | [12.7-20.9]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-22 | 2026-05-19 | 23 | Vĩnh Long |
| 2026-05-08 | 2026-05-05 | 91 | Vĩnh Long |
| 2026-04-17 | 2026-04-14 | 33 | Trà Vinh |

---


## MN × Thứ Bảy (T7)

**Đài hoạt động ngày này**:
- TP. HCM
- Long An
- Bình Phước
- Hậu Giang

**Coverage trong cell này**: 116 rule có data, **106 đạt p<0.05**, **86 BH-pass** ⭐.

### Rule #1 ⭐ — `MB:G7#1:D`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1 miền MB** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **194**
- Hit rate: **59.51%**
- Baseline (random): **42.83%**
- **LIFT: +16.68pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bình Phước | 312 | 66 | 21.15% | [17.0-26.0]% |
| Long An | 312 | 60 | 19.23% | [15.2-24.0]% |
| Hậu Giang | 312 | 57 | 18.27% | [14.4-22.9]% |
| TP. HCM | 312 | 56 | 17.95% | [14.1-22.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-30 | 51 | Hậu Giang |
| 2026-05-23 | 2026-05-23 | 84 | Hậu Giang |
| 2026-04-25 | 2026-04-25 | 27 | TP. HCM |

---

### Rule #2 ⭐ — `MB:G1#1:D-3`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **183**
- Hit rate: **56.13%**
- Baseline (random): **42.83%**
- **LIFT: +13.31pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Long An | 313 | 66 | 21.09% | [16.9-25.9]% |
| Bình Phước | 313 | 65 | 20.77% | [16.6-25.6]% |
| Hậu Giang | 313 | 56 | 17.89% | [14.0-22.5]% |
| TP. HCM | 313 | 49 | 15.65% | [12.1-20.1]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-04-25 | 2026-04-22 | 41 | Long An, Bình Phước |
| 2026-04-18 | 2026-04-15 | 68 | Bình Phước |
| 2026-04-04 | 2026-04-01 | 08 | Bình Phước |

---

### Rule #3 ⭐ — `MB:G2#2:D-1`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 2 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **182**
- Hit rate: **55.83%**
- Baseline (random): **42.83%**
- **LIFT: +13.00pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hậu Giang | 312 | 57 | 18.27% | [14.4-22.9]% |
| TP. HCM | 312 | 56 | 17.95% | [14.1-22.6]% |
| Bình Phước | 312 | 55 | 17.63% | [13.8-22.2]% |
| Long An | 312 | 53 | 16.99% | [13.2-21.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-29 | 51 | Hậu Giang |
| 2026-05-23 | 2026-05-22 | 10 | TP. HCM, Bình Phước |
| 2026-05-16 | 2026-05-15 | 54 | Bình Phước |

---

### Rule #4 ⭐ — `MB:G4#1:D`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 1 miền MB** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **182**
- Hit rate: **55.83%**
- Baseline (random): **42.83%**
- **LIFT: +13.00pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Long An | 312 | 67 | 21.47% | [17.3-26.4]% |
| Bình Phước | 312 | 60 | 19.23% | [15.2-24.0]% |
| Hậu Giang | 312 | 56 | 17.95% | [14.1-22.6]% |
| TP. HCM | 312 | 45 | 14.42% | [11.0-18.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-30 | 59 | Long An, Bình Phước |
| 2026-05-23 | 2026-05-23 | 36 | Long An |
| 2026-05-09 | 2026-05-09 | 96 | Long An, Hậu Giang |

---

### Rule #5 ⭐ — `MB:G6#1:D-2`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 1 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **179**
- Hit rate: **54.91%**
- Baseline (random): **42.83%**
- **LIFT: +12.08pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| TP. HCM | 312 | 69 | 22.12% | [17.9-27.0]% |
| Hậu Giang | 312 | 58 | 18.59% | [14.7-23.3]% |
| Bình Phước | 312 | 52 | 16.67% | [12.9-21.2]% |
| Long An | 312 | 45 | 14.42% | [11.0-18.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-28 | 64 | TP. HCM |
| 2026-05-23 | 2026-05-21 | 30 | TP. HCM |
| 2026-05-16 | 2026-05-14 | 72 | TP. HCM, Bình Phước |

---

### Rule #6 ⭐ — `MB:G2#1:D-2`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **178**
- Hit rate: **54.60%**
- Baseline (random): **42.83%**
- **LIFT: +11.77pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Hậu Giang | 312 | 62 | 19.87% | [15.8-24.6]% |
| Bình Phước | 312 | 59 | 18.91% | [14.9-23.6]% |
| TP. HCM | 312 | 51 | 16.35% | [12.7-20.9]% |
| Long An | 312 | 51 | 16.35% | [12.7-20.9]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-28 | 76 | Long An |
| 2026-05-23 | 2026-05-21 | 00 | Hậu Giang |
| 2026-05-09 | 2026-05-07 | 94 | Hậu Giang |

---

### Rule #7 ⭐ — `MB:G4#1:D-2`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 1 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **178**
- Hit rate: **54.60%**
- Baseline (random): **42.83%**
- **LIFT: +11.77pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Long An | 312 | 61 | 19.55% | [15.5-24.3]% |
| TP. HCM | 312 | 57 | 18.27% | [14.4-22.9]% |
| Hậu Giang | 312 | 52 | 16.67% | [12.9-21.2]% |
| Bình Phước | 312 | 48 | 15.38% | [11.8-19.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-16 | 2026-05-14 | 87 | Hậu Giang |
| 2026-05-02 | 2026-04-30 | 96 | Long An |
| 2026-04-25 | 2026-04-23 | 96 | Long An |

---

### Rule #8 ⭐ — `MT:G3#1:D-3`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1 miền MT** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MN): **259**
- Hit rate: **78.72%**
- Baseline (random): **67.09%**
- **LIFT: +11.63pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| TP. HCM | 316 | 99 | 31.33% | [26.5-36.6]% |
| Hậu Giang | 316 | 99 | 31.33% | [26.5-36.6]% |
| Long An | 316 | 97 | 30.70% | [25.9-36.0]% |
| Bình Phước | 316 | 92 | 29.11% | [24.4-34.4]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-27 | 56, 87 | Long An, Hậu Giang |
| 2026-05-23 | 2026-05-20 | 04, 44 | TP. HCM, Long An, Bình Phước, Hậu Giang |
| 2026-05-09 | 2026-05-06 | 41, 79 | Long An |

---

### Rule #9 ⭐ — `MB:G7#3:D-1`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 3 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **177**
- Hit rate: **54.29%**
- Baseline (random): **42.83%**
- **LIFT: +11.47pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| TP. HCM | 312 | 61 | 19.55% | [15.5-24.3]% |
| Bình Phước | 312 | 59 | 18.91% | [14.9-23.6]% |
| Hậu Giang | 312 | 58 | 18.59% | [14.7-23.3]% |
| Long An | 312 | 57 | 18.27% | [14.4-22.9]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-29 | 66 | Bình Phước |
| 2026-05-23 | 2026-05-22 | 78 | Hậu Giang |
| 2026-05-09 | 2026-05-08 | 42 | TP. HCM |

---

### Rule #10 ⭐ — `MB:G4#3:D-2`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 3 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **176**
- Hit rate: **53.99%**
- Baseline (random): **42.83%**
- **LIFT: +11.16pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bình Phước | 312 | 68 | 21.79% | [17.6-26.7]% |
| Hậu Giang | 312 | 59 | 18.91% | [14.9-23.6]% |
| TP. HCM | 312 | 52 | 16.67% | [12.9-21.2]% |
| Long An | 312 | 49 | 15.71% | [12.1-20.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-23 | 2026-05-21 | 61 | TP. HCM |
| 2026-05-09 | 2026-05-07 | 65 | Bình Phước, Hậu Giang |
| 2026-04-25 | 2026-04-23 | 54 | Long An |

---

### Rule #11 ⭐ — `MB:G6#1:D-1`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 1 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **176**
- Hit rate: **53.99%**
- Baseline (random): **42.83%**
- **LIFT: +11.16pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Bình Phước | 312 | 57 | 18.27% | [14.4-22.9]% |
| TP. HCM | 312 | 56 | 17.95% | [14.1-22.6]% |
| Long An | 312 | 47 | 15.06% | [11.5-19.5]% |
| Hậu Giang | 312 | 42 | 13.46% | [10.1-17.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-16 | 2026-05-15 | 88 | Long An |
| 2026-04-04 | 2026-04-03 | 80 | Hậu Giang |
| 2026-03-28 | 2026-03-27 | 38 | TP. HCM |

---

### Rule #12 ⭐ — `MT:G1#1:D-3`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MT** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MN): **256**
- Hit rate: **77.81%**
- Baseline (random): **66.92%**
- **LIFT: +10.89pp**
- p-value: 0.0000
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| TP. HCM | 316 | 107 | 33.86% | [28.9-39.2]% |
| Hậu Giang | 316 | 100 | 31.65% | [26.8-37.0]% |
| Long An | 316 | 96 | 30.38% | [25.6-35.7]% |
| Bình Phước | 316 | 96 | 30.38% | [25.6-35.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-30 | 2026-05-27 | 34, 57 | TP. HCM, Long An |
| 2026-05-23 | 2026-05-20 | 10, 62 | TP. HCM, Bình Phước |
| 2026-05-16 | 2026-05-13 | 45, 96 | Long An |

---


## MN × Chủ Nhật (CN)

**Đài hoạt động ngày này**:
- Tiền Giang
- Kiên Giang
- Đà Lạt

**Coverage trong cell này**: 116 rule có data, **1 đạt p<0.05**, **0 BH-pass** ⭐.

### Rule #1 — `MB:G4#4:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 4 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **155**
- Hit rate: **47.55%**
- Baseline (random): **42.83%**
- **LIFT: +4.72pp**
- p-value: 0.0479

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Kiên Giang | 312 | 60 | 19.23% | [15.2-24.0]% |
| Tiền Giang | 312 | 56 | 17.95% | [14.1-22.6]% |
| Đà Lạt | 312 | 55 | 17.63% | [13.8-22.2]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-31 | 2026-05-28 | 41 | Tiền Giang |
| 2026-05-24 | 2026-05-21 | 68 | Tiền Giang, Đà Lạt |
| 2026-05-17 | 2026-05-14 | 42 | Tiền Giang |

---

### Rule #2 — `MT:G3#1:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1 miền MT** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **330**
- Số ngày trúng (ANY station of MN): **239**
- Hit rate: **72.42%**
- Baseline (random): **68.72%**
- **LIFT: +3.70pp**
- p-value: 0.0822

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Kiên Giang | 316 | 106 | 33.54% | [28.6-38.9]% |
| Đà Lạt | 316 | 100 | 31.65% | [26.8-37.0]% |
| Tiền Giang | 316 | 96 | 30.38% | [25.6-35.7]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-31 | 2026-05-31 | 13, 76, 82 | Kiên Giang |
| 2026-05-24 | 2026-05-24 | 55, 71, 95 | Tiền Giang |
| 2026-05-17 | 2026-05-17 | 15, 95, 97 | Đà Lạt |

---

### Rule #3 — `MB:G6#2:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 2 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **150**
- Hit rate: **46.01%**
- Baseline (random): **42.83%**
- **LIFT: +3.18pp**
- p-value: 0.1345

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Tiền Giang | 312 | 68 | 21.79% | [17.6-26.7]% |
| Đà Lạt | 312 | 58 | 18.59% | [14.7-23.3]% |
| Kiên Giang | 312 | 45 | 14.42% | [11.0-18.8]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-17 | 2026-05-16 | 85 | Kiên Giang |
| 2026-03-29 | 2026-03-28 | 58 | Kiên Giang |
| 2026-03-22 | 2026-03-21 | 51 | Tiền Giang |

---

### Rule #4 — `MB:G7#2:D`

**Strength**: WEAK

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 2 miền MB** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **149**
- Hit rate: **45.71%**
- Baseline (random): **42.83%**
- **LIFT: +2.88pp**
- p-value: 0.1602

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đà Lạt | 312 | 61 | 19.55% | [15.5-24.3]% |
| Tiền Giang | 312 | 55 | 17.63% | [13.8-22.2]% |
| Kiên Giang | 312 | 51 | 16.35% | [12.7-20.9]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-17 | 2026-05-17 | 51 | Tiền Giang, Đà Lạt |
| 2026-05-03 | 2026-05-03 | 88 | Đà Lạt |
| 2026-04-26 | 2026-04-26 | 86 | Tiền Giang |

---

### Rule #5 — `MB:G4#3:D-2`

**Strength**: WEAK

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 3 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **148**
- Hit rate: **45.40%**
- Baseline (random): **42.83%**
- **LIFT: +2.57pp**
- p-value: 0.1890

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Tiền Giang | 312 | 63 | 20.19% | [16.1-25.0]% |
| Kiên Giang | 312 | 51 | 16.35% | [12.7-20.9]% |
| Đà Lạt | 312 | 51 | 16.35% | [12.7-20.9]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-24 | 2026-05-22 | 01 | Tiền Giang, Kiên Giang |
| 2026-05-17 | 2026-05-15 | 51 | Tiền Giang, Đà Lạt |
| 2026-05-10 | 2026-05-08 | 74 | Đà Lạt |

---

### Rule #6 — `MB:G6#1:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 1 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MN): **148**
- Hit rate: **45.40%**
- Baseline (random): **42.83%**
- **LIFT: +2.57pp**
- p-value: 0.1890

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Kiên Giang | 312 | 62 | 19.87% | [15.8-24.6]% |
| Tiền Giang | 312 | 58 | 18.59% | [14.7-23.3]% |
| Đà Lạt | 312 | 54 | 17.31% | [13.5-21.9]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-24 | 2026-05-23 | 72 | Đà Lạt |
| 2026-04-26 | 2026-04-25 | 30 | Đà Lạt |
| 2026-04-05 | 2026-04-04 | 66 | Kiên Giang |

---

### Rule #7 — `MT:G5#1:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1 miền MT** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **330**
- Số ngày trúng (ANY station of MN): **276**
- Hit rate: **83.64%**
- Baseline (random): **81.15%**
- **LIFT: +2.48pp**
- p-value: 0.1396

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Đà Lạt | 316 | 145 | 45.89% | [40.5-51.4]% |
| Kiên Giang | 316 | 143 | 45.25% | [39.9-50.8]% |
| Tiền Giang | 316 | 136 | 43.04% | [37.7-48.5]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-31 | 2026-05-30 | 25, 30, 43 | Tiền Giang |
| 2026-05-17 | 2026-05-16 | 11, 22, 29 | Tiền Giang, Kiên Giang, Đà Lạt |
| 2026-05-10 | 2026-05-09 | 31, 40, 84 | Tiền Giang, Kiên Giang, Đà Lạt |

---

### Rule #8 — `MT:G8#1:D-3`

**Strength**: WEAK

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MN: lấy LAST2 (2 chữ số cuối) của **Giải 8 bộ 1 miền MT** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MN ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **329**
- Số ngày trúng (ANY station of MN): **274**
- Hit rate: **83.28%**
- Baseline (random): **81.03%**
- **LIFT: +2.26pp**
- p-value: 0.1651

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| Tiền Giang | 316 | 146 | 46.20% | [40.8-51.7]% |
| Kiên Giang | 316 | 137 | 43.35% | [38.0-48.9]% |
| Đà Lạt | 316 | 133 | 42.09% | [36.8-47.6]% |

**3 ngày gần nhất rule trúng** (worked examples):

| Ngày D | Source date D-lag | Source LAST2 set | Trúng ở đài |
|---|---|---|---|
| 2026-05-31 | 2026-05-28 | 05, 37, 65 | Kiên Giang |
| 2026-05-24 | 2026-05-21 | 15, 55, 93 | Tiền Giang, Kiên Giang |
| 2026-05-17 | 2026-05-14 | 63, 66, 72 | Tiền Giang |

---


## Tổng kết

**Tài liệu này liệt kê các rule mạnh nhất cho target = MN** qua 7 thứ trong tuần, mỗi thứ với top 8-12 rules ranked theo lift.

### Disclaimer quan trọng

1. **Rule áp dụng ở mức "ANY station"** — nghĩa là source LAST2 cần xuất hiện trong **bất kỳ đài nào** của MN ngày D.
2. **Per-station breakdown** giúp anh biết đài nào carry nhiều signal nhất, nhưng baseline random thì 1 đài có hit thấp hơn ANY-station.
3. **Worked examples** chỉ là 3 ngày gần nhất. KHÔNG đảm bảo rule sẽ tiếp tục trúng — đang trong forward audit 90 ngày.
4. **BH-pass ⭐ = gold standard** sau multiple-testing correction.
5. Tất cả rule này hiện ở **PRE_REGISTER_FORWARD_AUDIT** — chưa live, chưa được hệ thống dùng. Sau 90 ngày audit em sẽ classify lại.

---
**See also**: V10667_RULES_INDEX.md (hub document)