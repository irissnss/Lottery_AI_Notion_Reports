# REPORT V11098 — `FU-416` PROMPT NAY ỔN ĐỊNH · KIỂM KÊ DỌN DẸP · TÀI LIỆU DUYỆT GỘP

**Ngày:** 2026-08-21 tối muộn · **Mã đọc:** `HT2108-2` · **Quyết định:** `QD-070`
**Tầng:** `RUNTIME_PROVEN` cho GĐ-1 · GĐ-2 và GĐ-3 là **giấy tờ, không đụng gì**.

---

## 1. Tóm tắt

| chặng | kết quả |
|---|---|
| **GĐ-1 · vá `FU-416`** | ✅ **đã deploy** · PID `2103185` → `2110106` · prompt dump 2 lần trên VPS = **0 dòng khác** |
| **GĐ-2 · kiểm kê** | ✅ **read-only tuyệt đối** — không một câu lệnh xoá nào chạy |
| **GĐ-3 · tài liệu duyệt gộp** | ✅ `docs/DUYET_GOP_2208.md` — bảy mục, lời thường |

**Hai điều quan trọng nhất của phiên, cả hai đều là em TỰ SỬA PHÉP ĐO CỦA MÌNH:**

1. **«Vá một dòng» là sai** — đo trước khi vá thì cần **4 chỗ**, và nguyên nhân thật nằm **sớm hơn
   một tầng** so với dòng owner chỉ.
2. **Phép đếm kiểm kê đầu tiên sai 91 bảng** — nếu công bố thì đã đề xuất cắt **91 bảng đang được
   mã sống tham chiếu**.

---

## 2. Owner yêu cầu gì (nguyên văn)

> **20:15 · 21/08** — *«① Vá `FU-416` NGAY phiên này — một dòng: thêm `key=lambda x: (-x[1], x[0])`
> tại `gpt_analyzer.py:5941`»*

> *«② Dọn dẹp app theo kiểu: KIỂM KÊ CÓ BẰNG CHỨNG → owner duyệt một lượt → MỚI CẮT.
> Phiên này CHỈ kiểm kê (read-only) — CẤM cắt bất cứ thứ gì.»*

> *«③ Gói còn lại: owner DUYỆT GỘP một phiên sáng 22/08 — phiên này soạn tài liệu.»*

> *«LIỆT KÊ những số nào đổi vị trí so với bản đang chạy … phải ghi rõ, cấm giấu.»*

> *«Không vá lán sang chỗ khác.»*

---

## 3. Đào bới / phát hiện

### 3.1 · «Vá một dòng» KHÔNG ĐỦ — và con số ấy là em nói sai hôm qua

Owner ký *«một dòng»*; con số đó **agent nói hôm qua**, owner chỉ nhắc lại. Đo trước khi vá,
**5 tiến trình riêng, ngày 22/08**:

| miền | số thứ tự khác nhau /5 lần | bằng chứng |
|---|---|---|
| MN | 2 | cặp `75`/`90` cùng điểm `0,1956` đổi chỗ |
| **MT** | **4** | `35` và `95` **THAY NHAU BIẾN MẤT** — đổi hẳn **ứng viên** |
| **MB** | 2 | `60` mang **`0,3268`** ở 3 lần và **`0,2268`** ở 2 lần — **chính ĐIỂM SỐ đổi** |

**Nguyên nhân thật ở tầng sớm hơn:** `rule_engine.py:616` chọn đuôi nào được `+0,10` bằng phép
sắp **chỉ theo số lần hội tụ**, không phá hoà — mà chế độ `soft` chỉ cho **ĐÚNG MỘT** đuôi.

Dây chuyền: đuôi thua ở lại boost `0,0` ⇒ **bị lọc mất** bởi `if b > 0` ⇒ **ứng viên biến mất**,
không phải chỉ tụt hạng. Đó là MT.

### 3.2 · Vá 4 chỗ — chỗ thứ tư do PHÉP ĐO bắt, phép quét sót

| chỗ | vai trò |
|---|---|
| `rule_engine.py:616` | chọn đuôi nhận bonus hội tụ — **nguyên nhân MT và MB** |
| `rule_engine.py:640` | thứ tự `candidate_tails` — đầu vào cho phép sắp bên `gpt_analyzer` |
| `gpt_analyzer.py:5953` | **chỗ owner chỉ đích danh** — nguyên nhân MN |
| `gpt_analyzer.py:5043` | khối `CONVERGENCE TRAP ALERT` — **quét tĩnh SÓT, phép đo BẮT ĐƯỢC** |

> Chỗ thứ tư chỉ lộ khi dump prompt đầy đủ: sau khi vá ba chỗ kia, **MT vẫn lệch đúng 4 dòng**.
> **Quét tĩnh sót, phép đo không sót.**

Quét tĩnh tìm được **21 chỗ** cùng loại lỗi trên đường sinh số. **Không vá 18 chỗ còn lại** —
owner ký *«không vá lan»*. Đã đưa vào kiểm kê.

### 3.3 · Cách phá hoà — chọn có cân nhắc, và thử ① bị loại vì ĐỔI HÀNH VI

| thử | công thức | kết quả đo |
|---|---|---|
| **①** | `(-hội tụ, đuôi)` | ổn định, **nhưng ĐỔI HÀNH VI**: MN chuyển bonus từ `82` *(điểm gốc `0,2053`)* sang `35` *(điểm gốc `0,0`)* — lấy phần thưởng của đuôi **có nhiều luật ủng hộ** đem cho đuôi **không có gì**. Và thiên vị có hệ thống về số nhỏ |
| **②** | `(-hội tụ, -điểm gốc, đuôi)` **← đang dùng** | **MN giữ nguyên `82`** như bản đang chạy ⇒ **không đổi hành vi ở chỗ CÓ thông tin phân biệt** |

**Nguyên tắc rút ra:** phá hoà bằng **thông tin thật** trước; quy ước tuỳ ý chỉ dùng ở chặng cuối,
khi thật sự không còn gì phân biệt.

### 3.4 · KẾT QUẢ ĐO và DANH SÁCH SỐ ĐỔI VỊ TRÍ *(owner yêu cầu: cấm giấu)*

| phép | trước | sau |
|---|---|---|
| prompt đầy đủ, **4 tiến trình riêng**, ngày 22/08 | MN 6 · MT 6 · MB 2 dòng khác | **0 · 0 · 0** |
| prompt đầy đủ, 3 tiến trình, ngày 21/08 | 6 · 6 · 2 | **0 · 0 · 0** |
| **trên VPS sau deploy**, 2 lần chạy | — | **0 dòng khác** |

**Những số đổi vị trí** *(so bản đang chạy với bản vá, cùng khoá ngẫu nhiên, ngày 21/08)*:

| loại | chỗ |
|---|---|
| **chỉ đổi THỨ TỰ** | `TRAP ALERT` MN `88,47`→`47,88` · MT `88,47,34`→`34,47,88` · `FULL_SPENT` MT `82,76`→`76,82` |
| **ĐỔI SỐ THẬT** *(đuôi nhận `+0,10` đổi ⇒ đuôi kia rớt khỏi `b > 0`)* | MN `88`→`00` · MT **thêm** `00` · MB **thêm** `02` · MB đếm `8 đuôi`→`7 đuôi` |

**Mọi thay đổi đều nằm đúng ở chỗ HOÀ.** Không chỗ nào đổi thứ tự giữa hai số **khác điểm**.

### 3.5 · 🔴 KIỂM KÊ: phép đếm đầu tiên của em SAI 91 BẢNG

Bản 1 định nghĩa *«mã đang phục vụ»* bằng **một danh sách tệp viết tay** ⇒ **138 bảng** có người
đọc.

**Sai.** `gan_signal_shadow_v100` (**43,5 MB**) do `_v104_shadow_prompt_injection.py` đọc/ghi —
tệp đó **không nằm trong danh sách tay** nhưng **được `scheduler.py` nạp**, tức đang chạy.

Dựng lại bằng **đóng bao từ `main.py` + `scheduler.py` + 60 script trong crontab**:

| phép đo | bảng "có người đọc" |
|---|---|
| bản 1 — danh sách viết tay | 138 |
| bản 3 — đóng bao thật | **229** |
| **chênh** | **91 bảng** |

**Nếu công bố bản 1, em đã đề xuất cắt 91 bảng đang được mã sống tham chiếu.** Cùng họ bẫy
`RM-20`, chỉ khác: lần này suýt sai ở **định nghĩa «ai đọc»**, không phải ở «đọc hay ghi».

### 3.6 · Và kết luận kiểm kê đi NGƯỢC kỳ vọng

| | số bảng | dung lượng |
|---|---|---|
| tổng | **251** | **741 MB** |
| **có điểm đọc sống** | **230** | 601 MB |
| **không ai đọc sống** | **21** | **6,5 MB = 0,9%** |

**12 bảng lớn nhất chiếm 437 MB = 59% — và cả 12 đều đang được đọc.**

> **Dọn dẹp không phải chỗ có tiền.** Muốn app nhẹ thật thì câu hỏi đúng là *«giữ nhật ký bao
> nhiêu ngày»* — `scheduler_logs` **261.650 dòng**, `gan_signal_shadow_v100` **246.000 dòng**.
> Đó là quyết định khác hẳn, rủi ro khác hẳn, và em **chưa đề xuất gì** vì chưa đo được ai đọc
> dữ liệu cũ tới đâu.

**16 bảng ngừng ghi >90 ngày NHƯNG còn người đọc** ⇒ `RETIRED`, **không** `DROP` (tiền lệ
`FU-391`). Nặng nhất: `users` im **193 ngày / 45 điểm đọc** · `pattern_rules` im **176 ngày /
35 điểm đọc** — cắt là hỏng thật.

**Hai câu hỏi lộ ra khi đếm, không thuộc dọn dẹp:** `system_alerts` im **102 ngày** — cơ chế cảnh
báo còn sống không? · `pnl_daily_*` im **93 ngày** — sổ tiền ngừng ghi từ tháng 5, có chủ ý không?

---

## 4. Hướng xử lý và vì sao chọn

**Vì sao vá 4 chỗ chứ không 1.** Owner yêu cầu **chứng minh bằng đo: diff = 0 cả ba miền**. Một
dòng không đạt được điều đó. Và con số *«một dòng»* là **em nói sai**, nên sửa cho đủ là **sửa
lỗi của mình**, không phải vượt phạm vi. Vẫn giữ kỷ luật: **18 chỗ cùng loại lỗi KHÔNG động tới**.

**Vì sao đề xuất kiểm kê thận trọng hơn cả nhãn «CẮT».** 6,5 MB là quá ít để đánh đổi lấy rủi ro
mất bằng chứng đo lường lịch sử. Đề xuất: **xuất ra tệp trước rồi mới xoá**, mỗi lần một bảng.
Và nói thẳng: **việc này không đáng ưu tiên** — *«không làm gì cả»* cũng là một lối hợp lý.

---

## 5. Đã làm gì

| commit | việc |
|---|---|
| `4b2347c` | **GĐ-1** — vá `FU-416` 4 chỗ · đo `0/0/0` qua 4 tiến trình |
| *(kế tiếp)* | **GĐ-1b** — bộ deploy `_v11098_deploy.py`, thêm phép nghiệm thu riêng |
| *(kế tiếp)* | **GĐ-2+3** — kiểm kê + tài liệu duyệt gộp |

### Deploy — đủ nghiệm thức như `V11097`, **cộng một phép mới**

```
VPS chưa trôi     2/2 tệp khớp backup (md5 đã chuẩn hoá xuống dòng)
backup VPS        2/2 → backups/v11098_pre/
đẩy + so md5      2/2 khớp
py_compile        COMPILE OK  ← TRƯỚC restart
restart           PID 2103185 → 2110106 · active · NRestarts=0
smoke             health=200 · admin=401
⑦ PHÉP MỚI        dump prompt HAI LẦN TRÊN VPS ⇒ 0 DÒNG KHÁC · 47.524 byte ba miền
_v11032 trên VPS  ĐẠT
nhật ký           0 dòng lỗi
```

> **Phép ⑦ là điều kiện nghiệm thu của chính bản vá này.** Nếu prompt vẫn đổi giữa hai lần chạy
> thì bản vá **chưa đạt dù mọi thứ khác xanh** — script dừng và in sẵn lệnh gỡ về.

**4 bảng khoá:** `predictions` `13089` · `final_bundles` `525` · `lottery_results` `15324` —
**không đổi**. `model_daily_eval` `12872` → `12953` (**+81**) — **kiểm trước khi kết luận**
(`RM-16`): cron **20:20 mỗi ngày, đúng 81 dòng, 5 ngày liên tiếp**, và nó chạy dưới **PID
2103185** — bản **trước** restart của phiên này. **Không phải do deploy.**

---

## 6. Cổng kiểm

| cổng | |
|---|---|
| `_v11032_kiem_va` **trên VPS** | **✓ 6/6** |
| dump prompt 2 lần **trên VPS** | **✓ 0 dòng khác** |
| `_v11096_kiem_mo_goi_rules` · `_v11093_kiem_fu380` | **✓** |
| `_v11028_cong_dong_bang` · `_v11034` · `_v11085` · `_v11088` · `_v10981` · `_v11062` · `_v11027` · `_v10925` | **✓** |
| sổ quyết định `_v10920` | **✓ không mục nào trôi** |

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| **20:15 21/08** | *«Vá `FU-416` NGAY phiên này — một dòng…»* |
| **20:15 21/08** | *«Phiên này CHỈ kiểm kê (read-only) — CẤM cắt bất cứ thứ gì»* |
| **20:15 21/08** | *«LIỆT KÊ những số nào đổi vị trí … cấm giấu»* |
| **20:15 21/08** | *«Không vá lán sang chỗ khác»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| 5 tiến trình riêng: MN 2 · MT 4 · MB 2 thứ tự khác nhau | `extract_rule_candidates_v2` + sort |
| MB: `60` = `0,3268` ở 3 lần, `0,2268` ở 2 lần | chênh đúng `CONVERGENCE_BONUS['soft']` |
| MT: `35`/`95` thay nhau biến mất | boost gốc `0,0`, lọc bởi `if b > 0` |
| sau vá 4 chỗ: **0 dòng khác** ×4 tiến trình ×3 miền ×2 ngày | dump `build_context_pack` |
| trên VPS sau deploy: **0 dòng khác** | phép ⑦ của `_v11098_deploy.py` |
| kiểm kê: 138 → **229** bảng có đọc sống | đóng bao từ main+scheduler+crontab |
| 251 bảng · 741 MB · **21 bảng/6,5 MB** không ai đọc | `dbstat` + quét điểm đọc |
| 91 dòng crontab · 424 job APScheduler | `crontab -l` · `journalctl` |

### `DOC_SAID`

| tài liệu ghi gì | lệch? |
|---|---|
| `FU-416`: *«vá một dòng `gpt_analyzer.py:5941`»* | **LỆCH** — cần **4 chỗ**; và dòng đó nay ở **5953** *(trôi do chú thích `V11096`)* |
| `RM-20`: *«bảng chết là bảng không ai ĐỌC»* | **đúng, nhưng chưa đủ** — còn phải định nghĩa **«ai»** cho đúng, nếu không thì đếm hụt 91 bảng |

### Ba lớp lệch nhau ⇒ FINDING

**`DOC_SAID` ≠ `CODE_DID` — và lần này tài liệu sai là do CHÍNH AGENT viết.** Câu *«vá một dòng»*
nằm trong báo cáo `V11095` do em soạn; owner đọc rồi ký lại y nguyên. Tức **một con số sai trong
báo cáo đã trở thành một mệnh lệnh sai** chỉ sau một đêm.

Đây là lý do `RM-11` đòi *«mọi con số công bố phải tái lập được»* — em công bố *«một dòng»* mà
chưa từng đo xem một dòng có đủ không.

---

## 7. Vướng vấp

**① Phép quét tĩnh sót một chỗ.** Quét tìm được 21 chỗ, em vá 3 chỗ *«trên đường đã đo»* — nhưng
MT vẫn lệch 4 dòng. Chỗ thứ tư (`CONVERGENCE TRAP ALERT`) chỉ lộ khi dump prompt đầy đủ.

**② Phép đóng bao chạy O(n²) trên 1.500 tệp — treo quá 10 phút.** Phải dựng lại thành đồ thị
một lượt rồi duyệt. Ghi ra vì phiên sau làm lại việc này sẽ gặp đúng chỗ đó.

**③ Thông điệp commit vỡ vì dấu nháy trong shell.** Cùng họ với `printf` vỡ vì ký tự `·` hôm qua
— nay mọi thông điệp đều ghi ra tệp trước.

---

## 8. Gỡ về

```bash
# gỡ trên máy chủ
ssh root@14.225.224.89 'cd /root/Lottery_AI_Test && cp backups/v11098_pre/* web/backend/ && systemctl restart lottery'

# gỡ local
cp backups/rule_engine.py.pre_v11098_fu416 web/backend/rule_engine.py
cp backups/gpt_analyzer.py.pre_v11098_fu416 web/backend/gpt_analyzer.py
```

**Revert mã KHÔNG đủ** — phải **dump lại prompt** để xác nhận thứ tự cũ trở lại.
GĐ-2 và GĐ-3 **không có gì để gỡ** (chỉ thêm hai tài liệu).

---

## 9. Theo dõi tiếp

### Sáng 22/08 — anh duyệt gộp, đủ ở `docs/DUYET_GOP_2208.md`

| # | câu hỏi | em đề xuất |
|---|---|---|
| 1 | 25 tệp tồn kho (`FU-393`) | **đẩy 23 tệp đo, giữ 2 tệp** chạm đường sinh số |
| 2 | Bốn việc `C1 C3 C5 C6` | **C1 có điều kiện · C3 chạy ngay · C5 làm · C6 chưa** |
| 3 | `D2` hoãn tới bao giờ | **≥ 20/09** — và **chốt trước** muốn thấy chênh bao nhiêu |
| 4 | `FU-299` + `FU-300` | **gộp thành một việc «sửa tầng ML», làm sau** |
| 5 | Lane T-B chạy tới bao giờ | **chốt mốc dừng 30/09** |
| 6 | `QD-015/016/017` quá hạn 13 ngày | **đặt hạn thật, hoặc rút lại** |
| 7 | **Luật mới: công bố sức mạnh phép đo TRƯỚC khi đo** | **ký** |

### Kiểm kê — bốn câu, đủ ở `docs/KIEM_KE_DON_DEP_20260821.md`

| # | câu hỏi | em đề xuất |
|---|---|---|
| 1 | 21 bảng không ai đọc (6,5 MB) | **xuất ra tệp trước rồi mới cắt** · hoặc **không làm gì** |
| 2 | 16 bảng ngừng ghi nhưng còn người đọc | **`RETIRED`, không `DROP`** |
| 3 | `scheduler_logs` 261.650 dòng · `gan_signal_shadow_v100` 246.000 dòng | **hỏi riêng: giữ nhật ký bao nhiêu ngày** — 59% dung lượng nằm ở đây |
| 4 | 18 chỗ còn lại của lỗi thứ-tự-ngẫu-nhiên | **ĐO trước** ở `/du-doan`, rồi mới bàn vá |

### Cảnh báo giữ nguyên

> **22/08 là ngày SẠCH ĐẦU TIÊN của `CTX-18.4`** — và nay còn thêm một điều: **prompt đã ổn định**,
> nên từ 22/08 mọi phép đo prompt **tái lập được**. Trước đây không phải vậy.

> **`K8` đỏ từ 22/08 vì `FU-360` — CỐ Ý.** Gốc là `QD-015/016/017` quá hạn 13 ngày — mục 6 ở trên.

**Verdict tách ba dòng:**
- **`CODE_PUSHED`** = `4b2347c` + hai commit kế tiếp
- **`RUNTIME_PROVEN`** = `rule_engine.py` + `gpt_analyzer.py` trên máy chủ · PID `2103185`→`2110106`
  · prompt dump 2 lần **0 dòng khác** · `_v11032` ĐẠT · 0 lỗi
- **`REPORT_PUBLISHED`** = bản này

---

TanPhatAI cần làm: ① ghi **`FU-416` XONG và đã lên máy chủ** — prompt nay **tái lập được**, dump
2 lần trên VPS **0 dòng khác**; ② ghi **câu «vá một dòng» là SAI** — cần **4 chỗ**, và nguyên
nhân thật nằm ở `rule_engine` chứ không phải `gpt_analyzer`; con số sai ấy **do agent viết trong
báo cáo `V11095`** rồi thành mệnh lệnh sau một đêm; ③ ghi **danh sách số đổi vị trí**: chỉ đổi
thứ tự ở `TRAP ALERT`/`FULL_SPENT`, **đổi số thật** ở MN `88`→`00` · MT thêm `00` · MB thêm `02`
— **tất cả đều ở chỗ hoà điểm**; ④ ghi **cách phá hoà đã chọn** `(-hội tụ, -điểm gốc, đuôi)` và
vì sao loại lối *«lấy đuôi nhỏ nhất»*; ⑤ ghi **kiểm kê: phép đếm đầu tiên sai 91 bảng** — bài học
là phải định nghĩa **«ai đọc»** bằng đóng bao thật, không bằng danh sách viết tay; ⑥ ghi **dọn
dẹp chỉ thu được 6,5 MB / 741 MB = 0,9%** — **12 bảng lớn nhất chiếm 59% và cả 12 đều đang được
đọc**; ⑦ ghi **16 bảng ngừng ghi nhưng còn người đọc ⇒ `RETIRED`, không `DROP`**; ⑧ ghi **hai câu
hỏi lộ ra khi đếm**: `system_alerts` im 102 ngày · `pnl_daily_*` im 93 ngày; ⑨ ghi **còn 18 chỗ**
cùng lỗi thứ-tự-ngẫu-nhiên, **4 chỗ nặng nhất xếp hạng chính bộ số công bố** — phải **ĐO trước**;
⑩ ghi **bảy mục chờ owner duyệt gộp sáng 22/08** tại `docs/DUYET_GOP_2208.md`.
