# CONVERSATION CONTEXT — V11060 · 11/08/2026 sáng

## Owner nói gì (NGUYÊN VĂN)

> *«Đầu ngày rồi em em tiến hành kiểm tra toàn diện dùm anh hôm qua giờ em đã cập nhật báo cáo
> đầy đủ chưa em?»*

Một câu hỏi thường lệ. Và nó lôi ra bốn lỗ, trong đó **cái nặng nhất là thứ owner đang đọc mỗi
ngày**.

---

## Lỗ owner suýt không bao giờ biết

Ba tệp `REPORT_V11050/V11051/V11052` mang **đính chính do chính owner ký**: ngưỡng
`FU-284 = 9,53`, ký **18:37 ngày 09/08**, huỷ con số `12,00` mà TanPhatAI ghi nhầm.

Chúng được sửa lúc **09/08 19:12:33**. Và **chưa bao giờ được commit**.

Suốt **2 ngày**, đi qua **5 commit** (V11054 → V11059), bản trên GitHub công khai — thứ owner mở
ra đọc — vẫn hiển thị *«9,53 vs 12,00 — chưa chốt, phải chốt trước 20/08»*.

**Và cổng báo cáo không thể thấy.** Nó hỏi: *tệp có nằm trong `git ls-files` không?* Cả ba **đều
nằm trong đó**. Nó in ra dòng *«file chưa commit: 7»* — tức nó **đã tính được** con số đúng — rồi
**không dùng con số đó** khi kết luận, và in tiếp *«MỌI PHIÊN BẢN ĐỀU CÓ BÁO CÁO ĐẦY ĐỦ VÀ ĐÃ
PUSH»*, thoát 0.

> **«Có trong git» không bằng «bản trong git là bản mới nhất».**

Đúng họ `RM-02`: *«hash bằng nhau chỉ chứng minh KHÔNG GHI BẬY, không chứng minh dữ liệu đúng
thời điểm»*.

Push 3 tệp là xử triệu chứng. Nên vá luôn cổng, và **thử chặn**: sửa một REPORT rồi không commit
⇒ cổng **đỏ**; khôi phục ⇒ **xanh**; tệp về nguyên trạng.

---

## Lỗ agent tự chẩn đoán SAI, và phản biện lật lại

Hôm qua lane A/B chạy lượt đầu 06:00 và **hỏng 5/5**. Agent phân loại:

> *«gemini-2.5-pro nhận 429 RESOURCE_EXHAUSTED «limit: 0» — đây là HẠN MỨC THẬT của nhà cung
> cấp, không phải lỗi mã.»*

Và ghi câu đó vào `REPORT_V11059`, rồi **gỡ model đó khỏi roster**.

Phản biện viên bác. Câu hỏi mà agent **đã không hỏi**: *official gọi đúng model đó lúc 05:17 và
THÀNH CÔNG — vậy nó dùng khoá nào?*

Đọc `main.py:8468-8521` thì ra đường official giải khoá **DB TRƯỚC, env SAU**:

```python
required_key = get_api_key('gemini_api_key') or GEMINI_API_KEY
```

Lane chỉ đọc hằng số cấp module (env). Đo băm:

```
ANTHROPIC  env 0735dcf3 == DB 0735dcf3   trùng — nên không lộ
DEEPSEEK   env 2fb83d77 == DB 2fb83d77   trùng — nên không lộ
GEMINI     env 08614b1c != DB da3deef6   LỆCH
```

Nên:
- `gemini-2.5-pro` 429 là **lỗi cấu hình của lane**, không phải hạn mức. Sửa khoá xong nó chạy
  được **ngay lượt đầu**.
- Nặng hơn: `gemini-2.5-flash` đã gọi bằng **dự án khác hẳn CONTROL**. Cặp đó khác nhau **cả
  prompt lẫn khoá** ⇒ **mất tính một-biến** ⇒ **đã huỷ và chạy lại**.

**Và cổng của chính agent đã nói dối.** `--soi-dinh-tuyen` bản đầu chỉ hỏi *«có khoá không»* và
trả lời **«CÓ»** — cho một khoá **sai**.

> **Cổng xác nhận SỰ TỒN TẠI mà không xác nhận ĐÚNG NGUỒN thì không phải cổng.**

Nay nó so **băm khoá lane vs official**: 5/5 KHỚP.

---

## Hai lỗ còn lại — cùng một khuôn: giả định thay vì đọc

**Lane không parse được.** `_call_*` trả về `{"content": "<chuỗi JSON thô>"}`, không phải dict đã
parse. Agent đọc thẳng `api["prediction"]["numbers"]` — **thứ chưa bao giờ tồn tại**. Nên **3/5
model gọi API THÀNH CÔNG vẫn báo `FAIL_KHONG_CO_SO`**, và agent nhìn mãi chỉ thấy
`{"content": "..."}` trong log vì thông báo lỗi in `api` thô.

Chỉ khi đổi thông báo lỗi để in **khoá của bản ĐÃ PARSE** mới thấy ngay vấn đề.

**Timeout bóp theo miền hẹp nhất.** 120s cho cả ba miền vì cửa sổ MT/MB hẹp — nhưng MN có cửa sổ
**10 tiếng**, và `deepseek-reasoner` trễ thật 190–197s. Tự bỏ mất MN vì lo cho MT.

---

## Một thứ không phải lỗi mà là phát hiện

Sau khi parse được thì lộ ra: **4/4 model chuyển sang dạng `§25`** (`prediction.main_number`)
thay vì `OUTPUT FORMAT` (`prediction.numbers`).

Vì T-B đẩy `§22–§26` xuống T3 nên `§25 MAIN-NUMBER OUTPUT CONTRACT` nằm **sát cuối** — và model
tuân nó **chặt hơn**.

Tức **việc xếp lại khối đã đổi hành vi model thật**. Đó chính là thứ phép đo này sinh ra để phát
hiện, chỉ là nó lộ ra ở **đầu ra** trước khi lộ ra ở **con số**.

Xử lý: **chấp nhận cả hai dạng**, KHÔNG bẻ lại thứ tự prompt — bẻ là thêm một biến nữa vào phép
so vốn đang cố giữ **một biến**. Và dạng `§25` là **hợp đồng chính thức** của prompt, không phải
model bịa.

---

## FU-360 — đóng, nhưng ghi đúng tầng

Đủ 24h canh: **0 dòng, 0 chặn nhầm**. Thử chặn **5/5 + đối chứng LỌT**. Bản vá còn sống. Và
**cả ba miền hôm nay đã chạy dưới cổng** (05:00 giờ VN) — cảnh báo hôm qua *«chỉ MT/MB»* đã
được giải quyết.

Nhưng **không nâng lên `RUNTIME_PROVEN`**: cổng **chưa từng chặn thật lần nào**. Ngày nổ ghi sẵn
là **21/08**. *«0 dòng» là đúng dự kiến, không phải bằng chứng cổng sống* (RM-20) — bằng chứng
cổng sống là **bài thử + đối chứng**.

---

## Điều agent nói thẳng

Bốn lỗ hôm nay có **cùng một khuôn**: agent **đọc đến thư viện rồi dừng**, không soi **người
gọi**.

- Không hỏi *«official dùng khoá nào»* → chẩn đoán sai 429
- Không hỏi *«`_call_*` trả về cái gì»* → parse hỏng
- Không hỏi *«cổng dùng con số nó vừa in ra không»* → cổng mù 2 ngày

Đúng lỗ `§60.2`: **«ai còn trỏ tới thứ này?»** — phải soi cả hai đầu, không chỉ đầu mình đang cầm.

---

## Trạng thái cuối phiên

Production **không đổi** — hash 4 bảng khoá PRE = POST y hệt · PID `1353489` · health 200 ·
`QD-041` nguyên vẹn.

MN 11/08 có **5/5 cặp sạch** trong lane A/B ba tầng. Sổ quyết định còn **1 phép trôi**:
`FU-283` hạn **13/08**, việc thật đang treo.

TanPhatAI cần làm: xem mục cuối `REPORT_V11060.md` — năm việc, quan trọng nhất là ② **đính chính
`REPORT_V11059`** (câu về 429 là sai) và ④ **`FU-283` hạn 13/08 đang trôi**.
