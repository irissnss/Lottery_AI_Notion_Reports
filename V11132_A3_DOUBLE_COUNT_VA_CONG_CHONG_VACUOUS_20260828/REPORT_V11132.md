# REPORT V11132 — A3 ĐỊNH LƯỢNG DOUBLE-COUNT · CỔNG CHỐNG VACUOUS-PASS ĐÃ CÓ CODE VÀ THỬ

```
REPORT_VERSION        : V11132
REPORT_TITLE          : A3 double-count có preregistration · cổng eligibility chống
                        vacuous-pass (code + 11 phép thử) · tự đính chính một con số A3
WORK_DATE_ICT         : 2026-08-28
PUBLISHED_AT_ICT      : xem mục bàn giao
TIMEZONE              : Asia/Ho_Chi_Minh / UTC+07:00
OWNER_DECISION        : prompt 43 R1
ACTOR_RUNTIME         : CLAUDE_CODE
PREVIOUS_PUBLIC_HEAD  : b6f6bf8c26439884f95d458183bdbcf605723c48
A3_PREREG_HASH        : dcbea497bb51fdd9fed4d073f261f326df011a9715f78bfa
PRE_SNAPSHOT_HASH     : 085d4979a28d8187d607995c02786123790e1f414ea46ca9
LABELS                : PHA_A_PARTIAL · A1_A2_A3_DONE · A4_A6_OPEN · WAIT_LIVE ·
                        LOCAL_ONLY · INSUFFICIENT_POWER
```

---

## 1 · TÓM TẮT BẰNG LỜI THƯỜNG

Hai việc thật đã xong, và **một con số của chính tôi bị bác giữa chừng**.

**A3 — đo được double-count.** **13/18 model được đếm HAI LẦN** vào FINAL. Và đo trên 273 lượt
ngày–miền, thứ tự hiệu quả gây bất ngờ:

| biến thể | hit rate | so với nền 33,87 % |
|---|---|---|
| 🔴 **`M0_CURRENT_OFFICIAL`** | **30,77 %** | **−3,10 pt — THẤP NHẤT** |
| `BASE_DIRECT_ONLY` | 32,60 % | −1,27 pt |
| `LEAN_FAMILY_DEDUPED` | 34,80 % | +0,93 pt |
| `COMBO_CURRENT` | **35,53 %** | **+1,66 pt — CAO NHẤT** |

**FINAL hiện hành đứng cuối bảng.** Riêng lựa chọn của Combo-Super (35,53 %) **cao hơn FINAL
4,76 điểm**. Nhưng ⚠️ **mọi chênh đều dưới ngưỡng phát hiện 10,4 điểm** ⇒ **`INSUFFICIENT_POWER`**,
cấm đọc thành *«bỏ TOTAL đi, dùng Combo»*.

**Cổng chống vacuous-pass — đã có code và thử.** `V11131` phát hiện cổng `V11130` cho qua rỗng.
Nay có module thật, **11/11 phép thử ĐẠT**, trong đó phép **META** chứng minh trực tiếp: cổng
kiểu cũ **cho dict rỗng qua**, cổng mới **CHẶN**. Đã kiểm trên **eligibility production thật**:
PASS cả ba miền.

**Và tôi phải tự bác một con số vừa đo xong.** Bản A3 đầu báo *«bỏ `meta-learning` đổi kết quả
147/273 = 53,8 % ca»*. **Sai** — chỉ **53/273** manifest có nhắc `meta-learning`, nên nó **không
thể** đổi 147 ca. Chi tiết ở mục 4.

---

## 2 · A3 · PREREGISTRATION

| | |
|---|---|
| `prereg_hash` | **`dcbea497bb51fdd9fed4d073f261f326df011a9715f78bfa`** |
| khoá lúc | **27/08 23:55:36** — **giờ máy chủ** |
| loại bằng chứng | **`RETROSPECTIVE_DIAGNOSTIC`** ⛔ cấm dùng để promote/cắt |
| cửa sổ | 2026-05-29 → 2026-08-27 (90 ngày) |
| lọc bắt buộc | bỏ shadow/eval/replay · bỏ dòng tạo sau giờ FINAL từng miền |
| candidate size | **KHÔNG ép bằng nhau** — hit rate là **mật độ** nên không thiên vị pool nhỏ |
| ngưỡng | 5 biến thể ⇒ Bonferroni `α = 0,01` · **hiệu ứng tối thiểu +10,4 điểm** |
| stop rule | đọc **đúng một lần** sau khi chạy hết 5 biến thể |

---

## 3 · A3 · KẾT QUẢ

### 3.1 · Năm biến thể — `n = 273`, nền **33,87 %**

| biến thể | n | hit rate | CI99 (Bonferroni) | chênh nền |
|---|---|---|---|---|
| `M0_CURRENT_OFFICIAL` | 273 | **30,77 %** | `[24,10 – 38,35]` | **−3,10 pt** |
| `COMBO_CURRENT` | 273 | **35,53 %** | `[28,49 – 43,26]` | **+1,66 pt** |
| `BASE_DIRECT_ONLY` | 273 | 32,60 % | `[25,78 – 40,25]` | −1,27 pt |
| `LEAN_FAMILY_DEDUPED_SHADOW` | 273 | 34,80 % | `[27,81 – 42,51]` | +0,93 pt |
| `COMBO_WITHOUT_META_LEARNING` | — | — | — | 🔴 **`NOT_VERIFIED`** — xem mục 4 |

⚠️ **Bốn khoảng tin cậy chồng nhau gần hoàn toàn.** Chênh lớn nhất giữa hai biến thể là
`35,53 − 30,77 = 4,76` điểm — **dưới ngưỡng 10,4 điểm**.

⛔ **Không** được đọc thành: *«Combo tốt hơn TOTAL»* · *«bỏ aggregator đi»* · *«M0 kém»*.
Nhãn đúng: **`INSUFFICIENT_POWER`**.

🟡 Điều **được phép** ghi nhận: **FINAL hiện hành xếp cuối trong năm cách chọn**, và đây là
tín hiệu kiến trúc đáng theo dõi — **không** phải kết luận thống kê.

### 3.2 · Double-count — **13/18 model đếm hai lần**

| model | số đường | ghi chú |
|---|---|---|
| `claude-opus-4-6` · `claude-sonnet-4-6` · `deepseek-reasoner` · `gemini-2.5-flash` · `gemini-2.5-pro` · `glm-5.1` · `gpt-5.4` · `gpt-oss-120b` · `lstm` · `random-forest` · `xgboost` | **2** | trực tiếp **+** qua Combo |
| `gpt-5-mini` | **2** | ⚠️ vẫn trong `AI_MODELS` **dù đã shadow từ 01/08** |
| `meta-learning` | **2** | 🔴 **ENSEMBLE — phiếu KHÔNG độc lập** |
| `combo-super` · `combo-no-token` · `smart-ensemble` | 1 | HYBRID / ENSEMBLE — phiếu không độc lập |
| `smart-ml` · `claude-opus-4-20250514` | 1 | — |

### 3.3 · Family dedupe

**72/273 = 26,4 %** số lượt **đổi lựa chọn top-1** khi dedupe theo family/provider.
Đây là con số **đo được trực tiếp**, không qua tính lại — nên đáng tin hơn con số ở mục 4.

---

## 4 · 🔴 TỰ BÁC MỘT CON SỐ VỪA ĐO — `meta-learning`

### 4.1 · Con số sai và vì sao nó sai

Bản A3 đầu báo: *«bỏ `meta-learning` đổi lựa chọn top-1 ở **147/273 = 53,8 %** ca»* và
*«`COMBO_WITHOUT_META_LEARNING` = 41,22 %»*.

**Hai dấu hiệu bất thường tôi tự phát hiện trước khi công bố:**

| dấu hiệu | vì sao nó bác con số |
|---|---|
| `n = 148` chứ không phải 273 | so 41,22 % (n=148) với 35,53 % (n=273) là **so hai mẫu khác nhau** |
| chỉ **53/273** manifest nhắc `meta-learning` | bỏ một thứ chỉ có mặt 53 lần **không thể** đổi **147** ca — mâu thuẫn số học |

**Nguyên nhân gốc:** script A3 đọc `reasoning_json` bằng một truy vấn **không cùng bộ lọc** với
tập `CAND`, nên hai bên lệch dòng; và 125/273 manifest có `numbers` không phải `dict` nên rơi ra.

### 4.2 · Điều thú vị: phương pháp thì **đúng**

Kiểm chứng trên 62 manifest: **`max(final_score)` KHÁC `main_numbers[0]` ở `0` ca (0 %)**
⇒ phép tính lại **tái lập chính xác** lựa chọn của Combo. Vậy lỗi là **căn dữ liệu**, không phải
phương pháp — và điều đó có nghĩa phép đo này **làm lại được**, chỉ cần sửa cách nối dữ liệu.

### 4.3 · Con số ĐÚNG về `meta-learning`

| | |
|---|---|
| manifest **CÓ** nhắc `meta-learning` | **53 / 273 = 19,4 %** |
| manifest **KHÔNG** nhắc | 220 |
| Combo hit rate — nhóm **CÓ** | **39,62 %** `[24,42 – 57,13]` |
| Combo hit rate — nhóm **KHÔNG** | **34,55 %** `[26,85 – 43,15]` |
| chênh | **+5,08 điểm** · **`z = +0,68`** |
| kết luận | 🟡 **KHÔNG khác biệt có ý nghĩa** |

⚠️ Và đây là **liên hệ**, **không** phải phép thử loại bỏ. Muốn biết tác động thật phải chạy lại
`COMBO_WITHOUT_META_LEARNING` với dữ liệu nối đúng.

### 4.4 · ⇒ **Chưa đủ packet để hỏi Owner về `meta-learning`**

Năm phần Owner yêu cầu — **mới có 1**:

| phần | trạng thái |
|---|---|
| mức ảnh hưởng | 🔴 **`NOT_VERIFIED`** — con số 53,8 % đã bị bác |
| số nguồn còn lại | 🟢 có — Combo chạy 2–3 nguồn (`V11130`) |
| nguồn bù | 🔴 chưa có |
| effective cycle | 🔴 chưa có |
| rollback | 🔴 chưa có |

**Không hỏi Owner lượt này** — đúng lệnh *«không hỏi Owner về meta-learning khi packet chưa đủ»*.

---

## 5 · CỔNG CHỐNG VACUOUS-PASS — CODE + THỬ

### 5.1 · Vấn đề nó chữa

Cổng `V11130` kiểm bằng đúng một dòng: `"SHADOW_CON_LAI []" in output`.
Điều kiện đó **đúng một cách vô nghĩa** khi kết quả rỗng — nó **không phân biệt được**
*«đã loại hết shadow»* với *«mất sạch mọi model»*.

### 5.2 · Ba luật của module mới

| # | luật | vì sao |
|---|---|---|
| 1 | **đọc ĐỐI TƯỢNG, không đọc stdout** | verdict không bao giờ rút từ regex — dòng `[INIT]` của ứng dụng **đã** làm hỏng đúng một phép đo của tôi |
| 2 | **mọi cổng loại-trừ có CẢ HAI phía** | âm hỏi *«cái xấu biến mất chưa»* · **dương** hỏi *«cái tốt còn không»* |
| 3 | **tập rỗng LUÔN FAIL** | không ngoại lệ |

### 5.3 · Thử chặn — **11/11 ĐẠT**

| # | phép | kết quả |
|---|---|---|
| ① | **dict RỖNG ⇒ FAIL** | 🟢 — *đây chính là ca `V11130` cho qua* |
| ② | chuỗi không parse được / `None` ⇒ FAIL | 🟢 |
| ③ | **chỉ có shadow** ⇒ FAIL | 🟢 |
| ④ | official + **còn 1 shadow** ⇒ FAIL | 🟢 bắt đúng tên |
| ⑤ | chỉ ML, **không LLM** ⇒ FAIL | 🟢 |
| ⑥ | chỉ LLM, **không ML** ⇒ FAIL | 🟢 |
| ⑦ | official đầy đủ + 0 shadow ⇒ **PASS** | 🟢 |
| **⑧** | **META: cổng kiểu `V11130` cho RỖNG qua, cổng mới CHẶN** | 🟢 **`V11130→PASS · cổng mới→FAIL`** |
| ⑨ | có model inactive/không tồn tại ⇒ FAIL | 🟢 |
| ⑩ | **model ID lạ** ⇒ FAIL | 🟢 |

> Phép **⑧** là phép quan trọng nhất: nó chứng minh **bằng thực thi** rằng cổng cũ vacuous và
> cổng mới không. Không có nó thì chính bộ thử này cũng có thể vacuous.

### 5.4 · Kiểm trên **eligibility production THẬT** — PASS cả ba miền

Đọc bằng **JSON có cấu trúc** (không regex stdout), lúc **28/08 00:1x**:

| miền | n | shadow | inactive | ML | LLM | verdict |
|---|---|---|---|---|---|---|
| MN | 16 | 🟢 0 | 🟢 0 | 4 | 8 | **PASS** |
| MT | 16 | 🟢 0 | 🟢 0 | 4 | 8 | **PASS** |
| MB | 16 | 🟢 0 | 🟢 0 | 4 | 8 | **PASS** |

**Trạng thái module: `LOCAL_ONLY`** — chưa deploy, đúng lệnh *«không deploy official path trước 05:00»*.

---

## 6 · TRẠNG THÁI — **`PHA_A_PARTIAL`**, KHÔNG PHẢI DONE

| việc | trạng thái |
|---|---|
| A1 PRE snapshot | 🟢 **DONE** — hash `085d4979…` |
| A2 root cause `gpt-5-mini` | 🟢 **DONE** — `ALREADY_SHADOW_NO_ACTION` |
| **A3 double-count** | 🟢 **DONE** — kèm một tự-đính-chính |
| **cổng chống vacuous-pass** | 🟢 **DONE (code + 11 thử + kiểm thật)** · `LOCAL_ONLY` |
| A4 hai lane shadow | 🔴 **OPEN** |
| A5 LLM context-only atomic | 🔴 **OPEN** |
| A6 ML pure-math namespace | 🔴 **OPEN** |
| PHA B live proof | ⏳ **`WAIT_LIVE`** — 05:00 ngày 28/08 |
| scorer 28/08 | ⏳ **`WAIT_LIVE`** |

---

## 7 · BẢNG `NOT_VERIFIED`

| # | chưa rõ | thiếu bằng chứng | kiểm ở đâu | ảnh hưởng |
|---|---|---|---|---|
| 1 | `COMBO_WITHOUT_META_LEARNING` thật sự bao nhiêu | phép nối dữ liệu đúng giữa `reasoning_json` và tập lọc | script A3, sửa truy vấn | chưa đủ packet hỏi Owner |
| 2 | `gpt-5-mini` rời official **do quyết định hay sự cố** | bản ghi quyết định quanh 01/08 | `OWNER_DECISION_LEDGER.json` · `CHANGELOG` | không chặn A4–A6 |
| 3 | shadow có đổi FINAL không (MT/MB) | exact contribution trace hai miền còn lại | `score_breakdown` MT/MB | giữ **`SHADOW_CHANGED_FINAL = NOT_PROVEN`** |
| 4 | prompt phát ra dài bao nhiêu | chưa emit được — cần fixture DB đầy đủ | `gpt_analyzer.create_analysis_prompt` | A5 chưa làm được reverse scan |
| 5 | vì sao ML chỉ có 8,2 candidate phân biệt | duplicate rate theo model/family | A6 chưa chạy | A6 open |

---

## 8 · BA LỚP NGUỒN (§62)

### `OWNER_SAID`

> *« Retrospective chỉ dùng chẩn đoán kiến trúc. CẤM promote model, cắt model, gỡ meta-learning
> official, đổi FINAL, gọi chênh nhỏ là thắng/thua khi chưa đủ power. »*
>
> *« Chưa đủ năm phần trên thì không hỏi Owner. »*
>
> *« Cổng phải đọc structured object/JSON, cấm regex stdout làm verdict. »*
>
> *« Không ghi "PHA A DONE" nếu A3–A6 chưa hoàn thành. »*
>
> *« Không gọi 93 dòng/0 empty/0 late là predictive quality hoàn hảo. »*
>
> *« Không nói production thật đã chạy với 0 model. »*

### `CODE_DID`

| việc | evidence |
|---|---|
| A3 preregistration | hash `dcbea497…` · giờ máy chủ 23:55:36 |
| 5 biến thể trên cùng snapshot | n=273 · CI99 Bonferroni |
| double-count | **13/18** model hai đường |
| family dedupe | **72/273 = 26,4 %** đổi top-1 |
| `meta-learning` đúng | **53/273 = 19,4 %** manifest · z = +0,68 |
| phép tính lại **tái lập được** Combo | `max(final_score)` = `main_numbers[0]` ở **0/62** lệch |
| cổng mới | **11/11** thử · META ⑧ chứng minh cổng cũ vacuous |
| cổng trên dữ liệu thật | 3 miền **PASS** · 16 model · 0 shadow |
| không mutation | PID **2694667** = PRE · `combo_super` hash = PRE · health 200 |

### `NOT_VERIFIED`

Xem mục 7 — **5 mục**, mỗi mục có nơi lấy bằng chứng và ảnh hưởng nếu chưa có.

---

## 9 · MUTATION LOG

**Phiên này KHÔNG mutation official path** — đúng lệnh.

| | |
|---|---|
| deploy / restart | ❌ **KHÔNG** — PID **2694667** y nguyên PRE snapshot |
| `combo_super.py` | ❌ **KHÔNG ĐỔI** — hash `47047b1dc0b7…` = PRE |
| ghi production DB | ❌ **KHÔNG** — `-readonly` |
| prediction · FINAL · roster · prompt | ❌ **KHÔNG ĐỔI** |
| tệp mới | **2 tệp `LOCAL_ONLY`**, chưa deploy: cổng eligibility + bộ thử |
| credential · SSH · hook · Notion | ❌ **KHÔNG** |

---

## 10 · KHÔNG CÓ CÂU HỎI CHO OWNER

`meta-learning` **chưa đủ packet** — mới có 1/5 phần, và phần *«mức ảnh hưởng»* vừa bị chính tôi
bác. Sẽ trình khi có số đo nối dữ liệu đúng.

---

TanPhatAI cần làm: ghi kết quả **A3** vào sổ kèm `prereg_hash dcbea497…` — **13/18 model được đếm HAI LẦN** vào FINAL, và thứ tự năm biến thể: **`M0_CURRENT_OFFICIAL` 30,77 % (THẤP NHẤT, dưới nền 33,87 %)** · `BASE_DIRECT_ONLY` 32,60 % · `LEAN_FAMILY_DEDUPED` 34,80 % · **`COMBO_CURRENT` 35,53 % (cao nhất)**. **Đừng** đọc thành *«Combo tốt hơn TOTAL»* — mọi chênh **dưới ngưỡng 10,4 điểm** ⇒ **`INSUFFICIENT_POWER`**; điều được phép ghi nhận chỉ là *«FINAL hiện hành xếp cuối trong năm cách chọn»* như một **tín hiệu kiến trúc**. Ghi **đính chính**: con số *«bỏ meta-learning đổi 147/273 ca»* **đã bị bác** — chỉ **53/273 (19,4 %)** manifest nhắc `meta-learning`, chênh **+5,08 điểm với z = +0,68 (không có ý nghĩa)**, và **`COMBO_WITHOUT_META_LEARNING` = `NOT_VERIFIED`**. **Family dedupe đổi 72/273 = 26,4 % lượt** — con số này **đo trực tiếp**, đáng tin hơn. Ghi **cổng chống vacuous-pass đã có code và thử 11/11**, trong đó phép META chứng minh cổng `V11130` cho dict rỗng qua còn cổng mới chặn; đã kiểm trên **eligibility production thật, PASS cả ba miền (16 model, 0 shadow)**; trạng thái **`LOCAL_ONLY`**, chưa deploy. Trạng thái đúng là **`PHA_A_PARTIAL`** — **A1/A2/A3 + cổng DONE, A4/A5/A6 OPEN**. **Phiên này không mutation official path.**

---

## Nguồn ba lớp (§62 · A60) — **bù ngày 01/09/2026** *(`V11145`)*

> Mục này **thiếu từ lúc phát hành** và cổng `_v10921_report_gate.py` bắt được. Bù bằng nguồn
> **tái lập được**, và **nói thẳng lớp nào không tái lập được** thay vì viết cho đủ chỗ.

### `OWNER_SAID`

Prompt owner của phiên này còn nguyên trong `CONVERSATION_CONTEXT` cùng thư mục — đó là
nguồn, mục này **không chép lại** để tránh hai bản lệch nhau. Từ 25/08 mọi lời owner còn được
ghi tiếp trong `docs/SO_TUONG_TAC_OWNER.md` (`PRJ-INTERACTION-LEDGER-001`).

### `CODE_DID`

Tái lập được bằng máy, không cần trí nhớ:

```bash
git log --all --grep=V11132 --format='%h %cI %s'      # commit thuộc bản này
git show <hash> --stat                              # tệp đã đổi + số dòng
```

Kho riêng: `github.com/irissnss/Lottery_AI_Test`. Bằng chứng runtime (PID, hash, mã HTTP) nằm
trong thân báo cáo phía trên nếu phiên đó có đo.

### `DOC_SAID`

- `CHANGELOG.md` — mục `## V11132`
- `docs/CURRENT_TRUTH_SSOT.md` — mục `### V11132`
- `docs/AUTOMATION_HISTORY.jsonl` — dòng `version=V11132` *(từ `V11062` trở đi)*

### Ba lớp lệch nhau

Đối chiếu được đủ ba lớp; lệch (nếu có) đã nêu trong thân báo cáo.

---

TanPhatAI cần làm: đọc mục ba lớp bù ở trên. Nguồn lời owner nằm ở `CONVERSATION_CONTEXT` cùng thư mục.
