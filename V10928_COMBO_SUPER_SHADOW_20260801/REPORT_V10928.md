# V10928 — combo-super ăn model nào (sửa lỗi báo cáo sai) + shadow 110 ngày chưa promote ai

**Ngày:** 01/08/2026 · **Trạng thái:** chỉ đo và soi, **không đổi gì** (đang trong cửa sổ đóng băng FU-186)

---

## 1. Tóm tắt

Owner cảnh báo *"cắt model ảnh hưởng đến combo super mới quan trọng cẩn thận chỗ này"* và bức
xúc *"showdow gì mà lâu quá trời không lấy được model nào tốt nhét vào total offical"*.

Hai kết quả:

**(a) Shadow: 110 ngày · 3.778 lượt gọi · 28 model · KHÔNG MỘT LẦN promote.** Owner nói đúng
hoàn toàn.

**(b) `combo-super` hoạt động KHÁC hẳn những gì agent báo cáo phiên trước.** Nó **chọn động
theo từng miền, tính lại mỗi ngày** — không phải danh sách cố định. Và **cả 4 model ML đều đang
được dùng thật**, không phải chỉ 2 như agent đã nói.

---

## 2. Owner yêu cầu gì (nguyên văn)

**01/08 12:56:**

> *"Ôi quá lâu quá mệt mỏi ah em, anh quên nhắc và đã bị trôi sông chứ showdow gì mà lâu quá
> trời không lấy được model nào tốt nhét vào total offical quả là lãng phí, 1 chú ý là cắt model
> ảnh hưởng đến combo super mới quan trọng cận thận chỗ này."*

---

## 3. Đào bới / phát hiện

### 3.1 SỬA LỖI — combo-super chọn động, không cố định

Phiên trước agent báo cáo với owner: *"combo-super MN/MT chỉ dùng `meta-learning` + `lstm`"*.
**Sai.** Đó chỉ là ảnh chụp tại một thời điểm, agent trình bày như thể là quy tắc cố định.

Đọc thẳng `combo_super.py` và **gọi thẳng hàm** trên VPS:

```python
get_dynamic_ml_filter(region, top_n=3, days=7)   # chọn 3 ML mạnh nhất, từ pool 4
get_dynamic_ai_filter(region, top_n=2, days=7)   # chọn 2 AI mạnh nhất, từ pool 7
```

| Pool | Số model | Lấy mấy |
|---|---|---|
| `ML_MODELS` | **4** — meta-learning · lstm · xgboost · random-forest | **3** |
| `AI_MODELS` | **7** — gpt-5-mini · claude-sonnet-4-6 · gemini-2.5-flash · claude-opus-4-6 · gemini-2.5-pro · deepseek-reasoner · gpt-5.4 | **2** |

Hôm nay 01/08 mỗi miền chọn:

| Miền | ML top-3 | AI top-2 |
|---|---|---|
| MN | random-forest · meta-learning · lstm | claude-sonnet-4-6 · gpt-5-mini |
| MT | lstm · xgboost · random-forest | gemini-2.5-flash · deepseek-reasoner |
| MB | meta-learning · lstm · xgboost | claude-sonnet-4-6 · claude-opus-4-6 |

**Cả 4 ML đều xuất hiện**: lstm (3 miền) · random-forest (2) · meta-learning (2) · xgboost (2).

### 3.2 Vì sao điều này quyết định cách cắt

Pool ML chỉ có **4** mà phải chọn **3** — biên độ cực mỏng:

| Cắt bao nhiêu ML | Pool còn | Hệ quả |
|---|---|---|
| 0 | 4 | chọn 3 trong 4 — bình thường |
| **1** | **3** | **buộc dùng cả 3, mất hoàn toàn khả năng chọn** |
| 2 | 2 | thiếu nguyên liệu |
| 3 | 1 | coi như hỏng |

Pool AI có **7** chọn **2** — rộng hơn nhiều, cắt 2 vẫn còn 5 để chọn.

### 3.3 Nghi vấn mốc 50% mặc định — đã kiểm, KHÔNG có vấn đề

Code ghi `# chưa có data = 50% default (cho cơ hội)`, mà model có dữ liệu thật chỉ đạt 21–36%.
Nghi ngờ: model **không** có dữ liệu sẽ xếp trên model có dữ liệu → chọn mù.

Kiểm từng lựa chọn hôm nay: **cả 15 lựa chọn (3 miền × 5 model) đều có n=7 dữ liệu thật.**
Nghi vấn không thành.

Nhưng lộ ra chuyện khác: **MN chọn 3 ML mà cả ba đều thắng 0/7 trong tuần.** Bộ lọc chọn "tốt
nhất trong đám tệ" — không có sàn chất lượng tối thiểu.

### 3.4 Shadow — 110 ngày, 0 lần promote

```
từ 2026-04-14 → 2026-08-01   ·   110 ngày   ·   3.778 lượt gọi   ·   28 model
số model đi từ shadow lên official: 0
```

Model chạy lâu nhất: `qwen3-max-thinking` 108 ngày / 322 lượt · `grok-4.20-multi-agent` 106 ngày
/ 318 lượt · `glm-5.1` 110 ngày / 309 lượt · `gpt-oss-120b` 104 ngày / 306 lượt.

Đây **không phải** thiếu mẫu. 104–110 ngày là quá đủ để quyết.

---

## 4. Hướng xử lý và vì sao chọn

| Phương án | Vì sao chọn / loại |
|---|---|
| **Phân biệt rõ "bỏ phiếu" và "cắt hẳn"** | **ĐÃ CHỌN làm nguyên tắc.** Bỏ cờ `output_eligible` → model vẫn chạy, combo-super vẫn có nguyên liệu, chỉ không bỏ phiếu vào bundle. Cắt hẳn → combo-super mất nguyên liệu |
| Cắt hẳn ML để tiết kiệm | Loại: 4 ML **miễn phí** (không tốn token), cắt không tiết kiệm được gì mà làm hỏng combo-super |
| Cắt 2 AI tốn tiền (`gpt-5.4`, `gpt-5-mini`) | **Khả thi** — pool AI còn 5, vẫn chọn được 2 |
| Đo thêm shadow rồi mới quyết | **Loại.** Owner đã từ chối: *"số liệu có rõ ràng rồi mà đo hoài"*. 110 ngày là quá đủ |
| Promote `glm-5.1` + `gpt-oss-120b` | **Đề xuất** — xem mục 9 |

---

## 5. Đã làm gì

**Không đổi gì trong hệ thống.** Đang trong cửa sổ đóng băng FU-186 (01–08/08) do owner chốt.

Phiên này chỉ đo và soi:

| Script | Việc |
|---|---|
| `_v10928_combo_deps.py` | Quét hằng số + tìm chỗ code phân biệt theo miền |
| `_v10928_combo_exact.py` | **Gọi thẳng hàm** `get_dynamic_ml_filter` / `get_dynamic_ai_filter` trên VPS |
| `_v10928_probe3.py` | Kiểm mốc 50% mặc định + đếm số lần promote |

---

## 6. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| Danh sách ML/AI của combo-super | Gọi thẳng hàm trên VPS, không suy từ regex |
| Lựa chọn hôm nay có dựa trên dữ liệu thật | **15/15 lựa chọn có n=7** — không cái nào dùng mặc định |
| Số lần promote shadow → official | **0** trên 110 ngày |
| Hệ thống có bị đổi gì không | **Không** — chỉ đọc |

---

## 7. Vướng vấp

| # | Vấp | Hậu quả nếu bỏ qua |
|---|---|---|
| 1 | **Agent từng báo cáo sai với owner**: nói combo-super MN/MT *"chỉ dùng meta-learning + lstm"* như thể là quy tắc cố định, trong khi thực tế là **chọn động top-3/top-2 mỗi ngày** | Owner có thể duyệt cắt `xgboost`/`random-forest` vì tưởng chúng không được dùng — thực tế cả 4 ML đều đang dùng |
| 2 | Regex quét hằng số bắt hụt vì `AI_MODELS` là danh sách **dict** chứ không phải chuỗi | Lượt đầu chỉ thấy 3 model thay vì 7 — suýt báo cáo sai lần nữa |
| 3 | Nghi mốc 50% mặc định làm chọn mù | Kiểm ra không phải; nhưng nếu không kiểm thì đã báo động nhầm |
| 4 | MN chọn 3 ML mà cả ba thắng 0/7 | Bộ lọc **không có sàn chất lượng** — vẫn chọn "tốt nhất trong đám tệ" |

---

## 8. Gỡ về

Không áp dụng — phiên này **không đổi gì**, chỉ đọc và đo.

---

## 9. Theo dõi tiếp

| Mã | Việc | Ngưỡng | Hạn |
|---|---|---|---|
| **FU-191** | **Nguyên tắc cắt model an toàn với combo-super** — ghi vào quy tắc: cắt ML phải giữ pool ≥ 4; muốn giảm ảnh hưởng thì bỏ cờ `output_eligible` chứ không dừng model | đã ghi vào báo cáo, cần khoá vào `CLAUDE.md` phiên sau | 08/08 |
| **FU-192** | **Promote shadow — 110 ngày 0 lần là lãng phí.** Ứng viên: `glm-5.1` (shadow duy nhất được xếp GIỮ ỔN ĐỊNH, dương 4/5 kỳ) và `gpt-oss-120b` (+3,14pp, 3/5 kỳ, 104 ngày) | owner quyết: promote sau 08/08, hay ngay bây giờ | chờ owner |
| **FU-193** | Bộ lọc combo-super **không có sàn chất lượng** — MN hôm nay chọn 3 ML thắng 0/7 | đề xuất: nếu cả pool dưới ngưỡng thì combo-super bỏ nhánh ML thay vì chọn bừa | 08/08 |
| FU-186 | Cửa sổ đóng băng | không đổi gì tới 08/08 | 08/08 |

Nguyên văn lời owner: `CONVERSATION_CONTEXT_V10928_20260801.md` cùng thư mục.
