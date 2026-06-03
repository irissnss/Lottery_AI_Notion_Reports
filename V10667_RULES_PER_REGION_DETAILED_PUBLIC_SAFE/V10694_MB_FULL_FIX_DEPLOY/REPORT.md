# V10694 — MB FULL FIX (E1–E8) → VERIFY → DEPLOY LANE

> **Pha:** CODE E1–E8 (local) → VERIFY → BACKUP + đối soát 3 chiều → **DEPLOY LANE-ONLY (đã thực hiện)** → báo cáo.
> **Data as-of:** 2026-06-03. **Official 4-table ZERO-DRIFT: PASS trên CẢ local lẫn VPS** (4/4 IDENTICAL trước & sau).
> **MN/MT bất biến.** Mọi thay đổi chỉ ghi `du_doan_test_*` / `mb_experimental_preview_shadow` / bảng `mb_*`-only.
> Nền: per-position rule-driven V10693. Trọng tâm: vá top3 & xiên3 mà không tụt top1/top2.

---

## A. KẾT QUẢ CHÍNH — VÁ TOP3/XIÊN3 (walk-forward TRUNG THỰC, no look-ahead)

| Cửa sổ | Method | top1 | top2 | **top3** | xiên2 | **xiên3** | coverTop4 | official top1 |
|---|---|---|---|---|---|---|---|---|
| 60d | V1 (nền) | 25.0 | 26.7 | 15.0 | 11.7 | 1.7 | 63.3 | 13.3 |
| 60d | **V2 (+E3)** | **28.3** | **30.0** | **23.3** | 11.7 | **5.0** | **71.7** | 13.3 |
| 90d | V1 (nền) | 22.2 | 25.6 | 18.9 | 8.9 | 1.1 | 66.7 | 21.1 |
| 90d | **V2 (+E3)** | **24.4** | **27.8** | **23.3** | 8.9 | **3.3** | **67.8** | 21.1 |

→ **top3 vá: 18.9→23.3 (90d), 15.0→23.3 (60d); xiên3: 1.1→3.3 (90d), 1.7→5.0 (60d)** — và **top1/top2 KHÔNG tụt mà còn tăng**. Đúng mục tiêu. (Scoreboard E6: V2 PASS cả 60d & 90d; V1 90d chỉ NEUTRAL.)

⚠️ Trung thực: 90d top1 V2 (24.4%) vẫn ≈ official (21.1%) và ≈ random (23.7%) → V2 là **nguồn độc lập + bổ trợ top2/xiên**, CHƯA thay BT official (đúng chỉ đạo, để sau 2 tuần live).

---

## B. ĐÒN NÀO HIỆU QUẢ (validate trung thực, không tô hồng)

| Mã | Ý tưởng | Kết quả walk-forward | Quyết định |
|---|---|---|---|
| **E3** | Bơm same-day MN(D)+MT(D) **full board** vào tập đuôi (board_bonus=0.12) | Vá mọi vị trí: top3 +4.4pp, xiên3 +2.2pp, top1/2 tăng | ✅ **ÁP DỤNG (= V2)** — đòn chính |
| E2 | Co-occurrence rerank top2/top3 theo top1 | Làm **TỤT** top2 (27.8→23.3) & xiên2 | ❌ **LOẠI** (giữ diagnostic) — trung thực |
| E2' | Marginal freq theo thứ | top3 tăng nhưng top1 tụt (22.2→20) | ❌ loại |
| E1/a/d | Per-position anti-herd rule-driven (nền V10693) | top1 13.3%→25% (60d) | ✅ nền |
| E4/c | Coverage: board đã nâng cover 66.7→67.8; cover_top4 vào scoreboard | đạt | ✅ qua E3 + scoreboard |
| E5/f | 77 MANUAL + 9 forward-audit confirm-only (drive_weight=0, không drive) | guard tam tầng giữ nguyên | ✅ infra |
| E6 | Scoreboard per-position+xiên2/3/4+coverage (bảng `mb_perpos_scoreboard`) | 4 dòng V1/V2×60/90d + verdict | ✅ |
| E7 | Field đọc `clone_warning` + "official unchanged" vào `/api/du-doan-test/mb` | code local xong | ⏸️ **DEPLOY-DEFER** (main.py xung đột 3 chiều VPS) |
| E8 | Đồng bộ runtime VPS↔git | đối soát xong (xem D) | ✅ đối soát; commit MN/MT để owner |

---

## C. PHÂN TÍCH LIÊN ĐỚI (E1–E8 → ảnh hưởng → đã kiểm tương thích)

| Thay đổi | File/bảng/endpoint | Ảnh hưởng MN/MT? | Ảnh hưởng official? | Đã kiểm |
|---|---|---|---|---|
| `_v10693_mb_perpos_predictor.py` (mới) | ghi `mb_experimental_preview_shadow`, `du_doan_test_experiments`, `mb_perpos_scoreboard` | Không (chỉ region='MB') | Không (VPS official code **0 ref** tới bảng này) | ✅ liên-đới VPS grep=0 |
| `mb_rule_ranker.py` (mới VPS) | ghi `mined_rules_mb_daily`, `mb_t2_manual_daily`, `mb_rule_context` | Không (đọc mined_rules, ghi bảng MB riêng) | Không (rule_engine VPS **0 ref** `MB_DAILY_RANK`) | ✅ |
| `_v10689_*` (mới VPS) | ghi cột rolling `mb_t2_manual_daily` | Không | Không | ✅ |
| artifact JSON (V10667/V10636) | đọc-only nguồn 77 rule | Không | Không | ✅ |
| cron root 23:55 | chạy chain MB-only | Không | Không (KHÔNG đụng scheduler.py) | ✅ |
| E7 `main.py` (MB handler, local) | thêm field đọc response API MB | Không (chỉ handler MB) | Không (field đọc) | ⏸️ chưa deploy |

---

## D. ĐỐI SOÁT 3 CHIỀU git↔VPS↔local + DEPLOY

**Phát hiện (đúng cảnh báo owner — VPS runtime MN/MT đi trước git):**
- `main.py`: VPS `d1514ece` (06-03 15:49, MN/MT hôm nay) ≠ git `b93b39d5` (05-31) ≠ local → **3 chiều khác** → KHÔNG upload (E7 defer).
- `scheduler.py`: VPS = git (`26d94a97`); local khác → KHÔNG upload (cron qua root crontab thay thế).
- `_materialize_mb_experimental_preview_shadow.py`: VPS có sẵn (đủ hàm cần) → KHÔNG đè.
- 5 file MB mới: **ABSENT trên VPS** → thuần thêm mới, 0 xung đột.

**Deploy thực hiện (script chuyên biệt `_v10694_deploy_lane_safe.py`, KHÔNG dùng `_v10690_deploy_lane_only.py` vì SAFE_FILES của nó chứa main.py/scheduler.py = nguy hiểm):**
1. Hash official BEFORE.
2. Upload 3 file: `_v10693_mb_perpos_predictor.py`, `_v10689_mb_manual_rolling_remeasure.py`, `mb_rule_ranker.py` (+ py_compile OK).
3. Upload 3 artifact JSON (nguồn 77 rule) → `manual_count` 9→**86**.
4. Chạy chain: ranker force → rolling (77 xử lý) → register → backfill 60 (V2).
5. Hash official AFTER → **IDENTICAL (ZERO-DRIFT PASS)**.
6. Cài root crontab 23:55 VN (MB-only chain hằng ngày) — KHÔNG đụng scheduler.py.
7. Smoke: V2 branch = 60 rows VPS, `/api/health` 200, manual rows = 86.

**Backup:** `.pre` local (main.py, scheduler.py, _v10693) + official hash baseline; `.pre_v10694` trên VPS cho mọi file ghi đè (không có file nào bị đè vì 3 file đều mới).

---

## E. ĐÃ DEPLOY GÌ / CHƯA DEPLOY GÌ

**Đã deploy (VPS lane, official bất biến):**
- 3 file MB + 3 artifact JSON.
- Bảng MB-only: `mined_rules_mb_daily` (35), `mb_t2_manual_daily` (86), `mb_experimental_preview_shadow` (branch `MB_PERPOS_RULEDRIVEN_V2` = 60), `mb_perpos_scoreboard`.
- Cron 23:55 VN hằng ngày → đồng hồ **2 TUẦN LIVE** bắt đầu từ 2026-06-04.

**CHƯA deploy (defer, có lý do):**
- **E7** (`main.py` field đọc): main.py VPS đang giữ thay đổi MN/MT hôm nay (3 chiều khác) → KHÔNG đè. Cần merge từng dòng có chủ đích hoặc owner commit runtime VPS trước. Code đã sẵn ở local.
- **Cron qua app scheduler** (`scheduler.py`): dùng root crontab thay thế để tránh xung đột; nếu owner muốn dời vào scheduler.py thì merge sau khi đồng bộ.
- **Commit runtime VPS MN/MT vào git** (E8): em KHÔNG tự commit công việc MN/MT hôm nay của owner (tránh "tự đoán" — rule 4.4). Đề nghị owner commit/bảo toàn `main.py`/`_v10679`/`_v10680`/`_v10692`/`du-doan-test.html` trên VPS.

---

## F. SAU 2 TUẦN LIVE — TIÊU CHÍ (scoreboard E6)
- PASS nếu: top1 ≥ official AND top1 ≥ ~random AND top2 ≥ ~random AND xiên2 ≥ 2× official.
- Nếu PASS bền 2 tuần out-of-sample → cân nhắc nâng V2 thành nguồn chính / blend với official. CHƯA làm bây giờ.

## G. FILE
- Code (private): `_v10693_mb_perpos_predictor.py`, `mb_rule_ranker.py`, `_v10689_*`, `_v10694_deploy_lane_safe.py`, `_v10694_install_cron.py`.
- Evidence: `evidence/V10694_SCOREBOARD.json`.

---

**official untouched, MN/MT bất biến — đã chứng minh bằng hash 4 bảng IDENTICAL (local + VPS) trước & sau.**
