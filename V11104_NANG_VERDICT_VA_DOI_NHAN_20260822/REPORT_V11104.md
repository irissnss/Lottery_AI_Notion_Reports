# REPORT V11104 — NÂNG VERDICT · `FU-424` ĐỔI NHÃN · ĐẾM BUNDLE THIẾU NGƯỜI · RÚT LẠI CHẨN ĐOÁN CẦU DAO

**Ngày:** 2026-08-22 (tối) · **Mã đọc:** `KS2208-2` · **Quyết định:** `QD-071` (thi hành tiếp)
**Production:** **không** deploy mã production; chỉ đưa **một bộ đo chỉ-đọc** lên VPS
**Verdict:** `V11102` → **`RUNTIME_PROVEN`** · bản thân V11104: `CODE_PUSHED` + `REPORT_PUBLISHED`

---

## 1. Tóm tắt

Bốn việc. **Ba trong bốn cho kết quả khác điều đang được tin**, và một trong đó buộc em **rút lại
chẩn đoán của chính báo cáo sáng nay**.

| việc | đang tin | đo được |
|---|---|---|
| kiểm chứng cuối `V11102` | — | ✅ **đủ ba điều kiện** ⇒ nâng `RUNTIME_PROVEN` |
| `glm-5.1` rỗng 18/08 | *«cầu dao ngắt mạch, lượt gọi chưa rời máy»* | ❌ **SAI** — model trả lời thật **79,36 s · 33.685 token** |
| nhãn `EMPTY_PROVIDER_OUTPUT` | *«ghi sai sự thật, phải vá»* | ❌ **SAI** — nhãn **ghi đúng**; **không vá** |
| `FU-419` khối D-1 | *«lỗi nguồn/lọc/định dạng?»* | ❌ cả ba đều không — là **một phép cắt** `sorted(...)[:12]` |

Và **kết quả dự đoán hôm nay**: **1 trúng / 3 miền**, đúng bằng nền — `n=3`, chưa được phép kết luận.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«Kiểm tra phân tích đánh giá kết quả dự đoán hôm nay dùm anh»*

> *«Sau 18:31: job đo phải sinh CẢ HAI HỌ cho 22/08 — nêu số dòng từng họ, giờ tạo từng bản ghi
> (RM-16). … ĐỦ ba điều kiện ⇒ nâng V11102 lên RUNTIME_PROVEN trong sổ, ghi rõ bằng chứng nâng.»*

> *«Vá: khi RM-01 đỏ, mọi phép đo dựa trên DB local phải đổi nhãn thành KHÔNG_KẾT_LUẬN_ĐƯỢC
> (không phải TRÔI) và được IN RA TRƯỚC các phép khác. … CẤM biến thành «bỏ qua các phép khác khi
> dữ liệu cũ».»*

> *«① Vá nhãn sai của đường cầu dao … ② Đếm và báo số ngày bundle thiếu người đóng góp: hiện
> KHÔNG AI ĐẾM.»*

> *«`FU-419` … Đo trước: vì sao chỉ 00–21 … chỉ trình, CẤM vá trong phiên này.»*

---

## 3. Đào bới / phát hiện

### 3.1 · Kết quả dự đoán hôm nay 22/08

| miền | số đuôi ra | **nền 1 số hôm nay** | bạch thủ | kết quả | model output có mặt | model trúng bằng số đầu |
|---|---:|---:|---|---|---|---|
| **MN** | 51 | **51%** | `10` | ✅ **WIN** | **14/15** — thiếu `deepseek-reasoner` | **4**: `combo-super` · `gemini-2.5-flash` · `random-forest` · `xgboost` |
| MT | 36 | 36% | `41` | ❌ LOSE | 15/15 | **1**: `lstm` |
| MB | 24 | 24% | `28` | ❌ LOSE | 15/15 | **0** |

Kỳ vọng theo nền hôm nay: `0,51 + 0,36 + 0,24 = 1,11`. Thực tế **1**. **Đúng bằng nền** — `n=3`,
`RM-04`: **chưa được phép kết luận**.

Ba điểm đáng chú ý:

- **MN trúng nhưng ít giá trị thông tin.** Hôm nay MN ra **51 đuôi khác nhau** ⇒ nền **51%**, gần
  như tung đồng xu. Trúng ở MB (nền 24%) mới đáng kể.
- **MB: 0/15 model trúng bằng số đầu.** Không cách chọn nào cứu được — **lỗi khâu sinh số**,
  không phải khâu chọn.
- **`deepseek-reasoner` vắng mặt ở MN** — chính là ca mẫu cho phép đếm ở §5.2.

### 3.2 · `glm-5.1` 18/08 — bằng chứng trực tiếp lật ngược chẩn đoán

Trace của đúng lượt đó:

```
finish_reason "stop"  ·  latency_seconds 79,3607  ·  token_count 33.685  ·  reasoning_tokens 9.180
```

Trung vị `token_count` của chính `glm-5.1`/MN qua 80 lượt: **28.045** (nhỏ nhất 20.162, lớn nhất
45.026). ⇒ lượt 18/08 **nằm trong khoảng bình thường**, không phải lượt hỏng.

**Model đã gọi thật, chạy 79 giây, sinh 33.685 token — rồi không rút ra được số nào.**

15/08 thì **không có dòng trace nào**, khớp với `ERROR` *«Lỗi phân tích response JSON từ AI:
Expecting value: line 1 column 1»* sau **134 giây** ⇒ provider trả thân rỗng thật. Phần này của
`REPORT_V11103` **vẫn đúng**, kể cả việc `deepseek-reasoner` (nhà cung cấp khác) hỏng cùng ngày.

### 3.3 · Một điều CHƯA GIẢI THÍCH ĐƯỢC — ghi thẳng

Bảng chẩn đoán ghi độ trễ **9 ms**; trace ghi **79.360 ms**. Đã kiểm:

- chỉ **1/13** dòng `official_ai_predict` có độ trễ dưới 1 giây ⇒ **không phải hỏng cả trường**;
- đường lượt-về-muộn (`_pending_ai_calls` → `:4665`) truyền **đúng** `model_call_start`;
- nhánh cầu dao trả dict **có** khoá `error` ⇒ sẽ ra `ERROR`, **không** ra `EMPTY_PROVIDER_OUTPUT`.

**Chưa truy ra.** Và chính con số 9 ms đó đã đẩy chẩn đoán đi sai hướng một lần — nên nó đáng
được truy tiếp, không đáng bỏ qua.

### 3.4 · `FU-419` — vì sao khối D-1 chỉ hiện đuôi 00–21

Đo 31 ngày trên kết quả thật:

| | |
|---|---:|
| kho đuôi D-1 thật | **71,0**/ngày (61–79) |
| dòng bơm vào prompt hiện | **12** |
| đuôi **từng** hiện trong 31 ngày | **22/100** · lớn nhất **`21`** |
| đuôi **chưa bao giờ** hiện | **78/100** |

Nguyên nhân, `gpt_analyzer.py:6019`:

```python
f"- D-1 cross-region tail pool: {', '.join(sorted(d1_union)[:12])}"
```

`sorted(...)` sắp **tăng dần** rồi `[:12]` lấy **12 phần tử đầu** ⇒ **luôn là 12 đuôi NHỎ NHẤT**.
Kho có ~71/100 đuôi nên 12 nhỏ nhất gần như luôn rơi vào `00–21`.

**Không phải nguồn dữ liệu · không phải bộ lọc · không phải lỗi định dạng.**

---

## 4. Hướng xử lý và vì sao chọn

### 4.1 · `FU-424` — ĐỔI NHÃN, không TẮT

Ca thật rạng sáng 22/08: `QD-056` (dữ liệu local cũ) và `QD-046` (`glm-5.1` rớt sàn) **cùng đỏ**,
và cái đầu là **lời giải thích** cho cái sau.

Bốn mảnh vá:

| mảnh | chi tiết |
|---|---|
| `tuoi_du_lieu()` | đọc `latest_manifest.json`; **không đọc được ⇒ trả `None`**, KHÔNG trả 0 — 0 đọc thành *«vừa mới đồng bộ»* |
| `_doc_db_local()` | dò **theo NỘI DUNG** tệp script, không theo tên (`RM-10`) |
| `main()` | in khối cảnh báo **TRƯỚC** bảng, rồi đánh dấu từng phép lệch có nguồn là DB local |
| `phan_tang()` | loại phép đã đánh dấu khỏi `TRÔI`; thêm nhãn `KHÔNG KẾT LUẬN ĐƯỢC` |

**Kết quả thật:** `QD-056` chuyển `TRÔI` → `KHÔNG KẾT LUẬN ĐƯỢC`, trôi **3 → 2**.

### 4.2 · `FU-423` ① — **KHÔNG VÁ**, và vì sao đó là câu trả lời đúng

Owner ra lệnh *«vá nhãn sai của đường cầu dao»* — nhưng lệnh đó **dựa trên chẩn đoán sai của
chính em** (§3.2). Nhãn `EMPTY_PROVIDER_OUTPUT` với câu *«provider response parsed but no
prediction numbers were found»* **mô tả đúng** điều đã xảy ra.

Vá một nhãn đang đúng thành một nhãn khác chỉ để khớp một chẩn đoán sai là **làm hỏng thứ đang
đúng**. Em dừng, rút lại, và trình lại.

**Việc đáng làm thay vào đó:** truy tiếp con số **9 ms** (§3.3) và truy **khâu rút số** — vì sao
một câu trả lời 33.685 token không cho ra số nào. **Cần owner duyệt** vì cả hai ngoài gói đã ký.

### 4.3 · `FU-419` — ba lối, kèm được/mất (`QD-069`)

**Chuyện đang xảy ra, nói gọn:** prompt có một dòng tên là *«kho đuôi D-1 của cả ba miền»*, nhưng
nó **chỉ liệt kê 12 đuôi nhỏ nhất** trong khoảng 71 đuôi thật. Suốt 31 ngày, **78/100 đuôi chưa
bao giờ xuất hiện** ở dòng đó, và số lớn nhất từng hiện là **`21`**.

| lối | **được** | **mất** |
|---|---|---|
| **(a) chỉ ghi SỐ ĐẾM, bỏ danh sách** — *«D-1 có 71 đuôi»* — **đề xuất** | dòng thôi nói sai; **không** còn cách nào thiên lệch; sửa một dòng | model mất một gợi ý cụ thể (mà gợi ý đó vốn đã lệch) |
| (b) lấy mẫu **12 đại diện** + ghi tổng số | giữ tính cụ thể, bỏ thiên lệch | phải chọn cách lấy mẫu, và mẫu ngẫu nhiên làm prompt **không tái lập được** — đụng `RM-11` |
| (c) để nguyên | rủi ro bằng 0 | prompt giữ một dòng **nói sai tên gọi của chính nó** |

**Cân nhắc quan trọng — không tô hồng:** `FU-316` (V11076) **đã đo** và model chọn đuôi thấp
**20,2%** so với nền **21,0%**, `z = −1,01` ⇒ **KHÔNG neo**. Nghĩa là đây là **prompt nói sai**,
**chưa chứng minh được là prompt làm hỏng**. Sửa để prompt thôi nói sai là đúng; **đừng hứa nó
làm tăng độ trúng**.

---

## 5. Đã làm gì

### 5.1 · `V11102` → `RUNTIME_PROVEN` (GĐ-0)

| điều kiện | bằng chứng, đo trên VPS |
|---|---|
| ① `CTX-18.4` | **19/19** bản ghi trace tạo 22/08 · **0** bản cũ · mới nhất `05:34:53` |
| ② job đo sinh **cả hai họ** | MN kết quả `16:40:40` → job ghi **`16:40:43`** (OUTPUT **14** · SHADOW **12**) · MT `17:32:34` → **`17:32:36`** (15 · 11) · MB `18:31:02` → **`18:31:05`** (15 · 11) · log: `inserted=26` |
| ③ bảng khoá + lỗi | `model_daily_eval` **không đổi** · `lottery_results` **+8** · `final_bundles` **+2** · `predictions` **+40** — tăng tự nhiên · **0** Traceback · **0** CRITICAL · PID `2128063` không đổi **19 giờ** |

Giờ tạo **2–3 giây sau khi kết quả về** chứng minh job chạy **đúng cơ chế**, không phải chạy tay.

### 5.2 · Đếm ngày bundle thiếu người (GĐ-2 ②)

`_v11104_dem_bundle_thieu_nguoi.py` — trước đây **không ai đếm**.

**Kết quả (chạy trên VPS): 30/183 ngày-miền = 16,4%** thiếu ít nhất một người.

**Đọc số cho đúng — đây là chỗ dễ đọc sai:** `glm-5.1` vắng 24 và `gpt-oss-120b` vắng 22 **gần
như toàn bộ là ảo** — hai model chỉ vào danh sách output ngày **21/08** (`FU-380`), và cửa sổ
±7 ngày làm sự có mặt của chúng «lem» ngược về trước. **Vắng mặt thật:** `deepseek-reasoner`
**5** · `gpt-5.4` **3** · và MN hôm nay.

Hai quyết định thiết kế, cả hai đều dễ sai nếu làm ẩu:

1. **Sĩ số kỳ vọng suy ĐỘNG** (cao nhất trong ±7 ngày), **không** lấy danh sách hôm nay áp cho 60
   ngày trước — làm thế thì mọi ngày cũ đều trông như *«thiếu 2 người»* trong khi hai model đó
   **chưa hề tồn tại** trong danh sách lúc ấy (`RM-13` · `PRJ-SELECTION-WINDOW-001`).
2. **Chỉ tính lượt tạo TRƯỚC mốc chốt** — bản ghi tạo sau mốc thì lúc dựng bundle nó không tồn tại.

Thử chặn **4/4**, gồm phép *«gỡ một model khỏi một ngày ⇒ ngày đó phải bị đếm là thiếu»*.

Bảng in ra ghi thẳng: **«ĐẾM VÀ CHỈ ĐẾM»** — nó **không** nói vắng người thì bundle tệ hơn; muốn
nói điều đó phải so tỉ lệ trúng ngày đủ người với ngày thiếu người, **có nền và có z**.

### 5.3 · Thiết kế cho 24/08 (GĐ-4, plan-only)

`docs/THIET_KE_VA_FU421_VA_GIAO_THUC_DOC_TB_2408.md` — hai phần:

- **Vá `FU-421`: BỐN việc cùng lúc** — ba khoá phá hoà · **làm đường lùi kêu lên** · đo lại ba
  phép ra 0 thay đổi · **thêm phép so TRƯỚC/SAU trên bộ số đã công bố**. Việc ④ tách khỏi ③ vì
  ③ chứng minh *«phép đo không đổi»* còn ④ chứng minh *«đầu ra không đổi»* — và ④ mới là câu
  owner cần.
- **Giao thức đọc lane T-B 24/08** — 6 bước, bắt đầu bằng **đồng bộ trước** (`RM-01`), và **bốn
  điều cấm**, đứng đầu là *«đổi ngưỡng sau khi thấy số»*.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v10920_decision_ledger.py --thu-chan` (mới) | **3/3**: dữ liệu mới ⇒ không đổi nhãn · dữ liệu cũ ⇒ đổi nhãn **và in trước** · **0 phép bị nuốt mất** · manifest khớp từng byte |
| `_v11104_dem_bundle_thieu_nguoi.py --thu-chan` | **4/4**, gồm phép «lượt sau mốc chốt không tính là có mặt» |
| `_v11050_kiem_cong.py` (K1) | **8/8** cổng chạy được (trước khi vá: **1/8 hỏng**) |
| `_v11062_nang_version.py --kiem` | `NANG_VERSION_V11062=ĐẠT` |
| sổ quyết định | trôi **3 → 2** (`QD-056` chuyển sang `KHÔNG KẾT LUẬN ĐƯỢC`) |

**Nguồn đo:** mọi số của §3.1, §3.2, §5.1, §5.2 đọc **thẳng trên VPS** (`RM-13`).

---

## 7. Vướng vấp

1. **Chẩn đoán cầu dao SAI, đã rút** — §3.2. Bài học: em suy từ **đọc mã** (`_openrouter_circuit_check`
   trả dict không có `prediction`) mà **không kiểm dòng `4329`** — chỗ đó bắt `'error' in result`
   **trước**, nên nhánh cầu dao sẽ ra `ERROR`. Đọc nửa đường rồi kết luận.

2. **Chính em mắc lại lỗi `FU-424` ngay trong phiên vá `FU-424`.** Bộ đếm mới chạy lần đầu trên
   bản local đồng bộ lúc 10:00 và báo *«MT 22/08 chỉ có 6/15»* — **sai hoàn toàn** (thật 15/15,
   tất cả trước mốc 16:58). Đã cắm phép cảnh tuổi dữ liệu **vào trong chính bộ đo**.

3. **Hai lỗi trong bản vá `FU-424` đầu**, cả hai làm cổng **tự làm mình mù**: đoán tên khoá thời
   gian trong manifest (thật là `sync_completed_at`) ⇒ luôn trả `None`; và bản ghi phép **không
   mang `chay_lenh`** ⇒ phép nhận diện **không bao giờ bật được**. Nếu chỉ chạy xuôi và thấy
   *«vẫn 4 TRÔI»* thì đã tưởng mình vừa làm một việc vô dụng.

4. **Hai khối FU thiếu ô `status`** do chính em ghi hôm nay (`FU-404`, `FU-423`) làm cổng K1 báo
   **1/8 hỏng**. Cùng một lỗi mắc **hai lần trong một phiên**.

---

## 8. Gỡ về

| việc | lệnh |
|---|---|
| `FU-424` | `git revert <sha>` · backup `backups/_v10920_decision_ledger.py.pre_v11104` |
| bộ đếm | `git revert <sha>` + `rm /root/Lottery_AI_Test/web/backend/_v11104_dem_bundle_thieu_nguoi.py` — chỉ-đọc, **không cron, không restart** |
| tài liệu thiết kế | `git revert <sha>` |

**Không có gì chạm production để gỡ** — phiên này không sửa mã production, không deploy, không
restart, không đụng DB.

---

## 9. Theo dõi tiếp

| mã | việc | hạn |
|---|---|---|
| `FU-421` | vá **BỐN việc cùng lúc** theo thiết kế đã soạn | **24/08** |
| — | đọc lane T-B theo **giao thức 6 bước** đã soạn | **24/08** |
| `FU-423` | owner chốt `FU-419`-style: hai việc còn lại **đã đổi** — không còn «vá nhãn», mà là **truy 9 ms** + **truy khâu rút số** | 25/08 |
| `FU-419` | owner chọn lối (a)/(b)/(c); **đề xuất (a)** — ghi số đếm, bỏ danh sách | 23/08 |
| `FU-424` | ✅ xong sớm (hạn 23/08) | — |
| — | 27/08 quyết **DỪNG** cho `gpt-5.5` và `qwen3-max-thinking` | 27/08 |
| *(chờ owner)* | truy con số **9 ms** — nó đã đẩy chẩn đoán đi sai một lần | — |

---

## §62 (A60) — BA LỚP NGUỒN

### `OWNER_SAID`

| nội dung | nguyên văn |
|---|---|
| kết quả hôm nay | *«Kiểm tra phân tích đánh giá kết quả dự đoán hôm nay dùm anh»* |
| nâng verdict | *«ĐỦ ba điều kiện ⇒ nâng V11102 lên RUNTIME_PROVEN trong sổ, ghi rõ bằng chứng nâng»* |
| `FU-424` | *«khi RM-01 đỏ, mọi phép đo dựa trên DB local phải đổi nhãn thành KHÔNG_KẾT_LUẬN_ĐƯỢC (không phải TRÔI) và được IN RA TRƯỚC… CẤM biến thành «bỏ qua các phép khác khi dữ liệu cũ»»* |
| `FU-423` | *«① Vá nhãn sai của đường cầu dao … ② Đếm và báo số ngày bundle thiếu người đóng góp: hiện KHÔNG AI ĐẾM»* |
| `FU-419` | *«chỉ trình, CẤM vá trong phiên này»* |

### `CODE_DID`

| việc | bằng chứng |
|---|---|
| lượt 05:00 + chiều đã chạy | `predictions` 22/08 **+40** dòng · bundle MN `05:20:58` · MT `16:47:19` · MB `17:40:35` |
| job đo sinh hai họ | 3 miền × 2 họ, ghi **2–3 giây** sau kết quả xổ |
| `FU-424` sống | `QD-056` chuyển `TRÔI` → `KHÔNG KẾT LUẬN ĐƯỢC`; thử chặn 3/3 |
| bộ đếm sống | 30/183 ngày-miền thiếu người; thử chặn 4/4 |
| `glm-5.1` 18/08 | trace: `finish_reason "stop"` · `79,3607 s` · `33.685 token` |
| `FU-419` | `sorted(d1_union)[:12]` ⇒ 78/100 đuôi chưa bao giờ hiện trong 31 ngày |
| production yên | không deploy · không restart · PID `2128063` · 0 Traceback |

### `DOC_SAID` — chỗ tài liệu **lệch** với mã

| lệch | chi tiết |
|---|---|
| `REPORT_V11103` ≠ dữ liệu | *«cầu dao ngắt mạch… lượt gọi chưa bao giờ ra khỏi máy»* — **đã rút** ở §3.2 |
| `REPORT_V11103` ≠ dữ liệu | *«nhãn `EMPTY_PROVIDER_OUTPUT` ghi sai sự thật»* — nhãn **ghi đúng**; **đã rút** |
| bảng chẩn đoán ≠ trace | độ trễ **9 ms** vs **79.360 ms** — **chưa truy ra**, ghi thẳng |
| prompt ≠ tên gọi của chính nó | dòng *«D-1 cross-region tail pool»* thật ra là **12 đuôi nhỏ nhất** trong ~71 |
| `docs/FOLLOW_UP_TRACKER.md` ≠ sổ quyết định | vẫn ghi `FU-216` hạn 09/08, `FU-231`/`FU-226` hạn 10/08 — chưa theo `QD-045` |

---

**TanPhatAI cần làm:** cập nhật `docs/FOLLOW_UP_TRACKER.md` — `FU-404` đóng (`V11102` nay là **`RUNTIME_PROVEN`**, bằng chứng ba điều kiện ghi trong khối), `FU-424` **xong sớm** trước hạn 23/08, và **`FU-423` đã ĐỔI NỘI DUNG**: không còn «vá nhãn cầu dao» (nhãn ghi đúng, chẩn đoán cũ đã rút) mà là **truy con số 9 ms** và **truy khâu rút số**; đọc thêm `docs/THIET_KE_VA_FU421_VA_GIAO_THUC_DOC_TB_2408.md` cho phiên 24/08; theo dõi ba việc: ① **24/08** vá `FU-421` phải làm **cả bốn việc** (cấm chỉ vá khoá phá hoà rồi bỏ đường lùi câm) và đọc lane T-B **theo đúng 6 bước, cấm đổi ngưỡng sau khi thấy số**, ② **23/08** owner chọn lối cho `FU-419` — đề xuất **(a) ghi số đếm, bỏ danh sách**, và **cấm hứa nó làm tăng độ trúng** vì `FU-316` đã đo ra `z = −1,01` không neo, ③ con số **9 ms** chưa truy ra và nó **đã đẩy chẩn đoán đi sai một lần** — cần owner duyệt cho truy tiếp.
