# Open issues — V78 (updated 2026-05-07 20:05 VN)

## Active

1. **FU-144 / V78 Prompt Shadow Audit**
   - Status: DEPLOYED_PENDING_LIVE_VERIFY.
   - Verify natural cron 19:10 VN tomorrow.
   - No provider calls yet. Owner OK required before calling AI providers with shadow prompts.

2. **MB all-method cold**
   - Status: WATCH.
   - OFFICIAL 0/4, V70/V73/C16/V67 no save in 4-day window.
   - Escalate to P0 if cold persists 7 additional days.

3. **MN AI herd ignores V67 save candidate**
   - Status: MEASURED.
   - 2026-05-07 AI/official herd 94 missed; V67/V73 95 hit.
   - Track with V78 shadow prompts.

## Resolved / Mitigated

- V77 timezone cron bug mitigated in V78 by replacing `datetime.now(VN_TZ)` string usage in selector/monitor nested jobs.
- V78 shadow tables all guard flags valid: `output_eligible=0`, `diagnostic_only=1`, `owner_approved=0`.
