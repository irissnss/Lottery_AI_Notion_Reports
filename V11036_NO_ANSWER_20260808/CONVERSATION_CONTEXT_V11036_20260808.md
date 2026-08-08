# CONVERSATION CONTEXT — V11036 · 2026-08-08 đêm

## Owner nói gì (NGUYÊN VĂN)

> mở khóa làm luôn, đồng thời xem luồng /nghiem-thu cũng khá dần lên đó em. Và đánh giá sau khi
> thay đổi prompt ngữ cảnh thực sư, số hóa ML thực sự thì các model có tiến triển gì không em?

## Ba việc, và hai trong ba câu trả lời là «chưa đo được»

### A — «mở khóa làm luôn»: ĐÃ VÁ

Owner mở khoá FU-355. Agent vá **ba chỗ**, không phải một:

| # | chỗ | vì sao phải vá |
|---|---|---|
| 1 | `scheduler.py` ghi `NO_ANSWER` | nguồn gốc — nơi lượt rỗng bị chép nhãn `LOSE` |
| 2 | **`combo_super._ti_le_bach_thu()`** | **chỗ THẬT SỰ dìm điểm** — `SUM(bt_hit)/COUNT(*)` đếm cả lượt rỗng vào **mẫu số** |
| 3 | 138 dòng lịch sử | để dữ liệu **nói đúng sự thật** |

**Suýt vá nửa vời:** bản đầu agent chỉ định sửa `scheduler.py`. Nhưng nếu không sửa
`combo_super` thì **138 dòng lịch sử vẫn tiếp tục làm sai bảng xếp hạng** — phải soi **ai ĐỌC
bảng**, không chỉ ai ghi (§60.2).

**Suýt tưởng xong khi mới vá bản sao:** backfill chạy ở máy local chỉ sửa **bản sao**; DB thật
nằm trên VPS và sẽ **ghi đè bản sao local** ở lần đồng bộ sau. Phải chạy backfill **trên VPS**.

**Tác động thật:** 7 ngày — MT `deepseek-reasoner` 42,9% → **50,0%**, MB `qwen3.7-max`
16,7% → **20,0%**. 30 ngày — 21 ô, nặng nhất **MB `gemma-4-31b` n 20→9** (11 lượt rỗng),
5,0% → **11,1%**. **0 model rớt sàn** ⇒ không mất ứng viên.

**Băm 4 bảng khoá ĐỔI CÓ CHỦ Ý** — lần đầu trong chuỗi phiên này. Ghi rõ để phiên sau không
báo động nhầm (RM-02). Sao lưu đủ mọi cột, **cả hai đầu**.

### B — `/nghiem-thu`: owner nhìn ĐÚNG bề mặt, nhưng số không chịu nổi phép kiểm

Bạch thủ **5/21 (23,8%) → 4/5 (80,0%)** — tái lập được, **đúng**.

Nhưng: đo tiến **chỉ có từ 30/07**; **135 hàng trước đó** tính lại retro trong **MỘT lượt** lúc
30/07 10:57:16. Trừ nền hai bên ⇒ chênh +52,3pp, **z +1,30**. Và **MDE ở n=5 là 104,1pp** —
cửa sổ này **không phát hiện nổi** thứ gì nhỏ hơn 104 điểm.

**Phản biện siết thêm ba chỗ:**
1. **Thiếu một miền-ngày, và nó là LOSE** — MB 08/08 chấm 19:10, đồng bộ 18:39. Vá đủ:
   **4/6 = 66,7%**, z **+1,96 → +1,60**. Con số gốc rơi **đúng ngay ngưỡng**.
2. MDE dùng công thức **một mẫu** cho câu hỏi **hai mẫu** — đúng là 106,5pp.
3. **«~46 ngày nữa soi được 20pp» SAI NẶNG** — cửa sổ TRƯỚC **đã đóng băng trong quá khứ**,
   không nở ra ⇒ **sàn MDE 50,2pp**. **Mức 20pp KHÔNG BAO GIỜ đạt bằng cách chờ.**

**Quy công cho đợt vá prompt là sai:** chỉ **1/5** miền-ngày «SAU» thật sự chạy prompt đã vá đủ.

**Đối chứng official không nhúc nhích** (z −0,05). **McNemar: p = 1,0.**

**✓ Cái DUY NHẤT khá lên thật: ĐỘ PHỦ** — 30/07–03/08 lỡ 3 miền-ngày → 04/08–08/08 **đủ 15/15**.

### C — Model có tiến triển không: CHƯA ĐO ĐƯỢC

**Runtime ≠ commit.** «Sáu lần đổi prompt» là mốc **commit**; runtime chỉ có **BỐN** bản.

Phép mạnh nhất kho dựng được (có ngữ cảnh vs ngữ cảnh hỏng, **trong cùng model**):
HIỆU **+3,28**, z **+0,94**, MDE **9,8** ⇒ **chưa vượt**.

Và dấu dương **không bền**: +3,65 → **+3,15** (sau dedupe 1.061 dòng trace trùng) → **+1,67**
(chỉ ngày có cả hai). **Phần lớn dấu dương là chênh thành phần ngày, không phải ngữ cảnh.**

Prompt dài thêm **không** đi kèm trúng nhiều hơn: r **+0,0337**, t **+1,22**.
Lần đổi prompt duy nhất đủ sức mạnh (18/07, **gấp 20 lần n**) cũng không kết luận được gì.

## ⚠ ĐIỀU NGUY NHẤT TÌM RA — phải nói ngay

**`_v10879_nghiemthu_lane.decide()` chỉ cần 2 ngày may nữa là lật sang
«ĐẠT — đủ điều kiện trình owner duyệt thay official» — KHÔNG có bất kỳ phép ý nghĩa nào.**

Hạn `DECISION_DATE = 19/08`, còn **11 ngày**. Trong khi McNemar trên đo tiến ra **p = 1,0**.
Nghĩa là ngày 19/08 hệ có thể **trình owner một kết luận sai**.

Kèm: `_discordant()` đếm sai — `both_lose` ra **−1** (số âm), backfill 33 thay vì 40.

Lane test, **QD-041 không chặn** ⇒ **làm được ngay**. Đây là NEXT ACTION.

## Điều agent NÓI THẲNG với owner

**1. Hai trong ba câu trả lời là «chưa đo được», và agent không làm nhẹ đi.** Kho này đã có
**bảy** lần *«hứa hẹn rồi rữa»* (V10655 → V10672 → V10677 → V10753 → V10789 → V10790 → V10857).
Đây sẽ không phải lần thứ tám.

**2. `/nghiem-thu` có khá lên — nhưng khá ở ĐỘ PHỦ, không phải ở tỉ lệ trúng.** Đó vẫn là tin
tốt thật: nó không còn lỡ ngày nữa. Chỉ là **không phải cái owner nghĩ**.

**3. Con số agent từng báo owner bị đính chính hai lần trong ngày:** «5 lượt rỗng» → **44**;
«prompt dài thêm 1.620 ký tự» → chỉ đúng MT+MB, **MN ngắn đi 10.475 ký tự**.

**4. Đây là biến thứ BA trong ngày.** `QD-018` «một biến một lần» bị nóng. Owner chủ động yêu
cầu nên thi hành, nhưng may là **08/08 đã bị loại** khỏi cả hai cửa sổ đo (SAU bắt đầu 09/08).

**5. Một bẫy phải vá TRƯỚC 21/08:** `database.py:2986` UPDATE **không lọc `run_source`**.
Chưa nổ (0 khoá trùng), nhưng **sẽ nổ đúng lúc `QD-015/016/017` chạy ngày 21/08** — vì đó chính
là lúc một model có thể chạy cả hai đường.
