# V10824 — PHÂN TÍCH TOÀN DIỆN KẾT QUẢ 19/07 (NGÀY FORWARD-1)

**Câu owner (22:27 19/07):** "Kiểm tra, phân tích đánh giá toàn diện kết quả dự đoán ngày hôm nay dùm anh. MB có rules ngon mà sao không bắt được như là 63,26 ah em, MN hội tụ đông quá, MT cũng yếu ớt ==> phân tích đánh giá tổng lực dùm anh"

**Phiên:** 19/07 22:27 → 23:0x · READ-ONLY (zero thay đổi production) · probes `_v10824_day1_full.py`, `_v10824_probe2.py`, `_v10824_calendar_check.py`, `_v10824_retrain_cpl6.py`, `_v10824_k_lanes.py`

---

## 1. KẾT QUẢ 3 MIỀN 19/07 (Chủ nhật)

| Miền | Số đuôi về | Official bundle | Lane TOTAL_V2 (giờ ghi) | LLM any |
|---|---|---|---|---|
| MN | 45 đuôi | BT **90 ✓** / phụ 50 ✗ (04:18) | [**90 ✓**, 50 ✗] @15:47 | 6/7 |
| MT | 43 đuôi | BT 34 ✗ / phụ 67 ✓ (16:38) | [34 ✗, 74 ✗] @16:56 | 4/7 |
| MB | 24 đuôi | BT 69 ✗ / phụ 46 ✗ (17:33) | [46 ✗, 01 ✗] @17:56 | 2/7 |

Trial V10820 ngày-2: LLM any 12/21; cộng dồn 2 ngày 27/42 = 64% — chưa chạm guard-rail nào (mốc 21/07).

## 2. "MB CÓ RULES NGON SAO KHÔNG BẮT ĐƯỢC 63, 26?"

### Số 63 — RULES ĐÃ PHÁT ĐÚNG, HỤT Ở TẦNG CHỌN
- Rule **2098** phát [63, 27] → **63 VỀ** (MRE 19/07). Union live 13 số lúc 17:42 CÓ 63 (lane risk_flags union_n=13).
- **0/7 LLM chọn 63** — 6/7 dồn main vào **46**: gpt-5-mini 46, gpt-5.4 46, claude-sonnet 46, claude-opus 46, deepseek 46, gemini-flash 46 (gemini-pro 01). Chỉ 2 model ML chạm: lstm [72,63], smart-ensemble [63,72].
- **Vì sao cả bầy dồn 46:** 46 vừa nổ **CẢ 3 MIỀN ngày 18/07** — đúng tật "đuổi số vừa nổ" (chase-bias). Bảng V10803 hôm nay ghi: BT official 69 là chase (nguồn MN,MT) → trượt; herd-top 69 (12 phiếu full-pool) cũng chase → trượt. Hội tụ MB hôm nay **47% (7/15 phiếu main) vs trung bình 90 ngày 29%** — miền hội tụ bất thường THẬT hôm nay là MB, không phải MN.
- **M2s coverage-rules xếp 63 hạng 3 trong-rules** → bộ-2 hụt, nhưng **top-4 = [46, 01, 63 ✓, 09 ✓]** — chơi dàn-3/dàn-4 theo rules ĐÃ bắt được 63 (backtest W3 any MB 65.4% vs bộ-2 50.3%, tốn 1.5× vốn — kèo vốn owner quyết, số có sẵn panel 🧮).

### Số 26 — NGOÀI RULES, NGOÀI MODEL (nói thật)
- 5 rule Chủ nhật của MB chỉ phát 13 số — KHÔNG có 26.
- KHÔNG model nào chạm 26 (0/27 kể cả shadow cohort).
- 26 về theo nền MB ~24%. Hệ rules+model hiện tại không với tới loại số này; muốn phủ rộng chỉ có dàn to thêm (đổi vốn lấy độ phủ). Em không hứa bắt được loại này.

### Official BT 69 — đúng "bệnh writer cũ"
69 NGOÀI union 13 số + là số chase (vừa về MN,MT hôm qua). Đây chính là lỗ hổng tầng tổng hợp mà track TOTAL-V2 (V10821) đang chữa — thêm 1 bằng chứng sống cho ngày chốt 28/07.

## 3. "MN HỘI TỤ ĐÔNG QUÁ" — ĐO PHIẾU THẬT: KHÔNG PHẢI

- Top-vote MN hôm nay: **4/15 = 27%, DƯỚI trung bình 90 ngày (29%)** — về mặt đo lường không phải ngày hội tụ cao.
- Phiếu chia 3 cụm: 17 (4v) ✗ · 50 (3v) ✗ · **90 (3v) ✓** — cảm giác "đông" đến từ 3 cụm chia đều, và cụm 90 là cụm ĐÚNG (BT official + lane đều ăn).
- Nhắc lại V10787 đã đo: consensus cao KHÔNG làm tăng xác suất trúng. Miền đáng lo hôm nay là MB 47% ⚠ — và nó trượt.
- Bonus MN: shadow M1 (không neo rules) chọn 17 ✗, M2s (neo rules) chọn 90 ✓ — **rules cứu MN hôm nay** (90 nằm rule 2028 phát [22,90,32,46] trúng [22,90]).

## 4. "MT YẾU ỚT" — ĐÚNG, NHƯNG LÀ NGÀY RULES XẤU (1 ngày = nhiễu)

- Union MT 12 số chỉ về 4 = **33% < nền 43%** — danh sách rules MT hôm nay dưới nền.
- Herd 34 (5 phiếu, TRONG rules) trượt; rule 2064 phát [82,99] trúng CẢ HAI nhưng chỉ 2 phiếu model chạm 99, 0 phiếu chạm 82.
- Không đổi gì: MT vốn là miền "ưu-tiên" (không bắt buộc) theo thiết kế V10820; đọc theo bucket miền×thứ, 1 ngày không đủ kết luận.

## 5. QUICK-TEST 2 BIẾN THỂ CHỐNG-DỒN-PHIẾU (đêm nay, leak-safe 166 ngày)

| Phương pháp | BT-gộp FULL | BT-gộp 60d | MB riêng |
|---|---|---|---|
| M2s (đang chạy) | 39.7% | 38.3% | 29.9% |
| VR (phiếu × chất-lượng-rule 56d) | 39.9% | 38.9% | 29.2% |
| VCAPR (cap 4 phiếu/số + rule-weight) | 39.9% | 38.9% | 28.6% |

→ Nhỉnh trong nhiễu, **MB còn giảm**; và hôm nay cả 2 vẫn chọn [46,01] (cap-4 không thắng nổi 7 phiếu). **KẾT LUẬN: GIỮ M2s nguyên kỳ đo. Thuốc đúng cho tật đuổi-số là anti-chase tie-break — bảng V10803 đang tích ngưỡng (−10pp/30 ngày forward), hôm nay +1 bằng chứng.**

## 6. HẠ TẦNG NGÀY FORWARD-1 — TẤT CẢ ĐÚNG GIỜ, ĐỦ ROWS

- Lane 3 miền ghi 15:47/16:56/17:56, mode REALTIME_AVAILABLE_ONLY, rules_active cả 3; evaluator chấm 3 rows.
- Shadow Total-V2 row forward đầu tiên 20:50 đủ 3 miền (`row_source='forward'`).
- A/B V10809 đủ 15 rows; chase-bias row forward 19:10; cặp biến-thể 0/19 (lệnh cấm giữ ngày-2).
- GĐB-đảo: ứng viên 62 TRƯỢT (forward 1/2 — ngày-1 54✓); GĐB 19/07 = 46438 → ứng viên mai **64**.
- Retrain Chủ nhật 02:00 + optimizer 03:14 **CHẠY THẬT** (12 dòng training_history, model files mtime 02:00-02:01). Check-3 self-check cần sửa định nghĩa (đếm status='OK' ra 0) — xem lần cron 21/07, retrain KHÔNG fail.

## 7. MỐC LỊCH ĐẾN HẠN HÔM NAY (đọc luôn trong phiên)

- **CP-S2 A/B giữa kỳ (16→19/07, 60 cặp):** arm B 40% vs arm A 52% = **−12pp gộp** (MN −35pp · MB −10pp · MT +10pp) — chưa chạm điều kiện dừng sớm (≥15pp ở 2 miền) → chạy tiếp đến CP-S3 23/07. Khớp kết luận trước: addendum per-số không phải hướng.
- **CP-L6 ĐẾN HẠN — CHỜ OWNER KÝ 3 mục:**
  1. **K11a MB (11 ngày):** challenger 1/11 vs champion 4/11 = net −3 ngày, champion VỀ bị thay 4 lần → khuyến nghị **FLIP VỀ CHAMPION**.
  2. **K15 MT (10 ngày):** challenger 2/10 vs champion 2/10 = HOÀ (chuỗi thua 7 ngày nhưng champ thua 6/7 ngày đó) → giữ đến trio 23/07.
  3. **Lean-roster (cắt opus/gpt-5.4) + CP-R4 + retire glm-5.1:** khuyến nghị **DỜI SAU 28/07** — đang giữa trial V10820 + lane 10 ngày, cắt roster lúc này trộn biến số (1 biến số/lần).

## 8. TÓM LẠI CHO OWNER

1. **63 không phải lỗi rules — rules đã phát và 63 về.** Lỗi ở tầng chọn: cả bầy đuổi 46 (số vừa nổ 3 miền). Dàn-4 theo rules đã bắt được 63.
2. **26 nằm ngoài mọi surface** — nói thật là không với tới, đừng kỳ vọng hệ bắt loại này bằng bộ-2.
3. **MN không hội tụ bất thường** (27% < trung bình) và hội tụ vào số ĐÚNG — lane ngày-1 ăn BT 90 ngay.
4. **MT hôm nay yếu vì danh sách rules xấu** — 1 ngày = nhiễu, không đổi gì.
5. **Không đổi phương pháp giữa kỳ** — quick-test 2 biến thể không thắng; anti-chase chờ ngưỡng V10803.
6. **CP-L6 cần anh ký 3 mục** (flip K11a / giữ K15 / dời lean-roster).
