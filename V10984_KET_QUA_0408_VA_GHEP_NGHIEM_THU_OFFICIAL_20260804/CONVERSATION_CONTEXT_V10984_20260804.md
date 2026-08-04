# Ngữ cảnh phiên V10984 — 04/08/2026

Ghi theo `§57.2` (A55.2): **nguyên văn** lời owner + agent làm gì + vấp ở đâu. Không diễn giải
lại, không sửa chính tả của owner.

---

## 1. Lời owner — nguyên văn

### 21:35 (giờ VN) — yêu cầu duy nhất của phiên

> *"Thực sự quán chán ngán kết quả dự đoán quá tệ anh cần một kế hoạch triển khai sơm hơn dự
> kiến em xem thử dùm anh có triển khai được gì trước không em ? Theo như anh quan sat thấy
> offical cũng khá tiềm năng chứ em, cần 1 sự kết hợp hoàn hảo ở /nghiem-thu và offical nha .
> Kết quả dự đoán ngày hôm nay thế nào em thử tổng lực dùm anh."*

Agent tách thành ba việc:

- **(A)** Kết quả dự đoán hôm nay 04/08 thế nào — đo tổng lực
- **(B)** Kết hợp official + lane `/nghiem-thu`
- **(C)** Kế hoạch triển khai sớm hơn dự kiến

Bối cảnh tinh thần cần ghi lại: owner **đang mất kiên nhẫn** (*"chán ngán… quá tệ"*). Nên
nguyên tắc của phiên là **không đường mật, không hứa lảo** — số liệu không ủng hộ thì nói thẳng.

---

## 2. Quyết định ghi vào sổ trong phiên

`QD-024` · `DO0811` · *Ghép `/nghiem-thu` với official phải đi đường đo bóng tiến, không bật
thẳng* · hạn rà soát **11/08** · 5 mệnh đề máy kiểm được · trạng thái `ACTIVE`.

---

## 3. Agent đã làm gì, theo thứ tự

| # | Việc | Kết quả |
|---|---|---|
| 1 | `_v10920_session_start.py` | 0 checkpoint quá hạn · 3 mục đến hạn hôm nay · 1 quá hạn · 18 mồ côi |
| 2 | `_v10920_decision_ledger.py` | 25 quyết định, **0 TRÔI** |
| 3 | `_v10sync_live_forensic_inputs.py` | **TRƯỢT 2 lần** — `Hash mismatch` → điều tra, sửa (xem §4.1) |
| 4 | Tra `tz_registry` trước khi đọc dấu thời gian | 6 bảng dùng trong phiên **đều lưu giờ VN** + có cột ngày nghiệp vụ → đọc thẳng, không dính bẫy UTC |
| 5 | Đọc mã xác minh (`_bt_status`, `_get_region_actual_tails`) | Xác định đúng luật chấm: bạch thủ trúng nếu số nằm trong tập 2 số đuôi của **mọi giải, mọi đài trong miền** |
| 6 | Kiểm chéo luật chấm | Tự tính lại từ `prizes_json` **khớp `bach_thu_status` 3/3 ô** hôm nay → yên tâm dùng |
| 7 | Đo phần (A) — kết quả hôm nay | Official **1/3 miền** (MT 60 trúng Đắk Lắk) · lane nghiệm thu **0/3** |
| 8 | Đo phạm vi thật của lane `/nghiem-thu` | **Chỉ 15 ô đo tiến**, không phải 123 ngày như bảng gợi ý — phần lớn là backfill hồi tố |
| 9 | Dựng `_v10984_ghep_lane_official.py` | 5 cách ghép, bảng đo bóng, ngưỡng viết sẵn |
| 10 | Đo phần (B) | **Không cách ghép nào hơn official**. Trùng lặp 73,33% · 4 ô lệch official thắng 4/4 |
| 11 | Chạy `_v10945_edge_gate.py` 30/90/180 ngày | **Cổng ĐÓNG cả 6 ô** — trả lời phần (C4) |
| 12 | Đọc `docs/LICH_CUON_CHIEU_DEN_10082026.md` | Lịch đã giãn **3 lần trong chính ngày hôm nay**; §3 đã kéo sẵn 5 mục |
| 13 | Ghi quản trị | `QD-024` + CHANGELOG + SSOT + `FU-264` + AUTOMATION_STATE |
| 14 | Deploy 21:59:37 | PID **770947 → 801640** · 4 bảng khoá **giữ nguyên** · health 200 · admin 401 |
| 15 | Nghiệm thu trên VPS | 11 nhóm kiểm, `_v10984_kiem.py` **14/14** trên chính VPS |
| 16 | Sửa `J8` + đóng `FU-244` | Cả hai cổng lịch **8/8** · ledger **0 TRÔI** |

---

## 4. Vấp ở đâu — kể cả vấp do chính agent gây ra

### 4.1 Bước tiền đề bắt buộc thì lại đang hỏng

`web/_sync_live_forensic_inputs.py` là bước **quy tắc bắt buộc** trước mọi việc accuracy. Nó
trượt **cả hai lần** với `Hash mismatch`, và hash khác nhau giữa hai lần:

```
lần 1: remote=8f1328e5c8a264c5…  local=dbf2a48072767c1d…
lần 2: remote=4f204e41eebdf125…  local=409cd10c885c85f9…
```

Agent **không đi vòng** bằng cách bỏ qua bước này. Đọc mã thì thấy nguyên nhân thật: script
`sha256sum` tệp DB **đang chạy** ở một thời điểm rồi `sftp.get` cùng tệp đó ở thời điểm khác —
production ghi vào giữa hai lần nên không bao giờ khớp. Với DB sống, phép kiểm đó **không thể
đúng**.

Đã sửa: đóng băng bản chụp trên máy chủ trước (`sqlite3 .backup` nhất quán theo giao dịch cho
DB, `cp -p` cho jsonl) rồi mới băm + tải. Chạy lại **exit 0**.

**Hậu quả nếu bỏ qua:** mọi phiên forensic sau này buộc phải đi vòng quy tắc toàn vẹn dữ liệu
sống, hoặc dùng bản local cũ mà tưởng là mới.

### 4.2 Cổng lịch phạt việc làm xong sớm — owner vừa yêu cầu làm sớm

Sau khi ghi `FU-244` là xong, ledger báo **`QD-022` TRÔI 1/9**:
`J8: MỒ CÔI trong nhóm: ['FU-244=?']`.

Hai lỗi ghép lại:

1. **Lỗi agent:** khối `FU-244` đầu tiên viết dạng gạch đầu dòng, **thiếu trường `status`** → bộ
   đọc trả `?`. Đã viết lại đúng khuôn bảng với `| **status** | CLOSED_PASS |`.
2. **Lỗi cổng:** `J8` chỉ soi `TREO_STATUSES` nên **bất kỳ** mục làm xong sớm với nhãn đóng hợp
   lệ đều bị báo MỒ CÔI — trái **chú thích của chính nó** ngay bên trên và trái định nghĩa gốc
   trong `trang_thai_mo_coi()`.

Đã sửa `J8` dùng `TREO_STATUSES | DONG_STATUSES`. **Không nới cổng** — chỉ chặn nhãn không thuộc
bộ nào, đúng ý định đã viết. Sau sửa 8/8, mồ côi toàn sổ **giảm** 19 → 18.

**Hậu quả nếu bỏ qua:** cổng dạy agent để mục treo vô thời hạn cho dễ xanh — ngược hẳn yêu cầu
(C) của owner.

### 4.3 Suýt ghi "xong" trước khi thật sự xong

Khối governance viết `FU-244` "ĐẠT" **trước khi** deploy chạy — lúc đó cron chưa cắm,
`edge_gate_daily` chưa có dòng mới. Đúng nghĩa hứa lảo. Đã đảo thứ tự: deploy → chạy cổng lợi
thế trên VPS → **rồi mới** ghi ĐẠT kèm số đo thật (`grep -c` = 1, bảng có 3 dòng ngày 04/08).

### 4.4 Ba lỗi kỹ thuật nhỏ tự gây

| Lỗi | Bắt được lúc nào |
|---|---|
| Lồng dấu nháy cùng loại trong f-string — chỉ chạy từ Python 3.12 | Trước khi chạy, sửa phòng xa cho venv 3.11 trên VPS |
| Thêm `dt.date` vào dữ liệu lịch → `_v10981_trang_lich.py` chết `TypeError` khi xuất JSON. **Trang MD ghi xong nhưng JSON thì không** — hỏng nửa vời | Ngay khi chạy; đổi sang chuỗi ISO |
| Gõ sai tên trường `vi_saoO_khong_som` | StrReplace báo không tìm thấy nên không vào file. Nếu vào thì phép `J7` mất một mục mà không ai biết |

### 4.5 Chỗ agent phải nói ngược ý owner

Owner quan sát *"official cũng khá tiềm năng"*. Agent **không chiều lòng**: đúng với 7 ngày
(9/21 ô = 42,9%, MN +6,55pp, MB +19,29pp) nhưng **sai với 30/90/180 ngày** — cổng lợi thế
`QD-013` **ĐÓNG cả 6 ô**, z cao nhất chỉ 1,20, MB chỉ có 7 lượt đặt.

Và owner muốn *"1 sự kết hợp hoàn hảo"* giữa hai luồng. Agent phải trả lời rằng **số liệu đang
nói ngược**: hai luồng trùng nhau 73,33%, và ở 4 ô lệch nhau thì official đúng **4/4** — lane
nghiệm thu **chưa từng** trúng ở một ô nó tự chọn khác official. Mọi cách ghép đều **tệ hơn**
official một mình.

Đồng thời phải nói rõ **giới hạn của chính kết luận đó**: 15 ô / 35 lượt đặt là quá nhỏ, z chỉ
1,30, cần ~536 ngày nữa mới đủ mẫu. Nên kết luận này là **hướng**, không phải bằng chứng — nói
cả hai chiều thay vì chỉ chiều có lợi cho lập luận.

---

## 5. Cái gì phiên này KHÔNG làm

- **Không** đụng `/du-doan`, writer `final_bundles`, bộ chọn model production, roster 15 model,
  bộ lọc combo-super, lớp ghi đè — `QD-014` còn khớp **7/7**.
- **Không** ghi gì vào Notion (§57.1 cấm mọi thao tác ghi).
- **Không** đặt tiền thật — `QD-013` giữ 100%.
- **Chưa xử 3 mục đến hạn hôm nay** (`FU-187` · `FU-191` · `FU-212`) vì owner yêu cầu việc khác.
  Nói rõ để không trôi mất.
- **Không** rút ngắn cửa sổ đo của `QD-015`→`QD-018` để "triển khai sớm" cho vừa lòng owner —
  đó là cái bẫy đã làm rữa V10655 → V10672 → V10677 → V10753 → V10789 → V10790.
