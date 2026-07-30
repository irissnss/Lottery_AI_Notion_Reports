# V10879 — Luồng "Nghiệm Thu 19/08" chạy live song song

**Ngày:** 30/07/2026 · **Trạng thái:** đã deploy, đang chạy thật · **Ngày chốt:** 19/08/2026

---

## 1. Owner nói gì

> *"Vấn đề anh quên là thay vì đợi 19/08 sao em không làm 1 luồng mới với tên Nghiệm Thu 19/08 để anh xem so sánh trực quan cũng như là live song song luồng Nghiệm Thu 19/08 với các luồng khác luôn em. Ok thì mình áp vào offical cũng nhanh chóng hơn ah em."* — 30/07 09:32

## 2. Vì sao cách cũ hỏng

Mười hạng mục đã đo xong (V10871 → V10878) đều xếp hàng chờ tới 19/08 mới đem ra quyết. Nhưng tới hôm đó thì trong tay vẫn chỉ có **bằng chứng backfill**, chưa có một ngày chạy thật nào. Nghĩa là 19/08 sẽ không phải ngày quyết — nó lại là ngày *bắt đầu* một kỳ đo mới, trễ thêm ba tuần nữa.

Owner chỉ ra đúng chỗ: gộp tất cả lại thành một phương án và cho chạy thật ngay từ hôm nay thì tới 19/08 đã có sẵn khoảng 21 ngày forward để áp thẳng vào official.

## 3. Cấu hình — đóng băng từ 30/07

Không sửa giữa kỳ. Đổi cấu hình giữa chừng thì mất luôn ý nghĩa của kỳ nghiệm thu.

| Thành phần | Chốt | Căn cứ |
|---|---|---|
| Bộ chọn số | de-herd family-√ | V10872: +7,9pp trên 267 ngày, McNemar p≈0,0035; thắng cả 15 phương án ở bake-off V10874 |
| Số mỗi miền | **1 số** | Cùng vốn, một số luôn hơn song thủ ở chuẩn 1/1 |
| Đài đặt | MN 2 · MT 1 · MB 1 | V10876: chọn đài theo phong độ là chỗ chữa bệnh chi phí lớn nhất |
| Phong độ đài | cửa sổ mở rộng ≤120 ngày, tối thiểu 5 mẫu | mỗi đài MN chỉ xổ 1 lần/tuần |
| Vốn | 50 điểm | |
| Chấm tiền | 1/1 quyết định · có nháy chỉ là may | Owner lock 30/07 |

### Một sai lệch đã sửa trong lúc dựng

Bản đầu em viết cửa sổ trượt 21 ngày. Nhưng con số MT +36,1% ở V10876 lại đo bằng cửa sổ mở rộng — hai thứ khác nhau. Để nguyên thì code không khớp với bằng chứng đã dùng để chọn cấu hình. Cửa sổ 21 ngày còn có lỗi thực tế: mỗi đài MN chỉ xổ một lần mỗi tuần nên 21 ngày chỉ cho khoảng 3 mẫu — quá ít để xếp hạng đài. Đã đổi sang cửa sổ mở rộng; MT lên đúng dải đã đo (+33,1% trên cửa sổ ngắn hơn).

## 4. Đối chứng lịch sử 15/06 – 29/07

135 miền-ngày · 182,2 triệu vốn · chuẩn 1/1

| Phạm vi | n | Trúng | **NGHIỆM THU** | official | `/choi` |
|---|---|---|---|---|---|
| **TỔNG** | 135 | 36 | **+4,9%** | −34,6% | −8,0% |
| MN | 45 | 14 | **+2,8%** | −18,9% | −31,4% |
| MT | 45 | 11 | **+33,1%** | −44,5% | +23,1% |
| MB | 45 | 11 | **−11,3%** | −51,6% | −27,4% |

Luồng ghép vượt cả official lẫn `/choi` ở tổng thể. MT gánh phần lớn phần dương.

**MB vẫn âm −11,3%.** Giữ nguyên trong luồng, không cắt. Cắt MB dựa trên chính bộ số đã dùng để chọn cấu hình là chọn số liệu cho vừa ý mình — để forward tự phán quyết.

## 5. Ngày chạy thật đầu tiên — 30/07

| Miền | Số | Đài đặt |
|---|---|---|
| MN | `86` | Cần Thơ, Đồng Nai |
| MT | `20` | Đà Nẵng |
| MB | `43` | Bắc Ninh |

## 6. Đã giao gì

- `web/backend/_v10879_nghiemthu_lane.py` — lane + bảng `v10879_nghiemthu_scoreboard`, chấm cả hai lớp 1/1 và có nháy, đặt official và `/choi` ngay cạnh trên cùng một dòng để so thẳng.
- Ghi `du_doan_test_bundles` tên `{REGION}_NGHIEMTHU_1908_V1` nên hiện luôn ở `/du-doan-test` cạnh các luồng khác, `test_only=1`, `output_eligible=0`.
- `GET /api/admin/nghiemthu-1908` — `require_admin`, `Cache-Control: no-store`.
- Panel `/monitoring` viền tím, đã đăng ký trong `loadAllSections()` và `setInterval` 60 giây.
- Cron 15:52 MN · 17:01 MT · 18:01 MB (pre-draw) · 21:16 chấm lại sau khi có kết quả.

## 7. An toàn

Không ghi `final_bundles`, không đụng `/choi`, không sửa bộ chọn official.

Hash 4 bảng official pre/post **IDENTICAL**:

```
predictions       11287  f3b649b6bb472f63
final_bundles       457  1e54985da004e902
lottery_results   15173  ba42b58e9fc148fa
model_daily_eval  11111  5f034cce2676713e
```

`V10841_CONTRACT_PASS` · smoke `/api/health=200` · `/du-doan=200` · endpoint admin `=401`.

## 8. Kiểm chứng trên máy chủ

| Mục | Kết quả |
|---|---|
| Lane ghi `du_doan_test_bundles` | 3/3 miền cho 30/07, hiện ở `/du-doan-test` cạnh các luồng khác |
| Cron | 4 dòng đã cài |
| Panel `/monitoring` | có trên VPS, đăng ký trong `init()` **và** trong vòng refresh 60 giây |
| Endpoint admin | 401 khi chưa đăng nhập |
| Service | `active` |

Hai lỗi trong chính bộ kiểm đã sửa: bộ kiểm panel tìm hàm tên `loadAllSections` trong khi hàm nạp của file này là `init()`, nên panel đăng ký đúng vẫn bị báo thiếu; bộ kiểm lane gọi CLI `sqlite3` vốn không cài trên máy chủ, nên trả về rỗng thay vì báo đúng số dòng đã ghi.

## 9. Notion

Trang tóm tắt: `3ad1d385-9bf8-81a7-a878-f841a94f3192`

## 10. Điều kiện lên official

Chỉ áp vào official khi forward 1/1 **dương** và **vượt official trên cùng cửa sổ**, có chữ ký owner ở mốc 19/08. Không tự động lên.

Rủi ro còn mở: MB âm ở backfill — nếu forward vẫn âm thì bỏ MB khỏi luồng thay vì để nó kéo cả cụm xuống.

Đang chờ owner cập nhật vốn và tỷ lệ ăn xiên (V10878); có số rồi sẽ cân nhắc thêm nhánh xiên vào chính luồng này.
