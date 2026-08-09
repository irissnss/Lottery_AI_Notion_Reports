# REPORT V11050 — GĐ-B (soi xét) · GĐ-C (nghiệm thu tối) · GĐ-D (lộ trình tới 20/08)

**Ngày:** 2026-08-09, từ 12:30 giờ VN · **Tầng verdict:** `RUNTIME_PROVEN` cho B1 ·
`REPORT_PROVEN` cho B4/B5/B6 · `PLAN_ONLY` cho B7 · GĐ-C **chưa tới giờ** (viết sau 18:05/19:35)

> **Tệp này còn được ghi tiếp trong ngày.** Owner cho tối đa **2 thư mục báo cáo** toàn phiên
> (GĐ-A một, GĐ-B/C/D một), nên GĐ-C và GĐ-D sẽ **nối vào chính tệp này**, không mở thư mục mới.

## 1. Tóm tắt

| việc | kết cục |
|---|---|
| **B1** vá biên `anchor_date` | ✅ vá **2 chỗ** + cổng thử thật + deploy · bẫy **đã nổ thật 05/05**, phạm vi **chỉ lane TEST** |
| **B4** đo lại FU-160/162/164 | ⚠ **cả 6 bảng ĐANG SỐNG**, ghi đều 122 ngày — và **chứa đề xuất chưa ai đọc** |
| **B5** drift K3 | ⚠ **30 tệp lệch** (không phải 465 — số đầu sai vì băm thô trên kho CRLF) · **0 tệp bị sửa thẳng trên VPS** · **28 tệp đã commit mà VPS chưa nhận** |
| **B6** `kiem_code` cho QD-047 | ✅ K3 **có phép máy thật**; K1 **một nửa**; K2 **để rỗng có lý do** (RM-14) |
| **B7** thiết kế lại FU-360 | ✅ **CHỈ KẾ HOẠCH** — gốc bệnh nằm ở **khoá duy nhất**, không phải ở `verify_prediction` |
| **B2** `loz_stage_trace` 96 ngày | ⛔ **KHÔNG chạy** — nguồn chưa hợp lệ, xem §7 |
| **B3** soi `_v10705` | ⏸ chờ owner ký `FU-388` |

## 2. Owner yêu cầu gì (nguyên văn)

> **GĐ-B (chỉ đọc, sau block).** B1 vá `anchor_date <= date(?,'-1 day')` + unit test ·
> B2 chạy lại `loz_stage_trace` trên 96 ngày mới · B3 soi khô `_v10705` (chỉ 3 câu hỏi, **không
> dùng backtest làm căn cứ**) · B4 đo lại FU-160/162/164 (bảng GIỮ/GỘP/GỠ) · B5 danh sách drift
> K3 · B6 thêm `kiem_code` cho QD-047 · B7 thiết kế lại FU-360 ở tầng `INSERT OR REPLACE`
> (**CHỈ KẾ HOẠCH**).

> **QD-041: CẤM đụng prompt/đường chọn số/roster/quyết định gửi LLM tới 21/08.**
> **TRẦN SINH MÃ: tối đa 5 mã FU mới toàn phiên.**

## 3. Đào bới / phát hiện

### B1 — BẪY NHÌN TRƯỚC: **đã nổ thật**, nhưng **chỉ lane TEST**

Tensor `model_strength_by_region_weekday_station_daily` với `anchor_date = D` được dựng bởi
`_compute_model_strength_tensor._date_iter(D, w)` = `[D-(w-1) … D]` — **gồm CHÍNH ngày D**, tức nó
đã đọc `lottery_results` của D. Vậy `WHERE anchor_date <= <ngày đang chấm>` cho phép lấy đúng
tensor của ngày đó ⇒ **chấm model bằng kết quả của chính ngày đó**.

**Không phải giả thuyết.** Đo trên DB production:

| | |
|---|---|
| ngày anchor trùng ngày chạy | **2026-05-05** |
| dòng voter dính | **87** (MB 29 · MN 29 · MT 29) |
| trong đó thành SELECTED/CONTROL | **26** |

**Phạm vi — ghi đúng tầng (RM-12), không thổi lên:** bảng ghi cờ `official_output=false` ·
`output_impact=false` · `test_only=1` · `output_eligible=0` · `diagnostic_only=1`, và
`predictions` có `run_source LIKE '%du_doan_test%'` = **0 dòng**.
⇒ **Output chính thức chưa bao giờ dính.**

**Vì sao vẫn phải vá dù nó đang không với tới:** `MAX(anchor_date)` = **2026-05-05**, cũ **96
ngày**, nên `<= hôm nay` không thể bằng hôm nay. Bẫy **ngủ vì dữ liệu chết, không phải vì code
đúng** — writer tensor chạy lại là nó tỉnh ngay.

**Lối viết đúng vốn ĐÃ CÓ trong kho:** `_materialize_experimental_preview_shadow.py:278` ghi thẳng
*"anchor strictly < date"*. Hai chỗ kia **không theo quy ước của chính kho** — đây là chỗ lệch
chuẩn, không phải chuẩn mới.

| chỗ | TRƯỚC | SAU |
|---|---|---|
| `_materialize_du_doan_test_model_budget.py:_latest_anchor` | `WHERE anchor_date <= ?` | `WHERE anchor_date <= date(?, '-1 day')` |
| `scheduler.py:6838` *(nhánh dự phòng xếp thứ tự shadow)* | `WHERE anchor_date <= ?` | `... <= date(?, '-1 day')` |

**Quét ngược §60.3 — PHÂN LOẠI, không đếm thô** (`_v11050_kiem_bien_anchor.py` phép 3):

| loại | số | chỗ |
|---|---|---|
| ĐẠT (có chặn biên) | **3** | `_materialize_du_doan_test_model_budget` · `_materialize_experimental_preview_shadow` · `scheduler` |
| VI PHẠM | **0** | — |
| CHÚ THÍCH (mô tả lối sai, **không phải** lối sai) | **2** | docstring — nhận ra bằng `ast`, không bằng đếm nháy |
| **NGOÀI PHẠM VI** (cùng mẫu, **bảng khác**) | **2** | `_materialize_adaptive_exploit_v1:236` (bảng `lag1_adaptive_exploit_signal_shadow`, **CÓ** chặn biên) · **`_v104_shadow_prompt_injection:297`** (bảng `gan_signal_shadow_v100`, **KHÔNG** chặn biên) |

⚠ Chỗ cuối **KHÔNG ĐỤNG**: nó nằm trong đường bơm prompt (`scheduler.py:8871`) ⇒ **vùng đóng băng
QD-041 tới 21/08**. Ghi vào `FU-392` để owner quyết sau 21/08. Và phải nói rõ: bảng đó **khác**,
nên chưa được suy ra là cũng sai — cần **phép kiểm nhân quả riêng cho bảng đó**.

### B4 — SÁU BẢNG ĐỀU SỐNG. Và một trong số đó **chứa đề xuất chưa ai đọc suốt 122 ngày**

V11046 đóng FU-160/162/164 với lý do *«KHÔNG CÓ BẢNG»*. Đo lại trên production:

| mã | bảng | dòng | khoảng | số ngày | ghi 08/08? |
|---|---|---|---|---|---|
| FU-160/162 | `v93_wr_gate_filter_audit_shadow` | 9.414 | 09/04 → 08/08 | **122** | ✅ 79 |
| FU-160/162 | `v93_verdict_weight_recalibration_shadow` | 3.775 | 09/04 → 08/08 | **122** | ✅ 44 |
| FU-160/162 | `v93_mn_save_signal_per_method_shadow` | 2.475 | 09/04 → 08/08 | **122** | ✅ 24 |
| FU-164 | `v94_cross_region_spillover_aware_shadow` | 13.278 | 09/04 → 08/08 | **122** | ✅ 127 |
| FU-164 | `v94_cross_region_leakage_continuous_monitor` | 2.196 | 09/04 → 08/08 | **122** | ✅ 18 |
| FU-164 | `v94_no_token_first_simulation_shadow` | 97 | 04/05 → 08/08 | 97 | ✅ 1 |

Ba endpoint **đang phục vụ** đọc chúng: `/api/admin/v95-dashboard` · `/api/admin/v96-master-tracker`
· `/api/admin/v98-command-center`.

**Nhưng «sống» chưa phải «có ích».** Đo nội dung `v93_verdict_weight_recalibration_shadow`, 30 ngày:

| | |
|---|---|
| dòng có đủ hai vế để so | **957** |
| đề xuất lệch **≥ 0,05** so trọng số đang dùng | **628** = **65,6%** |
| đề xuất lệch **≥ 0,15** | **561** = **58,6%** |

Sáu chỗ lệch nhất (n = mẫu 30 ngày):

| miền | verdict | họ | đang dùng | đề xuất | chênh | mẫu |
|---|---|---|---|---|---|---|
| MN | `SKIP` | AI | 0,40 | **1,189** | **+0,789** | 1.213 |
| MN | `SKIP` | NO_TOKEN | 0,40 | **1,185** | **+0,785** | 1.511 |
| MB | `CHOT_HA` | NO_TOKEN | 1,50 | **0,804** | **−0,696** | 4.082 |
| MT | `SKIP` | NO_TOKEN | 0,40 | **1,093** | **+0,693** | 1.486 |
| MT | `SKIP` | AI | 0,40 | **1,070** | **+0,670** | 2.475 |
| MB | `CHOT` | NO_TOKEN | 1,50 | **0,849** | **−0,651** | 525 |

Đọc thẳng: hệ **đang hạ giá verdict `SKIP` xuống 0,40** trong khi dữ liệu 30 ngày nói nó đáng
**~1,1**; và **đang tin `CHOT`/`CHOT_HA` họ NO_TOKEN ở mức 1,50** trong khi dữ liệu nói **~0,82**.
Đây là bảng đã ghi **122 ngày liên tục** và **suýt bị agent xoá ngày 08/08 vì tiền đề sai**.

**Ba điều PHẢI nói kèm, nếu không là RM-03/RM-17:**
1. `proposed_weight_30d` do chính materializer tính (`v93_..._v1`) — agent **chưa** kiểm dẫn xuất
   của nó (có trừ cụm ngày/VIF không? nền có đúng không?). **Chưa được dùng làm căn cứ đổi số.**
2. Đổi trọng số verdict **chính là** đường chọn số ⇒ **QD-041 khoá tới 21/08**.
3. **Chưa có ngưỡng hành động đăng ký trước.** Không có ngưỡng thì dù số đẹp cũng không được
   phép kết luận.

**Bảng GIỮ / GỘP / GỠ (đề xuất, owner quyết — RM-06 nên agent KHÔNG đặt hạn):**

| bảng | đề xuất | vì sao |
|---|---|---|
| cả **6** | **GIỮ** | đang ghi, đang được 3 endpoint đọc — không có cơ sở gỡ |
| `v93_verdict_weight_recalibration_shadow` | **GIỮ + đưa vào danh sách mở khoá 21/08** | là bảng duy nhất trong 6 cái mang **đề xuất định lượng** cho đường chọn số |
| 3 cron **19:16 / 19:18 / 19:20** | **GỘP — đề xuất, chưa làm** | ba job riêng, 8 bảng, panel đọc chồng nhau ⇒ ứng viên D4 |
| **GỠ** | **không mục nào** | không bảng nào chết |

### B5 — DRIFT K3: con số thật là **30**, không phải 465

Lần đo đầu ra **465/467 tệp «khác nhau»**. Sai. Kho này là **CRLF**, blob git là **LF** ⇒ băm thô
thì **mọi tệp đều khác**. Đúng dạng **RM-09**. Chuẩn hoá xuống dòng rồi đo lại:

| nhóm | nghĩa | số | mức lo |
|---|---|---|---|
| **(a)** VPS = bản làm việc ≠ git | vừa deploy phiên này, chưa commit | **2** | thấp |
| **(b)** ba bản ba đường | có người sửa thẳng trên VPS | **0** | — **điểm này TỐT** |
| **(c)** git = bản làm việc ≠ VPS | **đã commit mà VPS chưa nhận** | **28** | **cao** |
| **(d)** chỉ có trên VPS | không nằm trong git | **2** (`_v105_18_vps_smoke.py` · `_v11050_kiem_bien_anchor.py` — cái sau commit trong chính phiên này) | vừa |

**Không tệp nào bị sửa thẳng trên VPS** — đó là kết quả tốt và phải nói ra, vì nó bác một nghi
ngờ hợp lý. Vấn đề thật là chiều ngược: **28 tệp nằm trong git mà máy chủ chạy bản cũ** — đúng
căn bệnh `FU-387` vừa vá ở GĐ-A, chỉ khác là ở quy mô.

Trong 28 tệp, **6 tệp được `scheduler.py` đang chạy gọi tới** (ưu tiên xử):
`_du_doan_test_engine` · `_materialize_ai_no_token_cross_verification_shadow` ·
`_materialize_convergence_cluster` · `_materialize_experimental_preview_shadow` ·
`_v104_phase_b_runner` · `strength_calibrator`.

*Giới hạn agent tự khai:* phép đối chiếu này **chỉ phủ `web/backend/*.py` ở một tầng** — chưa phủ
`.html`/`.js`, chưa phủ thư mục con. Và «6 tệp» đo bằng cách dò tên trong `scheduler.py`; tệp
được gọi **gián tiếp** qua module khác thì phép này **không thấy**.

### B6 — `kiem_code` cho QD-047: ghi đúng cái đo được, để rỗng cái không đo được

QD-047 đặt **K1–K4** làm bốn chỉ số cứu cánh nhưng ô `kiem_code` chỉ có phép cho **K4** và cửa sổ
đóng băng. Nay thêm ba mục:

| chỉ số | phép máy | trung thực |
|---|---|---|
| **K3** drift | `_v11050_kiem_drift.py` ⇒ `DRIFT_K3_V11050=DAT` | **thật**. Nhưng K3 đòi «drift = 0» mà số hiện tại là **30** ⇒ **K3 CHƯA ĐẠT**; cổng chỉ chặn nó **xấu đi**, không tuyên bố nó tốt |
| **K1** cổng | chạy 8 cổng, đòi cả 8 thoát 0 | **một nửa**. Nó chứng minh cổng **CHẠY ĐƯỢC**, không chứng minh cổng **CHẶN ĐƯỢC** (RM-15). Muốn đủ phải có sổ đăng ký bằng chứng RM-15 cho từng cổng — **sổ đó chưa tồn tại** |
| **K2** prompt sạch | **để rỗng** | RM-14 buộc đo trên **dump production**. Chưa có script làm đúng việc đó, và dựng nó bây giờ là chạm **QD-041**. Mở lại sau 21/08 |

Ghi rỗng kèm lý do là **đúng hợp đồng** (`CLAUDE.md`: *"không kiểm được thì để rỗng + nêu lý do"*).
Bịa một phép giả vờ đo còn tệ hơn để trống.

### B7 — FU-360: gốc bệnh **KHÔNG** nằm ở `verify_prediction` (CHỈ KẾ HOẠCH)

Đọc mã thật:

```
predictions:  UNIQUE(date, target_region, ai_model)      ← KHÔNG có run_source
database.py:2635   INSERT OR REPLACE INTO predictions ...
database.py:2794   def verify_prediction(...)  →  SELECT * FROM predictions
                                                  WHERE date = ? AND target_region = ?
```

`verify_prediction` không lọc `run_source` **là hệ quả, không phải nguyên nhân**: khoá duy nhất
đảm bảo mỗi `(ngày, miền, model)` chỉ có **một** dòng, nên chẳng có gì để lọc. Nguyên nhân là
**`INSERT OR REPLACE` + khoá thiếu `run_source`**: hai lane ghi cùng bảng thì lane sau **ghi đè
lane trước, không để lại dấu vết**.

Đo trên production: `run_source` có **9 giá trị**, trong đó **`shadow_auto_eval` = 4.035 dòng
(≈33% bảng)** nằm chung bảng với `auto_daily` = 4.271. Bảy ngày gần nhất: **527 cặp / 527 dòng** —
đúng một dòng mỗi cặp, **theo cấu tạo**, nên va chạm nếu có thì **không thể phát hiện sau sự việc**.

Khối `FU-360` đã ghi sẵn ngày nổ: *«đúng lúc QD-015/016/017 chạy **21/08** — vì đó là lúc một
model chạy **cả hai đường**»*. Đo trên vẫn khớp.

**Ba phương án, cân theo rủi ro — owner chọn, agent KHÔNG tự làm:**

| | phương án | được | mất |
|---|---|---|---|
| **1** | chỉ lọc `run_source` trong `verify_prediction` | 1 dòng sửa | **vô ích** — dòng đã bị ghi đè mất rồi. **Loại** |
| **2** | mở khoá duy nhất thành `(date, region, ai_model, run_source)` | đúng gốc, hai lane cùng sống | đụng **bảng khoá** `predictions` (12.078 dòng): phải migrate + **§60.2 rà MỌI chỗ đọc** đang ngầm giả định «một dòng mỗi cặp». Việc lớn, phải owner ký |
| **3** ⭐ | **giữ khoá, chặn ở tầng ghi**: nếu dòng cũ có `run_source` KHÁC ⇒ **không ghi đè** — ghi log + bỏ qua (hoặc đẩy sang bảng phụ) | nhỏ, có đường lui, **không đổi schema**, **không chỗ đọc nào phải sửa** | không lưu được cả hai lane; chỉ **bảo vệ** dòng chính thức |

**Đề xuất: làm 3 trước 21/08 (rào chắn), cân 2 sau — và chỉ khi đo được va chạm thật.**
`FU-360` mang hạn **14/08** do owner ký; agent **không đổi hạn** (RM-06).

## 4. Hướng xử lý và vì sao chọn

**B1 vá dù bẫy đang ngủ** — vì nó ngủ do *dữ liệu chết*, không do code đúng. Loại bẫy này thức
dậy im lặng.

**B4 không gỡ gì cả** — sáu bảng đều sống. Việc đáng làm ngược lại: **đọc thứ đã nằm đó 122 ngày**.

**B5 công bố số 30 kèm số sai 465** — vì nếu chỉ đưa số đúng thì lần sau người khác lại đo bằng
băm thô và lại ra 465.

**B7 chỉ kế hoạch** — owner ghi rõ `PLAN-ONLY`, và đây là **bảng khoá**.

## 5. Đã làm gì — thay đổi production

| # | thay đổi | PID | nghiệm thu |
|---|---|---|---|
| B1 | `_materialize_du_doan_test_model_budget.py` + `scheduler.py` chặn biên anchor | 1171150 → **1172701** | health **200** · `/du-doan` **200** · `/monitoring` **401** · **0 dòng lỗi** · cổng chạy trên VPS **thoát 0** |

**4 bảng khoá:** không chạm ngoài SELECT. **QD-041 còn nguyên.**

## 6. Cổng kiểm

**Cổng cấp số hiệu FU-369 — chạy TRƯỚC khi cấp mã (bằng chứng quét):**

```
V  : 396 số · cao nhất V11049 · trống tiếp: V11050   ✓ dùng V11050
FU : 260 số · cao nhất FU-391 · trống tiếp: FU-392   ✓ dùng FU-392
QD : 42 số  · cao nhất QD-054 · trống tiếp: QD-055   (không dùng)
```

**Trần sinh mã toàn phiên: 2/5** — `FU-391` (GĐ-A) · `FU-392` (GĐ-B). Còn 3 suất.

**Hai cổng mới, cả hai đều có THỬ CHẶN THẬT (RM-15):**

| cổng | thử vi phạm | thử sạch |
|---|---|---|
| `_v11050_kiem_bien_anchor.py` | trả `<= ?` về ⇒ **thoát 1**, cả ba phép cùng đỏ | khôi phục ⇒ **thoát 0** |
| `_v11050_kiem_drift.py` | `--tran 5` (giả lập drift phình) ⇒ **thoát 1** | `--tran 30` ⇒ **thoát 0** |

Trạng thái đã **khôi phục nguyên vẹn** sau thử (`git diff` chỉ còn đúng bản vá chủ ý).

`_v11050_kiem_bien_anchor.py` **đã nối vào hook `git commit`** (cổng thứ **8**).
`_v11050_kiem_drift.py` **CỐ Ý KHÔNG nối** — nó cần SSH tới VPS mỗi lần commit; một cổng làm
commit phụ thuộc mạng là cổng sẽ bị vô hiệu hoá bằng `--no-verify`. Chạy tay hoặc theo lịch.

## 7. Vướng vấp

**7.1 — B2 KHÔNG CHẠY, và lý do là một phát hiện chứ không phải cái cớ.**
B2 đòi chạy lại `loz_stage_trace` trên 96 ngày mới. Nhưng `_materialize_loz_stage_trace_shadow.py`
**nằm trong danh sách 28 tệp mà VPS chưa nhận** (§B5). Chạy trên VPS là chạy **mã cũ**; chạy ở
local là đọc **DB không phải production**. Cả hai đều vi phạm **RM-13** — và ngày 07/08 đã đo bằng
nguồn sai **ba lần trong một ngày**. Nên: **giải quyết drift trước, đo sau.** Không đo bừa để có
số đẹp.

**7.2 — Đo drift lần đầu ra 465, sai gấp 15 lần.** Xem §B5. Nguyên nhân CRLF, đúng **RM-09**.
Đã đưa việc **chuẩn hoá xuống dòng** vào thẳng cổng để lỗi này không lặp bằng tay nữa.

**7.3 — Cổng B1 lần đầu tự báo động giả trên chính docstring của nó.** Docstring **trích lại lối
sai** để giải thích, và bộ dò chuỗi tính đó là vi phạm. Đúng bảng phân loại của **§60.3**
(`CHU_THICH` phải giữ). Sửa bằng `ast` để nhận docstring, **không** bằng đếm dấu nháy.

**7.4 — Phân loại drift lần đầu viết sai thứ tự nhánh** nên 28 tệp «git đi trước» bị dồn nhầm vào
ô «ba bản ba đường» — tức báo nhầm thành *«có người sửa thẳng trên VPS»*, một cáo buộc nặng.
Bắt được vì con số **28** vô lý so với ngữ cảnh. Ghi lại vì đây là kiểu lỗi **làm hỏng kết luận
mà không làm hỏng chương trình**.

## 8. Gỡ về

```bash
ssh root@14.225.224.89 'cd /root/Lottery_AI_Test && \
  cp backups/scheduler.py.pre_v11050 web/backend/scheduler.py && \
  cp backups/budget.py.pre_v11050 web/backend/_materialize_du_doan_test_model_budget.py && \
  systemctl restart lottery'
git revert <commit V11050>
```

B4/B5/B6/B7 **không đụng runtime** — không có gì để gỡ. Mục `kiem_code` thêm vào QD-047 gỡ bằng
`git revert` cùng commit.

## 9. Theo dõi tiếp

| mã | việc | chờ ai |
|---|---|---|
| `FU-392` | ① biên `anchor_date` — **xong** · ② `gan_signal_shadow_v100` cùng mẫu, **trong vùng đóng băng**, xét sau 21/08 | **owner, sau 21/08** |
| `FU-160/162/164` | **MỞ LẠI** — 6 bảng sống. Đề xuất trọng số verdict lệch tới **0,79** chưa ai đọc 122 ngày ⇒ đưa vào danh sách mở khoá 21/08 | **owner** |
| K3 / drift | **28 tệp** đã commit mà VPS chưa nhận, **6** trong đó `scheduler.py` đang gọi ⇒ cần một lượt deploy có ký, có backup, có so PID | **owner** |
| `FU-360` | ba phương án ở §B7, đề xuất **phương án 3** trước 21/08 | **owner** |
| `FU-388` | soi khô `_v10705` (chiều ĐÀI) — **B3 chưa chạy vì chờ ký** | **owner** |
| B2 | chạy lại `loz_stage_trace` **sau khi** hết drift | sau K3 |
| GĐ-C | **18:05** bộ 25 phép (C23/C24/**C25** lần đầu hợp lệ) · **19:35** lane · bầy đàn · trace | **tối nay** |

### B6 (tiếp) — BA LỖI LỘ RA NGAY KHI ĐEM `kiem_code` MỚI ĐI CHẠY THẬT

Viết `kiem_code` xong mà không chạy sổ quyết định thì coi như chưa viết. Chạy `_v10920` thì cả ba
lỗi dưới đây lộ trong một lượt — và **lỗi đầu tiên nguy hơn hai lỗi kia cộng lại**.

**① Một ô `kiem_code` RỖNG làm SẬP CẢ BỘ KIỂM — và sập trong im lặng.**
`CLAUDE.md` cho phép *"không kiểm được thì để rỗng + nêu lý do"*, và K2 dùng đúng quyền đó. Nhưng
`_v10920_decision_ledger.chay_bo_kiem` đọc thẳng `k['chay_lenh'][0]` ở dòng cuối hàm ⇒ **`IndexError`**
⇒ **bộ kiểm dừng giữa chừng**, phần còn lại của sổ **không được đọc mà không ai biết**. Trước khi
vá, nó in *«3 PHÉP TRÔI»* rồi chết; sau khi vá, số thật là **2**. Tức con số «3» kia cũng không đáng
tin — nó là con số của một lượt chạy **chưa hết sổ**.
Vá: `chay_lenh` rỗng ⇒ trả `None` = *«chưa có phép máy»* kèm lý do — khác hẳn `TRÔI` (đã kiểm và
lệch). Rỗng mà **không nêu lý do** thì in thẳng `KHÔNG NÊU LÝ DO (phải nêu)`.

**② Cổng `THI_HANH_57` đòi đóng đúng ba mã vừa được chứng minh là còn sống.**
QD-054 ký **một bảng 57 mục cụ thể**, nhưng cổng gọi `phan_loai()` **tính lại từ đầu mỗi lần chạy**
⇒ mọi mã mới hợp mẫu đều bị hút vào nhóm A. Ngày 09/08 nó đòi đóng **`FU-392`** (sinh cùng ngày),
**`FU-387`/`FU-388`** (sinh ở GĐ-A) và **`FU-160/162/164`** — tức **đóng lại chính ba mã mà GĐ-B
vừa chứng minh có 6 bảng sống 122 ngày**. Nghe theo là **đóng hàng loạt mù**, đúng thứ owner cấm.
Cùng họ với cổng đóng băng QD-041 từng **luôn báo xanh** (RM-15): **cổng đo một tập trôi theo thời
gian thì không còn đo cái nó được ký để đo**. Vá: ghim `NGOAI_PHAM_VI_KY_0033` **có nêu lý do từng
mã**, và cổng **bêu tên** những mã bị bỏ ra — cắt phạm vi trong im lặng đọc y như «đã phủ hết».

**③ `chay_lenh` của K1 viết sai lược đồ, và cách sửa hiển nhiên thì treo 300 giây.**
Bản đầu nhét **8 đường dẫn** vào `chay_lenh`, nhưng trường đó là **MỘT lệnh + tham số** ⇒ nó chạy
script đầu với 7 script kia làm `argv`. Sửa hiển nhiên là gọi thẳng hook `code_quality_guard.py`
(hook vốn gọi đủ 8) — thử thật thì **treo tới hết giờ**: hook đọc `sys.stdin.read()`, mà
`subprocess.run(capture_output=True)` **không đóng stdin**. Vá: `_v11050_kiem_cong.py` **đọc danh
sách `SOI` từ chính hook** (không chép tay — RM-10) rồi chạy từng cổng với `stdin=DEVNULL`.
Kết quả: **8/8 cổng thoát 0** ⇒ `CONG_K1_V11050=DAT`.

**Sổ quyết định sau ba vá: `KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI`** (từ «3», mà «3» còn là số của lượt
chạy chưa hết sổ).

**Nói thẳng về K1:** dấu ✓ đó là **nửa K1**. Nó chứng minh cổng **chạy được**, không chứng minh cổng
**chặn được**. Nửa còn lại đòi mỗi cổng có bằng chứng RM-15 được **ghi lại**, và sổ đăng ký đó
**chưa tồn tại** ⇒ **K1 chưa đạt đủ**. Câu này in thẳng trong output của cổng để không ai đọc dấu ✓
thành «K1 xong».

**Phụ chú định dạng:** commit V11050 ghi `OWNER_DECISION_LEDGER.json` bằng `indent=2` làm diff phình
lên **5.813 dòng** trong khi nội dung chỉ đổi **29 dòng**. Đã trả về `indent=1` như gốc (V11050b).
Đối chiếu ở mức JSON: **56 mục trước, 56 mục sau, 0 mục mất, chỉ QD-047 đổi nội dung**.

---

## LOCK-IN / OPEN / NEXT ACTION

**LOCK-IN:** sổ quyết định **0 phép trôi** (từ «3», và «3» là số của lượt chạy chưa hết sổ) · biên `anchor_date` đã chặn ở **cả 2 chỗ** thuộc tensor + cổng thử chặn thật, deploy
PID 1172701 · drift K3 có **phép máy đầu tiên** và con số thật là **30**, **0 tệp bị sửa thẳng trên
VPS** · QD-047 có `kiem_code` cho K3 (thật), K1 (một nửa, khai rõ), K2 (rỗng, có lý do) · 6 bảng
FU-160/162/164 **đều sống**, không gỡ gì · FU-360 có ba phương án dựa trên mã thật.

**OPEN:** 28 tệp VPS chưa nhận · `gan_signal_shadow_v100` chưa xét (đóng băng) · đề xuất trọng số
verdict chưa ai thẩm định dẫn xuất · B2 · B3 · FU-360 chọn phương án.

**NEXT ACTION:** **18:05** đọc bộ 25 phép · **19:35** đọc lane · nối GĐ-C và GĐ-D vào **chính tệp
này**.

*Đẩy cùng commit (A55 · §57.2).*
