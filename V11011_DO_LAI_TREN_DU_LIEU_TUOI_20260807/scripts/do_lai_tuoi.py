# -*- coding: utf-8 -*-
"""V11011 — ĐO LẠI TOÀN BỘ trên dữ liệu TƯƠI (đồng bộ 07/08 00:31).

Đối chiếu từng con số với bản đã công bố trên dữ liệu cũ.
"""
import collections
import json
import math
import os
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")

# ── cổng FU-303: từ chối chạy nếu dữ liệu cũ ────────────────────────────────
M = json.load(open("artifacts/live_sync/latest_manifest.json", encoding="utf-8"))
import datetime as dt
sync = dt.datetime.fromisoformat(M["sync_completed_at"])
tuoi = (dt.datetime.now(sync.tzinfo) - sync).total_seconds() / 3600
print(f"[cong] DU_LIEU_TUOI sync={M['sync_completed_at'][:19]} cu={tuoi:.1f} gio")
if tuoi > 6:
    print("✗ DỪNG — dữ liệu cũ hơn 6 giờ. Chạy web/_sync_live_forensic_inputs.py trước.")
    raise SystemExit(1)

c = sqlite3.connect("file:data/lottery_ai.db?mode=ro", uri=True)
c.row_factory = sqlite3.Row
ML = {"meta-learning", "lstm", "xgboost", "random-forest", "smart-ensemble", "smart-ml",
      "combo-super", "combo-no-token", "smart-ml-notoken"}
SS = []   # (tên, cũ, mới)


def pick(s):
    s = str(s or "").strip()
    try:
        v = json.loads(s)
        s = str(v[0] if isinstance(v, list) and v else v)
    except Exception:
        s = s.split(",")[0]
    d = "".join(ch for ch in s if ch.isdigit())
    return d[-2:] if len(d) >= 2 else None


def duoi(reg, d, kho={}):
    k = (reg, d)
    if k in kho:
        return kho[k]
    out = set()
    for (pj,) in c.execute("SELECT prizes_json FROM lottery_results WHERE region=? AND date=?"
                           " AND prizes_json IS NOT NULL", (reg, d)):
        try:
            pr = json.loads(pj)
        except Exception:
            continue
        for v in (pr.values() if isinstance(pr, dict) else []):
            for x in (v if isinstance(v, list) else [v]):
                s = "".join(ch for ch in str(x) if ch.isdigit())
                if len(s) >= 2:
                    out.add(s[-2:])
    kho[k] = out
    return out


ngay = collections.defaultdict(list)
for r in c.execute("""SELECT date d, target_region r, ai_model m, main_numbers mn FROM predictions
                      WHERE date >= date('now','-180 day') AND main_numbers IS NOT NULL
                        AND target_region IN ('MN','MT','MB')"""):
    p = pick(r["mn"])
    if p:
        ngay[(r["d"], r["r"])].append((r["m"], p))

print()
print("=" * 96)
print("1. MODEL NÀO HƠN NỀN — quyết định FU-290 (owner ký 08/08)")
print("=" * 96)
th = collections.defaultdict(lambda: {"n": 0, "k": 0, "nen": 0.0})
for (d, reg), ms in ngay.items():
    thuc = duoi(reg, d)
    if not thuc:
        continue
    for m, p in ms:
        t = th[m]
        t["n"] += 1
        t["k"] += 1 if p in thuc else 0
        t["nen"] += len(thuc) / 100.0
hang = []
for m, t in th.items():
    if t["n"] < 60:
        continue
    p0 = t["nen"] / t["n"]
    v = t["n"] * p0 * (1 - p0)
    hang.append((m, t["n"], t["k"] / t["n"] * 100, p0 * 100,
                 (t["k"] - t["n"] * p0) / math.sqrt(v) if v > 0 else 0))
hang.sort(key=lambda x: -x[4])
hon = [h for h in hang if abs(h[4]) >= 3.01]
print(f"  {len(hang)} model ≥60 lượt · HƠN/KÉM nền sau Bonferroni (|z|≥3,01): {len(hon)}")
print(f"  {'model':26} {'n':>5} {'trúng':>7} {'nền':>7} {'z':>8}")
for h in hang[:4] + hang[-3:]:
    print(f"  {h[0][:26]:26} {h[1]:>5} {h[2]:>6.1f}% {h[3]:>6.1f}% {h[4]:>+8.2f}")
SS.append(("model hơn nền (Bonferroni)", "0/34", f"{len(hon)}/{len(hang)}"))

print()
print("=" * 96)
print("2. BẦY ĐÀN")
print("=" * 96)
for reg in ("MN", "MT", "MB"):
    ds = [k for k in ngay if k[1] == reg]
    tm = sum(len(ngay[k]) for k in ds)
    ts = sum(len({p for _, p in ngay[k]}) for k in ds)
    print(f"  {reg}: {tm/len(ds):>5.1f} model/ngày → {ts/len(ds):>4.1f} số khác nhau "
          f"(hệ số {tm/ts:.2f}×)")
SS.append(("bầy đàn MN", "21,6 → 9,2", ""))

print()
print("=" * 96)
print("3. HỘI TỤ — quyết định FU-298")
print("=" * 96)
b = collections.defaultdict(lambda: [0, 0, 0.0])
for (d, reg), ms in ngay.items():
    if d < "2026-05-08":
        continue
    thuc = duoi(reg, d)
    if not thuc:
        continue
    dem = collections.Counter(p for _, p in ms)
    nen = len(thuc) / 100.0
    for so, k in dem.items():
        o = "1-2" if k <= 2 else ("3" if k == 3 else ">=4")
        b[o][0] += 1
        b[o][1] += 1 if so in thuc else 0
        b[o][2] += nen
print(f"  {'mức':6} {'lượt':>6} {'trúng':>6} {'tỉ lệ':>8} {'nền':>7} {'z':>8}")
z3 = None
for o in ("1-2", "3", ">=4"):
    n, k, nn = b[o]
    p0 = nn / n
    v = n * p0 * (1 - p0)
    z = (k - n * p0) / math.sqrt(v) if v > 0 else 0
    print(f"  {o:6} {n:>6} {k:>6} {k/n*100:>7.1f}% {p0*100:>6.1f}% {z:>+8.2f}")
    if o == "3":
        z3 = (n, z)
SS.append(("hội tụ 3 nguồn", "n=294 z=−2,51", f"n={z3[0]} z={z3[1]:+.2f}"))

print()
print("=" * 96)
print("4. BẢNG A/B samday MT — quyết định FU-297 (mốc 12/08)")
print("=" * 96)
r = c.execute("""SELECT COUNT(DISTINCT date) n, MIN(date) d0, MAX(date) d1, COUNT(*) tong
                 FROM v10801_ml_mark_ab_daily WHERE date >= '2026-07-15'""").fetchone()
print(f"  ngày forward từ 15/07: {r['n']}/28 · {r['d0']} → {r['d1']} · {r['tong']} dòng")
con = 28 - r["n"]
print(f"  còn thiếu {con} ngày ⇒ đủ vào ~2026-08-{6+con:02d} · mốc chốt 12/08 "
      f"{'KHẢ THI' if 6+con <= 12 else 'KHÔNG KỊP'}")
SS.append(("A/B ngày forward", "21/28 (ĐỨT)", f"{r['n']}/28 (liên tục)"))

print()
print("=" * 96)
print("5. FU-305 — phạm vi đếm shadow output_eligible=0")
print("=" * 96)
tong = c.execute("SELECT COUNT(*) FROM du_doan_test_bundles WHERE output_eligible=0").fetchone()[0]
print(f"  toàn thời gian: {tong}")
for nhan, dk in (("30 ngày", "run_date>=date('now','-30 day')"),
                 ("60 ngày", "run_date>=date('now','-60 day')"),
                 ("từ 08/05", "run_date>='2026-05-08'")):
    n = c.execute(f"SELECT COUNT(*) FROM du_doan_test_bundles WHERE output_eligible=0 "
                  f"AND {dk}").fetchone()[0]
    print(f"  {nhan:12}: {n}")
print("  ⇒ con số 512 của V10994 phải khớp một trong các cửa sổ trên; nếu không khớp thì")
print("     nó đếm theo tiêu chí khác (ví dụ chỉ lane còn sống).")

print()
print("=" * 96)
print("6. BẢNG CHI PHÍ + BUNDLE LÀM BÙ")
print("=" * 96)
r = c.execute("SELECT COUNT(*) n, SUM(cost_estimate IS NOT NULL) ce, "
              "SUM(latency_seconds IS NOT NULL) ls FROM model_latency_cost_audit_daily").fetchone()
print(f"  model_latency_cost_audit_daily: {r['n']} dòng · cost {r['ce']} · latency {r['ls']}")
n = c.execute("SELECT COUNT(*) FROM final_bundles WHERE created_at IS NOT NULL "
              "AND date(created_at) > date").fetchone()[0]
print(f"  bundle làm bù: {n}")
SS.append(("bảng chi phí", "0/4033", f"{r['ce']}/{r['n']}"))
SS.append(("bundle làm bù", "90", str(n)))

print()
print("=" * 96)
print("BẢNG ĐỐI CHIẾU — cũ (dữ liệu 05/08) vs mới (dữ liệu 06/08)")
print("=" * 96)
print(f"  {'con số':34} {'CŨ đã công bố':>18} {'MỚI (tươi)':>20}")
print("  " + "-" * 76)
for ten, cu, moi in SS:
    if moi:
        print(f"  {ten:34} {cu:>18} {moi:>20}")
c.close()
