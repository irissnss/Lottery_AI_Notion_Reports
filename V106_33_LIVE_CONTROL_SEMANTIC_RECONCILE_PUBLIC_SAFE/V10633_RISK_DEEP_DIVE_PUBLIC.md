# V10633 Risk Deep Dive Public

| risk | impact | missing_proof | verify_2705 | allowed_now | owner_gated |
|---|---|---|---|---|---|
| MN TOTAL_OUTPUT_ONLY | official hit source not proven independent | independent live proof from clean lane | compare clean lane vs official, clone rate, net | maintain clean lane only | production change |
| MT TOTAL_OUTPUT_ONLY | official hit but conversion gate not proven | 91/97 current support + conversion net after live | check 91/97, FULL_SPENT, rerun_post_mn dominance | shadow conversion gate only | production hard-block |
| Public/private proof risk | public package cannot substitute private code verification | private code inspection for implementation claims | private-only code review if needed | report-only evidence | public code disclosure |
