# V106.38-R8B — PHASE 0 CHUẨN HÓA + BẢN ĐỒ PHỤ THUỘC (PUBLIC-SAFE)

> Public-safe. Không code riêng, dòng DB thô, API key, IP/đường dẫn server.
> Không claim *_FIXED / PROMOTED. Read-only. 0 thay đổi production. AI vẫn chạy.

- **Auditor**: Opus 4.7 | 2026-05-29
- **Tham chiếu cha**: `V106_38R8_TOTAL_TRUTH_STANDARDIZATION_FLOW_PUBLIC_SAFE/V10638R8_OWNER_REPORT_VN_PUBLIC.md` (tổng hợp 6 nhóm vấn đề + trần khả thi + tách 3 luồng).
- **Nội dung gói này**: bước đầu tiên (Phase 0) của kế hoạch chuẩn hóa nhất quán toàn root.

---

## 0. KẾ HOẠCH 6 PHASE (tham chiếu)

| Phase | Việc | Rủi ro | Chạm production |
|---|---|---|---|
| **0** (gói này) | Data Dictionary đề xuất + bản đồ 163 bảng + bản đồ phụ thuộc + lint đọc | 0 | Không |
| 1 | VIEW canonical (đọc) | ~0 | Chờ duyệt |
| 2 | Chuẩn điểm ghi + giữ cột cũ alias | thấp | Chờ duyệt |
| 3 | Xóa bảng chết an toàn + gộp cặp trùng thật | trung | Chờ duyệt + backup |
| 4 | Dọn file sprawl | thấp | Chờ duyệt |
| 5 | Governance hook chống tái loạn | 0 | Không |

---

## 1. PHASE 0 ĐÃ LÀM GÌ (read-only)

1. **Data Dictionary đề xuất v0.1** — 1 tên/khái niệm (`date`, `region`, `ai_model`, `weekday`, `station`, `bach_thu`, `lo2`, `status`, `bt_hit`+`hit_count`, `strength`, `run_source`...) + bảng alias đài 3 miền + nhãn luồng + khóa per-slice `(flow, region, station, weekday)`.
2. **Bản đồ 163 bảng** — mỗi bảng: luồng, trục per-slice, cột không chuẩn, dead, trùng-với.
3. **Bản đồ phụ thuộc** — quét 351 file source để biết file nào dùng bảng/cột nào (TRƯỚC khi gộp/xóa).
4. **Lint đọc** — báo cáo 126 lần cột không chuẩn (không sửa gì).

---

## 2. PHÁT HIỆN AN TOÀN TỪ BẢN ĐỒ PHỤ THUỘC (chống làm hỏng hệ thống)

### 2.1. "Chết theo dòng" ≠ "chết theo code"
- 9 bảng có 0 dòng, nhưng **chỉ 1 bảng (`rule_features`) thật sự không có code tham chiếu** → an toàn xóa (sau backup).
- 8 bảng còn lại tuy trống nhưng code vẫn dùng (bảng chờ ghi) → **KHÔNG xóa** (xóa sẽ hỏng script).

### 2.2. 6 cặp bảng "trùng" → thực ra chỉ 4 cặp đáng gộp
- 4 cặp là trùng thật (chọn canonical theo số ref + số dòng), gộp SAU khi verify nội dung giống 100%.
- **2 cặp giống schema nhưng KHÁC chức năng** (vd partial-vs-win; digit_transform-vs-exact_position) → **giữ cả hai, KHÔNG gộp** (gộp sẽ làm sai nghĩa).

### 2.3. Đổi tên cột → CỰC rủi ro → dùng VIEW, không rename vật lý
- `target_region` được dùng ở **153 file**; `target_date` ở 73 file; `model_id` 32; `model_name` 25...
- Rename vật lý sẽ chạm 100-153 file → dễ vỡ. **Bắt buộc dùng tầng VIEW canonical**: code mới đọc tên chuẩn, code cũ giữ cột gốc → **0 breakage**.

---

## 3. NGUYÊN TẮC "1 TÊN DUY NHẤT ĐI TIẾP" (theo yêu cầu chủ hệ thống)
- Code MỚI: chỉ dùng tên canonical qua VIEW.
- Code CŨ: giữ nguyên, refactor dần từng file (không vội, không phá).
- Bảng MỚI: bắt buộc theo Data Dictionary + nhãn `flow` + đủ trục per-slice.
- Lint chặn tên mới không chuẩn (Phase 5) → chống "sinh sôi nảy nở".

---

## 4. AN TOÀN
- Phase 0 = tài liệu + đọc → không thể làm sập hệ thống đang chạy.
- 0 production mutation; chỉ ghi vùng báo cáo; AI vẫn chạy tới 2026-06-03.
- Mọi đổi production (Phase 2+) chỉ áp khi chủ hệ thống duyệt + backup.
- Chuẩn hóa chỉ đổi TÊN, không đổi SỐ/giá trị.

---

## 5. FILE TRONG GÓI (tham chiếu)
- `DATA_DICTIONARY_PROPOSED_v0.1.md` — chuẩn đề xuất.
- `P0_TABLE_INVENTORY_MAP.md` — bản đồ 163 bảng.
- `P0_DEPENDENCY_AWARE_ACTION_PLAN.md` — kế hoạch gộp/xóa dựa phụ thuộc.
- `machine_readable/V10638R8B_PHASE0_SUMMARY.json` — tóm tắt máy đọc.

---

**Cần chủ hệ thống duyệt**: (1) bảng tên cột canonical, (2) bảng alias đài, (3) danh sách gộp/xóa an toàn (chỉ xóa `rule_features`, gộp 4 cặp sau verify). Duyệt xong → promote Data Dictionary sang `docs/` + làm Phase 1 (VIEW, rủi ro ~0).
