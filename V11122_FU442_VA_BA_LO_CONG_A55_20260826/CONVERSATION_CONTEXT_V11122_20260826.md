# CONVERSATION CONTEXT — V11122 · 26/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ là **giờ Việt Nam (UTC+7)**.

## 1 · Owner nói gì — nguyên văn

Prompt 37 mục `IX. P4 — GOVERNANCE`:

> *« 1. Xác minh/vá A55: worklist = `git log ∪ CHANGELOG ∪ report directories`. 2. Chạy cả chế độ
> chỉ định version và toàn dải. 3. Xác nhận hoặc bác `R5` bằng output thật. … 5. Sửa `CLAUDE.md §0`
> đang dạy chế độ mù. … 7. Xác định rõ cổng có được nối vào hook hay không. 8. Nếu chưa nối: giải
> thích; mở decision riêng; **không để `grep=0` im lặng**. »*

Và mục `IV` liệt bảy phép thử bắt buộc, kết bằng: *«có thử chặn hai chiều»*.

## 2 · Agent làm gì

| # | việc | kết quả |
|---|---|---|
| 1 | Preflight `GĐ-0` | bắt **hai lỗi** trong module `V11121` dựng đêm trước |
| 2 | Đọc `_v10921_report_gate.py` (375 dòng) | xác định **ba** lỗ, có neo dòng cho từng lỗ |
| 3 | Chạy **cả hai** chế độ trong cùng một phút | thoát `0` + băng-rôn toàn cục ↔ thoát `1` + 3 bản thiếu |
| 4 | Vá: worklist ba nguồn · bỏ `[:8]` · sắp theo thời gian · băng-rôn theo phạm vi · fail-closed · sổ điểm danh | `py_compile` OK |
| 5 | Chạy toàn dải lần đầu | 🔴 **`424/575` — con số VÔ DỤNG** |
| 6 | Dừng lại, tìm **mốc thi hành thật** | `A55` dựng ở **`V10921`** — chính là tên tệp cổng |
| 7 | Khôi phục **luật hậu tố** | `V11120b` là commit phụ; `V10964b` là bản riêng thật |
| 8 | Chạy lại | **`51/200` · 32 bản thiếu thật** |
| 9 | Viết `_v11122_thu_chan_a55.py` | **11/11 ĐẠT** |
| 10 | Sửa `CLAUDE.md §0` + sinh lại hai mặt | sáu mặt đồng bộ |
| 11 | Kiểm cổng có nối hook không | `grep` = **0 dòng** ở 4 nơi ⇒ mở `FU-444`, **không tự nối** |

## 3 · Vấp ở đâu

### V1 · 🔴 Lần chạy toàn dải đầu tiên cho một con số **vô dụng**

`424/575` trượt. Nếu công bố nó thì mọi người sẽ học cách bỏ qua cổng — đúng bài học chính tệp cổng
đã ghi cho `§62`: *«cổng đỏ vì lý do sai thì người ta sẽ học cách bỏ qua nó, và cổng coi như chết»*.
Phải dừng, tìm mốc thi hành và luật hậu tố, rồi chạy lại.
**Hậu quả nếu bỏ qua:** giết chính cổng vừa vá.

### V2 · Hai lỗi trong module dựng đêm trước — chỉ lộ ra vì tiến trình khởi động lại

`PID 17016` → `18000` với **cùng** `session_id`. Nhánh «cùng phiên» chạy trước phép kiểm PID chết
⇒ lease ghi PID **đã chết** làm chủ. Nếu tiến trình không khởi động lại thì **không ai thấy**.

### V3 · Bộ quét route của agent bỏ sót bản vá của chính mình

Cửa sổ 14 dòng < docstring mới ⇒ báo nhầm *«chưa gắn cổng»*. Quét lại 34 dòng mới đúng.

## 4 · Điều agent **không** làm

| không làm | vì sao |
|---|---|
| Nối cổng A55 vào `cong_git_commit.py` | nối cứng **chặn mọi commit** tới khi bù đủ 32 báo cáo ⇒ quyết định vận hành, mở `FU-444` |
| Bỏ `[:8]` mà không khoá mốc | ⇒ `424/575`, cổng đỏ vì lý do sai |
| Ép luật A55 lên bản trước `V10921` | luật chưa tồn tại lúc đó |
| Đòi báo cáo cho mỗi commit phụ `b`/`c` | báo động giả ⇒ agent sẽ đi chế báo cáo rỗng |

**TanPhatAI cần làm:** con số bản thiếu báo cáo là **32** trên toàn dải từ `V10921`, không phải 10.
