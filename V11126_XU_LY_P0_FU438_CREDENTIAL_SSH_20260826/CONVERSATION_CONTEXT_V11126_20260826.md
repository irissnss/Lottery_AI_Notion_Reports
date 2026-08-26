# CONVERSATION CONTEXT — V11126 · 26/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ là **giờ Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`.

---

## 1 · Owner nói gì — nguyên văn

> *« Xử lý các vấn đề P0 thật. Không để việc Owner chưa có máy thứ hai làm treo `FU-438`,
> credential remediation hoặc code fix. »*

**Sự thật vận hành Owner khoá:**

> *« Owner chỉ code/fix trên một máy hiện tại, chưa đổi máy. Trạng thái:
> `SINGLE_DEVICE_OPERATION`. »*
>
> *« Owner không rõ và không giữ hai SSH key còn lại trong `authorized_keys`. Hai key đó phải
> được ghi `UNATTRIBUTED_AUTHORIZED_KEYS`. Chúng không phải backup của Owner. »*
>
> *« Cấm: suy hai key đó là key cũ của Owner; thử đăng nhập bằng chúng; in raw key hoặc
> fingerprint; tự ý xóa chúng. »*
>
> *« Một session khác dùng cùng owner key chỉ chứng minh `PRIMARY_PATH_REPROVEN`. Không được gọi
> đó là backup độc lập. »*
>
> *« Không bắt Owner phải có máy thứ hai mới được tiếp tục các phần không gây lockout. »*

**Thứ tự ưu tiên — cấm đảo:** `P0-A` FU-438 → `P0-B` credential → `P0-C` SSH/access.

> *« Không giữ ngoại lệ public `/user-view` nếu policy Owner không đổi. »*
>
> *« Không deploy production nếu chưa có chữ ký deploy rõ ràng. Không diễn giải câu "xử lý vấn đề
> chính" thành blanket deploy approval. »*
>
> *« Cấm coi 157 tệp là 157 active consumer. »*
>
> *« Không kết luận xâm nhập chỉ vì không nhận diện được key. Không coi key là an toàn chỉ vì log
> chưa thấy sử dụng. »*
>
> *« Không sinh key thứ hai trên cùng máy rồi gọi là independent backup. »*
>
> *« Không yêu cầu Owner chạy lệnh kỹ thuật thường ngày. »*

---

## 2 · Agent làm gì

| GĐ | việc | kết quả |
|---|---|---|
| `A-0` | đọc chính sách `D-13` từ sổ `FU-438` | Owner đã ký *«treo toàn bộ view người dùng»* từ 06–08/06 |
| `A-1` | **kiểm caller trước khi khoá** | cron **0** · frontend **9 gọi thật** (3 chú thích + 2 mock loại ra) |
| `A-2` | vá `/api/predictions` | `+31/−9` dòng · `py_compile` OK |
| `A-3` | route matrix | **211 route**; 6 endpoint đều `CONG_ADMIN`; còn **1** route lộ |
| `A-4` | thử chặn | **56/56 ĐẠT** — 401 / 403 / 200 |
| `B-1` | phân loại consumer | `SC-03` **0** · `SC-04` **34** (không phải 157) |
| `B-2` | lớp nguồn bí mật | **16/16 ĐẠT** |
| `C-1` | truy nguồn hai khoá lạ | `LEGACY_UNATTRIBUTED` × 2 |
| `C-2` | log xác thực | **293.748** thất bại · **0** thành công bằng mật khẩu |
| `C-3` | đường phục hồi | serial console **bật** · 2 mục recovery · vẫn `NOT_VERIFIED` |
| `C-4` | patch `OD-05` | **10/10**, **chưa áp** |

---

## 3 · Vấp ở đâu — kể cả vấp do chính agent gây ra

### V1 · 🔴 Agent báo **14 route nhạy cảm**, xác minh còn **1**

Bộ quét đầu gắn nhãn *«nhạy cảm»* theo **từ khoá** trong thân hàm — nên bắt cả những route chỉ
**nhắc** thuật ngữ mà **không phát ra số**.

Xác minh bằng cách hỏi đúng câu: *route này có trả **trường chứa số** không?* → **1/14**.

**Nếu công bố con số 14** thì Owner sẽ tưởng phải khoá 14 route, và kế hoạch khoá sẽ **rộng gấp
14 lần** thực tế — nhiều khả năng làm vỡ caller nội bộ. Đúng bài học `RM-09`: **cấm đếm chuỗi
thô, phải phân loại**.

### V2 · 🔴 Con số «157 tệp» đo trên **thước khác**

`157` đo trên **cây triển khai của máy chủ**; local là **40**, và **34** mới là consumer thật.
Chênh do máy chủ còn giữ bản sao.

Hậu quả nếu bỏ qua: kế hoạch xoay ước **157 điểm sửa** thay vì **34**, và quan trọng hơn — sẽ
tưởng phải **khởi động lại dịch vụ**, trong khi `SC-04` **không có consumer runtime nào**.

### V3 · 🔴 Một phép thử của agent **sai luật**, agent sửa phép thử chứ không nới lỏng

Bản thử nguồn bí mật đặt luật *«module không được nhắc TÊN biến bí mật»* rồi báo HỎNG vì tài liệu
có chữ `VPS_PASS`.

**Luật đó sai:** tên biến **không phải bí mật** — nó đã nằm công khai trong 40 tệp. Yêu cầu thật
của đề bài là **không log GIÁ TRỊ**. Đã sửa phép thử về đúng thứ phải kiểm, và **ghi rõ trong mã**
rằng đây là sửa luật sai chứ không phải hạ chuẩn để cho qua.

### V4 · 🔴 Suýt đếm một dòng **chú thích** thành lời gọi

Một trang frontend có dòng nhắc `/api/predictions`, nhưng đọc kỹ thì đó là **chú thích** ghi rằng
nó *từng* gọi — bản `V10877` đã gỡ. Nếu tính, agent sẽ báo nhầm rằng khoá endpoint sẽ phá thêm
một trang.

### V5 · 🔴 Sửa tệp cấu hình chính sẽ **vô ích**, và agent suýt đề xuất đúng thế

Phản xạ đầu là *«sửa `PasswordAuthentication` trong tệp chính»*. **Sai** — `sshd` lấy **giá trị
đọc được đầu tiên**, mà chỉ thị `Include` nằm ở dòng **12**, nên tệp drop-in của `cloud-init`
thắng mọi thiết lập về sau.

Phải đặt drop-in **sắp trước** theo thứ tự chữ cái. Đã mô phỏng lại luật *«giá trị đầu tiên
thắng»* để chứng minh bản vá đổi đúng hướng, thay vì tin vào suy đoán.

### V6 · Chọn `prohibit-password` chứ **không** `no`

`PermitRootLogin no` sẽ chặn **cả** đường vào bằng khoá đang dùng ⇒ **tự khoá mình ra ngoài** —
đặc biệt nguy hiểm trong chế độ **một máy**. `prohibit-password` tắt mật khẩu mà **giữ khoá**.

---

## 4 · Điều agent **không** làm, và vì sao

| không làm | vì sao |
|---|---|
| deploy `FU-438` | *«không diễn giải câu xử lý vấn đề chính thành blanket deploy approval»* |
| khoá `/api/slice-recommendation` | sổ `FU-438`: phần cần Owner ký là **cách khoá** để không vỡ caller |
| migrate 34 script | chờ cổng thay đổi riêng |
| xoay `SC-03` / `SC-04` | chờ cổng thay đổi riêng |
| áp patch `OD-05` | 🔴 `RECOVERY_PATH` còn `NOT_VERIFIED` — tắt mật khẩu là tự khoá mình ra |
| cài bộ chặn dò mật khẩu | cùng cổng với trên; và cần liệt địa chỉ Owner vào danh sách bỏ qua trước |
| xoá / sửa hai khoá lạ | cấm tường minh |
| thử đăng nhập bằng hai khoá lạ | cấm tường minh |
| sinh khoá thứ hai trên cùng máy | *«không gọi là independent backup»* — cùng máy hỏng thì mất cả hai |
| push code kho riêng | `GITHUB_PRIVATE_CODE_PUSH = NO` — commit **chỉ trên nhánh local** |
| in raw key / vân tay / giá trị credential | cấm tường minh |

---

## 5 · Trạng thái cuối

| | |
|---|---|
| production · DB · SSH · hook · visibility | **KHÔNG ĐỔI** — cả năm |
| credential | **KHÔNG xoay** |
| hai khoá lạ | **KHÔNG đụng** |
| code | nhánh local `fu438/admin-only-p0a` · **chưa push** |
| `FU-438` | **`CODED_NOT_DEPLOYED`** · thử 56/56 |
| nguồn bí mật | **`CODED_NOT_DEPLOYED`** · thử 16/16 |
| patch `OD-05` | **soạn xong, chưa áp** · thử 10/10 |
| chặn chính | `RECOVERY_PATH = NOT_VERIFIED` |

---

TanPhatAI cần làm: cập nhật `FU-438` thành **`CODED_NOT_DEPLOYED`** (thử 56/56) và mở mục mới cho **`/api/slice-recommendation`** — route duy nhất còn lộ trường chứa số. Ghi ba đính chính: `SC-04` **40 tệp local / 34 consumer thật** (không phải 157) · `SC-03` **0 consumer hoạt động** · *«14 route nhạy cảm»* thật ra **1**. Ghi trạng thái **`SINGLE_DEVICE_OPERATION`** và hai khoá **`UNATTRIBUTED_AUTHORIZED_KEYS`** — phân loại **`LEGACY_UNATTRIBUTED`**, **không phải** backup của Owner. **Đừng** đọc *«0 đăng nhập mật khẩu thành công»* thành *«an toàn»* — bộ chặn **chưa được cài** và log chỉ giữ vài ngày. **Đừng** áp patch `OD-05` khi `RECOVERY_PATH` còn `NOT_VERIFIED`.
