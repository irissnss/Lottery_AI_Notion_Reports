# REPORT V10996 — Đổi chỗ tính thành tích miền × thứ sang view sạch

> **Ngày:** 2026-08-06 · **Quyết định owner:** QD-034 · **Mã việc:** FU-280
> **Báo cáo chung cả mạch V10993–V10996:** [`REPORT_V10993_V10996.md`](./REPORT_V10993_V10996.md)

---

## 1. Tóm tắt

Sau khi xem bảng trước/sau đầy đủ, owner duyệt đổi **đúng một truy vấn**. **Đã sửa, đã nghiệm thu, CHƯA ĐẨY** — xem mục 7.

## 2. Owner yêu cầu gì (nguyên văn)

> *"OK LÀM ĐI EM"*

## 3. Đào bới / phát hiện

Soi **6 chỗ** tính thành tích từ `final_bundles`, **chỉ 1 chỗ bị ảnh hưởng**:

| Chỗ | Cửa sổ | Đổi? |
|---|---|---|
| `main.py:1662` | **toàn lịch sử, không lọc ngày** | **CÓ — 21/21 ô** |
| `main.py:12625` (`days=90`) | 90 ngày, từ 07/05 | không |
| `main.py:19485` | MB từ 08/04 (21/119 cả hai bản) | không |
| `main.py:20233` (`days=30`) | 30 ngày gần nhất | không |
| `main.py:20317` | 7 ngày gần nhất | không |
| `main.py:12496` | đọc `champion_selector_shadow` | không liên quan |

Năm chỗ kia sạch vì cửa sổ **bắt đầu sau vùng nhiễm 28/02→29/03**. **Đã kiểm bằng số, không suy đoán.**

## 4. Hướng xử lý và vì sao chọn

Chỉ đổi chỗ thật sự bị ảnh hưởng. Năm chỗ kia giữ nguyên — đổi thừa là tăng rủi ro mà không được gì.

Tại `main.py:1662` **cũng nên thêm cửa sổ ngày** (quét toàn bộ 23 tuần để chấm "thứ nào mạnh" là trộn cả dữ liệu tháng 2), nhưng đó là **biến thứ hai** — không gộp vào lần này, theo QD-018.

## 5. Đã làm gì

Đúng **một** tên bảng trong **một** truy vấn: `FROM final_bundles` → `FROM v_final_bundles_that`.

Đối chiếu hai bản: `FROM final_bundles` **39 → 38** · `v_final_bundles_that` **0 → 2** · diff **bỏ đúng 1 dòng**, thêm 17 (16 chú thích + 1 dòng truy vấn).

## 6. Cổng kiểm

Chạy thật truy vấn mới trên dữ liệu thật, 21 ô:

| Miền | Thứ | Trước | Sau |
|---|---|---|---|
| **MB** | **CN** | 21,7% | **11,1%** |
| MB | T6 | 22,7% | 16,7% |
| MB | T2 | 21,7% | 15,8% |
| MB | T3 | 26,1% | 21,1% |
| MN | T3 | 47,8% | **52,6%** ← tăng |

`_v10996_deploy.py` có cổng khung giờ **tự chặn** (thử 14:40 → chặn đúng), cổng kiểm view tồn tại trên VPS, và cổng đếm số ô lệch ≥5 điểm phải đúng **4**.

## 7. Vướng vấp

**CHƯA ĐẨY.** `main.py` là tệp của dịch vụ web nên **bắt buộc restart**, FU-207 áp.

Owner miễn trừ (*"hôm nay anh sẽ bỏ không tham gia vào dự đoán ... nên việc 18h15 cũng ko cần thiết"*). Agent thêm cờ `--owner-mien-tru` **có ghi lý do vào artifact**, giữ nguyên cổng chặn mặc định. Nhưng lệnh chạy bị **lớp kiểm duyệt của Claude Code chặn** vì cờ miễn trừ trông giống hành vi đi vòng cổng an toàn.

**Agent KHÔNG tìm cách lách** — không đổi tên cờ, không tự scp + restart bằng tay để né. Dừng và trình owner quyết.

Kiểm trước khi định đẩy (vẫn còn giá trị cho lần sau): VPS 14:48 · MN bundle đã chốt 05:20 · MT/MB chưa tới lượt (16:46/17:39) · không tiến trình nào đang chạy job dự đoán · job cron kế tiếp còn ~2 tiếng.

**Lỗi nguy hiểm đã tự bắt:** ban đầu để `kiem_code` của QD-034 gọi thẳng `_v10996_deploy.py`. Sổ quyết định chạy **mỗi phiên** — tức mỗi phiên sẽ **thử đẩy thật**. Đã tách ra `_v10996_kiem.py` chỉ đọc.

## 8. Gỡ về

Chưa đẩy — không cần gỡ. Nếu đã đẩy: `cp backups/v10996_pre/main.py.pre` (md5 `67f7adcd42be71ace3238f7991b8dc33`) về chỗ cũ + scp + `systemctl restart lottery`, so PID trước/sau.

## 9. Theo dõi tiếp

**FU-280** `DEPLOYED_PENDING_LIVE_VERIFY` (14/08). Nghiệm thu sau khi đẩy: 4 ô lệch ≥5 điểm đều MB · 22 phép tự kiểm · 4 bảng khoá giữ hash · health 200 · PID đổi.
