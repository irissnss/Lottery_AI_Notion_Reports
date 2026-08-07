# REPORT V11023 — ĐÍNH CHÍNH BA CON SỐ AGENT BÁO SAI

> **Ngày:** 2026-08-07 đêm · **Owner nghi ba chỗ — cả ba đều là agent báo sai**
> Không deploy runtime. Sửa hai cổng kiểm + dựng một cổng mới.

---

## 1. Tóm tắt

Owner đọc báo cáo kiểm tổng lực và nghi ba chỗ. Kiểm lại: **cả ba đều đúng là agent sai**.

| agent báo | sự thật |
|---|---|
| «lane MB 17:38 chấm thiếu model, **sai 4/7 ngày**» | **KHÔNG SAI** — lane có **5 lượt** tới `17:54`, hạn `17:58` |
| «C4 khoá /choi **rỗng** · C5 trang web **hiện sai giờ**» | **KHÔNG HỎNG** — chạy trên VPS: **20 đạt / 2 lệch**, C4 và C5 sạch |
| «cặp khối trùng **10 → 4**» | **KHÔNG TÁI LẬP** — thật là MB **14→10** · MT **9→3** · **MN 1→2 (tệ hơn)** |

**Nguyên nhân chung: đo bằng nguồn sai.** Đọc một dòng cron thay vì liệt kê hết · đọc crontab
**local** trong khi cron ở **VPS** · đo trên DB **trước** khi đồng bộ.

## 2. Owner yêu cầu gì (nguyên văn)

> *"FU312 là gì sao để sai vậy anh đã nói output tối đa của MB là 17h58 rồi mà em, **Đủ thời
> gian cho các model Ai chạy song song 5 model 1 lượt mà em.**"*

> *"C4-C5 **xử lý dứt điểm** dùm đi"*

> *"FU215 em phải **kiểm tra xác thực rõ ràng từ số liệu** chứ sao anh chốt được."*

> *"FU 290 thì trước mắt **vẫn chưa cắt**… cần model AI hiểu ngữ cảnh, và thông minh để chạy
> shadow đo là chọn lựa **thay thế** các model tệ… **Các model cao cấp nhất ah em có thinking**"*

> *"FU328 đơn giản em canh và tự xử lý nha"*

> *"em thử sao anh chỉ có xử lý MB thôi ah em và em chưa tổng hợp lại hoàn hảo và nhất quán"*

## 3. Đào bới / phát hiện

### 3.1 FU-312 — lane có NĂM lượt, không phải một · `VERIFIED_TEST`

```
crontab VPS — _v10879_nghiemthu_lane --predraw --region MB
  17:38 · 17:42 · 17:46 · 17:50 · 17:54          hạn official 17:58
```

Lượt cuối cách hạn cứng **4 phút**. Lane chỉ mở khi official đã chốt (`_official_closed_at` đọc
`final_bundles`), nên official xong `17:45` thì lượt `17:46` bắt được.

**Agent đọc một dòng `17:38` rồi kết luận cả cơ chế.** Owner nói đúng.

### 3.2 C4 · C5 — cổng MÙ, không phải hệ hỏng · `VERIFIED_TEST`

`_v10900_consistency_guard._crontab()` chạy `crontab -l` **trên máy đang chạy**. Cron nằm ở
**VPS**. Chạy local ⇒ `jobs` **rỗng** ⇒ C4 · C5 · C6 đều báo LỆCH.

Chạy đúng trên VPS:

```
BO TU KIEM CHAY TREN VPS: {'OK': 20, 'LỆCH': 2}
   LỆCH C18_bien_lane_du_rong    (biên MT 04/08 mỏng — cũ, đã theo dõi)
   LỆCH C19_bien_han_du_rong     (như trên)
```

**C4 và C5 SẠCH.** Bằng chứng trực tiếp:

| | |
|---|---|
| `_v10834_lock_freeze` trong crontab VPS | **15:43 · 16:56 · 17:56** — đúng y `LOCK_TARGET` mong đợi |
| `LANE_SCHEDULE` khai báo | MN `06:05` · MT `16:44` · MB `17:38` — **khớp crontab từng phút** |

### 3.3 «10 → 4» không tái lập · `VERIFIED_TEST`

Con số đó đo trên DB **trước** lượt đồng bộ 18:50. Đo lại **bốn bản × ba miền** trên **cùng một
nền dữ liệu mới** — đây là bảng chuẩn, thay cho mọi con số cũ:

| chỉ số | V11013 | V11014 | V11016 | **V11022 (nay)** |
|---|---|---|---|---|
| **mệnh lệnh** MB/MT/MN | 7/6/7 | **1/1/1** | 1/1/1 | **1/1/1** |
| cặp khối trùng ≥60% · MB | 16 | 14 | 10 | **10** |
| · MT | 12 | 9 | 3 | **3** |
| · MN | 2 | 1 | 2 | **2** |
| ký tự MB | 12.659 | 11.594 | 12.911 | **12.497** |
| số hai chữ số MB | 318 | 288 | 280 | **280** |

**Thành quả chắc chắn nhất: mệnh lệnh 6–7 → 1** ở **cả ba miền**, từ V11014.
Trùng lặp giảm mạnh ở MT (9→3), giảm vừa ở MB (14→10), **không giảm ở MN (1→2)**.

### 3.4 FU-215 — số liệu owner cần để chốt · `VERIFIED_TEST`

QD-014 nguyên văn: *"Có. Hôm qua đổi ba thứ cùng lúc, **cần một tuần yên** để biết chúng có tác
dụng gì không."*

⇒ Câu hỏi thật **không phải** «gia hạn hay không» mà **«tuần yên đó có xảy ra không»**.

| ngày giờ | phiên bản đổi `gpt_analyzer.py` |
|---|---|
| 06/08 19:52 | V11001 — gỡ gan/nóng/lạnh |
| 06/08 21:44 | V11007 — gỡ nốt 10 chỗ sót |
| 06/08 22:12 | V11008 — xoá CP-7.9 |
| 07/08 11:01 | V11014 — thôi ép chọn |
| 07/08 13:41 | V11016 — số thành lời kể |
| 07/08 19:41 | V11022 — gỡ ngưỡng tự quyết |

**SÁU lần trong BẢY ngày đóng băng.** Tuần yên **chưa từng xảy ra**.

## 4. Hướng xử lý và vì sao chọn

**C4/C5 — sửa dứt điểm bằng cách cho cổng BIẾT IM.** Cổng không đọc được crontab thì **không đo
và không báo lệch**, in rõ *"chạy trên VPS mới đo đủ"*. Cổng mù mà vẫn phán còn nguy hiểm hơn
cổng không chạy — nó tiêu niềm tin và đẩy người ta đi sửa thứ không hỏng.

**FU-215 — trình HAI lựa chọn kèm số, không tự quyết.** Owner nói *"em phải kiểm tra xác thực rõ
ràng từ số liệu chứ sao anh chốt được"* — nên agent đưa số, owner chốt.

**FU-290 — đổi hẳn hướng theo owner.** Từ «cắt model yếu» sang «**thử model mạnh có thinking ở
shadow để THAY model yếu**». Theo §59 đây là **thêm ứng viên vào shadow**, không phải «bỏ cờ»
cũng không phải «dừng hẳn» ⇒ sàn pool ML≥4 · AI≥3 không bị đụng.

## 5. Đã làm gì

| việc | kết quả |
|---|---|
| Sửa `_v10900_consistency_guard` | không đọc được crontab ⇒ **bỏ qua** C4·C5·C6, không báo lệch |
| Dựng `_v11023_canh_thieu_so.py` (FU-328) | ngưỡng **≥1 model RỖNG** hoặc **≥3 model ra 1 số** ⇒ ĐỎ |
| Đo lại prompt **4 bản × 3 miền** | bảng chuẩn thay mọi con số cũ |
| Đếm lần đổi prompt trong cửa sổ đóng băng | **6 lần / 7 ngày** |
| Đóng FU-312 | `CLOSED_NO_DEFECT` |
| Đổi hướng FU-290 | `SCOPE_CHANGED`, hạn 14/08 |

## 6. Cổng kiểm

| phép | kết quả |
|---|---|
| Bộ tự kiểm **trên VPS** | **20 đạt / 2 lệch** (C18·C19 — biên MT 04/08, cũ) |
| Bộ tự kiểm **local sau khi sửa** | **18 đạt / 2 lệch**, bỏ qua 3 phép cần cron, **không bịa** |
| Cổng thiếu số — `07/08` | **ĐỎ**, mã thoát 1 · bắt đúng deepseek RỖNG ở MT |
| Cổng thiếu số — `06/08` | **XANH**, mã thoát 0 · 48/48 lượt đủ 2 số |
| Cổng cắt cụt · ghi tệp · đoán tên | ✓ cả ba đạt |
| J5 mốc tải | ✓ khớp sổ thật |
| 4 bảng khoá | **không đụng** — phiên này không deploy runtime |

## 7. Vướng vấp

**Ba lần báo sai trong một báo cáo, cùng một kiểu lỗi: đo bằng nguồn sai.**

| # | đo bằng gì | lẽ ra phải đo bằng gì |
|---|---|---|
| 1 | một dòng cron `17:38` | **liệt kê hết** các lượt của lane |
| 2 | `crontab -l` trên **máy local** | crontab **trên VPS** |
| 3 | DB **trước** khi đồng bộ | DB **sau** khi đồng bộ |

Và điều tệ hơn cả ba: agent **đưa cả ba vào báo cáo cho owner như sự thật đã kiểm chứng**, kèm
đề xuất đi sửa thứ không hỏng. Nếu owner không nghi thì agent đã dời lane MB — một cơ chế đang
chạy đúng.

## 8. Gỡ về

Phiên này **không deploy runtime**, 4 bảng khoá không đụng. Muốn hoàn tác:

```bash
git checkout HEAD~1 -- web/backend/_v10900_consistency_guard.py   # cổng tự kiểm
rm web/backend/_v11023_canh_thieu_so.py                            # cổng thiếu số
```

## 9. Theo dõi tiếp

| Mã | Nội dung | Trạng thái | Hạn |
|---|---|---|---|
| **FU-312** | Lane MB — **không có lỗi** | **`CLOSED_NO_DEFECT`** | đóng |
| **FU-329** | Cổng mù mà vẫn phán — **đã sửa** | `CLOSED_PASS` | đóng |
| **FU-328** | Cổng canh thiếu số — **đã dựng**, còn gắn cron + panel | `DONE_LOCAL` | 08/08 |
| **FU-215** | **Có số rồi — owner chốt** | `OWNER_DECISION_NEEDED` | **08/08** |
| **FU-290** | **Đổi hướng** — thử model thinking ở shadow | `SCOPE_CHANGED` | 14/08 |
| **FU-325** | Lượt đo bầy đàn sạch | `WAIT_LIVE` | 10/08 |

### FU-215 — hai lựa chọn, owner chốt

| | nội dung | hệ quả |
|---|---|---|
| **(A)** | Đóng QD-014 «mục tiêu không đạt» + mở **cửa sổ yên MỚI 08/08 → 10/08** | Trùng luôn với phép đo bầy đàn đang cần 3 ngày sạch. Được cả hai việc trong một cửa sổ |
| **(B)** | Gia hạn QD-014 | Chỉ có nghĩa nếu **thật sự** không đổi gì nữa — bảy ngày vừa rồi đã chứng minh điều đó khó |

**Agent nghiêng về (A)** vì nó gắn cửa sổ yên vào một phép đo cụ thể có ngày chốt, thay vì một
lời hứa chung chung.

### FU-290 — nhóm model yếu đã đo được (30 ngày, MB)

`random-forest` **23%** · `combo-no-token` **26%** · `smart-ml` 29% · `gpt-oss-120b` 29% ·
`gpt-5-mini` 29% · `lstm` 32% · `combo-super` 32%.

Nhóm đều tay: `claude-sonnet-4-6` 48/48/**81** · `claude-opus-4-6` 45/58/71 ·
`deepseek-reasoner` 48/58/68 · `gemini-2.5-pro` 52/58/61.

**Việc tiếp:** chọn danh sách model **thinking** ứng viên → dựng lane shadow → đo ≥14 ngày →
chỉ thay khi hơn nhóm yếu rõ rệt.
