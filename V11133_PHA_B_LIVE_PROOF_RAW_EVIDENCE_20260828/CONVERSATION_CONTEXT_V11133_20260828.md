# CONVERSATION CONTEXT — V11133 · 28/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`.

---

## 1 · Owner nói gì — nguyên văn

**~09:20** — yêu cầu trực tiếp trong IDE:

> *« Xem tiếp báo cáo và tổng kết dùm anh »*

**~09:30** — lệnh tổng lực tiếp tục prompt 43 R1:

> *« AFTER V11132 · CLOSE PHA B · COMPLETE A3 · EXECUTE A4→A6 · VERIFY SCORER. Không mở Prompt 44.
> Không plan-only. Không dừng sau khi phát hành report. Không chuyển việc kỹ thuật Agent tự xử được
> sang Owner. »*
>
> *« V11133 phải chứa raw evidence, không chỉ phần tổng kết. »*
>
> *« Chứng minh shadow rows sinh trước hay sau từng Combo bundle; không lấy timeline MN suy thành
> MT/MB. »*
>
> *« Không dùng total_models làm danh sách vì total_models là số đếm int, không phải model set. »*
>
> *« Negative control: shadow contribution phải được đếm từ canonical join, không grep chuỗi
> "shadow". »*
>
> *« Chỉ nâng bộ lọc V11130 thành RUNTIME_PROVEN nếu chứng minh được: byte patch đang được PID
> production nạp · scheduled Combo run thật đã gọi đúng patched path · eligibility của scheduled
> path có official sources và 0 shadow · output/FINAL không drift. Không chỉ gọi module bằng một
> Python process riêng. »*
>
> *« source_weights={} và meta={} không chứng minh production dùng 0 model. Nó chỉ chứng minh
> trường observability đó rỗng. »*
>
> *« Không nói production thật đã chạy với 0 model. »*
>
> *« Báo tiến độ: ĐANG LÀM → ĐÃ XONG → EVIDENCE → VIỆC KẾ. »*

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| xác minh `V11133` chưa tồn tại | HEAD công khai `afa35cc` — đúng, chưa có |
| POST snapshot runtime | PID `2694667` = PRE · `NRestarts=0` · health 200 · 0 lỗi log |
| đọc header `.pyc` | src mtime `1787845974` · size `137520` — **khớp chính xác** nguồn |
| dựng chuỗi thời gian | nguồn 22:52:54 → pyc 22:52:55 → tiến trình 22:53:01 |
| truy log lượt scheduled | `RUN_ID MN_2026-08-28_76f85e02` · `success=9 errors=0` · **0 shadow** |
| phép vi sai bộ lọc | **27 → 16** · 11 shadow bị loại · **cả ba miền** |
| timeline từng miền | MN đủ · **MT/MB chưa tới lượt**, ghi rõ, không suy |
| eligibility structured | 3 miền · 16 · 0 shadow · 4 ML · 8 LLM · **PASS** |
| contribution trace canonical | 40 bundle · **871 component** · 871 khác 0 · **0 shadow** |
| `partial_bonus_shadow` | `OBSERVABILITY_ONLY` · `NO_SCORE_EFFECT` |
| 🔴 tự bắt một kết luận sai | *«scheduler_logs không có dòng nào»* → thật ra **75 dòng** |
| A3 / A5 / A6 | 🔄 sáu luồng đo chạy nền |

---

## 3 · Vấp ở đâu — kể cả vấp do chính agent gây ra

### 🔴 V1 · Suýt công bố một kết luận SAI về hạ tầng

Truy vấn `scheduler_logs` cho cửa sổ 05:00 trả **rỗng**. Tôi in ra
*«(THỰC SỰ không có dòng nào)»* — và nếu để yên, nó vào báo cáo thành *«đường scheduled không ghi
log»*, tức là **đúng cái mắt xích mà owner nói thiếu thì phải giữ `RUNTIME_LOADED`**.

**Sự thật ngược hẳn:** cửa sổ đó có **75 dòng**, trong đó **26 dòng `ai_predict`** — và chính 26
dòng ấy là **mắt xích số 4** tôi tìm cả buổi. Nếu tin con số rỗng, tôi đã **hạ cấp verdict một cách
sai**, và tệ hơn là đã ghi vào báo cáo một mô tả sai về hệ thống.

**Nguyên nhân gốc:** truy vấn tham chiếu cột **`status`** — bảng đó **không có** cột này (cột thật:
`id, log_time, log_level, message, job_name, region, date_str`). `sqlite3` báo lỗi **ra `stderr`**,
mà hàm đọc của tôi **chỉ lấy `stdout`** ⇒ lỗi bị nuốt, trả chuỗi rỗng, **không triệu chứng**.

**Bắt được nhờ đâu:** một phép đếm khác cho `2026-08-27 22 UTC | 256` dòng — **mâu thuẫn trực tiếp**
với "không có dòng nào". Hai con số ngược nhau trong cùng một phiên là dấu hiệu bắt buộc dừng lại.

**Đã sửa:** hàm đọc SQL nay **in cảnh báo khi `stderr` khác rỗng**. Cùng họ với lỗi `CLAUDE.md` đã
ghi (*«SQL nhiều dòng qua SSH trả 0 dòng im lặng»*) — cùng cơ chế im lặng, khác nguyên nhân.

### 🟡 V2 · Ba lỗi kỹ thuật nhỏ, không ảnh hưởng kết luận

- `tr '\0'` — Python dịch `\0` thành **ký tự null thật**, `CreateProcess` trên Windows từ chối chạy.
- `stat -c %%Y` không qua `%`-format nên shell nhận `%%Y`, in ra chữ `%Y`.
- `datetime(log_time,'+7 hours')` trả `NULL` làm **cả dòng ghép thành `NULL`**, in ra rỗng.
- Heredoc bash vấp ký tự đặc biệt khi ghi tệp báo cáo lớn — chuyển sang ghi tệp trực tiếp.

### 🟡 V3 · Một chỗ chưa truy tới cùng, ghi `NOT_VERIFIED`

PRE ghi `MB:61:WIN`, POST đọc `MB:61:ACTIVE`. Kiểm ra `final_bundles.status` **chỉ có** `ACTIVE`,
còn `predictions.combo-super` 27/08 là `PARTIAL/LOSE/PARTIAL` — **không khớp** `WIN/LOSE/WIN`.
Nhiều khả năng PRE đọc `bach_thu_status`, **chưa xác minh xong**.

Điều **đã** xác minh và mới là phép kiểm bất biến thật: `bach_thu` **không đổi**
(`MB=61 MN=61 MT=68` ở cả PRE lẫn POST).

### 🟢 V4 · Vì sao phải làm phép vi sai chứ không dừng ở *«0 shadow»*

*«Eligibility có 0 shadow»* một mình **không** chứng minh bộ lọc chạy — nó cũng đúng nếu bộ lọc bị
vô hiệu mà tình cờ không model shadow nào đủ tư cách. Đúng cái bẫy `V11130` đã sập (`RM-15`).
Phép vi sai `27 → 16` mới **phân biệt được hai khả năng**.

---

## 4 · Điều agent **không** làm, và vì sao

| không làm | vì sao |
|---|---|
| deploy / restart | không cần, và không được đổi official path khi cổng chưa tách lớp |
| deploy cổng `_v11132` | cổng **chưa tách ba lớp** — deploy sai lớp còn hại hơn |
| ghi *«production chạy 0 model»* | owner cấm, và log ghi `expected_models=9 success=9` |
| suy timeline MT/MB từ MN | owner cấm; hai miền **thật sự chưa chạy** lúc đo |
| ghi tuyệt đối *«shadow không bao giờ đổi FINAL»* | chỉ được nói trong **cửa sổ 14 ngày quan sát** |
| đổi tên `partial_bonus_shadow` | trường này nằm trong JSON đã lưu hơn 40 bundle, phải rà reader trước |
| hỏi Owner về `meta-learning` | packet vẫn chưa đủ 5 phần |
| ghi *«PHA A DONE»* | A4/A5/A6 còn OPEN |

---

## 5 · Trạng thái cuối

| | |
|---|---|
| mutation official path | **KHÔNG CÓ** — PID và 4 hash khớp PRE |
| **PHA B** | 🟢 **DONE** — bốn mắt xích đủ, kèm đối chứng dương |
| bộ lọc shadow `V11130` | 🟢 **`RUNTIME_PROVEN`** (kèm giới hạn ghi rõ ở mục 11 báo cáo) |
| A1 · A2 · A3 (một phần) · cổng | 🟢 DONE |
| A4 · A5 · A6 · tách ba cổng | 🔴 **OPEN** |
| scorer 28/08 · timeline MT/MB | ⏳ **WAIT_LIVE** |
| `SHADOW_CHANGED_FINAL` | **`FALSE_IN_OBSERVED_14D_WINDOW`** |

---

TanPhatAI cần làm: ghi **`PHA_B_DONE`** kèm bốn mắt xích runtime và **phép vi sai `27 → 16`** (đối chứng dương chứng minh bộ lọc không vô hiệu, giống hệt ba miền, 11/11 bị loại là shadow). Ghi **`SHADOW_CHANGED_FINAL = FALSE_IN_OBSERVED_14D_WINDOW`** và **`NO_OBSERVED_SHADOW_SCORE_CONTRIBUTION_14D`** — **không** ghi tuyệt đối; giữ riêng **`SHADOW_ENTERED_COMBO_ELIGIBILITY_PATH = TRUE_BEFORE_PATCH`**. Ghi **đính chính của Agent**: *«scheduler_logs không có dòng nào cho lượt 05:00»* là **SAI**, thật ra **75 dòng** — lỗi do truy vấn dùng cột `status` không tồn tại và `stderr` bị nuốt; nếu tin con số rỗng thì đã **hạ cấp verdict sai**. Ghi **`total_models` là `int`**, **`source_weights={}` là `OBSERVABILITY_MISSING`**, **`partial_bonus_shadow` không liên quan model shadow**. Trạng thái tổng thể vẫn **`PHA_A_PARTIAL`** — A4/A5/A6 còn OPEN. **Không mutation official path.**
