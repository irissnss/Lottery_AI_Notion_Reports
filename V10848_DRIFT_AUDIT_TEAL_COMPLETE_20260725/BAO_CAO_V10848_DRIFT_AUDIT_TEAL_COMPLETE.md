# V10848 — TRẢ LỜI DỨT ĐIỂM "VPS VÀ LOCAL KHÁC NHAU?": AUDIT MD5 TOÀN BỘ — LÕI RUNTIME KHỚP 100% · TEAL 14/14 HOÀN TẤT · KIỂM SOÁT ĐỊNH KỲ

- Phiên: 25/07/2026 21:57 → 22:4x. Bối cảnh: phiên thay áo teal (V10846/V10847, agent Claude Code) báo "VPS lệch repo 733 file" + "5 trang VPS khác local" → owner lo hệ dự đoán không khớp code fix, sợ hỏng công sức đo lường.

## 1. CÂU TRẢ LỜI NGẮN CHO OWNER

1. **Hệ dự đoán/đo lường trên VPS KHỚP 100% code fix hiện hành** — audit md5 từng file chứng minh, không phải suy đoán.
2. **"733 file lệch" là ảo giác của git trên VPS** — không phải 733 file runtime khác nhau thật.
3. **"5 trang VPS khác local" chẩn đoán lại: LOCAL MỚI HƠN VPS** (không có thay đổi nào trên VPS bị mất) → đã deploy nốt, thay áo **14/14 trang HOÀN TẤT**.
4. Tình huống xấu nhất **có kiểm soát**: rollback nhiều lớp + tool audit drift định kỳ vừa cài.

## 2. AUDIT MD5 (evidence: `artifacts/vps_drift_20260725/audit_result.json`)

### 2.1 Backend `web/backend/*.py`
| Nhóm | Số file | Kết luận |
|---|---|---|
| MATCH (md5 trùng) | 133 | Gồm TOÀN BỘ runtime: `main.py` `scheduler.py` `database.py` `gpt_analyzer.py` `model_registry.py` `_v10759_money_board.py` `_v10821/22/29/32` `_materialize_adaptive_exploit_v1.py` `_v10844_mb_whatif.py` `_v10834_lock_freeze.py` selfcheck/contract… |
| DIFF nhưng CRITICAL | 4 | `vn_timezone.py` `training_lock.py` `_v10773_three_layer_scoreboard.py` `_v10803_chase_bias_shadow.py` — **diff normalize = 0 dòng, chỉ lệch CRLF/LF** (lịch sử SFTP vs checkout) |
| DIFF khác | 277 | Script chẩn đoán/test/deploy cũ (`_analyze_* _check_* _test_* _debug_*`…) — KHÔNG chạy trong runtime |
| local-only | 616 | Probe/commit script các phiên — không cần deploy (by design) |
| VPS-only | 4 | Artifact cũ vô hại (`__trigger_reload__` , smoke cũ…) |

### 2.2 Vì sao git trên VPS báo 733 file?
- Quy trình deploy chủ đích từ trước tới nay = **SFTP đúng file đổi + verify compile/behavior/hash từng phiên** (đúng như owner nhớ "fix nào cũng deploy ghi nhận đầy đủ" — audit xác nhận điều này ĐÚNG cho runtime).
- Nhưng **git HEAD trên VPS không bao giờ được update** (VPS không phải git checkout đồng bộ) → `git diff` so working-tree hiện tại với HEAD cổ → phồng 733 file. Con số này KHÔNG đo drift thật.

### 2.3 "5 trang lệch" — sự thật từng dòng (diff đã in evidence)
- `accuracy/search/v82-monitor/viewer/user-view.html`: bản local = bản VPS **+ 1–6 dòng reskin** (`data-theme="dark"`, link `theme-v2.css`, khối viewer-safe CSS user-view). VPS **không có** dòng riêng nào.
- `accuracy.js`: local đã fix model-id **`claude-opus-4-6`**, VPS còn id cổ `claude-opus-4-20250514` (tier/màu opus chết trên trang accuracy) → deploy local là SỬA BUG live.
- `styles.css`, `model-names.js`: chỉ lệch line-ending, nội dung y hệt.

## 3. HOÀN TẤT THAY ÁO (V10848 phần deploy)

- Inline `theme-v2.css` vào 5 trang cuối (đúng kỹ thuật đã chứng minh ở 9 trang V10847 — backend serve route từng-file nên asset mới sẽ 404 nếu link ngoài).
- Deploy 5 trang + `accuracy.js`: **md5 khớp 6/6**, 0 ref ngoài, serve `user-view=200 accuracy=200 health=200`; backup per-file `.bak_pre_v10848` (6 file).
- `user-view` viewer-safe CSS đã live (ẩn KPI/model/history — hướng an toàn, ít lộ thông tin hơn); **B2 backend (API viewer-safe) vẫn chờ owner ký**.
- → **TEAL 14/14 trang HOÀN TẤT** (9 trang phiên V10847 + 5 trang phiên này).

## 4. ĐO LƯỜNG SAU THAY ÁO — NGUYÊN VẸN (kiểm chứng live)

- Cron tối nay chạy đủ SAU reskin: **M2s 20:50** (25/07 written=3: MB 05✓ · MN 76✗ · MT 74✗) · **rule-cond 21:00** (MB 05✓ · MN 04✓ · MT 74✗) · **V10844 21:10 lần đầu tự chạy đúng lịch** (row forward: /choi=GATE · laneV2 05✓ · laneV3 05✓).
- Journal 0 lỗi từ 19:00; marker sống trên live: choi `warn-strip`=2 + `form-line`=3 (V10845), monitoring `sectionMbWhatif`+`loadMbWhatif` (V10844), du-doan FINAL BUNDLE.
- Lũy kế M2s−M0 forward 19–25/07: **12/21 vs 10/21 (+9.5pp)** — đọc promote 28/07 (ngưỡng +5pp n≥30).

## 5. KIỂM SOÁT TÌNH HUỐNG XẤU NHẤT (trả lời câu 2)

| Lớp | Cụ thể |
|---|---|
| Rollback frontend | Tarball pre-teal 21:33 (`web/frontend_backup_pre_teal_20260725.tgz`, chứa V10845) + per-file `.bak_pre_v10848` — hoàn tác 1 lệnh |
| Rollback backend | `/root/backups_v10844/` + `/root/backups_v10845/` (pre-fix từng phiên) + backup local `backups/v104xx_pre/` |
| Lịch sử code | Git private đầy đủ (mỗi phiên đều push) |
| DB official | KHÔNG đụng suốt chuỗi — hash 4 bảng IDENTICAL từng phiên deploy |
| **Kiểm soát định kỳ MỚI** | `web/backend/_v10848_drift_audit.py`: so md5 local↔VPS backend/frontend/tools, flag ⛔CRITICAL, kéo file lệch về artifacts để diff — vào playbook §2.7; chạy sau mỗi đợt deploy lớn/nghi drift/đầu tuần |
| Quy ước | **KHÔNG git-pull trên VPS** (tránh đè bằng trạng thái sai); mọi deploy giữ SFTP-đúng-file + verify |

## 6. GOVERNANCE

- CHANGELOG V10848 (đã sắp đúng thứ tự trên V10847 của phiên thay áo) · SSOT block · FU-V10848-VPS-DRIFT-CONTROL (RESOLVED) · AUTOMATION seq 307 · playbook §2.7 · `UI_V2_LOCAL_PLAN.md` §14.6.
- Files: `_v10848_drift_audit.py` · `_v10848_diff_analysis.py` · `_v10848_page_diffs.py` · `_v10848_live_check.py` · `_v10848_finish_teal.py` + 5 trang inlined + `accuracy.js`.
