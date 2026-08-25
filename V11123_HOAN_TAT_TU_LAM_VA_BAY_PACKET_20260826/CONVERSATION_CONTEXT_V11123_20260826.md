# CONVERSATION CONTEXT — V11123 · 26/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ là **giờ Việt Nam (UTC+7)**.

## 1 · Owner nói gì — nguyên văn

> *« 1. Hoàn tất tất cả công việc Agent IDE có đủ quyền và bằng chứng để tự xử. 2. Với mọi việc cần
> Owner quyết: điều tra đến nơi; trình bằng lời thường; nêu code/runtime thật; nêu được, mất, rủi
> ro; đưa khuyến nghị; đưa test, gate và rollback; **kết thúc bằng đúng một câu Owner cần trả lời**.
> 3. Cập nhật tài liệu theo kịp code. 4. **Không suy diễn yêu cầu làm rõ thành chữ ký thực thi.**
> 5. Không để Owner phải hỏi "treo à?": phải báo tiến độ sau từng giai đoạn. »*

> *« Không được khuyến nghị `C` chỉ vì "cùng pipeline". Phải có paired prospective và phân tích rủi
> ro mất tín hiệu. »* — mục `VI`

> *« Cấm: hạ `96` để vừa lịch; kéo dài `D3`; trộn denominator `423` và `534`. »* — mục `IX`

`AUTHORIZED_LAYER = LOCAL_CODE_GIT_DB_COPY_TEST_VPS_READ_REPORT` — **VPS chỉ ĐỌC**.

## 2 · Agent làm gì — theo giai đoạn

| GĐ | việc | kết quả |
|---|---|---|
| `0` | preflight | bắt 2 lỗi module `V11121`; xác nhận public HEAD **khớp** `a43e298` |
| `1` | `FU-442` | 3 lỗ vá, thử **11/11** |
| `2` | bù 10 báo cáo | **10/10 ĐẠT**; thiếu `32 → 23` |
| `3` | family map | **49/49**; phép đo **bác giả định của chính agent** |
| `4` | điều kiện `D1` | **2 đủ · 3 thiếu**; tìm thêm khuyết tật `TOTAL_METHOD_VERSION` không có trong mã |
| `5` | release pack `FU-438` | **exact SHA** xác minh; route matrix **29** |
| `6` | `D3` | ý nghĩa sàn `96` (`π≈0,643`); ba protocol mới |
| `7` | Decision Packet | **7 packet** đủ 10 phần |
| `8` | sổ owner | **ba chuyên mục**; `OWNER_XAC_NHAN` **7/7 CHƯA KÝ** |

## 3 · Vấp ở đâu — kể cả vấp do chính agent gây ra

### V1 · 🔴 Giả định của agent bị **chính phép đo** bác

Vào phiên, agent tin *«4 ML dùng chung pipeline ⇒ gộp làm một nguồn»* — đó cũng là điều current-truth
của prompt 36/37 ghi. Đo 526 ngày–miền: **`lstm` đồng phiếu `3,7–5,0%` với ba ML kia**, đúng mức
**khác họ**, và **cứu 91/387 = 23,5%** số trúng một mình.
⇒ Nếu không đo mà theo pipeline thì đã đề xuất gộp `lstm` — **phá nguồn độc lập nhất**.
**Hậu quả nếu bỏ qua:** một khuyến nghị `C` sai, dựa trên tiền đề đúng-về-mã nhưng sai-về-hành-vi.

### V2 · Tài liệu owner gửi sai một điểm **nghiêm trọng**

*«Một tệp em KHÔNG đẩy: `REPORT_V11037.md`»* — **đã push** từ `25/08 18:43:41`, và bản trên remote
còn nguyên một lệnh `ssh root@<IP>`. Agent phát hiện khi đếm lại số liệu cho packet scrub.

### V3 · `prepend()` đặt khối mới lên **TRÊN** tiêu đề sổ

Vì sổ chưa có mục ngày ở đầu. Phải sửa lại thứ tự thủ công. Ghi lại để phiên sau không lặp.

### V4 · Cách chạy toàn dải đầu tiên cho con số vô dụng — xem `CONVERSATION_CONTEXT_V11122`

## 4 · Điều agent **không** làm, và vì sao

| không làm | vì sao |
|---|---|
| Deploy `FU-438` | `AUTHORIZED_LAYER = VPS_READ`; dừng ở `READY_TO_DEPLOY` |
| Bật `D1` | thiếu **3/5** điều kiện owner khoá |
| Hard-collapse family | phép đo cho thấy sẽ **phá `lstm`** |
| Hạ sàn `96` / kéo dài `D3` | owner cấm tường minh; và sàn `96` có **ý nghĩa thống kê** (`π≈0,643`) |
| Scrub Git HEAD | owner chưa ký — `PACKET 0` |
| Đóng/gia hạn `QD` | owner chưa ký — `PACKET 2` |
| Cài/chuyển hook | owner chưa ký — `PACKET 3` |
| Sửa `prepend()` | đường ghi **dùng chung** — `PACKET 4` |
| Vá 4 đường `FU-440` | phép đo **âm**; vá cái chưa chứng minh là rò = *«đổi mù»* |
| Nối cổng A55 vào commit | chặn mọi commit tới khi hết nợ ⇒ `PACKET 6` |
| Coi prompt 37 là chữ ký | prompt là **yêu cầu làm rõ để ký lượt sau** |

## 5 · Trạng thái cuối

| | |
|---|---|
| deploy · restart · ghi DB · Notion | **KHÔNG** — cả bốn |
| `M0`/official/roster/FINAL | **KHÔNG ĐỔI** — hash 4 bảng khoá ở `REPORT_V11123` mục 5 |
| `main.py` | **không đổi trong phiên này**; bản vá `FU-438` vẫn là blob `83a4657` từ `c8d87a5` |
| kết luận phiên | **`PARTIAL`** — xem `REPORT_V11123` mục 9.0 |

**TanPhatAI cần làm:** đọc `PACKET 0` trước tiên; và **đừng** coi prompt 37 là chữ ký —
`OWNER_XAC_NHAN` ghi rõ **7/7 CHƯA KÝ**.
