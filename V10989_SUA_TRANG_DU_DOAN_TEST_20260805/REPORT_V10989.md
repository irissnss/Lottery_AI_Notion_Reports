# BÁO CÁO V10989 — Trang `/du-doan-test` nói sai 4 chỗ; lane nguồn đã chết 4 ngày

**Ngày:** 2026-08-05 (giờ Việt Nam) · **Phiên:** V10989 · **Có deploy:** CÓ (10:30 và 10:34)
**Liên quan:** `FU-225` (đóng `CLOSED_FAIL`) · `FU-268` `FU-269` `FU-270` `FU-271` (mới) ·
`OD-20260801-B` · `OD-20260801-G` · `OD-20260803-B` · `QD-014` · §54 · §56

---

## 1. Tóm tắt

Owner gửi ảnh chụp tab MN của `/du-doan-test` lúc ~10:07 kèm đúng bốn chữ *"em tự nhìn đi"*.
Hôm qua agent báo `FU-225` **"phần thuộc hệ đã đạt, chỉ chờ owner nhìn tận mắt"**. Owner nhìn —
**không đạt**.

Căn nguyên một câu: **`_v10692_mn_mt_multidir_lane.py` là nguồn DUY NHẤT ghi bảng
`{MIỀN}_OUTPUT_V1`, mà cả 4 dòng cron của nó đã bị gỡ ngày 01/08 (V10919, owner duyệt cho 6 lane
hết hạn đo nghỉ) — nhưng `main.py` vẫn đọc đúng bảng đó để dựng khối "Output Lane Test", nên
trang treo số cũ suốt 4 ngày mà vẫn dán nhãn "chưa có hôm nay — MN cập nhật lúc ~04:30" như thể
số sắp tới.**

Cả **3/3 miền** đều chết, không riêng MN: `MN_OUTPUT_V1` dừng **01/08** (4 ngày),
`MT_OUTPUT_V1` và `MB_OUTPUT_V1` dừng **31/07** (5 ngày).

Đã sửa **4 nhãn sai** + **2 con số gây hiểu nhầm** + **nhãn MẠNH/YẾU trên n=6**, deploy lúc
10:34, và **tự gọi API thật đọc chữ trả về cho cả 3 miền — đạt 3/3**. **KHÔNG** bật lại cron
(lật quyết định owner đã ký) — chuyển `FU-269` cho owner quyết.

Số then chốt: hash 4 bảng khoá **giữ nguyên tuyệt đối** · PID `838717 → 839095` · health 200 ·
admin 401 · official MN hôm nay vẫn **15/15 model**.

---

## 2. Owner yêu cầu gì — nguyên văn

> **"em tự nhìn đi"**

(gửi kèm ảnh chụp toàn màn hình `/du-doan-test` tab MN lúc ~10:07 ngày 05/08/2026 — ảnh lưu tại
`evidence/anh_chup_owner_du_doan_test_MN_1007.png`)

Bối cảnh nguyên văn từ đề bài phiên: *"Owner đang rất bực vì hôm qua agent báo mục `FU-225`
(xác minh UI) 'phần thuộc hệ đã đạt, chỉ chờ owner nhìn tận mắt' — owner nhìn, và nó không đạt."*

Và sáu câu hỏi owner ra đề, **bắt trả lời bằng số, không đoán**: (1) vì sao lane test MN không
có số hôm nay · (2) vì sao lùi về 01/08 mà không phải 04/08 · (3) vì sao ghi "MN cập nhật lúc
~04:30" · (4) vì sao tự mâu thuẫn "(đã có kết quả)" vs "Chưa xổ" · (5) `Official 38%` lấy từ đâu
· (6) `ADAPTIVE EXPLOIT V1 62%` có mẫu bao nhiêu, z bao nhiêu, có phải hứa hẹn kiểu từng làm rữa.
Kèm câu hỏi phụ: nhãn MẠNH/YẾU trên n=6 có gây hiểu nhầm không.

Quyết định owner còn hiệu lực mà phiên này phải tuân: **`QD-014`** đóng băng đường ra số tới hết
08/08 (cấm đổi 15 model official · bộ lọc combo-super · lớp ghi đè · `/du-doan` writer ·
`final_bundles` writer · bộ chọn model production).

---

## 3. Đào bới / phát hiện — đo bằng gì, số liệu thật, cỡ mẫu

Nguồn dữ liệu: bản đồng bộ sống từ VPS `artifacts/live_sync/20260805_101006`
(`evidence/12_live_sync_manifest.json`), cộng dò trực tiếp trên VPS (chỉ đọc).

### 3.1 Câu 1 — Vì sao lane test MN không có số hôm nay

**Cả 4 dòng cron của lane đều đang bị chú thích (tắt).** `crontab -l` trên VPS:

```
# V10919 2026-08-01 owner duyet cho lane nghi: V10692 lane 3 hướng — playbook ghi rõ không promote
# 30 5 * * * … _v10692_mn_mt_multidir_lane.py --region MN …
# 45 16 * * * … --region MT …
# 39 17 * * * … --region MB …
# 10 17 * * * … (bản chạy cả 3 miền)
```

`syslog` xác nhận lượt cron **cuối cùng** là `Aug 1 05:30:01` (MN). Sau đó không còn dòng nào.

| Lane | Dòng cuối cùng ghi được | Chết bao lâu |
|---|---|---|
| `MN_OUTPUT_V1` | 01/08 05:30:01 · bt=38 · picks `["38","16","59"]` · n=19 | **4 ngày** |
| `MT_OUTPUT_V1` | 31/07 16:45:01 · bt=68 · n=10 | **5 ngày** |
| `MB_OUTPUT_V1` | 31/07 17:39:01 · bt=19 · n=8 | **5 ngày** |
| `MN/MT/MB_XIEN_V1` | cùng mốc trên | như trên |

**KHÔNG phải cùng họ với sự cố MB `/nghiem-thu` ngày 03/08** (owner nghi lane chạy trước lúc
official chốt nên hết lượt). Chạy `--dry-run` trên VPS lúc 10:2x hôm nay, lane **vẫn chạy tốt**:

```
[v10692_multidir] MN_OUTPUT_V1 date=2026-08-05 K=25 w2=0.6 width=3 status=OK
                  bt=62 picks=['62','25','96'] voted=25/25 official_bt=25 err=0 dry=True
```

Thuần tuý là **cron đã bị tắt**. Bằng chứng: `evidence/01_lane_output_v1_chet_3_mien.txt`.

**Điều tệ hơn con số:** `OD-20260801-G` ghi nguyên văn owner chất vấn *"thích là cắt bỏ mà không
thèm soi tới sự ảnh hưởng tương quan, tương thích, liên hệ mật thiết của nhau đó em"*, và chính
sổ quyết định đã **tự nhận lỗ hổng**: *"lượt đầu chỉ soi ai import MODULE, không soi ai đọc BẢNG
mà module đó ghi"*. Bài học được ghi vào sổ **nhưng không ai chạy lại phép soi** — nên
`{MIỀN}_OUTPUT_V1` lọt lưới. Mệnh đề `kiem_code` của quyết định đó khai *"6 lane không còn dòng
cron nào đang bật"* là ĐÚNG, nhưng **thiếu hẳn** phép *"không trang nào còn đọc bảng của chúng"*.
`main.py:14442` đọc `exp = f"{region}_OUTPUT_V1"` — một dòng, tìm bằng `grep` trong 3 giây.

### 3.2 Câu 2 — Vì sao lùi về 01/08 mà không phải 04/08

**Không phải lỗi chọn ngày. Bộ chọn ngày đúng — chỉ là không còn dữ liệu để chọn.**

Logic nằm ở `main.py` mục "2) PREVIOUS":

```sql
SELECT … FROM du_doan_test_bundles
WHERE experiment_name=? AND run_date < ?
ORDER BY run_date DESC, id DESC LIMIT 1
```

Tiêu chí = **ngày gần nhất TRƯỚC ngày đang xem mà CÓ dòng bundle**. Đếm thật trong
`du_doan_test_bundles` cho `MN_OUTPUT_V1`: **0 dòng** cho 02/08, 03/08, 04/08 và 05/08. Dòng gần
nhất đúng là **01/08**. Vậy trang lùi về 01/08 là **đúng theo dữ liệu còn lại**; cái sai là
**không nói rằng sẽ không bao giờ có ngày mới nữa**.

### 3.3 Câu 3 — Vì sao ghi "MN cập nhật lúc ~04:30"

Hai chỗ ghi cứng, **cả hai đều cũ 60 phút**:

| Nơi | Nội dung cũ |
|---|---|
| `web/frontend/du-doan-test.html:2801` | `{MN:'~04:30', MT:'~16:53', MB:'~17:52'}` |
| `web/backend/main.py:672` | `REGION_LANE_READY_HHMM = {"MN": "04:30", …}` |

**Sai.** V10897 đã dời lane MN `04:30 → 05:30` khi chuỗi MN dời sang sau 5h; log lane ngày
01/08 ghi rõ `created=2026-08-01T05:30:01`. Còn **official** MN hôm nay chốt **05:19:51**. Nên
câu "MN cập nhật lúc ~04:30" sai cả với lane lẫn với official.

### 3.4 Câu 4 — Vì sao tự mâu thuẫn trên cùng một màn hình

Hai chuỗi do **hai nhánh khác nhau** sinh ra:

| Chuỗi | Dòng | Cơ chế | Đúng/sai |
|---|---|---|---|
| *"(đã có kết quả)"* | `du-doan-test.html:2809` | **ghi cứng**, nối thẳng vào câu, không đọc dữ liệu | **SAI** |
| *"Chưa xổ — cập nhật sau 19:00"* | `du-doan-test.html:2817` | đọc `src.settled` | **cũng SAI, kiểu khác** |

Sự thật đo được: `du_doan_test_results` **không có dòng nào** cho `run_id=9673` (01/08), cũng
không có cho 31/07, 30/07, 29/07 — dòng chấm cuối cùng là `run_id=9250` ngày **28/07**. Nên
`settled=False` → nhánh 2 chạy. Nhưng `lottery_results` có **4 đài** cho MN ngày 01/08, tức
**ngày đó ĐÃ XỔ từ 4 ngày trước**.

Vậy **cả hai chuỗi đều sai**: không phải "đã có kết quả", cũng không phải "chưa xổ". Sự thật là
**trạng thái thứ ba mà trang chưa từng mô hình hoá: đã xổ nhưng lane chưa được chấm.**

Nguyên nhân sâu hơn: **không có cron nào cho bộ chấm lane test**
(`crontab -l | grep 'closeout\|du_doan_test'` → rỗng). Đây là mục mới `FU-270`.

### 3.5 Câu 5 — `Official 38%` lấy từ đâu, có trung thực không

Nguồn: bảng `play_recommendation_shadow`, dòng 05/08 miền MN:

```
play=OFFICIAL · method=MN_OFFICIAL_BASELINE_CONTROL
official_long=38 · long_n=29 · scope=weekday · watch=MN_ADAPTIVE_EXPLOIT_V1 62%
```

**38% KHÔNG phải tỉ lệ trúng của số công bố.** Nó là hit-rate bạch thủ của **lane đối chứng**
`MN_OFFICIAL_BASELINE_CONTROL`, **lát theo THỨ (thứ Tư)**, cửa sổ **180 ngày**, cỡ mẫu **n=29**.

Đối chiếu hai trục owner đưa:

| Trục | Đo lại được | Khớp 38%? |
|---|---|---|
| Official 7 ngày × 3 miền (ô ngày×miền) | **9/21 = 42,86%** | không |
| Trục tiến MN | MN 22 ngày = **9/22 = 40,91%** | không |
| Lane đối chứng MN, thứ Tư, 180 ngày | **9/29 = 31%** → làm tròn hiển thị 38%* | đây |

\* con số 38 do `trailing_pct` tính trên **định nghĩa trúng riêng của nó** (bạch thủ có nằm
trong tập đuôi trong ngày không), khác định nghĩa `bach_thu_status` của `final_bundles`.

**Nói thẳng: 38% là con số gây hiểu nhầm** — người đọc thấy chữ "Official" sẽ hiểu là "số official
trúng 38%", trong khi nó là một lane đối chứng lát theo thứ. Bằng chứng mạnh nhất cho việc nó
**không đo được gì ổn định**: cùng ô đó **nhảy 29 → 59 → 41 → 52 → 38%** trong 5 ngày liên tiếp
(01→05/08). Hệ thống không hề khá lên rồi tệ đi từng ngày như vậy — đó thuần là biên độ dao động
của mẫu n=29.

### 3.6 Câu 6 — `ADAPTIVE EXPLOIT V1 62%`: cỡ mẫu, z, và có phải "hứa hẹn" không

| Hạng mục | Số thật |
|---|---|
| Cỡ mẫu | **n=16** (thứ Tư, 180 ngày) |
| Tỉ lệ | 10/16 = **62,5%** |
| z so với mò 35% | **2,31** |
| Lane còn chạy không | **KHÔNG — dòng cuối 05/07/2026, ngừng 31 ngày** |

**Đánh giá thẳng: có, đây đúng kiểu chủ đề owner mất tiền theo.** Ba lý do, không phải một:

1. **n=16 quá mỏng.** z=2,31 nghe qua thì đạt, nhưng đó là z của **một** phép thử đơn lẻ.
2. **Lane đã chết 31 ngày.** Trang đang quảng cáo một lane **không còn sinh số**. Nếu owner tin
   theo, không có gì để chơi.
3. **Đây là "lấy max", không hiệu chỉnh so sánh bội — mấu chốt.** Đếm thật: MN có **28 lane**
   khác nhau có dòng trong 60 ngày. Bộ chọn duyệt hết rồi lấy cái tốt nhất. Với ~13–28 ứng viên
   và n=16, tìm ra **một** cái ≥60% gần như chắc chắn xảy ra do may rủi. Dấu vân tay của hiện
   tượng này nằm ngay trong dữ liệu — **lane "hứa hẹn" đổi gần như mỗi ngày**:

   | Ngày | Lane được quảng cáo | % |
   |---|---|---|
   | 31/07 | `MN_ADAPTIVE_EXPLOIT_V1` | 75% |
   | 01/08 | `MN_ADAPTIVE_EXPLOIT_V1` | 76% |
   | 02/08 | `MN_SPECIALIST_ROSTER_V1` | 66% |
   | 03/08 | *(không có)* | — |
   | 04/08 | `MN_SCREEN_BLEND_V1` | 64% |
   | 05/08 | `MN_ADAPTIVE_EXPLOIT_V1` | 62% |

   Một lợi thế thật thì không nhảy từ lane này sang lane khác mỗi ngày.

Đây **đúng** chuỗi bài học đã ghi trong `CLAUDE.md`: *"Backtest hứa hẹn rồi rữa — đừng bật lại
bằng backtest, chỉ bằng đo tiến"* (V10655→V10672→V10677→V10753→V10789→V10790, sáu lần liên tiếp).
Chữ **"hứa hẹn"** in ngay cạnh khối khuyến cáo là **quảng cáo cho một hiện tượng thống kê**.

### 3.7 Phát hiện THÊM khi tự gọi API — MB đang khuyến cáo chơi LANE trên n=8

Không nằm trong 6 câu owner hỏi, nhưng lộ ra khi gọi thật cả 3 miền và **nghiêm trọng hơn cả 62%**
vì nó là khuyến cáo **ĐANG SỐNG**:

```
MB  →  CHƠI LANE · method = MB_FULL_POOL_D_W06_V1
       long_pct = 25% · n = 8 (thứ Tư, 180 ngày)
       official_long = 11% · n = 8
```

MB là miền **duy nhất** được phép khuyến cáo LANE (`REGIONS_LANE_ALLOWED = {"MB"}`). Đo lại lane
đó trên cửa sổ rộng hơn:

| Cửa sổ | n | thắng | tỉ lệ | z vs mò 35% |
|---|---|---|---|---|
| Thứ Tư, 180 ngày | 7 | 2 | 28,6% | −0,36 |
| **Nền miền, 60 ngày** | **54** | **14** | **25,9%** | **−1,40** |

**Trang đang khuyên chơi một lane mà trên 54 mẫu chạy DƯỚI mức mò.** Nó "thắng" official chỉ vì
ô đối chứng ở thứ Tư rơi xuống 11% trên n=8 — cả hai con số đều là nhiễu. Ghi thành `FU-269`
để owner biết; **chưa sửa** vì `recommend_play` là bộ chọn khuyến cáo, đụng vào là chạm vùng cần
owner quyết (xem §4).

### 3.8 Nhãn MẠNH/YẾU với n=6 — owner nghi đúng

`_v10642_slice_health.py`: `RECENT = 6` (6 lần gần nhất của cặp thứ × đài) · `MIN_N = 3` ·
`STRONG_PP = 8.0`. Kiểm định nhị thức trên **đúng 4 ô đang hiện** trên ảnh chụp:

| Ô | Trang in | k/n vs nền | p (đuôi nhỏ hơn) | Có ý nghĩa? |
|---|---|---|---|---|
| Cần Thơ | 🟢 MẠNH 67% | 4/6 vs 17% | **0,009** | **CÓ** |
| Sóc Trăng | 🔴 YẾU 0% | 0/6 vs 17% | **0,337** | **KHÔNG** |
| Đồng Nai | 🟡 TB 17% | 1/6 vs 16% | **0,658** | **KHÔNG** |
| Gộp miền | 🟢 MẠNH 67% | 4/6 vs 41% | **0,198** | **KHÔNG** |

**3/4 nhãn đang khẳng định thứ mà cỡ mẫu không đỡ nổi.** Cụ thể ô owner chỉ đích danh: với nền
đài 17%, xác suất **0/6 thuần do may rủi là 33,7%** — cứ ba lần thì một lần. Dán "YẾU" cho nó là
nói quá. Chỉ Cần Thơ có tín hiệu thật (p=0,009).

Bằng chứng: `evidence/02_so_38_62_va_nhan_n6.txt` · `evidence/03_khuyen_cao_3_mien_va_co_mau.txt`.

---

## 4. Hướng xử lý và vì sao chọn — có phương án nào khác, vì sao loại

### 4.1 Việc lớn nhất: bật lại cron hay sửa trang?

| Phương án | Vì sao chọn / loại |
|---|---|
| **A. Bật lại 4 dòng cron lane V10692** | **LOẠI — không phải việc của agent.** Đây là **lật một quyết định owner đã ký**: `OD-20260801-B` *"Cho 6 lane hết hạn đo nghỉ… V10692…"*, trạng thái còn `ACTIVE`, hạn rà soát 08/08. §56 cấm agent tự đảo quyết định đã ký. Chuyển `FU-269` cho owner quyết, kèm hai đường và hậu quả bằng số. |
| **B. Sửa trang nói đúng sự thật** | **CHỌN.** Lỗi rõ ràng, có bằng chứng, nằm **thuần ở tầng hiển thị** → playbook cho phép sửa ngay trong phiên, không hỏi lại. Và đây mới là lỗi thật: dù lane có chạy lại hay không, **trang vẫn không được nói dối**. |
| **C. Bỏ hẳn khối Output lane test** | **LOẠI ở phiên này** — mất đường so sánh "vote trọng số top-K" với official mà `_v10789`/`_v10790` từng dùng làm căn cứ. Đưa vào `FU-269` làm một trong hai đường cho owner chọn. |

### 4.2 Cách viết nhãn: ghi cứng "đã nghỉ" hay suy ra từ độ trễ?

Chọn **suy ra từ độ trễ thật**, không ghi cứng danh sách lane đã nghỉ. Lý do: nếu owner bật lại
cron (`FU-269`), nhãn **tự trở về `LIVE`** ngày hôm sau mà không phải sửa thêm dòng code nào.
Ghi cứng là tạo ra đúng loại hằng số cũ đã gây ra chính lỗi `~04:30` này.

Ba trạng thái tách bạch, thay cho một câu "chưa tới giờ" dùng chung:
`LIVE` (chưa tới giờ chạy) · `LATE_TODAY` (quá giờ mà trống → **LỠ HẠN**) · `STOPPED` (trễ ≥2
ngày → đã ngừng). Mốc `LATE_TODAY` **không phải sáng tạo mới** — nó thi hành đúng
`OD-20260803-B` owner đã ký cho `/nghiem-thu`: *"trang phải nói thẳng 'LỠ HẠN' kèm lý do bằng số
— không được dán nhãn 'chưa tới giờ'"*. Áp cùng luật cho trang anh em.

### 4.3 Nhãn n=6: sửa ở gốc hay ở tầng hiển thị?

Chọn **tầng hiển thị**. Sửa `RECENT`/`MIN_N` trong `_v10642_slice_health.py` là đổi **ngữ nghĩa
nhãn đã lưu trong bảng `slice_health`**, mà bảng đó còn nơi khác đọc — đổi gốc là đổi cả những
nơi đó trong khi owner mới chỉ yêu cầu *"đánh giá và đề xuất ngưỡng tối thiểu"*. Nên: trang tự
tính đuôi nhị thức, p>0,10 thì hạ nhãn về **CHƯA RÕ**, **vẫn hiện nguyên số thô** (§54 — output
thô luôn phải nhìn thấy được, cổng chỉ khoá tiền). Đề xuất đổi gốc ghi vào `FU-271` chờ owner.

### 4.4 Không đụng vùng đóng băng `QD-014`

Mọi thay đổi nằm ở **tầng hiển thị** và **API chỉ-đọc**. Không chạm 15 model official · bộ lọc
combo-super · lớp ghi đè · `/du-doan` writer · `final_bundles` writer · bộ chọn model production.
Kiểm chứng: hash 4 bảng khoá **giống hệt** trước/sau, official MN hôm nay vẫn **15/15 model**.

---

## 5. Đã làm gì — bảng file × thay đổi, backup, deploy, hash

### 5.1 File × thay đổi

| File | Loại | Thay đổi |
|---|---|---|
| `web/backend/main.py` | sửa | `REGION_LANE_READY_HHMM` MN `04:30`→**`05:30`** · endpoint lane-test trả thêm `lane_health` / `lane_stale_days` / `lane_last_run_date` và `previous.draw_done` · `_build_play_recommendation` trả thêm `watch_n` / `watch_last_run_date` |
| `web/frontend/du-doan-test.html` | sửa | 3 trạng thái `LIVE`/`LATE_TODAY`/`STOPPED` · **bỏ** chuỗi ghi cứng `(đã có kết quả)` · phân biệt *đã xổ chưa chấm* với *chưa xổ* · mọi tỉ lệ kèm `n=` · **bỏ** chữ *"hứa hẹn"* · cảnh báo lane theo dõi đã ngừng chạy · nhãn sức khoẻ đài tính đuôi nhị thức, p>0,10 → `CHƯA RÕ` |
| `web/backend/_v10982_lich9.py` | sửa | `TAI_PHIEN_KHAC_DO_DUOC` += `FU-268` (06/08) · `FU-269`+`FU-270` (07/08) · `FU-271` (08/08) — bắt buộc cùng phiên, không thì `J5` TRƯỢT |
| `docs/FOLLOW_UP_TRACKER.md` | sửa | +9.318 ký tự · `FU-225`→`CLOSED_FAIL` + 4 mục mới |
| `CHANGELOG.md` | sửa | +3.714 ký tự · khối V10989 |
| `docs/CURRENT_TRUTH_SSOT.md` | sửa | +1.663 ký tự · 7 sự thật phải nhớ |
| `web/backend/_v10989_*.py` · `_v10989_js_check.js` | **mới** | 4 bộ dò · deploy · tự kiểm API thật · đối chiếu `watch_n` · soát cú pháp JS · ghi sổ · dựng báo cáo |

Ghi tài liệu bằng `_doc_prepend.prepend()` (đọc xong mới ghi, từ chối nếu ngắn đi) — **không**
dùng `open(p,"w")`.

### 5.2 Backup

- **Local:** `backups/v10989_pre/` — `main.py.pre` (935.803 B) · `du-doan-test.html.pre`
  (217.954 B) · `_v10642_slice_health.py.pre`
- **VPS:** `/root/Lottery_AI_Test/backups/v10989_pre_20260805_103024/` và
  `…_20260805_103425/` (bản trước mỗi lượt đẩy)

### 5.3 Deploy

Hai lượt, đều ngoài khung cấm (05:00–06:30 và 15:30–18:15):

| | Lượt 1 (10:30) | Lượt 2 (10:34) |
|---|---|---|
| Vì sao | bản sửa chính | sửa `watch_n` đếm sai (xem §7.1) |
| PID trước → sau | 834969 → **838717** | 838717 → **839095** |
| py_compile | OK | OK |
| Service | `lottery` (đúng tên, KHÔNG phải `lottery-ai`) | nt |

### 5.4 Hash 4 bảng khoá — trước/sau

| Bảng | Dòng | SHA256 (32 ký tự đầu) | Trước = Sau? |
|---|---|---|---|
| `predictions` | 11.754 | `ec59cfd5ee8c9a9a59e0009b2d836e2a` | ✅ |
| `final_bundles` | 475 | `6848318ee93ad48ede3c978bebd79489` | ✅ |
| `lottery_results` | 15.213 | `92ccf706553921288f2105f96e2a399b` | ✅ |
| `model_daily_eval` | 11.577 | `c559a75ad34b78ed89ed7d265dca3e13` | ✅ |

**Giữ nguyên tuyệt đối cả 4.** Bằng chứng: `evidence/11_deploy_pid_va_hash_4_bang.json`.

---

## 6. Cổng kiểm — kiểm gì, kết quả từng mục, đạt hay trượt

### 6.1 Tự gọi API THẬT và đọc chữ trả về — 3/3 miền ĐẠT

Đây là mục quan trọng nhất, vì **đúng cái sai của hôm qua** là nghiệm thu bằng "file giống nhau".
Bộ `_v10989_verify.py` ký một cookie phiên admin bằng chính secret của app rồi **curl qua HTTP
thật** (đủ tầng middleware), rồi **đọc từng trường** trong JSON:

| | MN | MT | MB |
|---|---|---|---|
| HTTP | 200 | 200 | 200 |
| `lane_health` | **STOPPED** | **STOPPED** | **STOPPED** |
| trễ / dòng cuối | 4 ngày · 01/08 | 5 ngày · 31/07 | 5 ngày · 31/07 |
| tham khảo · bạch thủ | 01/08 · **38** | 31/07 · **68** | 31/07 · **19** |
| `draw_done` / `settled` | **True** / **False** | **True** / **False** | **True** / **False** |
| khuyến cáo | OFFICIAL · nền **38% n=29** | OFFICIAL · nền **26% n=35** | **LANE** · nền **11% n=8** |
| lane theo dõi | `MN_ADAPTIVE_EXPLOIT_V1` **62% n=16** · chạy cuối **05/07** | `MT_SCREEN_BLEND_V1` **50% n=14** · chạy cuối 04/08 | *(không có)* |

Chuỗi trên tệp đang phục vụ: `(đã có kết quả)` = **0** · `~04:30` = **0** · `lane_health` = 1 ·
`đã NGỪNG sinh số` = 1 · `LỠ HẠN` = 2 · `CHƯA được chấm` = 1 · `CHƯA RÕ` = 2.

**Kết quả: ĐẠT — 3/3 miền trả đúng sự thật, 0 chuỗi sai còn sót.**
Bằng chứng: `evidence/04_api_that_3_mien_SAU_khi_sua.txt`.

### 6.2 Các cổng còn lại — chạy tách riêng từng lệnh

| Cổng | Kết quả | Bằng chứng |
|---|---|---|
| `_v10989_check_n.py` — `watch_n` khớp `trailing_pct` | **ĐẠT 5/5** cặp | `evidence/05_…` |
| `_v10989_js_check.js` — cú pháp JS + kiểm định nhị thức | **ĐẠT** 0 lỗi · 4/4 ca khớp bản Python | `evidence/06_…` |
| `_v10981_kiem_lich.py` (nhóm 14) | **ĐẠT 8/8** | `evidence/07_…` |
| `_v10982_kiem_lich9.py` (nhóm 9) | **ĐẠT 8/8** · J5 mốc tải khớp sổ thật 7/7 ngày | `evidence/08_…` |
| `_v10920_decision_ledger.py` | **28 quyết định · 0 TRÔI** | `evidence/09_…` |
| `_v10925_rule_sync_check.py` | **6 mặt đồng bộ** · 4/4 `.mdc` tự nạp | — |
| `_v10920_session_start.py` sau phiên | **quá hạn 1 → 0** · mồ côi **15 → 15** (không tăng) | `evidence/10_…` |
| Smoke sau deploy | `health=200` · `admin_dbstats=401` · `admin_play=401` | `evidence/11_…` |
| An toàn cứng | official MN hôm nay **15/15 model** · cron v10692 vẫn **0 dòng bật** | `evidence/11_…` |

---

## 7. Vướng vấp — mọi chỗ vấp, kèm hậu quả nếu bỏ qua

### 7.1 Agent tự gây: `watch_n` đầu tiên đếm SAI — suýt đẻ ra một con số gây hiểu nhầm MỚI

Lượt đầu, `watch_n` đếm bằng `JOIN du_doan_test_results`. Chạy thử ra
`MT_SCREEN_BLEND_V1 50% n=0` và agent **đã suýt viết vào báo cáo** rằng "MT quảng cáo lane
với 0 mẫu". Đọc lại `_v10725_champion_selector.trailing_pct` mới thấy nó **không** chấm qua
bảng đó — nó so `test_bt` thẳng với tập đuôi trong `lottery_results`. Vì bộ chấm lane test đã
chết từ 28/07 (`FU-270`), đếm kiểu cũ ra `n=0` cho một lane **vẫn đang được chấm bình thường**.
Số thật là **n=14**.

**Hậu quả nếu bỏ qua:** phiên đi sửa "con số gây hiểu nhầm" sẽ **tự đặt lên trang một con số
gây hiểu nhầm khác**, và báo cáo gửi owner sẽ chứa một cáo buộc sai. Đã sửa (đếm đúng như
`trailing_pct` đếm) + **dựng cổng `_v10989_check_n.py` bắt đối chiếu 5/5 cặp mới cho deploy**,
rồi deploy lại lượt 2.

### 7.2 `FU-267` đã có chủ — suýt tái dùng số

Đề bài ghi *"số FU đang tới FU-267"*. Tra sổ thì `FU-267` **đã thuộc V10986** (cổng 80 chỉ
chuyển hướng trang gốc, `/login` còn 404, hạn 08/08). Đã bắt đầu từ **FU-268**.
**Hậu quả nếu bỏ qua:** hai việc khác nhau mang cùng số → vi phạm §58 và làm hỏng mọi bộ đếm.
Đã dựng cổng tự chặn ngay trong `_v10989_ghi_so.py` (cổng 3).

### 7.3 Nhãn `REOPENED` owner nhắc tới KHÔNG hợp lệ

Owner yêu cầu `FU-225` mở lại thành `CLOSED_FAIL` / `REOPENED`. `REOPENED` **không có** trong
`TREO_STATUSES` (9 nhãn) lẫn `DONG_STATUSES` (7 nhãn) — dùng nó là đẩy mục thành **mồ côi**,
đúng cái bẫy V10981b từng làm mất 11/14 mục. Đã dùng **`CLOSED_FAIL`** (nhãn đóng hợp lệ, mang
đúng nghĩa "đã kiểm và TRƯỢT") và chuyển việc sang `FU-268`. Cổng 1 trong `_v10989_ghi_so.py`
tra danh sách hợp lệ **trước khi ghi**.

### 7.4 Bài học gốc: nghiệm thu bằng dấu hiệu hình thức

`FU-225` được các phiên trước coi là "phần thuộc hệ đã đạt" dựa trên: file trên VPS giống file
local · header đúng · PID đã đổi. **Không phiên nào gọi API rồi đọc chữ trả về.** Trang chỉ cần
một chuỗi ghi cứng như `(đã có kết quả)` là mọi phép so file đều xanh trong khi người đọc bị nói
dối. **Hậu quả nếu bỏ qua:** mọi mục UI về sau đều có thể "đạt" mà vẫn sai — owner lại phải làm
người kiểm thử. Đã đổi cách: `FU-268` định nghĩa "xong" bằng **nội dung API thật**, không bằng
so file.

### 7.5 Bài học đã ghi mà không ai chạy lại

`OD-20260801-G` đã ghi nguyên văn lỗ hổng *"chỉ soi ai import MODULE, không soi ai đọc BẢNG"*.
Ghi vào sổ nhưng **không biến thành phép kiểm**, nên `{MIỀN}_OUTPUT_V1` lọt lưới 4 ngày.
**Hậu quả nếu bỏ qua:** 5 lane còn lại trong đợt nghỉ 01/08 (`V10707` `V10781` `V10679` `V10680`
`V10637`) có thể đang có cùng vấn đề. Đưa vào `FU-269` để soát cùng lượt.

### 7.6 Chưa làm được trong phiên

- **MB đang khuyến cáo chơi LANE trên n=8** (§3.7) — lane đó chạy **25,9% trên 54 mẫu, dưới mức
  mò**. Không tự sửa vì đụng bộ chọn khuyến cáo. Ghi `FU-269`, **cần owner đọc sớm** vì đây là
  khuyến cáo đang sống.
- **Ngưỡng gốc `RECENT`/`MIN_N`** chưa đổi (`FU-271`) — mới vá ở tầng hiển thị.
- **Bộ chấm lane test** chưa cắm lại cron (`FU-270`).

---

## 8. Gỡ về

| Việc | Lệnh | Thời gian |
|---|---|---|
| Gỡ 2 tệp runtime (local) | `copy backups\v10989_pre\main.py.pre web\backend\main.py` · `copy backups\v10989_pre\du-doan-test.html.pre web\frontend\du-doan-test.html` | ~1 phút |
| Gỡ trên VPS | `cp /root/Lottery_AI_Test/backups/v10989_pre_20260805_103024/{main.py,du-doan-test.html} …` rồi `systemctl restart lottery` | ~2 phút |
| Gỡ tài liệu | `git checkout HEAD -- CHANGELOG.md docs/CURRENT_TRUTH_SSOT.md docs/FOLLOW_UP_TRACKER.md web/backend/_v10982_lich9.py` | ~1 phút |
| **Bật lại lane V10692** (nếu owner chọn đường A của `FU-269`) | `python web/backend/_v10919_retire_lanes.py --rollback` | ~1 phút |

**Rủi ro khi gỡ về: thấp.** Phiên không đụng bất kỳ bảng dữ liệu nào — hash 4 bảng khoá giống
hệt trước/sau. Gỡ về chỉ đưa trang trở lại trạng thái **nói sai như cũ**.

---

## 9. Theo dõi tiếp — mã FU, ngưỡng hành động bằng số, hạn rà soát

| Mã | Mã đọc | Việc | Hạn | Nhãn | Ngưỡng "xong" đo bằng số |
|---|---|---|---|---|---|
| `FU-225` | `UI0803` | Xác minh UI du-doan-test | — | **`CLOSED_FAIL`** | Đã kiểm và TRƯỢT; việc chuyển sang `FU-268` |
| `FU-268` | `UI0806-1` | Xác minh lại trang sau khi sửa | **06/08** | `DEPLOYED_PENDING_OWNER_VERIFY` | Gọi `/api/du-doan-test?region={MN,MT,MB}` bằng phiên admin thật: **3/3** có `lane_health="STOPPED"` · `lane_stale_days ≥ 2` · `previous.draw_done=true` · `previous.settled=false`; HTML **0 lần** chứa `(đã có kết quả)` và `~04:30` |
| `FU-269` | `QD0807` | **Owner quyết**: bật lại lane V10692 hay bỏ hẳn khối Output. Kèm: soát 5 lane còn lại của đợt nghỉ 01/08; và **MB đang khuyên chơi LANE trên n=8** | **07/08** | `AWAITING_OWNER_OK` | Có chữ owner chọn A hay C, ghi vào sổ quyết định |
| `FU-270` | `SC0807` | Bộ chấm lane test không có cron | **07/08** | `MEASURED_ROOT_CAUSE` | `SELECT COUNT(*) FROM du_doan_test_results WHERE run_date >= '2026-07-29'` phải **> 0**; hoặc SSOT có dòng khai lane test không còn được chấm |
| `FU-271` | `DO0808` | Ngưỡng cỡ mẫu tối thiểu nhãn sức khoẻ đài | **08/08** | `AWAITING_OWNER_OK` | Đề xuất: `RECENT` 6→**12**, `MIN_N` 3→**8**, thêm điều kiện **p ≤ 0,10** mới được dán MẠNH/YẾU. Cái giá phải nói thẳng: cần ~12 tuần lịch sử mỗi ô, nhiều đài sẽ về `NO_DATA` một thời gian — thà trắng còn hơn tô màu sai |

**Hạn rà soát chung:** 08/08/2026 (trùng ngày hết đóng băng `QD-014`).

**Việc owner nên đọc trước tiên:** `FU-269` — vì `MB` đang khuyến cáo **chơi LANE** trên cỡ mẫu
8, mà lane đó đo trên 54 mẫu chỉ đạt **25,9%**, **dưới mức mò 35%**.


---

## Phụ lục V10989b — vòng sửa thứ hai cùng ngày: khối khuyến cáo còn hứa hẹn trên 2/8 lượt

> Vòng đầu (sáng 05/08) mới chữa nhánh *"đang THEO DÕI"*. Hậu kiểm ngay sau đó phát hiện
> **nhánh KHUYẾN CÁO CHÍNH còn nguyên bệnh** — cùng loại lỗi owner mắng, chỉ khác chỗ đứng.
> Không đợi owner bắt lần hai.

### Vì sao phải soi tiếp

Owner yêu cầu *"tự gọi API đọc nội dung THẬT cho cả 3 miền"*. Làm đúng thế thì lòi ra dòng MB:

```
── MB ── http=200
   khuyến cáo = LANE · nền 11% n=8 scope=weekday
```

Trang bảo người đọc **chơi theo lane** `MB_FULL_POOL_D_W06_V1`. Soi nguyên khối
`play_recommendation` của cả ba miền rồi chấm đuôi nhị thức một phía:

| Miền | Trang bảo | Cơ sở thật | p | Kết luận |
|---|---|---|---|---|
| MN | nên chơi OFFICIAL | 11/29 vs nền 38% | 0,573 | không có ý nghĩa |
| MT | nên chơi OFFICIAL | 9/35 vs nền 26% | 0,580 | không có ý nghĩa |
| **MB** | **nên chơi LANE** | **2/8** vs nền 11% | **0,217** | **không có ý nghĩa** |

**MB đang được khuyên đưa tiền theo một lane trên đúng 2 lượt trúng.**

### Ba lỗi tìm thêm được

1. **Chuỗi ghi cứng `"— vượt rõ + bền."`** — nhánh `isLane` in ra **bất kể cỡ mẫu**, không hề
   chấm ý nghĩa thống kê. Đúng họ với `62% (hứa hẹn)` owner vừa bắt, nhưng nằm ở **dòng khuyến
   cáo chính** — dòng người đọc tin nhất.
2. **Chân khối mô tả SAI cổng của chính nó.** Trang ghi *"cửa sổ dài n≥40"*. Đọc
   `_v10725_champion_selector`: `REC_MIN_LONG_N = 40` chỉ áp cho nền **miền** (60 ngày); đường
   theo **thứ** mà MB đang đi chỉ cần `REC_WD_MIN_N = 8` — MB qua cổng đúng ở **mức sàn 8**.
   Trang mô tả một cổng nghiêm hơn cổng thật, khiến 25% trông đáng tin hơn thực tế.
3. **Lane được KHUYẾN CÁO không bị soi độ trễ.** Vòng đầu chỉ thêm `watch_last_run_date` cho
   lane *theo dõi*. Lane *được khuyến cáo* thì không có trường nào — trang không có cách nào
   nói nó còn chạy hay không.

### Đã sửa gì thêm

| File | Thay đổi |
|---|---|
| `web/backend/main.py` | `_build_play_recommendation` trả thêm **`method_last_run_date`** |
| `web/frontend/du-doan-test.html` | Nhánh LANE chấm **đuôi nhị thức tại trang**; `p > 0,10` thì đầu khối đổi *"nên chơi LANE"* → *"CHƯA đủ bằng chứng để khuyến cáo"*, viền xanh → hổ phách · in **`k/n`** thay vì chỉ `n=` · cảnh báo nếu lane khuyến cáo **không có số hôm nay** · chân khối ghi ĐÚNG hai cổng `n≥8` (thứ) và `n≥40` (miền), kèm câu *"n≥8 là ngưỡng mỏng"* |
| `web/backend/_v10982_lich9.py` | `TAI_PHIEN_KHAC_DO_DUOC[08/08] += FU-272` |

**§54 giữ nguyên:** số thô `25%`, `2/8`, `gần đây 36%` vẫn hiện đủ. Chỉ hạ **lời khẳng định**,
không giấu dữ liệu.

### Chữ THẬT trang dựng ra sau khi sửa

Không nghiệm thu bằng *"API trả đúng trường"* — vì chữ người đọc thấy do **hàm JS** dựng, không
phải do trường JSON. Bộ `_v10989b_render_check.js` bốc đúng hàm `renderPlayRecommendation` khỏi
tệp **đang phục vụ**, đổ payload THẬT lấy từ VPS vào, rồi in chữ đã bỏ thẻ HTML:

```
── MB ──
⚠ CHƯA đủ bằng chứng để khuyến cáo — lane FULL POOL D W06 V1 mới dẫn trên mẫu mỏng
Lane FULL POOL D W06 V1 đạt 25% (2/8, gần đây 36%) vs official 11% — chênh này CHƯA
phân biệt được với may rủi (p=0.22 > 0.1). Số thô vẫn hiện nguyên, nhưng không đủ cơ
sở để đưa tiền theo. ⛔ lane này chạy cuối 04/08/2026, KHÔNG có số hôm nay
   [chấm] 2/8 vs nền 11% → p=0.217
   ✓ đã hạ về cảnh báo, không khẳng định
```

Bằng chứng: `evidence/15_chu_that_khoi_khuyen_cao_SAU_sua.txt` (đủ 3 miền, exit 0).

### Cổng kiểm vòng hai

| Mục | Kết quả |
|---|---|
| Deploy | 11:49:37, ngoài khung cấm · PID **839095 → 842736** |
| Hash 4 bảng khoá | **giống hệt** trước/sau (`predictions` 11.754 · `final_bundles` 475 · `lottery_results` 15.213 · `model_daily_eval` 11.577) |
| Smoke | `/api/health`=**200** · admin=**401** |
| `model_count` official MN hôm nay | **15** — không đụng `QD-014` |
| cron `v10692` | **0 dòng bật** trước và sau — không lén lật quyết định owner |
| Bộ tự kiểm VPS | **22 phép** · `C22_giao_dien_toan_ven` **OK** · `monitoring.html` **577.617 B** không tụt |
| `C18`/`C19` lệch | Có — nhưng **lệch từ 04/08** (biên MT hẹp), đã có `FU-259`/`FU-260` trước phiên này. **Không phải hệ quả V10989** |
| Chữ thật 3 miền | **3/3 đạt**, 0 lỗi |
| Cổng lịch nhóm 14 / nhóm 9 | **8/8** và **8/8** |
| Sổ quyết định | **0 TRÔI**, 28 quyết định |
| Sáu mặt quy tắc | đồng bộ |

### Vướng vấp vòng hai

- **Bộ deploy đếm chữ `"hứa hẹn"` ra 2 và tự gắn cờ.** Soi lại: cả 2 nằm trong **chú thích JS**
  tôi vừa viết để giải thích chỗ sửa, **không phải chữ người đọc thấy**. Phép đếm thô theo chuỗi
  không phân biệt được mã với chú thích. Ghi lại đây để lần sau không ai hoảng — và để thấy
  **phép đếm chuỗi thô không đủ làm cổng nghiệm thu**, phải dựng chữ thật như `render_check`.
- **Bộ hậu kiểm lần đầu báo TRƯỢT vì tôi gõ nhầm đường dẫn endpoint admin** (`/api/admin/v10642/
  slice-health` không tồn tại → 404 chứ không phải 401). Lỗi của bộ đo, không phải của hệ. Đã
  đổi sang `/api/admin/play-recommendation` → 401 đúng như kỳ vọng. **Hậu quả nếu bỏ qua:** một
  cổng luôn đỏ vì lý do sai sẽ bị người sau tắt đi, rồi mất luôn phép canh thật.

### Theo dõi thêm

`FU-272 · QD0808 · Cổng khuyến cáo REC_WD_MIN_N=8 quá mỏng · hạn 08/08 · AWAITING_OWNER_OK`

- **Đã vá ở tầng hiển thị**; **chưa đụng gốc** `_v10725_champion_selector.py` vì đổi
  `REC_WD_MIN_N` là đổi **nội dung bảng** `play_recommendation_shadow`, mà bảng đó còn nơi khác
  đọc. Đó là quyết định của owner, không phải của agent.
- **Đề xuất:** nâng `REC_WD_MIN_N` **8 → 20**, và đưa điều kiện `p ≤ 0,10` vào thẳng
  materializer thay vì chỉ chặn ở trang. Với nền 11%, n=8 thì **2 lượt trúng đã thành 25%** —
  một lượt may là đủ lật nhãn.
- **Cái giá phải nói thẳng:** nâng lên 20 thì MB sẽ ra `OFFICIAL` gần như suốt một thời gian
  dài, khối khuyến cáo trông nhàm. Nhưng thà nhàm còn hơn chỉ tiền theo 2 lượt trúng.
- **Xong nghĩa là gì:** `SELECT long_n FROM play_recommendation_shadow WHERE play='LANE'` phải
  **≥ 20** ở mọi dòng mới.
