# -*- coding: utf-8 -*-
"""HE CO HON NGAU NHIEN KHONG — nen tinh RIENG cho TUNG MIEN-NGAY (RM-18).

Nen cua mot mien-ngay = |tap duoi that quay ra ngay do| / 100. Nen nay KHAC nhau tung ngay
(so dai, so giai khac nhau), nen dung Poisson-binomial thay vi mot nen co dinh.
Ky vong so lan trung neu doan NGAU NHIEN = tong cac nen. Phuong sai = tong p(1-p).
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

tap = collections.defaultdict(set)
for r in c.execute("SELECT date, region, prizes_json FROM lottery_results"):
    try: tap[(r["date"], r["region"])] |= duoi_cua(json.loads(r["prizes_json"] or "{}"))
    except Exception: pass

G = collections.defaultdict(lambda: {"n": 0, "trung": 0, "ky_vong": 0.0, "pvar": 0.0})
LECH_NHAN = 0
for r in c.execute("SELECT date,region,bach_thu,bach_thu_status,notes FROM final_bundles ORDER BY date"):
    if (r["notes"] or "").find("Phase 1.5 backfill") >= 0: continue
    bt = (r["bach_thu"] or "").strip()
    d = tap.get((r["date"], r["region"]))
    if not bt or not d: continue
    p = len(d) / 100.0
    trung = 1 if bt in d else 0
    # doi chieu nhan da luu voi phep cham lai
    if r["bach_thu_status"] in ("WIN", "LOSE"):
        if (r["bach_thu_status"] == "WIN") != bool(trung):
            LECH_NHAN += 1
    for k in (r["region"], "TAT CA"):
        G[k]["n"] += 1; G[k]["trung"] += trung
        G[k]["ky_vong"] += p; G[k]["pvar"] += p * (1 - p)

print("=== BACH THU vs NEN POISSON-BINOMIAL TINH RIENG TUNG MIEN-NGAY ===")
print("  (nen moi ngay khac nhau vi so dai/so giai khac nhau — khong dung mot nen co dinh)\n")
print("  %-8s %5s %6s %9s %9s %9s %8s   %s"
      % ("mien", "n", "trung", "ti le", "nen TB", "chenh", "z", "ket luan"))
for k in ("MN", "MT", "MB", "TAT CA"):
    g = G.get(k)
    if not g or not g["n"]: continue
    n, w, e, v = g["n"], g["trung"], g["ky_vong"], g["pvar"]
    sd = math.sqrt(v) if v > 0 else 0
    z = (w - e) / sd if sd else 0
    kl = "HON nen" if z > 1.96 else ("KEM nen" if z < -1.96 else "KHONG tach duoc khoi nen")
    print("  %-8s %5d %6d %8.1f%% %8.1f%% %+8.1f %+8.2f   %s"
          % (k, n, w, 100*w/n, 100*e/n, 100*(w-e)/n, z, kl))

print("\n  So lan nhan bach_thu_status luu KHAC voi cham lai: %d" % LECH_NHAN)

g = G["TAT CA"]
n, w, e, v = g["n"], g["trung"], g["ky_vong"], g["pvar"]
sd = math.sqrt(v)
print("\n=== CAN BAO NHIEU NGAY DE CHUNG MINH MOT LOI THE THAT ===")
print("  Do lech chuan cua mot mien-ngay: %.4f" % math.sqrt(v/n))
for lift in (0.02, 0.03, 0.05, 0.08):
    pbar = e/n
    need = ((1.96 + 0.84) ** 2) * pbar * (1 - pbar) / (lift ** 2)
    print("  De phat hien loi the +%.0f diem (alpha 5%%, suc manh 80%%): can %.0f mien-ngay = %.1f thang (3 mien/ngay)"
          % (100*lift, need, need/3/30))
print("\n  Hien co %d mien-ngay = %.1f thang du lieu sach." % (n, n/3/30))
print("  Chenh thuc te hien tai: %+.2f diem (z=%+.2f)." % (100*(w-e)/n, (w-e)/sd))
