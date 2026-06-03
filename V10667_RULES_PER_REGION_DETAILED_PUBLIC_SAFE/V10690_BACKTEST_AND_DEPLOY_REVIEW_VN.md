# V10690 — Walk-forward backtest 30d + review deploy script (phân tích trước khi deploy)

> **Generated**: 2026-06-03 14:25 VN | Owner: "chạy B+C, push GitHub phân tích trước, rồi mới deploy".
> **Trạng thái**: REPORT-ONLY. CHƯA deploy VPS. Official KHÔNG đụng.

---

## 1. Walk-forward backtest 30 ngày (HONEST — không look-ahead)

**Method**: với mỗi ngày D (30 ngày MB gần nhất), `drive_weight` mỗi MANUAL rule tính bằng rolling 8W **chỉ dùng dữ liệu ≤ D** (loại mining gap). Sau đó chấm 4 nhánh cho ngày D, so với control (official baseline). Đây là walk-forward của quyết định DRIVE — proxy trung thực nhất trước shadow 30d thật.

| Nhánh | n | BT hit | BT hit% | ΔBT vs CTRL | flip_win | false_promo | đổi pick/30 |
|---|---:|---:|---:|---:|---:|---:|---:|
| **CTRL** (official) | 30 | 2 | **6.7%** | — | — | — | — |
| **A** full-swap MANUAL | 30 | 5 | **16.7%** | **+10.0pp** | 4 | 1 | 18 |
| **B** BH-pass MANUAL | 30 | 4 | 13.3% | +6.7pp | 2 | **0** | 8 |
| **C** blend 0.7/0.3 | 30 | 3 | 10.0% | +3.3pp | 1 | **0** | 4 |

### Đọc kết quả (trung thực)

- **Control (official) BT chỉ 6.7%** trong 30 ngày — khớp với "MB tệ" (roadmap ~9% 22d). Nền rất thấp.
- **Cả 3 nhánh đều BEAT control** về BT hit-rate.
  - **A** (+10pp) mạnh nhất nhưng churn cao (18/30 đổi pick) + 1 false promotion.
  - **B** (+6.7pp) hồ sơ tốt nhất: **0 false promotion**, churn vừa (8/30) — rủi ro thấp.
  - **C** (+3.3pp) bảo thủ nhất: 0 false promotion, churn thấp (4/30).
- **Verdict theo ngưỡng owner** (flip_win≥8/30 VÀ false_promo≤5/30 VÀ ΔBT≥+5pp): cả 3 = **NEUTRAL** (ΔBT dương + false_promo thấp, nhưng flip_win chưa đạt 8/30).

### Caveat (phải nói rõ)

- Rule SET = 77 MANUAL hôm nay (ổn định); chỉ `drive_weight` là as-of → walk-forward của quyết định drive, KHÔNG phải out-of-sample tuyệt đối.
- n=30, BT hit thấp (2-5) → **mẫu nhỏ, nhiễu cao**. +10pp của A có thể co lại.
- **Test thật = shadow 30d forward** sau deploy (out-of-sample hoàn toàn).

→ Tín hiệu **khích lệ** (cả 3 beat control yếu), nhưng **chưa đủ mạnh để PASS** → đúng lý do cần shadow forward đo tiếp, KHÔNG promote official vội.

Machine-readable: `machine_readable/V10690_BACKTEST_WALKFORWARD.json`.

---

## 2. Review deploy script (owner muốn xem trước)

File: `web/backend/_v10690_deploy_lane_only.py` (custom, vì orchestrator chuẩn đẩy nhầm `gpt_analyzer.py`).

### 2.1 File ĐẨY (6, an toàn lane-test)

```
web/backend/mb_rule_ranker.py                      # sinh mb_t2_manual_daily + mined_rules_mb_daily
web/backend/_v10689_mb_manual_rolling_remeasure.py # drive_weight rolling
web/backend/_v10690_mb_manual_drive_shadow.py      # 4 nhánh -> mb_experimental_preview_shadow
web/backend/_v10690_register_experiments.py        # đăng ký 3 experiment
web/backend/scheduler.py                           # cron MB (gated)
web/backend/main.py                                # flag MB_MANUAL_EXPERIMENT_ENABLE
```

### 2.2 File KHÔNG ĐẨY (giữ official zero-drift)

```
rule_engine.py        # nhánh MB-daily -> đổi official MB
gpt_analyzer.py       # MB-context -> đổi prompt official MB
prompt_registry.py    # CTX-MB metadata
```

### 2.3 Quy trình (auto-rollback)

```
1. SSH hash 4 official tables (BEFORE)
2. SFTP upload 6 file (+ .bak_<ts> mỗi file)
3. sed bật MB_MANUAL_EXPERIMENT_ENABLE False->True (CHỈ trên VPS)
4. py_compile 6 file trên VPS
5. register 3 experiment + 1 materialize smoke
6. systemctl restart lottery + /api/health
7. hash 4 official tables (AFTER) == BEFORE? Nếu LỆCH -> tự rollback .bak + restart
```

Mặc định DRY-RUN. Chạy thật: `python web/backend/_v10690_deploy_lane_only.py --live`.

### 2.4 Điểm an toàn

| Cơ chế | Đảm bảo |
|---|---|
| Hardcode 6 file an toàn | Không thể đẩy nhầm rule_engine/gpt_analyzer |
| Hash official before/after | Phát hiện drift tức thì |
| Auto-rollback .bak | Lệch 1 hash → khôi phục ngay |
| Flag gated | Cron experiment chỉ chạy khi flag True (VPS only) |
| py_compile trên VPS | Không restart với code lỗi |

---

## 3. Đề xuất (sau phân tích)

| Lựa chọn | Em đánh giá |
|---|---|
| **Deploy cả 3 nhánh shadow** (A/B/C) đo 30d forward | ⭐ Khuyến nghị — backtest cho thấy tiềm năng, shadow không đụng official, để data forward quyết định |
| Deploy chỉ B (an toàn nhất: 0 false promo) | OK nếu owner muốn hẹp |
| Chưa deploy, đợi thêm | Mất cơ hội tích lũy data forward sớm |

Em nghiêng **deploy cả 3 shadow** vì: (1) không đụng official, (2) backtest khích lệ, (3) shadow là cách duy nhất có data out-of-sample thật để quyết promote/drop sau 30d.

---

## 4. CHECKLIST

| Phase | Trạng thái |
|---|---|
| 1 V10689 rolling | 🟢 |
| 2 V10690 4 nhánh | 🟢 |
| 3 T6/T7/CN forward-audit | 🟢 |
| Backtest 30d walk-forward | 🟢 (báo cáo này) |
| 4 Deploy VPS | ⏳ chờ owner OK sau khi đọc phân tích |
| 5 Đo 30d forward | ⏳ |

---

**Bottom line**: Backtest 30d — cả 3 nhánh beat control yếu (A +10pp, B +6.7pp/0 false-promo, C +3.3pp), verdict NEUTRAL (mẫu nhỏ). Deploy script custom an toàn (auto-rollback, không đụng official). Em đề xuất deploy 3 nhánh shadow để đo forward 30d, nhưng chờ anh quyết sau khi đọc.
