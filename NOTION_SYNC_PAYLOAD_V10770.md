# V10770 — MB mốc-điều-kiện: đầu tháng sameday, còn lại D-1 (nâng V10767)

**Ngày:** 2026-07-02 (UTC+7) · **Loại:** OFFICIAL (MB only, bundle tương lai) · **Rollback:** 2 tầng flag

## Bối cảnh (owner)
Owner đề xuất đào ML MB theo điều kiện thời gian: "đầu tháng verify dữ liệu sameday, cuối tháng thì D-1, hoặc xen kẽ tuần này tuần kia" trên 115+ ngày live. Sau khi backtest validate, owner chọn **deploy**.

## Bằng chứng (backtest 63d, causal, MB cost 27k) — validate + không overfit
Pattern LẶP LẠI cả tháng 5 VÀ tháng 6:
| Pha | Tháng 5 | Tháng 6 |
|---|---|---|
| Đầu (1-10) | sameday thắng | sameday thắng (+17.1M) |
| Cuối (21-31) | D-1 thắng (+19.3M) | D-1 thắng (+7.3M) |

Rule (dom≤10 → sameday, else → D-1):
| | Rule điều kiện | V10767 fixed-D-1 |
|---|---|---|
| Nửa cũ | +22.3M | −2.2M |
| Nửa mới | +8.5M | +3.6M |
| **Full 63d** | **+30.8M** | +1.4M |

Hôm nay 02/07 (dom=2, đầu tháng): rule dùng sameday → **38-29** (VPS smoke), **38 = số MB về hôm nay** — sửa đúng ngày V10767 pure-D-1 (56-88) miss.

## Thay đổi kỹ thuật (V10770)
- `_v10767_mb_prevday_override.py`: thêm `_sameday_plurality()` + `_mb_ml_plurality()` + gate `_V10770_CONDITIONAL_MILESTONE=True` (`_V10770_EARLY_MONTH_DOM=10`).
- `maybe_override_mb` rẽ nhánh: dom≤10 → sameday (MB ML-plurality HÔM NAY, 17:00 pre-MB-draw, causal); else → D-1 (V10767).
- champion-challenger log ghi milestone dùng mỗi ngày.
- **Rollback 2 tầng:** `_V10770_CONDITIONAL_MILESTONE=False` → pure D-1 (V10767); `_V10767_MB_PREVDAY_ENABLED=False` → aggregate cũ.

## An toàn / verify VPS
- compile OK; flag present; smoke đúng (dom=2→sameday 38-29; dom=25→D-1 35-92); health=200; `/du-doan`=200.
- **hash-guard 4 official IDENTICAL** (áp dụng từ MB 03/07). Backup nhiều lớp: `backups/v10770_remote_pre/` + VPS `.v10770_pre.bak` + git + 2 flag.

## Kèm review "1 lượt" (owner yêu cầu)
- **AI sau de-herd (V10768) ngày đầu 02/07:** MN 6/7 BT-hit, MT 3/7 BT+3 lo, MB 4/7 BT; model KHÔNG còn xúm 1 số (de-herd có tác dụng). NHƯNG 1 ngày = nhiễu → theo dõi ~1 tuần (checkpoint 08/07).
- **Method/output total:** MN weighted+specialist+de-herd; MT +nt_consensus+V10766+de-herd; MB +V10770. MN/MT official HIT ngày đầu.

## Checkpoint
07/07 theo dõi MB forward qua champion-challenger log; tụt bất thường → rollback flag.
