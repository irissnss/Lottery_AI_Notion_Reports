# Open issues — as of V81 (2026-05-07)

## Resolved during V77-V81 sessions

1. **V77 timing bug** (V70/V73 cron firing before daily test runners) → fixed (V77).
2. **scheduler tzinfo string bug** → fixed via `_today_vn_date_str()` / `_tomorrow_vn_date_str()` helpers (V78).
3. **AI prompt context gaps** (no_token_herd, V67/V70/V73, agreement_count) → captured in shadow prompts + shadow context (V78/V79).
4. **AI ↔ NO_TOKEN cross-verification missing** → shadow lane implemented (V79).
5. **Cluster-weighted consensus** → shadow lane implemented (V79).
6. **MB regime-shift watch** → shadow monitor implemented (V80).
7. **MN V67 save signal monitor** → shadow daily implemented (V80).
8. **No-token rule-aware feature pack** → shadow built (V80).
9. **Public root metadata stale at V77 after V78/V79/V80 publish** → fixed (V81 publish resets root).
10. **Provider shadow pilot owner consent** → received 2026-05-07 22:02 VN; pilot deployed shadow only (V81).

## Open watch (no P0)

1. Natural 6-job cron chain proof on 2026-05-08 (19:00 → 19:14 VN).
2. Accumulate 7-14d rolling `would_save vs would_break` per model + region in V81 shadow table.
3. MB cold streak watch — escalate to P0 regime-shift forensic if >= 7 more days all-method cold.
4. GPT-5-mini key validation on VPS (separate ops follow-up; pilot used deepseek-chat for FAST_CHEAP slot instead).

## Owner-locked

- Selector promotion (any) — requires explicit owner OK + 7-14d shadow proof + dossier.
- Official prompt change.
- Production model swap.
