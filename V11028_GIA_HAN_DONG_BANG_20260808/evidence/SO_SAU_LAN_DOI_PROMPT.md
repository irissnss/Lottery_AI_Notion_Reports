# SỔ SÁU LẦN ĐỔI PROMPT — cửa sổ đóng băng QD-014 (02/08 → 08/08)

> **Lập 2026-08-08 (V11028)** — owner hỏi: *"không rõ em còn lưu trữ và nắm rõ các lần em đã làm
> gì chứ?"*
>
> Đây là câu trả lời bằng **bằng chứng**, không bằng trí nhớ. Mọi dòng dưới đây tái lập được
> bằng `git log` + `md5sum`.

---

## Sáu lần đổi — commit · md5 · gỡ về được tới đâu

| # | Lúc | Commit | Phiên bản prompt | md5 `gpt_analyzer.py` | Bản sao lưu để gỡ về |
|---|---|---|---|---|---|
| 1 | 06/08 19:52 | `381d9da` | `SP-4.2 · CTX-16.6 · PB-18.2` | `1e9df12c5ee25901b738d2b1d5a6333e` | `backups/v11001_pre/` md5 `862ce620…` |
| 2 | 06/08 21:44 | `38fe600` | `SP-4.3 · CTX-16.7 · PB-18.3` | `50f99eb82ce4dbc5497bb51e2c2d5eb6` | `backups/v11007_pre/` md5 `d87956d1…` |
| 3 | 06/08 22:12 | `bf910d6` | `SP-4.3 · CTX-16.7 · PB-18.4` | `5eb260812641125669bc921eb16dc680` | `backups/v11008_pre/` md5 `c028047b…` |
| 4 | 07/08 11:01 | `9510886` | `SP-4.4 · CTX-17.0 · PB-19.0` | `11bef4ecca4c81360a10405e3c7f7d72` | `backups/v11014_pre/` md5 `a20dbb16…` |
| 5 | 07/08 13:41 | `e69c44c` | `SP-4.4 · CTX-18.0 · PB-20.0` | `96f6073cadafa73fb1542fe6e9c8e0b6` | `backups/v11016_pre/` md5 `f8b428ec…` |
| 6 | 07/08 19:41 | `7ec3cc3` | `SP-4.4 · CTX-18.1 · PB-20.1` | `6b28f0baa7aeceac0e9fd2b75a741a81` | `backups/v11022_pre/` md5 `96f6073c…` |

**Bản đang chạy trên VPS:** `PB-20.1` · md5 `6b28f0baa7aeceac0e9fd2b75a741a81`.

## Mỗi lần đổi cái gì — và ai bảo đổi

| # | Bản | Đổi gì | Ai bảo | Còn giữ hay đã gỡ |
|---|---|---|---|---|
| 1 | **V11001** | Gỡ **hết** gan/nóng/lạnh khỏi prompt | owner ký | **giữ** — nhưng V11024 phát hiện **chưa gỡ hết** (xem dưới) |
| 2 | **V11007** | Gỡ **nốt 10 chỗ sót** của V11001 + ký §60 *"cấm bỏ nửa chừng"* | agent tự soi ra | **giữ** |
| 3 | **V11008** | Xoá hẳn `CP-7.9` + đồng bộ trạng thái | agent | **giữ** |
| 4 | **V11014** | Prompt **trình bằng chứng** thay vì **ép chọn** — bỏ `BẮT BUỘC chọn từ DANH SÁCH` | owner giao 06/08 | **giữ** |
| 5 | **V11016** | **L-A** số thành lời kể · **L-B** ngưỡng tự quyết | owner *"làm ngay"* | L-A **giữ** · **L-B ĐÃ GỠ** |
| 6 | **V11022** | **Gỡ L-B** — nó đóng cửa số phụ | owner chỉ ra *"phụ 2 có tín hiệu trúng kìa"* | **giữ** |

## Ba việc trong sáu lần đó CHƯA XONG — ghi để không quên

| việc | tình trạng | mã |
|---|---|---|
| **V11001 chưa gỡ hết gan/hot.** `statistical_analyzer.format_condensed_stats` **vẫn sinh** `TOP 5 GỢI Ý (Score/Zone/Trend/Gan)` + `⏳ GAN CAO` + `🔥 HOT`, và `gpt_analyzer.py:2229` **vẫn bơm** khi `prediction_mode=='HYBRID'` | **CHỜ 21/08** — đổi prompt, bị QD-041 đóng băng | A3 |
| **`WEEKDAY SCAN` chết** — `gpt_analyzer.py:5372` SELECT cột `predicted_numbers` không tồn tại (cột thật `main_numbers`); prompt in thẳng `⚠️ SP-4.0 scan error` cho model đọc | **CHỜ 21/08** — đổi prompt | A4 |
| **Hai con số M4 trong prompt không tái lập được** — `z = −0,33 / +0,26` tính từ **9 và 15 cặp lệch**, bảng gốc đã bị lần đồng bộ 18:51 xoá | dựng lại phép đo **được** (shadow); sửa số **trong prompt** thì chờ 21/08 | A6 |

## Hệ quả cho phép đo

**FU-284 đang đo GỘP** — không tách được nhân quả giữa sáu thay đổi. Ngày sạch đầu tiên là
**08/08**; cửa sổ 08/08 → 21/08 vừa đúng 14 ngày, **với điều kiện không đổi prompt lần thứ bảy**.
Đó chính là lý do **QD-041** mở rộng phạm vi đóng băng sang `gpt_analyzer.py`.

Và **R9 đo được**: cửa sổ 14 ngày **không đủ sức** cho ngưỡng *"tụt ≥5 điểm"* mà FU-284 khai —
với VIF 2,92× thì 14 ngày chỉ phát hiện được chênh **≥8,76 điểm**; muốn thấy 5 điểm cần
**44,1 ngày**. Cửa sổ 14 ngày vẫn có giá trị nhưng là **cái phanh an toàn**, không phải phép
chứng minh.

## Lệnh tái lập sổ này

```bash
git log --since=2026-08-06 --format='%h|%ad|%s' --date=format:'%d/%m %H:%M' \
  -- web/backend/gpt_analyzer.py
md5sum backups/*/gpt_analyzer.py.pre
```
