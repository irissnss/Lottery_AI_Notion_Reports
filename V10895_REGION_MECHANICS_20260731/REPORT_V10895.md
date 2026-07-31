# V10895 — `/nghiem-thu` trống + ba miền ba cơ chế dự đoán khác nhau

**31/07/2026** · commit private `a2a3bbd` · hash 4 bảng IDENTICAL

---

## Owner yêu cầu

> *"Điều kiện đắt đầu dự đoán lại cho MT và MB có rồi nha đừng có quên, là sau khi cào và verify dự đoán, còn việc nạp sameday cho từng miền thì hiện tại từng cơ chế 1 mỗi miền mỗi khác phải làm cho rõ cho kỹ nha. Đừng có mơ hồ, các mốc thời gian, tổng hợp học tập tích lũy số liệu điều phải chính xác không mơ hồ nha em. MN thì thời gian dài hơn sau 5h sáng hàng ngày bắt đầu dự đoán cho MN là an toàn nhất giờ đó hệ thống không còn tổng hợp, retrain, gì nữa, là đầy đủ nhất rồi. Hạn total output MN 15h45 quá dài quá thong thả rồi khoản thời gian này để sáng anh làm việc có điều chỉnh gì vẫn update kịp không ảnh hưởng hệ thống. Hiện output https://xs.io.vn/nghiem-thu chả thấy đâu em?"*
> — 31/07 14:01

---

## 1. `/nghiem-thu` trống — hai nguyên nhân chồng nhau

### (a) Cron chưa từng chạy hôm đó

Dòng cron `04:25` và `04:35` cho MN **mới được thêm lúc 11h sáng 31/07** (trong phiên V10891 dời lịch). Lúc 04:25 sáng nó chưa tồn tại.

Bằng chứng: log `logs/v10879_nghiemthu.log` sửa lần cuối **30/07 21:16:01**. Nếu cron chạy sáng nay thì log đã được ghi thêm.

Số MN 31/07 có trong DB (`09:25:36`) là do **chạy tay** trong phiên kiểm buổi sáng, không phải cron.

### (b) Giao diện nuốt mất hai miền

`_today_cards` gặp miền chưa có số thì `continue`. Khối tiêu đề **"Hôm nay — 3 miền"** vì thế chỉ hiện **Miền Nam**. Người xem không phân biệt được "hệ hỏng" với "chưa tới giờ chạy".

Thêm nữa khối này nằm **dưới** bảng đối chứng lịch sử 25 dòng, phải cuộn rất xa mới thấy.

### Đã sửa

- Luôn trả **đủ ba miền**. Miền chưa tới giờ hiện thẻ nét đứt: *"Có số lúc 16:44 · final 16:53"* kèm lý do (`official chưa chốt miền này`) và giờ xổ.
- Tiêu đề có bộ đếm: **"1/3 đã có số"**.
- Khối hôm nay chuyển lên **đầu trang**, ngay dưới phần kết luận.

Kiểm bằng Playwright với **đúng payload live** ở 390px và 1440px: không tràn ngang, không tràn trong, 0 lỗi JS, đủ 3 miền, 8 bảng 173 dòng.

---

## 2. Ba miền ba cơ chế — bảng đối chiếu

| | **MN** | **MT** | **MB** |
|---|---|---|---|
| ML 04:00 ghi | 7 model | 7 model | 7 model |
| Chuỗi AI sáng | **có** — tới 15 model lúc 04:17–04:19 | không | không |
| Số 04:00 có được giữ? | **giữ, là bản cuối** | **giữ, là bản cuối** | **BỊ XOÁ** |
| Re-predict trong ngày | **không bao giờ** | **không bao giờ** | **có** — `rerun_post_mt` 17:30 |
| Chuỗi AI chiều | không | 16:35–16:43, 8 model | 17:31–17:35, 8 model |
| Nạp same-day miền khác | không có gì để nạp | chỉ qua chuỗi AI chiều | **MN + MT**, cả ML lẫn AI |
| Bundle official chốt | 04:17–04:19 · 14–15 model | 16:37–16:43 · 11–13 model | 17:33–17:35 · 13–14 model |
| Cào kết quả | 16:34–16:39 | 17:30–17:32 | 18:31–18:32 |
| **FINAL output** | **15:45:00** | **16:53:00** | **17:53:00** |

**Tóm gọn:** MN chốt xong từ sáng sớm và không bao giờ đổi. MT chốt số ML từ sáng, chiều chỉ thêm chuỗi AI. MB vứt bỏ hoàn toàn số buổi sáng, làm lại từ đầu lúc 17:30 khi đã có kết quả MN và MT.

---

## 3. Điều kiện bắt đầu dự đoán lại — MT và MB

Owner nhắc đúng: *"sau khi cào và verify dự đoán"*. Chi tiết đủ để đối chiếu:

| Miền vừa cào xong | Re-predict cho miền nào | `run_source` |
|---|---|---|
| **MN** (16:34–16:39) | **chỉ MB** | `rerun_post_mn` |
| **MT** (17:30–17:32) | **chỉ MB** | `rerun_post_mt` |
| **MB** (18:31–18:32) | không gọi — hết ngày | — |

### Vì sao MT không được re-predict

Quyết định có đo, ghi thẳng trong code (V10766):

> Re-predict MT sau khi cào MN **làm hại MT** (đo 45 ngày + 14 ngày, bền cả hai nửa): MT bản-sau +1,6 triệu so với bản-trước (04:00) +16,3 triệu/45 ngày. Riêng ML: +16,3 → +45,7 triệu/45 ngày. Nạp kết quả MN cùng ngày vào MT là **nhiễu**.

Cờ tắt/bật: `_V10766_SKIP_MT_REPREDICT = True`.

### Cổng verify

`verify_prediction` **chỉ chạy khi bộ đài ĐỦ** (`_cov_flag == "COMPLETE"`). Thiếu đài thì hoãn sang lượt cào lại **T+20 phút**, lượt đó luôn gọi `force_reverify=True` nên verify chắc chắn xảy ra.

Lý do có cổng: sự cố MN 04/11 — hệ đóng dấu THẮNG/THUA khi bộ đài chưa đủ. **Cổng chỉ hoãn verify** — re-predict và chuỗi AI vẫn chạy bình thường.

### Chuỗi AI chiều

- AI predict MT **16:42** — sau cào MN 16:30 → verify → re-predict miễn phí
- AI predict MB **17:42** — sau cào MT 17:30 → verify → re-predict miễn phí

---

## 4. Nạp same-day — mỗi miền một kiểu

### MN — không nạp gì, và không thể nạp

MN xổ **đầu tiên** (~16:15). Lúc MN dự đoán (04:00–04:19) chưa có kết quả nào của ngày hôm đó. MN chỉ dùng dữ liệu **D-1 trở về trước**, trong đó MB D-1 đã cào xong 18:31 hôm trước — nên D-1 **trọn vẹn**.

Đo 11 ngày: MN chỉ có `auto_daily` (04:00:04–04:19:04, 15 model) và `shadow_auto_eval` (không tính output). **Không một dòng re-predict nào.**

### MT — nạp same-day chỉ qua chuỗi AI chiều

- ML 04:00 ghi 7 model bằng dữ liệu **D-1**, giữ nguyên tới cuối ngày.
- Chuỗi AI 16:35–16:43 ghi thêm 8 model, chạy **sau khi cào MN** nên phần AI **có** thấy kết quả MN cùng ngày.

MT là bản **lai**: nửa ML dùng dữ liệu hôm qua, nửa AI dùng dữ liệu hôm nay.

### MB — nạp đầy đủ nhất, vứt bỏ bản buổi sáng

- ML 04:00 ghi 7 model rồi **bị xoá**. Có `DELETE FROM predictions WHERE date=? AND target_region=? AND ai_model=?` trong `scheduler.py`.
- 17:30 `rerun_post_mt` ghi lại 7 model với MN + MT cùng ngày trong tay.
- 17:31–17:35 chuỗi AI ghi 8 model, cũng thấy đủ.

**Bằng chứng bản sáng bị vứt:** đo 12 ngày, chỉ **31/07 còn thấy** `auto_daily 04:00:08` — vì lúc đo (14:0x) MT chưa xổ nên chưa có gì xoá nó. Cả 11 ngày trước đó không còn dòng nào.

---

## 5. Mốc học tập / tích luỹ — chính xác từng giờ

| Việc | Lịch | Bằng chứng |
|---|---|---|
| Retrain 4 model × 3 miền | **CN 02:00** | `lstm_MN.pt` đổi 26/07 **02:01:50** · `lstm_MT.pt` 02:02:14 · `lstm_MB.pt` 02:02:33 |
| Weight optimizer | **CN 03:00** | marker `.last_optimizer_run` = 26/07 **03:14:32** |
| Đào rule tuần | **T2 00:30** | ghi `mined_rules` |
| Kế hoạch giới hạn AI cho MN | **03:50** | ghi `mn_ai_limit_plan` — **trước** MN dự đoán |
| Chấm điểm model theo ngày | **20:20** mỗi tối | `model_daily_eval` 77–81 dòng/ngày |
| Xếp hạng rule MN/MT | 04:40 | đọc `mined_rules` — **không ghi bảng nào** |
| Chọn champion | 06:00 | ghi `champion_selector_shadow`, `play_recommendation_shadow` — **cả hai đều shadow** |
| Retrain guard dự phòng | 06:30 | ghi `ml_retrain_guard_log`; chỉ kích hoạt khi model ≥8 ngày |

### Bẫy: `training_history` lưu giờ UTC

Bảng ghi `2026-07-25 19:02:41` cho lượt retrain, file model đổi lúc `2026-07-26 02:01–02:02`. **Lệch đúng 7 tiếng.**

Retrain chạy **Chủ nhật 02:00 giờ VN** như thiết kế. Ai đọc bảng này mà tưởng là giờ VN sẽ kết luận sai rằng retrain chạy **thứ Bảy 19:02**.

Kiểm 12 lượt liên tiếp — 25/07, 18/07, 11/07, 04/07, 27/06, 20/06, 13/06, 06/06, 30/05, 23/05, 16/05, 09/05 — tất cả đều 19:00–19:02 UTC, cách nhau đúng 7 ngày.

---

## 6. "Dự đoán MN sau 5h sáng" — đo rồi mới làm

### Kiểm mọi việc chạy sau 04:19

| Chạy sau MN | Ghi vào đâu | MN có đọc không |
|---|---|---|
| Rule ranker 04:40 | **không ghi bảng nào** (chỉ đọc) | không |
| Champion selector 06:00 | `champion_selector_shadow`, `play_recommendation_shadow` | không — đều shadow |
| Retrain guard 06:30 | `ml_retrain_guard_log` | không — chỉ log |

Retrain (CN 02:00), optimizer (CN 03:00), đào rule (T2 00:30), kế hoạch giới hạn AI (03:50) — **tất cả xong trước 04:00**.

### Kết luận trung thực

Về **dữ liệu**, MN lúc 04:00 đã có đủ; dời sang sau 5h **không thêm được gì**. Nhưng nguyên tắc của owner vẫn có giá trị về **an toàn vận hành**: hạn 15:45 còn cách hơn 10 tiếng, chạy muộn hơn không mất gì mà tránh mọi va chạm với khối 04:xx.

### Đã làm

Lane Nghiệm Thu MN dời **04:25 → 05:05** (lượt chính) và **04:35 → 05:15** (lượt cứu). Sau mốc 05:00, cùng khối với doctrine shadow 05:00 và prompt-v2 05:10. Hằng số `LANE_SCHEDULE` trong lane khớp cron nên trang web hiển thị đúng giờ.

### Chưa làm — cần owner quyết

Chuỗi dự đoán MN chính (ML 04:00 + AI 04:0x–04:19) **giữ nguyên**, vì đo cho thấy dời không thêm dữ liệu mà lại đụng vào lõi sản xuất.

---

## 7. Tài liệu chống quên

**`docs/CO_CHE_DU_DOAN_TUNG_MIEN.md`** — bảng đối chiếu ba miền, điều kiện re-predict, cơ chế same-day từng miền, mốc học tập chính xác từng giờ, bẫy UTC, và **thủ tục bắt buộc khi thêm/đổi luồng**:

1. Đổi giờ cron lane thì phải sửa **cả** `LANE_SCHEDULE` trong lane — trang lấy giờ từ hằng số đó.
2. Thêm luồng đọc `predictions` phải biết miền nào có `run_source` nào. Đọc MB mà không lọc `rerun_post_mt` là lấy nhầm bản đã bị xoá.
3. Đọc `training_history` phải cộng 7 tiếng.
4. Mọi luồng mới phải ghi xong trước mốc lane (15:41 / 16:50 / 17:50).

Playbook §1 và §Chuỗi mốc trỏ về trang này.

---

## 8. Xác minh

| Mục | Kết quả |
|---|---|
| Hash 4 bảng chính | **IDENTICAL** trước-sau |
| `/api/health` · `/du-doan` | 200 · 200 |
| `/nghiem-thu` · `/api/nghiem-thu` | 401 · 401 (cổng admin đúng) |
| md5 `nghiem-thu.html` | **KHỚP** local-VPS, chứa 6/6 dấu hiệu mới |
| Playwright 390px + 1440px | không tràn, 0 lỗi JS, đủ 3 miền |
| Chạy thử lane MN đúng lệnh cron mai gọi | `ĐÃ CHỐT TRƯỚC ĐÓ · 09` — đóng băng đúng, không ghi đè |

**Rollback:** `crontab /root/Lottery_AI_Test/.local_backup_v10895_crontab_20260731_141740.txt`

**Follow-up:** `FU-V10895-REGION-MECHANICS` — xác minh **01/08 05:05** lượt cron MN đầu tiên phải ra số; 31/07 16:44 MT, 17:38 MB; sáng 01/08 mở `/nghiem-thu` phải thấy đủ 3 miền.
