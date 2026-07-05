# V10784 — BÁO CÁO PARTIAL #1 (PHẦN 0) — 18:15 05/07/2026

Hợp đồng thực thi V10784, mốc deliverable #1. Phạm vi: P0.1–P0.5 (khẩn trước 17:45–18:00).

## TÓM TẮT 1 DÒNG

P0 hoàn thành 5/5 hạng mục — eval đơn model được cứu bằng whitelist freeze (deploy 17:03, trước MB), freeze MT/MB verify đủ bằng chứng DB + journal, watch script sống lại từ 17:06, user-view.js (surface=official) đã upload 18:05.

## P0.1 — CỨU EVAL ĐƠN MODEL ✅ (deploy 17:03, trước hạn 17:45)

**Chẩn đoán (probe read-only `_v10784_p0_probe.py`):**

- `model_daily_eval` KHÔNG bị freeze chặn — bảng này ghi qua job 20:20 và không đi qua `save_prediction` (nhịp 8 ngày liên tục, hôm qua 68 rows lúc 20:20:00).
- `lottery_results` KHÔNG bị chặn — kết quả MN 16:34:35 + MT 17:30:00 ghi bình thường.
- Mất shadow eval MT (0 rows lúc 17:00 vs 13 hôm qua) nguyên nhân THẬT: service restart 16:38:38 (deploy V10783 P0) giết trigger shadow eval sau AI chain MT — KHÔNG phải freeze. Bằng chứng: journal `Shadow Auto-Eval` không fire sau restart; freeze hook chỉ nằm trong `save_prediction`.
- Tuy nhiên trace code xác nhận GAP THẬT: nếu shadow/test lane ghi row sau mốc freeze qua `save_prediction` thì bị dính `late=1` hoặc chặn — vi phạm thiết kế "freeze chỉ áp official surface".

**Hotfix whitelist (`_v10782_freeze.py` + `database.py` + `scheduler.py`):**

- `FREEZE_EXEMPT_TAGS = (shadow, test, eval, smoke, lane, backfill, pv2)` — mọi `run_source` chứa tag đi qua tự do (không block, không late=1).
- Official chain (`auto_daily`, `ai_chain`, `rerun_post_*`, fallback, manual) KHÔNG khớp tag nào → freeze giữ nguyên như V10782.
- Bỏ check `is_frozen` trong trigger materialize test panel (test lane tự do đúng thiết kế).

**Smoke sau deploy (`_v10784_p0_smoke2.py`, ghost rows, 17:04):**

| Case | Kết quả |
|---|---|
| Shadow write sau freeze | PASS — đi qua, `late=0` |
| Official write MỚI sau freeze | PASS — ghi được nhưng gắn `late=1` (đo lường) |
| Official OVERWRITE row cũ sau freeze | PASS — BỊ CHẶN |

**Backfill MT theo cơ chế chuẩn:** `_run_shadow_auto_eval('MT')` chạy lại 17:04→17:20 — 10 rows shadow MT (0 late). MB tối nay 9 rows shadow ghi 17:34–17:45 tự nhiên, KHÔNG dính freeze (nhờ hotfix). Eval MB sau kết quả ~18:30 sẽ verify tiếp ở partial #2.

## P0.2 — VERIFY FREEZE MT HẬU KIỂM ✅

| Mốc | Bằng chứng |
|---|---|
| T-10 16:45 | Journal: job `🔒 T-10 chốt bundle MT (16:45)` executed successfully |
| Bundle MT chốt | `final_bundles` MT bach_thu=49 v2, không đổi sau 16:45 |
| Official write cuối | 16:37:59 (trước freeze 16:55 — đúng) |
| Sau 16:55 | 0 write official mới; chỉ shadow_auto_eval (whitelist, late=0) |
| Card đứng yên | Watch 17:06→18:00: official_rows=15 + bt=49 bất động 100% |

## P0.3 — WATCH SCRIPT SỐNG LẠI ✅ (17:06, trước hạn 17:40)

Nguyên nhân fail cũ: gọi API path sai + stdout buffer không flush. Fix: query SQLite trực tiếp (`final_bundles` + `predictions`) + `line_buffering=True`. Timeline `artifacts/v10783_p0/watch_timeline.jsonl` ghi 15+ events từ 17:06, phủ cả MT lẫn MB.

## P0.4 — MB LIVE ✅ (phần quan sát; eval 18:30 verify ở partial #2)

| Mốc | Bằng chứng |
|---|---|
| T-10 17:45 | Journal: job `🔒 T-10 chốt bundle MB (17:45)` executed successfully (17:45:00,231) |
| Bundle MB chốt | bach_thu=70, v1 17:33:28 → v2 17:45:01 bởi single-flight T-10 (bt không đổi) |
| Official cuối | 17:33:27 (combo-super) — TRƯỚC freeze 17:55 |
| Sau 17:55 | 0 write official; watch xác nhận official_rows=15 + bt=70 đứng yên |
| Shadow MB | 9 rows 17:34:42→17:45:42, late=0 — whitelist hoạt động đúng ngay lần đầu |
| Không deploy 17:45–18:00 | Tuân thủ — deploy kế tiếp 18:08 (sau cửa sổ) |

**Bonus bằng chứng P1 hoạt động thật trên live:** shadow MB tối nay đã ghi `reasoning_tokens` thật vào DB: grok-4.20-multi-agent=78,346 · gpt-5.5=8,804 · glm-5.2=6,364 · kimi-k2.5=5,803 · glm-5.1=5,446 · gpt-oss-120b=4,156 · deepseek-reasoner (official ai_chain)=8,988. (qwen3-max-thinking=NULL — đang điều tra ở P1.3, nghi provider không trả reasoning qua route hiện tại.)

## P0.5 — USER-VIEW.JS SURFACE=OFFICIAL ✅ (upload 18:05)

Backup `.bak_v10784` trên server trước khi ghi đè; verify grep dòng 409 `surface: 'official'` trên VPS. Card/history user-view giờ chỉ đọc official surface — hoàn tất tách hiển thị lane test.

## TIẾN ĐỘ SỚM PHẦN SAU (deploy 18:08, ngoài cửa sổ cấm)

- **P3:** Đăng ký lane `gemini-3.5-flash` (SHADOW_AUTO, shadow_only=1, output_eligible=0, first_run 06/07, thinking_enabled_date 06/07) + **first_run gate mới** trong registry/scheduler: lane có `first_run_date` tương lai bị loại khỏi run + expected count (verify live: active hôm nay KHÔNG có gemini-3.5-flash, active 06/07 CÓ). Không đụng 2 lane Gemini official.
- **P4.1:** `/api/predictions` thêm `offset` + `total_count` (phân trang server-side) — verify live: total_count=5202, offset hoạt động.
- **P1.3:** Smoke reasoning 3 model đang chạy nền trên VPS (log unbuffered mới) — kết quả vào partial #2.

## HẠNG MỤC CHỜ MỐC THỜI GIAN

- Eval MB sau kết quả ~18:30 (P0.4 đuôi) — check ở partial #2.
- `model_daily_eval` 20:20 hôm nay — check ở partial #2.

Không có mục BLOCKED. Không có mục cần chữ ký owner trong P0.
