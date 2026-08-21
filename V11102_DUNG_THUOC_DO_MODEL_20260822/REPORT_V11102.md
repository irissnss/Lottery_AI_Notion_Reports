# REPORT V11102 — DỰNG THƯỚC ĐO SỨC MẠNH MODEL · BỘ CHẤM T-B LÊN VPS · ĐÓNG FU-420

**Ngày:** 2026-08-22 (00:00 → sáng sớm) · **Mã đọc:** `DO2208` · **Quyết định:** `QD-071`
**Chạm production:** deploy 2 tệp · restart `lottery` (PID `2110106 → 2128063`) · 1 dòng cron mới
**Verdict:** `CODE_PUSHED` + `DEPLOYED` + `REPORT_PUBLISHED`
**KHÔNG** phải `RUNTIME_PROVEN` — lý do ghi rõ ở §6

---

## 1. Tóm tắt

Tối qua owner ký hai quyết định lúc 23:35. Phiên này thi hành cả hai.

**Điều quan trọng nhất làm được đêm nay, nói bằng một câu:**

> **Từ hôm nay dự án ĐO ĐƯỢC từng model — kể cả model đang góp số công bố. Trước đêm nay thì
> không.**

Con số của chỗ thủng, đếm lại từng mã:

| | |
|---|---|
| model đang góp số công bố mà có **0 dòng chấm** | **12 / 15** |
| `claude-sonnet-4-6` — model **đương nhiệm** | **0 dòng** |
| 3 model có dòng (`glm-5.1` · `gpt-oss-120b` · `gpt-5.4`) | **ngừng được chấm từ 01/08**, đúng lúc rời danh sách shadow |

Sau khi vá: **15/15 model output có dòng chấm.**

Và một chỗ thủng thứ hai, cùng loại: **bộ chấm lane T-B chưa bao giờ lên VPS**. Lane **thu đủ mỗi
ngày** bằng 3 cron suốt nhiều tuần, nhưng **không ai chấm** — hệ thống biết A và B **có khác nhau
không**, nhưng **không biết bên nào thắng**. Nay đã chấm: **155/155 dòng, 0 từ chối, 111 cặp bất
đồng.**

**Hai con số em phải rút lại trong bản này** — cả hai là của chính em, công bố hôm qua: **§3.5.**

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«① `FU-420`: `QD-066` THAY `QD-021/027/065` ⇒ 102 mục quá hạn là HỢP LỆ (giữ có chủ đích, không
> phải trễ). KÈM ĐIỀU KIỆN: toàn bộ 102 mục được rà lại MỘT LƯỢT, trình owner MỘT bảng lời thường
> kèm hạn mới từng mục — **hợp lệ không có nghĩa là quên**. ② Ba sửa chữa thước ĐÃ KÝ + bộ chấm
> T-B lên VPS cùng đợt — triển khai sáng sớm 22/08.»*

Và khoá cách làm:

> *«Mỗi sửa chữa một commit riêng · thử chặn hai chiều · chứng minh bằng ĐO: chạy lại scorer trên
> dữ liệu cũ ⇒ 15 model output phải CÓ dòng chấm (trước: 0) · lượt trễ bị loại đúng · bảng cộng
> dồn khớp quét thô.»*

> *«Ghi rõ ngày bắt đầu thu: 22/08 — đếm từ 0 cho mọi quyết THĂNG (bảng 90 ngày đã bị nhìn thấy,
> chỉ dùng cho quyết DỪNG).»*

> *«CHỈ rà và trình — CẤM đóng hàng loạt mù.»*

---

## 3. Đào bới / phát hiện

### 3.1 · Vì sao writer bị đóng — và nó đóng bằng đúng hai dòng

```python
WHERE date=? AND target_region=? AND run_source='shadow_auto_eval'   # ← dòng thứ nhất
...
if model not in shadow_models:                                        # ← dòng thứ hai
    continue
```

Hai dòng đó không sai khi viết — bảng sinh ra để chấm **ứng viên shadow**. Cái sai là **không ai
quay lại hỏi**: *«nếu muốn so ứng viên với người đương nhiệm thì lấy số của người đương nhiệm ở
đâu?»* Suốt **4 tháng** không ai hỏi câu đó.

### 3.2 · Hai danh sách RỜI NHAU — và điều đó quyết định cách vá

Kiểm bằng máy trước khi động vào lược đồ:

```
shadow: 11 model · output: 15 model · GIAO NHAU: KHÔNG CÓ
```

Vì rời nhau nên khoá `UNIQUE(date, region, ai_model)` **không cần đổi** — không phải dựng lại bảng
4.167 dòng, **rủi ro bằng 0**. Nếu hai danh sách có giao nhau thì hai họ sẽ **đè lên nhau** và một
họ **biến mất im lặng**; nên phép kiểm K1 của cổng mới canh đúng điều này, mãi mãi.

### 3.3 · Lượt trễ — đo được 3,4%, không phải «1–12%»

`PRJ-SELECTION-WINDOW-001` mục 1: bản ghi tạo **sau mốc chốt** thì lúc model chọn nó **không tồn
tại**. Đo 45 ngày trên `predictions`:

```
3.669 lượt · TRỄ 125 = 3,4%
   MT  shadow_auto_eval  112
   MB  shadow_auto_eval   13
   → KHÔNG lượt OUTPUT nào trễ
```

### 3.4 · Chặn thôi KHÔNG đủ — và đây là chỗ dễ bỏ sót nhất

Vá xong `GĐ-1.2`, dễ tưởng là xong. **Không.** Dòng rò cũ **không tự biến mất** khi chạy lại:

- khoá bảng là `(ngày, miền, model)` ⇒ chạy lại chỉ **đè** lên model **còn nằm trong danh bạ**;
- model đã **rời cả hai danh sách** — `gemma-4-31b` (29 dòng), `kimi-k2.5` (22), `deepseek-v4-pro`
  (22) — thì **không lượt ghi nào chạm tới nữa** ⇒ dòng rò của chúng **sống mãi**.

Tìm thấy **334 dòng rò**, trễ nhất **387 phút** sau mốc chốt. Để nguyên thì mọi truy vấn về sau
phải **nhớ mà lọc** — mà cái gì phải nhớ thì sẽ có ngày quên.

### 3.5 · RÚT LẠI (theo `PRJ-RETRACTION-001` — đủ bốn phần)

**Rút lại #1 — «8/15»**

| phần | nội dung |
|---|---|
| **chỗ gốc** | `REPORT_V11101`, §1 bảng tóm tắt và §3.1, công bố đêm 21/08 |
| **nguyên văn câu sai** | *«8 trên 15 model đang góp số công bố có ĐÚNG 0 dòng»* |
| **điều đúng** | **12/15**. Đếm lại từng mã: chỉ `glm-5.1` (286 dòng), `gpt-oss-120b` (286), `gpt-5.4` (2) là có — và **cả ba dừng ở 31/07–01/08**, đúng lúc rời danh sách shadow. Tái lập: duyệt `get_output_eligible_ids()` rồi `SELECT COUNT(*) … WHERE ai_model=?` |
| **đã dựa vào đâu** | Con số này là **phần lõi** của lập luận *«chưa có thước nên chưa cắt được»*. Kết luận **không đổi** — nhưng nó **nặng hơn** báo cáo cũ, và một con số sai theo hướng **làm nhẹ vấn đề** thì vẫn phải rút |

**Rút lại #2 — «1–12% lượt trễ»**

| phần | nội dung |
|---|---|
| **chỗ gốc** | `REPORT_V11101` §4.3, mục 2 của ba sửa chữa |
| **nguyên văn câu sai** | *«1–12% lượt chạy sau mốc chốt vẫn vào sổ»* |
| **điều đúng** | **3,4%** (125/3.669 trong 45 ngày), **toàn bộ** ở `shadow_auto_eval` MT/MB, **không lượt OUTPUT nào**. Tái lập: đối chiếu `predictions.created_at` với `_v10782_freeze.FREEZE_MARKS` |
| **đã dựa vào đâu** | Chưa quyết định nào. Nhưng dải «1–12%» **không tái lập được** — nó là ước lượng chứ không phải phép đo, và `RM-17` cấm dùng loại số đó làm căn cứ |

### 3.6 · Bộ chấm điểm quét lại toàn bộ tệp trace cho TỪNG model

Phát hiện lúc 00:20 khi chạy lại 125 ngày: `_latest_trace_for()` (`:221`) đọc **cả tệp**
`prediction_trace.jsonl` rồi `json.loads` **từng dòng**, và được gọi **một lần cho mỗi model** ⇒
**≈9.750 lần quét cả tệp**, tốc độ ~50 dòng/phút.

**Vì sao đáng ghi:** cả bộ thước vừa dựng có tiền đề *«chạy lại được trên dữ liệu cũ»*. Nếu chạy
lại tốn hơn một giờ thì sẽ **không ai chạy lại**, và bảng sẽ trôi đúng kiểu nó đã trôi 4 tháng.
**Không** ảnh hưởng lượt chạy hằng ngày (1 ngày × 1 miền = 26 lần quét). → **`FU-422`, hạn 29/08.**

**Chưa vá ngay** vì lượt chạy lại **đang chạy dở** lúc phát hiện — vá giữa chừng thì tiến trình
vẫn dùng mã cũ, còn khởi động lại thì mất phần đã làm.

---

## 4. Hướng xử lý và vì sao chọn

### 4.1 · Thước: so từng cặp với chính bộ số đã công bố

```
b = số lần MODEL đúng   khi BỘ SỐ ĐÃ CÔNG BỐ sai
c = số lần MODEL sai    khi BỘ SỐ ĐÃ CÔNG BỐ đúng
điểm = (b − c) / n          z (McNemar) = (b − c) / √(b + c)
```

Nhiễu «hôm nay dễ / mai khó» có mặt ở **cả hai vế** nên bị **khử ngay trong phép trừ** — không cần
hiệu chỉnh gì thêm. Đo được: cần ít mẫu hơn **2,9×** ⇒ **66 ngày** thay vì **218**.

Hai cột `b`/`c` **đã có sẵn** trong bảng từ trước (`would_flip_baseline_to_win` /
`would_flip_baseline_to_lose`) — thứ thiếu chưa bao giờ là công thức, mà là **dữ liệu của người
đương nhiệm**.

### 4.2 · Vì sao `z` khi `b+c=0` phải trả `None`, không phải `0.0`

`0.0` đọc thành **«hoà»**. Sự thật là **«chưa có ngày nào phân biệt được hai bên»** — tức *chưa đo
được gì*. Hai chuyện khác hẳn nhau, và `RM-04` cấm đúng chỗ lẫn lộn này.

### 4.3 · Hai cột mốc, cố ý tách ra

| | dùng dữ liệu nào | vì sao |
|---|---|---|
| **DỪNG** một model | **toàn bộ lịch sử** | hướng thận trọng — cắt nhầm thì cho vào lại, rẻ |
| **THĂNG** một model | **đếm từ 0 kể từ 22/08/2026** | bảng 90 ngày cũ **đã bị nhìn thấy**; lấy nó phong chức là chọn cái cao nhất trong 15 con số nhiễu |

### 4.4 · Vì sao KHÔNG kết luận lane T-B hôm nay

111 cặp bất đồng **đã vượt** ngưỡng đếm `≥96`. Nhưng `QD-059` đăng ký **ngày đọc**, và `QD-017` đủ
14 ngày vào **24/08**. **Đọc sớm là đọc sau khi đã nhìn** — đúng lối đã làm hỏng cả 11 lần khen
model trước đây. Bộ chấm in **đếm và chỉ đếm**: không tỉ lệ, không so sánh, không `z`.

---

## 5. Đã làm gì

| # | việc | bằng chứng |
|---|---|---|
| **GĐ-1.1** | mở writer cho 15 model OUTPUT | chạy lại **377/378** cặp ngày-miền ⇒ **15/15** model output có dòng chấm |
| **GĐ-1.2** | chặn lượt tạo sau mốc chốt | `bo_vi_tre` được **báo ra**, không loại im lặng; 20/08 MT loại 1 dòng, mốc `16:58+07:00` |
| **GĐ-1.2b** | dọn dòng rò cũ | đối chiếu 9.021 dòng → tìm **334** → xoá → **đọc lại còn 0**; dấu vết đầy đủ `artifacts/v11102/dong_ro_da_don.json` |
| **GĐ-1.3** | bảng cộng dồn | `model_paired_scorecard_cumulative` · **108 khoá khớp TỪNG CON SỐ** với quét thô đi đường khác |
| **GĐ-2** | bộ chấm T-B lên VPS | md5 khớp từng byte · thử chặn **6/6 trên VPS** · **155/155 chấm, 0 từ chối, 111 bất đồng** · cron **136 → 137** |
| **GĐ-3** | `QD-071` + rà mục quá hạn | sổ **72 → 73** mục · `thay_boi` **3/3** · `docs/RA_102_MUC_QUA_HAN_20260822.md` |

### 5.0 · Bằng chứng chính owner yêu cầu — «15 model output phải CÓ dòng chấm (trước: 0)»

| model OUTPUT | dòng chấm | từ ngày → đến ngày |
|---|---:|---|
| `claude-sonnet-4-6` **(đương nhiệm)** | **376** | 18/04 → 21/08 · **trước bản vá: 0** |
| `lstm` · `meta-learning` · `random-forest` · `smart-ensemble` · `smart-ml` · `xgboost` | **378** mỗi cái | 18/04 → 21/08 · **trước: 0** |
| `gemini-2.5-flash` | 377 | 18/04 → 21/08 · **trước: 0** |
| `combo-super` · `gemini-2.5-pro` | 376 | 18/04 → 21/08 · **trước: 0** |
| `deepseek-reasoner` | 375 | 18/04 → 21/08 · **trước: 0** |
| `gpt-5.4` | 374 | 18/04 → 21/08 · trước: **2** |
| `claude-opus-4-6` | 198 | 17/06 → 21/08 (vào pool 17/06) · **trước: 0** |
| `gpt-oss-120b` | 63 | 19/04 → 21/08 · trước: 286 nhưng **dừng ở 31/07** |
| `glm-5.1` | 61 | 01/08 → 21/08 · trước: 286 nhưng **dừng ở 31/07** |

**⇒ 15/15 có dòng chấm. Trước bản vá: 3/15, và cả ba đã dừng từ 31/07–01/08.**

### 5.0b · Kết quả sơ bộ — và vì sao CẤM đọc thành kết luận

Họ `OUTPUT`, **45 khoá** (model × miền). Cao nhất:

| model | miền | n | b | c | điểm | z |
|---|---|---:|---:|---:|---:|---:|
| `glm-5.1` | MB | 21 | 5 | 1 | **+0,1905** | +1,63 |
| `claude-opus-4-6` | MN | 66 | 15 | 8 | +0,1061 | +1,46 |
| `deepseek-reasoner` | MB | 124 | 21 | 10 | +0,0887 | **+1,98** |
| `combo-super` | MT | 126 | 28 | 18 | +0,0794 | +1,47 |

**Không đọc được gì từ bảng này hôm nay**, và đó là **đúng thiết kế**: cột `n từ 22/08` của **mọi
khoá đều bằng 0**. Số trên là **lịch sử đã bị nhìn thấy** ⇒ chỉ dùng cho quyết **DỪNG** (ngày đọc
**27/08**), **không** dùng để phong chức ai. `deepseek-reasoner`/MB chạm `z = +1,98` là **đúng
loại số** đã làm hỏng 11 lời khen trước đây: cao nhất trong 45 khoá thì tự nhiên phải có một khoá
sát ngưỡng.

### 5.1 · Bảng rà mục quá hạn — và hai chỗ phải nói thẳng

**Số không phải 102 mà là 113.** «102» là số đếm **tối 21/08**; qua một đêm thêm **11 mục** chạm
hạn. Ghi thẳng thay vì ép số cũ cho khớp — một bảng rà mà sai ngay ở dòng đếm thì phần sau không
ai tin được nữa (`RM-11`).

**Bản nháp đầu của chính em chỉ phủ 6/11 trạng thái**, để lại **31 mục không có hạn** — đúng lỗi
«làm nửa chừng» mà `§60.1` cấm. Đã vá, nay **11/11**.

Xếp theo **trạng thái thật** chứ không theo ngày, vì xếp theo ngày thì cả trăm dòng trông giống
nhau hết:

| nhóm | là gì | bao nhiêu | hạn đề xuất |
|---|---|---:|---|
| `MEASURED_ROOT_CAUSE` | đã đo ra gốc, **chưa vá** | **35** | 05/09 |
| `DEPLOYED_PENDING_LIVE_VERIFY` | đã lên máy, chờ xác minh sống | **23** | 29/08 |
| `MEASURED_BUT_NOT_FIXED` | đã đo, chưa vá | **14** | 05/09 |
| `WAIT_LIVE` | chờ dữ liệu sống | **14** | 29/08 |
| `OWNER_LOCK` + `AWAITING_OWNER_OK` + `OWNER_DECISION_NEEDED` + `DEPLOYED_PENDING_OWNER_VERIFY` | **chờ chữ ký owner** | **19** | 25/08 |
| `READY_NOT_DEPLOYED` | sẵn sàng, chưa lên máy | **5** | 29/08 |
| còn lại (`MEASURED_ROOT_CAUSE_FOUND`, `BLOCKED`) | | **3** | 05/09 · 25/08 |

Nhóm chờ chữ ký lấy hạn **ngắn nhất (3 ngày)** vì chúng **không tự đi được**.
**Không mục nào bị đóng.**

### 5.2 · Lật chiều bài thử chặn của `_v11034` — đáng đọc kỹ

Bản cũ viết lúc va chạm `QD-021 × QD-066` **còn sống**, nên bước [1] chờ *«thoát 1»*. Owner ký
`QD-071`, ba mục nay mang `thay_boi` ⇒ trạng thái thật là **SẠCH** ⇒ [1] ra 0 ⇒ **bài thử báo
TRƯỢT trong khi cổng vẫn đúng**.

> Một bài thử neo vào **trạng thái nhất thời** thì mỗi lần sự thật đổi nó lại kêu oan, rồi sẽ bị
> ai đó tắt đi. Bản mới đo **đúng điều cần đo**: *gỡ `thay_boi` ra thì cổng có ĐỎ LẠI không.*

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v11102_kiem_thuoc_model.py` | K1 hai danh sách rời nhau · K2 mỗi ngày đủ **cả hai họ** · K3 không lọt lượt trễ |
| `_v11102_kiem_thuoc_model.py --thu-chan` | **5 phép hai chiều** — ép giao nhau ⇒ K1 đỏ; ép mốc sớm ⇒ K3 đỏ; khôi phục ⇒ xanh lại |
| `_v11102_bang_cong_don.py --thu-chan` | bẻ một con số ⇒ đỏ · bỏ một khoá ⇒ đỏ · gốc ⇒ khớp · `_z(0,0) is None` |
| `_v11102_don_dong_ro.py --thu-chan` | mốc thật 334 · ép `00:01` ⇒ **6.534** · ép `23:59` ⇒ **0** · khôi phục ⇒ **334**, `FREEZE_MARKS` nguyên trạng |
| `_v11089_cham_lane_tb.py --thu-chan` **trên VPS** | **6/6**, gồm **2 phép chống LOOKAHEAD** (T3 dòng tạo sau kết quả · T6 tạo đúng lúc kết quả về) |
| `_v11034_kiem_cheo_quyet_dinh.py --thu-chan` | **3/3 chiều ngược**, sổ khớp **từng byte** |
| `_v11044_cong_so_hieu.py` | `SO_HIEU_V11044=KHOP` |
| `_v11062_nang_version.py --kiem` | `NANG_VERSION_V11062=ĐẠT` — bốn mặt đi cùng nhau |
| `_v10920_decision_ledger.py` | không quyết định nào bị trôi |

### Nghiệm thu deploy

| phép | kết quả |
|---|---|
| md5 local = VPS | `f06fce9d…` (scorecard) · `f717a389…` (bộ chấm T-B) — **khớp từng byte** |
| `py_compile` **trước** restart | `PY_COMPILE_OK` cả hai tệp |
| PID trước → sau | `2110106 → 2128063` (scorecard gọi từ `scheduler.py:665` nên **phải** restart) |
| smoke | `health = 200` · `admin/bay-dan-shadow = 401` |
| lỗi sau restart | **0** Traceback/CRITICAL |
| **4 bảng khoá PRE = POST** | `predictions` 13.089 · `final_bundles` 525 · `lottery_results` 15.324 · `model_daily_eval` 12.953 |
| cron | 136 → **137** dòng · bản sao `/tmp/cron.bak.v11102` |

> **`admin = 404` ở lượt smoke đầu là đường KHÔNG TỒN TẠI, không phải chuyện quyền.** Đã kiểm lại
> bằng route admin có thật ⇒ **401**. Ghi ra đây vì đọc nhầm 404 thành «mất xác thực» là một
> báo động giả rất dễ mắc.

### Vì sao verdict KHÔNG phải `RUNTIME_PROVEN`

Lượt production **05:00 ngày 22/08** chưa chạy — lúc làm việc này là **00:00 VN**. Hai thứ phải
đọc lại **sau** lượt đó, và **chưa đọc thì chưa được kết luận** (`RM-16` — mốc theo **giờ tạo
từng bản ghi**, không theo ngày):

1. prompt phải đóng dấu **`CTX-18.4`** (`FU-404`). Bản trên VPS **đã có** `CTX-18.4` ở
   `gpt_analyzer.py:844`, md5 khớp local từng byte — nhưng **trace mới nhất là 17:48 ngày 21/08**,
   tức **trước** deploy. Chưa lượt nào chạy trên bản mới.
2. job `measurement_materialize` phải sinh **cả hai họ** cho ngày 22/08.

---

### 6.1 · LOCAL và VPS khớp nhau từng con số

Cùng phép dọn, cùng phép cộng dồn, chạy độc lập hai nơi:

| phép | local | VPS |
|---|---|---|
| dòng đối chiếu được | 9.021 | **9.021** |
| dòng rò tìm ra | 334 (MT 286 · MB 47 · MN 1) | **334** (MT 286 · MB 47 · MN 1) |
| còn lại sau khi xoá | 0 | **0** |
| khoá bảng cộng dồn | 108 | **108**, khớp quét thô |
| cổng thước | `SẠCH` | **`SẠCH`** |

### 6.2 · BA PHÉP TRÔI sau nửa đêm — không cái nào do việc đêm nay

Cổng sổ quyết định báo **3 phép trôi** lúc 01:00. Truy từng cái:

| mã | nguyên nhân thật | xử |
|---|---|---|
| `QD-021` | K8 báo `FU-360` **mồ côi đến hạn ≤24/08** — miễn trừ `QD-066` cho `FU-360`/`FU-389` **hết hạn cuối ngày 21/08**. GĐ-6 đã dự báo đúng chuyện này từ tối qua | nằm trong bảng rà 113 mục · **chờ owner** |
| `QD-027` | bảng khuyến cáo hôm nay **rỗng vì mới 1 giờ sáng**, job của ngày chưa chạy | tự hết sau lượt hôm nay |
| `QD-046` | **`glm-5.1` trả lời RỖNG trên MN** ⇒ rớt sàn ứng viên | → **`FU-423`**, hạn 25/08 |

**`QD-046` KHÔNG phải báo động giả — đã kiểm kỹ vì rất giống một cái.** Bản vá `V11096` (21/08)
đã tách «rớt sàn» khỏi «đã ngừng chạy», và nó **loại đúng** `gemma-4-31b` (nghỉ hẳn từ 29/07,
không còn trong cả hai danh sách). Model thực sự bị đếm là **`glm-5.1`**:

```
glm-5.1  MN  7 ngày: 7 lượt · 2 RỖNG        30 ngày: 30 lượt · 2 rỗng
glm-5.1  MB           0 rỗng / 30           MT: 1 rỗng / 28
```

Phép kiểm bắt đúng khuôn `n < MIN_MAU_DU_TUYEN ≤ n + rỗng` — tức **chính việc loại lượt rỗng** đã
đẩy nó xuống dưới sàn (`MIN_MAU_DU_TUYEN = 5`). Và điều làm nó nặng: **`glm-5.1` vừa được đưa vào
danh sách output ngày 21/08** (`FU-380`). Một model **đang góp số công bố** mà **không đủ mẫu để dự
tuyển** ở MN là hai vai trò mâu thuẫn nhau.

> **Đã ghi rõ trong sổ: cấm hạ sàn cho hết đỏ.** Sàn sinh ra để chặn kết luận trên mẫu mỏng; hạ nó
> là **xoá cái đèn báo** chứ không sửa cái hỏng.

---

## 7. Vướng vấp

1. **Bản vá `_rr()` đầu tiên trộn hai lượt khác nhau.** Bản đầu cho họ `OUTPUT` **lùi về** bản ghi
   độ tin cậy của lượt `shadow_auto_eval` khi không tìm thấy `official_ai_predict`. Đó là gán độ
   tin cậy của **một lượt khác** cho dòng output. Đã sửa: **vắng thì để vắng**.

2. **`python - <<'PY'` nuốt dấu thoát, làm hỏng cú pháp một script.** Chuỗi `\\n` trong heredoc
   thành `\n` thật ⇒ một khối `L.append("` bị cắt giữa dòng. Đúng bẫy `CLAUDE.md` đã ghi; đã
   chuyển sang **ghi tệp vá** thay vì heredoc.

3. **Bài thử chặn `_v11034` báo TRƯỢT trong khi cổng đúng** — §5.2.

4. **Đếm nhầm ở bảng rà: 6/11 trạng thái** — §5.1.

5. **Chạy lại 125 ngày mất hơn một giờ** — §3.6, đã ghi `FU-422`.

---

## 8. Gỡ về

| việc | lệnh |
|---|---|
| bản vá bộ chấm điểm | `/root/Lottery_AI_Test/backups/_materialize_shadow_promotion_scorecard.py.pre_v11102` → chép lại + `systemctl restart lottery` |
| bộ chấm T-B | `ssh root@14.225.224.89 'crontab /tmp/cron.bak.v11102 && rm -f /root/Lottery_AI_Test/web/backend/_v11089_cham_lane_tb.py'` |
| sổ quyết định | `backups/OWNER_DECISION_LEDGER.json.pre_v11102` |
| dòng rò đã dọn | danh sách đầy đủ trong `artifacts/v11102/dong_ro_da_don.json` — dựng lại được bằng cách chạy lại scorer cho các ngày đó |
| bốn mặt version | gỡ dòng `V11102` khỏi `HISTORY`, hạ `STATE.last_version`, **prepend** khối đính chính — **cấm** mở `"w"` |

**Điểm chấm đã ghi thì giữ** — chúng không ảnh hưởng đường chọn số.

---

## 9. Theo dõi tiếp

| mã | việc | hạn |
|---|---|---|
| `FU-404` | **đọc lại lượt 05:00 ngày 22/08**: prompt có đóng dấu `CTX-18.4` không, và job đo có sinh **cả hai họ** không | **22/08** |
| **`FU-423`** · `KS2508` | **`glm-5.1` trả lời rỗng trên MN** (2/7 lượt tuần này, chỉ ở MN) — model vừa vào danh sách output mà không đủ mẫu dự tuyển. **Cấm hạ sàn cho hết đỏ** | **25/08** |
| **`FU-422`** · `DO2908` | bộ chấm quét lại toàn bộ trace cho từng model — vá kèm **phép so hành vi từng con số** | 29/08 |
| `FU-421` · `SC2408` | ba chỗ còn phụ thuộc ngầm vào thứ tự khi điểm bằng nhau | 24/08 |
| — | **owner duyệt bảng rà 113 mục**: hạn theo nhóm dùng được không, nhóm «đã đo ra gốc chưa vá» (35 mục) có được ưu tiên không | 25/08 |
| — | `24/08`: đủ 14 ngày cho `QD-017` ⇒ **được phép đọc** lane T-B | 24/08 |
| — | `27/08`: ký khung đo, quyết **DỪNG** cho `gpt-5.5` và `qwen3-max-thinking` (đã đủ mẫu) | 27/08 |
| — | mốc **THĂNG** đếm từ **22/08**, đếm từ 0 | — |

---

## §62 (A60) — BA LỚP NGUỒN

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| **21/08 23:35** | *«`FU-420`: `QD-066` THAY `QD-021/027/065` ⇒ 102 mục quá hạn là HỢP LỆ (giữ có chủ đích, không phải trễ). KÈM ĐIỀU KIỆN: toàn bộ 102 mục được rà lại MỘT LƯỢT, trình owner MỘT bảng lời thường kèm hạn mới từng mục — hợp lệ không có nghĩa là quên.»* |
| **21/08 23:35** | *«Ba sửa chữa thước ĐÃ KÝ + bộ chấm T-B lên VPS cùng đợt — triển khai sáng sớm 22/08.»* |
| **21/08 23:35** | *«Ghi rõ ngày bắt đầu thu: 22/08 — đếm từ 0 cho mọi quyết THĂNG (bảng 90 ngày đã bị nhìn thấy, chỉ dùng cho quyết DỪNG).»* |
| **21/08 23:35** | *«CHỈ rà và trình — CẤM đóng hàng loạt mù.»* |

### `CODE_DID`

| việc | bằng chứng |
|---|---|
| writer mở cho họ OUTPUT | `_materialize_shadow_promotion_scorecard.py` — `_registry_maps()` trả 3 vế; 20/08 MN ra `OUTPUT 15 · SHADOW_AUTO 11` |
| chặn lượt trễ | `_tao_sau_moc()` + `bo_vi_tre` trong giá trị trả về; 20/08 MT loại 1, mốc `16:58+07:00` |
| bộ chấm T-B sống trên VPS | md5 `f717a389…` khớp · `155/155` chấm · cron `35 19 * * *` |
| production không lệch | PID `2110106 → 2128063` · 4 bảng khoá **PRE = POST** · `health 200` · `admin 401` · 0 lỗi |
| sổ quyết định | 72 → **73** mục · `QD-071` · `thay_boi = QD-066` trên **3/3** mục |
| bốn mặt version | `governance_seq` → **432** · `CHANGELOG` +5.729 byte · `SSOT` +1.383 byte |

### `DOC_SAID` — và chỗ tài liệu **lệch** với mã

| lệch | chi tiết |
|---|---|
| `REPORT_V11101` ≠ dữ liệu thật | *«8/15 model output có 0 dòng»* — thật là **12/15**. Đã rút lại ở §3.5 |
| `REPORT_V11101` ≠ dữ liệu thật | *«1–12% lượt trễ»* — đo được **3,4%**. Đã rút lại ở §3.5 |
| `_v11089_cham_lane_tb.py` docstring ≠ thực tế mới | tệp tự ghi *«⚠️ Chưa deploy lên VPS — vùng cấm phiên này»*. Từ 22/08 câu đó **hết đúng** — đã lên VPS, có cron. Ghi ra đây để không ai đọc lại rồi tưởng chưa deploy |
| `docs/FOLLOW_UP_TRACKER.md` ≠ sổ quyết định | vẫn ghi `FU-216` hạn 09/08, `FU-231`/`FU-226` hạn 10/08 — chưa theo `QD-045` đã dời mốc sang 21/08 |

---

**TanPhatAI cần làm:** cập nhật `docs/OWNER_DECISION_LEDGER.json` (`QD-071` đóng `FU-420`; ba mục `QD-021/027/065` nay mang `thay_boi = QD-066`), `docs/FOLLOW_UP_TRACKER.md` (`FU-421` hạn 24/08, `FU-422` hạn 29/08, **`FU-423` hạn 25/08 — `glm-5.1` rỗng trên MN, ưu tiên cao vì model này đang góp số công bố**), và `docs/RA_102_MUC_QUA_HAN_20260822.md` (113 mục chờ owner duyệt hạn mới — **chưa mục nào bị đóng**); theo dõi ba việc: ① lượt 05:00 ngày 22/08 phải đóng dấu `CTX-18.4` và job đo phải sinh **cả hai họ** — chưa chạy thì chưa kết luận, ② ngày 24/08 mới được phép đọc lane T-B (`QD-017` đủ 14 ngày; nay đã có 111 cặp bất đồng nhưng **cấm đọc sớm**), ③ ngày 27/08 quyết DỪNG cho `gpt-5.5` và `qwen3-max-thinking` — hai model đã đủ mẫu, và mốc đếm cho quyết THĂNG bắt đầu từ **22/08, đếm từ 0**.
