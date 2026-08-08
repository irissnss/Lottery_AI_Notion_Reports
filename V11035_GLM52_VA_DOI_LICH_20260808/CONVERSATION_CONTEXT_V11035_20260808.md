# CONVERSATION CONTEXT — V11035 · 2026-08-08 tối

## Owner nói gì (NGUYÊN VĂN)

> Model Ai GLM 5.2 lỗi không dự đoán MB em kiểm tra xử lý chưa em? Dời lịch để đo chứ em

## Owner đúng, và câu hỏi đó lôi ra thứ lớn hơn nhiều

`glm-5.2` **có thật** (89 lượt/30 ngày, model **shadow**), và hôm nay **ra `[]` ở MB** trong khi
MN và MT vẫn ra số bình thường.

**Vì sao agent không tự thấy:** báo cáo V11034 vài giờ trước quét lượt rỗng với mệnh đề
`COALESCE(run_source,'') <> 'shadow_auto_eval'` — **lọc mất toàn bộ model shadow**. Agent báo
*"5 lượt rỗng trong 30 ngày"*.

**Số thật khi không lọc: 44/2.383 lượt = 1,8%, 15 model.** Nặng nhất **`gemma-4-31b` 17/58 =
29,3%** — gần một phần ba số lượt của nó không trả về gì.

## Và lỗi thật nằm sâu hơn: lượt rỗng bị chấm thành THUA

Kiểm `model_daily_eval` × `predictions`: mọi lượt rỗng **đều có dòng chấm điểm**, ghi
`status='LOSE' · bt_hit=0 · pick_count=0` — **y hệt model đã đoán mà sai**.

Tính lại bằng cách loại lượt rỗng:

| model | rỗng | điểm đang ghi | **điểm thật** | bị dìm |
|---|---|---|---|---|
| `gemma-4-31b` | 29,3% | 17,2% | **24,4%** | **+7,1** |
| `qwen3-max-thinking` | 8,0% | 29,9% | **32,5%** | +2,6 |
| `gemini-3.5-flash` | 4,8% | 36,1% | **38,0%** | +1,8 |

**Vì sao nặng:** đây là ứng viên đang chấm để **THĂNG HẠNG** (FU-192, FU-290). Một model bị loại
vì *"yếu"* có thể chỉ là **hay lỗi API** — hai bệnh khác hẳn, cách chữa khác hẳn.

Cách chấm đúng phải tách **ba** trạng thái: `WIN` · `LOSE` · **`NO_ANSWER`** — `NO_ANSWER`
**không vào mẫu số** tỉ lệ trúng, mà đếm riêng làm **chỉ số độ tin cậy vận hành**.

**Agent KHÔNG sửa.** `model_daily_eval` là **1 trong 4 bảng khoá**, bộ chấm thuộc production,
`QD-041` khoá tới 21/08. Và sửa cách chấm là **đổi định nghĩa của mọi con số lịch sử** — cần
chữ ký owner, không phải quyền của agent. Mở **FU-355**.

## Việc thứ hai: dời lịch — QD-045

Owner nói *"Dời lịch để đo chứ em"*. Agent ghi **QD-045**:

| mã | mốc khởi động |
|---|---|
| `QD-015` shadow MT bạch thủ = random-forest đơn | 08/08 → **21/08** |
| `QD-016` bỏ lệnh bắt buộc chọn từ danh sách trên luồng bóng | 08/08 → **21/08** |
| `QD-017` chạy hai prompt song song trên cùng model | 08/08 → **21/08** |

**Chọn 21/08 chứ không ngày khác:** trùng **mốc mở khoá QD-041** và **mốc chốt FU-284** — một
cửa sổ phục vụ cả ba phép đo, thay vì ba lần làm bẩn dữ liệu.

**`OD-20260801-B` KHÔNG dời** dù nó cũng ghi «sau 08/08» — vì nó **đã thực thi xong** (6/6 lane
`cron=0`, kiểm hôm nay). Dời một việc đã xong là ghi sai sổ, và phiên sau sẽ đi làm lại việc
không cần làm.

## Điều agent PHẢI NÓI THẲNG: sai HAI LẦN TRONG MỘT NGÀY về cùng một cột

| lần | lỗi | chiều |
|---|---|---|
| 18:40 | đếm 12 lượt 64 ký tự **quên lọc** `run_source` ⇒ tưởng MN official chạy prompt hỏng | **quên lọc** |
| 19:xx | quét lượt rỗng **lọc thừa** `run_source` ⇒ bỏ sót toàn bộ model shadow | **lọc thừa** |

**Cùng một gốc: viết mệnh đề lọc trước khi hỏi rõ câu hỏi đang đo cái gì.**

- Lần một đo *"lượt nào ảnh hưởng bảng điểm official"* ⇒ **phải lọc**.
- Lần hai đo *"model nào hay lỗi"* ⇒ **không được lọc**, vì model shadow cũng là model đang được
  chấm để thăng hạng.

**Và cả hai lần agent đều không tự thấy** — lần một do agent phản biện bắt, **lần hai do owner
hỏi**. Sổ RM có RM-13 (nguồn đo phải là nguồn thật) nhưng **chưa có mục nào về mệnh đề lọc**.
Đề xuất bổ sung khi mở sổ RM lần tới.

## Việc phải nhớ khi deploy cổng canh

Cổng `_v11023_canh_thieu_so.py` (FU-350) khi deploy **phải BỎ mệnh đề lọc `run_source`** —
nếu giữ như hiện tại, nó sẽ bỏ sót **đúng ca `glm-5.2` mà owner vừa bắt**.
