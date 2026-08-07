# -*- coding: utf-8 -*-
"""V11024 — CỔNG BĂM 4 BẢNG KHOÁ (sinh hash_pre.json / hash_post.json).

Bộ phê bình độ đầy đủ bắt đúng: bản đầu phiên in băm ra màn hình rồi ghi hash_pre.json
nhưng KHÔNG lưu script sinh ra nó ⇒ con số băm **không tái lập được**, tức vi phạm chính
điều kiện E4 của đề bài. Tệp này vá chỗ đó.

Chạy:
    python artifacts/v11024_audit/scripts/cong_bam_4_bang_khoa.py pre
    python artifacts/v11024_audit/scripts/cong_bam_4_bang_khoa.py post   # so với pre, mã thoát 1 nếu lệch

Băm = sha256 của repr(mọi dòng) theo thứ tự rowid. Đây là băm NỘI DUNG, không phải chỉ đếm dòng —
đếm dòng không bắt được sửa tại chỗ.
"""
from __future__ import annotations

import hashlib
import io
import json
import os
import sqlite3
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

GOC = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DB = os.path.join(GOC, "data", "lottery_ai.db")
RA = os.path.join(GOC, "artifacts", "v11024_audit")
BANG = ("predictions", "final_bundles", "lottery_results", "model_daily_eval")


def _ghi(duong: str, doi_tuong) -> None:
    """Ghi an toàn: .tmp → flush → fsync → replace → đọc lại so."""
    noi_dung = json.dumps(doi_tuong, ensure_ascii=False, indent=2)
    tmp = duong + ".tmp"
    with io.open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(noi_dung)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, duong)
    if io.open(duong, encoding="utf-8", newline="").read() != noi_dung:
        raise IOError(f"{duong}: ghi xong đọc lại LỆCH")


def bam() -> dict:
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    ra = {}
    for b in BANG:
        h = hashlib.sha256()
        for r in con.execute(f"SELECT * FROM {b} ORDER BY rowid"):
            h.update(repr(r).encode("utf-8", "replace"))
        ra[b] = {"n": con.execute(f"SELECT COUNT(*) FROM {b}").fetchone()[0],
                 "sha256": h.hexdigest()[:16], "sha256_day_du": h.hexdigest()}
    con.close()
    ra["_do_luc"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ra["_db_mtime"] = datetime.fromtimestamp(os.stat(DB).st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    return ra


def main() -> int:
    che_do = (sys.argv[1] if len(sys.argv) > 1 else "pre").lower()
    os.makedirs(RA, exist_ok=True)
    kq = bam()
    print("=" * 92)
    print(f"  BĂM 4 BẢNG KHOÁ — {che_do.upper()}   (db mtime {kq['_db_mtime']})")
    print("=" * 92)
    for b in BANG:
        print(f"  {b:20} {kq[b]['n']:>7} dòng · {kq[b]['sha256']}")

    if che_do == "pre":
        _ghi(os.path.join(RA, "hash_pre.json"), kq)
        print("\n  đã ghi hash_pre.json")
        return 0

    _ghi(os.path.join(RA, "hash_post.json"), kq)
    pre_p = os.path.join(RA, "hash_pre.json")
    if not os.path.exists(pre_p):
        print("\n  ✗ KHÔNG CÓ hash_pre.json để so — cổng KHÔNG kết luận được")
        return 1
    pre = json.load(io.open(pre_p, encoding="utf-8"))
    lech = [b for b in BANG
            if pre.get(b, {}).get("sha256") != kq[b]["sha256"] or pre[b]["n"] != kq[b]["n"]]
    print()
    for b in BANG:
        k = b not in lech
        print(f"  {b:20} {'✓ Y HỆT' if k else '✗ ĐỔI — pre ' + pre[b]['sha256']}")
    print()
    if lech:
        print(f"  ✗ [cong] HASH_4_BANG_KHOA=LECH ({', '.join(lech)})")
        return 1
    print("  ✓ [cong] HASH_4_BANG_KHOA=PRE=POST")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
