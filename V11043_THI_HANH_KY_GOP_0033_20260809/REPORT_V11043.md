# REPORT V11043 — THI HÀNH KÝ GỘP 00:33 · ĐÓNG 43 MỤC · GỠ `viewer.html`

**Ngày:** 2026-08-09, 00:38 → 02:00 giờ VN
**Phiên bản:** V11043 · **Tầng verdict:** `RUNTIME_PROVEN` cho phần deploy (đo trên production) ·
`REPORT_PROVEN` cho phần sổ sách

---

## 1. Tóm tắt

Owner ký gộp **00:33 09/08** sáu quyết định. Thi hành **5/6**; món thứ sáu (`FU-380`) owner đã
ký là *chờ 21/08* nên **cố ý không làm**.

| # | quyết định | kết cục |
|---|---|---|
| 1 | bảng 57 mục: A=43 đóng · C=5 luật đứng · B=9 verify rồi trình lại | ✅ **xong** — treo **183 → 135** |
| 2 | `FU-381` B1 phương án A | ✅ **xong** — sửa mô tả **7 chỗ**, không đụng code |
| 3 | `FU-382` chỉ bỏ `viewer.html` | ✅ **xong + deploy** — kèm **5 chỗ** trỏ vào nó |
| 4 | `FU-383` giữ V10750, không bật phase-first | ✅ **xong** — ghi **xác nhận lại**, không tạo quyết định ngược |
| 5 | `FU-379` theo khuyến nghị agent | ✅ **đóng** |
| 6 | `FU-380` chờ 21/08 | ⏸ **cố ý không làm** — hạn 21/08, rủi ro ghi rõ |

**Và một phát hiện lớn hơn hẳn đề bài:** **một nửa sổ `FOLLOW_UP_TRACKER.md` chưa bao giờ được
đếm** — 384/768 khối, **640 KB (47,7%)**, vô hình với mọi bộ đếm.

---

## 2. Owner yêu cầu gì (nguyên văn)

> **OWNER SIGNATURE: Owner ký gộp 00:33 09/08 — sáu quyết định:**
> (1) BẢNG 57 MỤC (V11041): KÝ A=43 ĐÓNG + C=5 giữ luật đứng (liên tục, không đặt hạn) · nhóm
> B=9: agent tự mở từng trang/endpoint VERIFY còn sống rồi TRÌNH LẠI (cấm tự đặt hạn — RM-06).
> Quyết định này MỞ KHOÁ GĐ-3 dọn sổ FOLLOW_UP;
> (2) FU-381 (B1): phương án A — GIỮ cơ chế cổng CHẶN số ở main.py:10704, sửa câu mô tả sai
> trong tài liệu (§60);
> (3) FU-382 (FU-224): CHỈ BỎ viewer.html (file chết); GIỮ /v82-monitor · /user-view ·
> /api/filter-2-so-cuoi · /nghiem-thu;
> (4) FU-383 (P2): GIỮ trạng thái hiện tại theo V10750 — KHÔNG bật lại phase-first;
> (5) FU-379: theo khuyến nghị agent trong bảng A/B;
> (6) FU-380: CHỜ 21/08 — cấm vá roster giữa cửa sổ đo FU-284.

---

## 3. Đào bới / phát hiện

### 3.1 — GĐ-1: hai phép kiểm sống **chưa quan sát được**, nhưng dây nối đã chứng minh đúng

Owner đặt V1/V2 là *«bộ tự kiểm 18:05 **hôm nay**»* và *«cron lane 19:35 **hôm nay**»*. Đồng hồ
lúc bắt đầu: **00:38** — hai mốc đó còn **17,4 giờ** và **19 giờ** nữa. Không thể quan sát.

Nhưng thứ **kiểm được ngay** là dây nối, và nó khớp khít:

| đo | kết quả |
|---|---|
| cron `5 18 * * *` gọi `_v10900_consistency_guard.py` | **có** trong crontab VPS thật |
| bản **trên VPS** có `C23`/`C24` | **có** — `:614` `C23_vung_ban_dung_bien` · `:618` `C24_khong_sai_nhan_moi` |
| số phép | **21** lần `add("C…")` = C4…C24, **+3** phép trong vòng lặp MN/MT/MB = **24** |
| log 08/08 18:05 ghi **22** | **= 24 − 2**, vì lượt đó chạy **trước** khi C23/C24 deploy lúc **20:09** |

⇒ Số 22 hôm qua **được giải thích trọn vẹn**. Tối nay 18:05 phải ra **24**.

**Trôi phát hiện kèm:** `_v10900_consistency_guard.py` local **732 dòng** vs VPS **694** — lệch
**38 dòng**, là khối V11023 *«không đọc được crontab thì nói KHÔNG ĐO ĐƯỢC, đừng nói HỎNG»*, chỉ
có ở local. Trên VPS crontab đọc được nên hành vi giống hệt, nhưng **vẫn là trôi** (K3).

**V2:** lane `v11037_g2mb_lane` có **549 dòng, tất cả `la_do_lui=1`** (nạp lùi), **0 dòng đo
tiến**. Cron cài lúc 20:10 hôm qua ⇒ lần nổ đầu là 19:35 tối nay.
**V3:** `bay_dan_daily_shadow` 66 dòng / 22 ngày, mới nhất 07/08 — **ghi nhận, không kết luận**.
**V4:** `HAN_KE_THUA_V11038=DAT`; **6 mục** đến hạn 09/08, đúng bằng trần QD-052.

### 3.2 — Nhóm B: **401 là ĐÚNG, không phải chết**

Cả ba trang trả **401** vì đều gọi `require_admin` (`main.py:16226` · `:16244` · `:18486`).
Ba tệp HTML local và VPS **trùng khớp byte**. Bảng đầy đủ ở §5.3.

### 3.3 — `viewer.html` chết thật, nhưng **năm** chỗ còn trỏ vào nó

Chết: không route serve (`/viewer` chỉ `RedirectResponse` 307) · **không** `StaticFiles` mount
nào trong kho · 0 inbound link · nginx `proxy_pass` thuần, không static root · `curl` = **404** ·
nhật ký nginx **14 bản xoay: 0 hit `/viewer.html`**.

Nhưng gỡ mỗi tệp là **bỏ nửa chừng**. Năm chỗ, **một trong đó đang serve thật**:
`_v87_master_board.py:378` — bảng tra cứu hiển thị trên `/monitoring`, vẫn quảng cáo tệp đã xoá.

### 3.4 — MỘT NỬA SỔ `FOLLOW_UP_TRACKER.md` VÔ HÌNH

Bộ đọc chỉ khớp `### FU-<số>` (`_v10958_fu_reader.py:44-46`). Tệp có **768** tiêu đề `###`:

| | |
|---|---|
| khối bộ đọc **THẤY** | **384** |
| khối **KHÔNG BAO GIỜ THẤY** | **384** — **640,1 KB (47,7%)** · **5.669 dòng (39,7%)** |
| thành phần | **357 khối `### FU-V<version>-…`** di sản · 25 tiêu đề `###` khác · 1 template · **1 khối FU THẬT bị bỏ sót** |
| nhãn status riêng trong vùng vô hình | **199** *(vùng thấy được chỉ có 26)* |

**`FU-330` mất tích thật:** dòng 941 ghi `### A1 / FU-330 · ĐÃ LÀM …` — tiền tố `A1 / ` làm
trượt regex ⇒ `load_fu_latest()` **không có `FU-330`**. **Lần thứ tư** của họ lỗi
V10980 / FU-353 / FU-370.

**Hệ quả:** thân khối chạy tới `### FU-<số>` kế tiếp ⇒ **`FU-185` nuốt 573 KB** (dòng
5912→11104), `FU-117` nuốt 238 KB. Trạng thái của chính ba mục đó vẫn đúng, nhưng **bất kỳ công
cụ nào đọc cả thân sẽ đọc nhầm hàng trăm mục khác**.

**Trùng lặp:** 384 khối / 256 mã ⇒ **chênh 128** · **86 mã trùng**, hai mã lặp **5 lần**.

⇒ **Mọi con số về sổ theo dõi từ trước tới nay đều tính trên một nửa tệp.**

---

## 4. Hướng xử lý và vì sao chọn

**`STANDING_RULE` phải dạy bộ đọc TRƯỚC.** Nhãn đó không nằm trong `TREO_STATUSES` lẫn
`DONG_STATUSES` ⇒ `trang_thai_mo_coi()` sẽ bêu cả 5 mục là **mồ côi**. Ép vào `TREO` là phình
tồn đọng bằng thứ không bao giờ giảm; ép vào `ĐÓNG` là **tắt một cổng đang canh tiền thật**
(`FU-208`). Nên khai **loại thứ ba** `LUAT_DUNG_STATUSES`.

**Lời owner trong `FU-381` giữ nguyên văn.** Chỉ sửa số dòng kèm theo và thêm dòng kết luận —
sửa lời owner cho khớp code là **ghi đè lịch sử**.

**GĐ-3 dọn sổ: KHÔNG làm trong phiên này.** Sửa regex là **đổi thứ mọi bộ đếm dựa vào**, trong
một phiên đã sửa sổ 5 lần và đã băm tiêu đề một lần. Ghi `FU-384`, hạn 10/08.

---

## 5. Đã làm gì

### 5.1 — Bảng 57 mục · §60.4

| | TRƯỚC | SAU |
|---|---|---|
| treo | **183** | **135** (−48) |
| đã đóng | 65 | **108** (+43) |
| luật đứng *(loại mới)* | 0 | **5** |
| tiêu đề bị băm | — | **0** |

43 mục nhóm A đóng, mỗi mục **một dòng lý do trỏ bằng chứng** ghi thẳng vào ô `status`, **giữ
nguyên nhãn cũ** trong chính ô đó. Bốn kiểu lý do: *chờ bảng đã ngừng nhận dòng* · *chờ cron đã
bị cắt* · *cửa sổ chờ 14/30 ngày mở từ 05/2026* · *tự khai đã giải quyết*.

### 5.2 — `FU-381`: TRƯỚC → SAU, **7 chỗ**

**TRƯỚC:** *«hệ luôn xuất số kể cả khi bundle rỗng»*
**SAU:** *cổng **CHẶN** số — `publish_ready=False` ⇒ API thay bundle (đã có đủ số trong
`final_bundles`) bằng `None` ⇒ `du-doan.html` `return` sớm ⇒ **0 ô số***

`FOLLOW_UP_TRACKER` món nợ #2 · `CHANGELOG.md:436` · `CURRENT_TRUTH_SSOT.md:84` ·
`UI_V2_LOCAL_PLAN.md` ×4.

**Số dòng đính chính:** `10704`/`10767`/`10818` → **`10770`/`10833`/`10884`**. Chúng đúng ở
commit `207404c`, nhưng **chính commit `922b08f` (V11042 — commit ghi ra `FU-381`)** chèn khối
`TRUONG_KHACH_DUOC_XEM` ở `main.py:6378` làm cả vùng trôi **+66 dòng**.

**Sai kép được bắt:** câu cũ ghi *«nới `_confidence_gate`/`publish_gate`»* — `_confidence_gate`
**có thật** (`main.py:10507`) nhưng **không nằm trên đường `/api/final-bundle`**.

### 5.3 — 🖊️ BẢNG NHÓM B, TRÌNH OWNER (không đặt hạn — RM-06)

| mã | đường dẫn | HTTP | còn sống thật? | đề xuất |
|---|---|---|---|---|
| `FU-118` | `/du-doan-test` | 401 | **SỐNG** — 5 khoá payload có thật | owner mở bằng admin |
| `FU-131` | `/du-doan-test` «Trải nghiệm hôm nay» | 401 | **SỐNG** — builder trả 15 khoá cho cả 3 miền | owner mở bằng admin |
| `FU-149` | `/v82-monitor` | 401 | **SỐNG** — payload 18 khoá, sinh `2026-08-09T00:46:14` | **hỏi trước**: `v81_provider_pilot_recent = 0` là cố ý hay hỏng? |
| `FU-152` | `/monitoring` → `sectionV82MasterControl` | 401 | **SỐNG** | **sửa mô tả**: hết auto-refresh |
| `FU-153` | `/monitoring` → `sectionV87MasterIndex` | 401 | **SỐNG** — đủ 12 tab gốc | **sửa nhãn**: tiêu đề ghi «(12 tab)» trong khi có **29 nút** |
| `FU-154` | `/monitoring` → 6 tab V88 | 401 | **SỐNG** — đủ 6 nhãn | owner mở bằng admin |
| `FU-155` | `/monitoring` → 6 tab V89 | 401 | **SỐNG** — `migrations=3` `decision_log=22` `governance_ledger=96` | owner mở bằng admin |
| `FU-156` | `/monitoring` → 5 tab V90 | 401 | **4/5 SỐNG · 1 TAB HỎNG** | **chưa nghiệm thu được** — `FU-385` |
| `FU-300` | không phải trang | — | `AWAITING_OWNER_OK`, hạn `RM-LX` | chỉ ghi nhận |

`FU-152` và `FU-149` **chồng nhau** — V86 đã gộp `/v82-monitor` vào `/monitoring`; owner nghiệm
thu **cả hai trong một lần** mở `/monitoring`.

### 5.4 — `FU-382`: gỡ `viewer.html` + **5 chỗ**

| # | chỗ | vì sao phải xử |
|---|---|---|
| ① | `_v87_master_board.py:378` | **THAM CHIẾU SỐNG** — bảng tra cứu trên `/monitoring` |
| ② | `_v10866_deploy.py:97` | `texts['viewer.html']` không guard ⇒ **KeyError** |
| ③ | `_v10781_deploy.py:33` | bản kê deploy |
| ④ | `_v10848_drift_audit.py:164` | cổng so lệch (đăng ký playbook §2) |
| ⑤ | `_v10780_phase1_verify.py:161` | vòng lặp `grep` |

**Deploy:** `_v87_master_board.py` lên VPS · `viewer.html` + **3 tệp `.bak`** trong thư mục serve
→ `backups/v11043_viewer/`. **PID 1112152 → 1118902** · health **200** · `/viewer.html` **404** ·
`/du-doan` **200** · `/monitoring` **401**.

**CÒN MỒ CÔI — báo owner, KHÔNG tự gỡ:** owner chỉ ký bỏ `viewer.html`, nên `viewer.js`
(9.306 byte, `/viewer.js` vẫn **200**) · `/api/viewer/predictions` (`main.py:4260`) ·
`/api/viewer/today` (`main.py:4279`) **thành 100% mồ côi**.

### 5.5 — Sổ quyết định

`QD-054` (gói ký gộp 00:33) · `QD-049`/`QD-051`/`QD-053` → `ACTIVE` + `owner_chot`.
`QD-053` cố ý để `thay_the: []` và thêm `can_cu_goc` trỏ V10750 — ghi nó thành quyết định mới
«giữ phase-first» sẽ tạo **hai quyết định cùng ACTIVE nói về một thứ**, dù cùng chiều vẫn là
chồng tầng (§60). **56 quyết định.**

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v11043_thi_hanh_57.py` | 0 `THI_HANH_57_V11043=DAT` |
| `_v11042_gian_lich.py --ap-dung` | 0 `GIAN_LICH_V11042=DAT` — mọi ngày tương lai ≤ 6 |
| `_v11042_kiem_status_khach.py` | 0 `STATUS_KHACH_V11042=DAT` |
| `_v11040_kiem_cat_cut.py` | 0 `CAT_CUT_V11040=DAT` |
| `_v11040_kiem_dac_trung.py` | 0 `DAC_TRUNG_V11040=DAT` |
| `_v11038_kiem_han_ke_thua.py` | 0 `HAN_KE_THUA_V11038=DAT` |
| `_v11034_kiem_cheo_quyet_dinh.py` | 0 `KIEM_CHEO_QD=SACH` |
| `_v11028_cong_dong_bang.py` | 0 `DONG_BANG_QD041=CON_NGUYEN` |
| `_v11015_cong_chan_cat_cut.py` | 0 — **gọi TRƯỚC mỗi lần ghi sổ** (FU-378) |
| `_v10920_decision_ledger.py` | **1 phép trôi — BẰNG lúc bắt đầu phiên** (`QD-027`, hiện tượng nửa đêm) |

**Quét số hiệu BỐN NƠI:**

```
QD-054 QD-055 V11044 FU-384 FU-385 TK0909 DD0909 KS0909-2   TRỐNG — dùng được
V11043   ★ "đã dùng" — nhưng là 48 ô status do CHÍNH script này vừa ghi, không phải va chạm
QD0909   ★ ĐÃ DÙNG THẬT (FU-354) — BỎ
```

**4 bảng khoá:** không đụng ngoài SELECT. **QD-041 còn nguyên.**

---

## 7. Vướng vấp

**7.1 — Agent tự dính RM-09 lần nữa.** `grep -c '_v10848|_v10781|_v10780'` trên crontab VPS trả
**3**, và agent suýt kết luận *«ba cron đang gọi các script trỏ tới `viewer.html`»*. Đọc lại từng
dòng: **cả ba đều bắt đầu bằng `#`** (đã tắt) và trỏ tới `_v10781_prompt_v2_lane.py` — **một tệp
khác hẳn**. Đếm chuỗi thô mà không lọc `^#`. Nếu tin con số đó thì đã không gỡ `viewer.html`.

**7.2 — Lặp lại đúng lỗi «quên ô `status`» sau hai giờ.** `FU-385` viết thiếu
`| **status** | … |` ⇒ bộ đọc trả chuỗi rỗng. Đây là **lần thứ hai trong một đêm** (lần đầu:
`FU-381/382/383`). Một lỗi lặp hai lần thì theo §61 phải thành **cổng máy**, không được chỉ hứa —
ghi vào `FU-384` như một hạng mục con.

**7.3 — Assert chặn đúng lúc.** Lượt gỡ `viewer.html` đầu tiên dùng `\n` trong khi tệp là CRLF ⇒
`assert` fail ⇒ **script dừng trước khi xoá tệp**. Nếu viết `if count==1: replace` mà không
assert thì đã lặng lẽ bỏ qua bốn chỗ trỏ vào và vẫn xoá tệp.

**7.4 — Một agent điều tra tưởng có phiên song song.** Nó báo *«tệp đang bị một phiên SONG SONG
sửa»* — thực ra là **chính phiên này** đang ghi sổ trong lúc nó đọc. Nó xử lý đúng: chụp lại một
bản, chốt số trên bản chụp, rồi đối chiếu với bản live. Nhưng câu chữ có thể làm người đọc hiểu
nhầm là vi phạm luật PARALLELISM — **không phải**.

**7.5 — Thêm mục mới làm vỡ trần giãn.** Ghi `FU-384`/`FU-385` vào 10/08 làm ngày đó lên **8**,
vượt trần QD-052. Chạy lại phép giãn ⇒ về **6**. Bài học: **thêm mục cũng là đổi tải**, phải
chạy lại phép giãn sau khi thêm.

---

## 8. Gỡ về

```bash
# sổ theo dõi (43 mục đóng + 5 luật đứng)
cp backups/v11043_pre/FOLLOW_UP_TRACKER.md docs/FOLLOW_UP_TRACKER.md

# viewer.html + 5 chỗ tham chiếu
cp backups/v11043_pre/viewer.html web/frontend/
cp backups/v11043_pre/_v87_master_board.py backups/v11043_pre/_v10866_deploy.py web/backend/

# trên VPS
ssh root@14.225.224.89 'cd /root/Lottery_AI_Test && mv backups/v11043_viewer/* web/frontend/ && systemctl restart lottery'

git revert 0d432bf
```

---

## 9. Theo dõi tiếp

| mã | việc | trạng thái |
|---|---|---|
| **nhóm B · 9 mục** | **owner mở bằng tài khoản admin** rồi nghiệm thu | 🖊️ **chờ owner** |
| `FU-149` | `v81_provider_pilot_recent = 0` — cố ý hay hỏng? | 🖊️ **chờ owner** |
| **`viewer.js` + 2 endpoint** | mồ côi 100% sau khi gỡ `viewer.html` — gỡ luôn hay giữ? | 🖊️ **chờ owner** |
| `FU-384` | **một nửa sổ vô hình** — sửa regex + gộp 128 khối trùng | hạn **10/08** |
| `FU-385` | tab «Cursor Rules» hỏng hai tầng | hạn **10/08** |
| `FU-380` | hai danh sách cứng trôi khỏi registry | **chờ 21/08** theo lệnh owner |
| `FU-369` `FU-350` `FU-377` `FU-360` `FU-375` | hàng đợi GĐ-4 | **chuyển 10/08** — owner cho phép, cấm dồn |
| **tối nay 18:05 / 19:35** | 24 phép gồm C23/C24 · lane sinh dòng `la_do_lui=0` | chờ cron nổ |

---

## LOCK-IN / OPEN / NEXT ACTION

**LOCK-IN** — chốt, có bằng chứng máy:
43 mục đóng kèm lý do, treo **183 → 135**, **0** tiêu đề băm, đọc lại bằng bộ đọc thật ·
`viewer.html` gỡ khỏi cả local và production, **5 chỗ** trỏ vào nó đã xử, health 200 ·
câu mô tả B1 sửa **7 chỗ** · loại thứ ba `LUAT_DUNG_STATUSES` để 5 luật đứng không thành mồ côi ·
mọi ngày tương lai ≤ trần 6 · QD-041 còn nguyên · trôi **không tăng**.

**OPEN** — chờ owner: nghiệm thu 9 mục nhóm B bằng tài khoản admin · `v81_provider_pilot_recent`
rỗng · dây chuyền mồ côi `viewer.js`.

**NEXT ACTION** — không cần owner, chuyển **10/08**: `FU-384` (một nửa sổ vô hình — **việc nặng
nhất còn lại**) · `FU-385` · rồi hàng đợi GĐ-4 `FU-369` → `FU-350` → `FU-377` → `FU-360` →
`FU-375`. Và **tối nay** đọc log 18:05 + 19:35.

---

*Báo cáo này đẩy **cùng phiên** với commit (A55 · §57.2).*
