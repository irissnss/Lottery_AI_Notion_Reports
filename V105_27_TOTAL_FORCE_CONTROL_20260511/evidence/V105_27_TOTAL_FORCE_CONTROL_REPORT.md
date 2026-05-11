# V105.27 — TOTAL FORCE CONTROL REPORT (2026-05-11, 18:00 VN)

> **Tiếng Việt** — Báo cáo Owner. Đọc-only. Không đổi official. Không gọi provider. Bảo vệ MT. Khoá công thức MN/MT/MB. Cải thiện chất lượng dự đoán chỉ qua đo lường shadow/lane-test theo `region + weekday + station_set`.

---

## 1. EM ĐÃ ĐỌC GÌ TRONG PHIÊN NÀY

- Governance: `.Antigravityrules.md` (active-roadmap precedence + governance-traceability + live-data-integrity rules ở `.cursor/rules/`), `CHANGELOG.md`, `docs/CURRENT_TRUTH_SSOT.md`, `docs/FOLLOW_UP_TRACKER.md`, `docs/AUTOMATION_STATE.json`.
- Code: `web/backend/scheduler.py` (formulas, cascade, stdio harden, priority meta), `web/backend/main.py` (cascade-contract-audit endpoint, UI mapping), `web/backend/database.py` (token-cost guard, cuốn chiếu), `web/backend/model_registry.py` (`DD_COLUMN_POLICY`), `web/backend/station_identity.py` (canonical map), `web/frontend/app.js` + `index.html` (DD Trước/Sau UI), V101/V102/V103/V104/V105/V10524/V10525 materializers (`_v10524_source_pool_gap_drilldown.py`, `_v10525_candidate_flow_funnel.py`, …).
- Runtime: `data/lottery_ai.db` (live-sync `artifacts/live_sync/20260511_180555/manifest.json`), 160 tables, 4 official tables hashed.
- Reports: V105.19/20/22/22a/22b/25/25b CHANGELOG + SSOT rows; V105.21/23/24/26 NOT FOUND in local repo (only Drive/Notion).

## 2. CURRENT SSOT VERSION THEO TỪNG SOURCE

| Source | Latest version | Stale? |
|---|---|---|
| Local `CHANGELOG.md` | V20.3.37.105.25b | YES — thiếu V105.21/23/24/26 |
| Local `docs/CURRENT_TRUTH_SSOT.md` | V105.25b | YES — cùng gap |
| Local `docs/FOLLOW_UP_TRACKER.md` | FU-V105-25B (active) | YES — chưa có FU V105.21/23/24/26 |
| Local `docs/AUTOMATION_STATE.json` | `governance_seq=65`, full detail last seq 62 (V105.11) | YES — 14 phiên sau chưa append |
| Runtime DB (`data/lottery_ai.db`) | `predictions=4791 final_bundles=219 lottery_results=14654 model_daily_eval=4572` | RUNTIME_AHEAD |
| Notion MCP | Chưa re-check trong phiên | `NOTION_RECHECK_REQUIRED` |
| Public mirror `Lottery_AI_Notion_Reports/` | NOT_IN_WORKSPACE | `PUBLIC_STALE` |
| Root SSOT files (`LATEST_REPORT.json`, `REPORT_INDEX.md`, `CHANGELOG_PUBLIC.md`, `DELTA_INDEX.md`, `00_PUBLIC_RAW_LINKS.md`, `OPEN_ISSUES.md`, `NEXT_ACTION.md`) | NOT_PRESENT | `PUBLIC_STALE` / `SSOT_SYNC_REQUIRED` |

→ Phân loại tổng: `PUBLIC_STALE`, `CHANGELOG_STALE`, `SSOT_SYNC_REQUIRED`, `LATEST_REPORT_STALE`, `NOTION_RECHECK_REQUIRED`, `RUNTIME_AHEAD`.

## 3. KẾT LUẬN CÔNG THỨC + REGION GUARD

**Công thức đã được khoá đúng theo doctrine owner**:

```
MN_D = (MN+MT+MB) D-1 + (MN+MT+MB) D-2      [docs LOCK]
MT_D = (MN+MT+MB) D-1 + MN D                [code + runtime CONFIRM]
MB_D = (MN+MT+MB) D-1 + MN D + MT D         [code + runtime CONFIRM]
```

- Code: `scheduler.py:_attach_owner_priority_meta` (2406-2441) khoá đúng spec D-1 + same-day cross-region; MT/MB không có key D-2.
- Runtime probe 7 ngày: `d2_leak_in_predictions` (`source_regions` chứa `D2/D-2`) trả 0 rows cho MT+MB → **`D2_LEAK_BLOCKED`** xác nhận.
- MN D-2 hiện chỉ được tiêu thụ implicit qua `statistical_depth=30` trong `meta_predict.run_full_analysis`. Prompt-priority KHÔNG cite `MN_D2` → **`PROMPT_INJECTION_GAP` cho MN D-2 (P1, không phải stability)**.
- Region modes: `MN_PRIORITY=true`, `MT_PROTECT_MODE=true`, `MB_FORENSIC_MODE=true` (xác nhận qua `lane_test_region_profiles=3`).

→ `FORMULA_LOCK_CONFIRMED`, `D2_MN_ONLY`, `D2_LEAK_BLOCKED`, `MT_PROTECT_PRESERVED`, `MB_FORENSIC_ONLY`.

## 4. PHẦN ĐÃ ỔN

- ✅ Công thức MN/MT/MB khớp doctrine.
- ✅ MT/MB không leak D-2.
- ✅ Cascade khi stdio usable: 2026-05-09/10 MT+MB no-token 7/7 `rerun_post_mn` + 7/7 `rerun_post_mt` đầy đủ.
- ✅ Cascade MT-trigger ngày 2026-05-11 (17:30): MB `rerun_post_mt 7 thành công, 0 lỗi`.
- ✅ MT protect: V105.22 → V105.27 không có patch nào đổi MT selector/scoring/prompt/source-pool/roster.
- ✅ V105.22b token-cost guard: AI chỉ 1 lần/ngày, manual AI bị chặn ở `save_prediction` + `main.py /api/admin/predict-now`.
- ✅ Station identity runtime: `station_identity_runtime_audit=69 rows`, `unexpected_count=0`.
- ✅ Final bundles 21/21 last 7 days `model_count=15`, status=ACTIVE.
- ✅ Provider call session: **0**.
- ✅ Official 4 bảng đã hash guard (xem mục 11).

## 5. P0 BLOCKERS (PHẢI XỬ LÝ TRƯỚC KHI CẢI THIỆN PREDICTION)

| # | Blocker | Severity | Tác động | Hành động |
|---|---|---|---|---|
| P0-A | Cascade `_safe_stdio_ctx` chưa deploy VPS | P0 | 2026-05-11 MN-trigger cascade `0 thành công, 14 lỗi` → MT/MB no-token `rerun_post_mn` rỗng cho cả ngày. UI MT no-token vẫn ở DD Trước (không cập nhật D context sau MN verify). | Owner OK → deploy patch + restart `lottery.service` (xem Decision #10). |
| P0-B | PAT cũ chưa revoke + SSH deploy key chưa migrate | P0 (security) | Token cũ + token paste-trong-chat đều có nguy cơ rò rỉ. | Owner thực hiện theo `SECURITY_PAT_DEPLOY_KEY_AUDIT.md` mục 3 (Decision #9). |
| P0-C | Public SSOT bộ file root + `CHANGELOG_PUBLIC.md` không có trong workspace | P0 (governance) | Không thể chứng minh public latest. | Owner OK batch-publish sau khi P0-B xong (Decision #1). |
| P0-D | Local CHANGELOG/SSOT/FU/AUTOMATION_STATE thiếu V105.21/23/24/26 | P0 (governance) | Truy vết phiên gãy. | Backfill rows theo Drive/Notion. |

## 6. P1 BLOCKERS — CHẤT LƯỢNG DỰ ĐOÁN

| # | Blocker | Region | Note | Hành động |
|---|---|---|---|---|
| P1-A | `v10524_source_pool_gap_drilldown` / `v10524_candidate_flow_trace` NOT_PRESENT trong local DB; materializer code đã có | all | Không quan sát được drop-stage chi tiết (`FORMULA_EXCLUSION` / `TOP30_CAP` / `PROMPT_NOT_INJECTED` / `SELECTOR_RANK_DROP` / `BUNDLE_DROP`) | Owner OK chạy materializer (shadow_only=1, output_eligible=0) hoặc xác nhận tên bảng khác là canonical |
| P1-B | MN D-2 prompt explicit chưa wire | MN | statistical depth đã có D-2 nhưng AI prompt priority chưa có card `MN_D2` | Shadow-only profile `mn_d2_shadow_v1` (Decision #3) |
| P1-C | V103 supply class column `class` không tồn tại trong DB local | all | Có thể VPS đã migrate, local chưa; sample V102 RELAXED_L2 = 0 | Migrate schema + backfill 14d (Decision #6) |
| P1-D | Top2 A/B small sample (5-9 runs) | MN, MB | `would_save_count=2` MN (2026-05-10), break_ratio chưa stable per region+weekday | Run 14d structured shadow (Decision #4) |
| P1-E | MB_D_v2 chưa có scope chính thức | MB | 4 option (A-D), không có gì active | Owner định nghĩa scope (Decision #5); shadow-only 14d sau |

## 7. MÂU THUẪN CẦN OWNER XÁC NHẬN

1. **Huế canonical**: Code = `Thừa Thiên Huế` (V105.9/V105.19 live). Mission V105.27 = `Huế`. Đề xuất giữ `Thừa Thiên Huế`; nếu owner thực sự muốn `Huế`, kế hoạch flip cần coordinate 2 ngày để đổi tag mọi surface đang dùng (Decision #2).
2. **V105.26 báo cáo**: mission yêu cầu đọc nhưng local repo + CHANGELOG/SSOT/FU không có entry V105.26. Cần Drive/Notion cung cấp.
3. **`v10524_source_pool_gap_drilldown`**: tên bảng chuẩn — local không có; có thể VPS rename thành `candidate_drop_stage_daily` (103 rows). Cần owner xác nhận tên canonical.
4. **MB cuốn chiếu intermediate `rerun_post_mn`** trước khi MT verify: UI hiển thị hay ẩn (Decision #8)?

## 8. ĐỀ XUẤT THEO MIỀN

### 8.1 MN — `MN_PRIORITY=true`

- ✅ Giữ D-1/D-2 statistical depth (đã có).
- 🔬 Shadow-only `mn_d2_shadow_v1` — explicit MN_D2/MT_D2/MB_D2 priority card chỉ trong MN profile, không leak MT/MB. Đo natural-run 7/14 ngày.
- 🔬 V102 STRONG / PROMPT_REVIEW_STRONG candidate audit (V105.10 đã ghi FU-V105-11 còn mở) — tiếp tục cumulate sample.
- ⛔ Không promote official cho tới khi 14d clean + per-region+weekday positive evidence.

### 8.2 MT — `MT_PROTECT_MODE=true` (BẢO VỆ TUYỆT ĐỐI)

- ⛔ Không D-2 wide cho MT.
- ⛔ Không MN/MB rescue primary cho MT.
- ⛔ Không lo2 heavy tuning cho MT (giữ `LANE_TEST_LO2_POS_WEIGHT_BY_REGION.MT=0.55`).
- ⛔ Không bật V102 relaxed primary trên MT nếu chưa có evidence MT-specific tích cực.
- ✅ Cho phép: chỉ fix data quality (station, cascade stdio), UI labelling, stability — không đổi selector/scoring/prompt official MT.

### 8.3 MB — `MB_FORENSIC_MODE=true`

- ✅ Giữ `MB_D = (MN+MT+MB) D-1 + MN D + MT D`.
- 🔬 Anti-herding/shadow only. lo1/lo2 diagnostic only (V105.18 lane_test_region_weighted MB=0.95 lane-test only, không official).
- 🔬 MB_D_v2 chỉ shadow 14 ngày SAU khi owner định nghĩa scope (Decision #5). Default scope: option C (source-prize strong class) + D (same-day MN/MT stronger weighting); HOLD option A (D-2).

## 9. NHỮNG VIỆC LÀM ĐƯỢC NGAY AN TOÀN (KHÔNG CẦN OWNER GATE)

- ✅ Tạo bộ artifact V105.27 (đã làm trong phiên này, đường dẫn `artifacts/v10527/`).
- ✅ Cập nhật `CHANGELOG.md`, `docs/CURRENT_TRUTH_SSOT.md`, `docs/FOLLOW_UP_TRACKER.md` cho V105.27 (sẽ làm tiếp theo trong phiên).
- ✅ Cập nhật `docs/AUTOMATION_STATE.json` thêm event V105.27.
- ✅ Báo cáo chuẩn bị `SECURITY_PAT_DEPLOY_KEY_AUDIT.md` (đã có); không in token.
- ⛔ Không materialize `_v10524_source_pool_gap_drilldown.py` mà không owner OK (vì sẽ thêm rows vào diagnostic table mới — an toàn nhưng vẫn xin phép theo `live-data-integrity` rule).
- ⛔ Không flip station identity Huế canonical.

## 10. NHỮNG VIỆC CHỜ OWNER GATE

Xem `OWNER_DECISION_REGISTER.md` cho 10 decision. Tóm tắt:

- #1 Publish reports (cần #9 xong trước cho an toàn).
- #2 Huế canonical (recommend keep).
- #3 MN D-2 shadow prompt (recommend YES, shadow-only).
- #4 Top2 A/B 14d shadow (recommend YES).
- #5 MB_D_v2 scope (recommend C+D, HOLD A).
- #6 V102 relaxed HOLD (recommend YES).
- #7 Manual AI block (recommend KEEP).
- #8 MB intermediate display (recommend keep with label).
- #9 PAT/SSH (**P0** — recommend execute now).
- #10 VPS deploy `_safe_stdio_ctx` (**P0** — recommend deploy now).

## 11. OFFICIAL UNTOUCHED PROOF

Pre-flight hash + git status (đầu phiên):

```
git_head: e626ba7
git_branch: master
git_dirty_files: 809 (audit/doc artifacts từ phiên trước, không phải code change phiên này)

predictions     : rows=4791  sha256=675efcd3c1139e2fed6b73a25f529c3e295010461d5640a26c345e4f630a93cc
final_bundles   : rows=219   sha256=7c851d9b4e42907ac08817da125e19e2a5771bd0fe20f8b98d17e0270eae8c1a
lottery_results : rows=14654 sha256=36079dac47a93d8d9fb0c12736d2fe51490e6992d8713f7563e9edab76e99e0a
model_daily_eval: rows=4572  sha256=083a36ffea774fa6a711348b36e7293d5ed68b2ba88c40a1a119b8fdd36262df
```

Phiên này KHÔNG modify:
- `web/backend/main.py` `/du-doan` + `/api/final-bundle` + `generate_final_bundle`
- `final_bundles` table (4 hash giữ nguyên trong toàn phiên audit)
- selector/scoring/voting/production prompt/model roster/cascade semantics
- model pruning / production bundle weights / official output eligibility

Có thay đổi (chỉ artifact + governance docs sẽ cập nhật sau):
- Tạo `artifacts/v10527/` (preflight, db_tables scan, proxy evidence, drill, evidence/*).
- Sẽ cập nhật `CHANGELOG.md` + `docs/CURRENT_TRUTH_SSOT.md` + `docs/FOLLOW_UP_TRACKER.md` + `docs/AUTOMATION_STATE.json` với event V105.27.

## 12. PROVIDER CALL = 0 PROOF

- Không có code path provider mới được kích hoạt trong phiên này.
- Không gọi `gpt_analyzer.run_analysis`, `_run_ai_predict_job`, `_run_shadow_auto_eval`, hay bất kỳ entry point nào tới OpenAI/Anthropic/Google/DeepSeek/OpenRouter/Cohere/GLM/Grok/Qwen.
- Mọi script `_preflight.py / _proxy_evidence.py / _show_evidence.py / _today_drill.py / _db_tables_scan.py` đều read-only SQL trên `data/lottery_ai.db`.
- V105.22b token-cost guard vẫn active ở `database.save_prediction` + `_run_ai_predict_job` + `main.py /api/admin/predict-now` (returns 423 cho manual).

→ `NO_PROVIDER_CALL_CONFIRMED`.

## 13. EXACT NEXT COMMANDS / CHECKPOINTS

1. Update governance (làm ngay trong phiên này):
   - Append V105.27 row vào `CHANGELOG.md`.
   - Append V105.27 row vào `docs/CURRENT_TRUTH_SSOT.md`.
   - Append FU-V105-27-TOTAL-FORCE-CONTROL vào `docs/FOLLOW_UP_TRACKER.md`.
   - Append `_v66_last_event` (seq=66) vào `docs/AUTOMATION_STATE.json`.
2. Owner xử lý Decision #9 (PAT revoke + SSH migration).
3. Owner OK Decision #10 → deploy `_safe_stdio_ctx` lên VPS:
   ```
   ssh root@vietnix "cd /root/Lottery_AI_Test && \
     cp web/backend/scheduler.py backups/v105_25b_stdio_$(date +%Y%m%d_%H%M%S).py && \
     scp local:web/backend/scheduler.py web/backend/scheduler.py && \
     python -m py_compile web/backend/scheduler.py && \
     systemctl restart lottery.service && \
     sleep 5 && curl -s localhost:8000/api/health"
   ```
   Sau khi deploy: chờ MN verify tiếp theo, expect `Re-predict hoàn tất: N thành công, 0 lỗi`.
4. Owner OK Decision #1 → publish report sau khi PAT/SSH OK.
5. 7d natural-run tracking: kiểm `predictions.run_source='rerun_post_mn' COUNT(*)` cho MT/MB mỗi ngày = 7 cho từng region.
6. 14d window kết hợp Top2 A/B + V103 supply class + MB_D_v2 (sau khi owner định nghĩa scope).

## 14. DECISION CHECKLIST CHO OWNER

Anh chỉ cần trả lời `YES/NO/SCOPE` cho 10 mục dưới (chi tiết ở `OWNER_DECISION_REGISTER.md`):

- [ ] #1  Publish V105.24/25/25b/26/27 → Drive + Notion + public GitHub?  *(recommend YES sau khi #9 xong)*
- [ ] #2  Giữ canonical Huế = `Thừa Thiên Huế`?  *(recommend YES)*
- [ ] #3  Bật `mn_d2_shadow_v1` shadow-only 7/14d?  *(recommend YES)*
- [ ] #4  Chạy Top2 A/B shadow 14d cho MN + MB (MT measurement only)?  *(recommend YES)*
- [ ] #5  MB_D_v2 scope = ?  *(recommend C: source-prize strong class + D: same-day weighting; HOLD A: D-2)*
- [ ] #6  Giữ V102 relaxed HOLD?  *(recommend YES)*
- [ ] #7  Giữ chặn manual AI/provider call?  *(recommend YES)*
- [ ] #8  Hiển thị MB `rerun_post_mn` intermediate?  *(recommend YES, label `(stage=rerun_post_mn)`)*
- [ ] #9  Revoke PAT + chuyển SSH deploy key?  *(recommend YES — P0)*
- [ ] #10 Deploy `_safe_stdio_ctx` lên VPS?  *(recommend YES — P0)*

---

**Phân loại tóm tắt cho audit**: `OFFICIAL_LOCKED`, `NO_PROVIDER_CALL_CONFIRMED`, `FORMULA_LOCK_CONFIRMED`, `D2_MN_ONLY`, `D2_LEAK_BLOCKED`, `MT_PROTECT_PRESERVED`, `MB_FORENSIC_ONLY`, `MB_D_V2_OWNER_GATE`, `CASCADE_VERIFY_PENDING`, `NO_TOKEN_CASCADE_FAIL` (MT 2026-05-11), `CLOSED_FILE_FIXED_PENDING_LIVE`, `STATION_IDENTITY_PASS`, `PUBLIC_STALE`, `CHANGELOG_STALE`, `SSOT_SYNC_REQUIRED`, `LATEST_REPORT_STALE`, `NOTION_RECHECK_REQUIRED`, `RUNTIME_AHEAD`, `SOURCE_POOL_GAP_TABLE_NOT_MATERIALIZED`, `SOURCE_POOL_GAP_ACTIVE`, `PROMPT_INJECTION_GAP`, `V103_SUPPLY_BOTTLENECK`, `V102_RELAXED_HOLD`, `TOP2_AB_HIGH_BREAK=NO_SMALL_SAMPLE`, `SECURITY_P0_OPEN`, `PAT_REVOKE_PENDING`, `SSH_DEPLOY_KEY_PENDING`, `PUBLICATION_OWNER_GATE`, `NATURAL_LIVE_VERIFY_PENDING`, `DO_NOT_PROMOTE` (ngoài region-specific evidence).
