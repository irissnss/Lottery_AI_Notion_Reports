# NGỮ CẢNH PHIÊN V10987 — 2026-08-05 (giờ Việt Nam)

> Ghi lại **nguyên văn** yêu cầu, agent làm gì theo trình tự, và **vấp ở đâu** — kể cả vấp do
> chính agent gây ra. Theo §57.2 (A55.2).

---

## 1. Bối cảnh — phiên này nhận việc từ ĐÂU

Phiên V10987 **không nhận việc trực tiếp từ owner**. Nó là phiên con, nhận việc từ **agent cha**
sau khi agent cha đo được trong phiên **V10986** (~00:20 ngày 05/08) rằng `FU-262` đến hạn hôm nay
mà đang mồ côi.

Quyết định owner đứng phía sau (đã có trong sổ, §56 cấm hỏi lại):

- **`QD-021`** — owner ký **04/08/2026 10:29**, nguyên văn:
  > *"Giãn ra cuốn chiếu tới hết ngày 10/08 phải hoàn thành, làm lần lượt những vấn đề nào xác thực
  > rõ ràng , đơn giản làm trước tới cuối cùng 10/08 phải xong"*
- **`QD-014`** — đóng băng đường ra số công bố tới **hết 08/08**.
- **§56 (A54)** — owner ký **01/08/2026 10:41**, nguyên văn:
  > *"Anh không muốn nhắc tới nhắc lui hoài những vấn đề mà em có thể tra ra, có thể kiểm soát được
  > đâu? ... em phải tư duy để có mối liên hệ chặt chẽ giữa báo cáo, giữa tài liệu, giữa code để
  > kiểm soát chứ em."*

  → Chính tinh thần của phiên này: mục đến hạn mà máy **không tự nêu ra** thì owner phải nhắc lại,
  và đó là điều owner nói thẳng là không muốn.

---

## 2. Yêu cầu — nguyên văn từ agent cha

> *"Ban la agent van hanh Lottery_AI_Test. Viec nho nhung gap: **cuu `FU-262` khoi tinh trang mo
> coi TRUOC briefing sang 05/08**, va **mo rong pham vi phep `K8`**."*

> *"**`FU-262` den han 05/08 (HOM NAY) nhung dang MO COI** → briefing dau phien **khong hien** no →
> nguy co troi mat dung cai kieu owner ghet nhat."*

> *"Nguyen nhan: phep **`K8`** trong `web/backend/_v10981_kiem_lich.py` **chi canh 14 muc** cua nhom
> lich cuon chieu, **khong canh toan so** → muc ngoai nhom bi mo coi thi K8 van xanh. Day la cai
> thu 8 trong "chuoi xanh gia" ngay 04/08, con ho."*

> *"Tong mo coi hien tai: **18**."*

> *"Doc `docs/FOLLOW_UP_TRACKER.md`, tim muc `FU-262`, xem no thieu gi ma bi mo coi (thieu `ma_doc`
> §58? thieu o han? nhan khong nam trong `TREO_STATUSES`?)"*

> *"**Tra danh sach nhan hop le TRUOC khi ghi** — dung tao nhan la (V10981 tung gan `SCHEDULED` lam
> 11/14 muc thanh mo coi)"*

> *"Bo sung du: **ma may + ma doc §58 (hai chu loai viec + DDMM) + nhan tieng Viet ngan + han 05/08
> + dieu kien hoan thanh do duoc bang so**"*

> *"**Thu nguoc de chung minh cong co tac dung**: co tinh tao mot muc mo coi tam (hoac dung chinh
> trang thai truoc khi sua) → K8 phai **TRUOT** va **in dung ten ma** bi mo coi → roi tra lai trang
> thai dung. Ghi ket qua thu nguoc vao evidence. **Day la buoc bat buoc** — 4/9 loi xanh gia trong
> ngay 04/08 chi lo ra nho thu nguoc."*

> *"Muc nao **den han trong 3 ngay toi (05-07/08)** thi **bo sung du truong ngay trong phien nay**
> de khong troi. Muc nao han xa hon thi gom vao `FU-258`"*

> *"Cong kiem — chay TACH RIENG tung lenh (gop lai tung bi cat mat ket qua)"*

> *"`python web/backend/_v10921_report_gate.py` → **ban quet toan bo phai exit 0** (hom qua no truot
> 13,5 tieng ma khong ai thay vi moi phien chi chay cho phien ban cua minh — **lan nay bat buoc chay
> ban toan bo**)"*

> *"**Truoc khi push**: don `desktop.ini` do Google Drive de vao `.git` neu con
> (`find .git -name desktop.ini -delete`) roi `git fetch` — day la `FU-266`, no tung lam `git fetch`
> chet khien cong bao cao bao xanh du chua push"*

> *"**Xac minh push THAT**: `git ls-tree -r origin/main --name-only | grep V10987` phai thay du hai
> file, khong chi dua vao `git status`"*

> *"**QD-014 con hieu luc den het 08/08**: khong doi 15 model official, combo-super filter, override
> toggles, `/du-doan` writer, `final_bundles` writer, bo chon model production"*

> *"**KHONG deploy, KHONG restart `lottery`** — day la phien cong cu chay o may local + tai lieu"*

> *"Notion **chi doc**. Gio VN"*

---

## 3. Agent làm gì — theo trình tự

| # | Việc | Kết quả |
|---|---|---|
| 1 | Chạy `_v10920_session_start.py` lấy **mốc nền** | mồ côi **18** · đến hạn hôm nay **4** · treo **99** · quá hạn 1 (`FU-225`) |
| 2 | Đọc `_v10981_kiem_lich.py`, `_v10958_fu_reader.py`, `_v10982_kiem_lich9.py`, `_v10981_lich.py`, `_v10982_lich9.py` | xác nhận `K8` chỉ soi `xep` = 14 mã nhóm lịch; `FU-262` không thuộc nhóm 14 |
| 3 | Tìm `FU-262` trong sổ (dòng 1552) | **có đủ** `ma_doc SC0805`, `hạn 05/08`, `due 2026-08-05` → **hai giả thuyết đầu của lệnh SAI**, chỉ nhãn sai |
| 4 | Viết `_v10987_probe.py` dò **toàn bộ** mồ côi (chỉ đọc) | **18/145 mã** · chỉ **2** mục có hạn trong 05–07/08 (`FU-262` 05/08 · `FU-250` 06/08) |
| 5 | Soi tiếp `FU-256` | ô status RỖNG **và** hạn `None`, nhưng `ma_doc DO0806` + khối gốc V10978 đều nói **hạn 06/08** → thực chất là mục thứ 3 đến hạn trong cửa sổ |
| 6 | Kiểm `_v10900_consistency_guard.py` xem ngưỡng `FU-262` đã thoả chưa | có `C19` `C20` `C21`, **không có phép kiểm toàn vẹn giao diện** → **chưa thoả** |
| 7 | Chạy `_v10921_report_gate.py` bản toàn bộ **trước** khi sửa | exit **0** (nền sạch) |
| 8 | Dọn `desktop.ini` trong `.git` kho công khai | **267 → 0** · `git fetch` exit 0 · 0 ahead / 0 behind |
| 9 | **Mở rộng `K8`** 3 phần + thêm `--so` / `--hom-nay` | xong |
| 10 | **THỬ NGƯỢC ca thật**: chạy cổng mới trên sổ **CHƯA vá** | `K8` **TRƯỢT**, thoát 1, gọi đúng tên `FU-262` + `FU-250`, in đủ 18 mã · **7 phép kia vẫn ĐẠT** |
| 11 | Viết `_v10987_ghi_so.py` (có **cổng tự chặn nhãn tự chế**) rồi ghi sổ | `✓ 3/3 nhãn hợp lệ` · sổ +11.342 ký tự |
| 12 | Cập nhật `TAI_PHIEN_KHAC_DO_DUOC[06/08]` += `FU-256` | bắt buộc, không thì `J5` TRƯỢT |
| 13 | Viết `_v10987_thu_nguoc_k8.py` — bộ thử ngược **tái lập được**, 3 ca | **3/3 đúng kỳ vọng** |
| 14 | Sinh lại trang lịch | 38.160 byte · 247 dòng |
| 15 | Chạy 5 cổng kiểm **tách riêng** | tất cả exit 0 (chi tiết §6 báo cáo) |
| 16 | Prepend `CHANGELOG` + `SSOT`, viết báo cáo công khai, push cả hai kho | xong |

---

## 4. VẤP Ở ĐÂU

### 4.1 Vấp do lệnh đặt giả thuyết sai — không nghiêm trọng nhưng phải nói

Lệnh gợi ý ba khả năng: *"thieu `ma_doc` §58? thieu o han? nhan khong nam trong `TREO_STATUSES`?"*.
Đọc sổ thật thì **hai khả năng đầu không đúng** — `FU-262` có đủ `SC0805` và cả hai dạng ghi hạn.

**Nếu tin theo mà không kiểm:** agent sẽ "bổ sung `ma_doc`" cho một mục đã có `ma_doc`, mục **vẫn
mồ côi**, briefing **vẫn không hiện**, mà báo cáo lại ghi "đã bổ sung đủ trường". Đúng loại xanh
giả đang chữa.

### 4.2 Suýt để lọt `FU-256` — mục mất CẢ nhãn LẪN hạn

Theo đúng chữ của lệnh (*"muc nao han xa hon thi gom vao `FU-258`"*), `FU-256` đọc ra `hạn —` nên
đáng lẽ bị gom vào `FU-258` và **để tới sau**. Nhưng `ma_doc DO0806` và khối gốc V10978 đều nói
**hạn 06/08** — tức hạn thật nằm trong cửa sổ 3 ngày, chỉ bị **mất do lỗi ghi** của khối cập nhật
V10979 (bỏ bảng field, và tiêu đề mất luôn chữ `hạn 06/08`).

**Nếu bỏ qua:** một mục đến hạn **ngày mai** bị đẩy sang danh sách "hạn xa", tiếp tục vô hình —
**nặng hơn `FU-262`** vì mất cả hạn nên **không bộ đếm nào, kể cả phần (b) mới của `K8`**, nhìn
thấy được (phần (b) lọc theo `due_date`, mà `due_date=None`).

**Bài học:** đừng chỉ tin `due_date` máy đọc ra — đối chiếu với `ma_doc` và khối gốc phía dưới.

### 4.3 VẤP DO CHÍNH AGENT GÂY RA — bẫy regex `**status**` trong câu văn tài liệu

Khối V10987 lúc đầu có câu giải thích cho người đọc:

```
Bộ đọc chỉ nhận `| **status** |` hoặc `- **Trạng thái:**`,
```

Chuỗi đó chứa `**status**` **liền sau là dấu `|`** — khớp đúng regex của bộ đọc:

```python
_STATUS = re.compile(r"\*\*status\*\*\s*\|\s*`?([^`|\n]+)`?", re.I)
```

**Thử ngược ca B lộ ra ngay:** khi xoá ô status thật của `FU-256`, bộ đọc **nhảy xuống câu văn** và
lấy nhãn `= "hoặc"` thay vì rỗng. Đầu ra ca B in `FU-256(06/08=hoặc)` — sai.

**Đã sửa:** viết lại thành ``ô `**status**` trong bảng field, hoặc gạch đầu dòng
`- **Trạng thái:**` `` — bỏ dấu `|` liền sau. Chạy lại: ca B in đúng `FU-256(06/08=ô status RỖNG)`.

**Hậu quả nếu bỏ qua:** hôm nay **không sai** (ô status thật nằm trước câu văn nên `re.search` lấy
đúng — probe đã xác nhận `DEPLOYED_PENDING_LIVE_VERIFY`), nhưng để lại **bẫy nằm chờ**: phiên sau
viết khối cập nhật thiếu bảng field thì bộ đọc lấy nhãn `"hoặc"` — một **nhãn tự chế mới**, mồ côi
thêm một mục, và **khó tìm hơn nhiều** vì nó sinh ra từ chính câu văn tài liệu, không ai nghĩ tài
liệu có thể làm sai bộ đọc.

**Chính thử ngược bắt được lỗi này** — đúng như lệnh đã nói *"4/9 loi xanh gia trong ngay 04/08 chi
lo ra nho thu nguoc"*. Nếu chỉ chạy cổng xuôi và thấy 8/8, lỗi này lọt hoàn toàn.

### 4.4 `desktop.ini` — 267 tệp trong `.git` kho công khai

Quét ra **267 tệp**: phần lớn trong `.git/objects/**`, và **4 tệp trong `.git/logs/refs/**`**. Chưa
có tệp nào trong `.git/refs/` nên `git fetch` còn chạy — nhưng đó đúng là đường tới lỗi
`fatal: bad object refs/desktop.ini` mà `FU-266` ghi. Đã xoá **267 → 0**, `git fetch` exit 0.

**Nếu bỏ qua:** `git fetch` chết → `origin/main` local đứng yên → cổng báo cáo so `origin/main..HEAD`
thấy rỗng và **báo xanh dù chưa push**. Vì vậy phiên này không tin `git status`, mà xác minh bằng
`git ls-tree -r origin/main`.

### 4.5 Phát hiện thêm — 4 tệp `desktop.ini` ĐÃ LỌT VÀO LỊCH SỬ GIT

`git status` kho công khai báo 4 tệp `desktop.ini` **đã được commit từ trước** (trong
`V105_25_STATION_ALIAS_FIXUP_20260511/` và `V105_27_TOTAL_FORCE_CONTROL_20260511/`, cả thư mục gốc
lẫn `evidence/`) đang ở trạng thái sửa.

**Không stage, không commit** — ngoài phạm vi phiên, và lệnh cấm `git add -A`. Đã ghi bổ sung vào
`FU-266` (hạn 12/08): cần `git rm --cached` + thêm `.gitignore`.

### 4.6 PowerShell không có `find` / `tail` / `wc`

Lệnh gợi ý `find .git -name desktop.ini -delete` là cú pháp Unix. Trên PowerShell, `2>/dev/null` bị
hiểu thành `Out-File` và lỗi `Could not find a part of the path 'E:\dev\null'`; `tail` và `wc` cũng
không tồn tại. Đã đổi sang `Get-ChildItem -Recurse -Force -Filter desktop.ini | Remove-Item -Force`.

---

## 5. Việc CỐ Ý KHÔNG LÀM — và vì sao

| Không làm | Vì sao |
|---|---|
| Dựng `C22_giao_dien_toan_ven` để đóng `FU-262` | `_v10900_consistency_guard.py` chạy cron **18:05 trên VPS** → **phải deploy**, mà lệnh ghi rõ *"KHONG deploy, KHONG restart `lottery`"*. Viết code rồi để đó không deploy là đúng loại "xanh trên giấy" mà `FU-259` đang canh |
| Thêm `FIXED_PENDING_LIVE_VERIFY` vào `TREO_STATUSES` cho cổng xanh | Nới bộ nhãn để cổng xanh = nới cổng. Nhãn này là **biến thể thứ 4** của cùng một ý (`DEPLOYED_PENDING_LIVE_VERIFY` đã có) — thêm vào là nuôi dị bản |
| Dời hạn `FU-262` sang 06/08 để tránh quá hạn | **Dời hạn để tránh quá hạn chính là giấu việc.** Giữ 05/08 để briefing 06/08 bêu tên nếu chưa xong — đó là tác dụng cần có |
| Đòi `K8` "0 mồ côi toàn sổ" | Còn 15 mục nhãn cũ V54–V92 không phân loại nổi trong một phiên đêm → cổng đỏ vĩnh viễn → thành cổng bị bỏ qua, **tệ hơn** xanh giả |
| Phân loại 13 nhãn cũ ngay trong phiên | Không mục nào đến hạn trước 08/08; gom vào `FU-258` (hạn 06/08) kèm **danh sách đích danh + 3 họ nhãn + ngưỡng hạ `MO_COI_TRAN` 15 → 2** |
| Xử 4 tệp `desktop.ini` đã theo dõi trong kho công khai | Ngoài phạm vi; lệnh cấm `git add -A`. Ghi vào `FU-266` |
| Ghi bất cứ gì vào Notion | §57.1 — Notion **chỉ đọc**. Phiên này **không gọi một hàm Notion nào**, kể cả hàm đọc |

---

## 6. Số liệu trước / sau

| Chỉ số | Trước phiên | Sau phiên |
|---|---|---|
| Mồ côi toàn sổ | **18** | **15** |
| `FU-262` hiện trong briefing | **KHÔNG** | **CÓ** — ở mục "ĐẾN HẠN HÔM NAY", dòng đầu |
| Đến hạn hôm nay (05/08) | 4 | **5** |
| Mục theo dõi còn treo | 99 | **102** |
| Quá hạn | 1 (`FU-225`) | 1 (`FU-225`) — không đổi |
| `K8` soi bao nhiêu mã | **14** | **toàn sổ (145)** |
| `_v10981_kiem_lich.py` | 8/8 (**xanh giả**) | **8/8 thật**, có thử ngược chứng minh |
| `_v10982_kiem_lich9.py` | 8/8 | **8/8** · `J8` mồ côi 19 → **15** (giảm 4) |
| Tải 06/08 · 08/08 · 10/08 | 6 · 5 · 3 | **7** · **6** · **3** |
| `desktop.ini` trong `.git` kho công khai | **267** | **0** |
