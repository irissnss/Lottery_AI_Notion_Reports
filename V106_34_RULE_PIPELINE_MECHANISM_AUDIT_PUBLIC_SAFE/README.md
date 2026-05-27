# V106.34 Rule Pipeline Mechanism Audit (PUBLIC-SAFE)

Read-only investigation of the production rule pipeline that drives the live UI panel `Khuyến nghị / Rules hôm nay` shown at xs.io.vn/app.

## Read first

[`V10634_RULE_PIPELINE_MECHANISM_REPORT_VN_PUBLIC.md`](./V10634_RULE_PIPELINE_MECHANISM_REPORT_VN_PUBLIC.md) — full Vietnamese owner report.

## Three-question answer (owner's questions)

1. **Aggregated weekly or daily?** Axis is `region + weekday` (21 buckets = 3 regions × 7 weekdays). Mining runs **weekly** (Monday 00:30 VN), effectiveness is evaluated **daily** at 20:15 VN, UI panel renders **real-time** on every request.
2. **What ML?** Rules are **statistical lift mining, not ML**. Models (GLMS5.1, RF, COMBO, XGB+RF, Meta-Learn, Gemini, etc.) are the ML/AI side — two separate pipelines merged in the UI via `rec_score = 0.60 × model_WR_14d + 0.25 × rule_strength + 0.15 × diversity_bonus`.
3. **Real-time?** UI panel is real-time (no-cache); WR 14-day chart and predicted-tails are live SQL on each request; rule list and metrics are weekly snapshots refreshed every Monday 00:30.

## Region independence — owner correction validated

Owner pointed out that MN/MT/MB have independent cumulative coefficients, not a fixed shared 12-16 week formula. This audit confirms that claim:

- **Fixed across regions (7 items):** window sizes 4W/8W/12W/16W; composite weights 0.50/0.35/0.10/0.05; verdict thresholds; lifecycle gates; boost table; convergence cap.
- **Independent per region (8 items):** source pool (3/4/5 cross-region directions); prize key sets (MN/MT have 6 tiers, MB has 5); baseline probability `p_region`; BUCKET_QUALITY_TABLE (21 individual entries); BUCKET_SUPPRESS_THRESHOLD (MN=50, MT=60, MB=50); MB CALIBRATION V10.3 (MB ceiling 55% vs MN/MT 70%); station-per-day count (MN 3-4, MT 2, MB 1); effective sample sizes (`n_365` ranges differ).

## Files

| File | Purpose |
|---|---|
| `V10634_RULE_PIPELINE_MECHANISM_REPORT_VN_PUBLIC.md` | Full Vietnamese owner report |
| `machine_readable/V10634_PER_REGION_INDEPENDENCE_MATRIX.json` | Structured matrix of 7 fixed + 8 independent items with source-file refs |
| `machine_readable/V10634_BUCKET_QUALITY_TABLE_AUDIT.json` | 21 BUCKET_QUALITY scores + suppression effects per region |
| `machine_readable/V10634_RULE_PIPELINE_FLOW.json` | 12-stage pipeline DAG with file references |
| `machine_readable/V10634_DB_AUDIT_LIVE_DATA.json` | Live DB snapshot of mined_rules by region/weekday |
| `machine_readable/V10634_EXECUTION_SUMMARY.json` | Top-level summary + safety gate |

## Safety

- Read-only audit, no DB mutation.
- No DB/JSONL/log files included.
- No VPS IP, no local paths, no API keys, no provider call.
- Public push approved by owner for AI-tool consumption.

Status: report-only, diagnostic-only, no official mutation.
