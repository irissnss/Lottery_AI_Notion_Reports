# -*- coding: utf-8 -*-
"""V11018 (M-A / FU-317) — ĐỐI CHỨNG BA NGUỒN: ML × luật soi cầu × bộ lọc.

Owner nguyên văn (07/08): *"Với ML ngoài xác xuất thống kê thuần, anh quan tâm đến **đối chứng
với rules, bộ lọc** để so sánh đối chiếu để output **số chính và nhẹ hơn là số phụ**."*

Đo 07/08 (V11015): **7/7 tệp ML tham chiếu `mined_rule` = 0** — hiện KHÔNG có đối chứng nào.
Bảng này dựng tầng đối chứng đó ở dạng **shadow**, không đụng số official.

**Câu hỏi bảng này trả lời:** đuôi được **cả ba nguồn** cùng chỉ có trúng cao hơn đuôi chỉ
**một nguồn** chỉ không? Nếu có ⇒ có căn cứ để tách «số chính» / «số phụ» theo số nguồn.
Nếu không ⇒ đừng tách, và nói thẳng là không.

**Ba nguồn:**

| nguồn | lấy từ đâu |
|---|---|
| `ML` | đuôi các model ML chốt hôm đó — `phase_type` ∈ XGBOOST · LSTM · META · RF · SMART_ML · SMART_ENSEMBLE |
| `LUAT` | đuôi các luật `mined_rules` active của bucket (miền, thứ) trỏ tới, tính as-of |
| `LOC` | đuôi qua `filter_2_so_cuoi` — bộ lọc hai số cuối |

**CẢNH BÁO ĐỌC SỐ — đừng lặp lại lỗi §5g.** V11012 đo ra ô «3 nguồn» của §5g có
`z = −2,54`, tức ô **TỆ NHẤT** chứ không phải tốt nhất. Bảng này đo lại đúng câu hỏi đó trên
ba nguồn khác, và **mặc định là KHÔNG có lợi thế** cho tới khi số nói ngược lại.

An toàn §52: `output_eligible=0 · diagnostic_only=1 · owner_approved=0 · shadow_only=1`.
KHÔNG đụng `/du-doan`, writer `final_bundles`, hay bộ chọn model production.
"""
from __future__ import annotations

import json
import os
import sqlite3
import sys
from datetime import datetime, timedelta

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

H = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(H, "..", "..", "data", "lottery_ai.db")

BANG = "ma_doi_chung_shadow"
MIEN = ("MN", "MT", "MB")
PHASE_ML = ("XGBOOST", "LSTM", "META", "RF", "SMART_ML", "SMART_ENSEMBLE")
THU_PY = ("Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật")

DDL = f"""
CREATE TABLE IF NOT EXISTS {BANG} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    region TEXT NOT NULL,
    tail TEXT NOT NULL,
    tu_ml INTEGER NOT NULL DEFAULT 0,
    tu_luat INTEGER NOT NULL DEFAULT 0,
    tu_loc INTEGER NOT NULL DEFAULT 0,
    so_nguon INTEGER NOT NULL,          -- 1 | 2 | 3
    trung INTEGER,                      -- NULL = chưa có kết quả; 1/0 = trúng/trượt
    output_eligible INTEGER NOT NULL DEFAULT 0,
    diagnostic_only INTEGER NOT NULL DEFAULT 1,
    owner_approved INTEGER NOT NULL DEFAULT 0,
    shadow_only INTEGER NOT NULL DEFAULT 1,
    computed_at TEXT NOT NULL,
    UNIQUE(date, region, tail)
);
"""


def _con(ro: bool = False):
    if ro:
        return sqlite3.connect(f"file:{os.path.abspath(DB)}?mode=ro", uri=True)
    return sqlite3.connect(os.path.abspath(DB), timeout=30)


def _duoi(v) -> list[str]:
    """Lấy các đuôi hai chữ số từ một giá trị JSON/chuỗi bất kỳ."""
    ra = []
    try:
        x = json.loads(v) if isinstance(v, str) else v
    except Exception:
        x = v
    if isinstance(x, dict):
        x = list(x.values())
    if isinstance(x, list):
        for i in x:
            ra.extend(_duoi(i))
        return ra
    s = str(x or "").strip()
    if len(s) >= 2 and s[-2:].isdigit():
        ra.append(s[-2:])
    return ra


def _tu_ml(cur, ngay: str, mien: str) -> set[str]:
    q = ",".join("?" * len(PHASE_ML))
    cur.execute(
        f"SELECT main_numbers FROM predictions WHERE date=? AND target_region=? "
        f"AND phase_type IN ({q}) AND COALESCE(run_source,'')<>'shadow_auto_eval'",
        (ngay, mien, *PHASE_ML))
    ra = set()
    for (mn,) in cur.fetchall():
        ra.update(_duoi(mn))
    return ra


def _tu_luat(cur, ngay: str, mien: str) -> set[str]:
    """Đuôi các luật active của bucket trỏ tới — tính as-of, KHÔNG nhìn tương lai."""
    try:
        from mined_rule_eval import _extract_tails_from_prizes, _get_source_date
    except Exception:
        return set()
    dow = datetime.strptime(ngay, "%Y-%m-%d").weekday()
    cur.execute(
        "SELECT source_station, source_region, source_offset, prize_keys FROM mined_rules "
        "WHERE target_region=? AND target_weekday=? AND is_active=1", (mien, dow))
    ra = set()
    for st, rg, off, pk in cur.fetchall():
        try:
            sd = _get_source_date(ngay, off or "D-1")
            cur.execute("SELECT prizes_json FROM lottery_results "
                        "WHERE date=? AND region=? AND station=?", (sd, rg, st))
            row = cur.fetchone()
            if row and row[0]:
                ra.update(_extract_tails_from_prizes(json.loads(row[0]), pk or ""))
        except Exception:
            continue
    return ra


def _tu_loc(cur, ngay: str, mien: str) -> tuple[set[str], str]:
    """Đuôi qua bộ lọc hai số cuối. Trả (tập đuôi, ghi chú) — hỏng thì tập rỗng + lý do."""
    try:
        import filter_2_so_cuoi as F
    except Exception as e:
        return set(), f"không nạp được filter_2_so_cuoi: {str(e)[:60]}"
    # Tên hàm THẬT của bộ lọc — đọc từ mã nguồn, không đoán. V11015 đã vấp đúng lỗi
    # đoán tên tệp (`ml_train.py` không tồn tại); đây đoán tên HÀM thì cũng vậy.
    for ten in ("get_filter_data_with_cascade", "get_filter_data",
                "get_mined_review_filter_data_with_cascade"):
        fn = getattr(F, ten, None)
        if callable(fn):
            try:
                r = fn(mien, ngay)
                d = set(_duoi(r))
                return d, ("" if d else f"{ten}() chạy được nhưng không ra đuôi nào")
            except Exception as e:
                return set(), f"{ten}() lỗi: {str(e)[:60]}"
    return set(), "không tìm thấy hàm chạy được trong filter_2_so_cuoi"


def _duoi_ket_qua(cur, ngay: str, mien: str) -> set[str]:
    cur.execute("SELECT prizes_json FROM lottery_results WHERE date=? AND region=?",
                (ngay, mien))
    ra = set()
    for (pj,) in cur.fetchall():
        if pj:
            ra.update(_duoi(pj))
    return ra


def compute(so_ngay: int = 14, hom_nay: str | None = None) -> dict:
    ht = hom_nay or datetime.now().strftime("%Y-%m-%d")
    con = _con()
    con.execute(DDL)
    cur = con.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    n, ghi_chu_loc = 0, set()

    for i in range(so_ngay + 1):
        ngay = (datetime.strptime(ht, "%Y-%m-%d") - timedelta(days=i)).strftime("%Y-%m-%d")
        for mien in MIEN:
            ml = _tu_ml(cur, ngay, mien)
            luat = _tu_luat(cur, ngay, mien)
            loc, gc = _tu_loc(cur, ngay, mien)
            if gc:
                ghi_chu_loc.add(gc)
            if not (ml or luat or loc):
                continue
            kq = _duoi_ket_qua(cur, ngay, mien)
            for t in sorted(ml | luat | loc):
                a, b, c = int(t in ml), int(t in luat), int(t in loc)
                con.execute(
                    f"INSERT INTO {BANG} (date, region, tail, tu_ml, tu_luat, tu_loc, "
                    f"so_nguon, trung, computed_at) VALUES (?,?,?,?,?,?,?,?,?) "
                    f"ON CONFLICT(date, region, tail) DO UPDATE SET "
                    f"tu_ml=excluded.tu_ml, tu_luat=excluded.tu_luat, tu_loc=excluded.tu_loc, "
                    f"so_nguon=excluded.so_nguon, trung=excluded.trung, "
                    f"computed_at=excluded.computed_at",
                    (ngay, mien, t, a, b, c, a + b + c,
                     (1 if t in kq else 0) if kq else None, now))
                n += 1
    con.commit()
    con.close()
    return {"so_dong": n, "den_ngay": ht, "ghi_chu_bo_loc": sorted(ghi_chu_loc)}


def view() -> dict:
    """CHỈ ĐỌC — không tính lại."""
    con = _con(ro=True)
    con.row_factory = sqlite3.Row
    try:
        rows = [dict(r) for r in con.execute(
            f"SELECT so_nguon, COUNT(*) n, SUM(trung) trung FROM {BANG} "
            f"WHERE trung IS NOT NULL GROUP BY so_nguon ORDER BY so_nguon")]
        nguon = [dict(r) for r in con.execute(
            f"SELECT SUM(tu_ml) ml, SUM(tu_luat) luat, SUM(tu_loc) loc, COUNT(*) tong "
            f"FROM {BANG}")][0]
        gan = [dict(r) for r in con.execute(
            f"SELECT date, region, tail, tu_ml, tu_luat, tu_loc, so_nguon, trung FROM {BANG} "
            f"ORDER BY date DESC, region, so_nguon DESC, tail LIMIT 60")]
    except sqlite3.OperationalError as e:
        con.close()
        return {"success": False, "error": f"{e} — chạy compute() trước"}
    con.close()

    nhom = {}
    for r in rows:
        n, h = r["n"] or 0, r["trung"] or 0
        nhom[r["so_nguon"]] = {"n": n, "trung": h, "ty_le": round(100.0 * h / n, 2) if n else 0.0}

    m1, m3 = nhom.get(1, {}), nhom.get(3, {})
    if not m1.get("n") or not m3.get("n"):
        ket, gt = "CHUA_DU_DU_LIEU", "Chưa đủ mẫu ở nhóm 1 nguồn hoặc 3 nguồn."
    else:
        # z hai tỉ lệ độc lập
        p1, p3 = m1["trung"] / m1["n"], m3["trung"] / m3["n"]
        p = (m1["trung"] + m3["trung"]) / (m1["n"] + m3["n"])
        se = (p * (1 - p) * (1 / m1["n"] + 1 / m3["n"])) ** 0.5
        z = (p3 - p1) / se if se else 0.0
        nhom["z_3_vs_1"] = round(z, 2)
        if abs(z) < 1.96:
            ket = "KHONG_CO_LOI_THE"
            gt = (f"3 nguồn {p3 * 100:.1f}% vs 1 nguồn {p1 * 100:.1f}% · z={z:+.2f} — "
                  f"CHƯA vượt 1,96. Không có căn cứ tách số chính/phụ theo số nguồn.")
        elif z > 0:
            ket = "CO_LOI_THE"
            gt = (f"3 nguồn {p3 * 100:.1f}% vs 1 nguồn {p1 * 100:.1f}% · z={z:+.2f} — "
                  f"3 nguồn HƠN thật. Có căn cứ để bàn tách số chính/phụ.")
        else:
            ket = "NGUOC_DAU"
            gt = (f"3 nguồn {p3 * 100:.1f}% vs 1 nguồn {p1 * 100:.1f}% · z={z:+.2f} — "
                  f"3 nguồn TỆ HƠN, giống hệt ca §5g (z=−2,54). Càng nhiều nguồn càng dở.")

    return {
        "success": True, "bang": BANG,
        "an_toan": {"output_eligible": 0, "diagnostic_only": 1,
                    "owner_approved": 0, "shadow_only": 1},
        "cau_hoi": "Đuôi được CẢ BA nguồn cùng chỉ có trúng cao hơn đuôi chỉ MỘT nguồn không?",
        "canh_bao": "§5g đã đo ra ô «3 nguồn» có z=−2,54 — ô TỆ NHẤT. Mặc định là KHÔNG có "
                    "lợi thế cho tới khi số nói ngược lại.",
        "nguong": "cần |z| >= 1,96 mới kết luận",
        "theo_so_nguon": nhom, "phu_song_nguon": nguon,
        "ket_luan": ket, "giai_thich": gt, "dong": gan,
    }


if __name__ == "__main__":
    r = compute()
    print(f"  đã ghi {r['so_dong']} dòng · đến {r['den_ngay']}")
    for g in r["ghi_chu_bo_loc"]:
        print(f"  ⚠ bộ lọc: {g}")
    v = view()
    print(f"\n  {'số nguồn':>9} {'n':>6} {'trúng':>7} {'tỉ lệ':>8}")
    for k in (1, 2, 3):
        x = v["theo_so_nguon"].get(k)
        if x:
            print(f"  {k:>9} {x['n']:>6} {x['trung']:>7} {x['ty_le']:>7.2f}%")
    print(f"\n  phủ sóng: ML={v['phu_song_nguon']['ml']} · LUẬT={v['phu_song_nguon']['luat']} "
          f"· LỌC={v['phu_song_nguon']['loc']} / tổng {v['phu_song_nguon']['tong']} dòng")
    print(f"\n  ⇒ {v['ket_luan']}: {v['giai_thich']}")
