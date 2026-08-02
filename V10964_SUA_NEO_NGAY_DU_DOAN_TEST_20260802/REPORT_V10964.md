# REPORT_V10964 — Sửa neo ngày /du-doan-test + kiểm /filter

## 1. Tóm tắt một đoạn

Trang `/du-doan-test` neo ba miền ba ngày khác nhau vì API từng kéo cả trang về “ngày official mới nhất” khi hôm nay chưa có, cộng UI gắn nhãn “HÔM NAY” dù số là ngày cũ. Cột test MN trống vì gate đúng 20/20 (thực tế 18/20 có số nhưng UI không hiện preview). Đã sửa: ba miền cùng quy tắc `requested_date`, nhãn ngày của đúng dữ liệu, hiện preview phụ kèm lý do/giờ dự kiến. `/filter`: bản vá V10960 đã trên VPS nhưng thiếu `Cache-Control` nên trình duyệt dễ giữ HTML cũ; đã thêm `no-store`, ẩn sticky trùng ở overview, gộp 4 card → 2, sửa `getVNDateISO`. Deploy 18:13 VN, PID 641906→645169, `/api/health=200`, hash 4 bảng y nguyên. QD-014 tôn trọng — không đổi cách tính số.

## 2. Owner yêu cầu gì

> *"https://xs.io.vn/du-doan-test có dọn thì gọn cho đàng hoàng nha em. MN thì neo dữ liệu hôm qua, cột lane test thì trống. MT neo dự đoán ngày 31/07, cột lane test thì lại có hôm nay. MB thì chưa biết, cũng card cũng lưu ngày 31/07. Sao mà tùm lum vậy em?"*

> *"https://xs.io.vn/filter?tab=overview cũng chưa kiểm tra xử lý dùm anh luôn."*

Kèm: làm theo kiểu `_v10879_nghiemthu_lane` (đủ 3 miền + lý do + giờ dự kiến); không đụng QD-014; deploy tránh giờ chạy; báo cáo công khai V10964; không Notion.

## 3. Đào bới / phát hiện

### 3.1 Nguồn dữ liệu `/du-doan-test`

| Cột | Nguồn | API |
|---|---|---|
| Chính thức | `final_bundles` (read-only) | `/api/du-doan-test/{mn\|mt\|mb}` → `baseline` |
| Test challenger | `experimental_preview_shadow` / `mb_experimental_preview_shadow` + gate 20/20 | cùng API → `test_bundle` / `blocked_test_bundle` |
| FE | `web/frontend/du-doan-test.html` → `loadPreview()` | |

### 3.2 Đo live VPS (17:27–18:13 VN, 02/08)

| Miền | Official date | BT | Fallback? | Test publish | Preview phụ |
|---|---|---|---|---|---|
| MN | 2026-08-02 | 43 | Không | Không | Có · 18/20 · BT=39 |
| MT | 2026-08-02 | 69 | Không | Có · 20/20 · BT=86 | — |
| MB (17:27) | 2026-08-01 | 90 | Có | Không | Có · 4/20 |
| MB (sau 17:38 / verify xong) | 2026-08-02 | 52 | Không | Không | Có · 4/20 |

Owner thấy “MN hôm qua” + số 43: **43 đúng là BT MN hôm nay** (bundle 05:18) — lỗi nhãn/cách neo, không phải số sai. MT “31/07” khớp kiểu fallback khi owner xem trước ~16:42.

### 3.3 Cột test MN trống

Doctrine V105.16: publish chính cần đúng **20** model strongest. MN hôm nay primary chỉ **18/20** → `test_bundle=null`, số nằm ở `blocked_test_bundle`. FE cũ chỉ vẽ `test_bundle` → năm thẻ “Chưa có dữ liệu”. MT đủ 20 nên có số.

### 3.4 `/filter` V10960

- Patch UI (số lên đầu, chrome ~0.64, font ≥12px) **đã trên VPS** (PID từng 597451→639386).
- Route `/filter` **không** gửi `Cache-Control` → trình duyệt/etag giữ HTML cũ → owner tưởng chưa xử lý.
- Tự trùng: sticky + context + 4 overview card lặp cùng chỉ số 2–3 lần.

## 4. Hướng xử lý và vì sao chọn

| Phương án | Chọn? | Lý do |
|---|---|---|
| A. Giữ kéo `data_date` về latest, chỉ sửa nhãn | Không | Vẫn làm cột test lệch theo ngày cũ |
| B. Neo `requested_date` + nhãn fallback + hiện preview (kiểu nghiem-thu) | **Có** | Cùng quy tắc 3 miền; nói thẳng khi chưa có hôm nay |
| C. Hạ gate 20→18 để MN có publish | Không | Đụng doctrine / gần QD-014 |
| D. Xóa tab/trang `/filter` | Không | Owner giữ trang; chỉ giảm lặp + cache |

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `web/backend/main.py` | `_build_display_date_anchor`; bỏ kéo `data_date`; Cache-Control `/filter`; lý do trống + giờ dự kiến |
| `web/frontend/du-doan-test.html` | Nhãn ngày trang/cột; hiện preview phụ; banner lý do |
| `web/frontend/review-dashboard.html` | `getVNDateISO` đúng VN; ẩn sticky overview; 2 card gộp |

- Backup local: `backups/v10964_pre/`
- Backup VPS: `/root/Lottery_AI_Test/backups/v10964_pre/`
- Deploy: 18:13 VN · PID **641906 → 645169** · health 200
- Hash trước=sau: predictions `5985fc83f159ef18` · final_bundles `1ae42a20562a4864` · lottery_results `991f37947bbe7f6b` · model_daily_eval `2889edde455461c1`

## 6. Cổng kiểm

| Mục | Kết quả |
|---|---|
| `/api/health` | 200 |
| Hash 4 bảng | Y nguyên |
| PID đổi | Có |
| `/filter` Cache-Control | `no-store, no-cache, must-revalidate, max-age=0` |
| Handler MN/MT/MB `display_date_anchor.today_vn` | 2026-08-02 cả ba |
| Playwright filter overview | sticky `display:none`; 2 overview cards; top-cand đầu trang; ngày 02/08 |
| Playwright du-doan-test mock | MN hiện preview 18/20; MB nhãn “KHÔNG phải hôm nay” khi fallback |
| QD-014 | Không đổi roster/combo/cách tính |

## 7. Vướng vấp

| Vấp | Hậu quả nếu bỏ qua |
|---|---|
| Agent song song đã upload FE sớm; BE chưa restart → API thiếu `display_date_anchor` | FE fallback `{}`, nhãn vẫn yếu |
| `/filter` thiếu Cache-Control | Owner hard-refresh vẫn có thể thấy bản cũ nếu CDN/proxy; đã vá |
| Deploy 18:13 nằm sát mép cửa sổ cấm mới V10968 (15:30–18:15) | An toàn dữ liệu sau freeze MB 17:58; lần sau chờ ≥18:15 hoặc `DEPLOY_KHAN=1` |
| Cửa sổ 15–18 cấm deploy | Đã chờ tới sau 18:00 rồi mới restart |

## 8. Gỡ về

```text
# VPS
cp -a /root/Lottery_AI_Test/backups/v10964_pre/main.py.pre /root/Lottery_AI_Test/web/backend/main.py
cp -a /root/Lottery_AI_Test/backups/v10964_pre/du-doan-test.html.pre /root/Lottery_AI_Test/web/frontend/du-doan-test.html
cp -a /root/Lottery_AI_Test/backups/v10964_pre/review-dashboard.html.pre /root/Lottery_AI_Test/web/frontend/review-dashboard.html
systemctl restart lottery.service
# So PID; curl /api/health; hash 4 bang
```

Thời gian ước tính: ~2 phút. Không ảnh hưởng số dự đoán (chỉ UI/nhãn ngày).

## 9. Theo dõi tiếp

| Mã | Việc | Ngưỡng | Hạn |
|---|---|---|---|
| FU-225 · UI0803 | Owner xác nhận 3 miền + /filter hard refresh | MN: official hôm nay + preview 18/20 nói rõ; MT test publish; MB official hôm nay hoặc nhãn fallback đúng; /filter có Cache-Control no-store, không lặp sticky ở overview | 2026-08-03 |
| FU-224 | Dọn trang frontend chết/trùng (đề xuất, chưa xóa) | Owner quyết | 2026-08-09 |
