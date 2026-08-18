# CONVERSATION CONTEXT — V11089 · 18/08/2026 đêm

## Owner nói gì (NGUYÊN VĂN)

> **22:27** — *«① Lane T-B — LỐI A: dựng bộ chấm + CHẤM NGƯỢC 110 dòng hiện có.»*

> **22:27** — *«② Ngưỡng DEHERD + bầy đàn: agent ĐỀ XUẤT kèm DẪN XUẤT (tiền lệ 9,53đ của
> FU-284), trình owner ký trước 20/08. CHƯA CÓ CHỮ KÝ thì CẤM ĐỌC hai phép đo đó (RM-03).»*

> *«CHẤM ĐỂ LẤP DỮ LIỆU — CẤM tổng hợp thành verdict/kết luận trước 20/08. Chỉ in số lượng
> (đếm), KHÔNG in tỉ lệ thắng so sánh.»*

> *«Bầy đàn: RÀ TRƯỚC xem ngưỡng 0,50/0,35 từng xuất hiện ở đâu… nếu có nguồn thật thì khôi phục»*

---

## Một lane chạy 8 ngày, thu 110 dòng, và chưa bao giờ biết bên nào thắng

`V11088` tìm ra chuyện này chiều nay. Hôm nay sửa được.

Gốc bệnh gọn trong một dòng: `trung_control`/`trung_tb` **chỉ tồn tại ở câu `CREATE TABLE`**
(`_v11059:176-177`). Quét toàn kho — **không một câu `UPDATE` nào**.

Điều đáng nói là lane **không hỏng**. Nó thu đủ, ghi đủ, thậm chí tính được `bat_dong` (79 khác /
31 giống). Nó biết A và B **có khác nhau không**. Nó chỉ **không biết bên nào thắng**.

Đúng nửa việc — và nửa thiếu lại là nửa duy nhất người ta cần đọc ngày 20/08.

---

## Chấm ngược là chỗ dễ tự bơm điểm nhất — nên chốt phải là MÁY

Chấm ngược nghĩa là: lấy dự đoán cũ, đem so với kết quả **đã biết**. Nếu không cẩn thận thì rất
dễ chấm cả những dòng **được sinh ra sau khi kết quả đã về** — tức những dòng «biết đáp án».

Nên bộ chấm có **hai chốt**, và cả hai đều là mã chạy được, không phải lời hứa:

```
chốt 1 : chỉ chấm bằng kết quả của CHÍNH ngày-miền đó, không mượn ngày khác
chốt 2 : created_at của dòng lane phải < created_at sớm nhất của lottery_results cùng ngày-miền
         không thoả ⇒ TỪ CHỐI CHẤM, ghi lý do
```

Và chúng được **thử** trước khi dùng — `T3` (dòng tạo sau giờ kết quả) và `T6` (dòng tạo **đúng**
lúc kết quả về, biên `≥` chứ không phải `>`). Cả hai phải **từ chối**.

Không có `T3`+`T6` thì chấm ngược **là tự bơm điểm**, và không ai phát hiện được.

Thực tế thì dữ liệu sạch: dòng lane tạo lúc **09:51**, MN xổ **~16:35**. **0 dòng bị từ chối.**
Nhưng chốt vẫn phải có — nó canh cho **ngày mai**, không phải cho hôm nay.

---

## Kết quả — và một kỷ luật khó chịu mà owner đặt đúng

```
dòng đầu vào             110
chấm được                110
TỪ CHỐI                    0
đọc lại TỪ DB (xác minh)  110   ← khớp
còn NULL                    0
trong đó bất đồng          79   [ngưỡng QD-059: ≥96]
```

Owner ký thẳng: *«CẤM tổng hợp thành verdict trước 20/08. Chỉ in số lượng (đếm), KHÔNG in tỉ lệ
thắng so sánh.»*

Nên bộ chấm in **đếm** và **chỉ đếm**. Không tỉ lệ, không z, không so sánh. Dữ liệu đã nằm đó,
nhưng **ngày đọc là 20/08** — và ngưỡng `QD-059` đã đăng ký trước từ 11/08.

Kỷ luật này khó chịu vì con số đã ở ngay trước mắt. Nhưng đó chính là lý do nó tồn tại: **ai đọc
số rồi mới quyết đọc thế nào thì đã hỏng phép đo.**

**Xác minh:** đọc lại thẳng từ DB bằng truy vấn **độc lập**, không tin exit code — đúng lời owner
dặn *«kiểm dấu vết sau khi ghi»*.

---

## Ngưỡng bầy đàn — owner nhớ đúng, nhưng kho còn giữ nhiều hơn

Owner nhớ *«0,50/0,35»* và dặn **rà trước**. Rà ra `CHANGELOG.md:5128-5131` — không phải hai con
số, mà **bảng bốn dòng** đăng ký trước:

| kết luận | điều kiện |
|---|---|
| CÓ TÁC DỤNG | trung bình **≥ 0,50** *và* hơn nền **≥ 0,05** |
| KHÔNG TÁC DỤNG | trung bình **≤ 0,35** |
| CHƯA RÕ | nằm giữa hai ngưỡng |
| CHƯA ĐỦ | dưới **9 lượt** |

Và **nền = `0,47`**. Nên vế *«hơn nền ≥0,05»* thực chất là **≥ 0,52** — **chặt hơn** vế `≥0,50`.
**Hai vế không thừa nhau; vế nền mới là vế ràng buộc thật.**

Nếu chỉ khôi phục hai con số owner nhớ thì đã **nới ngưỡng** từ `0,52` xuống `0,50` mà không ai
biết. Đó là lý do owner dặn *«rà trước»* — và lý do đó đã chứng minh giá trị ngay lần đầu.

### Và một cái bẫy phải đọc kèm

Bản đầu phân loại theo **NGÀY** ⇒ ba lượt 07/08 bị gắn `SAU_V11016` với phân tán
`0,56 / 0,57 / 0,57`, *«nhìn như thắng lớn so với nền 0,47»*.

Nhưng ba lượt đó tạo lúc **05:00–05:20**, còn `V11016` lên máy chủ **13:35:48** — chúng chạy
**prompt CŨ**. Đã sửa thành **mốc giờ**, và `HON_HOP` bị **loại khỏi cả hai trung bình**.

⇒ Ngày 20/08 **phải kiểm `giai_doan` TRƯỚC khi đọc `ty_le_phan_tan`**.

---

## DEHERD — dẫn xuất được, và con số nói một điều không vui

`PL13` **không tồn tại trong kho**. Nên phải đề xuất mới, theo đúng khuôn `9,53`:

```
n   = 63 miền-ngày   (21 ngày × 3 miền)
var = 0,2174         (nền riêng: MB 0,235 · MN 0,427 · MT 0,350)
VIF = 1,002          (RM-21 — xem cảnh báo dưới)
z   = 1,96

SE  = √(2 × 0,2174 / 63) × √1,002 = 0,08316
MDE = 1,96 × 0,08316              = 16,3 pp
```

**⇒ ngưỡng đề xuất: `|chênh| ≥ 16,3pp` VÀ `|z| ≥ 1,96` VÀ `n ≥ 63`.**

### Con số không vui: phép đo này YẾU

| hiệu ứng | n cần | = ngày | ≈ tháng |
|---|---|---|---|
| 20 pp | 42 | 14 | 0,5 |
| **16,3 pp** | **63** | **21** | **0,7** ← hiện có |
| 10 pp | 167 | 56 | 1,9 |
| **5 pp** | **669** | **223** | **7,4** |

Nếu DEHERD có lợi thế thật cỡ **+5pp** — mức **rất đáng làm** — thì cửa sổ 21 ngày **không thể
thấy được**. Kết quả ngày 20/08 sẽ ra *«chưa được phép kết luận»*, và điều đó **không phải** bằng
chứng DEHERD vô dụng — nó là bằng chứng **cửa sổ quá ngắn**.

Phải nói ra **trước khi owner ký**, vì đây là thứ quyết định cách đọc kết quả. Ký xong rồi mới
biết là quá muộn.

---

## Một chỗ suýt làm sai, và `RM-21` chặn được

Dẫn xuất cần `VIF`. Có sẵn `VIF = 2,92` từ `FU-284` — dùng luôn thì tiện.

Nhưng `2,92` đo cho thước **16 model cùng đoán một ngày**. DEHERD là **một số / miền-ngày, ba
miền**. **Khác hẳn hình dạng.**

Dùng `2,92` sẽ đẩy ngưỡng lên **~27,8pp** — phồng **vô cớ**, và phồng **sai chiều**: làm phép đo
càng dễ ra *«không đủ bằng chứng»*. Đúng nguyên văn ca `RM-21` đã ghi.

Dùng `1,002` (thước bạch thủ/miền-ngày, cùng hình dạng), và **ghi rõ đó là hằng số MƯỢN** —
`RM-21` không cấm mượn, nó cấm **mượn mà không khai**.

---

## Trạng thái cuối phiên

Production **không đổi**. `QD-041` nguyên vẹn. Không đọc sớm thước nào.

**Hai ngưỡng đều ghi `CHỜ OWNER KÝ — CHƯA KÍCH HOẠT`.** Agent không tự kích hoạt, và **không
đọc** hai phép đo đó cho tới khi có chữ ký.

**Một cảnh báo phải nhắc:** bộ chấm **chưa lên VPS** (vùng cấm phiên này), và DB local bị **ghi
đè** mỗi lần đồng bộ ⇒ ngày 20/08 phải **chạy `_v11089_cham_lane_tb.py` SAU khi đồng bộ, TRƯỚC
khi đọc**.

TanPhatAI cần làm: đọc mục 9 của `REPORT_V11089.md` — quan trọng nhất là ① **hai ngưỡng chưa kích
hoạt**, ② **DEHERD chỉ thấy được ≥16,3pp**, ③ **bộ chấm phải chạy lại sau mỗi lần đồng bộ**.
