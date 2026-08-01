# V10919 — Cho 6 lane hết hạn đo nghỉ

**Ngày:** 01/08/2026 · **Commit riêng:** `d179b77` · **Trạng thái:** đã gỡ, tự kiểm 16/16 sạch

> Owner: *"Còn luồng thì anh thấy cũng bắt đầu rối rồi đó, mất kiểm soát rồi đó. Nào là lane
> test, nào là choi, nào là nghiem thu, nào là official v.v... cần xem xử lý luôn đi."*

---

## 1. Kiểm kê trước: cấu trúc không rối, cái rối nằm bên dưới

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

## 3. Chỉ gỡ cron — và đây là chỗ suýt sai

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

## 4. Sửa bộ tự kiểm để không báo động nhầm

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

## 5. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| Dòng cron đang bật | **83 → 71**, giảm đúng 12 |
| Sáu lane còn dòng bật | 0 / 0 / 0 / 0 / 0 / 0 |
| 71 dòng cron **khác** | **y nguyên từng ký tự** |
| Bộ tự kiểm chạy lại ngay | **16 phép kiểm, lệch 0** · C6 = OK *"không còn dòng cron nào"* |
| `/api/health` | 200 |

---

## 6. Sửa 3 chỗ tài liệu ghi sai giờ chạy thật

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

## 7. Gỡ về

```
python web/backend/_v10919_retire_lanes.py --rollback
```

Bản crontab cũ còn trên VPS: `/root/.local_backup_v10919_crontab_20260801_103142.txt`

---

## 8. Theo dõi

**FU-186** — owner chốt: chờ ít nhất **7 ngày** xem số liệu thật đúng như dự tính rồi mới động
tiếp. Trong 7 ngày này **không đổi thêm gì** ở đường ra số; có phát hiện mới thì ghi nhận chứ
không sửa, vì sửa chồng lên là mất khả năng quy kết kết quả cho thay đổi nào.
