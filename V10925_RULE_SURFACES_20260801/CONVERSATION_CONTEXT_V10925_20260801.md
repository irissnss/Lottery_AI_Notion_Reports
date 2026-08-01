# Nguyên văn phiên 01/08/2026 — phần V10925 (dọn bộ mặt quy tắc)

> Giữ **nguyên văn** lời owner, không diễn giải lại.

---

## Owner yêu cầu (11:49)

> **".cursorrules.AGENT.md.antigravityrules.Antigravityrules.md.cursorrules và claude.md các
> file này phục vụ cho các công cụ khác nhau nhưng là quy tắc chung toàn hệ thống và đã yêu cầu
> cập nhật sync 4-5 chiều gì đó anh quên mất rồi nếu claude.md chưa có thì tạo, cái nào sao tên
> dư thừa thì clear dùm anh nha, nội dung đảm bảo nhất quán sync đa chiều"**

### Agent hiểu thành bốn việc

1. Gom các file quy tắc phục vụ nhiều công cụ về một mối, đồng bộ đa chiều
2. Tạo `claude.md` nếu chưa có — **đã tạo ở V10924**
3. **Dọn file thừa / sai tên**
4. Nội dung phải nhất quán giữa mọi mặt

---

## Ba lỗi tìm được — hai có từ TRƯỚC hôm nay

### Lỗi 1 (nặng nhất) — `playbook-first.mdc` chưa bao giờ được Cursor nạp

Ba file `.mdc` kia đều có frontmatter `alwaysApply: true`. Riêng `playbook-first.mdc` bắt đầu
thẳng bằng `# Playbook First`, **không có khối `---` nào**. Cursor **bỏ qua âm thầm** — không
báo lỗi, không cảnh báo.

**Đây chính là nguyên nhân gốc** khiến phiên sáng 01/08 bỏ qua Playbook-First Rule. Quy tắc có
tồn tại trong repo, có được nhắc trong `.cursorrules`, nhưng file `.mdc` thi hành thì chưa bao
giờ đến được agent.

### Lỗi 2 — `§53` gán cho hai quy tắc khác nhau

```
dòng  162   ## §53 — TIMEZONE VÀ BIÊN CHỐT       ký 31/07
dòng 1730   ## §53 — PLAYBOOK-FIRST HARDLOCK     ký 15/07
```

Quy tắc 31/07 lấy số đã có người dùng từ 15/07. Đụng độ này có từ 31/07.

### Lỗi 3 — `.blackboxrules` rỗng 0 byte

Từ 10/04, không tool nào dùng, chỉ xuất hiện trong ba báo cáo kiểm kê cũ. Đã xoá.

---

## Lỗi do chính agent gây sáng nay

Console PowerShell hiển thị ký tự `§` thành mojibake trông **giống chữ `A`**. Agent đọc
`## §53 — TIMEZONE VÀ BIÊN CHỐT` thành `## A53`, rồi đếm tiếp và đặt hai quy tắc mới hôm nay là
`A54` và `A55` — **không quét xem số nào đã dùng**.

Hậu quả: `§54` khi đó đã thuộc về quy tắc `/choi output/capital + deadline lock` ký 27/07 →
**hai quy tắc khác nhau cùng một số**.

---

## Đánh số lại theo đúng thứ tự ngày ký

| Số | Quy tắc | Ngày ký | Trước đó |
|---|---|---|---|
| `§53` | PLAYBOOK-FIRST HARDLOCK | 15/07 | giữ (giành số trước) |
| `§54` | `/choi` output/capital + deadline | 27/07 | giữ |
| `§55` | TIMEZONE VÀ BIÊN CHỐT | 31/07 | **trùng `§53`** |
| `§56` | TRA CỨU TRƯỚC KHI HỎI *(A54)* | 01/08 10:41 | **trùng `§54`** |
| `§57` | BÁO CÁO CÔNG KHAI; NOTION CHỈ ĐỌC *(A55)* | 01/08 11:04 | `§55` |

Giữ bí danh `(A54)` / `(A55)` vì hơn **300 tham chiếu** đã ghi trong CHANGELOG, SSOT,
DECISION_LOG, GOVERNANCE_LEDGER, sổ quyết định và 4 báo cáo công khai đã push.

---

## Về `.AGENT.md` — tên không chuẩn nhưng không đổi được

Tên chuẩn của giới là `AGENTS.md` (số nhiều, không dấu chấm đầu). `.AGENT.md` có dấu chấm đầu
nên **không công cụ nào tự nạp** — nó chỉ được đọc khi agent được chỉ dẫn đọc.

Nhưng nó bị nhắc **353 lần** trong repo. Đổi tên là gãy hàng loạt. Nên giữ nguyên, bù bằng cách
tạo `AGENTS.md` riêng — **sinh tự động từ `CLAUDE.md`** để hai bản không bao giờ lệch.

---

## Bộ sáu mặt sau khi dọn

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

## Ba chỗ vấp trong lúc làm

1. **PowerShell `-match 'A53'` trả `False`** dù chuỗi có trong file — suýt kết luận sai. Phải
   dùng Python `str.count()` hoặc `rg`.
2. **Biểu thức kiểm trùng bắt cả `§53A` thành `§53`** → báo trùng oan ở `§51`. Đã siết bằng
   `(?=[\s(—-])`.
3. **Đổi số làm mệnh đề trong sổ quyết định hết khớp** — sổ tự báo `TRÔI 3/6` vì mệnh đề cũ dò
   chuỗi `"A55 — BÁO CÁO…"` nay đã thành `"§57 (A55) — BÁO CÁO…"`. Đây là bằng chứng cơ chế sổ
   quyết định hoạt động đúng: nó bắt được cả thay đổi do chính agent tạo ra.
