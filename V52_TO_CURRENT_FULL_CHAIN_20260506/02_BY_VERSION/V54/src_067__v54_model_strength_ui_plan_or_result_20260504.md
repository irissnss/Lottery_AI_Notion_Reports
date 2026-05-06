# V54 C-14 — Region / Weekday / Station Strength Chips Plan

> Status: `READY_FOR_UI_TEST_ONLY_NOT_DEPLOYED`

## Source

`model_strength_by_region_weekday_station_daily` (V52.5.1)

- 9052 rows.
- Windows: 7/14/30/60.
- Grains:
  - `region`
  - `region_weekday`
  - `region_station`

## Planned UI Placement

`/du-doan-test`:

- On test_bundle card header:
  - primary experiment;
  - strength anchor;
  - strongest model family for this region/week/window.
- New mini panel:
  - strongest TOKEN / NO_TOKEN / SHADOW by region.
  - weekday-specific risk.
  - station-specific strength for MN/MT.

## Labels

- `KEEP_FOR_REGION_SPECIFIC_SIGNAL`
- `KEEP_FOR_WEEKDAY_SPECIFIC_SIGNAL`
- `KEEP_FOR_STATION_SPECIFIC_SIGNAL`
- `WATCH_CANDIDATE`
- `SAMPLE_THIN`
- `NOT_ENOUGH_DATA`
- `DO_NOT_PRUNE_YET`

## Safety

UI-test-only. Does not change any model roster or output policy.
