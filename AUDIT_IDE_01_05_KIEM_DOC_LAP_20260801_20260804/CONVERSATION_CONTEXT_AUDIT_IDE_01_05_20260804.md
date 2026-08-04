# Ngữ cảnh — năm lượt kiểm độc lập, 01/08 → 04/08/2026

**Người thực hiện:** Agent IDE (Claude), chạy trên máy local của owner.
**Bản này đã lọc an ninh** theo quyết định owner ngày 04/08 (phương án A).

---

## 1. Lời owner — nguyên văn

### 01/08 ~13:35 — lượt 1
> *"Audit tổng lực toàn bộ hệ thống Lottery AI ĐANG CHẠY tại thời điểm audit, từ mọi ngóc ngách...
> Không được bỏ im bất cứ phần nào chưa xác minh."*
> *"Không dùng report cũ làm runtime truth. Mỗi claim phải có evidence."*

### 01/08 ~16:47 — lượt 2
> *"V10934: NOT DEPLOYED — HOLD FOR AUDIT. V10936: NOT DEPLOYED — HOLD FOR AUDIT.
> Không deploy chung V10934/V10936. Audit read-only trước mọi mutation."*

### 01/08 ~22:00 — lượt 3
> *"Có Owner authorization mới hơn 16:43 hay không... Nếu không có bằng chứng:
> classify UNAUTHORIZED_DEPLOYMENT."*
> *"Không dùng câu 'Owner quyết' trong report làm bằng chứng duy nhất."*

### 02/08 ~18:44 — lượt 4
> *"Hết live rồi em kiểm tra tổng lực toàn diện dùm anh tất cả mọi thứ không bỏ sót vấn đề nào nha em"*

### 02/08 ~18:50 — bàn giao
> *"Đồng thời em đánh live hôm nay thành công nhờ đâu? có thay đổi gì mà tại sao có sự tốt lên là sao em?"*
> *"kế hoạch đang đang chuyển qua máy local khác để code fix tiếp cần đảm bảo không thiếu sót nội dung nào"*

### 04/08 ~22:35 — lượt 5
> *"Không tiếp tục vá lẻ. Dựng current runtime truth và thiết kế một target architecture thống nhất."*
> *"FINAL giữ MN 15:45, MT 16:58, MB 17:58. Target phân tích: MN 15:35, MT 16:48, MB 17:48.
> Không áp target vào runtime."*

### 04/08 — owner phản hồi giữa chừng
> *"Thấy tào lao rồi đó anh chốt khác em mà sao kỳ thế em? MN 15h45 / MT là 16h58 / MB là 17h58
> mà em sao lại khác thường thế em? xem lại lần nữa"*

### 04/08 — về báo cáo công khai
> *"đẩy báo cáo lên github report chưa em?"* → sau khi được trình ba phương án: **"A nha em"**

---

## 2. Agent đã làm gì, theo thứ tự

1. **Lượt 1** — 16 phase, 17 tài liệu + 11 bảng máy đọc + thư mục bằng chứng. 56 phát hiện.
2. **Lượt 2** — chứng minh trạng thái deploy bằng **mã băm đối chiếu 7 mốc mã nguồn**; bắt được
   cửa sổ live của một miền đang chạy nên quan sát trực tiếp thay vì dựng lại.
3. **Lượt 3** — điều tra một lần deploy; dùng **chính mã băm đã ghi ở lượt 2** làm dấu vân tay
   "trước sự việc"; rà 5 nguồn tìm bằng chứng uỷ quyền.
4. **Lượt 4** — quét sau live; **kiểm chứng độc lập** kết luận "hệ không hơn ngẫu nhiên" bằng cách
   tự viết lại phép đo, không dùng bảng có sẵn.
5. **Bàn giao** — hồ sơ 8 phần cho máy mới, phân ba mức bằng chứng `[ĐO]` / `[ĐỌC]` / `[KHÔNG THẤY]`.
6. **Lượt 5** — audit tái nền: đo P50/P95/P99 từng chặng 90 ngày, đo trùng lặp phiếu trên
   273 miền-ngày, thiết kế kiến trúc đích và lộ trình 7 đợt.

---

## 3. Vấp ở đâu — kể cả vấp do chính agent gây ra

### 3.1 Agent trình bày gây hiểu nhầm mốc công bố *(lỗi của agent)*

Ở lượt 5, owner đưa **hai bộ mốc**: mốc công bố cuối (khoá) và mốc phân tích nội bộ (sớm hơn
10 phút, đưa ra để thẩm định). Agent đặt bảng kết luận về **bộ thứ hai** dưới tiêu đề *"Đề xuất"*
mà **không để bộ thứ nhất bên cạnh**.

Owner đọc lướt và phản ứng ngay: *"Thấy tào lao rồi đó..."*.

**Agent kiểm lại runtime: mốc công bố đúng ở cả 6 nơi, không sai chỗ nào, và agent chưa từng đụng
vào.** Vấn đề hoàn toàn nằm ở cách trình bày. Đã đính chính bằng một mục riêng đầu báo cáo và
bảng hai cột hiện cả hai bộ mốc.

**Bài học:** khi có hai bộ số gần giống nhau, **không bao giờ hiện một bộ mà giấu bộ kia**.

### 3.2 Agent chậm nêu mâu thuẫn về báo cáo công khai *(lỗi của agent)*

Quy tắc nội bộ yêu cầu đẩy báo cáo công khai sau mọi việc. Nhưng cả 5 brief đều ghi *"không
commit/push"*. Agent chọn tuân brief và **im lặng suốt 5 lượt**, chỉ nêu khi owner hỏi thẳng
*"đẩy báo cáo lên github report chưa em?"*.

Lẽ ra phải nêu mâu thuẫn ngay lượt 1 để owner quyết. Đây là **món nợ tự tạo**, và bản báo cáo
này chính là việc trả nợ.

### 3.3 Agent suýt để một cảnh báo cũ trôi thành kết luận sai

Ở lượt 2, agent cảnh báo hạn thời gian cấp cho hai model mới **dài hơn** biên tới mốc chốt, nên
chúng có thể vắng mặt khỏi bundle. Đến lượt sau, đo thật cho thấy **hôm đó chúng trả về rất
nhanh, không chạm biên**. Agent phải ghi rõ *"nỗi lo lớn nhất KHÔNG xảy ra"* thay vì lặp lại
cảnh báo cũ — nhưng cũng nói rõ **một ngày tốt không chứng minh được biên an toàn**.

### 3.4 Chỗ agent phải nói ngược ý owner

Owner hỏi *"đánh live hôm nay thành công nhờ đâu? có thay đổi gì mà tại sao có sự tốt lên?"*
sau một ngày cả ba miền cùng trúng.

Agent phải trả lời **không phải nhờ thay đổi gì** — đếm được đó là **1 ngày duy nhất trong 90
ngày** có cả ba miền cùng trúng, trong khi xác suất tự nhiên là **2,2 %**, tức ~1 lần/tháng, và
180 ngày quan sát được 5 lần — **khớp kỳ vọng**. Cái thật sự tốt lên hôm đó là **vận hành**
(đủ dòng đo, đủ phiếu, deploy đúng giờ), **không phải độ chính xác**.

Nói ngược ý owner ở đây là bắt buộc: nếu để owner tin "đổi model xong thấy tốt lên" thì đó đúng
là cái bẫy đã làm dự án lẩn quẩn nhiều tháng — quyết định trên khác biệt **nhỏ hơn mức đo được**.

### 3.5 Chỗ agent phải giữ kết luận dù bất lợi cho luồng chính

Ở lượt 3, agent phải phân loại một lần deploy là **không tìm thấy uỷ quyền**, kèm ba bằng chứng
ngược lại đều có trước thời điểm deploy. Nhưng agent cũng phải ghi rõ giới hạn: **không quan sát
được hội thoại giữa owner và agent khác**, nên đó là *"trong mọi nguồn quan sát được, không tồn
tại uỷ quyền"* — **không phải** kết luận có người cố ý vượt quyền. Chỉ owner gỡ được nút này.

### 3.6 Trạng thái thay đổi ngay trong lúc kiểm — ba lần

| Lúc | Việc | Ảnh hưởng |
|---|---|---|
| lượt 1, +4 phút sau khi chụp | một commit xuất hiện | phát hiện "chạy code chưa commit" **tự khép** |
| lượt 3, đang xuất gói | dịch vụ khởi động lại, một tệp lõi đổi | ghi phụ lục riêng, nêu rõ 3 dòng bị làm cũ |
| lượt 5, đang viết báo cáo | thêm một commit | ghi nhận trong phần tổng kết |

Cả ba **không do agent**, và đều được ghi kèm mốc giờ để người đọc biết ảnh chụp có hạn dùng.

---

## 4. Cái gì các lượt này KHÔNG làm

- **Không sửa bất kỳ dòng mã nào.**
- Không deploy, không khởi động lại dịch vụ, không sửa lịch chạy.
- Không ghi vào cơ sở dữ liệu — mọi truy vấn đều mở ở chế độ chỉ-đọc.
- Không gọi nhà cung cấp AI.
- Không commit/push vào kho mã riêng tư.
- Không đọc lịch sử lệnh của người dùng trên máy chủ (**cố ý không đọc**, ngoài phạm vi được cấp).
- Không đọc/ghi Notion (quy tắc nội bộ: chỉ đọc; agent chọn không đọc để giữ ranh giới rõ ràng).
- **Không in bất kỳ thông tin xác thực nào** — lọc ngay tại nguồn truy vấn.

---

## 5. Việc đã được luồng chính tiếp nhận và xử lý

Ghi nhận cho công bằng — một số phát hiện đã được xử trước khi báo cáo này ra đời:

| Phát hiện | Trạng thái |
|---|---|
| Sáu mặt quy tắc ghi sai mốc công bố | ✅ đã sửa, còn chú thích rõ lịch sử |
| Sổ quyết định owner thiếu mục | ✅ 12 → 19 mục |
| **Cổng lợi thế không có lịch chạy** | ✅ đã thêm lịch hằng ngày |
| Quy tắc "một biến số mỗi lần, đo 7–14 ngày" | ✅ đã thành quyết định có số hiệu |
| Yêu cầu so hai prompt trên **cùng** model | ✅ đã thành quyết định có số hiệu |

---

## 6. Còn nợ

- **Ba vấn đề an ninh P0** — báo từ 01/08, tới 04/08 chưa xử. **Chi tiết giữ nội bộ.**
- Công cụ đo tiền (chi phí, lãi/lỗ) chết 76–90 ngày, trong khi quyết định lớn nhất của giai đoạn
  này là **quyết định về tiền**.
- Ba câu chỉ owner trả lời được (thẩm quyền deploy · xử lý mục đóng băng bị trái · ngày khuyết).
