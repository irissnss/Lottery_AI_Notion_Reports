# V10979 — XONG SỚM THÌ BÁO "ĐÃ XONG", KHÔNG NGỒI ĐỢI HẾT GIỜ HẠN

**Ngày:** 04/08/2026 · **Giờ:** 09:47 → 10:40 (giờ Việt Nam) · **Loại:** đào bới + sửa + deploy

---

## 1. Tóm tắt

Owner báo *"mốc thời gian không ổn"* và nhắc lại yêu cầu chạy **cuốn chiếu 5 model AI một lượt**,
kèm một vế mới: **output cuối cùng xong sớm thì thông báo đã xong và chốt luôn**.

Tra lại thì đây là **lần thứ TƯ** owner nói cùng một việc — 27/07 00:48, 31/07 10:53, và hôm nay;
bản thân owner ngày 27/07 còn ghi *"trước đó đã xác nhận"*, tức còn sớm hơn nữa. Lời ngày 31/07
chỉ được chép vào **docstring của một script đo** (`_v10889_timing_list.py`), **chưa bao giờ vào
sổ quyết định**, nên không cổng máy nào canh và owner phải nhắc lại.

Đo 30 ngày trên VPS cho ra hai kết luận tách bạch:

| vế owner nói | thực tế đo được |
|---|---|
| **Nhịp chạy** — verify xong mới dự đoán, cuốn chiếu 5 model AI một lượt | **ĐÚNG và ĐANG CHẠY THẬT.** `AI_PARALLEL_ENABLE=1`, `AI_PARALLEL_WORKERS=5`; **42/42 lượt trong 14 ngày** có dòng `[PARALLEL] BỂ 5 chỗ BẬT` trong log. MT chờ verify MN trung bình **1,5 phút**, MB chờ MT **0,3 phút**. |
| **Xong sớm thì báo "đã xong" và block** | **CHƯA TỪNG CÓ.** Grep 8 từ khoá trên toàn `web/backend/*.py` → **0 kết quả**. |

Output vốn **đã xong sớm hơn hạn 11–25 phút**, nhưng máy im lặng suốt khoảng đó nên mọi thứ phía
sau phải **hỏi theo lịch**. Lịch thì cố định, còn giờ official chốt **trôi gần 12 phút trong 30
ngày** — đó chính là nguyên nhân **03/08 lane Nghiệm Thu MB mất trắng một ngày đo**.

Đã dựng và deploy bộ báo **"ĐÃ XONG — BLOCK"** chạy mỗi phút, cộng 3 phép tự kiểm mới (18 → 21).
Trong lúc làm còn **bắt được một lỗi nặng hơn**: `/monitoring` bị **cắt cụt 53,5%** từ 03/08
19:21 và chạy hỏng suốt hai ngày mà không cổng nào biết — đã vá.

**Bốn bảng khoá giữ nguyên hash 100%. Không đụng một dòng nào của đường ra số (QD-014).**

---

## 2. Owner yêu cầu gì (nguyên văn)

> *"Mốc thời gian không ổn ah em. Hay Sao đó mà trễ outout block luôn anh đã nói sau khi vào đủ
> dữ liệu và verify tiến hành dự đoán cho đơn model , lần lượt cuốn chiếu với 5 model AI 1 lượt
> mà em. mốc MB chốt 17h58 , mốc miền T 16h58 output cuối cùng xong sớm thì thông báo đã xong
> block thôi em. Kiểm tra toàn diện hệ thóng đầu ngày dùm anh luôn em"*
> — 04/08/2026 09:47

### Ba lần trước, cũng nguyên văn

> *"trước đó đã xác nhận cho các model AI chạy theo nhóm 5 model 1 lượt cuốn chiếu hết model này
> đến model kia và sao anh có cảm giác vẫn muôn ah em. Xem kỹ dùm anh nha. Anh đang nghi hệ
> thống đang có vấn đề đang làm ảnh hưởng đến kết quả dự đoán đến total output ah em."*
> — 27/07/2026 00:48

> *"các model dự đoán của MT được khởi động chạy dự đoán sau khi cào và verify kết quả MN , MB
> được khởi động chạy dự đoán sau khi cào và verify kết quả MN , MT nên em ghi là 17h anh thấy
> có gì đó không đúng rồi. Và đối với các model đang chọn phương pháp chạy 5 model song song 1
> lượt cuốn chiếu tuần từ hết model này đến model kia, ưu tiên model được đánh giá xếp hạng tốt
> nhất trước nên kết quả dự đoán total ở các luồng muộn nhất cũng chỉ là 17h55 cho MB và 16h55
> cho miền T như thế mới kịp thời gian cho ngươi dùng… Tất cả show list ra để anh xem lại đi anh
> thấy không đúng , không ổn rồi đó nha."*
> — 31/07/2026 10:53

Câu *"trước đó đã xác nhận"* trong lời 27/07 cho thấy còn một lần sớm hơn nữa mà không tìm được
bản gốc trong transcript phiên hiện tại.

---

## 3. Đào bới / phát hiện

### 3.1 Tra trước khi làm (quy tắc §56/A54)

| tra ở đâu | kết quả |
|---|---|
| `docs/OWNER_DECISION_LEDGER.json` (21 quyết định) | **KHÔNG có mục nào** về nhịp chạy / cuốn chiếu / batch model / báo xong sớm |
| `docs/ACTIVE_ROADMAP_*.md` | không có checkpoint nào |
| `docs/FOLLOW_UP_TRACKER.md` | **FU-256** (biên giờ chốt MT/MB co lại, mở 03/08, hạn 06/08) và **FU-252** (canh lane Nghiệm Thu) có liên quan, nhưng **không mục nào** nói về nhịp chạy hay thông báo xong |
| transcript phiên (6.608 dòng) | tìm thấy **3 lần owner nói**, dòng 3514 · 5202 · 6603 |
| `docs/PLAYBOOK_PERIODIC_FULL_SYSTEM_CHECK.md` §1 | có bảng mốc FINAL, **không có** mục nào về nhịp chạy model |
| `docs/CO_CHE_DU_DOAN_TUNG_MIEN.md` · `docs/MOC_FINAL_TOTAL_OUTPUT.md` | ghi điều kiện khởi động (verify xong mới chạy) nhưng **không ghi** cuốn chiếu 5 model, **không ghi** báo xong sớm |

**Chỗ duy nhất giữ lời owner 31/07** là docstring của `web/backend/_v10889_timing_list.py`:

```
Owner 31/07 10:53 nêu đúng thiết kế của hệ:
  · MT chỉ khởi động dự đoán SAU khi cào và verify xong kết quả MN
  · MB chỉ khởi động SAU khi cào và verify xong MN và MT
  · Model chạy 5 con song song, cuốn chiếu, ưu tiên model xếp hạng tốt trước
  · Nên total muộn nhất phải là 16:55 cho MT và 17:55 cho MB
```

Một docstring **không phải là cổng kiểm**. Đó là lý do chính xác vì sao việc này trôi bốn lần.

### 3.2 Bể cuốn chiếu 5 chỗ — đo thật, không đoán

| bằng chứng | giá trị |
|---|---|
| `.env` trên VPS | `AI_PARALLEL_ENABLE=1` · `AI_PARALLEL_WORKERS=5` |
| `scheduler_logs` 14 ngày | **42/42 lượt** có `[PARALLEL] 🏊 BỂ 5 chỗ BẬT: start trước 5/7 model, hàng đợi 2` |
| khoảng cách ghi giữa 2 model | nhỏ nhất **0,0 giây**; **321–332 khoảng dưới 5 giây** mỗi miền / 30 ngày |
| điều kiện khởi động MT | verify MN xong → gọi model đầu: chờ TB **1,5 phút**, lâu nhất 1,9 |
| điều kiện khởi động MB | verify MT xong → gọi model đầu: chờ TB **0,3 phút** |

**Vế nhịp chạy owner mô tả là đúng và đang chạy.** Cơ chế do V10710 dựng (owner ký 10/06).

### 3.3 Biên trước hạn — 30 ngày, giờ Việt Nam

| miền | hạn | official chốt (sớm nhất → muộn nhất) | dư ít nhất | dư TB | ngày trễ hạn |
|---|---|---|---|---|---|
| MN | 15:45 | 04:17 → 05:20 | **624,6 phút** | 678,7 | 0/31 |
| MT | 16:58 | 16:37 → **16:47 (03/08)** | **10,8 phút** | 16,6 | 0/30 |
| MB | 17:58 | 17:33 → **17:44 (03/08)** | **13,1 phút** | 22,9 | 0/30 |

Khớp đúng con số FU-256 đã ghi ngày 03/08 (MT ~11 phút, MB ~14 phút). **Chưa ngày nào trễ hạn**,
nhưng biên đang co đều: MT từ 20,6 phút (22/07) xuống 10,8; MB từ 25,0 xuống 13,1.

### 3.4 Đường găng buổi chiều — MB 03/08

| giờ | +phút | model |
|---|---|---|
| 17:30:17 | 0,0 | 7 model ML (`rerun_post_mt`) — gần như tức thì |
| 17:31:14 | 1,0 | `claude-sonnet-4-6`, `gemini-2.5-flash` |
| 17:32:51 | 2,6 | `deepseek-reasoner`, `gemini-2.5-pro`, `gpt-5.4` |
| 17:35:31 | 5,2 | `gpt-oss-120b` |
| **17:41:56** | **11,7** | **`glm-5.1`** ← đường găng |
| 17:44:54 | 14,6 | `combo-super` (bắt buộc chạy sau cùng) |

Thời gian thật 30 ngày: `glm-5.1` TB **487,3s**, chậm nhất **795,7s**; `gpt-oss-120b` TB **369,3s**,
chậm nhất **885,7s**. Hai model này là toàn bộ đường găng.

**Tính bằng số, cuốn chiếu KHÔNG rút ngắn thêm được bao nhiêu nữa.** Bể 5 chỗ đã bật; `glm-5.1`
nằm thứ 7 trong danh sách nên khởi động trễ **~54 giây** so với nếu nó ở 5 chỗ đầu. Xếp lại thứ
tự chỉ tiết kiệm được **dưới 1 phút**, trong khi biên hiện có là 13 phút. **Không đáng đánh đổi
rủi ro chạm chuỗi official trong cửa sổ đóng băng** — nên không làm.

### 3.5 Thứ owner thật sự thiếu

Trước phiên này, tìm 8 từ khoá (`early_block`, `EARLY_BLOCK`, `da_xong_block`, `DA_XONG`,
`announce`, `output_done`, `OUTPUT_DONE`, `block_som`) trên toàn `web/backend/*.py`:
**0 kết quả**. Không có bất kỳ cơ chế thông báo "đã xong" nào.

Hậu quả đo được: **03/08 official MB chốt 17:44:54**, lượt cron cuối của lane Nghiệm Thu lúc đó
là **17:42:01** — sau **2 phút 53 giây** thì cổng `_official_gate` mới đủ điều kiện mở, mà đã
hết lượt. **MB mất trắng một ngày đo.** Cả 16 phép tự kiểm vẫn xanh.

### 3.6 "Xong" hiện vẫn chưa bằng "bất động"

Mọi ngày đã hoàn tất đều kết thúc ở `bundle_version >= 2`, tức bundle **có bị dựng lại** sau lần
tạo đầu (job T-chốt MT 16:55 · MB 17:55 — job này gọi `generate_final_bundle()`, tức **có quyền
đổi số**). FU-207 ghi nhận một lần dựng lại đã kéo `model_count` **15 → 14**.

Nghĩa là giữa lúc output xong (17:44) và mốc FINAL (17:58) vẫn còn **~13 phút** mà số có thể đổi.

### 3.7 Phát hiện ngoài dự kiến — `/monitoring` hỏng từ 03/08

| | |
|---|---|
| kích thước hiện tại | **262.144 byte = 2^18 = đúng 256 KiB** |
| kích thước bản trước (`a5902de`, 01/08) | **563.654 byte** |
| mất | **301.510 byte = 53,5%** |
| gây ra bởi | commit `9430141` (V10977), mtime **03/08 19:21:58** |
| hậu quả | mất `</script>` `</body>` `</html>`; mất vòng `setInterval(60s)`; còn **25/65** hàm nạp |

Chạy hỏng **suốt hai ngày**, 18 phép tự kiểm vẫn xanh — vì **không phép nào kiểm tính toàn vẹn
của file giao diện**. Đây cũng là lý do §52 ("panel làm mới 60 giây") **không thể đúng** trong
hai ngày qua.

---

## 4. Hướng xử lý và vì sao chọn

### Phương án đã cân nhắc

| # | phương án | quyết định |
|---|---|---|
| A | Xếp lại thứ tự bể 5 chỗ để `glm-5.1` chạy trước | **LOẠI.** Đo được chỉ tiết kiệm <1 phút trong khi biên còn 13 phút; đổi lại phải sửa chuỗi official ngay trong cửa sổ đóng băng. Không đáng. |
| B | Đóng băng sớm ngay khi xong + cho T-chốt bỏ lượt | **LOẠI (trong phiên này).** Đúng ý owner nhất nhưng **chạm thẳng writer `final_bundles`** — vùng QD-014 đóng băng tới hết 08/08. Rủi ro: dò "đủ" sai một nhịp là khoá sớm và **mất model thật** khỏi bundle, đúng loại lỗi đổi số công bố mà đóng băng sinh ra để chặn. → **FU-261 chờ owner**. |
| C | Nới rộng thêm lượt cron cho lane | **LOẠI.** V10977 đã làm hôm qua (thêm MB 17:46/17:50/17:54). Vẫn là hỏi-theo-lịch; giờ official chốt trôi 12 phút nên sớm muộn lại lệch. Chữa triệu chứng. |
| **D** | **Nghe theo SỰ KIỆN: xong là báo ngay + gọi luôn phần phía sau** | **CHỌN.** Đúng vế owner yêu cầu ("thông báo đã xong"), sửa đúng gốc (hỏi-theo-lịch → nghe-theo-sự-kiện), và **thuần cộng thêm** — không sửa một dòng nào của đường ra số. |

### Vì sao D an toàn trong cửa sổ đóng băng

Module mới **chỉ đọc** `final_bundles` và kho model, **ghi** vào bảng mới của riêng nó, và **gọi**
lane Nghiệm Thu (lane test, `output_eligible=0`, tự chống ghi đè). Nó **không** đổi 15 model
official, **không** đổi bộ lọc combo-super, **không** bật/tắt lớp ghi đè, **không** chạm
`/du-doan`, **không** chạm writer `final_bundles`, **không** chạm bộ chọn model production.
Bằng chứng: hash 4 bảng khoá trước/sau deploy **giống hệt nhau**.

Một rào chắn quan trọng đã cài: **không bao giờ gọi lane sau mốc FINAL của miền đó** — nếu không
thì chính module này lại đẻ ra số bù sau hạn, đúng thứ OD-20260803-B cấm.

---

## 5. Đã làm gì

### File × thay đổi

| file | thay đổi |
|---|---|
| `web/backend/_v10979_early_block.py` | **MỚI (16.885 B)** — mỗi phút dò từng miền; đủ điều kiện xong thì ghi `DA_XONG_BLOCK` vào bảng `v10979_early_block` và **gọi ngay** lane Nghiệm Thu. Có rào chắn không gọi lane sau mốc FINAL. |
| `web/backend/_v10900_consistency_guard.py` | **18 → 21 phép.** `C19_bien_han_du_rong` (biên ≥480s) · `C20_bien_han_khong_troi` (không 3 ngày liên tiếp <720s) · `C21_co_thong_bao_da_xong` |
| `web/backend/main.py` | **+** `GET /api/admin/early-block` (`require_admin`, `Cache-Control: no-store`) |
| `web/frontend/monitoring.html` | **vá cắt cụt 262.144 → 563.654 B**, rồi **+** panel `ĐÃ XONG — BLOCK`, đăng ký trong `init()` **và** vòng `setInterval(60s)` → **569.778 B** |
| crontab VPS | **+3 dòng** `_v10979_early_block.py` mỗi phút: `* 5-6` MN · `* 16` MT · `* 17` MB |
| `docs/OWNER_DECISION_LEDGER.json` | **+ QD-020** với **8 mệnh đề máy kiểm** |
| `CHANGELOG.md` · `docs/CURRENT_TRUTH_SSOT.md` · `docs/FOLLOW_UP_TRACKER.md` | ghép khối V10979 bằng `_doc_prepend.prepend()` |
| `docs/PLAYBOOK_PERIODIC_FULL_SYSTEM_CHECK.md` | §1 +3 gạch đầu dòng · §5 +5 dòng lịch |

### C19/C20 chính là ngưỡng FU-256 tự viết

FU-256 (mở 03/08) tự đặt ngưỡng: *"nếu MT hoặc MB còn < 8 phút trước hạn, hoặc 3 ngày liên tiếp
< 12 phút → báo đỏ"*, hạn dựng **06/08**. Nay dựng xong **sớm 2 ngày**, đúng con số đó.

### Cách vá `/monitoring`

Không dùng `git checkout` bản cũ được: bản 03/08 **không phải tiền tố thuần** của bản 01/08 —
byte khác nhau đầu tiên ở **71198**, tức có sửa thật trước điểm cắt, lấy nguyên bản cũ đè lên là
mất những sửa đó. Đã vá bằng cách **giữ nguyên toàn bộ phần còn sống** rồi nối lại phần đuôi đã
mất, dùng **400 byte cuối làm mỏ neo** (kiểm trước: mỏ neo xuất hiện **đúng 1 lần** trong bản
đầy đủ; nếu không duy nhất thì script tự dừng). Cổng kiểm sau khi nối: có đủ ba thẻ đóng · kết
thúc bằng `</html>` · phần đang chạy không bị đổi một byte nào · kết quả không ngắn đi.

### Backup

- Local: `backups/v10979_pre/` — `_v10900_consistency_guard.py.pre` · `main.py.pre` ·
  `monitoring.html.cut_20260804_100331` (đúng bản cụt đang chạy trước khi vá)
- VPS: `/root/Lottery_AI_Test/backups/v10979_pre_20260804_101509/`

### Deploy

| | |
|---|---|
| giờ | 04/08 10:15 và 10:22 giờ VN — **ngoài khung cấm** (05:00–06:30 · 15:30–18:15) |
| PID | **738032 → 770722 → 770947** — đổi thật cả hai lần |
| service | `lottery` (không phải `lottery-ai`) · `active` |
| smoke | `/api/health` = **200** · `/api/admin/early-block` = **401** (đúng, admin-only) |

---

## 6. Cổng kiểm

| kiểm gì | kết quả |
|---|---|
| `py_compile` local + VPS (3 file .py) | **COMPILE_OK** cả hai |
| Hash 4 bảng khoá trước/sau deploy | **GIỐNG HỆT** — `predictions` 11.673 `2c5fca45…` · `final_bundles` 472 `d95dc3e6…` · `lottery_results` 15.207 `924fd080…` · `model_daily_eval` 11.496 `f6e52dc7…` |
| PID trước/sau restart | 738032 → 770947 · **đã đổi** |
| `/api/health` | **200** |
| `/api/admin/early-block` chưa đăng nhập | **401** |
| Bộ tự kiểm nhất quán | **21 phép · lệch 0** (C19/C20/C21 đều OK) |
| Sổ quyết định `_v10920_decision_ledger.py` | **QD-020 khớp 8/8** · toàn sổ **0 TRÔI** · exit 0 |
| Bộ dò chạy thật hôm nay | MN `DA_XONG_BLOCK` chốt 05:19:56, sớm hơn hạn **625 phút**; MT/MB đúng `CHUA_CHOT` |
| Bộ dò chạy lại 03/08 | MT sớm **650s** (10,8 phút) · MB sớm **786s** (13,1 phút) — khớp đúng số đo độc lập |
| Chống báo nhầm | ngày chưa có bundle (`2099-01-01`) → `CHUA_CHOT`, `xong=False` |
| `monitoring.html` trên VPS | **569.778 B** · có `</html>` · **66** hàm nạp · `loadEarlyBlock` **3** lần (định nghĩa + `init()` + `setInterval`) |
| cron | **3 dòng** V10979 có mặt |

---

## 7. Vướng vấp

**7.1 — Suýt báo cáo số sai vì bẫy múi giờ.** Lần đo đầu dùng `time(p.created_at)` của SQLite và
ra kết quả vô lý: MB "chuỗi chạy 10:30, bundle chốt 18:31", mọi miền đều "trễ hạn 30–50 phút".
Nguyên nhân: `predictions.created_at` lưu **ISO có đuôi múi giờ** (`2026-08-03T17:30:17+07:00`),
mà `time()` gặp đuôi đó thì **tự quy về UTC** — lệch đúng 7 tiếng. Phải dùng
`substr(created_at, 12, 8)`. Nếu không bắt kịp thì cả báo cáo này sai từ gốc.
**Đáng lưu ý:** script cũ `_v10935_slack.py` dùng đúng công thức sai đó — mọi kết luận về "dư bao
nhiêu phút" từ script ấy đều lệch 7 tiếng.

**7.2 — Chọn nhầm cột làm mốc chốt.** Ban đầu lấy `final_bundles.updated_at`. Cột này bị job
chấm điểm sau khi xổ sờ vào (MB `18:31:02` = đúng giây cào kết quả). Mốc chốt thật là
`created_at`.

**7.3 — Mệnh đề máy kiểm viết bằng builtin, TRÔI hết.** Bốn phép đầu tiên viết bằng
`__import__(...)`, `open(...)`, `any(...)`. Bộ kiểm chạy
`eval(bieu_thuc, {"__builtins__": {}}, vars(module))` — **không có builtins nào**. Đã viết lại
chỉ dùng tên có sẵn trong module, và đổi từ "so hằng số với chính nó" sang **chạy thật trên dữ
liệu thật** (dò lại 03/08 MB phải ra đúng 786 giây).
*(Đúng loại vấp mà V10977 đã ghi lại ngày 03/08 — vẫn lặp lại.)*

**7.4 — Thiếu khoá `trang_thai` làm hỏng bộ sinh tài liệu.** Mục QD-020 ghi lần đầu thiếu khoá
này, `sinh_md()` ném `KeyError` và **không sinh được bản đọc cho người** — bản `.md` sẽ đứng
im ở nội dung cũ mà vẫn trông như vừa cập nhật.

**7.5 — Đâm số hiệu FU với phiên chạy song song.** Phiên V10980 (kiểm toàn diện đầu ngày) chiếm
**FU-258** và **FU-259** trước. §58 cấm hai việc dùng chung số FU. Đã dời sang **FU-260/261/262**
và sửa lại những chỗ đã ghi nhầm trong CHANGELOG và sổ quyết định. Phép kiểm "đã ghi chưa" của
tôi cũng báo nhầm vì tìm chuỗi `"V10979"` trơn — mà khối của phiên V10980 có nhắc tên V10979.
Đã đổi sang mốc nhận dạng riêng.

**7.6 — Một lượt đo tay suýt bịt mất lượt thật.** Bản đầu chỉ cần thấy `DA_XONG_BLOCK` là bỏ
qua. Nghĩa là một lượt chạy `--no-lane` (chỉ đo, không gọi lane) sẽ ghi trạng thái cuối và
**chặn luôn lượt cron thật sau đó** — mất đúng việc module sinh ra để làm. Bắt được khi chạy
kiểm sau deploy, đã sửa và deploy lại.

**7.7 — Rào chắn thiếu, suýt tự vi phạm quy tắc đóng băng.** Cron MB chạy cả giờ 17; nếu official
chốt muộn thì lượt cron sau 17:58 sẽ gọi lane và **sinh số bù sau mốc FINAL** — đúng thứ
OD-20260803-B cấm. Đã thêm `_con_kip_goi_lane()`: quá mốc FINAL thì ghi rõ "KHÔNG gọi lane" thay
vì gọi.

**7.8 — `/monitoring` hỏng hai ngày mà 18 phép tự kiểm vẫn xanh.** Xem mục 3.7. Đây là vấp
nghiêm trọng nhất tìm được hôm nay, và **không phải do phiên này gây ra**. Hậu quả nếu bỏ qua:
mọi panel đo lường dựng trong hai ngày qua đều không thật sự làm mới, và §52 bị vi phạm âm thầm.

---

## 8. Gỡ về

```bash
# 1. gỡ 3 dòng cron báo xong
ssh root@14.225.224.89 "crontab -l | grep -v _v10979_early_block | crontab -"

# 2. khôi phục 3 file trên VPS (bản sao lưu tạo lúc deploy)
ssh root@14.225.224.89 "cd /root/Lottery_AI_Test/backups/v10979_pre_20260804_101509 && \
  cp -p _v10900_consistency_guard.py main.py /root/Lottery_AI_Test/web/backend/ && \
  cp -p monitoring.html /root/Lottery_AI_Test/web/frontend/ && \
  systemctl restart lottery"

# 3. xoá module mới (không bắt buộc — không ai gọi nó nữa sau khi gỡ cron)
ssh root@14.225.224.89 "rm -f /root/Lottery_AI_Test/web/backend/_v10979_early_block.py"
```

Bản sao lưu local: `backups/v10979_pre/`. **Lưu ý:** `monitoring.html` trong bản sao lưu VPS là
**bản CỤT 262.144 byte** — khôi phục nó là quay lại trang hỏng. Muốn giữ bản đã vá mà chỉ bỏ
panel mới thì dùng `backups/v10979_pre/monitoring.html.repaired_pre_panel` (563.654 byte).

Mất khoảng **2 phút**. Bảng `v10979_early_block` chỉ chứa dữ liệu chẩn đoán
(`diagnostic_only=1`, `shadow_only=1`, `output_eligible=0`, `owner_approved=0`), để lại vô hại.

---

## 9. Theo dõi tiếp

| mã | mã đọc | việc | hạn | ngưỡng hành động bằng số |
|---|---|---|---|---|
| **FU-260** | DP0805 | Canh live thông báo "đã xong" chiều nay | 05/08 | Khi `final_bundles` có dòng cho MT/MB thì trong **≤60 giây** phải có `DA_XONG_BLOCK`. Tới **16:58** (MT) / **17:58** (MB) mà vẫn chưa có → **gỡ 3 dòng cron ngay trong tối** |
| **FU-261** | QD0809 | "Xong" phải bằng "bất động" — chờ owner | 09/08 | Trình owner ngay sau 08/08. OK → làm trong phiên riêng có canh live cả ba miền. Không OK → đóng mục |
| **FU-262** | SC0805 | Thêm phép kiểm toàn vẹn file giao diện | 05/08 | Đủ thẻ đóng · kích thước không tụt **>10%** so với lần trước. Không dựng được → escalate |
| **FU-256** | DO0806 | Biên giờ chốt MT/MB co lại — **đã dựng cổng** | 06/08 | C19 <**8 phút** → đỏ · C20 **3 ngày liên tiếp <12 phút** → đỏ. Nền 03/08: MT 10,8 · MB 13,1 |
| **FU-252** | KS1008 | Canh lane Nghiệm Thu ra số đủ 3 miền | 10/08 | không đổi — nay được V10979 hỗ trợ bằng cách gọi lane theo sự kiện |

### Chiều nay phải nhìn gì

1. **16:37–16:47** — MT chốt → panel `ĐÃ XONG — BLOCK` phải hiện MT xanh, kèm `lane_ket_qua`.
2. **17:33–17:44** — MB tương tự. Đây là ngày kiểm chứng: hôm qua chính khung này làm mất ngày đo.
3. **18:05** — bộ tự kiểm phải ra **21/21**, C19/C20/C21 xanh.
4. Trang `/monitoring` phải **tự làm mới sau 60 giây** — lần đầu vòng này chạy lại sau khi vá.

---

**Phiên chạy song song:** V10980 (kiểm toàn diện đầu ngày) chạy cùng lúc, chiếm FU-258/259.
Báo cáo này dùng FU-260/261/262. Hai phiên không đụng cùng file runtime nào.
