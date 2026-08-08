# REPORT V11036 — VÁ NO_ANSWER + HAI CÂU OWNER HỎI ĐỀU CHƯA ĐO ĐƯỢC

**Ngày:** 2026-08-08 đêm · **Owner ký:** QD-046 *"mở khóa làm luôn"*
12 agent đo + phản biện đối kháng

---

## 1. Tóm tắt

| | |
|---|---|
| **A · ĐÃ VÁ** | lượt không-trả-lời không còn bị tính THUA. Deploy đạt cả hai đầu, **138 dòng** đổi nhãn trên DB thật |
| **B · `/nghiem-thu`** | owner **nhìn đúng bề mặt** (23,8% → 80,0%), nhưng **CHƯA ĐƯỢC PHÉP KẾT LUẬN**. Cái khá lên **thật** là **ĐỘ PHỦ** |
| **C · Model tiến triển?** | **CHƯA ĐO ĐƯỢC** — và cửa sổ SAU **thực chất chưa bắt đầu** |
| **⚠ Nguy nhất** | `decide()` chỉ cần **2 ngày may** nữa là lật sang *«ĐẠT — trình owner duyệt thay official»* mà **không có phép ý nghĩa nào**. Hạn 19/08, còn 11 ngày |

---

## 2. Owner yêu cầu gì (NGUYÊN VĂN)

> mở khóa làm luôn, đồng thời xem luồng /nghiem-thu cũng khá dần lên đó em. Và đánh giá sau khi
> thay đổi prompt ngữ cảnh thực sư, số hóa ML thực sự thì các model có tiến triển gì không em?

---

## 3. A · ĐÃ VÁ — NO_ANSWER

### 3.1 Ba việc, vá cả ba đầu

| # | chỗ | TRƯỚC | SAU |
|---|---|---|---|
| 1 | `scheduler.py:9327` | chép `row['status']` = `'LOSE'` | `'NO_ANSWER'` khi `main_nums` rỗng |
| 2 | `combo_super.py:328` | `SUM(bt_hit)/COUNT(*)` — đếm cả lượt rỗng vào **mẫu số** | loại lượt rỗng + thêm khoá `rong` |
| 3 | `model_daily_eval` | **138 dòng** `LOSE` | `NO_ANSWER` — **chỉ đổi cột `status`** |

**Vì sao lọc theo NỘI DUNG `main_numbers` chứ không theo `status`:** như vậy đúng ngay trên
**toàn bộ lịch sử**, không phụ thuộc dòng cũ đã đổi nhãn hay chưa.

### 3.2 Tác động thật lên bộ chọn model bỏ phiếu

| cửa sổ | đổi gì |
|---|---|
| **7 ngày** | MT `deepseek-reasoner` 42,9% → **50,0%** · MB `qwen3.7-max` 16,7% → **20,0%** |
| **30 ngày** | 21 ô model×miền; nặng nhất **MB `gemma-4-31b` n 20→9** (11 lượt rỗng), 5,0% → **11,1%** |

**0 model rớt sàn `MIN_MAU_DU_TUYEN=5`** ⇒ không mất ứng viên nào.

### 3.3 ⚠ BĂM 4 BẢNG KHOÁ ĐỔI — CÓ CHỦ Ý

`model_daily_eval` `34dd1369e5ed946f` → bản mới. **Lần đầu** trong chuỗi phiên này một bảng
khoá bị sửa có chủ ý. Ghi rõ để phiên sau **không báo động nhầm** (RM-02).

Kiểm trước khi sửa: cả 138 dòng đều `status='LOSE'` **và `bt_hit=0`** ⇒ đổi nhãn **không** làm
đổi bất kỳ tỉ lệ nào đang tính bằng `SUM(bt_hit)`; nó chỉ làm dữ liệu **nói đúng sự thật**.
Sao lưu đủ mọi cột: `backups/v11036_pre/` **cả hai đầu**.

**Deploy:** PID `1053968 → 1089328` · health **200** · backfill DB thật
`còn LOSE rỗng: 0 · đã NO_ANSWER: 138` · `NO_ANSWER_V11036=DAT`.

---

## 4. B · `/nghiem-thu` — anh nhìn đúng bề mặt, số không chịu nổi phép kiểm

**Bề mặt:** bạch thủ **5/21 (23,8%) → 4/5 (80,0%)** từ 07/08. **Đúng, tái lập được.**

### 4.1 Vì sao chưa kết luận được

| | |
|---|---|
| **Đo tiến chỉ từ 30/07** | `FROZEN_FROM` (`_v10879_nghiemthu_lane.py:71`). **135 hàng trước đó** tính lại retro trong **MỘT lượt** lúc `2026-07-30T10:57:16` |
| **Trừ nền hai bên (RM-18)** | TRƯỚC −10,7pp (z −0,61) · SAU +41,6pp (z +1,15). Chênh **+52,3pp**, z **+1,30** — không đủ |
| **MDE ở n=5** | **104,1pp** — cửa sổ này **không phát hiện nổi** thứ gì nhỏ hơn 104 điểm |

### 4.2 Phản biện siết chặt thêm — ba đính chính

1. **Thiếu một miền-ngày, và nó là LOSE.** MB 08/08 chấm **19:10**, DB đồng bộ **18:39**.
   Chấm tay `93 → LOSE`. Vá đủ: **4/6 = 66,7%**, z **+1,96 → +1,60**, hai cửa sổ z **+1,11**.
   Con số gốc rơi **đúng ngay ngưỡng 1,96** — không được trích.
2. **MDE dùng công thức MỘT MẪU** cho câu hỏi HAI MẪU. Đúng là **106,5pp**.
3. **«~46 ngày nữa soi được 20pp» SAI NẶNG.** Cửa sổ TRƯỚC **đã đóng băng trong quá khứ**,
   không nở ra ⇒ **sàn MDE 50,2pp** dù n_SAU vô hạn. **Mức 20pp KHÔNG BAO GIỜ đạt bằng cách
   chờ.** Phải **đổi thiết kế đo**.

### 4.3 Quy công cho đợt vá prompt là SAI

Trong 5 miền-ngày «SAU», **chỉ 1** (MT 08/08, chạy 16:48) thật sự dùng prompt đã vá đủ.
MN 08/08 chạy **05:32** — trước cả V11032 (10:27) lẫn V11033 (13:47).

### 4.4 Đối chứng — không nhúc nhích

Official: +3,6pp → +1,6pp, **z −0,05**.
McNemar trên đo tiến: chỉ NEW **3** · chỉ official **4** · **p = 1,0**.
**De-herd chưa hơn official một chút nào khi chạy thật.**

### 4.5 ✓ Cái DUY NHẤT khá lên THẬT: ĐỘ PHỦ

30/07–03/08 **lỡ 3 miền-ngày** → 04/08–08/08 **đủ 15/15** sau vá cron V10977.

### 4.6 ⚠ HAI LỖI TRONG CHÍNH LUỒNG NÀY

| lỗi | hại |
|---|---|
| `_discordant()` — `both_lose` ra **−1** (số âm), backfill 33 thay vì 40 | thổi phồng bảng *«Chỗ đáng nhìn nhất»* |
| **`decide()` chỉ cần 2 ngày may là lật sang «ĐẠT — trình owner duyệt thay official»** | **không có phép ý nghĩa nào**. Hạn **19/08**, còn 11 ngày. **Cổng có thể nói dối owner** |

---

## 5. C · Model có tiến triển không — **CHƯA ĐO ĐƯỢC**

**Lý do nghiêm trọng hơn owner tưởng: cửa sổ SAU thực chất CHƯA BẮT ĐẦU.**

### 5.1 Runtime ≠ commit

«Sáu lần đổi prompt» là mốc **COMMIT**. Runtime chỉ có **BỐN** bản:
`PB-18.1/CTX-16.5` (hết 06/08) → `PB-18.4` (**chỉ MN sáng 07/08, 20 lượt**) →
`PB-20.0` (MT+MB chiều 07/08) → `PB-20.1`.

### 5.2 Phép mạnh nhất kho này dựng được

Có ngữ cảnh vs ngữ cảnh **hỏng**, so **trong cùng model** (bỏ hết khác biệt giữa model,
nền đúng từng bên):

| cách đặt phép | HIỆU | z | MDE | |
|---|---|---|---|---|
| gộp (n 4.005 vs 888) | +3,65 | +1,24 | 8,25 | chưa vượt |
| sau **dedupe** (trace có **1.061 dòng trùng**) | +3,15 | +1,04 | 8,51 | chưa vượt |
| **chỉ ngày có CẢ HAI** | **+1,67** | **+0,50** | | chưa vượt |
| trong cùng model (17 model ≥25 lượt/nhánh) | +3,28 | +0,94 | 9,8 | chưa vượt |

**Chuỗi +3,65 → +3,15 → +1,67 cho thấy phần lớn dấu dương là CHÊNH THÀNH PHẦN NGÀY.**

### 5.3 Prompt dài thêm KHÔNG đi kèm trúng nhiều hơn

r = **+0,0337**, n_eff 1.312, **t = +1,22** — không ý nghĩa.
Bốn nhóm độ dài: Q1 −1,80 · Q2 +2,04 · Q3 −1,15 · **Q4 (dài nhất) +1,39** — **không đơn điệu**.

### 5.4 Bằng chứng lịch sử đắt giá

Lần đổi prompt DUY NHẤT đủ sức mạnh (`PB-18.0→18.1`, 18/07, **gấp 20 lần n hiện tại**) cũng
**không kết luận được gì** — z −0,37, MDE 12,84.

### 5.5 ⚠ ĐÍNH CHÍNH: «prompt dài thêm ~1.620 ký tự»

Ghép cặp cùng (miền, model) 07/08→08/08, n=55: trung vị +1.766. **Tách ra:**

| | chênh tổng | chênh ngữ cảnh |
|---|---|---|
| MT + MB (36 cặp) | **+1.792** | +1.267 |
| **MN (19 cặp)** | **−10.475** | **−11.222** |

**MN NGẮN ĐI hơn 10.000 ký tự.** Công bố như mệnh đề toàn hệ là **vi phạm RM-09**.

### 5.6 Bẫy chưa nổ nhưng còn đó

`database.py:2986` — `UPDATE predictions SET status/... WHERE date=? AND target_region=? AND
ai_model=?` **không lọc `run_source`**. Kiểm 30 ngày: **0 khoá trùng** ⇒ chưa nổ.
**Nổ khi nào:** một model chạy **cả hai đường** — đúng việc `QD-015/016/017` sẽ làm **21/08**.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| Tuổi dữ liệu | **ĐẠT** — 0,99 giờ |
| Backfill local | **ĐẠT** — 138 dòng, **chỉ cột `status` đổi**, đối chiếu từng cột |
| Backfill VPS | **ĐẠT** — `còn LOSE rỗng: 0 · đã NO_ANSWER: 138` |
| md5 3 tệp local = VPS | **ĐẠT** |
| PID trước/sau | **ĐỔI** `1053968 → 1089328` |
| health | **200** |
| `NO_ANSWER_V11036` | **ĐẠT** — 4/4 phép |
| **Băm 4 bảng khoá** | **ĐỔI CÓ CHỦ Ý** — ghi rõ, có sao lưu hai đầu |
| Không đưa runtime artifact vào bundle | **ĐẠT** |

---

## 7. Vướng vấp

**7.1 — Agent suýt vá NỬA VỜI.** Bản đầu chỉ định vá `scheduler.py`. Nhưng chỗ **thật sự** dìm
điểm là `combo_super._ti_le_bach_thu()` với `COUNT(*)` trần — vá `scheduler` mà không vá chỗ đó
thì **138 dòng lịch sử vẫn tiếp tục làm sai bảng xếp hạng**. Phải soi **ai ĐỌC bảng**, không
chỉ ai ghi (§60.2).

**7.2 — Agent vá BẢN SAO trước, suýt tưởng xong.** Backfill chạy ở máy local chỉ sửa bản sao;
DB thật nằm trên VPS và sẽ **ghi đè bản sao local** ở lần đồng bộ sau. Phải chạy backfill
**trên VPS**, nếu không việc vá coi như chưa làm.

**7.3 — Con số agent đã báo owner bị đính chính hai chỗ:**
- «5 lượt rỗng/30 ngày» → thật là **44** (báo cáo V11035 đã sửa)
- «prompt dài thêm ~1.620 ký tự» → chỉ đúng **MT+MB**; **MN ngắn đi 10.475**

**7.4 — Đây là biến thứ BA trong ngày** (sau V11032, V11033). `QD-018` «một biến một lần» bị
nóng. Owner **chủ động** yêu cầu *"mở khóa làm luôn"* nên thi hành, nhưng phải ghi rõ: cửa sổ
đo FU-284 nay có **ba** thay đổi chồng trong 08/08 — may là 08/08 **đã bị loại** khỏi cả hai
cửa sổ đo (SAU bắt đầu 09/08).

---

## 8. Gỡ về

```bash
cp backups/v11036_pre/combo_super.py.pre web/backend/combo_super.py
cp backups/v11036_pre/scheduler.py.pre   web/backend/scheduler.py
# 138 dòng: khôi phục từ backups/v11036_pre/model_daily_eval_138_dong_rong.json
#           (VPS: backups/v11036_pre/mde_rong_vps.json)
```

---

## 9. Theo dõi tiếp

| mã | nhãn | hạn | trạng thái |
|---|---|---|---|
| **FU-355** | NO_ANSWER — đã vá, 09/08 kiểm dòng mới | 09/08 | `DEPLOYED_PENDING_LIVE_VERIFY` |
| **FU-357 · KS1908** | **`decide()` có thể nói dối owner** + `both_lose = −1` | 19/08 | `MEASURED_ROOT_CAUSE` |
| **FU-358 · DO2209** | `/nghiem-thu` — cửa sổ TRƯỚC đóng băng, phải đổi thiết kế đo | 22/09 | `WAIT_LIVE` |
| **FU-359 · DO2108-3** | model tiến triển — chưa đo được, đọc lại 21/08 | 21/08 | `WAIT_LIVE` |
| **FU-360 · SC1408-2** | `verify_prediction` không lọc `run_source` — **phải vá TRƯỚC 21/08** | 14/08 | `MEASURED_BUT_NOT_FIXED` |

### LOCK-IN

- Lượt không-trả-lời **không còn bị tính thua**, cả forward lẫn lịch sử
- `/nghiem-thu`: cái khá lên **thật** là **ĐỘ PHỦ** (15/15), **không phải** tỉ lệ trúng
- Model tiến triển: **chưa đo được**, và **chưa được phép nói có hay không**

### NEXT ACTION — một bước

**Vá `decide()` (FU-357): bắt nó đòi z ≥ 1,96 trên ĐO TIẾN trước khi được ghi «ĐẠT».**
Lane test, **QD-041 không chặn**, làm được ngay. Nếu để nguyên, ngày 19/08 nó có thể trình
owner một kết luận sai với p thật = 1,0.
