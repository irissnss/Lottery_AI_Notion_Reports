# V10685 — Nhất quán đặt tên: T1/T2/T3 → PRODUCTION/MANUAL/PREREG

> **Generated**: 2026-06-03 02:00 VN
> **Trigger**: Owner: "em nên nhất quán dùm anh chưa deploy VPS thì sữa cái tên dùm T2 mà chạy tầng 1 thì code lộn tùng phèo lên mất kiểm soát mất".
> **Trạng thái**: REPORT-ONLY. **55/55 + 18/18 PASS**. Không deploy code, không đụng official.

---

## 0. Vấn đề owner phát hiện

V10683 plan đề xuất `MB_T2_MANUAL_DRIVE_SHADOW_V1` — nhưng "T2" trước giờ đã định nghĩa là CONFIRM-only ở official; nếu T2 lại "drive" trong shadow thì:
- Tên "T2" mâu thuẫn vai trò
- Code lẫn lộn ID (T1/T2/T3) với vai trò (drive/confirm/watch)
- Tài liệu khó đọc

→ Phải **rename TRƯỚC khi code** (chưa deploy VPS, đang là cơ hội tốt để dọn).

---

## 1. Quy ước mới (V10685)

**Nguyên tắc**: Tên ID gắn với **NGUỒN cố định**, vai trò drive/confirm ghi trong context (description/log) chứ không trong ID.

| ID cũ | ID mới | Nguồn | Vai trò OFFICIAL | Vai trò /du-doan-test |
|---|---|---|---|---|
| `MB-T1-DYN8W` | **`MB-PROD-DYN8W`** | 35 production `mined_rules` | **DRIVE** score qua `extract_rule_candidates_v2` | có thể downgrade trong shadow |
| `MB-T2-SOI` | **`MB-MANUAL-SOI`** | 77 manual V10667 + V10636-DIG/LAGS | **CONFIRM-only** | có thể **DRIVE** shadow |
| `MB-T3-WATCH` | **`MB-PREREG-WATCH`** | 19 V10626 pre-register | DROPPED V10681 | DROPPED |

→ Cùng 1 nguồn, 1 ID; vai trò drive/confirm thay đổi giữa lane test/official mà KHÔNG đụng tên ID.

---

## 2. Code đã sửa (chỉ local, không deploy)

### 2.1 `web/backend/mb_rule_ranker.py`

```
MECH_PROD   = 'MB-PROD-DYN8W'    # was MB-T1-DYN8W
MECH_MANUAL = 'MB-MANUAL-SOI'    # was MB-T2-SOI
MECH_PREREG = 'MB-PREREG-WATCH'  # was MB-T3-WATCH

# Backward-compat aliases — giữ tới khi callers cập nhật xong:
MECH_T1 = MECH_PROD
MECH_T2 = MECH_MANUAL
MECH_T3 = MECH_PREREG
```

- Section comment đổi `Tier 1/2/3` → `PRODUCTION / MANUAL / PRE-REGISTER`.
- Function `_t2_score` GIỮ tên (back-compat) + docstring nói rõ "logically = `_manual_score`".
- Log detail: `T3=DROPPED_V10681` → `PREREG=DROPPED_V10681`.
- Return dict thêm key mới (`prod`, `manual_count`, `prereg_count`) cùng key cũ (`tier1`, `tier2_count`, `tier3_count`).

### 2.2 `web/backend/gpt_analyzer.py`

- Header: `MB 2-TIER RULE STACK` → `MB RULE STACK (PRODUCTION + MANUAL, daily, window 8W-tuned, weekday-bound cross-verify)`
- Section labels:
  - `TẦNG 1 — LIVE (MB-T1-DYN8W, ...)` → `PRODUCTION (MB-PROD-DYN8W, 35 rule đang DRIVE official, snapshot ..., 8W-tuned + vòng đời)`
  - `TẦNG 2 — CONFIRM (MB-T2-SOI, ...)` → `MANUAL (MB-MANUAL-SOI, soi cầu thủ công MB-target; vai trò: CONFIRM ở /du-doan official, có thể DRIVE ở /du-doan-test khi owner OK)`
- Cross-verify note: `T1 (LIVE, drives score) cùng T2 (CONFIRM, không drive)` → `PRODUCTION (drives score ở /du-doan official) đồng thuận với MANUAL (CONFIRM ở official; có thể DRIVE shadow)`
- `MB_EXPERT_DOCTRINE`: bỏ "TẦNG 1/2", dùng `PRODUCTION 35 rule (MB-PROD-DYN8W)` và `MANUAL 77 rule (MB-MANUAL-SOI)`.

### 2.3 `web/backend/prompt_registry.py`

- `CTX-MB-1.0` bump version `MB-1.1` → `MB-1.2`.
- Description: bỏ `Tier1/Tier2/Tier-3`, dùng `PRODUCTION 35 = MB-PROD-DYN8W` / `MANUAL 77 = MB-MANUAL-SOI`.
- Doctrine list: cross-verify `PRODUCTION (drives official) ↔ MANUAL (CONFIRM in official)`.

### 2.4 KHÔNG đổi

- **Database table names** giữ nguyên (rename = migration risk, đã có data):
  - `mined_rules_mb_daily` (PRODUCTION snapshot)
  - `mb_t2_manual_daily` (MANUAL daily — tên cũ giữ, logical name = `MB_MANUAL_DAILY`)
  - `mb_t3_prereg_daily` (PREREG, DROPPED)
  - `mb_rule_context`, `mb_rerank_log`
- **V10683 experiment names** SẼ rename khi code (chưa code):
  - `MB_T2_MANUAL_DRIVE_SHADOW_V1` → `MB_MANUAL_DRIVE_SHADOW_V1`
  - `MB_T2_BHPASS_ONLY_DRIVE_SHADOW_V1` → `MB_MANUAL_BHPASS_DRIVE_SHADOW_V1`
  - `MB_T2_MANUAL_BLEND_T1_T2_SHADOW_V1` → `MB_BLEND_PROD_MANUAL_SHADOW_V1`
  - File `_v10683_mb_t2_drive_shadow.py` → `_v10683_mb_manual_drive_shadow.py`

---

## 3. Backup V10685

`backups/v10685_naming_consistency_20260603_015335/code/`:
- `rule_engine.py.v10685.pre`
- `gpt_analyzer.py.v10685.pre`
- `prompt_registry.py.v10685.pre`
- `scheduler.py.v10685.pre`
- `mb_rule_ranker.py.v10685.pre`

Restore: copy `*.v10685.pre` về `web/backend/` (strip suffix).

---

## 4. Verify (sau rename)

| Check | Kết quả |
|---|---|
| py_compile 5 file backend | PASS |
| ReadLints | 0 errors |
| Harness MN/MT 108 chữ ký | **108/108 IDENTICAL** |
| Full verify suite | **55/55 PASS, 0 FAIL** (thêm 1 check back-compat alias) |
| Isolation matrix MN/MT cả 2 luồng | **18/18 PASS** |
| Context pack render | 0 leak `TẦNG 1/2/3`, có `MB-PROD-DYN8W` + `MB-MANUAL-SOI` |
| Ranker run | `prod`/`manual_count`/`prereg_count` đầy đủ + back-compat keys |

---

## 5. Context pack render mẫu (sau rename)

```
### 🔵 MB RULE STACK (PRODUCTION + MANUAL, daily, window 8W-tuned, weekday-bound cross-verify)
  PRODUCTION (MB-PROD-DYN8W, 35 rule đang DRIVE official, snapshot 2026-06-03, 8W-tuned + vòng đời):
    #5  MB:Quảng Ninh:D-1 [G6+G7] comp=87 [mạnh] hr8=88% hr12=83% hr16=87% (n=15, LIMITED_WEIGHT)
    #11 MN:Vũng Tàu:D-1 [G5+G7] comp=81 [tăng↑] hr8=88% hr12=67% hr16=67% (n=15, LIMITED_WEIGHT)
    #18 MB:Quảng Ninh:D-1 [GĐB+G2] comp=76 [tăng↑] hr8=75% hr12=67% hr16=67% (n=15, LIMITED_WEIGHT)
    ...

  MANUAL (MB-MANUAL-SOI, soi cầu thủ công MB-target; vai trò: CONFIRM ở /du-doan official, có thể DRIVE ở /du-doan-test khi owner OK):
    Coverage thứ này: 14 rule [V10667=12, V10636-DIG=2]
    • MB:G7#4:D-1 [LAST2] lift=7.2pp hr=30.98% ⭐BH [mạnh] (V10667)
    • MB:G6#2:D-1 [LAST2_REV] lift=5.66pp hr=29.45%  [ổn định] (V10667)
    ...

  ➤ Cross-verify per weekday: PRODUCTION (drives score ở /du-doan official) đồng thuận với MANUAL
    (CONFIRM ở official; có thể DRIVE shadow ở /du-doan-test). Vòng đời: mạnh→trọng số đầy;
    tăng↑→ứng viên nâng; giảm↓→hạ + cảnh báo; yếu→nén. Không double-weight: runtime đã tính
    PRODUCTION vào score; MANUAL chỉ dùng để giải thích ở official.
```

---

## 6. Trạng thái

| Hạng mục | Status |
|---|---|
| Code deploy VPS | NO |
| Official mutation | NO |
| Naming consistent | DONE (V10685) |
| Backup full | DONE (`v10685_naming_consistency_20260603_015335`) |
| MN/MT bất biến | PROVEN 108/108 |
| Full verify | 55/55 PASS |
| Isolation 2 luồng | 18/18 PASS |
| Public report V10685 | sẽ push |
| V10683 experiment names | SẼ rename khi code (chưa code) |
| Owner decisions | vẫn còn V10683 (A/B/C/D + V10684 rolling re-measure + thresholds) |

---

**Bottom line**: tên đã nhất quán và clean. Khi anh OK V10683 + V10684 plans, em code thẳng với tên mới `MB_MANUAL_*` / `MB_BLEND_*` / `_v10683_mb_manual_drive_shadow.py` — không có rename retro nào nữa, code không bị lộn.
