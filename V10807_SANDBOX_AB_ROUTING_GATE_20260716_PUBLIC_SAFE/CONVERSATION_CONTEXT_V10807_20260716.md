# CONVERSATION CONTEXT — V10807 (16/07/2026, ~00:39 → 01:4x)

## Verbatim owner (nguyên văn)

> em đã test thử nghiệm trong sandbox chưa em nó ảnh hưởng đến output của đơn model ai ah em cần thử nghiệm thử dùm anh trong snadbox trong 3-5 model trên 3 miền thử dùm anh với model đang kém và đang mạnh nha em.

## Bối cảnh

- Nối tiếp V10806 (ma trận routing + escape audit trả lời 3 câu hỏi "ngược ngạo / nhầm miền / model nào vượt qua") — trong đó đề xuất CP-L6 (g) routing gate + (h) trap alert theo miền + (a′) nhãn per-số là THAY ĐỔI PROMPT, mới chỉ dựa trên đo lịch sử, chưa test tác động thực lên output đơn model.
- Owner yêu cầu đúng trọng tâm: test sandbox trước, 3-5 model, 3 miền, gồm model đang kém và đang mạnh.

## Việc đã làm trong phiên

1. Clone đường replay production V10805 → `_v10807_ab_sandbox.py`: 3 case as-of (MB@14/07, MT@15/07, MN@15/07), 5 model (kém: gemini-2.5-flash, gpt-5-mini; mạnh: claude-opus-4-6, qwen3.7-max; trung: deepseek-reasoner), 2 arm (A gốc / B + khối 🧭 điều kiện trỏ miền & per-số hook qua build_context_pack), không ghi DB.
2. Chạy 30 call thật trên VPS bằng key production — 30/30 OK, ~42 phút; hash 4 bảng official IDENTICAL trước/sau.
3. Phân tích `_v10807_analyze.py`: 14/15 đổi pick; MT ô-âm 3/5→1/5; phụ-là-trap 5/15→1/15; model kém 1/6→4/6; phát hiện SE1 (dồn 2 vị trí vào 1 rule ✔) + SE2 (bị hút khỏi tín hiệu nội-miền).
4. Governance: CHANGELOG V10807, SSOT block, FU-V10807-AB-SANDBOX (mới) + cập nhật FU-V10806-RULE-ROUTING, AUTOMATION_STATE seq 268, HISTORY, báo cáo public + payload Notion, commits 2 repo, Notion page.

## Trạng thái chờ

- CP-L6 19/07: owner ký (g′) = (g)+vá SE1+vá SE2, (h), (a′) → implement build_context_pack + shadow 7 ngày trước khi bật official.
- Gợi ý: cân nhắc hoãn thay API gemini-flash/gpt-5-mini (2 con hưởng lợi nhất từ gate) đến sau shadow để so.
