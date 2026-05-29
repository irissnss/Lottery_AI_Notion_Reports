# DATA DICTIONARY — ĐỀ XUẤT v0.1 (PHASE 0)

> TRẠNG THÁI: **ĐỀ XUẤT — chờ chủ hệ thống duyệt. CHƯA enforce. CHƯA đổi production.**
> Phase 0 chỉ là tài liệu + bản đồ + lint đọc. 0 thay đổi runtime/DB.
> Khi anh duyệt tên canonical → mới promote sang `docs/` và làm Phase 1 (VIEW).

- Auditor: Opus 4.7 | 2026-05-29
- Phạm vi: 163 bảng `lottery_ai.db` + tên đài + nhãn luồng.

---

## 1. TÊN CỘT CANONICAL (1 tên / khái niệm)

| Khái niệm | Tên CHUẨN đề xuất | Kiểu | Các tên ĐANG dùng (gộp về chuẩn) |
|---|---|---|---|
| Ngày | `date` | TEXT 'YYYY-MM-DD' (VN) | date · target_date · run_date · prediction_date · eval_date |
| Miền | `region` | TEXT (MN/MT/MB) | region · target_region |
| Miền nguồn (cross-region) | `source_region` | TEXT | (giữ riêng — KHÁC nghĩa) |
| Model | `ai_model` | TEXT | ai_model · model_name · model_id · model |
| Thứ | `weekday` | INT 0-6 (Mon=0); 'tất cả' = `-1` | weekday · day_of_week · target_weekday (bỏ 'ALL') |
| Đài | `station` | TEXT canonical | station · station_id (station_set giữ riêng nếu là tập đài) |
| Đài nguồn (cross-region) | `source_station` | TEXT | (giữ riêng) |
| Bạch thủ | `bach_thu` | TEXT 2 chữ số | bach_thu · bt_number · (main_numbers = mảng, giữ riêng) |
| Lô 2 | `lo2` | TEXT(JSON) | lo2 |
| Trạng thái | `status` | TEXT WIN/LOSE/PARTIAL | status (+ bach_thu_status / lo2_status cho bundle) |
| Hit (nhị phân) | `bt_hit` | INT 0/1 | bt_hit · hit_any · is_hit |
| Số lần trúng (nháy) | `hit_count` | INT | hit_count · tails_hit |
| Độ mạnh | `strength` | REAL 0-10 | strength · score · top_score · confidence · strength_score |
| Nguồn chạy | `run_source` | TEXT enum | run_source · source · phase_type |
| Verdict | `verdict` (+ `verdict_reason`) | TEXT | verdict · decision |
| Tạo / sửa | `created_at` / `updated_at` | TEXT ISO | created_at · updated_at · mined_at · timestamp |

**Quy tắc kiểu (chống clash ngầm)**: không trộn số + chữ trong 1 cột (vd `day_of_week` không được vừa INT vừa 'ALL'); sentinel "tất cả" dùng `-1`.

---

## 2. NHÃN LUỒNG (FLOW) — TÁCH 3 LUỒNG

| flow | Quy ước tên | Số bảng hiện tại |
|---|---|---|
| `official` | tên trần (predictions, final_bundles, lottery_results, model_daily_eval, mined_rules...) | 10 |
| `lane` | tiền tố `du_doan_test_` | 21 |
| `shadow` | hậu tố `_shadow` (+ experimental_preview / replay) | 62 |
| `measurement` | hậu tố `_daily` / `_audit` | 39 |
| `(chưa rõ)` | 31 bảng mơ hồ → cần gắn nhãn | 31 |

**Đề xuất**: thêm cột/quy ước `flow` minh bạch cho mọi bảng; 31 bảng mơ hồ phải được phân loại. official / lane / shadow độc lập hoàn toàn, kể cả prompt thử nghiệm shadow.

---

## 3. KHÓA PER-SLICE (độc lập miền × thứ × đài)

- Khóa chuẩn cho mọi rule/prompt/weight/eval: **`(flow, region, station_canonical, weekday)`**.
- Đài chạy nhiều thứ = nhiều ô riêng (vd Hà Nội-T2 ≠ Hà Nội-T5; HCM-T2 ≠ HCM-T7).
- Hiện chỉ ~24/163 bảng có đủ trục region+weekday+station → cần bổ sung dần (Phase 1+).

---

## 4. BẢNG ALIAS ĐÀI CANONICAL

### MN
| Canonical | Alias gộp | Thứ chạy |
|---|---|---|
| HCM | HCM, TP. HCM | T2, T7 |
| (21 đài khác giữ nguyên tên) | — | theo lịch |

### MT (loạn nhất — 3 cặp trùng)
| Canonical | Alias gộp | Thứ chạy |
|---|---|---|
| Thừa Thiên Huế | Huế, Thừa Thiên Huế | T2, CN |
| Đắk Lắk | Đắc Lắc, Đắk Lắk | T3 |
| Đắk Nông | Đắc Nông, Đắk Nông | T7 |
| Đà Nẵng | Đà Nẵng | T4, T7 |
| Khánh Hòa | Khánh Hòa | T4, CN |

### MB (tên sạch, nhưng đa-thứ)
| Canonical | Thứ chạy | Ghi chú |
|---|---|---|
| Hà Nội | T2, T5 | 1 đài chạy 2 thứ |
| Quảng Ninh / Bắc Ninh / Hải Phòng / Nam Định / Thái Bình | T3/T4/T6/T7/CN | mỗi thứ 1 tỉnh |

---

## 5. DANH SÁCH XỬ LÝ (từ bản đồ 163 bảng)
- **9 bảng chết** (0 dòng) → ứng viên xóa sau backup (Phase 3).
- **6 cặp bảng trùng chức năng** → ứng viên gộp (Phase 3).
- **100 bảng có cột không chuẩn** → VIEW canonical (Phase 1) + chuẩn điểm ghi (Phase 2).

Chi tiết: `P0_TABLE_INVENTORY_MAP.csv` (mỗi bảng: flow, trục, cột không chuẩn, dead, duplicate_with).

---

## 6. ĐẢM BẢO ỔN ĐỊNH (theo yêu cầu anh)
- Phase 0 = tài liệu + đọc → **không thể làm sập hệ thống đang chạy**.
- Mọi đổi production (Phase 2+) chỉ áp khi anh duyệt + có backup.
- Chuẩn hóa chỉ đổi **TÊN**, không đổi **SỐ/giá trị**.
- AI vẫn chạy bình thường (không tắt) tới 2026-06-03.
- Không claim "đã fix" khi chưa có forward proof.

---

**Cần anh duyệt**: bảng tên cột canonical (mục 1) + bảng alias đài (mục 4). Duyệt xong em promote sang `docs/DATA_DICTIONARY.md` và làm Phase 1 (VIEW canonical, rủi ro ~0).
