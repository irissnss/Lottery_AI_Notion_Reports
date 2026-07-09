# BÁO CÁO V10788-B — MỐC DỮ LIỆU ML PER MIỀN (09/07/2026 trưa)

## 1. Câu hỏi owner (11:51)

> "ML của MN phân tích và sử dụng mốc D-1 của 3 miền, còn ML của MT thì sử dụng mốc D-1 của 3 ngày hôm trước luôn không có same day MN, còn MB thì sao em? Nếu được em phân tích, kiểm tra lại tất cả các mốc xem mốc nào phù hợp hơn và nhận xét sau khi đổi mốc có thay đổi gì. MB phức tạp hơn lấy D-1 của sáng chiều gì đó lung tung lắm ah em."

## 2. Mốc dữ liệu thật của ML từng miền (xác nhận từ code)

| Miền | Mốc chạy | Input thật sự | Ghi chú |
|---|---|---|---|
| MN | 04:00 (1 lần) | Thống kê 30d miền mình (D-1) + momentum MT 7d **bắt buộc D-1** (draw-order guard V10667: MT xổ sau MN nên same-day không tồn tại) | Đúng như owner nói: toàn D-1 |
| MT | 04:00 (1 lần, từ V10766) | Miền mình D-1 + momentum MN & MB đều D-1. **KHÔNG same-day MN** | Đúng như owner nói |
| MB | 04:00 **rồi 17:30 chạy ĐÈ** | 04:00: toàn D-1. 17:30 (`rerun_post_mt`): momentum MT được phép `date <= hôm nay` (same-day) + inject tails MT tươi. Số 04:00 rotate sang cột "DD Trước", số 17:30 thành chính thức — doctrine 4-ML đọc số 17:30 | Đúng là "sáng chiều lung tung" nhất |

**Phát hiện code quan trọng:** model ML được **train với momentum D-1-only** (`include_same_day=False` — "backward compat with training"). Mốc 17:30 của MB bơm feature same-day vào model chưa từng học phân phối đó = **train/serve mismatch**. Đây là lời giải vì sao data tươi gần như không giúp gì.

## 3. Đo 60 ngày (10/05 → 08/07): mốc nào phù hợp hơn?

### MB — mốc 04:00 (D-1) vs mốc 17:30 (+same-day MT), 413 cặp

- Tổng: 04:00 BT **20%** vs 17:30 BT **22%** (83 vs 91 hit; 244 lần đổi số → đổi-thành-trúng 45 vs đổi-thành-trượt 37 = net +8 hit/60 ngày).
- Per model: lstm +7pp (15→22) · smart-ml +5pp · xgboost/meta +2pp · rf/combo-no-token 0 · smart-ensemble −2pp.
- Điều kiện "feature same-day cháy": số mới ∈ tails MT cùng ngày → hit 24%; số mới ∉ MT → 22%; giữ nguyên → 20%. Chiều đúng nhưng biên nhỏ.
- **Kết luận: mốc muộn 17:30 LỢI NHẸ (+2pp) — GIỮ.** Sự "lung tung" không gây hại, nhưng cũng không phải cứu cánh: MB yếu là do model (AUC 0.497), không phải do mốc.

### MT — lịch sử ≤01/07 (thời còn rerun same-day MN), 364 cặp

- Tổng: 04:00 BT 35% vs rerun 37% — nhìn tổng tưởng rerun tốt hơn, nhưng tách model thì phân cực:
  - ĐƯỢC: random-forest **+10pp** (35→44) · xgboost +8pp (40→48) · smart-ml/smart-ensemble +8pp.
  - MẤT: **lstm −15pp (37→21)** — đổi số 52/52 ngày = re-roll hằng ngày, phá form; combo-no-token −2pp.
- **Bằng chứng then chốt:** khi đổi số, số-mới-nằm-trong-tails-MN-cùng-ngày hit **29%** vs số-mới-KHÔNG-lấy-từ-MN hit **42%** → **chính phần "same-day MN" là nhiễu** (khớp đo echo MN→MT ≈ 0 hôm sáng, khớp quyết định V10766).

### MT — SAU khi đổi mốc (02/07+, chỉ còn 04:00): có thay đổi gì?

| Cửa sổ | ML top1 BT |
|---|---|
| 17–24/06 (2 mốc) | 23% |
| 25/06–01/07 (2 mốc) | 29% |
| 02–08/07 (1 mốc 04:00) | **33%** |

→ **Đổi mốc V10766 KHÔNG làm ML MT xấu đi — còn nhích lên.** Cảm giác "ML MT thảm hại" đến từ việc official bám modal khối ML chụm (6 phiếu như 1), không phải từ đổi mốc.

### Baseline 60d cạnh nhau (mốc hiện hành)

MN **37%** > MT **36%** >> MB **22%** — MB yếu CẤU TRÚC bất kể mốc nào.

## 4. Khuyến nghị mốc (kết luận)

| Miền | Khuyến nghị | Lý do |
|---|---|---|
| MN | **GIỮ 04:00** | Mốc tốt nhất hệ (37%); lag-1 MN +12pp khiến D-1 giàu thông tin |
| MT | **GIỮ 04:00** (V10766 re-verified ở 60d) | Same-day MN = nhiễu có số liệu (29% vs 42%); nếu ngày nào xét lại rerun → CHỈ rf/xgb, cấm lstm |
| MB | **GIỮ 17:30** | Lợi nhẹ +2pp, không đáng đổi; nút thắt MB là selector + model, không phải mốc |

## 5. Deploy + đề xuất mới

- **Deploy 12:00:** khối `rerun_ml` thêm `pre_hit/main_hit` → panel ⏱ MỐC & NHỊP hiển thị "mốc-04:00 BT x% vs mốc-muộn y% (n=...)" mỗi miền. Sandbox PASS, health 200/admin 401, hash 4 bảng pre/post IDENTICAL (efebca79/2e85228e/76af5ec6/4fc6e4a0), backup `.bak_v10788b`. DIAGNOSTIC-ONLY.
- **K14 (MỚI, chờ ký):** retrain sandbox biến thể MB với `include_same_day=True` ngay từ TRAIN (khép train/serve mismatch) — so AUC/backtest offline, KHÔNG đụng production khi chưa có kết quả + chữ ký.
- K13 (recency weight) / K10 (bloc dedup) / K11a (MB_OUTPUT_V1) / K9 (herd fade) vẫn chờ ký như báo cáo sáng.

## 6. Files

Probe: `web/backend/_v10788b_data_moc_probe.py` · Deploy: `_v10788b_deploy.py` (private repo). Docs: CHANGELOG V10788 PHẦN B, SSOT, FU-V10788-MILESTONE-AUDIT, AUTOMATION_STATE seq 248.
