# CONVERSATION CONTEXT — V11048 · 2026-08-09

## Owner nói gì (NGUYÊN VĂN)

> trước đó em đã dọn dẹp các mồ côi nào khác không em? các mồ côi thực sự thì có thể xóa gỡ bỏ
> tinh gọn, nhưng các mồ côi do lỗi code chưa đấu nối thì phải đấu nổi và tiếp tục kiểm tra còn
> giá trị phục vụ cho dự án không đã rồi mới có kế hoạch clear, nếu còn thì hạn đo, hoặc gộp
> cung với các phép đo không cần là rõ, đẩy toàn bộ các báo cáo chi tiết lên githubs dùm anh nha em

## Luật của owner áp ngược lại chính agent — và bắt được bốn chỗ

Agent dùng luật ba loại để rà lại **chính việc mình vừa làm trong ngày**. Kết quả: **bốn lỗi, đều
của agent**.

### ① Câu sai nằm trong mã production

V11046 để lại chú thích ở `main.py:4262` và `:18404`:
*«94 ngày vẫn được serve, 0 hit trên **57.011 dòng** nhật ký nginx»*.

Đo lại: nhật ký nginx chỉ có **15 bản xoay = 26/07 → 09/08 = 15 ngày · 58.262 dòng**.
**Sai cả hai số.** «0 hit» chỉ chứng minh được cho **15 ngày**; **79 ngày trước đó không có bằng
chứng nào** vì nhật ký đã xoay mất.

Kết luận gỡ không đổi — 0 hit trong 15 ngày cộng 0 inbound link cộng không route serve vẫn đủ.
Nhưng **câu chữ thì nói quá**. Và một câu sai nằm trong **code** nguy hơn trong báo cáo: người sau
đọc code, không đọc lại commit message. Đã sửa **và deploy**.

### ② Agent nhìn thấy 357 khối rồi cất chúng đi trong cùng một commit

V11044 dựng `_LEGACY_TD` — **lần đầu tiên** trong lịch sử kho nhìn thấy 357 khối `### FU-V…`.
Rồi trong **cùng lượt đó** đẩy chúng sang `docs/archive/`, với lý do **agent tự viết**:
*«chúng là lịch sử, không phải tồn đọng»*.

Rà lại thì lý do đó **chưa từng được chứng minh**:

| | |
|---|---|
| khối LEGACY | 357 |
| mang nhãn TREO **bộ đọc công nhận** | **97** |
| có mặt lại ở sổ chính | **0** ⇒ bỏ rơi thật **97** |
| gồm | `DEPLOYED_PENDING_LIVE_VERIFY` 64 · `OWNER_LOCK` 18 · `WAIT_LIVE` 9 · `MEASURED_BUT_NOT_FIXED` 5 |

`OWNER_LOCK` và `WAIT_LIVE` đúng là hai nhãn mà `_v10920_session_start.py:20` khai là **«mục treo
phải báo»**. Và không bộ đếm nào mở tệp archive.

**Công bằng với agent:** 97 khối đó **đã vô hình từ trước** — mẫu cũ chỉ khớp `### FU-<số>`.
Agent không tạo ra sự mù. **Nhưng thấy rồi mà cất đi thì khác với chưa từng thấy.**

Đã đấu nối bằng cổng đếm + bêu tên, nối hook commit, **KHÔNG tự đóng mục nào** (RM-06).

### ③ Con số deploy API chưa đủ chính xác

V11047 ghi «43 lượt, `restart: skipped`». Tách kỹ: **5** dry_run · **25** `RESTARTING` · **13**
`skip_restart`. Trong 13 lần skip, **9 lần đẩy tệp `.py` backend** (`main.py` ×3,
`gpt_analyzer.py` ×2, `database.py`, `model_registry.py`, `pnl_settlement.py`).

Chín lần đó **ghi Python xuống đĩa trong khi tiến trình vẫn giữ mã cũ trong bộ nhớ**.

Và 25 lần nhánh `RESTARTING` **kẹt vĩnh viễn** ở trạng thái đó — tiến trình ghi trạng thái nằm
trong cgroup của unit nên bị `systemctl restart` giết trước khi ghi xong.

*Giới hạn agent tự khai:* journald chỉ giữ một boot từ 09/08 05:23, nên «25 lần đó thật sự
restart» là **suy từ code**, không phải từ log.

### ④ Đúng số vẫn có thể sai kết luận

V11046 viết *«15 commit sửa `viewer.html` sau khi nó chết»* để chứng minh lãng phí. Đo từng diff:
**3** commit quét lại cả tệp, **12** commit còn lại chỉ 1–47 dòng CSS trong các lượt
«re-inlined 14 pages». **Không commit nào đổi tính năng.**

Con số 15 **đúng**. Lập luận rút ra («có người còn nuôi nó») **sai** — đó là bị quét chung.
Đây là bài học riêng: có số thật vẫn có thể kể sai câu chuyện.

## Điều agent nói thẳng

Bốn lỗi này không do owner, không do hệ, không do phiên trước — **do chính agent trong cùng ngày
hôm nay**. Chúng chỉ lộ ra vì owner đặt một luật buộc phải phân biệt *«không ai gọi»* với
*«chưa ai nối dây»*. Nếu không có luật đó thì cả bốn đã trôi qua: chú thích sai vẫn nằm trong
production, 97 mục treo vẫn nằm im, và lập luận thổi phồng vẫn được trích lại ở báo cáo sau.
