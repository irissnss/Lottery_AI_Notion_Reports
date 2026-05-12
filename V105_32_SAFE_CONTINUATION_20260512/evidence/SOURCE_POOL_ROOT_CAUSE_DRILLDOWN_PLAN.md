# Source-Pool Root-Cause Drilldown Plan

Generated: 2026-05-12 12:18 VN  
Status: `OPEN P1 / ACCURACY_LANE`  
Runtime action: plan only. No official policy changed.

## Goal

After runtime stability is clean, measure real accuracy loss: where does the actual tail drop out?

Pipeline:

`actual_tail -> source_pool -> prompt_context -> ranking -> top5 -> top2 -> bundle -> UI`

## Keys

| Key | Purpose |
|---|---|
| `date` | target draw date |
| `region` | target region |
| `weekday` | canonical quick-read bucket |
| `station_set` | canonical station bucket |
| `target_region` | region being predicted |
| `source_region` | source region used to supply evidence |
| `source_station` | source station after alias normalization |
| `source_offset` | D, D-1, D-2 |
| `prize_source` | prize key from source region |
| `rule_family` | mined/source-pool/rule family |
| `model` | model or selector involved |
| `tail` | candidate tail |
| `actual_hit` | whether tail appeared in actual result |
| `in_source_pool` | candidate was supplied |
| `in_prompt` | candidate reached prompt/context |
| `ranked` | candidate survived ranking |
| `in_top5` | candidate reached top5 |
| `in_top2` | candidate reached top2 |
| `bundled` | candidate entered final/test bundle |
| `displayed_ui` | candidate was visible in UI |
| `dropped_reason` | first missing stage |

## Existing Surfaces

| Surface | Current role |
|---|---|
| `v10524_source_pool_gap_drilldown` | row per actual tail and stage; records first miss reason |
| `v10524_candidate_flow_trace` | full candidate funnel trace |
| `v10525_source_pool_reason_ranking` | aggregates misses by region, weekday, station, reason, prize |
| `v101_region_source_pool_shadow` | source-pool supply layer |
| `v101_region_source_pool_top5_shadow` | top5 source-pool readout |
| `v104_shadow_prompt_candidate_injection` | prompt injection visibility |
| `experimental_preview_shadow` | ranking/top5/top2/bundle preview evidence |
| `final_bundles` | official bundle read-only comparison |

## Output Matrix

| Region | Actual tail | Source pool | Prompt | Rank | Top5 | Top2 | Bundle | UI | Drop reason | Action |
|---|---|---|---|---|---|---|---|---|---|---|
| MN/MT/MB | measured tail | yes/no | yes/no | yes/no | yes/no | yes/no | yes/no | yes/no | first failed stage | measure only |

Rules:

- Do not change official.
- Do not promote any experiment.
- Use `region + weekday + station_set` as the primary quick-read axis.
- Rule105 prize checks use `source_region`, not `target_region`.
