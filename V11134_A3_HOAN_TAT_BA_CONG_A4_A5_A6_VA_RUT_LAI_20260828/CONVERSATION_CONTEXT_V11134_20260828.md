# CONVERSATION CONTEXT — V11134 · 28/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`.

---

## 1 · Owner nói gì — nguyên văn

**~09:20** — *« Xem tiếp báo cáo và tổng kết dùm anh »*

**~09:30** — lệnh tổng lực tiếp tục prompt 43 R1:

> *« AFTER V11132 · CLOSE PHA B · COMPLETE A3 · EXECUTE A4→A6 · VERIFY SCORER. Không mở Prompt 44.
> Không plan-only. Không dừng sau khi phát hành report. Không chuyển việc kỹ thuật Agent tự xử được
> sang Owner. »*
>
> *« Không ghi "13/18 model thực sự được đếm hai lần vào FINAL". Tạm ghi 13/18
> DUPLICATE_LINEAGE_PATHS. Chỉ nhóm ACTUAL_DOUBLE_COUNT_NONZERO mới được gọi "đếm hai lần thật". »*
>
> *« Không chỉ so CI riêng lẻ. Vì cùng 273 lượt, phải xuất McNemar hoặc paired
> bootstrap/permutation phù hợp. »*
>
> *« 72/273 = 26,4% đổi top-1 chỉ chứng minh architecture sensitivity. »*
>
> *« source_weights={} và meta={} không chứng minh production dùng 0 model. Nó chỉ chứng minh
> trường observability đó rỗng. »*
>
> *« N≥1 official hợp lệ: vẫn output DEGRADED. N=0: mới không output. Cấm lấy SHADOW bù. »*
>
> *« Cổng hiện giữ LOCAL_ONLY / BLOCKED_TECHNICAL_SCHEMA_ALIGNMENT. Không ghi "chờ Owner duyệt". »*
>
> *« Điều gì chưa rõ phải ghi NOT_VERIFIED. »*
>
> *« Báo tiến độ: ĐANG LÀM → ĐÃ XONG → EVIDENCE → VIỆC KẾ. »*

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| phát hành `V11133` đóng PHA B | commit `48a4aa2`, ~10:20 |
| 🔴 **rút lại một câu của chính `V11133`** | 3 ca rò rỉ shadow qua `ai_confirm` |
| rút lại 2 con số của `V11132` | 0 không-phải-dict / 125 rỗng · 145/148 = 98,0% |
| A3 double-count điểm thật | **8/13** · 12,1% điểm · 50% bạch thủ |
| A3 paired McNemar + permutation | **0/10 cặp** có ý nghĩa |
| A3 family dedupe | net +6, p=0,3915, con số **không ổn định** |
| A3 ablation `meta-learning` | n=427, repro 100%, −0,94pp, p=0,4807 |
| 🔴 **đối chứng hằng số** | nền thật 33,87% · **M0 = 30,77% thấp hơn** |
| tách **ba cổng** | **12/12** thử, PASS trên production thật |
| A4 hai lane shadow | persist 3 tệp × 273 bản ghi |
| A5 dump prompt production | MN 50.594 ký tự · 35 khối ô nhiễm |
| A6 ML pure-math | 6/6 ĐẠT · 6,92 (không phải 8,2) |
| định vị nguyên nhân gốc | `combo_super.py:115-116` |

---

## 3 · Vấp ở đâu — kể cả vấp do chính agent gây ra

### 🔴 V1 · Tôi công bố một verdict quá mạnh, và phải rút sau 2 giờ

Sáng nay `V11133` viết *«`SHADOW_CHANGED_FINAL = FALSE_IN_OBSERVED_14D_WINDOW`»* dựa trên
**0/871 component shadow**. Con số đó **đúng** — nhưng nó chỉ nói về **một** kênh
(`components[].model`), còn tôi viết như thể nó nói về **mọi** kênh.

Có **kênh thứ hai**: `gemini-3.5-flash` (shadow) vào chấm điểm của Combo qua nhân tố `ai_confirm`
— **3 lần**, mỗi lần **rơi đúng số được chọn**, weight tới **2.000**. Và **kênh thứ ba**:
`number_voters` trong `predictions.analysis_text`.

**Bài học cụ thể, không phải lời chung chung:** trước khi viết `X = FALSE`, phải **đếm có bao
nhiêu đường X có thể xảy ra**, và nói rõ **đã soi đường nào**. Tôi soi một đường rồi phủ định
toàn bộ.

### 🟡 V2 · Suýt bác nhầm một kết quả ĐÚNG vì đường dẫn họ ghi sai

Một luồng đo báo *«shadow rót điểm official gián tiếp qua combo-super»*, kèm đường dẫn
`number_voters` trong `reasoning_json`. Tôi kiểm hai bảng: **0 dòng**. Suýt kết luận
*«không tái lập được»*.

Trường đó nằm ở **cột thứ ba — `predictions.analysis_text`** — cột tôi chưa soi.
**Đường dẫn họ ghi sai, nhưng kết luận của họ ĐÚNG.**

Bác một kết quả vì đường dẫn sai là một kiểu sai khác, và nó nguy hiểm vì trông giống như đang
cẩn thận.

### 🟡 V3 · Tiêu chí của tôi lỏng hơn cần thiết

Tôi đo double-count bằng «đồng xuất hiện base + aggregator trên cùng số» ⇒ **12** model.
Tiêu chí chặt — truy lineage thật qua `analysis_text['rf_numbers']` — ⇒ **8**.
Đồng xuất hiện **không** chứng minh tín hiệu chảy qua. Lấy **8**.

### 🟢 V4 · Một đối chứng THẤT BẠI lại dẫn tới phát hiện lớn nhất

Luồng A3.3 dựng đối chứng âm «lấy số ít phiếu nhất», kỳ vọng ra âm rõ. Nó **không** ra âm
(p=0,92). Đi truy vì sao ⇒ phát hiện **một hằng số cố định đạt trung bình 33,87%**, cao hơn FINAL
hiện hành (30,77%).

Đối chứng thất bại thường bị bỏ qua. Ở đây nó là thứ có giá trị nhất phiên.

### 🟡 V5 · Bốn lỗi kỹ thuật nhỏ

`tr '\0'` sinh ký tự null thật ⇒ Windows từ chối · `stat -c %%Y` in ra chữ `%Y` ·
`datetime()` trả `NULL` nuốt cả dòng ghép · heredoc bash vấp ký tự đặc biệt khi ghi báo cáo lớn.

### 🟡 V6 · Lỗi các luồng đo tự bắt được

- A6 audit xong trên kho **local** rồi mới đối chiếu hash ⇒ **7/10 tệp ML khác giữa local và VPS**,
  phải chạy lại toàn bộ trên VPS (`RM-13`).
- A3.2 lần dựng đầu dùng `ORDER BY id`, **không** tái lập được biến thể BASE.

---

## 4 · Điều agent **không** làm, và vì sao

| không làm | vì sao |
|---|---|
| deploy sửa `combo_super.py:115-116` hôm nay | MN đã chốt FINAL 05:20, MT/MB chưa chạy — deploy giữa ngày làm **hai pool khác nhau trong một ngày**. Đợi sau 18:15, `effective_from` 29/08 |
| deploy ba cổng | `BLOCKED_TECHNICAL_SCHEMA_ALIGNMENT` — chưa khớp schema thật. **Không** phải «chờ Owner duyệt» |
| ghi «shadow đã đổi FINAL» | chưa chạy lại hàm chấm điểm ⇒ `NOT_EXCLUDED`, không phải `TRUE` |
| ghi «meta-learning có hại» | −0,94pp, CI bao trùm 0; gỡ **bất kỳ** model nào cũng cho delta cùng dải |
| ghi «hệ thống vô dụng» từ đối chứng hằng số | phép đó nói **thước đo không phân biệt được**, không nói hệ vô dụng |
| dùng hằng số tốt nhất `'54'` (43,96%) | chọn **sau** khi biết kết quả = thiên vị |
| nới `main_numbers[:2]` | chưa đo tác động — `RM-07` cấm vá vội |
| hỏi Owner về `meta-learning` | packet vẫn chưa đủ 5 phần |

---

## 5 · Trạng thái cuối

| | |
|---|---|
| mutation official path | **KHÔNG CÓ** — PID 2694667 · 4 hash khớp PRE |
| A1 · A2 · A3 · PHA B · ba cổng · A4 · A5 · A6 | 🟢 **DONE** |
| tệp mới | **3 tệp `LOCAL_ONLY`** + 3 artifact JSONL (không vào Git) |
| `SHADOW_CHANGED_FINAL` | 🟡 **`NOT_EXCLUDED`** — đã rút lại `FALSE` |
| scorer 28/08 · timeline MT/MB | ⏳ **WAIT_LIVE** chiều nay |
| việc chờ sau 18:15 | comment `combo_super.py:115-116` |

---

TanPhatAI cần làm: ghi **RÚT LẠI** verdict shadow của **`REPORT_V11133` (commit `48a4aa2`)** — nhãn đúng là **`SHADOW_ENTERED_COMBO_SCORING_VIA_AI_CONFIRM = TRUE`** (3 ca: 12/08 · 13/08 · 23/08, đều MN, `gemini-3.5-flash`, mỗi ca rơi đúng số được chọn) và **`SHADOW_CHANGED_FINAL = NOT_EXCLUDED`**, **không phải `FALSE`**. Nguyên nhân gốc **`combo_super.py:115-116`**. Ghi **đối chứng hằng số**: trung bình 100 hằng số **33,87%** so với FINAL **30,77%**. Ghi **8/13 `ACTUAL_DOUBLE_COUNT_NONZERO`** (không phải 13/18), **0/10 cặp paired test có ý nghĩa**, **ablation meta-learning 47/427 = 11,0% · −0,94pp · p=0,4807**. Ghi **A5** de-herd nửa vời + `WEEKLY LIVINGNESS` treo 21 ngày, **A6** đa dạng 6,92 và `database.py:2463` cắt mất 54%. **Việc chờ sau 18:15 hôm nay:** comment `combo_super.py:115-116`, `effective_from` 29/08. **Phiên này không mutation official path.**
