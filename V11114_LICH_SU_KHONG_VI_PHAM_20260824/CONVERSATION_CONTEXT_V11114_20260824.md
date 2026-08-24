# CONVERSATION CONTEXT — V11114 — 24/08/2026 (chiều)

> Ghi **nguyên văn** lời owner, agent làm gì, và **vấp ở đâu**.

---

## 1 · OWNER NÓI GÌ — NGUYÊN VĂN

**Prompt tổng lực lần 34:**

> *«`P0-A` ảnh chụp + diff `v1/v2` **trước MN 15:45**.»*

> *«**CẤM đổi mù 300 thành 500**.»*

Ràng buộc còn hiệu lực:

> *«Cấm thay thuật toán mù.» · «Cấm tự quyết.» · «Cấm đổi ngưỡng sau khi thấy số.» ·
> «Cấm cờ bỏ-qua-cổng.» · «Cấm `except: pass`.» · «Agent phân tích mặc định chỉ được
> READ-ONLY.» · «Cấm gọi `CODE_PUSHED` hoặc `DEPLOYED` là `RUNTIME_PROVEN` trước lượt live
> thật.»*

---

## 2 · AGENT LÀM GÌ

**Chặng 1 — chụp ảnh #2 đúng cửa sổ.** Đặt lịch nền chạy `15:50` — **sau** T-chốt `15:40`,
**sau** mốc khoá `15:45`, **trước** khi chấm kết quả `~16:36`. Cửa sổ này **cô lập đúng** lần ghi
T-chốt, không lẫn lần ghi của bước chấm.

**Chặng 2 — diff.** Bốn cột đổi. Ba cột vận hành, **một cột mang dự đoán**. Mọi con số công bố
(bạch thủ · lô 2 · 3 càng · xiên 2 · xiên 3 · điểm · số model) **giữ nguyên**, cả thang xếp hạng
10 hàng **giống hệt tới 4 chữ số thập phân**.

**Chặng 3 — năm làn đo song song + năm làn phản biện.** Câu chính: *«có ngày nào trong lịch sử
mà một cột mang dự đoán đổi SAU mốc khoá không?»*

**Chặng 4 — phản biện lật kết luận.** Làn đo báo *«1 vi phạm»*. Phản biện bác bằng **ba bằng
chứng độc lập**, trong đó có **vân tay runtime** (chuỗi log cũ-viết-cứng vs mới-sinh-động) — một
cách chứng minh mà làn đo không nghĩ ra.

**Chặng 5 — vá bộ đo.** Phản biện tìm **13 lỗi** trong bộ đo. Vá lỗi 13 xong thì **sinh ra lỗi
14**. Vá tiếp, cho verdict **ba chiều**. Thử chặn **21/21**.

**Chặng 6 — rút lại, ghi bốn mặt, đẩy hai kho.**

---

## 3 · VẤP Ở ĐÂU — ghi hết, không giấu

### 3.1 · Bộ đo của chính em có 14 lỗi, và lỗi nặng nhất **đã tới tay owner**

Verdict *«chỉ trường settlement/meta đổi»* in ra **mỗi khi danh sách vi phạm rỗng**, không hề
kiểm có cột mang-dự-đoán nào đổi hay không. Bảng in rõ một cột `PREDICTION_BEARING` đã đổi, dòng
tổng kết ngay dưới nói ngược lại. **Em đã trình chính verdict đó cho owner** như bằng chứng.

Bài học không phải *«viết cẩn thận hơn»* mà là: **dòng tổng kết phải suy ra từ chính dữ liệu đã
in**, không được là một câu độc lập tự đứng.

### 3.2 · Vá lỗi 13 sinh ra lỗi 14 — `RM-07` đúng nguyên văn

Neo cổng vào mốc khoá (đúng) thì cổng **báo động giả mỗi ngày**, vì cửa sổ so sánh **vắt qua
mốc**. Một cổng kêu oan mỗi ngày sẽ bị tắt — **đúng cách một cổng chết**. Phải thêm chiều thứ ba:
*«không truy được»*, khác cả *«sạch»* lẫn *«vi phạm»*.

### 3.3 · Suýt kết luận bằng nguồn sai — hai lần

① Đo cổng khoá trong **bảng log** ra `0` và **suýt** kết luận cổng chưa từng chạy. Hai cổng dùng
`print()` ⇒ ra journald, **không** vào bảng. ② Cột giờ của bảng log là **UTC**, không phải giờ VN
— đọc thẳng sẽ lệch **7 tiếng** và kết luận T-chốt chạy lúc 8 giờ sáng.

### 3.4 · Đoán tên bảng

Thử bốn tên bảng theo suy đoán, **cả bốn không tồn tại**. Phải quét mã tìm đường thật.

### 3.5 · Suýt nói *«dữ liệu để vá đã có sẵn»*

Trường ngày **có trong lược đồ**, nhưng đo lại thì **rỗng ở đúng những mục cần nó**. Sửa ngay
trong cùng lượt.

### 3.6 · Phản biện cũng sai, và phản biện của phản biện bắt được

Một làn bác *«hai cổng chưa từng thử lửa»* — đúng, vì bài thử đã có sẵn trong kho **ba tiếng
hai mươi phút** trước phép đo của họ, và họ **không tra kho** trước khi kết luận. Nhưng chính
bản bác đó cũng nói quá: bài thử chỉ phủ **một** trong hai cổng.

---

## 4 · ĐIỀU ĐÁNG GHI NHỚ CHO PHIÊN SAU

1. **Đo xong phải cho người khác cố bác.** Nếu chỉ chạy làn đo, báo cáo này đã công bố *«có 1 vi
   phạm»* — sai.
2. **Kiểm mốc thời gian ở đúng độ phân giải của sự kiện.** Một commit lúc `16:19` không thể chi
   phối một lần ghi lúc `15:45` **cùng ngày**. Đo ở mức NGÀY cho sự kiện mức PHÚT là sai.
3. **Vân tay runtime mạnh hơn suy luận từ ngày commit.** Chuỗi log cũ-viết-cứng vs mới-sinh-động
   nói thẳng bản nào đang chạy.
4. **Một bộ đo sai nguy hiểm hơn không có bộ đo** — vì nó phát ra dấu xanh.
5. **Trường tự do vừa làm kênh điều khiển vừa làm danh tính là hỏng cả hai vai.**

---

TanPhatAI cần làm: đọc `REPORT_V11114.md` §9 — năm mục theo dõi, **bốn mục cần owner ký**; ghi nhận hai câu đã rút lại; **KHÔNG** dùng kết luận *«có 1 vi phạm ngày 31/07»* làm căn cứ — nó đã bị bác bằng ba bằng chứng độc lập.
