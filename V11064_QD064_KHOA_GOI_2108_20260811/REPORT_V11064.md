# REPORT V11064 (QD-064) — OWNER KÝ GỘP 4 MỤC + KHOÁ PHẠM VI GÓI 21/08

**Ngày:** 2026-08-11 23:55 · **Mã đọc:** `GN1108` · **Quyết định:** `QD-064`
**Phiên GHI NHẬN** — không đổi production · **không deploy, không restart** · `QD-041` nguyên vẹn ·
**không sinh mã FU mới**

---

## 0. NỐI TIẾP — hai dòng liền mạch

**Dòng 1 · từ đâu tới đây:** `V11063` (FU-283) đo xong độ trễ từng model và phát hiện **ngưỡng
`TB > 180s` sẽ cắt nhầm** (`kimi-k2.5` vượt ngưỡng nhưng 0% đường tới hạn và đã ngừng chạy từ
29/07; `glm-5.1` mới là rủi ro thật) — owner đọc số đó rồi **ký gộp 4 quyết định lúc 22:36**, trong
đó QĐ-2 chốt **đợi tới 21/08**, không chỉnh timeout sớm.

**Dòng 2 · phiên này giao gì cho phiên sau:** bốn quyết định đã vào sổ (`QD-064`), **gói 21/08 đã
khoá phạm vi 13 mục** (không thêm không bớt, ý tưởng mới vào **HÀNG ĐỢI SAU GÓI**), `D-2` được
đánh dấu **tham khảo** ngay trong tài liệu, và `AUTOMATION_HISTORY.jsonl` có **`GAP_MARKER`** cùng
cổng `K5` — nên phiên sau **chỉ cần đọc mục "GÓI 21/08" trong sổ theo dõi là biết đủ phạm vi**.

---

## 1. Tóm tắt

Owner ký gộp **4 mục** lúc 22:36. Phiên này **chỉ ghi nhận + cập nhật tài liệu**.

| | quyết định | đã thi hành |
|---|---|---|
| **QĐ-1** | `D-2` cho MN: **bỏ code, GIỮ tài liệu** | khung *"THAM KHẢO — KHÔNG TRIỂN KHAI (đo = 0, V11056)"* gắn **ngay trong** `V101_SHADOW_RULE_PROMPT_REPORT.md` |
| **QĐ-2** | `FU-290`: **đợi 21/08**, không chỉnh timeout | số V11063 vào dossier |
| **QĐ-3** | `HISTORY`: **không bù**, nhưng **có GAP MARKER** | marker + cổng `K5` + **K2 loại marker khỏi phép đo tuổi** |
| **QĐ-4** | **GÓI 21/08 khoá phạm vi 13 mục** | vào sổ theo dõi + CHANGELOG + mở HÀNG ĐỢI SAU GÓI |

**Cổng FU-369 bắt được một va chạm ngay đầu phiên**, và **agent mắc 2 lỗi trong phiên, cả hai đã
sửa** (mục 7).

**Sổ quyết định: 0 trôi.** Hệ **sẵn sàng live sáng mai**.

---

## 2. Owner yêu cầu gì (nguyên văn)

> **QĐ-1:** *"D-2 cho MN: BỎ TRONG CODE — KHÔNG triển khai vì đã đo = KHÔNG KHẢ THI… LƯU Ý QUAN
> TRỌNG CỦA OWNER: TÀI LIỆU VẪN GIỮ — đánh dấu rõ 'THAM KHẢO — KHÔNG TRIỂN KHAI (đo = 0, V11056)'
> ngay tại mục D-2 trong tài liệu. Tài liệu KHÔNG bị xoá theo code; nó là bằng chứng một ý tưởng
> đã được đo và loại bằng số — giá trị tham khảo cho sau."*
>
> **QĐ-2:** *"FU-290 / độ trễ model: ĐỢI LUÔN TỚI 21/08 — kể cả glm-5.1, KHÔNG chỉnh timeout sớm.
> ('cắt cũng đã cắt rồi thì đợi luôn')"*
>
> **QĐ-3:** *"ĐỒNG Ý không bù 286 bản ghi cũ (RM-17: bù = chế sử). NHƯNG phải GHI NHẬN RÕ Ở MỘT
> CHỖ HỢP LÝ để tra soát khi cần… Cổng §63 K2 phải hiểu marker này, không báo đỏ oan."*
>
> **QĐ-4:** *"XÁC NHẬN PHẠM VI GÓI MỞ KHOÁ 21/08 (đóng gói một lần, không nhỏ giọt)… để mọi phiên
> tới biết chính xác gói gồm gì — không thêm, không bớt. Mọi ý tưởng mới sinh từ nay tới 21/08 đi
> vào HÀNG ĐỢI SAU GÓI."*

Và cuối phiên:

> *"Anh nghỉ ngủ sớm đây em xem canh xử lý tỉ mỉ cẩn thận các vấn đề đã thống nhất, đã rõ ràng dùm
> anh để sẵn sàng live ngày mai nhé."*

---

## 3. Đào bới / phát hiện

### 3.1 · Va chạm số hiệu — cổng FU-369 bắt ngay đầu phiên

Owner ghi *"mã dự kiến QD-060 cho gói này"*. Nhưng:

| mã | đã dùng cho gì (đều trong ngày 11/08) |
|---|---|
| `QD-060` | kiểm toàn diện đầu ngày + đóng FU-360 |
| `QD-061` | kiểm toàn diện cuối chu kỳ live |
| `QD-062` | §63 cơ chế nâng version |
| `QD-063` | FU-283 đo độ trễ |

Cổng `_v11044_cong_so_hieu.py` (quét **sáu** nơi) trả **`QD-064`**. Đây đúng việc cổng sinh ra để
làm — số hiệu từng va chạm **5 lần trong 2 ngày**.

### 3.2 · Vì sao `D-2` phải đánh dấu TẠI CHỖ, không chỉ ghi ở SSOT

`docs/V101_SHADOW_RULE_PROMPT_REPORT.md` ghi:

```
| MN cross-region D-1/D-2 rule | _v101_shadow_pilot.py | ... | DEPLOYED |
| MN prompt V2 | ... | Adds MN D-1/D-2 rule + gan + V99 semantic guard | DEPLOYED |
```

**Đọc lướt sẽ tưởng `D-2` đang chạy trên đường ra số official.** Nên khung cảnh báo phải nằm
**ngay đầu tài liệu đó** và **từng dòng có `D-2`** phải được đánh dấu — đúng như owner yêu cầu
*"ngay tại mục D-2 trong tài liệu"*.

**Tài liệu giữ nguyên nội dung**, chỉ thêm khung. Số đo giữ lại làm bằng chứng:

| phép đo (V11056 · 10/08) | kết quả |
|---|---|
| lợi thế trên nền, mô phỏng 2.337 ngày | **+0,031pp · CI95 trùm 0** |
| bản thi hành thật `v101_mn_cross_region_rule_shadow`, 133 ngày | vế D-2 đóng góp **riêng 75/3.991 = 1,9%** |
| quy ra | **≈ 0,012 lượt trúng thêm/ngày** |

**Vế `D-1` không bị ảnh hưởng.**

### 3.3 · GAP MARKER — và cái bẫy suýt làm cổng mù vĩnh viễn

Marker ghi vào `AUTOMATION_HISTORY.jsonl` (append, không sửa dòng cũ):

| khoảng trống | im từ | commit cuối ghi thật | số ngày |
|---|---|---|---|
| sổ **SỰ KIỆN** (`seq`/`observed_at`/`event_type`) | `2026-07-31T18:20` | `7eb0571` (31/07, V10906) | **11** |
| sổ **VERSION** (`version`/`ngay`/`chu_de`) | `2026-08-04`, mục cuối `V10984` | `a2a7e61` (04/08) | **7** |

Nối lại ở `420cc46` (11/08, V11062). Marker kèm **vì sao chết**, **quyết định không bù**, và
**cách tra bù bằng `git log`**.

> **Cái bẫy:** nếu để marker tự tính là "mục mới" thì `K2` sẽ thấy tệp **luôn tươi** và **báo xanh
> vĩnh viễn** — đúng lỗi `RM-15`: cổng đóng băng `QD-041` từng **mù hoàn toàn** mà vẫn xanh **từ
> lúc dựng**.

Nên thiết kế là **marker giải thích quá khứ, không che tương lai**:

- **`K2` đo tuổi trên MỤC THẬT** — marker bị **loại** khỏi phép đo;
- thêm **`K5`** — phải **có** marker, và marker phải **đủ trường** tra soát.

### 3.4 · Gói 21/08 — và một cái bẫy tên gọi

13 mục: `FU-393` · **`D2`** · `D3` · `FU-394` · `FU-395` · `FU-397b` · `FU-398` · `FU-290A` ·
`FU-299` · `FU-300` · `FU-380` · gỡ `latency_score` · `GĐ2` *(chỉ nếu `FU-284` cho phép)*.

> **⚠️ HAI KÝ HIỆU GẦN GIỐNG NHAU — đã ghi cảnh báo vào sổ:**
>
> | ký hiệu | là gì | trạng thái |
> |---|---|---|
> | **`D-2`** (có gạch) | luật **chéo miền MN** | **ĐÃ LOẠI** ở QĐ-1 · **KHÔNG** trong gói |
> | **`D2`** (không gạch) | `MINED_RULES_MODE` **soft → shadow** | **CÓ** trong gói, mục #2 |
>
> Không ghi rõ thì phiên sau sẽ hỏi *"D-2 đã loại sao còn trong gói?"* và có thể **gỡ nhầm mục
> #2**.

---

## 4. Hướng xử lý và vì sao

**Không sửa hằng số dùng chung, dù nó đang gây trôi.**

Cổng lịch báo `FU-283` là **mồ côi đến hạn**. Truy ra: nhãn `DEPLOYED_LIVE_VERIFIED` **không nằm
trong `DONG_STATUSES` lẫn `TREO_STATUSES`** (`_v10958_fu_reader.py:99,130`) ⇒ **6 mục** mang nhãn
này **rơi khỏi mọi bộ đếm** — đúng họ lỗi **V10980** từng làm 14 mục biến mất.

Cách sửa "gọn" là thêm nhãn vào `DONG_STATUSES`. **Không làm**, vì:

1. Đó là **hằng số dùng chung**, ảnh hưởng **6 mục** — vượt phạm vi *"CHỈ GHI NHẬN"* owner khoá.
2. `RM-05`: làm đúng kỹ thuật nhưng **sai phạm vi**.

Thay vào đó: `FU-283` ghi nhãn **đã đăng ký** (`CLOSED`) **kèm ghi rõ tầng thật**, và **phát hiện
hệ thống đi vào HÀNG ĐỢI SAU GÓI** cho owner ký.

---

## 5. Đã làm gì

| # | việc | bằng chứng |
|---|---|---|
| 1 | Chạy cổng FU-369 trước khi cấp mã | `QD-060…063` đã dùng ⇒ cấp **`QD-064`** |
| 2 | **QĐ-1** — khung *"THAM KHẢO — KHÔNG TRIỂN KHAI (đo = 0, V11056)"* + đánh dấu từng dòng `D-2` | `docs/V101_SHADOW_RULE_PROMPT_REPORT.md` +1.060 ký tự, **nội dung giữ nguyên** |
| 3 | **QĐ-2** — FU-290 đợi 21/08, không chỉnh timeout | ghi vào sổ + dossier |
| 4 | **QĐ-3** — `GAP_MARKER` + `K5` + **K2 loại marker** | `AUTOMATION_HISTORY.jsonl` · `_v11062_nang_version.py` |
| 5 | **QĐ-3** — RM-15 thử chặn **hai chiều** | giữ marker + mục thật cũ ⇒ **ĐỎ** · xoá marker ⇒ **ĐỎ** · khôi phục ⇒ **XANH** · tệp về **344.449 byte** |
| 6 | **QĐ-4** — khoá phạm vi 13 mục + mở HÀNG ĐỢI SAU GÓI | `docs/FOLLOW_UP_TRACKER.md` |
| 7 | Ghi bốn mặt bằng công cụ §63 | `governance_seq → 406` |
| 8 | `FU-283` → nhãn đã đăng ký + queue phát hiện nhãn chưa khai | sổ theo dõi |

**Không deploy, không restart.** 4 bảng khoá: **12280 / 495 / 15259 / 12144** — nguyên vẹn.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v11044_cong_so_hieu.py` (FU-369) | **✓ đã chạy** — cấp `QD-064`, tránh va chạm |
| `_v10920_decision_ledger.py` | **✓ KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI** |
| `_v11062_nang_version.py --kiem` (§63) | **✓ ĐẠT** · `GAP_MARKER: 1 dòng · 2 khoảng trống` |
| RM-15 thử chặn marker | **✓ ĐẠT hai chiều** |
| **sẵn sàng live 12/08** | dịch vụ `active` · PID `1438110` · `NRestarts=0` · health **200** |
| ba cron tối | P4 **3 dòng** · anti-trap **3 dòng** · **độ trễ 57 dòng** *(cron mới, chạy đúng đêm đầu)* |

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn (trích) |
|---|---|
| 22:36 11/08 | *"TÀI LIỆU VẪN GIỮ — đánh dấu rõ 'THAM KHẢO — KHÔNG TRIỂN KHAI (đo = 0, V11056)' ngay tại mục D-2"* |
| 22:36 11/08 | *"cắt cũng đã cắt rồi thì đợi luôn"* |
| 22:36 11/08 | *"Cổng §63 K2 phải hiểu marker này, không báo đỏ oan"* |
| 22:36 11/08 | *"không thêm, không bớt… đi vào HÀNG ĐỢI SAU GÓI"* |
| cuối phiên | *"Anh nghỉ ngủ sớm đây em xem canh xử lý tỉ mỉ cẩn thận… để sẵn sàng live ngày mai nhé"* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| `QD-060`→`QD-063` **đã dùng hết** trong ngày | `_v11044_cong_so_hieu.py` → `QD-064` |
| tài liệu V101 ghi `Status = DEPLOYED` cho luật MN D-1/**D-2** | `docs/V101_SHADOW_RULE_PROMPT_REPORT.md:13,17` |
| `HISTORY` nửa sự kiện im từ `2026-07-31T18:20`, nửa version im từ `2026-08-04` | `git log -- docs/AUTOMATION_HISTORY.jsonl` → `7eb0571` · `a2a7e61` |
| `K2` **loại** marker khỏi phép đo tuổi | thử chặn: giữ marker + mục thật cũ ⇒ **ĐỎ** |
| `DEPLOYED_LIVE_VERIFIED` **không** trong `DONG_STATUSES`/`TREO_STATUSES`, **6 mục** dùng | `_v10958_fu_reader.py:99,130` |
| **`_v10987_governance.py` GHI TÀI LIỆU NGAY KHI IMPORT** | `import` làm CHANGELOG +5.420, SSOT +2.492 ký tự |
| cron 21:50 mới chạy đúng đêm đầu | `model_latency_shadow_v11063` **57 dòng** hôm nay |

### `DOC_SAID`

| tài liệu ghi gì | file:mục | lệch? |
|---|---|---|
| `V101` — luật MN D-1/D-2 `DEPLOYED` | `docs/V101_SHADOW_RULE_PROMPT_REPORT.md` | **⚠ ĐÃ SỬA** — thêm khung, không xoá |
| `RM-17` *"số không tái lập được thì cấm dùng làm căn cứ"* | `CLAUDE.md §61` | **khớp** — nên **không bù** 286 bản |
| `RM-15` *"cổng phải chứng minh chặn được"* | `CLAUDE.md §61` | **khớp** — và chính nó chỉ ra bẫy marker làm mù cổng |
| `V10980` *"nhãn ngoài danh sách ⇒ mục rơi khỏi mọi bộ đếm"* | `_v10981_kiem_lich.py:124` | **khớp** — đang tái diễn với 6 mục |

### Ba lớp lệch nhau ⇒ FINDING

1. **`OWNER_SAID` ≠ trạng thái sổ:** owner dự kiến `QD-060`, thực tế **đã dùng hết tới `QD-063`**.
   Không có cổng thì gói này đã ghi đè lên bản kiểm toán sáng nay.
2. **`DOC_SAID` ≠ `CODE_DID`:** `V101` ghi D-2 `DEPLOYED` trong khi D-2 **đo = 0** và **không
   triển khai**. Đã sửa đúng cách owner yêu cầu — **đánh dấu, không xoá**.
3. **`CODE_DID` tự mâu thuẫn:** một module **quản trị tài liệu** lại **ghi tài liệu ngay khi
   import** — biến một lệnh đọc thành một lệnh ghi.

---

## 7. Vướng vấp — hai lỗi của agent, cả hai đã sửa

### 7.1 · Ghi sai nguyên văn owner ký

Agent viết *"THAM KHẢO**,** KHÔNG TRIỂN KHAI"* (dấu phẩy) trong khi owner ký *"THAM KHẢO **—**
KHÔNG TRIỂN KHAI (đo = 0, V11056)"*.

**Cổng sổ quyết định bắt được** (`→ KHÔNG THẤY trong file`). Đã sửa dùng **đúng nguyên văn**.
Bài học: `§62` đòi **trích nguyên văn**, và sai một dấu câu là đủ để cổng trượt — đó là **tính
năng**, không phải phiền toái.

### 7.2 · `import` một module làm nó GHI VÀO TÀI LIỆU

Agent chạy `import _v10987_governance` chỉ để **đọc hai hằng số**. Module đó **chạy mã cấp module**
và **prepend một bản `V10987` TRÙNG**:

```
CHANGELOG.md              2.302.911 → 2.308.331   (+5.420)
docs/CURRENT_TRUTH_SSOT.md 1.079.202 → 1.081.694   (+2.492)
```

**Đã sửa:** xác minh là bản trùng (`## V10987` xuất hiện **2 lần**), cắt **đúng khối ở đầu**, giữ
nguyên `V11064` nằm dưới. Cả hai tệp về **1 lần** `V10987`.

> **Ghi nhớ cứng:** `_v10987_governance.py` **ghi tài liệu ngay khi import** — **cấm import**, chỉ
> đọc hằng số bằng cách khác. Một lệnh tưởng là **đọc** hoá ra là **ghi**.

---

## 8. Gỡ về

```bash
git revert 9895fc4      # V11064 — chỉ tài liệu + vá cổng §63, không đổi runtime
```

Phiên này **không deploy, không restart**. Nếu cần bỏ `GAP_MARKER`: xoá dòng `"loai":"GAP_MARKER"`
cuối `docs/AUTOMATION_HISTORY.jsonl` — nhưng cổng `K5` sẽ **ĐỎ**, đó là chủ ý.

---

## 9. Theo dõi tiếp

| mã | việc | mốc |
|---|---|---|
| **GÓI 21/08** | **13 mục ĐÃ KHOÁ PHẠM VI** — không thêm không bớt | **21/08** |
| **FU-284** | đọc ngày 20/08, ngưỡng **9,53** — quyết định mục #13 (`GĐ2`) của gói | **20/08** · cấm đọc sớm |
| **FU-398** | lane A/B — 12 cặp, 9 bất đồng | ~**22/08** · cấm đọc sớm |
| **FU-399** | UI `/filter` — **chờ owner mô tả** | HÀNG ĐỢI |
| **HÀNG ĐỢI SAU GÓI** | 6 mục, gồm **`DEPLOYED_LIVE_VERIFIED` chưa đăng ký** (6 mục rơi khỏi bộ đếm) | sau 21/08 |

**Không sinh mã FU mới trong phiên này** — đúng yêu cầu phiên ghi nhận.

---

TanPhatAI cần làm: ① ghi **`QD-064`** với **4 quyết định** và **mã thật là `QD-064`, KHÔNG phải
`QD-060`** (owner dự kiến nhầm, `QD-060`→`063` đã dùng hết trong ngày); ② ghi **`GÓI 21/08` đã
khoá phạm vi 13 mục** — mọi ý tưởng mới vào **HÀNG ĐỢI SAU GÓI**, **không chen vào gói**; ③ ghi
**cảnh báo `D-2` ≠ `D2`** — `D-2` (chéo miền MN) đã loại và **không** trong gói, `D2`
(`MINED_RULES_MODE`) **có** trong gói mục #2, **đừng gỡ nhầm**; ④ ghi **`GAP_MARKER`** và luật
**K2 không tính marker khi đo tuổi** — nếu tính, cổng xanh vĩnh viễn (RM-15); ⑤ ghi cảnh báo
**`_v10987_governance.py` GHI TÀI LIỆU NGAY KHI IMPORT** — cấm import, đã gây prepend trùng một
lần trong phiên này.
