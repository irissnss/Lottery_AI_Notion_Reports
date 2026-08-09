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


---

# PHẦN NỐI — V11051 · V11052 (chiều 09/08, sau PROMPT LẦN 9)

## Owner nói gì (NGUYÊN VĂN, bốn quyết định đã ký 13:58)

> **Q1.** *v93: ĐƯA VÀO danh sách mở khoá 21/08. ĐƯỢC thẩm định dẫn xuất READ-ONLY … CẤM dùng kết
> quả làm căn cứ đổi số trước 21/08.*
> **Q2.** *28+2 tệp: DUYỆT một lượt deploy có ký — theo đúng trình tự A'1.*
> **Q3.** *FU-360 phương án ③ — ĐÃ DUYỆT … nếu chạm đường ghi production → để sáng mai 10/08.*
> **Q4.** *FU-391 ĐÓNG · FU-388 ĐÓNG · FU-390 CẤM đóng hàng loạt, rà THEO NHÃN.*
>
> *«Bốn mục dưới đây là quyết định đã ký — thi hành, không hỏi lại.»*

## Chỗ agent KHÔNG thi hành nguyên văn, và vì sao

Owner ghi rõ *«thi hành, không hỏi lại»*. Agent vẫn dừng **một** mục — và đây là lý do.

**Q2 ký trên một tiền đề, sự thật là thứ khác.** Lệnh duyệt đẩy 28+2 tệp được ký khi cả owner lẫn
agent tin đó là **drift tồn đọng vô hại** — chính agent mô tả như vậy ở GĐ-B. Bước (b) của trình
tự A'1 (phân nhóm backend) buộc phải đọc diff, và diff cho thấy: **25/28 tệp đổi đúng MỘT dòng, và
cả 25 là cùng một việc — thêm `claude-opus-4-6`**.

`strength_calibrator.py` thêm `'claude-opus-4-6': 0.75`, mà `calibrate_strength(...)` được gọi ở
**bảy chỗ** trong `main.py` và `scheduler.py` đang chạy. Đẩy nó **là đổi đường chọn số** — thứ
`QD-041` cấm tới 21/08, và cũng chính là thứ **cắt cửa sổ đo FU-284** mà cả phiên này dựng ra để
giữ. Trong cùng prompt lần 9, owner vẫn ghi *«20/08 chốt mọi phép đo … 21/08 mở khoá»*.

Nên đây **không phải agent cãi lệnh**: đây là **hai lệnh của owner mâu thuẫn nhau khi tiền đề của
lệnh sau hoá ra sai**. Agent thi hành phần không mâu thuẫn (3 tệp không dính roster), dừng phần
mâu thuẫn, và trình **ba phương án** để owner ký lại trên sự thật đúng.

Agent cũng tự phản biện: *«model đã chạy sẵn rồi, đâu kích hoạt gì mới?»* — đúng, `claude-opus-4-6`
đã có trong `predictions` và `model_registry` trên VPS. Nhưng cái đổi là **hiệu chỉnh**, không phải
**sự tồn tại**. Kết luận không đổi.

## Việc đáng kể thứ hai: agent tự bác bỏ phát hiện lớn nhất của chính mình

Ở GĐ-B agent nêu bảng `v93_verdict_weight_recalibration_shadow` là phát hiện lớn nhất: **65,6%**
dòng đề xuất trọng số lệch so bản đang chạy, kèm những con số nghe rất mạnh (`SKIP` 0,40 ↔ 1,19).

Owner ký Q1 cho thẩm định. Kết quả: dẫn xuất là
`proposed = clip(0.5 + any_hit_pct/100, 0.4, 1.5)` — **hai hằng số không có nguồn gốc**, và chú
thích của chính tác giả ghi *«For now just store …»*. Tách theo trọng số hiện tại thì
`any_hit_pct` ba nhóm là **54,2% · 61,2% · 51,3%** — gần như nhau — trong khi «chênh» là
**+0,64 · +0,11 · −0,49**. ⇒ **Chênh do trọng số đang dùng, không do hiệu năng.**

Agent **rút lại** hai câu của chính mình. Agent có kèm ba câu cảnh báo ở B4 nên **không con số nào
bị dùng làm căn cứ**, nhưng tiêu đề *«phát hiện lớn nhất»* đã đi trước phần thẩm định — đó là lỗi
trình bày, ghi lại theo RM-17.

## Ba chỗ cổng tự quay lại cắn người dựng ra nó

**① Cổng `THI_HANH_57` đòi đóng đúng thứ vừa được chứng minh là còn sống.** Nó đòi đóng
`FU-160/162/164` (ba mã GĐ-B vừa chứng minh có 6 bảng sống 122 ngày), rồi sau đó đòi đóng cả
`FU-390` — thứ owner **vừa cấm đóng hàng loạt trong chính prompt này**. Nguyên nhân: cổng **tính
lại danh sách mỗi lần chạy** thay vì ghim tập đã được ký lúc 00:33.

**② Một ô `kiem_code` rỗng làm sập cả bộ kiểm sổ quyết định**, và sập **trong im lặng** — in
«3 phép trôi» rồi chết giữa chừng, nên chính con số 3 đó cũng là của một lượt chạy chưa hết sổ.

**③ Bộ sinh sáu mặt chỉ ghi một mặt.** Thêm RM-20 vào `CLAUDE.md` thì `AGENTS.md` có,
`GEMINI.md` **không** — mà script vẫn in *«SÁU MẶT ĐỒNG BỘ»*. `_v10925_rule_sync_check.py` **chưa
bao giờ** sinh `GEMINI.md`, dù `CLAUDE.md` khai cả hai là mặt sinh và cấm sửa tay cả hai.

Cả ba đều là **cổng báo xanh cho thứ nó chưa kiểm** — đúng họ với cổng đóng băng QD-041 từng luôn
báo xanh (RM-15). Đã vá cả ba.

## Chỗ agent nói thẳng

Prompt lần 9 viết *«thi hành, không hỏi lại»*, và agent hiểu vì sao owner viết vậy: phiên trước có
quá nhiều câu hỏi. Nhưng **dừng 25 tệp roster không phải là hỏi lại** — nó là báo rằng **lệnh và
tiền đề của lệnh đã tách nhau**. Nếu agent cứ đẩy cho đúng chữ, thì đến 20/08 phép đo FU-284 sẽ
vô giá trị và **không ai biết vì sao**, vì thay đổi được giấu trong một dòng của 25 tệp mang nhãn
«drift».
