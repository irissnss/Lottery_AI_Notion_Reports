# CONVERSATION CONTEXT — V11028 + V11029 · 2026-08-08

## Owner nói gì (NGUYÊN VĂN)

> Làm tiếp đi kiểm tra lại nội dung quy hoạch rewiter lại 1 bảng đầy đủ nhất toàn vẹn nhất chuản
> chỉnh nhất để sync nhất quán đi nào? FU215 anh nghĩ nên gia hạn thêm để đo đạt kỹ hơn đi em,
> dù gì cũng đã chồng 6 lần rồi, **Nhưng không rõ em còn lưu trữ và nắm rõ các lần em đã làm gì
> chứ?** Làm tiếp cho xong các vấn đề trong tầm tay một cách tỉ mỉ cẩn thận đi

Rồi:

> Đã kiểm tra kỹ quá trình xử lý chưa? đã cập nhật ghi nhận hết chưa?

## Câu «còn lưu trữ và nắm rõ không» — trả lời bằng bằng chứng

**Có.** Sáu lần đổi prompt, mỗi lần có **commit + md5 + bản sao lưu**. Chín bản
`backups/v1xxxx_pre/gpt_analyzer.py.pre` — gỡ về được bất kỳ mốc nào.
Lập thành `docs/SO_SAU_LAN_DOI_PROMPT.md` kèm lệnh tái lập.

## Bốn việc đã làm

| | |
|---|---|
| **QD-041** | gia hạn 08/08 → **21/08**, phạm vi **MỞ RỘNG** thêm `gpt_analyzer.py`. `QD-014` → `SUPERSEDED_BY_QD041` |
| **Bảng quy hoạch sáu mặt** | viết lại vào `CLAUDE.md` + 3 mặt sửa tay, băm `ad4bceb67be60018` giống hệt |
| **A5** | `84/84` → **`80/84`**, đo lại độc lập trên CSV tươi VPS |
| **A6** | M4 dựng lại **tất định**, chạy hai lần ra y hệt |

## Vì sao gia hạn phải MỞ RỘNG phạm vi

Cửa sổ 02→08/08 thất bại **không phải** vì 5 thứ cũ bị đụng — mà vì **prompt đổi sáu lần**.
Gia hạn y như cũ là lặp lại đúng bảy ngày vừa rồi. Nên QD-041 thêm `gpt_analyzer.py` vào danh
sách cấm, và mốc 21/08 chọn trùng ngày chốt FU-284 để **một cửa sổ phục vụ cả ba phép đo**.

**Hệ quả:** A3 (gan/hot còn sót) và A4 (`WEEKDAY SCAN` in dòng lỗi) là **lỗi thật** nhưng
**phải chờ 21/08** — cả hai đổi nội dung prompt. Ghi thành **FU-337 có ngày**.

## Vấp ở đâu — năm chỗ, tất cả do KIỂM mới ra

Owner hỏi *"đã kiểm tra kỹ chưa?"*. Agent chạy bộ kiểm và ra **năm lỗi**, trong đó **bốn do
chính phiên này gây**:

| # | lỗi | ai bắt |
|---|---|---|
| 1 | **`QD-028` đã tồn tại** — suýt ghi đè quyết định cũ của owner (*"N_min = 12"*) | phép kiểm `if any(id==)` trong chính script |
| 2 | **`QD-041` `kiem_code` viết SAI** — `module: "git"` và `module: "gpt_analyzer.PROMPT_VERSIONS"` không nạp được ⇒ sổ báo `TRÔI 2/3`. Số trôi **tăng 4 → 6** | sổ quyết định |
| 3 | **`FU-322` nhãn `ROLLED_BACK`** không có trong `TREO_STATUSES` ⇒ mục thành **mồ côi**, làm cổng K8 của QD-021/QD-022 trượt | sổ quyết định |
| 4 | **`FU-317` hạn 10/08** làm ngày đó **4 mục / trần 3** — mà hạn thật của nó là **21/08** (ngưỡng của chính nó là *"đo tiếp 14 ngày"*) | cổng J5 |
| 5 | **Thiếu `CONVERSATION_CONTEXT_V11028`** — chính tệp này | cổng báo cáo A55 |

**Và một chỗ suýt im lặng:** tệp quản trị dùng **CRLF**, mẫu trong script dùng **LF** ⇒
`str.count()` ra 0 và phép thay **không làm gì mà không báo lỗi**.

## Đã sửa cả năm

| | |
|---|---|
| 1 | đổi sang **`QD-041`** (số kế tiếp thật) |
| 2 | thay bằng **cổng chạy được** `_v11028_cong_dong_bang.py` — kiểm 3 phép: không commit nào đụng `gpt_analyzer.py` · bốn số phiên bản đứng yên · md5 đúng bản khoá |
| 3 | `ROLLED_BACK` → **`CLOSED_PASS`** |
| 4 | `FU-317` hạn 10/08 → **21/08**, gỡ khỏi bảng mốc tải ⇒ 10/08 còn **3** |
| 5 | viết tệp này |

## Điều agent NÓI THẲNG với owner

**1. `z = +10,41` trong bảng M4 KHÔNG phải tin tốt.** Nó nằm ở nhóm `KHONG_XAC_MINH_DUOC` — nhóm
**chấm ngược**, đúng nhóm mà V11024 R2 đo lift **1,084 trong cửa sổ chọn** và **1,000 ngoài**.
Đó là **thiên vị chọn**, không phải kỹ năng. Nhóm `DO_TIEN` hiện **0 dòng local · 15 VPS**.

**2. A5 chỉ sai CON SỐ, không sai KẾT LUẬN.** `80/84` thay `84/84`, nhưng cả 4 khoảng lệch đều
nằm **DƯỚI** 0,50 — phân biệt được nhưng ngược hướng. Doctrine M3 **giữ nguyên**.

**3. Sáu mặt quản trị KHÔNG cần giống nhau** — 7/97 mục giống nhau và đó là **đúng thiết kế**.
Câu cũ trong `CLAUDE.md` *"BỘ ĐỒNG BỘ NĂM FILE"* sai cả **số** lẫn **bản chất**, và dễ khiến
phiên sau đi "sửa cho bằng" rồi **phá mất 79 mục một-bản-duy-nhất**.

**4. Bài học lặp lại lần nữa:** agent báo "xong" rồi mới chạy bộ kiểm và ra **năm lỗi**. Đúng
**RM-12** — `REPORT_PROVEN ≠ CODE_PUSHED ≠ DEPLOYED`. Phải chạy cổng **TRƯỚC** khi nói xong,
không phải sau.
