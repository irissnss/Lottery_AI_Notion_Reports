# V10919 — Cho 6 lane hết hạn đo nghỉ

**Ngày:** 01/08/2026 · **Commit riêng:** `d179b77` · **Trạng thái:** đã gỡ, tự kiểm 16/16 sạch

---

## 1. Tóm tắt

Owner báo các luồng đã rối và mất kiểm soát. Kiểm kê cho thấy **cấu trúc 5 luồng owner ký là
mạch lạc** — rối đến từ ~15 lane đo lường và ~10 job buổi tối xếp chồng bên dưới, **không cái nào
ghi vào output chính**. Đã cho **6 lane** hết hạn đo nghỉ: **83 → 71 dòng cron**, 71 dòng còn lại
y nguyên từng ký tự, bộ tự kiểm 16 phép lệch 0.

Chỉ **gỡ cron, không xoá file** — vì `_v10692` là thư viện dùng chung cho ba file khác.

---

## 2. Owner yêu cầu gì (nguyên văn)

**01/08 ~10:0x:**

> *"Còn luồng thì anh thấy cũng bắt đầu rối rồi đó, mất kiểm soát rồi đó. Nào là lane test, nào
> là choi, nào là nghiem thu, nào là official v.v... cần xem xử lý luôn đi."*

**01/08 ~10:2x** — sau khi agent trình danh sách 6 lane, owner chọn: **dẹp cả 6**, và:

> *"Chờ ít nhất 7 ngày xem số liệu thật đúng như dự tính rồi mới động tiếp"*

---

## 3. Đào bới / phát hiện — cấu trúc không rối, cái rối nằm bên dưới

Cấu trúc **5 luồng** owner ký là mạch lạc, mỗi cái một việc:

| Luồng | Là gì | Ghi vào đâu |
|---|---|---|
| 1 · official `/du-doan` | số thật cho người dùng | **`final_bundles`** |
| 2 · lane test `/du-doan-test` | thử phương pháp mới (M01–M10) | `experimental_preview_shadow` |
| 3 · Total V2/V3 | đo cách cộng phiếu khác | `du_doan_test_bundles` |
| 4 · `/choi` | khuyên chơi, **đọc lại** số official | `money_board_daily_lock` |
| 5 · Nghiệm Thu 19/08 | official bản mới, chạy song song | `du_doan_test_bundles` |

Cảm giác mất kiểm soát đến từ **~15 lane đo lường + ~10 job buổi tối** xếp chồng dưới luồng
2/3/5. **Không lane nào trong số này ghi vào `final_bundles`** — nên dẹp chúng không đụng gì
tới số hiển thị.

---

## 2. Sáu lane cho nghỉ

| Lane | Dòng cron | Lý do |
|---|---|---|
| V10707 A/B doctrine MN/MT | 2 | hạn *"~2 tuần"* từ 10/06 — quá **7 tuần**, không ai chốt |
| V10781 A/B prompt v2 | 3 | hạn trình 14/07 — quá **2,5 tuần** |
| V10692 lane 3 hướng MN/MT | 4 | playbook ghi rõ *"MN không promote, /choi không dùng"* |
| V10679 lane full-pool d_w06 | 1 | không có đường lên official |
| V10680 lane top-K strength | 1 | không có đường lên official |
| V10637 lane-v2 | 1 | tự khai *"never imported by scheduler/main/official"*, không UI không API |

---

## 4. Hướng xử lý và vì sao chọn

| Phương án | Vì sao chọn / loại |
|---|---|
| **Gỡ cron, giữ file, comment kèm lý do** | **ĐÃ CHỌN.** Dừng được việc chạy vô ích mà không gãy thư viện; đọc crontab là hiểu vì sao, bỏ dấu `#` là chạy lại |
| Xoá hẳn file lane | **Loại — suýt làm.** `_v10692` là thư viện dùng chung cho 3 file khác, xoá là gãy ba chỗ |
| Xoá dòng cron thay vì comment | Loại: sau này không ai biết từng có gì và vì sao mất |
| Giữ nguyên, chỉ ghi tài liệu | Loại: owner nói rõ *"cần xem xử lý luôn đi"*, và các lane này đã quá hạn đo 2,5–7 tuần |
| Dẹp một phần (chỉ 2–3 lane) | Owner tự chọn **dẹp cả 6** khi được hỏi |

---

## 5. Đã làm gì

| Việc | Chi tiết |
|---|---|
| Gỡ cron 6 lane | 12 dòng, comment kèm ngày + lý do, **không xoá dòng** |
| Giữ nguyên file | Không xoá file nào; `_v10692` bắt buộc giữ vì là thư viện |
| Sửa bộ tự kiểm C6 | Không còn cron v10692 = đúng như mong đợi, không báo lệch oan |
| Backup | `backups/v10919_pre/crontab_before.txt` (109 dòng) + `/root/.local_backup_v10919_crontab_20260801_103142.txt` trên VPS |
| Nạp crontab | Bằng `crontab <file>` — lệnh nguyên khối, đứt giữa chừng không hỏng |
| Restart | Service `lottery`, PID đổi thật (so trước/sau) |

---

## 6. Chỉ gỡ cron — và đây là chỗ suýt sai

Soi tham chiếu chéo **trước** khi động tay, phát hiện **V10692 là thư viện dùng chung**:

```
_v10861_runtime_contract_audit.py:233   from _v10692... import _compute_model_strength
_v10869_cp_l6_lean_audit.py:336,554     import _v10692... as lane
_v10900_consistency_guard.py:110        đọc OUTPUT_FREEZE_HHMM
```

Xoá file là gãy ba chỗ. Nên **chỉ gỡ cron, giữ nguyên file**.

Dòng cron được **comment kèm ngày + lý do** chứ không xoá. Xoá thì sau này không ai biết từng
có gì và vì sao mất; comment thì đọc crontab là hiểu, bỏ dấu `#` là chạy lại.

---

## 7. Vướng vấp

Phép **C6** của `_v10900_consistency_guard` đối chiếu giờ cron lane v10692 với `LANE_SLOT`. Gỡ
cron mà không báo cho nó thì **ngày nào cũng báo lệch oan** — đúng loại "lỗi vặt mỗi ngày" owner
đã bực. Đã sửa: không còn dòng cron nào = đúng như mong đợi.

**Hai lỗi tự bắt được khi làm:**

1. Bản sửa đầu ghi `status="DAT"` trong khi cả hệ dùng `"OK"`/`"LECH"` và `compute_view` đếm
   `status == "OK"` — để nguyên là C6 bị tính lệch mỗi ngày, đúng thứ đang muốn tránh.
2. `compute_view()` chỉ **đọc bản đã lưu**, không tính lại. Lần kiểm đầu thấy C6 vẫn trả giờ cũ
   và suýt kết luận "gỡ cron không ăn". Phải gọi thẳng `run_checks()` mới biết bản sửa có chạy
   đúng không.

---

## 8. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| Dòng cron đang bật | **83 → 71**, giảm đúng 12 |
| Sáu lane còn dòng bật | 0 / 0 / 0 / 0 / 0 / 0 |
| 71 dòng cron **khác** | **y nguyên từng ký tự** |
| Bộ tự kiểm chạy lại ngay | **16 phép kiểm, lệch 0** · C6 = OK *"không còn dòng cron nào"* |
| Các job SỐNG còn nguyên | Nghiệm Thu · Total V2/V3 · de-herd · khoá `/choi` · screen |
| `/api/health` | 200 |

---

## 8b. Sửa 3 chỗ tài liệu ghi sai giờ chạy thật

Đối chiếu crontab và journal trên VPS (không tin tài liệu, tin hệ thống):

| Việc | Tài liệu ghi | Thực tế | Nguồn |
|---|---|---|---|
| ML 4 model dự đoán | 04:00 | **05:00** | journal `Free Model Auto-Predict: hàng ngày lúc 05:00` |
| Lane Nghiệm Thu MN | 05:05 + 05:15 | **06:05 + 06:15** | crontab `5 6` và `15 6` |
| Lane MN V10692 | 04:30 | **05:30** | crontab `30 5` |

Và `TEST_LANE_METHOD_REGISTRY`: M03 `V67_ADAPTIVE_EXPLOIT_V1` **đã bỏ MN từ 06/07**
(`scheduler.py:8225`) nhưng bảng vẫn ghi `MN/MT/MB`. Giờ cron trong bảng cũng chỉ là lượt tối —
còn lượt 19:00 và các script lane 16:49/17:38/17:43 không được ghi, ai đọc bảng sẽ tưởng mỗi
ngày chạy một lượt.

---

## 9. Gỡ về

```
python web/backend/_v10919_retire_lanes.py --rollback
```

Đẩy lại `backups/v10919_pre/crontab_before.txt` (109 dòng, chụp trước khi sửa) bằng
`crontab <file>` — lệnh nguyên khối, đứt giữa chừng không hỏng. **Mất khoảng 30 giây.**

Bản crontab cũ cũng còn trên VPS: `/root/.local_backup_v10919_crontab_20260801_103142.txt`

Gỡ về xong thì 12 dòng cron của 6 lane chạy lại như trước, tổng về 83 dòng. Không cần đụng
database — phiên này **không sửa dữ liệu**.

---

## 10. Theo dõi

**FU-186** — owner chốt: chờ ít nhất **7 ngày** xem số liệu thật đúng như dự tính rồi mới động
tiếp. Trong 7 ngày này **không đổi thêm gì** ở đường ra số; có phát hiện mới thì ghi nhận chứ
không sửa, vì sửa chồng lên là mất khả năng quy kết kết quả cho thay đổi nào.
