# V91 — Stale-FU auto-update spec

Generated 2026-05-08T01:19:20+07:00

## Trigger

On every CHANGELOG version bump (V?? new entry), agent runs:
1. Parse FU IDs mentioned in new CHANGELOG entry body.
2. For each FU:
   - If FU.status currently `WAIT*` → propose update to `DEPLOYED_PENDING_VERIFY`.
   - If FU.status currently `DEPLOYED*` and now has live evidence in CHANGELOG → propose update to `LIVE_PROVEN`.
   - If FU is older than 30 days and not mentioned in last 5 versions → propose `SUPERSEDED_BY_<latest_V>`.
3. Output proposals to `FU_STALE_REVIEW_REQUIRED.md` (NOT auto-applied).

## Auto-apply rules (safe subset)

Agent tự apply (no owner gate) if ALL conditions met:
- FU status currently `WAIT_*` AND
- FU mentioned in current CHANGELOG entry AND
- FU not on owner_lock AND
- official_impact = NO AND
- FU is < 5 versions old (recent)

Owner-gate required if:
- FU has owner_lock = YES
- FU.official_impact = YES
- FU > 5 versions old (likely SUPERSEDED, manual review)

## Implementation (V91 docs-only)

V91 demonstrates the rule by:
- Identifying 74 stale FU items.
- Proposing updates for 67 (90% docs-only).
- Leaving 7 NEEDS_RUNTIME for V92.
- NOT auto-applying — owner reviews FU_STALE_RECONCILIATION_MATRIX.md first.

## Hard locks

- NEVER auto-close FU with owner_lock = YES.
- NEVER auto-modify FU.official_impact field.
- NEVER auto-close FU during live cron window (19:00-19:14 VN).
