# V10784 — BÁO CÁO PARTIAL #2 (PHẦN 1 + PHẦN 2 + tiến độ P3/P4) — 18:4x 05/07/2026

(Nộp sớm trước hạn 21:00 — P1/P2 đã đóng xong, P4 cũng đã xong 4/4.)

## PHẦN 1 — LOGGING ✅ 4/4

### 1.1–1.2 Parse reasoning + custom_prompt trace (deploy 17:17)

- `predictions` thêm cột `reasoning_tokens` (migration tự động).
- `_call_openrouter`: đọc `message.reasoning` (và `reasoning_content` một số provider) + `usage.completion_tokens_details.reasoning_tokens` — trước đây BỊ VỨT.
- `_call_deepseek`: trả `reasoning_content` + reasoning_tokens ra caller (trước chỉ log độ dài).
- `_call_gemini`: `thoughts_token_count` → reasoning_tokens.
- `reasoning_json` per row nhận `reasoning_tokens` + `native_reasoning_excerpt` (3000 chars).
- `prediction_trace.jsonl`: thêm `reasoning_tokens` + `custom_prompt.applied_text` đầy đủ (FU V10782 trace 15h đã đóng).
- Nối đủ 4 đường ghi: ai_chain, rerun, shadow_auto_eval (fix bug shadow không lưu reasoning_json), api manual.

### 1.3 Smoke 3 model — ALL PASS (log `smoke_reasoning_v2.log` 18:03–18:29)

| Model | reasoning_tokens (API) | Ghi DB | reasoning text | PASS |
|---|---|---|---|---|
| qwen3-max-thinking | 1,503 | 1,503 | 5,826 chars | ✅ |
| grok-4.20-multi-agent | 20,589 | 20,589 | 0 chars (provider không trả text, chỉ count — ghi nhận trung thực) | ✅ |
| gpt-5.5 | 57 | 57 | 428 chars | ✅ |

Ghost rows đã xóa sau verify. Lưu ý chi phí: grok multi-agent 104,868 tokens/call (~$0.21) — circuit breaker tự mở 10' đúng thiết kế.

**Bằng chứng live bổ sung (không phải smoke):** shadow MB tối nay ghi reasoning thật: grok=78,346 · gpt-5.5=8,804 · glm-5.2=6,364 · kimi-k2.5=5,803 · glm-5.1=5,446 · gpt-oss-120b=4,156 · deepseek-reasoner (official)=8,988.

### 1.4 Checklist verify tự động sáng 06/07 ✅

`_v10784_verify_0607.py` + cron 07:30 06/07: C1 reasoning>0 (3 E3 + qwen3.7-max; glm-5.2 + Gemini lane mới informational) · C2 first-run 2 model mới · C3 /choi MN=MN_BT1_OFFICIAL_V1 · C4 prompt 3 miền đúng đài THỨ HAI (trace vs station calendar) · C5 freeze fire 3 mốc hôm trước · C6 eval đơn model đủ 3 miền. Output JSON vào `artifacts/v10784/`.

## PHẦN 2 — METHOD LOCK ✅ 3/3 (đóng từ 17:33–17:36, chi tiết ở partial #1 + đây)

- **2.1** `/choi` in method lock tuần đủ 3 miền (upload 17:33): "Method tuần này: MN=MN_BT1_OFFICIAL_V1 (BT 1-số, nghỉ T7) · MT=MT_ADAPTIVE_EXPLOIT_V1 · MB=MB_ADAPTIVE_EXPLOIT_V1" + khóa từ + tham chiếu quyết định + published_at.
- **2.2** Audit hồi tố toàn lịch sử (`_v10782_p2_seed_audit.py` chạy trên VPS): KHÔNG có đổi method giữa tuần thật; 2 nhóm artifact lịch sử được ghi nhận trung thực (locked_date giữa tuần cho tuần 29/06 + locked_at sau giờ kết quả 04/07) — do bảng lock TẠO SAU (V10782), không phải method switch thật. P&L lịch sử chấm theo method lock tại thời điểm đó.
- **2.3** Commit private governance: `58eb3fc` (17:36) — CHANGELOG + AUTOMATION_STATE seq 239 + SSOT + FU tracker + toàn bộ code P0–P2.

## PHẦN 3 — GEMINI SHADOW LANE (deploy 18:09, trước deadline 23:30) ✅ đăng ký xong

**Audit config Gemini hiện tại:**

| Lane | API id | Key | Route | Thinking | Log reasoning |
|---|---|---|---|---|---|
| gemini-2.5-flash (OFFICIAL) | gemini-2.5-flash | GEMINI_API_KEY (legacy) | google.genai direct | default dynamic (không set budget trong code) | thoughts_token_count → reasoning_tokens (V10784 P1) |
| gemini-2.5-pro (OFFICIAL) | gemini-2.5-pro | GEMINI_API_KEY | google.genai direct | luôn thinking | như trên |
| gemini-3.1-pro (shadow) | gemini-3.1-pro-preview | GEMINI_KEY_SHADOW_NEW | google.genai direct | dynamic | như trên |
| gemini-3-flash (shadow) | gemini-3-flash-preview | GEMINI_KEY_SHADOW_NEW | như trên | dynamic | như trên |
| gemma-4-31b (shadow) | gemma-4-31b-it | GEMINI_KEY_SHADOW_NEW | như trên | n/a | n/a |

Ghi chú trung thực: docstring cũ trong `_call_gemini` nói "thinking_budget=0 disables thinking" nhưng CODE THẬT không set thinking_config → mọi lane Gemini chạy thinking mặc định (dynamic). Không đổi hành vi trong phiên này (official giữ nguyên).

**Lane mới đăng ký (KHÔNG đụng 2 lane official):**

- `gemini-3.5-flash` — bản Flash STABLE mới nhất (ListModels probe 17:43; mới hơn gemini-3-flash-preview). SHADOW_AUTO, `shadow_only=1`, `output_eligible=0`, `first_run_date=2026-07-06`, `thinking_enabled_date=2026-07-06` (mốc riêng), key shadow cohort, thinking dynamic + reasoning_tokens log qua P1.
- **First-run gate MỚI (fix hệ thống):** `get_shadow_models_active_on(date)` — lane có first_run_date tương lai bị loại khỏi run + expected count + catch-up. Verify live sau deploy: active hôm nay = 8 model (KHÔNG có gemini-3.5-flash/qwen3.7-max/glm-5.2), active 06/07 = 11 (có đủ).

**⚠ PHÁT HIỆN TRUNG THỰC (pre-existing, không phải lỗi phiên này):** 2 lane V10781 (qwen3.7-max, glm-5.2) khai `first_run 2026-07-06` nhưng ĐÃ CHẠY HÔM NAY 05/07 (MN 15:28–15:30, MT 17:18, MB 17:45) vì trước 18:09 chưa có gate nào enforce first_run_date. Rows là shadow-only (zero official impact), giữ nguyên không xóa; cửa sổ đo từ 06/07 tự nhiên loại chúng. Gate V10784 đóng vĩnh viễn lớp lỗi này. → đưa vào bảng chờ ký: owner quyết có loại 3 rows/lane ngày 05/07 khỏi so găng không.

## PHẦN 4 — XONG SỚM 4/4 (chi tiết file riêng trong folder này)

- **4.1** History filter + phân trang server-side: API `offset`+`total_count` (verify live total_count=5202), UI index.html thêm lọc LANE (official/shadow) + pager; user-view.js chuyển server-side pagination + mặc định 7 ngày. Deploy backend 18:09 + frontend 18:16 (hash VPS = local `18e9def3…` verified).
- **4.2** Ma trận độc lập miền×thứ×tuần: `P42_MA_TRAN_DOC_LAP_MIEN_THU_TUAN.md` — 5 lớp × ~30 tham số gắn nhãn; 3 đề xuất tách chờ ký (ĐX-1 skip/confirm threshold per miền, ĐX-2 output_eligible per miền qua allowed_regions sẵn có, ĐX-3 reasoning effort GIỮ + đo 14 ngày).
- **4.3** CYCLE SCAN: bảng `cycle_scan_shadow_v10784` (1,614 cells, 696 đủ mẫu) + API `/api/admin/cycle-scan` (401 unauth ✅) + panel /monitoring (auto-refresh 60s) — deploy 18:57. Sanity: MN D-1 per-day đề∈lô hôm trước = 82.4% (n=369 window dài) / 75.4% (từ 10/05) — khớp mức ~73-82% owner nhớ; per-trial 45.5% vs base 43% (edge mỏng — số liệu trung thực). MB G2: per-day prevG2∈lô lag7=50%/lag28=50% (từ 10/05), lag2=44.9% (window dài) — tín hiệu G2 lag có mặt nhưng cell-level cần thêm mẫu. Top cells OOS-dương ổn định: MT T2 lag7 DB→LO2 +20.6pp (OOS +51pp, n=16), MN T2 lag28 DB→LO2 +25.5pp (OOS +48pp, n=24)... CẤM áp official trước 14/07 (flag trong bảng + API + UI).
- **4.4** Ma trận trùng lặp: `P44_MA_TRAN_TRUNG_LAP_GIU_HOPNHAT_BO.md` — 7 cụm, ~14 endpoint + ~12 card đề xuất BỎ/HỢP NHẤT, 5 hành động chờ ký S1–S5. KHÔNG xóa gì phiên này.

## P0.4 ĐUÔI — MB EVAL SAU KẾT QUẢ ✅

Kết quả MB về 18:31:01 (retry tự động sau 2 lần scrape fail 18:30 — bình thường). Verify chạy ngay: MB 24 rows PENDING → WIN 3 / PARTIAL 3 / LOSE 18 (đủ cả ai_chain + rerun + shadow). Freeze KHÔNG chặn verify/eval — đúng thiết kế whitelist. `model_daily_eval` 20:20 sẽ chốt ở báo cáo tổng.

## CÒN LẠI TRƯỚC 00:00

P5.1 hash 4 bảng (natural growth only) · P5.2 check 23:50 money_board_lock tuần 06/07 · P5.3 báo cáo tổng + Notion ≤30 dòng + 26_RUNTIME_AS-BUILT (đã định vị page id `ea141094…`) + AUTOMATION_STATE · commit private/public.

Không có mục BLOCKED.
