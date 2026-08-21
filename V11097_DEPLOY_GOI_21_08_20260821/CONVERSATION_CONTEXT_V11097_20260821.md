# CONVERSATION CONTEXT — V11097 · 21/08/2026 tối · ngày mở gói, phần cuối

## Owner nói gì (NGUYÊN VĂN)

> **19:0x** — *«Tới hạn rồi xong chu kỳ theo dõi, chu kỳ xổ số hôm nay rồi. Em tiến hành kiểm
> tra, rà soát tất cả chuẩn bị cho việc xử lý đi nào»*

> **20:0x** — *«deploy chứ chờ gì nữa em?»*

> *«`FU-394` … ⇒ cắt đi»* · *«chưa cắt là đúng vì độ trễ do nhiều yếu tố bới quá nhiều model
> quá mà em»*

> *«toàn là mã ngắn gọn mà bắt duyệt làm sao mà duyệt được duyệt mù ah em.»*

---

## Câu cuối là câu đúng nhất trong ngày hôm nay

Em đưa `FU-416` · `FU-393` kèm một dòng đề xuất rồi hỏi anh gật hay không. Đó là **bắt anh duyệt
mù** — anh không có cách nào biết `FU-416` là chuyện gì, sửa thì được gì mất gì.

Em đã viết lại hai việc đó thành `docs/TRINH_OWNER_FU416_FU393.md`: kể từ đầu, không mã tắt, mỗi
việc có **chuyện gì đang xảy ra · số đo · được gì mất gì · đề xuất và vì sao**.

Và ghi thành ràng buộc trong `QD-069`, để phiên sau không lặp lại.

---

## Rà soát cuối chu kỳ — và nó bắt được lỗi của chính phiên sáng

Sổ quyết định báo **10 phép TRÔI**. Em định lướt qua vì phần lớn trông như chuyện giấy tờ. Nhưng
trong đó có một dòng lạ:

```
QD-044 🔴 ✗ Prompt 3 miền × 2 chế độ KHÔNG còn rác lỗi
       → exit 1: ValueError: too many values to unpack (expected 11)
```

Truy ra: **bản vá `FU-404` sáng nay của em**. Em thêm `lift_365` vào câu `SELECT` ⇒ 12 cột, sửa
**một** chỗ mở gói, **bỏ quên chỗ thứ hai** trong nhánh `shadow_mode=True`.

Hậu quả: `build_context_pack(shadow_mode=True)` tụt còn **106 ký tự** thay vì ~11.000, cả ba miền.

### Và đây mới là phần đáng kể

Mở đúng dòng lỗi ra thì thấy **một chú thích cảnh báo nằm sẵn ngay trên nó**:

> *«V11032: câu SELECT trả **11** cột — bản cũ mở 10 nên ném
> `ValueError: too many values to unpack (expected 10)` suốt **67 ngày**.»*

Tức lỗi này **đã xảy ra một lần**, ẩn 67 ngày, được vá, và người vá đã viết cảnh báo. Em vẫn lặp
lại y hệt, **13 ngày sau**.

Chú thích không cứu được — vì em xuất phát từ **câu `SELECT`**, không xuất phát từ chỗ mở gói.
Em sửa cột thì em nhìn cột; em không có lý do gì để mở cái vòng lặp cách đó 100 dòng.

Đó chính xác là lý do `§61` viết *«nhắc suông đã thất bại, phải thành CỔNG MÁY»*. Em dựng cổng
`_v11096` đếm cột `SELECT` vs số tên ở **mọi** vòng mở gói.

### Lỗi này độc ở chỗ nó không kêu

Nó **không làm sập gì cả**. `build_context_pack` có `try/except`, nên khi vỡ nó trả một chuỗi
ngắn — model vẫn nhận prompt, vẫn trả lời, vẫn ra số. Không lỗi, không cảnh báo, không triệu
chứng. **Chỉ lộ khi đo độ dài.**

Nếu sáng nay em deploy luôn thì nó đã lên máy chủ, và có lẽ nằm đó tới khi ai đó tình cờ chạy
cổng nghiệm thu.

**Quyết định hoãn deploy nửa ngày — vì lý do khác hẳn (tránh ngày lai) — hoá ra cứu đúng chỗ này.**

---

## Chín phép trôi còn lại: không phép nào là code lệch khỏi quyết định anh

**Sáu phép** dò chuỗi `DONG_BANG_QD041=CON_NGUYEN`. Cửa sổ đóng băng **hết hạn đúng hạn hôm nay**
⇒ chuỗi biến mất ⇒ sáu mục báo **TRÔI vì một THÀNH CÔNG**.

Nếu để vậy thì sổ đỏ vĩnh viễn, và đỏ giả **che mất đỏ thật**. Em sửa **cổng trước**: sau khi
cửa sổ đóng, câu hỏi đúng không còn là *«có còn khoá không»* mà là *«cửa sổ đó đã được tôn trọng
trọn vẹn chưa»* — một sự thật lịch sử, không đổi nữa. Đo: **2/56 commit** trong cửa sổ, cả hai
đều được phép.

**`QD-068`** báo *«không thấy trong file»* — nội dung **có thật**, chuỗi dò viết `D3\` — HOÃN`
nhưng bản đồ viết `— **HOÃN,` (in đậm). **Phép kiểm sai, tài liệu không thiếu.**

**`QD-046`** báo *«1 model rớt sàn — MẤT ỨNG VIÊN»*. Model đó là `gemma-4-31b`, **ngừng chạy 23
ngày** và **không nằm trong pool**. Mất một thứ đã mất rồi thì không phải mất.

Đây là **lần thứ hai trong cùng một ngày** một model chết làm đỏ cổng canh model sống — sáng nay
`FU-290A` cũng phải loại `kimi-k2.5`, ngừng **đúng cùng ngày 29/07**.

---

## Ba báo động giả — và cái nguy nhất

Trước khi deploy em kiểm backup có khớp bản VPS không. `rule_engine.py` báo **LỆCH**.

Bỏ ký tự xuống dòng ra: **0 dòng khác**. VPS giữ tệp kiểu **LF**, local kiểu **CRLF**. Kho trên
VPS **trộn hai kiểu** — `main.py` CRLF, `rule_engine.py` LF.

Cái nguy không phải hôm nay. Là **phiên sau**: gặp báo động giả này vài lần thì sẽ kết luận *«cổng
hay báo bậy»* rồi ép ghi đè — và **lần đó ghi đè lên trôi thật**.

Còn `(b) BA BẢN BA ĐƯỜNG — dấu hiệu có người sửa thẳng trên VPS` kêu **hai lần**, cả hai đều là
**bản chưa commit của chính em**. Mọi phiên sửa một tệp đã deploy đều làm nó kêu như vậy.

---

## Một phát hiện thật giữa đám báo động giả

`_v10958_fu_reader.py` trên máy chủ **thiếu hẳn khối `V11065`** — 6 nhãn trạng thái thêm **12/08**
để chống mục rơi khỏi bộ đếm. Bản vá đó **chưa từng được đẩy**. Máy chủ đi sau git **9 ngày**.

Nếu chỉ nhìn `md5` thì kết luận là *«VPS đã trôi, DỪNG»* — dừng oan, và bản vá tiếp tục nằm lại.

Nên em dạy bộ deploy phân biệt hai chuyện vốn nhìn giống hệt nhau:

```
VPS ĐI SAU git   → bản trên VPS là MỘT PHIÊN BẢN CŨ trong lịch sử  → đẩy là ĐÚNG
ai đó sửa VPS    → bản trên VPS KHÔNG khớp phiên bản nào           → đẩy là XOÁ việc người khác
```

Cách phân biệt: dò nội dung VPS với 60 commit gần nhất của chính tệp đó. `_v10958` khớp bản
`6c4d1504` ⇒ **đi sau**, không bị sửa.

---

## Deploy

Hai lượt, 11 tệp. PID `1633166` → `2101247` → `2103185`. `py_compile` **trước** mỗi lần restart.
0 lỗi trong nhật ký. 4 bảng khoá không đổi.

Và nghiệm thu bằng cách **dump prompt trên chính máy chủ**, không tin bản local:

```
CTX-18.4 | dài 18.003 ký tự
  ⚠️ MB(D-1/T5) · Hà Nội: … | READY_WITH_CAUTION | lợi thế +6.7%/nền (n=51)
```

Nhãn mới **đã vào prompt sống**.

---

## `FU-394` — anh nói «cắt đi», và em chứng minh cắt xong không đổi gì

Cắt hai chỗ: `combo_super` bỏ nhánh `×0,3`, `post_filter` bỏ vế thay số.

Nhưng nói *«hành vi không đổi»* thì dễ. Em nạp **bản cũ và bản mới cạnh nhau** trong cùng một
tiến trình, chạy cùng đầu vào thật, so từng đầu ra:

```
post_filter : 0/12 ca lệch
combo_super : 100/100 số khớp TỪNG PHẦN TỬ, cả ba miền
```

Không phải *tin* là không đổi — là **đo ra** không đổi.

Em **giữ lại `_find_replacement()`** dù nay không ai gọi. Nó là một thiết kế đã viết xong; nếu
sau này anh muốn bật cơ chế thay số thì đó là thứ cần dùng. Xoá đi là mất.

---

## Kết quả hôm nay, nói cho đủ

MN `74` · MT `69` · MB `22` — **0/3**. Kỳ vọng từ nền là **1,01/3**, nên một ngày không nói được
gì.

Thước chính **525 miền-ngày**: `+0,52pp`, CI95 `[−3,5 … +4,6]`, `z=+0,25`. Và dấu **đổi theo cửa
sổ**: 30 ngày `+1,85`, 60 ngày `−4,79`, 163 ngày `+0,01`. Trích riêng cửa sổ nào cũng kể được
một câu chuyện khác — nên phải báo cả bộ.

Lane T-B: **111 cặp bất đồng** nhưng chỉ **43 cặp phân biệt**, `z=+0,457`. Với 43 cặp, phép đo
**đã đủ sức thấy chênh 65/35** — và nó thấy **53,5%**. Tức không phải *«thiếu dữ liệu cho mọi
thứ»*, mà là **không có hiệu ứng lớn**.

---

## Điều đáng nghĩ nhất

Hôm nay em vá `FU-341` lần thứ hai. Lần đầu nó ẩn 67 ngày; lần này 13 ngày và bị bắt trong cùng
ngày — **không phải vì em cẩn thận hơn, mà vì có cổng nghiệm thu tồn tại sẵn**.

Chú thích cảnh báo do người trước viết thì em đọc không tới. Cổng máy thì em không tránh được.

Đó là toàn bộ khác biệt giữa hai lần.

TanPhatAI cần làm: đọc mục 9 của `REPORT_V11097.md`, và `docs/TRINH_OWNER_FU416_FU393.md` cho
hai việc đang chờ owner. Nhớ hai điều: **22/08 là ngày sạch đầu tiên của `CTX-18.4`** (mọi phép
đo prompt mới tính từ đó), và **K8 sẽ đỏ từ 22/08 vì `FU-360` — CỐ Ý**.
