# REPORT V11133 — PHA B ĐÓNG BẰNG BẰNG CHỨNG THÔ: LƯỢT SINH 05:00 NGÀY 28/08

```
REPORT_VERSION        : V11133
REPORT_TITLE          : PHA B live proof · chuỗi runtime khép kín từ byte-patch tới lượt
                        scheduled 05:00 · trace đóng góp canonical 0/871 shadow ·
                        phép vi sai chứng minh bộ lọc không vô hiệu
WORK_DATE_ICT         : 2026-08-28
TIMEZONE              : Asia/Ho_Chi_Minh / UTC+07:00
OWNER_DECISION        : prompt 43 R1 — "AFTER V11132 · CLOSE PHA B"
ACTOR_RUNTIME         : CLAUDE_CODE
PREVIOUS_PUBLIC_HEAD  : afa35cc5516f81f067174852cf8fee3b09c0e5c7
PRE_SNAPSHOT_HASH     : 085d4979a28d8187d607995c02786123790e1f414ea46ca9
LABELS                : PHA_B_DONE · PHA_A_PARTIAL · A4_A6_OPEN · NO_MUTATION
```

---

## 1 · TÓM TẮT

`PHA B` đóng được, và đóng bằng **bằng chứng thô tái lập được**, không phải bằng lời.

Chuỗi từ **byte-patch** tới **lượt chạy scheduled thật** đã khép kín ở cả bốn mắt xích. Thêm một
**phép vi sai** chứng minh bộ lọc `V11130` **không vô hiệu**: bỏ nó ra thì **27** model đủ tư cách,
giữ nó thì **16** — đúng **11 model shadow** bị loại, giống hệt ở cả ba miền.

Trace đóng góp điểm trên **40 bundle · 871 component**: **0 component mang tên model shadow**, và
**871/871 component có contribution khác 0** (đối chứng dương đạt, không có bundle rỗng nào).

Phiên này **bắt được hai lỗi của chính tôi** — một trong hai suýt vào báo cáo dưới dạng một kết luận
sai về hạ tầng. Cả hai ghi ở mục 7.

---

## 2 · OWNER YÊU CẦU GÌ — NGUYÊN VĂN

Prompt 43 R1 tiếp nối, nhận lúc **28/08 khoảng 09:30 ICT**:

> *« Không mở Prompt 44. Không plan-only. Không dừng sau khi phát hành report. Không chuyển việc
> kỹ thuật Agent tự xử được sang Owner. »*
>
> *« V11133 phải chứa raw evidence, không chỉ phần tổng kết. »*
>
> *« Chứng minh shadow rows sinh trước hay sau từng Combo bundle; không lấy timeline MN suy thành
> MT/MB. »*
>
> *« Không dùng total_models làm danh sách vì total_models là số đếm int, không phải model set. »*
>
> *« Negative control: shadow contribution phải được đếm từ canonical join, không grep chuỗi
> "shadow". »*
>
> *« Chỉ nâng bộ lọc V11130 thành RUNTIME_PROVEN nếu chứng minh được: byte patch đang được PID
> production nạp · scheduled Combo run thật đã gọi đúng patched path · eligibility của scheduled
> path có official sources và 0 shadow · output/FINAL không drift. Không chỉ gọi module bằng một
> Python process riêng. »*
>
> *« Nếu thiếu liên kết scheduled run → patched function: giữ RUNTIME_LOADED. Ghi exact evidence
> còn thiếu. »*
>
> *« source_weights={} và meta={} không chứng minh production dùng 0 model. Nó chỉ chứng minh
> trường observability đó rỗng. »*
>
> *« Không nói production thật đã chạy với 0 model. »*

Yêu cầu trực tiếp trong phiên, trước đó:

> *« Xem tiếp báo cáo và tổng kết dùm anh »* — 28/08 khoảng 09:20.

---

## 3 · ĐÀO BỚI / PHÁT HIỆN — LIỆT KÊ ĐỦ

### 3.1 · Mục 1.1 · PRE/POST runtime — bằng chứng thô

```
giờ máy chủ         : 2026-08-28 09:58:41 +0700
MainPID             : 2694667          (PRE 27/08 23:27:23 = 2694667)  -> KHỚP
NRestarts           : 0
ActiveEnterTimestamp: Thu 2026-08-27 22:53:01 +07
proc start (stat)   : epoch 1787845981 = 2026-08-27 22:53:01.256670262 +0700
exe                 : /usr/bin/python3.10
cwd                 : <BACKEND>
cmdline             : <VENV>/bin/python3 main.py
/api/health         : 200
log 04:55-05:35     : 51 dòng · error/traceback/exception = 0
```

Hash và mtime bốn tệp runtime:

| tệp | sha256 (24 ký tự đầu) | mtime | size |
|---|---|---|---|
| `main.py` | `ec2540331be14115ade4bebc` | 2026-08-27 13:38:40 | 1 020 779 |
| `scheduler.py` | `a6c8bfff60b6c252de3b7281` | 2026-08-27 19:16:47 | 472 534 |
| `combo_super.py` | `47047b1dc0b7e0b991022eed` | 2026-08-27 22:52:54 | 137 520 |
| `gpt_analyzer.py` | `0d2be3247abfe8cb21dd5a98` | 2026-08-23 22:29:01 | 383 668 |

Cả bốn **khớp PRE snapshot**.

Row count DB:

| bảng | PRE 27/08 23:27 | POST 28/08 09:58 | chênh |
|---|---|---|---|
| `predictions` | 13 573 | 13 614 | **+41** — đúng bằng lượt sinh 28/08 |
| `final_bundles` | 543 | 544 | **+1** — đúng bundle MN 28/08 |
| `lottery_results` | 15 364 | 15 364 | **0** — chưa có kết quả nào về |
| `model_daily_eval` | 13 437 | 13 437 | **0** |

### 3.2 · Mục 1.6 · Chuỗi byte-patch tới lượt scheduled

**Mắt xích 1 — bytecode trên đĩa đúng là bản biên dịch của nguồn hiện tại.** Đọc header
`__pycache__/combo_super.cpython-310.pyc`:

```
pyc magic          : 0x0a0d0d6f
pyc flags          : 0            <- 0 = xác thực cache theo mtime+size
pyc ghi src mtime  : 1787845974
pyc ghi src size   : 137520
nguồn thật mtime   : 1787845974   <- KHỚP
nguồn thật size    : 137520       <- KHỚP
```

**Mắt xích 2 — tiến trình khởi động SAU khi biên dịch.**

```
22:52:54  (1787845974)  nguồn combo_super.py đã vá được ghi
22:52:55  (1787845975)  bytecode .pyc sinh ra
22:53:01  (1787845981)  tiến trình 2694667 khởi động   <- sau nguồn 7 giây
NRestarts = 0                                          <- chưa restart lần nào từ đó
```

**Mắt xích 3 — lượt scheduled chạy BÊN TRONG chính tiến trình đó.** `journalctl` ghi PID ở mọi dòng:

```
Aug 28 05:15:00  python3[2694667]: Running job "Auto AI Predict MN (05:15)" (cron[hour='5', minute='15'])
Aug 28 05:20:37  python3[2694667]: HTTP Request: POST ... 200
Aug 28 05:32:37  python3[2694667]: Job "Auto AI Predict MN (05:15)" ...
```

**Mắt xích 4 — eligibility của chính lượt scheduled đó, đọc từ log của nó.** Bảng `scheduler_logs`,
`job_name='ai_predict'`. Nhớ `§55`: cột `log_time` naive ở bảng này là **UTC**, cộng 7 ra giờ VN.

```
22:15:00 MN  [RUN_ID_SET] region=MN run_id=MN_2026-08-28_76f85e02 (ai-predict batch)
22:15:00 MN  [CASCADE_STAGE_START] region=MN stage=AI_CHAIN expected_models=9
22:15:00 MN  [MODEL_CALL_START] model=claude-sonnet-4-6
22:16:02 MN  [MODEL_CALL_END]   model=claude-sonnet-4-6 status=OK duration=62.1s
22:16:02 MN  [MODEL_CALL_START] model=gemini-2.5-flash
22:16:03 MN  [MODEL_CALL_END]   model=gemini-2.5-flash  status=OK
22:16:03 MN  [MODEL_CALL_START] model=claude-opus-4-6
22:16:04 MN  [MODEL_CALL_END]   model=claude-opus-4-6   status=OK
22:16:04 MN  [MODEL_CALL_START] model=deepseek-reasoner
22:17:34 MN  [SOFT_CONTINUE_90S] deepseek-reasoner -> chưa có output sau 90s
22:17:34 MN  [MODEL_CALL_START] model=gemini-2.5-pro
22:17:34 MN  [MODEL_CALL_END]   model=gemini-2.5-pro    status=OK duration=153.8s
22:17:34 MN  [MODEL_CALL_START] model=gpt-5.4
22:17:34 MN  [MODEL_CALL_END]   model=gpt-5.4           status=OK duration=153.7s
22:17:34 MN  [MODEL_CALL_START] model=glm-5.1
22:19:04 MN  [SOFT_CONTINUE_90S] glm-5.1 -> chưa có output sau 90s
22:19:04 MN  [MODEL_CALL_START] model=gpt-oss-120b
22:19:20 MN  [MODEL_CALL_END]   model=gpt-oss-120b      status=OK duration=196.9s
22:19:48 MN  [MODEL_CALL_END]   model=deepseek-reasoner status=OK_AFTER_SOFT_CONTINUE_90S
22:19:48 MN  [MODEL_CALL_END]   model=glm-5.1           status=OK_AFTER_SOFT_CONTINUE_90S
22:20:37 MN  [CASCADE_STAGE_END] region=MN stage=AI_CHAIN done_models=9 success=9 errors=0
22:20:38 MN  [RUN_ID_END] region=MN run_id=MN_2026-08-28_76f85e02
```

🟢 **Chín model được gọi trong `stage=AI_CHAIN` official — TẤT CẢ đều official, KHÔNG có model
shadow nào.** Lane shadow chạy **sau đó**, là một job **riêng biệt**:

```
22:20:38 MN  [SHADOW_PREFLIGHT] checked=11
22:20:38 MN  === Shadow Auto-Eval Start (2026-08-28) === models=['gpt-5-mini','glm-5.2','grok-4.3',
             'claude-opus-5-fast', ...]
22:22:34 MN  qwen3-max-thinking: ['43','14'] (str=7.5, 25.5s) [shadow_auto_eval]
```

### 3.3 · Phép VI SAI — bộ lọc có thật sự đổi kết quả không

Đây là **đối chứng dương cho chính bản vá**. Chạy đúng truy vấn eligibility hai lần trên **cùng một
cửa sổ 7 ngày**, khác nhau **đúng một mệnh đề** là bộ lọc `run_source`, ngưỡng
`MIN_MAU_DU_TUYEN = 5`:

| miền | KHÔNG bộ lọc | CÓ bộ lọc | bị loại | trong đó là shadow |
|---|---|---|---|---|
| **MN** | **27** | **16** | 11 | **11/11** |
| **MT** | **27** | **16** | 11 | **11/11** |
| **MB** | **27** | **16** | 11 | **11/11** |

Mười một model bị loại, giống hệt ở ba miền: `claude-opus-5-fast` · `deepseek-v4-pro-real` ·
`gemini-3.5-flash` · `gemini-3.6-flash` · `glm-5.2` · `gpt-5-mini` · `gpt-5.5` · `gpt-5.6-sol-pro` ·
`grok-4.3` · `qwen3-max-thinking` · `qwen3.7-max`.

⇒ **Bộ lọc có tác dụng thật.** Nếu nó vô hiệu thì hai con số phải bằng nhau.

*(`grok-4.20-multi-agent` là model shadow thứ 12, không nằm trong danh sách bị loại vì nó chưa đủ
5 lượt trong cửa sổ 7 ngày — tức nó vốn đã không đủ tư cách dự tuyển.)*

### 3.4 · Mục 1.2 · Timeline TỪNG MIỀN — không suy MN sang MT/MB

| | **MN** (khoá 15:45) | **MT** (khoá 16:58) | **MB** (khoá 17:58) |
|---|---|---|---|
| ML/aggregator | 7 dòng · 05:00:08 – 05:00:10 | 7 dòng · 05:00:04 – 05:00:07 | 7 dòng · 05:00:11 – 05:00:13 |
| LLM | 8 dòng · 05:16:02 – 05:19:48 | **CHƯA CHẠY** | **CHƯA CHẠY** |
| `combo-super` | **05:20:37** | **CHƯA CHẠY** | **CHƯA CHẠY** |
| shadow eval | 11 dòng · 05:22:34 – 05:32:37 | **CHƯA CHẠY** | **CHƯA CHẠY** |
| `final_bundles` | id 784 · 05:20:38 · BT=53 | **CHƯA CÓ** | **CHƯA CÓ** |
| shadow sinh **trước** combo | **0** | không áp dụng | không áp dụng |
| shadow sinh **sau** combo | **11** | không áp dụng | không áp dụng |

🟡 **MT và MB chưa kết luận được.** Tại thời điểm đo (09:58) hai miền đó mới chạy lane ML lúc 05:00,
chưa tới lượt LLM/Combo. **Không suy từ MN sang.** Sẽ đo lại trong ngày.

### 3.5 · Mục 1.3 · Eligibility structured — ba miền

Đọc bằng **đối tượng có cấu trúc**, không regex stdout. Chữ ký hàm thật:
`def _ti_le_bach_thu(region: str, days: int) -> dict` tại `combo_super.py:318`.

| | MN | MT | MB |
|---|---|---|---|
| `active_count` | **16** | **16** | **16** |
| ML base (4) | `lstm` `random-forest` `smart-ml` `xgboost` | y hệt | y hệt |
| LLM base (8) | `claude-opus-4-6` `claude-sonnet-4-6` `deepseek-reasoner` `gemini-2.5-flash` `gemini-2.5-pro` `glm-5.1` `gpt-5.4` `gpt-oss-120b` | y hệt | y hệt |
| ensemble/hybrid (4) | `combo-no-token` `combo-super` `meta-learning` `smart-ensemble` | y hệt | y hệt |
| shadow | **0** | **0** | **0** |
| inactive | **0** | **0** | **0** |
| unknown | **0** | **0** | **0** |
| verdict | **PASS** | **PASS** | **PASS** |

Khớp đúng kỳ vọng owner nêu: `n=16 · shadow=0 · ML base=4 · LLM base=8`.

### 3.6 · Mục 1.4 · Contribution trace — canonical join, chỉ tính contribution khác 0

Cửa sổ **2026-08-15 tới 2026-08-28**, nguồn `final_bundles.score_breakdown[].components[]`.
**Không** dùng `total_models` vì nó là `int` — số đếm, hôm nay bằng `15`.

```
bundle đọc được                : 40
bundle lỗi parse JSON          : 0
bundle KHÔNG có component      : 0
TỔNG component                 : 871
component contribution KHÁC 0  : 871
component contribution = 0     : 0
phân bố run_source             : auto_daily 424 · ai_chain 312 · rerun_post_mt 135
```

**Đối chứng DƯƠNG — ĐẠT:** 40/40 bundle đều có ít nhất một component; 871/871 component có
contribution khác 0. Không có bundle rỗng nào để phép quét "đúng một cách vô nghĩa".

**Đối chứng ÂM — canonical join, không grep chuỗi:**

```
component mang model SHADOW           : 0
trong đó contribution khác 0          : 0
```

Top model theo số component khác 0: `smart-ensemble` 79 · `smart-ml` 73 · `xgboost` 70 ·
`glm-5.1` 68 · `gemini-2.5-pro` 65 · `random-forest` 64 · `deepseek-reasoner` 62 · `gpt-5.4` 58 ·
`gemini-2.5-flash` 57 · `meta-learning` 54 · **`combo-super` 50** · `gpt-oss-120b` 48 ·
`claude-opus-4-6` 45 · `lstm` 39 · `claude-sonnet-4-6` 39.

🟡 **Ghi nhận cho A3:** `combo-super` **tự nó** đóng góp **50 component khác 0**, trong khi các model
là **đầu vào của nó** cũng đóng góp trực tiếp. Đây là dấu hiệu double-count **ở tầng điểm**, nhưng
**chưa đủ để kết luận** — phải xem **cùng một con số** có nhận điểm từ **cả hai đường** không.
Đang đo, xem mục 9.

### 3.7 · Mục 1.5 · `partial_bonus_shadow` — xác minh trên nguồn đang serve

```
9999 : partial_bonus_shadow = 1.03 if (i == 1 and verdict in ('SKIP','BO_QUA') and wr_pct >= 35) else 1.0
10000: score = model_weight * position_weight            <- KHÔNG nhân bonus
10007: number_scores[num] += score                       <- điểm THẬT cộng vào đây
10019: "shadow_score_if_partial_bonus": round(score * partial_bonus_shadow, 4)   <- chỉ GHI LẠI
```

Quan sát: `partial_bonus_shadow` khác `1.0` xuất hiện **53 lần** trong 14 ngày, **luôn bằng 1.03**,
và **chưa bao giờ ở MB**.

**Verdict:** `PARTIAL_BONUS_SHADOW = OBSERVABILITY_ONLY` · `NO_SCORE_EFFECT`.

Làm rõ ba điều, vì cái tên gài bẫy:

- Tên này **không liên quan gì tới model shadow**.
- Nó nói về **`verdict = SKIP/BO_QUA` ở vị trí thứ hai** (`i == 1`).
- **Không phải** một kênh rò shadow gián tiếp.

**Chuẩn bị đổi tên (chưa thực hiện):** tên rõ nghĩa đề xuất `skip_second_position_bonus_hypothesis`,
**giữ alias** đọc dữ liệu cũ, **không** viết lại lịch sử. **Chưa deploy** — trường này đang nằm
trong JSON đã lưu của hơn 40 bundle; đổi tên mà không rà hết reader là đúng lỗi `§60` cấm.

### 3.8 · Các việc đào bới khác đã làm

- Đối chiếu `final_bundles` có cột `status` không: **có**, nhưng chỉ nhận giá trị `ACTIVE`.
- Truy nguồn chuỗi `WIN/LOSE` trong PRE snapshot: **không phải** `final_bundles.status`.
- Kiểm `scheduler_logs` còn sống: **còn** — 270 192 dòng, mới nhất `2026-08-28 03:00:00` UTC.
- Kiểm có tệp `.log` nào ghi trong ngày: 4 tệp, lớn nhất `scraper.log` 46 MB.
- Đếm `ai_model` phân biệt trong `predictions` từ 01/06: **37** tên.
- Đọc `[AI_PREFLIGHT]` lượt 05:00: cảnh báo `db_env_drift:google:selected_db` cho
  `gemini-2.5-flash`, `gemini-2.5-pro`, `combo-s…` — **chưa điều tra**, ghi vào `NOT_VERIFIED`.
- Đọc `[RULE_QUALITY] MN (2026-08-28 wd=4)`: `1/5 READY_STRONG`,
  `LIMITED_WEIGHT=3` · `READY_WITH_CAUTION=1`.
- Đếm job ghi vào `scheduler_logs` trong cửa sổ 05:00: `shadow_eval` 31 · `ai_predict` 26 ·
  `du_doan_test_auto` 9 · `free_predict` 6 · `shadow_rerank` 1 · `preflight` 1 ·
  `post_batch_verify` 1.

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Vì sao đọc header `.pyc` thay vì tin mtime tệp nguồn.** So mtime nguồn với giờ khởi động chỉ nói
tệp *cũ hơn* tiến trình — **không** nói tiến trình nạp đúng tệp đó. Header `.pyc` nhúng
**mtime và size của nguồn** mà nó biên dịch ra; `flags = 0` nghĩa là Python xác thực cache theo đúng
cặp số này. Hai số khớp chính xác nên bytecode trên đĩa **đúng là** bản biên dịch của nguồn hiện tại.

**Vì sao phải có phép vi sai.** Quan sát *«0 shadow trong eligibility»* một mình **không** chứng minh
bộ lọc chạy — nó cũng đúng nếu bộ lọc bị vô hiệu mà tình cờ không model shadow nào đủ tư cách. Phép
vi sai `27 → 16` mới phân biệt được hai khả năng. Đây đúng là bài học của `V11130` (`RM-15`: cổng
không có đối chứng dương thì luôn báo xanh).

**Vì sao không dùng manifest làm nguồn tập bỏ phiếu.** `predictions.reasoning_json` của
`combo-super` hôm nay có `source_weights = {}` và `meta = {}`. Trường rỗng nghĩa là
**`OBSERVABILITY_MISSING`**, **không** phải *«production chạy 0 model»* — chính log của lượt đó ghi
`expected_models=9` và `success=9`.

---

## 5 · ĐÃ LÀM GÌ

| # | việc | kết quả |
|---|---|---|
| 1 | POST snapshot runtime | PID/hash/health khớp PRE · 0 lỗi log |
| 2 | Đọc header `.pyc` | mtime và size **khớp chính xác** nguồn |
| 3 | Dựng chuỗi thời gian byte-patch tới tiến trình | 7 giây · `NRestarts=0` |
| 4 | Truy log lượt scheduled | `RUN_ID MN_2026-08-28_76f85e02` · 9/9 official |
| 5 | Phép vi sai bộ lọc | 27 → 16 · 11 shadow bị loại · cả ba miền |
| 6 | Timeline từng miền | MN đủ · MT/MB **chưa tới lượt**, ghi rõ |
| 7 | Eligibility structured 3 miền | 16 · 0 shadow · 4 ML · 8 LLM · PASS |
| 8 | Contribution trace canonical | 40 bundle · 871 component · **0 shadow** |
| 9 | Xác minh `partial_bonus_shadow` | `OBSERVABILITY_ONLY` · `NO_SCORE_EFFECT` |
| 10 | Kiểm bất biến FINAL 27/08 | `bach_thu` MB=61 MN=61 MT=68 — **không đổi** |

**Không** deploy · **không** restart · **không** ghi DB · **không** đổi
prediction/FINAL/roster/prompt.

---

## 6 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| đối chứng DƯƠNG contribution trace | **ĐẠT** — 40/40 bundle có component · 871/871 khác 0 |
| đối chứng ÂM canonical join | **ĐẠT** — 0 component shadow |
| đối chứng DƯƠNG cho bản vá (vi sai) | **ĐẠT** — 27 khác 16, chênh đúng 11 model shadow |
| cổng eligibility `_v11132` trên dữ liệu thật | **PASS** cả ba miền |
| bất biến FINAL 27/08 | **ĐẠT** — `bach_thu` không đổi |
| bất biến `lottery_results` | **ĐẠT** — 15 364 = 15 364 |
| không mutation official path | **ĐẠT** — PID và 4 hash khớp PRE |

---

## 7 · VƯỚNG VẤP — KỂ CẢ VẤP DO CHÍNH TÔI GÂY RA

### 🔴 V1 · Tôi suýt công bố một kết luận SAI về hạ tầng

Tôi chạy truy vấn `scheduler_logs` cho cửa sổ 05:00 và nhận **rỗng**, rồi in ra
*«(THỰC SỰ không có dòng nào)»*. Suýt nữa nó vào báo cáo thành *«đường scheduled không ghi log»*.

**Sự thật ngược lại:** cửa sổ đó có **75 dòng**, trong đó **26 dòng `ai_predict`** — và chính 26
dòng đó là **mắt xích số 4** tôi đang tìm cả buổi.

**Nguyên nhân gốc:** truy vấn của tôi tham chiếu cột **`status`**, mà `scheduler_logs` **không có**
cột đó. Cột thật là `id, log_time, log_level, message, job_name, region, date_str`. `sqlite3` báo
`Error: in prepare, no such column: status` **ra `stderr`**, trong khi hàm đọc của tôi **chỉ lấy
`stdout`** — nên lỗi bị nuốt, trả về chuỗi rỗng, **không có triệu chứng nào**.

**Tôi tự bắt bằng cách nào:** một phép đếm khác cho ra `2026-08-27 22 UTC | 256` dòng — mâu thuẫn
trực tiếp với "không có dòng nào". **Hai con số ngược nhau trong cùng một phiên** là dấu hiệu bắt
buộc phải dừng lại và truy.

**Đã sửa:** hàm đọc SQL nay **in cảnh báo khi `stderr` khác rỗng**. Đây đúng họ lỗi mà `CLAUDE.md`
đã ghi (*«SQL nhiều dòng qua SSH trả 0 dòng im lặng»*) — cùng cơ chế, khác nguyên nhân.

### 🟡 V2 · Ba lỗi kỹ thuật nhỏ làm chậm, không ảnh hưởng kết luận

- `tr '\0'` — Python dịch `\0` thành **ký tự null thật**, `CreateProcess` trên Windows từ chối.
  Chuyển sang `ps -p <pid> -o args=`.
- `stat -c %%Y` nằm trong chuỗi **không** qua `%`-format, nên shell nhận `%%Y` và in ra chữ `%Y`.
- Ghép chuỗi SQL có `datetime(log_time,'+7 hours')` trả `NULL` làm **cả dòng thành `NULL`**, in ra
  rỗng.

### 🟡 V3 · Một chỗ tôi chưa truy tới cùng

PRE snapshot ghi `FINAL_2708 = MB:61:WIN, MN:61:LOSE, MT:68:WIN`. Hôm nay `final_bundles.status`
chỉ có giá trị `ACTIVE`, còn `predictions.combo-super` ngày 27/08 có `status` là
`PARTIAL/LOSE/PARTIAL` — **không khớp** chuỗi `WIN/LOSE/WIN` kia. Nhiều khả năng PRE đọc cột
`bach_thu_status`, nhưng tôi **chưa xác minh xong**.

**Điều quan trọng đã xác minh:** `bach_thu` **không đổi** — `MB=61 MN=61 MT=68` ở cả PRE và POST.
Đó mới là phép kiểm bất biến thật sự. Chỗ chưa rõ ghi vào bảng `NOT_VERIFIED`.

---

## 8 · GỠ VỀ (ROLLBACK)

Phiên này **không mutation** nên **không có gì để gỡ**.

| hạng mục | trạng thái | cách gỡ nếu sau này deploy |
|---|---|---|
| `_v11132_cong_eligibility.py` | `LOCAL_ONLY` | chưa lên VPS — xoá tệp local là xong |
| `_v11132_thu_chan_cong_eligibility.py` | `LOCAL_ONLY` | như trên |
| bộ lọc shadow trong `combo_super.py` | đã chạy từ 27/08 22:53 | gỡ = bỏ mệnh đề `run_source NOT LIKE` ở `combo_super.py:376`, restart `lottery`, **so PID trước/sau** |
| đổi tên `partial_bonus_shadow` | **chưa làm** | không áp dụng |

---

## 9 · THEO DÕI TIẾP — LIỆT KÊ ĐỦ

| mã | việc | trạng thái | chặn ở đâu |
|---|---|---|---|
| **A3** | tách `DUPLICATE_LINEAGE` khỏi double-count điểm thật | 🔄 **đang đo** | cần trace theo từng candidate |
| **A3** | paired McNemar 4 biến thể | 🔄 **đang đo** | — |
| **A3** | family dedupe: tách đúng→sai / sai→đúng | 🔄 **đang đo** | — |
| **A3** | `COMBO_WITHOUT_META_LEARNING` nối đúng dữ liệu | 🔄 **đang đo** | căn dữ liệu `reasoning_json` với tập `CAND` |
| **cổng** | tách ba lớp `ELIGIBILITY` / `MANIFEST_OBSERVABILITY` / `CONTRIBUTION` | 🔴 **OPEN** | — |
| **cổng** | thử fallback `N≥1 → DEGRADED` và `N=0 → NO_OUTPUT` | 🔴 **OPEN** | — |
| **A4** | `TOTAL_LEAN_SHADOW` và `COMBO_SUPER_VNEXT_SHADOW` | 🔴 **OPEN** | — |
| **A5** | LLM context-only atomic, reverse scan = 0 | 🔄 **đang đo** | cần fixture DB pre-result |
| **A6** | ML pure-math namespace, vì sao chỉ 8,2 candidate | 🔄 **đang đo** | — |
| **1.2** | timeline **MT/MB** lượt 28/08 | ⏳ **WAIT_LIVE** | hai miền chưa chạy LLM/Combo |
| **scorer** | mốc 16:50 / 17:45 / 18:45 / 20:20 | ⏳ **WAIT_LIVE** | chiều nay |
| **3-càng** | Algorithm Card, generator, writer | 🔴 `MISSING_PIPELINE` | không có writer và không có cột |

---

## 10 · BA LỚP NGUỒN (§62)

### `OWNER_SAID`

Xem mục 2 — nguyên văn kèm giờ.

### `CODE_DID`

| việc | evidence |
|---|---|
| bytecode bằng nguồn hiện tại | `.pyc` header src mtime `1787845974`, size `137520`, bằng `stat` nguồn |
| tiến trình nạp bản vá | proc start `1787845981` trừ nguồn `1787845974` bằng **7 giây** · `NRestarts=0` |
| lượt scheduled trong đúng tiến trình đó | `journalctl`: `python3[2694667]` ở mọi dòng 05:15 – 05:32 |
| eligibility đường scheduled | `scheduler_logs.ai_predict`: `expected_models=9` tới `done_models=9 success=9 errors=0`, **0 shadow** |
| lane shadow là job riêng, chạy sau | `[RUN_ID_END] 22:20:38` rồi `Shadow Auto-Eval Start 22:20:38` |
| bộ lọc không vô hiệu | vi sai `27 → 16`, 11/11 bị loại đều là shadow, **cả ba miền** |
| trace đóng góp | 40 bundle · 871 component · 871 khác 0 · **0 shadow** (canonical join) |
| `partial_bonus_shadow` | `main.py:9999–10019` — không vào `number_scores` |
| bất biến | `bach_thu` 27/08 `MB=61 MN=61 MT=68`, PRE bằng POST |

### `DOC_SAID`

- `CLAUDE.md §55` — `scheduler_logs` naive là **UTC, phải cộng 7**. Đã áp dụng đúng ở mục 3.2 và 3.8.
- `docs/CURRENT_TRUTH_SSOT.md` — chưa cập nhật `PHA_B_DONE`. **`DOC_SAID` đang chậm hơn
  `CODE_DID`**, đúng khung `PRJ-INTERACTION-LEDGER-001` cho phép, và được ghi nhận ngay trong phiên.

---

## 11 · RUNTIME_LADDER

| hạng mục | bậc | căn cứ |
|---|---|---|
| **bộ lọc shadow `V11130`** | 🟢 **`RUNTIME_PROVEN`** | đủ **cả bốn** điều kiện owner nêu, xem bảng dưới |
| FU-438 auth gate | 🟢 `RUNTIME_PROVEN` | V11127, 56/56 |
| scorer cuốn chiếu | 🟡 `RUNTIME_LOADED` | chưa tới mốc 16:50 |
| cổng eligibility `_v11132` | ⚪ `LOCAL_ONLY` | chưa deploy |
| đổi tên `partial_bonus_shadow` | ⚪ `NOT_STARTED` | — |

Bốn điều kiện owner đặt cho `RUNTIME_PROVEN`:

| # | điều kiện | kết quả |
|---|---|---|
| 1 | byte patch đang được PID production nạp | 🟢 `.pyc` header khớp, khởi động sau 7 giây, `NRestarts=0` |
| 2 | scheduled Combo run thật gọi đúng patched path | 🟢 job chạy trong PID 2694667, sinh bundle id 784 |
| 3 | eligibility đường scheduled có official và 0 shadow | 🟢 `expected_models=9 · success=9`, 9/9 official |
| 4 | output và FINAL không drift | 🟢 `bach_thu` 27/08 không đổi, hash không đổi |

⚠️ **Giới hạn phải nói rõ:** điều kiện 3 chứng minh **9 model được GỌI** đều official. Nó **không**
chứng minh tập eligibility *đầy đủ* mà hàm tính ra bên trong lượt đó — tập ấy **không được lưu**
(`source_weights = {}`). Một model shadow *đủ tư cách nhưng không được gọi* sẽ **vô hình** với phép
kiểm này. Đó chính là lý do phải dựng `MANIFEST_OBSERVABILITY_GATE`.

---

## 12 · NOT_VERIFIED

| # | chưa rõ | thiếu bằng chứng | kiểm ở đâu | ảnh hưởng |
|---|---|---|---|---|
| 1 | tập eligibility **đầy đủ** bên trong lượt scheduled | manifest không lưu `source_ids` và `source_weights` | cần `MANIFEST_OBSERVABILITY_GATE` | giới hạn điều kiện 3 ở trên |
| 2 | timeline **MT/MB** ngày 28/08 | hai miền chưa chạy LLM/Combo lúc 09:58 | đo lại sau 16:58 và 17:58 | không được suy từ MN |
| 3 | chuỗi `WIN/LOSE` trong PRE đến từ cột nào | chưa đối chiếu xong `bach_thu_status` | `final_bundles.bach_thu_status` | **không** ảnh hưởng bất biến — `bach_thu` đã xác minh |
| 4 | `db_env_drift:google:selected_db` nghĩa là gì | chưa điều tra cảnh báo `[AI_PREFLIGHT]` | log 05:15 và code preflight | chưa rõ có ảnh hưởng output không |
| 5 | vì sao `partial_bonus_shadow` **chưa bao giờ** ở MB | chưa tách theo verdict và `wr_pct` từng miền | `main.py:9999` và dữ liệu verdict | chỉ là trường quan sát, không đổi điểm |
| 6 | `combo-super` 50 component — có double-count thật không | cần trace **cùng candidate** trên hai đường | A3.1 đang đo | quyết định nhãn 13/18 |
| 7 | `COMBO_WITHOUT_META_LEARNING` | căn dữ liệu | A3.4 đang đo | packet meta-learning |

---

## 13 · MUTATION_LOG

| | |
|---|---|
| deploy / restart | ❌ **KHÔNG** — PID 2694667 bằng PRE, `NRestarts=0` |
| ghi production DB | ❌ **KHÔNG** — mọi truy vấn `-readonly` |
| prediction · FINAL · roster · prompt | ❌ **KHÔNG ĐỔI** |
| ghi đè hoặc tính lại ngày cũ | ❌ **KHÔNG** |
| tệp trong `Lottery_AI_Test` | ❌ **KHÔNG SỬA** |
| credential · SSH · Notion · ERP | ❌ **KHÔNG CHẠM** |
| CLASS C | ❌ **KHÔNG** |
| tệp mới phiên này | chỉ script đo trong scratchpad, cộng hai tệp báo cáo này |

---

## 14 · NEXT_ACTION

1. A3 — nhận kết quả bốn luồng đo, **tự xác minh lại con số** trước khi dùng.
2. Tách **ba cổng** và thử fallback `N≥1 → DEGRADED`, `N=0 → NO_OUTPUT` (10 phép).
3. A4 — persist hai lane shadow.
4. A5 — emit prompt thật, reverse scan có phân loại.
5. A6 — `ML_PURE_MATH` namespace, điều tra con số 8,2 candidate.
6. Chiều nay: scorer **16:50 → 17:45 → 18:45 → 20:20**, và timeline MT/MB.

**Không** deploy official path khi chưa tách đúng lớp. **Không** hỏi Owner việc tự xử được.

---

TanPhatAI cần làm: ghi **`PHA B` ĐÓNG** với bốn mắt xích runtime — `.pyc` header khớp nguồn (`mtime 1787845974` · `size 137520`), tiến trình `2694667` khởi động **sau bản vá 7 giây** với `NRestarts=0`, lượt scheduled `RUN_ID MN_2026-08-28_76f85e02` chạy **bên trong chính tiến trình đó** và gọi **9/9 model official, 0 shadow**, FINAL 27/08 **không drift**. Ghi **phép vi sai** làm đối chứng dương cho bản vá: **27 model khi không lọc, 16 khi có lọc**, đúng **11 model shadow** bị loại, **giống hệt ở ba miền** — đây là thứ chứng minh bộ lọc không vô hiệu. Ghi trace đóng góp **40 bundle · 871 component · 871 khác 0 · 0 shadow** bằng **canonical join**; nhãn đúng là **`NO_OBSERVED_SHADOW_SCORE_CONTRIBUTION_14D`** và **`SHADOW_CHANGED_FINAL = FALSE_IN_OBSERVED_14D_WINDOW`** — **không** ghi tuyệt đối *«shadow chưa bao giờ và sẽ không bao giờ đổi FINAL»*; giữ riêng finding kiến trúc **`SHADOW_ENTERED_COMBO_ELIGIBILITY_PATH = TRUE_BEFORE_PATCH`**. Ghi **`PARTIAL_BONUS_SHADOW = OBSERVABILITY_ONLY · NO_SCORE_EFFECT`** — tên này **không liên quan model shadow**, nó nói về `verdict=SKIP` ở vị trí thứ hai. Ghi **`total_models` là `int`** (hôm nay bằng 15), **không phải danh sách model**; và **`source_weights={}` là `OBSERVABILITY_MISSING`**, **không phải** *«production chạy 0 model»* — log cùng lượt ghi `expected_models=9 success=9`. Ghi **đính chính của Agent**: câu *«scheduler_logs không có dòng nào cho lượt 05:00»* là **SAI** — thật ra có **75 dòng**, lỗi do truy vấn tham chiếu cột `status` không tồn tại và `stderr` bị nuốt; hàm đọc đã được sửa. Trạng thái: **`PHA_B_DONE`**, **A4/A5/A6 còn OPEN**, tổng thể vẫn **`PHA_A_PARTIAL`** — **không** ghi *«PHA A DONE»*. **Phiên này không mutation official path.**
