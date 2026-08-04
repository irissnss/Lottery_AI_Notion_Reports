# Bối cảnh phiên V10983 — 04/08/2026 (giờ Việt Nam)

Ghi **nguyên văn** lời owner, agent đã làm gì sau mỗi câu, và vấp ở đâu. Không diễn giải lại lời
owner, không làm đẹp phần agent sai.

---

## 16:34 — owner báo lỗi

> **Owner:** "Hệ thống bị gì mà báo cảnh báo err connection failed ah em?"

**Agent làm gì:** dựng `_v10983_conn_probe.py` và `_v10983_conn_probe2.py`, đo trên máy chủ thật:

- `/api/health` → **200**
- `systemctl show lottery` → `active` từ **10:16:59**, `MainPID=770947`, **`NRestarts=0`**
- `journalctl -u lottery --since -3h` → **0 Traceback · 0 ERROR**, không chuỗi `ConnectionError` /
  `refused` / `timed out` / `Max retries` nào
- Nhìn nhịp ngày: lúc owner hỏi, cả 3 nguồn kết quả MN đều trả *"không có dữ liệu"* từ 16:30,
  thử lại mỗi 30 giây; **kết quả về 16:38:38** (Bạc Liêu, Bến Tre, Vũng Tàu). Lịch sử 7 ngày:
  MN luôn về 16:34–16:41 → chờ bình thường, **không phải lỗi**.

**Agent báo lại owner:** phần mềm không có lỗi nào, và hỏi owner nhìn thấy cảnh báo ở đâu — trình
duyệt, ứng dụng, hay phần mềm diệt virus.

---

## Owner làm rõ (owner viết chữ in)

> **Owner:** "GIAO DIỆN LOGIN ĐẦU TIÊN TRÊN ĐT AH EM CÓ VẺ NHƯ NHƯ CHƯA XÁC THỰC GÌ ĐÓ CỦA DOMAIN
> NÊN PHẦN MỀM KASPER CỦA ANH CHẶN TRUY CẬP AH EM, PC DESKTOP THÌ VÀO ĐƯỢC NHƯNG VẪN PHẢI XÁC
> NHẬN AN TOÀN MỚI VÀO ĐƯỢC NHA EM"

Câu này đổi hẳn hướng điều tra: **không phải lỗi app, mà là lớp tên miền / chứng chỉ** — lớp
trước giờ **chưa self-check nào canh**.

**Agent làm gì:**

1. `_v10983_ep_sweep.py` — quét **toàn bộ** endpoint frontend gọi: **không cái nào 5xx**.
2. `_v10983_probe3.py` / `_probe4.py` — soi 404 trong nginx access log: toàn bot dò lỗ hổng
   (`phpunit eval-stdin.php`, `.env`, `/cgi-bin/…`, `/..%2F..%2Fetc%2Fpasswd`, favicon, sitemap).
   **Rác internet, không phải frontend.**
3. `_v10983_read_nginx.py` + `_v10983_tls_check.py` — và ra nguyên nhân thật:

| | Đo được |
|---|---|
| DNS | **cả** `xs.io.vn` **và** `www.xs.io.vn` trỏ về `14.225.224.89` |
| nginx | `server_name xs.io.vn www.xs.io.vn` — nhận **cả hai** |
| SAN chứng chỉ | **chỉ `DNS:xs.io.vn`** · hạn 23/09/2026 |
| `https://xs.io.vn/login` | **200** |
| `https://www.xs.io.vn/login` | **000 — TLS từ chối** |

→ Chứng chỉ sai tên = dấu hiệu giả mạo với phần mềm diệt virus → **Kaspersky chặn cứng trên điện
thoại**. PC chỉ cảnh báo vì trình duyệt cho bấm bỏ qua. **Khớp chính xác điều owner mô tả.**

---

## ⚠ VẤP 1 — agent kết luận sai về cổng 80 TRƯỚC KHI ĐO

**Agent đã nói với owner:** *"trang đăng nhập chạy được cả trên HTTP thường nên bị chặn"*.

**Sai.** Agent suy diễn từ "cổng 80 mở" ra "cổng 80 phục vụ app" mà **chưa gọi thử một endpoint
nào**. Sau khi chạy `_v10983_port80.py` và `_v10983_apache.py`:

| | Sự thật |
|---|---|
| Ai giữ cổng 80 | **Apache**, không phải app |
| Trả gì | Trang giữ chỗ *"Welcome to nginx!"* từ `/www/server/apache/htdocs/index.html` (Last-Modified 17/04/2026) |
| `/login` trên cổng 80 | **404** |
| `/api/health` trên cổng 80 | **404** |
| App thật | nginx cổng **443** (và 8080) → `127.0.0.1:8000` |
| Chuyển hướng HTTP→HTTPS | **không có** |

**Agent đã đính chính với owner ngay trong phiên.**

*Nếu bỏ qua:* hướng sửa sẽ thành "ép HTTPS cho trang đăng nhập trên cổng 80" — sửa một thứ không
tồn tại, tốn một lượt deploy giữa khung ra số, mà bệnh thật (chứng chỉ thiếu `www`) vẫn nguyên.

**Bài học ghi lại:** đừng suy từ "cổng mở" ra "cổng phục vụ cái gì". Gọi thử endpoint trước rồi
mới nói.

---

## Owner chọn thời điểm sửa

Agent trình các mốc và rủi ro từng mốc (sửa ngay 16:40 giữa khung ra số / chờ sau MT 16:58 / chờ
sau MB 18:15).

> **Owner chọn:** "Sau 18:15, khi MB đã chốt xong - an toàn nhất"

**Agent làm gì:** viết `_v10983_fix_tls.py` **tự chờ đến sau 18:20** mới động tay. Trước đó chỉ
chạy `_v10983_mt_watch.py` canh MT chốt, không đụng gì.

**Kiểm trước khi sửa:** đường ACME `/.well-known/acme-challenge/` trả **200 cho cả hai tên** →
chắc chắn `certbot --expand` chạy được, không phải đoán.

---

## 18:20:20 → 18:20:51 — vá (31 giây, NGOÀI khung cấm 15:30–18:15)

1. Sao lưu `/etc/nginx/sites-available/lottery` + `/www/server/apache/htdocs/index.html` vào
   `/root/_v10983_backup/`
2. `certbot certonly --webroot -w /www/server/apache/htdocs --cert-name xs.io.vn -d xs.io.vn
   -d www.xs.io.vn --expand` — **chạy `--dry-run` trước** (`DRY_RUN_OK`), đạt rồi mới chạy thật
3. `nginx -t` → `systemctl reload nginx` (**reload, KHÔNG restart**)
4. Thay `index.html` cổng 80 thành trang chuyển hướng sang `https://xs.io.vn/`

**Kết quả:** SAN `DNS:xs.io.vn` → **`DNS:www.xs.io.vn, DNS:xs.io.vn`** · hạn 23/09 → **02/11/2026**
· `https://www.xs.io.vn/login` **000 → 200** · PID `lottery` **770947 trước và sau, không đổi** ·
**hash 4 bảng khoá giống hệt**.

---

## Sau đó — kiểm lại độc lập, không tin lời kể

Agent **tự đo lại** thay vì chép bảng số của bước trước:

- `curl` cả hai tên: `www=200 verify=0` · `nonwww=200 verify=0`
- PID `lottery` vẫn **770947**, `active`, health nội bộ 200
- Hash 4 bảng khoá: `predictions 5e4dbf167cee0e82` · `final_bundles 3c51731e5cfcd747` ·
  `lottery_results 7305048e8b8d3c80` · `model_daily_eval 89b4aa03fbf15b23` — **không đổi**
- `certbot renew --dry-run --cert-name xs.io.vn` → *"Simulating renewal … for xs.io.vn **and
  www.xs.io.vn** → all simulated renewals succeeded"*, chứng chỉ thật **giữ nguyên sê-ri**
- `webroot_map` trong `/etc/letsencrypt/renewal/xs.io.vn.conf` khai **cả hai tên** → gia hạn tự
  động (~03/10) không rơi mất `www`

**Không có điểm nào lệch so với bảng số của bước vá.**

---

## ⚠ VẤP 2 — bản sao lưu nginx chép NHẦM FILE

Khi đối chiếu md5 mới lộ ra:

| File | md5 |
|---|---|
| `/etc/nginx/sites-enabled/lottery` (**đang phục vụ thật**) | `d9f8f591…` |
| `/etc/nginx/sites-available/lottery` | `996b4b22…` |
| `/etc/nginx/sites-enabled/lottery.bak_pre_cache_20260726` | `996b4b22…` |
| `/root/_v10983_backup/nginx_lottery.conf` (**bản sao lưu vừa tạo**) | `996b4b22…` |

Tức bản sao lưu **không phải** file đang chạy. Khác đúng 2 dòng
`add_header Cache-Control "no-store" always`. Nguyên nhân: `sites-enabled/lottery` là **file
thường chứ không phải symlink** như thói quen Debian, nên `sites-available` đã trôi thành bản
chết từ lâu mà không ai biết.

*Nếu bỏ qua:* ai đó gỡ về bằng `cp /root/_v10983_backup/nginx_lottery.conf
/etc/nginx/sites-enabled/lottery` sẽ **âm thầm xoá hai dòng `no-store`** — endpoint admin bắt đầu
bị cache, lỗi rất khó truy vì cấu hình "trông vẫn đúng".

**Đã xử:** mục 8 báo cáo ghi rõ **KHÔNG được chép đè**; mở `FU-263` xử gốc. May mắn duy nhất:
phiên này **không sửa nginx.conf** (certbot expand giữ nguyên đường dẫn `live/`) nên không có gì
phải khôi phục.

---

## Ba việc canh cửa cùng ngày

**`FU-260`** — ngưỡng đặt trước: `DA_XONG_BLOCK` phải xuất hiện ≤60 giây sau khi official chốt.

| Miền | official chốt | ghi block | **trễ** |
|---|---|---|---|
| MT | 16:50:13 | 16:51:01 | **47 giây** ✓ |
| MB | 17:36:51 | 17:37:01 | **9 giây** ✓ |

→ **ĐẠT, đóng `CLOSED_PASS`.** Cam kết *"không đạt thì gỡ 3 dòng cron ngay trong tối"* **không
kích hoạt**.

**`FU-252`** — cửa sổ 04→10/08 được **3/21**, đêm 1/7 đủ cả ba miền: MN bt=22 · MT bt=29 ·
MB bt=71. MB trước đó ghi cuối 02/08 rồi **mất trắng 03/08**; tối nay là **đêm thử thật đầu tiên
sau khi vá cron — và MB ra số**.

**`FU-263`** — mở mới, xem vấp 2.

---

## ⚠ VẤP 3 — mã đọc đụng nhau

Đặt `FU-263 · DD0807` → cổng `_v10982_kiem_lich9.py` phép **J6** trượt ngay: `FU-255` đã giữ
`DD0807`. Đổi thành **`DD0807-1`** theo §58 (trùng loại+hạn thì thêm `-1`). Cổng bắt đúng, không
phải người phát hiện.

## ⚠ VẤP 4 — bảng mốc tải ghi cứng bị cũ ngay khi đóng/mở FU

Phép **J5** trượt: `TAI_PHIEN_KHAC_DO_DUOC` trong `_v10982_lich9.py` vẫn liệt `FU-260` ở 05/08 (đã
đóng) và chưa có `FU-263` ở 07/08. Đã cập nhật → J5 đạt lại, **8/8 phép**.

*Nếu bỏ qua:* mọi con số tải ngày trong `CHANGELOG`, trang lịch và báo cáo sẽ sai mà **không cổng
nào bắt được** — đúng loại "xanh giả". Đây chính là kịch bản V10982b siết J5 để chặn, và lần này
nó chặn thật.

## ⚠ VẤP 5 — cột trong hai bảng không đúng tên đoán

`v10979_early_block` dùng `date` (không phải `ngay`); `du_doan_test_bundles` dùng `run_date`
(không phải `date`) và bạch thủ tên là `test_bt`. Vòng truy vấn đầu trả `no such column`. Đã chạy
`PRAGMA table_info` rồi truy vấn lại.

*Nếu bỏ qua:* câu truy vấn lỗi rất dễ bị đọc thành "bảng trống" → kết luận `FU-260` trượt và **gỡ
cron oan**.

## ⚠ VẤP 6 — dòng MN trong `v10979_early_block` trễ 17.753 giây

Không phải lỗi cron: V10979 vừa lên ~10:15 nên lượt chạy đầu sau deploy mới bù dòng MN của sáng
(official MN chốt 05:19:56). MN nằm ngoài ngưỡng `FU-260` (chỉ đặt cho MT/MB). **05/08 là ngày
đầu MN chạy trong khung cron thật (05:00–06:59)** — trễ >60 giây lần nữa thì mở lỗi riêng.

---

## Ghi nhận quản trị trong cùng phiên

| Việc | Kết quả |
|---|---|
| `QD-023` vào `docs/OWNER_DECISION_LEDGER.json` | 24 → **25** quyết định · 4 mệnh đề máy kiểm |
| `_v10920_decision_ledger.py` | **0 TRÔI** · `QD-023` 🟢 khớp 4/4 |
| `CHANGELOG.md` · `CURRENT_TRUTH_SSOT.md` · `FOLLOW_UP_TRACKER.md` | prepend qua `_doc_prepend.prepend()` (+6.381 · +1.807 · +5.384 ký tự) — **không** `open(p,"w")` |
| `docs/PLAYBOOK_PERIODIC_FULL_SYSTEM_CHECK.md` | §2 thêm mục 7 *"chứng chỉ phủ mọi tên miền DNS trỏ về"* · §5 đóng dòng `FU-260`, bổ sung bằng chứng `FU-262`, thêm dòng `FU-263` |
| `_v10982_kiem_lich9.py` | **8/8 phép đạt** |
| Notion | **chỉ đọc** — không gọi một hàm ghi nào (§57.1) |
| Service `lottery` | **không restart** — chỉ `reload nginx` |

**Vì sao thêm phép kiểm vào playbook:** lớp tên miền / chứng chỉ **chưa self-check nào canh**.
Mọi phép đang có đều gọi `xs.io.vn` nên chúng **xanh hết** trong khi owner không vào được bằng
điện thoại. Đó là đúng loại "xanh giả" mà owner sợ nhất — nên nó phải thành phép cố định, chạy
được bằng một lệnh: `python web/backend/_v10983_kiem_tls.py`.
