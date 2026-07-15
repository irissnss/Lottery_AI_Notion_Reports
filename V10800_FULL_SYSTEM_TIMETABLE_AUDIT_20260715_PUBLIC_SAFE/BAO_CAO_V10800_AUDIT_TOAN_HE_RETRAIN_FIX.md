# V10800 — AUDIT TOÀN HỆ 3 MIỀN × 3 LUỒNG + MỌI MỐC HỌC TẬP → PHÁT HIỆN & FIX RETRAIN/OPTIMIZER CN CHẾT NGẦM + SELF-CHECK ĐỊNH KỲ

- **Ngày:** 15/07/2026 chiều (12:54 → 14:0x)
- **Trạng thái:** DEPLOYED — chờ verify sống CN 19/07 (retrain + optimizer) + T2 21/07 (self-check cron đầu tiên)
- **Yêu cầu owner (12:54):** "MN anh chả thấy em đề cập gì — đã nhắc là toàn bộ 3 miền, 3 luồng rồi mà, rồi các mốc giờ retrain nữa, mốc giờ học tập phân tích, xếp hạng rules, pattern nữa — verify lại luôn xem mốc giờ và cơ chế tổng hợp với số ngày số tuần còn đúng không, còn tương thích phù hợp không. Nói chung đây là những thứ cốt lõi để hệ thống ổn định và chính xác, phải kiểm tra định kỳ và thường xuyên. Xem lại toàn diện 1 lần nữa."

---

## 1. CÁCH LÀM — KHÔNG TIN COMMENT, CHỈ TIN NGUỒN THẬT

Dựng **bảng giờ toàn hệ** từ 3 nguồn sự thật:
1. **43 job scheduler** — journal `Added job` ngay sau restart (không đọc code suy diễn).
2. **40 dòng crontab VPS** — dump nguyên văn.
3. **app_settings** — giờ retrain/optimizer/predict/scrape từ DB.

Rồi đối chiếu TỪNG mốc với **dữ liệu thật sinh ra trong DB**: giờ tạo predictions (token/shadow), giờ tạo/updated bundle, giờ tạo lane rows, giờ settle, giờ lock /choi, freshness từng bảng học tập (`training_history`, `mined_rules*`, `*_rule_context`, `cau_registry`, `v10763_pattern_reasoning_daily`, `model_daily_eval`, `money_board_lock`).

## 2. PHÁT HIỆN LỚN — 2 JOB HỌC TẬP CHỦ NHẬT CHẾT NGẦM

### 2.1 Auto Retrain CN 02:00 — FAILED 4/6 tuần gần nhất

| Chủ nhật | training_history (12 dòng model×miền) |
|---|---|
| 07/06 | OK |
| 14/06 | **FAILED ×12** |
| 21/06 | **FAILED ×12** |
| 28/06 | **FAILED ×12** |
| 05/07 | OK (auc 0.48-0.56 ghi đủ) |
| 12/07 | **FAILED ×12** |

- Lỗi đồng loạt tức thì: **`I/O operation on closed file`** — stdout của service process bị handle đóng (job trước đó trong process để lại), mọi `print()` bên trong trainer nổ ngay khi bắt đầu.
- **Hệ sống 6 tuần nay nhờ backstop:** `_v10646_retrain_guard.py` (cron 06:30 hằng ngày, threshold 8 ngày) tự rebuild khi model quá tuổi. Bằng chứng mtime model files: **03/07 06:31 → 13/07 06:31**.
- **Hệ quả cho "mốc giờ retrain":** chu kỳ học ML THẬT là ~8-10 ngày lúc 06:30 sáng, KHÔNG phải CN 02:00 hằng tuần như thiết kế. Ngày guard rebuild (06:30), MN 04:00 đã predict bằng model cũ, MT/MB chiều dùng model mới — lệch trong-ngày.

### 2.2 Weight optimizer CN 03:00 — chết CÙNG LỖI

- 12/07 03:00: `❌ Lỗi khi tối ưu weights: I/O operation on closed file` — fail ngay miền đầu.
- Lần chạy thành công gần nhất: 05/07 (cùng ngày retrain OK) → sau đó chỉ chạy nhờ **weekly_guard 07:00 fallback** (marker >9 ngày) — lần thật 10/07 07:14.

### 2.3 Chứng cứ chéo → kết luận nguyên nhân

Cùng pipeline (cùng module train/optimize) chạy qua **SUBPROCESS** (guard cron 06:30, `_run_optimizer_once.py` do weekly_guard launch) thành công **100%**. → Lỗi là **môi trường process** (stdout đóng), không phải code train. Ngày 05/07 OK vì service vừa restart trước đó (stdout còn sạch).

## 3. FIX — MỘT ĐƯỜNG CHẠY DUY NHẤT (hết cảnh scheduled-path chết, guard-path sống)

| Job | Trước (chết) | Sau (V10800) |
|---|---|---|
| Retrain CN 02:00 | train in-process trong service | subprocess `_v10646_retrain_guard.py --force` (timeout 2700s) — parse `retrain_all rc=0; lstm_XX=ok` → ghi `training_history` 12 dòng OK/FAILED THẬT |
| Optimizer CN 03:00 | optimize in-process | subprocess `_run_optimizer_once.py` (timeout 3600s, log `logs/optimizer_once.log`) |
| `_run_optimizer_once.py` | hardcode `/root/...` | repo-relative + đọc setting `weight_optimizer_metric` |
| Backstop | guard 06:30 / weekly_guard 07:00 | GIỮ NGUYÊN (idempotent — CN thành công thì guard chỉ FRESH_SKIP) |

- Trade-off ghi nhận minh bạch: AUC-regression-gate V17.3 (in-process) nghỉ theo đường cũ — nhưng đường cũ đã chết từ 14/06 nên gate thực tế cũng chưa từng chạy 4/6 tuần. Metrics per-model vẫn có (`*_metrics.json` + `ml_retrain_guard_log`).
- Cửa sổ train thống nhất theo đường guard: meta/xgb/rf **300 ngày**, LSTM **500 ngày**.

## 4. SELF-CHECK ĐỊNH KỲ MỚI (đáp "phải kiểm tra định kỳ và thường xuyên")

`_v10800_timetable_selfcheck.py` — READ-ONLY, cron **T2 08:10** (sau retrain_guard 06:30, weekly_guard 07:00, mining T2 00:30, cau T2 04:50), chạy tay được bất kỳ lúc nào. **10 bất biến:**

| # | Bất biến | Kết quả chạy ngay trên VPS |
|---|---|---|
| 1 | Tuổi model ML ≤ 8 ngày | PASS (2.3d) |
| 2 | Marker optimizer ≤ 9 ngày | PASS (5.3d) |
| 3 | Retrain OK trong 8 ngày | **FAIL — đúng bệnh vừa phát hiện** (tự khỏi sau CN 19/07) |
| 4 | Rules fresh (mined_rules + mn/mt/mb_rule_context) | PASS |
| 5 | Cau + pattern fresh (cau_registry ≤9d, v10763 ≥ hôm qua) | PASS |
| 6 | MDE hôm qua ≥ 20 model | PASS (26) |
| 7 | T-chốt hôm qua đủ 3 miền | PASS 3/3 |
| 8 | Lane OUTPUT_V1 hôm qua đủ 3 miền | PASS 3/3 |
| 9 | Bundle official hôm qua đủ 3 miền | PASS 3/3 |
| 10 | Weekly lock /choi tuần hiện tại đủ 3 miền | PASS |

Kết quả ghi `logs/timetable_selfcheck.log` + bảng `v10800_selfcheck_log` (append-only).

## 5. MN — TRẢ LỜI ĐỦ (owner nhắc "MN chả thấy đề cập")

Chuỗi MN verify bằng dữ liệu thật 8 ngày (08-15/07):

| Mốc | Giờ thật | Verdict |
|---|---|---|
| Token AI MN | 04:0x-04:45 | ✓ |
| **Shadow MN về** | **04:19-04:45 (n=11)** — về NGAY SAU chain sáng | ✓ pool đủ 26 model từ ~04:45 |
| Bundle sáng | 04:17-04:21 (15 model tại thời điểm đó) | ✓ đảm bảo có output sớm |
| **Chốt 15:45 regen** | pool ĐỦ 26 model — vote sáng-vs-15:45 **đổi 4/8 ngày** | ✓ mốc chốt trễ CÓ GIÁ TRỊ THẬT |
| Freeze 15:55 | guard chặn regen | ✓ |
| Selector K10/K13 MN | 15:56 (sau freeze — không đụng official) | ✓ |
| Xổ 16:15 → scrape + settle | 16:34-16:39 (bundle `updated_at` 16:3x = ghi kết quả verify, KHÔNG đổi picks) | ✓ |
| /choi MN BT1 | daily lock trước cutoff 16:00 (13/07 15:46; 14/07 09:12); **lock-vs-final khớp 8/8 ngày** | ✓ |
| Lane MN 04:30 | n=13-16 (thiếu shadow về sau 04:30); settle 16:34 CHẶN refresh 17:10 → row partial-pool vĩnh viễn | ⚠ caveat ĐO LƯỜNG lane MN (MN không có promote, /choi không dùng lane MN) — KHÔNG sửa để giữ baseline đo K16 nguyên vẹn |

## 6. CÁC MỐC HỌC TẬP / XẾP HẠNG / PATTERN — VERIFY TỪNG CÁI (yêu cầu trực tiếp của owner)

| Nhóm | Lịch | Bằng chứng thật | Verdict |
|---|---|---|---|
| Rules MN/MT (v10708) | 04:40 + 20:35 | log 15/07: MN OK n=35, MT OK n=35; `mn_rule_context` snapshot 15/07, `mt_rule_context` 14/07 (job 16:50 chưa tới giờ — đúng lịch) | ✓ |
| Rules MB (MB-PROD-DYN8W) | 04:45 + guard 17:00 + 20:30 | `mined_rules_mb_daily` snapshot 15/07 (1470 rows) | ✓ |
| Weekly Rule Mining | T2 00:30 + weekly_guard 07:00 | chạy T2 13/07 00:30 (log UTC 12/07 17:30); `mined_rules` max 15/07 | ✓ |
| Cau (soi-cầu registry) | T2 04:50, cửa sổ 320d | `cau_registry` mined_at 13/07 04:50; `cau_forward_shadow` 14/07 | ✓ |
| Pattern V10763 | sau closeout mỗi miền | `v10763_pattern_reasoning_daily` computed 14/07 18:32 (sau MB 18:32) | ✓ |
| `pattern_rules` legacy | — | **0 active** → không bơm gì vào prompt (mined rules V2 là engine chính) — không phải bug | ✓ ghi nhận |
| MDE (chấm điểm model) | 20:20 | 13/07 + 14/07 đủ 26 model × 3 miền (78 rows/ngày) | ✓ |
| Strength 30d (v10692) | sáng hôm sau đọc kết quả đã settle | producer (MDE/results tối) → consumer (lane sáng) đúng thứ tự | ✓ |
| Selector K10/K13 | 15:56/16:56/17:56 + settle 21:30 | `v10789_selector_shadow` max 14/07; log 21:30 | ✓ |
| Champion/budget selector | 06:00 | log 15/07 06:00 | ✓ |
| Scrape 3 miền | 16:30 / 17:30 / 18:30 | thực tế 14/07: 16:34 / 17:30 / 18:32 | ✓ |

## 7. CƠ CHẾ TỔNG HỢP — SỐ NGÀY / SỐ TUẦN VERIFY

| Cơ chế | Cửa sổ | Verdict |
|---|---|---|
| Lane strength (v10692) | 30 ngày, K=25/10/8 (MN/MT/MB), w2=0.6 | ✓ code nguyên |
| Money board | 60d dài / 30d ngắn; cutoff 16/17/18h; weekly lock T2; daily lock | ✓ lock tuần 13/07 đủ 3 miền (15:46); daily MB 14/07 lock 17:58 đủ 2 leg = **bằng chứng sống fix combo V10794 chạy đúng** |
| Retrain data | meta/xgb/rf 300d; LSTM 500d (thống nhất theo đường guard) | ✓ |
| Guard thresholds | model 8d; optimizer/mining 9d | ✓ |
| T-chốt + freeze | 15:45/16:54/17:54 + freeze :55 (V10798) | ✓ journal sau restart đăng ký đúng |
| K11a/K15 promote | lookback giữ nguyên; đọc lane bundle (16:53/17:52) tại chốt :54 | ✓ by-construction |

## 8. DEPLOY + AN TOÀN

- Backup: local `backups/v10800_pre/` + remote `/root/backups/v10800_pre/`.
- SCP 3 file: `scheduler.py`, `_run_optimizer_once.py`, `_v10800_timetable_selfcheck.py` → py_compile remote OK.
- Cron mới (idempotent): `10 8 * * 1 … _v10800_timetable_selfcheck.py >> logs/timetable_selfcheck.log`.
- Restart `active`; smoke: health=200, /choi=401 (login-only — đúng), admin_noauth=401.
- Journal: `Auto Retrain (sun 02:00)`, `Tối ưu weights tự động (sun 03:00)`, T-chốt 15:45/16:54/17:54 — đăng ký đúng.
- Verify subprocess đúng call-path mới: `retrain_guard --check` rc=0.
- **Hash 4 bảng official pre=post IDENTICAL:** predictions 10084/4ac2715e · final_bundles 412/d99a595e · lottery_results 15075/d8f34e1a · model_daily_eval 9908/97c981c1.
- KHÔNG đụng: thuật toán train (chỉ đổi cách gọi), vote/promote/freeze/money-board, mốc V10798, /du-doan 15/15, lane 20/20.
- Rollback: restore 2 file từ `/root/backups/v10800_pre/` + bỏ dòng cron + restart.

## 9. LỊCH VERIFY SỐNG

| Mốc | Việc |
|---|---|
| Tối 15/07 | (chung V10798/V10799) lane 16:53/17:52 → chốt :54 → freeze :55; watchdog không báo giả |
| **CN 19/07 sáng** | `training_history` 19/07 = 12 dòng OK; `logs/optimizer_once.log` DONE ×3 miền; marker mới. Nếu vẫn FAIL → stderr giờ được capture, không còn mù lỗi |
| **T2 21/07** | `logs/timetable_selfcheck.log` — kỳ vọng ALL PASS (10/10) |
| 16/07 · 17/07 · 19/07 · 23/07 · 24/07 | K11a d7 · K15 d7 · CP-L6 + retire glm-5.1 + CP-R4 · selector-trio 14d · tổng kết lệch pool MT |
