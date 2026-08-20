# REPORT V11091 — RÀ TỔNG LỰC TRƯỚC NGÀY MỞ GÓI: BỐN MỤC KHÔNG AI CANH, VÀ `D3` CHƯA ĐỦ ĐỂ CHẠY

**Ngày:** 2026-08-20 · **Mã đọc:** `KS2108-2` · **Quyết định:** `QD-068`
**Production KHÔNG đổi** — không deploy · không Notion · `QD-041` nguyên vẹn tới 21/08.

---

## 1. Tóm tắt

Owner yêu cầu rà **toàn bộ**, vì *«lâu quá nên nhiều cái nó mơ hồ… có thể rơi rớt»*. Rà xong:

| | phát hiện |
|---|---|
| **①** | **4/14 mục gói 21/08 KHÔNG có mã theo dõi** — chạy mai mà không ai canh |
| **②** | **`D3` chưa đủ để chạy** — gỡ `§11`+`§18` để lại prompt **tự mâu thuẫn** ở **5 chỗ** |
| **③** | **Món nợ `RM-07` đã trả** — khuyết tật `_v11057` **không** lặp lại ở bộ đo nào khác |
| **④** | **5 món nợ khác chưa làm**, đo được bằng máy |

**Ba lần suýt báo động giả — cả ba tự bắt được trước khi trình owner.** Chi tiết ở mục 7.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«Đã xem kỹ tổng lực toàn bộ chưa? lâu quá nên nhiều cái nó mơ hồ, không rõ ràng và có thể rơi
> rớt em cần xem kỹ dùm anh lại 1 lần nữa nha em»*

Câu trả lời thật: **chưa**. Các phiên trước soi **từng việc được giao**, không soi **toàn bộ**.
Bản này là lần rà ngang.

---

## 3. Đào bới / phát hiện

### 3.1 · ① Bốn mục gói 21/08 **không có mã theo dõi**

Rà đủ 14 mục × trạng thái trong `FOLLOW_UP_TRACKER.md`:

| # | mã | trong sổ? | status |
|---|---|---|---|
| 1 | `FU-393` | CÓ | `OWNER_DECISION_NEEDED` |
| **2** | **`D2`** | **KHÔNG** | — |
| **3** | **`D3`** | **KHÔNG** | — |
| 4 | `FU-394` | CÓ | `MEASURED_SHADOW_ONLY` |
| 5 | `FU-395` | CÓ | `PLAN_21_08` |
| 6 | `FU-397b` | CÓ | `PLAN_21_08` |
| 7 | `FU-398` | CÓ | `DO_TIEN_DANG_CHAY` |
| **8** | **`FU-290A`** | **KHÔNG** | — |
| 9 | `FU-299` | CÓ | `AWAITING_OWNER_OK` |
| 10 | `FU-300` | CÓ | `AWAITING_OWNER_OK` |
| 11 | `FU-380` | CÓ | `BLOCKED` |
| **12** | **gỡ `latency_score`** | **KHÔNG** | — |
| 13 | `GĐ2` | KHÔNG | *(đã loại — `FU-284` không cho phép)* |
| 14 | `FU-404` | CÓ | `MEASURED_ROOT_CAUSE` |

⇒ **4 mục sẽ chạy mai mà không có trạng thái, không có điểm gỡ về ghi trong sổ, không ai canh.**

**Đích thật của từng mục — đã xác minh bằng máy:**

| mục | đích | xác minh |
|---|---|---|
| `D2` | `main.py:124` — hiện `MINED_RULES_MODE = 'soft'` | ✓ |
| `D3` | `gpt_analyzer.py:593` (§11) · `:635` (§18) | ✓ |
| `FU-290A` | **chỉ là nhãn trong văn xuôi** — `SSOT:761` ghi *«HOÃN tới 21/08»* | ⚠ **chưa có nội dung thiết kế** |
| `latency_score` | `_materialize_du_doan_test_model_budget.py:101` · `:372` · `:527` | ✓ |

### 3.2 · ② `D3` **chưa đủ để chạy** — và đây là phát hiện nặng nhất

`§11` và `§18` **đều dạy model dùng khối `🎯 RULE TAILS`**:

```
§11 (dòng 593) RULE TAILS UTILIZATION
    🔥STRONG (≥3 rules): CẦN xem xét nghiêm túc, nên có trong top-2
    ⚡MED (2 rules): tham khảo tốt, dùng như tín hiệu phụ
    💡LIGHT (1 rule): chỉ tham khảo, KHÔNG đủ để chọn đơn lẻ
    KHÔNG tự tạo số mới nếu Rule Tails đã có gợi ý mạnh

§18 (dòng 635) KHI NÀO KHÔNG TỰ "TẠO" SỐ
    Nếu Rule Tails có 🔥STRONG suggestion → dùng nó, đừng bịa số mới
```

**Gỡ hai mục này sẽ để lại:**

| còn lại | ở đâu |
|---|---|
| **khối `🎯 RULE TAILS (48h)` VẪN bơm** — **không có cổng shadow** | `gpt_analyzer.py:4836` |
| `§9` *«Rule Tails ở nhiều nguồn cross-region → tín hiệu MẠNH»* | `:534` |
| `§10` *«rule tails từ ĐB/G1 → tin tưởng hơn tails từ G7/G8»* | `:542` |
| `§20` đếm `rule tails` là một trong ba tín hiệu xếp **PRIMARY** | `:679` |
| `§25` định nghĩa `near_miss_shortlist` **dựa vào** Rule Tails | `:764` |

**Nặng nhất:** khối phát ra đúng ba nhãn `🔥STRONG` / `⚡MED` / `💡LIGHT` (`:4839`), và **`§11` là
nơi DUY NHẤT giải nghĩa chúng**. Gỡ `§11` ⇒ model nhận nhãn **không có định nghĩa**.

Và `§18` là **rào chắn chống bịa số**. Gỡ nó mà **giữ** khối dữ liệu = **bỏ rào mà giữ nguyên
nguồn cám dỗ**.

⇒ Đúng vết **`§60.1`**: V11001 gỡ 8 khối gan/nóng/lạnh, hôm sau còn **10 chỗ** vẫn dạy model dùng
thứ vừa gỡ. Đây là **cùng một lỗi, sắp lặp lại**.

### 3.3 · ③ Món nợ `RM-07` — **đã trả**, kết quả sạch

`V11079` hứa *«quét các bộ đo khác cũng tự khai READ-ONLY mà có ghi»* — chưa làm. Nay làm:

Lọc đúng khuyết tật `_v11057`: **khai READ-ONLY + ghi đè artifact bằng TÊN CỐ ĐỊNH** (không dấu
thời gian — vì dấu thời gian chính là cách `V11079` đã sửa).

⇒ **0 tệp.** Khuyết tật **không lặp lại**.

### 3.4 · ④ Năm món nợ chưa làm — đo bằng máy, không đoán

| | món nợ | nguồn |
|---|---|---|
| ✗ | cổng máy cho lớp lỗi `>/dev/null` che stderr | tái phạm **3 lần**, `V11079`/`V11087` |
| ✗ | cổng `RM-19` so **cả cặp khác chủ đề** | `V11087` — `_v11034` báo `SẠCH` trong khi có va chạm thật |
| ✗ | bộ đọc nhận nhãn `\| **hạn** \|` dạng ô bảng | `V11087` — đang đọc nhầm ngày ít nhất một mục |
| ✗ | `FU-407` đo `lo3`/`xien` cùng khuôn | `V11086` |
| ✗ | bộ chấm T-B lên VPS | `V11089` — vùng cấm |

---

## 4. Hướng xử lý và vì sao chọn

**Vì sao khai `FU-410` mà KHÔNG thêm mục vào gói.** `QD-064` khoá *«không thêm không bớt»*. Bốn
mục kia **đã nằm trong gói** — chúng chỉ **thiếu khối theo dõi**. Khai bổ sung là **ghi lại thứ
đã có**, không phải chen mục mới.

**Vì sao KHÔNG tự xử `D3`.** Nó chạm **cấu trúc prompt** ⇒ `QD-041` khoá tới 21/08. Và ba lối xử
lý đều là quyết định về **phạm vi gói** — thuộc owner.

**Vì sao không báo con số `287/554`.** Xem mục 7 — đó là đếm chuỗi thô, đúng bẫy `RM-09`.

---

## 5. Đã làm gì

| # | việc | commit |
|---|---|---|
| 1 | rà 14 mục gói × trạng thái sổ | — |
| 2 | xác minh đích thật của `D2` · `D3` · `FU-290A` · `latency_score` · `FU-397b` · `FU-404` · `FU-394` | — |
| 3 | quét coherence cho `D3` — tìm 5 chỗ dangling | — |
| 4 | **trả món nợ `RM-07`** — 0 tệp lặp khuyết tật | — |
| 5 | đo 5 món nợ còn lại bằng máy | — |
| 6 | **khai `FU-410`** ghi đủ 4 mục + cảnh báo `D3` + 3 lối | `f0c9583` |

**Không sửa dòng mã nào.** `QD-041` nguyên vẹn.

---

## 6. Cổng kiểm

| cổng | |
|---|---|
| ghi tệp an toàn · đoán tên · mất mục · đóng băng · chéo quyết định · sáu mặt | **✓ 6/6** |
| `_v11085_cong_rut_lai` · `_v11088_cong_cua_so_chon` | **✓ SẠCH** |
| `_v10981_kiem_lich` K8 | **✓ ĐẠT 8/8** · miễn trừ hết hạn **21/08** |
| `_v11062 --kiem` K1–K4 | **✓ ĐẠT** |

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| nội dung | nguyên văn |
|---|---|
| yêu cầu phiên này | *«lâu quá nên nhiều cái nó mơ hồ, không rõ ràng và có thể rơi rớt em cần xem kỹ dùm anh lại 1 lần nữa»* |
| `QD-064` (11/08) | *«13 mục, không thêm không bớt»* |
| `QD-041` | cấm chạm prompt/đường chọn số tới 21/08 |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| 4/14 mục không có mã theo dõi | `D2` · `D3` · `FU-290A` · `latency_score` |
| `MINED_RULES_MODE = 'soft'` | `main.py:124` |
| `§11`/`§18` tồn tại | `gpt_analyzer.py:593` · `:635` |
| khối RULE TAILS bơm **không cổng** | `:4836`, `try/except` không có gate |
| 3 nhãn chỉ định nghĩa ở `§11` | `:4839` phát nhãn · `:595-597` định nghĩa |
| 4 chỗ khác trỏ Rule Tails | `§9:534` · `§10:542` · `§20:679` · `§25:764` |
| khuyết tật `_v11057` không lặp | quét toàn `web/backend/_v1*.py` ⇒ **0** |

### `DOC_SAID`

| tài liệu ghi gì | lệch? |
|---|---|
| gói 21/08: 14 mục ngang hàng | **LỆCH** — 4 mục **không có khối theo dõi**, 1 mục (`FU-290A`) **không có nội dung** |
| `#3 D3` *«gỡ RR §11 + §18»* | **LỆCH** — mô tả **thiếu**: không nói gì về khối dữ liệu còn lại và 4 chỗ trỏ tới nó |
| `V11079` hứa quét họ lỗi `RM-07` | **đã trả** trong bản này |

### Ba lớp lệch nhau ⇒ FINDING

**`DOC_SAID` ≠ `CODE_DID`, hai chỗ, cả hai chặn ngày mai:** ① gói liệt kê 14 mục **như thể đều
sẵn sàng**, thực tế 4 mục không ai canh và 1 mục không có nội dung; ② `D3` mô tả một việc **gỡ hai
mục**, thực tế là việc **gỡ hai mục + xử 5 chỗ dangling**.

---

## 7. Vướng vấp — **ba lần suýt báo động giả, cả ba tự bắt được**

### (a) Suýt báo *«`RR §11`/`§18` KHÔNG TỒN TẠI»*

`grep "§11"` trong `gpt_analyzer.py` và `prompt_registry.py` ra **rỗng**. Rất muốn báo ngay
*«đích của `D3` không tồn tại»*.

Đào thêm thì thấy rulebook đánh số **`### 11.`**, không phải chuỗi `§11`. **Chúng tồn tại.**
Đã **rút lại trong cùng lượt**, trước khi trình owner.

### (b) Suýt báo *«`_v11044` cũng dính lỗi hậu tố»*

`_v11044` không có luật lọc hậu tố như `_v10921`/`_v11062` ⇒ trông như cùng họ lỗi. Đọc mã thì
nó chỉ lưu **phần số** (`int(m.group(1))`) ⇒ `V11080b → 11080`, tập hợp **tự gộp**.
**Miễn nhiễm theo thiết kế.** Không báo.

### (c) Suýt báo *«287/554 tệp khai READ-ONLY mà có ghi»*

Con số đúng về số học, **sai về kết luận**. Chính `_v11088_cuu_ban_sao.py` của phiên trước cũng
nằm trong danh sách — mà nó ghi rõ *«chỉ đọc kho, chỉ ghi vào `artifacts/`»*. **Không nói dối.**

Đúng bẫy `RM-09` (cấm đếm chuỗi thô). Lọc đúng khuyết tật `_v11057` ⇒ **0 tệp**.

> **Điểm chung ba ca:** con số đầu tiên đều **đúng** và **dẫn tới kết luận sai**. Thứ cứu được
> là hỏi thêm một câu: *«con số này thật sự đang đếm cái gì?»*

---

## 8. Gỡ về

```bash
git revert f0c9583   # chỉ là khai bổ sung vào sổ theo dõi
```

Phần rà là **read-only** — không có gì để gỡ.

---

## 9. Theo dõi tiếp

### ⚠️ BA VIỆC PHẢI QUYẾT TRƯỚC KHI CHẠY GÓI 21/08

| # | việc | vì sao |
|---|---|---|
| **1** | **`D3` — chọn lối A / B / C** | gỡ `§11`+`§18` như mô tả sẽ để lại prompt **tự mâu thuẫn 5 chỗ**. **Khuyến nghị lối C (HOÃN)** — nó là mục **duy nhất** chạm cấu trúc prompt và **chưa có phép quét ngược nào** |
| **2** | **`FU-290A`** — có nội dung thiết kế chưa? | chỉ là **nhãn**; `§59` đòi trả lời **ba câu** trước khi trình, **chưa câu nào** |
| **3** | **Ký hai ngưỡng** bầy đàn + DEHERD | không ký ⇒ hai thước đó **không bao giờ đọc được** |

### Ba lối cho `D3`

| lối | nghĩa |
|---|---|
| **A** | gỡ `§11`+`§18` **VÀ** gỡ khối `RULE TAILS` **VÀ** sửa 4 chỗ trỏ tới nó |
| **B** | gỡ `§11`+`§18` nhưng **GIỮ** khối ⇒ phải **chuyển định nghĩa 3 nhãn** sang mục khác |
| **C** | **HOÃN `D3`** thành việc riêng, có dump prompt + quét ngược phân loại đầy đủ |

### Năm món nợ — xếp theo mức gấp

| | món nợ | đề nghị |
|---|---|---|
| 1 | bộ chấm T-B **lên VPS** | mai, khi hết vùng cấm deploy |
| 2 | cổng `RM-19` so cặp **khác chủ đề** | sau gói — nó đang **báo `SẠCH` sai** |
| 3 | cổng máy cho `>/dev/null` che stderr | tái phạm **3 lần**, đã quá ngưỡng `§61` |
| 4 | bộ đọc nhãn `\| **hạn** \|` | đang đọc nhầm ngày ít nhất một mục |
| 5 | `FU-407` đo `lo3`/`xien` | sau gói |

**Verdict tách hai dòng:**
- **`CODE_PUSHED`** = `f0c9583` (khai `FU-410`)
- **`REPORT_PUBLISHED`** = bản này

---

TanPhatAI cần làm: ① ghi **4/14 mục gói 21/08 KHÔNG có mã theo dõi** (`D2` · `D3` · `FU-290A` ·
`latency_score`) — đã khai `FU-410`, **không phải thêm mục** (`QD-064` khoá); ② ghi **`D3` CHƯA ĐỦ
ĐỂ CHẠY** — gỡ `§11`+`§18` để lại khối `RULE TAILS` **vẫn bơm** + **4 chỗ** vẫn trỏ tới nó + ba
nhãn `🔥STRONG`/`⚡MED`/`💡LIGHT` **mất định nghĩa**; owner chọn **A/B/C**, khuyến nghị **C**;
③ ghi **`FU-290A` chỉ là NHÃN** — `§59` đòi ba câu, **chưa câu nào** được trả lời; ④ ghi **món nợ
`RM-07` ĐÃ TRẢ** — khuyết tật `_v11057` **không lặp lại** (0 tệp); ⑤ ghi **5 món nợ chưa làm**,
gấp nhất là **cổng `RM-19` đang báo `SẠCH` sai**; ⑥ ghi **ba lần suýt báo động giả đã tự bắt**
(`§11` tồn tại · `_v11044` miễn nhiễm · `287/554` là đếm chuỗi thô) — **không con số nào trong ba
cái đó được đưa ra như kết luận**.
