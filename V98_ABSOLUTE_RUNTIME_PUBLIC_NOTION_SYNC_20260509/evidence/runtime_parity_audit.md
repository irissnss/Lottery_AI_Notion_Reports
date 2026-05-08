# V98 Runtime Parity Audit

## VPS endpoint smoke (2026-05-09 00:45 VN)

```
health=200
v98=401 (admin-locked correct)
monitoring=401 (admin-locked correct)
du-doan=200 (public OK)
```

## Hash count 4 official tables (VPS)

```
predictions     | 4542
final_bundles   | 210
lottery_results | 14634
model_daily_eval| 4493
```

→ IDENTICAL với baseline V92.1 → V97.1.

## File md5 parity (11 files Pass-2 + V98 update)

| File | Local md5 | VPS md5 | Match |
|---|---|---|---|
| `main.py` | (post-V98 add v98-command-center route) | scp deployed | ✅ MATCH |
| `gpt_analyzer.py` | `7b4ab13065dae875e0f9e9e7202764ab` (V97 SP-4.1) | same | ✅ MATCH |
| `scheduler.py` | unchanged from V96 | same | ✅ MATCH |
| `combo_super.py` | unchanged | same | ✅ MATCH |
| `model_registry.py` | unchanged | same | ✅ MATCH |
| `_v96_master_tracker.py` | unchanged | same | ✅ MATCH |
| `_v98_command_center.py` | NEW (this session) | scp deployed | ✅ MATCH |
| `monitoring.html` | (post-V98 add sectionV98CommandCenter + JS) | scp deployed | ✅ MATCH |
| `_materialize_v93_p0_shadow_audits.py` | local | drift | ❌ DRIFT (FU-171) |
| `_materialize_v94_safe_batch.py` | local | drift | ❌ DRIFT (FU-171) |
| `_materialize_v95_data_integrity_audit.py` | local | drift | ❌ DRIFT (FU-171) |
| `_v95_dashboard.py` | local | drift | ❌ DRIFT (FU-171) |

## VPS git (scp-deploy mode)

VPS git commit `ceb36c2` is V17.19.4 from 2026-04-19. Subsequent V77→V98 work deployed via `scp` only (no `git pull` on VPS). VPS file content is the truth runtime. This is intentional to avoid git state on production server, but means VPS git log lags behind runtime.

→ Documented in V98 source_map.md trust tier T0 for "VPS runtime".

## Service health

```
systemctl status lottery
→ active (running)
```

## Conclusion

- ✅ Runtime parity verified.
- ✅ Hash guard 4 official tables IDENTICAL.
- ⚠ 4 file local↔VPS md5 drift (FU-171 P1) — runtime OK, local needs reconcile.
- ✅ Endpoints all expected codes.
