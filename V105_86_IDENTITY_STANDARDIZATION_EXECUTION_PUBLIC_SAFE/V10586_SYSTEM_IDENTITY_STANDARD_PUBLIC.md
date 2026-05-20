# System Identity Standard

Updated: `2026-05-20T11:04:21+07:00`

## Core Fields
- `canonical_station`: Accent/punctuation-normalized station used for DB lookup and grouping; never includes weekday/source_offset.
- `station_alias_raw`: Original raw spelling preserved for audit/trace only.
- `station_slot_key`: region:source_offset:weekday:canonical_station for rule/source-specific identity.
- `display_label`: Human UI label, e.g. HCM T2; never used for DB lookup.
- `region`: Target output region unless explicitly named source_region.
- `source_region`: Region where source result/rule input came from.
- `target_region`: Region being predicted/evaluated.
- `weekday`: Canonical weekday code T2/T3/T4/T5/T6/T7/CN.
- `source_weekday`: Weekday of source result after source_offset resolution.
- `target_weekday`: Weekday of target prediction date.
- `source_offset`: D, D-1, etc. used to resolve source_date.
- `station_set_canonical_json`: JSON array of canonical_station values, sorted or stable order by domain owner.
- `station_set_display`: UI-only joined display labels.
- `source_prize_keys`: Rule prize keys such as G?B+G7, resolved through prize-key aliases.

## Ownership
- **DB lookup**: canonical_station only; raw aliases are lookup candidates during read-time compatibility.
- **Rule identity**: station_slot_key.
- **UI**: display_label plus collapsed raw diagnostic.
- **Prompt**: must include canonical_station + display_label + source_offset + weekday when owner approves prompt patch.
- **ML feature key**: station_slot_key for rule/source-specific features; canonical_station only for station-level features.
- **Trace**: future additive raw + canonical + slot; no historical mutation in V105.86.
- **raw_value**: audit-only.
- **display_label**: must never be used for lookup.

## Examples
- `TP. TP. HCM` -> `{'raw': 'TP. TP. HCM', 'canonical_station': 'TP. HCM', 'station_alias_raw': 'TP. TP. HCM', 'display_label': 'HCM T2', 'station_slot_key': 'MN:D-1:T2:TP. HCM'}`
- `H? N?i T2 context` -> `{'raw': 'H? N?i T2 context', 'canonical_station': 'H? N?i', 'weekday': 'T2', 'station_slot_key': 'MB:D-1:T2:H? N?i'}`
- `H? N?i T5 context` -> `{'raw': 'H? N?i T5 context', 'canonical_station': 'H? N?i', 'weekday': 'T5', 'station_slot_key': 'MB:D-1:T5:H? N?i'}`
- `DakLak` -> `{'raw': 'DakLak', 'canonical_station': '??k L?k', 'display_label': '??k L?k', 'station_slot_key': 'depends on source_region/source_offset/weekday'}`
