# V10969 — Kiểm tổng lực hết live 02/08: ba miền đúng hạn, BT 3/3 WIN, hệ sạch

**Ngày:** 02/08/2026 · **Giờ thu thập VN:** 18:48:25 · **Commit riêng / công khai:** điền sau push · **Trạng thái:** HOÀN TẤT (chỉ đọc + báo cáo; không sửa production)

---

## 1. Tóm tắt

Sau khi hết live ngày **02/08/2026**, đã kiểm tổng lực trên VPS: ba miền đều **chốt đúng hạn** (MN 05:18 / MT 16:41 / MB 17:37), bạch thủ **cả 3 WIN** (MN 43 · MT 69 · MB 52), `/api/health=200`, `lottery.service` active PID **645169**, consistency guard **16/16 OK**, cổng lợi thế **ĐÓNG cả 3 miền** (90 ngày), pool official **15/15** có `gpt-5.4` không có `combo-no-token`, training CN **12/12 có AUC**. Nhật ký từ 05:00: **0 traceback**; 24 dòng khớp “error” chủ yếu là SCRAPE_FAIL nguồn khi chưa có kết quả / false-positive `error=0`. Không sửa runtime (QD-014). Đồng thời bù báo cáo công khai thiếu **V10964b** và **V10965b**, rồi đẩy GitHub report.

## 2. Owner yêu cầu gì (nguyên văn)

> *"Hết live rồi đó em kiểm tra tổng lực toàn diện dùm anh? đẩy toàn bộ các báo cáo chi tiết đầy đủ lên github report dùm anh nha em"*

(02/08 ~18:44 giờ Việt Nam.) Kèm phạm vi kỹ thuật: chốt 3 miền · health · journal · pool 15 · edge gate · training AUC · so BT với đánh bừa · báo cáo V10969 khung A55 · quét/bù báo cáo thiếu · push hai repo · không Notion ghi · không sửa production.

## 3. Đào bới / phát hiện

Nguồn: script `web/backend/_v10969_kiem_tong_luc.py` đẩy `/tmp/_v10969_het_live.py` chạy trên VPS bằng Python venv. Bằng chứng: `evidence/het_live_evidence.json`.

### 3.1 Ba miền — `final_bundles` ngày 2026-08-02

| Miền | Hạn | Giờ chốt | Đúng hạn? | model_count | BT | bach_thu_status | lo2_status | bundle_version |
|---|---|---|---|---|---|---|---|---|
| MN | 15:45 | **05:18:43** | Có | **15** | 43 | **WIN** | PARTIAL | 2 |
| MT | 16:58 | **16:41:36** | Có | **13** | 69 | **WIN** | PARTIAL | 2 |
| MB | 17:58 | **17:37:53** | Có | **14** | 52 | **WIN** | **WIN** | 2 |

Lưu ý trung thực: MT chỉ 13 model, MB 14 — pool eligible vẫn 15 nhưng không đủ phiếu trong bundle hôm nay (thiếu/timeout từng model). MN chốt sáng sớm (chuỗi AI MN) vẫn trước hạn 15:45.

### 3.2 Health / dịch vụ

| Mục | Kết quả |
|---|---|
| `systemctl is-active lottery` | **active** |
| MainPID | **645169** (ActiveEnter 02/08 **18:13:33** +07 — sau deploy V10964b) |
| `GET /api/health` | **200** |

### 3.3 Journal `lottery` từ 05:00

| Chỉ số | Giá trị |
|---|---|
| Tổng dòng | 7609 |
| Khớp error/traceback/exception/failed (đã lọc nhiễu health/404/401) | **24** |
| Traceback | **0** |
| Mẫu “nghiêm trọng” (traceback/critical/…) | **0** |

Phần lớn 24 dòng là: (a) `SHADOW_SUMMARY … error=0` (false positive vì chữ error); (b) `SCRAPE_FAIL` MN ~16:30 và MB ~18:30 khi nguồn chưa trả / tạm trống — kết quả cuối cùng đã có trong DB (BT đã chấm WIN).

### 3.4 Pool official (`model_registry.get_output_eligible_ids`)

- **n=15**, `pass=True`
- Có **`gpt-5.4`**
- **Không** có `combo-no-token`
- Danh sách: claude-sonnet-4-6, gemini-2.5-flash, claude-opus-4-6, deepseek-reasoner, gemini-2.5-pro, gpt-5.4, glm-5.1, gpt-oss-120b, meta-learning, lstm, xgboost, random-forest, smart-ensemble, smart-ml, combo-super

### 3.5 Cổng lợi thế `_v10945_edge_gate.compute_view()` — cửa sổ 90 ngày

| Miền | hệ | bừa | lợi thế | z | cổng |
|---|---|---|---|---|---|
| MN | 16,08% | 16,47% | **−0,38pp** | −0,17 | **ĐÓNG** |
| MT | 14,48% | 16,50% | **−2,02pp** | −0,81 | **ĐÓNG** |
| MB | 16,48% | 23,69% | **−7,21pp** | −1,62 | **ĐÓNG** |

`cong_mo_tong=False` — khớp quyết định owner 01/08 dừng đặt tiền thật.

### 3.6 Training history 02/08 (sau job ~02:00)

- **12/12** dòng có cột `auc` (không dòng nào thiếu AUC)
- `auc_present_rows=12`, `auc_missing_rows=0`

### 3.7 BT hôm nay vs “đánh bừa” (union đuôi 2 số / 100)

| Miền | BT | status DB | hit union | bừa union (ước lượng \|tails\|/100) | số đài |
|---|---|---|---|---|---|
| MN | 43 | WIN | Có | 46% | 3 |
| MT | 69 | WIN | Có | 43% | 3 |
| MB | 52 | WIN | Có | 26% | 1 |

Một ngày **3/3 WIN** là tin vui ngắn hạn — **không** mở cổng tiền: cửa sổ 90 ngày vẫn dưới ngưỡng (≥3pp và z≥2).

### 3.8 Consistency guard

`run_checks()` trên VPS: **n=16**, summary `{'OK': 16}` — **16/16**.

### 3.9 Quét báo cáo công khai

| Version | Cổng trước phiên | Ghi chú |
|---|---|---|
| V10952 / 52b / 53 / 55b | Đạt | Đã có thư mục + đủ 9 phần + đã commit |
| V10964b | **Thiếu** | Có CHANGELOG/SSOT nhưng chưa folder `V10964b_*` |
| V10965b | **Thiếu** | Nội dung từng nằm nhầm dưới folder tên `V10965_…XEP_HANG` (REPORT_V10965) |
| V10963 / V10966 | Không có mục `## V10963/66` trong CHANGELOG | Chỉ script kiểm nội bộ — **không bịa** báo cáo version |
| V10969 | Thiếu (phiên này) | Tạo mới |

## 4. Hướng xử lý và vì sao chọn

1. **Chỉ đọc + báo cáo** — owner đã ký QD-014 đóng băng đường ra số tới hết 08/08; không có lỗi chảy buộc phải sửa runtime.
2. **Bù V10964b / V10965b** từ CHANGELOG + SSOT + evidence có sẵn — không bịa số.
3. **Không tạo V10963/V10966** vì không phải phiên bản giao hàng có mục CHANGELOG; tạo sẽ làm loãng cổng A55.
4. **Push public trước**, rồi docs private + gate lại V10969.

## 5. Đã làm gì

| File / việc | Thay đổi |
|---|---|
| `web/backend/_v10969_kiem_tong_luc.py` | Script paramiko kiểm tổng lực (mới) |
| `artifacts/v10969_het_live/het_live_evidence.json` | Bằng chứng VPS |
| `Lottery_AI_Notion_Reports/V10969_…/` | REPORT + CONTEXT + evidence |
| `Lottery_AI_Notion_Reports/V10964b_…/` | Bù báo cáo addendum neo ngày/filter |
| `Lottery_AI_Notion_Reports/V10965b_…/` | Bù báo cáo cơ chế học đầy đủ |
| `CHANGELOG.md` / `CURRENT_TRUTH_SSOT.md` / `FOLLOW_UP_TRACKER.md` | prepend V10969 bằng `_doc_prepend.prepend()` |
| `docs/AUTOMATION_STATE.json` | `governance_seq` 387 → 388 |
| Deploy / hash 4 bảng | **Không đụng** (không deploy) |

## 6. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| 3 miền đúng hạn | **Đạt** |
| BT đã chấm | **3/3 WIN** |
| Health 200 + service active | **Đạt** |
| Journal traceback | **0** |
| Pool 15 + gpt-5.4 − combo-no-token | **Đạt** |
| Edge gate ĐÓNG 3 miền | **Đạt (vẫn đóng)** |
| training_history AUC 12/12 | **Đạt** |
| consistency 16/16 | **Đạt** |
| `_v10921_report_gate.py V10969` | Chạy sau push — phải đạt |
| Notion ghi | **Không** |

## 7. Vướng vấp

1. **`git fetch` public repo báo `bad object refs/desktop.ini`** — Windows thả `desktop.ini` vào refs. Hậu quả nếu bỏ qua: tưởng remote lệch; đã dùng `git ls-tree origin/main` và status local để đối chiếu.
2. **Bộ đếm journal “error_like=24” dễ gây hoảng** vì khớp chữ `error=0` trong SHADOW_SUMMARY. Hậu quả nếu bỏ qua: báo sai hệ đang lỗi nặng; đã tách traceback=0 và serious=0.
3. **model_count MT/MB < 15** dù pool eligible=15 — nếu chỉ nhìn pool sẽ tưởng đủ phiếu. Hậu quả: ẩn thiếu model trong bundle ngày.
4. **V10965b từng nằm dưới tên folder V10965** — cổng A55 không nhận. Hậu quả: tưởng đã báo cáo đủ trong khi version `b` vẫn FAIL.

## 8. Gỡ về

Không đổi runtime VPS. Gỡ tài liệu/báo cáo:

```text
# Private: revert commit V10969 (docs + script kiểm)
git checkout <commit_truoc> -- CHANGELOG.md docs/CURRENT_TRUTH_SSOT.md docs/FOLLOW_UP_TRACKER.md docs/AUTOMATION_STATE.json web/backend/_v10969_kiem_tong_luc.py

# Public: xoa thu muc bao cao neu can
rmdir /s /q E:\Lottery_AI_Notion_Reports\V10969_KIEM_TONG_LUC_HET_LIVE_20260802
```

Thời gian: < 2 phút. Không cần restore DB.

## 9. Theo dõi tiếp

- **FU-215 · DB0808 · Đóng băng đường ra số (QD-014) · hạn 08/08** — ngưỡng: tới hết 08/08 không đổi roster/combo/override trừ owner mở khoá.
- **FU-208 · KS0808 · Kiểm soát cổng lợi thế · hạn 08/08** — ngưỡng mở: lợi thế ≥ **+3,0pp** và **z ≥ 2,0** trên cửa sổ 90 ngày (hiện cả 3 miền âm).
- **FU-225 · UI0803 · Xác minh UI du-doan-test + filter · hạn 03/08** — owner mở tay 3 miền + `/filter` sau V10964b.
- **FU-189 · KS0802-1 · Xác minh lane nghỉ vắng · hạn 02/08** và **FU-184 · KS0802-2 · MT/MB công bố đúng phiếu · hạn 02/08** — hôm nay bundle MT 13 / MB 14 model: cần đối chiếu với kỳ vọng “đủ phiếu” trong phiên riêng nếu owner muốn đóng.
- Rà **08/08**: QD-014 hết hạn đóng băng → mới xét QD-018 (tắt optimizer / đo 105 luật / gỡ RULES-FIRST) từng bước.
