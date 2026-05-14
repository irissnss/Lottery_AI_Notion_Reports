# V105.38 Timeout Extended Grace Review — Proposal Only

Generated: 2026-05-12 22:53 VN

Decision: `NOT_DEPLOYED_TONIGHT`.

Current values:

- soft continue: `90s`
- hard timeout: `300s`
- extended grace: not deployed
- provider/manual call count: `0`
- trigger timing: unchanged
- restart/deploy: none

Reason:

- `scheduler.py` starts provider calls in worker threads and soft-continues at 90s, but pending calls are awaited sequentially to hard timeout after the model loop.
- Increasing hard timeout to 500 can add about 200s per pending call and delay region closeout/cascade.
- `main.py` late-result metadata still hard-codes 300s.
- `gpt_analyzer.py` OpenRouter HTTP timeout still hard-codes 300s.
- A real 500s EXTENDED_GRACE needs separate freeze/late-assimilation semantics, not a blind 300->500 change.

Final label:

- `V105_38_TIMEOUT_EXTENDED_GRACE_PROPOSAL_ONLY`
- `REASON_NOT_PROVEN_SAFE_FOR_NIGHT_DEPLOY`
- `SOFT_CONTINUE_REMAINS_90`
- `HARD_TIMEOUT_REMAINS_300`
- `EXTENDED_GRACE_TARGET_500_OWNER_GATED`

Private full proposal: `artifacts/v105_37_stability_quality/V105_38_TIMEOUT_EXTENDED_GRACE_PROPOSAL_ONLY.md`.
