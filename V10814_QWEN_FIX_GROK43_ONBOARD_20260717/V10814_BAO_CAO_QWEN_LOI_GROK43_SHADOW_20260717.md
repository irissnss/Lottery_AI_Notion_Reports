# V10814 — QWEN3 MAX THINKING LỖI RỖNG (REVERT CONFIG) + ONBOARD GROK 4.3 THINKING SHADOW + TƯ VẤN TIER 2 GOOGLE — 17/07/2026 12:10→13:0x

**Yêu cầu owner (12:10):** "Anh đã disable các API key cũ ngoại trừ google. Key Google cũ tier 2 nhưng account mới chỉ tier 1 — muốn lên tier 2 nộp nhiêu tiền tư vấn thêm. Key cũ hôm nay không phát sinh chắc chuyển đổi thành công rồi nhỉ. Qwen3 Max Thinking nay bị lỗi xem dùm anh. Nếu ổn thì add Grok 4.3 thinking suy luận sâu bằng key OpenRouter chạy shadow luôn, còn key nào nữa không? Còn đề xuất model nào không? Tiếp tục theo dõi hệ thống không được bỏ lỡ rơi rớt."

---

## 1. QWEN3 MAX THINKING — ANH BÁO ĐÚNG, ĐÃ TÌM RA GỐC VÀ SỬA

### 1.1. Triệu chứng
Hôm nay 17/07 chuỗi MN 04:23, qwen3-max-thinking trả **rỗng** (`main_numbers=[]`). Không phải lần đầu — đây là đỉnh của một chuỗi leo thang.

### 1.2. Bằng chứng theo giai đoạn (bảng đếm từ DB `predictions`)

| Giai đoạn | Config | Số dự đoán | Rỗng | Tỷ lệ |
|---|---|---|---|---|
| 21/06–04/07 (P1) | reasoning exclude (cũ) | 42 | 0 | **0%** |
| 05–11/07 (tuần 1 HIGH) | effort HIGH (E3a bật 05/07) | 21 | 3 | **14%** |
| 12–17/07 (tuần 2 HIGH) | effort HIGH | 16 | 6 | **38%** |

Ngày rỗng cụ thể tuần 2: 14/07 MB+MT, 15/07 MN+MT, 16/07 MT, 17/07 MN.

**Đối chứng cùng kỳ 12–17/07** — các model OpenRouter khác cùng cohort: grok-4.20 rỗng 1/16 (6%), gpt-5.5 1/16 (6%), qwen3.7-max / kimi-k2.5 / glm-5.1 / glm-5.2 / gpt-oss-120b đều **0%** → lỗi CỤC BỘ của qwen3-max × config effort HIGH, không phải sự cố key hay hạ tầng (call vẫn HTTP 200 trên key mới).

### 1.3. Cơ chế lỗi
Bật `reasoning effort HIGH` (thí nghiệm E3a ngày 05/07) làm model đốt phần lớn/toàn bộ token vào thinking rồi trả `content` rỗng. Bộ cứu salvage (V10785 B3 — lấy JSON từ reasoning text) chỉ cứu được một phần, không đủ.

### 1.4. Fix đã deploy (12:40)
- Bỏ qwen3-max-thinking khỏi cohort `_MODELS_REASONING_HIGH` → quay lại `reasoning exclude:true` (nguyên config P1 đã chứng minh 0% rỗng).
- `max_tokens` 32768 → 24576 (nguyên P1).
- Registry đánh mốc `thinking_disabled_date=2026-07-17` — mọi bảng so găng tách 3 giai đoạn (trước 05/07 / 05–16/07 / từ 17/07), KHÔNG trộn.
- **Vì sao revert chứ không retire:** khi CÓ output model này trúng BT 33/82 ngày = 40%/30d — thuộc nhóm khá của shadow, đáng giữ lại đo tiếp ở config ổn định.
- Verify: lần chạy đầu config mới = MT ~16:4x hôm nay; recheck tỷ lệ rỗng 7 ngày (~24/07), kỳ vọng ~0%.

---

## 2. GROK 4.3 THINKING — ĐÃ LÊN SHADOW NGAY THEO LỆNH ANH

### 2.1. Verify trước khi đấu dây
- Slug `x-ai/grok-4.3` có thật trên OpenRouter (list 344 model): **$1.25/M in + $2.50/M out** (phía out RẺ HƠN GPT-5.5 12 lần: $30 vs $2.5), context 1M, hỗ trợ `reasoning`.
- **Smoke bằng key OpenRouter CHUNG: HTTP 200**, trả lời đúng, có trường `message.reasoning` (thinking thật), chi phí $0.0005/call.

### 2.2. Cấu hình đã deploy
- Registry: `grok-4.3` / label **Grok 4.3 Thinking** — `SHADOW_AUTO`, `output_eligible=0`, `shadow_only=1`, `first_run_date=2026-07-17`, 3 miền, 2 slot shadow. **KHÔNG đụng official.**
- Reasoning **effort HIGH** (đúng yêu cầu "suy luận sâu"), max_tokens 24576 đồng chuẩn nhóm grok.
- **KHÔNG cần key mới**: model tự resolve về key OpenRouter chung (verify sau restart: `grok-4.3 → sk-or-v1-82f…cf7a`, đường `DB_GENERAL`).
- Roster shadow 11 → **12** model; UI thấy 30 model; registry self-test PASS cả local lẫn VPS.
- Chi phí ước tính: ~$0.15–0.25/ngày cho 3 miền.

### 2.3. Lịch chạy thật
- Hôm nay 17/07: chuỗi MN sáng đã qua → grok-4.3 chạy 2 miền đầu **MT ~16:4x + MB ~17:4x**.
- **18/07 = ngày đủ 3 miền đầu tiên.** KHÔNG backfill quá khứ.
- Vai trò: ứng viên thay gpt-5.5 tại **CP-L6 19/07** — tới đó có sẵn 2 ngày data đầu làm bối cảnh.

---

## 3. TRẢ LỜI 3 CÂU HỎI KEY/TIER

### 3.1. "Key cũ hôm nay không phát sinh = chuyển đổi thành công rồi nhỉ?"
- **Đúng** cho OpenAI / Anthropic / DeepSeek / 6 key OpenRouter cũ (đã verify sáng nay V10813: key mới ăn $1.541, key cũ đứng yên) — anh disable là chuẩn.
- **Riêng Google cần chú ý:** dashboard AI Studio anh chụp hiển thị theo **múi giờ UTC-8**. Chuỗi MN chạy 04:00 sáng VN 17/07 = **13:00 trưa 16/07 giờ UTC-8** → usage "hôm nay" của mình nằm ở **cột Jul 16** trên biểu đồ, không phải key hết được dùng. Thực tế `gemini-2.5-flash` + `gemini-2.5-pro` (2 model OFFICIAL) **vẫn gọi key Google CŨ mỗi ngày** (DB `gemini_api_key` xác nhận trỏ key cũ AIza…sPc0).
- → **Anh giữ key Google cũ là ĐÚNG. Tuyệt đối chưa revoke 2 key Google cũ và chưa đóng account Tier-2 cũ** cho tới khi migrate official sang gemini-3.x (bàn tại CP-L6 19/07 — FU-V10812-GEMINI25-EOL). Google chặn gemini-2.5 với project mới nên mất key cũ = 2 lane official chết không cứu được.

### 3.2. "Nộp nhiêu tiền để lên Tier 2?"
Theo chính sách Google hiện hành (ai.google.dev/gemini-api/docs/billing + rate-limits, đọc 17/07/2026):

| Tier | Điều kiện | Cap chi/tháng |
|---|---|---|
| Tier 1 | Gắn billing account | $250 |
| **Tier 2** | **Đã thanh toán THẬT tích lũy $100 + 3 ngày** kể từ lần thanh toán thành công đầu tiên | $2,000 |
| Tier 3 | $1,000 + 30 ngày (hoặc làm việc với sales) | $20,000+ |

- Credit khuyến mãi KHÔNG tính — phải là tiền thật đã trừ vào thẻ.
- Upgrade TỰ ĐỘNG (≤10 phút–48h sau khi đủ điều kiện), không cần đơn từ.
- Tier tính theo BILLING ACCOUNT (cộng dồn mọi project + mọi dịch vụ Google Cloud trên account đó).
- **Thực dụng:** nạp/tiêu $100 → chờ 3 ngày → Tier 2. Lưu ý usage hệ mình trên account mới chỉ ~vài cent/ngày (gemma free + gemini-3.5-flash shadow) → **Tier 1 là quá đủ cho hệ này**; nâng Tier 2 chỉ cần thiết cho nhu cầu ngoài hệ (Antigravity…).

### 3.3. "Còn key nào nữa không?"
**KHÔNG cần thêm key nào.** Cấu trúc hiện tại đủ: 4 key hãng (OpenAI · Anthropic · DeepSeek · Google-AQ shadow) + 1 OpenRouter chung + 2 key Google cũ (giữ hộ gemini-2.5 official). Key xAI chính hãng CHƯA cần — grok-4.3 đi key OR chung; nếu sau 2–4 tuần shadow chứng minh tốt và promote thì mới nối `_call_xai` (~20 dòng) + key riêng cho rẻ thêm ~5%.

---

## 4. "CÒN ĐỀ XUẤT MODEL NÀO KHÔNG?" (ổn định cao, suy luận sâu)

**Khuyến nghị: KHÔNG thêm model nào nữa hôm nay** — để so găng grok-4.3 sạch (roster shadow đã 12 lane; thêm nhiều lane cùng lúc = nhiễu + tốn). Ứng viên ĐÃ THẨM GIÁ sẵn nếu CP-L6 muốn mở thêm:

| Ứng viên | Giá in/out per M | Ghi chú |
|---|---|---|
| qwen3.7-plus | $0.32 / $1.28 | Em út của qwen3.7-max đang chạy tốt (0% rỗng), ctx 1M, giá 1/4 |
| minimax-m3 | $0.30 / $1.20 | Rẻ nhất nhóm reasoning; CAVEAT: dòng m2.7 từng bị REMOVED 04/2026 vì phá format — cần smoke kỹ |
| gemini-3.1-pro | (Google direct) | Key AQ gọi PASS sẵn — ứng viên thay gemini-2.5-pro nhánh EOL |
| ~~kimi-k3~~ | $3 / $15 | Đắt — bỏ |

---

## 5. AN TOÀN + HẠ TẦNG

- Chỉ đụng nhánh SHADOW: 3 file deploy (`model_registry.py`, `gpt_analyzer.py`, `_provider_pricing_table.py`), sha256 local=VPS khớp, compile OK.
- **Hash 4 bảng official PRE=POST IDENTICAL** (predictions 10240 / final_bundles 418 / lottery_results 15088 / model_daily_eval 10064).
- `/du-doan`, bundle writer, selector, prompt, A/B V10809: **KHÔNG đổi** (không model nào trong 2 nhánh sửa hôm nay nằm trong A/B).
- Restart 12:40 giữa trưa an toàn (job kế tiếp gần nhất: T-chốt MN 15:45); health 200, admin 401, journal startup sạch.
- Backup 2 đầu: local `backups/v10814_pre/` + VPS `backups/v10814_vps/`.
- Ghi chú kỹ thuật cho phiên sau: **journalctl VPS chỉ giữ ~39MB** → log chuỗi sáng bị rotate mất lúc trưa; bằng chứng phải lấy từ DB + OpenRouter usage API (đã áp dụng hôm nay).

## 6. VIỆC CHỜ PHÍA TRƯỚC (không rơi rớt)

| Khi nào | Việc |
|---|---|
| Chiều nay 16:4x + 17:4x | Verify grok-4.3 2 row đầu + qwen3-max hết rỗng |
| Tối nay 19:15 | Shadow A/B V10809 day-2 chấm điểm |
| Owner quyết | B1 hạ reasoning gpt-5.5 (còn HIGH — còn đốt ~$1.3/ngày); revoke key nhóm A+B (đèn xanh V10813); CẤM 2 key Google cũ |
| 18/07 | grok-4.3 ngày đủ 3 miền đầu + CP-S1 shadow A/B |
| 19/07 CN | CP-L6: retire gpt-5.5 (grok-4.3 thế chỗ) + glm-5.1 + CP-R4 + gemini-3.5 swap + K11a + CP-4.0 ack; 02:00 retrain subprocess lần đầu |
| ~24/07 | Recheck qwen empty-rate 7 ngày |

*Báo cáo public — key/API đã mask. Chi tiết code + probe nằm ở repo private `Lottery_AI_Test` (V10814).*
