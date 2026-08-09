# CONVERSATION CONTEXT — V11047 · 2026-08-09

## Owner nói gì (NGUYÊN VĂN)

> trước đó em đã dọn dẹp các mồ côi nào khác không em? các mồ côi thực sự thì có thể xóa gỡ bỏ
> tinh gọn, nhưng các mồ côi do lỗi code chưa đấu nối thì phải đấu nổi và tiếp tục kiểm tra còn
> giá trị phục vụ cho dự án không đã rồi mới có kế hoạch clear, nếu còn thì hạn đo, hoặc gộp
> cung với các phép đo không cần là rõ, đẩy toàn bộ các báo cáo chi tiết lên githubs dùm anh nha em

## Vì sao luật này quan trọng hơn nó nghe

Trước đó agent chỉ có **hai ngăn**: «có người gọi» / «không ai gọi». Owner tách ngăn thứ hai làm
đôi, và chính chỗ tách đó là chỗ agent vừa làm sai:

- **(A) mồ côi thật** — có người thay thế, có quyết định khai tử ⇒ gỡ
- **(B) chưa đấu nối** — xây rồi mà không ai nối dây ⇒ **phải nối, phải đo, rồi mới tính clear**
- **(C) tắt có chủ ý** — owner quyết / bằng chứng bác bỏ ⇒ giữ nguyên

«Không ai gọi» là **triệu chứng chung của cả ba**. Chỉ nhìn triệu chứng thì gỡ nhầm.

## Agent đã xếp sai một ca — và tự tìm ra

`__trigger_reload__.py`: agent xếp (A) rồi gỡ. Thật ra nó do **API deploy sinh ra** để kích
`uvicorn --reload`, mà service chạy `uvicorn.run(app, ...)` **không có `reload=True`**.

Đo trên VPS: **43 lượt deploy**, bước `restart` ghi **`skipped`**, router **vẫn mount**.
⇒ API báo «ok · files written» trong khi tiến trình **không nạp mã mới**.

**Gỡ tệp không sửa được gì** — API sẽ ghi lại. Cái sai nằm ở **cơ chế chưa đấu nối**, không ở
tệp. Đây đúng loại (B).

## Phát hiện lớn nhất — thứ owner đặt hàng 09/06 đang nằm trên một máy duy nhất

`_v10705_output_total_station.py` · **44.728 byte · 982 dòng**. Docstring:

> *«Owner directive (2026-06-09): độc lập THẬT SỰ theo **miền × THỨ × ĐÀI** … chấm độ mạnh model
> theo (thứ × đài) cụ thể, ra pick RIÊNG cho TỪNG ĐÀI»*

Ba phương pháp `STWEIGHTED` / `STCHAMPION` / `STBLEND`, **đều causal (chỉ dùng quá khứ <
target_date)**, có co-rút Bayesian cho n nhỏ.

Trạng thái: **xoá khỏi git 05/07** (gói «archive 10 oneoff»), bản VPS còn, **0 cron · 0 import**.

So ba anh em cùng họ thì nó là ca cá biệt — `_v10703` (miền×thứ) có 1 cron và trong git;
`_v10708` có 2 cron và trong git; riêng bản **có chiều ĐÀI, to gấp đôi** thì **vừa mất khỏi kho
vừa không được nối**.

**Trớ trêu:** đây đúng là thứ agent «đề xuất» trong báo cáo V11046 vài giờ trước như một hướng
cải tiến mới. Hoá ra owner đã yêu cầu và đã được xây từ hai tháng trước.

## Agent làm gì — và cố ý KHÔNG làm gì

**Làm:** kéo cả hai tệp về git (`PARSE OK`, quét 0 dấu hiệu bí mật). Đây là **chống mất** — trước
đó chúng là điểm hỏng đơn, mất VPS là mất hẳn.

**Cố ý không làm:** không chạy, không đấu nối, không kết luận giá trị. Vì `_v10705` là **backtest
walk-forward**, và CLAUDE.md ghi thẳng: *«đừng bật lại bằng backtest, chỉ bằng đo tiến»* — đã rữa
**6 lần** (V10655 → V10790). Chạy để soi thì được; dùng làm căn cứ bật thì cấm.

## Suýt báo động sai lần thứ hai trong ngày

Thấy `/api/_system/deploy/health` trả **200 không auth**, agent định báo. Kiểm tiếp đường **ghi
tệp** trước: `POST /deploy` đòi `X-Deploy-Token`, so sánh constant-time, `token_configured=True`
trên production. **Không phải lỗ hổng.** Sáng nay đã một lần suýt báo lỗ hổng không tồn tại ở
`/api/viewer/*` — lần này kiểm trước khi mở miệng.

## Trả lời câu «trước đó đã dọn mồ côi nào chưa»

Không trả lời bằng trí nhớ — quét git 60 ngày: **7 commit có xoá tệp**, tổng **89 tệp**.
Phần lớn vô hại (`node_modules` 53 tệp, `.cmd` commit 24 tệp). **Một đợt xoá nhầm loại (B)**:
commit `f86d611` (05/07) xoá `_v10705` trong gói «archive 10 oneoff» — nay đã cứu.

## Đề xuất GỘP thay vì thêm

Owner dặn *«gộp cùng với các phép đo, không cần lạ rõ»*. `_shadow_phase_audit.py` chỉ **đọc và
in**, không ghi gì ⇒ đề xuất **gộp thành một phép trong bộ tự kiểm 18:05** thay vì dựng cron
riêng. Bộ đó đang có 24 phép, thêm một phép rẻ hơn nhiều so với thêm một lane.
