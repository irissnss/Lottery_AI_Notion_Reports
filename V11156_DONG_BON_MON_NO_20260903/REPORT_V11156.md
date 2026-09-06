# REPORT V11156 — ĐÓNG BỐN MÓN NỢ: `NO_VALID_3CANG` · RM-13 · nợ báo cáo 38/232 · 31 stale reader

> `ACTOR_RUNTIME = CLAUDE_CODE` · `TRẠNG THÁI = CODE_PUSHED` cho hai bản vá đi kèm
> (`G1` ranked top-K adapter, `C1` role-at-time) — **`CODED_AND_TESTED_NOT_RUNTIME_PROVEN`**,
> nguyên văn từ chính commit `b9c2878`. **Không có deploy, không restart** trong phiên này
> (`AUTOMATION_HISTORY.jsonl` ghi `"runtime_thay_doi": false` cho `V11156`).
>
> ⚠️ **BẢN NÀY LÀ BẢN DỰNG LẠI (RECONSTRUCTED), không phải bản viết đồng thời với sự kiện.**
> `V11156` đã bị commit và ghi đủ bốn mặt quản trị (`CHANGELOG` · `SSOT` · `FOLLOW_UP_TRACKER` ·
> `AUTOMATION_HISTORY`) ngày 02–03/09/2026, nhưng **không có `REPORT_*.md`/`CONVERSATION_CONTEXT_*.md`
> công khai nào được tạo** — đúng vi phạm `A55_VIOLATION_REPORT_MISSING` mà cổng
> `_v10921_report_gate.py` phát hiện ngày 06/09/2026 (`V11167`, `CONG 5`). Bản này dựng lại
> **từ nguồn thật, không bịa** (`RM-17`): commit riêng `bd0ea862574b1b6ec404d6aaf4cade8003587bca`
> (và hai commit phụ trợ cùng đêm `b004f57` · `b9c2878`), mục `CHANGELOG.md` — `## V11156`,
> mục `docs/CURRENT_TRUTH_SSOT.md` — `### V11156`, mục `docs/FOLLOW_UP_TRACKER.md` (FU-449/450),
> và dòng `docs/AUTOMATION_HISTORY.jsonl` phiên bản `V11156`. Chỗ nào nguồn không đủ để tái lập
> thì ghi rõ **"không tái lập được vì …"** thay vì suy đoán.
>
> 🔴 **MỤC `XI` (3-càng) TRONG BẢN GỐC ĐÃ BỊ RÚT LẠI NGAY SAU ĐÓ** — xem hộp rút lại ở mục 3.1
> dưới đây và `docs/FOLLOW_UP_TRACKER.md` mục **FU-450 CẬP NHẬT 03/09** (`PRJ-RETRACTION-001`).
> Bản dựng lại này **giữ nguyên câu gốc** (để đúng lịch sử) **và** dán ngay bên cạnh **điều đã
> sửa**, để không lặp lại lỗi `PRJ_RETRACTION_SILENT` mà `V11167` vừa đo được (12 chỗ tài liệu
> vẫn khẳng định một mệnh đề đã rút lại).

---

## 1 · TÓM TẮT

Đêm 02→03/09/2026, agent chạy **bốn tuyến điều tra song song** theo `FU-449`/`FU-450`
(umbrella Grand Overhaul, không mở FU mới), mỗi tuyến có một **agent phản biện đối kháng** riêng.
**Cả bốn tuyến đều bị phản biện bác ở ít nhất một điểm**, và mỗi lần bác đều sửa một con số sắp
công bố: (1) 3-càng — kết luận ban đầu `NO_VALID_3CANG`, con số hiệu quả sửa từ `10,16%` xuống
`3,87%`; (2) `RM-13` VPS-lệch-git — đóng **có điều kiện**, phạm vi hẹp lại còn đúng cửa sổ đo
`_v11155`; (3) nợ báo cáo — xác định lại là **38/232**, và **cổng kiểm không có lỗi** (bản điều
tra trước đó gọi nhầm là lỗi cổng); (4) bảng dữ liệu im lặng (stale reader) — con số đúng là
**31**, không phải 26. Song song, hai bản vá code khác cùng đêm được đưa vào commit: `G1`
(`_v11156_ranked_adapter.py`, adapter chuẩn hoá UCC-1.0.0, tự kiểm 13/13, chặn được `DOUBLE_COUNT`
ngay ở lần chạy thật đầu tiên) và `C1` (vá lookahead trong
`_materialize_shadow_promotion_scorecard.py`, đo trên **bản sao DB 799 MB** — không đụng DB thật
— cho thấy lượt được phân loại tăng từ 8.853 → 12.967, tức `+46,5%`). **Không đụng production,
không deploy, không restart** trong phiên này; cả hai bản vá ở trạng thái
`CODED_AND_TESTED_NOT_RUNTIME_PROVEN`. `governance_seq` tăng lên **472**.

---

## 2 · OWNER YÊU CẦU GÌ — nguyên văn

> Không tìm được dòng nào trong `docs/SO_TUONG_TAC_OWNER.md` mang mốc giờ nằm **đúng trong**
> cửa sổ 02/09 23:00 → 03/09 00:30 (giờ mà `CHANGELOG` gán cho `V11156`). Ghi đúng những gì tra
> được, không suy diễn thêm lời owner không có nguồn.

Việc đêm 02–03/09 là phần tiếp theo của cùng **một** phiên uỷ quyền đã mở trước đó cùng buổi tối
(dẫn tới `V11155`, deploy 22:46), dưới cùng umbrella `FU-449`/`FU-450`, **không mở FU mới, không
mở Prompt 44** (commit `bd0ea86` ghi rõ dòng này):

| giờ (VN) | NGUYÊN VĂN (nguồn: `docs/SO_TUONG_TAC_OWNER.md`, mục "Phiên 31/08 – 01/09..." / `REPORT_V11155.md` mục 2) | loại | liên quan đến V11156 thế nào |
|---|---|---|---|
| 02/09 ~20:20 | `PROMPT 43 R1 · CONTINUATION AFTER V11154` — 12 mục `A`–`L` | `YÊU_CẦU` | prompt khung đang thi hành; `V11156` là phần việc tiếp sau các mục đã đóng ở `V11155` |
| 02/09 ~22:40 | *«Em tiến hành deploy 1 cách tự động cho anh, với việc backup đầy đủ dự phòng mọi rủi ro ghi mốc lịch sử thời điểm quan trọng này dùm anh. **Tiếp tục xử lý các vấn đề dứt điểm cho anh trong tối nay**, backup và deploy đầy đủ cho anh.»* | `YÊU_CẦU` | câu "tiếp tục xử lý các vấn đề dứt điểm cho anh trong tối nay" là uỷ quyền đang có hiệu lực khi `V11156` chạy tiếp ngay sau `V11155` cùng đêm |

**Không tái lập được:** owner có nói thêm câu nào mới, cụ thể cho bốn món nợ này (3-càng /
`RM-13` / nợ báo cáo / stale reader), giữa 23:00 và 00:30 hay không — sổ tương tác không có dòng
nào ghi giờ đó. Việc bốn món nợ này nằm trong phạm vi các mục La-mã `XI` và các dòng `RM-13`,
"nợ báo cáo", "stale reader" của một prompt khung dài hơn (cùng họ với `PROMPT 43 R1`) là suy ra
từ chính văn bản commit `bd0ea86` tự trích dẫn mã mục ("đúng thứ owner cấm ở mục `XI`"), không
phải từ một dòng owner mới được xác nhận trong sổ tương tác.

---

## 3 · ĐÀO BỚI / PHÁT HIỆN

Nguồn cho toàn bộ mục này: commit `bd0ea86` (điệp khúc cả 4 tuyến) + đối chiếu
`docs/FOLLOW_UP_TRACKER.md` bản đầy đủ hiện tại (đã có cập nhật 03/09 rút lại một phần).

### 3.1 🔴 `XI` — 3-càng: `NO_VALID_3CANG` cho tiêu chí generator (bản gốc) — **ĐÃ RÚT LẠI SAU ĐÓ**

**Câu công bố nguyên văn lúc đó** (từ `CHANGELOG.md` mục `V11156`):

> *«`561/561 = 100,00%` — mọi `lo3` kết thúc bằng đúng `bach_thu`, không một ngoại lệ.
> ⚠️ **Cố ý trích MỘT cửa sổ** (`PRJ-SELECTION-WINDOW-001` · RM-18 · RM-21). Con số ngay dưới là
> **số ĐÃ CÔNG BỐ tại thời điểm bản này ra**, giữ nguyên văn để truy vết — **không** phải một
> tuyên bố hiệu quả mới. Bộ đủ **14 / 30 / 90 / 180 ngày** nằm ở **V11084 + V11086**, và ở đó
> **dấu ĐỔI**: 30 ngày **+4,07pp** · 90 ngày **−3,18pp** · 180 ngày **+0,91pp** (CI95 [−3,2 ; +5,0]).
> Đo lại toàn cục ở **V11166**: 479 bundle LIVE, bạch thủ **31,7%** vs ngẫu nhiên **34,0%**.
> `_generate_lo3_frequency()` (`main.py:10587`) lấy nguyên bạch thủ làm đuôi rồi chỉ chọn một
> chữ số đầu ⇒ đúng thứ owner cấm ở mục `XI`.»*

Kèm: không có bảng/cột nào tên `3cang`; 3-càng nằm ở `final_bundles.lo3` + `lo3_status`. Con số
hiệu quả sửa lại lúc đó: cột `lo3_status` cho `57/561 = 10,16%` nhưng dải trước 04/2026 nhiễm lỗi
chấm tiền-`V16.1`; tính từ 01/04 trở đi ra `18/465 = 3,87%` (agent phản biện chấm độc lập ra
`25/558 = 4,48%` — khác phương pháp, cùng bậc, cả hai đều xa `10,2%`). Phát hiện phụ: bảng
`ai_region_specialist_provider_shadow_results` có 219 dòng (06/05→30/05) cho thấy LLM từng sinh
thẳng số 3 chữ số, `148/216` không khớp đuôi `bt` của chính model.

**Vì đây là quyết định sản phẩm, bản gốc KHÔNG tự quyết** — trình owner ba lựa chọn: (A) dừng
hiện 3-càng tới khi có generator thật · (B) giữ nhưng dán nhãn rõ "suy từ BT, không phải dự đoán
3 chữ số độc lập" · (C) dựng direct three-digit generator.

> ### 🔴 HỘP RÚT LẠI — `PRJ-RETRACTION-001`, đủ bốn phần (nguồn: `docs/FOLLOW_UP_TRACKER.md`,
> mục **FU-450 CẬP NHẬT 03/09 — RÚT LẠI `NO_VALID_3CANG`**, ghi cùng ngày 03/09/2026)
>
> | phần | nội dung |
> |---|---|
> | **chỗ gốc** | chính mục `XI` ở trên trong `REPORT_V11156` (bản dựng lại này) + `CHANGELOG V11156` + `SSOT V11156`, công bố lần đầu 03/09/2026 |
> | **câu sai** | *«`NO_VALID_3CANG` cho tiêu chí generator… `_generate_lo3_frequency()` lấy nguyên bạch thủ làm đuôi rồi chỉ chọn một chữ số đầu ⇒ đúng thứ owner cấm ở mục `XI`»* |
> | **điều đúng, đo tái lập được** | Owner correction 03/09 ~09:00: *«3 càng anh đang xây dựng với số đuôi bạch thủ»* — **prefix + BT CHÍNH LÀ thiết kế**, không phải vi phạm. Đọc lại `main.py:10587-10640`: giữ số 0 đầu (`zfill(2)[-2:]`) · không lookahead (`WHERE date >= cutoff AND date < date_str`) · chọn prefix bằng đếm substring 180 ngày có căn cứ backtest 118 ngày (`V10753.1`) · BT cha lấy **sau** toàn bộ chuỗi override · có persist + scorer exact-3-chữ-số + trạng thái `PENDING` không tự thua. Verdict sửa lại: `3CANG_PIPELINE = SUBSTANTIALLY_VALID` cho đúng thiết kế owner, **thiếu tầng ghi vết/lineage** (`ranked_prefixes`, `prefix_method_version`, `parent_bt_source`, `cutoff_at`, provenance hash) |
> | **quyết định đã dựa trên số sai** | ba lựa chọn A/B/C trình owner ở trên ("dừng hiện 3-càng" / "dán nhãn" / "dựng generator thật") — **cả ba đã bị huỷ** vì tiền đề sai; việc còn lại không phải viết generator mới mà là thêm tầng ghi vết quanh bộ chọn đang chạy đúng |
>
> Bản dựng lại này giữ câu gốc ở trên (đúng những gì đã được công bố) đúng theo yêu cầu tái lập
> lịch sử của `CONG 5`/`V11167`, và đặt hộp rút lại ngay tại đây để không tạo thêm một bản sao
> chép câu đã sai mà không cảnh báo.

### 3.2 🟢 `RM-13` — VPS lệch git: đóng **có điều kiện**

Có thật lỗ hổng 44 ngày (16/04→30/05) VPS lệch git — `CHANGELOG.md:20147` ghi "model_registry
+163", `git diff --stat` xác nhận 164 thêm/23 xoá — nhưng nằm **hoàn toàn ngoài** cả hai cửa sổ
đo (tái lập 60 ngày `04/07→02/09`; counterfactual 30 ngày `03/08→02/09`). Nhân chứng runtime
không phụ thuộc git: `output_eligible_completion_daily` do `main.py:1885-1918` ghi trên VPS ⇒
`365/370 = 98,6%` khớp git; trong cửa sổ tái lập chỉ `2/180` lệch, cả hai rơi đúng 01/08, gốc là
độ phân giải NGÀY của `--until <ngày> 23:59:59` (registry commit 4 lần hôm đó), không phải drift.

**Phản biện bác đúng ba chỗ:** (1) nhân chứng chỉ kiểm tập `output_eligible`, trong khi drift nằm ở
`status` — và `status` chính là một điều kiện lọc trong `get_output_eligible_ids` ⇒ mù đúng loại
lệch đang hỏi. (2) "93/93 khớp" là **một** ảnh git lặp 93 lần, một bậc tự do, không phải 93 phép
thử độc lập. (3) `VPS==local(28/07)` + `local==git(02/09)` **không** suy ra `VPS==git(28/07)`.

⇒ Nhãn đúng: **`ĐÓNG_CÓ_ĐIỀU_KIỆN`**, phạm vi "đầu vào `output_eligible` của `_v11155` trong
cửa sổ 60 ngày", **không phải** "VPS == git" nói chung. Việc còn treo (cần owner ký — `§52`
mục 13 cấm đụng writer của `final_bundles` khi đang đo): ghi `registry_sha256` vào
`source_predictions_json` của mỗi bundle để câu "ai output-eligible lúc chốt bundle này" trả
lời được từng byte về sau.

### 3.3 🟡 Nợ báo cáo — **38/232**, và cổng KHÔNG lỗi

Một bản điều tra trước đó (không phải bản này) gọi `_v10921_report_gate.py:467` là "lỗi của
cổng" vì nó chỉ dò 9 tiêu đề trên dòng bắt đầu bằng `#`. Phản biện bác: **sai** — `§57.3` viết
rõ "cổng kiểm dò theo tiêu đề" và "không được xoá tiêu đề". Cổng làm đúng hợp đồng; 16 bản
trong số 38 **thật sự vi phạm khung** (thiếu tiêu đề/nội dung thật) và đóng được bằng cách đọc
từng bản rồi đặt nội dung sẵn có dưới đúng tiêu đề (không bịa); 22 bản còn lại **thiếu hẳn báo
cáo**, không đóng được bằng cách viết bù — phải khai `GAP_MARKER`. Cấm lặp lại phép gán tiêu đề
tự động bằng đếm từ khoá (đã cho kết quả vô nghĩa một lần, gán nhầm "thiếu gỡ về" cho mục
`## 14 DECISION PACKET`).

**Đối chiếu với `V11167` (06/09):** con số nợ báo cáo đã đo lại hoàn toàn khác — **40/243** — vì
phạm vi đo đã mở rộng (từ mốc thi hành `V10921`, hợp ba nguồn `CHANGELOG ∪ git log ∪ thư mục báo
cáo`). Hai con số **không mâu thuẫn nhau**: chúng đo trên hai phạm vi khác nhau tại hai thời điểm
khác nhau; xem mục 6 của báo cáo này để có bằng chứng chạy lại ngay hôm nay.

### 3.4 🟡 Stale reader: **31**, không phải 26

Quét 253 bảng: 76 bảng im ≥7 ngày, và 31 trong số đó **có điểm đọc sống** (`RM-20`: đếm điểm
đọc, không đếm writer). Phân bố: 8 trên `/monitoring` · 11 trên `/du-doan-test` · 6 chỉ qua API ·
6 chỉ mã nội bộ. `verified_bucket_rules` im 170 ngày (không phải 169 như một bản đếm trước đó).
Đối chiếu ngược để không kể oan: panel `cycle-scan` và `cohere` tự in ngày lên màn hình ⇒ dù im
59 và 55 ngày, **không** thuộc diện "trả số cũ mà không báo". Cảnh báo đi kèm: số dòng tham chiếu
`RM-20` trong `CLAUDE.md` đã trôi ~360 dòng tại thời điểm đó (từ `:11881 :11918 :14923 :14935`
sang `:12244 :12281 :15390 :15402`) — mọi báo cáo phải dẫn số dòng đo lại, cấm chép từ báo cáo cũ.

### 3.5 🟢 `G1` — ranked top-K adapter, chặn được `DOUBLE_COUNT` ngay lần chạy đầu

File mới `web/backend/_v11156_ranked_adapter.py` (333 dòng, commit `b004f57`). Tự kiểm 13/13.
Chạy thật `2026-09-02 MB`: dựng được 7 bộ, `validate_batch ⇒ DEGRADED` (hợp lệ 4 · hỏng 3) —
`smart-ensemble` · `smart-ml` · `combo-no-token` bị chặn vì `parent_source_ids` rỗng. Đúng ba
nguồn nghi vấn ở mục `VIII` trước đó, nay bị chặn tại biên hợp đồng thay vì lọt vào Arena như
voter độc lập. Bộ tự kiểm bắt được một lỗi thiết kế của chính adapter: bản đầu tự điền
`["UNKNOWN_LEGACY"]` cho hybrid thiếu lineage — chuỗi không rỗng nên validator cho qua, tức
**adapter tự vô hiệu hoá chính cổng nó đang dựng**. Sửa: đường ghi mới để trống thật và để
validator chặn; `UNKNOWN_LEGACY` chỉ còn hợp lệ ở đường đọc artifact cũ.

### 3.6 🟢 `C1` — vá lookahead trong role-at-time, áp vào materializer nhưng CHƯA chạy trên DB thật

File sửa: `web/backend/_materialize_shadow_promotion_scorecard.py` (dòng 307-311, +45/-4, commit
`b9c2878`). Lỗi cũ: đối chiếu model với `shadow_models`/`output_models` lấy từ **registry hiện
tại** — một lượt tháng 6 của `glm-5.1` bị tính `MISSING_SHADOW_ROW` chỉ vì hôm nay `glm-5.1`
không còn trong danh sách đó (lookahead: lấy danh sách hôm nay áp cho sự kiện hôm qua). Bản vá
suy vai trò từ chính sự kiện (`run_source`), có ba lớp an toàn (ném lỗi khi `run_source` rỗng ·
fail-closed khi thiếu module vai-trò-tại-thời-điểm · loại `manual` khỏi bảng chấm). Đo trên
**bản sao DB 799 MB, không đụng DB thật**, 180 ngày: số lượt được phân loại tăng từ **8.853 lên
12.967 (+4.114 = +46,5%)** — cứu 4.132 lượt bị bỏ im lặng, loại đúng 18 lượt `manual` đếm nhầm
thành official. Hồi quy: `_v11155_test_vai_tro` 19/19 · `_v11150_test_contract` 37/37 ·
`ranked adapter` 13/13.

**Trạng thái ghi đúng, nguyên văn từ commit `b9c2878`:** "`CODED_AND_TESTED_NOT_RUNTIME_PROVEN`
— đã sửa mã production nhưng CHƯA deploy. Deploy sẽ làm cùng đợt với các thay đổi còn lại, sau
khi có runtime proof của đợt trước."

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

Bốn món nợ có bốn cách xử lý khác nhau, không gộp chung một khuôn:

- **3-càng (`XI`):** vì đây là **quyết định sản phẩm** (giữ/bỏ một tính năng người dùng đang
  thấy mỗi ngày), agent **không tự quyết** — trình ba phương án A/B/C cho owner chọn, kèm số đo
  đã sửa. (Owner sau đó, 03/09 ~09:00, sửa cả tiền đề — xem hộp rút lại mục 3.1 — nên cả ba
  phương án này đã bị huỷ; đó là diễn biến của phiên **sau**, không phải của phiên này.)
- **`RM-13`:** đóng có điều kiện thay vì đóng dứt điểm, vì phạm vi đo chỉ phủ đúng cửa sổ
  `_v11155` — mở rộng thành "VPS luôn khớp git" sẽ là kết luận vượt quá bằng chứng (`RM-03`).
  Việc ghi `registry_sha256` vào bundle bị hoãn vì đụng đúng writer của `final_bundles` đang
  trong lúc `§52` mục 13 cấm sửa khi đang đo — cần owner ký trước.
- **Nợ báo cáo:** giữ nguyên phán quyết "cổng không lỗi" của phản biện, và **chia hai nhóm xử lý
  khác nhau** — 16 bản đọc-lại-được (đóng ngay) và 22 bản thiếu hẳn (khai `GAP_MARKER`, không cố
  viết bù) — đúng tinh thần `RM-17` (cấm bịa dữ liệu để làm đầy báo cáo), chính là quy tắc `CONG
  5`/`V11167` đang áp dụng lại hôm nay cho 23 bản thiếu của phạm vi mới.
- **`G1`/`C1`:** cả hai code xong, tự kiểm đạt, nhưng **không deploy cùng đêm** — chờ gộp đợt với
  runtime proof của lượt trước, đúng nguyên tắc "không vá một chỗ rồi vá tiếp ngay khi còn số đo
  đang treo" (tránh chồng biến số khi đang tìm nguyên nhân, họ với `RM-03`).

---

## 5 · ĐÃ LÀM GÌ

| # | việc | file | trạng thái |
|---|---|---|---|
| 1 | Điều tra 3-càng, xác định `NO_VALID_3CANG` + sửa số hiệu quả `10,16% → 3,87%` | không sửa code — chỉ đo | tài liệu (đã rút lại sau, xem 3.1) |
| 2 | Điều tra `RM-13`, đóng có điều kiện | không sửa code | tài liệu |
| 3 | Rà nợ báo cáo, xác nhận cổng đúng, phân loại 16 đóng được / 22 `GAP_MARKER` | không sửa code | tài liệu |
| 4 | Quét 253 bảng tìm stale reader, ra số 31 | không sửa code | tài liệu |
| 5 | Viết adapter chuẩn hoá UCC-1.0.0, chặn `DOUBLE_COUNT` | `web/backend/_v11156_ranked_adapter.py` (mới, 333 dòng) | `CODED_AND_TESTED_NOT_RUNTIME_PROVEN` |
| 6 | Vá lookahead role-at-time trong materializer | `web/backend/_materialize_shadow_promotion_scorecard.py:307-311` (+45/-4) | `CODED_AND_TESTED_NOT_RUNTIME_PROVEN` — đo trên bản sao DB 799 MB |
| 7 | Ghi bốn mặt quản trị | `CHANGELOG.md` (+54) · `docs/CURRENT_TRUTH_SSOT.md` (+11) · `docs/FOLLOW_UP_TRACKER.md` (+109) · `docs/AUTOMATION_HISTORY.jsonl` (+1 dòng) · `docs/AUTOMATION_STATE.json` (`governance_seq` 471→472) | ✅ commit `bd0ea86` |

**Backup trước khi sửa:** **không tái lập được** — không tìm thấy dòng ghi backup riêng cho hai
tệp `_v11156_ranked_adapter.py` (tệp mới, không có "trước" để backup) và
`_materialize_shadow_promotion_scorecard.py` trong commit message hay trong
`docs/AUTOMATION_HISTORY.jsonl` của đêm đó. Không có deploy VPS, không restart, không PID
trước/sau — đúng với `"runtime_thay_doi": false`.

**Hash 4 bảng khoá trước/sau:** **không tái lập được** — phiên này không đụng runtime nên không
có số đo hash trong nguồn; chuỗi hoàn tất chuẩn (`§0` bước 6) chỉ bắt buộc khi có thay đổi
runtime.

---

## 6 · CỔNG KIỂM

**RM-01 (tuổi dữ liệu):** đạt — "đã đồng bộ lại (manifest `20260902_233615`) TRƯỚC khi chốt mọi
con số; bản trước đó lúc manifest 12,1 giờ tuổi, vượt ngưỡng 6 giờ" (nguyên văn commit `bd0ea86`).

**Hồi quy code (`C1`):** `_v11155_test_vai_tro` 19/19 · `_v11150_test_contract` 37/37 ·
`ranked adapter` tự kiểm 13/13 — cả ba nguồn trực tiếp từ commit message, không tái lập chạy lại
được trong phiên `CONG 5` này vì đây là cổng kiểm gắn với script không thuộc phạm vi sở hữu của
`CONG 5` (chỉ sở hữu thư mục báo cáo mới).

**Cổng báo cáo công khai — chạy lại hôm nay (06/09/2026), làm bằng chứng cho chính việc dựng lại
báo cáo này:**

```
$ python web/backend/_v10921_report_gate.py
...
✗ 40/243 phiên bản thiếu/không đạt
   phạm vi đã soi: TOÀN BỘ 243 bản từ mốc thi hành V10921 (CHANGELOG 443 ∪ git 584 ∪ báo cáo 356)
   THIẾU BÁO CÁO (23): V11156 · V11037C · V11087B · V11044B · V11037B · V11033B · V11032B ·
   V11029 · V11027 · V11026 · V11021B · V11021 · V11019 · V11015B · V11001 · V10997 · V10992 ·
   V10991B · V10940 · V10939 · V10933B · V10922 · V11039B
→ A55_VIOLATION_REPORT_MISSING / A55_VIOLATION_REPORT_INCOMPLETE · mã thoát 1
```

Sau khi thư mục này được tạo, cổng cần chạy lại lần nữa (mục 4 của phiên `CONG 5`) để xác nhận
`V11156` rời khỏi danh sách 23 bản "THIẾU BÁO CÁO" — số cụ thể nằm trong phần theo dõi của
`CONG 5`, không lặp lại ở đây để tránh hai bản báo cùng một con số theo hai cách khác nhau
(`RM-11`).

---

## 7 · VƯỚNG VẤP

**(1) Cả bốn tuyến điều tra đều bị phản biện bác ít nhất một điểm** — đây không phải một sự cố,
mà là bằng chứng cơ chế "agent phản biện đối kháng" đang hoạt động đúng chức năng: mỗi lần bác
đều **sửa một con số sắp công bố** trước khi nó ra ngoài, không phải sau. Cụ thể: 3-càng
(`10,16% → 3,87%`), `RM-13` (ba chỗ mù bị vạch trần), nợ báo cáo (đảo ngược kết luận "cổng lỗi"
thành "cổng đúng"), stale reader (loại hai panel bị đếm oan).

**(2) Chính mục `XI` (3-càng) — kết luận công bố trong `V11156` lại bị RÚT LẠI ngay hôm sau** khi
owner sửa tiền đề (03/09 ~09:00: "prefix + BT chính là thiết kế"). Đây là vướng vấp **nặng nhất**
của cả cụm: bốn lớp kiểm tra nội bộ (đo dữ liệu 561/561, đọc code, phân tích thống kê, phản biện
đối kháng) đều đồng thuận vào một kết luận sai vì **không ai hỏi lại owner xem thiết kế dự định
là gì** trước khi gọi nó là vi phạm — bài học trực tiếp cho `§56` (tra cứu trước khi hỏi áp dụng
cả chiều ngược: đôi khi phải HỎI trước khi kết luận, không chỉ tra tài liệu).

**(3) (Do `CONG 5` phát hiện khi dựng lại báo cáo này, 06/09):** `V11156` **không hề có
`REPORT_*.md`/`CONVERSATION_CONTEXT_*.md`** dù bốn mặt quản trị khác đều đầy đủ và đã commit —
đúng khoảng trống mà chính `V11156` (`3.3`) từng nói "22 bản thiếu hẳn không đóng được bằng
viết bù" rồi vô tình trở thành một trong 22 bản đó khoảng ba ngày sau khi được viết ra. Đây là
bằng chứng cho thấy nợ này **tiếp tục sinh ra** ngay cả sau khi được đo và cảnh báo — cần cổng
máy chặn tại thời điểm commit, không chỉ đo định kỳ.

---

## 8 · GỠ VỀ

**Không áp dụng cho hai bản vá `G1`/`C1`** — cả hai ở trạng thái
`CODED_AND_TESTED_NOT_RUNTIME_PROVEN`, chưa deploy, chưa đụng production, nên không có gì để gỡ
trên VPS. Gỡ về mức code (nếu cần trước khi đợt deploy sau này gộp chúng lại): `git revert
b004f57` (adapter) và `git revert b9c2878` (vá materializer) trên nhánh chứa hai commit đó —
**chưa cần dùng đến**, ghi ở đây chỉ để đủ phần theo khung A55.3.

**Cho việc tạo báo cáo này (`CONG 5`, 06/09):** đây là thao tác **thêm tệp mới** vào thư mục báo
cáo công khai, không sửa tệp cũ nào. Gỡ về là xoá thư mục
`V11156_DONG_BON_MON_NO_20260903/` — không ảnh hưởng gì khác.

---

## 9 · THEO DÕI TIẾP

| # | việc | trạng thái | nguồn |
|---|---|---|---|
| 1 | `XI` 3-càng — thêm tầng ghi vết (`ranked_prefixes` · `prefix_method_version` · `parent_bt_source` · `cutoff_at` · provenance hash) | mở, theo verdict sửa lại `SUBSTANTIALLY_VALID` | `FU-450` cập nhật 03/09 |
| 2 | `RM-13` — ghi `registry_sha256` vào `source_predictions_json` mỗi bundle | chờ owner ký (`§52` mục 13) | commit `bd0ea86` |
| 3 | Nợ báo cáo 22 bản thiếu hẳn (thời điểm `V11156`) | `GAP_MARKER`, không viết bù | commit `bd0ea86` mục "NO BAO CAO" |
| 4 | Deploy gộp `G1` + `C1` cùng đợt runtime proof kế tiếp | chờ | commit `b9c2878` |
| 5 | Nợ báo cáo bản thân `V11156` (chính báo cáo này) | đóng bằng bản dựng lại này, `CONG 5`/`V11167`, 06/09/2026 | — |
| 6 | 22 bản còn thiếu báo cáo khác trong đợt `CONG 5` 06/09 | xem bảng phân loại riêng của `CONG 5` (không lặp ở đây, `RM-11`) | `V11167` |

---

## §62 — BA LỚP NGUỒN

### OWNER_SAID

| giờ | nguyên văn | nguồn |
|---|---|---|
| 02/09 ~22:40 | *«…Tiếp tục xử lý các vấn đề dứt điểm cho anh trong tối nay, backup và deploy đầy đủ cho anh.»* | `docs/SO_TUONG_TAC_OWNER.md`, cùng dòng dùng trong `REPORT_V11155.md` mục 2 |
| 03/09 ~09:00 (SAU phiên này, chỉ nêu để đối chiếu) | *«3 càng anh đang xây dựng với số đuôi bạch thủ»* | `docs/FOLLOW_UP_TRACKER.md` mục FU-450 cập nhật 03/09 |

Không có dòng `OWNER_SAID` nào mới, có mốc giờ nằm đúng trong 23:00–00:30, được tìm thấy cho
riêng bốn món nợ này — ghi rõ theo `RM-17`, không suy diễn.

### CODE_DID

- commit riêng `bd0ea862574b1b6ec404d6aaf4cade8003587bca` (23:40:29, `+179/-4` dòng trên 6 tệp
  tài liệu) + hai commit phụ trợ cùng đêm `b004f57d662f0489f4e883c6b1fe2cdc74476664` (23:13:55,
  `+333` dòng, `web/backend/_v11156_ranked_adapter.py`) và
  `b9c2878b3577344d4ac5e6aac5fcdf259982abc9` (23:26:31, `+45/-4` dòng,
  `web/backend/_materialize_shadow_promotion_scorecard.py:307-311`)
- `governance_seq`: `471 → 472` (`docs/AUTOMATION_STATE.json`)
- `docs/AUTOMATION_HISTORY.jsonl` dòng `V11156`: `"runtime_thay_doi": false`
- tự kiểm: `_v11155_test_vai_tro` 19/19 · `_v11150_test_contract` 37/37 · ranked adapter 13/13
- **không** có commit deploy/restart nào cùng đêm gắn với `V11156` — xác nhận qua
  `git log --oneline b9c2878..bd0ea86` (chỉ một commit, chính `bd0ea86`, thuần tài liệu)

### DOC_SAID

- `CHANGELOG.md` mục `## V11156 — 2026-09-03 (23:00–00:30) — ĐÓNG BỐN MÓN NỢ`
- `docs/CURRENT_TRUTH_SSOT.md` mục `### V11156 (03/09/2026 23:00–00:30)`
- `docs/FOLLOW_UP_TRACKER.md` mục `FU-449 / FU-450 (CẬP NHẬT 03/09 — ĐÓNG BỐN MÓN NỢ)`

### Ba lớp lệch nhau ⇒ FINDING

**`DOC_SAID` (bản gốc `V11156`) ≠ `DOC_SAID` (bản cập nhật `FU-450` cùng ngày 03/09):** mục `XI`
kết luận `NO_VALID_3CANG` trong bản gốc, và **chính tài liệu dự án** (`FOLLOW_UP_TRACKER.md`) đã
tự sửa lại thành `SUBSTANTIALLY_VALID` chỉ trong cùng một ngày — sau khi có thêm một câu
`OWNER_SAID` mới (03/09 ~09:00) làm rõ tiền đề. Đây là ví dụ cho thấy `DOC_SAID` không phải một
lớp tĩnh: nó có thể tự mâu thuẫn với chính nó theo thời gian, và bản dựng lại này phải trình bày
**cả hai thời điểm** thay vì chỉ chọn bản mới nhất và giả vờ bản cũ chưa từng tồn tại.

---

TanPhatAI cần làm: đây là **báo cáo dựng lại (backfill)**, không phải báo cáo viết đồng thời —
tự thân việc này (`CONG 5` của phiên `V11167`, 06/09/2026) là một trường hợp **CODE ĐI TRƯỚC TÀI
LIỆU** kéo dài ba ngày (`bd0ea86` commit 02/09, báo cáo công khai xuất hiện 06/09), đúng phạm vi
`PRJ-INTERACTION-LEDGER-001`. Ghi nhận: (1) mục `XI` 3-càng trong bản gốc đã bị **rút lại** ngay
hôm sau (03/09) vì owner sửa tiền đề thiết kế — đã dán hộp rút lại đủ bốn phần ngay tại mục 3.1
của báo cáo này, không cần Notion lặp lại một lần nữa mệnh đề `NO_VALID_3CANG` đã sai. (2) `RM-13`
đóng **có điều kiện**, hẹp phạm vi vào đúng cửa sổ `_v11155`, còn một việc chờ owner ký
(`registry_sha256` vào bundle). (3) Hai bản vá `G1`/`C1` đang ở trạng thái
`CODED_AND_TESTED_NOT_RUNTIME_PROVEN` — **chưa deploy**, TanPhatAI không nên báo đây là đã chạy
production. (4) Nợ báo cáo của chính `V11156` nay đã đóng bằng bản này; còn 22 bản khác trong đợt
dọn nợ `V11167` 06/09 vẫn đang được `CONG 5` phân loại riêng, xem báo cáo tổng hợp của phiên đó
để có số cuối cùng.
