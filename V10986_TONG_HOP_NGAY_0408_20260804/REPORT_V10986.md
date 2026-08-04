# V10986 — TỔNG HỢP TOÀN NGÀY 04/08/2026 · xác minh push thật · đo lại số đã báo

> **Phiên:** V10986 · **Owner yêu cầu:** 04/08/2026 23:54 (giờ VN) · **Viết:** 05/08 00:0x–01:xx
> **Loại phiên:** tài liệu + xác minh. **KHÔNG deploy · KHÔNG restart `lottery` · KHÔNG đụng
> đường ra số** — `QD-014` còn hiệu lực hết 08/08.
>
> **Commit riêng:** `b477f4e` (`Lottery_AI_Test`, đẩy `eb53295..b477f4e`)
> **Commit công khai:** `6b27535` (`Lottery_AI_Notion_Reports`, đẩy `2414bbe..6b27535`)
> Cả hai kho **0 ahead / 0 behind** sau khi đẩy; 15 tệp của phiên đã xác nhận có thật trên
> `origin/main` bằng `git ls-tree -r origin/main`.

---

## MỤC LỤC — 7 báo cáo con của ngày 04/08

| Phiên | Thư mục báo cáo (link tương đối) | Chủ đề |
|---|---|---|
| V10979 | [`../V10979_NHIP_CUON_CHIEU_5_MODEL_20260804/REPORT_V10979.md`](../V10979_NHIP_CUON_CHIEU_5_MODEL_20260804/REPORT_V10979.md) | Nhịp cuốn chiếu 5 model · tín hiệu "đã xong block" |
| V10980 | [`../V10980_KIEM_TOAN_DIEN_DAU_NGAY_20260804/REPORT_V10980.md`](../V10980_KIEM_TOAN_DIEN_DAU_NGAY_20260804/REPORT_V10980.md) | Kiểm toàn diện đầu ngày · vá cổng đếm việc |
| V10980b | [`../V10980_KIEM_TOAN_DIEN_DAU_NGAY_20260804/REPORT_V10980b.md`](../V10980_KIEM_TOAN_DIEN_DAU_NGAY_20260804/REPORT_V10980b.md) | Đính chính: V10979 deploy giữa phiên **(viết bổ sung trong V10986)** |
| V10981 | [`../V10981_LICH_CUON_CHIEU_DEN_1008_20260804/REPORT_V10981.md`](../V10981_LICH_CUON_CHIEU_DEN_1008_20260804/REPORT_V10981.md) | Lịch cuốn chiếu 14 mục tới 10/08 |
| V10981b | [`../V10981_LICH_CUON_CHIEU_DEN_1008_20260804/REPORT_V10981b.md`](../V10981_LICH_CUON_CHIEU_DEN_1008_20260804/REPORT_V10981b.md) | Đính chính: nhãn `SCHEDULED` làm 11 mục mồ côi **(viết bổ sung trong V10986)** |
| V10982 | [`../V10982_GIAN_NOT_9_MUC_NGAY_CHOT_20260804/REPORT_V10982.md`](../V10982_GIAN_NOT_9_MUC_NGAY_CHOT_20260804/REPORT_V10982.md) | Giãn nốt 9 mục ngày chốt |
| V10982b | [`../V10982_GIAN_NOT_9_MUC_NGAY_CHOT_20260804/REPORT_V10982b.md`](../V10982_GIAN_NOT_9_MUC_NGAY_CHOT_20260804/REPORT_V10982b.md) | Chuyển `FU-224` xuống 06/08 · siết J5 **(viết bổ sung trong V10986)** |
| V10983 | [`../V10983_VA_CHUNG_CHI_TEN_MIEN_20260804/REPORT_V10983.md`](../V10983_VA_CHUNG_CHI_TEN_MIEN_20260804/REPORT_V10983.md) | Vá chứng chỉ tên miền (Kaspersky chặn điện thoại) |
| V10984 | [`../V10984_KET_QUA_0408_VA_GHEP_NGHIEM_THU_OFFICIAL_20260804/REPORT_V10984.md`](../V10984_KET_QUA_0408_VA_GHEP_NGHIEM_THU_OFFICIAL_20260804/REPORT_V10984.md) | Kết quả 04/08 · ghép nghiệm thu × official |
| V10985 | [`../V10985_XU_BA_MUC_DEN_HAN_0408_20260804/REPORT_V10985.md`](../V10985_XU_BA_MUC_DEN_HAN_0408_20260804/REPORT_V10985.md) | Đóng 3 mục đến hạn · khoá §59 luật cắt model |

---

## 1. Tóm tắt một đoạn

Ngày 04/08 có **7 phiên chính + 3 phiên bổ sung**, tất cả đều đã có báo cáo công khai và
**đã thật sự nằm trên `origin/main`** — xác minh độc lập bằng `git ls-tree -r origin/main` sau khi
`git fetch` thành công, không dựa vào commit local. **Không có báo cáo nào từng "báo xanh mà chưa
push"**: 7/7 thư mục ngày 04/08 và 10/10 thư mục các ngày trước (V10969–V10978) đều đủ cả
`REPORT_*.md` lẫn `CONVERSATION_CONTEXT_*.md` trên remote; cả hai kho đều **0 ahead / 0 behind**.
Đo lại 17 con số chính thì **13 khớp y hệt**, **4 lệch** — trong đó 3 lệch có nguyên nhân chính
đáng (deploy sau đó) và **1 là báo cáo cũ nói quá**: cổng 80 chỉ chuyển hướng ở trang gốc, còn
`http://.../login` vẫn trả **404**. Phát hiện mới quan trọng nhất của phiên này: **cổng báo cáo
`_v10921_report_gate.py` chạy toàn bộ đang TRƯỢT (exit 1)** suốt từ 10:20 sáng 04/08 vì ba phiên bổ
sung `V10980b` `V10981b` `V10982b` có khối trong `CHANGELOG` mà không có báo cáo cổng nhìn thấy —
cả ngày không ai biết vì mọi phiên chỉ chạy cổng cho **một** phiên bản. Đã vá bằng cách **viết đủ
ba báo cáo còn thiếu**, không nới cổng.

## 2. Owner yêu cầu gì — nguyên văn

Yêu cầu của phiên này, owner nói lúc **23:54 ngày 04/08/2026** (giờ VN):

> *"Xem lại và tổng hợp đẩy báo cáo chi tiết dùm anh lên github report nha em"*

Toàn bộ lời owner trong ngày 04/08 (11 lượt, nguyên văn, không diễn giải) nằm ở
[`CONVERSATION_CONTEXT_V10986_20260804.md`](CONVERSATION_CONTEXT_V10986_20260804.md). Bốn lượt
định hình cả ngày:

| Giờ | Nguyên văn |
|---|---|
| 09:47 | *"Mốc thời gian không ổn ah em. Hay Sao đó mà trễ outout block luôn anh đã nói sau khi vào đủ dữ liệu và verify tiến hành dự đoán cho đơn model , lần lượt cuốn chiếu với 5 model AI 1 lượt mà em. mốc MB chốt 17h58 , mốc miền T 16h58 output cuối cùng xong sớm thì thông báo đã xong block thôi em. Kiểm tra toàn diện hệ thóng đầu ngày dùm anh luôn em"* |
| 16:34 | *"Hệ thông bị gì mà báo cảnh báo err connection failed ah em?"* |
| 21:35 | *"Thực sự quán chán ngán kết quả dự đoán quá tệ anh cần một kế hoạch triển khai sơm hơn dự kiến em xem thử dùm anh có triển khai được gì trước không em ? Theo như anh quan sat thấy offical cũng khá tiềm năng chứ em, cần 1 sự kết hợp hoàn hảo ở /nghiem-thu và offical nha . Kết quả dự đoán ngày hôm nay thế nào em thử tổng lực dùm anh."* |
| 23:54 | *"Xem lại và tổng hợp đẩy báo cáo chi tiết dùm anh lên github report nha em"* |

## 3. Đào bới / phát hiện

### 3.1 Mốc thời gian trong ngày (giờ VN)

| Giờ | Phiên | Việc | Commit riêng | Commit công khai |
|---|---|---|---|---|
| 09:47 | — | Owner nêu mốc thời gian + yêu cầu kiểm toàn diện | — | — |
| 10:15–10:17 | V10979 | Deploy `_v10979_early_block.py` + panel (PID 738032 → **770947**) | — | — |
| 10:17 | V10980 | Kiểm toàn diện đầu ngày · vá cổng đếm việc | `f202a7f` | `d4b7c76` (10:18) |
| 10:23 | V10980b | Đính chính: V10979 deploy giữa phiên · 18 → **21** phép | `f80a66c` | `0a21cea` |
| 10:27 | V10979 | Xong sớm thì báo "ĐÃ XONG BLOCK" (owner nhắc lần **thứ tư**) | `8a3df81` | `df1e2c0` |
| 10:28 | V10979b | Kiểm cuối: chạy đúng dòng lệnh cron, soi payload API | `665b548` | — |
| 10:29 | — | Owner: *"Giãn ra cuốn chiếu tới hết ngày 10/08 phải hoàn thành…"* | — | — |
| 10:51 | V10981 | Giãn 14 mục dồn 08/08 thành lịch cuốn chiếu (`QD-021`) | `66fc594` | `ac49dcd` (10:52) |
| 10:58 | V10981b | Đính chính: nhãn `SCHEDULED` làm **11/14** mục mồ côi · thêm **K8** | `45dc75c` | `7ded777` (10:59) |
| 11:00 | V10981d | Sinh lại bản đọc sổ quyết định (`QD-021` khớp 5/5) | `56b5bc0` | — |
| 11:0x | — | Owner: *"Giãn luôn 9 mục cũ đó ra 05-09/08 cho ngày chốt nhẹ"* | — | — |
| 12:15 | — | Owner: *"tiếp tục đi em, gián đoạn nữa rồi em"* | — | — |
| 12:35 | V10982 | Giãn nốt 9 mục — ngày chốt **11 → 3** mục (`QD-022`) | `c5fe204` | `7f4fafa` |
| 12:43 | — | Owner: *"Chuyển xuống 06/08 - 09/08 còn 8 mục"* | — | — |
| 12:52 | V10982b | Chuyển `FU-224` 09/08 → 06/08 · **siết phép J5** | `feb7169` | `e66aa4d` |
| 16:34 | — | Owner báo lỗi *"err connection failed"* trên điện thoại | — | — |
| 18:45 | V10983 | Cấp lại chứng chỉ cho **cả hai tên miền** · cổng 80 | `08ec33e` | `c5c3086` (18:46) |
| 21:35 | — | Owner: *"chán ngán kết quả dự đoán quá tệ… official khá tiềm năng chứ em"* | — | — |
| 21:59:41 | V10984 | Deploy bảng ghép + API + panel · restart (PID → **801640**) | — | — |
| 22:11 | V10984 | Ghép `/nghiem-thu` × official — **không cách nào hơn official** | `a2a7e61` | `4ff1651` (22:12) |
| 22:34 | — | Owner: *"Tiếp đi em anh hết token API Key gián đoạn 1 tý em ơi"* | — | — |
| 22:4x | — | Owner chọn: **"xử luôn tối nay"** ba mục đến hạn | — | — |
| 23:30 | V10985 | Đóng `FU-187` `FU-191` `FU-212` · khoá **§59 (A57)** | `5c2f2d1` | `77d337a` (23:32) |
| 23:39 | V10985 bổ sung | Mở **`FU-266`** — `desktop.ini` làm `git fetch` chết | `eb53295` | `2414bbe` |
| 23:54 | — | Owner: *"Xem lại và tổng hợp đẩy báo cáo chi tiết…"* | — | — |

Tổng trong ngày: **18 commit riêng · 15 commit công khai**.

### 3.2 Bảng 7 phiên × kết quả × commit × trạng thái cổng kiểm

| Phiên | Kết quả chính | Commit riêng | Commit công khai | Trên `origin/main` | Cổng kiểm |
|---|---|---|---|---|---|
| **V10979** | Cuốn chiếu 5 model **đang chạy thật** (42/42 lượt/14 ngày). Dựng `_v10979_early_block.py` + panel + 3 phép tự kiểm (18→21). Phát hiện `monitoring.html` **bị cắt cụt tại 2^18 byte** | `8a3df81` `665b548` | `df1e2c0` | ✓ 8 tệp | 21/21 phép · panel đăng ký đủ |
| **V10980** | Bắt **cổng đếm việc báo xanh giả**: in *"81 treo / 0 quá hạn"* trong khi thật là **97 treo · 1 quá hạn · 17 mồ côi**. Tìm ra căn nguyên `FU-245` (hook treo `sys.stdin.read()`) | `f202a7f` | `d4b7c76` | ✓ 19 tệp | đã vá, đối chứng độc lập |
| **V10980b** | Đính chính ba con số vì V10979 deploy giữa phiên | `f80a66c` | `0a21cea` | ✓ (trong V10980) | `run_checks()` 21 · OK 21 · LỆCH 0 |
| **V10981** | Giãn 14 mục đơn 08/08, trần 3 mục/ngày · `QD-021` · cổng `_v10981_kiem_lich.py` 8 phép | `66fc594` | `ac49dcd` | ✓ 7 tệp | **8/8 ĐẠT** |
| **V10981b** | **Vấp tự gây:** nhãn `SCHEDULED` làm 11/14 mục mồ côi · trả nhãn thật + thêm **K8** | `45dc75c` | `7ded777` | ✓ (trong V10981) | K8 thử ngược: TRƯỢT đúng 11 mã |
| **V10982** | 10/08 từ **11 → 3** mục · `QD-022` · cổng `_v10982_kiem_lich9.py` (J1–J8) | `c5fe204` | `7f4fafa` | ✓ 7 tệp | **8/8 ĐẠT** |
| **V10982b** | Chuyển `FU-224` xuống 06/08 · **siết J5** vì bảng mốc tự so với chính mình | `feb7169` | `e66aa4d` | ✓ (trong V10982) | J5 thử ngược: TRƯỢT đúng |
| **V10983** | Cấp lại chứng chỉ phủ **cả hai tên miền** (serial `069FEA4D…3ACA`, hạn **02/11**) · `FU-260` **ĐẠT** | `08ec33e` `5f5a9bc` | `c5c3086` `f158a36` | ✓ 17 tệp | PID không đổi · hash 4 bảng y hệt |
| **V10984** | 04/08 official **1/3** miền, nghiệm thu **0/3**. Ghép: trùng **73,33%**, **cả 5 cách ghép đều TỆ HƠN** official-only | `a2a7e61` `162412e` `460eee6` | `4ff1651` `c20b53d` | ✓ 8 tệp | bảng bóng 4 cờ đúng · panel 60s |
| **V10985** | `FU-187` `FU-191` `FU-212` **đóng đúng hạn** · khoá **§59 (A57)** ở 5/5 mặt quy tắc · **không cắt model nào** | `5c2f2d1` `eb53295` | `77d337a` `2414bbe` | ✓ 5 tệp | 0 TRÔI · sửa 3 con số sai trước khi khoá |

### 3.3 Xác minh push THẬT — việc ưu tiên cao nhất (vì `FU-266`)

Lý do phải làm: `FU-266` ghi rằng Google Drive đẻ `desktop.ini` vào `.git/refs` làm `git fetch`
chết (`fatal: bad object refs/desktop.ini`). Khi `fetch` chết, `origin/main` local **đứng yên**,
nên `git status` vẫn khai *"up to date"* và cổng báo cáo vẫn xanh **dù chưa push gì**.

Cách đo (không tin lời kể, không tin commit local):

1. Quét `.git` cả hai kho tìm `desktop.ini` → **không còn tệp nào** (đã dọn trong V10985)
2. `git fetch --all --prune` cả hai kho → **exit 0**, không lỗi
3. `git rev-list --left-right --count origin/…​...HEAD` → public **0 0** · private **0 0**
4. `git ls-tree -r origin/main --name-only` → đọc **cây tệp thật trên remote** (2.136 tệp)
5. Đối chiếu từng thư mục phiên bản

| Nhóm | Số phiên bản | Có trên `origin/main` | Đủ `REPORT_` + `CONVERSATION_CONTEXT_` |
|---|---|---|---|
| Ngày 04/08 (V10979–V10985) | 7 | **7/7** | **7/7** |
| Các ngày trước (V10969–V10978) | 10 | **10/10** | **10/10** |

**Kết luận: KHÔNG có báo cáo nào từng báo "đã push" mà thực ra chưa lên remote.** `FU-266` là rủi
ro thật nhưng **chưa gây mất mát nào**. Bằng chứng: [`evidence/xac_minh_push.json`](evidence/xac_minh_push.json).

### 3.4 Đo lại các con số đã báo — 13 khớp, 4 lệch

Đo lúc **05/08 00:0x** (giờ VN), chỉ đọc, không đụng runtime.

| # | Mục | Đã báo trong ngày | Đo lại | Kết luận |
|---|---|---|---|---|
| 1 | Chứng chỉ — serial | `069FEA4D…3ACA` | `069FEA4D4332631687BFA0AB431A65D83ACA` | ✓ khớp |
| 2 | Chứng chỉ — hạn | 02/11 | `notAfter=Nov 2 10:22:15 2026 GMT` | ✓ khớp |
| 3 | Chứng chỉ — SAN | cả hai tên | `DNS:www.xs.io.vn, DNS:xs.io.vn` | ✓ khớp |
| 4 | `https://xs.io.vn/api/health` | 200 | **200** | ✓ |
| 5 | `https://www.xs.io.vn/api/health` | 200 | **200** | ✓ |
| 6 | Bundle MN 04/08 | bt=22 · 15 model · 05:19:56 | y hệt (`bach_thu_status=LOSE`) | ✓ |
| 7 | Bundle MT 04/08 | bt=60 · 13 model · 16:50:13 | y hệt (`bach_thu_status=WIN`) | ✓ |
| 8 | Bundle MB 04/08 | bt=71 · 14 model · 17:36:51 | y hệt (`bach_thu_status=LOSE`) | ✓ |
| 9 | `v10979_early_block` 04/08 | MN/MT/MB đều "đã xong block" | **3/3 `DA_XONG_BLOCK`** · sớm 625'4" / 7'47" / 21'9" | ✓ |
| 10 | `ghep_nt_official_daily` | có dòng · 4 cờ shadow đúng | **15 dòng** · **0 dòng cờ sai** | ✓ |
| 11 | Độ trùng lặp ghép | 73,33% (11/15) | **11/15 = 73,33%** | ✓ |
| 12 | 4 ô lệch | official đúng cả 4, nghiệm thu sai cả 4 | **4/4** `official_trung_mien=1` · `nt_trung_mien=0` | ✓ |
| 13 | Panel `/monitoring` làm mới 60s | có | trong danh sách nạp đầu (dòng 8184) **và** `setInterval(…, 60000)` (dòng 8199) | ✓ |
| 14 | **PID `lottery`** | **770947 không đổi** (V10983) | **801640** · `NRestarts=0` · từ 21:59:42 | **LỆCH — có lý do** |
| 15 | **`monitoring.html`** | vá về **563.654** byte (V10979) | **577.617** byte | **LỆCH — có lý do** |
| 16 | **Cổng 80** | *"đổi trang cổng 80 thành chuyển hướng https"* | `/` → **200** meta-refresh · **`/login` → 404** | **LỆCH — báo cáo nói quá** |
| 17 | Treo / mồ côi | 97 treo · 17 mồ côi (V10980) | **98 treo · 18 mồ côi** | LỆCH — trôi trong ngày |

**Giải thích bốn chỗ lệch:**

- **#14 PID.** Chuỗi PID trong ngày là `738032 → 770947 (V10979 lúc 10:15) → 801640 (V10984 lúc
  21:59:42)`. Câu *"PID 770947 không đổi"* của V10983 **đúng tại thời điểm V10983**; V10984 deploy
  sau đó nên PID hiện tại khác. `NRestarts=0` vì `systemctl restart` chủ động không tính vào bộ đếm
  restart do lỗi. **Không phải sự cố.**
- **#15 `monitoring.html`.** Lớn hơn 563.654 vì V10984 thêm panel ghép. Điều cần khẳng định:
  **không bị cắt lại** — 577.617 byte, xa ngưỡng cắt cũ 262.144 byte (2^18).
- **#16 Cổng 80 — đây là chỗ báo cáo V10983 nói quá.** Đo thật từ máy chủ:
  `http://xs.io.vn/` và `http://www.xs.io.vn/` trả **200** kèm trang HTML
  `<meta http-equiv="refresh" content="0; url=https://xs.io.vn/">`, còn
  `http://xs.io.vn/login` và `http://www.xs.io.vn/login` trả **404**. Nghĩa là **chỉ trang gốc**
  được chuyển hướng, mọi đường dẫn sâu vẫn 404; và đó là **meta-refresh của trình duyệt**, không
  phải chuyển hướng HTTP 301 (`curl` không thấy `redirect_url` nào). Apache (`httpd`) vẫn giữ cổng
  80 — đúng như V10983 mô tả. **Ảnh hưởng thực tế:** thấp, vì `https://.../login` trả **200** ở cả
  hai tên miền và trình duyệt hiện đại vào https trước; nhưng ai gõ thẳng
  `http://xs.io.vn/login` vẫn gặp 404. Mở **`FU-267`**.
- **#17 Treo/mồ côi.** Trôi tự nhiên trong ngày: mở thêm `FU-259`…`FU-266`, đóng 3 mục, nên 97→98
  và 17→18. Khớp với phép J8 (*"tổng mồ côi toàn sổ 18, trước phiên 19, giảm 1"*).

### 3.5 Chỗ **không đo được từ máy owner** — Kaspersky đang cắt giữa TLS

Khi đo chứng chỉ **từ máy local**, kết quả trả về là:

```
SUBJECT = CN=xs.io.vn
ISSUER  = CN=Kaspersky Anti-Virus Personal Root Certificate, O=AO Kaspersky Lab
SERIAL  = 42000000196A71CBB2      (không phải 069FEA4D…3ACA)
NOTAFTER= 2027-02-02              (không phải 02/11/2026)
SAN     = DNS:www.xs.io.vn, DNS:xs.io.vn
```

Kaspersky **thay chứng chỉ thật bằng chứng chỉ nó tự ký** để soi lưu lượng HTTPS. Vì vậy:

1. **Không thể xác minh chứng chỉ thật từ máy owner** — mọi số serial/hạn đo ở PC đều là số của
   Kaspersky. Phải đo **từ máy chủ** (`openssl s_client -connect 127.0.0.1:443`), và đo từ máy chủ
   thì serial/hạn/SAN **khớp y hệt** những gì V10983 báo.
2. Kaspersky **có sao chép SAN** từ chứng chỉ thật (cả hai tên đều còn) → xác nhận gián tiếp bản vá
   V10983 đã tới được máy owner.
3. Đây chính là gốc chuyện owner phải *"bấm xác nhận an toàn"* trên PC: phần mềm đang chen vào
   giữa. Vá chứng chỉ máy chủ là **điều kiện cần**, nhưng phần Kaspersky cảnh báo còn phụ thuộc
   cấu hình máy owner — nằm ngoài tầm với của máy chủ.

### 3.6 Phát hiện MỚI của phiên này — cổng báo cáo đang trượt cả ngày

Chạy `python web/backend/_v10921_report_gate.py` (quét **toàn bộ**, không chỉ định phiên bản):

```
V10982B   ✗ KHÔNG CÓ BÁO CÁO — vi phạm A55_VIOLATION_REPORT_MISSING
V10981B   ✗ KHÔNG CÓ BÁO CÁO — vi phạm A55_VIOLATION_REPORT_MISSING
V10980B   ✗ KHÔNG CÓ BÁO CÁO — vi phạm A55_VIOLATION_REPORT_MISSING
✗ 3 phiên bản thiếu/không đạt · mã thoát 1
```

Cơ chế: cổng đọc `CHANGELOG.md` lấy mọi tiêu đề khớp `^## (V\d{4,6}[A-Za-z]?)`, nên
`## V10980b` được coi là **một phiên bản độc lập** và bị đòi thư mục/báo cáo riêng. Ba phiên bổ sung
trong ngày đều có khối `CHANGELOG` nhưng nội dung chỉ nằm **lẫn trong báo cáo cha**, không có tệp
`REPORT_V1098xb.md` nào để cổng nhìn thấy.

**Vì sao cả ngày không ai biết:** mọi phiên chỉ chạy cổng cho **một** phiên bản của mình
(`_v10921_report_gate.py V10982` → exit 0), không lần nào chạy bản quét toàn bộ. Chính khối
V10982b trong `CHANGELOG` ghi *"`_v10921_report_gate.py V10982` | exit 0"* — đúng, nhưng không phải
điều cần biết.

## 4. Hướng xử lý và vì sao chọn

### 4.1 Với cổng báo cáo đang trượt — ba phương án

| Phương án | Kết luận |
|---|---|
| Sửa cổng để **bỏ qua** hậu tố `b` (coi `V10980b` ≡ `V10980`) | **loại** — nới cổng cho vừa hiện trạng. Phiên bổ sung là **việc thật có sửa file, có deploy, có quyết định owner**; A55 đòi báo cáo là đòi đúng |
| Xoá khối `## V10980b` khỏi `CHANGELOG` cho cổng khỏi thấy | **loại** — giấu việc để cổng xanh, đúng thứ owner ghét nhất |
| **Viết đủ ba báo cáo còn thiếu** theo khung 9 phần | **CHỌN** — cổng xanh vì hết thiếu thật, không vì được nới |

### 4.2 Với chỗ lệch cổng 80 — không sửa trong phiên này

`QD-014` cấm đụng đường ra số tới hết 08/08, và sửa cấu hình Apache/nginx là **đụng hạ tầng đang
phục vụ**. Ảnh hưởng thực tế thấp (https `/login` = 200 ở cả hai tên). Nên: **ghi nhận bằng số, mở
`FU-267`, không tự sửa lúc nửa đêm**. Đây cũng đúng luật playbook — bằng chứng rõ nhưng **rủi ro
sửa lớn hơn lợi ích tức thời**, nên đo và hẹn lịch thay vì đụng production.

### 4.3 Với các con số lệch — ghi số thật, không sửa báo cáo cũ

Không viết đè báo cáo trong ngày. Số cũ **đúng tại thời điểm đo**; phần đổi về sau ghi trong bảng
mục 3.4 kèm lý do. Xoá dấu vết là làm mất khả năng truy nguyên.

## 5. Đã làm gì

### 5.1 Bảng file × thay đổi

| File | Việc |
|---|---|
| `V10986_TONG_HOP_NGAY_0408_20260804/REPORT_V10986.md` | **MỚI** — báo cáo tổng hợp này |
| `V10986_TONG_HOP_NGAY_0408_20260804/CONVERSATION_CONTEXT_V10986_20260804.md` | **MỚI** — nguyên văn 11 lượt owner trong ngày |
| `V10986_TONG_HOP_NGAY_0408_20260804/evidence/*` | **MỚI** — kết quả xác minh push · đo lại · output cổng |
| `V10980_…/REPORT_V10980b.md` | **MỚI** — vá thiếu báo cáo A55 |
| `V10981_…/REPORT_V10981b.md` | **MỚI** — vá thiếu báo cáo A55 |
| `V10982_…/REPORT_V10982b.md` | **MỚI** — vá thiếu báo cáo A55 |
| `web/backend/_v10986_xac_minh.py` `_xac_minh2.py` `_xac_minh3.py` | **MỚI** — đo lại VPS (chỉ đọc) |
| `web/backend/_v10986_evidence.py` | **MỚI** — xác minh push thật trên `origin/main` |
| `web/backend/_v10986_trich_owner.py` `_soi_transcript.py` `_doc_ctx.py` `_doc_qd.py` `_bang_commit.py` | **MỚI** — trích nguyên văn owner · đọc kết quả |
| `CHANGELOG.md` · `docs/CURRENT_TRUTH_SSOT.md` | prepend khối V10986 (+4.521 / +1.531 ký tự) |
| `docs/FOLLOW_UP_TRACKER.md` | mở `FU-267` (+2.073 ký tự, prepend) |
| `web/backend/_v10982_lich9.py` | **SỬA** — thêm `FU-267` vào mốc tải 08/08 (bắt buộc, xem mục 7.4) |

**Backup:** `backups/v10986_pre/_v10982_lich9.py.pre` — file mã nguồn **duy nhất** bị sửa trong
phiên. Mọi tài liệu đều **prepend** qua `_doc_prepend.prepend()` (từ chối ghi nếu tệp ngắn đi), các
tệp còn lại đều là **thêm mới**.

### 5.2 Deploy · hash

**KHÔNG deploy · KHÔNG restart `lottery` · KHÔNG đụng đường ra số.** Mọi lệnh chạm VPS đều mở DB ở
chế độ `mode=ro`.

Hash 4 bảng khoá tại **05/08 00:0x** (mốc tham chiếu cho phiên sau):

| Bảng | Số dòng | SHA256 (40 ký tự đầu) |
|---|---|---|
| `predictions` | 11.713 | `7b27df5056380737e6129c7cc0094c6b67df9ab8` |
| `final_bundles` | 474 | `a8f4570db97f09dcdebad48ca62ea38edce19e79` |
| `lottery_results` | 15.213 | `92ccf706553921288f2105f96e2a399b89835429` |
| `model_daily_eval` | 11.577 | `c559a75ad34b78ed89ed7d265dca3e13349fe545` |

Dịch vụ: `active` · PID **801640** · `NRestarts=0` · health **200**.

## 6. Cổng kiểm

Chạy **tách riêng từng lệnh** (gộp nhiều lệnh từng bị cắt mất kết quả):

| Cổng | Kết quả |
|---|---|
| `_v10920_decision_ledger.py` | **0 TRÔI** · 27 quyết định · `QD-020` 8/8 · `QD-021` 5/5 · `QD-022` 9/9 · `QD-023` 4/4 · `QD-024` 5/5 · `QD-025` 11/11 *(có một vòng `QD-022` TRÔI 1/9 do chính phiên này gây ra — đã xử, xem mục 7.4)* |
| `_v10981_kiem_lich.py` | **8/8 ĐẠT** · `LICH_CUON_CHIEU_DAT` · K8: 14/14 nhãn hợp lệ, đã đóng 3/14 |
| `_v10982_kiem_lich9.py` | **TRƯỢT J5** khi vừa mở `FU-267` (mốc tải cũ) → sau khi cập nhật mốc: **8/8 ĐẠT** · mốc khớp sổ thật 7/7 ngày. Xem mục 7.4 |
| `_v10925_rule_sync_check.py --check` | **6/6 mặt quy tắc đồng bộ** · 4/4 `.mdc` tự nạp · không còn file quy tắc chết |
| `_v10920_session_start.py` | 0 checkpoint quá hạn · 98 treo · **1 quá hạn** (`FU-225`) · **4 đến hạn 05/08** · **18 mồ côi** |
| `_v10921_report_gate.py` (toàn bộ) | **trước phiên: exit 1** (3 phiên bản thiếu) → **sau khi vá + commit: exit 0** |
| `_v10921_report_gate.py V10986` | **exit 0** |
| Xác minh push độc lập | **17/17 thư mục báo cáo có thật trên `origin/main`** · public 0/0 · private 0/0 |

## 7. Vướng vấp

### 7.1 Cổng báo cáo trượt cả ngày mà không ai biết — nghiêm trọng nhất

**Hậu quả nếu bỏ qua:** ba phiên có sửa file, có quyết định owner (`QD-022` bổ sung), có siết cổng
kiểm — nhưng **owner không có báo cáo công khai nào để đọc** về chúng. Đúng vi phạm
`A55_VIOLATION_REPORT_MISSING`, kéo dài **~13,5 giờ**. Gốc rễ không phải cổng sai mà là **thói quen
gọi cổng theo một phiên bản** thay vì quét toàn bộ trước khi kết phiên.

### 7.2 Báo cáo V10983 nói quá về cổng 80

Câu *"đổi trang cổng 80 thành chuyển hướng https"* đúng với `/`, **sai với mọi đường dẫn khác**.
`http://.../login` trả **404**. **Hậu quả nếu bỏ qua:** owner tin rằng gõ `http://xs.io.vn/login`
trên điện thoại sẽ tự sang https, thực tế gặp 404 — đúng loại "trang không vào được" mà owner đã
báo lúc 16:34. Mở `FU-267`.

### 7.3 Vấp do chính agent gây ra trong phiên này

- **Bộ trích nguyên văn owner chạy sai lần đầu, trả về 0 tin nhắn.** Nguyên nhân: bóc sạch mọi thẻ
  `<...>` trong khi giờ nằm trong `<timestamp>` và lời owner nằm trong `<user_query>` — bóc xong là
  mất cả hai. Đã soi lược đồ thật của tệp `.jsonl` rồi viết lại; lần hai lấy đúng **28 lượt**, lọc
  còn **11 lượt owner thật** (17 lượt còn lại là prompt điều phối giữa các agent, không phải lời
  owner).
- **Đo chứng chỉ từ máy local ra số lạ** (`SERIAL=42000000196A71CBB2`, hạn 2027). Suýt kết luận
  V10983 báo sai. Đọc trường `ISSUER` mới thấy là **Kaspersky tự ký**. Bài học: đo TLS từ máy có
  phần mềm diệt virus **không phải bằng chứng**; phải đo từ máy chủ.
- **Regex tìm `loadAllSections` không khớp** nên vòng ba báo `None` và script chết ở dòng in. Đã đổi
  sang dò trực tiếp ba chỗ gọi `loadGhepNghiemThu` — kết quả rõ hơn regex ban đầu.
- **Chạy `python -c` với dấu `;` và list-comprehension nhiều câu lệnh** → `SyntaxError`. Đúng cái bẫy
  đã ghi trong `CLAUDE.md`; đã chuyển sang viết tệp script.

### 7.4 Phép J5 bắt được chính thay đổi của phiên này — bằng chứng cổng V10982b có tác dụng thật

Sau khi mở `FU-267` (hạn 08/08) vào `docs/FOLLOW_UP_TRACKER.md`, chạy lại sổ quyết định thì
**`QD-022` chuyển sang 🔴 TRÔI 1/9**, và `_v10982_kiem_lich9.py` **TRƯỢT J5** với thông báo:

```
J5 · 08/08: mốc=['FU-201'] ≠ sổ thật=['FU-201', 'FU-267']
```

Đây **đúng kịch bản V10982b dựng J5 để bắt**: đổi sổ theo dõi mà quên bảng mốc tải ghi cứng
`TAI_PHIEN_KHAC_DO_DUOC` thì mọi con số tải trong lịch, changelog và báo cáo đều sai. Trước V10982b
thì cổng vẫn xanh; nay nó **bắt ngay trong vòng một phút**, chỉ đích danh mã và ngày lệch.

**Đã xử:** backup `backups/v10986_pre/_v10982_lich9.py.pre` → thêm `FU-267` vào mốc 08/08 → J5 về
**8/8 ĐẠT**, sổ quyết định về **0 TRÔI**. Tải 08/08 thành **6** (không phải 5) — ghi đúng số thật
vào phần "còn nợ" thay vì để bảng cũ.

**Đáng ghi nhận:** đây là lần đầu một cổng "xanh giả" đã vá **bắt lỗi thật do phiên sau gây ra**,
chứ không phải chỉ chứng minh bằng thử ngược.

### 7.5 Cái bẫy nhãn mồ côi vẫn còn sống

`FU-262` (mở trong V10979, hạn **05/08**) mang nhãn `FIXED_PENDING_LIVE_VERIFY` — **không** thuộc
`TREO_STATUSES`, nên đang nằm trong danh sách **18 mồ côi** và **không hiện ở dòng "đến hạn hôm
nay"**. Phép **K8** chỉ canh 14 mục của nhóm V10981, **không canh toàn sổ**. **Hậu quả nếu bỏ qua:**
đúng mục theo dõi việc `/monitoring` từng bị cắt cụt lại là mục vô hình với bộ đếm — trượt hạn mà
không ai biết. Ghi vào phần "còn nợ".

## 8. Gỡ về

| Muốn gỡ gì | Lệnh | Mất bao lâu |
|---|---|---|
| Toàn bộ phiên này | `git revert <commit V10986>` ở cả hai kho | ~2 phút |
| Ba báo cáo bổ sung | xoá `REPORT_V10980b.md` `REPORT_V10981b.md` `REPORT_V10982b.md` | ~1 phút |
| Khối `CHANGELOG` / `SSOT` | xoá khối V10986 ở đầu tệp | ~1 phút |
| `FU-267` | xoá mục khỏi `docs/FOLLOW_UP_TRACKER.md` | ~1 phút |

**Không có gì để gỡ ở phía runtime** — phiên này không deploy, không restart, không sửa mã đang
chạy. Mọi truy cập VPS đều `mode=ro`. Backup: không cần (chỉ thêm mới + prepend).

## 9. Theo dõi tiếp

Xem chi tiết ở mục **"Còn nợ"** bên dưới. Mục mới mở trong phiên này:

| Mã máy | Mã đọc | Việc | Ngưỡng hành động bằng số | Hạn |
|---|---|---|---|---|
| **`FU-267`** | **`SC0808`** | Cổng 80 chỉ chuyển hướng `/`, đường dẫn sâu vẫn 404 | `http://xs.io.vn/login` và `http://www.xs.io.vn/login` phải trả **301/302 → https**, không phải 404 | **08/08** |

---

## CHUỖI LỖI "XANH GIẢ" PHÁT HIỆN TRONG NGÀY

Đây là **mạch xuyên suốt ngày 04/08**: cổng kiểm báo đạt trong khi thực tế hỏng. Chín cái, xếp theo
thứ tự phát hiện.

| # | Phiên | Cổng báo xanh trong khi… | Đã vá chưa | **Còn hỏi gì** |
|---|---|---|---|---|
| 1 | V10976 (03/08, nhắc lại cho liền mạch) | **5 lỗi** ở tầng cổng tự kiểm: cổng thoát 0 kể cả khi in "✗ thiếu" | **Đã vá** — `_v10921_report_gate.py` nay thoát 1 khi trượt | Còn cổng nào khác vẫn nuốt mã thoát? → `FU-250`, hạn 06/08 |
| 2 | V10980 | Cổng đếm việc in *"81 treo / 0 quá hạn"* trong khi thật là **97 treo · 1 quá hạn · 17 mồ côi**. Hai lỗ: chỉ tìm hạn ở ô `**due**` (kho có 51 ô đó nhưng **68 tiêu đề** ghi `hạn DD/MM`) → mất hạn **24 mã**; `TREO_STATUSES` khai 6 nhãn trong khi kho dùng **28 nhãn** → **14 mã** rơi khỏi bộ đếm | **Đã vá** | Danh sách nhãn vẫn ghi cứng — thêm nhãn mới là lại rơi. Xem #3 |
| 3 | V10981b | Nhãn `SCHEDULED` **tự chế** làm **11/14 mục** thành mồ côi ngay trong phiên đi xử chuyện mồ côi | **Đã vá** + thêm phép **K8**, thử ngược TRƯỢT đúng 11 mã | **CÒN**: K8 chỉ canh **14 mục** của nhóm, **không canh toàn sổ**. `FU-262` đang mồ côi vì đúng lỗi này |
| 4 | V10982b | Phép **J5** đọc **bảng mốc tải ghi cứng** rồi so với chính bảng đó → **luôn xanh** | **Đã vá** — J5 nay đối chiếu với sổ thật. **Chứng minh trong thực tế ở phiên này:** J5 bắt ngay khi V10986 mở `FU-267` mà chưa cập nhật mốc (mục 7.4) | Còn bảng ghi cứng nào khác tự so với chính mình? Chưa quét hệ thống |
| 5 | V10979 | `monitoring.html` **bị cắt cụt tại đúng 262.144 byte = 2^18** từ commit V10977 (03/08 19:21), mất **53,5%** nội dung và mất vòng làm mới 60s — **18 phép tự kiểm vẫn xanh suốt 2 ngày** | **Đã vá** — về 563.654 byte; nay **577.617** byte (V10984 thêm panel) | **CÒN**: `FU-262` chưa đóng, và **đang mồ côi** nên không hiện ở bộ đếm đến hạn. Hạn 05/08 |
| 6 | V10983 | **Mọi phép tự kiểm chỉ gọi `xs.io.vn`**, không phép nào thử `www.xs.io.vn` → chứng chỉ thiếu tên `www` suốt mà mọi cổng vẫn xanh | **Đã vá** — cấm phép mới vào playbook: kiểm tên miền phải thử **mọi tên DNS trỏ về** | **CÒN**: cổng 80 `/login` vẫn **404** (mục 3.4 #16) → `FU-267`, hạn 08/08 |
| 7 | V10985 | Phép **K8 chặn oan mục ĐÃ XONG** — càng làm đúng lịch, cổng càng đỏ | **Đã vá** — K8 chấp nhận cả `DONG_STATUSES` | — |
| 8 | V10985 / `FU-266` | Google Drive đẻ `desktop.ini` vào `.git/refs` → `git fetch` chết (`fatal: bad object refs/desktop.ini`) → `origin/main` local đứng yên → **cổng báo cáo có thể báo xanh dù chưa push** | Đã dọn `.git`; **V10986 xác minh: KHÔNG mất báo cáo nào** (17/17 có thật trên remote) | **CÒN**: Google Drive vẫn có thể đẻ lại. Chưa có cổng tự canh `.git` sạch → `FU-266`, hạn 12/08 |
| 9 | **V10986 (phiên này)** | `_v10921_report_gate.py` quét toàn bộ **TRƯỢT (exit 1)** suốt ~13,5 giờ vì 3 phiên bổ sung không có báo cáo cổng nhìn thấy — cả ngày không ai biết vì mọi phiên chỉ chạy cổng **cho một phiên bản** | **Đã vá** — viết đủ 3 báo cáo còn thiếu, **không nới cổng** | **CÒN**: chưa có gì bắt buộc chạy bản **quét toàn bộ** trước khi kết phiên. Đề nghị đưa vào chuỗi hoàn tất |

**Đọc ngang chín cái này thấy một mẫu chung:** cổng kiểm được viết cùng lúc với thứ nó canh, bởi
cùng một người, nên **thừa hưởng luôn giả định sai** của thứ đó. Bốn cái (#3, #4, #6, #9) chỉ lộ ra
khi có người **thử ngược** — cố tình tạo trạng thái hỏng rồi xem cổng có bắt không. Ba cái (#2, #5,
#8) lộ ra khi **đo bằng công cụ khác** với công cụ đã dựng cổng.

---

## CÂU TRẢ LỜI THẲNG CHO OWNER VỀ CHẤT LƯỢNG DỰ ĐOÁN

Owner nói lúc 21:35: *"chán ngán kết quả dự đoán quá tệ… official cũng khá tiềm năng chứ em, cần 1
sự kết hợp hoàn hảo ở /nghiem-thu và offical nha"*.

**Không chiều lòng. Số liệu nói ba điều, cả ba đều không dễ nghe.**

### 1. Kết quả 04/08 và 7 ngày

| | 04/08 | 7 ngày |
|---|---|---|
| Official | **1/3 miền** (trúng MT — Đắk Lắk) | **9/21 ô = 42,86%** |
| Nghiệm thu | **0/3 miền** | — |

Chi tiết 04/08: lô2 MT **WIN** · lô2 MN **PARTIAL** · lô3 + xiên **trượt sạch**. MN số **72 về
thật** và **nằm trong lô2**, nhưng bạch thủ chọn 22 — `grok-4.3` chọn đúng 72 mà **không được lấy**.
MB số 71 **không đài nào có**, **25/27 model MB trượt**.

### 2. Theo trục tiến (bằng chứng chính, không phải backtest)

| Miền | Tỉ lệ | z |
|---|---|---|
| MN | 22,73% | **0,83** |
| MT | 17,65% | **0,09** |
| MB | 42,86% | **1,20** |

**Cả ba z đều < 2.** Ngưỡng `QD-013` để đặt tiền thật là **≥ +3pp VÀ z ≥ 2**. Chưa miền nào chạm.
Cổng lợi thế: **8/9 ô đang ÂM**. Ô dương duy nhất là MT cửa sổ 180 ngày: **+0,67pp** (z **0,35**) —
**còn thiếu 1,18pp mới hoà vốn**.

### 3. Ghép `/nghiem-thu` với official — đo rồi, KHÔNG giúp

Đây là điều owner hỏi thẳng, nên trả lời thẳng:

| Đo | Kết quả |
|---|---|
| Độ trùng lặp | **73,33%** — 11/15 ô hai bên ra **cùng một số** |
| 4 ô lệch | **official đúng cả 4 · nghiệm thu sai cả 4** |
| 5 cách ghép thử | **cả 5 đều TỆ HƠN** official-only (**+216k**) |

Nghĩa là: `/nghiem-thu` **không mang thêm thông tin** so với official — ba phần tư thời gian nó nói
y hệt, và mỗi lần nó nói khác thì **nó sai**. Không có cách ghép nào cứu được điều đó; ghép hai
nguồn mà một nguồn không có thông tin riêng thì chỉ thêm nhiễu.

**Câu "official khá tiềm năng"** — official *nhỉnh hơn nghiệm thu*, đúng. Nhưng nhỉnh hơn một thứ
đang âm **không có nghĩa là dương**: 8/9 ô cổng lợi thế vẫn âm, cả ba z vẫn < 2.

### 4. Bao nhiêu ngày nữa mới kết luận được

**Cần thêm ~536 ngày** để đủ mẫu phân biệt tín hiệu thật với may rủi ở mức hiệu ứng đang đo. Đó là
hệ quả số học của việc hiệu ứng quá nhỏ (**+0,67pp**) so với độ nhiễu, **không phải** vì đo chậm.

**Nói thẳng:** muốn kết luận sớm hơn thì phải có **hiệu ứng lớn hơn**, tức phải đổi cách làm chứ
không phải đo lâu hơn. Đo thêm ngày trên cùng một cách làm chỉ cho cùng một kết quả với sai số hẹp
hơn. Vì vậy `QD-013` (dừng đặt tiền thật) và `QD-014` (đóng băng đường ra số tới hết 08/08) **vẫn
đúng**; ba việc mở sau 08/08 (`QD-015` `QD-016` `QD-017` `QD-018`) là chỗ có thể tạo hiệu ứng lớn
hơn.

---

## FU MỞ / ĐÓNG TRONG NGÀY 04/08

| Mã máy | Mã đọc §58 | Việc | Hạn | Mở/Đóng | Phiên |
|---|---|---|---|---|---|
| `FU-187` | `KS0804-1` | Nghiệm thu hook đầu phiên | 04/08 | **ĐÓNG — `CLOSED_PASS`** | V10985 |
| `FU-191` | `XH0804` | Luật cắt model an toàn cho combo-super | 04/08 | **ĐÓNG — `CLOSED_PASS`** | V10985 |
| `FU-212` | `DO0804` | Chênh RF → công bố | 04/08 | **ĐÓNG — `CLOSED_REPORT`** | V10985 |
| `FU-260` | `DP0805` | Canh live thông báo "đã xong" | 05/08 | **ĐÓNG — ĐẠT** (MT trễ 47s · MB trễ 9s) | V10983 |
| `FU-259` | `KS0805` | C17/C18 mới đúng trên giấy, chưa chạy thật | 05/08 | **MỞ** | V10980 |
| `FU-261` | `QD0809` | "Xong" phải bằng "bất động" — chờ owner sau 08/08 | 09/08 | **MỞ** | V10979 |
| `FU-262` | `SC0805` | `/monitoring` từng bị cắt cụt 53,5% mà không cổng nào biết | 05/08 | **MỞ** — *đang mồ côi* | V10979 |
| `FU-263` | `DD0807-1` | Dọn bản sao lưu nginx lẫn trong `sites-enabled` | 07/08 | **MỞ** | V10983 |
| `FU-264` | `DO0811` | Đo bóng ghép `/nghiem-thu` × official | 11/08 | **MỞ** | V10984 |
| `FU-265` | `DO1208` | Sàn `MIN_MAU_DU_TUYEN=5` không áp ở nhánh chọn thật | 12/08 | **MỞ** | V10985 |
| `FU-266` | `DD1208` | Google Drive đẻ `desktop.ini` vào `.git/refs` | 12/08 | **MỞ** | V10985 |
| `FU-267` | `SC0808` | Cổng 80 chỉ chuyển hướng `/`, `/login` vẫn 404 | 08/08 | **MỞ** | **V10986** |
| `FU-244` | — | Cấm cron cổng lợi thế | kéo sớm về 04/08 | cập nhật | V10984 |
| `FU-224` | `UI0806` | Dọn trang frontend trùng/chết | 09/08 → **06/08** | đổi hạn | V10982b |

Đến hạn 04/08: **3 → 0**. Mở mới trong ngày: **9** (`FU-259`…`FU-267`). Đóng: **4**.

## QUYẾT ĐỊNH OWNER KÝ TRONG NGÀY (QD-020 → QD-025)

| Mã | Nguyên văn (rút gọn, giữ chữ owner) | Mệnh đề máy kiểm |
|---|---|---|
| **QD-020** | *"Mốc thời gian không ổn ah em… lần lượt cuốn chiếu với 5 model AI 1 lượt mà em. mốc MB chốt 17h58, mốc miền T 16h58 output cuối cùng xong sớm thì thông báo đã xong block thôi em. Kiểm tra toàn diện hệ thóng đầu ngày dùm anh luôn em"* | **8/8** |
| **QD-021** | *"Giãn ra cuốn chiếu tới hết ngày 10/08 phải hoàn thành, làm lần lượt những vấn đề nào xác thực rõ ràng, đơn giản làm trước tới cuối cùng 10/08 phải xong"* | **5/5** |
| **QD-022** | *"Giãn luôn 9 mục cũ đó ra 05-09/08 cho ngày chốt nhẹ"* · bổ sung: *"Chuyển xuống 06/08 - 09/08 còn 8 mục"* | **9/9** |
| **QD-023** | *"Hệ thống bị gì mà báo cảnh báo err connection failed ah em?"* · *"GIAO DIỆN LOGIN ĐẦU TIÊN TRÊN ĐT AH EM CÓ VẺ NHƯ NHƯ CHƯA XÁC THỰC GÌ ĐÓ CỦA DOMAIN NÊN PHẦN MỀM KASPER CỦA ANH CHẶN TRUY CẬP AH EM, PC DESKTOP THÌ VÀO ĐƯỢC NHƯNG VẪN PHẢI XÁC NHẬN AN TOÀN MỚI VÀO ĐƯỢC NHA EM"* · *"Sau 18:15, khi MB đã chốt xong - an toàn nhất"* | **4/4** |
| **QD-024** | *"Thực sự quán chán ngán kết quả dự đoán quá tệ anh cần một kế hoạch triển khai sơm hơn dự kiến… Theo như anh quan sat thấy offical cũng khá tiềm năng chứ em, cần 1 sự kết hợp hoàn hảo ở /nghiem-thu và offical nha. Kết quả dự đoán ngày hôm nay thế nào em thử tổng lực dùm anh."* | **5/5** |
| **QD-025** | *"xử luôn tối nay"* (ba mục đến hạn) · nhắc gốc lần hai: *"cắt model ảnh hưởng đến combo super mới quan trọng cận thận chỗ này"* | **11/11** |

Tất cả **0 TRÔI**. Yêu cầu 23:54 của phiên này được ghi nhận là **yêu cầu báo cáo**, không mở `QD`
mới — vì nó không đặt ra ràng buộc mới lên code, mà lặp lại nghĩa vụ đã có ở **§57 (A55)**. Đã ghi
vào `CHANGELOG` và `SSOT` để truy nguyên được.

## CÒN NỢ

### Mục theo dõi còn treo

| Mã | Mã đọc | Việc | Hạn | Vì sao chưa xong |
|---|---|---|---|---|
| `FU-261` | `QD0809` | Phần **đóng băng sớm** ("xong" = "bất động") | 09/08 | Phải chạm writer `final_bundles` — `QD-014` cấm tới hết 08/08. **Chờ sau 08/08** |
| `FU-262` | `SC0805` | Nghiệm thu vá `/monitoring` | **05/08** | Nhãn `FIXED_PENDING_LIVE_VERIFY` làm mục **mồ côi** — không hiện ở bộ đếm đến hạn |
| `FU-263` | `DD0807-1` | Bản sao lưu nginx lẫn trong `sites-enabled` | 07/08 | Cần cửa sổ an toàn để đụng cấu hình web |
| `FU-265` | `DO1208` | Sàn 5 lượt thật không áp ở nhánh chọn thật của combo-super | 12/08 | Chưa đo tác động; đụng combo-super là đụng `QD-014` |
| `FU-266` | `DD1208` | Google Drive đẻ `desktop.ini` vào `.git` | 12/08 | Đã dọn lần này, **chưa có cổng tự canh** |
| `FU-259` | `KS0805` | C17/C18 chưa từng chạy thật (cron 18:05, deploy 19:23) | **05/08** | Chờ lượt cron thật; ngưỡng: **đúng 21 dòng** |
| `FU-267` | `SC0808` | Cổng 80 `/login` còn 404 | 08/08 | **Mới mở phiên này** |

### Việc từ 05/08 trở đi

| Ngày | Số mục | Gồm |
|---|---|---|
| **05/08** | 5 | `FU-207` `FU-254` `FU-243` `FU-259` `FU-262` |
| 06/08 | 6 | `FU-210` `FU-257` `FU-245` `FU-250` `FU-258` `FU-224` |
| 07/08 | 5 | `FU-193` `FU-223` `FU-244` `FU-255` `FU-263` |
| **08/08** | 6 | `FU-186` `FU-203` `FU-215` `FU-188` `FU-201` `FU-267` — **hết đóng băng `QD-014`** |
| 09/08 | 8 ⚠ | `FU-192` `FU-216` `FU-217` `FU-185` `FU-253` `FU-200` `FU-202` `FU-261` |
| 10/08 | 3 | `FU-226` `FU-231` `FU-252` — **ngày chốt** |

**Trần ≤5 mục/ngày CHƯA đạt**: 06/08 = 6 · **08/08 = 6** (tăng 1 vì `FU-267` mở trong phiên này) ·
09/08 = 8. Đã nói thẳng từ V10982b, không ép số cho đẹp.

### Ba việc nên làm nhưng chưa có mã theo dõi

1. **Mở rộng phép K8 ra toàn sổ** — hiện chỉ canh 14 mục nhóm V10981; `FU-262` mồ côi là bằng chứng
   lỗ hổng còn sống.
2. **Bắt buộc chạy `_v10921_report_gate.py` bản quét TOÀN BỘ** trước khi kết phiên, thay vì chỉ
   `report_gate <VERSION>`. Chính chỗ này làm cổng trượt 13,5 giờ mà không ai biết.
3. **Quét xem còn bảng ghi cứng nào tự so với chính mình** như J5 trước khi siết.

---

*Báo cáo lập theo khung §57.3 (A55.3) — đủ 9 phần, không xoá tiêu đề. Notion chỉ đọc, không ghi
(§57.1).*
