# V10797 — Sửa P1 theo giờ khóa xổ thật + Giải trình CP-L6 (kèm counterfactual) + Checkpoint GLM + Gói hướng cải tiến từ DB

- **Ngày:** 2026-07-15 sáng (READ-ONLY 100% — không code runtime, không deploy)
- **Trigger (owner 08:54):** "17h là khóa xổ MT rồi em dời sang 17h05 sao kịp bó tay bậy ah. MB khóa xổ 18h - nên 17h56 cũng tương đối tàm tạm. CP L6 là gì anh ko nhớ nổi sao mà duyệt em. Cái nào từ DB từ live em đề xuất hướng cải tiến, nâng cao dự đoán nha em"
- **Dữ liệu:** DB live sync `artifacts/live_sync/20260715_085732` (manifest kèm theo). Probe: `_v10797_glm_checkpoint.py`, `_v10797_cpl6_counterfactual.py`, `_v10797_cpl6_cost_roster.py`.

---

## 1. Sửa P1 — em nhận lỗi phần MT

Khung giờ khóa xổ owner chốt (khớp CUTOFF money board trong code: 16.0/17.0/18.0):

| Miền | Khóa xổ | Bundle official hiện tại | Kết luận |
|---|---|---|---|
| MN | 16:00 | 04:21 sáng | Không liên quan — giữ |
| MT | **17:00** | 16:38 (user còn 22') | **KHÔNG DỜI ĐƯỢC** — 17:05 vô dụng, em sai. 16:38 giữ nguyên |
| MB | **18:00** | 17:34 | **Dời được → đề xuất 17:50-17:52** (tốt hơn mốc 17:56): sau shadow-batch MB (~17:47-48) nên pool đủ ~24-26 model, trước lane 17:55, user còn 8-10 phút |

**MT thay thế bằng gì?** 2 đường, ưu tiên (i):
- (i) **Đo tiếp lệch inline-vs-lane đủ 14 ngày (đến 24/07)** — hiện mới 5 ngày (3 lệch nhưng P&L hoà). Nếu pool-thiếu THẬT SỰ gây hại mới tính bước tiếp.
- (ii) Chạy shadow-batch MT **song song** token-batch để pool đủ lúc ~16:48-50 → bundle 16:52 vẫn kịp trước 17:00. Nhưng đụng owner-lock V17.18.1 (shadow là completion-triggered) — chỉ trình nếu (i) chứng minh cần.

**MB P1B — chờ anh gật:** dời job bundle MB 17:34 → **17:50-17:52**. Được: pool đủ (official = đúng thuật toán K11a top-8 kể cả shadow), hết lệch inline-vs-lane, /choi combo đọc cùng nguồn. Mất: user còn 8-10' thay vì 26'. Có rollback flag về 17:34.

## 2. CP-L6 là gì (giải trình lại — anh quên là đúng, nó từ roadmap 19/06)

- **Xuất xứ:** checkpoint TÙY CHỌN cuối roadmap "Lean Harvest" (gặt tinh gọn) ký 19/06: *"official ≈ best model rồi, vậy có cần gọi model ĐẮT hằng ngày nữa không? Đến ~14/07 xét cắt."*
- **Ứng viên cắt:** `claude-opus-4-6` ($15/M tokens — đắt nhất hệ, gấp 5 lần sonnet) và `gpt-5.4` ($5/M).
- **Bằng chứng mới (counterfactual 90 ngày, bỏ model khỏi vote bằng score_breakdown):**

| Kịch bản | MN top1 | MT top1 | MB top1 |
|---|---|---|---|
| Vote gốc | 39/91 = 43% | 33/91 = 36% | 19/91 = 21% |
| Bỏ opus | 43% (đổi 3 ngày) | 36% (đổi 3) | 20% (đổi 3) |
| Bỏ gpt-5.4 | 43% (đổi 16) | 36% (đổi 2) | 22% (đổi 16) |
| Bỏ cả hai | 44% (đổi 19) | 35% (đổi 6) | 21% (đổi 18) |

→ **Cắt gần như VÔ HẠI cho official vote** (dao động ±1 ngày/91). NHƯNG 3 điểm ngược:
1. Tiết kiệm tuyệt đối NHỎ: ước ~$6-9/tháng (opus) + $2-3/tháng (gpt-5.4) — hệ đang chạy 94 call/30d/model, 4-6k tokens/call.
2. Cả hai đang nằm trong **roster lane đo hằng ngày** (budget-selector MT 14/14 ngày, MN 15/15; K11a/K15 selector dùng top-8/10 kể cả shadow) → cắt giữa cửa sổ đo K11a/K15 = trộn biến.
3. Opus là **voter chất lượng nhất khi lên tiếng**: những lần opus vote cho số top1, số đó trúng 46% — cao nhất bể (trung bình ~30%).

- **3 lựa chọn cho anh:** (a) **DỜI đến 19/07** quyết 1 lần cùng CP-R4 sau khi K11a (16/07) + K15 (17/07) chốt — EM KHUYẾN NGHỊ; (b) cắt ngay; (c) HUỶ checkpoint (chấp nhận ~$10/th để giữ nguyên bể). Anh chỉ cần trả lời a/b/c.

## 3. Checkpoint GLM 5.1 vs 5.2 (hạn 14/07 — trễ 1 ngày, em tự chạy)

9 ngày song song (06→14/07, 27-28 row/model):

| Model | Top1-lô | Top2-any | EMPTY | Tokens/call | Giá |
|---|---|---|---|---|---|
| glm-5.1 | 10/26 = 38% | 62% | 1 lần | 6.0k | $0.6/M |
| glm-5.2 | 10/27 = 37% | 63% | 0 | 4.9k | $1.5/M |

→ HOÀ accuracy; 5.2 ổn định hơn (không ngày trống, ít token). Chênh phí ~$0.4/tháng.
**Đề xuất: retire `glm-5.1`, giữ `glm-5.2` — làm tại mốc 19/07** (không đổi roster giữa cửa sổ đo K15 vì glm-5.1 đang trong budget-selector MN/MT).

## 4. Gói hướng cải tiến nâng dự đoán TỪ DB/LIVE (xếp theo tiềm năng × độ sạch bằng chứng)

| # | Hướng | Bằng chứng DB/live | Mốc quyết |
|---|---|---|---|
| 1 | **MB selector-trio → K16 promote** (thay official MB bằng picks SEL_BASE/DEDUP/RECENCY nếu giữ phong độ) | Forward shadow 6 ngày: trio BT **3/6=50% +3.4M** vs official MB BT 1/6 (~15% nền 60d) | **23/07** (đủ 14d) |
| 2 | **MB pool-full 17:50** (P1B trên) | K11a-era lệch inline-vs-lane 2/6 ngày; lane dùng đúng pool thuật toán ký | Anh gật là làm |
| 3 | **K11a MB chốt 16/07, K15 MT chốt 17/07** — quyết champion/challenger bằng số | K15 forward 5d: challenger 2/5 BT vs champion 0/5; K11a 6d: 1/6 vs 1/6 (P&L challenger nhỉnh) | 16-17/07 |
| 4 | **MT lệch pool** — đo đủ 14 ngày rồi mới đụng schedule/shadow-parallel | 5 ngày: 3 lệch, P&L hoà — chưa đủ kết luận | **24/07** |
| 5 | **MN GIỮ NGUYÊN** | V10640 override forward 60d net +2 ngày; vote MN 43-45% cao nhất hệ; ứng viên AI-cluster dưới chuẩn (+5d/137 — không đáng) | — |
| 6 | **Housekeeping roster 1 LẦN 19/07:** CP-L6 (nếu ký) + retire glm-5.1 + CP-R4 | Mục 2-3 trên | 19/07 |

Nguyên tắc chung em giữ: mọi thay đổi output đều đi qua cơ chế champion-challenger có số forward (như K11a/K15 đã làm), không đổi nhiều thứ cùng lúc, mỗi thay đổi 1 phiên riêng đủ chuỗi governance + rollback flag.

## 5. An toàn

- Phiên này 100% READ-ONLY: chỉ SELECT trên DB sync local; không sửa code runtime, không deploy, không restart.
- Hash 4 bảng (predictions/final_bundles/lottery_results/model_daily_eval): chỉ tăng trưởng tự nhiên trong ngày.
- `/du-doan` 15/15 và lane 20/20 không bị ảnh hưởng.
