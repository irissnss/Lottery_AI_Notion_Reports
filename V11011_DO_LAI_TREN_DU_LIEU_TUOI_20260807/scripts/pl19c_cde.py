# -*- coding: utf-8 -*-
"""PL19c Phần C (Q17·Q18·Q20) · D2 · E5 — trên dữ liệu TƯƠI. READ-ONLY."""
import collections
import datetime as dt
import json
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")
c = sqlite3.connect("file:data/lottery_ai.db?mode=ro", uri=True)
c.row_factory = sqlite3.Row
HOM_NAY = dt.date.today()

print("=" * 98)
print("Q17 — SWEEP 'CHẾT NHƯNG TƯỞNG SỐNG': bảng nào có dữ liệu cũ hơn 14 ngày?")
print("=" * 98)
bang = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table' "
                                "AND name NOT LIKE 'sqlite_%' ORDER BY name")]
chet, song, khong_ngay = [], [], []
for b in bang:
    cot = [x[1] for x in c.execute(f"PRAGMA table_info('{b}')")]
    tc = next((x for x in ("date", "run_date", "snapshot_date", "eval_date", "created_at")
               if x in cot), None)
    if not tc:
        khong_ngay.append(b)
        continue
    try:
        r = c.execute(f"SELECT COUNT(*) n, MAX({tc}) d FROM '{b}'").fetchone()
    except Exception:
        continue
    if not r["n"] or not r["d"]:
        chet.append((b, r["n"], "RỖNG", 9999))
        continue
    try:
        d = dt.date.fromisoformat(str(r["d"])[:10])
        tuoi = (HOM_NAY - d).days
    except Exception:
        continue
    (chet if tuoi > 14 else song).append((b, r["n"], str(r["d"])[:10], tuoi))
chet.sort(key=lambda x: -x[3])
print(f"  tổng {len(bang)} bảng · có cột ngày {len(bang)-len(khong_ngay)} · "
      f"SỐNG (≤14 ngày) {len(song)} · **CŨ/RỖNG {len(chet)}**")
print(f"\n  {'bảng':46} {'dòng':>7} {'mới nhất':>12} {'cũ (ngày)':>10}")
for b, n, d, t in chet[:28]:
    print(f"  {b[:46]:46} {n:>7} {d:>12} {('RỖNG' if t == 9999 else t):>10}")
if len(chet) > 28:
    print(f"  … còn {len(chet)-28} bảng nữa")

print()
print("=" * 98)
print("Q18 — BUNDLE THIẾU PHIẾU: bao nhiêu, và có liên quan bầy đàn không?")
print("=" * 98)


def pick(s):
    s = str(s or "").strip()
    try:
        v = json.loads(s)
        s = str(v[0] if isinstance(v, list) and v else v)
    except Exception:
        s = s.split(",")[0]
    d = "".join(ch for ch in s if ch.isdigit())
    return d[-2:] if len(d) >= 2 else None


ngay = collections.defaultdict(list)
for r in c.execute("""SELECT date d,target_region r,ai_model m,main_numbers mn FROM predictions
                      WHERE date>=date('now','-30 day') AND main_numbers IS NOT NULL
                        AND target_region IN ('MN','MT','MB')"""):
    p = pick(r["mn"])
    if p:
        ngay[(r["d"], r["r"])].append(p)
cot = [x[1] for x in c.execute("PRAGMA table_info(final_bundles)")]
cbt = next((x for x in ("bach_thu", "bt", "main_number") if x in cot), None)
print(f"  cột số chính của final_bundles: {cbt}")
thieu = du = 0
if cbt:
    for r in c.execute(f"""SELECT date,region,{cbt} bt FROM final_bundles
                           WHERE date>=date('now','-30 day') AND {cbt} IS NOT NULL"""):
        ms = ngay.get((r["date"], r["region"]))
        if not ms:
            continue
        bt = "".join(ch for ch in str(r["bt"]) if ch.isdigit())[-2:]
        (du if bt in ms else thieu).__class__
        if bt in ms:
            du += 1
        else:
            thieu += 1
    t = thieu + du
    if t:
        print(f"  30 ngày · {t} bundle · số chốt CÓ trong phiếu model: {du} "
              f"({du/t*100:.0f}%) · **KHÔNG có phiếu nào: {thieu} ({thieu/t*100:.0f}%)**")

print()
print("=" * 98)
print("Q20 — MB CHẠY THEO CƠ CHẾ NÀO THẬT SỰ? (14 ngày gần nhất)")
print("=" * 98)
print(f"  {'ngày':12} {'run_source có mặt cho MB':<52} {'số model':>9}")
for d in [r[0] for r in c.execute("SELECT DISTINCT date FROM predictions "
                                  "WHERE target_region='MB' AND date>=date('now','-14 day') "
                                  "ORDER BY date DESC")][:14]:
    rs = collections.Counter(r[0] for r in c.execute(
        "SELECT run_source FROM predictions WHERE target_region='MB' AND date=?", (d,)))
    n = sum(rs.values())
    print(f"  {d:12} {', '.join(f'{k}×{v}' for k, v in rs.most_common()):<52} {n:>9}")
print("\n  ⇒ nếu MỌI ngày đều có rerun_post_mt → cơ chế V10895 (luôn rerun) đang chạy,")
print("     V10770 (đầu tháng samday / cuối tháng D-1) đã bị THAY THẾ.")

print()
print("=" * 98)
print("D2 — HERD CÓ KIỂM SOÁT: khoá tập model AI chạy CẢ TRƯỚC lẫn SAU 29/03")
print("=" * 98)
MOC = "2026-03-29"
ML = {"meta-learning", "lstm", "xgboost", "random-forest", "smart-ensemble", "smart-ml",
      "combo-super", "combo-no-token", "smart-ml-notoken"}
tr, sa = set(), set()
for r in c.execute("SELECT DISTINCT ai_model, date FROM predictions WHERE date>='2025-11-01'"):
    (tr if r[1] < MOC else sa).add(r[0])
chung = sorted((tr & sa) - ML)
print(f"  model AI chạy TRƯỚC 29/03: {len(tr-ML)} · SAU: {len(sa-ML)} · "
      f"**CHUNG cả hai phía: {len(chung)}**")
print(f"  tập chung: {', '.join(chung) if chung else '(rỗng)'}")
if len(chung) < 3:
    print("\n  ⇒ KHÔNG ĐỦ model chung để đo có kiểm soát. Ghi rõ 'KHÔNG ĐO ĐƯỢC', cấm suy diễn.")
else:
    ng2 = collections.defaultdict(list)
    for r in c.execute("""SELECT date d,target_region r,ai_model m,main_numbers mn FROM predictions
                          WHERE date>='2025-11-01' AND main_numbers IS NOT NULL
                            AND target_region IN ('MN','MT','MB')"""):
        if r["m"] in chung:
            p = pick(r["mn"])
            if p:
                ng2[(r["d"], r["r"])].append(p)
    print(f"\n  {'giai đoạn':14} {'ngày':>6} {'model/ngày':>11} {'số khác nhau':>13} {'hệ số':>8}")
    for nhan, dk in (("TRƯỚC 29/03", lambda x: x < MOC), ("SAU 29/03", lambda x: x >= MOC)):
        ds = [k for k in ng2 if dk(k[0]) and len(ng2[k]) >= 3]
        if not ds:
            print(f"  {nhan:14} (không đủ ngày)")
            continue
        tm = sum(len(ng2[k]) for k in ds)
        ts = sum(len(set(ng2[k])) for k in ds)
        print(f"  {nhan:14} {len(ds):>6} {tm/len(ds):>11.1f} {ts/len(ds):>13.1f} {tm/ts:>7.2f}×")

print()
print("=" * 98)
print("E5 — pnl_daily_summary: 14 dòng tổng hợp từ đâu, có cột cờ chưa?")
print("=" * 98)
cot = [x[1] for x in c.execute("PRAGMA table_info(pnl_daily_summary)")]
print(f"  cột: {', '.join(cot)}")
r = c.execute("SELECT COUNT(*) n, MIN(date) d0, MAX(date) d1 FROM pnl_daily_summary").fetchone()
print(f"  {r['n']} dòng · {r['d0']} → {r['d1']}")
print(f"  có cột cờ shadow/real: {'CÓ' if any(x in cot for x in ('shadow_only','is_real','mode')) else '❌ KHÔNG'}")
c.close()
