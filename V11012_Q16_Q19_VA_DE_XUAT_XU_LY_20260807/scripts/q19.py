# -*- coding: utf-8 -*-
"""PL19c Q19 — LANE TỰ CHẤM SAI SỐ (V10884, 31/07): vá gốc đã chạy chưa, còn ca nào?

Bệnh: luồng CÔNG BỐ một con số lúc sáng, rồi lúc chấm TÍNH LẠI ra con khác và
chấm con tính lại. Tức "công bố một đằng, tự chấm một nẻo".
"""
import collections
import datetime as dt
import json
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")

M = json.load(open("artifacts/live_sync/latest_manifest.json", encoding="utf-8"))
s0 = dt.datetime.fromisoformat(M["sync_completed_at"])
tuoi = (dt.datetime.now(s0.tzinfo) - s0).total_seconds() / 3600
print(f"[cong] DU_LIEU_TUOI cu={tuoi:.1f} gio")
if tuoi > 6:
    raise SystemExit("✗ dữ liệu cũ")

c = sqlite3.connect("file:data/lottery_ai.db?mode=ro", uri=True)
c.row_factory = sqlite3.Row

print()
print("=" * 96)
print("Q19-a — CẤU TRÚC: bảng nào giữ SỐ CÔNG BỐ, bảng nào giữ SỐ ĐEM CHẤM?")
print("=" * 96)
for b in ("du_doan_test_bundles", "du_doan_test_results"):
    cot = [x[1] for x in c.execute(f"PRAGMA table_info({b})")]
    r = c.execute(f"SELECT COUNT(*) n, MAX(run_date) d FROM {b}").fetchone() \
        if "run_date" in cot else c.execute(f"SELECT COUNT(*) n FROM {b}").fetchone()
    print(f"\n  {b}: {r['n']} dòng" + (f" · mới nhất {r['d']}" if "run_date" in cot else ""))
    print(f"    cột: {', '.join(cot)}")

print()
print("=" * 96)
print("Q19-b — CÒN CA NÀO 'CÔNG BỐ MỘT ĐẰNG, CHẤM MỘT NẺO' KHÔNG? (30 ngày)")
print("=" * 96)
cb = [x[1] for x in c.execute("PRAGMA table_info(du_doan_test_bundles)")]
cr = [x[1] for x in c.execute("PRAGMA table_info(du_doan_test_results)")]
# cột số công bố trong bundles
c_pub = next((x for x in ("test_bt", "bach_thu", "bt") if x in cb), None)
# cột số đem chấm trong results
c_cham = next((x for x in ("test_bt", "bach_thu", "bt", "scored_bt") if x in cr), None)
print(f"  cột số CÔNG BỐ (bundles): {c_pub}")
print(f"  cột số ĐEM CHẤM (results): {c_cham}")

if c_pub and c_cham and "run_id" in cb and "run_id" in cr:
    q = f"""SELECT b.run_date, b.region, b.experiment_name,
                   b.{c_pub} pub, r.{c_cham} cham
              FROM du_doan_test_bundles b
              JOIN du_doan_test_results r ON r.run_id = b.run_id
             WHERE b.run_date >= date('now','-30 day')
               AND b.{c_pub} IS NOT NULL AND r.{c_cham} IS NOT NULL"""
    n = lech = 0
    ds = []
    for x in c.execute(q):
        a = str(x["pub"]).strip()
        b2 = str(x["cham"]).strip()
        n += 1
        if a != b2:
            lech += 1
            ds.append((x["run_date"], x["region"], x["experiment_name"], a, b2))
    print(f"\n  đối chiếu {n} cặp (run_id khớp) · **LỆCH {lech}**")
    if ds:
        print(f"  {'ngày':12} {'miền':5} {'lane':26} {'công bố':>10} {'đem chấm':>10}")
        for d, rg, e, a, b2 in ds[:15]:
            print(f"  {d:12} {rg:5} {str(e)[:26]:26} {a:>10} {b2:>10}")
    else:
        print("  ✓ KHÔNG ca nào lệch — vá gốc V10884 đang giữ được")
else:
    print("  ⚠ không đủ cột để đối chiếu tự động — cần chỉ đúng tên cột")

print()
print("=" * 96)
print("Q19-c — CỔNG CHẶN V10884 CÓ THẬT SỰ CHẠY KHÔNG? (luồng có chờ official không)")
print("=" * 96)
# nếu luồng chờ official thì số model dùng phải ~ bằng official
if "model_count" in cb:
    print(f"  {'miền':6} {'ngày':12} {'model_count lane':>17} {'model official':>16}")
    for rg in ("MN", "MT", "MB"):
        for r in c.execute("""SELECT run_date, region, MAX(model_count) mc
                              FROM du_doan_test_bundles WHERE region=? AND model_count IS NOT NULL
                                AND run_date>=date('now','-7 day')
                              GROUP BY run_date ORDER BY run_date DESC LIMIT 3""", (rg,)):
            o = c.execute("SELECT COUNT(DISTINCT ai_model) n FROM predictions "
                          "WHERE target_region=? AND date=?", (rg, r["run_date"])).fetchone()
            print(f"  {rg:6} {r['run_date']:12} {r['mc']:>17} {o['n']:>16}")
else:
    print("  (bảng không có cột model_count)")

print()
print("=" * 96)
print("Q19-d — PHÉP KIỂM 'số publish == số chấm' có chạy hằng ngày không?")
print("=" * 96)
import glob
import os
co = [os.path.basename(p) for p in glob.glob("web/backend/*.py")
      if any(k in os.path.basename(p).lower() for k in ("10884", "publish_vs", "cham_lech"))]
print(f"  script liên quan V10884: {co or '(không tìm thấy)'}")
c.close()
