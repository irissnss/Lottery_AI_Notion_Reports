# V10845 — CUỐI NGÀY 25/07 (T7): TỔNG LỰC MỌI TẦNG + /choi HIỂN THỊ SỐ + CẢNH BÁO REALTIME (OWNER KÝ)

- Phiên: 25/07/2026 18:53 → 19:4x. Nguồn: sync `artifacts/live_sync/20260725_185535`.
- Lệnh owner (4 phần): (1) kiểm tra tổng lực từ đơn model, prompt, rules đến total, cơ chế học tập tích lũy xếp hạng, 3 miền 4 luồng; (2) **/choi hiển thị số kèm nhãn cảnh báo — đừng ẩn nữa; cảnh báo realtime theo từng ngày/tuần/thứ**; (3) chuẩn bị nền báo cáo rõ ràng để đổi giao diện (Plan owner có sẵn — phiên sau); (4) vấn đề rõ ràng thì fix nâng cấp ngay.

## 1. /choi MỚI — OWNER-SIGNED, ĐÃ LIVE

**Nguyên tắc:** số LUÔN hiển thị; chơi hay không do người dùng; hệ chỉ dán nhãn. KHÔNG đổi: số của method, lock/P&L, gate V10828 (vẫn chặn khóa vốn — chỉ thêm hiển thị), /du-doan, writer.

| Thành phần | Chi tiết |
|---|---|
| Số luôn hiện | `display_songthu` + `display_reason`: MN T7 hiện official BT (lock tuần V10781 E5 vẫn NGHỈ, vốn 0, KHÔNG ghi P&L); MB khi gate chặn → hiện số pre-gate, hoặc top-2 V67 trace sau cutoff, kèm **cảnh báo đỏ "KHÔNG khóa chơi, P&L không tính, rủi ro cao, anh tự quyết"** |
| Form realtime | `📊 Form: 7 lần gần x/y (±M) · thứ này x/y · tuần này x/y · xu hướng ↗/→/↘` (trend = so net 7 lần gần vs 7 lần trước) |
| Verdict ĐỘNG | CHƠI→CÂN NHẮC khi 7-lần ≤1 thắng & net<0 · CÂN NHẮC→NGHỈ tương tự · NGHỈ→CÂN NHẮC khi ≥3 thắng & net>0 (đúng ý "mạnh lên đừng nghỉ hoài, yếu đi đừng bắt chơi hoài"). Riêng T7-lock MN (chữ ký owner V10781): verdict giữ NGHỈ, thêm form T7 để owner tự quyết |
| Live ngay 25/07 | MN NGHỈ-T7 hiện **[92]** (trượt hôm nay — hiển thị trung thực ✗) + "T7 4 lần gần: 0 trúng (−14.4M) — lock NGHỈ hợp lý" · MT lock [74,02] **02✓** + form 6/7 (+8.6M) ↗ + T7 4/4 · MB gate-chặn hiện **[58,52] THAM KHẢO** (cả 2 trượt — gate hôm nay chặn ĐÚNG) + form 1/7 (−12.7M) hạ CHƠI→CÂN NHẮC |

## 2. TỔNG LỰC HÔM NAY 25/07 (T7 — MN 4 đài)

| Luồng | MN | MT | MB |
|---|---|---|---|
| Official | BT 92✗, lo2 0/2 (LOSE) | BT **02✓** (WIN; 13/15 model — gpt-5-mini + gpt-5.4 lỗi 500 provider cả 2 attempt) | BT **05✓**, lo2 [05,52]→05 |
| /choi | Nghỉ T7 (lock) — display 92 | [74,02] → **02✓** | Gate không khóa — display 58/52 |
| laneV2 | 76✗ (63 phụ✓) | 74✗ (68 phụ✓) | **[05,28] TRÚNG CẢ 2 — 28 = ĐỀ MB** |
| laneV3 (điều kiện) | **04✓ (official trượt — điều kiện cứu MN)** | 74✗ | **[05,78] cả 2 về** |
| V67 AE | — | 60(sc 5.47)✗ · 54✓ · 96✓ | top-score 58✗ 52✗; rank thấp 75✓ 98✓ 92✓ |
| Per-model any | 6/15 (ngày khó) | 10/13 | **14/15** (8 model chạm đề 28) |

- V67 tiếp tục cho bằng chứng scoring không phân biệt tốt (top-score trượt, rank thấp về) — đúng hướng FU-V10843.

## 3. 15 NGÀY (11→25/07) + TỔNG HỢP

- Official BT: MN 5/15 · MT 6/15 · MB 3/15 (any 7/8/7).
- /choi: MT **10/15** · MN 5/12 · MB 3/12.
- **M2s vs M0 forward (19→24/07): BT 11/18 = 61.1% vs 8/18 = 44.4% → +16.7pp; any 88.9% vs 61.1%.** Ngưỡng promote +5pp (n≥30) — đọc 28/07 cùng trial PB-18.1.
- laneV2 7 ngày: MN 4/7 · MB 4/7 · MT 2/7. laneV3 (từ 22/07): MN 3/4 · MB 3/4 · MT 1/3.
- Model 15d: top meta-learning 29/45, gemini-flash 28/45, opus/sonnet/xgboost 27/45; đáy gpt-5-mini 21/44. Nhóm: MN ML 71% ≈ LLM 70%; MT ML 59% > LLM 53%; **MB LLM 50% >> ML 35%** (trũng cũ).
- Roster empty 15d: gemma 12/45 (quota 429), qwen legacy 7/45 (đã đóng FU), còn lại 1/45 — lean agenda 28/07.

## 4. HỌC TẬP / RULES / XẾP HẠNG / PROMPT

- mined_rules active 105 · MRE max 24/07 (3068 rows) · rerank MN/MT/MB đều 25/07 · MDE 27 model hôm qua · training_history 19/07 (đợt retrain CN 26/07 02:00 sắp tới) · trace hôm nay **69/69 PB-18.1** · self-check **11/11 PASS** · journal 0 lỗi · quick_check ok · contract V10841 PASS (pool MT 13 khớp sự cố 2 model).

## 5. V10844 WHAT-IF MB — FORWARD NGÀY 1 THUẬN

- Row forward đầu 25/07 (ghi sớm 19:09, cron 21:10 upsert): **/choi = gate-block · laneV2 = 05✓ · laneV3 = 05✓.**
- Lũy kế pre_v10844 (19–24/07): /choi 0/4 · laneV2 BT 3/6 · laneV3 2/3. Ngưỡng +15pp/≥7d — đọc ~01/08.

## 6. ĐÓNG VÒNG V10841 + V10809

- **BOUNDARY 04:30 25/07 PASS**: helper trả `today=2026-07-25` (VN) trong khi `utc_date=2026-07-24` — chứng minh live tại cửa UTC≠VN → **V10841 live-verify đóng trọn 3/3**; FU-V10842 CLOSED.
- **CP-S4 done sớm 1 ngày** (owner không phản đối CP-S3 trước 25/07): gỡ 4 cron `_v10809_shadow_ab.py` + 3 one-shot V10842; backup `/root/backups_v10845/crontab_pre_v10845.txt`; xác nhận 0 dòng sót. Roadmap V10809 → **COMPLETED**, archive `docs/archive/ACTIVE_ROADMAP_V10809_SHADOW_AB_7D_20260725.md`. Playbook §1 thêm mốc 21:10 V10844, §5 cập nhật.

## 7. AN TOÀN + VERIFY

- Backup local `backups/v10845_pre/` + remote `/root/backups_v10845/` trước sửa; compile OK; restart `lottery.service` active; health 200; `money-board`/`mb-whatif`/`choi` anon = 401; VPS compute_board smoke khớp local từng miền.
- **Hash 4 bảng official pre=post IDENTICAL** (`predictions 10928/bb8fb9ef · final_bundles 444/14b29035 · lottery_results 15148/e65f1e09 · model_daily_eval 10711/c2f1589e`).

## 8. WATCH + LỊCH

- gpt-5-mini + gpt-5.4 MT lỗi 500 provider (1 ngày) — xem lại 26/07, chưa fix phản xạ.
- 26/07 02:00 retrain CN + 03:00 optimizer — kiểm sáng 26/07. 28/07: đọc promote M2s (+16.7pp hiện tại), skim rule-cond, lean/shadow agenda, FU-V10843.
- Verdict động /choi: theo dõi 7 ngày; nếu lật verdict >2 lần/tuần/miền → xem lại ngưỡng form.
- **Owner Plan đổi giao diện: sẵn sàng xử lý phiên sau** — báo cáo này + SSOT là nền bàn giao.

## 9. GOVERNANCE

- CHANGELOG V10845 · SSOT block · FU-V10845 (mới) + FU-V10842 CLOSED + FU-V10843 update · AUTOMATION seq 306 · playbook §1/§5 · roadmap archive.
