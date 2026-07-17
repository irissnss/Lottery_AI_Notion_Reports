# V10818 — Prompt gốc + "lệch ±1" + "đảo pha 34-43" (17/07/2026)

**Câu hỏi owner 20:59:** Prompt gốc là gì? Model có "luôn lệch ±1" (34→35, 75→85)? Bỏ ±1/đảo pha để model chỉ soi rules có khá hơn không (MB toàn 34-43)? Cho chạy sandbox nếu cần.

**Kết quả chính:**
- Prompt gốc = `SYSTEM_PROMPT` (~160 dòng) + context pack động. **CÓ dạy pha thật:** ĐẢO GƯƠNG (46↔64) + GIAO TRỤC (±1) + điểm "Ảnh đối" + few-shot "chốt 64 chính, 46 phụ" + anti-herding gợi ý "±1 cùng family" → cặp 34-43 hôm nay là do prompt dạy (3 model MB cùng ghép).
- **"Trượt ±1" = ẢO GIÁC TẦN SUẤT:** 6.680 lần main trượt — hàng-xóm về 65.7-86.5% NHƯNG null 67-89%, z ÂM cả 3 miền → không tồn tại "luôn lệch 1", bỏ ±1 không cứu ngày trượt.
- **Cặp phụ-biến-thể là bias HẠI THẬT ở MB (90d):** any 33.6% vs 40.3% độc-lập (−6.7pp), phụ-hit 17.8% vs 23.7%; hay ghép nhất: qwen3-coder 17.4%, gemini-2.5-pro 15.4%, qwen3-max 14.6%. MT ngược lại NHỈNH hơn (mirror MT z=+3.55) → chỉ trị MB/MN, giữ MT.
- **Sandbox PHASE-OFF 27 cặp call (batch 1 ngày bầy-trượt + batch 2 đối chứng 3 ngày bầy-thắng):** B any-hit 19/27 vs A 14/27 (+18pp) nhưng main-hit 4 vs 6 (−7pp) → tắt hẳn PHA là quá tay; đúng liều = **cấm SỐ-PHỤ-biến-thể khi trap + sửa gợi ý ±1**, không tắt toàn phần.

**Đã deploy (§52):** view `variant_pairs` recurring + khối 🪞 CẶP BIẾN THỂ ±1/ĐẢO trong panel 🏃 /monitoring (60s); health 200, admin 401, hash 4 bảng IDENTICAL, không đụng official/prompt.

**Quyết định chờ:** CP-S3 23/07 (cùng V10809) — MB vẫn kém ≥5pp → trình addendum 2 dòng, owner OK thì sandbox lại 1 vòng trước khi vào production. FU: `FU-V10818-VARIANT-PAIR`.

**Báo cáo đầy đủ:** GitHub `Lottery_AI_Notion_Reports/V10818_PROMPT_PHA_VARIANT_20260717/`
