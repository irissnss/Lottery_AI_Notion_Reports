# V106.28R0A Master Issue Matrix Public

| issue_id | region | severity | status | root_cause | safe_action_now | blocked_action | owner_gate | next_checkpoint |
|---|---|---|---|---|---|---|---|---|
| P0-V10628R0A-NOT-RUN-BEFORE | ALL | P0 | OPEN | V10628R0A not run before this pass | RUN_NOW | claim prior run | none | this pass |
| P0-LABEL-CONFUSION-V10629 | ALL | P0 | OPEN | V10629 public-safe was mistaken risk for total pass | label truth lock | claim V10629 total consolidation | none | every conclusion |
| P0-SCHEMA-EXTRACTOR-GATE | ALL | P0 | OPEN | Rule import blocked until schema/extractor audit safe | block import | run V10628R1/rule import | owner+schema gate | separate audit close |
| P0-V108-BACH-THU-BLOCKER | ALL | P0 | OPEN | V108 phase2 blocked by lane table bach_thu query | separate code fix | use V108 as proof | owner separate code pass | V108 fix |
| P0-PUBLIC-LATEST-READ-FIRST | ALL | P0 | OPEN | Public latest must be read before conclusions | always verify LATEST_REPORT | stale pointer claims | none | session start |
| P0-NO-LIVE-ELIGIBLE-FU4 | ALL | P0 | OPEN | FU4 has 13 stable pre-register but live_eligible=0 | watch/forward audit | apply live | 90d owner gate | 2026-08-23 |
| P0-OFFICIAL-MUTATION-FORBIDDEN | ALL | P0 | OPEN | Official mutation remains forbidden | artifact only | mutate official | owner explicit only | always |
| P1-MT-91-SELECTOR-GAP | MT | P1 | OPEN | 91 can hit diagnostically but not reliably committed | SHADOW_GATE_ONLY | production hard-block | owner gate | 3/7/14d |
| P1-MT-60-FULL-SPENT | MT | P1 | OPEN | 60 FULL_SPENT/rerun_post_mn dominance failed | BOOST_CONFLICT_REVIEW | selector switch | owner gate | next MT closeout |
| P1-MT-LO2-BT-WRONG | MT | P1 | OPEN | LO2 present but BT wrong conversion | CONFIRM_ONLY | exact BT confirm production | owner gate | next MT |
| P1-MT-GATE-NEGATIVE | MT | P1 | OPEN | MT conversion gate 3/7/14d net negative | STRICT_SHADOW_BLOCK | promotion | owner gate after evidence | 7/14/30d |
| P1-MN-MB-G2-D123-WATCH | MN | P1 | OPEN | MB-G2 D1/D2/D3 useful only confirm/rerank/watch | WATCH_ONLY/RERANK_ONLY | force BT/LO2 | owner gate | next MN |
| P1-MN-PAIR-BREAK-RISK | MN | P1 | OPEN | MN pair rules can break official partial | WATCH_ONLY | force pair | owner gate | next MN |
| P1-MB-AICHAIN-MISS | MB | P1 | OPEN | MB high AI-chain support miss | READ_ONLY | wallet/expansion | owner gate | next MB |
| P1-BOARD-LOCAL-ONLY | ALL | P1 | OPEN | V10622/V10625 board local/artifact only without deploy | LOCAL_ARTIFACT_ONLY | claim deployed | owner deploy approval | deploy gate |
| P1-MANUAL-NO-CRON | ALL | P1 | OPEN | Manual checkpoints only; cron not installed | manual runbook | install cron | owner approval | tomorrow |
| P2-CP66-OVERDUE | ALL | P2 | OPEN | CP-66.7/CP-66.8 overdue/wait rows | surface reminder | ignore | owner no action | 2026-06-03 |
| P2-V10614-INCOMPLETE | ALL | P2 | OPEN | V10614 closure incomplete historical tracker | track | claim closed | none | future |
| P2-UI-SEMANTICS | ALL | P2 | OPEN | UI semantics gap around official/lane/shadow | read-only board proposal | deploy without owner | owner deploy | future |
| P2-PUBLIC-PRIVATE-DRIFT | ALL | P2 | OPEN | Public/private docs drift risk | sync report | stale public pointer | none | each publish |
| P2-DIRTY-REPO-HYGIENE | ALL | P2 | OPEN | Repo dirty state is large | commit only scoped files | hide dirty state | none | this commit |
