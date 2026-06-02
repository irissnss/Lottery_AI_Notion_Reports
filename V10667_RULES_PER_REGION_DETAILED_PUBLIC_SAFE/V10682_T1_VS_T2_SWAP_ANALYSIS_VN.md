# V10682 — Phân tích đảo T1 ↔ T2: lấy thủ công 77 lên drive, lấy production 35 xuống confirm có ổn không?

> **Generated**: 2026-06-03 01:30 VN
> **Trigger**: Owner đặt câu hỏi "đảo ngược T2 thủ công lên trước làm T1 có ổn hơn không?"
> **Trạng thái**: REPORT-ONLY. Không deploy code. Không đụng official.
> **Liên quan**: nối tiếp [V10681](V10681_DROP_TIER3_T1_T2_CROSS_VERIFY_VN.md).

---

## 0. Trả lời nhanh

| Phương án | Khuyến nghị |
|---|---|
| **A. Giữ nguyên: T1 drive, T2 CONFIRM** | ⭐ KHUYẾN NGHỊ (an toàn nhất, R4) |
| **B. Curated subset: 5 BH-pass T2 → shadow drive 30d /du-doan-test → owner OK promote** | ⭐ KHUYẾN NGHỊ ở pha sau khi anh OK |
| **C. Đảo HOÀN TOÀN T2 lên drive, T1 xuống confirm** | ❌ KHÔNG khuyến nghị |

Lý do C không ổn: phá doctrine forward audit + mất 7 lớp safety chain runtime + T2 đo 1 lần không rolling + 5 BH-pass T2 KHÔNG phủ T6/T7/CN.

---

## 1. So sánh T1 vs T2 (số liệu thực tế từ DB live)

| Chỉ số | T1 (production) | T2 (manual V10667) |
|---|---|---|
| Tổng MB-target | 35 | 73 |
| Distinct axes | 23 | 47 |
| **Overlap T1 ∩ T2** | **0 axes** (hoàn toàn bổ trợ) | |
| Sample | 365d MRE rolling, daily update | 326d, đo **1 lần** |
| Avg lift_365 | 1.171 | — |
| Avg lift_pp | — | 5.29 pp |
| Avg composite | 74.7 | — (chỉ có lift+p) |
| BH-pass FDR (gold) | composite-based | **5 rule** |
| p<0.01 (STRONG) | — | 12 rule |
| p<0.05 | — | 72 rule |
| Per-thứ rule | 5 rule × 7 thứ = 35 | 8-12 rule × 7 thứ = 73 |
| Per-thứ BH-pass | n/a | T2:1, T3:1, T4:1, T5:2, **T6:0, T7:0, CN:0** |
| Activation | active=32, shadow=3 | live_eligible=False all |
| Forward audit V10668 | n/a | **0 MB-target rule** đăng ký |

### Phát hiện cốt lõi: **T1 ∩ T2 = 0 overlap**

Hai bên dùng **axes hoàn toàn khác nhau** (source × prize × lag). Nghĩa là:
- T1 không chồng lên T2 và ngược lại.
- Cả hai cùng cung cấp tín hiệu **bổ sung**, không cạnh tranh.
- Đây là tin tốt: **không phải chọn 1 trong 2**, mà có thể KẾT HỢP nếu có cơ chế đúng.

---

## 2. Tại sao đảo HOÀN TOÀN T2 → T1 không ổn?

### 2.1 T2 đo MỘT LẦN, không rolling

T1 có `mined_rule_effectiveness` cập nhật mỗi ngày → có hr_4w/8w/12w/16w động, có lifecycle thật.

T2 sample là số ghi tại thời điểm V10667 đào (~2026-06-02). KHÔNG có rolling re-measure. Sau 1 tháng có thể rule đã decay nhưng AI vẫn thấy lift cũ → ra quyết định sai.

### 2.2 Mất 7 lớp safety chain runtime

T1 chạy qua `rule_engine.extract_rule_candidates_v2('MB')` được bảo vệ bởi:

1. **DH multiplier (V19)**: hit_level history quality weighting (0.85x-1.30x)
2. **Livingness 12W check (V17.5.1)**: rule chết → suppress 0.7×; rule sống → amplify 1.15×
3. **16W stability spike-risk (V20)**: 12W mạnh nhưng 16W yếu = spike risk → 0.80×
4. **Lift-based scale**: lift cao thưởng nhẹ
5. **Convergence bonus + anti-herding cap**: nhiều rule cùng tail → bonus có cap (0.10/0.20/0.30 tuỳ convergence)
6. **Bucket suppress threshold**: bucket yếu → fallback chỉ READY_STRONG
7. **Station alias lookup**: source station đổi tên → vẫn map đúng

T2 nếu drive: hiện CHỈ có composite + lifecycle. **Cần tái tạo 7 lớp trên hoặc bypass** → bypass = nguy hiểm.

### 2.3 Phá doctrine forward audit owner đã đặt

V10668 forward audit registry: 28 rule đăng ký, anchor 2026-06-02, **closeout 2026-08-31** (90 ngày). Trong đó **0 rule MB-target** đã đăng ký chính thức.

5 BH-pass T2 MB-target chỉ ở dạng `PRE_REGISTER_FORWARD_AUDIT` trong V10667/V10668 — chưa qua closeout.

Promote drive trước closeout = phá doctrine `live_eligible=False until forward audit pass`.

### 2.4 5 BH-pass MB-target KHÔNG phủ đủ 7 thứ

| Thứ | T2 BH-pass MB | Đánh giá |
|---|---:|---|
| T2 | 1 | đủ tối thiểu |
| T3 | 1 | đủ tối thiểu |
| T4 | 1 | đủ tối thiểu |
| T5 | 2 | đủ |
| **T6** | **0** | ⚠️ thiếu |
| **T7** | **0** | ⚠️ thiếu |
| **CN** | **0** | ⚠️ thiếu |

→ Đảo hoàn toàn = thứ 6/7/CN không có rule BH-pass nào dẫn dắt → bỏ ngỏ tín hiệu.

### 2.5 Mất cơ chế weekly mining tự update

Nếu T2 thay T1 hoàn toàn: weekly miner (`_seed_rules` mỗi T2 00:30) vẫn chạy nhưng output không được consume → lãng phí + mất tự động học từ MRE.

---

## 3. Tại sao GIỮ NGUYÊN (Phương án A) vẫn tốt?

| Yếu tố | T1 | T2 đóng góp gì |
|---|---|---|
| Drive score | T1 35 rule × safety chain | T2 không double-weight (CONFIRM) |
| Per-thứ coverage | 5 rule mọi thứ | 8-12 rule MB-target mọi thứ |
| BH-pass gold | composite-based | 5 BH-pass nổi bật trong context |
| Owner soi cầu thủ công | n/a | T2 đại diện owner rules cho AI giải thích |
| Cross-verify | T1 chạy độc lập | T2 confirm khi đồng thuận |
| Forward audit | n/a | T2 chờ closeout 31/08 |

→ Mỗi tầng đúng vai trò. Đảo ngược không cải thiện gì mà mất nhiều.

---

## 4. Phương án B (Curated subset, KHUYẾN NGHỊ pha sau)

### 4.1 5 rule BH-pass MB-target ứng viên

Sau khi anh OK, em đề xuất shadow promote 5 BH-pass MB-target lên `/du-doan-test`:

| # | Lineage | Thứ | Lift pp | Hit% | p-value |
|---|---|---|---:|---:|---:|
| 1 | `MN:DB#1:D` | T2 | 8.43 | 63.19 | 0.00134 |
| 2 | (cần re-extract từ V10667 để lấy đầy đủ 5 rule) | T3-T5 | — | — | — |

Em cần chạy script verify 5 BH-pass cụ thể trước khi đề xuất vào shadow.

### 4.2 Cơ chế shadow drive (đề xuất)

```
experiment_name: MB_RULE_STACK_T2_BHPASS_SHADOW_V1
- Ghi vào du_doan_test_* (KHÔNG đụng final_bundles/predictions)
- 5 rule BH-pass T2 drive với multiplier nhỏ 0.30 × T1 boost
- Đo 30 ngày false_promotion + would_break_official
- Sau 30d nếu Δ pp ≥ +5 pp + n_lose ≥ 30 → owner cân nhắc promote
```

### 4.3 Vẫn phải qua forward audit

Theo doctrine V10626: chỉ promote khi forward audit closeout (31/08/2026) PASS. Trước đó chỉ test-lane.

---

## 5. Verify đã làm cho V10681 + V10682

| Mục | Kết quả |
|---|---|
| py_compile 5 file backend | PASS |
| ReadLints | 0 errors |
| Harness MN/MT 108 chữ ký | **108/108 IDENTICAL** |
| Full verify suite | **54/54 PASS, 0 FAIL** |
| Smoke MB context pack | T1 5 rule + T2 8 rule + cross-verify; KHÔNG còn T3 |
| Ranker run | tier3_count=0, T3=DROPPED_V10681 |
| CHANGELOG / SSOT / FU_TRACKER | Đã sync V10681 |
| Public V10681 + LATEST_REPORT | Đã push GitHub commit `9091c3b` |

---

## 6. Câu hỏi anh đặt ra & câu trả lời ngắn

| Câu hỏi | Trả lời |
|---|---|
| "Đảo T2 ↔ T1 ổn hơn không?" | KHÔNG đảo hoàn toàn (mất safety chain, phá forward audit, T6/T7/CN trống BH-pass). Có thể curated subset BH-pass qua shadow. |
| "Em verify, kiểm tra kiểm soát kỹ chưa?" | Có: harness MN/MT 108/108, full verify 54/54, đã đếm + so sánh thực tế DB. |
| "Báo cáo deploy hết chưa?" | V10681 đã push GitHub `9091c3b`. V10682 (file này) sẽ push sau khi anh đọc xong. Local CHANGELOG/SSOT/FU_TRACKER đã sync V10681. |

---

## 7. Đề xuất bước tiếp theo

1. Anh đọc V10682, quyết định: A (giữ nguyên) / B (curated 5 BH-pass shadow 30d) / C (đảo hoàn toàn — KHÔNG khuyến nghị).
2. Nếu B: em viết script verify 5 BH-pass MB-target (lineage + thứ + p-value đầy đủ) → đề xuất `MB_RULE_STACK_T2_BHPASS_SHADOW_V1` experiment trong `du_doan_test_*` (KHÔNG đụng official).
3. Đồng thời em viết job rolling re-measure 73 manual T2 hàng tuần (T2 trend STATIC → DYNAMIC) — đây là pre-requisite trước khi cân nhắc bất kỳ promote nào.
4. Forensic MB official gates (`min_bt=12`, `min_wr=26`, d_w06 override, MB AI LIMIT planner).
5. Sau 30d shadow + forward audit closeout (31/08) → owner OK promote vào official nếu data tốt.

---

## 8. Trạng thái

| Hạng mục | Status |
|---|---|
| Code deploy VPS | NO |
| Official mutation | NO |
| Public report V10681 | PUSHED (`9091c3b`) |
| Public report V10682 | sắp push |
| Internal governance V10681 | SYNCED (CHANGELOG + SSOT + FU_TRACKER) |
| MN/MT bất biến | PROVEN 108/108 |
| Full verify | 54/54 PASS |
| Owner decision T1↔T2 | AWAITING |

**Bottom line**: Cấu trúc T1 drive + T2 CONFIRM hiện tại là phương án **ổn nhất** dựa trên dữ liệu thực. Đảo hoàn toàn KHÔNG khuyến nghị. Nếu muốn tăng tín hiệu — dùng curated 5 BH-pass T2 qua shadow `/du-doan-test`, không đảo cấu trúc tổng.
