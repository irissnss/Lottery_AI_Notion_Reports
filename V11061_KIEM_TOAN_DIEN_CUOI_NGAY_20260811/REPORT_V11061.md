# REPORT V11061 — KIỂM TOÀN DIỆN CUỐI CHU KỲ LIVE NGÀY 11/08/2026

**Ngày:** 2026-08-11 tối · **Mã đọc:** `KS1108-2` · **Production KHÔNG đổi** — không deploy, không
restart · PID `1353489` · `NRestarts=0` · `QD-041` nguyên vẹn · 4 bảng khoá số dòng **y hệt** đầu
và cuối phiên

---

## 1. Tóm tắt

**Kết quả: 1/3 bạch thủ** — MN `26` trượt · **MT `37` TRÚNG** · MB `73` trượt.

**Vận hành: sạch.** Ba miền chốt trước hạn, journal **3.509 dòng · 0 Traceback · 0 ERROR ·
0 CRITICAL · 0 exception**, `NRestarts=0`, 4 bảng khoá nguyên.

**Việc mới quan trọng nhất hôm nay:** lane A/B prompt ba tầng **chạy được cả ba miền, 12 cặp,
0 lỗi** — hôm qua 5/5 hỏng. Các bản vá sáng nay có tác dụng thật.

**Phát hiện cần owner biết:** biên an toàn của **MT chỉ ~13 phút suốt 12 ngày liền** (thấp nhất
**8 phút**), trong khi một model chậm mất **190–197 giây**. Đây **không phải xu hướng xấu đi** —
là **rủi ro thường trực chưa ai đo**.

**Ba lần agent tự bắt mình sai trong phiên này** (mục 7), gồm **một báo động giả về 6 script**
mà agent đã tự rút lại sau khi thử.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«Đã hết chu kỳ live hôm nay em tiến hành kiểm tra toàn diện, chi tiết đầu đủ phân tích đánh
> giá việc dự đoán hôm nay không bỏ sót điểm nào, đề xuất xử lý tiếp theo là gì em?»* — 11/08

Và trước đó, về cách làm việc:

> *«Không phải rẻ hay đắt mà anh đã từng gặp em load cả ngày và kết quả là đã đốt hết token và
> chả có 1 xử lý nào… thà em cập nhật tình hình thì anh còn dễ biết, em âm thầm quá»* — 11/08

**Đã thi hành:** phiên này báo tiến độ sau **mỗi chặng**, không gom vào một khối im lặng.

---

## 3. Đào bới / phát hiện

### 3.1 · Vận hành — đạt, nhưng phép đo ĐẦU TIÊN của agent là giả

| miền | chốt (giờ VN) | hạn §55 | sớm |
|---|---|---|---|
| MN | 05:24 | 15:45 | 621 phút |
| MT | 16:47 | 16:58 | **11 phút** |
| MB | 17:37 | 17:58 | 21 phút |

Journal: **3.509 dòng · 0 Traceback · 0 ERROR · 0 CRITICAL · 0 exception**.

> **Nhưng lần đo đầu tiên của agent trả về 0 dòng và agent suýt ghi «sạch».** Nguyên nhân ở mục
> 7.1 — và nó là **cùng họ với lỗ cổng báo cáo sáng nay**.

Bộ tự kiểm **18:05 đã chạy** (`logs/v10900_consistency.log`, 29 KB). Cron **21:40** (P4 gan hội
tụ) và **21:45** (B1 anti-trap) **có đúng dòng trong crontab** nhưng chưa tới giờ lúc kiểm
(VPS 21:15) — **không phải hỏng**.

### 3.2 · Phân tích dự đoán — trọng số hôm nay TRUNG TÍNH, không phải thủ phạm

| miền | BT | kết quả | BT ở hạng | «nhiều phiếu nhất» chọn | pool |
|---|---|---|---|---|---|
| MN | `26` | trượt | **#1** (8 phiếu) | `26` — **cùng số**, cũng trượt | 26 số, 8 trúng |
| **MT** | `37` | **TRÚNG** | **#2** (8 phiếu) | `82` (9 phiếu) — **cũng TRÚNG** | 17 số, 7 trúng |
| MB | `73` | trượt | **#2** (5 phiếu) | `71` (8 phiếu) — cũng trượt | 18 số, 2 trúng |

**① Trọng số không hại hôm nay.** MT: nó bỏ qua số dẫn phiếu (`82`) để chọn `37` — **cả hai đều
trúng**. MB: cũng bỏ qua số dẫn phiếu — cả hai đều trượt. Khác hẳn 10/08 khi trọng số làm mất `19`.

**② MN KHÔNG phải lỗi khâu chọn.** BT nằm **hạng 1**, luật thô cũng chọn đúng số đó. Hệ chọn
**đúng theo phiếu** — phiếu sai. Đây là **lỗi khâu SINH**.

**③ MB là ngày pool kém thật.** 22 đuôi ra, pool 18 số mà chỉ **2 số trúng**; bốc ngẫu nhiên 18 số
kỳ vọng **~4**. Số trúng tốt nhất (`00`) nằm **hạng 12**. **Không cách chọn nào cứu được ngày đó.**

**Cờ anti-trap: không miền nào bật hôm nay** ⇒ `FU-397` không có dữ liệu mới từ ngày này.

**Nền đúng:** 1/3 = 33,3% vs kỳ vọng ngẫu nhiên **30,3%** (nền từng miền 39% / 30% / 22%). Chênh
**+0,09 lượt trên 3 lượt** ⇒ **n=3, CHƯA ĐƯỢC PHÉP KẾT LUẬN** (RM-04), chỉ cộng dồn vào thước 164
ngày.

### 3.3 · Lane A/B ba tầng — chạy được cả ba miền

| miền | cặp | bất đồng |
|---|---|---|
| MN | 5 | 4 |
| MT | 4 | 2 |
| MB | 3 | 3 |
| **hôm nay** | **12** | **9** |

Tất cả `trang_thai=OK`, trễ 35–154s, **0 cặp lỗi**. Hôm qua 5/5 hỏng ⇒ bốn bản vá sáng nay
(khoá DB-trước-env-sau · parse bằng hàm thật · timeout theo miền · huỷ cặp nhiễm) **có tác dụng
thật**.

**Quan sát về TIẾN ĐỘ, không phải về thắng thua:** tỉ lệ bất đồng thực tế **75%**, trong khi
`N=96` được tính trên giả định **40,5%** (lấy từ lane cũ `PROMPT_V2_AB_V1`). Giữ nhịp này ⇒ **~9
cặp bất đồng/ngày** ⇒ đủ 96 trong **~11 ngày** thay vì 16.

> **Agent KHÔNG đọc ai thắng.** Ngưỡng đăng ký trước là `≥96 cặp bất đồng` **VÀ** `|z|≥1,96`. Bất
> đồng cao **không** nghĩa là T-B tốt hơn — nó cũng khớp với việc T-B trả lời khác đi ngẫu nhiên.

### 3.4 · `C20` LỆCH — và xu hướng NGƯỢC với điều agent định báo

Bộ tự kiểm 18:05 bắt `C20_bien_han_khong_troi`: *«MT/MB không có 3 ngày liên tiếp biên < 12 phút»*.
MT hôm nay 11 phút, hôm qua 11 phút.

**Agent định viết «biên đang mỏng dần». Đo 12 ngày thì SAI:**

```
MT:  11! 11! 16  14  13  15  12   8! 11! 17  12  12      (phút trước hạn, mới → cũ)
     6 ngày mới TB 13,3   ·   6 ngày trước TB 12,0   →   RỘNG hơn, không hẹp đi
```

**Sự thật khác và nặng hơn:** MT **luôn ở ~13 phút suốt 12 ngày**, thấp nhất **8 phút** (04/08).
Đó là **rủi ro thường trực**, không phải xu hướng mới. Và `deepseek-reasoner` trễ thật **190–197
giây** ⇒ **một model treo là MT vỡ hạn**.

**Điều này nối thẳng vào `FU-283` (hạn 13/08)** — mục đó đúng là *«đổ `latency_seconds` từ trace
vào bảng + panel §52, ngưỡng model TB > 180s»*. Nó **không phải việc giấy tờ**: nó là phép đo cho
đúng rủi ro vừa đo được.

---

## 4. Hướng xử lý và vì sao

Không đề xuất nào đụng production. Xếp theo **cái đã có bằng chứng**, không theo cái nghe hay.

| # | việc | vì sao | chạm gì |
|---|---|---|---|
| **1** | **`FU-283` — đo độ trễ từng model, panel §52** | biên MT chỉ ~13 phút mà một model mất 190s. **Chưa ai đo** cái này | **0** — chỉ đọc trace, bảng mới + panel |
| **2** | **Để lane A/B chạy tiếp ~11 ngày** | đang tích cặp đúng nhịp, không cần can thiệp | 0 |
| **3** | **Chờ 21:40/21:45 rồi kiểm hai bảng shadow** | cron đúng dòng, chưa tới giờ lúc kiểm | 0 |

**KHÔNG đề xuất** thêm model / thêm luật / sửa trọng số. Lý do đo được: lợi thế toàn hệ
**+0,34pp · CI95 [−3,8 … +4,5]** trên 164 ngày ⇒ **mọi thay đổi dưới +4,5pp nằm trong nhiễu**, và
hôm nay trọng số **không hại**. Sửa thứ chưa chứng minh là hỏng thì chỉ thêm chỗ để tin nhầm.

---

## 5. Đã làm gì

| # | việc | bằng chứng |
|---|---|---|
| 1 | Đồng bộ dữ liệu sống trước khi đo | manifest `20260811_210941` |
| 2 | Viết `_v11061_kiem_toan_1108.py` — bộ đo tái lập được (RM-11), có cổng RM-01 | script commit kèm |
| 3 | Đo kết quả · pool · hạng · luật nhiều-phiếu-nhất · nền đúng cho cả ba miền | mục 3.2 |
| 4 | Đo biên hạn 12 ngày để kiểm `C20` | mục 3.4 |
| 5 | Thử từng chuỗi thời gian `journalctl` để truy lỗi của chính mình | mục 7.1 |
| 6 | Ghi quy tắc làm việc mới: **báo tiến độ từng chặng** | owner ký 11/08 |

**Không deploy, không restart, không sửa production.**

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| RM-01 cổng tuổi dữ liệu | **✓ 0,08 giờ** |
| journal (đo đúng) | **3.509 dòng · 0 lỗi mọi loại** |
| mốc chốt §55 ba miền | **✓ đều trước hạn** |
| 4 bảng khoá đầu vs cuối phiên | **✓ số dòng y hệt** |
| `NRestarts` | **✓ 0** |
| bộ tự kiểm 18:05 | **✓ đã chạy** · `C20` LỆCH đúng (mục 3.4) |
| cron 21:40 / 21:45 | **✓ có trong crontab**, chưa tới giờ |

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| 11/08 | *«Đã hết chu kỳ live hôm nay em tiến hành kiểm tra toàn diện… đề xuất xử lý tiếp theo là gì em?»* |
| 11/08 | *«Không phải rẻ hay đắt mà anh đã từng gặp em load cả ngày và kết quả là đã đốt hết token và chả có 1 xử lý nào… thà em cập nhật tình hình thì anh còn dễ biết, em âm thầm quá»* |
| 11/08 | *«Em cứ tiến anh tổng lực kiểm tra toàn diện hôm nay dùm anh đi rồi mình tính tiếp»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| MT chốt `37`, TRÚNG | `final_bundles` 11/08 MT · `bach_thu_status=WIN` |
| BT của MT nằm hạng **#2**, số dẫn phiếu `82` **cũng trúng** | `_v11061_kiem_toan_1108.py` mục 3.2 |
| MB pool 18 số chỉ 2 trúng (kỳ vọng ~4) | cùng script |
| lane A/B ghi **12 cặp, 0 lỗi**, 3 miền | `prompt_3tang_ab_shadow_v11059` |
| MT biên hạn ~13 phút suốt 12 ngày, thấp nhất 8 phút | đo `final_bundles.created_at` 12 ngày |
| `journalctl --since "today 00:00"` **thất bại**, `--since today` **chạy** | `Failed to parse timestamp: today 00:00` |
| `final_bundles.created_at` là **giờ VN naive**, `predictions`/`lottery_results` là **ISO +07:00** | PRAGMA + đối chiếu giờ xổ |

### `DOC_SAID`

| tài liệu ghi gì | file:mục | lệch? |
|---|---|---|
| *«nhiều bảng lưu `created_at` theo UTC… so với `localtime` là lệch 7 tiếng»* | `CLAUDE.md` §55 | **⚠ không đúng cho ba bảng này** — hai bảng lưu ISO có offset, `final_bundles` lưu **naive giờ VN**. Câu cảnh báo đúng tinh thần nhưng **sai chi tiết**, và chi tiết mới là thứ gây đọc nhầm |
| `FU-283` *«đổ `latency_seconds` vào bảng + panel · ngưỡng TB > 180s»* | `docs/FOLLOW_UP_TRACKER.md:1821` | **khớp** — và hôm nay có bằng chứng nó cấp bách hơn tưởng |
| `RM-04` *«n nhỏ là CHƯA ĐƯỢC PHÉP KẾT LUẬN»* | `CLAUDE.md` §61 | **khớp** — 1/3 hôm nay không đọc riêng |

### Ba lớp lệch nhau ⇒ FINDING

1. **`DOC_SAID` ≠ `CODE_DID` về múi giờ.** `CLAUDE.md` §55 nói `created_at` là UTC; thực tế ba
   bảng có **ba quy ước khác nhau**, và `final_bundles` lưu **naive không offset** — đọc bằng
   `time(created_at)` sẽ ra sai. Agent đã suýt kết luận báo cáo V11057 hôm qua sai 7 tiếng vì
   chính chỗ này.
2. **`OWNER_SAID` ≠ hành vi agent trước đó.** Owner nói rõ vấn đề là **im lặng**, không phải chi
   phí; agent trước đó đề nghị **thu hẹp phạm vi** — đọc sai ý. Đã sửa: báo tiến độ từng chặng.

---

## 7. Vướng vấp — ba lần agent tự bắt mình

### 7.1 · Phép đo journal đầu tiên là GIẤY CHỨNG NHẬN SẠCH CẤP CHO TẬP RỖNG

Agent chạy `journalctl --since "today 00:00" 2>/dev/null` ⇒ **0 dòng** ⇒ suýt ghi *«0 traceback,
0 ERROR, 0 CRITICAL»*.

Thử lại từng chuỗi:

| chuỗi | dòng |
|---|---|
| `--since today` | **3.513** ✓ |
| `--since "today 00:00"` | **0** ✗ |
| `--since "2026-08-11 00:00"` | **3.513** ✓ |

`journalctl` **có kêu**: `Failed to parse timestamp: today 00:00`. Nhưng `2>/dev/null` **nuốt mất
tiếng kêu**, để lại đúng một số `0` câm lặng.

> **Chặn stderr biến một lỗi ồn ào thành số 0 im lặng** — cùng khuôn với lỗ cổng báo cáo sáng nay.

### 7.2 · BÁO ĐỘNG GIẢ về 6 script — agent tự rút lại

Thấy `--since "today 00:00"` hỏng, agent quét kho và tìm ra **6 script** dùng `--since today`,
gồm `_v10975_dau_ngay_probe.py` (**bộ dò đầu ngày**) và `_v10978_audit_probe.py` — và định báo
*«sáu script đã báo 0 lỗi trên tập rỗng bấy lâu»*.

**Sai.** `--since today` là chuỗi **hợp lệ** (3.513 dòng); chuỗi hỏng là `"today 00:00"` do agent
**tự chế**. Sáu script **không sao**. Đã thử trước khi báo, nên báo động giả **không ra khỏi phiên**.

### 7.3 · Suýt báo «biên MT đang mỏng dần» và «V11057 sai 7 tiếng» — cả hai đều SAI

- **Biên MT:** đo 12 ngày cho thấy 6 ngày mới **RỘNG hơn** 6 ngày trước (13,3 vs 12,0). Không có
  xu hướng xấu đi. Sự thật là **mức thấp kinh niên**, khác hẳn về mặt xử lý.
- **Múi giờ:** agent nghi `final_bundles.created_at` là UTC ⇒ báo cáo V11057 sai 7 tiếng. Kiểm
  thì `final_bundles` lưu **giờ VN naive** (chứng minh: MB chốt 17:37, kết quả MB về 18:31 — nếu
  17:37 là UTC thì = 00:37 hôm sau, tức **chốt sau khi đã xổ**, vô lý). **V11057 đúng.**

**Cả ba vấp cùng một khuôn:** agent tin **một phép đo duy nhất** thay vì hỏi *«phép đo này có thể
hỏng theo cách nào?»*.

---

## 8. Gỡ về

Phiên này **chỉ thêm một script đo read-only** và tài liệu — không đổi hành vi production.

```bash
git revert <sha V11061>
```

---

## 9. Theo dõi tiếp

| mã | việc | ngưỡng hành động | mốc |
|---|---|---|---|
| **FU-283** · `DO1308` | **đang trôi** — đo độ trễ từng model + panel §52. Hôm nay có bằng chứng **cấp bách hơn tưởng**: biên MT ~13 phút vs model chậm 190s | model TB > 180s ⇒ xét ở FU-290 | **13/08** |
| **FU-398** · `PB1108` | lane A/B — **12 cặp, 9 bất đồng** ngày đầu chạy sạch | `≥96 cặp bất đồng` **VÀ** `\|z\|≥1,96` · **cấm đọc sớm** | ~**22/08** (nhịp 9/ngày) |
| **FU-399** · `UI1108` | UI `/filter` — **chờ owner mô tả** | owner nói rõ muốn gì | — |
| **FU-397** · `AT1008` | B1 anti-trap — **hôm nay cờ không bật**, không có dữ liệu mới | `n(FULL_SPENT) ≥ 90` · đang **51/90** | ~giữa 12/2026 |
| **FU-394** | P4 gan hội tụ — chờ cron 21:40 | — | mỗi ngày |
| FU-284 | cửa sổ đang chạy | **9,53** · z ≥ 1,96 · n ≥ 150 | **20/08** — cấm đọc sớm |
| — | **42 mục quá hạn · 14 mồ côi** briefing cảnh báo | cần một phiên rà riêng | chờ owner xếp |

**Chưa dùng mã FU mới nào trong phiên này.**

---

TanPhatAI cần làm: ① ghi kết quả 11/08 **1/3** (MT `37` trúng) và ghi rõ **trọng số hôm nay trung
tính** — MT chọn hạng #2 nhưng số dẫn phiếu **cũng trúng**, khác hẳn ca 10/08; ② ghi phát hiện
**biên hạn MT ~13 phút kinh niên suốt 12 ngày, thấp nhất 8 phút**, và nối nó vào **`FU-283` hạn
13/08** — đây là lý do FU-283 không được để trôi tiếp; ③ **đính chính `CLAUDE.md` §55**: ba bảng
có ba quy ước `created_at` khác nhau, `final_bundles` lưu **naive giờ VN không offset**, không
phải UTC; ④ ghi vào sổ bài học *«chặn stderr biến lỗi ồn ào thành số 0 im lặng»*; ⑤ ghi quy tắc
owner ký 11/08: **báo tiến độ từng chặng, cấm chạy im lặng dài**.
