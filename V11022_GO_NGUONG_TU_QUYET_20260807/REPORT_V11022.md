# REPORT V11022 — GỠ NGƯỠNG TỰ QUYẾT (L-B) + KIỂM TỔNG LỰC SAU CHU KỲ LIVE 07/08

> **Ngày:** 2026-08-07 tối · **Đã deploy** · PID `982337 → 993241` · 4 bảng khoá Y HỆT
> **L-B sống đúng MỘT chu kỳ live rồi bị gỡ. Người bắt ra là OWNER, không phải agent.**

---

## 1. Tóm tắt

Owner yêu cầu kiểm tổng lực sau chu kỳ live. Kiểm ra **ba việc tốt, ba việc phải sửa**, và
**một lỗi nghiêm trọng agent đã bỏ sót** — owner chỉ ra.

**Việc tốt:** cơ chế V11016 chạy đúng thiết kế · MB đạt phân tán **0,69 cao nhất 9 ngày** ·
kho mã sạch **0 chỗ** ghi tệp không đóng tay.

**Phải sửa:** L-B **đóng một cửa trúng thật** ⇒ đã gỡ · hai cron trùng giờ ⇒ đã tách ·
`node_modules` lọt vào kho ⇒ đã gỡ.

## 2. Owner yêu cầu gì (nguyên văn)

> *"HẾT CHU KỲ LIVE RỒI EM KIỂM TRA TỔNG LỰC TOÀN DIỆN, ĐỐI CHIẾU CÁC VẤN ĐỀ ĐÃ XỬ LÝ HÔM NAY
> CÓ KẾT QUẢ NÀO ỔN KHÔNG, CÓ GÌ CẦN ĐIỀU CHỈNH, CÁC VẤN ĐỀ TỒN ĐỘNG V.V... TẤT CẢ MỌI THỨ
> KHÔNG BỎ SÓT VẤN ĐỀ GÌ NHA EM."*

Rồi sau khi đọc báo cáo đầu tiên của agent:

> *"Anh vẫn thấy tín hiệu có tín hiệu tốt tín hiệu xấu em phải soi chi tiết từng model AI chứ em,
> **phụ 2 có tín hiệu trúng kìa**, 🔬 DeepSeek Reasoner 40% 30d ở MT **lỗi nữa chứ**, Em phải xem
> kỹ chứ"*

## 3. Đào bới / phát hiện

### 3.1 CHỖ AGENT ĐO SAI — owner chỉ ra · `VERIFIED_TEST`

Agent so «1 số vs 2 số» mà **chỉ tính số chính**, báo *"12% vs 22%"*. Con số đó **che mất** sự
thật. Tính cả cửa số phụ:

| miền | prompt | chính trúng | **phụ trúng** | tổng lượt trúng |
|---|---|---|---|---|
| MB | **MỚI** | 3 | **2** | 5 |
| MT | hỗn hợp | 3 | 0 | 3 |
| **MN** | **CŨ** | 8 | **8** | **16** |

Ở MN số phụ trúng **ĐÚNG BẰNG** số chính. Ở MB **hai model chỉ trúng nhờ số phụ**:

```
lstm     ['69', '42']   chính trượt · PHỤ TRÚNG
xgboost  ['25', '94']   chính trượt · PHỤ TRÚNG
```

**Tính theo "trúng ít nhất một số":**

| | bỏ số phụ (1 số) | giữ số phụ (2 số) |
|---|---|---|
| **MB** | **0/4** | **5/12** |
| MT | 1/4 | 2/11 |

### 3.2 `deepseek-reasoner` — owner chỉ đúng · `VERIFIED_TEST`

| ngày | miền | số | ghi chú |
|---|---|---|---|
| **07/08** | **MT** | **`[]`** | verdict SKIP — **RỖNG** |
| **07/08** | MB | `['31']` | chỉ 1 số |
| 06/08 → 01/08 | cả ba miền | luôn **2 số** | |

**07/08 là ngày ĐẦU TIÊN trong 30 ngày** deepseek ra rỗng. 30 ngày trước: **88/93 lượt đều ra
2 số**. Và deepseek không hề tệ — 30 ngày: **MB 48% · MT 58% · MN 68%**.

⇒ Đây là **hồi quy do prompt**, không phải model hỏng.

### 3.3 Cơ chế L-B thì ĐÚNG — nhưng đúng theo hướng có hại

| miền | prompt | tự khai «MỨC TIN» | bỏ số phụ |
|---|---|---|---|
| MB | **mới** | **4/16** | 4 |
| MT | hỗn hợp | 4/16 | 4 |
| MN | **cũ** | **0/16** | **0** |

Đúng 0 ở miền prompt cũ — cơ chế thật. Nhưng thứ nó làm là **bỏ số**.

### 3.4 Ba miền chạy BA prompt khác nhau ngày 07/08

| miền | model chốt lúc | so với deploy 13:35 | phân loại |
|---|---|---|---|
| **MB** | 17:30–17:35 | sau | `SAU_V11016` — **phép đo sạch duy nhất** |
| **MT** | 05:00 **và** 16:39–16:45 | cả hai | `HON_HOP` — loại khỏi trung bình |
| **MN** | 05:00–05:20 | trước | `NEN` |

⇒ Lượt đo bầy đàn đủ 9 phần **sớm nhất là 10/08**, không phải 08/08. FU-325 đã dời hạn.

### 3.5 Kết quả trúng thật — agent báo nguyên văn, không chọn số đẹp

| miền | prompt | bạch thủ | kết quả |
|---|---|---|---|
| **MN** | **cũ** | 13 | **TRÚNG** |
| MB | mới | 60 | trượt |
| MT | hỗn hợp | 58 | trượt |

Miền prompt cũ trúng, hai miền prompt mới trượt. **n = 1 ngày, không kết luận được** — nhưng
phải nói ra.

### 3.6 Tín hiệu từng model — 30 ngày

| nhóm | model (MB / MT / MN) |
|---|---|
| **đều tay cả ba miền** | claude-sonnet-4-6 48/48/**81** · claude-opus-4-6 45/58/71 · deepseek-reasoner 48/58/68 · gemini-2.5-pro 52/58/61 · meta-learning 55/42/77 |
| **yếu rõ ở MB** | random-forest **23%** · combo-no-token **26%** · smart-ml 29% · gpt-oss-120b 29% · gpt-5-mini 29% · lstm 32% · combo-super 32% |

**MB là miền yếu chung của cả nhóm ML** — không phải lỗi một model. MN thì model nào cũng khá
(55–81%).

### 3.7 Bộ tự kiểm 18 đạt / 4 lệch

`C4` khoá `/choi` trước mốc FINAL — **rỗng** · `C5` giờ lane khai `null` nhưng crontab có
`06:05/16:44/17:38` — **trang web lấy giờ từ hằng số này** · `C18`/`C19` biên MT 04/08 mỏng.

### 3.8 FU-312 xác nhận là lỗi thật — **4/7 ngày**

Lane MB chạy 17:38, official chốt xong **sau đó** ở `06/08 (17:45)` · `05/08 (17:39)` ·
`03/08 (17:44)` · `01/08 (17:39)`. Hơn nửa số ngày lane chấm trên **dữ liệu thiếu model**.

## 4. Hướng xử lý và vì sao chọn

**Gỡ L-B, giữ L-A.** Hai thứ ở hai khối riêng nên tách được.

**Lý do quyết định KHÔNG phải thống kê.** L-B trái **quy tắc owner đã chốt**: *luôn ra số, không
bao giờ bỏ số, để owner tự quyết*. Một dòng prompt bảo model *"ra ít mà chắc hơn ra đủ cho đẹp"*
đi ngược quy tắc đó — dù số liệu đẹp hay xấu. Số liệu (0/4 vs 5/12) chỉ là xác nhận thêm.

**Giữ L-A** vì nó **không bỏ số nào**, và MB ngày 07/08 đạt phân tán **0,69 — cao nhất 9 ngày**
(nền 0,474).

**Hợp đồng JSON không đụng.** `secondary_number=""` + `NO_SECONDARY` vẫn hợp lệ như trước
V11016 — chỉ gỡ dòng **khuyên** model dùng quyền đó.

## 5. Đã làm gì

| việc | kết quả |
|---|---|
| **Gỡ L-B** khỏi `_rules_first_live_block` | `CTX-18.0 → 18.1` · `PB-20.0 → 20.1` |
| **Dọn ghi tệp không đóng tay** | 217 tệp tự động + 1 tay ⇒ toàn kho **0 chỗ** |
| **Tách hai cron trùng 19:05** | `_v11018` → **19:25** |
| **Gỡ `node_modules` khỏi kho** | 53 tệp · 19 MB · thêm `.gitignore` |
| **Sửa cổng đếm nhầm chú thích** | `tokenize` ⇒ 231 → **0** |
| **Dời hạn FU-325** | 08/08 → **10/08** |

## 6. Cổng kiểm

| phép | kết quả |
|---|---|
| md5 local = VPS | ✓ `6b28f0baa7aeceac0e9fd2b75a741a81` |
| Cổng prompt 3 miền | ✓ `ngưỡng_tự_quyết_ĐÃ_GỠ` · `khuyên_ra_ít_ĐÃ_GỠ` · `kể_sự_kiện` · `rổ_hợp_nhất_đã_hết` · `rổ_xếp_hạng_đã_hết` · `ép_chọn_đã_hết` |
| PID | `982337 → 993241` ✓ |
| `/api/health` | **200** |
| 4 bảng khoá | ✓ **Y HỆT** — `11956\|25766` · `483\|665` · `15232\|15336` · `11739\|11739` |
| Kho mã: ghi không đóng tay | **0 tệp · 0 chỗ** |
| Cổng đoán tên | ✓ sạch |
| Cổng cắt cụt | ✓ sạch |
| J5 mốc tải | ✓ khớp |
| Journal từ 13:35 | 29 dòng, **toàn bộ** là `SCRAPE_FAIL` MN 16:30–16:34 đã tự phục hồi. **Không lỗi nào từ code hôm nay** |

**Cổng deploy chặn đúng một lần nữa:** lần chạy đầu script vẫn đòi `nguong_tu_quyet=True` (chép
từ V11016) ⇒ **dừng trước restart**. Phải sửa phép kiểm cho khớp việc mới.

## 7. Vướng vấp

**Agent đo thiếu một chiều và suýt để nguyên.** Báo *"1 số 12% vs 2 số 22%"* — con số đúng
nhưng **chỉ tính số chính**, che mất chuyện nhóm bỏ số phụ trúng **0/4**. Owner đọc ra ngay:
*"phụ 2 có tín hiệu trúng kìa"*.

Đây là lỗi **cùng họ** với những lỗi khác trong ngày: **đo cái mình nghĩ là quan trọng, không đo
cái đang thật sự xảy ra**.

**Và ba lỗi cẩu thả nữa trong cùng buổi tối:**

1. `git add web/backend/` quét cả **`node_modules` 19 MB** vào kho
2. Cổng vừa dựng **tự đếm nhầm chú thích của chính nó** ⇒ báo 231 chỗ sau khi đã dọn sạch
3. Lệnh `sed` sửa cron **không ăn mà vẫn báo chạy xong** — phải đọc lại đầu ra mới thấy

## 8. Gỡ về

```bash
# VPS
cp /root/Lottery_AI_Test/backups/gpt_analyzer.py.v11022_pre \
   /root/Lottery_AI_Test/web/backend/gpt_analyzer.py && systemctl restart lottery
# local — bản có L-B
cp backups/v11022_pre/gpt_analyzer.py.pre web/backend/gpt_analyzer.py
```

md5 bản trước `96f6073cadafa73fb1542fe6e9c8e0b6` (= PB-20.0, có L-B).
Dọn ghi tệp: `backups/v11021_don_ghi/` giữ nguyên 217 bản gốc.

## 9. Theo dõi tiếp

| Mã | Nội dung | Trạng thái | Hạn |
|---|---|---|---|
| **FU-322** | L-B — **đã gỡ**, sống đúng 1 chu kỳ live | `ROLLED_BACK` | 07/08 |
| **FU-324** | Dọn ghi tệp không đóng tay — **0 chỗ** | `CLOSED_PASS` | xong sớm |
| **FU-328** | **Canh model ra THIẾU SỐ** — deepseek ra rỗng mà không cổng nào báo | `MEASURED_ROOT_CAUSE` | **08/08** |
| **FU-325** | Lượt đo bầy đàn sạch — **dời 08/08 → 10/08** | `WAIT_LIVE` | **10/08** |
| **FU-312** | MB lane 17:38 — xác nhận sai **4/7 ngày** | `MEASURED_ROOT_CAUSE` | 08/08 |
| **C4 · C5** | Bộ tự kiểm còn 4 phép lệch | chưa mở mục | — |
| **FU-215** | Đóng băng QD-014 hết hạn | **chờ owner** | **08/08** |

**Ngưỡng hành động FU-328:** ≥1 model ra rỗng, hoặc ≥3 model ra 1 số ⇒ **báo động trong ngày**,
không đợi ai đọc bảng. Ca deepseek hôm nay lọt qua vì bundle vẫn dựng, vẫn `ACTIVE`, chỉ thiếu
một phiếu — **im lặng**.

**Điều owner cần biết ngay:** phép đo bầy đàn cần **3 ngày × 3 miền sạch**. Từ 08/08 cả ba miền
mới cùng chạy prompt mới trọn ngày ⇒ **đừng đổi prompt thêm gì tới 10/08**, nếu không lại chồng
biến lần thứ tư.
