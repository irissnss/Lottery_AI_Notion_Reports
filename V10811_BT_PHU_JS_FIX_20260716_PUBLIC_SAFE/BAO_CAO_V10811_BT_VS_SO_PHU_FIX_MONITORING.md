# BÁO CÁO V10811 — "TÍN HIỆU TRÚNG ĐA PHẦN NẰM Ở SỐ PHỤ?" + PHÁT HIỆN /monitoring CHẾT JS 7 NGÀY + VERIFY TOÀN BỘ VẤN ĐỀ TREO

- Ngày: 2026-07-16, phiên tối 18:43 → 20:1x (giờ VN)
- Người yêu cầu: Owner ("Tiếp tục ngày buồn em nhỉ, có MN đỡ đỡ xíu. Em xem lại dùm anh tín hiệu trúng đa phần nằm ở số phụ không thế em? kiểm tra đơn model số phụ và bạch thủ luôn em, showdow nay sao rồi? kiểm tra toàn diện các vấn đề đang treo luôn xem nào em")
- Phạm vi: đo BT vs số phụ toàn hệ (26 model × 3 miền), shadow A/B day-1, quét pending, fix bug UI nghiêm trọng, panel mới.
- An toàn: KHÔNG đụng `/du-doan`, lane, prompt production, selector. Hash 4 bảng official PRE=POST IDENTICAL.

---

## 1. TRẢ LỜI CÂU HỎI CHÍNH: "TRÚNG ĐA PHẦN NẰM Ở SỐ PHỤ?"

Cách đo: mỗi model output 2 số — vị trí 1 = bạch thủ (BT), vị trí 2 = số phụ. Chấm bao-lô toàn miền (mọi giải, mọi đài của miền trong ngày).

### 1a. Hôm nay 16/07 (số liệu live VPS)

| Miền | Official | Đơn model trúng BT | Chỉ trúng số phụ | Nhận định |
|---|---|---|---|---|
| MN | BT=72 **WIN**, lô2 [72,96] **WIN** | **14/26** (6/7 AI official) | 7 | Không phải "đỡ đỡ" — **thắng thật**, tín hiệu nằm ở số CHÍNH |
| MT | BT=40 trượt cả bộ | 3/25 | **12** | Đúng cảm giác owner — tín hiệu có nhưng nằm VỊ TRÍ PHỤ |
| MB | BT=69 trượt cả bộ | 3/25 (toàn shadow) | 5 | Ngày tệ thật: 7 AI official trượt trắng 0 BT 0 phụ |

- MB: chỉ nhóm shadow cứu — gemini-3.5-flash + glm-5.2 BT=16 ✔, qwen3-max-thinking BT=46 ✔.
- Số **72 nổ MN 16:15 xong nổ luôn MT 17:15** — 5 model MT ăn 72 ở vị trí phụ. Đúng chiều routing MN→MT dương đã đo V10806/V10808.
- Lane `MT_ADAPTIVE_EXPLOIT` BT=19 **TRÚNG cả đôi [19,22]** trong khi official chọn 40 trượt.

### 1b. Trend 14 ngày (02–15/07, model_daily_eval — có phải quy luật không?)

| Miền | Nhóm | n | BT hit | Phụ hit | Nghiêng |
|---|---|---|---|---|---|
| MN | AI-OFF | 98 | 44.9% | 50.0% | cân (nhẹ phụ) |
| MN | AI-SHD | 136 | 51.5% | 42.6% | BT |
| MT | AI-OFF | 98 | 36.7% | 30.6% | BT |
| MT | **AI-SHD** | 137 | 29.2% | **38.0%** | **PHỤ** |
| MT | **ML** | 98 | 28.6% | **31.6%** | **PHỤ** |
| MB | AI-SHD | 127 | **29.1%** | 21.3% | BT |
| MB | ML | 98 | 16.3% | 17.3% | cân |

**KẾT LUẬN:** "Trúng đa phần ở số phụ" là **bệnh CỦA MT** (và của ngày 16/07), KHÔNG phải quy luật toàn hệ. MB thậm chí ngược lại (BT nhỉnh hơn phụ). Ý nghĩa: MT không thiếu tín hiệu — tín hiệu bị xếp **nhầm vị trí** (bệnh chọn-BT). Đây đúng là chỗ addendum per-số + gate (g′) nhắm tới → MT là miền hưởng lợi lớn nhất nếu CP-L6 19/07 được ký.

## 2. BUG THẬT PHÁT HIỆN & FIX NGAY: /monitoring CHẾT TOÀN BỘ JS TỪ TỐI 09/07

- Khối ⚖ BẬP BÊNH 2 MẶT (V10790-B, deploy 09/07 19:0x) khai báo `const SS` **trùng tên** với khối 📡 CUNG TÍN HIỆU (V10787-F, 08/07) trong cùng scope của `loadThreeLayer`.
- JavaScript: duplicate `const` trong cùng scope = **SyntaxError ngay lúc parse** → chết NGUYÊN inline script 4.578 dòng → **toàn bộ panel /monitoring không render suốt 7 ngày** (bao gồm ⛏ BEST SPOTS V10808 và 🧪 SHADOW A/B V10809 vừa deploy — owner chưa từng nhìn thấy chúng).
- Vì sao verify trước không bắt được: backend view/API vẫn đúng (compute_view chạy tốt, curl 401/200 đúng) — lỗi chỉ nổ ở browser khi parse JS. Quy trình trước giờ chưa từng parse-check JS.
- **Fix:** đổi tên `SS`→`SW` ở khối seesaw. **Gate mới bắt buộc:** `node --check` từng inline script trước mọi deploy file html (`_v10811_jscheck_local.py`). Sau fix: script 4578 dòng parse OK, VPS chỉ còn 1 `const SS`.

## 3. PANEL MỚI 🎯 TRÚNG NẰM Ở ĐÂU (BT vs SỐ PHỤ) — chuỗi §52 đủ

- View `bt_phu` trong `_v10773_three_layer_scoreboard.py`: per nhóm (AI-OFF / AI-SHD / ML / COMBO) × cửa sổ 14d + 60d + chi tiết ngày gần nhất; metric chính **`phu_only`** = phụ trúng mà BT trượt.
- UI: khối mới trong SO GĂNG 3 TẦNG `/monitoring` (đã nằm sẵn trong `loadAllSections()` + `setInterval` 60s), cảnh báo "⚠ nghiêng PHỤ" khi phụ−BT ≥ 8pp.
- Verify live sau deploy: MN w14 n=390 BT 184 / phụ 179 / chỉ-phụ 103 · MT n=390 BT 119 / **phụ 140** / chỉ-phụ 90 · MB n=380 BT 92 / phụ 83 / chỉ-phụ 52.

## 4. SHADOW A/B V10809 — DAY-1 HOÀN CHỈNH (trả lời "shadow nay sao rồi?")

- Đủ 15/15 row (5 model × 3 miền), scorer 19:15 chấm xong: **arm B (addendum) any-hit 8 vs arm A (production) 7**.
- Theo miền: **MT B thắng 4−2** (opus B [34,93] trúng cả đôi thay vì [40,82]; gpt-5-mini B ăn 82), **MB B thắng 1−0** (gpt-5-mini B [46,64] ăn 46 trong khi cả 5 arm A trượt trắng), MN B thua 3−5 (ngày MN dễ, production ăn đậm; B đổi pick mất 72).
- **SE3 mới ghi nhận:** qwen3.7-max arm B nhả pick trùng ["00","00"] (MT) — mất 1 slot đa dạng. Theo dõi; nếu lặp ≥2 lần trước CP-S3 (23/07) sẽ đề xuất vá dedup vào addendum. KHÔNG vá giữa kỳ để giữ so găng sạch.
- Còn 6 ngày (17–22/07), tổng kết 105 cặp tại CP-S3 23/07.

## 5. QUÉT TOÀN DIỆN VẤN ĐỀ ĐANG TREO (verify live từng cái)

| Vấn đề | Kết quả verify 16/07 | Trạng thái mới |
|---|---|---|
| C16 budget MB chết đói 6 tuần (FU-V10804) | Log `budget_catchup MB: selected=20` ~17:35 + lane MB có đủ row | **CLOSED** ✔ |
| T-chốt nhịp mới 16:54/17:54 (FU-V10798) | Ngày 2 liên tiếp đúng: [T10_CHOT] 15:45/16:54/17:54, bundle v2, models 15/13/15 | LIVE_VERIFIED_D2 (còn mốc lệch 24/07) |
| Watchdog báo động giả (FU-V10799) | 0 alert t10 giả cả 15/07 lẫn 16/07 | **LIVE_VERIFIED** ✔ |
| Cron tối 19:05 / 19:10 / 19:15 | ml-mark-ab +8 row, chase-bias +3 row, shadow scorer 15/15 | Sống cả 3 ✔ |
| Self-check 11 bất biến | 10/11 PASS; FAIL duy nhất = check-3 retrain (bệnh cũ đã fix V10800, chờ hàng OK đầu tiên CN 19/07) | KNOWN_TRANSIENT |
| K11a MB promote (đọc d8, chưa quyết) | Official-sau-promote BT **1/8** vs champion-cũ BT **3/8**; 3 ngày (11, 15, 16/07) champion đúng bị promote làm hỏng (16/07: champ 16✔ → thay 69✗). K15 MT chiều ngược: challenger nhỉnh (BT 2/7 vs 1/7) | Đọc số — **trio checkpoint 23/07 quyết** |
| MRE 20:15 | 0 row lúc probe 18:47 là ĐÚNG NHỊP (job chạy 20:15) | Bình thường |
| API key swap | Chưa làm — owner cung cấp key sau; inventory 7 key/5 hãng + quy trình đã chốt phiên 18:15; cửa sổ an toàn đến ~03:30 mỗi đêm | AWAITING_OWNER |

## 6. DEPLOY & AN TOÀN

- Backup: `backups/v10811_pre/` (local) + `/root/backups/v10811_pre/` (VPS).
- Upload 2 file: `_v10773_three_layer_scoreboard.py`, `monitoring.html` → py_compile OK → `grep -c 'const SS'` = 1 → restart `lottery.service` active → health 200, admin anon 401.
- **Hash 4 bảng PRE=POST IDENTICAL:** predictions 10200/d2732c81 · final_bundles 417/761958a3 · lottery_results 15088/b43f6694 · model_daily_eval 9986/aaa91dc6.
- Rollback: `cp /root/backups/v10811_pre/* <chỗ cũ>` + restart.

## 7. VIỆC CHỜ OWNER

1. Mở `/monitoring` xác nhận panel render lại (lần đầu sau 7 ngày) — sẽ thấy cả ⛏ BEST SPOTS, 🧪 SHADOW A/B, 🎯 TRÚNG NẰM Ở ĐÂU.
2. CP-L6 19/07: ký gói nhãn per-số + gate (g′) + align tier + thước ranking per-số (MT hưởng lợi lớn nhất theo số liệu mục 1).
3. API key mới: tạo xong dán vào `/settings` → gọi em (quy trình + inventory ở báo cáo phiên 18:15).
