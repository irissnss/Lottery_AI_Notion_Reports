# BÁO CÁO TỔNG V10788 — AUDIT TOÀN BỘ MỐC TỔNG HỢP (09/07/2026 sáng)

## 1. Câu hỏi của owner (09/07 09:26)

> "Cái vấn đề mà số miền trước ra miền sau và số trật hày hôm qua hay ra lại ngày hôm sau là anh đang nói với ML có lẻ đang tổng hợp sớm hoặc muộn với các mốc không hợp thời điểm nên thấy có vẻ như thế ML MT dạo này tổng hợp tệ hăn kiểm tra toàn bộ các mốc xem mốc nào ổn định và có hoạt động đúng như thiết kế không? Từ các vấn đề anh đề cập em đào bới soi xét đúc kết và đề xuất giúp a hướng xử lý an toàn chính xác hơn đi em."

Nghi vấn: ML tổng hợp SỚM hoặc MUỘN với các mốc không hợp thời điểm → yêu cầu kiểm tra TOÀN BỘ mốc.

## 2. Phương pháp

7 probe READ-ONLY chạy trên DB sống VPS (không đổi 1 byte official):
`_v10788_milestone_audit.py` (1-6) + `_v10788_persistence_probe.py`. Đối chiếu chéo: `app_settings`, `predictions.created_at/run_source/pre_result_numbers`, `final_bundles.source_predictions_json` (score breakdown), `training_history`, files model mtime, bảng tín hiệu V66.

## 3. BẢN ĐỒ MỐC — thiết kế vs thực tế 7 ngày (02-08/07)

| Mốc | Thiết kế | Thực tế đo được | Kết luận |
|---|---|---|---|
| ML `auto_daily` | 04:00, data D-1 | 04:00 đúng 8/8 ngày, cả 3 miền (`PRE=None`) | ✅ đúng thiết kế |
| Chain MT (AI token) | sau MN scrape 16:30 | rows 16:35–16:41 | ✅ |
| Chain MB (AI token) | sau MT scrape 17:30 | rows 17:30–17:42 | ✅ |
| Rerun ML post-MN → MT | TẮT từ V10766 (01/07) | 0 row rerun MT sau 01/07 | ✅ tắt đúng |
| Rerun ML post-MT → MB | 17:30 `rerun_post_mt` | 17:30–17:31 đủ 4 ML/ngày | ✅ chạy đúng — nhưng VÔ DỤNG (mục 5) |
| T-10 chốt bundle | 15:45/16:45/17:45 | bundle tạo 04:17-19 (MN) / 16:38-42 (MT) / 17:33-37 (MB) — chain-completion; T-10 regen không đổi nội dung | ✅ |
| Freeze | :55 mỗi miền | model về sau T-10 đều `shadow_auto_eval`, late=1 chỉ 2 ca đúng ca muộn | ✅ |
| Retrain ML | Chủ nhật 02:00 | files mtime 05/07 02:00–02:02 + `training_history` 05/07 đủ 3 miền × 4 model | ✅ đúng lịch |
| Dedupe phiếu | 1 row/model/ngày/miền | 0 duplicate trong 14 ngày | ✅ không đếm phiếu 2 lần |

**KẾT LUẬN 1: KHÔNG có mốc giờ nào chạy sai thiết kế. Không có bug timing.**

Lưu ý quan trọng: 9-10 model/ngày về SAU T-10 tại MT (16:46–17:19: qwen3-coder, deepseek-v4-pro, gemini-3.x, glm-5.x, gpt-5.5, kimi, gemma...) — toàn bộ là shadow, KHÔNG có quyền bầu official → không có race bug. NHƯNG đây là trần cứng: nếu muốn promote model shadow đang nóng (gemini-3.1-pro 7d 75%) vào voter MT thì giờ về của nó KHÔNG KỊP mốc chốt.

## 4. MỐC HỎNG THẬT = CẤU TRÚC PHIẾU (không phải giờ)

Bằng chứng từ `score_breakdown` bundle MT 08/07:
- BT=59 thắng với score 0.1946 = **6 phiếu ML cùng lane `auto_daily` 04:00** (combo-no-token, random-forest, xgboost, meta-learning, smart-ml, smart-ensemble).
- Số 41 của AI tươi (gpt-5.4, gemini... chạy 16:3x, ĐÃ thấy kết quả MN cùng ngày) chỉ đạt 0.1418 → thua.
- Nghĩa là: official MT = "consensus ML lúc 04:00 sáng" — mang thông tin CŨ NHẤT hệ thống nhưng thắng phiếu vì 6-8 sibling models chụm 1 số, còn 7 AI tán loạn mỗi con 1 số.
- 09/07: khối ML lại chụm 59/65/84 — modal 59 = đúng số official vừa THUA hôm 08/07 (59 từng về 06/07, ML đuổi số cũ 3 ngày).

Đây chính là cảm giác "ML tổng hợp tệ hẳn" của owner: bloc không tệ đi (form 3 tuần: 29% → 34% → 32%), nhưng official bám 100% modal của bloc → bloc sai 1 ngày = chết chùm (07/07 63✗, 08/07 59✗).

## 5. MỐC "TỔNG HỢP MUỘN" (rerun sau KQ miền trước) — VÔ DỤNG CÓ SỐ LIỆU

30 ngày, so `pre_result_numbers` (mốc sớm) vs `main_numbers` (mốc muộn) của ML:
- **MB rerun 17:30 (sau KQ MT):** 139 lần đổi số → đổi-thành-TRÚNG 21 vs đổi-thành-TRƯỢT 21. **HOÀ TUYỆT ĐỐI.** Hit mốc sớm 20% = hit mốc muộn 20%.
- **MT (data lịch sử trước khi tắt V10766):** 113 đổi → +25/−24. Nhiễu. Quyết định tắt rerun MT của V10766 là ĐÚNG.
- Nguyên nhân gốc: AUC retrain 05/07 — MT 0.55/0.56, MN 0.48/0.51, **MB 0.497/0.499 = đúng nghĩa tung xu**. Model AUC ~0.5 thì cho thêm data tươi cũng chỉ re-roll xúc xắc.

**KẾT LUẬN 2: "tổng hợp sớm hay muộn" KHÔNG phải biến số quan trọng với ML hiện tại — sớm và muộn cho hit y hệt nhau. Vấn đề là chất lượng tín hiệu ML (AUC≈0.5) + cách phiếu của chúng được đếm.**

## 6. MỐC ECHO — "số miền trước ra miền sau, số trật hôm qua ra lại" CÓ THẬT KHÔNG?

Đo 60 ngày, chỉ tính số official đã THUA (đúng định nghĩa AE):

| Flow | Tỷ lệ ra lại | Nền (đoán mò) | Chênh | Kết luận |
|---|---|---|---|---|
| Lag-1 MN (thua hôm trước → ra hôm sau) | 55% (18/33) | 43% | **+12pp** | THẬT, mạnh |
| Lag-1 MT | 41% (17/41) | 35% | +6pp | THẬT, vừa |
| Lag-1 MB | 18% (9/50) | 24% | **−6pp** | NGƯỢC — số cũ MB KHÔNG quay lại |
| Same-day MT→MB (miền trước ra miền sau) | 31% (13/42) | 24% | **+7pp** | THẬT |
| Same-day MN→MT | 36% (12/33) | 35% | ≈0 | không có edge |
| Same-day MN→MB | 18% (6/33) | 24% | −6pp | ngược |

Đối chiếu bảng tín hiệu V66 (anchor 08/07): BOOST đang bật đúng các flow dương (MN lag1 factor 1.12-1.13, MT lag1 1.07-1.08, MT→MB sameday 1.07, MB lag3 1.09) và **KHÔNG boost MB lag1 (flow âm)** — khớp 100% với audit độc lập này.

**KẾT LUẬN 3: Trực giác owner đúng NHƯNG theo miền: "số trật hôm qua ra lại" có thật ở MN/MT (không phải MB); "miền trước ra miền sau" chỉ có thật ở MT→MB. Bảng mốc V66/AE đang đo và khai thác ĐÚNG THIẾT KẾ các flow này.**

## 7. CHASING — model nào đang "đuổi số cũ" và trả giá

30 ngày, top1 ∈ tails hôm trước = "đuổi":

| Miền | Nhóm | Hit khi ĐUỔI | Hit khi KHÔNG đuổi | Tỷ lệ đuổi |
|---|---|---|---|---|
| MN | AI core | 46% | 40% | 70% ngày |
| MN | ML | 45% | 39% | 31% |
| MT | AI core | 33% | 37% | 48% |
| MT | ML | 36% | 34% | 14% |
| **MB** | **AI core** | **17%** | **31%** | **47%** |
| MB | ML | 31% | 22% | 6% |

- MN: đuổi CÓ LỢI (khớp echo +12pp) — mốc lành mạnh.
- **MB: AI đuổi số hôm trước 47% số ngày và hit chỉ 17% vs 31% khi không đuổi — TỰ SÁT.** MB có động lực học ngược (số cũ không quay lại) nhưng gần nửa phiếu AI vẫn chơi kiểu đuổi.
- ML lặp top1 của chính nó: MB 0/7 hit khi lặp, MT 3/13 (23%) — lặp số = chết.

## 8. Panel mới đã deploy — ⏱ MỐC & NHỊP

- Module: khối `milestones` trong `_v10773_three_layer_scoreboard.py` (READ-ONLY, compute-on-the-fly).
- UI: panel ⏱ MỐC & NHỊP mỗi miền trong SO GĂNG 3 TẦNG `/monitoring` (auto-refresh 60s sẵn có): lag1-echo 60d vs nền · cross same-day theo thứ tự xổ · chase AI/ML (cảnh đỏ "ĐUỔI LÀ HẠI" khi chênh ≥10pp) · rerun-ML ±  · dòng nhịp hệ thống (retrain cuối + giờ tạo bundle hôm qua).
- Deploy 10:07 09/07: sandbox PASS → backup local `backups/v10788_pre/` + VPS `.bak_v10788` → restart ngoài cửa sổ chain (guard SAFE) → health 200, admin 401 → **hash 4 bảng pre/post IDENTICAL** (predictions efebca79 · final_bundles 2e85228e · lottery_results 76af5ec6 · model_daily_eval 4fc6e4a0).
- DIAGNOSTIC-ONLY: không đổi số official, không đổi selector, không đổi /du-doan.

## 9. ĐÚC KẾT + ĐỀ XUẤT HƯỚNG XỬ LÝ AN TOÀN

Chuỗi nguyên nhân đầy đủ sau 3 ngày đào (V10787 A-F + V10788):

1. Mốc giờ: SẠCH — không sửa gì.
2. Official MT/MB kém vì: (a) khối ML 04:00 chụm số như 1 phiếu khổng lồ mang data cũ + AUC≈0.5; (b) trọng số BT-rate 30d NGUỘI (meta-learning 0/7 tuần này vẫn giữ ghế; claude-opus 6/7 bị đè); (c) MB: cả doctrine 4-ML lẫn thói quen chasing của AI đều ngược với động lực học MB.
3. AE/lane đang là mặt có edge thật (z=+1.78) nhờ khai thác đúng mốc echo dương.

**Đề xuất (tất cả SHADOW trước, không đụng official khi chưa ký):**

| ID | Đề xuất | Bằng chứng | Rủi ro |
|---|---|---|---|
| **K13 (MỚI)** | `RECENCY_WEIGHT_V1` shadow lane 14 ngày: trọng số vote = 7d×60% + 30d×40% (thay BT-rate 30d thuần) | Phản chứng V10787-E: RECENCY 43% vs ACTUAL 29% (14d); V10788: ghế vote nguội là mắt xích yếu nhất | Zero — shadow-only |
| K10 (chờ ký từ 08/07) | `ML_BLOC_DEDUP_V1` shadow: khối ML sibling đếm 1.5 phiếu thay 5-6 phiếu | 08/07 + 09/07: bloc chụm 59 hai ngày liên tiếp, 6 phiếu như 1 | Zero — shadow-only |
| K11a (chờ ký từ 08/07) | Promote-candidate `MB_OUTPUT_V1` cho BT official MB sau khi cửa sổ doctrine đóng (10/07) | 60d +32.9M BỀN vs official −5.2M; V10788 củng cố: MB chasing âm, doctrine mù | Cần chữ ký + 1 tuần shadow đối chiếu |
| K9 (chờ ký từ 08/07) | `HERD_FADE_V1` shadow: né top1 khi bầy ≥10 | bầy ≥10 tại MT hit 12% | Zero — shadow-only |

3 shadow (K9/K10/K13) chạy song song độc lập được — sau 14 ngày có bảng so 4 selector (actual vs 3 shadow) cùng thước, lúc đó mới bàn đổi official bằng số liệu, không bằng cảm giác.

## 10. Files & bằng chứng

- Probes: `web/backend/_v10788_milestone_audit.py` … `audit6.py`, `_v10788_persistence_probe.py` (private repo).
- Deploy: `web/backend/_v10788_deploy.py`; module `_v10773_three_layer_scoreboard.py` + `web/frontend/monitoring.html`.
- Docs: `CHANGELOG.md` (V10788), `docs/CURRENT_TRUTH_SSOT.md`, `docs/FOLLOW_UP_TRACKER.md` (FU-V10788-MILESTONE-AUDIT), `docs/AUTOMATION_STATE.json` (seq 247).
- Commit private: `8064514`.
