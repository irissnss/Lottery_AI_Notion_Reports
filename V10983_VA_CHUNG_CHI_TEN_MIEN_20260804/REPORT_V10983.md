# V10983 — Không phải lỗi phần mềm: chứng chỉ chỉ khai một tên miền trong khi DNS trỏ về hai

**Ngày:** 04/08/2026 · **Commit riêng:** `08ec33e` (`Lottery_AI_Test`, 28 file, +1.749 dòng) · **Commit công khai:** `c5c3086` (báo cáo + 15 tệp `evidence/`) · **Trạng thái:** đã vá, đã kiểm lại, `QD-023` khớp 4/4

> Báo cáo theo khung **A55.3** (owner ký 01/08/2026 11:04). Đủ 9 phần.

---

## 1. Tóm tắt

Owner báo *"err connection failed"* lúc 16:34 ngày 04/08. **Không phải lỗi phần mềm** — health 200, service `lottery` active từ 10:16 với `NRestarts=0`, **0 Traceback và 0 ERROR** trong journal 3 giờ, không endpoint frontend nào trả 5xx. Nguyên nhân nằm ở lớp chưa ai canh: **chứng chỉ Let's Encrypt chỉ khai `DNS:xs.io.vn`** trong khi DNS trỏ **cả `www.xs.io.vn`** về cùng máy chủ và nginx nhận cả hai tên — nên `https://www.xs.io.vn/login` trả **000 (TLS từ chối)** còn `https://xs.io.vn/login` trả 200. Chứng chỉ sai tên là dấu hiệu giả mạo với phần mềm diệt virus nên Kaspersky **chặn cứng trên điện thoại**; PC chỉ cảnh báo vì trình duyệt cho bấm bỏ qua. Lớp thứ hai: **cổng 80 do Apache giữ**, trả trang giữ chỗ *"Welcome to nginx!"*, `/login` trên cổng 80 trả **404**.

Owner chọn thời điểm sửa **"sau 18:15, khi MB đã chốt xong"**. Script tự chờ, động tay lúc **18:20:20–18:20:51** (31 giây). Sau khi vá: SAN = `DNS:www.xs.io.vn, DNS:xs.io.vn`, hạn 23/09 → **02/11/2026**, `https://www.xs.io.vn/login` **000 → 200**, cổng 80 chuyển hướng sang HTTPS. **PID `lottery` 770947 trước và sau — không đổi.** **Hash 4 bảng khoá giống hệt trước/sau.** `QD-014` nguyên vẹn.

Cùng phiên: **`FU-260` nghiệm thu ĐẠT và đóng** (MT trễ 47 giây, MB trễ 9 giây — ngưỡng 60 giây), **`FU-252` được 3/21** (đêm 1/7, đủ cả ba miền, MB ra số lần đầu sau sự cố 03/08), và **mở `FU-263`** dọn bản sao lưu nginx lẫn trong `sites-enabled`.

## 2. Owner yêu cầu gì (nguyên văn)

**04/08/2026 16:34 (giờ VN):**

> "Hệ thống bị gì mà báo cảnh báo err connection failed ah em?"

**Làm rõ ngay sau đó (owner viết chữ in):**

> "GIAO DIỆN LOGIN ĐẦU TIÊN TRÊN ĐT AH EM CÓ VẺ NHƯ NHƯ CHƯA XÁC THỰC GÌ ĐÓ CỦA DOMAIN NÊN PHẦN MỀM KASPER CỦA ANH CHẶN TRUY CẬP AH EM, PC DESKTOP THÌ VÀO ĐƯỢC NHƯNG VẪN PHẢI XÁC NHẬN AN TOÀN MỚI VÀO ĐƯỢC NHA EM"

**Owner được hỏi khi nào sửa và chọn:**

> "Sau 18:15, khi MB đã chốt xong - an toàn nhất"

Owner tự chọn thời điểm; agent chỉ trình các mốc. Đã ghi thành `QD-023` trong `docs/OWNER_DECISION_LEDGER.json`.

## 3. Đào bới / phát hiện

### 3.1 Loại trừ phần mềm trước (để không sửa nhầm chỗ)

| Phép đo | Công cụ | Kết quả |
|---|---|---|
| `/api/health` | `_v10983_conn_probe.py` | **200** |
| Service `lottery` | `systemctl show` | `active` từ **10:16:59**, `MainPID=770947`, **`NRestarts=0`** |
| Journal 3 giờ | `journalctl -u lottery --since -3h` | **0 Traceback · 0 ERROR** · không chuỗi `ConnectionError` / `refused` / `timed out` / `Max retries` nào |
| Quét **toàn bộ** endpoint frontend gọi | `_v10983_ep_sweep.py` | **không cái nào 5xx** |
| 404 trong nginx access log | `_v10983_probe3.py` `_probe4.py` | Toàn bot dò lỗ hổng: `phpunit eval-stdin.php`, `.env`, `/cgi-bin/…`, `/..%2F..%2Fetc%2Fpasswd`, favicon, sitemap — **rác internet, không phải frontend** |

### 3.2 Thời điểm owner hỏi, hệ đang chờ kết quả MN — đúng nhịp bình thường

Lúc 16:34 cả 3 nguồn kết quả MN đều trả *"không có dữ liệu"* từ 16:30, thử lại mỗi 30 giây; **kết quả về 16:38:38** (Bạc Liêu, Bến Tre, Vũng Tàu). Lịch sử 7 ngày: MN luôn về **16:34–16:41**. Đây là cửa sổ chờ bình thường, **không phải lỗi** — nhưng cũng không phải cái owner nhìn thấy.

### 3.3 Nguyên nhân thật 1 — chứng chỉ thiếu tên `www`

`_v10983_tls_check.py` đo trên hạ tầng thật:

| | Đo được |
|---|---|
| DNS | **cả** `xs.io.vn` **và** `www.xs.io.vn` trỏ về `14.225.224.89` |
| nginx | `server_name xs.io.vn www.xs.io.vn` — nhận **cả hai** |
| SAN chứng chỉ | **chỉ `DNS:xs.io.vn`** · sê-ri `05928A784AC741B6CC040CE2403559965602` · hạn 23/09/2026 |
| `https://xs.io.vn/login` | **200** |
| `https://www.xs.io.vn/login` | **000 — TLS từ chối bắt tay** |
| `openssl -verify_hostname` | chỉ non-www đạt |

Với phần mềm diệt virus, chứng chỉ không khớp tên = dấu hiệu giả mạo → Kaspersky chặn cứng. Trình duyệt PC chỉ cảnh báo vì cho người dùng bấm bỏ qua — **khớp chính xác điều owner mô tả**.

### 3.4 Nguyên nhân thật 2 — cổng 80 là trang giữ chỗ Apache, không phải app

| | Đo được (`_v10983_port80.py`, `_v10983_apache.py`) |
|---|---|
| Ai giữ cổng 80 | **Apache** (không phải app) |
| Trả gì | Trang giữ chỗ *"Welcome to nginx!"* từ `/www/server/apache/htdocs/index.html`, Last-Modified **17/04/2026** |
| `/login` trên cổng 80 | **404** |
| `/api/health` trên cổng 80 | **404** |
| App thật ở đâu | nginx cổng **443** (và 8080) → proxy `127.0.0.1:8000` |
| Chuyển hướng HTTP→HTTPS | **không có** |

Ghép hai lớp: điện thoại gõ tên miền trần → vào `http://` → **trang lạ**; hoặc gõ kèm `www` → **chứng chỉ sai tên** → Kaspersky chặn. Máy bàn có lẽ nhớ địa chỉ kèm `www` nên chỉ cảnh báo.

### 3.5 Kiểm trước khi động tay

Đường ACME `/.well-known/acme-challenge/` trả **200 cho cả hai tên** → chắc chắn `certbot --expand` chạy được, không phải đoán.

## 4. Hướng xử lý và vì sao chọn

| Phương án | Kết luận |
|---|---|
| **Mở rộng chứng chỉ sang `www` bằng `certbot --expand`** ✅ **CHỌN** | Sửa đúng nguyên nhân, giữ nguyên đường dẫn `live/xs.io.vn/` nên **không phải sửa nginx.conf** — ít bề mặt rủi ro nhất. Có `--dry-run` để thử trước. |
| Gỡ bản ghi DNS `www` | Loại. Owner có thể đang dùng địa chỉ kèm `www` (máy bàn nhớ địa chỉ đó), gỡ đi là làm hỏng đường vào đang chạy được. |
| Thêm `server` block nginx chuyển `www` → non-www | Loại **một mình nó**. Chuyển hướng vẫn phải bắt tay TLS trước → Kaspersky vẫn chặn ở đúng bước đó. Không sửa được gốc. |
| **Cổng 80 → trang chuyển hướng sang HTTPS** ✅ **CHỌN** | Sửa lớp thứ hai. Chọn thay `index.html` của Apache thay vì giành cổng 80 cho nginx: giành cổng là đổi ai giữ cổng vào giữa lúc `QD-014` đang đòi "một tuần yên" — rủi ro lớn hơn nhiều so với lợi ích. |
| Vá ngay lúc 16:40 | **Loại — owner tự chọn.** Owner ấn định *"Sau 18:15, khi MB đã chốt xong"*. Script tự chờ tới sau 18:20 mới động tay. |

**Thời điểm do owner quyết, không phải agent.** Agent chỉ trình các mốc và nêu rủi ro của từng mốc.

## 5. Đã làm gì

### 5.1 Trên máy chủ — deploy 18:20:20 → 18:20:51 (31 giây), NGOÀI khung cấm 15:30–18:15

`web/backend/_v10983_fix_tls.py` **tự chờ đến sau 18:20** mới chạy. Bốn bước:

1. Sao lưu `/etc/nginx/sites-available/lottery` và `/www/server/apache/htdocs/index.html` vào `/root/_v10983_backup/`
2. `certbot certonly --webroot -w /www/server/apache/htdocs --cert-name xs.io.vn -d xs.io.vn -d www.xs.io.vn --expand` — **chạy `--dry-run` trước** (`DRY_RUN_OK`), đạt rồi mới chạy thật
3. `nginx -t` rồi `systemctl reload nginx` — **reload, KHÔNG restart**
4. Thay `index.html` cổng 80 bằng trang chuyển hướng sang `https://xs.io.vn/` (meta refresh + `location.replace`, giữ nguyên đường dẫn và query)

Script tự gỡ về nếu kiểm sau khi vá không đạt. Không phải dùng đến.

### 5.2 Kết quả đo trước → sau

| | Trước | Sau |
|---|---|---|
| SAN chứng chỉ | `DNS:xs.io.vn` | **`DNS:www.xs.io.vn, DNS:xs.io.vn`** |
| Sê-ri | `05928A784AC741B6CC040CE2403559965602` | `069FEA4D4332631687BFA0AB431A65D83ACA` |
| Hạn | 23/09/2026 | **02/11/2026** |
| `https://www.xs.io.vn/login` | **000 (hỏng)** | **200** |
| `https://xs.io.vn/login` | 200 | 200 |
| `https://xs.io.vn/api/health` | 200 | 200 |
| Cổng 80 | trang giữ chỗ Apache | trả chuỗi `https://xs.io.vn` (chuyển hướng) |
| Xác minh tên miền (`openssl -verify_hostname`) | chỉ non-www đạt | **cả hai đạt** |

### 5.3 An toàn — không đụng đường ra số

| | |
|---|---|
| PID `lottery` | **770947 trước và sau, KHÔNG đổi** · `active` · health nội bộ 200 |
| Hash `predictions` | `5e4dbf167cee0e82` → `5e4dbf167cee0e82` |
| Hash `final_bundles` | `3c51731e5cfcd747` → `3c51731e5cfcd747` |
| Hash `lottery_results` | `7305048e8b8d3c80` → `7305048e8b8d3c80` |
| Hash `model_daily_eval` | `89b4aa03fbf15b23` → `89b4aa03fbf15b23` |
| `QD-014` | **nguyên vẹn** — không đổi 15 model official, combo-super filter, override toggles, `/du-doan` writer, `final_bundles` writer |

Bundle 3 miền hôm nay đều chốt **trước hạn**: MN bt=**22**, 15 model, 05:19:56 (hạn 15:45) · MT bt=**60**, 13 model, 16:50:13 (hạn 16:58) · MB bt=**71**, 14 model, 17:36:51 (hạn 17:58).

### 5.4 Tệp thay đổi

| File | Việc |
|---|---|
| `web/backend/_v10983_fix_tls.py` | **MỚI** — chờ qua 18:20, sao lưu, certbot expand (dry-run trước), reload nginx, thay trang cổng 80, tự gỡ nếu không đạt |
| `web/backend/_v10983_kiem_tls.py` | **MỚI** — mệnh đề máy kiểm của `QD-023`, chạy được bất cứ lúc nào |
| `web/backend/_v10983_conn_probe.py` `_conn_probe2.py` `_probe3.py` `_probe4.py` `_ep_sweep.py` `_read_nginx.py` `_port80.py` `_apache.py` `_tls_check.py` `_mt_watch.py` | **MỚI** — chuỗi đào bới |
| `web/backend/_v10983_verify.py` … `_verify5.py` | **MỚI** — kiểm lại sau khi vá: PID · hash · FU-260 · FU-252 · panel · gia hạn khô |
| `web/backend/_v10983_ghi_quyet_dinh.py` `_v10983_ghi_so.py` | **MỚI** — ghi `QD-023` và ba tài liệu quản trị qua `prepend()` |
| `web/backend/_v10982_lich9.py` | `TAI_PHIEN_KHAC_DO_DUOC`: 05/08 bỏ `FU-260` (đã đóng) · 07/08 thêm `FU-263` |
| `docs/OWNER_DECISION_LEDGER.json` | **`QD-023` MỚI** · 24 → **25** quyết định · mệnh đề kiểm toàn sổ → **100** |
| `CHANGELOG.md` | +6.381 ký tự (prepend) |
| `docs/CURRENT_TRUTH_SSOT.md` | +1.807 ký tự (prepend) |
| `docs/FOLLOW_UP_TRACKER.md` | +5.384 ký tự (prepend) — `FU-260` `CLOSED_PASS` · `FU-252` 3/21 · `FU-263` mới |
| `docs/PLAYBOOK_PERIODIC_FULL_SYSTEM_CHECK.md` | §2 thêm mục 7 (chứng chỉ phủ mọi tên DNS) · §5 đóng dòng `FU-260`, bổ sung bằng chứng `FU-262`, thêm dòng `FU-263` |
| `docs/LICH_CUON_CHIEU_DEN_10082026.md` | sinh lại · 34.915 byte |

**Backup:** máy chủ `/root/_v10983_backup/` (`nginx_lottery.conf`, `apache_index.html`) · chứng chỉ cũ còn nguyên ở `/etc/letsencrypt/archive/xs.io.vn/*2.pem`.

### 5.5 Ba việc canh cửa cùng ngày

**`FU-260` — ĐẠT, đóng `CLOSED_PASS`.** Ngưỡng đặt trước: `DA_XONG_BLOCK` phải xuất hiện **≤60 giây** sau khi official chốt, kèm `lane_ket_qua` khác rỗng.

| Miền | official chốt | ghi block lúc | **trễ** | sớm hơn hạn | `lane_da_kich_hoat` | `lane_ket_qua` |
|---|---|---|---|---|---|---|
| MT | 16:50:13 | 16:51:01 | **47 giây** ✓ | 467 s (7ph47s) | 1 | khác rỗng ✓ |
| MB | 17:36:51 | 17:37:01 | **9 giây** ✓ | 1.269 s (21ph09s) | 1 | khác rỗng ✓ |

Cam kết *"không đạt thì gỡ 3 dòng cron ngay trong tối"* **không kích hoạt** — cron giữ nguyên.

**`FU-252` — 3/21, đêm 1/7 đạt.** Cửa sổ 04→10/08. Đêm 04/08 đủ cả ba miền: `MN_NGHIEMTHU_1908_V1` bt=**22** · `MT_NGHIEMTHU_1908_V1` bt=**29** · `MB_NGHIEMTHU_1908_V1` bt=**71** (15 model, ghi 17:37:01). Chỗ quan trọng: MB trước đó ghi cuối **02/08** rồi **mất trắng 03/08** — lượt vá cron MB (17:46/17:50/17:54) chỉ hiệu lực từ 03/08 nên tối nay là **đêm thử thật đầu tiên, và MB ra số**. Giữ `DEPLOYED_PENDING_LIVE_VERIFY`.

**`FU-263` — MỚI**, xem mục 9.

## 6. Cổng kiểm

| Cổng | Kết quả |
|---|---|
| `_v10983_kiem_tls.py` (đo lại độc lập sau khi vá) | ✓ thoát 0 · `V10983_TLS_HAI_TEN_OK` — hai tên đều 200, SAN phủ đủ, cổng 80 trỏ https |
| `curl` cả hai tên (`ssl_verify_result`) | ✓ `www=200 verify=0` · `nonwww=200 verify=0` |
| Hash 4 bảng khoá trước/sau | ✓ **giống hệt** cả bốn |
| PID `lottery` | ✓ 770947 → 770947 · `active` · `NRestarts=0` |
| `/api/health` | ✓ 200 (ngoài) · 200 (nội bộ `127.0.0.1:8000`) |
| `/api/admin/early-block` chưa đăng nhập | ✓ **401** |
| Panel `/monitoring` | ✓ khối *ĐÃ XONG — BLOCK* dòng 2012–2014; `loadEarlyBlock()` **nằm trong `setInterval` 60 giây** (khối dòng 8087) → không dính `§52B_VIOLATION_REFRESH_MISSING` |
| `certbot renew --dry-run --cert-name xs.io.vn` | ✓ *"Simulating renewal … for xs.io.vn **and www.xs.io.vn** → all simulated renewals succeeded"*; chứng chỉ thật **giữ nguyên sê-ri** sau lượt thử khô |
| `webroot_map` trong `/etc/letsencrypt/renewal/xs.io.vn.conf` | ✓ khai **cả hai tên** → gia hạn tự động (~03/10) không rơi mất `www` |
| ACME challenge cả hai tên | ✓ **200 / 200** — trang chuyển hướng mới không chắn |
| `certbot.timer` | ✓ sống, lượt kế **05/08 06:59** |
| `_v10920_decision_ledger.py` | ✓ **0 TRÔI** · `QD-023` 🟢 khớp **4/4** · toàn sổ 25 quyết định |
| `_v10982_kiem_lich9.py` | ✓ **8/8 phép đạt** (sau khi cập nhật mốc tải — xem mục 7) |
| `QD-014` | ✓ vẫn **15 model official**, không đụng 5 thứ bị cấm đích danh |
| Bundle 3 miền hôm nay | ✓ đủ 3, đều **trước hạn** |
| Quét khoá API / token trong `evidence/` | ✓ **0 khoá thật** (các khớp là `TOKEN_HERD` trong tên thí nghiệm và chuỗi `etc%2Fpasswd` do bot dò) |

## 7. Vướng vấp

**7.1 — Agent kết luận sai về cổng 80 trước khi đo (vấp do chính agent gây ra).** Ban đầu agent báo owner rằng *"trang đăng nhập chạy được cả trên HTTP thường nên bị chặn"*. **Sai.** Soi kỹ thì cổng 80 **không phục vụ trang đăng nhập** — nó là trang giữ chỗ Apache, và `/login` trên cổng 80 trả **404**. Agent đã suy diễn từ "cổng 80 mở" ra "cổng 80 phục vụ app" mà không gọi thử một endpoint nào. **Đã đính chính với owner ngay trong phiên.** *Hậu quả nếu bỏ qua:* hướng sửa sẽ thành "ép HTTPS cho trang đăng nhập trên cổng 80" — sửa một thứ không tồn tại, tốn một lượt deploy giữa khung ra số, mà bệnh thật (chứng chỉ thiếu `www`) vẫn nguyên.

**7.2 — Bản sao lưu nginx chép NHẦM FILE.** `/root/_v10983_backup/nginx_lottery.conf` có md5 `996b4b22…`, **bằng `sites-available/lottery`**, **KHÔNG bằng** file đang phục vụ thật là `sites-enabled/lottery` (md5 `d9f8f591…`). Hai file khác nhau đúng 2 dòng `add_header Cache-Control "no-store" always`. Nguyên nhân: `sites-enabled/lottery` là **file thường chứ không phải symlink** như thói quen Debian, nên `sites-available` đã trôi thành bản chết từ lâu mà không ai biết. *Hậu quả nếu bỏ qua:* ai đó gỡ về bằng cách `cp /root/_v10983_backup/nginx_lottery.conf /etc/nginx/sites-enabled/lottery` sẽ **âm thầm xoá hai dòng `no-store`** — endpoint admin bắt đầu bị cache, và lỗi kiểu đó rất khó truy vì cấu hình "trông vẫn đúng". Mục 8 đã ghi rõ **đừng chép đè**; `FU-263` xử gốc. May mắn duy nhất: phiên này **không sửa nginx.conf** (certbot expand giữ nguyên đường dẫn `live/`) nên không có gì phải khôi phục.

**7.3 — Mã đọc `DD0807` đụng mã đã dùng.** Đặt `FU-263 · DD0807` thì cổng `_v10982_kiem_lich9.py` phép **J6** trượt ngay: `FU-255` đã giữ `DD0807`. Đã đổi thành **`DD0807-1`** theo §58 (trùng loại+hạn thì thêm `-1`). *Hậu quả nếu bỏ qua:* hai mục khác nhau cùng mã đọc → mọi tham chiếu "DD0807" trong báo cáo về sau chỉ vào chỗ mơ hồ, đúng thứ §58 sinh ra để chặn.

**7.4 — Bảng mốc tải ghi cứng bị cũ ngay khi đóng/mở FU.** Phép **J5** trượt vì `TAI_PHIEN_KHAC_DO_DUOC` trong `_v10982_lich9.py` vẫn liệt `FU-260` ở 05/08 (đã đóng) và chưa có `FU-263` ở 07/08. Đã cập nhật, J5 đạt lại. *Hậu quả nếu bỏ qua:* mọi con số tải ngày trong `CHANGELOG`, trang lịch và báo cáo sẽ sai mà **không cổng nào bắt được** — đúng loại "xanh giả". Đây chính là kịch bản mà V10982b siết J5 để chặn, và lần này nó chặn thật.

**7.5 — Bốn dòng `conflicting server name` không ai để ý từ 26/07.** `nginx -t` in cảnh báo này mỗi lần chạy suốt 9 ngày. Vô hại hôm nay nhưng là dấu hiệu `sites-enabled/` bẩn. → `FU-263`.

**7.6 — Dòng MN trong `v10979_early_block` trễ 17.753 giây.** Không phải lỗi cron: V10979 vừa lên ~10:15 nên lượt chạy đầu sau deploy mới bù dòng MN của sáng (official chốt 05:19:56). MN nằm ngoài ngưỡng `FU-260` (chỉ đặt cho MT/MB). *Hậu quả nếu bỏ qua:* nếu không ghi lại thì ngày mai nhìn con số 17.753 giây sẽ tưởng cron MN hỏng. **05/08 là ngày đầu MN chạy trong khung cron thật (05:00–06:59)** — trễ >60 giây lần nữa thì mở thành lỗi riêng.

**7.7 — Cột trong hai bảng không đúng tên đoán.** `v10979_early_block` dùng `date` (không phải `ngay`), `du_doan_test_bundles` dùng `run_date` (không phải `date`), và bạch thủ ở `du_doan_test_bundles` tên là `test_bt`. Vòng truy vấn đầu trả `no such column`. Đã chạy `PRAGMA table_info` rồi truy vấn lại. *Hậu quả nếu bỏ qua:* câu truy vấn lỗi rất dễ bị đọc thành "bảng trống" → kết luận `FU-260` trượt và **gỡ cron oan**.

## 8. Gỡ về

**Nếu cần trả chứng chỉ về bản cũ** (chỉ khai `xs.io.vn`, hạn 23/09/2026) — **~1 phút**:

```bash
cd /etc/letsencrypt/live/xs.io.vn
ln -sf ../../archive/xs.io.vn/fullchain2.pem fullchain.pem
ln -sf ../../archive/xs.io.vn/cert2.pem      cert.pem
ln -sf ../../archive/xs.io.vn/chain2.pem     chain.pem
ln -sf ../../archive/xs.io.vn/privkey2.pem   privkey.pem
nginx -t && systemctl reload nginx
```

`fullchain2.pem` (5.635 byte, 25/06/2026) là **đúng chứng chỉ đang chạy trước phiên này**; `*3.pem` là bản mới. Không xoá bản mới — chỉ đổi symlink, đổi lại lúc nào cũng được.

**Nếu cần trả cổng 80 về trang giữ chỗ cũ** — **~10 giây**:

```bash
cp /root/_v10983_backup/apache_index.html /www/server/apache/htdocs/index.html
```

**⚠ KHÔNG được chép đè cấu hình nginx.** `/root/_v10983_backup/nginx_lottery.conf` là bản của `sites-available/lottery`, **khác file phục vụ thật** `sites-enabled/lottery` đúng 2 dòng `add_header Cache-Control "no-store" always` (mục 7.2). **Phiên này không sửa nginx.conf** nên không có gì phải khôi phục. Nếu buộc phải khôi phục thì lấy từ git/`sites-enabled` chứ đừng lấy bản sao lưu này.

**Trạng thái sau khi gỡ về:** quay lại đúng tình trạng owner báo lúc 16:34 — `www.xs.io.vn` gãy TLS, Kaspersky chặn điện thoại, cổng 80 là trang lạ. Tức **gỡ về là quay lại lỗi**, chỉ nên làm nếu chứng chỉ mới gây sự cố khác.

## 9. Theo dõi tiếp

### `FU-263` · `DD0807-1` · Dọn bản sao lưu nginx lẫn trong `sites-enabled` · **hạn 07/08**

- **Trạng thái:** `MEASURED_ROOT_CAUSE` · gắn `QD-023` · **không chạm vùng đóng băng `QD-014`**
- **Vấn đề:** `/etc/nginx/sites-enabled/` bật **cả hai** file — `lottery` (1.167 byte, md5 `d9f8f591…`) và `lottery.bak_pre_cache_20260726` (1.063 byte, md5 `996b4b22…`, để lẫn từ 26/07). Thêm vào đó `sites-enabled/lottery` **không phải symlink**, còn `sites-available/lottery` **trùng md5 với bản `.bak`** → là bản chết.
- **Ngưỡng hoàn thành (đo được bằng số):** `nginx -t` in **0 dòng** `conflicting server name` · `ls /etc/nginx/sites-enabled/` còn **1 file** · `sites-available/lottery` **md5 bằng** file phục vụ (hoặc `sites-enabled/lottery` là symlink trỏ về nó) · `https://xs.io.vn/login`, `https://www.xs.io.vn/login`, `/api/health` **đều 200** sau reload · header `Cache-Control: no-store` **còn nguyên** trên endpoint admin.
- **Ràng buộc:** làm **ngoài** khung ra số 15:30–18:15; sao lưu **cả hai** file ra **ngoài** `/etc/nginx/sites-enabled/` trước khi động (chính thói quen sao lưu tại chỗ đẻ ra mục này).
- **Ai quyết:** agent tự làm, không cần owner OK — không chạm 5 thứ `QD-014` cấm.

### `FU-252` · `KS0810-5` · hạn **10/08** — đang **3/21**

- **Ngưỡng:** **21/21** ô miền-ngày trong cửa sổ 04→10/08. Đêm 1/7 đạt 3/3.
- **Điều kiện hỏng:** thiếu **bất kỳ** đêm nào → cửa sổ sạch bắt đầu lại, kết luận trượt sang sau 10/08. Rủi ro thật, không giấu.
- **Cần nhìn nhất:** `MB_NGHIEMTHU_1908_V1` phải có dòng **7/7 đêm**.

### `FU-260` · `DP0805` — **ĐÓNG `CLOSED_PASS`**

Đạt cả hai ngưỡng (MT 47 giây, MB 9 giây, đều < 60). Không mở lại trừ khi tái phát. **Mốc phụ đặt cho 05/08:** MN chạy lần đầu trong khung cron thật (05:00–06:59) — nếu ghi block trễ **> 60 giây** so với lúc official MN chốt thì mở lỗi riêng (xem mục 7.6).

### `QD-023` · `KS2610` · **hạn rà soát 26/10/2026**

- **Ngưỡng:** chứng chỉ hết hạn **02/11/2026**; certbot gia hạn ở mốc 30 ngày trước (~**03/10**). Rà ngày 26/10: nếu SAN **không còn đủ hai tên**, hoặc `https://www.xs.io.vn/login` khác 200, hoặc cổng 80 thôi chuyển hướng → `QD-023` TRÔI, xử ngay.
- **Kiểm bằng một lệnh:** `python web/backend/_v10983_kiem_tls.py` (thoát 0 + in `V10983_TLS_HAI_TEN_OK`). Đã cắm thành mệnh đề máy kiểm trong sổ quyết định, nên `_v10920_decision_ledger.py` sẽ tự bắt.
- **Đã cắm vào playbook §2 mục 7** để mọi phiên kiểm định kỳ đều chạy — lớp tên miền trước V10983 **chưa ai canh**, và đó là lý do tất cả self-check đều xanh trong khi owner không vào được bằng điện thoại.

### `FU-262` — còn chờ owner nhìn tận mắt

Phía máy chủ đã kiểm: `monitoring.html` còn nguyên >8.100 dòng, `loadEarlyBlock()` và `loadSignalQualitySkip()` (điểm cắt cũ) đều nằm trong vòng `setInterval` 60 giây. **Còn thiếu:** owner mở `/monitoring` xác nhận trang tự đổi số sau 60 giây.
