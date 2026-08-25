# V11037 — Đo tiến một mẫu hình owner phát hiện, và bịt cái bẫy suýt làm agent kết luận sai

**Ngày:** 08/08/2026 · **Commit riêng:** `207404c` · **Commit công khai:** `ef8cbc1` ·
**Trạng thái:** `DEPLOYED` (VPS, PID 1089328 → 1092764, health 200)

---

## 1. Tóm tắt

Owner nêu hai mẫu hình số. Cả hai đều **có thật ở đoạn gần đây** nhưng **không đứng vững khi
đo đủ**:

| Mẫu hình | Đoạn gần đây | Đo đủ trên dữ liệu sạch |
|---|---|---|
| MN∩MT có bộ 3 số, MB có hoán vị | 2/6 ngày trong tuần | 450 tổ hợp lệch ngày, **không cái nào vượt nhiễu** |
| Đuôi giải nhì MB → MN/MT hôm sau | 60 ngày cuối MN trúng bạch thủ **8 lần** vs kỳ vọng 3,7 — **kỷ lục 6,5 năm** | 1.973 ngày: z ∈ [−1,67 ; +1,84]; **5/6 năm dưới kỳ vọng** |

Đợt nóng 8/60 có **67,8%** khả năng xuất hiện đâu đó trong 6,5 năm chỉ do may rủi. Nên thay vì
kết luận, dựng **lane đo tiến 60 ngày, ngưỡng đăng ký trước**.

Trong lúc đào, lòi ra một chuyện lớn hơn: phép quét toàn lịch sử cho ra **"tín hiệu" +5,59
sigma** — hoàn toàn ảo, do **229 bản ghi đài MT bị gán `region='MN'`** năm 2020–2021. Đã dựng
bề mặt khai báo dùng chung + hai cổng canh, để phiên sau không sập lại.

## 2. Owner yêu cầu gì (nguyên văn)

> **Danh sách ĐẦY ĐỦ mọi yêu cầu trực tiếp trong phiên — xem `PHỤ LỤC C`.** Mục này chỉ
> trích các prompt lớn; owner làm việc theo dòng liên tục nên phần lớn yêu cầu nằm giữa phiên.


> *"Em hãy dựa vào DB mới nhất xem dùm anh mỗi ngày có hiện tượng này không nhé em… Trong tuần
> này có hiện tượng này liên tục không em?"* (08/08)

> *"ngày trước 3 hôm ổn hơn ah em? hoặc là MN trước 3 hôm só với MT hôm nay và MB hôm nay chẳng
> hạn em thử hết các phép thử chưa em?"* (08/08)

> *"Rồi còn 1 chỗ nữa mà anh cũng vừa thấy đó là đuôi giải 2 của MB ngày hôm trước hay về lại MN
> và MT ngày hôm sau với tỷ lệ khá cao và vị trúng khá ổn như là bạch thủ hoặc nhiều hit ah em…
> đồng thời kiểm tra dữ liệu sai có ai đang dùng không có ảnh hưởng gì không nha em? phương án
> xử lý thế nào em"* (08/08)

> *"ok đồng ý các đề xuất cho việc 1 và 2 nha em"* (08/08)

> *"Cách nào an toàn nhất , nhanh nhất , hợp lý nhất thì làm nha em về kỹ thuật em nắm tốt hơn
> anh . Tiến hành kiểm tra , dự đoán trước các tình huống nha em. Báo cáo chi tiết đầy đủ nha
> em"* (08/08)

**Owner chọn qua bảng hỏi:** deploy **gộp một lần sau Việc 1** · phạm vi đo **đủ 9 mức**.

## 3. Đào bới / phát hiện

> **Danh sách ĐẦY ĐỦ 41 phép đào bới/tra soát — kể cả 9 phép ra kết quả âm — xem `PHỤ LỤC D.1`.**


**3.1 — Hai ví dụ của owner khớp chính xác.** 07/08: MN Bình Dương G6 `1869`, MT Gia Lai G5
`4869`, MB Hải Phòng G1 `32689`. 06/08: MN Tây Ninh G5 `3617`, MT Quảng Trị G2 `93617`, MB Hà
Nội ĐB `26167`.

**3.2 — Lưới lệch ngày 225 tổ hợp.** Trung bình 20,19% · độ lệch chuẩn giữa các ô **0,89%** ·
sai số chuẩn lý thuyết **0,90%**. Hai số bằng nhau ⇒ toàn bộ biến thiên là nhiễu. Ô cao nhất
+2,84σ, trong khi kỳ vọng ô cao nhất của 225 phép nhiễu đã là +3,29σ.

**3.3 — "Tín hiệu" +5,59 sigma là ảo.** Lưới trên toàn lịch sử lộ đường chéo: MN và MT lấy cùng
ngày thì 23–24,7%, lệch ngày thì 20,1%. Tách theo năm:

| Năm | \|MN∩MT\| cùng ngày | Kỳ vọng |
|---|---|---|
| 2021 | **11,71** | 1,86 |
| các năm khác | 1,96 – 2,48 | ~2,0 |

Nguyên nhân: **229 bản ghi** đài MT gán `region='MN'` (04/2020 + 07–10/2021, COVID, MN ngưng,
MT xổ thay). Ví dụ 30/09/2021: MN = `[Bình Định, Quảng Trị, Quảng Bình]` — cả ba là đài MT.

**3.4 — Việc này ĐÃ BIẾT từ 05/07/2026.** `CHANGELOG.md:8579` và `gpt_analyzer.py:1059` đã ghi
đúng con số **229**. Owner đã ký: KHÔNG sửa dữ liệu, chỉ thu hẹp truy vấn đọc xuống 84 ngày.
Phát hiện của phiên này là **tái phát hiện**, không phải mới.

**3.5 — Mẫu hình đuôi G2-MB.** Owner nhìn đúng cho đoạn gần đây (14 ngày cuối 6 lần bạch thủ),
nhưng lag 1 — đúng giả thuyết — lại là lag **thấp nhất** trong 7 lag (9,5% vs nền 10,4%).

## 4. Hướng xử lý và vì sao chọn

**Việc 1 — đo tiến, không kết luận từ quá khứ.** Luật dự án đã ghi: *"đừng bật lại bằng
backtest, chỉ bằng đo tiến"*. Owner chọn đo đủ 9 mức; 9 phép cùng lúc có **37%** khả năng ăn
may ⇒ bắt buộc thêm **ngưỡng họ** (α = 0,05/9, z ≥ 2,539).

**Việc 2 — phương án A: đánh dấu, không sửa dữ liệu.** Ba lựa chọn đã trình owner: (A) khai báo
+ canh · (B) UPDATE 229 dòng — đụng bảng khoá, đổi hash · (C) để nguyên. Chọn A vì nó chặn đúng
cái bẫy vừa sập mà không đụng dữ liệu lịch sử, giữ nguyên quyết định owner đã ký 05/07.

## 5. Đã làm gì

| Tệp | Việc |
|---|---|
| `web/backend/_v11037_g2mb_lane.py` | **MỚI** — bảng `v11037_g2mb_lane`, 9 mức, ngưỡng đóng băng |
| `web/backend/data_quality_zones.py` | **MỚI** — nơi khai báo duy nhất vùng bẩn + hàm lọc dùng chung |
| `web/backend/_v11037_quet_nguoc.py` | **MỚI** — quét ngược §60.3, phân loại từng chỗ |
| `web/backend/_v11037_thu_cong.py` | **MỚI** — thử cổng C23/C24 (RM-15) |
| `web/backend/_v11037_deploy.py` | **MỚI** — deploy có đường lùi |
| `web/backend/main.py` | endpoint `/api/admin/v11037-g2mb-lane` (`require_admin` + `no-store`) |
| `web/frontend/monitoring.html` | panel `sectionG2mbLane`, đăng ký `Promise.all` **và** `setInterval` 60s |
| `web/backend/_v10900_consistency_guard.py` | thêm **C23** vùng đúng biên · **C24** không có dòng sai mới |
| `backtester.py` · `data_analysis.py` | chú thích chỉ đường, **không đổi hành vi** |
| 5 mặt quy tắc | «16 phép» → **«24 phép»** (số cũ đã sai từ lâu) |
| crontab VPS | `35 19 * * *` chạy lane, 88 → 89 dòng |

**Ngưỡng đăng ký trước** (tính trên 2.211 ngày sạch), đóng băng trong `_v11037_g2mb_lane.MUC`:

| Mã | Mức | Nền | Kỳ vọng/60 | Lẻ | **Họ** | Quyết? |
|---|---|---|---|---|---|---|
| M1 | MN bạch thủ | 6,1% | 3,67 | 7 | **9** | có |
| M2 | MT bạch thủ | 4,5% | 2,72 | 6 | **7** | có |
| M3 | MN/MT bạch thủ | 10,4% | 6,23 | 11 | **13** | có |
| M4 | MN nhất/nhì/ba | 22,3% | 13,37 | 19 | **22** | có |
| M5 | MT nhất/nhì/ba | 16,9% | 10,14 | 15 | **18** | có |
| M6 | MN/MT nhất/nhì/ba | 35,4% | 21,25 | 28 | **31** | có |
| M7–M9 | bất kỳ vị trí | 56–86% | — | — | — | **không** |

## 6. Cổng kiểm

Trên **VPS**, sau deploy:

```
bộ tự kiểm            → 24 phép · C23 OK 229→229 · C24 OK 0→0
_v11037_quet_nguoc.py → SẠCH, 0 chỗ chưa phân loại
_v11037_thu_cong.py   → CỔNG QUA THỬ
_v11037_g2mb_lane.py  → exit 0, cờ an toàn (0,1,0,1)
/api/health           → 200
/api/admin/v11037-g2mb-lane → 401
PID 1089328 → 1092764 · is-active = active
```

**Quét ngược phân loại 1.346 chỗ** đụng `lottery_results`: 512 chặn biên tại SQL · 2 chặn ở nơi
gọi · 4 ghi · 666 văn bản · 158 công cụ chạy tay · 2 báo cáo độ phủ · **1 production quét hết**
· 1 quét có chủ ý · **0 chưa phân loại**.

Nơi production quét hết duy nhất là `api_so_gan()` (`main.py:4035`). **Chứng minh bằng máy**
thay vì đoán: MN/MT/MB đều **0/100** đuôi có `last_seen` rơi vào vùng bẩn ⇒ ảnh hưởng **bằng 0**.

**Thử cổng (RM-15):** trạng thái sạch ⇒ `ngoai_vung=0`, cổng im. Giả lập đài MT «Gia Lai» gán
`region='MN'` ngày 2026-07-15 ⇒ `ngoai_vung=1`, **cổng bắt đúng dòng**. Thử trên DB tạm, không
chèn gì vào `lottery_results` thật.

## 7. Vướng vấp

**7.1 — Đụng số hiệu HAI LẦN.** Phiên này lấy V11035, cổng báo cáo phát hiện đã thuộc phiên khác
(`glm-5.2` rỗng ở MB) ⇒ đổi V11036; đổi xong lại thấy `_v11036_deploy.py` cũng của họ ⇒ đổi tiếp
**V11037**. Script đổi số cắt tài liệu tại đúng tiêu đề của họ, chỉ đụng phần trên.

**7.2 — Bộ quét ngược SAI BA LẦN**, cả ba đều đúng cái bẫy §60.3/RM-09 cảnh báo:
dò biên bằng chuỗi thô `"date >= ?"` nên trượt `date>=?` ⇒ sửa bằng regex · dò docstring bằng ký
tự đầu dòng nên bắt nhầm chính ví dụ trong file mình ⇒ sửa bằng **AST** · câu văn *"Fetch KQ from
lottery_results"* bị tính là truy vấn vì có chữ `from` ⇒ yêu cầu có **động từ SQL**.

**7.3 — Hash `model_daily_eval` đổi giữa phiên.** Không đoán: so với bản chụp VPS nguyên vẹn
`artifacts/live_sync/20260808_183907/from_vps/`. Kết quả: **138 dòng đổi đúng một cột `status`
`LOSE` → `NO_ANSWER`** — việc của **phiên V11036 song song**, không phải phiên này.

**7.4 — `_v10900_consistency_guard.py` local chứa khối V11023 CHƯA DEPLOY.** Đẩy nguyên bản local
là vô tình deploy hộ việc chưa xong của người khác. Xử: dựng **bản ghép = bản đang chạy trên VPS
+ đúng khối C23/C24 của phiên này**, compile trước rồi mới đẩy.

**7.5 — Không chạy thử `main.py` ở local được** (máy không có venv, thiếu `itsdangerous`). Xử:
nạp thử bằng **venv của VPS trước khi restart** — trượt thì không đụng service.

**7.6 — Thiếu RM-15 ở bản đầu.** Dựng cổng C23/C24 rồi báo "đạt" mà chưa thử. Đã bổ sung.

**7.7 — Nhãn sai tầng (RM-12).** Ghi `DEPLOYED_LOCAL` trong khi code mới chỉ ở local. Đã sửa
thành `LOCAL_CHUA_COMMIT`, nay là `DEPLOYED`.

## 8. Gỡ về

```bash
# mã: bản lưu trước khi ghi đè
ssh root@14.225.224.89 "cp /root/Lottery_AI_Test/backups/v11037_pre/*.py \
    /root/Lottery_AI_Test/web/backend/ && \
  cp /root/Lottery_AI_Test/backups/v11037_pre/monitoring.html \
    /root/Lottery_AI_Test/web/frontend/ && systemctl restart lottery"

# cron
ssh root@14.225.224.89 "crontab /tmp/cron_v11037.bak"

# bảng shadow (an toàn bỏ, không ai đọc ngoài panel)
ssh root@14.225.224.89 "sqlite3 /root/Lottery_AI_Test/data/lottery_ai.db \
  'DROP TABLE IF EXISTS v11037_g2mb_lane'"
```

`_v11037_deploy.py` tự gỡ về khi nạp thử trượt / service không active / health ≠ 200 / md5 lệch.

## 9. Theo dõi tiếp

> **Danh sách ĐẦY ĐỦ kèm ai chặn / chặn ở đâu — xem `PHỤ LỤC D.2`.**


| Mã | Nhãn | Hạn | Việc |
|---|---|---|---|
| **FU-367** · DO0710 | `WAIT_LIVE` | 07/10 | Chấm lane sau đủ 60 ngày. **Cấm** chấm sớm · sửa ngưỡng giữa chừng · dùng phần nhìn lại · dùng M7–M9 để quyết |
| **FU-366** · KS1208 | `DEPLOYED_PENDING_LIVE_VERIFY` | 12/08 | Xác nhận C23/C24 chạy thật lúc 18:05 và lane chạy 19:35 trên VPS |
| **FU-365** · DD1508 | `AWAITING_OWNER_OK` | 15/08 | Có sửa hẳn 229 dòng không (phương án B). Chỉ mở bàn nếu **C24 báo LỆCH** |
| **FU-368** · SC1308 | `MEASURED_BUT_NOT_FIXED` | 13/08 | `_v10900_consistency_guard.py` **local ≠ VPS**: local có khối V11023 chưa deploy. Drift này **có TRƯỚC** phiên này |

**Ngoài phạm vi, ghi nhận:** cổng quyết định còn **3 phép TRÔI** (QD-021, QD-022) do mục mồ côi
chờ owner quyết — `FU-354` (09/08) và bốn mục `OWNER_DECISION_NEEDED` khác. Không tự gỡ được.

---

# PHỤ LỤC A — VA CHẠM HAI PHIÊN SONG SONG (cập nhật 08/08 đêm)

Hai phiên agent làm việc **cùng lúc trên cùng kho, cùng VPS**. Phiên kia làm chuỗi
`glm-5.2 rỗng` → `NO_ANSWER` → `decide() nói dối` → `/nghiem-thu`. Phiên này làm lane G2-MB +
vùng dữ liệu bẩn. **Sáu lần va chạm** trong một tối — ghi đủ để phiên sau tránh:

| # | Va chạm | Phát hiện nhờ | Xử lý |
|---|---|---|---|
| 1 | Số hiệu **V11035** | `_v10921_report_gate.py` báo đã có `V11035_GLM52_VA_DOI_LICH` | đổi V11036 |
| 2 | Số hiệu **V11036** | thấy `_v11036_deploy.py` của họ (19:46:54) | đổi **V11037** |
| 3 | `model_daily_eval` **đổi hash** | đo hash hai lần, lệch | so bản chụp VPS ⇒ **138 dòng `LOSE`→`NO_ANSWER`**, việc của họ |
| 4 | `CHANGELOG`/`SSOT` **bị cuốn vào commit của họ** | `git status` báo *không có thay đổi* dù vừa ghi | kiểm lại: mục V11037 **còn nguyên** trong `dab632b` — không mất gì |
| 5 | **`_v11037_deploy.py` bị ghi đè** | tệp đổi nội dung sang deploy `/nghiem-thu` | khôi phục từ `207404c` thành **`_v11037_deploy_g2mb.py`** |
| 6 | **CẢ BỐN mã FU trùng** | soi tiêu đề theo **mã đọc**, không theo số | đổi mã của phiên này sang **365–368** |

## Bảng đổi mã FU (§58 cấm hai việc dùng chung số)

| Cũ | **Mới** | Việc của phiên này | Phiên kia giữ số cũ cho |
|---|---|---|---|
| FU-355 | **FU-365** · DD1508 | quyết có sửa hẳn 229 dòng · hạn 15/08 | SC2108-2 · lượt rỗng chấm LOSE |
| FU-356 | **FU-366** · KS1208 | xác minh C23/C24 chạy 18:05 · hạn 12/08 | KS0909 · `glm-5.2` rỗng ở MB |
| FU-357 | **FU-367** · DO0710 | chấm lane G2-MB sau 60 ngày · hạn 07/10 | KS1908 · `decide()` nói dối owner |
| FU-358 | **FU-368** · SC1308 | guard local ≠ VPS · hạn 13/08 | DO2209 · `/nghiem-thu` cửa sổ TRƯỚC |

Chừa khoảng **361–364** vì phiên kia cấp số liên tục (355→360 trong ít phút). Đó là **chữa
cháy, không phải cách xử** — cách xử ghi ở **FU-369**.

## Hai chỗ suýt hỏng nhờ kiểm trước khi đẩy

**A.1 — Suýt deploy hộ việc chưa xong của người khác.** Kéo bản VPS về so từng dòng thì
`_v10900_consistency_guard.py` bản local có thêm **khối V11023** (39 dòng) mà VPS không có —
việc của phiên khác, **chưa deploy**. Xử: dựng **bản ghép = bản đang chạy trên VPS + đúng khối
C23/C24 của phiên này**. Drift theo dõi ở **FU-368**.

**A.2 — Suýt restart chồng lên deploy của họ.** Kiểm trước: backfill của họ **đã chạy xong**
(`NO_ANSWER = 138` trên VPS), và bộ tệp họ đẩy **không chồng** bộ tệp của phiên này.

## Ba thứ đã cứu phiên này

1. **Cổng báo cáo A55 bắt trùng số hiệu** — không có nó thì V11035 đã trùng im lặng.
2. **So từng dòng với bản VPS trước khi đẩy**, thay vì tin bản local là đúng.
3. **Truy hash bằng bản chụp nguyên vẹn** thay vì đoán *"chắc không sao"*.

---

# PHỤ LỤC B — NGHIỆM THU CUỐI TRÊN VPS

| | |
|---|---|
| service `lottery` | **active** · PID `1089328` → **`1092764`** · ổn định từ 20:10:01 |
| `/api/health` | **200** |
| `/api/admin/v11037-g2mb-lane` | **401** (có chốt admin) |
| `/monitoring` | 401 (cần đăng nhập — đúng) |
| bộ tự kiểm trên VPS | **24 phép** · `C23 OK 229→229` · `C24 OK 0→0` |
| quét ngược trên VPS | **SẠCH**, 0 chỗ chưa phân loại |
| thử cổng trên VPS | **CỔNG QUA THỬ** |
| cron | `35 19 * * *` · crontab 88 → **89 dòng** · lưu `/tmp/cron_v11037.bak` |
| bảng shadow | `v11037_g2mb_lane` · **549 dòng / 61 ngày** · cờ `(0,1,0,1)` |

**Hash 4 bảng khoá cuối phiên:** `predictions e793ff9f` · `lottery_results 167c3670` ·
`final_bundles c91e4b4f` — **giữ nguyên**. `model_daily_eval b2551b30` — đổi do phiên song
song vá `NO_ANSWER`, **đã truy tận nơi**, không phải phiên này.

**Đường lùi đã dựng sẵn và KHÔNG phải dùng:** `/root/Lottery_AI_Test/backups/v11037_pre/`
(5 tệp) · `/tmp/cron_v11037.bak`.

---

# PHỤ LỤC C — MỤC `OWNER YÊU CẦU` ĐẦY ĐỦ (theo `PRJ-INTERACTION-LEDGER-001`)

> Owner làm việc theo dòng liên tục trong IDE, nên **phần lớn yêu cầu KHÔNG nằm trong prompt
> lớn**. Bảng này liệt kê **mọi** yêu cầu trực tiếp trong phiên, nguyên văn. Nguồn:
> `docs/SO_TUONG_TAC_OWNER.md` mục `2026-08-08`.
>
> **Về cột giờ:** phiên này chỉ có hai mốc **chứng minh được** — hook đầu phiên `19:21:34` và
> service khởi động lại xong `20:10:01`. Còn lại ghi `—`, **không suy giờ để điền cho đẹp**.

| # | giờ | NGUYÊN VĂN | loại | agent làm gì | trạng thái |
|---|---|---|---|---|---|
| 1 | ~19:20 | *«…mỗi ngày có hiện tượng này không nhé em… Thứ 6 07/08 MN có bộ số đuôi 869 - MT có cũng Bộ Số 869 --> MB có bộ số 689… Trong tuần này có hiện tượng này liên tục không em?»* | `YÊU_CẦU` | kiểm 2 ví dụ (khớp 100%), quét 2.354 ngày, phép thử ngẫu nhiên | `ĐÃ_LÀM` |
| 2 | — | *«ngày trước 3 hôm ổn hơn ah em?… em thử hết các phép thử chưa em?»* | `HỎI` | **thừa nhận chưa thử hết**; chạy 450 phép; lòi ra vùng dữ liệu bẩn | `ĐÃ_LÀM` |
| 3 | — | *«…đuôi giải 2 của MB ngày hôm trước hay về lại MN và MT ngày hôm sau… đồng thời kiểm tra dữ liệu sai có ai đang dùng không có ảnh hưởng gì không nha em? phương án xử lý thế nào em»* | `YÊU_CẦU` | đo 9 mức trên 1.973 ngày; tra sổ §56; trình 3 phương án | `ĐÃ_LÀM` |
| 4 | — | *«ok đồng ý các đề xuất cho việc 1 và 2 nha em»* | `XÁC_NHẬN` | bắt tay cả hai việc | `ĐÃ_LÀM` |
| 5 | — | *(bảng hỏi)* **«Gộp, deploy 1 lần sau Việc 1»** · **«Đo đủ 9 mức như bảng em đã trình»** | `XÁC_NHẬN` | gộp deploy; đo 9 mức **kèm ngưỡng họ** vì 9 phép ⇒ 37% ăn may | `ĐÃ_LÀM` |
| 6 | ≤20:10 | *«Cách nào an toàn nhất , nhanh nhất , hợp lý nhất thì làm nha em… Tiến hành kiểm tra , dự đoán trước các tình huống nha em. Báo cáo chi tiết đầy đủ nha em»* | `YÊU_CẦU` | bảng 7 tình huống + đường lùi; so từng dòng local vs VPS; deploy đạt | `ĐÃ_LÀM` |
| 7 | — | *«ghi nhận và cập nhật báo cáo đây đủ chi tiết nha em»* | `YÊU_CẦU` | phát hiện tệp bị ghi đè + 4 mã FU trùng; đổi 365–368; ghi 6 va chạm | `ĐÃ_LÀM` |
| 8 | — | *«Đã push báo cáo hết chưa em?… Các vấn đề anh tương tác trực tiếp đã push thành 1 bảng ghi nhận yêu cầu của owner chưa ?… cần ghi nhận trong báo cáo có chuyên mục onwern yêu cầu… Các vấn đề đào bới, tra soát, theo dõi cần liệt kê đầy đủ.»* | `YÊU_CẦU` | kiểm hai kho đã push hết; luật **đã có sẵn** ⇒ tuân thủ chứ không thêm; ghi sổ + phụ lục C/D | `ĐÃ_LÀM` |

**Chỗ code đi trước tài liệu trong phiên này:** lane + vùng dữ liệu bẩn **deploy lúc 20:10**,
tài liệu (CHANGELOG · SSOT · FOLLOW_UP · báo cáo công khai) ghi **sau đó**. Owner đã cho phép
tường minh cách làm này; ghi nhận tại `docs/SO_TUONG_TAC_OWNER.md` mục *«CHỖ CODE ĐI TRƯỚC
TÀI LIỆU»*.

---

# PHỤ LỤC D — LIỆT KÊ ĐỦ: ĐÀO BỚI · TRA SOÁT · THEO DÕI

> §57.3 mục 3 và 9 buộc **liệt kê đủ, không tóm lược** — kể cả phép đo ra kết quả **âm** hoặc
> **không kết luận được**. Rút gọn hai mục này làm người đọc sau tưởng phiên làm ít hơn thực tế.

## D.1 — Đào bới / tra soát: 41 phép, kể cả phép ra kết quả âm

| # | Phép | Kết quả |
|---|---|---|
| 1 | Kiểm 2 ví dụ owner (`869`, `617`) | **khớp 100%** |
| 2 | Quét bộ 3 số MN∩MT → MB, 2.354 ngày | 582 ngày có ≥1 cụ (24,7%) |
| 3 | Phép thử ngẫu nhiên 1 trục (dời MB, 7 lag) | thật 20,0% vs giả 17–21% ⇒ **không tín hiệu** |
| 4 | Soi chi tiết ngày 08/08 | MN∩MT = `184`, `507`; MB không có hoán vị nào |
| 5 | Biến thể lỏng (MN/MT chỉ cần hoán vị của nhau) | 3 cụ ngày 08/08 — nhưng đã là luật khác |
| 6 | Lưới 225 tổ hợp × toàn lịch sử | lộ **đường chéo**, ô cao nhất **+5,59σ** |
| 7 | Lưới 225 tổ hợp × 365 ngày | tổ hợp thật hạng **155/225** ⇒ không tín hiệu |
| 8 | Quy mô mỗi miền theo thứ | MN 49–65 bộ · MT 33–50 · MB ~23 |
| 9 | MN∩MT cùng ngày vs **khác ngày cùng thứ** | chênh +1,57 (**+10,2σ**) — khử bẫy số lượng đài |
| 10 | Quét đài xuất hiện ở **cả hai** miền | **14 đài** MT có bản ghi mang nhãn MN |
| 11 | Đếm ngày MN/MT trùng y hệt số ≥5 chữ số | **114/2.354** ngày, cụm 04/2020 |
| 12 | Tách MN∩MT **theo năm** | **2021 = 11,71** vs kỳ vọng 1,86; năm khác ~2,0 |
| 13 | Soi 2021 chi tiết (12 ngày mẫu) | 30/09/2021 MN = 3 đài **MT** ⇒ giao nhau 49 |
| 14 | Đếm bản ghi sai nhãn theo tháng | **229** — 04/2020: 11 · 07–10/2021: 218 |
| 15 | Lưới 225 tổ hợp trên **dữ liệu sạch** | tất cả ~20,2%; sd 0,89% = SE 0,90% ⇒ **nhiễu thuần** |
| 16 | Kiểm ví dụ G2-MB của owner (`94`/`43`) | MN Bình Phước ĐB `828343` — **bạch thủ**, owner đúng |
| 17 | Đo 9 mức trên 1.973 ngày, nền chính xác từng ngày | z ∈ **[−1,67 ; +1,84]** ⇒ không mức nào vượt |
| 18 | Lưới lag −3…+7 cho G2-MB | **lag 1 THẤP NHẤT** (9,5% vs nền 10,4%) |
| 19 | Số lần trúng trung bình mỗi ngày | thật 1,977 vs kỳ vọng 1,953 ⇒ **+0,024**, không «nhiều hit» |
| 20 | Riêng 60 ngày gần nhất | MN bạch thủ **13,3%** vs 6,1% (z = +2,33) |
| 21 | Chi tiết 14 ngày gần nhất | **6 lần bạch thủ** — owner nhìn đúng |
| 22 | Cửa sổ trượt 60 ngày qua 6,5 năm | 8 lần = **1/1914 cửa sổ**, kỷ lục |
| 23 | Poisson + hiệu chỉnh tìm-ở-đâu-cũng-thấy | P(có ≥1 cửa sổ như vậy) = **67,8%** |
| 24 | Tách MN bạch thủ theo năm | **5/6 năm DƯỚI kỳ vọng**; chỉ 2026 +1,37σ |
| 25 | Tính ngưỡng đo tiến 30/60/90/120 ngày | 60 ngày ⇒ **≥8** (95%) · **≥10** (99%) |
| 26 | Grep toàn bộ nơi đọc `lottery_results` | **46 tệp** |
| 27 | Đọc cửa sổ từng consumer production | sâu nhất **500 ngày** |
| 28 | Tra `CHANGELOG` + chú thích code (§56) | việc **đã biết từ 05/07/2026**, con số 229 có sẵn |
| 29 | Tính **live** ngày xa nhất từng cửa sổ | 500 ngày → `2025-03-27` ⇒ **không chạm** vùng bẩn |
| 30 | Chứng minh `api_so_gan()` không bị ảnh hưởng | MN/MT/MB đều **0/100** đuôi có `last_seen` trong vùng bẩn |
| 31 | Quét ngược phân loại nơi đọc | **1.346 chỗ**, 0 chưa phân loại — phải **sửa bộ quét 3 lần** |
| 32 | Tính ngưỡng 9 mức trên 2.211 ngày sạch | bảng ngưỡng lẻ/họ, **đóng băng trong code** |
| 33 | Nạp 61 ngày nhìn lại vào chính lane | M1 **z = +2,28** — chưa chạm ngưỡng họ 2,539 |
| 34 | Thử cổng C23/C24 (RM-15) | sạch ⇒ im · vi phạm ⇒ **bắt đúng dòng** |
| 35 | Hash 4 bảng khoá (đo 2 lần) | `model_daily_eval` **đổi** |
| 36 | Truy nguyên hash bằng bản chụp VPS | **138 dòng** `LOSE`→`NO_ANSWER` — việc phiên song song |
| 37 | So local vs VPS **từng dòng**, 5 tệp | 4 tệp **chỉ thêm** · guard **có khối V11023 lạ** |
| 38 | Kiểm phiên song song trước khi deploy | md5 + `NO_ANSWER=138` ⇒ deploy của họ **đã xong** |
| 39 | RM-01 tuổi dữ liệu | manifest `18:39:55`, **dưới 1 giờ** ⇒ đạt |
| 40 | Kiểm số hiệu còn trống (**3 lần**) | V11035 ✗ · V11036 ✗ · **V11037** ✓ |
| 41 | Kiểm mã FU trùng | **cả 4 mã** trùng ⇒ đổi sang 365–368 |

**Phép ra kết quả ÂM hoặc KHÔNG kết luận được — vẫn phải ghi:** #3 · #5 · #7 · #17 · #18 ·
#19 · #23 · #24 · #33. Chín phép này tốn công nhất và **không** cho ra «phát hiện» nào — nhưng
chính chúng là lý do phiên này **không** báo owner một quy luật không tồn tại.

## D.2 — Theo dõi còn treo: đủ, kèm ai chặn và chặn ở đâu

| Mã | Nhãn | Hạn | Việc | Ai/cái gì chặn |
|---|---|---|---|---|
| **FU-367** · DO0710 | `WAIT_LIVE` | 07/10 | Chấm lane G2-MB sau đủ **60 ngày** đo tiến | **thời gian** — cấm chấm sớm, cấm sửa ngưỡng giữa chừng |
| **FU-366** · KS1208 | `DEPLOYED_PENDING_LIVE_VERIFY` | 12/08 | Xác nhận C23/C24 chạy thật **18:05** và lane chạy **19:35** trên VPS | chờ cron chạy lần đầu |
| **FU-368** · SC1308 | `MEASURED_BUT_NOT_FIXED` | 13/08 | `_v10900_consistency_guard.py` **local ≠ VPS** (khối V11023) | cần biết V11023 có được duyệt deploy không — **drift có TRƯỚC V11037** |
| **FU-365** · DD1508 | `AWAITING_OWNER_OK` | 15/08 | Có sửa hẳn **229 dòng** sai nhãn không (phương án B) | **owner** — đụng bảng khoá, đổi hash |
| **FU-369** · HT1108 | `MEASURED_BUT_NOT_FIXED` | 11/08 | Cổng cấp số hiệu/mã FU quét **ba nơi** | chưa dựng |

**Ngoài phạm vi phiên này nhưng đang chặn cổng quyết định:** 3 phép **TRÔI** (`QD-021`,
`QD-022`) — nguồn là mục mồ côi chờ owner quyết: **`FU-354`** (hạn 09/08) cùng **`FU-315`** ·
**`FU-319`** · **`FU-320`** · **`FU-346`** mang nhãn `OWNER_DECISION_NEEDED`. Agent **không tự
gỡ được** — cần owner quyết.

---

**TanPhatAI cần làm:** đọc `docs/SO_TUONG_TAC_OWNER.md` mục **`2026-08-08`** trước khi phản
biện bất cứ điều gì về V11037 — phiên này **code đi trước tài liệu** (deploy `20:10`, tài liệu
ghi sau), và owner đã cho phép tường minh. Cập nhật theo dõi **FU-365 · FU-366 · FU-367 ·
FU-368 · FU-369** (mã đã đổi khỏi 355–358 vì trùng với phiên song song).
