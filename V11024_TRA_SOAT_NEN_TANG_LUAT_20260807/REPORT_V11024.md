# REPORT V11024 — TRA SOÁT NỀN TẢNG LUẬT SOI CẦU + KẾ HOẠCH SOẠN LẠI NGỮ CẢNH

> **Ngày:** 2026-08-07 đêm · **READ-ONLY toàn bộ GĐ1 · PLAN-ONLY toàn bộ GĐ2**
> **Quy mô:** 16 agent · 3,13 triệu token · 851 lượt gọi công cụ · 83 phút ·
> **83 script** + **101 tệp bằng chứng**
> **Verdict:** `REPORT_PUBLISHED` — không deploy, không sửa code production, không ghi DB

> **GHI CHÚ ĐÁNH SỐ:** đề bài owner ghi `REPORT V11015`. Số **V11015 đã dùng sáng 07/08**
> cho báo cáo ML/LLM. Báo cáo này mang số **V11024** để không đè lên bản cũ.

---

## 1. Tóm tắt

Owner giao tra soát toàn bộ nền tảng quy tắc soi cầu rồi lên kế hoạch biến context pack từ
*"bóc số sẵn + ra lệnh"* thành *"ngữ cảnh để model tự làm việc"*.

**Bốn phát hiện lật đổ nền tảng đang dùng để ra quyết định:**

| # | Phát hiện | Hệ quả |
|---|---|---|
| **1** | **105 luật production KHÔNG phải hậu duệ của chuỗi V10636.** `_seed_rules.py:432` chạy `DELETE FROM mined_rules` rồi đào lại 21 bucket × top-5 | Toàn bộ câu chuyện lineage *"2.387 → 268 → 232 → 28 → 105"* **sai ở mắt xích cuối** |
| **2** | **Bộ đếm ĐO TIẾN bị xoá mỗi thứ Hai** — `weekly_rule_miner.py:170` xoá 112 ngày `mined_rule_effectiveness` rồi backfill bằng chính bộ luật vừa đào | Mọi kế hoạch *"đo thêm N ngày rồi kết luận"* là **bất khả thi về cấu trúc** |
| **3** | **Cổng thăng hạng 55% NẰM DƯỚI mức ngẫu nhiên** của 71/105 luật — **toàn bộ 35 luật MN** | Bộ chọn đuôi **hoàn toàn ngẫu nhiên** cũng qua cổng. Cổng không lọc gì |
| **4** | **Prompt thật gấp ~3 lần con số agent vẫn báo cáo.** `context_pack` MB = **15.617** ký tự, nhưng prompt **đầy đủ** gửi model = **46.583** (đo trên VPS) | Mọi con số ký tự agent báo owner suốt ngày 07/08 **chỉ là 1/3 sự thật** |

**Trả lời thẳng câu hỏi R4 của owner:** **KHÔNG giải nguồn nào mang tín hiệu đo tiến** — không
ĐB, không G1, G2, G5, G6, G7, không G8, ở cả ba miền. 20/21 ô là `NGANG_NEN`, **0 ô sống sót**
sau hiệu chỉnh đa so sánh.

## 2. Owner yêu cầu gì (nguyên văn)

> *"lần nào cũng báo cáo vớ vẩn chả kiểm tra so sánh trên vps trước mà cứ báo cáo sai lệch xong
> rồi đi tìm hiểu rồi lại xin lỗi rồi lại đào bới khổ em quá nha."*

> *"Vấn đề ngữ cảnh, lời kể của em diễn giải như thế nào?"*

> *"em phải làm việc ở cường độ cực cao để tìm cho ra giải pháp điều chỉnh thật hoàn mỹ cho anh"*

Kèm đề bài đầy đủ R1–R10 + cổng kiểm 8 gạch. **Phê bình của owner đúng** — và chính vì thế phiên
này bắt mọi agent **kiểm trên VPS** trước khi kết luận; các phát hiện nặng nhất (số 2 và số 4)
đều chỉ lộ ra khi đo trên VPS.

## 3. Đào bới / phát hiện

### 3.1 R1 — LINEAGE: mắt xích cuối KHÔNG TỒN TẠI · `VERIFIED_CODE` + `VERIFIED_TEST`

Chuỗi V10636 tái lập được **gần trọn vẹn** từ artifact thật:

| mắt xích | tài liệu | đo lại | |
|---|---|---|---|
| CROSS cells | 2.387 | **2.387** | ✓ |
| DIG cells | 784 | **784** | ✓ |
| LAGS cells | 1.260 | **1.260** | ✓ |
| BH-pass FDR α=0,05 | 268 | **268** | ✓ |
| vi phạm temporal | 266 | **266** | ✓ |
| BH-pass vi phạm | 36 | **36** | ✓ |
| còn lại hợp lệ | 232 | **232** | ✓ |
| registry FIXED | 28 | **28** | ✓ |
| **dedup "3.696"** | 3.696 | **KHÔNG TÁI LẬP** — cộng thô 4.431, dedup khoá tự nhiên 4.011 | ✗ |
| **28 rule → 105 production** | — | **MẮT XÍCH KHÔNG TỒN TẠI** | ✗ |

**Bằng chứng mắt xích cuối không tồn tại:**

```
web/backend/_seed_rules.py:432     c.execute("DELETE FROM mined_rules")
web/backend/weekly_rule_miner.py:92-94   "_seed_rules.main() does DELETE FROM mined_rules"
DB: 105 luật đều mined_at 2026-08-03T00:30:01→00:30:11  (đào xong trong 10 GIÂY)
    rule_version = v2026W32 · một source_run_id duy nhất run-20260803-003000-d35eb5
    21 bucket × 5 luật = 105
Giao khoá (tgt_region, tgt_wd, src_region, offset) giữa registry và mined_rules: 4/47
```

**Temporal thì sạch:** 105/105 luật hợp lệ, 0 vi phạm thứ tự xổ MN→MT→MB, 0 luật khai sai miền
đài nguồn. Bảng lineage đủ **105/105 dòng**, không thiếu dòng nào.

**Bằng chứng ngoài mẫu chỉ 3,45%** (60/1.740 lượt) · **45/105 luật chưa có lượt ngoài mẫu nào** ·
**tối đa 1 lượt/luật**.

**Forward audit 90 ngày của 28 rule: 0/28 chấm sau 66 ngày**, còn 24 ngày tới hạn chốt 31/08 —
sẽ tới hạn với **đúng 0 ngày dữ liệu**.

### 3.2 R2 — DẤU VÂN TAY THIÊN VỊ CHỌN · `VERIFIED_TEST`

Đo lại từ đầu 105 luật trên toàn bộ `lottery_results` (2020-01-01 → 2026-08-07, 15.232 dòng).
Cách đo tái lập bảng thật **100%** (1.740/1.740 lượt trùng `hit_any`).

| | |
|---|---|
| **Trong cửa sổ chọn** (365 ngày mà `_seed_rules` dùng để lấy top-5) | lift **1,084** · z cụm-ngày **+8,84** |
| **Ngoài cửa sổ chọn** | lift **1,000** — 29.205 lượt, 20.976 trúng vs nền 20.969,4, **lệch 6,6 lượt** |

**Lợi thế tồn tại đúng trong cửa sổ dùng để chọn luật, ra ngoài về đúng ngẫu nhiên tới chữ số
thứ ba.** Đây là định nghĩa sách giáo khoa của thiên vị chọn.

**BH-FDR α=0,05 bác bỏ 0/105 luật ở cả bốn giai đoạn** — kể cả đoạn thuận lợi nhất.

**Đo tiến gần như không tồn tại:** cả 105 luật cộng lại chỉ **75 lượt**, không luật nào quá
**1 lượt**, **0/105 đạt n≥20**.

### 3.3 R3 — NGỮ NGHĨA NGUỒN: 20/20 PASS, nhưng tài liệu công khai mô tả HỌ LUẬT KHÁC

20 luật (phủ 20/21 ô miền×thứ, cả 2 offset, 3 miền nguồn, 16 tổ hợp giải): **20/20 PASS**.
Ngày nguồn · thứ nguồn · `source_weekday` · `source_station_slot` · đuôi trích ra đều khớp
**100%** trên 52 ngày đích/luật. Ba chỗ dễ sai đều **sạch**: MB đổi đài theo thứ 7/7 ·
Thừa Thiên Huế thêm CN đúng từ 26/10/2025 · Đà Lạt/Da Lat khớp qua `_identity_key`.

**Nhưng:** tài liệu công khai `V10667`/`V10670` **mô tả một họ luật KHÁC** với họ đang chạy.
Ai đọc tài liệu rồi soi `mined_rules` sẽ kết luận *"code sai"* — tốn nguyên một phiên.

**Và khối TIER2 đi thẳng vào prompt MB official dưới dạng chuỗi chữ chưa giải nghĩa:**
model được bảo `MB:G6#3:D-3 [HEAD_TAIL] hr=28%` mà **không** được cho biết `#3` là bộ nào,
`HEAD_TAIL` là phép gì, `D-3` là ngày nào. Nó sẽ **tự suy** — đúng lỗi §60.1.

### 3.4 R4 — KHÔNG GIẢI NÀO MANG TÍN HIỆU ĐO TIẾN · `VERIFIED_TEST`

Quét vũ trụ 364 ngày (**60.412 lượt** — con số đã đính chính từ "~66.000" sau kiểm chéo),
không qua bộ chọn của miner:

| kết quả | số ô |
|---|---|
| `NGANG_NEN` | **20/21** |
| sống sót sau hiệu chỉnh đa so sánh | **0** |

**Toàn bộ "sức mạnh" của các giải là hai thứ cộng lại:**

1. **NỀN QUÁ CAO.** `hit_any` nghĩa là *"có ít nhất 1 đuôi nguồn xuất hiện bất kỳ đâu"*. Nền
   thật: **MB 51,1% · MT 77,1% · MN 86,8%**. Tỉ lệ 93–98% được quảng cáo là **gần như miễn phí**.
2. **THIÊN LỆCH CHỌN MẪU.** 8/21 ô đẹp rực rỡ khi chấm ngược tụt về đúng 0 khi quét vũ trụ —
   `MB·G1`: **+14,3pp z=3,79 → +0,1pp z=0,15**.

**Phát hiện nặng nhất toàn phiên:** `weekly_rule_miner.py:170` **xoá 112 ngày**
`mined_rule_effectiveness` rồi backfill lại bằng chính bộ luật vừa đào. ⇒ Bộ đếm đo tiến
**reset về 0 mỗi 7 ngày**, không bao giờ vượt **35 lượt/miền**. Mọi kế hoạch *"đo thêm N ngày"*
**vĩnh viễn không về đích**.

### 3.5 R5 — DOCTRINE vs CODE: chỉ 7–10 / 28 mục có đường thực thi

RR-16.5 có **28 mục §** (`gpt_analyzer.py` L482-780), xác nhận y hệt trên VPS.

| loại | số mục |
|---|---|
| có code thật sự làm gì đó | **7–10 / 28** (bản gốc nói 10, phản biện bác 3 ⇒ 7) |
| chỉ bơm dữ liệu ra prompt rồi để model tự xử | 8 / 28 |
| **hoàn toàn không kiểm được** | **10 / 28** (7 chỉ là chữ, **3 khai có cơ chế mà code không hề làm**) |

**§11 RULE TAILS** — `0/180` lần có dữ liệu, mà **§14, §18, §23 đều trỏ vào nó**.
**§14 duplicate-family KHÔNG có code** ⇒ **95,4% "hội tụ" thực chất là một đài nguồn nói lại
nhiều lần**, và con số CONV×N sai đó chảy vào ba chỗ: CONVERGENCE TRAP ALERT · CONV_BOOST_CAP ·
xếp hạng.
**§10A** trình tự bắt buộc chỉ ép cho **8 model shadow**; model official **không nhận** — và khối
nguồn-giải lại nằm **SAU** anti-trap trong văn bản prompt.

### 3.6 R6 — HAI KHẲNG ĐỊNH NỀN CÓ VẤN ĐỀ NẶNG

| khẳng định | trước | đo lại | |
|---|---|---|---|
| (a) 0/34 model hơn nền | 0/34 | **0/35** (official 0/17) | ✓ giữ |
| (c) herding 3,8× | 3,8× | **3,91×** | ✓ giữ |
| (d) ô 3 nguồn z=−2,54 | −2,54 | **−2,46** (cửa sổ 90 ngày) | ✓ giữ, nhưng **cửa sổ không có lý do ghi lại** |
| **(b) 84/84 KTC chứa 0,50** | 84/84 | **80/84** (VPS tươi) · 75/84 (local cũ) · **không tồn tại script gốc** | ✗ **SAI** |
| **(e) M4 z=−0,33/+0,26** | tái lập đúng số | **chỉ trên bản sao lưu trước đồng bộ** — bảng gốc đã bị lần đồng bộ 18:51 xoá | ✗ **KHÔNG TÁI LẬP ĐƯỢC** |

**(b) nặng vì:** đó là **căn cứ duy nhất** đang dùng để TỪ CHỐI MẶC ĐỊNH bước 3 của FU-300
(đưa rules thành đặc trưng ML) theo doctrine M3. Căn cứ đó **vừa sai số vừa không có nguồn**.

**(e) nặng hơn:** con số `−0,33σ/+0,26σ` **đang được bơm vào prompt** (V11014/V11016) để model
đọc — và nó tính từ **9 và 15 cặp lệch**. Đổi một cặp là z nhảy ~0,3 đơn vị.

### 3.7 R7/R8 — PROMPT THẬT GẤP BA LẦN CON SỐ ĐANG BÁO CÁO

| | context_pack | prompt ĐẦY ĐỦ gửi model |
|---|---|---|
| **MB** | **15.617** (agent tự kiểm VPS) | **46.583** (dump VPS đường official) |
| MT | 10.257 | ~41.125 |
| MN | 9.396 | ~40.232 |

**Kết quả xổ THÔ chỉ chiếm 7,3% prompt MB.** 92,7% còn lại là **bóc sẵn + mệnh lệnh** —
đếm được **233 lần từ khoá ra lệnh** ở MB. Prompt nêu tên **88–90 trên 100 đuôi**.

**Khối lớn nhất toàn prompt không nằm ở doctrine** mà ở `create_analysis_prompt`:
«CHỈ SỐ ĐỊNH LƯỢNG (PYTHON TÍNH SẴN)» **10.066 ký tự (20,5%)**, trong đó «CHÍNH SÁCH QUYẾT
ĐỊNH AI — 7 LỚP» thật ra có **13 lớp**, chiếm **5.140 ký tự** — lớn hơn §19+§25+§10A+§10B cộng
lại, và **chưa từng bị soi**.

**Sáu khối HỎNG hoặc CHẾT đang nằm trong prompt official** (đều kiểm được trên VPS):

| # | khối | tình trạng |
|---|---|---|
| B1 | `WEEKDAY SCAN` | **chết hẳn** — `gpt_analyzer.py:5372` SELECT cột `predicted_numbers` **không tồn tại** (cột thật `main_numbers`); prompt in thẳng `⚠️ SP-4.0 scan error` |
| B2 | `RULE TAILS (48h)` | **rỗng đúng lúc dựng prompt** (cron chấm 20:15 chạy sau) — và 14/14 dòng đều `💡LIGHT`, **chưa từng có 🔥STRONG** mà §18/§25 lại đòi 🔥STRONG |
| B3 | TIER2 `#Bộ` | chuỗi chữ chưa giải nghĩa |
| B4 | `TOP 5 GỢI Ý (Score/Zone/Trend/Gan)` + `⏳ GAN CAO` + `🔥 HOT` | **vẫn đang bơm** dù V11001 tuyên bố đã gỡ gan/hot/cold |
| B5 | ba con số WR mồ côi, «6/7 AI» đã cũ | tự mâu thuẫn |
| B6 | truy vấn `:4662` chọn **11 cột**, unpack `:4761` có **10 tên** | lệch cột |

**B4 là một §60.1 mới:** V11001 báo *"gỡ hết gan/nóng/lạnh"* — nhưng đó là gỡ khỏi
`build_context_pack`. `statistical_analyzer.format_condensed_stats` **vẫn sinh** khối gan/hot và
`gpt_analyzer.py:2229` **vẫn bơm** khi `prediction_mode=='HYBRID'`.

## 4. Hướng xử lý và vì sao chọn

**Không đề xuất sửa gì trong phiên này** — đề bài là READ-ONLY + PLAN-ONLY, và bốn phát hiện nền
tảng ở trên làm thay đổi hẳn thứ tự ưu tiên. Sửa prompt trước khi sửa **bộ đếm đo tiến bị xoá
mỗi thứ Hai** thì mọi phép đo sau đó vẫn vô nghĩa.

**Thứ tự đúng phải là:** (1) sửa cơ chế **đo** trước · (2) sửa cơ chế **chọn luật** · (3) mới tới
soạn lại **ngữ cảnh**. Soạn ngữ cảnh trước là đánh bóng mặt tiền của một cái móng chưa đo được.

## 5. Đã làm gì

| | |
|---|---|
| GĐ1 R1–R6 | 6 mục, **mỗi mục có một agent phản biện đo lại bằng phương pháp khác** (SQL nếu gốc Python và ngược lại) |
| GĐ2 R7–R10 | 3 agent kế hoạch, **PLAN-ONLY** |
| Phê bình độ đầy đủ | 1 agent soi lại cả 9 agent trên |
| Sản phẩm | **83 script** + **101 tệp bằng chứng** trong `artifacts/v11024_audit/` |

**Bốn lỗi trong chính phiên này do agent phê bình bắt được** — ghi ra để không giấu:

1. **R7 tóm tắt không khớp artifact của chính nó**: khai `GỠ 8 · VIẾT LẠI 8`, artifact thật
   `GO 9 · VIET_LAI 10`; và **đếm chồng** (`MB HARD MODE` 2.206 đã bao gồm `MB MODEL RANKING`
   1.428 nhưng vẫn tính riêng) ⇒ tỉ lệ "96,2% phủ" không dựng lại được.
2. **R7 còn 43% bảng chưa động**: hai dòng lớn nhất mang nhãn `VIET_LAI` nhưng **TRƯỚC = SAU**
   (`RR-16.5` 15.465→15.465 · `CHÍNH SÁCH 7 LỚP` 5.139→5.139) — phần **khó nhất và dài nhất chưa
   soạn**, mà con số "giảm 33,8%" lại được trình như đã làm. Đúng dạng **§60.4 + §60.1**.
3. **R8 đo trên prompt KHÔNG PHẢI bản chạy thật**: local **49.270** vs VPS **46.583** — R8 cảnh
   báo *"VPS còn dài hơn"* là **SAI, VPS ngắn hơn 2.687 ký tự**. Mọi tỉ lệ cắt 94% của R8 đo trên
   vật sai.
4. **R5 và R7 mâu thuẫn về §11**: R5 nói *"chết 100%"*, dump VPS cho thấy MB có 8 dòng, MT 6 dòng,
   MN không có khối nào. **Hai chẩn đoán dẫn tới hai cách sửa khác nhau** — dời giờ chấm ≠ gỡ khối.

## 6. Cổng kiểm — đối chiếu 8 gạch của đề bài

| # | gạch | verdict | bằng chứng |
|---|---|---|---|
| 1 | Cổng tuổi dữ liệu FU-303 | **ĐẠT** (giờ) · **KHUYẾT** (xuất xứ) | tuổi **1,67 giờ** < 6. Nhưng sha256 DB ≠ manifest vì **chính agent** ghi 2 bảng shadow lúc 18:51 (`bay_dan_daily_shadow` 66 dòng). Hai bảng đó **không nằm trong 4 bảng khoá** |
| 2 | Hash 4 bảng khoá PRE=POST | **ĐẠT** | `cong_bam_4_bang_khoa.py` (mới, tái lập được) — cả 4 bảng **Y HỆT**: `20e776b2` · `d58fea10` · `213129d5` · `6175b0e1` |
| 3 | 105/105 luật có dòng lineage | **ĐẠT** | `R1_lineage.json` = **105 dòng · 105 rule_id phân biệt**; DB `is_active=1` = 105 (id 2311..2415); phép so tập **khớp hoàn toàn** |
| 4 | Mọi con số tái lập bằng script | **KHÔNG ĐẠT** | 3 con số tự nhận không tái lập: `dedup 3.696` · `84/84 KTC` · các số đầu bảng R7 |
| 5 | Nền 2 cửa sổ + sức mạnh + **đăng ký trước** | **KHÔNG ĐẠT một phần** | Nền+sức mạnh: R2/R4/R6/R9 làm tốt (VIF **2,92×** khớp độc lập 2,91× của R6). **Đăng ký trước: 0/6 mục có** |
| 6 | GĐ2 PLAN-ONLY, không diff code | **ĐẠT** | `git status`: **0/10** tệp lõi bị sửa. DB mtime `20:03:23` < script đầu tiên `20:34` |
| 7 | Report public-safe, verdict `REPORT_PUBLISHED` | **ĐẠT (bản này)** | không code/diff/PII/secret; verdict `REPORT_PUBLISHED`, **không tự nâng DEPLOYED** |
| 8 | LOCK-IN / OPEN ITEMS / NEXT ACTION | **ĐẠT (bản này)** | mục 9 |

## 7. Vướng vấp

**Phê bình của owner đúng, và phiên này chứng minh điều đó bằng số.** Con số ký tự prompt agent
báo owner suốt ngày 07/08 (`12.497` · `15.617`) là **`build_context_pack`**, không phải prompt
thật gửi model (**46.583**). Sai **gấp ba** — và chỉ lộ ra khi bắt buộc dump trên VPS.

Hai phát hiện nặng nhất — **bộ đếm bị xoá mỗi thứ Hai** và **khối gan/hot vẫn đang bơm** — đều
**không thể thấy được từ local**: một cái nằm trong cron VPS, một cái nằm ở nhánh
`prediction_mode=='HYBRID'` chỉ chạy khi có `numpy` (máy local thiếu numpy nên khối im lặng
biến mất).

**Đây chính là lý do "kiểm VPS trước" không phải hình thức mà là điều kiện cần.**

## 8. Gỡ về

Phiên này **không có gì để gỡ**: 0 tệp code production bị sửa, 0 lượt deploy, 0 lượt ghi DB,
4 bảng khoá **PRE=POST**. Muốn xoá dấu vết audit: `rm -rf artifacts/v11024_audit/`.

## 9. Theo dõi tiếp

### LOCK-IN — bốn sự thật chốt lại, không đo lại nữa trừ khi có bằng chứng ngược

| | |
|---|---|
| **L1** | 105 luật production **không** thuộc lineage V10636. Chúng do `_seed_rules` đào lại hằng tuần, xoá sạch bộ cũ |
| **L2** | **Không giải nguồn nào** mang tín hiệu đo tiến (20/21 ô `NGANG_NEN`, 0 ô sống sót sau hiệu chỉnh) |
| **L3** | Lợi thế của luật **chỉ tồn tại trong cửa sổ chọn**; ra ngoài lift = **1,000** |
| **L4** | Prompt thật MB = **46.583 ký tự**, kết quả thô chỉ **7,3%** |

### OPEN ITEMS — xếp theo mức chặn

| Mã | Việc | Vì sao chặn | Ai |
|---|---|---|---|
| **A1** | **Bộ đếm đo tiến bị xoá mỗi thứ Hai** (`weekly_rule_miner.py:170`) | Không sửa cái này thì **mọi phép đo tiến vĩnh viễn không về đích** — kể cả FU-284, FU-325 | **owner ký** (đụng cơ chế đào luật) |
| **A2** | **Cổng thăng hạng 55% dưới nền** — 71/105 luật, toàn bộ MN | Cổng đang thăng hạng luật **tệ hơn ngẫu nhiên** | **owner ký** |
| **A3** | **Khối gan/hot vẫn đang bơm** qua `format_condensed_stats` | V11001 tuyên bố đã gỡ — **chưa gỡ hết**. §60.1 | agent làm được |
| **A4** | **`WEEKDAY SCAN` chết** (`predicted_numbers` không tồn tại) | Prompt official đang in dòng lỗi cho model đọc | agent làm được |
| **A5** | **(b) "84/84 KTC"** sai và không nguồn | Đang là **căn cứ duy nhất** từ chối FU-300 bước 3 | agent sửa tài liệu |
| **A6** | **(e) M4 không tái lập được**, mà số đang bơm vào prompt | Model đang đọc một con số không ai dựng lại được | agent làm được |
| **A7** | R7/R8 phải làm lại trên **prompt VPS thật**, và soạn nốt **43% chưa động** | Kế hoạch hiện đứng trên vật đo sai | agent làm được |
| **A8** | FU-284 thật ra gộp **SÁU** biến, không phải ba | Ngày sạch đầu tiên là **08/08**; 08/08→21/08 vừa đúng 14 ngày | ghi nhận |
| **A9** | Cửa sổ 14 ngày **không đủ sức** cho ngưỡng "tụt ≥5 điểm" — cần **44,1 ngày** | 14 ngày chỉ phát hiện được chênh **≥8,76 điểm** | ghi nhận |

### NEXT ACTION — MỘT bước

**Owner đọc L1–L4 và quyết A1** (bộ đếm đo tiến bị xoá mỗi thứ Hai). Đây là nút thắt: mọi việc
còn lại — kể cả soạn lại ngữ cảnh — đều cần một phép đo tiến chạy được. Không gỡ nút này thì
mọi kế hoạch đo sau đó đều là đo trên một cái đồng hồ bị bấm lại về 0 mỗi tuần.
