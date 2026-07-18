# BÁO CÁO V10822 — TRẢ LỜI 2 CÂU OWNER: ĐƯỜNG ỐNG XẾP HẠNG RULES (NGÀY+TUẦN) + LANE TEST LÀM LUỒNG OUTPUT MỚI ĐỂ CHƠI 10 NGÀY

- **Ngày:** 2026-07-18, phiên 21:00 → 21:5x
- **Trigger (verbatim):** "Có 2 vấn đề anh cần em tìm hiểu kỹ. 1/ Rules có được tổng hợp phân tích xếp hạng hàng ngày hàng tuần không em? 2/ Nếu /choi, official không can thiệp được để vì sẽ phá đo lường không đo được, thế lane test có xử lý được không. anh cũng muốn 1 luồng output mới để chơi 10 ngày tới chứ nhi"
- **Kết quả:** Câu 1 trả lời bằng bằng chứng (không đổi code). Câu 2 trả lời bằng LANE MỚI đã live + vá 1 bug V10821 phát hiện trong lúc làm.

---

## PHẦN 1 — CÂU 1: RULES CÓ ĐƯỢC TỔNG HỢP / PHÂN TÍCH / XẾP HẠNG HÀNG NGÀY, HÀNG TUẦN KHÔNG?

**CÓ — đủ cả 2 nhịp.** Bằng chứng từ cron + scheduler + DB live (probe `_v10822_rules_pipeline_probe.py`, `probe2`):

| Nhịp | Giờ | Việc | Bằng chứng |
|---|---|---|---|
| Hàng ngày | 20:15 | **MRE chấm TỪNG rule active** của thứ hôm đó (`mined_rule_eval.evaluate_mined_rules`): nguồn phát tails gì, đích trúng gì | `mined_rule_effectiveness` **2.978 rows / 205 ngày liên tục** (20/12/2025 → 18/07/2026, ghi đều 20:15) |
| Hàng ngày | 20:30 | **Re-rank 35 rules MB** — nhấn cửa sổ **8W**, refresh hr_4w/8w/12w/16w từ MRE | snapshot `mined_rules_mb_daily` **45 ngày**; kèm guard pre-predict chống snapshot cũ |
| Hàng ngày | 04:40 + 20:35 | **Re-rank MN/MT độc lập** (`_v10708_mnmt_rule_ranker`) — nhấn **12W/16W**, phân loại vòng đời **MẠNH / TĂNG_TRƯỞNG / ỔN_ĐỊNH / XUỐNG_CẤP / YẾU** (YẾU → suppress), rank 1..35; lượt 20:35 chạy NGAY sau MRE để snapshot sẵn trước mọi lượt AI hôm sau | snapshot `mined_rules_mn_daily` / `mined_rules_mt_daily` **39 ngày** |
| Hàng tuần | T2 00:30 | **Weekly miner** archive version cũ + đào lại toàn bộ từ lịch sử mới | version hiện tại **v2026W29, 105 rules active (35/miền), 21 đợt mine** từ trước tới nay |
| Phụ trợ | hàng ngày / T2 | `weekday_rule_strength_daily` (84 ngày) + cầu-rerank weekly | bảng + cron sống |

Trục đo đúng chuẩn bucket-first **miền × thứ** (rule gắn `target_weekday`; hr_* recompute từ MRE mỗi ngày). Danh sách RULES-FIRST bơm vào prompt mỗi ngày lấy từ đúng hệ này.

---

## PHẦN 2 — CÂU 2: LANE TEST CÓ XỬ LÝ ĐƯỢC KHÔNG? → ĐƯỢC, VÀ ĐÃ LÀM XONG

### 2.1 Vì sao lane là cửa hợp lệ duy nhất (đúng ý anh: không phá phép đo)
- `/du-doan` (official) và `/choi` đang là ĐỐI CHỨNG của 2 phép đo chạy dở (trial V10820 đến 28/07, khóa tuần money board immutable) → cấm đụng.
- Lane test (`du_doan_test_bundles`) có sẵn hạ tầng: **34 experiment đăng ký**, evaluator chấm **GENERIC mọi bundle mỗi tối** (lane mới TỰ được chấm + vào scoreboard 7/14/30d), test_only/admin_only/output_eligible=0.
- **/choi miễn nhiễm có cơ chế**: money board chỉ nhận method mới làm ứng viên khóa tuần khi đủ **≥24 ngày (MB) / ≥30 ngày (MN/MT)** dữ liệu — lane mới chạy 10 ngày thuần song song, không thể chen vào khóa tuần hiện tại.

### 2.2 Lane `TOTAL_V2_RULES_V1` (3 miền) — luồng output mới để anh chơi
- **Phương pháp:** M2s COVERAGE-RULES (V10821 backtest 165 ngày leak-safe: BT MN 48.6% / MT 44.3% / MB 32.9% vs bundle thật 42.9/39.3/21.4; 60 ngày gần +10/+8.3/+15pp): 1 model = 1 phiếu cho MỖI số nó chạm (chính + phụ), ưu tiên tuyệt đối số trong danh sách rules ngày đó; danh sách <4 số thì fallback đếm phiếu thuần.
- **Khác biệt then chốt so với shadow:** ghi số **TRƯỚC giờ xổ** nên danh sách rules tính **LIVE** (`live_rules_union`): rules active của (miền×thứ) + kết quả đài nguồn ĐÃ QUAY trong DB (D-1 luôn có; same-day chỉ cặp hợp lệ MT←MN, MB←MN/MT khi nguồn đã xổ) — dùng chung code trích số với MRE nên khớp 100%, không nhìn trộm tương lai.
- **Lịch ghi số:** **MN 15:47 · MT 16:56 · MB 17:56** — đều TRƯỚC mốc khóa chống-nhìn-trước của /choi (16h/17h/18h) và SAU T-chốt bundle (để so diff với bản chốt official).
- **Anh lấy số ở đâu:** `/monitoring` panel 🧮 → khối **🚏 LANE TOTAL_V2_RULES_V1** (màu vàng): "hôm nay BT=xx bộ2=[xx, yy] lúc HH:MM" + 7 ngày gần ✓/✗ + BT%/any% cộng dồn. Preview phía trên cho xem sớm hơn (giờ đã dùng union live pre-draw).
- **Dry-run 18/07 (không ghi DB):** MN [31,38] · MT [41,46] — **46 VỀ ✓** · MB [93,86] — **86 VỀ ✓**; n_models 15/15, union 14/11/8 khớp đúng danh sách RULES-FIRST ngày-1.

### 2.3 Bug V10821 phát hiện & vá trong phiên
- **Cron shadow 19:14 chạy TRƯỚC MRE 20:15** → row ngày mới luôn `rules_active=0`, tức M2s âm thầm rơi về M1 mỗi ngày mới — nếu không vá thì 10 ngày forward đo SAI phương pháp. Bằng chứng: row 18/07 (ghi 20:1x) có rules_active=0 cả 3 miền; MT bộ2 là [41,97] thay vì [41,46].
- **Vá:** dời cron **19:14 → 20:50** (sau MRE 20:15 + re-rank 20:30/20:35; --catchup 3 tự chấm lại ngày cũ) + re-chấm 18/07: MT [41,**46**] 46✓, MB [93,86] 86✓ → **M2s any ngày-1 = 2/3**.
- Preview panel pre-draw cũng được sửa cùng lỗi gốc (trước 20:15 luôn "rules⏸ fallback M1").

### 2.4 Chuỗi §52 + verify
- Backup 2 đầu TRƯỚC sửa: `backups/v10822_pre/` (local) + `/root/backups_v10822/` (VPS).
- SHA khớp 3 file upload; py_compile + node --check pass; đăng ký 3 experiment idempotent; 3 cron lane mới + dời cron shadow.
- Restart `lottery.service` 21:3x (ngoài giờ job học) → active; health 200; admin endpoint 401 khi chưa auth; journal sạch.
- **Hash 4 bảng official pre/post IDENTICAL**: predictions a6a7fa8e / final_bundles c6bb036d / lottery_results b080e2cc / model_daily_eval b8de7d94. (Bảng lane là test-surface, không thuộc 4 bảng official.)

### 2.5 Mốc tiếp theo
| Ngày | Việc |
|---|---|
| 19/07 chiều-tối | 3 rows lane đầu tiên (15:47/16:56/17:56) hiện trong khối 🚏 + row forward shadow đầu tiên 20:50 |
| 28/07 | Đọc CÙNG cửa sổ V10820/V10821: lane BT%/any% forward = bằng chứng "chơi thật" bổ sung cho quyết promote writer (ngưỡng giữ nguyên M2s−M0 ≥ +5pp BT gộp 3 miền) |
| ~12-17/08 | Lane tự đủ 24-30 ngày → thành ứng viên khóa tuần /choi theo cơ chế sẵn có (không cần code); anh muốn sớm hơn thì ký riêng |

---

## PHẦN 3 — BỔ SUNG 21:44 (owner: "luồng mới cũng để đo so sánh đúng không? backup lane chưa? total lại để có lịch sử từ đây")

### 3.1 Xác nhận: lane vừa CHƠI vừa là kênh ĐO chính thức
- 3 tầng đo: (i) khối 🚏 tự chấm BT/any mỗi ngày; (ii) evaluator + scoreboard 7/14/30 ngày từ 19/07, so trực tiếp với 34 lane khác + lane đối chứng `{R}_OFFICIAL_BASELINE_CONTROL`; (iii) đọc chốt 28/07 cùng V10820/V10821.
- Caveat ghi sẵn: lane dùng union LIVE (pre-draw) còn shadow dùng MRE (post-draw) — nếu crawl KQ nguồn trễ thì hai bên có thể lệch nhẹ = train/serve gap ĐO ĐƯỢC (diff nằm sẵn trong risk_flags + so được 2 bảng).

### 3.2 Backup hoàn chỉnh (vá thiếu sót lượt deploy đầu) + rollback
- Lượt đầu mới backup 2 file code bị sửa; owner nhắc đúng — đã bổ sung: **crontab post + PRE tái dựng** (`crontab_{pre,post}_v10822.txt`), **lane script deployed** copy vào backup dir, **snapshot JSON** (3 registry rows + 3 rows ngày-0 + pre-fix values của row shadow 18/07). Tất cả nằm CẢ 2 ĐẦU: `/root/backups_v10822/` + `backups/v10822_pre/`.
- **Script quay đầu `_v10822_rollback.py`** (mặc định dry-run in kế hoạch; `--confirm` mới chạy): gỡ 3 cron lane → khôi phục 2 file .pre → xóa lane script → dọn DB lane (results/bundles/runs/registry) → restart + health/admin check → nhắc hash 4 bảng. Mặc định GIỮ cron shadow 20:50 (19:14 là bug); `--restore-cron-bug` nếu owner cần nguyên trạng từng bit.

### 3.3 Ngày-0 (18/07) đã ghi vào lane — lịch sử liền mạch từ hôm nay
- Run_id **8253-8255**, mode `RETRO_POST_DRAW_BASELINE`, diagnostic_only=1, risk_flags `retro_post_draw=true`: picks tính bằng ĐÚNG code lane với nguồn causal pre-draw (predictions trước freeze + union live từ đài nguồn đã quay) — chỉ THỜI ĐIỂM GHI 21:48 là sau xổ, nên: **/choi tự loại** (cutoff giờ tạo), **scoreboard không tính** (evaluator 18/07 đã chạy xong trước đó), chỉ hiện ở khối 🚏 làm mốc lịch sử.
- **Số ngày-0: MN [31,38] ✗ · MT [41,46] — 46 VỀ (phụ✓) · MB [93,86] — 86 VỀ (phụ✓) = any 2/3 miền.**
- Hash 4 bảng official pre/post **IDENTICAL lần 2** (a6a7fa8e / c6bb036d / b080e2cc / b8de7d94).

---

## ARTIFACTS
- Lane: `web/backend/_v10822_total_v2_lane.py`; shadow module cập nhật: `web/backend/_v10821_total_v2_shadow.py`; UI: `web/frontend/monitoring.html` (khối 🚏).
- Probes: `_v10822_rules_pipeline_probe.py`, `probe2`, `_v10822_lane_pattern_probe.py`, `_v10822_lane_schema_probe.py`, `_v10822_scoring_probe.py`, `_v10822_guard_probe.py`, `_v10822_moneyboard_safety_probe.py`, `_v10822_impl_check_probe.py`.
- Deploy/fix: `_v10822_deploy.py`, `_v10822_cron_fix.py`, `_v10822_day0_and_backup.py`, `_v10822_rollback.py`; backup `backups/v10822_pre/` (2 file .pre + crontab pre/post + `v10822_lane_snapshot.json`) + VPS `/root/backups_v10822/`.
- Governance: CHANGELOG V10822 (+mục 5) · SSOT V10822 (+row bổ sung) · FU-V10822-TOTAL-V2-LANE · AUTOMATION_STATE seq 283 (extended) · HISTORY jsonl (V10822 + V10822b) · PLAYBOOK §1+§5 · SO_TAY mục 1.3.
