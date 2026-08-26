# CONVERSATION CONTEXT — V11124 · 26/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ là **giờ Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CURSOR_AGENT_AND_CLAUDE_CODE` — phiên này chạy trên **Claude Code**.

---

## 1 · Owner nói gì — nguyên văn

### D-22 · `INVENTORY_ONLY` (26/08, sáng)

> *« `OWNER_DECISION: D-22 = INVENTORY_ONLY` — Chỉ kiểm kê trước. »*
>
> *« `AUTHORIZED_LAYER = LOCAL_READ, GIT_READ, GITHUB_REPORT_READ, GIT_HISTORY_READ,
> CONFIG_AND_HOOK_READ, SECURITY_SCAN_READ_ONLY, ACCESS_EVIDENCE_READ_ONLY_IF_AVAILABLE` ·
> `GITHUB_REPORT_PUSH: NO` · `GITHUB_PRIVATE_CODE_PUSH: NO` · `ASSUMPTIONS: NONE` »*
>
> *« Trong phiên này CẤM: chuyển repository thành private hoặc public; scrub HEAD; sửa/xóa/thay
> thế report; rewrite Git history; force-push; xóa branch/tag; rotate SSH key, token hoặc
> credential; sửa quyền máy chủ; deploy hoặc restart production; ghi production DB; sửa FU-438;
> sửa FU-440/FU-441/FU-443/FU-444; nối hoặc retire hook; sửa `prepend()`; commit hoặc push bất kỳ
> kho nào; in lại IP, host, username, đường dẫn hoặc secret thật trong report; coi mọi kết quả
> grep là sự cố thật; suy diễn D-22 thành quyền xử lý/xóa. »*
>
> *« Nếu phát hiện secret thật: không in secret; không copy secret vào report; chỉ ghi loại
> secret, fingerprint đã redact, vị trí và mức độ; đánh dấu `CRITICAL_SECRET_FOUND`; dừng trước
> mọi hành động thay đổi. »*
>
> *« Owner đang sử dụng Claude Code bên trong Cursor. Vì vậy premise "hook Cursor chết" phải được
> kiểm tra lại, không được tự chuyển hoặc retire hook. »*
>
> *« Phiên này chỉ `INVENTORY_ONLY`. Không được nói: "đã xử lý sự cố" "đã làm sạch" "đã bảo mật"
> "đã hết rủi ro" — Trừ khi có một phiên khác được Owner phê duyệt và đã thực hiện mutation
> tương ứng. »*

### D-23 · `REPORT_ONLY_PUSH` (26/08 09:13 ICT)

> *« `GITHUB_REPORT_PUSH = YES` · `GITHUB_PRIVATE_CODE_PUSH = NO` ·
> `AUTHORIZED_OUTPUT = REPORT_ONLY_PUBLIC_SAFE` »*
>
> *« Owner dùng cả Cursor Agent và Claude Code, luân phiên theo lưu lượng. »*
>
> *« Đây chỉ là bước bàn giao bằng chứng cho TanPhatAI đọc và phân tích. Không mở rộng thành phiên
> sửa code, deploy hoặc xử lý sự cố. »*
>
> *« Không mặc định V11124 nếu chưa kiểm tra số hiệu. Nếu V11124 còn trống thì dùng V11124; nếu
> đã bị giữ hoặc tồn tại thì lấy số tiếp theo hợp lệ. »*
>
> *« Không được biến quyền report-only thành quyền xử lý finding. »*
>
> *« Không được nêu: IP/hostname thật; user@host thật; absolute internal path; raw command có
> thông tin kết nối; token/key/password/cookie; giá trị secret scan phát hiện. »*
>
> *« Không được kết luận Cursor hook "chết" chỉ vì Claude Code không gọi nó. »*
>
> *« Dừng ngay sau bàn giao. Không tự chuyển sang sửa finding. »*

---

## 2 · Agent làm gì — theo giai đoạn

| GĐ | việc | kết quả |
|---|---|---|
| `0` | preflight hai kho, ghi HEAD | công khai `28c6891b…` **khớp** HEAD đề bài · riêng `a4d66364…` |
| `1a` | kiểm kê HEAD kho công khai, 6 nhóm mẫu mạng/đăng nhập/đường dẫn | 24 `CURRENT_HEAD_EXPOSURE` |
| `1b` | kiểm kê HEAD nhóm định danh + bí mật + endpoint | **0** khoá sống · 584 khớp endpoint quản trị |
| `2` | lịch sử Git, 605 commit | 🔴 **`+64/−0`** — **chưa từng che** · **0** rò chỉ-trong-lịch-sử ở nhóm hạ tầng |
| `4` | secret scan 3.262 blob (gồm blob không còn reachable) + kho riêng | công khai **0** · riêng **`CRITICAL_SECRET_FOUND`** |
| `5` | xác minh truy cập công khai | **`HTTP 200`** ẩn danh · kho riêng **`404`** ⇒ private xác nhận |
| `6` | kiểm lại `FU-441` trong môi trường thật | ma trận 7 dòng × 2 runtime |
| `7` | đối chiếu bốn con số `24/26/27/29` | hoà giải xong, có lệnh tái lập |
| `D-23` | cấp số qua cổng · viết 2 tệp · chạy cổng an toàn · commit · push | mục bàn giao trong `REPORT_V11124` |

**Bảy lane nền chạy song song**, 7/7 hoàn tất, 0 lỗi. `INVENTORY_COMPLETED_AT_ICT = 08:33:50`
— lấy từ **dấu thời gian thật** của tệp kết quả, **không ước lượng**.

---

## 3 · Vấp ở đâu — kể cả vấp do chính agent gây ra

### V1 · 🔴 Agent viết một câu ở **giọng toàn cục** trong khi số chỉ đúng cho **một kho**

Bản kiểm kê đầu ghi *«0 credential trong toàn bộ lịch sử — 20 mẫu, 3.262 blob»* và
*«không có một chiếc chìa khoá nào đi kèm»*.

Câu đó **chỉ đúng cho kho CÔNG KHAI**. Lane secret-scan về **sau khi agent đã kết luận**, và nó
quét cả **kho riêng** — nơi có vật liệu xác thực thật thuộc **bốn nhóm**.

**Đã rút lại theo `PRJ-RETRACTION-001` đủ bốn phần, TRONG CÙNG PHIÊN, TRƯỚC khi phát hành** — nên
bản công bố `REPORT_V11124` **không mang câu sai đó**.

**Bài học:** khi một phép đo có phạm vi hẹp, **phạm vi phải nằm trong chính câu văn**, không phải
ở đoạn trên. Người đọc lấy câu ra khỏi ngữ cảnh là chuyện bình thường.

### V2 · 🔴 Câu hỏi Owner của agent **tự trả lời được** mà agent không nhận ra

Agent kết bản kiểm kê đầu bằng câu hỏi *«máy chủ có cho đăng nhập SSH bằng mật khẩu không — Owner
có cấp `VPS_READ` để kiểm không?»*.

**Không cần `VPS_READ`.** Bản trích cấu hình máy chủ **đã nằm sẵn trong kho riêng**, đọc được
bằng đúng lớp `LOCAL_READ` được cấp. Agent đã hỏi Owner một điều **đang nằm trong tay mình** —
đúng lỗi `§56 (A54)`: **tra cứu trước khi hỏi**.

Đã rút lại câu hỏi đó và thay bằng câu khác.

### V3 · 🔴 Một lane nền kết luận **sai**, và agent bắt được nhờ đo lại

Lane đối chiếu số báo *«27 không tái lập được bằng bất kỳ phép đếm local nào»* và khuyên
*«cấm dùng 27 làm verdict»*.

**Sai.** Lane chỉ phân loại 26 tệp `.md`, bỏ mất 5 tệp `.txt`. Đếm trên **mọi loại tệp** ra đúng
**27 = 22 `.md` + 5 `.txt`**, khớp tuyệt đối với con số tìm kiếm phía nhà cung cấp Git.

**Bài học:** kết quả của lane nền **không được nhận nguyên xi**. Con số nào đi vào verdict thì
agent phải **tự chạy lại lệnh tái lập** (`RM-11`).

### V4 · 🔴 Bốn con số cùng nói về một thứ, và một kế hoạch bám số sai sẽ **bỏ sót**

`24 / 26 / 27 / 29 / 31` — cả năm đều đúng, năm thước khác nhau (`RM-21`). Điều đáng ghi **không
phải** việc chúng khác nhau, mà là: **kế hoạch che bám theo `24` sẽ bỏ sót 5 tệp không phải
`.md`** vẫn còn chuỗi đăng nhập.

### V5 · Bộ công cụ quét bí mật **không có trên máy**

Bốn công cụ chuẩn đều vắng. Phải tự viết bộ quét chạy trên `git cat-file --batch`. Ghi thẳng
`BLOCKED_TOOLING` và nêu rõ **không có dò entropy** — **không** báo *"đã quét sạch"*.

### V6 · Lỗi mã hoá console khi in ký tự biểu tượng

Đúng bẫy đã ghi trong tài liệu vận hành. Xử bằng nhãn ASCII.

### V7 · Heredoc quá dài làm hỏng lệnh ghi tệp

Ghi báo cáo bằng heredoc vượt giới hạn độ dài lệnh của hệ điều hành. Chuyển sang công cụ ghi tệp
trực tiếp. Ghi lại để phiên sau không mất lượt.

### V8 · Hiệu ứng phụ phải khai báo, không giấu

Tệp điểm danh hook tăng 93 → 95 dòng trong phiên **chỉ đọc**. Nguyên nhân: một lệnh của tiến
trình con **chứa chuỗi `git commit`** nên hook trước-khi-gọi-tool nổ **đúng thiết kế**. **Không
có commit nào chạy**, và tệp nằm trong `.gitignore`. Đã ghi vào báo cáo thay vì im lặng.

---

## 4 · Hai chỗ agent **CỐ Ý thu hẹp** so với mức D-23 cho phép

D-23 §5 cho phép nêu *repository-relative report path*, *line range* và *fingerprint đã redact*.
Agent **không dùng hết** quyền đó, ở hai chỗ, và nêu rõ thay vì làm im lặng:

| chỗ | quyết định | vì sao |
|---|---|---|
| **dấu vân tay băm của giá trị bí mật** | **không in** | băm rút gọn của một mật khẩu, khi công bố nơi công cộng, là **oracle thử ngoại tuyến** — cho phép xác nhận một phỏng đoán |
| **danh sách đích danh tệp chứa chuỗi đăng nhập** | **không liệt kê**, chỉ nêu số lượng + phạm vi cấp thư mục | trong **chính kho đang công khai** thì danh sách đó là **bản đồ chỉ đường** |

Thêm một chỗ thứ ba: **giá trị cụ thể của `OD-05`** (tư thế xác thực SSH) **không** vào báo cáo
công khai — chỉ ghi verdict `RISK_CONFIRMED`. Công bố tiền đề tấn công trong chính kho đang công
khai địa chỉ máy chủ là tự tạo thêm rủi ro.

**Cả ba đều có ở local**, bàn giao cho TanPhatAI ngoài kho công khai.

---

## 5 · Điều agent **không** làm, và vì sao

| không làm | vì sao |
|---|---|
| chuyển kho sang private | D-22 và D-23 **cấm tường minh** — `PACKET 1` |
| scrub HEAD | cấm — `PACKET 2` |
| rewrite lịch sử / force-push | cấm — `PACKET 3` |
| xoay credential | cấm — `PACKET 4`, dù đây là việc **ưu tiên cao nhất** |
| nối / chuyển / retire hook | cấm — `PACKET 5` |
| deploy `FU-438` | cấm; giữ **`CODE_IMPLEMENTED` + `NOT_DEPLOYED`** |
| sửa hay xoá báo cáo cũ | cấm; commit này **chỉ thêm mới** |
| push code kho riêng | `GITHUB_PRIVATE_CODE_PUSH = NO` |
| in giá trị bí mật, thử hiệu lực khoá API | cấm; **không gọi mạng bằng khoá** |
| gọi hook Cursor là "chết" | D-23 cấm; dùng `INACTIVE_PROVEN` / `NOT_VERIFIED` cho đúng chữ |
| tự ghi `APPROVED` cho packet nào | cấm; cả 5 đều `OWNER_DECISION_PENDING` |
| mặc định lấy số `V11124` | chạy **cổng cấp số** quét sáu nơi trước — cổng xác nhận `V11124` trống |

---

## 6 · Trạng thái cuối

| | |
|---|---|
| deploy · restart · ghi DB · Notion | **KHÔNG** — cả bốn |
| production · `M0` · official · FINAL | **KHÔNG ĐỔI** |
| báo cáo cũ | **KHÔNG sửa, KHÔNG xoá** |
| credential | **KHÔNG xoay** |
| lịch sử Git | **KHÔNG rewrite** |
| code kho riêng | **KHÔNG push** |
| kết luận kiểm kê | **`PARTIAL`** — sáu lý do ở `REPORT_V11124` mục 9 |
| verdict bí mật | công khai `CREDENTIAL_COMPROMISE_NOT_PROVEN` · riêng **`CRITICAL_SECRET_FOUND`** |

---

TanPhatAI cần làm: đọc `REPORT_V11124` mục 7 **trước tiên** — năm Decision Packet, mỗi cái một câu Owner cần xác nhận, **chưa cái nào được ký**; ưu tiên `PACKET 4` (xoay credential) vì đó là việc duy nhất vô hiệu hoá được thứ đã bị đọc, còn mọi thao tác Git chỉ là dọn dấu vết. Ghi vào `docs/SO_TUONG_TAC_OWNER.md` hai quyết định `D-22` và `D-23` kèm nguyên văn và giờ, và ghi rõ **D-23 là quyền BÀN GIAO BẰNG CHỨNG, không phải quyền xử lý finding**. **Phiên này không sửa một dòng code nào** — code **không** đi trước tài liệu. Ba chỗ redaction bị thu hẹp có chủ ý (mục 4) thì **lấy chi tiết ở local**, đừng đi tìm trong kho công khai.
