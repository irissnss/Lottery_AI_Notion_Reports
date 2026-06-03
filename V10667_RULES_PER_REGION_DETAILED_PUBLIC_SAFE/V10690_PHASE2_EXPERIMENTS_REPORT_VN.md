# V10690 — PHASE 2: 4 nhánh MANUAL-drive shadow → CỔNG 2 XANH

> **Generated**: 2026-06-03 13:50 VN | **Phase**: 2/5 | **Cổng**: 🟢 XANH
> **Phạm vi**: code + verify LOCAL. CHƯA deploy VPS. Official KHÔNG đụng.

---

## 0. Việc Phase 2 đã làm

1. `_v10690_register_experiments.py` — đăng ký 3 experiment vào `du_doan_test_experiments` (idempotent, diagnostic_only=1, owner_approved=0). ✅ all_present=True.
2. `_v10690_mb_manual_drive_shadow.py` — materialize 4 nhánh trên `/du-doan-test`:
   - **A** `MB_MANUAL_DRIVE_SHADOW_V1`: MANUAL quyết định trên TOÀN tập đuôi MANUAL dự đoán (full swap), model chỉ tie-break.
   - **B** `MB_MANUAL_BHPASS_DRIVE_SHADOW_V1`: chỉ 5 BH-pass MANUAL quyết định.
   - **C** `MB_BLEND_PROD_MANUAL_SHADOW_V1`: blend `0.7×norm(model) + 0.30×norm(manual)`.
   - **CTRL** `MB_OFFICIAL_BASELINE_CONTROL`: do materializer cũ sinh.
3. Cron **23:50** thêm vào scheduler — gated `MB_MANUAL_EXPERIMENT_ENABLE` (chưa bật).
4. Harness metrics/nhánh: `would_flip_to_win`, `false_promotion`, `ΔBT` (ghi mỗi row).

---

## 1. Weekday gate (owner: T6/T7/CN không cho MANUAL dẫn một mình)

| Thứ | A (MANUAL) | B (BH-pass) | C (BLEND) |
|---|---|---|---|
| T2/T3/T4/T5 | MANUAL dẫn | BH-pass dẫn (nếu có) | blend |
| **T6/T7/CN** | **→ blend** (MANUAL_LEAD_BLOCKED) | **→ control** (NO_BHPASS) | blend (cho phép) |

**Dry-run thực tế chứng minh gate:**

| Ngày | Thứ | base | A bt | B bt | C bt | Ghi chú |
|---|---|---|---|---|---|---|
| 2026-06-02 | T3 | 24 | **26** (full swap, ngoài pool) | 24 (none fired→ctrl) | 24 | MANUAL chọn đuôi riêng |
| 2026-05-01 | T6 | 94 | 94 (blocked→blend) | 94 (blocked→ctrl) | 94 | gate chặn đúng |
| 2026-05-02 | T7 | 43 | 91 (blocked→blend) | 43 (blocked→ctrl) | 91 | blend nudge |
| 2026-05-03 | CN | 48 | 48 (blocked→blend) | 48 (blocked→ctrl) | 48 | gate chặn đúng |

---

## 2. CỔNG 2 — kết quả

| Kiểm tra | Kết quả |
|---|---|
| 3 experiment đăng ký `du_doan_test_experiments` | 🟢 all_present=True |
| Dry-run in số 4 nhánh + log gate | 🟢 (bảng trên) |
| Official 4-table hash sau khi WRITE experiments | 🟢 ZERO-DRIFT (IDENTICAL) |
| Ghi vào `mb_experimental_preview_shadow` | 🟢 +3 rows (lane test only) |
| MN/MT invariance harness | 🟢 108/108 IDENTICAL |
| Full verify suite | 🟢 55/55 PASS |
| Isolation matrix (official+lane) | 🟢 18/18 PASS |
| py_compile + ReadLints | 🟢 PASS / 0 |

→ **CỔNG 2 XANH.**

---

## 3. Hard contract giữ đúng

| Guardrail | Trạng thái |
|---|---|
| Chỉ ghi `mb_experimental_preview_shadow` + `du_doan_test_experiments` | ✅ |
| 4 official tables zero-drift | ✅ |
| Không gọi `generate_final_bundle`, không ghi `predictions`/`final_bundles` | ✅ |
| Cấm double-weight: MANUAL drive thì model chỉ tie-break (A/B), blend tách rõ (C) | ✅ |
| T6/T7/CN không cho MANUAL dẫn một mình | ✅ (gate verify) |
| Cron 23:50 viết-chưa-bật (gated) | ✅ |
| Loại mining gap (qua drive_weight V10689) | ✅ |

---

## 4. CHECKLIST còn lại

| Phase | Việc | Trạng thái |
|---|---|---|
| 1 | V10689 rolling re-measure | 🟢 XONG |
| **2** | V10690 4 nhánh + register + cron | 🟢 **XONG** |
| 3 | T6/T7/CN B+A: 9 STRONG candidate CONFIRM-only drive_weight=0 + forward-audit | ⏳ kế tiếp |
| 4 | Deploy VPS /du-doan-test (2 cron) + smoke + official zero-drift | ⏳ |
| 5 | Tích lũy ≥7d + đo 30d | ⏳ |

---

**Bottom line CỔNG 2 🟢**: 4 nhánh chạy đúng, weekday gate chặn T6/T7/CN, official zero-drift, MN/MT bất biến. Sẵn sàng Phase 3 (nạp 9 STRONG candidate forward-audit, drive_weight=0).
