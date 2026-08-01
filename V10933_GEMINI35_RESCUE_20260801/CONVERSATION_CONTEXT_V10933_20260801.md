# Bối cảnh hội thoại — V10933 (01/08/2026)

Ghi nguyên văn lời owner, không diễn giải lại.

---

## Lời owner dẫn tới phiên này

### 01/08 — trước đó, khi bàn về việc cắt model

> Chỉ có gemini 3.5 flash là anh đang tiết nhất chạy ổn nhưng tự nhiên lỗi làm mất một model tốt
> tham gia total hi vọng các model thay thế cải có giá trị tương đương hoặc tốt hơn. các model LM
> mắc gì phải clear đúng không em? đâu ảnh hưởng chi phí đâu , mà cơ chế là filter lấy model mạnh
> nhất mà tổng hợp output mà em đúng không em? còn total thì anh không rõ đang đang dùng cơ chế
> nào anh chỉ đang nói ML và combo super thôi nha em.

### 01/08 14:09 — yêu cầu của phiên này

> gemini-3.5-flash ==> thử lại xem có phương pháp vào vượt qua lỗi này không em?

---

## Lời owner ngày 31/07 — nguồn gốc của cơ chế đường thoát

> hic gemini đang chạy API key chính hãng hả em? sao google rơt hoài em

Và khi được hỏi xử lý thế nào với `gemini-3.5-flash`, owner chọn phương án **nâng lên 3.6**.

Chính câu *"anh nghĩ do hạng khoá... cần có phương án lấy openrouter"* của owner là nguồn gốc của
`GOOGLE_OPENROUTER_FALLBACK` — cơ chế mà phiên này phát hiện là khai thiếu bản 3.5.

---

## Điều owner đã dặn và phiên này phải tuân

### Về việc tra cứu trước khi hỏi (31/07)

> Anh không muốn nhắc tới nhắc lui hoài những vấn đề mà em có thể tra ra, có thể kiểm soát được
> đâu? Em làm quá cẩu thả, em đã tham chiếu với lịch sử, changelog, tài liệu, v.v. để nắm rõ và
> kiểm tra lại, em phải tư duy để có mối liên hệ chặt chẽ giữa báo cáo, giữa tài liệu, giữa code
> để kiểm soát chứ em.

→ Phiên này tra thẳng vào code và số liệu sống trước khi trả lời, không hỏi lại owner.

### Về báo cáo công khai (01/08)

> thống nhất quy tắc Mô hình code, fix, audit của dự án anh là sau khi thực hiện code, fix, audit
> cần đẩy báo cáo report lên github report public dùm anh, cập nhật, ghi nhận quá trình, yêu cầu
> thật cụ thể chi tiết để kiểm soát tốt nhất nha em, Notion MCP dùng để tham khảo tài liệu khi
> cần không được cập nhật vào Notion nha em.

→ Báo cáo này đẩy lên GitHub công khai. Không đụng Notion.

### Về mức độ cẩn thận (31/07)

> Rồi làm đi thật cẩn thận có kiểm soát nha em

> Anh hết tin tưởng em rồi quá cẩu thả, chểnh mảng, thiếu tư duy, suy nghĩ v.v... quá chán mọi
> thứ hầu như ngày nào cũng đào ra lỗi, chả có cái nào mà ổn định chính xác là sao vậy?

→ Phiên này gọi thử thật 3 lượt riêng biệt trước khi khai slug, và tự bắt được một bẫy (hạn 20
token làm `content` rỗng) suýt dẫn tới kết luận sai.

### Về cách nói (31/07)

> Em vẫn báo cáo chuyên sâu, từ ngữ khó hiểu anh chả hiểu gì cả?

→ Báo cáo viết bằng lời thường, tránh thuật ngữ.

---

## Việc đã làm trong phiên

1. Đào lỗi thật của `gemini-3.5-flash`: 71 đậu / 4 lỗi 503 / 1 timeout trên 76 lượt.
2. So với `gemini-3-flash` (1,56%) và `gemini-3.1-pro` (1,04%) → xác nhận là vấn đề sức chứa của
   model mới, không phải vấn đề khoá hay hệ.
3. Phát hiện `GOOGLE_OPENROUTER_FALLBACK` dựng 31/07 khai thiếu chính bản 3.5.
4. Gọi thử thật slug `google/gemini-3.5-flash`: 6/6 đậu; qua đúng đường của hệ trả JSON hợp lệ.
5. Loại slug sai `google/gemini-3.5-flash-preview` (400).
6. Khai bù vào đường thoát; lật registry `RETIRED` → `SHADOW_AUTO`.
7. Sửa luôn hai con số tự kiểm registry đã sai từ trước phiên này.
8. Deploy, xác minh PID đổi thật, băm 4 bảng y nguyên.
9. Ghi CHANGELOG / SSOT / FU-197 / FU-198 / AUTOMATION_STATE.

---

## Điều owner cần quyết sau này

Phiên này **không** đưa `gemini-3.5-flash` vào luồng chính thức — nó quay lại làm shadow. Quyết
định đưa lên official chờ FU-197 (hạn 15/08): nếu tỉ lệ hỏng xuống dưới 1,5% thì mới xét thay một
model đang âm điểm.
