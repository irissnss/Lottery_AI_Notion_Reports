# CONVERSATION CONTEXT — V11046 · 2026-08-09

## Owner nói gì (NGUYÊN VĂN)

> Anh và em cùng 1 suy nghĩ với các mồ côi, nhưng em có nắm tại sao mồ côi và lý do mồ côi, trước
> đó dùng để làm gì hiện tại cần ko? có cần đấu nối đo lại với time line khác không hay thực sự
> mồ côi. Mồ côi thực sự thì gỡ luôn cho tinh gọn và nhất quán nha em. Sau đó đẩy báo cáo chi tiết
> kèm đề xuất xử lý an toàn nhất quán đảm bảo cải tiến nâng cao dự đoán nha em

## Vì sao câu hỏi này đúng hơn cách agent làm trước đó

Agent trước đó mới chứng minh **«không ai gọi nó»** rồi hỏi owner *«gỡ hay giữ»*. Owner chỉ ra
thiếu ba tầng: **vì sao mồ côi** · **trước dùng làm gì** · **dữ liệu còn đấu nối đo lại được
không**. Ba tầng đó mới phân biệt được *rác* với *đồ tốt bỏ quên*.

Và đúng như owner nghi: khi đào đủ sáu câu thì **ba thứ agent gọi là mồ côi hoá ra đang sống**,
và **một thứ nguy hiểm hơn mồ côi** lộ ra.

## Lỗi nặng nhất — agent làm owner ký nhầm

00:33 hôm nay owner ký đóng 43 mục theo bảng agent trình. Ba mục trong đó (`FU-160` `FU-162`
`FU-164`) đóng với lý do agent tự viết: *«bảng đã ngừng nhận dòng»*.

Đo lại: `v93_verdict_weight_recalibration_shadow` **3.775 dòng**, `v94_cross_region_spillover_aware_shadow`
**13.278 dòng**, cả hai ghi **mỗi ngày** tới 08/08, và **ba endpoint sống đang đọc**.

Nguyên nhân: agent quét tên thiếu tiền tố **`v93_`** rồi kết luận «KHÔNG CÓ BẢNG». Đúng **RM-10**
— quy tắc chính agent đã trích ra để nhắc mình hai lần trong hai ngày.

**Chữ ký owner không sai. Dữ kiện agent đưa mới sai.** Một phép quét hỏng làm hỏng cả một quyết
định đã ký. Ba mục đã mở lại.

## Thứ nguy hiểm hơn mồ côi

`model_strength_by_region_weekday_station_daily` — agent tưởng là «17.815 dòng vàng bị bỏ quên».
Sự thật khác hẳn:

- Nó **chưa bao giờ có tự động hoá** (0 cron, 0 import) — chỉ chạy tay hai đợt forensic.
- 17.815 dòng **không phải 17.815 ngày**: chỉ **2 anchor**, cùng `computed_at` trong **2 giây**.
- **Nhưng nó đang được đọc mỗi ngày**: **61% dòng voter 7 ngày qua** nhận điểm tính từ số **96
  ngày tuổi**. Không lỗi, không triệu chứng, số vẫn ra đẹp — RM-01 đúng nghĩa.
- Lookahead **sạch**, nhưng biên consumer `anchor_date <= ?` **cho phép anchor == ngày đó**. Bật
  lại hằng ngày mà không vá biên trước thì **tự tay tạo lookahead mới**.

Đây là bài học: *«không ai gọi»* và *«nguồn đứng im»* là **hai bệnh khác nhau**, và bệnh thứ hai
nguy hơn vì nó im lặng.

## Phát hiện lớn nhất cho câu cuối của owner

`loz_stage_trace_shadow` giữ câu trả lời cho *«cải tiến nâng cao dự đoán»*:

> **~85% đuôi trúng thật CHƯA BAO GIỜ được model nào sinh ra.**

Nút thắt **không nằm ở khâu chọn** — nằm ở **khâu sinh / độ phủ**. Nghĩa là mọi công sức tỉa bộ
chọn, xếp hạng model, cân trọng số… đang giành nhau trong **15%** dư địa còn lại.

Agent **không kết luận vội**: số đó đo trên roster tháng 5. Đề xuất chạy lại trên 96 ngày mới
(read-only, không chạm output) để xem còn đúng không, **rồi mới** quyết hướng đầu tư.

## Agent tự bắt được một cáo buộc sai của chính subagent

Subagent báo `/api/viewer/*` là *«lỗ hổng bảo mật đang mở»*. Agent chính kiểm độc lập trên
production: cả hai trả **401 Not authenticated**. **Không phải lỗ hổng.** Nếu chép lại thì đã báo
owner một lỗ hổng không tồn tại — đúng lý do RM-13 bắt kiểm nguồn trước khi kết luận.

## Đã gỡ những gì, và vì sao dám gỡ

Dây chuyền `viewer`: **0 hit trên 56.465 dòng nhật ký / 15 bản xoay**. Hai hit `/viewer` duy nhất
là **công cụ tự kiểm của chính agent** (cùng IP, curl rồi HeadlessChrome, cách 46 giây).
Thủ phạm làm nó mồ côi: commit `d411670` (07/05) cắt route trang nhưng để nguyên bốn thành phần
còn lại — **94 ngày**. Và trong 94 ngày đó có **15 commit** vẫn sửa `viewer.html`, gồm trọn đợt
reskin UI v2.

Giữ lại route `/viewer` redirect làm đường lùi cho bookmark cũ.
