# V10778 — PHASE A AUDIT: R1 NAMEFIX + SWAP + RETIRE (PLAN-20260705-V10777-R1SWAP-NAMEFIX-RETIRE)

- Ngày: 2026-07-05 (02:18–03:00 VN)
- Loại: PHASE A — PLAN ONLY (audit + kế hoạch, CHƯA sửa runtime; chờ owner chốt R2 rồi mới Phase B)
- Plan ID (immutable, do owner cấp): PLAN-20260705-V10777-R1SWAP-NAMEFIX-RETIRE
- Ghi chú version: prompt owner ghi V10777 nhưng V10777 đã được dùng cho phiên "MN BT 1-số" (seq 232, cùng đêm).
  Owner chốt: "linh động báo cáo version tiếp theo có ghi chú chạy cho prompt nào" → delivery này = V10778, thực thi Plan ID trên.
- Trạng thái cuối phiên: PHASE A HOÀN TẤT + 4/5 quyết định đã chốt. CHỜ owner chốt câu R2 (chọn model thay thế) trước khi sang Phase B.

## 1. BỐI CẢNH & YÊU CẦU CỦA OWNER (prompt HARD ENFORCEMENT)

Owner giao 4 nhiệm vụ + verify, two-phase commit (Phase A plan-only → owner duyệt → Phase B implement):

- R1 — FIX NAMING BUG: `deepseek-reasoner` bị hiển thị nhầm nhãn "DeepSeek R1" trên UI/labels.
  deepseek-reasoner và DeepSeek-R1 là 2 model KHÁC NHAU; R1 chưa từng chạy trong hệ thống.
- R2 — SWAP: retire `deepseek-v4-flash` (P&L 56d = −72.6M, owner OK tại V10776) và thêm model mới
  "deepseek-r1" tier SHADOW_AUTO, không backfill, first_run_date rõ ràng, smoke API trước khi gắn scheduler.
- R3 — RETIRE CP-66.9 (adaptive-exploit MN): owner chốt nguyên văn "chưa làm hệ thống tốt lên...
  không có giá trị thì không cần phải nâng cấp gì cả, từ bỏ." Flag off, không xóa file, quét xung đột /choi lock.
- R4 — CẮT 4 SHADOW MODEL ÂM (owner OK tại V10776): qwen3-coder (−118.2M), gemini-3-flash (−52.1M),
  gemini-3.1-pro (−41.5M), qwen3.6-plus (−33.9M). Tổng 5 model (gồm v4-flash) ≈ 45% chi phí token shadow.
- R5 — VERIFY TỔNG LỰC: hash-guard 4 bảng official PRE=POST, smoke, registry check, scheduler dry-check,
  naming grep = 0, ngày mai verify first_run row của model mới.

Acceptance lock: 4 bảng official không đổi; /du-doan, /choi lock tuần 29/06, scheduler main flow không đổi;
V10752 MT cap, V10766/V10767/V10770 không đổi; deepseek-reasoner model_id + API call không đổi (chỉ sửa nhãn);
shadow lanes checkpoint 14/07 chạy tiếp bình thường.

## 2. KẾT QUẢ PHASE A — 5 MÂU THUẪN PHÁT HIỆN (báo ngay theo blocking rule)

### Mâu thuẫn 1 — Version V10777 đã bị chiếm
- Phiên 02:04–02:17 cùng đêm đã ship V10777 = MN BT 1-số (FU-V10777-MN-BT, seq 232, backups/v10777_pre/ đã tồn tại).
- Owner chốt: dùng version kế tiếp V10778 + ghi chú thực thi Plan ID gốc. Backup Phase B sẽ là backups/v10778_pre/.

### Mâu thuẫn 2 — BLOCKER R2: `deepseek-r1` KHÔNG tồn tại trên API DeepSeek trực tiếp (docs 07/2026)
- Docs chính thức api-docs.deepseek.com/quick_start/pricing (07/2026): platform chỉ còn 2 model id
  `deepseek-v4-flash` ($0.14 in / $0.28 out per 1M) và `deepseek-v4-pro` ($0.435 / $0.87, promo từ $1.74/$3.48).
- KHÔNG có id `deepseek-r1`. Premise "cùng provider deepseek, cùng endpoint/key" của R2 không khả thi.
- DeepSeek-R1 thật (2025) chỉ còn gọi được qua aggregator: OpenRouter `deepseek/deepseek-r1` ($0.70/$2.50)
  hoặc `deepseek/deepseek-r1-0528` ($0.50/$2.15). Theo blocking rule "không xác định được giá → DỪNG hỏi",
  em dừng và trình phương án (mục 6).

### Mâu thuẫn 3 — CRITICAL PL-1: alias DeepSeek bị khai tử 24/07/2026 15:59 UTC
- Docs chính thức: `deepseek-chat` và `deepseek-reasoner` chỉ còn là alias tương thích, TỰ ĐỘNG trỏ về
  V4-Flash (non-thinking / thinking) từ khi V4 ra (~24/04/2026), và bị TẮT HẲN sau 24/07/2026.
- Ảnh hưởng hệ mình (3 chỗ):
  1) Model ACTIVE official `deepseek-reasoner` gọi API bằng chính alias sắp chết → sau 24/07 mọi call lỗi, ảnh hưởng /du-doan.
  2) `deepseek-v4-pro` (shadow) đang map qua alias `deepseek-reasoner` → thực chất là V4-Flash-thinking, KHÔNG phải V4 Pro thật.
  3) `deepseek-v4-flash` (shadow) map qua alias `deepseek-chat` → V4-Flash non-thinking (con này sắp retire nên hết ảnh hưởng).
- Vì acceptance lock ghi "deepseek-reasoner: API call KHÔNG ĐỔI", em KHÔNG đụng trong plan này.
  PL-1 đã append vào Plan Ledger: owner cần 1 quyết định riêng TRƯỚC 24/07 (đổi API call sang id tường minh
  `deepseek-v4-flash` + thinking mode, giữ nguyên model_id + lineage → track record liền mạch).

### Mâu thuẫn 4 — "SELECT ... FROM registry" và cột `active` không tồn tại
- Registry là FILE CODE `web/backend/model_registry.py` (list MODEL_REGISTRY), không phải bảng DB
  (đã quét sqlite_master: không có bảng registry model). Không có field `active`; chỉ có `status`
  (ACTIVE | SHADOW_AUTO | REGISTERED | REMOVED).
- Owner chốt: thêm enum mới `RETIRED` + `retire_reason` + `retired_date` trong dict; update guard
  `get_output_eligible_ids` loại thêm RETIRED; R5.3 xuất bảng text từ MODEL_REGISTRY thay vì SQL.

### Mâu thuẫn 5 — R5.3 kỳ vọng "v4-pro ACTIVE"
- Thực tế `deepseek-v4-pro` = SHADOW_AUTO (từ V10750-restore), không phải ACTIVE. Em sẽ báo đúng thực tế; không đổi status v4-pro trong plan này.

## 3. A1 — KẾT QUẢ QUÉT NAMING BUG (text-proof)

DB proof (read-only):
- SELECT DISTINCT ai_model FROM predictions WHERE LOWER(ai_model) LIKE '%r1%' → KHÔNG CÓ.
- SELECT DISTINCT ai_model FROM model_daily_eval WHERE LOWER(ai_model) LIKE '%r1%' → KHÔNG CÓ.
- Kết luận: model_id trong DB nhất quán `deepseek-reasoner`; "R1 chưa từng chạy" ĐÚNG.

12 vị trí LIVE gán nhãn sai "DeepSeek R1" cho model_id `deepseek-reasoner` (sẽ sửa ở Phase B, B2):

| # | File:Line | Nội dung hiện tại |
|---|---|---|
| 1 | web/backend/model_registry.py:108 | 'label': 'DeepSeek R1' |
| 2 | web/backend/combo_super.py:74 | {'id': 'deepseek-reasoner', 'label': 'DeepSeek R1', ...} |
| 3 | web/frontend/app.js:443 | 'deepseek-reasoner': '🔬 DeepSeek R1' |
| 4 | web/frontend/app.js:483 | 'deepseek-reasoner': 'DeepSeek R1' |
| 5 | web/frontend/user-view.js:17 | 'deepseek-reasoner': 'DeepSeek R1' |
| 6 | web/frontend/index.html:63 | option "🔬 DeepSeek R1 ⭐⭐⭐⭐" |
| 7 | web/frontend/index.html:447 | option "DeepSeek R1" |
| 8 | web/frontend/user-view.html:512 | option "🔬 DeepSeek R1" |
| 9 | web/frontend/settings.html:1158 | option "🔬 DeepSeek R1" |
| 10 | web/frontend/accuracy.html:280 | option "DeepSeek R1" |
| 11 | web/frontend/viewer.html:551 | option "DeepSeek R1" |
| 12 | web/backend/gpt_analyzer.py:5,183,3273,3277,3304,3305,3333 | comment/docstring/log string "DeepSeek R1" (KHÔNG đụng logic is_reasoner — line 3290 là model_id) |

2 vị trí docs LỊCH SỬ: docs/SANDBOX_GOVERNANCE.md:268 + docs/PHASE1_CHANGELOG.md (~8 dòng thời v7.9.x).
Owner chốt: GIỮ NGUYÊN lịch sử + thêm 1 dòng ERRATUM đầu file (không phá audit trail).

## 4. A2 — DEPENDENCY SCAN (6 mục bắt buộc — đủ)

1. model_registry + pricing: derived sets tự tính khi import — SHADOW_AUTO_EVAL_MODELS = get_model_ids(status='SHADOW_AUTO')
   (model_registry.py:720) → flip status là model tự rút khỏi scheduler, KHÔNG cần sửa scheduler.py.
   Pricing _provider_pricing_table.py: deepseek-reasoner 0.0014 / v4-flash 0.0007 / v4-pro 0.0014 (blended per 1k).
2. scheduler.py: _run_shadow_auto_eval (line 6970) import SHADOW_AUTO_EVAL_MODELS mỗi lần chạy; anti-dup theo
   run_source='shadow_auto_eval'; preflight _preflight_check_provider_runtime (line 2230) phân loại provider
   theo prefix (deepseek-* → package openai — hợp lệ cho cả route OpenRouter). Cost log: model_latency_cost_audit_daily.
3. UI: bảng model chính = tab models v87 Master Index (monitoring.html:5143-5156) đọc registry qua API → status mới
   tự hiển thị; cần thêm màu RETIRED (line 5152). Dropdowns tĩnh 6 file HTML (danh sách A1).
   Nhóm "ĐÃ NGHỈ": deepseek-chat không nằm trong registry (EOL V7.9.12, chỉ còn history DB) — 5 model cắt sẽ hiện
   pill RETIRED đỏ trong tab models.
4. API endpoints model list/labels: _v87_master_board.py (đọc registry), combo_super.py MODEL list, dropdowns tĩnh. Không chỗ nào khác hardcode nhãn sai ngoài A1.
5. CP-66.9 references: roadmap docs/ACTIVE_ROADMAP_LAG1_ADAPTIVE_EXPLOIT.md (CP-66.9 OVERDUE ~26 ngày, CP-66.10 LOCKED_ON);
   scheduler cron V66 23:35 + V67 23:40 (chạy CẢ 3 MIỀN); pool /choi main.py:700-713 TEST_LANE_CHALLENGER_PREFERENCE_BY_REGION
   (MN_ADAPTIVE_EXPLOIT_V1 đứng đầu pool MN); panel watch main.py:13557 _build_adaptive_exploit_watch.
6. Model lineage (V10751): database.py:3144 MODEL_LINEAGE — model mới là id mới chưa từng chạy → không cần lineage entry
   (mốc lịch sử = first_run_date); retire giữ nguyên id trong registry → lineage không đứt.

## 5. A4 — CP-66.9 vs /choi LOCK: CÓ XUNG ĐỘT (evidence DB, sau live-sync)

money_board_lock tuần 2026-06-29:
- MN: MN_ADAPTIVE_EXPLOIT_V1 (mode=1 method) ← XUNG ĐỘT với R3
- MT: MT_HYBRID_V1 + MT_STRENGTH_WEIGHTED_V52_5_2 (gộp 2 method) ← không liên quan
- MB: MB_ADAPTIVE_EXPLOIT_V1 (mode=1 method) ← NGOÀI SCOPE R3 (R3 chỉ MN; tắt chung sẽ phá /choi MB)

Lock tuần 29/06 kết thúc CN 05/07 (hôm nay); candidate hôm nay đã materialize từ 23:40 đêm qua.
OWNER ĐÃ CHỐT: Option A — giữ lock hết hôm nay; từ tuần 06/07 bỏ MN_ADAPTIVE_EXPLOIT_V1 khỏi pool MN;
V66/V67 cron GIỮ chạy cho MT/MB. Fallback pool MN tuần mới = MN_HYBRID_V1 (trừ khi owner duyệt MN chuyển BT 1-số theo đề xuất V10777).

## 6. TRẢ LỜI CÂU HỎI OWNER: "DeepSeek trên UI lịch sử dự đoán từng miền là model nào?"

| Tên hiện trên UI | model_id trong DB | Model THẬT phía sau API (docs 07/2026) | Vai trò |
|---|---|---|---|
| "DeepSeek R1" (NHÃN SAI — bug R1) | deepseek-reasoner | DeepSeek-V4-Flash THINKING (alias tự trỏ từ ~24/04/2026; trước đó R1/V3.x tùy thời kỳ) | ACTIVE official, /du-doan, 3 miền |
| "DeepSeek V4 Pro" (LỆCH tầng API) | deepseek-v4-pro | CŨNG là V4-Flash THINKING (code map qua alias deepseek-reasoner, gpt_analyzer.py:143) — KHÔNG phải V4 Pro thật 1.6T | SHADOW_AUTO 3 miền |
| "DeepSeek V4 Flash" | deepseek-v4-flash | V4-Flash NON-thinking (map qua alias deepseek-chat) | SHADOW_AUTO — con −72.6M sắp cắt |
| — | deepseek-chat | EOL, chỉ còn history | Nghỉ từ V7.9.12 |

Kết luận: hiện cả 3 id DeepSeek đang sống thực chất đều là V4-Flash (khác chế độ thinking).
"V4 Pro" của hệ chưa bao giờ là Pro thật ở tầng API.

Hệ quả cho R2: premise "DeepSeek-R1 mạnh hơn deepseek-reasoner" xây trên nhãn sai — R1-0528 (05/2025) là
thế hệ CŨ hơn V4-Flash-thinking (04/2026) mà deepseek-reasoner đang chạy. Lựa chọn mới đáng cân nhắc:
V4 Pro THẬT (id tường minh deepseek-v4-pro trên api.deepseek.com, 1.6T params, AA Index 52 vs Flash 47,
giá promo $0.435/$0.87 per 1M) — chưa từng thực chạy trong hệ.

## 7. QUYẾT ĐỊNH GATE — ĐÃ CHỐT 4/5, CHỜ 1

| # | Câu hỏi | Trạng thái |
|---|---|---|
| 1 | Version | ✅ CHỐT: V10778, ghi chú thực thi PLAN-20260705-V10777-R1SWAP-NAMEFIX-RETIRE |
| 2 | R2 route model thay thế | ⏳ CHỜ OWNER: R2-D thay bằng V4 Pro THẬT (khuyến nghị) / R2-A thêm R1-0528 qua OpenRouter / R2-C chỉ cắt không thêm |
| 3 | Cơ chế retire | ✅ CHỐT: thêm enum RETIRED + retire_reason + retired_date |
| 4 | CP-66.9 xung đột /choi | ✅ CHỐT: Option A (giữ lock hết 05/07, loại khỏi pool MN từ tuần 06/07; V66/V67 giữ cho MT/MB) |
| 5 | Docs lịch sử | ✅ CHỐT: ERRATUM đầu file, không rewrite lịch sử |

## 8. PLAN PHASE B (đã trình, chờ chốt R2 rồi thực thi)

B1 backup (backups/v10778_pre/: DB + 10 file code) + snapshot SHA256 PRE 4 bảng official
→ B2 R1 namefix 12 vị trí + ERRATUM + grep verify = 0 (XONG mới sang B3)
→ B3 R2 swap: retire v4-flash (RETIRED + retire_reason='PnL_56d=-72.6M_owner_approved_20260705') + đăng ký model
  mới theo phương án owner chốt (SHADOW_AUTO, output_eligible=False, first_run_date, KHÔNG backfill) + pricing + smoke 1 call thật trước khi gắn scheduler
→ B4 R3 retire CP-66.9: roadmap CLOSED_BY_OWNER_ABANDON + CP-66.10 đóng theo + STATUS CANCELLED → archive;
  main.py bỏ MN_ADAPTIVE_EXPLOIT_V1 khỏi pool MN (hiệu lực tuần 06/07); lý do: 'Owner decision 20260705: 21d gần −11M,
  không cải thiện hệ thống → từ bỏ, không promote.'
→ B5 R4 cắt 4 model: status RETIRED + retire_reason P&L 56d; giữ 100% history; reversible (như V10750)
→ B6 UI: màu RETIRED trong v87 models tab
→ B7 deploy VPS + restart + smoke (/api/health 200, /du-doan 200, admin 401)
→ B8 R5 verify: hash POST=PRE trong cửa sổ deploy (shadow rows ngày mai = natural growth); registry text-proof;
  scheduler dry-check (model mới CÓ, 5 model cắt KHÔNG); grep naming = 0; docs + Notion + public repo;
  NGÀY MAI sau closeout: báo cáo bổ sung first_run proof.

Rollback: restore backups/v10778_pre/ (code + DB nếu cần) + restart service; retire reversible bằng flip status.

## 9. HẠNG MỤC KHÔNG ĐỤNG (tuân thủ acceptance lock)

- 4 bảng official: predictions / final_bundles / lottery_results / model_daily_eval — Phase A chỉ ĐỌC.
- /du-doan, /choi lock tuần 29/06, scheduler main flow, V10752 MT cap top-13, V10766/V10767/V10770 — không đụng.
- deepseek-reasoner: model_id + API call — không đụng (chỉ sẽ sửa NHÃN ở Phase B; vấn đề alias 24/07 = PL-1 chờ owner).
- Shadow lanes checkpoint 14/07 (RF-MB, wplur_rf2_ml, ai_plurality2, MN BT) — chạy tiếp bình thường.

## 10. PLAN LEDGER (PL items phát sinh trong Phase A)

- PL-1 (CRITICAL, deadline 24/07/2026): alias deepseek-reasoner/deepseek-chat bị DeepSeek khai tử 24/07 15:59 UTC.
  Cần owner quyết riêng: đổi API call của deepseek-reasoner (ACTIVE official) sang id tường minh deepseek-v4-flash
  + thinking mode (giữ model_id + lineage), và sửa DIRECT_DEEPSEEK_SHADOW_MODEL_MAP cho v4-pro. KHÔNG làm trong V10778.
- PL-2 (ghi nhận): "deepseek-v4-pro" shadow từ trước đến nay thực chất đo V4-Flash-thinking (trùng bản chất với
  deepseek-reasoner official) — dữ liệu so găng v4-pro vs reasoner cần đọc với hiểu biết này.

## 11. EVIDENCE & INTEGRITY

- Live-sync trước audit DB: artifacts/live_sync/20260705_024425/manifest.json (production_db + prediction_trace).
- Nguồn giá: api-docs.deepseek.com/quick_start/pricing (07/2026); openrouter.ai/deepseek/deepseek-r1 ($0.70/$2.50);
  openrouter.ai/deepseek/deepseek-r1-0528 ($0.50/$2.15). V4 Pro promo $0.435/$0.87 (giá gốc $1.74/$3.48).
- Phase A KHÔNG sửa file runtime nào; script kiểm tra DB (read-only) đã archive vào backups/.
- 4 bảng official không bị ghi trong toàn bộ phiên Phase A.

— Hết payload V10778 (Phase A). Phase B sẽ có payload riêng sau khi owner chốt R2 và em thực thi xong.
