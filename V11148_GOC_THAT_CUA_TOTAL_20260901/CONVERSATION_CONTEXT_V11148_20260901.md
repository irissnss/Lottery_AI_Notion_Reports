# CONVERSATION CONTEXT — V11148 · 01/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`. **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI / agent Notion.** Đây là **MỆNH LỆNH TRỰC
> TIẾP CỦA OWNER**, nói trong IDE, **có hiệu lực ngay**. Owner trao đổi liên tục nên **code
> thường đi trước tài liệu** — điều owner cho phép tường minh (`PRJ-INTERACTION-LEDGER-001`).
> Tài liệu cũ mâu thuẫn thực tế đang chạy thì **thực tế + sổ `docs/SO_TUONG_TAC_OWNER.md`
> thắng**; tài liệu là thứ phải sửa.

**01/09 ~19:00** — owner nêu vấn đề gốc, giọng bức xúc và **hoàn toàn có cơ sở**:

> *«Sau 1 thời gian dài live, điều chỉnh kết quả dự đoán vẫn tệ. Các yêu thay đổi của quá chậm và
> yêu cầu live triền miên. Một cuộc cách mạng xử lý dứt điểm đi. Prompt ngử cảnh thuần đã áp dụng
> tới đâu đo được gì? lm xử lý ra sao? Anh cần xử lý tổng lực.»*
>
> *«— Prompt nhử cảnh thuần với các điều kiện phải được soi xét kỹ lưỡng. Đưa vào lớp showdow như
> thế nào?»*
> *«— LLM LỚP OFFICAL THÌ THẾ NÀO?»*
> *«— total cần xem xét kỹ lưỡng đưa top model vào kể cả model showdow luôn, mang tiếng showdow mà
> chạy lâu như final offical luôn rồi còn gì»*
> *«— còn gì nữa rà soát lại luôn dùm anh»*

**01/09 ~19:40** — owner chốt ba điểm, **điểm 3 là chỉ đạo quyết định**:

> *«1/ tại sao gemini 2.5 flash lại tốt hơn gemini 3.6 flash mặc dù model tốt hơn thông minh hơn»*
> *«2/ a cần xử lý dứt điểm cho xong ko chần chừ»*
> *«3/ ko phải cắt total mà là xử lý lại total với xếp hạng model mới mạnh mẻ hơn tốt hơn ah em»*

**Điểm 3 sửa hướng của agent.** Agent trước đó đề nghị *«cắt TOTAL ở MB, dùng thẳng model
champion»*. Owner **bác**: không cắt, mà **làm lại TOTAL**. Hướng owner đúng — và khi truy tiếp
thì lộ ra thứ phải làm lại **không phải bảng xếp hạng** mà là **ai được vào phòng bỏ phiếu**.

**01/09 ~20:00** — *«push báo cáo github hết chưa em?»* ⇒ bản này.

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| so model theo **cùng cửa sổ** 08/2026 | loại bẫy thời kỳ — `2.5-flash` 32,61% vs `3.6-flash` 27,47%, `n≈91` |
| so **hai thước** trên cùng dữ liệu | `3.6-flash` hạng **6 `win_rate`** nhưng hạng **24 bạch thủ** |
| đọc `main.py:9633` `generate_final_bundle` | công thức `WR × strength × verdict × position` |
| ❌ **kết luận vội** từ dòng `9953` | *«TOTAL xếp hạng theo `win_rate`»* — **SAI** |
| ✅ đọc đủ ngữ cảnh `9948-9955` | `effective_weight = bt_weight if total>=5 else wr_weight` ⇒ **rút lại** |
| đo **độ dốc trọng số** | model tốt nhất nắm **7,1%** lá phiếu / 27 voter · tỉ số **3,87×** |
| đối chiếu FINAL vs trung bình pool | **khớp ± 2 điểm cả ba miền** ⇒ **gốc thật** |
| tra `prompt ngữ cảnh thuần` | **chưa từng lên production, chưa đo gì** |

---

## 3 · Vấp trong phiên — cái nặng nhất là của chính agent

**🔴 Agent công bố một "gốc hỏng" SAI với owner.** Đọc `main.py:9953` (`wr_weight = ...`) tách
khỏi hai dòng ngay trên nó, kết luận TOTAL xếp hạng theo `win_rate`. Sự thật ngược lại: `bt_weight`
là chính, `wr_weight` chỉ là dự phòng khi `< 5` mẫu BT — điều gần như không xảy ra.

Bắt được **20 phút sau**, khi đọc đủ khối để chuẩn bị sửa. **Nếu không đọc lại thì đã dựng một
thay đổi official cho cả ba miền trên một chỗ đọc sai.**

**Bài học cụ thể:** khi kết luận về một biểu thức, phải đọc **cả câu gán VÀ điều kiện chọn** —
nhất là khi tên biến ở dòng cuối gợi ý sai (`wr_weight` đứng cuối nhưng chỉ là nhánh phụ).

**🟡 Cổng chỉ-đọc của chính agent chặn nhầm nhiều lần** — mẫu cấm `>` khớp vào `>=` trong câu
`SELECT`; `%` trong `LIKE '2026-08%'` phá chuỗi định dạng Python. Làm chậm và có thể khiến người
sau tưởng dữ liệu không tồn tại.

---

## 4 · Điều agent KHÔNG làm, và vì sao

| không làm | vì sao |
|---|---|
| bật `TOTAL v2` lên official | **CLASS B**, đổi đường chọn số cả ba miền — và agent vừa đọc sai một chỗ trong chính phiên này. Chứng minh trước, bật sau |
| tuyên bố top-5 sẽ cho 52,90% | đó là **trung bình pool**, **không** phải kết quả gộp. Gộp ít voter thì phương sai tăng |
| kết luận *«model mạnh bám mẫu ⇒ bịa»* | **giả thuyết chưa đo**. `n≈91`, SE ~4,8đ ⇒ một cặp chưa đủ |
| promote model shadow vào TOTAL | owner đúng là chúng đã chạy đủ dài để phán quyết — nhưng phán quyết là **không promote**: `3.5-flash` 33,73% ngang `combo-super`, `3.6-flash` 27,66% kém rõ |

---

## 5 · Trạng thái cuối

| | |
|---|---|
| production | 🟢 **không bị đụng** — phiên chỉ đo và ghi tài liệu |
| gốc TOTAL | 🎯 **tìm ra và khớp số** — pool 27 model ⇒ trọng số gần phẳng ⇒ FINAL = trung bình pool |
| `FU-449` `TOTAL v2` | 🔴 **chờ owner gật một câu** |
| `FU-450` | 🟡 agent làm ngay — dừng `gemini-3.6-flash` · vá emitter `SYSTEM_PROMPT` |
| prompt ngữ cảnh thuần | 🔴 **chưa từng lên production** — kẹt ở emitter thiếu 16,4% |

---

TanPhatAI cần làm: ghi **gốc thật của TOTAL là HÌNH DẠNG PHÉP GỘP**, không phải bảng xếp hạng — 27 model bỏ phiếu với trọng số chuẩn hoá ⇒ tốt nhất nắm **7,1%** ⇒ **FINAL = trung bình pool**. Ghi **RÚT LẠI** câu *«TOTAL xếp hạng theo `win_rate`»* — agent đọc sai `main.py:9953`, sự thật ở `9948-9955`. Ghi **owner đã BÁC hướng "cắt TOTAL"** và chỉ đạo **"làm lại TOTAL"** — hướng owner đúng. Ghi **`FU-449` chờ owner gật**, **`FU-450` agent tự làm**. Ghi **prompt ngữ cảnh thuần chưa từng lên production**.
