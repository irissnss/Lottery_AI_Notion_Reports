# V10968 — Gộp tài liệu cơ chế học + chốt giờ cấm deploy

**Ngày:** 02/08/2026 · **Commit riêng:** `8f49d21` (nội dung chính `4aed49b` + archive/evidence) · **Commit công khai:** `b87e602` · **Trạng thái:** HOÀN TẤT (không deploy VPS)

---

## 1. Tóm tắt

Hai sai sót phiên hôm nay đã được khắc phục trên máy local: (1) hai tài liệu trùng chủ đề cơ chế học được gộp thành **một bản chính** `docs/CO_CHE_HOC_VA_XEP_HANG.md`, bản rút chuyển archive; con số dùng với owner là **~18 cơ chế đang chạy**, trong đó **~7 đụng số công bố**. (2) Hook `governance_guard.py` chặn deploy trong **05:00–06:30** và **15:30–18:15** giờ Việt Nam, có đường thoát `DEPLOY_KHAN=1` kèm nhật ký. Ba phép thử máy đều đạt. Không đụng đường ra số (QD-014), không deploy VPS.

## 2. Owner yêu cầu gì (nguyên văn)

> Hai việc dọn dẹp nhỏ, khắc phục hai sai sót trong phiên hôm nay… Gộp hai tài liệu trùng chủ đề… Giữ `docs/CO_CHE_HOC_VA_XEP_HANG.md` làm bản chính… Chuyển bản rút gọn vào `docs/archive/`… Nếu con số giữa hai bản khác nhau… thì nói rõ vì sao khác…

> Hôm nay có hai lần deploy khởi động lại dịch vụ trong giờ nguy hiểm… Một lần lúc **17:28:06**, trong khi chuỗi miền Bắc chạy lúc **17:30**. Chỉ cách **2 phút**… Cần một chốt chặn bằng máy… Đề xuất khung cấm: **05:00–06:30** và **15:30–18:15** giờ Việt Nam. Bạn tự xem lại crontab thật trên VPS rồi chốt khung cho chuẩn… Phải có đường thoát… `DEPLOY_KHAN=1`… Dùng giờ Việt Nam… Dán kết quả ba phép thử vào báo cáo.

> Dùng version **V10968**… Đẩy hai repo… **KHÔNG đụng Notion.**

## 3. Đào bới / phát hiện

### Tài liệu
- Bản đầy đủ đã có bảng ~25 hàng (sống + chết) và đếm ~18 sống; bản rút đếm ~14 theo nhóm A–F.
- Nội dung bản rút còn thiếu trên bản đầy đủ (đã bổ sung): bảng trọng số optimizer 4 tầng × 3 miền; bảng same-day MN/MT/MB; ghi chú đơn vị mẫu LSTM; `runtime_reliability_model_daily`; Phase-15; khung “có ích / chạy cho có / hại”.

### Crontab / playbook (VPS `14.225.224.89`, đọc 02/08)
- Sáng: Free ML / AI MN khoảng **05:00–05:15**; các job lane/ranker tới **06:30** (`_v10646_retrain_guard`).
- Chiều: lane MN từ **15:36+**; T-chốt/freeze MN→MT→MB; AI MT ~**16:42**; AI MB ~**17:30–17:42**; FINAL **15:45 / 16:58 / 17:58**; `consistency_guard` **18:05**.
- Khung cấm chốt: **05:00–06:30** và **15:30–18:15** Asia/Ho_Chi_Minh — khớp đề xuất owner sau khi đối chiếu crontab thật.

### Ba phép thử (máy local)

| # | Giả lập | Kết quả |
|---|---|---|
| 1 | `DEPLOY_GUARD_NOW_VN=17:28` + lệnh deploy | **`permission: deny`** — thông báo khung cấm + giờ an toàn |
| 2 | `DEPLOY_GUARD_NOW_VN=14:00` | **Không deny vì giờ** — tiếp tục cổng tài liệu (`ask` vì working tree còn thiếu surface sync — đúng hành vi cũ) |
| 3 | `17:28` + `DEPLOY_KHAN=1` | **Không deny vì giờ** + ghi `artifacts/deploy_khan_overrides.jsonl` |

Bằng chứng: `evidence/v10968_deploy_window_tests.json`, `evidence/deploy_khan_overrides.jsonl`.

## 4. Hướng xử lý và vì sao chọn

1. **Gộp tài liệu:** giữ bản đầy đủ (đã có bằng chứng số WR vs BT +47pp) làm SSOT; archive bản rút thay vì xoá — đúng yêu cầu owner và tránh mất lịch sử.
2. **Chốt giờ trong hook có sẵn** thay vì script riêng: mọi lệnh deploy đã đi qua `beforeShellExecution` + `DEPLOY_PATTERNS`/`DEPLOY_REGEXES`; thêm phép giờ cùng chỗ không tạo bề mặt thứ hai để quên.
3. **`DEPLOY_KHAN=1` thay vì khoá cứng:** vẫn sửa được lỗi chảy trong giờ nguy hiểm, nhưng mọi lần thoát đều để dấu.
4. **Không chọn chặn theo từng job riêng:** quá mỏng manh khi lịch đổi; hai cửa sổ bao phủ chuỗi sáng MN và cả chiều MN→MB.

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `docs/CO_CHE_HOC_VA_XEP_HANG.md` | Bản chính; bổ sung thiếu từ bản rút; giải thích đếm 14 vs 18 |
| `docs/archive/CAC_CO_CHE_HOC_CUA_HE.md` | Chuyển archive + dòng đầu ĐÃ GỘP V10968 |
| `docs/CAC_CO_CHE_HOC_CUA_HE.md` | Không còn ở `docs/` |
| Liên kết SSOT / FU / ledger / AUTOMATION_STATE | Trỏ bản chính |
| `.cursor/hooks/governance_guard.py` | Chốt giờ VN + KHAN log + UTF-8 stdout |
| `CHANGELOG.md` / `CURRENT_TRUTH_SSOT.md` / `FOLLOW_UP_TRACKER.md` | prepend V10968 |
| `docs/AUTOMATION_STATE.json` | `governance_seq` 385 → **386** |
| `artifacts/v10968_deploy_window_tests.json` | Kết quả 3 phép thử |

Backup: không sửa runtime VPS; file hook/docs nằm git — rollback = checkout commit trước. **Không deploy VPS.**

## 6. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| Ba phép thử giờ deploy | **Đạt** (deny / không-deny-giờ / KHAN+log) |
| Bản rút còn trong `docs/`? | **Không** — chỉ `docs/archive/` |
| Liên kết còn trỏ path cũ sống? | Đã sửa các mặt người đọc; CHANGELOG lịch sử V10965 giữ nguyên chữ cũ |
| Deploy VPS | **Không làm** (đúng ràng buộc) |
| Notion ghi | **Không** (A55) |
| QD-014 roster/combo | **Không đụng** |

## 7. Vướng vấp

1. **PowerShell nuốt backtick** khi ghi dòng đầu archive bằng `Set-Content` — phải ghi lại bằng script Python. Hậu quả nếu bỏ qua: dòng archive thiếu path markdown, khó click.
2. **In JSON tiếng Việt trên console Windows cp1252** làm crash phép thử deny lần đầu — đã `stdout.reconfigure(utf-8)` trong hook. Hậu quả nếu bỏ qua: hook vỡ giữa đường, Cursor không nhận được `deny`.
3. **Phép thử ngoài khung trả `ask` (thiếu doc sync)** chứ không `allow` thuần — vì working tree bẩn. Không phải lỗi chốt giờ; cần đọc đúng: chốt giờ chỉ chịu trách nhiệm không `deny` vì giờ.

## 8. Gỡ về

```bash
# Private repo
git checkout <commit_truoc_V10968> -- .cursor/hooks/governance_guard.py docs/CO_CHE_HOC_VA_XEP_HANG.md
# Khôi phục bản rút từ archive nếu cần đọc lại riêng:
copy docs\archive\CAC_CO_CHE_HOC_CUA_HE.md docs\CAC_CO_CHE_HOC_CUA_HE.md
```

Thời gian gỡ: < 2 phút. Không ảnh hưởng VPS (chưa deploy).

## 9. Theo dõi tiếp

- **FU-236 · DD0802 · Gộp tài liệu cơ chế học · hạn 02/08** — CLOSED trong phiên.
- **FU-237 · DP0815 · Canh chốt giờ cấm deploy · hạn 15/08** — ngưỡng: tới 09/08 không có restart service trong khung cấm trừ khi có dòng `DEPLOY_KHAN` trong log; rà 15/08.
