# REPORT V11047 — BA LOẠI MỒ CÔI + CỨU HAI TỆP CHỈ CÒN TRÊN MỘT MÁY

**Ngày:** 2026-08-09 13:00–14:00 · **Tầng verdict:** `REPORT_PROVEN` — bảo toàn + phân loại,
chưa đấu nối, chưa kết luận giá trị

## 1. Tóm tắt

Owner đặt **luật ba loại** cho mồ côi. Agent rà lại thì **đã xếp sai một ca** và **phát hiện một
tệp 44,7 KB do chính owner đặt hàng 09/06 đang chỉ tồn tại trên MỘT máy**.

| loại | số ca phiên này |
|---|---|
| **(A) mồ côi thật** → đã gỡ | 4 (dây chuyền viewer) |
| **(B) chưa đấu nối** → cứu, chưa nối | **3** (`__trigger_reload__` · `_v10705` · `_shadow_phase_audit`) |
| **(C) tắt có chủ ý** → giữ nguyên | 1 (V81 provider pilot) |

## 2. Owner yêu cầu gì (nguyên văn)

> trước đó em đã dọn dẹp các mồ côi nào khác không em? các mồ côi thực sự thì có thể xóa gỡ bỏ
> tinh gọn, nhưng các mồ côi do lỗi code chưa đấu nối thì phải đấu nổi và tiếp tục kiểm tra còn
> giá trị phục vụ cho dự án không đã rồi mới có kế hoạch clear, nếu còn thì hạn đo, hoặc gộp
> cung với các phép đo không cần là rõ, đẩy toàn bộ các báo cáo chi tiết lên githubs dùm anh nha em

## 3. Đào bới / phát hiện



### Owner đặt luật mới — agent đã phân loại SAI một ca

> *«các mồ côi thực sự thì có thể xoá gỡ bỏ tinh gọn, nhưng **các mồ côi do lỗi code chưa đấu
> nối thì phải đấu nối** và tiếp tục kiểm tra còn giá trị phục vụ cho dự án không đã rồi mới có
> kế hoạch clear, nếu còn thì **hạn đo**, hoặc **gộp cùng với các phép đo** không cần là rõ»*

**BA LOẠI, cấm gộp:**

| loại | dấu hiệu | xử |
|---|---|---|
| **(A) MỒ CÔI THẬT** | có **người thay thế** rõ ràng + quyết định khai tử | gỡ |
| **(B) CHƯA ĐẤU NỐI** | được xây nhưng **không ai nối dây** | **đấu nối trước**, đo giá trị, rồi mới tính clear |
| **(C) TẮT CÓ CHỦ Ý** | owner quyết / bằng chứng bác bỏ | giữ nguyên trạng thái tắt, ghi lý do |

### Agent xếp SAI `__trigger_reload__.py` — loại (B), không phải (A)

Tệp đó **do API deploy sinh ra** để chạm vào cho `uvicorn --reload` nạp lại mã. Nhưng
`main.py:21228` chạy `uvicorn.run(app, ...)` — **không có `reload=True`**. Đo trên VPS:

| | |
|---|---|
| lượt deploy qua API | **43**, gần nhất **10/05** |
| bước `restart` trong bản ghi | **`skipped`** |
| router | **vẫn mount** (`main.py:190`, `/api/_system/*`) |
| `/api/_system/deploy/health` | **200** |

⇒ API báo *«ok · files written · restart skipped»* trong khi tiến trình **không nạp mã mới** —
chỉ có hiệu lực ở lần restart sau vì lý do khác. **Gỡ tệp không sửa được gì**, API sẽ ghi lại.
Đây là **(B) chưa đấu nối**, đang ngủ.

**Kiểm trước khi báo động (RM-13):** đường **ghi tệp** `POST /api/_system/deploy` **CÓ bảo vệ** —
đòi `X-Deploy-Token`, so sánh constant-time, `token_configured = True` trên production.
**Không phải lỗ hổng.**

### ⭐ CỨU ĐƯỢC: `_v10705_output_total_station.py` — chính thứ owner yêu cầu 09/06

Tệp **44.728 byte · 982 dòng**, chỉ còn **trên VPS**, **xoá khỏi git 05/07** (commit `f86d611`,
gói *«archive 10 oneoff»*), **0 cron · 0 import**. Docstring nguyên văn:

> *«**Owner directive (2026-06-09): độc lập THẬT SỰ theo miền × THỨ × ĐÀI.** `_v10703` mới tới
> (miền×thứ); lane này thêm chiều ĐÀI: chấm độ mạnh model theo (thứ × đài) cụ thể, ra pick RIÊNG
> cho TỪNG ĐÀI»* — ba phương pháp `STWEIGHTED` · `STCHAMPION` · `STBLEND`, **đều causal, chỉ dùng
> quá khứ < target_date**, có **co-rút Bayesian** về region mean cho n nhỏ.

**Đây đúng là thứ agent «đề xuất» trong V11046 §9 Hướng 2** — hoá ra owner đã yêu cầu và đã được
xây từ **09/06**, rồi bị dọn vào «one-off» và không ai nối.

**So với ba anh em cùng họ — nó là ca cá biệt:**

| tệp | trong git | cron | cỡ |
|---|---|---|---|
| `_v10703_output_total_screen` (miền × thứ) | ✅ | **1** | 19,4 KB |
| **`_v10705_output_total_station` (+ ĐÀI)** | ❌ | **0** | **44,7 KB** |
| `_v10707_mnmt_doctrine_shadow` | ✅ | 0 | 42,1 KB |
| `_v10708_mnmt_rule_ranker` | ✅ | **2** | 11,5 KB |

Ba cái kia đều trong git, hai cái có cron. Riêng bản **sâu nhất, to nhất, có chiều ĐÀI** thì
**vừa mất khỏi kho vừa không được nối**.

### Đã làm — BẢO TOÀN trước, đo giá trị sau

Kéo hai tệp từ VPS về kho (`PARSE OK`, quét **0** dấu hiệu bí mật):

| tệp | dòng | vì sao cứu |
|---|---|---|
| `_v10705_output_total_station.py` | 982 | owner directive 09/06, chiều ĐÀI, causal, **chỉ tồn tại trên một máy** |
| `_shadow_phase_audit.py` | 217 | cơ chế nó soi **vẫn sống** (`gpt_analyzer.py:1109-1125` vẫn bắt buộc 3 trường) |

**Chưa đấu nối, chưa chạy, chưa kết luận gì.** Bước này chỉ là **chống mất**: cả hai đang là
điểm hỏng đơn — mất VPS là mất hẳn 44,7 KB công việc owner đã đặt hàng.

### ⚠ CẢNH BÁO PHẢI GHI KÈM — đừng lặp lại lỗi cũ

`_v10705` là công cụ **backtest walk-forward**, không phải materializer (nó in ra màn hình/JSON,
**không `INSERT INTO`** bảng nào). CLAUDE.md ghi thẳng:

> *«Backtest hứa hẹn rồi rữa — **đừng bật lại bằng backtest, chỉ bằng đo tiến**
> (V10655→V10672→V10677→V10753→V10789→V10790 đều rữa)»*

⇒ Kết quả chạy lại `_v10705` **chỉ được dùng để soi**, **CẤM** dùng làm căn cứ bật bất cứ thứ gì.
Muốn nhận thì phải **đo tiến** có ngưỡng đăng ký trước — và **sau 21/08** (QD-041).

### Trả lời câu «trước đó đã dọn mồ côi nào chưa»

Quét git 60 ngày, **7 commit có xoá tệp** trong `web/` hoặc `docs/`, tổng **89 tệp**:

| đợt | xoá | loại |
|---|---|---|
| `bc04e54` 07/08 | 53 tệp `node_modules` | dọn kho, vô hại |
| `3a9b7ac` 02/08 | 24 tệp `.cmd` commit | dọn kho, vô hại |
| **`f86d611` 05/07** | **8 tệp**, gồm **`_v10705`** | ⚠ **xoá nhầm loại (B)** — đã cứu ở trên |
| `0d432bf` · `664b53c` 09/08 | `viewer.html` · `viewer.js` | loại (A), đúng |
| `4aed49b` · `954f58c` | gộp tài liệu · lưu trữ roadmap | vô hại |


---

## 4. Hướng xử lý và vì sao chọn

**Bảo toàn TRƯỚC, đo giá trị SAU.** Cả hai tệp cứu về đều là **điểm hỏng đơn** — mất VPS là mất
hẳn. Kéo về git là việc không thể sai; đấu nối và đo giá trị là việc phải cân nhắc và cần owner.

**KHÔNG chạy `_v10705` vội.** Nó là backtest, và CLAUDE.md ghi 6 lần backtest hứa rồi rữa.
Chạy để soi thì được, dùng làm căn cứ bật thì cấm.

## 5. Đã làm gì

| việc | kết quả |
|---|---|
| kéo `_v10705_output_total_station.py` về git | 44.728 byte · 982 dòng · `PARSE OK` · 0 dấu hiệu bí mật |
| kéo `_shadow_phase_audit.py` về git | 8.102 byte · 217 dòng · `PARSE OK` · 0 dấu hiệu bí mật |
| ghi luật ba loại thành `FU-386` | `STANDING_RULE`, `due: liên tục` |
| ghi khiếm khuyết reload thành `FU-387` | `MEASURED_ROOT_CAUSE`, ba cách xử cho owner chọn |
| ghi hai tệp cứu thành `FU-388` · `FU-389` | `READY_NOT_DEPLOYED`, hạn `LX` (RM-06) |

## 6. Cổng kiểm

`_v11015_cong_chan_cat_cut` **0** · `_v11044_cong_o_status` **DAT** (263 khối đều có ô status) ·
`_v11044_cong_so_hieu`: `V11048` · `FU-390` · `QD-055` trống · phép giãn QD-052: **không ngày nào
vượt trần 6** · cả hai tệp cứu `PARSE OK`, quét **0** dấu hiệu bí mật trước khi đưa vào git.

## 7. Vướng vấp

**Agent xếp sai `__trigger_reload__.py` thành loại (A) và đã gỡ.** Gỡ tệp không gây hại (API sẽ
ghi lại) nhưng **cũng không sửa được gì** — cái sai nằm ở cơ chế, không ở tệp. Đúng luật owner
vừa đặt: loại (B) phải **đấu nối**, không phải gỡ.

**Suýt báo động sai lần nữa.** Khi thấy `/api/_system/deploy/health` trả **200 không auth**, agent
kiểm tiếp đường **ghi tệp** trước khi kết luận: `POST /deploy` đòi `X-Deploy-Token`, constant-time
compare, `token_configured=True`. **Không phải lỗ hổng.**

## 8. Gỡ về

```bash
git rm --cached web/backend/_v10705_output_total_station.py web/backend/_shadow_phase_audit.py
git revert <commit V11047>
```
Hai tệp vẫn còn trên VPS — gỡ về không mất gì.

## 9. Theo dõi tiếp

| mã | việc | chờ ai |
|---|---|---|
| `FU-387` | chọn cách xử reload: (a) `reload=True` · (b) API tự restart · **(c) báo thật `MANUAL_REQUIRED`** ← khuyến nghị | **owner** |
| `FU-388` | chạy soi `_v10705` (chỉ soi, cấm làm căn cứ) rồi quyết có dựng đo tiến không | **owner** |
| `FU-389` | **gộp** vào bộ tự kiểm 18:05 thay vì dựng cron riêng | **owner** |
| — | vá biên `anchor_date <= date(?,'-1 day')` chống lookahead | ngay, trước khi bật lại tensor |

---

## LOCK-IN / OPEN / NEXT ACTION

**LOCK-IN:** luật ba loại vào sổ (`FU-386`, luật đứng) · hai tệp chỉ-còn-một-máy **đã vào git** ·
khiếm khuyết reload đã đo và ghi (`FU-387`) · trả lời được «trước đó đã dọn mồ côi nào»: 7 commit
/ 89 tệp, trong đó **1 đợt xoá nhầm loại (B)** đã cứu.

**OPEN:** ba câu ở §9 chờ owner · và toàn bộ 6 mục xin ký ở báo cáo V11046 vẫn treo.

**NEXT ACTION:** vá biên chống lookahead (ngay) · gộp `_shadow_phase_audit` vào 18:05 nếu owner
duyệt · tối nay đọc log 18:05 + 19:35 đóng `FU-373` / `FU-366`.

*Đẩy cùng commit (A55 · §57.2).*
