# REPORT V11114 — CÂU LỊCH SỬ: **KHÔNG CÓ VI PHẠM NÀO (0/532)** · BỘ ĐO CỦA CHÍNH PHIÊN NÀY CÓ **14 LỖI**

**Ngày:** 24/08/2026 (chiều) · **Kho riêng:** `de7dfe8` · **Trạng thái:** `REPORT_PROVEN` + `CODE_PUSHED`
**KHÔNG deploy · KHÔNG chạm production** — toàn bộ đọc-only.

> ⚠️ **`RM-12`:** phiên này **không** có gì đạt `RUNTIME_PROVEN`.

---

## 1 · TÓM TẮT

Năm làn đo + **năm làn phản biện** đọc-only (1,16 triệu token · 241 lượt gọi · 0 lỗi).
**Phản biện bác kết luận đầu của chính làn đo**, và bác luôn một câu em vừa báo owner.

| câu hỏi | trả lời |
|---|---|
| FINAL có bị đổi **sau** mốc khoá không? | 🟢 **KHÔNG** — `VI PHẠM 0/532`; kỳ mốc hiện hành **70/70** ghi trước mốc |
| bộ đo dùng để trả lời câu trên có đúng không? | 🔴 **KHÔNG** — **14 lỗi**, lỗi 1 sinh verdict **tự mâu thuẫn đã trình owner**. Đã vá, thử chặn **21/21** |
| khối dữ liệu đổi lúc T-chốt có ảnh hưởng kết quả không? | 🟢 **KHÔNG** — replay **531/531** chứng minh nó thuần chẩn đoán |
| có cửa hậu nào đi xuyên cổng khoá không? | 🟡 **CÓ, có thiết kế** — `require_admin`, **chưa từng dùng** (0 dòng) |

---

## 2 · OWNER YÊU CẦU GÌ (NGUYÊN VĂN)

> *«`P0-A` ảnh chụp + diff `v1/v2` **trước MN 15:45**.»*

> *«Cấm thay thuật toán mù.» · «Cấm tự quyết.» · «Agent phân tích mặc định chỉ được READ-ONLY.»*

> *«Cấm gọi `CODE_PUSHED` hoặc `DEPLOYED` là `RUNTIME_PROVEN` trước lượt live thật.»*

---

## 3 · ĐÀO BỚI / PHÁT HIỆN

### 3.1 · 🟢 Câu lịch sử — KHÔNG có vi phạm

```
TRƯỚC mốc 150 · VI PHẠM 0 · KHÔNG TRUY ĐƯỢC trong phạm vi 1 · ngoài phạm vi 381 · tổng 532
Kỳ mốc hiện hành (từ 01/08): 70/70 ghi TRƯỚC mốc · 0 vi phạm · 0 không truy được
```

### 3.2 · 🔴 Làn đo báo *«1 vi phạm»* — phản biện **bác sạch bằng ba bằng chứng độc lập**

Làn đo kết luận một bundle ngày 31/07 ghi đúng `15:45:00` là vi phạm mốc `15:45`.

| # | bằng chứng bác |
|---|---|
| **a** | commit đổi mốc từ `15:55` xuống `15:45` xảy ra lúc **`31/07 16:19:34`** — **34 phút SAU** lần ghi. Làn đo dùng `git log --date=short` rồi coi mốc mới có hiệu lực cả ngày ⇒ **đo ở mức NGÀY cho sự kiện ở mức PHÚT** |
| **b** | **vân tay runtime:** log của lần ghi đó chứa chuỗi **CŨ viết cứng** *«freeze mốc :55 sẽ khoá»*; cùng ngày, miền khác đã ghi chuỗi **MỚI sinh động**. Bản cũ vẫn đang chạy lúc đó |
| **c** | `CHANGELOG` ghi chính bundle đó là **dấu vết phát hiện ĐỂ ĐỔI MỐC**. Lấy sự cố **sinh ra luật** để tính là vi phạm chính luật đó là **ngược chiều thời gian**. `CHANGELOG` còn ghi *«hôm nay số không đổi»* |

Và *«79 dòng không truy được»* bị **đếm chồng** — 78 nằm trong nhóm 303 dòng **trước khi cổng
khoá ra đời**, đã đếm riêng. Thực sự không truy được: **đúng một dòng**.

### 3.3 · 🔴 Cột giờ của bảng log là **UTC** — quy ước giờ **thứ TƯ**, tài liệu chưa ghi

Cột dùng `DEFAULT CURRENT_TIMESTAMP` và hàm ghi **không truyền giờ** ⇒ SQLite ghi UTC.

**Chứng minh, không giả định:** giá trị lớn nhất là `08:55:00` trong khi giờ máy chủ là
`15:57:27`. Và cụm công việc T-chốt của hai miền rơi đúng `09:55` và `10:55` UTC — **cộng 7 giờ
ra đúng mốc đã đăng ký**, khớp trên **hai miền độc lập**.

> ⚠️ Đọc thẳng như giờ VN sẽ kết luận T-chốt **chạy lúc 08:40 sáng** — sai 7 tiếng.
> Tài liệu quản trị liệt kê **ba** quy ước giờ; **thiếu bảng này**. Cần bổ sung.

### 3.4 · 🔴 Bộ đo của chính phiên này có **14 lỗi**

**Lỗi 1 đã gây hậu quả thật:** verdict *«chỉ trường settlement/meta đổi»* được in ra **mỗi khi
danh sách vi phạm rỗng**, **không hề kiểm** có cột mang-dự-đoán nào đổi hay không. Kết quả: bảng
in rõ một cột `PREDICTION_BEARING` đã đổi, mà dòng tổng kết ngay dưới nói ngược lại —
**tự mâu thuẫn, và verdict đó ĐÃ ĐƯỢC TRÌNH CHO OWNER**.

Các lỗi khác: miền không có trong ảnh gốc bị **bỏ qua im lặng** · cắt chuỗi làm hai giá trị khác
nhau **in ra giống hệt** đúng lúc cần bằng chứng · băm **không so được** vì có giờ chụp bên trong ·
thử chặn 9/9 **không bao giờ gọi hàm chính** · tham số ngày đi thẳng vào chuỗi shell · câu
*«không ghi một byte nào»* **sai theo nghĩa đen** · đường dẫn tương đối theo thư mục hiện hành ·
hàm tên *«mới nhất»* trả về **cũ nhất**.

**Lỗi 13** (tự tìm): cổng **neo vào giờ xổ** thay vì mốc khoá ⇒ cửa sổ mù ~45 phút.

**Lỗi 14 sinh ra TỪ CHÍNH BẢN VÁ LỖI 13** (`RM-07` — vá một lỗi không phải vá cả họ lỗi): vá xong
thì cổng **báo động giả mỗi ngày**, vì cửa sổ so sánh **vắt qua mốc** — biết «đã đổi» nhưng không
biết «đổi lúc nào». **Một cổng kêu oan mỗi ngày sẽ bị tắt — đúng cách cổng chết.**

**Vá cuối — verdict BA CHIỀU:**

```
giờ ghi < mốc   ⇒ TRƯỚC MỐC, hợp đồng cho phép
giờ ghi ≥ mốc   ⇒ VI PHẠM
không truy được ⇒ KHÔNG TRUY ĐƯỢC — báo, KHÔNG kết luận vi phạm, KHÔNG gọi là sạch
```

Chiều thứ ba hay bị bỏ: writer chấm kết quả ghi đè cột giờ, nên với hàng đã chấm thì giờ ghi dự
đoán **đã bị xoá**. Gọi là *«sạch»* là **nói quá**; gọi là *«vi phạm»* là **vu oan**.

Thử chặn **21/21**. Chạy lại: `VI PHẠM 0`, verdict *«ghi lúc 15:40 < mốc 15:45»*.

### 3.5 · 🟢 Khối dữ liệu đổi lúc T-chốt là **thuần chẩn đoán** — replay **531/531**

Writer chấm kết quả đọc **đúng 5 khoá số**. Cả tệp chứa nó **không một tham chiếu nào** tới khối
dữ liệu đã đổi.

**Chứng minh thực nghiệm (`RM-11`, tái lập được):** chấm lại **531** bundle đã verified chỉ từ
5 cột số + bảng kết quả xổ:

```
bạch thủ 531/531 · lô 2 531/531 · xiên 2 531/531 · xiên 3 531/531 = 100,00%
3 càng 499/531 — 32 dòng lệch TẤT CẢ nằm trong 01/03–27/03, TẤT CẢ khớp lỗi 2-chữ-số cũ
                 mà mã nguồn đã ghi chú rõ. Di sản mã cũ, KHÔNG phải bằng chứng ảnh hưởng điểm.
```

**Chiều nhân quả NGƯỢC lại:** hàm sinh khối đó **nhận số đã chọn làm đầu vào**; docstring ghi
*«informational only, does not change ranking/scoring»*.

### 3.6 · 🟡 Cửa hậu `owner_force` — **có thiết kế**, có kiểm soát, **chưa từng dùng**

Một chuỗi ma thuật trong trường ghi chú tự do sẽ **đi xuyên cổng khoá**. Chú thích ghi rõ đây là
*«bypass hợp lệ duy nhất — lệnh owner tường minh»*. Endpoint **có `require_admin`**. Đo thật:
**0 dòng** từng dùng, **0 dòng log**.

> 🟡 Hệ quả phụ: trường ghi chú vừa là **kênh điều khiển** vừa là **danh tính writer** ⇒
> **không tin được** như bằng chứng xuất xứ thuần.

### 3.7 · 🔴 Trường ghi chú **KHÔNG** dùng làm danh tính writer được

Mệnh đề ghi-đè có `notes = excluded.notes` ⇒ **writer thứ hai XOÁ HẲN nhãn của writer thứ nhất**.
Bằng chứng: cả **147** dòng mang nhãn T-chốt đều được **TẠO** vào giờ **không phải** mốc T-chốt.

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Chọn: đo, phản biện chính mình, vá bộ đo — KHÔNG sửa production.**

1. Owner khoá *«Cấm thay thuật toán mù»* + *«Cấm tự quyết»*.
2. Một bộ đo sai **nguy hiểm hơn không có bộ đo**, vì nó phát ra dấu xanh. Lỗi 1 đã chứng minh
   điều đó bằng một verdict tự mâu thuẫn **đã tới tay owner**.
3. `RM-15`: cổng chưa qua thử **coi như không tồn tại**.

---

## 5 · ĐÃ LÀM GÌ

| # | việc | trạng thái |
|---|---|---|
| 1 | Năm làn đo + **năm làn phản biện** đọc-only | 🟢 0 lỗi |
| 2 | Vá **14 lỗi** của bộ đo ảnh FINAL | 🟢 thử chặn **21/21** |
| 3 | Chạy lại diff bằng bản vá | 🟢 `VI PHẠM 0`, verdict khớp bảng |
| 4 | Hợp đồng FINAL §6 — chín mục con, đầy đủ bằng chứng | 🟢 |
| 5 | Rút lại **hai câu** đã nói với owner trong chính phiên | 🟢 |
| 6 | Bốn mặt version | 🟢 cổng **ĐẠT** |

---

## 6 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| thử chặn bộ đo ảnh FINAL | 🟢 **21/21** |
| thử chặn hai cổng bất biến | 🟢 **17/17** |
| bốn mặt version | 🟢 **ĐẠT** |
| an toàn báo cáo công khai | 🟢 chạy trước khi đẩy |
| DB production nguyên vẹn | 🟢 từng byte |

---

## 7 · VƯỚNG VẤP

**7.1 · Làn đo kết luận sai, phản biện bắt được.** Nếu chỉ chạy làn đo thì báo cáo này đã công bố
*«có 1 vi phạm»* — sai. Bài học: **đo xong phải cho người khác cố bác**.

**7.2 · Lỗi 14 sinh ra từ chính bản vá lỗi 13.** `RM-07` đúng nguyên văn: vá một lỗi không phải
vá cả họ lỗi.

**7.3 · Phản biện bắt lỗi của phản biện.** Một làn phản biện bác *«hai cổng chưa từng thử lửa»* —
đúng, nhưng nó cũng nói quá: bài thử chỉ phủ **một** trong hai cổng. Đã sửa tại chỗ.

**7.4 · Làn đo tự nhận *«TOÀN BỘ điểm đọc»* mà bỏ sót hẳn một tệp lớn.** Đó là
`A58_VIOLATION_NO_REVERSE_SCAN`. **Vế chất vẫn đứng** — phản biện đọc từng điểm bị bỏ sót và
không điểm nào chấm điểm.

---

## 8 · GỠ VỀ

**Không có gì để gỡ** — không sửa mã production, không deploy, không restart. Thay đổi duy nhất
là **vá một công cụ đo độc lập** và **thêm tài liệu**.

---

## 9 · THEO DÕI TIẾP

| # | việc | chặn ở đâu |
|---|---|---|
| 1 | Bổ sung tài liệu quản trị: bảng log dùng **UTC**, phải cộng 7 giờ | nên làm ngay |
| 2 | Cổng khoá **thứ hai** chưa có thử lửa riêng | **cần owner ký** |
| 3 | Trường ghi chú không dùng làm danh tính writer được — cần cột xuất xứ riêng | **cần owner ký** — đổi lược đồ |
| 4 | Cửa hậu qua trường tự do — nên đổi thành tham số tường minh | **cần owner ký** |
| 5 | **32 dòng** trạng thái WIN giả trong `01/03–27/03` chưa chấm lại | **cần owner ký** — đổi thành tích đã ghi |

---

## 10 · BA LỚP NGUỒN (§62 · A60)

### `OWNER_SAID`

> *«`P0-A` ảnh chụp + diff `v1/v2` **trước MN 15:45**.»* — prompt 34
> *«Cấm tự quyết.» · «Agent phân tích mặc định chỉ được READ-ONLY.»* — prompt 33/34

### `CODE_DID`

| điều mã **thực sự** làm | bằng chứng |
|---|---|
| FINAL **không** bị đổi sau mốc | `0/532` vi phạm; kỳ hiện hành `70/70` trước mốc |
| T-chốt ghi lúc `15:40`, trước mốc `15:45` | cột giờ của hàng chưa chấm |
| khối dữ liệu đổi **không** vào đường chấm điểm | replay `531/531` |
| bảng log ghi **UTC** | giá trị lớn nhất `08:55` khi máy chủ `15:57`; hai miền độc lập khớp `+7h` |
| writer thứ hai **xoá nhãn** writer thứ nhất | mệnh đề ghi-đè có `notes = excluded.notes` |

### `DOC_SAID`

| tài liệu | nói gì | khớp mã? |
|---|---|---|
| tài liệu quản trị §55 | ba quy ước giờ | 🔴 **THIẾU** bảng log (UTC) — quy ước thứ tư |
| hợp đồng FINAL §2.5 (bản sửa đầu) | *«HAI cổng đã chứng minh chặn thật»* | 🔴 **nói quá** — chỉ một cổng. Đã sửa tại chỗ |
| tin nhắn cho owner ~16:00 | *«cột ghi chú khai tên writer»* | 🔴 **KHÔNG ĐỦ** — đã rút lại |

### 🔴 BA LỚP LỆCH NHAU — finding bắt buộc báo

**`DOC_SAID` ≠ `CODE_DID`** ở ba chỗ, **cả ba do chính em viết trong phiên này**, và **cả ba đã
rút lại** đúng chỗ đã công bố.

**Hai câu đã nói với owner, rút lại:**

① *«cột ghi chú khai tên writer»* — **không đủ**: nó chỉ ghi writer **cuối**, **xoá** nhãn writer
trước, và **giả mạo được** qua endpoint admin.
② *«không cột nào ghi lại giờ của lần ghi thứ hai»* — **quá rộng**: đúng với hàng **đã chấm**,
**sai** với hàng **chưa chấm**, và chính cột đó đã phân xử được ngày 24/08.

**Quyết định nào đã dựa trên hai câu này:** **chưa cái nào**.

---

TanPhatAI cần làm: bổ sung tài liệu quản trị §55 quy ước giờ **thứ tư** — bảng log ghi **UTC**, phải cộng 7 giờ, nếu không mọi phép đo theo giờ trên bảng đó sẽ lệch 7 tiếng; ghi nhận **hai câu đã rút lại** để không trích lại bản cũ; theo dõi năm mục ở §9, trong đó **bốn mục cần owner ký**; **KHÔNG** dùng kết luận *«có 1 vi phạm ngày 31/07»* làm căn cứ cho bất kỳ quyết định nào — nó **đã bị bác** bằng ba bằng chứng độc lập.
