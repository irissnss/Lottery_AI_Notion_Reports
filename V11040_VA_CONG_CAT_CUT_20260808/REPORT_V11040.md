# REPORT V11040 — VÁ CỔNG CHỐNG CẮT CỤT (FU-378) + SỬA SỐ ĐẶC TRƯNG ML (FU-347)

**Ngày:** 2026-08-08, 22:00–23:10 giờ VN *(owner gọi là «phiên 09/08»; ghi theo đồng hồ thật)*
**Phiên bản:** V11040 · **Tầng verdict:** `REPORT_PROVEN` + `CODE_PUSHED` — **CHƯA deploy VPS**
(không cần: hai tệp sửa là **cổng kiểm local**, không nằm trên đường chạy production)

---

## 1. Tóm tắt

Hai việc, cả hai đều là **vá cổng đã báo xanh trong khi thứ nó canh đang hỏng**.

**FU-378 — cổng chống cắt cụt mù với tệp CRLF.** Ngày 08/08 `CHANGELOG.md` mất **17.453 dòng**
và `web/backend/main.py` mất **4.056 dòng** (cắt đúng **768 KiB**, `SyntaxError` dòng 17149,
**không parse được**). Cổng `_v11015_cong_chan_cat_cut.py` sinh ra để canh đúng việc đó đã
**thoát 0** và chỉ in *«ngắn đi nhiều nhưng không phải cắt cụt — kiểm tay rồi commit»*.
Ba lỗ hổng, cả ba đã vá và **đã thử chứng minh chặn được**.

**FU-347 — «39 đặc trưng» là số sai, và nó đang là ngưỡng hành động của FU-320.** Code thật có
**28**, không phải 39. Bỏ 6 đặc trưng gan/vùng còn **22**, không phải 33. Bản A/B của FU-320 nếu
chạy theo số cũ là **đăng ký sai từ đầu**.

Và một việc thứ ba **không định làm mà bật ra**: cổng sổ quyết định báo `QD-022` **TRÔI**. Đào
tới gốc thì **không phải lỗi của phiên này** — bảng tải owner ký ngày 04/08 **đếm thiếu ngay từ
lúc ký**. Ghi thành `FU-379`, **chờ owner ký**, agent không tự sửa.

---

## 2. Owner yêu cầu gì (nguyên văn)

Từ **PROMPT TỔNG LỰC LẦN 3 — PHIÊN 09/08**:

> **GĐ-1** — vá cổng chống cắt cụt (FU-378).
>
> **KÈM NHANH (15 phút, cùng GĐ-1):** FU-347 — sửa "39 đặc trưng" → 28 ở CHANGELOG.md:1179 +
> FOLLOW_UP_TRACKER.md:533 (đây là ngưỡng hành động của FU-320 — sai thì bản A/B đăng ký sai từ
> đầu). §60 đầy đủ.
>
> **Báo cáo công khai ĐẨY NGAY cùng commit** (A55 — hôm qua owner phải hỏi mới lộ thiếu; không
> để lặp).

Ràng buộc owner đặt, còn nguyên hiệu lực:

> **KHÔNG LÀM:** đổi prompt/chọn số/roster (QD-041 tới 21/08) · FU-290 · chấm sớm lane G2-MB ·
> kết luận FU-284 · B1/B2 trước khi sổ FOLLOW_UP sạch · §24 · mở rộng phạm vi ngoài danh sách trên.

> **NUMBERING:** TRƯỚC khi dùng bất kỳ mã mới nào (V · FU · QD · mã đọc §58), phải quét thủ công
> BỐN nơi… và in bằng chứng quét vào report. Cấm "đoán số tiếp theo".

---

## 3. Đào bới / phát hiện

### 3.1 — Cổng chống cắt cụt: ba lỗ hổng, không phải một

| # | lỗ hổng | vì sao chí mạng |
|---|---|---|
| ① | `cu.startswith(moi)` so bản đĩa **CRLF** với `git show` trả **LF** | gần như **cả kho này là CRLF**. Dấu hiệu mạnh nhất — *«phần còn lại là tiền tố nguyên vẹn»* — **không bao giờ khớp**. Cổng mù với đúng nhóm tệp nó cần canh |
| ② | `BIEN_NGHI` chỉ chứa luỹ thừa 2: `{64,128,256,512,1024,2048} KiB` | sự cố cắt tại **768 KiB**. 768 **không phải luỹ thừa 2** ⇒ dấu hiệu thứ hai cũng câm. Trần đệm thật là **bội 64 KiB** |
| ③ | `_doc_prepend.prepend()` chỉ so bản mới với **bản trên đĩa** | đĩa cụt sẵn thì ghép khối mới vào vẫn *«dài hơn»* ⇒ cho ghi. Tệ hơn: việc ghi đó **phá luôn quan hệ tiền tố** mà cổng dùng để nhận diện — **tự tay xoá bằng chứng máy đọc được** |

Lỗ ③ đã được ghi thẳng trong docstring của chính cổng từ sự cố **07/08**. **Lỗi lặp lại y nguyên
sau đúng một ngày.**

### 3.2 — «39 đặc trưng» mâu thuẫn với bảng nằm ngay cạnh nó

Đo bằng **AST** trên code thật, không đọc lại tài liệu (RM-10):

```
web/backend/ml_models.py:31     FEATURE_COLS = 28 cột
web/backend/meta_learner.py:51  FEATURE_COLS = 28 cột
```

Bảng phân rã đi kèm ngay bên phải chữ «39» trong `CHANGELOG.md`:
`tần suất(5) · gan/vùng(6) · xu hướng(3) · hội tụ(1) · xếp hạng(5) · thứ(2) · lag(5) · chéo miền(1)`
→ **5+6+3+1+5+2+5+1 = 28**.

Con số 39 **mâu thuẫn với bảng nằm cùng dòng với nó**, và không ai đọc ra suốt thời gian đó.
Bỏ 6 đặc trưng gan/vùng ⇒ **22**, không phải 33.

### 3.3 — Việc không định tìm: `QD-022` TRÔI, và gốc nằm ở chỗ khác hẳn

`_v10920_decision_ledger` báo `QD-022 🔴 TRÔI 1/9`. Cổng `_v10982_kiem_lich9.py` trượt phép **J5**:
*«10/08 = 4 mục (trần 3)»*.

Mục thứ tư là **`FU-325`** — và nó **luôn** đáo hạn 10/08. Tiêu đề gốc viết `cần 10/08`,
**thiếu chữ «hạn»**, nên bộ đọc trả `due=None`, `han=''`: **vô hình với mọi bộ đếm** kể từ ngày
được viết. V11037/`FU-353` vá tiêu đề và V11038/`FU-370` cho kế thừa hạn — hai bản vá đó
**không tạo** tải mới, chúng **làm hiện** tải vốn có.

⇒ Bảng tải trong `QD-022` (*«10/08 = 3 mục»*) **sai ngay tại thời điểm owner ký 04/08**.
Đúng dạng **RM-17**: số không tái lập được đã thành căn cứ quyết định.

Phần thứ hai của J5 là **lỗi thiết kế cổng**: nó ghim **danh sách thành viên từng ngày** chụp
04/08. Sổ từ đó lớn thêm 11 mục có hạn rơi vào 08–09/08 ⇒ cổng **đỏ vĩnh viễn** ngay khi có việc
mới. Cổng đỏ vĩnh viễn bị bỏ qua **y hệt** cổng xanh mù.

---

## 4. Hướng xử lý và vì sao chọn

**FU-378 — vá cả ba lỗ, không vá một (RM-07).** Vá lỗ ① mà bỏ ② thì tệp CRLF cắt đúng biên vẫn
lọt; vá ①② mà bỏ ③ thì `prepend` vẫn xoá bằng chứng trước khi cổng kịp nhìn.

`_doc_prepend` chỉ **CẢNH BÁO**, không ném lỗi. Tài liệu có thể ngắn đi hợp lệ, và chặn đứng
đường ghi nhận là đổi một lỗi hiếm lấy một lỗi thường xuyên. Nhưng phải **kêu to**.

**FU-347 — sửa số, giữ nguyên dấu vết.** Không xoá con số cũ khỏi lịch sử: mọi chỗ ghi lại lỗi
được **giữ**, đó là bằng chứng đã sửa (§60.3 phân loại `CHU_THICH`).

**FU-379 — trình owner, không tự xử.** Ba cách «làm cho xanh» đều bị loại:

| cách làm | vì sao KHÔNG |
|---|---|
| dời hạn `FU-325` | nó neo vào một **cửa sổ đo** — dời hạn là dời phép đo (RM-06: agent không tự đặt/dời hạn) |
| sửa trần 3 → 4 trong cổng | đổi cam kết owner đã ký mà không hỏi |
| nới cổng cho hết đỏ | **ép số cho đẹp** — đúng thứ `QD-022` tự dặn *«nói thẳng thay vì ép số»* |

---

## 5. Đã làm gì

### 5.1 — FU-378 · §60.4 TRƯỚC / SAU / PHIÊN BẢN / KIỂM

| chỗ | TRƯỚC | SAU |
|---|---|---|
| `_v11015` so tiền tố | `cu.startswith(moi)` — bản đĩa CRLF vs `git show` LF | chuẩn hoá **cả hai** về LF (`cu_ss`/`moi_ss`) rồi mới so. Số dòng/byte vẫn báo theo bản thật |
| `_v11015` `BIEN_NGHI` | `{64,128,256,512,1024,2048} KiB` — **6 mốc** | `{n × 64 KiB : n = 1..128}` — **128 mốc**, 64 → 8192 KiB |
| `_doc_prepend.prepend()` | chỉ so `merged` với `old` (bản trên đĩa) | thêm `_canh_bao_cut_truoc_khi_ghi(p, old)` gọi **trước** khi dựng `merged` |

**PHIÊN BẢN:** V11040 · 2026-08-08 23:00

| tệp | md5 TRƯỚC (git HEAD) | md5 SAU |
|---|---|---|
| `_v11015_cong_chan_cat_cut.py` | `5eb88f13dab5693761d468e670e1917d` | `4d3f58bf7126f5771166fc8222889265` |
| `_doc_prepend.py` | `b56b96af8b03…` | `affb041091c01937b9c8fb86c96bf835` |

### 5.2 — FU-347

| chỗ | TRƯỚC | SAU |
|---|---|---|
| `CHANGELOG.md` bảng «Bốn sự thật về ML» | «**39 đặc trưng**» | «**28 đặc trưng**» + ghi chú vì sao |
| `docs/FOLLOW_UP_TRACKER.md` ngưỡng hành động FU-320 | «39 đặc trưng vs 33» *(SỐ CŨ)* | «**28 đặc trưng vs 22**» + bằng chứng AST |

Số dòng owner trích trong brief (`CHANGELOG.md:1179` · `FOLLOW_UP_TRACKER.md:533`) **đã cũ** —
hai sổ này ghi kiểu prepend nên số dòng trôi liên tục. Vị trí thật khi sửa: `CHANGELOG.md:2564` ·
`FOLLOW_UP_TRACKER.md:1055`. Đã sửa đúng **nội dung**, không sửa mù theo số dòng.

### 5.3 — Hai cổng mới, cả hai **đã thử chứng minh chặn được** (RM-15)

`web/backend/_v11040_kiem_cat_cut.py` · `web/backend/_v11040_kiem_dac_trung.py`

### 5.4 — FU-379 ghi vào sổ, `OWNER_DECISION_NEEDED`, hạn `LX`

Không đặt hạn (RM-06). Trình owner hai phương án A/B kèm khuyến nghị **A** và hậu quả nếu treo.

---

## 6. Cổng kiểm

**`_v11040_kiem_cat_cut.py`** — thử trên vật thật `web/backend/main.py` (976.303 byte · 21.204
CRLF), khôi phục byte-khớp trong `finally` sau **mỗi** phép, có `assert` xác nhận khôi phục:

```
vật thử: \web\backend\main.py · 976,303 byte · 21,204 CRLF
✓ cắt đúng biên 768 KiB (kiểu 08/08)      mã thoát=1 CHẶN     (mong CHẶN)
✓ cắt lệch biên, chỉ còn dấu hiệu TIỀN TỐ mã thoát=1 CHẶN     (mong CHẶN)
✓ tệp nguyên vẹn                          mã thoát=0 cho qua  (mong cho qua)
✓ 768 KiB nằm trong BIEN_NGHI (128 mốc, từ 64 tới 8192 KiB)
✓ `_doc_prepend` soi bản trên đĩa TRƯỚC khi ghi
✓ [cong] CAT_CUT_V11040=DAT
```

**Hook `.cursor/hooks/truncation_guard.py` kế thừa bản vá** (nó gọi thẳng `_v11015`):

```
hook khi VI PHẠM: {"permission": "deny", "user_message": "CHẶN COMMIT — có tệp bị cắt cụt…"}
khôi phục byte-khớp: True
hook khi SẠCH:   {"permission": "allow"}
```

**`_doc_prepend` vẫn ghép đúng:** `{'truoc': 18, 'sau': 39, 'them': 21}`, khối cũ còn nguyên.

**`_v11040_kiem_dac_trung.py`:**

```
① AST: ml_models.py:31 = 28 cột ✓ · meta_learner.py:51 = 28 cột ✓
② bảng phân rã cộng ra 28 (5+6+3+1+5+2+5+1) ✓
③ quét ngược §60.3: 17 dòng CHU_THICH (giữ) · 0 dòng còn khẳng định số sai
④ ngưỡng hành động FU-320 đã ghi «28 đặc trưng vs 22» ✓
✓ [cong] DAC_TRUNG_V11040=DAT
```

**Chứng minh chặn được (RM-15):** trả ngưỡng về «39 vs 33» *(SỐ CŨ)* ⇒ **mã thoát 1 CHẶN** ·
khôi phục byte-khớp ⇒ **mã thoát 0 cho qua**.

**Loạt cổng chuẩn:**

| cổng | mã thoát |
|---|---|
| `_v11040_kiem_cat_cut.py` | 0 `CAT_CUT_V11040=DAT` |
| `_v11040_kiem_dac_trung.py` | 0 `DAC_TRUNG_V11040=DAT` |
| `_v11027_so_muc_quan_tri.py` | 0 |
| `_v11034_kiem_cheo_quyet_dinh.py` | 0 |
| `_v11028_cong_dong_bang.py` | 0 |
| `_v11015_cong_chan_cat_cut.py` | 0 — không tệp nào ngắn đi bất thường |
| `_v10920_decision_ledger.py` | **2 — `QD-022` TRÔI** ⇒ đã đào tới gốc, ghi `FU-379`, chờ owner |

**Cổng tuổi dữ liệu (RM-01):** `DU_LIEU_TUOI cu=4.06 giờ · ngưỡng=6 giờ` — **ĐẠT**.

**Quét số hiệu BỐN NƠI trước khi cấp mã** (owner bắt buộc in bằng chứng):

```
FU-379     TRỐNG — dùng được      ← đã cấp
FU-380     TRỐNG — dùng được
V11041     TRỐNG — dùng được
QD-048     TRỐNG — dùng được
SC0908-3   ★ ĐÃ DÙNG ở: docs/FOLLOW_UP_TRACKER.md   ← BỎ, đổi sang TD1008
TD1008     TRỐNG — dùng được      ← đã cấp
```

Lần thứ **năm** trong hai ngày quét bắt được va chạm mã đọc. `FU-369` (dựng cổng cấp số hiệu)
càng đáng làm.

---

## 7. Vướng vấp

**7.1 — Agent tự dính RM-09 ngay trong lượt quét ngược của chính mình.** Lượt quét ngược đầu
dùng regex lỏng `vs\s*33`, bắt nhầm `48.17% vs 33.75%` — ba dòng backtest V10636 chẳng liên quan
gì tới đặc trưng ML — rồi báo *«còn 5 chỗ sai»*. Đúng bẫy §60.3 và RM-09 cấm: **đếm chuỗi thô,
không đọc ngữ cảnh**. Đã siết regex (`\b39\s*vs\s*33\b(?!\s*[.,]\d)`) và **phân loại theo ngữ
cảnh** thay vì đếm.

**7.2 — Rồi dính tiếp lần hai, ngược chiều.** Sau khi ghi khối tài liệu V11040, cổng đỏ **3
chỗ** — chính khối báo cáo của em **trích lại số cũ** để kể sự cố. Cám dỗ ở đây là **nới danh
sách từ khoá cho cổng xanh**, và làm thế là làm **yếu** cổng: một dòng khẳng định thật cũng sẽ
lọt. Chọn cách ngược lại — đặt **dấu quy ước bắt buộc `(SỐ CŨ)`**: báo cáo nào trích số sai phải
ghi kèm dấu này trên cùng dòng. Hồi quy thật không bao giờ tự viết «SỐ CŨ», nên cổng giữ nguyên
độ chặt.

**7.3 — Owner trích sai số dòng trong brief, và số dòng vốn không đáng tin.** Brief ghi
`FOLLOW_UP_TRACKER.md:533`; vị trí thật là **1055**. Hai sổ này ghi kiểu prepend nên **mọi số
dòng đều hết hạn ngay lượt ghi sau**. Đã sửa theo **nội dung**, không sửa mù theo số dòng.

**7.4 — Ngày trong brief lệch ngày thật.** Brief gọi «phiên 09/08», đồng hồ là **08/08 23:00**.
Em đã lỡ ghi `2026-08-09` vào ba mặt tài liệu rồi **sửa lại theo đồng hồ**. Sổ ghi theo giờ thật;
nhãn phiên của owner ghi trong ngoặc.

---

## 8. Gỡ về

```bash
git revert <mã commit V11040>
# hoặc lấy lại từng tệp:
git checkout HEAD~1 -- web/backend/_v11015_cong_chan_cat_cut.py web/backend/_doc_prepend.py
rm web/backend/_v11040_kiem_cat_cut.py web/backend/_v11040_kiem_dac_trung.py
```

**Không cần gỡ trên VPS** — không deploy gì. Hai tệp sửa là **cổng kiểm chạy local**, không nằm
trên đường chạy production. `web/backend/main.py` **không nằm trong danh sách tệp sửa**: bộ thử
khôi phục byte-khớp và đã `assert` xác nhận.

**Gỡ FU-347 thì mất số đúng** — cân nhắc: gỡ về là trả ngưỡng FU-320 về «39 vs 33», tức trả lại
một con số **đã chứng minh sai bằng AST**.

---

## 9. Theo dõi tiếp

| mã | việc | trạng thái |
|---|---|---|
| **FU-379 · TD1008 · LX** | bảng tải `QD-022` đếm thiếu từ lúc ký — **hai phương án A/B, chờ owner ký** | `OWNER_DECISION_NEEDED` |
| **FU-369** | cổng cấp số hiệu quét bốn nơi — **đã va chạm 5 lần trong 2 ngày** | GĐ-4, chưa làm |
| **FU-350** | deploy cổng canh model thiếu số (**bỏ lọc `run_source`**) | GĐ-4, chưa làm |
| **FU-360** | `verify_prediction` lọc `run_source` — phải xong **trước 18/08** | GĐ-4, chưa làm |
| **FU-375** | bù báo cáo công khai cho 8 commit từ 25/07 | GĐ-4, chưa làm |
| **57 mục không hạn** | phân loại 3 nhóm, **trình owner ký gộp** — cấm agent tự đặt hạn (RM-06) | GĐ-2, đang làm tiếp |
| **FU-284** | **cấm kết luận trước 21/08** — `_v11033_verdict_fu284.py` đọc ngày đó | đang đo |

**Việc kiểm còn treo sang sáng 09/08** (hai bất khả thi về thời gian, không phải thất bại):
bộ tự kiểm 18:05 phải cho **24 phép gồm C23/C24** (lượt 18:05 hôm nay chạy **trước** khi cổng
deploy lúc 20:09) · cron lane 19:35 phải sinh dòng `la_do_lui=0` (cron cài lúc 20:10).

---

*Báo cáo này đẩy **cùng phiên** với commit, không đợi owner hỏi (A55 · §57.2).*
