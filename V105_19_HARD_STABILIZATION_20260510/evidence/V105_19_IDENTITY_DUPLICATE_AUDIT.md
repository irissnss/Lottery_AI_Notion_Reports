# V105.19 Identity / Duplicate Audit

Generated at: `2026-05-10T22:05:37`

## Contract

- `station_identity.py` is the station SSOT.
- Raw `lottery_results.station` was not mutated.
- Official tables touched: NO.

## Required Alias Proof

- `Huế` -> `Thừa Thiên Huế`
- `Thừa Thiên Huế` -> `Thừa Thiên Huế`
- `TP. HCM` -> `TP. HCM`
- `HCM` -> `TP. HCM`
- `TPHCM` -> `TP. HCM`
- `Thành phố Hồ Chí Minh` -> `TP. HCM`
- `Đắk Lắk` -> `Đắk Lắk`
- `Đắc Lắc` -> `Đắk Lắk`
- `Đắk Nông` -> `Đắk Nông`
- `Đắc Nông` -> `Đắk Nông`
- `Bà Rịa Vũng Tàu` -> `Bà Rịa - Vũng Tàu`

## Aggregate

- `station_alias_unexpected_count`: 0
- `table_column_duplicate_count`: 1
- `method_id_duplicate_count`: 0
- `prompt_version_duplicate_count`: 0

## Table / Column Findings

### `lottery_results.station`
- action_taken: `READ_TIME_CANONICALIZATION_ONLY`
- official_table_touched: `NO`
- collision_groups: `{"TP. HCM": ["HCM", "TP. HCM"], "Đắk Nông": ["Đắc Nông", "Đắk Nông"], "Thừa Thiên Huế": ["Huế", "Thừa Thiên Huế"], "Đắk Lắk": ["Đắc Lắc", "Đắk Lắk"]}`
- unexpected_aliases: `[]`

