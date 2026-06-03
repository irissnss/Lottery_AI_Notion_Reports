# V10690 — PHASE 4: DEPLOY PLAN (lane-test only) — chờ owner xác nhận push

> **Generated**: 2026-06-03 14:10 VN | **Phase**: 4/5 | **Cổng 1+2+3**: 🟢 đều XANH
> **Trạng thái**: deploy script SẴN SÀNG (dry-run OK), **CHƯA push VPS** — chờ owner OK.

---

## 0. Vì sao dừng ở đây xin xác nhận

Phát hiện QUAN TRỌNG khi khảo sát cơ chế deploy:

> Orchestrator chuẩn `web/_deploy_orchestrator.py` có `DEPLOY_FILES` **hardcode gồm `gpt_analyzer.py`** (sẽ làm ĐỔI official MB context) và **THIẾU** `mb_rule_ranker.py` / `_v10689` / `_v10690`.

→ **KHÔNG dùng được orchestrator chuẩn.** Em đã viết deploy script **tùy chỉnh** chỉ đẩy file lane-test an toàn. Vì đây là (1) production tiền thật + (2) deploy path tùy chỉnh, em xin owner xác nhận trước khi push thật.

---

## 1. File deploy AN TOÀN (chỉ lane test)

| File | Vai trò | Đụng official? |
|---|---|---|
| `mb_rule_ranker.py` | sinh `mb_t2_manual_daily` + `mined_rules_mb_daily` | KHÔNG (data table) |
| `_v10689_mb_manual_rolling_remeasure.py` | drive_weight rolling | KHÔNG |
| `_v10690_mb_manual_drive_shadow.py` | 4 nhánh → `mb_experimental_preview_shadow` | KHÔNG (lane test) |
| `_v10690_register_experiments.py` | đăng ký 3 experiment | KHÔNG |
| `scheduler.py` | cron MB (20:25/23:50 gated; 20:30/17:00 ranker) | KHÔNG (chỉ thêm job MB) |
| `main.py` | flag `MB_MANUAL_EXPERIMENT_ENABLE` | KHÔNG (flag mới) |

## 2. File TUYỆT ĐỐI KHÔNG đẩy (giữ official zero-drift)

| File | Lý do |
|---|---|
| `rule_engine.py` | nhánh MB-daily → official MB đọc snapshot (đổi số) |
| `gpt_analyzer.py` | MB-context section → đổi prompt official MB |
| `prompt_registry.py` | CTX-MB metadata |

→ Official VPS giữ nguyên 3 file này → official MB **đọc `mined_rules` thẳng như cũ** → zero-drift đảm bảo.

---

## 3. Quy trình deploy (script `_v10690_deploy_lane_only.py`)

```
1. Hash 4 official tables trên VPS (BEFORE)
2. SFTP upload 6 file an toàn (+ .bak mỗi file trên VPS)
3. Bật flag CHỈ trên VPS: sed MB_MANUAL_EXPERIMENT_ENABLE False->True
4. py_compile 6 file trên VPS
5. register 3 experiment + 1 lần materialize smoke
6. systemctl restart lottery + /api/health
7. Hash 4 official tables (AFTER) → PHẢI IDENTICAL, lệch → ROLLBACK tự động (.bak)
```

**An toàn:** mặc định DRY-RUN; chỉ chạy thật khi `--live`. Rollback tự động nếu official lệch dù 1 hash.

---

## 4. Cổng đã xanh (điều kiện Phase 4)

| Cổng | Kết quả |
|---|---|
| CỔNG 1 (V10689 rolling) | 🟢 official zero-drift, 108/108, 55/55, 18/18 |
| CỔNG 2 (V10690 4 nhánh) | 🟢 official zero-drift, gate T6/7/CN, 108/108, 55/55, 18/18 |
| CỔNG 3 (forward-audit) | 🟢 16/16, drive_weight=0 ×9, 108/108, 55/55, 18/18 |

---

## 5. Rủi ro + giảm thiểu

| Rủi ro | Giảm thiểu |
|---|---|
| Đẩy nhầm file official | Script HARDCODE 6 file an toàn; KHÔNG đụng rule_engine/gpt_analyzer/prompt_registry |
| Official lệch sau deploy | Hash before/after + auto-rollback .bak |
| Cron lỗi | py_compile trên VPS trước khi restart; gated flag |
| SSH/key không có quyền | Script báo lỗi sớm (connect fail) trước khi đụng gì |
| Service không lên | health check; rollback nếu cần |

---

## 6. Cần owner xác nhận

CỔNG 1+2+3 đều XANH (đúng điều kiện Phase 4 của master prompt). Deploy script tùy chỉnh đã sẵn sàng + dry-run OK. Em **chưa push** vì:
1. Production tiền thật + deploy path tùy chỉnh (orchestrator chuẩn không an toàn).
2. Đúng tinh thần "cẩn thận tỉ mỉ" của anh.

**Anh xác nhận em chạy `python web/backend/_v10690_deploy_lane_only.py --live` để deploy thật lên VPS lane test không?** (hoặc anh muốn review file/script trước).

---

## 7. CHECKLIST

| Phase | Trạng thái |
|---|---|
| 1 V10689 rolling | 🟢 XONG |
| 2 V10690 experiments | 🟢 XONG |
| 3 T6/T7/CN forward-audit | 🟢 XONG |
| **4 Deploy VPS** | ⏳ **script sẵn sàng — chờ owner OK push** |
| 5 Đo 30d | ⏳ |

---

**Bottom line**: Mọi cổng XANH, deploy script tùy chỉnh chỉ-lane-test đã sẵn sàng + có auto-rollback. Em dừng ở ranh giới production chờ anh ra lệnh "deploy" — vì orchestrator chuẩn không an toàn và đây là tiền thật.
