# V10749 — OFFICIAL selector change MT: tắt convergence dampener (owner-approved)

**Thời gian:** 2026-06-25T21:55:00+07:00
**Owner:** duyệt phương án A (đổi selector MT official) + dặn soi kỹ tầng shadow-first/prompt-khác trước khi đụng official. ĐÂY LÀ THAY ĐỔI OUTPUT OFFICIAL (chỉ MT).

## Soi shadow trước (theo owner dặn) — SẠCH
- generate_final_bundle (selector official → /du-doan) lọc FAIL-CLOSED chỉ 15 model output-eligible; shadow KHÔNG vào.
- run_source 7d: model OE chỉ ở official lanes (ai_chain/auto_daily/rerun_post_mn/rerun_post_mt); truy vấn "run_source shadow/first mang model OE" → NONE.
- phase_first_shadow ghi bảng shadow (source_model=PHASE_FIRST_DECISION), không ghi predictions với model OE.
- => shadow-first + prompt-khác CÔ LẬP hoàn toàn khỏi vote official.

## Thay đổi (surgical, region-gated, reversible)
- main.py generate_final_bundle: _PP1_DAMPENER_DISABLED_REGIONS={MT}; MT → _PP1_DAMPENER_FACTOR=1.0 (tắt convergence dampener). MN/MB giữ 0.85 byte-identical.
- Cơ sở: 89d — MT plurality (số nhiều model OE đồng thuận nhất) vượt official BT lô-hit +10.1pp (47.2% vs 37.1%); dampener phạt đúng con số đồng thuận hay trúng.
- Rollback 1 dòng: bỏ MT khỏi set + restore backups/v10749_remote_pre/main.py.

## Verify deploy
- compile PASS, restart OK, health=200, marker live, 4 bảng official IDENTICAL pre/post (predictions 6cd53e1dedbe1a02, final_bundles 9779d624c5a52964, lottery_results 3812f94588de6d0f, model_daily_eval f7dd3711b9f5191c) — không regen quá khứ. MN/MB không đổi. MT áp dụng từ chu kỳ mai.

## Theo dõi 5–7 ngày
- So MT BT lô-hit + P&L vs baseline 37.1% (kỳ vọng ~47%). Tệ đi → revert ngay. Tốt → cân nhắc mở MN/MB (chỉ +2pp) hoặc step-2 plurality-tilt. Honest: step 1 = bỏ thành phần hại rõ nhất, không hứa phép màu.
