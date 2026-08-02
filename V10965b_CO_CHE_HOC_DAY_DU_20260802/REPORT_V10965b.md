# V10965b — Tài liệu đầy đủ cơ chế học và xếp hạng

**Ngày:** 02/08/2026 · **Trạng thái:** HOÀN TẤT (chỉ tài liệu + đo VPS; không deploy) · **Báo cáo bù A55** trong phiên V10969

> Nội dung đo/tài liệu đã có trong CHANGELOG/SSOT và từng nằm dưới folder tên `V10965_CO_CHE_HOC_VA_XEP_HANG_*` (file `REPORT_V10965.md`). Cổng A55 cần đúng prefix **V10965b** — báo cáo này chuẩn hoá tên + đủ 9 phần.

---

## 1. Tóm tắt

Đào toàn bộ cơ chế học / tích luỹ / xếp hạng / retrain đang chạy (chỉ đọc). Viết `docs/CO_CHE_HOC_VA_XEP_HANG.md`. Kết luận kiểm soát: ~**18** cơ chế sống, ~**7** ảnh hưởng số công bố, ~**8** chạy chỉ ghi số, ~**6+** chết/tắt. RULES-FIRST đang hại; optimizer lift âm (MN −4,75 / MT −10,95 / MB −8,47); lệch WR vs BT tới **+47pp**. Retrain CN 02/08 **12/12** RETRAINED. Cổng lợi thế ĐÓNG 3 miền. **Không** sửa code / **không** deploy (QD-014).

## 2. Owner yêu cầu gì (nguyên văn)

> *"Roi cac co che nhu hoc tap tich luy, xep hang, retrain cua cac model LLM va ML thi sao, em da dao sau het co chua? Viet chi tiet cu the tat ca moi thu hien dang code de kiem soat, tong hop that day du."*

(Phiên 02/08; yêu cầu tài liệu kiểm soát đầy đủ — bản rút `CAC_CO_CHE_*` chưa đủ.)

## 3. Đào bới / phát hiện

Đo VPS thật (crontab + DB), evidence trong `evidence/` (probe_live / probe5_lech nếu có):

| Hạng mục | Số liệu |
|---|---|
| Retrain CN 02/08 ~02:02 | **RETRAINED 12/12**; guard 06:30 FRESH_SKIP |
| Optimizer 02/08 03:15 | lift MN **−4,75** / MT **−10,95** / MB **−8,47** (âm) |
| mined_rules | 105 active v2026W31; MRE 01/08; RULES-FIRST vẫn ép list |
| Champion | cron 06:25 còn chạy log; bảng `champion_selector_shadow` đứng **15/06** |
| Lệch WR vs BT 30d | sonnet MN WR 83,9 / BT 36,7 (**+47pp**); deepseek-reasoner MN **+44pp** |
| edge_gate (01/08 ghi nhận trong phiên) | ĐÓNG 3 miền (MN −0,36 / MT −2,92 / MB −7,19 pp) |

## 4. Hướng xử lý và vì sao chọn

Chỉ viết tài liệu + FU theo dõi. Không sửa runtime vì **QD-014** đóng băng tới 08/08. Việc tắt RULES-FIRST / đo từng cơ chế / sửa champion để sau 08/08 (QD-016/017, FU-228/229/230).

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `docs/CO_CHE_HOC_VA_XEP_HANG.md` | Tài liệu đầy đủ (6 câu hỏi bằng chứng + sơ đồ đường đi) |
| CHANGELOG / SSOT / FOLLOW_UP | prepend V10965b + FU liên quan |
| `artifacts/v10965_co_che_hoc/` | Probe VPS |
| Deploy / hash | Không áp dụng (chỉ doc) |

## 6. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| Chỉ đọc — không deploy | Đúng |
| Crontab + DB đối chiếu probe | Có trong evidence / CHANGELOG |
| Folder public đúng `V10965b_*` | Bù phiên V10969 |
| QD-014 | Không đụng đường ra số |

## 7. Vướng vấp

1. Agent song song đã viết bản rút + stub V10965 — dễ tưởng “đã đủ”. Hậu quả: thiếu bản đầy đủ owner yêu cầu.
2. Cột predictions là `ai_model` (không phải `model`) — probe đầu lỗi schema.
3. Champion: cron sống / bảng đứng — dễ tưởng còn xếp hạng thật nếu chỉ nhìn log.
4. Báo cáo đặt nhầm prefix V10965 → cổng A55 không nhận V10965b.

## 8. Gỡ về

Không đổi runtime. Xoá/revert tài liệu:

```text
git checkout <commit_truoc> -- docs/CO_CHE_HOC_VA_XEP_HANG.md
# va thu muc bao cao public V10965b_* neu can
```

Thời gian < 2 phút. Không restore VPS.

## 9. Theo dõi tiếp

- **FU-228 · DO0808 · Đo từng cơ chế học · hạn 08/08** (nếu còn mở trên tracker) — ngưỡng bằng số theo từng bề mặt.
- **FU-229 · KS0808 · Champion bảng đứng 15/06** — ngưỡng: bảng có dòng mới sau khi sửa hoặc tắt cron chết.
- **FU-230 · DO0808 · Đồng bộ thước WR vs BT** — ngưỡng: không còn lệch >20pp trên cùng cửa sổ đo khi dùng cho quyết định cắt/thêm model.
- **FU-215 · DB0808 · QD-014** — không sửa trước 08/08.
