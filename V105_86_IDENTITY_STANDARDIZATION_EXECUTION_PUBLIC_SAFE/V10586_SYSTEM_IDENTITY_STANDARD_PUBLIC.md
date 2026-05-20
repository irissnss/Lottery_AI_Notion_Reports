# System Identity Standard

Updated: `2026-05-20T11:07:44+07:00`

## Core Fields
- `canonical_station`: Canonical station name used for DB lookup/grouping; never includes weekday/source_offset.
- `station_alias_raw`: Original raw station spelling; audit/trace only.
- `station_slot_key`: region:source_offset:weekday:canonical_station for rule/source identity.
- `display_label`: Human UI label, e.g. HCM T2; never use for DB lookup.
- `region`: Target region unless explicitly named source_region.
- `source_region`: Region of source result/rule input.
- `target_region`: Region being predicted/evaluated.
- `weekday`: Canonical weekday code T2/T3/T4/T5/T6/T7/CN.
- `source_weekday`: Weekday of source result after source_offset resolution.
- `target_weekday`: Weekday of target prediction date.
- `source_offset`: D, D-1... used to resolve source_date.
- `station_set_canonical_json`: JSON array of canonical_station values.
- `station_set_display`: UI-only display string.
- `source_prize_keys`: Rule prize keys such as GĐB+G7, resolved through prize-key aliases.

## Ownership
- **DB lookup**: Use canonical_station only; raw aliases are read-time compatibility candidates.
- **Rule identity**: Use station_slot_key.
- **UI**: Use display_label; raw stays in diagnostic.
- **Prompt**: Patch only after owner OK; must include canonical_station + display_label + source_offset + weekday.
- **ML feature key**: station_slot_key for source/rule-specific features; canonical_station for station-level features.
- **Trace**: Future additive raw + canonical + slot fields only; V105.86 does not mutate history.
- **raw_value**: Audit-only.
- **display_label**: Never use as lookup key.

## Examples
- `TP. TP. HCM` -> canonical_station=`TP. HCM`, display_label=`HCM T2`, station_slot_key=`MN:D-1:T2:TP. HCM`
- `Hà Nội T2 context` -> canonical_station=`Hà Nội`, display_label=``, station_slot_key=`MB:D-1:T2:Hà Nội`
- `Hà Nội T5 context` -> canonical_station=`Hà Nội`, display_label=``, station_slot_key=`MB:D-1:T5:Hà Nội`
- `DakLak` -> canonical_station=`Đắk Lắk`, display_label=`Đắk Lắk`, station_slot_key=`depends on source_region/source_offset/weekday`
