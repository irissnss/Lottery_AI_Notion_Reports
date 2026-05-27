# V106.35 MB Target D = MB GĐB D-2 Deep-Dive (PUBLIC-SAFE)

Read-only audit of the owner hypothesis: "MB target date D matches MB Giải Đặc Biệt at D-2 — observed to often repeat".

## Read first

[`V10635_MB_DB_D2_DEEP_DIVE_REPORT_VN.md`](./V10635_MB_DB_D2_DEEP_DIVE_REPORT_VN_PUBLIC.md) — full Vietnamese owner report.

## Headline (honest, negative result)

Hypothesis tested across 2,338 days of MB history, 6 windows × 28 transforms × 7 weekday breakdown.

| Window | H1 loose (LAST2 D-2 in any MB tail D) | H2 strict (D-2 GĐB = D GĐB) | Verdict |
|---|---|---|---|
| 60d | 20.00% (lift −3.70pp) | 0.00% (lift −1.00pp) | ❌ Below random |
| 90d | 20.00% (lift −3.78pp) | 0.00% (lift −1.00pp) | ❌ Below random |
| 180d | 25.00% (lift +1.10pp) | 0.58% (lift −0.42pp) | ⚠️ Neutral |
| 365d | 22.97% (lift −0.91pp) | 1.12% (lift +0.12pp) | ❌ Below baseline |
| 730d | 24.72% (lift +0.87pp) | 1.12% (lift +0.12pp) | ⚠️ Marginal |
| ALL (2,268 days) | 25.44% (lift +1.65pp) | 0.97% (lift −0.03pp) | ❌ Random level |

**Verdict: hypothesis NOT validated by data.** Recent 60-90 days show NEGATIVE lift (−3.7 to −3.78pp). Recommended action: do NOT add this rule to any pipeline tier including SHADOW/PRE_REGISTER.

Owner observation likely caused by selection bias and confusion between H1 LOOSE (which sits at random baseline 23.8-24% by construction) and H2 STRICT (which is true random 1%).

## Files

| File | Purpose |
|---|---|
| `V10635_MB_DB_D2_DEEP_DIVE_REPORT_VN_PUBLIC.md` | Full Vietnamese owner report with statistical context, weekday breakdown, recommendations |
| `machine_readable/V10635_HYPOTHESIS_RESULTS.json` | 168 rows = 28 transforms × 6 windows full grid |
| `machine_readable/V10635_TOP_TRANSFORMS.json` | All 28 transforms ranked by composite score |
| `machine_readable/V10635_WEEKDAY_BREAKDOWN.json` | LAST2 transform broken down by weekday (365d) |
| `machine_readable/V10635_RECENT_TIMELINE.json` | Last 180 days hit/miss timeline + streak/gap stats |
| `machine_readable/V10635_EXECUTION_SUMMARY.json` | Top-level summary + safety gate |

## Safety

- Read-only audit, no DB mutation.
- No DB/JSONL/log files included.
- No VPS IP, no API keys, no provider call.
- Public push approved by owner for AI-tool consumption.

Status: report-only, diagnostic-only, no official mutation, hypothesis NOT validated.
