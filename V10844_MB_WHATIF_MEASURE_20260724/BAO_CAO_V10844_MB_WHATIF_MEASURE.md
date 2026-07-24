# V10844 — TRIỂN KHAI ĐO ĐƯỢC OWNER DUYỆT: WHAT-IF /choi MB (LANE V2/V3 vs AE) + AE THEO NGUỒN

- Phiên: 24/07/2026 23:45 → 25/07 00:1x (giờ VN), ngay sau báo cáo cuối ngày V10843.
- Lệnh owner (verbatim): "Các vấn đề an toàn , có giá trị nâng cao dự đoán  đã xác thực , đo lường rõ ràng thì tiến hành dùm anh đi em."

## 1. PHẠM VI — CHỈ LÀM MỤC ĐÃ ĐO RÕ

| Mục đề xuất từ V10843 | Quyết định phiên này | Lý do |
|---|---|---|
| Đo shadow what-if /choi MB = lane V2/V3 thay AE | ✅ **TRIỂN KHAI** (bảng + API + panel + cron) | Đã đo rõ: AE-MB không nguồn nào vượt baseline ~25% (30d); /choi MB 4/13, 0/4 gần nhất; laneV2 MB BT 3/6 cùng kỳ |
| Readout AE V67 theo nguồn lên /monitoring | ✅ **TRIỂN KHAI** (trong cùng API + panel) | Data đã có sẵn trong `contributions_json` — chỉ hiển thị, zero đổi gate |
| Mở rộng catalog V10829 / rút trailing window | ❌ **KHÔNG LÀM phiên này** | FU-V10829 cấm sửa giữa cửa sổ đo; remedy chưa được xác thực → đọc skim 28/07 rồi mới thiết kế |
| AE-MT | ❌ **KHÔNG ĐỤNG** | MT có edge thật (same_region_lag1 54.5% 30d) |

**Nguyên tắc giữ nguyên:** production /choi MB VẪN chạy AE + gate như cũ. Phiên này CHỈ đo — không đổi số nào owner nhìn thấy ở /choi, /du-doan.

## 2. THIẾT KẾ ĐO (anti-lookahead)

- Bảng `v10844_mb_whatif_daily` (UNIQUE date; `output_eligible=0, diagnostic_only=1, owner_approved=0, shadow_only=1`).
- Mỗi ngày 1 row so 3 cánh tay MB, tất cả lấy từ row **đã ghi trước cutoff 18:00 VN** (MB xổ ~18:15):
  - `/choi` thật: `money_board_daily_lock` (khoá ≤17:54).
  - Lane V2: `MB_TOTAL_V2_RULES_V1` (cron 17:56) — row MỚI NHẤT pre-cutoff.
  - Lane V3: `MB_TOTAL_V3_COND_V1` (cron 17:58) — row MỚI NHẤT pre-cutoff.
- Không gọi model mới, không sinh số mới — chỉ đối chiếu các luồng đã tồn tại với kết quả (về-lô).
- `row_source`: 19–24/07 = `pre_v10844` (lane vốn ghi trước giờ xổ nên leak-safe, nhưng chỉ để tham khảo); **forward đếm từ 25/07** (sau thời điểm owner duyệt).
- Cron VPS `10 21 * * *` (21:10 VN, sau rule-cond 21:00), log `logs/v10844_mb_whatif.log`, `--catchup 2` idempotent.

## 3. NGƯỠNG HÀNH ĐỘNG (viết sẵn — không mơ hồ)

> Sau ≥7 ngày forward: **BT% lane (V2 hoặc V3) − hit% /choi ≥ +15pp bền** (không đảo dấu giữa 2 nửa kỳ) → trình owner **1 quyết định** đổi nguồn /choi MB. Dưới ngưỡng → giữ AE + gate. Trước đó KHÔNG đổi gì. Đọc sớm nhất ~01/08, kèm skim 28/07.

## 4. BACKFILL 19–24/07 (pre_v10844 — tham khảo)

| Cánh tay | Kết quả | % |
|---|---|---|
| /choi thật (AE/gate) | 0/4 | 0% |
| AE lane BT | 0/4 | 0% |
| **lane V2 BT** | **3/6** | **50%** |
| lane V2 any | 4/6 | 66.7% |
| lane V3 BT | 2/3 | 66.7% |
| lane V3 any | 2/3 | 66.7% |

Từng ngày: 19/07 /choi[69,93]✗ AE93✗ V2:46✗ · 20/07 [46,69]✗ 46✗ V2:26✗ · 21/07 [48,57]✗ 48✗ V2:09✓ · 22/07 /choi∅ V2:97✗(any✓) V3:33✗ · 23/07 /choi∅ V2:39✓ V3:93✓ · 24/07 [60]✗ 60✗ V2:17✓ V3:17✓. Khớp 100% số liệu V10843.

## 5. AE THEO NGUỒN (readout 30d — per-candidate về-lô, hiển thị trong cùng panel)

| Miền | Nguồn | hit/n | % |
|---|---|---|---|
| MT | same_region_lag1_final_bundle | 12/22 | 54.5% |
| MT | per_model_lag1 | 61/136 | 44.9% |
| MT | lo2_lag1_final_bundle | 6/14 | 42.9% |
| MT | cross_region_nextday | 5/12 | 41.7% |
| MT | cross_region_sameday | 2/8 | 25.0% |
| MB | per_model_lag1 | 43/164 | 26.2% |
| MB | cross_region_sameday | 7/30 | 23.3% |
| MB | cross_region_nextday | 0/2 | 0.0% |

## 6. SURFACE ĐÃ LIVE

- **API** `GET /api/admin/mb-whatif`: `require_admin` + `Cache-Control: no-store`; trả rows + tally forward/gộp + `ae_sources` + ngưỡng.
- **Panel** 🔁 "WHAT-IF /choi MB (V10844)" tại `/monitoring`, cạnh panel 📐; đăng ký `loadMbWhatif()` trong `loadAllSections()` **và** `setInterval` 60s (đúng §52B).
- **Materializer** `_v10844_mb_whatif.py`: import-safe (không wrap stdout module-level — bài học V10831/V10843), ngày VN explicit, DB path chuẩn V10821.

## 7. VERIFY + AN TOÀN

- Local: compile PASS, backfill 6 row, compute_view PASS.
- VPS: backup remote `/root/backups_v10844/` (main.py + monitoring.html) + backup local `backups/v10844_pre/`; upload 3 file; compile OK; backfill 6 row **khớp local từng số**; restart `lottery.service` → active; health 200; `mb-whatif(anon)=401` · `total-v2(anon)=401` · `/monitoring=401` (admin-only đúng); compute_view trên VPS success; cron dòng 98.
- **Hash 4 bảng official pre=post IDENTICAL** (`predictions 10847/5adf2f7c · final_bundles 441/74b1705d · lottery_results 15140/95bf835b · model_daily_eval 10711/c2f1589e`).
- ZERO đụng: `/du-doan`, writer bundle, `/choi` lock logic, AE lane, selector, prompt, MT.

## 8. CHỜ LIVE + LỊCH

- 25/07 21:10: cron chạy lần đầu → row forward đầu tiên (25/07 có kết quả MB).
- Owner mở `/monitoring` → panel 🔁 hiển thị (verify mắt).
- Đọc ngưỡng sớm nhất ~01/08; đọc kèm skim 28/07 (cùng buổi với rule-cond forward + lean agenda).
- FU-V10843-AE-MB-SOURCE-EDGE = `DEPLOYED_PENDING_LIVE_VERIFY`.

## 9. GOVERNANCE

- CHANGELOG V10844 · SSOT block V10844 · FU-V10843 cập nhật owner_ack 23:45 · AUTOMATION_STATE seq 305 + HISTORY.
- Files: `_v10844_mb_whatif.py` · `main.py` · `monitoring.html` · `_v10844_deploy.py` · `_v10844_state_update.py`.
