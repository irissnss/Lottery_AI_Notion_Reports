# V10753.1 — Lô3 3-càng: backtest tìm method tốt hơn + đổi window 90→180

**Thời điểm:** 2026-06-26T01:05:00+07:00 · **Owner hỏi:** "3 càng cần test thử có gì hay ho mới khả quan hơn không?"

## Backtest nhân-quả 7 method ghép-prefix (118 ngày live)

Định nghĩa 3-càng nới lỏng: 3 chữ số (prefix + BT) xuất hiện như chuỗi con ở **bất kỳ giải nào**. BT = official thực tế; prefix chỉ tính từ dữ liệu **trước** ngày dự (không nhìn trước).

| Miền | substring_90 (deploy V10753) | substring_180 | global_lead_90 | Trần (oracle) |
|---|---|---|---|---|
| MN | 13.6% | **14.4%** | 8.5% | 81% |
| MT | 8.5% (≈ngẫu nhiên) | **14.4%** | 15.3% | 71% |
| MB | 1.7% (tệ nhất) | 3.4% | ~5.9% | 43% |

## Kết luận

- **substring_90 (vừa deploy ở V10753) KHÔNG tối ưu** — MT chỉ 8.5% (≈ngẫu nhiên 10%), MB tệ nhất.
- **`substring_180` thắng substring_90 ở CẢ 3 miền** (MN +0.8, MT +5.9, MB +1.7) → cửa sổ dài ổn định hơn.
- **Sự thật quan trọng:** 3-càng là cược **biên lợi nhuận thấp cố hữu** — trần ~14-15% (MN/MT), ~6% (MB). Conditional |BT-hit chỉ 16-18% vs 10% ngẫu nhiên → chữ số ghép gần như random, không có tín hiệu mạnh. → Nên xem 3-càng là **cược phụ vốn nhỏ**; MB 3-càng gần như không nên chơi.

## Thay đổi + Verify

- `main._generate_lo3_frequency`: cutoff `days=90 → 180` (1 tham số, additive, secondary output).
- diff sạch (+8/-5); compile OK; restart OK; `/api/health=200`; **4 bảng official IDENTICAL pre/post**.
- Rollback: đổi `days=180` về `90`.
