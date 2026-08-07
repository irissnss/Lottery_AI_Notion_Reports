# REPORT V11025 — A1: THÔI XOÁ BỘ ĐẾM ĐO TIẾN MỖI THỨ HAI

> **Ngày:** 2026-08-07 đêm · **Đã deploy** · PID `993241 → 1004216` · 4 bảng khoá Y HỆT
> Đây là **nút thắt số 1** mà tra soát V11024 chỉ ra. Gỡ xong thì mọi kế hoạch đo mới có chỗ đứng.

---

## 1. Tóm tắt

Trước hôm nay, **mỗi thứ Hai hệ tự xoá 1.680 dòng bằng chứng** rồi chấm lại bằng hindsight. Hậu
quả: số lượt đo tiến **không bao giờ vượt 35/miền**, **0/105 luật** đạt ngưỡng n≥20. Mọi kế hoạch
*"đo thêm N ngày rồi kết luận"* — kể cả FU-284 và FU-325 — **bất khả thi về cấu trúc**, không
phải thiếu mẫu.

Nay bằng chứng **được nối lại thay vì bị xoá**. Trên VPS: MRE **3.248 dòng giữ nguyên**,
`DO_TIEN` **15** và bắt đầu tích luỹ.

## 2. Owner yêu cầu gì (nguyên văn)

> *"Ok vậy em làm A1 đi chờ gì nữa?"*

## 3. Đào bới / phát hiện

### 3.1 Bệnh · `VERIFIED_CODE`

`weekly_rule_miner.run_weekly_mining()` Step 4:

```python
c.execute("DELETE FROM mined_rule_effectiveness WHERE date >= date('now','-112 days')")
backfill_mined_rules(112)
```

Chú thích ghi ý định **đúng** — *"Rebuild recent effectiveness window so new rule_ids keep
livingness/tracking continuity"*.

### 3.2 Gốc bệnh nằm chỗ khác · `VERIFIED_CODE`

`_seed_rules.py:432` chạy `DELETE FROM mined_rules` rồi INSERT lại ⇒ **`rule_id` đổi hết mỗi
tuần** (AUTOINCREMENT mới). Không có cách nào nối bằng chứng cũ với luật mới ⇒ giải pháp cũ buộc
phải **xoá sạch rồi chấm lại bằng hindsight**.

Mô phỏng đổi `rule_id` trên bản sao DB: **3.248 dòng MRE mồ côi ngay lập tức**. Đó là lý do
thật khiến Step 4 phải xoá.

### 3.3 Khoá bền có dùng được không · `VERIFIED_TEST`

Bộ **sáu cột định danh nghiệp vụ**:
`(target_region, target_weekday, đài nguồn, source_region, source_offset, prize_keys)`

```
105 luật active → 105 khoá phân biệt   ⇒ KHOÁ DUY NHẤT, dùng được
```

Và `mined_rule_effectiveness` **đã có sẵn cả sáu cột** ⇒ suy được khoá cho mọi dòng cũ, không mất
dữ liệu.

## 4. Hướng xử lý và vì sao chọn

**Không đụng `rule_id`** — nhiều chỗ đang đọc nó, đổi là vỡ dây chuyền. Thay vào đó cấp thêm
**khoá bền** song song.

**Sổ khoá phải CHỈ THÊM, không bao giờ xoá.** Vì bảng lưu luật cũ **không tồn tại**
(`archived_previous` chỉ dùng để ghi log), nên nếu sổ này cũng bị xoá thì lại rơi vào đúng bệnh cũ.

**Step 4 mới đạt đúng mục tiêu ban đầu mà không mất gì:** nối `rule_id` mới theo khoá bền →
**không xoá dòng nào** → chỉ lấp những (ngày, khoá) chưa có.

## 5. Đã làm gì

| bề mặt | nội dung |
|---|---|
| `_v11025_khoa_luat_ben.py` | module khoá bền — `khoa_luat()` · `nang_cap_luoc_do()` · `gieo_mam_registry()` · `ghi_nhan_lan_dao()` · `noi_lai_rule_id()` · `phan_loai_giai_doan()` |
| `rule_key_registry` | bảng **CHỈ THÊM** — ngày sinh thật của mỗi khoá + `nguon_lan_dau` (OBSERVED / SEED_*) |
| `mined_rule_effectiveness` | **+2 cột** `rule_key` · `giai_doan` · **+1 index** |
| `weekly_rule_miner.py` Step 4 | **DELETE + backfill → NỐI LẠI + lấp chỗ trống** |
| `mined_rule_eval.py` | ghi kèm `rule_key` ở mỗi lần chấm |
| `_v11025_di_tru.py` | di trú, **chạy nhiều lần vô hại** |
| `_v11025_thu_tren_ban_sao.py` | mô phỏng lần đào tới **trên bản sao DB** |

## 6. Cổng kiểm

### 6.1 Mô phỏng lần đào tới — chứng minh TRƯỚC khi tin

| | |
|---|---|
| **cách CŨ** | `DELETE date>=now-112d` ⇒ **xoá 1.680 dòng** |
| đổi hết `rule_id` | **3.248 dòng mồ côi** |
| **cách MỚI** | nối **2.452 dòng** · mồ côi **3.248 → 796** · MRE **giữ nguyên** · đo tiến **giữ nguyên** |

### 6.2 Deploy

| phép | kết quả |
|---|---|
| md5 4 tệp local ≡ VPS | ✓ cả bốn |
| `py_compile` (venv của service) | ✓ OK |
| **mô phỏng trên BẢN SAO** đạt trước khi động DB thật | ✓ `✓ ĐẠT` |
| di trú: MRE trước → sau | **3.248 → 3.248** ✓ không mất dòng nào |
| **4 bảng khoá** | ✓ **Y HỆT** |
| PID | `993241 → 1004216` ✓ |
| `/api/health` | **200** |
| chạy di trú lần hai | **0 thay đổi** ✓ đúng tính chất chạy nhiều lần vô hại |

### 6.3 Trạng thái VPS sau di trú

```
giai_doan            dòng  khoá
-------------------  ----  ----
DO_TIEN               15     15
KHONG_RO_LUAT        796    275
KHONG_XAC_MINH_DUOC 2437    105

rule_key_registry: 105 khoá · nguồn SEED_TU_MRE · sớm nhất 2026-01-05
```

## 7. Vướng vấp

### 7.1 Bản đầu tạo ra một THẮNG LỢI GIẢ

Hàm phân loại bản đầu gán `DO_TIEN` khi `date >= lan_dau_thay`. Thử khô ra
**`DO_TIEN 2.437 · CHAM_NGUOC 0`** — nghe như thắng lớn.

**Nhưng đó là phép đo tự khen chính mình:** với khoá gieo mầm, `lan_dau_thay` được lấy bằng
**chính ngày chấm sớm nhất trong MRE**, nên mọi dòng đương nhiên `>=` nó.

Sự thật: bảng lưu luật cũ **không tồn tại**, nên với dòng cũ ta **không chứng minh được** luật đã
tồn tại trước ngày đó hay được chọn ra bằng chính dữ liệu ngày đó. **Không biết thì phải nói là
không biết** ⇒ nhãn `KHONG_XAC_MINH_DUOC`, **cấm đếm là đo tiến**.

Sau khi sửa: `DO_TIEN` = **0** ở local, **15** trên VPS (đúng — các dòng ngày 07/08).

### 7.2 Một cổng kiểm của chính agent nói dối

`_bam4()` trong `_v11025_di_tru.py` băm `repr(r)` trong khi lời gọi đã đặt
`con.row_factory = sqlite3.Row` ⇒ `repr` ra `<sqlite3.Row object at 0x000001C4...>`, tức **băm
địa chỉ bộ nhớ**, đổi mỗi lần chạy.

Script báo **"4 bảng khoá ĐÃ ĐỔI"** trong khi cổng độc lập `cong_bam_4_bang_khoa.py` (không đặt
`row_factory`) báo **Y HỆT** — và **cổng độc lập đúng**.

**Có hai phép kiểm độc lập mới bắt được.** Một mình phép sai thì đã báo động giả cả đêm và có thể
dẫn tới gỡ về một thay đổi đang chạy đúng.

## 8. Gỡ về

```bash
# code
cp /root/Lottery_AI_Test/backups/v11025_pre/*.py /root/Lottery_AI_Test/web/backend/ \
  && systemctl restart lottery
# local
cp backups/v11025_pre/weekly_rule_miner.py backups/v11025_pre/mined_rule_eval.py web/backend/
```

**DB không cần gỡ:** V11025 **chỉ thêm** 2 cột + 1 bảng + 1 index, **không xoá và không sửa** dữ
liệu cũ. Bỏ qua là xong. Muốn sạch hẳn: `DROP TABLE rule_key_registry`.

## 9. Theo dõi tiếp

| Mã | Nội dung | Trạng thái | Hạn |
|---|---|---|---|
| **FU-330** (A1) | Thôi xoá bộ đếm đo tiến | **`DEPLOYED_PENDING_LIVE_VERIFY`** | 07/08 |
| **FU-331** | **Xác minh lần đào THẬT 10/08 không xoá bằng chứng** | `WAIT_LIVE` | **11/08** |

**FU-331 là phép kiểm quyết định.** V11025 mới chỉ chứng minh bằng **mô phỏng** trên bản sao. Lần
đào thật đầu tiên sau khi vá là **thứ Hai 10/08 00:30**.

**Ngưỡng hành động, chốt trước:** sáng 11/08 chạy
`SELECT giai_doan, COUNT(*) FROM mined_rule_effectiveness GROUP BY 1`.
Số dòng MRE **không được giảm** và `DO_TIEN` **không được về 0**. Sai một trong hai ⇒ **gỡ về
ngay** `backups/v11025_pre/`.

Và tìm trong `logs/weekly_miner_cron.log` dòng
`Step 4 (V11025): NỐI LẠI thay vì xoá` — không có dòng đó nghĩa là nhánh mới không chạy.

---

**Điều owner cần biết:** con số `DO_TIEN` hôm nay là **15**, rất nhỏ. Đó là **con số đúng** — nó
nhỏ vì đây là ngày đầu tiên hệ có khả năng đếm. Trước hôm nay con số đó bị bấm về 0 mỗi tuần nên
**không bao giờ lớn lên được**. Từ 08/08 nó bắt đầu tích luỹ thật.
