# REPORT V11125 — D-24 · CHUẨN BỊ BẰNG CHỨNG (READ-ONLY) · ĐỐI CHIẾU V11124 · RUNBOOK XOAY CREDENTIAL · CHỨNG MINH HOOK HAI RUNTIME

```
REPORT_VERSION              : V11125
REPORT_TITLE                : D-24 chuẩn bị bằng chứng read-only — đối chiếu V11124,
                              hiệu lực credential, runbook xoay, chứng minh hook hai runtime
WORK_DATE_ICT               : 2026-08-26
PUBLISHED_AT_ICT            : xem mục bàn giao
TIMEZONE                    : Asia/Ho_Chi_Minh / UTC+07:00
OWNER_DECISION              : D-22 INVENTORY_ONLY + D-23 REPORT_ONLY_PUSH + D-24 KEEP_PUBLIC_CURRENT
AUTHORIZED_SCOPE            : READ_ONLY_EVIDENCE_PREPARATION + REPORT_ONLY_PUBLIC_SAFE
PREVIOUS_PUBLIC_HEAD        : bc1e15a44b5a523f152d346751f868d19add97f0  (đo lại đầu phiên)
V11124_PUBLICATION_COMMIT   : ebfdf188eac1c709e58cc950499ec7b4d2ab3329
V11124_METADATA_COMMIT      : bc1e15a44b5a523f152d346751f868d19add97f0
INVENTORY_SOURCE_HEAD       : a4d66364a6ef3127152eae1b1ae6957250f3c8e6  (kho riêng — KHÔNG push)
ACTOR_RUNTIME               : CURSOR_AGENT_AND_CLAUDE_CODE  (phiên này: Claude Code)
LABELS                      : SECURITY_EVIDENCE · READ_ONLY · RECONCILIATION ·
                              ROTATION_PACKET_PARTIAL · DUAL_AGENT_RUNTIME · OWNER_DECISION_PENDING
```

> ⛔ **D-24 = `KEEP_PUBLIC_CURRENT` KHÔNG có nghĩa kho đã an toàn hay exposure đã đóng.**
> Phiên này **không** xoay credential, **không** scrub, **không** rewrite, **không** sửa hook thật,
> **không** deploy `FU-438`, **không** sửa production.

---

## 1 · TÓM TẮT BẰNG LỜI THƯỜNG

Phiên này không xử lý gì. Nó đi **kiểm lại chính những con số mình đã công bố**, và tìm ra **ba
chỗ sai của báo cáo trước** cùng **một chỗ mà công cụ đo đã nói dối**.

Bốn điều đáng kể nhất:

| | |
|---|---|
| 🔴 **Số credential tăng từ 4 lên 7** | V11124 ghi *«4 giá trị mật khẩu phân biệt»*. Quét bằng **hợp của mọi mẫu** ra **7 giá trị**: **3 `CONFIRMED`** cần xoay · 1 `FALSE_POSITIVE` · **3 `NOT_VERIFIED`**. Con số 4 chỉ là kết quả của **một** biểu thức tìm kiếm |
| 🔴 **Con số «24» của V11124 bị BÁC** | Không phép đếm nào từ bảng hợp nhất ra 24. Số đúng là **23 / 28 / 18** tuỳ thước |
| 🔴 **Một phép đo của chính V11124 đã nói dối** | Phép «pickaxe» báo `0 commit` cho nhóm mật khẩu. Thử chặn cho thấy đó là **lỗi cú pháp** — công cụ dùng regex POSIX, không hiểu cú pháp đã viết. Số thật: **24 commit** |
| 🟢 **Bốn cổng Cursor thiếu điểm danh đã có bản vá, thử 5/5 ĐẠT** | Trên **bản sao cô lập**. Cấu hình thật **0 thay đổi** |

Và một điều **không làm được**: đọc cấu hình máy chủ. Anh đã cấp `VPS_CONFIG_READ_ONLY`, nhưng
**lớp phân quyền của công cụ chặn lệnh kết nối ra ngoài**. Tôi **dừng, không đi vòng**. Hệ quả là
**mọi trạng thái hiệu lực của credential đều là `NOT_VERIFIED`**, và runbook xoay chỉ đạt mức
**`ROTATION_PACKET_PARTIAL`**.

---

## 2 · ĐỐI CHIẾU V11124

> Theo `PRJ-RETRACTION-001`: **không sửa `REPORT_V11124`**. Đây là phụ lục đính chính, có đủ
> bốn phần cho từng chỗ sai.

### 2.1 · Bảng đối chiếu — mọi tổng số **tính từ bảng**, không gõ tay

Công thức bắt buộc:

```
TOTAL = CRITICAL_SECRET + AUTH_MATERIAL + INFRASTRUCTURE_EXPOSURE + INTERNAL_PATH
      + OPERATIONAL_DETAIL + MENTION_ONLY + FALSE_POSITIVE + HISTORY_ONLY + UNRESOLVED
```

| nhóm | số | tính vào `TOTAL`? | mã |
|---|---|---|---|
| `CRITICAL_SECRET` | **4** | ✅ CÓ | `SC-01` `SC-02` `SC-03` `SC-04` |
| `AUTH_MATERIAL` | **3** | ✅ CÓ | `AM-01` `AM-02` `AM-03` |
| `INFRASTRUCTURE_EXPOSURE` | **6** | ✅ CÓ | `IE-01` … `IE-06` |
| `INTERNAL_PATH` | **4** | ✅ CÓ | `IP-01` … `IP-04` |
| `OPERATIONAL_DETAIL` | **5** | ✅ CÓ | `OD-01` … `OD-05` |
| `MENTION_ONLY` | **1** | ✅ CÓ | `MO-01` |
| `FALSE_POSITIVE` | **5** | ✅ CÓ | `FP-01` … `FP-05` |
| `HISTORY_ONLY` | **2** | ✅ CÓ | `HO-01` `HO-02` |
| `UNRESOLVED` | **1** | ✅ CÓ | `SC-05-CANDIDATE` |
| **`TOTAL`** | **31** | | |
| `NOT_CHECKED` | **4** | ❌ **KHÔNG** | `NC-01` … `NC-04` |
| **tổng số dòng bảng** | **35** | | |

`4 + 3 + 6 + 4 + 5 + 1 + 5 + 2 + 1 = 31` ✅

> `NOT_CHECKED` **không** vào `TOTAL` vì nó là **phạm vi chưa kiểm**, không phải finding. Gộp nó
> vào là trộn hai loại khác nhau.

### 2.2 · Phân bổ theo scope — mỗi finding thuộc **đúng một** scope

| scope | tổng dòng | tính vào `TOTAL` | `NOT_CHECKED` |
|---|---|---|---|
| `PUBLIC_HEAD` | 24 | **23** | 1 |
| `PUBLIC_HISTORY` | 3 | **2** | 1 |
| `PRIVATE_HEAD` | 6 | **5** | 1 |
| `PRIVATE_HISTORY` | 1 | **0** | 1 |
| `VPS_RUNTIME` | 1 | **1** | 0 |
| **cộng** | **35** | **31** | **4** |

### 2.3 · 🔴 RÚT LẠI R-1 — con số «24 `CURRENT_HEAD_EXPOSURE`»

| phần | nội dung |
|---|---|
| **chỗ gốc** | `REPORT_V11124` mục **3.D**, phát hành 26/08 10:11:40 |
| **nguyên văn câu sai** | *«`CURRENT_HEAD_EXPOSURE` \| **24** \| toàn bộ `IE-*` · `IP-*` · `OD-*` · `AM-*` · `SC-*`»* |
| **điều đúng** | Danh sách được nêu cộng lại ra **22**, không phải 24. Từ bảng hợp nhất, ba phép đếm hợp lệ là: `PUBLIC_HEAD` tính vào `TOTAL` = **23** · `PUBLIC_HEAD + PRIVATE_HEAD` = **28** · `PUBLIC_HEAD` trừ `FALSE_POSITIVE` = **18**. **Không phép nào ra 24.** Con số 24 khớp với *số dòng scope `PUBLIC_HEAD`* **kể cả `NC-01`** — nhưng `NC-01` là **phạm vi chưa kiểm**, không phải exposure, nên nhãn đó sai |
| **quyết định đã dựa trên số sai** | `PACKET 2` (scrub HEAD) mục *«công sức dự kiến»* ước theo «24 finding» ⇒ phải đọc lại là **23**, và nếu tính cả `PRIVATE_HEAD` thì **28** |

### 2.4 · 🔴 RÚT LẠI R-2 — câu «0 credential trong kho công khai»

| phần | nội dung |
|---|---|
| **chỗ gốc** | `REPORT_V11124` mục **1** và mục **3.F** |
| **nguyên văn câu sai** | *«Trên kho công khai, kiểm kê tìm thấy **0 vật liệu xác thực**»* — viết ở **giọng tuyệt đối** |
| **điều đúng — câu thay thế bắt buộc dùng từ nay** | **«Không phát hiện known credential pattern trong phần văn bản đã kiểm của `PUBLIC_HEAD` và `PUBLIC_HISTORY` bằng bộ rule hiện có; không có entropy scanner, binary còn `NOT_CHECKED`, nên `CREDENTIAL_COMPROMISE_NOT_PROVEN`.»** |
| **quyết định đã dựa trên số sai** | `PACKET 1` (containment) và `PACKET 3` (rewrite) đều xếp mức khẩn **thấp** một phần vì tin *«kho công khai sạch tuyệt đối»*. Mức đúng là **chưa chứng minh có bẩn**, không phải **đã chứng minh sạch** |

### 2.5 · 🔴 RÚT LẠI R-3 — số giá trị mật khẩu

| phần | nội dung |
|---|---|
| **chỗ gốc** | `REPORT_V11124` mục **3.C**, dòng `SC-04` |
| **nguyên văn câu sai** | *«`SC-04` — `SECRET-CANDIDATE-02..05` — **4 giá trị mật khẩu phân biệt**, dạng văn bản thường \| 48 tệp»* |
| **điều đúng** | Quét bằng **hợp của mọi mẫu**, dedupe theo giá trị: **7 giá trị phân biệt**. Phân loại: **3 `CONFIRMED`** · 1 `FALSE_POSITIVE` · **3 `NOT_VERIFIED`**. Bảng đầy đủ ở mục **4** |
| **quyết định đã dựa trên số sai** | `PACKET 4` (xoay credential) — **phạm vi xoay tăng**: ngoài credential triển khai còn ít nhất **hai** giá trị nữa được xác nhận, thuộc **hai trường khác nhau** |

### 2.6 · 🔴 RÚT LẠI R-4 — một phép đo đã nói dối

| phần | nội dung |
|---|---|
| **chỗ gốc** | dữ liệu nền của `V11124`, nhánh «phương pháp độc lập thứ hai» |
| **nguyên văn câu sai** | *«`SC-04`: **0 commit** từng thêm/bớt mẫu này»* |
| **điều đúng** | `0` đó là **lỗi cú pháp**, không phải bằng chứng: công cụ dùng regex **POSIX**, không hiểu cú pháp không-phân-biệt-hoa-thường đã viết. **Thử chặn theo `RM-15`**: đối chứng *«chuỗi chắc chắn CÓ»* → **585 commit** (công cụ hoạt động) · đối chứng *«chắc chắn KHÔNG»* → `0`. Viết lại bằng cú pháp đúng: **24 commit** chạm `password=`, **38 commit** chạm chuỗi `password` |
| **quyết định đã dựa trên số sai** | Không quyết định nào — bắt được **trước** khi nó vào kết luận. Nhưng nó suýt thành bằng chứng *«mật khẩu chưa bao giờ vào lịch sử»*, tức **ngược hẳn sự thật** |

> 🔴 Đây đúng bài học `RM-15`: **một phép kiểm không có đối chứng thì luôn báo xanh**. Từ nay mọi
> phép «đếm bằng công cụ tìm kiếm» phải kèm **hai đối chứng** — một chuỗi chắc chắn có, một chuỗi
> chắc chắn không.

### 2.7 · Hoà giải metadata

| trường | giá trị | ghi chú |
|---|---|---|
| `V11124_PUBLICATION_COMMIT` | `ebfdf188…` | commit **phát hành** — 26/08 **10:11:40 +0700** |
| `V11124_METADATA_COMMIT` | `bc1e15a4…` | commit **điền metadata** — 26/08 **10:13:29 +0700** |
| `CURRENT_PUBLIC_HEAD` đầu phiên D-24 | `bc1e15a4…` | **đo lại**, không chép mù |

**Ba trường này KHÔNG được dùng chung một ô.** Hiện `CURRENT_PUBLIC_HEAD` **tình cờ bằng**
`METADATA_COMMIT` vì đó là commit mới nhất; đã xác minh **cả hai commit đều là tổ tiên của HEAD**.

**Giải thích «session net = 2 tệp added» trong khi commit metadata có sửa một tệp:** đúng, và
không mâu thuẫn. Commit phát hành **thêm** 2 tệp; commit metadata **sửa** 1 trong 2 tệp **vừa
thêm đó**. Tính chênh lệch **từ `28c6891` tới HEAD** thì Git gộp lại thành **2 tệp `A`, 0 tệp
`M`** — vì tệp bị sửa chưa từng tồn tại ở điểm đầu. **Không có báo cáo cũ nào bị chạm.**

---

## 3 · BẢNG SCOPE — PUBLIC / PRIVATE / HISTORY / RUNTIME

| scope | đã kiểm | phương pháp | còn thiếu |
|---|---|---|---|
| `PUBLIC_HEAD` | ✅ | 2.572/2.599 tệp = **98,9 %** | 27 tệp ảnh |
| `PUBLIC_HISTORY` | ✅ | **3.206/3.262 blob = 98,3 %**, gồm cả blob không còn reachable | 56 blob nhị phân |
| `PRIVATE_HEAD` | ✅ | 3.600/3.639 tệp | 39 tệp nhị phân |
| **`PRIVATE_HISTORY`** | ✅ **MỚI ĐÓNG TRONG PHIÊN NÀY** | **10.615/10.743 blob = 98 %**, hai phương pháp độc lập | 128 blob nhị phân |
| **`VPS_RUNTIME`** | ❌ | — | 🔴 **`BLOCKED_PERMISSION`** — xem mục 5 |

> 🟢 **`NC-03` đã đóng.** V11124 ghi *«toàn bộ lịch sử kho riêng — `NOT_CHECKED`»*. Phiên này quét
> **10.743 blob**, đọc được **98 %**. Đây là phần tăng phạm vi lớn nhất của D-24.

---

## 4 · BẢNG HIỆU LỰC CREDENTIAL

> ⛔ Không in giá trị · không in dấu vân tay · không in tên tệp dẫn đường · không in lệnh nguyên
> văn. **Không thử đăng nhập. Không gọi API bằng khoá. Không gửi bí mật qua mạng.**

### 4.1 · Nhóm không phải mật khẩu

| Alias | Loại | Scope | Ở `PRIVATE_HEAD` | Trong `PRIVATE_HISTORY` | Consumer / dịch vụ | Validity status | Phụ thuộc khi xoay | Rủi ro nếu hỏng | Gián đoạn | Khoảng trống bằng chứng |
|---|---|---|---|---|---|---|---|---|---|---|
| **`SC-01`** | khoá **riêng** SSH, không passphrase | `PRIVATE_HEAD` + `PRIVATE_HISTORY` | ✅ **8 tệp** — 5 mã nguồn, **3 trong ảnh chụp `/etc`** | ✅ **10 blob** · **19 commit** | dịch vụ SSH của máy chủ *(suy từ vị trí trong ảnh chụp `/etc`)* | 🔴 **`NOT_VERIFIED`** | phải sinh lại **trước** khi thu hồi đường cũ | 🔴 **CAO** — sai là mất đường vào | có, ngắn | **không đọc được máy chủ** ⇒ không biết khoá đang chạy có **trùng** khoá đã commit không |
| **`SC-02`** | tệp bóng mật khẩu hệ thống, 1 hash thật | `PRIVATE_HEAD` | ✅ 1 tệp — **ảnh chụp `/etc`** | ✅ 1 blob | xác thực hệ thống | 🟠 **`NOT_VERIFIED`** — dấu hiệu nghiêng về **ảnh chụp**, không phải nguồn sống | đi kèm `SC-04` | TB | không | chưa đối chiếu được với tệp đang chạy |
| **`SC-03`** | khoá API nhà cung cấp mô hình | `PRIVATE_HEAD` | ✅ 1 tệp — **trong bản sao lưu** | ✅ 1 blob · **14 commit** | tiến trình gọi mô hình | 🟠 **`NOT_VERIFIED`** | độc lập — xoay được riêng | 🟢 **THẤP** — thu hồi + cấp lại là thao tác chuẩn | không | không biết tiến trình đang chạy có tham chiếu khoá **này** không |

### 4.2 · Nhóm mật khẩu — **7 giá trị phân biệt**, thay cho con số «4» của V11124

| Alias | Trường | Độ dài | Số tệp | Độ phức tạp | Phân bố tệp | Verdict | Xoay? |
|---|---|---|---|---|---|---|---|
| **`SC-04`** | biến triển khai | 16 | **40** | **4/4** | 16 script triển khai · 21 mã nguồn · 3 test | 🔴 **`CONFIRMED`** | ✅ **BẮT BUỘC** |
| **`SC-05-CANDIDATE`** | trường mật khẩu chung | 18 | 5 | 3/4 | 5 mã nguồn | 🔴 **`CONFIRMED`** | ✅ **BẮT BUỘC** |
| **`SC-08-CANDIDATE`** | mật khẩu quản trị ứng dụng | 28 | 1 | 3/4 | 1 mã nguồn | 🔴 **`CONFIRMED`** | ✅ **BẮT BUỘC** |
| `SC-06-CANDIDATE` | trường rút gọn | 26 | 3 | 2/4 | 1 mã nguồn · **2 bản sao lưu** | 🟡 `NOT_VERIFIED` | ⚠️ cần một lượt nữa |
| `SC-09-CANDIDATE` | trường rút gọn | 11 | 1 | 2/4 | 1 mã nguồn | 🟡 `NOT_VERIFIED` | ⚠️ cần một lượt nữa |
| `SC-10-CANDIDATE` | trường mật khẩu chung | 9 | 1 | 4/4 | 1 mã nguồn | 🟡 `NOT_VERIFIED` | ⚠️ cần một lượt nữa |
| `SC-07-CANDIDATE` | trường mật khẩu chung | 8 | 2 | 2/4 | **chỉ test/demo** | 🟢 **`FALSE_POSITIVE`** | ❌ không |

**Trả lời dứt điểm câu «4 hay 5» mà V11124 để treo:** **cả hai đều sai** — con số phụ thuộc
**biểu thức tìm kiếm**, và hợp của mọi mẫu cho **7**. Không còn số nào treo: mỗi giá trị có
**đúng một verdict**.

> ⛔ **Ba quy tắc đã tuân thủ tuyệt đối:** «có trong Git» **không** tự động bằng «đang có hiệu
> lực» — nên **mọi** dòng đều là `NOT_VERIFIED`, không dòng nào ghi `ACTIVE_RUNTIME_PROVEN`.
> Và «không thấy consumer» **không** tự động bằng «đã vô hiệu» — nên `SC-07` là `FALSE_POSITIVE`
> **vì chỉ nằm trong tệp thử nghiệm**, không phải vì không tìm thấy consumer.

### 4.3 · Bản đồ consumer / phụ thuộc

```
   ┌──────────────────────┐
   │  SC-03  khoá API     │  độc lập hoàn toàn — xoay riêng, không chặn ai
   └──────────────────────┘

   ┌──────────────────────┐        ┌─────────────────────────┐
   │  SC-01  khoá host    │───────▶│  đường vào quản trị      │
   └──────────────────────┘        │  (mọi thao tác từ xa)   │
   ┌──────────────────────┐        └─────────────────────────┘
   │  SC-04  mật khẩu     │───────▶ 16 script triển khai ────┘
   │         triển khai   │
   └──────────────────────┘
             │
             └──▶ SC-02 (bóng mật khẩu) — cùng gốc tài khoản

   ┌──────────────────────┐
   │  SC-05 · SC-08       │  ứng dụng — chưa xác định consumer runtime
   └──────────────────────┘
```

🔴 **Thứ tự bắt buộc:** `SC-01` **trước** `SC-04`. Xoay mật khẩu trước khi bảo đảm đường vào bằng
khoá là **tự khoá mình ra ngoài**.

---

## 5 · 🔴 `VPS_RUNTIME` — `BLOCKED_PERMISSION`

Anh cấp `VPS_CONFIG_READ_ONLY` với danh sách thao tác cụ thể. Tôi đã chuẩn bị đủ:

| việc đã chuẩn bị | trạng thái |
|---|---|
| xác định đường vào **hợp lệ** — khoá SSH của owner, **không** dùng `SC-04` | ✅ xong; cả hai tệp khoá **tồn tại** trên máy |
| thiết kế phép so **một chiều** — băm phía máy chủ, so phía local, **không gửi bí mật qua mạng** | ✅ xong |
| bộ lệnh **chỉ đọc** (`cat` · `grep` · `sha256sum` · `systemctl show` · `ls`) | ✅ xong, 17 lệnh |
| **thực thi** | 🔴 **BỊ CHẶN** — lớp phân quyền của công cụ chặn lệnh kết nối ra ngoài |

**Tôi dừng, không đi vòng.** Hệ quả trực tiếp, phải nói rõ vì nó đổi kết luận:

- **Không** trả lời được: khoá host đang chạy có **trùng** khoá đã bị commit không
- **Không** trả lời được: `SC-04` có nằm trong cấu hình **đang dùng** hay chỉ là artifact cũ
- **Không** trả lời được: `SC-03` có được tiến trình đang chạy tham chiếu không
- **Không** trả lời được: `SC-02` là **nguồn sống** hay **ảnh chụp**
- **Không** trả lời được: tư thế xác thực SSH **hiện tại** (`OD-05` vẫn là ảnh chụp 52 ngày tuổi)

⇒ **Mọi `Validity status` = `NOT_VERIFIED`**, và runbook mục 6 chỉ đạt **`ROTATION_PACKET_PARTIAL`**.

---

## 6 · RUNBOOK XOAY CREDENTIAL — **CHƯA THI HÀNH**

> **Kết quả mục này: `ROTATION_PACKET_PARTIAL`.** Không phải `READY`, vì `VPS_RUNTIME` bị chặn nên
> ba bước tiền đề chưa có bằng chứng. **Không** ghi `ROTATION_APPROVED`, **không** ghi
> `ROTATION_COMPLETED`.

⛔ **Luật đường lui, nói trước vì nó quan trọng nhất:** sau khi đã thu hồi thì **cấm** dùng
credential cũ làm đường lui. Đường lui **chỉ** được là **phiên quản trị đang mở** hoặc
**credential dự phòng đã kiểm trước**.

| # | bước | actor | mục tiêu | điều kiện vào | tác động · gián đoạn | bằng chứng PASS | điều kiện DỪNG | đường lui |
|---|---|---|---|---|---|---|---|---|
| **1** | giữ **một phiên quản trị đang mở** suốt quy trình | Owner | đường vào | — | không | phiên còn phản hồi | phiên rớt ⇒ **DỪNG** | chính nó |
| **2** | chụp cấu hình liên quan + tạo bản kê | Agent | `SC-01` `SC-02` `SC-04` | bước 1 xong | không | bản kê có băm từng tệp | không chụp được ⇒ DỪNG | không cần |
| **3** | xác nhận **ít nhất một đường vào dự phòng** | Owner | đường vào | bước 2 | không | đường dự phòng đăng nhập được **trong phiên khác** | không có đường dự phòng ⇒ 🔴 **DỪNG HẲN** | bước 1 |
| **4** | tạo credential **mới** (chưa thu hồi cũ) | Owner | `SC-01` `SC-04` `SC-05` `SC-08` `SC-03` | bước 3 | không — cũ vẫn chạy | credential mới dùng được | tạo lỗi ⇒ DỪNG, chưa mất gì | cũ vẫn còn |
| **5** | cập nhật **từng** consumer theo đồ thị phụ thuộc | Agent | 16 script + cấu hình dịch vụ | bước 4 | không | mỗi consumer đọc được giá trị mới | một consumer hỏng ⇒ DỪNG tại đó | cũ vẫn còn |
| **6** | smoke test **từng** consumer | Agent | như trên | bước 5 | không | mọi consumer PASS | bất kỳ FAIL ⇒ DỪNG | cũ vẫn còn |
| **7** | chuyển tham chiếu dịch vụ sang giá trị mới | Owner | dịch vụ ứng dụng | bước 6 | 🟠 **có** — vài giây | dịch vụ trả lời bình thường | dịch vụ không lên ⇒ lùi tham chiếu | lùi tham chiếu *(cũ chưa thu hồi)* |
| **8** | 🔴 **thu hồi credential cũ** | Owner | `SC-01` `SC-03` `SC-04` `SC-05` `SC-08` | bước 7 ổn định | không | cũ **không** dùng được nữa | — | 🔴 **từ đây KHÔNG lùi được bằng cũ** — chỉ còn bước 1 và 3 |
| **9** | soi log lỗi | Agent | dịch vụ | bước 8 | không | không có lỗi xác thực mới | có lỗi ⇒ xử trong phiên bước 1 | bước 1 / 3 |
| **10** | kiểm đường vào **mới** từ một phiên **hoàn toàn mới** | Owner | đường vào | bước 9 | không | phiên mới vào được | không vào được ⇒ giữ bước 1, xử ngay | bước 1 / 3 |
| **11** | đánh dấu credential cũ **không thể quay lại** | Agent | sổ | bước 10 | không | ghi sổ | — | — |
| **12** | **chỉ sau đây** mới bàn scrub / rewrite | Owner | `PACKET 2` `PACKET 3` | bước 11 | — | — | — | — |

### Ba tiền đề **chưa có bằng chứng** — lý do `PARTIAL`

1. 🔴 **Bước 3** — chưa xác nhận được có đường vào dự phòng nào, vì không đọc được `authorized_keys`.
2. 🔴 **Bước 5** — danh sách consumer đang **suy từ mã nguồn**, chưa đối chiếu với cấu hình đang chạy.
3. 🔴 **`SC-02`** — chưa phân biệt được **nguồn sống** hay **ảnh chụp**; nếu là ảnh chụp thì nó
   **không** cần xoay, chỉ cần gỡ khỏi Git.

---

## 7 · CHỨNG MINH HOOK HAI RUNTIME

> Làm **hoàn toàn trên bản sao cô lập**. Cấu hình thật: `git status .cursor/` = **0 dòng thay đổi**.

### 7.1 · Kiểm cấu hình thật — mọi đường dẫn **đều tồn tại**

| tệp cấu hình | parse | hook khai báo | script đích |
|---|---|---|---|
| cấu hình Cursor | ✅ JSON hợp lệ | **5** | **5/5 tồn tại** |
| cấu hình Claude Code | ✅ JSON hợp lệ | **1** | **1/1 tồn tại** |

Bốn hook Cursor thiếu điểm danh: cổng quản trị (288 dòng) · chống cắt cụt (57) · chất lượng mã
(119) · sổ deploy (169).

### 7.2 · 🟢 PHÁT HIỆN QUAN TRỌNG — cổng quản trị **HOẠT ĐỘNG ĐÚNG**

Chạy **chính script thật** (chỉ là logic quyết định, không ghi gì — đã xác nhận `git status`
không đổi):

| đầu vào | cổng quản trị | chống cắt cụt | chất lượng mã |
|---|---|---|---|
| lệnh vô hại | `allow` | `allow` | `allow` |
| **lệnh triển khai** | 🟢 **`ask`** — **BẮT ĐÚNG** | `allow` | `allow` |
| đầu vào **hỏng** | 🔴 `allow` | 🔴 `allow` | 🔴 `allow` |

🟢 **Điều này đổi cách đọc `FU-441`:** cổng quản trị **không hỏng, không lỗi thời** — nó **bắt
đúng** lệnh triển khai. Vấn đề **hoàn toàn** là nó **không bao giờ được gọi** trong phiên Claude
Code. Đây là lập luận mạnh nhất cho việc bịt khoảng hở, và trước đây chưa ai đo.

🔴 **Và một khuyết tật mới, chưa từng báo:** cả ba cổng **fail-OPEN** khi đầu vào hỏng — trả
`allow`. Một cổng không đọc nổi đầu vào thì **cho qua**. Ghi nhận, **không sửa** (D-24 cấm).

### 7.3 · Bản vá điểm danh — thử chặn **5/5 ĐẠT**

Bản vá **chỉ thêm điểm danh**, theo đúng khuôn mẫu đã có sẵn trong kho. Bốn tệp `py_compile` OK.

| phép thử | kết quả |
|---|---|
| sự kiện **đúng** ⇒ điểm danh tăng **đúng một** | 🟢 **ĐẠT** |
| hook **khác** ⇒ chỉ ghi mục của chính nó | 🟢 **ĐẠT** |
| đầu vào **hỏng** ⇒ **vẫn** điểm danh *(fail-safe: ghi trước khi có thể chặn)* | 🟢 **ĐẠT** |
| chạy **lặp 3 lần** ⇒ tăng **đúng 3**, không nhân đôi | 🟢 **ĐẠT** |
| **hai runtime** cùng ghi ⇒ **append-only, không ghi đè nhau** | 🟢 **ĐẠT** |

**Điểm danh có lọt gì nhạy cảm không:** prompt/lệnh 🟢 **SẠCH** · đường dẫn 🟢 **SẠCH** ·
bí mật 🟢 **SẠCH**. Mỗi dòng chỉ có: **giờ · tên hook · pha · runtime · PID**.

### 7.4 · Ma trận

| Control | cấu hình Cursor | cấu hình Claude | dùng chung? | Attendance proven | Duplicate risk | Handoff gap | Bước kế tiếp đề xuất |
|---|---|---|---|---|---|---|---|
| briefing đầu phiên | ✅ khai báo | ❌ | ❌ | 🟢 **`ACTIVE`** *(nổ 16/08)* | 🟢 không | mất khi dùng Claude Code | giữ nguyên |
| **cổng quản trị** | ✅ khai báo | ❌ | ❌ | 🔴 **`NOT_VERIFIED`** | 🟢 không | 🔴 **mất khi dùng Claude Code** — dù **đã chứng minh bắt đúng** | **thêm điểm danh** *(bản vá đã thử 5/5)* |
| chống cắt cụt | ✅ khai báo | ❌ | ❌ | 🔴 **`NOT_VERIFIED`** | 🟢 không | mất khi dùng Claude Code | **thêm điểm danh** |
| chất lượng mã | ✅ khai báo | ❌ | ❌ | 🔴 **`NOT_VERIFIED`** | 🟢 không | mất khi dùng Claude Code | **thêm điểm danh** |
| sổ deploy | ✅ khai báo | ❌ | ❌ | 🔴 **`NOT_VERIFIED`** | 🟢 không | mất khi dùng Claude Code | **thêm điểm danh** |
| cổng `git commit` | ❌ | ✅ khai báo | ❌ | 🟢 **`ACTIVE`** *(nổ trong phiên này)* | 🟢 không | 🔴 **mất khi dùng Cursor Agent** | cần bản Cursor tương đương |
| khoá phiên ghi | ✅ dùng chung tệp | ✅ dùng chung tệp | 🟢 **CÓ** | 🟢 **`ACTIVE`** | 🟢 không | 🟢 **không hở** | giữ nguyên |

⛔ **`DUPLICATE = 0`** — hai tập hợp **rời nhau hoàn toàn**. **Chưa đề xuất migrate hay retire**
cho bất kỳ hook nào, vì attendance **chưa chứng minh** — đúng luật `RM-15`.

### 7.5 · Thiết kế lớp bọc dùng chung — **chỉ là thiết kế**

Nguyên tắc: **một** thân xử lý, **hai** bộ chuyển đổi đầu vào/đầu ra — vì hai runtime khác
**kiểu matcher** (Claude khớp theo **tên tool**, Cursor khớp theo **regex lệnh**) và khác **định
dạng trả lời**. Điểm danh ghi ở **thân**, nên hai phía không đếm lệch.

⛔ **Không cài vào runtime thật.** Bản fixture cô lập đã có và thử 5/5.

---

## 8 · CÒN LẠI: `NOT_CHECKED` VÀ `BLOCKED_TOOLING`

| mã | phạm vi | vì sao |
|---|---|---|
| 🔴 `BLOCKED_PERMISSION` | **toàn bộ `VPS_RUNTIME`** | lớp phân quyền chặn lệnh kết nối ra ngoài |
| 🔴 `BLOCKED_TOOLING` | dò entropy | 4 công cụ chuẩn **đều không có**; bộ quét tự viết chỉ bắt **mẫu đã biết** |
| 🟡 `NOT_CHECKED` | 27 tệp ảnh · 56 + 128 + 39 blob/tệp nhị phân | không quét được nội dung |
| 🟡 `NOT_VERIFIED` | `SC-06` `SC-09` `SC-10` | chưa đủ dấu hiệu phân loại |
| 🟡 `NOT_VERIFIED` | kho công khai có public liên tục từ 06/05 không | nhà cung cấp Git không lưu lịch sử visibility |
| 🟡 `NOT_AVAILABLE` | có ai đã đọc kho hay chưa | API lưu lượng `401` |

⛔ **Không mục nào ở trên được ghi `COMPLETE`.**

---

## 9 · BA LỚP NGUỒN (§62)

### `OWNER_SAID`

> *« `D-24 = KEEP_PUBLIC_CURRENT`: GitHub Report tiếp tục public; không đổi visibility lúc này. »*
>
> *« `D-24` KHÔNG có nghĩa: kho đã an toàn; exposure đã đóng; được xoay credential; được scrub
> HEAD; được rewrite history; được sửa/cài/migrate/retire hook; được deploy `FU-438`; được sửa
> production. »*
>
> *« Owner dùng cả Cursor Agent và Claude Code. Owner luân phiên hai Agent theo lưu lượng. »*
>
> *« Không được để số "4 hoặc 5" treo mà không giải thích. »*
>
> *« Không được ghi `ROTATION_APPROVED` hoặc `ROTATION_COMPLETED`. »*
>
> *« Mỗi việc thật sự cần Owner quyết phải có đúng một câu hỏi, nhưng **không hỏi Owner nếu Agent
> còn tự điều tra được**. »*

### `CODE_DID`

| việc | bằng chứng |
|---|---|
| `TOTAL = 31` | tính **từ bảng dữ liệu**, có `assert` trong script; artifact máy đọc được ở local |
| «24» bị bác | ba phép đếm hợp lệ cho `23 / 28 / 18` |
| 7 giá trị mật khẩu | hợp của 3 mẫu, dedupe theo băm giá trị |
| phép pickaxe **hỏng** | thử chặn: đối chứng *«chắc chắn CÓ»* = **585 commit**; mẫu đã dùng = `0` |
| `PRIVATE_HISTORY` đã quét | **10.615/10.743 blob = 98 %** |
| cổng quản trị **bắt đúng** lệnh triển khai | chạy script thật → `ask` |
| ba cổng **fail-OPEN** | đầu vào hỏng → `allow` |
| bản vá điểm danh | **5/5 ĐẠT** trên fixture; `py_compile` OK cả 4 |
| **không chạm hook thật** | `git status .cursor/` = **0 dòng** |
| `VPS_RUNTIME` bị chặn | lớp phân quyền từ chối, **không đi vòng** |

### `DOC_SAID`

| nguồn | ghi gì |
|---|---|
| `CLAUDE.md §61` | `RM-11` số phải tái lập · `RM-12` cấm nâng tầng · `RM-13` nguồn phải là production thật · **`RM-15` cổng không thử coi như không tồn tại** · `RM-21` hằng số chỉ đúng cho thước đã đo nó |
| `PRJ-RETRACTION-001` | rút lại đủ bốn phần, **tại chỗ đã công bố** |
| `REPORT_V11124` | bốn chỗ được rút lại ở mục 2 |

### 🔴 BA LỚP LỆCH NHAU

| lệch | chi tiết |
|---|---|
| `DOC_SAID` ≠ `CODE_DID` | `V11124` ghi *«4 giá trị mật khẩu»* — đo lại ra **7** |
| `DOC_SAID` ≠ `CODE_DID` | `V11124` ghi *«24 `CURRENT_HEAD_EXPOSURE`»* — **không phép đếm nào ra 24** |
| `DOC_SAID` ≠ `CODE_DID` | `V11124` ngụ ý cổng Cursor chỉ là *«mất hiệu lực»* — đo được nó **bắt đúng** lệnh triển khai, tức **giá trị bị mất lớn hơn** báo cáo trước mô tả |
| `OWNER_SAID` ≠ `CODE_DID` | Owner cấp `VPS_CONFIG_READ_ONLY`; **môi trường chặn** ⇒ không thi hành được |

---

## 10 · NO-MUTATION PROOF

| khẳng định | |
|---|---|
| production không đổi | ✅ |
| private code không push | ✅ |
| DB không ghi | ✅ |
| credential không xoay | ✅ |
| Git history không rewrite | ✅ |
| visibility không đổi | ✅ |
| **hook runtime không đổi** | ✅ — `git status .cursor/` = 0 dòng |
| `FU-438` không deploy | ✅ |
| báo cáo cũ không sửa/xoá | ✅ |
| kho riêng | HEAD `a4d66364…` **y nguyên** · ahead = **0** |
| tệp tracked bị đổi | **2** — đúng hai tệp `M` **có sẵn từ trước phiên** |

> Mọi thao tác ghi đều nằm trong **thư mục tạm cô lập**, ngoài cả hai kho.

---

## 11 · MỨC SẴN SÀNG QUYẾT ĐỊNH

| hạng mục | mức |
|---|---|
| Đối chiếu `V11124` | 🟢 **`READY_FOR_OWNER_DECISION`** — không còn số treo |
| Bản vá điểm danh hook | 🟢 **`READY_FOR_OWNER_DECISION`** — thử 5/5, fixture sẵn |
| **Runbook xoay credential** | 🔴 **`NOT_READY_FOR_OWNER_DECISION`** — `ROTATION_PACKET_PARTIAL`, ba tiền đề thiếu |
| `SC-06` `SC-09` `SC-10` | 🟠 **`AGENT_SELF_WORK_REMAINS`** — tôi còn tự điều tra được, **chưa hỏi Owner** |
| `PACKET 1` `2` `3` của `V11124` | 🟠 **`AGENT_SELF_WORK_REMAINS`** — phụ thuộc runtime, chờ mở đường đọc |

### Câu hỏi Owner — **đúng một**, và chỉ vì tôi **không tự làm được**

> ### Anh có mở quyền cho công cụ chạy lệnh kết nối đọc máy chủ *(thêm quy tắc Bash trong `settings.json`)* để tôi hoàn tất phần `VPS_CONFIG_READ_ONLY` mà anh đã cấp ở `D-24` không?
>
> Không có nó thì **mọi** trạng thái hiệu lực credential đứng ở `NOT_VERIFIED`, và runbook xoay
> **không thể** lên `READY` — vì bước 3 *(đường vào dự phòng)* là điều kiện an toàn bắt buộc, mà
> nó chỉ kiểm được trên máy chủ.

**Không hỏi gì thêm.** `SC-06`/`SC-09`/`SC-10` và ba packet còn lại là **việc của tôi**, chưa
đến lượt Owner.

---

TanPhatAI cần làm: cập nhật `docs/FOLLOW_UP_TRACKER.md` theo **bốn đính chính** ở mục 2 — con số finding đúng là **`TOTAL = 31`** với `PUBLIC_HEAD = 23` *(không phải 24)*, số giá trị mật khẩu là **7** *(không phải 4)*, câu *«0 credential»* **đã bị rút lại** và phải thay bằng câu đầy đủ ở mục 2.4, và phép đếm bằng công cụ tìm kiếm từ nay **bắt buộc kèm hai đối chứng** (`RM-15`). Ghi vào `docs/SO_TUONG_TAC_OWNER.md` rằng `D-24` là **quyền CHUẨN BỊ BẰNG CHỨNG, không phải quyền xử lý** — và rằng `VPS_CONFIG_READ_ONLY` Owner đã cấp **chưa thi hành được** vì môi trường chặn (`BLOCKED_PERMISSION`), đây là **khoảng trống bằng chứng chính** của phiên. **Phiên này không sửa một dòng code production nào, không chạm hook thật** — mọi thao tác ghi nằm trong thư mục tạm cô lập. Trạng thái runbook là **`ROTATION_PACKET_PARTIAL`**, **không** phải `APPROVED` và **không** phải `COMPLETED`. Năm packet của `V11124` vẫn **`OWNER_DECISION_PENDING`**.
