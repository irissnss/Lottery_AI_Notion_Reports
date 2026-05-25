# V106.29 Next-Live Runbook Public-Safe

This runbook is public-safe and omits private runtime details.

## Manual checkpoints

1. Pre-live: rebuild artifact-only comparison board.
2. Post-bundle per region: refresh official-vs-lane-vs-shadow board, but do not mutate official output.
3. Post-result per region: close out would_save, would_break, false_promo, and net effect.
4. End of day: produce artifact-only summary and safety gate.

## Hard stops

- Stop if schema/extractor audit has not passed and a V106.28R1 import is requested.
- Stop if any action would write official predictions, final bundles, production prompt, selector, scoring, roster, wallet, deploy, or cron without explicit owner approval.
- Stop if public-safe scan fails.

## Current run mode

Manual-only, artifact-only, diagnostic-only. Cron and live deploy remain false unless owner approval and smoke proof are recorded.
