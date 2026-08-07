# -*- coding: utf-8 -*-
"""V11028 (A5) — ĐO LẠI khẳng định «84/84 khoảng tin cậy đặc trưng ML đều chứa 0,50».

Khẳng định này đang là **căn cứ duy nhất** để TỪ CHỐI MẶC ĐỊNH bước 3 của FU-300 (đưa rules
thành đặc trưng ML) theo doctrine M3. Tra soát V11024 (R6) đo lại ra **80/84** trên bản CSV
tươi ở VPS và **75/84** trên bản local đã cũ — và **không tìm được script gốc** nào sinh ra con
số 84/84.

Tệp này đo lại **độc lập**, chạy được trên cả local lẫn VPS, để con số công bố có script tái lập
(chuẩn E4).

**Cách đo:** với mỗi (miền × đặc trưng), tính AUC của đặc trưng đó so với nhãn trúng/trượt, rồi
dựng khoảng tin cậy 95% bằng công thức **Hanley–McNeil**. Khoảng CHỨA 0,50 nghĩa là đặc trưng
đó **không phân biệt được** trúng với trượt.

**Nói thật về giới hạn:** Hanley–McNeil giả định các quan sát ĐỘC LẬP. Ở đây nhiều dòng cùng một
ngày nên có tương quan cụm-ngày, khoảng thật **rộng hơn** khoảng tính ra. Nghĩa là số đặc trưng
"không chứa 0,50" mà ta đếm được là **cận trên** — thực tế còn ít hơn.

    python web/backend/_v11028_do_lai_84_ktc.py
"""
from __future__ import annotations

import csv
import io
import math
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

GOC = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
MIEN = ("MN", "MT", "MB")
COT_BO = {"date", "region", "tail", "label", "y", "target", "hit"}


def _auc(x: list[float], y: list[int]) -> tuple[float, int, int]:
    """AUC bằng thống kê hạng Mann–Whitney (xử lý đồng hạng bằng hạng trung bình)."""
    n1 = sum(y)
    n0 = len(y) - n1
    if n1 == 0 or n0 == 0:
        return float("nan"), n0, n1
    cap = sorted(zip(x, y), key=lambda t: t[0])
    hang = [0.0] * len(cap)
    i = 0
    while i < len(cap):
        j = i
        while j + 1 < len(cap) and cap[j + 1][0] == cap[i][0]:
            j += 1
        tb = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            hang[k] = tb
        i = j + 1
    tong_hang_1 = sum(h for h, (_, lab) in zip(hang, cap) if lab == 1)
    return (tong_hang_1 - n1 * (n1 + 1) / 2.0) / (n0 * n1), n0, n1


def _ktc(auc: float, n0: int, n1: int) -> tuple[float, float, float]:
    """Khoảng tin cậy 95% Hanley–McNeil."""
    q1 = auc / (2 - auc)
    q2 = 2 * auc * auc / (1 + auc)
    se = math.sqrt((auc * (1 - auc) + (n1 - 1) * (q1 - auc ** 2)
                    + (n0 - 1) * (q2 - auc ** 2)) / (n0 * n1))
    return auc - 1.96 * se, auc + 1.96 * se, se


def main() -> int:
    print("=" * 100)
    print("  A5 — ĐO LẠI «84/84 khoảng tin cậy đặc trưng ML đều chứa 0,50»")
    print("=" * 100)
    tong, chua, khong, thieu = 0, 0, [], []
    for m in MIEN:
        p = os.path.join(GOC, "data", f"meta_training_{m}.csv")
        if not os.path.exists(p):
            thieu.append(p)
            continue
        with io.open(p, encoding="utf-8", errors="replace", newline="") as fh:
            dr = csv.DictReader(fh)
            hang = list(dr)
        if not hang:
            thieu.append(p + " (rỗng)")
            continue
        cot_nhan = next((c for c in ("label", "y", "target", "hit") if c in hang[0]), None)
        if not cot_nhan:
            thieu.append(p + f" (không thấy cột nhãn trong {list(hang[0])[:8]})")
            continue
        dac = [c for c in hang[0] if c not in COT_BO]
        y = [int(float(r[cot_nhan] or 0)) for r in hang]
        print(f"\n  ── {m}: {len(hang):,} dòng · {len(dac)} đặc trưng · "
              f"nhãn `{cot_nhan}` (trúng {sum(y)}, trượt {len(y) - sum(y)})")
        for c in dac:
            try:
                x = [float(r[c]) if r[c] not in ("", None) else 0.0 for r in hang]
            except ValueError:
                continue
            a, n0, n1 = _auc(x, y)
            if a != a:
                continue
            lo, hi, se = _ktc(a, n0, n1)
            tong += 1
            if lo <= 0.50 <= hi:
                chua += 1
            else:
                khong.append((m, c, a, lo, hi))
    if thieu:
        print("\n  ⚠ THIẾU NGUỒN:")
        for t in thieu:
            print(f"      {t}")
    print()
    print("=" * 100)
    print(f"  KẾT QUẢ: {chua}/{tong} khoảng tin cậy CHỨA 0,50 · {len(khong)} KHÔNG chứa")
    print("=" * 100)
    for m, c, a, lo, hi in khong:
        print(f"    {m}  {c:<24} AUC {a:.4f}  KTC [{lo:.4f}, {hi:.4f}]  ✗ KHÔNG chứa 0,50")
    print()
    print("  Đọc cho đúng: Hanley–McNeil giả định quan sát ĐỘC LẬP. Ở đây nhiều dòng cùng một")
    print("  ngày nên có tương quan cụm-ngày ⇒ khoảng THẬT rộng hơn ⇒ số 'KHÔNG chứa' đếm được")
    print("  là CẬN TRÊN, thực tế còn ít hơn.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
