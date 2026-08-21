# REPORT V11095 — NGÀY MỞ GÓI 21/08: THI HÀNH, VÀ BỐN THỨ CHỈ LỘ RA KHI ĐỘNG VÀO

**Ngày:** 2026-08-21 · **Mã đọc:** `HT2108` · **Quyết định:** `QD-068`
**`QD-041` HẾT HIỆU LỰC.** **KHÔNG DEPLOY** — mọi mục dừng ở `CODE_PUSHED`, production chạy bản cũ.

---

## 1. Tóm tắt

Gói **12 mục thực thi + 1 thiết kế** mở khoá sáng nay. Kết quả:

| | |
|---|---|
| **thi hành xong** | **4 mục** — `FU-380` · `#12 latency_score` · `FU-404` · `FU-397b` |
| **thiết kế xong, chờ duyệt** | **1** — `FU-290A` |
| **KHÔNG thi hành, có lý do** | **`#4 FU-394`** — tiền đề của mục bị **lật** · **`D2`** — bảng kiểm bảo dừng |
| **chờ owner** | **8 mục** (`#1 FU-393` · `#9 FU-299` · `#10 FU-300` · `#5 FU-395` C1/C3/C5/C6…) |
| hash 4 bảng khoá | **PRE = POST**, không đổi một byte |
| cổng | **12/12 xanh** · `_v11062` ĐẠT · **không dùng cờ bỏ qua lần nào** |

**Điều đáng nói nhất không phải 4 mục đã làm, mà là bốn thứ chỉ lộ ra khi đụng vào chúng.**
Cả bốn đều **không** nằm trong gói, và cả bốn đều đổi cách đọc những phép đo đã có:

| # | phát hiện | vì sao đổi cách đọc |
|---|---|---|
| **①** | **prompt production không ổn định giữa hai lần chạy** | mọi phép đo prompt A/B — kể cả `FU-284` — có nhiễu **chưa ai trừ ra** |
| **②** | nhãn `HR12W` có lúc **nói NGƯỢC** | **13/105 luật dưới nền**, một số đeo nhãn *«hoàn hảo»* |
| **③** | **phần GAN của bộ lọc chưa từng chạy** | một cơ chế production **chết**, mà **log vẫn in như đang sống** |
| **④** | cắt model theo độ trễ **không có cơ sở** | biên **220 phút**, lượt tệ nhất **23,8 phút** |

---

## 2. Owner yêu cầu gì (nguyên văn)

> **PROMPT TỔNG LỰC LẦN 22 · sáng 21/08** — *«GO 21/08: THỰC THI GÓI 12 MỤC + 1 THIẾT KẾ …
> `QD-041` HẾT HẠN · thực thi theo `docs/BAN_DO_THUC_THI_2108.md` ĐÃ CHỐT tối 20/08.»*

> *«L1 → L2 → L3 đúng bản đồ · bảng kiểm 10 bước · mỗi mục một commit riêng, revert độc lập.»*

> *«Va chạm `D2` × `FU-397b`: CẤM GỘP — `D2` tắt đúng thứ `FU-397b` đang đo; thứ tự trong bản đồ
> có lý do từng vị trí, không được đổi.»*

> *«`FU-290A`: VIẾT THIẾT KẾ TRƯỚC (trả lời đủ 3 câu §59) → trình owner duyệt → mới thi hành.»*

> *«Miễn trừ K8 (`QD-066`) HẾT HẠN HÔM NAY: `FU-360`/`FU-389` phải được xử trong phiên; nếu chưa
> xử thì K8 đỏ lại là CỐ Ý — phải ghi rõ, cấm im.»*

> *«không tự thêm/bớt mục khỏi gói (`QD-064`) — phát hiện mới → `CHO_OWNER` · cổng chặn thì VÁ
> CHO ĐẠT THẬT, cấm cờ bỏ-qua.»*

---

## 3. Đào bới / phát hiện

### 3.1 · ① PROMPT PRODUCTION KHÔNG ỔN ĐỊNH — `FU-416`

Phát hiện này sinh ra từ **một dòng diff em không giải thích được**. So prompt TRƯỚC/SAU cho
`FU-404` thì thấy một dòng đổi mà bản vá **không đụng tới**. Thay vì cho qua:

| phép | MN | MT | MB |
|---|---|---|---|
| **hai lần chạy CÙNG MÃ**, cùng miền, cùng ngày | **6 dòng khác** | **6 dòng khác** | **2 dòng khác** |
| đặt `PYTHONHASHSEED=0` | **0** | **0** | **0** |

⇒ **prompt đổi nội dung theo hạt băm chuỗi của từng tiến trình Python.**

**Đích danh** `gpt_analyzer.py:5941`:

```python
ranked = sorted(candidate_tails.items(), key=lambda x: -x[1])[:10]
```

Sắp xếp **chỉ theo điểm, không phá hoà bằng khoá**. Đuôi cùng điểm giữ thứ tự chèn của `dict`,
mà thứ tự đó đến từ `set` ⇒ đổi theo hạt băm. Rồi `[:10]` và `fresh_carry[:6]` **CẮT**.

**Đo 21/08 — và đây là chỗ nó thành nghiêm trọng:**

| miền | đuôi hoà điểm | hậu quả |
|---|---|---|
| MN | 2/3 hoà tại `0,0242` | thứ tự 2–3 ngẫu nhiên |
| **MT** | 2/3 hoà tại `0,1207` — **đúng hai vị trí đầu** | **số model nhìn thấy TRƯỚC TIÊN do hạt băm** |
| **MB** | 5/6 trong nhóm hoà, gồm cả top-2 | như trên |

**Không phải xáo thứ tự cho vui — nó đổi SỐ NÀO tới được model.** Mọi so sánh prompt A/B trong
dự án đang có nhiễu này **chồng lên tín hiệu**. `FU-284` đo ba miền × 12 ngày mà không biết mỗi
lượt gọi có thể nhận **một prompt khác**.

**Vá đề nghị một dòng:** `key=lambda x: (-x[1], x[0])`.
**Không làm hôm nay** — prompt đã đổi vì `FU-404`, thêm biến thứ hai là đúng vết `QD-018`.

### 3.2 · ② NHÃN `HR12W` CÓ LÚC NÓI NGƯỢC — `FU-404`

Sổ mô tả *«nói quá»*. Đo lại thì nặng hơn:

| luật (đo 21/08) | prompt hiển thị | lợi thế thật cùng dòng |
|---|---|---|
| `MN/Hà Nội G6+G7` | `HR12W = 1.0` | **−3,88% · KÉM NỀN** |
| `MN/Nam Định G1+G7` | `HR12W = 1.0` | **−1,62% · KÉM NỀN** |

**13/105 luật có `lift ≤ 1,0`.** Và `1.0` gần **mức sàn** chứ không phải đỉnh: `HR12W` đếm
*«tuần đó có ÍT NHẤT MỘT trong 3–4 số trúng»* ⇒ **105/105 luật đạt ≥ 40%**, trung bình `0,8675`.

> ### ⚠️ `PRJ-SELECTION-WINDOW-001` mục 3 — PHẢI BÁO CẢ HAI VẾ, và đây là vế còn lại
>
> **Cổng `_v11088` bắt đúng chỗ này**, nên ghi rõ thay vì lách: `lift_365` là số đo **TRONG cửa
> sổ chọn** — cùng cửa sổ 365 ngày đã dùng để đào và xếp hạng chính các luật đó.
>
> | vế | tình trạng |
> |---|---|
> | **TRONG cửa sổ chọn** | `lift_365` trải **0,8634 → 1,4159** · **13/105 luật ≤ 1,0** · TB `1,1058` |
> | **NGOÀI cửa sổ chọn** | **CHƯA ĐO ĐƯỢC** — và hôm nay mới vừa có điều kiện để đo *(xem `FU-397b`, mục 3.5)* |
>
> Prompt production **đã tự nói** vế thứ hai từ trước, tại `gpt_analyzer.py:4805`: *«các mốc HR
> 4W/12W/16W ở trên đều đo TRONG cửa sổ đã đào ra chính các luật đó, nên là điểm tự chấm.
> **Đo tiến ngoài cửa sổ hiện ngang bằng luật giả.**»*
>
> **Đọc cho đúng, cả hai chiều:** con số `−3,88%` **không** phải bằng chứng luật đó tệ ngoài mẫu
> — nó là bằng chứng luật đó tệ **ngay trong cửa sổ ưu ái nhất nó có**. Đó là điều làm nhãn
> `HR12W 1.0` thành nói ngược, chứ không phải một phán quyết ngoài mẫu.
> Và `RM-18` nhắc đúng chỗ này: luật hơn nền **+7,5 / +13,8 / +20,7 điểm** *trong* cửa sổ chọn
> và **đúng bằng 0** ngoài cửa sổ.

> **Hai chỗ sổ ghi SAI ĐƯỜNG, chỉ lộ khi dump prompt thật (`RM-13` · `RM-14`):**
>
> **(a)** Sổ trích *«`CTX-18.3` CÓ khối `[V2-RULES]` … `HR12W 1.0 (n=20)`»*. Nhưng `[V2-RULES]`
> ở `_v10781_context_pack_v2.py`, mà **chính tệp đó tự khai dòng 26**: *«Chỉ
> `_v10781_prompt_v2_lane.py` (cron riêng) dùng nó»* — **lane A/B**. `CTX-18.3` thật ở
> `gpt_analyzer.py:844`. **Dump production: chuỗi `HR12W` xuất hiện 0 lần** ở cả ba miền.
> Tin sổ mà không dump thì đã đi sửa một tệp **không ai chạy**.
>
> **(b)** Vế *«trạng thái ngoài mẫu»* mà sổ đòi **ĐÃ CÓ SẴN** tại `gpt_analyzer.py:4805` từ
> trước. Phần thiếu thật là **lợi thế trên nền**.

### 3.3 · ③ PHẦN GAN CỦA BỘ LỌC CHƯA TỪNG CHẠY — `FU-394`

Mục này treo suốt vì tin `×0,3` đang dìm số gan cao. **Đo 21/08: nhánh đó chưa chạy lần nào.**

`analyze_gan()` trả dict **BỐN KHOÁ** (`gan`/`top_20_gan`/`avg_gan`/`max_gan`); số nằm ở tầng
trong `gan_data['gan'][num]['gan_days']`. Nhưng `combo_super.py:607` đọc `gan_data.get(num, 0)`
— `'02'` **không phải khoá tầng ngoài** ⇒ **luôn `0`** ⇒

```python
if gan_days <= 8:   # 0 <= 8 → LUÔN ĐÚNG
    score *= 0.6
else:
    score *= 0.3    # KHÔNG BAO GIỜ TỚI
```

**Xác nhận bằng đo:** nhóm `COLD + gan>8` = **0 số cả ba miền**, trong khi MB **thật sự có**
`75`:15 ngày · `98`:15 · `01`:14, và **`01` đúng là `COLD`**.

**Cùng họ lỗi (`RM-07`) — chỗ thứ hai NẶNG HƠN.** Quét 9 nơi gọi `analyze_gan`, phân loại:
**1 đúng · 6 truyền nguyên dict (đúng) · 2 SAI TẦNG**:

| chỗ | hậu quả |
|---|---|
| `combo_super.py:607` | nhánh `×0,3` chết |
| **`post_filter.py:120`** | `gan_days` luôn 0 ⇒ **toàn bộ nhánh THAY SỐ (`:147-159`) chưa từng chạy** |

`post_filter.apply_hot_cold_filter` được gọi từ **`main.py:8637`** · **`scheduler.py:4411, 5738`**
⇒ **đường production sống**.

> **Chi tiết xảo quyệt nhất:** nhật ký in `«COLD nhưng GAN=0d (≤10), giữ lại»`.
> Dòng log đó **đọc như bằng chứng cơ chế đang chạy** — thật ra là bằng chứng nó **đang hỏng**.
> Cùng họ `RM-20` nhưng nặng hơn: không phải bảng không ai đọc, mà là **log nói dối**.

### 3.4 · ④ CẮT MODEL THEO ĐỘ TRỄ KHÔNG CÓ CƠ SỞ — `FU-290A`

| | |
|---|---|
| biên trung bình tới mốc chốt | **≈220 phút** |
| lượt chậm nhất từng ghi nhận (`glm-5.1` max) | **1.429,5s = 23,8 phút = 10,8% biên** |
| `p95` của `glm-5.1` | **207s = 3,5 phút = 1,6% biên** |
| lượt `p95 > biên` | `glm-5.1` **1/90** · `deepseek-reasoner` **1/90** · `gpt-oss-120b` **1/92** |

Con số **1** là **nền**, không phải dấu hiệu riêng của `glm-5.1`.

**`TB` và `%trên-đường-tới-hạn` là HAI TRỤC KHÁC NHAU:** `gpt-5.4` nhanh nhất hệ (**15,9s**)
nhưng ở trên đường tới hạn **97,8%**; `gpt-5.5` chậm (**170,4s**) nhưng **0%**.

Ngưỡng `TB > 180s` sẽ cắt ba model, **hai trong ba không mua được gì**: `kimi-k2.5` **ngừng chạy
từ 29/07**, `qwen3.7-max` **không nằm trong pool**.

Và **4 model ML không có một dòng đo nào** — chạy local, không qua API. ML **chạm sàn 4** ⇒
**không cắt được ML nào**.

### 3.5 · Các phát hiện nhỏ hơn nhưng có thật

| | |
|---|---|
| **cổng đóng băng `QD-041` LỆCH MỘT NGÀY** | so `hôm_nay > 21/08` ⇒ **khoá đúng cái ngày** mọi văn bản khác coi là ngày làm việc |
| **bản đồ xếp NHẦM LÀN cho `#1 FU-393`** | mô tả *«đổi tên tệp, không chạm logic, LÀN 1»* — thật ra là **thêm roster** với `strength_calibrator.py` gọi ở **7 chỗ** đường chính thức |
| **`_v10759_money_board.py:35`** | chú thích **tự khai** *«registry 15/15 khớp fallback»* — **nay SAI** |
| **`model_latency_cost_audit_daily`** | chết **107 ngày**, `latency_available=1` = **0/4.033**, nhưng còn **2 điểm đọc SỐNG** trong `main.py` |
| **hook cổng commit** | dùng **đường dẫn tương đối** ⇒ sau một lệnh `cd` vào thư mục con thì **mọi** lệnh Bash bị chặn cứng, kể cả `cd` quay về |

---

## 4. Hướng xử lý và vì sao chọn

**Vì sao `#12 latency_score` KHÔNG gỡ thẳng.** Chỉ số ấy chết thật (`0,5` ở cả **7.981** dòng,
nguồn chết 107 ngày). Nhưng gỡ thẳng **không trung tính**: điểm đi qua `final *= 0.55` khi model
chưa đo được, nên bỏ hằng số `0,05` làm nhóm **đo được** mất `0,05` còn nhóm **chưa đo** chỉ mất
`0,0275` ⇒ hình phạt bị **chỉnh lại ngầm**. Đo được **1.115/109.426 cặp đảo chiều**, **100%** là
cặp *(đo được × chưa đo)*, **930 cặp chạm `SELECTED_VOTER`**. Nên giữ hằng số dưới tên
`DI_SAN_LATENCY` **hiện nguyên hình**; công thức mới tái lập điểm cũ **7.981/7.981, lệch 0**.

**Vì sao `#4 FU-394` KHÔNG vá.** Vá lỗi tra tầng = **kích hoạt hai cơ chế ngủ đông trên
production**, trong đó một cơ chế chính là thứ mục ấy gọi là *«ngược thiết kế owner»*. Sửa đúng
kỹ thuật mà **sai phạm vi** (`RM-05`).

**Vì sao `D2` KHÔNG chạy.** Bảng kiểm bước 6 ghi *«DỪNG — `D2` chỉ chạy khi `FU-397b` đã có cửa
sổ đo riêng đủ dài»*. Hôm nay `FU-397b` mới vừa có **điều kiện tiên quyết**, chưa có một ngày đo.

**Vì sao KHÔNG DEPLOY.** MN **đã chốt bundle 05:20 sáng nay**. Deploy giữa ngày ⇒ MN prompt
**cũ**, MT/MB prompt **mới** ⇒ **ngày lai** — đúng thứ nhiễu đã giết cửa sổ `FU-284`.
Đề nghị deploy **sau 18:15 tối nay** để **22/08 là ngày sạch đầu tiên** của `CTX-18.4`.

---

## 5. Đã làm gì

| commit | việc |
|---|---|
| `3cea289` | **`FU-380`** — vá hai danh sách cứng fail-closed, **chênh 4 → 0** cả ba miền + cổng `_v11093` thử chặn ĐẠT |
| `e3ebc19` | **`#12`** — gỡ `latency_score`, **số học không đổi** (7.981/7.981, lệch 0) |
| `143a95e` | chốt LÀN 1 + **sửa chỗ bản đồ xếp nhầm làn** cho `#1 FU-393` |
| `b5d9367` | **mở cổng đóng băng `QD-041`** — sửa lệch một ngày |
| `74f3c37` | **`FU-404`** — nhãn luật nói thật, `CTX-18.3` → **`CTX-18.4`** |
| `d0b20f6` | **`FU-397b`** — chặn nhìn trước cho bộ luật + phát hiện `CHỐT GẤP` đi vòng trần |
| `fd19d95` | **`FU-394`** — ghi phát hiện tiền đề bị lật, **không sửa mã** |
| `709efaf` | **`FU-290A` thiết kế** + K8 (`FU-389` đóng · `FU-360` neo theo sự kiện · khai `CODE_PUSHED`) |

**Không dùng `BO_QUA_CONG_COMMIT` lần nào.** Cổng chặn hai lần (`_v11062` thiếu `HISTORY`), cả
hai lần đều **vá cho đạt thật** rồi commit lại.

---

## 6. Cổng kiểm

| cổng | |
|---|---|
| `_v11062 --kiem` K1–K4 | **✓ ĐẠT** |
| `_v10981_kiem_lich` K1–K8 | **✓ 8/8** — mồ côi **2 → 1** |
| `_v11085_cong_rut_lai` · `_v11088_cong_cua_so_chon` | **✓ SẠCH** |
| `_v11028_cong_dong_bang` | **✓** — hết hiệu lực từ 21/08, đúng luật |
| `_v11093_kiem_fu380` (mới) | **✓ thử chặn ĐẠT hai chiều** · `main.py` khôi phục **khớp từng byte** |
| ghi tệp an toàn · đoán tên · mất mục · chéo quyết định · sáu mặt | **✓ 5/5** |
| **hash 4 bảng khoá** | **✓ PRE (09:00) = POST (09:23)** — không đổi một byte |

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| sáng **21/08** | *«GO 21/08: THỰC THI GÓI 12 MỤC + 1 THIẾT KẾ … `QD-041` HẾT HẠN»* |
| sáng **21/08** | *«Va chạm `D2` × `FU-397b`: CẤM GỘP … thứ tự trong bản đồ có lý do từng vị trí»* |
| sáng **21/08** | *«`FU-290A`: VIẾT THIẾT KẾ TRƯỚC → trình owner duyệt → mới thi hành»* |
| sáng **21/08** | *«Miễn trừ K8 HẾT HẠN HÔM NAY … nếu chưa xử thì K8 đỏ lại là CỐ Ý — phải ghi rõ, cấm im»* |
| sáng **21/08** | *«cổng chặn thì VÁ CHO ĐẠT THẬT, cấm cờ bỏ-qua»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| `FU-380` chênh 4 phần tử cả ba miền → **0** | `main.py:466` · `main.py:9462` · cổng `_v11093` |
| `latency_score` = `0,5` ở **7.981/7.981** dòng | `du_doan_test_selected_voters` |
| nguồn `model_latency_cost_audit_daily` chết **06/05**, `latency_available=1` = **0/4.033** | DB |
| gỡ thẳng ⇒ **1.115** cặp đảo, **930** chạm `SELECTED_VOTER` | mô phỏng trên dữ liệu thật |
| prompt **KHÔNG ổn định**: 6/6/2 dòng khác; `PYTHONHASHSEED=0` ⇒ 0/0/0 | `gpt_analyzer.py:5941` |
| `HR12W 1.0` ⇒ lợi thế **−3,88%**; **13/105** luật dưới nền | `mined_rules.lift_365` |
| `analyze_gan` đọc sai tầng ở **2 chỗ**, một chỗ trên production | `combo_super.py:607` · `post_filter.py:120` |
| biên **220 phút** vs lượt tệ nhất **23,8 phút** | `model_latency_shadow_v11063` |
| `QD-015/016/017` còn `ACTIVE`, hạn **08/08**, quá hạn **13 ngày** | sổ quyết định |
| K8 ngày **22/08** ⇒ **TRƯỢT** | `_v10981_kiem_lich.py --hom-nay 2026-08-22` |

### `DOC_SAID`

| tài liệu ghi gì | lệch? |
|---|---|
| `FU-404`: *«`CTX-18.3` CÓ khối `[V2-RULES]`»* | **LỆCH** — khối đó thuộc **lane A/B**; dump production: `HR12W` **0 lần** |
| `FU-404`: cần thêm *«trạng thái ngoài mẫu»* | **LỆCH** — vế đó **đã có sẵn** tại `gpt_analyzer.py:4805` |
| `FU-394`: *«`×0,3` dìm số gan cao»* | **LỆCH** — nhánh đó **chưa từng chạy** |
| `FU-397b`: *«105 luật đào lúc 10/08 00:30»* | **LỆCH** — đo 21/08: `mined_at = 17/08` |
| bản đồ: *«`FU-393` đổi tên tệp, không chạm logic»* | **LỆCH** — là **thêm roster**, 7 điểm gọi đường chính thức |
| `_v10759_money_board.py:35`: *«registry 15/15 khớp fallback»* | **LỆCH** — chú thích **nằm trong mã**, không cổng tài liệu nào soi tới |

### Ba lớp lệch nhau ⇒ FINDING

**`DOC_SAID` ≠ `CODE_DID` ở SÁU chỗ trong một phiên** — và **cả sáu chỉ lộ ra khi chạy mã thật**,
không chỗ nào lộ khi đọc tài liệu. Đây không phải sáu lỗi rời: đó là **một thói quen** — sổ ghi
kết luận **kèm đường dẫn**, nhưng đường dẫn ấy **không được kiểm lại** khi mã đổi. Ba trong sáu
chỗ sai vì **số dòng/tệp đã trôi**, ba chỗ sai vì **chưa bao giờ đúng**.

**`OWNER_SAID` ≠ `CODE_DID`:** owner ký `QD-015/016/017` ngày **02/08** hạn **08/08**; hôm nay
**21/08** cả ba vẫn `ACTIVE` và **chưa chạy**. Và đây không phải chuyện nhỏ — `QD-066` giữ
`FU-360` mở **chính vì chờ ba quyết định ấy chạy**.

---

## 7. Vướng vấp

**① Cổng chặn hai lần, cả hai lần đều vá cho đạt thật.** `_v11062` chặn vì `V11093` rồi `V11094`
chưa có dòng `HISTORY`. Không dùng cờ bỏ qua lần nào.

**② Bộ phân loại của chính em báo động giả — và em suýt tin.** Quét ngược mục `#12` báo *«2 chỗ
còn sót»*. Đọc kỹ thì **cả hai là bắt nhầm**: một là chú thích vừa thêm, một là `latency_class`
— **cột của bảng khác**. Nếu tin phép đếm thì đã đi sửa nhầm hai chỗ đúng (`RM-09`).

**③ Đo một câu hỏi hai lần, ra hai đáp án khác nhau.** Ô *«tập được chọn có đổi không»* ra
**1/281** rồi **0/281**. Chênh do **thứ tự đầu vào phá hoà** trong phép sắp xếp ổn định — artefact
của cách đo. Phải đổi sang phép **đếm cặp đảo chiều** (không dính hoà) mới ra con số đứng vững.

**④ Neo bản vá chép từ trí nhớ, trượt ngay.** Bản vá `FU-404` đầu tiên trượt vì neo thiếu
`AS hr_12w`/`AS composite_score`. Script **dừng trước khi ghi** nên tệp nguyên vẹn — đó là lý do
mọi bản vá phiên này đều bắt neo **khớp đúng một lần**, sai là thoát.

**⑤ Hook cổng commit tự khoá cả phiên.** Sau một lệnh `cd web/backend`, **mọi** lệnh Bash bị chặn
— kể cả chính lệnh `cd` quay về, vì hook chạy **trước** lệnh. Gỡ bằng công cụ PowerShell (thư mục
làm việc riêng).

**⑥ Em đã nói sai một câu và tự đính chính ngay trong phiên.** Em báo mệnh lệnh
`SCAN 12W … HR12W >= 40%` nằm ở **đường chính thức**. Đọc tiếp thì nó nằm trong `if shadow_mode:`
(`gpt_analyzer.py:5550`), có chú thích *«Production path: shadow_mode=False → this block is
skipped entirely»*. **Phép đo 105/105 đạt · 0/105 bị hạ vẫn đúng**, nhưng nó nói về **cổng shadow
PB-18.0**, không phải prompt production. Đính chính trước khi con số ấy đi vào bất kỳ kết luận nào.

---

## 8. Gỡ về

```bash
git revert 709efaf   # FU-290A thiết kế + K8
git revert fd19d95   # FU-394 (chỉ tài liệu)
git revert d0b20f6   # FU-397b   + cp backups/rule_engine.py.pre_v11094_fu397b
git revert 74f3c37   # FU-404    + cp backups/gpt_analyzer.py.pre_v11094_fu404 + DUMP LẠI prompt
git revert b5d9367   # cổng đóng băng
git revert 143a95e   # chốt LÀN 1
git revert e3ebc19   # #12       + cp backups/_materialize_du_doan_test_model_budget.py.pre_v11093_muc12
git revert 3cea289   # FU-380    + cp backups/main.py.pre_v11093_fu380
```

**`FU-404` revert mã KHÔNG ĐỦ** — phải **dump lại prompt** xác nhận nhãn cũ trở lại.
**Chưa deploy** nên production không cần gỡ gì.

---

## 9. Theo dõi tiếp

### Owner cần quyết — **bốn việc**

| # | việc | lựa chọn |
|---|---|---|
| **1** | **DEPLOY khi nào** | đề nghị **sau 18:15 tối nay** ⇒ 22/08 sạch. Deploy giữa ngày ⇒ **ngày lai** |
| **2** | **`FU-290A`** *(`docs/FU290A_THIET_KE_CAT_MODEL.md`)* | **(a)** không cắt vì độ trễ *(đề xuất)* · **(b)** chốt luật hai cổng để dành · **(c)** vẫn cắt `glm-5.1` theo thước cũ |
| **3** | **`FU-394`** | **(a)** gỡ hẳn nhánh gan — **hành vi không đổi** *(đề xuất)* · **(b)** vá và bật · **(c)** vá và đảo chiều theo P4 |
| **4** | **`FU-416`** | vá một dòng `key=lambda x: (-x[1], x[0])` — `QD-066` gọi đây là loại *«làm dự đoán tốt lên thì xử ngay»* |

### 8 mục gói còn chờ owner

`#1 FU-393` **(ba lối a/b/c — và bản đồ từng mô tả sai làn)** · `#9 FU-299` *(đổi đặc trưng ML,
phải huấn luyện lại)* · `#10 FU-300` · `#5 FU-395` C1/C3/C5/C6 · `#2 D2` *(chờ `FU-397b` có cửa
sổ đo)* · `#3 D3` → `FU-411` · `#13 GĐ2` **ra khỏi gói** · `#8 FU-290A` chờ duyệt.

### Năm mục theo dõi mới

| | |
|---|---|
| `FU-412` | hình phạt `×0,55` **nhạy với điểm gốc tuỳ ý** của thang chấm |
| `FU-413` | hai bản sao roster ngoài phạm vi — nặng nhất là **chú thích tự khai đã sai** |
| `FU-414` | bảng chết **107 ngày** còn **2 điểm đọc sống** trong `main.py` |
| `FU-415` | hook cổng commit dùng **đường dẫn tương đối** |
| `FU-416` | **prompt production không ổn định** |

### Cảnh báo phải nhớ

> **Từ 22/08 `K8` sẽ ĐỎ vì `FU-360` — CỐ Ý, không phải lỗi mới.** Kiểm bằng máy:
> `_v10981_kiem_lich.py --hom-nay 2026-08-22` ⇒ **TRƯỢT**. Đỏ vì vế **«mồ côi ĐẾN HẠN»**
> (hạn 18/08 đã qua), **không** phải vế tổng (**1/2**, còn dưới trần).

> **`QD-015` · `QD-016` · `QD-017` quá hạn 13 ngày, vẫn `ACTIVE`, chưa chạy.** Ba quyết định này
> là **điều kiện** để `FU-360` đóng được — `QD-066` giữ `FU-360` mở chính vì chờ chúng.

**Verdict tách hai dòng:**
- **`CODE_PUSHED`** = `3cea289` · `e3ebc19` · `143a95e` · `b5d9367` · `74f3c37` · `d0b20f6` ·
  `fd19d95` · `709efaf` — **CHƯA `DEPLOYED`**, cố ý
- **`REPORT_PUBLISHED`** = bản này

---

TanPhatAI cần làm: ① ghi **gói 21/08 đã thi hành 4 mục + 1 thiết kế**, **KHÔNG deploy** — mọi mục
ở tầng `CODE_PUSHED`, production **vẫn chạy bản cũ**; ② ghi **`CTX-18.3` → `CTX-18.4`** và lý do
hoãn deploy: **MN đã chốt bundle 05:20** nên deploy giữa ngày tạo **ngày lai**; ③ ghi
**`FU-416` — prompt production KHÔNG ổn định giữa hai lần chạy** (6/6/2 dòng khác; `PYTHONHASHSEED=0`
⇒ 0/0/0), và hệ quả: **mọi phép đo prompt A/B, kể cả `FU-284`, có nhiễu chưa ai trừ ra**; ④ ghi
**13/105 luật dưới nền** trong khi một số đeo nhãn `HR12W 1.0` — nhãn có lúc **nói ngược**;
⑤ ghi **phần GAN của bộ lọc nóng/lạnh CHƯA TỪNG CHẠY** ở hai chỗ, một chỗ làm **cả cơ chế thay số
của `post_filter` chết trên production** trong khi **log vẫn in như đang chạy**; ⑥ ghi
**`FU-290A` thiết kế xong, CHỜ DUYỆT** — biên **220 phút** vs lượt tệ nhất **23,8 phút** ⇒ cắt
model theo độ trễ **không có cơ sở**, và **ML chạm sàn 4 nên không cắt được ML nào**; ⑦ ghi
**từ 22/08 K8 ĐỎ vì `FU-360` — CỐ Ý**, đã kiểm bằng `--hom-nay 2026-08-22`; ⑧ ghi
**`QD-015/016/017` quá hạn 13 ngày, vẫn `ACTIVE`, chưa chạy** — chúng là điều kiện để `FU-360`
đóng được; ⑨ ghi **năm mục mới `FU-412`…`FU-416`**; ⑩ ghi **bốn việc owner cần quyết** ở mục 9.
