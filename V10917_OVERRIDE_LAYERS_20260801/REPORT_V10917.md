# V10917 / V10918 — Tắt 5 lớp ghi đè bạch thủ

**Ngày:** 01/08/2026 · **Commit riêng:** `67ec1a3` · **Trạng thái:** đã deploy, chờ xác minh live

> Owner sáng 01/08: *"Xử lý an toàn, cải tiến, cải thiện, tinh gọn, sạch sẽ cho cả 3 miền nha em."*

---

## 1. Tóm tắt một đoạn

Đang chạy bước "thử trên giấy" của kế hoạch cắt model thì phát hiện chuyện lớn hơn: **37% số
ngày, bạch thủ công bố không phải số thắng cuộc bỏ phiếu của các model.** Có 5 lớp ghi đè chạy
sau khi cộng phiếu xong và đổi số. Đo tiến 60 ngày live cho thấy chỉ 1 trong 6 lớp có lợi; 5 lớp
còn lại làm mất **73,5 triệu**. Đã tắt 5 lớp, giữ lớp duy nhất có lợi.

Kỳ vọng: **28,9% → 35,6%** tỉ lệ trúng, **−96,5tr → −23,0tr** trên 60 ngày. Miền Bắc từ lỗ
27,1tr thành **lãi 12,1tr**.

---

## 2. Phát hiện

### 2.1 Hai cổng kiểm tự đặt đều trượt

Trước khi dùng phép mô phỏng để quyết định cắt model, đặt hai điều kiện bắt buộc:

| Cổng | Yêu cầu | Kết quả |
|---|---|---|
| 1 | Tổng điểm đóng góp từng model = điểm đã lưu | **trượt** — 76/1.776 số lệch, tỉ lệ đều 1,176–1,186 |
| 2 | Số đầu bảng = bạch thủ đã công bố | **trượt** — 67/180 bundle khác nhau |

Cổng 1 truy ra là bộ giảm điểm `pp1_convergence_dampener`: ≥3 model "bầy đàn" cùng chọn một số
thì điểm nhân 0,85. Kiểm: `0.1154 × 0.85 = 0.0981` khớp chính xác, và `1/0.85 = 1,176` đúng bằng
tỉ lệ lệch quan sát được.

Cổng 2 mới là vấn đề thật.

### 2.2 Năm lớp ghi đè nối tiếp

`web/backend/main.py:9858–9942`, chạy sau khi cộng phiếu xong:

| Thứ tự | Lớp | Miền | Việc |
|---|---|---|---|
| 1 | V10883 connector | cả ba | thay cả bảng xếp hạng — **chưa từng chạy** (`generation_method` = `weighted_voting_wr` cả 181 lượt) |
| 2 | V10640 per-slice | cả ba | MN `specialist` · MT `nt_consensus` · MB `prior_region` |
| 3 | V10767 prev-day | MB | lấy đa số ML hôm trước |
| 4 | V10789 lane promote | MB | lấy theo luồng test `MB_OUTPUT_V1` |
| 5 | V10790 lane promote | MT | lấy theo luồng test `MT_OUTPUT_V1` |

Lớp sau đè lớp trước. Ví dụ MB 31/07 số bị đổi ba lần rồi quay về chỗ cũ:

```
phiếu bầu 19 → V10640 → 28 → V10767 → 93 → V10789 → 19
```

Ví dụ đổi thật, 04/06 MB: số `16` được 0,1213 điểm (cao nhất) nhưng công bố số `94` chỉ 0,0522 —
chưa bằng một nửa.

---

## 3. Đo tiến từng lớp, 60 ngày live (02/06 – 31/07)

Chấm bằng chính nhật ký champion/challenger của từng lớp. Đã loại 3 dòng ghi bù (ghi sau khi
bundle chốt, mang `champion_bt=99` là số giữ chỗ).

| Lớp | Ngày | Đổi số | Tốt | Xấu | Hòa | p | Trúng vào→ra | Tiền |
|---|---|---|---|---|---|---|---|---|
| V10767 · MB hôm trước | 32 | 29 | 5 | 5 | 19 | 1,000 | 21,9%→21,9% | **±0,0tr** |
| V10789 · MB luồng test | 23 | 23 | 4 | 5 | 14 | 1,000 | 21,7%→17,4% | −4,9tr |
| V10790 · MT luồng test | 22 | 16 | 3 | 4 | 9 | 1,000 | 31,8%→27,3% | −9,8tr |
| **V10640 · MN** specialist | 60 | 21 | 6 | 4 | 11 | 0,754 | 36,7%→40,0% | **+14,7tr** |
| **V10640 · MB** prior_region | 60 | 29 | **2** | **8** | 19 | 0,109 | 31,7%→21,7% | **−29,4tr** |
| **V10640 · MT** nt_consensus | 60 | 23 | **2** | **5** | 16 | 0,453 | 35,0%→30,0% | **−24,5tr** |

Gộp hai nhánh MT+MB của V10640: **4 tốt / 13 xấu**, phép thử dấu **p = 0,049**.

### Đo theo cửa sổ ngày từng lớp được bật

Bắt buộc tách, vì V10767 bật 01/07, V10789 bật 09/07, V10790 bật 10/07 — đo gộp 60 ngày cho một
lớp mới bật 20 ngày là sai.

| Cửa sổ | Lượt | Theo phiếu bầu | Thực tế công bố |
|---|---|---|---|
| MN · chỉ V10640 | 60 | 36,7% (−36,9tr) | **40,0% (−22,2tr)** |
| MT · chỉ V10640 (<10/07) | 38 | **34,2% (−4,4tr)** | 28,9% (−28,9tr) |
| MT · +V10790 (≥10/07) | 22 | **36,4% (−8,5tr)** | 27,3% (−18,3tr) |
| MB · chỉ V10640 (<01/07) | 29 | **27,6% (+0,1tr)** | 20,7% (−9,8tr) |
| MB · +V10767 (01–08/07) | 8 | **25,0% (−1,0tr)** | 12,5% (−5,9tr) |
| MB · +V10789 (≥09/07) | 23 | **39,1% (+13,1tr)** | 17,4% (−11,4tr) |

MT và MB thua ở **mọi** cửa sổ, kể cả trước khi hai lớp mới được bật. MN thắng.

---

## 4. Mô phỏng nguyên chuỗi — cổng kiểm 180/180

Không được cộng dồn tiền từng lớp, vì lớp sau đè lớp trước. Dựng lại nguyên chuỗi theo đúng cửa
sổ ngày, **bắt buộc tái tạo đúng bạch thủ đã công bố ở cả 180 lượt** trước khi được kết luận.

Lần chạy đầu lệch 3 ngày (25/06, 01/07, 02/07 — đều MB). Không nới ngưỡng cho qua; soi ra cả ba
dòng nhật ký được ghi **sau** khi bundle đã chốt (25/06 ghi bù tận 02/07) và đều mang
`champion_bt=99`. Đặt luật: **chỉ tính dòng nhật ký ghi trước lúc bundle chốt.** Sau luật này,
cổng kiểm đạt **180/180**.

| Kịch bản | Trúng | So mốc | Lãi/lỗ | So mốc |
|---|---|---|---|---|
| 0 · hiện tại | 28,9% | — | −96,5tr | — |
| 1 · tắt V10640 cho MB+MT | 31,7% | +2,8pp | −57,3tr | +39,2tr |
| **2 · tắt 5 lớp, giữ V10640 MN** | **35,6%** | **+6,7pp** | **−23,0tr** | **+73,5tr** |
| 3 · tắt tất cả, phiếu bầu thuần | 34,4% | +5,5pp | −37,7tr | +58,8tr |
| 4 · tắt 2 lớp luồng test | 30,0% | +1,1pp | −81,8tr | +14,7tr |
| 5 · tắt 2 lớp MB | 30,0% | +1,1pp | −86,7tr | +9,8tr |
| 6 · chỉ tắt V10640 MB | 30,6% | +1,7pp | −81,8tr | +14,7tr |
| 7 · chỉ tắt V10640 MT | 30,0% | +1,1pp | −72,0tr | +24,5tr |

Kịch bản 2, chi tiết theo miền: MN 40,0% (−22,2tr) · MT 35,0% (−12,9tr) · MB **31,7% (+12,1tr)**.

---

## 5. Ba phép kiểm chắc chắn — đều đạt

| Phép kiểm | Kết quả | Đạt? |
|---|---|---|
| **McNemar** (so từng ngày, dữ liệu ghép cặp) | 15 ngày kịch bản 2 thắng / 3 ngày thua · **p = 0,0075** | ✓ |
| **Bootstrap** bốc lại 60 ngày 20.000 lần | thắng **99,9%** · trung vị +73,5tr · khoảng 95% **[+29,4tr, +122,5tr]** | ✓ |
| **Chia đôi thời gian** | tháng 6: −37,0 → −2,8tr · tháng 7: −59,5 → −20,2tr | ✓ cùng chiều |

Chia đôi theo miền (kiểm chéo): MN giống hệt ở cả hai nửa (đúng — lớp MN giữ nguyên ở cả hai kịch
bản, đây là phép kiểm tự đối chứng). MT và MB đều cải thiện ở cả hai nửa.

---

## 6. Đã làm

| Việc | Chi tiết |
|---|---|
| `_v10640_official_perslice_override.py` | MT `enabled=False` · MB `enabled=False` · **MN giữ `True`** |
| `_v10767_mb_prevday_override.py` | `_V10767_MB_PREVDAY_ENABLED = False` |
| `_v10789_mb_lane_promote.py` | `_V10789_MB_LANE_PROMOTE_ENABLED = False` |
| `_v10790_mt_lane_promote.py` | `_V10790_MT_LANE_PROMOTE_ENABLED = False` |
| Backup | `backups/v10917_pre/` — bản VPS trước khi sửa |
| Deploy | service `lottery`, PID `503462 → 547411 → 547740`, health 200, admin 401, journal 0 lỗi |
| Hash 4 bảng khoá | `predictions` · `final_bundles` · `lottery_results` · `model_daily_eval` — **GIỮ NGUYÊN** |
| Gỡ về | `python web/backend/_v10917_deploy.py --rollback` |

### Bẫy suýt sập khi deploy

Lần đầu dùng tên `lottery-ai` → `systemctl` báo *"Unit not found"* nhưng `/api/health` vẫn trả
**200** vì tiến trình cũ còn sống, và bước đọc cờ vẫn thấy đúng vì nó đọc từ đĩa chứ không từ
tiến trình đang chạy. Suýt kết luận "deploy xong" trong khi code mới **chưa hề chạy**.

Đã thêm **so PID trước/sau** làm cổng bắt buộc trong script deploy. Tên đúng: **`lottery`**.

---

## 7. V10918 — bảng canh, để lỗi này không âm ỉ lần nữa

Lỗi này sống nhiều tháng vì **không có chỗ nào đối chiếu** số phiếu bầu với số công bố.

- API: `/api/admin/override-watch` (`require_admin`, `Cache-Control: no-store`)
- UI: panel `/monitoring` viền đỏ, làm mới 60 giây, đăng ký trong `loadAllSections()` + `setInterval`
- Nội dung: mỗi ngày × mỗi miền, số phiếu bầu và số công bố nằm cạnh nhau, kèm ai trúng ai trượt;
  trạng thái **thật** của cả 6 cờ (bắt trường hợp có người bật lại mà quên báo); tự canh ngưỡng
  30 ngày cho lớp MN

---

## 8. Ba điều nói thẳng

**Một — vẫn lỗ.** Ngay cả phương án tốt nhất vẫn **−23,0tr/60 ngày**. Đây là bớt chảy máu, chưa
phải hệ thống có lãi. Chỉ miền Bắc thành có lãi.

**Hai — lớp MN chưa được chứng minh.** Giữ vì +14,7tr là phương án đo được tốt nhất, **không phải
vì đã chứng minh** (p = 0,754). Ngưỡng đã ghi thành văn bản: rà **31/08**, nếu âm tiền thì tắt
nốt, không hỏi lại (FU-183).

**Ba — rủi ro chọn trúng cái hợp số cũ.** Kịch bản 2 được chọn sau khi xem 8 kịch bản trên cùng
bộ dữ liệu. Phép chia đôi thời gian là để soi đúng rủi ro đó và nó vẫn đạt, nhưng đây là hạn chế
thật của phép đo.

---

## 9. Bài học: đừng tin backtest

Lịch sử `_v10640_official_perslice_override.py` là một chu kỳ lặp:

| Phiên bản | Backtest lúc ký | Kết cục |
|---|---|---|
| V10655 (31/05) | MT +11–15pp · MB +18–22pp | rữa |
| V10672 (02/06) | MN 90d 48% vs 45% | rữa |
| V10677 (02/06) | MB 30d 23% vs 10% | rữa |
| V10753 (26/06) | MN +7,8pp · MB +7,5pp "robust cả 4 cửa sổ" | **đo tiến: MB −29,4tr** |
| V10789 (09/07) | "+32,9M cả 2 nửa vs official −5,2M" | **đo tiến: −4,9tr** |
| V10790 (09/07) | "60d BT 38% vs official 30%" | **đo tiến: −9,8tr** |

Chính comment trong file đã ghi *"d_w06 had DECAYED to baseline-level"* — tức chu kỳ này đã lặp
ít nhất một lần trước đó mà không ai rút ra luật.

**Luật mới ghi thẳng vào cả 4 file:** *đừng bật lại bằng backtest, chỉ bằng đo tiến.*

---

## 10. Theo dõi tiếp

| Mã | Việc | Hạn |
|---|---|---|
| **FU-183** | Lớp V10640·MN: rà 31/08, âm tiền thì tắt nốt (panel tự kết luận) | 31/08 |
| **FU-184** | Xác minh live: MT/MB phải có phiếu bầu = số công bố **100%** số ngày | 02/08 |
| **FU-185** | Tinh gọn lane hết hạn đo: V10707 (quá 7 tuần), V10781 (quá 2,5 tuần), V10692, V10679/V10680, V10637 | 03/08 |

---

## 11. Bằng chứng

| Tệp | Nội dung |
|---|---|
| `evidence/v10913_override.json` | so số thắng phiếu vs số công bố, 180 lượt |
| `evidence/v10913_layers.json` | tách theo cửa sổ ngày từng lớp được bật |
| `evidence/v10914_per_layer.json` | chấm từng lớp bằng nhật ký champion/challenger |
| `evidence/v10915_chain.json` | mô phỏng nguyên chuỗi, 8 kịch bản, cổng kiểm 180/180 |
| `evidence/v10916_significance.json` | McNemar, bootstrap 20k, chia đôi thời gian |

Mã nguồn phép đo nằm ở repo riêng: `web/backend/_v10913_*.py` … `_v10916_significance.py`.
