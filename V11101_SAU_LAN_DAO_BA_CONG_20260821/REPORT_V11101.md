# REPORT V11101 — SÁU LÀN ĐÀO · BA CỔNG QUẢN TRỊ · VÌ SAO CHƯA CẮT ĐƯỢC MODEL NÀO

**Ngày:** 2026-08-21 (đêm) · **Mã đọc:** `KS2108` · **Quyết định:** `QD-070`
**Production KHÔNG đổi trong phiên này** — không deploy, không restart, không đụng DB
**Verdict:** `CODE_PUSHED` + `REPORT_PUBLISHED` · **KHÔNG** phải `RUNTIME_PROVEN` (xem §6)

---

## 1. Tóm tắt

Owner mắng thẳng: *«đưa vào 1 đống model AI không tham gia total output để làm cảnh ah để đốt tiền
ah em? em quá kém cỏi đó»* — và owner **đúng ở chỗ nặng nhất**, nhưng **không đúng ở chỗ em tưởng**.

Phiên này chạy **sáu làn** song song (bốn làn chỉ-đọc + một làn vá cổng + một làn kiểm chuẩn bị).
Kết luận gọn trong một câu:

> **Vấn đề không phải «nhiều model». Vấn đề là KHÔNG CÓ CÁI THƯỚC CHUNG để biết model nào đáng
> giữ — nên không ai dám cắt, và càng không dám thay.**

Con số chứng minh, đo hôm nay:

| đo được | số |
|---|---|
| model đang góp số công bố mà **có 0 dòng** trong bảng chấm điểm | **8 / 15** |
| `claude-sonnet-4-6` — model **đương nhiệm** — số lượt được chấm | **0** |
| tổ hợp model × miền **hơn nền** (01/02→21/08, official, trong cửa sổ chốt) | **0 / 57** |
| số lần lịch sử **khen** một model, và số lần thực tế **xác nhận** lời khen đó | **11 khen · 0 xác nhận** |
| 19 model AI cùng chạy, số **câu trả lời khác nhau** trung bình mỗi ngày | **6,7** |

Nghĩa là: **đông mà loãng đúng như owner nói** — nhưng cắt bừa lúc này là cắt mù, vì
**chưa có thước** thì cắt nhầm người giỏi cũng không ai biết.

**Việc phải làm để thoát bế tắc, đã đo bằng số:** đổi thước từ *«model có hơn nền không»* sang
**«so từng cặp với chính bộ số đã công bố»**. Cùng một câu hỏi, nhưng nhanh hơn **3,3 lần** —
**66 ngày** thay vì **218 ngày**. Và **hai model đã đủ mẫu để quyết DỪNG ngay 27/08**.

Song song: **ba cổng quản trị** đã được vá vì cả ba **đang báo xanh sai**, và một trong ba
lôi ra được **một quyết định của owner bị mất khỏi sổ 5 ngày** — nội dung của nó chính là điều
owner mắng tối nay.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«Chi phí ở đây không phải là model đắt tiền đong đếm bằng tiền. Chị phí chạy quá nhiều model
> ai lãng phí mà trong khi đó không đo được sức mạnh của model, model nào đáng dùng không đáng
> dùng, đắt cũng được nhưng phải chất lượng, phù hợp với dự án, phù hợp với ngữ cảnh, prompt phải
> tối ưu thuần ngữ cảnh nhồi toàn số đã lọc sẵn vào thì model ai đâu hoạt động đúng nghĩa của nó
> em. Đắt phải chất, ít nhưng hiệu quả đông loãng, nhiều thì không nên. Showdow là thử nghiệm để
> so sánh và tìm ra model phù hợp để thay thế các model hiện tại giá trị nó chỗ đó nó chưa tham
> gia output là đúng mà em, em phải làm việc này so sánh tìm ra ứng viên sáng giá chứ em..»*

> *«Em làm việc có vẻ cẩu thả và dư thừa, em có biết là anh đã yêu cầu em lên kế hoạch chuyển đổi
> các thông số đang tiêm vào prompt thành ngữ cảnh kèm các điều kiện phù hợp tương thích miền thứ
> biết bao nhiêu lần không hả? ML là ML là một model cơ chết số học hoàn toàn, LLM là LLM nó hoạt
> động với các ngủ cảnh điều kiện để truy vết, sàn lọc, chọn lọc, khoanh vùng để xác định được số
> tốt nhất đưa ra output tốt nhất… Showdow, lane test nhiệm vụ của nó là để thử nghiệm để so sánh
> để phân biệt được cái nào tốt sấu, hơn thua để áp dụng cho offical, final mà giờ nói là không có
> giá trị sao em làm việc có vẻ kém thông minh quá vậy em? Anh tin chắc trong các audit báo cáo
> trong root có rất nhiều điều cần em phải kiểm tra, rà soát lại rồi đó em nên tìm hiểu, xem lại
> hết đi trong lịch sử, hisory, báo cáo, changlog v.v… còn rất nhiều thông tin quý giá đó. EM nghỉ
> anh rảnh lắm đưa vào 1 đống model AI không tham gia total output để làm cảnh ah để đốt tiền ah
> em? em quá kém cỏi đó. Tiếp tục đào sâu tìm hiểu nữa đi sau đó tổng hợp báo cáo tổng lực đầy đủ
> chi tiết nhất cho anh.»*

Và trong **PROMPT TỔNG LỰC LẦN 24**, owner khoá cách làm:

> *«Cổng `_v11044`: chỉ CẤP SỐ không ĐỐI CHIẾU — thêm đối chiếu nhãn QD trong báo cáo với sổ
> (học từ vụ QD-068 ma: 4 ngày báo cáo tag quyết định không tồn tại). Cổng `>/dev/null` che
> stderr: tái phạm 3 lần, đã quá ngưỡng §61 ⇒ dựng cổng máy. MỌI CỔNG: thử chặn HAI CHIỀU
> bắt buộc. Mỗi cổng một commit riêng.»*

---

## 3. Đào bới / phát hiện

### 3.1 · Owner đúng — nhưng «đông loãng» nằm ở chỗ khác chỗ em từng chỉ

Em từng báo *«19 model AI chỉ đẻ ra 6,7 câu trả lời khác nhau»* và coi đó là kết luận. Đào tiếp
hôm nay thì thấy **đó mới là triệu chứng**, gốc bệnh nằm ở chỗ khác:

**Bảng chấm điểm để so model VỚI NHAU đang sống, đủ cột, chạy từ 24/04 tới hôm nay — nhưng nó
chỉ chấm model shadow.**

```
shadow_model_promotion_scorecard_daily     4.167 dòng · 24/04 → 21/08 · CÓ SẴN hai cột b/c
   nhưng writer lọc  run_source='shadow_auto_eval'
   ⇒ 8 / 15 model đang GÓP SỐ CÔNG BỐ có ĐÚNG 0 dòng
   ⇒ claude-sonnet-4-6 (đương nhiệm) : n = 0
```

Nghĩa là hôm nay, nếu owner hỏi *«`claude-sonnet-4-6` mạnh hay yếu?»* thì **không ai trả lời
được**, kể cả bằng dữ liệu 6 tháng. **Đó mới là chỗ loãng thật.** Không phải tiền, không phải
số lượng model — mà là **chạy 6 tháng mà vẫn không biết ai đang gánh, ai đang ăn theo**.

### 3.2 · Và thước cũ thì gần như không bao giờ kết luận nổi

Đo lại nền đúng cho từng miền (`RM-18` — nền phải đúng cho từng vế):

```
nền 1 số:   MB 23,8%      MT 35,1%      MN 43,1%
```

Đối chiếu **toàn bộ** model × miền trên `predictions`, đường official, **trong cửa sổ chốt**,
01/02 → 21/08:

| phép | kết quả |
|---|---|
| số tổ hợp `z ≥ +1,96` | **0 / 57** |
| sau hiệu chỉnh Bonferroni (`|z| ≥ 3,327`) | **0**, cả hai chiều |
| cao nhất toàn bảng | `deepseek-reasoner`/MT **+7,53pp**, `z = +1,91` — **chưa đủ** |

Và sức mạnh mẫu cho biết vì sao mãi không xong: chứng minh **+5pp** ở MT cần **729 ngày**; săn
**+3pp** cần **67 tháng**. Tức **thước cũ là một cái thước không bao giờ đọc được số**.

### 3.3 · Lịch sử: 11 lần khen, 0 lần thực tế xác nhận

Đây là phần owner bảo *«trong lịch sử, history, báo cáo, changelog còn rất nhiều thông tin quý
giá»* — đúng, và nó không dễ nghe:

| model/miền | khen bằng gì | TRƯỚC khi khen | SAU khi khen |
|---|---|---|---|
| `combo-no-token`/MT | V10947 *«+5,07pp z=2,81»* | +3,01 (z+0,57) | **+0,65 (z+0,06)** |
| `random-forest`/MT | V10952 *«tín hiệu tốt nhất toàn hệ»* | +1,48 (z+0,28) | **+5,65 (z+0,54)** |
| `xgboost`/MT | V10947 z=1,88 | +4,01 (z+0,75) | **+0,65 (z+0,06)** |
| `smart-ensemble`/MT | V10947 z=1,68 | +3,44 (z+0,65) | **−4,35 (z−0,41)** đổi dấu |
| `gemini-2.5-pro`/MN | V10947 *«cao nhất»* | +5,37 (z+1,35) | **−12,65 (z−1,15)** đổi dấu |
| lane `MB_PRIOR_REGION` | *«34% vs 21%, p=0.01»* | — | **−17,98 (z−0,73)** |

**11 lần khen · 0 lần được thực tế xác nhận.** Không tổ hợp nào chạm `|z| ≥ 1,96` ở cột SAU.

Nặng hơn: con số **`z = 2,81`** của báo cáo V10947 **không tái lập được** — nó dùng nền **16,49%**
cho MT trong khi nền thật là **35,12%**. Và nó **chưa bao giờ được rút lại ở chỗ đã công bố**
⇒ đúng ca `PRJ_RETRACTION_SILENT`. **Bản này rút lại — xem §3.6.**

### 3.4 · Lần «rữa» thứ BẢY đã xảy ra, và không ai đọc

Luật GĐB-đảo (V10816) **đã ký sẵn ngưỡng trước**: *«≤28% ⇒ đóng, đọc ngày 16/08»*.
Đo forward 30 ngày: **16,7%** so với nền **23,3%**. **Phải đóng từ 16/08 — nay quá hạn 5 ngày.**

Đây là lần thứ **bảy** một cơ chế được bật rồi rữa (V10655→V10672→V10677→V10753→V10789→V10790→
GĐB-đảo). Bài học đã ghi trong `CLAUDE.md` từ lâu — *«đừng bật lại bằng backtest, chỉ bằng đo
tiến»* — và nó vẫn xảy ra lần thứ bảy vì **không có ai đọc cái ngưỡng đã ký**.

### 3.5 · Prompt: chỗ nhồi nặng nhất KHÔNG phải chỗ em từng chỉ

Owner nói *«prompt phải tối ưu thuần ngữ cảnh, nhồi toàn số đã lọc sẵn vào thì model AI đâu hoạt
động đúng nghĩa»*. Kiểm kê **32 khối** trong gói ngữ cảnh:

**GIỮ 7 · DỊCH SANG NGỮ CẢNH 7 · BỎ 15 · để nguyên 3.**

Ba phát hiện đổi kết luận:

**① Ba khối đầu gói ngữ cảnh KHÔNG TỚI TAY MODEL NÀO.** `_V10768_DEHERD_PROMPT_ENABLED = True`
(`gpt_analyzer.py:4331`) cắt `Model Performance` + `BT MODEL RANKING` + `Riêng <thứ>` **ngay sau
khi dựng** — 1.125/1.092/1.041 ký tự bị vứt mỗi lượt, 567 lượt/tuần.

**② Khối đáng bỏ nhất là `MB MODEL RANKING`** (1.564 ký tự = **12% gói MB**). Trong 35 model nó
liệt kê, **11/35 (31%) đã rời danh bạ**. Prompt vẫn đang dạy model:

> *«MB Thứ Bảy TRUST: `deepseek-v4-flash` → output giống thì tăng confidence»*

— model đó **ngừng dự đoán MB từ 04/07/2026, 48 ngày trước**. Đây là **lệnh bầy đàn thuần tuý**,
lọt lưới de-herding chỉ vì tiêu đề thụt lề 2 dấu cách thay vì `### `.

**③ Khối `D-1 tail pool` hỏng theo kiểu im lặng.** `sorted(d1_union)[:12]` → 31 ngày **chỉ hiện
đuôi 00–21**; **78/100 đuôi chưa bao giờ xuất hiện**, trong khi kho thật trung bình **70,8 đuôi**.

**Và chỗ nặng nhất thì chưa dump được:** `create_analysis_prompt` (≈**18.200 ký tự**,
`:2042–2977`) — **de-herding không chạm tới nó**, và ở đó còn nguyên `🏆 HIỆU SUẤT THEO MODEL` kết
bằng *«AI nên ưu tiên patterns từ models có win_rate cao hơn»*. **Ghi thẳng: chưa kiểm được lớp
này**, không đoán.

### 3.6 · RÚT LẠI (theo `PRJ-RETRACTION-001` — đủ bốn phần)

**Rút lại #1 — con số của chính phiên hôm nay:**

| phần | nội dung |
|---|---|
| **chỗ gốc** | `docs/UNG_VIEN_MODEL_VA_CHAT_LUONG_PROMPT_20260821.md`, công bố 21/08 chiều |
| **nguyên văn câu sai** | *«MN 15% / MT 13% / MB 32% ký tự trong prompt là thống kê hiệu suất model»* |
| **điều đúng** | Ba con số đó đo trên gói **THÔ**. Trên gói **model thật sự đọc** (sau khi de-herding cắt 3 khối đầu) chỉ còn **5,8% / 4,6% / 26,5%**. Tái lập: `docs/BAN_DO_NGU_CANH_PROMPT_20260821.md` §2, script trong scratchpad |
| **đã dựa vào đâu** | Chưa quyết định nào dựa trên nó — nó mới ra chiều nay. Nhưng nếu để nguyên, nó sẽ làm việc dọn prompt **nhắm sai cả ba miền**: sự thật là vấn đề **gần như trọn ở MB** |

**Rút lại #2 — con số cũ, nặng hơn:**

| phần | nội dung |
|---|---|
| **chỗ gốc** | `REPORT_V10947`, mục xếp hạng model |
| **nguyên văn câu sai** | *«`combo-no-token`/MT +5,07pp, z = 2,81»* |
| **điều đúng** | Nền dùng để tính là **16,49%**; nền thật của MT là **35,12%**. Tính lại: **+3,01pp, z = +0,57** — **không hơn nền**. Sau ngày khen: **+0,65pp, z = +0,06** |
| **đã dựa vào đâu** | Đây là **một trong bốn con số** đưa `combo-no-token` vào nhóm được tin; model này về sau **vẫn nằm trong danh sách cứng** của `main.py` cho tới khi `FU-380` gỡ ra hôm nay |

---

## 4. Hướng xử lý và vì sao chọn

### 4.1 · Đổi thước — và vì sao thước mới nhanh hơn 3,3 lần

**Thước cũ:** *«model X có hơn NỀN không?»* → nhiễu theo ngày rất lớn (hôm nay dễ, mai khó), nên
phải chờ rất lâu mới tách được tín hiệu.

**Thước mới:** *«cùng một ngày, cùng một miền, cùng ngữ cảnh — model X đúng khi bản ĐANG CÔNG BỐ
sai bao nhiêu lần (b), và ngược lại bao nhiêu lần (c)?»* → điểm = `(b − c) / n`.

Nhiễu chung của ngày bị **khử ngay trong phép trừ**, không cần hiệu chỉnh gì thêm. Đo được:
**68% nhiễu chung biến mất**, cần ít mẫu hơn **2,9×**, và góp dữ liệu nhanh hơn **2,3×**.

|  | thước cũ | thước mới |
|---|---|---|
| ngày cần để kết luận | **218** (27/03/2027) | **66** (27/10/2026) |

Đây cũng **đúng hình dạng câu hỏi owner đang hỏi**: không phải *«model này giỏi không»* mà
*«có nên đổi người không»*.

### 4.2 · Ai đã đủ mẫu, ai chưa — nói thẳng ngày

| model | n đo cặp | đủ để **DỪNG** | đủ để **THĂNG** |
|---|---|---|---|
| `gpt-5.5` | 273 | **ĐỦ — quyết 27/08** | 24/10 |
| `qwen3-max-thinking` | 273 | **ĐỦ — quyết 27/08** | 21/10 |
| `gemini-3.5-flash` | 139 | 29/09 | **27/10** |
| `qwen3.7-max` | 144 | 17/10 | 12/11 |
| `claude-sonnet-4-6` **(đương nhiệm)** | **0** | — | **không bao giờ — chưa có thước** |

Hai cột lệch nhau **có chủ ý**: *dừng* được dùng dữ liệu đã tích (sai thì cho vào lại, rẻ);
*thăng* phải **đếm lại từ 0 kể từ 22/08**, vì bảng 90 ngày **đã bị nhìn thấy** — lấy nó phong chức
là chọn cái cao nhất trong 15 con số nhiễu.

### 4.3 · Vì sao KHÔNG cắt gì trong phiên này

Owner ra lệnh rõ: *«Phiên này CHỈ kiểm kê (read-only) — CẤM cắt bất cứ thứ gì»*. Em giữ đúng.
Nhưng ngoài mệnh lệnh, còn một lý do kỹ thuật **em phải nói ra**:

**Cắt bây giờ là cắt mù.** `claude-sonnet-4-6` có **n = 0**. Nếu hôm nay cắt một model bất kỳ,
sáu tháng nữa không ai chứng minh được là cắt đúng hay cắt nhầm — **vì cùng một lý do đã làm
11 lời khen trước đây thành vô nghĩa**.

**Thứ tự đúng là: dựng thước → chạy 1 tuần → mới cắt.** Ba việc phải sửa để có thước (đề xuất,
**chưa làm**, chờ owner duyệt):

1. Mở writer chấm điểm cho **15 model output** (`_materialize_shadow_promotion_scorecard.py:223–231`
   đang lọc `run_source='shadow_auto_eval'`)
2. Thêm chặn lượt trễ — chỗ đó **không có** điều kiện `created_at`, nên **1–12%** lượt chạy **sau
   mốc chốt** vẫn vào sổ (`PRJ_WINDOW_LEAK`)
3. Dựng bảng cộng dồn để không phải quét lại 6 tháng mỗi lần hỏi

### 4.4 · Shadow — em đã nói sai, và đây là chỗ sửa

Em từng viết shadow *«không tham gia output»* theo giọng **chê**. Owner sửa: *«nó chưa tham gia
output là đúng mà em, em phải làm việc này so sánh tìm ra ứng viên sáng giá chứ em»*.

**Owner đúng, và cấu trúc hệ thống cho thấy owner đúng:** bảng chấm điểm shadow là **thứ duy nhất
trong toàn kho** đã có sẵn hai cột `b`/`c` — tức **đúng cái thước** phần 4.1 cần. Shadow không
phải hàng thừa; nó là **phòng thí nghiệm**, và cái hỏng là **chưa ai mang thước từ phòng thí
nghiệm ra đo người đang thi đấu**.

---

## 5. Đã làm gì

### 5.1 · Ba cổng quản trị — mỗi cổng một commit, mỗi cổng thử chặn hai chiều

| cổng | TRƯỚC | SAU | bắt được gì |
|---|---|---|---|
| `_v11034` chéo quyết định | chỉ so **cùng chủ đề** ⇒ báo `SẠCH` | thêm **phép 3 theo TRỤC**, chạy **mọi cặp** | **3 va chạm thật** quanh `QD-066` |
| `_v11044` số hiệu | chỉ **cấp số** | thêm **đối chiếu nhãn QD × sổ**, 173 báo cáo | **`QD-067` mất khỏi sổ 5 ngày** |
| *(mới)* `_v11101` che stderr | không ai canh, tái phạm 3 lần | cổng máy, phân loại 4 mức | **4 chỗ thật** đang canh |

**Cổng 1 — và điều nó lôi ra.** `QD-021` (04/08) ký *«tới cuối cùng **10/08 phải xong**»*.
`QD-066` (12/08) ký *«tạm thời để nguyên… **để lâu cho rõ, cấm clear vội**»* — và vế (2) của nó là
**nguyên tắc dùng TỪ NAY**, không bó trong hai mục nó nêu tên. Tức một nguyên tắc ra sau đã **lặng
lẽ vô hiệu hoá** một hạn chót tuyệt đối, **mà không mục nào bị đánh dấu thay thế**.

**Hậu quả đo được: 102 mục quá hạn**, cụm nặng nhất đúng **06/08–09/08** — đúng nhóm `QD-021` ấn
hạn 10/08. → **`FU-420`, owner quyết sáng 22/08.**

**Cổng 2 — và nó bắt em ngay trong lúc em dựng nó.** Bản vá đầu lấy tập «đã khai» từ hàm quét
**sáu nơi**; gỡ một mã khỏi **sổ** thì nó vẫn thấy ở `CHANGELOG` ⇒ cổng **không bao giờ đỏ được**.
Bài thử chặn bước [2] TRƯỢT ⇒ phát hiện ⇒ đổi sang đọc **thẳng sổ quyết định**.
**Nếu chỉ chạy xuôi và thấy màu xanh thì đã giao một cổng mù.**

Sau khi sửa, nó bắt ngay một ca thật: báo cáo `V11076` (16/08) và `AUTOMATION_HISTORY:290` đều gắn
nhãn **`QD-067`**, còn **sổ quyết định không có mục nào**. Nội dung quyết định đó, nguyên văn
owner **16/08**:

> *«…tóm lại nên xem **chuyển hoá thuần ngữ cảnh cho model** để model AI **tự phân tích theo năng
> lực** thay vì **nhồi nhét** vào nha em. nhồi cái đúng ko nói, nhồi cái sai, nhồi cái quá sai bầy
> đàn thôi bó tay luôn đó em»*

**Đây chính là điều owner mắng tối 21/08** — *«anh đã yêu cầu em… biết bao nhiêu lần không hả?»*.
Một trong những lần đó là **16/08**, và nó **rơi khỏi sổ** nên **không ai theo**. Đã **khai bù**,
ghi thẳng là bù (`khai_bu = true` · `khai_bu_ngay = 2026-08-21` · `ngay = 2026-08-16`), nguyên văn
**chép từ báo cáo công khai 16/08**, không diễn giải lại, **không đóng dấu như thể ghi lúc xảy ra**
(`RM-17`).

**Cổng 3 — và hai lần nó tự bắt mình sai.** Ca gốc, `CHANGELOG` dòng ~1893, ngày 11/08:

```
journalctl --since "today 00:00" 2>/dev/null   ⇒      0 dòng   ⇒ đọc thành «SẠCH»
journalctl --since today                       ⇒  3.513 dòng
```

`journalctl` **có kêu** `Failed to parse timestamp`, nhưng `2>/dev/null` **nuốt mất tiếng kêu**.
Cấp giấy chứng nhận sạch cho một **tập rỗng**.

Cổng **không cấm** `2>/dev/null` — cấm sạch là vô lý. Nó chặn **đúng một khuôn**:
*che stderr của một **công cụ bằng chứng** **và** lấy chính kết quả đó làm **phán quyết***.
Phân loại thay vì đếm chuỗi thô (`RM-09` · `§60.3`), đo được trên bề mặt sống:

```
457 chỗ che stderr  ⇒  NGUY_HIỂM 6 · CẦN_XEM 29 · AN_TOÀN 405 · CHÚ_THÍCH 17
```

**Hai lần cổng tự làm mình mù trong lúc dựng — ghi lại vì đây là lỗi dễ tái phạm:**

1. Bộ dò docstring bản đầu coi **mọi** khối ba nháy là chú thích. Kho này dùng rất nhiều khuôn
   `SH = r"""…shell…"""` — ba nháy nhưng bên trong là **mã shell thật**. `CHÚ_THÍCH` nhảy
   **5 → 194**: cổng **nuốt mất 189 chỗ**, đúng thứ nó sinh ra để chống.
2. Bản thứ hai dùng **một biến** nên bỏ sót **docstring lồng trong tải trọng**: `_v10978` bọc cả
   thân chương trình trong `REMOTE_SRC = r'''…'''`. Sửa bằng **ngăn xếp**.

**Đã vá 4 chỗ thật** (`_v10978:211,214` · `_v10980:103,104,115` · `_v10990:24`) — tất cả đều là
`journalctl … 2>/dev/null | grep -c Traceback`, tức **hỏng thành 0 ⇒ đọc thành «không có lỗi»**.
Cách vá: bỏ che stderr, thêm `sh_bc()` trả **hẳn** chuỗi `KHONG_DO_DUOC` khi stderr có chữ.
**Không** dùng mã thoát làm dấu hiệu — `grep -c` trả 1 khi đếm được 0, đó là **0 hợp lệ**.

### 5.2 · Bốn làn đọc — bốn tài liệu, không đụng gì

| làn | tài liệu | kích thước |
|---|---|---|
| GĐ-1 bản đồ ngữ cảnh prompt | `docs/BAN_DO_NGU_CANH_PROMPT_20260821.md` | 64 KB |
| GĐ-2 khung đo sức mạnh model | `docs/KHUNG_DO_SUC_MANH_MODEL_20260821.md` | 545 dòng |
| GĐ-3 đào sâu lịch sử | `docs/DAO_SAU_LICH_SU_20260821.md` | 17 phát hiện |
| GĐ-6 chuẩn bị duyệt gộp 22/08 | `docs/DUYET_GOP_2208.md` | 267 → **464 dòng**, 0 xoá |

**DB không đổi:** 741.208.064 byte trước = sau, khớp manifest 19:00.

### 5.3 · GĐ-6: bốn thứ tưởng hỏng, kiểm ra khác hẳn

| tưởng | thật |
|---|---|
| bộ chấm lane T-B đang chạy | **chưa lên VPS**: không có tệp, không có cron. Lane **vẫn thu đủ mỗi ngày** (3 cron) nhưng **không ai chấm** |
| `system_alerts` chết | im vì **không có lỗi để báo** (log 20/08: `Row count OK: 21/21`). Nhưng theo `RM-20` nó **là bảng chết**: chỉ 2 điểm đọc, **không frontend nào gọi** |
| `pnl_daily_*` chết | im vì **không ai bấm nút** từ 20/05 — nhưng **UI vẫn đọc thật** ⇒ **không** phải bảng chết |
| `QD-015/016/017` quá hạn 13 ngày | **sai gốc**: cả ba mang `ngay_khoi_dong = 2026-08-21` do `QD-045` (owner ký 08/08 *«Dời lịch để đo chứ em»*) đã dời mốc. **Hôm nay là đúng ngày.** Con số 13 chính là độ dời owner đã duyệt |

**Khoảng trống thật của D2:** chỗ áp boost (`main.py:7876/8083/8336`, `combo_super.py:1938`) **chỉ
`print`, không một câu `INSERT`** ⇒ **không bảng nào ghi boost đã áp cho số nào** ⇒ **không đo được
hiệu ứng của chính việc lật `soft → shadow`**.

---

## 6. Cổng kiểm

| cổng | lệnh | kết quả |
|---|---|---|
| chéo quyết định | `_v11034_kiem_cheo_quyet_dinh.py` | `KIEM_CHEO_QD=SACH` |
| chéo quyết định — thử chặn | `--thu-chan` | **ĐẠT 3 chiều**, sổ **khớp từng byte** (219.789 byte trước = sau) |
| số hiệu + nhãn QD | `_v11044_cong_so_hieu.py` | `SO_HIEU_V11044=KHOP` |
| số hiệu — thử chặn | `--thu-chan` | [1] thoát 0 · [2] thoát 1 · [3] thoát 0 — **ĐẠT**, sổ khớp từng byte |
| che stderr | `_v11101_cong_che_stderr.py` | `CHE_STDERR_V11101=SẠCH` |
| che stderr — thử chặn | `--thu-chan` | [1] 0 · [2] 1 · [3] 0 — **`THU_CHAN_V11101=ĐẠT`**, tệp tạm đã xoá |
| bốn mặt version | `_v11062_nang_version.py --kiem` | `NANG_VERSION_V11062=ĐẠT` |
| ghi tệp an toàn | `_v11019_cong_ghi_an_toan.py --moi` | ✓ không tệp nào thêm chỗ ghi không đóng tay |
| sổ quyết định × code | `_v10920_decision_ledger.py` | trôi **2 → 0** |

**Tài liệu dài ra, không tệp nào ngắn đi:** `CHANGELOG` +3.130 byte · `SSOT` +1.000 byte ·
`FOLLOW_UP_TRACKER` +1.857 byte · sổ quyết định **70 → 72 mục**.

**Vì sao verdict KHÔNG phải `RUNTIME_PROVEN`:** phiên này **không deploy**. Bản `CTX-18.4` đã nằm
trên VPS từ deploy tối qua (md5 `c6618121…` **khớp từng byte** với local, PID `2110106`), nhưng
**lượt production gần nhất là 17:48**, tức **trước** deploy — nên trace vẫn ghi `CTX-18.3`.
**Phép kiểm thật là lượt 05:00 ngày mai phải đóng dấu `CTX-18.4`.** Chưa chạy thì **chưa được kết
luận** (`RM-16`: mốc theo **giờ tạo từng bản ghi**, không theo ngày).

---

## 7. Vướng vấp

1. **Commit đầu của GĐ-5b nuốt mất 5 tệp.** Lần bị cổng `§63` chặn trước đó đã **xoá sạch phần đã
   `git add`**, nên commit landed với **đúng 4 tệp nâng version** trong khi thông điệp mô tả cả
   phần vá cổng. Đã `--amend` (chưa push) cho khớp lại. **Bài học: sau mỗi lần cổng chặn, phải
   `git add` lại — đừng cho rằng index còn nguyên.**

2. **Cổng ghi tệp an toàn chặn chính bài thử chặn của em.** `_v11044 --thu-chan` sửa rồi khôi phục
   **sổ quyết định thật** bằng `open(...,'w').write(...)` — đúng khuôn đã cắt cụt hai tệp 900 KB
   ngày 31/07. Đã đổi sang `tmp → flush → fsync → replace → đọc lại so`. **Cổng đó làm đúng việc**:
   tiến trình chết giữa bài thử thì sổ nằm lại ở trạng thái **cụt**, mà bài thử vốn sinh ra để
   **bảo vệ** sổ.

3. **Hai lần bộ dò docstring của cổng mới tự làm mình mù** — đã ghi ở §5.1. Cả hai lần đều bị bắt
   vì **soi lại con số bất thường** (`CHÚ_THÍCH` nhảy 5 → 194) thay vì tin màu xanh.

4. **`python - <<'PY'` in tiếng Việt lỗi mã hoá console** làm một lệnh ghi thành công nhưng báo
   `UnicodeEncodeError` ở dòng `print`. Đúng bẫy đã ghi trong `CLAUDE.md`; đã kiểm lại kết quả ghi
   bằng `grep` thay vì tin thông báo.

5. **Đếm nhầm hai lần trước khi ra số đúng** ở phần phân loại `/dev/null`: 12 → 6 → 8 → 6. Mỗi lần
   đều do **phân loại**, không do đếm — và đó chính là lý do `RM-09` cấm đếm chuỗi thô.

---

## 8. Gỡ về

| việc | lệnh gỡ |
|---|---|
| ba cổng + bản vá | `git revert <sha>` — **không** chạm production, **không** deploy, **không** đụng DB |
| bản vá 4 chỗ che stderr | `backups/_v10978_audit_probe.py.pre_v11101` · `_v10980_…` · `_v10990_…` |
| sổ quyết định | `backups/OWNER_DECISION_LEDGER.json.pre_qd067` |
| bốn mặt version | gỡ dòng `V11101` khỏi `HISTORY`, hạ `STATE.last_version` về `V11100`, và **prepend** khối đính chính vào `CHANGELOG` — **cấm** mở `"w"` |

**Không có gì cần gỡ trên VPS** — phiên này không deploy.

---

## 9. Theo dõi tiếp

| mã | việc | hạn |
|---|---|---|
| **`FU-420`** · `QD2208` | owner quyết: `QD-066` **thay** `QD-021/027/065` (⇒ 102 mục quá hạn là **hợp lệ**) hay **chỉ áp cho việc dọn sổ** (⇒ 102 mục kia **thật sự đang trễ**) | **22/08** |
| **`FU-421`** · `SC2408` | ba chỗ còn phụ thuộc ngầm vào thứ tự khi điểm bằng nhau — vá **cả ba cùng lúc**, cấm vá lẻ | 24/08 |
| `FU-419` · `HT2108-3` | khối `D-1 tail pool` chỉ hiện đuôi 00–21 | 23/08 |
| `FU-404` | **kiểm `CTX-18.4` trên lượt 05:00 ngày 22/08** — chưa chạy thì chưa kết luận | 22/08 |
| *(chờ duyệt)* | ba sửa chữa để **có thước**: mở writer 15 model · chặn lượt trễ · bảng cộng dồn | 27/08 |
| *(chờ duyệt)* | đóng luật **GĐB-đảo** — ngưỡng đã ký, đã chạm, **quá hạn 5 ngày** | 22/08 |
| *(chờ duyệt)* | sửa nhãn **vòng tròn** ở bảng chấm điểm promote (`if main_hit: return "PROMOTION_CANDIDATE"`) | 27/08 |

**Ngày quyết định gần nhất — 27/08:** ký khung đo, chọn **một** ứng viên, quyết **hai** model đã đủ
mẫu để dừng (`gpt-5.5` · `qwen3-max-thinking`), duyệt ba sửa chữa.
**Không** quyết được `gemini-3.5-flash` hôm đó — tới 27/08 nó mới có ~157 trên 198 lượt cần.

---

## §62 (A60) — BA LỚP NGUỒN

### `OWNER_SAID` — nguyên văn, kèm giờ

| giờ | nguyên văn |
|---|---|
| **21/08 ~20:15** | *«① Vá `FU-416` NGAY phiên này — một dòng… ② Dọn dẹp app theo kiểu: KIỂM KÊ CÓ BẰNG CHỨNG → owner duyệt một lượt → MỚI CẮT. Phiên này CHỈ kiểm kê (read-only) — CẤM cắt bất cứ thứ gì»* |
| **21/08 tối** | *«Chi phí ở đây không phải là model đắt tiền đong đếm bằng tiền… prompt phải tối ưu thuần ngữ cảnh nhồi toàn số đã lọc sẵn vào thì model ai đâu hoạt động đúng nghĩa của nó em. Đắt phải chất, ít nhưng hiệu quả đông loãng, nhiều thì không nên»* |
| **21/08 tối** | *«Showdow là thử nghiệm để so sánh và tìm ra model phù hợp để thay thế các model hiện tại giá trị nó chỗ đó nó chưa tham gia output là đúng mà em»* |
| **21/08 tối** | *«anh đã yêu cầu em lên kế hoạch chuyển đổi các thông số đang tiêm vào prompt thành ngữ cảnh kèm các điều kiện phù hợp tương thích miền thứ biết bao nhiêu lần không hả?»* |
| **21/08 đêm** | *«Cổng `_v11044`: chỉ CẤP SỐ không ĐỐI CHIẾU… Cổng `>/dev/null` che stderr: tái phạm 3 lần… MỌI CỔNG: thử chặn HAI CHIỀU bắt buộc. Mỗi cổng một commit riêng»* |
| **16/08** *(mới tìm lại được)* | *«tóm lại nên xem chuyển hoá thuần ngữ cảnh cho model để model AI tự phân tích theo năng lực thay vì nhồi nhét vào nha em»* — **`QD-067`, bị mất khỏi sổ 5 ngày** |

### `CODE_DID` — bằng chứng

| việc | bằng chứng |
|---|---|
| ba cổng vá xong | `_v11034` `KIEM_CHEO_QD=SACH` · `_v11044` `SO_HIEU_V11044=KHOP` · `_v11101` `CHE_STDERR_V11101=SẠCH` |
| thử chặn hai chiều | cả ba cổng ĐẠT; `THU_CHAN_V11101=ĐẠT`; sổ quyết định **khớp từng byte** trước/sau |
| 4 chỗ che stderr đã vá | `_v10978:211,214` · `_v10980:103,104,115` · `_v10990:24` |
| `CTX-18.4` trên VPS | `gpt_analyzer.py:844` = `'CTX-18.4'` · md5 `c6618121d1027c9d0355b8a761e4cb52` **= local** · PID `2110106` |
| production không đổi | không deploy, không restart; DB **741.208.064 byte** trước = sau |
| sổ quyết định | 70 → **72** mục (`QD-070` + `QD-067` khai bù); trôi **2 → 0** |
| bốn mặt version | `governance_seq` → **431**, `last_version` = `V11101`, `HISTORY` +1 dòng |

### `DOC_SAID` — và ba chỗ tài liệu **lệch** với mã

| lệch | chi tiết |
|---|---|
| `docs/UNG_VIEN_MODEL_VA_CHAT_LUONG_PROMPT_20260821.md` ≠ mã | ghi `gemini-3.1-pro` hạng 7 bảng ứng viên — model đó **đã ngừng chạy từ 04/07** |
| cùng tệp ≠ mã | ghi *«~30 model đang chạy»* — đếm 7 ngày gần nhất: **27** (8 ML + 19 AI); sau khi gộp theo `FU-352` chỉ còn **25 phép thử độc lập** |
| `docs/FOLLOW_UP_TRACKER.md` ≠ sổ quyết định | vẫn ghi `FU-216` hạn 09/08, `FU-231`/`FU-226` hạn 10/08 — **chưa theo `QD-045`** đã dời mốc sang 21/08 |
| sổ quyết định ≠ sổ quyết định | `QD-066` (nguyên tắc dùng từ nay) phủ lên `QD-021`/`QD-027`/`QD-065` mà **không mục nào** mang `thay_boi` → `FU-420` |

---

**TanPhatAI cần làm:** cập nhật `docs/OWNER_DECISION_LEDGER.json` (đã có `QD-067` khai bù ngày 16/08 và `QD-070` ngày 21/08 — đọc trường `khai_bu` để biết mục nào ghi sau), `docs/FOLLOW_UP_TRACKER.md` (`FU-420` hạn 22/08 chờ owner quyết, `FU-421` hạn 24/08), và `docs/DUYET_GOP_2208.md` (464 dòng, dùng cho phiên duyệt gộp sáng 22/08); theo dõi ba việc: ① owner quyết `FU-420` vì nó quyết luôn 102 mục quá hạn là hợp lệ hay đang trễ, ② lượt 05:00 ngày 22/08 phải đóng dấu `CTX-18.4` — chưa chạy thì chưa kết luận, ③ ngày 27/08 là mốc ký khung đo sức mạnh model và quyết hai model đã đủ mẫu (`gpt-5.5`, `qwen3-max-thinking`).
