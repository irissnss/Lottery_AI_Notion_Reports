# CONVERSATION CONTEXT — V11062 · 11/08/2026 tối muộn

## Owner nói gì (NGUYÊN VĂN)

> *«Còn 1 chỗ em chưa phân tích tại sao " Gemini 3.6 Flash " MB nay rỗng là sao? các prompt hôm
> qua điều chỉnh có thấy output dự đoán khá hơn không? Các đề xuất của em anh đồng ý em tiến hành
> 1 cách cẩn thận và tỉ mỉ dùm anh nhé.*
>
> *Dự án có cơ chế nâng version và cập nhật changlog, history chưa anh cần em xử lý thêm chỗ này
> và cập nhật vào claude.md sync nhất quán với 5 file quản trị khac dùm anh»*

Owner nhìn vào một **ô trống trên màn hình** mà agent đã lướt qua trong bản kiểm "toàn diện" vừa
nộp. Và câu hỏi thứ tư — tưởng là việc dọn dẹp — lôi ra **hai mảnh quản trị đã chết nhiều ngày**.

---

## Ô trống đó dẫn xuống bốn lớp

**Lớp 1.** `gemini-3.6-flash` có 32 dòng lịch sử, **chỉ 1 rỗng** — chính là MB hôm nay. MN và MT
cùng ngày vẫn ra số (MN còn **WIN**). Nên **không phải khoá**, không phải hỏng kinh niên.

**Lớp 2.** Google trả **503**, và chỉ cho model đó:

```
16:59:09  gemini-3.5-flash → 200
17:00:42  gemini-3.6-flash → 503      ← 93 giây sau, cùng dự án, cùng đường khoá
17:49:23  gemini-3.5-flash → 200
17:50:05  gemini-3.6-flash → 503
```

Đây là chỗ agent phải cẩn thận: **sáng nay agent vừa mắc lỗi NGƯỢC LẠI** — gọi một lỗi cấu hình
của mình thành *«hạn mức nhà cung cấp»*. Cám dỗ bây giờ là bẻ kết luận cho khớp bài học đó. Nhưng
bằng chứng đi hướng khác: khoá **đúng** (`[KEY_MODE] … from DB`), model khác **200** cách đó 93
giây. **Không được bẻ.**

**Lớp 3 — và đây mới là nguyên nhân thật:**

```
17:50:05  Google      → 503
17:50:08  OpenRouter  → 200 OK       ← dự phòng ĐÃ chạy và ĐÃ thành công
17:51:13  ghi vào DB  → RỖNG
```

**HTTP 200 ≠ có số.** Đúng họ lỗi agent vừa mắc sáng nay ở lane A/B.

**Lớp 4 — trả lời câu «có ảnh hưởng gì không».** Model này `run_source=shadow_auto_eval`,
**không nằm trên đường ra số official**. Và dòng ghi lúc **17:51**, bundle MB chốt **17:37** —
muộn **14 phút**. Kể cả có số cũng vô ích.

---

## Một báo động giả agent đã tự rút — và nó suýt to

Trên đường truy, agent thấy **140 dòng dự đoán rỗng trong toàn kho, tất cả mang
`predictions.status = LOSE`**. Nặng nhất `gemma-4-31b`: **53/230 = 23% số lượt**.

Nếu đúng thì đây là lỗi lớn: tỉ lệ thắng chính là thước chọn top-3 cho combo-super, model bị dìm
23% sẽ **rớt hạng oan**.

Agent định báo. Rồi kiểm bảng chấm thật:

```
model_daily_eval: pick_count=0  status=NO_ANSWER  bt_hit=0
combo_super.py:673:  AND status IN ('WIN','LOSE')     ← NO_ANSWER bị loại khỏi mẫu số
```

`LOSE` chỉ nằm ở bảng `predictions`. Bảng **chấm điểm** có nhãn riêng đúng nghĩa. Và việc này
**đã được xử từ `V11036` / `QD-046` / `FU-355`**, có cổng riêng — chạy lại hôm nay:
**`NO_ANSWER_V11036=ĐẠT`**, *«0 model rớt sàn vì loại lượt rỗng»*.

**Agent suýt báo lại một việc đã xong.** §56 nói rõ: **tra ba nơi trước khi báo**.

---

## Câu prompt: điều agent phải nói KHÔNG được

Owner hỏi prompt điều chỉnh hôm qua có cho output khá hơn không.

Có hai cách trả lời sai:
- **Nói «có»** — vì 12/12 chạy sạch nghe như thắng lợi. Nhưng đó là **vận hành**, không phải **chất lượng**.
- **Nói «chưa biết»** rồi bỏ đó — vì thực ra **có** thứ đo được và nói được.

Agent trả lời tách bạch:

> Prompt ba tầng **chỉ chạy trong lane shadow**, **không** đụng production (`QD-041` khoá tới
> 21/08). Nên **1/3 hôm nay không liên quan gì tới nó**.
>
> Về chất lượng: **chưa được phép đọc** — ngưỡng đăng ký trước là **≥96 cặp bất đồng và
> |z|≥1,96**, hiện có **9**.
>
> Về vận hành: **0/5 → 12/12**, trễ 35–154s. Và **4/4 model đổi dạng đầu ra** sang `§25` vì §22–§26
> bị đẩy xuống tầng 3 — bằng chứng prompt **có tác động**, **không phải** bằng chứng nó **tốt hơn**.

Đọc sớm chính là cách sáu lần *«hứa rồi rữa»* (V10655→V10790) đã xảy ra.

---

## Câu hỏi thứ tư lôi ra hai mảnh đã chết

Owner hỏi tưởng nhẹ: *«có cơ chế nâng version chưa?»*

| khâu | thực trạng |
|---|---|
| cấp số hiệu | ✅ có cổng thật, quét **sáu** nơi — dựng sau khi số va chạm **5 lần trong 2 ngày** |
| ghi tài liệu | ❌ **không có công cụ dùng lại**; mỗi phiên tự viết script nháp — **riêng hôm nay agent viết 2 cái** |
| `AUTOMATION_HISTORY.jsonl` | ❌ **CHẾT** — nửa sổ sự kiện im từ **31/07**, nửa sổ version im từ **04/08** |
| luật thành văn | ❌ **không mặt nào** trong sáu mặt ghi quy trình |

**Tám cổng máy đang chạy, không cổng nào soi tới** — vì chưa ai đặt câu hỏi *«tệp này còn được ghi
không?»*. Đúng họ `RM-20`: **ngừng ghi ≠ không có việc**.

Và `CLAUDE.md` vẫn liệt kê `AUTOMATION_HISTORY.jsonl` là *«mặt máy đọc được»* — **mô tả một mặt
không còn hoạt động**.

---

## Agent tự bắt một tiền đề sai của chính mình

Bản nháp đầu của cổng mới lấy tiền đề *«HISTORY phải có đủ mọi mục của CHANGELOG»* và báo:

> **thiếu 286 bản**

Nghe rất kêu. **Sai.** Đọc **tên trường thật** thì:

```
A) sổ SỰ KIỆN   seq / observed_at / event_type / command / exit_code    206 dòng, gốc 26/04
B) sổ VERSION   version / ngay / chu_de                                 101 dòng, nhét vào sau
```

Tệp **trộn hai lược đồ** và **chưa bao giờ** là bản sao của `CHANGELOG`.

> **Agent viết một cổng ĐỂ CHỐNG việc đoán, mà chính cổng đó dựng trên một cái đoán** (`RM-10`).
> Chỉ khi buộc mình in ra tên trường thật mới lộ.

**Và agent CỐ Ý không bù 286 bản.** Bù nghĩa là chế 286 dòng suy từ tiêu đề rồi đóng dấu như thể
ghi lúc xảy ra — đúng thứ `RM-17` cấm. Cổng thi hành **từ V11062 trở đi**, khoảng trống cũ **ghi
thẳng là thiếu, kèm lý do**.

---

## Đã dựng gì

**`§63` (A61) vào đủ sáu mặt** — `CLAUDE.md` · `.Antigravityrules.md` · `.AGENT.md` (tiếng Anh) ·
`.cursorrules` · `.antigravityrules` · hai mặt sinh regenerate. Nhân tiện sửa `.antigravityrules`
còn ghi `RM-01…RM-20` → **`RM-21`**.

**Công cụ dùng lại** — `_v11062_nang_version.ghi()` cập nhật **bốn mặt một lệnh**:

```
CHANGELOG.md               prepend
CURRENT_TRUTH_SSOT.md      prepend
AUTOMATION_STATE.json      governance_seq += 1
AUTOMATION_HISTORY.jsonl   append          ← mặt vẫn bị quên
```

**Cổng bốn phép**, và **K2 bắt đúng lỗi đã xảy ra**: HISTORY im quá **3 ngày** ⇒ **ĐÃ CHẾT**.

**RM-15 thử chặn:** bỏ 1 mục ⇒ **ĐỎ**; khôi phục ⇒ **XANH**; tệp về nguyên trạng **342.323 byte**.

**Và agent dùng chính công cụ đó để ghi V11062** — nếu nó không tự ghi được chính nó thì nó vô
dụng. `governance_seq 403 → 404`, HISTORY mới **0 ngày tuổi**, cổng **ĐẠT**.

---

## Trạng thái cuối phiên

Production **không đổi** — không deploy, không restart, `QD-041` nguyên vẹn.

Việc tiếp theo owner **đã duyệt**: **`FU-283` hạn 13/08** — đo độ trễ từng model + panel §52.
Bằng chứng cấp bách đo được hôm nay: biên hạn MT **~13 phút kinh niên** trong khi
`deepseek-reasoner` trễ thật **190–197 giây**.

TanPhatAI cần làm: xem mục cuối `REPORT_V11062.md` — năm việc, quan trọng nhất là ③ **CỐ Ý không
bù 286 bản** (đừng ai "sửa" bằng cách bù sau) và ⑤ **prompt ba tầng CHƯA ĐƯỢC PHÉP ĐỌC** (9/96
cặp) — đừng ai suy diễn từ kết quả 1/3 hôm nay.
