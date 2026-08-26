# CONVERSATION CONTEXT — V11125 · 26/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ là **giờ Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CURSOR_AGENT_AND_CLAUDE_CODE` — phiên này chạy trên **Claude Code**.

---

## 1 · Owner nói gì — nguyên văn

### D-24 · `KEEP_PUBLIC_CURRENT` (26/08)

> *« `D-24 = KEEP_PUBLIC_CURRENT`: GitHub Report tiếp tục public; không đổi visibility lúc này. »*
>
> *« `D-24` KHÔNG có nghĩa: kho đã an toàn; exposure đã đóng; được xoay credential; được scrub
> HEAD; được rewrite history; được sửa/cài/migrate/retire hook; được deploy `FU-438`; được sửa
> production. »*
>
> *« Owner dùng cả Cursor Agent và Claude Code. Owner luân phiên hai Agent theo lưu lượng.
> TanPhatAI quản lý Notion, hợp nhất evidence và trình Decision Gate. Agent IDE quản lý
> Local/Git/Code/DB copy/Test/VPS trong đúng lớp được cấp. Owner chỉ quyết khi packet đã đủ hiểu. »*

**Lớp được cấp** *(trích)*: `LOCAL_READ` · `PRIVATE_REPO_READ` · `PUBLIC_REPORT_REPO_READ` ·
`GIT_HEAD_READ` · `GIT_HISTORY_READ` · `CONFIG_AND_HOOK_READ` · **`VPS_CONFIG_READ_ONLY`** ·
`SECURITY_SCAN_READ_ONLY` · `ISOLATED_TEMP_COPY_WRITE_AND_TEST` ·
`LOCAL_EVIDENCE_ARTIFACT_WRITE` · `GITHUB_REPORT_PUSH = YES` *(đúng một report)* ·
`GITHUB_PRIVATE_CODE_PUSH = NO` · `NOTION_WRITE = NO`.

**Cấm** *(trích)*:

> *« thử đăng nhập bằng credential; gọi API nhà cung cấp bằng khóa phát hiện được; in secret ra
> stdout, report hoặc Conversation Context; thay credential; sửa authorized_keys; sửa SSH
> configuration; restart service; ghi production DB; sửa code production; push private code;
> scrub; force-push; rewrite history; đổi visibility; sửa hoặc xóa report cũ; cài/migrate/retire
> hook trong cấu hình thật; deploy `FU-438`; tự ghi `APPROVED` cho bất kỳ packet nào. »*

Và hai câu định hình cách làm việc của phiên:

> *« Không được để số "4 hoặc 5" treo mà không giải thích. »*
>
> *« Mỗi việc thật sự cần Owner quyết phải có đúng một câu hỏi, nhưng **không hỏi Owner nếu Agent
> còn tự điều tra được**. »*

---

## 2 · Agent làm gì — theo mục tiêu

| MT | việc | kết quả |
|---|---|---|
| `0` | preflight: đo lại HEAD, cổng cấp số, lease | `V11125` trống · hai commit `D-23` xác nhận là tổ tiên HEAD |
| `1` | đối chiếu `V11124` | **`TOTAL = 31` xác nhận** · **«24» bị BÁC** · 4 chỗ rút lại |
| `2a` | quét `PRIVATE_HISTORY` *(đóng `NC-03`)* | **10.615/10.743 blob = 98 %** |
| `2b` | chốt số giá trị mật khẩu | **7 giá trị** — 3 `CONFIRMED` · 1 `FALSE_POSITIVE` · 3 `NOT_VERIFIED` |
| `2c` | đọc cấu hình máy chủ | 🔴 **`BLOCKED_PERMISSION`** |
| `3` | runbook xoay, 12 bước | **`ROTATION_PACKET_PARTIAL`** |
| `4` | chứng minh hook trên fixture cô lập | **5/5 ĐẠT** · cấu hình thật **0 thay đổi** |
| `5` | cổng an toàn + phát hành | mục bàn giao trong `REPORT_V11125` |

---

## 3 · Vấp ở đâu — kể cả vấp do chính agent gây ra

### V1 · 🔴 Một phép đo của chính agent đã **nói dối**, và suýt vào kết luận

Ở `V11124`, «phương pháp độc lập thứ hai» báo **`0 commit`** cho nhóm mật khẩu. Nếu tin, kết luận
sẽ là *«mật khẩu chưa bao giờ vào lịch sử»* — **ngược hẳn sự thật**.

Thử chặn theo `RM-15` phơi ra ngay: đối chứng *«chuỗi chắc chắn CÓ»* → **585 commit** *(công cụ
chạy tốt)*; đối chứng *«chắc chắn KHÔNG»* → `0`. Vậy `0` của mẫu đã dùng là **lỗi cú pháp** —
công cụ dùng regex POSIX, không hiểu cú pháp không-phân-biệt-hoa-thường. Viết lại đúng cú pháp:
**24 commit**.

**Bài học đưa vào luật:** mọi phép «đếm bằng công cụ tìm kiếm» **bắt buộc kèm hai đối chứng**.
Không có đối chứng thì `0` là **vô nghĩa**, không phải bằng chứng.

### V2 · 🔴 Con số phụ thuộc **biểu thức tìm kiếm**, và agent đã công bố một con số như thể nó tuyệt đối

Ba lần quét cho **ba tập khác nhau**: 1 giá trị · 4 giá trị · 7 giá trị — chỉ vì **bộ lọc khác
nhau**. `V11124` công bố **«4»** như một sự thật.

Cách xử: lấy **hợp của mọi mẫu**, dedupe **theo giá trị**, rồi cho **từng giá trị một verdict**.
Ra **7**. Giờ không còn số nào treo.

### V3 · 🔴 Fixture cô lập suýt tạo ra một kết luận SAI về production

Chạy cổng quản trị **trong fixture** thì nó trả `allow` cho cả lệnh triển khai ⇒ đọc vội sẽ
thành *«cổng quản trị hỏng»*.

**Sai.** Fixture nằm ở thư mục tạm nên cổng giải đường dẫn repo về thư mục fixture, **không thấy
tài liệu thật**. Chạy **chính script thật** từ vị trí thật thì nó trả **`ask`** — **bắt đúng**.

Đúng `RM-13`: **nguồn sai thì mọi kết luận sai**. Suýt báo một cổng đang hoạt động là hỏng.

### V4 · 🔴 Agent đoán tên biến thay vì tra

Bộ đọc cấu hình máy chủ tìm biến tên `HOST`/`VPS_HOST` — **không có**. Tên thật là `VPS_IP`
*(116 tệp)*. Đúng `RM-10`: **cấm kết luận theo tên đoán**. Phải quét tên biến thật rồi mới viết.

### V5 · 🔴 `VPS_CONFIG_READ_ONLY` Owner đã cấp — **môi trường chặn**

Đã chuẩn bị đủ: đường vào hợp lệ *(khoá SSH của owner, **không** dùng mật khẩu đã phát hiện)*,
phép so **một chiều** *(băm phía máy chủ, so phía local — không gửi bí mật qua mạng)*, 17 lệnh
**chỉ đọc**.

Lớp phân quyền của công cụ **từ chối lệnh kết nối ra ngoài**. **Agent DỪNG, không đi vòng** —
hướng dẫn nói rõ: nếu năng lực này là thiết yếu thì **dừng và trình bày cho Owner quyết**.

Hệ quả: **mọi** trạng thái hiệu lực credential đứng ở `NOT_VERIFIED`, runbook chỉ đạt `PARTIAL`.
Đây là **khoảng trống bằng chứng chính** của phiên.

### V6 · Một lệnh sửa-script-bằng-script bị chặn

Cách xử: dùng công cụ sửa tệp trực tiếp thay vì script sinh script. **Không tìm cách lách.**

---

## 4 · Điều agent **không** làm, và vì sao

| không làm | vì sao |
|---|---|
| thử đăng nhập bằng `SC-04` | 🔴 cấm tường minh — dùng khoá SSH của owner, và **chỉ** khi được phép |
| gọi nhà cung cấp bằng `SC-03` | cấm — **không** kiểm hiệu lực khoá API |
| gửi bí mật qua mạng | thiết kế phép so **một chiều** ngay từ đầu |
| in giá trị / dấu vân tay bí mật | `D-24` §VII cấm; kho vẫn public |
| sửa `authorized_keys` / cấu hình SSH / restart | cấm |
| cài, chuyển, gỡ hook trong cấu hình thật | cấm — **chỉ** làm trên fixture cô lập |
| sửa `REPORT_V11124` | cấm — đính chính bằng **phụ lục mới** theo `PRJ-RETRACTION-001` |
| ghi `ROTATION_APPROVED` / `ROTATION_COMPLETED` | cấm — kết quả là **`ROTATION_PACKET_PARTIAL`** |
| đề xuất migrate/retire hook | attendance **chưa chứng minh** ⇒ `RM-15` cấm |
| hỏi Owner về `SC-06`/`SC-09`/`SC-10` | Owner dặn **không hỏi nếu Agent còn tự điều tra được** |
| đi vòng lớp phân quyền | trình bày để Owner quyết, không lách |

---

## 5 · Trạng thái cuối

| | |
|---|---|
| production · DB · Notion · visibility | **KHÔNG ĐỔI** — cả bốn |
| credential | **KHÔNG xoay** |
| hook runtime | **KHÔNG chạm** — `git status .cursor/` = 0 dòng |
| `FU-438` | **KHÔNG deploy** |
| báo cáo cũ | **KHÔNG sửa, KHÔNG xoá** |
| kho riêng | HEAD y nguyên · ahead = 0 |
| runbook xoay | **`ROTATION_PACKET_PARTIAL`** |
| khoảng trống chính | 🔴 **`VPS_RUNTIME` = `BLOCKED_PERMISSION`** |

---

TanPhatAI cần làm: ghi nhận **bốn đính chính** của `REPORT_V11125` mục 2 vào sổ — `TOTAL = 31`, `PUBLIC_HEAD = 23` *(không phải 24)*, **7** giá trị mật khẩu *(không phải 4)*, và câu *«0 credential»* **đã bị rút lại**; thêm vào `docs/FOLLOW_UP_TRACKER.md` một mục cho **ba ứng viên `NOT_VERIFIED`** *(`SC-06` `SC-09` `SC-10`)* — đây là **việc của Agent**, chưa đến lượt Owner. Ghi vào `docs/SO_TUONG_TAC_OWNER.md` rằng `D-24` là **quyền CHUẨN BỊ BẰNG CHỨNG**, và rằng `VPS_CONFIG_READ_ONLY` **chưa thi hành được** vì môi trường chặn. **Đừng** đọc *«cổng Cursor mất hiệu lực»* thành *«cổng Cursor vô dụng»* — đo được nó **bắt đúng** lệnh triển khai, nên giá trị đang mất **lớn hơn** báo cáo trước mô tả. **Phiên này không sửa code production, không chạm hook thật.**
