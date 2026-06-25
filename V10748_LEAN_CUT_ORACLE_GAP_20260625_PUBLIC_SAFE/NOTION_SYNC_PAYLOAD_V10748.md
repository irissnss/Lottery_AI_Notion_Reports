# V10748 — Lean cut CP-L1 (cắt 6 model shadow đắt) + Oracle-gap diagnosis

**Thời gian:** 2026-06-25T19:35:00+07:00
**Owner:** "cắt giảm chi phí thực sự đi" + "đào sâu đơn model có tín hiệu mà total lệch lạc, kế hoạch xử lý triệt để".

## A) LEAN CUT — thực thi CP-L1 (owner OK 19/06)
- `model_registry.py`: 6 model SHADOW_AUTO → REMOVED: gpt-5.5, grok-4.20-multi-agent, deepseek-v4-pro, deepseek-v4-flash, qwen3-max-thinking, kimi-k2.5 (đắt + ~0 đóng góp độc nhất).
- SHADOW_AUTO_EVAL: 13 → 7 (giữ rẻ/free). OUTPUT_ELIGIBLE: 15 (không đổi — official nguyên vẹn).
- Tiết kiệm: ~6 model trả phí × 3 miền mỗi lượt shadow-eval/ngày.
- Verify VPS: shadow 13→7, restart OK, health=200, 4 bảng official IDENTICAL pre/post (predictions 6cd53e1dedbe1a02, final_bundles 9779d624c5a52964, lottery_results 3812f94588de6d0f, model_daily_eval fb495368581bd7fb). 0 official impact. Backup backups/v10748_remote_pre/.

## B) ORACLE-GAP DIAGNOSIS (đơn model trúng mà total trượt) — 90 ngày, metric LÔ
| Miền | Official BT lô-hit | Plurality (số nhiều model đồng thuận) | Oracle ≥1 model trúng | Recoverable miss |
|---|---|---|---|---|
| MN | 48.3% | 50.6% | 97.8% | 44/46 = 96% |
| MT | 37.1% | 47.2% (+10.1pp) | 95.5% | 52/56 = 93% |
| MB | 18.0% | 20.2% | 85.4% | 60/73 = 82% |

- Tín hiệu CÓ gần như mỗi ngày (oracle 85–98%) nhưng total chỉ bắt 18–48%.
- Plurality (số được nhiều model OE chốt nhất) ĐÃ vượt official, mạnh nhất MT (+10.1pp).
- Root cause: selector weighted_voting_wr có convergence dampener (0.85 phạt số ≥3 model đồng thuận) + anti-trap → tự hạ điểm số đúng.
- Lưu ý: oracle 97% là trần lookahead (không chốt trước được). Mục tiêu khả thi causal = plurality/consensus.

## Kế hoạch xử lý triệt để (staged, owner-gated)
Dựng Consensus Selector Lab (shadow): A/B official vs plurality-1/plurality-2/weighted-no-dampener theo lô-hit + song-thủ P&L + OOS theo miền×thứ. Forward 2–4 tuần. Nếu biến thể (đặc biệt MT) thắng bền → owner duyệt → thay selector. KHÔNG đụng official trước khi có bằng chứng forward.

## Rollback
Lean cut: restore backups/v10748_remote_pre/model_registry.py + restart lottery.
