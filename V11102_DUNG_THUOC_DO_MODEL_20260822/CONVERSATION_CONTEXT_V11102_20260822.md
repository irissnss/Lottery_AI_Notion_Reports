# CONVERSATION CONTEXT — V11102 · 21/08 đêm → 22/08 sáng sớm

## Owner nói gì (NGUYÊN VĂN)

> *«① `FU-420`: `QD-066` THAY `QD-021/027/065` ⇒ 102 mục quá hạn là HỢP LỆ (giữ có chủ đích, không
> phải trễ). KÈM ĐIỀU KIỆN: toàn bộ 102 mục được rà lại MỘT LƯỢT, trình owner MỘT bảng lời thường
> kèm hạn mới từng mục — **hợp lệ không có nghĩa là quên**. ② Ba sửa chữa thước ĐÃ KÝ + bộ chấm
> T-B lên VPS cùng đợt — triển khai sáng sớm 22/08.»*

> *«chứng minh bằng ĐO: chạy lại scorer trên dữ liệu cũ ⇒ 15 model output phải CÓ dòng chấm
> (trước: 0) · lượt trễ bị loại đúng · bảng cộng dồn khớp quét thô.»*

> *«CHỈ rà và trình — CẤM đóng hàng loạt mù.»*

---

## Câu owner ký hay nhất trong prompt này

> *«hợp lệ không có nghĩa là quên»*

Owner công nhận việc giữ 102 mục là **có chủ đích** — nhưng **không cho phép** biến chữ «hợp lệ»
thành cái cớ để chúng nằm đó mãi. Đây đúng là chỗ mà một câu «đã được duyệt» có thể giết cả một
hàng đợi công việc, và owner chặn ngay.

---

## Ba lần agent tự bắt mình sai trong phiên này

### ① Bản vá đầu tiên trộn độ tin cậy của hai lượt khác nhau

`_rr()` bản đầu, khi không tìm thấy bản ghi `official_ai_predict` cho một model output, **lùi về**
lấy bản ghi của lượt `shadow_auto_eval`. Nghĩa là gán độ tin cậy của **một lượt chạy khác** cho
dòng chấm điểm của lượt output.

Đó không phải «thiếu dữ liệu», đó là **dữ liệu sai**. Đã sửa: **vắng thì để vắng**, chỗ đọc đã
chịu được vắng mặt và tự lùi về `predictions.status`.

### ② Bảng rà chỉ phủ 6/11 trạng thái — 31 mục không có hạn

Bản nháp đầu của bảng rà có luật hạn cho 6 trạng thái. Chạy ra thì sổ có **11** trạng thái ⇒ **31
mục** rơi vào ô *«cần owner chỉ»* mà **không có hạn đề xuất**.

Owner yêu cầu *«bảng lời thường kèm hạn mới TỪNG MỤC»*. Một bảng bỏ trống 31/113 mục là **làm nửa
chừng** — đúng thứ `§60.1` cấm. Đã vá, nay **11/11**.

### ③ Bài thử chặn báo TRƯỢT trong khi cổng vẫn đúng

Sau khi khai `QD-071` và gắn `thay_boi`, bài thử chặn của `_v11034` báo **TRƯỢT**. Phản xạ đầu
tiên là đi tìm lỗi trong cổng — **sai hướng**.

Sự thật: bài thử viết lúc va chạm **còn sống**, nên bước [1] chờ *«thoát 1»*. Va chạm nay **đã
được xử thật** ⇒ trạng thái là SẠCH ⇒ [1] ra 0 ⇒ bài thử kêu oan.

> Một bài thử neo vào **trạng thái nhất thời** thì mỗi lần sự thật đổi nó lại báo động giả, rồi sẽ
> có ngày bị ai đó tắt đi — và lúc đó cổng mất luôn bằng chứng nó chặn được.

Bản mới đo **đúng điều cần đo**, không phụ thuộc trạng thái: *gỡ `thay_boi` ra thì cổng có **đỏ
lại** không.*

---

## Hai con số của chính agent phải rút lại

Cả hai công bố trong `REPORT_V11101` **đêm hôm trước**:

| công bố | thật |
|---|---|
| *«8/15 model output có 0 dòng chấm»* | **12/15**. Và 3 model có dòng thì **ngừng từ 01/08**, đúng lúc rời danh sách shadow |
| *«1–12% lượt chạy sau mốc chốt vẫn vào sổ»* | **3,4%** (125/3.669 trong 45 ngày), **toàn bộ** ở shadow MT/MB, **không lượt output nào** |

Con số thứ nhất sai theo hướng **làm nhẹ vấn đề đi** — kết luận không đổi, nhưng vẫn phải rút.
Con số thứ hai là một **dải ước lượng**, không phải phép đo; `RM-17` cấm dùng loại số đó làm căn cứ.

---

## Chỗ dễ tưởng đã xong mà chưa xong

Vá `GĐ-1.2` (chặn lượt trễ) xong thì dễ tưởng là hết chuyện. **Không.**

Khoá bảng là `(ngày, miền, model)`, nên chạy lại chỉ **đè** lên model **còn trong danh bạ**. Model
đã **rời cả hai danh sách** — `gemma-4-31b` 29 dòng, `kimi-k2.5` 22, `deepseek-v4-pro` 22 — thì
**không lượt ghi nào chạm tới nữa**, và dòng rò của chúng **sống mãi trong bảng**.

Tìm ra **334 dòng**, trễ nhất **387 phút** sau mốc chốt.

Để nguyên thì mọi truy vấn về sau phải **nhớ mà lọc**. Cái gì phải nhớ thì sẽ có ngày quên — nên
dọn hẳn, và ghi dấu vết đầy đủ trước khi xoá.

---

## Vấp về công cụ

**`python - <<'PY'` nuốt dấu thoát.** Chuỗi `\\n` trong heredoc thành `\n` thật, cắt một khối
`L.append("` giữa dòng và làm hỏng cú pháp script. Đúng bẫy `CLAUDE.md` đã ghi từ lâu. Đã chuyển
sang **ghi tệp vá** thay vì heredoc — mất thêm một bước nhưng không còn đoán mò về dấu thoát.

**`admin = 404` ở lượt smoke đầu.** Suýt đọc thành «mất xác thực». Thật ra `/api/admin/model-registry`
**không tồn tại**; kiểm lại bằng route admin có thật (`/api/admin/bay-dan-shadow`) ⇒ **401**, quyền
vẫn chặn đúng. Ghi ra đây vì đây là báo động giả rất dễ mắc.

---

## Điều chưa làm xong — ghi thẳng, không giấu

**Chưa kết luận được gì về lượt production ngày 22/08.** Lúc làm việc này là **00:00 giờ VN**, lượt
05:00 còn 5 tiếng nữa. Hai thứ phải đọc lại **sau** lượt đó:

1. prompt có đóng dấu `CTX-18.4` không (bản trên VPS **đã có**, md5 khớp local từng byte — nhưng
   trace mới nhất là **17:48 ngày 21/08**, tức **trước** deploy);
2. job đo có sinh **cả hai họ** không.

`RM-16` nói rõ: mốc phải theo **giờ tạo từng bản ghi**, không theo ngày. **Chưa chạy thì chưa được
kết luận.**

**Chưa vá `FU-422`** — bộ chấm quét lại toàn bộ tệp trace cho **từng** model (≈9.750 lần quét cả
tệp cho một lượt chạy lại 125 ngày). Phát hiện lúc lượt chạy lại **đang chạy dở**: vá giữa chừng
thì tiến trình vẫn dùng mã cũ, khởi động lại thì mất phần đã làm. Vá **sau khi có số**, và vá kèm
phép so **từng con số** chứ không chỉ so tổng số dòng.
