# Current System State

## Official

- `/du-doan` remains user-facing official output.
- `final_bundles`, official `predictions`, scoring, voting, prompt, and roster remain locked.
- No official change has enough proof yet.

## Test lane

- `/du-doan-test` is admin-only.
- Current status: `LIVE_PARALLEL_AUTO_PENDING_ONLY` moving toward pre-result readiness.
- It now includes:
  - visual test output card;
  - experience mode;
  - C-16 adaptive model budget;
  - strict LO3/Xien verification;
  - dynamic readiness trigger.

## Measurement

- Model strength tensor exists and is bucket-aware.
- Loz stage trace exists.
- Weekday blackspot exists.
- Per-model latency remains missing and blocks pruning/cost decisions.
