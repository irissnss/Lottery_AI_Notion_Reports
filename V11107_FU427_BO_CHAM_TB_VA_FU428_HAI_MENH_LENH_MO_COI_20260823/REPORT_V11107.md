# V11107 — 2026-08-23 (tối) — FU-427 BỘ CHẤM T-B IN ĐÚNG THƯỚC · FU-428 GỠ **HAI** MỆNH LỆNH MỒ CÔI · DỰNG CỔNG `PRJ_PROMPT_DANGLING` · `RR-16.5` → `RR-16.6`

**Ngày làm việc:** 23/08/2026 ·
**Ngày viết báo cáo này:** 26/08/2026 · **Commit riêng:** `8ca990d` ·
**Trạng thái:** `BÙ TỪ NGUỒN GỐC`

---

> ## ⚠️ ĐÂY LÀ BÁO CÁO **BÙ**, KHÔNG PHẢI BẢN VIẾT LÚC LÀM VIỆC
>
> Bản `V11107` làm ngày **23/08** nhưng **không có** thư mục báo cáo công khai —
> vi phạm `§57.2` đã tồn tại **3 ngày**.
> Cổng A55 cũ **không thấy** vì nó chỉ soi **8 bản gần nhất** (đã vá ở `V11122`, `FU-442`).
>
> **Ba nguồn dựng nên bản này — cả ba đều là bản ghi ĐƯƠNG THỜI:**
>
> | nguồn | quy mô |
> |---|---|
> | khối `## V11107` trong `CHANGELOG.md` — viết **ngay lúc làm việc** | **12,091 ký tự / 214 dòng** |
> | commit git mang nhãn `V11107` | **1** commit |
> | lượt owner trong vết phiên `.jsonl` cùng ngày | **có** |
> | khối phụ (`V11107b`/`c`/…) | — |
>
> 🔴 **PHẦN KHÔNG KHÔI PHỤC ĐƯỢC** — ghi thẳng, không suy:
> · **giờ chính xác** từng thao tác trong phiên · **vướng vấp giữa chừng** không được ghi lại lúc đó
> · **hash 4 bảng khoá trước/sau** (nếu phiên có chạm DB) · **PID trước/sau** (nếu có restart).
> Những chỗ đó dưới đây đều ghi `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.

---

## 1. Tóm tắt

### 🔴 RÚT LẠI TRONG CHÍNH MỤC NÀY — `FU-427` bản đầu **TỰ ĐỔI NGƯỠNG SAU KHI THẤY SỐ**
**Chỗ gốc:** `CHANGELOG.md` mục `V11107` (chính mục này) · `docs/CURRENT_TRUTH_SSOT.md` mục
`V11107` · `docs/FOLLOW_UP_TRACKER.md` khối `FU-427` · commit `8ca990d`, **đã đẩy lên remote
lúc 21:2x ngày 23/08**. Bản sai đã lưu hành, nên rút lại ở đây chứ không sửa lặng lẽ.
**Nguyên văn câu sai:**
> *«`122` là số dòng hai DỰ ĐOÁN khác nhau; ngưỡng `96` của `QD-059` đăng ký cho **cặp lệch
> KẾT CỤC** (`b+c`). Con số đó là **46**.»*
> *«CẶP LỆCH KẾT CỤC (b+c) : 46 [ngưỡng QD-059: ≥96] ← ĐÂY mới là số so với ngưỡng»*
> *«⛔ CHƯA ĐƯỢC PHÉP KẾT LUẬN — còn thiếu **50 cặp lệch kết cục** · còn thiếu 1 ngày»*
**Điều đúng.** Ngưỡng đăng ký trước, viết **11/08** — trước mọi kết quả — nguyên văn ở **ba
nơi độc lập**, và cả ba đều nói **«cặp BẤT ĐỒNG»**, không phải `b+c`:
| nguồn | nguyên văn |
|---|---|
| `docs/CURRENT_TRUTH_SSOT.md:818` | *«NGƯỠNG ĐĂNG KÝ TRƯỚC: `≥96 cặp bất đồng` VÀ `\|z\| ≥ 1,96`»* |
| `docs/BAN_DO_THUC_THI_2108.md:19` | *«`≥96 cặp bất đồng` **VÀ** `\|z\| ≥ 1,96`»* |
| `docs/DUYET_GOP_2208.md:411` | *«ngưỡng đăng ký trước từ 11/08: **≥ 96 cặp bất đồng** và trị tuyệt đối của `z` **≥ 1,96**»* |
Và ngày **20/08** chính dự án đọc đúng như vậy — `docs/BAN_DO_THUC_THI_2108.md:219`:
*«**Sàn mẫu ĐẠT (100 ≥ 96)** nhưng `|z| = 0,480` ⇒ CHƯA ĐƯỢC PHÉP KẾT LUẬN»*.

## 2. Owner yêu cầu gì (nguyên văn)

> *«PROMPT TỔNG LỰC LẦN 28 — 23/08: TRUY 9 ms + TRUY KHÂU RÚT SỐ + VÁ FU-419 LỐI (a) ═══ OWNER ĐÃ KÝ (03:44 + 03:50 23/08) — KHÔNG HỎI LẠI ═══ ① Duyệt truy tiếp CẢ HAI: con số 9 ms chưa giải thích + khâu rút số (33.685 token không cho ra số nào). ② FU-419 lối (a): dòng «D-1 cross-region tail pool» chuyển thành GHI SỐ ĐẾM, bỏ danh sách. Ghi nhận điều kiện đi kèm: CẤM hứa nó làm tăng độ trúng (FU-316 đã đo: 20,2% vs nền 21…»*
> — owner, **23/08/2026 03:53** (giờ VN)

> *«push báo cáo chưa em?»*
> — owner, **23/08/2026 04:37** (giờ VN)

> *«Phiên prompt lần 28 đã xong việc nhưng báo cáo CHƯA lên kho GitHub công khai. Đóng phiên đúng kỷ luật: nâng bốn mặt version (_v11062) → lấy số hiệu từ _v11044 → đẩy báo cáo + tài liệu lên kho công khai → chạy cổng cuối phiên → xác nhận commit đã thấy trên remote. Xong báo lại mã commit.»*
> — owner, **23/08/2026 04:46** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 29 — TỐI 23/08: ĐÁNH GIÁ DỰ ĐOÁN + XỬ LÝ TOÀN BỘ TỒN ĐỌNG LỖI + ĐỌC LANE T-B + CHUYỂN HOÁ NGỮ CẢNH ĐỢT 1 ═══ BỐI CẢNH ═══ Live 23/08 đã kết thúc. Owner yêu cầu TỔNG LỰC: đánh giá dự đoán hôm nay, xử lý toàn bộ các lỗi đã được ký duyệt (FU-421, 425, 426, dòng chị em FU-419), đọc lane T-B (đã đủ 14 ngày), và bắt đầu CHUYỂN HOÁ NGỮ CẢNH NGAY LẬP TỨC (đợt 1). Không dậm chân tại chỗ. ═══ GĐ-0 · ĐÁNH GI…»*
> — owner, **23/08/2026 19:47** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 30 — 24/08: AUDIT CỰC GẮT — KIỂM CHỨNG DỮ LIỆU + ĐO MODEL AI NGAY + RỖNG→NGUYÊN NHÂN→THAY + ML GỐC→NGỌN + CHẤM DỨT "ĐO HOÀI KHÔNG RA" ═══ BỐI CẢNH ═══ Owner chất vấn 6 điểm: ① nghi ngờ dữ liệu kết quả bị ghi đè/trôi (MN không có bạch thủ 10) ② đòi ĐO MODEL AI TỚI ĐÂU NGAY, không chờ chuyển đổi ngữ cảnh ③ so sánh shadow vs official chéo regime là SAI (1 thằng nhồi số bốc thăm, 1 thằng tự kiếm số th…»*
> — owner, **23/08/2026 20:45** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 30 — 23/08 TỐI (CHẠY NGAY): AUDIT CỰC GẮT — KIỂM CHỨNG DỮ LIỆU + ĐO MODEL AI NGAY + RỖNG→NGUYÊN NHÂN→THAY + ML GỐC→NGỌN + CHẤM DỨT "ĐO HOÀI KHÔNG RA" ═══ BỐI CẢNH ═══ Owner chất vấn 6 điểm (20:42) + đòi tổng hợp toàn bộ yêu cầu (20:32) + yêu cầu CHẠY NGAY (20:51), không chờ 05:00. PHẦN AUDIT READ-ONLY LÀM NGAY. Chỉ 2 việc gắn mốc sau (ghi rõ trong báo cáo, không chặn phần còn lại): xác minh CTX-18…»*
> — owner, **23/08/2026 22:20** (giờ VN)


*(Trích từ corpus lượt owner đã khử trùng của vết phiên `.jsonl`; giờ đã quy về giờ Việt Nam.)*

## 3. Đào bới / phát hiện

Toàn văn khối `CHANGELOG` đương thời — **nguồn chính** của bản này:

## V11107 — 2026-08-23 (tối) — FU-427 BỘ CHẤM T-B IN ĐÚNG THƯỚC · FU-428 GỠ **HAI** MỆNH LỆNH MỒ CÔI · DỰNG CỔNG `PRJ_PROMPT_DANGLING` · `RR-16.5` → `RR-16.6`

### 🔴 RÚT LẠI TRONG CHÍNH MỤC NÀY — `FU-427` bản đầu **TỰ ĐỔI NGƯỠNG SAU KHI THẤY SỐ**

**Chỗ gốc:** `CHANGELOG.md` mục `V11107` (chính mục này) · `docs/CURRENT_TRUTH_SSOT.md` mục
`V11107` · `docs/FOLLOW_UP_TRACKER.md` khối `FU-427` · commit `8ca990d`, **đã đẩy lên remote
lúc 21:2x ngày 23/08**. Bản sai đã lưu hành, nên rút lại ở đây chứ không sửa lặng lẽ.

**Nguyên văn câu sai:**

> *«`122` là số dòng hai DỰ ĐOÁN khác nhau; ngưỡng `96` của `QD-059` đăng ký cho **cặp lệch
> KẾT CỤC** (`b+c`). Con số đó là **46**.»*
> *«CẶP LỆCH KẾT CỤC (b+c) : 46 [ngưỡng QD-059: ≥96] ← ĐÂY mới là số so với ngưỡng»*
> *«⛔ CHƯA ĐƯỢC PHÉP KẾT LUẬN — còn thiếu **50 cặp lệch kết cục** · còn thiếu 1 ngày»*

**Điều đúng.** Ngưỡng đăng ký trước, viết **11/08** — trước mọi kết quả — nguyên văn ở **ba
nơi độc lập**, và cả ba đều nói **«cặp BẤT ĐỒNG»**, không phải `b+c`:

| nguồn | nguyên văn |
|---|---|
| `docs/CURRENT_TRUTH_SSOT.md:818` | *«NGƯỠNG ĐĂNG KÝ TRƯỚC: `≥96 cặp bất đồng` VÀ `\|z\| ≥ 1,96`»* |
| `docs/BAN_DO_THUC_THI_2108.md:19` | *«`≥96 cặp bất đồng` **VÀ** `\|z\| ≥ 1,96`»* |
| `docs/DUYET_GOP_2208.md:411` | *«ngưỡng đăng ký trước từ 11/08: **≥ 96 cặp bất đồng** và trị tuyệt đối của `z` **≥ 1,96**»* |

Và ngày **20/08** chính dự án đọc đúng như vậy — `docs/BAN_DO_THUC_THI_2108.md:219`:
*«**Sàn mẫu ĐẠT (100 ≥ 96)** nhưng `|z| = 0,480` ⇒ CHƯA ĐƯỢC PHÉP KẾT LUẬN»*.

Nghĩa là thiết kế **vốn đã đúng**: `96` là **sàn hoạt động của lane** đặt trên số bất đồng, còn
phần thống kê do `|z| ≥ 1,96` gánh. `b+c` là **mẫu số của `z`** — nó chưa bao giờ là cái sàn.

**Phép đo tái lập được** (`RM-11`) — `_v11089_cham_lane_tb.py --chi-dem`, DB production 23/08:

```
── BA ĐIỀU KIỆN ĐĂNG KÝ TRƯỚC (11/08 · QD-059 + QD-017) — phải ĐẠT CẢ BA ──
  ✓ số cặp BẤT ĐỒNG : 122   [QD-059 cần ≥96]
  ✗ số NGÀY         : 13    [QD-017 cần ≥14]
  ✗ |z| McNemar     : 0.5898 [QD-059 cần ≥1.96]
      z = (b−c)/√(b+c) = (21−25)/√46 = -0.5898
⛔ CHƯA ĐƯỢC PHÉP KẾT LUẬN (RM-04) — mới 13 ngày, cần 14 · |z| 0.5898 < 1.96
```

**Quyết định nào đã dựa trên số sai:** *(phần bắt buộc thứ tư của `PRJ-RETRACTION-001`)*
**Không có quyết định nào** — và đó là may, không phải nhờ cẩn thận. Bản sai sống đúng ~30
phút, trong đó lane **không được đọc** ở cả hai bản (bản sai bảo thiếu 50 cặp, bản đúng bảo
thiếu 1 ngày và `|z|` còn xa). **Phán quyết trùng nhau, lý do khác hẳn.**

**Vì sao đây là lỗi NẶNG dù verdict không đổi.** Bản sai **nâng sàn** từ 96-trên-bất-đồng
(đã đạt từ ~20/08) lên 96-trên-`b+c` (46, tức thiếu hơn một nửa) — **sau khi đã nhìn thấy
số**. Owner khoá đúng câu này ở dòng kỷ luật `GĐ-3`: *«CẤM tự ý đổi ngưỡng sau khi thấy số»*.
Nếu số nghiêng chiều khác, cùng thao tác đó sẽ là **dời cột gôn**.

**Và bài thử chặn KHÔNG bắt được — đây mới là phần đáng sợ nhất.** Bản đầu `_v11107_thu_chan_
fu427.py` **ĐẠT 9/9** trên chính cái ngưỡng bịa ra. Bài thử chỉ chứng minh hàm làm **đúng
điều nó được viết ra để làm**; nó **không** kiểm được điều đó có phải điều **ĐÃ ĐĂNG KÝ**
hay không. Chín dấu ✓ xanh trên một ngưỡng sai vẫn là chín dấu xanh.

Nay bài thử có riêng **phép [10]**: đối chiếu ba con số ngưỡng **trong mã** với bản đăng ký
`(96 · 1,96 · 14)`. **13/13 ĐẠT.**

**Điều gì THẬT SỰ hỏng ở bản in cũ** — có thật, chỉ là bản đầu vá sai chỗ:

```
trong đó bất đồng (A≠B) : 122   [ngưỡng QD-059: ≥96]
```

Nó in **một** điều kiện kèm ngưỡng của điều kiện đó, mà **giấu hai điều kiện còn lại**
(`|z| ≥ 1,96` và `QD-017 ≥14 ngày`). Đọc lướt là dừng ở *«122 ≥ 96 ⇒ đủ»*. Cách vá đúng là
**in cả ba**, mỗi cái kèm ngưỡng của chính nó — **không đụng tới bất kỳ ngưỡng nào**.

**Đọc lane hôm nay, đúng phạm vi cho phép:** sàn mẫu **đã đạt**; điều kiện phân định là `|z|`,
hiện **0,59** so với cần **1,96**. `c=25 > b=21` (T-B đúng nhiều hơn 4 lượt trên 46) — **CẤM
đọc thành «T-B thắng»**: `|z|` còn cách ngưỡng rất xa, và owner khoá *«CẤM kết luận ngoài
ngưỡng»*.

**Sức mạnh (`RM-03` bắt buộc tính `n` cần):** giữ nguyên chênh lệch hiện tại
`(b−c)/(b+c) = −4/46 = −0,087`, cần `n = (1,96/0,087)² ≈ **508** cặp lệch kết cục`. Tốc độ
thật **46 cặp / 13 ngày ≈ 3,5 cặp/ngày** ⇒ **≈ 131 ngày nữa**. **Kèm cảnh báo `RM-21`:** con
số `−0,087` tự nó đo trên `n = 46`, **rất không ổn định** — nó có thể đổi cả dấu khi thêm vài
ngày, nên `508` là **phép ước lượng độ lớn**, không phải lịch trình.

---

### ĐÍNH CHÍNH NGAY TRONG MỤC NÀY — ba câu bản đầu viết sai

Mục này được viết **hai lần** trong cùng buổi tối. Bản đầu ghi ba điều, cả ba sai, và cả ba
đều được chính công cụ trong phiên lật lại. Ghi ở đây thay vì sửa lặng lẽ, vì mục đã **ĐẨY LÊN
VPS** một lần với nội dung của bản đầu.

| bản đầu viết | ĐÚNG là | ai lật |
|---|---|---|
| *«`CTX-18.6` → `CTX-18.7`»* | **`RR-16.5` → `RR-16.6`** — dòng gỡ nằm trong `REASONING_RULEBOOK`, **nâng nhầm lớp** | đọc lại `PROMPT_VERSIONS`: `reasoning_rulebook` phủ thân chứa dòng `:736` |
| *«đúng một dòng · không có họ lỗi phía sau»* | **HAI dòng** — còn `WEEKLY LIVINGNESS`, mồ côi từ **07/08**, **16 ngày** | bộ đếm trong script đẩy nới rộng hơn dự định ⇒ lộ ra **tình cờ** |
| *«cổng tìm ra 10 mệnh lệnh mồ côi»* | **1** — bản nháp cổng đo thiếu nguồn và đếm chuỗi thô | xem mục cổng bên dưới |

`CTX-18.7` **đã đẩy lên VPS lúc 21:02** rồi sửa lại lúc 21:1x. Trong khoảng đó **không lượt dự
đoán nào chạy** — bốn bảng khoá `+0` ở cả hai lượt đẩy, lượt kế tiếp là **05:00**. Nên **không
bản ghi nào đóng dấu `CTX-18.7`**, và `context_pack` đã trả về `CTX-18.6`.

### FU-427 — bộ chấm lane T-B in con số SAI VẾ ngay cạnh ngưỡng

TRƯỚC:

```
trong đó bất đồng (A≠B) : 122   [ngưỡng QD-059: ≥96]
```

Đọc lướt là kết luận: **122 ≥ 96 ⇒ đủ mẫu**. Sự thật `122` là số dòng **hai DỰ ĐOÁN khác
nhau**; ngưỡng `96` của `QD-059` đăng ký cho **cặp lệch KẾT CỤC** (`b+c` — một bên trúng, bên
kia trượt). Con số đó là **46**. Hai bên đoán khác nhau 122 lần nhưng phần lớn **cùng trượt**,
mà cùng trượt thì không phân biệt được ai hơn ai nên **không vào mẫu** (McNemar).

Nguy hiểm không nằm ở con số 122, mà ở việc bộ chấm **in ngưỡng ngay cạnh nó** — tức **mời
người đọc so hai thứ không so được**. Họ `RM-21`: hằng số đo được chỉ đúng cho thước đã đo nó.

SAU (chạy thật trên DB production 23/08):

```
hai dự đoán KHÁC NHAU   : 122   (tiến độ thu mẫu — KHÔNG phải số phán quyết)
CẶP LỆCH KẾT CỤC (b+c)  : 46   [ngưỡng QD-059: ≥96]  ← ĐÂY mới là số so với ngưỡng
   b = 21 (control đúng · T-B sai)  ·  c = 25 (T-B đúng · control sai)
số ngày thật            : 13   [QD-017 cần: 14 ngày]
⛔ CHƯA ĐƯỢC PHÉP KẾT LUẬN (RM-04) — còn thiếu 50 cặp lệch kết cục · còn thiếu 1 ngày
```

Phép quyết định **tách thành hàm thuần** `doc_thuoc_tb()` — không phải cho gọn, mà để **thử
chặn được cả hai chiều**. Khi nó nằm lẫn trong `main()` giữa các lệnh `print`, nhánh «ĐỦ ĐIỀU
KIỆN» **không bao giờ được chạy thử** cho tới đúng cái ngày người ta cần nó chạy đúng — đó
chính là lỗi cổng đóng băng `QD-041`: **luôn báo xanh** kể từ lúc dựng, không ai biết.

Thử chặn `_v11107_thu_chan_fu427.py`: **9/9 ĐẠT** — gồm đúng biên (n=95 chặn · n=96 qua ·
13 ngày chặn · 14 ngày qua), nhồi 1.300 ô «cùng đúng/cùng sai» ⇒ `n` **không đổi**, `b=c=0` ⇒
**không nổ chia-cho-0**, 40 dòng chưa chấm (`None`) **không** bị đọc thành «trượt».

### FU-428 — HAI mệnh lệnh bảo model dùng khối KHÔNG BAO GIỜ tới tay nó

| # | dòng trong `REASONING_RULEBOOK` | khối nó trỏ vào | mồ côi từ |
|---|---|---|---|
| (a) | *«Khi Context Pack có "BT MODEL RANKING" → ưu tiên evidence từ model BT cao»* | bị de-herding **cắt vô điều kiện** (`_V10768_HERD_SECTION_KEYS`, áp ở `:6405`) | không truy được mốc |
| (b) | *«Khi Context Pack có "WEEKLY LIVINGNESS" → chỉ tin rules ACTIVE/SUPPORT»* | `V11014` ép `_live_rows = []` ngày **07/08** | **16 ngày** |

**Dump prompt production 23/08** (`RM-14` — cấm đo trên bản đọc từ tài liệu). Trước/sau
de-herding, cả ba miền: `Model Performance` 1→**0** · `BT MODEL RANKING` 1→**0** · `Riêng`
1→**0** · `Width Warning` 0→0. Cắt **1.039–1.160 ký tự** mỗi miền. `WEEKLY LIVINGNESS`
**0 trước, 0 sau** — khối không hề được dựng.

Ca (b) lộ ra **hoàn toàn tình cờ**: bộ đếm trong script đẩy bắt cả câu «Khi Context Pack có …»
nói chung chứ không riêng khoá đang gỡ. Không có nó thì mệnh lệnh đó **còn nằm im thêm bao lâu
nữa không ai biết** — đúng ca `RM-07` *«vá một lỗi không phải vá cả họ lỗi»*.

### Cổng máy cho `PRJ-PROMPT-COHERENCE-001` — vì họ lỗi này đã cắn BA LẦN

`V11001` (gan/nóng/lạnh) · `V11014` (`WEEKLY LIVINGNESS`) · `FU-428` (`BT MODEL RANKING`).
Luật ghi rõ: **một RM tái phạm hai lần ⇒ phải dựng cổng máy, không được chỉ hứa.**
`PRJ-PROMPT-COHERENCE-001` tới nay **chưa có cổng nào**.

`_v11107_cong_prompt_mo_coi.py` — dump prompt **ĐẦY ĐỦ** từ hàm đang serve, rồi soi **đúng một
khuôn**: câu **điều kiện-có-mặt** (*«Khi … có/nhận được "X"»*). Đó là khuôn **duy nhất** vỡ khi
khối `X` bị gỡ.

**Kết quả trên bản đang chạy:** `MỒ CÔI=0 · LỆCH MIỀN=1 · CÓ MẶT=5`, prompt thật
**MN 34.774 · MT 36.169 · MB 40.460** ký tự. Thử chặn **4/4**, khôi phục nguyên trạng.

**Hai lỗi của chính bản nháp cổng — ghi lại vì đây mới là phần đáng học:**

Bản nháp đầu chạy ra **«10 mệnh lệnh mồ côi»**. Con số đó **sai gấp mười lần**, và sai theo
đúng hai kiểu mà luật trong kho này đã cảnh báo:

1. **Đo thiếu nguồn** (`RM-13`). Nó chỉ dump **context pack**, trong khi prompt thật còn thân
   do `create_analysis_prompt()` dựng. Bốn khối `CHỈ SỐ ĐỊNH LƯỢNG` · `CẶP ĐÔI HAY ĐI CÙNG` ·
   `KẾT QUẢ NGÀY TRƯỚC` · `KNOWLEDGE BASE` bơm bằng `prompt +=` ở `:2253 :2706 :2720 :2895` —
   **có thật**, nhưng cổng không nhìn tới nên gọi cả bốn là mồ côi.
2. **Đếm chuỗi thô** (`RM-09` · `§60.3`). Nó nuốt luôn **giá trị mẫu trong khung JSON đầu ra**:
   `"decision": "CHOT_HA"` · `"confidence": "CAO / TRUNG BÌNH / THẤP"` ·
   `"phase": "DAO_GUONG / GIAO_TRUC / MIXED"`. Không cái nào là tên khối — chúng là thứ model
   phải **GHI RA**, không phải thứ model **ĐỌC VÀO**.

**Cổng này KHÔNG soi gì** — ghi thẳng trong docstring, vì một cổng nói mình soi nhiều hơn thực
tế thì **nguy hiểm hơn không có cổng**: nó **không** bắt được ca `V11001` (tên khối nằm trong
danh sách liệt kê **không ngoặc kép**, và few-shot là **ví dụ** chứ không phải câu điều kiện),
không bắt **nhãn hiển thị** mô tả dữ liệu đã gỡ, không bắt **hai câu bảo ngược nhau**.

### Vá thêm — `_v11062.ghi()` và cổng `K4` của chính nó dùng HAI hợp đồng khác nhau

`ghi()` nhận khối mở đầu bằng `### V11107 — …`, ghi đủ bốn mặt, in **«✓ ghi đủ BỐN mặt»** —
rồi `--kiem` của **chính tệp đó** TRƯỢT `K4`, vì `RE_MUC_V` chỉ nhận `^## V…`. **Bộ ghi nói
xong, bộ kiểm nói chưa.**

Cùng khuôn `RM-15` nhưng ngược chiều: cổng có thử, nhưng thứ **sinh ra dữ liệu cho cổng** thì
không ai buộc nó theo hợp đồng của cổng. Hậu quả nặng là ai đó thấy «✓ ghi đủ bốn mặt» rồi
**không chạy `--kiem`**, và `STATE.last_version` trôi khỏi `CHANGELOG` mà không ai biết.

Nay `ghi()` **TỪ CHỐI GHI** khi heading sai, nêu đúng dạng cần — **cấm tự sửa hộ**, vì sửa hộ
thì người viết không bao giờ học được dạng đúng. Thử chặn **7/7**: ba dấu `#` chặn · không dấu
`#` chặn · heading không có số hiệu chặn · **heading ghi sai số hiệu** (V11106 khi đang nâng
V11107) chặn · khối rỗng chặn · hai dạng đúng cho qua.

### Điều KHÔNG hứa

Gỡ hai dòng mồ côi **không phải** để tăng độ trúng, và chưa phép đo nào chứng minh chúng ảnh
hưởng độ trúng. Lý do gỡ là prompt **tự mâu thuẫn**: model được bảo *«ưu tiên evidence từ model
BT cao»* và *«chỉ tin rules ACTIVE/SUPPORT»* trong khi **không có bảng nào để đọc** ⇒ nó tự bịa
hoặc tự suy lại mệnh lệnh cũ (`§60.1`).

**Lộ ra khi dump, chưa mở mục:** ba khối `Model Performance` · `BT MODEL RANKING` · `Riêng`
**được dựng kèm truy vấn DB rồi vứt đi ở MỌI lượt gọi**, cả ba miền. Không sai kết quả — là
công vô ích mỗi lần dự đoán.

### Deploy

Hai lượt đẩy cùng tối, `_v11107_deploy_ctx187.py` (cổng thời gian đọc giờ **từ VPS**, từ chối
đẩy trong khung dự đoán): `21:02` PID `2299279 → 2317479` · `21:1x` PID `2317479 → 2320523`.
`/api/health=200`, bốn bảng khoá `+0` cả hai lượt. Dump từ hàm đang serve xác nhận
**`RR= RR-16.6`**.

## 4. Hướng xử lý và vì sao chọn

Lý do chọn nằm trong chính khối `CHANGELOG` ở mục 3 — đó là bản ghi viết **lúc làm việc**,
không phải suy lại. Phần **cân nhắc phương án bị loại** thì 🔴 **KHÔNG KHÔI PHỤC ĐƯỢC**: nó chỉ
tồn tại trong vết phiên và không được ghi vào tài liệu nào lúc đó.

## 5. Đã làm gì

| commit | ngày (giờ VN) | tệp | tổng |
|---|---|---|---|
| `8ca990d` | 2026-08-23 21:15:49 | CHANGELOG.md, docs/AUTOMATION_HISTORY.jsonl, docs/AUTOMATION_STATE.json, docs/CURRENT_TRUTH_SSOT.md, web/backend/_v11062_nang_version.py, web/backend/ | 10 files changed, 880 insertions(+), 7 deletions(-) |

## 6. Cổng kiểm

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC output cổng của phiên gốc** — cổng in ra `stdout`, không ghi tệp
(đúng khuyết tật `RM-15` mà `V11121` đã vá cho `cong_git_commit.py` bằng sổ điểm danh).

Điều **kiểm được hôm nay**, `26/08/2026`:

| phép | kết quả |
|---|---|
| commit của bản này còn trong `git log` | ✅ **1/1** còn nguyên, đều là tổ tiên của `origin/master` |
| khối `CHANGELOG` còn nguyên | ✅ 12,091 ký tự |
| bản này đã có báo cáo công khai chưa | ✅ **có, từ bản bù này** — trước đó `A55_VIOLATION_REPORT_MISSING` |

## 7. Vướng vấp

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC** vướng vấp trong phiên gốc — không tài liệu nào ghi lại lúc đó.

Vướng vấp **của chính việc bù này**, ghi trung thực: bản bù dựng từ ba nguồn đương thời nhưng
**không thay được** một báo cáo viết lúc làm việc. Cụ thể mất: giờ từng thao tác · các phương án
đã cân nhắc rồi loại · lỗi gặp giữa chừng · trạng thái trước/sau của DB nếu phiên có chạm.

## 8. Gỡ về

Bản bù này **chỉ thêm tài liệu**, không đụng mã và không đụng dữ liệu ⇒ gỡ về =
`git rm -r V11107_FU427_BO_CHAM_TB_VA_FU428_HAI_MENH_LENH_MO_COI_20260823/` rồi commit lại. Trạng thái quay về đúng như trước khi bù.

Việc gỡ về của **bản gốc `V11107`** nằm trong chính khối `CHANGELOG` ở mục 3 (nếu bản đó có ghi).

## 9. Theo dõi tiếp

| mã | việc | trạng thái |
|---|---|---|
| `FU-442` | vá cổng A55 — chính lỗ hổng làm bản này vô hình | ✅ **ĐÃ VÁ** ở `V11122`, thử chặn **11/11** |
| — | bù nốt các bản còn thiếu | trên **toàn dải từ mốc thi hành `V10921`** còn **32** bản thiếu báo cáo; 10 bản của đợt này là nhóm ưu tiên |
| — | ngưỡng đóng bằng số | `_v10921_report_gate.py` chạy **không tham số** ⇒ `V11107` không còn trong danh sách `THIẾU BÁO CÁO` |

---

## 10. BA LỚP NGUỒN (§62 · A60)

### `OWNER_SAID`
> *«PROMPT TỔNG LỰC LẦN 28 — 23/08: TRUY 9 ms + TRUY KHÂU RÚT SỐ + VÁ FU-419 LỐI (a) ═══ OWNER ĐÃ KÝ (03:44 + 03:50 23/08) — KHÔNG HỎI LẠI ═══ ① Duyệt truy tiếp CẢ HAI: con số 9 ms chưa giải thích + khâu rút số (33.685 token không cho ra số nào). ② FU-419 lối (a): dòng «D-1 cross-region tail pool» chuyển thành GHI SỐ ĐẾM, bỏ danh sách. Ghi nhận điều kiện đi kèm: CẤM hứa nó làm tăng độ trúng (FU-316 đã đo: 20,2% vs nền 21…»*
> — owner, **23/08/2026 03:53** (giờ VN)

> *«push báo cáo chưa em?»*
> — owner, **23/08/2026 04:37** (giờ VN)

> *«Phiên prompt lần 28 đã xong việc nhưng báo cáo CHƯA lên kho GitHub công khai. Đóng phiên đúng kỷ luật: nâng bốn mặt version (_v11062) → lấy số hiệu từ _v11044 → đẩy báo cáo + tài liệu lên kho công khai → chạy cổng cuối phiên → xác nhận commit đã thấy trên remote. Xong báo lại mã commit.»*
> — owner, **23/08/2026 04:46** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 29 — TỐI 23/08: ĐÁNH GIÁ DỰ ĐOÁN + XỬ LÝ TOÀN BỘ TỒN ĐỌNG LỖI + ĐỌC LANE T-B + CHUYỂN HOÁ NGỮ CẢNH ĐỢT 1 ═══ BỐI CẢNH ═══ Live 23/08 đã kết thúc. Owner yêu cầu TỔNG LỰC: đánh giá dự đoán hôm nay, xử lý toàn bộ các lỗi đã được ký duyệt (FU-421, 425, 426, dòng chị em FU-419), đọc lane T-B (đã đủ 14 ngày), và bắt đầu CHUYỂN HOÁ NGỮ CẢNH NGAY LẬP TỨC (đợt 1). Không dậm chân tại chỗ. ═══ GĐ-0 · ĐÁNH GI…»*
> — owner, **23/08/2026 19:47** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 30 — 24/08: AUDIT CỰC GẮT — KIỂM CHỨNG DỮ LIỆU + ĐO MODEL AI NGAY + RỖNG→NGUYÊN NHÂN→THAY + ML GỐC→NGỌN + CHẤM DỨT "ĐO HOÀI KHÔNG RA" ═══ BỐI CẢNH ═══ Owner chất vấn 6 điểm: ① nghi ngờ dữ liệu kết quả bị ghi đè/trôi (MN không có bạch thủ 10) ② đòi ĐO MODEL AI TỚI ĐÂU NGAY, không chờ chuyển đổi ngữ cảnh ③ so sánh shadow vs official chéo regime là SAI (1 thằng nhồi số bốc thăm, 1 thằng tự kiếm số th…»*
> — owner, **23/08/2026 20:45** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 30 — 23/08 TỐI (CHẠY NGAY): AUDIT CỰC GẮT — KIỂM CHỨNG DỮ LIỆU + ĐO MODEL AI NGAY + RỖNG→NGUYÊN NHÂN→THAY + ML GỐC→NGỌN + CHẤM DỨT "ĐO HOÀI KHÔNG RA" ═══ BỐI CẢNH ═══ Owner chất vấn 6 điểm (20:42) + đòi tổng hợp toàn bộ yêu cầu (20:32) + yêu cầu CHẠY NGAY (20:51), không chờ 05:00. PHẦN AUDIT READ-ONLY LÀM NGAY. Chỉ 2 việc gắn mốc sau (ghi rõ trong báo cáo, không chặn phần còn lại): xác minh CTX-18…»*
> — owner, **23/08/2026 22:20** (giờ VN)


### `CODE_DID`
| điều mã **thực sự** làm | bằng chứng |
|---|---|
| 1 commit mang nhãn `V11107` | `8ca990d` — còn nguyên trong `git log`, đều là tổ tiên `origin/master` |
| tệp bị đụng | xem bảng mục 5 |
| bản này **chưa từng** có báo cáo công khai cho tới hôm nay | `_v10921_report_gate.py` liệt `V11107` trong `THIẾU BÁO CÁO` trước khi bù |

### `DOC_SAID`
| tài liệu | nói gì | khớp code chưa |
|---|---|---|
| `CHANGELOG.md` khối `## V11107` | 12,091 ký tự, viết đương thời | 🟢 **khớp** — commit tồn tại đúng ngày ghi |
| kho báo cáo công khai | **không có** thư mục `V11107_*` | 🔴 **LỆCH** — đã đóng bằng bản bù này |

### 🔴 BA LỚP LỆCH NHAU
`DOC_SAID` ≠ `CODE_DID`: mã đã chạy và đã commit, `CHANGELOG` đã ghi, nhưng **kho công khai không
có gì** suốt 3 ngày. Đó là `A55_VIOLATION_REPORT_MISSING`, và nó **vô hình** vì cổng chỉ soi 8
bản gần nhất — nay đã vá (`FU-442` · `V11122`).

---

**TanPhatAI cần làm:** ghi nhận đây là **báo cáo BÙ** viết ngày 26/08/2026 cho việc làm ngày
23/08, dựng từ **ba nguồn đương thời** (CHANGELOG 12,091 ký tự ·
1 commit · vết phiên), **không** phải bản viết lúc làm việc — mọi chỗ không khôi phục
được đã ghi thẳng là `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.
