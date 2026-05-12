# NEXT ACTION (V105.33 — 2026-05-12 16:08 VN, natural verify snapshot)

Trạng thái: **V105_32_PUBLIC_SSOT_PASS** vẫn là baseline current truth; **V105_30D_SHADOW_NO_MISSING_DEPLOYED** giữ nguyên cho MN proof; **NATURAL_VERIFY_PENDING** vẫn active vì tại live sync 16:00 VN, MT/MB chưa đủ chu kỳ thật (`official=7/15` mỗi miền, chưa có final bundle 2026-05-12, chưa có shadow natural run). GitHub raw là SSOT công khai; Notion V105.30/V105.31/V105.32 tạm deferred theo owner. Official `/du-doan` giữ hard-lock.

Việc tiếp theo (ưu tiên):

1. **Natural verify MT/MB sau chu kỳ thật** — chỉ quan sát/sync/audit: `closed_file=0`, official `15/15`, same-day final bundle `model_count=15`, shadow expected/persisted/missing đúng contract, không `SYSTEM_MISSING`, không manual provider call. Chỉ gọi `V105_33_NATURAL_VERIFY_PASS` khi MN/MT/MB đều đủ.
2. **GLM-5.1 compact shadow profile (owner-gated)** — proposal `glm-5.1_compact_json_profile` đã được tạo: JSON-only, no explanation/CoT, max 2 tails, strict schema. Không gọi provider để test nếu chưa owner OK.
3. **Source-pool root-cause drilldown (accuracy lane)** — đo actual tail rớt ở tầng nào: `source_pool -> prompt -> rank -> top5 -> top2 -> bundle -> UI`, theo `region + weekday + station_set`, không đổi official.
4. **`FU-V105-28-AI-PRIORITY-ORDER` (P1)** — vẫn `AI_PRIORITY_HOLD`: reorder strongest-first theo region×weekday cần owner OK; tensor strength refresh cron 19:30 VN chỉ là proposal.
5. **Rule105 wording discipline** — dùng `prize_source_lock_by_source_region`, `true_violation_count=0`, `prior_flagged_rows_false_positive`, `production_mined_rules_untouched`, `quarantine_withdrawn`. Không dùng lại wording “30 violation” như current truth.
6. **Notion** — optional pointer page later; not blocking while GitHub raw exists.

Evidence mới: `V105_33_NATURAL_VERIFY_SNAPSHOT_20260512/evidence/V105_33_NATURAL_VERIFY_SNAPSHOT_REPORT.md`, plus private live sync manifest `artifacts/live_sync/20260512_160034/manifest.json`.
