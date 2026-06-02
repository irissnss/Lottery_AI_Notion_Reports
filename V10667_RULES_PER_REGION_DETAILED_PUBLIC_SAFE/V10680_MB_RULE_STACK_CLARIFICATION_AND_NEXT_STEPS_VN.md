# V10680 — MB Rule Stack Clarification + Official/Test Lane Questions + Next Steps

> **⚠️ ĐÍNH CHÍNH 2026-06-03 01:15**: Tầng 3 (V10626 pre-register, 19 rule MB) đã được BỎ khỏi runtime — xem [V10681](V10681_DROP_TIER3_T1_T2_CROSS_VERIFY_VN.md). Cấu trúc mới là **2 tầng cross-verify** T1 + T2 (cả hai đều weekday-bound + dynamic). Các phần khác của V10680 (T1, T2, gates, /du-doan-test) vẫn còn hiệu lực.
>
> **Generated**: 2026-06-03 00:45 VN  
> **Scope**: PUBLIC-SAFE report only. **Không deploy code. Không bật VPS. Không đổi official.**  
> **Purpose**: làm rõ chức năng từng tầng, prompt AI nhận ngữ cảnh gì, MB official đang bị chặn bởi cơ chế nào, `/du-doan-test` có dùng được không, và bước tiếp theo nên làm gì.

---

## 0. Kết luận nhanh

1. **UI official đã có xiên**: `generate_final_bundle()` tạo `xien2 = top1 + top2`, `xien3 = top1 + top2 + top3` với quality gate. Vì vậy **không cần** xây xiên aggregator riêng.
2. **R3 xiên aggregator đã rollback**: file `mb_xien_aggregator.py` đã bị xoá; context pack không còn block `MB XIÊN CANDIDATE SET`. Lý do: dư, dễ double-weight, lệch ý owner.
3. **Điểm đúng cần giữ**: MB-only daily rule stack, 3 tầng, window 8W, T2 cap 8, T2 mở rộng V10636-DIG/LAGS, lifecycle rule.
4. **Vấn đề thật cần xử lý tiếp**: không phải “tạo xiên”, mà là **tăng số rule mạnh đưa tín hiệu vào model/ranked top-N** để xiên official hiện có tốt hơn.
5. **Chưa deploy code**: mọi thứ đang ở local verified; báo cáo này chỉ để AI tools đọc và phân tích.

---

## 1. Chức năng từng tầng là gì?

| Tầng | ID | Nguồn | Số rule MB-target | Chức năng đúng | Có drive score không? |
|---|---|---|---:|---|---|
| **Tầng 1** | `MB-T1-DYN8W` | Production `mined_rules` lọc `target_region='MB'` | **35** | Xương sống runtime. Re-rank hằng ngày theo MB 8W; đưa vào `rule_engine` để boost các số trong model outputs. | **Có** |
| **Tầng 2** | `MB-T2-SOI` | Manual MB-target rules: V10667 + V10636-DIG/LAGS sau dedup | **77** | Kho soi cầu thủ công/forensic. Dùng để **confirm**, phân tích rule mạnh/yếu, và làm nguồn ứng viên promote sau khi đo shadow. | **Chưa** (confirm-only) |
| **Tầng 3** | `MB-T3-WATCH` | V10626 pre-register lọc MB | **19** | Watch-list dài hạn. Theo dõi rule đã pre-register, không trộn vào score khi chưa đủ bằng chứng. | **Không** |

### Vì sao 3 tầng phải tách?

- **Tầng 1** là rule production đã có trong runtime; nếu đổi sai có thể ảnh hưởng dự đoán nên chỉ re-rank MB-only và có fallback.
- **Tầng 2** nhiều hơn, chứa rule owner/forensic đã soi ra; nếu cho drive ngay sẽ tăng tín hiệu nhưng cũng tăng nhiễu. Do đó trước mắt để confirm-only.
- **Tầng 3** là pre-register, nhiều rule có transform khác biệt; không hoàn toàn nằm trong Tầng 2. Verify overlap cho thấy chỉ **5/19 axis** overlap với 73/77 manual rules, nên không gộp.

---

## 2. Các con số đúng sau khi lọc MB-target

| Nhóm gốc | Tổng | MB-target thật | Ghi chú |
|---|---:|---:|---|
| 105 production rules | 105 | **35** | 5 rule/thứ × 7 thứ |
| 183 V10675 labeled research | 183 | **1** | 183 chủ yếu target MT/MN; không phải kho MB manual |
| V10667 MB manual rules | 73 | **73** | mỗi thứ có 8–12 rule |
| V10636-DIG/LAGS bổ sung unique | — | **+4** | sau dedup T2 thành **77** |
| 63 V10626 pre-register | 63 | **19** | watch-list |

### Coverage Tầng 2 theo thứ

| Thứ | Rule manual V10667 | Sau merge DIG/LAGS | Đủ tối thiểu 3 rule? |
|---|---:|---:|---|
| T2 | 12 | ≥12 | Có |
| T3 | 11 | ≥11 | Có |
| T4 | 12 | 14 | Có |
| T5 | 12 | ≥12 | Có |
| T6 | 10 | ≥10 | Có |
| T7 | 8 | ≥8 | Có |
| CN | 8 | ≥8 | Có |

Trước đó AI chỉ thấy ít vì context pack cap `top 4`; đã nâng display cap lên **8**.

---

## 3. AI prompt nhận ngữ cảnh gì?

Prompt MB hiện được thêm một section MB-only trong `build_context_pack()`:

### 3.1 Tầng 1 — LIVE

Hiển thị 5–6 rule MB production đã re-rank 8W:

```text
TẦNG 1 — LIVE (MB-T1-DYN8W, snapshot YYYY-MM-DD, xếp hạng 8W + vòng đời):
  #5 MB:Quảng Ninh:D-1 [G6+G7] comp=87 [mạnh] hr8=88% hr12=83% hr16=87%
  #11 MN:Vũng Tàu:D-1 [G5+G7] comp=81 [tăng↑] hr8=88% hr12=67% hr16=67%
```

AI hiểu:
- rule nào đang **mạnh**
- rule nào đang **tăng**
- rule nào đang **giảm/yếu**
- window 8W/12W/16W có đồng thuận không

### 3.2 Tầng 2 — CONFIRM

Hiển thị tối đa 8 rule thủ công mạnh của đúng thứ:

```text
TẦNG 2 — CONFIRM (MB-T2-SOI, soi cầu thủ công MB-target; CONFIRM-only):
  Coverage thứ này: 14 rule [V10667=12, V10636-DIG=2]
  • MB:G7#4:D-1 [LAST2] lift=7.2pp hr=30.98% ⭐BH [mạnh] (V10667)
  • MB:G6#2:D-1 [LAST2_REV] lift=5.66pp hr=29.45% [ổn định] (V10667)
```

AI dùng Tầng 2 để:
- củng cố nếu trùng hướng với Tầng 1/model vote
- giải thích vì sao một số đáng tin hơn
- không tự cộng trùng vào score

### 3.3 Tầng 3 — WATCH

Hiển thị summary 19 pre-register:

```text
TẦNG 3 — WATCH (MB-T3-WATCH, pre-register): 19 rule MB [mạnh=17, yếu=2]
```

AI dùng để biết rule nào đang nằm watch-list, không dùng để chốt số nếu thiếu Tầng 1/Tầng 2 đồng thuận.

### 3.4 MB Expert Doctrine

Prompt có thêm các nguyên tắc:
- MB xổ cuối: được dùng MN(D), MT(D) same-day.
- MB chỉ 1 đài/ngày: evidence mỏng hơn MN/MT → trần confidence thấp hơn.
- MB ưu tiên window 8W, dùng 12W/16W để xác nhận độ bền.
- Không double-weight: runtime đã tính Tầng 1 vào score.

---

## 4. Official MB đang bị “chặn” bởi cơ chế gì?

### 4.1 Final bundle gate

Trong `generate_final_bundle()`, MB có gate riêng:

```text
REGION_GATE_OVERRIDE["MB"] = { "min_bt": 12, "min_wr": 26 }
```

Ý nghĩa:
- Nếu model có đủ lịch sử BT (`bt_total >= 5`) mà BT-rate < 12% → bị loại khỏi voting.
- Nếu chưa đủ BT data thì fallback WR < 26% → bị loại.

Đây là **model gate**, không phải rule gate. Nó ảnh hưởng trực tiếp `ranked`, từ đó ảnh hưởng BT/lo2/xien2/xien3 official.

### 4.2 V10640/V10677 MB BT override

MB đang dùng `d_w06` chooser:

```text
OVERRIDE_CONFIG["MB"] = { enabled: True, chooser: "d_w06" }
```

Nó có thể override BT top1 official nếu chooser chọn số khác. Đây ảnh hưởng BT chính, còn xiên 2/3 vẫn dựa vào ranked và số phụ.

### 4.3 CP-66.7 / ADAPTIVE_EXPLOIT

CP-66.7 trước đây bị “kẹt” vì rows test-lane chưa settle actual result. V10677 đã backfill/settle:

| Region | ADAPTIVE_EXPLOIT_V1 |
|---|---|
| MN | 26 closed / 58% |
| MT | 25 closed / 44% |
| MB | 26 closed / **23%** |

Kết luận: CP-66.7 **không còn block về dữ liệu**, nhưng MB adaptive exploit đang yếu nhất, nên **không nên promote official**.

### 4.4 MB AI LIMIT planner

Roadmap ghi MB có nhiều model bị LIMIT/planner theo dõi. Đây có thể làm official thiếu model mạnh hoặc giữ model yếu tùy trạng thái. Cần forensic riêng trước khi đụng.

---

## 5. Đưa lên `/du-doan-test` có ổn không?

Có thể dùng `/du-doan-test` để kiểm tra MB an toàn hơn official.

### Vì sao an toàn?

`_du_doan_test_mb_engine.py` có hard contract:

```text
- Does NOT call generate_final_bundle().
- Does NOT write final_bundles.
- Does NOT write production predictions.
- Writes only du_doan_test_* tables.
- Test output is admin/dev preview only, never official.
```

Vì vậy `/du-doan-test` phù hợp để:
- thử T2/T3 có nên drive không
- thử promote subset rule mà không chạm official
- đo false promotion / would-break-official

### Nhưng cần lưu ý

`/du-doan-test` MB hiện lấy từ `experimental_preview_shadow`, không tự động thay thế official. Nếu muốn test rule stack mới, nên tạo experiment rõ tên, ví dụ:

```text
MB_RULE_STACK_T2_BHPASS_SHADOW_V1
MB_RULE_STACK_T2_MULT_030_SHADOW_V1
```

và ghi riêng vào `du_doan_test_*`, không chạm `predictions`/`final_bundles`.

---

## 6. Việc chưa rõ / chưa hoàn thiện

| Vấn đề | Hiện trạng | Rủi ro nếu làm vội |
|---|---|---|
| Tier 2 đang confirm-only | 77 rule mạnh nhưng không drive score | Nếu bật hết có thể nhiễu |
| Tier 2 trend | STATIC từ report, chưa rolling theo ngày | AI chưa biết rule thủ công đang tăng/giảm thật |
| MB official gate | min_bt=12/min_wr=26 + d_w06 override | Có thể loại model hữu ích hoặc giữ model yếu |
| MB CP-66.7 | dữ liệu đã unblock nhưng MB chỉ 23% | Không nên promote adaptive exploit official |
| `/du-doan-test` | an toàn nhưng cần experiment riêng | Nếu không đặt tên rõ sẽ khó audit |

---

## 7. Đề xuất bước tiếp theo — không deploy code official

### Bước 1 — Report-only/public docs

Đã làm báo cáo này để AI tools đọc. Không deploy code.

### Bước 2 — Làm rõ bằng shadow/test lane, chưa official

Tạo kế hoạch test-lane cho 3 phương án:

| Option | Test-lane experiment | Mục tiêu |
|---|---|---|
| **A** | `MB_RULE_STACK_T2_BHPASS_SHADOW_V1` | chỉ thử 5 BH-pass T2 drive nhẹ |
| **B** | `MB_RULE_STACK_T2_TOP_PER_WEEKDAY_SHADOW_V1` | mỗi thứ lấy top 3–5 T2 rule mạnh nhất |
| **C** | `MB_RULE_STACK_T2_MULT_030_SHADOW_V1` | toàn bộ T2 drive với multiplier nhỏ 0.30 |

Chỉ viết vào `du_doan_test_*`, không chạm official.

### Bước 3 — Rolling re-measure Tier 2

Trước khi promote official, cần đo lại 77 manual rules theo thời gian:

- daily/weekly hit
- recent 4W/8W
- split-half trend
- recent decay
- confidence theo sample

Sau đó T2 mới có lifecycle thật giống T1.

### Bước 4 — Forensic MB official gates

Audit MB official:

- model nào bị gate bởi `bt<12`
- model nào bị gate bởi `wr<26`
- model nào bị LIMIT planner
- nếu đưa sang `/du-doan-test`, có cứu được xiên/lo2 không

### Bước 5 — Owner quyết định

Chỉ sau khi có test-lane + rolling T2:

- promote subset T2?
- giảm/tăng MB gate?
- giữ d_w06 hay rollback?
- bật official hay tiếp tục test?

---

## 8. Trạng thái cuối cùng

| Hạng mục | Status |
|---|---|
| Code deploy VPS | **NO** |
| Official mutation | **NO** |
| Public report | **YES** |
| Xiên aggregator riêng | **ROLLBACK / REMOVED** |
| 3 tầng rule stack | **LOCAL VERIFIED, chưa deploy** |
| `/du-doan-test` | **Đề xuất dùng cho shadow experiment** |
| Next action | Owner/AI tools đọc report, quyết định test-lane plan |

---

**Bottom line**: Không xây xiên mới. Hãy dùng xiên official/test-lane hiện có, nhưng tăng chất lượng tín hiệu đầu vào bằng rule stack MB, trước hết ở shadow/test lane.
