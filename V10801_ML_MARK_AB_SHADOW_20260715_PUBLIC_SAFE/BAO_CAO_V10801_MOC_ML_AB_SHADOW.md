# V10801 — Mốc dự đoán ML per miền: backtest A/B 42 ngày (D-1 04:00 vs re-predict same-day) → MB giữ nguyên, MT có ứng viên meta+xgb → shadow forward-proof + panel (15/07/2026, DEPLOYED)

## 1. Câu hỏi owner (14:23, 15/07)

> "Model ML của MN và MT, MB khác nhau về mốc dự đoán à em xem kỹ nha. MN thì đang lấy D-1 của 3 miền, còn miền trung và miền Bắc thì sao? Có cần kiểm tra tới thời điểm này việc setting mốc như thế còn phù hợp không có ổn định không? MB nữa trước nữa sau gì đó anh không nhớ nổi, kiểm tra backtest lại xem có mốc nào tốt hơn nữa không em? v.v… ví dụ mốc giờ fix retrain cho MT và hiện tại MT không cần same day thì cũng nên tư duy mà xử lý nha. xem lại vẫn chưa yên tâm luôn em"

## 2. Hiện trạng mốc ML — xác nhận từ DB 10 ngày (06/07→15/07) + code

| Miền | Mốc dự đoán ML (4 model: meta-learning, lstm, xgboost, random-forest) | Bằng chứng DB |
|---|---|---|
| **MN** | **04:00, dữ liệu D-1** — duy nhất. Ép buộc: MN xổ ĐẦU ngày (16:15), không tồn tại nguồn cùng-ngày nào trước giờ chốt. Không có mốc thay thế để cân nhắc. | 10/10 ngày `04:00 auto_daily` |
| **MT** | **04:00, dữ liệu D-1** — CỐ Ý không re-predict cùng-ngày theo quyết định V10766 (đo 45 ngày money-board: re-predict MN→MT làm MT TỆ đi, +1.6M vs +16.3M). | 10/10 ngày `04:00 auto_daily`, KHÔNG có rerun row nào sau 14/06 |
| **MB** | **"Nửa trước nửa sau" đúng như anh nhớ**: 04:00 D-1 → re-predict sau KQ MN (~16:35) → re-predict sau KQ MT (**17:30-17:32, bản cuối**) với dữ liệu cùng-ngày. | 9/9 ngày có KQ: bản cuối `17:30-32 rerun_post_mt` < lane 17:52 < chốt 17:54 ✓ |

Retrain: CN 02:00 (một đường subprocess từ V10800) + guard 06:30 backstop, chung cho 3 miền, train bằng features D-1 — khớp với serve D-1 của MN/MT. K14 (V10793) đã đo phương án train same-day cho MB: AUC ±0.002 = nhiễu → giữ nguyên. **Không cần mốc retrain riêng cho MT.**

## 3. Backtest A/B mới (V10801) — "có mốc nào tốt hơn không?"

Phương pháp: 42 ngày (02/06→14/07), chạy đúng model files production trên VPS, mỗi ngày mỗi model dự đoán 2 nhánh — **A = mốc 04:00 D-1** (`include_same_day_cross=False`), **B = mốc re-predict cùng-ngày** (True + fresh tails miền nguồn; MT←MN mô phỏng 16:40, MB←MN+MT mô phỏng 17:30; draw-order guard giữ causal — miền xổ SAU không lọt vào). So **CẶP ĐÔI cùng model + cùng ngày** nên chênh lệch chỉ do độ tươi dữ liệu. Thước: top-2 any-hit vs tails thật.

### MT (nguồn same-day: MN)

| Model | Top2 A → B | Δ | Ghi chú |
|---|---|---|---|
| meta-learning | 57.1% → **71.4%** | **+14.3pp** | dương cả 2 nửa kỳ |
| xgboost | 47.6% → **59.5%** | **+11.9pp** | dương cả 2 nửa kỳ |
| lstm | 59.5% → 50.0% | −9.5pp | same-day làm TỆ đi |
| random-forest | 66.7% → 61.9% | −4.8pp | hơi tệ đi |

Gộp meta+xgb: B-thắng 16 ngày / A-thắng 5 ngày (sign test **p~0.027**), nửa đầu Δ+8, nửa sau Δ+3.

### MB (nguồn same-day: MT)

4 model tổng: top2 45.2% → 47.6% (+2.4pp, p~0.8) = **hoà** → mốc re-predict 17:30 hiện tại của MB **giữ nguyên là đúng** (không tốt hơn rõ rệt nhưng không tệ hơn; panel V10772 trước đó cũng cho thấy mốc same-day thắng về kinh tế với RF).

## 4. Vì sao CHƯA đổi production MT ngay

- **Mâu thuẫn 2 thước đo**: V10766 (kinh tế money-board toàn-wave, cửa sổ tháng 5-6) nói same-day HẠI MT; V10801 (hit-rate per-model, cửa sổ tháng 6-7) nói GIÚP meta+xgb nhưng vẫn HẠI lstm/rf. Cả 2 cùng đúng một phần: cái hại nằm ở lstm/rf, cái lợi nằm ở meta/xgb.
- Mẫu 42 ngày, và "meta+xgb" là lựa chọn SAU khi nhìn số liệu (post-hoc) — p~0.027 chưa trừ phạt multiple-comparison.
- Nguyên tắc hệ: mọi thay đổi official phải qua forward-proof + owner ký.

## 5. Đã triển khai (shadow-only, ZERO đụng official)

- **Bảng** `v10801_ml_mark_ab_daily` (`shadow_only=1, output_eligible=0, diagnostic_only=1, owner_approved=0`; UNIQUE date+region+model; row_source: backfill ≤14/07 < forward).
- **Cron 19:05 hằng ngày** (sau khi đủ KQ 3 miền; `--catchup 2` tự bù ngày thiếu): chạy lại 4 model × MT+MB × 2 nhánh, ghi bảng shadow. Backfill 42 ngày = 672 rows đã chạy lúc deploy.
- **API admin** `GET /api/admin/ml-mark-ab` (require_admin, Cache-Control no-store).
- **Panel /monitoring** "⏱️ MỐC ML A/B — D-1 04:00 (A) vs re-predict same-day (B)" — auto-refresh 60s, cột **FORWARD từ 15/07** là thước quyết định.
- **Ngưỡng hành động ghi sẵn** (chống trôi): ≥28 ngày forward, meta+xgb B−A ≥ +8pp top2 bền 2 nửa → trình owner phương án **re-predict CHỌN LỌC chỉ meta+xgb cho MT ~16:40** (lstm/rf giữ 04:00 — V10766 vẫn đúng với 2 model đó); ≤0pp → đóng, giữ nguyên V10766 toàn phần.

## 6. Deploy + an toàn

- Backup local `backups/v10801_pre/` + remote `/root/backups/v10801_pre/`; upload 3 file; py_compile OK; cron thêm; restart `active`.
- Smoke: `/api/health=200`, `/choi=401` (đòi login), `/api/admin/ml-mark-ab=401` no-auth ✓.
- **Hash 4 bảng official pre=post IDENTICAL**: predictions 10084/4ac2715e · final_bundles 412/d99a595e · lottery_results 15075/d8f34e1a · model_daily_eval 9908/97c981c1.
- Rollback: xoá dòng cron v10801 + restore 2 file từ `/root/backups/v10801_pre/` + restart.

## 7. Trả lời gọn từng ý owner

1. **"MN lấy D-1"** — đúng, và là lựa chọn DUY NHẤT (xổ đầu ngày). Ổn định 10/10 ngày.
2. **"MT, MB thì sao?"** — MT: 04:00 D-1 (cố ý, V10766). MB: 04:00 + re-predict 16:35/17:30 ("nửa trước nửa sau" anh nhớ đúng).
3. **"Còn phù hợp không, ổn định không?"** — MB: phù hợp, giữ (A/B hoà, mốc 17:30 về trước chốt 17:54 an toàn 9/9 ngày). MN: không có lựa chọn khác. MT: phù hợp với lstm/rf, CÓ TÍN HIỆU tốt hơn cho meta+xgb — đang forward-proof, chưa đổi.
4. **"Backtest mốc tốt hơn?"** — đã chạy 42 ngày như trên; ứng viên duy nhất đáng theo: MT meta+xgb same-day.
5. **"Mốc retrain cho MT?"** — retrain chung CN 02:00 + guard 06:30 (V10800), train D-1 khớp serve D-1 của MT, không cần mốc riêng.
6. **"MT không cần same-day thì tư duy mà xử lý"** — đã xử lý bằng bộ đo forward tự động + ngưỡng quyết định ghi sẵn; nếu đạt ngưỡng em trình anh đổi (1 quyết định, có số liệu), không đạt thì tự đóng.
