# V10964b — Hoàn tất neo ngày /du-doan-test + Cache-Control /filter

**Ngày:** 02/08/2026 · **Giờ deploy VN:** ~18:13 · **PID:** 641906 → **645169** · **Trạng thái:** HOÀN TẤT (báo cáo bù A55 sau khi CHANGELOG/SSOT đã ghi)

> Báo cáo này **bù cổng A55**: phiên V10964b đã sửa UI/API neo ngày và `/filter` trên VPS, đã ghi CHANGELOG/SSOT, nhưng thiếu thư mục `V10964b_*` trên repo công khai. Số liệu lấy từ CHANGELOG + SSOT + REPORT_V10964 — không bịa.

---

## 1. Tóm tắt

Addendum sau V10964: triệt nguyên nhân “ba miền ba ngày” trên `/du-doan-test` bằng neo `display_date_anchor` / `data_date` theo ngày đang xem; cột test hiện preview phụ khi gate 20/20 chưa đạt; `/filter` thêm `Cache-Control: no-store`, gom overview, sửa `getVNDateISO`. Deploy **18:13 VN**, PID **645169**, health 200, hash 4 bảng y nguyên. Sau 18:00 MB official hôm nay BT=**52**. QD-014 tôn trọng.

## 2. Owner yêu cầu gì (nguyên văn)

(Từ chuỗi V10964, tiếp tục xử lý tới hết:)

> *"https://xs.io.vn/du-doan-test có dọn thì gọn cho đàng hoàng nha em. MN thì neo dữ liệu hôm qua, cột lane test thì trống. MT neo dự đoán ngày 31/07, cột lane test thì lại có hôm nay. MB thì chưa biết, cũng card cũng lưu ngày 31/07. Sao mà tùm lum vậy em?"*

> *"https://xs.io.vn/filter?tab=overview cũng chưa kiểm tra xử lý dùm anh luôn."*

## 3. Đào bới / phát hiện

### Nguyên nhân gốc
- API từng gán `data_date = baseline.date` khi official hôm nay chưa có → kéo cả trang (kể cả cột test) về ngày cũ.
- Ba miền chạy lệch giờ (MN ~04:30, MT ~16:42, MB ~17:38) nên “latest” khác nhau lúc owner xem.
- UI gắn nhãn “HÔM NAY” dù số là ngày cũ.

### Đo sau sửa (SSOT V10964b)

| Miền | Official | BT | Test |
|---|---|---|---|
| MN | 2026-08-02 | 43 | Preview phụ 18/20 BT=39 (không publish đủ 20) |
| MT | 2026-08-02 | 69 | Publish BT=86 (20/20) |
| MB (sau freeze) | 2026-08-02 | 52 | Preview phụ 4/20 |

`/filter` header: `cache-control: no-store, no-cache, must-revalidate, max-age=0`.

## 4. Hướng xử lý và vì sao chọn

- Sửa **UI + chọn ngày hiển thị**, không đổi cách tính số (QD-014).
- Thêm `Cache-Control` trên route `/filter` thay vì bảo owner hard-refresh — V10960 UI đã trên VPS nhưng trình duyệt giữ HTML cũ.
- Không nới gate 20/20 để “có số” — vẫn hiện preview phụ kèm nhãn lý do.

## 5. Đã làm gì

| Hạng mục | Chi tiết |
|---|---|
| Neo ngày | `display_date_anchor` thống nhất; `data_date` = ngày đang xem |
| Cột test | Preview phụ + nhãn / giờ dự kiến |
| Official fallback | Nhãn rõ “KHÔNG phải số hôm nay” |
| `/filter` | `Cache-Control: no-store`; ẩn sticky overview; gộp 4→2 card; `getVNDateISO` |
| Deploy | PID 641906→645169 · health 200 · hash 4 bảng y nguyên |
| Backup | `backups/v10964_pre/` + VPS `/root/Lottery_AI_Test/backups/v10964_pre/` |

## 6. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| `/api/health` | 200 |
| PID đổi sau restart | 641906 → 645169 |
| Hash 4 bảng khoá | Y nguyên (CHANGELOG) |
| MB sau 18:00 BT hôm nay | 52 (không fallback 01/08) |
| Báo cáo folder `V10964b_*` | Bù trong phiên V10969 |

## 7. Vướng vấp

1. **Báo cáo công khai thiếu dù code đã deploy** — cổng A55 FAIL cho V10964b. Hậu quả nếu bỏ qua: owner không kiểm soát được phiên trên GitHub report.
2. Deploy lúc **18:13** sát khung nguy hiểm chiều — đã xong trước khi owner chốt hook cấm giờ (V10968). Hậu quả: rủi ro đụng chuỗi MB nếu trễ hơn.

## 8. Gỡ về

```text
# VPS: khoi phuc tu backups/v10964_pre/ (frontend + handler lien quan)
# roi systemctl restart lottery; so PID
```

Thời gian ước lượng: 5–10 phút. Hash 4 bảng không bị đụng nên không cần restore DB.

## 9. Theo dõi tiếp

- **FU-225 · UI0803 · Xác minh UI du-doan-test + filter · hạn 03/08** — ngưỡng: owner mở tay MN/MT/MB cùng một `requested_date` và `/filter` không còn HTML cache cũ.
- **FU-215 · DB0808 · Đóng băng đường ra số (QD-014) · hạn 08/08** — phiên này không đụng roster/combo.
