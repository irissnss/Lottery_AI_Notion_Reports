# BÁO CÁO V10796 — MỔ NGÀY LẠNH 14/07 (CẢ 3 MIỀN TRƯỢT) + VERIFY FIX KHÓA COMBO PASS + PHÁT HIỆN LỆCH POOL-GIỜ MT

**Ngày:** 2026-07-14 tối · **Loại:** READ-ONLY (không code, không deploy, không restart) · **DB sync:** `artifacts/live_sync/20260714_185025`

**Câu hỏi owner (18:48):** "Kiểm tra toàn diện, phân tích, đào sâu, đề xuất phương án xử lý. MB nay tín hiệu tệ thật sự, MN full tín hiệu mà output không khá được, MT trung bình trật luôn — quá chán. Có gì cần xử lý không em?" (Việc thay API key dời lại theo lệnh owner — inventory 13 key đã giao phiên chiều.)

---

## 1. Ngày 14/07 có bất thường không? — KHÔNG

- Kết quả hôm nay: official MN 12✗/04✓ (−0.5M) · MT 17✗ 59✗ (−3.6M) · MB 51✗ 36✗ (−2.7M); /choi cả 3 miền trượt (−5.9M ngày).
- Đo 136 ngày đủ 3 miền: ngày **cả-3-miền-BT-trượt = 32/136 = 24%** (nếu 3 miền độc lập với nền 43/28/15% thì kỳ vọng ~35%). Ngày cả-3-pair-không-nháy chỉ 10%.
- Journal VPS: 0 traceback; chỉ SCRAPE_FAIL retry-noise trước giờ công bố (tự phục hồi, kết quả đủ trong DB). Health 200.
- Kết luận: **ngày lạnh nằm trong phân phối**, không phải lỗi hệ thống.

## 2. MN — "full tín hiệu mà output không khá" → owner nói ĐÚNG, và đây là lý do

- Bể MN hôm nay nóng thật: **10/15 model eligible trúng top-1**, 23/25 model có ≥1 nháy top-2.
- Vote gốc (ranked[0]) = **04 — TRÚNG** (7 phiếu, gồm 3 AI: gemini-flash, gpt-5.4, gpt-5-mini).
- Tầng override V10640 (specialist chooser, owner ký V10753) đổi 04 → **12 — TRẬT** (12 chỉ có cụm 4 ML: combo-no-token, xgboost, meta-learning, smart-ensemble). /choi MN (BT1-official) chết theo, may có E5 guard CÂN NHẮC nửa vốn (−1.4M).
- **Nhưng KHÔNG sửa gì**, vì forward-test từ 26/06 (sau lần chỉnh V10753): trên 8 ngày override can thiệp, override trúng 4 vs vote1 lẽ-ra-trúng 2 = **override vẫn +2 ngày net**; 60d: override 43% ≥ vote1 41%. Hôm nay là 1 ngày đau, không phải gãy cấu trúc.
- Nền đối chiếu: những ngày bể-nóng (≥8/15 top1-hit) official trúng BT **23/29 = 79%** lịch sử — hôm nay là ngoại lệ thứ 6/29.
- Ứng viên cải tiến "AI-cluster ≥3 phiếu → theo AI-plurality": full-history 137 ngày hybrid 47% vs official 43% (**chỉ +5 ngày**, hai nửa +4/+1) → DƯỚI chuẩn bằng chứng V10795 (≥39d hai-nửa-dương rõ ràng). Lane `MN_AI_CHAIN_PRESERVATION_V1` (chính là ý tưởng này, hôm nay chọn đúng 04✓) 60d chỉ 44% ≈ official 43% → không đáng đổi official.

## 3. MT — "trung bình trật luôn" → hôm nay lạnh bể, NHƯNG lộ 1 phát hiện cấu trúc đáng tiền

- Hôm nay MT lạnh cả bể: 9/25 model có nháy; challenger 17✗/59✗, champion cũ 45✗/59✗ — không nhánh nào cứu được.
- **PHÁT HIỆN:** official MT sinh bundle 16:38 khi pool mới có **13-15 model** (cụm shadow glm/kimi/qwen/gemma về 16:52-16:55) trong khi lane `MT_OUTPUT_V1` chạy 17:10 với **đủ 26 model**. Thuật toán K15 chọn top-10 strength KỂ CẢ shadow → thiếu phiếu shadow là lệch pick.
- K15-era (10-14/07): **lệch inline-vs-lane 3/5 ngày (10·11·14/07) = CHẠM NGƯỠNG BÁO ≥3** đặt ra ở V10794.
- Bằng chứng 60 ngày: lane-17:10 BT **36%** vs official-chốt **28%** (+8pp — đúng biên độ owner ký K15, nhưng official chưa hưởng trọn vì lệch pool-giờ). P&L 5 ngày K15-era hai bên bằng nhau (−2.0M) — chưa phân thắng bại ngắn hạn, nhưng cấu trúc thì rõ.
- MB cùng bệnh nhẹ hơn: shadow MB về 17:47-17:48, lane 17:55, official 17:34 → lệch 2/6 ngày K11a-era (11·12/07).

## 4. MB — "tín hiệu tệ" → đúng, và đo được: bầy-chụm KHÔNG phải tín hiệu ở MB

- Hôm nay 51 ôm **12/24 phiếu top-1**, 36 ôm 11 phiếu — toàn bộ AI + combo + shadow đồng hô 51/36 và trượt cả cụm; chỉ khối ML nắm số trúng (57✓ ×3 model, 90✓).
- Đo 120 ngày theo độ-chụm modal top-1 full-pool: share <30% → hit 22% · 30-44% → 20% · 45-59% → 18% (≥60%: 2/3 nhưng n=3). **Bầy càng đông không càng đúng ở MB** → không chế guard theo bầy (tránh zombie panel).
- Mặt AE của seesaw hôm nay vẫn ăn khi vote-mặt trượt: MB AE leg2 **46✓**, MT AE leg2 **62✓** — union sống đúng thiết kế. Khóa V0 lấy top1+top1 nên không hưởng 46; V10795 đã backtest 5 biến thể chứng minh V0 bền nhất — 1 ngày không đổi kết luận.

## 5. Verify fix khóa combo V10794 (việc đến hạn TỐI NAY) — PASS

- Daily lock MB 14/07: `locked_at=17:58:21`, songthu `["51","16"]` = m1-top1 (MB_OUTPUT_V1 17:55) + m2-top1 (AE 17:35) — đúng thiết kế V0, không còn freeze sớm 17:36 như bug cũ.
- Journal sạch, health 200, service up từ 09:11. **Item verify FU-V10794 ĐÓNG.**

## 6. Nhịp theo dõi (không đổi quyết định nào trước checkpoint)

| Kênh | Trạng thái | Chốt |
|---|---|---|
| K11a MB (d6) | challenger −1.5M · BT 1/6 · ăn 3/6 vs champion +3.4M · BT 1/6 · ăn 3/6 (chênh = đúng 1 ngày đúp 11/07) | **16/07** |
| K15 MT (d5) | challenger −2.0M · BT 2/5 ≥ champion −6.9M · BT 1/5 | **17/07** |
| Selector forward (d6) | MB trio +3.4M BT 3/6 (nổi bật, n nhỏ) · MN âm sâu −19.5M (ngược backfill → giữ vote) · MT âm nhẹ | **23/07** |
| /choi tuần 13-19/07 | −2.4M sau 2 ngày (13/07 +3.5M · 14/07 −5.9M) | cuối tuần |
| Seesaw union 60d | MN 87 · MT 84 · MB 78 — giữ ≥75% guard | — |

## 7. Đề xuất trình owner (KHÔNG code phiên này)

1. **P1 — Chuẩn hoá "pool-đầy" cho official (cần chữ ký):** dời giờ sinh bundle MT 16:38 → **~17:05** (sau shadow-batch 16:55) và MB 17:34 → **~17:56** (đọc thẳng lane bundle 17:55 như thiết kế V10789 gốc). Được: official hưởng trọn +8pp biên độ đã đo; hết lệch inline-vs-lane. Mất: official ra muộn hơn (MT còn ~10 phút, MB còn ~19 phút trước giờ quay). Nếu anh OK, em làm 1 phiên riêng đủ chuỗi (backup + flag rollback + verify 0-lệch).
2. **P2 — MN giữ nguyên:** override forward đang dương; hôm nay là noise. "Hot-pool guard" chỉ đo shadow nếu anh muốn.
3. **P3 — MB giữ nguyên** chờ K11a chốt 16/07 (selector trio +3.4M đang là ứng viên so sánh 23/07).
4. **P4 — CP-L6 QUÁ HẠN hôm nay:** xin anh chọn (a) **dời 19/07** gộp CP-R4 (khuyến nghị — thêm bằng chứng mới: selector top-8/10 đang ăn phiếu thật từ cụm shadow) / (b) làm ngay / (c) huỷ.
5. **P5 — Key rotation:** inventory 13 key đã giao, chờ anh cấp key mới là em thay cuốn chiếu.

**Hash 4 bảng:** predictions 10044 · final_bundles 411 · lottery_results 15075 · model_daily_eval 9830 (`3da3f94a` không đổi so post-V10794) — tăng trưởng tự nhiên trong ngày, không mutation.

**Scripts:** `_v10796_day_probe1-11.py`, `_v10796_vps_verify.py`, `_v10796_hash4.py` (READ-ONLY). **FU:** `FU-V10796-COLD-DAY-REVIEW`.
