# -*- coding: utf-8 -*-
"""MB — mien kem nhat. Chenh lech nam o dau? Dung nen RIENG TUNG NGAY (RM-18).
Canh bao tu dat ra: day la phep tach HAU NGHIEM 3 nhom => bay so sanh boi.
Phai bao ca so lan so sanh va nguong Holm, va noi ro day la UNG VIEN DANG KY TRUOC (RM-03),
KHONG phai ket luan. CHI DOC.
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

G = collections.defaultdict(lambda: {"n": 0, "w": 0, "e": 0.0, "v": 0.0})
for r in c.execute("SELECT date,region,bach_thu,notes,source_predictions_json "
                   "FROM final_bundles ORDER BY date"):
    if (r["notes"] or "").find("Phase 1.5 backfill") >= 0: continue
    d = tap.get((r["date"], r["region"]))
    bt = (r["bach_thu"] or "").strip()
    if not d or not bt: continue
    try: j = json.loads(r["source_predictions_json"] or "{}")
    except Exception: continue
    at = j.get("main_number_anti_trap") or {}
    lv = at.get("level") or "?"
    p = len(d)/100.0
    hit = 1 if bt in d else 0
    k = (r["region"], lv)
    G[k]["n"] += 1; G[k]["w"] += hit; G[k]["e"] += p; G[k]["v"] += p*(1-p)

print("=== TUNG (MIEN x MUC CHONG BAY) vs NEN RIENG TUNG NGAY ===")
print("  %-4s %-16s %5s %5s %8s %8s %8s %8s   %s"
      % ("mien","muc","n","trung","ti le","nen","chenh","z","p 2 phia"))
ds = []
for (reg, lv), g in sorted(G.items()):
    n, w, e, v = g["n"], g["w"], g["e"], g["v"]
    if n < 8: continue
    sd = math.sqrt(v) if v > 0 else 0
    z = (w-e)/sd if sd else 0
    p2 = math.erfc(abs(z)/math.sqrt(2))
    ds.append((p2, reg, lv, n, w, e, z))
    print("  %-4s %-16s %5d %5d %7.1f%% %7.1f%% %+7.1f %+7.2f   %.4f"
          % (reg, lv, n, w, 100*w/n, 100*e/n, 100*(w-e)/n, z, p2))

print("\n=== HIEU CHINH HOLM cho %d phep so sanh ===" % len(ds))
ds.sort()
m = len(ds)
qua = []
for i, (p2, reg, lv, n, w, e, z) in enumerate(ds):
    nguong = 0.05/(m-i)
    ok = p2 < nguong
    if ok: qua.append((reg, lv))
    print("  %-4s %-16s p=%.4f  nguong Holm=%.4f  %s"
          % (reg, lv, p2, nguong, "QUA" if ok else "khong qua"))
print("\n  So o QUA duoc Holm: %d" % len(qua))
if not qua:
    print("  => KHONG o nao song sot sau hieu chinh boi. Moi chenh lech thay o tren")
    print("     deu CHUA DUOC PHEP KET LUAN (RM-04). Chung la UNG VIEN de DANG KY TRUOC")
    print("     roi do tien cuu (RM-03), KHONG phai phat hien da chung minh.")

print("\n=== MB CAN BAO NHIEU NGAY DE PHAN BIET PARTIAL_SPENT voi FRESH ===")
a = G.get(("MB", "PARTIAL_SPENT")); b = G.get(("MB", "FRESH"))
if a and b and a["n"] and b["n"]:
    p1, p2_ = a["w"]/a["n"], b["w"]/b["n"]
    pp = (a["w"]+b["w"])/(a["n"]+b["n"])
    se = math.sqrt(pp*(1-pp)*(1/a["n"]+1/b["n"]))
    z = (p1-p2_)/se if se else 0
    print("  PARTIAL_SPENT %.1f%% (n=%d) vs FRESH %.1f%% (n=%d) · chenh %+.1f diem · z=%+.2f"
          % (100*p1, a["n"], 100*p2_, b["n"], 100*(p1-p2_), z))
    if abs(p1-p2_) > 1e-9:
        need = 2*((1.96+0.84)**2)*pp*(1-pp)/((p1-p2_)**2)
        print("  n-can MOI NHOM: %.0f mien-ngay MB = %.1f thang (MB 1 bundle/ngay)" % (need, need/30))
        print("  Hien co: PARTIAL_SPENT %d · FRESH %d" % (a["n"], b["n"]))
