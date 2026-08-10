# REPORT V11055 — FU-360 BẬT CHẶN CHÉO LANE (có đối chứng) + P4 GAN LÀ ĐIỂM HỘI TỤ

**Ngày:** 2026-08-10 · **Quyết định owner:** `QD-055` · **Mã đọc:** `CL1008` · `GH1008`
**Trạng thái production:** PID `1286954` · health 200 · hash 4 bảng khoá **PRE = POST y hệt**

---

## 1. Tóm tắt

Hai việc owner duyệt trong một câu: *«FU360, Và P4 luôn nha em cái này hiếm gặp ==> tiến hành»*.

| việc | kết quả | tầng verdict |
|---|---|---|
| **FU-360** chặn ghi đè **chéo lane** | **DEPLOYED 10:06** · thử chặn **5/5 + đối chứng** · canh 24h chạy | `DEPLOYED_CANH_24H` — đóng **sáng 11/08** |
| **P4** gan làm **điểm hội tụ** | **đo xong**: gộp 3 miền **−0,94pp · CI95 [−5,5 … +3,6]** ⇒ **không có lợi thế đáng kể** | `MEASURED_SHADOW_ONLY` — **chưa bật** |

Hai thứ đáng kể hơn cả hai việc trên:

1. **Bài thử FU-360 của chính agent đã nói dối HAI LẦN theo HAI CHIỀU NGƯỢC NHAU** — báo `5/5`
   khi chưa chứng minh gì, rồi báo `2/5` vu oan cho bản vá đúng. Gốc: **phán quyết phụ thuộc giờ
   treo tường**.
2. **P4 lộ ra một cơ chế đang sống trên đường chọn số làm NGƯỢC HẲN thiết kế owner**:
   `_apply_hot_cold_post_filter` **dìm số gan cao xuống ×0,3** trước khi vào top-10.

**Không đụng:** prompt · đường chọn số · roster · `/du-doan` · 4 bảng khoá.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«FU360, Và P4 luôn nha em cái này hiếm gặp ==> tiến hành»* — 10/08/2026

Điều kiện đã ký từ trước cho FU-360 (Q3, 09/08 13:58):

> *«Deploy trước 15:30 · thử chặn thật ngay sau deploy (khác run_source bị CHẶN, cùng run_source
> QUA) · canh 24h · sáng 11/08 mới đóng. Rollback ngay nếu thử chặn không đạt.»*

Thiết kế P4 do owner mô tả (09/08):

> *«gan chỉ là điểm hội tụ không nằm trong gan thì cũng đâu có ảnh hưởng, còn trước đây thì cứ đề
> +điểm nên bực ah em, nếu trong số có trong gan thì hội tụ mới được đề xuất… đề xuất không có
> trong gan thì gan vô giá trị giống như anh đang tắt gan thôi.»*

> *«gan điều kiện soi với giải 8 và giải đặc biệt nha em, MB thì gan đang soi với giải đặc biệt…
> chú ý các giải đặt biệt là các giải ÍT BỘ SỐ chứ không phải là giải đặc biệt trong đài.»*

---

## 3. Đào bới / phát hiện — kết quả đo được

### 3.1 · Bài thử FU-360 nói dối hai lần, theo hai chiều ngược nhau

| lần | khi nào | nói gì | vì sao sai |
|---|---|---|---|
| ① | 09/08 ~14:00 | **5/5 ĐẠT** | ghim cứng `date=2026-08-09` + miền **MN**, mà mốc freeze MN là **15:45**. Chạy **trước** 15:45 ⇒ cơ chế freeze **còn ngủ** ⇒ năm phép đi trót lọt mà **chưa chứng minh được gì** |
| ② | 10/08 09:58 | **2/5 TRƯỢT** | chạy **sau** mốc đó 18 tiếng ⇒ freeze **thức**, chặn phép 2 và phép 5. Phép 3 thì bản vá **chặn ĐÚNG** — dòng `[CHAN CHEO LANE]` in rành rành, số cũ giữ nguyên — nhưng assert lại viết `rs == "rerun_post_mt"`, tức **giả định phép 2 đã ghi đè thành công** ⇒ trượt oan |

**Cổng mà phán quyết đổi theo lúc bấm nút thì không phải cổng** (RM-15). Và ba dòng "trượt" đều
in `[FREEZE_LATE_*]`, **không dòng nào** in `[CHAN CHEO LANE]` — đọc con số mà không đọc **nhãn
cơ chế** là đúng RM-09.

### 3.2 · Ngưỡng gan đang chạy đều nằm DƯỚI trung vị rất xa

| miền | phạm vi gan | nền hẹp 1 ngày | trung vị gan THẬT | ngưỡng ĐANG CHẠY | ⇒ cờ bật cho |
|---|---|---|---|---|---|
| MN | G8+ĐB | 6,04% | **12** ngày | 7 | **65%** số |
| MT | G8+ĐB | 4,52% | **15** ngày | 7 | **72%** số |
| MB | ĐB | 1,00% | **68** ngày | 15 | **86%** số |

Trung vị lý thuyết `ln0,5/ln(1−p)` = **11,0 · 14,5 · 69** — khớp số đo. Cờ bật gần như **thường
trực** ⇒ cộng điểm cho gần như **mọi** số. **Lỗi nằm ở NGƯỠNG, không ở Ý TƯỞNG.**

*(Trực giác owner «MN/MT không quá 5 ngày là nổ» ứng với phạm vi **rộng** — đuôi ra ở bất kỳ giải
nào, nền ~43%. Hai phạm vi lệch nhau **7–24 lần** và đã làm agent kết luận sai một lần rồi.)*

### 3.3 · Kết quả đo P4 — gộp 3 miền, phân tầng Mantel–Haenszel, ngưỡng đăng ký TRƯỚC 15/15/60

| phép | chênh | CI95 | z | n | MDE | kết |
|---|---|---|---|---|---|---|
| **B · pool** 10 số/ngày | **−0,94pp** | **[−5,5 … +3,6]** | −0,24 | 2148+2701 | **4,62pp** | **KHÔNG có lợi thế đáng kể — CI đã loại trừ +5pp** |
| **A · bạch thủ** | +1,95pp | [−12,6 … +16,5] | +0,47 | 201+288 | 14,62pp | chưa được phép kết luận (RM-04) |
| **C · luật phản thực** (McNemar) | 70 vs 64 ngày | — | +0,30 | 134 cặp lệch | — | chưa được phép kết luận |

**Vì sao BẮT BUỘC phải gộp:** MDE từng miền là **15pp** (pool) và **26–32pp** (bạch thủ) trong
khi hiệu ứng chỉ 3–6pp — **thiết kế đo yếu hơn hiệu ứng khoảng ba lần**. `n` cần cho +5pp là
**1.513–2.199 ngày/nhóm** = **4–6 năm**. Gộp 3 miền đưa MDE về **4,62pp**, vừa đủ chạm.

**Vì sao phải PHÂN TẦNG chứ không cộng dồn thô:** nền bạch thủ ba miền lệch xa nhau
(42,9% · 38,7% · 21,5%); cộng thô thì tỉ lệ bị kéo theo **tỉ trọng miền** chứ không theo gan —
đúng nghịch lý Simpson.

**Dấu đảo chiều giữa các thước trong cùng một miền** (MT pool −2,6pp nhưng bạch thủ +14,6pp;
MB pool −3,6pp nhưng luật C +9,1pp) — đúng RM-04: n nhỏ **không ổn định**, không phải «yếu».

### 3.4 · Phát hiện nặng nhất — và nó lật ngược cách đọc chính con số ở 3.3

`combo_super._apply_hot_cold_post_filter` **đang sống trên đường chọn số**: 4 điểm gọi
(`combo_super.py:2029` · `main.py:7892 · 8099 · 8352`), **y hệt trên VPS**, **không có công tắc tắt**.

```
HOT ×1,5 · WARM ×1,2 · COOL ×0,7 · COLD ×0,6 (gan≤8) hoặc ×0,3 (gan>8)   → rồi SẮP XẾP LẠI
```

Ba hệ quả:

1. Số **gan cao** bị **dìm tới ×0,3** *trước khi* vào top-10 ⇒ pool mà phép đo 3.3 đang soi
   **đã bị trừng phạt vì có gan**. Đo giá trị của gan trên một pool đã phạt gan là **luẩn quẩn**.
2. Cơ chế này làm **ngược hẳn** thiết kế owner (gan cao = điểm hội tụ đáng **xác nhận**).
3. Đây là **§60 «bỏ nửa chừng» theo chiều ngược**: V11001 gỡ gan/nóng/lạnh khỏi **prompt** nhưng
   **cơ chế nhân điểm trong mã vẫn nguyên**.

---

## 4. Hướng xử lý và vì sao chọn phương án này

### 4.1 · FU-360 — vì sao so theo LANE chứ không so chuỗi `run_source`

Câu chữ owner là *«khác run_source bị CHẶN»*. Làm đúng chữ sẽ **hỏng production ngay**: đường
chính thức vốn đi qua **nhiều nhãn nối tiếp** — `auto_daily` → `rerun_post_mn`/`rerun_post_mt` →
`rerun_after_verify` (đo trên DB: **9 giá trị** `run_source`, **6** thuộc đường chính thức). Cái
cần chặn là **bắc cầu GIỮA HAI LANE**, không phải mọi thay đổi nhãn. Nên phép so là **lane**.

`run_source` rỗng ⇒ **không chặn** — thà cho qua còn hơn chặn nhầm dòng lịch sử chưa gắn nhãn.

### 4.2 · Vì sao rollback ngay lúc 10:01 dù nghi bài thử sai

Owner ký *«rollback ngay nếu thử chặn không đạt»*. Lúc thấy `2/5`, agent **chưa** biết lỗi nằm ở
bài thử hay ở bản vá. **Gỡ về trước, mổ sau** — đó là thứ tự đúng, và cũng là điều kiện đã ký.

### 4.3 · Vì sao P4 chỉ ĐO, không BẬT

- **QD-041 khoá đường chọn số tới 21/08.**
- Số retro chỉ đủ tư cách **sơ tuyển**. Bài học đứng cả kho: *«đừng bật lại bằng backtest, chỉ
  bằng đo tiến»* — V10655→V10672→V10677→V10753→V10789→V10790, **sáu lần** hứa rồi rữa.
- Và như 3.4, retro đang đo trên pool đã bị méo ⇒ càng không đủ tư cách để bật.

---

## 5. Đã làm gì (deploy)

| # | việc | bằng chứng |
|---|---|---|
| 1 | Backup `database.py` · `main.py` · `monitoring.html` · `crontab` trên VPS | `backups/*.pre_v11052` · `*.pre_v11055` · `crontab.pre_v11055.txt` (134 dòng) |
| 2 | Deploy `database.py` (FU-360) | md5 (bỏ `\r`) VPS = git = `b11059d889c67ca64044811d1147dd79` |
| 3 | **Thử chặn TRƯỚC khi kích hoạt**, rồi mới restart | 5/5 + đối chứng, chạy trên chính VPS |
| 4 | Viết lại bài thử cho **trung tính thời gian** + thêm **đối chứng** | ngày thử = **hôm nay +30**; `--doi-chung <bản chưa vá>` |
| 5 | Dựng bảng shadow `gan_hoi_tu_shadow_v11055` | **489 dòng** trên production |
| 6 | API `/api/admin/gan-hoi-tu-shadow` | `require_admin` + `no-store`, **chỉ đọc** |
| 7 | Panel `/monitoring` §52B | đăng ký **cả** `loadAllSections` **lẫn** `setInterval` 60s |
| 8 | Cron **21:40** hằng ngày (sau settle 21:30) | crontab 134 → **135** dòng |
| 9 | Ghi `QD-055` vào sổ quyết định | **5/5 phép** máy kiểm đạt, **0 quyết định trôi** |

**Restart:** PID `1207732` → `1284725` (thử) → `1285083` (rollback) → `1285643` (bật lại) →
`1286954` (đẩy P4). Mỗi lần đều so PID trước/sau · health 200 · `/du-doan` 200 · admin 401 ·
**0 dòng lỗi**.

**Hash 4 bảng khoá — PRE = POST y hệt suốt cả phiên:**

```
predictions      12159 / 296f3a98bfd0
final_bundles      490 / e486071f2fa3
lottery_results  15247 / 07701c83c83a
model_daily_eval 11982 / 13034d9f5187
```

---

## 6. Cổng kiểm — xác minh

| cổng | lệnh | kết quả |
|---|---|---|
| chặn chéo lane | `_v11052_thu_chan_cheo_lane.py --doi-chung <bản chưa vá>` | **A: 5/5 CHẶN · B: đối chứng LỌT** ⇒ `CHAN_CHEO_LANE_V11052=DAT` |
| §52 cho P4 | `_v11055_kiem_p4.py --thu-chan` | **6/6 + thử chặn ĐẠT** ⇒ `P4_GAN_HOI_TU_V11055=DAT` |
| canh 24h | `_v11055_canh_chan_cheo_lane.py` | 0 dòng — **đúng dự kiến**, exit 0 |
| sổ quyết định | `_v10920_decision_ledger.py` | **KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI** |
| tuổi dữ liệu | RM-01 trong `_v11055_gan_hoi_tu.py` | manifest **0,1 giờ** ⇒ ĐẠT |
| đối chiếu hàm thật | RM-10 trong cùng script | so với `database.get_all_tails` — **lệch 0** |

**Đối chứng là phần làm cổng có nghĩa:** bản **đã vá** chặn, bản **chưa vá** lọt. Cổng không phân
biệt được hai bản thì nó đang đo **thứ khác**.

---

## 7. Vướng vấp — lỗi tự gây và bài học

| # | vấp | gốc | quy tắc |
|---|---|---|---|
| 1 | Bài thử báo **5/5 giả** rồi **2/5 oan** | phán quyết phụ thuộc **giờ treo tường** (ngày thử ghim trùng mốc freeze MN 15:45) | **RM-15** |
| 2 | Suýt kết luận bản vá đúng là hỏng | đọc con số `2/5` mà không đọc **nhãn cơ chế** — ba dòng "trượt" đều là `[FREEZE_LATE_*]` | **RM-09** |
| 3 | Cổng P4 báo "endpoint có câu ghi" | mẫu `UPDATE` khớp **`d.update({`** — dict method của Python, không phải SQL | `A58_VIOLATION_RAW_COUNT` |
| 4 | Cổng P4 báo **xanh giả** ở K4 | cửa sổ "4000 ký tự cho chắc" **tràn qua** khối `setInterval` (dài ~1.200) và nuốt luôn **định nghĩa hàm** ⇒ nhầm **định nghĩa** thành **đăng ký** | **RM-15** — chính `--thu-chan` lộ ra |
| 5 | Đối chứng chết khi nạp module | tệp backup tên `database.py.pre_v11052`, **đuôi không phải `.py`** ⇒ `spec_from_file_location` trả `None` | — |
| 6 | Dòng cron ghi vào có `\&\&` nguyên văn | escape SSH lọt vào crontab | phải ghi qua **tệp**, không qua chuỗi SSH |
| 7 | `str.replace` khớp **0 lần** trên `main.py` | kho dùng **CRLF**, chuỗi so có `\n` | bẫy CRLF — **lần thứ 6** trong hai ngày |
| 8 | `kiem_code` trong sổ báo trôi 3 phép | `chay_lenh` là **list argv**, không phải một chuỗi có dấu cách; và dấu hiệu tìm phải **đúng nguyên văn có dấu** | — |

**Cả hai lỗi 3 và 4 do CHÍNH cổng tự khai qua `--thu-chan`.** Không chạy phép thử chặn thì K4 sẽ
báo xanh vĩnh viễn, kể cả khi panel bị gỡ hẳn khỏi `setInterval`.

---

## 8. Gỡ về (rollback)

**FU-360:**
```bash
cp backups/database.py.pre_v11052 web/backend/database.py && systemctl restart lottery
```
*(Đã dùng thật một lần lúc 10:01 — khôi phục sạch, `grep -c "CHAN CHEO LANE"` = 0, health 200.)*

**P4:**
```bash
DROP TABLE gan_hoi_tu_shadow_v11055;
crontab -l | grep -v _materialize_gan_hoi_tu_shadow | crontab -   # hoặc: crontab backups/crontab.pre_v11055.txt
cp backups/main.py.pre_v11055 web/backend/main.py
cp backups/monitoring.html.pre_v11055 web/frontend/monitoring.html
systemctl restart lottery
```

**Ngưỡng gỡ về tự động cho FU-360:** `_v11055_canh_chan_cheo_lane.py` thoát **≠ 0** khi phát hiện
**chặn NHẦM** (cả hai phía đều OFFICIAL) ⇒ rollback ngay.

---

## 9. Theo dõi tiếp

| mã | việc | ngưỡng hành động | mốc |
|---|---|---|---|
| **FU-360** · `CL1008` | canh 24h chặn chéo lane | **bất kỳ** lần chặn NHẦM ⇒ rollback ngay | **đóng sáng 11/08** |
| **FU-394** · `GH1008` | P4 đo tiến trên bảng shadow | McNemar `\|z\| ≥ 1,96` gộp 3 miền | chờ tích luỹ |
| **chờ owner** | `_apply_hot_cold_post_filter` dìm số gan cao ×0,3 — **ngược** thiết kế owner | — | **QD-041 khoá tới 21/08** |
| **chờ owner** | ngưỡng gan 7/7/15 → **15/15/60** | — | cùng cửa 21/08 |
| FU-284 | cửa sổ đang chạy | **9,53** điểm · z ≥ 1,96 · n ≥ 150 | **20/08** — cấm đọc sớm |
| DEHERD_V1 | mới **1/21** ngày | ≥21 ngày · dẫn official · không thua miền nào | **19/08** |

**Ngày nổ đã ghi sẵn của FU-360 là 21/08** — khi `QD-015/016/017` chạy, lúc một model chạy **cả
hai đường**. Nền **0 dòng** hôm nay là **đúng dự kiến**, không phải bằng chứng bản vá chết
(RM-20: «0 dòng mới» ≠ «không ai đọc»).
