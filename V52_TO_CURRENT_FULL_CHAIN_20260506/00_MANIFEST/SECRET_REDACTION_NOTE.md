# Secret Redaction Note

This GitHub-ready export redacts raw API keys before commit/push. Redaction preserves report structure and evidence labels but replaces key values with placeholders.

Patterns redacted:
- Google API keys: `AIzaSy...`
- OpenAI project keys: `sk-proj-...`
- Anthropic keys: `sk-ant-...`

Files changed by redaction:

- `01_RAW_FULL_REPORT_CHUNKS\raw_full_report_combined_V52_to_current.txt`
- `01_RAW_FULL_REPORT_CHUNKS\raw_full_report_part_007_lines_015001_017500.txt`
- `01_RAW_FULL_REPORT_CHUNKS\raw_full_report_part_008_lines_017501_020000.txt`
- `01_RAW_FULL_REPORT_CHUNKS\raw_full_report_part_011_lines_025001_027500.txt`
- `01_RAW_FULL_REPORT_CHUNKS\raw_full_report_part_012_lines_027501_030000.txt`
- `07_GOVERNANCE_DOCS\CHANGELOG.md`
- `08_EMBEDDED_REPORTS\embedded_report_006_lines_000240_000489.md`
- `02_BY_VERSION\V52\src_130_CHANGELOG.md`
- `02_BY_VERSION\V52\src_130_CHANGELOG.md_part_001_lines_000001_002500.txt`
- `02_BY_VERSION\V55\src_077_SHADOW_ADD_GOOGLE_DIRECT_COHORT_20260505.md`
- `02_BY_VERSION\V55\src_088__v55_fix_envpath.sh`
- `02_BY_VERSION\V55\src_113__v55_vps_apply.sh`
