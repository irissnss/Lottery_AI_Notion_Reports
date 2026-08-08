# REPORT V11031 — KIỂM ĐẦU NGÀY 08/08: LỖI CÂM 67 NGÀY TRONG KHỐI NGỮ CẢNH

**Ngày:** 2026-08-08 · **Loại:** audit đầu ngày · **CHỈ ĐỌC — không sửa, không deploy, không mutation DB**

29 agent song song (6 mũi soi + 22 phản biện đối kháng + 1 tổng hợp), 2,62 triệu token, 0 lỗi.

---

## 1. Tóm tắt

**Máy chạy tốt. Thước đo và cổng canh thì đang hỏng.**

| | |
|---|---|
| **Nặng nhất** | `build_context_pack(shadow_mode=True)` **vỡ hoàn toàn** — lỗi sống **67 ngày**, đã chạm đường chính thức, **không một triệu chứng nào** |
| **Nguy hiểm ngầm** | cổng đóng băng QD-041 **chưa nối vào hook `git commit`** — chỉ chạy khi gọi tay |
| **Sổ tự mâu thuẫn** | **ba** quyết định đóng băng ngược nhau cùng `ACTIVE`; lược đồ sổ **không có trường "bị thay bởi"** |
| **Về ăn thua** | 7 ngày qua **không miền nào** chứng minh được vượt nền. MN đảo **20 điểm** giữa hai tuần liền kề |
| **VPS** | khoẻ: PID 1004216, `NRestarts=0`, health 200, 83 cron, 0 lỗi 24h, 6/6 lane đã nghỉ |

---

## 2. Owner yêu cầu gì (NGUYÊN VĂN)

> Kiểm tra phân tích đánh giá nhân xét đầu ngày , đề xuất xử lý tiếp là gì

---

## 3. Đào bới / phát hiện

### 3.1 (NGHIÊM TRỌNG) `build_context_pack(shadow_mode=True)` vỡ — RUNTIME_PROVEN

**Lỗi:** cùng một biến `rules`, hai vòng lặp mở số biến khác nhau.

```
gpt_analyzer.py:4662–4676   SELECT ... 11 cột
gpt_analyzer.py:4681        for src, rank_sc, legacy_sc, tier, hr, n, hr12, hr16, hr4, comp, verdict in rules:      ← 11 ✓
gpt_analyzer.py:4761        for _r_src, _r_sc, _r_tier, _r_hr, _r_n, _r_hr12, _r_hr16, _r_hr4, _r_comp, _r_verdict in rules:   ← 10 ✗
```

⇒ `ValueError: too many values to unpack (expected 10)` mỗi khi `shadow_mode=True` **và** miền
đó có luật `READY_STRONG` cho thứ hôm đó.

**Vì sao câm suốt 67 ngày — BA lớp che nhau, mỗi lớp tự nó hợp lý:**

| # | chỗ | làm gì |
|---|---|---|
| 1 | `:5575` | `except Exception as e: return f"\n## CONTEXT PACK — Lỗi: {str(e)[:60]}\n"` — nuốt sạch |
| 2 | — | chuỗi trả về dài **đúng 64 ký tự** |
| 3 | `:6272` | cổng canh là `if _ctx_pack and len(_ctx_pack) > 50:` ⇒ **64 > 50 nên LỌT** |
| 4 | `:6284` | in `[CONTEXT_PACK] Injected 64 chars` — **log xanh cho một thất bại toàn phần** |

Cổng canh dựng ra để bắt *"không có ngữ cảnh"* bị đánh bại bởi **một chuỗi báo lỗi dài hơn 50 ký
tự**. Model nhận được đúng một dòng:

```
## CONTEXT PACK — Lỗi: too many values to unpack (expected 10)
```

thay cho **~10.000 ký tự** bảng hiệu suất model, luật đã đào, hội tụ, soi cầu — rồi vẫn được nối
`REASONING_RULEBOOK` phía sau như thường.

**Bằng chứng RUNTIME — chạy chính hàm production, ngày 08/08/2026:**

| miền | `shadow_mode=False` | `shadow_mode=True` |
|---|---|---|
| MN | 9.935 ký tự ✓ | **64 ký tự ✗ VỠ** |
| MT | 9.948 ký tự ✓ | 12.927 ký tự ✓ |
| MB | 9.610 ký tự ✓ | **64 ký tự ✗ VỠ** |

**MT không vỡ** vì thứ Bảy MT có **0 luật `READY_STRONG`** ⇒ `rules` rỗng ⇒ vòng lặp không chạy.
Đây là **kiểm chứng cơ chế**, không phải may rủi: số luật `READY_STRONG` theo miền × thứ ra
MN `T7=2` · MT `T7=0` · MB `T7=1` — đúng ba kết quả trên.

**Bằng chứng LỊCH SỬ:** `prediction_trace.jsonl`, **908 / 4.897 lượt** có `context_pack_chars`
**đúng bằng 64** — và **không một giá trị nào khác dưới 200**. Phân bố hoàn hảo, không phải trùng hợp.

| | |
|---|---|
| cửa sổ | **02/06/2026 → 08/08/2026 05:41** (sáng nay) |
| theo miền | MN 259 · MT 257 · MB 392 |
| tỉ lệ theo model | `gemma-4-31b` 46,3% · `gpt-5.5` 37,2% · `qwen3-max-thinking` 37,1% · `gpt-oss-120b` 36,6% |

**Đường CHÍNH THỨC bị dính bao nhiêu:** `_shadow_mode = lane_test_shadow_pack or (selected_model
in SHADOW_GATE_MODELS)`. Giao giữa `SHADOW_GATE_MODELS` (8 model) và 15 model official ra **đúng
một**: **`gpt-oss-120b`** ⇒ mọi lượt của nó, kể cả official, đều `shadow_mode=True`.

Khớp trace × `predictions` official: **9 / 21 lượt = 42,9%**, ngày gần nhất **08/08**.
Bảy model còn lại trong `SHADOW_GATE_MODELS` không phải official nên chỉ hỏng luồng bóng.

**CHƯA ĐƯỢC PHÉP KẾT LUẬN** thiệt hại accuracy — n = 9 lượt official (**RM-04**).
Cơ chế thì đã chứng minh xong ở tầng `RUNTIME_PROVEN`.

### 3.2 Cổng đóng băng chưa nối hook

```bash
grep -n "cong_dong_bang\|_v11028" .cursor/hooks.json .cursor/hooks/*.py   # → 0 kết quả
```

`_v11028_cong_dong_bang.py` chỉ chạy khi có người gọi tay. Một commit chạm `gpt_analyzer.py`
trước 21/08 là mất FU-284 + FU-325 + FU-331, **không gì tự chặn**.

### 3.3 Ba quyết định đóng băng ngược nhau cùng `ACTIVE`

| mã | trạng thái | nội dung |
|---|---|---|
| `QD-041` | `ACTIVE` | gia hạn đóng băng tới **21/08**, thêm `gpt_analyzer.py` |
| `QD-029` | `ACTIVE` | *"vướng mắc 2: **mở** nha em"* — MỞ đóng băng, ký 05/08 |
| `OD-20260801-D` | `ACTIVE` | đóng băng 01→08/08 |

Lược đồ sổ có **34 trường**, **không trường nào** là `thay_boi`/`superseded_by`. `QD-014` phải
mượn **trạng thái** (`SUPERSEDED_BY_QD041`) để diễn đạt quan hệ thay thế — tức máy không lần
ngược được.

Bộ kiểm sổ báo *"43 mục, không mục nào trôi, toàn 🟢"* vì nó **chỉ đối chiếu quyết định × CODE**,
**chưa bao giờ đối chiếu quyết định × QUYẾT ĐỊNH**. Đúng lỗi mà `CLAUDE.md` đã ghi về
`_v10925_rule_sync_check` — *"chỉ dò vài dấu hiệu rồi báo ĐỒNG BỘ"*.

### 3.4 Bảy ngày qua: không miền nào vượt nền

Nền = số đuôi khác nhau ra trong ngày ÷ 100, tính riêng từng ngày. Hiệu chỉnh cụm ngày `VIF = 2,92`.

| cửa sổ | MN | MT | MB |
|---|---|---|---|
| **01→07/08** (n=111) | 46,8% vs 42,8% · z **+0,51** | 27,0% vs 35,4% · z **−1,08** | 18,9% vs 23,7% · z **−0,69** |
| **25→31/07** (n=105) | 24,8% vs 41,0% · z **−1,98** | 41,9% vs 35,4% · z +0,81 | 21,9% vs 23,0% · z −0,16 |
| **01/07→07/08** (n=576) | 39,8% vs 42,6% · z −0,82 | 33,5% vs 35,4% · z −0,57 | 20,7% vs 23,4% · z −0,92 |

**MN đảo từ −16,2 điểm sang +4,1 điểm giữa hai tuần liền kề** — biên độ **20 điểm** với n≈105
mỗi tuần. Đây là **bằng chứng số cho RM-04**: n nhỏ không phải "yếu", mà **không ổn định**.

Ngày 07/08: MN **WIN** (BT=13) · MT **LOSE** (58) · MB **LOSE** (60).

### 3.5 VPS — máy khoẻ

`lottery` active · PID **1004216** · `NRestarts=0` · vào lúc **07/08 23:27:41** · health **200** ·
**83 dòng cron** sống, **0 dòng trỏ vào file đã mất** · đĩa 69% (13G trống) · **0 lỗi** journal 24h.

`OD-20260801-B` đã thực thi đủ — **6/6 lane đã nghỉ** (`_v10707` `_v10781` `_v10692` `_v10679`
`_v10680` `_v10637`, mỗi cái `cron=0`).

md5 khớp tuyệt đối local = VPS:

| tệp | md5 |
|---|---|
| `gpt_analyzer.py` | `6b28f0baa7aeceac0e9fd2b75a741a81` (đúng bản khoá QD-041) |
| `weekly_rule_miner.py` | `5cf5a285396d53e93ec520f17e8e9fdd` (bản A1) |
| `mined_rule_eval.py` | `f4ef7d8cd6926379293155a64e851afd` |

A1 deploy **07/08 23:27:29**, service vào **23:27:41** — khớp.

---

## 4. Hướng xử lý và vì sao chọn

**Chọn: KHÔNG SỬA GÌ HÔM NAY.** Ba lý do:

1. Lỗi nặng nhất nằm trong `gpt_analyzer.py` — **đang bị QD-041 khoá md5 tới 21/08**. Vá là
   phá chính cửa sổ đo mà owner vừa ký hôm qua vì prompt đã chồng **sáu lần** trong bảy ngày.
   Đây là **quyết định của owner, không phải việc agent tự chọn**.
2. Lỗi này **sống 67 ngày** rồi. Thêm 13 ngày không đổi bản chất, nhưng **phá cửa sổ đo thì
   mất 14 ngày** — và đó là thứ không mua lại được.
3. `RM-08` nói rõ: quan ngại đã nêu một lần thì owner quyết, agent không được viện để hoãn.
   Ngược lại cũng đúng — **agent không được tự phá cái owner vừa ký**.

---

## 5. Đã làm gì

**KHÔNG SỬA GÌ.** Phiên này chỉ đọc. Đã làm:

| | |
|---|---|
| Đồng bộ dữ liệu sống | local cũ **13,6 giờ** ⇒ **RM-01 chặn** ⇒ chạy `_sync_live_forensic_inputs.py` trước |
| 6 mũi soi song song | VPS runtime · kết quả 07/08 · xung đột đóng băng · phép đo đang chờ · sức khoẻ A1 · phân loại tồn đọng |
| 22 phản biện đối kháng | mỗi phát hiện nặng bị một agent riêng **cố bác bỏ**; chỉ giữ phát hiện sống sót |
| Tự kiểm độc lập | agent chính tự chạy lại phát hiện nặng nhất, **không tin agent con** |
| Ghi 3 mặt tài liệu | `CHANGELOG` · `SSOT` · `FOLLOW_UP` (FU-341 → FU-344) |

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| **RM-01** tuổi dữ liệu | local 13,6h ⇒ **CHẶN** ⇒ đồng bộ lại, manifest `20260808_082653` |
| Không sửa production | **ĐẠT** — 0 tệp `web/backend/*.py` bị sửa |
| Không mutation DB | **ĐẠT** — mọi kết nối `mode=ro` |
| Không đụng 4 bảng khoá | **ĐẠT** |
| **QD-041** đóng băng | **ĐẠT** — `_v11028_cong_dong_bang.py` → `DONG_BANG_QD041=CON_NGUYEN`, md5 khớp cả VPS |
| Không deploy / restart | **ĐẠT** — `NRestarts=0`, PID không đổi |

---

## 7. Vướng vấp

**7.1 — Agent con báo NHẸ hơn sự thật.** Mũi soi báo *"908 lượt, riêng official 9/21"*. Đúng,
nhưng nó **chưa nêu** rằng cổng canh `> 50` **chính là** thứ làm lỗi câm, và **chưa nêu** log in
ra màu xanh. Agent chính phải tự đọc code mới ra hai chi tiết đó — chúng mới là lý do lỗi sống
được 67 ngày.

**7.2 — Đoán nhầm tên cột hai lần.** `predictions.model_name` (thật là `ai_model`) và
`final_bundles.target_region` (thật là `region`). Đúng bẫy **RM-10**. Phải `PRAGMA table_info`
mới đi tiếp được.

**7.3 — Trace không có `run_source`.** Muốn tách official khỏi shadow phải **join** trace ×
`predictions` theo `(date, region, model)`. Nếu chỉ đọc trace thì con số 908 sẽ bị hiểu nhầm
thành 908 lượt official.

**7.4 — Ba mũi soi con dùng tên tự nghĩ.** Một mũi báo *"cổng tuổi dữ liệu chưa có một dòng code
nào"* — sai, khuôn cổng đã tồn tại dưới tên khác. Phản biện bác được. Đúng **RM-10**.

---

## 8. Gỡ về

Không cần — phiên này **không sửa gì**. Ba mặt tài liệu chỉ **thêm vào đầu tệp**
(`_doc_prepend.prepend`, từ chối nếu tệp ngắn đi).

---

## 9. Theo dõi tiếp

| mã | nhãn | hạn | trạng thái |
|---|---|---|---|
| **FU-341 · SC2108** | `build_context_pack(shadow_mode=True)` vỡ | 21/08 | `OWNER_DECISION_NEEDED` |
| **FU-342 · KS0808-3** | cổng đóng băng chưa nối hook `git commit` | 08/08 | `MEASURED_BUT_NOT_FIXED` |
| **FU-343 · QD0811** | ba quyết định đóng băng ngược nhau | 11/08 | `OWNER_DECISION_NEEDED` |
| **FU-344 · DO2108-2** | bằng chứng số cho RM-04 + phải đăng ký ngưỡng FU-284 TRƯỚC 21/08 | 21/08 | `WAIT_LIVE` |

### Ba câu cần owner ký

1. **FU-341** — *"`gpt-oss-120b` (model chính thức) chạy thiếu ~10.000 ký tự ngữ cảnh ở 42,9%
   số lượt. Vá thì phá cửa sổ đo 14 ngày anh vừa ký. Anh chọn (a) mở khoá vá ngay và tính lại
   cửa sổ đo, (b) giữ đóng băng tới 21/08, hay (c) tạm gỡ nó khỏi bỏ phiếu — nhưng (c) lại đụng
   chính mục ① của QD-041?"*
2. **FU-343** — *"Đóng `QD-029` và `OD-20260801-D`, giữ mình `QD-041` — anh duyệt không?"*
3. **FU-344** — *"Ngưỡng FU-284 'tụt ≥5 điểm' vượt sức cửa sổ 14 ngày. Anh chọn (a) đổi ngưỡng
   thành ≥9,33 điểm giữ hạn 21/08, hay (b) giữ 5 điểm và dời hạn?"*
