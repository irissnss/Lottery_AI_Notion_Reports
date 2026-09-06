# -*- coding: utf-8 -*-
"""HOC THUYET CHONG BAY: so da 'chay' o mien truoc trong ngay co thuc su xau hon khong?

Do tren chinh truong main_number_anti_trap.level da luu san trong bundle => khong phai
tu dinh nghia lai, khong bi bay chon-sau. CHI DOC.
"""
import sqlite3, json, collections, math
c = sqlite3.connect("file:/root/Lottery_AI_Test/data/lottery_ai.db?mode=ro", uri=True)
c.row_factory = sqlite3.Row

rows = c.execute(
    "SELECT id, date, region, bach_thu, bach_thu_status, notes, source_predictions_json "
    "FROM final_bundles WHERE bach_thu_status IS NOT NULL AND bach_thu_status<>'' "
    "ORDER BY date").fetchall()

BACKFILL = 0
by = collections.defaultdict(lambda: {"n": 0, "win": 0})
theo_thang = collections.defaultdict(lambda: collections.defaultdict(lambda: {"n": 0, "win": 0}))
canh_bao = []
for r in rows:
    if (r["notes"] or "").find("Phase 1.5 backfill") >= 0:
        BACKFILL += 1
        continue                      # RM: tru 91 dong backfill ra khoi moi phep do
    try:
        j = json.loads(r["source_predictions_json"] or "{}")
    except Exception:
        continue
    at = j.get("main_number_anti_trap")
    if not isinstance(at, dict):
        continue
    lv = at.get("level")
    if not lv:
        continue
    win = 1 if r["bach_thu_status"] == "WIN" else 0
    by[lv]["n"] += 1; by[lv]["win"] += win
    theo_thang[r["date"][:7]][lv]["n"] += 1
    theo_thang[r["date"][:7]][lv]["win"] += win
    if j.get("main_number_anti_trap_warning"):
        canh_bao.append((r["date"], r["region"], r["bach_thu"], lv, r["bach_thu_status"]))

print("=== BO 91 BUNDLE BACKFILL: %d dong ===" % BACKFILL)
print("\n=== TI LE TRUNG BACH THU THEO MUC CHONG BAY (toan bo lich su sach) ===")
print("  %-18s %6s %6s %8s   %s" % ("muc", "n", "win", "ti le", "KTC95 (Wilson)"))
for lv in sorted(by, key=lambda x: -by[x]["n"]):
    n, w = by[lv]["n"], by[lv]["win"]
    p = w / n if n else 0
    if n:
        z = 1.96
        d = 1 + z*z/n
        ctr = (p + z*z/(2*n)) / d
        hw = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / d
        ktc = "[%.1f%% , %.1f%%]" % (100*(ctr-hw), 100*(ctr+hw))
    else:
        ktc = "-"
    print("  %-18s %6d %6d %7.1f%%   %s" % (lv, n, w, 100*p, ktc))

print("\n=== SO SANH FULL_SPENT vs FRESH (phep kiem hai ti le) ===")
a, b = by.get("FULL_SPENT"), by.get("FRESH")
if a and b and a["n"] and b["n"]:
    p1, p2 = a["win"]/a["n"], b["win"]/b["n"]
    pp = (a["win"]+b["win"]) / (a["n"]+b["n"])
    se = math.sqrt(pp*(1-pp)*(1/a["n"] + 1/b["n"]))
    z = (p1-p2)/se if se else 0
    print("  FULL_SPENT %.1f%% (n=%d)  vs  FRESH %.1f%% (n=%d)" % (100*p1, a["n"], 100*p2, b["n"]))
    print("  chenh = %+.2f diem · z = %+.2f · %s" %
          (100*(p1-p2), z, "CO Y NGHIA (|z|>1,96)" if abs(z) > 1.96 else "KHONG co y nghia thong ke"))
    # n-can de phat hien chenh lech hien tai voi suc manh 80%
    if abs(p1-p2) > 1e-9:
        need = 2*((1.96+0.84)**2)*pp*(1-pp)/((p1-p2)**2)
        print("  n-can moi nhom de phat hien dung chenh nay (alpha 5%%, suc manh 80%%): %.0f" % need)
else:
    print("  khong du du lieu hai nhom")

print("\n=== CAC LAN HE DA CANH BAO (main_number_anti_trap_warning != null) ===")
print("  tong %d lan" % len(canh_bao))
w = sum(1 for x in canh_bao if x[4] == "WIN")
print("  trong do TRUNG: %d (%.1f%%)" % (w, 100*w/len(canh_bao) if canh_bao else 0))
for x in canh_bao[-25:]:
    print("    %s %-3s BT=%-4s %-14s %s" % x)

print("\n=== THEO THANG (chi thang co >= 10 dong) ===")
for th in sorted(theo_thang):
    d = theo_thang[th]
    tot = sum(v["n"] for v in d.values())
    if tot < 10:
        continue
    bit = " ".join("%s %d/%d" % (k, v["win"], v["n"]) for k, v in sorted(d.items()))
    print("  %s  %s" % (th, bit))
