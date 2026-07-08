# V10787 — Đối chứng 3 mặt official/lane//choi + audit live 07-08/07 (08/07/2026)

Owner hỏi: "official 1 đường, lane test 1 nẻo, /choi 1 kiểu — mỗi cái trúng mỗi kiểu, điểm mạnh để output hoàn hảo?"

**Kết quả đo (từ 10/05, cùng thước /choi):**
- 3 mặt gần như KHÔNG trùng số: same-pick MN 0/57 · MT 3/58 · MB 0/34 — khác nhau là THIẾT KẾ (selector khác nhau).
- Bù trừ có thật: trần chọn-đúng-mặt 75.4% / 56.9% / 47.1% (MN/MT/MB) — nhưng là hindsight.
- GỘP cặp [off-BT, lane-BT] THUA mặt tốt nhất ở CẢ 3 MIỀN: MN +30.6 vs lane +47.2 · MT +8.2 vs off +31.7 · MB +1.3 vs lane +25.8 (triệu) — tiền cược x2 nuốt hết lợi ích bù trừ.
- KẾT LUẬN: không có output hoàn hảo bằng trộn. Điểm mạnh = CHỌN ĐÚNG MẶT THEO MIỀN + bám weekly-lock /choi.
- Lock tuần 06/07 owner ký KHỚP data 21d: MN official +8.6M > lane -6.1M (lane nguội) · MT hoà · MB lane +36.4M >> off -7.7M.

**Deploy:** khối ⚔ ĐỐI CHỨNG official vs lane-AE thêm vào panel SO GĂNG 3 TẦNG `/monitoring` (module `_v10773`, sandbox-first, restart 14:01 ngoài live-window, health 200 · admin 401, hash 4 bảng IDENTICAL). DIAGNOSTIC-ONLY — official/selector không đổi.

**Audit live 07-08/07 cùng phiên:** BT 3 miền LOSE 07/07 (MT 0/26 model WIN) · MB doctrine chọn 87, plain-vote 62 TRÚNG → scorecard 1W-1L, theo dõi hết dom≤10 · coverage 78/78 · late-fill cứu ca 2 (gemma MT 439s) · hạ tầng ALL_GREEN (T-10 đúng giây, watchdog 0 alert, cron gate log OK) · /choi tuần: MN +1.7M · MT -2.8M · MB -3.2M sau 3 ngày.

**Bổ sung 15:xx — owner hỏi "3 luồng cũng đoán mò à?" (V10787-C):** Z-test + Monte Carlo 5000 người mò, 59 ngày: OFFICIAL-BT ≈ đoán mò thật (combined z=-1.12; MB 15.3% vs mò 23.7%, z=-1.53 TỆ hơn mò) — trực giác owner đúng cho mặt này. LANE-AE có edge THẬT khiêm tốn: cùng chiều 3 miền, combined z=+1.78 (p≈0.038); P&L percentile 91/75/89 vs dân mò (dân mò median ÂM). MN BT1 1-số hoà vốn lịch sử (percentile 52) — sống nhờ form 21d, gắn trigger đổi mặt nếu 21d âm. Badge z + mốc "đoán mò" thêm vào khối ⚔ /monitoring (deploy 15:06, hash IDENTICAL).

**Bổ sung 18:xx — owner: "ML MT thảm hại khi thay đổi, xem kỹ MT cả 3 luồng" (V10787-D):** MT 08/07: official 59✗ (chuỗi 4L, 21d 4/19=21% DƯỚI mò) · lane AE 63✓ · /choi [63,37] +1.3M → tuần +3.9M, KHÔNG thảm. ML lạnh 0-1/3 sau 06/07 nhưng không có change ML nào — mẫu nhỏ + miền lạnh. Phát hiện chính: HERD — 3 model mới bám bầy 5-6/9 lượt, concentration top1 MT nổ 46/42/58% (15/26 chụm 86✗ hôm nay); đo 30d bầy ≥10 tại MT chỉ trúng 12% = ANTI-SIGNAL. AE MT = lag-1 echo chủ đích (13/23 ngày). Panel 🐑 BẦY deploy 18:05 (guarded, hash IDENTICAL). **K9 chờ ký:** HERD_FADE_V1 shadow 14 ngày.

**Quyết định chờ ký:** K8 gemma MB 429 (K8a slim-context / K8b nâng tier / K8c chấp nhận) · **K9 HERD_FADE_V1** (mới). Nhắc: CP-L5 hard deadline 09/07 (ngày mai).

**Chi tiết đầy đủ:** GitHub `Lottery_AI_Notion_Reports/V10787_THREE_SURFACE_CONTRAST_20260708_PUBLIC_SAFE/BAO_CAO_TONG_V10787.md`
