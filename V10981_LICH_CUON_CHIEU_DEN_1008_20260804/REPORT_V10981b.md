# V10981b — ĐÍNH CHÍNH: nhãn `SCHEDULED` tự chế làm 11/14 mục thành MỒ CÔI

> **Phiên bổ sung của V10981** · 2026-08-04 (giờ VN)
> Bổ sung cho `REPORT_V10981.md` cùng thư mục. Ngữ cảnh hội thoại dùng chung
> `CONVERSATION_CONTEXT_V10981_20260804.md`.
>
> **Vì sao có báo cáo riêng (viết bổ sung 05/08 trong V10986):** `CHANGELOG.md` có khối
> `## V10981b` nên cổng `_v10921_report_gate.py` đòi báo cáo riêng cho phiên bản này. Ngày 04/08
> chỉ chạy cổng theo từng phiên bản nên bản quét toàn bộ trượt mà không ai thấy. V10986 vá bằng
> cách viết đúng báo cáo còn thiếu, **không nới cổng**.

---

## 1. Tóm tắt một đoạn

**Lỗi do chính phiên V10981 gây ra, đã sửa xong trong cùng ngày.** Khi giãn 14 mục dồn ngày 08/08
thành lịch cuốn chiếu, agent gán cho cả 14 mục một nhãn **tự chế là `SCHEDULED`**. Nhãn đó không
nằm trong `_v10958_fu_reader.TREO_STATUSES` cũng không nằm trong `DONG_STATUSES`, nên **11/14 mục
rơi khỏi mọi bộ đếm và bị xếp MỒ CÔI**. Đã trả lại đúng nhãn thật của từng mục và thêm phép **K8**
vào cổng để chặn tái phát.

## 2. Owner yêu cầu gì — nguyên văn

Không có yêu cầu riêng. Yêu cầu gốc vẫn là lời owner lúc **10:29 ngày 04/08**:

> *"Giãn ra cuốn chiếu tới hết ngày 10/08 phải hoàn thành, làm lần lượt những vấn đề nào xác thực
> rõ ràng , đơn giản làm trước tới cuối cùng 10/08 phải xong"*

Phiên bổ sung này là **agent tự phát hiện lỗi mình vừa gây ra và tự sửa**, owner không phải nhắc.

## 3. Đào bới / phát hiện

**Trớ trêu:** kiểm toán V10980 sáng cùng ngày vừa bêu **19 mục mồ côi**; phiên đi xử chuyện đó
suýt đẻ thêm **11 mục** nữa.

Cơ chế lỗi: bộ đọc sổ theo dõi chỉ công nhận nhãn nằm trong hai danh sách cứng. Nhãn lạ không báo
lỗi, không cảnh báo — mục chỉ **im lặng biến mất** khỏi bộ đếm.

**Hậu quả nếu bỏ qua:** 11 mục biến mất khỏi briefing đầu phiên, khỏi bộ đếm quá hạn, khỏi cổng
thiếu mã đọc. Đến 10/08 không ai biết chúng trượt hạn — **cả phiên giãn lịch thành vô nghĩa vì
lịch không cổng nào canh**. Đúng loại xanh giả.

## 4. Hướng xử lý và vì sao chọn

| Phương án | Kết luận |
|---|---|
| Thêm `SCHEDULED` vào `TREO_STATUSES` | **loại** — nới danh sách để hợp thức hoá nhãn tự chế; lần sau lại đẻ nhãn mới |
| Trả lại đúng nhãn từng mục đang có trước phiên | **chọn** — phiên này chỉ đổi **HẠN**, không đổi **tiến độ việc**, nên nhãn phải giữ nguyên |
| Chỉ sửa dữ liệu, không thêm cổng | **loại** — sửa xong lần này không ngăn được lần sau |

Riêng `FU-193` nâng `MEASURED_BUT_NOT_FIXED` → `AWAITING_OWNER_OK` vì nay chờ owner duyệt một con
số ngưỡng; cả hai nhãn đều hợp lệ.

## 5. Đã làm gì

Trả lại đúng nhãn cho 14 mục:

| Mã máy | Mã đọc | Hạn | Nhãn đúng |
|---|---|---|---|
| `FU-187` | `KS0804-1` | 04/08 | `DEPLOYED_PENDING_LIVE_VERIFY` |
| `FU-191` | `XH0804` | 04/08 | `MEASURED_BUT_NOT_FIXED` |
| `FU-212` | `DO0804` | 04/08 | `MEASURED_ROOT_CAUSE_FOUND` |
| `FU-207` | `DP0805-1` | 05/08 | `MEASURED_BUT_NOT_FIXED` |
| `FU-210` | `DO0806-1` | 06/08 | `MEASURED_BUT_NOT_FIXED` |
| `FU-193` | `XH0807` | 07/08 | `AWAITING_OWNER_OK` |
| `FU-186` | `KS0808-2` | 08/08 | `WAIT_LIVE` |
| `FU-203` | `DO0808-2` | 08/08 | `WAIT_LIVE` |
| `FU-215` | `DB0808` | 08/08 | `OWNER_LOCK` |
| `FU-192` | `XH0809` | 09/08 | `AWAITING_OWNER_OK` |
| `FU-216` | `XH0809-1` | 09/08 | `OWNER_LOCK` |
| `FU-217` | `SC0809` | 09/08 | `MEASURED_BUT_NOT_FIXED` |
| `FU-231` | `HT0810-1` | 10/08 | `OWNER_LOCK` |
| `FU-226` | `HT0810-2` | 10/08 | `OWNER_LOCK` |

**Chặn tái phát:** thêm phép **K8** vào `_v10981_kiem_lich.py` — mọi mục trong nhóm phải mang nhãn
thuộc `TREO_STATUSES` hoặc `DONG_STATUSES`.

Hạn · mã đọc · điều kiện xong · phụ thuộc **không đổi** so với khối V10981.
`docs/FOLLOW_UP_TRACKER.md` 1.034.263 → **1.051.529** ký tự. **Không deploy, không đụng runtime.**

## 6. Cổng kiểm

| Cổng | Kết quả |
|---|---|
| **K8 chạy trên bản LỖI** (thử ngược) | **TRƯỢT** — liệt đúng 11 mã · bằng chứng `evidence/cong_kiem_lich_K8_truot_truoc_khi_sua.txt` |
| `_v10981_kiem_lich.py` sau khi sửa | **8/8 ĐẠT** |
| `_v10920_session_start.py` (đối chứng độc lập) | mồ côi vẫn **19** (không tăng) · treo vẫn **98** · briefing hiện đúng *"ĐẾN HẠN HÔM NAY: 3"* (`FU-187` `FU-191` `FU-212`) |

Lịch đã **sống trong bộ đếm** chứ không chỉ nằm trong báo cáo.

**Xác minh lại 05/08 (V10986):** `_v10981_kiem_lich.py` vẫn **8/8 ĐẠT**, K8 báo *"14/14 nhãn hợp
lệ, đều được bộ đếm nhìn thấy · đã đóng 3/14"*. Mồ côi toàn sổ nay **18** (giảm 1 so với 19).

## 7. Vướng vấp

**Vấp do chính agent gây ra** — đây là mục quan trọng nhất của báo cáo này. Agent tự đặt một nhãn
trạng thái nghe hợp lý (`SCHEDULED`) mà không tra danh sách nhãn bộ đọc công nhận. Không có thông
báo lỗi nào; mọi thứ **trông như đã ghi đúng**.

**Bài học:** nhãn trạng thái trong sổ theo dõi **không phải chỗ để sáng tạo**. Phải lấy từ danh
sách bộ đọc công nhận, nếu không mục "trông như đã ghi" mà thực chất **vô hình với mọi cổng**.

**Cái bẫy này còn sống:** `FU-262` (mở cùng ngày trong V10979) hiện mang nhãn
`FIXED_PENDING_LIVE_VERIFY` — cũng **không** thuộc `TREO_STATUSES` — nên đang nằm trong danh sách
**18 mồ côi** dù có hạn 05/08. K8 chỉ canh 14 mục của nhóm này, không canh toàn sổ.

## 8. Gỡ về

Đổi nhãn 14 mục về `SCHEDULED` trong `docs/FOLLOW_UP_TRACKER.md` và gỡ phép K8 khỏi
`_v10981_kiem_lich.py` (~3 phút). Backup: `backups/v10981_pre/`. **Không nên gỡ** — gỡ là tự làm
mù bộ đếm trở lại.

## 9. Theo dõi tiếp

| Mã | Mã đọc | Việc | Ngưỡng bằng số | Hạn |
|---|---|---|---|---|
| — | — | K8 canh 14 mục nhóm này | 14/14 nhãn hợp lệ mỗi lần chạy | liên tục |
| `FU-262` | `SC0805` | Nhãn `FIXED_PENDING_LIVE_VERIFY` đang làm mục này mồ côi | mồ côi toàn sổ phải **≤ 18** và giảm dần | 05/08 |

Việc mở rộng phép K8 ra **toàn sổ** (không chỉ 14 mục) chưa làm — ghi nhận trong V10986 phần "còn nợ".
