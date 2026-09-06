# -*- coding: utf-8 -*-
"""SO CONG BO THEO BANG XEP HANG NAO? Doi chieu bach_thu voi 3 ung vien:
   (a) ranked_numbers[0]           — bang xep hang SAU PP-1 (thu he tu ghi la top1)
   (b) top1 khi DUNG LAI diem TRUOC PP-1
   (c) khong phai ca hai
Tra loi bang dem tren toan bo lich su sach. CHI DOC.
"""
import sqlite3, json, collections
c = sqlite3.connect("file:/root/Lottery_AI_Test/data/lottery_ai.db?mode=ro", uri=True)
c.row_factory = sqlite3.Row

dem = collections.Counter()
dem_mien = collections.defaultdict(collections.Counter)
dem_thang = collections.defaultdict(collections.Counter)
khac_ca_hai = []
for r in c.execute("SELECT id,date,region,bach_thu,bach_thu_status,notes,source_predictions_json "
                   "FROM final_bundles ORDER BY date"):
    if (r["notes"] or "").find("Phase 1.5 backfill") >= 0: continue
    try: j = json.loads(r["source_predictions_json"] or "{}")
    except Exception: continue
    rn = j.get("ranked_numbers") or []
    if not rn: continue
    bt = (r["bach_thu"] or "").strip()
    if not bt: continue
    a = (rn[0].get("number") or "").strip()
    truoc = {x.get("number"): (x.get("score") or 0) for x in rn}
    pp1 = j.get("pp1_convergence_dampener") or {}
    for e in (pp1.get("events") or []):
        if e.get("number") in truoc and e.get("score_before") is not None:
            truoc[e["number"]] = e["score_before"]
    b = max(truoc.items(), key=lambda kv: kv[1])[0] if truoc else None
    if bt == a:
        k = "a_ranked0" if a == b else "a_ranked0 (PP1 giu nguyen thu hang)"
        k = "khop ranked[0]"
    elif bt == b:
        k = "khop top1 TRUOC PP-1 (bo qua PP-1)"
    else:
        k = "KHONG khop ca hai"
        khac_ca_hai.append((r["date"], r["region"], bt, a, b, r["bach_thu_status"]))
    dem[k] += 1
    dem_mien[r["region"]][k] += 1
    dem_thang[r["date"][:7]][k] += 1

tong = sum(dem.values())
print("=== bach_thu CONG BO khop voi cai gi? (n=%d bundle sach) ===" % tong)
for k, v in dem.most_common():
    print("  %-40s %5d  (%.1f%%)" % (k, v, 100*v/tong))

print("\n=== THEO MIEN ===")
for reg in sorted(dem_mien):
    t = sum(dem_mien[reg].values())
    print("  %s (n=%d)" % (reg, t))
    for k, v in dem_mien[reg].most_common():
        print("      %-40s %5d  (%.1f%%)" % (k, v, 100*v/t))

print("\n=== THEO THANG (chi cot KHONG khop ca hai) ===")
for th in sorted(dem_thang):
    t = sum(dem_thang[th].values())
    x = dem_thang[th]["KHONG khop ca hai"]
    y = dem_thang[th]["khop top1 TRUOC PP-1 (bo qua PP-1)"]
    print("  %s  n=%-4d  khac ca hai=%-4d (%.0f%%)   bo qua PP-1=%-3d" % (th, t, x, 100*x/t if t else 0, y))

print("\n=== 25 CA 'KHONG KHOP CA HAI' GAN NHAT ===")
print("  %-11s %-4s %-8s %-10s %-10s %s" % ("ngay","mien","cong bo","ranked[0]","truoc PP1","ket qua"))
for x in khac_ca_hai[-25:]:
    print("  %-11s %-4s %-8s %-10s %-10s %s" % x)
print("\n  TONG so ca khong khop ca hai: %d" % len(khac_ca_hai))
