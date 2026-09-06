# CONVERSATION CONTEXT — V11156 · 02–03/09/2026 (bản DỰNG LẠI 06/09/2026)

> Giờ **Việt Nam (UTC+07:00)**. `ACTOR_RUNTIME = CLAUDE_CODE`.
>
> ⚠️ Tệp này KHÔNG được viết đồng thời với sự kiện (`V11156` xảy ra đêm 02–03/09/2026, tệp này
> được dựng lại ngày 06/09/2026 bởi `CONG 5` của phiên `V11167`, sau khi cổng
> `_v10921_report_gate.py` phát hiện `V11156` không có báo cáo công khai). Toàn bộ nội dung dưới
> đây lấy từ nguồn thật đã commit — commit riêng `bd0ea86` (+ hai commit phụ trợ `b004f57` ·
> `b9c2878`), `CHANGELOG.md`, `docs/CURRENT_TRUTH_SSOT.md`, `docs/FOLLOW_UP_TRACKER.md`,
> `docs/AUTOMATION_HISTORY.jsonl`, `docs/SO_TUONG_TAC_OWNER.md`. Không có transcript hội thoại
> gốc của đêm đó được lưu lại ở đâu mà agent tìm thấy — mục 1 dưới đây ghi rõ **KHÔNG tái lập
> được** ở đúng những chỗ không có nguồn, thay vì suy đoán lời owner.

---

## 1 · Owner nói gì — NGUYÊN VĂN (những gì tra được)

**Không tìm được dòng nào trong `docs/SO_TUONG_TAC_OWNER.md` có mốc giờ nằm đúng trong cửa sổ
02/09 23:00 → 03/09 00:30** (khung giờ mà `CHANGELOG.md` gán cho `V11156`). Hai dòng gần nhất về
mặt thời gian, đứng NGAY TRƯỚC và SAU cửa sổ đó, là:

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 02/09 ~22:40 (TRƯỚC cửa sổ V11156, dẫn tới V11155) | *«Em tiến hành deploy 1 cách tự động cho anh, với việc backup đầy đủ dự phòng mọi rủi ro ghi mốc lịch sử thời điểm quan trọng này dùm anh. **Tiếp tục xử lý các vấn đề dứt điểm cho anh trong tối nay**, backup và deploy đầy đủ cho anh.»* | `YÊU_CẦU` | uỷ quyền này được dùng làm căn cứ hiệu lực cho việc tiếp tục làm `V11156` ngay sau đó, cùng đêm | `ĐÃ_LÀM` (V11155), tiếp diễn sang V11156 |
| 03/09 ~09:00 (SAU cửa sổ V11156, thuộc phiên kế tiếp) | *«3 càng anh đang xây dựng với số đuôi bạch thủ»* | `HỎI`/`ĐỔI_ƯU_TIÊN` | dẫn tới rút lại kết luận `NO_VALID_3CANG` của chính `V11156` — xem `REPORT_V11156.md` mục 3.1 hộp rút lại | `ĐÃ_LÀM` (ghi tại `FU-450` cập nhật 03/09, KHÔNG phải trong phiên V11156 này) |

**KHÔNG tái lập được:** nguyên văn owner (nếu có) đã kích hoạt cụ thể bốn mục điều tra của
`V11156` (3-càng mục `XI`, `RM-13`, nợ báo cáo, stale reader). Commit `bd0ea86` tự trích dẫn
"mục `XI`" như một mã đã tồn tại từ một prompt khung trước đó (họ với `PROMPT 43 R1`), nhưng
không có bản lưu đầy đủ 12+ mục của prompt đó trong `docs/SO_TUONG_TAC_OWNER.md` ở phạm vi agent
tra được trong phiên `CONG 5` này. Ghi đúng theo `RM-17`: thiếu nguồn thì ghi thiếu, không bịa.

---

## 2 · Agent làm gì (từ nguồn: commit `bd0ea86`, `b004f57`, `b9c2878`)

| việc | kết quả |
|---|---|
| Điều tra 3-càng (`XI`) | `NO_VALID_3CANG` ban đầu; con số hiệu quả sửa `10,16% → 3,87%`; trình 3 phương án A/B/C cho owner — **sau đó bị rút lại** (xem mục 3 dưới) |
| Điều tra `RM-13` (VPS lệch git) | Đóng **có điều kiện** — lỗ hổng 44 ngày thật nhưng ngoài cửa sổ đo; nhân chứng runtime khớp git 98,6% trong cửa sổ tái lập |
| Rà nợ báo cáo | Xác nhận cổng `_v10921_report_gate.py` KHÔNG lỗi; 16/38 bản đóng được bằng đọc lại, 22/38 phải khai `GAP_MARKER` |
| Quét stale reader | 253 bảng → 76 im ≥7 ngày → 31 có điểm đọc sống (không phải 26) |
| Viết `G1` ranked top-K adapter | `web/backend/_v11156_ranked_adapter.py` (333 dòng mới), tự kiểm 13/13, chặn `DOUBLE_COUNT` thật ở lần chạy đầu (`2026-09-02 MB`, `DEGRADED`) |
| Vá `C1` lookahead role-at-time | `_materialize_shadow_promotion_scorecard.py:307-311` (+45/-4), đo trên bản sao DB 799 MB: `8.853 → 12.967` lượt phân loại (+46,5%) |
| Ghi bốn mặt quản trị | `CHANGELOG` +54 dòng · `SSOT` +11 · `FOLLOW_UP_TRACKER` +109 · `AUTOMATION_HISTORY` +1 dòng · `governance_seq` 471→472 |
| **KHÔNG làm** | deploy, restart, sửa dữ liệu production — xác nhận qua `"runtime_thay_doi": false` |

---

## 3 · Vấp trong phiên (đo được từ nguồn, không phải quan sát trực tiếp)

**🔴 (1) Toàn bộ kết luận mục `XI` (3-càng) của chính `V11156` đã bị RÚT LẠI trong vòng chưa đầy
một ngày.** Nguồn: `docs/FOLLOW_UP_TRACKER.md` mục "FU-450 (CẬP NHẬT 03/09 — RÚT LẠI
`NO_VALID_3CANG`)". Owner sửa lại tiền đề (*"3 càng anh đang xây dựng với số đuôi bạch thủ"*) —
tức prefix+BT là **thiết kế có chủ đích**, không phải lỗi generator. Đọc lại `main.py:10587-10640`
cho thấy bộ chọn prefix thực ra đạt hầu hết tiêu chí kỹ thuật đúng (giữ số 0 đầu, không lookahead,
có backtest 118 ngày hậu thuẫn, BT cha lấy sau toàn bộ override, có persist + scorer). Bài học:
bốn lớp kiểm tra nội bộ của `V11156` (đo dữ liệu, đọc code, thống kê, phản biện đối kháng) đều
đồng thuận sai vì không ai hỏi lại owner về Ý ĐỊNH thiết kế trước khi gọi nó là vi phạm.

**🟡 (2) Cả ba tuyến điều tra còn lại đều bị phản biện sửa số trước khi công bố** — không phải
lỗi trong nghĩa "hỏng", mà là bằng chứng cơ chế phản biện đối kháng hoạt động: `RM-13` (ba chỗ
mù bị vạch trần: mù với cột `status`, "93/93" chỉ là một ảnh git lặp lại, và suy luận bắc cầu
sai `VPS==local + local==git ⇏ VPS==git`); nợ báo cáo (đảo ngược kết luận "cổng lỗi" của một
bản điều tra trước thành "cổng đúng, 16 bản thật sự vi phạm"); stale reader (loại hai panel
`cycle-scan`/`cohere` khỏi diện bị đếm oan vì chúng tự in ngày).

**🟡 (3) Phát hiện bởi `CONG 5` khi dựng lại báo cáo này (06/09):** bản thân `V11156` — dù đã
tự phân tích và cảnh báo về 22 bản báo cáo thiếu hẳn ở mục "NO BAO CAO 38/232" của chính nó —
lại **không có `REPORT_V11156.md`/`CONVERSATION_CONTEXT_V11156_*.md` nào được tạo**, và trở
thành một trong những bản thiếu đó chỉ vài ngày sau khi cảnh báo được viết ra. Không có cổng máy
nào chặn tại thời điểm commit; việc bị phát hiện thuần tuý nhờ lần quét định kỳ tiếp theo (`V11167`,
06/09), tức khoảng trống tồn tại công khai suốt ba ngày.

**⚪ (4) Giới hạn của chính việc dựng lại báo cáo này:** không có transcript hội thoại gốc, không
có PID/hash trước-sau (vì không có deploy), không tái lập được nguyên văn owner cho riêng bốn
mục điều tra — tất cả đã ghi rõ "không tái lập được" thay vì suy đoán, theo đúng `RM-17`.

---

## 4 · Trạng thái cuối (tại thời điểm commit `bd0ea86`, 02/09 23:40)

| | |
|---|---|
| `XI` 3-càng | `NO_VALID_3CANG` (bản gốc) → **RÚT LẠI 03/09**, verdict sửa lại `SUBSTANTIALLY_VALID` (xem `REPORT_V11156.md` mục 3.1) |
| `RM-13` | `ĐÓNG_CÓ_ĐIỀU_KIỆN`, phạm vi hẹp = cửa sổ `_v11155` |
| nợ báo cáo | `38/232` tại thời điểm đó; cổng kiểm xác nhận KHÔNG lỗi |
| stale reader | `31/253` bảng có điểm đọc sống dù im ≥7 ngày |
| `G1` | `CODED_AND_TESTED_NOT_RUNTIME_PROVEN`, tự kiểm 13/13 |
| `C1` | `CODED_AND_TESTED_NOT_RUNTIME_PROVEN`, đo trên bản sao DB, chưa chạy DB thật |
| production | **KHÔNG đổi** — `"runtime_thay_doi": false` |
| `governance_seq` | `471 → 472` |
| umbrella | `FU-449`/`FU-450`, không mở FU mới, không mở Prompt 44 |

---

## 5 · Ghi chú cho `CONG 5` / `V11167` (phiên dựng lại 06/09/2026)

Bản này đóng nợ báo cáo của riêng `V11156` trong đợt dọn nợ `V11167`. Không sửa, không xoá bất
kỳ tệp nào khác trong `E:\Lottery_AI_Notion_Reports` — chỉ tạo mới thư mục
`V11156_DONG_BON_MON_NO_20260903/` gồm `REPORT_V11156.md` và tệp này. Cổng
`_v10921_report_gate.py` cần chạy lại sau khi tệp này được thêm để xác nhận số bản "THIẾU BÁO
CÁO" giảm đúng 1 (từ 23 xuống 22), theo đúng yêu cầu mục 4 của nhiệm vụ `CONG 5`.
