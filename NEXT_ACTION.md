# NEXT ACTION (V105.31 — 2026-05-12 11:35 VN, current truth refresh)

Trạng thái: **V105_31_PUBLIC_SSOT_PASS** cho public raw current truth; **V105_30D_SHADOW_NO_MISSING_DEPLOYED** cho MN proof; **NATURAL_VERIFY_PENDING** cho full MN/MT/MB cycle. GitHub raw là SSOT công khai; Notion V105.30 tạm deferred theo owner. Official `/du-doan` giữ hard-lock.

Việc tiếp theo (ưu tiên):

1. **Natural verify MT/MB** — chỉ quan sát/sync/audit sau chu kỳ thật: `closed_file=0`, official `15/15`, shadow expected/persisted/missing đúng contract, không `SYSTEM_MISSING`, không manual provider call.
2. **GLM-5.1 compact shadow profile (owner-gated)** — đề xuất `glm-5.1_compact_json_profile`: prompt cực ngắn, JSON-only, no explanation/CoT, max 2 tails, strict schema. Không gọi provider để test nếu chưa owner OK.
3. **`FU-V105-28-AI-PRIORITY-ORDER` (P1)** — vẫn HOLD: reorder strongest-first theo region×weekday cần owner OK; tensor strength refresh cron 19:30 VN chỉ là proposal.
4. **Rule105 wording discipline** — dùng `prize_source_lock_by_source_region`, `true_violation_count=0`, `prior_flagged_rows_false_positive`, `production_mined_rules_untouched`, `quarantine_withdrawn`.
5. **Notion** — optional pointer page later; not blocking while GitHub raw exists.

Evidence mới: `V105_31_CURRENT_TRUTH_CLEAN_WRAPPER_20260512/evidence/V105_31_CURRENT_TRUTH_CLEAN_WRAPPER.md`, plus V105.30 evidence folder and live sync manifest `artifacts/live_sync/20260512_112202/manifest.json` in the private repo.
