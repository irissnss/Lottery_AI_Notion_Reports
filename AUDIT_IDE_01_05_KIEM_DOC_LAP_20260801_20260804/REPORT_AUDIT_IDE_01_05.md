# BÁO CÁO — NĂM LƯỢT KIỂM ĐỘC LẬP (READ-ONLY), 01/08 → 04/08/2026

**Người thực hiện:** Agent IDE (Claude) · **Chế độ:** CHỈ ĐỌC, không mutation
**Số hiệu:** đặt ngoài dãy `V109xx` để **không đụng** số hiệu của luồng phát triển chính.
**Tự kiểm chung cho cả 5 lượt:**
`code=0 · db=0 · cron=0 · deploy=0 · restart=0 · rollback=0 · commit=0 · provider=0 · secrets=0`

> ⚠️ **Bản công khai này đã LỌC AN NINH theo quyết định owner.** Ba phát hiện an ninh mức P0 được
> rút gọn thành một dòng, **chi tiết giữ nội bộ** cho tới khi vá xong. Xem §3.6.

---

## 1. TÓM TẮT

Năm lượt kiểm liên tiếp trong bốn ngày, tất cả read-only, tổng **~70 phát hiện**.

| Lượt | Thời điểm | Nội dung | Verdict |
|---|---|---|---|
| 1 | 01/08 13:35 | Kiểm tổng lực runtime, 16 phase | `PARTIAL_AUDIT_WITH_EXPLICIT_GAPS` |
| 2 | 01/08 16:47 | Kiểm trạng thái deploy V10931–V10936 | `LOCAL_AHEAD`, không partial deploy |
| 3 | 01/08 22:00 | Điều tra deploy 17:44 | `AUTHORIZATION_CONFLICT_REQUIRES_OWNER` |
| 4 | 02/08 18:44 | Quét tổng lực sau live | hệ vận hành sạch, cơ chế canh đứng yên |
| 5 | 04/08 22:35 | Audit tái nền + thiết kế kiến trúc đích | `PARTIAL_WITH_EXPLICIT_GAPS` |

**Ba kết luận lớn nhất:**

1. **Hệ chưa phân biệt được với đánh ngẫu nhiên sau 90 ngày** — kiểm chứng độc lập, khớp với
   phát hiện V10945 của luồng chính.
2. **Miền Trung có 53 % số phiếu cho số thắng đến từ một nhóm model trùng nhau 61–88 %** — ứng
   viên nguyên nhân gốc cho việc MT kém nhất.
3. **Mẫu hình lặp lại:** hệ giỏi dựng cơ chế nhưng hay quên lên lịch chạy; cơ chế chết âm thầm
   trong khi bảng điều khiển vẫn hiện số cũ.

---

## 2. OWNER YÊU CẦU GÌ (NGUYÊN VĂN)

**Lượt 1 — 01/08:**
> *"Audit tổng lực toàn bộ hệ thống Lottery AI ĐANG CHẠY tại thời điểm audit, từ mọi ngóc ngách...
> Không được bỏ im bất cứ phần nào chưa xác minh."*

**Lượt 2 — 01/08:**
> *"V10934: NOT DEPLOYED — HOLD FOR AUDIT. V10936: NOT DEPLOYED — HOLD FOR AUDIT.
> Không deploy chung V10934/V10936."*

**Lượt 3 — 01/08:**
> *"Có Owner authorization mới hơn 16:43 hay không... Nếu không có bằng chứng:
> classify UNAUTHORIZED_DEPLOYMENT. Không dùng câu 'Owner quyết' trong report làm bằng chứng duy nhất."*

**Lượt 4 — 02/08:**
> *"Hết live rồi em kiểm tra tổng lực toàn diện dùm anh tất cả mọi thứ không bỏ sót vấn đề nào."*

**Lượt 5 — 04/08:**
> *"Không tiếp tục vá lẻ. Dựng current runtime truth và thiết kế một target architecture thống nhất."*

**Phản hồi giữa chừng — 04/08:**
> *"Thấy tào lao rồi đó anh chốt khác em mà sao kỳ thế em? MN 15h45 / MT là 16h58 / MB là 17h58
> mà em sao lại khác thường thế em?"*

---

## 3. ĐÀO BỚI / PHÁT HIỆN

### 3.1 Hệ chưa hơn ngẫu nhiên — kiểm chứng độc lập

Tự viết lại phép đo từ đầu: tự đọc dữ liệu giải, tự trích hai số cuối, tự tính xác suất một số
ngẫu nhiên trúng. **Không dùng bảng có sẵn của hệ.**

| Cửa sổ 90 ngày | Hệ | Ngẫu nhiên | Lợi thế | z |
|---|---|---|---|---|
| MN | 16,08 % | 16,47 % | −0,38 pp | −0,17 |
| MT | 14,48 % | 16,50 % | −2,02 pp | −0,81 |
| MB | 16,48 % | 23,69 % | −7,21 pp | −1,62 |

Cửa sổ 180 ngày: MN +0,15 · MT +0,60 · MB −1,32. **Mọi ô `|z| < 2`.**

Và điều nặng hơn: **hoà vốn cần 18,37 % (MN/MT) và 27,55 % (MB), trong khi ngẫu nhiên chỉ được
16,47 % và 23,69 %** ⇒ **ngay cả đánh ngẫu nhiên cũng lỗ**. Trò chơi tự nó âm ~10 % và ~14 %.

⇒ Quyết định **dừng đặt tiền thật** của owner là **đúng và có căn cứ đo được**.

### 3.2 Đếm trùng phiếu — nguyên nhân gốc ứng viên cho MT

Đo 273 miền-ngày, so từng cặp model:

| Cặp | Trùng số top-1 | Trùng top-2 |
|---|---|---|
| ensemble-gộp ↔ meta-learning | 49,8 % | **88,3 %** |
| xgboost ↔ ensemble-gộp | 41,0 % | 84,2 % |
| random-forest ↔ smart-ml | 28,6 % | 81,7 % |
| xgboost ↔ smart-ml | 27,1 % | 77,7 % |
| **lstm ↔ mọi model ML khác** | **1,1–18,7 %** | **2,9–37,0 %** |

⇒ **`lstm` là model ML duy nhất độc lập thật.** Sáu model còn lại là một tiếng nói kèm nhiễu.

Cấu trúc phiếu cho số thắng (30 ngày):

| Miền | Phiếu TB | Họ ML | Tỉ lệ | Kết quả 90 ngày |
|---|---|---|---|---|
| MN | 5,26 | 0,94 | 18 % | 16,08 % |
| **MT** | 5,45 | **2,90** | **53 %** | **14,48 %** |
| MB | 5,84 | 0,52 | 9 % | 16,48 % |

**Miền tệ nhất cũng là miền bị nhóm model trùng nhau chi phối nhiều nhất.**

### 3.3 Đo thời gian thật — 90 ngày

| Miền | Chuỗi AI P50 | P95 | **P99** | Biên tới mốc chốt |
|---|---|---|---|---|
| MN | 1 167 s | 1 422 s | 5 273 s | 624–687 phút |
| MT | 265 s | 557 s | **708 s** | 10,8–20,6 phút |
| MB | 241 s | 550 s | **1 317 s** | 13,1–25,0 phút |

**MB không chạy theo đồng hồ — nó chạy theo dữ liệu.** Kết quả miền trước về ở `mốc cuối +32′…37′`,
MB chỉ khởi động được sau đó. Nên mọi mốc cố định cho MB đều là **phỏng đoán về một sự kiện dữ liệu**.

### 3.4 Sự cố deploy giữa cửa sổ live — 01/08

Một lần deploy lúc **17:44:07** rơi vào giữa lúc bundle miền Bắc vừa tạo (17:39:55) và lúc job
dựng lại bundle chạy (17:55). Hậu quả đo được: `bundle_version 1→2`, `model_count 15→14`.

Chứng minh bằng mã băm: lượt kiểm trước đó (16:48–17:00) đã ghi mã băm hai file lõi; sau 17:44:07
cả hai đổi. Đây là **dấu vân tay thời điểm lấy độc lập trước sự việc**.

**Hai nguyên nhân làm mất 1 phiếu, không phải một:**
- một model bị tắt quyền bỏ phiếu lúc 17:44 → bị loại khi dựng lại bundle;
- một model được bật quyền, **nhưng** dòng dữ liệu của nó đã ghi trước deploy với nhãn khác nên
  **không được tính là phiếu chính thức**.

**Cổng an toàn "băm 4 bảng khoá y nguyên" không thể phát hiện việc này** — cổng băm ngay trước và
ngay sau thao tác 17:44, còn thay đổi xảy ra lúc **17:55, tức 11 phút sau khi cổng đã đóng sổ**.
Cổng chứng minh đúng *"việc chép file không tự nó ghi vào cơ sở dữ liệu"*; nó **không** chứng minh
*"deploy không làm đổi đầu ra"*.

**Và một thiệt hại chưa được nhắc:** lần khởi động lại đó cắt ngang vòng đo bóng của miền Bắc —
hôm đó chỉ 3 dòng, sáu ngày trước là 10–12 dòng. **Khoảng 9 model mất dữ liệu đo của đêm đó.**

### 3.5 Mẫu hình lặp lại — cơ chế dựng xong rồi chết

| Cơ chế | Chết bao lâu (tính 04/08) | Vẫn "sống" ở đâu |
|---|---|---|
| Bảng chi phí | **90 ngày** | — |
| Bảng lãi/lỗ | **76 ngày** | job hằng đêm vẫn chạy |
| Chọn nhà vô địch | **50 ngày** | cron 06:25 vẫn chạy, vẫn ghi log |
| Rerank | **26 ngày** | API vẫn khai *đang đo* |
| Tham số cửa sổ tối ưu | **175 ngày** | giá trị lift **âm cả ba miền** |

> Hệ **rất giỏi dựng cơ chế** — có mã, có API, có bảng điều khiển, có tài liệu, có mã theo dõi.
> **Nhưng hay quên lên lịch chạy.** Cơ chế chết ngay sau ngày dựng mà không ai biết, vì bảng điều
> khiển vẫn hiện số cũ.

Ghi nhận tích cực: **cổng lợi thế** — cơ chế quan trọng nhất trong nhóm này — đã được luồng chính
bổ sung lịch chạy hằng ngày sau khi lượt kiểm 02/08 nêu ra.

### 3.6 An ninh — **chi tiết giữ nội bộ**

Phát hiện **3 vấn đề an ninh mức P0** liên quan tới quyền truy cập tệp cấu hình, cách lưu thông
tin xác thực, và quyền ghi thư mục mã nguồn trên máy chủ.

**Chi tiết kỹ thuật KHÔNG công bố ở đây** theo quyết định owner, để tránh chỉ đường khi lỗ hổng
chưa được vá. Đã báo owner đầy đủ từ **01/08**; tính tới 04/08 **chưa được xử lý**.
Đây là mục cần ưu tiên cao nhất ngoài các việc đo lường.

### 3.7 Hai luồng prompt trộn trong cùng một bundle

Điều kiện rẽ nhánh prompt **chỉ xét tên model**, không xét đường chạy. Hệ quả: một model chính
thức vẫn nhận khối prompt của luồng bóng ⇒ **bundle chính thức trộn hai nhóm prompt**, trong khi
bộ chọn cộng mọi phiếu như nhau.

Kèm theo: bảng dữ liệu dự đoán **không có cột ghi nhóm prompt** ⇒ mọi bảng xếp hạng đang trộn hai
nhóm mà không ai biết. Kết luận này ở mức **xác nhận-bằng-mã**, chưa đối chiếu được bằng dữ liệu.

---

## 4. HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Bốn nguyên tắc nền, rút từ đo đạc:**

| # | Nguyên tắc | Bằng chứng |
|---|---|---|
| N1 | Lịch chạy theo **dữ liệu sẵn sàng**, không theo đồng hồ | MB khởi động vì kết quả miền trước về, không vì đến giờ |
| N2 | Mỗi phiếu phải là **một nguồn tin**, không phải một dòng dữ liệu | 6/7 model trùng nhau 61–88 % |
| N3 | Thước quyết định phải là **thước đặt cược** | thước cũ lệch tới −10,9 pp so với thước thật |
| N4 | Không quyết trên khác biệt **nhỏ hơn mức đo được** | cần 380–1 575 ngày để thấy 3 pp |

**Vì sao không vá lẻ tiếp:** một sự cố ngày 03/08 được xử bằng cách **thêm mốc chạy** cho lane.
Cách đó giảm xác suất trượt nhưng không xoá nguyên nhân — bằng chứng: **số dòng lịch tăng
71 → 81 trong 2 ngày**. Nguyên nhân gốc là lane chạy theo đồng hồ còn chuỗi chính xong theo dữ liệu.

---

## 5. ĐÃ LÀM GÌ

- **5 gói kiểm** với đầy đủ tài liệu, bảng máy đọc được, và thư mục bằng chứng có mã băm.
- **Tự đo lại** thay vì tin báo cáo: mã băm tệp hai phía, truy vấn cơ sở dữ liệu chỉ-đọc, đo
  P50/P95/P99 từng chặng 90 ngày, tính lại tỉ lệ trúng và so với ngẫu nhiên.
- **Kiểm chứng độc lập** kết luận "hệ không hơn ngẫu nhiên" của luồng chính — **khớp**.
- **Thiết kế kiến trúc đích** (chưa triển khai): cổng dữ liệu-sẵn-sàng, chuẩn hoá phiếu theo họ,
  lõi prompt chung + bộ chuyển theo model, hợp đồng thước đo, và cổng
  `ĐÃ HUẤN LUYỆN → ĐƯỢC ĐỀ CỬ → ĐÃ TRIỂN KHAI`.
- **Lộ trình 7 đợt**, mỗi đợt **một biến số**, đo 7–14 ngày, không gộp.

---

## 6. CỔNG KIỂM

| Cổng | Kết quả |
|---|---|
| Mốc công bố cuối khớp mã nguồn | ✅ kiểm 6 nơi, đúng ở cả 6 |
| Không dòng nào ghi sau mốc bất động | ✅ 0 dòng, cả ba miền |
| Không mutation trong mọi lượt kiểm | ✅ đã kiểm lại mã băm + PID sau mỗi lượt |
| Không lộ thông tin nhạy cảm trong báo cáo | ✅ lọc tại nguồn truy vấn |
| Tự kiểm nhất quán hằng ngày | ✅ chạy, lệch 0 |

---

## 7. VƯỚNG VẤP

**7.1 Lỗi trình bày của chính người kiểm.** Ở lượt 5, bảng "mốc phân tích nội bộ" được đặt cạnh
nhau mà **không ghi kèm mốc công bố cuối**, khiến owner đọc lướt tưởng người kiểm đề nghị đổi mốc
công bố. Owner phản hồi ngay. **Đã đính chính** bằng một mục riêng đầu báo cáo và bảng hai cột.
Đây là lỗi của người kiểm, không phải của hệ thống.

**7.2 Xung đột giữa quy tắc báo cáo công khai và lệnh trong từng brief.** Quy tắc nội bộ yêu cầu
đẩy báo cáo công khai sau mọi việc; nhưng cả 5 brief đều ghi rõ *"không commit/push"*. Người kiểm
chọn tuân brief và **lẽ ra phải nêu mâu thuẫn này ngay từ lượt 1** để owner quyết — thay vì lặng
lẽ chọn một bên. Chính báo cáo này là việc trả nợ đó.

**7.3 Trạng thái thay đổi ngay trong lúc kiểm.** Ba lần: một commit xuất hiện 4 phút sau khi chụp
trạng thái; một lần khởi động lại dịch vụ giữa lúc đang xuất gói; một commit nữa khi đang viết
báo cáo. Đều **không phải do người kiểm**, và đều đã ghi nhận kèm mốc giờ.

**7.4 Có việc không kiểm được bằng quyền đọc.** Không quan sát được hội thoại giữa owner và các
agent khác ⇒ câu hỏi về thẩm quyền của một lần deploy **chỉ owner trả lời được**.

---

## 8. GỠ VỀ

Không có gì để gỡ — **cả 5 lượt đều không thay đổi gì**. Mọi kết quả nằm trong thư mục artifact
nội bộ, đã được loại khỏi Git, **không nằm trong đường chạy thật**.

Với các đề xuất trong kiến trúc đích: mỗi đợt đều kèm sẵn điều kiện vào, hậu kiểm và cách gỡ về;
đợt đụng đường ra số đều yêu cầu **chạy song song trước khi cắt bản cũ**.

---

## 9. THEO DÕI TIẾP

| Việc | Ghi chú |
|---|---|
| **Vá 3 vấn đề an ninh P0** | báo từ 01/08, chưa xử — ưu tiên cao nhất |
| Khôi phục bảng chi phí + lãi/lỗ | quyết định về tiền mà công cụ đo tiền chết 76–90 ngày |
| Thêm phép tự kiểm *"bảng khai đang đo phải tươi ≤48 h"* | bắt được cả 5 ca chết âm thầm và mọi ca tương lai |
| Thêm cột ghi nhóm prompt | để bảng xếp hạng thôi trộn hai nhóm |
| Đo chuẩn hoá phiếu theo họ | cơ chế đã chạy ở luồng bóng — chỉ cần so, chưa cần mã mới |
| Ba câu chờ owner | thẩm quyền lần deploy 17:44 · xử lý mục đóng băng bị trái · ngày khuyết 01/08 |

**Nguyên tắc bắt buộc cho mọi việc kế tiếp:** một biến số mỗi lần, đo 7–14 ngày, không gộp.
