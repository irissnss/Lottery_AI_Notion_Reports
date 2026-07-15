# V10798 — Dời T-chốt bundle MT 16:54 / MB 17:54 + lane early 16:53/17:52 + CP-L6 dời 19/07 (15/07, DEPLOYED)

**Trigger:** owner ký mốc tối đa ép output hoàn hảo MT 16:55 / MB 17:55 (= freeze marks V10782); yêu cầu rà kỹ thứ tự producer trước consumer, không chồng chéo; "cpl6 theo khuyến nghị".

**Phát hiện gốc (audit 7 ngày):** job chốt bundle cuối (T-10 cũ 16:45/17:45) chạy TRƯỚC giờ shadow về (MT 16:52-59, MB 17:47-52) → official quanh năm thiếu 9-11 model — gốc lệch inline-vs-lane V10796.

**Deploy:**
- scheduler.py: T-chốt MT 16:45→16:54, MB 17:45→17:54, MN giữ 15:45; misfire_grace 60s (trễ qua :55 tự no-op, bundle đầu ngày vẫn đứng).
- Crontab lane v10692 early: MT 16:50→16:53, MB 17:55→17:52 — lane sinh số liệu trước, chốt :54 đọc lane tươi (K11a/K15 promote giữ nguyên code).
- Freeze :55 KHÔNG đổi. /choi combo m1 (lane MB) có số sớm hơn 3 phút.

**Verify:** test local ALL_PASS (freeze biên, marks, compile, promote smoke); deploy: service active, health 200, /du-doan 200, admin noauth 401, journal jobs T-chốt 16:54/17:54 đúng, crontab 4 dòng v10692 đúng, **hash 4 bảng pre=post IDENTICAL**. Rollback: scheduler.py.bak_v10798 + crontab pre + restart.

**CP-L6:** owner ký "theo khuyến nghị" → DỜI 19/07, quyết 1 lần cùng CP-R4 + retire glm-5.1 (counterfactual V10797). Roadmap: OWNER_APPROVED_DEFER_19/07.

**Live-verify tối 15/07:** lane 16:53/17:52 chạy đúng → chốt 16:54/17:54 pool đầy → freeze :55 khóa → /choi combo lock trước 18:00. Đo lệch inline-vs-lane 14d đến 24/07.

**Chi tiết:** GitHub public `V10798_TCHOT_TIMING_20260715_PUBLIC_SAFE/BAO_CAO_V10798_FULL.md`
