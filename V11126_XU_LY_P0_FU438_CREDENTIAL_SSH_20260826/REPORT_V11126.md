# REPORT V11126 — XỬ LÝ BA VIỆC P0: `FU-438` · CREDENTIAL · SSH/ACCESS

```
REPORT_VERSION        : V11126
REPORT_TITLE          : Xử lý P0 — ADMIN_ONLY đủ sáu endpoint · bỏ gán cứng credential ·
                        truy nguồn hai khoá lạ và đường phục hồi một máy
WORK_DATE_ICT         : 2026-08-26
PUBLISHED_AT_ICT      : xem mục bàn giao
TIMEZONE              : Asia/Ho_Chi_Minh / UTC+07:00
OWNER_DECISION        : D-22 · D-23 · D-24 KEEP_PUBLIC_CURRENT · prompt 38 SINGLE_DEVICE_OPERATION
AUTHORIZED_SCOPE      : LOCAL/BRANCH CODE+TEST · VPS_SSH_READ_ONLY · REPORT_ONLY_PUSH
PREVIOUS_PUBLIC_HEAD  : db67cf2fabbc5700946bc8d464c9f18e885e9ea5
ACTOR_RUNTIME         : CLAUDE_CODE  (Cursor Agent không cần — outbound đã thông)
LABELS                : P0_HANDLED · CODED_NOT_DEPLOYED · SINGLE_DEVICE_OPERATION ·
                        ADMIN_ONLY · OWNER_DECISION_PENDING
```

> ⛔ **Phiên này KHÔNG deploy, KHÔNG restart, KHÔNG xoay credential, KHÔNG sửa SSH, KHÔNG chạm
> hook.** Mọi thứ dừng ở **`CODED_NOT_DEPLOYED`**.

---

## 1 · TÓM TẮT BẰNG LỜI THƯỜNG

Ba việc P0 đã làm xong phần **code và thử**, đúng thứ tự Owner khoá.

**Việc lớn nhất — và cũng là tin tốt nhất — nằm ở P0-C.** Máy chủ đang bị dò mật khẩu **rất
nặng**: gần **294.000 lần thử thất bại** từ **1.470 địa chỉ khác nhau**, trong khi cổng mật khẩu
vẫn mở và **không có bộ chặn nào được cài**. Nhưng đọc toàn bộ log giữ được thì **số lần đăng
nhập bằng mật khẩu thành công là `0`**, và **chỉ đúng MỘT khoá** từng đăng nhập thành công. Tức
là: **bị gõ cửa liên tục, chưa ai vào được.**

| việc | trạng thái |
|---|---|
| **P0-A** `FU-438` | 🟢 **XONG code+thử** — sáu endpoint `ADMIN_ONLY`, thử **56/56 ĐẠT** bằng lời gọi thật |
| **P0-B** credential | 🟢 **XONG code+thử** — lớp nguồn bí mật fail-closed, thử **16/16 ĐẠT** |
| **P0-C** SSH/access | 🟠 **XONG phần đọc** — hai khoá lạ đã phân loại, patch đã soạn, **chưa áp** |

Và **ba con số cũ phải đính chính**, cả ba đều theo hướng **nhẹ đi**:

| con số cũ | đúng là |
|---|---|
| *«157 tệp chứa `SC-04`»* | **40** tệp local, trong đó **34** là consumer thật |
| *«`SC-03` trong 5 tệp»* | **1** tệp local, và là **bản sao lưu** ⇒ **0 consumer hoạt động** |
| *«14 route nhạy cảm không cổng»* | **1** — mười ba cái kia là đếm theo từ khoá nên thừa |

---

## 2 · P0-A · `FU-438` — ADMIN_ONLY ĐỦ SÁU ENDPOINT

### 2.1 · Đã kiểm caller **trước** khi khoá

Sổ `FU-438` ghi rõ **⛔ *«CẤM tự khoá trước khi kiểm caller»***. Đã làm đúng thứ tự đó:

| nhóm caller | kết quả |
|---|---|
| **cron / scheduler** | 🟢 **0** — khoá **không vỡ lịch** |
| **frontend** | **9 lời gọi thật** trên 6 tệp |
| phân loại theo `RM-09` | **9 gọi thật** · **3 chú thích** · **2 mock** — chú thích và mock **không** bị ảnh hưởng |

Một chỗ suýt đếm nhầm: một trang có dòng nhắc endpoint nhưng đó là **chú thích** ghi rằng nó
*từng* gọi — bản `V10877` đã gỡ từ lâu.

**Hai trang công khai sẽ rỗng với khách.** Đó **đúng ý** lệnh Owner ký 06–08/06
*«Treo TOÀN BỘ view người dùng»* và prompt 33 *«Đóng toàn bộ viewer/anonymous»*.

### 2.2 · Bản vá — hẹp, `+31 / −9` dòng

| | trước | sau |
|---|---|---|
| `/api/predictions` | **chỉ LỌC TRƯỚNG** cho khách ⇒ **số dự đoán vẫn ra khỏi cửa** | `_cong_bundle_admin()` **chặn ngay ở cửa**, fail-closed |
| khối lọc trường | đang chạy | **đã gỡ khỏi đường chạy** |
| hằng số `_TRUONG_LICH_SU_KHACH_DUOC_XEM` | không nhãn | **dán nhãn `NGHỈ HƯU`** — giữ dấu vết, chặn việc dùng lại |

> Vì sao **dán nhãn** thay vì xoá: xoá thì mất dấu vì sao hằng số từng được nới; để **không nhãn**
> thì người sau đọc tên sẽ tưởng khách vẫn được xem, rồi *«khôi phục»* đúng thứ vừa gỡ — đúng bẫy
> **§60.1**.

### 2.3 · Route matrix — **211 route** trong `main.py`

| cổng | số route |
|---|---|
| `require_admin` | **143** |
| **`CONG_ADMIN` (fail-closed)** | **7** *(6 endpoint + định nghĩa)* |
| chỉ đóng băng, không chặn | 2 |
| yêu cầu đăng nhập | 1 |
| **không có cổng** | 58 |

**Sáu endpoint sau khi vá — tất cả `CONG_ADMIN` fail-closed:**
`/api/final-bundle` · `/api/final-bundle/history` · `/api/final-bundle/selection-delta` ·
`/api/prediction-trace` · `/api/prediction-quality` · `/api/predictions`

🔴 **Còn đúng MỘT route chưa khoá mà vẫn trả trường chứa số:** `/api/slice-recommendation`
— **`HTTP 200`** với khách, và **2 trang frontend đang gọi**. **Chưa tự khoá**: sổ `FU-438` ghi
phần cần Owner ký là *«cách khoá để không làm vỡ caller nội bộ»*.

> ⚠️ **Đính chính ngay trong phiên:** bản quét đầu của tôi báo **14 route** nhạy cảm không cổng.
> Con số đó **đếm theo từ khoá nên thừa**. Xác minh xem route có **thật sự trả trường chứa số**
> hay không thì còn **1**. Mười ba route kia nhắc thuật ngữ liên quan nhưng **không phát ra số**.

### 2.4 · Thử chặn — **56/56 ĐẠT**, gọi thật bằng client

| vai | kết quả trên cả 6 endpoint |
|---|---|
| **khách vô danh** | 🟢 **`HTTP 401`** — 6/6 |
| **đã đăng nhập, KHÔNG phải admin** | 🟢 **`HTTP 403`** — 6/6 |
| ├─ `role = user` · `role` rỗng · không phải đối tượng · **tầng auth NỔ** | 🟢 cả **bốn** kiểu đều bị chặn |
| **admin** | 🟢 **`HTTP 200`** — 6/6, thấy đủ |
| `/api/health` | 🟢 **vẫn mở** — không chặn nhầm đường giám sát |

> Nhóm *«tầng auth NỔ»* là phép quan trọng nhất: nó chứng minh cổng **fail-CLOSED** — khi tầng
> xác thực ném lỗi, cổng trả **403** chứ không cho qua.

### 2.5 · Gỡ về

| | |
|---|---|
| **artifact** | `web/backend/main.py` trên nhánh `fu438/admin-only-p0a` |
| **blob** | `57522fa7b81f` *(trước: `83a4657cd471`)* |
| **bản sao lưu** | `backups/main.py.pre_fu438_p0a_20260826_141159` |
| **gỡ về** | `git checkout master -- web/backend/main.py` · hoặc `git revert <commit nhánh>` |
| **ảnh hưởng** | chỉ tầng xác thực. **Không** đụng đường ghi `final_bundles`, **không** đụng bộ chọn model, **không** đụng settlement |
| **cửa deploy an toàn** | ngoài giờ chốt cả ba miền — sau `18:05` |

---

## 3 · P0-B · CREDENTIAL — CONSUMER THẬT VÀ BỎ GÁN CỨNG

### 3.1 · 🔴 Đính chính quy mô — «157» là con số sai đường

| alias | đo trên máy chủ | đo local | **consumer THẬT** |
|---|---|---|---|
| `SC-03` | 5 tệp | **1** tệp | 🟢 **0** — tệp duy nhất là **bản sao lưu** |
| `SC-04` | 157 tệp | **40** tệp | **34** script triển khai |

**Phân loại đủ theo taxonomy:**

| nhóm | `SC-03` | `SC-04` |
|---|---|---|
| **active runtime source** | **0** | 🟢 **0** |
| **deploy script** | 0 | 🔴 **34** |
| copy/backup | 1 | 0 |
| test/example | 0 | 6 |
| dead artifact | 0 | 0 |

🟢 **Kết luận đổi hẳn kế hoạch xoay:** `SC-04` **không có consumer runtime nào**. Nó là credential
của **công cụ vận hành chạy tay**, không phải của dịch vụ đang chạy. ⇒ Xoay nó **không cần khởi
động lại dịch vụ**, **không gây gián đoạn**.

Củng cố bằng đo runtime: biến môi trường của tiến trình đang chạy chứa **0** tham chiếu tới cả
`SC-03` lẫn `SC-04`.

⚠️ Vẫn **KHÔNG** được gọi là `ACTIVE_RUNTIME_PROVEN`: đã chứng minh **có mặt trong cấu hình/mã**,
**chưa** chứng minh tiến trình **thực sự dùng**.

### 3.2 · Lớp nguồn bí mật — `_v11126_nguon_bi_mat.py`

Ba luật, và **luật 1 là lý do tệp này tồn tại**:

| # | luật | vì sao |
|---|---|---|
| **1** | **FAIL-CLOSED** — thiếu bí mật thì **ném lỗi**, **không** có giá trị mặc định | trả rỗng là cách credential sai đi tiếp vào lệnh thật rồi hỏng ở chỗ khó truy |
| **2** | **không bao giờ log giá trị** — kể cả trong thông điệp lỗi | thông điệp chỉ nêu **tên** và **nguồn đã thử** |
| **3** | **không trạng thái lẫn** — một tiến trình chỉ thấy **một** giá trị cho một tên | tránh nửa cũ nửa mới giữa chừng |

⛔ **Chỉ đổi biến môi trường là vô ích** nếu mã còn dòng gán cứng — nên mẫu chuyển đổi là **thay
chính dòng gán**, mỗi script **đúng một dòng đổi**.

### 3.3 · Thử chặn fixture — **16/16 ĐẠT**

| tính chất bắt buộc | kết quả |
|---|---|
| ① thiếu bí mật ⇒ **fail closed** | 🟢 ném đúng loại lỗi · `co_bi_mat()` trả `False` không ném ra ngoài |
| ② **không log** bí mật | 🟢 thông điệp không chứa giá trị · có nêu tên để gỡ được · module không chứa chuỗi nào giống credential · **không có giá trị mặc định** |
| ③ **parity** cũ/mới | 🟢 nguồn mới trả đúng giá trị consumer cũ đang dùng |
| ④ **rollback** | 🟢 quay lại giá trị cũ được |
| ⑤ **không trạng thái lẫn** | 🟢 đổi nguồn giữa chừng không làm tiến trình thấy hai giá trị |
| phụ: tệp bí mật hỏng | 🟢 **vẫn** fail-closed, không nổ kiểu khác |

> **Một phép thử của tôi đã sai và tôi sửa phép thử, không nới lỏng nó.** Bản đầu đặt luật
> *«module không được nhắc TÊN biến bí mật»* rồi báo HỎNG vì tài liệu có chữ `VPS_PASS`. **Luật
> đó sai:** tên biến **không phải bí mật** — nó đã nằm công khai trong 40 tệp. Yêu cầu thật là
> **không log GIÁ TRỊ**. Đã sửa phép thử về đúng thứ phải kiểm.

⛔ **Chưa migrate 34 script và chưa xoay giá trị thật** — chờ cổng thay đổi riêng.

---

## 4 · P0-C · SSH / ACCESS TRONG CHẾ ĐỘ MỘT MÁY

### 4.1 · 🔴 Sự thật vận hành nặng nhất của cả phiên

| phép đo | kết quả |
|---|---|
| lần thử mật khẩu **thất bại** | 🔴 **293.748** |
| địa chỉ nguồn tấn công **khác nhau** | 🔴 **1.470** |
| bộ chặn dò mật khẩu | 🔴 **CHƯA ĐƯỢC CÀI** — không phải tắt, mà là **không có** |
| xác thực bằng mật khẩu | 🔴 **đang bật** |
| **lần đăng nhập bằng MẬT KHẨU thành công** | 🟢 **`0`** |
| số **vân tay khoá phân biệt** từng đăng nhập thành công | 🟢 **1** |
| lần đăng nhập bằng khoá thành công | 6.230 |

🟢 **Đọc cho đúng:** cửa đang bị gõ rất mạnh, **chưa ai vào được bằng mật khẩu**, và **chỉ một
khoá duy nhất** từng vào. Không có bằng chứng xâm nhập.

⚠️ **Giới hạn:** log giữ được chỉ vài ngày. *«Chưa ai vào»* đúng **trong cửa sổ đó**, không phải
mọi thời điểm.

### 4.2 · Hai khoá lạ — phân loại

| bằng chứng | kết quả |
|---|---|
| `authorized_keys` sửa lần cuối | **2026-04-10** — **trước** ngày kho báo cáo được tạo (06/05) |
| số khoá | **3** — một là khoá Owner đang dùng |
| tuỳ chọn hạn chế (`from=`, `command=`, …) | 🔴 **KHÔNG có** — cả ba khoá **toàn quyền** |
| từng đăng nhập thành công trong log | 🟢 **không** — chỉ 1 vân tay xuất hiện, và đó là khoá đang dùng |

| khoá | phân loại |
|---|---|
| `UNATTRIBUTED_AUTHORIZED_KEY_1` | **`LEGACY_UNATTRIBUTED`** |
| `UNATTRIBUTED_AUTHORIZED_KEY_2` | **`LEGACY_UNATTRIBUTED`** |

⛔ **Không** kết luận xâm nhập chỉ vì không nhận diện được khoá. ⛔ **Không** coi khoá là an toàn
chỉ vì log chưa thấy dùng. ⛔ **Không** suy chúng là khoá cũ của Owner. ⛔ **Không** thử, **không**
xoá.

### 4.3 · Đường phục hồi — **không cần máy thứ hai**

| cơ chế | trạng thái đo được |
|---|---|
| `cloud-init` | 🟢 **có** |
| loại ảo hoá | KVM |
| agent nhà cung cấp đang chạy | 🟢 **6** dịch vụ |
| **serial console** | 🟢 **`enabled-runtime`** |
| mục **recovery mode** trong bộ nạp khởi động | 🟢 **2** mục |

**`RECOVERY_PATH = NOT_VERIFIED`** — và đây là chỗ phải nói cho đúng: tôi chứng minh được **máy
chủ có bật** các cơ chế đó, nhưng **không** chứng minh được Owner **truy cập tới** bảng điều khiển
nhà cung cấp, vì đó nằm ở phía tài khoản nhà cung cấp, ngoài tầm đọc của tôi.

🟢 **Tin tốt cho chế độ một máy:** đường phục hồi **rất có khả năng tồn tại** và **không cần máy
thứ hai** — chỉ cần Owner đăng nhập bảng điều khiển nhà cung cấp bằng trình duyệt.

⛔ **Không** sinh khoá thứ hai trên **cùng một máy** rồi gọi là đường dự phòng độc lập — cùng một
máy hỏng thì mất cả hai.

### 4.4 · `OD-05` — nguyên nhân gốc và bản vá

**Vì sao thiết lập cho phép mật khẩu thắng:** `sshd` dùng luật **giá trị đọc được ĐẦU TIÊN thắng**.
Dòng **12** của tệp cấu hình chính là chỉ thị `Include` cho thư mục drop-in, và trong đó có một
tệp của `cloud-init` **bật lại** xác thực bằng mật khẩu. Vì `Include` nằm **sớm**, giá trị của
`cloud-init` được đọc **trước** mọi thiết lập về sau.

*(Cặp chỉ thị + giá trị cụ thể **cố ý không in ở đây** — §VIII.6 cấm đưa cấu hình có thể hỗ trợ
tấn công vào báo cáo công khai. Chi tiết có ở local.)*

⇒ **Sửa tệp chính là vô ích.** Bản vá phải là một drop-in **sắp trước** tệp `cloud-init` theo thứ
tự chữ cái.

**Bản vá đã soạn — thử cú pháp 10/10 ĐẠT, CHƯA ÁP:**

| thay đổi | vì sao chọn thế |
|---|---|
| `PermitRootLogin prohibit-password` | **không** dùng `no` — `no` sẽ chặn **cả** đường vào bằng khoá đang dùng ⇒ tự khoá mình ra ngoài |
| `PasswordAuthentication no` | bịt bề mặt đang bị 1.470 địa chỉ dò |
| bật tường minh xác thực bằng khoá | tệp chính mới chỉ để dạng chú thích |
| giảm số lần thử và thời gian chờ | giảm bề mặt dò |
| cấu hình bộ chặn dò mật khẩu | **chưa cài**, nên phải cài trước khi bật |

**Mô phỏng luật «giá trị đầu tiên thắng»** xác nhận bản vá **đổi đúng hướng** cho cả hai chỉ thị:
từ trạng thái **cho phép** sang trạng thái **siết**, và drop-in mới thắng tệp của `cloud-init`.
*(Giá trị hiện tại của từng chỉ thị **cố ý không in** — §VIII.6.)*

⛔ **Bản vá có ghi thẳng trong chính nó: CẤM áp khi đường phục hồi còn `NOT_VERIFIED`.** Tắt mật
khẩu mà chưa có đường vào dự phòng đã chứng minh là **tự khoá mình ra ngoài**.

---

## 5 · ĐÍNH CHÍNH BẮT BUỘC

| # | mục | đính chính |
|---|---|---|
| **1** | `SC-01` · `SC-02` | chỉ được gọi **`STALE_FOR_THIS_VPS`** — **không** loại khỏi kiểm kê toàn cục khi chưa kiểm máy khác |
| **2** | *«2 M»* | là **cây làm việc kho riêng** |
| **3** | *«2 A»* | là **commit kho công khai** |
| **4** | cả hai | **đều đúng**; lỗi là **thiếu nhãn phạm vi**, không phải sai số |
| **5** | fail-open | **chỉ** cổng quản trị có phát hiện fail-open, và bản vá fixture **6/6** |
| **6** | hai cổng kia | **bỏ qua stdin theo hợp đồng**, và trả `ask` khi thiếu bộ soi |
| **7** | trạng thái | **`PRESENT_IN_ACTIVE_CONFIG` KHÔNG tự động bằng `ACTIVE_RUNTIME_PROVEN`** |
| **8** *(mới)* | «157 tệp» | đo local = **40**, consumer thật = **34** |
| **9** *(mới)* | «14 route nhạy cảm» | xác minh thật = **1** |

---

## 6 · TÁCH LỚP XÁC MINH

| lớp | nội dung |
|---|---|
| **`GITHUB_VERIFIED`** | `PREVIOUS_PUBLIC_HEAD = db67cf2…` · báo cáo này sau khi push |
| **`LOCAL_VERIFIED`** | `FU-438` **56/56** · nguồn bí mật **16/16** · patch `OD-05` **10/10** · route matrix 211 route · consumer map `SC-03`/`SC-04` |
| **`VPS_RUNTIME_VERIFIED`** | 293.748 lần thử thất bại · 1.470 địa chỉ · **0** đăng nhập mật khẩu thành công · **1** vân tay khoá · bộ chặn **chưa cài** · `authorized_keys` sửa **2026-04-10** · serial console **bật** · 2 mục recovery |
| **`CODED_NOT_DEPLOYED`** | `FU-438` · lớp nguồn bí mật · patch `OD-05` — **cả ba** |
| **`NOT_VERIFIED`** | đường phục hồi độc lập · chủ sở hữu hai khoá lạ · `SC-05`/`SC-08` runtime map · dò entropy |

---

## 7 · BA LỚP NGUỒN (§62)

### `OWNER_SAID`

> *« Xử lý các vấn đề P0 thật. Không để việc Owner chưa có máy thứ hai làm treo `FU-438`,
> credential remediation hoặc code fix. »*
>
> *« Owner chỉ code/fix trên một máy hiện tại — `SINGLE_DEVICE_OPERATION`. »*
>
> *« Owner không rõ và không giữ hai SSH key còn lại. Chúng phải được ghi
> `UNATTRIBUTED_AUTHORIZED_KEYS`. Chúng **không phải** backup của Owner. »*
>
> *« Không giữ ngoại lệ public `/user-view` nếu policy Owner không đổi. »*
>
> *« Không diễn giải câu "xử lý vấn đề chính" thành blanket deploy approval. »*
>
> *« Không yêu cầu Owner chạy lệnh kỹ thuật thường ngày. »*

### `CODE_DID`

| việc | bằng chứng |
|---|---|
| 6 endpoint `ADMIN_ONLY` | thử **56/56**, gọi thật: 401 / 403 / 200 |
| caller đã kiểm trước khi khoá | cron **0** · frontend 9 gọi thật (3 chú thích + 2 mock đã loại) |
| lớp nguồn bí mật | **16/16**, gồm cả tệp hỏng vẫn fail-closed |
| consumer thật | `SC-03` **0** · `SC-04` **34** |
| dò mật khẩu | **293.748** thất bại · **0** thành công |
| hai khoá lạ | `authorized_keys` mtime **2026-04-10** · **1** vân tay từng dùng |
| `OD-05` nguyên nhân gốc | `Include` sớm + luật *giá trị đầu tiên thắng* |
| patch `OD-05` | **10/10**, có mô phỏng luật thắng |
| **không mutation** | xem mục 8 |

### `DOC_SAID`

| nguồn | ghi gì |
|---|---|
| `FOLLOW_UP_TRACKER` `FU-438` | *«CẤM tự khoá trước khi kiểm caller»* · phần cần Owner ký là **cách khoá** |
| Owner ký 06–08/06 | *«Treo TOÀN BỘ view người dùng»* |
| `CLAUDE.md §60.1` | gỡ dữ liệu mà để nhãn ở lại thì nhãn tự dạy lại |
| `RM-09` | cấm đếm chuỗi thô, phải phân loại |
| `RM-15` | cổng không qua thử coi như không tồn tại |

### 🔴 BA LỚP LỆCH NHAU

| lệch | chi tiết |
|---|---|
| `DOC_SAID` ≠ `CODE_DID` | sổ ghi `SC-04` trong **157** tệp; đo local **40**, consumer thật **34** |
| `DOC_SAID` ≠ `CODE_DID` | bản quét đầu của chính tôi báo **14** route nhạy cảm; xác minh còn **1** |
| `OWNER_SAID` ≠ `CODE_DID` | Owner ký *«treo toàn bộ view người dùng»* từ **06/06**; tới **26/08** `/api/predictions` vẫn chỉ **lọc trường** — nay mới thật sự chặn |

---

## 8 · NO-MUTATION PROOF

| khẳng định | |
|---|---|
| production không đổi · không deploy · không restart | ✅ |
| DB không ghi | ✅ |
| credential không xoay | ✅ |
| SSH không sửa — `authorized_keys` · `sshd_config` · dịch vụ | ✅ |
| hai khoá lạ **không** bị xoá | ✅ |
| hook runtime không đổi | ✅ |
| Git history không rewrite · visibility không đổi | ✅ |
| báo cáo cũ không sửa/xoá | ✅ |
| **private code không push** | ✅ — commit **chỉ nằm trên nhánh local** `fu438/admin-only-p0a` |

Mọi lệnh chạy trên máy chủ đều **chỉ đọc**, và **34 lệnh** đều qua preflight
`READ_ONLY_PROVEN` trước khi chạy. Bộ soi preflight **tự chứng minh chặn được** bằng 5 đối chứng
xấu (ghi tệp · `tee` · restart · `sudo` shell · tải-rồi-chạy) — cả 5 đều **FAIL** đúng.

---

## 9 · CÒN LẠI

| việc | trạng thái |
|---|---|
| `/api/slice-recommendation` | 🔴 route **duy nhất** còn trả trường chứa số cho khách — chờ Owner ký cách khoá |
| migrate 34 script sang lớp nguồn bí mật | `CODED_NOT_DEPLOYED` |
| xoay `SC-03` · `SC-04` | chờ cổng thay đổi riêng |
| áp patch `OD-05` + cài bộ chặn dò | 🔴 **chặn bởi** `RECOVERY_PATH = NOT_VERIFIED` |
| chủ sở hữu hai khoá lạ | `NOT_VERIFIED` |
| `SC-05` · `SC-08` runtime map | `NOT_VERIFIED` |
| report backfill · hook · family · `D3` | P1/P2 — **sau** ba P0 |

---

TanPhatAI cần làm: ghi vào `docs/FOLLOW_UP_TRACKER.md` rằng `FU-438` nay **`CODED_NOT_DEPLOYED`** với thử **56/56**, và mở một mục mới cho **`/api/slice-recommendation`** — route **duy nhất** còn lộ trường chứa số, cần Owner ký cách khoá. Ghi ba đính chính số liệu: `SC-04` là **40 tệp local / 34 consumer thật** (không phải 157), `SC-03` có **0 consumer hoạt động**, và *«14 route nhạy cảm»* xác minh thật chỉ còn **1**. Ghi vào `docs/SO_TUONG_TAC_OWNER.md` trạng thái **`SINGLE_DEVICE_OPERATION`** và rằng hai khoá trong `authorized_keys` là **`UNATTRIBUTED_AUTHORIZED_KEYS`** — **không phải** backup của Owner, phân loại **`LEGACY_UNATTRIBUTED`**. **Đừng** đọc *«0 lần đăng nhập mật khẩu thành công»* thành *«an toàn»*: cửa vẫn mở, bộ chặn **chưa được cài**, và log chỉ giữ được vài ngày. **Đừng** áp patch `OD-05` khi `RECOVERY_PATH` còn `NOT_VERIFIED`. **Phiên này không deploy, không xoay credential, không sửa SSH** — code nằm trên nhánh local, **chưa push**.
