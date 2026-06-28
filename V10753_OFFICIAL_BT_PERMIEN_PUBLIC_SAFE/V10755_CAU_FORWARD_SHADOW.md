# V10755 — Soi-cầu FORWARD-TEST shadow (top-3 cầu/miền)

**Thời điểm:** 2026-06-28T13:00:00+07:00 · **Owner duyệt:** "lấy top 3 của từng miền, dựng shadow". Sau khi train/test (V10754.1) chứng minh cầu overfit, đây là cách trung thực để xem cầu có giữ được LIVE không.

## Top-3 cầu/miền (locked, station-specific)
- **MN** (nền 43.2%): MN D-1 Vĩnh Long G7.1 [đầu-cuối] 74.4% · MB D-1 Hải Phòng ĐB.1 [last2] 74.4% · MN D-1 Bình Dương G2.1 [đảo-đầu-cuối] 72.1%.
- **MT** (nền 34.9%): MN D Tiền Giang G4.5 [last2] 69% · MN D-1 Trà Vinh G4.5 [đảo-2cuối] 65.1% · MT D-1 Quảng Ngãi G6.1 [last2] 64.3%.
- **MB** (nền 23.9%): MT D-1 TT Huế G4.4 [đảo-2cuối] 43.4% · MN D An Giang G3.1 [đảo-đầu-cuối] 47.6% · MT D Quảng Nam G6.3 [đầu-cuối] 45.2%.

## Sửa lỗi quan trọng (theo owner nhấn mạnh đài)
Cầu gắn ĐÀI chỉ "lên" ~1 lần/tuần → tracker **CHỈ chấm ngày cầu lên** (đài nguồn có xổ), không tính miss ngày không lên. In-sample khớp mining (MN_C1 32/43 = 74.4%).

## Thành phần (SHADOW — KHÔNG feed official)
- Bảng `cau_forward_shadow` (diagnostic_only=1, output_eligible=0) — chỉ đọc kết quả xổ, ghi 1 bảng.
- API admin `/api/admin/cau-forward-shadow` (no-store) — in-sample vs forward + cầu hôm nay.
- Panel "🔭 SOI-CẦU FORWARD-TEST" trên /monitoring (tự refresh 60s).
- Hook materialize sau mỗi closeout (scheduler).

## Verify
diff additive; compile OK; backfill 422 dòng; health 200; endpoint/panel admin-gated (401 cho khách); **4 bảng official IDENTICAL** (shadow riêng). Forward bắt đầu 2026-06-28.

## Lưu ý
Cầu là HYPOTHESIS (in-sample đẹp nhưng train/test sụp). Forward tích lũy ~1 mẫu/tuần/cầu → cần vài tuần-tháng. **Forward ≈ nền → xác nhận overfit, đóng. Forward giữ cao → cầu thật.**
