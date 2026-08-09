# CONVERSATION CONTEXT — V11050 · GĐ-B/C/D · 2026-08-09

## Owner nói gì (NGUYÊN VĂN, phần định đoạt GĐ-B)

> **GĐ-B (chỉ đọc, sau block).**
> B1 vá `anchor_date <= date(?,'-1 day')` + unit test ·
> B2 chạy lại `loz_stage_trace` trên 96 ngày mới ·
> B3 soi khô `_v10705` — **chỉ 3 câu hỏi, không dùng backtest làm căn cứ** ·
> B4 đo lại FU-160/162/164 (bảng GIỮ/GỘP/GỠ) ·
> B5 danh sách drift K3 · B6 thêm `kiem_code` cho QD-047 ·
> B7 thiết kế lại FU-360 ở tầng `INSERT OR REPLACE` (**CHỈ KẾ HOẠCH**).

> **QD-041: CẤM đụng prompt/đường chọn số/roster/quyết định gửi LLM tới 21/08.**
> **Mọi phát hiện do subagent đưa phải verify lại độc lập. Cấm chép lại tuyên bố chưa kiểm.**
> **TRẦN SINH MÃ: tối đa 5 mã FU mới toàn phiên.**

---

## Việc đáng kể nhất: hai lần suýt báo sai, cả hai đều tự bắt được

### ① Suýt báo «465 tệp lệch giữa local và VPS»

Đo drift lần đầu bằng `md5` thô: **465/467 tệp khác nhau**. Con số đó nếu đưa lên báo cáo thì đọc
như một thảm hoạ toàn vẹn.

Nó **sai**. Kho này là **CRLF**, blob trong git là **LF** ⇒ băm thô thì **mọi tệp đều khác**, kể
cả tệp không ai động tới. Số thật sau khi chuẩn hoá xuống dòng: **30**.

Đây đúng **RM-09** (kết luận bằng đếm/băm thô). Bẫy CRLF là bẫy `CLAUDE.md` **đã ghi sẵn**, và
hôm nay nó cắn lần thứ **năm** trong hai ngày. Nên lần này không sửa bằng cách nhớ kỹ hơn: việc
**bỏ `\r` trước khi băm** viết thẳng vào cổng `_v11050_kiem_drift.py`, hai đầu local và VPS đo
cùng một cách.

### ② Suýt cáo buộc «có người sửa thẳng 28 tệp trên VPS»

Phân loại drift lần đầu viết sai **thứ tự nhánh `if`**: nhánh «khác cả git lẫn bản làm việc» đặt
trước nhánh «git = bản làm việc, VPS khác», nên nó **nuốt** trọn nhóm sau. Kết quả: 28 tệp thuộc
loại lành (**đã commit mà VPS chưa nhận**) bị dồn vào ô nặng nhất — *ba bản ba đường, dấu hiệu có
người sửa thẳng trên máy chủ*.

Bắt được vì con số 28 **vô lý so với ngữ cảnh**, không phải vì chương trình báo lỗi. Chương trình
chạy trơn, in đẹp, và **sai kết luận** — đúng loại lỗi khó nhất.

Số đúng: **(a) 2 chờ commit · (b) 0 sửa thẳng trên VPS · (c) 28 git đi trước.**
Và **(b) = 0 là tin tốt**, phải nói ra: không ai sửa lén trên máy chủ.

---

## Chỗ agent DỪNG, và vì sao dừng là đúng

**B2 không chạy.** `_materialize_loz_stage_trace_shadow.py` nằm trong **28 tệp VPS chưa nhận**.
Chạy trên VPS = chạy **mã cũ**; chạy ở local = đọc **DB không phải production**. Cả hai đều là
**RM-13** (nguồn sai ⇒ mọi kết luận sai) — cái lỗi ngày 07/08 phạm **ba lần trong một ngày** và
suýt «sửa» một lane MB đang chạy đúng.

Có số để báo cáo thì dễ. **Có số đúng thì phải sửa drift trước.**

**`_v104_shadow_prompt_injection.py:297` không đụng.** Nó dùng **cùng mẫu** `anchor_date <= ?` và
**không** chặn biên — nhưng bảng khác (`gan_signal_shadow_v100`) và tệp nằm trong **đường bơm
prompt** (`scheduler.py:8871`) ⇒ **vùng đóng băng QD-041**. Ghi lại, không sửa. Và cũng không
được suy «cùng mẫu nên cũng sai» — bảng khác thì phải có phép kiểm nhân quả riêng.

---

## Phát hiện lớn nhất của GĐ-B, kèm ba câu phải nói ngay sau nó

Bảng `v93_verdict_weight_recalibration_shadow` — **suýt bị agent xoá ngày 08/08 vì tiền đề sai** —
đã ghi **122 ngày liên tục** và chứa đề xuất định lượng chưa ai đọc:

- verdict `SKIP` đang được tính **0,40**, dữ liệu 30 ngày nói nên là **~1,1** (mẫu 1.213–2.475)
- `CHOT`/`CHOT_HA` họ NO_TOKEN đang tính **1,50**, dữ liệu nói **~0,82** (mẫu 4.082)
- **65,6%** số dòng đề xuất lệch ≥ 0,05 so với trọng số đang chạy

Ba câu phải nói ngay, nếu không thì đây thành đúng loại «số đẹp dùng làm căn cứ» mà RM-17 cấm:

1. **Chưa kiểm dẫn xuất** của `proposed_weight_30d` — có trừ cụm ngày/VIF không, nền có đúng
   không. Chưa kiểm thì chưa được dùng.
2. Đổi trọng số verdict **chính là đường chọn số** ⇒ **QD-041 khoá tới 21/08**.
3. **Chưa có ngưỡng hành động đăng ký trước** ⇒ dù số đẹp cũng chưa được phép kết luận (RM-03).

---

## Điều agent nói thẳng

Hai lỗi trong GĐ-B đều **không làm chương trình gãy** — chúng làm **kết luận sai** trong khi mọi
thứ chạy trơn. Đó là loại lỗi nguy nhất, và cả hai chỉ lộ vì con số bị đem đối chiếu với ngữ cảnh
thay vì được chép thẳng vào báo cáo.

Và việc đáng giá thứ hai của GĐ-B là **không làm B2** — trong khi làm nó thì dễ, có số để khoe, và
gần như chắc chắn không ai phát hiện nguồn sai.
