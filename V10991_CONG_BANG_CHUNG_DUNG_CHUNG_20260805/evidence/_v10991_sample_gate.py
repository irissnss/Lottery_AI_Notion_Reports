# -*- coding: utf-8 -*-
"""V10991 — CỔNG CỠ MẪU DÙNG CHUNG + HIỆU CHỈNH SO SÁNH BỘI.

Owner ký 2026-08-05 (~20:5x): duyệt phương án A — "một quy tắc chung + hiệu chỉnh
so sánh bội, ngưỡng N_min = 12".

VÌ SAO CẦN
==========
Bốn chỗ trong `main.py` cùng chọn method để hiển thị trên `/du-doan-test` đều dùng
lối **lấy cực đại trên nhiều ứng viên** mà không hiệu chỉnh:

    _wd_best()   HAVING n>=4   ORDER BY wins/n DESC LIMIT 1   (bạch thủ theo thứ)
    _best()      total_runs>=10                               (bạch thủ dự phòng)
    _pos_hit()   min_n=6  cửa sổ 90d cùng thứ                 (số phụ, vòng a)
    _pos_hit()   min_n=10 cửa sổ 60d mọi thứ                  (số phụ, vòng b)

Lấy max trên m ứng viên thì kỳ vọng của cực đại **luôn cao hơn** năng lực thật.
Với n=4 và tỉ lệ nền ~30%, xác suất CÓ ÍT NHẤT MỘT ứng viên đạt 4/4 trong 20 method
là ~15%; đạt >=75% là ~80%. Con số "62% BT hit/T3, n=8" in trên trang vì thế gần như
chắc chắn là **may rủi được chọn ra**, không phải năng lực.

QUY TẮC (một, dùng cho cả bốn chỗ)
==================================
Được dán nhãn "đủ bằng chứng" chỉ khi CẢ HAI:
    1. n >= MIN_N (=12)
    2. đuôi nhị thức P(X >= k | n, p_nền) <= ALPHA / m       ← Bonferroni

`m` là **số ứng viên thật sự đem so trong lần chọn đó**, không phải hằng số.
`p_nền` là tỉ lệ gộp của chính nhóm ứng viên đó (mặt bằng cùng kỳ, cùng miền).

KHÔNG ĐẠT ⇒ **VẪN TRẢ SỐ**, chỉ hạ nhãn xuống "chưa đủ bằng chứng".
Đây là §54 owner đã ký: luôn ra số, chỉ nói thật về độ tin cậy.

KHI KHÔNG ỨNG VIÊN NÀO ĐẠT ⇒ rơi về lựa chọn **đăng ký trước**
(`FALLBACK_SUFFIX`, mặc định baseline official), KHÔNG lấy max — vì lấy max lúc đó
chính là lấy nhiễu.

Module thuần tính toán: không đọc DB, không ghi gì, không phụ thuộc module dự án.
"""

from __future__ import annotations

MIN_N = 12            # cỡ mẫu tối thiểu (owner ký 05/08)
ALPHA = 0.10          # mức ý nghĩa TRƯỚC khi chia cho số ứng viên
FALLBACK_SUFFIX = "OFFICIAL_BASELINE_CONTROL"   # lựa chọn đăng ký trước

NHAN_DAT = "đủ bằng chứng"
NHAN_THIEU_MAU = "chưa đủ mẫu"
NHAN_THIEU_BC = "chưa đủ bằng chứng"


def _log_comb(n: int, k: int) -> float:
    """log(C(n,k)) bằng lgamma — tránh tràn số với n lớn."""
    from math import lgamma
    if k < 0 or k > n:
        return float("-inf")
    return lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)


def duoi_nhi_thuc(k: int, n: int, p: float) -> float:
    """P(X >= k) với X ~ Binomial(n, p). Trả 1.0 nếu tham số vô nghĩa."""
    from math import exp, log
    if n <= 0 or k <= 0:
        return 1.0
    if k > n:
        return 0.0
    if p <= 0.0:
        return 0.0 if k > 0 else 1.0
    if p >= 1.0:
        return 1.0
    tong = 0.0
    for i in range(k, n + 1):
        tong += exp(_log_comb(n, i) + i * log(p) + (n - i) * log(1.0 - p))
    # sai số dấu phẩy động có thể đẩy ra ngoài [0,1]
    return min(1.0, max(0.0, tong))


def _lam_tron(x: float) -> float:
    """Làm tròn để IN RA. `round(x, 4)` biến p=2e-05 thành 0.0 — trông như bịa và
    làm người đọc tưởng chắc chắn tuyệt đối. Giữ 3 chữ số có nghĩa cho số rất nhỏ."""
    if x is None:
        return None
    if x == 0.0 or abs(x) >= 1e-4:
        return round(x, 4)
    return float("%.3g" % x)


def danh_gia(k: int, n: int, p_nen: float, so_ung_vien: int) -> dict:
    """Chấm MỘT ứng viên.

    k = số lần trúng · n = số lượt · p_nen = tỉ lệ mặt bằng của nhóm
    so_ung_vien = m, số ứng viên đem so trong CÙNG lần chọn (để hiệu chỉnh Bonferroni)

    Trả dict: dat · p_value · nguong · nhan · pct · n · m
    """
    m = max(1, int(so_ung_vien or 1))
    nguong = ALPHA / m
    pct = round(100.0 * k / n) if n else 0
    if n < MIN_N:
        return {"dat": False, "p_value": None, "nguong": _lam_tron(nguong),
                "nhan": NHAN_THIEU_MAU, "pct": pct, "n": n, "m": m}
    p = duoi_nhi_thuc(k, n, p_nen)
    dat = p <= nguong
    return {"dat": dat, "p_value": _lam_tron(p), "nguong": _lam_tron(nguong),
            "nhan": NHAN_DAT if dat else NHAN_THIEU_BC, "pct": pct, "n": n, "m": m}


def ti_le_nen(ung_vien) -> float:
    """Mặt bằng = tỉ lệ GỘP của chính nhóm ứng viên (tổng trúng / tổng lượt).

    ung_vien: iterable các (ten, k, n). Trả 0.0 nếu không đủ dữ liệu.
    """
    tk = tn = 0
    for _t, k, n in ung_vien:
        tk += int(k or 0)
        tn += int(n or 0)
    return (tk / tn) if tn else 0.0


def chon(ung_vien, fallback_ten: str | None = None) -> dict | None:
    """Chọn ứng viên tốt nhất theo quy tắc trên.

    ung_vien: iterable các (ten, k, n).
    fallback_ten: tên đăng ký trước, dùng khi KHÔNG ứng viên nào đạt.

    Trả None nếu không có ứng viên nào. Ngược lại trả dict:
        ten · pct · n · dat · p_value · nguong · nhan · m · p_nen · la_fallback
    """
    ds = [(str(t), int(k or 0), int(n or 0)) for t, k, n in (ung_vien or []) if n]
    if not ds:
        return None
    m = len(ds)
    p_nen = ti_le_nen(ds)

    cham = []
    for ten, k, n in ds:
        d = danh_gia(k, n, p_nen, m)
        d["ten"] = ten
        d["p_nen"] = round(p_nen, 4)
        d["la_fallback"] = False
        cham.append(d)

    # 1) ưu tiên ứng viên ĐẠT — trong nhóm đạt thì lấy p nhỏ nhất (bằng chứng mạnh nhất),
    #    hoà thì lấy n lớn hơn
    dat = [d for d in cham if d["dat"]]
    if dat:
        dat.sort(key=lambda d: (d["p_value"], -d["n"]))
        return dat[0]

    # 2) không ai đạt → lựa chọn ĐĂNG KÝ TRƯỚC, không lấy max
    if fallback_ten:
        for d in cham:
            if d["ten"] == fallback_ten or d["ten"].endswith(fallback_ten):
                d["la_fallback"] = True
                return d

    # 3) không có fallback trong nhóm → vẫn TRẢ SỐ (không giấu), lấy mẫu lớn nhất
    #    (mẫu lớn nhất ổn định hơn tỉ lệ cao nhất khi cả hai đều chưa đủ bằng chứng)
    cham.sort(key=lambda d: (-d["n"], -d["pct"]))
    cham[0]["la_fallback"] = True
    return cham[0]


def mo_ta(d: dict | None) -> str:
    """Chuỗi ngắn để in kèm số trên giao diện."""
    if not d:
        return ""
    if d.get("dat"):
        return f"{d['pct']}% · n={d['n']} · {NHAN_DAT} (p={d['p_value']}≤{d['nguong']})"
    if d.get("nhan") == NHAN_THIEU_MAU:
        return f"{d['pct']}% · n={d['n']} · {NHAN_THIEU_MAU} (cần n≥{MIN_N})"
    return (f"{d['pct']}% · n={d['n']} · {NHAN_THIEU_BC} "
            f"(p={d['p_value']}>{d['nguong']}, đã chia cho {d['m']} ứng viên)")
