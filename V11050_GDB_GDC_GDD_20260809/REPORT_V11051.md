# REPORT V11051 — GĐ-A': 30 TỆP TRƯỚC 15:30 · C26 VÀO BỘ 18:05 · RM-20

> **Cùng thư mục với `REPORT_V11050.md`** — owner cho tối đa **2 thư mục báo cáo** toàn phiên và
> ra lệnh *«nối báo cáo vào REPORT_V11050, không mở folder mới»*. Tệp này là **bản đầy đủ theo
> khung 9 phần cho riêng V11051**; phần tường thuật dài nằm trong `REPORT_V11050.md`.

**Ngày:** 2026-08-09, 14:00 → 14:20 giờ VN · **Tầng verdict:** `RUNTIME_PROVEN`

## 1. Tóm tắt

Owner ký Q2 duyệt đẩy 28+2 tệp «drift». Thi hành đúng trình tự A'1, và **bước (b) làm sập tiền
đề**: **25/28 tệp chỉ đổi ĐÚNG MỘT DÒNG**, đều là **một việc duy nhất** — thêm roster
`claude-opus-4-6`. ⇒ **DỪNG 25 tệp, đẩy 3 tệp không dính roster.** Song song: đưa **C26** vào bộ
18:05 để con số 97 mục archive hiện **mỗi ngày** (Q4c), đóng `FU-391`/`FU-388` (Q4a/b), ghi
**RM-20** vào đủ sáu mặt.

## 2. Owner yêu cầu gì (nguyên văn)

> **Q2.** *«28+2 tệp: DUYỆT một lượt deploy có ký — theo đúng trình tự A'1 … Nhớ: nhóm backend
> KHÔNG qua API deploy; 15:00 chưa qua bước (d) thì cắt nhóm backend sang sau 18:15.»*
>
> **Q4a.** *«FU-391: ĐÓNG — không gỡ (4 điểm đọc sống). Ghi bài học vào RM register: "0 dòng mới"
> ≠ "không ai đọc".»*
>
> **Q4b.** *«FU-388: ĐÓNG — soi xong … Quyết định đấu nối `_v10705` thuộc gói 21/08.»*
>
> **Q4c.** *«FU-390: CẤM đóng hàng loạt. Rà THEO NHÃN … Cổng canh 97 mục phải báo số đếm mỗi ngày
> trong bộ 18:05 — nếu cổng chưa in được số thì đó là việc đầu tiên của GĐ-B'.»*

## 3. Đào bới / phát hiện

**25/28 tệp là MỘT lần thêm roster.** Diff toàn bộ 28 tệp: **83 dòng thêm / 34 dòng bớt**; 25 tệp
đổi đúng một dòng, nội dung là `"claude-opus-4-6"` / `'claude-opus-4-6': 0.75` /
`{"model": "claude-opus-4-6", "provider": "anthropic"}`.

**Vì sao là QD-041:** `strength_calibrator.py` thêm trọng số hiệu chỉnh, và
`calibrate_strength(model, region, raw_strength)` được gọi ở **7 chỗ đang chạy** —
`main.py:7451/7913/8118` · `scheduler.py:2986/3310/4401/5730`. Strength → verdict → chọn số.

**Phản biện tự đặt:** model **đã chạy sẵn** (có trong `predictions` production, có trong
`model_registry.py` trên VPS, 17 tệp VPS đã nhắc tên) ⇒ 25 tệp này là bề mặt **bị bỏ quên**.
**Kết luận không đổi:** cái đổi là **hiệu chỉnh**, không phải **sự tồn tại** của model.

**C26 chạy thật lộ ngay 4 thứ chưa bao giờ có trên VPS:** `_v11048_kiem_legacy_treo.py` ·
`_v10958_fu_reader.py` · `docs/archive/FOLLOW_UP_TRACKER_LICH_SU.md`, và
`docs/FOLLOW_UP_TRACKER.md` trên VPS còn là bản **trước khi tách archive** (718.081 → 633.638 byte).

**Thêm RM-20 lộ ra bộ sinh chỉ ghi MỘT mặt:** `_v10925_rule_sync_check.py` **chưa bao giờ** sinh
`GEMINI.md`, trong khi `CLAUDE.md` khai cả hai là mặt sinh và **cấm sửa tay cả hai** — mà script
vẫn in *«SÁU MẶT ĐỒNG BỘ»*.

## 4. Hướng xử lý và vì sao chọn

**Dừng 25 tệp** vì Q2 ký trên tiền đề khác sự thật ⇒ đây là **quyết định mới của owner**, không
phải chi tiết thi hành. **Đẩy 3 tệp** vì chúng không dính roster và không nằm trong tập `main.py`
nạp. **Phân loại 25 tệp thành C/B/A** để owner ký chính xác thay vì ký gộp.

## 5. Đã làm gì

| việc | kết quả |
|---|---|
| đẩy 3 tệp không dính roster | md5 khớp git **3/3** · `py_compile` **3/3** · **không restart** |
| kéo `_v105_18_vps_smoke.py` vào git | 61 dòng, chỉ đọc, **đã soi không có khoá/mật khẩu/token** |
| **C26** vào `_v10900_consistency_guard.py` | bộ **26 phép** · đẩy đủ 4 phụ thuộc lên VPS |
| restart có kiểm soát | PID **1172701 → 1207732** · health 200 · `/du-doan` 200 · `/monitoring` 401 · **0 dòng lỗi** |
| `FU-391` · `FU-388` | **ĐÓNG** theo chữ ký owner |
| **RM-20** | vào `CLAUDE.md` · `.Antigravityrules.md` · `.AGENT.md` · `.cursorrules` + sinh lại `AGENTS.md`/`GEMINI.md` |
| vá bộ sinh | nay sinh **cả hai** mặt · `SAU_MAT` thêm `GEMINI.md` · `.antigravityrules` trỏ đủ |

## 6. Cổng kiểm

```
V  : cao nhất V11050 · trống tiếp V11051      ✓ dùng V11051
FU : cao nhất FU-392 · trống tiếp FU-393      ✓ dùng FU-393
QD : cao nhất QD-054 · trống tiếp QD-055      (không dùng)
```
**Trần sinh mã: 3/5** — `FU-391`(GĐ-A) · `FU-392`(GĐ-B) · `FU-393`(GĐ-A'). Còn 2 suất.

**RM-15 cho C26 — hai chiều:** thêm 1 khối treo giả ⇒ **LECH** (98 > trần 97) · khôi phục ⇒ **OK**
(97) · md5 archive **nguyên vẹn** `dc76faeeaff102749836563831189385`.

`SÁU MẶT ĐỒNG BỘ` (exit 0) · `không mục quản trị nào biến mất` · `O_STATUS_V11044=DAT` ·
`CONG_K1_V11050=DAT` 8/8 · `DRIFT_K3_V11050=DAT` (lệch 25, trần 30) · `KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI`.

## 7. Vướng vấp

**7.1 — Gọi 28 tệp là «drift» là mô tả sai bản chất.** Kể cả em ở GĐ-B. «28 tệp lệch» nghe như 28
việc rời rạc; thật ra là **một việc**.

**7.2 — Cổng `THI_HANH_57` đòi đóng đúng ba mã vừa chứng minh còn sống** (`FU-160/162/164`) cộng ba
mã sinh sau chữ ký, rồi sau đó đòi đóng cả `FU-390` — thứ owner **vừa cấm đóng hàng loạt**. Nguyên
nhân: cổng **tính lại danh sách mỗi lần chạy** thay vì ghim tập đã ký. Đã ghim
`NGOAI_PHAM_VI_KY_0033`, có nêu lý do từng mã, và **bêu tên** mã bị bỏ ra.

**7.3 — Bẫy CRLF lần thứ năm trong hai ngày** khi vá `_v10925_rule_sync_check.py`.

## 8. Gỡ về

```bash
ssh root@14.225.224.89 'cd /root/Lottery_AI_Test && \
  tar xzf backups/snapshot_20260809_1400_pre_v11051/web_backend_py.tgz && \
  cp backups/guard.py.pre_v11051 web/backend/_v10900_consistency_guard.py && \
  systemctl restart lottery'
git revert <commit V11051 / V11051b>
```
Snapshot kèm `md5_truoc.txt` + `pid_truoc.txt` để đối chiếu.

## 9. Theo dõi tiếp

| mã | việc | chờ ai |
|---|---|---|
| `FU-393` | 25 tệp roster — ba phương án **(a)** giữ tới 21/08 *(đề xuất)* · **(b)** đẩy 20 tệp shadow · **(c)** ký đè QD-041 | **owner** |
| `FU-390` | rà theo nhãn 64/18/9/5 · **⚠ cổng đếm 97 nhưng bảng owner gộp 96** — còn 1 khối `FALSE_NEGATIVE` (`FU-V10864-FOUR-CARD`) chờ owner xếp nhóm | **owner** |
| ngưỡng FU-284 | **9,53** (có dẫn xuất) vs **12,00** (prompt lần 9) — chốt **trước 20/08**, bằng dẫn xuất | **owner** |
| GĐ-C | **18:05** bộ 26 phép · **19:35** lane · bầy đàn · trace | tối nay |

*Đẩy cùng commit (A55 · §57.2).*
