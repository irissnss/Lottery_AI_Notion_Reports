# V11115 — 2026-08-25 (trưa) — `GĐ-0` PROMPT 35: CHỤP TRẠNG THÁI VPS TRƯỚC KHI CHẠM · SUBSTRATE LỊCH SỬ **ĐỦ 100%** ĐỂ BENCHMARK

**Ngày làm việc:** 25/08/2026 ·
**Ngày viết báo cáo này:** 26/08/2026 · **Commit riêng:** `3dc3611` ·
**Trạng thái:** `BÙ TỪ NGUỒN GỐC`

---

> ## ⚠️ ĐÂY LÀ BÁO CÁO **BÙ**, KHÔNG PHẢI BẢN VIẾT LÚC LÀM VIỆC
>
> Bản `V11115` làm ngày **25/08** nhưng **không có** thư mục báo cáo công khai —
> vi phạm `§57.2` đã tồn tại **1 ngày**.
> Cổng A55 cũ **không thấy** vì nó chỉ soi **8 bản gần nhất** (đã vá ở `V11122`, `FU-442`).
>
> **Ba nguồn dựng nên bản này — cả ba đều là bản ghi ĐƯƠNG THỜI:**
>
> | nguồn | quy mô |
> |---|---|
> | khối `## V11115` trong `CHANGELOG.md` — viết **ngay lúc làm việc** | **2,530 ký tự / 53 dòng** |
> | commit git mang nhãn `V11115` | **1** commit |
> | lượt owner trong vết phiên `.jsonl` cùng ngày | **có** |
> | khối phụ (`V11115b`/`c`/…) | — |
>
> 🔴 **PHẦN KHÔNG KHÔI PHỤC ĐƯỢC** — ghi thẳng, không suy:
> · **giờ chính xác** từng thao tác trong phiên · **vướng vấp giữa chừng** không được ghi lại lúc đó
> · **hash 4 bảng khoá trước/sau** (nếu phiên có chạm DB) · **PID trước/sau** (nếu có restart).
> Những chỗ đó dưới đây đều ghi `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.

---

## 1. Tóm tắt

**Bước bảo toàn của prompt 35.** Chụp **trước** khi chạm bất cứ thứ gì. Toàn bộ **READ-ONLY**
(`mode=ro`), không deploy, không restart.
### Trạng thái chụp `25/08 12:54:48` (giờ VN, UTC+7)
```
PID 2341779 · NRestarts 0 · health 200 · service start 2026-08-23 22:29:02 +07
hash 10 tệp runtime local ↔ VPS : KHỚP TOÀN BỘ
253 bảng · DB 760.795.136 byte · 92 dòng cron
MN 25/08  v=1  BT='84'  lo2=["84","91"]  lo3='884'  xien2=["84","91"]  xien3=["84","91","70"]
          mc=15  top_score=0.0853  created=05:18:56 (giờ VN)  notes='auto_auto_daily'
roster: 15 output_eligible / 49 registry
freeze MN 15:45 · MT 16:58 · MB 17:58   ·   T-chốt MN 15:40 · MT 16:55 · MB 17:55
lượt 25/08: MN 16 model auto_daily + 11 shadow · MT 7 · MB 7 · chưa miền nào xổ
```
Băm nội dung `6f7841d5b2fbd0d1…` ·
`artifacts/gd0_snapshots/gd0_2026-08-25_125448_6f7841d5.json` · thử chặn **10/10**.
### 🟢 CÂU CHẶN ĐÃ THÔNG — substrate lịch sử **đủ để benchmark**
Owner khoá: *«roster lịch sử không tái lập được ⇒ DỪNG VÀ BÁO»*. Đo thật:
| | |

## 2. Owner yêu cầu gì (nguyên văn)

> *«PROMPT TỔNG LỰC LẦN 35 KIỂM TOÁN VÀ THAY PHƯƠNG PHÁP TOTAL/OUTPUT THỰC THI TRONG NGÀY 25/08/2026 Dùng multi-agent song song nhưng chỉ MỘT Coordinator hợp nhất. Không mở Plan/sổ cạnh tranh. Không mặc định 15 model tốt hơn 8 model. Không mặc định nhiều model tốt hơn ít model. Số lượng model chỉ là tồn kho. Chất lượng TOTAL phải được chứng minh bằng: - khả năng sinh số; - độ phủ; - xếp hạng; - đóng góp biên; - tính độc …»*
> — owner, **25/08/2026 12:52** (giờ VN)

> *«đang đo lường ah em? đợi kết quả hay sao?»*
> — owner, **25/08/2026 13:03** (giờ VN)

> *«còn đang chạy không em ? xong chưa push báo cáo tổng lực chưa em?»*
> — owner, **25/08/2026 14:26** (giờ VN)

> *«Đã push báo cáo hết chưa em? - Kiểm tra lại toàn bộ 1 lần nữa xem còn gì không để push báo cáo 1 lần luôn - Các vấn đề anh tương tác trực tiếp đã push thành 1 bảng ghi nhận yêu cầu của owner chưa ? Có cần cập nhật quy tắc trong claude.md để chuẩn hóa không vì đôi lúc code đi trước tài liệu do tương tác trực tiếp với em liên tục cho liền mạch ah em. Nên em claude code có thể đi trước tài liệu và việc ghi nhận các yêu …»*
> — owner, **25/08/2026 18:29** (giờ VN)

> *«Em hãy tiến hành đọc toàn bộ các phiên làm việc của claude code và cursor kết hợp báo cáo tổng hợp đính kèm và các thông tin audit báo cáo tất cả mọi thể chạy tổng lực tổng hợp lại một phiên tổng lực với đầy đủ tất cả các vấn đề không làm rơi rụng bất kỳ vấn đề nào, các vấn đề đã xử lý , có thể xử lý , tự xử lý rõ ràng , các yêu cầu của anh v.... không bỏ sớt bất kỳ điểm nào nha em. Em tiến hành xem toàn bộ các phiên…»*
> — owner, **25/08/2026 18:56** (giờ VN)


*(Trích từ corpus lượt owner đã khử trùng của vết phiên `.jsonl`; giờ đã quy về giờ Việt Nam.)*

## 3. Đào bới / phát hiện

Toàn văn khối `CHANGELOG` đương thời — **nguồn chính** của bản này:

## V11115 — 2026-08-25 (trưa) — `GĐ-0` PROMPT 35: CHỤP TRẠNG THÁI VPS TRƯỚC KHI CHẠM · SUBSTRATE LỊCH SỬ **ĐỦ 100%** ĐỂ BENCHMARK

**Bước bảo toàn của prompt 35.** Chụp **trước** khi chạm bất cứ thứ gì. Toàn bộ **READ-ONLY**
(`mode=ro`), không deploy, không restart.

### Trạng thái chụp `25/08 12:54:48` (giờ VN, UTC+7)

```
PID 2341779 · NRestarts 0 · health 200 · service start 2026-08-23 22:29:02 +07
hash 10 tệp runtime local ↔ VPS : KHỚP TOÀN BỘ
253 bảng · DB 760.795.136 byte · 92 dòng cron
MN 25/08  v=1  BT='84'  lo2=["84","91"]  lo3='884'  xien2=["84","91"]  xien3=["84","91","70"]
          mc=15  top_score=0.0853  created=05:18:56 (giờ VN)  notes='auto_auto_daily'
roster: 15 output_eligible / 49 registry
freeze MN 15:45 · MT 16:58 · MB 17:58   ·   T-chốt MN 15:40 · MT 16:55 · MB 17:55
lượt 25/08: MN 16 model auto_daily + 11 shadow · MT 7 · MB 7 · chưa miền nào xổ
```

Băm nội dung `6f7841d5b2fbd0d1…` ·
`artifacts/gd0_snapshots/gd0_2026-08-25_125448_6f7841d5.json` · thử chặn **10/10**.

### 🟢 CÂU CHẶN ĐÃ THÔNG — substrate lịch sử **đủ để benchmark**

Owner khoá: *«roster lịch sử không tái lập được ⇒ DỪNG VÀ BÁO»*. Đo thật:

| | |
|---|---|
| bundle có `ranked_numbers` | **535/535 = 100%**, phủ đều `02/2026 → 08/2026` |
| có trường `voters` | **535/535 = 100%** |
| `score_breakdown` từng thành phần | **có** — `model · run_source · position · position_weight · verdict_weight · lane_weight · strength_weight · effective_weight · score` |
| `model_bt` · `model_wr` | **có** — nhưng mang **30 model**, gồm cả model đã nghỉ |
| mẫu benchmark (có **cả** ladder **lẫn** kết quả xổ) | **534 bundle** — MB 178 · MN 178 · MT 178 |
| roster lịch sử | tái lập được từ `predictions` (`run_source` official), **621** cặp ngày–miền |

⇒ **toàn bộ phép tính TOTAL tái lập được từ dữ liệu đã lưu** — chạy được `M0…M6` trên **cùng
snapshot · cùng roster lịch sử thật · không lookahead**.

### 🔴 Mâu thuẫn phát hiện ngay ở `GĐ-0`

Bundle `24/08` MN ghi `total_models=15` · `scoreable_model_count=15` ·
`output_eligible_row_count=15` — nhưng ladder chỉ có **13 model bỏ phiếu thật**, còn bảng trọng
số `model_wr`/`model_bt` mang **30 model** (gồm `gpt-5-mini`, `glm-5.2`, `grok-4.3`… đã nghỉ).
Đang truy trong `GĐ-1`.

### Phân bố roster thật theo ngày–miền — **KHÔNG phải lúc nào cũng 15**

```
1:11 · 2:6 · 3:8 · 5:2 · 6:4 · 7:4 · 8:215 · 9:30 · 10:3 · 11:8 · 12:22
13:37 · 14:36 · 15:164 · 16:50 · 17:15 · 18:3 · 19:3
```

Cụm lớn nhất là **8 model** (215 ngày–miền), rồi **15** (164). Con số 15 **không phải hằng số**.

## 4. Hướng xử lý và vì sao chọn

Lý do chọn nằm trong chính khối `CHANGELOG` ở mục 3 — đó là bản ghi viết **lúc làm việc**,
không phải suy lại. Phần **cân nhắc phương án bị loại** thì 🔴 **KHÔNG KHÔI PHỤC ĐƯỢC**: nó chỉ
tồn tại trong vết phiên và không được ghi vào tài liệu nào lúc đó.

## 5. Đã làm gì

| commit | ngày (giờ VN) | tệp | tổng |
|---|---|---|---|
| `3dc3611` | 2026-08-25 13:01:58 | CHANGELOG.md, .../gd0_2026-08-25_125448_6f7841d5.json, docs/AUTOMATION_HISTORY.jsonl, docs/AUTOMATION_STATE.json, docs/CURRENT_TRUTH_SSOT.md, web/back | 6 files changed, 396 insertions(+), 3 deletions(-) |

## 6. Cổng kiểm

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC output cổng của phiên gốc** — cổng in ra `stdout`, không ghi tệp
(đúng khuyết tật `RM-15` mà `V11121` đã vá cho `cong_git_commit.py` bằng sổ điểm danh).

Điều **kiểm được hôm nay**, `26/08/2026`:

| phép | kết quả |
|---|---|
| commit của bản này còn trong `git log` | ✅ **1/1** còn nguyên, đều là tổ tiên của `origin/master` |
| khối `CHANGELOG` còn nguyên | ✅ 2,530 ký tự |
| bản này đã có báo cáo công khai chưa | ✅ **có, từ bản bù này** — trước đó `A55_VIOLATION_REPORT_MISSING` |

## 7. Vướng vấp

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC** vướng vấp trong phiên gốc — không tài liệu nào ghi lại lúc đó.

Vướng vấp **của chính việc bù này**, ghi trung thực: bản bù dựng từ ba nguồn đương thời nhưng
**không thay được** một báo cáo viết lúc làm việc. Cụ thể mất: giờ từng thao tác · các phương án
đã cân nhắc rồi loại · lỗi gặp giữa chừng · trạng thái trước/sau của DB nếu phiên có chạm.

## 8. Gỡ về

Bản bù này **chỉ thêm tài liệu**, không đụng mã và không đụng dữ liệu ⇒ gỡ về =
`git rm -r V11115_GD0_CHUP_TRANG_THAI_VPS_TRUOC_KHI_CHAM_20260825/` rồi commit lại. Trạng thái quay về đúng như trước khi bù.

Việc gỡ về của **bản gốc `V11115`** nằm trong chính khối `CHANGELOG` ở mục 3 (nếu bản đó có ghi).

## 9. Theo dõi tiếp

| mã | việc | trạng thái |
|---|---|---|
| `FU-442` | vá cổng A55 — chính lỗ hổng làm bản này vô hình | ✅ **ĐÃ VÁ** ở `V11122`, thử chặn **11/11** |
| — | bù nốt các bản còn thiếu | trên **toàn dải từ mốc thi hành `V10921`** còn **32** bản thiếu báo cáo; 10 bản của đợt này là nhóm ưu tiên |
| — | ngưỡng đóng bằng số | `_v10921_report_gate.py` chạy **không tham số** ⇒ `V11115` không còn trong danh sách `THIẾU BÁO CÁO` |

---

## 10. BA LỚP NGUỒN (§62 · A60)

### `OWNER_SAID`
> *«PROMPT TỔNG LỰC LẦN 35 KIỂM TOÁN VÀ THAY PHƯƠNG PHÁP TOTAL/OUTPUT THỰC THI TRONG NGÀY 25/08/2026 Dùng multi-agent song song nhưng chỉ MỘT Coordinator hợp nhất. Không mở Plan/sổ cạnh tranh. Không mặc định 15 model tốt hơn 8 model. Không mặc định nhiều model tốt hơn ít model. Số lượng model chỉ là tồn kho. Chất lượng TOTAL phải được chứng minh bằng: - khả năng sinh số; - độ phủ; - xếp hạng; - đóng góp biên; - tính độc …»*
> — owner, **25/08/2026 12:52** (giờ VN)

> *«đang đo lường ah em? đợi kết quả hay sao?»*
> — owner, **25/08/2026 13:03** (giờ VN)

> *«còn đang chạy không em ? xong chưa push báo cáo tổng lực chưa em?»*
> — owner, **25/08/2026 14:26** (giờ VN)

> *«Đã push báo cáo hết chưa em? - Kiểm tra lại toàn bộ 1 lần nữa xem còn gì không để push báo cáo 1 lần luôn - Các vấn đề anh tương tác trực tiếp đã push thành 1 bảng ghi nhận yêu cầu của owner chưa ? Có cần cập nhật quy tắc trong claude.md để chuẩn hóa không vì đôi lúc code đi trước tài liệu do tương tác trực tiếp với em liên tục cho liền mạch ah em. Nên em claude code có thể đi trước tài liệu và việc ghi nhận các yêu …»*
> — owner, **25/08/2026 18:29** (giờ VN)

> *«Em hãy tiến hành đọc toàn bộ các phiên làm việc của claude code và cursor kết hợp báo cáo tổng hợp đính kèm và các thông tin audit báo cáo tất cả mọi thể chạy tổng lực tổng hợp lại một phiên tổng lực với đầy đủ tất cả các vấn đề không làm rơi rụng bất kỳ vấn đề nào, các vấn đề đã xử lý , có thể xử lý , tự xử lý rõ ràng , các yêu cầu của anh v.... không bỏ sớt bất kỳ điểm nào nha em. Em tiến hành xem toàn bộ các phiên…»*
> — owner, **25/08/2026 18:56** (giờ VN)


### `CODE_DID`
| điều mã **thực sự** làm | bằng chứng |
|---|---|
| 1 commit mang nhãn `V11115` | `3dc3611` — còn nguyên trong `git log`, đều là tổ tiên `origin/master` |
| tệp bị đụng | xem bảng mục 5 |
| bản này **chưa từng** có báo cáo công khai cho tới hôm nay | `_v10921_report_gate.py` liệt `V11115` trong `THIẾU BÁO CÁO` trước khi bù |

### `DOC_SAID`
| tài liệu | nói gì | khớp code chưa |
|---|---|---|
| `CHANGELOG.md` khối `## V11115` | 2,530 ký tự, viết đương thời | 🟢 **khớp** — commit tồn tại đúng ngày ghi |
| kho báo cáo công khai | **không có** thư mục `V11115_*` | 🔴 **LỆCH** — đã đóng bằng bản bù này |

### 🔴 BA LỚP LỆCH NHAU
`DOC_SAID` ≠ `CODE_DID`: mã đã chạy và đã commit, `CHANGELOG` đã ghi, nhưng **kho công khai không
có gì** suốt 1 ngày. Đó là `A55_VIOLATION_REPORT_MISSING`, và nó **vô hình** vì cổng chỉ soi 8
bản gần nhất — nay đã vá (`FU-442` · `V11122`).

---

**TanPhatAI cần làm:** ghi nhận đây là **báo cáo BÙ** viết ngày 26/08/2026 cho việc làm ngày
25/08, dựng từ **ba nguồn đương thời** (CHANGELOG 2,530 ký tự ·
1 commit · vết phiên), **không** phải bản viết lúc làm việc — mọi chỗ không khôi phục
được đã ghi thẳng là `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.
