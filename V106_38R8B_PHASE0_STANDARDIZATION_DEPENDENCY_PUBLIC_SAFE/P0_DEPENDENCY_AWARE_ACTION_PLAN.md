# PHASE 0 — KẾ HOẠCH GỘP/TÁCH/XÓA DỰA TRÊN PHỤ THUỘC (an toàn, không làm hỏng)

> Owner: gộp/tách/xóa OK nhưng phải tư duy liên kết kỹ, tránh làm hỏng hệ thống.
> Báo cáo này dựa trên quét **351 file source** (web/backend + web/frontend) — read-only.
> Nguồn: `P0_DEPENDENCY_MAP.json` + `P0_TABLE_INVENTORY_MAP.json`.

---

## 1. BÀI HỌC LỚN: "CHẾT THEO DÒNG" ≠ "CHẾT THEO CODE"

9 bảng có 0 dòng, NHƯNG khi quét code:

| Bảng chết (0 dòng) | Số file code dùng | Phán quyết |
|---|---|---|
| `rule_features` | **0** | ✅ AN TOÀN XÓA (sau backup) |
| bundle_replay_compare_daily | 2 | ❌ GIỮ (code đang ghi/đọc) |
| data_preservation_manifest_daily | 2 | ❌ GIỮ |
| du_doan_test_ai_predictions | 2 | ❌ GIỮ |
| du_doan_test_latency_daily | 1 | ❌ GIỮ |
| rule_effectiveness | 1 | ❌ GIỮ |
| sync_parity_audit_daily | 2 | ❌ GIỮ |
| training_records | 1 | ❌ GIỮ |
| v10522_v102_strong_selector_shadow | 1 | ❌ GIỮ |

→ **Chỉ XÓA `rule_features`.** 8 bảng còn lại tuy 0 dòng nhưng code vẫn tham chiếu (bảng trống chờ ghi) → xóa sẽ làm hỏng script. Đây chính xác là rủi ro anh cảnh báo.

---

## 2. 6 CẶP BẢNG TRÙNG — CANONICAL THEO REF + ROWS (verify trước khi gộp)

| Cặp | Giữ (canonical) | Gộp từ | Lý do | Cảnh báo |
|---|---|---|---|---|
| experimental_preview_shadow ↔ mb_experimental_preview_shadow | **experimental_preview_shadow** (22 ref) | mb_... (5 ref) | nhiều ref hơn | verify MB có phải subset |
| v101_region_source_pool_shadow ↔ v101_mn_cross_region_rule_shadow | **v101_region_source_pool_shadow** (10 ref, 10170 dòng) | v101_mn_... (7 ref) | nhiều ref+rows | verify semantic |
| tier2_replay_v2_shadow ↔ tier2_replay_shadow | **tier2_replay_v2_shadow** (558 dòng) | v1 (192 dòng) | v2 mới hơn | v1 có thể là lịch sử |
| ai_prompt_context_audit_shadow ↔ ai_region_specialist_prompt_shadow_results | **ai_prompt_context_audit_shadow** | còn lại | ref ngang, schema 100% | verify nội dung |
| pre_partial_post_lose_daily ↔ pre_win_post_lose_daily | **GIỮ CẢ HAI** | — | schema giống NHƯNG nghĩa KHÁC (partial vs win) | ⚠️ KHÔNG gộp — khác chức năng |
| digit_transform_source_rule_shadow_v10610 ↔ exact_position_source_rule_shadow_v10610 | **GIỮ CẢ HAI** | — | 0 ref code, schema giống nhưng 9211 vs 240 dòng | ⚠️ KHÔNG gộp — khác loại rule |

→ **Quan trọng**: 2 cặp cuối "giống schema nhưng KHÁC chức năng" (partial vs win; digit_transform vs exact_position). **Tuyệt đối không gộp** — sẽ làm hỏng nghĩa. Đây là điểm "tương ứng/tương thích" anh dặn phải xem kỹ. → Thực tế chỉ **4 cặp** đáng gộp (sau verify), không phải 6.

---

## 3. ĐỔI TÊN CỘT — RỦI RO CỰC CAO → DÙNG VIEW, KHÔNG RENAME VẬT LÝ

Số file dùng mỗi cột không chuẩn:

| Cột | Số file dùng | Rename vật lý? |
|---|---|---|
| `target_region` | **153 file** | ❌ KHÔNG (quá rủi ro) → VIEW |
| `target_date` | **73 file** | ❌ KHÔNG → VIEW |
| `model_id` | 32 | ❌ KHÔNG → VIEW |
| `model_name` | 25 | ❌ KHÔNG → VIEW |
| `day_of_week` | 23 | ❌ KHÔNG → VIEW |
| `run_date` | 18 | ❌ KHÔNG → VIEW |
| `target_weekday` | 13 | ❌ KHÔNG → VIEW |
| `bt_number` / `strength_score` | 10 mỗi | VIEW |
| `phase_type` | 6 | VIEW |

→ **KẾT LUẬN AN TOÀN**: rename cột vật lý chạm 100-153 file → CỰC kỳ dễ hỏng. **Bắt buộc dùng tầng VIEW canonical (Phase 1)**: code MỚI đọc view tên chuẩn (`region`, `date`, `ai_model`...), code CŨ giữ nguyên cột gốc → **0 breakage**. Đây là cách "1 tên duy nhất đi tiếp" mà không đập vỡ 153 file.

---

## 4. HÀNH ĐỘNG AN TOÀN ĐÃ XÁC ĐỊNH (dependency-aware)

| # | Hành động | An toàn? | Điều kiện |
|---|---|---|---|
| 1 | Xóa `rule_features` | ✅ | sau backup (0 ref) |
| 2 | Gộp 4 cặp bảng trùng thật | ⚠️ có điều kiện | verify nội dung giống 100% + cập nhật ref ở các file dùng bảng "merge_from" |
| 3 | KHÔNG gộp 2 cặp khác-nghĩa | ✅ | giữ cả hai, chỉ document rõ |
| 4 | Tên cột → VIEW canonical | ✅ | Phase 1, không rename vật lý |
| 5 | Bổ sung trục (thứ, đài) cho bảng thiếu | ⚠️ | thêm cột mới (không phá cột cũ) |

---

## 5. NGUYÊN TẮC "1 TÊN DUY NHẤT ĐI TIẾP" (theo yêu cầu anh)
- Code MỚI: chỉ dùng tên canonical qua VIEW (`region`, `date`, `ai_model`, `weekday`, `station`, `bach_thu`, `strength`...).
- Code CŨ: giữ nguyên cho tới khi rảnh refactor từng file (không vội, không phá).
- Bảng MỚI: bắt buộc theo Data Dictionary + có nhãn `flow` + đủ trục per-slice.
- Lint `check_naming.py` (Phase 5) chặn tên mới không chuẩn → chống "sinh sôi nảy nở".

---

## 6. CẬP NHẬT TÀI LIỆU (sau khi anh duyệt)
- Promote `DATA_DICTIONARY_PROPOSED_v0.1.md` → `docs/DATA_DICTIONARY.md` (SSOT chuẩn).
- Ghi bảng map 163 bảng + dependency vào docs để sau này chỉ tra 1 nguồn.
- Mọi báo cáo đẩy lên `Lottery_AI_Notion_Reports` có tham chiếu chéo rõ ràng.

---

**Bottom line**: Nhờ quét phụ thuộc, em đã chặn được rủi ro: chỉ 1 bảng an toàn xóa (không phải 9), chỉ 4 cặp đáng gộp (không phải 6 — 2 cặp khác nghĩa), và tên cột PHẢI dùng VIEW (không rename vì chạm tới 153 file). Đây là "tư duy liên kết" để không làm hỏng hệ thống. Mọi hành động chạm production vẫn chờ anh duyệt + backup.
