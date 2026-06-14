# V10720 — OOS BT Audit + Tín hiệu đơn-model + Thiết kế UI per-position (14/06/2026)

**Loại:** READ-ONLY audit + sửa UI lane-test (admin). KHÔNG đụng official/predictions/final_bundles.
**Data as-of:** 2026-06-14. **Window đo:** 2026-05-15 → 2026-06-14 (~1 tháng, đã settle).

---

## 0. TÓM TẮT (đọc nhanh)
1. **ĐÍNH CHÍNH:** Tuyên bố trước đây "lane test BT +299tr, official −53.8tr (1 tháng)" là **NÓI QUÁ** — do gom phương pháp tốt-nhất-từng-miền (selection bias) + bỏ qua MT thua + không nêu khoảng tin cậy/1-window. KHÔNG bịa (MN/MB có vượt thật trong window này) nhưng **chưa đủ chắc để công bố là "thắng".**
2. **PHÁT HIỆN GỐC (luận điểm owner đúng):** output (bản gộp) bị chặn bởi chất lượng tín hiệu **ĐƠN-MODEL**. MN/MT model mạnh, MB còn yếu (đang xây lại). Đặc biệt: với MT/MB, **bản gộp official đang TỆ HƠN trung bình đơn-model** → bộ gộp đang kéo tín hiệu xuống.
3. **CHUẨN HOÁ UI (V10715–V10719):** card "Phương pháp riêng cho từng số" = mỗi vị trí (BT/SP1/SP2) một phương pháp ĐỘC LẬP, chọn theo hit-rate **độc lập miền × thứ**, pool chỉ method chuyên biệt (loại XIEN combo + OUTPUT multidir). Áp đồng nhất cả 3 miền.

---

## 1. ĐÍNH CHÍNH "+299tr" — đo OOS có thống kê (Wilson CI95)
Metric: `test_bt_status` (BT lô-style, cùng nguồn cho mọi method + official). "VƯỢT CHẮC" = CI-dưới của method > win-rate official.

| Miền | Official BT lô | Method vượt CHẮC | Ghi chú |
|---|---|---|---|
| MN | 48.4% (30/62) | ADAPTIVE_EXPLOIT / HYBRID 64.5% [52–75%] | 2 method trùng nhau (1 tín hiệu) |
| MT | 32.4% (22/68) | **KHÔNG có** (mọi CI chồng official) | MT: 0 tín hiệu vượt |
| MB | 12.9% (4/31) | PRIOR_REGION_CONTEXT 29% [16–47%] | PRIOR_REGION ở MN = 0% (ngược hẳn) |

- **Nhân quả OK:** method top tạo cùng-ngày (gap=0), không backfill → không rò rỉ.
- **Nhưng:** multiple-comparison (~45 phép so → kỳ vọng ~2 "đẹp" do may) + chỉ 1 window + method vượt khác nhau từng miền (không tổng quát) → **ứng viên hứa hẹn, CHƯA đủ chắc để áp.** Cần window thứ 2 độc lập.

## 2. CHẤT LƯỢNG TÍN HIỆU ĐƠN-MODEL (28 model/miền)
| Miền | OFFICIAL (gộp) | TB đơn-model | Top model | Kết luận |
|---|---|---|---|---|
| MN | **48.4%** | 42.6% | gpt-5.5 54.8% | gộp > TB → aggregation CÓ giá trị ✓ |
| MT | **32.3%** | 37.1% | deepseek-reasoner 48.4% | ⚠️ gộp < TB → **aggregation đang kéo xuống** |
| MB | **16.1%** | 20.1% | gpt-5.4 29% | ⚠️ gộp < TB + model còn yếu (đang xây lại) |

→ **Đòn bẩy thật cho MT/MB không phải model — mà là bộ GỘP/override** (official MT thậm chí < combo-no-token 45%). MB thêm yếu tố model-non, cần thời gian + dữ liệu.

## 3. THIẾT KẾ UI per-position (V10715–V10719, đã deploy)
- **V10715:** fix endpoint MB lùi-cả-trang (tách `legacy_date` khỏi `data_date`) + card doctrine MB LIVE.
- **V10716:** card MB hiện sớm (cron 17:45) + fix 3 endpoint admin V105.24 chết (graceful).
- **V10717:** fix `git reset --hard` xoá +x file .sh (cron lane Permission denied) — chmod + bash-cron + git 100755.
- **V10718:** chuẩn hoá ranker MB: thêm rerank 04:45 (same-day trước predict) — khớp MN/MT.
- **V10719:** card số phụ MN/MT/MB chọn method chuyên biệt theo (miền×thứ), **loại XIEN/OUTPUT**.
- **Xác nhận thiết kế:** card "Phương pháp riêng" = BT/SP1/SP2 mỗi vị trí 1 method độc lập, độc lập miền×thứ — đúng hướng. Card "Output Lane Test (multidir)" tạm GIỮ NGUYÊN theo quyết định owner.

## 4. KẾ HOẠCH + MỐC
- **Giữ đo forward (chưa áp):** MN `ADAPTIVE_EXPLOIT`(+HYBRID), MB `PRIOR_REGION_CONTEXT`. MT: giữ official.
- **Gate adopt:** chỉ "elite" nếu vượt official **2 window độc lập** + sống sót hiệu chỉnh multiple-comparison → lúc đó mới rút 15→≤3 method.
- **Giám sát chặt tín hiệu đơn-model hằng ngày** (đặc biệt sau khi doctrine MN/MT ngấm).
- **Mốc:** 15/06 CP-4.0 (cross-region leakage) · **19/06 A/B doctrine MB** · 24/06 doctrine MN/MT · 12/07 confidence layer · window-2 OOS xác nhận ~giữa 07.

**Nguyên tắc:** CẤM dùng số in-sample/cherry-pick làm "thắng". Mọi tuyên bố "method > official" phải OOS + có ý nghĩa thống kê.

STATUS: AUDIT_DONE — official untouched, code_deployed = UI lane-test only (V10715–V10719).
