# <VERSION> — <tiêu đề ngắn, nói kết quả chứ không nói việc>

**Ngày:** DD/MM/YYYY · **Commit riêng:** `xxxxxxx` · **Commit công khai:** `xxxxxxx` · **Trạng thái:** …

> Bản mẫu bắt buộc theo quy tắc **A55.3** (owner ký 01/08/2026 11:04):
> *"yêu cầu thật cụ thể chi tiết để kiểm soát tốt nhất nha em."*
>
> **Đủ 9 phần dưới đây.** Phần nào không áp dụng thì ghi rõ *"không áp dụng vì …"*, không được
> bỏ trống và không được xoá tiêu đề — cổng kiểm `_v10921_report_gate.py` dò theo tiêu đề.

---

## 1. Tóm tắt

Một đoạn. Làm gì, kết quả gì, con số chính. Người đọc chỉ đọc phần này cũng phải nắm được
chuyện gì đã xảy ra và nó có ý nghĩa gì.

## 2. Owner yêu cầu gì (nguyên văn)

> Trích **nguyên văn** lời owner, không diễn giải lại, không sửa chính tả.

Kèm ngày giờ. Nếu owner chọn phương án qua bảng hỏi thì ghi rõ đã chọn gì.

## 3. Đào bới / phát hiện

Đo bằng cách nào · cỡ mẫu · số liệu thật · công cụ nào sinh ra số đó. Có bảng thì để bảng.
Nêu cả những phép kiểm **không đạt** và vì sao.

## 4. Hướng xử lý và vì sao chọn

Có những phương án nào. Vì sao chọn cái này, vì sao loại cái kia. Nếu owner tự chọn thì ghi rõ
owner chọn, agent chỉ trình.

## 5. Đã làm gì

Bảng `file × thay đổi`. Backup ở đâu. Deploy thế nào (service nào, PID trước/sau). Hash 4 bảng
khoá trước/sau.

## 6. Cổng kiểm

Kiểm những gì, kết quả từng mục, đạt hay trượt. **Không được chỉ ghi "đã kiểm"** — phải có con
số hoặc trạng thái cụ thể.

## 7. Vướng vấp

Mọi chỗ vấp trong phiên, **kể cả vấp do chính agent gây ra**. Mỗi chỗ kèm **hậu quả nếu bỏ qua**.
Đây là phần owner đọc để biết chỗ nào hệ thống còn mong manh — không được giấu.

## 8. Gỡ về

Lệnh cụ thể. Backup nằm ở đâu. Mất bao lâu. Gỡ về rồi thì trạng thái quay lại như thế nào.

## 9. Theo dõi tiếp

Mã `FU-xxx` · **ngưỡng hành động bằng số** (không được ghi "theo dõi thêm" chung chung) ·
hạn rà soát · ai quyết.
