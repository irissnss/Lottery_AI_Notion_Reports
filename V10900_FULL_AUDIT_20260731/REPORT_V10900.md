# V10896→V10900 — Rà soát toàn bộ theo yêu cầu owner + bộ tự kiểm nhất quán

**31/07/2026** · commit private `3470aec` · hash 4 bảng IDENTICAL qua 5 lượt deploy

> Owner 15:17: *"Anh hết tin tưởng em rồi, quá cẩu thả, chểnh mảng, thiếu tư duy... hầu như ngày nào cũng đào ra lỗi, chả có cái nào mà ổn định chính xác là sao vậy? Em không thấy em làm việc rất vô trách nhiệm ah, làm cho có sao tốn token lãng phí ah. Anh cần em rà soát lại thật kỹ toàn bộ, báo cáo đầy đủ showlist tất cả dùm anh để anh xem lại."*

Showlist đầy đủ nằm trong repo private: `docs/SHOWLIST_RA_SOAT_TOAN_BO_20260731.md`. Báo cáo này là bản công khai tóm các phần chính.

---

## 1. Lỗi của chính agent — 13 mục

Owner nói đúng. Liệt kê thẳng, không giảm nhẹ.

| # | Sai gì | Hậu quả |
|---|---|---|
| A1 | Bộ đo độ trễ job trừ **giờ ghi cũ** cho **giờ cron mới** | Ra 600–1500 giây vô nghĩa, suýt đặt biên an toàn sai |
| A2 | Khẳng định *"D-1 trọn vẹn lúc 04:00"* mà không đo | Owner phải tự chất vấn mới lộ |
| A3 | Bộ dò UTC #1 theo *"nhiều bản ghi rơi khung 17–23h"* | Nhiễu nặng; gán nhầm `model_daily_eval` 20:20 VN là UTC |
| A4 | Bộ dò UTC #2 theo *"gần giờ VN hay UTC hơn"* | Sai với mọi bảng ghi 1 lần/ngày; **gán nhầm `predictions` là UTC** |
| A5 | Bộ dò UTC #3 theo schema có `DEFAULT CURRENT_TIMESTAMP` | Không phải bằng chứng — 29/42 bảng luôn truyền tay giá trị |
| A6 | Bộ dò UTC #4 theo khuôn chuỗi `YYYY-MM-DD HH:MM:SS` | `datetime.now().strftime()` trên VPS múi giờ VN sinh **đúng khuôn đó**; gán `final_bundles` là UTC dù bundle MT 16:37 mà MT xổ 17:15 |
| A7 | Bộ dò default cắt giữa `(datetime('now'` | Mất phần `,'localtime'` — chính chỗ quyết định |
| A8 | Dò trường prompt trong trace bằng tên đoán | Báo "không có prompt" trong khi bản ghi có đủ |
| A9 | Kiểm `/choi` `/monitoring` bằng `curl` trần | Nhận trang 401 rồi báo "thiếu nội dung" |
| A10 | Đường dẫn `frontend` sai khi chép script | Playwright báo "0 thẻ render" giả |
| **A11** | **Đổi mốc FINAL ở chốt chặn + tài liệu + UI nhưng KHÔNG rà code còn lại** | **`/choi` hiện HAI con số hạn khác nhau suốt từ V10894 tới V10900** |
| **A12** | Dời chuỗi MN nhưng không cập nhật `LANE_SLOT` | Bản kiểm 20:45 dò lane MN ở 04:30 trong khi đã sang 05:30 |
| A13 | Bộ dò tên script chỉ tìm đuôi `.py`/`.sh` | Bỏ sót dòng cron gọi `-m lane._v10637_lane_v2_daily` |

### Hai bài học, đã biến thành cơ chế chứ không chỉ hứa

**Bài học 1 — đừng kết luận bằng phỏng đoán gián tiếp.** Bốn bộ dò UTC liên tiếp sai vì đều là suy luận vòng. Chỉ khi đọc **chính biểu thức code sinh ra giá trị** mới đúng, và khi đó khớp cả **5 mỏ neo độc lập**.

**Bài học 2 — đổi một con số thì phải rà hết chỗ giữ con số đó.** Đây là gốc của việc "ngày nào cũng đào ra lỗi". Tài liệu không chặn được, nên đã dựng bộ tự kiểm hằng ngày — mục 6.

---

## 2. MN CÓ đọc D-1 cả ba miền — chứng minh ba lớp

Owner nghi MN dự đoán bằng dữ liệu cũ, chưa có D-1: *"4h19 mới có dữ liệu mà dự đoán lúc 4h cũng có đúng đâu? Anh nhớ MN phải có sameday D-1 mà, sameday của MN là D-1 vì miền nam đầu ngày mà."*

**Lớp 1 — dữ liệu vào kho từ khi nào (13 ngày):** D-1 của cả ba miền ghi xong từ tối trước — MN 16:34–16:39, MT 17:30–17:32, **MB 18:31–18:32**. Sớm hơn lúc MN dự đoán khoảng **9,5 tiếng**. Không ngày nào D-1 về sau 04:00, không kết quả nào ghi sang ngày hôm sau.

**Lớp 2 — phía ML (7 model):** `meta_data_collector._get_cross_region_momentum` đã có cổng thứ tự xổ V10667:

```
_DRAW_ORDER = {'MN': 1, 'MT': 2, 'MB': 3}
earlier_src = miền xổ TRƯỚC target  → được dùng same-day (date <= target)
later_src   = miền xổ SAU target    → BUỘC dùng date < target
```

Với MN (thứ tự 1) thì MT và MB đều là `later_src` → code **ép** `date < hôm nay` = lấy tới hết D-1. Đúng y như owner nói *"sameday của MN là D-1"*.

**Lớp 3 — phía AI (8 model), đọc trace thật:**
- `strongest_source_prizes_used`: `["MB(D-1/T5) Hà Nội G6+G7 → 64, 95", "MB(D-1/T5) Hà Nội GĐB+G6 → 64, 95"]`
- `candidate_support_map`: `"34": ["Hà Nội ĐB(D-1)=34, có mirror 43", …]`
- 11/15 model official dẫn chứng D-1 bằng chữ; cả 15 nhận đủ **17 rule** như nhau

**Kết luận: dữ liệu MN không thiếu.** Nhưng owner đã chỉ đạo dời và đã dời — mục 3.

---

## 3. Dời chuỗi MN sang sau 5h (hiệu lực 01/08)

Đổi **2 cài đặt** và **9 mốc cron**:

| Giờ mới | Việc | Giờ cũ |
|---|---|---|
| 04:50 | kế hoạch giới hạn AI MN | 03:50 |
| **05:00** | **ML 7 model, cả 3 miền** (`free_predict_time`) | 04:00 |
| **05:15** | **chuỗi AI MN 8 model** (`ai_predict_mn_time`) | 04:15 |
| ~05:17–05:19 | bundle MN chốt | ~04:17–04:19 |
| 05:30 | lane v10692 MN | 04:30 |
| 05:35 | output final lab | 04:40 |
| 05:40 | rule ranker | 04:40 |
| 05:50 | doctrine shadow MN | 05:00 |
| **06:05** | **Nghiệm Thu MN lượt chính** | 04:25 |
| 06:10 | prompt v2 MN | 05:10 |
| 06:15 | Nghiệm Thu MN lượt cứu | 04:35 |
| 06:25 | champion selector | 06:00 |

**Vì sao phải dời cả 9 job:** 6 job có truy vấn `final_bundles ... date = ?` của chính ngày đó. Chỉ dời dự đoán mà quên chúng thì chúng chạy **trước** lúc bundle chốt → cổng đóng → không ra số, đúng lỗi vừa sửa ở V10895.

**Tác động ngoài MN — phải nói rõ:** `free_predict_time` điều khiển ML cho **cả ba miền**, nên số ML buổi sáng của MT và MB cũng dời sang 05:00. Vô hại vì hạn MT 16:53 / MB 17:53 còn rất xa, và số ML của MB dù sao cũng bị xoá lúc 17:30.

Scheduler xác nhận: `Free Model Auto-Predict: hàng ngày lúc 05:00` · `AI Auto-Predict: MT=16:42, MB=17:42, MN=05:15`.

---

## 4. Xác định dứt điểm 33 bảng lưu giờ UTC

### Cách phân biệt — thử thật, không phỏng đoán

| Biểu thức default | Sinh ra |
|---|---|
| `CURRENT_TIMESTAMP` | **UTC** |
| `datetime('now')` | **UTC** |
| `datetime('now','localtime')` | **giờ VN** |
| `datetime('now','+7 hours')` | **giờ VN** |

Cột chỉ lưu UTC khi default là UTC **và** lệnh INSERT bỏ qua cột. Nếu code truyền tay `vn_now()` thì vẫn ra giờ VN.

### Bốn bảng hash-guard KHÔNG bị ảnh hưởng — điểm quan trọng nhất

| Bảng | Cơ chế | Kết luận |
|---|---|---|
| `predictions` | code truyền `vn_now()` → hậu tố `+07:00` | **giờ VN** |
| `final_bundles` | default `datetime('now','localtime')` | **giờ VN** |
| `lottery_results` | code truyền `vn_now()` → hậu tố `+07:00` | **giờ VN** |
| `model_daily_eval` | default `datetime('now','localtime')` | **giờ VN** |

→ **Mọi phân tích mốc giờ trong ngày dựa trên bốn bảng này là đúng.**

### 33 bảng thật sự lưu UTC

Lớn nhất: `scheduler_logs` **232.154 dòng**; rồi `prompt_section_breakdown_daily` 35.419 · `source_prize_effectiveness_daily` 8.567 · `verdict_distribution_daily` 7.902 · `prompt_pressure_daily` 5.381 · `runtime_reliability_model_daily` 4.110 · `mined_rule_effectiveness` 3.143 · và 26 bảng nhỏ hơn, trong đó có `training_history` 216 dòng (bảng gây nhầm ban đầu) và `daily_eval_log` 389 dòng.

Hai mỏ neo kiểm chéo khớp hoàn hảo: `daily_eval_log` ghi `13:00` UTC = **20:00 VN**, đúng cài đặt `daily_eval_time=20:00`. `training_history` ghi `25/07 19:02` UTC = **26/07 02:02 VN**, khớp mtime file `lstm_MN.pt` là `02:01:50`.

**Chờ owner quyết:** owner từng chọn phương án "chuyển hết sang giờ VN" khi cả hai còn tưởng chỉ có **một** bảng. Thực tế 33 bảng, SQLite không cho đổi `DEFAULT` nên phải dựng lại từng bảng. Ba mức đề xuất trong showlist Phần E.

---

## 5. Xoá mốc giờ CŨ ở 4 file live

| File | Hằng số | Cũ | Mới |
|---|---|---|---|
| `_v10759_money_board.py` | `OUTPUT_DUE` (đẩy thẳng ra `/choi`) | 15:55/16:55/17:55 | **15:45/16:53/17:53** |
| `_v10861_runtime_contract_audit.py` | `DEADLINE` | 15:55/16:55/17:55 | **15:45/16:53/17:53** |
| `_v10861_runtime_contract_audit.py` | `LANE_SLOT` | MN 04:30 · MT 16:53 · MB 17:52 | **MN 05:30 · MT 16:45 · MB 17:39** |
| `_v10692_mn_mt_multidir_lane.py` | `OUTPUT_FREEZE_HHMM` | 15:55/16:55/17:55 | **15:45/16:53/17:53** |
| `database.py` | hạt giống `free_predict_time` · `ai_predict_mn_time` | 04:00 · 04:15 | **05:00 · 05:15** |

### Quyết định có chủ ý — `CUTOFF` KHÔNG ép bằng FINAL

`CUTOFF = {"MN":16.0,"MT":17.0,"MB":18.0}` là chặn **nhìn-trước** (bundle phải tạo trước **giờ xổ** 16:15/17:15/18:15). FINAL là **hạn output đủ**. Hai việc khác nhau.

Đo trước khi quyết: siết `CUTOFF` về mốc FINAL sẽ loại **1 bundle MT ngày 02/04/2026 (16:54:10, BT=21, 15 model)** khỏi chuỗi P&L — đổi số P&L quá khứ mà không được lợi gì về tính đúng. **Giữ nguyên**, và ghi chú ngay trong code để lần sau không ai ép bừa.

---

## 6. Bộ tự kiểm nhất quán — chặn gốc loại lỗi này

`_v10900_consistency_guard.py`, cron **18:05 hằng ngày**, 7 phép kiểm:

| Phép kiểm | Bắt được lỗi gì |
|---|---|
| C1 `_v10759_money_board.OUTPUT_DUE` khớp FINAL | `/choi` hiện hai con số hạn khác nhau (chính lỗi A11) |
| C2 `_v10861.DEADLINE` khớp FINAL | bản kiểm 20:45 chấm theo hạn cũ |
| C3 `_v10692.OUTPUT_FREEZE_HHMM` khớp FINAL | lane còn cho ghi sau hạn thật |
| C4 khoá `/choi` chạy trước FINAL | mốc FINAL mất nghĩa "đã xong" |
| C5 giờ lane Nghiệm Thu khai báo khớp crontab | trang web hiện sai giờ có số |
| C6 `LANE_SLOT` khớp crontab lane v10692 | bản kiểm dò sai giờ rồi báo thiếu oan (lỗi A12) |
| C7 cài đặt đang chạy khớp hạt giống `database.py` | khởi tạo DB mới âm thầm quay về giờ cũ |

Chạy thử hôm nay: **7/7 đạt**. Bảng `v10900_consistency_guard` · API `/api/admin/consistency-guard` (401 admin) · panel viền tím trên `/monitoring`, đăng ký cả `loadAllSections()` và `setInterval`.

Tài liệu không chặn được lỗi "đổi một chỗ quên chỗ khác". Chỉ máy kiểm mỗi ngày mới chặn được.

---

## 7. Hai câu treo, đã trả lời

**Khoá `/choi` MN hôm nay ghi lúc 08:04:10, sao sớm hơn cron 15:43 nhiều vậy?**

Do `compute_board()` được gọi từ API `/api/admin/money-board` — khoá sinh **ngay lần đầu ai mở `/choi` trong ngày**; cron 15:43 chỉ là chốt hậu. Giờ khoá MN 14 ngày rải rác 05:41 → 16:00 đúng theo lúc admin mở trang.

**Có an toàn với lịch MN mới không?** Có, logic fail-safe: chưa có bundle → `trow=None` → `songthu=None` → **nhánh ghi khoá bị bỏ qua**. Mở `/choi` lúc 05:10 (trước bundle 05:17) **không** tạo khoá rỗng; khoá sẽ sinh ở lần mở sau hoặc chậm nhất cron 15:43.

**Hai dòng cron 00:16 và 14:30 là gì?**

00:16 là cron hệ thống aaPanel (`/www/server/cron/a50afd8f…`), không thuộc mã dự án. 14:30 là `python3 -m lane._v10637_lane_v2_daily` — bộ dò chỉ tìm đuôi `.py`/`.sh` nên bỏ sót dạng gọi module.

---

## 8. Xác minh

| Mục | Kết quả |
|---|---|
| Hash `predictions`/`final_bundles`/`lottery_results`/`model_daily_eval` | **IDENTICAL** qua **5 lượt deploy** |
| `/api/health` · `/du-doan` | 200 · 200 |
| `/choi` · `/monitoring` · `/nghiem-thu` | 401 · 401 · 401 (cổng admin đúng) |
| `/api/admin/consistency-guard` · `/api/admin/deadline-guard` | 401 · 401 |
| md5 mọi file đẩy | **KHỚP** local-VPS |
| Chốt chặn hạn hôm nay | **17 đúng hạn · 0 trễ · 4 chưa tới giờ** |
| Bộ tự kiểm nhất quán | **7/7 đạt** |

---

## 9. Cần owner quyết + cần theo dõi live

**Cần quyết:** 33 bảng lưu UTC — chọn mức 1 (chỉ ghi tài liệu, không đụng dữ liệu) / mức 2 (chuyển `training_history` 216 dòng) / mức 3 (chuyển hết, kể cả `scheduler_logs` 232k dòng, cần phiên riêng).

**Theo dõi live:** 31/07 **16:53** MT final · **17:53** MB final · **18:02** chốt chặn hạn phải 0 trễ · **18:05** bộ tự kiểm phải 7/7 · **01/08 05:00→06:15** chuỗi MN mới chạy lần đầu · **01/08 sáng** mở `/choi` `/nghiem-thu` `/monitoring` kiểm mắt.

**Rollback:** `crontab /root/Lottery_AI_Test/.local_backup_v10900_crontab_20260731_153846.txt` · cài đặt: `.local_backup_v10897_appsettings_*.sql`

**Follow-up:** `FU-V10900-CONSISTENCY`
