# V91 — Region strategy matrix

Generated 2026-05-08T01:19:20+07:00

## MN — Recovery candidate

**Status**: 2 method 60d clean lift, 1 V67/V73 save signal hôm 2026-05-07.

| Item | Evidence | Action |
|---|---|---|
| MN_SPECIALIST_ROSTER_V1 | 60d 51.7% save=4 break=0 | DOSSIER_PREP target 2026-05-21 |
| MN_AI_CHAIN_PRESERVATION_V1 | 60d 52.5% save=5 break=1 | DOSSIER_PREP target 2026-05-21 |
| V81 provider pilot MN | 3 model converge V67/V73 tail 95 | KEEP_PILOT 7d→14d |
| AI_HERD MN | 48.3% PARITY+ vs OFFICIAL 45% | NO change |
| NO_TOKEN_HERD MN | 51.7% PARITY (Wilson overlap OFFICIAL) | NO global floor change |

**Hard locks**: KHÔNG promote vào official trước 30d (2026-06-06). Test-lane voter cần dossier + owner OK.

## MT — Protect at all cost

**Status**: OFFICIAL 50% baseline mạnh nhất hệ thống.

| Item | Evidence | Action |
|---|---|---|
| OFFICIAL MT | 50.0% baseline | DO_NOT_TOUCH |
| AI_HERD MT | 43.3% (-6.7pp), 12 breaks | DESTRUCTIVE_PROVEN; do not weight up |
| MT_AI_CHAIN_PRESERVATION_V1 | 41.7% (-8.3pp), 12 breaks | DESTRUCTIVE_PROVEN; CLOSE_DECISION |
| MT_PRIOR_REGION_CONTEXT_SAFE_V1 | 41.7% (-8.3pp), 9 breaks | DESTRUCTIVE_PROVEN; CLOSE_DECISION |
| V70_CONSENSUS MT | 4/4 hits (n=4 only) | INSUFFICIENT; wait 14d |
| Any new method | must include MT_no_break test | MANDATORY GATE |

**Hard locks**: KHÔNG remove OFFICIAL/V70 consensus-first. KHÔNG promote AI_CHAIN/PRIOR_REGION. MT no-break test (lose_flip < win_flip / 2 over 14d) is mandatory cho mọi promotion proposal.

## MB — Forensic queue

**Status**: cold confirmed; mọi method ±5pp around OFFICIAL 25%.

| Item | Evidence | Action |
|---|---|---|
| OFFICIAL MB | 25.0% baseline weak | continue measure |
| MB_SPECIALIST_ROSTER_V1 | 36.6% n=41 only (PROMISING_LIMITED) | WAIT_60D target 2026-07-06 |
| AI_HERD MB | 26.7% noisy (12 save 11 break) | continue measure |
| NO_TOKEN_HERD MB | 23.3% PARITY- | NO floor increase |
| V79 cluster MB | 0/4 (n=4) | INSUFFICIENT |
| V80 mb_regime_shift | 4d only | continue 7d watch |

**Auto-trigger**: Nếu MB OFFICIAL still 0/7 đến **2026-05-14** → escalate P0 MB regime forensic dossier (auto-generate em sẽ làm).

**Hard locks**: KHÔNG raise NO_TOKEN MB (60d delta -3.3pp). KHÔNG promote method nào trước 60d sample.

## Cross-cutting policy

- KHÔNG global NO_TOKEN floor change (region delta differ: MN +3.4pp / MT +8.3pp / MB -3.3pp).
- Region-specific only; mỗi region cần dossier riêng.
- MT no-break test bắt buộc.
- 30d gate (2026-06-06) cho MN proposals; 60d gate (2026-07-06) cho MB.
