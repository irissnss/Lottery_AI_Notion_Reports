# REPORT V11058 — THI HÀNH TẦNG AN TOÀN: A1·A2·A3 + B1·B4 · VÀ MỘT TÍN HIỆU DƯƠNG BỊ RÚT LẠI

**Ngày:** 2026-08-10 đêm · **Quyết định owner:** `QD-058` · **Mã đọc:** `TH1008`
**Production:** PID `1286954` → **`1345720`** · health 200 · **hash 4 bảng khoá PRE = POST y hệt**

---

## 1. Tóm tắt

Owner: *«Các đề xuất an toàn tiến hành ngay được thì tiến hành xử lý đi em… đảm bảo chỉ có cải
tiến nâng cao chính xác dự đoán nha em đừng đi lùi nữa»*.

Đã thi hành **năm việc**, **không việc nào đổi hành vi production** — tất cả chỉ **thêm phép đo**:

| # | việc | kết quả |
|---|---|---|
| **A1** | đính chính nhãn tầng trong `REPORT_V11055` | banner đủ TRƯỚC/SAU/PHIÊN BẢN/KIỂM (§60.4) |
| **A2** | luật **RM-21** *«hằng số đo được chỉ đúng cho thước đã đo nó»* | vào **đủ sáu mặt** governance |
| **A3** | **BẢNG n-CẦN CHUẨN** đặt đầu `FOLLOW_UP_TRACKER` | +10pp→29 ngày · +5pp→115 ngày · +3pp→319 ngày |
| **B1** | **đo tiến ANTI-TRAP** đủ §52 | bảng 336 dòng · API · panel · cron 21:45 · cổng 6/6 |
| **B4** | đo nhánh **CHỐT GẤP** | **+0,40 chạy ở 69/90 miền-ngày = 76,7%** |

**Và một tín hiệu dương bị chính agent rút lại.** B4 ban đầu cho `+11,5pp · z=+1,77` — con số
**dương đầu tiên** sau nhiều phiên. Kiểm ra: **cả 105 luật được đào lúc `2026-08-10 00:30`**, nên
mọi ngày em chấm ngược đều **nằm TRONG cửa sổ đào luật**. Đó là **khớp trong mẫu**, không phải
lợi thế. **Rút lại.**

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«Các đề xuất an toàn tiến hành ngay được thì tiến hành xử lý đi em, còn gì chưa rõ, chưa xác
> định thì tiếp tục đảm bảo chỉ có cải tiến nâng cao chính xác dự đoán nha em đừng đi lùi nữa»*
> — 10/08

Hai vế, và vế sau định đoạt cách làm: **«đừng đi lùi»** ⇒ mọi thứ thi hành đêm nay đều **chỉ
THÊM phép đo**, không gỡ gì, không đổi hành vi nào của đường sinh số.

---

## 3. Đào bới / phát hiện

### 3.1 · B4 — nhánh CHỐT GẤP bơm **+0,40**, gấp **2,7 lần** con số mọi tài liệu vẫn nhắc

`combo_super.py:1901` có **bảng bonus riêng**, khác hẳn `BOOST_TABLE` của Phase 4:

```python
_chot_bonus = {'shadow': 0.0, 'soft': 0.40, 'active': 0.80}.get(_rm, 0.0)
```

Chế độ đang chạy là `soft` ⇒ **+0,40 mỗi đuôi hội tụ**. Trong khi mọi báo cáo — kể cả
`CHANGELOG.md:222` — đều nói *«MINED_RULES đang cộng **+0,15**»*, tức trần của **nhánh khác**.

**Nhánh này có thật sự chạy không?** Journal `lottery` là **volatile** (`/run/log/journal`) nên
«0 dòng log» **không chứng minh được gì** (RM-20). Nên em đo **ĐẦU VÀO** của nhánh thay vì gắn
thiết bị đo vào mã (chạm module sinh số ⇒ `QD-041` khoá): gọi thẳng
`extract_rule_candidates_v2` — **đúng hàm production**, đã kiểm **0 câu ghi** (0 INSERT/UPDATE/
DELETE/commit).

| | |
|---|---|
| miền-ngày đo | **90** (30 ngày × 3 miền) |
| `convergence_map` **KHÔNG rỗng** | **69 = 76,7%** |
| ví dụ 10/08 MN | `{21: 3, 77: 2, 29: 2, 97: 2}` — mỗi đuôi **+0,40** |
| combo-super MN xuất ra hôm đó | **`['97', '21']`** — **cả hai đều trong tập hội tụ** |

⇒ **Nhánh CHỐT GẤP đang sống, chạy 3/4 số ngày, và định hình output của combo-super.**

### 3.2 · Tín hiệu dương `+11,5pp` — và vì sao phải RÚT LẠI

Đo tiếp: trong 138 số combo-super xuất ra trên 69 miền-ngày có hội tụ,

| nhóm | trúng | so nền 33,8% | z |
|---|---|---|---|
| **trong** tập hội tụ (được +0,40) | 24/53 = **45,3%** | **+11,5pp** | **+1,77** |
| **ngoài** tập hội tụ | 17/85 = 20,0% | −13,8pp | −2,69 |

Nhìn thì rất mạnh — số được bơm trúng nhiều hơn hẳn số không được bơm.

**Câu hỏi chặn:** em gọi hàm **hôm nay** cho **ngày quá khứ**. Bộ luật có khoá theo thời điểm không?

```sql
-- get_active_rules (rule_engine.py:262-266) — TOÀN BỘ mệnh đề WHERE:
WHERE target_region = ? AND target_weekday = ?
  AND (is_active = 1 OR activation_status = 'active')
  AND production_tier IN (…)
```

**Không có một bộ lọc thời điểm nào.** Không `mined_at <= target_date`, không gì cả.

Và:

```
mined_at của cả 105 luật: 2026-08-10T00:30:00 → 2026-08-10T00:30:11
```

**Cả 105 luật được đào lúc 00:30 SÁNG NAY.** Thống kê của chúng (`lift_365` · `hit_rate_365` ·
`hr_4w`…`hr_16w`) tính trên dữ liệu **đến 10/08**. Nên **toàn bộ 30 ngày** em chấm ngược
(12/07 → 10/08) đều **nằm TRONG cửa sổ đào luật**. Luật được **chọn chính vì** nó khớp đúng
những ngày đó.

Chữ ký khớp quá mức lộ rõ trên chính dữ liệu luật: `hr_4w = 1,0 · hr_8w = 1,0 · hr_12w = 1,0` —
một luật trúng **100% suốt 12 tuần**.

**Và đây là hiện vật ĐÃ ĐƯỢC ĐO TRƯỚC.** `RM-18` ghi thẳng: *«luật hơn nền +7,5/+13,8/+20,7 điểm
**trong** cửa sổ chọn nhưng **đúng bằng 0** ngoài cửa sổ»* (V11030). Em vừa tái tạo lại **đúng
hiện vật đó** rồi suýt báo nó như phát hiện mới.

> **RÚT LẠI `+11,5pp`.** Nó là **khớp trong mẫu**, không phải lợi thế. Muốn biết nhánh CHỐT GẤP
> có giá trị hay không thì **chỉ có một cách**: đo tiến trên luật đào **trước** ngày dự đoán —
> tức phải thêm `mined_at <= target_date` vào truy vấn, mà việc đó **chạm đường sinh số**
> ⇒ **PLAN 21/08**.

### 3.3 · B1 — đo tiến ANTI-TRAP, và vì sao chọn thước «xấu hơn» nhưng KHẢ THI

Hai thước ứng viên. Em tính **n-cần cho cả hai** rồi mới chọn (RM-03 đòi «tính sức mạnh»):

| thước | n cần | tốc độ tích luỹ | ⇒ bao lâu | chọn? |
|---|---|---|---|---|
| **A · McNemar phép thay số** | 72 cặp lệch | 0,079/ngày | **910 ngày ≈ 30 tháng** | ✗ |
| **B · so tỉ lệ `FULL_SPENT` vs `FRESH`** | 90 quan sát (đang có **51**) | 0,31/ngày | **thêm 124 ngày ≈ 4,1 tháng** | ✓ **CHÍNH** |

Thước A có vẻ «đúng câu hỏi hơn» (nó đo trực tiếp phép thay số), nhưng **đặt hạn cho một thước
cần 30 tháng là đúng thứ `RM-06` cấm**. Nên A vẫn được ghi lại nhưng **KHÔNG đặt hạn**.

```
NGƯỠNG ĐĂNG KÝ TRƯỚC (10/08/2026 — cấm đổi sau khi thấy số):
  · thước    : tỉ lệ trúng bạch thủ, nhóm FULL_SPENT vs nhóm FRESH
  · gộp      : Mantel–Haenszel PHÂN TẦNG THEO MIỀN (nền MT/MB lệch ~3 lần)
  · điều kiện: n(FULL_SPENT) >= 90  VÀ  |z_MH| >= 1,96
  · VIF      : đo lại cho CHÍNH thước này (RM-21)
  · đọc sớm  : CẤM — chưa đủ n thì ghi đúng chữ «chưa được phép kết luận» (RM-04)
```

Bảng đã nạp **336 dòng**, và ghi lại một con số đáng chú ý: **51 lần** bundle **có** cảnh báo
anti-trap mà **vẫn công bố**.

---

## 4. Hướng xử lý và vì sao

### 4.1 · Vì sao KHÔNG đẻ cổng thứ hai cho B1

Sổ V11054 đã liệt kê **sáu chỗ trùng lặp** (`T1`–`T6`): thang trạng thái luật có **4 bản**, cửa
sổ tuần có **3 cách**, `_family()` có **2 bản**. Đẻ thêm một cổng §52 thứ hai là **làm dày đúng
cái đống đó**.

Nên em **mở rộng cổng có sẵn** `_v11055_kiem_p4.py` thành **sổ đăng ký `BO_DO`** — một cổng soi
**tất cả** phép đo shadow. Thêm phép đo mới sau này chỉ cần thêm một mục vào danh sách.

### 4.2 · Vì sao K6 (nhìn trộm) khai «KHÔNG ÁP» thay vì lặng lẽ bỏ qua

B1 chỉ **đọc nhãn đã lưu** trong `final_bundles`, không tự tính gan ⇒ không có cột nào để soi
dấu nhìn trộm. Cổng khai `cot_nhin_trom=None` và **in ra lý do**, thay vì bỏ qua im lặng.
**Bỏ qua im lặng là cách cổng chết dần** — đúng bài học cổng đóng băng QD-041 từng mù hoàn toàn.

### 4.3 · «Đừng đi lùi» — em hiểu và thi hành thế nào

Không việc nào đêm nay **gỡ** thứ gì hay **đổi** hành vi nào của đường sinh số:

- A1/A2/A3 chỉ sửa **tài liệu và sổ luật**
- B1 **thêm** một bảng shadow đọc từ dữ liệu đã có sẵn
- B4 chỉ **gọi đọc** một hàm production, không ghi gì

Bằng chứng: **hash 4 bảng khoá PRE = POST y hệt** (`12199/8bdbf0131cb3` · `492/4fe3f3b6c481` ·
`15253/0b02cd675ce9` · `12063/2dac7ddfc665`).

---

## 5. Đã làm gì (deploy)

| # | việc | bằng chứng |
|---|---|---|
| 1 | Backup `main.py` · `monitoring.html` · `crontab` | `backups/*.pre_v11058` (135 dòng cron) |
| 2 | Bảng `anti_trap_shadow_v11058` nạp trên production | **336 dòng**, cờ shadow đúng 4/4 |
| 3 | API `/api/admin/anti-trap-shadow` | `require_admin` + `no-store`, **chỉ đọc** |
| 4 | Panel `/monitoring` §52B | đăng ký **cả** `loadAllSections` **lẫn** `setInterval` 60s |
| 5 | Cron **21:45** (sau P4 21:40) | crontab 135 → **136** dòng, **0** dấu `\&` hỏng |
| 6 | Cổng §52 mở rộng thành sổ đăng ký `BO_DO` | **P4 6/6 · B1 6/6 · thử chặn ĐẠT cho từng phép** |
| 7 | RM-21 vào **đủ sáu mặt** | `_v10925_rule_sync_check.py` → **SÁU MẶT ĐỒNG BỘ** |

**Restart:** PID `1286954` → **`1345720`** · health 200 · `/du-doan` 200 · admin 401 ·
**0** traceback/CRITICAL/ERROR · **hash 4 bảng khoá PRE = POST y hệt**.

---

## 6. Cổng kiểm — xác minh

| cổng | kết quả |
|---|---|
| `_v11055_kiem_p4.py --thu-chan` **trên VPS** | `P4_GAN_HOI_TU_V11055=DAT` · `B1_ANTI_TRAP_V11058=DAT` · thử chặn **ĐẠT cho từng phép** |
| `_v10925_rule_sync_check.py` | **SÁU MẶT ĐỒNG BỘ** sau khi thêm RM-21 |
| `_v11044_cong_so_hieu.py` | V11058 · FU-397 · QD-058 là số trống |
| hash 4 bảng khoá | **PRE = POST y hệt** |
| dòng cron | **0** dấu `\&` lọt vào (bẫy đã sập ở V11055) |
| `_v11055_canh_chan_cheo_lane.py` | **0 dòng · 0 chặn nhầm** |

**RM-15 — thử chặn nay soi TỪNG phép đo riêng:** gỡ đăng ký `setInterval` của P4 ⇒ deny; gỡ của
B1 ⇒ deny. Cổng phân biệt được **cả hai**, không phải chỉ báo xanh chung chung.

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| **10/08 đêm** | *«Các đề xuất an toàn tiến hành ngay được thì tiến hành xử lý đi em, còn gì chưa rõ, chưa xác định thì tiếp tục đảm bảo chỉ có cải tiến nâng cao chính xác dự đoán nha em đừng đi lùi nữa»* |
| **10/08 12:52** | *«"đúng theo tài liệu" ≠ "có giá trị đo được". PHẢI ĐO TRƯỚC.»* — nguyên tắc chi phối B4 |
| **doctrine cũ** | học thuyết **anti-trap** — mã gọi thẳng là *«owner anti-trap owner-doctrine flag»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| nhánh CHỐT GẤP có **bảng bonus RIÊNG** `soft: 0.40` | `combo_super.py:1901` |
| nhánh đó **chạy 69/90 miền-ngày = 76,7%** | gọi thật `extract_rule_candidates_v2`, 30 ngày × 3 miền |
| **`get_active_rules` KHÔNG có bộ lọc thời điểm** | `rule_engine.py:262-266` — mệnh đề `WHERE` không hề nhắc `mined_at` |
| **cả 105 luật đào lúc 00:30 sáng nay** | `SELECT MIN/MAX(mined_at) FROM mined_rules` → `2026-08-10T00:30:00…11` |
| luật có `hr_4w = hr_8w = hr_12w = 1,0` | `SELECT … FROM mined_rules WHERE production_tier='READY_STRONG'` |
| bộ ráp bundle **51 lần** công bố số bị gắn cờ anti-trap | `anti_trap_shadow_v11058` · `co_canh_bao=1` |

### `DOC_SAID`

| tài liệu ghi gì | file:mục | lệch? |
|---|---|---|
| *«MINED_RULES đang cộng **+0,15**»* | `CHANGELOG.md:222` | ✗ **thiếu nhánh +0,40** — gấp **2,7 lần** |
| *«luật hơn nền +7,5/+13,8/+20,7 điểm TRONG cửa sổ chọn nhưng ĐÚNG BẰNG 0 ngoài cửa sổ»* | `CLAUDE.md §61 RM-18` (V11030) | **khớp** — và agent vẫn suýt tái phạm |
| `RR §10B`: *«Main pick KHÔNG được là tail ở FULL_SPENT»* | `gpt_analyzer.py:755` | ✗ **bộ ráp bundle không thi hành** |

### Ba lớp lệch nhau ⇒ FINDING

1. **`DOC_SAID` ≠ `CODE_DID`** — mọi tài liệu nói boost trần `+0,15`; mã có **nhánh thứ hai
   `+0,40`** chạy 3/4 số ngày. **Chưa ai ghi nhận nhánh này.**
2. **`OWNER_SAID` ≠ `CODE_DID`** — học thuyết anti-trap của owner được prompt dạy nhưng bộ ráp
   bundle bỏ qua **51 lần**.
3. **`DOC_SAID` đã cảnh báo trước mà agent vẫn suýt sập** — `RM-18` mô tả **đúng** cái bẫy
   trong-cửa-sổ-chọn, agent vẫn tạo lại nó rồi suýt báo là phát hiện mới.

---

## 7. Vướng vấp

| # | vấp | quy tắc |
|---|---|---|
| 1 | **`+11,5pp` là khớp TRONG MẪU** — cả 105 luật đào **00:30 sáng nay**, mọi ngày chấm ngược đều trong cửa sổ đào. **Đã rút lại.** | **RM-18** |
| 2 | Cổng §52 mở rộng lần đầu **chết** ở K6 vì B1 không có cột `gan_bach_thu` | — |
| 3 | Thay chuỗi nhiều dòng vào tệp CRLF khớp **0 lần** ⇒ phải dùng công cụ Edit | bẫy CRLF, lần thứ **tám** |

**Vấp 1 là loại nguy hiểm nhất trong cả hai phiên hôm nay** — vì nó là **tín hiệu DƯƠNG**. Bốn
lỗi trước đều là tín hiệu âm hoặc trung tính; một tín hiệu dương giả là thứ **mời người ta hành
động**, và đó chính là hình dạng của sáu lần «hứa rồi rữa».

---

## 8. Gỡ về

```bash
# B1 (nếu owner bác)
sqlite3 data/lottery_ai.db "DROP TABLE anti_trap_shadow_v11058;"
crontab backups/crontab.pre_v11058.txt
cp backups/main.py.pre_v11058 web/backend/main.py
cp backups/monitoring.html.pre_v11058 web/frontend/monitoring.html
systemctl restart lottery

# A1/A2/A3 (chỉ tài liệu)
git revert <sha V11058> && python web/backend/_v10925_rule_sync_check.py
```

---

## 9. Theo dõi tiếp

| mã | việc | ngưỡng hành động | mốc |
|---|---|---|---|
| **FU-360** · `CL1008` | chốt hay rollback | bất kỳ chặn NHẦM ⇒ rollback. **Hôm nay chỉ MT/MB chạy dưới cổng** — ghi đúng tầng | **sáng 11/08** |
| **FU-397** · `AT1008` | B1 đo tiến anti-trap | `n(FULL_SPENT) ≥ 90` **VÀ** `\|z_MH\| ≥ 1,96` · đang **51/90** | **~mid 12/2026** |
| **FU-397b** | nhánh CHỐT GẤP `+0,40` — thêm `mined_at <= target_date` để đo được ngoài cửa sổ | chạm đường sinh số ⇒ **PLAN** | **21/08** |
| **FU-396** · `DO1108` | B2 (P4) · B3 (dùng bảng có sẵn) | McNemar gộp miền | tích luỹ |
| **FU-395** · `HT2108` | gói 21/08 — bổ sung mục CHỐT GẤP | owner ký từng mục | **21/08** |
| FU-284 | cửa sổ đang chạy | **9,53** điểm · z ≥ 1,96 · n ≥ 150 | **20/08** — cấm đọc sớm |

**Đã dùng 1 mã FU mới (`FU-397`).**

---

TanPhatAI cần làm: ① ghi `QD-058` (owner 10/08 đêm — thi hành tầng an toàn, «đừng đi lùi») và
`FU-397 · AT1008`; ② **ghi vào sổ nhánh CHỐT GẤP `+0,40`** (`combo_super.py:1901`) — mọi tài liệu
hiện chỉ nhắc `+0,15`, thiếu mất một nhánh chạy **76,7%** số ngày; ③ ghi nhận **`+11,5pp` đã bị
RÚT LẠI** vì khớp trong mẫu (105 luật đào 10/08 00:30, `get_active_rules` không lọc thời điểm) —
**đừng để ai trích lại con số đó**; ④ ghi ngưỡng B1 đăng ký trước `n(FULL_SPENT) ≥ 90` và **cấm
đọc sớm**; ⑤ theo dõi **FU-360 sáng 11/08**, nhớ hôm nay **chỉ MT/MB chạy dưới cổng**.
