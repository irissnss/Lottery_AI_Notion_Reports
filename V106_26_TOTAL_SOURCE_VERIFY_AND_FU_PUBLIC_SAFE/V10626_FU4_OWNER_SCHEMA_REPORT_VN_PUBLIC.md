# V10626 FU4 — Pre-register panel expansion theo schema MB owner-confirmed (PUBLIC)

> **Version:** V20.3.37.106.26.2
> **Created:** 2026-05-25
> **Schema source:** Owner image 2026-05-25 (xosodaiphat.com MB structure)
> **Status:** PRE_REGISTER_ONLY (report-only, no live application)

---

## Tóm tắt

Owner xác nhận cơ cấu giải MB qua hình ảnh: G.DB, G.1, G.2, **G.4 (4 bộ 4d), G.6 (3 bộ 3d), G.7 (4 bộ 2d)** đều là "ít bộ số" để dùng làm nguồn soi cầu.

Pass V10626 FU3 trước chỉ scan 4 source MB (DB#1, G1#1, G2#1, G2#2). Pass FU4 sửa schema gap, scan đầy đủ **15 source MB mỗi ngày** (thêm G4 4 bộ + G6 3 bộ + G7 4 bộ = 11 mới).

Sau scan + stability check w60/w90/w180, em đề xuất bổ sung **13 rule mới** (STABLE_ALL) vào pre-register panel V10626. Tổng panel: **58 + 13 = 71**, vẫn 100% PRE_REGISTER_ONLY.

## Risk overlay

Tất cả 13 rule mang đầy đủ tag risk (giữ nguyên policy V107):
- BH_FAIL_GLOBAL
- SELECTION_BIAS_RISK
- PRE_REGISTER_ONLY
- FORWARD_90D_INSUFFICIENT
- NEW_FU4_SCHEMA_EXPANSION

`live_eligible = False` cho tất cả 71 entry.

## Forward audit

Anchor: **2026-05-25**, window 90 ngày forward. Verify weekly. Chỉ rule sống sót sau 90 ngày forward audit mới được nâng `COMMIT_ELIGIBLE_SHADOW` (vẫn không live).

## Files

- Pre-register addendum panel CSV/JSON: `machine_readable/V10626_FU4_PRE_REGISTER_ADDENDUM_{MB,MN,MT}.{csv,json}`
- Stability proof: `machine_readable/V10626_FU4_NEW_MB_CANDIDATES_STABILITY.json`
- Raw scan output: `machine_readable/V10626_FU4_OWNER_SCHEMA_SCAN.csv` (top-8000)
- Owner Vietnamese report (private, mirror this file): `V10626_FU4_OWNER_SCHEMA_REPORT_VN.md`

## Safety

| Check | Status |
|---|---|
| Official mutation | 0 |
| Production switch | 0 |
| Provider/manual AI | 0 |
| Wallet | 0 |
| Live eligible | 0 |
| Public push | YES (this bundle) |
