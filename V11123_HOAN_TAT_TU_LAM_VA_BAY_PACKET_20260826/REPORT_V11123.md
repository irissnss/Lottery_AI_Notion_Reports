# V11123 — HOÀN TẤT VIỆC TỰ LÀM + **BẢY DECISION PACKET** · VÀ MỘT TỆP OWNER TƯỞNG CHƯA ĐẨY THÌ **ĐÃ Ở TRÊN GITHUB**

**Ngày:** 26/08/2026 · **Commit riêng:** `2ee0f9a` → *(bản này)* · **Trạng thái:** `PARTIAL` —
xem §9.0 để biết **chính xác** phần nào chưa đạt

---

## 1. Tóm tắt

Prompt 37 `GĐ-0`…`GĐ-8`. Phiên `READ-ONLY` với production: **không** deploy · **không** restart ·
**không** ghi DB · `M0`/official/roster/FINAL **không đổi một dòng** (chứng minh bằng hash ở §5).

### 🔴 Điều phải báo trước mọi thứ khác

Tài liệu tổng kết owner gửi ghi: *«Một tệp em KHÔNG đẩy: `REPORT_V11037.md` — cổng an toàn chặn 12
vi phạm… Phần bổ sung của tệp đó đang chờ anh quyết.»*

**Câu đó SAI.** Đo `26/08`:

| phép | kết quả |
|---|---|
| `git branch -r --contains eab8c24` | **`origin/main`** — commit `eab8c24` (25/08 `18:43:41`) **ĐÃ PUSH** |
| bản **trên remote** | **IP 3 dòng · `root@` 3 dòng · đường dẫn máy chủ 6 dòng** |
| dòng `184` | một lệnh `ssh root@<IP>` **đầy đủ**, kèm đường dẫn tuyệt đối tới DB |
| tổng tệp trên remote chứa `root@` | **24** |

Cổng an toàn **chặn đúng** — nhưng nó **chưa bao giờ được nối vào đường commit**, nên commit vẫn đi
qua. ⇒ `PACKET 0`, cần owner ký **ngay**.

## 2. Owner yêu cầu gì (nguyên văn)

> *« 1. Hoàn tất tất cả công việc Agent IDE có đủ quyền và bằng chứng để tự xử. 2. Với mọi việc cần
> Owner quyết: điều tra đến nơi; trình bằng lời thường; nêu code/runtime thật; nêu được, mất, rủi
> ro; đưa khuyến nghị; đưa test, gate và rollback; **kết thúc bằng đúng một câu Owner cần trả lời**.
> 3. Cập nhật tài liệu theo kịp code. 4. **Không suy diễn yêu cầu làm rõ thành chữ ký thực thi.**
> 5. Không để Owner phải hỏi "treo à?": phải báo tiến độ sau từng giai đoạn. »*
> — prompt 37, `26/08/2026`

`AUTHORIZED_LAYER = LOCAL_CODE_GIT_DB_COPY_TEST_VPS_READ_REPORT` — **VPS chỉ ĐỌC**.

## 3. Đào bới / phát hiện

### 3.1 · `GĐ-0` — preflight bắt **hai lỗi trong module dựng đêm trước**

Tiến trình khởi động lại (`PID 17016` → `18000`) nhưng `CLAUDE_CODE_SESSION_ID` **giữ nguyên** ⇒
nhánh «cùng phiên» của `lay()` chạy **trước** phép kiểm PID chết ⇒ lease ghi **PID đã chết** làm
chủ. Lỗi hai: đếm ngược từ `lay_luc` thay vì `cham_luc` ⇒ in *«còn −11 777s»*. **Đã vá**, thử lại
**8/8**.

### 3.2 · `GĐ-3` — phép đo **BÁC giả định của chính agent**

Giả định vào phiên (và trong current-truth của prompt 36/37): *«4 ML dùng chung pipeline ứng
viên/đặc trưng»*. Đo **526 ngày–miền**:

| cụm | đồng phiếu |
|---|---|
| `xgboost` · `random-forest` · `meta-learning` · `smart-ml` · `combo-no-token` | **59,6 – 87,1%** |
| 🔴 **`lstm` vs cụm trên** | **3,7 – 5,0%** |
| đối chứng **khác họ** | **4,1 – 6,9%** |

⇒ `lstm` đồng phiếu với ba ML kia ở **đúng mức khác họ**. Và nó **cứu nhiều số trúng một mình nhất
toàn hệ: `91/387 = 23,5%`**. Gộp cả 4 ML là **phá đúng nguồn độc lập nhất**.

**Bốn phép owner yêu cầu:** đồng phiếu (trên) · unique-save (**387** ca) ·
**RANK FLIP `251/525 = 47,8%`** · **WOULD-BREAK `123/525 = 23,4%`**.
`47,8%` **xa** ngưỡng `≤ 2/423` ⇒ `S1` **KHÔNG** phải `OPERATIONALLY_EQUIVALENT_TO_M0`.

Chi tiết + bảng registry **49/49**: `docs/FAMILY_MAP_SHADOW_DEDUPE_20260826.md`.

### 3.3 · `GĐ-4` — `D1`: **2 đủ · 3 thiếu**, và một khuyết tật **mới tìm ra**

🟢 `scorer pass` (`T8` `423/423`) · 🟢 `official path không đổi`.
🔴 `dữ liệu sạch` · 🔴 `card hoàn chỉnh` · 🔴 `mapping family` (đã trình, **chưa ký**).

> 🔴 **Khuyết tật mới:** `TOTAL_V2_CONTRACT` ghi *«Mọi bundle từ nay phải mang
> `total_method_version`»* — nhưng `grep TOTAL_METHOD_VERSION` **toàn kho mã** ra **0 dòng**. Nó
> chỉ tồn tại trong **ba tài liệu**. `final_bundles` có `generation_method` · `policy_version_ref` ·
> `bundle_version` — **không** có trường đó. Hợp đồng đang mô tả một thứ **chưa được cài**.

### 3.4 · `GĐ-5` — **EXACT SHA** đã xác minh

| | |
|---|---|
| artifact | `web/backend/main.py` @ blob **`83a4657cd471a1894b703cb894706d9c42bde705`** |
| commit sinh ra | **`c8d87a54795646418f85be9474865631881fb90f`**, `25/08 20:37:36 +07` |
| không đổi từ đó | ✅ `git diff HEAD` **rỗng**; md5 đĩa `e113e16d…` khớp git |
| diff so với trước vá | **+169 / −10**, **1 tệp** |
| backup | `1.007.440 B`, md5 `a5472268a3d02719…` |

🔴 **Đính chính:** báo cáo trước ghi release candidate là *«`c8d87a5` + `731a10a`»*.
**`731a10a` KHÔNG chạm `main.py`** — nó gỡ blob backup và sửa `.gitignore`.

**Route matrix — `29` route** (không phải 27): `_cong_bundle_admin` **5** · `require_admin` **17** ·
lọc trường **2** · 🔴 **không cổng 4** (`FU-440`) · trang tĩnh **1**.

### 3.5 · `GĐ-6` — ý nghĩa thật của sàn `96`

McNemar, `α=0,05` hai phía, power `80%`: `n_d ≥ (z_{α/2}+z_β)² / (4(π−0,5)²) = 7,85/(4(π−0,5)²)`.
`n_d = 96` ⇔ phát hiện được ứng viên thắng **`π ≈ 0,643`** số cặp bất đồng.
**Sàn không tuỳ tiện — hạ nó là đổi câu hỏi.**

`26/08 → 23/09` = `87` region-day; `b+c ≤ 87 < 96` là **trần số học**, không phụ thuộc ước lượng.
⇒ **`NO_PROMOTION_INSUFFICIENT_POWER` biết trước từ hôm nay.**
Điều này **KHÔNG** có nghĩa *«hệ thống vô dụng»* — nó có nghĩa **cửa sổ 29 ngày không đủ dài cho
thước này**.

### 3.6 · Phép đo ra kết quả **ÂM** — vẫn ghi đủ

| # | đo gì | kết quả |
|---|---|---|
| 1 | 4 đường `FU-440` có rò trường nhạy cảm không | **KHÔNG thấy** — nên agent **không vá**, chỉ khai `FU-440` |
| 2 | `TOTAL_METHOD_VERSION` có trong mã không | **KHÔNG** — 0 dòng toàn kho |
| 3 | 4 hook Cursor có hook nào nổ trong phiên Claude Code không | **KHÔNG** — sổ điểm danh im từ `16/08` |
| 4 | cổng A55 có được nối hook không | **KHÔNG** — `grep` 0 dòng ở 4 nơi |
| 5 | 22 làn của phiên trước còn chạy không | **KHÔNG** — đã dừng, 2/22 có kết quả, 6 làn mất, 14 chưa chạy |

## 4. Hướng xử lý và vì sao chọn

| việc | lối đã chọn | vì sao loại lối kia |
|---|---|---|
| cổng A55 | bỏ `[:8]` **+ khoá mốc thi hành `V10921` + luật hậu tố** | bỏ `[:8]` trần trụi ⇒ `424/575` trượt, con số **vô dụng**, và cổng đỏ vì lý do sai thì người ta học cách bỏ qua |
| bù 10 report | dựng từ **ba nguồn đương thời**, đánh dấu rõ phần không khôi phục được | soạn hộ = chế lịch sử; để trống = mất luôn |
| family | **`A` rồi `B` trong shadow** | `C` hard-collapse **phá** `lstm` — nguồn độc lập nhất |
| `FU-440` | **không vá**, chỉ khai | vá cái chưa chứng minh là rò = *«đổi mù»* |
| nối cổng A55 vào hook | **không tự nối** | nối cứng chặn mọi commit tới khi bù đủ 23 báo cáo ⇒ quyết định vận hành |

## 5. Đã làm gì

| tệp | thay đổi |
|---|---|
| `web/backend/_v10921_report_gate.py` | `FU-442` — worklist ba nguồn · bỏ `[:8]` · sắp theo thời gian · băng-rôn theo phạm vi · fail-closed · sổ điểm danh |
| `web/backend/_v11120_session_lease.py` | vá 2 lỗi |
| `web/backend/_v11122_thu_chan_a55.py` | **mới** — 7 phép + hai chiều |
| `docs/FAMILY_MAP_SHADOW_DEDUPE_20260826.md` | **mới** — registry 49/49 + 4 phép đo + 3 lối |
| `docs/DECISION_PACKET_20260826.md` | **mới** — **7 packet** đủ 10 phần |
| `docs/SO_TUONG_TAC_OWNER.md` | **ba chuyên mục** |
| `docs/FOLLOW_UP_TRACKER.md` | khai `FU-444`; `FU-442` đóng |
| `CLAUDE.md` `§0` + hai mặt sinh | thôi dạy chế độ mù |
| kho công khai | **10 thư mục báo cáo bù** + `V11122_*` + `V11123_*` |

### 🟢 CHỨNG MINH OFFICIAL **KHÔNG ĐỔI** — hash 4 bảng khoá

Đọc `02:0x` ngày `26/08` (phiên **không** ghi DB một lần nào):

| bảng | dòng | md5 (20 ký tự đầu) |
|---|---|---|
| `predictions` | 13.129 | `27c730e3f1f8d1b574e2` |
| `final_bundles` | 526 | `31a67c94361df9129318` |
| `lottery_results` | 15.324 | `dbc84f41458945c93740` |
| `model_daily_eval` | 12.953 | `e7b517794f1d7902465c` |

`SELECT COUNT(*) FROM final_bundles WHERE date >= '2026-08-25'` ⇒ **0** — phiên này **không tạo,
không sửa** bundle nào.
*(Đọc trên bản local; theo `RM-01` bản này dừng ở `22/08` nên nó chứng minh **phiên không ghi**,
không chứng minh trạng thái VPS.)*

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v11122_thu_chan_a55.py` | ✅ **11/11 ĐẠT** · `T5` cổng nổ ⇒ **thoát 2 FAIL-CLOSED** |
| `_v11120_thu_chan_lease.py` | ✅ **8/8 ĐẠT** sau khi vá |
| `_v10921_report_gate.py` **toàn dải** | 42/201 trượt · **23** bản thiếu *(trước khi bù: 51/200 · 32)* |
| `_v10921_report_gate.py` **10 bản bù** | ✅ **10/10 ĐẠT** |
| `_v11110_cong_bao_cao_cong_khai.py` | ✅ **ĐẠT** trên **13** thư mục mới — 0 vi phạm |
| `_v11062_nang_version.py --kiem` | ✅ **ĐẠT** · `seq=453` |
| `_v10925_rule_sync_check.py` | ✅ **SÁU MẶT ĐỒNG BỘ** |
| `_v11044_cong_so_hieu.py` | ✅ **KHỚP** |
| `cong_git_commit.py` (9 cổng con) | ✅ có `DAT · 9/9` trong sổ điểm danh cho **mỗi** commit |

## 7. Vướng vấp

1. **Lần chạy toàn dải đầu tiên cho con số vô dụng** `424/575` — phải dừng, tìm mốc thi hành thật
   (`V10921`) và luật hậu tố rồi chạy lại. *Bỏ qua = giết chính cổng vừa vá.*
2. **Hai lỗi trong module dựng đêm trước** chỉ lộ ra vì tiến trình khởi động lại.
3. **Bộ quét route của agent bỏ sót bản vá của chính mình** (cửa sổ 14 dòng < docstring mới).
4. **Giả định `4 ML = 1 nguồn` bị chính phép đo bác** — nếu không đo mà cứ theo pipeline thì đã đề
   xuất gộp `lstm`, tức phá nguồn độc lập nhất.
5. **`prepend()` đặt khối mới lên TRÊN tiêu đề sổ** khi sổ chưa có mục ngày ⇒ phải sửa lại thứ tự.

## 8. Gỡ về

| việc | lệnh |
|---|---|
| toàn bộ `V11122`+`V11123` | `git revert` hai commit |
| chỉ cổng A55 | một tệp `_v10921_report_gate.py` |
| 10 báo cáo bù | `git rm -r` 10 thư mục ở kho công khai |
| tài liệu mới | ba tệp `docs/*.md` |

**Không có migration DB. Không đụng mã production.** `main.py` **không** thay đổi trong phiên này
(bản vá `FU-438` đã có từ `c8d87a5` hôm qua và **vẫn chưa deploy**).

## 9. Theo dõi tiếp

### 9.0 · 🔴 `PARTIAL` — phần **chưa đạt**, ghi chính xác

| BLOCKER | EVIDENCE CÒN THIẾU | AI CHỊU TRÁCH NHIỆM | NGÀY ĐÓNG |
|---|---|---|---|
| **23 bản còn thiếu báo cáo** (sau khi bù 10) | cần một phiên ghi riêng có lease; nguồn đã xác minh là có | Agent IDE | 30/09 |
| **`D1` thiếu 3/5 điều kiện** | 4 trường dòng dõi (đổi lược đồ) · số `material difference` trên thước `M0` · chữ ký bản đồ `ROOT` | **Owner** (điều kiện 1 và 4) + Agent (điều kiện 2) | chờ ký |
| **`TOTAL_METHOD_VERSION` chưa có trong mã** | trường định danh mà hợp đồng `TOTAL_V2` đòi | Agent IDE, sau khi owner ký family | chờ ký |
| **`FU-438` chưa deploy** | chữ ký owner (`AUTHORIZED_LAYER = VPS_READ`) | **Owner** | chờ ký |
| **7 packet chưa ký** | — | **Owner** | chờ ký |

⛔ **Không gọi phiên này là "đã xong tổng lực".** Bảy việc cần owner, một việc cần một phiên ghi riêng.

### 9.1 · ✅ ĐÃ TỰ HOÀN TẤT

| việc | bằng chứng |
|---|---|
| `FU-442` — vá 3 lỗ cổng A55 | thử **11/11**, mã thoát 0, có hai chiều |
| Bù **10** báo cáo công khai | cổng A55 **10/10 ĐẠT**; an toàn **10/10** |
| Family map **49/49** + 4 phép đo | `docs/FAMILY_MAP_SHADOW_DEDUPE_20260826.md` |
| Điều kiện `D1` — phần agent làm được | ablation đã chạy: `47,8%` ⇒ **không** tương đương `M0` |
| Sổ tương tác owner **ba chuyên mục** | `docs/SO_TUONG_TAC_OWNER.md` |
| Vá 2 lỗi khoá phiên `V11121` | thử lại **8/8** |
| `CLAUDE.md §0` thôi dạy chế độ mù | sáu mặt đồng bộ |

### 9.2 · 🔴 CHỜ OWNER — 7 packet, mỗi cái **một câu hỏi**

| # | việc | status | blocker | khuyến nghị |
|---|---|---|---|---|
| `P0` | **Scrub HEAD** — 24 tệp chứa `root@` trên remote | `RUNTIME_PROVEN` | owner | **A ngay + đổi khoá SSH trong 24h** |
| `P1` | **Deploy `FU-438`** | `READY_TO_DEPLOY` | owner (`VPS_READ`) | deploy tối nay ngoài block, giữ lọc trường cho `/api/predictions` |
| `P2` | `QD-041` + 14 quyết định quá hạn | `OWNER_DECISION` | owner | đóng **8**, gia hạn **7** tới `30/09` |
| `P3` | `FU-441` — 4 hook Cursor chết 9 ngày | `OWNER_DECISION` | owner | chuyển **2**, retire **2** |
| `P4` | `FU-443` — khoá tầng `prepend()` | `OWNER_DECISION` | owner | khoá **theo tệp**, thử race trên bản sao |
| `P5` | `FU-440` — 4 đường không auth | `OWNER_DECISION` | owner | đóng cả 4 về admin |
| `P6` | `FU-444` — nối cổng A55 vào commit | `OWNER_DECISION` | owner | nối **cảnh báo** nay, chuyển **chặn** khi hết nợ hoặc `30/09` |
| — | **Protocol `D3`** | `BLOCKED_EVIDENCE` | owner | đóng cũ (`NO_PROMOTION`), mở `N2` + `N3` |

### 9.3 · ATTRIBUTION LEDGER

| ai | làm gì trong phiên này |
|---|---|
| **Owner** | viết prompt 37; đặt `AUTHORIZED_LAYER = VPS_READ`; **chưa ký** bất kỳ mục nào |
| **Agent IDE (Coordinator)** | **toàn bộ** phần đọc, đo, sửa mã, viết tài liệu, commit, push |
| **TanPhatAI** | **không** tham gia phiên này; **không** sửa dòng mã nào; nhận bàn giao sau |
| *(làn con)* | **không dùng** trong phiên này — 8 làn của prompt 36 đã xong từ hôm trước |

### 9.4 · CROSS-LAYER MATRIX

| tầng | trạng thái sau phiên |
|---|---|
| **Local** | `main.py` **không đổi** (bản vá `FU-438` từ `c8d87a5`) · cổng A55 + lease đã vá · 3 tài liệu mới |
| **Git riêng** | `2ee0f9a` → *(commit bản này)* · **0/0** với remote |
| **Git công khai** | `87e6cd5` → *(commit bản này)* · **0/0** · +13 thư mục báo cáo |
| **VPS** | 🔴 **KHÔNG ĐỤNG** — vẫn chạy mã **trước** `FU-438`, **vẫn đang rò ~678 KB** |
| **DB** | 🔴 **KHÔNG GHI** — hash 4 bảng khoá ở §5; 0 bundle mới |
| **Notion** | 🔴 **KHÔNG ĐỤNG** — `§57.1` cấm ghi; chờ `TanPhatAI` |
| **Report** | 13 thư mục mới (10 bù + `V11122` + `V11123`) |

### 9.5 · RÚT LẠI / THAY THẾ trong phiên này

| # | câu bị rút | nguồn | điều đúng |
|---|---|---|---|
| 1 | *«`REPORT_V11037.md` — em KHÔNG đẩy»* | tài liệu tổng kết owner | **ĐÃ PUSH** — `eab8c24`, `origin/main`, còn `root@` + IP |
| 2 | *«release candidate `c8d87a5` + `731a10a`»* | `REPORT_V11120` | `731a10a` **KHÔNG chạm `main.py`** |
| 3 | *«27 route»* | prompt 37 §VIII.3 | đo được **29** route |
| 4 | *«4 ML dùng chung pipeline ⇒ cùng nguồn»* | current-truth prompt 36/37 §11 | **`lstm` KHÔNG** — đồng phiếu `3,7–5,0%` = mức khác họ |
| 5 | *«`_v10872` thiếu 6/27 model»* | báo cáo lane prompt 36 | trên **toàn registry 49** là thiếu **28**; con số 6 đúng cho tập `ACTIVE+SHADOW_AUTO` hẹp |
| 6 | *«10 bản thiếu báo cáo»* | `V11119` | đúng cho dải `V11070–V11199`; **toàn dải** là **32** (sau bù còn **23**) |

*(`R6`/`R7` của `V11119` đã rút ở `V11121` — không lặp lại ở đây.)*

---

## 10. BA LỚP NGUỒN (§62 · A60)

### `OWNER_SAID`
> *«Hoàn tất tất cả công việc Agent IDE có đủ quyền và bằng chứng để tự xử.»*
> *«**Không suy diễn yêu cầu làm rõ thành chữ ký thực thi.**»*
> *«Không được khuyến nghị `C` chỉ vì "cùng pipeline".»*
> *«Không hạ ngưỡng. Không tự kéo dài.»* — prompt 37, `26/08/2026`

### `CODE_DID`
| điều mã **thực sự** làm | bằng chứng |
|---|---|
| `REPORT_V11037.md` **đang ở** `origin/main` với chuỗi đăng nhập | `git branch -r --contains eab8c24` → `origin/main`; dòng `184` |
| `lstm` **không** đồng phiếu với 3 ML kia | `3,7% / 5,0% / 4,7%` trên n=`427/423/405` |
| dedupe theo root đổi hạng 1 ở **47,8%** ngày–miền | `251/525`, thước **số phiếu** (proxy) |
| `TOTAL_METHOD_VERSION` **không tồn tại** trong mã | `grep` toàn kho = **0 dòng** |
| phiên này **không ghi DB** | 4 hash + `0` bundle mới từ `25/08` |
| `main.py` **không đổi** trong phiên | `git diff HEAD` rỗng; blob `83a4657` từ `c8d87a5` |

### `DOC_SAID`
| tài liệu | nói gì | khớp code chưa |
|---|---|---|
| tổng kết owner | *«không đẩy `REPORT_V11037.md`»* | 🔴 **SAI** — đã push |
| `TOTAL_V2_CONTRACT_20260825.md` | *«mọi bundle phải mang `total_method_version`»* | 🔴 **CHƯA CÀI** — 0 dòng mã |
| prompt 37 §II.3 | release candidate `c8d87a5` + `731a10a` | 🟡 **một nửa** — `731a10a` không chạm `main.py` |
| prompt 37 §VIII.3 | *«27 route»* | 🟡 đo được **29** |
| prompt 37 §II.11 | *«4 ML dùng chung pipeline»* | 🟡 **đúng về pipeline, sai về hệ quả** — `lstm` vẫn độc lập theo phép đo |

### 🔴 BA LỚP LỆCH NHAU — finding bắt buộc báo

- `DOC_SAID` ≠ `CODE_DID` ở **năm** chỗ trên. Nặng nhất là chỗ đầu: owner **tin** một tệp chưa
  public trong khi nó **đang public** kèm chuỗi đăng nhập máy chủ.
- `OWNER_SAID` ≠ `CODE_DID`: owner khoá *«viewer/anonymous đóng»* từ `06/06`; mã **vẫn** phục vụ
  `~678 KB` nội dung nội bộ cho khách ẩn danh. Bản vá **đã có**, **chưa deploy**.
- `OWNER_SAID` ≠ `DOC_SAID`: prompt 37 khoá *«4 ML dùng chung pipeline… cho phép family mapping và
  shadow dedupe»* — phép đo cho thấy **mapping phải tách `lstm` ra**, nếu không sẽ dedupe nhầm.

---

**TanPhatAI cần làm:** (a) **đọc `PACKET 0` trước tiên** — có một chuỗi đăng nhập máy chủ đang
public trên `origin/main`, và owner đang tin là chưa; (b) ghi vào **Current Control**: `FU-438` là
`CODE_PUSHED`/`READY_TO_DEPLOY`, **KHÔNG** phải `DEPLOYED` — production vẫn rò `~678 KB`; `D1`
**2/5** điều kiện; `D3` sẽ là `NO_PROMOTION_INSUFFICIENT_POWER`; (c) ghi vào **Decision Ledger**:
**7 packet chưa ký**, mỗi packet có **đúng một câu hỏi**, xem `docs/DECISION_PACKET_20260826.md`;
(d) ghi vào **Active Plan Ledger**: bù **23** báo cáo còn lại (hạn `30/09`) và ba protocol `N1`/`N2`/
`N3` chờ owner chọn; (e) **đừng** coi prompt 37 là chữ ký — sổ tương tác mục `OWNER_XAC_NHAN` ghi
rõ **7/7 CHƯA KÝ**; (f) `TanPhatAI` **không** sửa dòng mã nào trong phiên này — xem Attribution
Ledger §9.3.
