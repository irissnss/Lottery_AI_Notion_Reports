# BÁO CÁO V10791 — TỔNG KẾT TUẦN 05–12/07/2026: CẢ 3 MIỀN × 3 LUỒNG + GIẢI MÂU THUẪN "BẦY ĐÔNG" + STATUS CHỜ-LIVE

- **Ngày:** 2026-07-12 (tối, sau khi MB 12/07 có kết quả)
- **Tính chất:** READ-ONLY — không code change, không deploy, không restart, DB chỉ đọc
- **Yêu cầu owner (20:25):** "Đào sâu, phân tích đánh giá kết quả dự đoán cả 3 miền tuần vừa rồi — có gì cải tiến, tiến bộ, phát hiện điều gì, đề xuất xử lý tiếp theo? Em từng nhận xét phương pháp total 14-16/26 model khả quan — mâu thuẫn với trước đó đúng không? Cần xem CẢ 3 luồng lane test / official / /choi — em khuyến cáo dùng /choi mà chưa phân tích ở đó. Các vấn đề tồn đọng, chờ live cũng chưa thấy đào sâu."
- **Probe:** `_v10791_week_review_probe.py` (1–3) + `_v10791_mn_ae_probe.py` (1–2) + `_v10791_v66_gate_probe.py` (1–3) — chạy trực tiếp trên DB production (read-only)

---

## 1. KINH TẾ TUẦN 05–12/07 (thước money-board, cặp 2 số, đồng nhất 3 luồng)

| Miền | Official (/du-doan) | /choi (mặt khuyến cáo) | Lane AE |
|---|---|---|---|
| MN | **+13.8M** — 6/8 ngày ăn, HỒI PHỤC RÕ | −2.0M (3/7 ngày, nghỉ T7 theo rule) | — (MN retired khỏi AE từ 06/07) |
| MT | −1.7M — nhưng **3/3 ngày ăn từ khi K15 chạy (10/07)** | **+22.8M** — 6/8 ngày ăn | +
| MB | **−6.9M** — vẫn là vùng lõm | **+14.1M** — 4/8 ngày | +
| **Tổng** | **+5.2M** | **+34.9M** | +26.6M |

**Đọc nhanh:**
- Mặt em khuyến cáo anh chơi (/choi) tuần này **LÃI +34.9M**, kéo bởi MT/MB; chân yếu là MN (−2.0M).
- Official tổng dương trở lại (+5.2M) nhờ MN hồi phục mạnh; MB official vẫn âm — đúng vùng mà K11a đang thử thay thuật toán.
- 30 ngày làm nền: MN off +19.6M (21/31 ngày ăn) · MT off +29.8M · MB off −5.3M; **MB AE +54.9M là dòng mạnh nhất hệ** — củng cố vai /choi MB = echo AE.

## 2. GIẢI MÂU THUẪN "BẦY ĐÔNG" — OWNER BẮT ĐÚNG

Hai phát biểu trước đây của em ("bầy to = anti-signal" ở V10787-D vs "bầy 14-16/26 model khả quan" ở V10789) **đều đúng trong ngữ cảnh riêng nhưng em trình bày như quy luật chung — đó là lỗi trình bày của em**. Đo lại 60 ngày, cỡ-bầy × thành-phần × miền:

| Cỡ bầy top-1 | MT hit | MB hit | MN hit |
|---|---|---|---|
| Lẻ ≤5 | 45% | ~26% (nền) | 40-55% (phẳng) |
| Vừa 6-9 | giảm dần | **13% (đáy chữ U)** | phẳng |
| To 10-14 | thấp | hồi | phẳng |
| **Rất to ≥15** | **0% (anti-signal)** | **40% (gấp đôi nền)** | phẳng |

- **MT: giảm đơn điệu theo cỡ bầy** → bầy càng to càng nên né (câu V10787-D đúng Ở MT).
- **MB: hình chữ U** → bầy vừa (6-9) tệ nhất, nhưng bầy RẤT to (≥15, AI-đa-số) đáng tin — hai ngày 62 (07/07) và 77 (08/07) nằm đúng nhóm này (câu V10789 đúng Ở MB).
- **MN: phẳng** → cỡ bầy không mang thông tin ở MN.
- Thành phần cũng khác: bầy MT nhỏ AI-đa-số hit 67% vs ML/lẫn 20%.
- Hai lần đo còn dùng **metric khác nhau**: V10789 đo "winner có nằm trong top-2 của bầy" (đo CUNG tín hiệu), V10787-D đo "số bầy top-1 có trúng" (đo CHẤT pick). Panel 🐑 (herd) + ⚖ (seesaw) trên /monitoring đang đo sống cả hai.

## 3. PHÁT HIỆN TUẦN: MN ADAPTIVE-EXPLOIT DỪNG TỪ 06/07 — BY DESIGN, KHÔNG PHẢI BUG

- Trong lúc đào /choi MN, em thấy `MN_ADAPTIVE_EXPLOIT_V1` không sinh bundle từ 06/07 → truy ngược: **owner abandon roadmap LAG1 ngày 05/07** → V10779 (CP-66.9 Option A) retire MN khỏi V67: scheduler chỉ chạy `("MT","MB")` từ target-date 06/07.
- /choi MN tự chuyển về `BT1_OFFICIAL` đúng thiết kế lock tuần — không có lỗ hổng dữ liệu.
- Ghi chú số liệu để anh biết (không phải đề xuất): flow `same_region_lag1` MN vẫn BOOST ở cửa sổ 60/90 ngày (+11.8pp/+16.7pp); w30 chưa đủ mẫu. Nếu tương lai anh muốn mở lại MN AE thì chỉ cần bỏ retire — hiện tại em TÔN TRỌNG quyết định abandon.

## 4. STATUS CÁC VIỆC CHỜ-LIVE (owner hỏi "chưa thấy đào")

| Việc | Ngày chạy | Kết quả đến 12/07 | Phán quyết |
|---|---|---|---|
| **K11a MB** (official = MB_OUTPUT_V1) | 4 ngày (09→12/07) | Challenger 2/4 ngày ăn (36✓/17✓) vs champion 2/4 — champion tạm dẫn ~4.9M nhờ ĐÚP 98✓65✓ ngày 11/07 | CHƯA chạm kill (cần 5 ngày thua liên tục); checkpoint ngày-7 = **16/07** |
| **K15 MT** (official = MT_OUTPUT_V1) | 3 ngày (10→12/07) | **3/3 ngày ăn** (85✓ · 61✓BT · 64✓+10✓ đúp), luôn ≥ champion | Đúng hướng; checkpoint ngày-7 = **17/07** |
| **Selector shadow K10/K13** (forward) | 3 ngày | MN XẤU: BASE/RECENCY 0/3, −9.0M (trong khi official MN +13.8M) — NGƯỢC với backfill; MT/MB 1/3 hoà-dương | Đây chính là lý do phải đo forward trước khi đổi selector; tổng kết 14 ngày = **23/07** |
| **Seesaw union** (V10790-B) | — | Union ≥1 mặt trúng giữ MN 88 / MT 82 / MB 77% | Khớp thiết kế tách vai vote/echo |
| **repeat_lost** (lặp-số-vừa-thua) | — | Không tái diễn tuần này | Sạch |
| **Gemma 429 MB** (K8) | — | KHÔNG tái diễn cả tuần (bể MB 22-26 model/ngày) | Để mở, không cần xử lý |
| **Journal/hạ tầng 11-12/07** | — | 0 warning, 0 traceback; /choi MN không lock 11/07 = rule NGHỈ-THỨ-7 chữ ký owner | Đúng thiết kế |

## 5. ĐỀ XUẤT

1. **KHÔNG đổi gì thêm bây giờ** — 2 thay đổi lớn (K11a, K15) đang giữa cửa sổ đo; chồng thêm thay đổi là mất khả năng quy nguyên nhân.
2. Checkpoint đã hẹn: **13/07 sáng** verify weekly /choi lock (cron 00:05 tự chọn method mới) · **16/07** K11a ngày-7 · **17/07** K15 ngày-7 · **23/07** selector 14 ngày.
3. **K14** (retrain sandbox MB `include_same_day=True` — khép train/serve mismatch): vẫn chờ ký, khuyến nghị LÀM (offline, zero risk).
4. **K9** (HERD_FADE): khuyến nghị CHƯA làm — K15 đã xử phần lớn gốc bệnh MT.
5. **CP-L6** (lean harvest, hạn 14/07): cần owner OK.

## 6. AN TOÀN & TRUY VẾT

- Phiên READ-ONLY: không sửa runtime, không restart, không ghi DB — /du-doan, lane, /choi nguyên trạng.
- Commit private: `51d3cd1` (docs + 12 probe files).
- Docs cùng phiên: `CHANGELOG.md` (V10791) · `docs/CURRENT_TRUTH_SSOT.md` (block V10791) · `docs/FOLLOW_UP_TRACKER.md` (FU-V10791-WEEK-REVIEW) · `docs/AUTOMATION_STATE.json` (seq 252) · `docs/AUTOMATION_HISTORY.jsonl`.
