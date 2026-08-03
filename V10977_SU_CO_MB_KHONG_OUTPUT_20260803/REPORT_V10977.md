# V10977 — MB `/nghiem-thu` mất trắng một ngày đo vì cổng mở SAU khi hết lượt chạy

**Ngày:** 03/08/2026 · **Trạng thái:** ĐÃ SỬA + ĐÃ DEPLOY · **Loại:** (A) không có dữ liệu thật

---

## 1. Tóm tắt

Ngày 03/08 luồng **Nghiệm Thu** (`/nghiem-thu`) **không có số cho MB**. Official MB thì **có bình
thường** — `final_bundles` id=641, bạch thủ **59**, lo2 `["59","52"]`, 14 model, chốt **17:44:54**.
Nguyên nhân gốc: lane chỉ chạy hai lượt **17:38** và **17:42**, còn cổng `_official_gate` chỉ mở
khi official đã chốt miền đó — mà hôm nay official chốt lúc **17:44:54**, tức **muộn hơn lượt chạy
cuối 2 phút 53 giây**. Cả hai lượt đều ghi `CHƯA ĐỦ ĐIỀU KIỆN · official chưa chốt miền này` rồi
thoát, và không còn lượt nào để bù.

Biên an toàn đã mỏng từ trước chứ không phải hỏng đột ngột: **02/08 lane chỉ hơn official 9 GIÂY**
(official 17:37:53 · lane 17:38:02), 01/08 phải nhờ lượt vá 17:42. Giờ official chốt MB đo 34 ngày
trôi từ **17:33:00 đến 17:44:54** theo độ trễ nhà cung cấp — hôm nay là ngày trôi xa nhất và biên
hết chỗ.

Đã sửa và deploy trong phiên: thêm lượt vá **MB 17:46 · 17:50 · 17:54** và **MT 16:52 · 16:54**
(đều ≤ biên lane), sửa mốc FINAL còn nợ từ V10931 (MT `16:53→16:58`, MB `17:53→17:58`) ở cả lane
lẫn `/monitoring`, thay nhãn trang từ *"chưa tới giờ"* sai sự thật sang **"LỠ HẠN"** kèm giờ
official chốt, và thêm **hai phép tự kiểm C17/C18** (16 → 18 phép) để lần sau máy kêu trước owner.
**Không sinh số bù cho MB 03/08** — đã quá mốc FINAL 17:58 và đã xổ ~18:31, quy tắc đóng băng cấm.
Hash 4 bảng khoá **giữ nguyên tuyệt đối**.

---

## 2. Owner yêu cầu gì (nguyên văn)

Owner, **03/08/2026 19:03** (giờ VN):

> *"MB /nghiem-thu này không output là sao em? ly do gi sao ma tao lao the em? Riet em mat kiem
> soat dan thi phai"*

Owner **không chọn phương án nào** — owner báo sự cố và nêu mối lo lớn hơn: hệ đang mất kiểm soát
dần, owner phải là người phát hiện thay vì máy. Toàn bộ hướng xử lý bên dưới do agent đề xuất.

---

## 3. Đào bới / phát hiện

Đo trực tiếp trên VPS `14.225.224.89`, DB `/root/Lottery_AI_Test/data/lottery_ai.db`, giờ máy VN
`2026-08-03 19:08:43`. Đã tra `tz_registry` trước khi đọc dấu thời gian: `final_bundles.created_at`,
`predictions.created_at`, `du_doan_test_bundles.created_at` đều **stored_tz = VN** → đọc thẳng;
riêng `scheduler_logs.log_time` là **UTC** (view `v_scheduler_logs_vn`).

### 3.1 MB hôm nay CÓ output official, KHÔNG có output Nghiệm Thu

| Bảng | MN | MT | MB |
|---|---|---|---|
| `final_bundles` (official) | BT **64** · 15 model · **05:20:15** | BT **64** · 13 model · **16:47:10** | BT **59** · 14 model · **17:44:54** |
| `du_doan_test_bundles` (Nghiệm Thu) | BT **64** · ghi **06:05:01** | BT **64** · ghi **16:48:01** | **KHÔNG CÓ DÒNG NÀO** |

`predictions` MB 03/08: **27 dòng · 0 dòng rỗng**. Kho dự đoán đầy đủ — không phải model im lặng.

### 3.2 Bằng chứng dứt khoát: chính log của lane

`/root/Lottery_AI_Test/logs/v10879_nghiemthu.log`, hai lượt MB ngày 03/08:

```
2118: V10879_PREDRAW MB CHƯA ĐỦ ĐIỀU KIỆN · official chưa chốt miền này
2187: V10879_PREDRAW MB CHƯA ĐỦ ĐIỀU KIỆN · official chưa chốt miền này
```

`/var/log/syslog` xác nhận cron **có chạy** đủ hai lượt:

```
Aug  3 17:38:01 CRON[732516]: _v10879_nghiemthu_lane.py --predraw --region MB
Aug  3 17:42:01 CRON[732662]: _v10879_nghiemthu_lane.py --predraw --region MB
```

Không có lượt thứ ba. Official chốt **17:44:54** → muộn hơn lượt cuối **173 giây**.

### 3.3 Biên đã mỏng bao lâu rồi — đây mới là phần đáng sợ

| Ngày | official MB chốt | lane MB ghi | biên thực tế |
|---|---|---|---|
| **03/08** | **17:44:54** | **KHÔNG CÓ** | **−173s (mất)** |
| 02/08 | 17:37:53 | 17:38:02 | **+9 giây** |
| 01/08 | 17:39:55 | 17:42:01 | +126s |
| 31/07 | 17:35:27 | 17:38:01 | +154s |

MT cũng sát: 03/08 official 16:47:10 · lane 16:48:01 = **+51 giây**.

Giờ official chốt MB, 34 ngày (30/06 → 03/08): **17:33:00 → 17:44:54**, biên độ gần **12 phút**.
Nguyên nhân trôi là độ trễ nhà cung cấp — journal cùng ngày có `gemini-3.5-flash` HTTP **503** lúc
16:57:45, và model cuối `combo-super` mãi 17:44:54 mới ghi (`glm-5.1` 17:41:56).

### 3.4 Vì sao không phép kiểm nào kêu

- `_v10900_consistency_guard` báo **16/16 OK** đúng ngày MB trắng. Phép `C5_nghiemthu_lane_time`
  chỉ so **hằng số giờ khai báo** với crontab — nó không hề kiểm có output thật.
- `_v10891_deadline_guard` **có đếm**: `V10891_GUARD 2026-08-03: 55 mục · trễ 0 · chưa có 1`.
  Nhưng nó chỉ in **con số**, không nêu tên mục, và chỉ nằm trong file log không ai mở.

Máy biết mà không nói được — đúng thứ owner gọi là *"mất kiểm soát dần"*.

### 3.5 Soi lui 35 ngày — mất bao nhiêu ngày rồi

Lane Nghiệm Thu chỉ tồn tại từ **30/07** (`FROZEN_FROM = 2026-07-30`); trước đó trống là **đúng**,
không phải lỗi.

| Ngày | Có | Thiếu |
|---|---|---|
| 30/06 → 29/07 | — | lane chưa tồn tại |
| 30/07 | MN | MT, MB (đã ghi nhận ở V10880) |
| 31/07 | MN, MT, MB | — |
| 01/08 | MN, MT, MB | — |
| 02/08 | MN, MT, MB | — |
| **03/08** | MN, MT | **MB** |

→ **03/08 MB là lần lỡ THẬT đầu tiên: đúng 1 miền-ngày.** Không có chuỗi ngày âm thầm nào.

### 3.6 Lỗi thứ hai cùng ngày, cùng miền, khác nguyên nhân

Lane de-herd `MB_DEHERD_V1` ngày 03/08 **cũng trống**, nhưng vì lý do hoàn toàn khác:
`_v10872_deherd_selector.py` chết `sqlite3.OperationalError: database is locked` tại `_write_lane`
lúc 17:42:01 — khung 17:40–17:43 có **5 cron đè nhau** (`_v10822`, `_v10789`, `_v10832`, `_v10879`,
`_v10872`). MN (15:38:01) và MT (16:47:01) của lane này vẫn có. → mở **FU-253**.

### 3.7 Loại trừ các khả năng khác

| Nghi vấn | Kết quả đo |
|---|---|
| Service restart trong khung MB? | **Không** — PID **645169** liên tục từ 02/08 18:13:33 tới lúc điều tra |
| Deploy trong khung cấm 15:30–18:15? | **Không** — `main.py` mtime 02/08 18:13, lane 31/07 15:24, trang 31/07 14:18 |
| Lỗi cache / thiếu `no-store`? | **Không** — `/api/nghiem-thu` trả `Cache-Control: no-store, no-cache, must-revalidate, max-age=0` |
| Lỗi ngày (`getVNDateISO` nhảy sang mai)? | **Không** — API trả đúng `date=2026-08-03` |
| Lỗi lọc miền / JS? | **Không** — MN và MT hiện bình thường cùng trang |
| Cổng vốn `/choi` chặn nên `display_numbers` rỗng? | **Không áp dụng** — lane này không đi qua cổng vốn |

---

## 4. Hướng xử lý và vì sao chọn

### 4.1 Phân loại

Đây là **(A) không có dữ liệu thật**: lane thật sự không chạy ra được số, không phải trang hỏng.
Kèm một lớp **(B) hiển thị sai** làm sự cố khó hiểu hơn (mục 4.3).

**Không vi phạm §54.** §54 nói *"output phơi bày phải luôn thấy được; cổng chỉ khoá TIỀN"* và phạm
vi của nó là `/choi`. `_official_gate` ở đây **không phải cổng vốn** — nó là cổng **đủ điều kiện**,
dựng sau bài học 30/07 khi lane chốt bừa `43` từ 7 model rồi tối tính lại thành `86`, đúng cái bệnh
"số cứ giao động" owner đã than. Cổng đó cần thiết và không được gỡ.

Nhưng phải nói thẳng: **hậu quả rơi đúng vào họ lỗi §54 cảnh báo** — một cái cổng âm thầm tạo ra
phép đo NULL mà không ai hay. Cổng đúng, nhưng thiếu cái chuông.

### 4.2 Vì sao KHÔNG sinh số bù

Bây giờ là 19:2x. Mốc FINAL MB là **17:58** và MB đã xổ **~18:31**. Sinh số lúc này là số *sau khi
đã biết kết quả* — vừa phá quy tắc đóng băng output, vừa đầu độc chính phép đo mà luồng Nghiệm Thu
tồn tại để phục vụ (so bản mới với official tới mốc 19/08). **Ngày 03/08 MB ghi nhận MẤT, không vá.**

### 4.3 Ba việc phải sửa, và các phương án đã cân nhắc

| # | Việc | Phương án đã cân nhắc | Chọn gì · vì sao |
|---|---|---|---|
| 1 | Cổng mở sau khi hết lượt | (a) nới cổng cho chạy với kho thiếu · (b) cho lane tự chờ-và-thử trong tiến trình · (c) thêm lượt cron vá | **(c)**. Loại (a) vì đó chính là bài học 30/07, nới cổng là quay lại chốt bừa. Loại (b) vì thêm vòng chờ trong tiến trình cron là thêm chỗ treo mới, khó quan sát. (c) rẻ, **idempotent sẵn** (`ĐÃ CHỐT TRƯỚC ĐÓ` thoát ngay), và đúng khuôn hệ đang dùng |
| 2 | Trang nói dối | (a) để nguyên, chỉ sửa cron · (b) tách trạng thái và nói thật | **(b)**. Nếu chỉ sửa cron thì lần lỡ sau owner vẫn thấy "chưa tới giờ · Có số lúc 17:38" — vẫn không lần được manh mối |
| 3 | Không có chuông | (a) thêm cột vào `_v10891` · (b) thêm phép kiểm vào `_v10900` | **(b)**. `_v10900` đã có panel `/monitoring` và chạy 18:05 — **sau cả ba mốc FINAL**, đúng chỗ để bắt trong ngày |

Chọn giờ lượt vá bằng số đo, không đặt bừa: biên lane MB là **17:56** (= giờ khoá `/choi`), nên lượt
cuối phải ≤ 17:54 để ghi xong trước biên. Và cố ý đặt vào các phút **TRỐNG** trong crontab
(17:46/17:50/17:54) để không làm nặng thêm tranh khoá SQLite ở mục 3.6.

### 4.4 Không đụng vùng đóng băng QD-014

Không sửa: 15 model official · combo-super filter constants · override toggles · `/du-doan` ·
writer `final_bundles` · bộ chọn model production. Không deploy `main.py`. Toàn bộ thay đổi nằm
trong lane shadow (`output_eligible=0`, `test_only=1`), bộ tự kiểm, và hai trang hiển thị.

---

## 5. Đã làm gì

### 5.1 Bảng file × thay đổi

| File | Thay đổi |
|---|---|
| `web/backend/_v10879_nghiemthu_lane.py` | `LANE_SCHEDULE`: `final` MT **16:53→16:58**, MB **17:53→17:58** (nợ từ V10931); thêm khoá `last_run` (MN 06:15 · MT 16:54 · MB 17:54); thêm `_official_closed_at()`; thêm `_pending_reason()` tách ba trạng thái `CHUA_TOI_GIO` / `DANG_CHO` / `LO_HAN`; `_today_cards()` trả thêm `state`, `official_at`, `last_run_at` |
| `web/backend/_v10900_consistency_guard.py` | thêm hằng `BIEN_LANE_TOI_THIEU_GIAY = 300`, helper `_hhmmss()` / `_giay()`; thêm **C17** (miền qua mốc FINAL mà lane trống = LỆCH) và **C18** (biên lượt-cuối↔official chốt < 300s trong 7 ngày = LỆCH). **16 → 18 phép kiểm** |
| `web/frontend/nghiem-thu.html` | thẻ **LỠ HẠN** viền đỏ (`.nt-badge-missed`, `.nt-card.nt-missed`) tách hẳn khỏi "chưa tới giờ"; hiện giờ official chốt + lượt chạy cuối |
| `web/frontend/monitoring.html` | mốc FINAL cứng MT **16:53→16:58**, MB **17:53→17:58**; chuỗi dẫn `16:50/17:50 → 16:56/17:56` |
| crontab VPS | thêm 5 lượt vá: **MT 16:52 · 16:54**, **MB 17:46 · 17:50 · 17:54** |

Lượt `--predraw` sau khi sửa: MN `06:05 · 06:15` · MT `16:44 · 16:48 · 16:52 · 16:54` ·
MB `17:38 · 17:42 · 17:46 · 17:50 · 17:54`.

### 5.2 Backup

`E:\Lottery_AI_Test\backups\v10977_pre\` — 4 file gốc + `crontab_pre.txt` (121 dòng) +
`hash_pre.json` + `pid_pre.txt`.

### 5.3 Deploy

Deploy lúc **19:2x VN** — ngoài khung cấm (05:00–06:30 và 15:30–18:15). Hai lượt: lượt 1 đẩy 4 file
+ crontab; lượt 2 đẩy lại `_v10879_nghiemthu_lane.py` sau khi sửa câu chữ (mục 7.1).

| | PID trước | PID sau | health | `/api/nghiem-thu` chưa đăng nhập | traceback sau restart |
|---|---|---|---|---|---|
| Lượt 1 | 645169 | **737795** | 200 | 401 | 0 |
| Lượt 2 | 737795 | **738032** | 200 | 401 | 0 |

Service `lottery` (không phải `lottery-ai`), `is-active = active`. SHA256 từng file khớp local↔VPS.

### 5.4 Hash 4 bảng khoá — GIỮ NGUYÊN TUYỆT ĐỐI

| bảng | trước | sau |
|---|---|---|
| `predictions` | 11632 · `b8c9824f4813fe3e` | 11632 · `b8c9824f4813fe3e` |
| `final_bundles` | 471 · `2daecf094f81b289` | 471 · `2daecf094f81b289` |
| `lottery_results` | 15207 · `ad76b64a877ff460` | 15207 · `ad76b64a877ff460` |
| `model_daily_eval` | 11415 · `dae5167c47de30bc` | 11415 · `dae5167c47de30bc` |

### 5.5 Tài liệu và sổ

`CHANGELOG.md` (+3.763 ký tự) · `docs/CURRENT_TRUTH_SSOT.md` (+2.134) ·
`docs/FOLLOW_UP_TRACKER.md` (+2.318) — tất cả bằng `_doc_prepend.prepend()`, cả ba file **dài ra**.
`docs/OWNER_DECISION_LEDGER.json`: thêm **OD-20260803-B** (21 quyết định), 5 mệnh đề máy kiểm được.

---

## 6. Cổng kiểm

| # | Kiểm gì | Kết quả | Đạt? |
|---|---|---|---|
| 1 | Bộ tự kiểm chạy thẳng `run_checks()` (không đọc bản đã lưu) | **18 phép** (trước 16) | ĐẠT |
| 2 | **C17 có kêu đúng không** | `LECH` — `["MB: lane trống, official chốt 17:44:54"]` | ĐẠT |
| 3 | **C18 với lượt cuối mới** | `OK` — biên nhỏ nhất MB **546s**, MT **410s** (ngưỡng 300s) | ĐẠT |
| 4 | C5 cũ còn xanh sau khi thêm cron | `OK` — lượt đầu vẫn 06:05 / 16:44 / 17:38 | ĐẠT |
| 5 | Trang nói thật | MB: `state=LO_HAN`, `official_at=17:44:54`, `last_run_at=17:54` | ĐẠT |
| 6 | MN/MT vẫn hiện số | MN BT 64 · MT BT 64 · `final_at` 15:45 / 16:58 | ĐẠT |
| 7 | **Không sinh số bù** | `MB_NGHIEMTHU_1908_V1` ngày 03/08 = **0 dòng** | ĐẠT |
| 8 | Official MB nguyên vẹn | id 641 · BT 59 · `["59","52"]` · 14 model · 17:44:54 | ĐẠT |
| 9 | `Cache-Control` | `no-store, no-cache, must-revalidate, max-age=0` | ĐẠT |
| 10 | Smoke | health **200** · `/api/nghiem-thu` chưa đăng nhập **401** | ĐẠT |
| 11 | PID đổi thật | 645169 → 737795 → 738032 | ĐẠT |
| 12 | Traceback sau restart | **0** | ĐẠT |
| 13 | Hash 4 bảng khoá | **4/4 giữ nguyên** | ĐẠT |
| 14 | Compile + lint 4 file | sạch | ĐẠT |

Bằng chứng: `evidence/do_luong_v10977.json`, `evidence/log_lane_predraw_0308.txt`,
`evidence/syslog_cron_mb_1735_1750.txt`, `evidence/crontab_predraw_sau_sua.txt`,
`evidence/hash_4_bang_khoa.json`, `evidence/smoke_sau_deploy.txt`,
`evidence/deadline_guard_log.txt`, `evidence/deherd_log_loi_locked.txt`.

---

## 7. Vướng vấp

### 7.1 Agent tự gây: câu chữ "LỠ HẠN" suýt chỉ sai hướng điều tra

Bản đầu của `_pending_reason()` so giờ official chốt với hằng `last_run`, và khi official chốt
**trước** lượt cuối thì kết luận thẳng *"Đây là lỗi khác (không phải trôi giờ), phải soi log"*.
Kiểm sau deploy lượt 1 cho ra đúng câu đó cho MB 03/08 — **sai**, vì `last_run` lúc đó đã là 17:54
(lịch MỚI vừa thêm) trong khi lượt cuối THẬT của hôm nay là 17:42 (lịch CŨ).

**Hậu quả nếu bỏ qua:** owner mở trang tối nay sẽ đọc "đây là lỗi khác" và đi tìm một con bọ không
tồn tại — đúng loại hiển thị nói dối mà cả phiên này đang sửa. Đã sửa câu chữ để chỉ nói phần chắc
chắn (official chốt lúc nào, lane trống, hôm nay không có số) và trỏ vào log, không tự chẩn đoán.
Deploy lượt 2. **Bài học: khi đổi hằng số lịch trong cùng phiên, mọi câu chữ suy ra từ hằng số đó
đều nói về NGÀY MAI, không nói được về hôm nay.**

### 7.2 Hai lỗi khác nhau cùng đội lốt "MB không có số"

Suýt gộp `MB_DEHERD_V1` trống 03/08 vào cùng một nguyên nhân. Đo kỹ mới thấy nó chết vì
`database is locked`, không phải vì cổng. **Hậu quả nếu bỏ qua:** sửa cron cho lane Nghiệm Thu rồi
tuyên bố xong, trong khi lane de-herd vẫn rụng tiếp mỗi lần cron đè nhau. Đã tách thành **FU-253**.

### 7.3 Bộ tự kiểm báo xanh trong khi hệ đang hỏng

`_v10900` báo **16/16 OK** ngày 03/08. Không phải bộ kiểm chạy sai — nó kiểm đúng thứ nó được giao
(hằng số giờ khớp crontab) nhưng thứ đó không nói gì về việc có output hay không. **Hậu quả nếu bỏ
qua:** cả tầng tự kiểm thành thứ trang trí, càng nhiều phép xanh càng tin nhầm. Đây là lý do C17
kiểm **kết quả** chứ không kiểm **cấu hình**.

### 7.4 Chuông đã kêu mà không ai nghe thấy

`_v10891_deadline_guard` **đã đếm đúng** (`chưa có 1`) cả ngày 01/08 lẫn 03/08, nhưng chỉ in con số
vào file log. **Hậu quả nếu bỏ qua:** tưởng hệ mù, đi dựng bộ đo mới trong khi bộ cũ đã đo đúng chỉ
thiếu đường phát tín hiệu. Chưa sửa `_v10891` trong phiên này (C17 đã phủ được việc cần kíp) —
ghi vào FU-252 để cân nhắc cho nó nêu tên mục thay vì chỉ đếm.

### 7.5 Agent tự gây: sổ quyết định TRÔI 1/5 trong ~1 phút, phiên V10978 chạy song song bắt được

Mệnh đề `kiem_code` thứ hai của **OD-20260803-B** viết `all('last_run' in v for v in
LANE_SCHEDULE.values()) and ...`. Sandbox của `_v10920_decision_ledger.py` **không nạp builtins**,
nên `all` không tồn tại → `LỖI: name 'all' is not defined` → sổ chuyển từ **0 TRÔI sang 1 TRÔI**
lúc **19:30**.

Phiên **V10978** (kiểm toán diện cuối ngày, chạy song song) chụp đúng khoảnh khắc đó và đã ghi vào
báo cáo công khai của họ. Agent tự phát hiện và sửa ngay: đổi sang so sánh trực tiếp ba miền
(`LANE_SCHEDULE['MN']['last_run'] == '06:15' and ...`), chạy lại lúc **19:31:28** → **khớp 5/5,
0 TRÔI, exit 0**.

**Hậu quả nếu bỏ qua:** luật nhà nói *"có mục TRÔI thì dừng, xử trước khi làm việc mới"* — để lại
là chặn phiên sau, và tệ hơn là mệnh đề kiểm không bao giờ chạy được nên quyết định OD-20260803-B
coi như không có ai canh. **Bài học: mệnh đề `kiem_code` chỉ được dùng toán tử và truy cập thuộc
tính, không được gọi builtin.** Đã kiểm lại: bốn mệnh đề còn lại của mục này dùng `==`, `and`, và
một set-comprehension — đều chạy được.

### 7.6 Cột `predictions` không có `region`/`model_name`

Probe đầu tiên chết hai lần vì đoán tên cột. Tên thật là `target_region` và `ai_model`. **Hậu quả
nếu bỏ qua:** không có — đã bắt ngay tại chỗ. Ghi lại để phiên sau đọc `PRAGMA table_info` trước.

---

## 8. Gỡ về

Backup: `E:\Lottery_AI_Test\backups\v10977_pre\` (4 file + `crontab_pre.txt` 121 dòng).

```bash
# 1. Trả 4 file (chạy từ E:\Lottery_AI_Test)
scp backups/v10977_pre/_v10879_nghiemthu_lane.py    root@14.225.224.89:/root/Lottery_AI_Test/web/backend/
scp backups/v10977_pre/_v10900_consistency_guard.py root@14.225.224.89:/root/Lottery_AI_Test/web/backend/
scp backups/v10977_pre/nghiem-thu.html              root@14.225.224.89:/root/Lottery_AI_Test/web/frontend/
scp backups/v10977_pre/monitoring.html              root@14.225.224.89:/root/Lottery_AI_Test/web/frontend/

# 2. Trả crontab (gỡ 5 lượt vá)
scp backups/v10977_pre/crontab_pre.txt root@14.225.224.89:/tmp/
ssh root@14.225.224.89 "crontab /tmp/crontab_pre.txt && crontab -l | grep -c V10977"   # phải ra 0

# 3. Restart + so PID
ssh root@14.225.224.89 "systemctl restart lottery && sleep 10 && \
  systemctl show -p MainPID --value lottery && \
  curl -s -o /dev/null -w 'health=%{http_code}\n' http://127.0.0.1:8000/api/health"
```

Mất khoảng **3 phút**. Không cần đụng DB: phiên này **không ghi một dòng dữ liệu nào** — hash 4 bảng
khoá giữ nguyên, và cũng không thêm dòng lane nào cho 03/08.

---

## 9. Theo dõi tiếp

### FU-252 · KS1008 · Canh lane Nghiệm Thu ra số đủ 3 miền · hạn 10/08
`DEPLOYED_PENDING_LIVE_VERIFY`

Rà ngày **10/08**, cửa sổ 04→10/08 (7 ngày). **Ngưỡng hành động bằng số:**

- lane Nghiệm Thu phải đủ **21/21 miền-ngày**. Thiếu ≥1 → điều tra ngay trong ngày đó.
- **C18 phải OK cả 7 ngày.** Có 1 ngày LỆCH → dời lượt vá muộn thêm 2 phút (còn dư tới biên
  16:56 / 17:56) và báo owner.
- giờ official chốt MB **> 17:52:00** bất kỳ ngày nào → biên còn dưới 2 phút, **hết chỗ dời trong
  khung biên hiện tại**, phải báo owner để quyết (dời biên hay tăng tốc chuỗi AI).
- cân nhắc cho `_v10891_deadline_guard` nêu **tên mục** thay vì chỉ đếm `chưa có N` (mục 7.4).

### FU-253 · SC1008 · Lane de-herd chết "database is locked" khung 17:40–17:43 · hạn 10/08
`MEASURED_BUT_NOT_FIXED`

Đếm `database is locked` trong `logs/v10872_deherd.log` từ 04→10/08. **Ngưỡng:** ≥2 ngày dính →
giãn cron hoặc bật `PRAGMA busy_timeout` cho lane này, làm ngay trong phiên đó.

### Quyết định đã ghi sổ

**OD-20260803-B** (`docs/OWNER_DECISION_LEDGER.json`, `ngay_ra_soat: 2026-08-10`) — 5 mệnh đề máy
kiểm được, gồm `LANE_SCHEDULE` khai đúng mốc FINAL, có `last_run`, `BIEN_LANE_TOI_THIEU_GIAY == 300`,
C17/C18 có mặt trong `run_checks()`, và trang có nhãn `nt-badge-missed`.

### Ghi nhận mất mát

**MB 03/08 luồng Nghiệm Thu = 1 miền-ngày mất, không vá.** Cửa sổ đo forward tới mốc quyết định
19/08 mất 1 điểm dữ liệu MB. Không ảnh hưởng official, `/du-doan`, `/choi`, hay ví tiền.
