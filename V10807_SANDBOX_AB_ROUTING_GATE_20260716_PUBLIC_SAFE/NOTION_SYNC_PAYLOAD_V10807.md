# V10807 — Sandbox A/B routing-gate: 5 model thật × 3 miền × 2 arm (30 call)

Owner 16/07 00:39: "Em đã test thử nghiệm trong sandbox chưa — nó ảnh hưởng đến output của đơn model AI. Cần thử 3-5 model trên 3 miền, với model đang kém và đang mạnh."

Kết quả chính:
- 30/30 call thật OK trên VPS (key production, KHÔNG ghi DB, hash 4 bảng IDENTICAL). Arm A = prompt gốc; Arm B = + khối "🧭 ĐIỀU KIỆN TRỎ MIỀN & NHÃN PER-SỐ" ((g)+(h)+(a′) từ V10806).
- Addendum tác động THẬT: 14/15 cặp đổi pick; 7/15 record trích dẫn addendum trong reasoning.
- Đúng hướng thiết kế: MT dùng tail ô-âm Quảng Ninh 3/5 → 1/5; vị trí phụ là trap 5/15 → 1/15; MN any-hit 2 → 4.
- Model KÉM hưởng lợi nhất: 1/6 → 4/6 trúng (gemini-flash bỏ 19@MN trúng 74; gpt-5-mini bỏ 61@MT trúng 54) — đúng 2 con danh sách thay API. Model MẠNH trơ: qwen lì 51/61 cả 2 arm; opus giữ [17,67]@MN trúng đôi cả 2 arm.
- 2 tác dụng phụ phải vá vào (g′): SE1 = opus dồn cả 2 vị trí vào 1 rule ✔ (cần ràng buộc cứng "mỗi rule tối đa 1 vị trí"); SE2 = MB mất 2 hit vì secondary bị hút khỏi tín hiệu nội-miền 66 sang tail rule ✔ (cần mandate "≥1 vị trí từ tín hiệu nội-miền độc lập").
- Giới hạn trung thực: any-hit A 5/15 vs B 6/15 — mẫu 1 ngày/case, không kết luận accuracy; kết luận chắc nằm ở hành vi.

Quyết định chờ owner (CP-L6 19/07): ký (g′)+(h)+(a′) → implement trong build_context_pack + shadow 7 ngày trước khi bật official; cân nhắc hoãn thay API gemini-flash/gpt-5-mini đến sau shadow.

Chi tiết đầy đủ: GitHub `Lottery_AI_Notion_Reports/V10807_SANDBOX_AB_ROUTING_GATE_20260716_PUBLIC_SAFE/` (báo cáo + evidence addendum 3 miền + raw 30 call).
