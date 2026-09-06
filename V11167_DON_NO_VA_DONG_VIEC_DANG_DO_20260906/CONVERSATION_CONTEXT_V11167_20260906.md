# CONVERSATION CONTEXT — V11167 · 06/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `CURRENT_ACTOR = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| ~09:0x | *«Tiếp theo là gì các agent khác đang chạy fable nên hút Token em điều phối các agent nhẹ hơn để xử lý tiếp cho xong đi em.»* | `ĐỔI_ƯU_TIÊN` | Chuyển toàn bộ agent sang **Sonnet/Haiku**; **bỏ vòng phản biện LLM**, thay bằng **bắt mỗi agent chạy cổng máy và dán mã thoát**; tách quyền sở hữu tệp để hai workflow không giẫm chân | `ĐÃ_LÀM` |
| ~09:2x | *«Các agent được điều đi trước đó có còn cần thiết không. Do fable hút Token quá nên có vẻ gián đoạn em rà soát điều tiếp theo với các agent model nhẹ hơn để làm tiếp các việc còn dang dở chưa xác định cần tìm hiểu nha e»* | `YÊU_CẦU` | Kiểm **16 workflow cũ** — đều đã chết, không tốn token; gom **131 mục dang dở** từ V11165–V11166; chạy đợt 5 cổng nhẹ | `ĐÃ_LÀM` |

**Trả lời trực tiếp câu hỏi của owner:** **không**, các agent trước **không còn cần thiết và cũng
không còn tốn token** — 16 workflow đều đã chết, cái im lâu nhất 11 ngày. Hai cái từng dở dang
(`wf_3eea8ad4` 0 kết quả, `wf_4e2f2d34` 18/40) đều **đã được thay thế xong**, không phải chạy lại.

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| chuyển sang model nhẹ | 🟢 **11 agent (10 Sonnet + 1 Haiku)** · 0 lỗi · **2,1 triệu token** · 45 phút |
| so với trước | Opus: 40 agent · 6,0 triệu token/workflow ⇒ **rẻ hơn ~5,7 lần trên mỗi agent** |
| dọn nợ quản trị | 🟢 6/6 cổng, mỗi cổng có **cổng máy** chứng minh |
| đóng việc dang dở | 🟢 **16/28** đóng được · 11 còn treo · 1 không đáng làm |
| phân loại 131 mục | 🟢 22 đã giải quyết · 91 cần bằng chứng · 6 cần owner · 6 cần công cụ · 4 bỏ |
| rút lại | 🔴 **3 ca mới** `RL-021`…`RL-023` |
| production | 🟢 **0 ghi · 0 deploy · 0 restart** |

---

## 3 · Điều đáng nói nhất — hai P0 của hôm qua là báo động giả, cả hai do agent gây ra

**① `QD-047` không hề trôi.** V11166 xếp nó là **P0 số 8** và đưa vào danh sách việc chặn ở owner.
Sự thật: **cổng bị SẬP**, không phải «mù». Nguyên nhân là ở V11165 chính agent ghi
`QD-073.kiem_code` **sai kiểu** — một chuỗi thay vì `list[dict]` — nên vòng lặp
`for k in kiem_code: k.get(...)` chạy trên **từng ký tự** và vỡ `AttributeError` cho **cả 75 quyết
định**. Sau khi sửa kiểu: `exit 0`, `QD-047 🟢 khớp 5/5`, `✓ KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI`.

Đáng nói hơn: ngày 04/09 agent **đã thấy** cổng báo *«KHÔNG ĐO ĐƯỢC»* và **đã đúng khi từ chối báo
"0 TRÔI"** — nhưng **không truy tiếp nguyên nhân**, để nó thành một P0 sai trong báo cáo công khai.
**Từ chối kết luận là đúng; dừng ở đó là chưa đủ.**

**② «VPS lệch git HEAD» — 100% là kết thúc dòng.** Giữa phiên này agent nói với owner đây là
*«lỗ hổng nghiêm trọng»*. Kiểm lại: CR **7.290 / 279 / 575** vs **0**, chênh byte **đúng bằng số
dòng**, nội dung sau chuẩn hoá **giống hệt cả ba tệp**. **Không bản vá nào bị mất.**

Dấu hiệu lẽ ra phải thấy ngay: **7290 dòng khác / 7290 byte chênh** là con số quá đều để là nội dung.

---

## 4 · Điều đáng nói thứ hai — phần lớn việc dang dở là báo động hạ nhiệt

Trong 16 mục đóng được, **6 mục hoá ra không phải lỗi**:

- 2 model shadow_only trong pool combo-super: mâu thuẫn **cấu trúc** có thật, nhưng **0/271 bundle**
  trong 90 ngày từng thắng phiếu.
- `gpt_analyzer.py:6449` đọc bảng chết 99 ngày: **không rò vào official** — writer bị tắt **chủ ý**
  bởi V10659, reader chỉ chạy khi `lane_test_shadow_pack=True`.
- «OpenRouter vượt 300s»: **retry cộng dồn có chủ ý**, không request đơn nào vượt.
- Trộn regime prompt: chỉ **1/31 ngày**, đúng giai đoạn chuyển tiếp trước deploy V11160.
- «Số token không đo được»: **đo được** từ `usage` của provider.
- «Chỉ 2 cổng có sổ điểm danh»: thật ra **10 cổng** chứng minh được đã chạy.

**Một mục thì đổi bản chất theo hướng nghiêm túc hơn:** **79 bundle** (không phải 78) có
`bach_thu ≠ ranked[0]` — **50/79 là override hợp lệ owner đã duyệt**, lỗi thật là
**`main_selection_reason` khoá cứng** ở `main.py:10379` ⇒ **lỗ hổng provenance**. **29/79** tập
trung tháng 6/2026, **trước cả ngày ba module override ra đời** ⇒ có thể có **cơ chế thứ 5**.

---

## 5 · Vấp ở đâu

| # | vấp | gỡ |
|---|---|---|
| 1 | 🔴 **Ghi `QD-073.kiem_code` sai kiểu ở V11165** → sập cổng 2 ngày, đẻ một P0 giả | sửa kiểu, giữ nội dung. **Bài học: cổng báo «KHÔNG ĐO ĐƯỢC» thì phải truy nguyên nhân, không chỉ từ chối kết luận** |
| 2 | 🔴 **Nói «lỗ hổng nghiêm trọng» trước khi kiểm chiều lệch** | tự sửa trong cùng lượt; rút ở `RL-023` |
| 3 | **Deploy từ Windows đẻ CRLF trên VPS** ⇒ cổng đồng bộ **báo lệch giả vĩnh viễn** | cùng họ với ghi chú đã có trong bộ nhớ |
| 4 | **Agent tự bắt bẫy đếm-chuỗi-thô của chính nó**: lần dò đầu ra *«184/271 bundle»* vì `model_wr/model_bt` liệt kê **cả 27 model** để theo dõi; đọc đúng `ranked_numbers[*].voters` mới ra **0/271** | đúng tinh thần RM-09/RM-10 |
| 5 | **Đề bài của chính agent ghi «10 lượt»** — số thật là **9** | không đổi kết luận, nhưng phải sửa khi trích lại |
| 6 | **Cổng cửa sổ chọn chặn 23 chỗ** trong báo cáo cũ V11054 (bị quét vì vừa được thêm nhãn đính chính) | **sửa nội dung**, thêm ghi chú «cố ý trích một cửa sổ» dẫn chỗ có đủ bộ — **không** dùng `BO_QUA_CONG_COMMIT` |

---

## 6 · Trạng thái cuối

| | |
|---|---|
| FU mồ côi | 🟢 **6 → 0** |
| trích lại kết luận đã rút | 🟢 **12 → 0** |
| 3 tệp điều hướng | 🟢 **V11098 → V11166 / 443 thư mục** |
| cổng trôi quyết định | 🟢 **SẬP → `exit 0`, 0 quyết định trôi** |
| nợ báo cáo | 🟡 **23 → 22** bản thiếu hẳn |
| briefing đầu phiên | 🟢 **sinh lại sau 20 ngày** |
| việc dang dở | 🟡 **16/28 đóng · 11 treo · 1 bỏ** |
| production | 🟢 `neo558` khớp · 6 hash serve không đổi · PID `3370750` · `NRestarts 0` |
| rút lại | **23 ca** (`RL-001`…`RL-023`) |

---

## 7 · Cho TanPhatAI đọc tiếp

**Năm P0 hạ tầng của V11166 vẫn nguyên** (backup ngoài máy · swap · SSH root · nối lại 7 cổng ·
cảnh báo đĩa). **P0 số 8 cũ — «`QD-047` trôi» — đã HUỶ** vì là báo động giả.

**Sáu việc mới chặn ở owner:** ký `FU-444` (không bù 22 báo cáo cũ) · `QD-022`/`QD-026` có tách
phần-đã-thay không · 16 QĐ ACTIVE quá hạn rà soát (8 cái đáo hạn 06/09) · bật 2 adapter vào
`.claude/settings.json` · cho phép push kho công khai · **gán P0–P3 cho 194 mục treo** (sổ hiện
**không có trường ưu tiên**).

**Việc rẻ nhất, đóng 6 mục cùng lúc:** `pip install tiktoken` trên VPS.

**Bốn con số dễ bị trích sai:**
- **«`QD-047` trôi»** — **SAI**, đã rút ở `RL-021`.
- **«78 bundle»** — số đúng là **79**, và 50/79 là override hợp lệ (`RL-022`).
- **«VPS lệch git»** — **SAI**, chỉ là CRLF vs LF (`RL-023`).
- **«152 quá hạn»** — nay **154**, trong đó **+1 là trôi lịch tự nhiên**, không phải do sửa nhãn.

---

TanPhatAI cần làm: ghi **`V11167`** — `governance_seq 483`, công khai bản này cùng `REPORT_V11167.md` và `V11156_DONG_BON_MON_NO_20260903/`. Ghi **11 agent model nhẹ (10 Sonnet + 1 Haiku), 2,1 triệu token, rẻ hơn ~5,7 lần mỗi agent so với Opus**, và **bỏ phản biện LLM thay bằng cổng máy + mã thoát**. Ghi **HAI BÁO ĐỘNG P0 CỦA V11166 LÀ GIẢ, cả hai do chính agent**: `QD-047` **không trôi** (cổng SẬP vì agent ghi `QD-073` sai kiểu ở V11165 ⇒ **P0 số 8 HUỶ**), và «VPS lệch git» là **100% kết thúc dòng**. Ghi **BA CA RÚT LẠI `RL-021`…`RL-023`**. Ghi **dọn nợ có cổng máy chứng minh từng cái**: FU mồ côi **6 → 0** · trích lại đã rút **12 → 0** · điều hướng **V11098 → V11166/443** · nợ báo cáo **23 → 22** (`V11156` dựng từ nguồn thật) · briefing sinh lại sau 20 ngày · chạy tay đủ 7 cổng chết. Ghi **đóng 16/28 việc dang dở, phần lớn là BÁO ĐỘNG HẠ NHIỆT** (2 model shadow_only **0/271** · `:6449` **không rò official** · OpenRouter là **retry có chủ ý** · số token **đo được** · **10 cổng** chứng minh đã chạy). Ghi **một mục ĐỔI BẢN CHẤT: 79 bundle (không phải 78) — 50/79 là override HỢP LỆ, lỗi thật là `main_selection_reason` khoá cứng ở `main.py:10379` ⇒ LỖ HỔNG PROVENANCE; 29/79 có thể do cơ chế thứ 5 chưa xác định**. Ghi **phân loại đủ 131 mục dang dở** và **việc rẻ nhất là `pip install tiktoken` đóng 6 mục cùng lúc**. **Code KHÔNG đi trước tài liệu** — 0 ghi production, 0 deploy, 0 restart; mọi thay đổi là tài liệu, có backup, ghi bằng `prepend()`, tệp sau đều DÀI HƠN. **Không mở Prompt 44. Không mở FU mới. Không mở Plan mới.**
