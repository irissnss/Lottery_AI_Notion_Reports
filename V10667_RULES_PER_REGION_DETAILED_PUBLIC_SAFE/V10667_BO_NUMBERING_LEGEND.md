# V10667 — Quy Ước Đánh Số Bộ Số (Bộ Numbering Legend)

> **Mục đích**: Làm rõ ký hiệu `Giải X bộ Y` trong toàn bộ tài liệu rule V10667.
> **Trigger**: Owner ghi chú 02/06/2026 — "anh có bổ sung G4 ở MB với việc đánh số bộ số rõ ràng để làm nguồn cho rules. Với giải 4 hầu như chưa có trong tài liệu và hệ thống nên việc này nên ghi nhận thêm nhãn bổ sung và ghi chú bộ số thứ mấy được đánh dấu như nào, giải 6 và các giải khác có hơn 1 bộ số cũng tương tự đánh số cho rõ ràng."

---

## 1. Quy ước CHUNG

Trong tất cả tài liệu V10667, ký hiệu `Giải X bộ Y` (hoặc `GX#Y` trong rule_id) là:

- **`X`** = số giải (1, 2, 3, 4, 5, 6, 7, 8, hoặc ĐB)
- **`Y`** = số thứ tự bộ trong giải đó, đếm từ **trái sang phải, trên xuống dưới** trên bảng kết quả công bố

**Quy ước số hóa**: `Bộ Y` tương ứng với phần tử thứ `Y` (1-indexed) trong mảng JSON của giải đó. Tức là:
- DB array index 0 → BỘ 1
- DB array index 1 → BỘ 2
- DB array index N-1 → BỘ N

---

## 2. MIỀN BẮC (MB) — Bảng các giải có >1 bộ

### 2.1. Giải Đặc Biệt (G.ĐB) — 1 bộ

```
G.ĐB:  XXXXX   ← 1 số duy nhất, 5 chữ số
```

Ký hiệu: `DB#1` (1 bộ duy nhất). Đây là giải lớn nhất.

### 2.2. Giải 1 (G.1) — 1 bộ

```
G.1:   XXXXX   ← 1 số duy nhất, 5 chữ số
```

Ký hiệu: `G1#1`.

### 2.3. Giải 2 (G.2) — 2 bộ ⭐

```
G.2:   [BỘ 1]  [BỘ 2]
       XXXXX   XXXXX
```

Ký hiệu:
- `G2#1` = số bên trái (array index 0)
- `G2#2` = số bên phải (array index 1)

**Ví dụ verify trên MB 31/05/2026**:
```
G.2:   92978 [bộ 1]   42290 [bộ 2]
```

### 2.4. Giải 4 (G.4) — 4 bộ ⭐⭐ (OWNER MỚI BỔ SUNG)

> ⚠️ **Owner note 02/06/2026**: G.4 mới được bổ sung làm nguồn cho rules. Trước đó G.4 chưa có nhiều trong tài liệu và hệ thống. Anh đánh dấu rõ 4 bộ như sau:

```
G.4:   [BỘ 1]   [BỘ 2]
       XXXX     XXXX

       [BỘ 3]   [BỘ 4]
       XXXX     XXXX
```

(2 hàng × 2 cột, đếm từ trái-trên xuống phải-dưới)

Ký hiệu:
- `G4#1` = top-left (array index 0)
- `G4#2` = top-right (array index 1)
- `G4#3` = bottom-left (array index 2)
- `G4#4` = bottom-right (array index 3)

**Ví dụ verify trên MB 31/05/2026** (theo image anh đánh dấu):
```
G.4:   7717 [bộ 1]   7829 [bộ 2]
       5183 [bộ 3]   4559 [bộ 4]
```

**Khớp với owner image 31/05**: anh marked `1` trên số 7717 (top-left), `2` trên 7829 (top-right), `3` trên 5183 (bottom-left), `4` trên 4559 (bottom-right).

### 2.5. Giải 6 (G.6) — 3 bộ ⭐

```
G.6:   [BỘ 1]   [BỘ 2]   [BỘ 3]
       XXX      XXX      XXX
```

(3 bộ trên 1 hàng, đếm từ trái sang phải)

Ký hiệu:
- `G6#1` = bộ trái nhất (array index 0)
- `G6#2` = bộ giữa (array index 1)
- `G6#3` = bộ phải nhất (array index 2)

**Ví dụ verify trên MB 31/05/2026**:
```
G.6:   320 [bộ 1]   652 [bộ 2]   359 [bộ 3]
```

### 2.6. Giải 7 (G.7) — 4 bộ ⭐⭐

```
G.7:   [BỘ 1]  [BỘ 2]  [BỘ 3]  [BỘ 4]
       XX      XX      XX      XX
```

(4 bộ trên 1 hàng, đếm từ trái sang phải — đặc biệt G.7 là 2-digit native = đuôi 2d trực tiếp)

Ký hiệu:
- `G7#1` = bộ trái nhất (array index 0)
- `G7#2` = bộ thứ 2 (array index 1)
- `G7#3` = bộ thứ 3 (array index 2)
- `G7#4` = bộ phải nhất (array index 3)

**Ví dụ verify trên MB 31/05/2026**:
```
G.7:   73 [bộ 1]   39 [bộ 2]   81 [bộ 3]   84 [bộ 4]
```

### 2.7. Tóm tắt MB source whitelist (per owner constraint)

| Giải | Số bộ | Ký hiệu nguồn |
|---|---|---|
| Giải ĐB | 1 | `DB#1` |
| Giải 1 | 1 | `G1#1` |
| Giải 2 | 2 | `G2#1`, `G2#2` |
| **Giải 4** ⭐ MỚI | **4** | **`G4#1`, `G4#2`, `G4#3`, `G4#4`** |
| Giải 6 | 3 | `G6#1`, `G6#2`, `G6#3` |
| Giải 7 | 4 | `G7#1`, `G7#2`, `G7#3`, `G7#4` |

→ **15 nguồn MB/ngày** (1+1+2+4+3+4) khi anh xài đầy đủ tài liệu G.4 mới.

> ⚠️ **NOT included as MB source** (per owner constraint): G3 (2 bộ, 5d), G5 (6 bộ, 4d), G8 (4 bộ, 2d).

---

## 3. MIỀN NAM (MN) và MIỀN TRUNG (MT) — Bảng các giải có >1 bộ

MN và MT có cấu trúc giải GIỐNG NHAU. Bộ numbering áp dụng tương tự MB.

### 3.1. Giải 8 (G.8) — 1 bộ

```
G.8:   XX   ← 1 số 2 chữ số
```

Ký hiệu: `G8#1`.

### 3.2. Giải 7 (G.7) — 1 bộ

```
G.7:   XXX  ← 1 số 3 chữ số
```

Ký hiệu: `G7#1`.

### 3.3. Giải 6 (G.6) — 3 bộ

```
G.6:   XXXX   XXXX   XXXX
```

Ký hiệu: `G6#1`, `G6#2`, `G6#3` (trái sang phải).

> ⚠️ MN/MT G.6 thường KHÔNG dùng làm nguồn (em chỉ test G8/G7/G5/G3/G2/G1/DB của MN/MT theo whitelist).

### 3.4. Giải 5 (G.5) — 1 bộ

```
G.5:   XXXX   ← 1 số 4 chữ số
```

Ký hiệu: `G5#1`.

### 3.5. Giải 4 (G.4) — 7 bộ

(MN/MT G.4 có 7 bộ × 5 chữ số — không dùng làm nguồn trong V10667 do quá nhiều bộ.)

### 3.6. Giải 3 (G.3) — 2 bộ ⭐ (source-only per owner constraint)

```
G.3:   [BỘ 1]   [BỘ 2]
       XXXXX    XXXXX
```

Ký hiệu:
- `G3#1` = bộ trái (array index 0)
- `G3#2` = bộ phải (array index 1)

**Ví dụ verify trên MN Kiên Giang 31/05/2026**:
```
G.3:   17803 [bộ 1]   22584 [bộ 2]
```

> ⚠️ Per owner constraint: **MN/MT G3 chỉ làm NGUỒN (source), không làm TARGET**. MB G3 KHÔNG dùng làm nguồn (quá nhiều bộ trong context khác).

### 3.7. Giải 2 (G.2) — 1 bộ (khác MB)

```
G.2:   XXXXX   ← 1 số 5 chữ số (MN/MT, khác MB có 2 bộ)
```

Ký hiệu: `G2#1`.

### 3.8. Giải 1 (G.1) — 1 bộ

```
G.1:   XXXXX   ← 1 số 5 chữ số
```

Ký hiệu: `G1#1`.

### 3.9. Giải Đặc Biệt (G.ĐB) — 1 bộ

```
G.ĐB:  XXXXXX   ← 1 số 6 chữ số (MN/MT, khác MB có 5 chữ số)
```

Ký hiệu: `DB#1`.

### 3.10. Tóm tắt MN/MT source whitelist (per owner constraint)

| Giải | Số bộ | Ký hiệu nguồn |
|---|---|---|
| Giải 8 | 1 | `G8#1` |
| Giải 7 | 1 | `G7#1` |
| Giải 5 | 1 | `G5#1` |
| **Giải 3** ⭐ (source-only) | **2** | **`G3#1`, `G3#2`** |
| Giải 2 | 1 | `G2#1` |
| Giải 1 | 1 | `G1#1` |
| Giải ĐB | 1 | `DB#1` |

→ **8 source positions/station** với MN/MT, nhân với 3-4 stations/ngày = 24-32 source values/ngày/region.

---

## 4. Áp dụng nhãn `Giải X bộ Y` trong rule

Trong các tài liệu rule (MB/MN/MT target), khi anh thấy:

```
Rule #1 — `MB:G4#3:D-3`
**Mô tả**: lấy LAST2 của Giải 4 bộ 3 miền MB ngày D-3 (trước 3 ngày)
```

Có nghĩa là:
- **Nguồn**: Miền Bắc (MB)
- **Giải**: Giải 4
- **Bộ**: Bộ thứ 3 (= `5183` trong ví dụ MB 31/05/2026 = position bottom-left)
- **Lag**: D-3 (= 3 ngày trước ngày target D)
- **Transform**: LAST2 (2 chữ số cuối)

→ Cụ thể: nếu D = 02/06/2026 (Thứ Ba), thì source date = 30/05/2026, lấy G.4 bộ 3 của ngày đó = "5183", LAST2 = "83". Rule kỳ vọng "83" sẽ xuất hiện trong các đuôi giải MB ngày 02/06.

---

## 5. Owner image reference (để cross-check)

Anh đã gửi 2 hình ảnh đánh dấu các bộ số:

### 5.1. MB 24/05/2026 image (xosodaiphat.com)
Đánh dấu các giải có ít bộ số dùng làm nguồn:
- G.ĐB (1 bộ)
- G.1 (1 bộ)
- G.2 (2 bộ — số trái = bộ 1, số phải = bộ 2)
- **G.4 (4 bộ — số 1, 2, 3, 4 đánh dấu vị trí: top-left, top-right, bottom-left, bottom-right)** ⭐
- G.6 (3 bộ — trái-giữa-phải = 1-2-3)
- G.7 (4 bộ — trái sang phải = 1-2-3-4)

### 5.2. MB 31/05/2026 image (xosodaiphat.com)
Anh đánh số `1, 2, 3, 4` rõ ràng cạnh các bộ G.4:
- Bộ 1 = 7717 (top-left)
- Bộ 2 = 7829 (top-right)
- Bộ 3 = 5183 (bottom-left)
- Bộ 4 = 4559 (bottom-right)

→ Convention **khớp 100%** với DB array index (0=bộ 1, 1=bộ 2, 2=bộ 3, 3=bộ 4).

---

## 6. Lưu ý sử dụng

1. **Khi tra cứu rule cho ngày D**: tìm thứ trong tuần (T2-CN) → xem tài liệu miền tương ứng → top rule cell → đọc `nguồn:giải:lag` rồi áp dụng.
2. **Khi tra cứu DB raw**: array position = bộ_number − 1 (0-indexed in JSON, 1-indexed in `Giải X bộ Y` notation).
3. **G.4 mới**: nếu anh thấy rule với G4 bộ 1-4, hãy tra ảnh đánh dấu để biết position thực tế.
4. **G3 chỉ làm source MN/MT**: rule có "Giải 3 bộ 1" hoặc "Giải 3 bộ 2" là từ MN/MT, không phải MB.

---

## 7. Reference

- **Detailed rule docs**:
  - [V10667_RULES_MB_TARGET.md](./V10667_RULES_MB_TARGET.md) — Miền Bắc
  - [V10667_RULES_MN_TARGET.md](./V10667_RULES_MN_TARGET.md) — Miền Nam
  - [V10667_RULES_MT_TARGET.md](./V10667_RULES_MT_TARGET.md) — Miền Trung
- **Index hub**: [V10667_RULES_INDEX.md](./V10667_RULES_INDEX.md)
- **Forward audit (28 temporal-valid BH-pass rules)**: [machine_readable/V10668_FORWARD_AUDIT_REGISTRY_FIXED.json](./machine_readable/V10668_FORWARD_AUDIT_REGISTRY_FIXED.json) — bản 35-rule cũ đã DEPRECATED (7 cell vi phạm thứ tự xổ).
- **Master verification**: [V10672_MASTER_VERIFICATION_REPORT_VN.md](./V10672_MASTER_VERIFICATION_REPORT_VN.md)
- **Owner image gốc**: `assets/c__Users_Admin_..._image-4e73e7a8-...png` (MB 24/05) + `assets/...-image-b513c887-840a-498b-a15c-9c5893172a52.png` (MB 31/05)

---

**STATUS**: Bộ numbering legend documented. Convention verified against DB on 31/05/2026 owner annotation. G4 newly added MB source explicitly noted with position map.
