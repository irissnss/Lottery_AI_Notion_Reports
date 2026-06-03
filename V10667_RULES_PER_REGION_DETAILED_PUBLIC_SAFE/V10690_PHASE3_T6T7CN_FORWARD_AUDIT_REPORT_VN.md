# V10690 — PHASE 3: T6/T7/CN B+A (9 STRONG forward-audit, CONFIRM-only) → CỔNG 3 XANH

> **Generated**: 2026-06-03 14:00 VN | **Phase**: 3/5 | **Cổng**: 🟢 XANH 16/16
> **Phạm vi**: code + verify LOCAL. CHƯA deploy VPS. Official KHÔNG đụng.

---

## 0. Việc Phase 3 đã làm (owner: T6/T7/CN = B+A)

Nạp **9 ứng viên STRONG** (V10687, T6/T7/CN) vào pool MANUAL với vai trò **CONFIRM-only forward-audit**:
- `role = CONFIRM_ONLY`, `live_eligible = False`, `drive_weight = 0`
- `status = PRE_REGISTER_FORWARD_AUDIT` (90d, tới ~2026-08-31)
- `SELECTION_BIAS_RISK = True`, **KHÔNG gắn gold/BH-pass**

Tích hợp vào ranker (`mb_rule_ranker._rerank_tier2`) để tồn tại mỗi ngày: T2 pool 77 → **86** (77 driving + 9 forward-audit). V10689 **ép drive_weight=0** cho rule `confirm_only`. V10690 **loại** rule `confirm_only` khỏi driver (bảo vệ kép).

---

## 1. 9 ứng viên forward-audit

| Thứ | Lineage | Lift (dig) | drive_weight | confirm_only | role |
|---|---|---:|---:|:---:|---|
| T6 | `MN:G1#1:FIRST2:D-4` | +10.9pp | 0 | ✅ | CONFIRM forward-audit |
| T6 | `MT:DB#1:FIRST2:D-6` | +8.73pp | 0 | ✅ | CONFIRM forward-audit |
| T6 | `MN:G7#1:LAST2:D-4` | +8.55pp | 0 | ✅ | CONFIRM forward-audit |
| T7 | `MB:G6#3:LAST2:D-7` | +7.27pp | 0 | ✅ | CONFIRM forward-audit |
| T7 | `MT:G5#1:HEAD_TAIL:D-4` | +7.2pp | 0 | ✅ | CONFIRM forward-audit |
| T7 | `MN:G2#1:LAST2:D-5` | +6.63pp | 0 | ✅ | CONFIRM forward-audit |
| CN | `MN:G2#1:HEAD_TAIL:D-2` | +9.45pp | 0 | ✅ | CONFIRM forward-audit |
| CN | `MT:G7#1:HEAD_TAIL:D-7` | +8.64pp | 0 | ✅ | CONFIRM forward-audit |
| CN | `MB:G7#2:LAST2:D-7` | +6.65pp | 0 | ✅ | CONFIRM forward-audit |

---

## 2. CỔNG 3 — kết quả (16/16 PASS)

| Nhóm kiểm tra | Kết quả |
|---|---|
| 9 row present, drive_weight=0, confirm_only=1, live_eligible=0, bh_pass=0 | 🟢 9/9 |
| V10690 `_load_manual_rules` LOẠI hết 9 confirm_only khỏi driver (T6/T7/CN) | 🟢 0 leak (10/8/10 driver rules) |
| materialize T6/T7/CN: A blocked→blend, B→control | 🟢 3/3 (gate chặn) |
| **Tổng CỔNG 3** | 🟢 **16/16 PASS** |

**Bảo vệ 3 lớp cho 9 forward-audit (không thể lái số):**
1. `drive_weight = 0` (V10689 ép cứng, bất kể rolling).
2. `confirm_only = 1` → V10690 loại khỏi danh sách driver.
3. T6/T7/CN weekday gate → A→blend, B→control (không MANUAL-alone-lead).

---

## 3. Verify hệ thống sau thay đổi ranker

| Kiểm tra | Kết quả |
|---|---|
| MN/MT invariance harness | 🟢 108/108 IDENTICAL |
| Full verify suite | 🟢 55/55 PASS (T2=86 chấp nhận) |
| Isolation matrix | 🟢 18/18 PASS |
| Official 4-table zero-drift | 🟢 (ranker không ghi official) |
| py_compile + ReadLints | 🟢 PASS / 0 |

---

## 4. CHECKLIST còn lại

| Phase | Việc | Trạng thái |
|---|---|---|
| 1 | V10689 rolling re-measure | 🟢 XONG |
| 2 | V10690 4 nhánh + register + cron | 🟢 XONG |
| **3** | T6/T7/CN forward-audit CONFIRM-only | 🟢 **XONG** |
| 4 | Deploy VPS /du-doan-test (2 cron) + smoke + official zero-drift | ⏳ kế tiếp (cần owner OK "deploy") |
| 5 | Tích lũy ≥7d + đo 30d | ⏳ |

---

## 5. Trạng thái deploy (Phase 4) — chờ owner

CỔNG 1+2+3 đều XANH. Sẵn sàng Phase 4 deploy VPS. Khi deploy CHỈ đẩy:
- `mb_rule_ranker.py`, `_v10689_...`, `_v10690_...`, `_v10690_register_experiments.py`
- `scheduler.py` (2 cron gated) + `main.py` (flag) → bật `MB_MANUAL_EXPERIMENT_ENABLE=True` CHỈ trên VPS

**KHÔNG đẩy** nhánh `rule_engine` MB-daily + `gpt_analyzer` MB-context (giữ official zero-drift).

Smoke sau deploy: 4 nhánh ra số, cron chạy, log gate có data, official `/du-doan` hash IDENTICAL.

---

**Bottom line CỔNG 3 🟢**: 9 STRONG candidate T6/T7/CN đã vào pool forward-audit, bảo vệ 3 lớp drive_weight=0 — không thể lái số. MN/MT 108/108, full 55/55, isolation 18/18. Sẵn sàng Phase 4 deploy (chờ owner OK).
