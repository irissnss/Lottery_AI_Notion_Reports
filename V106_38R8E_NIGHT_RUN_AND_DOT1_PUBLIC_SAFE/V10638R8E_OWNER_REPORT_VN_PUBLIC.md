# V106.38-R8E — NIGHT RUN (P0-P5) + ĐỢT 1 SHADOW LANES (PUBLIC-SAFE)

> Public-safe. Không code business, dòng DB thô, API key, IP/đường dẫn server.
> Không claim *_FIXED / PROMOTED. Read-only/shadow. 0 thay đổi official (0 ghi, mode=ro).

- **Auditor**: Opus 4.7 | 2026-05-30
- **Chain**: R8 → R8B → R8C → R8D → **R8E (night run + Đợt 1)**.
- **Môi trường**: IDE local + DB forensic local (KHÔNG VPS shell) → việc cần VPS chỉ flag/chuẩn bị.

---

## 1. NIGHT RUN — 6/6 PHASE PASS

| Phase | Kết quả |
|---|---|
| 0 Verify R8D | ✅ 5 VIEW PASS, DD v1.0, 163 bảng |
| 1 Backup/drop-merge | ✅ backup thật + demo COPY (75=75, 0 mất số); prod DROP chờ owner |
| 2 KPI per-slice | ✅ **MT·T5 BT=76.9% p=0.013 sig**; MN·T7 yếu (23% vs 52%); MB≈random; MB freq p~0.01 token-free |
| 3 MB cap shadow | ✅ strength 10→6 phẳng; WR 44→16% (time-confounded honest); patch chưa áp |
| 4 Token cost/edge | ✅ giữ 5 token có lift; **12 token no-lift → LIMIT** (chưa áp) |
| 5 Flow + safety | ✅ official=10/lane=18/shadow=62; **official 0 ghi, diff=0** |

---

## 2. ĐỢT 1 — SHADOW LANES (token=0, official untouched)

### A1 — MB freq_hot forward-validation lane
- Backtest 91 ngày: **2.75 hít/ngày vs 2.38 random, lift +0.37, z=2.62, p=0.0089** (significant, borderline đa-kiểm-định).
- Token cost: **ZERO** (chỉ đếm tần suất).
- Đã seed forward-log để chấm tiến hằng ngày.

### A3 — deep-dive 2 slice
- **MT·T5 (mạnh)**: top model là **ML FREE** — combo-no-token 84.6%, random-forest 84.6%, meta-learning 76.9%. → lane MT·T5 nên dựng từ cụm ML free (không token).
- **MN·T7 (yếu)**: KHÔNG thiếu tín hiệu — gemini-2.5-pro hit **81.8%**, gemini-2.5-flash 75% trên T7, nhưng bundle official chỉ 23% → **lỗi SELECTION** (bundle bỏ qua model giỏi của T7). → per-slice weighting sẽ sửa.

---

## 3. PHÁT HIỆN CHỐT
- Edge token-free thật: MB freq_hot (p~0.009) + MT·T5 dùng ML free.
- MN·T7 là lỗi chọn (selection), không phải thiếu tín hiệu → khẳng định hướng per-slice model-weighting.
- 12 token-AI MB không lift → tiết kiệm được khi LIMIT.

---

## 4. LỘ TRÌNH KIỂM SOÁT
Toàn bộ việc còn lại được quản trong roadmap tuần tự (4 đợt): Đợt 1 (shadow, đang chạy) · Đợt 2 (production, chờ owner) · Đợt 3 (per-slice/cap/token) · Đợt 4 (data-bound 2026-06-03).

## 5. CHỜ OWNER (production/VPS/token)
Phase B drop/merge · deploy 5 VIEW · backfill tên đài · cap MB forward (token) · LIMIT weight · cron. Official chỉ đụng khi owner bấm nút + backup.

**An toàn**: official 0 ghi (mode=ro); 0 promote lane; 0 token; 0 deploy/cron. Đợt 1 = shadow/read-only.
