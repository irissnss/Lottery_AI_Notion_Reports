# V10829 — Báo cáo catalog điều kiện RULES (pipeline A→B)

Ngày phiên: 2026-07-21 (~00:22–00:40 VN)

## 1. Bối cảnh owner

Owner 00:22–00:28: sau vá V10828 (herd/AE), anh hiệu chỉnh hướng — **mọi rule có giá trị tiềm năng**; đuôi lộ thô không phải edge; cần **điều kiện + phối hợp**. Không đào `rule_id` rồi vá phản xạ. Chọn pipeline **C**: tầng A (kích hoạt) → tầng B (chọn số).

V10828 giữ như **hygiene tạm**, không mở rộng trong cửa sổ đo.

## 2. Phương pháp

- Sync forensic trước đo; leak-safe same-day `OK_SAMEDAY`.
- Backtest ≥180 ngày đến 2026-07-20; báo 2 nửa; placebo selection-aware cho top-ranked.
- Đối chứng RAW = union rules không điều kiện.
- Shadow-only: không đụng `/du-doan`, writer `final_bundles`, PB-18.1.

## 3. Kết quả catalog (sandbox)

| Hạng | ID | Số liệu chính |
|------|-----|----------------|
| RAW | — | precision ≈ **38.18%** |
| A1 | H-A1a | prec 50.1 · lift **+11.9pp** · n=81 · placebo rank 1/20 |
| A2 | H-A4b | prec 49.6 · lift **+11.4pp** · n=81 · placebo OK |
| A3 | H-A4a | prec 42.1 · lift **+3.9pp** · n=290 (coverage) · placebo OK |
| B1 | H-A4a+H-B2a | BT **46.9%** vs M0 31.6 → **Δ+15.2pp** · n=335 |
| B2 | RAW+H-B2a | ΔM0 **+11.4pp** |
| B3 | H-A4a+H-B1a | ΔM0 **+10.4pp** |

Primary materialize: **H-A4a ∧ H-B2a** (tier+anti-herd ∩ không chase D−1).

## 4. Ngưỡng wire (viết sẵn)

- A-best precision − RAW ≥ **+5pp** bền 2 nửa & placebo rank_frac ≤ 0.5
- B-best BT − M0 ≥ **+5pp**, n ≥ 30 region-days forward
- **28/07:** chỉ đọc sơ bộ (n nhỏ) — **KHÔNG promote**
- **~04/08 (≥14d) / ~11/08 (≥21d):** đọc ngưỡng → trình owner 1 quyết định wire hoặc đóng H

## 5. Deliverable kỹ thuật

| Hạng mục | Đường dẫn / endpoint |
|----------|----------------------|
| Runner | `web/backend/_v10829_rule_cond_shadow.py` |
| Finalists | `web/backend/_v10829_finalists.json` |
| Bảng | `v10829_rule_cond_daily` (shadow_only=1) |
| API | `GET /api/admin/rule-cond` (401 nếu không admin) |
| UI | `/monitoring` panel 📐 |
| Cron | 21:00 `--catchup 3` |
| Deploy | `_v10829_deploy.py` |

## 6. Verify deploy

- health=200 · rule-cond-unauth=401 · view `success=True` 3 miền
- hash 4 bảng official **IDENTICAL**: predictions `4b303e45` · final_bundles `23843b5a` · lottery_results `7ce7a13f` · model_daily_eval `07b4fbc5`
- Backup: `backups/v10829_pre/` + VPS `/root/backups_v10829/`

## 7. Phân biệt V10828 vs V10829

| | V10828 | V10829 |
|--|--------|--------|
| Bản chất | Hygiene tạm tầng tổng hợp/AE | Catalog điều kiện thật A→B |
| Hành động | herd≥3 strip + AE vote-gate | Đo + forward shadow |
| Cửa sổ này | **FROZEN — không mở rộng** | ACTIVE measure → wire sau ngưỡng |
