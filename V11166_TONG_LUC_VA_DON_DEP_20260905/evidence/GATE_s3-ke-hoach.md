# s3-ke-hoach · tang=PARTIAL

## TOM TAT

GATE 3 — KẾ HOẠCH & CHECKPOINT, đo 05/09/2026, phiên SOI (0 ghi production · 0 deploy · 0 commit).

BẰNG SỐ: Kế hoạch Active `PLAN-20260723-lottery-doc-restructure` **KHÔNG nằm trong repo** — nó là một trang Notion, checkpoint mới nhất trên đó là **V11154 (02/09 21:54)**, tức **trễ 11 bản / 3 ngày** so với repo V11165. Plan Ledger có **19 mã PL**: 7 PASS_LOCKED · 2 DONE · 1 DONE-chờ-ký · 1 BLOCKED · 1 MEASURING quá hạn 17 ngày · 1 XONG-một-phần quá hạn 24 ngày · 5 OPEN · 1 PENDING; chính trang ghi «OPEN ITEMS: PL6, PL11–PL18» = **9 mục còn mở**, tuổi kế hoạch **44 ngày**.

Prompt 43 R1 `PARTIAL` vì Definition of Done (mục 10 của trang prompt, 12 điều kiện): **4 ĐẠT · 2 MỘT PHẦN · 5 CHƯA · 1 chưa áp dụng** = 4/12 = 33,3% (tính nửa điểm cho MỘT PHẦN: 41,7%). Điều kiện lớn nhất còn CHƯA là «context-only atomic, reverse scan 0»: 57/57 payload thật TRƯỢT `CONTAMINATION_GATE_V2`.

Tồn đọng FU: **326 mã** trong sổ · **194 treo** · **152 quá hạn** · 34 không ghi hạn · 1 đến hạn hôm nay · **6 mục mồ côi rơi khỏi mọi bộ đếm**. Ai chặn: **AGENT 90 (80 quá hạn) · THỜI_GIAN 55 (44) · OWNER 49 (28)**.

Sổ quyết định: 75 mục · **72 ACTIVE** · **18 ACTIVE quá hạn ngày rà soát** (lâu nhất 28 ngày) · **8 quyết định cùng đến hạn rà soát NGÀY MAI 06/09**.

BỐN VIỆC NẶNG NHẤT PHÁT HIỆN MỚI (không ai đang nhìn): ① **QD-047 đang `TRÔI`** và bộ kiểm trôi **mù 6 ngày** (lần chạy 04/09 23:25 không đo được) — chính luật của sổ nói «có mục DRIFTED là dừng». ② **FU-449 + FU-450 — toàn bộ mạch Grand Overhaul — mang nhãn MỒ CÔI**, nên con số «152/194» owner đang đọc **KHÔNG bao gồm mạch việc chính**; FU-450 quá hạn 3 ngày mà không xuất hiện ở bất kỳ bộ đếm nào, FU-449 **không có hạn**. ③ Lane **`CAP5_CANDIDATE_PRESERVING` của QD-072: 0/60 region-day hợp lệ** sau 21 ngày (21/21 `CAP5_INPUT_NOT_READY`) — hạn chót số học để còn kịp 30/09 là **10/09**. ④ **5 quyết định đã có người thay mà vẫn `ACTIVE`** (RM-19), cổng `_v11034` vẫn báo `SẠCH` vì nó chỉ soi 2 trục chủ đề.

## VIEC CAN LAM

**P0 — làm trước, không hỏi thêm**

1. **Chạy lại bộ kiểm trôi cho tới khi hết dòng «KHÔNG ĐO ĐƯỢC»** rồi xử QD-047. Ai chặn: **AGENT**. Ở đâu: `web/backend/_v10920_decision_ledger.py` (probe VPS trả thiếu `JSON_START`) + `docs/_LEDGER_TRANG_THAI.json`. Luật của chính sổ: có mục `DRIFTED` là **dừng**, xử trước khi làm việc mới — đã bỏ qua 6 phiên.
2. **Sửa nhãn FU-449 / FU-450 (và 4 mục mồ côi còn lại) về nhãn có trong `TREO_STATUSES`**, và **đặt hạn cho FU-449**. Ai chặn: **AGENT**. Ở đâu: `docs/FOLLOW_UP_TRACKER.md` + `web/backend/_v10958_fu_reader.py::TREO_STATUSES`. Cho tới khi làm, mọi con số «x/194» báo lên owner đều thiếu mạch việc chính.
3. **Hồi sinh briefing đầu phiên** (FU-349, quá hạn 20 ngày). Ai chặn: **AGENT**. Ở đâu: hook `sessionStart` — `docs/_HOOK_DIEM_DANH.log` chứng minh chỉ `CONG_GIT_COMMIT` và `CONG_A55` chạy. Đây là điều kiện tiên quyết của việc 2: cổng mồ côi có bắt đúng nhưng đầu ra duy nhất là briefing.

**P1 — trong tuần**

4. **Quyết trước 10/09: bật đo top-5 cho lane CAP5, hay đóng CAP5 sớm với verdict `INVALID_EXPERIMENT`.** Ai chặn: **OWNER** (QD-072 là quyết định có điều kiện của owner). Ở đâu: `web/backend/_v11137_d30_lane.py` + `/root/Lottery_AI_Test/artifacts/d30/`. Sau 10/09 thì lựa chọn tự mất, 30/09 buộc phải ghi `INVALID_EXPERIMENT`.
5. **Ký hoặc bác câu hỏi D3 đã treo từ 26/08** — đóng protocol D3 với `NO_PROMOTION_INSUFFICIENT_POWER` và mở N2+N3, hay để 23/09 đọc một mốc đã biết là vô ích. Ai chặn: **OWNER**. Ở đâu: `docs/DECISION_PACKET_20260826.md` PACKET 0 · `docs/SO_TUONG_TAC_OWNER.md:144` («Protocol D3 mới: CHƯA KÝ»).
6. **Ký deploy 3 bản vá NHÓM A** (`VA-B` vân tay · `VA-A` `gpt_analyzer.py:6738` · `VA-h12` kế toán MT). Ai chặn: **OWNER**. Ở đâu: `docs/FOLLOW_UP_TRACKER.md` khối FU-449/450 05/09. Cho tới khi vá `VA-A`, **nhánh official không phải đối chứng sạch** — mọi phép so Grand Overhaul chạy trước đó đều mất nghĩa.
7. **Chỉ rõ `UCC` là gì.** Ai chặn: **OWNER**. Ở đâu: `SC-10 INDETERMINATE` — kho không có định nghĩa nào (12 tệp khớp chỉ vì là chuỗi con của `SUCCESS`).
8. **Sửa 5 quyết định vi phạm luật 3 của sổ** (QD-021·022·026·027·065 → `SUPERSEDED` + `thay_boi`), rồi **mở rộng `_v11034` để soi luật lược đồ**, không chỉ 2 trục chủ đề. Ai chặn: **AGENT**. Ở đâu: `docs/OWNER_DECISION_LEDGER.json` + `web/backend/_v11034_kiem_cheo_quyet_dinh.py`.
9. **Giãn 8 quyết định cùng đáo hạn 06/09** hoặc rà gộp trong một buổi. Ai chặn: **OWNER** (giãn hạn là quyết định của owner, tiền lệ QD-021/022/052). Ở đâu: `docs/OWNER_DECISION_LEDGER.json` QD-031→040.
10. **Bù 23 báo cáo thiếu hẳn, ưu tiên V11156.** Ai chặn: **AGENT**. Ở đâu: `E:\Lottery_AI_Notion_Reports`. Nợ đang xấu đi: 38/232 → 40/241 → 40/242.
11. **Hợp nhất cửa sổ thống kê + roster giữa official và shadow TRƯỚC khi chạy replay đầu tiên.** Ai chặn: **AGENT**. Ở đâu: `scheduler.py:4245-4255` (`find_optimal_window` ghi đè 15/30/30) vs `scheduler.py:7356` (60 ngày). Chạy replay khi còn đổi 3 biến cùng lúc là vứt công.

**P2**

12. **Cập nhật trang No

## PHAT HIEN
  [P0][PROVEN_DEFECT] QD-047 đang TRÔI và bộ kiểm trôi đã MÙ 6 NGÀY — luật của chính sổ nói phải DỪNG
  [P0][PROVEN_DEFECT] FU-449 + FU-450 (toàn bộ Grand Overhaul) mang nhãn MỒ CÔI — con số «152/194» owner đang đọc KHÔNG bao gồm mạch việc chính
  [P1][PROVEN_DEFECT] Lane CAP5 của QD-072: 0/60 region-day hợp lệ sau 21 ngày — hạn chót số học để còn kịp 30/09 là 10/09
  [P1][PROVEN_DEFECT] RM-19: NĂM quyết định đã có người thay mà vẫn ACTIVE — cổng _v11034 vẫn báo SẠCH vì chỉ soi 2 trục chủ đề
  [P1][PROVEN_DEFECT] Kế hoạch Active KHÔNG có trong repo — nó nằm trên Notion, đúng nơi CLAUDE.md cấm dùng để tra trạng thái hiện tại
  [P1][PROVEN_DEFECT] Briefing đầu phiên im 20 ngày — mọi cảnh báo mồ côi/quá hạn không tới ai kể từ 16/08
  [P1][OPERATIONAL_IMPROVEMENT] 18 quyết định ACTIVE quá hạn ngày rà soát — và 8 quyết định cùng đáo hạn NGÀY MAI 06/09 (RM-06 tái diễn)
  [P1][PROVEN_DEFECT] Nợ báo cáo §57 đang XẤU ĐI theo số tuyệt đối: 38/232 → 40/241 → 40/242, 23 bản thiếu hẳn
  [P1][SUSPICIOUS_NEEDS_MORE_EVIDENCE] Grand Overhaul: 0/5 Wave đạt ACCEPTED, replay đầu tiên CHƯA CHẠY, và nếu chạy bây giờ thì phép so đang đổi BA biến cùng lúc
  [P1][PROVEN_DEFECT] Mốc 23/09 (D3): verdict đã biết trước là NO_PROMOTION_INSUFFICIENT_POWER, và câu hỏi đóng sớm trình owner từ 26/08 vẫn CHƯA KÝ
  [P2][INDETERMINATE] Sổ theo dõi KHÔNG ghi mức ưu tiên P0..P3 — không thể phân loại 194 mục treo theo yêu cầu của owner
  [P2][EXPECTED_BEHAVIOR] Ba roadmap local đứng yên 32–34 ngày trong khi cổng checkpoint báo 0 quá hạn — xanh vì không có gì chuyển động