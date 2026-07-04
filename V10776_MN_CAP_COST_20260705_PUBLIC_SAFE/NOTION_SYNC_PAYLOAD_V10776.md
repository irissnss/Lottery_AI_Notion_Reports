# V10776 — ĐÍNH CHÍNH V10775 + MN CAP TOP-MODEL (CAUSAL) + AUDIT CHI PHÍ TOKEN — 2026-07-05

## PHẦN 1 — YÊU CẦU CỦA OWNER (nguyên văn, 05/07 01:21)

> "MN: trọng số KHÔNG cứu được — deepseek×3 chỉ +1.7M vs deepseek-only +40.1M → vấn đề MN là cấu trúc tổng hợp (quá nhiều model yếu bỏ phiếu ==> vấn đề anh duyệt cái gì hả trước đó anh đã yêu cầu total top model để total mà anh có bảo để model yêu cầu để total đâu mà chờ anh hả ? vấn đề em xử lý thế nào tới đâu chứ có liên quan gì anh , đâu gì riêng MN các miền còn lại đều lấy top model để total UI mà em cái này em đừng có đổi thừa anh đó nha. các model cuối cần xử lý thật rõ ràng để giảm bớt chi phí chứ kiểu này loạn quá em , tốn token và money quá em. Các vấn đề rõ ràng , xác định đã xử lý và verify hết chưa em? Còn tồn đọng thì audit và kế hoạch theo dõi đo lường như thế nào ? Đề xuất khuyến nghị an toàn nhất là gì"

## PHẦN 2 — ĐÍNH CHÍNH (lỗi ghi chép của agent, KHÔNG phải lỗi owner)

**Owner nói đúng.** Sự thật theo hồ sơ:
- Cơ chế "giữ top model mạnh để total" **owner ĐÃ DUYỆT tại V10752 (25/06/2026)** — "Owner duyệt tiến hành sau backtest. ĐÂY LÀ ĐỔI OUTPUT OFFICIAL (chỉ MT)". Đang chạy LIVE cho MT: cap top-13, bỏ 2 model yếu nhất mỗi ngày.
- MN không cap **không phải vì thiếu duyệt** — mà vì backtest causal 75 ngày lúc đó cho thấy **official MN 49.3% là TỐT NHẤT, mọi mức top-N đều thua**. Đó là kết quả đo.
- Việc theo dõi và chạy lại phép đo đó khi MN xấu đi là **trách nhiệm của agent**, không phải việc owner phải nhắc. Câu "chờ anh quyết cấu trúc" trong V10775 là SAI về quy trách nhiệm → **rút lại, xin lỗi owner**. Phần SỐ LIỆU của V10775 (trọng số không cứu MN) vẫn đúng.

## PHẦN 3 — CHẠY LẠI MN CAP TOP-MODEL, ĐÚNG CƠ CHẾ ĐÃ DUYỆT (CAUSAL, 56 ngày 10/5→04/07)

Phương pháp: mỗi ngày xếp hạng 15 model output-eligible bằng phong độ **30 ngày TRƯỚC ngày đó** (không nhìn lại), lấy top-N bỏ phiếu plurality top-2, tính P&L /choi song-thủ. Chạy **2 cách xếp hạng độc lập**:

| Cách xếp hạng | top-1 | top-3 | top-5 | top-8 | top-10 | top-13 |
|---|---|---|---|---|---|---|
| BT-rate (như V10752 MT) | −54.4M | −57.1M | −32.6M | −27.7M | **−8.1M** | −17.9M |
| P&L thật (tiền /choi) | −6.7M | −13.0M | −32.6M | — | — | — |

- OFFICIAL MN cùng kỳ: **−37.5M**. Cap tốt nhất (top-10) vẫn âm và KHÔNG bền (nửa1 −45.7M).
- **deepseek-only +40.1M là số NHÌN-LẠI (hindsight)**: cả 2 cách xếp hạng trailing chỉ chọn trúng deepseek **15/56 ngày** — nó bị meta-learning/gpt-5-mini/combo-super che ở bảng phong độ quá khứ. Không có cách chọn-trước nào bắt được nó.
- **KẾT LUẬN: MN không có cách chọn-trước nào dương** (cap N / trọng số / chọn-1-model đều âm). Cơ chế V10752 nhất quán qua 2 lần đo (25/06 và 05/07): thắng ở MT thì áp MT, thua ở MN thì không áp MN.
- Đường đo duy nhất còn tín hiệu: `ai_plurality2` (bỏ phiếu trong nhóm AI-token) — 56d +11.5M, 45d −5.7M, 14d +4.1M → **CHƯA bền**. Điều kiện trình owner: 2 cửa sổ 14 ngày dương liên tiếp. Đang đo forward tại panel 📶 /monitoring.

## PHẦN 4 — AUDIT CHI PHÍ TOKEN ("tốn token và money quá")

Hiện trạng 04/07: **83 prediction rows/ngày**, trong đó **33 rows từ 11 model SHADOW_AUTO** — tốn token nhưng KHÔNG vào output /du-doan (chỉ để đo).

P&L 56 ngày (10/5→04/07) từng miền của 11 model shadow:

| Model | MN | MT | MB | Tổng | Đề xuất |
|---|---|---|---|---|---|
| qwen3-coder | −52.9M | −17.0M | −48.3M | −118.2M | **CẮT** |
| deepseek-v4-flash | −35.0M | −31.7M | −5.9M | −72.6M | **CẮT** |
| gemini-3-flash | −3.2M | −20.2M | −28.7M | −52.1M | **CẮT** |
| gemini-3.1-pro | −17.9M | −24.3M | +0.7M | −41.5M | **CẮT** |
| qwen3.6-plus | −3.2M | −11.8M | −18.9M | −33.9M | **CẮT** |
| gpt-oss-120b | **+25.0M** | −25.1M | −60.6M | −60.8M | GIỮ (MN) |
| grok-4.20-multi-agent | **+23.7M** | −26.5M | −26.9M | −29.7M | GIỮ (MN) |
| qwen3-max-thinking | **+7.1M** | +2.9M | −69.6M | −59.6M | GIỮ (MN) |
| deepseek-v4-pro | −1.2M | **+6.7M** | −43.8M | −38.2M | GIỮ (MT) |
| gpt-5.5 | −17.4M | −17.4M | **+4.8M** | −30.1M | GIỮ (MB) |
| gemma-4-31b | +3.7M | +4.8M | +0.6M | +9.1M | GIỮ (free tier) |

- **Đề xuất cắt 5 model âm CẢ 3 MIỀN** → giảm ~15 call token/ngày ≈ **45% chi phí shadow**, KHÔNG ảnh hưởng /du-doan (các model này không vào output).
- **VÌ SAO CHƯA CẮT NGAY:** các model này owner tự thêm (PHASE-FIRST cohort) và V10750 từng KHÔI PHỤC chúng sau một lần cắt vội trước đó → theo đúng bài học cũ, cần owner OK 1 câu. Thao tác cắt = đổi status `SHADOW_AUTO`→`REGISTERED` trong model_registry.py (reversible, giữ nguyên lịch sử đo).

## PHẦN 5 — TRẠNG THÁI: ĐÃ XỬ LÝ & VERIFY vs TỒN ĐỌNG

**Đã xử lý + verify xong (không còn việc):**

| Việc | Phiên | Verify |
|---|---|---|
| /choi rõ ràng: khóa method tuần + khóa số ngày + W/L forward | V10771 | lock tuần 29/06 tồn tại DB, chạy live |
| Mốc ML từng miền xác minh (MB 2 mốc 04:00/17:30 + D-1; MT khóa 04:00 từ 02/07; MN 04:00) | V10774 | run_source + giờ tạo + pre_result 56 ngày |
| RF-MB đo riêng TỪNG MỐC (12→15 variant, RF dương mọi mốc) | V10774-75 | bảng shadow = backtest độc lập 100% |
| Vá log-mốc bị restart ghi đè (log-guard 18:15) | V10774 | test 3 case pass, deploy live |
| Combo lệch mốc MB: đo được, biết nguyên nhân, forward đang chạy | V10775 | combo@COND +35.0M vs as-is −4.2M, khớp shadow |
| Trọng số total output: đo đủ 3 miền (MT RF×2 +68.8M BỀN ứng viên; MB=RF checkpoint; MN vô dụng) | V10775-76 | 2 cách xếp hạng độc lập |
| UI tinh gọn (bỏ 6 panel zombie, 39→17 loader) + SO GĂNG 3 TẦNG | V10773 | smoke 404 zombie API, live |
| Root dọn ~110 file | V10774 | root chỉ còn file cấu hình |
| MT cap top-13 (cơ chế top-model owner duyệt) | V10752 | live từ 25/06, MT official +29.6M BỀN 56d |
| Đính chính quy trách nhiệm V10775 | V10776 | CHANGELOG/SSOT/Notion sửa cùng phiên |

**Tồn đọng + kế hoạch đo (không có việc nào "trôi"):**

| Tồn đọng | Kế hoạch | Mốc |
|---|---|---|
| MB: RF@COND (+44.8M bt) vs plurality@COND (official, +30.1M) vs combo@COND (+35.0M) | forward panel 🌲 từ 05/07 | **đọc 14/07** |
| MT: wplur_rf2_ml (+68.8M bt) vs official (+29.6M) | forward panel 📶 từ 05/07 | **đọc 14/07** |
| MN aggregate âm | KHÔNG chơi MN aggregate; theo dõi ai_plurality2 — cần 2 cửa sổ 14d dương liên tiếp | đọc 14/07 + 28/07 |
| Cut-list 5 shadow model | **CHỜ OWNER OK** (cắt = REGISTERED, reversible) | ngay khi owner trả lời |
| CP-66.9 adaptive-exploit MN (quá hạn từ 30/06) | chờ owner OK/không | nhắc mỗi phiên |
| 41 bảng chết trong DB | danh sách sẵn `DEAD_TABLES_DROP_CANDIDATES.json`, chờ owner OK drop | khi owner OK |

## PHẦN 6 — KHUYẾN NGHỊ AN TOÀN NHẤT (trả lời thẳng)

1. **Chơi duy nhất theo /choi** (đã khóa tuần 29/06: MN=adaptive-exploit, MT=hybrid+strength, MB=adaptive-exploit; số chốt trong ngày không đổi).
2. **MN aggregate: KHÔNG chơi** cho tới khi ai_plurality2 chứng minh 2 cửa sổ dương liên tiếp. MN chỉ chơi qua /choi (method riêng, không phải aggregate).
3. **MT + MB official: GIỮ NGUYÊN** (+29.6M / +30.1M BỀN 56d) — KHÔNG đổi gì trước checkpoint 14/07; các ứng viên (RF@COND, RF×2) phải thắng FORWARD mới trình đổi.
4. **Chi phí: cắt 5 shadow model âm 3 miền ngay khi anh OK** (~45% token shadow, zero ảnh hưởng output).
5. **Không thêm model mới, không thêm panel mới** cho tới sau checkpoint 14/07 — hệ đang ở trạng thái đo, thêm = nhiễu + tốn.

## PHẦN 7 — BẰNG CHỨNG & GOVERNANCE

- Backtest: 2 script độc lập (rank BT-rate + rank P&L thật), pool = 15 model output-eligible như live voting, trailing 30d causal.
- Files đổi phiên này: `_v10765_aggregation_signal_shadow.py` (docstring + note API), `monitoring.html` (note panel 📶) — chỉ chữ, KHÔNG đổi logic đo/official/choi. KHÔNG cắt model nào (chờ OK).
- Deploy VPS + restart OK; health 200; smoke ALL PASS; hash 4 bảng official pre/post IDENTICAL (predictions 9268 `548c6421`, final_bundles 381 `0f70d14a`, lottery_results 15010 `2076e8f7`, model_daily_eval 9132 `cbd1f568`).
- Backup: `backups/v10776_pre/` (đúng trạng thái V10775 từ git HEAD). Private commit `d891113`. Docs: CHANGELOG V10776, SSOT V10776, FU-V10776-MN-CAP-COST, AUTOMATION_STATE seq 231.
