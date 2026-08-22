# REPORT V11105 — TRUY RA CON SỐ 9 ms · PAYLOAD BỊ VỨT CÓ CHỦ Ý · VÁ `FU-419` (CHƯA DEPLOY)

**Ngày:** 2026-08-23 (rạng sáng) · **Mã đọc:** `SC2308` · **Quyết định:** owner ký **03:44** + **03:50**
**Production KHÔNG đổi** — hai phép truy **chỉ-đọc**; bản vá `FU-419` đã commit nhưng **chưa deploy**
**Verdict:** `CODE_PUSHED` + `REPORT_PUBLISHED` · **CHƯA `DEPLOYED`** — lý do ở §5.3

---

## 1. Tóm tắt

Owner duyệt truy hai thứ còn treo từ hôm qua. **Cả hai đều truy ra đích**, và **cả hai đều nặng hơn
dự kiến** — không phải hai sự cố lẻ mà là **hai lớp lỗi**.

| việc | tưởng là | thật ra là |
|---|---|---|
| **9 ms** | một dòng dữ liệu lạ | **lỗi hệ thống của mốc đo** — cùng lượt chạy có **5 model khác** cũng sai |
| **khâu rút số** | *«đọc payload xem model trả gì»* | **payload đã bị vứt CÓ CHỦ Ý** — và thứ bị vứt là thứ duy nhất giải thích được |
| **`FU-419`** | sửa một dòng | ✅ vá xong, diff **đúng 1 dòng** × 3 miền — nhưng **chưa deploy**, cổng giờ chặn |

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«① Duyệt truy tiếp CẢ HAI: con số 9 ms chưa giải thích + khâu rút số (33.685 token không cho ra
> số nào). ② `FU-419` lối (a): dòng «D-1 cross-region tail pool» chuyển thành GHI SỐ ĐẾM, bỏ danh
> sách. Ghi nhận điều kiện đi kèm: CẤM hứa nó làm tăng độ trúng (FU-316 đã đo: 20,2% vs nền 21,0%,
> z=−1,01 — không neo).»*

> *«Deploy CHỈ SAU 18:31 (kết quả ba miền đã về đủ — không làm lai ngày 23/08; 24/08 là ngày sạch
> đầu tiên của bản mới)»*

> *«Nếu payload không còn lưu: ghi thẳng «không kiểm được» (không đoán) + đề xuất THIẾT KẾ lưu raw
> response cho các lượt rỗng từ nay — chờ owner duyệt, cấm tự vá.»*

---

## 3. Đào bới / phát hiện

### 3.1 · Con số **9 ms** — HAI ĐỒNG HỒ trong cùng một vòng lặp

Trong **toàn bộ mã sống** chỉ có **một** nơi ghi `latency_ms` cho `component='official_ai_predict'`.
Đường ghi đầy đủ, năm mắt xích:

```
:4546  _model_call_start = _stage_time.time()   ← đồng hồ A: lúc VÒNG LẶP TUẦN TỰ tới lượt model
:4557  start_time = _pre["start_time"]          ← đồng hồ B: lúc BỂ SONG SONG thật sự gọi
                                                  ⚠ CHỈ start_time được sửa. _model_call_start KHÔNG.
:4375  _model_elapsed = _stage_time.time() - model_call_start
:4380  _persist_official_diagnostic_empty_row(..., elapsed_sec=_model_elapsed)
:4303  latency_ms = int(elapsed_sec * 1000)
:6774  ghi vào runtime_reliability_model_daily
```

Khi `AI_PARALLEL_ENABLE=1`, bể nạp lượt gọi **trước** khi vòng lặp tuần tự tới lượt. Dòng thời gian
thật của `glm-5.1` (thứ **7/8**, nằm hàng đợi):

```
05:16:04   rolling nạp vào bể
05:17:26   lượt gọi XONG           (trace: latency_seconds = 79,36)
05:17:43   vòng lặp MỚI TỚI LƯỢT   ⇒ future.result() trả về TỨC THÌ ⇒ _model_elapsed ≈ 9 ms
```

**Và đây là chỗ đổi kết luận — KHÔNG phải ca cá biệt:**

> Cùng lượt chạy đó, **5 model khác** cũng bị ghi **0,0–0,4 giây** trong khi trace ghi
> **12,7–86,0 giây**.

Tức **mọi phép đo độ trễ đọc từ `runtime_reliability_model_daily` đều không đáng tin khi bể song
song bật**. Và `FU-283` — việc canh độ trễ model — **đang đọc đúng trường đó**. Một trường sai theo
hướng **nhỏ đi** thì cảnh báo *«model chậm»* **không bao giờ nổ**.

**Nguồn đúng:** `scheduler.py` trên VPS **trùng md5 với local** (`ae9db52a…`) ⇒ đo đúng mã production
(`RM-13`).

**Ghi rõ để không lẫn:** `EMPTY_PROVIDER_OUTPUT` là **lỗi THẬT và RIÊNG BIỆT** — dict kết quả không
có khoá `prediction` dù model đã trả 33.685 token. Hai chuyện khác nhau, đừng gộp.

### 3.2 · Payload — **KHÔNG CÒN**, và chỗ vứt nó mới là phát hiện

Owner hỏi *«model trả về định dạng gì, parser kỳ vọng gì, vì sao không khớp»*.
**Trả lời: KHÔNG KIỂM ĐƯỢC.** Đã kiểm hết những chỗ sau:

| đã kiểm | kết quả |
|---|---|
| **253 bảng** DB production trên VPS | chuỗi dài nhất cho bộ ba đó là `analysis_text` **621 ký tự** — chính là **bản chẩn đoán placeholder** |
| `prediction_trace.jsonl` (5.774 dòng, **57 khoá**) | **không khoá nào** chứa nội dung thô |
| `journalctl` | **có đủ** ngày 18/08 (**959 dòng**) nhưng **0 dòng** nhắc `glm` — journal chỉ nhận log của module `logging`; `print()` của ứng dụng **không tới journal** |

**Chỗ vứt, có tệp:dòng:**

```python
scheduler.py:4242  def _persist_official_diagnostic_empty_row(ai_model, outcome_status,
                       error_message, elapsed_sec=0.0, result_payload=None)
scheduler.py:4256      "result_keys": sorted(result_payload.keys())   ← CHỈ TÊN KHOÁ, không giá trị
```

**ĐIỂM ĐAU NHẤT.** Khoá `_native_reasoning_json` **CÓ MẶT** trong danh sách tên khoá được ghi lại —
nghĩa là **tới 3.000 ký tự suy luận thật của model đang nằm trong bộ nhớ ngay tại thời điểm đó**
(`gpt_analyzer.py:6748` đã cắt sẵn `_cap_text[:3000]`), và mã **chỉ ghi TÊN KHOÁ rồi vứt nội dung đi**.

**Và đó là chênh lệch CỐ Ý, không phải lỗi ngẫu nhiên:**

| đường | ghi `reasoning_json`? |
|---|---|
| **thành công** — `scheduler.py:4470` | **CÓ**: `reasoning_json=result.get('_native_reasoning_json')` |
| **rỗng** — `_persist_official_diagnostic_empty_row` | **KHÔNG** |

> **Đường rỗng vứt đúng thứ duy nhất giải thích được vì sao nó rỗng.**

Mỗi lượt rỗng là một lần mất bằng chứng **vĩnh viễn**. Tỉ lệ rỗng đo được: **2,26%** ≈ **2 lần mỗi
90 lượt**.

*(Ghi thêm: câu trả lời thô **có** được giữ **500 ký tự** — nhưng chỉ trên nhánh `PARSE_ERROR`
(`gpt_analyzer.py:6815-6819`), **không phải** nhánh của ca này.)*

---

## 4. Hướng xử lý và vì sao chọn

### 4.1 · `FU-425` — hai đồng hồ (thiết kế, **chưa vá**)

| # | việc | vì sao |
|---|---|---|
| ① | dùng **một** mốc duy nhất — lấy `_pre["start_time"]` khi lượt gọi đến từ bể, y như `start_time` đã làm ở `:4557` | sửa đúng gốc, không vá triệu chứng |
| ② | thêm **phép kiểm chéo**: `latency_ms` lệch quá 20% so với `latency_seconds` của trace ⇒ ghi cờ `LECH_DONG_HO` | **không có ② thì lần sau lệch kiểu khác lại im lặng đúng như lần này** |
| ③ | thử chặn hai chiều: lượt đến từ bể ⇒ độ trễ phải khớp trace; lượt tuần tự ⇒ không đổi | `RM-15` |

**Cấm:** chỉ sửa con số rồi bỏ ②.

### 4.2 · `FU-426` — đường rỗng giữ bằng chứng (thiết kế, **chưa vá**)

| lối | **được** | **mất** |
|---|---|---|
| **ghi `reasoning_json` cho đường rỗng — đề xuất** | lần rỗng sau **chẩn đoán được ngay trong ngày** thay vì mất vĩnh viễn. Nội dung **đã có sẵn trong bộ nhớ** ⇒ **không tốn thêm một lượt gọi nào** | thêm ~3–5 KB mỗi lượt rỗng ≈ **2 lượt/90** — không đáng kể |
| lưu cho **mọi** lượt | đầy đủ nhất | **đổi một vấn đề nhỏ lấy một vấn đề dung lượng lớn** — không đề xuất |
| để nguyên | 0 rủi ro | mỗi lượt rỗng lại mất bằng chứng, và câu hỏi hôm nay sẽ lặp lại y hệt |

Kèm: `raw_response[:2000]` **chỉ cho lượt rỗng**, giữ **90 ngày** rồi xoá, ghi rõ trong tài liệu.

---

## 5. Đã làm gì

### 5.1 · Hai phép truy — chỉ-đọc, không sửa một dòng mã nào

Kết quả ở §3.1 và §3.2. Mọi số đo **trên VPS** (`RM-13`), mọi khẳng định kèm **tệp:dòng**.

### 5.2 · Hai mục theo dõi mới

`FU-425` · `SC2608` · hạn **26/08** — hai đồng hồ.
`FU-426` · `SC2608-1` · hạn **26/08** — đường rỗng vứt bằng chứng.

### 5.3 · `FU-419` lối (a) — vá xong, **CHƯA DEPLOY**

```
TRƯỚC:  - D-1 cross-region tail pool: 00, 01, 03, 04, 05, 06, 07, 09, 10, 11, 12, 13 ...
SAU:    - D-1 cross-region tail pool: 77 distinct tails
```

Dump từ **hàm đang serve trên VPS** (`RM-14`):

| miền | TRƯỚC | SAU |
|---|---|---|
| MN | 11.579 kt · `4c6e54fe321198e7` | `d1f5e4a6f8b30cd6` |
| MT | 11.422 kt · `cbb156e3332d6e27` | `84f60682898ebbe9` |
| MB | 17.194 kt · `aeced4ce9cdc1c43` | `426b4e1b5513fae7` |

**Diff: ĐÚNG 1 DÒNG đổi ở cả ba miền** (2 dòng diff = 1 xoá + 1 thêm). **Tái lập:** gọi lại cùng
đầu vào ⇒ SHA256 **khớp cả ba** (`RM-11`). Nhãn `CTX-18.4 → CTX-18.5`.

> **Một vấp đáng ghi:** bản dump đầu dùng ngày **24/08** và cho ra **dòng D-1 RỖNG** — vì D-1 của
> 24/08 là 23/08, **chưa xổ**. Đã đổi sang ngày **23/08** (D-1 = 22/08 đã có kết quả) thay vì báo
> một con số vô nghĩa.

**CHƯA DEPLOY, và cổng giờ nằm trong mã chứ không trong đầu.** `_v11105_deploy_fu419.py` **từ chối
chạy** trước 18:31 giờ VN — đã thử lúc **04:02** ⇒ **từ chối đúng**. Chín bước:

| bước | nội dung |
|---|---|
| 1 | cổng giờ ≥ 18:31 VN — **đọc giờ TỪ VPS**; không đọc được ⇒ **từ chối** (cấm đoán giờ) |
| 2 | **cả ba miền** phải có kết quả hôm nay — thiếu một miền là deploy làm **lai** ngày đó |
| 3–6 | backup · md5 TRƯỚC · chép · md5 SAU **khớp từng byte** |
| 7 | `py_compile` **trên VPS TRƯỚC restart** — hỏng ⇒ **khôi phục backup ngay** |
| 8 | restart · **so PID** · smoke `health=200`/`admin=401` · đếm lỗi 3 phút |
| 9 | **4 bảng khoá PRE=POST** + dump prompt xác nhận dòng mới |

### 5.4 · Ghi trung thực — điều kiện owner kèm theo

Mục đích của `FU-419` là **prompt thôi nói sai về chính nó**. **KHÔNG kỳ vọng bất kỳ công bố nào về
độ trúng** — `FU-316` (V11076) đã đo, có đăng ký ngưỡng **trước** khi chạy: model chọn đuôi thấp
**20,2%** so với nền **21,0%**, `z = −1,01` ⇒ **KHÔNG NEO**. Điều này ghi thẳng **trong mã**, trong
`CHANGELOG` và ở đây: **cấm mọi báo cáo sau này viện dòng này làm nguyên nhân của thay đổi độ trúng.**

**Chưa đụng tới:** dòng chị em `{region}(D) tails already spent` (`tails[:12]`, `:6013`) **cùng họ
lỗi** — owner khoá *«một dòng, không đụng gì khác»* nên để nguyên. **Vẫn còn treo.**

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v11062_nang_version.py --kiem` | `NANG_VERSION_V11062=ĐẠT` — bốn mặt đi cùng nhau |
| `_v11050_kiem_cong.py` (K1) | **8/8** cổng chạy được |
| `_v11105_deploy_fu419.py` (cổng giờ) | chạy lúc 04:02 ⇒ **từ chối đúng** |
| dump prompt TRƯỚC/SAU | diff **1 dòng** × 3 miền · tái lập **SHA256 khớp** cả ba |
| md5 nguồn đo | `scheduler.py` VPS = local (`ae9db52a…`) |

**Không cổng nào bị bỏ qua bằng cờ.** Không sửa production, không deploy, không restart, không
đụng DB.

---

## 7. Vướng vấp

1. **Bản dump đầu cho ra dòng D-1 rỗng** vì chọn ngày 24/08 (D-1 chưa xổ). Bắt được vì **đọc kỹ
   con số thay vì chép nó vào báo cáo**. Đã đổi ngày.

2. **Phiên trước bị ngắt giữa chừng**, hai trong bốn làn đào chưa xong. Nhưng **hai làn owner ký
   đích danh đã xong** và kết quả còn nguyên trong nhật ký — nối lại lấy được bản đã lưu, không
   phải chạy lại từ đầu.

3. **Cổng `§63` chặn commit hai lần** trong phiên vì `V11105` chưa có dòng `HISTORY`. Đúng thiết kế
   — nhưng nó cho thấy một thói quen cần đổi: **nâng version sớm hơn**, đừng để dồn tới cuối.

---

## 8. Gỡ về

| việc | lệnh |
|---|---|
| bản vá `FU-419` | `git revert <sha>` · backup `backups/gpt_analyzer.py.pre_v11105` — **chưa lên VPS nên không có gì để gỡ ở đó** |
| bộ deploy | `git revert <sha>` — chỉ là công cụ, **chưa chạy deploy nào** |
| hai mục theo dõi | `git revert <sha>` |

---

## 9. Theo dõi tiếp

| mã | việc | hạn |
|---|---|---|
| `FU-419` | **deploy sau 18:31 ngày 23/08** — chạy `_v11105_deploy_fu419.py --that`; lượt 05:00 ngày **24/08** phải đóng dấu `CTX-18.5` mới được ghi `RUNTIME_PROVEN` | **23/08 tối** |
| **`FU-425`** · `SC2608` | hai đồng hồ — vá **kèm phép kiểm chéo**, cấm chỉ sửa con số | 26/08 |
| **`FU-426`** · `SC2608-1` | đường rỗng ghi `reasoning_json` như đường thành công | 26/08 |
| `FU-421` | vá **bốn việc cùng lúc** theo thiết kế đã soạn | 24/08 |
| — | đọc lane T-B theo **giao thức 6 bước** | 24/08 |
| — | dòng chị em `tails[:12]` (`:6013`) **vẫn còn treo** | chờ owner |
| — | 27/08 quyết **DỪNG** cho `gpt-5.5` và `qwen3-max-thinking` | 27/08 |

---

## §62 (A60) — BA LỚP NGUỒN

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| **23/08 03:44** | *«Duyệt truy tiếp CẢ HAI: con số 9 ms chưa giải thích + khâu rút số (33.685 token không cho ra số nào)»* |
| **23/08 03:50** | *«`FU-419` lối (a)… CẤM hứa nó làm tăng độ trúng (FU-316 đã đo: 20,2% vs nền 21,0%, z=−1,01 — không neo)»* |
| **23/08** | *«Deploy CHỈ SAU 18:31… 24/08 là ngày sạch đầu tiên của bản mới»* |
| **23/08** | *«Nếu payload không còn lưu: ghi thẳng «không kiểm được» (không đoán)»* |

### `CODE_DID`

| việc | bằng chứng |
|---|---|
| gốc 9 ms | `scheduler.py:4546` vs `:4557` — chỉ `start_time` được sửa theo bể; dòng thời gian glm-5.1: nạp `05:16:04` · xong `05:17:26` · vòng lặp tới lượt `05:17:43` |
| không phải ca cá biệt | **5 model khác** cùng lượt chạy ghi 0,0–0,4 s trong khi trace ghi 12,7–86,0 s |
| payload bị vứt | `scheduler.py:4256` chỉ lưu `sorted(result_payload.keys())`; `_native_reasoning_json` **có mặt** trong danh sách đó |
| chênh lệch cố ý | `:4470` đường thành công **có** ghi `reasoning_json`; đường rỗng **không** |
| đã kiểm hết mọi nơi | 253 bảng DB · trace 5.774 dòng/57 khoá · journal 959 dòng ngày 18/08, **0** dòng nhắc `glm` |
| `FU-419` | diff **1 dòng** × 3 miền · SHA256 tái lập khớp cả ba · `CTX-18.5` |
| cổng giờ deploy | chạy 04:02 ⇒ **từ chối** |

### `DOC_SAID` — chỗ tài liệu **lệch** với mã

| lệch | chi tiết |
|---|---|
| `runtime_reliability_model_daily.latency_ms` ≠ thực tế | trường này **không đo khoảng mà tên nó gợi ý** khi bể song song bật — chưa tài liệu nào ghi điều đó |
| `_persist_official_diagnostic_empty_row` ≠ tên gọi | tên nói *«persist diagnostic»* nhưng nó **vứt** phần chẩn đoán được nhất (`reasoning`) |
| `docs/FOLLOW_UP_TRACKER.md` ≠ sổ quyết định | vẫn ghi `FU-216` hạn 09/08, `FU-231`/`FU-226` hạn 10/08 — chưa theo `QD-045` |

---

**TanPhatAI cần làm:** cập nhật `docs/FOLLOW_UP_TRACKER.md` — **`FU-425`** (hai đồng hồ, hạn 26/08) và **`FU-426`** (đường rỗng vứt bằng chứng, hạn 26/08), cả hai **đã đo ra gốc, chưa vá**, thiết kế đã soạn và **chờ owner duyệt vá**; `FU-419` chuyển sang **đã vá, CHƯA deploy** (`CODE_PUSHED`); theo dõi ba việc: ① **tối 23/08 sau 18:31** chạy `_v11105_deploy_fu419.py --that` rồi **24/08** kiểm lượt 05:00 có đóng dấu `CTX-18.5` không — **cấm ghi `RUNTIME_PROVEN` trước đó**, ② **`FU-425` là việc gấp hơn vẻ ngoài**: `FU-283` đang canh độ trễ model bằng đúng trường bị sai theo hướng nhỏ đi, nên cảnh báo *«model chậm»* hiện **không bao giờ nổ**, ③ dòng chị em `tails[:12]` (`gpt_analyzer.py:6013`) **cùng họ lỗi với `FU-419` nhưng chưa được ký** — cần owner quyết có vá cùng đợt không.
