# V10841 — Bugbot toàn diện vòng 3 và xử lý dứt điểm

Ngày: 23/07/2026, 22:28–23:1x VN  
Phạm vi: TOTAL-V2 shadow/lane, rule-condition shadow/lane, AE money board, API/panel monitoring.  
Yêu cầu owner: tiếp tục `/review-bugbot` toàn diện; xử lý được thì xử lý, mục cần live thì ghi lịch; báo cáo đầy đủ và push GitHub.

## 1. Kết quả Bugbot vòng 3

| Severity | Vị trí | Finding |
|---|---|---|
| High | `_v10821_total_v2_shadow.py:445` | `compute_view()` dùng ngày naive; có thể lệch ngày VN trong cửa 00:00–06:59 nếu process UTC |
| High | `_v10829_rule_cond_shadow.py:29` | Import module tự thay `sys.stdout`, có thể đóng wrapper của API/scheduler |
| Medium | `_v10821_total_v2_shadow.py:199` | Filter `run_source != 'shadow'` xử sai NULL và không đồng nhất với các module khác |
| Medium | `_v10821_total_v2_shadow.py:333` | Cache trial-day không invalidated sau catchup/backfill |
| Medium | `_v10829_rule_cond_shadow.py:919` | Rule-cond view cũng dùng ngày naive |

Ngoài 5 finding trên, phiên này đóng luôn Bugbot vòng 2 Medium: bộ canon tĩnh money board có thể lệch registry động.

## 2. Đo tác hại trước khi sửa

- Vote-pool mismatch: **0/225 canon rows forward** (19–23/07) và **0/6.644 canon rows 180 ngày** có `run_source NULL` hoặc `shadow%`. Fix không đổi picks/số liệu lịch sử.
- Hai lỗi ngày VN chỉ chạm API preview/hint/readout trong cửa biên. Cron materialize chạy 20:50/21:00 VN nên không nằm cửa lỗi; không có bằng chứng làm sai bảng official.
- Cache stale chỉ chạm panel dispersion `%inrules`, không feed writer/selector.
- Stdout side-effect đã tái hiện trong các probe điều tra (`I/O operation on closed file`), nhưng không tìm thấy row lane bị mất hoặc official table bị sửa.
- Canon động hiện trả đúng 15 model cho cả MN/MT/MB, khớp fallback tĩnh; wire động không đổi gate outcome hiện tại.

**Kết luận tác hại:** lỗi kỹ thuật là thật nhưng phần lớn là latent/diagnostic. Không có bằng chứng 5 finding vòng 3 làm sai `/du-doan`, kết quả xổ hoặc 4 bảng official.

## 3. Fix đã thực hiện

1. **Ngày VN explicit:** `_today_vn_str()` / `_today_vn()` dùng `vn_now()` và fallback UTC+7; áp vào API view và CLI catchup.
2. **Không import-side-effect:** bỏ wrap stdout module-level ở V10829; chỉ wrap trong `__main__`.
3. **Vote pool thống nhất:** `LOWER(COALESCE(run_source,'')) NOT LIKE '%shadow%'`.
4. **Cache đúng:** chỉ cache baseline lịch sử đóng; trial dispersion luôn đọc DB mới, nên catchup/backfill phản ánh ngay.
5. **Canon một SSOT:** `get_output_eligible_ids(region)` + fallback tĩnh trong money board.

## 4. Verify

### Local
- `py_compile` 4 module: PASS.
- Import V10829 giữ nguyên identity `sys.stdout`: PASS.
- TOTAL-V2 + rule-cond `compute_view`: `success=True`, đủ MN/MT/MB.
- Date helper: 2026-07-23 (VN).
- Vote pool: 15 model/miền.
- Dynamic canon: 15/15 cả 3 miền.
- Dispersion cache: chỉ key `base`.
- Lane V3 dry-run: chạy sạch.

### VPS
- Backup: `/root/backups_v10841/`.
- SHA 3 file local/VPS: khớp.
- Behavior check trước và sau restart: PASS.
- Service active; `/api/health=200`; admin TOTAL-V2/rule-cond = 401.
- Journal errors: 0.
- Hash 4 bảng pre=post **IDENTICAL**:
  - predictions `fce6bae9`
  - final_bundles `60e876fa`
  - lottery_results `066d773b`
  - model_daily_eval `bfb0670f`

## 5. Vì sao audit nhiều vòng vẫn còn finding?

1. V10828 ban đầu là hotfix phản xạ trong đêm; policy bị sao chép ở nhiều module thay vì một SSOT.
2. Các vòng đầu có lần diff rỗng/giới hạn scope; vòng sau mới ép tìm edge case liên module.
3. Trước V10841 chưa có contract test chung cho ngày VN, stdout import, vote-pool, cache invalidation và registry.

Đây là nợ kỹ thuật thật của cách làm phản xạ, không nên ngụy biện. Tuy nhiên cũng phải phân biệt: **finding tiềm ẩn/readout không đồng nghĩa official đã sai**. V10841 đã chuẩn hóa 4 contract ở playbook để không tái phạm.

## 6. Mục chờ live

- 24/07 trong cửa 00:00–06:59 VN: API hai panel nhận đúng ngày VN, lane V3 không lỗi stdout.
- Sau cron 20:50: dispersion nhận union mới không cần restart.

Không còn code finding mở. FU-V10838B đã CLOSED.
