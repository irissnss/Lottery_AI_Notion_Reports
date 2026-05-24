# V106.26 Methodology

Locked live sync: `artifacts/live_sync/20260524_221208/manifest.json`.
DB source: live-synced from VPS. Read-only.

## Total verify scope (main V10626)
- Inventoried 55,546 rules with exact lineage from V10603/V10605/V10606/V107 panel.
- Coverage matrix 3x3 target x source (MN/MT/MB).
- Pre-register panels: MT max 20, MN max 15, MB max 15, controls 10, negative 5.

## FU1 — MB DB D-2 hypothesis verify
- H1 LOOSE: LAST2(MB DB D-2) appears in any MB prize D.
- H2 STRICT: LAST2(MB DB D-2) equals MB DB D directly.
- Outcome: NOT verified (-0.4pp to +1pp lift across windows).

## FU2 — Comprehensive cross-source scan
- Self-lag + cross-region MB_BOARD + cross-region top-6 MN/MT stations.
- Detected schema inconsistency: ~8% MN/MT rows have JSON key order swapped (G8 first vs DB first).

## FU3 — Schema-safe key-name extractor (CORRECTED)
- Replaced positional access with Vietnamese key-name lookup.
- Extended low-cardinality prizes: MB (DB/G1/G2#1/G2#2), MN/MT (G8/G7/G5/G2/G1/DB).
- 12,966 positive rules across 3 targets.
- Top finding: `MT<-MT:Đà Nẵng:G1#1:P3P4:D-2` H1 +14.7pp + H2 +9.80pp.

Transforms tested: LAST2, LAST2_REV, FIRST2, FIRST2_REV, HEAD_TAIL, TAIL_HEAD, HEAD_SECOND_LAST, SECOND_HEAD_TAIL, all P{i}P{j} pairs.
Lags: D-1..D-7, W-1..W-4. Windows: 60, 90, 180.

V107 risk overlay applies to every rule: BH_FAIL_GLOBAL + SELECTION_BIAS_RISK + FORWARD_90D_INSUFFICIENT. PRE_REGISTER_ONLY status. live_eligible = False.

Public-safe constraints: no DB, no JSONL, no log, no runtime artifact, no secrets.
