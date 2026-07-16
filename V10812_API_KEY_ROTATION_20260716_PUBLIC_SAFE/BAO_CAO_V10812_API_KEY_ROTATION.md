# V10812 — THAY TOÀN BỘ API KEY (5 KEY MỚI) + DỌN 22 BIẾN ENV LEGACY + PHÁT HIỆN GOOGLE CHẶN GEMINI-2.5 VỚI PROJECT MỚI + ĐỀ XUẤT THAY GPT-5.5

- Thời gian: 2026-07-16 22:54 → 23:5x (giờ VN)
- Trạng thái: **DEPLOYED — chờ live-verify chuỗi sáng 17/07**
- An toàn: hash 4 bảng official PRE=POST **IDENTICAL**; `/du-doan` 15/15, lane 20/20, prompt production KHÔNG ĐỘNG
- Bảo mật: báo cáo này chỉ chứa key MASKED (8 đầu + 4 cuối). Key đầy đủ chỉ nằm ở file owner + DB/env VPS (gitignored).

## 1. Yêu cầu owner (22:54)

> "Anh gửi em thông tin API key nha em. tiến hành xử lý dùm anh nhé. có vài vấn đề anh nhờ em kiểm tra trong ảnh các key đã dừng sử dụng 12, 4 ngày trong hệ thống còn hoạt động không em? xem kỹ dùm các model có còn hoạt động thì add bằng key chung không thì clear sạch sẻ dùm anh nhé em.
> - Hiện tại chi phí GPT 5.5 cao quá em cần có kế hoạch thay thế gấp đi em chi phí lớn quá em ơi. Hiện có một số model mới giá rẻ cũng mạnh mẻ không kém như grok ah, em xem thử model nào phù hợp đề xuất dùm anh nhé. Nếu ok anh sẽ tạo key chính hãng từ trang chủ cho ít lỗi và mạnh mẻ nha em.
> Danh sách API Key đính kèm em làm cẩn thận tỉ mỉ verify đầy đủ nha em"

## 2. Trả lời "key dừng dùng 12 / 7 / 4 ngày còn hoạt động không?"

| Key trên dashboard | Usage lifetime | Model | Trạng thái model | Xử lý |
|---|---|---|---|---|
| Qwen3.6 Plus | $4.71 (12 ngày trước) | qwen3.6-plus | **RETIRED 04/07** (lean harvest V10779) | Clear — revoke NGAY được |
| Qwen3 Coder 480B | $2.61 (12 ngày trước) | qwen3-coder | **RETIRED 04/07** | Clear — revoke NGAY được |
| Cohere: Rerank 4 Pro | $0.638 (7 ngày trước) | cohere-rerank-4-pro | **ĐÃ THÁO 09/07** (V10789: 247 mẫu helped=0) | Clear — revoke NGAY được |
| OpenAI: GPT-5.5 | **$71.92** (5 giờ trước) | gpt-5.5 | SHADOW_AUTO — chạy hằng ngày | Đã chuyển key chung mới |
| OpenAI: GPT-OSS-120b | $0.924 (5 giờ) | gpt-oss-120b | SHADOW_AUTO | Đã chuyển key chung mới |
| Qwen: Qwen3 Max Thinking | $8.59 (4 giờ) | qwen3-max-thinking | SHADOW_AUTO | Đã chuyển key chung mới |
| MoonshotAI: Kimi K2.5 | $10.62 (4 giờ) | kimi-k2.5 | SHADOW_AUTO | Đã chuyển key chung mới |
| Lottery DDXS | $0.000 (chưa dùng) | — | Chính là key OpenRouter MỚI anh vừa tạo | Đang là key chung production |
| (ẩn dưới scroll) Grok | **$36.31** | grok-4.20-multi-agent | SHADOW_AUTO | Đã chuyển key chung mới |
| (ẩn dưới scroll) key chung cũ a3a…151 | $25.38 | glm-5.1/5.2, qwen3.7-max + fallback | — | Thay bằng key chung mới |

Lưu ý: mấy key "4 giờ trước" là **4 GIỜ** (đang sống), không phải 4 ngày. Tổng usage lifetime các key OpenRouter cũ: **$187.09** (đọc trực tiếp API `/api/v1/key` từng key — không cần scroll dashboard).

## 3. Smoke test 5 key mới TRƯỚC khi đụng config

| Hãng | Kết quả | Chi tiết |
|---|---|---|
| OpenAI | ✅ PASS | gpt-5-mini + gpt-5.4 đều có quyền; chat call OK |
| Anthropic | ✅ PASS | chat OK; models.list thấy cả sonnet-5 / opus-4-8 (tương lai có đường nâng cấp) |
| DeepSeek | ✅ PASS | deepseek-v4-flash + v4-pro; chat OK |
| OpenRouter | ✅ PASS | 344 model, chat OK, credit account-level hoạt động |
| Google (key `AQ.*`) | ⚠ PASS CÓ ĐIỀU KIỆN | Key hợp lệ nhưng Google trả **404 "gemini-2.5-flash/pro is no longer available to NEW users"** — 2 model official chỉ sống trên project CŨ. Key AQ gọi được: gemma-4-31b ✔, gemini-3-flash ✔, gemini-3.1-pro ✔, gemini-3.5-flash ✔ (retry sau 503 tạm) |

**Hệ quả quan trọng (FU-V10812-GEMINI25-EOL):** gemini-2.5-flash/pro official là "tù nhân" của project Google cũ. **TUYỆT ĐỐI KHÔNG revoke 2 key Google cũ.** Lộ trình thoát: gemini-3.5-flash shadow 33 ngày BT 42% (cao nhất cohort) — CP-L6 bàn migrate official sang 3.x rồi mới gộp về 1 key Google.

## 4. Swap đã làm gì (staged, có rollback, verify từng bước)

1. **Hash 4 bảng PRE** → backup `.env` + dump DB ai_keys + `cohere_rerank.py` vào `/root/backups/v10812_pre/`.
2. **DB `ai_keys`:** openai/anthropic/deepseek/openrouter_api_key = key mới; `gemini_key_shadow_new` = key AQ (chỉ shadow); **`gemini_api_key` giữ nguyên key cũ**; xóa orphan `openrouter_key_kimi_k26`.
3. **`.env` VPS:** thay 4 key chung; **DỌN 22 biến legacy** (18 `OPENROUTER_KEY_*` + `DEEPSEEK_SHADOW_API_KEY` + `GEMINI_KEY_SHADOW_NEW` + `XAI_API_KEY` rỗng) — bắt buộc vì per-model env có độ ưu tiên CAO HƠN key chung; giữ nguyên các biến không phải key. Local `.env` đồng bộ cùng cấu trúc.
4. **Fix kèm:** `cohere_rerank.py` fallback DB đọc sai category (`api_keys` → `ai_keys`) — nhánh chết im lặng từ đầu.
5. **Restart + verify:** service active, health 200, admin no-auth 401, journal watchdog OK.
6. **Verify resolve key 19/19 PASS** — từng model trỏ đúng nguồn kỳ vọng:
   - claude-* → key Anthropic mới; gpt-5-mini/5.4 → key OpenAI mới; deepseek-reasoner + v4-pro-real → key DeepSeek mới (shadow fallback đúng thiết kế)
   - 8 model OpenRouter (gpt-5.5, oss-120b, qwen3-max, qwen3.7, glm-5.1, glm-5.2, kimi, grok) → `KEY_MODE=DB_GENERAL` key chung mới
   - gemini-2.5-flash/pro → key CŨ (không đổi); gemini-3.5-flash + gemma-4-31b → `DB_GOOGLE_SHADOW` key AQ mới; rerank fallback → key chung mới
7. **Hash 4 bảng POST = PRE IDENTICAL** (predictions 10200/d2732c81, final_bundles 417/761958a3, lottery_results 15088/b43f6694, model_daily_eval 10064/999fc5db).

## 5. GPT-5.5: chi phí thật + đề xuất thay (owner giục "gấp")

**Chi phí:**
- Giá OpenRouter thật: gpt-5.5 **$5/M in + $30/M out** — so cohort: grok-4.20/4.3 $1.25/$2.50, grok-4.5 $2/$6, kimi $0.57/$2.85, glm-5.2 $0.92/$2.90, qwen3.7 $1.48/$4.42.
- Từ khi bật reasoning effort HIGH (05/07, V10781 E3c): thêm ~23K reasoning token/ngày (tính giá OUT $30/M) → **~$1.3/ngày, gấp ~2.5 lần trước**; lifetime $71.92 = **38% tổng chi OpenRouter** ($187.09).
- Hiệu năng: BT trước/sau bật HIGH = **37% → 27%** (n=84/33) — đắt hơn để TỆ hơn 10pp. 14d BT 29% thua grok 38%, qwen3.7 40%, gemini-3.5 42%.

**Grok minh oan:** trace 35.6M token/7 ngày là số nội bộ multi-agent — **bill thật chỉ $36.31 lifetime ≈ $0.40/ngày**, BT 30d 37% nhóm đầu. Không phải hố tiền.

**Đề xuất 2 bước (chờ owner OK):**
- **B1 (ngay, 1 dòng):** hạ reasoning effort gpt-5.5 HIGH → default. Tiết kiệm ~60% chi phí model này, prior hiệu năng 37% BT có cơ sở quay lại. Giữ đo lường liên tục.
- **B2 (CP-L6 19/07):** RETIRE gpt-5.5 hẳn + onboard **x-ai/grok-4.3** ($1.25/$2.50, ctx 1M — kế nhiệm 4.20, KHÔNG multi-agent) làm shadow lane qua key OpenRouter chung (~15 dòng registry+slug+pricing, zero key mới). Option premium: grok-4.5 ($2/$6 — vẫn rẻ hơn gpt-5.5 5 lần ở output).
- **Key chính hãng xAI (anh đề nghị tạo):** code đã có sẵn route `_call_xai` (api.x.ai) + biến `XAI_API_KEY` — em nối (~20 dòng) SAU khi grok-4.3 chứng minh 2-4 tuần shadow, đỡ phí nạp OpenRouter và ít 429 hơn.
- An toàn: gpt-5.5 KHÔNG nằm trong shadow A/B V10809 (cohort: opus, qwen3.7, deepseek-reasoner, gemini-2.5-flash, gpt-5-mini) → cắt không đụng thí nghiệm đang chạy.

## 6. Hướng dẫn revoke key cũ cho owner

- **NHÓM A — revoke NGAY được (model đã nghỉ):** Qwen3.6 Plus, Qwen3 Coder 480B, Cohere Rerank 4 Pro.
- **NHÓM B — revoke SAU khi em verify chuỗi sáng 17/07 chạy sạch key mới:** GPT-5.5, GPT-OSS-120b, Qwen3 Max Thinking, Kimi K2.5, Grok, key chung cũ (a3a…151) trên OpenRouter + key OpenAI cũ + key Anthropic cũ + 2 key DeepSeek cũ + key Google shadow cũ (AIzaSyCmiW…).
- **TUYỆT ĐỐI GIỮ:** 2 key Google cũ (DB AIzaSyDz…sPc0 + env AIzaSyB4…ITaY) — gemini-2.5-flash/pro official chết ngay nếu revoke (Google không cấp quyền 2.5 cho key mới nữa).

## 7. Follow-up items

| FU | Trạng thái | Nội dung |
|---|---|---|
| FU-V10812-KEY-SWAP | DEPLOYED_PENDING_LIVE_VERIFY | Verify chuỗi MN 04:15 sáng 17/07 + shadow 11 model + official 8 model, 0 lỗi 401/403 → báo owner revoke NHÓM B |
| FU-V10812-GPT55-REPLACE | AWAITING_OWNER | B1 hạ effort / B2 retire + grok-4.3 (CP-L6 19/07) |
| FU-V10812-GEMINI25-EOL | OPEN (RISK) | Official Google phụ thuộc project cũ; CP-L6 bàn migrate gemini-3.5-flash |

## 8. Artifacts

`_v10812_key_audit.py`, `_v10812_cost_perf.py`, `_v10812_smoke_keys.py`, `_v10812_google_probe.py`, `_v10812_trace_cost.py`, `_v10812_swap.py`, `_v10812_or_key_usage.py`, `_v10812_journal_check.py`, `_v10812_g35_retry.py` (repo private); backup `/root/backups/v10812_pre/` (VPS).
