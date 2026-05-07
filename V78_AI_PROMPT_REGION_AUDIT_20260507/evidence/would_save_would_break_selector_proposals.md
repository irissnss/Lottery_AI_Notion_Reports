# Would-save / Would-break Selector Proposals — V78

| proposal | 4d_effect | classification | reason |
| --- | --- | --- | --- |
| MN prefer V67 when V67 fires and official/AI herd disagrees | Would save 2026-05-07 MN; no observed break in 4d because V67 only emitted 1 row | WAIT_7D_LIVE | Positive but sample n=1 for current live config |
| MB all-method cold diversification prompt | No selector method would save MB 4d; prompt should report low confidence | IMPLEMENT_NOW_TEST_LANE_ONLY | Shadow prompt/audit only, no official selector change |
| MT consensus-first hard preference | V70/V73 4/4 after V77 timing fix | KEEP_CURRENT | Do not disturb MT |
| Independent cluster consensus | Needed because raw agreement can be clones; not enough data | WAIT_14D_FRESH_EVIDENCE | Requires cluster lineage metric |

No selector change was promoted in V78. Only shadow prompts + shadow audit tables were implemented.
