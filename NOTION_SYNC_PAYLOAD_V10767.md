# V10767 — MB official dùng ML-plurality hôm qua (MB_Dm1) — OFFICIAL CHANGE

**Ngày:** 2026-07-01 (UTC+7) · **Loại:** OFFICIAL (MB only, chỉ ảnh hưởng bundle tương lai) · **Rollback:** flag 1-dòng

## Bối cảnh (owner)
Owner xác nhận trực giác lâu nay: "dự đoán ngày trước hay xổ ngày hôm sau, dự đoán miền trước xổ miền sau" → ML có vấn đề lag. Owner duyệt: "MB bền thì xử lý MB luôn vào official, backup + ghi nhận chi tiết, sẵn sàng quay đầu." + hỏi lane test có bị ảnh hưởng không.

## Bằng chứng (milestone × lag grid, causal, bền 2 nửa)
Test nhiều "mốc ảnh chụp dự đoán" (4h same-day, re-predict same-day, các mốc D-1) dự đoán target(D):
- MB same-day ML (cả 04:00 lẫn re-predict) đều yếu/bất ổn.
- Mốc DUY NHẤT dương cả 2 nửa = **MB_Dm1 (ML-plurality của MB HÔM QUA)**: nửa cũ (31d) **+9.4M**, nửa mới (14d) **+6.3M**.
- Vượt official MB cả 2 cửa: MB_Dm1 **+15.7M/45d, +6.3M/14d** vs official MB **+5.9M/45d, +1.4M/14d**.

## MN — KHÔNG xử lý (tránh bẫy)
Các mốc D-1 của MN net dương +45–55M/45d nhưng **100% đến từ nửa cũ**; nửa mới (14d) **LỖ −25M = y hệt bản hiện tại** → đi tới không lời, chỉ là ký ức regime cũ. Deploy = cược regime cũ quay lại. Giữ AI-plurality shadow (V10765).

## Thay đổi kỹ thuật
- `_v10767_mb_prevday_override.py`: `maybe_override_mb()` tính ML-plurality top-2 của MB D-1; champion-challenger log `v10767_mb_prevday_shadow`.
- Inject `main.py::generate_final_bundle` NGAY sau ráp `lo2` (trước `lo3`), **MB ONLY**, gated `_V10767_MB_PREVDAY_ENABLED=True`. Override `bach_thu`+`lo2`; `lo3` tự tính lại từ bach_thu mới. Defensive: lỗi/thiếu data → giữ official.

## Lane test — trả lời owner: KHÔNG ảnh hưởng output
- Lane test hard-contract: KHÔNG gọi `generate_final_bundle`, KHÔNG ghi `final_bundles`/`predictions`.
- Lane test chỉ ĐỌC `final_bundles` làm cột "official baseline" so sánh → sẽ hiển thị MB mới (đúng ý, so sánh trung thực).
- Candidate lane lấy từ `experimental_preview_shadow` (materialize từ `predictions`). V10767 KHÔNG đụng `predictions` (chỉ override output bundle) → candidate lane KHÔNG đổi.

## An toàn / verify VPS
- compile OK; inject confirmed (main.py:9820); module smoke MB→prev-day, MN no-op; health=200; `/du-doan`=200.
- **hash-guard 4 official IDENTICAL** (deploy không regen bundle; áp dụng từ MB 02/07 ~17:42).
- Backup nhiều lớp: `backups/v10767_remote_pre/main.py`, VPS `backups/main.py.v10767_pre.bak`, git history, flag `_V10767_MB_PREVDAY_ENABLED=False`.

## Rủi ro đã nêu
Official MB hiện đã DƯƠNG (tối ưu thêm, không phải cứu hỏa); MB_Dm1 là 1/9 mốc test (multiple-comparison) + cơ chế mới → theo dõi forward sát qua champion-challenger log + V10760; tụt là revert.

## Next action
Theo dõi forward từ 02/07 (FU-V10767): challenger(prev-day) vs champion(official cũ) live. Giữ edge → giữ; tụt → flag False.
