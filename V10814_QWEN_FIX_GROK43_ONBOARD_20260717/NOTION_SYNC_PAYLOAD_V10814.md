# V10814 — Qwen lỗi rỗng (revert) + Grok 4.3 Thinking shadow + tư vấn Tier 2 (17/07)

**Owner 12:10:** Qwen3 Max Thinking bị lỗi xem dùm; nếu ổn add Grok 4.3 thinking chạy shadow bằng key OpenRouter; tier 2 Google nộp nhiêu tiền; key cũ không phát sinh đúng không; còn key/model nào nữa; tiếp tục theo dõi không bỏ lỡ.

**Kết quả chính:**
- **Qwen3 Max Thinking:** root cause = reasoning effort HIGH (bật 05/07): trả rỗng leo thang 0% → 14% → 38% (hôm nay MN rỗng); cohort khác chỉ 0–6%. FIX: revert về config cũ (exclude + 24576) — khi có output BT 40%/30d nên GIỮ không retire. Mốc so găng mới 17/07. Recheck ~24/07.
- **Grok 4.3 Thinking:** ONBOARD SHADOW xong 12:40 qua key OR CHUNG (không cần key mới): slug x-ai/grok-4.3, $1.25/$2.50 per M (out rẻ hơn gpt-5.5 12×), ctx 1M, smoke 200 + reasoning text. Chạy thật MT+MB chiều nay; ngày đủ 3 miền đầu 18/07; ứng viên thế gpt-5.5 tại CP-L6 19/07. Ước ~$0.2/ngày.
- **"Key cũ không phát sinh":** đúng cho OR/OpenAI/Anthropic/DeepSeek. RIÊNG GOOGLE: dashboard hiển thị UTC-8 nên usage 04:00 VN nằm cột Jul-16 — gemini-2.5-flash/pro OFFICIAL vẫn ăn key Google cũ hằng ngày → **TUYỆT ĐỐI chưa revoke 2 key Google cũ / chưa đóng account Tier-2 cũ** (Google chặn 2.5 với project mới).
- **Tier 2 Google:** thanh toán thật tích lũy **$100 + 3 ngày** từ lần thanh toán đầu → auto-upgrade (cap $2,000/tháng). Tier 3 = $1,000 + 30 ngày. Hệ mình trên account mới chỉ ~vài cent/ngày → Tier 1 đủ; nâng chỉ vì nhu cầu ngoài.
- **Còn key nào nữa:** KHÔNG — đủ 4 hãng + 1 OR chung + 2 Google cũ. xAI direct chưa cần.
- **Model đề xuất thêm:** hôm nay KHÔNG thêm (giữ so găng sạch); ứng viên CP-L6: qwen3.7-plus $0.32/$1.28 · minimax-m3 $0.30/$1.20 · gemini-3.1-pro (AQ PASS).

**An toàn:** chỉ nhánh shadow; hash 4 bảng PRE=POST IDENTICAL; /du-doan + A/B V10809 không đổi; health 200; backup 2 đầu.

**Việc chờ:** chiều nay verify grok-4.3 + qwen hết rỗng; owner quyết B1 gpt-5.5 + revoke nhóm A+B; 19/07 CP-L6; ~24/07 recheck qwen.

**GitHub (báo cáo đầy đủ):** `Lottery_AI_Notion_Reports/V10814_QWEN_FIX_GROK43_ONBOARD_20260717/`
