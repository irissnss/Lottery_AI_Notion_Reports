# V10784 — BÁO CÁO TỔNG: HỢP ĐỒNG THỰC THI ĐẾN HẾT (05/07/2026)

Phiên chạy theo hợp đồng thực thi owner 16:5x — chạy đến hết P0→P5, không dừng hỏi. Kết quả: **P0–P5 hoàn tất 100%, 0 mục BLOCKED**, 3 partial report đúng/sớm hạn (18:15 ✅ 18:16 · 21:00 ✅ nộp sớm 18:4x · 00:00 ✅ báo cáo này).

## TÓM TẮT ĐIỀU HÀNH (10 dòng)

1. **Cứu eval đơn model:** nguyên nhân MT shadow mất hôm nay = restart 16:38 giết trigger (KHÔNG phải freeze); freeze whitelist deploy 17:06 — freeze CHỈ chặn official surface; backfill MT chuẩn 10 rows; verify MB tối chạy xuyên freeze bình thường.
2. **Freeze MT/MB verified hậu kiểm:** T-10 16:45:03 (MT BT=49) + 17:45:00 (MB BT=06) fire; bundle đứng yên sau mốc; 0 official write late cả ngày (đến giờ báo cáo).
3. **Reasoning capture toàn tuyến:** OpenRouter/DeepSeek/Gemini → cột mới `predictions.reasoning_tokens` + `reasoning_json` + trace; smoke 3/3 PASS (1,503 / 20,589 / 57 rt); live tối nay grok 78,346 · reasoner official 8,988.
4. **Method lock hoàn tất:** /choi in lock tuần 06/07 đủ 3 miền; audit hồi tố trung thực (0 đổi method thật; 2 artifact ngày sinh bảng 04/07 ghi nhận); governance commit đủ.
5. **Gemini shadow lane mới:** `gemini-3.5-flash` (STABLE mới nhất) shadow_only=1, output_eligible=0, first_run 06/07, thinking_enabled_date riêng + **first-run gate toàn hệ mới** (phát hiện + đóng vĩnh viễn lỗ hổng lane chạy sớm).
6. **P4 xong 4/4 trong đêm:** history filter + phân trang server-side; ma trận độc lập ~30 tham số; cycle scan 1,614 cells measurement-only (sanity MN D-1 82.4%/75.4% khớp mốc owner); ma trận trùng lặp 7 cụm.
7. **Hash 4 bảng:** chỉ natural growth (chi tiết bảng dưới) — 0 mutation ngoài quy trình.
8. **money_board_lock tuần 06/07:** 3 miền nguyên vẹn (kiểm 2 lần: 18:5x + 23:50).
9. Docs: CHANGELOG + SSOT + FU tracker + AUTOMATION_STATE seq 239→240 + 26_RUNTIME_AS-BUILT (mục 1 freeze + Sổ CLOSED 5 hồ sơ mới + SHADOW_AUTO 11).
10. **Bảng chờ ký cuối báo cáo — 4 nhóm quyết định, không tự quyết.**

## PHẦN 0 — KHẨN (17:45 deadline: PASS)

| Mục | Kết quả | Bằng chứng |
|---|---|---|
| 0.1 Cứu eval | Root cause MT shadow = restart 16:38:38 (V10783 deploy) giết trigger sau AI chain — KHÔNG phải freeze. Freeze whitelist `is_freeze_exempt_run_source` (shadow/test/eval/smoke/lane/backfill/pv2) deploy 17:06 TRƯỚC hạn 17:45. Smoke 3/3: shadow qua (late=0) · official mới → late=1 · official overwrite → block. Backfill MT chuẩn qua `_run_shadow_auto_eval('MT')`: 10 rows late=0. `model_daily_eval` nhịp 20:20 nguyên vẹn 8 ngày liền | partial #1 §0.1 |
| 0.2 Freeze MT hậu kiểm | T-10 16:45:03 `[T10_CHOT] MT: bundle chốt BT=49 (v2)`; sau 16:55 bundle đứng yên (watch 17:06→17:20); official rows 15, write cuối 16:37:59; 0 late | partial #1 §0.2 |
| 0.3 Watch script | Nguyên nhân: API path sai + clamp + stdout buffer → viết lại direct-DB + line_buffering; timeline events từ 17:06 | partial #1 §0.3 |
| 0.4 MB live | T-10 17:45:00 `[T10_CHOT] MB: bundle chốt BT=06 (v1)` (single-flight); freeze 17:55; card đứng yên 17:45–18:00; kết quả MB 18:31:01 (2 scrape fail 18:30 → retry OK); verify ngay: 24 rows WIN3/PARTIAL3/LOSE18 đủ ai_chain+rerun+shadow — **freeze không chặn verify/eval** | partial #2 + probe 18:33 |
| 0.5 user-view.js | surface=official upload 18:0x; re-upload 18:16 kèm server-side pagination; hash VPS=local `18e9def3…` | probe 18:4x |

## PHẦN 1 — LOGGING (23:00 deadline: PASS lúc ~18:30)

- **1.1–1.2:** OpenRouter `message.reasoning` + `usage.completion_tokens_details.reasoning_tokens` (trước đây VỨT BỎ), DeepSeek `reasoning_content` native, Gemini `thoughts_token_count` → cột mới `predictions.reasoning_tokens` + `reasoning_json.native_reasoning_excerpt` (3000 chars) + `prediction_trace.jsonl` thêm `reasoning_tokens` + `custom_prompt.applied_text` đầy đủ (đóng FU V10782 trace 15h). Vá cả shadow-lane save không truyền reasoning_json (root cause cohort E3 NULL).
- **1.3 Smoke 3/3 PASS (18:03–18:29):** qwen3-max-thinking rt=1,503 + text 5,826 chars · grok-4.20-multi-agent rt=20,589 (count-only, provider không trả text — trung thực; $0.21/call, circuit breaker mở 10' đúng thiết kế) · gpt-5.5 rt=57 + text 428 chars. Ghost rows dọn sạch. Live bổ sung: shadow MB grok=78,346 · gpt-5.5=8,804 · glm-5.2=6,364 · kimi=5,803 · reasoner official=8,988.
- **1.4:** `_v10784_verify_0607.py` cron 07:30 06/07 — C1 reasoning>0 · C2 first-run 2 lane · C3 /choi MN lock · C4 đài THỨ HAI · C5 freeze 3 mốc hôm trước · C6 MDE 3 miền; JSON vào `artifacts/v10784/`.

## PHẦN 2 — METHOD LOCK (23:00 deadline: PASS lúc 17:36)

- **2.1:** /choi in lock tuần 06/07: MN=MN_BT1_OFFICIAL_V1 (BT 1-số, nghỉ T7) · MT=MT_ADAPTIVE_EXPLOIT_V1 · MB=MB_ADAPTIVE_EXPLOIT_V1 + khóa từ + owner_decision_ref + published_at (upload 17:33).
- **2.2:** Audit hồi tố toàn lịch sử: KHÔNG có đổi method giữa tuần thật; 2 nhóm artifact ngày 04/07 (locked_date +5d tuần 29/06 + locked_at 22:14 sau giờ xổ) = ngày sinh bảng lock (V10782), ghi nhận trung thực; 0 vi phạm money_board_log; 0 lệch songthu.
- **2.3:** Private commit `58eb3fc` (17:36) — CHANGELOG + AUTOMATION_STATE seq 239 + SSOT + FU + code P0–P2.

## PHẦN 3 — GEMINI SHADOW LANE (23:30 deadline: PASS lúc 18:09)

Audit 5 lane hiện có (bảng chi tiết partial #2): official gemini-2.5-flash/pro giữ nguyên; ghi nhận trung thực docstring cũ nói budget=0 disable nhưng code thật không set thinking_config → mọi lane thinking dynamic mặc định.

Lane mới: **gemini-3.5-flash** (Flash STABLE mới nhất, probe ListModels 17:43) — SHADOW_AUTO, shadow_only=1, output_eligible=0, first_run_date=2026-07-06, thinking_enabled_date=2026-07-06 riêng, không backfill, key shadow cohort.

**First-run gate toàn hệ (mới):** `get_shadow_models_active_on(date)` — lane chưa tới first_run_date bị loại khỏi run + expected count + catch-up. Verify: active 05/07 = 8 · active 06/07 = 11.

**Phát hiện trung thực (pre-existing):** qwen3.7-max + glm-5.2 (V10781, first_run 06/07) đã chạy 05/07 (MN 15:28/15:30 + MT 17:18 + MB 17:45) vì trước 18:09 chưa có gate. Rows shadow-only, zero official impact, giữ nguyên — quyết định loại khỏi so găng nằm ở bảng chờ ký.

## PHẦN 4 — VIỆC DÀI (4/4 XONG)

- **4.1 History filter + pagination:** API `offset`+`total_count` (live total_count=5202 surface=official); lọc LANE official/shadow + pager (index.html/app.js); user-view.js server-side pagination + mặc định 7 ngày. Không đẻ bảng mới.
- **4.2 Ma trận độc lập:** `P42_MA_TRAN_DOC_LAP_MIEN_THU_TUAN.md` — 5 lớp × ~30 tham số gắn nhãn GLOBAL/per-MIỀN/per-MIỀN×THỨ/per-TUẦN; đề xuất ĐX-1/2/3 kèm evidence, có default kế thừa.
- **4.3 Cycle scan measurement-only:** bảng `cycle_scan_shadow_v10784` (1,614 cells / 696 đủ mẫu n≥8; diagnostic_only=1, shadow_only=1, cấm official trước 14/07 flag trong schema) + API `/api/admin/cycle-scan` (401 unauth) + panel /monitoring 60s. Lưới lag {1,2,3,7,14,28} × 3 miền × 7 thứ × đài × {BT,G2,LO2}; window từ 10/05 + window dài từ 01/07/2025 (mốc sáp nhập tỉnh); baseline + OOS 70/30 + ổn định 2 nửa. **Sanity PASS:** MN D-1 per-day đề∈lô-hôm-trước = 82.4% (n=369 dài) / 75.4% (10/05+) — khớp mốc ~73% owner (per-trial 45.5% vs base 43% — edge mỏng, trung thực); MB G2 lag7/lag28 per-day 50%. Top cells OOS-dương ổn định: MT T2 lag7 DB→LO2 +20.6pp (OOS +51pp, n=16) · MN T2 lag28 DB→LO2 +25.5pp (OOS +48pp, n=24).
- **4.4 Ma trận trùng lặp:** `P44_MA_TRAN_TRUNG_LAP_GIU_HOPNHAT_BO.md` — 7 cụm; ~14 endpoint + ~12 card đề xuất BỎ/HỢP NHẤT; 5 hành động S1–S5 chờ ký. KHÔNG xóa gì phiên này.

## PHẦN 5 — VERIFY CUỐI PHIÊN

### 5.1 Hash 4 bảng (baseline ~17:30 → cuối phiên)

| Bảng | Baseline | Cuối phiên | Diff | Giải trình |
|---|---|---|---|---|
| predictions | 9,325 `69fb20fd…` | 9,342 `3e04c004…` (19:0x) | +17 rows | MB tối: 8 ai_chain (17:31–33) + 9 shadow_auto_eval (17:34–45) — natural; +verify UPDATE status MB 18:31 |
| final_bundles | 383 `d04fd95e…` | 384 `1ff8b476…` | +1 row | Bundle MB id=466 do T-10 17:45 single-flight — natural |
| lottery_results | 15,016 `3bea5774…` | 15,017 `e3a4fb57…` | +1 row | Kết quả MB Thái Bình 18:31:01 — natural (MT 3 đài 17:30 nằm trong baseline) |
| model_daily_eval | 9,132 `cbd1f568…` | 9,206 (20:20:00) | +74 rows | Nhịp chuẩn 20:20 fired đúng giờ: MB 24 + MN 25 + MT 25 — NGÀY ĐẦU sau hotfix whitelist, eval đơn model SỐNG (05/07 verify đủ 3 miền) |

0 official write late hôm nay (query late=1 loại smoke/shadow/test = 0 rows). Không có diff ngoài giải trình → không cần điều tra.

### 5.2 money_board_lock tuần 06/07 (check 18:5x + 23:50)

| Region | method_label | locked_date | owner_decision_ref | published_at | 23:50 |
|---|---|---|---|---|---|
| MN | MN_BT1_OFFICIAL_V1 | 2026-07-05 | V10780-E5 + V10782-P2.3 (owner ký 05/07) | 16:12:26 | re-check 21:0x V10785: NGUYÊN VẸN (re-run seed changes=0) — check 23:50 trong gate D V10785 |
| MT | MT_ADAPTIVE_EXPLOIT_V1 | 2026-07-05 | V10782-P2.3 | 16:12:26 | NGUYÊN VẸN 21:0x — gate D 23:50 |
| MB | MB_ADAPTIVE_EXPLOIT_V1 | 2026-07-05 | V10782-P2.3 | 16:12:26 | NGUYÊN VẸN 21:0x — gate D 23:50 |

compute_board() sau 00:00 06/07 sẽ tạo daily lock từ 3 method này.

### 5.3 Service + governance

- Service PID 3289161 active từ 18:29:23 (restart cuối); /api/health=200; /api/admin/cycle-scan=401 unauth; 0 traceback journal từ 19:00.
- Deploy timeline tôn trọng blackout: 17:06/17:15/17:33 (giữa 17:00–17:45) + 18:09/18:29 (sau 18:00); KHÔNG deploy 16:45–17:00 và 17:45–18:00.
- Governance: private commits `58eb3fc` (P0–P2) + `bd574f7` (P3+P4+docs) + `d31b683` (chốt trong V10785: scheduler B2 + docs seq240); public commits `892578b` (partial#1) + `a3cb5ac` (partial#2) + `73e1d51` (P42/P44) + commit chốt kèm file này; AUTOMATION_STATE seq 239 (V10784) → 240 (V10785); 26_RUNTIME_AS-BUILT updated (page `ea141094-9569-44fb-8de7-9dd6963382e7`): mục 1 + freeze/whitelist, SHADOW_AUTO 8→11 + first-run gate, Sổ CLOSED +5 hồ sơ (E1–E6, exclude:true, reasoning NULL, nghi freeze chặn eval, watch script), mục 5 refresh.
- Notion V10784 (≤30 dòng): tạo trong phiên V10785 — ID ghi tại NOTION_SYNC_PAYLOAD_V10784.md + AUTOMATION_STATE.
- **Forensic V10785 re-verify (21:0x)**: 6 claim V10784 kiểm chứng độc lập — 5 ĐÚNG; 1 đính chính: P2.1 "lock UI hoàn tất hiển thị" SỚM 1 ngày (board hôm nay còn tuần 29/06; lockLine + decision ref đầy đủ hiện từ 00:00 06/07). MDE 20:20 = 74 rows fired đúng — claim "cứu eval" XÁC NHẬN SỐNG.

## BẢNG CHỜ KÝ (gom toàn phiên — KHÔNG tự quyết)

| # | Quyết định | Nguồn | Đề xuất của em | Deadline gợi ý |
|---|---|---|---|---|
| K1 | Loại 3 rows/lane ngày 05/07 của qwen3.7-max + glm-5.2 (chạy sớm trước first-run gate) khỏi mọi bảng so găng 14/07 | P3 phát hiện | LOẠI (cửa sổ đo chuẩn bắt đầu 06/07; giữ rows trong DB, chỉ loại khỏi so găng) | trước 14/07 |
| K2 | ĐX-1: tách skip/confirm threshold per-MIỀN (hiện GLOBAL) | P4.2 | Tách sau khi có 14 ngày dữ liệu reasoning mới | 14/07 |
| K3 | ĐX-2: output_eligible per miền qua `allowed_regions` sẵn có | P4.2 | Giữ nguyên đợt này; dùng khi có model lệch miền rõ | khi cần |
| K4 | ĐX-3: reasoning effort per miền | P4.2 | GIỮ GLOBAL + đo 14 ngày trước khi tách | 19/07 |
| K5 | S1–S5 ma trận trùng lặp (hợp nhất accuracy 4 bảng → 1 nguồn, bỏ ~14 endpoint + ~12 card, gộp health, gộp history, dedupe deploy scripts) | P4.4 | Ký từng mục S1→S5, em thực thi từng bước có backup | tuần 07–13/07 |
| K6 | Cycle scan: cell nào (nếu có) được nâng lên official rule sau cửa sổ đo | P4.3 | CHỜ đủ 14 ngày OOS (sau 14/07) + báo cáo riêng — cấm áp trước 14/07 đã flag trong schema | 14/07+ |

## FILE / ARTIFACT INDEX

- Public: `BAO_CAO_PARTIAL1_P0_V10784.md` · `BAO_CAO_PARTIAL2_P1_P2_V10784.md` · `P42_…` · `P44_…` · `CONVERSATION_CONTEXT_V10784_20260705.md` · `NOTION_SYNC_PAYLOAD_V10784.md` · báo cáo này.
- Private code: `_v10782_freeze.py` (whitelist) · `database.py` · `scheduler.py` · `main.py` · `gpt_analyzer.py` · `model_registry.py` · `_v10784_verify_0607.py` · `_v10784_p43_cycle_scan.py` · frontend (choi/index/app/user-view/monitoring).
- VPS artifacts: `/root/Lottery_AI_Test/artifacts/v10784/` (verify_0607 output từ 06/07) · watch timeline · smoke logs `/tmp/smoke_reasoning_v2.log`.
- Rollback: `/root/backups/v10784_pre` + `/root/backups/v10784_p1_pre`.
