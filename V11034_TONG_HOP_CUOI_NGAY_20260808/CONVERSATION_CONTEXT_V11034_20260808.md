# CONVERSATION CONTEXT — V11034 · 2026-08-08 tối

## Owner nói gì (NGUYÊN VĂN)

> Hết chu kỳ live rồi em kiểm tra phân tích đánh giá dự đoán hôm nay dùm anh nha em, sau đó
> tổng hợp đầy đủ và đề xuất xử lý tiếp dùm anh nhé em

## Agent làm gì

Cổng tuổi dữ liệu **CHẶN** ngay (local cũ 10,11 giờ). Đồng bộ lúc 18:34 **thất bại**
(«database is locked»), lượt **18:39:07 thành công**. Trong lúc chưa đồng bộ được thì **đo
thẳng trên VPS** — tươi hơn bản sao. 19 agent soi + phản biện đối kháng.

## Việc quan trọng nhất phiên này: AGENT TỰ ĐÍNH CHÍNH LỜI MÌNH

Lúc 18:40 agent báo với owner:

> *"MN chạy prompt HỎNG được 68,8%, MB chạy prompt ĐÃ VÁ được 6,2%"*

và dựng cả một lập luận quanh đó. **Tiền đề ấy SAI.**

Bóc 12 lượt mang gói ngữ cảnh 64 ký tự ngày 08/08:

| | |
|---|---|
| **11/12 là SHADOW** | `run_source='shadow_auto_eval'`, 05:33–05:41 — **bị loại khỏi 16 lượt chấm** |
| **1 lượt official** | `gpt-oss-120b` MN 05:17:21 |
| **7/8 model TOKEN official của MN** | gói **8.797 ký tự** — nền MN 7 ngày trước 8.307–9.009 ⇒ **nằm giữa dải bình thường** |

**MN official chạy prompt CHƯA VÁ nhưng LÀNH**, không phải prompt hỏng. Hai chuyện khác hẳn.

**Lỗi gốc của agent: QUÊN LỌC `run_source`.** Đúng cái bẫy sổ RM đã ghi nhiều lần. Agent đếm
12 lượt 64 ký tự rồi gán cho MN mà không hỏi 12 lượt đó có thuộc đường chính thức không.

**Và sâu hơn:** phơi nhiễm **không phải biến theo MIỀN, mà theo MODEL**. Quét 25/07–08/08,
model official duy nhất từng dính là `gpt-oss-120b`, **8 ngày rải đều cả ba miền**. Chia nhóm
theo miền là **sai hai tầng**: sai nhãn, sai cả trục biến.

## Năm lớp bác bỏ cái bẫy «vá xong tệ hơn»

| lớp | nội dung |
|---|---|
| 1 | **nhãn sai** — MN official chạy prompt lành ⇒ phép so mất hiệu lực ở tầng cơ bản nhất |
| 2 | **nền** — chênh MN−MB 62,5 điểm thì 28,0 là do nền; còn 34,5, vẫn dưới ngưỡng 84,6 |
| 3 | **tự huỷ** — hai miền ĐÃ VÁ nằm hai cực (MT +42,7 · MB −25,0), **ôm trọn** miền chưa vá (+9,5). Nếu bản vá gây ra 0/8 của MB thì chính nó phải gây ra 6/7 của MT |
| 4 | **đối chứng âm** — nhóm ML không đọc prompt cũng trải 65 điểm trong cùng ngày |
| 5 | **tiền lệ** — MB 6,2% đã xảy ra **đúng mức đó** ngày 04/08 và 06/08, **cùng bộ 16 model, cả hai TRƯỚC bản vá** |

Lớp 3 là lập luận **logic**, không phụ thuộc cỡ mẫu — đứng vững kể cả khi mọi số thống kê khác
bị bác.

## Ba cạm bẫy thống kê tìm ra

**1. `n = 16` là con số ẢO.** Model xúm nhau chọn cùng số: MN 16 model chỉ ra **8** số bạch thủ
khác nhau · MT 15 ra **7** · MB 16 ra **7**. **n hiệu dụng thật 4,8 – 6,1.**

**2. MB ở cỡ mẫu này VỀ CẤU TRÚC là không thể kiểm được.** Ngưỡng bác bỏ chiều giảm ở n=16 là
**p ≤ −11,3%** — tức **dù hôm nay MB có 0/16 thì cũng KHÔNG BAO GIỜ đạt ý nghĩa thống kê**.
Nói "MB tệ" vô căn cứ ở mức **mạnh hơn cả** "thiếu bằng chứng".

**3. Ba model là BẢN SAO TẤT ĐỊNH.** `combo-no-token` · `smart-ml` · `smart-ensemble` là hàm
của 4 bộ sinh kia. Đếm "7 model NO_TOKEN" là **đếm trùng**. Ví dụ MB: đếm thô 1/7 = 14,3%
(nghe như hỏng) — đếm đúng **1/4 = 25,0% = ĐÚNG BẰNG NỀN**.

## Phát hiện quý nhất: MN hỏng ở XẾP HẠNG, không phải ở SINH

Top-10 MN có **9/10 số trúng**, kỳ vọng theo nền chỉ **5,3**. Bạch thủ trượt **đúng một bậc**:
hạng 1 số 69 (**4 phiếu** · 0,1184 điểm) trượt, hạng 2 số **43** (**5 phiếu** · 0,1037) TRÚNG.
**Số nhiều phiếu hơn lại xếp dưới.**

Nhưng **n = 1 ngày** — agent mở FU-351 với ngưỡng rõ: cần **≥30 ngày**, và **≥40% số ngày** có
«BT trượt nhưng top-3 trúng» mới đủ căn cứ mở bàn sửa.

## Lỗi thật hôm nay

`deepseek-reasoner` miền MT: `Expecting value: line 7 column 18`, chạy **230,3 giây**, trả về
`[]`. **API CÓ trả lời** — không timeout, không API chết. **Lặp hai ngày liên tiếp 07/08 và
08/08.** 30 ngày: 3/90 lượt rỗng, riêng MT **6,7%**.

**Cổng canh việc này đã viết từ hôm qua nhưng CHƯA DEPLOY** — quét toàn ổ VPS ra 0 kết quả,
không cron, không ghi dòng nào. Sổ ghi `DEPLOYED_PENDING_LIVE_VERIFY` là **SAI TẦNG** (RM-12);
tầng thật là `CODE_PUSHED`.

## Điều agent NÓI THẲNG với owner

**1. Agent đã báo sai một lần trong chính phiên này** và tự bắt được nhờ phản biện. Ghi ra đây
để owner biết mức tin cậy, không giấu.

**2. Hôm nay KHÔNG có miền nào được phép gọi là tốt hay tệ.** Chênh quan sát (10,3–18,8 điểm)
thấp hơn ngưỡng đọc được (45,8–51,5 điểm) **từ ba đến năm lần**.

**3. Đừng đụng bộ xếp hạng vì một ngày.** Phát hiện MN rất đáng đào, nhưng n=1. Và nó thuộc bộ
chọn số ⇒ **QD-041 khoá tới 21/08**. Trong cửa sổ này **chỉ được ĐO**.

**4. Việc duy nhất đáng làm sớm là deploy cổng canh model thiếu số** — nó là **cổng kiểm**,
không đụng đường ra số, và bệnh nó bắt **vừa xảy ra hai ngày liên tiếp**.

**5. Ngày mai bốn quyết định đổi trạng thái.** `OD-20260801-B` · `QD-015` · `QD-016` · `QD-017`
đều ghi «SAU 08/08» ⇒ từ 09/08 chuyển từ chờ sang phải thi hành. **Ba trong bốn đụng prompt** —
va chạm `QD-041`. Thi hành trong 08–10/08 còn làm bẩn **đúng cửa sổ** FU-325 + FU-284 đang đo,
cộng V11032/V11033 thành **ba biến chồng** — đúng thứ `QD-018` cấm.

**6. Hệ khoẻ, đừng nhầm với kết quả.** PID 1053968, `NRestarts=0`, health 200, **1 ERROR**
trong 24 giờ, `database is locked` **0 lần hôm nay**. Hạ tầng không phải vấn đề.
