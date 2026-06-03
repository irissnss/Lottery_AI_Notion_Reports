# V10688 — MASTER CONSOLIDATION: tên gọi, khái niệm "đảo", sổ quyết định, việc tồn đọng

> **Generated**: 2026-06-03 12:50 VN
> **Mục đích**: 1 tài liệu DỨT ĐIỂM cho owner — làm rõ tên gọi, làm rõ "đảo T2↔T1" thực chất là gì, liệt kê mọi quyết định đã thống nhất + mọi việc tồn đọng. Đọc cái này là hiểu toàn bộ.
> **Trạng thái**: REPORT-ONLY. Không deploy code, không đụng official. **CHƯA đi tiếp tới khi owner xác nhận tài liệu này.**

---

## PHẦN 1 — TÊN GỌI: dứt điểm (T1/T2/T3 → PROD/MANUAL/PREREG)

### 1.1 Bảng ánh xạ chính thức

| Tên CŨ (bỏ) | Tên MỚI (chính thức) | Nguồn rule | Số rule MB | Vai trò ở /du-doan (official) |
|---|---|---|---:|---|
| ~~T1 / MB-T1-DYN8W~~ | **PRODUCTION** = `MB-PROD-DYN8W` | `mined_rules` (đào tự động) | **35** | **DRIVE** số (đang chạy live) |
| ~~T2 / MB-T2-SOI~~ | **MANUAL** = `MB-MANUAL-SOI` | soi cầu thủ công V10667 + V10636-DIG/LAGS | **77** | **CONFIRM** (đối chiếu, không drive) |
| ~~T3 / MB-T3-WATCH~~ | **PREREG** = `MB-PREREG-WATCH` | V10626 pre-register | ~~19~~ | **ĐÃ HỦY** (V10681), purge sạch (V10686.1) |

### 1.2 Vì sao đổi tên theo NGUỒN, không theo VAI TRÒ

- "T1/T2/T3" gắn với THỨ HẠNG/VAI TRÒ → khi MANUAL chạy drive trong lane test thì "T2 lại làm T1" → loạn.
- Tên mới gắn với **NGUỒN cố định**: PRODUCTION mãi là 35 rule production, MANUAL mãi là 77 rule thủ công. Vai trò (drive/confirm) ghi riêng trong context, đổi tự do không đụng tên.

### 1.3 Tên bảng DB giữ nguyên (tránh migration risk)

| Bảng | Chứa | Ghi chú |
|---|---|---|
| `mined_rules_mb_daily` | PRODUCTION snapshot | tên giữ |
| `mb_t2_manual_daily` | MANUAL daily | tên giữ (logical = MB_MANUAL_DAILY) |
| `mb_t3_prereg_daily` | PREREG | giữ làm audit, KHÔNG đọc/refresh |
| `mb_rule_context` | payload cho prompt | chỉ còn `TIER2_CONFIRM` (TIER3_WATCH đã purge) |

Code giữ alias back-compat `MECH_T1=MECH_PROD`, `MECH_T2=MECH_MANUAL` để không vỡ caller cũ.

---

## PHẦN 2 — "ĐẢO T2 ↔ T1" thực chất là gì (làm rõ hiểu nhầm)

### 2.1 Sau khi đổi tên, KHÔNG còn "T1/T2" để đảo tên

"Đảo T2 lên làm T1" theo nghĩa **đổi tên** → KHÔNG còn áp dụng. Vì tên giờ theo nguồn (PRODUCTION/MANUAL), không theo thứ hạng.

### 2.2 "Đảo" = đổi VAI TRÒ (ai DRIVE số), KHÔNG phải đổi tên

```
HIỆN TẠI (official /du-doan):
   PRODUCTION (35)  --DRIVE-->  số chốt (qua rule_engine + final_bundle)
   MANUAL (77)      --CONFIRM-> chỉ đối chiếu, không drive

"ĐẢO" mà owner muốn thử = cho MANUAL DRIVE thay vì chỉ confirm:
   MANUAL (77)      --DRIVE-->  số (thử nghiệm)
   PRODUCTION (35)  --so sánh-> control

→ Đây là đổi VAI TRÒ, thử ở /du-doan-test (shadow), KHÔNG đụng official.
→ KHÔNG phải rename. Tên vẫn PRODUCTION / MANUAL.
```

### 2.3 "Đảo" được thử bằng 3 EXPERIMENT trong lane test (owner đã chọn D = cả 3)

| Experiment (tên mới, V10685) | MANUAL drive thế nào |
|---|---|
| `MB_MANUAL_DRIVE_SHADOW_V1` | 77 MANUAL drive hoàn toàn (đảo đầy đủ) |
| `MB_MANUAL_BHPASS_DRIVE_SHADOW_V1` | chỉ 5 BH-pass MANUAL drive (conservative) |
| `MB_BLEND_PROD_MANUAL_SHADOW_V1` | trộn 0.7×PRODUCTION + 0.3×MANUAL (đảo một phần) |

→ Cả 3 chạy SONG SONG với control `MB_OFFICIAL_BASELINE_CONTROL`, đo 30 ngày. KHÔNG cái nào đụng official.

### 2.4 Vì sao KHÔNG đảo thẳng trên official (V10682 đã phân tích)

- PRODUCTION có rolling MRE 365d + 7 lớp safety chain; MANUAL đo 1 lần, chưa rolling.
- T1∩T2 = 0 overlap (bổ trợ, không cạnh tranh) → giữ PRODUCTION drive + thử MANUAL ở lane là an toàn nhất.
- Forward-audit doctrine: MANUAL `live_eligible=False` tới khi qua audit.

---

## PHẦN 3 — SỬA TRÙNG SỐ VERSION (đang gây rối)

### 3.1 Vấn đề: "V10684" bị dùng 2 lần

| V10684 dùng ở đâu | Là gì |
|---|---|
| `V10684_ISOLATION_MATRIX_AND_FULL_BACKUP_VN.md` | **REPORT** isolation + backup (đã push) |
| `_v10684_mb_manual_rolling_remeasure.py` (trong design V10686) | **CODE** rolling re-measure (chưa viết) |

→ Trùng số = rối. Phải tách.

### 3.2 Quy ước mới: số CODE feature tách khỏi số REPORT

| Hạng mục | Số CŨ (bỏ) | Số MỚI (chính thức) | Tên file |
|---|---|---|---|
| Rolling re-measure 77 MANUAL | ~~V10684~~ | **V10689** | `_v10689_mb_manual_rolling_remeasure.py` |
| 3 shadow experiments | ~~V10683 code~~ | **V10690** | `_v10690_mb_manual_drive_shadow.py` + `_v10690_register_experiments.py` |

- **Report** giữ chuỗi tuần tự: V10680 … V10687 (dig) … V10688 (file này).
- **Code feature** dùng số riêng: V10689 (rolling), V10690 (experiments).
- Các tham chiếu cũ `_v10684_...` và `_v10683_mb_t2_drive_shadow.py` → **SUPERSEDED**, không dùng nữa.

---

## PHẦN 4 — SỔ QUYẾT ĐỊNH (đã thống nhất / điều chỉnh / thay đổi)

| Report | Việc | Quyết định cuối | Verify |
|---|---|---|---|
| V10679 | Xây MB rule stack (R0-R4) | Subsystem MB-only, window 8W, không đụng miner chung | 108/108 |
| V10680 | Làm rõ 3 nhóm rule | (một phần superseded bởi V10681) | — |
| V10681 | **Hủy T3** (PREREG) | T3 BH_FAIL + không weekday → BỎ khỏi runtime | 54/54 |
| V10682 | Phân tích đảo T1↔T2 official | KHÔNG đảo official; thử ở lane | — |
| V10683 | Plan lane test | (file code đổi tên → V10690) | — |
| V10684 | Isolation MN/MT 2 luồng + backup | Cô lập sạch | 18/18 |
| V10685 | **Đổi tên** T1/T2/T3→PROD/MANUAL/PREREG | Tên theo nguồn | 55/55 |
| V10686 | Technical design rolling + experiments | (số code → V10689/V10690) | — |
| V10686.1 | Purge TIER3_WATCH khỏi mb_rule_context | self-heal | 55/55 |
| V10687 | Đào T6/T7/CN tìm gold | **KHÔNG có gold**; có STRONG candidates | dig done |
| V10688 | **File này** — consolidation + sửa trùng số | (chờ owner xác nhận) | — |

### Owner đã chốt (lock-in):
- Phương án experiment = **D (cả 3)**
- Rolling re-measure trước experiment 1 tuần = **OK**
- Ngưỡng PASS/FAIL 30d = **OK**

---

## PHẦN 5 — VIỆC TỒN ĐỌNG (cần làm tiếp, theo thứ tự)

| # | Việc | Phụ thuộc | Owner cần quyết | Trạng thái |
|---|---|---|---|---|
| 1 | **T6/T7/CN**: A (forward-audit STRONG) / B (MANUAL CONFIRM-only ngay) / C (bỏ qua) | V10687 done | **YES** | chờ owner |
| 2 | Xác nhận tên gọi + khái niệm đảo (PHẦN 1-2) | — | **YES** | chờ owner |
| 3 | Xác nhận sửa trùng số V10689/V10690 (PHẦN 3) | — | **YES** | chờ owner |
| 4 | **Code V10689** rolling re-measure 77 MANUAL (local + verify + backup) | sau #2,#3 OK | "code đi" | chưa code |
| 5 | +1 tuần data rolling tươi | sau #4 | — | chưa |
| 6 | **Code V10690** 3 experiments (local + verify + backup) | sau #5 | — | chưa code |
| 7 | Deploy VPS (2 cron: V10689 20:25 + V10690 23:50) | sau #6 verify | "deploy đi" | chưa |
| 8 | 30 ngày đo 4 ngưỡng → promote/drop | sau #7 | review | chưa |

---

## PHẦN 6 — TRẠNG THÁI VERIFY (rõ ràng: gì đã chắc, gì chưa)

### ĐÃ verify (chắc chắn)
| Hạng mục | Bằng chứng |
|---|---|
| MN/MT bất biến (official) | 108/108 IDENTICAL (frozen DB + hashseed) |
| MN/MT cô lập (official + lane test) | 18/18 isolation matrix PASS |
| Full code verify | 55/55 PASS |
| 4 official tables zero-drift | hash IDENTICAL |
| T3 purge sạch | `mb_rule_context` chỉ còn TIER2_CONFIRM |
| T6/T7/CN không có gold | dig 1809 cells, 0 BH-pass (V10687) |
| Backup đầy đủ | 3 bộ (`v10684_full`, `v10685_naming`, + code .pre) |
| Tên PROD/MANUAL trong code + prompt | grep 0 leak T1/T2/T3 trong pack |

### CHƯA verify (vì chưa code)
| Hạng mục | Khi nào verify |
|---|---|
| Rolling re-measure 77 MANUAL chạy đúng | sau code V10689 |
| 3 experiments chọn số đúng | sau code V10690 |
| MANUAL-drive có beat control không | sau 30d shadow |
| T6/T7/CN STRONG candidates sống sót forward-audit | sau 90d (nếu owner chọn A) |

---

## PHẦN 7 — CỔNG CHẶN (gate) trước khi đi tiếp

> **Em KHÔNG code/đào gì thêm cho tới khi owner xác nhận 3 điều ở PHẦN 5 (#1, #2, #3).**

Cụ thể em chờ owner trả lời:
1. **T6/T7/CN** → chọn A / B / C?
2. **Tên gọi + khái niệm đảo** (PHẦN 1-2) → OK chưa, hay cần chỉnh?
3. **Sửa trùng số** V10689 (rolling) + V10690 (experiments) → OK chưa?

Sau khi owner OK cả 3 → em code V10689 (local, verify, backup, KHÔNG deploy) → anh review → mới deploy.

---

## PHẦN 8 — Lịch sử báo cáo public (cho AI tools)

```
V10688 (file này) MASTER consolidation: naming + swap + ledger + pending
V10687  dig T6/T7/CN — no gold, STRONG candidates
V10686  technical design (rolling + experiments) — số code đổi sang V10689/V10690
V10685  naming T1/T2/T3 -> PROD/MANUAL/PREREG
V10684  isolation matrix MN/MT 2 lanes + full backup
V10683  lane test plan (3 experiments)
V10682  T1 vs T2 swap analysis (official: no; lane: yes)
V10681  drop T3 (PREREG)
V10680  MB rule-stack clarification
```

---

**Bottom line**: Tên gọi đã rõ (PRODUCTION/MANUAL/PREREG-hủy). "Đảo" = đổi VAI TRÒ drive, thử ở lane test, KHÔNG phải rename. Trùng số V10684 đã tách thành V10689 (rolling) + V10690 (experiments). Mọi quyết định + việc tồn đọng đã liệt kê. Em **dừng ở đây chờ owner xác nhận PHẦN 7** — đúng như anh dặn: chưa rõ chưa đi tiếp.
