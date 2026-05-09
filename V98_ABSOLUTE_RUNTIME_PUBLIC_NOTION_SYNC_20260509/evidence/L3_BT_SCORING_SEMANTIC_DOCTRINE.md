# V99.2 L3 — BT Scoring Semantic Doctrine (LOCK)

**Generated**: 2026-05-09 12:55 VN  
**Owner directive**: V99.2 LANE 3 — lock semantic doctrine, không đổi production scoring.

---

## 1. Two scoring semantics defined

### `BT_STRICT_DAC_BIET` (Production KPI — LOCKED)
- **Definition**: BT trúng if và only if khớp 2D tail của Giải Đặc Biệt
- **Per region per day**: 1 special tail per region
- **Used by**: Production `final_bundles.bach_thu_status`, `/du-doan` UI, all historical hit-rate reports
- **Hit rate**: 0% across 14d/30d for ALL methods (n=413/728), Wilson 95% upper bound 0.4-0.7% — **statistical normal for rare event**

### `TAIL_ANY_PRIZE_DIAGNOSTIC` (Shadow / signal quality only)
- **Definition**: BT khớp 2D tail của BẤT KỲ giải nào trong all-prize set (~25-35 unique tails/day per region)
- **Used by**: V93 forensic "MB 56", V99 evaluator `bt_lenient_match`, signal-quality reports
- **Hit rate**: 35-50% — expected baseline

---

## 2. Decision rules (LOCK)

| Rule | Decision |
|---|---|
| Production KPI | BT_STRICT_DAC_BIET — UNCHANGED |
| UI display | "Bạch thủ" chỉ tính khớp ĐB |
| V93 MB 56 claim | Valid dưới TAIL_ANY_PRIZE_DIAGNOSTIC, NOT production bug |
| Bundle conversion replay | Báo riêng strict_save/break + diagnostic_save/break |
| Method promotion | Cần net_strict ≥ +5pp + n≥30 + Wilson CI lower > 0 + owner approval |
| No mixing | Tuyệt đối không claim "lenient hit = BT production win" |

---

## 3. Owner Decision Record

**Recommendation**: Keep STRICT_DAC_BIET. Pilot LENIENT in shadow only.

→ Until owner explicitly directs otherwise, production scoring stays STRICT.  
→ FU-V99-BT-SCORING-DEBATE → DEFAULT KEEP STRICT (not closed; can revisit at 30d gate 2026-06-08 if evidence justifies).

---

## 4. Implications for V93 MB 56

V93 "AI bắt 56 nhưng bundle làm rơi" = TRUE under DIAGNOSTIC, NOT a production bug under STRICT.  
Bundle replay must report both lanes. Owner gate uses STRICT.

---

**STATUS**: BT semantic doctrine LOCKED. Production STRICT. Diagnostic shadow OK. NO production scoring change.
