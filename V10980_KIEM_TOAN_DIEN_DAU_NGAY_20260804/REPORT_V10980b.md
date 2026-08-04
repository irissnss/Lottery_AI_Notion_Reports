# V10980b — ĐÍNH CHÍNH: V10979 deploy giữa phiên kiểm toán, ba con số trong V10980 phải đọc lại

> **Phiên bổ sung của V10980** · 2026-08-04 10:20 (giờ VN)
> Báo cáo này bổ sung cho `REPORT_V10980.md` trong cùng thư mục. Ngữ cảnh hội thoại dùng chung
> `CONVERSATION_CONTEXT_V10980_20260804.md`.
>
> **Vì sao có báo cáo riêng (viết bổ sung 05/08 trong V10986):** `CHANGELOG.md` có khối
> `## V10980b` nên cổng `_v10921_report_gate.py` coi đây là một phiên bản độc lập và đòi báo cáo
> riêng. Suốt ngày 04/08 các phiên chỉ chạy cổng theo từng phiên bản (`report_gate V10982`) nên
> **không ai thấy** bản quét toàn bộ đang trượt. V10986 phát hiện và vá bằng cách viết đúng báo
> cáo còn thiếu, **không** nới cổng.

---

## 1. Tóm tắt một đoạn

Trong lúc phiên kiểm toán đầu ngày V10980 đang đo, phiên **V10979 deploy song song** lúc
**10:15:13** và **10:16:59**, làm **PID đổi 738032 → 770947**. Đây **không phải sự cố**: tắt êm,
`NRestarts=0`, health 200, 0 traceback, 0 error. Hậu quả là **ba con số trong báo cáo V10980 đo
trước 10:12 đã cũ ngay khi viết**: PID, số phép tự kiểm (18 → **21**), số dòng cron (76 → **79**).
Đã đo lại phần bị ảnh hưởng và xác nhận V10979 **không đè** bản vá tối 03/08.

## 2. Owner yêu cầu gì — nguyên văn

Không có yêu cầu riêng cho phiên bổ sung này. Yêu cầu gốc vẫn là lời owner lúc **09:47 ngày
04/08**:

> *"Kiểm tra toàn diện hệ thóng đầu ngày dùm anh luôn em"*

Phiên bổ sung này là **agent tự phát hiện và tự đính chính**, không phải owner nhắc.

## 3. Đào bới / phát hiện

Lần kiểm sống cuối lúc **10:20** thấy PID không khớp con số đã ghi lúc 09:52. Truy `journalctl`
ra hai mốc restart **10:15:13** và **10:16:59**, khớp đúng cửa sổ deploy của V10979.

| Con số trong V10980 | Ghi lúc đo (09:52–10:12) | Đúng sau 10:20 | Vì sao đổi |
|---|---|---|---|
| PID `lottery` | 738032 | **770947** | V10979 deploy |
| Bộ tự kiểm | 18 phép | **21 phép** | V10979 thêm C19/C20/C21 |
| Cron | 76 dòng | **79 dòng** | thêm 3 dòng `_v10979_early_block.py` |

Vì V10979 sửa **đúng file** `_v10900_consistency_guard.py` mà V10980 vừa vá, phải kiểm lại bản vá
có bị đè không — không suy đoán:

- `C17_nghiemthu_co_output` và `C18_bien_lane_du_rong` **còn nguyên**
- Gọi tươi `run_checks()` (không đọc bản đã lưu): **21 phép · OK 21 · LỆCH 0**
- Cron lane nghiệm thu vẫn đủ **11 dòng predraw** (MN 2 · MT 4 · MB 5) — bản vá tối 03/08 không bị đè
- **4 bảng khoá không đổi**
- MN official hôm nay vẫn bạch thủ **22** / `model_count` **15**

## 4. Hướng xử lý và vì sao chọn

Ba phương án cân nhắc:

1. **Sửa đè số cũ trong khối V10980** — loại: xoá dấu vết là đúng thứ owner ghét; người đọc sau
   không biết số từng sai và vì sao.
2. **Bỏ qua vì "không phải sự cố"** — loại: ba con số sai vẫn là ba con số sai, và **ngưỡng
   FU-259 phụ thuộc trực tiếp** vào số phép tự kiểm (18 hay 21).
3. **Viết khối đính chính riêng, nêu rõ số nào đọc lại** — **chọn**. Giữ nguyên bản gốc, thêm
   đính chính, và **đo lại phần bị ảnh hưởng** thay vì chỉ sửa chữ.

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `CHANGELOG.md` | thêm khối `## V10980b` (prepend) |
| `docs/FOLLOW_UP_TRACKER.md` | ngưỡng `FU-259` đổi 18 → **21 dòng** lúc 18:05 |

**Không deploy, không restart, không đụng runtime** trong phiên bổ sung này — việc deploy là của
V10979, phiên này chỉ đo lại và ghi nhận. Không cần backup vì không sửa file mã nguồn.

## 6. Cổng kiểm

| Cổng | Kết quả |
|---|---|
| `run_checks()` gọi tươi | **21 phép · OK 21 · LỆCH 0** |
| Cron predraw lane nghiệm thu | **11 dòng** (MN 2 · MT 4 · MB 5) — đủ |
| Hash 4 bảng khoá | **không đổi** |
| `systemctl` | `active` · `NRestarts=0` · health **200** |
| MN official 04/08 | bạch thủ **22** · `model_count` **15** |

**Xác minh lại 05/08 (V10986):** PID nay là **801640** (V10984 deploy lúc 21:59:42), `NRestarts=0`,
health **200** — chuỗi PID trong ngày là 738032 → 770947 (V10979) → 801640 (V10984), tất cả đều là
deploy có chủ đích, không lần nào là sự cố.

## 7. Vướng vấp

**Hai phiên chạy song song trên cùng một file.** V10979 và V10980 cùng sửa
`_v10900_consistency_guard.py` trong khoảng 20 phút. Lần này may: V10979 thêm phép mới chứ không
viết đè, nên bản vá C17/C18 sống sót. **Hậu quả nếu bỏ qua:** nếu V10979 ghi đè cả file thì hai
phép C17/C18 vừa vá tối 03/08 biến mất **mà báo cáo V10980 vẫn khai "đã vá"** — xanh giả loại
nặng nhất, và không cổng nào bắt được vì cổng đọc chính file đã bị đè.

**Bài học:** báo cáo kiểm toán chụp ảnh hệ thống tại một thời điểm; nếu có phiên khác deploy giữa
chừng thì **mọi số đo trước mốc đó phải đọc lại**, không được coi là còn đúng.

## 8. Gỡ về

Không có gì để gỡ — phiên này chỉ ghi tài liệu, không sửa mã, không deploy. Muốn bỏ đính chính thì
xoá khối `## V10980b` khỏi `CHANGELOG.md` và trả ngưỡng `FU-259` về 18 dòng (~1 phút), nhưng làm
vậy là cố ý giữ lại ba con số sai.

## 9. Theo dõi tiếp

| Mã | Mã đọc | Việc | Ngưỡng bằng số | Hạn |
|---|---|---|---|---|
| `FU-259` | `KS0805` | C17/C18 mới đúng trên giấy, chưa có lượt chạy thật | 18:05 bảng phải có **đúng 21 dòng** (không phải 18) | 05/08 |

**Trạng thái 05/08 (V10986):** `FU-259` vẫn `WAIT_LIVE`, đến hạn hôm nay.
