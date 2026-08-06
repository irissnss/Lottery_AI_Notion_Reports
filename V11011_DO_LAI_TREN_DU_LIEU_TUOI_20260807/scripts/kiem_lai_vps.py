# -*- coding: utf-8 -*-
"""PL19c — KIỂM LẠI TOÀN BỘ con số đầu bài của V10991→V11009 trên VPS (nguồn thật).

Bản local đồng bộ lần cuối 05/08 12:11. Mọi phép đo sau đó cũ 9–35 giờ.
Script này chạy TRÊN VPS, read-only, để biết con số nào ĐỔI và con số nào GIỮ.
"""
import sys

import paramiko

sys.stdout.reconfigure(encoding="utf-8")

MA = r'''
import json, math, sqlite3, collections
c = sqlite3.connect("file:/root/Lottery_AI_Test/data/lottery_ai.db?mode=ro", uri=True)
c.row_factory = sqlite3.Row
ML = {"meta-learning","lstm","xgboost","random-forest","smart-ensemble","smart-ml",
      "combo-super","combo-no-token","smart-ml-notoken"}

def pick(s):
    s = str(s or "").strip()
    try:
        v = json.loads(s); s = str(v[0] if isinstance(v,list) and v else v)
    except Exception:
        s = s.split(",")[0]
    d = "".join(ch for ch in s if ch.isdigit())
    return d[-2:] if len(d) >= 2 else None

def duoi(reg, d, kho={}):
    k=(reg,d)
    if k in kho: return kho[k]
    out=set()
    for (pj,) in c.execute("SELECT prizes_json FROM lottery_results WHERE region=? AND date=? AND prizes_json IS NOT NULL",(reg,d)):
        try: pr=json.loads(pj)
        except Exception: continue
        for v in (pr.values() if isinstance(pr,dict) else []):
            for x in (v if isinstance(v,list) else [v]):
                s="".join(ch for ch in str(x) if ch.isdigit())
                if len(s)>=2: out.add(s[-2:])
    kho[k]=out; return out

print("### 1. V11000/V11005 — CO MODEL NAO HON NEN KHONG? (quyet dinh FU-290 han 08/08)")
thong = collections.defaultdict(lambda: {"n":0,"k":0,"nen":0.0})
for r in c.execute("""SELECT target_region r,date d,ai_model m,main_numbers mn FROM predictions
                      WHERE date>=date('now','-180 day') AND main_numbers IS NOT NULL
                        AND target_region IN ('MN','MT','MB')"""):
    p=pick(r["mn"])
    if not p: continue
    thuc=duoi(r["r"],r["d"])
    if not thuc: continue
    t=thong[r["m"]]; t["n"]+=1; t["k"]+= 1 if p in thuc else 0; t["nen"]+=len(thuc)/100.0
hang=[]
for m,t in thong.items():
    if t["n"]<60: continue
    p0=t["nen"]/t["n"]; v=t["n"]*p0*(1-p0)
    z=(t["k"]-t["n"]*p0)/math.sqrt(v) if v>0 else 0
    hang.append((m,t["n"],t["k"]/t["n"]*100,p0*100,z))
hang.sort(key=lambda x:-x[4])
hon=[h for h in hang if h[4]>=3.01]
print("  so model >=60 luot: %d · HON NEN sau Bonferroni (|z|>=3,01): %d" % (len(hang), len(hon)))
print("  top 3:", ", ".join("%s z=%+.2f" % (h[0][:20],h[4]) for h in hang[:3]))
print("  bet 2:", ", ".join("%s z=%+.2f" % (h[0][:20],h[4]) for h in hang[-2:]))

print()
print("### 2. V11000 — BAY DAN")
ngay=collections.defaultdict(list)
for r in c.execute("""SELECT date d,target_region r,ai_model m,main_numbers mn FROM predictions
                      WHERE date>=date('now','-180 day') AND main_numbers IS NOT NULL
                        AND target_region IN ('MN','MT','MB')"""):
    p=pick(r["mn"])
    if p: ngay[(r["d"],r["r"])].append((r["m"],p))
for reg in ("MN","MT","MB"):
    ds=[k for k in ngay if k[1]==reg]
    if not ds: continue
    tm=sum(len(ngay[k]) for k in ds); ts=sum(len({p for _,p in ngay[k]}) for k in ds)
    print("  %s: %.1f model/ngay -> %.1f so khac nhau (he so %.2fx)" % (reg,tm/len(ds),ts/len(ds),tm/ts))

print()
print("### 3. V11006 — TEN DAI: co ten la moi khong?")
dai=[r[0] for r in c.execute("SELECT DISTINCT station FROM lottery_results WHERE station IS NOT NULL AND date>=date('now','-400 day')")]
print("  so dai dang song: %d" % len(dai))
moi=[r[0] for r in c.execute("SELECT station FROM lottery_results WHERE station IS NOT NULL GROUP BY station HAVING MIN(date)>='2026-08-05'")]
print("  dai XUAT HIEN LAN DAU tu 05/08:", moi or "khong co")

print()
print("### 4. V11003 — DO TIEN that su bao nhieu?")
r=c.execute("""SELECT SUM(CASE WHEN e.date>date(r.mined_at) THEN 1 ELSE 0 END) dt,
   COUNT(DISTINCT CASE WHEN e.date>date(r.mined_at) THEN e.date END) nd,
   COUNT(DISTINCT CASE WHEN e.date>date(r.mined_at) THEN e.rule_id END) nr
   FROM mined_rule_effectiveness e JOIN mined_rules r ON r.id=e.rule_id""").fetchone()
print("  DO_TIEN: %d dong · %d ngay · %d luat  (local bao: 15 dong / 1 ngay / 15 luat)" % (r["dt"],r["nd"],r["nr"]))

print()
print("### 5. V10993/V10994 — bundle lam bu + shadow")
r=c.execute("SELECT COUNT(*) n FROM final_bundles WHERE created_at IS NOT NULL AND date(created_at)>date").fetchone()
print("  bundle LAM BU (date(created_at)>date): %d  (local bao: 90)" % r["n"])
try:
    r2=c.execute("SELECT COUNT(*) n FROM du_doan_test_bundles WHERE output_eligible=0").fetchone()
    print("  shadow output_eligible=0: %d  (local bao: 512)" % r2["n"])
except Exception as e:
    print("  shadow: khong doc duoc -", str(e)[:60])

print()
print("### 6. V11000 — bang chi phi con rong khong?")
try:
    r=c.execute("SELECT COUNT(*) n, SUM(cost_estimate IS NOT NULL) c, SUM(latency_seconds IS NOT NULL) l FROM model_latency_cost_audit_daily").fetchone()
    print("  model_latency_cost_audit_daily: %d dong · cost khong rong %s · latency khong rong %s  (local bao 0/4033)" % (r["n"],r["c"],r["l"]))
except Exception as e:
    print("  ", str(e)[:70])

print()
print("### 7. moc du lieu hien tai tren VPS")
for b in ("lottery_results","predictions","final_bundles","model_daily_eval","mined_rule_effectiveness"):
    r=c.execute("SELECT COUNT(*) n, MAX(date) d FROM %s" % b).fetchone()
    print("  %-28s %6d dong · moi nhat %s" % (b,r["n"],r["d"]))
'''

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
cli.connect("14.225.224.89", username="root",
            key_filename=r"C:\Users\Admin\.ssh\id_ed25519", timeout=60)
sftp = cli.open_sftp()
with sftp.open("/tmp/_pl19c_kiem.py", "w") as f:
    f.write(MA)
_i, o, e = cli.exec_command("/root/Lottery_AI_Test/venv/bin/python3 /tmp/_pl19c_kiem.py", timeout=900)
print(o.read().decode("utf-8", "replace"))
err = e.read().decode("utf-8", "replace")
if err.strip():
    print("stderr:", err[:600])
sftp.close()
cli.close()
