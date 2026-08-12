# REPORT V11065 (FU-400) — 3/3 BẠCH THỦ · VÀ PHÉP ĐO CHƯA TỪNG CÓ: TRỌNG SỐ KHÔNG HƠN LUẬT THÔ

**Ngày:** 2026-08-12 · **Mã đọc:** `DO1208` · **Quyết định:** `QD-065`
**Production KHÔNG đổi** — không deploy, không restart · `QD-041` nguyên vẹn · gói 21/08 **không
thêm không bớt**

---

## 0. NỐI TIẾP — hai dòng liền mạch

**Dòng 1 · từ đâu tới đây:** `V11064` (`QD-064`) khoá phạm vi gói 21/08 và chốt *«FU-290 đợi tới
21/08, không chỉnh timeout»*; sáng nay kiểm trước live thấy MN chốt sạch và phát hiện tệp briefing
**cũ 12,2 giờ** vì hook chỉ chạy trong Cursor.

**Dòng 2 · phiên này giao gì cho phiên sau:** hôm nay **3/3 bạch thủ** — và chính vì thế phiên này
đi đo **câu gốc chưa ai đo** (`FU-400`): *trọng số có hơn luật thô không?* Kết quả **A−B =
−2,75pp, CI95 [−6,28 … +0,79]** trở thành **bằng chứng cho `FU-290A` đã có sẵn trong gói 21/08** —
**không phải mục mới**, đúng `QĐ-4`.

---

## 1. Tóm tắt

**Kết quả 12/08: 3/3** — MN `61` · MT `82` · MB `73`. Vận hành sạch tuyệt đối.

**Nhưng phần quan trọng nhất của báo cáo này không phải kết quả hôm nay.**

| | |
|---|---|
| nền đúng hôm nay | `0,42 + 0,30 + 0,22 = **0,94**` lượt |
| xác suất cả ba trúng **do ngẫu nhiên** | **2,8%** = **1 ngày trong 36** |
| kỳ vọng số ngày như vậy trên 166 ngày | **~4,6 ngày, hoàn toàn do may** |
| `RM-04` | **n = 3 ⇒ CHƯA ĐƯỢC PHÉP KẾT LUẬN** |

**Phát hiện chính — `FU-400`:** đo ghép cặp trên **437 miền-ngày**, **đường chấm điểm có trọng số
KHÔNG hơn luật thô «nhiều phiếu nhất»** — điểm ước lượng **−2,75pp**, và **CI loại trừ khả năng
trọng số giúp quá +0,79pp**.

**Agent tự bắt một lỗ trong CHÍNH phép đo của mình** (mục 7.1) — con số đầu sai **hơn 3 lần**.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *"Đã hết chu kỳ live em tiến hành phân tích toàn lực, đánh giá nhận xét dự đoán hôm nay và các
> cơ chế, phương pháp đo lường, đề xuất xử lý tất cả thật tổng lực cực gắt nha em cấm rơi rụng,
> gián đoạn, ngắt quãng mọi thứ phải liền mạch, tương quan tương thích, tương ứng phù hợp tuyệt
> đối nha em"* — 12/08

Và sáng cùng ngày:

> *"Đầu ngày em kiểm tra phân tích đánh giá trước live dùm anh nhé"*

---

## 3. Đào bới / phát hiện

### 3.1 · Vận hành 12/08 — đạt hết

| miền | bạch thủ | kết quả | chốt (giờ VN) | hạn §55 | sớm |
|---|---|---|---|---|---|
| MN | `61` | **TRÚNG** | 05:20 | 15:45 | 625 phút |
| MT | `82` | **TRÚNG** | 16:46 | 16:58 | **12 phút** |
| MB | `73` | **TRÚNG** | 17:35 | 17:58 | 23 phút |

Journal **0 Traceback · 0 ERROR · 0 CRITICAL** · dịch vụ `active` · `NRestarts=0` · PID `1438110`
**không đổi suốt ngày**.

### 3.2 · Khâu chọn hôm nay — và MB là ca trọng số CỨU

| miền | BT ở hạng | luật thô «nhiều phiếu nhất» |
|---|---|---|
| MN | **#1** (12 phiếu) | `61` — cùng số, cùng trúng |
| MT | **#1** (13 phiếu) | `82` — cùng số, cùng trúng |
| **MB** | **#4** (4 phiếu) | `91` (9 phiếu) — **SẼ TRƯỢT** ⇒ **trọng số CỨU** |

**Ba ngày liên tiếp, ba kết quả NGƯỢC NHAU về cùng một cơ chế:**

| ngày | miền | trọng số làm gì | kết quả |
|---|---|---|---|
| 10/08 | MT | bỏ `19` (trúng, hạng #2) chọn `28` | **HẠI** |
| 11/08 | MT | bỏ `82` (trúng) chọn `37` (cũng trúng) | **trung tính** |
| 12/08 | **MB** | bỏ `91` (hạng #1, trượt) chọn `73` (hạng #4) | **CỨU** |

Mỗi lần agent đều bị cám dỗ kết luận từ **một ngày**. **Cả ba lần đều sai về mặt bằng chứng.**
Đó là lý do phải đi đo tử tế.

### 3.3 · `FU-400` — CÂU GỐC CHƯA AI ĐO

**Câu hỏi:** đường chấm điểm có trọng số + boost + mọi cổng lọc, có hơn **luật thô «nhiều phiếu
nhất»** không?

**Thiết kế — vì sao GHÉP CẶP:** hai luật chấm trên **cùng ngày, cùng pool, cùng tập phiếu**. So
hai tỉ lệ rời rạc sẽ vứt mất thông tin ghép cặp. Dùng **McNemar** trên ngày **bất đồng**.

- **A** = `final_bundles.bach_thu` — đường THẬT
- **B** = đuôi nhiều phiếu thô nhất; **hoà ⇒ lấy đuôi nhỏ hơn** (quy tắc **khai TRƯỚC**, không
  chọn sau khi thấy số)

**Kết quả — 437 miền-ngày (28/02 → 12/08):**

| | |
|---|---|
| **A · trọng số** | **147/437 = 33,6%** |
| **B · luật thô** | **159/437 = 36,4%** |
| nền ngẫu nhiên đúng | 34,4% |
| **A − B** | **−2,75pp · CI95 [−6,28 … +0,79]** |
| McNemar | A cứu **25** · A hại **37** · **z = −1,456** · p = 0,145 |
| VIF thực nghiệm (`RM-21`, cụm = ngày) | **0,920** |
| hai luật chọn **giống nhau** | 281/437 = **64,3%** |

> **Đọc đúng:** **chưa đủ bằng chứng** để kết luận trọng số hại. **Nhưng CI loại trừ khả năng nó
> giúp quá +0,79pp**, và cho phép nó **hại tới −6,28pp**. Muốn **chứng minh** mức −2,75pp cần
> **~240 ngày** ⇒ còn **~94 ngày nữa**.

**Mọi cửa sổ cạnh nhau (`RM-18` — cấm window-shopping):**

| cửa sổ | A | B | A−B | z |
|---|---|---|---|---|
| 30 ngày | 32,2% | 30,0% | **+2,22pp** | +0,25 |
| 60 ngày | 29,4% | 33,9% | −4,44pp | −1,20 |
| 90 ngày | 30,0% | 34,8% | −4,81pp | **−1,79** |
| 120 ngày | 32,2% | 35,8% | −3,61pp | **−1,71** |
| toàn bộ | 33,6% | 36,4% | −2,75pp | −1,40 |

**4/5 cửa sổ âm.** Không cửa sổ nào đạt `|z| ≥ 1,96` ⇒ **cấm kết luận**, nhưng hình dạng nhất quán.

**Phân tầng theo miền** (gộp thô là bẫy Simpson vì nền khác nhau):

| miền | A | B | z |
|---|---|---|---|
| MN | 44,4% | 45,1% | −0,00 |
| MT | 36,2% | 38,4% | −0,46 |
| **MB** | **18,2%** | **24,1%** | **−1,65** |

**Hạng của bạch thủ thật:** #1 chiếm **65%** (trúng 36,3%) · #2 **16%** (28,2%) · #3 **11%**
(30,0%). Lệch khỏi đồng thuận thì tỉ lệ trúng **giảm** — **nhưng đây có thể là hiệu ứng chọn mẫu**
(ngày đồng thuận mạnh vốn dễ đoán hơn), nên **KHÔNG dùng làm bằng chứng**. Bằng chứng sạch là
McNemar ghép cặp ở trên.

### 3.4 · Anti-trap (`FU-397`) — hiệu ứng đang CO VỀ 0

`n = 52/90` FULL_SPENT · số hiện hành trúng **21,2%** · số thay thế **25,0%** ⇒ phản thực
**+3,8pp**.

**Hôm 10/08 con số này là +6,4pp ở n=47.** Co về 0 khi n tăng — **đúng dấu hiệu của hiệu ứng
KHÔNG TỒN TẠI**, không phải hiệu ứng thật đang chờ đủ mẫu.

### 3.5 · Lane A/B ba tầng (`FU-398`) — nhanh hơn dự kiến

Hôm nay **13 cặp** (MN 5 · MT 4 · MB 4) · **10 bất đồng** · **0 lỗi**. Cộng dồn **26 cặp · 19 bất
đồng** / ngưỡng **96**. Nhịp ~10/ngày ⇒ **~20/08**, sớm hơn ước tính 22/08. **Cấm đọc sớm.**

### 3.6 · Độ trễ (`FU-283`) — MT nhẹ hơn hôm qua

Đường tới hạn MN sáng nay: **9 model · tổng 756s · wall 5 phút 11 giây**. `glm-5.1` chỉ **172s**
(hôm qua ở MT là **410s**). `deepseek-reasoner` **289s** là con chậm nhất.

**Không kết luận «an toàn»** — `glm-5.1` có max từng đo **1.027s**; một ngày nhẹ không nói gì về
ngày mai.

### 3.7 · Lỗ quản trị phát hiện sáng nay

`docs/_BRIEFING_DAU_PHIEN.txt` **cũ 12,2 giờ**, ghi ngày **11/08**, và danh sách *«ĐẾN HẠN HÔM
NAY»* trong đó là **6 mục của hôm qua** (`FU-318 · FU-331 · FU-310 · FU-304 · FU-294 · FU-264`,
tất cả hạn 11/08).

Nguyên nhân: tệp do `.cursor/hooks/session_start_briefing.py` ghi, nối vào `sessionStart` trong
**`.cursor/hooks.json`** — **hook của Cursor**, **không kích hoạt trong Claude Code**.

> `CLAUDE.md` bảo Claude Code đọc một tệp mà **chỉ Cursor mới sinh lại**.

Đã chạy tay để lấy số đúng (**48 quá hạn · 6 đến hạn hôm nay**). Việc sửa cơ chế vào **HÀNG ĐỢI
SAU GÓI** theo `QĐ-4`.

---

## 4. Hướng xử lý và vì sao

### 4.1 · KHÔNG gỡ trọng số — ba lý do, mỗi lý do đủ để dừng

1. **`QD-041` khoá đường chọn số tới 21/08.**
2. **CI vẫn trùm 0** — chưa đủ bằng chứng. Gỡ bây giờ là hành động trên một kết quả *"chưa được
   phép kết luận"*, đúng thứ đã làm sáu lần *«hứa rồi rữa»* (V10655→V10790).
3. **`QĐ-4` khoá phạm vi gói 21/08** — thêm mục là vi phạm.

**Việc đúng:** kết quả này là **BẰNG CHỨNG** cho `FU-290A` (*thiết kế lại*) **đã có sẵn trong
gói**, **không phải mục mới**.

### 4.2 · Đăng ký 6 nhãn trạng thái — và vì sao đây KHÔNG phải scope creep

Cổng lịch cuốn chiếu **chặn mọi phiên** vì **7 nhãn đang dùng thật mà chưa bao giờ được khai** ⇒
**15 mục rơi khỏi mọi bộ đếm**. Đúng gốc bệnh **V10980** từng làm 14 mục biến mất.

Và **chính tệp đó đã ghi sẵn nguyên tắc** (dòng 116–118):

> *«NGUYÊN TẮC PHÂN LOẠI: không chắc thì để TREO. Gán nhầm "đã đóng" làm mục BIẾN MẤT khỏi mọi bộ
> đếm — đúng thứ đã gây ra V10980. Gán nhầm "còn treo" chỉ hơi ồn.»*

Nên agent **không tự đặt chính sách**, chỉ **áp đúng luật đã ghi**. Kết quả:

| | trước | sau |
|---|---|---|
| mồ côi | **15** | **2** |
| còn treo | 140 | **153** (+13 mục **hiện ra**) |
| quá hạn | 48 | **48 — không đổi** |

**Không mục nào bị đóng lén.** `DEPLOYED_LIVE_VERIFIED` (2 mục) **cố ý KHÔNG xếp** — đóng một mục
là **chiều rủi ro**, chờ owner ký.

---

## 5. Đã làm gì

| # | việc | bằng chứng |
|---|---|---|
| 1 | Kiểm trước live + sau live, đủ chặng, báo tiến độ từng chặng | mục 3.1 |
| 2 | Nâng bộ đo `_v11061` **nhận tham số `--ngay`** thay vì viết script nháp mới | bài học §63 |
| 3 | **Dựng `FU-400`** — `_v11065_do_trong_so.py`, có cổng RM-01, VIF theo thước, in mọi cửa sổ | mục 3.3 |
| 4 | **Tự bắt lỗ nhiễm shadow** trong chính phép đo, thêm hai lớp lọc | mục 7.1 |
| 5 | Đăng ký **6 nhãn** vào `TREO_STATUSES` theo nguyên tắc có sẵn | mồ côi 15→2 |
| 6 | `FU-290` hạn 14/08 → **21/08** + `OWNER_LOCK` theo `QĐ-2` + gắn dossier V11063 | sổ theo dõi |
| 7 | Ghi bốn mặt bằng công cụ §63 | `governance_seq → 407` |

**Không deploy, không restart.** 4 bảng khoá chỉ tăng tự nhiên trong ngày.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v10920_decision_ledger.py` | **✓ KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI** |
| `_v11062_nang_version.py --kiem` (§63) | **✓ ĐẠT** · `GAP_MARKER: 1 dòng · 2 khoảng trống` |
| `_v11044_cong_so_hieu.py` (FU-369) | **✓ đã chạy** — `FU-400` · `QD-065` |
| RM-01 cổng tuổi dữ liệu | **✓** trong cả hai bộ đo |
| journal | **✓ 0 lỗi mọi loại** |
| mốc chốt §55 | **✓ ba miền đều trước hạn** |

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn (trích) |
|---|---|
| 12/08 sáng | *"Đầu ngày em kiểm tra phân tích đánh giá trước live dùm anh nhé"* |
| 12/08 tối | *"phân tích toàn lực… cấm rơi rụng, gián đoạn, ngắt quãng mọi thứ phải liền mạch"* |
| 11/08 22:36 (`QĐ-2`) | *"cắt cũng đã cắt rồi thì đợi luôn"* |
| 11/08 22:36 (`QĐ-4`) | *"không thêm, không bớt… đi vào HÀNG ĐỢI SAU GÓI"* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| ba miền trúng bạch thủ, ba miền chốt trước hạn | `final_bundles` 12/08 · `bach_thu_status=WIN` |
| MB chọn hạng **#4**, luật thô chọn `91` sẽ trượt | `_v11061_kiem_toan_1108.py --ngay 2026-08-12` |
| **A 33,6% vs B 36,4% trên 437 miền-ngày** | `_v11065_do_trong_so.py` |
| `predictions` chứa `shadow_auto_eval` chạy **sau** khi bundle chốt | MB 12/08: **11/27 model** |
| anti-trap `n=52/90`, phản thực **+3,8pp** (từ +6,4pp ở n=47) | `anti_trap_shadow_v11058` |
| lane A/B **26 cặp / 19 bất đồng** | `prompt_3tang_ab_shadow_v11059` |
| briefing do **hook Cursor** ghi | `.cursor/hooks.json` → `session_start_briefing.py` |
| **7 nhãn chưa khai ⇒ 15 mục mồ côi** | `_v10958_fu_reader.py:99,130` |

### `DOC_SAID`

| tài liệu ghi gì | file:mục | lệch? |
|---|---|---|
| *"Hook `sessionStart` tự chạy lệnh đầu và **ghi ra** `_BRIEFING_DAU_PHIEN.txt`"* | `CLAUDE.md §0` | **⚠ LỆCH** — hook đó **chỉ có trong Cursor**; Claude Code đọc bản cũ |
| *"NGUYÊN TẮC PHÂN LOẠI: không chắc thì để TREO"* | `_v10958_fu_reader.py:116` | **khớp** — và agent áp đúng nó thay vì tự đặt chính sách |
| `RM-04` *"n nhỏ là CHƯA ĐƯỢC PHÉP KẾT LUẬN"* | `CLAUDE.md §61` | **khớp** — 3/3 hôm nay không đọc riêng |
| `QĐ-4` *"không thêm không bớt"* | `docs/FOLLOW_UP_TRACKER.md` | **khớp** — `FU-400` là **bằng chứng**, không phải mục mới của gói |

### Ba lớp lệch nhau ⇒ FINDING

1. **`DOC_SAID` ≠ `CODE_DID` — briefing.** `CLAUDE.md` bảo Claude Code dựa vào một tệp mà **chỉ
   Cursor mới sinh lại**. Sáng nay agent **suýt báo danh sách đến hạn của hôm qua** thành hôm nay.
2. **`CODE_DID` tự mâu thuẫn — nhãn trạng thái.** Hệ **dùng** 7 nhãn mà bộ đọc **không khai**, nên
   15 mục vừa *tồn tại* vừa *vô hình*.

---

## 7. Vướng vấp

### 7.1 · Agent tự bắt một lỗ trong CHÍNH phép đo của mình — và nó lệch hơn 3 lần

Bản đầu của `FU-400` cho **`A−B = −0,80pp`** trên **498** miền-ngày.

**Sai.** `predictions` chứa cả `shadow_auto_eval` — MB ngày 12/08 có **11/27 model là shadow chạy
SAU khi bundle đã chốt**. Đếm phiếu của chúng là so đường có trọng số với **một pool KHÁC, LỚN
HƠN**, không phải với *«chính hệ bỏ trọng số»*.

Thêm **hai lớp lọc**: bỏ `shadow_auto_eval` **và** chỉ lấy dòng ghi **trước giờ chốt**.

```
498 miền-ngày  →  437
A−B = −0,80pp  →  −2,75pp        (lệch hơn 3 lần)
```

**Nếu không bắt được, báo cáo này đã công bố một con số sai gấp ba** — và nó sẽ là căn cứ cho
quyết định 21/08.

### 7.2 · Suýt báo danh sách đến hạn của HÔM QUA

Tệp briefing cũ 12,2 giờ. Agent đọc và **suýt liệt kê 6 mục hạn 11/08** thành *"đến hạn hôm nay"*.
Bắt được nhờ **đối chiếu ngày ghi trong tệp** với hôm nay — không phải nhờ cổng nào.

### 7.3 · Một lệnh treo 600 giây

Lệnh gộp gọi hook briefing qua `subprocess` bị treo, chuyển nền. **Bản vá nhãn trạng thái KHÔNG hề
chạy** — kiểm lại thấy `V11065` xuất hiện **0 lần** trong tệp đích. Đã làm lại bằng công cụ sửa
tệp trực tiếp.

> Bài học: **treo ≠ đã chạy**. Phải **kiểm dấu vết** chứ không suy từ việc lệnh có được gửi đi.

---

## 8. Gỡ về

```bash
git revert be59e4b
```

Phiên này **chỉ thêm bộ đo read-only + tài liệu + đăng ký nhãn**. Không deploy, không restart,
không chạm `/du-doan` / writer `final_bundles` / bộ chọn model.

Riêng phần đăng ký nhãn: gỡ 6 dòng trong `TREO_STATUSES` là quay lại trạng thái cũ — **15 mục sẽ
lại vô hình**.

---

## 9. Theo dõi tiếp

| mã | việc | ngưỡng hành động | mốc |
|---|---|---|---|
| **FU-400** · `DO1208-2` | **MỚI** — trọng số vs luật thô, `n=437` | `\|z\| ≥ 1,96` McNemar · **cấm đọc sớm** · **CẤM gỡ trọng số** (QD-041 + CI trùm 0) | ~**94 ngày** |
| **FU-398** | lane A/B — **26 cặp / 19 bất đồng** | `≥96 bất đồng` **VÀ** `\|z\|≥1,96` | ~**20/08** |
| **FU-397** | anti-trap — `n=52/90`, **+3,8pp đang co về 0** | `n≥90` **VÀ** `z≥1,96` | ~giữa 12/2026 |
| **FU-290** | **đợi 21/08** theo `QĐ-2`, dossier V11063 đã gắn | owner quyết một lần | **21/08** |
| **FU-284** | đọc **20/08**, ngưỡng **9,53** | quyết mục #13 của gói | **20/08** |
| **GÓI 21/08** | **13 mục ĐÃ KHOÁ** — `FU-400` là **bằng chứng**, không phải mục mới | | **21/08** |
| **HÀNG ĐỢI SAU GÓI** | +2 mục mới: **hook briefing chỉ có ở Cursor** · **`DEPLOYED_LIVE_VERIFIED` chờ owner ký** | | sau 21/08 |

---

TanPhatAI cần làm: ① ghi **kết quả 12/08 = 3/3** **kèm nền `0,94/3` và xác suất ngẫu nhiên 2,8%**
— **cấm ghi 3/3 trần trụi** như một thành tích; ② ghi **`FU-400`**: trọng số **A 33,6% vs luật thô
B 36,4%**, `A−B = −2,75pp` CI95 `[−6,28 … +0,79]` — **chưa kết luận được**, nhưng **CI loại trừ
trọng số giúp quá +0,79pp**; ③ ghi rõ **CẤM gỡ trọng số** — `QD-041` khoá tới 21/08 **và** CI vẫn
trùm 0; `FU-400` là **bằng chứng cho `FU-290A` đã có trong gói**, **không phải mục mới** (`QĐ-4`);
④ ghi **anti-trap đang CO VỀ 0** (+6,4pp ở n=47 → **+3,8pp** ở n=52) — đừng ai đọc con số cũ; ⑤
ghi hai mục mới vào **HÀNG ĐỢI SAU GÓI**: **hook briefing chỉ chạy trong Cursor** (Claude Code đọc
bản cũ) và **`DEPLOYED_LIVE_VERIFIED` chờ owner ký** để khép 2 mục.
