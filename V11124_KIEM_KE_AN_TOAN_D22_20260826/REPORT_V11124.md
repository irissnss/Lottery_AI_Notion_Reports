# REPORT V11124 — KIỂM KÊ AN TOÀN D-22 (INVENTORY_ONLY) · PHÁT HÀNH THEO D-23

```
REPORT_VERSION              : V11124
REPORT_TITLE                : Kiểm kê an toàn D-22 — bề mặt hạ tầng trên kho báo cáo công khai
WORK_DATE_ICT               : 2026-08-26
INVENTORY_COMPLETED_AT_ICT  : 2026-08-26 08:33:50
PUBLISHED_AT_ICT            : 2026-08-26 10:05 (giờ chính xác = giờ COMMIT_SHA)
TIMEZONE                    : Asia/Ho_Chi_Minh / UTC+07:00
OWNER_DECISION              : D-22 INVENTORY_ONLY + D-23 REPORT_ONLY_PUSH
AUTHORIZED_SCOPE            : REPORT_ONLY_PUBLIC_SAFE
PREVIOUS_PUBLIC_HEAD        : 28c6891b74096faee8cc332b11204585375bf092
CURRENT_PUBLIC_HEAD_AFTER_PUSH : ebfdf188eac1c709e58cc950499ec7b4d2ab3329
                              ↑ commit PHÁT HÀNH báo cáo này (26/08 10:11:40 +0700).
                                Trường này được điền bằng một commit metadata ngay sau đó —
                                một báo cáo không thể chứa SHA của chính commit chứa nó.
INVENTORY_SOURCE_HEAD       : a4d66364a6ef3127152eae1b1ae6957250f3c8e6  (kho riêng — KHÔNG push)
ACTOR_RUNTIME               : CURSOR_AGENT_AND_CLAUDE_CODE
LABELS                      : SECURITY_INVENTORY · INVENTORY_ONLY · REPORT_ONLY_PUSH ·
                              PUBLIC_SAFE · DUAL_AGENT_RUNTIME · OWNER_DECISION_PENDING
```

> ⛔ **Báo cáo này KHÔNG phải bản xử lý sự cố.** Không có việc gì được khắc phục. Không nói
> "đã xử lý", "đã làm sạch", "đã bảo mật", "đã hết rủi ro" — **không việc nào đã xảy ra**.

---

## 1 · TÓM TẮT

Kho báo cáo công khai đang phơi **địa chỉ một máy chủ** và **tên một tài khoản quản trị** ra
Internet, đọc được **không cần tài khoản**, liên tục **112 ngày** kể từ 06/05/2026 — và
**chưa từng được che một lần nào** (`+64 dòng / −0 dòng` qua 23 commit).

Trên **kho công khai**, kiểm kê tìm thấy **0 vật liệu xác thực**: không khoá riêng, không khoá
API, không mật khẩu, không chuỗi kết nối — trên **cả HEAD lẫn toàn bộ lịch sử**.

Trên **kho riêng** (đã xác minh **không** truy cập công khai được), kiểm kê tìm thấy vật liệu
xác thực **thật** thuộc bốn nhóm. Phép đối chiếu trên **toàn bộ 3.262 blob** của kho công khai
cho kết quả **0/3 mẫu đại diện lọt sang công khai** — **ranh giới riêng/công khai giữ được**.

Chưa xác định được **có ai đã đọc hay chưa**: GitHub trả `401` cho API lưu lượng ⇒
`ACCESS_EVIDENCE_NOT_AVAILABLE`. Đây **không** đồng nghĩa "không ai đọc".

**FINAL_STATUS của kiểm kê: `PARTIAL`** — sáu lý do liệt kê ở mục 9.

---

## 2 · OWNER YÊU CẦU GÌ

### D-22 (26/08/2026, sáng) — nguyên văn trích

> *« `OWNER_DECISION: D-22 = INVENTORY_ONLY` — Chỉ kiểm kê trước. »*
>
> *« Nếu phát hiện secret thật: không in secret; không copy secret vào report; chỉ ghi loại
> secret, fingerprint đã redact, vị trí và mức độ; đánh dấu `CRITICAL_SECRET_FOUND`; dừng trước
> mọi hành động thay đổi. »*
>
> *« Owner đang sử dụng Claude Code bên trong Cursor. Vì vậy premise "hook Cursor chết" phải được
> kiểm tra lại, không được tự chuyển hoặc retire hook. »*
>
> *« Phiên này chỉ `INVENTORY_ONLY`. Không được nói: "đã xử lý sự cố" "đã làm sạch" "đã bảo mật"
> "đã hết rủi ro". »*

### D-23 (26/08/2026 09:13 ICT) — nguyên văn trích

> *« `GITHUB_REPORT_PUSH = YES` · `GITHUB_PRIVATE_CODE_PUSH = NO` ·
> `AUTHORIZED_OUTPUT = REPORT_ONLY_PUBLIC_SAFE` »*
>
> *« Owner dùng cả Cursor Agent và Claude Code, luân phiên theo lưu lượng. »*
>
> *« Đây chỉ là bước bàn giao bằng chứng cho TanPhatAI đọc và phân tích. Không mở rộng thành
> phiên sửa code, deploy hoặc xử lý sự cố. »*
>
> *« Không mặc định V11124 nếu chưa kiểm tra số hiệu. »*
>
> *« Không được biến quyền report-only thành quyền xử lý finding. »*

---

## 3 · ĐÀO BỚI / PHÁT HIỆN

### A · PHẠM VI ĐÃ QUÉT

| mặt | phạm vi | kết quả |
|---|---|---|
| **HEAD kho công khai** | `28c6891b…`, nhánh `main` | **2.599** tệp Git quản lý · **1.637** tệp `.md` |
| quét được bằng văn bản | 2.521 tệp văn bản + 51 tệp UTF-16 giải mã lại | **2.572 / 2.599 = 98,9 %** |
| **`NOT_CHECKED` tại HEAD** | **27** tệp `.png` | không quét được nội dung |
| **Lịch sử Git kho công khai** | **605** commit trên `main` · 626 commit trong object DB | `.git` 19 MB |
| blob lịch sử quét được | **3.206 / 3.262 = 98,3 %** | dùng `git cat-file --batch-all-objects` ⇒ **bao gồm cả blob không còn reachable** |
| **`NOT_CHECKED` trong lịch sử** | **56** blob nhị phân | bỏ qua |
| **Kho riêng** | HEAD `a4d66364…` · **3.639** tệp tracked | quét 3.600 tệp văn bản; **39** tệp nhị phân bỏ qua |
| **`NOT_CHECKED` kho riêng** | **toàn bộ lịch sử** — chỉ quét HEAD | phải đóng ở lượt sau |
| Cấu hình hook | tệp cấu hình của Claude Code và của Cursor | xem mục 6 |
| Truy cập công khai | API kho + đọc ẩn danh qua đường `raw` | xem mục **G** |
| **Bằng chứng truy cập** | API lưu lượng / clone | **`NOT_AVAILABLE`** — `401` |

**Công cụ và rule dùng để quét:**

| | |
|---|---|
| `gitleaks` · `trufflehog` · `detect-secrets` · `git-secrets` · `gh` | ❌ **KHÔNG CÓ** trên máy ⇒ **`BLOCKED_TOOLING`** |
| thay bằng | bộ quét Python/regex **tự viết**, chạy trên `git cat-file --batch` |
| rule | 20 mẫu: khối `BEGIN…PRIVATE KEY` · AWS · OpenAI · Anthropic · GitHub · GitLab · Slack · Google · chuỗi kết nối CSDL có mật khẩu · JWT · gán mật khẩu literal · công cụ nhập mật khẩu SSH tự động · chỉ thị cấu hình SSH · tệp máy chủ đã biết · đường dẫn khoá riêng · IPv4 · IPv6 · đường dẫn máy chủ · chuỗi đăng nhập |
| **giới hạn của rule** | bắt **mẫu đã biết**; **KHÔNG có dò entropy** ⇒ token nội bộ dạng lạ vẫn có thể lọt |

### B · SỐ ĐẾM — **raw match KHÔNG phải actual exposure**

| chỉ số | kho công khai |
|---|---|
| **tổng raw match** tại HEAD | **1.487** |
| **tổng raw match** trên toàn object DB | **1.616** |
| **`FALSE_POSITIVE`** đã loại tại HEAD | **1.040 / 1.487 = 69,9 %** |
| ├─ chuỗi phiên bản trông giống IPv4 | 983 |
| ├─ `token` / `api_key` là **thuật ngữ nghiệp vụ** | 47 |
| └─ địa chỉ máy chủ của **chính nhà cung cấp Git** | 10 |
| **finding sau deduplicate** | **31** *(bảng mục C)* |
| tệp unique dính ít nhất một finding thật | **≈ 300** *(các nhóm chồng lấn — không cộng dồn)* |
| **vật liệu xác thực xác nhận — kho công khai** | 🟢 **0** |

> ⚠️ **69,9 % raw match là nhiễu.** Ai đọc con số `1.487` rồi kết luận *"1.487 lỗ hổng"* là sai
> hoàn toàn. Con số dùng được là **31 finding sau dedupe**, và phần lớn trong đó là
> `INTERNAL_PATH` / `OPERATIONAL_DETAIL` chứ **không** phải bí mật.

### C · PHÂN LOẠI TỪNG FINDING

> **Ghi chú redaction — hai chỗ tôi CỐ Ý thu hẹp so với mức D-23 §5 cho phép, và nêu rõ thay vì
> làm im lặng:**
> 1. **Không** in dấu vân tay băm của giá trị bí mật — băm rút gọn vẫn là **oracle thử mật khẩu
>    ngoại tuyến** khi công bố nơi công cộng.
> 2. **Không** liệt kê đích danh tệp nào chứa chuỗi đăng nhập — trong **chính kho đang công
>    khai** thì danh sách đó là **bản đồ chỉ đường**.
>
> Danh sách đầy đủ **có ở local**, bàn giao cho TanPhatAI ngoài kho công khai.

#### `CRITICAL_SECRET` — 4 finding · **CHỈ trong kho RIÊNG · KHÔNG công khai**

| mã | loại | phạm vi | lộ từ |
|---|---|---|---|
| `SC-01` | khoá **RIÊNG** SSH, không có passphrase bảo vệ | 8 tệp | 2026-07-05 |
| `SC-02` | tệp bóng mật khẩu hệ thống — **1 hash thật** (thuật toán crypt hiện đại) + 33 tài khoản đã khoá | 1 tệp | 2026-07-05 |
| `SC-03` | `SECRET-CANDIDATE-01` — khoá API nhà cung cấp mô hình, gán cứng trong mã | 1 tệp | 2026-07-05 |
| `SC-04` | `SECRET-CANDIDATE-02..05` — **4 giá trị mật khẩu phân biệt**, dạng văn bản thường | 48 tệp | 2026-03-23 |

**Thời gian phơi trong kho riêng:** `SC-04` **156 ngày** · `SC-01` / `SC-02` / `SC-03` **52 ngày**.
🟢 **0 / 3** mẫu đại diện lọt sang kho công khai — bằng chứng ở mục **F**.

#### `AUTH_MATERIAL` — 3 finding *(kho công khai — **không** phải bí mật)*

| mã | loại | phạm vi | ghi chú |
|---|---|---|---|
| `AM-01` | khoá **CÔNG KHAI** SSH dán nguyên văn kèm chú thích | 1 tệp | khoá công khai **không** phải bí mật; nhưng xác nhận quan hệ sở hữu khoá |
| `AM-02` | **đường dẫn** tới tệp khoá riêng SSH trên máy local | 5 tệp | **là tên đường dẫn, KHÔNG phải nội dung khoá** — đã xác minh 0 khối `BEGIN…PRIVATE KEY` trong kho công khai |
| `AM-03` | chuỗi bí mật phiên **MẶC ĐỊNH** trích nguyên văn vào một báo cáo | 1 tệp | **đã hết hiệu lực**, và chính kho đã ghi nhận việc xử lý |

#### `INFRASTRUCTURE_EXPOSURE` — 6 finding *(kho công khai)*

| mã | loại | phạm vi | mức |
|---|---|---|---|
| `IE-01` | `HOST-01` — địa chỉ IPv4 máy chủ sản xuất | **95 lần / 52 tệp / 36 thư mục báo cáo** · 06/05 → 23/08 | 🔴 **CAO** |
| `IE-02` | `ACCOUNT-01@HOST-01` — chuỗi đăng nhập đặc quyền đầy đủ | **51 lần / 27 tệp** | 🔴 **CAO** |
| `IE-03` | `HOST-02` — cùng đích, viết dạng bí danh chữ | 2 tệp | 🔴 **CAO** |
| `IE-04` | nội dung **log máy chủ web nguyên bản** — dòng access log + error log | 20 + 4 dòng · **9 địa chỉ khách duy nhất** · 2 tệp / 1 thư mục | 🟠 **TB** |
| `IE-05` | trích nhật ký dịch vụ có kèm 1 địa chỉ khách | 4 tệp | 🟡 **THẤP** |
| `IE-06` | khối cấu hình máy chủ web dán nguyên văn (59 dòng): tên miền, cổng, **đường dẫn** chứng chỉ | 1 tệp | 🟠 **TB** |

> 🔴 **`IE-04` đáng chú ý riêng:** đó **không phải dữ liệu của dự án** mà là **địa chỉ của bên
> thứ ba** kèm dấu thời gian và chuỗi nhận dạng trình duyệt, đang công khai. Đây là nhóm duy nhất
> có yếu tố **dữ liệu của người khác**.
>
> `IE-06` là **đường dẫn** tới chứng chỉ, **không** phải nội dung khoá chứng chỉ.

#### `INTERNAL_PATH` — 4 finding *(kho công khai)*

| mã | loại | phạm vi |
|---|---|---|
| `IP-01` | `PATH-01` — gốc cây triển khai trên máy chủ | **1.182 lần / 203 tệp** |
| `IP-02` | `PATH-02` — đường dẫn tệp CSDL sản xuất | 40 tệp |
| `IP-03` | `PATH-03` — thư mục sao lưu trên máy chủ | 139 tệp |
| `IP-04` | `PATH-04` — đường dẫn tệp nhật ký và tệp vết | 30 + 3 tệp |

Tổng đường dẫn máy chủ: **34 giá trị phân biệt · 1.338 lần · 255 tệp**.

#### `OPERATIONAL_DETAIL` — 5 finding *(kho công khai)*

| mã | loại | phạm vi |
|---|---|---|
| `OD-01` | tên đơn vị dịch vụ hệ thống + lệnh điều khiển dịch vụ | 60 / 97 tệp |
| `OD-02` | chuỗi lệnh vận hành từ xa ghép hoàn chỉnh | 110 tệp / 291 lần |
| `OD-03` | script triển khai **tắt kiểm tra khoá máy chủ** khi kết nối | 5 tệp |
| `OD-04` | `ENDPOINT-01` — các đường endpoint quản trị nội bộ | 584 khớp |
| `OD-05` | **tư thế xác thực SSH của máy chủ**, đọc từ bản trích cấu hình nằm trong kho riêng | — |

> 🔴 **`OD-05` — giá trị cụ thể CỐ Ý KHÔNG công bố ở đây.** Verdict: **`RISK_CONFIRMED`**.
> Công bố chi tiết tư thế xác thực, trong **chính kho đang công khai địa chỉ máy chủ**, là cung
> cấp **điều kiện tiền đề** cho tấn công. Chi tiết có ở local, bàn giao ngoài kho công khai.
>
> ⚠️ **Giới hạn bắt buộc đọc kèm:** bản trích cấu hình có tuổi **52 ngày**.
> **`RUNTIME_UNVERIFIED`** — cấu hình đang chạy hôm nay **có thể đã khác**. Không được đọc
> `OD-05` thành kết luận về hiện trạng máy chủ.

#### `MENTION_ONLY` — 1 finding

| mã | loại | phạm vi |
|---|---|---|
| `MO-01` | 5 báo cáo mới nhất (V11119–V11123) chỉ **thuật lại** bằng **chữ thay thế đã che**, 0 giá trị thật | 2 tệp |

#### `FALSE_POSITIVE` — 5 finding · **1.040 khớp thô đã loại**

| mã | loại | vì sao loại |
|---|---|---|
| `FP-01` | chuỗi phiên bản bốn nhóm số trông giống IPv4 | 983 khớp — là số phiên bản |
| `FP-02` | địa chỉ vòng lặp nội bộ · địa chỉ bind mọi giao diện · hằng số metadata đám mây | không lộ hạ tầng |
| `FP-03` | số phiên bản phần mềm trong tệp cấu hình thư mục Windows | 4 tệp |
| `FP-04` | mẫu IPv6 khớp nhầm vào **dấu thời gian** trong dòng log | toàn kho **không có** IPv6 thật |
| `FP-05` | `token` / `api_key` là **thuật ngữ nghiệp vụ**, không có literal | 47 khớp |

> **Bằng chứng loại `FP-05` là ĐỘ DÀI, không phải phán đoán:** chuỗi khớp dài nhất chỉ **10–12
> ký tự**, trong khi khoá thật của các nhà cung cấp cần **36–40+ ký tự**. Ngắn hơn **ba lần**.
> Đây là phép loại khách quan, tái lập được.

### D · VỊ TRÍ TỒN TẠI

| phân loại | số finding | chi tiết |
|---|---|---|
| **`CURRENT_HEAD_EXPOSURE`** | **24** | toàn bộ `IE-*` · `IP-*` · `OD-*` · `AM-*` · `SC-*` |
| **`BOTH_HEAD_AND_HISTORY`** | **19** | mọi dấu vết hạ tầng: có ở HEAD **và** trong lịch sử — vì `−0 dòng`, chưa từng gỡ |
| **`HISTORY_ONLY_EXPOSURE`** | **2** | `HO-01` một địa chỉ thư điện tử còn trong 4 blob, đến từ 40 tệp lệnh tạm đã gỡ ngày 2026-07-30 bởi commit `c84a4e9` · `HO-02` 4 đường dẫn Windows dài |
| **`NOT_VERIFIED`** | **2** | 27 tệp `.png` tại HEAD + 56 blob nhị phân trong lịch sử · **toàn bộ lịch sử kho riêng** |

🔴 **Con số quan trọng nhất của mục này:**

```
ACCOUNT-01@HOST-01     +64 dòng  /  −0 dòng     (23 commit)
HOST-01                +95 dòng  /  −0 dòng     (38 commit)
đường dẫn máy chủ   +1.267 dòng  /  −5 dòng     (121 commit)
```

**`−0`** nghĩa là **chưa một lần nào có ai gỡ dấu vết này ra**. Không phải *"đã che rồi lộ lại"* —
mà là **chưa từng che**. 5 dòng đường dẫn từng bị xoá thuộc 4 commit, và đọc lại thì **cả 4 đều
là sửa câu văn**, không phải hành động che giấu.

**Hệ quả cho quyết định:** ở nhóm hạ tầng **không có giá trị nào nằm-riêng-trong-lịch-sử** ⇒
danh sách cần che/xoay là **biết hết từ HEAD**, không có ẩn số.

### E · TRẠNG THÁI BẰNG CHỨNG

| việc | trạng thái |
|---|---|
| Kiểm kê này | **`REPORT_PROVEN`** |
| Kho công khai đọc được ẩn danh | **`REPORT_PROVEN`** — xác minh bằng phép gọi thật |
| 0 vật liệu xác thực trong kho công khai | **`REPORT_PROVEN`** |
| Ranh giới riêng/công khai giữ được | **`REPORT_PROVEN`** |
| Tư thế xác thực SSH (`OD-05`) | **`RUNTIME_UNVERIFIED`** — ảnh chụp 52 ngày tuổi |
| Có ai đã đọc kho hay chưa | **`NOT_CHECKED`** — `401` |
| Bản vá bề mặt công khai `FU-438` | **`CODE_IMPLEMENTED`** + **`NOT_DEPLOYED`** |
| Che HEAD · rewrite lịch sử · xoay credential · hook | **`OWNER_DECISION_PENDING`** — cả bốn |

⛔ **Không tầng nào được tự nâng cấp** (`RM-12`):
`REPORT_PROVEN` ≠ `CODE_IMPLEMENTED` ≠ `DEPLOYED` ≠ `RUNTIME_PROVEN`.

### F · SECRET SCAN

| | |
|---|---|
| **scanner** | bộ quét Python/regex **tự viết** — bốn công cụ chuẩn **đều không có** ⇒ **`BLOCKED_TOOLING`** |
| **phạm vi** | kho công khai: HEAD **và toàn bộ object DB** (3.262 blob, gồm cả blob không còn reachable) · kho riêng: **chỉ HEAD** |
| **số finding — kho công khai** | 🟢 **0** vật liệu xác thực |
| **số finding — kho riêng** | 🔴 **4 nhóm** (`SC-01` … `SC-04`) |

**Kết quả âm trên kho công khai — cả HEAD lẫn toàn bộ lịch sử:**

```
khối BEGIN…PRIVATE KEY   0      khoá AWS       0      khoá OpenAI / Anthropic   0
khoá GitHub / GitLab     0      khoá Slack     0      khoá Google               0
chuỗi kết nối CSDL       0      JWT            0      gán mật khẩu literal      0
công cụ nhập mk tự động  0      tệp máy chủ    0
```

**Đối chiếu chéo — phép đo quan trọng nhất của cả báo cáo:**

3 mẫu đại diện lấy từ kho riêng, đối chiếu trên **toàn bộ 3.262 blob** kho công khai
→ 🟢 **0 / 3 lọt**.

Bổ sung: **0 tệp** nào chứa **cả** chuỗi đăng nhập **lẫn** một giá trị mật khẩu ⇒ công thức đăng
nhập **không nằm trọn trong một tệp nào**.

**Verdict:**

| | |
|---|---|
| kho **công khai** | **`CREDENTIAL_COMPROMISE_NOT_PROVEN`** |
| kho **riêng** | **`CRITICAL_SECRET_FOUND`** — đã dừng trước mọi hành động thay đổi |
| lịch sử kho **riêng** | **`NOT_CHECKED`** |

⛔ **Không giá trị nghi là bí mật nào được in lại.** Khoá API **không** được thử hiệu lực —
cấm gọi mạng bằng khoá.

⚠️ **Một số chưa hoà giải xong:** phép đo sơ bộ nêu một ứng viên mật khẩu **thứ năm** không có
trong bảng 4 giá trị đã xác nhận. Chưa đóng được ⇒ **ghi thẳng là thiếu**, không điền số ước
(`RM-11` · `RM-17`).

### G · BẰNG CHỨNG TRUY CẬP CÔNG KHAI

| phép kiểm | kết quả |
|---|---|
| API kho — trường hiển thị | `private: False` · `visibility: public` · nhánh mặc định `main` |
| tạo lúc | **2026-05-06** · push gần nhất **2026-08-25T17:57:18Z** · kích thước 12.372 KB |
| **đọc ẩn danh, không tài khoản**, một tệp báo cáo qua đường `raw` | 🔴 **`HTTP 200` · 26.700 byte** |
| 6 phép dò ẩn danh độc lập | giới hạn nhịp = 60 ⇒ **xác nhận lane ẩn danh**, không phải phiên đã đăng nhập |
| forks | 🟢 **0** |
| stars · watchers · issues | 🟢 **0 · 0 · 0** |
| **kho RIÊNG**, gọi API **ẩn danh** | 🟢 **`HTTP 404`** ⇒ **PRIVATE, đã xác minh** |
| API lưu lượng / clone | ❌ **`401`** ⇒ **`ACCESS_EVIDENCE_NOT_AVAILABLE`** |

**Verdict: `PUBLICLY_ACCESSIBLE` — đã chứng minh.**
Toàn bộ **2.599 tệp** và **605 commit** đọc được không cần đăng nhập.

> 🟢 **`forks = 0` là con số có giá trị nhất ở đây:** chưa ai nhân bản kho. Nếu về sau chọn
> rewrite lịch sử thì **không có bản sao nào ngoài tầm** làm hỏng việc.
>
> ⚠️ **`NOT_VERIFIED`:** nhà cung cấp Git **không lưu lịch sử visibility** ⇒ **không chứng minh
> được** kho có public liên tục từ 06/05 hay không. Chỉ biết: tạo 06/05, **hiện đang** public.

### H · NO-MUTATION PROOF

| | preflight `08:05:20` | sau kiểm kê `08:33:50` |
|---|---|---|
| HEAD kho riêng | `a4d66364…` | `a4d66364…` **y nguyên** |
| HEAD kho công khai | `28c6891b…` | `28c6891b…` **y nguyên** |
| lệch remote, cả hai kho | `0 / 0` | `0 / 0` |
| cây bẩn kho riêng | 2 tệp `M` + 189 tệp `??` | **y nguyên** |
| cây kho công khai | sạch | sạch |
| reflog mới nhất kho công khai | `26/08 00:57:14` | **không đổi** — trước phiên |

| khẳng định | |
|---|---|
| production không đổi | ✅ |
| private code không push | ✅ |
| DB không ghi | ✅ |
| Git history không rewrite | ✅ |
| report cũ không sửa / xoá | ✅ |
| credential không xoay | ✅ |
| `FU-438` không deploy | ✅ |

> **Một hiệu ứng phụ khai báo thẳng, không giấu:** tệp điểm danh hook tăng 93 → 95 dòng. Nguyên
> nhân: một lệnh của tiến trình con **chứa chuỗi `git commit`** nên hook trước-khi-gọi-tool nổ
> **đúng thiết kế** và ghi điểm danh. **Không có commit nào chạy.** Tệp nằm trong `.gitignore`
> nên `git status` không đổi.

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Không xử lý gì** — đúng `D-22 INVENTORY_ONLY` và `D-23 REPORT_ONLY_PUBLIC_SAFE`.

Nguyên tắc dùng để **xếp thứ tự** khuyến nghị ở mục 7, nói bằng lời thường:

> **Thứ lộ ra là ĐỊA CHỈ, không phải CHÌA KHOÁ.** Mọi thao tác trên Git chỉ **gỡ tờ giấy ghi địa
> chỉ xuống**. Nếu bản thân cánh cửa vẫn nhận mật khẩu thì gỡ giấy là **mỹ phẩm**.
>
> Và: **xoay credential không thay thế được bằng bất kỳ thao tác Git nào.** Ai **đã** đọc rồi thì
> xoá tệp không thu hồi lại được.

---

## 5 · ĐÃ LÀM GÌ

| GĐ | việc | kết quả |
|---|---|---|
| `GĐ-0` | preflight hai kho | HEAD ghi nhận · lease kiểm |
| `GĐ-1` | kiểm kê HEAD kho công khai, 12 nhóm mẫu | 24 `CURRENT_HEAD_EXPOSURE` |
| `GĐ-2` | kiểm kê lịch sử Git, 605 commit | **0 rò chỉ-trong-lịch-sử** ở nhóm hạ tầng · `+64/−0` |
| `GĐ-4` | secret scan 3.262 blob + kho riêng | kho công khai **0** · kho riêng **`CRITICAL_SECRET_FOUND`** |
| `GĐ-5` | xác minh truy cập công khai | **`HTTP 200`** ẩn danh · kho riêng **`404`** |
| `GĐ-6` | kiểm lại `FU-441` trong môi trường thật | mục 6 |
| `GĐ-7` | đối chiếu bốn con số từng gây lẫn | mục 8 |
| `D-23` | phát hành báo cáo này | mục 10 |

---

## 6 · CỔNG KIỂM · `FU-441` — MA TRẬN HAI RUNTIME

**Premise mới của Owner:** *dùng cả Cursor Agent và Claude Code, chuyển qua lại theo lưu lượng.*

Đã đo trong môi trường thật: biến môi trường điểm vào xác nhận Claude Code đang chạy **như một
extension bên trong Cursor**; hai runtime đọc **hai tệp cấu hình khác nhau**, và dùng **kiểu
matcher khác nhau** — Claude Code khớp **theo tên tool**, Cursor khớp **theo regex lệnh**.

| Control / Hook | Cursor Agent | Claude Code | Chức năng tương đương | Rủi ro chạy hai lần | Khoảng hở khi chuyển | Bằng chứng | Verdict |
|---|---|---|---|---|---|---|---|
| briefing đầu phiên | khai báo, **có mã điểm danh** | **không** khai báo | ❌ không có | 🟢 thấp | briefing đầu phiên **không chạy** khi dùng Claude Code | điểm danh — lần nổ cuối **2026-08-16 23:16:35** | **`INACTIVE_PROVEN`** *(với Claude Code)* |
| cổng quản trị | khai báo, **không** có mã điểm danh | **không** khai báo | ❌ không có | 🟢 thấp | 🔴 **cổng quản trị mất hiệu lực** trong phiên Claude Code | không có dòng điểm danh nào | **`NOT_VERIFIED`** |
| cổng chống cắt cụt tài liệu | khai báo, **không** có mã điểm danh | **không** khai báo | ❌ không có | 🟢 thấp | 🔴 **chống cắt cụt mất hiệu lực** | không có dòng điểm danh nào | **`NOT_VERIFIED`** |
| cổng chất lượng mã | khai báo, **không** có mã điểm danh | **không** khai báo | ❌ không có | 🟢 thấp | cổng chất lượng mã mất hiệu lực | không có dòng điểm danh nào | **`NOT_VERIFIED`** |
| sổ tự động hoá deploy | khai báo, **không** có mã điểm danh | **không** khai báo | ❌ không có | 🟢 thấp | 🔴 **sổ deploy mất hiệu lực** | không có dòng điểm danh nào | **`NOT_VERIFIED`** |
| cổng `git commit` | **không** khai báo | **khai báo, CÓ mã điểm danh** | ❌ không có bản Cursor | 🟢 thấp | 🔴 **cổng commit mất hiệu lực khi dùng Cursor Agent** | điểm danh nổ **trong phiên này** | **`ACTIVE`** *(với Claude Code)* |
| khoá phiên ghi (lease) | dùng chung một tệp lease | dùng chung một tệp lease | ✅ **có** | 🟢 thấp | ✅ **không hở** | đọc được từ cả hai runtime | **`ACTIVE`** |

### Điều bắt buộc phải nói cho đúng chữ

⛔ **KHÔNG được kết luận hook Cursor "chết".** Chúng **`INACTIVE_PROVEN` / `NOT_VERIFIED` đối với
runtime Claude Code** — chúng **sẽ nổ** nếu Owner làm việc bằng Cursor Agent. Đây là hai chuyện
khác nhau, và trước đây đã bị gọi nhầm thành "chết".

### Rủi ro khi Owner chuyển giữa hai Agent

| câu hỏi | trả lời |
|---|---|
| **cổng nào mất hiệu lực?** | 🔴 Dùng **Claude Code**: mất cổng quản trị, chống cắt cụt, chất lượng mã, sổ deploy, briefing đầu phiên. 🔴 Dùng **Cursor Agent**: mất **cổng `git commit`** |
| **cổng nào chạy hai lần?** | 🟢 **Không cổng nào** — hai tập hợp **rời nhau hoàn toàn**, `DUPLICATE = 0` |
| **cổng nào không có chức năng tương đương?** | 🔴 **6 / 7** — chỉ **lease** có mặt ở cả hai bên |
| **bằng chứng nào còn thiếu?** | 4 / 5 hook Cursor **không có mã điểm danh** ⇒ **không chứng minh được** chúng từng nổ hay không, kể cả trong phiên Cursor. Đó là `NOT_VERIFIED`, **không** phải "không chạy" |

🔴 **Hệ quả thật, và nó nặng hơn cả hai vế trên:** vì hai tập hợp **rời nhau**, mỗi lần Owner đổi
Agent là **đổi luôn bộ cổng đang bảo vệ**. Không có lớp nào phủ cả hai, trừ lease.

⛔ Phiên này **không cài, không chuyển, không retire** hook nào.

---

## 7 · DECISION PACKET

> ⛔ **Không quyết định nào được tự ghi `APPROVED`.** Cả năm đều **`OWNER_DECISION_PENDING`**.

### PACKET 1 · CONTAINMENT / VISIBILITY

| | |
|---|---|
| **bằng chứng hiện có** | kho công khai đọc được ẩn danh (`HTTP 200`) · 112 ngày · `forks/stars/watchers = 0` |
| **điều chưa chứng minh** | có ai đã đọc hay chưa (`401`) · kho có public liên tục từ 06/05 hay không |
| **được gì** | cầm máu **ngay**, một thao tác |
| **mất gì** | ngược tinh thần §57 (báo cáo phải công khai) · link ngoài gãy |
| **rủi ro** | 🟢 **thấp nhất trong năm packet** — không xoá gì |
| **công sức dự kiến** | **phút** |
| **ảnh hưởng dữ liệu** | 🟢 **không** |
| **rollback** | bật lại public trong phần cài đặt kho — **không mất gì** |
| **khuyến nghị của Agent** | **Làm, nếu và chỉ nếu `PACKET 4` chưa chạy xong.** Nếu credential đã xoay và SSH đã siết thì giá trị công khai còn lại **gần như vô hại**, và chuyển private là cái giá không cần trả |
| ❓ **câu Owner cần xác nhận** | **Owner có muốn chuyển kho báo cáo sang private tạm thời trong lúc chờ xoay credential không?** |

### PACKET 2 · SCRUB CURRENT HEAD

| | |
|---|---|
| **bằng chứng hiện có** | 24 `CURRENT_HEAD_EXPOSURE`; danh sách **biết hết** vì `−0 dòng` |
| **điều chưa chứng minh** | 27 tệp `.png` chưa quét được nội dung |
| **được gì** | người xem bình thường không còn thấy; đúng `PRJ-RETRACTION-001` |
| **mất gì** | 🔴 **không giải quyết được gì cả** — 605 commit lịch sử **vẫn công khai** |
| **rủi ro** | 🔴 **rủi ro lớn nhất là TÂM LÝ** — dễ tưởng *"xong rồi"* trong khi giá trị vẫn đọc được từ lịch sử. Đúng bẫy `RM-12` |
| **công sức dự kiến** | **giờ** — 24 finding trải trên khoảng 300 tệp |
| **ảnh hưởng dữ liệu** | không đụng CSDL · SHA **không đổi** |
| **rollback** | `git revert` commit scrub — **không mất gì** |
| **khuyến nghị của Agent** | **Làm, nhưng SAU `PACKET 4`, và bắt buộc đi kèm việc nối cổng an toàn vào đường commit.** Scrub mà không nối cổng thì **tái lộ** — đúng lỗi §60.1 *bỏ nửa chừng còn tệ hơn không làm* |
| ❓ **câu Owner cần xác nhận** | **Owner có đồng ý scrub HEAD chỉ được chạy SAU khi cổng an toàn đã nối vào đường commit không?** |

### PACKET 3 · REWRITE GIT HISTORY

| | |
|---|---|
| **bằng chứng hiện có** | 605 commit · 23 + 38 + 121 commit chạm ba nhóm dấu vết · 🟢 **`forks = 0`** |
| **điều chưa chứng minh** | nhà cung cấp Git giữ commit mồ côi trong cache bao lâu |
| **được gì** | cách **duy nhất** gỡ giá trị khỏi Git; `forks = 0` nên **không phá bản sao của ai** |
| **mất gì** | 🔴 đổi **toàn bộ 605 SHA** ⇒ mọi trích dẫn commit trong tài liệu quản trị **chết hàng loạt** |
| **rủi ro** | 🔴 **cao nhất trong năm packet.** Force-push **không quay lại được** nếu làm sai |
| **công sức dự kiến** | **ngày** — kể cả việc soát lại các sổ trỏ SHA |
| **ảnh hưởng dữ liệu** | 🔴 mọi tham chiếu SHA trong sổ lịch sử tự động hoá và các sổ quản trị |
| **rollback** | 🔴 **bắt buộc có bản mirror TRƯỚC khi chạy**; không có mirror thì **KHÔNG gỡ về được** |
| **khuyến nghị của Agent** | **Chưa làm.** `forks = 0` nên **không gấp**, và nó chỉ có nghĩa **sau khi** credential đã xoay. Xét lại khi `PACKET 4` xong |
| ❓ **câu Owner cần xác nhận** | **Owner có đồng ý hoãn rewrite lịch sử tới sau khi xoay credential, và khi làm thì bắt buộc tạo bản mirror trước không?** |

### PACKET 4 · CREDENTIAL ROTATION

| | |
|---|---|
| **bằng chứng hiện có** | 4 nhóm `CRITICAL_SECRET` trong kho riêng · phơi **156 ngày** / **52 ngày** · `OD-05` verdict **`RISK_CONFIRMED`** |
| **điều chưa chứng minh** | ai đã có quyền đọc kho riêng (`401`, không liệt kê được cộng tác viên) · lịch sử kho riêng **chưa quét** · ứng viên mật khẩu **thứ năm** chưa hoà giải · `OD-05` **`RUNTIME_UNVERIFIED`** |
| **được gì** | 🔴 việc **duy nhất** vô hiệu hoá thứ đã bị đọc. Xoay khoá máy chủ còn chặn được **giả mạo chính máy chủ** — thứ mà **không thao tác Git nào** làm được |
| **mất gì** | gián đoạn ngắn khi đổi khoá và khoá API |
| **rủi ro** | 🟠 trung bình — làm sai có thể **tự khoá mình ra ngoài máy chủ**; bắt buộc giữ một phiên đang mở khi đổi |
| **công sức dự kiến** | **giờ** |
| **ảnh hưởng dữ liệu** | 🟢 không đụng dữ liệu · có thể gián đoạn dịch vụ ngắn nếu phải khởi động lại |
| **rollback** | khoá cũ **không nên** khôi phục *(đó chính là mục đích của việc xoay)*; đường lui là giữ một phiên đang mở |
| **khuyến nghị của Agent** | 🔴 **ƯU TIÊN CAO NHẤT — làm TRƯỚC mọi việc dọn Git.** Gỡ khỏi Git **không thu hồi** được thứ đã bị đọc |
| ❓ **câu Owner cần xác nhận** | **Owner có cho phép mở một lượt riêng với quyền ghi máy chủ để xoay mật khẩu, sinh lại khoá máy chủ, thu hồi và cấp lại khoá API, và siết tư thế xác thực SSH không?** |

### PACKET 5 · HOOK MIGRATION / RETIREMENT

| | |
|---|---|
| **bằng chứng hiện có** | ma trận mục 6 · hai tập hợp cổng **rời nhau** · `DUPLICATE = 0` · 4/5 hook Cursor **không có mã điểm danh** |
| **điều chưa chứng minh** | 4 hook Cursor có từng nổ trong phiên Cursor hay không — **`NOT_VERIFIED`**, không đo được vì thiếu điểm danh |
| **được gì** | Owner đổi Agent mà **không đổi bộ cổng đang bảo vệ** |
| **mất gì** | công dựng bản tương đương cho từng bên |
| **rủi ro** | 🟠 trung bình — làm ẩu có thể **chặn nhầm** hoặc tạo **chồng tầng** mà §60 cấm |
| **công sức dự kiến** | **ngày** |
| **ảnh hưởng dữ liệu** | 🟢 không |
| **rollback** | gỡ khai báo hook, khôi phục tệp cấu hình |
| **khuyến nghị của Agent** | 🔴 **Việc đầu tiên phải làm là THÊM MÃ ĐIỂM DANH cho 4 hook Cursor** — không đo được thì không quyết được (`RM-15`: **cổng không qua thử coi như không tồn tại**). **Chưa** migrate, **chưa** retire |
| ❓ **câu Owner cần xác nhận** | **Owner có đồng ý bước đầu chỉ THÊM mã điểm danh cho 4 hook Cursor để đo, chưa chuyển và chưa retire hook nào không?** |

---

## 8 · VƯỚNG VẤP

### V1 · 🔴 Bốn con số cùng nói về một thứ — `24 / 26 / 27 / 29`

Cả bốn **đều đúng**, chỉ là **bốn thước khác nhau** — đúng loại lỗi `RM-21` (hằng số đo trên
thước này bị đem sang thước khác):

| con số | thước |
|---|---|
| **24** | tệp `.md` chứa chuỗi, đo ở HEAD **trước** phiên V11123 |
| **26** | tệp `.md` chứa chuỗi ở HEAD **hiện tại** — `+2` là **chính hai báo cáo V11123** tự thuật lại bằng chữ đã che |
| **27** | **mọi loại tệp** có chuỗi đăng nhập dạng số = 22 tệp `.md` + 5 tệp `.txt` |
| **29** | lộ thật = 27 dạng số + 2 dạng bí danh |
| **31** | mọi tệp chứa chuỗi, kể cả bản đã che |

🔴 **Hậu quả vận hành — đây mới là điều đáng ghi:** kế hoạch che bám theo con số **24** sẽ
**bỏ sót 5 tệp không phải `.md`** vẫn còn chuỗi đăng nhập.

### V2 · 🔴 Một lane của chính phiên này kết luận sai

Lane đối chiếu số báo *«27 không tái lập được bằng bất kỳ phép đếm local nào»*. **Sai** — nó chỉ
phân loại 26 tệp `.md` mà bỏ 5 tệp `.txt`. Đo lại bằng mẫu có nhóm số trên **mọi loại tệp** thì
ra đúng **27**. Ghi lại để không ai dùng kết luận sai đó.

### V3 · 🔴 Chính Agent viết một câu ở giọng toàn cục trong khi số chỉ đúng cho một kho

Bản kiểm kê đầu viết *«0 credential trong toàn bộ lịch sử»*. Câu đó **chỉ đúng cho kho công
khai**; kho riêng có 4 nhóm. Đã **rút lại trong cùng phiên** theo `PRJ-RETRACTION-001` **trước
khi phát hành** — nên bản công bố này **không mang câu sai đó**.

### V4 · Công cụ quét bí mật **không có trên máy**

Bốn công cụ chuẩn đều vắng ⇒ phải tự viết bộ quét. Ghi thẳng là `BLOCKED_TOOLING`, **không** báo
*"đã quét sạch"*.

### V5 · Lỗi mã hoá console khi in ký tự biểu tượng

Đúng bẫy đã ghi trong tài liệu vận hành. Xử bằng nhãn ASCII.

---

## 9 · GỠ VỀ

Phiên kiểm kê **không có gì để gỡ** — không mutation nào (mục **H**).

Phiên phát hành này chỉ **thêm mới** một thư mục báo cáo. Gỡ về:
`git revert <COMMIT_SHA>` — không đụng báo cáo cũ, không đổi SHA lịch sử.

**Vì sao verdict kiểm kê là `PARTIAL` chứ không `COMPLETE`:**

1. 🔴 **`ACCESS_EVIDENCE_NOT_AVAILABLE`** — API lưu lượng `401`, không biết có ai đã đọc.
2. 🔴 **`BLOCKED_TOOLING`** — không có scanner chuyên dụng; quét theo mẫu, **không dò entropy**.
3. 🟡 **`NOT_CHECKED`** — 27 tệp `.png` tại HEAD + 56 blob nhị phân trong lịch sử.
4. 🟡 **`NOT_CHECKED`** — **toàn bộ lịch sử kho riêng** (chỉ quét HEAD).
5. 🟡 **`RUNTIME_UNVERIFIED`** — `OD-05` đọc từ ảnh chụp 52 ngày tuổi.
6. 🟡 ứng viên mật khẩu **thứ năm** chưa hoà giải.

---

## 10 · THEO DÕI TIẾP

| mã | việc | trạng thái |
|---|---|---|
| `FU-438` | bịt bề mặt công khai — **`CODE_IMPLEMENTED`**, **`NOT_DEPLOYED`** | chờ Owner |
| `FU-441` | hai runtime, hai bộ cổng rời nhau | `PACKET 5` |
| `FU-444` | cổng an toàn **chưa nối** vào đường commit — **nguyên nhân gốc** của 112 ngày phơi | `PACKET 2` |
| *(mới)* | xoay credential kho riêng | `PACKET 4` — **ưu tiên cao nhất** |
| *(mới)* | quét lịch sử kho riêng | **`NOT_CHECKED`**, phải đóng |
| *(mới)* | hoà giải ứng viên mật khẩu thứ năm | `RM-11` |
| *(mới)* | thêm mã điểm danh cho 4 hook Cursor | `PACKET 5` bước 1 |

---

## 11 · BA LỚP NGUỒN (§62)

### `OWNER_SAID`

Nguyên văn + giờ ở **mục 2**. Hai quyết định: `D-22` (26/08 sáng) · `D-23` (26/08 09:13 ICT).

### `CODE_DID`

| việc | bằng chứng |
|---|---|
| kho công khai đọc được ẩn danh | `HTTP 200`, 26.700 byte, lúc `08:16:39` |
| kho riêng **không** đọc được ẩn danh | `HTTP 404` |
| 0 vật liệu xác thực kho công khai | 3.262 blob × 20 mẫu |
| ranh giới giữ được | 0/3 mẫu đại diện lọt |
| chưa từng che | `+64/−0` · `+95/−0` · `+1.267/−5` |
| số hiệu `V11124` trống | cổng cấp số quét sáu nơi, thoát `0` |
| không mutation | HEAD hai kho y nguyên; reflog mới nhất trước giờ mở phiên |

### `DOC_SAID`

| nguồn | ghi gì |
|---|---|
| `CLAUDE.md §61` | `RM-11` số phải tái lập · `RM-12` cấm nâng tầng · `RM-13` nguồn phải là production thật · `RM-15` cổng không thử coi như không tồn tại · `RM-20` "0 dòng mới" ≠ "không ai đọc" · `RM-21` hằng số chỉ đúng cho thước đã đo nó |
| `CLAUDE.md §57.3` | khung báo cáo 9 phần |
| `CLAUDE.md §62` | ba lớp nguồn + dòng cuối bắt buộc |
| `PRJ-RETRACTION-001` | rút lại phải đủ bốn phần |

### 🔴 BA LỚP LỆCH NHAU — finding bắt buộc báo

| lệch | chi tiết |
|---|---|
| `DOC_SAID` ≠ `CODE_DID` | tài liệu tổng kết ghi *«một tệp em KHÔNG đẩy»* — tệp đó **đã ở trên nhánh chính** từ 25/08 và đọc ẩn danh được |
| `DOC_SAID` ≠ `CODE_DID` | *«hook Cursor chết»* — **không chết**; chúng `INACTIVE_PROVEN` / `NOT_VERIFIED` **với runtime Claude Code**. Chữ khác, hậu quả giống |
| nội bộ phiên | một lane kết luận *«27 không tái lập được»* — **tái lập được**, mục 8 V2 |

---

TanPhatAI cần làm: mở mục theo dõi ưu tiên cao nhất cho **xoay credential kho riêng** (`PACKET 4`) trong `docs/FOLLOW_UP_TRACKER.md`, và ghi vào `docs/SO_TUONG_TAC_OWNER.md` rằng phiên D-22 kết thúc ở trạng thái **`CRITICAL_SECRET_FOUND` — đã dừng, chưa xử lý**, còn D-23 chỉ là **bàn giao bằng chứng**, không phải xử lý; theo dõi tiếp `FU-444` (cổng chưa nối — nguyên nhân gốc), `FU-441` (`PACKET 5`) và `FU-438` (**`NOT_DEPLOYED`**). **Đừng** đọc *«0/3 không lọt»* thành *«an toàn»* — vật liệu xác thực vẫn nằm trong Git của kho riêng, chỉ là chưa ra công khai. **Đừng** đọc *«`CREDENTIAL_COMPROMISE_NOT_PROVEN`»* thành *«không ai đọc»* — bằng chứng truy cập là `NOT_AVAILABLE`, không phải âm tính. **Chi tiết `OD-05` cố ý không có trong báo cáo công khai này** — lấy ở local. Năm packet đều **`OWNER_DECISION_PENDING`**, chưa cái nào được ký.
