# CONVERSATION CONTEXT — V11116 — 25/08/2026

> Ghi **nguyên văn** lời owner, agent làm gì, và **vấp ở đâu**.
> Mọi giờ là **giờ Việt Nam (UTC+7)**.

---

## 1 · OWNER NÓI GÌ — NGUYÊN VĂN

**Prompt tổng lực lần 35**, mở đầu:

> *«Dùng multi-agent song song nhưng chỉ **MỘT Coordinator hợp nhất**. Không mở Plan/sổ cạnh
> tranh. **Không mặc định 15 model tốt hơn 8 model. Không mặc định nhiều model tốt hơn ít
> model.** Số lượng model chỉ là **tồn kho**.»*

> *«Chất lượng TOTAL phải được chứng minh bằng: khả năng sinh số; độ phủ; xếp hạng; đóng góp
> biên; tính độc lập; độ ổn định; bằng chứng walk-forward không lookahead.»*

Mục `GĐ-5`:

> *«Nếu chưa đủ bằng chứng, vẫn phải chốt: `TOTAL_V2_CANDIDATE` · công thức · scorer · shadow
> pipeline · ngưỡng · ngày đọc lại · điều kiện promotion. **Cấm đổi mù chỉ để có vẻ đã tạo
> «phương pháp mới»**.»*

> *«Phải: đăng ký ngưỡng **trước khi đọc**; đăng ký ngày quyết định; hiệu chỉnh multiple
> comparisons; báo đầy đủ các cửa sổ; **cấm chọn một cửa sổ đẹp riêng lẻ**.»*

Điều kiện **DỪNG VÀ BÁO OWNER**:

> *«roster lịch sử không tái lập được; dùng roster hôm nay cho quá khứ; có lookahead;
> alias/family bị đếm lặp; prediction ngày 25/08 bị đổi; migration/rollback/restore thất bại;
> phương pháp mới không đạt gate nhưng có yêu cầu bật OFFICIAL.»*

> *«**Cấm hứa tăng tỷ lệ trúng**.»*

**Giữa phiên, owner hỏi hai lần:** *«đang đo lường ah em? đợi kết quả hay sao?»* và
*«còn đang chạy không em? xong chưa push báo cáo tổng lực chưa em?»*

---

## 2 · AGENT LÀM GÌ

**Chặng 1 — `GĐ-0` bảo toàn, TRƯỚC khi chạm gì.** Chụp trạng thái máy chủ, băm 10 tệp runtime
hai phía (**khớp toàn bộ**), lược đồ, bundle hiện tại, roster/config, cron. Thử chặn 10/10.

**Chặng 2 — trả lời câu CHẶN.** Owner khoá *«roster lịch sử không tái lập được ⇒ DỪNG»*. Đo:
bậc thang lịch sử có **535/535 = 100%** kèm danh sách model bỏ phiếu, và **dữ liệu thành phần**
đủ để tái lập từng bước tính. ⇒ **không phải dừng**, benchmark khả thi.

**Chặng 3 — TIỀN ĐĂNG KÝ NGƯỠNG.** Việc này làm **trước khi có một con số nào**, commit lúc
`13:06:08`, khi `0/7` làn đã trả kết quả. Lý do: dự án **đã phạm đúng lỗi này ngày 23/08** — so
số cặp bất đồng `46` với sàn `96` rồi **tự hạ sàn**.

**Chặng 4 — bảy làn đo + bảy làn phản biện**, 2,09 triệu token, 41 phút, 0 lỗi.

**Chặng 5 — phản biện lật kết luận.** Bác 36, giữ 92, thêm 57.

**Chặng 6 — viết ba tài liệu, commit, đẩy hai kho.**

---

## 3 · VẤP Ở ĐÂU — ghi hết, không giấu

### 3.1 · Kết quả không phải điều ai mong muốn, và đó là điểm chính

Cả bảy phương pháp — kể cả phương pháp đang chạy — **nằm trong vùng nhiễu quanh nền**. Cám dỗ ở
đây rất cụ thể: chọn một cửa sổ đẹp, hoặc một miền đẹp, hoặc hạ sàn `96` xuống cho vừa `46`, rồi
báo *«đã tìm ra phương pháp mới tốt hơn»*.

**Tiền đăng ký làm trước chính là để chặn cám dỗ đó.** Không có nó, cái sàn `96` sẽ rất dễ trở
thành `40`.

### 3.2 · Phản biện bác ba kết luận của làn đo

① Quy gán dấu cho *«lớp ghi đè đang chạy»* — **sai**: con số gộp là hiện vật của việc **gộp hai
lớp ngược dấu**, và dấu âm đến **toàn bộ từ những lớp đã bị tắt**.
② Đếm *«ba lớp»* — thực ra **bốn**.
③ Công thức `n`-cần **thiếu `z_beta`** ⇒ đó là `n` cho sức mạnh 50%, không phải để **phát hiện**.
Hệ quả thật: *«5,1 tháng»* đọc thành **«làm được trong quý này»**; *«10,4–13 tháng»* đọc thành
**«không khả thi»** — hai cách đọc dẫn tới **hai quyết định khác nhau**.

### 3.3 · Một tiền đề của chính agent sai

Brief giao cho các làn đo ghi *«mẫu 534 bundle»*. Thật ra chỉ **423** dùng được — 90 bundle
tháng 2–3 là **backfill** tạo cùng một ngày, **không có dữ liệu thành phần**. Sửa trong cùng
phiên, **trước** khi công bố.

### 3.4 · Suýt đọc quá lời

Kết quả *«không khác nền»* rất dễ đọc thành *«hệ thống vô dụng»*. **Không đúng.** Mẫu hiện tại
chỉ đủ phát hiện hiệu ứng **≥ 6pp**; để phát hiện `+3pp` cần **1,6 năm** dữ liệu. Câu đúng là
*«không có lợi thế đo được ở mức ≥ 6pp»*.

Đây là `RM-04`: `n` nhỏ là **«chưa được phép kết luận»**, không phải **«đã chứng minh bằng 0»**.

---

## 4 · ĐIỀU ĐÁNG GHI NHỚ CHO PHIÊN SAU

1. **Đăng ký ngưỡng trước khi đo là việc phải làm NGAY, không phải việc làm sau.** Nó chỉ có giá
   trị nếu commit của nó đi **trước** commit của kết quả.
2. **Thêm đối chứng ngớ ngẩn vào mọi benchmark.** «Luôn chọn một số cố định» và «chọn số hay về
   nhất 90 ngày qua» — hai đối chứng tầm thường, và cả hai **thắng** phương pháp đang chạy. Nếu
   không có chúng, bảng so sánh sẽ tạo ấn tượng sai về **tầm vóc** cuộc thi.
3. **Đo bề rộng và độ chính xác là hai việc khác nhau.** Số model mua được bề rộng (bão hoà
   `k=8–10`), **không** mua được độ chính xác.
4. **In-sample vs walk-forward phải báo cạnh nhau.** Ở đây khoảng cách là `9,8pp` — toàn bộ là
   overfit.
5. **Một kết luận «âm» cũng phải qua phản biện như kết luận «dương».** Ba trong bốn cái bị bác ở
   phiên này đều thuộc nhóm kết luận âm.

---

TanPhatAI cần làm: đọc `REPORT_V11116.md` §9 — bảy mục theo dõi, phần lớn **cần owner ký**; ghi nhận **LỐI C** (giữ phương pháp hiện hành, không đổi) và ngày chốt **23/09/2026**; **KHÔNG** đọc *«không khác nền»* thành *«hệ thống vô dụng»* — mẫu chỉ đủ phát hiện hiệu ứng từ `6pp` trở lên.
