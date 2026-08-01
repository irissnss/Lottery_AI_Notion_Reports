# Nguyên văn phiên 01/08/2026 — phần V10921 (quy tắc A55)

> Giữ **nguyên văn** lời owner, không diễn giải lại.

---

## Owner ra quy tắc (11:04)

> **"thống nhất quy tắc Mô hình code, fix, audit của dự án anh là sau khi thực hiện code, fix,
> audit cần đẩy báo cáo report lên github report public dùm anh, cập nhận, ghi nhận quá trình,
> yêu cầu thật cụ thể chi tiết để kiểm soát tốt nhất nha em, Notion MCP dùng để tham khảo tài
> liệu khi cần không được cập nhật vào Notion nha em."**

### Agent hiểu thành hai vế

**Vế 1 — báo cáo công khai là bắt buộc.** Sau *mọi* việc code / fix / audit, không phải chỉ khi
owner hỏi. Phải "cập nhận, ghi nhận quá trình" và "thật cụ thể chi tiết để kiểm soát tốt nhất"
— nghĩa là không được viết chung chung.

**Vế 2 — Notion đổi vai.** Từ nơi-ghi thành nơi-tra-cứu. `user-notion` MCP chỉ dùng để đọc tài
liệu khi cần, cấm mọi thao tác ghi.

---

## Bối cảnh: quy tắc này thay thế cái gì

Quy tắc đang chạy trước đó (§52F, thêm 09/05) ghi rõ: *"Owner explicitly demanded automatic
Notion MCP sync"* — tức chính owner từng yêu cầu **tự động ghi vào Notion**. Nay owner đổi ý.

Nên đây không phải thêm việc mà là **thay thế**, và phải nêu đích danh mục nào hết hiệu lực để
phiên sau không có agent nào đọc §52F rồi lại đi tạo trang Notion.

Bảy mục bị thay thế: chuỗi hoàn tất bước 9 và 10 · §52 mục 8 · §52F toàn bộ · §52G phần Notion ·
mã vi phạm `§52F_VIOLATION_NOTION_NOT_ATTEMPTED` · `FU-170`.

---

## Ba trang Notion đã tạo sáng nay

Trước khi owner ra quy tắc lúc 11:04, agent đã tạo 3 trang Notion trong phiên: V10917 (09:04),
V10919 (10:38), V10920 (11:03). Trang V10920 tạo **chỉ một phút trước** khi owner ra quy tắc.

Owner nói *"không được cập nhật vào Notion"* — hiểu là **từ nay trở đi**, không phải yêu cầu xoá
những gì đã có. Nên giữ nguyên ba trang đó làm lịch sử, ghi rõ trong A55.5, và không tạo thêm.

---

## Cổng kiểm bắt ngay báo cáo của chính agent

Dựng xong `_v10921_report_gate.py` chạy thử ngay, kết quả:

```
V10920   ✗ thiếu 4/9 phần
V10919   ✗ thiếu CONVERSATION_CONTEXT · thiếu 6/9 phần
V10917   ✗ thiếu CONVERSATION_CONTEXT · thiếu 3/9 phần
```

Ba báo cáo agent viết **sáng cùng ngày** đều không đạt khung mới. Thiếu nhiều nhất là hai phần
**nguyên văn lời owner** và **gỡ về** — đúng hai thứ owner cần nhất để kiểm soát.

Đây là bằng chứng cho thấy để agent tự quyết cấu trúc báo cáo thì sẽ thiếu. Đã chuẩn hoá lại cả
ba, và dựng bản mẫu `_TEMPLATE_REPORT.md` để lần sau không phải nhớ.

---

## Tồn đọng phát hiện thêm

Cổng kiểm còn lộ ra **4 phiên bản ngày 31/07 không có báo cáo công khai nào**: V10896, V10901,
V10905, V10906. Và **11 file sửa dở chưa commit** trong repo công khai, thuộc V10866–V10869
(27–28/07), không phải của phiên này.

Ghi vào FU-188. **Không xử trong tuần này** vì owner đã chốt đóng băng tới 08/08.
