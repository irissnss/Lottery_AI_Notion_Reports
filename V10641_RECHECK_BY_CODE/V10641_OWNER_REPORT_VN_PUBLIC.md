# V10641 — RECHECK BY CODE (read-only): phân xử 5 điểm tranh cãi bằng base-rate + p-value

**Ngày:** 2026-05-30 (đêm). **Chain:** … → V10640 → **V10641**. **Mode:** READ-ONLY (đo + báo cáo; 0 deploy / 0 đổi official / 0 push code-private / 0 AI-provider / 0 ví).
**Public push:** owner requested for cross-AI analysis (TanPhatAI). Mọi số truy được về query/script tái lập.

> ⚠ **OVERDUE:** CP-66.7 (LAG1 adaptive exploit) hạn 2026-05-21 — data-blocked, recheck 2026-06-03.

## Khung đo (vì sao kết luận đảo so với trước)
- HIT bạch thủ = bach_thu ∈ tập đuôi trúng (code: `database.py:4648`).
- **BASE-RATE per slice** = E[# đuôi trúng phân biệt mỗi ngày]/100, tính riêng region×weekday: **MN ~42% (T7 52%), MT ~30%/42%, MB ~24%**.
- LIFT = hit − base (cùng lát); p = one-sided binomial. PROMOTE chỉ khi **n≥30 AND lift≥+5pp AND p<0.05 AND no-lookahead PASS**.
- ⟹ **MN official 45% chỉ +3pp trên ngẫu nhiên; MB official 24% ≈ ngẫu nhiên (lift~0).** Mọi "edge" phải đo vs base này.

## 5 VERDICT (không nhãn giả, báo cả số xấu)
| # | Điểm | VERDICT | Sự thật theo code |
|---|---|---|---|
| **A** | MB G2 D-2 → MN | **KILL** | broad n=115: overlap quan sát 100% nhưng **base cũng 100% → lift +0.0pp, p=1.000**. "60%/76%" = phủ-sóng + slicing, KHÔNG tín hiệu. |
| **B** | MN override (LIVE) | **HOLD-LANE** | "+5.4pp vs official" ĐÚNG (+5.43pp, 13 override/92 ngày, net +5) — NHƯNG vs base +6.9pp **p=0.111 (không significant)**; per-weekday n=13-14 (<30); T7 −16pp/T6 −11pp/T4 −3.5pp âm. Reversible, no-lookahead PASS, impact thật tới nay = 0 (counterfactual). |
| **C1** | MT lane→official | **HOLD-LANE** | lane sạch +8.8pp vs official (khớp claim) nhưng region **p=0.070**, per-weekday n=8, **no-lookahead PARTIAL** (199/596 backfill). |
| **C2** | MT override (LIVE, bật ở V10640D) | **UNVERIFIED → NARROW** | "+4.4pp" xác nhận là **vs-official**; vs base +16.5pp region (p=0.0002) NHƯNG per-weekday n=16-18 (<30); **T6/T7/CN âm gần đây**; **BUG family-classifier** (random-forest/glm-5.1 bị loại nhầm, nemotron-super nhận nhầm). Đề xuất tắt T7/CN, giữ T3/T4/T5; KHÔNG full-kill. |
| **D** | MB freq_hot | **HOLD-LANE** | "+15.7pp" = ARTIFACT (freq_hot recent-hot 34.3% − official recent-COLD 18.6%=trailing-70d, official −5.1pp DƯỚI base). Cấu trúc full-history lift ~0 (W30 +0.5pp p=0.30). Tín hiệu chỉ ở W60 recent (không bền, ≠ config dàn W30 đã publish). Token-free xác nhận. |

## Sự thật cốt lõi (cho chủ + TanPhatAI quyết)
- **Không tín hiệu nào đạt chuẩn PROMOTE nghiêm** (n≥30/slice + lift≥+5pp vs base + p<0.05 + no-lookahead). Tất cả KILL/HOLD-LANE/UNVERIFIED.
- 2 override LIVE của agent (MN, MT) là "lane bet" hợp lý nhưng **chưa significant per-slice** (cần ~7 tháng/weekday để đủ n≥30). Đừng coi là "đã chứng minh".
- Per-slice bar (n≥30/weekday) **bất khả về cấu trúc** với ~4 tháng dữ liệu — đây là rào toán học, không phải lỗi method.

## Ưu tiên hành động (đòn bẩy lớn trước — KHÔNG tự thực thi, chờ chủ)
1. **MT override:** NARROW (tắt T7/CN đang âm, giữ T3/T4/T5) + fix family-classifier bug.
2. **MN override:** giữ lane, theo dõi T4/T6/T7; không quảng bá "đã chứng minh".
3. **MB freq_hot:** re-anchor doc về base; lock 1 cửa sổ W; forward-monitor.
4. **MB G2→MN:** KILL khỏi mọi tài liệu/quyết định.
5. CP-66.7: recheck 2026-06-03.

Chi tiết đầy đủ + bảng per-slice + đường dẫn file:dòng + script tái lập: `evidence/V10641_FULL_EVIDENCE_DETAIL.md`. Máy đọc: `machine_readable/V10641_SUMMARY.json`. Cross-ref: gói V10640.

*Public-safe: không chứa code private / DB rows / API keys / VPS internals. Số liệu là thống kê tổng hợp từ backtest read-only.*
