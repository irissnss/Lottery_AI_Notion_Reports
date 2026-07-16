# V10812 — Thay toàn bộ API key (5 key mới) + đề xuất thay GPT-5.5 (16/07 22:54→23:5x)

**Kết quả chính:**
- Swap XONG 5 key mới: OpenAI, Anthropic, DeepSeek, OpenRouter (1 key chung 8 model), Google AQ (chỉ shadow). Dọn 22 biến env legacy + xóa key orphan DB. Verify 19/19 model resolve đúng key; health 200; hash 4 bảng official IDENTICAL.
- Key dừng 12 ngày (Qwen3.6 Plus, Qwen3 Coder) = model RETIRED 04/07; 7 ngày (Cohere Rerank) = tháo 09/07 → owner revoke NGAY được. Key "4 giờ" là model đang sống — đã về key chung.
- **PHÁT HIỆN LỚN:** Google chặn gemini-2.5-flash/pro với project MỚI ("no longer available to new users") → 2 model official Google chỉ sống trên 2 key project cũ — **CẤM revoke**; lộ trình thoát = migrate gemini-3.5-flash (shadow BT 42%/33d) tại CP-L6.
- **GPT-5.5:** giá thật $5/M in + $30/M out; từ khi bật reasoning HIGH 05/07 tốn ~$1.3/ngày (=38% tổng chi OpenRouter $187 lifetime) mà BT tụt 37%→27%. Grok-4.20 bill thật chỉ $0.40/ngày, BT 37-38% nhóm đầu.

**Chờ owner quyết (FU-V10812-GPT55-REPLACE):**
- B1: hạ reasoning effort gpt-5.5 HIGH→default (1 dòng, tiết kiệm ~60%).
- B2 (CP-L6 19/07): retire gpt-5.5 + onboard grok-4.3 ($1.25/$2.50, ctx 1M) shadow qua key OpenRouter chung; option grok-4.5 ($2/$6). Key xAI chính hãng nối sau khi grok-4.3 chứng minh (route `_call_xai` có sẵn).

**Revoke:** NHÓM A ngay (3 key model nghỉ); NHÓM B sau verify sáng 17/07 (6 key OR cũ + OpenAI + Anthropic + DeepSeek ×2 + Google shadow cũ); GIỮ 2 key Google cũ.

**Báo cáo đầy đủ:** GitHub `Lottery_AI_Notion_Reports/V10812_API_KEY_ROTATION_20260716_PUBLIC_SAFE/`
