# V10785 — BÁO CÁO TỔNG — FORENSIC + COVERAGE + SANDBOX 25 LANE + GATE GO/NO-GO 06/07

Phiên 05/07/2026 19:06 → 06/07 00:2x. Hợp đồng: KHÔNG tin báo cáo cũ — re-verify bằng bằng chứng độc lập; vá tận gốc lỗ phủ sóng model; sandbox 25 lane cho 06/07; đóng hết mảnh treo; gate GO/NO-GO 2 giai đoạn.

## 1. KẾT LUẬN NHANH

- **GATE STAGE-1 (đêm 05/07): 9/9 PASS → GO.** Check 23:50 PASS toàn bộ; lock tuần 06/07 active từ 00:00 (bằng chứng 00:03). Stage-2 = cron 07:30 sáng 06/07 (`_v10784_verify_0607.py`, armed).
- Vá thêm sau 00:00: VPS chạy bản money-board cũ thiếu field `owner_decision_ref` → sandbox test → deploy 00:10 → /choi lockLine hiển thị đủ quyết định ký (LIVE_REFS_OK 3 miền).
- Forensic: **5/6 claim 3 phiên trước ĐÚNG**; 1 đính chính trung thực (P2.1 V10784 "lock UI hoàn tất hiển thị" sớm 1 ngày). Phát hiện mới: **T-10 MN 15:45 hôm nay không fire** (code deploy 16:03 SAU mốc — tự lành 06/07; watchdog canh).
- Coverage: lỗ thật lớn nhất là **kimi-k2.5 7 ô/7 ngày do hard-timeout 300s < p95 ~470s** → fix **per-model cutoff (620s/480s) + late-fill lane đo (late=1, không vào bundle)** — deploy 20:33 sau sandbox 11/11 PASS.
- Sandbox 25 lane cho 06/07: **24/25 OK vòng đầu** (production 0 rows đụng); lane cuối **qwen3-max-thinking root cause chính xác** (provider trả JSON trong `message.reasoning`, `content` rỗng → code cũ vứt) → **salvage fix deploy 21:24**.
- **Watchdog heartbeat 15' + startup-recovery +120s** sống từ 20:33 — bịt vĩnh viễn lớp lỗi "restart giết trigger" (bài học 16:38 hôm nay).
- 4 bảng official: **0 write official sau freeze, 0 late row, tăng trưởng 100% natural khai báo được** (bảng hash mục 6).

## 2. PHẦN A — FORENSIC (chi tiết trong BAO_CAO_PARTIAL1)

- A1 timeline 04:00→22:00: 10 restart đều gắn deploy trong prompt các phiên (V10782/83/84/85); double-restart 16:38 (37s) giết trigger shadow MT = bài học đẻ ra startup-recovery; MDE 20:20 = 74 rows/3 miền — hotfix whitelist V10784 sống ngày đầu.
- A2 re-verify 6 claim — bảng đầy đủ partial #1. Điểm nhấn: freeze whitelist test 2 chiều **5/5 PASS trên sandbox copy 483MB** (official new→late=1; overwrite verified/PENDING→CHẶN; shadow/eval→pass late=0; prod hash IDENTICAL trước/sau); repo=VPS **13/13 file** (user-view.html chỉ khác CRLF/LF).
- A3 hồ sơ đính chính: 1 mục (P2.1) — đã ghi vào BAO_CAO_TONG_V10784 + Notion V10784 + SSOT. Không có claim nào SAI về code/behavior; sai là **diễn đạt thời điểm hiển thị**.

## 3. PHẦN B — COVERAGE + FIX + SANDBOX

### B1 — Bảng phủ sóng 7 ngày (29/06→05/07)
19 model đủ 21/21 ô; 6 model RETIRED dừng đúng thiết kế từ 05/07; 3 lane mới first-run đúng gate. Lỗ thật + root cause: kimi-k2.5 7 ô (timeout) · qwen3.7-max MB 05/07 (kết quả về 349s bị vứt — trace có, row không) · glm-5.1 29/06 MN + gemma-4-31b 03/07 MN (miss đơn lẻ trước diagnostic-contract V10784).

### B2 — Fix theo nguyên nhân (deploy 20:33, sandbox 11/11 PASS trước)
1. `_v10785_late_fill.py`: late-fill hợp nhất freeze — kết quả về sau hard-timeout ghi lane đo `run_source=shadow_auto_eval, late=1, note=late_fill_v10785`; KHÔNG vào bundle; dup-guard (date,region,model); expire 2h.
2. Cutoff p95 per-model: kimi-k2.5 **620s** · qwen3.7-max **480s** · default 300s (env-override được).
3. Watchdog cron 15' + startup-recovery +120s: shadow-after-chain miss >75' → tự re-run idempotent; MDE miss sau 20:40 → kick; T-10/verify → **ALERT-ONLY** (không tự can thiệp gần mốc freeze). Live: startup-recovery fired sạch 20:34:47 + 21:26:13; ticks 15' đều, 0 MISS giả.
4. grok-4.20: `reasoning_text_expected=False` (provider count-only — không phải lỗi model).
5. (Phát sinh từ B3) `gpt_analyzer._call_openrouter` salvage EMPTY_RESPONSE (deploy 21:24).

### B3 — Sandbox 25 lane cho 06/07 (prompt THỨ HAI)
- Hạ tầng cách ly đúng chuẩn: DB `/root/sandbox_v10785/sandbox_b3.db` (copy fresh) + **trace sandbox riêng** (patch `log_prediction_trace` — KHÔNG ghi vào prediction_trace.jsonl production).
- **17/18 AI lane OK** (mỗi lane 1 call MN 06/07, per-model timeout): đáng chú ý **gemini-3.5-flash first call OK 31s rt=4,312** (lane mới validated trước live) · **kimi-k2.5 OK 432s** (chứng minh trực tiếp giá trị budget 620s — với 300s cũ đã chết) · grok rt=75,753 · 14/18 lane rt>0 (4 lane rt=None đúng bản chất: claude ×2, gpt-5.4, gpt-5-mini non-thinking).
- **7/7 ML lane × 3 miền OK** (21 rows sandbox).
- **Guard: production predictions 0 rows sandbox** (query xác nhận 2 lần).
- qwen3-max-thinking: vòng đầu TIMEOUT>330s; retry 6s trả **content rỗng + 20,199 tokens toàn thinking** → root cause + salvage fix live 21:24; live-verify = run shadow 06/07 (log `salvage parse`).
- D2 bonus: prompt 3 miền 06/07 build offline — Deep Focus đúng đài THỨ HAI: MN=[Cà Mau, TP. HCM, Đồng Tháp] · MT=[Phú Yên, Thừa Thiên Huế] · MB=[Hà Nội].

## 4. PHẦN C — ĐÓNG MẢNH TREO (6/6 DONE, chi tiết partial #2)

C1 user-view official (live=repo + API surface) · C2 /choi lock (payload 3 miền PASS; decision ref hiện từ 00:00 06/07) · C3 private `d31b683` 70 files + docs seq240 · C4 Notion V10784 `3941d385-9bf8-81b6-8cd3-e9d6c42504c9` + BAO_CAO_TONG_V10784 chốt + public `8b76646` · C5 pagination live · C6 seed audit re-run (script LOCAL-runner — hồ sơ làm rõ).

## 5. PHẦN D — GATE GO/NO-GO

**Stage-1 đêm 05/07: 9/9 PASS → GO** (bảng partial #2: D1 lock · D2 đài T2 · D3 reasoning · D4 first-run · D5 T-10 armed · D6 MDE · D7 watchdog · health/auth · cron 07:30).
**Check 23:50: PASS toàn bộ** — bundles 05/07 bất biến (MN BT=71 v3 · MT BT=49 v2 · MB BT=70 v2) · 0 official write sau freeze · 0 late row · lock week 06/07 nguyên 3 miền · watchdog 14 tick sạch từ 22:00 · 0 ERROR journal · health 200 · cron 07:30 armed · salvage fix hiện diện file live.
**Sau 00:00 06/07 (bằng chứng lock active):** `compute_board()` 00:03 trả `MN=MN_BT1_OFFICIAL_V1 · MT=MT_ADAPTIVE_EXPLOIT_V1 · MB=MB_ADAPTIVE_EXPLOIT_V1, locked=True, lock_since=2026-07-05` — tuần 06/07 chính thức active. Phát hiện + vá luôn 1 gap hiển thị: VPS chạy bản `_v10759_money_board.py` CŨ (13:59, thiếu V10782-P2.3 fields) nên payload thiếu `owner_decision_ref/published_at` dù DB có sẵn → sandbox test bản repo trên `sandbox_board.db` (refs OK 3 miền) → deploy 00:10 + restart + verify live: **LIVE_REFS_OK 3 miền** (`V10782-P2.3 (owner ký 05/07/2026)`, published 16:12:26). /choi lockLine giờ hiển thị đủ quyết định + thời điểm ký. Hash 4 bảng TRƯỚC=SAU restart IDENTICAL (da147af0/d5293ac7/0708cd89/9fd897e9) — restart 00:10 nằm NGOÀI cửa sổ live, không đụng dữ liệu.
Stage-2: cron 07:30 06/07 tự chạy (C1 reasoning>0 · C2 first-run 3 lane mới · C3 /choi MN lock · C4 đài THỨ HAI · C5 freeze fire 05/07 · C6 MDE 3 miền) — kết quả ghi `/root/Lottery_AI_Test/artifacts/v10784/verify_0607.log`.
Ghi chú watchdog: journal 23:35 in 10 dòng ALERT T-10 MN là **echo trùng của stdout logger** (scheduler_logs DB chỉ ghi đúng 1 row/tick, xác nhận bằng `GROUP BY minute` = 1); T-10 MT/MB 05/07 có `[T10_CHOT]` thật lúc 09:45/10:45 (log DB) — alert chỉ đúng cho MN như forensic A-phase đã kết luận.

## 6. PHẦN E — HASH 4 BẢNG (baseline V10784 17:26 → chốt phiên 23:52 → post-restart 00:13)

| Bảng | Baseline 17:26 | Chốt phiên 23:52 | Post-restart 00:13 | Diff giải trình |
|---|---|---|---|---|
| predictions | 9,325 `69fb20fd…` | 9,342 `da147af0…` | `da147af0…` IDENTICAL | +17: shadow MB tối + rerun_post_mt + ai_chain đêm — natural, 0 late, 0 official sau freeze |
| final_bundles | 383 `d04fd95e…` | 384 `d5293ac7…` | `d5293ac7…` IDENTICAL | +1: MB bundle 17:33 (v1) → T-10 17:45 (v2) — natural |
| lottery_results | 15,016 `3bea5774…` | 15,017 `0708cd89…` | `0708cd89…` IDENTICAL | +1: MB Thái Bình 18:31 — natural |
| model_daily_eval | 9,132 `cbd1f568…` | 9,206 `9fd897e9…` | `9fd897e9…` IDENTICAL | +74: nhịp 20:20 (24+25+25) — natural, NGÀY ĐẦU hậu whitelist |

Attribution rows mới 21:26→23:52 (`created_at > 21:26`): ai_chain 16 · auto_daily 22 · rerun_post_mt 7 · shadow_auto_eval 29 — toàn bộ lane đo/chuẩn bị 06/07, 0 rows official ngày 05/07 sau freeze (query riêng = 0).

/du-doan LOCKED nguyên phiên: bundles hôm nay MN BT=71 v3 · MT BT=49 v2 · MB BT=70 v2 — không đổi sau freeze.

## 7. BẢNG CHỜ KÝ (gom đủ — KHÔNG tự quyết)

| # | Quyết định | Nguồn | Đề xuất | Deadline |
|---|---|---|---|---|
| K1 (B4) | **Loại 3 rows/lane 05/07 của qwen3.7-max + glm-5.2** (chạy sớm trước first-run gate 18:09) khỏi mọi so găng từ 06/07 | V10784-P3 + V10785-B4 | **LOẠI** — cửa sổ đo chuẩn tính từ 06/07; rows GIỮ trong DB (đánh dấu khi so găng), không xoá | trước 14/07 |
| K2 | ĐX-1 tách skip/confirm threshold per-MIỀN | P4.2 | tách sau 14 ngày reasoning data | 14/07 |
| K3 | ĐX-2 output_eligible per miền (`allowed_regions`) | P4.2 | giữ nguyên đợt này | khi cần |
| K4 | ĐX-3 reasoning effort per miền | P4.2 | giữ GLOBAL + đo 14 ngày | 19/07 |
| K5 | S1–S5 dọn trùng lặp (accuracy 4 bảng→1, bỏ ~14 endpoint + ~12 card, gộp health/history, dedupe deploy scripts) | P4.4 | ký từng mục, em làm từng bước có backup | 07–13/07 |
| K6 | Cycle scan: cell nào lên official rule | P4.3 | chờ đủ 14 ngày OOS + báo cáo riêng | 14/07+ |
| K7 | **Per-model timeout + late-fill giữ vĩnh viễn hay chỉnh ngưỡng** sau 7 ngày đo (kimi 620s / qwen37 480s) | V10785-B2 | giữ + review số liệu late-fill 12/07 | 12/07 |

## 8. GOVERNANCE + ARTIFACT INDEX

- Private commits: `d31b683` + commit chốt cuối phiên (board ref fix + scripts + docs). Public: `785e544` (partial#1) · `8b76646` (V10784 final) · `e33af02` (partial#2) · commit final (báo cáo này).
- Docs: CHANGELOG V10785 · SSOT V10785 · FU-V10785-FORENSIC-GATE · AUTOMATION_STATE seq241 (+ Notion pages ghi ID).
- Notion: V10784 page `3941d385-9bf8-81b6-8cd3-e9d6c42504c9` · V10785 page `3941d385-9bf8-817e-8d93-d53d17472e4d` · AS-BUILT `ea141094…` +7 blocks · HOME snapshot `495fa208…` refresh 21:22.
- VPS: `/root/sandbox_v10785/` (sandbox_freeze.db, sandbox_b3.db, sandbox_board.db, b3_results.json, b3_d2_prompts.json, b3_run.log, b3_retry.log, b3_salvage.log) · rollback `scheduler.py.bak_v10785` + `model_registry.py.bak_v10785` + `gpt_analyzer.py.bak_v10785` + `_v10759_money_board.py.bak_v10785_p2ref`.
- Restart ledger: 20:31 · 20:33 · 21:24 · 00:10 (đều ngoài cửa sổ live; health 200 + startup-recovery WATCHDOG_OK mỗi lần; hash 4 bảng bất biến qua restart).

## 9. BLOCKERS

Không có blocker kỹ thuật. Chờ chữ ký: K1–K7. Live-verify pending (tự động): late-fill/salvage/watchdog lần đầu chạy thật ngày 06/07 + cron 07:30 stage-2.
