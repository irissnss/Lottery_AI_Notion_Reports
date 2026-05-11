# Open Issues — as of V105.23 (2026-05-11 11:20 VN)

## V105.23 status

- `FU-V105-23-SOURCE-POOL-GAP-DRILLDOWN`: OPEN. SOURCE_POOL_MISS remains the main blind spot and needs persistent per-tail/per-station/per-stage drilldown.
- `FU-V105-23-V102-RELAXED-SHADOW`: OPEN. V102 strict selector shadow is 0 rows; relaxed diagnostic exists only as audit evidence, not DB/API/UI.
- `FU-V105-23-MODEL-COUNT`: OPEN. MN lane row has exact 20/20, but MT/MB latest adaptive rows are below 20/20 and must remain preview/diagnostic.
- `FU-V105-23-MANUAL-PREDICT-GATE`: OPEN. Manual scheduler/shadow endpoints are owner-locked, but manual `/api/predict/{region}` should also be owner-gated.
- `FU-V105-23-UI-TRUTH`: OPEN. `/du-doan-test` should render exact `MAIN_TEST_EQUALS_OFFICIAL` marker and a LO1/LO2/source-flow admin panel.
- Security owner action remains: revoke exposed/old PATs and approve SSH deploy-key migration.

## Measurement risk

No official promotion is justified. MN has positive lane-test signal only; MT remains protect mode; MB remains forensic mode. Any future adjustment must be region-specific and stay test-lane/shadow-only until owner gates pass.
