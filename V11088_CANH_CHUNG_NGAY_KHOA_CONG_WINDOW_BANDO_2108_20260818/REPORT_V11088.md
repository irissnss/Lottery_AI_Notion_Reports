# REPORT V11088 — CANH CHỨNG NGÀY KHOÁ 20/08 · CỔNG SELECTION-WINDOW · BẢN ĐỒ 21/08 · CỨU NỐT 52 BẢN SAO

**Ngày:** 2026-08-18 · **Mã đọc:** `KS1808-5` · **Quyết định:** `QD-068`
**Production KHÔNG đổi** — không DB · không deploy · không Notion · `QD-041` nguyên vẹn ·
**không đọc sớm** thước `FU-284` (`RM-03`).

---

## 1. Tóm tắt

| chặng | kết quả |
|---|---|
| **GĐ-0** canh chứng ống đo cho ngày khoá | **3 PASS / 1 FAIL** |
| **GĐ-1** đọc gate DEHERD 19/08 | **KHÔNG thi hành được** — kèm phát hiện |
| **GĐ-2** cổng máy `PRJ-SELECTION-WINDOW-001` | **XONG** — 9/9 thử chặn, **0 báo động giả** |
| **GĐ-3** bản đồ thực thi 21/08 | **XONG** — PLAN-ONLY, phát hiện **va chạm `D2` × `FU-397b`** |
| **GĐ-4** cứu nốt 52 bản sao | **XONG** — **52/52**, 0 mất |

**Hai việc nặng nhất, cả hai đều là thứ chưa ai nêu trước đây:**

**①** Lane T-B **không có bộ chấm nào tồn tại** — ngày 20/08 sẽ có ~140 dòng và **0 cặp đọc
được**. Không phải thiếu mẫu; là **chờ mãi cũng không bao giờ có cặp nào**.

**②** `D2` và `FU-397b` **triệt tiêu nhau** — `D2` đưa bonus `0,40 → 0,00`, tức **tắt đúng thứ
`FU-397b` đang đo**. Gộp hai mục trong ngày 21/08 = giết phép đo ngay khi sinh ra.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«GĐ-0 · CANH CHỨNG READ-ONLY CHO NGÀY KHOÁ — Kiểm toàn bộ ống đo SẴN SÀNG cho 20/08… Mục nào
> FAIL → báo rõ, CẤM tự sửa trong vùng đo.»*

> *«CẤM đọc giá trị thước đo trước 20/08 (RM-03)»* · *«CẤM chấm sớm lane T-B/G2-MB»*

> *«Thử chặn hai chiều bắt buộc + đo báo động giả trên 8 báo cáo thật gần nhất (bài học V11085:
> viết đúng cũng bị bắt nếu dấu hiệu quá rộng)»*

> *«Đầu ra: MỘT tệp PLAN trong docs/ — KHÔNG chạy gì… tối 20/08 TanPhatAI + owner chỉ cần điền
> verdict đo vào là ra lệnh chạy ngay.»*

---

## 3. Đào bới / phát hiện

### 3.1 · GĐ-0 ① — Lane T-B: **không có bộ chấm nào tồn tại**

| | |
|---|---|
| tổng dòng | **110** |
| có **cả** `control_bt` và `tb_bt` | **110** |
| **ĐÃ CHẤM** (`trung_control` + `trung_tb`) | **0** |
| mục tiêu `QD-059` | **96 cặp** |

Quét toàn kho: `trung_control`/`trung_tb` **chỉ xuất hiện ở câu `CREATE TABLE`**
(`_v11059_lane_ab_3tang.py:176-177`). **Không một câu `UPDATE` nào** ghi vào chúng. Cron
`06:00/16:52/17:45` chỉ **thu**, không **chấm**.

Cột `bat_dong` **có** được ghi (79 khác / 31 giống) — lane biết A và B **có khác nhau không**,
nhưng **không biết bên nào thắng**.

⇒ Đây **không phải** *«thiếu 96 cặp, chờ thêm ngày»*. Là **chờ mãi cũng không có cặp nào**.

### 3.2 · GĐ-0 ② — suýt báo FAIL oan

Thoạt đo: **908/5541** lượt `context_pack_chars = 64` ⇒ trông như FAIL nặng.

Tách theo ngày thì **toàn bộ 908 lượt nằm TRƯỚC 09/08** (ngày hỏng cuối cùng là **08/08**,
12/60 lượt). **Trong cửa sổ đo 09→20/08: `0/605`** ⇒ **sạch**.

| ngày | tổng | =64 |
|---|---|---|
| 05–08/08 | 241 | **47** |
| **09→18/08** | **605** | **0** |

Cửa sổ 09→20/08: **10/10 ngày đã qua đều có mặt**; 19–20/08 còn chờ tự nhiên.
**Không đọc giá trị thước** — `RM-03`.

### 3.3 · GĐ-0 ③④ — suýt báo FAIL oan **lần hai**

Ba bảng (`bay_dan_daily_shadow` · `ai_herding_failure_daily` · `v10872_deherd_scoreboard`) thoạt
trông **cũ đến 17/08**, 0 dòng cho 18/08.

Nguyên nhân: ảnh chụp đồng bộ lúc **18:34**, **trước** cron **19:35**. Đồng bộ lại lúc **21:55**
⇒ cả ba đều có dòng 18/08.

Đúng `RM-13` — **nguồn sai thì mọi kết luận sai**. Nếu báo FAIL ngay, owner sẽ đi kiểm hộ ba bảng
đang chạy đúng.

### 3.4 · GĐ-1 — `PL13` **không tồn tại**

| | |
|---|---|
| giờ máy | **18/08 21:5x** — gate `19/08` **chưa tới** |
| `PL13` trong kho | quét toàn bộ `.md`/`.py`/`.json` ⇒ **0 kết quả** |
| ngưỡng DEHERD đăng ký trước | **không có** — chỉ có một ngưỡng cũ trong `docs/archive/`, không liên quan |
| dữ liệu | **sẵn sàng** — `v10872_deherd_scoreboard` **330 dòng**, đủ 18/08 |

⇒ **KHÔNG đọc.** Đọc khi chưa có ngưỡng đăng ký trước là đúng thứ `RM-03` và
`PRJ-SELECTION-WINDOW-001` cấm — ngưỡng đặt sau là ngưỡng **đặt vừa khít quanh kết quả**.

### 3.5 · GĐ-3 — **VA CHẠM `D2` × `FU-397b`**

```
FU-397b  đo bonus RIÊNG  {shadow: 0.00, soft: 0.40, active: 0.80}   (combo_super.py:1901)
D2       đổi MINED_RULES_MODE   soft ─────────────► shadow
                                            ↓
                          bonus 0.40 ─────► 0.00    TẮT thứ FU-397b đang đo
```

`FU-397b` là mục có **bằng chứng mạnh nhất** trong gói: đo được **ngoài cửa sổ chọn**, chạy
**69/90 miền-ngày = 76,7%**, và bảng bonus thật `+0,40` **gấp 2,7 lần** con số `+0,15` mọi tài
liệu vẫn nhắc.

Chạy `D2` **trước** hoặc **cùng ngày** ⇒ phép đo `FU-397b` **chết ngay khi sinh ra**.

---

## 4. Hướng xử lý và vì sao chọn

**Vì sao KHÔNG tự sửa lane T-B.** Owner viết thẳng *«Mục nào FAIL → báo rõ, CẤM tự sửa trong
vùng đo»* và *«CẤM chấm sớm lane T-B»*. Dựng bộ chấm bây giờ là **vừa sửa vùng đo vừa chấm sớm**.
Nên: **trình ba lối** (§9), owner chọn.

**Vì sao KHÔNG đọc DEHERD dù dữ liệu sẵn sàng.** Không có ngưỡng đăng ký trước. Đây đúng ca
`FU-316` đã cứu tuần trước: nếu không đăng ký ngưỡng trước, báo cáo đã ghi *«tìm ra nguyên
nhân»* cho một thứ không tồn tại.

**Vì sao cổng `SELECTION-WINDOW` canh việc BÁO chứ không canh việc ĐO.** Cổng không thể biết
người ta đã đo bao nhiêu cửa sổ. Nó chỉ biết **báo cáo nói gì**. Và tác hại nằm ở chỗ **báo** —
trích một cửa sổ thuận là tạo ra một «lợi thế» **hoàn toàn do cách vạch cửa sổ**.

**Vì sao bản đồ 21/08 chia ba làn.** `QD-018` «một biến một lần» là ràng buộc mạnh nhất của ngày
đó. Gói có **bốn** mục chạm đường sinh số; chạy cả bốn cùng ngày thì **mọi phép đo sau đó vô
nghĩa** — đúng vết `FU-284` đã dẫm và đang phải **đếm lại lần ba**.

---

## 5. Đã làm gì

### GĐ-2 — cổng `PRJ-SELECTION-WINDOW-001` · commit `3b987c4`

| | |
|---|---|
| nguồn | **`docs/SO_CUA_SO_CHON.json`** — 3 thước (`TW-001` bạch thủ · `TW-002` bộ k số · `TW-003` luật khai mỏ), **cấm hardcode** |
| BLOCK khi | thước có mặt **và** < `toi_thieu_cua_so` nhãn cửa sổ **và** vùng có từ ngữ tuyên bố hiệu quả **và** không có từ khoá miễn trừ **và** không trong khối ``` |
| thử chặn | **9/9 ĐẠT** |
| báo động giả trên 8 báo cáo thật | **0** (trước sửa: **3**) |
| đã cắm hook | hook nay chạy **8 cổng** |

### GĐ-3 — `docs/BAN_DO_THUC_THI_2108.md` · commit `f4bbb53` · **PLAN-ONLY**

**Ba làn:** `L1` không chạm đường sinh số (chạy hết trong ngày) · `L2` chạm đường sinh số
(**nối tiếp, mỗi lần một mục**) · `L3` có điều kiện.

**Thứ tự `L2`, mỗi vị trí có lý do:**

| thứ | mục | vì sao ở đây |
|---|---|---|
| 1 | `FU-404` sửa nhãn `HR12W` | sửa **nhãn sai** trước khi đo bất cứ thứ gì dùng nhãn đó; **39%** bộ luật đang được giới thiệu bằng con số nói quá |
| 2 | `FU-397b` `+0,40` | bằng chứng **mạnh nhất** (ngoài cửa sổ chọn, 76,7% ngày) ⇒ chạy sớm để có cửa sổ đo dài nhất |
| 3 | `D2` | **sau** `FU-397b` vì va chạm ở §3.5 |
| 4 | `D3` gỡ `RR §11`+`§18` | đổi **cấu trúc** prompt, dễ che lấp ba mục trên; bắt buộc **dump prompt từ hàm đang serve** |
| 5 | `FU-394` hot/cold filter | **cuối**, vì nó lọc **sau** mọi thứ trên |

Kèm **4 ô điền verdict** · **điểm gỡ về từng mục** · **bảng kiểm 9 bước** · **§9 ghi rõ bản đồ
KHÔNG quyết gì**.

### GĐ-4 — cứu nốt 52 bản sao

**52/52 · 0 mất · 20,7 MB.** Thêm **`diff` vs tệp đích hiện tại** chứ không chỉ chép —
`BS-037` chỉ **5 dòng khác**, `BS-043` **111 dòng**. **14** truy ra tệp đích · **38**
`KHÔNG_KIỂM_ĐƯỢC` (**cấm đoán**).

**READ-ONLY bằng BĂM:** `main.py` · `scheduler.py` · `_v11059_lane_ab_3tang.py` ·
`gpt_analyzer.py` — trước = sau, **không đổi một byte**.

---

## 6. Cổng kiểm

| cổng | |
|---|---|
| `_v11062 --kiem` **K1–K4** | **✓ ĐẠT** |
| `_v11088 --thu-chan` | **✓ 9/9** |
| `_v11088 --do-bao-dong-gia` | **✓ 0 báo động giả**/8 báo cáo thật |
| `_v11085_cong_rut_lai --thu-chan` | **✓ 10/10** |
| `_v10981_kiem_lich` K8 | **✓ ĐẠT 8/8** · in dòng miễn trừ |
| ghi tệp an toàn · đoán tên · mất mục · đóng băng · chéo quyết định · sáu mặt | **✓ 6/6** |

> `K1` **ĐẠT thật** sau `V11087` — không có mục nào thiếu `HISTORY`.

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| nội dung | nguyên văn |
|---|---|
| canh chứng | *«Kiểm toàn bộ ống đo SẴN SÀNG cho 20/08… Mục nào FAIL → báo rõ, CẤM tự sửa trong vùng đo»* |
| cấm nhìn sớm | *«CẤM đọc giá trị thước đo trước 20/08 (RM-03)»* · *«CẤM chấm sớm lane T-B»* |
| đo báo động giả | *«bài học V11085: viết đúng cũng bị bắt nếu dấu hiệu quá rộng»* |
| bản đồ | *«KHÔNG chạy gì… chỉ cần điền verdict đo vào là ra lệnh chạy ngay»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| lane T-B **0 cặp chấm** | `trung_control` chỉ ở `_v11059:176-177`; 0 câu `UPDATE` toàn kho |
| 908 lượt hỏng **đều trước 09/08** | trong cửa sổ 09→18/08: **0/605** |
| 3 bảng «cũ» là do ảnh chụp | đồng bộ 18:34 → 21:55 ⇒ đủ dòng 18/08 |
| `PL13` không tồn tại | quét `.md`/`.py`/`.json` ⇒ 0 |
| `D2` tắt bonus của `FU-397b` | `combo_super.py:1901` `{shadow:0.0, soft:0.40, active:0.80}` |
| cổng window 9/9 · 0 báo động giả | `--thu-chan` · `--do-bao-dong-gia` |
| 52/52 cứu · băm trước=sau | `PHU_LUC_BAN_SAO.md` |

### `DOC_SAID`

| tài liệu ghi gì | lệch? |
|---|---|
| `FU-398`: *«đọc khi đủ ≥96 cặp bất đồng»* | **LỆCH** — không có cặp nào **được chấm**, và **không có bộ chấm** |
| gói 21/08: `D2` và `FU-397b` cùng danh sách | **LỆCH** — không tài liệu nào nêu **hai mục triệt tiêu nhau** |
| `FU-406`: `SELECTION-WINDOW` 2 ca, `PROMPT-COHERENCE` 1 ca | **khớp** — dựng đúng một cổng |

### Ba lớp lệch nhau ⇒ FINDING

**`DOC_SAID` ≠ `CODE_DID` — hai chỗ, cả hai đều chặn ngày khoá:** ① `FU-398` mô tả một điều kiện
đọc (**≥96 cặp**) mà **cơ chế sinh ra cặp không tồn tại**; ② gói 21/08 xếp `D2` và `FU-397b` cạnh
nhau **như hai mục độc lập**, trong khi mục này **tắt** mục kia.

---

## 7. Vướng vấp — **bốn**, cả bốn bắt được vì NHÌN SỐ

| # | vấp | bắt được bằng |
|---|---|---|
| 1 | suýt báo FAIL `FU-284` từ `908/5541` | **tách theo ngày** — toàn bộ nằm trước cửa sổ |
| 2 | suýt báo FAIL 3 bảng «cũ đến 17/08» | nhận ra **ảnh chụp 18:34 < cron 19:35**, đồng bộ lại |
| 3 | «8 báo cáo gần nhất» ra `V91`/`V90` tháng 5 | **nhìn tên** — sắp theo chuỗi thì `'9' > '1'` |
| 4 | cổng mới **3 báo động giả** trên báo cáo đã push | **phép đo owner bắt buộc** |

**Vấp 3 là đúng lớp lỗi đã vấp ở `_v11083`** — sửa bằng cách **chép lại khoá sắp xếp đã đúng**,
không sáng chế cách thứ hai.

**Vấp 4 chia hai loại, và sửa ở hai chỗ khác nhau:**
· `lo2` khớp **bên trong** định danh `v66_1_lag1_adaptive_exploit_signal_v2_…` ⇒ sửa **cổng**:
dấu hiệu ≤4 ký tự đòi **biên từ**;
· cửa sổ **đối xứng** 25 dòng kéo nhãn từ mục **khác** vào và **không với tới** bảng nằm **sau**
⇒ sửa **SỔ**: cửa sổ **LỆCH** (lùi 6 · tới 45), vì báo cáo luôn viết theo lối *«nêu rồi mới trưng
bảng»*; thêm **5 từ khoá miễn trừ** cho báo **kết quả một ngày**.

**Trước sửa 3 → sau sửa 0.** Cắm bản đầu thì cổng **đỏ ngay trên chính báo cáo viết đúng**.

---

## 8. Gỡ về

```bash
git revert f4bbb53   # GĐ-3 bản đồ 21/08 (chỉ là giấy tờ)
git revert <GĐ-4>    # cứu 52 bản sao (chỉ thêm artifacts)
git revert 3b987c4   # GĐ-2 cổng window (gỡ luôn khỏi hook)
```

`GĐ-0`/`GĐ-1` **không có gì để gỡ** — read-only.

---

## 9. Theo dõi tiếp

### ⚠️ BA VIỆC CHỜ OWNER — hai việc có **hạn cứng 20/08**

| # | việc | hạn |
|---|---|---|
| **1** | **Lane T-B** — chọn lối **A** (chấm ngược 110 dòng) / **B** (chỉ chấm từ nay) / **C** (đóng `FU-398`, ghi *«đo không thực hiện được»*) | **trước 21/08** · khuyến nghị **A** |
| **2** | **Ngưỡng `PL13` / DEHERD** — ký một ngưỡng **bằng số** | **trước 20/08**, không thì **cấm đọc** |
| **3** | **Ngưỡng bầy đàn** — ký một ngưỡng **bằng số** | **trước 20/08**, không thì **cấm đọc** |

### Đã sẵn sàng cho 20/08

`FU-284` **dữ liệu đủ** (trace sạch trong cửa sổ · 10/10 ngày đã qua · manifest < 6h) — chỉ chờ
19–20/08 về tự nhiên rồi đọc **đúng ngày**, ngưỡng **≥ 9,53**.

### Mục mới

**Không mở FU mới trong phiên này** — mọi phát hiện đều gắn vào mục có sẵn
(`FU-398` · `FU-406` · `FU-409` · `FU-284`), đúng giới hạn ≤5 FU/phiên.

**Verdict tách hai dòng:**
- **`CODE_PUSHED`** = `3b987c4` (GĐ-2) · `<GĐ-4>` · `f4bbb53` (GĐ-3)
- **`REPORT_PUBLISHED`** = bản này

---

TanPhatAI cần làm: ① ghi **lane T-B KHÔNG ĐỌC ĐƯỢC ngày 20/08** — 110 dòng, **0 cặp chấm**, và
**không có bộ chấm nào tồn tại** trong kho ⇒ chờ owner chọn lối **A/B/C**; ② ghi **va chạm
`D2` × `FU-397b`** — `D2` đưa bonus `0,40 → 0,00`, **tắt đúng thứ `FU-397b` đang đo** ⇒ **cấm
gộp** trong ngày 21/08; ③ ghi **`PL13` KHÔNG TỒN TẠI trong kho** và **không có ngưỡng DEHERD/bầy
đàn đăng ký trước** ⇒ owner phải ký **trước 20/08**, không thì **cấm đọc** (`RM-03`); ④ ghi
**cổng `PRJ-SELECTION-WINDOW-001` đã dựng và cắm hook** — nguồn `docs/SO_CUA_SO_CHON.json`, thêm
thước mới **chỉ sửa JSON**; ⑤ ghi **bản đồ 21/08** `docs/BAN_DO_THUC_THI_2108.md` — tối 20/08 chỉ
cần điền **4 ô**; ⑥ ghi **52/52 bản sao đã cứu, 0 mất**, kèm **`diff`** để không phải mở tệp 1 MB;
⑦ ghi **`FU-284` dữ liệu ĐỦ** — 908 lượt hỏng **đều trước cửa sổ**, trong cửa sổ **0/605**.
