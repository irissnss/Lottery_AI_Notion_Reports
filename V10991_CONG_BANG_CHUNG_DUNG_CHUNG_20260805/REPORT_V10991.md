# REPORT V10991 — Một cổng bằng chứng dùng chung cho `/du-doan-test`

> **Ngày:** 2026-08-05 · **Miền ảnh hưởng:** MN · MT · MB (chỉ trang lane test)
> **Quyết định owner:** QD-028 · QD-029 · QD-030 (ký ~20:5x giờ VN)
> **Mã việc:** FU-274 · QD0808-1 (đóng) · FU-271 · DO0808 (đóng) · FU-275 · DO1208 · FU-276 · DO1908

---

## 1. Tóm tắt

Trang `/du-doan-test` in ra những câu như **«62% BT hit/T3, n=8»** để nói số hiển thị đến từ
phương pháp nào và đã kiểm chứng bao nhiêu. Bốn chỗ chọn phương pháp trong `main.py` đều dùng
lối **lấy cực đại trên nhiều ứng viên mà không hiệu chỉnh**, mỗi chỗ một ngưỡng riêng
(`n>=4` · `total_runs>=10` · `min_n=6` · `min_n=10`).

Lấy max trên `m` ứng viên thì kỳ vọng của cực đại **luôn cao hơn** năng lực thật. Với `n=4` và
tỉ lệ nền ~30%, xác suất có **ít nhất một** trong 20 phương pháp đạt 4/4 do may rủi là **~15%**.
Con số 62% kia gần như chắc chắn là **may rủi được chọn ra**.

V10991 gộp cả bốn về **một cổng chung**: dán nhãn «đủ bằng chứng» chỉ khi **n≥12** *và* đuôi nhị
thức `P(X≥k | n, p_nền) ≤ 0,10 / m` (Bonferroni). Không đạt thì **vẫn ra số** — luôn luôn — chỉ
hạ nhãn và dùng lựa chọn **đăng ký trước** thay vì lấy con cao nhất.

Trong lúc nối cổng, phát hiện **hai lỗi nặng hơn** cái ban đầu, và lúc deploy lộ thêm **ba lỗi
nữa** mà máy local không thể thấy. Tất cả đã xử trong cùng phiên.

**Kết quả đáng chú ý nhất:** sau khi chữa cỡ mẫu, so sánh bội và đơn vị đếm thì **9/9 ô
(3 miền × 3 ngày) không phương pháp nào qua cổng**. Trên trang lane test hiện **chưa có phương
pháp nào có bằng chứng thắng được mặt bằng của chính nhóm nó**.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *"Em là agent siêu việt cả coder, fixder, writer và auditor luôn ah. Giờ anh giao hết nhiệm vụ
> dự án cho em, em kiểm soát, xử lý nâng cao dự đoán cho anh theo các quy tắc hướng dẫn đã có còn
> lại vướng mắc chờ anh xác nhận thì nêu lên ngay cho anh"*

> *"Hết chú kỳ live hôm nay rồi em, tiến hành xử lý dùm anh, vướng mắc 1: anh đồng ý khuyến nghị
> của em, vướng mắc 2: mở nha em, Vướng mắc 3: em writer nha em em tiến hành đi"*

Ba vướng mắc em đã trình trước đó, owner trả lời gọn:

| # | Nội dung trình | Owner chốt |
|---|---|---|
| 1 | Bốn chỗ chọn số mỗi chỗ một ngưỡng, đề xuất **phương án A**: một quy tắc chung + hiệu chỉnh so sánh bội, `N_min = 12` | **Đồng ý** → QD-028 |
| 2 | Đóng băng còn giữ hay mở | **Mở** → QD-029 |
| 3 | Ai là người ghi (sáng 05/08 phải dừng vì có tiến trình khác ghi cùng lúc) | **Em là writer** → QD-030 |

---

## 3. Đào bới / phát hiện

### 3.1 Lỗi ban đầu — bốn ngưỡng rời rạc, không cái nào hiệu chỉnh

| Chỗ | Ngưỡng cũ |
|---|---|
| `_wd_best()` bạch thủ theo thứ | `HAVING n>=4 ORDER BY wins/n DESC LIMIT 1` |
| `_best()` bạch thủ dự phòng | `total_runs>=10 ... LIMIT 1` |
| `_pos_hit()` số phụ vòng a | `min_n=6`, cửa sổ 90 ngày cùng thứ |
| `_pos_hit()` số phụ vòng b | `min_n=10`, cửa sổ 60 ngày mọi thứ |

Trong khi **cổng khuyến cáo trên CÙNG MỘT TRANG** đã nâng lên `n≥40` từ V10990. Chỗ chọn SỐ vẫn
`n≥4` — **lỏng gấp mười lần**.

### 3.2 Lỗi nặng hơn #1 — chấm bằng chứng trên bảng dựng sẵn ĐÃ CŨ

`_best()` đọc `du_doan_test_experiment_scoreboard`. Ngày 05/08 dòng
`MT_ADAPTIVE_EXPLOIT_V1 / window 30` vẫn mang `last_updated = 2026-07-28` — **cũ 8 ngày** — ghi
**59% (51/87)**. Trong khi **6 lượt gần nhất của chính phương pháp ấy thua sạch**:

```
2026-08-04  win=0     2026-08-01  win=0
2026-08-03  win=0     2026-07-31  win=0
2026-08-02  win=0     2026-07-30  win=0
```

Nếu không phát hiện, cái nhãn ✔ mới sẽ **chứng nhận số liệu tuần trước** — tệ hơn cả trước khi
sửa, vì nay nó mang dấu kiểm.

### 3.3 Lỗi nặng hơn #2 — sai đơn vị đếm

`COUNT(*)` trên phép nối đếm **theo đài**, không theo ngày. Đo ngày 05/08:

| Miền | Số dòng mỗi ngày cho cùng một phương pháp |
|---|---|
| MT | **2,86** |
| MN | **2,00** |
| MB | **1,05** |

Các dòng cùng ngày **dùng chung một bộ số** nên không độc lập. Nhét vào phép nhị thức thì `n`
phồng 2–3 lần và `p` nhỏ giả tạo — tức là **dễ dán ✔ hơn thực tế**. Cả hai lỗi này đều làm cổng
**LỎNG hơn**, không phải chặt hơn.

### 3.4 Ba lỗi chỉ lộ ra lúc deploy

1. **MT mất hẳn ô bạch thủ.** Cổng chấm trên toàn bộ ứng viên rồi mới hỏi hôm nay có số không.
   `MT_OFFICIAL_BASELINE_CONTROL` **không chạy ngày 05/08** → chọn xong không có gì để bày.
   DB local đồng bộ lúc 10:10, **trước khi** MT/MB chạy, nên phép thử local không thể thấy.
2. **`database is locked`** lúc `seed_defaults()` → tiến trình chết, systemd tự dựng lại. Không
   phải lỗi code: hai lần restart cách nhau 3 phút. Nhưng phép đo `sleep 8` rồi curl đã kịp
   chấm `000`.
3. **Cổng tự kiểm của chính em báo động giả ba lần liên tiếp** (mục 7).

---

## 4. Hướng xử lý và vì sao chọn

**Chọn:** một module thuần tính toán dùng chung cho cả bốn chỗ.

| Vì sao | |
|---|---|
| **Một quy tắc, không bốn** | Bốn ngưỡng rời rạc là nguồn gốc chuyện «chỗ này n≥40, chỗ kia n≥4» ngay trên cùng một trang |
| **Hiệu chỉnh theo `m` THẬT** | `m` là số ứng viên thật sự đem so trong chính lần chọn đó, không phải hằng số. Ngày ít phương pháp chạy thì ngưỡng nới ra một cách chính đáng |
| **`p_nền` lấy từ chính nhóm** | Mặt bằng cùng kỳ, cùng miền — không mượn con số ở đâu khác |
| **Không đạt thì VẪN RA SỐ** | Quy tắc §54 owner đã ký: luôn ra số, chỉ nói thật về độ tin cậy. Giấu số là tự ý thu hẹp sản phẩm |
| **Không ai đạt thì dùng bản ĐĂNG KÝ TRƯỚC** | Lúc đó lấy max chính là lấy nhiễu. Bản đăng ký trước (`OFFICIAL_BASELINE_CONTROL`) là đối chứng, chọn từ trước khi nhìn kết quả |
| **Tính thẳng từ bảng gốc** | Bỏ bảng dựng sẵn thì hết chuyện số liệu cũ, và cùng lúc sửa được đơn vị đếm |

**Đã cân nhắc và bỏ:** giữ bảng dựng sẵn rồi thêm phép canh «bảng cũ quá thì không dán ✔». Bỏ vì
nó chữa triệu chứng: bảng vẫn cũ, chỉ là ta thôi tin nó. Tính thẳng từ bảng gốc thì **không bao
giờ cũ** và đồng thời chữa luôn đơn vị đếm.

---

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `web/backend/_v10991_sample_gate.py` | **MỚI**, 7.327 byte. `duoi_nhi_thuc()` (lgamma, không tràn số) · `danh_gia()` · `ti_le_nen()` · `chon()` · `mo_ta()` · `_lam_tron()`. Thuần tính toán: không đọc DB, không ghi gì, không phụ thuộc module dự án |
| `web/backend/main.py` | 941.751 → **949.940 byte**. Thêm `_ung_vien()` — nguồn ứng viên **duy nhất**, tính từ bảng gốc **theo NGÀY**, lọc trước những phương pháp hôm nay có số. `_wd_best()`/`_best()`/hai vòng số phụ cùng gọi cổng chung. `_best("bt_wins")` → `_best("test_bt_status")`. `_pos_hit()` gộp một dòng/ngày (`MAX(id)`) + neo cửa sổ vào ngày yêu cầu thay vì `date('now')`. Payload thêm 7 trường nhãn |
| `web/frontend/du-doan-test.html` | 218.579 → **220.726 byte**. In nhãn ✔/⚠ kèm dòng giải thích vì sao chưa đủ; tiêu đề bỏ chữ «đã verify» (đang hứa quá) và ghi thẳng công thức cổng; `window=null` → «toàn kỳ» thay vì in ra `/nulld` |
| `web/backend/_v10991_kiem_song.py` | **MỚI**. Cổng sống 6 mệnh đề, chạy THẬT hàm trên DB VPS |
| `web/backend/_v10991_deploy.py` | **MỚI**. Chuỗi deploy đủ cổng, chờ tới khi `health=200` |
| `web/backend/_v10991_docs.py` | **MỚI**. Ghép tài liệu + ghi QD-028/029/030 |

### Quy tắc, viết gọn

Dán nhãn **«đủ bằng chứng»** chỉ khi **cả hai**:

1. `n ≥ 12` — cỡ mẫu, đơn vị **NGÀY**
2. `P(X ≥ k | n, p_nền) ≤ 0,10 / m` — đuôi nhị thức, đã chia cho số ứng viên

Không đạt ⇒ **vẫn ra số**, hạ nhãn, dùng bản đăng ký trước.

**KHÔNG đụng:** `/du-doan` official · writer của `final_bundles` · bộ chọn model production ·
Combo Super · prompt · scheduler · cron.

---

## 6. Cổng kiểm

### 6.1 Module khớp tay

| Phép | Máy tính | Tay tính |
|---|---|---|
| `P(4/4 | n=4, p=0,3)` | 0,0081 | 0,3⁴ = 0,0081 ✓ |
| `P(1/1 | n=1, p=0,5)` | 0,5 | 0,5 ✓ |
| `P(X≥0 | n=10)` | 1,0 | 1,0 ✓ |
| `P(10/10 | n=10, p=0,3)` | 5,9049e-06 | 0,3¹⁰ ✓ |

### 6.2 Nghiệm thu trước/sau — bóc hàm khỏi tệp thật, đổ dữ liệu thật

Chạy `_build_per_number_method_output()` bóc từ **cả hai bản** (bản `.pre` đã sao lưu và bản
sửa), 3 miền × 3 ngày 03–05/08:

| | Trước | Sau |
|---|---|---|
| MB bạch thủ | `SCREEN_WEIGHTED_V1` **62% n=8** → số `45` | `OFFICIAL_BASELINE_CONTROL` 15% n=122 → số `71` ⚠ |
| MN bạch thủ 03/08 | `SPECIALIST_ROSTER_V1` **61% n=31** → số `43` | `OFFICIAL_BASELINE_CONTROL` 40% n=124 → số `64` ⚠ |
| MB số phụ 1 03/08 | `STRENGTH_WEIGHTED` **60% n=10** → số `13` | `FULL_POOL_D_W06_V1` 26% n=62 → số `79` ⚠ |
| MB số phụ 1 05/08 | `FULL_POOL_D_W06_V1` 44% **n=9** | **cùng phương pháp, cùng số `45`**, 26% **n=61** |
| MN/MT 03–04/08 | **ô trống** | có số, kèm nhãn ⚠ |

**Không ô nào mất số** — bản mới là tập cha của bản cũ. Bằng chứng thô:
`evidence/so_truoc_sau_0308.txt` · `evidence/so_truoc_sau_0408.txt`.

### 6.3 Cổng trên hệ thật — `✓ MỌI CỔNG ĐẠT`

| | |
|---|---|
| PID | 846146 → 873576 → **873793** |
| smoke | `/api/health=200` · `/api/du-doan-test/MN=401` · traceback 3 phút = **0** |
| byte trên VPS | khớp local **từng byte** cả ba tệp |
| **4 bảng khoá** | `predictions` 11.794 · `final_bundles` 477 · `lottery_results` 15.219 · `model_daily_eval` 11.658 — **GIỮ NGUYÊN hash cả bốn** |
| tự kiểm | 22 phép · ĐẠT 19 · LỆCH 3 |
| cổng sống | `MIN_N=12` · bảng dựng sẵn **0** chỗ · đếm theo ngày ✓ · gộp `MAX(id)` ✓ |
| official | MN `model_count=15` ✓ |

**3 phép LỆCH là `C18_bien_lane_du_rong` · `C19_bien_han_du_rong` · `C20_bien_han_khong_troi`** —
đều đo **biên giờ trên cửa sổ 7 ngày quá khứ** (địa hạt FU-256). Có sẵn trước khi deploy và
không thể do một thay đổi code vừa đẩy vài phút trước gây ra.

### 6.4 Trang hiện ra gì (đo trực tiếp trên DB VPS, 05/08)

| Miền | Bạch thủ | Số phụ 1 |
|---|---|---|
| MN | `25` · 40% n=124 · ⚠ | `10` · 30% n=61 · ⚠ |
| MT | `93` · 28% n=122 · ⚠ | `67` · 23% n=60 · ⚠ |
| MB | `82` · 15% n=123 · ⚠ | `82` · 25% n=61 · ⚠ |

**Cả 6 ô đều ⚠, không ô nào rỗng.** `so_phu_2` không có số ở cả ba miền — **giống hệt bản cũ**,
không phải hụt do V10991.

---

## 7. Vướng vấp

### 7.1 Lỗi của em, tự bắt trong lúc nghiệm thu

- Bản nối cổng đầu tiên **chặn thẳng khi không đạt** → MB **mất hẳn số phụ 1**. Trái §54. Sửa
  thành xếp thứ tự ưu tiên, không loại ai.
- `_wd_best()` bản đầu **luôn trả kết quả** → chặn mất nhánh `or _best(...)`, làm mẫu nhỏ theo
  thứ đè lên cửa sổ rộng hơn. Sửa: chỉ trả khi đạt.
- `round(p, 4)` biến `p = 3,89e-05` thành `0.0` — trông như bịa và đọc thành «chắc chắn tuyệt
  đối». Thêm `_lam_tron()` giữ 3 chữ số có nghĩa.
- `window = null` ghép thẳng vào chuỗi giao diện in ra `"/nulld"`.

### 7.2 Cổng tự kiểm của chính em báo động giả BA LẦN liên tiếp

Đúng cái bẫy V10990 đã ghi («chú thích vs chỗ render»), mà em vẫn sập lại:

| Lần | Cách đếm | Vì sao dính |
|---|---|---|
| 1 | đếm thô tên bảng trong thân hàm | bắt trúng **2 dòng chú thích đang giải thích vì sao bảng đó bị bỏ** |
| 2 | bỏ dòng bắt đầu bằng `#` | lần này tên bảng nằm trong **docstring** — docstring không phải chú thích `#` |
| 3 | «chuỗi có tên bảng **và** có từ khoá SQL» | docstring viết «`COUNT(*)` **trên join** đếm THEO ĐÀI» → `.upper()` thành `TRÊN JOIN ĐẾM` |
| **4 — dứt** | tên bảng phải đứng **NGAY SAU** từ khoá (`FROM\|JOIN\|UPDATE\|INSERT INTO` + tên bảng) | văn xuôi tiếng Việt không giả được dạng đó |

**Bài học:** cổng dò theo chuỗi thô thì **văn bản mô tả chính nó** sẽ làm nó báo động giả. Phải
dò theo **cấu trúc** (cú pháp SQL), không theo sự có mặt của từ.

### 7.3 Lỗi chỉ lộ khi chạm hệ thật

DB local đồng bộ **10:10**, trước khi MT/MB chạy. Nên phép thử local **không thể** thấy chuyện
«phương pháp được chọn hôm nay không có số». Chỉ cổng sống chạy trên DB VPS mới bắt được.

**Bài học:** thử tại chỗ trên bản local là cần nhưng **chưa đủ**. Phải có cổng chạy THẬT trên hệ
thật, ngay trong lượt deploy, và cổng đó phải biết so với bản `.pre`.

### 7.4 Deploy hai lần cách nhau 3 phút

Lần sau vấp `database is locked` đúng lúc tiến trình cũ còn đang ghi. Không hỏng gì (systemd tự
dựng lại, `NRestarts=1`) nhưng làm phép đo báo TRƯỢT nhầm. Đã sửa thành vòng chờ tới khi
`health=200`.

---

## 8. Gỡ về

```
1) copy backups\v10991_pre\main.py.pre → web\backend\main.py
   (941.751 byte · md5 ba973cce3972557d5dc7a991d81ae891)
2) copy backups\v10991_pre\du-doan-test.html.pre → web\frontend\du-doan-test.html
   (218.579 byte · md5 15169916b8745acdc98936f45285e01b)
3) xoá web\backend\_v10991_sample_gate.py
4) scp cả ba lên VPS rồi `systemctl restart lottery`  (KHÔNG phải `lottery-ai`), so PID trước/sau
```

Bản trên VPS trước deploy giữ tại `<VPS_ROOT>/backups/v10991_pre_vps/`.

Gỡ về **không cần đụng DB** — V10991 không ghi bảng nào.

---

## 9. Theo dõi tiếp

| Mã | Nhãn | Hạn | Nội dung |
|---|---|---|---|
| **FU-275 · DO1208** | Bảng xếp hạng dựng sẵn có bị bỏ đói không | 12/08 | `du_doan_test_experiment_scoreboard` có dòng cũ **8 ngày**. V10991 đã thôi đọc nó, nhưng bảng vẫn còn và **chỗ khác có thể đang đọc**. Phải soi **AI ĐỌC BẢNG** (không phải ai `import`), tìm job lẽ ra phải làm mới nó, rồi quyết định làm mới hay khai tử. **Ngưỡng:** có ≥1 chỗ khác đọc ⇒ phải xử trong cùng phiên |
| **FU-276 · DO1908** | Đo tiến 14 ngày cổng bằng chứng | 19/08 | QD-018: một biến một lần, đo 7–14 ngày. Mỗi ngày ghi: số ô ✔, số ô ⚠, phương pháp được chọn, kết quả settle. **Ngưỡng:** sau 14 ngày nếu lối cũ trúng cao hơn có ý nghĩa (p≤0,05) ⇒ trình owner xem lại; bằng nhau ⇒ giữ V10991 vì trung thực hơn. **Không được bật/tắt bằng backtest** — V10655→V10672→V10677→V10753→V10789→V10790 đều rữa |

### Việc cần owner biết, chưa cần quyết

**Mở đóng băng (QD-029) không có nghĩa được gộp B1+B2+B3 vào một lượt.** QD-018 vẫn ràng:
V10991 là **biến thứ nhất**, phải đo tiến tới 19/08 trước khi thả biến sau. Ba mục đang chờ:
`FU-216` (B1, hạn 09/08) · `FU-231` (B2, hạn 10/08) · `FU-226` (B3, hạn 10/08).

### Điều đáng suy nghĩ nhất từ phiên này

Sau khi chữa cỡ mẫu, so sánh bội và đơn vị đếm, **9/9 ô không phương pháp nào qua cổng**. Trùng
khớp với bản đo accuracy ngày 05/08 (không miền nào có lợi thế thống kê, mọi `|z| < 2`).

Nghĩa là: **những con số 62% · 61% · 60% mà trang từng bày ra không phải là năng lực bị che lấp —
chúng là nhiễu được chọn ra.** Cổng này không làm hệ dự đoán kém đi; nó chỉ thôi hứa hẹn thứ chưa
có. Muốn có lợi thế thật thì phải tìm ở chỗ khác, và FU-276 là chỗ để biết mình đã tìm được chưa.
