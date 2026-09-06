# CONVERSATION CONTEXT — V11171 · 07/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `CURRENT_ACTOR = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| ~00:2x | *«Đã push báo cáo đầy đủ chi tiết hết chưa em?»* | `HỎI` | Kiểm hai kho bằng lệnh; **tự phát hiện thiếu 10 phát hiện** của lớp phản biện → bổ sung mục 3.12, đẩy `0720dfb` | `ĐÃ_LÀM` |
| ~00:4x | *«github có nhưng thay đổi anh chuyển cá nhân sáng Organization tổ chức ảo này có ảnh hưởng đến 4 link trong ảnh không ? em có bị ảnh hưởng không code và báo cáo có ảnh hưởng gì không em»* | `HỎI` | Đo `ls-remote` cả hai đường · thử `raw` · kiểm crontab và service VPS · quét địa chỉ ghi cứng | `ĐÃ_LÀM` |
| ~00:5x | *«fix dùm anh đi chứ chờ gì nữa?»* | `YÊU_CẦU` | Ghim 3 remote · sửa 12 chỗ trong 6 mặt · sửa 2 script · chạy đủ cổng | `ĐÃ_LÀM` |

---

## 2 · Điều đáng nói nhất — câu trả lời «chưa đầy đủ» là do agent tự bắt

Owner hỏi *«đã push đầy đủ chưa»*. Agent **không trả lời "rồi"** mà đi rà lại bằng lệnh, và tìm ra
**10 phát hiện có số đo thật** của lớp phản biện V11170 **bị bỏ ngoài báo cáo** — trong khi owner đã
yêu cầu *«không sót vấn đề nào»*. Bổ sung thành mục **3.12** rồi mới trả lời.

**Bài học:** câu hỏi *«xong chưa»* phải được trả lời bằng **phép kiểm**, không bằng trí nhớ. Trí nhớ
của agent về việc mình vừa làm là **không đáng tin** — nó nhớ **ý định**, không nhớ **kết quả**.

---

## 3 · Điều đáng nói thứ hai — «không hỏng» vẫn cần vá

Việc chuyển kho **không làm hỏng gì**: hai đường cũ/mới trả cùng `HEAD`, trang cũ `301`, `raw` cũ
vẫn `200`, Public/Private giữ đúng. Và **production không phụ thuộc GitHub** — không cron nào
`git pull`, service chạy thẳng từ tệp trên đĩa.

Nhưng ba nơi vẫn ghi địa chỉ cũ và **sống nhờ chuyển hướng**. Chuyển hướng của GitHub **gãy vĩnh
viễn** nếu có ai tạo kho trùng tên dưới `irissnss` — lúc đó push **âm thầm đi vào kho SAI**, không
báo lỗi. Đây là kiểu hỏng nguy hiểm nhất vì **nó không kêu**.

⇒ *«Đang chạy tốt»* **không phải** lý do để không vá.

---

## 4 · Điều đáng nói thứ ba — một báo động TẠM suýt thành lỗi vĩnh viễn trong sổ

Ghim địa chỉ VPS xong thì `ls-remote` báo `Repository not found` ở **cả hai** đường, trong khi
`ssh -T` vẫn xác thực thành công. Bản nháp báo cáo **đã viết** *«deploy key mất quyền do chuyển tổ
chức»*, kèm một việc giao owner đi mở `Settings → Deploy keys`.

**Đo lại vài phút sau thì nó THÔNG** — 3/3 lần, cả hai đường `rc=0`, `fetch --dry-run` thấy đủ nhánh.
Đó chỉ là **trạng thái tạm trong lúc GitHub lan truyền việc đổi chủ sở hữu**.

**Nếu không đo lại**, kho sẽ mang một mục *«deploy key hỏng, cần owner xử lý»* **vĩnh viễn sai**, và
phiên sau đọc được sẽ đi tìm một lỗi **không tồn tại** — đúng thứ owner vừa cảnh báo:
*«để lâu quên tình huống này rồi phải đi kiếm, cho rằng lỗi này lỗi kia mất thời gian lắm»*.

**Luật rút ra:** sau thao tác đổi hạ tầng, **một lần đo hỏng KHÔNG đủ để kết luận** — phải đo lại
sau vài phút, và đo **cả đường cũ lẫn mới**.

---

## 4b · Bẫy thứ hai — phép thử «ẩn danh» không hề ẩn danh

Khi dựng bảng kiểm, phép thử *«HTTPS ẩn danh đọc kho RIÊNG»* **THÀNH CÔNG** — trông y hệt
**kho riêng bị lộ**, một P0 bảo mật.

Sự thật: Git trên Windows có `credential.helper = manager`, **âm thầm cấp thông tin đăng nhập đã
lưu**. Tắt hẳn nó (`git -c credential.helper=`) thì kho riêng **từ chối đúng**, và `curl` thẳng vào
API trả **404** ở cả hai đường. **Kho riêng KÍN nguyên vẹn.**

**Suýt báo một P0 bảo mật KHÔNG CÓ THẬT.** Muốn thử ẩn danh cho đúng: dùng `curl` vào API, đừng dùng
git.

## 5 · Vấp ở đâu

| # | vấp | gỡ |
|---|---|---|
| 1 | Lệnh `git remote set-url` **bị bộ lọc quyền chặn** | **Dừng, không lách**, báo owner kèm lệnh cụ thể. Chỉ làm sau khi owner cho phép |
| 2 | Ghim VPS xong thì `ls-remote` hỏng — bản nháp **đã viết «deploy key mất quyền»** | **Đo lại: THÔNG 3/3.** Chỉ là trạng thái tạm. **Sửa trước khi công bố** — nếu không, kho mang lỗi vĩnh viễn không tồn tại |
| 2b | 🔴 Phép thử «ẩn danh» đọc kho riêng **THÀNH CÔNG** — trông như **kho riêng bị lộ** | `credential.helper = manager` âm thầm cấp thông tin đăng nhập. `curl` thẳng API: **404 đúng như phải thế**. **Suýt báo P0 bảo mật giả** |
| 3 | Suýt bỏ sót `_v10921_rule_a55.py` vì nghĩ *"chỉ là chuỗi văn bản"* | Nó **ghi ngược** vào ba mặt quản trị ⇒ bỏ qua sẽ **tự hoàn tác** việc hôm nay (§60.1) |
| 4 | `grep -r` toàn kho **quá 300 giây** (vướng `venv`, `backups`, `.git`) | Chuyển sang công cụ tìm kiếm có lọc theo loại tệp |

---

## 6 · Cho TanPhatAI đọc tiếp

**Địa chỉ chính thức từ nay:**
`github.com/BaoBiTanPhat/Lottery_AI_Test` (Private) ·
`github.com/BaoBiTanPhat/Lottery_AI_Notion_Reports` (Public).
Đường `irissnss/...` **vẫn chạy nhờ chuyển hướng** nhưng **đừng ghi vào tài liệu mới**.

**Một điều dễ hiểu nhầm:** sáu mặt quy tắc đã đổi địa chỉ, nhưng `AGENTS.md` và `GEMINI.md`
**sinh tự động từ `CLAUDE.md`** — **cấm sửa tay**. Muốn đổi nữa thì sửa `CLAUDE.md` + ba mặt sửa tay
kia, rồi chạy `_v10925_rule_sync_check.py`.

**Việc còn chờ owner — KHÔNG có việc nào về GitHub.** Vẫn nguyên: ba việc kỹ thuật của **V11170** (ký `SC-12` · sửa `main.py:10491`/`:10511` ·
`LIMIT 270` ra trước bộ lọc) và **năm P0 hạ tầng của V11166** vẫn nguyên.

---

TanPhatAI cần làm: ghi **`V11171`** — công khai bản này cùng `REPORT_V11171.md`. Ghi **ĐỊA CHỈ CHÍNH THỨC MỚI: `github.com/BaoBiTanPhat/...`** cho cả hai kho; đường `irissnss/...` chỉ còn sống nhờ chuyển hướng, **cấm ghi vào tài liệu mới**. Ghi **KHÔNG mất gì, KHÔNG hỏng gì** và **production KHÔNG phụ thuộc GitHub**. Ghi **đã ghim 3 remote + sửa 12 chỗ trong 6 mặt + 2 script**, sửa đúng quy trình sáu mặt. Ghi **BẢNG KIỂM 24/24 THÔNG** — local đọc+ghi cả hai kho, người ngoài tải được báo cáo công khai, **kho riêng KÍN đúng (404 ẩn danh)**, VPS đọc được qua deploy key, VPS không cần GitHub để chạy ⇒ **KHÔNG có việc gì về GitHub cần owner**. Ghi **HAI BẪY ĐO LƯỜNG đã sập**: ① một lần đo hỏng **không đủ kết luận** — `Repository not found` rồi đo lại **thông 3/3**, chỉ là trạng thái tạm lúc GitHub lan truyền; ② `credential.helper` khiến phép thử «ẩn danh» **không hề ẩn danh**, **suýt báo P0 bảo mật giả**. Ghi **tài liệu tra cứu thường trực `docs/GITHUB_KHO_VA_QUYEN.md`**. Ghi **agent tự bắt lỗi báo cáo thiếu khi owner hỏi «xong chưa»** — câu hỏi đó phải trả lời bằng phép kiểm, không bằng trí nhớ. **Code KHÔNG đi trước tài liệu** — 0 ghi production. **Không mở Prompt 44. Không mở FU mới. Không mở Plan mới.**
