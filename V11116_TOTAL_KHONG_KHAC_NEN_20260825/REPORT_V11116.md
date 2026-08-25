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

## 2 · OWNER YÊU CẦU GÌ (NGUYÊN VĂN + GIỜ)

> **Đọc theo `§57.3` mục 2 bản 25/08 (`PRJ-INTERACTION-LEDGER-001`):** mục này phải liệt kê
> **prompt chính VÀ mọi yêu cầu trực tiếp trong phiên**, kèm **nguyên văn + giờ**. Owner làm việc
> theo dòng liên tục trong IDE, nên phần lớn yêu cầu **không** nằm trong prompt lớn. Chỉ chép
> prompt lớn rồi bỏ qua các câu giữa phiên là `PRJ_INTERACTION_REPORT_MISSING`.
>
> Nguồn: **`docs/SO_TUONG_TAC_OWNER.md`** (sổ append-only, kho riêng).

### 2.1 · Prompt chính — `~12:50`, `PROMPT TỔNG LỰC LẦN 35`

> *«Không mặc định 15 model tốt hơn 8 model. Không mặc định nhiều model tốt hơn ít model.
> Số lượng model chỉ là **tồn kho**.»*

> *«Nếu chưa đủ bằng chứng, vẫn phải chốt: `TOTAL_V2_CANDIDATE` · công thức · scorer · shadow
> pipeline · ngưỡng · ngày đọc lại · điều kiện promotion. **Cấm đổi mù chỉ để có vẻ đã tạo
> phương pháp mới**.»*

> *«Cấm hứa tăng tỷ lệ trúng.»* · *«Cấm lookahead.»* · *«Đăng ký ngưỡng trước khi đọc.»*

### 2.2 · Các yêu cầu TRỰC TIẾP giữa phiên — phần trước nay hay bị bỏ sót

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì |
|---|---|---|---|
| `~13:00` | *«đang đo lường ah em? đợi kết quả hay sao?»* | `HỎI` | Báo trạng thái thật: **6/7 làn đang chạy, 0 làn xong**. Và làm ngay việc bắt buộc phải làm **trước khi số về** — tiền đăng ký ngưỡng `T1…T8` + `R1…R6`, commit `90db2ca` lúc `13:06:08` |
| `~14:26` | *«còn đang chạy không em? xong chưa push báo cáo tổng lực chưa em?»* | `HỎI` | Báo thật: làn đo **xong 14/14**; kho riêng **đã push**; kho công khai **CHƯA** ⇒ viết báo cáo này + context, chạy cổng, đẩy (`e81ce91`) |
| `~18:37` | *«Đã push báo cáo hết chưa em? · Kiểm tra lại toàn bộ 1 lần nữa xem còn gì không để push báo cáo 1 lần luôn · Các vấn đề anh tương tác trực tiếp đã push thành 1 bảng ghi nhận yêu cầu của owner chưa? Có cần cập nhật quy tắc trong claude.md để chuẩn hóa không vì đôi lúc code đi trước tài liệu do tương tác trực tiếp với em liên tục cho liền mạch ah em… việc ghi nhận các yêu cầu xác nhận của anh, chia sẻ của anh là cần thiết kể agent notion không bỡ ngỡ và phản bác nha em. · …em cần ghi nhận trong báo cáo có chuyên mục owner yêu cầu · Các vấn đề đào bới, tra soát, theo dõi cần liệt kê đầy đủ.»* | `YÊU_CẦU` | Dựng luật **`PRJ-INTERACTION-LEDGER-001`** vào **đủ sáu mặt** · mở rộng `§57.3` mục **2/3/9** · dựng **`docs/SO_TUONG_TAC_OWNER.md`** · mở rộng mục 2 và mục 9 của chính báo cáo này · **đẩy một lượt cả hai kho** |

### 2.3 · Vì sao owner nêu yêu cầu ở `~18:37` — và agent thừa nhận chỗ hổng

Owner nói thẳng: *«đôi lúc code đi trước tài liệu do tương tác trực tiếp với em liên tục cho liền
mạch»*. Đó là **mô tả đúng cách làm việc**, và owner **cho phép** code đi trước.

Chỗ hổng thật: kho có `docs/OWNER_DECISION_LEDGER.json` cho **quyết định trang trọng** (`QD-xxx`)
và `docs/SO_YEU_CAU_OWNER_20260824.md` **sinh tự động** từ `FOLLOW_UP_TRACKER` — nhưng **không có
chỗ nào** giữ **lời owner chưa thành quyết định**: xác nhận, chia sẻ, đổi ưu tiên, *«làm cái này
trước»*. Nên agent khác (đặc biệt **TanPhatAI/Notion**) mở kho ra, thấy code đã đi trước tài liệu,
**không tìm được chỗ nào ghi «owner đã bảo làm thế»** ⇒ **bỡ ngỡ và phản bác** ⇒ owner mất công
giải thích lại một việc đã nói rồi.

**Luật mới `PRJ-INTERACTION-LEDGER-001` chốt bốn câu:** ① code **ĐƯỢC** đi trước tài liệu, không
phải vi phạm · ② nhưng **ghi nhận KHÔNG được đi sau quá một phiên** · ③ sổ **append-only** ·
④ mọi báo cáo công khai phải có mục `OWNER YÊU CẦU` **đủ**, không chỉ prompt lớn.

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

### 4.9 · KIỂM KÊ ĐẦY ĐỦ MỌI VIỆC ĐÀO BỚI / TRA SOÁT — kể cả việc ra kết quả ÂM

> **Hai bảng, hai góc — không phải hai bản sao.** Bảng dưới đây là **17 việc theo dòng chảy
> của phiên** (gồm cả việc tra soát *kho* ở cuối phiên, mục 15–17, không có ở bảng kia).
> **`9.2`** là **danh sách 41 phép đo đầy đủ** theo từng phép. Ai cần **đếm phép** thì đọc
> `9.2`; ai cần **hiểu phiên đã đi đường nào** thì đọc bảng này. Sửa số liệu thì **sửa cả
> hai**, đừng để chúng trôi khỏi nhau.

> `§57.3` mục 3 bản 25/08: *«mục 3 phải LIỆT KÊ ĐỦ mọi việc đào bới / tra soát đã làm, **kể cả
> việc đo ra kết quả âm hoặc không kết luận được**»*. Rút gọn mục này làm người đọc sau tưởng
> phiên làm ít hơn thực tế, và **làm mất dấu những phép đo đã tốn công nhưng chưa ra kết luận**.

| # | việc đào bới / tra soát | kết quả | ghi ở |
|---|---|---|---|
| 1 | Chụp trạng thái VPS trước khi chạm: băm **10 tệp runtime** hai phía · lược đồ · bundle · roster/config · cron | **khớp toàn bộ** — nền sạch để benchmark | `5b.1` |
| 2 | Tái lập `M0` từ lá phiếu thô (cổng `T8`) | **423/423 = 100,00%** — roster lịch sử tái lập được ⇒ **không phải dừng** | `4.1` |
| 3 | Benchmark **7 phương pháp** trên cùng snapshot, cùng roster, cùng scorer, không lookahead, 5 cửa sổ, hiệu chỉnh Holm | 🔴 **không phương pháp nào thắng `M0`** | `4.2` |
| 4 | So `M0` **với nền** (chứ không chỉ so với nhau) | 🔴 **`M0` cũng không khác nền** — phát hiện nặng hơn cả mục 3 | `4.3` |
| 5 | Đo giá trị của **bước xếp hạng** | 🔴 **không mang thông tin**, hơi **kém hơn** bốc ngẫu nhiên | `4.4` |
| 6 | Hai **đối chứng ngớ ngẩn** đưa vào để phá kết quả | ⚠ **chúng thắng** — dấu hiệu thước đo chứ không phải phương pháp | `4.5` |
| 7 | **Saturation curve** + **leave-one-out** + **add-one** + **walk-forward** cho câu «bao nhiêu model là đủ» | trả lời được **một phần**; `CORE = 0` model | `4.6` · `4.7` |
| 8 | Tra **trùng lặp nguồn** giữa các model | 🟢 **kết luận có ý nghĩa DUY NHẤT** về roster của cả phiên | `4.7` |
| 9 | Phân loại model theo họ / alias | ⚠ **không kết luận được** — kho **không có bảng family/alias chính thức**, bản đồ hiện do agent tự đặt | `4.8` · `9.3` |
| 10 | Phản biện **7 làn** chạy song song để tự bác kết quả | bác **3 kết luận** của làn đo + **1 tiền đề của chính báo cáo** | `7.1` · `7.2` |
| 11 | Truy lại mẫu thật sự dùng được | ⚠ brief ghi `534`, thật là **`423`** — 90 bundle tháng 2–3 là **backfill** rỗng thành phần | `7.2` |
| 12 | Truy **nhiễm dữ liệu** ở nhánh dự phòng | 🔴 **21,8%** — nhánh rơi về *toàn bộ* model, **không lọc** nguồn chạy | `7.3` |
| 13 | Tính lại `n`-cần **có `z_beta`** | ⚠ số cũ là `n` cho **sức mạnh 50%**; sai lệch hệ thống **đúng 2,04 lần** ⇒ `+3pp` là **10,4–13 tháng**, không phải 5,1 | `7.1` |
| 14 | Đo lại **hệ số cụm cho CHÍNH thước này** (không mượn hằng số cũ — `RM-21`) | **0,994** ⇒ ba miền trong ngày **không tụ** ở thước này | `11` |
| 15 | **Tra soát hai kho trước khi trả lời owner `~18:37`** — commit chưa push · tệp chưa commit · báo cáo thiếu mục | thấy **11 tệp sửa chưa commit** + **`docs/SO_TUONG_TAC_OWNER.md` chưa vào git** | `5b.11` |
| 16 | Tra `§56` (tra trước khi hỏi) xem đã có sổ tương tác chưa | ⚠ có `docs/SO_YEU_CAU_OWNER_20260824.md` **nhưng KHÔNG phải thứ owner cần** — nó **sinh tự động** từ `FOLLOW_UP_TRACKER` (`_v11107_so_yeu_cau_owner.py`), chỉ là bảng mã `FU`, **không giữ lời owner** | `2.3` |
| 17 | Soi **bó xuất bản** `share_exports/` + `share_exports.rar` (**7,7 MB**) đang nằm ngoài git | **KHÔNG đưa vào git** — là bó xuất bản, không phải mã nguồn; đã thêm vào `.gitignore` | `5b.12` |

**Ba việc ra kết quả ÂM hoặc KHÔNG kết luận được — ghi rõ để không ai tưởng đã xong:**
mục **3** (không phương pháp nào thắng) · mục **4** (`M0` không khác nền) · mục **9**
(family/alias — **không có bảng chính thức để đối chiếu**).

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

## 9 · THEO DÕI TIẾP — LIỆT KÊ ĐẦY ĐỦ

> Owner yêu cầu `~18:37`: *«Các vấn đề đào bới, tra soát, theo dõi cần liệt kê đầy đủ.»*
> Mục này **không tóm lược**. Kể cả việc đã đo mà **ra kết quả âm** hoặc **không kết luận được**
> cũng phải có dòng — nếu không, người đọc sau tưởng phiên làm ít hơn thực tế và **mất dấu những
> phép đo đã tốn công**.

### 9.1 · Mười hai mục `GĐ` của prompt 35 — trạng thái từng mục

| mục | nội dung | trạng thái |
|---|---|---|
| `GĐ-0` | bảo toàn 25/08: chụp trạng thái · băm 10 tệp runtime · lược đồ · roster · cron | 🟢 **DONE** — thử chặn 10/10 |
| `GĐ-1` | Algorithm Card AS-IS bốn sản phẩm (BT · Xiên2 · Xiên3 · 3-càng) | 🟡 **dữ liệu ĐÃ ĐO ĐỦ, tài liệu CHƯA VIẾT** |
| `GĐ-2` | tách sinh số / xếp hạng · `GENERATION_MISS` vs `RANKING_MISS` | 🟢 **DONE** |
| `GĐ-3` | bao nhiêu model là đủ · saturation · marginal contribution | 🟢 **DONE** |
| `GĐ-4` | benchmark `M0…M6` | 🟢 **DONE** |
| `GĐ-5` | thước chọn `TOTAL_V2` · tiền đăng ký ngưỡng | 🟢 **DONE** — commit `13:06:08` |
| `GĐ-6` | hợp đồng output không phụ thuộc `N` cố định | 🟢 **DONE** |
| `GĐ-7` | mười bản vá | 🟡 **thiết kế xong (54 kết luận), CHƯA sửa một dòng nào** |
| `GĐ-8` | deploy + live proof | ⚪ **KHÔNG ÁP DỤNG** — không có gì để deploy, gate không đạt |
| deliverable | `AS_IS_TOTAL_OUTPUT` · `DAILY_ROSTER_PROVENANCE` · `FINAL_EVENT_AUDIT_MIGRATION` | 🔴 **CHƯA VIẾT** |
| deliverable | benchmark · saturation · hợp đồng `TOTAL_V2` · tiền đăng ký | 🟢 **DONE** (kho riêng) |
| deliverable | report + conversation context công khai | 🟢 **DONE** |

### 9.2 · Đã ĐÀO BỚI / TRA SOÁT gì — kể cả thứ ra kết quả âm

> Bảng **đầy đủ theo từng phép đo**. Góc nhìn theo **dòng chảy phiên** (kèm phần tra soát
> kho ở cuối phiên) nằm ở **`4.9`**.

| # | đã đo gì | kết quả |
|---|---|---|
| 1 | Tái lập công thức tính điểm từ dữ liệu thành phần | 🟢 **100%** — `10.618/10.618` |
| 2 | Tái lập `M0` top-1 từ lá phiếu thô | 🟢 **`423/423 = 100,00%`** |
| 3 | Benchmark 6 phương pháp vs `M0`, 5 cửa sổ, hiệu chỉnh Holm | 🔴 **âm** — không cái nào đạt |
| 4 | `M0` vs nền ngẫu nhiên, **ba làn độc lập** | 🔴 **âm** — không khác nền |
| 5 | Hit-rate theo từng bậc `r0…r9` | 🔴 **phẳng đều** — xếp hạng không mang thông tin |
| 6 | Bốc ngẫu nhiên trong **chính pool** vs lấy bậc 1 | 🔴 bậc 1 **kém hơn** `1,45` điểm |
| 7 | 100 chiến lược hằng số làm đối chứng | 🔴 **67/100 thắng hệ** |
| 8 | Quy tắc tần suất 30/60/90/180 ngày | 🟡 `90d` cho `39,48%` — **cao hơn cả 7 phương pháp**, chưa hiệu chỉnh |
| 9 | `GENERATION_MISS` vs `RANKING_MISS` | 🟢 sinh số **không phải** chỗ mất (`1,9%`) |
| 10 | `leave-one-out` 21 model | 🔴 **0/21** có ý nghĩa |
| 11 | `add-one` 44 model | 🔴 **0/44** chứng minh được làm tăng |
| 12 | Saturation `k=1…16`, walk-forward 2 cấu hình | 🟢 bão hoà `k=8–10`; **không `k` nào vượt nền** |
| 13 | Biên độ overfit in-sample vs walk-forward | 🟢 đo được **`9,8pp`** |
| 14 | Ma trận trùng lặp nguồn theo family/alias | 🟢 **`+13,4pp ± 3,3`** — kết luận có ý nghĩa **duy nhất** |
| 15 | Truy `15` vs `13` voter vs `30` model trong bảng trọng số | 🟢 giải xong — do **cắt ladder còn top-10** |
| 16 | Truy bốn lớp ghi đè và lớp nào còn bật | 🟢 chỉ **một** lớp còn chạy |
| 17 | Truy `PP1` / `PP5` / các cờ hard-exclude | 🟢 `PP5` **chưa bao giờ chạy** (`0/361`) |
| 18 | `combo-super` kéo model ngoài roster | 🟢 **có thật**, hiếm (`10/73` lượt) |
| 19 | Nhiễm dữ liệu trong lịch sử tin cậy | 🔴 **`21,8%`** |
| 20 | Hệ số cụm (`deff`/`VIF`) **đo lại cho từng thước** | 🟢 `0,902` · `2,542` · `0,994` |
| 21 | Sức mạnh thống kê / `MDE` | 🟢 mẫu chỉ đủ `≥ +6pp` |
| 22 | Ba kết luận của làn đo bị phản biện bác | 🟢 đã sửa **trước** khi công bố |

### 9.3 · Cần OWNER KÝ — không tự làm

| # | việc | vì sao chặn |
|---|---|---|
| 1 | `K1` `M0` **không chuẩn hoá** — biên độ điểm **15 lần** | đổi thuật toán |
| 2 | `K2` **không shrinkage/cap/floor**, hai thang đo bị dùng lẫn (3 lượt ăn giá trị cứng ≈ **gấp 15 lần**) | đổi thuật toán |
| 3 | `K3` **không dedupe family/alias** — `8,3%` cặp hạng1–hạng2 sẽ đảo chiều | đổi thuật toán |
| 4 | `R-a` **thiếu tie-break** khi hoà điểm — chưa nổ nhưng là rủi ro thật | đổi hành vi |
| 5 | `R-b` giới hạn **`50`** dòng lịch sử — hiện `27` nên an toàn; vượt sẽ **âm thầm** bỏ dòng cũ nhất | đổi hành vi |
| 6 | **Ranh giới family/alias** — bản đồ **do agent tự đặt**, kho **không có bảng chính thức** | cần owner chốt định nghĩa |
| 7 | Bỏ **cắt ladder top-10** và **cắt thành phần ở 8** | đổi lược đồ bundle |
| 8 | Mười bản vá `GĐ-7` (fail-open · sổ audit · cutoff `500s` · roster theo ngày · timezone · thử lửa cổng thứ hai · tách `writer_source` · bỏ magic string · 32 dòng di sản) | đều đổi hành vi cổng hoặc lược đồ |
| 9 | **Không dừng model nào** — `CORE = 0`, gate chưa đạt | owner khoá |

### 9.4 · Lịch đã đăng ký

| mốc | ngày | việc |
|---|---|---|
| `D1` | **26/08/2026** | bật 3 ứng viên ở `SHADOW`, `effective_date ≥ 26/08` |
| `D2` | **09/09/2026** | đọc lại lần 1 — 14 ngày prospective |
| `D3` | **23/09/2026** | **NGÀY CHỐT PROMOTION** — trước đó cấm nâng `OFFICIAL` |

### 9.5 · Cảnh báo cổng đầu phiên — chưa xử

mục theo dõi **đến hạn hôm nay**: **6** · **quá hạn**: **125** ·
quyết định **tới hạn rà soát**: **15** · mục treo **thiếu mã đọc**: **3**

### 9.6 · Chỗ tài liệu **chưa bắt kịp code**

| chỗ | trạng thái |
|---|---|
| quy ước giờ **thứ tư** — bảng log ghi **UTC** | 🔴 **tài liệu quản trị vẫn chưa bổ sung** |
| bốn lớp ghi đè (tài liệu cũ ghi «ba») | 🟢 đã sửa trong báo cáo này |
| `SO_YEU_CAU_OWNER_*.md` là bảng **sinh tự động**, không phải sổ tương tác | 🟢 đã làm rõ |

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

TanPhatAI cần làm: ghi nhận **LỐI C** — giữ phương pháp hiện hành, **không đổi**; ghi nhận ngày chốt promotion **23/09/2026**; ghi nhận ba khuyết tật `K1`/`K2`/`K3` và hai rủi ro tiềm ẩn **đều chờ owner ký, chưa vá**; ghi nhận **`CORE = 0` model** và **không dừng model nào**; **KHÔNG** dùng các con số `n`-cần cũ (`~5,1 tháng` / `~1,8 tháng`) — đã bị bác, số đúng là `~10,4` và `~3,7` tháng; và **KHÔNG** đọc *«không khác nền»* thành *«hệ thống vô dụng»* — mẫu hiện tại chỉ đủ phát hiện hiệu ứng từ `6pp` trở lên. · **CODE ĐI TRƯỚC TÀI LIỆU trong phiên này — và đó KHÔNG phải vi phạm** (`PRJ-INTERACTION-LEDGER-001`, owner cho phép tường minh): bảy làn đo + tiền đăng ký ngưỡng chạy từ `~13:00`, còn luật và sổ ghi nhận mới dựng lúc `~18:37`. Chỗ đi trước và lời owner cho phép đều nằm ở **`docs/SO_TUONG_TAC_OWNER.md`** (kho riêng, append-only) — **đọc sổ đó trước khi phản bác bất kỳ thay đổi nào của phiên này**; đừng đoán.
