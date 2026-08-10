# CONVERSATION CONTEXT — V11057 · 10/08/2026 tối

## Owner nói gì (NGUYÊN VĂN)

> *«Hôm nay anh bận quá chưa xử lý gì thêm nha em, Giờ em tiến hành kiểm tra toàn lực dự đoán ngày
> hôm nay, sau đó tổng hợp lại đầy đủ chi tiết nhất đề xuất hướng xử lý an toàn nâng cao cải thiện
> dự đoán, push lên githubs nha em»*

Owner bận cả ngày, không xử lý gì thêm. Đây là phiên agent tự chạy, và vì thế **tầng phản biện
đối kháng là thứ duy nhất đứng giữa agent và một báo cáo sai** — không có owner chặn lại như
phiên V11054.

Nó đã chặn được **ba lần**, và agent tự bắt thêm **hai lần** khi buộc mình viết script tái lập.

---

## Kết quả ngày: 1/3, và điều đó bình thường

MN `75` TRÚNG · MT `28` trượt · MB `74` trượt. Vận hành sạch tuyệt đối: ba miền chốt đúng hạn,
26 phép tự kiểm chạy 18:05, ba cron tối chạy đúng phút, journal **0 traceback / 0 ERROR /
0 CRITICAL**, `NRestarts=0`, 4 bảng khoá nguyên vẹn.

Kiểm tra viên K5 tính lại **toàn bộ 81/81 dòng** `model_daily_eval` (không lấy mẫu) — lệch 0 ở
`bt_hit`, `hit_count`, `hit_numbers`, `status`.

---

## Thứ agent tưởng là phát hiện lớn, nhưng không phải

### «Cap V10752 cắt hai model bỏ phiếu cho số trúng»

Hôm nay MT: cổng `max_voters_cap` gỡ `meta-learning` và `smart-ensemble` — **cả hai đều bỏ phiếu
`19`, và `19` trúng**. Nghe rất nặng.

Agent đếm ra **41%** số ngày MT có model bị cắt từng bỏ phiếu số trúng. Rồi tự chặn mình lại và
tính nền đúng `1−(1−b)^k`: **71,0%**. Thực tế chỉ **57,6%** ⇒ nhóm bị cắt **KÉM nền**, không hề
giỏi hơn.

**Ca hôm nay là giai thoại một ngày.** Nếu không tính nền, nó đã thành một «phát hiện P0» sai.

### «Pool chứa số trúng 97,8% ⇒ trần cải thiện khổng lồ»

Cũng sai. Bốc **ngẫu nhiên 10 số** cũng chứa số trúng **~97,6%** vì mỗi ngày có ~31/100 đuôi ra.
Đó là **số học**, không phải độ phủ tốt. Con số 97,8% không nói gì về chất lượng khâu sinh.

### «MB là lỗi khâu chọn»

Agent chính nhìn dữ liệu thô và tưởng MB chọn sai (74 thua, 78 trúng ở hạng #5). Phản biện viên
K3 bác: **74 dẫn phiếu thật** (5 thô / 4 sau cộng) so với 78 (4 thô / 3). Luật «nhiều phiếu nhất»
**cũng chọn 74** và cũng trượt. **MB không phải lỗi khâu chọn.**

Chỉ **MT** mới là thất bại chọn thật — và cơ chế cũng không phải cái agent đoán: không phải
«trọng số lật ngược 6 phiếu bằng 3 phiếu», mà là **ba cổng lọc chạy TRƯỚC khi chấm điểm** đã gỡ
đúng ba model bỏ phiếu `19`, biến 6–3 thành hoà 3–3, rồi trọng số mới bẻ về `28`.

---

## Lỗi nằm trong báo cáo agent ĐÃ PUSH sáng nay

`REPORT_V11055 §3.4` viết `_apply_hot_cold_post_filter` *«đang sống trên đường chọn số»* và
*«dìm số gan cao ×0,3 trước khi vào top-10»*.

Phản biện K3 bác. Agent kiểm lại: bốn điểm gọi đều nằm trong `run_combo_super()`
(`combo_super.py:2029`) và `_make_prediction()` (`main.py:7892/8099/8352`) — tầng **output từng
model**. Bundle do `generate_final_bundle()` (`main.py:9405`) ráp, **hàm khác**.

Kết luận P4 vẫn còn hiệu lực **gián tiếp** (hàm định hình cái mà từng model xuất ra, rồi mới vào
pool), nhưng **mô tả cơ chế đã sai tầng**. Đã ghi TRƯỚC/SAU và đưa vào dòng `TanPhatAI cần làm:`.

---

## Phản biện sửa cả PHƯƠNG PHÁP của agent

Agent dùng `VIF = 2,92` cho mọi thước — coi nó như hằng số toàn cục vì `CLAUDE.md §61 RM-18` ghi
con số đó.

Phản biện K2 chỉ ra: **2,92 đo cho thước KHÁC** (16 model cùng đoán một ngày). Agent tự đo VIF
thực nghiệm cho thước bạch thủ, cụm = ngày, 164 ngày:

```
phương sai nếu độc lập 106,36  ·  phương sai quan sát 94,60  ⇒  VIF = 0,889
```

Áp `2,92` làm CI **phồng lên vô cớ**, và theo hướng **có lợi cho kết luận «không kết luận được»**
— tức bảo thủ sai chiều. Đây là điểm phương pháp đáng ghi vào sổ.

---

## Con số quyết định của cả phiên

Sau khi sửa VIF và bỏ window-shopping, đo trên **toàn bộ 164 ngày / 492 miền-ngày**:

| | |
|---|---|
| bạch thủ công bố | **169/492 = 34,3%** |
| nền ngẫu nhiên đúng (`đuôi ra ngày đó / 100`) | **34,0%** |
| **lợi thế** | **+0,34pp** · CI95 **[−3,8 … +4,5]** |

Agent suýt báo **−2,2pp** (cửa sổ 120 ngày) — nghe như hệ tệ hơn ngẫu nhiên. Nhưng dấu **đổi theo
cửa sổ**, và chọn cửa sổ xấu để kể chuyện là đúng thứ RM-18 cấm.

**Đọc đúng: hệ không tệ hơn ngẫu nhiên, cũng không tách được khỏi ngẫu nhiên — và CI đủ hẹp để
loại trừ mọi lợi thế trên +4,5pp.**

Kèm số cần cho kế hoạch: muốn **chứng minh** +5pp phải chạy **115 ngày = 3,8 tháng**. Cho +3pp: **10,5 tháng**.

*(Bản nháp đầu ghi 11 tháng vì dùng nhầm `VIF=2,92` của thước khác — nặng hơn **3 lần** thực
tế. Bắt được lúc buộc mình viết script tái lập theo RM-11. «11 tháng» đọc thành *vô vọng*,
«3,8 tháng» đọc thành *làm được trong quý này* — lỗi đổi kết luận.)*

> Đây là lời giải **vật lý** cho sáu lần «hứa rồi rữa» (V10655→V10790): các phép đo đó **chưa bao
> giờ đủ sức mạnh**. Không phải ý tưởng sai — **thiết kế đo sai**.

---

## Thứ duy nhất vượt ngưỡng thống kê trong cả phiên

**Bầy đàn cụm AI là có thật.** Đo bằng tỉ lệ đồng thuận từng cặp (không phụ thuộc cỡ mẫu), 90
lượt miền-ngày: AI **0,2929** vs ML **0,1519**, chênh **+0,1411**, **z = +3,10**.

Nhưng bầy đàn **chưa chứng minh được gây thiệt hại**: tỉ lệ trúng hai cụm gần bằng nhau (33,27%
vs 32,22%, z=−0,10), **cả hai đều đúng trên nền**.

Và phản biện chỉ ra kho **đã có sẵn** bảng `convergence_cluster_pattern_daily` (1.067 dòng, có
`herd_voter_count`/`ai_voters`/`ml_voters`) — **không cần dựng bảng mới**. Đúng bài học V11054:
agent hay đề xuất lại thứ đã có.

---

## Một học thuyết của owner đang bị chính hệ bỏ qua

MT hôm nay, hệ tự ghi ra cảnh báo này rồi **vẫn công bố**:

> *«bundle bach_thu 28 was already emitted in ALL prior same-day regions (MN) — owner anti-trap
> owner-doctrine flag»*

Prompt **dạy** model tuân học thuyết (`gpt_analyzer.py:755`), nhưng bộ ráp bundle chỉ **tính cờ
SAU khi đã chọn xong** (`main.py:10205` nhận `bach_thu` đã chốt làm tham số) rồi ghi cảnh báo.
**Không có nhánh nào đổi số.** Đã xảy ra **51 lần**.

Thành tích của cờ, phân tầng theo miền: MB **−12,7pp** · MT **−12,7pp** — hai miền nền khác hẳn
nhau (12,7% vs 38,4%) cho chênh **giống hệt đến một chữ số thập phân**. Gộp MH: −12,7pp,
CI95 [−26,2 … +0,7], z=−1,02.

Nhưng phản thực thay số chỉ được **+6,4pp**, z=+0,49 — vì số thay thế nằm tận hạng **#2,4**, mất
lợi thế xếp hạng. **Biết một số kém không đồng nghĩa có số tốt hơn để thay.** Nên đề xuất là
**đo tiến**, không phải bật.

---

## Điều agent nói thẳng về «nâng cao chất lượng dự đoán»

Với lợi thế đo được **+0,34pp ± 4,2pp** trên 164 ngày, **thêm model / thêm luật / thêm tầng
prompt là hướng sai** — không phải vì ý tưởng dở, mà vì **mọi thay đổi dưới +4,5pp nằm trong
nhiễu**, và thêm thứ mới chỉ tạo thêm chỗ để tin nhầm.

Thứ nên làm là **sửa thiết kế đo trước, không sửa hệ**: mọi phép đo mới phải gộp 3 miền, khai
**n-cần** ngay từ đầu, đăng ký ngưỡng trước. Và ưu tiên thứ có **CƠ CHẾ rõ** (như anti-trap —
chênh giống hệt ở hai miền nền khác nhau là dấu hiệu cơ chế thật) thay vì thứ có **SỐ ĐẸP**
(105 luật khai mỏ: **0/105 qua cổng**).

---

## Cảnh báo cho việc chốt FU-360 sáng mai

**MN chạy 05:00–05:36, TRƯỚC lần restart 10:22:41.** Nên hôm nay **chỉ MT/MB thực sự chạy dưới
cổng chặn chéo lane**. Chưa phải `RUNTIME_PROVEN` đủ ba miền — phải ghi **đúng tầng** khi đóng
(RM-12), không được nâng cấp tầng.

---

## Trạng thái cuối phiên

Production **không đổi**: PID `1286954` · health 200 · 4 bảng khoá nguyên · `QD-041` nguyên vẹn.
Canh 24h FU-360: **0 dòng, 0 chặn nhầm**, 11,8 giờ vào cửa sổ.

TanPhatAI cần làm: xem mục cuối `REPORT_V11057.md` — năm việc, gồm đính chính nhãn tầng trong
`REPORT_V11055 §3.4`, ghi VIF phải đo theo từng thước, và ghi n-cần vào các phép đo đang treo.
