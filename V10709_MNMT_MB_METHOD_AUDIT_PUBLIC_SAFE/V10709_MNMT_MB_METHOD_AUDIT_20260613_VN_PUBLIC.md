# V10709 — MN/MT vs MB lane mechanism + MB-rules-method application audit

> **Compiled**: 2026-06-14 10:41 VN  
> **Data as-of**: 2026-06-13  
> **Measured on**: live VPS DB (read-only audit, official untouched)  
> **Machine-readable source**: `machine_readable/V10709_MEASUREMENTS.json`

Public-safe summary. Báo cáo này gom cơ chế MN/MT/MB, kết quả 10 ngày live, last 30d, và A/B MB-style doctrine khi áp sang MN/MT.

---

## 1. Executive verdict

- MN/MT vẫn là **model-AI-driven**; MB là **rule-driven**.
- MB-style doctrine đã được áp sang MN/MT từ **2026-06-10**, nhưng **chưa chứng minh được lift rõ**: MN hiện **không đổi** so với control, MT **hơi tệ hơn**.
- MB V2 rule **vượt official MB trên 30d**, nhưng strict live 10d thì **gần parity** và xiên vẫn yếu.
- Baseline 1-num trong JSON: **MB 23.7%**, **MN 42.4%**, **MT 34.8%**. MB có room lớn nhất; MN/MT cao hơn baseline nên khó kéo lift hơn.

---

## 2. Mechanism snapshot

| Region | Type | Method | Uses model votes | Anti-herd |
|---|---|---|---|---|
| MN | model-AI-driven | D_w06 vote over predictions + per-region TOP-K (K=25/22) | yes | no |
| MT | model-AI-driven | D_w06 vote over predictions + TOP-K (K=10, stricter) | yes | no |
| MB | rule-driven | MANUAL soi-cau drive_weight + same-day MN/MT board injection (V10693/V2) | no | yes |

- MB là lane rule-driven + anti-herd.
- MN/MT vẫn là lane model-vote driven; MB-style doctrine trên MN/MT hiện chỉ là hybrid A/B thử nghiệm.

---

## 3. Live since 2026-06-04

| Region | Days | Top1 | Top2 | Top3 | Xien2 | Xien3 | Official top1 |
|---|---|---:|---:|---:|---:|---:|---:|
| MB | 10 | 30.0% | 20.0% | 0.0% | 0.0% | 0.0% | 40.0% |
| MN | 10 | 30.0% | 30.0% | 50.0% | 20.0% | 20.0% | 50.0% |
| MT | 10 | 40.0% | 10.0% | 30.0% | 0.0% | 0.0% | 40.0% |

Ghi chú: `n_days = 10` là số ngày kể từ lúc V10709 live start. Đây là window mới nhất trong JSON.

---

## 4. Last 30d

| Region | Days | Top1 | Top2 | Top3 | Xien2 | Xien3 | Official top1 |
|---|---|---:|---:|---:|---:|---:|---:|
| MB | 30 | 23.3% | 16.7% | 20.0% | 6.7% | 3.3% | 16.7% |
| MN | 30 | 43.3% | 30.0% | 53.3% | 16.7% | 13.3% | 46.7% |
| MT | 30 | 36.7% | 33.3% | 30.0% | 6.7% | 3.3% | 30.0% |

Kết luận nhanh 30d:
- MN là lane mạnh nhất ở `top3` và xien, nhưng official vẫn rất sát.
- MT ổn ở `top1/top2`, nhưng xien còn yếu.
- MB V2 rule tốt hơn official MB ở 30d, nhưng không phải kiểu “lấn át” mạnh.

---

## 5. MB-style doctrine applied to MN/MT

| Region | Settled days | Treatment doctrine top1 | Control top1 | Days changed BT | Verdict |
|---|---|---:|---:|---:|---|
| MN | 4 | 75.0% | 75.0% | 0 | no effect yet (doctrine == control every day) |
| MT | 3 | 33.3% | 66.7% | 1 | slightly worse so far (1 change hurt: 06-11 doctrine 16 miss vs control 54 hit) |

Giải nghĩa:
- `Treatment` = gọi lại 7 LLMs với MB-style rule doctrine trong prompt.
- `Control` = cùng models nhưng không doctrine.
- Sample còn nhỏ nên đây chỉ là tín hiệu sớm, chưa phải kết luận cuối.

**Caveat:** sample mới khoảng 4-5 ngày sau 2026-06-10; kết luận chắc hơn sau khoảng 2 tuần, cỡ **2026-06-24**.

---

## 6. Branch presence

| Surface | Presence |
|---|---|
| MB_PERPOS_RULEDRIVEN_V2 | 10 days (06-04..06-13) |
| MN_OUTPUT_V1 | 11 days |
| MT_OUTPUT_V1 | 10 days |
| MN_DOCTRINE_AB_V1 | 6 rows |
| MT_DOCTRINE_AB_V1 | 4 rows |

- `MB_PERPOS_RULEDRIVEN_V2` đã chạy 10 ngày.
- `MN_OUTPUT_V1` / `MT_OUTPUT_V1` là lane model hiện hành.
- `MN_DOCTRINE_AB_V1` / `MT_DOCTRINE_AB_V1` là A/B doctrine mới cho MN/MT.

---

## 7. Honest summary

> MN/MT lane = model-AI-driven (NOT same as MB rule-driven anti-herd) by design. MB rules method WAS applied to MN/MT (V10707 doctrine A/B + V10708 ranker, hybrid, since 06-10) but improvement NOT yet proven (MN no effect, MT slightly worse, tiny sample). MB V2 beats weak official MB over 30d (23.3% vs 16.7%) but in strict 10-day live it's ~parity (30% vs 40%) with xien weak (0%). MN lane strongest (xien2/3 16.7/13.3% 30d).

---

## 8. Status

- `official_integrity`: READ-ONLY audit; official 4 tables not written; no code changed this session.
- No DB, JSONL, or log files were added to this public package.
- This report is public-safe and ready to be linked from `README.md`, `REPORT_INDEX.md`, and `LATEST_REPORT.json`.
