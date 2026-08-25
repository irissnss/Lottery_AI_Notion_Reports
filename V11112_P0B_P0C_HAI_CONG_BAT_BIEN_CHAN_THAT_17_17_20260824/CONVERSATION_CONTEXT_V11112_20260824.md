# CONVERSATION CONTEXT — V11112 · bù ngày 26/08/2026

> ⚠️ **BẢN BÙ.** Việc làm ngày **24/08/2026**; tệp này viết ngày **26/08/2026**.

## 1 · Vì sao có tệp này

`V11112` **không có** thư mục báo cáo công khai — vi phạm `§57.2` tồn tại
**2 ngày** mà không cổng nào thấy, vì cổng A55 chỉ soi **8 bản gần nhất**
(lỗ hổng ②, vá ở `V11122`/`FU-442`).

## 2 · Nguồn dùng để dựng

| nguồn | quy mô | tính chất |
|---|---|---|
| khối `## V11112` trong `CHANGELOG.md` | 3,439 ký tự / 66 dòng | **đương thời** — viết lúc làm việc |
| commit git | 1 commit, ngày 2026-08-24 | **đương thời** |
| lượt owner trong vết phiên `.jsonl` | có | **đương thời** |

## 3 · Nguyên văn lời owner

> *«em đã push báo cáo githubs chưa em?»*
> — owner, **24/08/2026 08:38** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 33 FINAL BẤT BIẾN · OFFICIAL FALLBACK · SỐ PHỤ · XIÊN 2/3 · 3 CÀNG · ADMIN-ONLY · BỘ ĐỐI CHỨNG VPS Đây là prompt thi hành sau V11110, hợp nhất toàn bộ quyết định Owner ngày 24/08 lúc 09:35, 09:49, 09:59 và 10:09. Không được sử dụng lại phương án viewer, P&L, timeout, sản phẩm output hoặc cách tính thành tích cũ đã bị Owner thay thế. ================================================== 0. VAI TRÒ, MỤ…»*
> — owner, **24/08/2026 10:25** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 34 TIẾP NỐI PROMPT 33 — DỰNG FINAL BẤT BIẾN DÁN PROMPT NÀY VÀO ĐÚNG PHIÊN AGENT IDE ĐANG THỰC HIỆN PROMPT 33. Đây là lệnh TIẾP NỐI và sắp lại mức ưu tiên sau bằng chứng runtime ngày 24/08. KHÔNG mở phiên cạnh tranh, KHÔNG làm lại việc GĐ-0/GĐ-1 đã hoàn thành, KHÔNG dừng bốn Algorithm Card đang chạy. Nơi nào trình tự cũ xung đột, ưu tiên P0 FINAL trong prompt này. ==================================…»*
> — owner, **24/08/2026 12:11** (giờ VN)


## 4 · Điều KHÔNG khôi phục được — ghi thẳng, không suy

- **giờ chính xác** từng thao tác trong phiên gốc
- **vướng vấp giữa chừng** — không tài liệu nào ghi lúc đó
- **các phương án đã cân nhắc rồi loại**
- **hash 4 bảng khoá trước/sau** và **PID trước/sau** nếu phiên gốc có chạm DB hoặc restart
- **output cổng kiểm** của phiên gốc — cổng in `stdout`, không ghi tệp (khuyết tật `RM-15`, đã vá
  cho `cong_git_commit.py` ở `V11121` bằng sổ điểm danh)

## 5 · Điều bản bù này **không** làm

| không làm | vì sao |
|---|---|
| Chế lại lời owner | `§62` cấm — thà để trống còn hơn bịa |
| Điền số ước cho hash/PID | `RM-11` — số không tái lập được thì không dùng |
| Sửa khối `CHANGELOG` gốc | nó là bản ghi đương thời, **cấm viết lại lịch sử** |
| Gộp với bản khác | mỗi bản một thư mục riêng, đúng `§57.2` |

**TanPhatAI cần làm:** đọc mục 4 trước khi đối chiếu — bản bù **không** thay được báo cáo viết lúc
làm việc, và những chỗ trống là **cố ý trung thực**, không phải thiếu sót.
