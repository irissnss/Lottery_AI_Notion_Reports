# V10689 — PHASE 1: Rolling re-measure 77 MANUAL → CỔNG 1 XANH

> **Generated**: 2026-06-03 13:38 VN
> **Phase**: 1/5 của MASTER PROMPT (MB MANUAL-drive experiment)
> **Trạng thái cổng**: 🟢 **XANH** — đủ điều kiện sang Phase 2
> **Live sync**: `artifacts/live_sync/20260603_122600/manifest.json`
> **Phạm vi**: code + verify LOCAL. CHƯA deploy VPS. Official KHÔNG đụng.

---

## 0. Việc Phase 1 đã làm

1. Code `web/backend/_v10689_mb_manual_rolling_remeasure.py`:
   - Re-measure 77 MANUAL rule trên `lottery_results` tươi nhất.
   - Cửa sổ rolling: recent 4W & 8W; split-half trend (16 occ); recent-decay; confidence theo sample.
   - **Loại mining gap W20/W21 (2026-05-04..2026-05-31)** khỏi mọi mẫu (owner guardrail).
   - Sinh `drive_weight` ∈ [0,1] + lifecycle + `static_caveat` (nếu <4 mẫu tươi → không lái bằng nhãn đóng băng).
   - Ghi vào `mb_t2_manual_daily` (thêm cột rolling). KHÔNG đụng official table.
2. Thêm cron **20:25** vào `scheduler.py` — **gated** sau cờ `MB_MANUAL_EXPERIMENT_ENABLE` (default `False` ở `main.py`) → "viết, chưa bật".
3. 7 transform hỗ trợ: LAST2, FIRST2, HEAD_TAIL, LAST2_REV, SECOND_HEAD_TAIL, FIRST2_REV, TAIL_HEAD → **77/77 rule parse được, 0 skip**.

---

## 1. CỔNG 1 — kết quả verify

| Kiểm tra | Ngưỡng | Kết quả |
|---|---|---|
| Official 4 bảng hash | IDENTICAL | 🟢 ZERO-DRIFT (predictions/final_bundles/lottery_results/model_daily_eval) |
| mined_rules MN/MT hash | IDENTICAL | 🟢 IDENTICAL trước/sau V10689 |
| MN/MT invariance harness | 108/108 | 🟢 108/108 IDENTICAL |
| Full verify suite | 55/55 | 🟢 55/55 PASS |
| Isolation matrix (official+lane) | 18/18 | 🟢 18/18 PASS |
| py_compile + ReadLints | PASS / 0 | 🟢 PASS / 0 errors |
| 77 MANUAL rule re-measured | 77/77 | 🟢 77/77 (0 skip) |

→ **Tất cả cổng XANH.**

---

## 2. Bảng drive_weight (rolling) — phân bố 77 MANUAL

| Lifecycle (rolling) | Số rule | drive_weight TB |
|---|---:|---:|
| TANG_TRUONG (tăng↑) | 23 | 0.969 |
| MANH (mạnh) | 4 | 1.000 |
| XUONG_CAP (giảm↓) | 4 | 0.780 |
| YEU (yếu) | 46 | 0.037 |
| **rule có drive_weight > 0** | **55 / 77** | |

**Top drive_weight (rolling 8W):**

| Thứ | Rule | hit8w | lift8w | trend | drive_weight | lifecycle |
|---|---|---:|---:|---:|---:|---|
| T4 | `MB:G6#2:D-1` LAST2_REV | 75.0% | +51.2pp | +62.5 | 1.00 | TANG_TRUONG |
| T6 | `MN:G7#1:D-2` LAST2 | 87.5% | +31.8pp | +50.0 | 1.00 | TANG_TRUONG |
| T5 | `MN:G8#1:D` LAST2 | 87.5% | +31.8pp | +12.5 | 1.00 | TANG_TRUONG |
| T2 | `MB:G6#2:D-1` HEAD_TAIL | 50.0% | +26.2pp | 0.0 | 1.00 | MANH |
| T5 | `MN:G2#1:D-1` LAST2 | 75.0% | +19.2pp | 0.0 | 1.00 | MANH |

---

## 3. Phát hiện quan trọng (trung thực)

- **Rolling khác hẳn static**: rule gold tĩnh `MN:DB#1:D` (V10667 +8.43pp/326d) khi đo rolling 8W gần đây = hit 37.5%, lift **−18.3pp** → `drive_weight=0` (YEU). Đây CHÍNH là giá trị của rolling re-measure: bắt được rule đã **decay** mà nhãn tĩnh không thấy.
- **46/77 rule YEU** ở cửa sổ gần → nếu cho MANUAL drive thì chỉ 55 rule thực sự đóng góp, phần lớn là rule đang tăng trưởng.
- **Caveat noise**: cửa sổ 8W = 8 lần xuất hiện của thứ đó → mẫu nhỏ, nhiễu. drive_weight dùng cho **shadow** (đo 30d), KHÔNG promote official khi chưa đủ 14 ngày data tươi (Phase 5 guard).

---

## 4. An toàn (guardrails đã giữ)

| Guardrail | Trạng thái |
|---|---|
| Không đụng official /du-doan | ✅ (V10689 chỉ ghi `mb_t2_manual_daily`) |
| 4 official tables zero-drift | ✅ |
| MN/MT 108/108 + isolation 18/18 | ✅ |
| Cron viết-nhưng-chưa-bật | ✅ (gated `MB_MANUAL_EXPERIMENT_ENABLE=False`) |
| Loại mining gap W20/W21 | ✅ (2026-05-04..05-31 excluded) |
| static_caveat khi thiếu data | ✅ (0 rule static hiện tại, mọi rule ≥4 mẫu) |
| Backup .pre trước sửa | ✅ `backups/v10689_phase1_20260603_133757/` + V10685 .pre |

---

## 5. CHECKLIST việc còn lại

| Phase | Việc | Trạng thái |
|---|---|---|
| **1** | Rolling re-measure V10689 + CỔNG 1 | 🟢 **XONG** |
| 2 | Code `_v10690_mb_manual_drive_shadow.py` + 4 nhánh + register + cron 23:50 | ⏳ kế tiếp |
| 3 | T6/T7/CN B+A: nạp 9 STRONG candidate CONFIRM-only drive_weight=0 | ⏳ |
| 4 | Deploy VPS /du-doan-test (2 cron) + smoke + official zero-drift | ⏳ |
| 5 | Tích lũy ≥7d + đo 30d (would_flip / false_promotion / ΔBT) | ⏳ |

---

## 6. Lưu ý kiến trúc deploy (Phase 4) — để KHÔNG đụng official

Khi deploy, CHỈ đẩy script data/lane-test:
- `mb_rule_ranker.py` (sinh `mined_rules_mb_daily` + `mb_t2_manual_daily`)
- `_v10689_mb_manual_rolling_remeasure.py` (drive_weight)
- `_v10690_...` (experiments → `experimental_preview_shadow` lane test)

**KHÔNG đẩy** nhánh `rule_engine` MB-daily + `gpt_analyzer` MB-context (chúng đổi official MB). Official tiếp tục đọc `mined_rules` thẳng → zero-drift đảm bảo.

---

**Bottom line CỔNG 1 🟢**: V10689 rolling re-measure chạy đúng, official zero-drift, MN/MT bất biến, 77/77 rule có drive_weight động. Sẵn sàng Phase 2 (experiments). Chưa deploy gì.
