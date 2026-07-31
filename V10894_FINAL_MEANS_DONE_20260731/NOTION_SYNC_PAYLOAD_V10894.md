# V10894 — Mốc FINAL là "đã xong", không phải "bắt đầu chốt"

**31/07/2026** · commit `ce3347c` · hash 4 bảng IDENTICAL

## Owner yêu cầu
"total output Tối đa MN là 15h45 / MT 16h53 / MB 17h53 thật chuẩn chính xác để người dùng còn ra quyết định nữa... biết lúc nào là cuối cùng là final. Đừng có mơ hồ."

## Chỗ mơ hồ đã sửa
V10893 đặt khoá `/choi` CHẠY đúng mốc nên nó ghi xong lúc 15:45:0x — tức SAU mốc. Mốc đang là "bắt đầu chốt" chứ không phải "đã final".

Lùi khoá về **15:43 / 16:51 / 17:51** (đổi 3/3). Sau đổi: tại đúng **15:45:00 / 16:53:00 / 17:53:00** mọi output ĐÃ nằm trong kho.

## Đo trước khi đặt biên
Bộ đo đầu tiên sai (trừ giờ ghi cũ cho cron mới → 600–1500s vô nghĩa). Đối chiếu đúng: mọi job xong trong **1–2 giây**, chậm nhất `_v10781_prompt_v2_lane` MN **38 giây**. Biên 2 phút dư sức.

## Chốt chặn siết theo giây
`_hm()` → `_hms()`: ghi lúc 15:45:30 trước bị làm tròn thành "15:45" rồi cho qua, nay là TRỄ. Kiểm 4 trường hợp biên đều đạt. Hồi tố 30/07: 37 mục trễ.

## Người dùng thấy mốc
- `/choi`: khối 3 ô MN/MT/MB, giờ FINAL cỡ lớn, đếm ngược sống ("còn 1h59" → "✓ đã final — số không đổi nữa"), quy về giờ VN, cập nhật 30s.
- `/monitoring`: panel đổi tiêu đề MỐC FINAL TOTAL OUTPUT, ba con số ngay đầu panel.
- Playwright 390px + 1440px: khối hiện, không tràn, 0 lỗi JS, 3 thẻ miền, đếm ngược khớp giờ thật.

## Tài liệu chống quên
`docs/MOC_FINAL_TOTAL_OUTPUT.md` — một trang một bảng một cách hiểu: ba mốc, chuỗi đầy đủ, cái gì miễn áp mốc kèm lý do, ai canh, vì sao lịch từng trôi, thủ tục bắt buộc khi thêm luồng mới, rollback, lịch sử đổi mốc. Playbook trỏ về đây làm gốc.

## Xác minh
Hash 4 bảng IDENTICAL (2 lần deploy) · `/api/health` 200 · `/du-doan` 200 · guard 401. `/choi` + `/monitoring` trả 401 do cổng admin nên xác minh theo chuỗi route → STATIC_DIR → md5 KHỚP → nội dung 8/8 và 6/6 dấu hiệu.

## Theo dõi live hôm nay
15:43 khoá MN → **15:45:00 MN final** · 16:51 → **16:53:00 MT final** · 17:51 → **17:53:00 MB final** · 18:02 guard phải ra 0 trễ.

Rollback: `crontab .local_backup_v10894_crontab_20260731_133757.txt`

Báo cáo đầy đủ: `V10894_FINAL_MEANS_DONE_20260731/REPORT_V10894.md`
