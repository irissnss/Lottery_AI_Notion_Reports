# V10799 — AUDIT MA TRẬN NHẤT QUÁN 9 LUỒNG SAU V10798 + VÁ 3 LỆCH SÓT + REPLAY 7 NGÀY

- **Ngày:** 2026-07-15 trưa (VN)
- **Trigger (owner 10:42):** "Làm cho cẩn thận nha em, nhất quán các luồng lane, official, /choi cũng như các phương pháp đơn model ML mới fix lại cho MT và MB… vấn đề là em đã tư duy liên quan, tương thích, nhất quán hết chưa thôi. chứ anh nhắc cái nào là lòi ra cái đó là sao em? Sau đó tổng hợp tổng lực toàn bộ dùm anh nha em."
- **Trạng thái:** DEPLOYED — hash 4 bảng pre=post IDENTICAL.

## 1. Cách làm khác trước

Các phiên trước xử lý theo TỪNG ĐIỂM owner nhắc. Phiên này rà NGUYÊN MA TRẬN: liệt kê 9 nhóm luồng × mọi mốc giờ đọc/ghi quanh thay đổi V10798, soi từng ô "có bị ảnh hưởng không, đã khớp chưa":

| # | Luồng | Mốc giờ liên quan | Kết luận |
|---|-------|-------------------|----------|
| 1 | Official chain (token → bundle inline → T-chốt → freeze) | 16:38/17:34 → 16:54/17:54 → :55 | ĐÚNG (V10798) |
| 2 | Lane v10692 (early + 17:10 all) + advanced + prompt-v2 | 16:53/17:52 + 17:10; 16:55/17:45/18:05; 16:56/17:58 | ĐÚNG — 17:10 giữ làm reference full-pool |
| 3 | K11a/K15 promote (đọc lane → fallback inline) | tại giờ chốt | ĐÚNG by-construction — chốt :54 đọc lane :53/:52 vừa sinh |
| 4 | /choi money board (CUTOFF 16/17/18, weekly lock, daily lock, combo V10794) | lock 17:52-17:54 < 18:00 | ĐÚNG — combo giờ thường đủ sớm hơn 3' |
| 5 | Đơn-model ML (MN BT1 official-source; MB ML re-predict 17:30; retrain CN 02:00) | 17:30 < 17:54 | ĐÚNG — không đổi gì (K14 đã kết luận NO_EDGE) |
| 6 | Selector K10/K13 + budget lane | 15:56/16:56/17:56 (sau freeze) | ĐÚNG — không đụng; chỉ cần chú thích regime-change khi đọc số |
| 7 | AE (adaptive exploit, */5 refresh) + leg m2 /choi | ~17:35-17:55 | ĐÚNG |
| 8 | Watchdog V10785 heartbeat 15' + MB Prediction Watchdog 17:55 | **LỆCH SÓT #1** | ĐÃ VÁ |
| 9 | Freeze V10782 + UI copy (/monitoring, /du-doan-test) | **LỆCH SÓT #2 #3** | ĐÃ VÁ |

## 2. Ba lệch sót tìm thấy (tự lòi trước khi anh nhắc) + vá cùng phiên

1. **Watchdog `T10_EXPECT` còn mốc :50 cũ** (`_v10785_late_fill.py`): job chốt đã dời 16:54/17:54 → heartbeat cron 15 phút chạy lúc 16:50-16:53 / 17:50-17:53 sẽ báo động giả "T-chốt chưa fire" MỖI NGÀY (alert-only — không hại số, nhưng gây nhiễu và làm mất niềm tin alert). **Vá:** `{MN (15,55), MT (16,55), MB (17,55)}` — check tại freeze, job :54 phải xong trước :55. Test 8 case time-gate ALL_PASS.
2. **Copy `/monitoring`** còn ghi "T-10 chốt 15:45/16:45/17:45" và "model về sau T-10 = shadow, không có phiếu official" — câu sau SAI từ V10798 (shadow về trước :54 CÓ phiếu). **Vá:** nhịp mới đầy đủ (lane sớm 16:53/17:52 → T-chốt 15:45/16:54/17:54 → freeze :55; model về trước :54 đều có phiếu).
3. **Copy `/du-doan-test`** laneTime MT ~16:50 / MB ~17:55 (cũ). **Vá:** ~16:53 / ~17:52.

Kèm đồng bộ docstring 3 module (comment-only, chống lệch tài-liệu-vs-code cho phiên sau): `_v10789_mb_lane_promote.py`, `_v10790_mt_lane_promote.py` (từ V10798 lane_bundle là nhánh CHÍNH, inline chỉ còn fallback), `_v10759_money_board.py` (combo V10794 giờ thường đủ 17:52-17:54).

## 3. Replay 7 ngày (08-14/07) — bằng chứng số

Chạy lại đúng thuật toán lane V10692 (MT K=10 / MB K=8, w2=0.6) nhưng cắt pool predictions theo `created_at`:

- **MB:** pool tại 17:45-cũ chỉ **3-6 voter** → tại 17:54-mới **7-8 voter** (gần GẤP ĐÔI — mốc cũ chạy trước shadow 17:47-52). Picks đổi 2/7 ngày.
- **MT:** pool 16:45-cũ 6-8 voter → 16:54-mới 7-9. Picks đổi 5/7 ngày.
- **Any-hit delta tuần này ±0-1** → đây là fix CẤU TRÚC pool-đủ + nhất quán luồng, KHÔNG phải thuốc tăng hit tức thì (MT còn trần vật lý: khóa xổ 17:00, 2/7 ngày shadow về sau 16:55).
- **Nhất quán by-construction:** tại chốt :54, K11a/K15 đọc NGUYÊN lane bundle (16:53/17:52) — official = lane chính xác từng số; khác biệt chỉ có thể xảy ra ở nhánh fallback inline (khi cron lỡ).
- Xác nhận từ log VPS: MB 17:10 all-region luôn INSUFFICIENT_POOL (token 17:33 chưa có) → không có row sớm rác; row MT cuối ngày là bản 17:10 (by design — reference full-pool cho lệch-monitor); money board vẫn loại row ≥ cutoff (anti-lookahead) — hành vi không đổi.

## 4. Các luồng xác nhận KHÔNG cần đổi (đã soi từng cái)

MN nguyên chuỗi (bundle 04:21, chốt 15:45, freeze 15:55, /choi BT1 đọc bundle < 16:00, NGHỈ T7); /choi weekly lock Thứ 2 + daily lock + CUTOFF 16/17/18; MB ML re-predict 17:30 về trước chốt 17:54; retrain CN 02:00; selector K10/K13 sau freeze; AE */5; MB Prediction Watchdog 17:55 (sau chốt :54 — đúng thứ tự); prompt-v2 16:56/17:58; advanced lanes 16:55/17:45/18:05; cron v10737 + v10658 lúc :55 nay đọc bundle GIÀU HƠN (hưởng lợi); shadow sau :55 vẫn insert predictions (chỉ bundle bị freeze) nuôi strength ngày mai.

## 5. Lưu ý đo lường (regime-change 15/07)

Từ 15/07 official pool đầy hơn → khi đọc số các checkpoint: K11a d7 (16/07), K15 d7 (17/07), selector-trio (23/07), lệch-monitor (24/07) PHẢI chú thích trước/sau 15/07.

## 6. Deploy + an toàn

- Backup 6 file `.bak_v10799` trên VPS + bản pre về `backups/v10799_pre/`.
- SCP 6 file (4 backend + 2 frontend) → py_compile remote OK → restart `active`.
- Smoke: health=200, /du-doan=200, /choi=401(login), /monitoring=401(login), admin noauth=401.
- **Hash 4 bảng pre=post IDENTICAL** (predictions 10084 / final_bundles 412 / lottery_results 15075 / model_daily_eval 9908).
- Rollback: `cp <file>.bak_v10799 <file>` ×6 + restart.

## 7. Scripts

`_v10799_replay_check.py`, `_v10799_lane_rows_probe.py`, `_v10799_cron_full.py`, `_v10799_vps_cron_lane_check.py`, `_v10799_local_test.py`, `_v10799_deploy.py`, `_v10799_deploy2.py`, `_v10799_admin_smoke.py`, `_v10799_lane_log_tail.py`.
