# REPORT V11109 — AUDIT LẦN 2 (READ-ONLY) · 23/08/2026 khuya

> **Phiên READ-ONLY theo lệnh owner.** Ngoại lệ duy nhất: **gỡ `gpt_analyzer.py` về `V11106`**
> (`CTX-18.6` · `RR-16.5`) — owner ký trực tiếp trong phiên. **Không deploy đợt 2.**
>
> **Tám tác nhân đọc-only trên VPS:** 1,56 triệu token · 434 lượt gọi công cụ · 0 lỗi.
> Sáu làn đo + **hai làn phản biện**; phản biện bác **12 kết luận**, gồm **một câu vừa báo owner**.
>
> **VPS sau phiên:** `RR-16.5` · `CTX-18.6` · PID `2341779` · `/api/health=200` · 4 bảng khoá `+0`.

---

## 1 · TÓM TẮT — sáu điều owner cần biết trước

| # | điều | số |
|---|---|---|
| 1 | 🔴 **Nền đang LỖ** — mọi phép «model vs nền» đều so với một cái nền lỗ | **−90,3tr / 60 ngày** |
| 2 | 🔴 **`FU-183` tự nổ 31/08, ngưỡng có HAI cách đọc ngược nhau** | `+14,7tr` ⇒ GIỮ · `−16,7tr` ⇒ TẮT |
| 3 | 🔴 **Không có cron nào thi hành `FU-183`** | `crontab \| grep -ci` = **0** |
| 4 | **Không model nào đạt ngưỡng**, cửa sổ nào cũng vậy | cao nhất **+4,27đ** / ngưỡng **±10đ** |
| 5 | **Không đề xuất thay model nào** — 0% lượt rỗng do «model kém» | **78,9% do provider** |
| 6 | 🔴 **Ba con số em đếm sai trong một ngày** | 10→**1** · 3,2%→**bốn cửa sổ** · 302→**418** |

---

## 2 · OWNER YÊU CẦU GÌ (NGUYÊN VĂN)

> *«PROMPT TỔNG LỰC LẦN 30 — 23/08 TỐI (CHẠY NGAY): AUDIT CỰC GẮT»* · *«PHẦN AUDIT READ-ONLY
> LÀM NGAY»* · *«CẤM deploy đợt 2 trong phiên này (chờ ngày sạch CTX-18.6)»* · *«đo hoài không
> ra»* — mọi phép đo phải có **ngày quyết định** và **verdict**.

Và trong phiên owner ký thêm một quyết định: **«Gỡ về CTX-18.6 ngay»** — sau khi em báo bản
`RR-16.6` em đã đẩy lúc 21:1x (**trước** khi nhận lệnh READ-ONLY) làm 24/08 **không còn là ngày
sạch của `CTX-18.6`** như owner lên kế hoạch.

---

## 3 · ĐÀO BỚI / PHÁT HIỆN


Tám tác nhân đọc-only trên VPS (**1,56 triệu token · 434 lượt gọi · 0 lỗi**): sáu làn đo, **hai
làn phản biện**. Phản biện bác **12 kết luận**, trong đó **một câu em vừa báo owner giờ trước**.

### 🔴 ĐIỀU NẶNG NHẤT — mọi phép so «model vs nền» đều so với một cái nền ĐANG LỖ

`_v10918_override_watch.compute_view(60 ngày)` trên DB production:

| miền | lãi THỰC TẾ | lãi nếu đi theo phiếu bầu | chênh |
|---|---:|---:|---:|
| MN | **−30,7tr** | −69,9tr | **+39,2tr** |
| MT | **−26,3tr** | −6,7tr | −19,6tr |
| MB | **−33,4tr** | −4,0tr | −29,4tr |
| **TỔNG** | **−90,3tr** | −80,5tr | −9,8tr |

Sáu phiên vừa qua kết luận *«không model nào hơn nền 10 điểm»* — **đúng, nhưng bản thân cái nền
đang lỗ 90,3tr / 60 ngày**. Không phép đo nào của sáu phiên phát hiện được điều đó **vì tất cả
đều là trúng/trật, không phải tiền**.

### 🔴 `FU-183` tự nổ **31/08** — ngưỡng có HAI CÁCH ĐỌC NGƯỢC NHAU, và KHÔNG có gì thi hành nó

Sổ ghi *«nếu tới **31/08** lớp MN **âm tiền** → đặt `OVERRIDE_CONFIG['MN']['enabled'] = False`.
**Không hỏi lại owner**»* (`FOLLOW_UP_TRACKER.md:6312`).

| nguồn | công thức | giá trị | verdict |
|---|---|---:|---|
| **mã** `_v10918_override_watch.py:183` | `chenh_tr < 0` — **chênh** so với đi theo phiếu | **+14,7tr** | **GIỮ** |
| **sổ** — đọc nghĩa đen *«MN âm tiền»* | lãi **tuyệt đối** | **−16,7tr** | **TẮT** |

Cùng một câu, hai kết luận ngược nhau, nổ sau **8 ngày**, và văn bản ghi **không hỏi lại owner**.

**Và không có gì thi hành nó:** `crontab -l | grep -ci 'v10918|override'` = **0**. Ba chỗ trong
mã nhắc `enabled=False` đều **không phải mã thi hành** — một dòng tài liệu
(`_v10917_governance.py:136`), một **chuỗi bên trong thông điệp** (`_v10918:186`), một chỗ chỉ
**đọc** (`_v10926_status_now.py:61`). Nó **chờ một người mở `/monitoring` ngày 31/08 và đọc chữ**.

Thêm: nhánh **GIỮ** không xét `p` — hiện `p = 0,375` (4 cứu / 1 phá). Chính `FU-183` từng loại
bằng chứng cũ vì `p = 0,754` chưa đạt.

### 🔴 BA CON SỐ EM ĐẾM SAI TRONG MỘT NGÀY — cùng một nguyên nhân

| # | em báo | ĐÚNG là | vì sao sai |
|---|---|---|---|
| 1 | *«10 mệnh lệnh mồ côi»* | **1** | cổng chỉ dump context pack, bỏ thân prompt; và nuốt cả giá trị mẫu trong khung JSON |
| 2 | *«chặn 3,2%»* | **4,4 / 3,2 / 28,2 / 63,9%** theo 4 cửa sổ | trích **một** cửa sổ — cổng `PRJ_WINDOW_NOT_SPLIT` chặn commit, và **nó đúng** |
| 3 | *«302 mã FU · 19 thiếu hạn»* | **418 mã · 95 thiếu hạn** | bộ đếm dùng `^###` nên **bỏ sót 118 mã** nằm ở khối **THỤT LỀ** |

Cả ba: **chạy một phép khớp mẫu, thấy con số kêu, tin nó.** Bộ đếm đã vá; sổ đã sinh lại.

**Còn khuất chưa gộp:** `docs/archive/FOLLOW_UP_TRACKER_LICH_SU.md` giữ **366 mã ngoài chuẩn
`§58`** (dạng `FU-V10812-…`), trong đó **13 mục ghi thẳng `owner_ack: Chưa`**. Một trong 13 là
`FU-V10812-GEMINI25-EOL` trạng thái **OPEN (RISK REGISTER)**: Google chặn `gemini-2.5-flash/pro`
với project mới, official sống nhờ **2 key project cũ** — và đo hôm nay **cả hai model vẫn đang
chạy**. Và **15.155 ký tự** cuối tệp nằm trong một khối mã ` ``` ` **mở mà không đóng**.

### `GĐ-1` — bảng xếp hạng, đã hiệu chỉnh đúng: **KHÔNG model nào đạt ngưỡng, cửa sổ nào cũng vậy**

12/15 model **đã đủ mẫu** (`n` 375–384 vs `n_cần` 180–268 sau hiệu chỉnh `DEFF`). Điểm cao nhất
**+4,27 điểm** (`deepseek-reasoner`), thấp nhất **−2,08** (`lstm`) — ngưỡng là **±10 điểm**.
Ba model chưa đủ mẫu: `claude-opus-4-6` 204/234 · `glm-5.1` 65/198 · `gpt-oss-120b` 68/225.
Cột **THĂNG** đếm từ 22/08 mới có **2 ngày** ⇒ **chưa được phép kết luận**, còn thiếu 54–84 ngày.
**Tới 27/08 KHÔNG model nào quyết được gì.**

**Biên chế độ nền có BA mốc, không phải hai.** `git log --diff-filter=A` cho
`_v10640_official_perslice_override.py` → **30/05/2026**. Trước ngày đó **không tồn tại lớp ghi
đè nào**:

| | R0 18/04–31/05 | R1 01/06–31/07 | R2 01/08–23/08 |
|---|---|---|---|
| lớp ghi đè | **không có** | 3 miền | chỉ MN |
| điểm (gộp 15 model) | +0,0095 | **+0,0365** | **−0,0303** |
| `z` sau `DEFF` riêng | +0,31 | +1,39 | −0,45 |
| **`DEFF` đo riêng** | 4,61 | 5,26 | **12,64** |

`DEFF` **đổi theo cửa sổ trong cùng một loại lát cắt** — bằng chứng cứng cho `RM-21`.

### 🔴 RÚT LẠI — *«0/384 ô có đồng thời b>0 và c>0 ⇒ 15 model luôn cùng dấu»*

Câu này em báo owner giờ trước. **Nó là TAUTOLOGY của mã, không phải phát hiện thực nghiệm.**
`_materialize_shadow_promotion_scorecard.py:275`:

```python
baseline_hit = bool(baseline and baseline["bach_thu_status"] == "WIN")   # MỘT giá trị / ô
would_flip_win  = int((not baseline_hit) and main_hit)     # b
would_flip_lose = int(baseline_hit and not main_hit)       # c
```

Nền THẮNG ⇒ `b = 0` cho **mọi** model trong ô; nền THUA ⇒ `c = 0` cho **mọi** model. `0/384` là
**hệ quả bắt buộc của định nghĩa**.

**`DEFF ≈ 6,8` vẫn đứng** — nó đo bằng sandwich + bootstrap, độc lập với câu chuyện đó. Nhưng
**cách giải thích thì sai**, và bản đúng còn đáng lo hơn: **cụm nằm sẵn trong ĐỊNH NGHĨA của
thước**, không phải hiện tượng quan sát được.

### `GĐ-3` — lượt rỗng: **KHÔNG đề xuất thay model nào**

76/76 lượt rỗng 60 ngày **đều truy được nguyên nhân**: **78,9% PROVIDER lỗi** · 5,3% lỗi phía
ta · 13,2% sai định dạng · **0% «model kém»**. Sau hiệu chỉnh bội (Bonferroni 36 model) **chỉ
`gemma-4-31b` khác nền — và nó đã RETIRED từ 29/07**.

Ba việc **SỬA** có bằng chứng cứng: trần token `deepseek-reasoner` (lượt thành công đã chạm
**31.391/32.768 = 95,8%**) · bộ rút số **bỏ sót câu trả lời đã có** (`qwen3.7-max` 13/08 nói rõ
*«50»* mà `numbers={}`) · `database is locked` khi ghi shadow (2 ca).

**Rút lại:** con số *«tỉ lệ rỗng 2,26%»* ghi trong `FU-426` là tỉ lệ **riêng của `glm-5.1`**,
không phải của hệ (hệ **1,58%**; 15 model OUTPUT trên lane chính thức **0,39%**).

### `GĐ-2` — shadow: hai họ là hai TẬP MODEL khác nhau, và **gốc bệnh đã tìm ra**

`parse_ok=1`: OUTPUT **15** model · SHADOW_AUTO **21** model · **giao nhau = 0**.
*«9 model có mặt ở cả hai họ»* là **ẢO** — 100% là dòng giữ chỗ `parse_ok=0`.

**Gốc bệnh:** `_materialize_shadow_promotion_scorecard.py:428` **ghi cứng chuỗi `"SHADOW_AUTO"`**
vào trường `family` của câu `INSERT`, trong khi `:392-393` đã dựng đúng `ho` ⇒ **mọi model OUTPUT
vắng mặt đều bị dán nhãn SHADOW_AUTO**.

⇒ So hai họ là **so MODEL, không phải so REGIME**. Về thiết kế nó **không bao giờ** tách được
«do lane» khỏi «do model».

**Rút lại bằng chứng *«contract_required chênh 27 lần»* của phiên trước:** số tái lập đúng
(1,36% vs 38,10%) nhưng nó **không phải hành vi** — trường đó là **nhãn thành viên của một
cohort ĐÓNG BĂNG** (`PFG-20260505-E`, `end_at=None` từ 05/05). Chỗ thi hành thật là
`gpt_analyzer.py:6393`, mà `:953 PHASE_FIRST_CONTRACT_MODELS = set()` ⇒ **hợp đồng chưa bao giờ
được bơm**.

### ĐỢT 2 — **bảy khối có tên đích danh**, và trục «dịch» bị mô tả sai

`docs/BAN_DO_NGU_CANH_PROMPT_20260821.md:913` (§3.4) liệt kê đủ bảy: **MINED RULES · EVIDENCE
TABLE · NGUYÊN TẮC · MB HARD MODE (18a) · MB CALIBRATION (18c) · WEEKDAY SCAN · OWNER ANTI-TRAP**.
Dump production 23/08: bảy khối = **5.194 / 6.080 / 7.876 ký tự** = **10,4% / 11,8% / 14,1%**
prompt tổng, tức **50–56% gói ngữ cảnh**.

> 🔴 **LẬT KHUNG:** **6/7 khối KHÔNG chứa một đuôi số nào.** Trục *«nhồi số → kể ngữ cảnh»* mô
> tả **sai** việc phải làm. Khối chứa **nhiều đuôi số nhất cả gói** (`BỐI CẢNH SOI CẦU`, 12–14
> đuôi) lại được xếp **GIỮ** — vì nó **KỂ**. Trục thật là **ngôn ngữ BẢNG TÍNH → ngôn ngữ KỂ
> CHUYỆN**, và `BỐI CẢNH SOI CẦU` chính là **bản mẫu đã có sẵn trong kho**.

Bốn lỗi mới, mỗi lỗi đủ làm hỏng một đợt dịch làm theo tài liệu: họ SKIP có **5 chỗ trong mã**
(tài liệu ghi 2; hai chỗ nằm trong `MB_EXPERT_DOCTRINE` `gpt_analyzer.py:4077 · :4081`) ·
**ba trần tự tin khác nhau trong cùng prompt MB**: **55% (`:4077`) · 60% (`:5324`) · 55%
(`:5419`)** ⇒ `PRJ_PROMPT_CONTRADICTS`.

### `QD-045` — owner **KHÔNG nhớ nhầm mã**

`QD-045` nguyên văn chỉ nói dời `QD-015/016/017`. Nhưng có một dòng thật nối nó với sổ theo dõi:
`docs/DUYET_GOP_2208.md:464` — *«sổ theo dõi | sửa hạn FU-216 FU-231 FU-226 về 21/08 | QD-045
dời lịch mà sổ chưa dời»*. Đo hôm nay: **cả ba vẫn mang hạn cũ** 09/08 · 10/08 · 10/08.

Quyết định **thực sự** về dọn sổ là **`QD-054`** (09/08). Nhưng **`QD-066`** (12/08) phủ lên:
*«việc dọn sổ/phân loại/kế toán quản trị thì **ĐỂ LÂU CHO RÕ, cấm clear vội**»*, và **`QD-071`**
(21/08) ràng thêm *«**CẤM đóng hàng loạt mù**»*. ⇒ **Không dọn trong phiên này là ĐÚNG LUẬT.**

### Ba lớp, không phải hai — và hai lớp owner duyệt đang kéo NGƯỢC NHAU

`PP1 dampener` → `ranked[0]` → lớp ghi đè `V10640`. **`ranked[0]` tự nó đã bị `PP1` sửa.**

Ca sống **23/08 MN**: `PP1` dìm `73` từ `score 0,1477` xuống `0,1256` (3 phiếu bầy đàn:
`deepseek-reasoner` · `gemini-2.5-pro` · `glm-5.1`) ⇒ `46` thành `ranked[0]`; rồi lớp ghi đè MN
**chọn lại `73`**. Số công bố cuối: **`73`**.

`PP1` nổ ở **138/384 bundle (35,9%)**, **đổi top-1 ở 14/384** (MB 7 · MN 7 · MT 0). Trong 14 lần
đó, số công bố cuối cùng **bằng đúng con số `PP1` vừa dìm ở 9/14 lần**.

**Và `PP5 family bonus` CHƯA BAO GIỜ CHẠY** — `ENABLE_FAMILY_BONUS = False` ghi cứng, ngay phía
trên là chú thích *«Policy E bake-off on 174 closed region-days: BT 43.7% vs baseline 42.5%
(+1.2pp)… MB 39.7% vs 36.2% (+3.5pp)»*. Một cải tiến **có bằng chứng** đang **TẮT**, không mục
theo dõi nào nêu.

### `combo-super` kéo model NGOÀI roster 15 vào bộ số công bố

Quét 384 lượt `combo-super`, đọc được top-3 ở 179 lượt: **64 lượt (35,8%) có ít nhất một model
NGOÀI 15 model OUTPUT** — `gpt-5-mini` 54 · `claude-opus-4-20250514` 6 · `gemini-3.5-flash` 3 ·
`gemini-3.6-flash` 1. Còn sống trong tháng 8, gồm **23/08 MN** dùng `gemini-3.5-flash` — **chính
model được đem chấm như ứng viên shadow** ⇒ phép so cặp cho model đó **không độc lập** trên
những ngày ấy.

### Khoảng trống hạ tầng đo

`shadow_model_promotion_scorecard_daily` — bảng nuôi **toàn bộ** phép đo model — **không có
endpoint trong `main.py`, không có panel trong `monitoring.html`** ⇒ đúng mã
`§52_VIOLATION_UI_MISSING`. `model_paired_scorecard_cumulative` **không cron, và chỉ có ĐÚNG
MỘT tệp nhắc tới nó — chính tệp GHI nó**. Đồng hồ đếm mẫu THĂNG owner ký 21/08 vừa **không có
cron** vừa **không có người đọc**.

**Mã đang chạy trên VPS không gắn được với commit nào:** `git log -1` → `68f0ea6` (15/06), trong
khi `main.py` mtime **23/08 20:10** và `git status --porcelain` → **362 dòng bẩn**. Khi nói *«đo
trên hàm ĐANG SERVE»* thì chỉ neo được vào **mtime + PID**, **không neo được vào phiên bản mã**.

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Không đụng production, trừ việc owner ký.** Ngoại lệ duy nhất là gỡ về `CTX-18.6`, và nó
**khôi phục** trạng thái owner đã định chứ không thêm biến mới.

**Không dọn sổ theo dõi.** `QD-066` (12/08) khoá: *«việc dọn sổ… **ĐỂ LÂU CHO RÕ, cấm clear
vội**»*; `QD-071` (21/08) thêm *«**CẤM đóng hàng loạt mù**»*. Không dọn là **đúng luật**.

**Không đề xuất thay model.** Sau hiệu chỉnh bội, **0% lượt rỗng do «model kém»**. Đề xuất thay
lúc này là **hạ sàn cho hết đỏ** — owner cấm.

**Không nâng trần 300s.** Có bằng chứng nó quá chặt cho `glm-5.1` (`p90 = 339s > 300s`), nhưng
nâng trần là **đổi một biến production** trong phiên READ-ONLY, và cần **ngưỡng đo trước/sau**.

---

## 5 · ĐÃ LÀM GÌ

| # | việc | bằng chứng |
|---|---|---|
| 1 | **Gỡ về `V11106`** (owner ký) | PID `2320523 → 2341779` · dump `RR-16.5` + `CTX-18.6` · 4 bảng khoá `+0` |
| 2 | Tự kiểm **9/9** bạch thủ 3 ngày × 3 miền | khớp 100% với đuôi tính lại từ `prizes_json` |
| 3 | Truy ghi đè 4 bảng khoá | `lottery_results` **0 id bị đốt** · `predictions` **1.608** |
| 4 | Đo lớp ghi đè trên **HAI** thước | bạch thủ **và** lô-2 — MN **29/29 hoà** trên lô-2 |
| 5 | Số đầu vs nền, `DEFF` đo cho **chính thước đó** | MN `−1,19` · MT `+1,28` · MB `−1,17` |
| 6 | `FU-434` · `FU-435` · `FU-436` | tất cả có **hạn + ngưỡng** |
| 7 | Vá bộ đếm sổ yêu cầu owner | **305 → 418 mã**, hiện 118 mã khuất |
| 8 | Rút lại **ba** câu đã công bố | `PRJ-RETRACTION-001`, đủ bốn phần |

---

## 6 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| `_v11062_nang_version.py --kiem` | ✓ **ĐẠT** (V11109) |
| `_v11044_cong_so_hieu.py` | ✓ `SO_HIEU_V11044=KHOP` |
| `_v10981_kiem_lich.py` | ✓ **ĐẠT 8/8** — 0 mồ côi |
| `_v10920_decision_ledger.py` | ✓ **0 TRÔI** |
| `_v11088_cong_cua_so_chon.py` | 🔴 **CHẶN COMMIT của chính em** — và **nó đúng** (§7.2) |
| 4 bảng khoá PRE→POST | ✓ `+0` |

---

## 7 · VƯỚNG VẤP

### 7.1 · Em deploy trước khi nhận lệnh READ-ONLY — và backup trên VPS đã hỏng

`RR-16.6` lên VPS lúc 21:1x. Owner ký gỡ về. **Không lượt dự đoán nào chạy trên bản đó.**

`_v11107_deploy_ctx187.py:138` chạy `cp -a … .pre_v11107` **không điều kiện ở MỌI lượt đẩy** ⇒
đẩy hai lần trong một phiên thì lượt thứ hai **chép đè** bản gốc. Backup ấy có tên, có kích
thước, `md5sum` chạy trơn — **nhìn y như một backup thật**. Nguồn khôi phục đúng là **git
`6a646d0`**. Bộ gỡ mới đặt tên backup **có dấu thời gian** và **từ chối chạy nếu tên đã tồn tại**.

### 7.2 · Cổng `PRJ_WINDOW_NOT_SPLIT` bắt lại chính em

Bản đầu của mục rút lại trong `V11108` chỉ trích **30 ngày** (`3,2%`). Cổng **chặn commit**.
Nó đúng: nhìn đủ bốn cửa sổ thì tỉ lệ chặn là **4,4 / 3,2 / 28,2 / 63,9%**, và **126 bundle
THẮNG chưa bao giờ lên trang** trong 180 ngày.

Đây là **đúng cái lỗi em phê hai làn đo suốt phiên**, và em mắc lại **ngay trong mục rút lại
một lỗi khác**.

### 7.3 · Ba con số đếm sai, cùng một nguyên nhân

Bảng ở §3. Cả ba: **chạy một phép khớp mẫu, thấy con số kêu, tin nó.**

---

## 8 · GỠ VỀ

| việc | lệnh |
|---|---|
| `gpt_analyzer.py` | `cp /root/Lottery_AI_Test/web/backend/gpt_analyzer.py.truoc_go_ve_2026-08-23_222858 /root/Lottery_AI_Test/web/backend/gpt_analyzer.py && systemctl restart lottery` |
| lớp ghi đè MN | `OVERRIDE_CONFIG["MN"]["enabled"] = False` — **một dòng** |
| bộ đếm sổ | `git checkout 53d6697 -- web/backend/_v11107_so_yeu_cau_owner.py` |

---

## 9 · THEO DÕI TIẾP

| ngày | việc | verdict nếu ngưỡng đạt |
|---|---|---|
| **24/08** | kiểm lượt 05:00 đóng dấu `CTX-18.6` ⇒ nâng `V11106` | `RUNTIME_PROVEN` |
| **24/08** | luật chống ML giả-đa-dạng (`FU-431`) | áp dụng ngay |
| **26/08** | vá `FU-429` (sổ gốc tự mâu thuẫn) + `FU-434` (đường hết giờ) | `0/N` vi phạm |
| **27/08** | `FU-435` cổng publish · `FU-436` trần 300s | **cần owner ký** |
| **30/08** | `FU-432` bản đóng băng — **trước 02:00** | đủ 12/12 tệp |
| **31/08** | 🔴 **`FU-183` TỰ NỔ** — hai cách đọc ngược nhau, **không có cron** | **cần owner phán TRƯỚC ngày đó** |
| **13/09** | ML MB `AUC < 0,50` ba lần liên tiếp | BỎ CỜ |
| **30/09** | `smart-ml` vs `random-forest` | BỎ CỜ |
| **06/11** | cadence retrain (`FU-285`) | cắt học lại hằng tuần |

**Chưa kiểm được:** bề mặt `/du-doan` với quyền **admin** (curl vô danh rơi vào nhánh viewer bị
đóng băng) · `chooser="specialist"` chọn số theo luật nào · nguyên nhân gốc 3 model ML trùng nhau
· P&L theo mô hình `_v10759_money_board` (có mức cược 0 / ½ / 1) thay vì mô hình đánh phẳng.

---

## §62 (A60) — BA LỚP NGUỒN

### `OWNER_SAID`

> *«PHẦN AUDIT READ-ONLY LÀM NGAY»* · *«CẤM deploy đợt 2 trong phiên này»* · *«đo hoài không
> ra»* · và trong phiên: **«Gỡ về CTX-18.6 ngay»**.

### `CODE_DID`

| điều | bằng chứng |
|---|---|
| gỡ về `V11106` | PID `2320523 → 2341779` · dump `RR-16.5` + `CTX-18.6` · 4 bảng khoá `+0` |
| P&L 60 ngày | `_v10918_override_watch.compute_view(60)` → tổng **−90,3tr** |
| `FU-183` không có cron | `crontab -l \| grep -ci 'v10918\|override'` → **0** |
| tautology `b`/`c` | `_materialize_shadow_promotion_scorecard.py:275` |
| 118 mã khuất | `^[ \t]+###[ \t]+FU-` → 120 khối · 118 mã **chỉ** có ở đó |
| ba lớp | `PP1` (`main.py:9924`) → `ranked[0]` → `V10640` (`main.py:10068`) |
| `PP5` chưa bao giờ chạy | `ENABLE_FAMILY_BONUS = False` ghi cứng |

### `DOC_SAID`

| nguồn | ghi gì | lệch không |
|---|---|---|
| `FOLLOW_UP_TRACKER.md:6312` | *«MN **âm tiền** → tắt. Không hỏi lại owner»* | 🔴 **MƠ HỒ** — hai cách đọc ngược nhau |
| `_v10918_override_watch.py:183` | `chenh_tr < 0` ⇒ tắt | 🔴 **LỆCH** với chữ «âm tiền» |
| `BAN_DO_NGU_CANH_PROMPT_20260821.md:913` | bảy khối đợt 2 | ✓ khớp — nhưng họ SKIP ghi **2** chỗ, mã có **5** |
| `QD-066` · `QD-071` | *«cấm clear vội»* · *«cấm đóng hàng loạt mù»* | ✓ khớp ⇒ **không dọn sổ** |

**Ba lớp lệch nhau ⇒ finding bắt buộc báo:** `FU-183` mơ hồ · họ SKIP thiếu 3 chỗ trong tài liệu
· **ba trần tự tin khác nhau** trong cùng prompt MB (55% · 60% · 55%).

---

**TanPhatAI cần làm:** ưu tiên **`FU-183` TRƯỚC 31/08** — ngưỡng *«MN âm tiền»* có hai cách đọc
cho hai kết luận **NGƯỢC NHAU** (`chenh_tr +14,7tr` ⇒ GIỮ · lãi tuyệt đối `−16,7tr` ⇒ TẮT), văn
bản ghi *«không hỏi lại owner»*, **và không có cron nào thi hành** ⇒ cần owner phán **cách đọc
nào đúng** và **ai bấm nút**; cập nhật `docs/FOLLOW_UP_TRACKER.md` cho `FU-434/435/436` và ba
mục rút lại; ghi vào sổ **P&L thật −90,3tr / 60 ngày** (mọi kết luận *«model không hơn nền»*
phải đọc kèm con số này); mở mục cho **366 mã ngoài chuẩn `§58`** trong `docs/archive/` (13 mục
`owner_ack: Chưa`, gồm `FU-V10812-GEMINI25-EOL` **OPEN — Google chặn `gemini-2.5` với project
mới**); mở mục cho `§52_VIOLATION_UI_MISSING` (`shadow_model_promotion_scorecard_daily` không
endpoint, không panel) và cho việc **mã trên VPS không gắn được với commit nào** (`git log -1`
= 15/06 trong khi `main.py` mtime 23/08, 362 dòng bẩn).
