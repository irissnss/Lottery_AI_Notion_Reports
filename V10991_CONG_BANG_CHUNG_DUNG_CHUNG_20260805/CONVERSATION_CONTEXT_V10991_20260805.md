# CONVERSATION CONTEXT — V10991 — 2026-08-05

> Nguyên văn lời owner · agent làm gì · vấp ở đâu. Không diễn giải lại.

---

## 1. Owner nói gì (nguyên văn, theo thứ tự)

### Lượt trước — giao toàn bộ dự án

> *"Em là agent siêu việt cả coder, fixder, writer và auditor luôn ah. Giờ anh giao hết nhiệm vụ
> dự án cho em, em kiểm soát, xử lý nâng cao dự đoán cho anh theo các quy tắc hướng dẫn đã có còn
> lại vướng mắc chờ anh xác nhận thì nêu lên ngay cho anh"*

### Lượt này — chốt ba vướng mắc

> *"Hết chú kỳ live hôm nay rồi em, tiến hành xử lý dùm anh, vướng mắc 1: anh đồng ý khuyến nghị
> của em, vướng mắc 2: mở nha em, Vướng mắc 3: em writer nha em em tiến hành đi"*

Ba vướng mắc em đã trình trước đó:

| # | Em trình gì | Owner chốt |
|---|---|---|
| 1 | Bốn chỗ chọn số trên `/du-doan-test` mỗi chỗ một ngưỡng (`n≥4` · `total_runs≥10` · `min_n=6` · `min_n=10`), không chỗ nào hiệu chỉnh so sánh bội. Đề xuất **phương án A**: một quy tắc chung + Bonferroni, `N_min = 12` | **"anh đồng ý khuyến nghị của em"** |
| 2 | Đóng băng còn giữ hay mở? | **"mở nha em"** |
| 3 | Sáng 05/08 phiên soi lưu trữ phải dừng vì có tiến trình khác ghi cùng lúc (`BLOCKED_CONCURRENT_WRITER`). Ai là người ghi? | **"em writer nha em em tiến hành đi"** |

→ Ghi thành **QD-028** · **QD-029** · **QD-030** trong `docs/OWNER_DECISION_LEDGER.json`, nguyên
văn, ngay trong phiên.

---

## 2. Agent làm gì, theo đúng thứ tự

1. Chạy `_v10920_session_start.py` (bắt buộc §0). 29 quyết định đang hiệu lực, 0 tới hạn rà soát,
   cảnh báo 15 mục FU mồ côi.
2. Kiểm khung deploy: VPS 20:53, cả ba miền đã có `bundle_version=2`, đã settle, **0 dự đoán ghi
   sau FINAL** → cửa deploy an toàn theo FU-207.
3. Sao lưu `main.py` → `backups/v10991_pre/main.py.pre` (md5 `ba973cce`).
4. Dựng `_v10991_sample_gate.py`, thử độc lập — 4/4 giá trị nhị thức khớp tay.
5. Nối vào bốn cổng trong `main.py`, thêm 7 trường nhãn vào payload.
6. **Thử tại chỗ:** bóc `_build_per_number_method_output()` khỏi **cả hai bản** (`.pre` và bản
   sửa), chạy trên DB thật, so từng trường, 3 miền × 3 ngày.
7. Phát hiện và sửa **hai lỗi nặng hơn** (bảng dựng sẵn cũ 8 ngày · sai đơn vị đếm).
8. Sửa giao diện in nhãn thật.
9. Ghép tài liệu + ghi ba quyết định vào sổ.
10. Deploy → **TRƯỢT** → sửa → deploy lại → **TRƯỢT** → sửa cổng → **✓ MỌI CỔNG ĐẠT**.

---

## 3. Vấp ở đâu — kể hết, kể cả lỗi của chính em

### 3.1 Bản nối cổng đầu tiên làm MẤT SỐ

Chặn thẳng khi không đạt → MB **mất hẳn số phụ 1**. Trái §54 owner đã ký («luôn ra số, chỉ nói
thật về độ tin cậy»). Tự bắt được lúc so trước/sau. Sửa thành **xếp thứ tự ưu tiên, không loại
ai**: đủ bằng chứng trước, không ai đủ thì vẫn ra số từ bản nền mẫu rộng nhất.

### 3.2 `_wd_best()` bản đầu chặn mất nhánh dự phòng

Bản đầu luôn trả kết quả → chặn `or _best(...)`, làm **mẫu nhỏ theo thứ đè lên cửa sổ rộng hơn**
— đúng cái bệnh đang đi chữa. Sửa: chỉ trả khi đạt, không thì trả `None` để rơi xuống.

### 3.3 Hai lỗi nặng hơn cái owner hỏi

Đang nối cổng thì thấy con số `MT_ADAPTIVE_EXPLOIT_V1` **59% n=87** đẹp bất thường. Soi ra:

- dòng đó trong `du_doan_test_experiment_scoreboard` mang `last_updated = 2026-07-28`, **cũ 8
  ngày**, trong khi **6 lượt gần nhất của chính nó thua sạch**;
- `COUNT(*)` đếm **theo đài** (MT 2,86 dòng/ngày), các dòng cùng ngày dùng chung một bộ số nên
  **không độc lập** → `p` nhỏ giả tạo.

Cả hai đều làm cổng **LỎNG hơn**. Nếu không sửa thì cái nhãn ✔ mới sẽ **dán lên số liệu tuần
trước** — tệ hơn cả trước khi sửa, vì nay nó mang dấu kiểm. Đã sửa cùng phiên: bỏ bảng dựng sẵn,
tính thẳng từ bảng gốc, đếm theo NGÀY.

### 3.4 Deploy lần 1 TRƯỢT — MT mất ô bạch thủ

Cổng chấm trên toàn bộ ứng viên rồi mới hỏi hôm nay có số không.
`MT_OFFICIAL_BASELINE_CONTROL` **không chạy ngày 05/08** → chọn xong không có gì để bày.

**DB local đồng bộ lúc 10:10, TRƯỚC khi MT/MB chạy** — nên phép thử local **không thể** thấy.
Chỉ cổng sống chạy trên DB VPS mới bắt được.

Sửa: `_ung_vien()` lọc trước, chỉ so những phương pháp **hôm nay có số**. Lọc theo điều kiện NGÀY
chứ không theo kết quả nên không làm lệch phép thử.

### 3.5 Deploy lần 2 — `database is locked`

Restart lần hai cách lần đầu 3 phút, vấp đúng lúc tiến trình cũ còn ghi → `seed_defaults()` chết,
systemd tự dựng lại (`NRestarts=1`, PID 873576 → 873793). **Không phải lỗi code.** Nhưng phép đo
`sleep 8` rồi curl đã kịp chấm `000` và báo TRƯỢT nhầm.

Sửa: vòng chờ tới khi `health=200`, tối đa 2 phút.

### 3.6 Cổng tự kiểm của chính em báo động giả BA LẦN

| Lần | Cách đếm | Vì sao dính |
|---|---|---|
| 1 | đếm thô tên bảng trong thân hàm | bắt trúng **2 dòng chú thích đang giải thích vì sao bảng đó bị bỏ** |
| 2 | bỏ dòng bắt đầu bằng `#` | tên bảng nằm trong **docstring** |
| 3 | «chuỗi có tên bảng **và** có từ khoá SQL» | docstring viết «`COUNT(*)` **trên join** đếm THEO ĐÀI» → viết hoa thành `TRÊN JOIN ĐẾM` |
| **4 — dứt** | tên bảng phải đứng **NGAY SAU** từ khoá | văn xuôi tiếng Việt không giả được dạng đó |

Đây đúng cái bẫy V10990 đã ghi vào tài liệu («chú thích vs chỗ render») mà em vẫn sập lại.

### 3.7 Hai lỗi hiển thị nhỏ

- `round(p, 4)` biến `p = 3,89e-05` thành `0.0` — trông như bịa và đọc thành «chắc chắn tuyệt
  đối».
- `window = null` ghép thẳng vào chuỗi in ra `"/nulld"`.

### 3.8 Bẫy môi trường đã ghi sẵn trong CLAUDE.md mà vẫn suýt sập

`python -c` in tiếng Việt lỗi mã hoá console (`UnicodeEncodeError: charmap`). Tài liệu đã ghi
«viết ra file script có `sys.stdout.reconfigure(encoding="utf-8")`». Em gõ `python -c` theo phản
xạ và dính ngay.

---

## 4. Điều đáng nói nhất

Sau khi chữa cỡ mẫu, so sánh bội và đơn vị đếm: **9/9 ô (3 miền × 3 ngày) không phương pháp nào
qua cổng.** Trùng khớp với bản đo accuracy 05/08 (không miền nào có lợi thế thống kê, mọi
`|z| < 2`).

Những con số **62% · 61% · 60%** mà trang từng bày ra **không phải là năng lực bị che lấp — chúng
là nhiễu được chọn ra.**

Cổng này không làm hệ dự đoán kém đi. Nó chỉ thôi hứa hẹn thứ chưa có. Số vẫn ra đủ, mỗi ngày,
cả ba miền — chỉ là nay trang nói thật rằng chưa đủ bằng chứng.

---

## 5. Còn treo, cần owner biết

**Mở đóng băng (QD-029) không có nghĩa được gộp B1+B2+B3 vào một lượt deploy.** QD-018 vẫn ràng:
một biến một lần, đo 7–14 ngày. V10991 là **biến thứ nhất**, phải đo tiến tới **19/08** (FU-276)
trước khi thả biến sau.

Ba mục đang chờ: `FU-216` (B1, hạn 09/08) · `FU-231` (B2, hạn 10/08) · `FU-226` (B3, hạn 10/08).

Em **không tự quyết** chuyện có nới QD-018 hay không — đây là chỗ cần owner nói.
