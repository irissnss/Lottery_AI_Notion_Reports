# V10630B Tomorrow Live Checkpoint Lock

| checkpoint | inspect | compute | decision |
|---|---|---|---|
| PRE_MN_BUNDLE | official MN BT/LO2; MN clean lane <=8; clone_official_flag; false_consensus_flag; selector_gap_flag | MN_PRE_BUNDLE_STATUS | WATCH_ONLY / CONFIRM_ONLY / RERANK_ONLY |
| POST_MN_RESULT | MN result closeout | would_save; would_break; false_promotion; net_effect | if net > 0 keep measuring no promotion; if net <= 0 tighten clean lane no promotion |
| PRE_MT_BUNDLE | official MT BT/LO2; 91/97 current support; conversion gate; FULL_SPENT/rerun dominance | MT_PRE_BUNDLE_STATUS | STRICT_SHADOW_BLOCK / BOOST_CONFLICT_REVIEW / CONFIRM_ONLY |
| POST_MT_RESULT | MT result closeout | lane win root cause; boost conflict; would_save/would_break/false_promotion/net_effect | no production hard-block |
| PRE_MB_BUNDLE | official MB; strategic rule fired rows; model diagnostic lane; high-support miss risk | MB_PRE_BUNDLE_STATUS | RULE_ONLY_READ_ONLY_MEASUREMENT |
| POST_MB_RESULT | MB result closeout | MB net_effect; false_promotion; high_support_miss | if net <= 0 keep freeze recommendation no provider/no wallet; if net > 0 read-only continue one more measurement |
| EOD_CLOSEOUT | EOD artifact closeout | public-safe summary if scan passes | do not include DB/raw/private traces |
