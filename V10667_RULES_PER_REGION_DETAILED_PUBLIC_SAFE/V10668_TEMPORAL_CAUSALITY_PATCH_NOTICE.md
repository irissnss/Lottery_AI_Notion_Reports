# V10668 — TEMPORAL CAUSALITY FIX NOTICE (CRITICAL)

> **Patch date**: 2026-06-02 10:30 VN
> **Trigger**: Owner phát hiện rule "MN ngày D Thứ 3 = MT DB bộ 1 ngày D" có vấn đề:
> "MT xổ sau MN mà lấy nguồn MT D thì có gì đó sai sai"
> → **Anh đúng 100%. Đây là BUG NGHIÊM TRỌNG trong analysis V10667.1**.

---

## 1. Vấn đề: Vi phạm Temporal Causality

### Thứ tự xổ thực tế Việt Nam (chronological order)

| Region | Giờ xổ chính (~) |
|---|---|
| **MN** | **16:10 - 16:30** (xổ TRƯỚC) |
| **MT** | **17:10 - 17:30** (xổ SAU MN) |
| **MB** | **18:15 - 18:30** (xổ SAU CÙNG) |

### Quy luật

Một rule "Source(D) → Target(D)" với lag=0 (same-day) **CHỈ HỢP LỆ** khi source xổ **TRƯỚC** target. Nếu source xổ SAU target, ta đang dùng "data từ tương lai" để dự đoán quá khứ — vi phạm temporal causality, không có giá trị actionable cho forward prediction.

### 6 trường hợp lag=D cross-region phân loại

| Source → Target | Source xổ trước target? | Valid? |
|---|---|---|
| MN(D) → MT(D) | ✅ MN 16:10 trước MT 17:10 | ✅ **VALID** |
| MN(D) → MB(D) | ✅ MN 16:10 trước MB 18:15 | ✅ **VALID** |
| MT(D) → MB(D) | ✅ MT 17:10 trước MB 18:15 | ✅ **VALID** |
| **MT(D) → MN(D)** | ❌ MT 17:10 SAU MN 16:10 | ❌ **INVALID** |
| **MB(D) → MN(D)** | ❌ MB 18:15 SAU MN 16:10 | ❌ **INVALID** |
| **MB(D) → MT(D)** | ❌ MB 18:15 SAU MT 17:10 | ❌ **INVALID** |

(Lag ≥ 1 ngày: TẤT CẢ combinations valid vì previous day fully known.)

---

## 2. Quy mô bug trong V10667.1

Audit `V10668_TEMPORAL_VIOLATION_AUDIT.json` cho thấy:

| Metric | Value |
|---|---|
| Total cells V10636-CROSS | 2,387 |
| **Cells temporal violation** | **266 (11.14%)** |
| Cells valid | 2,121 |
| **BH-pass violations** | **36 / 268 total BH-pass (13.43%)** |
| BH-pass valid | 232 |
| p<0.05 violations | 48 |
| p<0.05 valid | 320 |

### Breakdown violations theo direction

| Direction | Total cells | p<0.05 invalid | BH-pass invalid |
|---|---|---|---|
| MB(D) → MN(D) | 105 | 14 | 11 |
| MB(D) → MT(D) | 105 | 25 | 17 |
| MT(D) → MN(D) | 56 | 9 | 8 |
| **TỔNG** | **266** | **48** | **36** |

### 7 rule trong Forward Audit Registry bị loại

Em đã đăng ký 35 rule cho 90-day forward audit. Sau khi audit temporal violation: **7 rule INVALID phải drop**:

| ❌ Dropped Rule | Lift bị loại bỏ |
|---|---|
| MB:G7#1:D → (MN,T7) | +16.68pp ⭐⭐⭐ (đây là rule #1 mạnh nhất em từng tìm thấy) |
| MB:G7#3:D → (MT,T5) | +14.26pp |
| MB:G4#1:D → (MN,T7) | +13.00pp |
| MB:G2#1:D → (MT,T7) | +12.87pp |
| MB:G4#1:D → (MT,T7) | +12.57pp |
| MB:G6#1:D → (MT,T7) | +12.26pp |
| MB:G2#2:D → (MT,T7) | +11.95pp |

→ **Forward audit registry fix**: 35 → 28 valid rules.

---

## 3. Top valid rules sau khi fix

### Top 15 cells valid (BH-pass) — đã loại violations

| Rank | Rule | Lift | p | Direction valid? |
|---|---|---|---|---|
| 1 | MT G2#1 D-2 → MT T7 (self-lag) | +15.50pp | <0.0001 | ✅ |
| 2 | MT G2#1 D-2 → MT T5 (self-lag) | +14.82pp | <0.0001 | ✅ |
| 3 | MB G4#2 D-1 → MT T5 | +14.42pp | <0.0001 | ✅ (lag ≥ 1) |
| 4 | MN G5#1 D → MT T5 | +13.85pp | <0.0001 | ✅ (MN trước MT) |
| 5 | MB G4#2 D-3 → MT T7 | +13.79pp | <0.0001 | ✅ |
| 6 | MT DB#1 D-1 → MT T5 (self-lag) | +13.60pp | <0.0001 | ✅ |
| 7 | MT G5#1 D-2 → MT T7 (self-lag) | +13.37pp | <0.0001 | ✅ |
| 8 | MB G1#1 D-3 → MN T7 | +13.31pp | <0.0001 | ✅ (lag ≥ 1) |
| 9 | MB G2#2 D-3 → MT T7 | +13.18pp | <0.0001 | ✅ |
| 10 | MB G6#3 D-3 → MT T7 | +13.18pp | <0.0001 | ✅ |
| 11 | MN G3#2 D-3 → MT T5 | +13.17pp | <0.0001 | ✅ |
| 12 | MB G2#1 D-3 → MT T5 | +13.02pp | <0.0001 | ✅ |
| 13 | MB G2#2 D-1 → MN T7 | +13.00pp | <0.0001 | ✅ (lag ≥ 1) |
| 14 | MN G5#1 D-1 → MT T5 | +12.83pp | <0.0001 | ✅ |
| 15 | MT G1#1 D-1 → MT T5 (self-lag) | +12.66pp | <0.0001 | ✅ |

→ **Vẫn còn 232 BH-pass valid cells** sau fix. Đây là baseline thực sự sử dụng được.

---

## 4. Impact per (target × weekday) cell

Cell ảnh hưởng nặng nhất bởi fix:

| Target | Weekday | OLD top rule (invalid) | NEW top rule (valid) | Lift change |
|---|---|---|---|---|
| MN | T3 | MT DB#1 D (+7.28pp) ⭐ | MB G4#1 D-1 (+5.33pp) | mất BH-pass |
| MN | T7 | MB G7#1 D (+16.68pp) ⭐⭐⭐ | MB G1#1 D-3 (+13.31pp) | giảm -3.4pp |
| MT | T7 | (giữ nguyên top) MT G2#1 D-2 (+15.50pp) | same | unchanged |
| MT | T5 | (giữ nguyên top) | same | unchanged |
| MB | (all weekdays) | unchanged — MB là region xổ cuối, mọi nguồn MN/MT/MB của ngày D đều đã xổ trước MB | no change | unchanged |

→ **MB target không bị ảnh hưởng** vì MB xổ cuối cùng (18:15), nên dùng MN(D) hoặc MT(D) làm nguồn cho MB(D) đều hợp lệ (cả 2 đã xổ trước MB).

→ **MT target bị ảnh hưởng nhẹ**: chỉ mất các rule MB(D)→MT(D); các rule MN(D)→MT(D) và MT self-lag vẫn giữ. Top rule MT T5/T7 (MT G2#1 D-2 self-lag) KHÔNG đổi.

→ **MN target bị ảnh hưởng nặng nhất**: MN xổ đầu tiên nên KHÔNG được dùng bất kỳ nguồn same-day nào từ MT/MB. Chỉ giữ được: MN self-lag (D-1/D-2/D-3) + MN/MT/MB nguồn lag ≥ 1 ngày.

---

## 5. Nguyên tắc đúng cho MN target (quan trọng nhất)

Vì **MN xổ ĐẦU TIÊN trong ngày**, rule cho MN target chỉ được dùng:

| Loại nguồn | Hợp lệ? | Lý do |
|---|---|---|
| MN self-lag (D-1, D-2, D-3) | ✅ | Ngày trước đã biết |
| MT D-1, D-2, D-3 | ✅ | MT ngày trước đã xổ xong |
| MB D-1, D-2, D-3 | ✅ | MB ngày trước đã xổ xong |
| **MT(D) same-day** | ❌ | MT xổ SAU MN cùng ngày |
| **MB(D) same-day** | ❌ | MB xổ SAU MN cùng ngày |
| MN(D) same-day | ❌ (trivial) | Chính nó |

→ **MN chỉ predict được từ data quá khứ (lag ≥ 1) hoặc MN self-lag**. Không có "shortcut same-day" từ miền khác.

---

## 6. Files đã fix trong patch V10668

| File | Thay đổi |
|---|---|
| `_audit_temporal_violations.py` | NEW — audit script phát hiện 266 violation cells |
| `_build_owner_reference_ranking.py` | Thêm `is_temporal_violation()` filter |
| `_build_per_region_detailed_rules.py` | Thêm filter, skip violation rules |
| `V10636_OWNER_REFERENCE_RANKING.md/.json` | Re-built, đã loại violations |
| `V10667_RULES_MB/MN/MT_TARGET.md` | Re-built, đã loại violations |
| `V10668_FORWARD_AUDIT_REGISTRY_FIXED.json` | 35 → 28 valid rules |
| `V10668_TEMPORAL_VIOLATION_AUDIT.json` | Full violation map |
| `V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md` | File này |

---

## 7. Lời cảm ơn anh

Anh phát hiện bug này cực kỳ giá trị. Nếu không có anh chỉ ra "MT xổ sau MN mà lấy nguồn MT D thì sai sai", thì:
- 36 BH-pass cells temporal-invalid sẽ bị tưởng nhầm là rule mạnh
- 7/35 forward audit rules (bao gồm rule #1 mạnh nhất +16.68pp) sẽ được track sai
- Tool AI ngoài đọc tài liệu public sẽ học pattern không thể dùng được trong thực tế

Đây là lỗi logic của em khi build cross-region matrix (V10636-CROSS) — em đã không áp ràng buộc thứ tự xổ. Em xin lỗi anh và đã fix toàn bộ.

---

## 8. Safety

| Check | Status |
|---|---|
| official_mutation | 0 |
| mined_rules mutation | 0 (READ-ONLY) |
| Đây là FIX của analysis bug, không phải data mutation | ✓ |
| Public docs sẽ được re-push với version V10668 | pending |

---

**STATUS**: V10668 TEMPORAL CAUSALITY FIX — 266 violation cells identified & filtered, 7 forward-audit rules dropped (35→28), all V10667 docs rebuilt clean. Pending public re-push as V10668.