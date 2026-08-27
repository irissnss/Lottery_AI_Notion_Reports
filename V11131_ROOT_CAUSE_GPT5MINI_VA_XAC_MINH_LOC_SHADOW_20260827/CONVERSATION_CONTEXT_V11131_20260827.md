# CONVERSATION CONTEXT — V11131 · 27/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`.

---

## 1 · Owner nói gì — nguyên văn

Prompt tổng lực lần 43 R1, hiệu lực **27/08/2026**:

> *« Không mở Prompt 44. Không quay lại kiểm tra mâu thuẫn 17/16 vì V11130 đã giải quyết: roster
> official đúng là 17. Không dừng ở plan/audit/report-only. »*
>
> *« Bắt đầu ngay PHA A; không chờ 05:00 và không thay official path trước phép kiểm live. »*
>
> *« Chỉ ghi `SHADOW_ENTERED_COMBO_PATH`. Không ghi `SHADOW_CHANGED_FINAL` nếu chưa có marginal
> contribution trace. »*
>
> *« Không gọi việc mất Combo eligibility là "đã cắt model". Mất Combo eligibility không đồng
> nghĩa rời direct FINAL. »*
>
> *« Với LLM official: 8 KEEP. gpt-5-mini NOT_VERIFIED cho tới khi audit xong. Cấm ghi "9 LLM
> còn lại KEEP" trước evidence. »*
>
> *« Điều chưa chứng minh phải ghi `NOT_VERIFIED` + thiếu bằng chứng gì + Agent lấy bằng chứng ở
> đâu + ảnh hưởng nếu chưa xác minh. »*
>
> *« Không hỏi Owner về meta-learning khi packet chưa đủ. »*

---

## 2 · Agent làm gì

| pha | việc | kết quả |
|---|---|---|
| A1 | PRE snapshot | hash `085d4979…` · giờ máy chủ 23:27:23 |
| — | 🔴 tự phát báo động rồi tự bác | *«0 model dự tuyển»* → **sai**, lỗi script đo |
| — | phát hiện cổng `V11130` hỏng | `SHADOW_CON_LAI []` **đúng vô nghĩa** khi dict rỗng |
| — | xác minh lại bản vá | 🟢 **16 dự tuyển · 0 shadow · `gpt-5-mini` False** |
| A2 | root cause `gpt-5-mini` | 🔴 **shadow từ 01/08** — 100 % `shadow_auto_eval` 26 ngày |
| A2 | verdict | **`ALREADY_SHADOW_NO_ACTION`** |
| — | 🔴 đính chính roster | **16 official**, không phải 17 — `V11130` sai |
| — | phân định shadow trong FINAL blob | chỉ ở `model_wr`/`model_bt`, **không** trong `score_breakdown` |
| B | live proof | ⏳ **`WAIT_LIVE`** — 05:00 ngày 28/08 |

---

## 3 · Vấp ở đâu — kể cả vấp do chính agent gây ra

### V1 · 🔴 Tôi tự phát một báo động nghiêm trọng, rồi tự bác nó

Script A1 báo `_ti_le_bach_thu` trả **0 model ở cả ba miền** — tức bản vá `V11130` đã làm rỗng
bảng dự tuyển và sẽ **làm hỏng Combo lúc 05:00**.

Chạy lại không cắt output: **`LEN 16`**, đủ 16 model, 0 shadow. Regex của tôi không khớp vì dòng
`[INIT]` chen vào stdout.

**Trình tự đúng đã được giữ:** nghi ngờ → **xác minh** → mới kết luận. Nếu tôi báo ngay khi thấy
số 0, Owner sẽ nhận một báo động sai giữa đêm.

### V2 · 🔴 Và điều nghiêm trọng thật nằm ở chỗ khác: **cổng deploy `V11130` đã cho qua RỖNG**

Ở `V11130` tôi kiểm bằng `"SHADOW_CON_LAI []" in output`. Điều kiện đó **đúng một cách vô nghĩa**
nếu dict rỗng — nó **không phân biệt được** *«đã loại shadow»* với *«mất sạch mọi model»*.

Lần này bản vá tình cờ đúng. Nhưng nếu nó sai, cổng của tôi **vẫn báo xanh** và tôi đã deploy một
thay đổi làm hỏng Combo mà không biết.

**Đúng `RM-15`.** Bài học thành luật: **mọi cổng loại-trừ phải kèm ĐỐI CHỨNG DƯƠNG** — không chỉ
hỏi *«cái xấu đã biến mất chưa»* mà phải hỏi *«cái tốt có còn không»*.

### V3 · 🔴 `gpt-5-mini` — tôi đã đếm nhầm nó thành official ở `V11130`

Phép đếm dùng cửa sổ **30 ngày** với `run_source IN (auto_daily, ai_chain)`. Đo lại theo **thời
gian** thì các dòng đó nằm ở **28/07–01/08** — tức **rìa cửa sổ**. Từ **01/08** tới nay nó
**100 % `shadow_auto_eval`**.

⇒ **Roster official đúng là 16, không phải 17.**

Điều này **không phải mở lại tranh luận 17/16** mà Owner đã khoá — nó đổi **verdict**: từ
*«official cần audit»* thành **`ALREADY_SHADOW_NO_ACTION`**, tức **không có gì để rút, không có
gì để thay**. Tôi buộc phải báo vì Owner khoá con số 17 **dựa trên chính báo cáo sai của tôi**.

Và trớ trêu: **`V11128` ghi 16 — tình cờ đúng**, nhưng bằng lập luận sai (nhãn `n < 30`). Tôi đã
bác nó ở `V11130` bằng một lập luận cũng sai.

### V4 · 🔴 Suýt báo một sự cố nghiêm trọng **không có thật**

Thấy **11 model shadow** có tên trong `source_predictions_json` của **cả ba** bundle FINAL 27/08,
phản xạ đầu là: *«shadow đang vào FINAL hàng loạt»*.

Đọc kỹ cấu trúc thì các khoá gồm `quality_filtered_models` và `diagnostic_empty_models` — tức
blob này **ghi cả model bị LOẠI**. Truy tiếp:

| mục | có shadow không |
|---|---|
| `total_models` (tập bỏ phiếu) — 13–15 | — |
| `score_breakdown` (**đóng góp điểm thật**) | 🟢 **KHÔNG** |
| `model_wr` / `model_bt` (**bảng thống kê 30 model**) | 🔴 có 11 |

Câu hỏi đúng **không phải** *«tên có xuất hiện không»* mà *«nó nằm ở mục nào»*. Nếu dừng ở câu
hỏi sai, tôi đã báo một sự cố không tồn tại và có thể kéo theo một đợt rollback vô cớ.

---

## 4 · Điều agent **không** làm, và vì sao

| không làm | vì sao |
|---|---|
| deploy / restart bất cứ gì | Owner: *«không thay official path trước phép kiểm live»* |
| nâng `RUNTIME_PROVEN` | lượt sinh 05:00 chưa tới ⇒ `WAIT_LIVE` |
| ghi `SHADOW_CHANGED_FINAL` | `score_breakdown` **không** chứa shadow ⇒ không có marginal trace |
| gọi `gpt-5-mini` là *«đã cắt»* | nó **đã ở shadow 26 ngày**; mất Combo eligibility ≠ rời direct FINAL |
| ghi *«9 LLM còn lại KEEP»* | Owner cấm trước evidence — nay đúng là **8 KEEP** + `gpt-5-mini` shadow |
| hỏi Owner về `meta-learning` | packet chưa đủ (thiếu marginal impact) — **rút lại** câu hỏi ở `V11130` |
| ghi vào production DB | mọi truy vấn `-readonly` |

---

## 5 · Trạng thái cuối

| | |
|---|---|
| mutation | **KHÔNG CÓ** |
| runtime | `main.py` `ec254033…` · `scheduler.py` `a6c8bfff…` · `combo_super.py` `47047b1d…` |
| MainPID | **2694667** · health **200** |
| bản vá lọc shadow | **`RUNTIME_LOADED`** · xác minh **16 dự tuyển, 0 shadow** |
| roster official | **16** *(đính chính từ 17)* |
| `gpt-5-mini` | **`ALREADY_SHADOW_NO_ACTION`** — shadow từ 01/08 |
| live proof | ⏳ **05:00 ngày 28/08** |

---

TanPhatAI cần làm: ghi đính chính **`gpt-5-mini` đã rời official từ `2026-08-01`** (100 % `shadow_auto_eval` 26 ngày, output hoàn hảo 93 dòng/0 rỗng/0 late) ⇒ **`ALREADY_SHADOW_NO_ACTION`**, và **roster official đúng là 16 chứ không phải 17** — con số 17 ở `V11130` là **lỗi của Agent** do cửa sổ 30 ngày chạm đuôi giai đoạn official cũ. Ghi rằng đây **không phải mở lại tranh luận 17/16** mà là đổi **verdict** của một model. Ghi **giới hạn kết luận shadow**: 11 model shadow chỉ nằm trong **bảng thống kê** `model_wr`/`model_bt`, **không** trong `score_breakdown` ⇒ giữ `SHADOW_ENTERED_COMBO_PATH`, **cấm** `SHADOW_CHANGED_FINAL`. Ghi **bài học cổng**: cổng deploy `V11130` **cho qua rỗng** — mọi cổng loại-trừ từ nay **phải kèm đối chứng dương**. Câu hỏi về `meta-learning` ở `V11130` đã **rút lại**, sẽ trình khi có số đo. **Phiên này không mutation gì cả.**
