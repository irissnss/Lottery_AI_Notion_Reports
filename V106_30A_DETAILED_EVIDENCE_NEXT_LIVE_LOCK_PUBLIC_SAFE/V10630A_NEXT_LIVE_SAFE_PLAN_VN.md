# V10630A Next Live Safe Plan VN

| checkpoint | inspect | command |
|---|---|---|
| Pre-MN bundle | official vs MN clean signal vs MN shadow; clone_official_flag; false_consensus | read V10630_MN_* artifacts |
| Post-MN result | would_save/would_break/false_promotion/net_effect | refresh scorecard artifact-only |
| Pre-MT bundle | 91/97 support; conversion gate; FULL_SPENT | read V10630_MT_* artifacts |
| Post-MT result | lane win root cause; boost conflict | refresh MT scorecard |
| Pre-MB bundle | strategic rule fired rows; model diagnostic; high-support miss risk | read V10630_MB_* artifacts |
| Post-MB result | MB net_effect; cost kill gate | refresh MB cost gate |
| EOD | public-safe report if scan passes | artifact-only publish |

Owner decisions:
| decision | default | recommendation |
|---|---|---|
| freeze_mb_ai_model | OWNER_GATE_REQUIRED | True |
| deploy_read_only_board | NO | False |
| continue_one_more_live | YES_FOR_MEASUREMENT_ONLY | True |
| run_v10628r1 | NO | False |
