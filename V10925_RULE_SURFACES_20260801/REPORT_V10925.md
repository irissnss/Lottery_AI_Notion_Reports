# V10925 — Sáu mặt quy tắc: dọn file chết, sửa lỗ không tự nạp, đánh lại số mục trùng

**Ngày:** 01/08/2026 · **Trạng thái:** sáu mặt đồng bộ · mọi `.mdc` tự nạp · không còn số mục trùng

---

## 1. Tóm tắt

Owner yêu cầu gom các file quy tắc phục vụ nhiều công cụ khác nhau về một mối, tạo `claude.md`
nếu chưa có, dọn file thừa, đảm bảo nội dung nhất quán.

Kiểm ra **ba lỗi thật**, hai trong đó có từ trước hôm nay:

| # | Lỗi | Mức độ |
|---|---|---|
| 1 | `playbook-first.mdc` **thiếu hẳn frontmatter** → Cursor **chưa bao giờ tự nạp** quy tắc Playbook-First | **nặng** — đây là nguyên nhân gốc khiến sáng nay agent bỏ qua playbook |
| 2 | `§53` gán cho **hai** quy tắc khác nhau (Playbook-first 15/07 và Timezone 31/07) | nặng — có từ 31/07 |
| 3 | `.blackboxrules` rỗng **0 byte**, không tool nào dùng | nhẹ |

Và **một lỗi do chính agent gây sáng nay**: gán `§54` cho quy tắc mới trong khi `§54` đã thuộc
về quy tắc `/choi` ký 27/07.

Kết quả: bộ **sáu mặt** đồng bộ, `AGENTS.md` sinh tự động từ `CLAUDE.md`, số mục đánh lại theo
đúng thứ tự ngày ký, cả 4 file `.mdc` đều được tự nạp.

---

## 2. Owner yêu cầu gì (nguyên văn)

**01/08 11:49:**

> *".cursorrules.AGENT.md.antigravityrules.Antigravityrules.md.cursorrules và claude.md các file
> này phục vụ cho các công cụ khác nhau nhưng là quy tắc chung toàn hệ thống và đã yêu cầu cập
> nhật sync 4-5 chiều gì đó anh quên mất rồi nếu claude.md chưa có thì tạo, cái nào sao tên dư
> thừa thì clear dùm anh nha, nội dung đảm bảo nhất quán sync đa chiều"*

---

## 3. Đào bới / phát hiện

### 3.1 File nào thực sự được công cụ TỰ NẠP

| File | Công cụ | Tự nạp? |
|---|---|---|
| `.cursorrules` | Cursor (định dạng cũ) | **CÓ** |
| `.cursor/rules/*.mdc` | Cursor (định dạng mới) | **CÓ** — nếu có `alwaysApply: true` |
| `CLAUDE.md` | Claude Code | **CÓ** |
| `AGENTS.md` | chuẩn chung nhiều công cụ | **CÓ** |
| `.antigravityrules` | Antigravity | có (tên chuẩn) |
| `.Antigravityrules.md` · `.AGENT.md` | — | **KHÔNG** — đọc theo chỉ dẫn |

### 3.2 Lỗi 1 — `playbook-first.mdc` chưa bao giờ được nạp

```
active-roadmap-precedence.mdc            frontmatter=có · alwaysApply=true   ✓
governance-traceability-automation.mdc   frontmatter=có · alwaysApply=true   ✓
live-data-integrity.mdc                  frontmatter=có · alwaysApply=true   ✓
playbook-first.mdc                       frontmatter=KHÔNG                   ✗
```

File bắt đầu thẳng bằng `# Playbook First`, không có khối `---` frontmatter. **Cursor bỏ qua âm
thầm** — không báo lỗi, không cảnh báo.

Đây chính là **nguyên nhân gốc** khiến phiên sáng 01/08 bỏ qua Playbook-First Rule: quy tắc có
tồn tại trong repo nhưng chưa bao giờ đến được agent.

### 3.3 Lỗi 2 — `§53` gán cho hai quy tắc

```
dòng  162   ## §53 — TIMEZONE VÀ BIÊN CHỐT       ký 31/07
dòng 1730   ## §53 — PLAYBOOK-FIRST HARDLOCK     ký 15/07
```

Quy tắc 31/07 lấy số đã có người dùng từ 15/07.

### 3.4 Lỗi do agent gây sáng nay

Console PowerShell hiển thị ký tự `§` thành mojibake trông giống chữ `A`. Agent đọc
`## §53 — TIMEZONE` thành `## A53`, rồi đếm tiếp đặt hai quy tắc mới là `A54` và `A55` — **không
quét xem số nào đã dùng**. `§54` khi đó đã thuộc về quy tắc `/choi` ký 27/07.

### 3.5 `.AGENT.md` — tên không chuẩn nhưng không đổi được

Tên chuẩn của giới là `AGENTS.md` (số nhiều, không dấu chấm đầu). `.AGENT.md` có dấu chấm đầu
nên **không công cụ nào tự nạp**. Nhưng nó bị nhắc tới **353 lần** trong repo → đổi tên là gãy
hàng loạt. Giữ nguyên, và bù bằng cách tạo `AGENTS.md` riêng.

---

## 4. Hướng xử lý và vì sao chọn

| Phương án | Vì sao chọn / loại |
|---|---|
| **Sinh `AGENTS.md` TỪ `CLAUDE.md` bằng script** | **ĐÃ CHỌN.** Hai file cùng vai trò; viết tay hai bản là chắc chắn lệch sau vài phiên. Sinh một bản từ bản kia thì **không thể lệch** |
| Viết tay `AGENTS.md` riêng | Loại: hai bản sẽ trôi khỏi nhau |
| Đổi tên `.AGENT.md` → `AGENTS.md` | Loại: 353 tham chiếu sẽ gãy |
| **Đánh số lại theo ngày ký** | **ĐÃ CHỌN.** Ai giành số trước thì giữ; mục sau dời đi |
| Để nguyên đụng độ, chỉ ghi chú | Loại: hai quy tắc cùng số thì tham chiếu chéo trỏ nhầm |
| Đổi thẳng `A54`→`§56`, bỏ bí danh | Loại: hơn 300 tham chiếu đã ghi trong changelog, SSOT, decision log, sổ quyết định, 4 báo cáo đã push |
| **Giữ bí danh `(A54)`/`(A55)`** | **ĐÃ CHỌN.** Tra được bằng cả hai dạng |
| Xoá `.blackboxrules` | **ĐÃ CHỌN.** 0 byte, chỉ xuất hiện trong báo cáo kiểm kê cũ, không tool nào dùng |

---

## 5. Đã làm gì

### Đánh số lại theo đúng thứ tự ngày ký

| Số | Quy tắc | Ngày ký | Trước đó |
|---|---|---|---|
| `§53` | PLAYBOOK-FIRST HARDLOCK | 15/07 | giữ nguyên (giành số trước) |
| `§54` | `/choi` output/capital + deadline lock | 27/07 | giữ nguyên |
| `§55` | TIMEZONE VÀ BIÊN CHỐT | 31/07 | **trùng `§53`** |
| `§56` | TRA CỨU TRƯỚC KHI HỎI *(bí danh A54)* | 01/08 10:41 | **trùng `§54`** |
| `§57` | BÁO CÁO CÔNG KHAI; NOTION CHỈ ĐỌC *(bí danh A55)* | 01/08 11:04 | `§55` |

Đổi từ số **lớn xuống nhỏ** để bước sau không đè bước trước.

### Thay đổi từng file

| File | Thay đổi |
|---|---|
| `.cursor/rules/playbook-first.mdc` | **Thêm frontmatter** `alwaysApply: true` — giờ mới thực sự được nạp |
| `.blackboxrules` | **XOÁ** (0 byte, chết) |
| `AGENTS.md` | **Mới** — sinh tự động từ `CLAUDE.md`, 11.666 ký tự |
| `.antigravityrules` | Viết lại: liệt kê đủ sáu mặt + bảng đánh số + ba lệnh bắt buộc |
| `.Antigravityrules.md` | +641 ký tự — đánh số lại + ghi chú đụng độ + thêm `AGENTS.md` |
| `.AGENT.md` | +341 ký tự |
| `.cursorrules` | +367 ký tự |
| `CLAUDE.md` | +460 ký tự |
| `_v10925_rule_sync_check.py` | **Mới** — sinh `AGENTS.md` + kiểm sáu mặt + kiểm `.mdc` tự nạp + tìm file chết |
| `docs/OWNER_DECISION_LEDGER.json` | Thêm `OD-20260801-H`, 5 mệnh đề |

### Bộ sáu mặt sau khi dọn

```
.Antigravityrules.md   bản đầy đủ canonical (98 KB)     đọc theo chỉ dẫn
.antigravityrules      file trỏ đường                   Antigravity tự tìm
.AGENT.md              bản mirror (353 tham chiếu)      đọc theo chỉ dẫn
.cursorrules           bề mặt Cursor                    TỰ NẠP
CLAUDE.md              bề mặt Claude Code               TỰ NẠP  ← NGUỒN
AGENTS.md              chuẩn chung nhiều công cụ        TỰ NẠP  ← sinh ra
.cursor/rules/*.mdc    4 file, đều alwaysApply: true    TỰ NẠP
```

---

## 6. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| Sáu mặt có đủ §55 / §56 / §57 + nhắc `CLAUDE.md` + `AGENTS.md` | **6/6 đủ** |
| Bốn `.mdc` có `alwaysApply: true` | **4/4 tự nạp** |
| Số mục trùng nhau | **0** — trước có 2 (`§53`, `§54`) |
| File quy tắc chết ở gốc repo | **0** |
| Sổ quyết định | **12 quyết định · 0 mục trôi** |
| Ghi file | script **từ chối ghi nếu ngắn đi**; `AGENTS.md` từ chối nếu ngắn hơn 60% bản cũ |

Sổ quyết định còn **tự bắt được** việc đổi số: mệnh đề cũ dò chuỗi `"A55 — BÁO CÁO…"` không còn
khớp sau khi tiêu đề đổi thành `"§57 (A55) — BÁO CÁO…"` → báo `TRÔI 3/6`. Đã sửa mệnh đề. Đây là
bằng chứng cơ chế hoạt động đúng.

---

## 7. Vướng vấp

| # | Vấp | Hậu quả nếu bỏ qua |
|---|---|---|
| 1 | **Console hiện `§` thành mojibake giống chữ `A`** | Agent đọc `§53` thành `A53`, đặt tiếp `A54`/`A55` → **đụng độ với `§54` đã có**. Đây là gốc của cả chuỗi lỗi hôm nay |
| 2 | Đặt số mục mà **không quét xem số nào đã dùng** | Hai quy tắc cùng số; tham chiếu chéo trỏ nhầm |
| 3 | `playbook-first.mdc` thiếu frontmatter, Cursor **bỏ qua âm thầm** | Quy tắc có trong repo nhưng chưa bao giờ tới được agent — không báo lỗi gì |
| 4 | PowerShell `-match 'A53'` trả `False` dù chuỗi có trong file | Suýt kết luận sai. Phải dùng Python `str.count()` hoặc `rg` |
| 5 | Biểu thức kiểm trùng bắt cả `§53A` thành `§53` | Báo trùng oan ở `§51`. Đã siết bằng `(?=[\s(—-])` |
| 6 | Đổi số làm **mệnh đề trong sổ quyết định hết khớp** | Nếu không có sổ thì không ai biết; sổ đã tự bắt và báo `TRÔI` |

---

## 8. Gỡ về

Phiên này **chỉ đổi tài liệu quy tắc**, không đụng code chạy, không deploy, không đụng database.

```
git revert <commit V10925>
```

Gỡ lẻ: khôi phục `.blackboxrules` (file rỗng) · xoá `AGENTS.md` · bỏ frontmatter khỏi
`playbook-first.mdc` · hoàn nguyên số mục về `§53`/`§54`/`§55`. **Mất khoảng 1 phút.**

Lưu ý: gỡ về sẽ **trả lại** lỗi `playbook-first.mdc` không được nạp và hai đụng độ số mục.

---

## 9. Theo dõi tiếp

| Mã | Việc | Ngưỡng | Hạn |
|---|---|---|---|
| **FU-190** | Chạy `_v10925_rule_sync_check.py` mỗi khi sửa bất kỳ mặt quy tắc nào | phải đạt: 6/6 mặt đủ · 4/4 `.mdc` tự nạp · 0 số mục trùng · 0 file chết | liên tục |
| **FU-190b** | Trước khi đặt số mục mới: **quét số đã dùng**. Quy ước là `§NN`, không phải `A-NN` | đã ghi bảng đánh số vào `.antigravityrules` | xong |
| FU-186 | Cửa sổ đóng băng đường ra số | không đổi gì tới 08/08 | 08/08 |
| FU-189 | Xác minh 02/08: 19 experiment của lane nghỉ phải thực sự vắng | journal 0 lỗi | 02/08 |

Nguyên văn lời owner: `CONVERSATION_CONTEXT_V10925_20260801.md` cùng thư mục.
