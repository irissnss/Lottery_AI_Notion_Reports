# V10988 — Kiểm tổng lực đầu ngày 05/08/2026 + DEPLOY phép canh toàn vẹn giao diện (`C22`)

| | |
|---|---|
| **Phiên bản** | V10988 |
| **Ngày** | 2026-08-05 (giờ Việt Nam) |
| **Owner ký** | 08:59 |
| **Có deploy** | **CÓ** — 09:0x, ngoài cả hai khung cấm (05:00–06:30 · 15:30–18:15) |
| **Tệp deploy** | đúng **một**: `web/backend/_v10900_consistency_guard.py` |
| **PID `lottery`** | 801640 → **834969** (`NRestarts=0`) |
| **Hash 4 bảng khoá** | **GIỐNG HỆT trước/sau** — không ghi một dòng nào |
| **Vùng đóng băng `QD-014`** | **KHÔNG chạm** — còn hiệu lực hết 08/08 |

---

## 1. Tóm tắt một đoạn

Kiểm tổng lực đầu ngày: **6/6 cổng tự kiểm thoát 0**, **0 quyết định TRÔI** (28 quyết định,
QD-026 mới khớp 14/14), **0 traceback**, **0 lỗi nhà cung cấp** từ 00:00. Hệ đang chạy sạch.
Việc deploy chính là dựng **`C22_giao_dien_toan_ven`** — phép **duy nhất** trong bộ tự kiểm
nhìn vào chính tệp giao diện — nâng bộ tự kiểm **21 → 22 phép**. Đây là ngưỡng đến hạn hôm nay
của `FU-262`, và là phép sẽ bắt được đúng chuyện `monitoring.html` bị cắt cụt **53,5%** hôm
04/08 mà 18 phép còn lại vẫn xanh suốt 2 ngày. **Thử ngược 7/7** bằng **chính tệp cụt thật
262.144 byte** đã chạy trên VPS, không phải bản dựng giả. Năm mục đến hạn 05/08: **đóng 4**
(`FU-262` `FU-259` `FU-207` `FU-254` → `CLOSED_PASS`), **dời 1** (`FU-243` → 09/08, vì phần
còn lại nằm đúng trong vùng `QD-014` cấm). Sống hôm nay: MN chốt **05:19:51**, bạch thủ **25**,
**15/15 model**, và tín hiệu `DA_XONG_BLOCK` ghi lúc **05:20:03 — trễ đúng 12 giây** (hôm qua
17.754 giây); **hôm nay là ngày đầu MN chạy đúng khung cron và đạt**. Cổng lợi thế **9/9 ô vẫn
ĐÓNG**, **tiền thật = 0 đồng**.

---

## 2. Owner yêu cầu gì — nguyên văn

> **08:59 ngày 05/08/2026 (giờ VN):**
> *"Đầu ngày rồi đó em, kiểm tra tổng lực và deploy nếu cần đi chứ chờ đợi gì nữa?"*

Hai vế: **kiểm tổng lực đầu ngày** và **deploy những gì đang chờ**. Vế thứ hai là chỗ đáng chú
ý — phiên V10987 hôm qua đã phải bỏ dở đúng phần `C22` vì được giao phạm vi *"không deploy"*,
và `FU-262` đến hạn **đúng hôm nay**. Câu *"chờ đợi gì nữa"* đọc thẳng là: đừng hoãn tiếp.

Đã ghi vào sổ quyết định thành **`QD-026`** (`KS0508`), nguyên văn, kèm **14 mệnh đề máy kiểm
được** — `_v10920_decision_ledger.py` chấm **khớp 14/14**.

---

## 3. Đào bới / phát hiện

### 3.1 Sáu cổng tự kiểm — chạy TÁCH RIÊNG từng lệnh

| Lệnh | Mã thoát | Kết quả |
|---|---|---|
| `_v10920_session_start.py` | **0** | 0 checkpoint quá hạn · 102 mục treo · **5 đến hạn hôm nay** · 15 mồ côi · 1 quá hạn (`FU-225`) |
| `_v10920_decision_ledger.py` | **0** | 27 quyết định, **0 TRÔI** |
| `_v10921_report_gate.py` *(bản quét TOÀN BỘ)* | **0** | 8 phiên bản gần nhất đều đủ 9 phần **và đã push** |
| `_v10925_rule_sync_check.py --check` | **0** | 6 mặt quy tắc đồng bộ · 4/4 `.mdc` đều tự nạp |
| `_v10981_kiem_lich.py` | **0** | K1–K8 **8/8 ĐẠT** |
| `_v10982_kiem_lich9.py` | **0** | J1–J8 **8/8 ĐẠT** |

### 3.2 `FU-266` — cổng báo cáo có thể báo xanh giả, đã kiểm thật

Cổng kiểm *"đã push chưa"* bằng `git fetch`, mà Google Drive đẻ `desktop.ini` vào `.git/refs`
làm `fetch` chết → `origin/main` đứng đông → cổng xanh oan. **Đã kiểm bằng cách khác, không tin
`git status`:** `HEAD` = `origin/main` = `628734e997885ed1592b84fbb1571c6dcd8de3ae`, và
`git ls-tree -r origin/main` **có đủ 10 tệp của V10987 trên remote**. Bốn tệp *"chưa commit"*
mà cổng báo chỉ là `desktop.ini` của Google Drive, vô hại.

### 3.3 Sức khoẻ hệ thống

| Mục | Số đo |
|---|---|
| `/api/health` | **200** |
| Dịch vụ `lottery` | `active` · **MainPID 801640** — **đúng bằng PID đã biết**, `NRestarts=0` |
| Uptime máy | 109 ngày |
| Đĩa | 27G/39G = **69%**, còn 13G |
| DB | **657 MB** |
| Traceback/ERROR từ 00:00 | **0** |
| Lỗi nhà cung cấp (429/503/timeout) | **0** |
| `monitoring.html` trên VPS | **577.617 byte** — nguyên vẹn, đúng bằng mốc 04/08 |

### 3.4 `FU-259` — C17/C18 có lượt ghi thật chưa? **CÓ, và bắt được việc thật ngay lượt đầu**

Ngưỡng mục tự viết: *"18:05 ngày 04/08 bảng phải có **đúng 21 dòng**"*.

**Đo được:** bảng `v10900_consistency_guard` ngày `2026-08-04` có **đúng 21 dòng**,
`computed_at_vn` = **`2026-08-04T18:05:02+07:00`** — đúng lượt cron, không phải chạy tay.
Lịch sử: 31/07 → 03/08 đều **16 dòng**; 04/08 nhảy lên **21**. **ĐẠT.**

**Mạnh hơn ngưỡng — hai phép mới không hề "xanh cho có":**

| Phép | Trạng thái | Nội dung |
|---|---|---|
| `C17_nghiemthu_co_output` | OK | `[]` |
| **`C18_bien_lane_du_rong`** | **LỆCH** | *"MT 2026-08-04: official 16:50:13 · lượt cuối 16:54 · biên **227s**"* (ngưỡng 300s) |
| **`C19_bien_han_du_rong`** | **LỆCH** | *"MT 2026-08-04: chốt cách hạn **467s**"* (ngưỡng 480s) |
| `C20` · `C21` | OK | `[]` |

19/21 OK. Hai mục LỆCH là **việc thật của MT hôm qua**, thuộc ngưỡng hành động của `FU-256`
(hạn 06/08) — **không phải lỗi của phiên này**.

### 3.5 Sống hôm nay 05/08 — MN và tín hiệu `DA_XONG_BLOCK`

| Mục | Số đo |
|---|---|
| MN official chốt | **05:19:51** |
| Bạch thủ | **25** · lô2 `["25","10"]` |
| `model_count` | **15/15** — **không bị lọc phiếu** |
| Đồng thuận | `strong` · `weighted_voting_wr` · `is_fallback=0` · `status=ACTIVE` |
| `predictions` hôm nay | 41 dòng, 27 model, 05:00:05 → 05:30:44 |

**Câu quan trọng nhất của phiên — độ trễ tín hiệu `DA_XONG_BLOCK`:**

| Ngày | official chốt | ghi `DA_XONG_BLOCK` | **trễ** |
|---|---|---|---|
| 04/08 | 05:19:56 | 10:15:50 | **17.754 giây** (~4h56) — vì V10979 vừa lên 10:15, lượt sáng đã qua |
| **05/08** | **05:19:51** | **05:20:03** | **12 giây** ✓ |

Ngưỡng `FU-260` là **≤ 60 giây**. Hôm nay là **ngày đầu tiên MN chạy đúng trong khung cron
thật** (`* 5-6 * * *`) và **đạt với biên rộng** — 12 giây so với hạn 60 giây. `som_hon_giay` =
37.509 (sớm hơn hạn 15:45 tới 625 phút). **Không phải lỗi, không phải mở mục mới.**

### 3.6 Lane nghiệm thu · cổng lợi thế · tiền thật · chấm điểm

- **Lane nghiệm thu MN 05/08 đã ra số** lúc **05:20:01** (`MN_NGHIEMTHU_1908_V1`).
  `FU-252` đang **4/21** ô miền-ngày trong cửa sổ 04→10/08 — đúng nhịp, MT/MB chưa tới giờ.
- **Cổng lợi thế: chạy đủ 3 miền × 3 cửa sổ = 9 ô, TẤT CẢ ĐÓNG.**

| Cửa sổ | MN | MT | MB |
|---|---|---|---|
| 30 ngày | −2,46pp · z −0,65 | −4,15pp · z −0,95 | −0,17pp · z −0,02 |
| 90 ngày | −0,20pp · z −0,09 | −3,26pp · z −1,30 | −7,04pp · z −1,57 |
| 180 ngày | −0,05pp · z −0,03 | **+0,67pp · z 0,35** | −1,59pp · z −0,47 |

  Ô khá nhất là **MT 180 ngày +0,67pp, z = 0,35** — còn rất xa ngưỡng `QD-013` (**≥3pp VÀ
  z≥2**). Ước tính cần thêm **380–1.575 ngày** mới đủ mẫu chứng minh lợi thế 3pp.
- **Tiền thật = 0 đồng.** `money_board_log` **114/114 dòng** đều `shadow_only=1`,
  `output_eligible=0`, `owner_approved=0`. Cột `stake` là **nhãn chữ** (*"Full (50 điểm…)"* /
  *"Nửa"* / *"Nghỉ"*), là **mô phỏng**, không phải lệnh đặt tiền.
- **Chấm điểm 04/08 xong:** `model_daily_eval` **81 dòng** (27 model × 3 miền), chấm lúc
  **20:20**. Bạch thủ trúng: MN **8** · MT **11** · MB **2**. Kết quả 04/08 về đủ 3 miền.
- **Bảng đo ghép** `ghep_nt_official_daily` có **3 dòng ngày 04/08**; cron `19:10` có thật
  trong `crontab` (script tên `_v10984_ghep_lane_official.py`).

### 3.7 Phát hiện MỚI — hai cron của V10984 **chưa từng chạy thật**

Kiểm bằng máy: **không tồn tại** `logs/v10945_edge_gate.log` lẫn `logs/v10984_ghep_lane.log`.
Cron được đặt lúc **~22:0x ngày 04/08**, tức **sau** giờ chạy 19:00/19:10 của chính ngày đó.
Nên các dòng ngày 04/08 trong `edge_gate_daily` (`created_at` **22:36:44**) và
`ghep_nt_official_daily` là **do chạy tay trong phiên V10984**, không phải cron.

`FU-244` vẫn đóng **đúng**, vì ngưỡng nó tự viết chỉ đòi *"có dòng cron"* + *"có dòng mới mang
ngày ≥ ngày đặt cron"* — cả hai đều đạt. Nhưng **tối nay 05/08 mới là lượt cron đầu tiên**,
phải xác nhận lại sau 19:10.

### 3.8 `FU-243` — ngưỡng bị vượt mọi tuần suốt hơn một tháng

Đo lại 30 ngày trên `final_bundles`:

| Miền | Số ngày | Ngày `model_count` < 15 | Thấp nhất | Cao nhất | Trung bình |
|---|---|---|---|---|---|
| **MT** | 30 | **30/30 = 100%** | 11 | 13 | **12,93** |
| **MB** | 30 | **25/30 = 83%** | 12 | 15 | 13,83 |
| MN | 31 | 2/31 = 6% | 13 | 15 | 14,90 |

Tổng **57/91 ô**. Ngưỡng của chính mục này — *"≥3 ngày/tuần incomplete cùng pattern →
escalate"* — bị vượt **mọi tuần**, riêng MT là **7/7 ngày mỗi tuần**, mà chưa lần nào escalate
vì phép canh chỉ nhìn **một ngày**. Và `/api/health` vẫn khai
`expected_output_model_count: 15` trong khi mức thật ổn định của MT là **13**.

### 3.9 `FU-254` — ba bảng P&L chết **77 ngày** (không phải 75)

| Bảng | Dòng | Dòng cuối | Cron ghi |
|---|---|---|---|
| `pnl_daily_summary` | 14 | 2026-05-20 | **0** |
| `pnl_daily_bets` | 28 | 2026-05-20 | **0** |
| `pnl_daily_settlements` | 76 | 2026-05-20 | **0** |

Hai nguồn P&L **đang sống thật**: `money_board_log` (114 dòng, mới nhất 04/08, cron 18:31) và
`pnl_forward_track_shadow` (**1.242 dòng**, mới nhất 04/08, cron 22:30).

### 3.10 `FU-207` — phần SỬA đã có sẵn, chỉ thiếu phần NGHIỆM THU

Đọc thẳng code (không đọc lại báo cáo cũ): `MB_SCRIPT` trong `_v10934_deploy.py` **đã** đòi
**một trong hai** từ V10940 — `qua_moc` (giờ VN > `17:58`) **hoặc** `da_tchot`
(`bundle_version >= 2`). Thứ còn thiếu đúng là **hai ca thử** mà ngưỡng FU-207 tự viết.

---

## 4. Hướng xử lý và vì sao chọn

### 4.1 `C22` — so với **MỐC CAO NHẤT**, không phải *"lần chạy trước"*

FU-262 viết nguyên văn *"kích thước không tụt quá 10% **so với lần trước**"*. **Đã cố ý làm
khác**, và đây là quyết định đáng nói nhất của phiên:

| Phương án | Điều gì xảy ra khi tệp bị cắt cụt | Vì sao chọn / loại |
|---|---|---|
| So với **lần chạy trước** *(đúng câu chữ)* | Đỏ **đúng một ngày**. Hôm sau bản cụt thành mốc mới → **cổng xanh trở lại** dù tệp vẫn hỏng | **LOẠI** — đây đúng là loại "xanh giả" đang đi diệt |
| So với **mốc cao nhất** *(đã chọn)* | Đỏ **mãi** cho tới khi có người xử | **CHỌN** — bảng `v10988_ui_moc` cập nhật bằng `MAX()`, mốc chỉ đi lên |

Bước 4–5 của bộ thử ngược tồn tại **chỉ để chứng minh tính chất này**: chạy lần thứ hai trên
bản cụt vẫn đỏ, và mốc vẫn giữ 577.617 chứ không tụt theo.

### 4.2 Ba điều kiện độc lập chứ không một dấu hiệu

Chọn **3 điều kiện cùng lúc** (thẻ đóng · kích thước · `setInterval`/`loadXxx`) vì mỗi kiểu
hỏng để lại dấu khác nhau: ghi đứt giữa chừng mất thẻ đóng; ghi đè bằng bản cũ thì đủ thẻ
nhưng tụt kích thước; xoá nhầm một khối panel thì kích thước tụt ít mà số hàm `loadXxx` giảm
mạnh. Thử ngược cho thấy bản cụt thật **kích hoạt cả 3** — nhưng nếu chỉ dựa vào một dấu thì
sẽ có kiểu hỏng lọt.

### 4.3 Vì sao **restart** dù phép mới chạy bằng cron

`main.py` `import _v10900_consistency_guard` **bên trong hàm endpoint**, và Python giữ module
trong `sys.modules` sau lần gọi đầu — nên tiến trình đang chạy vẫn ôm **bản cũ trong bộ nhớ**
dù đĩa đã mới. Phần `compute_view()` không đổi nên về mặt chức năng không sai, nhưng để
**tiến trình và đĩa khớp nhau** thì phải restart. Chọn khởi động lại lúc **09:2x** vì đó là
khe an toàn nhất trong ngày: MN đã chốt xong từ 05:19, MT còn hơn 7 tiếng nữa.

### 4.4 Năm mục đến hạn — đóng 4, dời 1

| Mã | Quyết | Vì sao |
|---|---|---|
| `FU-262` | **ĐÓNG** `CLOSED_PASS` | `C22` đã dựng + thử ngược 7/7 + deploy + chạy thật |
| `FU-259` | **ĐÓNG** `CLOSED_PASS` | 21 dòng đúng 18:05 ngày 04/08, đủ mặt C17–C21 |
| `FU-207` | **ĐÓNG** `CLOSED_PASS` | 2/2 ca bắt buộc (6/6 toàn bộ) |
| `FU-254` | **ĐÓNG** `CLOSED_PASS` | 3/3 bảng đánh dấu `RETIRED` trong SSOT |
| `FU-243` | **KHÔNG ĐÓNG**, dời **09/08** | phần còn lại nằm ĐÚNG vùng `QD-014` cấm |

**`FU-254` chọn nhánh RETIRE thay vì nối lại cron:** hai nguồn P&L đang sống đã phủ đủ việc;
dựng thêm một đường ghi thứ ba cho ba bảng **không ai đọc** là thêm chỗ hỏng mà không thêm
thông tin. Không xoá bảng, không xoá dữ liệu — giữ làm lịch sử.

**`FU-243` vì sao không thể đóng hôm nay, nói thẳng:** ba thứ phải chạm để sửa —
`bt_gate`, `MT_top13_V10752` (đều là **bộ lọc combo-super / bộ chọn model production**) và
`expected_output_model_count` (**con số công bố của đường ra số**) — **đều nằm trong 5 thứ
`QD-014` cấm đích danh tới hết 08/08**. Không có cách nào đóng đúng hạn 05/08 mà không phạm
quy tắc owner đã ký. Chọn **09/08** vì đó là **ngày đầu tiên** hết đóng băng; không dời xa hơn
để khỏi trôi tiếp.

---

## 5. Đã làm gì

### 5.1 Bảng tệp × thay đổi

| Tệp | Thay đổi |
|---|---|
| `web/backend/_v10900_consistency_guard.py` | **+`C22_giao_dien_toan_ven`** · thêm `UI_FILES` (5 tệp) · `UI_TUT_TOI_DA = 0.10` · `UI_SCHEMA` (bảng `v10988_ui_moc`) · `_do_giao_dien()` · `kiem_giao_dien()`. **30.847 → 36.053 byte** |
| `web/backend/_v10988_thu_nguoc_c22.py` | **MỚI** — thử ngược 7 bước bằng tệp cụt thật |
| `web/backend/_v10988_thu_cong_deploy.py` | **MỚI** — nghiệm thu cổng deploy `FU-207`, 6 ca |
| `web/backend/_v10982_lich9.py` | `TAI_PHIEN_KHAC_DO_DUOC`: 05/08 → `[]` · 09/08 `+FU-243` |
| `web/backend/_v10988_probe.py` · `_probe2.py` · `_ui_probe.py` · `_chay_c22.py` · `_hash.py` | **MỚI** — dò trạng thái sống, **chỉ đọc** |
| `web/backend/_v10988_governance.py` · `_ghi_quyet_dinh.py` · `_sua_qd026.py` | **MỚI** — ghi tài liệu qua `prepend()` |
| `docs/FOLLOW_UP_TRACKER.md` | **+13.201** ký tự (1.112.161 → 1.125.362) |
| `CHANGELOG.md` | **+2.950** ký tự |
| `docs/CURRENT_TRUTH_SSOT.md` | **+2.882** ký tự, gồm 3 dòng `RETIRED` |
| `docs/OWNER_DECISION_LEDGER.json` | **+`QD-026`** · 27 → 28 quyết định · 14 mệnh đề máy kiểm |
| `docs/LICH_CUON_CHIEU_DEN_10082026.md` | sinh lại từ máy — 38.146 byte, 247 dòng |
| `docs/PLAYBOOK_PERIODIC_FULL_SYSTEM_CHECK.md` | §5 đánh dấu 05/08 **ĐẠT** · §2 thêm mục **8b** (`C22`) và **9** (cổng deploy) |

### 5.2 Backup trước khi sửa

`backups/v10988_pre/` — `_v10900_consistency_guard.py.pre` (30.847B) ·
`FOLLOW_UP_TRACKER.md.pre` · `CURRENT_TRUTH_SSOT.md.pre` · `CHANGELOG.md.pre` ·
`OWNER_DECISION_LEDGER.json.pre`. Trên VPS:
`/root/Lottery_AI_Test/backups/_v10900_consistency_guard.py.v10988_pre`.

### 5.3 Deploy

| Mục | Trước | Sau |
|---|---|---|
| md5 tệp | `05466bc600a2f420aba11ae0a02d7b7d` | `b0442354f96d86af72ccf6fe11f8314e` |
| Kích thước | 30.847 B | **36.053 B** |
| PID `lottery` | **801640** | **834969** |
| `NRestarts` | 0 | **0** (tắt êm, không crash-loop) |
| Bộ tự kiểm | **21 phép** | **22 phép** |

Restart dùng đúng tên **`lottery`**. PID **đổi thật** → không dính bẫy *"Unit not found"* mà
health vẫn 200.

### 5.4 Chạy thật ngay, không đợi cron 18:05

Gọi thẳng `run_checks()` trên VPS lúc **09:10** → **22 phép · 20 OK · 2 LỆCH**.
`C22_giao_dien_toan_ven` = **`OK`**. Mốc dựng đúng kích thước thật đang chạy:

| Tệp | Mốc | `setInterval` | `loadXxx` |
|---|---|---|---|
| `monitoring.html` | 577.617 | 2 | 67 |
| `du-doan-test.html` | 221.956 | 0 | 11 |
| `review-dashboard.html` | 118.497 | 0 | 6 |
| `pnl-tracker.html` | 101.095 | 0 | 2 |
| `choi.html` | 61.568 | 2 | 3 |

Sau đó chạy lượt ghi đầy đủ để bảng ngày 05/08 có **22 dòng** — panel `/monitoring` hiện `C22`
ngay hôm nay chứ không đợi 18:05.

---

## 6. Cổng kiểm

### 6.1 THỬ NGƯỢC `C22` — **7/7 ĐẠT** (bắt buộc)

Dùng **chính tệp cụt thật** `backups/v10979_pre/monitoring.html.cut_20260804_100331`
(**262.144 byte** = 256 KiB chẵn), không phải bản dựng giả.

| Bước | Tình huống | Kỳ vọng | Thật |
|---|---|---|---|
| 1 | bản lành, lượt đầu | 0 hỏng, dựng mốc | **ĐẠT** |
| 2 | bản lành, lượt hai | 0 hỏng (không báo oan) | **ĐẠT** |
| 3 | **thay bằng bản cụt thật** | TRƯỢT **và gọi đúng tên tệp** | **ĐẠT — 4 chỗ hỏng** |
| 4 | chạy lại trên bản cụt | VẪN đỏ | **ĐẠT** |
| 5 | mốc sau khi gặp bản cụt | vẫn 577.617 | **ĐẠT** |
| 6 | trả lại bản lành | 0 hỏng | **ĐẠT** |
| 7 | tệp giao diện thật ở local | 0 hỏng | **ĐẠT** |

Bốn dòng `C22` in ra ở bước 3, **nguyên văn**:

```
monitoring.html: thiếu thẻ đóng </script> </body> </html>
monitoring.html: 262,144 byte — tụt 54.6% so với mốc 577,617
monitoring.html: còn 1 vòng setInterval, mốc 2
monitoring.html: còn 25 hàm loadXxx, mốc 67
```

**Cả ba điều kiện độc lập đều bắt được.**

### 6.2 Nghiệm thu cổng an toàn deploy (`FU-207`) — **2/2 ca bắt buộc, 6/6 toàn bộ**

Chạy **nguyên văn `MB_SCRIPT`** đang dùng thật (đọc bằng `ast`, thay `sqlite3`/`datetime` ở
`sys.modules`). **Không sửa code đang chạy để cho dễ thử** — sửa thì thứ được nghiệm thu không
còn là thứ đang chạy.

| Ca | Giờ | `bundle_version` | Kỳ vọng | Thật |
|---|---|---|---|---|
| **A** *(bắt buộc)* | 17:45 | v1 | **CHẶN** | ĐẠT — `CHUA_QUA_T_CHOT` |
| **B** *(bắt buộc)* | 18:05 | v2 | **CHO QUA** | ĐẠT — `AN_TOAN (da qua moc bat dong 17:58)` |
| C | 17:56 | v2 | cho qua | ĐẠT |
| D | 18:01 | v1 | cho qua | ĐẠT |
| E | 17:45 | *(chưa có bundle)* | CHẶN | ĐẠT — `CHUA_CHOT` |
| F | 17:50 | `NULL` | CHẶN | ĐẠT — `NULL` quy về v1 |

### 6.3 Sáu cổng tự kiểm — chạy lại SAU khi sửa

| Lệnh | Mã thoát |
|---|---|
| `_v10920_session_start.py` | **0** — *"đến hạn hôm nay"* **5 → 0** · treo 102 → **98** |
| `_v10920_decision_ledger.py` | **0** — 28 quyết định, **0 TRÔI**, `QD-026` khớp **14/14** |
| `_v10921_report_gate.py` *(toàn bộ)* | **0** *(sau khi có báo cáo này)* |
| `_v10925_rule_sync_check.py --check` | **0** |
| `_v10981_kiem_lich.py` | **0** — K1–K8 **8/8** |
| `_v10982_kiem_lich9.py` | **0** — J1–J8 **8/8**, `J5` xác nhận mốc tải khớp sổ thật **7/7 ngày** |

### 6.4 Smoke sau restart + hash 4 bảng khoá

| Mục | Kết quả |
|---|---|
| `/api/health` | **200** |
| `/api/admin/consistency-guard` | **401** |
| `/api/admin/early-block` | **401** |
| Traceback 2 phút sau restart | **0** |

| Bảng | SHA256 **trước = sau** | Dòng |
|---|---|---|
| `predictions` | `ec59cfd5ee8c9a9a59e0009b2d836e2a8b4e0c9069aa25d90442b409e653a250` | 11.754 |
| `final_bundles` | `6848318ee93ad48ede3c978bebd79489bb8bdaf6538f05b5260548342d362560` | 475 |
| `lottery_results` | `92ccf706553921288f2105f96e2a399b89835429fbfb6d6fac1104f9841e0029` | 15.213 |
| `model_daily_eval` | `c559a75ad34b78ed89ed7d265dca3e13349fe54561759258a5109b87aa5fb744` | 11.577 |

**Giống hệt nhau từng ký tự** — phiên này không ghi một dòng nào vào 4 bảng khoá.

---

## 7. Vướng vấp

### 7.1 Mệnh đề máy kiểm của `QD-026` báo TRÔI oan — tự gây, sửa trong phiên

Viết mệnh đề kiểm bảng mốc tải bằng `module: _v10982_lich9` + `bieu_thuc`. Chạy sổ quyết định
→ **`QD-026` TRÔI 1/14**, lỗi `No module named '_v10982_lich9'`.

**Căn nguyên:** `_v10920_decision_ledger.py` chạy mệnh đề `module`/`bieu_thuc` **TRÊN VPS**,
còn `_v10982_lich9.py` là công cụ chạy ở **máy local**, không có trên VPS. Mệnh đề đúng về ý
nhưng sai về chỗ chạy.

**Hậu quả nếu bỏ qua:** sổ quyết định đứng ở trạng thái **TRÔI**, mà luật ghi rõ *"có mục TRÔI
thì dừng, xử trước khi làm việc mới"* — cả phiên sau sẽ bị chặn bởi một lỗi giả.

**Đã sửa:** đổi sang `file_chua` (chạy ở local) kiểm đúng dòng
`dt.date(2026, 8, 9): ["FU-200", "FU-202", "FU-243", "FU-261"]`. Chạy lại → **khớp 14/14**.

**Bài học:** mệnh đề `module`/`bieu_thuc` chạy trên **VPS** — chỉ dùng cho module **có deploy**.
Công cụ chỉ chạy local phải kiểm bằng `file_chua` / `file_ton_tai`.

### 7.2 PowerShell băm nát lệnh bash/python nhồi qua SSH — vấp **hai lần**

Nhồi `python3 -c "..."` nhiều tầng nháy qua `ssh` → PowerShell nuốt dấu, báo
*"An expression was expected after '('"*. Lần hai với `for f in ...; do ... $(stat -c%s $p) ...`
→ *"$(subexpression) is missing the closing ')'"*.

**Đã xử:** bỏ hẳn lối nhồi lệnh; viết tệp `.py` rồi `scp` lên VPS và chạy. Đây đúng là bẫy đã
ghi trong mục *"Mẹo vận hành"* của bộ quy tắc — **đã biết mà vẫn vấp**, nên ghi lại đây.

### 7.3 Bộ thử ngược cổng deploy không chặn được lượt `import` — sửa trong phiên

Ban đầu đưa `sqlite3`/`datetime` giả vào **globals của `exec`**. Nhưng `MB_SCRIPT` tự
`import sqlite3, datetime` ở dòng đầu, nên lượt import **ghi đè** bản giả → script mở **DB
thật** và chết `unable to open database file`.

**Đã sửa:** thay ở `sys.modules` trước khi `exec`, khôi phục trong `finally`.
**Hậu quả nếu bỏ qua:** hoặc bộ thử không chạy được, hoặc tệ hơn — nếu máy local có DB thật
thì bộ thử sẽ đọc dữ liệu thật và cho kết quả **vô nghĩa nhưng trông như đạt**.

### 7.4 Dò sai tên cột ở lượt đầu — không kết luận theo bản dò hỏng

Lượt dò đầu dùng `final_bundles.numbers`, `model_daily_eval.bach_thu_hit`,
`predictions.region` — **cả ba đều không tồn tại**. Tên thật: `lo2`/`bach_thu` · `bt_hit` ·
`target_region`.

**Đã xử:** đọc `PRAGMA table_info` rồi dò lại bằng tên đúng, **không suy đoán từ tên cột quen
thuộc**. Không có con số nào trong báo cáo này lấy từ lượt dò hỏng.

### 7.5 Bộ tự kiểm đang có **2 phép LỆCH** — nói rõ để không ai hiểu nhầm

`C18` và `C19` đang LỆCH. **Không phải do phiên này gây ra**: cả hai mô tả cùng một sự việc
thật của **04/08** — MT official chốt **16:50:13**, cách lượt lane cuối 16:54 đúng **227 giây**
(ngưỡng 300s) và cách hạn cứng 16:58 đúng **467 giây** (ngưỡng 480s). Chúng đã LỆCH từ lượt ghi
18:05 hôm qua, **trước** khi phiên này bắt đầu.

Đây là **ngưỡng hành động của `FU-256`** (hạn 06/08), và `FU-256` tự viết là cần **đủ 2 ngày
liên tiếp** mới quyết — nên hôm nay **chưa dời lượt vá**, đúng như mục đã ghi. Không có phép
nào ở trạng thái **`LOI`** (đổ).

### 7.6 Không có vướng vấp nào phải gỡ về

Cả ba lỗi tự gây (7.1 · 7.3 · 7.4) đều sửa xong trong phiên và có bằng chứng chạy lại.

---

## 8. Gỡ về

```bash
# 1. Trả bộ tự kiểm về 21 phép
cd E:\Lottery_AI_Test
copy backups\v10988_pre\_v10900_consistency_guard.py.pre web\backend\_v10900_consistency_guard.py
scp web\backend\_v10900_consistency_guard.py root@14.225.224.89:/root/Lottery_AI_Test/web/backend/
# (bản trên VPS trước deploy: /root/Lottery_AI_Test/backups/_v10900_consistency_guard.py.v10988_pre
#  md5 05466bc600a2f420aba11ae0a02d7b7d)
ssh root@14.225.224.89 "systemctl restart lottery"

# 2. Bỏ bảng mốc giao diện
ssh root@14.225.224.89 "sqlite3 /root/Lottery_AI_Test/data/lottery_ai.db 'DROP TABLE v10988_ui_moc'"

# 3. Trả tài liệu
git checkout HEAD -- docs/FOLLOW_UP_TRACKER.md docs/CURRENT_TRUTH_SSOT.md CHANGELOG.md
git checkout HEAD -- docs/OWNER_DECISION_LEDGER.json docs/LICH_CUON_CHIEU_DEN_10082026.md
git checkout HEAD -- docs/PLAYBOOK_PERIODIC_FULL_SYSTEM_CHECK.md web/backend/_v10982_lich9.py
```

**Mất khoảng 3 phút.** Không phải gỡ gì khác: tệp deploy **chỉ ĐỌC**, không ghi vào 4 bảng
khoá (hash chứng minh), và không đụng `/du-doan`, `final_bundles` writer, hay bộ chọn model.

---

## 9. Theo dõi tiếp

| Mã máy | Mã đọc | Nhãn | Hạn | Ngưỡng hành động bằng số |
|---|---|---|---|---|
| `FU-262` | `SC0805` | `/monitoring` cắt cụt | 05/08 | **ĐÓNG `CLOSED_PASS`** |
| `FU-259` | `KS0805` | C17/C18 chưa có lượt ghi thật | 05/08 | **ĐÓNG `CLOSED_PASS`** |
| `FU-207` | `DP0805-1` | Cổng an toàn deploy | 05/08 | **ĐÓNG `CLOSED_PASS`** |
| `FU-254` | `DD0805` | 3 bảng P&L chết | 05/08 | **ĐÓNG `CLOSED_PASS`** |
| **`FU-243`** | **`SC0908`** | Canh incomplete bundle | **09/08** | `expected_output_model_count` tách theo miền và khớp thật (MN 15 · MT 13 · MB 14), **hoặc** rà `bt_gate`/`MT_top13_V10752` + dựng phép canh **cửa sổ 7 ngày** thay vì 1 ngày |
| **`FU-256`** | `DO0806` | Biên giờ chốt MT/MB co lại | **06/08** | Đọc `C19`+`C20` đủ **2 ngày liên tiếp**. **04/08 `C19` đã LỆCH lần đầu** (MT 467s < 480s) → theo đúng mục đã ghi, nếu 05/08 còn LỆCH thì **dời lượt vá muộn thêm 2 phút** |
| **`FU-252`** | `KS0810-5` | Lane Nghiệm Thu đủ 3 miền | **10/08** | Cần **21/21** ô miền-ngày; hiện **4/21**, đúng nhịp. Thiếu bất kỳ đêm nào thì cửa sổ bắt đầu lại |
| **`FU-244`** | `KS0807` | Cổng lợi thế ghi hằng ngày | *(đã đóng)* | **Phải xác nhận lại sau 19:10 tối nay** — hai cron của V10984 **chưa từng chạy thật** (không có tệp log). 06/08 vẫn không có log → **mở mục mới** |
| `FU-266` | `DD1208` | `desktop.ini` làm `git fetch` chết | 12/08 | Trước mỗi lần push: `find .git -name desktop.ini -delete` rồi xác minh bằng `git ls-tree -r origin/main` |
| `FU-225` | `UI0803` | Xác minh UI du-doan-test | 03/08 | **Đang QUÁ HẠN 2 ngày** — chờ owner nhìn tận mắt |

**Ngày rà soát `QD-026`: 2026-08-12.**

**Việc gần nhất phải làm, theo thứ tự:**

1. **Sau 19:10 tối nay 05/08** — kiểm `logs/v10945_edge_gate.log` và `logs/v10984_ghep_lane.log`
   đã sinh chưa. Đây là lượt cron **đầu tiên** của cả hai.
2. **18:05 tối nay** — đọc bảng tự kiểm ngày 05/08: phải có **22 dòng**, và xem `C19` có còn
   LỆCH không (quyết định của `FU-256` ngày mai phụ thuộc con số này).
3. **06/08** — `FU-256` · `FU-250` · `FU-258` · `FU-224` · `FU-257` · `FU-210` đến hạn.
4. **09/08** — `FU-243` cùng `FU-200` · `FU-202` · `FU-261` (ngày đầu hết đóng băng `QD-014`).

---

*Bằng chứng máy đọc: `evidence/` — 11 tệp gồm output 6 cổng kiểm, thử ngược `C22`, nghiệm thu
cổng deploy, hash trước/sau, PID trước/sau, cổng lợi thế 9 ô, trạng thái sống 05/08.*
