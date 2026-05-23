# V106.05 Public-Safe Owner Report: MT Target From MB D-1/D-2/D-3

This is a public-safe analytical report for AI/tool consultation. It contains derived metrics only. It does not include runtime DB, JSONL traces, logs, credentials, or deploy artifacts.


Live sync manifest: `artifacts/live_sync/20260523_223517/manifest.json`

Latest rerun status: PASS. Rerun after latest sync found 804 positive candidate rules; top global/scoped conclusions remained stable.

Scope: target is `MT D`. Source is only `MB_BOARD` at `D-1`, `D-2`, `D-3`. Source prizes are restricted to low-cardinality MB prizes:

- `DB#1`
- `G1#1`
- `G2#1`
- `G2#2`

This pass deliberately excludes broad selectors such as `G3_ALL`, `LOW_ALL`, `TOP3_PRIZES`, and `ALL_PRIZES` from boost conclusions.

## 1. Transform families tested

Each source number is converted into one exact 2-digit candidate using a named transform:

- `LAST2`: last two digits.
- `LAST2_REV`: reverse last two digits.
- `FIRST2`: first two digits.
- `FIRST2_REV`: reverse first two digits.
- `HEAD_TAIL`: first digit + last digit.
- `TAIL_HEAD`: last digit + first digit.
- `SUM_UNIT_PAIR`: unit digit of digit sum repeated as pair.
- `P{i}P{j}`: digit at source position i + digit at source position j.

Examples:

- MB DB `123456`, `HEAD_TAIL` -> `16`.
- MB DB `123456`, `TAIL_HEAD` -> `61`.
- MB DB `123456`, `P2P4` -> `24`.
- MB G2#1 `24688`, `P4P3` -> `86`.

## 2. Measurement definitions

For each rule:

- `hit_rate`: transformed tail appears in any MT prize on target date.
- `hit_base`: baseline from the number of unique MT tails on target date.
- `hit_lift_pp`: hit rate minus baseline.
- `db_day_rate`: transformed tail matches at least one MT station DB on target date.
- `db_day_lift_pp`: DB-day rate minus DB baseline.
- `stable_halves`: whether the rule remains positive in both halves of the window.

## 3. Best global MT rules from MB D-1/D-2/D-3

These apply to all MT target days, not restricted by weekday or station-set.

| Tier | Rule | Window | Days | Hit | Lift | DB day | DB lift | Note |
|---|---|---:|---:|---:|---:|---:|---:|---|
| A | `MB:G2#1:P4P1 D-1` | 90d | 90 | 50.0% | +14.9 pp | 6.7% | +4.2 pp | Best global stable candidate |
| A | `MB:G1#1:P5P2 D-1` | 90d | 90 | 46.7% | +11.6 pp | 7.8% | +5.4 pp | Good DB conversion |
| B | `MB:G2#1:P1P4 D-1` | 90d | 90 | 50.0% | +14.9 pp | 4.4% | +2.0 pp | Good source-pool, weaker DB |
| B | `MB:G2#1:P4P2 D-3` | 60d | 60 | 48.3% | +13.0 pp | 5.0% | +2.6 pp | Good medium-window candidate |
| B | `MB:G1#1:P5P3 D-3` | 90d | 90 | 46.7% | +11.6 pp | 4.4% | +2.0 pp | Secondary global |
| C | `MB:G1#1:SUM_UNIT_PAIR D-2` | 30d | 30 | 46.7% | +11.9 pp | 13.3% | +10.9 pp | Very interesting, short window only |
| C | `MB:DB#1:P2P4 D-1` | 30d | 30 | 53.3% | +18.6 pp | 6.7% | +4.2 pp | Strong 30d, needs longer verify |
| C | `MB:G2#1:FIRST2_REV D-2` | 30d | 30 | 53.3% | +18.6 pp | 6.7% | +4.2 pp | Same as `P2P1` |

Interpretation:

- The most useful global rule is not plain `MB DB LAST2`.
- The better global candidates are digit-position transforms from `MB G2#1` and `MB G1#1`.
- `MB G2#1 D-2 LAST2` is still useful, but it becomes more powerful when scoped to weekday/station-set.

## 4. Best scoped MT rules

These are stronger than global rules, but they are conditional. They must be used only when the matching weekday or MT station-set is present.

| Scope | Rule | Window | Days | Hit | Lift | DB day | DB lift | Use |
|---|---|---:|---:|---:|---:|---:|---:|---|
| CN | `MB:DB#1:P2P4 D-1` | 180d | 25 | 76.0% | +35.2 pp | 16.0% | +13.0 pp | Strong scoped shadow |
| CN | `MB:G2#1:P1P3 D-1` | 180d | 25 | 64.0% | +23.2 pp | 20.0% | +17.0 pp | Strong scoped shadow |
| T6 / `Gia Lai,Ninh Thuận` | `MB:G1#1:P4P1 D-3` | 180d | 25 | 60.0% | +29.5 pp | 12.0% | +10.1 pp | Strong scoped shadow |
| T5 / `Bình Định,Quảng Bình,Quảng Trị` | `MB:G1#1:SUM_UNIT_PAIR D-2` | 180d | 25 | 68.0% | +26.3 pp | 16.0% | +13.0 pp | Good but sum transform needs caution |
| T5 / same station-set | `MB:G2#1:P4P3 D-1` | 180d | 25 | 56.0% | +14.3 pp | 20.0% | +17.0 pp | Very practical scoped DB signal |
| T7 / `Quảng Ngãi,Đà Nẵng,Đắk Nông` | `MB:G2#1:LAST2 D-2` | 180d | 25 | 64.0% | +22.0 pp | 8.0% | +5.0 pp | Confirms owner intuition on G2 D-2 |
| T4 / `Khánh Hòa,Đà Nẵng` | `MB:G2#1:HEAD_TAIL D-2` | 180d | 25 | 52.0% | +22.0 pp | 8.0% | +6.0 pp | Useful transform of G2#1 |
| T6 / `Gia Lai,Ninh Thuận` | `MB:DB#1:P4P3 D-3` | 180d | 25 | 48.0% | +17.5 pp | 12.0% | +10.1 pp | DB special-prize transform |

Interpretation:

- Owner's observation about `MB D-1 DB` and `MB D-2 G1/G2` is correct, but the strongest form is usually not raw last-two only.
- For MT, the best rules are often weekday/station-set gated.
- `MB G2#1 D-2 LAST2` is especially relevant for `T7` / `Quảng Ngãi,Đà Nẵng,Đắk Nông`.

## 5. Practical shortlist

### Tier 1: implement in shadow first

1. `MB_G2_1_P4P1_D1_TO_MT_GLOBAL`
   - Source: MB `G2#1`, digit position 4 + digit position 1, lag D-1.
   - 90d global, 90 days, hit lift +14.9 pp, DB lift +4.2 pp.

2. `MB_G1_1_P5P2_D1_TO_MT_GLOBAL`
   - Source: MB `G1#1`, digit position 5 + digit position 2, lag D-1.
   - 90d global, hit lift +11.6 pp, DB lift +5.4 pp.

3. `MB_G2_1_LAST2_D2_TO_MT_T7_STATIONSET`
   - Source: MB `G2#1`, last two digits, lag D-2.
   - Scope: T7 / `Quảng Ngãi,Đà Nẵng,Đắk Nông`.
   - 180d scoped, hit lift +22.0 pp, DB lift +5.0 pp.

4. `MB_G2_1_P4P3_D1_TO_MT_T5_STATIONSET`
   - Source: MB `G2#1`, digit position 4 + digit position 3, lag D-1.
   - Scope: T5 / `Bình Định,Quảng Bình,Quảng Trị`.
   - 180d scoped, DB lift +17.0 pp.

### Tier 2: shadow but lower confidence

1. `MB_DB_1_P2P4_D1_TO_MT_CN`
   - Very high scoped hit, but weekday scoped only.

2. `MB_G1_1_SUM_UNIT_PAIR_D2_TO_MT_T5`
   - Strong, but digit-sum transforms are more data-snooping prone.

3. `MB_DB_1_P4P3_D3_TO_MT_T6`
   - Good DB conversion, but scoped only.

## 6. Model design recommendation

Module name:

`MT_MB_LOW_PRIZE_DIGIT_TRANSFORM_V1`

Shadow table:

`mt_mb_low_prize_digit_transform_shadow`

Mandatory columns:

- `target_date`
- `target_region='MT'`
- `target_weekday`
- `target_station_set`
- `source_region='MB'`
- `source_lag`
- `source_prize`
- `source_index`
- `source_number`
- `transform_name`
- `transformed_tail`
- `window_days`
- `hit_lift_pp`
- `db_day_lift_pp`
- `stable_halves`
- `rule_tier`
- `output_eligible=0`
- `diagnostic_only=1`

Scoring rule:

- Global Tier A can add source-pool score, not final boost.
- Scoped Tier shadow can add score only when weekday/station-set matches.
- No rule can directly choose final BT alone.
- Require agreement from at least two independent rules or one rule plus existing no-token strength layer.

## 7. Deployment guard

Do not promote to official from this backtest. This pass searched many transforms. To avoid data-snooping:

1. Run daily shadow for 14 days.
2. Track:
   - transformed tail appears in MT any prize,
   - transformed tail hits MT DB,
   - false promotion,
   - would-save / would-break compared with current test-lane baseline.
3. Only consider promotion if:
   - 14d live net positive,
   - no official winner would be broken in simulation,
   - at least 2 independent rule families agree on the same tail.

## 8. Bottom line

There are stronger MT-specific situations than the previous broad scan:

- `MB G2#1 D-2` is valid, especially for T7 / `Quảng Ngãi,Đà Nẵng,Đắk Nông`.
- `MB DB D-1` is valid in transformed form, especially `P2P4` on CN.
- `MB G1 D-1/D-2/D-3` has real value, especially `P5P2`, `P4P1`, `SUM_UNIT_PAIR` under scoped conditions.

Best next step: implement `MT_MB_LOW_PRIZE_DIGIT_TRANSFORM_V1` as measurement-only shadow.
