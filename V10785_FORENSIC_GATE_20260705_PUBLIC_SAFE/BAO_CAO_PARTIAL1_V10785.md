# V10785 — BÁO CÁO PARTIAL #1 — 21:05 05/07/2026

Hợp đồng V10785 (forensic + coverage + đóng mảnh treo + gate 06/07). Partial ~2h đầu tiên.

## TÓM TẮT

- **PHẦN A forensic**: timeline 04:00→nay dựng xong; re-verify 6/6 claim — 5 ĐÚNG, 1 claim P2.1 cần đính chính cách diễn đạt (lock line /choi chỉ hiện từ tuần 06/07, không phải "đã hiện hôm nay"); phát hiện T-10 MN 15:45 hôm nay KHÔNG fire (code deploy 16:03 SAU mốc — tự lành từ mai, watchdog đã canh).
- **PHẦN B**: bảng phủ sóng 7 ngày xong; root cause đủ; **B2 fix deploy 20:33** (late-fill + per-model timeout + watchdog heartbeat + startup-recovery); **B3 sandbox 25 lane: 24/25 OK ngay vòng đầu** (qwen3-max-thinking đang retry 600s), production 0 rows đụng.
- MDE 20:20 tối nay: **74 rows / 3 miền ghi bình thường** — hotfix whitelist V10784 hoạt động đúng ngày đầu.

## A1 — TIMELINE 04:00 → 21:00 (từ journal + DB + syslog)

| Giờ | Sự kiện | Ghi chú |
|---|---|---|
| 04:00–04:18 | ML 04:00 + MN AI chain + bundle MN v1 04:17:47 | auto_daily 15+7 rows |
| 08:15–08:30 | Shadow eval MN (trigger owner_v10782_p0_repredict 15:15) | 9 rows |
| 15:40–15:45 | T-10 MN 15:45 **KHÔNG fire** | code T-10 deploy 16:03 SAU mốc — bundle MN giữ v1 04:17 |
| 16:03:51 | restart #1 (deploy V10782 freeze+seed) | T-10/freeze jobs armed từ đây |
| 16:30–16:34 | Scrape MN fail→OK 16:34:35 (3 đài) | verify MN chạy, bundle verified_at 16:34:35 |
| 16:38:02 + 16:38:39 | restart #2+#3 (V10783 P0 deploy, double restart 37s) | giết trigger shadow MT — bài học watchdog |
| 16:42–16:45 | AI chain MT (8 rows ai_chain) + T10_CHOT MT 16:45:03 BT=49 v2 | freeze 16:55 giữ nguyên |
| 17:03–17:05 | restart #4 (V10784 hotfix whitelist freeze) | trước MB đúng deadline |
| 17:07–17:20 | Backfill shadow MT 10 rows (late=0) | cơ chế chuẩn `_run_shadow_auto_eval` |
| 17:22 | restart #5 (V10784 P1 reasoning parse) | |
| 17:30 | Scrape MT OK 17:30:00 | verify MT + bundle MT verified 17:30:01 |
| 17:33–17:45 | AI chain MB (8 rows) + rerun_post_mt 7 rows + bundle MB v1 17:33:28 → T10_CHOT MB 17:45:00 BT=70 v2 | |
| 17:34–17:46 | Shadow MB 9 rows tự nhiên (whitelist pass, late=0) | +19 rows shadow_auto_eval trong giờ 17h |
| 18:09 / 18:29 | restart #6 (P3 gemini lane + P4.1 pagination) / #7 (P1.1 shadow reasoning persist) | ngoài cửa sổ cấm |
| 18:30–18:31 | Scrape MB fail→OK 18:31:01 (Thái Bình) + verify + bundle verified 18:31:02 | |
| 20:00 / 20:20 | Daily Eval + **MDE 74 rows 3 miền 20:20:00** | eval đơn model SỐNG lại sau hotfix |
| 20:31 + 20:33 | restart #8+#9 (V10785 B2 deploy + fix tzinfo) | ngoài cửa sổ live; startup-recovery fire 20:34:47 ✅ |

**Write 4 bảng official hôm nay**: predictions 05/07 = 84 rows (15 official/miền + shadow + backfill); final_bundles 3 (MN 04:17/MT 16:38→v2 16:45/MB 17:33→v2 17:45); lottery_results 7 stations (16:34/17:30/18:31); model_daily_eval 74 rows 20:20. KHÔNG có write official surface nào sau mốc freeze từng miền.

**Hành động NGOÀI prompt được giao**: không phát hiện hành động thừa; các restart đều gắn với deploy được prompt yêu cầu. Điểm trừ vận hành: double-restart 16:38 (2 lần trong 37s) gây mất trigger shadow MT — đã có startup-recovery từ 20:33 chống tái diễn.

## A2 — RE-VERIFY 6 CLAIM (không tin báo cáo cũ)

| Claim | Kết quả re-verify | Bằng chứng |
|---|---|---|
| Freeze fire 3 mốc | **MT+MB ĐÚNG; MN cần chú thích** | T10_CHOT MT 16:45:03 + MB 17:45:00 (DB scheduler_logs); freeze block hoạt động (sandbox 2 chiều dưới). MN: mốc 15:45/15:55 hôm nay KHÔNG có T-10 vì code deploy 16:03 SAU mốc — is_frozen(MN) vẫn active từ 16:03. Từ mai T-10 MN armed (job registered, watchdog canh) |
| Whitelist eval 2 chiều | **PASS 5/5 (sandbox copy 483MB, prod untouched)** | (a) official new sau freeze → late=1 ✔ (b) official overwrite row verified → CHẶN ✔ (b2) overwrite row PENDING → CHẶN (FREEZE_LATE_SKIP) ✔ (c) shadow sau freeze → pass late=0 ✔ (d) run_source chứa 'eval' → pass late=0 ✔; hash predictions prod trước/sau IDENTICAL (9342\|21433) |
| reasoning_tokens ghi DB thật | **ĐÚNG** — query lại predictions 05/07: 8 rows rt>0 live (grok 78,346 · deepseek-reasoner 8,988 · gpt-5.5 8,804 · glm-5.2 6,364 · kimi 5,803 · glm-5.1 5,446 · gpt-oss 4,156 · ds-v4-pro-real 644); 22 shadow rows NULL = rows trước 18:29 (code P1.1 deploy 18:29) + model không trả reasoning | DB query trực tiếp |
| Backfill MT shadow 10 rows | **ĐÚNG cơ chế chuẩn** — 10 rows 17:07:05→17:19:48, late=0, run_source=shadow_auto_eval, trigger `_run_shadow_auto_eval('MT')` | DB query |
| Seed lock tuần 06/07 nguyên vẹn | **ĐÚNG** — 3 rows: MN=MN_BT1_OFFICIAL_V1 (bt1-official, ref V10780-E5+V10782-P2.3) · MT=MT_ADAPTIVE_EXPLOIT_V1 · MB=MB_ADAPTIVE_EXPLOIT_V1, locked_date 2026-07-05, INSERT OR IGNORE re-run changes=0 (immutable ✔) | DB + seed audit re-run |
| Commit khớp code VPS | **ĐÚNG 13/13** — sha256 12/13 identical; user-view.html khác sha do CRLF/LF (fc so nội dung: 0 khác biệt) | sha256sum + fc |

**A3 — đính chính trung thực (1 mục):** Báo cáo V10784 viết "P2.1 UI /choi in method lock ĐÃ DEPLOY ✅". Thực tế đúng là file choi.html có lockLine đã live (hash khớp) NHƯNG dữ liệu decision-ref chỉ có từ lock tuần 06/07 — hôm nay board vẫn hiển thị lock tuần 29/06 (không có owner_decision_ref → fallback "auto theo ổn định"). Lock line ĐẦY ĐỦ (method + khóa từ + quyết định V10782-P2.3) chỉ xuất hiện từ 00:00 06/07. Không phải báo cáo sai về code, nhưng diễn đạt "hoàn tất hiển thị" là SỚM 1 ngày. Gate D sáng mai sẽ chụp evidence sau 00:00.

## B1 — PHỦ SÓNG 7 NGÀY (29/06→05/07, model × miền × ngày)

21 ô/model (7 ngày × 3 miền). Kết quả phân loại:

- **Đủ 21/21**: claude-opus-4-6, claude-sonnet-4-6, combo-no-token, combo-super, deepseek-reasoner, gemini-2.5-flash/pro, gpt-5-mini, gpt-5.4, gpt-5.5, gpt-oss-120b, grok-4.20-multi-agent, lstm, meta-learning, qwen3-max-thinking, random-forest, smart-ensemble, smart-ml, xgboost (19 model).
- **Đúng thiết kế (không phải lỗ)**: 6 model RETIRED V10779 dừng từ 05/07 (deepseek-v4-flash/pro, gemini-3-flash/3.1-pro, qwen3-coder, qwen3.6-plus); 3 lane MỚI chỉ có từ 05/07 (deepseek-v4-pro-real, glm-5.2, qwen3.7-max — first-run V10779/V10781).
- **LỖ THẬT (root cause)**:
  - `kimi-k2.5` **7 ô miss/7 ngày** (29/06 MT+MB · 30/06 MT+MB · 01/07 MT · 02/07 MN · 04/07 MB): hard-timeout >300s (p95 ~470s), scheduler vứt kết quả về muộn → **B2 fix: timeout riêng 620s + late-fill** (bằng chứng sandbox: kimi về 432s → OK với budget mới).
  - `qwen3.7-max` 05/07 MB: TIMEOUT >300s, kết quả về 17:49:09 (349s — trace có, row không) → **B2 fix: timeout 480s + late-fill**.
  - `glm-5.1` 29/06 MN + `gemma-4-31b` 03/07 MN: miss đơn lẻ trước khi có diagnostic-row contract (đã có từ V10784; gemma 05/07 MB lỗi 429 quota vẫn có diagnostic row ✔).
- **Eval coverage**: 29/06→04/07 mỗi ngày 81–83 rows/28 model/3 miền; 05/07 = 74 rows lúc 20:20 (thấp hơn do 6 model retired; lần đầu sau hotfix whitelist).
- **Bundle 05/07**: MN 15 voters / MT 13 / MB 14 — đúng expected (khác biệt do model skip/verdict).

## B2 — FIX THEO NGUYÊN NHÂN (deploy 20:33, sandbox-first PASS 11/11)

1. **Late-fill hợp nhất freeze** (`_v10785_late_fill.py`): kết quả về SAU hard-timeout không vứt nữa — future poll lại (watchdog 15'), ghi lane đo `run_source=shadow_auto_eval` + **late=1** + note late_fill; KHÔNG vào bundle (shadow không bao giờ vào bundle); dup-guard; quá 2h thì bỏ.
2. **Cutoff riêng theo p95**: kimi-k2.5 620s · qwen3.7-max 480s · default 300s (env-overridable).
3. **Watchdog heartbeat cron 15'** + **startup-recovery +120s sau restart** (bài học 16:38): shadow-after-chain miss >75' → tự re-run (idempotent DUP_GUARD); MDE 20:20 miss sau 20:40 → kick job; T-10/verify → ALERT-ONLY (không tự can thiệp gần mốc freeze). Test sandbox: phát hiện đúng shadow MB miss giả lập + MDE miss giả lập + T-10 MN true-positive hôm nay; live: startup-recovery fire 20:34:47, watchdog OK 20:45.
4. **grok count-only**: ghi vào registry `reasoning_text_expected=False` — provider chỉ trả reasoning token count (rt=78k, không kèm text) — bản chất provider, KHÔNG tính model lỗi.

## B3 — SANDBOX 25 LANE CHO 06/07 (chạy 20:44–20:57, DB sandbox riêng)

- **24/25 lane OK vòng đầu**: 17/18 AI lane (list đầy đủ trong artifact `b3_results.json`) + 7/7 ML lane × 3 miền. **Production predictions: 0 rows sandbox** (guard query xác nhận).
- **gemini-3.5-flash lần gọi ĐẦU TIÊN: OK 31s, rt=4,312** — lane mới validated trước live.
- **kimi-k2.5: OK 432s** (budget mới 620s — với 300s cũ đã chết lần nữa).
- Reasoning capture: 14/18 lane rt>0; rt=None đúng bản chất provider: claude ×2 (Anthropic không trả reasoning tokens qua route hiện tại), gpt-5.4/gpt-5-mini (non-thinking).
- **1 lane FAIL vòng đầu: qwen3-max-thinking TIMEOUT>330s** — đang retry 600s nền; kết hợp evidence live hôm nay (MN OK 190.9s sáng, MB "trả về rỗng" 11.9s tối) → root cause: provider chập chờn theo giờ tải, KHÔNG phải code; late-fill sẽ vớt các lần chậm. Kết quả retry vào partial #2.
- **D2 sớm**: prompt 3 miền 06/07 build thử — station set THỨ HAI đúng (chi tiết gate D).

## VIỆC CÒN LẠI (partial #2 ~23:00)

C3 commit governance + C4 Notion V10784 + BAO_CAO_TONG_V10784 chốt (MDE 74 rows đã có) · D gate script + chạy đêm + cron 07:30 · E1 hash 4 bảng · E2 báo cáo tổng V10785 + BẢNG CHỜ KÝ (B4: loại 3 rows qwen3.7-max/glm-5.2 chạy sớm 05/07) · E3 AS-BUILT + HOME.

Không có mục BLOCKED. Chưa đụng mục nào cần chữ ký (gom vào bảng cuối).
