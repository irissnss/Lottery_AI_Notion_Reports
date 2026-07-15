# V10801 — Mốc dự đoán ML per miền: backtest A/B + shadow forward-proof (15/07, DEPLOYED)

**Owner 14:23:** "Model ML của MN và MT, MB khác nhau về mốc dự đoán à… MN đang lấy D-1, còn miền trung miền Bắc thì sao? Setting mốc còn phù hợp không, ổn định không? MB nửa trước nửa sau gì đó… backtest lại xem có mốc nào tốt hơn không… MT không cần same day thì cũng nên tư duy mà xử lý."

**Hiện trạng (verify DB 10 ngày):**
- MN: 04:00 D-1 — ép buộc (xổ đầu ngày), không có mốc thay thế.
- MT: 04:00 D-1, KHÔNG re-predict (quyết định V10766: same-day là nhiễu — đo kinh tế money-board toàn-wave).
- MB: "nửa trước nửa sau" đúng như owner nhớ — 04:00 → re-predict ~16:35 (sau KQ MN) → 17:30-32 (sau KQ MT, bản cuối) < chốt 17:54 ✓ 9/9 ngày.

**Backtest A/B 42 ngày (model production, so cặp đôi cùng model+ngày, top2 any-hit):**
- **MB: hoà** (45.2% → 47.6%, p~0.8) → mốc re-predict 17:30 GIỮ NGUYÊN đúng.
- **MT: meta +14.3pp (57→71%), xgb +11.9pp (48→60%)** khi có same-day MN — gộp B-thắng 16/thua 5 (p~0.027), bền 2 nửa; NHƯNG lstm −9.5pp, rf −4.8pp → V10766 đúng với lstm/rf, đáng ngờ với meta/xgb.
- Mâu thuẫn 2 thước (kinh tế wave cũ vs hit per-model mới) + mẫu 42d + chọn model post-hoc → **CHƯA đổi production**.

**Triển khai (shadow-only, ZERO official):** bảng `v10801_ml_mark_ab_daily` + cron 19:05 daily + API `GET /api/admin/ml-mark-ab` (admin, no-store) + panel /monitoring ⏱️ 60s (backfill 672 rows, FORWARD từ 15/07).

**Ngưỡng hành động ghi sẵn:** ≥28 ngày forward, meta+xgb B−A ≥ +8pp top2 bền 2 nửa → trình owner re-predict CHỌN LỌC meta+xgb MT ~16:40 (giữ lstm/rf 04:00); ≤0pp → đóng, giữ V10766.

**Retrain MT:** CN 02:00 + guard 06:30 chung 3 miền (V10800), train D-1 khớp serve D-1 — không cần mốc riêng.

**An toàn:** restart active · health=200 · admin 401 no-auth · hash 4 bảng official pre=post IDENTICAL · rollback `/root/backups/v10801_pre/`.

**Mốc theo dõi:** 16/07 tối (cron chạy lần đầu) · 29/07 (review 14d) · ≥12/08 (quyết định theo ngưỡng).

**GitHub:** `Lottery_AI_Notion_Reports/V10801_ML_MARK_AB_SHADOW_20260715_PUBLIC_SAFE/` (báo cáo đầy đủ + conversation context).
