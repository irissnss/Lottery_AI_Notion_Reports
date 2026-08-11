# REPORT V11062 — §63 CƠ CHẾ NÂNG VERSION + TRUY "GEMINI 3.6 FLASH MB RỖNG"

**Ngày:** 2026-08-11 tối · **Mã đọc:** `TK1108` · **Quyết định:** `QD-062`
**Production KHÔNG đổi** — không deploy, không restart · `QD-041` nguyên vẹn

---

## 1. Tóm tắt

Owner hỏi bốn việc. Ba việc trả lời được ngay, một việc lộ ra **hai mảnh quản trị đã chết**.

| # | owner hỏi | kết quả |
|---|---|---|
| 1 | *"Gemini 3.6 Flash MB nay rỗng là sao?"* | **Google trả 503 riêng model đó**; dự phòng OpenRouter **có chạy, trả 200, nhưng nội dung không dùng được**. Model là **shadow**, **không ảnh hưởng bạch thủ MB** |
| 2 | *"prompt hôm qua điều chỉnh có thấy output khá hơn không?"* | **Chưa được phép đọc** (9/96 cặp). Nhưng **vận hành cải thiện đo được: 0/5 → 12/12** |
| 3 | *"các đề xuất anh đồng ý"* | `FU-283` là việc tiếp theo — **chưa làm trong phiên này** |
| 4 | *"có cơ chế nâng version chưa?"* | **Ba mảnh rời, HAI mảnh đã CHẾT.** Đã dựng `§63` + công cụ + cổng |

---

## 2. Owner yêu cầu gì (nguyên văn)

> *"Còn 1 chỗ em chưa phân tích tại sao ' Gemini 3.6 Flash ' MB nay rỗng là sao? các prompt hôm
> qua điều chỉnh có thấy output dự đoán khá hơn không? Các đề xuất của em anh đồng ý em tiến hành
> 1 cách cẩn thận và tỉ mỉ dùm anh nhé.*
>
> *Dự án có cơ chế nâng version và cập nhật changlog, history chưa anh cần em xử lý thêm chỗ này
> và cập nhật vào claude.md sync nhất quán với 5 file quản trị khac dùm anh"* — 11/08

---

## 3. Đào bới / phát hiện

### 3.1 · "Gemini 3.6 Flash" MB rỗng — bốn lớp, và lớp cuối mới là nguyên nhân

**Lớp 1 — không phải hỏng kinh niên.** 32 dòng lịch sử, **chỉ 1 rỗng**, chính là MB hôm nay.
MN (`["03","19"]` WIN) và MT (`["56","31"]`) **cùng ngày vẫn ra số** ⇒ khoá không phải nguyên nhân.

**Lớp 2 — Google trả 503, và chỉ cho model này:**

```
16:59:09  gemini-3.5-flash  → 200
17:00:42  gemini-3.6-flash  → 503 Service Unavailable      ← 93 giây sau
17:49:23  gemini-3.5-flash  → 200
17:50:05  gemini-3.6-flash  → 503                          ← 42 giây sau
```

Cùng dự án, cùng đường khoá, **cách nhau chưa tới 2 phút**. ⇒ **KHÔNG phải Google sập chung**,
**KHÔNG phải khoá** — riêng **model id** đó không được phục vụ.

Journal xác nhận khoá đúng: `[KEY_MODE] gemini-3.6-flash: DB_GOOGLE_SHADOW (gemini_key_shadow_new
from DB)`, và preflight của đường official **đã tự phát hiện lệch env/DB rồi chọn DB**:
`[SHADOW_PREFLIGHT] warnings=['gemini-3.6-flash:db_env_drift:google:selected_db']`.

> Ghi rõ vì sáng nay agent mắc **lỗi ngược lại**: gọi một lỗi cấu hình của mình thành *«hạn mức
> nhà cung cấp»*. Lần này bằng chứng đi hướng khác — **không được bẻ kết luận cho khớp bài học
> hôm trước**.

**Lớp 3 — dự phòng CÓ chạy và CÓ thành công, nhưng vẫn rỗng:**

```
17:50:05  Google      → 503
17:50:08  OpenRouter  → 200 OK        ← GOOGLE_OPENROUTER_FALLBACK đã kích hoạt
17:51:13  ghi vào DB  → RỖNG
```

**HTTP 200 ≠ có số.** Đúng họ lỗi agent vừa mắc sáng nay ở lane A/B.

**Lớp 4 — và đây là câu trả lời cho «có ảnh hưởng gì không»:**

| | |
|---|---|
| `run_source` | **`shadow_auto_eval`** ⇒ **KHÔNG nằm trên đường ra số official** |
| giờ ghi | **17:51:13** — MB chốt bundle **17:37**, tức **muộn 14 phút** |
| có bị tính thua oan không | **KHÔNG** — bộ chấm gắn `status=NO_ANSWER`, `pick_count=0` |

⇒ **Không ảnh hưởng bạch thủ MB hôm nay.** MB trượt vì pool kém (18 số, 2 trúng, kỳ vọng ~4).

**Một báo động giả agent đã tự rút:** thấy 140 dòng dự đoán rỗng đều mang `predictions.status =
LOSE`, agent định báo *«model bị dìm oan, ảnh hưởng xếp hạng combo-super»* — nặng nhất
`gemma-4-31b` **53/230 = 23%**. Kiểm ra thì **bộ chấm dùng nhãn riêng**: `model_daily_eval` gắn
`NO_ANSWER`, và `combo_super.py:673` lọc `AND status IN ('WIN','LOSE')` ⇒ **đã loại khỏi mẫu số**.
Việc này **đã được xử từ `V11036` / `QD-046` / `FU-355`**, có cổng riêng —
`_v11036_kiem_no_answer.py` chạy lại hôm nay: **`NO_ANSWER_V11036=ĐẠT`, exit 0**, *«0 model rớt
sàn vì loại lượt rỗng»*.

**Chỗ mù nhỏ còn lại (không sửa vội, ghi lại):** dự phòng trả 200 mà không có số thì **không ghi
gì để phân biệt** với "model từ chối trả lời". Nằm ở đường shadow nên không cấp bách.

### 3.2 · Prompt ba tầng có tốt hơn không — trả lời trung thực

**Phải nói rõ trước, vì rất dễ hiểu nhầm:** prompt ba tầng **CHỈ chạy trong lane shadow**,
**KHÔNG** đụng production (`QD-041` khoá tới 21/08). Kết quả **1/3 hôm nay không liên quan gì tới
nó** — production vẫn chạy prompt cũ nguyên vẹn.

**Về chất lượng: CHƯA ĐƯỢC PHÉP ĐỌC.** Ngưỡng đăng ký trước là **≥96 cặp bất đồng VÀ |z|≥1,96**;
hiện có **9**. Đọc bây giờ chính là cách sáu lần *«hứa rồi rữa»* (V10655→V10790) đã xảy ra.

**Hai thứ đo được ngay và nói được:**

| | 10/08 | 11/08 |
|---|---|---|
| lượt chạy thành công | **0/5** | **12/12** |
| trễ | timeout | 35–154s |

Và **một thay đổi hành vi thật**: **4/4 model chuyển sang dạng `§25`** (`main_number`) thay vì
`numbers`, vì T-B đẩy §22–§26 xuống tầng 3. Đó là bằng chứng prompt **có tác động** — **không
phải** bằng chứng nó **tốt hơn**. Dự kiến đủ ngưỡng khoảng **22/08**.

### 3.3 · Cơ chế nâng version — ba mảnh rời, HAI mảnh đã chết

| khâu | trước V11062 |
|---|---|
| cấp số hiệu | ✅ `_v11044_cong_so_hieu.py` quét **sáu** nơi — dựng sau khi số va chạm **5 lần trong 2 ngày** |
| ghi tài liệu | ❌ **không có công cụ dùng lại** — `_v10967_docs_bump.py` viết cứng cho riêng V10967; **mỗi phiên tự viết script nháp mới** (riêng hôm nay **2 cái**) |
| `AUTOMATION_HISTORY.jsonl` | ❌ **CHẾT** — nửa sổ sự kiện im từ **31/07**, nửa sổ version im từ **04/08** (mục cuối `V10984`) |
| luật thành văn | ❌ **KHÔNG mặt nào** trong sáu mặt ghi quy trình |

**Không cổng nào phát hiện, vì chưa ai hỏi «tệp này còn được ghi không?»** — đúng họ `RM-20`.

**Phát hiện thêm:** `AUTOMATION_STATE.json` còn sống nhưng **phình khoá** —
`_v10893_last_event`, `_v10891_last_event`, `_v10889_last_event`… **mỗi phiên thêm một khoá**, và
`events[]` chỉ có **7 mục** trong khi có **374** version.

---

## 4. Hướng xử lý và vì sao

### Vì sao KHÔNG bù 286 bản cũ

Bản nháp đầu của cổng lấy tiền đề *«HISTORY phải soi gương toàn bộ CHANGELOG»* rồi báo **«thiếu
286 bản»**. **Tiền đề SAI** — `RM-10`, kết luận theo tên đoán.

Đọc trường thật:

```
A) sổ SỰ KIỆN  seq / observed_at / event_type / command / exit_code   206 dòng, gốc 26/04
B) sổ VERSION  version / ngay / chu_de                                101 dòng, do _v10787_* nhét vào sau
```

Tệp **trộn hai lược đồ** và **chưa bao giờ** là bản sao của `CHANGELOG`.

Và bù 286 dòng suy từ tiêu đề rồi đóng dấu như thể ghi lúc xảy ra là **chế dữ liệu** — đúng thứ
`RM-17` cấm. **Ghi thẳng là thiếu, kèm lý do.** Cổng thi hành **từ V11062 trở đi**.

---

## 5. Đã làm gì

| # | việc | bằng chứng |
|---|---|---|
| 1 | **`§63` (A61) vào ĐỦ SÁU MẶT** | `CLAUDE.md` +3.285 · `.Antigravityrules.md` +3.285 · `.AGENT.md` +2.021 (tiếng Anh) · `.cursorrules` +1.202 · `.antigravityrules` +173 · hai mặt sinh regenerate |
| 2 | **Công cụ dùng lại** `_v11062_nang_version.ghi()` — **bốn mặt một lệnh** | `CHANGELOG` prepend · `SSOT` prepend · `STATE` seq+1 · **`HISTORY` append** |
| 3 | **Cổng bốn phép** K1–K4, thi hành từ V11062 | `NANG_VERSION_V11062=ĐẠT` |
| 4 | **RM-15 thử chặn** | bỏ 1 mục ⇒ **ĐỎ** · khôi phục ⇒ **XANH** · tệp về nguyên trạng **342.323 byte** |
| 5 | **Dùng chính công cụ đó ghi V11062** | `governance_seq 403 → 404`, `HISTORY` mới **0 ngày tuổi** |
| 6 | Sửa `.antigravityrules` còn ghi `RM-01…RM-20` | → **`RM-21`** |
| 7 | `_v11061_kiem_toan_1108.py` — bộ đo kiểm toán cuối ngày, có cổng RM-01 | commit kèm |

**Ba luật cứng ghi vào sáu mặt:** ① cấm `open(p,"w")` trên tài liệu quản trị — dùng
`_doc_prepend.prepend()` (sinh từ ngày **31/07 xoá sạch hai tệp 900 KB**) · ② cấm cấp số bằng mắt
· ③ `HISTORY` chỉ APPEND.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v11062_nang_version.py --kiem` | **✓ ĐẠT** — K1–K4 |
| `_v11062_nang_version.py --thu-chan` | **✓ ĐẠT** (RM-15) |
| `_v10925_rule_sync_check.py` | **✓ SÁU MẶT ĐỒNG BỘ** |
| `_v11036_kiem_no_answer.py` | **✓ `NO_ANSWER_V11036=ĐẠT`**, exit 0 |
| `_v10921_report_gate.py V11062` | (chạy cuối phiên) |

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| 11/08 | *"Còn 1 chỗ em chưa phân tích tại sao ' Gemini 3.6 Flash ' MB nay rỗng là sao?"* |
| 11/08 | *"các prompt hôm qua điều chỉnh có thấy output dự đoán khá hơn không?"* |
| 11/08 | *"Dự án có cơ chế nâng version và cập nhật changlog, history chưa anh cần em xử lý thêm chỗ này và cập nhật vào claude.md sync nhất quán với 5 file quản trị khac dùm anh"* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| Google trả **503 riêng** `gemini-3.6-flash`; `3.5-flash` **200** trước đó 93 giây | journal 16:59:09 / 17:00:42 / 17:49:23 / 17:50:05 |
| dự phòng OpenRouter **kích hoạt và trả 200** | 17:50:08, `GOOGLE_OPENROUTER_FALLBACK` (`gpt_analyzer.py:239`) |
| dòng MB ghi **17:51:13**, bundle chốt **17:37** | `predictions` · `final_bundles` |
| bộ chấm gắn `NO_ANSWER` chứ không phải `LOSE`; WR loại khỏi mẫu số | `model_daily_eval` · `combo_super.py:673` |
| `HISTORY` nửa sự kiện im từ **31/07**, nửa version im từ **04/08** | đọc trực tiếp `AUTOMATION_HISTORY.jsonl` |
| `STATE` phình khoá `_v10XXX_last_event` mỗi phiên | `AUTOMATION_STATE.json` |

### `DOC_SAID`

| tài liệu ghi gì | file:mục | lệch? |
|---|---|---|
| *"Máy đọc được: `AUTOMATION_STATE.json` · `AUTOMATION_HISTORY.jsonl`"* | `CLAUDE.md` §Bề mặt tự động hoá | **⚠ đúng tên, sai trạng thái** — cả hai nửa `HISTORY` **đã ngừng ghi** khi câu này vẫn đứng |
| `RM-17` *"số không tái lập được thì cấm dùng làm căn cứ"* | `CLAUDE.md` §61 | **khớp** — nên **không bù** 286 bản |
| `RM-10` *"cấm kết luận theo tên đoán"* | `CLAUDE.md` §61 | **khớp** — và agent **vừa vi phạm rồi tự bắt** |
| `V11036`/`QD-046`/`FU-355` — `NO_ANSWER` | `CHANGELOG.md` | **khớp** — cổng vẫn ĐẠT |

### Ba lớp lệch nhau ⇒ FINDING

1. **`DOC_SAID` ≠ `CODE_DID`:** `CLAUDE.md` liệt kê `AUTOMATION_HISTORY.jsonl` là mặt máy đọc
   được, nhưng **cả hai nửa đã chết** 11 và 7 ngày. Tài liệu mô tả **một mặt không còn hoạt động**
   mà không ai biết. `§63`/K2 nay canh đúng chỗ đó.
2. **`OWNER_SAID` phát hiện thứ mà mọi cổng đều bỏ sót** — câu hỏi *"có cơ chế chưa?"* lôi ra hai
   mảnh chết mà **8 cổng máy** hiện có không mảnh nào soi tới.

---

## 7. Vướng vấp

| # | vấp | quy tắc |
|---|---|---|
| 1 | **Đặt tiền đề sai cho chính cổng mình viết** — *"HISTORY phải soi gương CHANGELOG"* ⇒ báo *"thiếu 286 bản"*. Đọc trường thật mới thấy đó là **sổ sự kiện** | **RM-10** |
| 2 | **Suýt báo động giả về 140 dòng rỗng bị tính thua** — bộ chấm dùng nhãn riêng `NO_ANSWER` và **đã xử từ V11036** | **RM-13** · §56 (tra trước khi báo) |
| 3 | Suýt gọi 503 là *"cấu hình sai"* để khớp bài học buổi sáng — bằng chứng đi **hướng khác** | **RM-13** |

**Vấp 1 đáng nói nhất:** agent viết một cổng **để chống việc đoán**, mà **chính cổng đó dựng trên
một cái đoán**. Chỉ khi buộc mình in ra **tên trường thật** mới lộ.

---

## 8. Gỡ về

```bash
git revert 420cc46      # V11062 — chỉ thêm công cụ + luật, không đổi hành vi production
```

---

## 9. Theo dõi tiếp

| mã | việc | mốc |
|---|---|---|
| **FU-283** · `DO1308` | **việc tiếp theo owner đã duyệt** — đo độ trễ từng model + panel §52. Bằng chứng cấp bách: biên MT **~13 phút kinh niên** vs model chậm **190s** | **13/08** |
| **FU-398** · `PB1108` | lane A/B — 12 cặp, 9 bất đồng | ~**22/08** · cấm đọc sớm |
| **FU-399** · `UI1108` | UI `/filter` — **chờ owner mô tả** | — |
| — | chỗ mù: dự phòng trả 200 mà không có số ⇒ **không phân biệt được** với "model từ chối" | đường shadow, không cấp bách |
| — | `STATE.json` phình khoá `_v10XXX_last_event` mỗi phiên | chưa cấp bách |

---

TanPhatAI cần làm: ① ghi `QD-062` và **`§63` (A61)** — quy tắc mới, **đã vào đủ sáu mặt**;
② ghi rằng **`AUTOMATION_HISTORY.jsonl` từng CHẾT** (sự kiện 31/07, version 04/08) và nay có cổng
**K2** canh tuổi ≤ 3 ngày; ③ ghi **CỐ Ý không bù 286 bản trước mốc** kèm lý do `RM-17` — đừng ai
"sửa" bằng cách bù sau; ④ ghi câu trả lời cho owner về **`gemini-3.6-flash` MB rỗng**: **503 riêng
model đó + dự phòng trả 200 nhưng nội dung rỗng**, model là **shadow**, **không ảnh hưởng bạch thủ**;
⑤ ghi rõ **prompt ba tầng CHƯA ĐƯỢC PHÉP ĐỌC** (9/96 cặp) — đừng ai suy diễn từ kết quả 1/3 hôm nay.
