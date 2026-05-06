# V68 — MT diagnostic + C-16 budget expansion 15-20 voters

Published: 2026-05-07 01:45 VN.

- Main: [V68_REPORT.md](V68_REPORT.md)
- Manifest: [MANIFEST.json](MANIFEST.json)
- Index: [00_READING_INDEX.md](00_READING_INDEX.md)

## Highlights

- MT regression diagnosed: 4/6 V67 picks were single-source noise (single cross MN→MT factor ~1.23-1.25 has good expected edge but high single-day variance).
- V67.1 STRICT-confidence gate (no penalty): skip emit when `top.contributions<2 AND score<1.5`.
  - MT 33% → 50%; MN 100% (fewer rows but cleaner); MB unchanged.
- C-16 budget expanded `target_min/max 8/10 → 15/20`.
  - 2026-05-07 MN selected 20, MT 15, MB 15.

## Hard contract

- Test-lane only. ZERO touching `/du-doan`/`final_bundles`/scoring/model_registry/prompt.
