# REPORT V11167 — DỌN NỢ QUẢN TRỊ + ĐÓNG VIỆC DANG DỞ

> **Ngày:** 06/09/2026 (VN) · `CURRENT_ACTOR = CLAUDE_CODE`
> **Hai workflow model NHẸ theo yêu cầu owner:** 11 agent (10 Sonnet + 1 Haiku) · 0 lỗi ·
> **2,1 triệu token · 45 phút** — so với 6,0 triệu/workflow Opus của V11164–V11166.
>
> **Ba con số nổi bật:** mục FU mồ côi **6 → 0** · việc dang dở **16/28 ĐÓNG ĐƯỢC** ·
> cổng trôi quyết định **SẬP 2 NGÀY → chạy sạch, 0 quyết định trôi**.
>
> `POOL_VERDICT = HOLD` · `MODEL_ACTION = BLOCKED` · `PROMPT_43_R1 = PARTIAL` ·
> `MATERIALIZATION_OPTION = B` (`QD-073`, `OWNER_LOCKED`)

---

## 1 · Tóm tắt

**Hai báo động P0 của V11166 hoá ra là báo động giả — và cả hai đều do chính agent gây ra.**

| báo động V11166 | sự thật hôm nay |
|---|---|
| 🔴 «`QD-047` đang TRÔI, bộ kiểm mù 6 ngày» | ✅ **`QD-047` 🟢 khớp 5/5, KHÔNG hề trôi.** Bộ kiểm sập vì **em viết `QD-073` sai kiểu dữ liệu ở V11165** |
| 🔴 «3 tệp production trên VPS lệch git HEAD» *(em nói giữa phiên này)* | ✅ **Chênh lệch 100% là kết thúc dòng.** Nội dung sau chuẩn hoá **giống hệt cả ba tệp** |

Cả hai đều là **lỗi công cụ của agent**, không phải lỗi hệ thống. Điều đáng nói: **cả hai đều chỉ
lộ ra khi có người đi kiểm lại thay vì tin con số cũ.**

**Việc thật đã đóng dứt điểm:** 6 mục FU mồ côi · 12 chỗ trích lại kết luận đã rút · 3 tệp điều
hướng lệch 15 ngày · 3 quyết định RM-19 · báo cáo `V11156` · 16/28 việc dang dở.

---

## 2 · Owner yêu cầu gì — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 06/09 ~09:0x | *«Tiếp theo là gì các agent khác đang chạy fable nên hút Token em điều phối các agent nhẹ hơn để xử lý tiếp cho xong đi em.»* | `ĐỔI_ƯU_TIÊN` | Chuyển toàn bộ sang **Sonnet/Haiku**, bỏ vòng phản biện LLM, thay bằng **bắt mỗi agent chạy cổng máy** | `ĐÃ_LÀM` |
| 06/09 ~09:2x | *«Các agent được điều đi trước đó có còn cần thiết không. Do fable hút Token quá nên có vẻ gián đoạn em rà soát điều tiếp theo với các agent model nhẹ hơn để làm tiếp các việc còn dang dở chưa xác định cần tìm hiểu nha e»* | `YÊU_CẦU` | Kiểm 16 workflow cũ — **đều đã chết, không tốn token**; gom **131 mục dang dở**; chạy đợt 5 cổng nhẹ | `ĐÃ_LÀM` |

**Trả lời câu hỏi của owner:** 16 workflow cũ **đều đã chết**, cái im lâu nhất 11 ngày, **không
còn tốn token**. Hai cái từng dở dang đã được thay thế xong, không cần chạy lại.

---

## 3 · Đào bới / phát hiện

### 3.1 · 🔴 `QD-047` KHÔNG hề trôi — bộ kiểm sập vì lỗi của agent

**Nguyên nhân gốc:** ở V11165 em ghi `QD-073` với `kiem_code` là **một chuỗi** thay vì
`list[dict]`. Vòng lặp `for k in kiem_code: k.get('mo_ta')` chạy trên **từng KÝ TỰ** của chuỗi và
vỡ `.get()` trên `str` ⇒ **`AttributeError` làm sập probe cho CẢ 75 quyết định**, không riêng
`QD-047`.

Đây đúng là cái *«KHÔNG ĐO ĐƯỢC — probe VPS trả về thiếu JSON_START»* em gặp ngày 04/09 và **đã từ
chối báo "0 TRÔI"**. Việc từ chối đó là đúng — nhưng em đã **không truy tiếp nguyên nhân**, và để
nó thành một báo động P0 sai trong V11166.

**Sau khi sửa kiểu dữ liệu** (giữ nguyên nội dung):

```
QD-047   🟢 khớp 5/5   Duyet toan bo lo trinh 10 ngay...
✓ KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI
⛔ 1 PHÉP KHÔNG KẾT LUẬN ĐƯỢC — đo trên DB local đã cũ (RM-01); cấm đọc thành TRÔI
```

Cổng cũng tự nhắc đúng RM-01: một phép **KHÔNG_KẾT_LUẬN_ĐƯỢC ≠ TRÔI**.

### 3.2 · 🔴 «VPS lệch git» — báo động giả, 100% là kết thúc dòng

Cổng đồng bộ `_v11143` (một trong 7 cổng chết) khi chạy tay **có cảnh báo thật**:
*«tệp production trên VPS LỆCH với git HEAD. Deploy lúc này có thể XOÁ MẤT bản vá chỉ tồn tại trên
VPS.»* Em đã nói với owner giữa phiên rằng đây là **lỗ hổng nghiêm trọng**. Kiểm lại thì:

| tệp | VPS | git HEAD | nội dung sau chuẩn hoá |
|---|---|---|---|
| `gpt_analyzer.py` | CR = **7.290** · 416.285 B | CR = 0 · 408.995 B | **GIỐNG HỆT** |
| `_v11162_lo3_lineage.py` | CR = **279** · 14.631 B | CR = 0 · 14.352 B | **GIỐNG HỆT** |
| `_materialize_shadow_promotion_scorecard.py` | CR = **575** · 28.273 B | CR = 0 · 27.698 B | **GIỐNG HỆT** |

Chênh lệch byte **đúng bằng số dòng** ⇒ VPS dùng **CRLF**, git dùng **LF**. **Không có bản vá nào
bị mất.** Git HEAD có đủ `regime_prompt_cho_luot` và `runtime_prompt_sha256` của V11160.

**Nhưng hệ quả thật vẫn còn:** cổng `_v11143` so **hash thô**, nên nó sẽ **luôn luôn** cảnh báo —
một cổng kêu sói mãi là cổng không ai tin. Và **nguồn của CRLF là chính em**: em deploy tệp từ
Windows. Cùng họ lỗi với ghi chú `python-write-newline-windows` đã có trong bộ nhớ.

### 3.3 · Dọn nợ quản trị — sáu cổng, tất cả có cổng máy chứng minh

| cổng | trước | sau | cổng máy |
|---|---|---|---|
| **FU mồ côi** | 6 mồ côi · 194 treo | **0 mồ côi** · 200 treo | `_v10958_fu_reader` trước/sau, exit 0 |
| **Trích lại kết luận đã rút** | **12 chỗ** ở 7 tệp báo cáo cũ | **0** | `_v11085` trên bản HEAD: bắt 6 vi phạm, exit 1 → sau khi sửa: **exit 0** |
| **3 tệp điều hướng** | kẹt **V11098**, lệch 15 ngày | **V11166 · 443 thư mục** | `_v11083 --thu` → `DIEU_HUONG_KHOP_THU_MUC=DAT`, exit 0 + một phép đối chiếu **độc lập** tự viết |
| **Sổ quyết định** | probe **SẬP** 2 ngày | **exit 0, SẠCH** · 3 QĐ RM-19 đồng bộ nhãn | `_v10920` + `_v11034`, cả hai exit 0 |
| **Nợ báo cáo** | 23 bản thiếu hẳn | **22** (`V11156` đã viết từ nguồn thật) | `_v10921_report_gate` trước/sau |
| **7 cổng chết** | chưa ai chạy | **chạy tay đủ 7**, có bảng mã thoát | 7 lệnh + output thật |

**Chi tiết đáng ghi:**

- **FU-449** trước đây **không có dòng `status` nào** trong thân (khối tiêu đề gộp) → nay `BLOCKED`,
  hạn 09/09 *(3 ngày — vì là hạ tầng P0 có rủi ro mất dữ liệu)*. **FU-450** → `OWNER_DECISION_NEEDED`,
  hạn 13/09 *(1 tuần — diễn tập trên bản sao, không rủi ro production)*.
- Con số quá hạn **152 → 154**, và cổng **tự tách hai nguyên nhân**: **+1 là trôi lịch tự nhiên**
  (chạy bản gốc chưa sửa tại ngày hôm nay đã ra 153), **+1 là `FU-445`** hạn 31/08 nay hết mồ côi
  nên lần đầu bị đếm. **Không phải do việc sửa gây ra.**
- 12 chỗ trích lại nằm ở **V11054 · V11057 · V11059 · V11081 · V11163** — đều là báo cáo cũ. Cách
  xử: **thêm nhãn đính chính ngay tại chỗ, giữ nguyên văn câu gốc** để người đọc thấy cả hai.
- Cổng `_v11085` **chỉ quét "báo cáo mới" qua `git status`** — giới hạn này được nói rõ và bù bằng
  một phép quét toàn kho **1.713 tệp** tự viết.
- `REPORT_V11156.md` dựng từ **commit `bd0ea86` + 2 commit phụ trợ + CHANGELOG + SSOT + HISTORY**,
  kèm **hộp rút lại đủ 4 phần** cho mục 3-càng vì phát hiện nó đã bị owner bác ngay hôm sau.
  **22 bản còn lại: KHÔNG viết** — vì `FU-444` đã có sẵn khuyến nghị *«KHÔNG BÙ»* đang chờ owner ký;
  viết đè lên một quyết định đang treo là vượt quyền.

### 3.4 · Đóng việc dang dở — 16/28 mục

**131 mục dang dở** được gom từ V11165–V11166 (100 «chưa trả lời được» · 13 `INDETERMINATE` ·
18 «cần thêm bằng chứng»). Năm cổng xử 28 mục nặng nhất:
**16 `DONG_DUOC` · 11 `VAN_TREO` · 1 `KHONG_DANG_LAM`**.

#### Đã đóng — và phần lớn là **báo động hạ nhiệt**, không phải lỗi mới

| mục | kết luận |
|---|---|
| **2 model shadow_only trong pool combo-super** | Mâu thuẫn **cấu trúc** có thật (pool không lọc `output_eligible`), nhưng **0/271 bundle trong 90 ngày** có chúng là voter thật. Cơ chế top-3 theo WR **chưa bao giờ chọn chúng** |
| **`gpt_analyzer.py:6449` đọc bảng chết 99 ngày** | ✅ **KHÔNG rò vào official.** Writer bị **tắt CHỦ Ý** bởi V10659 (31/05, có chú thích rõ). Reader xử lý rỗng đúng cách, và **chỉ chạy khi `lane_test_shadow_pack=True`** |
| **Trộn regime prompt cùng ngày** | Chỉ **1/31 ngày** (03/09 — đúng giai đoạn chuyển tiếp **trước** deploy V11160). Từ 04/09 ổn định 100% một regime |
| **OpenRouter vượt timeout 300s** | ✅ **Không phải lỗi.** Là **retry cộng dồn có chủ ý**: 4 lần thử × 300s + backoff 5/15/30s. Không request đơn nào vượt 300s |
| **Reasoning ăn 96,0% trần đầu ra** | Có thật, tái lập được (62.911/65.536), nhưng **chưa lượt nào hỏng vì nó** ⇒ đúng là **rủi ro tiềm ẩn** |
| **Số token «không đo được»** | ✅ **Đo được** — đọc `usage` của provider cho lượt **đã chạy**. Không còn `INDETERMINATE` |
| **7 lượt lệch `ctx_pack` trong nhóm shadow** | Tìm đúng 7 lượt, **cả 7 đều RÚT NGẮN**. **Bác bỏ** giả thuyết «trôi theo giờ gọi» của phiên trước |
| **«Chỉ 2 cổng có sổ điểm danh»** | ✅ Thật ra **10 cổng chứng minh được đã chạy**; 604/614 tệp còn lại là **`INDETERMINATE`**, không phải «chưa từng chạy» |
| **3 nhãn job im 117–120 ngày** | ✅ Cả ba có lời giải: script test tay một lần · nhãn log từ sự cố V105.13 · hàm còn sống chỉ im vì không có sự cố. **Không job nào bị âm thầm gỡ** |
| **`FU-419` D-1 cross-region tail pool** | ✅ đã lên production |
| **4 tệp shadow tự định nghĩa lại `DEGRADED_LIVE_DAY`** | ✅ xác nhận: chúng dùng ngưỡng cứng `m >= 15`, **không đọc `day_governance`** ⇒ mọi số liệu từ chúng **không so được** với sổ chính |

#### 🔴 Còn treo — và một mục đổi bản chất

**`79` bundle (KHÔNG phải 78 — RM-11) có `bach_thu` ≠ `ranked_numbers[0]`.**
**Không phải lỗi tính toán.** **50/79** giải thích đầy đủ bằng **4 cơ chế override hợp lệ owner đã
duyệt** (V10640 MN đang hoạt động: 27/32 khớp; V10767+V10789 MB và V10790 MT đã **TẮT từ 01/08**:
15/25 + 8/22 khớp qua bảng audit champion/challenger).

Cơ chế thật: các override đổi biến `bach_thu` **SAU KHI** biến `ranked` đã dùng để xây
`ranked_numbers`/`score_breakdown` (`main.py:10225` vs `:10465`), và **`main_selection_reason` là
một CHUỖI CỨNG** (`:10379`) **không bao giờ được cập nhật** để ghi override nào đã chạy.

⇒ **Đây là LỖ HỔNG PROVENANCE, không phải lỗi số.** Và **29/79 còn lại** (MN 5 · MB 10 · MT 14)
tập trung tháng 6/2026, **TRƯỚC cả ngày ba module V10767/89/90 ra đời** ⇒ **có thể có một cơ chế
thứ 5 chưa xác định**.

| mục còn treo | cần gì để đóng |
|---|---|
| 79 bundle — cơ chế thứ 5 | truy mã tháng 6/2026 |
| `ctx_pack` lệch 1.472 ký tự (05/09 MT) | phải gọi `build_context_pack()` — luật phiên cấm |
| Phase 15 as-of leak toàn lịch sử | mở rộng quét ngoài 30 ngày |
| 65 ca chép sai số của model | bị nhiễu bởi lỗi nền «prompt đã phục vụ không tái dựng được» |
| TOTAL thua trung bình model thành phần | n chưa đủ |
| combo-super cứu/phá | cần thêm bundle |
| 85/66/27 bảng im | **không tái lập được** bộ số gốc bằng phương pháp độc lập (ra 66/79 và 8 bảng/7 tệp) |

#### Phân loại 131 mục *(Haiku — việc cơ học, model rẻ nhất)*

| nhóm | n | ghi chú |
|---|---|---|
| **đã giải quyết** | **22** | 8 bị phủ nhận · 9 đã quan sát · 5 là **kết quả thiết kế**, không phải thiếu sót |
| cần thêm bằng chứng | 91 | 66 giả thuyết · 15 thiếu dữ liệu · 7 metadata · 2 viewer-freeze · 1 trùng |
| **cần owner** | **6** | gồm: chính sách MB `min_bt/min_wr` · có được đo hiệu ứng dự đoán không · **gán P0–P3 cho 194 mục treo** |
| **cần công cụ** | **6** | **tất cả đều là đếm token** — chỉ cần `pip install tiktoken` trên VPS |
| không đáng làm | 4 | ngoài phạm vi giai đoạn 1 |

---

## 4 · Hướng xử lý và vì sao chọn

### 4.1 · Vì sao bỏ vòng phản biện LLM

Owner nói Fable hút token. Em bỏ **32 agent phản biện** và thay bằng **bắt mỗi agent chạy cổng máy
và dán mã thoát**. Cổng máy **chặt hơn** agent kiểm agent vì nó cho **mã thoát**, không cho ý kiến.
Kết quả: 2,1 triệu token cho 11 agent, so với 6,0 triệu cho 40 agent Opus — **rẻ hơn ~5,7 lần trên
mỗi agent** mà vẫn bắt được hai báo động giả.

### 4.2 · 🔴 RÚT LẠI — `PRJ-RETRACTION-001`

#### R21 — «`QD-047` đang TRÔI và bộ kiểm trôi đã MÙ 6 NGÀY»

- **Chỗ gốc:** `REPORT_V11166.md` §1, §3.7 và §9 (P0 số 8) · `CONVERSATION_CONTEXT_V11166` ·
  `CHANGELOG` V11166 · `FOLLOW_UP_TRACKER` · commit công khai `b6aa6ae`/`0429ffd`
- **Nguyên văn câu sai:** *«`QD-047` đang `TRÔI` và bộ kiểm trôi đã MÙ 6 NGÀY — luật của chính sổ
  nói phải DỪNG»*
- **Điều đúng:** **`QD-047` KHÔNG trôi.** Sau khi sửa kiểu dữ liệu `QD-073.kiem_code`
  (string → `list[dict]`), cổng chạy `exit 0`: **`QD-047 🟢 khớp 5/5`** và
  **`✓ KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI`**. Bộ kiểm không «mù» — nó **SẬP** với `AttributeError`
  cho **cả 75 quyết định**, do **agent ghi `QD-073` sai kiểu ở V11165**.
- **Quyết định đã dựa trên:** đây được liệt là **P0 số 8** trong V11166 và đưa vào việc chặn ở owner.
  **Việc đó nay HUỶ.**

#### R22 — «78 bundle có `bach_thu` khác `ranked_numbers[0]`»

- **Chỗ gốc:** `REPORT_V11166.md` §3.5 · `evidence/GATE_s7-chat-luong.md`
- **Điều đúng:** **79/571**, không phải 78 (RM-11). Và bản chất khác hẳn: **50/79 là override hợp
  lệ owner đã duyệt**; lỗi thật là **`main_selection_reason` bị khoá cứng ở `main.py:10379`**
  ⇒ **lỗ hổng provenance**, không phải lỗi tính. **29/79 chưa giải thích được.**

#### R23 — «3 tệp production trên VPS lệch git HEAD» *(em nói với owner trong phiên này)*

- **Nguyên văn câu sai:** *«Xác nhận lỗ hổng nghiêm trọng: 3/10 tệp production trên VPS KHÁC git HEAD»*
- **Điều đúng:** chênh lệch **100% là kết thúc dòng** (VPS CRLF, git LF); byte chênh **đúng bằng số
  dòng**; nội dung sau chuẩn hoá **giống hệt cả ba tệp**. **Không bản vá nào bị mất.**
  Em đã tự sửa ngay trong cùng lượt, nhưng owner đã đọc câu sai nên ghi lại đây.

---

## 5 · Đã làm gì

| việc | TRƯỚC | SAU |
|---|---|---|
| FU mồ côi | 6 | **0** |
| trích lại kết luận đã rút | 12 chỗ / 7 tệp | **0** |
| 3 tệp điều hướng | V11098, lệch 15 ngày | **V11166 · 443 thư mục** |
| cổng trôi quyết định | **SẬP 2 ngày** | **exit 0, sạch** |
| QĐ RM-19 | 5 ACTIVE dù đã bị thay | **3 đồng bộ nhãn** `SUPERSEDED_BY_QD066`; 2 chờ owner |
| báo cáo thiếu | 23 | **22** (`V11156` viết từ nguồn thật) |
| briefing đầu phiên | im 20 ngày | **đã sinh lại** (194 treo / 153 quá hạn) |
| 7 cổng chết | chưa ai chạy | **chạy tay đủ 7, có bảng mã thoát** |
| việc dang dở | 131 mục chưa phân loại | **16 đóng · 22 đã giải quyết từ trước · phân loại đủ 131** |
| rút lại | 20 ca | **23 ca** |
| production | — | **0 ghi · 0 deploy · 0 restart** |

---

## 6 · Cổng kiểm — xác minh

| cổng | kết quả |
|---|---|
| `_v10958_fu_reader` trước/sau | mồ côi **6 → 0**, exit 0 cả hai lần |
| `_v11085_cong_rut_lai` trên bản HEAD | **exit 1**, bắt đúng 6 vi phạm |
| `_v11085_cong_rut_lai` sau khi sửa | **exit 0 · `PRJ_RETRACTION=SACH`** |
| `_v11083_sinh_dieu_huong --thu` | **`DIEU_HUONG_KHOP_THU_MUC=DAT`**, exit 0 |
| đối chiếu điều hướng **độc lập** (tự viết) | 443 thư mục · V11166 · **KHỚP**, exit 0 |
| `_v10920_decision_ledger` | **exit 0** · `✓ KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI` |
| `_v11034_kiem_cheo_quyet_dinh` | exit 0, sạch |
| `_v10921_report_gate` trước/sau | 23 → **22** bản thiếu |
| 7 cổng chết chạy tay | đủ 7, có mã thoát + output |
| `_v11062_nang_version --kiem` | **ĐẠT** |
| production `neo558` | **khớp** · 6 hash tệp serve **không đổi** · PID `3370750` · `NRestarts 0` |

---

## 7 · Vướng vấp

| # | vấp | gỡ |
|---|---|---|
| 1 | 🔴 **Ghi `QD-073.kiem_code` sai kiểu ở V11165** → sập cổng trôi quyết định **2 ngày**, đẻ ra một P0 giả trong V11166 | sửa kiểu, giữ nguyên nội dung. **Bài học: khi cổng báo «KHÔNG ĐO ĐƯỢC», phải truy nguyên nhân ngay, không chỉ từ chối kết luận** |
| 2 | 🔴 **Nói với owner «lỗ hổng nghiêm trọng: VPS lệch git»** trước khi kiểm chiều lệch | tự sửa trong cùng lượt; rút lại ở **R23**. Bài học: con số quá đều (7290 dòng / 7290 byte) là dấu hiệu kết thúc dòng |
| 3 | **Deploy từ Windows đẻ CRLF trên VPS** ⇒ cổng đồng bộ **luôn báo lệch** | cùng họ với ghi chú đã có trong bộ nhớ; cần chuẩn hoá LF khi deploy |
| 4 | **Agent tự bắt bẫy đếm-chuỗi-thô của chính nó**: lần dò đầu cho «2 model shadow_only» ra *«184/271 bundle có nhắc tên»* — SAI, vì `model_wr/model_bt` liệt kê **cả 27 model** để theo dõi. Đọc đúng `ranked_numbers[*].voters` mới ra **0/271** | ghi lại đúng tinh thần RM-09/RM-10 |
| 5 | **Đề bài của chính em ghi «10 lượt cùng lane/miền/ngày»** — số thật là **9** | không đổi kết luận, nhưng phải sửa khi trích lại |

---

## 8 · Gỡ về

Mọi thay đổi đều là **tài liệu**, có backup trước khi sửa
(`backups/FOLLOW_UP_TRACKER.md.pre_v11167_cong1`, `backups/OWNER_DECISION_LEDGER.json.pre_v11167`)
và ghi bằng `_doc_prepend.prepend()` — **không dùng `open(p,"w")`** (§63).
Tệp sau khi sửa đều **DÀI HƠN** bản cũ.

**Production: 0 ghi · 0 deploy · 0 restart** — không có gì để gỡ.

---

## 9 · Theo dõi tiếp

### Chặn ở owner — **năm P0 hạ tầng của V11166 vẫn nguyên**

1. **Backup ngoài máy** · 2. **Swap + `OOMScoreAdjust`** · 3. **Tắt SSH root mật khẩu + `fail2ban`**
· 4. **Nối lại 7 cổng vào `.claude/settings.json`** · 5. **Cảnh báo đĩa + hồi sinh `system_alerts`**

*(P0 số 8 cũ — «`QD-047` trôi» — **đã huỷ**, xem R21.)*

### Chặn ở owner — mới phát sinh từ phiên này

| # | việc |
|---|---|
| 6 | **Ký `FU-444`**: xác nhận *«KHÔNG BÙ 22 báo cáo trước V11088, khai thành khoảng trống lịch sử»* — hoặc nói rõ muốn bù bản nào |
| 7 | **`QD-022`/`QD-026`**: có tách thành phần-đã-thay / phần-còn-hiệu-lực không (hiện `thay_boi_mot_phan`) |
| 8 | **16 quyết định ACTIVE quá hạn rà soát** *(đã giảm từ 18)*, **8 cái đáo hạn 06/09** — agent **không tự gia hạn** |
| 9 | **Bật 2 adapter mới** (`deploy_guard`, `deploy_ledger`) vào `.claude/settings.json` — đổi hành vi Bash-tool toàn phiên |
| 10 | **Cho phép commit+push kho công khai** — luật cấm của phiên trước không nói rõ có bao gồm kho báo cáo hay không |
| 11 | **Gán mức P0–P3 cho 194 mục treo** — sổ theo dõi hiện **không có trường ưu tiên** |

### Agent làm tiếp được

| # | việc |
|---|---|
| 12 | **`pip install tiktoken`** trên VPS ⇒ đóng **6 mục** cùng lúc (tất cả đều là đếm token) |
| 13 | **`main_selection_reason` khoá cứng** (`main.py:10379`) — lỗ hổng provenance của 79 bundle |
| 14 | **Truy cơ chế thứ 5** cho 29/79 bundle tháng 6/2026 |
| 15 | **Chuẩn hoá LF khi deploy** để cổng `_v11143` hết báo lệch giả |
| 16 | **4 tệp shadow dùng ngưỡng cứng `m >= 15`** thay vì đọc `day_governance` |

---

## 10 · Nguồn ba lớp (§62)

### `OWNER_SAID`
- 06/09 ~09:0x — *«…em điều phối các agent nhẹ hơn để xử lý tiếp cho xong đi em.»*
- 06/09 ~09:2x — *«Các agent được điều đi trước đó có còn cần thiết không… làm tiếp các việc còn
  dang dở chưa xác định cần tìm hiểu nha e»*

### `CODE_DID`
- `docs/OWNER_DECISION_LEDGER.json` — `QD-073.kiem_code` **string → `list[dict]`**, `thay_the` `"" → []`
- `main.py:10225` vs `:10465` — override đổi `bach_thu` sau khi `ranked` đã dùng
- `main.py:10379` — `main_selection_reason` là **chuỗi cứng**
- `scheduler.py:9024-9031` — V10659 **tắt CHỦ Ý** writer của `v101_region_source_pool_top5_shadow`
- `scheduler.py:7690` — `lane_test_shadow_pack=True` **chỉ** trong luồng `shadow_auto_eval`

### `RUNTIME_DID`
- `_v10920_decision_ledger` **exit 0** · `QD-047 🟢 khớp 5/5` · `✓ KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI`
- `_v11085` bản HEAD **exit 1** (6 vi phạm) → sau khi sửa **exit 0**
- `_v11083 --thu` → `DIEU_HUONG_KHOP_THU_MUC=DAT`
- VPS vs git: CR **7.290 / 279 / 575** vs **0** — nội dung chuẩn hoá **giống hệt**
- 0/271 bundle có 2 model shadow_only là voter thật

### `DOC_SAID`
- `REPORT_V11166.md` «`QD-047` đang TRÔI» — **`DOC_SAID` ≠ `RUNTIME_DID`**, rút ở **R21**
- `REPORT_V11166.md` «78 bundle» — rút ở **R22**
- `FU-444` đã có sẵn khuyến nghị *«KHÔNG BÙ»* — agent **không viết đè** lên quyết định đang treo

### `NOT_VERIFIED`
- cơ chế thứ 5 của 29/79 bundle · nguyên nhân `ctx_pack` lệch 1.472 ký tự · 604/614 cổng
  `INDETERMINATE` · bộ số 85/66/27 bảng im **không tái lập được**

### `RETRACTED`
- **R21** «`QD-047` trôi» · **R22** «78 bundle» · **R23** «VPS lệch git»
- (còn hiệu lực) `RL-001`…`RL-020`

---

## 11 · Commit

| | |
|---|---|
| private HEAD trước | `6c9001e2dcb10c1adaf7cecd5c545ad791911f8f` |
| public HEAD trước | `0429ffdc4fddc2992fe0fdf25c995a3ff6c0d5e1` |
| `governance_seq` | 482 → **483** |
| **private commit V11167** | **`ad2bfd51362f2d84c65afba1e3d20e46376ec06f`** — `6c9001e..ad2bfd5`, 12 tệp |
| **public commit V11167** | **`d41c4c3932c1100514d517560f9a36e1d6b5506e`** — `0429ffd..d41c4c3` |
| cổng `_v11062 --kiem` | ✅ **ĐẠT** |
| cổng `PRJ-RETRACTION-001` | ✅ **`SACH`** |
| cổng `PRJ-SELECTION-WINDOW-001` | ✅ **`SACH`** *(đã chặn 23 chỗ trong V11054 — sửa nội dung, không bỏ qua)* |

---

TanPhatAI cần làm: ghi **`V11167`** — `governance_seq 483`, công khai bản này. Ghi **hai workflow model NHẸ theo yêu cầu owner: 11 agent (10 Sonnet + 1 Haiku), 2,1 triệu token, 45 phút — rẻ hơn ~5,7 lần mỗi agent so với Opus**, và **bỏ vòng phản biện LLM, thay bằng bắt mỗi agent chạy CỔNG MÁY và dán mã thoát**. Ghi **HAI BÁO ĐỘNG P0 CỦA V11166 LÀ BÁO ĐỘNG GIẢ, cả hai do chính agent gây ra**: ① **`QD-047` KHÔNG hề trôi** — cổng chạy `exit 0`, `QD-047 🟢 khớp 5/5`, `✓ KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI`; bộ kiểm **SẬP** vì agent ghi `QD-073.kiem_code` **sai kiểu** (string thay vì `list[dict]`) ở V11165, làm `AttributeError` cho **cả 75 quyết định** ⇒ **P0 số 8 của V11166 nay HUỶ**; ② **«3 tệp production VPS lệch git» là 100% kết thúc dòng** (CR 7.290/279/575 vs 0), nội dung sau chuẩn hoá **giống hệt**, **không bản vá nào bị mất** — nhưng cổng `_v11143` so hash thô nên **luôn báo lệch giả**, và nguồn CRLF là **deploy từ Windows của chính agent**. Ghi **BA CA RÚT LẠI R21–R23**. Ghi **DỌN NỢ có cổng máy chứng minh từng cái**: FU mồ côi **6 → 0** · **12 chỗ trích lại kết luận đã rút → 0** (cổng bản HEAD exit 1 bắt 6 vi phạm, sau khi sửa exit 0) · 3 tệp điều hướng **V11098 → V11166/443** · **3 QĐ RM-19** đồng bộ nhãn · báo cáo thiếu **23 → 22** (`V11156` dựng từ commit `bd0ea86` + CHANGELOG + SSOT + HISTORY, kèm hộp rút lại đủ 4 phần) · **briefing sinh lại sau 20 ngày** · **chạy tay đủ 7 cổng chết**. Ghi **ĐÓNG 16/28 VIỆC DANG DỞ**, phần lớn là **báo động hạ nhiệt**: 2 model shadow_only **0/271 bundle** từng thắng phiếu · `gpt_analyzer.py:6449` **KHÔNG rò vào official** (chỉ chạy khi `lane_test_shadow_pack=True`) · OpenRouter «vượt 300s» là **retry cộng dồn có chủ ý** · trộn regime chỉ **1/31 ngày** rồi ổn định · **số token đo được** từ `usage` provider · **10 cổng** chứng minh được đã chạy (không phải 2). Ghi **MỘT MỤC ĐỔI BẢN CHẤT: 79 bundle (không phải 78 — RM-11) có `bach_thu` ≠ `ranked[0]` — 50/79 là OVERRIDE HỢP LỆ owner đã duyệt; lỗi thật là `main_selection_reason` KHOÁ CỨNG ở `main.py:10379` ⇒ LỖ HỔNG PROVENANCE, không phải lỗi tính; 29/79 tập trung tháng 6/2026 TRƯỚC khi ba module override ra đời ⇒ có thể có cơ chế thứ 5 chưa xác định**. Ghi **phân loại đủ 131 mục dang dở**: 22 đã giải quyết · 91 cần thêm bằng chứng · **6 cần owner** · **6 cần công cụ (tất cả chỉ cần `pip install tiktoken`)** · 4 không đáng làm. Ghi **NĂM P0 HẠ TẦNG CỦA V11166 VẪN NGUYÊN** và **sáu việc mới chặn ở owner**, trong đó có **ký `FU-444`** (không bù 22 báo cáo cũ) và **gán P0–P3 cho 194 mục treo** (sổ hiện không có trường ưu tiên). **Code KHÔNG đi trước tài liệu** — 0 ghi production, 0 deploy, 0 restart; mọi thay đổi là tài liệu, có backup, ghi bằng `prepend()`, tệp sau đều DÀI HƠN. **Không mở Prompt 44. Không mở FU mới. Không mở Plan mới.** `POOL_VERDICT` giữ **`HOLD`** · `MODEL_ACTION` giữ **`BLOCKED`** · `PROMPT_43_R1` giữ **`PARTIAL`**.
