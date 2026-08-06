# -*- coding: utf-8 -*-
"""PL19c B1·B2·B3 — ĐO LẠI ĐỘC LẬP. Truy vấn VIẾT MỚI, thuật toán khác PL19b.

B1: dùng SQL thuần gom theo số + đếm trong SQL (PL19b gom bằng Python dict).
B2: dùng strftime của SQLite trên chuỗi thô (PL19b parse bằng datetime Python).
B3: đếm bằng GROUP BY + COUNT(DISTINCT) trong một câu (PL19b duyệt nhiều câu).
"""
import math
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")
c = sqlite3.connect("file:data/lottery_ai.db?mode=ro", uri=True)
c.row_factory = sqlite3.Row
KQ = {}

# ── B1 ────────────────────────────────────────────────────────────────────────
# Cách khác PL19b: tách đuôi bằng SQL, đếm hội tụ bằng SQL, join thẳng kết quả xổ.
SQL_B1 = """
WITH p AS (
  SELECT date, target_region AS reg, ai_model,
         substr(replace(replace(replace(replace(TRIM(main_numbers),'[',''),']',''),'"',''),' ',''),
                1, instr(replace(replace(replace(replace(TRIM(main_numbers),'[',''),']',''),'"',''),' ','')||',', ',')-1) AS so
    FROM predictions
   WHERE main_numbers IS NOT NULL AND TRIM(main_numbers) <> ''
     AND target_region IN ('MN','MT','MB') AND date >= ?
),
q AS (SELECT date, reg, substr('0'||so, -2, 2) AS duoi FROM p WHERE length(so) >= 1),
hoi_tu AS (SELECT date, reg, duoi, COUNT(*) AS k FROM q GROUP BY 1,2,3),
kq AS (SELECT date, region AS reg, prizes_json FROM lottery_results WHERE prizes_json IS NOT NULL)
SELECT h.date, h.reg, h.duoi, h.k,
       (SELECT GROUP_CONCAT(prizes_json,'|') FROM kq WHERE kq.date=h.date AND kq.reg=h.reg) AS pj
  FROM hoi_tu h
"""


def duoi_tu_json(s):
    import json
    out = set()
    for phan in (s or "").split("|"):
        try:
            pr = json.loads(phan)
        except Exception:
            continue
        for v in (pr.values() if isinstance(pr, dict) else []):
            for x in (v if isinstance(v, list) else [v]):
                d = "".join(ch for ch in str(x) if ch.isdigit())
                if len(d) >= 2:
                    out.add(d[-2:])
    return out


def z_nhi_thuc(k, n, p0):
    v = n * p0 * (1 - p0)
    return (k - n * p0) / math.sqrt(v) if v > 0 else 0.0


def do_b1(tu_ngay, den_ngay=None, nhan=""):
    b = {"1-2": [0, 0, 0.0], "3": [0, 0, 0.0], ">=4": [0, 0, 0.0]}
    kho = {}
    for r in c.execute(SQL_B1, (tu_ngay,)):
        if den_ngay and r["date"] > den_ngay:
            continue
        if not r["duoi"] or len(r["duoi"]) != 2 or not r["duoi"].isdigit():
            continue
        k = (r["date"], r["reg"])
        if k not in kho:
            kho[k] = duoi_tu_json(r["pj"])
        thuc = kho[k]
        if not thuc:
            continue
        o = "1-2" if r["k"] <= 2 else ("3" if r["k"] == 3 else ">=4")
        b[o][0] += 1
        b[o][1] += 1 if r["duoi"] in thuc else 0
        b[o][2] += len(thuc) / 100.0
    print(f"\n  {nhan}")
    print(f"    {'mức':6} {'lượt':>6} {'trúng':>6} {'tỉ lệ':>8} {'nền':>7} {'z':>8}")
    ra = {}
    for o in ("1-2", "3", ">=4"):
        n, k, nn = b[o]
        if not n:
            continue
        p0 = nn / n
        z = z_nhi_thuc(k, n, p0)
        ra[o] = (n, k, z)
        print(f"    {o:6} {n:>6} {k:>6} {k/n*100:>7.1f}% {p0*100:>6.1f}% {z:>+8.2f}")
    return ra


print("=" * 90)
print("B1 — ĐO LẠI ô hội tụ (SQL thuần, thuật toán KHÁC PL19b)")
print("=" * 90)
r = do_b1("2026-05-08", None, "toàn cửa sổ 90 ngày (đối chiếu PL19b: 3 nguồn n=294, 26,5%, z=−2,51)")
KQ["B1"] = r
print("\n  ── độ bền: tách hai nửa ──")
n1 = do_b1("2026-05-08", "2026-06-21", "nửa ĐẦU (08/05 → 21/06)")
n2 = do_b1("2026-06-22", None, "nửa SAU (22/06 → nay)")

print()
print("=" * 90)
print("B2 — ĐẾM LẠI rerun_post_mt (strftime của SQLite, KHÁC PL19b dùng Python)")
print("=" * 90)
r = c.execute("""
  SELECT COUNT(*) tong,
         SUM(CASE WHEN CAST(substr(created_at,12,2) AS INT)*60
                     + CAST(substr(created_at,15,2) AS INT) >= 18*60+15
                  THEN 1 ELSE 0 END) sau_1815,
         MIN(substr(created_at,12,5)) som, MAX(substr(created_at,12,5)) muon
    FROM predictions
   WHERE run_source='rerun_post_mt' AND target_region='MB'
     AND date >= date('now','-60 day') AND created_at IS NOT NULL""").fetchone()
print(f"    tổng {r['tong']} dòng · ghi SAU 18:15: {r['sau_1815']} · "
      f"sớm nhất {r['som']} · muộn nhất {r['muon']}")
KQ["B2"] = (r["tong"], r["sau_1815"])

print()
print("=" * 90)
print("B3 — ĐẾM LẠI nhãn giai_doan (một câu GROUP BY, KHÁC PL19b duyệt nhiều câu)")
print("=" * 90)
print(f"    {'nhãn':12} {'dòng':>6} {'ngày':>6} {'luật':>6} {'từ':>12} {'đến':>12}")
KQ["B3"] = {}
for r in c.execute("""SELECT COALESCE(giai_doan,'(rỗng)') g, COUNT(*) n,
                             COUNT(DISTINCT date) nd, COUNT(DISTINCT rule_id) nr,
                             MIN(date) d0, MAX(date) d1
                        FROM mined_rule_effectiveness GROUP BY 1 ORDER BY 2 DESC"""):
    print(f"    {r['g']:12} {r['n']:>6} {r['nd']:>6} {r['nr']:>6} {r['d0']:>12} {r['d1']:>12}")
    KQ["B3"][r["g"]] = (r["n"], r["nd"], r["nr"])

print()
print("=" * 90)
print("PHÁN XỬ B1·B2·B3 — KHỚP hay LỆCH so với PL19b")
print("=" * 90)
CHUAN = {
    "B1 · 3 nguồn n": (294, KQ["B1"].get("3", (0,))[0]),
    "B1 · 3 nguồn z": (-2.51, round(KQ["B1"].get("3", (0, 0, 0))[2], 2)),
    "B1 · 1-2 nguồn n": (1925, KQ["B1"].get("1-2", (0,))[0]),
    "B1 · ≥4 nguồn n": (603, KQ["B1"].get(">=4", (0,))[0]),
    "B2 · tổng dòng": (413, KQ["B2"][0]),
    "B2 · sau 18:15": (0, KQ["B2"][1]),
    "B3 · DO_TIEN dòng": (15, KQ["B3"].get("DO_TIEN", (0, 0, 0))[0]),
    "B3 · DO_TIEN ngày": (1, KQ["B3"].get("DO_TIEN", (0, 0, 0))[1]),
    "B3 · CHAM_NGUOC dòng": (1695, KQ["B3"].get("CHAM_NGUOC", (0, 0, 0))[0]),
    "B3 · CHAM_NGUOC ngày": (113, KQ["B3"].get("CHAM_NGUOC", (0, 0, 0))[1]),
    "B3 · MO_COI dòng": (1493, KQ["B3"].get("MO_COI", (0, 0, 0))[0]),
}
lech = 0
for ten, (pl19b, moi) in CHUAN.items():
    ok = (abs(pl19b - moi) < 0.02) if isinstance(pl19b, float) else (pl19b == moi)
    if not ok:
        lech += 1
    print(f"    {'KHỚP' if ok else '✗ LỆCH':>7}  {ten:<24} PL19b={pl19b:<8} mới={moi}")
print("\n" + ("    ✓ TẤT CẢ KHỚP — không kích hoạt STOP" if not lech
               else f"    ✗ {lech} SỐ LỆCH — STOP TOÀN GÓI, báo owner ngay"))
c.close()
