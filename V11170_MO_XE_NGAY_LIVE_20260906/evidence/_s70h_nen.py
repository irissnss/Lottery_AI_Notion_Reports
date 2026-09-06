# -*- coding: utf-8 -*-
"""NEN DUNG CHO TUNG MIEN (RM-18) roi moi so muc chong bay.

Bay can loai: NOT_APPLICABLE = mien RA DAU TIEN trong ngay. Neu mien do von co NHIEU
duoi hon (nhieu dai hon) thi ti le trung cao hon la do LUAT CHOI, khong phai do mo hinh.
Nen dung = xac suat mot duoi bat ky co mat trong tap duoi da quay cua chinh mien-ngay do.
CHI DOC.
"""
import sqlite3, json, collections, math
c = sqlite3.connect("file:/root/Lottery_AI_Test/data/lottery_ai.db?mode=ro", uri=True)
c.row_factory = sqlite3.Row

def duoi_cua(pz):
    d = set()
    def w(v):
        if isinstance(v, str) and v.isdigit(): d.add(v[-2:])
        elif isinstance(v, list):
            for x in v: w(x)
        elif isinstance(v, dict):
            for x in v.values(): w(x)
    w(pz); return d

# tap duoi that cua tung (ngay, mien)
tap = collections.defaultdict(set)
for r in c.execute("SELECT date, region, prizes_json FROM lottery_results"):
    try: tap[(r["date"], r["region"])] |= duoi_cua(json.loads(r["prizes_json"] or "{}"))
    except Exception: pass

rows = c.execute("SELECT id,date,region,bach_thu,bach_thu_status,notes,source_predictions_json "
                 "FROM final_bundles WHERE bach_thu_status IS NOT NULL AND bach_thu_status<>'' "
                 "ORDER BY date").fetchall()

# nen theo mien = trung binh |tap duoi| / 100
nen = collections.defaultdict(list)
for (d, reg), s in tap.items():
    nen[reg].append(len(s))
print("=== NEN DUNG CHO TUNG MIEN (RM-18) ===")
print("  %-4s %6s %10s %10s   %s" % ("mien", "ngay", "duoi TB", "nen", "y nghia"))
NEN = {}
for reg in sorted(nen):
    k = sum(nen[reg]) / len(nen[reg])
    NEN[reg] = k / 100.0
    print("  %-4s %6d %10.1f %9.1f%%   xac suat MOT duoi bat ky co mat" % (reg, len(nen[reg]), k, 100*k/100))

def wilson(w, n):
    if not n: return (0, 0)
    p = w/n; z = 1.96; d = 1 + z*z/n
    ctr = (p + z*z/(2*n))/d
    hw = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return (100*(ctr-hw), 100*(ctr+hw))

per = collections.defaultdict(lambda: {"n": 0, "win": 0})
lvl_reg = collections.defaultdict(lambda: {"n": 0, "win": 0})
bo = 0
for r in rows:
    if (r["notes"] or "").find("Phase 1.5 backfill") >= 0:
        bo += 1; continue
    try: j = json.loads(r["source_predictions_json"] or "{}")
    except Exception: continue
    at = j.get("main_number_anti_trap")
    if not isinstance(at, dict) or not at.get("level"): continue
    win = 1 if r["bach_thu_status"] == "WIN" else 0
    per[r["region"]]["n"] += 1; per[r["region"]]["win"] += win
    lvl_reg[(r["region"], at["level"])]["n"] += 1
    lvl_reg[(r["region"], at["level"])]["win"] += win

print("\n=== MUC CHONG BAY XUAT HIEN O MIEN NAO — kiem bay ===")
mm = collections.defaultdict(lambda: collections.Counter())
for (reg, lv), v in lvl_reg.items():
    mm[lv][reg] = v["n"]
for lv in sorted(mm):
    print("  %-16s %s" % (lv, dict(mm[lv])))

print("\n=== TI LE TRUNG BACH THU vs NEN CUA CHINH MIEN DO (da bo %d dong backfill) ===" % bo)
print("  %-4s %-16s %5s %5s %8s %8s %9s  %s" % ("mien","muc","n","win","ti le","nen","chenh","KTC95"))
for reg in ("MN", "MT", "MB"):
    b = NEN.get(reg, 0)
    for lv in ("NOT_APPLICABLE", "FRESH", "PARTIAL_SPENT", "FULL_SPENT"):
        v = lvl_reg.get((reg, lv))
        if not v or not v["n"]: continue
        p = v["win"]/v["n"]; lo, hi = wilson(v["win"], v["n"])
        print("  %-4s %-16s %5d %5d %7.1f%% %7.1f%% %+8.1f  [%.1f%% , %.1f%%]"
              % (reg, lv, v["n"], v["win"], 100*p, 100*b, 100*(p-b), lo, hi))
    t = per[reg]
    if t["n"]:
        lo, hi = wilson(t["win"], t["n"])
        print("  %-4s %-16s %5d %5d %7.1f%% %7.1f%% %+8.1f  [%.1f%% , %.1f%%]  <== CA MIEN"
              % (reg, "TAT CA", t["n"], t["win"], 100*t["win"]/t["n"], 100*b,
                 100*(t["win"]/t["n"] - b), lo, hi))
    print()
