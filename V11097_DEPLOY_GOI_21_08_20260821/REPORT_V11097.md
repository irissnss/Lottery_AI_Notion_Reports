# REPORT V11097 — GÓI 21/08 LÊN MÁY CHỦ · `FU-394` CẮT NHÁNH GAN · SỔ QUYẾT ĐỊNH VỀ 0 TRÔI

**Ngày:** 2026-08-21 tối · **Mã đọc:** `DP2108` · **Quyết định:** `QD-069`
**Tầng:** `RUNTIME_PROVEN` — đã deploy, đã nghiệm thu trên máy chủ.

---

## 1. Tóm tắt

| | |
|---|---|
| **deploy** | **2 lượt, 11 tệp** · PID `1633166` → `2101247` → `2103185` · `NRestarts=0` · **0 lỗi** |
| **prompt sống** | **`CTX-18.4`** — dòng luật mang `\| lợi thế +6.7%/nền (n=51)` |
| **4 bảng khoá** | `13.089 · 525 · 15.324 · 12.872` — **không đổi** |
| **sổ quyết định** | **10 phép TRÔI → 0** |
| **K3 drift** | **31 → 25** (trần 30) — deploy xử đúng phần của nó |
| **cổng** | **12/12 xanh**, gồm hai cổng mới dựng trong ngày |

**Nhưng việc quan trọng nhất của phiên tối không phải deploy — mà là cái BẮT ĐƯỢC TRƯỚC KHI
DEPLOY:** rà soát cuối chu kỳ tìm ra **một lỗi do chính phiên sáng gây ra**, đúng loại đã từng
ẩn **67 ngày**. Nếu deploy ngay sáng thì nó đã lên máy chủ.

---

## 2. Owner yêu cầu gì (nguyên văn)

> **19:0x 21/08** — *«Tới hạn rồi xong chu kỳ theo dõi, chu kỳ xổ số hôm nay rồi. Em tiến hành
> kiểm tra, rà soát tất cả chuẩn bị cho việc xử lý đi nào»*

> **20:0x 21/08** — *«deploy chứ chờ gì nữa em?»*

> *«`FU-290A` (đề xuất: không cắt vì độ trễ) ⇒ ko rõ model nào nhưng chưa cắt là đúng vì độ trễ
> do nhiều yếu tố bới quá nhiều model quá mà em»*

> *«`FU-394` (đề xuất: gỡ hẳn nhánh gan, hành vi không đổi) ⇒ cắt đi»*

> *«`FU-416` (vá một dòng) · `FU-393` (ba lối a/b/c) ⇒ chi tiết cụ thể là gì diễn giải cụ thể
> toàn là mã ngắn gọn mà bắt duyệt làm sao mà duyệt được duyệt mù ah em.»*

---

## 3. Đào bới / phát hiện

### 3.1 · Kết quả chu kỳ 21/08

| | chốt | số | | nền hôm nay |
|---|---|---|---|---|
| MN | 05:20 | `74` | ❌ trật | 43% |
| MT | 16:48 | `69` | ❌ trật | 32% |
| MB | 17:34 | `22` | ❌ trật | 26% |

**0/3.** Kỳ vọng từ nền là **1,01/3** ⇒ một ngày **không nói được gì** (`RM-04`).

**Thước chính, 525 miền-ngày** *(báo đủ bộ cửa sổ — `PRJ-SELECTION-WINDOW-001`)*:

| cửa sổ | bạch thủ | nền | lợi thế | z |
|---|---|---|---|---|
| 30 ngày | 35,5% | 33,6% | **+1,85pp** | +0,38 |
| 60 ngày | 29,0% | 33,7% | **−4,79pp** | −1,37 |
| 90 ngày | 30,4% | 33,9% | **−3,49pp** | −1,22 |
| 163 ngày | 33,9% | 33,9% | **+0,01pp** | +0,00 |
| **tất cả (525)** | **34,5%** | **34,0%** | **+0,52pp** · CI95 [−3,5 … +4,6] | **+0,25** |

⇒ **không tách được khỏi nền**, và **dấu đổi theo cửa sổ** — nên trích riêng bất kỳ cửa sổ nào
là kể chuyện theo cửa sổ mình chọn.

**Lane T-B** sau chu kỳ: 155 chấm · **111 cặp bất đồng ✓** (ngưỡng 96) nhưng chỉ **43 cặp phân
biệt**, `z=+0,457` ⇒ **chưa được phép kết luận**. Đáng chú ý: 43 cặp **đã đủ sức thấy chênh
65/35** — và nó thấy **53,5%**.

### 3.2 · 🔴 LỖI DO PHIÊN SÁNG GÂY RA — bắt được trước khi deploy

Sổ quyết định báo **10 phép TRÔI**. Truy ra thì trong đó có một lỗi thật:

`V11094` (`FU-404`) thêm `lift_365` vào câu `SELECT` ⇒ **12 cột**. Sửa **một** chỗ mở gói nhưng
**bỏ quên chỗ thứ hai** trong nhánh `shadow_mode=True` (`gpt_analyzer.py:4802`) ⇒
`ValueError: too many values to unpack (expected 11)`.

**Hậu quả:** `build_context_pack(shadow_mode=True)` tụt còn **106 ký tự** thay vì ~11.000, ở
**cả ba miền**.

> **Đây là `FU-341`/`QD-042` lặp lại y hệt.** Lần trước: `SELECT` 11 cột, chỗ mở gói còn 10 ⇒
> **vỡ 67 NGÀY**. Lần này `11→12`, **cách nhau 13 ngày**.

**Vì sao nó độc:** **không làm sập gì cả**. Có `try/except` nên model vẫn nhận prompt, vẫn ra
số. Không lỗi, không cảnh báo. **Chỉ lộ khi đo độ dài.**

**Và chú thích cảnh báo đã nằm sẵn ngay trên dòng lỗi**, do chính `V11032` viết sau 67 ngày kia.
Nó **không cứu được** — vì người sửa xuất phát từ **câu `SELECT`**, không xuất phát từ chỗ mở
gói. Đó chính là lý do `§61` đòi **cổng máy** chứ không phải lời nhắc.

**Đã dựng cổng `_v11096_kiem_mo_goi_rules.py`** — đếm tĩnh số cột `SELECT` vs số tên ở **mọi**
vòng mở gói. Thử chặn `RM-15` **ĐẠT**. Nghiệm thu bằng cổng thật: `VA_V11032=ĐẠT 6/6`,
`shadow=True` nay **14.226 · 13.669 · 17.123** ký tự.

### 3.3 · 🔴 VPS ĐI SAU GIT 9 NGÀY

`_v10958_fu_reader.py` trên máy chủ **thiếu hẳn khối `V11065`** — 6 nhãn trạng thái thêm **12/08**
để chống mục rơi khỏi bộ đếm. **Bản vá đó chưa từng được đẩy.**

Nếu chỉ nhìn `md5` thì kết luận sẽ là *«VPS đã trôi, DỪNG»* — **dừng oan**, và bản vá tiếp tục
nằm lại. Nên bộ deploy được dạy **phân biệt hai chuyện**:

| | nghĩa là gì | phải làm gì |
|---|---|---|
| **VPS đi sau git** | bản trên VPS là **một phiên bản CŨ trong lịch sử** | **đẩy là đúng** |
| **ai đó sửa VPS** | bản trên VPS **không khớp phiên bản nào** | **dừng**, đẩy là xoá việc người khác |

Phân biệt bằng cách dò nội dung VPS với **60 commit gần nhất** của chính tệp đó. Đo được:
`_v10958` khớp bản `6c4d1504` ⇒ **đi sau**, không bị sửa.

### 3.4 · Ba báo động giả — nếu tin thì hỏng

| báo động | sự thật |
|---|---|
| `md5` lệch trên `rule_engine.py` ⇒ *«VPS đã trôi»* | VPS giữ **LF**, local **CRLF**, nội dung **giống hệt** (0 dòng khác). Kho trên VPS **trộn hai kiểu** |
| `(b) BA BẢN BA ĐƯỜNG — dấu hiệu có người sửa thẳng trên VPS` | **hai lần**, cả hai đều là **bản chưa commit của chính phiên này** |
| `QD-046`: *«1 model rớt sàn — MẤT ỨNG VIÊN»* | `gemma-4-31b` **ngừng chạy 23 ngày** và **không trong pool**. Mất một thứ đã mất rồi thì không phải mất |

> **Nguy nhất là cái đầu:** phiên sau gặp báo động giả này có thể kết luận *«cổng hay báo bậy»*
> rồi ép ghi đè — và **lần đó ghi đè lên trôi thật**.

Đây cũng là **lần thứ hai trong cùng một ngày** một model chết làm đỏ cổng canh model sống —
`FU-290A` cũng phải loại `kimi-k2.5`, **ngừng đúng cùng ngày 29/07** với `gemma-4-31b`.

### 3.5 · Sáu phép trôi vì cổng làm ĐÚNG

Sáu mục (`QD-041` `QD-042` `QD-044` `QD-045` `QD-047` `QD-048`) dò chuỗi
`DONG_BANG_QD041=CON_NGUYEN`. Cửa sổ đóng băng **hết hạn đúng hạn** ⇒ chuỗi biến mất ⇒ cả sáu
báo **TRÔI vì một THÀNH CÔNG**.

Để vậy thì sổ **đỏ vĩnh viễn**, và đỏ giả **che mất đỏ thật**. Đã sửa **cổng trước**, rồi mới
sửa sổ: sau khi cửa sổ đóng, câu hỏi đúng không còn là *«có còn khoá không»* mà là **«cửa sổ đó
đã được tôn trọng trọn vẹn chưa»** — một sự thật **lịch sử**.

Đo được: **56 commit** đụng `gpt_analyzer.py`, trong cửa sổ 08/08→20/08 có **đúng 2**, cả hai
thuộc `QD-042`/`QD-044` ⇒ **`DONG_BANG_QD041=DA_DONG_DUNG_HAN`**.

---

## 4. Hướng xử lý và vì sao chọn

**Vì sao không deploy sáng mà deploy tối.** MN chốt bundle **05:20**. Deploy giữa ngày ⇒ MN chạy
prompt **cũ**, MT/MB chạy prompt **mới** ⇒ **ngày lai** — đúng thứ nhiễu đã giết cửa sổ `FU-284`.
Deploy sau khi cả ba miền đã xổ ⇒ **22/08 là ngày sạch đầu tiên** của `CTX-18.4`.

**Và quyết định hoãn ấy đã cứu một lỗi thật** — bản sáng nay **mang lỗi `shadow_mode`**.

**Vì sao `FU-394` cắt mà không sửa.** Vá lỗi tra tầng = **kích hoạt hai cơ chế ngủ đông trên
production**, trong đó một cơ chế chính là thứ owner gọi là *«ngược thiết kế»*. Cắt thì hành vi
**không đổi một chút nào** — và mã **nói đúng điều nó đang làm**.

---

## 5. Đã làm gì

| commit | việc |
|---|---|
| `676e34b` | **`V11096`** — vá lỗi `shadow_mode` + cổng `_v11096` chống tái phạm |
| `2fb1919` | xử **7/10** phép trôi — cổng đóng băng nghiệm thu lịch sử + sửa chuỗi dò `QD-068` |
| `194fed1` | `QD-046` — tách `RỚT SÀN` khỏi `ĐÃ NGỪNG CHẠY` |
| `ce37ba5` | bộ deploy `_v11096_deploy.py` — 9 bước có đường lùi |
| `3827afe` | **`V11097`** — `FU-394` cắt nhánh gan · `QD-069` · bản trình bày cho owner |

### Deploy lượt 1 — 9 tệp

```
VPS chưa trôi   4 tệp runtime khớp backup TỪNG BYTE (sau chuẩn hoá xuống dòng)
backup VPS      7/7 tệp → backups/v11096_pre/
đẩy + so md5    9/9 khớp
py_compile      COMPILE OK  ← TRƯỚC restart
restart         PID 1633166 → 2101247 · active · NRestarts=0
smoke           /api/health=200 · admin=401
dump prompt VPS CTX-18.4 · 18.003 ký tự · 4 lần chuỗi "lợi thế"
_v11032 trên VPS 6/6 ĐẠT
nhật ký          0 dòng error/traceback/exception
```

### Deploy lượt 2 — `FU-394`, 2 tệp

```
backup VPS      2/2 → backups/v11097_pre/
py_compile      COMPILE OK  ← TRƯỚC restart
restart         PID 2101247 → 2103185 · active · NRestarts=0
smoke           /api/health=200 · admin=401
kiểm nhánh gan  combo_super: 0 chỗ còn ×0,3 · post_filter: 0 dòng MÃ SỐNG dùng gan_days
                (5 dòng còn lại đều là chú thích/docstring — §60.3 nói GIỮ)
```

### `FU-394` — cắt gì

| chỗ | TRƯỚC | SAU |
|---|---|---|
| `combo_super.py:607` | `if gan_days <= 8: ×0.6 else: ×0.3` | **`×0.6` thẳng** |
| `post_filter.py:120` | vế `gan_days > 10` **THAY SỐ** kèm `penalty −0,5/−0,7` | **giữ số, hết** |

Gỡ luôn `analyze_gan` khỏi `import` và lời gọi ở cả hai tệp. Sửa cả **docstring** đầu
`post_filter.py`: dòng *«Thay thế số COLD bằng số HOT/WARM»* **chưa bao giờ đúng trong thực tế**.

**GIỮ `_find_replacement()`** — nay không ai gọi, nhưng đó là thiết kế đã viết xong.

> **CHỨNG MINH hành vi KHÔNG ĐỔI** — nạp bản CŨ và MỚI **cạnh nhau**, chạy cùng đầu vào thật:
> `post_filter` **0/12 ca lệch** · `combo_super` **100/100 số khớp TỪNG PHẦN TỬ** ở cả ba miền.
> Không phải *tin* là không đổi — là **đo ra** không đổi.

### `FU-290A` — chốt KHÔNG cắt, và trả lời câu owner hỏi

Owner hỏi *«ko rõ model nào»* — **model duy nhất từng bị đề nghị cắt là `glm-5.1`**.

Nhận xét của owner *«độ trễ do nhiều yếu tố»* **khớp đúng số đo**: `gpt-5.4` **nhanh nhất hệ**
(`15,9s`) nhưng nằm trên đường tới hạn **97,8%** lượt, còn `gpt-5.5` chậm (`170,4s`) thì **0%**
— ở trên đường tới hạn là chuyện **vị trí trong chuỗi**, không phải nhanh chậm.

---

## 6. Cổng kiểm

| cổng | |
|---|---|
| **sổ quyết định `_v10920`** | **✓ KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI** *(từ 10 phép trôi)* |
| `_v11032_kiem_va` **trên VPS** | **✓ 6/6** |
| `_v11096_kiem_mo_goi_rules` (mới) | **✓** · thử chặn `RM-15` **ĐẠT** |
| `_v11093_kiem_fu380` (mới) | **✓** |
| `_v11036_kiem_no_answer` | **✓** — model chết vẫn in ra, chỉ không đếm nhầm |
| `_v11028_cong_dong_bang` | **✓ `DA_DONG_DUNG_HAN`** |
| `_v11050_kiem_drift` K3 | **31 → 25** (trần 30) — **đạt** |
| `_v10981_kiem_lich` · `_v11062` · `_v11034` · `_v11085` · `_v11088` · `_v11027` · `_v10925` | **✓ 7/7** |
| **4 bảng khoá** | `13.089 · 525 · 15.324 · 12.872` — **không đổi qua cả hai lượt deploy** |

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| **19:0x** | *«rà soát tất cả chuẩn bị cho việc xử lý đi nào»* |
| **20:0x** | *«deploy chứ chờ gì nữa em?»* |
| **20:0x** | *«`FU-394` … ⇒ cắt đi»* |
| **20:0x** | *«chưa cắt là đúng vì độ trễ do nhiều yếu tố bới quá nhiều model quá»* |
| **20:0x** | *«toàn là mã ngắn gọn mà bắt duyệt làm sao mà duyệt được duyệt mù ah em»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| bạch thủ 0/3 hôm nay; 525 miền-ngày `+0,52pp` `z=+0,25` | `_v11057_do_thuoc_chinh` |
| T-B: 111 bất đồng, **43 phân biệt**, `z=+0,457` | `prompt_3tang_ab_shadow_v11059` |
| `shadow_mode=True` vỡ còn **106 ký tự** cả ba miền | `_v11032_kiem_va` trước vá |
| sau vá: **14.226 · 13.669 · 17.123** ký tự, 6/6 ĐẠT | `_v11032_kiem_va` sau vá |
| VPS `_v10958` khớp bản `6c4d1504` ⇒ **đi sau 9 ngày** | dò 60 commit |
| `rule_engine.py` VPS LF vs local CRLF ⇒ **0 dòng khác** | `diff` sau khi bỏ `\r` |
| `gemma-4-31b` cuối chạy **29/07**, ngoài pool | `predictions` · `_v10985_bang_chung` |
| cửa sổ đóng băng: **2/56 commit**, cả hai được phép | `_v11028` nghiệm thu lịch sử |
| `FU-394`: **0/12 ca** · **100/100 số** khớp | nạp cũ/mới song song |
| deploy: PID `1633166`→`2101247`→`2103185` · 0 lỗi | `systemctl` · `journalctl` |

### `DOC_SAID`

| tài liệu ghi gì | lệch? |
|---|---|
| `post_filter.py` docstring: *«Thay thế số COLD bằng số HOT/WARM»* | **LỆCH — chưa bao giờ đúng**; đã sửa |
| chú thích `V11032` cảnh báo đúng lỗi mở gói | **đúng nhưng VÔ TÁC DỤNG** — người sửa đi từ `SELECT`, không đi từ đây |
| 6 mục sổ dò `CON_NGUYEN` | **LỆCH sau 21/08** — cửa sổ đóng đúng hạn; đã đổi sang `DA_DONG_DUNG_HAN` |
| `QD-068`: chuỗi dò `` D3` — HOÃN `` | **LỆCH** — bản đồ viết `— **HOÃN,` (in đậm); phép kiểm sai, tài liệu đủ |

### Ba lớp lệch nhau ⇒ FINDING

**`OWNER_SAID` ≠ cách agent làm việc.** Owner chỉ ra một lỗi **cách làm**, không phải lỗi kỹ
thuật: agent tóm quyết định thành **mã ngắn** (`FU-416`, `FU-393`) rồi hỏi *«duyệt không»* —
tức **bắt owner duyệt mù**. Đã ghi thành ràng buộc trong `QD-069` và viết lại hai việc đó thành
`docs/TRINH_OWNER_FU416_FU393.md` — kể từ đầu, không mã tắt, mỗi việc có **chuyện gì đang xảy
ra · số đo · được gì mất gì · đề xuất và vì sao**.

---

## 7. Vướng vấp

**① Bộ deploy tự bắt được ba lỗi của chính nó trong dry-run** — so `md5` thô báo động giả · ba
tệp công cụ bị xếp nhầm nhóm *«mới»* nên sẽ ghi đè **mà không đối chiếu** · bước backup trên VPS
chỉ backup **4/9** tệp ⇒ gỡ về sẽ thiếu. Cả ba đã sửa **trước khi** chạy thật.

**② Cổng mới tự báo đỏ trên mã ĐÚNG.** `_v11096` bản đầu vớ phải câu `SELECT` đầu tiên trong tệp
(6 cột, hàm khác) thay vì câu ngay trước vòng lặp. Bài học riêng: **cổng báo đỏ thì câu hỏi đầu
tiên là «đỏ vì mã, hay vì phép đo?»** — lần này là vì phép đo.

**③ Lệnh kiểm phụ vỡ vì mã hoá console** khi in tiếng Việt qua `python -c`. Không ảnh hưởng kết
quả, nhưng làm mã thoát hiểu nhầm thành lỗi.

---

## 8. Gỡ về

```bash
# gỡ deploy lượt 2 (FU-394)
ssh root@14.225.224.89 'cd /root/Lottery_AI_Test && cp backups/v11097_pre/* web/backend/ && systemctl restart lottery'

# gỡ deploy lượt 1 (gói 21/08)
ssh root@14.225.224.89 'cd /root/Lottery_AI_Test && cp backups/v11096_pre/* web/backend/ && systemctl restart lottery'

# gỡ local
cp backups/post_filter.py.pre_v11097_fu394 web/backend/post_filter.py
cp backups/combo_super.py.pre_v11097_fu394 web/backend/combo_super.py
git revert 3827afe 676e34b
```

**`FU-404` revert mã KHÔNG ĐỦ** — phải **dump lại prompt** xác nhận nhãn cũ trở lại.

---

## 9. Theo dõi tiếp

### Owner còn hai việc để quyết — đã trình bày đầy đủ tại `docs/TRINH_OWNER_FU416_FU393.md`

| | việc | em đề xuất |
|---|---|---|
| **1** | **Bản đề bài đổi ngẫu nhiên mỗi lần chạy** *(`FU-416`)* — hai lần chạy cùng mã ra **6/6/2 dòng khác**; khoá ngẫu nhiên lại thì **0/0/0**. MT và MB có số **bằng điểm ngay ở hai vị trí đầu** ⇒ **số nào AI nhìn thấy trước là do may rủi** | **sửa** (một dòng), nhưng **để riêng một ngày** — hôm nay prompt vừa đổi |
| **2** | **25 tệp tồn kho** *(`FU-393`)* — model `claude-opus-4-6` **đã chạy thật**, nhưng 25 tệp chưa biết tên nó. **2/25 tệp chạm đường sinh số** (`strength_calibrator.py`, 7 điểm gọi) | **đẩy 23 tệp đo** (số công bố **không đổi**), **giữ 2 tệp** cho một ngày riêng có chữ ký riêng |

### Việc còn treo khác

`FU-412` hình phạt `×0,55` nhạy điểm gốc · `FU-413` hai bản sao roster · `FU-414` bảng chết 107
ngày còn 2 điểm đọc sống · `FU-415` hook đường dẫn tương đối · `FU-411` (`D3`, hạn 25/08) ·
`FU-360` neo theo sự kiện `QD-015/016/017` — **ba quyết định đó vẫn `ACTIVE`, hạn 08/08, quá hạn
13 ngày, chưa chạy**.

### Cảnh báo

> **Từ 22/08 `K8` sẽ ĐỎ vì `FU-360` — CỐ Ý.** Kiểm bằng máy: `--hom-nay 2026-08-22` ⇒ **TRƯỢT**.
> Đỏ vì vế *«mồ côi ĐẾN HẠN»* (hạn 18/08 đã qua), **không** phải vế tổng (1/2, dưới trần).

> **22/08 là ngày SẠCH ĐẦU TIÊN của `CTX-18.4`** — cả ba miền cùng một bản prompt. Mọi phép đo
> về prompt mới **phải tính từ ngày đó**, không tính từ 21/08.

**Verdict tách ba dòng:**
- **`CODE_PUSHED`** = `676e34b` · `2fb1919` · `194fed1` · `ce37ba5` · `3827afe`
- **`RUNTIME_PROVEN`** = 11 tệp trên máy chủ · PID đổi hai lần · `_v11032` 6/6 trên VPS · 0 lỗi
- **`REPORT_PUBLISHED`** = bản này

---

TanPhatAI cần làm: ① ghi **gói 21/08 ĐÃ LÊN MÁY CHỦ** — tầng `RUNTIME_PROVEN`, PID
`1633166`→`2101247`→`2103185`, prompt sống **`CTX-18.4`**, 4 bảng khoá **không đổi**; ② ghi
**22/08 là ngày sạch đầu tiên** của `CTX-18.4` — mọi phép đo prompt mới **tính từ 22/08**, không
từ 21/08; ③ ghi **rà soát cuối chu kỳ bắt được lỗi do phiên sáng gây ra** — `shadow_mode=True`
tụt còn **106 ký tự**, đúng loại đã từng ẩn **67 ngày**, và **hoãn deploy nửa ngày đã cứu nó**;
④ ghi **cổng mới `_v11096`** đếm cột `SELECT` vs số tên mở gói — dựng vì lỗi **tái phạm hai lần**;
⑤ ghi **VPS từng đi sau git 9 ngày** (`_v10958` thiếu khối `V11065`) và bộ deploy nay **phân biệt
«VPS đi sau» với «ai đó sửa VPS»**; ⑥ ghi **`FU-394` ĐÓNG** — owner ký *«cắt đi»*, hành vi
**đo được là không đổi** (0/12 ca · 100/100 số); ⑦ ghi **`FU-290A` ĐÓNG** — không cắt model nào
vì độ trễ; model duy nhất từng bị đề nghị là **`glm-5.1`**; ⑧ ghi **sổ quyết định 10 phép TRÔI →
0** và **K3 drift 31 → 25**; ⑨ ghi **ràng buộc mới trong `QD-069`**: cấm trình bằng mã ngắn rồi
bắt owner duyệt — phải diễn giải bằng lời thường, có số, có được-mất; ⑩ ghi **hai việc còn chờ
owner** tại `docs/TRINH_OWNER_FU416_FU393.md`.
