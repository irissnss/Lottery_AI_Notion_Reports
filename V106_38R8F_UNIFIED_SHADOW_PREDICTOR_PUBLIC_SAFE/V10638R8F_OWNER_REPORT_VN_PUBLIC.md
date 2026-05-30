# V106.38-R8F — UNIFIED PER-SLICE SHADOW PREDICTOR + RANKING AUDIT (PUBLIC-SAFE)

> Public-safe. Không code business, dòng DB thô, API key, IP/path server. Không claim *_FIXED.
> Read-only/shadow. 0 thay đổi official (0 ghi, mode=ro). 0 token.

- **Auditor**: Opus 4.7 | 2026-05-30 | Chain: R8 → … → R8E → **R8F**

## 1. RANKING AUDIT (trả lời nghi vấn "output cứng nhắc")
- Weight model hiện tại = region-level + cửa sổ 30 ngày + base lô-gần-random → **weight gần đều (nhiễu)**, KHÔNG theo thứ/đài, còn lẫn model đã loại.
- Per-(region×weekday) WR biến thiên rộng (vd 33%..58%) — tín hiệu thật bị region-weight làm phẳng.
- A2 (shadow) sửa: ranking **linh hoạt theo thứ** (MN top-1 đổi 6/7 thứ) + chỉ model active.

## 2. B1 — UNIFIED SHADOW PREDICTOR (backtest 70 ngày, BT lô-hit vs official)
| Miền | Cơ chế | Unified | Official | Δ |
|---|---|---|---|---|
| **MB** | **freq_hot (token-free)** | **34.3%** | 18.6% | **+15.7pp** |
| MT | ML-free vote | 24.3% | 21.4% | +2.9pp |
| MN | per-slice ranking | 20.0% | 22.9% | −2.9pp |

## 3. ĐỌC TRUNG THỰC
- **MB freq_hot** là ứng viên mạnh nhất + miễn phí → nên thử qua lane/shadow live trước khi bàn deploy.
- MT ml-free hơn nhẹ. MN ranking KHÔNG hơn official (AI MN đã tốt) → cần lever khác hoặc chấp nhận trần.
- Giới hạn: chỉ MB freq forward được từ IDE (thuần lịch sử); MN/MT cần pipeline model.
- n=70, trần xổ số thấp → KHÔNG claim "đã cải thiện"; cần forward proof.

## 4. AN TOÀN
Official 0 ghi (mode=ro); 0 token; 0 deploy/cron/push-production; forward-log seeded 3 miền (chấm tiến). Mọi việc deploy/drop/token = owner-gated.

## 5. CÒN LẠI (đầy đủ, không sót)
- Owner-gate (14): push private/commit, Phase B drop/merge, deploy 5 VIEW, backfill tên đài, **deploy per-slice weighting**, LIMIT 12 token MB, cap MB forward (token), Cohere removal, admin board, cron, FU-V10628R1, UI/API smoke.
- Data-bound: 5 lane probation + MB-weekday-gap + CP-66.7/66.8 → 2026-06-03; FU-71 → 2026-08-23.
- Watch: provider badge, hard-locks, live-eligible-count-zero.
- Roadmap kiểm soát: `docs/ACTIVE_ROADMAP_STANDARDIZATION_ACCURACY.md`.
