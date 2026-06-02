# V10669 — Báo Cáo Verify Toàn Diện Temporal Causality (Owner Report VN)

> **Generated**: 2026-06-02 10:45 VN
> **Trigger**: Owner 02/06 — "kiểm tra lại thật kỹ... MN xổ đầu, tiếp MT, cuối MB... verify lại hết... tổng hợp báo cáo đầy đủ"
> **Kết quả tổng**: ✅ **OVERALL CLEAN = True** (mọi output sử dụng được đã sạch 100%)

---

## 0. TL;DR

Em đã quét **TOÀN BỘ artifacts** của session V10636 (8 file JSON grid + 2 registry + 3 file region MD + ranking + raw + harness). Kết quả:

| Nhóm | Trạng thái |
|---|---|
| **Output dùng được** (3 region docs, ranking, raw, FIXED registry, harness) | ✅ **SẠCH 100%** |
| Raw grid gốc (CROSS_FULL_GRID) | ✅ Giữ data nhưng đã **flag** mọi violation |
| Registry cũ (35 rules) | ✅ Đã **mark DEPRECATED** + xóa khỏi public |

→ Không còn rule vi phạm thứ tự xổ nào trong tài liệu anh/AI tool sử dụng.

---

## 1. Xác nhận thứ tự xổ (anh nhấn mạnh)

| Miền | Giờ xổ | Thứ tự |
|---|---|---|
| **MN** (Miền Nam) | ~16:10 - 16:30 | **1st (ĐẦU TIÊN)** |
| **MT** (Miền Trung) | ~17:10 - 17:30 | **2nd (GIỮA)** |
| **MB** (Miền Bắc) | ~18:15 - 18:30 | **3rd (CUỐI CÙNG)** |

**Quy tắc temporal**: Rule "Nguồn(D) → Đích(D)" cùng ngày CHỈ hợp lệ nếu **Nguồn xổ TRƯỚC Đích**. Nếu nguồn xổ sau → dùng data tương lai → INVALID.

---

## 2. Kết quả verify từng file

### 2.1. File JSON grid (raw analysis data)

| File | Cells | Violations | Trạng thái |
|---|---|---|---|
| V10636_CROSS_FULL_GRID.json | 2,387 | 266 | ✅ RAW_ANNOTATED (mọi cell violation đã flag `temporal_violation=true`) |
| V10636_LP_PER_STATION_PRIZE.json | 210 | 0 | ✅ CLEAN (nguồn MB GĐB D-1, lag≥1) |
| V10636_EXT_FULL_GRID.json | 288 | 0 | ✅ CLEAN (toàn lag≥1) |
| V10636_DIG_FULL_GRID.json | 784 | 0 | ✅ CLEAN (MB self-lag cùng miền) |
| V10636_LAGS_FULL_GRID.json | 180 | 0 | ✅ CLEAN (lag D-1/D-2/D-3) |

→ **Chỉ V10636-CROSS có same-day (lag=0) cross-region** nên chỉ nó có violations. Các pass khác toàn lag≥1 hoặc self-lag → không thể vi phạm.

### 2.2. Forward audit registries

| File | Rules | Violations | Trạng thái |
|---|---|---|---|
| V10636_FORWARD_AUDIT_REGISTRY.json (cũ) | 35 | 7 | ✅ DEPRECATED (đã mark `_DEPRECATED`, xóa khỏi public, harness KHÔNG dùng) |
| **V10668_FORWARD_AUDIT_REGISTRY_FIXED.json** | **28** | **0** | ✅ **CLEAN — harness đang dùng file này** |

### 2.3. Output documents (anh + AI tool dùng)

| File | Rules | Violations | Trạng thái |
|---|---|---|---|
| V10636_OWNER_REFERENCE_RANKING.json | 197 | 0 | ✅ CLEAN |
| V10667_RULES_PER_REGION_RAW.json | 197 | 0 | ✅ CLEAN |
| V10667_RULES_MB_TARGET.md | 37 | 0 | ✅ CLEAN |
| V10667_RULES_MN_TARGET.md | 30 | 0 | ✅ CLEAN |
| V10667_RULES_MT_TARGET.md | 32 | 0 | ✅ CLEAN |

### 2.4. Harness

✅ `_forward_audit_harness.py` đã update đọc **FIXED registry** (28 rules), fallback cũ chỉ khi không có fixed. Test chạy: `Using TEMPORAL-FIXED registry: V10668_FORWARD_AUDIT_REGISTRY_FIXED.json`.

---

## 3. Phân tích vì sao chỉ CROSS có violations

Em rà soát logic từng pass trong session:

| Pass | Source → Target | Lag | Có same-day cross-region? |
|---|---|---|---|
| V10636-MAIN | MB GĐB → MN/MT | D-1 | ❌ Không (lag≥1) |
| V10636-LP | MB GĐB → MN/MT station | D-1 | ❌ Không |
| V10636-EXT | MB GĐB → MN/MT | D-1..D-21 | ❌ Không |
| V10636-MBSELF | MB prize → MB | D-1 | ❌ Không (cùng miền) |
| V10636-DIG | MB self-lag → MB | D-1 | ❌ Không |
| V10636-LAGS | MB self → MB | D-1/D-2/D-3 | ❌ Không |
| **V10636-CROSS** | **MN/MT/MB → MN/MT/MB** | **D=0, D-1, D-2, D-3** | ✅ **CÓ — đây là nguồn duy nhất của bug** |

→ Bug **chỉ tồn tại trong V10636-CROSS** vì đó là pass duy nhất em test lag=0 (same-day) cross-region. Em đã confirm điều này bằng cách scan thực tế tất cả file, không chỉ dựa vào trí nhớ.

---

## 4. 3 hướng same-day INVALID (đã loại toàn bộ)

| Direction | Lý do invalid | Số cells | BH-pass loại |
|---|---|---|---|
| **MT(D) → MN(D)** | MT 17:10 xổ SAU MN 16:10 | 56 | 8 |
| **MB(D) → MN(D)** | MB 18:15 xổ SAU MN 16:10 | 105 | 11 |
| **MB(D) → MT(D)** | MB 18:15 xổ SAU MT 17:10 | 105 | 17 |
| **TỔNG** | | **266** | **36** |

## 5. 3 hướng same-day VALID (giữ lại)

| Direction | Lý do valid |
|---|---|
| MN(D) → MT(D) | MN xổ trước MT — dùng được sau khi MN closeout |
| MN(D) → MB(D) | MN xổ trước MB |
| MT(D) → MB(D) | MT xổ trước MB |

(Tất cả lag≥1 đều valid vì ngày trước đã biết hết.)

---

## 6. Nguyên tắc đúng theo từng miền target

| Target | Xổ thứ | Nguồn same-day (D=0) được dùng | Nguồn lag≥1 |
|---|---|---|---|
| **MN** | 1st | ❌ KHÔNG có (vì MN xổ đầu, không miền nào xổ trước) — chỉ MN self ngày trước | ✅ MN/MT/MB D-1, D-2, D-3 |
| **MT** | 2nd | ✅ MN(D) — MN xổ trước. ❌ MB(D) loại | ✅ MN/MT/MB D-1, D-2, D-3 |
| **MB** | 3rd | ✅ MN(D) + MT(D) — cả 2 xổ trước MB | ✅ MN/MT/MB D-1, D-2, D-3 |

→ **MN target là miền bị giới hạn nhất**: vì xổ đầu tiên nên KHÔNG có "shortcut same-day" từ miền nào khác. Chỉ dùng được lịch sử (lag≥1) hoặc MN tự thân ngày trước.

---

## 7. Hành động finalize (V10669)

| # | Action | Status |
|---|---|---|
| 1 | Annotate CROSS_FULL_GRID — flag 266 cells `temporal_violation=true` + annotation block | ✅ |
| 2 | Mark registry cũ `V10636_FORWARD_AUDIT_REGISTRY.json` thành `_DEPRECATED` | ✅ |
| 3 | Xóa registry cũ khỏi public bundle (chỉ giữ FIXED 28) | ✅ |
| 4 | Update harness đọc FIXED registry + fallback warning | ✅ |
| 5 | Re-verify toàn bộ → OVERALL CLEAN = True | ✅ |

---

## 8. Còn lại bao nhiêu rule mạnh dùng được sau fix?

| Metric | Trước fix | Sau fix |
|---|---|---|
| BH-pass cells (gold standard) | 268 | **232 valid** |
| Forward audit rules | 35 | **28 valid** |
| Region docs total rules | (có violations) | MB 37 + MN 30 + MT 32 = 99 (sạch) |

→ Vẫn còn **232 BH-pass cells** + **28 forward audit rules** hợp lệ làm baseline thực sự.

### Top 5 rule mạnh nhất CÒN VALID sau fix

| Rank | Rule | Lift | Loại |
|---|---|---|---|
| 1 | MT G2#1 D-2 → MT T7 (self-lag) | +15.50pp | MT self, lag≥1 ✓ |
| 2 | MT G2#1 D-2 → MT T5 (self-lag) | +14.82pp | MT self ✓ |
| 3 | MB G4#2 D-1 → MT T5 | +14.42pp | MB→MT lag≥1 ✓ |
| 4 | MN G5#1 D → MT T5 | +13.85pp | MN(D)→MT(D) — MN xổ trước MT ✓ |
| 5 | MB G4#2 D-3 → MT T7 | +13.79pp | MB→MT lag≥1 ✓ |

---

## 9. Safety

| Check | Status |
|---|---|
| official_mutation | 0 |
| mined_rules mutation | 0 (READ-ONLY) |
| Đây là verification + annotation, không phải data mutation | ✓ |
| Tất cả output dùng được đã sạch temporal | ✅ verified |
| Harness dùng FIXED registry | ✅ |
| Public bundle đã xóa registry cũ | ✅ |

---

## 10. Kết luận cho anh

Em đã verify **THẬT KỸ** đúng như anh yêu cầu, không dựa trí nhớ mà scan thực tế từng file:

1. ✅ Xác nhận thứ tự xổ **MN (16:10) → MT (17:10) → MB (18:15)**
2. ✅ Bug chỉ ở V10636-CROSS (pass duy nhất có same-day cross-region). Các pass khác sạch.
3. ✅ 266 violations đã loại khỏi mọi output, raw data giữ lại nhưng đã flag
4. ✅ Registry cũ deprecated + xóa khỏi public; harness dùng FIXED 28 rules
5. ✅ 3 region docs + ranking + raw đều CLEAN (verify bằng parse trực tiếp)
6. ✅ OVERALL CLEAN = True

Còn 232 BH-pass cells + 28 forward audit rules hợp lệ. Quy tắc vàng: **MN target chỉ dùng lag≥1 hoặc MN self; MT dùng MN(D) OK + MB(D) loại; MB dùng cả MN(D)+MT(D)**.

---

**STATUS**: V10669 COMPREHENSIVE TEMPORAL VERIFICATION — OVERALL CLEAN = True. Mọi output sử dụng được đã sạch 100%, raw data annotated, registry cũ deprecated, harness dùng FIXED.
