# V10782 — RE-PREDICT MN TRƯỚC LIVE + FREEZE 55' + METHOD LOCK + (P3–P5 PENDING)

- **Ngày:** 2026-07-05 (Asia/Ho_Chi_Minh) · **Owner:** TanPhatERP · **Trạng thái:** PHẦN 0–2 DONE (một phần) · P3–P6 PENDING
- **Chính sách báo cáo:** §52G GitHub-first — đây là bản gốc chi tiết
- **Artifacts VPS:** `/root/Lottery_AI_Test/artifacts/v10782_p0/`, `v10782_p1a/`

---

## 0. TÓM TẮT EXECUTIVE

| Phần | Trạng thái | Ghi chú |
|---|---|---|
| **P0 Re-predict MN** | **DONE ✔** (ổn định 15:38, trước deadline 15:40) | Owner-approved exception hash MN 05/07 |
| **P1A Đo thực trạng 55'** | **DONE ✔** | 7 ngày evidence; 0 bundle đổi sau mốc |
| **P1B Freeze + late=1** | **DEPLOYED VPS ✔** | Code local chưa push private GitHub |
| **P2 Method lock minh bạch** | **PARTIAL ✔** | Seed tuần 06/07 + audit script; UI /choi chưa in lock |
| **P3 Lịch sử UI** | PENDING | |
| **P4 Tra soát trùng lặp** | PENDING | |
| **P5 Google thinking** | PENDING | |
| **P6 Verify full + Notion** | THIS REPORT (partial) | |

---

## PHẦN 0 — RE-PREDICT TOÀN BỘ MN 05/07 (KHẨN, OWNER DUYỆT)

### 0.1 Snapshot bản ~04:00 (đối chứng, KHÔNG xóa lịch sử)

- **Artifact:** `artifacts/v10782_p0/snapshot_0400_MN_2026-07-05.json` (15:14 VN)
- **Rows:** 25 predictions MN + 1 final_bundle
- **PRE final_bundle bạch thủ:** **87**
- **PRE hash 4 bảng (toàn DB):** predictions `5e92c59e…` · final_bundles `1bef9c34…` · lottery_results `2076e8f7…` · model_daily_eval `cbd1f568…`

Rotation semantics: mỗi model giữ row cũ; `pre_result_numbers` ← số 04:00, `main_numbers` ← số mới (lịch sử đo không mất).

### 0.2 Re-run timeline (15:15–15:38 VN)

| Giai đoạn | Thời gian | Cơ chế |
|---|---|---|
| ML/free | ~15:15 | `_run_smart_ensemble`, `_run_smart_ml_ensemble`, `_run_combo_no_token`, 4 ML free models |
| Official AI chain | ~15:16–15:22 | `_run_ai_models_predict('MN', run_source='auto_daily')` → log `/tmp/v10782_ai.log` |
| Shadow lane | ~15:15–15:37 (~21.5 phút) | `_run_shadow_auto_eval('MN')` → log `/tmp/v10782_shadow.log` |
| Apply + bundle | **15:38:57** | `_v10782_p0_apply.py` — 15 model applied, 3 skipped (đã fresh) |

**Shadow timeline (model cuối):** qwen3-max-thinking 15:37:14 → `['71','17']` str=8.0

**Skipped (đã fresh trước apply):** kimi-k2.5 (15:28:39), glm-5.2 (15:28:40), qwen3.7-max (15:30:20)

### 0.3 Deadline

- **Nội bộ 15:40:** PASS — apply xong 15:38:57
- **Mốc chơi MN 15:55:** không re-run sau mốc (freeze P1B active sau deploy)

### 0.4 Diff 04:00 vs bản mới

| Câu hỏi | Kết quả |
|---|---|
| **(a) 3 đài CN đúng?** | **✔** Tiền Giang / Kiên Giang / Đà Lạt — log AI×8 + shadow×10 mỗi đài (`p04_diff_report` fix_evidence) |
| **(b) FIX-1 nhãn nguồn?** | **✔ trong prompt runtime** (log); `custom_prompt` trace 15h không lưu đủ text → **FU: bổ sung logging trace** |
| **(c) reasoning tokens >0?** | **CHƯA XÁC MINH ĐƯỢC** qua DB — `reasoning_json` EMPTY cho qwen3-max-thinking, grok-4.20-multi-agent, gpt-5.5, qwen3.7-max, glm-5.2, kimi-k2.5; trace 15h `reasoning_tokens=None`. Calls đã chạy (15:21–15:37). **Verify lại 06/07 run thật** |
| **(d) BT/total đổi?** | **✔ Official BT 87 → 71**; lo2 `["71","96"]`; lo3 `571`; model_count 15; consensus strong. Nhiều model official đổi số (deepseek-reasoner 85/58→71/17, gemini-flash 73/87→15/71, …) |
| **(e) kimi rớt row?** | **✔ KHÔNG** — row mới `["57","71"]` lúc 15:28 (trước đây mất row do latency >90s) |

**Models đổi số chính (official path):**

| Model | 04:00 | Sau re-predict |
|---|---|---|
| deepseek-reasoner | 85, 58 | 71, 17 |
| gemini-2.5-flash | 73, 87 | 15, 71 |
| claude-sonnet-4-6 | 78, 71 | 71, 17 |
| gpt-5-mini | 73, 87 | 87, 71 |
| final_bundle BT | **87** | **71** |

**POST hash (sau P0, 16:14 refresh):** predictions `8fb485648944` · final_bundles `9be2264ac911` · lottery_results `f4a8bd4bcefa` · model_daily_eval `c382a7354655`

**Ngoại lệ hash 6.1:** chỉ predictions + final_bundles MN 05/07 thay đổi có chủ đích; lottery_results/model_daily_eval chỉ tăng tự nhiên nếu có scrape/verify.

### 0.5 /choi MN hôm nay (CN 05/07) — KHÔNG áp E5

- Tuần hiện hành **29/06** → method **`MN_ADAPTIVE_EXPLOIT_V1`** (daily_lock 09:44, songthu `["65","79"]`)
- Tuần **06/07** đã seed lock `MN_BT1_OFFICIAL_V1` (16:12) — hiệu lực từ T2 07/07 ✔

### 0.6 MT/MB

- **KHÔNG re-predict** đợt này ✔

---

## PHẦN 1 — DAO ĐỘNG QUA MỐC 55'

### 1A — Đo thực trạng (READ-ONLY, 7 ngày 29/06→05/07)

**Artifact:** `artifacts/v10782_p1a/p1a_evidence.json`

| Metric | Kết quả |
|---|---|
| Bundle regen sau mốc 55' | **0 / 21** ngày-miền |
| BT đổi sau mốc 55' | **0** |
| Card lưu sau mốc | **1** — MT 29/06: 4 shadow_auto_eval rows sau 16:55 |
| Latency p95 nổi bật | deepseek-reasoner **114.6s**; claude-sonnet **64.7s**; gemini-flash max **240.6s** |

**Kết luận 1A:** vấn đề chính là **model về trễ + card shadow lưu sau mốc** (1 case/7 ngày), chưa thấy bundle BT đổi sau 55' trong cửa sổ đo.

### 1B — Freeze design + deploy

**Module:** `web/backend/_v10782_freeze.py`

| Mốc | Giờ VN |
|---|---|
| MN | 15:55 |
| MT | 16:55 |
| MB | 17:55 |

**Semantics:**
- Sau mốc: CẤM overwrite prediction row đã có; model mới → INSERT `late=1` (measure-only)
- final_bundles: CẤM overwrite; create-only nếu chưa có
- Single-flight total: regen chỉ end-of-chain + T-10 jobs (15:45/16:45/17:45)
- Hợp nhất late-fill kimi → nhánh `late=1` (thay thiết kế riêng 14/07)

**Hooks:** `database.py` (save_prediction), `scheduler.py` (shadow/materialize), `main.py` (generate_final_bundle)

**VPS:** deployed + smoke OK; MN 05/07 frozen sau 15:55

**Rollback:** `FREEZE_ENABLED=False` + restart

**Chưa làm:** push private GitHub (170 dòng local uncommitted)

---

## PHẦN 2 — /choi METHOD LOCK (PARTIAL)

### 2.1–2.2 Chuẩn + bảng lock

- Bảng **`money_board_lock`** = method_week_lock chính thức (immutable INSERT OR IGNORE)
- Cột mới: `owner_decision_ref`, `published_at`

### 2.3 Seed tuần 06/07 (ký trước 00:00 T2)

| Miền | Method | Quyết định |
|---|---|---|
| MN | `MN_BT1_OFFICIAL_V1` | E5: BT 1-số official bạch-thủ + NGHỈ T7 |
| MT | `MT_ADAPTIVE_EXPLOIT_V1` | V66 cap top-13 |
| MB | `MB_ADAPTIVE_EXPLOIT_V1` | V67 + exploit |

**Locked:** 2026-07-05T16:12:26+07:00 · ref `V10780-E5 + V10782-P2.3`

### 2.4 Audit hồi tố

- Script: `_v10782_p2_seed_audit.py` (2a week lock giữa tuần, 2b daily lock sau giờ xổ, 2c/2d log mismatch)
- **UI /choi in method lock:** PENDING (P2 còn lại)

---

## PHẦN 3–5 — PENDING (chưa thực thi)

| Phần | Nội dung chờ |
|---|---|
| **P3** | Filter lịch sử trên bảng hiện có (miền/model/lane/method/7–56 ngày, phân trang server-side) — không tạo bảng mới |
| **P4** | Ma trận mục đích→surface; bảng GIỮ/HỢP NHẤT/ĐỀ XUẤT BỎ chờ ký |
| **P5** | Audit Gemini config + lane shadow thinking mới (first_run 06/07) + bảng TRẠNG THÁI tồn đọng |
| **P6** | Hash POST từng phần sau P1B deploy; báo cáo bổ sung 06/07 |

---

## PHẦN 6 — VERIFY + HASH

| Bảng | PRE (V10781 baseline) | POST P0 MN | Ghi chú |
|---|---|---|---|
| predictions | `5e92c59e…` | `8fb485648944…` | **EXPECTED** — MN 05/07 re-predict |
| final_bundles | `1bef9c34…` | `9be2264ac911…` | **EXPECTED** — BT 87→71 |
| lottery_results | `2076e8f7…` | `f4a8bd4bcefa…` | natural growth |
| model_daily_eval | `cbd1f568…` | `c382a7354655…` | natural growth |

**Smoke:** /api/health 200 · MN frozen post-15:55 ✔

---

## BLOCKERS / FU

1. **reasoning_tokens logging gap** — verify 06/07 first-run
2. **P1B code** — commit + push private repo
3. **P3–P5** — owner priority order sau báo cáo này
4. **Checkpoint 14/07** — gộp từ V10781 FU + freeze live verify + Google gate

---

## ARTIFACT INDEX

| Path | Mô tả |
|---|---|
| `artifacts/v10782_p0/snapshot_0400_MN_2026-07-05.json` | Snapshot PRE re-predict |
| `artifacts/v10782_p0/apply_log_2026-07-05.json` | 15 applied + 3 skipped |
| `artifacts/v10782_p0/p04_diff_report_2026-07-05.json` | Diff + fix evidence |
| `artifacts/v10782_p1a/p1a_evidence.json` | 7-day 55' measurement |
| `/tmp/v10782_ai.log`, `/tmp/v10782_shadow.log` | Runtime logs re-predict |

**Scripts:** `_v10782_p0_repredict_mn.py`, `_v10782_p0_apply.py`, `_v10782_p1a_measure.py`, `_v10782_freeze.py`, `_v10782_p2_seed_audit.py`
