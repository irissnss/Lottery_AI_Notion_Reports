# CONVERSATION CONTEXT — V11127 · 27/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`.

---

## 1 · Owner nói gì — nguyên văn

Prompt tổng lực lần 40 R1, hiệu lực **27/08/2026 13:15 ICT**:

> *« Đây là prompt THỰC THI TỔNG LỰC, không phải yêu cầu viết thêm kế hoạch hoặc chỉ xuất báo cáo. »*
>
> *« Production DB trên VPS là nguồn dữ liệu chuẩn và mới nhất… Mọi phân tích dự đoán và sức mạnh
> model phải bắt đầu từ production DB trên VPS. »*
>
> *« Code local, Git commit hoặc file nằm trên VPS chưa chắc đang được production sử dụng. Chỉ
> được gọi code là "đã deploy/đang chạy" nếu chứng minh đủ: đúng service; đúng PID; đúng command
> line; đúng working directory; đúng imported module path; đúng byte hash của code/config được
> tiến trình nạp… »*
>
> *« Không được trả `CODED_NOT_DEPLOYED` nếu đang ngoài block, đủ thời gian và full gate PASS. »*
>
> *« Kết quả một ngày chỉ mang nhãn `DAILY_OBSERVATION_ONLY`. Cấm dùng một ngày để cắt/promote model. »*
>
> *« Thiếu lực thì ghi `INSUFFICIENT_POWER`. Không được đổi thành "model vô dụng". »*
>
> *« Giữ `lstm` riêng cho tới khi có gate khác. »*
>
> *« Cấm chạy im lặng dài. Cấm tuyên bố có công việc đang chạy nền nếu không thực sự có tiến trình.
> Cấm kết luận DONE chỉ vì đã viết report. »*
>
> *« Không bắt Owner thức khuya ký từng deploy thông thường. »*

---

## 2 · Agent làm gì — theo chặng

| chặng | việc | kết quả |
|---|---|---|
| 1a | kiểm giờ + cửa deploy | **13:24**, ngoài block, còn **2h06p** |
| 1b | chứng minh runtime | PID **2341779** · chạy từ **23/08 22:29** · `NRestarts=0` |
| 1c | tìm production DB | `lottery_ai.db` **770 MB**, sửa **1 phút trước** |
| 2 | đọc DB | 253 bảng · 4 bảng khoá đủ · độ tươi ghi nhận |
| 3a | chấm 26/08 | ba miền **LOSE** |
| 3b | chấm lại **có lọc** | tách **33** bản ghi shadow · nền **33 %** |
| 4 | diff bốn mặt | 9 khối, **9/9 đều là FU-438** |
| 5 | **deploy FU-438** | PID → **2642376** · sáu endpoint **200→401** |
| 6 | xác minh | tìm ra **route thứ bảy** đang lộ |
| 7 | **deploy vá 2** | PID → **2646084** · route thứ bảy **401** |
| 8 | snapshot `PRE_RESULT` | **41** model · `PRE_RESULT_VALID` ×3 |
| 9 | auto-scorer | **21/21** · phát hiện **chưa cuốn chiếu** |
| 10 | sức mạnh ML/LLM | nền **33,6 %** · **0 model trên nền** |
| 11 | phát hành | báo cáo này |

---

## 3 · Vấp ở đâu — kể cả vấp do chính agent gây ra

### V1 · 🔴 Agent trộn 33 bản ghi shadow vào bảng chấm

Bảng chấm 26/08 đầu tiên tính **cả `shadow_auto_eval`** — đúng điều
`PRJ-SELECTION-WINDOW-001` mục 2 cấm. Tự bắt được khi rà lại `run_source`, đã tách ra và chỉ
công bố bảng đã lọc.

**Hậu quả nếu bỏ qua:** bảng *"model nào mạnh"* sẽ trộn lượt đánh giá lại với lượt chọn thật —
tức lấy kết quả đã biết để chấm chính mình.

### V2 · 🔴 Agent suýt công bố *"nhiều model có top-1 đúng"* mà **không có nền**

Bảng đầu cho thấy 16 model có top-1 đúng ở đâu đó. Nghe như phát hiện lớn. Nhưng đo nền thì
**33/100 số về mỗi ngày** ⇒ một lựa chọn ngẫu nhiên trúng **33 %**, và với 16 model thì kỳ vọng
~5 model *"đúng"* mỗi miền **thuần do may**.

Đó **đúng bằng** những gì quan sát được. Không có gì để kết luận.

### V3 · 🔴 Một truy vấn trả **`0/0`** và suýt thành *"scorer không chạy"*

Truy vấn nhiều dòng qua SSH bị hỏng, trả rỗng. Nếu tin, kết luận sẽ là *«không có bằng chứng tự
chấm»* — **ngược hẳn sự thật**.

Chạy đối chứng theo `RM-15`: `46` kết quả 7 ngày, `268.933` dòng `scheduler_logs` ⇒ bộ đọc
**hoạt động**. Viết lại truy vấn một dòng thì ra **21/21 lượt tự chấm**.

### V4 · 🔴 Bộ quét của agent báo **14 route nhạy cảm**, xác minh còn **1**

Nhãn *"nhạy cảm"* gắn theo **từ khoá** trong thân hàm nên bắt cả route chỉ **nhắc** thuật ngữ.
Hỏi đúng câu — *route này có trả trường chứa số không* — thì còn **2**, và phân định tiếp thì
chỉ **1** lộ thật.

**Hậu quả nếu bỏ qua:** kế hoạch khoá rộng gấp 14 lần thực tế, nhiều khả năng làm vỡ caller nội bộ.

### V5 · 🔴 `/api/status` suýt bị báo nhầm là lỗ hổng

Bộ quét bắt `main_numbers`. Nhưng đọc **dữ liệu thật** thì mọi trường `date` là **`2026-06-07`**
— đóng băng đúng ngày viewer freeze, đúng `QD-050` đã ký. **Không phải lỗ hổng.**

Nếu không đọc dữ liệu mà chỉ đọc tên trường, agent sẽ đi sửa một thứ đang đúng.

### V6 · 🔴 Diff đầu tiên cho *"production có 21.730 dòng local không có"*

Nghe như production đã đi trước rất xa. **Sai** — VPS dùng **CRLF**, local dùng **LF**, nên diff
coi **mọi dòng** là khác. Chuẩn hoá xuống dòng thì còn **8 khối**, và 10 dòng *"chỉ có ở
production"* hoá ra là **bản cũ của chính những dòng local sửa**.

Nếu tin bản diff đầu, agent sẽ **không dám deploy** vì sợ xoá mất 21.730 dòng của production.

### V7 · Tên cột đoán sai

Truy vấn dùng `target_date`; cột thật là `date`. Đã tra `pragma_table_info` thay vì đoán tiếp
(`RM-10`).

---

## 4 · Điều agent **không** làm, và vì sao

| không làm | vì sao |
|---|---|
| ghi vào production DB | mọi truy vấn `-readonly`, thêm lớp chặn từ khoá ghi phía client |
| đụng `/api/status` | `QD-050` đã ký và dữ liệu **đóng băng đúng** — sửa là phá thứ đang đúng |
| migrate 34 script credential | cần cổng riêng; code sẵn ở `V11126` |
| áp patch `OD-05` / tắt mật khẩu / restart SSH | `RECOVERY_PATH` còn `NOT_VERIFIED` — CLASS C |
| xoay credential thật | CLASS C |
| promote hay retire model nào | chưa có effect · cỡ mẫu · power · stop rule · gate đăng ký trước |
| hard-collapse `lstm` | Owner khoá giữ riêng |
| kết luận *"model vô dụng"* | `RM-04` — `INSUFFICIENT_POWER` ≠ *"kém"* |
| dùng Notion làm nguồn | cấm tường minh |
| push code kho riêng | commit chỉ trên nhánh local |
| chạy im lặng dài | báo tiến độ từng chặng |

---

## 5 · Trạng thái cuối

| | |
|---|---|
| `FU-438` | 🟢 **`RUNTIME_PROVEN`** — 7 endpoint, đo trên production |
| production DB | **không ghi một dòng nào** |
| prediction / FINAL | **không drift** |
| credential · SSH · hook · Notion · visibility | **KHÔNG ĐỔI** — cả năm |
| snapshot 27/08 | `PRE_RESULT_VALID` ×3 |
| auto-scorer | `PROVEN`, nhưng **chưa cuốn chiếu** |
| sức mạnh model | **0/17** model trên nền — `INSUFFICIENT_POWER` |

---

TanPhatAI cần làm: ghi nhận **`FU-438` đã `RUNTIME_PROVEN`** và có **route thứ bảy** ngoài sáu route trong sổ; mở mục cho **scorer chưa cuốn chiếu từng miền**. Ghi rõ vào SSOT rằng **production trước 27/08 chạy code từ 23/08**, nên mọi câu *«đã code ADMIN_ONLY»* trong báo cáo trước phải đọc là **chưa deploy**. **Điều phải ghi đậm nhất:** nền ngẫu nhiên **33,6 %** vs model **32,3 %** vs FINAL bạch thủ **33,0 %** — **trùng nhau**, `z = −1,06`, **không model nào** có khoảng tin cậy trên nền. **Đừng** đọc thành *«model vô dụng»*; nhãn đúng là **`INSUFFICIENT_POWER`**. **Đừng** mượn con số này sang Xiên/3-càng — thước khác (`RM-21`). Chấm 26/08 là **`DAILY_OBSERVATION_ONLY`**.
