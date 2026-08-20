# REPORT V11092 — HAI NGƯỠNG ACTIVE · ĐỌC NỐT HAI THƯỚC · CHỐT BẢN ĐỒ 21/08

**Ngày:** 2026-08-20 · **Mã đọc:** `QD2008` · **Quyết định:** `QD-068`
**Production KHÔNG đổi** — không deploy · không ghi DB production · không Notion ·
`QD-041` nguyên vẹn tới 21/08.

---

## 1. Tóm tắt

Phiên này **chỉ GHI NHẬN** năm chữ ký owner đã có — **không đổi một con số nào**.

| chặng | kết quả |
|---|---|
| **GĐ-1** | hai ngưỡng `CHỜ KÝ` → **ACTIVE** · khai **`QD-068`** đủ **năm chữ ký** |
| **GĐ-2** | **bầy đàn: CÓ TÁC DỤNG** · **DEHERD: CHƯA ĐƯỢC PHÉP KẾT LUẬN** |
| **GĐ-3** | `D3` **gỡ khỏi gói** · `FU-284` **ĐÓNG** · bảng kiểm **9 → 10 bước** |

**Kết quả đáng chú ý nhất:** **bầy đàn CÓ TÁC DỤNG** — đây là **kết quả dương duy nhất** trong cả
bốn ô đo của gói.

**Chỗ hở đã bịt:** các báo cáo trước gắn nhãn `QD-068` nhưng cổng `_v11044` báo `QD-068`
**chưa từng được khai** — tức đã tag báo cáo bằng một quyết định **không tồn tại**. Nay lập thật.

---

## 2. Owner yêu cầu gì (nguyên văn)

> **23:45 · 18/08** — *«① bầy đàn: XÁC NHẬN KHÔI PHỤC bảng 4 dòng (CHANGELOG:5128), giữ nguyên
> số. ② DEHERD: KÝ |chênh| ≥16,3pp VÀ |z| ≥1,96 VÀ n ≥63 (kèm ghi nhận phép đo yếu).»*

> **19:58 · 20/08** — *«③ D3: HOÃN (lối C) — tách thành việc riêng có dump prompt + quét ngược
> đầy đủ; D3 KHÔNG nằm trong gói 21/08.»*

> **19:58 · 20/08** — *«④ FU-290A: trong phiên 21/08 agent VIẾT THIẾT KẾ trước (trả lời đủ 3 câu
> §59), owner duyệt rồi mới thi hành — không tự chạy khi chưa có thiết kế.»*

> **19:58 · 20/08** — *«⑤ FU-284: ĐÓNG, ghi «cửa sổ 12 ngày không đủ sức (±14–17đ so ngưỡng
> 9,53), không kết luận» — KHÔNG kéo dài vì sau 21/08 hệ đổi ⇒ số đo sẽ nhiễm.»*

> *«mọi chữ ký dưới đây ĐÃ TỒN TẠI, việc là GHI VÀO KHO»* · *«CẤM đổi bất kỳ con số nào»*

---

## 3. Đào bới / phát hiện

### 3.1 · BẦY ĐÀN ⇒ **CÓ TÁC DỤNG** *(dương duy nhất trong 4 ô)*

**Bước bắt buộc trước tiên — kiểm `giai_doan`** (bẫy 07/08):

| `giai_doan` | n | phân tán TB | khoảng |
|---|---|---|---|
| `NEN` | **64** | **0,4739** | 17/07 → 07/08 |
| `SAU_V11016` | **37** | **0,5815** | 07/08 → 19/08 |
| `HON_HOP` | **1** | *(0,6667)* | 07/08 — ⛔ **LOẠI khỏi cả hai trung bình** |

| điều kiện (bảng 4 dòng, ký 23:45 18/08) | đo được | |
|---|---|---|
| n ≥ 9 lượt sạch | **37** | ✓ |
| trung bình ≥ 0,50 | **0,5815** | ✓ |
| hơn nền ≥ 0,05 | **+0,1076** | ✓ |

⇒ **CÓ TÁC DỤNG.**

**Một xác nhận quan trọng:** nền đo được **`0,4739`** **khớp** con số `0,47` ghi trong ngưỡng đăng
ký trước ⇒ **ngưỡng và dữ liệu cùng một nền**, không phải nền được vẽ lại sau khi thấy số.

> ⚠️ **Đọc cho đúng:** ngưỡng bầy đàn **KHÔNG có vế `z`** — khác hẳn `FU-284` và DEHERD. Nó là
> **ngưỡng thực dụng** (*«phân tán có cao hơn nền không»*), **không phải** phép kiểm ý nghĩa thống
> kê. Ghi ra để không ai đọc `CÓ TÁC DỤNG` thành *«đã chứng minh bằng thống kê»*.

### 3.2 · DEHERD ⇒ **CHƯA ĐƯỢC PHÉP KẾT LUẬN** — cả ba vế đều không đạt

| điều kiện | đo được | |
|---|---|---|
| `n ≥ 63` | **60** | ✗ *(thiếu 3 — một ngày trống trong cửa sổ 21 ngày)* |
| `\|chênh\| ≥ 16,3pp` | **6,67pp** | ✗ |
| `\|z\| ≥ 1,96` | **1,155** | ✗ |

DEHERD **20/60 = 33,3%** · official **24/60 = 40,0%** · McNemar `b=8` (official-only) · `c=4`
(deherd-only) · hoà **48**.

Hướng: DEHERD **kém hơn**, nhưng `6,67pp` nằm **sâu trong vùng nhiễu** của phép đo này.

> **Nghĩa là CỬA SỔ NGẮN, KHÔNG phải DEHERD vô dụng.** Owner **ký kèm ghi nhận này từ 18/08**:
> `n=63` chỉ thấy được `≥16,3pp`; muốn thấy `+5pp` cần **223 ngày**.

### 3.3 · `QD-068` chưa từng được khai

Cổng `_v11044` báo *«cao nhất `QD-067` · trống tiếp `QD-068`»* — trong khi các báo cáo `V11082`
→ `V11091` đều gắn nhãn `quyet_dinh="QD-068"`.

⇒ **đã tag báo cáo bằng một quyết định không tồn tại** suốt bốn ngày. Nay lập thật với đủ **năm
chữ ký** và **5 phép `kiem_code`** máy kiểm được.

---

## 4. Hướng xử lý và vì sao chọn

**Vì sao không đổi một con số nào khi kích hoạt.** Bản đề xuất 18/08 và bản ký 18/08 **phải giống
hệt** — đó là điều kiện để ngưỡng vẫn là **ngưỡng đăng ký trước**. Sửa dù một chữ số sau khi đã
thấy dữ liệu là biến nó thành ngưỡng **đặt vừa khít quanh kết quả**.

**Vì sao nâng bốn mặt TRƯỚC khi commit `GĐ-2/3`.** Cổng `_v11062` chặn commit vì `V11092` chưa có
dòng `HISTORY` — **đó là lỗi thật**, không phải cổng phiền. Nâng bốn mặt trước ⇒ cổng **ĐẠT thật**
⇒ commit qua cổng **không cần cờ bỏ qua**. Đây là lần đầu trong nhiều phiên không phải dùng
`BO_QUA_CONG_COMMIT`.

**Vì sao `FU-284` không kéo dài** (owner nêu): sau 21/08 hệ **đổi** (12 mục thi hành) ⇒ mọi ngày
đo thêm sẽ **nhiễm**. Kéo dài không cho số **sạch hơn**, chỉ cho số **lẫn nhiều biến hơn**.

---

## 5. Đã làm gì

| # | việc | commit |
|---|---|---|
| 1 | hai ngưỡng `CHỜ KÝ` → **ACTIVE**, thêm bảng **luật đọc** chốt trước | `69997f9` |
| 2 | khai **`QD-068`** đủ 5 chữ ký + 5 phép `kiem_code` + `go_ve` | `69997f9` |
| 3 | đọc bầy đàn (kiểm `giai_doan` trước) + DEHERD | `f273b4b` |
| 4 | điền **hai ô cuối** vào bản đồ ⇒ **cả bốn ô đã đủ** | `f273b4b` |
| 5 | **gỡ `D3`** khỏi gói + khai **`FU-411`** với 4 ràng buộc | `f273b4b` |
| 6 | **đóng `FU-284`** = `CLOSED_REPORT` kèm bảng số 3 miền | `f273b4b` |
| 7 | bảng kiểm **9 → 10 bước** | `f273b4b` |

**Không sửa dòng mã nào.** `QD-041` nguyên vẹn.

### Bảng kiểm 21/08 — ba bước MỚI

| bước | vì sao thêm |
|---|---|
| **b2** — chạy lại bộ chấm T-B **SAU đồng bộ, TRƯỚC khi đọc** | đồng bộ **ghi đè** DB local ⇒ đọc thẳng sẽ thấy **0 cặp** và kết luận nhầm *«lane hỏng»* |
| **b8** — `FU-290A` **viết thiết kế + owner duyệt** trước khi thi hành | owner ký 19:58; `FU-290A` hiện **chỉ là nhãn**, `§59` đòi ba câu |
| **b9** — **`FU-360`/`FU-389`** | miễn trừ K8 **HẾT HẠN 21/08**; không xử thì K8 đỏ lại — và đó là **CỐ Ý** |

---

## 6. Cổng kiểm

| cổng | |
|---|---|
| **`_v11062 --kiem` K1–K4** | **✓ ĐẠT** — commit qua cổng **không dùng cờ bỏ qua** |
| `_v11034_kiem_cheo_quyet_dinh` | **✓ SẠCH** — `QD-068` không mâu thuẫn quyết định nào đang `ACTIVE` |
| `_v11085_cong_rut_lai` · `_v11088_cong_cua_so_chon` | **✓ SẠCH** |
| `_v10981_kiem_lich` K8 | **✓ ĐẠT 8/8** · miễn trừ **hết hạn 21/08** |
| ghi tệp an toàn · đoán tên · mất mục · sáu mặt · đóng băng | **✓ 5/5** |

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| **23:45 18/08** | *«bầy đàn: XÁC NHẬN KHÔI PHỤC bảng 4 dòng, giữ nguyên số»* |
| **23:45 18/08** | *«DEHERD: KÝ \|chênh\| ≥16,3pp VÀ \|z\| ≥1,96 VÀ n ≥63 (kèm ghi nhận phép đo yếu)»* |
| **19:58 20/08** | *«D3: HOÃN (lối C)… D3 KHÔNG nằm trong gói 21/08»* |
| **19:58 20/08** | *«FU-290A: agent VIẾT THIẾT KẾ trước… owner duyệt rồi mới thi hành»* |
| **19:58 20/08** | *«FU-284: ĐÓNG… KHÔNG kéo dài vì sau 21/08 hệ đổi ⇒ số đo sẽ nhiễm»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| bầy đàn: `NEN` 0,4739 · `SAU` 0,5815 · `HON_HOP` 1 lượt bị loại | `bay_dan_daily_shadow` |
| hơn nền `+0,1076` ≥ 0,05 · TB ≥ 0,50 · n=37 ≥ 9 | ⇒ **CÓ TÁC DỤNG** |
| DEHERD `n=60` · `6,67pp` · `z=1,155` | `v10872_deherd_scoreboard`, McNemar `b=8 c=4` |
| `QD-068` chưa từng được khai | `_v11044` báo *«trống tiếp QD-068»* |
| cổng chéo quyết định sạch sau khi khai | `KIEM_CHEO_QD=SACH` |
| `_v11062` ĐẠT sau bump ⇒ commit qua cổng | không dùng `BO_QUA_CONG_COMMIT` |

### `DOC_SAID`

| tài liệu ghi gì | lệch? |
|---|---|
| ngưỡng bầy đàn: nền `0,47` | **khớp** — đo được `0,4739` |
| tài liệu ngưỡng: *«CHỜ OWNER KÝ»* | **đã cập nhật** → `ĐÃ KÝ · ACTIVE` |
| báo cáo `V11082`→`V11091` tag `QD-068` | **LỆCH — đã bịt**: quyết định ấy **chưa từng tồn tại** |

### Ba lớp lệch nhau ⇒ FINDING

**`DOC_SAID` ≠ `CODE_DID`:** bốn ngày qua các báo cáo tag `QD-068` trong khi sổ quyết định
**không có mục đó**. Không ai phát hiện vì cổng `_v11044` chỉ **cấp số**, không **đối chiếu** nhãn
trong báo cáo với sổ. Đã lập `QD-068` thật; **chỗ mù của cổng vẫn còn** — ghi vào theo dõi.

---

## 7. Vướng vấp

**Một chỗ cổng chặn ĐÚNG, và cách xử đúng là không đi vòng.**

Commit `GĐ-2/3` bị `_v11062` chặn: *«`V11092` KHÔNG có dòng `HISTORY`»*. Phản xạ quen là đặt
`BO_QUA_CONG_COMMIT=1`. Nhưng cổng **nói đúng** — bốn mặt chưa đi cùng nhau.

Nâng bốn mặt **trước**, cổng **ĐẠT thật**, commit qua bình thường. **Lần đầu trong nhiều phiên
không phải dùng cờ bỏ qua.**

**Một chỗ suýt để lọt:** `printf` trong shell vỡ vì ký tự `·` trong nội dung commit message
(*«invalid format character»*). Chuyển sang ghi tệp bằng công cụ ghi — cùng họ bài học đã cấm
heredoc khi sửa mã.

---

## 8. Gỡ về

```bash
git revert f273b4b   # GĐ-2+3: đọc hai thước + chốt bản đồ
git revert 69997f9   # GĐ-1: kích hoạt ngưỡng + QD-068
```

Gỡ `69997f9` đưa hai ngưỡng về `CHỜ KÝ` ⇒ hai phép đo **lại bị cấm đọc**.

---

## 9. Theo dõi tiếp

### Gói 21/08 — **CHỐT: 12 mục thực thi + 1 việc thiết kế**

| | |
|---|---|
| ~~#13 `GĐ2` dịch ngữ cảnh~~ | ⛔ `FU-284` **không cho phép** |
| ~~#3 `D3` gỡ `RR §11`+`§18`~~ | ⛔ **HOÃN lối C** → `FU-411` `DEFER` |
| **#8 `FU-290A`** | **việc THIẾT KẾ** — viết trước, owner duyệt, rồi mới thi hành |
| 12 mục còn lại | **giữ nguyên**, thứ tự ba làn **y nguyên** |

### Bốn ô verdict — **đã đủ**

| ô | thước | verdict |
|---|---|---|
| A | `FU-284` | **KHÔNG ĐẠT** ⇒ `#13` không mở khoá · `FU-284` **ĐÓNG** |
| B | lane T-B | **CHƯA ĐƯỢC PHÉP KẾT LUẬN** (100 bất đồng nhưng `z=+0,480`) |
| **C** | **bầy đàn** | ✅ **CÓ TÁC DỤNG** |
| D | DEHERD | **CHƯA ĐƯỢC PHÉP KẾT LUẬN** (cả ba vế không đạt) |

### Việc còn treo

| | việc |
|---|---|
| 1 | **`FU-360`/`FU-389`** — miễn trừ K8 **hết hạn 21/08**, phải xử mai |
| 2 | `FU-411` — `D3` tách riêng, hạn **25/08** |
| 3 | `FU-410` — 4 mục gói thiếu mã, đã khai |
| 4 | **5 món nợ** (`V11091`): cổng `RM-19` khác chủ đề · cổng `>/dev/null` · nhãn `\| hạn \|` · `FU-407` · bộ chấm T-B lên VPS |
| 5 | **mới:** cổng `_v11044` **không đối chiếu** nhãn `QD-xxx` trong báo cáo với sổ quyết định |

**Verdict tách hai dòng:**
- **`CODE_PUSHED`** = `69997f9` (GĐ-1) · `f273b4b` (GĐ-2+3)
- **`REPORT_PUBLISHED`** = bản này

---

TanPhatAI cần làm: ① ghi **hai ngưỡng nay ACTIVE** (owner ký 23:45 18/08) và **`QD-068` đã lập
thật** với năm chữ ký — trước đó báo cáo tag một quyết định **chưa từng tồn tại**; ② ghi **BẦY ĐÀN
CÓ TÁC DỤNG** — `NEN 0,4739` vs `SAU 0,5815`, hơn nền **+0,1076**, `HON_HOP` **1 lượt bị loại**;
nền đo được **khớp** `0,47` của ngưỡng ⇒ cùng một nền; ③ ghi **ngưỡng bầy đàn KHÔNG có vế `z`** —
là ngưỡng **thực dụng**, **cấm** đọc `CÓ TÁC DỤNG` thành *«đã chứng minh bằng thống kê»*;
④ ghi **DEHERD CHƯA ĐƯỢC PHÉP KẾT LUẬN** — cả ba vế không đạt (`n=60<63` · `6,67pp<16,3` ·
`z=1,155<1,96`); **cửa sổ ngắn, KHÔNG phải DEHERD vô dụng**; ⑤ ghi **gói 21/08 CHỐT: 12 mục thực
thi + 1 việc thiết kế** — `#13` và `D3` đều **ra khỏi gói**; ⑥ ghi **bảng kiểm nay 10 bước**, đặc
biệt **b2 chạy lại bộ chấm T-B sau đồng bộ** và **b9 `FU-360`/`FU-389` miễn trừ hết hạn 21/08**;
⑦ ghi **chỗ mù mới của cổng `_v11044`** — nó cấp số nhưng **không đối chiếu** nhãn `QD-xxx` trong
báo cáo với sổ quyết định.
