# CONVERSATION CONTEXT — V11085 · 17/08/2026 tối muộn

## Owner nói gì (NGUYÊN VĂN, kèm giờ)

> **21:16** — *«① `FU-348`: HẠ `MO_COI_TRAN` 15 → 2 NGAY HÔM NAY. Căn cứ đo sẵn: mồ côi hiện
> đúng bằng 2 ⇒ hạ xong K8 vẫn ĐẠT, không vỡ gì.»*

> **21:16** — *«② K8 — LỐI A: miễn trừ CÓ THỜI HẠN cho hai mục `FU-360`/`FU-389`, gắn mã
> `QD-066`, TỰ HẾT 21/08… KHÔNG đóng lén mục nào · KHÔNG sửa `QD-066` · KHÔNG thêm nhãn vào
> `DONG_STATUSES` · Miễn trừ phải tự rơi ra sau 21/08 (không cần ai nhớ gỡ)»*

> *«Luật đã tái phạm 3 lần ⇒ tới ngưỡng "phải dựng cổng, không được chỉ hứa"… Danh sách "đã rút"
> đọc từ MỘT sổ rút-lại duy nhất — CẤM hardcode trong cổng.»*

---

## Phiên này khác các phiên trước ở một chỗ

Owner **không hỏi ý kiến nữa** — owner **ra lệnh**, kèm căn cứ và ràng buộc. Cả hai quyết định
21:16 đều dựa trên số agent trình buổi chiều: *«mồ côi hiện đúng bằng 2»* là con số agent đo,
owner đọc rồi quyết.

Nghĩa là phần việc của agent ở đây **không phải phân tích** mà là **thi hành đúng ràng buộc** —
và ràng buộc của lối A rất chặt: bốn chữ **KHÔNG**, một chữ **PHẢI TỰ RƠI**, một chữ **PHẢI IN
RÕ**. Mỗi cái đều có một cách làm sai tương ứng, nên mỗi cái được biến thành **một phép thử**.

---

## Việc ① — con số nằm chờ 10 ngày mới hạ được

`FU-258` **tự viết** ngưỡng ≤2 mà code để **15**. Nghe như lỗi cẩu thả, nhưng đọc kỹ thì không:
lúc `FU-348` được viết, mồ côi là **5** — hạ ngay sẽ làm cổng **đỏ thêm** trong khi chưa ai xử
được 5 mục đó.

Nên nó nằm lại, và nằm **đúng**. Tới 17/08 mồ côi còn **2** ⇒ hạ về 2 là **ĐẠT ngay, không vỡ
gì**. Owner ký sau khi thấy con số đó.

Bài học nhỏ nhưng đáng ghi: **một mục treo lâu không đồng nghĩa với bị bỏ quên**. Điều kiện để
làm nó rẻ mới vừa xuất hiện.

---

## Việc ② — làm sao để một miễn trừ không thành cửa sau

Miễn trừ là chỗ **dễ hỏng nhất** trong cả bộ cổng: nó tồn tại để làm một phép **thôi kêu**. Nên
mỗi ràng buộc owner đặt được dịch thẳng thành một phép thử:

| owner nói | thi hành | phép thử |
|---|---|---|
| KHÔNG đóng lén | miễn **chỉ** phần (b); hai mục vẫn đếm `2/2`, vẫn in tên | `T5` |
| KHÔNG thêm nhãn vào `DONG_STATUSES` | không đụng | `T6` |
| TỰ HẾT, không cần ai nhớ gỡ | hạn là **hằng số ngày**, so với hôm nay **mỗi lần chạy** | **`T3`** |
| PHẢI IN RÕ mỗi lần chạy | dòng `ⓘ` + nhắc lại trong chi tiết K8 | `T1`, `T4` |

**`T3` là phép quan trọng nhất** và nó đáng nói riêng: giả lập ngày 22/08, miễn trừ phải **tự
rơi** và K8 phải **đỏ lại**. Không có `T3` thì bản vá này chỉ là **một dòng tắt cổng vĩnh viễn
có gắn nhãn cho đẹp** — và không ai phát hiện được điều đó cho tới lúc quá muộn.

`T6` canh một đường hoàn toàn khác: **có thể làm K8 xanh bằng cách lén thêm nhãn vào
`DONG_STATUSES`**. Cách đó `QD-066` cấm thẳng, và nó còn **đóng luôn 6 mục khác** đang mang cùng
nhãn. Một đường tắt vừa sai luật vừa gây thiệt hại lan, nên phải có phép canh riêng.

**Và sau 21/08 K8 sẽ đỏ lại.** Đó là **CỐ Ý** — đã ghi vào sổ theo dõi và vào báo cáo, để phiên
nào gặp cũng biết ngay đó là **lời nhắc**, không phải lỗi mới.

---

## Việc ③ — cổng suýt ra đời trong tình trạng vô dụng

Đây là phần đáng kể nhất của phiên.

Cổng dựng xong, chạy thử trên **8 báo cáo thật** đã push ⇒ **20 báo động giả**. Tất cả đều trên
các báo cáo viết **đúng**.

Ví dụ dòng bị bắt:

```
### 3.3 · Giả thuyết ① «ba miền tụ» — BÁC
```

Chữ **BÁC** nằm ngay trên cùng dòng. Cổng vẫn bắt, vì danh sách từ khoá của agent **thiếu chữ
đó**.

Nghịch lý ở đây đáng suy nghĩ: **viết đúng thì càng bị bắt.** Viết đúng nghĩa là **trích nguyên
văn câu sai rồi bác nó ngay bên cạnh** — mà trích nguyên văn chính là thứ cổng đi tìm.

Nếu đẩy nguyên như vậy thì cổng mới **đỏ ngay từ ngày dựng**, người đọc quen mắt, và ngày nó bắt
được vi phạm thật sẽ **không ai nhìn**. Đúng thứ owner đã cấm ở `CHECKSUMS`: *«đỏ 100% thì tệ
hơn là không có»*.

**Sửa hai chỗ — và một trong hai là sửa SỔ chứ không sửa cổng:**

**Sửa cổng:** thêm phép phân loại **trích dẫn** (`«»`, `""`, `` ` ``, `*`) và **khối ```**. Dấu
trích dẫn là tín hiệu mạnh nhất phân biệt *nhắc tới* với *khẳng định*, và quan trọng hơn: nó
**không phụ thuộc** vào việc danh sách từ khoá có đủ hay không. Danh sách từ khoá sẽ **luôn**
thiếu chữ nào đó — đó là bản chất của `RM-09` (cấm kết luận bằng đếm chuỗi thô).

**Sửa sổ:** dấu hiệu `«CÓ NEO»` **quá rộng** — hai chữ đó nằm trong **chính câu định nghĩa
ngưỡng** (`CÓ NEO ⇔ chênh ≥ +2,5pp VÀ |z| ≥ 2`), nên cổng bắt nhầm báo cáo đang **mô tả phép đo**.
Dấu hiệu phải là **mệnh đề bị rút**, không phải mảnh chữ xuất hiện trong nó. Đã ghi lý do vào
`_ghi_chu_dau_hieu` để phiên sau không đặt lại dấu hiệu kiểu đó.

**Trước sửa: 20 báo động giả. Sau sửa: 0.** Và `T7` được thêm vào bài thử để **canh chính chiều
này** — chống báo động giả cũng phải có phép thử, không thể chỉ sửa rồi tin.

---

## Vì sao danh sách rút-lại BẮT BUỘC nằm ngoài cổng

Owner ra lệnh *«CẤM hardcode»*, và lý do sâu hơn chuyện gọn gàng:

Cổng nào **tự giữ** danh sách thì **sửa danh sách = sửa cổng**, mà sửa cổng thì **phải thử lại
cổng**. Trên thực tế điều đó nghĩa là **không ai thêm mục mới nữa** — và cổng chết dần đúng kiểu
`RM-20` (*«bảng chết là bảng không ai ĐỌC»*), chỉ khác là ở đây nó chết vì không ai **ghi** vào.

Thêm một mục rút lại = **sửa một tệp JSON**. `T4` (sổ rỗng ⇒ cổng không bắt gì) và `T5` (thêm mục
mới ⇒ bắt được ngay) chứng minh điều đó **bằng máy**, không bằng lời hứa.

---

## Việc ④ — một lời hứa của chính agent chưa thực hiện

Báo cáo `V11084` viết *«mở `FU-405`»*. Nhưng khi chạy `_v11044` đầu phiên này thì `FU-405` **vẫn
còn trống** — tức phiên đó **chưa khai** vào sổ theo dõi.

Nghĩa là báo cáo đã hứa một mục theo dõi **không tồn tại**. Không ai phát hiện được nếu không
tình cờ chạy cổng cấp số.

Cùng họ với lỗi mà cả phiên hôm nay đang đi chữa: **nói và làm lệch nhau, và không có cổng nào
soi chỗ lệch đó**.

---

## Hai luật `PRJ` còn lại — hoãn CÓ LÝ DO, không phải quên

`§61` đặt ngưỡng dựng cổng là **tái phạm HAI LẦN**:

```
PRJ-RETRACTION-001    6 ca (3 ca cùng một tuần)  →  ĐÃ DỰNG
PRJ-SELECTION-WINDOW  2 ca                        →  đã chạm ngưỡng, dựng phiên tới
PRJ-PROMPT-COHERENCE  1 ca                        →  chưa tới, chỉ canh
```

**Cổng thừa cũng gây hại như cổng thiếu** — nó chiếm chỗ chú ý mà chưa có bằng chứng cần thiết.
Đã ghi sẵn **cổng sẽ soi gì** cho cả hai vào `FU-406`, để phiên sau không phải nghĩ lại từ đầu.

---

## Trạng thái cuối phiên

Production **không đổi**: không DB · không deploy · không Notion · `QD-041` nguyên vẹn.

**`_v11062` vẫn ĐỎ, và đỏ ĐÚNG** — `V11080b` là bản của **phiên khác**, agent này **không giữ bản
ghi gốc** nên **bị cấm tự bù** theo phương án (a) owner khoá 12:57. Cổng đang chỉ vào một việc
**thật sự đang thiếu**, và nó **chờ chữ ký owner** chứ không chờ agent làm thêm việc.
**Không ghi «mọi cổng xanh».**

TanPhatAI cần làm: đọc mục 9 của `REPORT_V11085.md` — quan trọng nhất là **mốc 22/08** (miễn trừ
tự hết, **K8 đỏ lại là CỐ Ý**) và **cách thêm mục vào `docs/SO_RUT_LAI.json`** (chỉ sửa JSON,
cấm sửa cổng).
