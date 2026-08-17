# CONVERSATION CONTEXT — V11083 · 17/08/2026

## Owner nói gì (NGUYÊN VĂN, kèm giờ)

> **12:54** — *«TẠM DỪNG mọi lane khác — phiên này là lane DUY NHẤT; toàn bộ công sức dồn cho
> hoàn thiện luật. (Các lane đo chạy bằng cron trên server không bị ảnh hưởng — CẤM đụng chúng.)»*

> **12:57** — *«V11077/V11079 theo phương án (a) — CHỈ phiên gốc viết bù từ bản ghi của chính nó
> (RM-17). Nếu không còn truy cập bản ghi gốc → DỪNG mục này, báo owner; CẤM tự chuyển sang soạn
> từ commit message hay nguồn khác.»*

> **17/08** — *«không đẩy báo cáo lên ah để anh còn phân tích đánh giá và ra lệnh xử lý mới em»*

---

## Câu ngắn nhất của phiên này

**Hai cổng đang đỏ, và một trong hai đỏ vì chính bản vá của phiên này.**

Không có câu nào gọn hơn để mô tả buổi làm việc. Sáng vá `K1` cho nó hết mù ⇒ nó lập tức bắt 3
bản thiếu `HISTORY` ⇒ `_v11062` đỏ ⇒ phép RM-15 của chính cổng đó không chạy nổi ⇒ sổ quyết định
đếm thêm một phép trôi. **3 → 4.**

Đó **không phải** hồi quy. Đó là cổng vừa mở mắt và **nhìn thấy thứ vốn vẫn ở đó**. Nhưng nếu
báo cáo chỉ ghi *«đã vá K1, thử chặn ĐẠT»* rồi thôi, thì con số 4 sẽ xuất hiện ở phiên sau như
một bí ẩn.

---

## Thứ tự làm việc — vì sao GĐ-5 chen lên trước GĐ-2

Owner ra thứ tự `GĐ-2 → GĐ-3 → GĐ-4 → GĐ-5`. Phiên này làm **GĐ-5 trước**, và lý do là loại lý
do owner đã dạy: *«cái nào đạp cái nào»*.

Cổng `git commit` đang đỏ vì 3 bản thiếu `HISTORY`. Mỗi commit sau đó đều phải dùng cờ bỏ qua.
Bù xong hai bản được phép bù ⇒ cổng còn đúng **một** mục, và mục đó là mục **owner phải quyết**.
Bỏ qua một lần vì lý do chờ owner thì hợp lệ; bỏ qua bốn lần vì lười dọn thì thành thói quen.

---

## Ba việc phiên này **cố ý KHÔNG làm**

### 1 · `V11080b` — dừng đúng chỗ owner vạch

`K1` bắt ba bản: `V11077`, `V11079` (của phiên này) và `V11080b` (của **phiên khác**).

Hai bản đầu bù được vì phiên này **chính là** phiên đã làm chúng — bản ghi còn nguyên. `V11080b`
thì không: agent này **không có** bản ghi gốc của phiên kia. Soạn từ commit message là **đúng thứ
owner cấm lúc 12:57**, và cũng là `RM-17` (số/việc không tái lập được thì không dùng).

Nên `K1` **vẫn đỏ**, và đỏ **đúng**. Cổng đang chỉ vào một việc thật đang thiếu.

### 2 · K8 — biết đủ để sửa, vẫn không sửa

Điều tra xong thì đã biết chính xác ba cách làm cổng xanh lại. Cả ba đều đụng thứ owner đã ký:
thêm nhãn vào `DONG_STATUSES` (`QD-066` **cấm thẳng**) · đóng hai mục (**cấm thẳng**) · miễn trừ
khỏi K8 (**nới cổng để cổng khỏi kêu**).

`GĐ-4` viết rõ **TRÌNH owner, cấm tự đóng**. Nên bản trình có ba lối kèm *được gì / mất gì*, và
dừng ở đó.

### 3 · Hook `SessionStart` — không cắm

Một subagent trong đợt đào 16/08 đề xuất tự cắm hook `SessionStart` vào `.claude/settings.json`.
Đó là thêm **mã tự chạy mỗi lần mở phiên**. Owner chưa cho phép. Không áp, và nêu lên thành mục
chờ ký.

---

## K8 — điều tra ra thứ ngược với tên gọi «mồ côi»

Tên phép là *«0 mồ côi đến hạn trong 2 ngày tới»*. Nghe như có mục nào đó bị bỏ rơi.

Sự thật: hai mục ấy **được owner cố ý giữ nguyên**, có chữ ký, có lý do ghi rõ trong sổ:

> `FOLLOW_UP_TRACKER.md:236` — *«FU-360 · chặn ghi đè chéo lane: cổng **CHƯA TỪNG chặn thật lần
> nào**; ngày nó gặp va chạm thật là **21/08** khi QD-015/016/017 chạy. **Đóng bây giờ = mất
> người canh đúng ngày đó**»*
>
> `:239` — *«Hai mục này vẫn hiện là **mồ côi** trong briefing; **đó là chủ ý**, không phải lỗi.»*

Sổ **biết**. Cổng **không có cách nào đọc được câu đó**. Nên nó cứ đỏ, và sổ quyết định cứ đếm
`QD-021` là TRÔI — trong khi mã đang làm **đúng** điều owner ký gần nhất.

Và ba chi tiết chỉ lộ ra khi đo, không lộ ra khi đọc:

**① K8 không tự hết.** Chạy `--hom-nay` cho từng ngày: **15/08 ĐẠT → 16/08 TRƯỢT**, và
**21/08 · 22/08 vẫn TRƯỢT** — vì qua hạn rồi thì mồ côi quá hạn cũng làm K8 trượt. Đỏ liên tục
**≥6 ngày**, đúng thứ owner đã cấm khi nói về `CHECKSUMS`.

**② Cổng `RM-19` đang mù.** `_v11034` báo `KIEM_CHEO_QD=SACH`. Nó chỉ so **trong cùng chủ đề** —
`QD-021` (lịch cuốn chiếu) và `QD-066` (đóng băng hai mục) khác chủ đề nên **không bao giờ được
đem ra so với nhau**. Cùng họ với lý do `RM-19` ra đời: bộ kiểm cũ *«chỉ soi quyết định × code,
chưa bao giờ quyết định × quyết định»*. Nay đã soi, nhưng **chỉ trong cùng ô**.

**③ Ngày `18/08` là ngày đọc nhầm nhãn.** Khối gốc ghi **hai** ngày khác nhau: tiêu đề
`hạn 18/08`, thân bảng `| **hạn** | 14/08 |` *(owner ký, `RM-06`)*. Bộ đọc nhận **bốn** nhãn —
`**due**` · `- **Hạn:**` · `**hạn mới**` · `**deadline**` — sổ dùng nhãn **thứ năm** ⇒ rơi xuống
tiêu đề. **Nhưng vá nhãn không cứu được K8**: ngày đúng là `14/08`, còn quá hạn sâu hơn. Ghi ra
vì nó là khuyết tật riêng, **không phải** vì nó là lối thoát.

---

## Một mục lộ ra nhờ chính việc vừa làm

Bộ sinh điều hướng (GĐ-2) vừa dựng xong thì bảng «sắp tới» in ra một dòng phiên này **chưa hề
biết**:

> `FU-348 · KS1708-2 · CỔNG K8 ĐANG XANH GIẢ — MO_COI_TRAN chưa hạ · hạn 17/08`

Ghép với điều tra K8 thì bức tranh mới đủ, và nó **ngược với ấn tượng ban đầu**: K8 **không hề
ngày càng chặt**. Nó từng xanh vì **trần nới gấp 7 lần** ngưỡng `FU-258` **tự khai** (15 thay vì
2). Nay đỏ **không phải** vì chặt hơn — mà vì **một hạn trôi vào** cửa sổ 2 ngày.

Và một con số làm việc của `FU-348` trở nên rẻ bất ngờ: mồ côi toàn sổ nay là **2**, **đúng bằng**
ngưỡng tự khai ⇒ **hạ trần 15 → 2 hôm nay là ĐẠT, không vỡ gì**. Lúc `FU-348` được viết thì con
số là **5** nên hạ trần sẽ làm cổng đỏ thêm.

Đây là lần thứ hai trong một ngày mà **việc dọn dẹp lại đẻ ra phát hiện**: buổi sáng vá `K1` lộ
ra `V11080b`, buổi chiều dựng `NEXT_ACTION` lộ ra `FU-348`.

---

## Sáu vấp của chính agent — và điểm chung của cả sáu

| # | vấp |
|---|---|
| 1 | biến dùng trước khi định nghĩa ⇒ `UnboundLocalError` |
| 2 | khoá sắp xếp ép `V105_60` thành một số ⇒ `V10756_3` **nhảy lên trên** `V11082`; chỉ nhận **248/365** thư mục |
| 3 | `NEXT_ACTION` bản đầu in 12 mục **đều đã `CLOSED`** |
| 4 | cắt danh sách chung ở N mục ⇒ mục đến hạn **ngày mai** không bao giờ hiện |
| 5 | ghi đè `REPORT_INDEX.md` **594 → 385 dòng**, nuốt **38 câu tóm tắt viết tay** |
| 6 | ba luật mới đặt **bốn tiêu đề khác nhau** ⇒ cổng đọc thành **bốn điều riêng** |

**Điểm chung: không vấp nào báo lỗi.** Không cái nào ném exception, không cái nào làm lệnh thoát
khác 0. Cả sáu đều **chạy trơn và ra kết quả trông hợp lệ**.

Bắt được bằng ba việc rất tầm thường: **nhìn output**, **đọc nội dung vừa sinh ra**, và **so số
dòng trước/sau**.

**Vấp 5 đáng nói nhất vì nó gần lọt.** «594 → 385 dòng» đọc như *gọn hơn* — mà bản mới phủ **363**
bản trong khi bản cũ chỉ có ~50, nên «gọn hơn» còn nghe như **tiến bộ**. Chỉ khi hỏi *«594 dòng
kia đựng gì?»* mới thấy **38 câu tóm tắt do người viết**, không suy ra được từ tên thư mục.
Đã khôi phục và thêm bước cất bản viết tay. Cùng tinh thần §63 *«từ chối nếu tệp ngắn đi»*: bản
máy sinh **được phép thay** bản viết tay, **không được phép nuốt** nó.

**Vấp 2 là `RM-10` nguyên bản:** kho có **bốn** họ tên thư mục, agent giả định **một**.

---

## Ba luật mới — vì sao là ba luật này

Không chọn theo cảm giác. Cả ba đều là **lớp lỗi đã tái phạm**, và cả ba đều thuộc loại *«sai mà
không có triệu chứng»*:

| luật | tái phạm ở đâu |
|---|---|
| `PRJ-RETRACTION-001` | *«mất số +0,34pp»* · *«0/105 luật qua cổng»* · *«verdict không ổn định»* — **ba câu, đều do agent viết ra rồi tự phát hiện** |
| `PRJ-SELECTION-WINDOW-001` | `RM-18`: luật hơn nền **+20,7 điểm trong** cửa sổ chọn, **bằng 0 ngoài** |
| `PRJ-PROMPT-COHERENCE-001` | `§60.1`: V11001 gỡ 8 khối rồi báo xong, hôm sau còn **10 chỗ** vẫn dạy model dùng thứ vừa gỡ |

Mang mã `PRJ-` chứ không đánh số `§` mới vì owner **khoá đổi tiền tố `§` tới sau 21/08** — ba
luật này không chờ được.

---

## Trạng thái cuối phiên

Production **không đổi**: không DB · không deploy · không Notion · không chạm đường dự đoán.
`QD-041` nguyên vẹn.

**Hai cổng ĐỎ, cả hai đỏ ĐÚNG:** `_v11062` vì `V11080b` (chờ owner), `_v10920` vì 4 phép trôi
(một phép là hệ quả của bản vá V11082 sáng nay). **Không ghi «mọi cổng xanh»** — đó là câu nói
dối quen thuộc mà `RM-12` sinh ra để chặn.

TanPhatAI cần làm: đọc mục 9 của `REPORT_V11083.md` — quan trọng nhất là **bốn việc chờ owner ký**
(cảnh báo an ninh hook `SessionStart` · 48 bản vá cũ · `V11080b` · K8 chọn A/B/C + `FU-348` hạn
HÔM NAY), và ghi rõ **hai cổng đang đỏ đúng**.
