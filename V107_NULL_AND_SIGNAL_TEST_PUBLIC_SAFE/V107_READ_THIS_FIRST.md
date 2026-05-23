# V107 Read This First

V107 is a null-hypothesis stress test on the V106.x rule discovery framework.

Aggregate verdict: WEAK SIGNAL / mostly selection bias.

Critical findings:
- Null Test 3 (multiple-testing): 0/153228 rules survive BH q<0.05 within family.
- Null Test 4 (replication): 65.3% rate_both observed vs 67.4% expected under independence.
- Null Test 5 (forward): forward 90d window has not yet elapsed (V106.05 published 2026-05-23).

Recommendation: pre-register a panel of <50 rules NOW, do not promote any V106.05/06 rules, wait actual 90 days, then evaluate with strict multiple-testing correction.

No DB / JSONL / log / runtime artifact in this public package.
