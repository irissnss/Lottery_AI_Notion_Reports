# CONVERSATION CONTEXT — V11132 · 28/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`.

---

## 1 · Owner nói gì — nguyên văn

Lệnh tiếp tục prompt 43 R1, sau `V11131`:

> *« Không mở Prompt 44. Không dừng ở V11131. Không phát hành thêm report chỉ để nhắc lại
> A1/A2. Tiếp tục thi hành các phần còn thiếu ngay trong phiên này. »*
>
> *« V11131 không phải "PHA A DONE". Nhãn đúng: `PHA_A_PARTIAL · A1_A2_DONE · A3_A6_OPEN`. »*
>
> *« 93 dòng/0 empty/0 late chỉ chứng minh delivery completeness; cấm gọi predictive quality
> "hoàn hảo". »*
>
> *« Retrospective chỉ dùng chẩn đoán kiến trúc. CẤM promote model, cắt model, gỡ meta-learning
> official, đổi FINAL, gọi chênh nhỏ là thắng/thua khi chưa đủ power. »*
>
> *« Kết quả về meta-learning phải có: mức ảnh hưởng · số nguồn còn lại · nguồn bù ·
> effective cycle · rollback. Chưa đủ năm phần trên thì không hỏi Owner. »*
>
> *« Cổng phải đọc structured object/JSON, cấm regex stdout làm verdict. »*
>
> *« Không nói production thật đã chạy với 0 model. »*
>
> *« Trước 05:00: không restart production, không deploy thay đổi official path. »*

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| A3 preregistration | hash `dcbea497…` · giờ máy chủ 23:55:36 · ngưỡng **10,4 điểm** |
| A3 đo 5 biến thể | `M0` **30,77 %** thấp nhất · `COMBO_CURRENT` **35,53 %** cao nhất |
| A3 double-count | **13/18** model đếm hai lần |
| A3 family dedupe | **72/273 = 26,4 %** đổi top-1 |
| 🔴 tự bác một con số A3 | *«meta-learning đổi 147 ca»* → **sai**, đúng là **53/273 manifest** |
| cổng chống vacuous-pass | module + **11/11** thử · META ⑧ |
| cổng trên dữ liệu thật | **PASS** cả ba miền · 16 model · 0 shadow |
| PHA B | ⏳ **`WAIT_LIVE`** 05:00 |

---

## 3 · Vấp ở đâu — kể cả vấp do chính agent gây ra

### V1 · 🔴 Tôi tự bác một con số **vừa đo xong, trước khi công bố**

Bản A3 đầu cho *«bỏ `meta-learning` đổi lựa chọn ở **147/273 = 53,8 %** ca»* — nghe như
`meta-learning` là biến số lớn nhất của Combo, đủ để đề xuất gỡ ngay.

**Hai dấu hiệu tự phát hiện:**

1. `COMBO_WITHOUT_META_LEARNING` có **n = 148**, không phải 273 ⇒ so với biến thể n=273 là
   **so hai mẫu khác nhau**.
2. Chỉ **53/273** manifest nhắc `meta-learning` ⇒ bỏ một thứ có mặt 53 lần **không thể** đổi
   **147** ca. **Mâu thuẫn số học.**

**Nguyên nhân gốc:** script đọc `reasoning_json` bằng truy vấn **không cùng bộ lọc** với tập
`CAND` nên lệch dòng; và 125/273 manifest có `numbers` không phải `dict` nên rơi ra.

**Nếu công bố con số 53,8 %**, Owner sẽ có cơ sở để gỡ `meta-learning` — dựa trên một con số
**không tồn tại**.

### V2 · 🟢 Nhưng kiểm chứng lại cho thấy **phương pháp thì đúng**

`max(final_score)` **KHÁC** `main_numbers[0]` ở **0/62 ca** ⇒ phép tính lại **tái lập chính xác**
lựa chọn của Combo. Vậy lỗi là **căn dữ liệu**, không phải phương pháp — phép đo này **làm lại
được**, chỉ cần sửa cách nối.

Đây là lý do tôi ghi `NOT_VERIFIED` thay vì bỏ hẳn: **có đường đi tiếp**.

### V3 · Con số đúng lại **nhỏ và không có ý nghĩa**

`meta-learning` có mặt **53/273 = 19,4 %** manifest. Combo hit **39,62 %** (có) vs **34,55 %**
(không) — chênh **+5,08 điểm**, `z = +0,68` ⇒ **không khác biệt**. Và đó là **liên hệ**, không
phải phép thử loại bỏ.

⇒ **Packet hỏi Owner mới có 1/5 phần**, và chính phần *«mức ảnh hưởng»* vừa bị bác. **Không hỏi.**

### V4 · 🔴 Kết quả A3 dễ bị đọc sai theo hướng nguy hiểm

`M0_CURRENT_OFFICIAL` **30,77 %** — **thấp nhất trong năm biến thể**, thấp hơn cả nền.
`COMBO_CURRENT` **35,53 %** — cao nhất.

Đọc vội sẽ thành *«bỏ TOTAL, dùng Combo»*. **Sai**: chênh 4,76 điểm nằm **sâu dưới ngưỡng phát
hiện 10,4 điểm**, và bốn khoảng tin cậy **chồng nhau gần hoàn toàn**.

Điều **được phép** ghi nhận: *«FINAL hiện hành xếp cuối trong năm cách chọn»* — một **tín hiệu
kiến trúc đáng theo dõi**, không phải kết luận thống kê.

### V5 · Cổng mới phải tự chứng minh **nó không vacuous**

Nếu chỉ viết cổng rồi thử vài ca, chính bộ thử cũng có thể vacuous. Nên tôi thêm phép **⑧ META**:
mô phỏng cổng kiểu `V11130` và chứng minh **bằng thực thi** rằng nó cho dict rỗng qua
(`PASS`) còn cổng mới chặn (`FAIL`).

---

## 4 · Điều agent **không** làm, và vì sao

| không làm | vì sao |
|---|---|
| deploy / restart | Owner cấm trước 05:00 — PID **2694667** y nguyên PRE snapshot |
| deploy cổng mới | `LOCAL_ONLY` — cùng lý do |
| hỏi Owner về `meta-learning` | packet **1/5 phần**, và phần chính vừa bị bác |
| gỡ `meta-learning` | retrospective **cấm** dùng để cắt |
| kết luận *«Combo hơn TOTAL»* | chênh 4,76 < ngưỡng 10,4 ⇒ `INSUFFICIENT_POWER` |
| công bố con số 53,8 % | tự bác trước khi công bố |
| ghi *«PHA A DONE»* | A4/A5/A6 còn **OPEN** ⇒ `PHA_A_PARTIAL` |
| gọi `gpt-5-mini` *«chất lượng hoàn hảo»* | 93 dòng/0 rỗng/0 late chỉ là **delivery completeness** |
| ghi vào production DB | `-readonly` |

---

## 5 · Trạng thái cuối

| | |
|---|---|
| mutation official path | **KHÔNG CÓ** — PID và hash y nguyên PRE snapshot |
| tệp mới | **2 tệp `LOCAL_ONLY`** — cổng eligibility + bộ thử |
| A1 · A2 · A3 · cổng | 🟢 **DONE** |
| A4 · A5 · A6 | 🔴 **OPEN** |
| PHA B | ⏳ **`WAIT_LIVE`** 05:00 ngày 28/08 |
| `SHADOW_CHANGED_FINAL` | **`NOT_PROVEN`** |

---

TanPhatAI cần làm: ghi **A3** kèm `prereg_hash dcbea497…` — **13/18 model đếm hai lần**, và thứ tự: **`M0` 30,77 % thấp nhất** (dưới nền 33,87 %), `COMBO_CURRENT` 35,53 % cao nhất. **Đừng** đọc thành *«bỏ TOTAL dùng Combo»* — chênh 4,76 điểm **dưới ngưỡng 10,4** ⇒ **`INSUFFICIENT_POWER`**. Ghi **đính chính**: *«meta-learning đổi 147/273 ca»* **đã bị Agent tự bác trước khi công bố** — đúng là **53/273 (19,4 %)**, chênh **+5,08 điểm z=+0,68 không có ý nghĩa**, `COMBO_WITHOUT_META_LEARNING` = **`NOT_VERIFIED`** (lỗi căn dữ liệu, phương pháp vẫn đúng nên làm lại được). **Family dedupe đổi 26,4 % lượt** — đo trực tiếp, đáng tin hơn. Ghi **cổng chống vacuous-pass 11/11 thử**, phép META chứng minh cổng cũ cho rỗng qua; đã PASS trên eligibility production thật (3 miền, 16 model, 0 shadow); **`LOCAL_ONLY`**. Trạng thái **`PHA_A_PARTIAL`** — A4/A5/A6 còn OPEN. **Không mutation official path.**
