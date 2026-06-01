# V10667 Rules cho TARGET = MB (Đích = Miền MB)

> **Generated**: 2026-06-02T01:27:09+07:00
> **Target region**: MB
> **Audit window**: Forward 90d, anchor 2026-06-02 → earliest closeout 2026-08-31

## ⚠️ Đọc trước: Quy ước Đánh Số Bộ Số

Rule sử dụng ký hiệu `Giải X bộ Y` (hoặc `GX#Y`). Owner đánh dấu G.4 MB rõ ràng:

**MB sources có nhiều bộ**: G2 (2 bộ), **G4 (4 bộ — owner mới bổ sung ⭐)**, G6 (3 bộ), G7 (4 bộ).

**G.4 MB (4 bộ) — quy ước vị trí**:
```
Giải 4 bộ 1 [top-left]    Giải 4 bộ 2 [top-right]
Giải 4 bộ 3 [bottom-left] Giải 4 bộ 4 [bottom-right]
```

Ví dụ MB 31/05/2026: G.4 bộ 1=7717, bộ 2=7829, bộ 3=5183, bộ 4=4559.

**Xem đầy đủ legend**: [📖 V10667_BO_NUMBERING_LEGEND.md](./V10667_BO_NUMBERING_LEGEND.md)

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
- MB_BOARD

**Coverage trong cell này**: 296 rule có data, **17 đạt p<0.05**, **1 BH-pass** ⭐.

### Rule #1 ⭐ — `MN:DB#1:D`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MN** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **206**
- Hit rate: **63.19%**
- Baseline (random): **54.76%**
- **LIFT: +8.43pp**
- p-value: 0.0013
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #2 — `MB:G4#4:D-3`

**Strength**: STRONG

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 4 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **97**
- Hit rate: **29.85%**
- Baseline (random): **23.79%**
- **LIFT: +6.06pp**
- p-value: 0.0062

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #3 — `MT:G3#1:D`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1 miền MT** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **156**
- Hit rate: **47.85%**
- Baseline (random): **41.82%**
- **LIFT: +6.04pp**
- p-value: 0.0157

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #4 — `MT:G5#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1 miền MT** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **156**
- Hit rate: **47.71%**
- Baseline (random): **41.77%**
- **LIFT: +5.94pp**
- p-value: 0.0170

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #5 — `MT:G3#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1 miền MT** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **156**
- Hit rate: **47.71%**
- Baseline (random): **41.77%**
- **LIFT: +5.94pp**
- p-value: 0.0170

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #6 — `MB:G6#2:D-1`

**Strength**: STRONG

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 2 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **96**
- Hit rate: **29.45%**
- Baseline (random): **23.79%**
- **LIFT: +5.66pp**
- p-value: 0.0097

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #7 — `MB:DB#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.62%**
- Baseline (random): **23.79%**
- **LIFT: +4.83pp**
- p-value: 0.0239

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #8 — `MB:G2#2:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 2 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.53%**
- Baseline (random): **23.79%**
- **LIFT: +4.74pp**
- p-value: 0.0258

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #9 — `MB:G6#3:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 3 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.53%**
- Baseline (random): **23.79%**
- **LIFT: +4.74pp**
- p-value: 0.0258

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #10 — `MB:G7#4:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.31%**
- Baseline (random): **23.79%**
- **LIFT: +4.52pp**
- p-value: 0.0322

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #11 — `MB:G7#4:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.31%**
- Baseline (random): **23.79%**
- **LIFT: +4.52pp**
- p-value: 0.0322

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #12 — `MB:G7#4:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Hai (T2) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.31%**
- Baseline (random): **23.79%**
- **LIFT: +4.52pp**
- p-value: 0.0322

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---


## MB × Thứ Ba (T3)

**Đài hoạt động ngày này**:
- MB_BOARD

**Coverage trong cell này**: 296 rule có data, **14 đạt p<0.05**, **1 BH-pass** ⭐.

### Rule #1 ⭐ — `MN:G3#2:D-2`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 2 miền MN** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **203**
- Hit rate: **62.46%**
- Baseline (random): **54.83%**
- **LIFT: +7.63pp**
- p-value: 0.0034
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #2 — `MN:G3#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1 miền MN** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **199**
- Hit rate: **61.04%**
- Baseline (random): **54.95%**
- **LIFT: +6.09pp**
- p-value: 0.0155

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #3 — `MB:G1#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **324**
- Số ngày trúng (ANY station of MB): **95**
- Hit rate: **29.32%**
- Baseline (random): **23.79%**
- **LIFT: +5.54pp**
- p-value: 0.0115

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #4 — `MB:G4#3:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 3 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **95**
- Hit rate: **29.23%**
- Baseline (random): **23.79%**
- **LIFT: +5.45pp**
- p-value: 0.0125

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #5 — `MB:G7#4:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **94**
- Hit rate: **28.92%**
- Baseline (random): **23.79%**
- **LIFT: +5.14pp**
- p-value: 0.0174

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #6 — `MB:G7#4:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **94**
- Hit rate: **28.92%**
- Baseline (random): **23.79%**
- **LIFT: +5.14pp**
- p-value: 0.0174

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #7 — `MB:G7#4:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **94**
- Hit rate: **28.92%**
- Baseline (random): **23.79%**
- **LIFT: +5.14pp**
- p-value: 0.0174

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #8 — `MB:G6#2:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 2 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **324**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.70%**
- Baseline (random): **23.79%**
- **LIFT: +4.92pp**
- p-value: 0.0220

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #9 — `MB:G7#2:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 2 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.62%**
- Baseline (random): **23.79%**
- **LIFT: +4.83pp**
- p-value: 0.0239

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #10 — `MB:G7#2:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 2 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.62%**
- Baseline (random): **23.79%**
- **LIFT: +4.83pp**
- p-value: 0.0239

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #11 — `MB:G7#2:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Ba (T3) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 2 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.62%**
- Baseline (random): **23.79%**
- **LIFT: +4.83pp**
- p-value: 0.0239

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---


## MB × Thứ Tư (T4)

**Đài hoạt động ngày này**:
- MB_BOARD

**Coverage trong cell này**: 296 rule có data, **21 đạt p<0.05**, **1 BH-pass** ⭐.

### Rule #1 ⭐ — `MB:G7#4:D-1`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **101**
- Hit rate: **30.98%**
- Baseline (random): **23.79%**
- **LIFT: +7.20pp**
- p-value: 0.0014
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #2 — `MB:G7#4:D-1`

**Strength**: STRONG

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **101**
- Hit rate: **30.98%**
- Baseline (random): **23.79%**
- **LIFT: +7.20pp**
- p-value: 0.0014

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #3 — `MB:G7#4:D-1`

**Strength**: STRONG

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **101**
- Hit rate: **30.98%**
- Baseline (random): **23.79%**
- **LIFT: +7.20pp**
- p-value: 0.0014

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #4 — `MB:G6#2:D-1`

**Strength**: STRONG

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 2 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **96**
- Hit rate: **29.45%**
- Baseline (random): **23.79%**
- **LIFT: +5.66pp**
- p-value: 0.0097

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #5 — `MB:G7#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MB): **95**
- Hit rate: **29.41%**
- Baseline (random): **23.79%**
- **LIFT: +5.63pp**
- p-value: 0.0105

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #6 — `MB:G7#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MB): **95**
- Hit rate: **29.41%**
- Baseline (random): **23.79%**
- **LIFT: +5.63pp**
- p-value: 0.0105

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #7 — `MB:G7#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MB): **95**
- Hit rate: **29.41%**
- Baseline (random): **23.79%**
- **LIFT: +5.63pp**
- p-value: 0.0105

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #8 — `MB:G2#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **95**
- Hit rate: **29.14%**
- Baseline (random): **23.79%**
- **LIFT: +5.36pp**
- p-value: 0.0137

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #9 — `MT:G7#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1 miền MT** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **153**
- Hit rate: **46.93%**
- Baseline (random): **41.67%**
- **LIFT: +5.26pp**
- p-value: 0.0307

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #10 — `MN:G3#2:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 2 miền MN** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **196**
- Hit rate: **60.12%**
- Baseline (random): **54.91%**
- **LIFT: +5.21pp**
- p-value: 0.0332

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #11 — `MN:DB#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MN** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **194**
- Hit rate: **59.33%**
- Baseline (random): **54.57%**
- **LIFT: +4.75pp**
- p-value: 0.0474

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #12 — `MB:DB#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Tư (T4) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.53%**
- Baseline (random): **23.79%**
- **LIFT: +4.74pp**
- p-value: 0.0258

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---


## MB × Thứ Năm (T5)

**Đài hoạt động ngày này**:
- MB_BOARD

**Coverage trong cell này**: 296 rule có data, **12 đạt p<0.05**, **2 BH-pass** ⭐.

### Rule #1 ⭐ — `MB:G2#2:D-1`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 2 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **99**
- Hit rate: **30.28%**
- Baseline (random): **23.79%**
- **LIFT: +6.49pp**
- p-value: 0.0036
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #2 ⭐ — `MB:DB#1:D-3`

**Strength**: ⭐ STRONG (BH-pass)

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MB): **97**
- Hit rate: **30.03%**
- Baseline (random): **23.79%**
- **LIFT: +6.25pp**
- p-value: 0.0051
- BH-pass FDR α=0.05: ✓ PASS (gold standard)

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #3 — `MN:G3#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1 miền MN** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **199**
- Hit rate: **61.23%**
- Baseline (random): **54.95%**
- **LIFT: +6.28pp**
- p-value: 0.0132

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #4 — `MB:G2#2:D-1`

**Strength**: STRONG

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 2 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **98**
- Hit rate: **29.97%**
- Baseline (random): **23.79%**
- **LIFT: +6.18pp**
- p-value: 0.0052

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #5 — `MN:G2#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MN** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **198**
- Hit rate: **60.92%**
- Baseline (random): **54.98%**
- **LIFT: +5.94pp**
- p-value: 0.0180

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #6 — `MT:G3#2:D`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 2 miền MT** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **198**
- Hit rate: **60.55%**
- Baseline (random): **55.25%**
- **LIFT: +5.30pp**
- p-value: 0.0306

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #7 — `MN:G8#1:D`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 8 bộ 1 miền MN** ngày cùng ngày → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **198**
- Hit rate: **60.55%**
- Baseline (random): **55.36%**
- **LIFT: +5.19pp**
- p-value: 0.0335

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #8 — `MB:G4#4:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 4 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.44%**
- Baseline (random): **23.79%**
- **LIFT: +4.65pp**
- p-value: 0.0279

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #9 — `MB:G4#2:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 2 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MB): **91**
- Hit rate: **28.17%**
- Baseline (random): **23.79%**
- **LIFT: +4.39pp**
- p-value: 0.0370

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #10 — `MB:G4#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 1 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MB): **91**
- Hit rate: **28.17%**
- Baseline (random): **23.79%**
- **LIFT: +4.39pp**
- p-value: 0.0370

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #11 — `MB:G4#3:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 3 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **323**
- Số ngày trúng (ANY station of MB): **91**
- Hit rate: **28.17%**
- Baseline (random): **23.79%**
- **LIFT: +4.39pp**
- p-value: 0.0370

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #12 — `MB:DB#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Năm (T5) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.13%**
- Baseline (random): **23.79%**
- **LIFT: +4.35pp**
- p-value: 0.0374

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---


## MB × Thứ Sáu (T6)

**Đài hoạt động ngày này**:
- MB_BOARD

**Coverage trong cell này**: 296 rule có data, **13 đạt p<0.05**, **0 BH-pass** ⭐.

### Rule #1 — `MB:G4#3:D-1`

**Strength**: STRONG

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 3 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **97**
- Hit rate: **29.75%**
- Baseline (random): **23.79%**
- **LIFT: +5.97pp**
- p-value: 0.0068

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #2 — `MN:G7#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 1 miền MN** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **197**
- Hit rate: **60.62%**
- Baseline (random): **54.98%**
- **LIFT: +5.63pp**
- p-value: 0.0236

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #3 — `MT:G1#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MT** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **153**
- Hit rate: **46.93%**
- Baseline (random): **41.72%**
- **LIFT: +5.21pp**
- p-value: 0.0320

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #4 — `MB:G4#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 1 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **94**
- Hit rate: **28.92%**
- Baseline (random): **23.79%**
- **LIFT: +5.14pp**
- p-value: 0.0174

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #5 — `MN:G2#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MN** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **195**
- Hit rate: **60.00%**
- Baseline (random): **54.98%**
- **LIFT: +5.02pp**
- p-value: 0.0390

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #6 — `MN:G3#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1 miền MN** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **194**
- Hit rate: **59.51%**
- Baseline (random): **54.65%**
- **LIFT: +4.86pp**
- p-value: 0.0438

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #7 — `MB:G7#3:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 3 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.22%**
- Baseline (random): **23.79%**
- **LIFT: +4.44pp**
- p-value: 0.0347

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #8 — `MB:G6#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 1 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.22%**
- Baseline (random): **23.79%**
- **LIFT: +4.44pp**
- p-value: 0.0347

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #9 — `MB:G7#3:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 3 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.22%**
- Baseline (random): **23.79%**
- **LIFT: +4.44pp**
- p-value: 0.0347

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #10 — `MB:G7#3:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Sáu (T6) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 3 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **326**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.22%**
- Baseline (random): **23.79%**
- **LIFT: +4.44pp**
- p-value: 0.0347

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---


## MB × Thứ Bảy (T7)

**Đài hoạt động ngày này**:
- MB_BOARD

**Coverage trong cell này**: 296 rule có data, **7 đạt p<0.05**, **0 BH-pass** ⭐.

### Rule #1 — `MN:G3#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1 miền MN** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **197**
- Hit rate: **60.62%**
- Baseline (random): **54.87%**
- **LIFT: +5.74pp**
- p-value: 0.0214

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #2 — `MT:G1#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MT** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **328**
- Số ngày trúng (ANY station of MB): **154**
- Hit rate: **46.95%**
- Baseline (random): **41.67%**
- **LIFT: +5.28pp**
- p-value: 0.0298

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #3 — `MT:G3#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 3 bộ 1 miền MT** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **198**
- Hit rate: **60.55%**
- Baseline (random): **55.36%**
- **LIFT: +5.19pp**
- p-value: 0.0335

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #4 — `MB:G4#4:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 4 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.62%**
- Baseline (random): **23.79%**
- **LIFT: +4.83pp**
- p-value: 0.0239

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #5 — `MB:DB#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải ĐB bộ 1 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.44%**
- Baseline (random): **23.79%**
- **LIFT: +4.65pp**
- p-value: 0.0279

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #6 — `MB:G4#3:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 3 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **92**
- Hit rate: **28.13%**
- Baseline (random): **23.79%**
- **LIFT: +4.35pp**
- p-value: 0.0374

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #7 — `MB:G1#1:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **324**
- Số ngày trúng (ANY station of MB): **91**
- Hit rate: **28.09%**
- Baseline (random): **23.79%**
- **LIFT: +4.30pp**
- p-value: 0.0398

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #8 — `MT:G5#1:D-1`

**Strength**: WEAK

**Mô tả**: Khi xổ Thứ Bảy (T7) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 5 bộ 1 miền MT** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **328**
- Số ngày trúng (ANY station of MB): **150**
- Hit rate: **45.73%**
- Baseline (random): **41.77%**
- **LIFT: +3.96pp**
- p-value: 0.0809

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---


## MB × Chủ Nhật (CN)

**Đài hoạt động ngày này**:
- MB_BOARD

**Coverage trong cell này**: 296 rule có data, **14 đạt p<0.05**, **0 BH-pass** ⭐.

### Rule #1 — `MB:G2#2:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 2 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **96**
- Hit rate: **29.36%**
- Baseline (random): **23.79%**
- **LIFT: +5.57pp**
- p-value: 0.0107

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #2 — `MB:G4#3:D-3`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 4 bộ 3 miền MB** ngày D-3 (trước 3 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **325**
- Số ngày trúng (ANY station of MB): **94**
- Hit rate: **28.92%**
- Baseline (random): **23.79%**
- **LIFT: +5.14pp**
- p-value: 0.0174

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #3 — `MB:G6#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 1 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **94**
- Hit rate: **28.75%**
- Baseline (random): **23.79%**
- **LIFT: +4.96pp**
- p-value: 0.0206

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #4 — `MB:G1#1:D-1`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MB** ngày D-1 (trước 1 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **328**
- Số ngày trúng (ANY station of MB): **94**
- Hit rate: **28.66%**
- Baseline (random): **23.79%**
- **LIFT: +4.87pp**
- p-value: 0.0223

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #5 — `MN:G1#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 1 bộ 1 miền MN** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **328**
- Số ngày trúng (ANY station of MB): **195**
- Hit rate: **59.45%**
- Baseline (random): **54.73%**
- **LIFT: +4.72pp**
- p-value: 0.0482

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #6 — `MB:G7#4:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 7 bộ 4 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.44%**
- Baseline (random): **23.79%**
- **LIFT: +4.65pp**
- p-value: 0.0279

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #7 — `MB:G6#3:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 6 bộ 3 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.44%**
- Baseline (random): **23.79%**
- **LIFT: +4.65pp**
- p-value: 0.0279

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

---

### Rule #8 — `MB:G2#1:D-2`

**Strength**: MODERATE

**Mô tả**: Khi xổ Chủ Nhật (CN) miền MB: lấy LAST2 (2 chữ số cuối) của **Giải 2 bộ 1 miền MB** ngày D-2 (trước 2 ngày) → kỳ vọng xuất hiện trong các đuôi giải miền MB ngày D.

**Số liệu lịch sử**:
- Số ngày đánh giá: **327**
- Số ngày trúng (ANY station of MB): **93**
- Hit rate: **28.44%**
- Baseline (random): **23.79%**
- **LIFT: +4.65pp**
- p-value: 0.0279

**Per-station breakdown** (đài nào contribute nhiều nhất):

| Đài | n eval | Hits | Hit rate | CI95 |
|---|---|---|---|---|
| MB_BOARD | 0 | 0 | 0.00% | [0.0-0.0]% |

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