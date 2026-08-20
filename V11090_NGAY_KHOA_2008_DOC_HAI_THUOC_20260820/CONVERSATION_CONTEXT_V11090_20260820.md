# CONVERSATION CONTEXT — V11090 · 20/08/2026 · NGÀY KHOÁ

## Owner nói gì (NGUYÊN VĂN)

> *«Đã nhiều ngày qua anh không xử lý, kiểm tra hệ thống để hệ thống chạy ổn định và đo lường.
> Ngày mai tới hạn xử lý rất nhiều vấn đề rồi em. Trước tiên em kiểm tra, phân tích đánh giá,
> kết quả dự đoán nhiều ngày qua như thế nào có gì chuyển biến mới mẻ, cần xử lý gì, có phát
> hiện gì mới. Kế hoạch xử lý sau ngày 21/08 vẫn như cũ đúng không em?»*

---

## Hôm nay đúng là ngày khoá — và hai thước tới hạn đọc

Ngày đọc `FU-284` được owner chốt từ **09/08**: **20/08**, không kéo dài. Hôm nay là ngày đó.

Nên phiên này không phải «kiểm cho biết» — nó là **phiên đọc verdict**, và verdict quyết định
gói ngày mai có 13 hay 14 mục.

---

## `FU-284` — cả ba miền CHƯA KẾT LUẬN, và MT là ca đáng nói

```
MN  n 214/176   chênh  +2,5 điểm   z +0,29   sức thật ±16,82
MT  n 214/175   chênh +14,2 điểm   z +1,72   sức thật ±16,20
MB  n 214/176   chênh  -3,4 điểm   z -0,46   sức thật ±14,47
```

**MT vượt ngưỡng chênh.** `+14,2` lớn hơn `9,53` khá nhiều. Nhìn riêng con số đó thì rất muốn
viết *«MT có tiến bộ»*.

Nhưng ngưỡng đăng ký trước đòi **CẢ HAI** — `|chênh| ≥ 9,53` **VÀ** `|z| ≥ 1,96`. `z = 1,72`,
thiếu **0,24**.

Và tài liệu ngưỡng (`docs/NGUONG_FU284_N12_20260809.md`, viết **09/08**) đã ghi sẵn:

> *«Không có ô «gần đạt». Thiếu một điều kiện là chưa được phép kết luận — không phải «yếu»,
> không phải «xu hướng tích cực» (RM-04).»*

Câu đó viết **trước khi ai thấy số**. Đó chính là toàn bộ giá trị của luật đăng-ký-trước: nó
không cho phép người đọc thương lượng với chính mình sau khi đã thấy kết quả.

### Nhưng phải đọc cho đúng nghĩa

`CHƯA ĐƯỢC PHÉP KẾT LUẬN` **không** có nghĩa *«prompt mới không khác gì»*.

Nó có nghĩa **cửa sổ 12 ngày không đủ sức phân biệt**: sức thật **±14–17 điểm**, trong khi ngưỡng
là `9,53`. Muốn thấy chênh **5 điểm** cần **44–50 ngày**.

Tức là: nếu ba thay đổi prompt có tác dụng thật cỡ 5 điểm — mức rất đáng có — thì phép đo này
**không thể thấy được**, và kết quả sẽ **luôn** ra «chưa kết luận».

---

## Lane T-B — hai ngày trước «không đọc được», nay đọc được

Đây là khác biệt đáng ghi. Ngày 18/08 lane có 110 dòng và **0 cặp chấm**, vì **không có bộ chấm
nào tồn tại**. Owner ký lối A lúc 22:27, bộ chấm dựng xong trong đêm.

Hôm nay, sau khi đồng bộ và **chạy lại bộ chấm**:

```
140 cặp chấm được · 0 từ chối
100 cặp BẤT ĐỒNG          ✓ ĐẠT sàn 96 của QD-059
McNemar: b=18 · c=21 · hoà 61
z = (21-18)/√39 = +0,480   ✗ cần ≥1,96
thô: control 41/140 · T-B 44/140
```

**Sàn mẫu đạt, `z` không đạt ⇒ chưa được phép kết luận.**

T-B nhỉnh hơn về **hướng** (21 thắng vs 18 thua trong các cặp phân biệt), nhưng **39 cặp phân
biệt là quá ít** — 100 cặp bất đồng nhưng 61 trong số đó **hoà** (cùng trúng hoặc cùng trật).

Đó là chi tiết đáng chú ý: *bất đồng về SỐ CHỌN* không đồng nghĩa *phân biệt được về KẾT QUẢ*.
Sàn `≥96 cặp bất đồng` của `QD-059` hoá ra **không phải sàn đúng** — sàn đúng phải là số cặp
**phân biệt** (`b+c`), và con số đó mới chỉ **39**.

---

## Một chỗ dễ quên, và nếu quên thì kết luận sai hoàn toàn

`_sync_live_forensic_inputs.py` **ghi đè** DB local. Điểm chấm lane T-B **mất sạch** sau mỗi lần
đồng bộ.

Nếu hôm nay đồng bộ xong rồi đọc thẳng, sẽ thấy **0 cặp đã chấm** và kết luận *«lane vẫn hỏng»* —
trong khi bộ chấm hoàn toàn ổn.

Đã ghi vào bản đồ 21/08: **chạy lại `_v11089_cham_lane_tb.py` SAU đồng bộ, TRƯỚC khi đọc.**

---

## Kết quả dự đoán 12 ngày — không có chuyển biến gì

```
14 ngày  n= 42   +4,48pp   z +0,61
30 ngày  n= 90   +3,03pp   z +0,61
90 ngày  n=270   −3,16pp   z −1,10     <-- âm
180 ngày n=522   +0,72pp   CI95 [−3,3 · +4,8]
```

Cửa sổ 30 ngày tụt nhẹ (`+4,23 → +3,03pp`) sau hai ngày yếu (19/08 `1/3`, 20/08 `0/3`), nhưng
bức tranh **y hệt 17–18/08**: **dấu đổi theo cửa sổ**, và con số đứng vững là `+0,72pp` với
khoảng tin cậy **trùm số 0**.

Theo miền 90 ngày: MN `+0,54pp` · MT `−4,13pp` · MB `−5,88pp`. MB vẫn là miền yếu nhất.

**Không có phát hiện mới nào về hiệu quả dự đoán.** Đó tự nó là thông tin: hệ **ổn định quanh
nền**, không trôi xuống, cũng không nhích lên.

---

## Trả lời thẳng câu owner hỏi về kế hoạch sau 21/08

**Có đổi, đúng một chỗ:**

`#13 GĐ2 dịch ngữ cảnh` có điều kiện *«CHỈ nếu `FU-284` cho phép»* (`QD-064`). `FU-284`
**không cho phép** ⇒ **mục này không làm**.

**Gói 21/08 từ 14 mục còn 13 mục.** Mọi thứ khác — thứ tự ba làn, cảnh báo va chạm
`D2` × `FU-397b`, điểm gỡ về từng mục, bảng kiểm 9 bước — **y nguyên**.

---

## Trạng thái cuối phiên

Production **không đổi**. `QD-041` nguyên vẹn tới 21/08. **10/10 cổng xanh.**

**Hai thước vẫn cấm đọc** — bầy đàn và DEHERD, vì **chưa có chữ ký owner**. Ngưỡng đã đề xuất
đầy đủ từ 18/08; không ký thì hai phép đo đó **không bao giờ đọc được**.

**Miễn trừ K8 hết hạn 21/08** — sau đó đỏ lại là **CỐ Ý**, là lời nhắc xử `FU-360`/`FU-389`.

TanPhatAI cần làm: đọc mục 9 của `REPORT_V11090.md` — quan trọng nhất là ① **`#13 GĐ2` không mở
khoá** (gói còn 13 mục), ② **hai ngưỡng chưa ký**, ③ **`FU-284` nên đóng hay kéo dài** — ba lối
A/B/C chờ owner.
