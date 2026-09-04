# h12-mt · tang=EVIDENCE_COMPLETE

## TOM TAT

GATE 1 xong: đã dán nhãn RAW_PRE_REVIEW_ARTIFACT · NOT_CANONICAL_IN_ISOLATION cho 8 tệp evidence/GATE_g*.md kèm sha256 hiện tại, và xác nhận nội dung 8 tệp đó KHÔNG bị sửa một byte nào (hash sau đúng bằng hash trước). Lập bảng claim correction 13 mục (11 mục đề bài + 2 mục MỚI tự đào ra), mỗi mục có chỗ gốc, nguyên văn câu sai, điều đúng và phép đo tái lập được. Về «71 ngày liên tiếp»: con số TÁI LẬP ĐƯỢC nhưng CHỈ với định nghĩa evaluation_policy != INCLUDE (2026-06-26→2026-09-04 = 70 EXCLUDE_PRIMARY + 1 EXCLUDE_ALL); chuỗi EXCLUDE_PRIMARY liên tiếp thật chỉ là 7 NGÀY, nên cấm viết «EXCLUDE_PRIMARY 71 ngày liên tiếp». Trong 71 ngày đó 65 mang dấu hiệu cấp 13/15 và 6 KHÔNG phải cấp — riêng 2026-08-28 là hỏng CHẠY thật (0 dòng ai_chain), nên câu «vì một lỗi KẾ TOÁN» không đúng cho cả 71 ngày. Con số «46/72» KHÔNG tái lập được từ artifact đã công bố (dẫn xuất không được ghi ở đâu) — RM-11. Phát hiện MỚI nặng nhất: MB bị loại 74/91 = 81,3%, CAO HƠN MT 80,0%, mà báo cáo chỉ so MT với MN và bỏ hẳn MB — vấn đề không đặc thù MT mà HAI TRONG BA miền đang bị loại ~80% số ngày. Phát hiện MỚI thứ hai: GATE_g4-total-final.md tự khai «gate6 · EVIDENCE_COMPLETE» trong khi REPORT mục 11 ghi «GATE 6 = PARTIAL» — hai câu ngược nhau ngay trên bề mặt lớp bằng chứng. Gate này 0 ghi production, 0 deploy, 0 restart, 0 commit, 0 ghi Notion.

## TRA LOI

**Hai tệp đã tạo (local, CHƯA commit — agent chính commit):**
- `E:\Lottery_AI_Notion_Reports\V11164_EOD_LIVE_CLOSURE_20260904\EVIDENCE_STATUS_V11164.md` — sha256 `5bec0810057422f429c6ab009afa50290a0e0ab9ee12d3f4f7af9d44c678ad20`, 28.966 bytes
- `E:\Lottery_AI_Notion_Reports\V11164_EOD_LIVE_CLOSURE_20260904\EVIDENCE_STATUS_V11164.json` — sha256 `53d0bfee67ccf5151af4e591f9dcdb8ddde51847007b506ca9e9ac67d0c812bc`, 27.238 bytes (JSON hợp lệ, 13 mục claim_correction, 8 tệp raw dán nhãn)

`git status --short` trong `E:\Lottery_AI_Notion_Reports` chỉ có đúng hai dòng `??` cho hai tệp trên — không đụng tệp nào khác.

**1 · Dán nhãn RAW — XONG.** 8 tệp `evidence/GATE_g*.md` mang `RAW_PRE_REVIEW_ARTIFACT · NOT_CANONICAL_IN_ISOLATION`, `SUPERSEDED_BY = REPORT_V11164.md + evidence/PHAN_BIEN_32_SUA_LAI.md`. Đã ghi sha256 hiện tại của từng tệp. **Nội dung KHÔNG bị sửa** — băm lại sau khi viết xong hai deliverable, cả 8 hash trùng khít hash đã ghi.

**2 · Bảng claim correction — 13 mục** (11 mục đề bài + `CC-12` và `CC-13` là hai phát hiện MỚI, chưa có trong V11164 và chưa có trong 32 phản biện). Mỗi mục có chỗ gốc, nguyên văn, điều đúng, phép đo tái lập được.

**3 · Câu hỏi bắt buộc «tự đo lại 71 ngày liên tiếp» — ĐÃ ĐO, và câu trả lời KHÔNG đơn giản:**
- **Bao nhiêu ngày liên tiếp:** **71** — nhưng CHỈ với định nghĩa `evaluation_policy != 'INCLUDE'` (2026-06-26 → 2026-09-04, phá ở 2026-06-25). Nếu đọc theo đúng chữ `EXCLUDE_PRIMARY` thì là **7 NGÀY** (2026-08-29 → 2026-09-04). Vậy headline **tái lập được**, nhưng **bắt buộc kèm định nghĩa**, và **cấm** viết «MT bị `EXCLUDE_PRIMARY` 71 ngày liên tiếp».
- **Bao nhiêu do cấp:** **65/71** mang dấu hiệu `Thiếu 2 model (13/15)`. Trong cửa sổ 90 dòng: **65/72**.
- **Bao nhiêu do nguyên nhân khác:** **6/71** (7/72 trong cửa sổ 90) — liệt kê đủ ngày và lý do ở bảng C3. Riêng **2026-08-28** là **hỏng CHẠY thật** (0 dòng `ai_chain`), nên câu «vì một lỗi KẾ TOÁN» **không đúng cho cả 71 ngày**.
- **«46/72» — NÓI THẲNG: KHÔNG TÁI LẬP ĐƯỢC.** Dẫn xuất không được ghi ở bất kỳ tệp evidence nào (`GATE_g1:49` chỉ nêu kết quả, không kèm truy vấn) ⇒ `RM-11`. Đếm theo dấu hiệu cho 65/72. Tôi thử một định nghĩa chặt hơn nhưng **bộ lọc `run_source` của tôi SAI** (bỏ sót `auto_daily` và `rerun_post_mn`), kết quả 0/65 **vô giá trị** — ghi `INDETERMINATE`, không dùng, và ghi lại lỗi để không ai lặp.

**4 · Ba mâu thuẫn CÒN SỐNG trong chính lớp evidence** (lý do bắt buộc phải dán nhãn thay vì để người đọc tự chọn tệp): `g6:35` vs `g7:22` về `_safe_stdio_ctx`; `g5:5` giữ 88/88·50.670 trong khi REPORT dùng 86/86·50.658; `g4` tự khai «gate6 · EVIDENCE_COMPLETE» trong khi mục 11 ghi «GATE 6 = PARTIAL».

## PHAT HIEN
  - [PROVEN_DEFECT] «71 ngày liên tiếp» chỉ đúng với một định nghĩa; chuỗi EXCLUDE_PRIMARY liên tiếp thật là 7 ngày
  - [PROVEN_DEFECT] Không thể quy cả 71 ngày cho lỗi kế toán — 6/71 ngày là nguyên nhân khác, riêng 28/08 là hỏng chạy thật
  - [INDETERMINATE] Con số «46/72» KHÔNG TÁI LẬP ĐƯỢC từ artifact đã công bố — RM-11
  - [PROVEN_DEFECT] MỚI — MB bị loại khỏi đo lường chính NHIỀU HƠN MT, nhưng báo cáo chỉ so MT với MN và bỏ hẳn MB
  - [OPERATIONAL_IMPROVEMENT] MỚI — tệp evidence tự khai SỐ HIỆU CỔNG lệch, tạo hai câu ngược nhau trên bề mặt lớp bằng chứng
  - [PROVEN_DEFECT] Mâu thuẫn CÒN SỐNG trong lớp evidence: g6 dòng 35 giữ nguyên mệnh đề đã bị rút lại ở RL-010
  - [EXPECTED_BEHAVIOR] Đường rò prompt còn lại đúng MỘT chỗ — tự đo lại trên mã đang serve, và nó chạm NỘI DUNG chứ không chạm CỜ
  - [PROVEN_DEFECT] NULL: STATE_SPACE = 4, hai tệp evidence đếm ở hai mốc khác nhau mà không tệp nào nêu mốc
  - [EXPECTED_BEHAVIOR] «8 cổng» đọc thành «8/8 PASS» — thực là 6 EVIDENCE_COMPLETE + 2 PARTIAL
  - [PROVEN_DEFECT] «Năm tầng» thực là BỐN — tầng 5 (UI) KHÔNG ĐO ĐƯỢC; và «TOTAL trung thực tuyệt đối» nói quá phạm vi
  - [PROVEN_DEFECT] Ba con số prompt đã bị thay và phạm vi stdio đã thu hẹp — raw g5/g7 vẫn giữ bản cũ
  - [EXPECTED_BEHAVIOR] Đếm rút lại 5 + 1 = 6, cả 6 mục đủ bốn phần bắt buộc
  - [EXPECTED_BEHAVIOR] combo-super gọi lại model là EXPECTED_BEHAVIOR; defect thật nằm ở consensus_level đếm voter thô

## DAU VAO LAN SAU

**① Điều kiện CHẶN cho mọi phép so sánh liên-miền (từ CC-09 + CC-12).** Trước khi bất kỳ ai dùng rolling WR/TOP1 làm nền, phải biết **mẫu thật là MN 80/90 · MT 17/90 · MB 17/90**. Vấn đề **không đặc thù MT**: **hai trong ba miền** đang bị loại ~80% số ngày (MB 81,3% còn **cao hơn** MT 80,0%). Điều này **củng cố** `MT_PREREGISTRATION = NOT_READY_FOR_OWNER_LOCK` nhưng **mở rộng lý do** — không phải «thước của MT hỏng» mà «thước liên-miền hỏng ở hai miền». Đây là đầu vào bắt buộc cho bất kỳ câu «model nào tốt hơn» nào của làn sóng 2.

**② Cách nói về MT phải kèm định nghĩa, mọi lần.** Câu dùng được: *«MT không được `INCLUDE` vào đo lường chính 71 ngày liên tiếp (2026-06-26 → 2026-09-04) = 70 `EXCLUDE_PRIMARY` + 1 `EXCLUDE_ALL`; trong đó 65 mang dấu hiệu cấp 13/15 và 6 do nguyên nhân khác»*. Câu **CẤM**: *«MT bị `EXCLUDE_PRIMARY` 71 ngày liên tiếp»* (thật là 7) và *«cả 71 ngày vì lỗi kế toán»* (28/08 là hỏng chạy thật).

**③ NULL: owner đã khoá Option B (QD-073) ⇒ KHÔNG có migration ⇒ cột `output_counterfactual_rank` giữ nguyên `17.121/17.121` NULL, gộp ĐỦ BỐN state.** Mọi tài liệu sau phải viết «bốn state, **chưa** migration» và **không được mượn** cách đếm «ba nghĩa **sau** migration» của `g8` — hai cách đếm đúng ở hai mốc khác nhau, trộn lại là `A60_VIOLATION_LAYER_CONFLATED`.

**④ Đường rò prompt: đúng MỘT chỗ, và nó chạm NỘI DUNG chứ không chạm CỜ.** `gpt_analyzer.py:6738` → `build_context_pack(shadow_mode=)` `:6740` → `prompt += _ctx_pack` `:6755`. `:6680` chỉ nuôi dòng `print` chẩn đoán, **không** phải rò thứ hai. Mọi đề xuất vá phải nói rõ nó sửa **nội dung `ctx_pack`** hay sửa **cờ `context_only`** — hai việc khác nhau. Kèm theo: vân tay `:6723` băm **trước** khi nối ctx_pack và RULEBOOK, nên `contam_hits = 0` **vẫn** không chứng minh prompt cuối sạch dù có vá `:6738`.

**⑤ Khi trích «GATE n» phải nói rõ là TÊN TỆP hay SỐ HIỆU TỰ KHAI — hai hệ đang lệch.** `GATE_g3-model-universe.md` tự khai `gate4`; `GATE_g4-total-final.md` tự khai `gate6`. Mục 11 của REPORT ánh xạ theo tên tệp và **đúng**. Dùng bảng ánh xạ ở mục 2 của `EVIDENCE_STATUS_V11164.md`, **không** sửa tệp raw.

**⑥ Hai việc treo, chưa mở FU (luật cứng của phiên cấm):** (a) ghi dẫn xuất hoặc rút lại con số «46/72»; (b) đo nguyên nhân gốc việc MB rớt một model đều đặn (43 ngày «Thiếu 1 model (14/15)»).

**⑦ Ba mâu thuẫn còn sống trong lớp evidence** — làn sóng 2 nếu trích evidence phải đi qua `EVIDENCE_STATUS_V11164.md` trước: `g6:35` vs `g7:22` (`_safe_stdio_ctx`); `g5:5` giữ 88/88·50.670 đã bị thay bằng 86/86·50.658; `g4` tự khai `EVIDENCE_COMPLETE` dưới nhãn «gate6» mà mục 11 gọi là `PAR

## CHUA TRA LOI

**1 · Dẫn xuất của «46/72» — `INDETERMINATE`.** Không tệp evidence nào của V11164 ghi truy vấn sinh ra con số này. Đếm theo `degradation_reason` cho 65/72. Không thể nói 46 sai, cũng không thể nói đúng — chỉ có thể nói **không tái lập được từ artifact đã công bố** (`RM-11`). Lần sau hoặc ghi rõ dẫn xuất, hoặc rút lại con số.

**2 · «13/15 ⇒ trần V10752» chưa thành nhân quả — `SUSPICIOUS_NEEDS_MORE_EVIDENCE`.** Dấu hiệu `Thiếu 2 model (13/15)` đã xuất hiện **7 lần TRƯỚC 2026-06** (tháng 3: 5 · tháng 4: 1 · tháng 5: 1), tức trước ngày owner duyệt trần 25/06. Quy nguyên nhân theo **hình dạng chuỗi** là đúng thứ `RM-10` cấm. Muốn thành nhân quả phải đối chiếu `gate_diagnostics` (`pass=true` cho đúng hai model bị đẩy ra) từng ngày — phép đo đó tôi **chưa làm** trong gate này.

**3 · Phép thử «định nghĩa chặt» của tôi HỎNG — ghi lại để không ai lặp.** Tôi thử điều kiện «cấp 13/15 **và** ≥15 model chạy thật trong ngày» và ra **0/65**. Kết quả đó **SAI vì bộ lọc của tôi**: tôi chỉ lấy `run_source IN ('ai_chain','free_predict')`, trong khi lượt official của MT thực tế là `ai_chain + auto_daily` (04/09: 9+7 = 16 dòng) hoặc `ai_chain + rerun_post_mn` (01/07: 8+7 = 15 dòng). **Không được dùng con số 0/65.**

**4 · MB bị loại 81,3% — nguyên nhân gốc chưa đo.** Tôi đo được **cái gì** (43× «Thiếu 1 model (14/15)» + 21× 13/15 + 10× 12/15) nhưng **chưa đo được vì sao** MB rớt một model đều đặn như vậy. Đây là việc mới, không mở FU trong gate này theo luật cứng của phiên.

**5 · Ảnh hưởng định lượng của rò `:6738` lên số — `NOT PROVEN` (kế thừa từ V11164, tôi không thu hẹp được).** Đo được prompt khác và `gpt-oss-120b` bỏ phiếu top-1 vào bạch thủ MN (53) và MB (86), nhưng **không** chứng minh được lá phiếu **khác đi vì** prompt khác. Mọi đối chứng đều phải gọi lại model sau khi đã biết kết quả ⇒ vi phạm cấm ORACLE.

**6 · Nội dung `ctx_pack` có chứa dấu ô nhiễm không — `INDETERMINATE`.** Phải gọi `build_context_pack()` trên hàm đang serve; luật cứng của phiên buộc phải chứng minh trư