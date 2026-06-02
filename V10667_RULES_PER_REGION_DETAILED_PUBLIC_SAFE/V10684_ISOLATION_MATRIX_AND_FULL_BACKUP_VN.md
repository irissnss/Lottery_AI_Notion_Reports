# V10684 — Isolation MN/MT (cả official + lane test) + Backup đầy đủ

> **Generated**: 2026-06-03 01:50 VN
> **Trigger**: Owner: "MN và MT của cả 2 luồng lane test và official cũng cần phải cô lập, backup đầy đủ".
> **Trạng thái**: REPORT-ONLY. **18/18 PASS**. Không deploy code, không đụng official.

---

## 0. Trả lời nhanh

| Câu hỏi | Trả lời |
|---|---|
| MN/MT đã cô lập trong **official** chưa? | ✅ Có. 108/108 chữ ký bất biến. |
| MN/MT đã cô lập trong **lane test** chưa? | ✅ Có. 2 engine multi-region KHÔNG đọc/ghi symbol MB-only. |
| Backup đầy đủ chưa? | ✅ Có. 5 file code `.v10684.pre` + 11 file ref + 22 bảng DB snapshot + 4 official table hash baseline. |

---

## 1. Hai luồng MB hiện tại (làm rõ cấu trúc)

### Luồng 1 — OFFICIAL
- `predictions` ← model outputs (TOKEN: 17:42 AI MB; NO_TOKEN: 04:00 free predict)
- `extract_rule_candidates_v2('MB', ...)` → boost từ T1 production
- `final_bundles` ← `generate_final_bundle('MB', ...)` (BT/lo2/xien2/xien3)
- UI `/du-doan` đọc `final_bundles`

### Luồng 2 — LANE TEST
Có **2 engine** chạy song song:

| Engine | Quy mô | File |
|---|---|---|
| Multi-region engine | MN + MT + MB | `_materialize_experimental_preview_shadow.py` + `_du_doan_test_engine.py` |
| MB-legacy engine | Chỉ MB | `_materialize_mb_experimental_preview_shadow.py` + `_du_doan_test_mb_engine.py` |

Cả 2 ghi vào `mb_experimental_preview_shadow` (MB-only) hoặc `experimental_preview_shadow` (multi) → `du_doan_test_*`. UI `/du-doan-test` đọc từ đó.

**Không file nào** trong luồng lane test gọi `generate_final_bundle()` hay ghi `predictions/final_bundles/lottery_results/model_daily_eval`.

---

## 2. Isolation matrix (18 check, 18 PASS)

### A. Static — multi-region engines KHÔNG đụng symbol MB-only

| Engine | Symbol leak |
|---|---|
| `_materialize_experimental_preview_shadow.py` | ✅ 0 leak |
| `_du_doan_test_engine.py` | ✅ 0 leak |
| `_du_doan_test_daily_runner.py` | ✅ 0 leak |

Symbol kiểm tra: `mined_rules_mb_daily`, `mb_rule_context`, `mb_t2_manual_daily`, `mb_t3_prereg_daily`, `mb_rule_ranker`, `MB_DAILY_RANK_ENABLE`, `_get_mb_daily_rules`, `_build_mb_layered_section`, `MB_EXPERT_DOCTRINE`.

### B. Static — MB-only path KHÔNG ghi MN/MT

| Check | Kết quả |
|---|---|
| `mb_rule_ranker` chỉ INSERT vào `mb_*` tables | ✅ |
| `_build_mb_layered_section` không cross-write MN/MT | ✅ |
| `rule_engine` MB-daily branch gated bởi `target_region=='MB' and MB_DAILY_RANK_ENABLE` | ✅ |

### C. Runtime — Harness MN/MT 108/108 IDENTICAL

`_mn_mt_invariance_harness.py check`: PASS — 108/108 chữ ký giống baseline (frozen DB + PYTHONHASHSEED=0).

### D. DB — mined_rules MN/MT bất biến

| Check | Kết quả |
|---|---|
| `mined_rules` MN count = 35 (== backup) | ✅ |
| `mined_rules` MT count = 35 (== backup) | ✅ |
| MN row hash IDENTICAL | ✅ |
| MT row hash IDENTICAL | ✅ |

### E. 4 official tables hash zero-drift

| Table | Hash IDENTICAL với backup |
|---|---|
| `predictions` | ✅ `4ceeee330fd6a0d7...` |
| `final_bundles` | ✅ `dac6a8edb5a280a1...` |
| `lottery_results` | ✅ `25812b7e5fd2a895...` |
| `model_daily_eval` | ✅ `cdb87e4448b123ba...` |

### F. Lane test multi-region engine sanity

| Check | Kết quả |
|---|---|
| Import `_materialize_experimental_preview_shadow` | ✅ |
| Import `_du_doan_test_engine` | ✅ |
| Engine `SUPPORTED_REGIONS == ('MN','MT','MB')` | ✅ |

→ **Tất cả 18 PASS**. MN/MT cô lập tự nhiên ở **cả 2 luồng** vì code MB-only của em chỉ chạm tables/symbols `mb_*` đặt riêng.

---

## 3. Backup V10684 — đầy đủ

### 3.1 Vị trí

```
backups/v10684_full_isolation_backup_20260603_014605/
├── MANIFEST.json                              # restore instructions + all hashes
├── code/                                      # 5 file MB đã sửa, .v10684.pre
│   ├── rule_engine.py.v10684.pre
│   ├── gpt_analyzer.py.v10684.pre
│   ├── prompt_registry.py.v10684.pre
│   ├── scheduler.py.v10684.pre
│   └── mb_rule_ranker.py.v10684.pre
└── code_ref/                                  # 11 file official-critical (read-only ref)
    ├── main.py.ref
    ├── database.py.ref
    ├── _seed_rules.py.ref
    ├── weekly_rule_miner.py.ref
    ├── mined_rule_eval.py.ref
    ├── _materialize_experimental_preview_shadow.py.ref
    ├── _materialize_mb_experimental_preview_shadow.py.ref
    ├── _du_doan_test_engine.py.ref
    ├── _du_doan_test_mb_engine.py.ref
    ├── _du_doan_test_schema.py.ref
    └── _du_doan_test_daily_runner.py.ref
```

### 3.2 Bảng DB snapshot trong cùng DB (`_bak_v10684_*`)

#### Official (8 bảng)
| Bảng | Rows | sha256 |
|---|---:|---|
| `mined_rules` | 105 | `43c82c8cb31787f4...` |
| `mined_rule_effectiveness` | 2332 | `816cf0d36636b8ab...` |
| `mining_log` | 24 | `29206a4b1a4f36c1...` |
| `predictions` | 6612 | `4ceeee330fd6a0d7...` |
| `final_bundles` | 285 | `dac6a8edb5a280a1...` |
| `lottery_results` | 14799 | `25812b7e5fd2a895...` |
| `model_daily_eval` | 6476 | `cdb87e4448b123ba...` |
| `prediction_policies` | 6 | `603d8ce5af46bf8d...` |

#### MB-only (5 bảng)
| Bảng | Rows |
|---|---:|
| `mined_rules_mb_daily` | 70 |
| `mb_t2_manual_daily` | 150 |
| `mb_t3_prereg_daily` | 38 |
| `mb_rule_context` | 4 |
| `mb_rerank_log` | 5 |

#### Lane test (9 bảng)
| Bảng | Rows |
|---|---:|
| `mb_experimental_preview_shadow` | 231 |
| `experimental_preview_shadow` | 2015 |
| `du_doan_test_runs` | 1748 |
| `du_doan_test_bundles` | 1748 |
| `du_doan_test_results` | 1748 |
| `du_doan_test_experiments` | 31 |
| `du_doan_test_audit_log` | 514 |
| `du_doan_test_model_contribution` | 36881 |

### 3.3 Restore instructions (trong `MANIFEST.json`)

```
code:        copy backups/.../code/*.v10684.pre back to web/backend/ (strip suffix)
db_table:    INSERT INTO <table> SELECT * FROM _bak_v10684_<table>
flag_off:    set MB_DAILY_RANK_ENABLE = False in rule_engine.py
cron_remove: remove auto_mb_rule_rerank + auto_mb_rule_guard jobs from scheduler.py
```

---

## 4. Tóm tắt logic isolation MN/MT trong cả 2 luồng

### Luồng OFFICIAL — MN/MT cô lập vì
- `extract_rule_candidates_v2` chỉ chạy nhánh MB-daily khi `target_region=='MB' and MB_DAILY_RANK_ENABLE`. Với `'MN'` hoặc `'MT'`, đường code này KHÔNG chạy → MN/MT đọc `mined_rules` thẳng như cũ.
- `build_context_pack` chỉ chèn `_build_mb_layered_section` + `MB_EXPERT_DOCTRINE` khi `target_region=='MB'`. MN/MT prompt giữ nguyên.
- `mb_rule_ranker` chỉ ghi vào `mb_*` tables, không bao giờ chạm `mined_rules` chung.
- Cron mới (`auto_mb_rule_rerank`, `auto_mb_rule_guard`) chỉ chạy MB ranker — không gọi gì MN/MT.

### Luồng LANE TEST — MN/MT cô lập vì
- `_materialize_experimental_preview_shadow.py` (multi-region) **0 ref** đến symbol MB-only.
- `_du_doan_test_engine.py` (multi-region) **0 ref** đến symbol MB-only.
- `_du_doan_test_daily_runner.py` chỉ phối logic theo `region` arg, **0 ref** đến symbol MB-only.
- `_materialize_mb_experimental_preview_shadow.py` + `_du_doan_test_mb_engine.py` (MB-legacy) hard-coded `REGION='MB'` → không thể chạy cho MN/MT.

→ Khi anh OK code experiment T2-drive (V10683), em sẽ làm **chỉ trong file mới** `_v10683_mb_t2_drive_shadow.py` + thêm 1 dòng vào registry MB; **không sửa** bất cứ file multi-region nào → MN/MT trong lane test cũng tiếp tục bất biến.

---

## 5. Verify đã làm

| Mục | Tool / kết quả |
|---|---|
| Static code grep | 7 check PASS |
| Runtime harness MN/MT | 108/108 IDENTICAL |
| DB MN/MT count + hash | 4 check PASS |
| 4 official tables hash | 4 check PASS (zero-drift) |
| Lane test multi-region import | 3 check PASS |
| **Tổng** | **18/18 PASS** |

Script: `artifacts/v107_mb_independent/scripts/_v10684_isolation_matrix.py`
Backup script: `artifacts/v107_mb_independent/scripts/_b0_full_backup_v10684.py`

---

## 6. Trạng thái

| Hạng mục | Status |
|---|---|
| Code deploy VPS | NO |
| Official mutation | NO |
| MN/MT bất biến (official) | PROVEN |
| MN/MT cô lập (lane test) | PROVEN (static + runtime) |
| Backup full | DONE (`v10684_full_isolation_backup_20260603_014605`) |
| Public report | sẽ push |
| V10683 plan | đã push, awaiting owner choice |

---

**Bottom line**: Anh yên tâm. MN/MT cô lập ở cả 2 luồng, có bằng chứng 18/18 + backup đầy đủ có thể restore mọi điểm. Khi anh OK V10683, em làm chỉ trong file mới — không thể vô tình ảnh hưởng MN/MT.
