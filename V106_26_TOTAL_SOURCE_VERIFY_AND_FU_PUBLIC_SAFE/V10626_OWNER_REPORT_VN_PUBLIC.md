# V10626 — Total Source Rule Verification & Pre-Register Gate

> Phien ban: V20.3.37.106.26 | Generated: 2026-05-24T22:21:22
> Locked manifest: `artifacts/live_sync/20260524_221208/manifest.json`
> DB sha256: `dc3cfc95ae381786818df29062bd5c323a1a5d78224edfa609ca1929cd88f219`
>
> Muc dich: VERIFY toan bo source->target rule da bao cao trong V10603/V10605/V10606/V107. Khong mine moi, khong applied live, khong promote, khong sua official.

## 1. Co phai chi check MB->MT khong?

KHONG. Full coverage 3x3 target x source da chay:

| Target | Source MB | Source MN | Source MT (self / cross) |
|---|---:|---:|---:|
| MT | 8747 | 8274 | 0 (self) |
| MN | 9441 | 0 (self) | 7519 |
| MB | 7771 (self) | 7512 | 6282 |

Tong rule inventory: **55546** (lineage day du). Rejected (broad/no-lineage): **0**.

Ghi chu: MN-self = 0, MT-self = 0 vi V10606 deep mining khong include same-region station-source for non-MB. Chi MB-self co (MB_BOARD self-lag). Day la limitation cua V10606 mining va se can rieng pass moi cho MN-self / MT-self neu owner muon.

## 2. MT nguon nao manh nhat sau verify?

Theo coverage matrix:

| Source | Total | Verified | Best lift_pp | Best DB lift_pp | Tier A count |
|---|---:|---:|---:|---:|---:|
| MB | 8747 | 7223 | 38.85 | 21.08 | 329 |
| MN | 8274 | 5061 | 61.42 | 23.0 | 154 |
| MT | 0 | 0 | N/A | N/A | 0 |

**Ket luan rieng MT**:
- **MN->MT** co best lift cao nhat (+61.4pp) nhung scoped sample chi 12-26 ngay - SELECTION_BIAS_RISK.
- **MB->MT** co volume lon nhat (8747 rules, 329 Tier A) va verified backtest cao (7223).
- **MT-self** chua co rule trong V10606 inventory - can pass rieng neu owner muon.
- TUY NHIEN: tat ca deu PRE_REGISTER_ONLY vi V107 verdict mostly selection bias.

## 3. Rule research-only la nhung gi?

Toan bo **55546 rules** trong inventory deu RESEARCH_ONLY hoac PRE_REGISTER_ONLY. 
Khong rule nao co status COMMIT_ELIGIBLE_SHADOW / OUTPUT_ELIGIBLE / PROMOTION_READY.

Breakdown theo source artifact:

| Artifact | Count |
|---|---:|
| V10605 | 120 |
| V10606 | 54924 |
| V107_PANEL | 498 |
| V10603 | 4 |

## 4. Rule eligible pre-register la nhung gi?

Da chon **58 entries** vao pre-register panel (cap theo spec):

| Panel | Size | Cap |
|---|---:|---:|
| MT | 20 | 20 |
| MN | 15 | 15 |
| MB | 15 | 15 |
| Controls | 3 | 10 |
| Negative controls | 5 | 5 |

Tat ca entries: status=`PRE_REGISTER_ONLY`, live_eligible=`False`. Chi tiet tung panel tai:
- `V10626_PRE_REGISTER_PANEL_MT.{csv,json,md}`
- `V10626_PRE_REGISTER_PANEL_MN.{csv,json,md}`
- `V10626_PRE_REGISTER_PANEL_MB.{csv,json,md}`
- `V10626_PRE_REGISTER_PANEL_SUMMARY.{json,md}`

## 5. Rule rejected/quarantined boi V107

**55546** rules thua huong BH_FAIL_GLOBAL + SELECTION_BIAS_RISK + FORWARD_90D_INSUFFICIENT + PRE_REGISTER_ONLY. 
Day la ket qua truc tiep cua V107 verdict:

- 0/153,228 V10606 rules survived BH q<0.05 within family.
- Sub-sample replication odd/even DOY below independence.
- Forward 90d window chua co (V10603 only 2 days).

Risk distribution:

| Risk | Count |
|---|---:|
| BH_FAIL_GLOBAL | 55546 |
| SELECTION_BIAS_RISK | 55546 |
| PRE_REGISTER_ONLY | 55546 |
| FORWARD_90D_INSUFFICIENT | 55546 |
| SMALL_SAMPLE_RISK | 1540 |
| REPLICATION_FAIL_RISK | 5969 |

## 6. Co rule nao applied official khong?

**KHONG.** Cu the:
- official_mutation = 0
- provider_manual_ai_call = 0
- wallet = 0
- lane_promotion = 0
- production_prompt_switch = 0
- production_selector/scoring/voting/roster_switch = 0
- public_push = NO
- cron_install = 0
- live_candidate_generation = 0
- board_application = 0
- production_hard_block = 0
- broad_selector_used = 0
- db_hash_unchanged_mid_pass = True
- strict_official_drift_detected = False

## 7. Buoc an toan ngay mai live la gi?

1. **GIU NGUYEN V10622 workflow** - hien tai van la operational baseline an toan.
2. **Khong promote** bat ky V10626 panel rule nao len official.
3. **Tuy chon** anh OK thi luu pre-register panel V10626 vao file da timestamp (chinh la output cua pass nay) de sau 90 ngay (uoc tinh ~2026-08-22) chay forward audit voi BH correction tren chinh xac panel da khoa.
4. **Khong mine moi** bat ky source rule moi nao cho den khi forward 90d evidence co.
5. Tiep tuc V10622_PARALLEL_LIVE_RERUN.py o cac moc live nhu cu, **read-only**.

## 8. Owner decisions can quyet

- (A) Lock V10626 pre-register panel hom nay lam baseline 90-day audit? Default: chua quyet.
- (B) Public push V10626 package? Default: NO (per HARD LOCK).
- (C) Mo rong inventory bao gom MN-self / MT-self? Default: chua quyet, can pass moi.
- (D) Co thay doi V10622 operational workflow khong? Default: NO.

## 9. Output artifacts

Trong `artifacts/v106_26_total_source_rule_verification/`:
- `V10626_PHASE0_SOURCE_PACKAGE_VERIFY.{json,md}`
- `V10626_TOTAL_RULE_INVENTORY.{csv,json,md}`
- `V10626_REJECTED_NO_LINEAGE_RULES.csv`
- `V10626_TARGET_SOURCE_COVERAGE_MATRIX.{csv,json,md}`
- `V10626_MT_SOURCE_VERIFY_{MB_TO_MT,MN_TO_MT,MT_SELF}.{csv,json,md}`
- `V10626_MN_SOURCE_VERIFY.{json,md}` + per-source breakdown
- `V10626_MB_SOURCE_VERIFY.{json,md}` + per-source breakdown
- `V10626_V107_RISK_OVERLAY.{json,md}`
- `V10626_PRE_REGISTER_PANEL_{MT,MN,MB,SUMMARY}.{csv,json,md}`
- `V10626_ZERO_OFFICIAL_DRIFT_PROOF.{json,md}`
- `V10626_SAFETY_GATE.{json,md}`
- `V10626_OWNER_REPORT_VN.md`
- `V10626_EXECUTION_SUMMARY.json`
