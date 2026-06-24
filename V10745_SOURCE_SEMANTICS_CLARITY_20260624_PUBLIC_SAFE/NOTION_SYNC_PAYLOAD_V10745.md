# V10745 — Source Semantics & Causality clarity (read-only)

**Thời gian:** 2026-06-24T21:20:00+07:00
**Yêu cầu owner:** "ok thực hiện các đề xuất để hệ thống thực sự rõ ràng dùm anh nhé em"

## Mục tiêu
Làm hệ thống "thực sự rõ ràng" về ngữ nghĩa nguồn dữ liệu D (same-day) và D-1 (hôm qua) cho từng miền, mà tuyệt đối KHÔNG đụng prompt/đầu ra official.

## Vấn đề cần làm rõ
Nhãn `source_regions` của MN lưu rút gọn (`MB`, `MB,MT,MN`) dễ bị hiểu nhầm là dùng kết quả same-day của MT/MB — trong khi MN xổ ĐẦU TIÊN và chốt số sáng sớm nên mọi nguồn của MN tất yếu là D-1.

## Đã xác minh an toàn trước khi làm
- Chuỗi `source_region` KHÔNG đi vào prompt (prompt chỉ phụ thuộc `source_data` dict keys).
- KHÔNG có nơi nào trong backend rẽ nhánh logic theo giá trị `source_regions` (grep 0 kết quả).
- => Đổi dict keys = đổi prompt = đổi official (CẤM). Đổi nhãn ghi DB chỉ là cosmetic nhưng nằm trên hot-path nhiều call-site → rủi ro cao. Chọn lớp đọc-diễn-giải, không sửa đường ghi predict.

## Đã triển khai (read-only, admin)
- `_build_source_semantics_audit()` trong `main.py`; resolver theo THỨ TỰ XỔ MN→MT→MB: đài xổ SAU target không thể là same-day tại thời điểm chốt ⇒ tất yếu D-1 (không phải vi phạm).
- API `GET /api/admin/source-semantics-audit` (require_admin, no-store).
- Panel `/monitoring` "SOURCE SEMANTICS & CAUSALITY": badge vi phạm chiều xổ / chốt-trước-giờ-xổ / trùng station; per-region doctrine + resolve từng token + nhãn DB; bảng mined_rules keyed theo weekday+station. Auto-refresh 60s.

## Kết quả verify trên dữ liệu thật
- Vi phạm chiều xổ: **0**.
  - MN: tất cả nguồn = D-1 (MB/MT xổ sau → D-1; MN chính miền → D-1).
  - MT: `MN` same-day hợp lệ (MN xổ trước MT); `MB` → D-1 (MB xổ sau MT).
  - MB: `MN`, `MT` same-day hợp lệ (đều xổ trước MB).
- Trùng station trong cùng ngày (120 ngày): **0**.
- Predict (sớm nhất) đều trước giờ xổ: MN 00:29 < 16:30; MT 04:00 < 17:30; MB 04:00 < 18:30.
- `mined_rules` keyed đầy đủ target_weekday + source_station + source_weekday: **35/35** mỗi miền (MN/MT/MB).

## An toàn / Verify deploy
- Service `lottery`, port 8000. main.py compile PASS; backup remote pre-deploy; restart OK.
- `/api/health = 200`; `/api/admin/source-semantics-audit = 401` (chưa auth); `/api/admin/rescue-candidate-monitor = 401`.
- 4 bảng official hash **IDENTICAL** pre/post: predictions `b6cd981a392bc987`, final_bundles `e069c59d12108179`, lottery_results `6f595e2306153ddb`, model_daily_eval `fb495368581bd7fb`.
- 0 official mutation, KHÔNG cron mới.

## Rollback
Khôi phục `backups/v10745_remote_pre/main.py` + `monitoring.html`, restart `lottery`. Official output không liên quan.
