# s4-no · tang=EVIDENCE_COMPLETE

## TOM TAT

CỔNG 4 (nợ tồn đọng toàn kho) — đếm lại từ đầu, không tin số cũ. Ba con số cũ ĐÚNG NGUYÊN: nợ báo cáo A55 vẫn 40 bản trượt (mẫu số 241→242 vì V11165 mới và ĐẠT), mục quá hạn vẫn khớp từng số 152/194, không bản nào mới trượt cũng không bản nào cũ được vá. Nhưng ba thứ đã XẤU ĐI và một thứ mới đào ra nặng hơn đã báo.

Xấu đi: ba tệp điều hướng nay lệch 15 ngày (không phải 14) — kẹt ở V11098 trong khi thật là V11165, tụt 67 bản và 68 thư mục báo cáo chưa vào chỉ mục; briefing đầu phiên im 20 ngày (không phải 19).

Gốc thật của cả hai, đo được chứ không suy: hai bề mặt hook LỆCH NHAU. `.cursor/hooks.json` khai 5 hook (sessionStart + 3 beforeShell + 1 afterShell) nhưng Claude Code không đọc tệp đó; `.claude/settings.json` chỉ có DUY NHẤT PreToolUse/Bash → `cong_git_commit.py`, mà bên trong lọc `if "git commit" not in lenh: return 0`. Hệ quả: 7 cổng chết hẳn dưới công cụ đang thật sự dùng — trong đó có `_v11143_cong_dong_bo.py` (chính cổng dựng ra để chặn deploy đè mất bản vá trên VPS) và `_v10920_session_start.py`. Lệnh bắt buộc số 1 của CLAUDE.md §0 đã 20 ngày không tự chạy lần nào; sổ điểm danh `docs/_HOOK_DIEM_DANH.log` có dòng `VAO_HOOK` cuối cùng đúng `2026-08-16 23:16:35`. Lệnh deploy / `git push` / cắt cụt tài liệu hiện KHÔNG đi qua cổng nào.

Mới đào ra, nặng hơn đã báo: 85/253 bảng im >7 ngày hoặc rỗng, trong đó 66 bảng VẪN CÓ điểm ĐỌC sống và 27 bảng được đọc bởi chính 6 tệp đang serve (main.py 20 bảng, database.py 2, scheduler.py 1, gpt_analyzer.py 1). Ca FU-391/RM-20 đã biết chỉ là 1 trong 66. Cổng máy cho RM-20 vẫn CHƯA CÓ dù RL-012 (V11164) đã làm RM-20 tái phạm — §61 bắt phải dựng.

Và sổ rút lại vẫn rò: 12 chỗ trích lại kết luận đã rút mà không có dấu rút lại. Nặng nhất là `RL-014` («46/72») còn sống nguyên trong `REPORT_V11164.md:421` của kho CÔNG KHAI đẩy hôm qua — đúng ca `PRJ_RETRACTION_SILENT` mà luật cấm.

## VIEC CAN LAM

P0 — chặn ở AGENT, làm được ngay, không cần owner:
1. Bù `.claude/settings.json` cho đủ bốn nhánh hook mà Cursor đang có: `SessionStart` → briefing; `PreToolUse/Bash` phải xử thêm lệnh deploy/restart (gọi `governance_guard` + `_v11143_cong_dong_bo`) và `git push` (gọi `_v11015_cong_chan_cat_cut`); thêm ba cổng con `_v11044_cong_o_status` · `_v11048_kiem_legacy_treo` · `_v11050_kiem_bien_anchor` vào `cong_git_commit.py`. CHÚ Ý hai bẫy đã ghi sẵn trong docstring `cong_git_commit.py`: thoát 2 mới là CHẶN, và matcher của Claude Code khớp TÊN CÔNG CỤ chứ không khớp chuỗi lệnh. Kèm `--thu-chan` hai chiều cho từng nhánh (RM-15).
2. Rút lại RL-014 ĐÚNG CHỖ GỐC: `V11164_EOD_LIVE_CLOSURE_20260904/REPORT_V11164.md:421` + `evidence/GATE_g1-region-ledger.md:49` (kho CÔNG KHAI) + `docs/FOLLOW_UP_TRACKER.md:154`. Đủ bốn phần theo PRJ-RETRACTION-001. Làm luôn cho RL-002 ở 9 chỗ (trễ 21 ngày).
3. Thêm chế độ `--hoi-to` cho `_v11085_cong_rut_lai.py`: quét toàn kho `.md` chứ không chỉ tệp chưa commit, để mục rút lại thêm SAU không bỏ lọt bản cũ. Vá luôn `_vung()` để nối cửa sổ bằng khoảng trắng (hoặc chuẩn hoá xuống dòng) trước khi dò từ khoá — hiện dương tính giả 1/13 do ngắt dòng.

P0 — chặn ở OWNER:
4. Ký deploy ba vá NHÓM A: `VA-A` (routing gói ngữ cảnh) · `VA-B` (vân tay prompt) · `VA-h12` (kế toán MT). Cả ba đã code+test xong. Chưa có `VA-A` thì nhánh official không phải đối chứng sạch.
5. Quyết ưu tiên cho `consensus_level` gắn nhãn sai ra tới người dùng (`du-doan.html:1413`, 268/567 bundle = 47,3%) — chưa có vá, cần owner xếp trước hay sau ba vá trên.

P1 — chặn ở AGENT:
6. Dựng cổng máy cho RM-20 (bảng chết = bảng không ai ĐỌC). §61 bắt buộc sau khi RL-012 làm RM-20 tái phạm. Dữ liệu nền đã có sẵn ở `/root/Lottery_AI_Test/artifacts/v11166_s4_bang.json` (85 bảng im, 66 có reader).
7. Nối `_v11083_sinh_dieu_huong.py` vào hook (hoặc cron) và chạy ngay một lần để ba tệp điều hướng bắt kịp V11165 / 444 thư mục. Kèm `--thu-chan`.
8. Chuẩn hoá 6 nhãn tự đặt của các mục mồ côi (FU-445 447 448 449 450 · FU-430) về ba loại đã khai trong `_v10958_fu_reader`, hoặc khai thêm loại thứ tư — hiện chúng rơi khỏi mọi bộ đếm, trong đó 2 mục đã quá hạn mà không ai thấy.
9. Thêm `--thu-chan` cho `_v11019` · `_v11020` · `_v11028_cong_dong_bang`. Ưu tiên `_v11028` — nó là ví dụ gốc của RM-15.
10. Đóng nợ A55 gần nhất trước: V11157 (thiếu 7/9 phần + `DOC_SAID`) và V11156 (không có báo cáo).
11. Deploy `_v11033`/FU-303 (cổng tuổi dữ liệu RM-01) — `READY_NOT_DEPLOYED`, hạn 08/08, trễ 28 ngày.
12. Xử `_knowledge_base.json` đóng băng 26/04 vẫn được đọc mỗi lượt và mâu thuẫn với khối sống cùng prompt (`PRJ_PROMPT_CONTRADICTS`); và Phase 19 không có cổng (`weight=` sống sót 933 lần, `A58_VIOLATION_HALF_DONE`).
13. Đồng bộ cửa sổ thống kê hai lane (official 15/30/30 vs shadow 60 ngày) và roster (8 vs 11 model) TRƯỚC khi so CONTEXT_ONLY_V2 với LEGACY — hiện đang đổi ≥3 biến cùng lúc.

P1 — chặn ở OWNER:
14. Chỉ rõ `UCC` là gì (SC-10 INDETERMINATE ⚠️[ĐÍNH CHÍNH · ĐÃ RÚT LẠI RL-019: SC-10 KHÔNG còn INDETERMINATE — `UCC` = UNIFIED CANDIDATE CONTRACT, `UCC-1.0.0`, tệp `_v11150_unified_candidate_contract.py` (01/09) CÓ định nghĩa đầy đủ ở repo local; V11165 quét thiếu phạm vi. Trích ở đây chỉ để giữ nguyên văn bản gốc] — không có định nghĩa nào trong kho).
15.

## PHAT HIEN
  [P0][PROVEN_DEFECT] Hai bề mặt hook lệch nhau — 7 cổng chết dưới Claude Code, deploy hoàn toàn không có cổng
  [P0][PROVEN_DEFECT] Briefing đầu phiên im 20 ngày — lệnh bắt buộc §0 số 1 chưa tự chạy lần nào, số đang phục vụ thấp hơn sự thật 78 mục quá hạn
  [P1][PROVEN_DEFECT] 85 bảng im >7 ngày, 66 bảng VẪN CÓ điểm đọc sống, 27 bảng được đọc bởi chính 6 tệp đang serve — cổng RM-20 vẫn chưa có
  [P1][PROVEN_DEFECT] PRJ_RETRACTION_SILENT — 12 chỗ còn trích lại kết luận ĐÃ RÚT, nặng nhất RL-014 nằm trong báo cáo CÔNG KHAI đẩy hôm qua
  [P1][PROVEN_DEFECT] Ba tệp điều hướng lệch 15 ngày, tụt 67 bản, 68 thư mục báo cáo chưa vào chỉ mục — bộ sinh chưa nối hook nào
  [P1][PROVEN_DEFECT] Nợ báo cáo A55 đứng nguyên 40/242 — không bản nào mới trượt, cũng không bản nào cũ được vá; cổng không nối hook, không cron
  [P1][PROVEN_DEFECT] 152/194 mục quá hạn — khớp từng số với báo cũ; nhưng 6 mục mồ côi mang nhãn TỰ ĐẶT rơi khỏi mọi bộ đếm, kể cả mục của chính phiên trước
  [P1][PROVEN_DEFECT] 3/9 cổng chạy mỗi lần commit KHÔNG có thử chặn — trong đó có đúng cổng mà RM-15 lấy làm ví dụ «từng mù hoàn toàn»
  [P0][PROVEN_DEFECT] Nợ kỹ thuật V11164/V11165 chưa đóng: 15 mục, 4 mục P0 — cả bốn đều đang chặn ở owner hoặc chưa có vá
  [P2][SUSPICIOUS_NEEDS_MORE_EVIDENCE] gpt_analyzer.py:6449 đọc bảng chết 98 ngày, trên đúng nhánh rò ngữ cảnh shadow vào official
  [P3][PROVEN_DEFECT] Cổng _v11085 báo dương tính giả khi từ khoá rút lại bị NGẮT DÒNG — 1/13 ca
  [P2][INDETERMINATE] Không chứng minh được cổng nào «CHƯA BAO GIỜ CHẠY» — chỉ 2/nhiều cổng có sổ điểm danh