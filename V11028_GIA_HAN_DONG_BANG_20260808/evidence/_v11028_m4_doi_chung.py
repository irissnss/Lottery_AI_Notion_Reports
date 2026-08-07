# -*- coding: utf-8 -*-
"""V11028 (A6) — DỰNG LẠI M4 ĐỐI CHỨNG LUẬT GIẢ, lần này TÁI LẬP ĐƯỢC.

═══ VÌ SAO PHẢI DỰNG LẠI ═══

Hai con số `z = −0,33σ / +0,26σ` **đang được bơm vào prompt** cho model đọc (từ V11014, còn
nguyên ở PB-20.1). Tra soát V11024 (R6) phát hiện:

- bảng gốc `mined_rule_doi_chung` **đã bị lần đồng bộ 18:51 ngày 07/08 xoá sạch** —
  chạy `SELECT` bây giờ ra `no such table`
- hai con số đó tính từ **9 và 15 cặp lệch** — đổi một cặp là z nhảy ~0,3 đơn vị
- **không ai tái lập được** ⇒ vi phạm chuẩn E4 *"mọi con số công bố phải tái lập được"*

Model đang đọc một con số **không ai dựng lại được**. Đó là chỗ tệ nhất trong cả bộ.

═══ CÁCH ĐO ═══

Với mỗi luật thật, dựng **luật giả** cùng hình dạng (cùng miền đích, cùng thứ, cùng số đuôi
sinh ra) nhưng **chọn đuôi bằng băm tất định** — không nhìn dữ liệu. Rồi so **từng cặp** trên
CÙNG một ngày bằng **McNemar**:

    b = ngày luật THẬT trúng mà luật GIẢ trượt
    c = ngày luật THẬT trượt mà luật GIẢ trúng
    z = (b − c) / sqrt(b + c)

So từng cặp trên cùng ngày nên **triệt tiêu độ khó của ngày** — thứ mà so tỉ lệ thô không làm được.

**Tất định:** luật giả sinh từ `sha256(rule_key + date)` nên chạy bao nhiêu lần cũng ra y hệt.
Đó là điều bản M4 cũ không có, và là lý do nó không tái lập được.

═══ AN TOÀN ═══

`output_eligible=0 · diagnostic_only=1 · owner_approved=0 · shadow_only=1`.
KHÔNG đụng prompt (đang bị QD-041 đóng băng tới 21/08) · KHÔNG đụng 4 bảng khoá ·
KHÔNG đụng `mined_rules` hay `mined_rule_effectiveness`.

    python web/backend/_v11028_m4_doi_chung.py
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import sqlite3
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
GOC = os.path.abspath(os.path.join(H, "..", ".."))
DB = os.path.join(GOC, "data", "lottery_ai.db")
BANG = "m4_doi_chung_v11028"

DDL = f"""
CREATE TABLE IF NOT EXISTS {BANG} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    rule_key TEXT NOT NULL,
    region TEXT NOT NULL,
    giai_doan TEXT NOT NULL,          -- lấy từ mined_rule_effectiveness (V11025)
    so_duoi INTEGER NOT NULL,
    that_trung INTEGER NOT NULL,
    gia_trung INTEGER NOT NULL,
    duoi_gia TEXT NOT NULL,
    output_eligible INTEGER NOT NULL DEFAULT 0,
    diagnostic_only INTEGER NOT NULL DEFAULT 1,
    owner_approved INTEGER NOT NULL DEFAULT 0,
    shadow_only INTEGER NOT NULL DEFAULT 1,
    computed_at TEXT NOT NULL,
    UNIQUE(date, rule_key)
);
"""


def duoi_gia(rule_key: str, ngay: str, so_duoi: int) -> list[str]:
    """Luật giả TẤT ĐỊNH — chọn `so_duoi` đuôi từ băm, không nhìn dữ liệu."""
    ra, i = [], 0
    while len(ra) < so_duoi and i < 400:
        h = hashlib.sha256(f"{rule_key}|{ngay}|{i}".encode()).hexdigest()
        d = f"{int(h[:8], 16) % 100:02d}"
        if d not in ra:
            ra.append(d)
        i += 1
    return ra


def _duoi_kq(con, ngay: str, mien: str) -> set[str]:
    ra = set()
    for (pj,) in con.execute("SELECT prizes_json FROM lottery_results "
                             "WHERE date=? AND region=?", (ngay, mien)):
        if not pj:
            continue
        try:
            v = json.loads(pj)
        except Exception:
            continue

        def w(x):
            if isinstance(x, dict):
                [w(i) for i in x.values()]
            elif isinstance(x, list):
                [w(i) for i in x]
            else:
                s = str(x or "").strip()
                if len(s) >= 2 and s[-2:].isdigit():
                    ra.add(s[-2:])
        w(v)
    return ra


def compute() -> dict:
    con = sqlite3.connect(DB, timeout=30)
    con.row_factory = sqlite3.Row
    con.execute(DDL)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    hang = list(con.execute(
        "SELECT date, rule_key, target_region, giai_doan, tails_produced, hit_any "
        "FROM mined_rule_effectiveness "
        "WHERE rule_key IS NOT NULL AND tails_produced IS NOT NULL"))
    kq_cache, n = {}, 0
    for r in hang:
        try:
            duoi_that = json.loads(r["tails_produced"]) or []
        except Exception:
            continue
        if not duoi_that:
            continue
        k = (r["date"], r["target_region"])
        if k not in kq_cache:
            kq_cache[k] = _duoi_kq(con, r["date"], r["target_region"])
        kq = kq_cache[k]
        if not kq:
            continue
        gia = duoi_gia(r["rule_key"], r["date"], len(duoi_that))
        con.execute(
            f"INSERT INTO {BANG} (date, rule_key, region, giai_doan, so_duoi, that_trung, "
            f"gia_trung, duoi_gia, computed_at) VALUES (?,?,?,?,?,?,?,?,?) "
            f"ON CONFLICT(date, rule_key) DO UPDATE SET "
            f"giai_doan=excluded.giai_doan, so_duoi=excluded.so_duoi, "
            f"that_trung=excluded.that_trung, gia_trung=excluded.gia_trung, "
            f"duoi_gia=excluded.duoi_gia, computed_at=excluded.computed_at",
            (r["date"], r["rule_key"], r["target_region"], r["giai_doan"] or "KHONG_RO",
             len(duoi_that),
             1 if any(d in kq for d in duoi_that) else 0,
             1 if any(d in kq for d in gia) else 0,
             json.dumps(gia), now))
        n += 1
    con.commit()
    con.close()
    return {"so_dong": n}


def view() -> dict:
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        hang = list(con.execute(f"SELECT giai_doan, that_trung, gia_trung FROM {BANG}"))
    except sqlite3.OperationalError as e:
        con.close()
        return {"success": False, "error": f"{e} — chạy compute() trước"}
    con.close()

    ra = {"success": True, "bang": BANG,
          "an_toan": {"output_eligible": 0, "diagnostic_only": 1,
                      "owner_approved": 0, "shadow_only": 1},
          "phep": "McNemar theo cặp cùng ngày · luật giả tất định từ sha256(rule_key|date|i)",
          "nhom": {}}
    for g in sorted({r["giai_doan"] for r in hang}):
        b = sum(1 for r in hang if r["giai_doan"] == g and r["that_trung"] and not r["gia_trung"])
        c = sum(1 for r in hang if r["giai_doan"] == g and not r["that_trung"] and r["gia_trung"])
        n = sum(1 for r in hang if r["giai_doan"] == g)
        z = (b - c) / math.sqrt(b + c) if (b + c) else 0.0
        ra["nhom"][g] = {"n": n, "b_that_hon": b, "c_gia_hon": c, "cap_lech": b + c,
                         "z": round(z, 3),
                         "ket": ("CHUA_DU_MAU" if (b + c) < 25 else
                                 "THAT_HON" if z >= 1.96 else
                                 "GIA_HON" if z <= -1.96 else "NGANG_NHAU")}
    return ra


def main() -> int:
    print("=" * 96)
    print("  V11028 (A6) — M4 ĐỐI CHỨNG LUẬT GIẢ, dựng lại cho TÁI LẬP ĐƯỢC")
    print("=" * 96)
    r = compute()
    print(f"  đã ghi {r['so_dong']:,} dòng vào `{BANG}`")
    v = view()
    print(f"\n  {'giai đoạn':<22} {'n':>6} {'b(thật hơn)':>12} {'c(giả hơn)':>11} "
          f"{'cặp lệch':>9} {'z':>7}  kết luận")
    for g, x in v["nhom"].items():
        print(f"  {g:<22} {x['n']:>6} {x['b_that_hon']:>12} {x['c_gia_hon']:>11} "
              f"{x['cap_lech']:>9} {x['z']:>7.2f}  {x['ket']}")
    print()
    print("  Ngưỡng chốt trước: cần ≥25 cặp lệch mới kết luận · |z|≥1,96 mới nói hơn/kém.")
    print("  Luật giả TẤT ĐỊNH ⇒ chạy lại bao nhiêu lần cũng ra y hệt. Đây là thứ bản M4 cũ")
    print("  KHÔNG có, và là lý do hai con số −0,33/+0,26 không tái lập được.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
