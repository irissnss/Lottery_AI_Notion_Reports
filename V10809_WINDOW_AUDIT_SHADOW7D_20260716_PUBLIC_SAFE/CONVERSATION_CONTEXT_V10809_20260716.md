# CONVERSATION CONTEXT V10809 — 2026-07-16 (10:35)

## Owner message nguyên văn (10:35, sau báo cáo V10808)

> có em và anh đang đi đúng hướng ah em. Tiếp tục anh cần em xem lại rules đang cập nhật tự động
> phân tích xếp hạng ở mốc 12 W thì phải , và mỗi miền có hệ số khác nhau như miền nam thì 8w ,
> hay miền trung thì 6-8 w ah em xem kỹ dùm anh chỗ này nữa ah . sẵn xác định những hệ số này còn
> đúng không em, còn phù hợp không em có điều chỉnh gì không em? sau đó tiếp tục chạy test trong
> showdow tổng hợp những cái cái em vừa làm rõ mang hướng cải thiện trong 7 ngày với 3 miền và
> 5 model ai kết hợp tốt và tệ nhất lại dùm anh
> ==> sau đó đưa ra đề xuất hoàn hảo an toàn nhất nha em. Toàn bộ các vấn đề phân tích xử lý cần
> ghi nhận lại nha em. chứ anh không nhớ nổi đâu đó em

## Diễn giải yêu cầu

1. Audit hệ mốc cửa sổ xếp hạng rules (12W? MN 8W? MT 6-8W?) — xác định còn đúng/phù hợp không, điều chỉnh gì.
2. Chạy shadow 7 ngày × 3 miền × 5 model (tốt + tệ nhất) tổng hợp các cải thiện đã làm rõ (addendum V10806-V10808).
3. Sau shadow → trình đề xuất hoàn hảo an toàn nhất.
4. Ghi nhận cố định toàn bộ (owner không nhớ nổi) → roadmap checkpoint bắt buộc surface đầu phiên.

## Việc đã làm trong phiên (tóm tắt)

- `_v10809_window_audit.py` (VPS, read-only): audit forward 2921 MRE rows → per-số 12W/16W tốt,
  cụm-any hỏng (MN bão hòa, MB đảo chiều), thiên lệch cụm corr −0.62..−0.83.
- `_v10809_shadow_ab.py` + cron 4 mốc + bảng `v10809_shadow_ab_daily` + panel 🧪 /monitoring → shadow chạy live.
- `docs/ACTIVE_ROADMAP_V10809_SHADOW_AB_7D.md` (CP-S1..S4) + CHANGELOG/SSOT/FU/AUTOMATION seq 270 + playbook §5.
- Deploy VPS: hash 4 bảng pre=post IDENTICAL, smoke 200/401/401, journal sạch.
