# V10816 — Rule "GĐB MB đảo 2 số đầu → lô D+1" có mạnh không? (17/07)

**Owner 19:52:** flag rule GĐB 96763 → 69 về hôm sau + hỏi "có cái nào rõ ràng fix sớm hơn không, thua quá".

## Kết quả chính
- Ví dụ verify ĐÚNG: GĐB 16/07 96763 → 69 có trong lô 17/07 (69 cũng là BT official 16/07 — trùng kép).
- Backtest 2331 cặp (2020-2026): toàn kỳ 24.2% vs nền 23.8% (z=+0.42) = **KHÔNG edge**; cả họ 20 biến thể vị-trí rớt FDR; ăn BT 0.9% = nền.
- Vệt nóng THẬT: 30d cuối 12/30 = **40% = trần lịch sử** (8 cụm/6.5 năm); chuỗi 12-16/07 **5 ngày = bằng kỷ lục**. NHƯNG 7 cụm nóng trước đều xẹp về ~24% trong 30 ngày sau; null-sim: cụm 40%/30d chắc chắn xuất hiện do may.
- Kết luận: KHÔNG đưa vào official/prompt — forward-proof từ 17/07 với ngưỡng ghi sẵn (~16/08: ≥12/30 → trình side-bet lô /choi; ≤~28% → đóng). Số theo dõi mai 18/07: GĐB 45739 → **54**.
- Panel mới: khối 🔄 trong CHASE-BIAS /monitoring (full/cửa sổ/forward/chuỗi/8 cụm nóng/số theo dõi). Hash 4 bảng IDENTICAL, health 200, admin 401, node --check PASS.

## "Fix sớm hơn?" — xếp theo độ chắc
1. **K11a MB flip về champion (chờ ký — OK là flip ngay tối nay):** champion đúng bị thay 4 lần, net −3 ngày.
2. B1 hạ reasoning gpt-5.5 (chờ ký, 1 dòng).
3. CP-L6 19/07 đúng lịch: gemini-3.5 swap (43% vs 29%), retire glm-5.1, gpt-5.5→grok-4.3.
4. Rule GĐB-đảo: không fix gì được ngay — chỉ theo dõi forward.

**Chi tiết đầy đủ:** GitHub `Lottery_AI_Notion_Reports/V10816_GDB_DAO_2_SO_DAU_20260717/`
