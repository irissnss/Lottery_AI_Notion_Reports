# REPORT V10995 — Tách bundle làm bù bằng view tự suy ra (hướng b)

> **Ngày:** 2026-08-06 · **Quyết định owner:** QD-033 · **Mã việc:** FU-279 (đóng) · FU-280
> **Báo cáo chung cả mạch V10993–V10996:** [`REPORT_V10993_V10996.md`](./REPORT_V10993_V10996.md)

---

## 1. Tóm tắt

Owner chọn hướng (b) trong ba hướng đã trình. Thực hiện bằng **view tự suy ra** thay vì ghi cột vào bảng — và **nêu rõ chỗ chệch khỏi chữ owner nói trước khi làm**.

## 2. Owner yêu cầu gì (nguyên văn)

> *"ok vậy b nha em. làm đi nhưng nó sẽ đúng và có tính lại vẫn không bị sợ sơ xuất nha em"*

## 3. Đào bới / phát hiện

`final_bundles`: **478 dòng = 388 thật + 90 làm bù**, **0 dòng thiếu `created_at`** nên không có ca biên phải xử tay.

Dự án đã có sẵn **54 view** theo lối `v_<tên_bảng>` — nên view là lối quen, không phải sáng tạo mới.

## 4. Hướng xử lý và vì sao chọn

Hướng (b) nguyên văn là *"đánh cờ `is_backfill` vào bảng rồi lọc theo cờ"*. Làm đúng chữ thì vướng **hai chỗ**, cả hai đá vào chính câu owner dặn *"tính lại vẫn không bị sợ sơ xuất"*:

1. **`final_bundles` là một trong bốn bảng khoá.** Thêm cột và ghi giá trị là **đổi mã băm** — phá chính cái cổng đang canh số của owner.
2. **Cờ ghi cứng có thể LỆCH.** Thêm bundle làm bù mới mà quên chạy lại lệnh cập nhật là cờ sai, mà **sai lặng lẽ**.

Nên cờ **tự suy ra lúc đọc**. **Không có đường nào để lệch**, và `final_bundles` **không bị ghi một byte**. Chỗ chệch này đã **nêu với owner trước khi làm**, không làm lén.

## 5. Đã làm gì

`web/backend/_v10995_loc_lam_bu.py`:

| | |
|---|---|
| Quy tắc, **một chỗ duy nhất** | `DIEU_KIEN_THAT = "date(created_at) <= date"` |
| `v_final_bundles_that` | dự đoán THẬT — view mọi phép đo thành tích phải dùng |
| `v_final_bundles_lam_bu` | phần làm bù — **tách ra chứ không giấu đi** |
| cờ `is_lam_bu` | tính sẵn trong view |
| mặc định | **CHỈ KIỂM, không ghi gì**; muốn dựng view phải `--dung` |

Nối vào nhịp canh 14:45: `_v10660` gọi `tu_kiem()` và **kéo cờ đỏ nếu bộ lọc lệch**.

## 6. Cổng kiểm

**Tự kiểm 6 phép:** đủ view · không mất/thừa dòng · không dòng nào ở cả hai view · **tính lại từ quy tắc gốc phải khớp** · cờ đúng · **`final_bundles` không đổi mã băm khi dựng view**.

Hệ thật: `478 = 388 + 90` · tính lại **KHỚP** · **6/6 đạt** · `[cong] LOC_LAM_BU=DAT`. Chạy hai lần liên tiếp vẫn đúng. 4 bảng khoá giữ nguyên hash cả bốn.

Đối chiếu tác dụng — MB Chủ Nhật: `final_bundles` 5/23 = **21,7%** → `v_final_bundles_that` 2/18 = **11,1%**.

## 7. Vướng vấp

**Ba lỗi tự bắt trong phiên:**

1. DB local chưa dựng view → phép tự kiểm trượt → đã dựng view trên local.
2. **Lần thứ hai** mắc cùng lỗi: đặt `chay_lenh` kèm tham số (`--kiem`) trong sổ quyết định → Python coi cả chuỗi là đường dẫn → exit 2. Đã bỏ tham số và **đổi mặc định thành chỉ-kiểm** cho an toàn.
3. Thông báo lỗi **nói sai nguyên nhân** — báo *"1 bản ghi sau giờ xổ"* trong khi thật ra là bộ lọc lệch. Đã sửa thành liệt kê đúng từng lý do.

## 8. Gỡ về

`DROP VIEW v_final_bundles_that; DROP VIEW v_final_bundles_lam_bu;` + xoá `_v10995_loc_lam_bu.py`. Không cần restart. **Không có dữ liệu nào bị ghi nên không có gì để khôi phục.**

## 9. Theo dõi tiếp

**FU-279 ĐÓNG** `CLOSED_PASS`. **FU-280** (14/08) — đổi từng phép đo sang view mới; **chưa làm** vì đổi là đổi số đang hiện trên màn hình.
