# BÁO CÁO V10804 — TRUY NGUỒN 51/19/92/17 + SANDBOX DI CƯ SỐ TRƯỢT + FIX C16 BUDGET MB + AUDIT PROMPT 3 MIỀN

- Ngày: 2026-07-15 (tối muộn, sau chu kỳ live)
- Phiên trước cùng ngày: V10803 (chase-bias shadow)
- Trigger: owner 19:07 — 5 nghi vấn (51, 19, 92+3card, lane test lỗi?, MN/MT/prompt) + yêu cầu "kiểm tra phân tích tổng lực cực mạnh hơn nữa" + cảnh báo thay API khi cắt model.

## 1. TRUY NGUỒN 4 CON SỐ (bằng chứng DB, sync 18:39)

### Số 19 — "trượt cả MN và MT lại nổ ở MB"
- MN 15/07: 4 model dự 19 trong top2 (gemini-2.5-flash, gpt-5-mini, gpt-5.4 @04:16 auto_daily; gpt-oss-120b @04:32 shadow) + official lô2 = [63, **19**] → 19 KHÔNG nổ MN.
- MT 15/07: **12 model** dự 19 pos1 (claude-sonnet, combo-super, deepseek-reasoner, deepseek-v4-pro-real, gemini-2.5-flash/pro, glm-5.1/5.2, gpt-5-mini/5.4/5.5, grok @16:36-16:52) + official BT=19 → 19 KHÔNG nổ MT.
- Nguồn gốc 19 tại MT = **CHASE**: 19 nổ MN ngày 14/07 → pool đuổi.
- MB 15/07: **KHÔNG model nào dự 19 cho MB** — mà ĐB MB = **19**. Đây chính là pattern H3/H5 bên dưới.

### Số 92 — "AI đoán 92 trúng MB dựa vào yếu tố nào?"
- 5-6 model dự 92 cho MB: claude-opus-4-6 (64,92), claude-sonnet-4-6 (64,92), gemini-2.5-pro (92,49), deepseek-v4-pro-real (92), glm-5.2 (64,92).
- Reasoning từ trace (analysis_text): **92 ∈ g8_tails ngày hôm trước** ["69","42","**92**","98",…] + frequency 2 lần + nằm trong cụm dao động — tức là tín hiệu D-1 thuần, KHÔNG phải đuổi số vừa nổ. Lô2 MB 92 NỔ ✓.
- **"3 card trong hình"** = lane multidir (v10692): BT 64 / phụ1 92 / phụ2 12, "tạo lúc 17:52". Phụ1 92 đến từ method **MB_DIR2_LO2_V1** (per-position). Lịch sử method này: MB pos2 chỉ **11/42 = 26%** (riêng T4: 2/6) — hôm nay trúng vì 92 là tín hiệu thật của pool, KHÔNG phải vì method per-position ổn định. Đánh giá: chưa đáng tin cậy làm phương pháp độc lập.

### Số 51 — "trượt MB hôm qua, hôm nay nổ liên tục MN tới MT"
- Đã truy vết V10803: 13/07 nổ MN → 14/07 16 model đuổi cho MB (BT=51, trượt) → 15/07 nổ MN+MT nhưng không ai dự cho MB.
- BỔ SUNG V10804: hôm nay lane MB vẫn có 51 — **MB_HYBRID_V1 BT=51** và **MB_ADAPTIVE_EXPLOIT_V1 51+36** (lag-1 exploit: contributions gemini-flash/pro factor ~1.06 "yesterday_bt=51") → trượt MB. /choi MB songthu [64, 51] (leg AE) trượt cả 2. AE là lane test, không đụng official.

### Số 17 — "/choi chắc may mắn hay sao mà 17 về không rõ"
- money_board_daily_lock MT 15/07 = ["17","19"], method `MT_HYBRID_V1 + MT_STRENGTH_WEIGHTED_V52_5_2`, lock 16:40:54 (trước xổ 17:15) → **17 NỔ MT**.
- 17 = **BT official MT ngày 14/07 vừa trượt** → MT_HYBRID_V1 đánh LẠI số vừa trượt. KHÔNG phải may mắn thuần: khớp đúng pattern H1 (dưới). MT_HYBRID_V1 lịch sử BT 29/68 = **43%** (68 ngày) so official MT 30d chỉ 20%.

## 2. SANDBOX DI CƯ — kiểm mọi giả thuyết owner (120 ngày, null HOÁN VỊ 4000 sim)

Phương pháp: giữ nguyên picks, xáo ngày-kết-quả cùng miền (uniform + weekday-matched + day-block) — chuẩn hơn "random số" vì pick của hệ dồn vào đuôi phổ biến.

| Giả thuyết | Kết quả thật | Null | p | Kết luận |
|---|---|---|---|---|
| **H1** đánh lại BT vừa trượt, cùng miền D+1 — **MT** | 34/74 = **45.9%** | 34.8% | **≈0.027** | Có tín hiệu (case 17) |
| H1 — MN | 34/66 = 51.5% | 43.1% | ≈0.10 | Yếu |
| H1 — MB | 21/98 = 21.4% | 23.7% | 0.73 | KHÔNG |
| **H2** BT MB trượt → MN/MT hôm sau (vụ 51) | MN 40.8% / MT 41.8% | 43.0% / 34.8% | 0.70 / 0.11 | **KHÔNG edge — 51 vẫn là ảo giác** |
| **H3** BT MT trượt chiều → MB tối cùng ngày | 25/75 = 33.3% | 24.2% | ≈0.048 | Có tín hiệu (case 19) |
| **H3b** MỌI pick MN+MT trượt → MB tối | 130/423 = **30.7%** | 24.3-24.9% | **≈0.013-0.016** | Mạnh nhất phiên |
| H5 số trượt CẢ MN và MT → MB tối | 50/166 = 30.1% (1 lần trúng thẳng ĐB = vụ 19) | 24.3% | ≈0.053 | Cùng chiều H3 |
| H4 ĐB miền X → miền Y hôm sau (9 cặp) | ±5pp quanh baseline | — | — | KHÔNG dùng được |

**Đánh giá trung thực:** phiên này chạy ~25 test ngầm → p 0.03-0.05 chưa vượt ngưỡng đa-so-sánh. H3b (p≈0.013, 423 legs, causal sạch vì MN xổ 16:34 / MT 17:30 TRƯỚC MB chốt 17:54) là ứng viên duy nhất đáng đo tiếp. **KHÔNG promote** — đã nhúng khối `migration` vào view `/api/admin/chase-bias` + mục "🔁 DI CƯ SỐ TRƯỢT" trong panel /monitoring (đọc LIVE từ bảng official, không bảng mới, không cron mới). Ngưỡng: sau ≥30 ngày, H3b giữ ≥+5pp và p<0.01 → trình owner lane experiment `MB_EVENING_MISS_V1`.

## 3. BUG THẬT ĐÃ FIX — C16 BUDGET MB CHẾT ĐÓI TỪ 04/06 (= "lane test lỗi output")

- Screenshot owner: cột TEST CHALLENGER /du-doan-test toàn "Chưa có dữ liệu — Bundle test chưa sẵn sàng", header "Primary: (none)".
- Root cause chuỗi: API đòi **FULL_BUDGET_PRIMARY = row đúng 20 model** (`MB_ADAPTIVE_BUDGET_SELECTOR_V1`) → row này do C16 budget materializer tạo → C16 chỉ chạy trong nhánh `existing==0` của trigger */5 phút → **từ 04/06 các lane mới (OUTPUT_V1/DIR* 17:55, HYBRID/AE same-day refresh 17:35, screen lanes 18:20…) ghi `du_doan_test_bundles` TRƯỚC tick đầu tiên có final_bundle MB** → `existing>0` vĩnh viễn → budget không bao giờ chạy cho MB.
- Bằng chứng: `du_doan_test_model_budget_daily` MB dừng 03/06 (id 95) trong khi MN/MT có row hằng ngày (id 177/178 hôm nay); log "start MB / done MB: budget_selected=20" lần cuối 03/06 17:40; MB 15/07 chỉ có log "same_day_lose_refresh".
- **Fix (scheduler.py):** thêm `budget_done` đọc thẳng bảng budget; nhánh `existing>0` giờ bù `budget_catchup` (chỉ C16+ABS row, không đổi thứ tự job nào khác). MN/MT không đổi hành vi (budget đã chạy nhánh start như cũ).
- Gap 04/06→15/07 ghi nhận **measurement gap** — KHÔNG backfill (pick as-of không tái tạo trung thực).
- Verify 16/07 ~17:40: log `budget_catchup MB` + row budget MB + ABS preview row + TEST CHALLENGER có số.

## 4. AUDIT PROMPT 3 MIỀN (dựng nguyên văn prompt 16/07 bằng đúng code production)

- Cấu trúc chuẩn cả 3 miền: header đúng miền/thứ/đài, nguồn D-1 dán nhãn ưu tiên, mined rules theo bucket miền×thứ, 3-layer mandate 12W/16W/4W, evidence table, ràng buộc miền cuối prompt, de-herd V10768 vẫn strip ranking (MN 8174→7049 chars, MT 7333→6224, MB 10843→9670).
- **Lỗi hygiene ĐÃ FIX:** header MT Thứ Năm hiện "Bình Định, QB, QT, Quảng Bình, Quảng Trị" (5 nhãn cho 3 đài thật — rows 25/06 scrape tên tắt). Fix: alias QB→Quảng Bình, QT→Quảng Trị trong `station_identity.py` + dedup header qua canonical trong `gpt_analyzer.py`. Sau fix: "Bình Định, Quảng Bình, Quảng Trị" ✓.
- **TỒN ĐỌNG QUAN TRỌNG (input CP-L6):** khối "CHỈ SỐ ĐỊNH LƯỢNG (PYTHON TÍNH SẴN)" dùng CHUNG 129 đuôi từ 9 đài (cả 3 miền D-1) → dòng "🎯 ĐỀ XUẤT PYTHON: 96, 57" Y HỆT NHAU trong prompt MN/MT/MB. Đây là nguồn HERDING XUYÊN MIỀN còn sót sau V10768 (giải thích herd share tăng MT 45→57%, MB 60→65%). Sửa = regime change prompt → cần owner ký tại CP-L6: lọc metrics theo miền target + A/B shadow trước.
- **"Với prompt đó nay em dự ra số gì" (16/07, đọc tay từ data trong prompt, không gọi API):**
  - MN: **77** chính (rule candidate CONV×2 duy nhất của bucket MN/T5, boost 0.100), 16 phụ; số Python 96/57 GIẢM TIN vì là đề xuất chung 3 miền.
  - MT: bucket yếu (FALLBACK, không READY_STRONG) — prompt ép dựa rule Bắc Ninh D-1 (91.7% 12W) nhưng không có bảng tra trực tiếp G1+G7 → model phải tự map từ KQ MB 15/07; điểm yếu ghi nhận.
  - MB: **69** chính (CONV×2 + READY_STRONG Khánh Hòa MT-D1 75% 12W + Sóc Trăng MN-D1), 57/97 phụ.

## 5. PROMPT ĐỔI (V10768 de-herd 02/07) CÓ CẢI TIẾN KHÔNG? — trả lời trực tiếp

- MT pool top2 any-hit: 55.8% (15d pre) → **56.2%** (14d post) — **KHÔNG giảm**. Cảm giác "tín hiệu MT giảm mạnh" = ngày 15/07 xấu cục bộ (5/25 model trúng), không phải trend.
- Official BT: MT 13%→29%, MB 7%→14%, MN 40%→29% (MN giảm — cùng chiều với chuỗi MN dưới baseline).
- **Cảnh báo:** herd top-vote share TĂNG (MT 45→57%, MB 60→65%) dù đã gỡ ranking → 2 nguồn tụ còn lại: chase-bias (đo V10803) + khối định lượng chung (mục 4).
- Per-model MT (input trực tiếp cho CP-L6 cắt/thay API):
  - TĂNG: claude-opus-4-6 +32pp (86%), qwen3-max-thinking +33pp (73%), deepseek-v4-pro-real 64%, gpt-oss-120b +14pp, grok +11pp.
  - GIẢM: gemini-2.5-flash −18pp (29%), combo-super −16pp, claude-sonnet −11pp, gpt-5-mini −11pp.
  - Khuyến nghị: ứng viên thay API đợt cắt = **gemini-2.5-flash, gpt-5-mini** (yếu bền ở MT); giữ opus/qwen-max/deepseek-pro-real.

## 6. MN "ngập tín hiệu nhưng output tệ" + MT model trượt toàn vùng 15/07

- MN: đúng số liệu — official BT 30d 11/31 = 35% < baseline bao-lô 43%. 15/07: **15/25 model có số trúng** (99×4, 93×3, 74×3, 16×3…) nhưng total chốt 63 (9 phiếu — trượt): total-vote đang thua tín hiệu lẻ. Selector shadow K10/K13 (V10789) + chase-bias + migration đo đủ 3 mặt; không đổi selector giữa cửa sổ đo (còn ~8 ngày đến review 29/07).
- MT 15/07: 5/25 model trúng (toàn no-token: combo-no-token/rf/xgb 21, smart-ensemble/smart-ml 42) — AI chain trượt cả dàn vì đuổi 19. Lane MT (HYBRID 17) tốt hơn official đúng như owner thấy.
- MB 15/07: 8/25 model trúng (92×5, 47×2, 86); official lô2 ăn 1 chân (92).

## 7. DEPLOY + AN TOÀN

- `_v10804_deploy.py`: backup remote `/root/backups/v10804_pre/` + local `backups/v10804_pre/` (5 file) → upload `scheduler.py`, `gpt_analyzer.py`, `station_identity.py`, `_v10803_chase_bias_shadow.py`, `monitoring.html` → py_compile OK → restart `active` → smoke health=200, /choi=401, chase-bias=401, /monitoring=401 → view migration OK → journal sạch.
- **Hash 4 bảng official pre = post IDENTICAL**: predictions 10122/3a18c24b · final_bundles 414/0e68ae9c · lottery_results 15081/1a1820b1 · model_daily_eval 9908/97c981c1.
- ZERO đụng /du-doan, final_bundles writer, selector, T-chốt, nội dung prompt production (chỉ header đài chính xác hơn).
- Rollback: `cp /root/backups/v10804_pre/*` về chỗ cũ + restart.

## 8. VIỆC CHỜ (đăng ký lịch)

| Mốc | Việc |
|---|---|
| 16/07 ~17:40 | budget_catchup MB lần đầu → TEST CHALLENGER MB có số |
| 16/07 | prompt MT header 3 đài; cron 19:05/19:10 lần 2 |
| 29/07 | review selector shadow 14d (MN total-vote) |
| ~16/08 | đọc ngưỡng chase-bias + migration (H3b ≥+5pp & p<0.01 → trình lane MB_EVENING_MISS_V1) |
| CP-L6 | trình: khối định lượng per-miền + cắt/thay API gemini-2.5-flash, gpt-5-mini |
