# GÓI DUYỆT OWNER — sửa hai lỗi ghi chép lịch sử `final_bundles`

**V11169 · CÔNG 3 · 2026-09-06 · phiên chỉ SOẠN, KHÔNG CHẠY gì trên DB**

Phiên này chạy dưới luật cứng: DB production **read-only** (chỉ SELECT), cấm mọi
INSERT/UPDATE/DELETE/CREATE/ALTER/DROP, cấm deploy/restart/sửa `web/backend`, cấm git
commit/push. Mọi câu lệnh SQL trong tài liệu này **CHƯA được chạy** — chúng nằm ở đây để owner
đọc, chọn phương án, rồi một phiên **có quyền ghi DB** mới thực thi.

---

## Cách đọc tài liệu này

Mỗi mục (A, B) có đúng ba câu hỏi owner cần trả lời:

1. **Nếu DUYỆT thì chạy lệnh nào** — SQL chính xác, số dòng bị chạm, việc cần làm trước khi chạy.
2. **Nếu TỪ CHỐI (giữ nguyên) thì hậu quả là gì** — rủi ro cụ thể nếu không sửa.
3. **Cách gỡ về** — nếu chạy rồi mà owner đổi ý, lệnh nào đưa dữ liệu về nguyên trạng.

Owner chỉ cần trả lời bằng một trong ba: **DUYỆT phương án X** / **TỪ CHỐI, giữ nguyên** /
**hỏi thêm**.

---

## Nguồn dữ liệu & cách tái lập (bắt buộc theo RM-11)

Mọi con số dưới đây tính lại từ **`artifacts/v11166_s7_fact.json`** — bản dump **DB production
qua kết nối read-only** (`sqlite3.connect("file:...lottery_ai.db?mode=ro", uri=True)`) ngày
05/09/2026, script nguồn `_s7g_fact.py`, đọc đúng quy tắc của hàm **đang serve**:

| quy tắc | tại đâu |
|---|---|
| `bach_thu_status = WIN` nếu `bach_thu` ∈ `tails_set` | `database.py:4849`, gọi qua `main.py:6574` |
| `lo3_status = WIN` nếu `lo3` khớp **ĐỦ 3 chữ số** với đuôi giải | `database.py:4886` (hàm `verify_final_bundle`, dòng bắt đầu `database.py:4812`) |
| `lo2_status` | `database.py:4857` |

Script tính lại của phiên này (đọc lại `v11166_s7_fact.json`, **không** kết nối lại VPS, **không**
ghi gì) đính kèm cùng packet này ở `evidence/`:
`_w3_compute.py` (Mục A + B, danh sách 91 & 32 dòng) · `_w3_compute2.py` (trước/sau theo miền) ·
`_w3_check_notes.py` (đối chiếu cột `notes`, **CÓ** kết nối VPS, **chỉ SELECT**).

Kiểm chéo với số đã công bố trước đó (V11166, `evidence/GATE_s2-ngay-live.md`): backfill lệch
nền bạch thủ tính lại ra **đúng +9,80pp** — khớp con số đã công bố «+9,8pp trên nền» → xác nhận
phương pháp đúng, không phải trùng hợp.

---

# MỤC A — 91 bundle "backfill" nằm chung bảng với dữ liệu LIVE

## A.1 · Bằng chứng — đây là backfill, không phải suy đoán

**Định nghĩa dùng để phát hiện:** `created_at` của bundle **muộn hơn** thời điểm kết quả xổ số
đầu tiên của đúng (ngày, miền) đó đã có trong `lottery_results` (`MIN(created_at)`). Một bundle
"sinh ra" sau khi đã biết kết quả không thể là một dự đoán thật.

- **Tổng: 91 bundle** — MN 30 · MT 31 · MB 30
- **Khoảng ngày bị backfill:** 2026-02-28 → 2026-03-30 (31 ngày liên tiếp, đúng 3 miền/ngày trừ vài ngày lẻ)
- **90/91 dòng ghi `created_at` = `2026-03-30 13:42:14 / :15 / :16`** (chênh nhau 1-2 giây — một
  lượt chạy script duy nhất). Dòng còn lại (**id=93**, MT 2026-03-30) có `created_at =
  2026-03-30 17:53:42` và cột `notes = 'Admin manual trigger'` — tức bundle ngày cuối cùng của
  đợt (30/03) được một tay admin tạo lại **sau khi** kết quả MT ngày đó đã về (17:38:01), nên vẫn
  tính là backfill theo đúng định nghĩa thời gian, dù không cùng đợt script.
- **Script nguồn:** `web/backend/_backfill_bundles.py` — tự khai ngay ở docstring dòng 2-14:
  *"V16 Phase 1.5 — 30-Day Backfill Script … Uses CURRENT model WR weights (not historical
  snapshots) … Lo3 verify = simplified 2-digit tail check (Phase 1 trial limitation)"*. File này
  **không được import bởi bất kỳ file `.py` nào khác**, **không có trong crontab** hiện tại (đã
  kiểm bằng `crontab -l` trên VPS, phiên này) → đây là kịch bản **chạy một lần, không còn chạy
  lại**, không phải lỗi đang tiếp diễn.
- **90/91 dòng còn nguyên `notes = 'Phase 1.5 backfill'`** trong DB **tính đến hôm nay**
  (kiểm read-only trực tiếp trên VPS, phiên này) — bundle không bị ghi đè từ 30/03 tới nay, nhờ
  cơ chế **V17.1 FREEZE GUARD** (`database.py: save_final_bundle`) chặn overwrite mọi bundle đã
  có `verified_at` trừ khi gọi với `force=True`.

## A.2 · Trước/sau theo TỪNG miền — bốn thước (bạch thủ, lô2, lô3, top-10)

*"TRƯỚC" = hiện trạng (gộp cả 91 backfill, không lọc). "SAU" = loại 91 backfill, chỉ còn 479
bundle LIVE thật. Nền bạch thủ = trung bình `D2/100` (xác suất một số cố định trúng 1 trong D2
đuôi-2-số thật xuất hiện ngày đó) — công thức khớp với con số nền 34,0% đã công bố trước đây.*

| miền | | n bundle | bạch thủ (đã cham lại, đều khớp nhãn lưu) | nền bạch thủ | lô3 (nhãn lưu vs thật) | lô2 WIN | top-10 (số ô / trúng) |
|---|---|---|---|---|---|---|---|
| **MN** | TRƯỚC | 190 | 42,11% | 43,07% | 12,11% vs **6,84%** | 15,26% | 1810 / 791 = 43,70% |
| | SAU | 160 | 42,50% | 43,09% | 6,88% (khớp) | 13,75% | 1530 / 680 = 44,44% |
| **MT** | TRƯỚC | 190 | 37,37% | 35,17% | 10,00% vs **3,68%** | 14,74% | 1760 / 643 = 36,53% |
| | SAU | 159 | 34,59% | 35,13% | 2,52% (khớp) | 14,47% | 1450 / 524 = 36,14% |
| **MB** | TRƯỚC | 190 | 21,58% | 23,76% | 7,89% vs **2,63%** | 4,21% | 1820 / 423 = 23,24% |
| | SAU | 160 | 18,12% | 23,71% | 1,88% (khớp) | 5,00% | 1540 / 356 = 23,12% |
| **GỘP 3 MIỀN** | TRƯỚC | 570 | 33,68% | 34,00% | 10,00% vs **4,39%** | 11,40% | 5390 / 1857 = 34,45% |
| | SAU | 479 | 31,73% | 33,97% | 3,76% (khớp) | 11,06% | 4520 / 1560 = 34,51% |

**Đọc bảng:** cột **bạch thủ** và **lô2** *không* đổi khi lọc — nhãn lưu đã khớp 100% với tính
lại (writer của hai thước này không có lỗi). Cột **lô3** đổi mạnh vì đây chính là 32 nhãn sai của
Mục B (tất cả nằm trong 91 backfill) — số bên phải dấu "vs" là con số **thật**. Riêng bạch thủ
BACKFILL-ONLY đạt **43,96%** so nền **34,15%** (chênh **+9,80pp** — khớp con số đã công bố),
trong khi LIVE-ONLY (SAU) đạt 31,73% dưới nền 33,97% (**-2,24pp**) ở mức gộp 3 miền — tức backfill
đang **kéo trung bình toàn lịch sử lên**, làm accuracy trông tốt hơn thật.

## A.3 · Ba phương án đánh dấu — KHÔNG XOÁ dữ liệu

### Phương án 1 — Dùng cột `notes` sẵn có (không ghi DB nào cả)

```sql
-- Chỉ ĐỌC, dùng ngay hôm nay, không cần owner duyệt ghi gì:
SELECT * FROM final_bundles WHERE notes LIKE '%backfill%';
```
- **Số dòng bị chạm:** 0 (không ghi gì).
- **Độ đầy đủ:** bắt được **90/91** — thiếu đúng **id=93** (notes bị đổi thành
  `'Admin manual trigger'` khi tạo lại lúc 17:53:42).
- **Rủi ro:** THẤP nhưng **KHÔNG ĐẦY ĐỦ** — mọi script lọc theo cách này sẽ lẫn 1 bundle backfill
  vào phần "LIVE". Ngoài ra cột `notes` từng bị ghi đè trong quá khứ (ON CONFLICT DO UPDATE SET
  `notes = excluded.notes` — `database.py`) nên **không đảm bảo bền theo thời gian** nếu sau này
  có `force=True` overwrite (hiện bị FREEZE GUARD chặn, nhưng đó là chặn ở tầng code, không phải
  ràng buộc DB).
- **Gỡ về:** không áp dụng — không có gì để gỡ.

### Phương án 2 — Thêm cột `is_backfill` vào `final_bundles` (khuyến nghị nếu owner muốn 1 cột đơn giản)

```sql
-- Bước 1: backup file DB trước khi ALTER (bắt buộc theo CLAUDE.md — "Backup trước khi sửa")
-- Bước 2:
ALTER TABLE final_bundles ADD COLUMN is_backfill INTEGER DEFAULT 0;

-- Bước 3: gắn cờ đúng 91 dòng đã xác minh (danh sách đầy đủ ở Phụ lục A)
UPDATE final_bundles SET is_backfill = 1
WHERE (id BETWEEN 2 AND 91) OR id = 93;
```
- **Số dòng bị chạm:** ALTER không đổi dữ liệu hàng nào (mọi dòng cũ nhận mặc định 0);
  UPDATE chạm đúng **91 dòng**.
- **Độ đầy đủ:** 91/91 — chính xác, không phụ thuộc `notes`.
- **Rủi ro:** TRUNG BÌNH — đụng `ALTER TABLE` trên bảng production đang được `main.py` và
  `scheduler.py` ghi/đọc mỗi ngày. SQLite `ADD COLUMN` là thao tác an toàn/atomic tự thân, nhưng
  **phải quét trước** mọi chỗ dùng `SELECT *` rồi unpack theo vị trí cột (không theo tên) — thêm
  cột mới sẽ làm lệch vị trí. Chưa quét trong phiên này (ngoài phạm vi CONG 3; cần một phiên khác
  quét `SELECT *.*final_bundles` + unpack theo index trước khi chạy ALTER).
- **Gỡ về:**
  ```sql
  -- Bỏ cờ (giữ cột, coi như quay lại trạng thái "chưa đánh dấu")
  UPDATE final_bundles SET is_backfill = 0 WHERE (id BETWEEN 2 AND 91) OR id = 93;
  -- Gỡ hẳn cột (chỉ chạy được nếu SQLite server ≥ 3.35.0, kiểm bằng `sqlite3 --version` trước):
  ALTER TABLE final_bundles DROP COLUMN is_backfill;
  -- Nếu SQLite cũ hơn 3.35: không DROP COLUMN được — phải khôi phục từ bản backup file đã chụp ở Bước 1.
  ```

### Phương án 3 — Bảng phụ riêng, KHÔNG đụng `final_bundles` (an toàn nhất, khuyến nghị chính)

```sql
CREATE TABLE IF NOT EXISTS data_quality_flags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bundle_id INTEGER NOT NULL,
    flag_type TEXT NOT NULL,
    reason TEXT,
    tagged_at TEXT DEFAULT (datetime('now','localtime')),
    tagged_by TEXT
);

INSERT INTO data_quality_flags (bundle_id, flag_type, reason, tagged_by)
SELECT id, 'BACKFILL_HISTORICAL',
       'created_at sau khi ket qua da ve; _backfill_bundles.py chay 2026-03-30 13:42-17:53; ' ||
       'khong con trong crontab, khong con file nao import',
       'V11169_CONG3'
FROM final_bundles WHERE (id BETWEEN 2 AND 91) OR id = 93;
```
- **Số dòng bị chạm:** **0 dòng** trong `final_bundles` (bảng gốc tuyệt đối không đổi);
  **91 dòng mới** trong bảng mới `data_quality_flags`.
- **Độ đầy đủ:** 91/91, và bảng này **dùng chung được cho cả Mục B** (chỉ cần `flag_type` khác)
  — một cơ chế cho cả hai vấn đề, không phải hai giải pháp rời.
- **Rủi ro:** THẤP NHẤT về phía `final_bundles` — không `ALTER`, không đổi hành vi
  `SELECT *`/vị trí cột của bảng đang chạy sản xuất. Đánh đổi: mọi script muốn lọc backfill phải
  thêm một `LEFT JOIN`/`NOT IN (SELECT bundle_id ...)`, tức cần sửa từng script báo cáo đang gộp
  "180 ngày"/"toàn lịch sử" — việc này chưa làm trong phiên này (ngoài phạm vi CONG 3), nhưng
  **hiện KHÔNG có API/UI production nào lộ số gộp lô3 ra ngoài** (xem A.4), nên rủi ro người dùng
  thấy số sai ngay bây giờ là thấp; rủi ro nằm ở các script phân tích nội bộ tương lai.
- **Gỡ về:** `DROP TABLE data_quality_flags;` — hoàn toàn không để lại dấu vết trên bảng gốc.

## A.4 · Phạm vi hiển thị hiện tại (để owner cân nhắc mức khẩn)

- API lịch sử bundle công khai (`main.py:11255`, hàm phục vụ UI) **clamp cứng `limit` về tối đa
  30 dòng** — 91 bundle backfill (tháng 02-03/2026) **không nằm trong tầm nhìn** của UI hiện tại
  (ngày hôm nay 06/09, 30 dòng gần nhất chỉ tới khoảng đầu/giữa tháng 8). Không có bảng
  tổng-hợp/cache nào khác trong `database.py` lưu tỉ lệ thắng gộp toàn lịch sử.
- **Kết luận mức khẩn:** đây là lỗi **về SỔ SÁCH/PHÂN TÍCH nội bộ**, chưa chứng minh được đang
  làm sai lệch bất kỳ con số nào người dùng cuối nhìn thấy hôm nay. Vẫn cần sửa vì mọi phép đo
  "accuracy toàn lịch sử" nội bộ (kể cả các báo cáo V11116/V11164/V11166 đã dùng) đang bị nhiễm.

## A.5 · Nếu TỪ CHỐI (giữ nguyên, không đánh dấu gì)

- Mọi phép đo accuracy sau này lấy `SELECT * FROM final_bundles` mà **không tự nhớ** trừ 91 dòng
  sẽ tiếp tục báo bạch thủ toàn lịch sử **cao hơn thật khoảng +0,3 đến +2pp tuỳ miền** (xem bảng
  A.2), và báo lô3 cao hơn thật gấp **2,28 lần** (do trùng với lỗi Mục B).
- Không có cơ chế máy nào nhắc agent tương lai "nhớ trừ 91 dòng" — mỗi lần đo phải tự nhớ lại
  bằng tay, dễ quên (đã quên ít nhất tới khi V11166 phát hiện, tức từ 30/03 đến 05/09 = 159 ngày).

---

# MỤC B — 32 nhãn `lo3_status = WIN` trong DB là SAI

> **Vạch chú `PRJ-SELECTION-WINDOW-001` — các con số trong MỤC A và MỤC B KHÔNG PHẢI tuyên bố
> hiệu quả.** «+0,3 đến +2pp», «2,28 lần», «57 WIN → 25 WIN thật» đều là số về **tính toàn vẹn
> của sổ sách**, đo trên **TOÀN BỘ lịch sử có kết quả (570 bundle)** — không cắt cửa sổ nào, nên
> **không có cửa sổ để chọn**. Chúng nói *nhãn đã lưu sai bao nhiêu*, **không** nói *mô hình đoán
> tốt hơn nền bao nhiêu*.
>
> Câu hỏi hiệu quả — «bạch thủ có hơn nền không», «bộ lô2/lô3 có hơn nền `1−(1−b)^k` không» —
> đã đo riêng ở V11084 · V11086 · V11164 với **đủ bộ cửa sổ** 14 / 30 / 90 / 180 ngày, và ở đó
> **dấu ĐỔI theo cửa sổ** (30 ngày +4,07pp · 90 ngày −3,18pp · 180 ngày +0,91pp). **CẤM trích**
> riêng một cửa sổ từ những con số đó. Gói này **không** dùng chúng làm căn cứ duyệt.
>
> Ngược lại: chính vì 32 nhãn sai và 91 dòng backfill còn nằm trong sổ mà **mọi** phép đo hiệu quả
> trước đây đều đang chạy trên nền dữ liệu nhiễm. Sửa hai mục này là **điều kiện cần** để các phép
> đo đủ bộ cửa sổ sau này có nghĩa — không phải bằng chứng rằng dự đoán tốt lên.


## B.1 · Bằng chứng — danh sách đầy đủ 32 dòng

Cách phát hiện: chấm lại **đúng quy tắc của hàm đang serve** (`database.py:4886`, đối chiếu 3
chữ số đầy đủ) trên toàn bộ 570 bundle có kết quả, so với `lo3_status` đã lưu.

- Tổng dòng có `lo3` + có kết quả: **570**. Nhãn lưu ghi **57 WIN**; chấm lại đúng quy tắc hiện
  hành ra **25 WIN thật**. Chênh **32 dòng**, tỉ lệ phóng đại **57 / 25 = 2,28 lần**.
- **CẢ 32/32 dòng đều nằm trong 91 bundle backfill của Mục A** (không dòng nào ngoài backfill bị
  sai) — xem cột `la_backfill` trong bảng dưới.
- **CẢ 32/32 dòng đều có đặc điểm giống hệt nhau:** `lo3[-2:] == bach_thu` — tức nhãn WIN được
  gán vì **2 chữ số cuối của lô3 trùng với bạch thủ**, đúng y hệt lỗi mà chính code hiện tại ghi
  chú lại: *"Old bug: lo3='446' → tail='46' → matched BT=46 → false WIN"* (`database.py:4870`,
  comment ngay trên logic `V16.1 FIX`).

> `PRJ-SELECTION-WINDOW-001`: bảng dưới là **32/32 dòng, không lấy mẫu, không cắt cửa sổ** —
> nó đo **nhãn sai**, không đo hiệu quả. Số hiệu quả có **đủ bộ cửa sổ** ở V11084/V11086;
> **CẤM trích** một cửa sổ từ đó rồi ghép vào gói này.

| id | ngày | miền | bạch thủ | lô3 | nhãn đã lưu | thật (đúng quy tắc đang serve) | lô3[-2:] == bạch thủ? |
|---|---|---|---|---|---|---|---|
| 5 | 2026-03-01 | MN | 71 | 571 | WIN | LOSE | CÓ |
| 6 | 2026-03-01 | MT | 09 | 909 | WIN | LOSE | CÓ |
| 13 | 2026-03-03 | MB | 84 | 784 | WIN | LOSE | CÓ |
| 14 | 2026-03-04 | MN | 28 | 428 | WIN | LOSE | CÓ |
| 15 | 2026-03-04 | MT | 39 | 439 | WIN | LOSE | CÓ |
| 19 | 2026-03-05 | MB | 08 | 108 | WIN | LOSE | CÓ |
| 22 | 2026-03-06 | MB | 92 | 892 | WIN | LOSE | CÓ |
| 20 | 2026-03-06 | MN | 82 | 382 | WIN | LOSE | CÓ |
| 25 | 2026-03-07 | MB | 91 | 191 | WIN | LOSE | CÓ |
| 24 | 2026-03-07 | MT | 29 | 729 | WIN | LOSE | CÓ |
| 27 | 2026-03-08 | MT | 15 | 415 | WIN | LOSE | CÓ |
| 33 | 2026-03-10 | MT | 74 | 674 | WIN | LOSE | CÓ |
| 37 | 2026-03-11 | MB | 70 | 270 | WIN | LOSE | CÓ |
| 39 | 2026-03-12 | MT | 34 | 834 | WIN | LOSE | CÓ |
| 42 | 2026-03-13 | MT | 28 | 028 | WIN | LOSE | CÓ |
| 49 | 2026-03-15 | MB | 91 | 491 | WIN | LOSE | CÓ |
| 50 | 2026-03-16 | MN | 64 | 064 | WIN | LOSE | CÓ |
| 51 | 2026-03-16 | MT | 64 | 464 | WIN | LOSE | CÓ |
| 54 | 2026-03-17 | MT | 91 | 991 | WIN | LOSE | CÓ |
| 59 | 2026-03-19 | MN | 57 | 657 | WIN | LOSE | CÓ |
| 60 | 2026-03-19 | MT | 49 | 749 | WIN | LOSE | CÓ |
| 64 | 2026-03-20 | MB | 01 | 001 | WIN | LOSE | CÓ |
| 65 | 2026-03-21 | MN | 46 | 546 | WIN | LOSE | CÓ |
| 66 | 2026-03-21 | MT | 93 | 693 | WIN | LOSE | CÓ |
| 70 | 2026-03-22 | MB | 06 | 206 | WIN | LOSE | CÓ |
| 73 | 2026-03-23 | MB | 57 | 057 | WIN | LOSE | CÓ |
| 71 | 2026-03-23 | MN | 53 | 053 | WIN | LOSE | CÓ |
| 76 | 2026-03-24 | MB | 23 | 423 | WIN | LOSE | CÓ |
| 74 | 2026-03-24 | MN | 05 | 005 | WIN | LOSE | CÓ |
| 80 | 2026-03-26 | MN | 32 | 832 | WIN | LOSE | CÓ |
| 81 | 2026-03-26 | MT | 32 | 632 | WIN | LOSE | CÓ |
| 83 | 2026-03-27 | MN | 71 | 471 | WIN | LOSE | CÓ |

*(danh sách trên = toàn bộ 32 dòng, không rút gọn)*

## B.2 · Truy nguyên nhân — CÓ chạy nữa không

- **Ai ghi nhận sai:** `web/backend/_backfill_bundles.py` gọi `verify_final_bundle()` (import ở
  dòng 25) trong lượt chạy một-lần ngày 2026-03-30. **Tại thời điểm đó**, `verify_final_bundle`
  trong `database.py` **chưa có bản vá V16.1** — dùng cách chấm đơn giản theo đuôi 2 chữ số
  (đúng như `_backfill_bundles.py` tự khai ở dòng 13: *"Lo3 verify = simplified 2-digit tail
  check (Phase 1 trial limitation)"*).
- **Writer HIỆN TẠI đã được vá — bản vá này ĐANG chạy production:** `database.py:4812` hàm
  `verify_final_bundle`, đoạn `lo3_status` ở dòng 4869-4886, có comment **"V16.1 FIX: Must check
  FULL 3-digit match, not just 2-digit tail"**. Hàm này được gọi từ `main.py:6574, 6583, 6592,
  6608, 6947, 6971, 7006` và `scheduler.py:1264` — tức **mọi lần verify bundle LIVE hiện nay đều
  dùng bản ĐÚNG**. Bằng chứng thực nghiệm: trong 479 bundle LIVE (loại backfill), nhãn `lo3` lưu
  và tính lại **khớp 100%** (18/18 WIN, không lệch dòng nào) — xem B.3.
- **Kết luận: ĐÂY LÀ LỖI LỊCH SỬ ĐÃ ĐÓNG, KHÔNG PHẢI LỖI ĐANG TIẾP DIỄN.** `_backfill_bundles.py`
  không được import ở bất kỳ file nào khác, không có trong crontab (kiểm `crontab -l` trực tiếp
  trên VPS phiên này) → không có đường nào để nó chạy lại và tạo thêm dòng sai.

## B.3 · Ảnh hưởng nếu sửa — trước/sau

| | tổng dòng có lô3 | WIN theo nhãn lưu | WIN thật | tỉ lệ WIN |
|---|---|---|---|---|
| TRƯỚC (toàn bộ 570, hiện trạng) | 570 | **57** | 25 | **10,00%** (phóng đại 2,28×) |
| SAU khi sửa (toàn bộ 570) | 570 | 25 | 25 | **4,39%** (đúng thật) |
| Chỉ 479 dòng LIVE (không đổi, đối chứng) | 479 | 18 | 18 | 3,76% (đã đúng từ đầu, không cần sửa) |

## B.4 · Hai phương án sửa

### Phương án 1 — Sửa thẳng `lo3_status` (khuyến nghị chính — dùng đúng luật của hàm đang serve)

```sql
-- Bước 1: backup file DB trước khi UPDATE
-- Bước 2: sửa đúng 32 dòng đã xác minh (danh sách ở B.1), có điều kiện guard
--         "AND lo3_status='WIN'" để không lỡ ghi đè dòng nào đã được ai đó sửa trước:
UPDATE final_bundles
SET lo3_status = 'LOSE',
    notes = COALESCE(notes, '') || ' [V11169-CONG3: lo3_status sua WIN(sai,2-so-tail-bug 30/03)->LOSE]',
    updated_at = datetime('now','localtime')
WHERE id IN (5,6,13,14,15,19,20,22,24,25,27,33,37,39,42,49,50,51,54,59,60,64,65,66,70,71,73,74,76,80,81,83)
  AND lo3_status = 'WIN';
```
- **Số dòng bị chạm:** đúng **32 dòng** (điều kiện `AND lo3_status='WIN'` đảm bảo không chạm dòng
  nào khác nếu trạng thái đã đổi từ lúc đo tới lúc chạy).
- **Rủi ro:** THẤP-TRUNG BÌNH — sửa trực tiếp bảng production đang phục vụ `/du-doan` và mọi
  API lịch sử. Vì cả 91 bundle này đã có `verified_at` (bị FREEZE GUARD khoá từ tầng ứng dụng),
  **không app nào tự ghi đè lại các dòng này** — an toàn để sửa bằng SQL trực tiếp mà không lo
  race-condition với tiến trình đang chạy. Vẫn cần backup trước (chuẩn CLAUDE.md).
- **Gỡ về (rollback):** vì TRƯỚC KHI SỬA cả 32 dòng đều là `'WIN'` (đồng nhất), rollback đơn giản:
  ```sql
  UPDATE final_bundles SET lo3_status = 'WIN'
  WHERE id IN (5,6,13,14,15,19,20,22,24,25,27,33,37,39,42,49,50,51,54,59,60,64,65,66,70,71,73,74,76,80,81,83);
  -- (dòng "notes" annotation không cần xoá — vô hại, là dấu vết audit)
  ```

### Phương án 2 — KHÔNG sửa `lo3_status`, chỉ gắn cờ trong bảng phụ (bảo toàn "y nguyên lịch sử")

Dùng chung bảng `data_quality_flags` đề xuất ở Phương án 3 của Mục A:

```sql
INSERT INTO data_quality_flags (bundle_id, flag_type, reason, tagged_by)
SELECT id, 'LO3_LABEL_INCORRECT',
       'lo3_status luu = WIN nhung cham lai dung quy tac verify_final_bundle hien hanh = LOSE; ' ||
       'nguyen nhan: _backfill_bundles.py 30/03/2026 dung ban verify CU (2-so-tail, truoc V16.1)',
       'V11169_CONG3'
FROM final_bundles
WHERE id IN (5,6,13,14,15,19,20,22,24,25,27,33,37,39,42,49,50,51,54,59,60,64,65,66,70,71,73,74,76,80,81,83);
```
- **Số dòng bị chạm:** **0** trong `final_bundles` (giữ nguyên như một "biên bản đã xảy ra");
  **32 dòng mới** trong bảng phụ.
- **Rủi ro:** THẤP NHẤT về mặt ghi đè, nhưng **owner cần biết**: mọi script/API cũ đọc thẳng
  `lo3_status` (không join bảng phụ) sẽ **tiếp tục hiển thị sai** — bảng phụ chỉ có tác dụng nếu
  các script phân tích tương lai chủ động join nó vào.
- **Gỡ về:** `DELETE FROM data_quality_flags WHERE flag_type='LO3_LABEL_INCORRECT';`

## B.5 · Nếu TỪ CHỐI (giữ nguyên `lo3_status` sai)

- Lịch sử tỉ lệ 3-càng tiếp tục hiển thị **10,00%** thay vì thật **4,39%** cho bất kỳ ai/script
  nào đọc thẳng `lo3_status` gộp toàn lịch sử — phóng đại đúng **2,28 lần**.
- Vì đây là lỗi đã đóng (không tái diễn), rủi ro **không tăng thêm theo thời gian** — nhưng mọi
  con số "tỉ lệ lô3" đã/sẽ công bố dựa trên gộp toàn lịch sử vẫn sai cho tới khi sửa.

---

# PHẦN C — Việc NGOÀI phạm vi packet này (không xử ở đây, ghi rõ để không rơi)

Theo `evidence/GATE_s2-ngay-live.md` (V11166), còn hai việc liên quan **không** thuộc phạm vi
CONG 3 (đề bài giao đúng Mục A/B/C của gói duyệt):

- **RÚT LẠI công khai (PRJ-RETRACTION-001)** cho mọi báo cáo cũ từng dùng con số "57 lần WIN
  lô3" hoặc tỉ lệ lô3 gộp toàn lịch sử chưa lọc — việc này giao cho **agent báo cáo** ở phiên
  khác, không phải việc sửa DB.
- **Sửa các script báo cáo đang gộp "toàn lịch sử"/"180 ngày"** để tự động trừ 91 backfill (nếu
  owner chọn Phương án 3 của Mục A) — cần một phiên riêng quét toàn bộ `_v*.py`/`_materialize_*.py`
  đang query `final_bundles` không giới hạn ngày.

---

## PHỤ LỤC A — Danh sách đầy đủ 91 bundle backfill

| id | ngày | miền | bạch thủ | lô3 | bt_status lưu | bt đúng (tính lại) | created_at (giờ VN) | giờ kết quả đầu tiên về |
|---|---|---|---|---|---|---|---|---|
| 4 | 2026-02-28 | MB | 48 | 248 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-02-28T18:36:03+07:00 |
| 2 | 2026-02-28 | MN | 22 | 622 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-02-28T16:36:03+07:00 |
| 3 | 2026-02-28 | MT | 97 | 997 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-02-28T17:36:06+07:00 |
| 7 | 2026-03-01 | MB | 48 | 248 | WIN | WIN | 2026-03-30 13:42:14 | 2026-03-01T18:36:08+07:00 |
| 5 | 2026-03-01 | MN | 71 | 571 | WIN | WIN | 2026-03-30 13:42:14 | 2026-03-01T16:36:03+07:00 |
| 6 | 2026-03-01 | MT | 09 | 909 | WIN | WIN | 2026-03-30 13:42:14 | 2026-03-01T17:36:03+07:00 |
| 10 | 2026-03-02 | MB | 84 | 784 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-02T18:36:03+07:00 |
| 8 | 2026-03-02 | MN | 72 | 772 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-02T16:38:06+07:00 |
| 9 | 2026-03-02 | MT | 97 | 997 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-02T17:36:03+07:00 |
| 13 | 2026-03-03 | MB | 84 | 784 | WIN | WIN | 2026-03-30 13:42:14 | 2026-03-03T18:36:03+07:00 |
| 11 | 2026-03-03 | MN | 45 | 045 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-03T16:36:08+07:00 |
| 12 | 2026-03-03 | MT | 32 | 632 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-03T17:36:04+07:00 |
| 16 | 2026-03-04 | MB | 49 | 649 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-04T18:36:03+07:00 |
| 14 | 2026-03-04 | MN | 28 | 428 | WIN | WIN | 2026-03-30 13:42:14 | 2026-03-04T16:36:05+07:00 |
| 15 | 2026-03-04 | MT | 39 | 439 | WIN | WIN | 2026-03-30 13:42:14 | 2026-03-04T17:36:03+07:00 |
| 19 | 2026-03-05 | MB | 08 | 108 | WIN | WIN | 2026-03-30 13:42:14 | 2026-03-05T18:36:03+07:00 |
| 17 | 2026-03-05 | MN | 14 | 514 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-05T16:36:03+07:00 |
| 18 | 2026-03-05 | MT | 40 | 840 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-05T17:36:05+07:00 |
| 22 | 2026-03-06 | MB | 92 | 892 | WIN | WIN | 2026-03-30 13:42:14 | 2026-03-06T18:36:03+07:00 |
| 20 | 2026-03-06 | MN | 82 | 382 | WIN | WIN | 2026-03-30 13:42:14 | 2026-03-06T16:40:16+07:00 |
| 21 | 2026-03-06 | MT | 51 | 651 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-06T17:36:03+07:00 |
| 25 | 2026-03-07 | MB | 91 | 191 | WIN | WIN | 2026-03-30 13:42:14 | 2026-03-07T18:36:03+07:00 |
| 23 | 2026-03-07 | MN | 94 | 294 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-07T16:38:07+07:00 |
| 24 | 2026-03-07 | MT | 29 | 729 | WIN | WIN | 2026-03-30 13:42:14 | 2026-03-07T17:36:04+07:00 |
| 28 | 2026-03-08 | MB | 02 | 302 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-08T18:36:05+07:00 |
| 26 | 2026-03-08 | MN | 71 | 571 | WIN | WIN | 2026-03-30 13:42:14 | 2026-03-08T16:36:04+07:00 |
| 27 | 2026-03-08 | MT | 15 | 415 | WIN | WIN | 2026-03-30 13:42:14 | 2026-03-08T17:36:03+07:00 |
| 31 | 2026-03-09 | MB | 32 | 432 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-09T18:36:03+07:00 |
| 29 | 2026-03-09 | MN | 98 | 698 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-09T16:40:25+07:00 |
| 30 | 2026-03-09 | MT | 28 | 528 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-09T17:36:03+07:00 |
| 34 | 2026-03-10 | MB | 68 | 768 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-10T18:36:09+07:00 |
| 32 | 2026-03-10 | MN | 95 | 395 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-10T16:36:08+07:00 |
| 33 | 2026-03-10 | MT | 74 | 674 | WIN | WIN | 2026-03-30 13:42:14 | 2026-03-10T17:36:08+07:00 |
| 37 | 2026-03-11 | MB | 70 | 270 | WIN | WIN | 2026-03-30 13:42:15 | 2026-03-11T18:36:03+07:00 |
| 35 | 2026-03-11 | MN | 78 | 778 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-11T16:36:03+07:00 |
| 36 | 2026-03-11 | MT | 35 | 635 | LOSE | LOSE | 2026-03-30 13:42:14 | 2026-03-11T17:36:03+07:00 |
| 40 | 2026-03-12 | MB | 74 | 774 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-12T18:36:04+07:00 |
| 38 | 2026-03-12 | MN | 31 | 631 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-12T16:36:03+07:00 |
| 39 | 2026-03-12 | MT | 34 | 834 | WIN | WIN | 2026-03-30 13:42:15 | 2026-03-12T17:36:08+07:00 |
| 43 | 2026-03-13 | MB | 23 | 423 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-13T18:36:03+07:00 |
| 41 | 2026-03-13 | MN | 16 | 216 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-13T16:38:07+07:00 |
| 42 | 2026-03-13 | MT | 28 | 028 | WIN | WIN | 2026-03-30 13:42:15 | 2026-03-13T17:36:06+07:00 |
| 46 | 2026-03-14 | MB | 76 | 276 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-14T18:36:03+07:00 |
| 44 | 2026-03-14 | MN | 95 | 395 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-14T16:36:03+07:00 |
| 45 | 2026-03-14 | MT | 68 | 368 | WIN | WIN | 2026-03-30 13:42:15 | 2026-03-14T17:33:52+07:00 |
| 49 | 2026-03-15 | MB | 91 | 491 | WIN | WIN | 2026-03-30 13:42:15 | 2026-03-15T18:36:03+07:00 |
| 47 | 2026-03-15 | MN | 48 | 248 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-15T16:36:03+07:00 |
| 48 | 2026-03-15 | MT | 32 | 632 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-15T17:36:03+07:00 |
| 52 | 2026-03-16 | MB | 33 | 133 | WIN | WIN | 2026-03-30 13:42:15 | 2026-03-16T18:36:03+07:00 |
| 50 | 2026-03-16 | MN | 64 | 064 | WIN | WIN | 2026-03-30 13:42:15 | 2026-03-16T16:38:10+07:00 |
| 51 | 2026-03-16 | MT | 64 | 464 | WIN | WIN | 2026-03-30 13:42:15 | 2026-03-16T17:36:03+07:00 |
| 55 | 2026-03-17 | MB | 73 | 073 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-17T18:36:03+07:00 |
| 53 | 2026-03-17 | MN | 74 | 474 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-17T16:36:03+07:00 |
| 54 | 2026-03-17 | MT | 91 | 991 | WIN | WIN | 2026-03-30 13:42:15 | 2026-03-17T17:36:08+07:00 |
| 58 | 2026-03-18 | MB | 44 | 344 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-18T18:36:10+07:00 |
| 56 | 2026-03-18 | MN | 93 | 093 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-18T16:36:03+07:00 |
| 57 | 2026-03-18 | MT | 91 | 991 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-18T17:36:03+07:00 |
| 61 | 2026-03-19 | MB | 57 | 057 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-19T18:36:03+07:00 |
| 59 | 2026-03-19 | MN | 57 | 657 | WIN | WIN | 2026-03-30 13:42:15 | 2026-03-19T16:36:03+07:00 |
| 60 | 2026-03-19 | MT | 49 | 749 | WIN | WIN | 2026-03-30 13:42:15 | 2026-03-19T17:36:03+07:00 |
| 64 | 2026-03-20 | MB | 01 | 001 | WIN | WIN | 2026-03-30 13:42:15 | 2026-03-20T18:36:03+07:00 |
| 62 | 2026-03-20 | MN | 52 | 852 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-20T16:40:10+07:00 |
| 63 | 2026-03-20 | MT | 27 | 827 | LOSE | LOSE | 2026-03-30 13:42:15 | 2026-03-20T17:36:03+07:00 |
| 67 | 2026-03-21 | MB | 49 | 649 | LOSE | LOSE | 2026-03-30 13:42:16 | 2026-03-21T18:36:08+07:00 |
| 65 | 2026-03-21 | MN | 46 | 546 | WIN | WIN | 2026-03-30 13:42:15 | 2026-03-21T16:36:06+07:00 |
| 66 | 2026-03-21 | MT | 93 | 693 | WIN | WIN | 2026-03-30 13:42:16 | 2026-03-21T17:36:03+07:00 |
| 70 | 2026-03-22 | MB | 06 | 206 | WIN | WIN | 2026-03-30 13:42:16 | 2026-03-22T18:36:03+07:00 |
| 68 | 2026-03-22 | MN | 61 | 261 | LOSE | LOSE | 2026-03-30 13:42:16 | 2026-03-22T16:36:03+07:00 |
| 69 | 2026-03-22 | MT | 61 | 561 | WIN | WIN | 2026-03-30 13:42:16 | 2026-03-22T17:36:03+07:00 |
| 73 | 2026-03-23 | MB | 57 | 057 | WIN | WIN | 2026-03-30 13:42:16 | 2026-03-23T18:36:03+07:00 |
| 71 | 2026-03-23 | MN | 53 | 053 | WIN | WIN | 2026-03-30 13:42:16 | 2026-03-23T16:40:21+07:00 |
| 72 | 2026-03-23 | MT | 18 | 218 | WIN | WIN | 2026-03-30 13:42:16 | 2026-03-23T17:36:03+07:00 |
| 76 | 2026-03-24 | MB | 23 | 423 | WIN | WIN | 2026-03-30 13:42:16 | 2026-03-24T18:36:03+07:00 |
| 74 | 2026-03-24 | MN | 05 | 005 | WIN | WIN | 2026-03-30 13:42:16 | 2026-03-24T16:36:03+07:00 |
| 75 | 2026-03-24 | MT | 91 | 991 | LOSE | LOSE | 2026-03-30 13:42:16 | 2026-03-24T17:36:08+07:00 |
| 79 | 2026-03-25 | MB | 23 | 923 | LOSE | LOSE | 2026-03-30 13:42:16 | 2026-03-25T18:36:03+07:00 |
| 77 | 2026-03-25 | MN | 51 | 251 | LOSE | LOSE | 2026-03-30 13:42:16 | 2026-03-25T16:36:08+07:00 |
| 78 | 2026-03-25 | MT | 90 | 590 | LOSE | LOSE | 2026-03-30 13:42:16 | 2026-03-25T17:36:05+07:00 |
| 82 | 2026-03-26 | MB | 34 | 634 | LOSE | LOSE | 2026-03-30 13:42:16 | 2026-03-26T22:07:55+07:00 |
| 80 | 2026-03-26 | MN | 32 | 832 | WIN | WIN | 2026-03-30 13:42:16 | 2026-03-26T16:38:56+07:00 |
| 81 | 2026-03-26 | MT | 32 | 632 | WIN | WIN | 2026-03-30 13:42:16 | 2026-03-26T17:36:03+07:00 |
| 85 | 2026-03-27 | MB | 71 | 571 | LOSE | LOSE | 2026-03-30 13:42:16 | 2026-03-27T18:38:00+07:00 |
| 83 | 2026-03-27 | MN | 71 | 471 | WIN | WIN | 2026-03-30 13:42:16 | 2026-03-27T16:59:34+07:00 |
| 84 | 2026-03-27 | MT | 71 | 671 | LOSE | LOSE | 2026-03-30 13:42:16 | 2026-03-27T17:38:00+07:00 |
| 88 | 2026-03-28 | MB | 89 | 789 | LOSE | LOSE | 2026-03-30 13:42:16 | 2026-03-28T18:38:00+07:00 |
| 86 | 2026-03-28 | MN | 67 | 667 | LOSE | LOSE | 2026-03-30 13:42:16 | 2026-03-28T16:38:01+07:00 |
| 87 | 2026-03-28 | MT | 74 | 674 | LOSE | LOSE | 2026-03-30 13:42:16 | 2026-03-28T17:28:25+07:00 |
| 91 | 2026-03-29 | MB | 23 | 923 | LOSE | LOSE | 2026-03-30 13:42:16 | 2026-03-29T18:38:00+07:00 |
| 89 | 2026-03-29 | MN | 03 | 203 | WIN | WIN | 2026-03-30 13:42:16 | 2026-03-29T16:39:32+07:00 |
| 90 | 2026-03-29 | MT | 09 | 009 | LOSE | LOSE | 2026-03-30 13:42:16 | 2026-03-29T17:38:00+07:00 |
| 93 | 2026-03-30 | MT | 46 | 446 | WIN | WIN | 2026-03-30 17:53:42 | 2026-03-30T17:38:01+07:00 |

*(danh sách trên = toàn bộ 91 dòng, không rút gọn; nguồn: `v11169_w3_thuoc_raw.json` đính kèm ở
`evidence/`)*

---

## Ba lớp nguồn (§62)

- **OWNER_SAID:** không có lời owner trực tiếp trong phiên này về hai lỗi cụ thể này — phiên
  V11169 giao việc "soạn gói duyệt" qua đề bài văn bản đầu phiên (không phải hội thoại trực
  tiếp), nên không có nguyên văn+giờ để trích theo §62/PRJ-INTERACTION-LEDGER-001.
- **CODE_DID:** mọi số liệu trong tài liệu này tính lại trực tiếp từ `database.py:4812-4891`
  (hàm `verify_final_bundle`, quy tắc WIN/LOSE) và dump read-only `v11166_s7_fact.json` +
  kiểm `notes` trực tiếp trên VPS (script `_w3_check_notes.py`, phiên này, chỉ SELECT).
- **DOC_SAID:** `Lottery_AI_Notion_Reports/V11166_TONG_LUC_VA_DON_DEP_20260905/evidence/GATE_s2-ngay-live.md`
  mục "VIEC CAN LAM" P1 (dòng 15-19 của gate đó) — nơi hai việc này lần đầu được flag là cần
  owner quyết định.

**TanPhatAI cần làm:** không có — packet này chưa ghi gì vào DB, chưa công bố số mới, chỉ chờ
owner chọn phương án. Khi owner duyệt và một phiên có quyền ghi DB thực thi xong, phiên đó phải
tự cập nhật `CHANGELOG.md`/`CURRENT_TRUTH_SSOT.md`/`OWNER_DECISION_LEDGER.json` theo đúng chuỗi
hoàn tất — việc đó KHÔNG nằm trong packet này.
