# V10813 — KIỂM TRA TOÀN DIỆN ĐẦU NGÀY 17/07/2026 (READ-ONLY)

**Owner 09:18:** "đầu ngày rồi em, em kiểm tra toàn bộ, toàn diện dùm anh đi."

Phiên 100% read-only: 0 file code VPS đổi, 0 restart, 4 bảng official không đụng. 11 probe `_v10813_*.py` chạy từ local qua SSH.

---

## 1. KẾT QUẢ QUAN TRỌNG NHẤT: KEY SWAP V10812 → **LIVE_VERIFIED** ✅

Chuỗi sáng MN 17/07 chạy **SẠCH 100% trên bộ key mới** (thay đêm qua 23:36):

| Hạng mục | Kết quả |
|---|---|
| Chuỗi MN 04:00-04:31 | **26/26 model** (official 15 + shadow 11) — xong sớm hơn mọi ngày (~04:45 trước đây) |
| Bundle official MN | Chốt 04:18 — BT 63, lô2 [63, 34], 15 model, consensus strong |
| Journal từ restart 23:36 | **0 error, 0 lỗi 401/403** |
| Call theo hãng (03:55-05:05) | Tất cả HTTP 200: Anthropic ×4 · OpenAI ×2 · DeepSeek ×2 · Google ×4 (**gemini-3.5-flash + gemma-4-31b lần đầu chạy live trên key AQ mới**) · OpenRouter ×8 (đủ cohort: gpt-5.5, oss-120b, qwen3-max-thinking, qwen3.7-max, glm-5.1, glm-5.2, kimi-k2.5, grok-4.20) |
| **Bằng chứng tiền (quyết định)** | Key OpenRouter **MỚI**: usage $0.000 → **$1.541**. Cả **6 key OR CŨ ĐỨNG YÊN** đúng số đêm qua (GPT55 $71.917 · GROK $36.308 · chung-cũ $25.384 · KIMI $10.620 · QWEN3MAX $8.593 · OSS $0.924) → không còn call nào rơi vào key cũ |

### → Anh REVOKE được NGAY:
- **NHÓM A** (model đã nghỉ): Qwen3.6 Plus, Qwen3 Coder, Cohere Rerank.
- **NHÓM B** (đã verify sạch): 6 key OpenRouter cũ + OpenAI cũ + Anthropic cũ + DeepSeek cũ ×2 + Google shadow cũ (AIzaSyCmiW…).
- **TUYỆT ĐỐI GIỮ 2 key Google cũ** (DB AIzaSyDz…sPc0 + env AIzaSyB4…ITaY) — gemini-2.5-flash/pro chỉ sống trên project cũ (Google chặn project mới); lộ trình thoát bàn tại CP-L6 19/07.

---

## 2. SỨC KHỎE TOÀN HỆ SÁNG NAY

| Mục | Trạng thái |
|---|---|
| Service + health | active, HTTP 200; watchdog WATCHDOG_OK đến 09:45 |
| Self-check 11 bất biến | **10/11 PASS** — FAIL duy nhất = check-3 `retrain_OK_in_8d` (bệnh CŨ, fix subprocess V10800 đã deploy, model files thật 4.1 ngày tuổi; hàng OK đầu tiên kỳ vọng **CN 19/07 02:00**) |
| Budget C16 (V10804) | Đủ 3 miền 15-17/07, tên đài chuẩn sau V10810 (MT Thứ5 16/07 = Bình Định, Quảng Bình, Quảng Trị ✓) |
| Đài / station alert | STATION_INCOMPLETE = 0; check-11 shortcode PASS rows=0 |
| Lane sáng MN | 21 row (04:20-05:11): v10692 OK bt=63 khớp official; PROMPT_V2 A/B chạy 73.8s OK |
| Money board | 16/07 MB lock 17:56:32 ≥17:55 (fix V10794 ngày 3 giữ nhịp); 17/07 MN lock 08:19 |
| Panel /monitoring | Backend `compute_view()` đủ key: best_spots (4 phần tử) + rule_adoption + rule_routing + shadow_ab7; JS đã sống từ fix V10811 — **anh mở /monitoring xác nhận mắt 1 lần là khép** |
| Hạ tầng | Disk 67%, RAM OK, load 0.00 |
| Cron tối qua | 19:05 V10801 (+8 row) ✓ · 19:10 V10803 (+3 row) ✓ · 19:15 scorer A/B (15 chấm) ✓ · retrain guard "models fresh" ✓ · system_health 16 checks ALL OK ✓ |

**Bài học ghi playbook:** `scheduler_logs.log_time` lưu **UTC** (chuỗi MN 04:00 VN nằm ở 21:00 UTC hôm trước) — sáng nay suýt đọc nhầm "log dừng 02:45"; thực tế hệ sống bình thường.

---

## 3. CHECKPOINT ĐỌC HÔM NAY

### K15 MT d7 (đến hạn hôm nay) — CHALLENGER GIỮ
| Ngày | Champion | Challenger |
|---|---|---|
| 10/07 | 16 ✗ | 16 ✗ (lô2 có 85✓) |
| 11/07 | 94 ✗ (lô2 61✓) | **61 ✓** |
| 12/07 | 43 ✓ | **64 ✓** |
| 13-16/07 | ✗ ×4 | ✗ ×4 |
| **Tally BT** | **1/7** | **2/7** |

→ Challenger nhỉnh → **GIỮ**. Chuỗi thua hiện 4 ngày liên tiếp (quy tắc kill = 5, chưa chạm).

### K11a MB d8 — đối chiếu khớp số V10811
Champion-cũ BT **3/8** (98✓ 11/07 · 57✓ 15/07 · 16✓ 16/07) vs challenger-promote **1/8** (89✓ 13/07); 15+16/07 champion đúng bị promote thay (57→64, 69 thay 16) = net **−2 ngày**. Giữ lịch quyết: **trio 23/07 + agenda CP-L6 19/07** — không tự kill (n nhỏ).

### Shadow A/B V10809 — CP-S1 (18/07) ON TRACK
- Day-1 (16/07): **15/15 row, 0 lỗi, chấm đủ — B 8 vs prod 7** (any-hit).
- Day-2 (17/07): MN 5/5 row lúc 04:20, **0 lỗi trên key mới** (opus B=53 lệch prod=63; 4 model còn lại B=34). MT 16:48 + MB 17:42 chiều nay; chấm 19:15.

### Kết quả 16/07 (official): MN **WIN đôi** (BT 72 + lô2 [72,96]) · MT 40 ✗ · MB 69 ✗.

### Roadmap quét sáng
Không checkpoint sống nào quá hạn, trừ **CP-4.0** (roadmap CROSS_REGION, hạn 15/06) — phạm vi đã bị phủ bởi các quyết định sau (Cohere tháo V10789 · prune = CP-L6 · promote = K11a/K15 đang đo) → đánh dấu **FOLDED_INTO_CP-L6**, anh ack tại 19/07 là khép hẳn. CP-S1 18/07 = đúng lịch.

---

## 4. VIỆC CHỜ PHÍA TRƯỚC

| Khi nào | Việc | Ai |
|---|---|---|
| Ngay được | Revoke key NHÓM A + NHÓM B (mục 1) — **giữ 2 key Google cũ** | **Anh** |
| Ngay được | Quyết **B1**: hạ reasoning gpt-5.5 HIGH→default (code còn HIGH — sáng nay vẫn đốt trong $1.541; 1 dòng, tiết kiệm ~60% model này) | **Anh** |
| Hôm nay 16:4x + 17:4x | Vòng MT + MB đầu tiên trên key mới (kỳ vọng sạch như MN) — em theo dõi | Em |
| 18/07 | CP-S1 shadow A/B health chính thức | Em |
| **CN 19/07** | Retrain 02:00 + optimizer 03:00 qua subprocess lần đầu (khép check-3) + **CP-L6**: retire gpt-5.5 → grok-4.3 (B2) · retire glm-5.1 · CP-R4 · gemini-3.5-flash swap (EOL) · K11a đọc số · CP-4.0 ack | Em + Anh |
| T2 21/07 | Self-check cron có check-11 lần đầu (08:10) | Em |
| 23/07 | CP-S3 tổng kết 105 cặp A/B + trio selector 14d | Em |

---

*Phiên V10813 — read-only, no-deploy. Private commit: xem `docs/AUTOMATION_STATE.json` seq 274. Mọi giá trị key trong báo cáo đã mask.*
