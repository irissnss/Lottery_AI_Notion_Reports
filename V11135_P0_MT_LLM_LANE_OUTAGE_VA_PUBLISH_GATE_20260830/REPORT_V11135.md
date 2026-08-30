# REPORT V11135 — HAI LỖI LÀM MẤT MỘT NGÀY CỦA OWNER: TOKEN BỊ TIÊU OAN VÀ CỔNG PUBLISH LÀM TRẮNG

```
REPORT_VERSION        : V11135
WORK_DATE_ICT         : 2026-08-29 → 2026-08-30
TIMEZONE              : Asia/Ho_Chi_Minh / UTC+07:00
OWNER_DECISION        : prompt 43 R1 — P0 MT_LLM_LANE_OUTAGE
ACTOR_RUNTIME         : CLAUDE_CODE
PREVIOUS_PUBLIC_HEAD  : ed73afeb485d49662456cda4d96ec9c0b72cdda1  (V11134)
LABELS                : SCHEDULER_ROOT_FIX=RUNTIME_PROVEN ·
                        PUBLISH_GATE_FIX=RUNTIME_PROVEN ·
                        C1_C6=CODED_NOT_DEPLOYED · C5=BLOCKED_NOT_IN_RELEASE
```

---

## 1 · TÓM TẮT

Ngày 28/08 owner mất trọn một ngày dự đoán ở miền Trung. **Hai lỗi riêng biệt, hai tầng khác
nhau, cộng lại.** Cả hai đã vá, deploy, và có bằng chứng hành vi thật.

| # | lỗi | tầng | trạng thái |
|---|---|---|---|
| 1 | Một lần thử **bị chặn** vẫn tiêu mất suất gọi AI duy nhất trong ngày | GENERATION | 🟢 `RUNTIME_PROVEN` — MT lấy lại 8/8 LLM ngày 29/08 |
| 2 | Cổng publish đòi **đúng 15** model, làm **trắng** một bundle hợp lệ | DELIVERY | 🟢 `RUNTIME_PROVEN` — MT 28/08 hiện ra `PUBLISHED_DEGRADED` |

**Ba đính chính bắt buộc** so với mô tả ban đầu:

- *«MT không có output»* — **không đúng ở tầng FINAL**. Row `786` tồn tại, chốt **16:55** (trước
  mốc khoá 16:58), đủ `bach_thu` `lo2` `lo3` `xien2` `xien3`. Nhãn đúng: **`MT_LLM_LANE_OUTAGE`**.
- *«ML-only»* — cũng không chính xác. Sáu nguồn là **4 ML base + 2 aggregator**, `shadow ∩ = 0`.
- *«toàn bộ FINAL 29/08 sai»* — **đúng**, 3/3 LOSE. Nhưng `n=3` **không đủ** để kết luận về TOTAL:
  nếu FINAL đúng bằng nền 39,3% thì xác suất 0/3 vẫn là **22%**.

---

## 2 · OWNER YÊU CẦU GÌ — NGUYÊN VĂN

**29/08 00:47** — *« MT 28/08 có FINAL hợp lệ… Cấm recompute row 786, đổi số, backfill LLM/Combo,
sửa FINAL lịch sử… Không được tiếp tục dùng "có dòng AI_ONCE_DAILY_ATTEMPT trong log" làm bằng
chứng duy nhất rằng token đã bị tiêu. »*

**30/08 ~12:40** — *« MT nay đã sẵn sàng chưa nha em chứ hôm qua thì mất 1 ngày của anh rồi đó
nha em… anh thấy em vẫn quá lòng vòng hời hợt quá em »*

**29/08 21:42** — *« toàn bộ FINAL/lane dự đoán ngày 29/08 đều sai; một số đơn model có tín hiệu;
TOTAL/FINAL lại chọn tệ… Không dừng ở kết luận INSUFFICIENT_POWER. »*

---

## 3 · LỖI SỐ 1 — TOKEN BỊ TIÊU OAN

### 3.1 · Dòng thời gian, đến từng giây

| ngày | kết quả MN về | MT AI chain chạy | MT LLM |
|---|---|---|---|
| 26/08 | 16:36:40 | 16:38:13 | 8 |
| 27/08 | 16:37:42 | 16:39:41 | 8 |
| **28/08** | **16:42:42** | **KHÔNG CHẠY** | **0** |

```
16:42:00  [AI_ONCE_DAILY_ATTEMPT] MT source=fallback     ← scheduler.py:5338 GHI DẤU
16:42:00  🚫 [FALLBACK_BLOCKED] MT: MN:0/3, D2=OK        ← scheduler.py:5368 CHẶN
16:42:42  ← kết quả MN mới thực sự về
16:43:09  🚫 [AI_ONCE_DAILY_BLOCK] attempt_marker=1      ← scheduler.py:5326 CHẶN RETRY
16:55:00  [T10_CHOT] MT: bundle chốt BT=11 (v1)          ← chỉ còn 6 nguồn
```

### 3.2 · Nguyên nhân gốc

`ROOT_CAUSE = BLOCKED_ATTEMPT_CONSUMES_ONCE_DAILY_TOKEN`

Dấu được ghi ở **`:5338`**, cổng chặn ở **`:5361-5375`** — **cách nhau 23 dòng**. Khi chặn nó dọn
`CURRENT_RUN_ID` (`:5374`) nhưng **không thể rút lại dòng log đã ghi**. Hàm
`_owner_ai_token_attempt_exists` (`:2185-2206`) chỉ **đếm dòng log** — không phân biệt lần thử
**thành công** với lần thử **bị chặn**.

**Kết quả MN về muộn hơn thường lệ ~5 phút. Cron fallback kiểm trước 42 giây. Một cuộc đua 42
giây làm mất cả lane LLM của một miền trong một ngày.**

### 3.3 · Bản vá — máy trạng thái, không phải dời log

| trạng thái | tiêu suất? |
|---|---|
| `BLOCKED_PRECONDITION` — chưa qua cổng upstream, chưa gọi provider | 🟢 **KHÔNG** |
| `RUNNING` — đang chạy, kèm **lease 600s** chống hai caller song song | 🔴 CÓ, trong hạn |
| `SUCCESS` — đã chạy xong, output đã persist | 🔴 **CÓ** |
| `FAILED_RETRYABLE` — thất bại trước khi persist | 🟢 KHÔNG, giải phóng ngay |
| `FINAL_LOCK_PASSED` — sau mốc khoá, dùng `FREEZE_MARKS` của dự án | — |

Dấu **định dạng cũ** (không có `state=`) **vẫn tiêu suất** — hướng bảo thủ, không viết lại lịch sử.

**T1–T12 + META: 15/15 ĐẠT** — 13 phép **hành vi** (trích đúng hàm đã vá rồi `exec` với DB giả) ·
2 phép **cấu trúc**. Tôi ghi tách hai loại để không ai đọc nhầm là đã chứng minh nhiều hơn thực tế.

🔑 **META-1** chứng minh bằng thực thi: bản **gốc** trả `(True, 'attempt_marker=1')` trên dấu thô —
**đúng lỗi 28/08**; bản vá trả `False`.

### 3.4 · Runtime proof

```
PRE  sha256 scheduler.py : a6c8bfff60b6c252de3b7281926ca163a96044bbd77e3d10
POST sha256              : 2961987d8c3a6e27a962cd3bf3f76c023eebd3a224d13789
diff                     : +110 dòng · −9 dòng (đúng parser cũ + khối dấu sớm)
backup                   : scheduler.py.bak_v11136, chmod 444, hash KHỚP PRE
PID                      : 2694667 → 2866664
ExecMainStartTimestamp   : 2026-08-29 00:40:36 +07
bytecode                 : pyc ghi src mtime 1787938834 / size 478436 — KHỚP CHÍNH XÁC nguồn
                           tiến trình khởi động SAU khi biên dịch 2 giây
health · traceback       : 200 · 0
job đăng ký lại          : MN 05:15 · MT 16:42 · MB 17:42
```

### 3.5 · 🟢 LIVE PROOF — ngày 29/08

| miền | ML | LLM | AGG | HYBRID | `model_count` |
|---|---|---|---|---|---|
| MN | 4 | 8 | 2 | 2 | 15 |
| **MT** | 4 | **8** | 2 | 2 | **13** *(28/08 là 6)* |
| MB | 4 | 8 | 2 | 2 | 13 |

MT chạy tới **17:15**, FINAL chốt **16:47:26** — trước mốc khoá 16:58. **Lane LLM của MT quay lại
đầy đủ.** Ngày **30/08** MN ghi đúng chuỗi `state=RUNNING` → `state=SUCCESS`.

⇒ **`SCHEDULER_ROOT_FIX = RUNTIME_PROVEN`**.

---

## 4 · LỖI SỐ 2 — CỔNG PUBLISH LÀM TRẮNG BUNDLE HỢP LỆ

### 4.1 · Điều owner thực sự nhìn thấy

Ảnh màn hình owner gửi ghi đúng chữ:

```
Gate: WAIT_OUTPUT_ELIGIBLE_ROW_COUNT · output rows 6/15 · scoreable 6/15
Thiếu: claude-opus-4-6, claude-sonnet-4-6, combo-super, deepseek-reasoner,
       gemini-2.5-flash, gemini-2.5-pro, glm-5.1, gpt-5.4, gpt-oss-120b
```

`main.py:597` — `publish_ready = len(output_models) >= expected_count` với `expected_count = 15`.
MT có 6 ⇒ **ba nhánh** đều trả `bundle: None`.

| miền | `model_count` DB | API trả |
|---|---|---|
| MN | 15 | ✅ `784` |
| **MT** | **6** | 🔴 **`null`** |
| MB | 14 | ✅ `787` |

⚠️ Điều này **vi phạm trực tiếp hợp đồng owner đã khoá**: *«N≥1 official hợp lệ ⇒ vẫn tạo DEGRADED
FINAL, không để blank»*. Bundle có **N=6 official**, `bundle_quality=DEGRADED`,
`incomplete_bundle=true` — đúng ca hợp đồng bắt phải hiện.

### 4.2 · Bản vá

`N ≥ 1` ⇒ trả bundle kèm **bảy trường** owner khoá: `degraded` · `degraded_reason` ·
`missing_lanes` · `active_model_ids` · `expected_model_count` · `actual_model_count` ·
`eligibility_version`.
`N = 0` ⇒ `NO_OUTPUT` kèm lý do phân biệt: `ZERO_OFFICIAL_SOURCE` (có bundle, 0 nguồn) và
`NO_BUNDLE_FOR_DATE_REGION` (không có bundle nào).

🔴 **Bộ thử bắt được một lỗ trong chính bản vá của tôi**: có **BA** nhánh làm trắng, bản đầu tôi
mới vá **hai**. Nhánh thứ ba (`main.py:11111`, ca *«không có bundle nào»*) trả `null` là **đúng**,
nhưng nhãn phải là `NO_OUTPUT` — đã sửa.

**P1–P11 + META-1/2: 13/13 ĐẠT** — 5 hành vi · 8 cấu trúc.

**Không cần migrate schema:** kênh `incomplete_bundle` **đã có sẵn** và **đã đặt đúng**
(`true` cho MT/MB, `false` cho MN).

### 4.3 · Runtime proof + END-TO-END

```
PRE  sha256 main.py : ec2540331be14115ade4bebc8d50d3c9de3430faf4916404
POST sha256         : 42ffe2e6b456f48a26458049…
diff                : +140 dòng · −39 dòng (đúng hai khối bundle=None cũ) + 4 dòng nhánh ba
backup              : main.py.bak_v11136, chmod 444, hash KHỚP PRE
PID                 : 2866664 → 2897561 · health 200 · 0 traceback
```

**Gọi handler thật cho ca MT 28/08:**

```
MN   bundle=784   status=OFFICIAL             degraded=None
MT   bundle=786   status=PUBLISHED_DEGRADED   degraded=True   active=6
     missing_lanes: {"LLM":[8 model], "HYBRID":["combo-super"]}
     msg: Official DEGRADED: 6/15 model output-eligible. Thiếu lane: LLM(8)+HYBRID(1)
MB   bundle=787   status=OFFICIAL             degraded=None
```

**11/11 ĐẠT**, MN/MB không regression.

---

## 5 · BẤT BIẾN FINAL — KHÔNG SỬA MỘT CHỮ

| | |
|---|---|
| row 786 chuỗi | `786\|11\|1\|2026-08-28 16:55:00` — PRE **==** POST |
| `sha256(source_predictions_json)` | `8aa789870b0ca19c5fec21e95701b52b9907fcc64b8af4a9…` — PRE **==** POST |
| canonical row hash | MN `806e8f8cd8b2…` · MT `5b8a546e13f8…` · MB `071e1eb85ef5…` |
| bảng khoá | không bảng nào giảm dòng qua **hai** lần deploy |

---

## 6 · SÁU COMPONENT CỦA ROW 786

| MODEL_ID | TYPE | RUN_SOURCE | OFFICIAL | CONTRIBUTION |
|---|---|---|---|---|
| `lstm` | ML_BASE | auto_daily | official | 0,0306 |
| `meta-learning` | ML_BASE | auto_daily | official | 0,0445 |
| `random-forest` | ML_BASE | auto_daily | official | 0,0395 |
| `xgboost` | ML_BASE | auto_daily | official | 0,0518 |
| `smart-ml` | ENSEMBLE | auto_daily | official | 0,0916 |
| `smart-ensemble` | ENSEMBLE | auto_daily | official | 0,0202 |

**`shadow ∩ = 0`.** `model_count=6` ≠ 7 dòng predictions vì `combo-no-token` có dự đoán nhưng
**đóng góp 0** (`output_eligible=False`). Không TOTAL, không fallback source.

---

## 7 · NGÀY 29/08 — SÁU VERDICT

**Availability 29/08 LÀNH** — nên ngày này được so như một ngày bình thường.

| # | verdict | kết quả |
|---|---|---|
| 1 | `GENERATION_SIGNAL` | 🟢 **OBSERVED — CÓ tín hiệu**. 21/48 model có TOP1 trúng = **43,8%** so với nền **39,3%** (+4,4 điểm) |
| 2 | `CAP_PRESERVATION` | ⚪ **`NOT_VERIFIED`** — chỉ `smart-ml`/`smart-ensemble` lưu top-5; 14 model còn lại không lưu |
| 3 | `AGGREGATION` | 🔴 **`TOTAL_SELECTION_LOSS`** cả ba miền · `FIRST_STAGE_LOST = STAGE 6` |
| 4 | `OVERRIDE` | 🟢 **`NO_OVERRIDE`** cả ba miền — `vote_winner == published` |
| 5 | `FINAL` | 🔴 3/3 LOSE — MN `92` · MT `02` · MB `91` |
| 6 | `SCORER` | 🟢 **ĐÚNG** — **12/12** sản phẩm khớp DB tuyệt đối |

**Base độc lập có TOP1 trúng mà TOTAL không chọn:** MN **7** · MT **4** · MB **3**.

⚠️ **Nhưng 29/08 một mình không kết luận được**: nếu FINAL đúng bằng nền 39,3% thì xác suất **0/3**
vẫn là **22%**.

---

## 8 · CỬA SỔ LỊCH SỬ ĐÓNG BĂNG — ĐÂY MỚI LÀ BẰNG CHỨNG

`n = 273` lượt ngày–miền, 29/05–27/08, **không trộn** 28–29/08.

| | tỉ lệ |
|---|---|
| `gemini-2.5-pro` — model đơn tốt nhất | **37,00%** |
| `gemini-2.5-flash` · `combo-super` | 35,53% |
| nền mật độ số về | 33,87% |
| random source pick (seed `20260829`, 2000 lần) | 32,60% |
| 🔴 **M0 — FINAL đang chạy** | **30,77%** |

**FINAL thấp hơn model đơn tốt nhất 6,23 điểm · thấp hơn bốc ngẫu nhiên một nguồn 1,83 điểm.**

**Paired 13 model, Bonferroni `α = 0,00077`:**

| | |
|---|---|
| model chứng minh được **hơn** M0 có ý nghĩa | **0/13** (`gemini-2.5-pro` gần nhất, p=0,078) |
| model có tỉ lệ **cao hơn** M0 | **7/13** |
| M0 vs random-source (McNemar) | 31 vs 41 · p = 0,2888 — **không có ý nghĩa** |

⚠️ **Đọc cho đúng:** đây **chưa** phải bằng chứng thống kê để cắt TOTAL. Nó là **tín hiệu kiến
trúc nhất quán qua nhiều phép so** — TOTAL không cộng thêm giá trị, và có dấu hiệu **trừ đi**.

---

## 9 · VƯỚNG VẤP — KỂ CẢ LỖI CỦA CHÍNH TÔI

🔴 **Tôi công bố một verdict quá mạnh rồi phải rút sau 2 giờ.** `V11133` viết
`SHADOW_CHANGED_FINAL = FALSE` dựa trên 0/871 component shadow. Con số đúng, nhưng nó chỉ nói về
**một** kênh còn tôi viết như thể nói về **mọi** kênh. Có kênh thứ hai: `gemini-3.5-flash` vào
chấm điểm Combo qua `ai_confirm` **3 lần** (12/08 · 13/08 · 23/08, đều MN), mỗi lần **rơi đúng số
được chọn**. **Bài học:** trước khi viết `X = FALSE`, phải **đếm có bao nhiêu đường X có thể xảy
ra**, và nói rõ đã soi đường nào.

🔴 **Suýt công bố một kết luận SAI về hạ tầng.** Truy vấn `scheduler_logs` trả rỗng, tôi in
*«thực sự không có dòng nào»*. Sự thật: **75 dòng**, trong đó **26 dòng `ai_predict`** — chính là
mắt xích tôi tìm cả buổi. Nguyên nhân: truy vấn tham chiếu cột `status` không tồn tại,
`sqlite3` báo lỗi ra `stderr` mà hàm đọc chỉ lấy `stdout`. Bắt được nhờ **hai con số ngược nhau
trong cùng một phiên**. Đã sửa hàm đọc để in cảnh báo khi `stderr` khác rỗng.

🟡 **Cổng của chính tôi mắc lỗi `RM-09`.** Phép kiểm *«không official reader nào đọc lane shadow»*
grep chuỗi thô và báo động giả: `main.py:16954` có `v10622_parallel_lane_shadow_live_board` chứa
chuỗi đó. Đã neo lại vào đường dẫn thật, xác minh **cả hai phía**.

🟡 **Phép counterfactual của tôi tự bị đối chứng âm bác.** Mô hình quy đổi `final_score / Σ weight`
làm đổi top-1 ở **3/23 ca dù không bỏ gì** ⇒ mô hình vô giá trị. Truy ra: manifest chỉ lưu **2 số**
và `factors` **bỏ sót toàn bộ** bonus hậu kỳ (`final_score` lớn hơn tổng weight ở **85/87** ca).
⇒ **`MANIFEST_CANNOT_RECONSTRUCT_ITS_OWN_SCORE`**.

🟡 **Bộ thử publish bắt lỗ trong chính bản vá của tôi** — ba nhánh, tôi mới vá hai.

🟡 **Phép kiểm `NRestarts` của tôi sai giả định** — nó đếm restart **tự động sau lỗi**, không đếm
`systemctl restart`. Bằng chứng đúng là PID đổi + bytecode khớp.

🟡 Bốn lỗi kỹ thuật nhỏ: ký tự null thật trong `tr` · `stat -c %%Y` in ra chữ `%Y` · `datetime()`
trả `NULL` nuốt cả dòng · đặt tên tệp `signal.py` che module `signal` của Python.

---

## 10 · BA LỚP NGUỒN (§62)

**`OWNER_SAID`** — xem mục 2, nguyên văn kèm giờ.

**`CODE_DID`**

| việc | evidence |
|---|---|
| lỗi token | `scheduler.py:5338` ghi dấu · `:5368` chặn · `:2185-2206` chỉ đếm dòng |
| race 42 giây | MN về `16:42:42` · cron kiểm `16:42:00` · retry chặn `16:43:09` |
| vá scheduler | `a6c8bfff60b6` → `2961987d8c3a` · PID `2694667→2866664` · pyc khớp nguồn |
| live proof | MT 29/08: **8/8 LLM**, `model_count 6→13`, FINAL 16:47 trước khoá |
| lỗi publish | `main.py:597` `>= 15` · ba nhánh trả `bundle: None` |
| vá publish | `ec2540331be1` → `42ffe2e6b456` · PID `2866664→2897561` |
| end-to-end | MT 28/08 → `bundle=786` · `PUBLISHED_DEGRADED` · `degraded=true` |
| bất biến | `sha(spj)` row 786 PRE == POST qua **hai** lần deploy |
| 29/08 | 21/48 TOP1 trúng · `NO_OVERRIDE` ×3 · scorer 12/12 đúng |
| cửa sổ đóng băng | M0 **30,77%** · best model **37,00%** · random source **32,60%** |

**`DOC_SAID`** — `CLAUDE.md §55` `scheduler_logs` naive là **UTC, cộng 7**: đã áp dụng đúng.
`docs/CURRENT_TRUTH_SSOT.md` chưa cập nhật hai bản vá — `DOC_SAID` chậm hơn `CODE_DID`, đúng khung
`PRJ-INTERACTION-LEDGER-001`.

---

## 11 · RUNTIME_LADDER

| hạng mục | bậc |
|---|---|
| **scheduler root fix** | 🟢 **`RUNTIME_PROVEN`** — hành vi scheduled thật 29/08 + 30/08 |
| **publish gate fix** | 🟢 **`RUNTIME_PROVEN`** — end-to-end trên ca thật MT 28/08 |
| C1 · C2 · C3 · C4 · C6 | ⚪ **`CODED_NOT_DEPLOYED`** — 108 phép thử ĐẠT, 0 tệp trên VPS |
| C5 (A5 prompt) | 🔴 **`BLOCKED_NOT_IN_RELEASE`** |

**C5 bị chặn vì hai điểm, không phải vì thiếu thời gian:** emitter **không emit `SYSTEM_PROMPT`**
(7.935 ký tự = 16,4%) nên mọi con số ô nhiễm đo trên chuỗi **thiếu**; và **cổng có sẵn của dự án
`_v11107_cong_prompt_mo_coi.py` vẫn thoát 1** trên bản đã sửa.

---

## 12 · NOT_VERIFIED

| # | chưa rõ | thiếu gì |
|---|---|---|
| 1 | admin delivery ở tầng **HTTP/session thật** | tôi kiểm ở tầng handler với session admin giả; không có thông tin đăng nhập và không được lấy |
| 2 | ba ca rò rỉ `ai_confirm` **có lật top-1 không** | manifest không tái lập được chính điểm của nó |
| 3 | `CAP5` cho 29/08 | 14/16 model không lưu top-5 |
| 4 | `gemini-2.5-pro` 37,00% có phải kỹ năng thật | p=0,078, chưa qua Bonferroni |
| 5 | 3-càng | `MISSING_PIPELINE / NOT_SCORABLE` — không có writer |

---

## 13 · MUTATION_LOG

| | |
|---|---|
| deploy | 🟡 **HAI tệp**: `scheduler.py` · `main.py` — mỗi tệp backup `chmod 444` riêng |
| restart | 🟡 **hai lần** — PID `2694667 → 2866664 → 2897561` |
| ghi production DB | ❌ **KHÔNG** — mọi truy vấn `-readonly` |
| FINAL / prediction lịch sử | ❌ **KHÔNG ĐỔI** — chứng minh bằng hash PRE==POST |
| roster · prompt · override · TOTAL | ❌ **KHÔNG ĐỔI** |
| C1–C6 · C5 | ❌ **KHÔNG deploy** |
| credential · SSH · Notion · ERP | ❌ **KHÔNG CHẠM** |

**Rollback:** `cp <tệp>.bak_v11136 <tệp> && systemctl restart lottery`, so PID trước/sau.
Cả hai backup còn nguyên, `chmod 444`, hash khớp PRE.

---

## 14 · DECISION PACKET — MỘT CÂU OWNER CẦN KÝ

**1 · Đang sai ở đâu.** FINAL chọn kém hơn cả bốc ngẫu nhiên một nguồn (30,77% so với 32,60%), và
kém model đơn tốt nhất 6,23 điểm — trên 273 lượt.

**2 · Số thắng mất ở stage nào.** `STAGE 6` (TOTAL/ranking). Ngày 29/08 có 7/4/3 base độc lập
trúng top-1 mà TOTAL không chọn. Không phải lỗi generation, không phải override, không phải scorer.

**3 · Phương án.** Chạy **shadow** `DIRECT_BASE_ONLY` và `CAP5_CANDIDATE_PRESERVING` song song với
TOTAL official trong **30 ngày**, ghi cả hai, **không đổi official**.

**4 · Được gì.** Sau ~30 ngày có `n ≈ 90` lượt **tiến cứu** — đủ để trả lời dứt điểm thay vì mãi
`INSUFFICIENT_POWER`. Hồi cứu không bao giờ đủ (V10655→V10790: sáu lần bật bằng backtest, sáu lần rữa).

**5 · Mất gì / rủi ro.** Không gì về output. Lane ghi ra tệp riêng, DB mở `mode=ro`, không reader
official — ba tính chất ở mức **cấu trúc**, không phải lời hứa.

**6 · Forward evidence.** `PROSPECTIVE_SHADOW`, stop-rule đăng ký trước, không đọc giữa chừng.

**7 · `effective_from`** = 30/08. **8 · Rollback** = xoá dòng cron, artifact giữ làm bằng chứng.

**9 · CÂU CẦN KÝ:**

> **Có cho phép chạy hai lane shadow `DIRECT_BASE_ONLY` và `CAP5_CANDIDATE_PRESERVING` trong 30
> ngày, KHÔNG đổi official, để cuối kỳ có bằng chứng tiến cứu quyết định TOTAL hay không?**

**Chưa đề xuất** cắt TOTAL, nới `main_numbers[:2]`, promote/retire model, đổi roster — chưa đủ
bằng chứng, và **một ngày không được dùng để promote**.

---

TanPhatAI cần làm: ghi **HAI lỗi riêng biệt** đã làm mất ngày 28/08 của owner, cả hai nay **`RUNTIME_PROVEN`**. ① **`BLOCKED_ATTEMPT_CONSUMES_ONCE_DAILY_TOKEN`** — dấu `[AI_ONCE_DAILY_ATTEMPT]` ghi ở `scheduler.py:5338` **TRƯỚC** cổng `FALLBACK_BLOCKED` ở `:5368` **23 dòng**; kết quả MN về `16:42:42` còn cron kiểm `16:42:00` — **race 42 giây** làm MT mất **8/8 LLM**. Vá bằng **máy trạng thái** (`BLOCKED_PRECONDITION` không tiêu suất · `RUNNING` có lease 600s · chỉ `SUCCESS` mới tiêu), 15/15 thử, PID `2694667→2866664`; **live proof 29/08: MT lấy lại 8/8 LLM, `model_count 6→13`**. ② **Cổng publish** `main.py:597` đòi `>= 15` model làm **trắng** bundle hợp lệ; MT 28/08 row `786` (BT=11, chốt 16:55 **trước** khoá 16:58, 6 nguồn official, 0 shadow) bị trả `bundle: null` — **vi phạm hợp đồng owner `N≥1 ⇒ DEGRADED`**. Vá 13/13 thử, PID `2866664→2897561`, end-to-end MT 28/08 nay trả `bundle=786 · PUBLISHED_DEGRADED · degraded=true`. Ghi **ba đính chính**: *«MT không có output»* → **`MT_LLM_LANE_OUTAGE`** (FINAL có thật, đủ 5 sản phẩm); *«ML-only»* → **4 ML base + 2 aggregator**; *«toàn bộ FINAL 29/08 sai»* đúng nhưng **n=3 không đủ** (xác suất 0/3 = 22%). Ghi **sáu verdict 29/08**: generation **CÓ tín hiệu** (43,8% vs nền 39,3%) · `NO_OVERRIDE` ×3 · scorer **12/12 đúng** · mất ở **STAGE 6 TOTAL_SELECTION_LOSS**. Ghi **cửa sổ đóng băng n=273**: M0 **30,77%** — **thấp hơn** random-source-pick 32,60%, nền 33,87%, và model đơn tốt nhất `gemini-2.5-pro` **37,00%**; nhưng **0/13 model** vượt M0 có ý nghĩa sau Bonferroni, **7/13** cao hơn về dấu ⇒ **tín hiệu kiến trúc**, chưa phải bằng chứng thống kê. Ghi **FINAL lịch sử BẤT BIẾN** — `sha(spj)` row 786 PRE==POST qua hai lần deploy. **C1–C6 vẫn `CODED_NOT_DEPLOYED`** (108 phép thử ĐẠT), **C5 `BLOCKED_NOT_IN_RELEASE`** vì emitter bỏ sót `SYSTEM_PROMPT` 16,4% và cổng `_v11107` vẫn thoát 1. **Decision Packet chờ owner ký một câu** về hai lane shadow 30 ngày.
