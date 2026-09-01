# REPORT V11150 — GRAND OVERHAUL · **WAVE 1** · 02/09/2026

> `ACTOR_RUNTIME = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**
> Trạng thái tổng: **`CODED_AND_TESTED_NOT_RUNTIME_PROVEN`**.
> **Không deploy · không restart · không ghi DB production.** `PID 3156545` không đổi ·
> health `200` · **558 FINAL hash `a82c508d3569abda…` KHÔNG DRIFT**.

---

## 1 · TÓM TẮT

Wave 1 làm ra **ba thành phần chạy được** — không phải schema nháp, không phải kế hoạch:

| | thành phần | bằng chứng |
|---|---|---|
| A | `UNIFIED_CANDIDATE_CONTRACT` | bộ thử **37/37** · **`E2E_PASS` trên dữ liệu production thật** |
| B | FULL EMITTER (gỡ chặn `FU-450`) | prompt thật **MN 49.329 · MT 47.164 · MB 48.473** · trùng khít `prediction_trace` |
| C | `LLM_CONTEXT_ONLY_V2` + `ML_PURE_MATH_V2` | contamination **0/3 miền** khi bật cờ · `ML_PURE_MATH_PASS` |

**Phát hiện nặng nhất:** `gpt_analyzer.py` **Phase 14A** đang bơm vào prompt của **mọi LLM**
một bảng xếp hạng model kèm trọng số, rồi đóng lại bằng mệnh lệnh *«AI nên ưu tiên patterns từ
models có `win_rate` cao hơn»*. Đây là **cơ chế trực tiếp** biến các LLM thành bản sao của
model dẫn đầu — và nó khớp với trọng số gần-phẳng đo được ở `V11149` (đỉnh chỉ hơn mức chia
đều **1,28×**).

**Phát hiện tốt bất ngờ:** tầng ML **vốn đã sạch**. Không model ML nào đọc tầng LLM/Combo, cả
bốn đều chặn ngày, và `lstm` trùng ba model kia chỉ **0,0–0,5%**.

---

## 2 · OWNER YÊU CẦU GÌ — nguyên văn

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI.** Đây là **mệnh lệnh trực tiếp của owner**,
> nói trong IDE, có hiệu lực ngay. Owner trao đổi liên tục nên **code thường đi trước tài liệu**
> — điều owner cho phép tường minh (`PRJ-INTERACTION-LEDGER-001`).

**02/09** — `PROMPT 43 R1 · CONTINUATION AFTER V11149 · EXECUTE WAVES 1–5`, 19 mục.
Trích **nguyên văn** các câu quyết định:

> *«Bắt đầu ngay tại WAVE 1. Không làm lại Phase 0. Không đo lại D-30. Không mở FU mới. Không
> mở Prompt 44. Không trả về một kế hoạch khác. Không hỏi Owner xác nhận. EXECUTE NOW.»*
>
> *«KHÔNG dừng ở phân tích, inventory, kế hoạch hoặc đề xuất. KHÔNG hỏi Owner giữa các Wave,
> ngoại trừ đúng bốn trường hợp: destructive schema/data; SSH/key/credential/access mutation;
> thay đổi không có rollback khả dụng; kích hoạt Grand Overhaul vào official production path.»*
>
> *«Không cắt bỏ TOTAL. Phải xây lại TOTAL thành bộ chọn nguồn và xếp hạng candidate mạnh hơn.»*
>
> **`V.1`** — *«Fail-closed với schema hỏng nhưng không được biến N≥1 thành NO_OUTPUT. N≥1 nguồn
> hợp lệ phải tạo DEGRADED output có cảnh báo. N=0 mới tạo explicit NO_OUTPUT.»*
>
> **`V.2`** — *«Không chấp nhận emitter tiếp tục bỏ 7.935 ký tự SYSTEM_PROMPT.»*
>
> **`V.3`** — *«Reverse scan các pattern ML/TOTAL/FINAL/model ranking. Kết quả phải bằng 0 trước
> khi gọi CONTEXT_ONLY_PASS.»*
>
> **`V.4`** — *«Không dùng LLM để lấp cho ML khi ML thiếu diversity. Phải điều tra nguyên nhân
> mathematical/feature/model khiến candidate pool ML co hẹp.»*
>
> **`V.5`** — *«Nếu mới code/test nhưng chưa runtime: `CODED_AND_TESTED_NOT_RUNTIME_PROVEN`.
> Không nói "đã deploy" nếu PID chưa nạp đúng imported path/hash.»*
>
> **`VII.2`** — *«Không hạ tiêu chuẩn chỉ để có phương pháp thắng.»*
>
> **`VIII`** — *«Chưa được gọi actual double-count chỉ từ tên nguồn.»*
>
> **`III`** — bốn retraction bắt buộc: «27 model cùng bỏ phiếu» SAI · «3,87×» SAI · «16 shadow
> rò rỉ» DƯƠNG TÍNH GIẢ · nhãn `NO_OBSERVED_DIRECT_SHADOW_VOTER_LEAK_IN_270_BUNDLES`.

**Đã tuân thủ đủ.** Không hỏi owner câu nào; không chạm bốn cổng.

---

## 3 · ĐÀO BỚI / PHÁT HIỆN — liệt kê ĐỦ, kể cả phép đo ra kết quả âm

### 3.1 Xác nhận lại baseline (bước 1 của mục `XIX`)

`558` bundle · hash **đầy đủ** `a82c508d3569abda47041ad625cca93fdec2227fbe389c395dc7f139893a0e5f`
— khớp neo `V11149`. `PID 3156545` · health `200`.

### 3.2 🔴 Ổ CONTAMINATION NẶNG NHẤT — `gpt_analyzer.py` Phase 14A

```python
prompt += f"\n🏆 HIỆU SUẤT THEO MODEL ({target_region}, 30 ngày):\n"
for model, stats in sorted(model_wr.items(), key=lambda x: x[1]['win_rate'], reverse=True):
    prompt += f"  {model}: {stats['win_rate']:.0f}% (...) — weight={stats['weight']:.2f}\n"
prompt += "  → AI nên ưu tiên patterns từ models có win_rate cao hơn.\n"
```

**TRƯỚC** (prompt MN thật, dòng 449–480):

```
🏆 HIỆU SUẤT THEO MODEL (MN, 30 ngày):
  claude-opus-4-6: 48% (8/30) — weight=0.04
  …
  gpt-5-mini: 27% (1/30) — weight=0.02
  → AI nên ưu tiên patterns từ models có win_rate cao hơn.
```

**Ba hệ quả**, đo được chứ không suy đoán:

1. **LLM thôi là nguồn độc lập.** Nó được bảo thẳng hãy bắt chước model dẫn đầu. Đưa nó và
   model đó cùng vào `TOTAL` rồi gọi là «hai nguồn đồng thuận» là **đếm một tiếng nói hai lần**.
2. **Vô hiệu hoá chính phép de-herding `V10768`.** Phép đó công phu gỡ bảng WR/BT khỏi
   *context pack* (**−1.102** ký tự ở MN) — nhưng bảng này nằm ở *user payload*, nơi phép gỡ
   **không với tới**. Gỡ một cửa để mở cửa kia ⇒ `A58_VIOLATION_HALF_DONE` (§60.1).
3. **Dạy herding ngay cạnh câu cấm herding.** Vài nghìn ký tự sau, `RULEBOOK` viết *«CONV×3
   tails có win rate THẤP HƠN average trong herding scenarios»* ⇒ `PRJ_PROMPT_CONTRADICTS`.

Cùng họ: **Phase 11** bơm win-rate miền + `✅ SỐ ĐÃ TRÚNG GẦN ĐÂY` — **chính output cũ của hệ
bơm ngược vào đầu vào**.

### 3.3 Emitter cũ hụt ở đâu — và con số `7.935` của `FU-450` là ĐO THẬT

| | MN | MT | MB |
|---|---|---|---|
| cổng cũ `_v11107._prompt_day_du` | 33.836 | 33.675 | 36.408 |
| **emitter mới** (8 mảnh) | **49.329** | **47.164** | **48.473** |

Cổng cũ hụt vì **bỏ `REASONING_RULEBOOK` (15.256 ký tự)** và dùng sàn `ctx > 50` thay vì
`CTX_PACK_SAN = 500` (`V11032` đã nâng).

**Kiểm chéo runtime:** `prediction_trace` ghi `context_pack_chars` MN = **11.294**; emitter đo
**11.294** — **trùng khít**. Chênh `prompt_total_chars` MT vs emitter cũ = **7.922**, tức con số
**7.935** của `FU-450` **là phép đo thật**, không phải nhầm lẫn.

**Phát hiện phụ:** `SYSTEM_SERVED` **cùng độ dài nhưng KHÁC hash** với `SYSTEM_BASE` —
production chạy ngưỡng `≥8`/`<6` (rules `confirm=8`, `skip=6`) còn endpoint trả bản `≥7`/`<4`.
Một emitter chỉ dump hằng module **không bao giờ thấy** chênh này.

### 3.4 🟢 `ML_PURE_MATH_V2` — kết quả TỐT HƠN dự đoán

`ML_PURE_MATH_PASS`:

- **Không** model ML nào import `gpt_analyzer` / `combo_super` / `ensemble_voting` (quét phụ
  thuộc **bắc cầu**, không chỉ import trực tiếp — §60.2);
- **cả bốn đều chặn ngày** `< target_date`: `meta_predict.py` · `lstm_predict.py:160` (lối
  **Python**) · `statistical_analyzer.py:71` qua `run_full_analysis()`;
- `include_same_day_cross` mặc định `False`, production **không** truyền (chỉ sandbox A/B
  `_v10801_*` bật).

**Herding đo THẲNG** — không mượn `VIF` của thước khác (`RM-21`), 93 ngày-miền:

| cặp | trùng | | cặp | trùng |
|---|---|---|---|---|
| `lstm` × `meta-learning` | **0,0%** | | `meta` × `xgboost` | 21,5% |
| `lstm` × `xgboost` | **0,0%** | | `rf` × `xgboost` | 21,0% |
| `lstm` × `random-forest` | **0,5%** | | `meta` × `rf` | 17,7% |

**Không có sụp đổ đa dạng ở tầng ML.** `lstm` độc lập thật.

### 3.5 Phép đo ra kết quả ÂM / không kết luận được — ghi đủ

- **`predictions` đọc được qua `database.py`** cho `meta-learning`/`xgboost`/`random-forest`.
  Đây là tầng tiện ích **dùng chung cả kho**, không phải model tự đọc. **CHƯA chứng minh** ML có
  dùng làm đặc trưng hay không ⇒ để `NOT_VERIFIED`, không kết luận.
- **`gpt_analyzer.py:5620`** — chuỗi **báo lỗi** anti-trap không nằm sau cờ. Chỉ bơm khi hàm
  ném; phép quét runtime hôm nay cho **0**, tức nó không kích hoạt. Ghi nhận, chưa xử.
- **Cổng mồ côi** vẫn `CHẶN` 1 câu (`📊 KNOWLEDGE BASE` — `SYSTEM_PROMPT:56` trỏ vào khối
  không tồn tại ở miền nào). **Có từ trước bản này**, không phải do Wave 1 gây ra.
- **Artifact local 144,6 ngày** — phép đo này **SAI về production**: VPS train lại **30/08**
  (2 ngày). Xem mục 7.

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Vì sao đặt `LLM_CONTEXT_ONLY_V2` sau một cờ, mặc định TẮT.** Owner khoá *«Shadow chưa được
tác động current official TOTAL/FINAL trước cutover policy»* (`IV.9`) và *«chỉ hỏi Owner khi
bật vào official»* (`XV.D`). Cờ cho phép mã **có mặt, chạy được, đo được ngay** ở đường
challenger mà official vẫn nguyên **từng ký tự**. Gỡ về = đổi đúng một cờ, **không cần deploy
lại**.

**Vì sao KHÔNG nới mẫu cổng contamination cho hết báo động.** Sáu chỗ khớp đầu tiên, đọc nguyên
văn thì **4 là dương tính giả** (mục 7). Owner cấm *«hạ tiêu chuẩn chỉ để có phương pháp
thắng»* (`VII.2`). Nên làm mẫu **SẮC HƠN** thay vì lỏng hơn: `win-rate` phải có **phạm vi
model**; `override` phải là **kết quả** (một số cụ thể đã bị thay) chứ không phải **phương
pháp**. Kèm **4 phép phân định ranh giới**, mỗi phép một cặp *phải-qua / phải-chặn*, để lần sau
ai nới mẫu thì **vế phải-chặn gãy ngay**.

**Vì sao bảng mới thay vì `ALTER` bảng cũ.** Additive thuần: `unified_candidate_sets` không
đụng bảng nào đang có; gỡ về là `DROP` đúng nó. `FINAL` cũ **bất biến** (`X`).

**Vì sao chạy `_sync_live_forensic_inputs.py`.** DB local chỉ có 7 dòng cho ngày-miền và
**không có `final_bundle`** — E2E trên đó sẽ là bằng chứng rỗng. Đây là lối chính `CLAUDE.md`
quy định trước mọi việc audit dùng bản local.

---

## 5 · ĐÃ LÀM GÌ — trước / sau / phiên bản / kiểm (§60.4)

### A · `UNIFIED_CANDIDATE_CONTRACT` — `_v11150_unified_candidate_contract.py` (MỚI)

**TRƯỚC:** ba hình dạng output rời nhau, không tầng nào ghi được nguồn gốc của tầng trên:
`predictions.main_numbers` = `"34,72,09"` (chuỗi phẳng, **không rank không điểm**) ·
`final_bundles…ranked_numbers` = `[{number,score,voters}]` · `model_bt`/`model_wr` = chẩn đoán.

**SAU:** một hợp đồng `UCC-1.0.0`, từ vựng **đóng**, ứng viên có `rank` + `raw_score` +
`normalized_confidence`, và **lineage bắt buộc** — `ENSEMBLE`/`HYBRID` không khai
`parent_source_ids` ⇒ `INVALID`.

**KIỂM:** `python web/backend/_v11150_test_contract.py` → **37/37 ĐẠT**
(positive · negative · empty · malformed · duplicate · late · idempotency · tất định ·
tương thích ngược).

### B · FULL EMITTER — `_v11150_full_emitter.py` (MỚI)

**TRƯỚC:** `_v11107._prompt_day_du` ghép `system + thân + ctx`, **bỏ `REASONING_RULEBOOK`**.
**SAU:** tám mảnh, mỗi mảnh có hash riêng, dump từ **hàm đang phục vụ** với **rules thật 17
khoá** và **`source_data` thật**. `tu_kiem()` đối chiếu ngược vào mã `_call_anthropic` ⇒ emitter
**không thể lặng lẽ dump bản cũ**.

**KIỂM:** `python web/backend/_v11150_full_emitter.py --tat-ca` → MN 49.329 · MT 47.164 ·
MB 48.473 · `✓ tự kiểm`.

### C · `LLM_CONTEXT_ONLY_V2` — `gpt_analyzer.py` (SỬA, sau cờ)

**TRƯỚC:** Phase 14A + Phase 11 bơm vô điều kiện.
**SAU:** cả hai nằm sau `LLM_CONTEXT_ONLY_V2_ENABLED` (`os.getenv`, **mặc định `0`**).
**PHIÊN BẢN:** `gpt_analyzer.py` `4fc988bd2c23d22c` → local mới (VPS **chưa nhận**).

**KIỂM — hai chế độ, ba miền:**

| | cờ TẮT (official hiện hành) | cờ BẬT |
|---|---|---|
| MN | `CONTEXT_ONLY_FAIL` · **28 chỗ** | **`PASS` · 0** · 49.329→48.048 |
| MT | `FAIL` | **`PASS` · 0** · 47.164→45.853 |
| MB | `FAIL` | **`PASS` · 0** · 48.473→47.162 |

`RUNTIME_EMITTED = 0` cả ba miền. **META 17/17.**

### D · `ML_PURE_MATH_V2` AUDIT — `_v11150_ml_pure_math_audit.py` (MỚI)

**KIỂM:** `ML_PURE_MATH_PASS` — chi tiết mục 3.4.

### E · E2E TRÊN DỮ LIỆU PRODUCTION — `_v11150_e2e_contract.py` (MỚI)

**KIỂM:** `E2E_PASS` — 27 `predictions` chuyển đủ **0 lỗi** · `final_bundle` → **10 ứng viên,
13 nguồn cha**, top-1 số `34` `raw_score 0,1224` evidence `[gpt-oss-120b, glm-5.1,
gemini-2.5-pro]` · ghi-đọc-lại **khớp hash** · ghi lần hai đẻ **0** dòng.
Phân bố lớp: `LLM_BASE 19` · `ML_BASE 4` · `ENSEMBLE 2` · `HYBRID 2`.

### F · Cổng chỉ-đọc của chính agent — vá

**TRƯỚC:** mẫu `\bUPDATE\b` / `>` trần khớp vào **mã Python** (`h.update(...)`) và **toán tử
SQL** (`date >= …`), chặn nhầm **ba lần**.
**SAU:** neo vào cú pháp đầy đủ (`UPDATE … SET`, `INSERT INTO`, chuyển hướng shell).
**KIỂM (RM-15 hai chiều):** `rm -f` → **CHẶN** · `SELECT COUNT(*)` → **558** · `h.update()` → **qua**.

---

## 6 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| `_v11150_test_contract.py` | ✅ **37/37** |
| `_v11150_contamination_gate.py --meta` | ✅ **17/17** |
| `_v11150_contamination_gate.py --tat-ca` (cờ BẬT) | ✅ **`CONTEXT_ONLY_PASS` × 3 miền** |
| `_v11150_ml_pure_math_audit.py` | ✅ **`ML_PURE_MATH_PASS`** |
| `_v11150_e2e_contract.py` | ✅ **`E2E_PASS`** trên dữ liệu production |
| `_v11044_cong_so_hieu.py` | ✅ `SO_HIEU_V11044=KHỚP` |
| `_v11062_nang_version.py --kiem` | ✅ `ĐẠT` — bốn mặt · `governance_seq 466` |
| `_v11107_cong_prompt_mo_coi.py` | 🟡 `CHẶN` 1 câu — **có từ trước**, không xấu đi |
| **neo no-drift 558 FINAL** | ✅ `a82c508d3569abda…` **KHÔNG DRIFT** |

---

## 7 · VƯỚNG VẤP — bốn lần tự báo sai rồi tự sửa

**① Bộ thử bắt một mâu thuẫn trong chính thiết kế hợp đồng.** `source_snapshot_at` vừa bị liệt
là **bắt buộc-có-giá-trị** vừa được xử như *«thiếu thì cảnh báo»*. Hậu quả: **mọi artifact cũ
đều `INVALID`** ⇒ đường replay chết từ dòng đầu, phá đúng `V.1` khoản 9. Tách hai hạng
`BAT_BUOC_CO_GIA_TRI` / `BAT_BUOC_CO_KHOA`.

**② Cổng contamination báo 6 chỗ — đọc nguyên văn thì 4 là DƯƠNG TÍNH GIẢ.**
*«CONV×3 herding scenarios có win rate THẤP HƠN average»* là câu **chống** herding nói về một
**lớp mẫu hình**, không phải thành tích model. *«Anti-trap chỉ là lớp an toàn sau khi đã xác
định đúng quy luật»* là mô tả **thứ tự làm việc**. **Gỡ cả sáu thì đã làm hỏng đúng thứ cần
giữ** (`RM-09`).

**③ Bộ audit ML báo `lstm` «chưa chứng minh chặn ngày» — SAI.** `lstm_predict.py:160` chặn
bằng **Python** (`[d for d in all_dates if d < target_date]`), bộ dò chỉ tìm cú pháp SQL. Cùng
lỗi cho `ml_predict` — chặn nằm ở `statistical_analyzer.py:71` **một tầng dưới**.

**④ Bộ audit báo artifact ML **144,6 ngày** — SAI VỀ PRODUCTION.** Đó là bản **local**. VPS
train lại **30/08** — **2 ngày tuổi**. `RM-13`: local cũ **không** chứng minh production cũ. Nếu
công bố thì đã báo owner một sự cố *«ML 5 tháng không train»* **không có thật**.

**⑤ `\n` trong heredoc thành xuống dòng thật — lần thứ tư trong dự án.** Bỏ hẳn lối viết Python
có escape qua heredoc bash; dùng công cụ ghi tệp.

---

## 8 · GỠ VỀ

| thành phần | gỡ về |
|---|---|
| `LLM_CONTEXT_ONLY_V2` | đặt `LLM_CONTEXT_ONLY_V2=0` (**đã là mặc định**) — không cần deploy |
| bảng `unified_candidate_sets` | `DROP INDEX ×3; DROP TABLE unified_candidate_sets;` (hằng `UCC.ROLLBACK`, có phép thử chứng minh **không đụng** `final_bundles`) |
| `gpt_analyzer.py` | `git revert e9a0ca9` — VPS **chưa nhận** bản này |
| tệp mới (`_v11150_*`) | xoá; **không tệp nào được production import** |

**Không có gì cần gỡ trên production** — phiên này không deploy.

---

## 9 · THEO DÕI TIẾP — liệt kê ĐỦ, kèm ai chặn và chặn ở đâu

| # | việc | trạng thái | chặn ở đâu |
|---|---|---|---|
| 1 | **LLM tự sinh ranked top-K đúng hợp đồng** | ⚪ chưa | cần adapter output LLM → `UCC`; Wave 1 mục còn lại |
| 2 | `predictions` qua `database.py` — ML có dùng làm đặc trưng? | 🟡 `NOT_VERIFIED` | cần truy `extract_prediction_features` |
| 3 | `gpt_analyzer.py:5620` chuỗi báo lỗi anti-trap ngoài cờ | 🟡 tồn dư nhẹ | chỉ bơm khi ném; runtime hôm nay **0** |
| 4 | Cổng mồ côi `📊 KNOWLEDGE BASE` | 🟡 `CHẶN` | có từ trước; `_knowledge_base.json` không tồn tại |
| 5 | **`DOUBLE_COUNT`** — `combo-super`/`smart-ensemble`/`smart-ml` trong voters FINAL | 🔴 `PARENT_LINEAGE_PENDING` | **Wave 3** — cần `parent_output_hashes`, chưa chứng minh |
| 6 | `ALL_MODEL_ARENA` — 57 → 27 → 18, và **9 runtime-active không vào voters** | ⚪ Wave 2 | tiếp ngay sau bản này |
| 7 | `TOTAL_V2` / `COMBO_V2` / `FINAL_V2` | ⚪ Wave 3 | — |
| 8 | Replay out-of-time + canary | ⚪ Wave 4 | — |
| 9 | **Cutover Packet** — một lần duy nhất | ⚪ Wave 5 | cần owner ký (`XV.D`) |
| 10 | D-30 `PRE_LOCK_GENERATOR` + reconciliation | ⚪ bảo trì | **không** chặn Grand Overhaul (`XIII`) |
| 11 | 26 stale reader · 38 lane nghỉ hưu | ⚪ hàng bảo trì | song song |
| 12 | `FU-447` (16 báo cáo) · `FU-444` (22 báo cáo thiếu) | ⚪ bảo trì quản trị | không ngắt Wave |
| 13 | Bảo mật / SSH / world-writable | ⚪ hàng `CLASS C` riêng | **cần owner** — không tự mutation |

---

## §62 — BA LỚP NGUỒN

### `OWNER_SAID` (nguyên văn + giờ)

| giờ (VN) | nguyên văn | loại |
|---|---|---|
| 02/09 ~00:00 | *«Bắt đầu ngay tại WAVE 1… Không hỏi Owner xác nhận. EXECUTE NOW.»* | `YÊU_CẦU` |
| 02/09 ~00:00 | *«Không hạ tiêu chuẩn chỉ để có phương pháp thắng.»* | `YÊU_CẦU` |
| 02/09 ~00:00 | *«Chưa được gọi actual double-count chỉ từ tên nguồn.»* | `YÊU_CẦU` |
| 02/09 ~00:00 | *«Không chấp nhận emitter tiếp tục bỏ 7.935 ký tự SYSTEM_PROMPT.»* | `YÊU_CẦU` |

### `CODE_DID` (evidence: tệp:dòng · lệnh · hash)

- `gpt_analyzer.py:872` cờ `LLM_CONTEXT_ONLY_V2_ENABLED` · `:2842` Phase 11 · `:2874` Phase 14A
- `_v11150_test_contract.py` → **37/37** · `_v11150_contamination_gate.py --meta` → **17/17**
- `_v11150_full_emitter.py --tat-ca` → 49.329 / 47.164 / 48.473
- `_v11150_ml_pure_math_audit.py` → `ML_PURE_MATH_PASS`
- `_v11150_e2e_contract.py` → `E2E_PASS`
- **558 FINAL** `a82c508d3569abda47041ad625cca93fdec2227fbe389c395dc7f139893a0e5f` — không drift
- `PID 3156545` · health `200` — **không restart**
- commit riêng `e9a0ca9` + `6330ddf`

### `DOC_SAID`

- `docs/FOLLOW_UP_TRACKER.md` `FU-450` mục 2 — *«emitter thiếu 16,4% (7.935 ký tự)»* ⇒
  **XÁC NHẬN là đo thật** (chênh MT = 7.922). `FU-450` mục 2 nay **ĐÓNG**.
- `docs/CURRENT_TRUTH_SSOT.md` — *«prompt ngữ cảnh thuần: chưa từng lên production, chưa đo
  gì — kẹt ở emitter»* ⇒ **hết kẹt**; nhưng *«chưa lên production»* **vẫn đúng** (cờ mặc định TẮT).
- `CLAUDE.md` §55 mốc khoá MN 15:45 · MT 16:58 · MB 17:58 ⇒ **khớp** `UCC.REGION_LOCK_HHMM`,
  có phép thử.

### `NOT_VERIFIED`

`predictions` qua `database.py` · `gpt_analyzer.py:5620` · lineage `parent_output_hashes` của
hybrid/ensemble · nguyên nhân 9 nguồn runtime-active không vào voters.

### Ba lớp lệch nhau ⇒ FINDING

**`DOC_SAID` ≠ `CODE_DID`:** tài liệu ghi *«emitter thiếu `SYSTEM_PROMPT`»*. Đo lại thì emitter
cũ **có** `SYSTEM_PROMPT` — thứ nó bỏ là **`REASONING_RULEBOOK` (15.256 ký tự)**. Con số tổng
đúng, **quy sai mảnh**. Đã sửa ở `FOLLOW_UP_TRACKER`.

---

TanPhatAI cần làm: ghi **Grand Overhaul WAVE 1 xong phần lớn** — `V11150`, riêng `e9a0ca9` + `6330ddf`, trạng thái **`CODED_AND_TESTED_NOT_RUNTIME_PROVEN`**, **không deploy, không restart**. Ghi **`FU-450` mục 2 ĐÓNG** — emitter đã vá, và con số `7.935` được **xác nhận là đo thật** (chênh MT `7.922`); nhưng **sửa quy kết**: thứ emitter cũ bỏ là **`REASONING_RULEBOOK` 15.256 ký tự**, không phải `SYSTEM_PROMPT`. Ghi **ổ contamination `gpt_analyzer` Phase 14A** — bảng xếp hạng model + trọng số + mệnh lệnh bắt chước model dẫn đầu, bơm vào prompt **mọi LLM**; nó **vô hiệu hoá phép de-herding `V10768`** (`A58_VIOLATION_HALF_DONE`) và **mâu thuẫn** với `RULEBOOK` (`PRJ_PROMPT_CONTRADICTS`). Ghi **`LLM_CONTEXT_ONLY_V2` đạt `CONTEXT_ONLY_PASS` cả ba miền** khi bật cờ, **mặc định TẮT** nên official chưa đổi. Ghi **`ML_PURE_MATH_PASS`** — tầng ML vốn đã sạch, `lstm` trùng model khác **0,0–0,5%**. Ghi **`DOUBLE_COUNT_RISK` xác nhận có mặt, CHƯA chứng minh** — Wave 3. Ghi **558 FINAL không drift**. **Không mở FU mới** — umbrella `FU-449`/`FU-450`. **Không mở Prompt 44.**
