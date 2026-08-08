# REPORT V11035 — OWNER BẮT ĐÚNG `glm-5.2`, VÀ NÓ LÔI RA LỖI CHẤM ĐIỂM

**Ngày:** 2026-08-08 tối · **Loại:** audit + quyết định · **CHỈ ĐỌC + ghi sổ quyết định**

---

## 1. Tóm tắt

Owner hỏi một câu về một model. Câu đó lôi ra **hai** thứ lớn hơn:

| | |
|---|---|
| **① Agent đếm thiếu** | báo cáo V11034 nói *"5 lượt rỗng/30 ngày"* — vì phép quét **lọc mất mọi model shadow**. Số thật **44/2.383 = 1,8%, 15 model** |
| **② Lỗi chấm điểm** | lượt rỗng bị ghi `status='LOSE'` — **y hệt model đã đoán mà sai**. `gemma-4-31b` bị dìm **7,1 điểm** |
| **③ QD-045** | owner duyệt dời `QD-015/016/017` sang **21/08** |

**`glm-5.2` ở MB: 1/29 = 3,4%, lần đầu trong 29 ngày** — chưa phải bệnh kinh niên, nhưng là
triệu chứng của bệnh rộng hơn.

---

## 2. Owner yêu cầu gì (NGUYÊN VĂN)

> Model Ai GLM 5.2 lỗi không dự đoán MB em kiểm tra xử lý chưa em? Dời lịch để đo chứ em

---

## 3. Đào bới / phát hiện

### 3.1 Owner đúng — và agent đã đếm thiếu

```
MB  glm-5.2  []                run_source=shadow_auto_eval  phase=shadow_eval
MN  glm-5.2  ["79", "41"]      run_source=shadow_auto_eval
MT  glm-5.2  ["89", "91"]      run_source=shadow_auto_eval
```

**Vì sao agent không thấy:** phép quét lượt rỗng ở V11034 có mệnh đề
`COALESCE(run_source,'') <> 'shadow_auto_eval'` ⇒ **lọc mất toàn bộ model shadow**.
`glm-5.2` là model shadow.

Đây là lỗi **cùng họ** với lỗi agent vừa tự đính chính vài giờ trước (quên lọc `run_source` khi
đếm lượt 64 ký tự) — nhưng **ngược chiều**: lần trước quên lọc, lần này lọc thừa. Cùng một gốc:
**không hỏi rõ câu hỏi đang đo cái gì trước khi viết mệnh đề lọc.**

### 3.2 Số thật khi KHÔNG lọc: **44/2.383 = 1,8%, 15 model**

| model | rỗng/lượt | tỉ lệ |
|---|---|---|
| **`gemma-4-31b`** | **17/58** | **29,3%** |
| `qwen3-max-thinking` | 7/90 | 7,8% |
| `gemini-3.5-flash` | 4/86 | 4,7% |
| `deepseek-reasoner` | 3/90 | 3,3% |
| `grok-4.3` | 2/67 | 3,0% |
| **`glm-5.2`** | **2/89** | **2,2%** — MB 1/29 · MN 1/30 · MT 0/30 |
| `gpt-5.6-sol-pro` · `claude-opus-5-fast` | 1/29 | 3,4% |
| `kimi-k2.5` · `grok-4.20-multi-agent` | 1/58–60 | 1,7% |
| `qwen3.7-max` · `gpt-5.5` · `gpt-5.4` · `gpt-5-mini` · `glm-5.1` | 1/88–90 | 1,1% |

### 3.3 LỖI NẶNG HƠN — lượt rỗng bị chấm thành `LOSE`

Kiểm `model_daily_eval` × `predictions`: mọi lượt rỗng **đều có dòng chấm**, ghi:

```
status='LOSE'  ·  bt_hit=0  ·  hit_count=0  ·  pick_count=0
```

**Model không trả về gì bị ghi sổ y hệt model đã đoán mà sai.**

#### Tính lại điểm bằng cách loại lượt rỗng

| model | lượt rỗng | điểm **đang ghi** | **điểm thật** | bị dìm |
|---|---|---|---|---|
| **`gemma-4-31b`** | **17/58 = 29,3%** | 17,2% | **24,4%** | **+7,1** |
| `qwen3-max-thinking` | 7/87 = 8,0% | 29,9% | **32,5%** | +2,6 |
| `gemini-3.5-flash` | 4/83 = 4,8% | 36,1% | **38,0%** | +1,8 |
| `gpt-5.6-sol-pro` | 1/26 | 26,9% | 28,0% | +1,1 |
| `grok-4.3` | 2/64 | 26,6% | 27,4% | +0,9 |
| `deepseek-reasoner` | 2/87 | 34,5% | 35,3% | +0,8 |
| 9 model khác | 1 lượt | | | +0,3 → +0,6 |

#### Vì sao đây là lỗi nặng

1. **Xếp hạng shadow sai.** `gemma-4-31b` bị dìm **7,1 điểm** — gần **một phần ba hồ sơ** của nó
   là **thua giả**.
2. **Quyết định cắt/giữ model đứng trên số sai** (FU-192, FU-290). Model bị loại vì "yếu" có thể
   chỉ là **hay lỗi API** — hai bệnh khác hẳn, cách chữa khác hẳn.
3. **Mất một thông tin quan trọng.** "Đoán sai" và "không đoán được" nói hai điều khác nhau về
   chất lượng model; gộp làm một là **vứt đi** chỉ số độ tin cậy vận hành.

**Cách chấm đúng — tách BA trạng thái:**

| trạng thái | vào mẫu số tỉ lệ trúng? | dùng làm gì |
|---|---|---|
| `WIN` | có | tỉ lệ trúng |
| `LOSE` | có | tỉ lệ trúng |
| **`NO_ANSWER`** | **KHÔNG** | đếm riêng — **chỉ số độ tin cậy vận hành** |

### 3.4 QD-045 — dời lịch

| mã | mốc khởi động | nội dung |
|---|---|---|
| `QD-015` | 08/08 → **21/08** | shadow MT bạch thủ = random-forest đơn |
| `QD-016` | 08/08 → **21/08** | bỏ lệnh bắt buộc chọn từ danh sách trên luồng bóng |
| `QD-017` | 08/08 → **21/08** | chạy hai prompt song song trên cùng model |

**`OD-20260801-B` KHÔNG dời** — đã thực thi xong (6/6 lane `cron=0`, kiểm 08/08).

---

## 4. Hướng xử lý và vì sao chọn

**4.1 — KHÔNG sửa bộ chấm tối nay.** `model_daily_eval` là **1 trong 4 bảng khoá**; bộ chấm
thuộc đường production ⇒ `QD-041` khoá tới 21/08. Và sửa cách chấm là **đổi định nghĩa của mọi
con số lịch sử** — việc đó cần chữ ký, không phải quyết định của agent.

**4.2 — Dời 21/08 chứ không dời ngày khác.** 21/08 trùng **mốc mở khoá QD-041** và **mốc chốt
FU-284** ⇒ một cửa sổ phục vụ cả ba phép đo, thay vì ba lần làm bẩn dữ liệu.

**4.3 — Không dời `OD-20260801-B`.** Nó **đã xong**. Dời một việc đã xong là ghi sai sổ, và
phiên sau sẽ đi làm lại việc không cần làm.

**4.4 — Cổng `_v11023` khi deploy phải soi CẢ shadow.** Nếu giữ mệnh đề lọc như hiện tại, nó sẽ
bỏ sót đúng ca `glm-5.2` mà owner vừa bắt.

---

## 5. Đã làm gì

**KHÔNG SỬA CODE.** Đã làm:

| | |
|---|---|
| Kiểm tên model từ nguồn thật | `glm-5.1` và `glm-5.2` **đều tồn tại**, mỗi cái 89 lượt/30 ngày (RM-10 — không đoán) |
| Đo lại lượt rỗng **không lọc shadow** | 44/2.383 = 1,8%, 15 model |
| Xác định cách chấm | `model_daily_eval` ghi lượt rỗng thành `LOSE` — dán bằng chứng 12 dòng |
| Tính lại xếp hạng loại lượt rỗng | bảng 15 model, chênh +0,3 → **+7,1** điểm |
| Ghi **QD-045** | dời `QD-015/016/017` → 21/08, ghi lý do vào **từng mục** |

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| Tuổi dữ liệu | **ĐẠT** — đồng bộ 18:39:07, DB local trùng VPS |
| Không sửa production | **ĐẠT** — 0 tệp `web/backend/*.py` bị sửa |
| Không mutation 4 bảng khoá | **ĐẠT** — mọi kết nối `mode=ro` |
| `_v11034_kiem_cheo_quyet_dinh` | **ĐẠT** — `KIEM_CHEO_QD=SACH` sau khi ghi QD-045 |
| Sổ quyết định đọc lại khớp | **ĐẠT** — 47 quyết định, ba mục có `ngay_khoi_dong=2026-08-21` |

---

## 7. Vướng vấp

**7.1 — Agent sai HAI LẦN TRONG MỘT NGÀY về cùng một cột.**

| lần | lỗi | chiều |
|---|---|---|
| 18:40 | đếm 12 lượt 64 ký tự **quên lọc** `run_source` ⇒ tưởng MN official chạy prompt hỏng | **quên lọc** |
| 19:xx | quét lượt rỗng **lọc thừa** `run_source` ⇒ bỏ sót toàn bộ model shadow | **lọc thừa** |

Cùng một gốc: **viết mệnh đề lọc trước khi hỏi rõ câu hỏi đang đo cái gì**. Lần một đo *"lượt
nào ảnh hưởng bảng điểm official"* — phải lọc. Lần hai đo *"model nào hay lỗi"* — **không được
lọc**, vì model shadow cũng là model đang được chấm.

**7.2 — Owner phải là người bắt ra.** Cả hai lần agent đều **không tự thấy**; lần một do phản
biện bắt, lần hai do **owner hỏi**. Đây là lý do RM-13 tồn tại — nhưng RM-13 nói về *nguồn đo*,
chưa nói về *mệnh đề lọc*. Đề xuất bổ sung khi mở sổ RM lần tới.

---

## 8. Gỡ về

Phiên này chỉ ghi sổ quyết định. Gỡ về = xoá `QD-045` và trả `ngay_khoi_dong` của ba mục về
`2026-08-08`. Bản trước nằm trong commit `86dc6e9`.

---

## 9. Theo dõi tiếp

| mã | nhãn | hạn | trạng thái |
|---|---|---|---|
| **FU-355 · SC2108-2** | lượt rỗng bị chấm `LOSE` — dìm điểm oan tới **7,1 điểm** | 21/08 | `OWNER_DECISION_NEEDED` |
| **FU-356 · KS0909** | `glm-5.2` rỗng ở MB — theo dõi, chưa phải bệnh kinh niên | 09/08 | `WAIT_LIVE` |
| **FU-354 · QD0909** | bốn quyết định «SAU 08/08» | — | `CLOSED_PASS` (QD-045) |

### LOCK-IN

- `QD-015` · `QD-016` · `QD-017` khởi động **21/08**, lý do ghi trong từng mục
- `OD-20260801-B` **đã xong**, không dời
- Cách chấm hiện tại **giữ nguyên** tới khi owner ký — mọi báo cáo xếp hạng từ nay phải **ghi
  kèm số lượt rỗng**

### NEXT ACTION — một bước

**Sáng 09/08: deploy cổng `_v11023_canh_thieu_so.py`, và BỎ mệnh đề lọc `run_source` để nó soi
cả shadow.** Nghiệm thu: chạy với ngày **08/08** phải bắt được **cả** `deepseek-reasoner` MT
**và** `glm-5.2` MB.

### Câu cần owner ký

**FU-355** — *"Lượt model không trả lời đang bị chấm thành THUA, làm `gemma-4-31b` bị dìm 7,1
điểm và bảng xếp hạng thăng hạng đứng trên số sai. Sửa cách chấm — anh cho làm sau 21/08 cùng
đợt mở khoá, hay mở khoá sớm?"*
