# CONVERSATION CONTEXT — V10980 · 04/08/2026

Ghi lại **nguyên văn** lời owner, agent đã làm gì theo thứ tự, và vấp ở đâu.

---

## 1. Owner nói gì — nguyên văn

**09:47 ngày 04/08/2026 (giờ Việt Nam):**

> "Kiểm tra toàn diện hệ thống đầu ngày dùm anh luôn em"

Không có lời nhắn nào khác của owner trong phiên này.

### Bối cảnh mang sang từ phiên trước (03/08)

Tối 03/08 lúc 19:03, **owner tự phát hiện trước cả máy** rằng trang MB `/nghiem-thu` trắng —
không có lấy một con số. Trong khi đó cả **16 phép tự kiểm vẫn xanh**, `/monitoring` vẫn sạch,
và không cơ chế nào kêu. Nguyên nhân: official MB chốt **17:44:54**, sau lượt lane cuối (17:42)
**2 phút 53 giây**, nên cổng `_official_gate` không bao giờ mở.

Owner **đang mất dần niềm tin**, nên yêu cầu phiên này trả lời **bằng số, không đường mật**.

### Quyết định của owner còn hiệu lực, ràng buộc phiên này

- **QD-014** — đóng băng đường ra số công bố **tới hết 08/08**. Không đụng đường chọn số.
- **QD-013** — chỉ đặt tiền thật khi lợi thế **≥ +3pp** và **z ≥ 2**.
- **§57 (A55)** — Notion **chỉ đọc**; mọi báo cáo đẩy lên GitHub công khai.
- **Múi giờ** — mọi mốc là giờ Việt Nam. Nhiều bảng lưu UTC, phải tra `tz_registry` trước khi
  đọc dấu thời gian.

---

## 2. Agent đã làm gì — theo thứ tự

1. **Chạy bốn cổng tự kiểm trước khi trả lời** (bắt buộc theo `.cursorrules` §0). Cả bốn
   **exit 0**.
2. **Dựng probe chỉ-đọc lên VPS** (`_v10980_audit_probe.py`) — đẩy một script lên `/tmp`, chạy
   bằng venv của dự án, thu về JSON 110 KB. Không ghi bất kỳ bảng nào.
3. **Probe 2** — gọi thẳng `run_checks()` để kiểm bản code trên đĩa (không dùng `compute_view()`
   vốn chỉ đọc bản đã lưu — bẫy đã ghi trong sổ tay). Kiểm cờ tiền, endpoint, giờ cron lane.
4. **Probe 3** — `scheduler_logs` theo đúng cột `log_level`, view lane, health đầy đủ.
5. **Đọc sổ theo dõi** — phát hiện briefing đầu phiên báo *"81 treo · 0 quá hạn"* trong khi
   FU-245 tới hạn **đúng hôm nay**.
6. **Đào ra hai lỗ của bộ đọc** (`_v10980_gate_hole.py`) — đo bằng số: 51 ô `**due**` / 68 tiêu
   đề mang hạn → 24 mã mất hạn; `TREO_STATUSES` khai 6 nhãn trong khi kho dùng 28 nhãn → 14 mã
   rơi khỏi bộ đếm, 17 mã mồ côi.
7. **Vá bộ đọc + briefing** — chuỗi dò hạn 4 bước, thêm 3 nhãn đồng nghĩa, thêm
   `trang_thai_mo_coi()` và mục `[3b]`.
8. **Chứng minh căn nguyên FU-245** (`_v10980_hook_test.py`) — chạy đối chứng bản cũ và bản mới
   với stdin để mở. Bản cũ treo, bản mới ghi sau 0,62 giây.
9. **Vá hook** — chuyển việc lên trước `stdin.read()`, thêm sổ điểm danh.
10. **Kiểm hash 4 bảng khoá trước/sau** — giống hệt cả bốn.
11. **Ghép governance** vào `CHANGELOG.md` · `docs/CURRENT_TRUTH_SSOT.md` ·
    `docs/FOLLOW_UP_TRACKER.md` bằng `_doc_prepend.prepend()`.
12. **Dựng báo cáo công khai** + che khoá API (quét ra 0 chỗ cần che) + push.

---

## 3. Vấp ở đâu — ghi đủ, kể cả lỗi do agent gây ra

### 3.1 Tự tạo ra 2 mục mồ côi khi ghi sổ — và bị chính bộ dò vừa viết bắt được

Khối cập nhật FU-243 và FU-252 lúc đầu viết dạng kể chuyện, **không kèm bảng
`| **status** |`**. Bộ đọc chỉ lấy bản mới nhất nên hai mã đó lập tức mất trạng thái, số mồ côi
nhảy **17 → 19**. Đã bổ sung bảng trạng thái cho cả hai, kiểm lại về 17.

*Nếu bỏ qua:* FU-252 (đang canh lane MB — đúng sự cố owner bắt tối qua) và FU-243 (đang canh lọc
phiếu) **biến mất khỏi mọi bộ đếm**. Nghĩa là vừa sửa xong một lỗ thì tự tay đào lại đúng cái lỗ
đó. Bài học ghi lại: **mỗi khối cập nhật FU bắt buộc có bảng trạng thái**, không viết suông.

### 3.2 Suýt báo nhầm FU-185 quá hạn — loại vấp nguy hiểm nhất phiên này

Bản dò hạn đầu tiên đòi ô hạn khớp **trọn chuỗi** `DD/MM`. Ô của FU-185 ghi
`10/08 (sau freeze QD-014)` nên không khớp; bộ đọc rơi xuống lấy hạn ở tiêu đề là `03/08` và báo
**QUÁ HẠN**. Thực tế owner **đã gia hạn tới 10/08**. Phát hiện khi rà lại từng mục bị đánh dấu
thay vì tin thẳng đầu ra. Đã sửa sang dò trong chuỗi, kèm chặn ngày/tháng hợp lệ.

*Nếu bỏ qua:* báo cho owner một mục quá hạn **không có thật**. Cái này **tệ hơn xanh giả** —
xanh giả làm owner không biết có việc; báo động giả làm owner **thôi tin cả những cảnh báo
đúng**. Đúng lúc owner đang mất niềm tin thì đây là lỗi không được phép mắc.

### 3.3 Kết luận "0 lỗi scheduler" từ một câu truy vấn hỏng

Truy vấn `scheduler_logs` bằng cột `status` trong khi bảng chỉ có `log_level` → trả
`ERR no such column`, và bản tóm tắt đầu tiên in ra *"lỗi hôm nay: 0"*. Suýt nữa báo "sạch" từ
một câu hỏng. Đã đọc `PRAGMA table_info` rồi truy vấn lại: **341 INFO · 7 WARNING · 0 ERROR**,
7 WARNING đều là `SOFT_CONTINUE_90S` theo thiết kế.

*Nếu bỏ qua:* lại một xanh giả nữa, lần này do chính agent tạo ra ngay trong phiên đi diệt xanh
giả.

### 3.4 Đếm thô bắt "500" rồi suýt báo là lỗi HTTP

Phép đếm `grep -ci '500'` trả 1. Soi ra là **dấu mili-giây** trong dòng log **thành công**
(`05:22:58,500 … "HTTP/1.1 200 OK"`). Đã ghi rõ trong báo cáo thay vì để con số trần gây hiểu
nhầm.

### 3.5 Gõ sai kiểu shell

Dùng `cd /d … && …` (lối `cmd`) trong phiên PowerShell → lỗi cú pháp ngay lệnh đầu tiên. Mất một
lượt, không ảnh hưởng dữ liệu.

### 3.6 `compute_view()` của lane cần tham số `con`

Gọi thiếu tham số ở probe 2, trả `TypeError`. Gọi lại đúng ở probe 3.

### 3.7 `/api/du-doan` trả 404

Đường dẫn thử là phỏng đoán chứ không phải endpoint thật. **Không kết luận gì** từ con số này.
Việc kiểm 15/15 lấy thẳng từ `final_bundles.model_count` nên không phụ thuộc endpoint.

### 3.8 Không kiểm được trang `/nghiem-thu` bằng mắt

Endpoint trả **401** khi gọi không kèm khoá — đúng thiết kế admin. Nhưng nghĩa là phiên này
**chỉ xác nhận được dữ liệu trong DB**, không xác nhận được trang hiển thị ra sao. Owner tối qua
bắt lỗi **bằng mắt trên trang**, nên khoảng trống đó **vẫn còn**. Đã ghi vào FU-252 thay vì lờ đi.

---

## 4. Hai luồng chạy song song trong ngày

| phiên | việc | quan hệ |
|---|---|---|
| **V10979** | thiết kế lại **nhịp chạy cuốn chiếu 5 model AI một lượt** | phiên này **không chạm**, chỉ ghi nhận |
| **V10980** (phiên này) | kiểm toàn diện đầu ngày + vá cổng đếm việc | |

Cả hai đều chạm `docs/FOLLOW_UP_TRACKER.md`. Phiên này **chỉ stage đúng file của mình**, không
dùng `git add -A`, và đọc lại nội dung tài liệu **ngay trước khi** ghép để không đè lên khối của
phiên kia.

---

## 5. Điều agent muốn owner biết rõ

1. **Hạ tầng đang chắc.** Dịch vụ sống nguyên PID sau 14 tiếng, 0 traceback, 0 error, hash 4
   bảng khoá không đổi. Việc deploy tối qua đứng vững hết: cron mới đã vào, mốc FINAL khớp cả 4
   module.

2. **Nhưng chỗ owner nghi là đúng.** Có **hai** thứ đang "chỉ có trên giấy":
   - Hai phép tự kiểm C17/C18 thêm tối qua **chưa chạy thật lần nào** (cron 18:05 chạy trước
     deploy 19:23). Code đúng, nhưng lượt ghi thật đầu tiên là **tối nay**.
   - **Chính cổng đếm việc đang báo xanh giả** — nó nói *"0 quá hạn"* trong khi có 1 mục quá hạn
     thật và 1 mục tới hạn hôm nay. Đã vá.

3. **Chuyện tối qua owner bắt được thì máy nay đã có cách bắt** — nhưng **chưa chứng minh được
   là bắt thật**. C18 giờ đo biên giữa lượt lane cuối và giờ official chốt; biên MB hiện là 546
   giây, trên ngưỡng 300. Phải đợi 18:05 tối nay mới biết chắc.

4. **Tiền vẫn an toàn tuyệt đối.** Cổng lợi thế **đóng cả 6 ô**, không ô nào dương. Tiền thật
   **0 đồng**, 111/111 dòng đều shadow.

5. **Bạch thủ hôm qua trượt cả ba miền** (MN 64 · MT 64 · MB 59). Không giấu.
