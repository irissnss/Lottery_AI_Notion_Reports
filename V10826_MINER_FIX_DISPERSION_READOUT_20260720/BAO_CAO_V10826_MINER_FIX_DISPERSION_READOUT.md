# BÁO CÁO V10826 — KIỂM TRA TOÀN DIỆN ĐẦU NGÀY 20/07 + PHÁT HIỆN & FIX GỐC MINER TUẦN + ĐO ĐỘ PHÂN TÁN PHIẾU MODEL

- **Ngày:** 2026-07-20 (10:31 → 12:0x, giờ VN)
- **Loại:** bugfix runtime (miner subprocess) + kiểm tra toàn diện đầu ngày + readout đo lường (độ phân tán phiếu)
- **Nguồn lệnh owner (10:31):** *"xuôi ngược gì nó phải có điều kiện đi kèm mới có khả năng cao và chính xác nha em. Đầu ngày rồi em tiến hành kiểm tra toàn diện dùm anh nha em. Hiện mỗi model ra mỗi số thiệt phức tạp quá total khó mà tóm gọn các số tốt ah em. Xem kỹ thật kỹ tỉ mỉ và phương án thật tối ưu nha em, theo sát dùm anh"*
- **Governance seq:** 288 · **Zero đụng official:** /du-doan · final_bundles writer · model selector KHÔNG đổi; hash 4 bảng pre/post IDENTICAL.

---

## 1. KIỂM TRA TOÀN DIỆN ĐẦU NGÀY — KẾT QUẢ TỔNG

| Hạng mục | Kết quả |
|---|---|
| Service + health | ✅ active, /api/health 200, journal 0 lỗi |
| **Self-check T2 08:10 (lần cron ĐẦU TIÊN)** | ✅ **11/11 ALL PASS** — gồm check-11 `no_shortcode_station_14d` (V10810) PASS rows=0 và check-3 retrain đọc "OK rows 8d=12" (item nghi vấn V10824 đóng: định nghĩa OK tự thông) |
| Chu kỳ MN sáng | ✅ 15 official + 12 shadow (grok-4.3 ngày-3 đủ 3 miền), 28 trace PB-18.1 |
| Bundle MN | ✅ BT 26 chốt 04:18 (M2s hôm nay MN [26,90] — trùng bundle + khóa /choi) |
| A/B shadow V10809 | ✅ 5 rows sáng, 0 lỗi call |
| Khóa tuần /choi | ✅ T2 lock 3 miền @07:03 |
| Watch xuôi/đảo hôm nay | cand xuôi **46** (GĐB 46438) + cand đảo **64** — X1/X3 panel tự chấm sau MN 16:15 / MT 17:15, TRƯỚC giờ MB 18:15 |
| **Miner rules tuần T2 00:30** | ❌ **CHẾT — phát hiện + fix trong phiên (mục 2)** |

## 2. PHÁT HIỆN LỚN: MINER TUẦN CHẾT NGẦM 3/5 THỨ HAI — ĐÃ MINE BÙ W30 + FIX GỐC

### 2.1 Triệu chứng & truy vết
- Sáng 20/07 (Thứ Hai) rules vẫn ở **v2026W29 mine 15/07** — đúng lịch thì 00:30 đã phải có W30.
- Truy vết 5 lớp (`_v10826_miner_forensic*.py`): `mining_log` (nguồn thật DB) + `scheduler_logs` + journal + crontab + `app_settings`.
- **Chìa khóa mở án: `scheduler_logs.log_time` là UTC** — job "17:30 Chủ Nhật" trong log chính là **00:30 Thứ Hai giờ VN**. Job CÓ nổ đúng lịch, nhưng chết ngay dòng log đầu.
- Root cause: `_run_weekly_rule_mining` chạy **in-process**; stdout của service process bị job trước đóng → `print()` trong `weekly_rule_miner` nổ **"I/O operation on closed file"** ngay lập tức. Đúng bệnh V10800 từng chữa cho retrain CN 02:00 + optimizer 03:00 — nhưng **miner bị bỏ sót**.
- Tần suất: **3/5 Thứ Hai gần nhất fail** (22/06 · 13/07 · 20/07). Các lần sống là nhờ chạy qua đường subprocess khác (weekly_guard 07:00 ngày 15/07 SUCCESS, catch-up tay SUCCESS) — cùng pipeline, khác đường I/O ⇒ chẩn đoán chốt.
- Lưới đỡ hiện có: guard 07:00 hằng ngày tự mine lại khi rules >9 ngày — nghĩa là nếu không phát hiện, hệ vẫn tự cứu ~24/07 nhưng **chịu rules cũ cả tuần**.

### 2.2 Xử lý (2 nước, cùng phiên)
1. **Mine bù W30 ngay** (`_v10826_mine_catchup.py`): backup `mined_rules` 2 đầu TRƯỚC khi mine (local `backups/v10826_pre/` + VPS `/root/backups_v10826/mined_rules_pre_w30.db`) → chạy qua **subprocess** → `mining_log`: **SUCCESS v2026W30, 105 rules / 8 STRONG**, data-cut tới 19/07 y hệt job 00:30 đáng lẽ chạy.
2. **Fix gốc `scheduler.py`**: `_run_weekly_rule_mining` → delegate **subprocess** (`python -c run_weekly_mining(schedule_slot='auto')`), stdout ghi `logs/weekly_miner_cron.log`, kết quả đọc từ bảng `mining_log` (DB là nguồn thật, không tin stdout). Dry-run PASS trước deploy.

### 2.3 Verify sau mine bù (union W29 → W30)
- **MN, MT: union y hệt W29** (MN sang zero lệch) — không xáo trộn giữa trial.
- **MB: 9 → 8 số** (+68 mới; −36, −79 rớt) = mining tuần hoạt động đúng chức năng, áp dụng từ chiều 20/07.
- MRE rebuild 112d kiểm tra: 0 orphan rule_id, khoảng ngày đủ.

## 3. ĐO ĐỘ PHÂN TÁN PHIẾU MODEL — TRẢ LỜI "MỖI MODEL RA MỖI SỐ, TOTAL KHÓ TÓM GỌN"

Owner nhắc lần 2 (lần 1 = 18/07 19:39 → V10821/22/23) ⇒ theo §52 re-reminder: audit lại chuỗi cũ (ĐỦ deliverable) + bổ sung **readout bằng số** để owner nhìn hằng ngày thay vì cảm giác.

### 3.1 Kết quả đo (READ-ONLY từ `predictions` canonical, pick trước freeze)
| Thước | Nền 90d trước trial | Trial 18-20/07 | Đọc |
|---|---|---|---|
| Số KHÁC NHAU / miền / ngày (15 model) | 12.6–12.9 | 10–14 | **KHÔNG tán hơn nền** — xưa giờ vẫn vậy, không phải bệnh mới |
| Top-share (số dày phiếu nhất) | 38–41% | 27–47% | dao động bình thường |
| **%phiếu rơi TRONG danh sách rules** | **24–30%** | **48–69%** | **×2 — RULES-FIRST đang GOM phiếu vào rules đúng thiết kế** |

### 3.2 Kết luận phương án tối ưu
- Cái thay đổi thật KHÔNG phải "tán hơn" mà là **phiếu dồn vào cụm rules gấp đôi** → trục tóm gọn đúng = **M2s coverage-rules top-2 + DÀN-4** (đã thắng M0 +5→+12pp backtest 165 ngày; 7+2 biến thể đã quét không ai hơn — V10823). Bằng chứng sống hôm nay: M2s MN [26,90] trùng đúng bundle BT 26 + khóa /choi [26].
- **Không đổi kỳ đo, không thêm biến số** — giữ nguyên mốc 25/07 giữa kỳ · 28/07 CHỐT.
- Cảnh báo viết sẵn: %in-rules tụt <35% nhiều ngày = model bỏ rules → báo động trial.

### 3.3 Hạ tầng readout (deploy trong phiên)
- `_v10821_total_v2_shadow.py`: thêm `_day_dispersion` / `_stored_union` / `_dispersion_view` — **union rules lấy AS-OF từng ngày** từ `rules_union_json` bảng daily (chống miner T2 "viết lại lịch sử" MRE 112d); cache nền tĩnh ⇒ ~0.1s/call.
- `monitoring.html` panel 🧮: khối mới **📡 ĐỘ PHÂN TÁN PHIẾU MODEL** (uniq · số dày nhất · %in-rules vs nền 90d + vệt từng ngày trial, auto-refresh 60s sẵn qua loadTotalV2).

## 4. XUÔI/NGƯỢC PHẢI CÓ ĐIỀU KIỆN — KHẲNG ĐỊNH + NHẤN UI

- Nguyên tắc owner chốt **khớp đúng thiết kế đang chạy**: mọi ngưỡng hành động đặt trên bản-CÓ-điều-kiện (xuôi: X1 đuôi GĐB MN chiều / X3 MN∪MT — V10825; đảo: lớp điều kiện 🧩 A6… — V10817); bản thô chỉ là đối chứng.
- UI nhấn thêm (deploy trong phiên): dòng watch xuôi ghi đậm **"chỉ tính tín hiệu khi X1/X3 NỔ"**; dòng watch đảo ghi **"chỉ tính tín hiệu khi lớp 🧩 nổ — bản thô là đối chứng"**.

## 5. CHUỖI §52 — BẰNG CHỨNG

- Backup 2 đầu: `backups/v10826_pre/` (local) + `/root/backups_v10826/` (VPS, gồm `mined_rules_pre_w30.db`); sha 3 file khớp sau upload.
- Sandbox: py_compile + node --check PASS; dry-run miner delegate PASS; đo compute_view ~0.1s.
- Deploy: restart 11:51 active; health 200 · admin unauth 401 · /du-doan 200; journal sạch; job miner re-add xác nhận trong journal; view dispersion sống trên VPS.
- **Hash 4 bảng pre/post IDENTICAL:** predictions `7f54ae9a` · final_bundles `9e8ad398` · lottery_results `42a3d128` · model_daily_eval `d93423b5`.
- Docs cùng phiên: CHANGELOG · SSOT · FU (FU-V10826-MINER-SUBPROCESS + FU-V10826-DISPERSION-READOUT kèm escalation §52 re-reminder) · STATE seq 288 · HISTORY · playbook (timetable 00:30 + bài học UTC + lịch verify 27/07) · sổ tay owner.

## 6. LỊCH VERIFY TIẾP

| Mốc | Việc |
|---|---|
| Chiều nay 20/07 | Watch xuôi 46 / đảo 64 — panel tự chấm X1/X3 sau 16:15/17:15 |
| 21/07 | Guard-rail trial ngày 3 (model-any < baseline −10pp → rollback ngay) |
| **27/07 T2 00:30** | **Cron miner SUBPROCESS lần thật đầu** — kỳ vọng scheduler_logs "✅ Weekly Mining OK (subprocess)" + `mining_log` W31 SUCCESS; nếu vẫn fail → chuyển crontab hệ thống như retrain_guard |
| 28/07 | CHỐT trial V10820 + Total-V2 + CP-L6 re-verify cả gói |

## 7. ARTIFACTS

`_v10826_morning_full.py` (probe toàn diện + đo phân tán) · `_v10826_miner_forensic2/3/4/5.py` (truy vết UTC + caller + unit) · `_v10826_mine_catchup.py` (backup + mine bù + verify) · `_v10826_mre_verify.py` · `_v10826_union_compare.py` (W29 vs W30) · `_v10826_sandbox.py` · `_v10826_deploy.py` (chuỗi deploy + hash) · code: `scheduler.py` + `_v10821_total_v2_shadow.py` + `monitoring.html`.
