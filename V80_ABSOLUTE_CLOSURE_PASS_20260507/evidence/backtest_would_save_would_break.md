# Accuracy Gap Priority Matrix

| Gap | Evidence | Region | Risk | Suggested fix | Shadow/test only |
| --- | --- | --- | --- | --- | --- |
| AI herd wrong MN | 94 miss vs V67/V73 95 hit | MN | HIGH | V79 cluster-weight + V80 MN monitor | YES |
| MB all-method cold | official/test 0/N | MB | HIGH | V80 MB regime monitor | YES |
| No-token underweighted | NO_TOKEN >= TOKEN in recent window | MN/MB/MT | HIGH | V79 no-token floor | YES |
| Rule-phase delivery incomplete | Notion doctrine ahead | ALL | MEDIUM | V80 rule_phase_synthesis_shadow | YES |
| No-token rule pack missing | No production feature pack | ALL | MEDIUM | V80 no_token_rule_aware_pack_shadow | YES |
| Timezone HCM risk | V77 datetime.now(VN_TZ string) bug | ALL | HIGH | helpers + ongoing audit | YES |
