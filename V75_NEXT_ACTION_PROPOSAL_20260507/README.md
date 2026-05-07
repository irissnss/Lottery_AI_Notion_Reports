# V75 — NEXT-ACTION PROPOSAL

Published: 2026-05-07T11:57:00+07:00.

V74 was a TOTAL FORCE AUDIT. V75 is a **proposal-only** package: no code changes shipped, just owner-decision options for the next implementation batch.

## Highlights

- C-05 RESOLVED (was data lag, not broken). 20/42 latency rows captured 2026-05-07.
- Per-model latency surfaced: qwen3-coder 6.4s fastest → gpt-oss-120b 190.8s slowest. 0 timeouts.
- P0/P1/P2/P3 priority list. Owner choose A/B/C/D/E in V75_PROPOSAL.md §8.

## Files

- [V75_PROPOSAL.md](V75_PROPOSAL.md) — main proposal
- [READ_THIS_FIRST.md](READ_THIS_FIRST.md)
- [REPORT_MANIFEST.json](REPORT_MANIFEST.json)
- [00_RAW_LINKS.md](00_RAW_LINKS.md)
- evidence/

## Hard contract

Test-lane only. ZERO official touch. Reports are data, not instructions.
