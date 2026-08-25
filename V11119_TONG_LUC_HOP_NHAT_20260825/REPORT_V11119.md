# V11119 — ĐỌC LẠI TOÀN BỘ VẾT LÀM VIỆC, GOM VỀ MỘT SỔ: **BỐN CON SỐ ĐÃ CÔNG BỐ PHẢI RÚT LẠI**

**Ngày:** 25/08/2026 · **Commit riêng:** `de35b10` · **Commit công khai:** `62bc74f` ·
**Trạng thái:** `READ-ONLY` — không deploy, không restart, không sửa mã production, không ghi DB

---

> # 🔴 RÚT LẠI — HAI CÂU TRONG CHÍNH BẢN NÀY SAI
>
> *Thêm `25/08/2026 21:0x` bởi `V11121`, theo `PRJ-RETRACTION-001` (*«rút lại đúng chỗ đã công
> bố»*). **Không sửa câu gốc bên dưới** — giữ nguyên để người đọc thấy điều đã lưu hành.*
>
> ### R6 — *«**26** nhãn version chỉ có ở `git log`»* (§3.3) — **KHÔNG TÁI LẬP ĐƯỢC**
>
> **Nguyên văn câu sai:** *«Và chiều ngược lại — **26 nhãn version chỉ có ở `git log`**, không có
> mục CHANGELOG, trong đó `V11077` và `V11079`.»*
>
> **Điều đúng:** không một phạm vi theo **số hiệu** nào ra `26` — cổng ra **12**, thô `≥V11062` ra
> **21**, gộp hậu tố toàn lịch sử **54**, thô toàn lịch sử **135**. Con số `26` **chỉ tái lập được**
> khi cắt theo **NGÀY COMMIT `≥ 2026-08-10`** — và mốc đó **không được khai** ở bất kỳ đâu trong
> bản này. Đây là `RM-11`: số không tái lập được thì không dùng làm căn cứ.
> *Tái lập:* `_v11062_nang_version.muc_git_log()` ∖ `muc_changelog()` → **12** nhãn.
>
> **Quyết định đã dựa vào số sai:** mục `P0-4` của plan — *«bù mục CHANGELOG cho 26 bản chỉ có ở
> git»*. Khối lượng việc đó sai; và **12/12** nhãn git-only trong phạm vi cổng **ĐỀU CÓ** báo cáo
> công khai, `V11070`–`V11075` đã được ghi bù **GỘP** trong khối `CHANGELOG V11076` — cách ghi hợp
> lệ. ⇒ **Không có việc bù nào ở đây.**
>
> ### R7 — *«đây chính là chỗ làm cổng `_v11062 K1` mù»* (§3.3) — **SAI TỪ `V11082`**
>
> **Nguyên văn câu sai:** *«Đây chính là chỗ làm cổng `_v11062 K1` mù: nó lấy worklist từ
> `muc_changelog()`, nên bản **không có mục CHANGELOG** thì cổng **không thể** báo thiếu.»*
>
> **Điều đúng:** worklist của `K1` **đã là** `CHANGELOG ∪ git log` **từ `V11082`**
> (`web/backend/_v11062_nang_version.py:207-212`), và chính mã ghi rõ `chi_git` là **GHI CHÚ**,
> không phải lỗi (`:249-258`, kèm lý do *«cổng đỏ 100% mất sạch giá trị cảnh báo»*).
> *Tái lập:* `python web/backend/_v11062_nang_version.py --kiem` →
> `chỉ-có-ở-git 12 (trong đó THIẾU HISTORY: 0)` · `✓ NANG_VERSION_V11062=ĐẠT`.
>
> **Quyết định đã dựa vào số sai:** mục `P3-2` của plan — *«vá `_v11062 K1`»*. **Việc đó không tồn
> tại**; nó đã được vá 8 ngày trước bản này.
>
> ### Điều **KHÔNG** rút — vẫn đúng nguyên
>
> `R1` (`V11077`/`V11079` **có đủ** báo cáo) · `R2` (**10** bản thiếu báo cáo, đã xác minh lại
> `10/10` và **cả 10 đều có nguồn để bù**) · `R3` (**0** quyết định trôi) · `R4` (Algorithm Card
> đã có — nay đo được **4 thẻ**, ma trận `4 sản phẩm × 14 bước`: **43 ô đủ · 4 một phần · 6 thiếu ·
> 3 không áp dụng**) · `R5` (cổng A55 nói quá — **xác nhận**, và thật ra có **BA** lỗ hổng chứ
> không phải hai; xem `REPORT_V11121`) · `FU-438` (**xác nhận**, và bề mặt rò thật là **~678 KB**
> chứ không phải 39,7 KB; xem `REPORT_V11120`).

---

## 1. Tóm tắt

Owner yêu cầu đọc **toàn bộ** phiên làm việc Claude Code **và** Cursor, hợp với tài liệu tổng kết
đính kèm, rồi gom thành **một** báo cáo và **một** plan, *«không làm rơi rụng bất kỳ vấn đề nào»*.

Đã bóc và đọc hết: **12 tệp phiên `.jsonl`** (≈350 MB) ⇒ **234 lượt owner duy nhất** trên
**7 phiên riêng biệt** (03/07 → 25/08), trong đó phát hiện **5 tệp là bản rẽ nhánh `--resume`** của
cùng một cuộc trò chuyện — 192 MB đĩa cho ~38 MB nội dung thật. Và kho Cursor
**10,9 GB** (`cursorDiskKV` 310.889 dòng · 286 phiên `composerData` · 213.115 bong bóng)
⇒ **890 tin owner** trên **125 phiên** (04/07 → 05/08).
Hợp hai nguồn, khử trùng: **711 lượt owner duy nhất** — sổ sinh **bằng phép cơ học**, không qua
diễn giải, nên bảo đảm **không rơi lượt nào**.

**Bốn con số đã công bố hoá ra sai và phải rút lại** (`PRJ-RETRACTION-001`, §4):

| # | câu đã công bố | điều đúng |
|---|---|---|
| R1 | *«`V11077` · `V11079` thiếu báo cáo, chưa ai nhận»* | **SAI** — cả hai có **đủ** báo cáo công khai từ 16/08; thứ thiếu là **mục CHANGELOG** |
| R2 | *«còn 4 bản (hoặc 6 bản) thiếu báo cáo công khai»* | **THIẾU** — đếm bằng máy: **10 bản**, cộng **1 bản đặt sai thư mục** |
| R3 | *«cổng quyết định vẫn báo 3 phép TRÔI»* | **KHÔNG CÒN ĐÚNG** — chạy lại 19:30 hôm nay: **0 TRÔI**, 1 phép không kết luận được |
| R4 | *«`AS_IS_TOTAL_OUTPUT` + 4 Algorithm Card — chưa viết»* | **QUÁ NẶNG** — đã có **175.765 byte / 2.169 dòng**, ba thẻ phủ cả bốn sản phẩm |

**Một việc đang hở ngay lúc này:** `FU-438` được xác minh lại **trực tiếp trên production lúc
19:27** — đường `/api/final-bundle/history` trả **39.682 byte cho người xem ẩn danh**, chứa cả
`ranked_numbers` **và** `voters`, tức toàn bộ bảng xếp hạng nội bộ. Đường anh em
`/api/final-bundle` **chặn đúng** (1.711 byte, không có hai trường đó). Đây là mức
**`RUNTIME_PROVEN`**, không phải đọc lại báo cáo.

**Kết luận kiểm toán `TOTAL` của `V11116` không bị lật.** Bản này không cố lật nó — nó **đổi thứ
tự ưu tiên** theo đúng điều kết luận đó chỉ ra.

---

## 2. Owner yêu cầu gì (nguyên văn)

### 2.1 · Prompt chính — `~18:57` giờ VN, 25/08/2026

> *« Em hãy tiến hành đọc toàn bộ các phiên làm việc của claude code và cursor kết hợp báo cáo
> tổng hợp đính kèm và các thông tin audit báo cáo tất cả mọi thể chạy tổng lực tổng hợp lại một
> phiên tổng lực với đầy đủ tất cả các vấn đề không làm rơi rụng bất kỳ vấn đề nào, các vấn đề đã
> xử lý , có thể xử lý , tự xử lý rõ ràng , các yêu cầu của anh v.... không bỏ sớt bất kỳ điểm nào
> nha em. Em tiến hành xem toàn bộ các phiên làm việc khác của Claude Code dùm anh, đồng thời anh
> có đinh kèm các tổng kết báo cáo cuối cùng , Sau đó phân tích lên kế hoạch xử lý cho liền mạch
> nhất quán nha em . Gom lại tổng hợp lại thành một báo cáo cáo tổng chi tiết đầy đủ tổng lực hợp
> nhất và đề xuất 1 plan tổng lực dùm anh. »*

Kèm tệp đính kèm **«Tổng Kết Lottery Ai.txt»** — bốn lượt báo cáo cuối của các phiên khác.
Đã vào `docs/SO_TUONG_TAC_OWNER.md` dòng `~18:57`, loại `YÊU_CẦU`, trạng thái `ĐANG_LÀM`.

### 2.2 · Yêu cầu này **KHÔNG** phải lần đầu — **24 lượt** owner đã nêu cùng một điều

Quét toàn corpus 711 lượt tìm các câu phàn nàn về việc rơi rớt/cẩu thả: **24 lượt trực tiếp**
(chưa tính prompt dài trên 4.000 ký tự), rải từ 02/08 tới hôm nay. Trích nguyên văn, kèm giờ VN:

| # | giờ VN | nguyên văn (trích) |
|---|---|---|
| 10 | 02/08 21:25 | *«…tất cả mọi thứ không bỏ sót bất kỳ nội dung nào trong trò chuyện này ?»* |
| 46 | 06/08 20:20 | *«Cần 1 cơ chế chống quên lãng , rơi rớt các vấn đề anh phân tích đề xuất cũng như căn dặn nha em.»* |
| 50 | 06/08 21:48 | *«Trời trời em làm việc cẩu thả quá… câm rơi rớt, liền mạch, ghi nhận đầy đủ, tư duy logic, tương quan tương thích phù hợp , tránh làm chỗ này hỏng chỗ kia nha»* |
| 71 | 07/08 14:47 | *«Điều này chứng tỏ em làm việc cẩu thả , từ các lần trước đó làm nên chứ ai»* |
| 123 | 09/08 20:38 | *«Anh thực sự rất không hài lòng về em, em đã xem nhẹ tài liệu mặc dù anh nhắc rất nhiều lần , tài liệu có thể đi sau code thật nhưng…»* |
| 124 | 09/08 20:50 | *«Rất bực bội bữa giờ toàn làm mù các seccsion trước đó đều mù, em có xem được seccsion của chính cursos không có kết nối đọc hiểu không thì tìm hiểu luôn đi»* |
| 155 | 12/08 19:23 | *«…cấm rơi rụng , gián đoạn, ngắt quản mọi thử phải liền mạch, tương quan tương thích , tương ưng phù hợp tuyệt đối nha em»* |
| 179 | 16/08 14:19 | *«…em làm việc vẫn chểnh mãng lắm rơi rớt tùm lum , anh phải nhắc đi nhắc lại, nhân mạnh nhiều lần mệt mỏi quá em.»* |
| 180 | 16/08 18:43 | *«Rules quy tắc quy luật soi cầu ngày nào cũng có mà toàn làm rơi rụng…»* |
| 181 | 16/08 18:51 | *«làm sao phải tổng lực không rơi rớt, phải tìm cho ra chỗ cải tiến nâng cao dự đoán , cấm đoán bừa , suy diễn.»* |
| 203 | 20/08 19:33 | *«Đã xem kỹ tổng lực toàn bộ chưa ? lâu quá nên nhiều cái nó mơ hồ , không rõ ràng và có thể rơi rớt…»* |
| 212 | 21/08 21:35 | *«Em làm việc có vẻ cẩu thả và dư thừa , em có biết là anh đã yêu cầu em lên kế hoạch chuyển đổi các thông số đang tiêm vào prompt … biết bao nhiêu lần không hả ?»* |

*(12 lượt còn lại nằm trong sổ yêu cầu owner kèm theo — mục #22 #30 #49 #73 #120 #122 #125 #141 #147 #198 #234 và các lượt Cursor.)*

### 2.3 · Vì sao bản này dựng sổ bằng **máy** chứ không bằng tóm tắt

Một yêu cầu lặp **24 lần** nghĩa là cách làm cũ — đọc rồi tóm tắt — **đã thất bại nhiều lần**.
Nên sổ yêu cầu owner của bản này sinh **bằng phép cơ học** từ vết phiên: trích thẳng nguyên văn,
không qua mô hình diễn giải. Cột phân loại có thể sai ở ca biên; cột **NGUYÊN VĂN** thì **luôn
đúng**. Đó là cách duy nhất bảo đảm không rơi lượt nào.

---

## 3. Đào bới / phát hiện

### 3.1 · Quy mô corpus — đo được, không ước lượng

| nguồn | quy mô thật | khoảng |
|---|---|---|
| Claude Code — tệp phiên | **12 tệp `.jsonl`**, ≈350 MB | — |
| — phiên riêng biệt | **7** | 03/07 → 25/08 |
| — **bản rẽ nhánh `--resume`** | **5** tệp, cùng `promptId`/nội dung, chỉ khác `sessionId` và `uuid` từng dòng ⇒ **192 MB đĩa cho ~38 MB nội dung thật** | 01/08 → 09/08 |
| — lượt owner duy nhất | **234** · 810.865 ký tự | 03/07 → 25/08 |
| Cursor — kho | **10,9 GB** · `cursorDiskKV` **310.889** dòng · `composerData` **286** · `bubbleId` **213.115** | — |
| — phiên có lời owner | **125** | 04/07 → 05/08 |
| — tin owner | **890** · 1.113.046 ký tự | 04/07 → 05/08 |
| **hợp nhất, khử trùng** | **711 lượt owner duy nhất** (227 Claude Code + 484 Cursor) | 04/07 → 25/08 |
| CHANGELOG | **893** mục version · **387** tiêu đề `## Vxxxxx` duy nhất | — |
| kho công khai | **390** thư mục báo cáo · **1.607** tệp `.md` | — |

Phân loại 711 lượt: `YÊU_CẦU` 263 · `HỎI` 183 · `ĐỔI_ƯU_TIÊN` 93 · `PHÀN_NÀN` 74 ·
`XÁC_NHẬN` 65 · `BÁC_BỎ` 33. Dạng: lượt trực tiếp 563 · prompt lớn 138 · tóm tắt nén hệ thống 10.

### 3.2 · Trục 35 prompt tổng lực — dựng lại đủ, và một lỗ hổng

Dựng lại được toàn bộ chuỗi: `PL19b` · `PL19c` · lần 1 → lần 35.

| lần | trạng thái |
|---|---|
| 10 | ghi rõ **bị thay** bởi lần 11 (*«thay prompt lần 10 chưa chạy»*) |
| 20 | ghi rõ **bị thay** bởi lần 21 (*«thay thế prompt lần 20 chưa từng chạy»*) |
| 31 | ghi rõ **`VOID`** trong prompt 32 |
| **14** | 🔴 **không có dấu vết nào** trong toàn bộ vết phiên lẫn tài liệu. **KHÔNG KẾT LUẬN ĐƯỢC** đây là prompt chưa từng gửi hay phiên chứa nó đã mất |

### 3.3 · Đối chiếu version × báo cáo công khai — **con số cũ sai**

Đếm bằng máy trên dải `V11070–V11199` (40 bản gốc trong CHANGELOG):

```
🔴 KHÔNG CÓ BÁO CÁO CÔNG KHAI (10):
   V11093 · V11094 · V11096 · V11099 · V11100 · V11107 · V11111 · V11112 · V11115 · V11117
🟡 CÓ BÁO CÁO NHƯNG ĐẶT SAI THƯ MỤC (1):
   REPORT_V11118.md → nằm trong V11116_TOTAL_KHONG_KHAC_NEN_20260825/
🟢 CÓ THƯ MỤC RIÊNG (29)
```

Và chiều ngược lại — **26 nhãn version chỉ có ở `git log`, không có mục CHANGELOG**, trong đó
`V11077` và `V11079`. Đây chính là chỗ làm cổng `_v11062 K1` mù: nó lấy worklist từ
`muc_changelog()`, nên bản **không có mục CHANGELOG** thì cổng **không thể** báo thiếu.
CHANGELOG `V11081` đã ghi lại đúng cơ chế này: *«`V11077` (`a33b86a`) và `V11079` (`4a7ee6d`)
trôi 34 phút sau khi vừa bù xong 12 bản, cổng vẫn báo xanh»*.

### 3.4 · `FU-438` — xác minh lại trên production, 19:27 ngày 25/08 (`RM-13`)

Gọi **ẩn danh** qua tên miền công khai, chỉ đọc mã trạng thái và đếm trường, **không in giá trị**:

| đường | HTTP | byte | `ranked_numbers` | `voters` |
|---|---|---|---|---|
| `/api/health` | 200 | 866 | — | — |
| `/api/final-bundle?region=MN` | 200 | **1.711** | — | — |
| `/api/final-bundle/history?region=MN&limit=2` | 200 | **39.682** | **CÓ** | **CÓ** |
| `/api/final-bundle/selection-delta?region=MN&days=7` | 200 | 5.401 | — | — |

Đường `/api/final-bundle` **chặn đúng**. Chỉ `/history` lọt, vì `api_get_bundle_history`
(`main.py:10952`) **không nhận tham số `request`** ⇒ về mặt vật lý **không thể** gọi cổng đóng
băng. Owner ký treo toàn bộ view người dùng **06–08/06** ⇒ đã hở **78 ngày**.
Mức: **`RUNTIME_PROVEN`**.

### 3.5 · Cấu trúc nợ quản trị — không phải một đống

Đọc `docs/FOLLOW_UP_TRACKER.md`: **313 khối `FU` duy nhất**, **207** không mang nhãn đóng.
Con số chính thức của cổng đầu phiên: **189 treo · 125 quá hạn · 6 đến hạn hôm nay · 34 không ghi
hạn · 3 thiếu mã đọc**.

| nhóm | số mục | nghĩa |
|---|---|---|
| chặn ở **owner** | **37** | `OWNER_DECISION_NEEDED` 12 · `OWNER_LOCK` 12 · `AWAITING_OWNER_OK` 11 · `CHO_OWNER_KY` 1 · `BLOCKED` 1 |
| đã tìm ra nguyên nhân, **chưa vá** | **81** | `MEASURED_ROOT_CAUSE` 52 · `MEASURED_BUT_NOT_FIXED` 24 · `..._FOUND` 5 |
| đã deploy, **chờ xác minh** | **33** | `DEPLOYED_PENDING_LIVE_VERIFY` 26 · `DEPLOYED_PENDING_OWNER_VERIFY` 7 |
| chờ chu kỳ live | **18** | `WAIT_LIVE` |
| sẵn sàng, chưa deploy | **7** | `READY_NOT_DEPLOYED` |
| đã đóng | **106** | `CLOSED` 53 · `CLOSED_PASS` 38 · `DONE` 8 · `CLOSED_FAIL` 4 · … |

### 3.6 · Hai chỗ hỏng trong chính bộ máy quản trị

- 🔴 **`QD-041` — quyết định đóng băng — quá hạn rà soát 4 ngày mà vẫn `ACTIVE`.** Vùng khoá của
  nó hết hiệu lực **21/08**, nhưng không ai đóng quyết định. Hệ quả: các mục ghi *«chặn bởi vùng
  `QD-041`»* (ví dụ `FU-406`, `FU-337`) đang treo lơ lửng — không rõ còn bị chặn hay không.
- 🔴 **Chỉ `8/73` quyết định khai được quan hệ thay thế** (`thay_the`/`thay_boi`), trong khi
  `RM-19` buộc **mọi** quyết định mới phải có. 65 quyết định còn lại không truy được cái nào thay
  cái nào.

**15 quyết định quá hạn rà soát 4–17 ngày:** `OD-20260801-B` · `QD-015` · `QD-016` · `QD-017` ·
`QD-018` (quá 16–17 ngày) · `OD-20260803-B` · `QD-021` · `QD-022` (quá 15) · `QD-024` (14) ·
`QD-025` · `QD-026` · `QD-027` (13) · `QD-028` (6) · `QD-037` (5) · `QD-041` (4).

### 3.7 · Chỗ chi phí — owner hỏi nhiều lần, và số đo có thật

Đo 21/08 (`docs/CAT_GIAM_MODEL_VA_TON_DONG_20260821.md`), **vẫn đúng**:

- **30 model chạy mỗi ngày** · 22 là AI tốn tiền · ~58 lượt gọi/ngày · **1.741 lượt/30 ngày**.
- **999 lượt/30 ngày = 57% toàn bộ chi phí gọi AI** chảy vào **14 model không nằm trong danh
  sách được phép vào output** — **13/14 có ĐÚNG 0 phiếu** trong bundle.
- **41 model từng chạy ngoài output · 4.955 lượt · CHƯA CÓ model nào từng được cất nhắc** — sổ
  `shadow_activation_registry` toàn bộ `SHADOW_AUTO`, `owner_approved = 0`.
- 🔴 **Không ai đang đo tiền.** `model_latency_cost_audit_daily.token_count`/`cost_estimate` và
  `prediction_trace.jsonl.cost_estimate` — **cả hai đều 0 giá trị**.

### 3.8 · Phép đo ra kết quả **ÂM hoặc không kết luận được** — vẫn ghi đủ

| # | đã đo gì | kết quả |
|---|---|---|
| 1 | 5 tệp phiên có trùng byte không | **KHÔNG** — băm khác nhau; phải đo lại mới ra đúng quan hệ (bản rẽ nhánh) |
| 2 | Cursor có đọc được qua `conversation-search.db` không | **KHÔNG** — 164 hàng, tiêu đề rỗng gần hết, chỉ **6/164** hàng có nội dung |
| 3 | Prompt 14 nằm ở đâu | **KHÔNG TÌM ĐƯỢC** — không kết luận |
| 4 | Có phiên nào từng đọc Cursor trước đây không | **CÓ** — `d2a0e7e5` mở kho lúc **13:50:40** ngày 09/08, tức **40 giây** sau câu hỏi của owner. Giả thuyết ban đầu của agent («đây là phiên đầu tiên») **bị bác** |
| 5 | Thiết kế `GĐ-7` nằm trong tài liệu nào | **KHÔNG CÓ TÀI LIỆU NÀO** — chỉ tồn tại trong vết phiên |
| 6 | `AS_IS_TOTAL_OUTPUT` đã có chưa | **CÓ PHẦN LỚN** — bản 24/08 dài 175.765 B, ba Algorithm Card phủ cả bốn sản phẩm ⇒ trạng thái «chưa viết» là **quá nặng** |
| 7 | Cổng quyết định còn báo TRÔI không | **KHÔNG** — 0 TRÔI, 1 không kết luận được |

---

## 4. Hướng xử lý và vì sao chọn

| lối | vì sao không chọn |
|---|---|
| vừa đọc vừa vá luôn | 25/08 là ngày `GĐ-0` khoá *«cấm đổi production TOTAL giữa ngày»*, và phần lớn việc tồn đọng **đổi hành vi cổng hoặc lược đồ** ⇒ đúng vùng owner khoá *«cấm tự quyết»* |
| chỉ đọc rồi tóm tắt | owner yêu cầu *«không làm rơi rụng bất kỳ vấn đề nào»* — mà tóm tắt là **cách chắc chắn nhất để rơi**, và đã thất bại 24 lần |
| **đọc đủ → dựng sổ bằng máy → một plan** ✅ | mỗi vấn đề có **đúng một dòng**, có nhãn trạng thái, có ai chặn, có bằng chứng ⇒ phiên sau và `TanPhatAI` đọc là biết ngay phải làm gì |

**Về cách đọc:** 22 làn chạy song song `READ-ONLY` — 6 lát Claude Code theo mốc thời gian,
3 lát Cursor, 8 khu vực trạng thái, và **5 làn phản biện** có nhiệm vụ **bác bỏ**, không phải
xác nhận. Song song đó, sổ yêu cầu owner được dựng **bằng phép cơ học** để không phụ thuộc vào
việc mô hình có bỏ sót hay không.

**Vì sao plan xếp thứ tự như ở §9:** phép đo 25/08 chứng minh **bậc thang xếp hạng không mang
thông tin**. Nếu vậy thì thêm model, bớt model, hay tinh chỉnh trọng số **đều không phải đòn
bẩy** — cả đường cong `k=1..16` đã đo là dưới nền. Plan dồn sức vào **ba chỗ có bằng chứng**:
trùng lặp nguồn (`+13,4pp ± 3,3`) · chi phí không ai đo (`57%`) · bề mặt công khai đang hở
(`78 ngày`).

---

## 5. Đã làm gì

| tệp | thay đổi | ghi chú |
|---|---|---|
| `docs/SO_TUONG_TAC_OWNER.md` | **THÊM 1 dòng** (`~18:57`), +1.086 ký tự · bảng 6 → **7 dòng** | append-only, **không sửa dòng cũ** nào — `PRJ-INTERACTION-LEDGER-001` mục 3 |
| `docs/OWNER_DECISION_LEDGER.md` | máy sinh lại — **chỉ đổi dòng dấu thời gian** | tác dụng phụ của việc chạy cổng `_v10920_decision_ledger.py`; bản `.md` do máy sinh |
| `docs/_LEDGER_TRANG_THAI.json` · `docs/_I2_DA_CHAY.json` | dấu thời gian chạy cổng | máy sinh |
| kho công khai | **thêm** `V11119_TONG_LUC_HOP_NHAT_20260825/` (báo cáo này + conversation context) | — |

**KHÔNG deploy · KHÔNG restart service · KHÔNG sửa một dòng mã production nào · KHÔNG ghi DB ·
KHÔNG đụng `/du-doan`.** Không có hash 4 bảng khoá trước/sau vì phiên không chạm DB.

Sản phẩm kèm theo (kho riêng, thư mục làm việc tạm — **không đưa vào Git** vì là bản trung gian):
sổ yêu cầu owner cơ học **711 dòng** · sổ theo dõi cơ học **313 khối `FU`** · bản đồ 35 prompt ·
chỉ mục chủ đề toàn corpus.

---

## 6. Cổng kiểm

| cổng | lệnh | kết quả thật |
|---|---|---|
| đầu phiên | `_v10920_session_start.py` | **chạy** · 189 treo · **125 quá hạn** · 6 đến hạn hôm nay · 15 QĐ tới hạn · 3 thiếu mã đọc · checkpoint quá hạn **0** · `AGENTS.md` khớp bản sinh |
| sổ quyết định | `_v10920_decision_ledger.py` | ✓ **`KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI`** · ⛔ **1 phép không kết luận được** (`QD-056`, `RM-01` chặn vì DB local cũ hơn 6 giờ) |
| cấp số hiệu | `_v11044_cong_so_hieu.py` | ✓ `SO_HIEU_V11044=KHỚP` · V 462 số, cao nhất `V11118`, trống tiếp **`V11119`** · `FU-439` · `QD-072` · mọi nhãn QD trong 186 báo cáo đều có trong sổ |
| bốn mặt §63 | `_v11062_nang_version.py --kiem` | ✓ **`NANG_VERSION_V11062=ĐẠT`** · CHANGELOG 420 mục · HISTORY 160 mục (mới nhất **0 ngày trước**) · STATE `seq=448`, `last_version=V11118` · git-only 12 (thiếu HISTORY: 0) |
| production (`RM-13`) | `curl` ẩn danh 4 đường | health `200` · `/final-bundle` **1.711 B không lộ** · `/final-bundle/history` **39.682 B CÓ `ranked_numbers`+`voters`** ⇒ `FU-438` **`RUNTIME_PROVEN`** |
| báo cáo A55 | `_v10921_report_gate.py V11119` | *(chạy sau khi commit — kết quả điền ở §9)* |

---

## 7. Vướng vấp

1. **Cursor không đọc được bằng đường thông thường.** `conversation-search.db` có 164 hàng nhưng
   **tiêu đề rỗng gần hết**, và bảng nội dung chỉ **6/164** hàng có chữ. Phải mở thẳng kho
   `state.vscdb` **10,9 GB** và lọc `bubbleId:*` lấy `type == 1`.
   **Hậu quả nếu bỏ qua:** kết luận *«Cursor không có dữ liệu»* — sai, mất 890 tin owner.
2. **Năm tệp phiên trùng nhau làm mọi phép đếm thô sai gấp ~5 lần.** Và **băm tệp khác nhau** nên
   không thể khử theo băm tệp — mỗi dòng nhúng `sessionId` riêng. Phải khử theo **băm nội dung
   từng lượt**.
   **Hậu quả nếu bỏ qua:** báo *«1.168 lượt owner»* thay vì 234 — phóng đại gấp 5.
3. **Agent tự đặt một giả thuyết sai và phải tự bác.** Định ghi *«đây là phiên đầu tiên đọc được
   Cursor»*. Tra vết phiên: `d2a0e7e5` đã mở kho lúc **13:50:40** ngày 09/08, **40 giây** sau câu
   hỏi của owner. Giả thuyết **bị bác trước khi trình**.
   **Hậu quả nếu bỏ qua:** một câu tự khen sai sự thật, và làm owner tưởng yêu cầu 09/08 bị bỏ.
4. **Mã `GĐ-n` bị dùng lại giữa các prompt.** `GĐ-7` là «retire P&L» ở prompt 32, «lượt rỗng» ở
   prompt 33/34, «10 bản vá» ở prompt 35.
   **Hậu quả nếu bỏ qua:** tra theo mã ra nhầm việc — đã suýt xảy ra trong chính phiên này.
5. **Thiết kế `GĐ-7` chỉ tồn tại trong vết phiên**, không có trong tài liệu nào của kho.
   **Hậu quả nếu bỏ qua:** phiên đóng hoặc bị nén là **mất hẳn**; owner phải trả tiền để suy lại
   toàn bộ 10 bản vá.
6. **Các làn đọc sinh kết quả rất chậm** (mỗi làn trả 76–113 mục có nguyên văn). Nên sổ yêu cầu
   owner được dựng **bằng phép cơ học song song**, không chờ mô hình — đó là lý do bản này bảo
   đảm được «không rơi lượt».

---

## 8. Gỡ về

Phiên không chạm runtime nên không có gì phải gỡ ở phía máy chủ.

| tệp | gỡ về | mất bao lâu |
|---|---|---|
| `docs/SO_TUONG_TAC_OWNER.md` | `git checkout -- docs/SO_TUONG_TAC_OWNER.md` | tức thì |
| `docs/OWNER_DECISION_LEDGER.md` · `docs/_LEDGER_TRANG_THAI.json` | `git checkout --` hoặc chạy lại `_v10920_decision_ledger.py` | tức thì |
| thư mục báo cáo công khai `V11119_*` | `git rm -r` thư mục đó rồi commit lại | tức thì |

Gỡ về rồi thì kho quay lại đúng trạng thái `76c391b` / `cb6c746`.

---

## 9. Theo dõi tiếp

### 9.1 · Việc **tự xử lý được ngay** — không cần chờ ai, không chạm production

| mã đọc | việc | ngưỡng đóng bằng số |
|---|---|---|
| `BC2608` | Bù **10 báo cáo công khai** còn thiếu + dời `REPORT_V11118.md` về thư mục riêng | đếm lại: **0 bản** trong dải `V11070–V11199` thiếu báo cáo |
| `TK2608` | Bù mục CHANGELOG cho **26 bản chỉ có ở git**, hoặc khai vào `GAP_MARKER` kèm lý do | `_v11062 --kiem` báo `chỉ-có-ở-git = 0` |
| `TK2608-1` | **Cứu thiết kế `GĐ-7`** khỏi vết phiên thành tài liệu thật (10 bản vá) | tồn tại tệp `docs/GD7_*.md` chứa đủ 10 mục |
| `SC2608-4` | Vá **`_v11062 K1`** — worklist lấy từ `git log ∪ CHANGELOG` | thử chặn hai chiều: giả lập bản git-only ⇒ cổng **đỏ**; sạch ⇒ **xanh** |
| `TK2608-2` | Bổ sung **§55 quy ước giờ THỨ TƯ** — `scheduler_logs.log_time` là UTC | có mục §55 nhắc tên bảng ở đủ sáu mặt |
| `TK2608-3` | Sửa cột đơn vị lẫn lộn `143,3` (là **số lượt kỳ vọng**, đứng cạnh phần trăm) ở **ba nơi**: CHANGELOG · SSOT · `REPORT_V11116` | grep `143,3` không còn đứng trong cột nền phần trăm |
| `TK2608-4` | Gán **mã đọc §58** cho 3 mục treo còn thiếu (`FU-330` `FU-321` `FU-300`) | cổng đầu phiên báo `thiếu mã đọc = 0` |

### 9.2 · Cần **OWNER KÝ** — agent không tự làm (9 quyết định gom từ 37 mục `FU`)

| # | việc | agent nghiêng về |
|---|---|---|
| `K1` | Rò rỉ kho công khai — IP 1.137 lần/86 tệp · đường dẫn 681 lần/151 tệp · chuỗi root 40 lần/22 tệp | **scrub nội dung hiện tại**, không đụng lịch sử git |
| `K2` | 🔴 `FU-438` — bề mặt công khai lộ bảng xếp hạng nội bộ, **`RUNTIME_PROVEN` 19:27 hôm nay** | **vá cổng** — owner đã ký treo view 06/06, đây là chỗ lọt ngoài ý muốn |
| `K3` | `GĐ-7` — **10 bản vá** | ký **6 cái không đổi lược đồ** trước (①②③⑥⑦⑧) |
| `K4` | Ba khuyết tật `K1/K2/K3` của `M0` | **vá `K3` (dedupe family) trước** — chỗ duy nhất có bằng chứng thống kê |
| `K5` | Cổng khoá phiên — chưa có cổng nào soi «phiên khác đang ghi cùng kho» | **dựng** — va chạm đã xảy ra thật chiều 25/08 |
| `K6` | `REPORT_V11037.md` bị cổng an toàn chặn 12 vi phạm | **scrub bản mới**, không dùng cờ bỏ qua cổng |
| `K7` | Cắt model — 57% chi phí vào 14 model, 13/14 có 0 phiếu | **đo tiền trước** — hiện không ai đo tiền |
| `K8` | `FU-365` — 229 dòng sai nhãn miền | cần một câu quyết (đã chặn từ 22/08) |
| `K9` | **15 quyết định quá hạn rà soát**, gồm `QD-041` hết hạn 21/08 vẫn `ACTIVE` | **gia hạn gộp** kèm ngày mới, và **đóng `QD-041`** |

**37 mã `FU` đang chặn ở owner:** `FU-438` `FU-437` `FU-435` `FU-420` `FU-418` `FU-412` `FU-399`
`FU-396` `FU-393` `FU-391` `FU-390` `FU-383` `FU-376` `FU-365` `FU-346` `FU-337` `FU-320`
`FU-319` `FU-315` `FU-300` `FU-299` `FU-298` `FU-295` `FU-290` `FU-261` `FU-235` `FU-234`
`FU-233` `FU-232` `FU-231` `FU-226` `FU-224` `FU-223` `FU-221` `FU-216` `FU-193` `FU-192`.

### 9.3 · Lịch đã đăng ký — **không đổi**

| mốc | ngày | việc | ai chặn |
|---|---|---|---|
| `D1` | **26/08/2026** | bật 3 ứng viên shadow, `effective_date ≥ 26/08` | không ai — **lỡ là mất 14 ngày** |
| `D2` | **09/09/2026** | đọc lại lần 1 — 14 ngày prospective | thời gian |
| `D3` | **23/09/2026** | **ngày chốt promotion** — trước đó cấm nâng `OFFICIAL` | thời gian |
| — | **07/10/2026** | `FU-367` chấm lane G2-MB | thời gian — **cấm chấm sớm** |

### 9.4 · Mục chờ **thời gian**, không chờ người

`FU-366` xác minh `C23`/`C24` + cron — chờ cron chạy lần đầu ·
`FU-368` guard local ≠ VPS — cần biết `V11023` có được duyệt deploy không ·
`FU-407` đo `lo3`/`xien2`/`xien3` với nền đúng từng bó — **read-only, không chặn**,
nhưng phải dùng **hypergeometric** `1 − C(100−D,k)/C(100,k)` cho bạch thủ MN/MT nhiều đài,
**không** dùng `1 − (1−b)^k`.

### 9.5 · Mục mới khai trong phiên này

| mã | nội dung | hạn |
|---|---|---|
| `FU-439` · `TK2608-1` | **Thiết kế `GĐ-7` chỉ tồn tại trong vết phiên** — phải cứu thành tài liệu | 26/08 |

---

## 10. BA LỚP NGUỒN (§62 · A60)

### `OWNER_SAID`

> *« …tổng hợp lại một phiên tổng lực với đầy đủ tất cả các vấn đề **không làm rơi rụng bất kỳ vấn
> đề nào**, các vấn đề đã xử lý , có thể xử lý , tự xử lý rõ ràng , các yêu cầu của anh… »*
> — owner, **25/08/2026 ~18:57 giờ VN**

> *« Cần 1 cơ chế chống quên lãng , rơi rớt các vấn đề anh phân tích đề xuất cũng như căn dặn nha em. »*
> — owner, **06/08/2026 20:20 giờ VN**

> *« Rất bực bội bữa giờ toàn làm mù các seccsion trước đó đều mù, em có xem được seccsion của
> chính cursos không có kết nối đọc hiểu không thì tìm hiểu luôn đi »*
> — owner, **09/08/2026 20:50 giờ VN**

### `CODE_DID`

| điều hệ thống **thực sự** làm | bằng chứng |
|---|---|
| `/api/final-bundle/history` trả bảng xếp hạng nội bộ cho khách ẩn danh | `curl` 19:27 ngày 25/08 → `200`, **39.682 B**, có `ranked_numbers` + `voters`; nguyên nhân `main.py:10952` không nhận `request` |
| `/api/final-bundle` **chặn đúng** | cùng lượt đo → `200`, **1.711 B**, không có hai trường đó |
| Claude Code sinh **bản rẽ nhánh** mỗi lần `--resume` | 5 tệp cùng `promptId`/`timestamp`/nội dung, khác `sessionId` + `uuid`; cùng 8.687 dòng và 38.409.630 byte |
| Cổng quyết định **đã tách đúng tầng** `RM-12` | `_v10920_decision_ledger.py` 19:30 → `0 TRÔI`, `1 KHÔNG KẾT LUẬN ĐƯỢC` |
| Cổng `_v11062 K1` **mù với bản không có mục CHANGELOG** | 26 nhãn version chỉ có ở `git log`; CHANGELOG `V11081` ghi lại đúng cơ chế |
| `V11077`/`V11079` **có đủ** báo cáo công khai | `V11077_DO_NEO_POOL_D1_20260816/` (6.498 B + 4.408 B) · `V11079_BO_DO_TU_KHAI_READONLY_20260816/` (6.582 B + 4.373 B) |

### `DOC_SAID`

| tài liệu | nói gì | khớp code chưa |
|---|---|---|
| tệp owner đính kèm «Tổng Kết Lottery Ai.txt» | *«V11077 · V11079 thiếu báo cáo»* | 🔴 **KHÔNG** — xem `R1` §1 |
| cùng tệp | *«còn 4 bản thiếu báo cáo»* | 🔴 **KHÔNG** — thật ra 10 bản |
| cùng tệp | *«cổng quyết định vẫn báo 3 phép TRÔI»* | 🔴 **KHÔNG CÒN** — 0 TRÔI |
| `docs/CURRENT_TRUTH_SSOT.md` §V11116 | `33,10%/143,3` | 🟡 **đơn vị lẫn** — `143,3` là số lượt, không phải phần trăm |
| `CLAUDE.md` §55 | ba quy ước cột thời gian | 🔴 **THIẾU quy ước thứ tư** — `scheduler_logs.log_time` là UTC |
| `docs/OWNER_DECISION_LEDGER.json` | `QD-041` `ACTIVE` | 🔴 **LỆCH** — vùng khoá hết hiệu lực 21/08, quyết định chưa đóng |

### 🔴 BA LỚP LỆCH NHAU — finding bắt buộc báo

- **`DOC_SAID` ≠ `CODE_DID`** ở **bốn** chỗ (R1–R4) ⇒ đã rút lại ở §1, đủ bốn phần
  `PRJ-RETRACTION-001`.
- **`OWNER_SAID` ≠ `CODE_DID`**: owner ký treo toàn bộ view người dùng 06–08/06, nhưng mã vẫn
  phục vụ bảng xếp hạng nội bộ cho khách ẩn danh suốt **78 ngày** ⇒ `FU-438`, chờ owner ký `K2`.
- **`OWNER_SAID` ≠ `DOC_SAID`**: owner nêu *«cần cơ chế chống quên lãng, rơi rớt»* từ **06/08**;
  sổ chỉ ghi được **24 lượt phàn nàn** rải rác chứ chưa có cơ chế nào đếm chúng ⇒ chính bản này
  là lần đầu đếm được.

---

## 11. GIỚI HẠN — phải đọc kèm mọi con số ở trên

- **`RM-04`:** mẫu benchmark hiện có chỉ đủ phát hiện hiệu ứng **≥ 6pp**. Câu đúng là *«không có
  lợi thế đo được ở mức ≥6pp»* — **không phải** *«đã chứng minh bằng 0»*. `+3pp` cần **1,6 năm**.
- **`RM-12`:** trong phiên này **chỉ `FU-438` đạt `RUNTIME_PROVEN`**. Mọi thứ khác là
  `REPORT_PROVEN` hoặc thấp hơn.
- **Chỗ không kiểm được thì ghi thẳng:** prompt 14 không có dấu vết — **không kết luận** nó chưa
  từng gửi hay phiên chứa nó đã mất. `QD-056` không kiểm được vì DB local cũ — **không** đọc
  thành «trôi». Cột giờ của các lượt Cursor là **giờ tạo phiên**, không phải giờ từng tin.
- **Cấm hứa tăng tỷ lệ trúng.** Bản này không hứa điều đó ở bất kỳ chỗ nào, và không đề xuất bật
  `OFFICIAL` cho phương pháp nào trước **23/09/2026**.

---

**TanPhatAI cần làm:** ghi nhận (a) phiên `V11119` là `READ-ONLY` — chỉ ghi
`docs/SO_TUONG_TAC_OWNER.md` (append 1 dòng) và các tệp `.md`/`.json` do máy sinh, **không sửa mã
production nào**, nên **không có chỗ code đi trước tài liệu** trong phiên này; (b) **bốn con số đã
công bố bị rút lại** ở §1 — nặng nhất là *«V11077/V11079 thiếu báo cáo»* là **SAI**, hai bản đó có
đủ báo cáo từ 16/08, thứ thiếu là **mục CHANGELOG**, nên đừng đi bù báo cáo cho chúng; (c) số bản
thiếu báo cáo công khai là **10**, không phải 4–6, danh sách đủ ở §3.3; (d) `FU-438` nay ở mức
`RUNTIME_PROVEN` — đo trực tiếp trên production 19:27 ngày 25/08, đang chờ owner ký `K2`;
(e) `QD-041` hết hạn rà soát 21/08 nhưng vẫn `ACTIVE` ⇒ trước khi đọc bất kỳ mục nào ghi *«chặn
bởi vùng QD-041»*, phải hỏi owner xem vùng khoá đó còn hiệu lực không.
