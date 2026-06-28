# V10760 — BẢNG NGHIỆM THU TỰ ĐỘNG (Auto Deploy-Verification)

**Ngày:** 2026-06-28 · **Scope:** SHADOW diagnostic, ZERO official impact · **FU:** FU-V10760-AUTO-VERIFY

## Bối cảnh (owner)
Sau khi owner duyệt nghiệm thu live: "ok em tiếp tục đi em **lập bảng kiểm tra tự động** đi em" → thay cho việc chạy script tay mỗi lần.

## Bảng đo gì (tự động mỗi ngày sau closeout)
1. **OFFICIAL_BT** — per miền: BT official trúng lô **kể từ ngày deploy** (MN/MB 26/06, MT 25/06) so với:
   - **Nền cũ**: MN 44.9% · MT 37.1% · MB 23.7%
   - **Kỳ vọng**: MN ~52% · MT ~47% · MB ~31%
   - **Verdict theo cỡ mẫu**: <7 kỳ → ⏳ CHỜ ĐỦ MẪU; ≥7 kỳ → ✅ ĐẠT / 🟢 TRÊN NỀN / 🟡 TRONG BIẾN ĐỘNG (còn trong dao động nhị thức 90%) / 🔴 DƯỚI NỀN (cân nhắc revert).
2. **MONEY_BOARD** — tổng hợp `money_board_log` (/choi): số ngày bảng/official trúng + tổng nháy.

## Hiện trạng (mốc 28/06)
- MN: ⏳ CHỜ ĐỦ MẪU — 1/3 (33%), kỳ vọng 52%.
- MT: ⏳ CHỜ ĐỦ MẪU — 1/4 (25%), kỳ vọng 47%.
- MB: ⏳ CHỜ ĐỦ MẪU — 0/3 (0%), kỳ vọng 31% (0/3 xảy ra ~33% dù đúng kỳ vọng → bình thường với mẫu nhỏ).
- Bảng /choi: mới 1 ngày log (MN/MT mỗi bên 1 nháy = ngang official; MB 0).
- **Tái kiểm ~02-03/07** khi đủ 5-7 kỳ mới có verdict thật.

## Thành phần (§52)
- Module `_v10760_deploy_verify.py`: `compute_view()` + `snapshot()` + bảng `v10760_deploy_verify_shadow` (diagnostic_only=1, shadow_only=1, output_eligible=0, owner_approved=0).
- API `/api/admin/deploy-verify` (require_admin, Cache-Control no-store).
- Panel `/monitoring` "🧾 NGHIỆM THU TỰ ĐỘNG" (nhóm focus, auto-refresh 60s, đăng ký loadAllSections + setInterval).
- Scheduler: snapshot mỗi closeout trong `_materialize_closeout_measurements`.

## An toàn
READ-ONLY (lottery_results / final_bundles / money_board_log), ghi DUY NHẤT bảng shadow. ZERO official change. Hash-guard 4 bảng official (predictions/final_bundles/lottery_results/model_daily_eval) IDENTICAL pre/post. Rollback: gỡ 3 hook (api/scheduler/ui) + drop bảng shadow.
