# V10808 — Sandbox 7 ngày-case + Best Spots đài×giải + bản nhãn TRƯỚC/SAU cho CP-L6

Owner 16/07 08:44: "Đề xuất tốt nhất là gì? Chỗ đang khai thác cần ghi nhận + đào bới thêm tìm chỗ tốt nhất. Sandbox chạy bao nhiêu ngày? Nhãn prompt đổi thế nào — cần cụ thể, anh khó hiểu quá."

Kết quả chính:
- Sandbox tổng: 7 ngày-case × 3 miền = 78 call thật (V10807: 3 ngày bẫy × 5 model; V10808: thêm 4 ngày thường 10-13/07 × 2 model rẻ, fix leakage). 0 lỗi, không ghi DB, hash 4 bảng IDENTICAL.
- Ngày thường KHÔNG bị gate phá: A 67% → B 75%, trúng-đôi 2→5, không miền nào tụt; gpt-5-mini 8/12→10/12.
- GỘP 7 ngày (2 model rẻ, 30 cặp): any-hit 57% → 73% (+16pp); thắng-mới 8/mất 3; sign-test p≈0.11 — hướng tốt nhưng CHƯA đạt ý nghĩa → bắt buộc shadow live 7 ngày trước khi bật official.
- Đào bới best spots (per-số đài×giải×đích×offset, n≥40): 12 ô DƯƠNG z≥2 — top Ninh Thuận G1+G7 MT→MB 47.7%/số (+23.9pp z=3.73, T7); TẤT CẢ đang được khai thác nhưng 6/12 bị tier thấp (LIMITED_WEIGHT/CAUTION). 1 ô ÂM: Quảng Ninh G6+G7 MB→MT (−8.4pp z=−2.39, n=186) VẪN active = thủ phạm 39/61.
- Phát hiện sửa đề xuất: cùng ô MB→MT có cả âm (QN) lẫn dương thật (Hải Phòng G6 +14.8pp z=2.18) → gate = Ô-nền + NGOẠI LỆ per-rule, không chặn cả ô. Thêm (i) align tier miner theo per-số.
- Bảng ⛏ BEST SPOTS đã live trong panel 🏃 /monitoring (ghi nhận cố định, tự cập nhật). Deploy smoke 200/401/401, hash pre=post IDENTICAL.
- Bản nhãn TRƯỚC/SAU nguyên văn (prompt MT 15/07 thật): GIỮ dòng 12W cũ + THÊM dòng ↳ per-số ~X% (n=Y) | ô ✔/⛔ | tối đa 1 vị trí + header giải thích % + footer "≥1 vị trí nội-miền" — file LABEL_SPEC_TRUOC_SAU_CP_L6.md.

Chờ owner ký CP-L6 19/07 (xếp theo độ chắc): (1) nhãn ↳ + ràng buộc; (2) demote/loại QN G6+G7→MT; (3) align tier 12 ô dương; (4) MN trap CONV×2; (5) hoãn thay API gemini-flash/gpt-5-mini đến sau shadow.

Chi tiết: GitHub `Lottery_AI_Notion_Reports/V10808_BEST_SPOTS_AB48_LABEL_SPEC_20260716_PUBLIC_SAFE/` (báo cáo + label spec + evidence raw).
