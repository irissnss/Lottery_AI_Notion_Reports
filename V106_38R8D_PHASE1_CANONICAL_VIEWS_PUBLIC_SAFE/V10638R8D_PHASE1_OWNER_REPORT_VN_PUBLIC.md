# V106.38-R8D — PHASE 1 VIEW CANONICAL + DATA DICTIONARY v1.0 (PUBLIC-SAFE)

> Public-safe. Không code business riêng, dòng DB thô, API key, IP/đường dẫn server.
> Không claim *_FIXED / PROMOTED. Read-only thực thi. 0 thay đổi bảng/số production.

- **Auditor**: Opus 4.7 | 2026-05-29
- **Tham chiếu**: R8 (truth) → R8B (dependency) → R8C (verify) → **R8D (Phase 1 thực thi an toàn)**.
- **Owner đã duyệt**: gói A (tên cột qua VIEW) + gói B (xóa rule_features + gộp cặp #4 sau backup).

---

## 1. PHASE 1 — VIEW CANONICAL (đã sinh + test, read-only)

5 VIEW core sinh ra, test PASS, **không ghi gì vào DB thật** (test qua ATTACH read-only):

| VIEW | Alias áp dụng | Rows | Test |
|---|---|---|---|
| v_predictions | target_region→region | 6282 | PASS |
| v_model_daily_eval | bt_number→bach_thu | 6064 | PASS |
| v_mined_rules | target_region→region, target_weekday→weekday | 105 | PASS |
| v_final_bundles | (đã canonical) | 273 | PASS |
| v_lottery_results | (đã canonical) | 14772 | PASS |

→ Code MỚI đọc `v_*` để dùng 1 tên chuẩn (`region`, `date`, `ai_model`, `weekday`, `bach_thu`). Bảng gốc + số liệu **nguyên vẹn**. 0 breakage cho code cũ.

SQL sẵn sàng deploy: `phase1_canonical_views.sql` (chỉ áp lên DB khi owner duyệt deploy).

---

## 2. DATA DICTIONARY v1.0 — SSOT (promote)
- 1 tên/khái niệm (mục 1) · nhãn flow (official/lane/shadow) · khóa per-slice `(flow, region, station, weekday)`.
- Đài canonical + lịch đài×thứ verified (HCM=T2+T7; Hà Nội=T2+T5; Thừa Thiên Huế=T2+CN).
- Model: KHÔNG gộp; registry 41 là SSOT; giữ row lịch sử.
- Cố ý CHƯA gộp các cái mơ hồ (phase_type/mined_at/score/confidence/main_numbers/source_*).

---

## 3. PHASE B — XÓA/GỘP (SQL sẵn sàng, CHỜ bấm nút + backup)
- **Xóa**: `rule_features` (0 dòng, 0 ref) — sau backup.
- **Gộp dup thật**: `ai_region_specialist_prompt_shadow_results` → `ai_prompt_context_audit_shadow` (75 dòng giống 100%). ⚠️ Cần consolidate 2 materializer (code) TRƯỚC khi DROP.
- **GIỮ** 2 cặp region-subset + 1 version + 1 khác-nghĩa + 8 bảng-trống-còn-dùng.
- SQL: `phase_b_drop_merge.sql` — **CHƯA chạy**, chờ owner bấm nút + backup.

---

## 4. AN TOÀN
- Phase 1 = sinh VIEW SQL + test trên DB tạm qua ATTACH read-only → **0 ghi vào DB thật, 0 đổi số**.
- docs/DATA_DICTIONARY.md = tài liệu SSOT (không phải runtime).
- Phase B (xóa/gộp bảng) = SQL sẵn sàng nhưng **chưa thực thi** (chờ backup + bấm nút + deploy gate).
- AI vẫn chạy tới 2026-06-03 để đo edge thật (MB frequency) — chuẩn hóa chạy song song, không chặn.

---

## 5. CÒN LẠI (chờ)
- Owner bấm nút + backup → thực thi Phase B (xóa rule_features, refactor 2 materializer rồi gộp cặp #4).
- Deploy VIEW lên production (deploy gate riêng).
- Tiếp tục refactor code cũ dần sang đọc `v_*` (không vội).

---

**Bottom line**: Phase 1 hoàn tất an toàn — 5 VIEW canonical đã test PASS (0 đụng số), Data Dictionary v1.0 thành SSOT, SQL xóa/gộp sẵn sàng chờ bấm nút. Đạt mục tiêu "1 tên duy nhất đi tiếp" mà không phá 153 file. Tham chiếu đầy đủ R8→R8D.
