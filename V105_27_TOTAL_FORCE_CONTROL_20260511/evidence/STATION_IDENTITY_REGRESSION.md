# STATION IDENTITY REGRESSION AUDIT — V105.27

## 1. Canonical SSOT in code

`web/backend/station_identity.py:16-33`

```
HCM, TPHCM, TP HCM, TP.HCM, TP. HCM, Hồ Chí Minh, Thành phố Hồ Chí Minh -> "TP. HCM"
Huế, Hue, Thừa Thiên Huế, Thua Thien Hue -> "Thừa Thiên Huế"
Đắk Lắk, Đắc Lắc, Dak Lak -> "Đắk Lắk"
Đắk Nông, Đắc Nông, Dak Nong -> "Đắk Nông"
```

## 2. Mission target

Owner mission V105.27 specifies:

```
HCM/TPHCM/TP.HCM/TP HCM/Thành phố Hồ Chí Minh -> "TP. HCM"      [MATCHES]
Huế/Thừa Thiên Huế -> "Huế"                                     [DOES NOT MATCH — code uses "Thừa Thiên Huế"]
Đắc Lắc/Đắk Lắk -> "Đắk Lắk"                                    [MATCHES]
Đắc Nông/Đắk Nông -> "Đắk Nông"                                 [MATCHES]
```

## 3. Runtime regression status

| Layer | Unexpected alias count | Raw exception allowed? | Status | Fix |
|---|---:|---|---|---|
| `station_identity_runtime_audit` (69 rows) | 0 (`unexpected_count=0` across all sampled rows) | `lottery_results.station` raw values kept for forensic | `STATION_IDENTITY_PASS` for runtime grouping (consistent with V105.9 / V105.19 lock) | None — preserved |
| `/pnl-tracker` | 0 — V105.9 confirmed Huế/Khánh Hòa/Kon Tum render canonical | `lottery_results` raw allowed | PASS | None |
| Prompt context / rule labels | 0 — V105.9 systemic audit confirmed routing through `canonical_station` | n/a | PASS | None |
| `lane_test_region_profiles` | 3 region rows (one per region), no weekday-as-station | n/a | PASS | None |
| Source-pool top5 | Per V101 shadow audits, canonicalized | n/a | PASS | None |

## 4. Conflict requiring owner

`Huế` canonical target conflict:

- Current code target: `Thừa Thiên Huế` (deployed live via V105.9, locked via V105.19).
- Mission V105.27 target: `Huế`.
- Surfaces that consume `Thừa Thiên Huế` today: `/pnl-tracker`, `station_identity_runtime_audit`, V101 source-pool shadow, prompt context labels, V52 MT drop/loz, cross-region spillover.
- Risk if flipped without coordination: P0 visible drift in `/pnl-tracker`, V101 shadow rows, prompt labels — would look like a station regression to UI consumers.

Recommendation: keep `Thừa Thiên Huế` until owner explicitly confirms flip OR clarifies that the mission's "Huế" target is shorthand. Add an explicit `OWNER_GATE` row to the decision register.

## 5. Acceptance state

- `runtime unexpected_count = 0` ✓
- Daily regression artifact: `station_identity_runtime_audit` 69 rows present, `shadow_only=1`, `diagnostic_only=1`, `output_eligible=0` flags set on every row.
- Owner mission Huế target mismatch: `OWNER_DECISION_PENDING`.

## 6. Verdicts

- `STATION_IDENTITY_PASS` for runtime grouping under current canonical target.
- `OWNER_DECISION_PENDING` for Huế target name (`Huế` vs `Thừa Thiên Huế`).
- No P0 data identity bug detected.
