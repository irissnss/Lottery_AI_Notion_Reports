# V11120 — `FU-438`: BỀ MẶT CÔNG KHAI RÒ **~678 KB**, KHÔNG PHẢI 39,7 KB — VÁ FAIL-CLOSED, **CHƯA DEPLOY**

**Ngày:** 25/08/2026 · **Commit riêng:** `c8d87a5` + `731a10a` · **Commit công khai:** *(bản này)* ·
**Trạng thái:** 🔴 **`READY_TO_DEPLOY_FU438`** — code xong, test 17/17, **chưa deploy**

---

## 1. Tóm tắt

Prompt 36 mục `V` giao đóng `FU-438`. Đo lại trên production (`RM-13`, gọi **ẩn danh** qua tên miền
công khai, `19:27` và `20:2x` giờ VN) thì bề mặt rò **lớn hơn hẳn** con số đã công bố ở `V11119`:

| đường | byte trả về khách ẩn danh | trường nội bộ lộ ra |
|---|---|---|
| `/api/predictions` | **328.878** | `voters` · `analysis_text` · `reasoning_json` · `top1_reason` · `candidate_support_map` |
| `/api/prediction-trace` | **253.755** | `top1_reason` · `candidate_support_map` |
| `/api/prediction-quality` | **56.194** | `voters` |
| `/api/final-bundle/history` | **39.682** | `ranked_numbers` · `voters` · `source_predictions_json` · `score_breakdown` · `components` |
| **tổng** | **≈ 678 KB** | |

`V11119` báo `39.682 B`. Con số đó **đúng cho một đường, nhưng thiếu ba đường còn lại** — trong đó
`/api/predictions` một mình đã **gấp 8 lần**, và mang `analysis_text` + `reasoning_json`, đúng thứ
`V11042` từng gọi là *«phương pháp của hệ»* khi vá `/api/status`.

Đã vá **hai lớp**, thử chặn **17/17 ĐẠT** (có thử hai chiều `RM-15`). **Chưa deploy** — xem §5.

## 2. Owner yêu cầu gì (nguyên văn)

> *« **V. P0 SECURITY — FU-438** … 3. Patch common admin gate fail-closed. … 5. Anonymous/non-admin
> phải 401/403 hoặc redirect login. Admin Owner phải thấy full current/history. … 9. Nếu thiếu quyền
> deploy: dừng tại `READY_TO_DEPLOY_FU438` và hỏi Owner đúng một câu duyệt deploy. »*
> — prompt 36, `25/08/2026`

> *« Owner đã khóa `ADMIN_ONLY`/`CLOSE_VIEWER`; không hỏi lại chính sách này. »* — prompt 36 mục `III`

## 3. Đào bới / phát hiện

### 3.1 · Nguyên nhân là **CẤU TRÚC**, không phải quên một dòng

| hàm | chữ ký thật | hệ quả |
|---|---|---|
| `api_get_bundle_history(region, limit)` | **không có `request`** | về mặt **vật lý** không thể gọi bất kỳ phép kiểm quyền nào |
| `api_selection_delta(region, days)` | **không có `request`** | như trên |
| `api_get_final_bundle(request, region, date)` | **có `request`** | nhưng **chỉ KẸP NGÀY** (`_freeze_clamp_date`), **không lọc trường** |

Ba docstring đều ghi *«No auth required (public-facing, same as /du-doan)»* — câu đó **sai về hậu
quả**, vì thân bundle là `SELECT *` từ `final_bundles` (`database.py:4718-4729`) nên vẫn mang
`source_predictions_json`.

### 3.2 · `/api/final-bundle` im lặng hôm nay là **MAY, không phải thiết kế**

Đo ẩn danh với ba ngày ≤ mốc đóng băng: cả ba trả `1.711 B`, **không** trường nội bộ. Đọc mã thì
thấy lý do: cổng publish rơi vào nhánh rỗng `WAIT_MODEL_COUNT`. **Khi nhánh đó không nổ**, hàm trả
`bundle` đầy đủ — tức **rò tiềm tàng đúng cùng nhóm trường**.

### 3.3 · Phép đo **âm** cũng ghi đủ

| đường | kết quả |
|---|---|
| `/api/model-selection` · `/api/prediction-advisory` · `/api/model-ranking` · `/api/repredict-quality` | `200`, **không** trường nhạy cảm nào trong phép đo. **Không vá** — chỉ báo là chúng **không có auth**, để owner quyết |

## 4. Hướng xử lý và vì sao chọn

**Hai lớp, cố ý không dùng một lớp:**

**① `_cong_bundle_admin(request)` — FAIL-CLOSED.** Thiếu `request` ⇒ `401`; tầng auth **NỔ** ⇒ `403`.
Khác hẳn `_viewer_freeze_on()` ngay cạnh vốn `except → False` (fail-**OPEN**): mẫu đó **đúng** cho
việc *kẹp ngày*, **sai** cho việc *giữ cửa*. Gắn vào **năm** đường.

**② `_bundle_cho_khach()` + danh sách CHO PHÉP** — để nếu về sau ai mở lại cho khách thì mặc định
vẫn sạch. Cố ý **không** dùng danh sách cấm: bảng `final_bundles` còn được thêm cột, deny-list sẽ
rò ngay lần thêm cột sau mà không ai hay.

**`/api/predictions` xử KHÁC — lọc trường, không đóng cứng.** Nó là nguồn của **trang công khai**
`/user-view` (`user-view.js:426`). Đóng cứng là trang tắt hẳn ⇒ phá luật sản phẩm *«luôn xuất số»*.
Dùng **đúng khuôn `V11042`** đã chọn cho `/api/status`: danh sách rút từ **chính** `user-view.js:466-487`
(10 trường trang thật sự đọc), thêm đúng `hit_level`. **Không đoán thêm trường nào.**

## 5. Đã làm gì

| tệp | thay đổi |
|---|---|
| `web/backend/main.py` | `+169 / −10` — thêm `_cong_bundle_admin` · `_bundle_cho_khach` · `_TRUONG_BUNDLE_KHACH_DUOC_XEM` · `_TRUONG_LICH_SU_KHACH_DUOC_XEM`; gắn cổng vào **5** đường; lọc trường ở `/api/predictions`; **gỡ** ba câu docstring *«No auth required»* sai sự thật |
| `web/backend/_v11120_thu_chan_fu438.py` | **mới** — bộ thử 7 ca + thử hai chiều |
| `backups/main.py.pre_FU438_20260825` | backup `1.007.440 B` *(giữ trên đĩa, không đưa vào Git — Git đã có bản trước-vá tại `de35b10`)* |

🔴 **KHÔNG deploy · KHÔNG restart · KHÔNG ghi DB.** `AUTHORIZED_LAYER` của prompt 36 là
**`VPS_READ`**, không phải `VPS_WRITE` ⇒ theo đúng mục `V.9`, **dừng tại `READY_TO_DEPLOY_FU438`**.

## 6. Cổng kiểm

| phép | kết quả |
|---|---|
| `py_compile main.py` | **OK** |
| `_v11120_thu_chan_fu438.py` | ✅ **17/17 ĐẠT**, mã thoát `0` |
| — ca 1 ẩn danh | `401` |
| — ca 2 user thường | `403` |
| — ca 3 admin | cho qua, trả về `{'role': 'admin'}` |
| — ca 4 **thiếu `request`** | `401` |
| — ca 5 **tầng auth NỔ** | `403` *(fail-closed — đây là ca `_viewer_freeze_on` sẽ trả `False`)* |
| — ca 6 sáu đường chị em | đủ `request` + gọi đúng cổng |
| — ca 7 danh sách cho phép | bóc hết trường nội bộ, giữ 7 trường an toàn; danh sách lịch sử đủ cho `user-view`, **0** trường cấm |
| — **thử HAI CHIỀU (`RM-15`)** | gỡ cổng khỏi `/history` ⇒ phép kiểm **BẮT ĐƯỢC**; bản thật ⇒ **CHO QUA** |
| cổng `git commit` (9 cổng con) | **ĐẠT** — có dòng `DAT · 9/9` trong sổ điểm danh |

## 7. Vướng vấp

1. **Bộ quét route của chính agent bỏ sót** — cửa sổ 14 dòng, mà docstring mới dài hơn ⇒ báo nhầm
   *«chưa gắn cổng»*. Đã quét lại với cửa sổ 34 dòng và xác nhận cả ba đường **đã gắn**.
   *Hậu quả nếu bỏ qua:* báo cáo sai về chính bản vá vừa viết.
2. **Giả thuyết ban đầu sai và phải tự bác:** agent định kết luận `/api/final-bundle` *«chặn đúng»*.
   Đo thật với ba ngày ≤ mốc đóng băng thì đúng là không rò — **nhưng lý do là cổng publish rỗng,
   không phải lọc trường**. Nếu không đọc mã thì đã bỏ sót một rò tiềm tàng.
3. **Công cụ Bash bị kẹt thư mục làm việc cả nửa phiên** vì hook `git commit` gọi bằng đường dẫn
   tương đối — chi tiết ở `REPORT_V11121`.

## 8. Gỡ về

```
cp backups/main.py.pre_FU438_20260825 web/backend/main.py
```
Hoặc `git revert c8d87a5`. Backup `1.007.440 B` khớp `md5` bản trước vá. **Không có migration DB,
không có gì để rollback ở phía dữ liệu** — bản vá chỉ đụng tầng route.

## 9. Theo dõi tiếp

| mã | việc | ngưỡng đóng bằng số | ai chặn |
|---|---|---|---|
| `FU-438` | **Deploy bản vá** | sau deploy: khách ẩn danh nhận `401/403` ở cả 5 đường · admin thấy đủ current + history · `health 200` · `NRestarts` không tăng · **0 traceback** · `/user-view` vẫn vẽ được bảng lịch sử | 🔴 **OWNER** — cần một câu duyệt deploy (`AUTHORIZED_LAYER = VPS_READ`) |
| `FU-440` *(mới)* | Bốn đường **không có auth** mà phép đo **không** thấy trường nhạy cảm: `/api/model-selection` · `/api/prediction-advisory` · `/api/model-ranking` · `/api/repredict-quality` | quyết: đóng admin hay để công khai có chủ ý | 🔴 **OWNER** |

---

## 10. BA LỚP NGUỒN (§62 · A60)

### `OWNER_SAID`
> *«Anonymous/non-admin phải 401/403 hoặc redirect login. Admin Owner phải thấy full current/history.»*
> *«Nếu thiếu quyền deploy: dừng tại `READY_TO_DEPLOY_FU438` và hỏi Owner đúng một câu duyệt deploy.»*
> — prompt 36, `25/08/2026`

### `CODE_DID`
| điều mã **thực sự** làm | bằng chứng |
|---|---|
| 4 đường trả **~678 KB** cho khách ẩn danh | `curl` ẩn danh `19:27`+`20:2x`, đếm trường, **không in giá trị** |
| `history`/`selection-delta` **không thể** kiểm quyền | chữ ký hàm không có `request` |
| `final-bundle` chỉ **kẹp ngày**, không lọc trường | `_freeze_clamp_date` + `SELECT *` tại `database.py:4718-4729` |
| cổng mới **fail-closed** ở cả 4 nhánh | thử 17/17, gồm ca thiếu `request` và ca auth nổ |

### `DOC_SAID`
| tài liệu | nói gì | khớp code chưa |
|---|---|---|
| docstring 3 hàm | *«No auth required (public-facing…)»* | 🔴 **SAI VỀ HẬU QUẢ** — đã gỡ |
| `REPORT_V11119` | *«rò 39.682 B»* | 🟡 **THIẾU** — thật là ~678 KB; đã rút lại trong bản này |
| `main.py:6305-6311` | owner ký treo **toàn bộ** view người dùng `06–08/06` | 🔴 **LỆCH** — 4 đường vẫn phục vụ khách ẩn danh **78 ngày** |

### 🔴 BA LỚP LỆCH NHAU
`OWNER_SAID` ≠ `CODE_DID`: owner ký treo view `06/06`, mã vẫn trả bảng xếp hạng nội bộ cho khách
suốt **78 ngày**. `DOC_SAID` ≠ `CODE_DID`: docstring nói *«public-facing»* trong khi thứ trả về là
`ranked_numbers` + `voters`. Cả hai đã đóng ở tầng mã, **chưa đóng ở production**.

---

**TanPhatAI cần làm:** ghi nhận (a) `FU-438` nay là **`CODE_PUSHED`**, **KHÔNG** phải `DEPLOYED` —
production **vẫn đang rò ~678 KB** cho tới khi owner ký deploy; (b) con số `39.682 B` của
`REPORT_V11119` là **thiếu**, số đúng là **~678 KB** trên 4 đường, `/api/predictions` là đường lớn
nhất; (c) `/api/predictions` **không** bị đóng cứng mà bị **lọc trường** — trang công khai
`/user-view` vẫn phải vẽ được bảng lịch sử sau deploy, đó là phép kiểm bắt buộc; (d) mở `FU-440`
cho 4 đường không auth mà phép đo chưa thấy rò.
