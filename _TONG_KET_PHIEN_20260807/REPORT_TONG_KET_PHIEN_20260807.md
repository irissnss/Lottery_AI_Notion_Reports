# TỔNG KẾT PHIÊN 07/08/2026 — V11015 → V11018

> **Bảy phiên bản trong một ngày** · 3 lượt deploy · 4 báo cáo công khai
> **Dừng deploy lúc 14:41** — cửa sổ khoá 15:00–18:45

---

## 1. Tóm tắt

| Phiên bản | Việc | Trạng thái |
|---|---|---|
| **V11015** | ML và LLM: hiện trạng, chỗ thiếu, 7 đề xuất | READ-ONLY, xong |
| **V11015b** | **Sự cố mất 23.551 dòng** + dựng cổng chặn | đã gỡ về, đã dựng cổng |
| **V11015c** | Truy nguồn sự cố — 246 chỗ ghi tệp không đóng tay | FU-324 mở |
| **V11016** | **Số thành lời kể** (L-A) + ngưỡng tự quyết (L-B) | **đã deploy** |
| **V11017** | **Đo bầy đàn** — phép đo cơ chế, biết trong 1 ngày | **đã deploy** |
| **V11018** | **M-A: đối chứng ba nguồn** ML × luật × bộ lọc | **đã deploy** |

**Ba phát hiện lớn nhất trong ngày, xếp theo mức quan trọng:**

1. **ML và LLM chạy theo hai niềm tin trái ngược** — prompt đã gỡ sạch gan/nóng/lạnh nhưng ML
   **vẫn còn 6 đặc trưng** gan/hot/cold. Chưa ai phát hiện.
2. **Cơ chế «nhiều nguồn cùng chỉ» đi ngược LẦN THỨ HAI** — §5g `z=−2,54`, nay M-A `z=−1,01`.
3. **Prompt vẫn đưa rổ số dọn sẵn ở BỐN chỗ**, không phải một. Đã gỡ cả bốn.

## 2. Owner yêu cầu gì (nguyên văn)

> *"ML và LLM đã làm được gì rồi? hiện tại và tương lại đề xuất là gì… Em làm được gì và cần gì
> phải rõ ràng"*

> *"Làm ngay luôn đi em."* — chốt L-A sau khi được trình đánh đổi

> *"Giờ đề xuất tiếp theo là gì em"* → *"ok tiếp đi em."*

> *"khẩn trương đi em, sắp tới giờ block rồi rm"*

> *"cập nhật báo cáo github và nâng verison … cho aritifact đi em"*

## 3. Đào bới / phát hiện

### 3.1 ML — bốn sự thật · `VERIFIED_CODE`

| câu hỏi owner | trả lời | bằng chứng |
|---|---|---|
| ML có **đối chứng rules/bộ lọc** không? | **KHÔNG** | 7/7 tệp ML đếm `mined_rule` = 0 |
| ML có tự phân biệt **chính/phụ** không? | **KHÔNG** | `secondary`/`top1`/`top2` = 0 lần trong `ml_predict.py` |
| **1 tháng mới retrain thì kiểm soát sao?** | hệ **chưa trả lời được** | chỉ có lịch CN 02:00 + chốt chặn tuổi 8 ngày |
| ML hơn nền chưa? | **0/34 model** | AUC 0,48–0,56 qua 228 lượt học lại |

### 3.2 MÂU THUẪN HAI TẦNG — chưa ai phát hiện

| tầng | gan / nóng / lạnh |
|---|---|
| **LLM prompt** | **đã gỡ hết** (V11001 + V11007) |
| **ML đặc trưng** | **VẪN CÒN 6** — `gan_score_w` · `gan_days` · `gan_vs_avg` · `zone_encoded` · `freq_x_gan` · `trend_x_zone` |

Owner nói *"gan, cold, hot chả tích sự gì"*; agent gỡ khỏi prompt rất kỹ — quét ngược, phân loại,
cổng kiểm — **nhưng chưa hề soi tầng ML**. Lỗi **§60.2 câu 1**.

### 3.3 Prompt đưa rổ số dọn sẵn ở BỐN chỗ, không phải một

Sửa **một** khối rồi đo lại thì prompt **dài thêm 1.336 ký tự** mà dòng rổ số **9 → 12** —
**đi ngược mục tiêu**.

| # | chỗ | hình thức | mức neo |
|---|---|---|---|
| 1 | `RULES-FIRST` | rổ hợp nhất `trỏ tới 10 đuôi: …` | cao |
| 2 | `EVIDENCE TABLE` › Rule candidates | rổ **ĐÃ XẾP HẠNG** `🔥 35: boost=0.180` ×8 | rất cao |
| 3 | `EVIDENCE TABLE` › trace | rổ trần `← tails=[13,35,69,…]` ×5 | cao |
| 4 | `OWNER ANTI-TRAP` › FRESH | **vừa xếp hạng vừa khuyên chọn** | **cao nhất** |

Chỗ #4 **suýt bị bỏ sót** — cổng deploy bắt được, dừng trước restart.

### 3.4 Nền bầy đàn — 64 lượt miền-ngày · `VERIFIED_TEST`

**Phân tán trung bình 0,474 ± 0,087.** Ca nặng: **16 model ra 5 số** (0,31); có hôm **8/16 model
chốt đúng một số**.

### 3.5 Đối chứng ba nguồn — số nói ĐỪNG LÀM · `VERIFIED_TEST`

| số nguồn | n | tỉ lệ trúng |
|---|---|---|
| 1 nguồn | 2.658 | **43,60%** |
| 2 nguồn | 516 | **47,48%** |
| **3 nguồn** | **24** | **33,33%** |

**z (3 vs 1) = −1,01.** Lần **thứ hai** cơ chế «nhiều nguồn» đi ngược (§5g: `z=−2,54`).

## 4. Hướng xử lý và vì sao chọn

**Gỡ cả bốn chỗ, không gỡ ba.** §60.1: *"bỏ nửa chừng còn tệ hơn không làm"*.

**Giữ thông tin LOẠI TRỪ, bỏ thông tin XẾP HẠNG.** «đuôi này miền ra trước đã tiêu rồi» là căn
cứ để **tránh**; `boost=0.100` là điểm xếp hạng của bộ luật đã đo ra **ngang luật giả**.

**Đưa hồ sơ luật KÈM cách đọc, thay vì giấu.** Con số `12 tuần trúng 10/12` là thật, nhưng chấm
**ngược** trên chính cửa sổ đã đào ra luật. Đưa cả hai — con số **và** lý do nó bị thổi phồng.

**Đo shadow trước khi gắn vào ML.** Owner hỏi *"có đối chứng không"* — câu trả lời đúng không
phải *"em gắn vào rồi"* mà *"em đo xem có ích không đã"*. §5g là ví dụ của việc đi thẳng từ trực
giác vào production mà không đo.

**Ngưỡng chốt TRƯỚC khi có dữ liệu**, viết vào mã nguồn lẫn panel, để sau này không ai bẻ.

## 5. Đã làm gì

### 5.1 V11016 — số thành lời kể (đã deploy)

Mỗi luật nay là **một sự kiện**: *"thứ Năm 06/08, đài Hà Nội (MB) ra ở G6+G7 các đuôi 13 35 69
84 88 89 95. Luật nối chỗ này với hôm nay có hồ sơ 12 tuần trúng 10/12 — nhưng tỉ lệ đó chấm
ngược trên chính cửa sổ đã đào ra luật, nên cao là đương nhiên."*

Kèm **ngưỡng tự quyết**: mức tin vừa/thấp ⇒ **chỉ ra số chính**, `secondary_number=""`.

| chỉ số | MB | MT | MN |
|---|---|---|---|
| ký tự trước→sau | 10.387 → **11.401** | 8.903 → **10.298** | 8.370 → **9.818** |
| số hai chữ số | 252 → **235** | 209 → **206** | 195 → 198 |
| **cặp khối trùng ≥60%** | 10 → **4** | 7 → **3** | 1 → 1 |

**Prompt DÀI THÊM ~1.000–1.400 ký tự — nói thẳng.** Lời kể dài hơn danh sách.
`CTX-17.0→18.0` · `PB-19.0→20.0`

### 5.2 V11017 — đo bầy đàn (đã deploy)

Bảng `bay_dan_daily_shadow` + API + panel + cron **19:05**. Nền **64 lượt · 0,474 ± 0,087**.
Ngưỡng: `≥0,50 và hơn nền ≥0,05` ⇒ có tác dụng · `≤0,35` ⇒ không tác dụng.

### 5.3 V11018 — đối chứng ba nguồn (đã deploy)

Bảng `ma_doi_chung_shadow` + API + panel + cron **19:25**. Kết quả: **KHÔNG CÓ LỢI THẾ**.

### 5.4 V11015b — cổng chặn cắt cụt

`_v11015_cong_chan_cat_cut.py` + hook `git commit|git push` `failClosed`. So bản làm việc với
**bản trong git** — đúng chỗ ba cổng cũ mù.

## 6. Cổng kiểm

| phép | kết quả |
|---|---|
| 4 bảng khoá qua **cả ba** lượt deploy | ✓ **Y HỆT** — `11916\|25692` · `481\|661` · `15226\|15330` · `11739\|11739` |
| PID đổi mỗi lượt | `974549 → 979960 → 981452 → 981799 → 982337` |
| `/api/health` | **200** sau mỗi lượt |
| endpoint admin mới, chưa đăng nhập | **401** cả hai |
| cổng prompt sạch gan | `PROMPT_SACH=DAT` |
| cổng chặn cắt cụt | ✓ sạch |
| J5 mốc tải | ✓ khớp sổ thật |
| cổng báo cáo A55 | ✓ **đủ 9 phần, đã push** cho V11015 · V11016 · V11017 · V11018 |
| crontab | 81 → **83** dòng |
| `governance_seq` | 393 → **395** |

## 7. Vướng vấp

**Bảy lỗi trong một ngày, sáu do phép đo bắt chứ không phải agent tự thấy.**

| # | lỗi | ai bắt |
|---|---|---|
| 1 | Commit đẩy lên GitHub **CHANGELOG mất 21.583 dòng**, SSOT mất 1.968 | agent đọc dòng `+156 / −23551` **sau khi đã push** |
| 2 | `_doc_prepend` so với **đĩa**, đĩa hỏng thì nó **ký cho cái hỏng** | truy nguyên sự cố 1 |
| 3 | Sửa **1/4 chỗ** rổ số rồi tưởng xong | phép đo trước/sau |
| 4 | Sót chỗ neo **mạnh nhất** (`FRESH candidates`) | **cổng deploy**, dừng trước restart |
| 5 | Mốc đo lấy theo **NGÀY** ⇒ 3 lượt prompt **CŨ** bị gắn nhãn `SAU_V11016` với 0,57 — **nhìn như thắng lớn** | đọc lại dữ liệu thật sau deploy |
| 6 | Script deploy dùng `cp` ⇒ chạy lần hai **ghi đè bản sao lưu**, mất đường gỡ về | phải deploy hai lần mới lộ |
| 7 | Dò hàm bộ lọc bằng **tên đoán** ⇒ một nguồn ra **0 dòng** mà bảng **vẫn ra số và vẫn có kết luận** | so số dòng bất thường |

**Lỗi số 5 là đáng sợ nhất:** một phép đo dựng ra để **chống tự huyễn hoặc** lại suýt trở thành
công cụ **tự huyễn hoặc** — và tự huyễn hoặc theo hướng **có lợi cho việc agent vừa làm**.

**Lỗi số 7 là kiểu hỏng nguy hiểm nhất:** không có gì báo lỗi, chỉ có một con số nhỏ hơn bình
thường mà không ai biết bình thường là bao nhiêu.

**Điều rút ra:** cái cứu không phải là cẩn thận. Cái cứu là **cổng máy chạy được** và **đọc lại
dữ liệu thật ngay sau khi làm**, thay vì tin vào thứ mình vừa viết.

## 8. Gỡ về

| phiên bản | lệnh |
|---|---|
| **V11016** | `cp backups/gpt_analyzer.py.v11016_pre web/backend/gpt_analyzer.py && systemctl restart lottery` · md5 `f8b428ece9d90181642806e095ced195` |
| **V11017** | `cp backups/*.v11017_pre …` · `crontab -l \| grep -v _v11017_bay_dan_shadow \| crontab -` |
| **V11018** | `cp backups/*.v11018_pre …` · `crontab -l \| grep -v _v11018_ma_doi_chung \| crontab -` |
| **cổng chặn cắt cụt** | xoá khối `truncation_guard.py` khỏi `.cursor/hooks.json` |

Hai bảng shadow mới bỏ đi không ảnh hưởng gì — `DROP TABLE` là xong.

## 9. Theo dõi tiếp

### Bốn câu chỉ owner trả lời được — 08/08

| mã | câu hỏi | vì sao chặn |
|---|---|---|
| **FU-215** | **Đóng băng QD-014 hết hạn 08/08 — chốt hay gia hạn?** | **chặn nhiều nhất** — còn đóng băng thì M-B và M-D không làm được |
| **FU-290** | Cắt model — **«bỏ cờ»** hay **«dừng hẳn»**? | §59 cấm trình đề xuất mà không phân biệt |
| **FU-319** M-B | Chính/phụ theo **biên** xác suất | đổi cách chọn số |
| **FU-320** M-D | Bỏ **6 đặc trưng gan** khỏi ML | phải huấn luyện lại 4 model |

### Việc agent làm được, không cần duyệt

| mã | việc | hạn |
|---|---|---|
| **FU-318** M-C | Canh **trôi đặc trưng** hằng ngày, học lại theo trôi | 11/08 |
| **FU-324** | Rà **246 chỗ** ghi tệp không đóng tay | 14/08 |
| **FU-326** | Rà phép đo dùng **mốc NGÀY** thay vì **mốc GIỜ** | 14/08 |
| **FU-327** | Cổng bắt **nguồn chết** trong bảng gộp nguồn | 14/08 |
| **FU-303** | Cổng chặn audit khi dữ liệu cũ | 08/08 |

### Phép đo đang chạy

| mã | đo gì | chốt |
|---|---|---|
| **FU-325** | Lượt đo bầy đàn **SẠCH** đầu tiên | **08/08** |
| **FU-317** | Đối chứng ba nguồn, 14 ngày | 21/08 |
| **FU-284** | Kết quả prompt — **gộp BA biến** | **21/08** |
| **FU-316** | Còn 1 pool đuôi chưa gắn nguồn | 14/08 |

### Cảnh báo tải

**8 mục quá hạn từ 06/08** chưa ai động — phần lớn là `DEPLOYED_PENDING_LIVE_VERIFY`, tức đã làm
chỉ thiếu người xác nhận: FU-268 · FU-250 · FU-256 · FU-258 · FU-224 · FU-257 · FU-210 · FU-245.

**Ngày 08/08 có 11 mục đáo hạn** — nặng.
