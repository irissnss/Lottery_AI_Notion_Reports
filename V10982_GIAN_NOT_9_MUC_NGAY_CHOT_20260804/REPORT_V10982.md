# V10982 — Giãn nốt 9 mục còn dồn ngày chốt 10/08 (`QD-022`)

| | |
|---|---|
| Ngày | 2026-08-04 (giờ Việt Nam) |
| Owner ký | ~11:0x |
| Quyết định | `QD-022`, nối tiếp `QD-021` |
| Phạm vi | **Lập kế hoạch + cập nhật tài liệu.** Không deploy, không đụng runtime |
| Cổng kiểm | `_v10982_kiem_lich9.py` 8/8 · `_v10981_kiem_lich.py` 8/8 · sổ quyết định 0 TRÔI |
| Mồ côi | 19 → **18** |

---

## 1. Tóm tắt

Phiên trước (`V10981` / `QD-021`, ký 10:29 cùng ngày) đã giãn **14 mục** cùng đáo hạn 08/08
thành lịch cuốn chiếu 04/08 → 10/08, nhưng cố ý **không đụng 9 mục đáo hạn 10/08** có sẵn từ
các phiên V10974–V10980 vì nằm ngoài phạm vi. Kết quả là ngày chốt vẫn gánh **11 mục**. Owner
đọc trang lịch, thấy chỗ đó và ký tiếp: giãn luôn 9 mục ấy.

Phiên này giãn đúng 9 mục đó ra **05 → 09/08**. **Ngày chốt 10/08 từ 11 mục xuống còn 3** —
hai mục khởi động shadow của nhóm 14 (`FU-231`, `FU-226`) cộng một mục không kéo lên được
(`FU-252`, cửa sổ đo 7 đêm kết thúc đúng 10/08, chi phí trong ngày là một câu đếm).

Ba con số đáng chú ý: **trần ≤5 mục/ngày KHÔNG đạt được** và lý do không nằm ở 9 mục này —
ngày 09/08 đã sẵn 7 mục trước khi phiên bắt đầu; **1 mục không kết luận nổi trong hạn**
(`FU-253`, sớm nhất 12/08) đã ghi thẳng thay vì hứa; và **mồ côi giảm 19 → 18** vì `FU-244`
trước phiên có ô `status` rỗng, nay được trả về nhãn thật.

---

## 2. Owner yêu cầu gì — nguyên văn

> **11:0x ngày 04/08/2026:** *"Giãn luôn 9 mục cũ đó ra 05-09/08 cho ngày chốt nhẹ nhé"*

Quyết định gốc vẫn còn hiệu lực, `QD-021` ký 10:29 cùng ngày:

> *"Giãn ra cuốn chiếu tới hết ngày 10/08 phải hoàn thành, làm lần lượt những vấn đề nào xác
> thực rõ ràng , đơn giản làm trước tới cuối cùng 10/08 phải xong"*

Hai câu này ghép lại thành ba ràng buộc: **tuần tự** · **xác thực rõ ràng và đơn giản làm
trước** · **ngày chốt 10/08 phải nhẹ**.

---

## 3. Đào bới / phát hiện

### 3.1 Chín mục đó chính xác là gì

Đọc `docs/FOLLOW_UP_TRACKER.md` bằng `_v10958_fu_reader` (bộ đọc biết 28 nhãn trạng thái, và
đọc hạn ở cả ô `**due**`, `**hạn mới**`, `**deadline**` lẫn tiêu đề `hạn DD/MM`). Trong cửa sổ
04→10/08 có **11 mục đáo hạn 10/08**, trong đó 2 thuộc nhóm 14. Chín mục còn lại:

| Mã máy | Nhãn | Mở ở phiên | Vì sao hạn 10/08 |
|---|---|---|---|
| `FU-185` | Tinh gọn lane hết hạn vẫn chạy | V10975 | Tự ghi ngưỡng *"sau 08/08"* vì sửa `.sh` + crontab |
| `FU-188` | Tồn đọng báo cáo A55 | (cũ) | Tự ghi *"không xử trong cửa sổ đóng băng FU-186, rà sau 08/08"* |
| `FU-223` | Chéo prompt cùng model GĐ4 | (cũ) | `deadline` ghi cứng 2026-08-10, chờ owner OK sau dọn model |
| `FU-244` | Cổng lợi thế không có bản ghi hằng ngày | V10975→V10978 | Hoãn vì *"thêm cron là đụng crontab production"* |
| `FU-252` | Canh lane Nghiệm Thu ra số đủ 3 miền | V10977→V10980 | Ngưỡng 21/21 ô miền-ngày trong 7 ngày |
| `FU-253` | Lane de-herd chết "database is locked" | V10977 | Ngưỡng đếm log 04→10/08 |
| `FU-254` | Ba bảng P&L chết 75 ngày | V10978 | Ngưỡng *"tới 10/08 — nối cron hoặc RETIRED"* |
| `FU-255` | Bảng cảnh báo chết + 4 bảng rỗng | V10978 | Ngưỡng *"tới 10/08 — nối writer hoặc RETIRED"* |
| `FU-257` | Cohere chết 25 ngày mà health khai đang chạy | V10978 | Ngưỡng *"tới 10/08 — bật lại log hoặc hạ đếm"* |

### 3.2 Tải thật mỗi ngày TRƯỚC phiên — đây mới là chỗ chật

Đếm cả nhóm 14, nhóm 9 và mục có sẵn của các phiên khác:

| Ngày | Nhóm 14 | Nhóm 9 | Phiên khác | Tổng trước phiên |
|---|---|---|---|---|
| 04/08 | 3 | 0 | 0 | 3 |
| 05/08 | 1 | 0 | 4 (`FU-243` `FU-259` `FU-260` `FU-262`) | **5** |
| 06/08 | 1 | 0 | 3 (`FU-245` `FU-250` `FU-258`) | **4** |
| 07/08 | 1 | 0 | 0 | 1 |
| 08/08 | 3 | 0 | 1 (`FU-201`) | **4** |
| 09/08 | 3 | 0 | 4 (`FU-200` `FU-202` `FU-224` `FU-261`) | **7** ⚠ |
| 10/08 | 2 | 9 | 0 | **11** ⚠ |

**Phát hiện quyết định cả bài toán:** ở mức trần 5, chỗ trống thật chỉ còn **6 khe**
(06/08=1 · 07/08=4 · 08/08=1) — ngày 04/08 không tính vì phiên này chạy lúc gần trưa 04/08, và
09/08 đã **vượt trần từ trước**. Nhưng phải xếp **8 mục** (mục thứ 9 là `FU-252` buộc ở lại).
Tức là trần ≤5 không thể đạt bằng cách dịch chuyển 9 mục — phải nói ra chứ không ép số.

### 3.3 QD-014 — đọc nguyên văn thay vì đoán

Bốn trong chín mục (`FU-185` `FU-188` `FU-244` và một phần `FU-253`) được các phiên trước hoãn
với lý do *"đụng production trong cửa sổ đóng băng QD-014"*. Tra thẳng
`docs/OWNER_DECISION_LEDGER.json`, `QD-014.ghi_chu`:

> *"Phạm vi đóng băng = đường TẠO SỐ CÔNG BỐ. **Được phép: sửa lỗi kỹ thuật rõ ràng, điều tra
> chỉ-đọc, viết tài liệu.** Không được: đổi roster 15 official, đổi hằng số bộ lọc combo-super,
> bật/tắt thêm lớp ghi đè."*

Và nguyên văn owner khi ký: *"Hôm qua đổi ba thứ cùng lúc, cần một tuần yên để biết chúng có
tác dụng gì không."*

Đối chiếu từng mục với 5 thứ bị cấm đích danh (roster 15 official · bộ lọc combo-super · lớp
ghi đè · `/du-doan` writer · `final_bundles` writer): **không mục nào trong 9 mục chạm bất kỳ
thứ nào**. Lý do hoãn cũ rộng hơn chữ ký của owner.

### 3.4 Nhưng có một ràng buộc THẬT mà các phiên trước chưa nêu

Đọc kỹ điều kiện hoàn thành của `FU-186` (đọc kết quả 7 ngày sau tắt lớp ghi đè, cửa sổ
02→08/08), tiêu chí thứ ba là:

> *"6 lane đã nghỉ vẫn lệch 0 ở bộ tự kiểm 18:05"*

Tiêu chí này **đang TRƯỢT** vì đúng cái rò của `FU-185`. Hai lane hết hạn chạy lúc **17:38 và
17:43**. Nếu sửa `FU-185` trước 08/08 thì tiêu chí đang đo bị lật từ TRƯỢT sang ĐẠT giữa
chừng, bảng 7 ngày của `FU-186` đọc không ra.

Thêm một ràng buộc nữa: `FU-253` đếm `database is locked` ở khung **17:40–17:43**, nơi có **5
cron đè nhau**. `FU-185` gỡ **2 trong 5 cron đó** — tức là `FU-185` **đổi luôn mẫu số của
FU-253**. Hai mục phải cùng ngày, `FU-185` chạy trước.

### 3.5 `FU-244` đang là MỒ CÔI

`FU-244` có ô `status` **rỗng** — không thuộc `TREO_STATUSES` cũng không thuộc `DONG_STATUSES`,
nên rơi khỏi mọi bộ đếm: không bị tính treo, không bị kêu quá hạn, không bị soi thiếu mã đọc.
Đây là 1 trong 19 mục mồ côi mà kiểm toán V10980 sáng nay vừa bêu.

### 3.6 `FU-223` là phụ thuộc của một mục nhóm 14

`FU-226` (nhóm 14, hạn 10/08) khai đích danh trong ô phụ thuộc: *"FU-223 (thiết kế trước)"*.
Nếu để `FU-223` cùng ngày 10/08 với `FU-226` thì thiết kế và thi hành rơi cùng một ngày — sai
thứ tự.

---

## 4. Hướng xử lý và vì sao chọn

### 4.1 Nguyên tắc xếp

Theo đúng chữ ký owner ở `QD-021`: **xác thực rõ ràng và đơn giản làm trước**, ngày chốt phải
nhẹ. Với mỗi mục xét bốn thứ: (a) có chạm 5 vùng `QD-014` cấm đích danh không, (b) độ rõ của
bằng chứng, (c) độ phức tạp, (d) phụ thuộc mục nào.

### 4.2 Ba phương án đã cân, và vì sao loại hai

| Phương án | Nội dung | Vì sao loại / chọn |
|---|---|---|
| A | Đẩy hết 9 mục sang 09/08 (ngày đầu sau đóng băng) | **Loại.** 09/08 đã sẵn 7 mục → thành 16. Chỉ dời chỗ nghẽn từ 10/08 sang 09/08, không giải quyết gì. |
| B | Chia đều 9 mục cho 05→09/08, mỗi ngày ~2 mục | **Loại.** Bỏ qua ràng buộc thật: `FU-185`/`FU-253` không được đụng trước 08/08 vì cửa sổ đo `FU-186`; `FU-223` phải trước `FU-226`. Chia đều là chia mù. |
| C | Xếp theo ràng buộc thật, chấp nhận 09/08 nặng, nói thẳng trần ≤5 không đạt | **CHỌN.** Ngày chốt về 3, mọi ràng buộc được tôn trọng, chỗ nghẽn còn lại được nêu tên kèm đề nghị cụ thể cho owner. |

### 4.3 Vì sao `FU-244` kéo lên 07/08 dù phiên trước hoãn

Cổng lợi thế `_v10945` **chỉ ĐỌC** bảng official rồi ghi vào bảng shadow của chính nó
(`edge_gate_daily`), cron đặt **19:00 giờ VN** — sau cả ba mốc FINAL (15:45 · 16:58 · 17:58)
nên không chen vào khung ra số. `QD-014` ghi rõ *"Được phép: điều tra chỉ-đọc"*. Rủi ro tiền =
**0** vì cả 6 ô (3 miền × 2 cửa sổ) đang đóng, không ô nào chạm ngưỡng 3pp/z2 của `QD-013`. Kéo
lên được thêm 3 ngày chuỗi số cho `QD-013` — có lợi, không hại.

### 4.4 Vì sao `FU-188` kéo lên 08/08 dù ghi chú cũ nói "rà sau 08/08"

`FU-188` là bù 4 báo cáo thiếu (`V10896` `V10901` `V10905` `V10906`) + commit 11 file dở trong
repo báo cáo công khai. Việc này **chỉ đụng repo báo cáo** — không runtime, không DB, không
cron. Viết báo cáo cho V10896–V10906 không đổi một dòng dữ liệu nào của cửa sổ đo `FU-186`, nên
lý do hoãn cũ không áp dụng. Xếp 08/08 vì khối lượng viết lớn nhất trong 9 mục, mà ngày đó
nhóm 14 chỉ toàn việc **ĐỌC kết quả** nên còn chỗ.

### 4.5 Vì sao `FU-252` KHÔNG kéo lên được

Ngưỡng là **21/21 ô miền-ngày trong 7 ngày**. Cron vá MB (17:46/17:50/17:54) chỉ có hiệu lực
từ đêm 03/08, nên **tối 04/08 mới là đêm thử thật đầu tiên**. Cửa sổ 7 đêm sạch 04→10/08 kết
thúc đúng ngày chốt. Kéo lên 09/08 là cắt cửa sổ còn 6 đêm — đúng cái bẫy rút ngắn cửa sổ đo
đã làm rữa V10655→V10672→V10677→V10753→V10789→V10790. Bù lại chi phí ngày 10/08 gần bằng 0:
chạy một câu đếm, không sửa gì.

### 4.6 Vì sao mở `QD-022` mới thay vì bổ sung vào `QD-021`

Đã cân hai cách. Chọn mở mới, ba lý do đo được:

1. `QD-021.theo_doi` là **14 mã cố định** và phép `K1` của `_v10981_kiem_lich.py` đếm đúng 14.
   Nhét thêm 9 mã vào là làm hỏng mệnh đề kiểm của chính `QD-021`.
2. Hai quyết định có **mệnh đề kiểm khác nhau**: `QD-021` canh trần 3 mục/ngày cho nhóm 14;
   `QD-022` canh trần 3 mục cho NGÀY CHỐT. Gộp lại thì khi trượt không biết trượt cái nào.
3. Bộ mục **không giao nhau**: 14 mục đáo hạn 08/08 (V10917–V10956) so với 9 mục đáo hạn 10/08
   (V10974–V10980).

`QD-022` trỏ ngược `QD-021` ở ô `ghi_chu`; `QD-021` giữ nguyên không sửa.

---

## 5. Đã làm gì

### 5.1 Lịch mới 04/08 → 10/08

| Ngày | Nhóm 14 (QD-021) | Nhóm 9 (QD-022) | Phiên khác | Tổng | Tính chất |
|---|---|---|---|---|---|
| **04/08** | 3 | 0 | 0 | **3** | Rõ ràng + đơn giản |
| **05/08** | 1 | 1 · `FU-254` | 4 | **6** | Sửa công cụ deploy + dọn bảng P&L chết |
| **06/08** | 1 | 1 · `FU-257` | 4 | **6** | Đào chỉ-đọc + sửa con đếm health nói sai + dọn frontend |
| **07/08** | 1 | 3 · `FU-223` `FU-244` `FU-255` | 0 | **4** | Thiết kế + dọn bảng ma · hạn chót owner quyết |
| **08/08** | 3 | 1 · `FU-188` | 1 | **5** | Hết đóng băng — đọc kết quả + trả nợ báo cáo |
| **09/08** | 3 | 2 · `FU-185` `FU-253` | 3 | **8** ⚠ | Ngày đầu động vào đường ra số + dọn cron 17:38–17:43 |
| **10/08** | 2 · `FU-231` `FU-226` | 1 · `FU-252` | 0 | **3** | **Hạn chót — chỉ còn đọc số** |

**Ngày chốt 10/08: 11 → 3 mục.**

> Bảng trên đã tính **V10982b** — xem §5.5: owner duyệt chuyển `FU-224` từ 09/08 xuống 06/08,
> nên 09/08 là **8** (không phải 9) và 06/08 là **6** (không phải 5).

### 5.2 Chi tiết từng mục

| Mã máy | Mã đọc cũ → mới | Nhãn | Hạn cũ → mới | Xong nghĩa là gì (đo bằng số) |
|---|---|---|---|---|
| `FU-254` | `KS0810-2` → `DD0805` | Ba bảng P&L chết 75 ngày | 10/08 → **05/08** | 3 bảng `pnl_daily_*` (14/28/76 dòng, dừng 2026-05-20) được chốt: nối cron, hoặc đủ 3 tên bảng có chữ `RETIRED` trong SSOT kèm câu ghi nguồn P&L chính thức là `money_board_log` + `pnl_forward_track_shadow` |
| `FU-257` | `KS0810-4` → `SC0806` | Cohere chết 25 ngày | 10/08 → **06/08** | Hoặc `cohere_rerank_log` có dòng mới, hoặc `/api/health` trả `active_rerank_measurement_model_count` = **0** và `active_measured_component_count` 27 → **26** |
| `FU-223` | `HT0810` → `HT0807` | Chéo prompt cùng model GĐ4 — thiết kế | 10/08 → **07/08** | Bản thiết kế có đủ 4 con số: danh sách model A/B · số ngày đo tối thiểu 14 (QD-017) · dự toán lượt gọi và USD/ngày · thước chấm = tỉ lệ trúng bạch thủ. Chưa chạy job nào |
| `FU-244` | `KS0810` → `KS0807` | Cổng lợi thế không có bản ghi hằng ngày | 10/08 → **07/08** | `crontab -l \| grep -c 10945` ≥ **1** và `edge_gate_daily` có dòng mới ngày ≥ ngày đặt cron (hiện 3 dòng, đều 2026-08-01). Cron đặt 19:00 |
| `FU-255` | `KS0810-3` → `DD0807` | Bảng cảnh báo chết + 4 bảng rỗng | 10/08 → **07/08** | Đủ **5/5** bảng có kết cục ghi thành chữ: `system_alerts` + 4 bảng rỗng. Đếm 5 tên bảng trong SSOT = 5 |
| `FU-188` | `BC0810` → `BC0808` | Tồn đọng báo cáo A55 | 10/08 → **08/08** | `_v10921_report_gate.py` về **0 phiên bản thiếu** và **0 commit chưa push** |
| `FU-185` | `DD0803` → `DD0809` | Tinh gọn lane hết hạn vẫn chạy | 10/08 → **09/08** | 2 dòng gọi lane trong `_mb_advanced_lane_daily.sh` bị gỡ + 2 dòng cron trùng gộp còn 1. Số dòng lane hết hạn ghi vào `du_doan_test_*` ngày 10/08 = **0** (hiện ~10/ngày) |
| `FU-253` | `SC1008` → `SC0809-1` | Lane de-herd chết "database is locked" | 10/08 → **09/08** | Đếm `database is locked` trong `logs/v10872_deherd.log` **04→08/08**. ≥2 ngày dính → bật `PRAGMA busy_timeout` hoặc giãn cron ngay 09/08. 0–1 ngày → đóng mục kèm số |
| `FU-252` | `KS1008` → `KS0810-5` | Canh lane Nghiệm Thu đủ 3 miền | **10/08 (giữ)** | **21/21 ô miền-ngày** trong 7 đêm 04→10/08 (đo lần đầu V10980 được 13/21) |

`FU-252` đổi mã đọc dù hạn không đổi: `KS1008` viết theo DDMM, đọc theo quy ước MMDD của kho
này thành 08/10 (tháng 10) — sai tháng. `KS0810-5` khớp đúng hạn 10/08.

### 5.3 Nhãn trạng thái — giữ nguyên tiến độ, trừ một ngoại lệ

Tám mục **giữ nguyên nhãn cũ** vì phiên này chỉ đổi hạn, không đổi tiến độ việc. Ngoại lệ duy
nhất: `FU-244` từ ô rỗng (mồ côi) → `MEASURED_ROOT_CAUSE`, cùng nhãn ba mục anh em cùng phiên
V10978. **Mồ côi toàn sổ 19 → 18.**

### 5.4 Bảng file × thay đổi

| File | Việc |
|---|---|
| `web/backend/_v10982_lich9.py` | **MỚI** — nguồn sự thật duy nhất của 9 mục |
| `web/backend/_v10982_kiem_lich9.py` | **MỚI** — cổng 8 phép J1–J8 |
| `web/backend/_v10982_ghi_so.py` | **MỚI** — ghi khối vào sổ theo dõi qua `prepend()`, chặn nhãn lạ trước khi ghi |
| `web/backend/_v10982_ghi_quyet_dinh.py` | **MỚI** — ghi `QD-022` |
| `web/backend/_v10982_gov.py` | **MỚI** — prepend CHANGELOG + SSOT |
| `web/backend/_v10982_probe.py` `_probe2.py` `_probe3.py` | **MỚI** — ba bộ dò chỉ-đọc (tìm 9 mục, in thân khối, soát va chạm mã đọc) |
| `web/backend/_v10981_trang_lich.py` | thêm cột nhóm 9, mục §8, tệp bằng chứng riêng |
| `docs/FOLLOW_UP_TRACKER.md` | khối V10982 · 1.051.529 → 1.071.604 ký tự (**+20.075**, prepend) |
| `docs/LICH_CUON_CHIEU_DEN_10082026.md` | sinh lại · 17.076 → 32.718 byte |
| `docs/OWNER_DECISION_LEDGER.json` | thêm `QD-022` · 23 → 24 quyết định |
| `docs/ACTIVE_ROADMAP_LEAN_HARVEST_20260619.md` | gắn ngày cho đuôi CP-L2 (`FU-185`) + CP-L3 (`FU-254` `FU-255`) |
| `CHANGELOG.md` | 1.954.070 → 1.961.243 (**+7.173**) |
| `docs/CURRENT_TRUTH_SSOT.md` | 936.424 → 943.597 (**+7.173**) |
| `artifacts/v10982_gian_9_muc.json` | **MỚI** — bảng lịch mới dạng JSON |

**Backup trước khi sửa:** `backups/v10982_pre/` (7 file, chụp trước mọi thao tác ghi).

### 5.5 V10982b — owner duyệt chuyển `FU-224` xuống 06/08 (cùng ngày, ~12:4x)

Owner đọc mục 6 của báo cáo này và chọn phương án, nguyên văn:

> *"Chuyển xuống 06/08 - 09/08 còn 8 mục"*

| | |
|---|---|
| Mục | `FU-224` · *Dọn trang frontend trùng/chết* |
| Hạn | 09/08 → **06/08** |
| Mã đọc | `UI0809` → `UI0806` (MMDD khớp hạn mới) |
| Nhãn | `OWNER_LOCK` — **giữ nguyên** |
| Kết quả | 09/08 **9 → 8** · 06/08 **5 → 6** · ngày chốt 10/08 **không đổi** |

`FU-224` **không thuộc nhóm 9** — nó ở nhóm "phiên khác", nên việc chuyển không đổi danh sách
`theo_doi` của `QD-022` và không phá mệnh đề kiểm nào. Ghi nhận vào `QD-022` dạng **bổ sung**,
không mở `QD-023`: đây là owner trả lời đúng đề nghị mà `QD-022` đưa ra, không phải quyết định
độc lập. Số quyết định vẫn **24**; mệnh đề kiểm của `QD-022` **7 → 9**.

**Cái gì GIỮ NGUYÊN:** owner duyệt việc **đổi ngày**, chưa duyệt việc xử từng trang.
`next_action` vẫn là *"Owner chọn: giữ / gộp / bỏ. Agent KHÔNG tự xoá trang."* Ngày 06/08 agent
chỉ được trình phương án.

**`docs/ACTIVE_ROADMAP_*.md`: không áp dụng** — đã soát toàn bộ, không roadmap nào tham chiếu
`FU-224`.

#### Cổng kiểm được siết thêm trong cùng phiên

Chính việc chuyển `FU-224` phơi ra một lỗ: bảng mốc tải `TAI_PHIEN_KHAC_DO_DUOC` trong
`_v10982_lich9.py` được **ghi cứng**, nên nếu chỉ đổi hạn trong sổ theo dõi mà quên bảng đó thì
mọi con số tải trong `CHANGELOG`, trang lịch và báo cáo này đều sai **mà không cổng nào bắt
được** — đúng loại xanh giả.

Đã siết phép **J5**: nay đối chiếu bảng mốc với **sổ theo dõi THẬT** (`tai_phien_khac_that()`)
và trượt nếu lệch. **Đã thử ngược để chứng minh cổng có tác dụng:** chạy cổng khi mốc đã đổi
nhưng sổ chưa đổi → J5 **TRƯỢT**, in đúng tên `FU-224` ở cả hai ngày lệch (06/08 và 09/08), exit
1. Sau khi ghi sổ thì J5 ĐẠT. Vẫn giữ **8 phép**, không thêm phép thứ 9.

**Backup V10982b:** `backups/v10982b_pre/` (8 file).

**Deploy: KHÔNG.** Phiên này là lập kế hoạch + cập nhật tài liệu. Không sửa 15 model official,
không sửa bộ lọc combo-super, không bật/tắt lớp ghi đè, không đổi crontab, không restart
service. `QD-014` còn hiệu lực hết 08/08. Vì không đụng runtime nên **không cần kiểm hash 4
bảng khoá** — không có đường nào để phiên này chạm vào chúng.

---

## 6. Cổng kiểm

| Cổng | Kiểm gì | Kết quả |
|---|---|---|
| `_v10982_kiem_lich9.py` **J1** | đủ 9 mã trong sổ theo dõi | ✅ đủ 9/9 |
| **J2** | không mã nào còn hạn sau 10/08 | ✅ 0 mã vượt |
| **J3** | mỗi mã có mã đọc §58 | ✅ 9/9 |
| **J4** | hạn thật trong sổ khớp hạn đã xếp | ✅ 9/9 khớp |
| **J5** | ngày chốt 10/08 tổng tải ≤ 3 · **(V10982b)** mốc tải "phiên khác" còn khớp sổ thật | ✅ 10/08 = **3** mục · mốc khớp 7/7 ngày · tải 3·6·6·4·5·8·3 |
| **J6** | mã đọc không đụng mã của mục khác | ✅ 0 va chạm |
| **J7** | mục không kết luận nổi trong hạn đều ghi rõ lý do | ✅ 1 mục nêu thẳng: `FU-253`→12/08 |
| **J8** | 0 mồ côi trong nhóm · tổng mồ côi toàn sổ ≤ 19 | ✅ 9/9 nhãn hợp lệ · tổng **18** (giảm 1) |
| | **`GIAN_9_MUC_DAT` · exit 0** | ✅ **8/8** |
| `_v10981_kiem_lich.py` | nhóm 14 của `QD-021` KHÔNG bị phiên này phá | ✅ **8/8** · `LICH_CUON_CHIEU_DAT` |
| `_v10920_decision_ledger.py` | code có trôi khỏi quyết định owner không | ✅ **0 TRÔI** · `QD-022` khớp **9/9** sau V10982b · 24 quyết định |
| `_v10920_session_start.py` | briefing hiện đúng số mục đến hạn mỗi ngày | ✅ đọc đúng hạn mới (`FU-254` 05/08 · `FU-257` 06/08 …); mồ côi in **18** |
| Mồ côi trước/sau | không được tăng | ✅ **19 → 18** |
| `_v10921_report_gate.py V10982` | báo cáo công khai đủ 9 phần, đã push | ✅ exit 0 |

Bằng chứng thô trong `evidence/`: `cong_kiem_J1_J8.txt` · `cong_kiem_nhom14_K1_K8.txt` ·
`so_quyet_dinh_0_troi.txt` · `briefing_dau_phien_sau.txt` · `v10982_gian_9_muc.json`.

---

## 7. Vướng vấp

### 7.1 Trần ≤5 mục/ngày — KHÔNG đạt được, nói thẳng

Yêu cầu đặt ra là tổng tải mỗi ngày ≤5. **Không đạt.** Lý do không nằm ở 9 mục này: trước khi
phiên bắt đầu, tải sẵn đã là 05/08=5 · 06/08=4 · 08/08=4 · **09/08=7**. Riêng 09/08 vượt trần
ngay từ đầu do 7 mục của phiên khác (3 nhóm 14 + `FU-200` `FU-202` `FU-224` `FU-261`), mà phạm
vi phiên này chỉ được dịch chuyển 9 mục.

Chỗ trống thật ở mức trần 5 chỉ còn **6 khe**, phải xếp **8 mục**. Phiên này nhận trần **thực
tế = 6** cho những ngày mình động vào, và để nguyên 09/08 ở mức **9**.

**Hậu quả nếu bỏ qua:** ngày 09/08 có 3 mục nặng của nhóm 14 (`FU-192` promote roster ·
`FU-216` dựng shadow · `FU-217` sửa key LSTM) cộng 2 mục dọn cron của nhóm 9 — nếu không ai
nhìn thấy con số 9 này thì đúng ngày đó sẽ vỡ, và vỡ ở ngay trước hạn chót.

**Đề nghị cụ thể cho owner (ngoài phạm vi, KHÔNG tự làm):** chuyển `FU-224` *Dọn trang frontend
trùng/chết* từ 09/08 xuống 06/08 — mục đó chỉ đụng file HTML/JS, không chạm runtime dự đoán,
kéo 09/08 từ 9 xuống 8.

> ✅ **ĐÃ XỬ cùng ngày (V10982b, ~12:4x):** owner duyệt đề nghị này, nguyên văn *"Chuyển xuống
> 06/08 - 09/08 còn 8 mục"*. **09/08 nay là 8 mục**, 06/08 lên 6. Trần ≤5 vẫn không đạt (05/08
> và 06/08 đều 6) nhưng không ngày nào vượt trần thực tế 6. Chi tiết ở §5.5.

**Vấp phụ phát hiện khi làm V10982b:** bảng mốc tải `TAI_PHIEN_KHAC_DO_DUOC` ghi cứng trong
code — chuyển `FU-224` mà quên bảng đó thì mọi con số tải in ra đều sai mà **không cổng nào bắt
được**. Đã siết phép `J5` cho đối chiếu với sổ thật, và thử ngược để chứng minh cổng trượt đúng
(xem §5.5). **Hậu quả nếu bỏ qua:** báo cáo và trang lịch tự tin in ra một bảng số cũ, owner
xếp việc theo con số sai.

### 7.2 Suýt lặp lại lỗi mồ côi của V10981b

`V10981b` (cùng ngày, 2 giờ trước) đã vấp: gán nhãn tự chế `SCHEDULED` cho 14 mục, nhãn đó
không nằm trong `TREO_STATUSES` nên **11/14 mục rơi khỏi mọi bộ đếm** ngay trong phiên đi vá
chuyện mồ côi.

**Đã phòng bằng máy, không bằng trí nhớ:** `_v10982_ghi_so.py` kiểm mọi nhãn với
`TREO_STATUSES` **trước khi ghi** và `sys.exit(1)` nếu gặp nhãn lạ; phép **J8** canh cả nhóm 9
lẫn tổng mồ côi toàn sổ. Kết quả 9/9 nhãn hợp lệ ngay lần ghi đầu.

**Hậu quả nếu bỏ qua:** 9 mục biến mất khỏi briefing đầu phiên và khỏi bộ đếm quá hạn — đến
10/08 không ai biết chúng trượt hạn, cả phiên giãn lịch thành vô nghĩa.

### 7.3 Lý do hoãn cũ rộng hơn chữ ký của owner

`FU-185` `FU-188` `FU-244` đều bị các phiên trước hoãn với lý do *"đụng production trong cửa sổ
đóng băng QD-014"*, nhưng `QD-014` chỉ đóng băng **đường tạo số công bố** và ghi rõ được phép
sửa lỗi kỹ thuật rõ ràng, điều tra chỉ-đọc, viết tài liệu. Không mục nào chạm 5 thứ bị cấm.

**Hậu quả nếu bỏ qua:** ba mục nằm im thêm 3–5 ngày không vì lý do gì, rồi dồn hết vào ngày
chốt — đúng cái đang phải đi sửa.

**Nhưng cũng không lật hết:** khi đào tiếp thì `FU-185` và `FU-253` có một ràng buộc THẬT mà
các phiên trước chưa nêu — cả hai sửa cron trong khung 17:38–17:43 trong khi tiêu chí 3 của
`FU-186` đang được đo ở đúng khung đó. Nên hai mục này vẫn nằm 09/08, chỉ khác là lý do ghi
trong sổ nay là lý do thật.

### 7.4 `FU-185` đổi mẫu số của `FU-253` — phát hiện muộn

Khi xếp xong lần đầu mới nhận ra `FU-185` gỡ 2 trong 5 cron đè nhau ở khung 17:40–17:43, tức
là nó thay đổi chính điều kiện mà `FU-253` đang đếm. Nếu để `FU-185` chạy trước rồi mới đếm cho
`FU-253` thì con số đếm được vô nghĩa.

**Đã xử:** cửa sổ đếm của `FU-253` chốt là **04→08/08** (nền sạch, trước khi dọn), và hai mục
đứng cùng ngày 09/08 theo thứ tự `FU-185` trước. Ghi vào ô `phu_thuoc` của cả hai.

### 7.5 Phiên bị gián đoạn giữa chừng

Phiên chạy đến bước phân tích xong (đã xác định 9 mục, đã soát va chạm mã đọc) thì đứt. Khi nối
lại đã tự kiểm `git status` + `git log` cả hai repo trước khi làm tiếp: xác nhận **chưa có gì
được ghi** ngoài 3 script dò chỉ-đọc, sổ theo dõi và trang lịch còn nguyên, chưa có thư mục báo
cáo. Không có file sửa dở nào phải dọn.

### 7.6 `FU-253` không kết luận nổi trong hạn — không hứa lảo

Trong hạn 09/08 chỉ xong phần **ĐẾM + SỬA**. Câu hỏi thật là *"sửa xong lane de-herd còn chết
nữa không"* — cần ít nhất 3 đêm chạy sau khi sửa (10 · 11 · 12/08). **Kết luận sớm nhất
12/08**, đã ghi vào sổ và cổng `J7` canh.

**Rủi ro `FU-252` cũng không giấu:** nếu bất kỳ đêm nào trong 04→10/08 MB lại trống thì cửa sổ
7 đêm sạch bắt đầu lại và kết luận trượt sang sau 10/08.

---

## 8. Gỡ về

```bash
# trả 9 mục về hạn 10/08 (khối V10982 nằm ở đầu docs/FOLLOW_UP_TRACKER.md, xoá khối đó là xong)
git checkout HEAD -- docs/FOLLOW_UP_TRACKER.md
git checkout HEAD -- docs/LICH_CUON_CHIEU_DEN_10082026.md
git checkout HEAD -- docs/ACTIVE_ROADMAP_LEAN_HARVEST_20260619.md

# huỷ quyết định: đổi QD-022 trang_thai -> SUPERSEDED trong docs/OWNER_DECISION_LEDGER.json
python web/backend/_v10920_decision_ledger.py

# xác nhận nhóm 14 của QD-021 vẫn nguyên
python web/backend/_v10981_kiem_lich.py
```

Bản trước khi sửa nằm ở **`backups/v10982_pre/`** (7 file). Phiên **không đụng runtime** —
không sửa 15 model official, không sửa bộ lọc combo-super, không bật/tắt lớp ghi đè, không đổi
crontab, không deploy. Gỡ về chỉ là gỡ tài liệu, **~2 phút**.

---

## 9. Theo dõi tiếp

### 9.1 Chín mục và ngưỡng hành động bằng số

| Mã máy | Mã đọc | Nhãn | Hạn | Ngưỡng hành động |
|---|---|---|---|---|
| `FU-254` | `DD0805` | Ba bảng P&L chết 75 ngày | **05/08** | 3 tên bảng có `RETIRED` trong SSOT, hoặc `crontab -l \| grep -c pnl_daily` ≥ 1 |
| `FU-257` | `SC0806` | Cohere chết 25 ngày | **06/08** | `/api/health`: `active_rerank_measurement_model_count` = 0 và `active_measured_component_count` = 26 |
| `FU-223` | `HT0807` | Chéo prompt cùng model — thiết kế | **07/08** | Thiết kế có đủ 4 con số; phải xong TRƯỚC `FU-226` (10/08) |
| `FU-244` | `KS0807` | Cổng lợi thế không có bản ghi hằng ngày | **07/08** | `crontab -l \| grep -c 10945` ≥ 1 và `edge_gate_daily` có dòng mới |
| `FU-255` | `DD0807` | Bảng cảnh báo + 4 bảng rỗng | **07/08** | 5 tên bảng có kết cục ghi trong SSOT = 5 |
| `FU-188` | `BC0808` | Tồn đọng báo cáo A55 | **08/08** | `_v10921_report_gate.py` = 0 thiếu, 0 chưa push |
| `FU-185` | `DD0809` | Tinh gọn lane hết hạn vẫn chạy | **09/08** | Dòng lane hết hạn trong `du_doan_test_*` ngày 10/08 = **0** |
| `FU-253` | `SC0809-1` | Lane de-herd "database is locked" | **09/08** | Đếm log 04→08/08; ≥2 ngày dính → sửa ngay. **Kết luận sớm nhất 12/08** |
| `FU-252` | `KS0810-5` | Canh lane Nghiệm Thu đủ 3 miền | **10/08** | **21/21** ô miền-ngày trong 7 đêm 04→10/08 |

### 9.2 Owner cần quyết gì, trước ngày nào

Không có câu hỏi **chặn** nào phát sinh từ 9 mục này. Ba mục agent tự chốt hướng theo §56
(không hỏi lại thứ đã có trong sổ) — owner không phản đối trước hạn thì làm theo:

| Mã máy | Đề xuất của agent | Phản đối trước | Vì sao tự quyết được |
|---|---|---|---|
| `FU-254` | Đánh dấu 3 bảng `pnl_daily_*` RETIRED, ghi nguồn P&L chính thức là `money_board_log` + `pnl_forward_track_shadow`, thay vì nối lại cron | **05/08** | `QD-013` đã dừng đặt tiền thật nên ba bảng thanh toán hằng ngày không còn nghiệp vụ nào đọc. Nối cron lại là nuôi bảng chết |
| `FU-257` | Hạ `active_rerank_measurement_model_count` về 0 thay vì bật lại Cohere | **06/08** | Bật lại một cấu phần đo đã ngừng 25 ngày là thêm biến số giữa lúc `QD-014` đang đòi "một tuần yên". Hạ con số cho khớp sự thật là sửa lỗi báo cáo |
| `FU-255` | Ghi RETIRED cho `system_alerts` + 4 bảng rỗng, gỡ khai báo 3 bảng chưa từng có writer khỏi `database.py` | **07/08** | Bốn bảng chưa từng có một dòng nào và 0 cron. Nếu owner muốn giữ `system_alerts` sống thì phải cấp một writer — đó mới là việc cần quyết |

Một **đề nghị thật sự cần owner** (ngoài phạm vi phiên này) — **đã được duyệt cùng ngày**:

| Việc | Trạng thái | Kết quả |
|---|---|---|
| Chuyển `FU-224` *Dọn trang frontend trùng/chết* từ 09/08 → 06/08 | ✅ **OWNER DUYỆT ~12:4x ngày 04/08** (V10982b) — *"Chuyển xuống 06/08 - 09/08 còn 8 mục"* | Đã chuyển. Mã đọc `UI0809` → `UI0806`, nhãn `OWNER_LOCK` giữ nguyên. 09/08 **9 → 8**, 06/08 **5 → 6** |

Việc còn lại của `FU-224` vẫn chờ owner và **không** được coi là đã xong: ngày 06/08 owner phải
chọn **giữ / gộp / bỏ** cho 5 hạng mục frontend. Agent chỉ trình phương án, KHÔNG tự xoá trang.

Ba mục owner phải quyết của nhóm 14 vẫn nguyên: `FU-192` và `FU-193` trước **07/08**, `FU-215`
trước **08/08** (chi tiết ở báo cáo V10981).

### 9.3 Hạn rà soát

`QD-022.ngay_ra_soat` = **2026-08-10**. Đúng ngày chốt, rà lại: 9/9 mục đã đóng chưa, mục nào
trượt hạn, `FU-253` có đúng kết luận được 12/08 không.

---

*Báo cáo do agent vận hành `Lottery_AI_Test` lập ngày 2026-08-04. Không có API key, secret hay
thông tin đăng nhập nào trong tài liệu này hoặc trong `evidence/`.*
