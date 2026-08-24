# CONVERSATION CONTEXT — V11110 · 24/08/2026 (rạng sáng)

## Owner nói gì (NGUYÊN VĂN)

> *«PROMPT TỔNG LỰC LẦN 32 — MASTER WORK PACKAGE … PROMPT NÀY THAY THẾ TOÀN BỘ PROMPT 31 —
> PROMPT 31 = VOID / DO NOT EXECUTE»*

> *«Cấm tự quyết thay model, bật PP5, tắt lớp ghi đè MN, đổi publish gate hoặc timeout.»*

> *«Giữ nguyên các mốc khoa học 30/09 và 06/11 nếu dữ liệu thực sự chưa đủ; cấm "hoàn tất giả".»*

Và giữa phiên, một câu ngắn:

> *«em đã push báo cáo githubs chưa em?»*

**Trả lời thẳng lúc đó: CHƯA.** Kho riêng đã đẩy ba commit; kho công khai mới nhất vẫn là
`V11109`. Câu hỏi đó là lý do bản báo cáo này tồn tại — và nó lôi ra hai thứ em chưa từng kiểm.

---

## Câu hỏi của owner lôi ra một cổng chưa bao giờ tồn tại

Prompt 32 mục `GĐ-12` bắt *«chạy `PUBLIC_REPORT_SAFETY_GATE`»*. Em đi tìm nó. **Không có.**
Tên nghe như một thứ đã dựng từ lâu, nhưng quét toàn kho không tệp nào cài nó.

Nên trước khi đẩy bất cứ gì, em dựng cổng. Và **bản đầu của chính cổng đó mù hoàn toàn với
địa chỉ IP**.

Lý do đáng ghi lại: em viết một danh sách ngoại lệ để khỏi báo giả trên *«số phiên bản»*, trong
đó có dòng tha khuôn `\d+.\d+.\d+.\d+`. **Một địa chỉ IPv4 khớp đúng khuôn đó.** Ngoại lệ nuốt
sạch thứ cổng sinh ra để bắt.

Phép thử `[1]` đỏ ngay lần chạy đầu. Nếu em không viết bài thử — và nhiều cổng trong kho này
từng không có — thì nó sẽ **luôn báo xanh**, y hệt cổng đóng băng từng mù suốt từ lúc dựng.

> **Bài học:** ngoại lệ phải **hẹp hơn** thứ nó tha. Số phiên bản ba thành phần **không bao giờ**
> khớp regex IP, vì regex đòi đủ **bốn** octet — nên nó **không cần** ngoại lệ nào cả.

Sửa xong: **11/11**.

---

## Rồi chạy cổng lên kho công khai đã có — và đây là phần owner cần biết

**1.599 tệp `.md`:**

| loại | số lần | số tệp |
|---|---:|---:|
| địa chỉ máy chủ | **1.137** | **86** |
| đường dẫn tuyệt đối trên máy chủ | **681** | **151** |
| chuỗi đăng nhập `user@host` | **40** | **22** |
| **credential · khoá riêng · chuỗi kết nối CSDL** | **0** | **0** |

**Không khoá nào lộ.** Nhưng đây là kho **công khai** — địa chỉ máy chủ nằm đó nghĩa là bất kỳ
ai cũng biết đúng máy nào đang chạy dịch vụ.

Em **không tự dọn**. Dọn lịch sử một kho công khai là viết lại lịch sử git — thao tác phá huỷ,
và là quyết định của owner. Cổng chặn tệp **mới**; tệp **cũ** chỉ được **báo**.

---

## Điều nặng nhất phiên này: em sai lần thứ ba trên cùng một câu hỏi

Owner hỏi từ mấy phiên trước: *«MN không có bạch thủ 10»*.

| lần | em trả lời | thật ra |
|---|---|---|
| `V11104` | *«MN 22/08 bạch thủ 10 WIN»* | đúng — **nhưng chỉ ở tầng DB** |
| `V11108` | *«bác bỏ ở tầng DB»* rồi rút lại thành *«owner ĐÚNG, chưa bao giờ lên trang»* | một cái **sai tầng**, một cái **sai vì chỉ soi một endpoint** |
| `V11110` | thẻ chính trống **100%**, bảng lịch sử **có** hiện | *(bản này)* |

Làn phản biện tìm ra: trang gọi **ba** endpoint số, không phải một. Endpoint lịch sử **không có
tham số `request`** nên **về mặt vật lý không thể** bị đóng băng, và **không có cổng publish**.
Gọi ẩn danh trên production thì nó **trả về đúng bạch thủ `10`** mà em vừa tuyên là *«chưa bao
giờ lên trang»*.

**Khuôn chung của cả ba lần:** em đo **một lớp** rồi kết luận cho **cả hệ**. `RM-13` nói *«nguồn
sai thì mọi kết luận sai»* — ba lần này **nguồn đều đúng**, nhưng **phạm vi** thì sai. Đó là một
họ lỗi khác, và kho chưa có luật nào cho nó.

---

## Nhưng điều thật sự hỏng thì lớn hơn cả ba lần sai kia cộng lại

Đo tiếp thì ra:

```
Ngày đóng băng viewer = 07/06 ⇒ cả ba miền 14/15, thiếu đúng MỘT model ⇒ CHẶN
Mọi ngày người xem ẩn danh mở được:  qua cổng 0  ·  BỊ CHẶN 372  =  100,0%
```

**Thẻ chính của trang dự đoán trống với mọi người xem ẩn danh, 100% số ngày, suốt 77 ngày.**
Và ngay bên dưới nó, bảng lịch sử hiện dữ liệu hôm nay đầy đủ. **Trang tự mâu thuẫn với chính
nó.**

Điều làm em dừng lại lâu nhất: **không quyết định nào của owner sai khi đứng một mình.**

- Lệnh đóng băng viewer (ký 08/06) nói *«viewer thấy tới 07/06»* — hợp lý.
- Cổng publish đòi đủ 15 model — hợp lý.
- Nhưng cổng áp **roster hôm nay** cho **ngày cũ**, mà một model vào roster **sau** 07/06.

Hai điều đúng chồng lên nhau thành một điều **không ai ký**.

Đây là loại lỗi mà không cổng nào trong kho bắt được, vì mỗi cổng chỉ soi **một** quyết định.

---

## Con số em đưa owner hôm qua cũng phải sửa

Em báo *«nền đang lỗ −90,3tr / 60 ngày»* như một sự thật cố định. Đo lại:

- Tái lập được đúng `−90,3tr` **chỉ ở cửa sổ 61 ngày**. Gọi đúng **60 ngày** hôm nay ra
  **`−89,4tr`** — hàm dùng cửa sổ trượt neo vào thời điểm gọi, **số đổi mỗi ngày**.
- **Hai mô hình tiền trong kho cho kết quả ĐỔI DẤU**: 30 ngày, mô hình đánh phẳng `−30,9tr`;
  mô hình có mức cược `0 / ½ / 1` ra **`+1,9tr`**.
- Nguyên nhân: một bên đếm trúng bằng tập hợp (**tối đa 1 lần/đài**), bên kia đếm **nháy**.
  ⇒ **8–12 điểm phần trăm lỗ là hiện vật của quy ước đếm**, không phải của chiến lược.

**Và điều này KHÔNG gỡ được bế tắc `FU-183`** — thứ sẽ tự nổ ngày 31/08. Cách đọc *«âm tiền»* =
P&L tuyệt đối ⇒ **TẮT** dưới **cả hai** mô hình. Cách đọc = chênh so với phiếu bầu ⇒ **GIỮ**
dưới **cả hai**. **Chọn mô hình tiền không quyết được gì. Chỉ chọn cách đọc mới quyết được.**

---

## Một rủi ro chưa ai nêu, và nó có hạn 30/08

Bộ model **đóng băng 02/08** — cánh tay đối chứng cho phép đo cadence hẹn **06/11** — **chỉ tồn
tại trên một máy**. Không trong git, không bản sao nào. `DOC.txt` của chính nó ghi *«KHÔNG XOÁ.
KHÔNG GHI ĐÈ.»*

Đã kéo bản sao về, **13/13 khớp từng byte**. Rủi ro mất trắng đã gỡ.

Nhưng tầng thứ hai mới đáng lo: `.gitignore` chặn đúng **hai đuôi tệp của hai model đang thiếu**
trong bộ đóng băng. `FU-432` hạn **30/08** yêu cầu chép chúng vào. Ai làm đúng `FU-432` mà chỉ
chép tệp thì **git vẫn lặng lẽ bỏ qua** — và không ai biết cho tới ngày 06/11 khi phép đo thiếu
một nửa.

---

## Điều em KHÔNG làm, và vì sao

**Không sửa một byte nào của production.** Phiên READ-ONLY.

**Không tự chọn ở bất kỳ Decision Gate nào.** `FU-437` có bốn lối, mỗi lối kèm được/mất bằng số
— em trình, owner chọn. Và em ghi rõ hai trong bốn lối **giao với `FU-435`**, nên phải đọc cùng
lúc, đừng quyết hai lần ngược nhau.

**Không dọn kho công khai**, dù vừa đo ra 1.137 lần lộ địa chỉ máy chủ.

**Không đưa 45,6 MB nhị phân vào git** — đó là hình dạng kho, thuộc về owner.

---

## Điều em KHÔNG hứa

Không phép đo nào trong phiên này làm tăng độ trúng, và em không hứa thế.

`FU-437` là mục về **bề mặt hiển thị**, không phải về độ trúng. Sửa nó không làm bộ số đúng hơn
— nó chỉ làm người xem thấy đúng thứ hệ thống đã chọn.

---

## Điều còn treo

**Lượt 05:00 ngày 24/08 chưa xảy ra** khi phiên này khép. `V11106` vẫn `WAIT_LIVE`, chưa
`RUNTIME_PROVEN`. Đợt 2 bảy khối **chưa deploy**, đúng lệnh.

**Bảy làn đo bị phản biện bác 13 kết luận.** Nặng nhất: một làn tuyên bố *«byte đang chạy
production nằm trong git»* — sai ở mức byte, vì cấu hình chuẩn hoá xuống dòng khiến phép so của
git diễn ra **sau khi chuẩn hoá**. Câu đúng hẹp hơn: *«nội dung sau chuẩn hoá được neo; byte thô
thì không»*. Khác biệt này quyết định mọi cổng nghiệm thu khôi phục bằng băm **nói thật hay báo
động giả** — và chính làn đó đã tự mắc rồi tự rút lại một con số vì đúng lý do này.
