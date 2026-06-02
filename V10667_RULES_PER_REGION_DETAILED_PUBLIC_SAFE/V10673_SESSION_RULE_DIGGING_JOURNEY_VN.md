# V10673 — Tổng Hợp TOÀN BỘ Hành Trình Đào Rules (Session Master Journey)

> **Generated**: 2026-06-02 13:15 VN
> **Trigger**: Owner — "trong suốt trò chuyện này... trước đó anh có cùng em đào bới một số Rules, em đã tổng hợp lại hết chưa?"
> **Mục đích**: GOM về 1 chỗ DUY NHẤT mọi giả thuyết/rule đã đào trong cả cuộc trò chuyện (21/05 → 02/06), kèm **kết luận** (validated / pre-register / yếu / bác bỏ) + link artifact. Trước đây mỗi đợt nằm rải rác ~10 package khác nhau — file này là index thống nhất.

---

## 0. TL;DR — đào gì, kết quả ra sao

Cả cuộc trò chuyện đã test **38 đợt giả thuyết**, gom thành **10 nhóm phiên bản**. Phân loại kết quả:

| Loại kết quả | Số nhóm | Nghĩa |
|---|---|---|
| ✅ **VALIDATED (BH-pass)** | 1 | Sống sót đa kiểm định — V10636-CROSS → 28 rule forward-audit |
| 🟡 **PRE-REGISTER** | 1 | Ứng viên chờ 90 ngày — V10626 FU (13 + 58) |
| ⚠️ **WEAK / SELECTION BIAS** | 4 | Lift đẹp nhưng V107 null-test bác (0/153k BH) |
| ❌ **REJECTED** | 2 | Giả thuyết không đúng (MB D-2 self) |
| 🔧 **OPERATIONAL/FIX** | 2 | Timing audit + temporal/semantics fix/verify |

→ **Đã tổng hợp HẾT.** Mỗi đợt đều có artifact + public package. File này là bản gom thống nhất (trước đó thiếu).

---

## 1. Bản đồ hành trình theo thời gian

| # | Ngày | Phiên bản | Chủ đề đào | Kết luận | Link |
|---|---|---|---|---|---|
| 1 | 21/05 | **V106.03** | MB Giải nhì (bộ #1 / cả 2 bộ) → MN D, lag D-1/D-2/D-3 | ⚠️ D-2 bộ#1 +14.1pp (30d) nhưng tiền-V107 → yếu | `V106_03_MB_G2_PAIR_LAG_RECURRENCE_PUBLIC_SAFE` |
| 2 | 22/05 | **V106.04** | Quét rộng nguồn mạnh cho MN/MT/MB + exact-position + digit-transform | ⚠️ Lift cao (vd +21pp, +27pp) nhưng sample nhỏ → V107 bác | `V106_04` (private) |
| 3 | 23/05 | **V106.05** | MT D ← MB D-1/D-2/D-3 (DB/G1/G2 + transforms) | ⚠️ Hướng đúng (MB:G2#1:P4P1 D-1→MT +14.9pp) nhưng V107 BH_FAIL | `V106_05_MT_FROM_MB_D1D3_PUBLIC_SAFE` |
| 4 | 23/05 | **V106.06** | Mega-mine: 3 miền × transforms × lag D-1..D-7/W-1..W-4 (153,228 rule) | ⚠️ 54,924 accepted, 1,263 Tier A — **nhưng xem V107** | `V106_06_DEEP_SOURCE_RULE_DISCOVERY_PUBLIC_SAFE` |
| 5 | 23/05 | **V107** | Null-test (5 null) + 7 family A–G: signal thật hay selection bias? | ⚠️ **WEAK SIGNAL — Null3 FAIL 0/153,228 BH q<0.05**. Phần lớn là selection bias | `V107_NULL_AND_SIGNAL_TEST_PUBLIC_SAFE` |
| 6 | 24–25/05 | **V106.26** | Verify TOÀN BỘ rule đã báo (V106.03/05/06/07); pre-register only | 🟡 55,546 rule inventoried; coverage matrix MT/MN/MB; tất cả PRE_REGISTER_ONLY | `V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE` |
| 6a | 24/05 | **FU1** | MB D = MB GĐB D-2 (self-recurrence, lần đầu) | ❌ **NOT verified** (H2 strict ~0%) | (trong V106.26 FU) |
| 6b | 24/05 | **FU2** | Self-lag MN/MT + cross-region (4 giải ít bộ), H1+H2 | 🟡 9,226 cell dương; cross-region MN/MT > MB self D-2 | (FU2) |
| 6c | 25/05 | **FU3** | Giải ít bộ MN/MT (G8/G7/G5/G2/G1/DB) + fix bug key-order ~8% | 🟡 12,966 rule dương; bổ sung G8/G7 | (FU3) |
| 6d | 25/05 | **FU4** | MB thêm G4#1-4, G6#1-3, G7#1-4 làm nguồn (owner gửi ảnh schema) | 🟡 **20,843 dương (+8,886 từ G4/G6/G7); 13 STABLE_ALL pre-register** | (FU4 addendum) |
| 7 | 27/05 | **V10635** | MB D = MB GĐB D-2 deep dive (6 window × 28 transform × weekday) | ❌ **BÁC BỎ** — 60-90d H1 −3.7pp; H2 ≈ random 1% | `V106_35_MB_DB_D2_DEEP_DIVE_PUBLIC_SAFE` |
| 8 | ~01/06 | **(timing audit)** | Hệ thống xác định D / D-1 từ thời điểm nào? | 🔧 D = nửa đêm VN (Asia/Ho_Chi_Minh); D-1 = −1 ngày lịch; cron 04:00/20:15 | `docs/TIMEZONE_AND_DATE_SEMANTICS.md` (private) |
| 9 | 01–02/06 | **V10636** (main/LP/EXT/MBSELF/DIG/LAGS/CROSS) | MB GĐB D-1 → MN/MT; self-lag MB; **full cross-region matrix** | ✅ **CROSS: 268 BH-pass, max +16.68pp**; các pass strict khác 0 BH-pass | `V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE` |
| 10 | 02/06 | **V10667→V10672** | Tài liệu 3 miền + bộ-numbering + temporal fix + source semantics + master verify | ✅ Consolidated; 232 BH-valid → **28 forward-audit (90d)** | (bundle này) |

---

## 2. Chi tiết từng đợt owner trực tiếp yêu cầu (checkpoint)

| Owner hỏi | Đợt | Kết luận | Mạnh nhất |
|---|---|---|---|
| MB G4/G6/G7 thêm làm nguồn | FU4 | 🟡 13 pre-register STABLE_ALL | MN←MB:G4#2:TAIL_HEAD D-6 +4.84pp (H2) |
| MB D = MB D-2 GĐB "thường về" | FU1 + V10635 | ❌ Bác bỏ | H1 −3.7pp (giả thuyết sai) |
| MB GĐB D-1 → MN D / MT D + loại trừ MN⊥MT | V10636-main | ✅ T7 EITHER +22.5pp; **MN⊥MT KHÔNG xác nhận** (độc lập) | T7 EITHER 84.62% |
| Mở rộng giải ít bộ (7,8,1,2,5,3) | FU3 + V10636-LP | ⚠️ 4 cell strict, 0 BH-pass | An Giang G1 T5 ~+1.9pp |
| LAST2_REV/HEAD_TAIL + D-2/D-3/W-1 cho 4 cell | V10636-EXT | ❌ NEGATIVE, 0 BH-pass | max +1.90pp (D-1 vẫn tốt nhất) |
| MB D ← MB D-1 self-lag, G4 bộ 1-3 | V10636-MBSELF | ⚠️ G4#3 T6 FIRST2 **+5.97pp p=0.007** (raw, 0 BH) | G4#3 T6 |
| Weekday cells (G6#X CN, DB#1 T2) | V10636-DIG | ⚠️ **G7#4 T4 +7.20pp p=0.0014** (raw); G6#1 CN +3.35pp n.s. | G7#4 T4 |
| MN/MT làm nguồn, hoán đổi mọi hướng | V10636-CROSS | ✅ **268 BH-pass**; MT→MB = 0 BH-pass | MB G7#1 D→MN T7 +16.68pp* |
| Top ≥5 rule/miền/thứ/đài | V10667 ranking | ✅ Đã có 3 tài liệu MB/MN/MT | (xem region docs) |
| D/D-1 từ thời điểm nào | timing audit | 🔧 nửa đêm VN | — |

\* Lưu ý: rule +16.68pp (MB G7#1 **D**→MN) sau đó bị **loại vì vi phạm thứ tự xổ** (MB xổ sau MN cùng ngày) ở V10668. Mạnh nhất CÒN VALID = **MT G2#1 D-2 → MT +15.50pp** (self-lag). Xem `V10672_MASTER_VERIFICATION_REPORT_VN.md`.

---

## 3. Bài học lớn rút ra (để AI tool + owner không lặp lại)

1. **Lift cao ≠ rule thật.** V106.04/05/06 cho lift +20~35pp nhưng V107 null-test chứng minh **0/153,228 sống sót BH** → phần lớn là selection bias. ⇒ Luôn qua null-test + BH trước khi tin.
2. **MB D = MB D-2 GĐB: đã test 2 lần (FU1 + V10635), BÁC BỎ.** Đừng đào lại hướng này.
3. **Chỉ V10636-CROSS (full cross-region matrix) cho BH-pass hàng loạt** (268). Đây là nguồn rule đáng tin duy nhất → đã lọc temporal còn **28 rule forward-audit 90 ngày** (anchor 2026-06-02, closeout 2026-08-31).
4. **Thứ tự xổ MN→MT→MB là ràng buộc cứng**: same-day chỉ hợp lệ MN→MT, MN/MT→MB. 266 cell vi phạm đã loại (V10668).
5. **13 ứng viên FU4 (G4/G6/G7)** + 58 pre-register V10626 vẫn đang chờ, **chưa live**.

---

## 4. Trạng thái LIVE / chưa LIVE (quan trọng)

| Nhóm | Trạng thái | Live chưa? |
|---|---|---|
| 28 forward-audit rules (V10636-CROSS lọc temporal) | PRE_REGISTER_FORWARD_AUDIT, đang audit 90d | ❌ CHƯA (chờ 2026-08-31) |
| 71 pre-register V10626 (58 + 13 FU4) | PRE_REGISTER_ONLY | ❌ CHƯA |
| V106.03/04/05/06 broad rules | WEAK (V107 bác) | ❌ KHÔNG đưa live |
| MB D-2 self | REJECTED | ❌ |
| Production `mined_rules` đang chạy | 105 rule (cơ chế riêng, temporal-safe) | ✅ LIVE (đã verify V10672 sạch) |

→ **Không có rule nào từ các đợt đào trên được tự ý đưa vào production.** Tất cả ở trạng thái pre-register / forward-audit / rejected. Production hiện tại độc lập và đã verify sạch.

---

## 5. Liên kết verify (đối chiếu chéo)

- **Temporal + system-wide clean**: `V10672_MASTER_VERIFICATION_REPORT_VN.md`
- **Temporal fix gốc**: `V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md` + `V10669_TEMPORAL_VERIFICATION_REPORT_VN.md`
- **Source semantics (#Bộ, nguồn nhiều đài)**: `V10670_SOURCE_SEMANTICS_LEGEND.md`
- **Bộ numbering**: `V10667_BO_NUMBERING_LEGEND.md`
- **28 forward-audit rules**: `machine_readable/V10668_FORWARD_AUDIT_REGISTRY_FIXED.json`
- **3 tài liệu rule theo miền**: `V10667_RULES_MB/MN/MT_TARGET.md`

---

## 6. Kết luận cho anh

**Đã tổng hợp HẾT rồi anh** — mỗi đợt đào trong cả cuộc trò chuyện (38 giả thuyết, 10 nhóm phiên bản, từ 21/05 đến 02/06) đều có artifact + public package riêng. Thứ **trước đây còn thiếu** là một bản gom thống nhất để anh/AI tool nhìn cả hành trình trong 1 lần — **đó chính là file V10673 này**.

Tinh gọn: trong tất cả những gì mình đào, **chỉ V10636-CROSS cho rule đáng tin (28 rule forward-audit)**; phần còn lại hoặc yếu (V107 bác), hoặc bị bác bỏ (MB D-2), hoặc còn pre-register chờ 90 ngày. Production đang chạy độc lập và đã verify sạch.

---

**STATUS**: V10673 SESSION RULE-DIGGING JOURNEY — 38 episodes / 10 packages consolidated into one index. 1 VALIDATED (28 fwd-audit) · 71 pre-register · 4 weak · 2 rejected · all NON-LIVE except independent production.
