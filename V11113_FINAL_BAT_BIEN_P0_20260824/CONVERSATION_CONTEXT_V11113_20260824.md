# CONVERSATION CONTEXT — V11111 · V11112 · V11113 — 24/08/2026

> Ghi **nguyên văn** lời owner, agent làm gì, và **vấp ở đâu**. Không diễn giải lại lời owner.

---

## 1 · OWNER NÓI GÌ — NGUYÊN VĂN

**Prompt tổng lực lần 34**, mục VI:

> *«**CẤM đổi mù 300 thành 500**. Phải truy `AI_MODEL_HARD_TIMEOUT_SEC=300` hiện đang: hủy
> request/future; chỉ hết thời gian chờ; hay model vẫn chạy ngầm.»*

> *«Provider/runtime hard timeout là trục khác. **Không được dùng eligibility cutoff để hủy
> model**.»*

Các mục `P0`:

> *«`P0-A` ảnh chụp + diff `v1/v2` **trước MN 15:45**.»*
> *«`P0-B` truy toàn bộ writer/reader.»*
> *«`P0-C` tách CANDIDATE/FINAL/RESULT + máy trạng thái.»*
> *«`P0-E` fallback OFFICIAL với roster đóng băng.»*

Ràng buộc còn hiệu lực từ các prompt trước:

> *«Cấm thay thuật toán mù.» · «Cấm tự quyết thay model, bật PP5, tắt lớp ghi đè MN, đổi publish
> gate hoặc timeout.» · «Cấm đổi ngưỡng sau khi thấy số.» · «Cấm cờ bỏ-qua-cổng.» · «Cấm nuốt
> stderr.» · «Cấm `except: pass`.» · «Cấm hứa tăng tỷ lệ trúng.» · «Cấm gọi `CODE_PUSHED` hoặc
> `DEPLOYED` là `RUNTIME_PROVEN` trước lượt live thật.» · «Agent phân tích mặc định chỉ được
> READ-ONLY.»*

---

## 2 · AGENT LÀM GÌ

**Chặng 1 — `P0-D`, truy `300s`.** Đọc `scheduler.py`, `_v10785_late_fill.py`. Phát hiện
`future.cancel()` **không** giết được luồng đã chạy, và **mã tự ghi nhận điều đó**. Tìm ra bảng
trần riêng từng model và cơ chế late-fill **đã chạy 68 lần** từ 06/07.

**Chặng 2 — `P0-B`, quét writer/reader.** Quét toàn kho, loại thư mục sao lưu chết, phân loại
theo **thao tác SQL**. Ra **đúng hai** câu lệnh ghi. Hai chỗ trông như writer được **phân loại**
là không phải, kèm lý do.

**Chặng 3 — `P0-A`, đọc hai cổng bất biến.** Đọc `save_final_bundle` + `verify_final_bundle`.
Xác nhận writer settlement **không thể** đổi số. Phát hiện nhánh ghi-đè **có** chạm toàn bộ cột
mang dự đoán ⇒ hai cổng là thứ duy nhất chặn.

**Chặng 4 — `RM-15`, dựng thử chặn.** Dựng DB tạm từ đúng lược đồ production, thử **hai chiều**,
**17/17**, DB thật nguyên vẹn từng byte.

**Chặng 5 — `P0-E`, roster.** Tìm ra fallback **hai lớp** đã có. Phát hiện hàm lấy roster
**không có tham số ngày**, và trường ngày **rỗng ở cả 15** model output.

**Chặng 6 — rút lại + ghi bốn mặt + đẩy.** Ba câu sai, rút đủ bốn phần, **đúng chỗ đã công bố**.

---

## 3 · VẤP Ở ĐÂU — ghi hết, không giấu

### 3.1 · Cổng `§63` chặn commit của chính em

Commit đầu gán nhãn `V11111` nhưng **quên ghi `HISTORY`**. Cổng chặn với
`A61_VIOLATION_PARTIAL_BUMP` và in đúng chỗ hỏng:
*«K1: 1 version từ V11062 trở đi KHÔNG có dòng HISTORY: V11111»*.

**Không dùng cờ bỏ qua.** Sửa nguyên nhân bằng `ghi()` đủ bốn mặt, chạy `--kiem` xác nhận
`THIẾU HISTORY: 0`, rồi commit lại. **Cổng làm đúng việc của nó.**

### 3.2 · Suýt kết luận bằng nguồn sai — `RM-13`

Đo `FREEZE-GUARD`/`FREEZE-55` trong bảng log ra **0**, và **suýt** viết *«hai cổng chưa bao giờ
chạy»*. Kịp nhận ra hai cổng dùng `print()` ⇒ ra journald, **không** vào bảng log.
**Nguồn sai thì mọi kết luận sai.** Đổi sang journald rồi mới đo.

### 3.3 · Đoán tên bảng — `RM-10`

Thử bốn tên bảng roster theo suy đoán, **cả bốn không tồn tại**. Phải quét mã tìm đường thật.
Đúng bài học *«`ml_train.py`/`meta_train.py` không tồn tại»*.

### 3.4 · Suýt nói *«dữ liệu để vá đã có sẵn»*

Thấy trường ngày **có trong lược đồ** và đã viết ra câu đó. Đo lại thì **cả 15/15** model output
đều **rỗng**. Sửa ngay trong cùng lượt, **trước khi câu đó kịp đứng thành kết luận**.

### 3.5 · Ba câu đã công bố mà sai

| # | câu sai | điều đúng |
|---|---|---|
| **R1** | *«không có bước finalize một lần»* | **có** — job T-chốt, đủ ba miền. Em kết luận từ **một cột sai** (`created_at` không nằm trong nhánh ghi-đè nên **không thể** cho biết có lần ghi thứ hai) |
| **R2** | *«máy trạng thái chưa tồn tại»* | bộ khung **đã có**, thiếu **hai chặng đầu** |
| **R3** | *«model chậm nhất bị trần `300s` cắt»* | model đó có trần riêng **840s** từ 01/08, và **60 ngày không một timeout nào**. Em so `p90` với **hằng số mặc định** mà **không tra bảng override** |

Cả ba **rút lại đủ bốn phần** theo `PRJ-RETRACTION-001`: chỗ gốc · nguyên văn câu sai · điều đúng
kèm phép đo tái lập được · quyết định nào đã dựa vào (**chưa cái nào**).

---

## 4 · ĐIỀU ĐÁNG GHI NHỚ CHO PHIÊN SAU

1. **Phần lớn kiến trúc «cần xây» hoá ra đã có.** Trước khi trình một đề xuất xây mới, **quét
   đường thật trước** — ba trên năm mục `P0` đã tồn tại.
2. **`0` trong log không có nghĩa là chết.** Phải hỏi *«nguồn này có ghi được không?»* trước khi
   đọc số `0` (`RM-13` · `RM-20`).
3. **Trường có trong lược đồ ≠ trường có dữ liệu.** Luôn đo giá trị thật.
4. **Cùng một khuôn `try/except ImportError` có thể fail-CLOSED ở chỗ này và fail-OPEN ở chỗ
   kia.** Không suy hành vi từ hình dạng mã.

---

TanPhatAI cần làm: đọc `REPORT_V11113.md` §9 — bảy mục theo dõi, **năm mục cần owner ký**; ghi nhận ba câu đã rút lại để không trích lại bản cũ; chờ kết quả diff ảnh chụp `15:50` trước khi kết luận FINAL có bất biến trong thực tế hay không.
