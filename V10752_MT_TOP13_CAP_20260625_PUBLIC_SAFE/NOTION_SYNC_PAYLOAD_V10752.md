# V10752 — OFFICIAL MT: cap top-13 model mạnh nhất (backtested +9.3pp)

**Thời gian:** 2026-06-25T23:40:00+07:00
**Owner:** duyệt tiến hành sau backtest. ĐỔI OUTPUT OFFICIAL (chỉ MT).

## Backtest causal 75 ngày (không lookahead — xếp hạng bằng phong độ 30 ngày TRƯỚC)
Plurality top-N model mạnh vs official BT lô-hit:
- MN: official 49.3% là TỐT NHẤT (top-N đều thua) → MN GIỮ NGUYÊN. (Tương quan thô "13–14>15+" trước đó là selection-bias, backtest đã bóc.)
- MT: top-13 = 45.3% vs official 36.0% → +9.3pp → đổi MT.
- MB: top-14 +2.7pp (nhiễu) → giữ + theo dõi.

## Thay đổi (surgical, region-gated, reversible)
- main.py generate_final_bundle: `_MAX_VOTERS_BY_REGION={"MT":13}` — sau gate, xếp model theo BT-rate (đã nối lineage V10751) + WR tiebreak, giữ top-13, bỏ 2 yếu nhất.
- Preview MT bỏ: claude-sonnet-4-6 (27.6%) + lstm (28.9%). MN/MB byte-identical.
- Robustness "trượt-hạng": nếu <13 model khả dụng (model lỗi) → dùng hết, không cap.
- Kết hợp V10749 (tắt dampener MT) = lean plurality + ít nhiễu ≈ đúng cấu hình backtest thắng.

## Verify deploy
- compile+lint PASS, restart OK, health=200, marker live, preview drop đúng 2 model yếu nhất, 4 bảng official IDENTICAL pre/post (predictions 6cd53e1dedbe1a02, final_bundles 9779d624c5a52964, lottery_results 3812f94588de6d0f, model_daily_eval f7dd3711b9f5191c). MT áp dụng từ chu kỳ mai. Backup backups/v10752_remote_pre/.

## Theo dõi 5–7 ngày
MT BT lô-hit vs baseline 36% (kỳ vọng ~45%). Tệ đi → revert (bỏ MT khỏi map). MN/MB không đổi.
