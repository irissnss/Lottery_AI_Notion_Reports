# V10798 — Dời T-chốt bundle sát mốc owner (MT 16:54, MB 17:54) + lane early 16:53/17:52 + CP-L6 ký dời 19/07

- **Ngày:** 2026-07-15 sáng (DEPLOYED 10:15)
- **Trigger (owner 09:25):** "Mốc giờ tối đa để bắt buộc hệ thống output dự đoán hoàn hảo là MT 16h55 và MB 17h55 là được, em xem thật kỹ để không bị chồng chéo hoặc ảnh hưởng nha em, các mốc thật logic cái nào cần cho số liệu trước, cần ưu tiên trước phải rà soát lại hết nha em. cpl6 theo khuyến nghị nha em"

## 1. Rà soát timeline thật (audit 7 ngày, DB live)

| Mốc | MT | MB |
|---|---|---|
| Token batch xong | 16:38-16:43 | 17:33-17:36 |
| Bundle official lần đầu (inline sau chain) | ngay sau token | ngay sau token |
| Shadow batch về đủ | 16:52-16:59 (2/7 ngày lố 17:00+) | 17:47-17:52 (2/7 ngày lố 18:00) |
| Job chốt cuối cũ (T-10, V10782) | **16:45 — TRƯỚC khi shadow về** | **17:45 — TRƯỚC khi shadow về** |
| Lane `*_OUTPUT_V1` early (cron) | 16:50 | 17:55 |
| FREEZE khóa official (V10782) | 16:55 | 17:55 |

**Phát hiện gốc:** job chốt cuối chạy trước giờ shadow về → bundle official quanh năm thiếu 9-11 model shadow — đây chính là gốc "lệch inline-vs-lane" đã báo động ở V10796. Mốc owner chốt (16:55/17:55) trùng đúng freeze marks hiện hành → không đổi freeze, chỉ xếp lại phút.

## 2. Thay đổi (2 surface, producer → consumer, reversible)

1. **`scheduler.py` — T-chốt bundle:** MT 16:45 → **16:54**, MB 17:45 → **17:54**, MN giữ 15:45 (pool MN đủ từ sáng). misfire_grace 240→60s; nếu job trễ qua :55 → guard freeze tự no-op, bundle đầu ngày vẫn đứng (output không bao giờ trống).
2. **Crontab VPS — lane v10692 early:** MT `16:50` → **`16:53`**, MB `17:55` → **`17:52`** — lane sinh số liệu TRƯỚC, job chốt :54 đọc lane bundle tươi (cơ chế K11a/K15 ưu tiên lane, thiếu thì inline cùng thuật toán — không đổi code promote).

**Chuỗi mới mỗi chiều:**
- MT: 16:38 bundle đầu → 16:53 lane (pool tới 16:53) → **16:54 chốt official** → 16:55 freeze → 16:56 selector shadow → 17:10 lane full-pool (reference đo lệch).
- MB: 17:34 bundle đầu → 17:47-52 shadow về đủ → **17:52 lane (pool ~đủ)** → **17:54 chốt official** → 17:55 freeze → 17:56 selector. /choi combo m1 có số sớm hơn 3 phút → lock combo rộng cửa hơn trước 18:00.

**Không đụng:** freeze marks, vote layer, promote modules, money board, MN chain, prompt-v2, watchdog 17:55, lane đo 17:10.

## 3. Test & Deploy

- **Test local ALL_PASS:** freeze biên (16:54:59 chưa khóa / 16:55:00 khóa; 17:54:59/17:55:00 tương tự), marks tuple đúng, py_compile OK, promote smoke đọc lane 14/07 đúng picks.
- **Deploy:** backup VPS (`scheduler.py.bak_v10798`, `backups_crontab_v10798_pre.txt`) → SCP + compile OK → sed crontab (verify 4 dòng v10692: 04:30 MN / 16:53 MT / 17:52 MB / 17:10 all-region) → restart service `active` → smoke: health=200, /du-doan=200, /choi=401 (cần login — đúng), admin noauth=401 → journal xác nhận jobs "T-chốt bundle MT (16:54) / MB (17:54)".
- **Hash 4 bảng pre = post IDENTICAL** (predictions 10084 / final_bundles 412 / lottery_results 15075 / model_daily_eval 9908).
- **Rollback 1 lệnh:** restore `.bak_v10798` + crontab pre + restart.

## 4. CP-L6 — owner ký "theo khuyến nghị"

CP-L6 chính thức **DỜI 19/07**: quyết 1 lần cùng CP-R4 + retire glm-5.1, dựa bằng chứng counterfactual V10797 (cắt opus/gpt-5.4 khỏi vote 90d vô hại ±1 ngày; tiết kiệm ~$10/th; opus carry-quality 46% cao nhất bể). Roadmap Lean Harvest cập nhật `OWNER_APPROVED_DEFER_19/07`.

## 5. Kỳ vọng & live-verify tối nay (15/07)

| Kiểm | Kỳ vọng |
|---|---|
| Lane MT 16:53 + chốt 16:54 | Official MT ăn thêm shadow về trước 16:53 (ngày nhanh ăn trọn; 2/7 ngày shadow lố 16:55 là giới hạn vật lý — khóa xổ 17:00 không dời thêm được) |
| Lane MB 17:52 + chốt 17:54 | Official MB ăn ~trọn pool 24-26 model (shadow xong 17:47-52) — kỳ vọng lệch inline-vs-lane MB → ~0 |
| Freeze :55 | Vẫn khóa đúng — job trễ tự no-op |
| /choi combo MB | Lock trước 18:00, m1 từ lane 17:52 |

Đo lệch inline-vs-lane tiếp tục đủ 14 ngày đến 24/07 làm bằng chứng số cho hiệu quả thay đổi này.
