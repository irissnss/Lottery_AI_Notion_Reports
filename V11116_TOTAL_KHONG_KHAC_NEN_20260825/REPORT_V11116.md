# REPORT V11116 — KIỂM TOÁN TOTAL/OUTPUT: **KHÔNG PHƯƠNG PHÁP NÀO THẮNG `M0`, VÀ `M0` CŨNG KHÔNG KHÁC NỀN**

**Ngày:** 25/08/2026 · **Kho riêng:** `3dc3611` → `90db2ca` → `bb4e4e9`
**Trạng thái:** `REPORT_PROVEN` + `CODE_PUSHED` · **KHÔNG deploy · KHÔNG chạm production**

> ⚠️ **`RM-12`:** phiên này **không** có gì đạt `RUNTIME_PROVEN`. Toàn bộ đọc-only.
> Mọi giờ trong báo cáo là **giờ Việt Nam (UTC+7)**; bảng log của hệ ghi **UTC**, đã cộng 7 giờ.

---

## 1 · TÓM TẮT

Bảy làn đo + **bảy làn phản biện** đọc-only (2,09 triệu token · 458 lượt gọi · 0 lỗi · 41 phút).
Phản biện **bác 36 kết luận**, giữ 92, thêm 57 phát hiện — **và bác cả kết luận đầu của chính
làn đo**.

| câu owner hỏi | trả lời |
|---|---|
| phương pháp nào thắng `M0`? | 🔴 **không cái nào.** Tốt nhất `p_Holm = 0,4611` |
| `M0` có tốt không? | 🔴 **không khác nền** — ba làn độc lập cùng kết luận |
| bao nhiêu model là đủ? | ở **độ chính xác: không có đáp án** · ở **độ phủ: bão hoà `k=8–10`** |
| có deploy không? | 🔴 **KHÔNG** |

---

## 2 · OWNER YÊU CẦU GÌ (NGUYÊN VĂN)

> *«Không mặc định 15 model tốt hơn 8 model. Không mặc định nhiều model tốt hơn ít model.
> Số lượng model chỉ là **tồn kho**.»*

> *«Nếu chưa đủ bằng chứng, vẫn phải chốt: `TOTAL_V2_CANDIDATE` · công thức · scorer · shadow
> pipeline · ngưỡng · ngày đọc lại · điều kiện promotion. **Cấm đổi mù chỉ để có vẻ đã tạo
> phương pháp mới**.»*

> *«Cấm hứa tăng tỷ lệ trúng.»* · *«Cấm lookahead.»* · *«Đăng ký ngưỡng trước khi đọc.»*

---

## 3 · TIỀN ĐĂNG KÝ — làm TRƯỚC khi có số

Ngưỡng `T1…T8` và `R1…R6` chốt tại commit `90db2ca` lúc **`13:06:08 +0700`**, khi **0/7 làn đã
trả kết quả**. Commit đó **là bằng chứng thời điểm**.

Lý do làm trước: dự án **đã phạm đúng lỗi này** ngày 23/08 — so `b+c = 46` với sàn `96` rồi
**tự hạ sàn**. Đặt ngưỡng sau khi nhìn số là cách chắc chắn nhất để tự chứng minh bất cứ điều gì.

---

## 4 · ĐÀO BỚI / PHÁT HIỆN

### 4.1 · Cổng `T8` — `M0` tái lập được không? **ĐẠT**

```
M0 tái lập từ lá phiếu, TOP-1 ......... 423/423 = 100,00%
components vs predictions ............. 10.618/10.618 = 100,00%
scorer vs trạng thái đã lưu ........... 534/534
```

⇒ benchmark có nghĩa. (Nếu trượt, mọi so sánh sẽ vô nghĩa và phải sửa `M0` trước.)

### 4.2 · 🔴 Không phương pháp nào thắng `M0`

Ứng viên tốt nhất: **`+2,84` điểm** (`b=29`, `c=17`, `n=423`), `p` thô `0,0768` →
**Holm `0,4611`**. Ở **cả 5 cửa sổ** không phương pháp nào đạt `p_Holm < 0,05`.

Nó cũng **không ổn định**: nửa đầu `+4,76` (`p=0,0499`) → nửa sau `+0,94` (`p=0,655`); một miền
đổi dấu `+10,00 → −4,23`. Báo con số toàn mẫu hoặc riêng nửa đẹp sẽ thành một «phát hiện» sai.

Nó có **`b+c = 46`**, sàn tiền đăng ký là **`96`**. **Giữ sàn.**

Một ứng viên khác phải **bị loại khỏi bảng**: nó chỉ khác `M0` ở **2/423 = 0,47%** ngày–miền.
Đó không phải phương pháp khác — **đó là `M0`**.

### 4.3 · 🔴 Phát hiện nặng hơn — `M0` cũng không khác nền

**Ba làn ĐỘC LẬP, ba phép tính khác nhau, cùng kết luận:**

| làn | quan sát | nền | `z` |
|---|---|---|---|
| A | `189/534 = 35,4%` | Poisson-binomial `34,0%` | `+0,71` |
| B | `140/423 = 33,10%` | kỳ vọng `143,3` | `−0,348` |
| C | `136/423 = 32,2%` | `33,9%` | `−1,7pp ± 4,2pp` |

Nền tính **riêng từng ngày–miền** theo số đuôi **thật sự về** hôm đó — không dùng `1/100`.

**Bằng chứng mạnh nhất — top-3 DƯỚI ngẫu nhiên:**

```
top-3 của hệ phủ đuôi trúng   68,32%
BA SỐ NGẪU NHIÊN               69,92%     ⇒ DƯỚI ngẫu nhiên 1,60 điểm
top-5   0,8605 vs 0,8566        ≤10 bậc  0,9787 vs 0,9736
```

⇒ ở **mọi độ sâu** của bậc thang, khoảng cách với một bộ số ngẫu nhiên cùng kích thước đều nằm
trong **`±1,6` điểm**. Độ phủ pool `99,29%` chỉ là **hệ quả kích thước pool** — 12 số ngẫu nhiên
cũng cho `98,43%`.

### 4.4 · 🔴 Bước xếp hạng không mang thông tin — và hơi **kém hơn** bốc ngẫu nhiên

```
bốc NGẪU NHIÊN một số trong CHÍNH pool của hệ  →  kỳ vọng 34,55%
lấy bậc 1 thật sự                              →           33,10%   ⇒ −1,45 điểm
hit-rate theo từng bậc r0 → r9                 →  PHẲNG ĐỀU 32,4% – 38,5%
```

**Xếp một bảng 10 bậc mà bậc nào cũng trúng như bậc nào thì phép xếp hạng đó không mang thông
tin.**

**Và tầng sinh số KHÔNG phải chỗ mất:** bậc thang top-10 chứa ít nhất một số trúng ở
**`524/534 = 98,1%`**; mất ở khâu sinh chỉ **`1,9%`**. Mọi nỗ lực thêm model đang **chĩa sai chỗ**.

### 4.5 · Hai đối chứng ngớ ngẩn mà **thắng**

| đối chứng | kết quả |
|---|---|
| 100 chiến lược **hằng số** (*«luôn chọn một số cố định»*) | trung bình `0,3388` (đúng bằng nền) · median **144** · max **177** |
| hệ đạt **140** | ⇒ **67/100 chiến lược hằng số đánh bại hệ** |
| **quy tắc tần suất 90 ngày** (không lookahead) | **`167/423 = 39,48%`** · `z=+2,477` · `p` thô `0,0132` — **cao hơn cả bảy phương pháp** |

Quy tắc tần suất **chưa** qua hiệu chỉnh đa so sánh và **chưa** có prospective ⇒ vào **shadow**,
**không** vào kết luận.

### 4.6 · Bao nhiêu model là đủ

**Walk-forward: không `k` nào từ 1 đến 16 vượt nền.** `leave-one-out` **0/21** có ý nghĩa;
`add-one` **0/44** chứng minh được làm tăng.

**Biên độ overfit đo trực tiếp:** chọn tham lam **trên chính mẫu** cho `39,0%` tại `k=5`;
**cùng thuật toán** chạy walk-forward chỉ còn **`29,2%`** ⇒ khoảng cách **`9,8pp` là overfit
thuần tuý**.

**Thứ duy nhất số model thực sự mua được là BỀ RỘNG:**

```
k=1 53,9% · k=2 73,7% · k=3 81,1% · k=5 90,1% · k=8 94,7% · k=10 95,9% · k=16 98,4%
BÃO HOÀ TỪ k=8–10 · từ model thứ 11 mỗi model thêm chỉ mở rộng < 1pp
```

⇒ **không ủng hộ «15 hơn 8», cũng không ủng hộ «8 hơn 15»** — ở độ chính xác cả hai bằng nền.

### 4.7 · 🟢 Kết luận có ý nghĩa **duy nhất** về roster — trùng lặp nguồn

| | |
|---|---|
| cặp **cùng family** trùng số top1 | **28,6%** |
| cặp **khác family** | **15,2%** |
| chênh | **+13,4pp ± 3,3** (CI95) 🟢 |

**Cơ chế: KHÔNG CÓ dedupe family/alias** — chỉ chống trùng **tên y hệt**. Hàm chuẩn hoá tên
model **có tồn tại** nhưng **chỉ** dùng khi tính trọng số, **không** dùng khi bỏ phiếu.

**Hậu quả:** `15,2%` bậc hạng-1 có số nguồn độc lập **bị thổi phồng**. Một ví dụ thật: một số
ghi **6 voter**, nhưng hai trong số đó là **tổ hợp của** những model đã bỏ phiếu riêng, và một
cái nữa là bộ gộp chọn lại chính chúng ⇒ **thực chất 3 nguồn gốc**.

**Tác động: `21/252` (`8,3%`) cặp hạng1–hạng2 sẽ ĐẢO CHIỀU nếu dedupe**, và `16/21` ca đó số
hạng-1 chính là con số đã công bố.

### 4.8 · Phân loại model

`CORE` = **0** (không model nào chứng minh được bỏ ra thì kết quả giảm) · `RESERVE` **10** ·
`REDUNDANT` **4** · `SHADOW_CHALLENGER` **15** · `INSUFFICIENT_EVIDENCE` **15**.

⛔ **Không dừng model nào** — gate chưa đạt, và owner khoá *«không tự dừng model nếu gate chưa
đạt»*.

---

## 5 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

Theo tiền đăng ký, đây là **LỐI `C`**: *«giữ `M0` tạm thời · vẫn đóng hợp đồng `TOTAL_V2` ·
tiếp tục shadow · **cấm đổi chỉ để có phương pháp mới**»*.

**Vì sao chọn lối này chứ không bật một phương pháp mới:** ứng viên tốt nhất trượt **năm** ngưỡng
đã đăng ký trước (`T1` `T2` `T5` `T6` `T7`). Bật nó lên sẽ là **đổi mù để có vẻ đã tạo phương
pháp mới** — đúng điều owner cấm. Và hạ sàn `96` xuống cho vừa `46` chính là lỗi dự án **đã phạm
ngày 23/08**.

Ba khuyết tật đo được của `M0` — **cả ba chờ owner ký, không tự vá**: không chuẩn hoá (biên độ
điểm 15 lần) · không shrinkage/cap/floor, và hai thang đo khác nhau bị dùng lẫn nhau · không
dedupe family/alias.

---

## 5b · ĐÃ LÀM GÌ

| # | việc | trạng thái |
|---|---|---|
| 1 | **`GĐ-0` bảo toàn** — chụp trạng thái máy chủ trước khi chạm gì: băm 10 tệp runtime hai phía (**khớp toàn bộ**), lược đồ, bundle hiện tại, roster/config, cron | 🟢 thử chặn **10/10** |
| 2 | **Trả lời câu CHẶN** của owner — roster lịch sử **tái lập được**, nên **không phải dừng** | 🟢 |
| 3 | **TIỀN ĐĂNG KÝ ngưỡng** `T1…T8` + `R1…R6` **trước khi có một con số nào** (`13:06:08`, khi `0/7` làn đã trả kết quả) | 🟢 |
| 4 | **Bảy làn đo + bảy làn phản biện** đọc-only — 2,09 triệu token, 458 lượt gọi, 0 lỗi, 41 phút | 🟢 |
| 5 | **Tái lập `M0`** từ lá phiếu thô để qua cổng `T8` | 🟢 **423/423 = 100,00%** |
| 6 | **Benchmark 7 phương pháp** trên cùng snapshot / cùng roster lịch sử / cùng scorer / **không lookahead**, đủ 5 cửa sổ, hiệu chỉnh Holm | 🟢 |
| 7 | **Saturation curve + leave-one-out + add-one + walk-forward** cho câu «bao nhiêu model là đủ» | 🟢 |
| 8 | **Sửa ba kết luận sai** của làn đo và **một tiền đề sai của chính báo cáo**, trước khi công bố | 🟢 |
| 9 | Bốn tài liệu: tiền đăng ký · benchmark · saturation · hợp đồng `TOTAL_V2` | 🟢 |
| 10 | Bốn mặt version + đẩy hai kho | 🟢 |

**KHÔNG làm** (và không được nói là đã làm): không deploy · không restart · không sửa một dòng mã
production nào · không dừng model nào · không đổi phương pháp `TOTAL`.

---

## 6 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| `T8` `M0` tái lập ≥ 99% | 🟢 **ĐẠT** (100,00%) |
| `T1` `b+c ≥ 96` | 🔴 TRƯỢT (`46`) |
| `T2` `\|z\| ≥ 1,96` · `T5` Holm | 🔴 TRƯỢT |
| `T6` nhất quán cửa sổ · `T7` nhất quán miền | 🔴 TRƯỢT |
| thử chặn `GĐ-0` | 🟢 10/10 |
| bốn mặt version | 🟢 ĐẠT |

---

## 7 · VƯỚNG VẤP

**7.1 · Phản biện bác ba kết luận của làn đo — đã sửa TRƯỚC khi công bố.**
① *«lớp ghi đè đang chạy làm giảm kết quả»* — **sai**: con số gộp là hiện vật của việc **gộp hai
lớp ngược dấu**; dấu âm đến **toàn bộ từ các lớp ĐÃ TẮT**, thứ đang chạy cho dấu **dương**.
② *«ba lớp ghi đè»* — thực ra **bốn**, bỏ sót một lớp.
③ công thức `n`-cần **thiếu `z_beta`** ⇒ đó là `n` cho **sức mạnh 50%**. Sửa: mục tiêu `+3pp`
không phải `~5,1` tháng mà là **`~10,4–13` tháng**. Sai lệch hệ thống **đúng `2,04` lần**.

**7.2 · Một tiền đề của chính báo cáo sai.** Brief ghi *«mẫu 534 bundle»*; thật ra chỉ **`423`**
dùng được — 90 bundle tháng 2–3 là **backfill** không có dữ liệu thành phần. Sửa trong cùng
phiên, trước khi công bố.

**7.3 · Nhiễm dữ liệu 21,8%.** Một nhánh dự phòng rơi về **toàn bộ** model trong bảng dự đoán,
**không lọc** nguồn chạy — và chính dữ liệu đó nuôi lịch sử tin cậy của ba phương pháp ứng viên.

---

## 8 · GỠ VỀ

**Không có gì để gỡ** — không sửa mã production, không deploy, không restart. Toàn bộ là
tài liệu + công cụ đo độc lập.

---

## 9 · THEO DÕI TIẾP

| # | việc | trạng thái |
|---|---|---|
| 1 | Ba khuyết tật `K1`/`K2`/`K3` của `M0` | **cần owner ký** |
| 2 | Hai rủi ro tiềm ẩn: thiếu tie-break khi hoà điểm · giới hạn `50` dòng lịch sử | **cần owner ký** |
| 3 | Ranh giới **family/alias** — bản đồ hiện do agent tự đặt, kho **không có bảng chính thức** | **cần owner chốt** |
| 4 | Ba ứng viên vào shadow từ `26/08` | chờ `D1` |
| 5 | Đọc lại `D2 = 09/09` · **chốt `D3 = 23/09`** | đã đăng ký |
| 6 | `GĐ-7` mười bản vá — **mới thiết kế, chưa sửa** | chờ owner |
| 7 | Algorithm Card bốn sản phẩm · `GĐ-8` deploy | **chưa làm** |

---

## 10 · BA LỚP NGUỒN (§62 · A60)

### `OWNER_SAID`

> *«Không mặc định 15 model tốt hơn 8 model… Số lượng model chỉ là **tồn kho**.»*
> *«Cấm đổi mù chỉ để có vẻ đã tạo phương pháp mới.»* · *«Cấm hứa tăng tỷ lệ trúng.»*

### `CODE_DID`

| điều mã **thực sự** làm | bằng chứng |
|---|---|
| công thức tính điểm | tái lập **100%** — `10.618/10.618` thành phần khớp |
| bậc thang bị **cắt còn top-10** | giải thích trọn vẹn mâu thuẫn *«15 model nhưng 13 voter»* trên **168** bundle lệch |
| **không** dedupe family/alias | phép chống trùng duy nhất là so **tên y hệt** |
| một lớp ghi đè **không** cập nhật câu giải thích | **77/534** bundle có con số công bố khác bậc 1 — câu giải thích đang mô tả **một số KHÔNG được công bố** |
| một cơ chế thưởng **chưa bao giờ chạy** | `0/361` bundle |

### `DOC_SAID`

| tài liệu | nói gì | khớp mã? |
|---|---|---|
| brief phiên này | *«mẫu 534 bundle»* | 🔴 **KHÔNG** — `423`. Đã sửa |
| tài liệu quản trị | ba quy ước giờ | 🔴 **THIẾU** bảng log (UTC) — quy ước thứ tư |

### 🔴 BA LỚP LỆCH NHAU — finding bắt buộc báo

**`OWNER_SAID` ≠ `CODE_DID`:** owner khoá *«model cùng alias/family không tính là hai nguồn độc
lập»* — mã **không thi hành điều đó**. Đây là chỗ lệch **có tác động đo được** (`8,3%` cặp
hạng1–hạng2 sẽ đảo chiều).

**`DOC_SAID` ≠ `CODE_DID`:** đã rút lại trong cùng phiên.

---

## 11 · GIỚI HẠN — phải đọc kèm mọi con số ở trên (`RM-04`)

**«Không khác nền» KHÔNG có nghĩa «đã chứng minh bằng 0».**

```
534 quan sát (hệ số cụm đo lại cho CHÍNH thước này = 0,994) chỉ đủ phát hiện hiệu ứng ≥ +6pp
+5pp cần 717 · +4pp cần 1.116 · +3pp cần 1.978        — đều CHƯA ĐỦ
Phát hiện +3pp so với nền: 587 ngày = 1,6 năm   ·   +2pp: 3,6 năm
```

⇒ Câu đúng: **«không có lợi thế đo được ở mức ≥ 6pp; mẫu hiện tại không loại trừ được một lợi
thế nhỏ hơn.»** **Không phải** *«hệ thống vô dụng»*.

---

TanPhatAI cần làm: ghi nhận **LỐI C** — giữ phương pháp hiện hành, **không đổi**; ghi nhận ngày chốt promotion **23/09/2026**; ghi nhận ba khuyết tật `K1`/`K2`/`K3` và hai rủi ro tiềm ẩn **đều chờ owner ký, chưa vá**; ghi nhận **`CORE = 0` model** và **không dừng model nào**; **KHÔNG** dùng các con số `n`-cần cũ (`~5,1 tháng` / `~1,8 tháng`) — đã bị bác, số đúng là `~10,4` và `~3,7` tháng; và **KHÔNG** đọc *«không khác nền»* thành *«hệ thống vô dụng»* — mẫu hiện tại chỉ đủ phát hiện hiệu ứng từ `6pp` trở lên.
