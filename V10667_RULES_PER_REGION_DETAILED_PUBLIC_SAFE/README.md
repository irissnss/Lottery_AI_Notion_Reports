# V10667 — Detailed Rule Reference Per Region (PUBLIC-SAFE)

Tài liệu chi tiết cho 3 miền target (MN, MT, MB) với:
- Per-weekday breakdown (T2-CN)
- Per-station hit rate (đài nào contribute nhiều nhất)
- Worked examples (3 ngày gần nhất rule trúng)
- Strength classification (BH-pass, STRONG, MODERATE, MARGINAL, WEAK)

## 🏷️ Read first #0000 — BẢNG TỔNG HỢP TOÀN BỘ RULES + NHÃN (V10675, mới nhất)

**[V10675_ALL_RULES_LABELED_VN.md](./V10675_ALL_RULES_LABELED_VN.md)** — gắn nhãn trạng thái từng rule, KHÔNG bỏ sót: **183 rule qualifying** (28 forward-audit + 155 pool) mỗi cái có nhãn 🟢 mạnh lên / 🟡 ổn định / 🔴 yếu đi (+ ⚠️ recent decay), **266 cell bị loại** (vi phạm thứ tự xổ), + tham chiếu 71 pre-register / weak / rejected. Tổng: 🟢69 / 🟡56 / 🔴58 / ⚠️39. Sinh tự động từ dữ liệu.

## 📈 Read first #000 — THỰC NGHIỆM ĐO LẠI ĐỘ MẠNH (V10674)

**[V10674_RULE_STRENGTH_REMEASURE_VN.md](./V10674_RULE_STRENGTH_REMEASURE_VN.md)** — đo lại 28 rule forward-audit trên DB hiện tại (sync VPS). **28/28 tái hiện chính xác (Δ=0, 0 vướng bug temporal)**; xu hướng lịch sử: 12 rule mạnh lên, 8 ổn định, 8 yếu đi (3 cái recent-60 <5pp cần canh); 155 cell pool bổ sung; 266 cell vi phạm vẫn loại đúng. Chưa đổi vs đăng ký vì DB chưa có data sau mốc 02/06.

## 🗺️ Read first #00 — TỔNG HỢP CẢ HÀNH TRÌNH ĐÀO RULES (V10673)

**[V10673_SESSION_RULE_DIGGING_JOURNEY_VN.md](./V10673_SESSION_RULE_DIGGING_JOURNEY_VN.md)** — gom 38 đợt đào (21/05→02/06, 10 nhóm phiên bản V106.03→V10672) vào 1 index: đào gì · kết quả (validated/pre-register/yếu/bác bỏ) · link. Trả lời "đã tổng hợp hết chưa". **Chỉ V10636-CROSS cho rule đáng tin (28 forward-audit); còn lại yếu/bác bỏ/pre-register.**

## ✅ Read first #0 — MASTER VERIFICATION (V10672, 2026-06-02)

**[V10672_MASTER_VERIFICATION_REPORT_VN.md](./V10672_MASTER_VERIFICATION_REPORT_VN.md)** — verify TOÀN BỘ rules trong hệ thống (không chỉ session này): production LIVE (105 rule) + máy sinh rule `_seed_rules` + pre-register (63) + 11 research mine (~286,000 rule, 234,040 dòng cross-region).

**Kết luận:** PRODUCTION SẠCH 100% · pipeline khai thác chuẩn chỉ sinh lag≥1 (lag0=0 tuyệt đối) → bug temporal CHỈ tồn tại trong 1 grid thử nghiệm (V10636-CROSS) và đã xử lý trọn vẹn. Dữ liệu máy đọc: [machine_readable/V10672_ALL_ARTIFACTS_TEMPORAL_VERIFY.json](./machine_readable/V10672_ALL_ARTIFACTS_TEMPORAL_VERIFY.json).

## 🕐 Read first #1 — TEMPORAL CAUSALITY (CRITICAL)

**[V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md](./V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md)**

Vietnam draws sequentially: **MN (~16:10) → MT (~17:10) → MB (~18:15)**.

A same-day cross-region rule where the source draws AFTER the target (MT(D)→MN(D), MB(D)→MN(D), MB(D)→MT(D)) is a TEMPORAL CAUSALITY VIOLATION — you'd be using data from the future. These 266 invalid cells (36 BH-pass) have been **removed**. Per region:
- **MN target** (draws first): only lag≥1 sources or MN self-lag
- **MT target** (draws 2nd): MN(D) same-day OK, MB(D) removed
- **MB target** (draws last): no same-day temporal limit

## ⚠️ Read first #2 — Bộ Numbering Convention

**[📖 V10667_BO_NUMBERING_LEGEND.md](./V10667_BO_NUMBERING_LEGEND.md)** — quy ước đánh số bộ cho mỗi giải (G2/G4/G6/G7 MB, G3 MN/MT).

Owner 02/06/2026 đã bổ sung G.4 MB làm nguồn rules. Mỗi bộ được đánh số rõ ràng theo position:

**G.4 MB (4 bộ):**
```
Bộ 1 [top-left]    Bộ 2 [top-right]
Bộ 3 [bottom-left] Bộ 4 [bottom-right]
```

Ví dụ verify MB 31/05/2026: G.4 bộ 1=7717, bộ 2=7829, bộ 3=5183, bộ 4=4559.

## Read next

[`V10667_RULES_INDEX.md`](./V10667_RULES_INDEX.md) — hub navigation.

## 3 per-region documents

| Target | Document | Lines |
|---|---|---|
| **MB** | [V10667_RULES_MB_TARGET.md](./V10667_RULES_MB_TARGET.md) | 1,711 |
| **MN** | [V10667_RULES_MN_TARGET.md](./V10667_RULES_MN_TARGET.md) | 2,061 |
| **MT** | [V10667_RULES_MT_TARGET.md](./V10667_RULES_MT_TARGET.md) | 2,150 |

## Supplementary

- [V10667_RULES_FLAT_RANKING.md](./V10667_RULES_FLAT_RANKING.md) — flat ranking (all 3 regions in one MD)
- [machine_readable/V10667_RULES_PER_REGION_RAW.json](./machine_readable/V10667_RULES_PER_REGION_RAW.json) — structured per-station data
- [machine_readable/V10668_FORWARD_AUDIT_REGISTRY_FIXED.json](./machine_readable/V10668_FORWARD_AUDIT_REGISTRY_FIXED.json) — **28 BH-pass rules (temporal-clean, 7 invalid removed)**. Bản 35-rule cũ đã DEPRECATED + gỡ khỏi public.
- [V10672_MASTER_VERIFICATION_REPORT_VN.md](./V10672_MASTER_VERIFICATION_REPORT_VN.md) + [V10669_TEMPORAL_VERIFICATION_REPORT_VN.md](./V10669_TEMPORAL_VERIFICATION_REPORT_VN.md) + [V10670_SOURCE_SEMANTICS_LEGEND.md](./V10670_SOURCE_SEMANTICS_LEGEND.md) — verification + source semantics

## Methodology summary

- **Data source**: V10636 series audit (CROSS + DIG + LAGS + MBSELF)
- **Total unique cells**: 3,696
- **p<0.05 raw**: 431
- **BH-pass FDR α=0.05**: 268 raw → **232 temporal-valid** ⭐ (36 same-day violations removed; gold standard, survives multiple-testing correction)
- **Lift ≥ +5pp**: 357

## Owner constraints (applied)

- MN/MT G3 = source only (NO MB G3 source)
- MB source whitelist: DB, G1, G2, G4, G6, G7
- MN/MT source whitelist: DB, G1, G2, G3 (both bộ), G5, G7, G8

## Status

- All rules at `PRE_REGISTER_FORWARD_AUDIT`
- `live_eligible = False` for all
- Forward audit anchor: 2026-06-02
- Earliest closeout: 2026-08-31

Public push approved by owner for external AI tool consumption.

## Safety

- Read-only audit
- No DB/JSONL/log files
- No VPS IP, no API keys
- No official mutation
