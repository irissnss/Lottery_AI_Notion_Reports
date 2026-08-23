# CONVERSATION CONTEXT — V11106 · 23/08/2026 (tối)

## Owner nói gì (NGUYÊN VĂN)

> *«Live 23/08 đã kết thúc. Owner yêu cầu TỔNG LỰC: đánh giá dự đoán hôm nay, xử lý toàn bộ các
> lỗi đã được ký duyệt (FU-421, 425, 426, dòng chị em FU-419), đọc lane T-B (đã đủ 14 ngày), và
> bắt đầu CHUYỂN HOÁ NGỮ CẢNH NGAY LẬP TỨC (đợt 1). Không dậm chân tại chỗ.»*

> *«BỎ hoàn toàn khối MB MODEL RANKING (chiếm 26,5% prompt MB) — nó đang dạy model tin vào các
> model đã ngừng dự đoán 48 ngày.»*

> *«LUẬT BIÊN REGIME: Mọi quyết định THĂNG cho model MB sẽ đếm lại từ mốc hôm nay (để không lai
> dữ liệu cũ).»*

---

## Hai chỗ trong lệnh của owner mà em phải nói lại

### ① *«đã đủ 14 ngày»* — thật ra **13**

Owner viết lane T-B *«đã đủ 14 ngày»*. Đo trên VPS: mẫu trải **11/08 → 23/08 = 13 ngày**.
`QD-017` đăng ký **14 ngày**. Còn thiếu **một ngày**.

Và điều kiện thứ hai còn xa hơn nhiều: ngưỡng đăng ký là **≥96 cặp lệch kết cục**, hiện có **46**.

**Nên em DỪNG ở bước 2 của giao thức, không đọc.** Đó chính là điều owner khoá ở dòng kỷ luật:
*«CẤM tự ý đổi ngưỡng sau khi thấy số»* — và cách duy nhất để giữ đúng nó là **không đọc khi chưa
đủ**, chứ không phải đọc rồi nói *«nghiêng về…»*.

### ② *«chiếm 26,5% prompt MB»* — thật ra **8,83–10,76%**

Con số 26,5% **lấy từ báo cáo cũ của chính em**, nhưng đó là **TỔNG mọi nội dung thống kê model**
trong gói MB, không phải riêng khối `MB MODEL RANKING`.

Đo lại đúng khối, 7 ngày trên VPS: **1.484–1.667 ký tự = 8,83–10,76%** gói ngữ cảnh MB. Và sau khi
gỡ thật, gói MB giảm **1.540 ký tự = 10,0%** — khớp với dải đo.

**Vẫn đáng gỡ.** Nhưng em không để một con số sai của mình đi tiếp vào báo cáo chỉ vì nó nghe kêu
hơn.

---

## Điều suýt xảy ra ở lane T-B — và nó đáng kể

Bộ chấm tự in ra dòng này:

```
trong đó bất đồng (A≠B) : 122   [ngưỡng QD-059: ≥96]
```

Đọc lướt: **122 ≥ 96 ⇒ đủ mẫu, đọc thôi.**

Sự thật: **122** là số dòng mà **hai DỰ ĐOÁN khác nhau**. Ngưỡng **96** đăng ký cho **cặp lệch
KẾT CỤC** — một bên trúng, bên kia trượt. Con số đó là **46**.

Hai bên đoán số khác nhau 122 lần nhưng **phần lớn cùng trượt**, mà cùng trượt thì **không phân
biệt được ai hơn ai** nên không vào mẫu.

> Cái nguy hiểm không phải con số 122. Là việc bộ chấm **in ngưỡng ngay cạnh nó** — tức nó **mời
> người đọc so hai thứ không so được**. Một dòng chỉ in 122 thì còn phải đi tra ngưỡng; in kèm
> ngưỡng sai vế thì đọc lướt là kết luận.

Đây là họ `RM-21`: **hằng số đo được chỉ đúng cho thước đã đo nó**. → `FU-427`.

---

## Bài thử chặn bắt được hai lỗi trong chính bản vá của em

Bản vá `FU-425` thêm một cờ chéo `LECH_DONG_HO`. Chạy bài thử: **phép [1] và [4] TRƯỢT** — cờ
**không bao giờ đỏ**.

Truy ra hai lỗi, cả hai đúng họ «che tiếng kêu» mà `V11101` vừa dựng cổng để chặn:

1. Hàm dùng `__file__` để tìm tệp trace. Bài thử `exec` thân hàm trong không gian tên không có
   `__file__` ⇒ `NameError`.
2. `except Exception: return None` **nuốt luôn** `NameError` đó ⇒ trả `None` ⇒ đọc thành *«không
   có gì bất thường»*.

**Nếu chỉ chạy xuôi và thấy không có cờ nào**, em đã kết luận *«dữ liệu hiện tại không lệch»* và
giao owner một cái cờ **chết** mà trông như đang canh.

Đã sửa: bỏ phụ thuộc `__file__`, và lỗi nay trả cờ **riêng** `KHONG_DOI_CHIEU_DUOC` — phân biệt rõ
với *«đã đối chiếu và khớp»*.

Rồi khi viết bài thử cho `FU-426`, em đưa hẳn phép **[4] payload hỏng ⇒ phải GHI LÝ DO, không nuốt
im** vào — vì vừa mắc đúng lỗi đó ở bản vá trước.

---

## Một lỗi thao tác, và cách bắt

Bản vá `FU-425` đầu tiên **làm hỏng cú pháp** `scheduler.py`: em neo vào chuỗi
`def _persist_official_diagnostic_empty_row(...` **không kèm phần thụt lề**, mà đó là **hàm lồng
thụt 4 dấu cách** — nên khối chèn vào **giữa dòng**.

`py_compile` báo `IndentationError` ngay. Khôi phục từ backup, và **md5 sau khôi phục khớp VPS
từng byte** — xác nhận không để lại dấu vết nào.

Bài học: `t.count(cu) == 1` **không đủ** để yên tâm. Chuỗi khớp một lần vẫn có thể khớp **giữa
dòng**.

---

## Điều kiện owner đặt cho `FU-421`, trả lời cho đúng

Owner: *«Đo lại phải ra 0 thay đổi trên dữ liệu thật»*.

| lát cắt | Smart Ensemble | Smart ML/Combo |
|---|---:|---:|
| **TOP-2 — lát hệ thống THẬT SỰ đọc** | **0/114** | **0/114** |
| TOP-3 trở đi | 0/114 | **11/114 ĐỔI** |

Trả lời đúng là: **phần được dùng 0 thay đổi**; phần đổi nằm ở top-3 trở đi và **không tới được
đầu ra** vì mã lấy top-2.

Gộp thành *«0 thay đổi»* thì đúng chữ nhưng **giấu mất một nửa** — và nếu sau này ai đọc top-3
cho việc khác, con số gộp sẽ nói dối họ.

---

## Điều em KHÔNG hứa

Gỡ khối `MB MODEL RANKING` **không phải** để tăng độ trúng, và em không hứa thế.

Lý do gỡ là **nó dạy sai**: hai mệnh lệnh bảo model *«output giống model này → tăng confidence»*,
và bảng nó bơm vào lấy `all-time` **không có điều kiện thời gian nào**, nên **model đã nghỉ nhiều
tuần vẫn được nêu tên kèm chữ "historically mạnh nhất"**.

Chưa phép đo nào chứng minh khối này làm giảm độ trúng. Mọi kết luận về độ trúng phải chờ **đo
tiến, có nền, có z** — và theo **luật biên regime** owner ký, dữ liệu MB đếm lại **từ 24/08**.

---

## Điều chưa kết luận được

**Chưa `RUNTIME_PROVEN`.** `CTX-18.6` và bốn bản vá lên máy lúc **20:1x**, sau khi cả ba miền đã
chốt số hôm nay. Lượt production đầu tiên trên bản mới là **05:00 ngày 24/08**. `RM-12` cấm tự
nâng tầng.
