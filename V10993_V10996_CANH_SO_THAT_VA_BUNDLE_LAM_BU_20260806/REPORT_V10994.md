# REPORT V10994 — Đo A2/A3 samday · đo mức lẫn của bundle làm bù · cổng canh mới

> **Ngày:** 2026-08-06 · **Quyết định owner:** QD-032 · **Mã việc:** FU-277 · FU-278
> **Báo cáo chung cả mạch V10993–V10996:** [`REPORT_V10993_V10996.md`](./REPORT_V10993_V10996.md)

---

## 1. Tóm tắt

Ba việc, ràng buộc **không sửa số, không sửa prompt** — đã giữ đúng, chỉ thêm phép canh.

**A2/A3:** samday chưa kết luận được. **Shadow:** không chảy vào số chính thức. **Mức lẫn:** có thật, tập trung ở MB, nặng nhất MB Chủ Nhật thổi **+10,6 điểm**.

## 2. Owner yêu cầu gì (nguyên văn)

> *"ok em làm đi em đồng ý nếu lẫn thì phải làm cho rõ ra để có xác nhận và quyết định chính xác || Đo tiếp A2/A3. Kiểm tra thêm bảng shadow có ảnh hưởng số chính thức không. Bổ sung kiểm tra cho 3 bảng chính thức. Không sửa số, không sửa prompt."*

## 3. Đào bới / phát hiện

### A2/A3 — `VERIFIED_TEST` · INCONCLUSIVE

Nguồn `v10801_ml_mark_ab_daily` (cron 19:05 sẵn có): 512 dòng · 64 ngày 03/06→05/08 · 4 model. Dữ liệu **cặp đôi** nên dùng **McNemar** trên cặp bất đồng, không so hai tỉ lệ rời.

| Bạch thủ | n | A (D-1) | B (samday) | A>B | B>A | z | KTC 95% |
|---|---|---|---|---|---|---|---|
| MT | 256 | 32,0% | **37,9%** | 25 | 40 | **+1,86** | [−0,3%; +12,0%] |
| MB | 256 | 19,9% | 20,3% | 24 | 25 | +0,14 | [−5,0%; +5,7%] |
| Gộp | 512 | 26,0% | 29,1% | 49 | 65 | +1,50 | [−1,0%; +7,2%] |

Top-2: MT +0,25 · MB +0,25. Cặp bất đồng 49–65 mỗi ô → phép McNemar có nghĩa.

**MN không có dữ liệu samday là ĐÚNG THIẾT KẾ** (MN xổ đầu ngày), không phải thiếu sót.

### Shadow có chảy vào số chính thức không — `VERIFIED_CODE` · KHÔNG

`database.py` (nơi GHI `final_bundles`): 2 chỗ nhắc `_shadow` là **tên hàm** `ensure_shadow_daily_comparison_table()` và **tên biến khoá API**. `combo_super.py`: cả 3 chỗ là **dòng chú thích**. Bảng A/B: toàn bộ 512 dòng `output_eligible=0` · `shadow_only=1`.

### FU-277 — mức lẫn trên phép ĐANG CHẠY `main.py:1662`

| Ô | Có lẫn | Đã loại | Chênh |
|---|---|---|---|
| **MB Chủ Nhật** | 5/23 = **21,7%** | 2/18 = **11,1%** | **+10,6** |
| MB T6 | 5/22 = 22,7% | 3/18 = 16,7% | +6,1 |
| MB T2 | 5/23 = 21,7% | 3/19 = 15,8% | +5,9 |
| MB T3 | 6/23 = 26,1% | 4/19 = 21,1% | +5,0 |

**4/21 ô lệch ≥5 điểm, cả bốn đều MB.** MN/MT lệch tối đa ±4,8. Soi toàn bộ tệp `.py`: **không chỗ nào đang lọc**.

## 4. Hướng xử lý và vì sao chọn

**Không tuyên bố thắng cho A2/A3** vì mọi KTC chứa 0 — đúng điều kiện dừng PL17. MT gần ngưỡng nhất (z=+1,86 so với 1,96), cần thêm **~7 ngày** cặp bất đồng.

**Biến phát hiện FU-277 thành cổng canh thường trực** thay vì chỉ ghi báo cáo — báo cáo thì người ta quên, cổng thì chạy mỗi ngày.

## 5. Đã làm gì

`soi_bundle_lam_bu()` trong `_v10660_no_lookahead_harness.py`: in riêng một khối và đưa `BUNDLE_LAM_BU=n` vào dòng máy đọc được. **Không tự sửa dữ liệu, không xoá bundle nào** — chỉ bêu ra để mọi phép đo sau biết mà lọc.

## 6. Cổng kiểm

`[cong] SO_THAT_HINDSIGHT=0 SO_BI_SUA=0 LATE_FREEZE=27 BUNDLE_LAM_BU=90`

Deploy 1 tệp, **không restart**. 4 bảng khoá giữ nguyên hash cả bốn. health 200.

## 7. Vướng vấp

Ràng buộc owner *"không sửa số, không sửa prompt"* — đã giữ đúng, không đụng số nào.

Chỗ khó: 560 tệp nhắc tên `final_bundles`. Không soi hết được, nên thu hẹp về câu hỏi thực dụng: **chỗ nào ĐANG SỐNG và ĐANG tính thành tích**. Cách này có rủi ro bỏ sót script một lần — đã ghi vào FU-277 để soi tiếp.

## 8. Gỡ về

Xem mục 8 của báo cáo chung.

## 9. Theo dõi tiếp

**FU-277** (13/08) — quyết định sửa chỗ nào. **FU-278** (13/08) — 27 bản ghi trễ hạn chốt 2–4 phút, gộp xem cùng FU-256.
