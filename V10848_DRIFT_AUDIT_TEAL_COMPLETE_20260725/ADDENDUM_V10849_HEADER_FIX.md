# ADDENDUM V10849 (25/07 22:47→23:1x) — FIX LỖI HEADER UI v2 + PHÂN LOẠI 14 TRANG

Owner báo: khoảng trống trên header · header không ghim · cuộn lọt nội dung qua thanh tìm kiếm · vài trang chưa thấy thay áo · hỏi danh sách 14 trang.

## Root cause + fix (display-only, không backend/restart)

- Shell `theme-v2.css` để `.v2-topbar/.v2-sidebar { sticky; top:28px }` — 28px chừa cho banner "PREVIEW" chỉ có ở bản nháp → production hở 28px trên đỉnh, header không sát top, nội dung cuộn lọt qua khe; topbar nền pha trong suốt.
- Fix: `top:0` + nền đặc `var(--background)` + `z-index:90` + `min-height:100vh`; preview bù bằng `body:has(.v2-mock-banner)`. Re-inline CSS đã fix vào **14/14 trang**; `viewer.html` dời khối theme xuống cuối `<head>` → teal thật (trước bị bộ var trùng tên nội bộ đè).
- Verify: md5 14/14 khớp · header-fix 14/14 · marker đo lường nguyên (warn-strip/sectionMbWhatif/FINAL BUNDLE) · serve 200 · backup `.bak_pre_v10849`.

## Phân loại 14 trang

| Nhóm | Trang | Mức teal |
|---|---|---|
| 4 trang chính (sidebar + topbar) | `/` (`/app`) · `/du-doan` · `/choi` · `/pnl-tracker` | Full shell |
| 5 trang admin | `/login` · `/settings` · `/du-doan-test` · `/review-dashboard` · `/monitoring` | Teal token |
| 5 trang view | `/user-view` (ẩn KPI viewer-safe) · `/accuracy` · `/viewer` (teal từ V10849) | Teal token |
| | **`/search` · `/v82-monitor`** | **CHƯA teal thật** — bảng màu hardcode riêng, cần reskin từng trang trong đợt Plan giao diện owner |

Git private `2df1fc3`. Lưu ý owner: bấm **Ctrl+F5** (hard refresh) vì trình duyệt cache bản HTML cũ.
