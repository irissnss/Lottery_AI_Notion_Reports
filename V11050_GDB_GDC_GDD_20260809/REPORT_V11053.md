# REPORT V11053 — GĐ-C (18:05): C25 BÁO ĐỎ GIẢ, GỐC LÀ BIẾN `day` CÒN SÓT

> Cùng thư mục với `REPORT_V11050.md` theo lệnh owner *«nối báo cáo vào REPORT_V11050, không mở
> folder mới»*. Bản đầy đủ 9 phần cho riêng V11053.

**Ngày:** 2026-08-09, 18:47 → 19:00 giờ VN · **Tầng verdict:** `RUNTIME_PROVEN`

## 1. Tóm tắt

Lượt **18:05** — lượt hợp lệ **đầu tiên** của `C25` — báo **LỆCH 12**, toàn cặp `/MT`. Đào tới
gốc: **`C25` chưa bao giờ so hôm nay với hôm qua**, vì biến `day` mà nó dùng là **biến vòng lặp
còn sót** của phép khác, giữ giá trị **2026-08-04**. Đã vá, deploy, chạy lại trên VPS: **26 phép ·
24 OK**, chỉ còn `C18`/`C19` đỏ — **có từ trước**.

## 2. Owner yêu cầu gì (nguyên văn)

> **GĐ-C tối nay: 18:05 = 25 phép (gồm C25/C23/C24).**

*(Bộ nay **26 phép** vì `C26` được thêm theo Q4c cùng ngày.)*

## 3. Đào bới / phát hiện

**Bước 1 — đọc lượt 18:05:** `26 phép · 23 OK`. Đỏ: `C18` · `C19` (biên MT 04/08, có từ trước) và
**`C25 = LỆCH 12`**.

**Bước 2 — chạy lại lúc 18:50, vẫn LỆCH 12.** Con số **không đổi** sau 45 phút. Nếu là «ngày dở»
như agent từng chẩn đoán thì nó phải giảm dần khi các miền chạy xong. **Không đổi ⇒ không phải
ngày dở.**

**Bước 3 — đọc thẳng dữ liệu, không tái lập logic.** Ba model bị bêu (`claude-opus-5-fast` ·
`gemini-3.5-flash` · `glm-5.2`, đều `/MT`): `reasoning_json` **cả 08/08 và 09/08 đều CÓ ĐỦ 3
trường** `current_week_context` · `phase_alignment_summary` · `strongest_candidate_seen`.
⇒ **Dương tính giả**, không phải đường ghi trace hỏng.

**Bước 4 — gốc.** Quét toàn `run_checks()`:

```
dòng 311   today = _now_vn().date().isoformat()      ← hôm nay, ĐÚNG, nhưng C25 KHÔNG dùng
dòng 342   for day, off_at in con_c.execute(         ← `day` sinh ra ở đây
dòng 381   for day, off_at in con_c.execute(
dòng 388   for day, bien in bien_ngay:               ← vòng CUỐI, để lại `day` = 2026-08-04
dòng 693   _hom_qua = ... dt.date.fromisoformat(day) ← C25 mượn cái tên còn sót
```

**Không có dòng nào gán `day = today`.** Nên `C25` suốt từ lúc dựng đã so **04/08 với 03/08**.
Và 04/08 **chính là** ngày `C18`/`C19` đang bêu — nên kết quả ra **đúng 12 cặp, toàn `/MT`, đứng
im**. Mọi chi tiết của triệu chứng đều khớp với nguyên nhân này.

## 4. Hướng xử lý và vì sao chọn

Không mượn tên biến nữa: `C25` **tự tính** `_hom_nay = _now_vn().date().isoformat()`. Mượn `today`
cũng được, nhưng `today` nằm trong một khối `try` ở trên — nếu khối đó không chạy thì tên có thể
không tồn tại. Tự tính là cách duy nhất không phụ thuộc khối khác.

**Giữ nguyên cái gác theo giờ** (`< 18:00` ⇒ «chưa đủ ngày»). Nó vẫn đúng về nguyên tắc — chỉ là
nó **không phải** thứ đang gây đỏ.

## 5. Đã làm gì

| việc | kết quả |
|---|---|
| vá `C25` dùng `_hom_nay` tự tính | local `C25 = OK (0)` |
| deploy VPS | backup `backups/guard.py.pre_v11053` · `py_compile` OK · md5 khớp |
| chạy lại bộ tự kiểm trên VPS | **26 phép · 24 OK** · dòng 09/08 ghi lại lúc **18:53:36** |
| ghi đè bản ghi 18:05 sai | bảng `v10900_consistency_guard` là **shadow**, không thuộc 4 bảng khoá |

**Không restart** — bộ tự kiểm chạy bằng cron như tiến trình riêng, đọc tệp từ đĩa mỗi lượt.

## 6. Cổng kiểm

```
V : cao nhất V11052 · trống tiếp V11053   ✓ dùng V11053
FU: cao nhất FU-393 · trống tiếp FU-394   (không sinh mã mới — gắn vào FU-389)
```
**Trần sinh mã: 3/5**, không tăng.

Bộ 18:05 sau vá, chạy thật trên VPS:

| phép | trạng thái |
|---|---|
| `C23_vung_ban_dung_bien` | **OK** 229/229 |
| `C24_khong_sai_nhan_moi` | **OK** 0 |
| `C25_trace_ba_truong_phase` | **OK** 0 |
| `C26_muc_treo_archive` | **OK** 97/97 |
| `C18` · `C19` | **LỆCH** — biên MT **2026-08-04** (227s · 467s), **có từ trước, không phải mới** |

## 7. Vướng vấp

**Đây là lỗi của agent, và là lỗi RM-10 — đoán tên.** Sáng nay agent sửa `C25` **ba lần** vì
«dương tính giả»: ① đếm tuyệt đối → ② so theo model → ③ so theo cặp → ④ gác theo giờ. **Cả bốn đều
chữa triệu chứng.** Nguyên nhân thật — biến `day` chưa bao giờ là hôm nay — chỉ lộ ra khi lượt
18:05 thật chạy và con số **không đổi** giữa hai lần đo cách nhau 45 phút.

Bài học cụ thể hơn «đừng đoán tên»: khi viết thêm vào một hàm dài, **tên biến có sẵn trong tầm
nhìn không có nghĩa là nó mang giá trị mình tưởng**. Phải truy nơi nó được gán, không chỉ nơi nó
đọc được.

Và một điều nữa: nếu lượt 18:05 **không** báo đỏ, lỗi này sẽ **im lặng mãi mãi** — `C25` sẽ mãi so
hai ngày cũ và mãi báo xanh sau khi 04/08 trôi khỏi tầm. Cổng báo đỏ nhầm còn cứu được; cổng báo
xanh nhầm thì không.

## 8. Gỡ về

```bash
ssh root@14.225.224.89 'cd /root/Lottery_AI_Test && \
  cp backups/guard.py.pre_v11053 web/backend/_v10900_consistency_guard.py'
git revert <commit V11053>
```
Không restart nên không có PID để khôi phục.

## 9. Theo dõi tiếp

| việc | khi nào |
|---|---|
| `C18`/`C19` — biên MT 04/08 quá hẹp (227s · 467s) | còn đỏ, **chưa xử** — cần owner quyết trong gói 21/08 |
| lượt **18:05 ngày 10/08** | phép đo C25 sạch đầu tiên **sau khi vá** |
| `19:35` lane `la_do_lui=0` · bầy đàn 08+09/08 · trace `64=0` | phần còn lại của GĐ-C |

*Đẩy cùng commit (A55 · §57.2).*
