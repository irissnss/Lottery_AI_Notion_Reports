# CONVERSATION CONTEXT — V11061 · 11/08/2026 tối

## Owner nói gì (NGUYÊN VĂN)

Ba lượt, và lượt giữa mới là lượt quan trọng nhất.

> *«Đã hết chu kỳ live hôm nay em tiến hành kiểm tra toàn diện, chi tiết đầu đủ phân tích đánh giá
> việc dự đoán hôm nay không bỏ sót điểm nào, đề xuất xử lý tiếp theo là gì em?»*

> *«đang có vấn đề gì vậy em sao chạy loading hoài tốn token lắm biết không em?»*

> *«Không phải rẻ hay đắt mà anh đã từng gặp em load cả ngày và kết quả là đã đốt hết token và chả
> có 1 xử lý nào thôi nên anh rút kinh nghiệm và nhắc chừng liên tục thà em cập nhật tình hình thì
> anh còn dễ biết em âm thầm quá. Em cứ tiến anh tổng lực kiểm tra toàn diện hôm nay dùm anh đi
> rồi mình tính tiếp»*

---

## Agent đọc sai ý owner ở lượt giữa

Nghe *«tốn token»*, agent đề nghị **làm bản rẻ hơn** — cắt phần phân tích sâu, chỉ kiểm 5 mục,
*«~50k token»*.

Owner bác thẳng: **«Không phải rẻ hay đắt»**. Điều owner cần là **thấy tiến trình**. Nỗi sợ thật
của owner là phiên chạy cả ngày rồi **không ra xử lý nào** — chứ không phải con số token.

Hai cách đọc dẫn tới hai hành động ngược nhau: một bên **thu hẹp việc**, một bên **giữ nguyên việc
và mở miệng ra**. Agent chọn nhầm bên.

Đã ghi thành quy tắc làm việc và thi hành ngay trong phiên này: **báo sau mỗi chặng**, năm chặng,
không gom vào một khối im lặng.

---

## Ngày hôm nay: 1/3, và MT thắng theo cách đáng chú ý

MN `26` trượt · **MT `37` TRÚNG** · MB `73` trượt.

Điều đáng nói không phải con số 1/3 mà là **cơ chế**:

| miền | BT ở hạng | luật thô «nhiều phiếu nhất» chọn gì |
|---|---|---|
| MN | **#1** | `26` — **cùng số**, cũng trượt |
| MT | **#2** | `82` — **cũng TRÚNG** |
| MB | **#2** | `71` — cũng trượt |

**Trọng số hôm nay trung tính.** MT nó bỏ qua số dẫn phiếu để chọn số khác — **cả hai đều trúng**,
nên không chứng minh được trọng số giỏi. MB nó cũng bỏ qua số dẫn phiếu — cả hai đều trượt.

Khác hẳn ngày 10/08, khi trọng số làm mất `19` (số trúng) để chọn `28` (trượt).

**MN không phải lỗi khâu chọn.** Bạch thủ nằm **hạng 1** và luật thô cũng chọn đúng số đó. Hệ chọn
**đúng theo phiếu** — phiếu sai. Đó là khâu SINH.

**MB là ngày pool kém thật.** 22 đuôi ra, pool 18 số mà chỉ **2 số trúng**; bốc ngẫu nhiên 18 số
kỳ vọng ~4. Số trúng tốt nhất nằm **hạng 12**. Không cách chọn nào cứu được.

---

## Việc mới quan trọng nhất: lane A/B sống lại

Hôm qua lượt đầu **hỏng 5/5**. Hôm nay **12 cặp, cả ba miền, 0 lỗi**, trễ 35–154s.

Bốn bản vá sáng nay (khoá DB-trước-env-sau · parse bằng hàm thật của official · timeout theo miền
· huỷ cặp gọi nhầm khoá) **có tác dụng thật**, không phải chỉ chạy được trên giấy.

Tỉ lệ bất đồng **75%** — cao hơn hẳn giả định **40,5%** dùng để tính `N=96`. Nếu giữ nhịp thì đủ
ngưỡng trong **~11 ngày** thay vì 16.

Agent **không đọc ai thắng**. Đó là điều kiện đã đăng ký trước, và bất đồng cao **không** nghĩa là
prompt mới tốt hơn — nó cũng khớp với việc prompt mới trả lời khác đi một cách ngẫu nhiên.

---

## Thứ bộ tự kiểm bắt được, và cái bẫy nằm ngay sau nó

`C20_bien_han_khong_troi` báo LỆCH: MT hai ngày liền biên < 12 phút.

Agent định viết **«biên đang mỏng dần»**. Đo 12 ngày thì **ngược lại**:

```
MT:  11! 11! 16  14  13  15  12   8! 11! 17  12  12
     6 ngày mới TB 13,3  ·  6 ngày trước TB 12,0   →  RỘNG hơn
```

Không có xu hướng xấu đi. **Sự thật khác và nặng hơn: MT ở mức ~13 phút suốt 12 ngày liền, thấp
nhất 8 phút.** Đó là **rủi ro kinh niên chưa ai đo**, không phải sự cố mới.

Và nó nối thẳng vào một mục đang trôi: **`FU-283` hạn 13/08** — *«đổ `latency_seconds` vào bảng +
panel, ngưỡng model TB > 180s»*. `deepseek-reasoner` trễ thật **190–197 giây**. Biên 13 phút,
model chậm 3 phút. **FU-283 không phải việc giấy tờ.**

---

## Ba lần agent tự bắt mình trong một phiên

### 1 · Giấy chứng nhận sạch cấp cho tập rỗng

Agent chạy `journalctl --since "today 00:00" 2>/dev/null` ⇒ **0 dòng** ⇒ suýt ghi *«0 traceback,
0 ERROR, 0 CRITICAL»* vào báo cáo.

Thử lại: `--since today` cho **3.513 dòng**; `--since "today 00:00"` cho **0** và **có báo lỗi**
`Failed to parse timestamp`. Nhưng `2>/dev/null` **nuốt mất tiếng kêu**.

> **Chặn stderr biến một lỗi ồn ào thành số 0 im lặng.**

Cùng khuôn với lỗ cổng báo cáo bắt được sáng nay: một cơ chế **có** phát ra tín hiệu đúng, và
tầng đọc **vứt tín hiệu đó đi**.

### 2 · Báo động giả về sáu script — rút lại trước khi nói ra

Thấy chuỗi kia hỏng, agent quét kho tìm ra **6 script** dùng `--since today`, gồm cả **bộ dò đầu
ngày**, và định báo *«sáu script đã báo 0 lỗi trên tập rỗng bấy lâu»*.

Sai. Chuỗi hỏng là `"today 00:00"` — thứ **agent tự chế**, không script nào dùng. Thử trước khi
báo nên báo động giả **không ra khỏi phiên**.

### 3 · Suýt kết tội báo cáo hôm qua sai 7 tiếng

`CLAUDE.md` §55 cảnh báo `created_at` lưu UTC. Agent thấy `final_bundles` ghi MN chốt `05:24` và
nghi V11057 hôm qua đọc nhầm.

Kiểm ba bảng thì ra **ba quy ước khác nhau**:

```
predictions      2026-08-11T05:00:05+07:00     ISO, CÓ offset
lottery_results  2026-08-11T16:37:37+07:00     ISO, CÓ offset
final_bundles    2026-08-11 05:24:19           naive, KHÔNG offset
```

`final_bundles` là **giờ VN naive**. Chứng minh: MB chốt `17:37`, kết quả MB về `18:31` VN — nếu
17:37 là UTC thì bằng 00:37 hôm sau, tức **chốt sau khi đã xổ**. Vô lý.

**V11057 đúng.** Nhưng lộ ra thứ khác: câu cảnh báo trong `CLAUDE.md` **đúng tinh thần, sai chi
tiết** — và chi tiết mới là thứ gây đọc nhầm.

**Cả ba vấp cùng một khuôn:** tin **một phép đo duy nhất**, không hỏi *«phép đo này có thể hỏng
theo cách nào?»*.

---

## Đề xuất — và vì sao danh sách ngắn

Owner hỏi *«đề xuất xử lý tiếp theo là gì»*. Chỉ có **ba việc**, và không việc nào đụng production:

1. **`FU-283` hạn 13/08** — đo độ trễ từng model. Hôm nay có bằng chứng nó cấp bách hơn tưởng.
2. **Để lane A/B chạy tiếp ~11 ngày** — đang đúng nhịp, can thiệp là hỏng phép đo.
3. **Chờ cron 21:40/21:45** rồi kiểm hai bảng shadow.

**Không đề xuất thêm model / thêm luật / sửa trọng số.** Lý do là số: lợi thế toàn hệ **+0,34pp,
CI95 [−3,8 … +4,5]** trên 164 ngày ⇒ mọi thay đổi dưới **+4,5pp nằm trong nhiễu**. Và hôm nay
trọng số **không hại**. Sửa thứ chưa chứng minh là hỏng thì chỉ thêm chỗ để tin nhầm.

---

## Trạng thái cuối phiên

Production **không đổi**: PID `1353489` · `NRestarts=0` · 4 bảng khoá **số dòng y hệt đầu và cuối
phiên** · `QD-041` nguyên vẹn. Không deploy, không restart.

TanPhatAI cần làm: xem mục cuối `REPORT_V11061.md` — năm việc, quan trọng nhất là ② nối **biên hạn
MT ~13 phút kinh niên** vào **`FU-283` hạn 13/08**, và ③ **đính chính `CLAUDE.md` §55** về ba quy
ước múi giờ khác nhau.
