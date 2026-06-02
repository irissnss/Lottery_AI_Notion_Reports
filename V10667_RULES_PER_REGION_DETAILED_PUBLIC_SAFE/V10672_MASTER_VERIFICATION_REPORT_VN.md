# V10672 — Báo Cáo Verify TOÀN BỘ Rules Trong Hệ Thống (Master Verification)

> **Generated**: 2026-06-02 12:30 VN
> **Trigger**: Owner 02/06 — "với các sai lầm phát hiện ra với các Rules trước giờ... verify kiểm tra lại toàn bộ... xem thêm `artifacts` có nhiều tổng hợp báo cáo về rules... xem thật kỹ tránh bỏ sót, verify lại tất cả"
> **Phạm vi**: KHÔNG chỉ session V10636 (như V10669) mà **TẤT CẢ rule artifacts trong repo**: production LIVE + pre-register + 11 research mine + public bundle.
> **Kết quả tổng**: ✅ **PRODUCTION (LIVE) = SẠCH 100%** · ✅ **PRE-REGISTER = SẠCH** · ✅ **~234,000 dòng cross-region research = SẠCH (lag0 = 0)** · 1 file đánh dấu trung thực UNVERIFIABLE (valid by design).

---

## 0. TL;DR — đọc 30 giây

Anh lo: "3 lỗi đã phát hiện (temporal, #bộ, nguồn nhiều đài) có lan ra các rules KHÁC ngoài session vừa rồi không?"

**Trả lời: KHÔNG.** Em quét thực tế (không dựa trí nhớ) từng file rule trong `E:\Lottery_AI_Test\artifacts` + bảng `mined_rules` LIVE trong DB. Kết quả:

| Lớp | Số rule quét | Vi phạm temporal | Trạng thái |
|---|---|---|---|
| **PRODUCTION mined_rules (đang CHẠY LIVE)** | 105 | **0** | ✅ SẠCH |
| **_seed_rules.py** (máy sinh rule production) | config 3 miền | **0** | ✅ SẠCH (thiết kế đúng từ gốc) |
| **V10636 production lane gate** | 105 | **0** | ✅ SẠCH |
| **Pre-register panels** (V10626 + FU4) | 63 | **0** | ✅ SẠCH |
| **11 research mine** (V10604/05/06/26) | ~286,000 | **0** | ✅ SẠCH (234k dòng cross-region, lag0=0) |
| V10636-CROSS (exploratory của em) | 2,387 | 266 | ⚠ đã flag + loại khỏi output (V10668/69) |

→ **Bug temporal CHỈ tồn tại trong 1 grid thử nghiệm (V10636-CROSS) của em — đã xử lý xong. KHÔNG có rule LIVE nào, KHÔNG có report rule nào khác bị dính.**

---

## 1. Thứ tự xổ (nền tảng mọi kiểm tra)

| Miền | Giờ xổ | Thứ tự |
|---|---|---|
| **MN** (Miền Nam) | ~16:10–16:30 | **1st — ĐẦU TIÊN** |
| **MT** (Miền Trung) | ~17:10–17:30 | **2nd — GIỮA** |
| **MB** (Miền Bắc) | ~18:15–18:30 | **3rd — CUỐI** |

**Quy tắc temporal (luật vàng):** Rule "Nguồn(D) → Đích(D)" cùng ngày chỉ HỢP LỆ nếu **Nguồn xổ TRƯỚC Đích**.
- 3 hướng same-day **HỢP LỆ**: MN→MT, MN→MB, MT→MB.
- 3 hướng same-day **VI PHẠM** (dùng số tương lai): MT→MN, MB→MN, MB→MT.
- Mọi lag ≥ 1 ngày (D-1, D-2, D-3, W-x) **luôn hợp lệ** (ngày trước đã biết hết).

---

## 2. Phát hiện QUAN TRỌNG NHẤT — Production LIVE sạch từ gốc

Đây là điều V10669 **chưa** kiểm (V10669 chỉ soi session V10636). V10672 soi tới tận máy sinh rule và bảng đang chạy.

### 2.1. Máy sinh rule `_seed_rules.py` — `src_cfgs(target)`

```python
MN target ← [ MT:D-1 , MN:D-1 , MB:D-1 ]                      # CHỈ lag≥1
MT target ← [ MN:D0 , MT:D-1 , MN:D-1 , MB:D-1 ]             # MN(D0) hợp lệ (MN xổ trước MT)
MB target ← [ MT:D0 , MN:D0 , MT:D-1 , MN:D-1 , MB:D-1 ]     # MT(D0)+MN(D0) đều xổ trước MB
```

**Vì sao production không thể dính bug:**
- **MN** (xổ đầu) chỉ lấy nguồn **lag≥1** — không có "shortcut same-day" từ miền nào → an toàn tuyệt đối.
- **MT** chỉ lấy same-day từ **MN** (miền xổ trước) → hợp lệ. KHÔNG bao giờ lấy MB(D).
- **MB** lấy same-day từ **MT + MN** (cả hai xổ trước) → hợp lệ.

→ Máy sinh rule **được thiết kế đúng nguyên tắc temporal ngay từ đầu**. Nó **không bao giờ** sinh ra 3 hướng vi phạm (MT→MN, MB→MN, MB→MT same-day).

### 2.2. Bảng `mined_rules` LIVE (105 rule đang chạy)

Quét trực tiếp DB `data/lottery_ai.db` **đã sync từ VPS ngay trước khi verify** (manifest `artifacts/live_sync/20260602_122052/manifest.json`, status=ok; DB local đổi hash `675208…` → khớp VPS `566b94…`):

| Kiểm tra | Kết quả |
|---|---|
| Tổng rule | 105 |
| Rule vi phạm temporal | **0** |
| Rule **active** vi phạm | **0** |

→ Không một rule nào đang ảnh hưởng dự đoán thực tế bị lỗi thứ tự xổ — kiểm trên DB khớp đúng bản LIVE trên VPS.

> **Đối chiếu độc lập:** một audit runtime song song (V10671 DRAW-ORDER causality guard, `docs/CAUSALITY_AUDIT_MN_MT_MB_20260602.md`) đã kiểm 6 cơ chế runtime (mined_rules, prompt AI, AI chain, lag1 signals, adaptive_exploit, no-token momentum) và cũng kết luận **mined_rules 0 vi phạm** + gắn thêm hàng rào draw-order cho feature `cross_region_momentum`. V10672 (báo cáo này) bổ sung lớp ARTIFACT/REPORT; hai lớp khớp nhau.

---

## 3. Kết quả verify từng lớp artifact (quét thực tế)

### 3.1. Pre-register panels (rule chờ promote lên production)

| File | Rule | Vi phạm |
|---|---|---|
| V10626_PRE_REGISTER_PANEL_MB.csv | 15 | 0 ✅ |
| V10626_PRE_REGISTER_PANEL_MN.csv | 15 | 0 ✅ |
| V10626_PRE_REGISTER_PANEL_MT.csv | 20 | 0 ✅ |
| V10626_FU4_PRE_REGISTER_ADDENDUM_MB.csv | 4 | 0 ✅ |
| V10626_FU4_PRE_REGISTER_ADDENDUM_MN.csv | 3 | 0 ✅ |
| V10626_FU4_PRE_REGISTER_ADDENDUM_MT.csv | 6 | 0 ✅ |

→ Tất cả dùng trục **D-1, D-3, D-6, W-x** (lag≥1). Không có same-day cross-region.

### 3.2. Production lane (V10636 tier gate)

| File | Rule | Vi phạm |
|---|---|---|
| V10636_TOP_RULES_TIER_GATE.csv | 105 | 0 ✅ |

→ Cross-region toàn `source_offset = D-1` trở lên.

### 3.3. 11 research mine (kho khai thác rule — to nhất)

Đây là phần anh nhắc "artifacts có nhiều tổng hợp báo cáo về rules". Em quét từng file, **đếm số dòng cross-region thực sự parse được + số dòng lag0** để chứng minh không phải "clean giả do không đọc được cột":

| File | Dòng quét | Dòng cross-region | Dòng lag0 | Vi phạm |
|---|---|---|---|---|
| V10626_TOTAL_RULE_INVENTORY.csv | 55,546 | 47,775 | **0** | 0 ✅ |
| deep_source_rule_candidates.csv (V10606) | 54,924 | 47,223 | **0** | 0 ✅ |
| V10606_rejected_rules.csv | 98,304 | 81,321 | **0** | 0 ✅ |
| V10606_weekday_rules.csv | 21,978 | 18,195 | **0** | 0 ✅ |
| V10606_station_set_rules.csv | 21,904 | 18,905 | **0** | 0 ✅ |
| V10604_digit_transform_rules.csv | 16,310 | 10,704 | **0** | 0 ✅ |
| V10626_FU4_OWNER_SCHEMA_SCAN.csv | 8,000 | 4,877 | **0** | 0 ✅ |
| V10626_FU3_KEYNAME_LOW_PRIZE_SCAN.csv | 6,000 | 3,220 | **0** | 0 ✅ |
| V10604_source_rule_candidates.csv | 2,730 | 1,820 | **0** | 0 ✅ |
| **TỔNG (9 file parse được)** | **285,696** | **234,040** | **0** | **0 ✅** |
| v10605_mt_from_mb_d1d3.csv | 804 | — | — | ⚠ UNVERIFIABLE |

**Phát hiện cấu trúc quan trọng:** trong **234,040 dòng cross-region** thực sự parse được, **lag0 = 0 tuyệt đối**. Nghĩa là pipeline khai thác chuẩn (V10604/V10606/V10626) **chưa bao giờ sinh rule same-day cross-region** — nó chỉ mine lag≥1. Vì vậy **về mặt cấu trúc, các kho này không thể chứa bug temporal.**

---

## 4. Vì sao CHỈ V10636-CROSS có bug? (giải thích gốc rễ)

| Nguồn rule | Có test same-day (lag=0) cross-region? | Có bug? |
|---|---|---|
| Production `_seed_rules` | Chỉ hướng hợp lệ (MN→MT, MN/MT→MB) | ❌ Không |
| Pipeline mine V10604/06/26 | KHÔNG (chỉ lag≥1) | ❌ Không |
| Pre-register / lane gate | KHÔNG | ❌ Không |
| **V10636-CROSS (grid thử nghiệm của em)** | **CÓ — test MỌI hướng × MỌI lag để khám phá** | ✅ **Đây là nơi DUY NHẤT phát sinh 266 violation** |

→ Em cố tình test cả lag=0 mọi hướng trong V10636-CROSS để "đào bới" rule mạnh nhất. Đó là lý do nó lòi ra 266 cell vi phạm (gồm hướng MT→MN, MB→MN, MB→MT same-day). **Pipeline production/research chuẩn không làm vậy nên sạch.** Bug này đã được xử lý trọn vẹn ở V10668/V10669.

---

## 5. Trạng thái 3 lỗi đã phát hiện trước đó (cross-check toàn hệ thống)

| Lỗi | Phát hiện ở | Đã fix | Lan ra nơi khác? |
|---|---|---|---|
| **#1 Temporal causality** (same-day nguồn xổ sau đích) | V10636-CROSS | V10668 (loại 266 cell) + V10669 (annotate/deprecate/harness) | ❌ Không — production + 234k dòng research đều sạch (mục 2,3) |
| **#2 #Bộ là vị trí, không phải đài** | tài liệu region docs | V10670 (legend `#Bộ` = vị trí; mô tả rõ) | ❌ Không lan — chỉ là vấn đề diễn giải tài liệu |
| **#3 Nguồn nhiều đài (GOM/union)** | tài liệu region docs | V10670 (banner GOM + station-by-weekday DB-verified) | ❌ Không lan — đã ghi rõ MB xoay tỉnh theo thứ |

→ Cả 3 lỗi **đã xử lý xong và KHÔNG lan** sang production hay các report rule khác.

---

## 6. Đối chiếu với V10669 (verify trước đó vẫn đúng)

Em chạy lại verifier V10669 để chắc session V10636 vẫn sạch:

| Artifact (output dùng được) | Vi phạm |
|---|---|
| V10668_FORWARD_AUDIT_REGISTRY_FIXED.json (28 rule) | 0 ✅ |
| V10636_OWNER_REFERENCE_RANKING.json (197) | 0 ✅ |
| V10667_RULES_PER_REGION_RAW.json (197) | 0 ✅ |
| V10667_RULES_MB/MN/MT_TARGET.md (73/60/64 rule) | 0 ✅ |
| Harness dùng FIXED registry | True ✅ |
| Public bundle: chỉ còn FIXED registry (xóa bản 35 cũ) | ✅ |

**OVERALL CLEAN = True** (giữ nguyên từ V10669).

---

## 7. Trung thực: 1 file UNVERIFIABLE (không che giấu)

`v10605_mt_from_mb_d1d3.csv` (804 dòng) **không có cột `source_region`/`target_region`** — chỉ có `selector`, `transform`, `axis`. Scanner không parse được hướng → em đánh dấu **UNVERIFIABLE** thay vì báo "clean" giả.

**Tuy nhiên rule này hợp lệ theo thiết kế (valid by construction):**
- Tên folder + file: `mt_from_mb_d1d3` = đích MT, nguồn MB, lag **D-1/D-3**.
- Mẫu `axis` trong file: `D-1` → lag≥1.
- MB→MT lag≥1 **luôn hợp lệ** (ngày trước đã biết).

→ Không phải bug, nhưng em ghi rõ là "không verify được bằng cột region" để anh nắm chính xác mức độ kiểm tra.

---

## 8. Phương pháp (để anh / AI tool tin được)

1. **Quét DB trực tiếp**: đọc bảng `mined_rules` LIVE, không qua trung gian.
2. **Đọc code máy sinh rule**: `_seed_rules.py` `src_cfgs()` — xác nhận từng cặp (nguồn, lag) theo từng target.
3. **Parse từng file CSV**: tách `source_region`, `target_region`, `lag/axis`; áp luật `order[src] > order[tgt] AND lag==0 → violation`.
4. **Đếm chứng cứ**: với mỗi research mine, đếm `cross_region_rows` + `lag0_rows` để chứng minh scanner thực sự đọc được data (không clean giả).
5. **Guard FALSE-CLEAN**: file nào không parse được cột region → đánh dấu `UNVERIFIABLE`, không tính là clean.
6. **Đối chiếu lại V10669** + public bundle.

Script tái lập: `artifacts/v105_55_safe_quality/v10636_mb_db_d1_to_mnmt_d_audit/scripts/_verify_all_artifacts_temporal.py`
Dữ liệu máy đọc: `machine_readable/V10672_ALL_ARTIFACTS_TEMPORAL_VERIFY.json`

---

## 9. Safety

| Check | Status |
|---|---|
| official_mutation | 0 (READ-ONLY) |
| mined_rules mutation | 0 (chỉ SELECT) |
| Đây là verification, không phải data change | ✓ |
| Production LIVE rule | ✅ verified SẠCH |

---

## 10. Kết luận cho anh

Em đã verify **TOÀN BỘ** đúng như anh dặn — không bỏ sót, không dựa trí nhớ:

1. ✅ **Production đang chạy LIVE hoàn toàn sạch** — 105 rule + máy sinh rule `_seed_rules` đúng nguyên tắc temporal từ gốc (MN chỉ lag≥1; MT lấy MN(D); MB lấy MN(D)+MT(D)).
2. ✅ **Pre-register (63 rule) + production lane (105 rule)** sạch.
3. ✅ **~286,000 rule trong 11 research mine** sạch; trong đó **234,040 dòng cross-region thực sự kiểm, lag0 = 0 tuyệt đối**.
4. ✅ Bug temporal **chỉ ở V10636-CROSS** (grid thử nghiệm của em) — đã loại 266 cell, annotate, deprecate registry cũ, harness dùng FIXED. **Không lan đi đâu.**
5. ✅ 3 lỗi đã phát hiện (temporal, #bộ, nguồn nhiều đài) đều đã fix và **không lan** sang nơi khác.
6. ✅ Trung thực đánh dấu 1 file UNVERIFIABLE (V10605) — hợp lệ theo thiết kế nhưng thiếu cột region.

**Một câu cho anh:** *Mọi rule đang dùng thật và mọi báo cáo rule trong hệ thống đều tuân thủ thứ tự xổ MN → MT → MB. Sai sót temporal duy nhất nằm trong một bảng thử nghiệm và đã được xử lý trọn vẹn.*

---

**STATUS**: V10672 MASTER VERIFICATION — PRODUCTION_CLEAN = True · PREREG_CLEAN = True · RESEARCH_CLEAN = True (234k cross-region rows, lag0=0) · 1 UNVERIFIABLE (valid by design).
