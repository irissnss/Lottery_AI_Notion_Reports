# V10775 — COMBO LỆCH MỐC + TRỌNG SỐ TOTAL OUTPUT — báo cáo đầy đủ từ yêu cầu đến xử lý — 2026-07-05

## PHẦN 1 — YÊU CẦU CỦA OWNER (nguyên văn, 05/07 00:58)

> "Nếu như ML các mốc chưa chính xác thì muilt model như combo hoặc super chắc phải kiểm tra lại rồi đó em. nhồi vào đó mốc không tương thích thì thôi bó tay em luôn đó. Total Output offical có cần thay đổi gì không sau khi đào sâu, có cần + thêm trọng số cho model nào trong quá trình total output không em? Ghi chép đầu đủ chi tiết , từ yêu cầu đến xử lý lên githubs report và notion nha em không bỏ sót , rơi rớt gì nha em."

Ba câu hỏi tách ra:
1. Combo/Super có đang "nhồi mốc không tương thích" không? → phải kiểm tra lại theo mốc.
2. Total Output official có cần thay đổi gì không sau khi đào sâu mốc (V10774)?
3. Có cần cộng trọng số cho model nào trong quá trình total output không?

## PHẦN 2 — CÁCH KIỂM CHỨNG (phương pháp, tái lập được)

- Dữ liệu: bản sync live `artifacts/live_sync/20260705_001326` (DB + trace đồng bộ từ VPS trước khi phân tích).
- Soi code: `combo_super.py` (combo-super = 4 ML + AI, tự chạy model), `scheduler.py` `_run_combo_no_token` (combo-no-token = 4 ML weighted).
- Soi dữ liệu live 02–04/07 + phân phối `run_source` từ 10/5: xác định giờ chạy thật của combo từng miền.
- Backtest 56 ngày (10/5 → 04/07, giai đoạn dữ liệu ổn định theo owner), kinh tế /choi (50đ × 98.000đ; vốn 27.000đ/số MB, 18.000đ/số MN-MT), song-thủ top-2, chia 2 nửa để đo BỀN, cột 28 ngày gần.
- Mọi con số sau đó được đối chiếu: bảng shadow (engine live) phải KHỚP backtest độc lập.

## PHẦN 3 — TRẢ LỜI CÂU 1: COMBO CÓ LỆCH MỐC KHÔNG? → CÓ, Ở MB (owner đoán đúng)

### Mốc combo THẬT đang chạy (kiểm chứng live)

| Miền | combo-no-token | combo-super | Đánh giá |
|---|---|---|---|
| MN | 04:00 (`auto_daily`) | 04:17 (`auto_daily`) | 1 mốc duy nhất — khớp miền, không lệch |
| MT | 04:00 từ 02/07 (theo V10766; trước đó 16:35) | 16:40 (`ai_chain`, sau KQ MN, TRƯỚC quay MT 17:15) | hợp lệ; combo-super MT +39.4M BỀN — không cần đổi |
| MB | 17:30 (`rerun_post_mt`; bản 04:00 giữ ở pre_result 55/56) | 17:32–18:03 (`ai_chain`, TRƯỚC quay 18:15; KHÔNG có bản 04:00) | **combo mặc định mốc sameday trong khi official chạy mốc điều-kiện V10770 → LỆCH** |

### Combo MB theo TỪNG MỐC (56 ngày, /choi)

| Cách | as-is (mốc đang chạy) | @04:00 | @D-1 | @MỐC ĐIỀU-KIỆN (như official) |
|---|---|---|---|---|
| combo-no-token | −4.2M | −53.2M | +5.6M | **+35.0M BỀN 2 nửa (12.6/22.4)** |
| combo-super | −53.2M | (không tồn tại) | +10.5M | +0.7M |

→ **Đúng như anh nói: combo-no-token bị "nhồi" mốc sameday nên −4.2M; nếu đi ĐÚNG mốc điều-kiện như official thì +35.0M BỀN — lệch +39M chỉ vì mốc.** combo-super lệch tới +54M (−53.2M → +0.7M) nhưng kể cả đúng mốc vẫn chỉ hòa → combo-super MB yếu tự thân, không chỉ vì mốc.

### Đã làm gì
- KHÔNG tự đổi mốc combo (governance). Thêm 2 variant forward vào shadow V10772: `combo_nt_cond`, `combo_super_cond` (combo áp đúng mốc điều-kiện) — panel 🌲 /monitoring đo FORWARD từ 05/07, checkpoint 14/07.

## PHẦN 4 — TRẢ LỜI CÂU 2+3: TOTAL OUTPUT CÓ CẦN ĐỔI / CỘNG TRỌNG SỐ KHÔNG?

### Backtest trọng số (56 ngày, /choi)

**MT — CÓ TÍN HIỆU MẠNH NHẤT: nên cân nhắc trọng số RF×2 (sau forward):**

| Cách MT | P&L 56d | Nửa 1 | Nửa 2 | Bền? |
|---|---|---|---|---|
| ML-plurality trọng số **RF×2** | **+68.8M** | +19.7M | +49.1M | **BỀN** |
| RF-only (≡ RF×3) | +68.8M | +5.0M | +63.8M | BỀN (nửa 1 mỏng) |
| combo-super as-is | +39.4M | +29.5M | +9.9M | BỀN |
| **OFFICIAL MT** | +29.6M | +0.1M | +29.5M | BỀN |
| ML-plurality đều phiếu | +24.7M | +14.8M | +9.9M | BỀN |

→ RF×2 giữ 3 ML kia làm "phanh" nhưng cho RF quyền dẫn — cân bằng nhất (2 nửa đều dương mạnh). Hơn official +39M.

**MB — trọng số RF×2 KHÔNG bền; RF×3 ≡ RF-only mới là ứng viên:**

| Cách MB (@mốc điều-kiện) | P&L 56d | Bền? |
|---|---|---|
| RF-only ≡ RF×3 | **+44.8M** | BỀN |
| combo-no-token đúng mốc | +35.0M | BỀN |
| plurality đều phiếu (OFFICIAL logic) | +30.1M | BỀN |
| trọng số RF×2 | +20.3M | KHÔNG (nửa 2 −2.1M) |

→ MB: câu trả lời trọng số trùng với checkpoint RF 14/07 đã chạy — nếu RF thắng forward thì chuyển hẳn RF (tương đương ×3), không cần nấc giữa ×2.

**MN — TRỌNG SỐ KHÔNG CỨU ĐƯỢC (quan trọng):**

| Cách MN | P&L 56d |
|---|---|
| deepseek-reasoner MỘT MÌNH | **+40.1M BỀN** |
| gpt-oss-120b một mình | +25.0M BỀN |
| plurality tất cả model, deepseek×3 | +1.7M |
| combo-super as-is | −3.2M |
| plurality tất cả, deepseek×2 | −17.9M |
| plurality tất cả đều phiếu | −22.8M |
| **OFFICIAL MN** | **−37.5M** |
| combo-no-token as-is | −47.3M |
| ML-plurality (4 ML) | −57.1M |

→ Dù cộng trọng số deepseek×3, aggregate MN vẫn chỉ +1.7M so với deepseek-only +40.1M. **Vấn đề MN là CẤU TRÚC — quá nhiều model yếu cùng bỏ phiếu — không phải thiếu trọng số.** Phải quyết chọn model (đi cùng CP-66.9), em không tự đổi.

### KẾT LUẬN TOTAL OUTPUT (trả lời thẳng)
1. **Hôm nay KHÔNG đổi số official nào** — theo governance mọi thay đổi official cần forward-proof + owner OK.
2. **3 ứng viên đã vào đo FORWARD từ 05/07:**
   - MB: RF@mốc-điều-kiện (+44.8M backtest) vs plurality hiện tại (+30.1M) vs combo-đúng-mốc (+35.0M) — panel 🌲.
   - MT: ML-plurality RF×2 (+68.8M backtest) vs official (+29.6M) — panel 📶, `wplur_rf2_ml` là BEST_HINT MT mới.
   - MN: không có ứng viên trọng số — chờ anh quyết cấu trúc (deepseek-only là ứng viên mạnh nhất, +40.1M BỀN).
3. **Checkpoint 14/07**: đọc cột FORWARD, cái nào giữ khoảng cách thì em trình anh quyết chuyển.

## PHẦN 5 — THAY ĐỔI KỸ THUẬT (đầy đủ)

1. `web/backend/_v10772_mb_rf_shadow.py`: 12 → 15 variant (`combo_nt_cond`, `combo_super_cond`, `wplur_rf2_cond`); backfill tự-lành khi thiếu variant mới; note ghi số backtest từng mốc.
2. `web/backend/_v10765_aggregation_signal_shadow.py`: 4 → 5 variant (`wplur_rf2_ml` cho cả 3 miền); BEST_HINT MT đổi `official` → `wplur_rf2_ml` (ứng viên forward); backfill tự-lành 56 ngày.
3. `web/frontend/monitoring.html`: panel 🌲 thêm 3 dòng V10775 + note "combo LỆCH MỐC"; panel 📶 thêm cột RF×2 + note kết luận trọng số 3 miền.
4. Không đổi dòng code nào của: bộ chọn số official, combo runtime, /du-doan, /choi, scheduler flow.

## PHẦN 6 — BẰNG CHỨNG & VERIFY (đầy đủ)

- Đối chiếu bảng shadow (engine live) vs backtest độc lập 56d: `combo_nt_cond` +35.0M = +35.0M KHỚP; `combo_super_cond` +0.7M KHỚP; `wplur_rf2_cond` +20.3M KHỚP; `wplur_rf2_ml` MT +68.8M KHỚP (cả trên VPS).
- VPS live sau deploy: V10772 trả 15 variant; V10765 trả 5 variant + BEST_HINT MT mới; backfill đủ (96 rows MB, 168 rows agg-signal).
- Hash 4 bảng official pre/post deploy IDENTICAL: predictions 9268 `548c6421`, final_bundles 381 `0f70d14a`, lottery_results 15010 `2076e8f7`, model_daily_eval 9132 `cbd1f568`.
- Smoke: health 200, /du-doan 200, admin API 401, 6 zombie API 404 — ALL PASS.
- Backup: `backups/v10775_pre/` (3 file pre-edit). Rollback = restore + restart.
- Commit: private `833d656` (Lottery_AI_Test), public repo này. Docs đồng bộ cùng phiên: CHANGELOG V10775, SSOT V10775, FU-V10775-COMBO-MOC-WEIGHT, AUTOMATION_STATE seq 230.

## PHẦN 7 — VIỆC CHỜ OWNER (không tự làm)

1. **CP-66.9** adaptive-exploit MN (quá hạn) + **phương án cấu trúc MN** (deepseek-only +40.1M vs official −37.5M).
2. OK/không OK **drop 41 bảng chết** (`DEAD_TABLES_DROP_CANDIDATES.json`).
3. **Checkpoint 14/07**: quyết theo forward — (a) official MB → RF@điều-kiện?; (b) official MT → trọng số RF×2?; (c) mốc combo MB → áp điều-kiện hay giữ nhãn "số nóng sameday"?
