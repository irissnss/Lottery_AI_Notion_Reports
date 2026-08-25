# CONVERSATION CONTEXT — V11121 · 25/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ là **giờ Việt Nam (UTC+7)**.

## 1 · Owner nói gì — nguyên văn

Prompt 36, các mục thi hành trong bản này:

> *« **IV. P0** … 2. Kiểm trạng thái thật của "22 làn đang chạy": PID, output, thời điểm cuối và
> verdict; **không tìm được thì UNKNOWN**. 3. Dựng session lease: owner/session/PID/start/TTL.
> 5. **Thử chặn hai writer và thử đường sạch.** 6. Không rewrite các commit bị lẫn nhãn; chỉ tạo
> mapping truy vết. »*

> *« **VIII. P3** … 26/08→23/09 tối đa khoảng 87 region-days < sàn 96. **Phải ghi rõ bất khả thi
> nếu dùng prospective-only.** … **Không hạ ngưỡng. Không tự kéo dài.** Muốn tiếp tục phải mở
> preregistration mới. Denominator 423 và 534 phải tách riêng. »*

> *« **IX. P4** … 3. **Xác nhận hoặc bác R5 bằng output thật.** 4. Cứu "GĐ-7 mười bản vá" thành tài
> liệu có đủ 10 mục, code anchor, được/mất, test, rollback. … **6. Không bù report cho
> V11077/V11079.** 7. V11118 có xung đột vị trí: **không move/xóa**; tạo pointer/index không phá
> huỷ. … 10. Bổ sung `scheduler_logs.log_time=UTC` đúng sáu mặt. »*

## 2 · Agent làm gì

| # | việc | kết quả |
|---|---|---|
| 1 | Kiểm **trạng thái thật** của 22 làn phiên trước | 🔴 **ĐÃ DỪNG** — `journal.jsonl` chỉ có **2/22** kết quả; 6 làn dở dang **không có** `StructuredOutput` ⇒ **mất**; 14 làn chưa chạy. Không suy đoán, đọc thẳng tệp |
| 2 | Phóng **8 làn đọc mới** `READ-ONLY` | 8/8 xong · 1,07 triệu token · 336 lượt gọi · **0 lỗi** |
| 3 | Xác minh `R5` bằng **output thật** | **XÁC NHẬN**, và tìm thêm **lỗ hổng thứ ba** |
| 4 | Tái lập vụ lẫn nhãn 25/08 | **100%** bằng `git show` + `git reflog` |
| 5 | Dựng khoá phiên + thử chặn hai chiều | **8/8 ĐẠT**, có khôi phục nguyên trạng |
| 6 | Vá hai lỗ hổng hook | đường dẫn tuyệt đối + sổ điểm danh |
| 7 | Tính `P3` | `T1` **bất khả thi**, ba trần độc lập |
| 8 | Viết 3 Candidate Card + ma trận khuyết | `D1` **chưa đủ điều kiện** (thiếu 3/5) |
| 9 | **Đo** `scheduler_logs` trước khi ghi luật | `t10_chot` lệch **đúng 7h** ở ba neo |
| 10 | Cứu `GĐ-7` | 10 mục, neo mã **xác minh lại từng cái** |

## 3 · Vấp ở đâu

### V1 · 🔴 Bash kẹt thư mục làm việc gần **nửa phiên** — và chính nó là phát hiện lớn nhất
Một lệnh `cd web/backend` làm hook `git commit` (gọi bằng **đường dẫn tương đối**) không tìm thấy
tệp Python ⇒ **thoát 2**. Với `PreToolUse`, thoát 2 = **CHẶN**. Nên **mọi lệnh Bash sau đó bị từ
chối**, kể cả lệnh `cd` để quay lại. Phải chuyển sang PowerShell và công cụ đọc/grep chuyên dụng
cho tới khi shell tự đặt lại.
**Hậu quả nếu bỏ qua:** đây là **lỗ hổng cổng số 1** — chín cổng con **không chạy lần nào** mà agent
lại tưởng bị cổng chặn. Nếu không vấp thì không ai phát hiện.

### V2 · Commit đầu lỡ đưa backup **1 MB / 22.184 dòng** vào Git
Git đã có bản trước-vá tại `de35b10` ⇒ dư thừa **vĩnh viễn**. Đã gỡ khi **chưa push** và thêm mẫu
vào `.gitignore`. *(Chọn `--amend` thay vì commit mới, có cân nhắc: commit chưa push, và để một
blob 1 MB nằm lại lịch sử là cái giá lớn hơn.)*

### V3 · Cổng commit **chặn đúng** một lần — ghi lại để không ai đọc nhầm thành lỗi
Lần amend bị chặn vì `V11120` đã vào `git log` mà chưa có dòng `HISTORY` (`§63 K1`). Đó là **cổng
làm đúng việc**. Đã ghi bốn mặt rồi commit lại.

### V4 · Agent phải rút lại **hai câu của chính mình** viết cách đó hai giờ
`R6` (*«26 nhãn git-only»*) và `R7` (*«chỗ làm K1 mù»*) trong `REPORT_V11119`. Làn phản biện tìm ra:
`26` **không tái lập được** ở bất kỳ phạm vi số hiệu nào, và `K1` **đã hết mù từ `V11082`**.
**Hậu quả nếu bỏ qua:** hai việc **không tồn tại** nằm trong plan, tốn công phiên sau.

### V5 · Suýt ghi luật `§55` theo lời báo cáo cũ
Câu *«`scheduler_logs.log_time` là UTC»* đến từ báo cáo trước. Agent **không ghi ngay** mà đo lại:
`MAX(log_time)` một mình **không đủ** kết luận. Phải tìm job có **giờ VN đã biết** (`t10_chot`) mới
chứng minh được lệch đúng 7 giờ ở ba neo.
**Hậu quả nếu bỏ qua:** ghi một quy ước vào **sáu mặt quy tắc** dựa trên lời truyền miệng.

### V6 · Phát hiện ba mặt sửa tay **đã có** luật này từ trước
`.cursorrules:643` · `.Antigravityrules.md:786` · `.AGENT.md:682` đều đã ghi *«33 cột đang lưu
UTC, lớn nhất `scheduler_logs.log_time`»*. Thiếu **chỉ ở `CLAUDE.md`** + hai mặt sinh. Nên câu
*«§55 chưa bổ sung quy ước thứ tư»* đúng **3/6 mặt**, không phải 6/6.

## 4 · Điều agent **không** làm

| không làm | vì sao |
|---|---|
| Rewrite commit lẫn nhãn | owner cấm; chỉ tạo mapping truy vết trong báo cáo |
| Move/xoá `REPORT_V11118.md` | owner khoá — chỉ thiết kế con trỏ không phá huỷ |
| Bù report cho `V11077`/`V11079` | owner khoá, và chúng **không thiếu** |
| Bù 10 report thiếu | cần lease + đúng nguồn; đã xác minh **cả 10 đều có nguồn**, để phiên sau |
| Khoá tầng `prepend()` | đụng đường ghi **mọi** tài liệu ⇒ `FU-443`, chờ owner |
| Vá 4 hook Cursor chết | đổi hành vi hook ⇒ `FU-441`, chờ owner |
| Thi hành bản vá `GĐ-7` nào | cả 10 đều đổi hành vi cổng hoặc lược đồ |
| Bật `D1` | thiếu **3/5** điều kiện owner khoá |
| Hạ sàn `96` hay kéo dài `D3` | owner cấm tường minh |

## 5 · Trạng thái cuối

| | |
|---|---|
| commit | `2d973c7` (riêng) · bản này (công khai) |
| deploy · restart · ghi DB | **KHÔNG** |
| `M0_WEIGHTED_VOTING_WR` | **giữ `OFFICIAL`**, không đổi một dòng đường official |
| khoá phiên | đang giữ bởi phiên `c8d5eaf3`, `PID 17016` |

**TanPhatAI cần làm:** đọc `REPORT_V11121 §3.1`–`§3.2` **trước** khi thi hành bất kỳ việc nào từ
plan của `V11119` — hai việc trong đó đã được chứng minh là **không tồn tại**.
