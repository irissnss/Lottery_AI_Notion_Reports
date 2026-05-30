# V106.38-R8G — DEPLOY 5 VIEW CANONICAL LÊN VPS (PUBLIC-SAFE)

> Public-safe. Không token/key/IP/path nhạy cảm. Read overlay deploy; 0 đổi số official.
> Auditor: Opus 4.7 | 2026-05-30 | Chain R8→R8G.

## 1. DEPLOY THÀNH CÔNG (production, an toàn)
- **Backup DB trước** (sqlite online backup, ~330MB) → có điểm khôi phục.
- Tạo 5 VIEW canonical trên VPS: v_predictions, v_final_bundles, v_model_daily_eval, v_mined_rules, v_lottery_results.
- **Official UNCHANGED**: 4 bảng (predictions/final_bundles/lottery_results/model_daily_eval) count before==after.
- Tổng 13 view (8 cũ + 5 mới, khác tên, không đụng nhau).
- Smoke `/api/health` = 200, service active (V20.3.36).
→ Standardization (tên cột canonical) giờ LIVE trên production; reversible (DROP VIEW).

## 2. PHÁT HIỆN QUAN TRỌNG (khi chẩn đoán VPS)
- **Local ↔ VPS LỆCH NHAU**: VPS branch `master` HEAD khác + 164 bảng + uncommitted; local `main` 163 bảng. → KHÔNG deploy code mù (sẽ đè production). Deploy code phải qua git-based có kiểm soát, reconcile divergence trước.
- **Bảo mật**: GitHub PAT bị nhúng plaintext trong git remote của VPS → owner nên ROTATE token (redact trong báo cáo).

## 3. CHƯA DEPLOY (cần kiểm soát, KHÔNG làm mù)
- Phase B drop/merge (destructive) · MB freq lane runtime + cron · per-slice weighting (đổi scoring) · cap MB · token LIMIT.
- Lý do: đụng code/behavior trên cây code đang lệch → cần git-based deploy có review + backup, không tự động.

## 4. AN TOÀN
- Chỉ deploy VIEW overlay (0 đổi số official); backup trước; verify count; smoke 200.
- Wallet không đụng; lane không promote; provider/AI không gọi.

## 5. CÒN LẠI
- Owner-gate: code deploy (git reconcile) cho runtime mới · Phase B · scoring/cap/token (supervised).
- Data-bound: 2026-06-03 forward proof.
- Roadmap: docs/ACTIVE_ROADMAP_STANDARDIZATION_ACCURACY.md.
