# REPORT V11168 — ĐÓNG VIỆC DANG DỞ CỦA V11165–V11166

> **Ngày:** 06/09/2026 (VN) · `CURRENT_ACTOR = CLAUDE_CODE`
> **Model nhẹ theo yêu cầu owner:** 5 agent (4 Sonnet + 1 Haiku) · 0 lỗi · **1,04 triệu token · 23 phút**
> **Kết quả: 16/28 mục ĐÓNG ĐƯỢC · 11 còn treo · 1 không đáng làm**
>
> `POOL_VERDICT = HOLD` · `MODEL_ACTION = BLOCKED` · `PROMPT_43_R1 = PARTIAL`

---

## 1 · Tóm tắt

**Phần lớn việc dang dở hoá ra là báo động hạ nhiệt, không phải lỗi mới.** Trong 16 mục đóng được,
**6 mục** khi đo thật thì **không phải lỗi**: mâu thuẫn cấu trúc chưa bao giờ xảy ra, «rò rỉ» thực
ra bị chặn bởi một cờ, «vượt timeout» là retry có chủ ý, «không đo được» thì đo được.

Nhưng **một mục đổi bản chất theo hướng nghiêm túc hơn**: 79 bundle có bạch thủ khác
`ranked_numbers[0]` **không phải lỗi tính toán** — phần lớn là **override hợp lệ owner đã duyệt**,
và lỗi thật là một **lỗ hổng truy vết** khiến không ai biết cơ chế nào đã quyết định số cuối cùng.

---

## 2 · Owner yêu cầu gì — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 06/09 ~09:2x | *«Các agent được điều đi trước đó có còn cần thiết không. Do fable hút Token quá nên có vẻ gián đoạn em rà soát điều tiếp theo với các agent model nhẹ hơn để làm tiếp các việc còn dang dở chưa xác định cần tìm hiểu nha e»* | `YÊU_CẦU` | Gom **131 mục dang dở** từ V11165–V11166, chạy 5 cổng Sonnet/Haiku | `ĐÃ_LÀM` |

---

## 3 · Đào bới / phát hiện

### 3.1 · Sáu báo động hạ nhiệt — đo thật thì không phải lỗi

| mục | kết luận đo được |
|---|---|
| **2 model shadow_only trong pool bỏ phiếu combo-super** | Mâu thuẫn **cấu trúc** có thật (pool không lọc `output_eligible`), nhưng **0/271 bundle trong 90 ngày** có chúng là voter thật. Đọc đúng `ranked_numbers[*].voters` mới ra con số này |
| **`gpt_analyzer.py:6449` đọc bảng chết 99 ngày** | ✅ **KHÔNG rò vào official.** Writer bị **tắt CHỦ Ý** bởi V10659 (31/05, chú thích rõ trong `scheduler.py:9024-9031`). Reader trả dòng tĩnh khi rỗng, và **chỉ chạy khi `lane_test_shadow_pack=True`** — tức chỉ luồng `shadow_auto_eval` |
| **Trộn regime prompt cùng ngày** (gemini-3.5/3.6-flash) | Chỉ **1/31 ngày** (03/09 — đúng giai đoạn chuyển tiếp **trước** deploy V11160 lúc 00:20-00:55 ngày 04/09). Từ 04/09 ổn định **100% một regime** |
| **OpenRouter thành công dài hơn `httpx timeout=300s`** | ✅ **Không phải lỗi.** Là **retry cộng dồn có chủ ý**: 4 lần thử × 300s + backoff 5/15/30s, cộng 4 lần fallback ở tầng ngoài. Khớp số học với `glm-5.1 max=1429,5s ≈ 300+5+300+15+300+30+480` |
| **Reasoning ăn 96,0% trần đầu ra** | Có thật, tái lập được (**62.911/65.536**), nhưng **chưa lượt nào hỏng vì nó** — cả 4 lượt lịch sử đều `finish_reason=STOP` ⇒ đúng là **rủi ro tiềm ẩn**, không phải lỗi đã xảy ra |
| **«Chỉ 2 cổng có sổ điểm danh»** | ✅ Thật ra **10 cổng chứng minh được đã chạy** (8 cổng nữa qua sổ điểm danh dùng chung của hook git-commit). 604/614 tệp còn lại là **`INDETERMINATE`**, **không phải** «chưa từng chạy» |

**Thêm ba mục đóng khác:** «số token không đo được» → **đo được** từ `usage` của provider ·
**`FU-419`** đã lên production · **3 nhãn job im 117–120 ngày** đều có lời giải (script test tay
một lần · nhãn log từ sự cố V105.13 · hàm còn sống chỉ im vì không có sự cố) — **không job nào bị
âm thầm gỡ**.

### 3.2 · 🔴 Mục đổi bản chất — 79 bundle, không phải 78

**`bach_thu` ≠ `ranked_numbers[0]`: 79/571 bundle** (RM-11 — số đúng là 79, không phải 78).

**Đây KHÔNG phải lỗi tính toán.** 50/79 giải thích đầy đủ bằng **4 cơ chế override hợp lệ owner đã
duyệt**: `V10640` (MN, đang hoạt động, 27/32 khớp) · `V10767+V10789` (MB, **đã tắt từ 01/08**,
15/25) · `V10790` (MT, **đã tắt từ 01/08**, 8/22).

**Cơ chế thật:** các override đổi biến `bach_thu` **SAU KHI** biến `ranked` đã được dùng để xây
`ranked_numbers`/`score_breakdown` (`main.py:10225` vs `:10465`), và **`main_selection_reason` là
một CHUỖI CỨNG** (`:10379`) **không bao giờ được cập nhật** để ghi override nào đã chạy.

⇒ **LỖ HỔNG PROVENANCE**, không phải lỗi số. Và **29/79** (MN 5 · MB 10 · MT 14) tập trung tháng
6/2026, **TRƯỚC cả ngày ba module `V10767/89/90` ra đời** theo chính docstring của chúng ⇒ **có thể
có cơ chế thứ 5 chưa xác định**.

### 3.3 · Bốn tệp shadow tự định nghĩa lại `DEGRADED_LIVE_DAY`

Xác nhận đúng 4 tệp bằng grep thật: `_materialize_corrected_rescue_replay_shadow.py:247` ·
`_strength_skip_calibration_replay_shadow.py:160` · `_single_vote_rescue_replay_shadow.py:151` ·
`_tier2_replay_v2_shadow.py:170`. Chúng dùng **ngưỡng cứng `m>=15/22/10` trên SỐ DÒNG
`predictions` THÔ (gộp cả ba miền/ngày)**, khác hẳn logic chính thức
`classify_bundle_quality()` = `model_count/expected` **theo TỪNG MIỀN** trong `database.py`.

⇒ Mọi số liệu từ 4 tệp đó **không so được** với sổ quản trị chính. *(Đo định lượng ở V11169.)*

### 3.4 · Phân loại đủ 131 mục dang dở *(Haiku — việc cơ học, model rẻ nhất)*

| nhóm | n | ghi chú |
|---|---|---|
| **đã giải quyết** | **22** | 8 bị phủ nhận · 9 đã quan sát · **5 là KẾT QUẢ THIẾT KẾ**, không phải thiếu sót |
| cần thêm bằng chứng | 91 | 66 giả thuyết · 15 thiếu dữ liệu · 7 metadata · 2 viewer-freeze · 1 trùng |
| **cần owner** | **6** | chính sách MB `min_bt/min_wr` · có được đo hiệu ứng dự đoán không · **gán P0–P3 cho 194 mục treo** |
| **cần công cụ** | **6** | **tất cả đều là đếm token** |
| không đáng làm | 4 | ngoài phạm vi giai đoạn 1 |

### 3.5 · Agent tự bắt bẫy của chính nó

Lần dò đầu cho mục «2 model shadow_only» tìm chuỗi tên model trong `source_predictions_json` ra
*«184/271 bundle có nhắc tên»* — **SAI**, vì trường `model_wr/model_bt` liệt kê **CẢ 27 model** để
theo dõi WR/BT, không phải danh sách đã bỏ phiếu. Đọc đúng `ranked_numbers[*].voters` mới ra
**0/271**. Đúng tinh thần **RM-09/RM-10**, ghi lại để không ai lặp.

Thêm: đề bài của chính agent ghi *«10 lượt cùng lane/miền/ngày»* — số thật là **9**. Không đổi kết
luận nhưng phải sửa khi trích lại.

---

## 4 · Hướng xử lý và vì sao chọn

**Vì sao dùng Haiku cho cổng phân loại:** việc đó thuần cơ học — đọc 131 dòng văn bản đã có và xếp
nhóm, không cần đo lại gì. Dùng model đắt cho việc này là lãng phí đúng cái owner vừa nhắc.

**Vì sao không tự đóng 6 mục «cần công cụ» bằng `pip install tiktoken`:** cài gói trên VPS là
**thay đổi môi trường sản xuất**, phải owner duyệt. Lối sạch hơn — suy tỉ lệ từ chính corpus —
được làm ở **V11169**.

---

## 5 · Đã làm gì

| việc | kết quả |
|---|---|
| gom việc dang dở | **131 mục** từ V11165–V11166 (100 «chưa trả lời được» · 13 `INDETERMINATE` · 18 «cần thêm bằng chứng») |
| xử 28 mục nặng nhất | **16 `DONG_DUOC` · 11 `VAN_TREO` · 1 `KHONG_DANG_LAM`** |
| phân loại toàn bộ 131 | 22 đã giải quyết · 91 cần bằng chứng · 6 cần owner · 6 cần công cụ · 4 bỏ |
| production | **0 ghi · 0 deploy · 0 restart** |

---

## 6 · Cổng kiểm — xác minh

| cổng | kết quả |
|---|---|
| DB production | mọi kết nối `mode=ro` |
| `neo558` trước/sau | **khớp** `a82c508d3569abda…` |
| 6 hash tệp đang serve | **không đổi** |
| service | PID `3370750` · `NRestarts 0` · health 200 |
| AST-parse trên VPS (không import `main.py`) | tránh side-effect khi kiểm `model_registry` + `combo_super` |
| agent lỗi | **0/5** |

---

## 7 · Vướng vấp

| # | vấp | gỡ |
|---|---|---|
| 1 | **Đếm chuỗi thô ra «184/271»** vì `model_wr/model_bt` liệt kê cả 27 model theo dõi | đọc đúng `ranked_numbers[*].voters` → **0/271**. RM-09/RM-10 |
| 2 | **Đề bài ghi «10 lượt»** — số thật **9** | không đổi kết luận, sửa khi trích lại |

---

## 8 · Gỡ về

**Không áp dụng** — phiên chỉ đo, **0 ghi production · 0 deploy · 0 restart**. Mọi kết quả ghi ra
`artifacts/v11168_*.json` trên VPS, nằm ngoài đường phục vụ.

---

## 9 · Theo dõi tiếp

| # | việc | ai chặn |
|---|---|---|
| 1 | **Cơ chế thứ 5** cho 29/79 bundle tháng 6/2026 | AGENT *(đã làm ở V11169)* |
| 2 | **`main_selection_reason` khoá cứng** `main.py:10379` | OWNER (chạm mã đang serve) |
| 3 | **4 tệp shadow dùng ngưỡng cứng** thay vì đọc `day_governance` | OWNER (chạm mã) |
| 4 | **6 mục cần đếm token** | AGENT *(đã làm ở V11169 bằng tỉ lệ từ corpus)* |
| 5 | `ctx_pack` lệch 1.472 ký tự (05/09 MT) | phải gọi `build_context_pack()` — luật phiên cấm |
| 6 | Phase 15 as-of leak toàn lịch sử · 65 ca chép sai số · TOTAL thua trung bình model · combo-super cứu/phá | cần thêm mẫu hoặc mở rộng quét |
| 7 | **85/66/27 bảng im** — **không tái lập được** bộ số gốc bằng phương pháp độc lập (ra 66/79 và 8 bảng/7 tệp) | cần phương pháp gốc để đối chiếu |

**Năm P0 hạ tầng của V11166 vẫn nguyên:** backup ngoài máy · swap + `OOMScoreAdjust` · tắt SSH root
mật khẩu + `fail2ban` · nối lại 7 cổng vào `.claude/settings.json` · cảnh báo đĩa +
hồi sinh `system_alerts`.

---

## 10 · Nguồn ba lớp (§62)

### `OWNER_SAID`
- 06/09 ~09:2x — *«…em rà soát điều tiếp theo với các agent model nhẹ hơn để làm tiếp các việc còn
  dang dở chưa xác định cần tìm hiểu nha e»*

### `CODE_DID`
- `main.py:10225` vs `:10465` — override đổi `bach_thu` sau khi `ranked` đã dùng
- `main.py:10379` — `main_selection_reason` là **chuỗi cứng**
- `scheduler.py:9024-9031` — V10659 **tắt CHỦ Ý** writer của `v101_region_source_pool_top5_shadow`
- `scheduler.py:7690` — `lane_test_shadow_pack=True` **chỉ** trong luồng `shadow_auto_eval`
- `gpt_analyzer.py:3546` — `max_output_tokens=65536`
- 4 tệp shadow: `:247` · `:160` · `:151` · `:170` — ngưỡng cứng `m>=15/22/10`

### `RUNTIME_DID`
- **0/271** bundle có 2 model shadow_only là voter thật (90 ngày)
- gemini-3.5-flash **95 lượt/31 ngày** · gemini-3.6-flash **91 lượt/31 ngày** — chỉ **1 ngày** trộn regime
- reasoning **62.911–62.914/65.536 = 95,99–96,00%**, cả 4 lượt lịch sử `finish_reason=STOP`
- `glm-5.1` max **1429,5s** — khớp công thức retry cộng dồn

### `DOC_SAID`
- Docstring `V10767/89/90` ghi ngày ra đời **sau** 29 bundle mismatch tháng 6/2026 ⇒ không thể do
  chúng gây ra

### `NOT_VERIFIED`
- cơ chế thứ 5 · nguyên nhân `ctx_pack` lệch 1.472 ký tự · 604/614 cổng `INDETERMINATE` ·
  bộ số 85/66/27 bảng im

---

## 11 · Commit

| | |
|---|---|
| `governance_seq` | → **484** *(cùng lượt với V11169)* |
| commit | *(ghi ở V11169 — hai bản cùng một lượt push)* |

---

TanPhatAI cần làm: ghi **`V11168`** — công khai bản này. Ghi **5 agent (4 Sonnet + 1 Haiku), 1,04 triệu token, 23 phút** — theo yêu cầu owner dùng model nhẹ. Ghi **16/28 việc dang dở ĐÓNG ĐƯỢC**, và **phần lớn là BÁO ĐỘNG HẠ NHIỆT**: 2 model shadow_only **0/271 bundle** từng thắng phiếu · `gpt_analyzer.py:6449` **KHÔNG rò vào official** (writer tắt chủ ý bởi V10659; reader chỉ chạy khi `lane_test_shadow_pack=True`) · «OpenRouter vượt 300s» là **retry cộng dồn có chủ ý** · trộn regime chỉ **1/31 ngày** rồi ổn định từ 04/09 · reasoning 96% là **rủi ro tiềm ẩn chưa từng gây hỏng** · **10 cổng** chứng minh được đã chạy chứ không phải 2. Ghi **MỘT MỤC ĐỔI BẢN CHẤT: 79 bundle (không phải 78 — RM-11) có `bach_thu` ≠ `ranked[0]`; 50/79 là OVERRIDE HỢP LỆ owner đã duyệt; lỗi thật là `main_selection_reason` KHOÁ CỨNG ở `main.py:10379` ⇒ LỖ HỔNG PROVENANCE; 29/79 tập trung tháng 6/2026 TRƯỚC khi ba module override ra đời**. Ghi **4 tệp shadow tự định nghĩa lại `DEGRADED_LIVE_DAY`** bằng ngưỡng cứng trên số dòng THÔ gộp cả ba miền, khác hẳn `classify_bundle_quality()` theo từng miền. Ghi **phân loại đủ 131 mục**: 22 đã giải quyết · 91 cần bằng chứng · 6 cần owner · 6 cần công cụ · 4 không đáng làm. Ghi **agent tự bắt bẫy đếm-chuỗi-thô của chính nó** (184/271 → 0/271). **Code KHÔNG đi trước tài liệu** — 0 ghi production, 0 deploy, 0 restart. **Không mở Prompt 44. Không mở FU mới. Không mở Plan mới.**
