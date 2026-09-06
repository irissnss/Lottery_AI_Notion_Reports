# -*- coding: utf-8 -*-
"""BO HAM PP-1: no co lam thay doi so cong bo khong, va lam vay TOT hay XAU?

Cach do (khong tu dinh nghia lai): moi bundle luu san
  - ranked_numbers: diem SAU khi ap PP-1
  - pp1_convergence_dampener.events[]: moi su kien co score_before va score_after
Dung score_before de dung lai bang xep hang GIA DINH KHONG CO PP-1, roi so:
  so se duoc chon neu KHONG co PP-1   vs   so THUC SU da cong bo (cot bach_thu)
va doi chieu voi tap duoi that cua mien-ngay do.
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

co_pp1 = 0; bat = 0; doi_top1 = 0; bo_backfill = 0
ket = {"pp1_dung": 0, "pp1_sai": 0, "hue": 0}
chi_tiet = []
tong_bundle = 0
for r in c.execute("SELECT id,date,region,bach_thu,bach_thu_status,notes,source_predictions_json "
                   "FROM final_bundles ORDER BY date"):
    if (r["notes"] or "").find("Phase 1.5 backfill") >= 0:
        bo_backfill += 1; continue
    try: j = json.loads(r["source_predictions_json"] or "{}")
    except Exception: continue
    tong_bundle += 1
    pp1 = j.get("pp1_convergence_dampener")
    if not isinstance(pp1, dict): continue
    co_pp1 += 1
    if not pp1.get("enabled"): continue
    ev = pp1.get("events") or []
    if not ev: continue
    bat += 1
    rn = j.get("ranked_numbers") or []
    if not rn: continue
    # dung lai diem KHONG CO PP-1
    truoc = {}
    for x in rn:
        truoc[x.get("number")] = x.get("score") or 0
    for e in ev:
        if e.get("number") in truoc and e.get("score_before") is not None:
            truoc[e["number"]] = e["score_before"]
    if not truoc: continue
    top_khong_pp1 = max(truoc.items(), key=lambda kv: kv[1])[0]
    top_co_pp1 = rn[0].get("number")
    if top_khong_pp1 == top_co_pp1: continue
    doi_top1 += 1
    d = tap.get((r["date"], r["region"]), set())
    if not d: continue
    a = top_khong_pp1 in d          # so BI HAM co trung khong
    b = top_co_pp1 in d             # so DUOC LEN co trung khong
    if b and not a: ket["pp1_dung"] += 1; nhan = "PP1 DUNG"
    elif a and not b: ket["pp1_sai"] += 1; nhan = "PP1 SAI"
    else: ket["hue"] += 1; nhan = "hue"
    chi_tiet.append((r["date"], r["region"], top_khong_pp1, a, top_co_pp1, b,
                     r["bach_thu"], r["bach_thu_status"], nhan))

print("=== PHAM VI ===")
print("  bundle xet (da bo %d backfill): %d" % (bo_backfill, tong_bundle))
print("  co truong pp1_convergence_dampener : %d" % co_pp1)
print("  PP-1 BAT va CO su kien             : %d" % bat)
print("  PP-1 THUC SU DOI top1              : %d" % doi_top1)
print("\n=== KHI PP-1 DOI TOP1 THI NO DUNG HAY SAI ===")
tong = sum(ket.values())
for k, v in ket.items():
    print("  %-10s %4d  (%.1f%%)" % (k, v, 100*v/tong if tong else 0))
if ket["pp1_dung"] + ket["pp1_sai"]:
    n = ket["pp1_dung"] + ket["pp1_sai"]; w = ket["pp1_dung"]
    p = w/n; z = 1.96; dd = 1 + z*z/n
    ctr = (p + z*z/(2*n))/dd
    hw = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/dd
    print("\n  Bo cac ca hue: PP-1 dung %d/%d = %.1f%%  KTC95 [%.1f%% , %.1f%%]"
          % (w, n, 100*p, 100*(ctr-hw), 100*(ctr+hw)))
    print("  Neu PP-1 vo dung thi ti le nay = 50%%. %s"
          % ("KHAC 50% co y nghia" if (ctr-hw) > 0.5 or (ctr+hw) < 0.5 else "KHONG tach duoc khoi 50% => CHUA DUOC PHEP KET LUAN (RM-04)"))

print("\n=== 30 CA GAN NHAT ===")
print("  %-11s %-4s %-6s %-6s %-6s %-6s %-6s %-6s %s" %
      ("ngay","mien","bi ham","trung?","duoc len","trung?","cong bo","ket qua","nhan"))
for x in chi_tiet[-30:]:
    print("  %-11s %-4s %-6s %-6s %-8s %-6s %-7s %-7s %s" %
          (x[0], x[1], x[2], "CO" if x[3] else "khong", x[4], "CO" if x[5] else "khong",
           x[6], x[7], x[8]))
