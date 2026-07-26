# V10860 — Tổng lực closeout 26/07/2026

## Nguồn dữ liệu

- DB source: VPS_SYNCED, đồng bộ DB + prediction trace theo cặp.
- Manifest nội bộ: `artifacts/live_sync/20260726_235321/manifest.json`.
- Ngày nghiệp vụ: 2026-07-26, Asia/Saigon, Chủ nhật (`weekday()=6`).
- Station-set đầy đủ: MN 3 đài, MT 3 đài, MB 1 đài.
- DB quick_check: OK.

## Kết luận chính

Ngày 26/07 xấu không phải do “thay áo”.

- UI V10859 chỉ thay HTML/CSS; không restart backend.
- Service dự đoán tiếp tục cùng process/runtime đã chạy từ 25/07.
- 72/72 prediction trace dùng PB-18.1 và có rules injected.
- Không có timeout/fallback/degraded ở official.
- Cả ba miền đủ đúng 15 output-eligible rows.

Đây là một ngày selection/ranking chọn sai top trên các nguồn có tương quan, không phải mất dữ liệu hay hỏng scheduler.

## 3 miền × các luồng

| Miền | Official BT | Per-model BT | Per-model any | Rule union có số trúng | V2/V3 |
|---|---:|---:|---:|---|---|
| MN | 50 trượt | 1/15 | 5/15 | 05,35,69,78 | BT 50 trượt |
| MT | 03 trượt | 8/15 | 14/15 | 02,16,28,75 | BT 40 trượt; any 16 trúng |
| MB | 69 trượt | 3/15 | 5/15 | 05,37,38,75 | BT 54 trượt |

Điểm quan trọng:

- MT model-pool rất khỏe. Champion 58 trúng nhưng K15 đổi sang challenger 03 trượt.
- MB có 38 trúng trong A-best và được ba LLM chọn, nhưng ranker chọn 54/39.
- Candidate supply không chết: mỗi miền đều có bốn tail trúng trong rule union. Sai nằm ở bước chọn top.
- Bốn “luồng” không độc lập hoàn toàn: nhiều luồng dùng chung predictions/rules, nên có thể cùng trượt trong một ngày.

## Các mốc live

- M2s 19–26/07: 12/24 BT so với M0 10/24, lift +8.3pp; any lift +29.2pp. Chưa đủ n=30, không promote sớm.
- PB-18.1 equal-window 9 ngày:
  - LLM any: 46.6% → 65.8%.
  - Official BT: 18.5% → 37.0%.
  - Một ngày xấu chưa đủ đảo kết luận trial.
- K15 MT in-trial 18–26/07: challenger 4/9, champion 5/9, net −1. Gate hành động là net ≤−2 tại mốc 28/07.
- K11a MB in-trial: challenger 2/9, champion 1/9. Hiện giữ.
- Rule-condition: B 8/18 bằng M0 8/18, chưa có edge.
- What-if MB mới hai ngày: V2/V3 một ngày trúng, một ngày trượt; chưa đủ bảy ngày.

## Bug rõ đã xử lý

1. Pattern-reasoning shadow bị lỗi khi `/choi` MB không lock và JSON chứa literal `null`.
   - Fix: JSON null được xử lý như danh sách rỗng.
   - Chỉ ảnh hưởng shadow measurement, không ảnh hưởng official.
2. Timing-audit cũ báo giả:
   - hard-code cửa 15–21/07;
   - trộn row retro sau xổ;
   - đọc timestamp UTC của MRE như giờ VN.
   - Fix: cửa 7 ngày động, pre-draw only, UTC→VN.
3. UI đa thiết bị:
   - settings tràn tại 320px vì nav cũ song song drawer;
   - user-view actions tràn 320–430px;
   - một số trang còn `overflow-wrap:anywhere`.
   - Fix và test lại.

## Kiểm thử UI

- 14 trang.
- 6 viewport: 320, 390, 430, 768, 1024, 1366 px.
- 84 trường hợp.
- Kết quả cuối: 78 PASS, 6 cảnh báo API giả lập tĩnh ở index, 0 FAIL.
- Drawer mobile được kiểm cả trạng thái đóng và mở sau khi transition hoàn tất.

## An toàn deploy

- 7 file runtime/UI khớp MD5 local↔VPS.
- Service active, health 200.
- Admin endpoint guest 401.
- Journal error-level: không có entry.
- Hash bốn bảng official giữ nguyên:
  - predictions
  - final_bundles
  - lottery_results
  - model_daily_eval

## Mốc 27/07 00:30 đã xử lý

- Weekly miner natural subprocess SUCCESS: W31, 105 rules, 9 STRONG, 32 CAUTION, 11.45 giây.
- Sau rollover, weekly money-board lock được materialize đủ 3 miền trước chu kỳ 04:00.
- Self-check cuối: 11/11 PASS; hash official giữ nguyên.

## Quyết định còn chờ

- 28/07: chốt PB-18.1, M2s n=30, K15, K11a, CP-L6 và CP-R4.
- Khoảng 01/08: what-if `/choi` MB đủ tối thiểu bảy ngày.

Không đổi official giữa trial chỉ vì một ngày xấu.
