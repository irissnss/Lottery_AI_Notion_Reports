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

| Mã | Nhãn | Hạn | Việc |
|---|---|---|---|
| **FU-357** · DO0710 | `WAIT_LIVE` | 07/10 | Chấm lane sau đủ 60 ngày. **Cấm** chấm sớm · sửa ngưỡng giữa chừng · dùng phần nhìn lại · dùng M7–M9 để quyết |
| **FU-356** · KS1208 | `DEPLOYED_PENDING_LIVE_VERIFY` | 12/08 | Xác nhận C23/C24 chạy thật lúc 18:05 và lane chạy 19:35 trên VPS |
| **FU-355** · DD1508 | `AWAITING_OWNER_OK` | 15/08 | Có sửa hẳn 229 dòng không (phương án B). Chỉ mở bàn nếu **C24 báo LỆCH** |
| **FU-358** · SC1308 | `MEASURED_BUT_NOT_FIXED` | 13/08 | `_v10900_consistency_guard.py` **local ≠ VPS**: local có khối V11023 chưa deploy. Drift này **có TRƯỚC** phiên này |

**Ngoài phạm vi, ghi nhận:** cổng quyết định còn **3 phép TRÔI** (QD-021, QD-022) do mục mồ côi
chờ owner quyết — `FU-354` (09/08) và bốn mục `OWNER_DECISION_NEEDED` khác. Không tự gỡ được.
