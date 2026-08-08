# CONVERSATION CONTEXT — V11032 · 2026-08-08

## Owner nói gì (NGUYÊN VĂN)

> 1/ (a) mở khoá vá ngay
> 2/ chưa rõ là vấn đề gì cần diễn giải cụ thể
> 3/ giữ hạn

Ba câu trả lời cho ba câu agent hỏi ở báo cáo V11031 (FU-341 · FU-343 · FU-344).

## Agent làm gì

| câu | làm gì |
|---|---|
| **1** | Vá **ba chỗ** trong `gpt_analyzer.py`, dựng cổng nghiệm thu, deploy VPS, so PID, băm 4 bảng khoá |
| **2** | Dựng **bộ kiểm quyết định × quyết định** đầu tiên của kho + diễn giải bằng bảng ba mảnh giấy |
| **3** | Viết `_v11033_verdict_fu284.py`, ngưỡng **9,33 điểm** ghi bằng số **trong tệp**, commit **trước** ngày chốt |

## Vì sao vá BA chỗ chứ không một

Ba chỗ là **ba lớp của cùng một lỗi**:

```
GỐC   :4761   mở 10 biến cho rules 11 cột            → hỏng
CÂM   :5576   except nuốt lỗi, không in gì            → không ai nghe thấy
MÙ    :6271   cổng canh len > 50, chuỗi lỗi dài 64    → không ai bắt được
```

Vá mình **GỐC** thì lần vỡ **SAU** vẫn câm y hệt — và sẽ lại mất 67 ngày nữa mới có người thấy.
Vá mình **MÙ** thì lỗi vẫn còn. §60 gọi đây là *"cấm bỏ nửa chừng"*.

## Bằng chứng TRƯỚC / SAU — chạy hàm production thật

```
TRƯỚC:  MN shadow=True      64 ký tự   MB shadow=True      64 ký tự
SAU  :  MN shadow=True  13.199 ký tự   MB shadow=True  12.775 ký tự
```

Trên VPS sau deploy: **6/6 ô đạt**, `VA_V11032=DAT`.
PID `1004216 → 1044843` · health **200** · 4 bảng khoá **PRE = POST y hệt** · **0 lỗi** journal.

## ⚠ Điều agent PHẢI báo ngay: chính cổng nghiệm thu lôi ra một lỗi RỘNG HƠN

`⚠️ SP-4.0 scan error: no such column: predicted_numbers` có mặt ở **cả 6 ô** — kể cả
`shadow_mode=False`.

| | FU-341 (vừa vá) | A4 / FU-345 (chưa vá) |
|---|---|---|
| model dính | **1** — `gpt-oss-120b` | **cả 15 official** |
| tần suất | 42,9% số lượt | **mọi miền, mọi ngày** |
| chế độ | chỉ shadow | **cả hai** |

**Agent KHÔNG vá.** `QD-042` chỉ mở khoá cho FU-341, và chính nó ghi ở dòng `khong_duoc`:
*"cấm dùng QD-042 làm cớ mở khoá cho lần sửa SAU"*. Tự nới chữ ký của owner là việc agent
không được làm — dù lỗi đã rõ mười mươi. Đây đúng **RM-07**: vá một lỗi không phải vá cả họ lỗi,
nhưng **phải rà và phải khai**.

## Vấp ở đâu

| # | vấp | sửa |
|---|---|---|
| 1 | Neo vá `PROMPT_VERSIONS = {` khớp **2 lần** | đổi neo sang `RUNTIME_PROMPT_VERSIONS = {` |
| 2 | `assert CTX_PACK_LOI == 3` sai — thật ra **4** (1 định nghĩa + 1 chỗ trả + **2** ở cổng canh) | sửa số |
| 3 | Bộ kiểm quyết định bắt **thừa** QD-020/021/022 (giãn hạn, chỉ *nhắc tới* đóng băng) | thắt từ khoá — **RM-09** |
| 4 | Thắt xong lại bắt **sót** QD-029 (owner nói gọn *"mở nha em"*) | đọc `ghi_chu` nhưng **bỏ từng CÂU nhắc mã khác** |
| 5 | Nạp `gpt_analyzer` mất ~7 phút + in hàng trăm dòng, kết quả trôi mất | cổng nghiệm thu **nuốt stdout** khi nạp và khi gọi |

Vấp 1 và 2 **dừng trước khi ghi** nhờ `assert` đặt **trước** `os.replace` — tệp không hỏng lần nào.
Vấp 3 và 4 là bài học ngược nhau: **đổi báo-thừa lấy báo-sót là tệ hơn**, vì một cổng báo sót
là cổng **không tồn tại**.

## Câu 2 — diễn giải cho owner

Ba mảnh giấy dán trên cùng một cái tủ lạnh, không mảnh nào bị gỡ xuống:

| ngày | mã | owner nói | chiều | trong sổ |
|---|---|---|---|---|
| 01/08 | `OD-20260801-D` | *"Chờ ít nhất 7 ngày… rồi mới động tiếp"* | **ĐÓNG** | `ACTIVE` |
| 05/08 | `QD-029` | *"vướng mắc 2: **mở** nha em"* | **MỞ** | `ACTIVE` |
| 08/08 | `QD-041` | *"gia hạn thêm để đo đạt kỹ hơn"* | **ĐÓNG** | `ACTIVE` |

**Owner ký đúng ở từng thời điểm.** Sai ở chỗ **sổ không ghi mảnh nào đã bị mảnh nào thay** —
lược đồ có 34 trường mà **không trường nào** là `thay_boi`.

**Và nó đã gây hại thật:** cả **sáu** lần đổi prompt (V11001…V11022) đều diễn ra **SAU** khi
`QD-029` mở khoá ⇒ trên giấy đều hợp lệ. Chính sáu lần đó phá hỏng cửa sổ đo và buộc phải ký
`QD-041`. Nếu sổ nói được *"QD-029 thay OD-D, và nó mở đúng những gì"* thì *"đổi sáu lần trong
một cửa sổ mở"* đã lộ ra sớm hơn nhiều.

## Câu 3 — giữ hạn thì ngưỡng phải đổi

Ngưỡng cũ *"tụt ≥5 điểm"* cần **44–50 ngày**. Cửa sổ 14 ngày chỉ thấy được **≥9,33 điểm**.
**Không giữ được cả hai.** Owner giữ hạn ⇒ ngưỡng nâng lên đúng sức cửa sổ, và **ghi bằng số
trong tệp, commit trước ngày chốt** (RM-03: chọn định nghĩa sau khi đã thấy số là gian lận).

Điều phải nói trước: nếu 21/08 ra chênh nhỏ hơn 9,33 thì kết luận đúng là **"chưa được phép kết
luận"** — **KHÔNG phải** *"prompt mới không khác gì"*. Hai câu đó khác hẳn nhau.
