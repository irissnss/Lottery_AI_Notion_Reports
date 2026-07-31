# V10884 — Nghiệm thu 30/07 + ba lỗi gốc của luồng thứ 5

**31/07/2026 · đã sửa gốc, đã deploy, đã xác minh**

Owner: *"nghiệm thu ngày hôm qua 30/07... hôm qua quá tệ, hôm nay thì /nghiem-thu ko có output... kiểm tra tổng lực toàn diện 3 miền 5 luồng"*

## Ba lỗi gốc — đều do luồng chạy sai giờ

**1. Chạy quá sớm.** Lịch cũ MN 15:52 · MT 17:01 · MB 18:01 đặt theo lane de-herd. Đo 7 ngày: official chốt **MN 04:17 · MT 16:39 · MB 17:33**. Nên sáng nào `/nghiem-thu` cũng trống.

**2. Chốt bừa khi kho model chưa đủ.** 30/07 lúc 09:41: MB **chưa có một dòng dự đoán nào** (26 dòng do `rerun_post_mt` ghi lúc 17:30) mà luồng vẫn ra `43` từ 7 model. MT ra `20` từ 7/15 model.

**3. Chấm con khác con đã công bố.** Settle 21:16 tính lại với 15 model: MB thành `86`, MT thành `02`. Công bố một đằng chấm một nẻo — đúng bệnh "số cứ giao động".

| Miền | Công bố | Đem chấm | |
|---|---|---|---|
| MN | 86 | 86 | khớp |
| MT | 20 | 02 | **lệch** |
| MB | 43 | 86 | **lệch** |

## Cách sửa

Cổng chỉ mở khi **official đã chốt** miền đó VÀ pool ≥ `model_count` của official · số chốt xong **đóng băng** (kiểm 3 lần, không đổi) · settle **đọc dòng đã công bố**, không tính lại · lịch mới: chốt MN 04:25 · MT 16:50 · MB 17:45, chấm 17:10 · 18:10 · 19:10.

## Nghiệm thu 30/07

**Official cả 3 miền: bạch thủ 1/3** — MB `75` TRÚNG, MN `86` trượt, MT `20` trượt. Owner nói "quá tệ" là đúng.

**Luồng mới: chỉ MN so được.** MT/MB **đã huỷ** vì số công bố tính từ 7/15 model.

| MN | Bản mới | Official |
|---|---|---|
| Bạch thủ | `86` trượt | `86` trượt |
| Lô 2 | `86-84` **1/2** | `86-31` trượt |

Kỳ nghiệm thu **bắt đầu lại từ 31/07**. Sớm nhất chốt **05/08 → 06/08**, hạn chót 19/08 giữ nguyên.

## Hôm nay 31/07 — 3 miền × 5 luồng

MN: official `BT=09` (15 model, 04:17) · Nghiệm Thu **`BT=09` trùng official** · `/choi` `["09"]` · 21 K-lane · 26 model chạy, **0 rỗng**.
MT/MB: official chưa chốt (đúng lịch), luồng chờ cổng mở — **trống là đúng, không phải hỏng**.

## Hai model cao cấp — bản sửa V10880 đã ăn

`claude-opus-5-fast` và `gpt-5.6-sol-pro` ra số sạch ở 30/07 MT, 30/07 MB và 31/07 MN. `gemini-3.5-flash` rớt thêm 1 lần do Google 503.

## An toàn

Hash 4 bảng official pre/post IDENTICAL. V10841 PASS. Ổ cắm vào official vẫn TẮT cả 3 miền.

## Bài học

Lane chạy song song official **phải lấy tín hiệu từ official**, không tự đặt giờ. Và **số đã công bố là bất biến** — chấm phải đọc lại đúng con đó.

Báo cáo đầy đủ: `V10884_ACCEPTANCE_AND_LANE_ROOTFIX_20260731/REPORT_V10884.md`
