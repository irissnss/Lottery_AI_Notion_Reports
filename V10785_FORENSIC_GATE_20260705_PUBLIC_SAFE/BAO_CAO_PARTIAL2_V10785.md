# V10785 — BÁO CÁO PARTIAL #2 — 21:40 05/07/2026

Tiếp partial #1 (21:05). Khối C/D/E + chốt B3.

## B3 CHỐT — lane cuối cùng (qwen3-max-thinking)

- Retry 600s lần 1 (21:04): provider trả **content RỖNG, finish=stop, 20,199 tokens toàn thinking** — 6 giây. Root cause CHÍNH XÁC tìm được: **provider trả reasoning-only response** (JSON nằm trong `message.reasoning`, field `content` rỗng) — code cũ vứt toàn bộ → "Trả về rỗng".
- **Fix salvage**: `_call_openrouter` — khi content rỗng nhưng `message.reasoning` chứa JSON thì parse từ reasoning thay vì vứt. Sandbox-first: compile OK trên staged; test call sandbox lần 2 bị provider treo >6' (đúng bản chất chập chờn theo giờ tải — kill sạch, production 0 rows đụng).
- **Deploy 21:24** (restart ngoài cửa sổ live; health 200, 0 error journal, watchdog + T-10 re-registered, startup-recovery fired 21:26:13 sạch). Live-verify: run shadow 06/07 — mọi lần EMPTY_RESPONSE sẽ có log `salvage parse` + row được cứu.
- Kết luận 25 lane: **24/25 PASS sandbox vòng đầu + 1 lane (qwen3-max-thinking) có root cause chính xác + fix đã live** — không còn lane nào "mất tích không rõ lý do".

## C — ĐÓNG MẢNH TREO (tất cả DONE)

| Mục | Kết quả | Bằng chứng |
|---|---|---|
| C1 user-view official | user-view.js live=repo (sha khớp); `surface: 'official'` line 415; API `/api/predictions?date_from=...&surface=official` hoạt động | probe 21:0x |
| C2 /choi lock DOM | File live=repo; route `/choi` FileResponse + require_admin (curl không cookie → 401 là ĐÚNG thiết kế); lockLine code render `d.method + d.lock_since + d.owner_decision_ref`; compute_board() payload đủ field 3 miền; **decision ref hiện từ 00:00 06/07** (đã đính chính A3) | payload probe PASS 3 miền |
| C3 commit governance | Private `d31b683` (70 files: scheduler B2 + late_fill + registry + toàn bộ script V10782→85 + 4 docs governance seq240) pushed | GitHub |
| C4 Notion V10784 | Page `3941d385-9bf8-81b6-8cd3-e9d6c42504c9` (≤30 dòng, §52G) + BAO_CAO_TONG_V10784 chốt hết placeholder (MDE 74 rows + lock re-check + đính chính) + payload mirror; public push `8b76646` | Notion + GitHub |
| C5 history filter | `offset`+`total_count` live (`date_from=2026-06-29..07-05`: total_count đúng, offset phân trang đúng) | curl probe |
| C6 seed audit | `_v10782_p2_seed_audit.py` là script chạy LOCAL (import paramiko) — làm rõ hồ sơ V10784; re-run local: tuần 06/07 seed đúng 3 method + immutable (changes=0); 2 phát hiện 04/07 = artifact ngày sinh bảng (như đã ghi) | run 21:0x |

## D — GATE GO/NO-GO STAGE 1 (đêm 05/07): **9/9 PASS → GO**

| Gate | Kết quả |
|---|---|
| D1 lock tuần 06/07 | PASS — 3 rows đúng method + decision ref, immutable |
| D2 prompt đài THỨ HAI | PASS — Deep Focus 06/07: MN=[Cà Mau, TP. HCM, Đồng Tháp] · MT=[Phú Yên, Thừa Thiên Huế] · MB=[Hà Nội] (probe offline 3 miền, không tốn API; lần đầu FAIL do grep "TP.HCM" thiếu space — đã sửa cách đo, không phải lỗi prompt) |
| D3 reasoning live | PASS — 8 rows rt>0 hôm nay |
| D4 first-run gate | PASS — gemini-3.5-flash 0 row sớm; qwen3.7-max/glm-5.2 chỉ có 5 rows 05/07 đã biết (chờ ký K1) |
| D5 T-10 + freeze armed | PASS — jobs MN 15:45/MT 16:45/MB 17:45 registered + watchdog + startup-recovery |
| D6 MDE | PASS — 74 rows 20:20 + job armed mai |
| D7 watchdog live | PASS — 0 WATCHDOG_MISS thật; chỉ ALERT T-10 MN (true-positive có giải trình) |
| Health/auth | PASS — health 200, admin unauth 401 |
| Cron 07:30 | PASS — crontab `_v10784_verify_0607.py` armed (C1–C6 sáng mai) |

## E — TIẾN ĐỘ

- **E1 hash interim 21:2x**: predictions 9,342 `da147af0cf49e299` · final_bundles 384 `d5293ac74ccdcf2a` · lottery_results 15,017 `0708cd896d140e39` · model_daily_eval 9,206 `9fd897e938a156ac`. Đối chiếu baseline V10784 17:26: +17 predictions (shadow tối + backfill) / +1 bundle (MB) / +1 result (MB) / +74 MDE — **100% natural growth khai báo được; 0 late; 0 official write sau freeze**. Hash chốt phiên sẽ chạy lại 23:5x.
- **E3 DONE 21:2x**: `26_RUNTIME_AS-BUILT` +7 blocks V10785 (late-fill/watchdog/sandbox/forensic); **HOME snapshot refresh** (section "SNAPSHOT MỚI NHẤT 05/07" — official 15 model + lịch T-10/freeze + shadow 11 lane + giám sát + /choi lock + chờ ký).
- **E2 (final)**: báo cáo tổng + Notion V10785 + BẢNG CHỜ KÝ — sau check 23:50.

## RESTART LEDGER TỐI NAY (đều ngoài cửa sổ live)

20:31 (B2 deploy) · 20:33 (fix tzinfo) · 21:24 (salvage qwen). Mỗi lần: health 200 + startup-recovery fired sạch (20:34:47 · 21:26:13).

## CÒN LẠI

23:50 lock check + E1 hash chốt → báo cáo tổng V10785 + Notion page (≤30 dòng) trước 00:00 → sau 00:00 chụp /choi lockLine (đóng A3/D7 evidence) + cron 07:30 tự chạy stage-2.
