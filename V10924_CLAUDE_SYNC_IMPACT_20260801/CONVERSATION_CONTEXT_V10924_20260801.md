# Nguyên văn phiên 01/08/2026 — phần V10922 / V10923 / V10924

> Giữ **nguyên văn** lời owner, không diễn giải lại.

---

## Owner nêu ba việc (11:31)

> **"Cập nhật các quy tắc anh vừa trao đổi với em vào claude.md đồng bộ nhất quán với các file
> liên quan, tiếp đi em, chắc chăn là do công cụ của cursos làm lỗi chứ gì nữa hiện tại tự nhiên
> sinh ra 3 tab cùng 1 công việc và đang treo cả chỉ có tab anh đang tương tác với em là hoàn
> thành đó em. Kiểm tra lại đi, chắc chắn đang lỗi treo chỗ nào rồi,**
>
> **Đồng thời em đã cát giảm thay thay thế hết chưa? đã thực sự kiểm soát, có tư duy có logic
> nhất quán chưa hay là thích là cắt bỏ mà không thèm soi tới sự ảnh hưởng tương quan, tương
> thích, liên hệ mật thiết của nhau đó em."**

Owner kèm 3 ảnh chụp màn hình Cursor cho thấy ba tab cùng tên *"Number pattern analysis"*, tất
cả dừng ở trạng thái *"Asking questions"*.

---

## Việc 1 — chuyện treo

**Kiểm được gì:**

| Nơi | Kết quả |
|---|---|
| Hai terminal của agent (`1.txt`, `2.txt`) | **đều rảnh**, chỉ có dấu nhắc `PS E:\Lottery_AI_Test>`, không lệnh nào chạy |
| Tiến trình VPS chạy > 1 giờ | chỉ `networkd-dispatcher`, `unattended-upgrade`, `BT-Panel`, `BT-Task` — của hệ điều hành và panel máy chủ |
| Journal service `lottery` từ 10:25 | **0 dòng lỗi** |

**Kết luận trung thực:** không có gì treo phía hệ thống. Ba tab kia là **phiên agent của Cursor**
kẹt ở trạng thái *"Asking questions"* — chúng đang **chờ người trả lời** chứ không phải treo do
tiến trình. Agent không điều khiển được UI của Cursor. Cách xử: đóng ba tab đó, hoặc chạy
`Developer: Reload Window`.

---

## Việc 2 — owner nghi agent cắt mà không soi tương quan

Câu hỏi đúng chỗ. Trước khi cắt agent **có** soi tham chiếu chéo (và nhờ đó cứu được `_v10692`
khỏi bị xoá), nhưng **soi TRƯỚC khi cắt** khác với **soi SAU khi cắt xem thực tế có gãy không**.

### Kết quả soi lại đầy đủ

**Không gãy chỗ nào.** 6 lane nghỉ sinh ra **19 `experiment_name`**, không cái nào còn bị UI /
API / cron / scheduler gọi đích danh. Journal 0 lỗi. Bundle MN hôm nay 15 model bình thường. Số
model 7 ngày không tụt.

### Nhưng phát hiện một lỗ trong CÁCH soi

`_v10637_lane_v2_daily` ghi bảng `lane_v2_daily_shadow`. Soi lượt đầu chỉ hỏi *"ai import MODULE
này"* → "không ai" → kết luận an toàn.

Phải hỏi thêm *"ai đọc BẢNG mà module này ghi"*. Hỏi vậy mới ra
`_v10660_no_lookahead_harness.py` — **có cron** lúc 14:45, đọc đúng bảng đó.

Kiểm tiếp: nó là bộ kiểm chứng không-nhìn-trộm, có `_table_exists()` bảo vệ, bảng vẫn tồn tại
nên chỉ audit 0 dòng. **Không gãy** — nhưng nếu là lane có người đọc thật thì đã gãy âm thầm.

**Đã ghi bài học này vào `CLAUDE.md` (bảng bẫy) và `OD-20260801-G`:** soi phụ thuộc phải **hai
tầng** — ai import module, **và** ai đọc bảng module đó ghi.

### Ba lượt dò sai của chính agent trong lúc kiểm

1. Dò cột `experiment` — tên thật là **`experiment_name`**. Hai lượt đầu trả rỗng, suýt tưởng
   "không có gì để lo".
2. So "cùng khung giờ" bằng `time(started_at)` — cột đó lưu **UTC**, lệch 7 tiếng, làm danh sách
   "vắng" dính đầy MT/MB chỉ vì chúng chưa tới giờ chạy. Suýt báo động nhầm hàng loạt.
3. Quên rằng cron gỡ lúc **10:31** còn lane chạy lượt sáng **05:30–06:10** — nên dữ liệu hôm nay
   **vẫn còn** chúng. Hiệu lực thật bắt đầu **từ ngày mai**.

---

## Việc 3 — CLAUDE.md

Chưa có file này. Đã dựng thành **mặt quy tắc thứ tư**, tự đứng được (không chỉ trỏ sang file
khác), chứa A53 + A54 + A55 + chuỗi hoàn tất 12 bước + §52 + playbook-first + bảng 8 bẫy đã học.

Đổi bộ đồng bộ từ **ba** thành **bốn** file ở **5 nơi**: `.cursorrules` · `.AGENT.md` ·
`.Antigravityrules.md` (gồm mục 51I SYNC CONTRACT) · `.cursor/rules/governance-traceability-automation.mdc`.

**Vấp:** `.AGENT.md` và `.Antigravityrules.md` dùng câu chữ khác ("semantically aligned", "SYNC
CONTRACT WITH", "mirrored in") nên mẫu tìm lượt đầu không khớp — hai file này suýt bị bỏ quên,
mà bỏ quên thì bộ đồng bộ hỏng ngay từ ngày đầu. Bắt được nhờ đếm lại số lần nhắc `CLAUDE.md`
trong từng file sau khi sửa.
