# REPORT V11042 — GÓI KÝ GỘP 7 QUYẾT ĐỊNH + ĐÓNG LỖ HỔNG `/api/status`

**Ngày:** 2026-08-08 23:40 → 2026-08-09 01:05 giờ VN
**Phiên bản:** V11042 · **Tầng verdict:** `RUNTIME_PROVEN` cho QD-050 (đã deploy, đo trên
production) · `REPORT_PROVEN` cho phần còn lại

---

## 1. Tóm tắt

Owner ký gộp **23:38 08/08** bảy quyết định. Thi hành: **3 làm được ngay · 1 hoãn có lý do đo
được · 3 phải hỏi lại vì tiền đề lệch thực tế**.

| # | quyết định owner | mã | kết cục |
|---|---|---|---|
| 1 | FU-290A — bỏ cờ `output_eligible` | `QD-048` | ⏸ **HOÃN tới 21/08**, ba lý do đo được |
| 2 | xác nhận `QD-044` (FU-346 đóng) | `QD-044` | ✅ xong — `ACTIVE_DA_XAC_NHAN` |
| 3 | B1 — phê chuẩn hành vi `/du-doan` | `QD-049` | ⚠ **hỏi lại** — mệnh đề NGƯỢC với code |
| 4 | B2 — bảo vệ `/api/status` | `QD-050` | ✅ **xong + ĐÃ DEPLOY** |
| 5 | FU-224 — gộp 4 trang | `QD-051` | ⚠ **hỏi lại** — không phải 4 trang, `OWNER_LOCK` chưa gỡ |
| 6 | FU-315 — giãn ngày nặng | `QD-052` | ✅ **xong** — 27 mục dời, mọi ngày ≤ trần 6 |
| 7 | P2 — giữ PHASE-FIRST | `QD-053` | ⚠ **hỏi lại** — ngược quyết định owner ký 25/06 |

**Không giấu mục nào.** Ba mục "hỏi lại" được ghi vào sổ với trạng thái
`CHO_OWNER_XAC_NHAN_LAI` — **không** ghi `ACTIVE`, vì ghi ACTIVE là tạo đúng tình huống RM-19
cấm: hai quyết định ngược nhau cùng hiệu lực.

---

## 2. Owner yêu cầu gì (nguyên văn)

> **OWNER SIGNATURE: Owner ký gộp 23:38 08/08 — bảy quyết định:**
> (1) FU-290 phương án A — BỎ CỜ `output_eligible`, model vẫn chạy vẫn đo, sàn ML≥4 · AI≥3;
> (2) XÁC NHẬN QD-044 (FU-346 đóng);
> (3) B1 — phê chuẩn hành vi hiện tại của `/du-doan` (bundle=None, empty=True ở `main.py:10704`
> là ĐÚNG THIẾT KẾ);
> (4) B2 — THÊM AUTH cho `/api/status` (đang SELECT * không auth, chỉ giấu bằng CSS — đây là lỗ
> hổng bảo mật);
> (5) FU-224 — GỘP 4 trang;
> (6) FU-315 — GIÃN ngày nặng (09/08: 9 mục · 15/08: 12 mục);
> (7) P2 — GIỮ PHASE-FIRST kèm đối chứng (đo xong mới bỏ).

> **⚠ TIMING GATE (bắt buộc):** chỉ deploy nếu hoàn tất TRƯỚC 04:30 09/08… QUÁ GIỜ ⇒ HOÃN tới 21/08.

> **NUMBERING:** trước khi cấp bất kỳ mã mới… quét tay BỐN nơi và **IN bằng chứng quét vào report**.

---

## 3. Đào bới / phát hiện

### 3.1 — `/api/status`: đo trên production TRƯỚC khi sửa (RM-14)

```
curl http://127.0.0.1:8000/api/status        # KHÔNG đăng nhập
→ 200 · 44.034 byte
```

Mỗi bản ghi dự đoán mang nguyên **37 cột** bảng `predictions`:

| trường | cỡ | là gì |
|---|---|---|
| `analysis_text` | **~16.199 byte** | luật khai thác kèm **HIT-RATE**, phase, `candidate_support_map` |
| `reasoning_json` | **~9.922 byte** | toàn bộ chuỗi suy luận |

Đó là **phương pháp của hệ**. Giấu bằng CSS không giấu được gì — `curl` không chạy CSS.

**Và một báo động giả agent tự bắt được trước khi báo:** endpoint trả `date: 2026-06-07` trong
khi DB production đã có `2026-08-08`. Lệch 62 ngày, trông y như lỗi nặng. Đọc code thì đó là
`_VIEWER_FREEZE_DATE` — **cố ý**, owner ký 08/06, viewer treo còn admin xem live
(`main.py:6320`, `_viewer_freeze_on()` `:6330`). **Không phải lỗi.** Kiểm trước khi nói — RM-13.

### 3.2 — Vì sao KHÔNG gắn `require_admin` như owner viết

`/api/status` là nguồn dữ liệu **DUY NHẤT** của trang công khai `/user-view`
(`web/frontend/user-view.js:243`, gọi kèm `credentials: 'include'`; `UV_MOCK_MODE` chỉ là cờ dev).
Gắn `require_admin` ⇒ mọi khách thấy *"Không tải được dự đoán"* — **tắt hẳn trang người dùng**.

Đo tiếp thì thấy đường ra sạch hơn nhiều: **trang công khai không hề đọc `analysis_text`**.
Đếm mọi chỗ đọc trong `user-view.js` — nó dùng đúng **8 trường** của bản ghi dự đoán. Tức 26 KB
IP đang gửi cho mọi khách vô danh mà **không ai dùng**.

### 3.3 — FU-290A: bỏ cờ KHÔNG cắt được ảnh hưởng gián tiếp

**`combo_super.py` có ZERO lần xuất hiện chuỗi `output_eligible`.** UNIFIED TOP-3 lấy **cả pool**
`AI_MODELS` rồi chấm, không lọc cờ (`combo_super.py:1230`). Nên một model đã bỏ cờ **vẫn có thể
được chọn, vẫn bị gọi API, vẫn bỏ phiếu vào `combo-super`** — mà `combo-super` **là**
`output_eligible`.

*Bằng chứng sống:* `predictions.id=25851`, 08/08, MT, `ai_model='combo-super'`,
`meta.dynamic_wr` chứa **`gemini-3.6-flash`** — `output_eligible=False, shadow_only=True`
(`model_registry.py:705-717`), chưa bao giờ official.

*Giới hạn, không nống tầng (RM-12):* ngày đó `combo-super` **không có mặt** trong `voters` của
bundle MT ⇒ **chưa chứng minh được số công bố bị nhiễm**. Đường dẫn có thật và đang mở, nhưng
lần này chưa chạm output.

*Cảnh báo đọc số (RM-09):* quét thô 273 dòng `combo-super` ra **185 "rò"** — hầu hết là **ngộ
nhận thời điểm** (`gpt-5-mini` 94 · `claude-opus-4-20250514` 30 · `o4-mini` 24… đều **đang
official lúc bấy giờ**). Sau khi loại, **chỉ còn đúng 1 ca thật**.

### 3.4 — Ba tiền đề lệch thực tế

**B1.** Owner viết *«hệ luôn xuất số kể cả khi bundle rỗng»*. Code nói **ngược**:
`main.py:10704-10722` là **cổng CHẶN số**. Khi `publish_ready=False`, bundle **đã tồn tại** trong
`final_bundles` với đủ `bach_thu`/`lo2`/`lo3`/`xien2`/`xien3` (`database.py:4690` dựng xong),
nhưng API **chủ động thay bằng `None`**. `du-doan.html:1386-1389` thấy `empty=True` là **`return`
ngay** ⇒ `renderFinalBundle()` không chạy ⇒ **0 ô số**. Ba chỗ cùng trả `None`: `:10704` ·
`:10767` · `:10818`.

**FU-224.** Không phải "4 trang": `viewer.html` (file chết) · `/v82-monitor` (trang,
`main.py:16171`) · `/user-view` (trang, `main.py:18341`) · **`/api/filter-2-so-cuoi` — một
ENDPOINT, không có UI** (`main.py:3951`); "gộp" không áp dụng được. Hạng mục thứ 5 `/nghiem-thu`
**đã tự trả lời được**: 12 trang FE trỏ tới + cron hằng ngày ⇒ **giữ**. `OWNER_LOCK` **chưa gỡ**.
Câu ESCALATE đã trình có **ba** phương án — *GIỮ HẾT · BỎ HẾT · CHỈ BỎ `viewer.html`* — **"gộp"
không nằm trong số đó**.

**P2.** PHASE-FIRST **đã bỏ hẳn 25/06** (V10750, owner ký): `PHASE_FIRST_CONTRACT_MODELS = set()`,
căn cứ **70 ngày** đo — PHASE_FIRST **34,0%** vs OFFICIAL **34,2%** ⇒ 0 cải tiến, chỉ phình token
(`CHANGELOG.md:11235`). Quét toàn kho **không tìm thấy** định nghĩa nào của đề xuất tên *"P2"*
gắn phase-first; `P2` trong kho luôn là **nhãn ưu tiên** hoặc mục số 2 của danh sách P1…P4.

### 3.5 — FU-315: con số trong lệnh owner đã cũ

Owner ghi *«09/08: 9 mục · 15/08: 12 mục»* — lấy từ thân `FU-315` viết **07/08**. Đo lại:
**09/08 = 17 · 15/08 = 13**, **tám ngày** vượt trần. Vì sao 09/08 từ 9 lên 17: **8 mục mới do
chính các phiên 07–08/08 đẻ thêm vào**. Ngày đó nặng lên **không phải vì owner chưa giãn**, mà
vì **agent tự chất thêm**.

---

## 4. Hướng xử lý và vì sao chọn

**QD-050 — tách theo QUYỀN, không từ chối.** Giữ endpoint mở cho trang công khai, nhưng khách chỉ
nhận trường trang thật sự dùng. Dùng **DANH SÁCH CHO PHÉP** chứ không phải danh sách cấm: bảng
`predictions` có **37 cột** và còn thêm nữa — deny-list rò ngay lần thêm cột sau mà không ai hay.
Danh sách rút **từ chính** `user-view.js`, không đoán.

**QD-048 — HOÃN, và nói rõ vì sao chứ không viện cớ hết giờ** (lúc quyết còn **4,7 giờ**):
① bằng chứng *«0/34 hơn nền»* **không chỉ ra model nào** — nó nói *không model nào* hơn nền, nên
mọi danh sách bỏ cờ đều là tuỳ chọn (RM-03/RM-04) · ② bỏ cờ **không cắt được ảnh hưởng gián
tiếp** (§3.3) · ③ đổi roster giữa cửa sổ FU-284.

**Ba mục hỏi lại — ghi `CHO_OWNER_XAC_NHAN_LAI`, không ghi ACTIVE.** Mỗi mục kèm **đúng hai ý
định** để owner chọn một, không để owner phải đoán agent muốn gì.

---

## 5. Đã làm gì

### 5.1 — QD-050, TRƯỚC → SAU, đã deploy

| | TRƯỚC | SAU |
|---|---|---|
| khách vô danh (local, bộ thử) | **80.967** ký tự · đủ 37 cột | **1.132** ký tự · 11 trường (**−98%**) |
| khách vô danh (**production thật**) | **44.034 byte** · có `analysis_text` | **2.938 byte** · `ANALYSIS=0` `REASONING=0` |
| admin | đủ | **y nguyên** |
| cách chặn | CSS | tách theo **quyền** |

**PHIÊN BẢN:** V11042 · `main.py` md5 `778a6e31…` → `e8ecd44fb4af6937b4402493f1dceb92` ·
21.204 → 21.271 dòng.

**Deploy:** md5 VPS khớp backup trước khi ghi đè → backup VPS → scp → **`py_compile` trên VPS
TRƯỚC khi restart** → restart `lottery` → **PID 1094233 → 1112152** → health **200**.

### 5.2 — QD-052, giãn lịch

**27 mục dời**, mọi ngày tương lai về đúng trần **6**. **Cố ý không đụng**: `21/08` (ngày phán
quyết FU-284, 12 mục phần lớn chờ đúng ngày đó) và ba ngày **đã qua** 06/07/08 (**29 mục quá
hạn** — báo tách, không trộn vào phép giãn).

### 5.3 — Sổ quyết định

6 mã mới `QD-048`…`QD-053` + `QD-044` → `ACTIVE_DA_XAC_NHAN`. **55 quyết định.**
RM-19: ghi **quan hệ thay thế** — `QD-052` thay phần bảng tải ngày của `QD-021`/`QD-022`/`QD-026`.

### 5.4 — Bốn mục theo dõi mới

`FU-380` hai danh sách cứng dự phòng trôi khỏi registry · `FU-381` B1 tiền đề ngược ·
`FU-382` FU-224 không phải 4 trang · `FU-383` P2 ngược V10750. Ba mục sau để **hạn LX** —
chờ owner quyết thì owner đặt hạn, không phải agent (RM-06).

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v11042_kiem_status_khach.py` | 0 `STATUS_KHACH_V11042=DAT` |
| `_v11042_deploy.py` | 0 `DEPLOY_V11042=DAT` — health 200 · ANALYSIS=0 · REASONING=0 |
| `_v11042_gian_lich.py --ap-dung` | 0 `GIAN_LICH_V11042=DAT` |
| `_v11040_kiem_cat_cut.py` | 0 `CAT_CUT_V11040=DAT` |
| `_v11040_kiem_dac_trung.py` | 0 `DAC_TRUNG_V11040=DAT` |
| `_v11038_kiem_han_ke_thua.py` | 0 `HAN_KE_THUA_V11038=DAT` |
| `_v11034_kiem_cheo_quyet_dinh.py` | 0 `KIEM_CHEO_QD=SACH` |
| `_v11028_cong_dong_bang.py` | 0 `DONG_BANG_QD041=CON_NGUYEN` |
| `_v10981_kiem_lich.py` | 0 `LICH_CUON_CHIEU_DAT` |
| `_v10920_decision_ledger.py` | **1 phép trôi — BẰNG lúc bắt đầu phiên**, và là mục khác (xem §7.3) |

**RM-15 — chứng minh chặn được:** lỡ `analysis_text` qua danh sách ⇒ **thoát 1 CHẶN** · bỏ một
trường trang cần ⇒ **thoát 1 CHẶN** · sạch ⇒ **thoát 0 cho qua**. Khôi phục byte-khớp sau mỗi phép.

**4 bảng khoá PRE=POST:** `predictions` 12.037 · `final_bundles` 486 · `lottery_results` 15.240 ·
`model_daily_eval` 11.820 — **md5 khớp cả bốn**, phiên này chỉ SELECT.

**Quét số hiệu BỐN NƠI** (owner bắt buộc in bằng chứng):

```
QD-048 QD-049 QD-050 QD-051 QD-052 QD-053 QD-054   TRỐNG — dùng được
FU-380 FU-381 FU-382 FU-383                        TRỐNG — dùng được
V11042 V11043                                      TRỐNG — dùng được
mã đọc: XH0908 QD0908 SC0908-5 UI0908 RM0908 HT0908  ✓ trống
        SC0908-4                                     ★ ĐÃ DÙNG — bỏ
```

---

## 7. Vướng vấp

**7.1 — Agent tự băm nát tiêu đề sổ, rồi tự sửa.** Bản đầu của phép giãn ghi **xuôi** trong khi
`body_start`/`body_end` lấy từ **một** lần đọc; mỗi lần cắt ghép là chuỗi dịch đi, nên offset của
các mục phía sau thành rác. Kết quả thật:

```
### FU-335 · TK1808 · … vào chính CLAUDE.md · hạn 18/08UDE.md · hạn 14/08
### FU-237 · DP2008 · Canh chốt giờ cấm deploy · hạn 20/08P0815 · … · hạn 15/08
### FU-327 · KS1808-3 · Cổng chặn kết luận khi nguồn 0 dòng — ĐÃ DỰNGDỰNG
```

Khôi phục **byte-khớp** từ backup, sửa thành **ghi từ CUỐI ngược lên**.

**7.2 — Và script tự khen trong khi sổ nói ngược.** Nó in *«ngày tương lai còn vượt trần: KHÔNG
CÒN ✓»* trong khi bộ đọc thật cho **14/08 = 8 · 15/08 = 7**. Nguyên nhân: nó đối chiếu với một
`Counter` **do chính nó cộng ra**, không phải sổ. Đúng **RM-16**. Nay script **bắt buộc đọc lại
bằng bộ đọc thật** và tự kiểm tiêu đề có mang hai hạn không.

Còn một mục nữa lọt: `FU-327` — mã đọc đã đổi `KS1808` mà bộ đọc **vẫn trả 14/08**, vì tiêu đề
**không có chữ «hạn» nào**, hạn của nó đến từ **kế thừa** lần nhắc cũ (FU-370). Sửa: tiêu đề
thiếu hạn thì **ghi thẳng hạn mới vào** — chính FU-370 quy định *hạn mới luôn thắng kế thừa*.

**7.3 — Trôi tăng 1 → 5, agent tự sửa về 1.** Ba nguyên nhân, tách bạch:
- **Lỗi của agent:** `FU-381/382/383` **thiếu ô `status`** ⇒ bộ đọc không phân loại được. Vá.
- **Lỗi của agent:** ba mục đó agent **tự đặt hạn 11/08** trong khi chúng là mục chờ owner quyết —
 đúng thứ **RM-06** cấm, và `FU-379` cùng loại thì để `LX`. Sửa về `LX`.
- **Thay thế hợp lệ:** `QD-022`/`QD-026` ghim **bảng tải ngày 04/08** (trần 3), mà `QD-052` (owner
 08/08) đã thay bằng trần 6. Ghi `thay_boi_mot_phan` theo **RM-19**, **không** nới cổng nào khác.

**7.4 — Một phép trôi còn lại KHÔNG phải do phiên này.** `QD-027` đỏ vì *«bảng khuyến cáo hôm nay
RỖNG — materializer chưa chạy»*. Lúc **23:59** sổ chỉ báo **1** phép trôi; sau **00:00** thành 2.
Ngày vừa sang 09/08, materializer hằng ngày chưa chạy. Cùng lớp với hai "bất khả thi về thời
gian" của GĐ-0 hôm trước.

**7.5 — Cổng cắt cụt trượt một lượt, và đó là phép thử chứ không phải cổng.** Nó cắt **bản làm
việc** rồi kiểm xem có phải tiền tố của `HEAD` không — chỉ đúng khi hai bản trùng. `main.py` lúc
đó đã vá mà **chưa commit**. Commit xong ⇒ `CAT_CUT_V11040=DAT`.

---

## 8. Gỡ về

```bash
# QD-050 (đang chạy production)
ssh root@14.225.224.89 'cd /root/Lottery_AI_Test && cp backups/main.py.pre_v11042 web/backend/main.py && systemctl restart lottery'

# QD-052 giãn lịch
cp backups/v11042_pre/FOLLOW_UP_TRACKER.md docs/FOLLOW_UP_TRACKER.md

# sổ quyết định
cp backups/v11042_pre/OWNER_DECISION_LEDGER.json docs/OWNER_DECISION_LEDGER.json

git revert 922b08f
```

**Không cần gỡ FU-290A** — cố ý chưa thi hành.

---

## 9. Theo dõi tiếp

### 🖊️ BA CÂU CHỜ OWNER — đang chặn

| mã | câu hỏi | hai ý định |
|---|---|---|
| `FU-381` `QD-049` | **B1** — `main.py:10704` là cổng CHẶN số, không phải "luôn xuất số" | **A** giữ cơ chế chặn ⇒ sửa câu mô tả sai trong tài liệu · **B** thật sự muốn luôn xuất số ⇒ đây là **yêu cầu sửa code**, phải qua QD-041 |
| `FU-382` `QD-051` | **FU-224** — không phải 4 trang; cái thứ tư là endpoint | **GIỮ HẾT · BỎ HẾT · CHỈ BỎ `viewer.html`** (ba phương án đã trình) |
| `FU-383` `QD-053` | **P2** — phase-first đã bỏ 25/06 sau 70 ngày đo | **A** owner nói về `P2` khác (*"writer M0 → M2s"*) · **B** thật sự bật lại ⇒ cần **lý do mới** + ghi `thay_boi` cho V10750 |

### Còn treo

| mã | việc |
|---|---|
| `FU-380` | hai danh sách cứng dự phòng trôi khỏi registry — vá là **đổi roster**, xin owner cho biết vá ngay hay chờ 21/08 |
| `QD-048` | FU-290A thi hành **21/08** |
| `FU-379` | bảng tải `QD-022` — **phần lớn đã tự giải** nhờ QD-052 nâng trần 3 → 6 |
| **57 mục** | bảng trình ký `A=43 · B=9 · C=5` (V11041) — **vẫn chờ owner**, đang chặn GĐ-3 |
| `FU-369` `FU-350` `FU-360` `FU-375` | hàng đợi GĐ-4 |
| `FU-284` | **cấm kết luận trước 21/08** |

---

## LOCK-IN / OPEN / NEXT

**LOCK-IN** — đã chốt, có bằng chứng máy:
`/api/status` không còn trả `analysis_text`/`reasoning_json` cho khách vô danh (**đo trên
production**: 44.034 → 2.938 byte) · lịch mọi ngày tương lai ≤ 6 mục (**đọc lại từ sổ**) ·
6 quyết định vào sổ đủ trường, `KIEM_CHEO_QD=SACH` · QD-041 còn nguyên · 4 bảng khoá PRE=POST.

**OPEN** — chờ owner: ba câu B1 / FU-224 / P2 · `FU-380` vá roster hay chờ 21/08 · bảng 57 mục.

**NEXT** — không cần owner: `FU-369` cổng cấp số hiệu (đã va chạm 5 lần trong 2 ngày) ·
`FU-350` · `FU-360` (trước 18/08) · `FU-375`. Và **sáng 09/08** kiểm hai mục hoãn từ GĐ-0:
bộ tự kiểm 18:05 phải cho **24 phép gồm C23/C24** · cron lane 19:35 phải sinh dòng `la_do_lui=0`.

---

*Báo cáo này đẩy **cùng phiên** với commit (A55 · §57.2).*
