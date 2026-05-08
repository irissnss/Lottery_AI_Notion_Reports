# V98 Owner Gate Queue

## P0 — CRITICAL (need owner decision soon)

### FU-170 — Notion sync UNVERIFIED
- **Severity**: P1 → upgrade to P0 if Notion AI is critical for owner workflow
- **Evidence needed**: Owner provide one of (a) MCP access in Cursor session next time, (b) screenshot từng Notion page với current text, (c) confirm stand-down for now
- **Decision date**: Owner anytime
- **Current status**: OWNER_LOCK
- **Safe action**: Public V98 wrapper đầy đủ — owner có thể copy-paste vào Notion manually nếu cần
- **Blocked action**: Programmatic Notion update via Cursor MCP

### FU-172 — Cron natural-fire 23:45+ misfire
- **Severity**: P1
- **Evidence needed**: Tomorrow 2026-05-09 23:45-23:55 cron clean test (no service restart in interim) — if still misfire, root cause is APScheduler config not service restart
- **Decision date**: 2026-05-09 23:55 VN
- **Current status**: OWNER_LOCK pending tomorrow's data
- **Safe action**: Wait one cycle. V98 Command Center Panel 3 will show row counts.
- **Blocked action**: Modify APScheduler config without 7d empirical pattern

## P1 — MEDIUM (owner-gated 14d / 30d)

### FU-173 — Bundle conversion replay 30d evidence
- **Decision date**: 2026-05-21 (14d gate)
- **Evidence needed**: when many models picked actual but final missed; top1 vs top2; AI vs no-token; WR gate filtered winners; would_save / would_break per region
- **Current status**: DEFER (V93/V94/V95 shadow tables already collecting data)
- **Safe action**: Wait for natural data accumulation through V93.1/V94.1 cron daily
- **Blocked action**: Production bundle scoring change

### FU-174 — Combo-super BT-first replay
- **Decision date**: 2026-05-21 (14d gate)
- **Evidence needed**: BT-first vs current WR; registry-derived pool vs hardcode 6 AI; would_save/would_break/false_promotion; MT no-break; MB behavior; Wilson CI
- **Current status**: DEFER
- **Safe action**: Build replay-only metric in shadow lane; document `combo_super.py` BT-first variant as method 't40_bt_first_replay'
- **Blocked action**: Modify combo_super.py production logic without 14d evidence

### FU-175 — Prompt context injection dossier per region
- **Decision date**: 2026-05-21 (14d gate)
- **Evidence needed**: For each region (MN/MT/MB) — which fields to inject (V67/V73/D-2/cold_flag/spillover/AI-NT conflict warning); source table; leakage guard; expected benefit; risk
- **Current status**: DEFER
- **Safe action**: Document in `docs/PROMPT_CONTEXT_INJECTION_DOSSIER.md` — owner-locked
- **Blocked action**: Production prompt change without 14d evidence

### FU-165 — RR-16.4 §9 D-2 region-gated
- **Decision date**: 2026-05-21
- **Evidence needed**: V94 D-2 60d data MN +11.67pp / MT NEGATIVE / MB NEUTRAL — does §9 update warrant?
- **Current status**: OWNER_LOCK

## P2 — INFORMATIONAL (no decision needed)

- FU-161 (3-càng status docs) — DONE
- FU-V96-AUDIT-9 Notion sync (subset of FU-170)

## Summary

- **2 P0** owner decisions pending (FU-170 Notion access, FU-172 cron misfire)
- **5 P1 owner-gated** waiting 14d-30d evidence
- **9 P1 carry-overs** mostly tied to above
- **Owner safe action tonight**: SLEEP. Tomorrow auto cron will provide first natural data points.
