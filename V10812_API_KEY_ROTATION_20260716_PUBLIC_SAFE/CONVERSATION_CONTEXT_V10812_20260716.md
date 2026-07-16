# CONVERSATION CONTEXT — V10812 (2026-07-16 22:54 → 17/07 00:1x)

Ghi lại nguyên văn tin nhắn owner trong phiên (để public repo giữ cùng ngữ cảnh với Notion).

## Owner 22:54 (kèm ảnh dashboard OpenRouter + file `z:\key api .txt` — file key KHÔNG đưa vào repo)

> Anh gửi em thông tin API key nha em. tiến hành xử lý dùm anh nhé . có vài vấn đề anh nhờ em kiểm tra trong ảnh các key đã dừng sử dụng 12 , 4 ngày trong hệ thống còn hoạt động không em? xem kỹ dùm các model có còn hoạt động thì add bằng key chung không thì clear sạch sẻ dùm anh nhé em.
> - Hiện tại chi phí GPT 5.5 cao quá em cần có kế hoạch thay thế gấp đi em chi phí lớn quá em ơi. Hiện có một số model mới giá rẻ cũng mạnh mẻ không kém như grok ah, em xem thử model nào phù hợp đề xuất dùm anh nhé. Nếu ok anh sẽ tạo key chính hãng từ trang chủ cho ít lỗi và mạnh mẻ nha em.
> Danh sách API Key đính kèm em làm cẩn thận tỉ mỉ verify đầy đủ nha em

Ảnh đính kèm: trang openrouter.ai/workspaces/default/keys — 10 key, hiển thị 8 dòng:
Lottery DDXS ($0, chưa dùng — key mới), Qwen3.6 Plus ($4.71, 12 ngày), OpenAI: GPT-5.5 ($71.92, 5 giờ), OpenAI: GPT-OSS-120b ($0.924, 5 giờ), Qwen: Qwen3 Max Thinking ($8.59, 4 giờ), MoonshotAI: Kimi K2.5 ($10.62, 4 giờ), Qwen3 Coder 480B A35B ($2.61, 12 ngày), Cohere: Rerank 4 Pro ($0.638, 7 ngày).

## Owner 00:15 (17/07)

> sao thế em chạy cho xong đi chứ

(Bối cảnh: phiên trước đó owner đã chốt chiến lược 1 key/hãng + 1 OpenRouter chung — V10811 phiên 18:15-22:0x.)

## Việc đã thực hiện trong phiên V10812

1. Audit key/model trên VPS: xác định model RETIRED/tháo tương ứng các key ngừng dùng 12/7 ngày; model đang sống (last=16/07).
2. Smoke 5 key mới TRƯỚC khi đụng config (call thật tối thiểu từng hãng) — phát hiện Google chặn gemini-2.5 với project mới.
3. Swap staged trên VPS: DB ai_keys + rewrite .env (dọn 22 biến legacy) + fix cohere_rerank category + restart + verify 19/19 resolve + hash 4 bảng IDENTICAL.
4. Đọc usage thật từng key OpenRouter cũ qua API (tổng $187.09) + token trace gpt-5.5 (reasoning HIGH từ 05/07 → ~$1.3/ngày, BT 37%→27%).
5. Lấy giá thật OpenRouter: grok-4.3 $1.25/$2.50 (ctx 1M), grok-4.5 $2/$6 — làm đề xuất thay gpt-5.5 (B1 hạ effort / B2 retire + onboard grok-4.3).
6. Governance: CHANGELOG V10812, SSOT, 3 FU items mới, AUTOMATION_STATE seq 273, báo cáo public + payload Notion, push 2 repo, trang Notion.
