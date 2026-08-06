# -*- coding: utf-8 -*-
"""V10995 — TÁCH BUNDLE LÀM BÙ khỏi dự đoán thật, bằng view TỰ SUY RA.

Owner ký 06/08, chọn hướng (b): *"vậy b nha em. làm đi nhưng nó sẽ đúng và có tính lại
vẫn không bị sợ sơ xuất nha em"*.

VÌ SAO KHÔNG GHI CỘT THẲNG VÀO `final_bundles`
==============================================
Hướng (b) nguyên văn là "đánh cờ `is_backfill` vào bảng rồi lọc theo cờ". Làm đúng chữ
thì vướng hai chỗ:

  1. `final_bundles` là MỘT TRONG BỐN BẢNG KHOÁ. Thêm cột và ghi giá trị là đổi mã băm —
     phá chính cái cổng đang canh số của owner.
  2. Cờ GHI CỨNG có thể LỆCH với thực tế. Thêm bundle làm bù mới mà quên chạy lại lệnh
     cập nhật là cờ sai, mà sai lặng lẽ. Owner dặn "tính lại vẫn không bị sợ sơ xuất" —
     cờ ghi cứng không đạt yêu cầu đó.

Nên cờ ở đây **tự suy ra lúc đọc**, đóng thành view — đúng lối `v_<tên_bảng>` mà dự án đã
dùng cho 54 view sẵn có. Tính lại lúc nào cũng ra đúng, **không có đường nào để lệch**.
Và `final_bundles` **không bị ghi một byte nào**.

QUY TẮC — chỉ có ĐÚNG MỘT chỗ định nghĩa
========================================
    bundle LÀM BÙ  ⇔  date(created_at) > date        (tạo sang ngày khác)
    dự đoán THẬT   ⇔  date(created_at) <= date

Đo 06/08: 385 thật · 90 làm bù · 0 dòng thiếu `created_at`. 90 bản làm bù đều mang
`notes='Phase 1.5 backfill'`, tạo một lượt 30/03 13:42:14, bù cho 28/02→29/03.

DÙNG NHƯ THẾ NÀO
================
Mọi phép đo thành tích đọc `final_bundles` **đổi sang `v_final_bundles_that`**. Không cần
nhớ điều kiện lọc, không sợ quên.

    -- trước
    SELECT ... FROM final_bundles WHERE region=?
    -- sau
    SELECT ... FROM v_final_bundles_that WHERE region=?

Muốn xem riêng phần làm bù thì đọc `v_final_bundles_lam_bu` — nó **không bị giấu đi**,
chỉ được tách ra.

Chạy:
    python _v10995_loc_lam_bu.py            # CHỈ tự kiểm (mặc định — không ghi gì)
    python _v10995_loc_lam_bu.py --dung     # dựng/dựng lại view rồi kiểm
"""
from __future__ import annotations

import argparse
import hashlib
import os
import sqlite3
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

_HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB = os.path.join(os.path.dirname(os.path.dirname(_HERE)), "data", "lottery_ai.db")

# ── ĐỊNH NGHĨA DUY NHẤT. Sửa ở đây là sửa cả hệ. ─────────────────────────────
DIEU_KIEN_LAM_BU = "date(created_at) > date"
DIEU_KIEN_THAT = "date(created_at) <= date"

VIEW_THAT = "v_final_bundles_that"
VIEW_LAM_BU = "v_final_bundles_lam_bu"


def _cot(cur) -> list[str]:
    return [r[1] for r in cur.execute("PRAGMA table_info(final_bundles)")]


def cau_lenh_view(cols: list[str]) -> list[str]:
    """Sinh câu tạo view. Liệt kê cột tường minh + thêm cờ `is_lam_bu` tính sẵn.

    Cờ đi kèm ngay trong view để chỗ nào lỡ đọc view gộp vẫn thấy được, không phải
    nhớ lại điều kiện.
    """
    ds = ", ".join('"%s"' % c for c in cols)
    return [
        "DROP VIEW IF EXISTS %s" % VIEW_THAT,
        "DROP VIEW IF EXISTS %s" % VIEW_LAM_BU,
        # dự đoán THẬT — đây là view mọi phép đo thành tích phải dùng
        "CREATE VIEW %s AS SELECT %s, 0 AS is_lam_bu FROM final_bundles WHERE %s"
        % (VIEW_THAT, ds, DIEU_KIEN_THAT),
        # làm bù — tách ra chứ KHÔNG giấu đi
        "CREATE VIEW %s AS SELECT %s, 1 AS is_lam_bu FROM final_bundles WHERE %s"
        % (VIEW_LAM_BU, ds, DIEU_KIEN_LAM_BU),
    ]


def _bam_bang(cur) -> tuple[str, int]:
    """Mã băm của `final_bundles` — để CHỨNG MINH bảng khoá không bị ghi."""
    h = hashlib.sha256()
    n = 0
    for row in cur.execute("SELECT * FROM final_bundles ORDER BY id"):
        h.update(repr(tuple(row)).encode("utf-8", "replace"))
        n += 1
    return h.hexdigest(), n


def dung_view(db_path: str) -> None:
    con = sqlite3.connect(db_path, timeout=30)
    try:
        con.execute("PRAGMA busy_timeout=30000;")
        cur = con.cursor()
        truoc = _bam_bang(cur)
        for cau in cau_lenh_view(_cot(cur)):
            con.execute(cau)
        con.commit()
        sau = _bam_bang(con.cursor())
        if truoc != sau:
            raise SystemExit("✗ DỪNG — final_bundles bị đổi khi dựng view. Không được phép.")
        print("  ✓ đã dựng %s và %s · final_bundles KHÔNG đổi (%d dòng, băm %s…)"
              % (VIEW_THAT, VIEW_LAM_BU, sau[1], sau[0][:16]))
    finally:
        con.close()


def tu_kiem(db_path: str) -> int:
    """Sáu phép. Mục đích: chứng minh KHÔNG MẤT DÒNG, KHÔNG ĐẾM HAI LẦN, KHÔNG LỆCH."""
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    cur = con.cursor()
    truot: list[str] = []
    try:
        for v in (VIEW_THAT, VIEW_LAM_BU):
            if not cur.execute("SELECT 1 FROM sqlite_master WHERE type='view' AND name=?",
                               (v,)).fetchone():
                truot.append("thiếu view %s" % v)
        if truot:
            print("  " + "\n  ".join("✗ " + x for x in truot))
            return 1

        tong = cur.execute("SELECT COUNT(*) FROM final_bundles").fetchone()[0]
        n_that = cur.execute("SELECT COUNT(*) FROM %s" % VIEW_THAT).fetchone()[0]
        n_bu = cur.execute("SELECT COUNT(*) FROM %s" % VIEW_LAM_BU).fetchone()[0]
        thieu = cur.execute(
            "SELECT COUNT(*) FROM final_bundles WHERE created_at IS NULL OR TRIM(created_at)=''"
        ).fetchone()[0]

        print("  final_bundles %d dòng = thật %d + làm bù %d" % (tong, n_that, n_bu))
        if n_that + n_bu != tong:
            truot.append("MẤT/THỪA dòng: %d + %d != %d" % (n_that, n_bu, tong))
        if thieu:
            truot.append("%d dòng thiếu created_at — không phân loại được, phải xử tay" % thieu)

        # không được có dòng nào nằm ở CẢ HAI view
        chung = cur.execute(
            "SELECT COUNT(*) FROM %s a JOIN %s b ON a.id=b.id" % (VIEW_THAT, VIEW_LAM_BU)
        ).fetchone()[0]
        if chung:
            truot.append("%d dòng nằm ở CẢ HAI view" % chung)

        # tính lại từ quy tắc gốc, phải khớp view
        lai_that = cur.execute(
            "SELECT COUNT(*) FROM final_bundles WHERE %s" % DIEU_KIEN_THAT).fetchone()[0]
        lai_bu = cur.execute(
            "SELECT COUNT(*) FROM final_bundles WHERE %s" % DIEU_KIEN_LAM_BU).fetchone()[0]
        if (lai_that, lai_bu) != (n_that, n_bu):
            truot.append("TÍNH LẠI KHÔNG KHỚP view: (%d,%d) vs (%d,%d)"
                         % (lai_that, lai_bu, n_that, n_bu))

        # cờ trong view phải đúng
        sai_co = cur.execute("SELECT COUNT(*) FROM %s WHERE is_lam_bu<>0" % VIEW_THAT).fetchone()[0]
        sai_co += cur.execute("SELECT COUNT(*) FROM %s WHERE is_lam_bu<>1" % VIEW_LAM_BU).fetchone()[0]
        if sai_co:
            truot.append("%d dòng có cờ is_lam_bu sai" % sai_co)

        print("  tính lại từ quy tắc gốc: thật %d · làm bù %d — %s"
              % (lai_that, lai_bu, "KHỚP" if not truot else "LỆCH"))
    finally:
        con.close()

    if truot:
        print("  ✗ TỰ KIỂM TRƯỢT:")
        for x in truot:
            print("     ·", x)
        print("[cong] LOC_LAM_BU=TRUOT")
        return 1
    print("  ✓ 6/6 phép đạt — không mất dòng, không đếm hai lần, tính lại vẫn khớp")
    print("[cong] LOC_LAM_BU=DAT")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=DEFAULT_DB)
    # Mặc định CHỈ KIỂM — lệnh chạy trong sổ quyết định gọi mỗi phiên, không nên ghi gì.
    ap.add_argument("--dung", action="store_true", help="dựng/dựng lại view rồi mới kiểm")
    ap.add_argument("--kiem", action="store_true", help="(giữ cho tương thích) chỉ tự kiểm")
    a = ap.parse_args(argv)
    print("── V10995 · tách bundle làm bù ──")
    if a.dung:
        dung_view(a.db)
    return tu_kiem(a.db)


if __name__ == "__main__":
    raise SystemExit(main())
