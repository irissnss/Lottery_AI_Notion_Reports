# V10848 — "VPS và local khác nhau?" → Audit md5 toàn bộ: LÕI RUNTIME KHỚP 100%; teal 14/14 xong; kiểm soát định kỳ

- **Câu trả lời:** hệ dự đoán/đo lường trên VPS **khớp 100% code fix hiện hành** — md5 MATCH 133 file gồm toàn bộ runtime (main/scheduler/database/gpt_analyzer/model_registry/money_board/V10821/22/29/32/44/AE/freeze/contract). 4 file critical báo lệch (`vn_timezone`, `training_lock`, `_v10773`, `_v10803`) = **chỉ lệch line-ending CRLF/LF, nội dung giống hệt** (diff normalize 0 dòng).
- **"733 file lệch" = ảo giác git trên VPS** (VPS không phải git checkout được update; deploy từ trước tới nay = SFTP đúng-file CÓ verify — đúng như owner nhớ). Lệch thật = script chẩn đoán cũ không chạy runtime + 616 probe local không cần deploy.
- **"5 trang lệch" chẩn đoán lại: LOCAL MỚI HƠN** (reskin + fix model-id `claude-opus-4-6` trong accuracy.js — VPS còn id cổ làm tier opus chết trang accuracy). VPS không có thay đổi riêng nào bị mất → inline + deploy nốt 5 trang + accuracy.js: md5 6/6, serve 200, backup `.bak_pre_v10848` → **TEAL 14/14 HOÀN TẤT**.
- **Đo lường sau thay áo nguyên vẹn (kiểm chứng):** cron 20:50/21:00/21:10 chạy đủ sau reskin — M2s (MB 05✓), rule-cond (MB 05✓ MN 04✓), **V10844 cron đầu tự chạy** (choi=GATE · laneV2 05✓ · laneV3 05✓); journal 0; marker warn-strip/form-line/sectionMbWhatif/FINAL BUNDLE sống. M2s−M0 forward **12/21 vs 10/21 (+9.5pp)** — đọc 28/07.
- **Kiểm soát xấu nhất:** rollback matrix nhiều lớp (tarball pre-teal + `.bak_pre_v10848` + backups_v10844/45 + git + local backups; DB official hash IDENTICAL suốt); tool định kỳ mới `_v10848_drift_audit.py` (playbook §2.7); quy ước KHÔNG git-pull trên VPS.
- user-view viewer-safe CSS live (ẩn KPI — hướng an toàn); B1/B2 backend vẫn chờ owner ký riêng.
- Báo cáo đầy đủ: GitHub `Lottery_AI_Notion_Reports/V10848_DRIFT_AUDIT_TEAL_COMPLETE_20260725/`.

Owner quote: "VPS và local khác nhau ? ... anh không muốn công sức của anh và em đổ sông đổ biển , đo lường code fix quá trời giờ hỏng hệ thống là không được đâu đó nhé."
