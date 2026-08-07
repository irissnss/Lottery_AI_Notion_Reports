# -*- coding: utf-8 -*-
"""V11025 (A1) — DI TRÚ: dựng khoá bền + sổ khoá + nhãn giai đoạn trên DB THẬT.

Chạy được nhiều lần, không hỏng gì (mọi bước đều idempotent).
KHÔNG đụng 4 bảng khoá — chỉ `mined_rule_effectiveness` + bảng mới `rule_key_registry`.

    python web/backend/_v11025_di_tru.py            # THỬ KHÔ, in ra sẽ làm gì
    python web/backend/_v11025_di_tru.py --lam-that
"""
from __future__ import annotations

import hashlib
import os
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
GOC = os.path.abspath(os.path.join(H, "..", ".."))
DB = os.path.join(GOC, "data", "lottery_ai.db")
BANG_KHOA = ("predictions", "final_bundles", "lottery_results", "model_daily_eval")

import _v11025_khoa_luat_ben as K  # noqa: E402


def _bam4(con) -> dict:
    """Băm nội dung 4 bảng khoá.

    CẨN THẬN — bản đầu của hàm này SAI và suýt báo động giả. Nó băm `repr(r)` trong khi lời gọi
    đã đặt `con.row_factory = sqlite3.Row`, nên `repr` ra chuỗi kiểu
    `<sqlite3.Row object at 0x000001C4...>` — tức băm **địa chỉ bộ nhớ**, đổi mỗi lần chạy.
    Kết quả: script báo "4 bảng khoá ĐÃ ĐỔI" trong khi cổng độc lập
    `cong_bam_4_bang_khoa.py` (không đặt row_factory) báo Y HỆT — và cổng độc lập mới đúng.
    Nay ép `row_factory=None` trong đúng phạm vi băm.
    """
    cu = con.row_factory
    con.row_factory = None
    try:
        ra = {}
        for b in BANG_KHOA:
            h = hashlib.sha256()
            for r in con.execute(f"SELECT * FROM {b} ORDER BY rowid"):
                h.update(repr(r).encode("utf-8", "replace"))
            ra[b] = h.hexdigest()[:16]
        return ra
    finally:
        con.row_factory = cu


def main() -> int:
    that = "--lam-that" in sys.argv
    print("=" * 96)
    print("  V11025 DI TRÚ — khoá bền cho bằng chứng luật" +
          ("   ⚠ LÀM THẬT" if that else "   (THỬ KHÔ)"))
    print("=" * 96)
    print(f"  DB: {DB}")

    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    bam_truoc = _bam4(con)
    n_truoc = con.execute("SELECT COUNT(*) FROM mined_rule_effectiveness").fetchone()[0]
    print(f"  MRE trước: {n_truoc:,} dòng")
    print(f"  băm 4 bảng khoá TRƯỚC: {bam_truoc}")

    if not that:
        con.close()
        print("\n  (THỬ KHÔ — chưa ghi gì. Chạy lại với `--lam-that`.)")
        return 0

    print("\n  1. nâng cấp lược đồ    :", K.nang_cap_luoc_do(con))
    print("  2. điền khoá cho MRE   :", f"{K.dien_khoa_cho_mre(con):,} dòng")
    print("  3. gieo mầm sổ khoá    :", K.gieo_mam_registry(con))
    print("  4. nối lại rule_id     :", K.noi_lai_rule_id(con))
    print("  5. phân loại giai đoạn :", K.phan_loai_giai_doan(con))
    con.commit()

    n_sau = con.execute("SELECT COUNT(*) FROM mined_rule_effectiveness").fetchone()[0]
    bam_sau = _bam4(con)
    tk = K.thong_ke(con)
    con.close()

    print(f"\n  MRE sau: {n_sau:,} dòng  "
          f"{'✓ KHÔNG mất dòng nào' if n_sau == n_truoc else '✗ MẤT ' + str(n_truoc - n_sau)}")
    giu = all(bam_truoc[b] == bam_sau[b] for b in BANG_KHOA)
    print(f"  băm 4 bảng khoá SAU  : {'✓ Y HỆT' if giu else '✗ ĐỔI — ' + str(bam_sau)}")
    print(f"\n  Thống kê: {tk}")
    print("\n  Đọc con số này cho đúng: ĐO TIẾN gần 0 là ĐÚNG — chưa dòng cũ nào chứng minh")
    print("  được là đo tiến. Nó bắt đầu tăng từ ngày mai và KHÔNG BỊ XOÁ nữa.")
    return 0 if (n_sau == n_truoc and giu) else 1


if __name__ == "__main__":
    raise SystemExit(main())
