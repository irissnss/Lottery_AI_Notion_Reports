# V10884 — Nghiệm thu 30/07 và ba lỗi gốc của luồng thứ 5

**Ngày:** 31/07/2026 · **Trạng thái:** đã sửa gốc, đã deploy, đã xác minh

---

## 1. Owner nói gì

> *"hãy tiến hành nghiệm thu ngày hôm qua 30/07 và kiểm tra toàn diện ngày hôm nay 31/07 nha em. chứ sơ sơ anh thấy là hôm qua quá tệ, hôm nay thì /nghiem-thu ko có output nha em ==> kiểm tra tổng lực toàn diện 3 miền 5 luồng luôn"* — 31/07 09:17

Owner đúng cả hai chỗ. Đào ra thì lỗi nặng hơn vẻ ngoài.

---

## 2. Ba lỗi gốc — đều xuất phát từ việc luồng chạy sai giờ

### Lỗi 1 — chạy quá sớm

Lịch cũ MN 15:52 · MT 17:01 · MB 18:01. Em đặt theo lane de-herd chứ không theo giờ chốt thật của official.

Đo 7 ngày liền:

| | Official chốt | Xổ |
|---|---|---|
| MN | 04:17 | 16:36 |
| MT | 16:39 | 17:30 |
| MB | 17:33 | 18:31 |

Official MN có số từ 04:17 mà luồng tới 15:52 mới chạy. Nên sáng nào mở `/nghiem-thu` cũng trống — đúng như owner thấy.

### Lỗi 2 — chốt bừa khi kho model chưa đủ

Sáng 30/07 lúc 09:41 luồng chạy cả ba miền. Kiểm lại kho dự đoán tại thời điểm đó:

- **MB: không có một dòng nào.** Cả 26 dòng dự đoán MB của ngày 30/07 đều do `rerun_post_mt` ghi lúc 17:30. Vậy mà luồng vẫn ra `43`, với `model_count=7` — tức nó vơ lấy mấy model chạy sớm rồi chốt.
- **MT: chỉ 7 dòng**, trong khi official dùng đủ 15.

### Lỗi 3 — chấm một con số khác con đã công bố

Lúc chấm 21:16, luồng **tính lại** thay vì đọc con đã công bố. Khi đó kho model đã đủ 15 nên ra kết quả khác:

| Miền | Công bố 09:41 | Đem chấm 21:16 | |
|---|---|---|---|
| MN | `86` (15 model) | `86` | khớp — official đã chốt từ 04:17 nên kho đủ |
| MT | `20` (7 model) | `02` (15 model) | **lệch** |
| MB | `43` (7 model) | `86` (15 model) | **lệch** |

Luồng công bố một đằng, tự chấm một nẻo. Đây đúng là bệnh *"số cứ giao động"* owner đã than từ lâu — lần này do chính em tạo ra.

---

## 3. Cách sửa

**Cổng chặn.** Luồng chỉ được chạy khi official **đã chốt** miền đó, VÀ kho model đạt bằng `model_count` của official. Lấy chính bundle official làm tín hiệu: official chốt xong nghĩa là kho dự đoán đã đủ. Chờ tín hiệu này thì luồng nhìn đúng thứ official nhìn tại đúng thời điểm đó — vừa hết trôi số, vừa thành phép so công bằng.

**Đóng băng.** Số chốt xong ghi một lần, gọi lại không ghi đè. Đã kiểm: gọi `run_predraw` ba lần liên tiếp, số không đổi.

**Chấm đúng con đã công bố.** Tách hẳn `--predraw` và `--settle`. Lúc chấm đọc lại dòng đã đóng băng, tuyệt đối không tính lại.

**Lịch mới bám giờ chốt official:**

| | Chốt số | Chấm điểm |
|---|---|---|
| MN | 04:25 | 17:10 |
| MT | 16:50 | 18:10 |
| MB | 17:45 | 19:10 |

---

## 4. Nghiệm thu 30/07

### Official cả 3 miền: bạch thủ 1/3

| Miền | Bạch thủ | |
|---|---|---|
| MB | `75` | **TRÚNG** |
| MN | `86` | trượt |
| MT | `20` | trượt |

Owner nói "quá tệ" là đúng.

### Luồng mới: chỉ MN so được

Hai dòng MT và MB đã **huỷ khỏi bảng điểm và khỏi lane**, vì số công bố tính từ 7/15 model, không đạt chuẩn mới. Giữ lại thì làm bẩn cả kỳ nghiệm thu.

| MN 30/07 | Bản mới | Official |
|---|---|---|
| Bạch thủ | `86` trượt | `86` trượt |
| Lô 2 | `86-84` **1/2** | `86-31` trượt |
| Lô 3 càng | `086` trượt | `086` trượt |
| Xiên 2 | `86-84` trượt | `86-31` trượt |

Cùng bạch thủ, bản mới hơn ở lô 2. Một miền-ngày thì chưa nói lên điều gì.

### Hệ quả

Kỳ nghiệm thu coi như **bắt đầu lại từ 31/07**. Mốc chốt sớm nhất dời **05/08 → 06/08**. Hạn chót 19/08 giữ nguyên.

---

## 5. Hôm nay 31/07 — 3 miền × 5 luồng

| | MN | MT | MB |
|---|---|---|---|
| 1 · official | `BT=09` `lo2=09-64` `lo3=909`, 15 model, 04:17 | chưa chốt (~16:39) | chưa chốt (~17:33) |
| 2 · K-lane | 21 lane | chờ | chờ |
| 3 · Total V2/V3 | chưa có | chờ | chờ |
| 4 · `/choi` | `["09"]` | chờ | chờ |
| 5 · Nghiệm Thu | **`BT=09`** `lo2=09-64` `lo3=909` | chờ cổng mở | chờ cổng mở |
| Model chạy | 26, **0 rỗng** | 7, 0 rỗng | 7, 0 rỗng |

MN hôm nay bản mới và official **ra cùng một bạch thủ**. MT và MB trống là **đúng** — official chưa chốt thì cổng chưa mở, không phải hỏng.

---

## 6. Hai model cao cấp mới — bản sửa V10880 đã ăn

| Model | 30/07 MT | 30/07 MB | 31/07 MN |
|---|---|---|---|
| `claude-opus-5-fast` | ✅ `34-02` | ✅ `32-75` | ✅ `64-95` |
| `gpt-5.6-sol-pro` | ✅ `02-34` | ✅ `75-52` | ✅ `64-09` |
| `gemini-3.5-flash` | ✅ `83-02` | ❌ 503 | ✅ `64-95` |

Hai model mới chạy sạch từ lúc sửa định tuyến. `gemini-3.5-flash` rớt thêm một lần do Google 503 — vấn đề phía nhà cung cấp.

---

## 7. An toàn

Hash 4 bảng official trước/sau **giống hệt**. `V10841_CONTRACT_PASS`. Ổ cắm vào official vẫn **TẮT** cả 3 miền. Chỉ đụng bảng đo lường và lane test; không chạm `final_bundles`, `/choi`, hay bộ chọn official.

---

## 8. Bài học ghi lại

Một lane chạy song song official **phải lấy tín hiệu từ official**, không được tự đặt giờ. Và **số đã công bố là bất biến** — lúc chấm phải đọc lại đúng con đó, không bao giờ tính lại.
