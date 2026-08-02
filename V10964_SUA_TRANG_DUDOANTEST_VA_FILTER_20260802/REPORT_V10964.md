# REPORT V10964 — Sửa trang `/du-doan-test` neo ngày + `/filter` lệch múi giờ

**Phiên bản:** V10964 · **Ngày:** 2026-08-02 · **Giờ VN:** 17:22–17:30  
**Commit riêng / công khai:** điền sau khi push · **Deploy:** PID 639386 → 641906 · hash 4 bảng y nguyên

---

## 1. Tóm tắt

Sửa hai lỗi hiển thị (không đổi cách tính số). Trên `/du-doan-test`, ba miền dùng chung quy tắc neo ngày và gắn nhãn ngày to; MN cột test trống vì 18/20 model (không phải thiếu dữ liệu). Trên `/filter`, sửa `getVNDateISO` đang nhảy sang ngày mai sau ~17:00 VN — Playwright trước: 03/08 + 0 unique; sau: 02/08 + 11 unique. Deploy xong trước khung MB 17:38.

## 2. Owner yêu cầu gì

Nguyên văn:

> *"https://xs.io.vn/du-doan-test có dọn thì gọn cho đàng hoàng nha em. MN thì neo dữ liệu hôm qua, cột lane test thì trống. MT neo dự đoán ngày 31/07 cột lane test thì lại có hôm nay. MB thì chưa biết, cũng card cũng lưu ngày 31/07. Sao mà tùm lum vậy em?"*

> *"cũng chưa kiểm tra xử lý dùm a luôn"* (trang `/filter?tab=overview` vẫn kẹt tải / trống sau V10960)

Ràng buộc: QD-014 đóng băng đường ra số tới hết 08/08 — chỉ sửa hiển thị; deploy ngoài giờ chạy.

## 3. Đào bới / phát hiện

Đối chiếu `final_bundles` + `experimental_preview_shadow` trên VPS + gọi handler API in-process + Playwright timezone `Asia/Ho_Chi_Minh`.

| Miền | Official (final_bundles) | Lane test publish | Ghi chú |
|---|---|---|---|
| MN | **02/08** BT=`43` lo2=`43-39` lo3=`443` (05:18:43) | Không publish — **18/20** model; preview phụ BT=`39` | Owner nhầm “hôm qua”; số khớp ảnh |
| MT | **02/08** BT=`69` lo2=`69-90` lo3=`069` | Publish `MT_AI_CHAIN_PRESERVATION_V1` BT=`86` (**20/20**) | Có số vì đủ budget |
| MB | Fallback **01/08** BT=`90` (`is_fallback`) | Preview phụ 4/20 | Chưa tới giờ chốt ~17:38 |

Gốc “tùm lum”: MN/MT từng **kéo `data_date` về ngày official cũ** khi hôm nay thiếu; MB giữ hôm nay. Ba quy tắc khác nhau.

`/filter`: API public `/api/review-hub/filter` =200. Lỗi = `getVNDateISO` cộng offset timezone hai lần → sau ~17:00 VN chọn **2026-08-03**.

## 4. Hướng xử lý và vì sao chọn

- **Chọn:** thống nhất neo `requested_date` (hôm nay); official cũ gắn nhãn §54; cột test hiện lý do trống / preview phụ; sửa `getVNDateISO` bằng `Intl` Asia/Ho_Chi_Minh.
- **Không chọn:** hạ ngưỡng 20/20 để MN có publish — đó đổi doctrine đo lường, phạm QD-014.
- **Không chọn:** tin lời “MN hôm qua” rồi kéo data — bằng chứng DB nói ngược.

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `web/backend/main.py` | Bỏ kéo `data_date`; thêm `_build_display_date_anchor` |
| `web/frontend/du-doan-test.html` | Nhãn ngày header/compare; preview phụ; lý do trống |
| `web/frontend/review-dashboard.html` | Sửa `getVNDateISO`; cảnh báo ngày xem ≠ hôm nay |
| Docs | CHANGELOG · SSOT · FU-225 · `governance_seq` 381→382 |

Backup: `backups/v10964_pre/` · VPS `/root/backups_v10964_pre/`.  
Deploy: `_v10964_deploy.py` lúc 17:28 VN.

## 6. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| Ngoài khung MB lúc deploy | Đạt (17:28 < 17:38) |
| PID đổi | 639386 → 641906 |
| `/api/health` | 200 |
| `/filter` · `/api/review-hub/filter` | 200 |
| Hash 4 bảng trước/sau | Y nguyên |
| Playwright `/filter` sau sửa | date=`2026-08-02`, 11 unique, rates 91.2/86/67.2 |
| API anchor MN/MT/MB | Có `display_date_anchor` đúng |

## 7. Vướng vấp

- Owner mô tả MN “hôm qua” — **sai**; bỏ qua sẽ sửa nhầm ngày đang đúng.
- Deploy suýt chạm khung MB — phải so giờ VPS trước restart.
- Agent V10965 song song ghi docs — chờ mtime ≥60s rồi mới prepend.
- Hậu quả nếu bỏ nhãn §54: owner tưởng số cũ là số hôm nay khi miền chưa chốt.

## 8. Gỡ về

```
cp /root/backups_v10964_pre/main.py /root/Lottery_AI_Test/web/backend/main.py
cp /root/backups_v10964_pre/du-doan-test.html /root/Lottery_AI_Test/web/frontend/du-doan-test.html
cp /root/backups_v10964_pre/review-dashboard.html /root/Lottery_AI_Test/web/frontend/review-dashboard.html
systemctl restart lottery.service
```

Local: `backups/v10964_pre/`. Thời gian ~2 phút.

## 9. Theo dõi tiếp

- **FU-225** — owner xác minh UI tối 02/08 hoặc sáng 03/08.
- Ngưỡng: MN vẫn 18/20 thì cột test phải hiện preview + lý do, không còn “Chưa có dữ liệu” trống.
- `/filter` sau 17:00 phải neo đúng hôm nay VN.
