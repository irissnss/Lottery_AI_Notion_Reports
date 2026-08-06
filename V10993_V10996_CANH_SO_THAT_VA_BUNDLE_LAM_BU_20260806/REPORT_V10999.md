# REPORT V10999 — Đính chính: đọc sai múi giờ, rủi ro nêu ở V10997 không có thật

> **Ngày:** 2026-08-06 · **Liên quan:** QD-035 · FU-281 (đóng `CANCELLED`)
> **Báo cáo chung:** [`REPORT_V10993_V10996.md`](./REPORT_V10993_V10996.md)

---

## 1. Tóm tắt

V10997 và V10998 ghi một **rủi ro tồn dư không có thật**, do agent đọc giờ UTC tưởng là giờ VN.
Sửa xong thì bức tranh **sạch hơn** chứ không xấu hơn: dời MN sang 15:00 là khung chặn che kín
toàn bộ lượt gọi model, không còn rủi ro nào.

## 2. Owner yêu cầu gì (nguyên văn)

> *"Hết chu kỳ live rồi em tiếp tục đi em ơi, phân tích đánh giá kết quả dự đoán hôm nay dùm
> anh, kế hoạch xử lý tiếp theo là gì?"*

Lỗi lộ ra khi đang phân tích kết quả hôm nay — bảng in `MN 22h` trong khi lúc đó mới 18:34.

## 3. Đào bới / phát hiện

`predictions.created_at` lưu dạng `2026-08-05T05:30:44.669658+07:00` — **có hậu tố múi giờ**.
SQLite `time()` gặp chuỗi ấy thì **tự quy về UTC**:

| Cách đọc | Kết quả |
|---|---|
| `created_at` nguyên bản | `2026-08-05T05:30:44.669658+07:00` |
| `time(created_at)` | `22:30:44` ← **UTC, lệch 7 tiếng** |
| `substr(created_at,12,5)` | `05:30` ← **giờ VN thật** |

Đúng cái bẫy `CLAUDE.md` đã ghi sẵn: *"nhiều bảng lưu `created_at` theo UTC. So sánh với
`time('now','localtime')` là lệch 7 tiếng — lỗi này đã gây báo nhầm nhiều lần."*
Agent đọc tài liệu rồi vẫn sập.

### Giờ VN thật — đo lại bằng cắt chuỗi

| Miền | Giờ VN | Lượt/14 ngày |
|---|---|---|
| MN | **04h · 05h** | 268 · 134 |
| MT | 04h · 05h | 70 · 35 |
| MT | **16h** · 17h | 264 · 8 |
| MB | 05h · **17h** | 7 · 363 |

**Chỉ có HAI cụm:** `04h–05h` (MN sinh số) và `16h–17h` (MT + MB sinh số). Không hề có cụm
nào ở 09h hay 21h giờ VN.

## 4. Hướng xử lý và vì sao chọn

Sửa cả ba nơi đã ghi sai, và **đóng `FU-281` bằng `CANCELLED`** thay vì để nó chạy tiếp — nó
sinh ra để canh một thứ không tồn tại. Giữ lại một mục theo dõi rỗng còn tệ hơn không có, vì
nó tạo cảm giác đang được canh.

## 5. Đã làm gì

Sửa `CHANGELOG` V10997 · `FOLLOW_UP_TRACKER` FU-281 · `OWNER_DECISION_LEDGER` QD-035 `ghi_chu`.
Module `_v10997_khung_gio` đã không còn câu sai từ V10998.

## 6. Cổng kiểm

Sổ quyết định: **không mục nào trôi**. Đối chiếu ba cách đọc cùng một giá trị `created_at` cho
kết quả như bảng mục 3.

## 7. Vướng vấp

Lỗi này **không phải do thiếu tài liệu** — `CLAUDE.md` đã ghi rõ cái bẫy. Nó do agent tin vào
hàm `time()` của SQLite mà không kiểm xem cột đó có hậu tố múi giờ không.

Chỗ khó chịu: **`final_bundles.created_at` KHÔNG có hậu tố** nên `time()` dùng được;
**`predictions.created_at` CÓ hậu tố** nên không. Hai bảng cạnh nhau, hai luật khác nhau — và
agent đã dùng đúng cách cho bảng thứ nhất rồi mang nguyên cách đó sang bảng thứ hai.

## 8. Gỡ về

Không có gì để gỡ — đây là sửa tài liệu, không đụng mã chạy.

## 9. Theo dõi tiếp

**FU-281 → `CANCELLED`.** Rủi ro thật (khoảng 04h–05h chưa được che cho tới khi MN dời) đã nằm
trong **FU-282 · hạn 07/08**.

**Quy tắc mới cần nhớ:** bảng nào có `created_at` kèm hậu tố múi giờ thì **cấm dùng
`time()`/`strftime()` của SQLite** — phải cắt chuỗi `substr(created_at,12,2)`.
