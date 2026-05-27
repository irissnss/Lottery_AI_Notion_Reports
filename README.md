# Lottery AI Notion Reports

Latest public-safe package: `V106_34_RULE_PIPELINE_MECHANISM_AUDIT_PUBLIC_SAFE` (V106.34).

Latest report: `V106_34_RULE_PIPELINE_MECHANISM_AUDIT_PUBLIC_SAFE/V10634_RULE_PIPELINE_MECHANISM_REPORT_VN_PUBLIC.md`.

## Latest update (2026-05-27 — V106.34 Rule Pipeline Mechanism Audit)

Read-only investigation of the production rule pipeline that drives the live UI panel at xs.io.vn/app (Khuyến nghị / Rules hôm nay).

Three-question answer:

1. **Aggregated weekly or daily?** Axis is `region + weekday` (21 buckets). Mining runs **weekly** (Monday 00:30 VN), effectiveness eval **daily** at 20:15 VN, UI render **real-time** (no-cache).
2. **What ML?** Rules are **statistical lift mining, not ML**. Models (GLMS5.1, RF, COMBO, XGB+RF, Meta-Learn, Gemini, etc.) are the ML/AI side, merged with rules via `rec_score = 0.60 × WR_14d + 0.25 × rule_strength + 0.15 × diversity`.
3. **Real-time?** UI panel real-time on each open; WR 14d live SQL; predicted_tails live lookup; rule list weekly snapshot.

Owner correction confirmed: **MN/MT/MB independent across 8 dimensions** (source pool 3/4/5, prize keys, baseline p_region, BUCKET_QUALITY_TABLE 21 entries, BUCKET_SUPPRESS_THRESHOLD MN50/MT60/MB50, MB CALIBRATION V10.3 ceiling 55 vs 70, stations per day, n_365 ranges); only **7 items fixed** across regions (windows 4/8/12/16W, composite weights, verdict thresholds, lifecycle gates, boost table, convergence cap).

For previous versions (V106.33, V106.32, V106.31, ..., V106.26.2 FU4, V107, V106.06, ...), see `REPORT_INDEX.md`.
