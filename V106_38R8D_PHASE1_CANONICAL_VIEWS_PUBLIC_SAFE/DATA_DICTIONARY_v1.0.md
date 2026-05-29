# DATA DICTIONARY — SSOT v1.0 (chuẩn hóa nhất quán toàn hệ thống)

> Nguồn chuẩn DUY NHẤT cho tên file / bảng / cột / đài / model đi tiếp.
> Trạng thái: **v1.0 — owner đã duyệt hướng 2026-05-29** (gói A tên cột qua VIEW + gói B xóa/gộp).
> Nguyên tắc: chuẩn hóa đổi TÊN/CẤU TRÚC, KHÔNG đổi SỐ. Code mới dùng tên chuẩn (qua VIEW). Code cũ refactor dần.
> Lineage: `artifacts/.../phase0_standardization/` (inventory, dependency, verification, views).

---

## 1. TÊN CỘT CANONICAL (áp dụng qua VIEW `v_<table>`, không rename vật lý)

| Khái niệm | Tên CHUẨN | Gộp từ (alias qua VIEW) |
|---|---|---|
| Ngày | `date` | target_date, run_date |
| Miền | `region` | target_region |
| Model | `ai_model` | model_name, model_id, model |
| Thứ | `weekday` (INT 0-6, Mon=0; 'tất cả'=-1) | day_of_week, target_weekday |
| Đài | `station` | (tên canonical, xem mục 3) |
| Bạch thủ | `bach_thu` | bt_number |
| Lô 2 | `lo2` | — |
| Trạng thái | `status` (+ bach_thu_status/lo2_status) | outcome_status |
| Verdict | `verdict` (+ verdict_reason) | decision |
| Hit nhị phân | `bt_hit` (0/1) | hit_any, is_hit |
| Số lần trúng | `hit_count` | tails_hit |
| Độ mạnh | `strength` (REAL 0-10) | strength_score |

### CỐ Ý CHƯA gộp (có thể khác nghĩa — xem riêng từng bảng trước khi alias):
- `phase_type` vs `run_source` (có thể là 2 chiều khác nhau trong predictions).
- `mined_at` vs `created_at` (mined_at = thời điểm mine luật, nghĩa riêng).
- `score` / `confidence` vs `strength` (rule-score / AI-confidence ≠ model-strength).
- `main_numbers` (mảng) vs `bach_thu` (1 số) — KHÁC cấu trúc, giữ riêng.
- `source_region` / `source_station` — chiều cross-region, KHÁC `region`/`station`.

VIEW đã sinh + test PASS (read-only): `phase1_canonical_views.sql`:
`v_predictions` (target_region→region) · `v_model_daily_eval` (bt_number→bach_thu) · `v_mined_rules` (target_region→region, target_weekday→weekday) · `v_final_bundles` · `v_lottery_results`.

---

## 2. NHÃN LUỒNG (FLOW) — TÁCH 3 LUỒNG ĐỘC LẬP
- `official` = tên trần (predictions, final_bundles, lottery_results, model_daily_eval, mined_rules...).
- `lane` = tiền tố `du_doan_test_`.
- `shadow` = hậu tố `_shadow` (+ experimental_preview / replay).
- `measurement` = hậu tố `_daily` / `_audit`.
- official / lane / shadow độc lập hoàn toàn (data + prompt thử nghiệm), không trộn.

---

## 3. ĐÀI CANONICAL + KHÓA PER-SLICE (QUYẾT ĐỊNH: TÁCH theo thứ)

### Khóa chuẩn: `(flow, region, station_canonical, weekday)` — TÁCH tối đa
- 1 đài chạy nhiều thứ = nhiều ô RIÊNG (bộ model/luật/ngưỡng riêng):
  - MN: `HCM·T2` ≠ `HCM·T7`
  - MB: `Hà Nội·T2` ≠ `Hà Nội·T5`
  - MT: `Thừa Thiên Huế·T2` ≠ `Thừa Thiên Huế·CN`; `Đà Nẵng·T4` ≠ `Đà Nẵng·T7`; `Khánh Hòa·T4` ≠ `Khánh Hòa·CN`

### Tên đài THỐNG NHẤT 1 cách viết (sửa chính tả, không gộp đài):
| Canonical | Gộp từ |
|---|---|
| HCM | HCM, TP. HCM |
| Thừa Thiên Huế | Huế, Thừa Thiên Huế |
| Đắk Lắk | Đắc Lắc, Đắk Lắk |
| Đắk Nông | Đắc Nông, Đắk Nông |

### Lịch đài × thứ (verified, 2025-08 → nay):
- **MN**: T2[Cà Mau, HCM, Đồng Tháp] · T3[Bạc Liêu, Bến Tre, Vũng Tàu] · T4[Cần Thơ, Sóc Trăng, Đồng Nai] · T5[An Giang, Bình Thuận, Tây Ninh] · T6[Bình Dương, Trà Vinh, Vĩnh Long] · T7[Bình Phước, HCM, Hậu Giang, Long An] · CN[Kiên Giang, Tiền Giang, Đà Lạt]. (HCM = T2+T7, KHÔNG CN.)
- **MT**: T2[Phú Yên, Thừa Thiên Huế] · T3[Quảng Nam, Đắk Lắk] · T4[Khánh Hòa, Đà Nẵng] · T5[Bình Định, Quảng Bình, Quảng Trị] · T6[Gia Lai, Ninh Thuận] · T7[Quảng Ngãi, Đà Nẵng, Đắk Nông] · CN[Khánh Hòa, Kon Tum, Thừa Thiên Huế].
- **MB** (1 tỉnh/thứ): T2 Hà Nội · T3 Quảng Ninh · T4 Bắc Ninh · T5 Hà Nội · T6 Hải Phòng · T7 Nam Định · CN Thái Bình.

---

## 4. MODEL AI — KHÔNG GỘP TÊN; registry là SSOT
- Registry (41 model) là nguồn định danh duy nhất đi tiếp. Tên/giá trị model KHÔNG đổi.
- 28 đang chạy (9 TOKEN-output + 12 TOKEN-shadow + 7 ML local free).
- 13 đã loại/idle (status=REMOVED) + 13 orphan lịch sử (Feb-Mar) → chỉ tồn tại trong row cũ (lịch sử), KHÔNG dự đoán bằng chúng, KHÔNG xóa row.
- Key dùng chung theo provider: google(5) · openrouter(21) · deepseek(3) · anthropic(2) · openai(2) · local(7, free).

---

## 5. BẢNG — XÓA / GỘP (verified, owner duyệt; thực thi chờ backup + bấm nút)
- **Xóa**: `rule_features` (0 dòng, 0 ref).
- **Gộp (dup thật)**: `ai_region_specialist_prompt_shadow_results` → `ai_prompt_context_audit_shadow` (75 dòng giống 100%) — cần consolidate 2 materializer trước khi DROP.
- **GIỮ (không gộp)**: 2 cặp region-subset + 1 cặp version + 1 cặp khác-nghĩa + 8 bảng-trống-còn-dùng.
- SQL sẵn sàng (chưa chạy): `phase_b_drop_merge.sql`.

---

## 6. GOVERNANCE (chống "sinh sôi nảy nở")
- Bảng/cột MỚI bắt buộc theo Data Dictionary này + nhãn `flow` + đủ trục per-slice.
- Lint `check_naming.py` cảnh báo tên không chuẩn (Phase 5 → hook chặn).
- Mọi báo cáo công bố lên `Lottery_AI_Notion_Reports` (public-safe) có tham chiếu chéo.

---

**Phiên bản**: v1.0 (2026-05-29). Cập nhật khi có quyết định mới. Đây là nguồn chuẩn DUY NHẤT — tránh dùng tên/bảng/cột cũ ngoài danh sách alias ở trên.
