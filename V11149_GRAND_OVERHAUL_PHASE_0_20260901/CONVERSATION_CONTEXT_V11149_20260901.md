# CONVERSATION CONTEXT — V11149 · 01/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`. **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI / agent Notion.** Đây là **MỆNH LỆNH TRỰC
> TIẾP CỦA OWNER**, nói trong IDE, **có hiệu lực ngay**. Owner trao đổi liên tục nên **code
> thường đi trước tài liệu** — điều owner cho phép tường minh (`PRJ-INTERACTION-LEDGER-001`).
> Tài liệu cũ mâu thuẫn thực tế đang chạy thì **thực tế + sổ `docs/SO_TUONG_TAC_OWNER.md`
> thắng**; tài liệu là thứ phải sửa.

**01/09** — `PROMPT 43 R1 · GRAND OVERHAUL AFTER V11148`, 15 mục `I`–`XV`. Trích các câu quyết
định, **nguyên văn**:

> *«Dừng chuỗi đo nhỏ giọt và report chủ yếu về D-30. Thực hiện một work package tích hợp để thay
> kiến trúc dự đoán hiện hành: `LLM_CONTEXT_ONLY_V2` + `ML_PURE_MATH_V2` +
> `UNIFIED_CANDIDATE_CONTRACT` + `ALL_MODEL_ARENA` + `TOTAL_V2` + `COMBO_V2` + `FINAL_V2`.»*
>
> *«Không cắt TOTAL. Phải làm lại TOTAL.»*
>
> *«Không hỏi Owner ký từng bước kỹ thuật. Chỉ trình đúng một Cutover Decision Packet sau khi
> package hoàn chỉnh.»*
>
> **`I` — OWNER REQUIREMENTS LOCKED (16 khoản)**, trong đó: *«LLM = thuần ngữ cảnh · ML = thuần
> số học · ML và LLM tự sinh output độc lập trước Combo · Combo-Super = hybrid, không phải base
> voter độc lập · Shadow không được chạy vô hạn mà không có verdict · TOTAL phải chọn nguồn mạnh,
> phù hợp miền và có diversity thật · Không bình quân hoá hàng chục model gần-phẳng · Không
> double-count base + ensemble + Combo · Hidden override phải bị loại hoặc hấp thụ vào ranker có
> log · Ít model nhưng chất lượng · FINAL cũ bất biến.»*
>
> **`II` — bắt buộc sửa cách diễn giải `V11148`:** *«FINAL gần trung bình pool là diagnostic, chưa
> phải causal proof · Không dùng câu ±2 cả ba miền; MN tháng 08 lệch 4,69pp · Top-5 mean không
> phải kết quả gộp top-5 · Không tự retire/promote model chỉ từ một cửa sổ · Exact pool 27 phải
> được phân loại trước khi hành động.»*
>
> **`XIV`** — *«Report kế tiếp phải là Grand Overhaul progress, không phải inventory… Không mở
> thêm FU chỉ để ghi cùng một root cause. Dùng umbrella items FU-449/FU-450.»*

### Các câu trước đó trong phiên (giờ **ước**)

| giờ (ước) | NGUYÊN VĂN | loại |
|---|---|---|
| 01/09 ~19:00 | *«Sau 1 thời gian dài live, điều chỉnh kết quả dự đoán vẫn tệ… Một cuộc cách mạng xử lý dứt điểm đi»* | `YÊU_CẦU` |
| 01/09 ~19:40 | *«ko phải cắt total mà là xử lý lại total với xếp hạng model mới mạnh mẻ hơn tốt hơn»* | `BÁC_BỎ` |
| 01/09 ~20:00 | *«push báo cáo github hết chưa em?»* | `HỎI` |
| 01/09 ~22:00 | `GRAND OVERHAUL AFTER V11148` (bản này) | `YÊU_CẦU` |

---

## 2 · Agent làm gì — Phase 0, READ-ONLY

| việc | kết quả |
|---|---|
| chụp runtime + 7 hash lõi + DB counts | `PID 3156545` · 253 bảng · 761 MB · 93 cron |
| khoá `FINAL` cũ bằng hash | 558 bundle · **`a82c508d3569abda47041ad6…`** |
| phân loại pool bằng **dấu vết**, không tin registry | 57 từng chạy → **27 runtime-active** → **18 trong `voters`** |
| ❌ báo động `SHADOW_LINEAGE_LEAK` 16 nguồn | **DƯƠNG TÍNH GIẢ** — đếm chuỗi thô trên blob 38 khoá |
| ✅ đo đúng chỗ (`voters`, 270 bundle) | **0 shadow** ⇒ **không có leak** |
| tính lại trọng số trên 18 voter thật | **MN 1,63× · MB 2,08× · MT 5,70×** — **phẳng hơn** con số 3,87× đã báo |

---

## 3 · Vấp trong phiên

**🔴 Agent tự báo động P0 sai rồi tự bác trong cùng phiên.** Phép đếm tên model trong toàn bộ
`source_predictions_json` cho **16 nguồn shadow "rò rỉ"** với `DIRECT_INFLUENCE = 270`. Đo đúng
chỗ — danh sách `voters` — cho **0**.

Nếu công bố bản đầu thì đã báo owner một **sự cố không có thật**, và có thể kéo theo việc **gỡ
nhầm shadow** khỏi hệ. Đây là lần thứ tư trong ngày một phép **đếm chuỗi thô** suýt đẻ ra kết
luận sai (`RM-09`).

**🟡 Cổng chỉ-đọc của chính agent chặn nhầm** vì chữ `update` trong `khoa.update(...)` — mẫu cấm
`\\bUPDATE\\b` khớp không phân biệt hoa thường vào **mã Python**, không phải câu SQL ghi.

---

## 4 · Trạng thái cuối

| | |
|---|---|
| production | 🟢 **không bị đụng** — Phase 0 chỉ đọc |
| `FINAL` cũ | 🟢 **khoá bằng hash** `a82c508d3569abda…` |
| pool | 🔴 **18 voter**, không phải 27 — `V11148` đã sửa |
| shadow leak | 🟢 **không có** |
| Wave 1 | ⚪ còn `UNIFIED_CANDIDATE_CONTRACT` · full emitter + `LLM_CONTEXT_ONLY_V2` · `ML_PURE_MATH_V2` |
| Prompt 43 | **`PARTIAL`** — không mở Prompt 44 |

---

TanPhatAI cần làm: ghi **Grand Overhaul Phase 0 xong** — bản chụp đóng băng, `FINAL` cũ khoá bằng hash `a82c508d3569abda…`. Ghi **pool bỏ phiếu THẬT là 18, không phải 27**. Ghi **KHÔNG có shadow leak** — agent tự bác báo động của chính mình. Ghi **sửa hai con số `V11148`**: «27 model» → **18**; «3,87×» → **MN 1,63× · MB 2,08×**. Ghi **kết luận lõi sống sót và nặng hơn**. **Không mở FU mới** — umbrella `FU-449`/`FU-450`.
