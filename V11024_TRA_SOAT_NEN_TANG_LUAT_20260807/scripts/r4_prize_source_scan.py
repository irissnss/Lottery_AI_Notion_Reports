# -*- coding: utf-8 -*-
"""
R4 — DO SUC MANH TUNG NHOM GIAI SOI (prize-source scan).  READ-ONLY.

Nguyen tac do:
  * hit_any cua he = "co it nhat 1 duoi so nguon xuat hien trong TOAN BO ket qua mien dich".
    Xac suat nen cua phep nay KHONG phai 1/100 — no phu thuoc:
        k = so duoi so KHAC NHAU ma giai nguon sinh ra
        T = so duoi so KHAC NHAU co trong ket qua mien dich NGAY HOM DO
    Nen dung ngay:  p_nen = 1 - C(100-T, k) / C(100, k)
  * z Poisson-binomial:  z = (O - E) / sqrt(sum p_i(1-p_i))   [gia dinh doc lap]
  * z cum theo ngay (cluster-robust): moi ngay 1 quan sat diff_d = obs_d - exp_d,
    z = mean(diff)/(sd(diff)/sqrt(D)). DUNG CAI NAY DE PHAN DINH (bao thu hon),
    vi cac dong cung ngay dung chung tap duoi so dich => KHONG doc lap.
  * suc manh: n can de phat hien chenh 5 diem pp, alpha=0.05 hai phia, power=0.8.

Nguon dinh nghia (doc tu ma nguon, khong doan):
  web/backend/_seed_rules.py : SRC_MB, SRC_MNMT, src_cfgs(), ext_tails(), ext_all()
  web/backend/mined_rule_eval.py : PRIZE_KEY_ALIASES, _get_source_date, hit_any
"""
import sqlite3, sys, os, json, math
from datetime import datetime, timedelta
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DB = os.path.join(ROOT, "data", "lottery_ai.db")
EVID = os.path.join(ROOT, "artifacts", "v11024_audit", "evidence")

# ── copy nguyen van tu _seed_rules.py / mined_rule_eval.py ──
PRIZE_KEYS = {
    'db': ['Giải Đặc Biệt', 'Giải đặc biệt', 'Giải ĐB', 'GDB', 'DB', 'ĐB', 'GĐB'],
    'g1': ['Giải nhất', 'G1'], 'g2': ['Giải nhì', 'G2'],
    'g5': ['Giải năm', 'G5'], 'g6': ['Giải sáu', 'G6'],
    'g7': ['Giải bảy', 'Giải bẩy', 'G7'], 'g8': ['Giải tám', 'G8'],
}
PK_L = {'db': 'GĐB', 'g1': 'G1', 'g2': 'G2', 'g5': 'G5', 'g6': 'G6', 'g7': 'G7', 'g8': 'G8'}
L_PK = {v: k for k, v in PK_L.items()}
SRC_MNMT = ['g8', 'g7', 'db', 'g1', 'g2', 'g5']   # _seed_rules.py:26
SRC_MB   = ['db', 'g6', 'g7', 'g1', 'g2']          # _seed_rules.py:27
WD = {0: 'T2', 1: 'T3', 2: 'T4', 3: 'T5', 4: 'T6', 5: 'T7', 6: 'CN'}

def src_cfgs(tr):                                   # _seed_rules.py:94-97
    if tr == 'MN': return [('MT', -1, SRC_MNMT), ('MN', -1, SRC_MNMT), ('MB', -1, SRC_MB)]
    if tr == 'MT': return [('MN', 0, SRC_MNMT), ('MT', -1, SRC_MNMT), ('MN', -1, SRC_MNMT), ('MB', -1, SRC_MB)]
    return [('MT', 0, SRC_MNMT), ('MN', 0, SRC_MNMT), ('MT', -1, SRC_MNMT), ('MN', -1, SRC_MNMT), ('MB', -1, SRC_MB)]

def ext_tails(pr, pk):                              # _seed_rules.py:57
    for k in PRIZE_KEYS.get(pk, []):
        if k in pr:
            v = pr[k]; t = []
            if isinstance(v, list):
                for x in v:
                    s = str(x).strip()
                    if len(s) >= 2: t.append(s[-2:])
            else:
                s = str(v).strip()
                if len(s) >= 2: t.append(s[-2:])
            return t
    return []

def ext_all(pr):                                    # _seed_rules.py:71
    t = set()
    for k, v in pr.items():
        if isinstance(v, list):
            for x in v:
                s = str(x).strip()
                if len(s) >= 2: t.add(s[-2:])
        else:
            s = str(v).strip()
            if len(s) >= 2: t.add(s[-2:])
    return t

# ── thong ke ──
Z_A = 1.959963985   # alpha .05 hai phia
Z_B = 0.841621234   # power .8
DELTA = 0.05

def p_nen(T, k):
    """Xac suat nen: rut ngau nhien k duoi so trong 100, trung >=1 trong T duoi so dich."""
    if k <= 0: return None
    miss = 1.0
    for i in range(k):
        num = (100 - T - i)
        if num <= 0: return 1.0
        miss *= num / (100.0 - i)
    return 1.0 - miss

def n_can(p0):
    """n de phat hien chenh 5pp, alpha=.05 hai phia, power=.8 (lay nhanh bao thu nhat)."""
    cands = []
    for p1 in (p0 + DELTA, p0 - DELTA):
        if not (0.001 < p1 < 0.999): continue
        n = ((Z_A * math.sqrt(p0 * (1 - p0)) + Z_B * math.sqrt(p1 * (1 - p1))) / DELTA) ** 2
        cands.append(n)
    if not cands: return None
    return int(math.ceil(max(cands)))

def agg(rows):
    """rows = [(date, hit(0/1), p_nen)] -> dict thong ke."""
    n = len(rows)
    if n == 0: return None
    O = sum(r[1] for r in rows)
    E = sum(r[2] for r in rows)
    V = sum(r[2] * (1 - r[2]) for r in rows)
    obs = O / n; exp = E / n
    z_ind = (O - E) / math.sqrt(V) if V > 1e-12 else None
    # cluster theo ngay
    byd = defaultdict(lambda: [0, 0.0, 0])
    for d, h, p in rows:
        byd[d][0] += h; byd[d][1] += p; byd[d][2] += 1
    diffs = [(v[0] / v[2]) - (v[1] / v[2]) for v in byd.values()]
    D = len(diffs)
    z_cl = None
    if D >= 3:
        m = sum(diffs) / D
        var = sum((x - m) ** 2 for x in diffs) / (D - 1)
        se = math.sqrt(var / D)
        z_cl = m / se if se > 1e-12 else None
    return {"n_luot": n, "n_ngay": D, "hit": O, "hit_rate": obs, "nen": exp,
            "chenh_pp": (obs - exp) * 100.0, "z_ind": z_ind, "z_cum": z_cl,
            "n_can_5pp": n_can(exp) if 0 < exp < 1 else None}

def verdict(s):
    """Ngưỡng theo yeu cau: n<20 => THIEU_MAU; |z|>=1.96 moi duoc noi CO/DUOI."""
    if s is None or s["n_luot"] < 20: return "THIEU_MAU"
    z = s["z_cum"] if s["z_cum"] is not None else s["z_ind"]
    if z is None: return "THIEU_MAU"
    if z >= 1.96: return "CO_TIN_HIEU"
    if z <= -1.96: return "DUOI_NEN"
    return "NGANG_NEN"

def fz(x, w=6, d=2):
    return ("%*.*f" % (w, d, x)) if x is not None else ("%*s" % (w, "—"))

# ══ nap du lieu ══
con = sqlite3.connect("file:%s?mode=ro" % DB.replace("\\", "/"), uri=True)
con.row_factory = sqlite3.Row
cur = con.cursor()

data = defaultdict(lambda: defaultdict(list))   # date -> region -> [(station, prizes)]
for r in cur.execute("SELECT date,region,station,prizes_json FROM lottery_results "
                     "WHERE prizes_json IS NOT NULL AND date >= '2025-01-01' ORDER BY date"):
    try:
        data[r["date"]][r["region"]].append((r["station"], json.loads(r["prizes_json"])))
    except Exception:
        pass

tt_cache = {}
def target_tails(d, reg):
    key = (d, reg)
    if key not in tt_cache:
        s = set()
        for st, p in data.get(d, {}).get(reg, []):
            s.update(ext_all(p))
        tt_cache[key] = s
    return tt_cache[key]

# moc phan dinh CHAM NGUOC / DO TIEN
MINE_AT = cur.execute("SELECT MIN(mined_at), MAX(mined_at), rule_version FROM mined_rules").fetchone()
MINE_DATE = str(MINE_AT[0])[:10]
RULE_VER = MINE_AT[2]

out = []
def p(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

p("=" * 100)
p("R4 — DO SUC MANH TUNG NHOM GIAI SOI (prize-source scan)")
p("=" * 100)
p("DB              : %s" % DB)
p("Bo luat hien tai: rule_version=%s · mined_at=%s .. %s" % (RULE_VER, MINE_AT[0], MINE_AT[1]))
p("MOC DO TIEN     : date >= %s  (truoc moc = CHAM NGUOC, vi miner dung lookback 365 ngay)" % MINE_DATE)
p("Whitelist giai nguon (doc tu _seed_rules.py, KHONG doan):")
p("   nguon MB    : %s" % " · ".join(PK_L[k] for k in SRC_MB))
p("   nguon MN/MT : %s" % " · ".join(PK_L[k] for k in SRC_MNMT))
p("Cau hinh nguon hop le (src_cfgs):")
for tr in ("MB", "MT", "MN"):
    p("   dich %s <- %s" % (tr, ", ".join("%s(D%s)" % (sr, off if off else "") for sr, off, _ in src_cfgs(tr))))

# ════════════════════════════════════════════════════════════════
# PHAN 0 — kiem chung: tai lap tails_produced tu ma nguon
# ════════════════════════════════════════════════════════════════
p("")
p("=" * 100)
p("PHAN 0 — KIEM CHUNG TAI LAP (recompute == luu trong DB?)")
p("=" * 100)
eff = list(cur.execute("""SELECT id, rule_id, date, bucket, source_station, source_region, source_offset,
                                 prize_keys, tails_produced, tails_count, hit_any, target_region, weekday
                          FROM mined_rule_effectiveness ORDER BY date"""))
ok = mismatch = nosrc = 0
for r in eff:
    sd = (datetime.strptime(r["date"], "%Y-%m-%d") + timedelta(days=-1 if r["source_offset"] == "D-1" else 0)).strftime("%Y-%m-%d")
    sp = None
    for st, pr in data.get(sd, {}).get(r["source_region"], []):
        if st == r["source_station"]: sp = pr; break
    if sp is None: nosrc += 1; continue
    got = set()
    for lbl in str(r["prize_keys"]).split("+"):
        got.update(ext_tails(sp, L_PK.get(lbl.strip(), lbl.strip().lower())))
    try: stored = set(json.loads(r["tails_produced"] or "[]"))
    except Exception: stored = set()
    if got == stored: ok += 1
    else: mismatch += 1
p("  tong dong effectiveness : %d" % len(eff))
p("  tai lap KHOP            : %d" % ok)
p("  tai lap LECH            : %d" % mismatch)
p("  khong tim thay nguon    : %d" % nosrc)
p("  => %s" % ("DAT — phep do duoi day dung dung logic production."
              if mismatch == 0 else "CANH BAO — co %d dong lech, doc ky truoc khi tin so." % mismatch))

# ════════════════════════════════════════════════════════════════
# PHAN 1 — SCAN A: bam theo LUAT THAT (rule-anchored), bo tung giai
# ════════════════════════════════════════════════════════════════
p("")
p("=" * 100)
p("PHAN 1 — SCAN A: bam theo LUAT THAT trong mined_rule_effectiveness")
p("  moi luot danh gia luat -> bo combo prize_keys ra tung GIAI DON, cham lai tung giai")
p("=" * 100)

A = defaultdict(list)     # (mode, tgt, prize) -> rows
A_wd = defaultdict(list)  # (mode, tgt, wd, prize) -> rows
A_combo = defaultdict(list)
for r in eff:
    d, tgt = r["date"], r["target_region"]
    mode = "DO_TIEN" if d >= MINE_DATE else "CHAM_NGUOC"
    T = len(target_tails(d, tgt))
    if T == 0: continue
    sd = (datetime.strptime(d, "%Y-%m-%d") + timedelta(days=-1 if r["source_offset"] == "D-1" else 0)).strftime("%Y-%m-%d")
    sp = None
    for st, pr in data.get(sd, {}).get(r["source_region"], []):
        if st == r["source_station"]: sp = pr; break
    if sp is None: continue
    tt = target_tails(d, tgt)
    # combo (tai lap hit_any cua he)
    allt = set()
    for lbl in str(r["prize_keys"]).split("+"):
        allt.update(ext_tails(sp, L_PK.get(lbl.strip(), lbl.strip().lower())))
    if allt:
        pb = p_nen(T, len(allt))
        A_combo[(mode, tgt)].append((d, 1 if any(t in tt for t in allt) else 0, pb))
    # tung giai don
    for lbl in str(r["prize_keys"]).split("+"):
        pk = L_PK.get(lbl.strip(), lbl.strip().lower())
        ts = set(ext_tails(sp, pk))
        if not ts: continue
        pb = p_nen(T, len(ts))
        hit = 1 if any(t in tt for t in ts) else 0
        A[(mode, tgt, PK_L[pk])].append((d, hit, pb))
        A_wd[(mode, tgt, WD[r["weekday"]], PK_L[pk])].append((d, hit, pb))

HDR = ("  %-6s %-4s %-5s | %5s %5s | %6s %6s %7s | %7s %7s | %8s | %s"
       % ("giai", "dich", "n_ngay", "n", "hit", "hr%", "nen%", "chenh", "z_cum", "z_ind", "n_can5pp", "PHAN DINH"))

def dump(bucketmap, keyfmt, title):
    p("")
    p(title)
    p("  " + "-" * 112)
    p(HDR)
    p("  " + "-" * 112)
    rows = []
    for k, v in bucketmap.items():
        s = agg(v)
        if s: rows.append((k, s, verdict(s)))
    rows.sort(key=lambda x: (-(x[1]["z_cum"] if x[1]["z_cum"] is not None else -99), -x[1]["n_luot"]))
    for k, s, vd in rows:
        p("  %-6s %-4s %5d | %5d %5d | %6.1f %6.1f %+7.1f | %s %s | %8s | %s"
          % (keyfmt(k), k[1] if len(k) > 1 else "", s["n_ngay"], s["n_luot"], s["hit"],
             s["hit_rate"] * 100, s["nen"] * 100, s["chenh_pp"],
             fz(s["z_cum"], 7), fz(s["z_ind"], 7),
             s["n_can_5pp"] if s["n_can_5pp"] else "—", vd))
    return rows

p("")
p(">>> A0. TAI LAP hit_any CUA CA COMBO (de thay nen cao co nao)")
p("  " + "-" * 112)
p("  %-12s %-10s | %5s %5s | %6s %6s %7s | %7s | %8s | %s"
  % ("che do", "dich", "n", "hit", "hr%", "nen%", "chenh", "z_cum", "n_can5pp", "PHAN DINH"))
p("  " + "-" * 112)
for k in sorted(A_combo.keys()):
    s = agg(A_combo[k])
    if not s: continue
    p("  %-12s %-10s | %5d %5d | %6.1f %6.1f %+7.1f | %s | %8s | %s"
      % (k[0], k[1], s["n_luot"], s["hit"], s["hit_rate"] * 100, s["nen"] * 100,
         s["chenh_pp"], fz(s["z_cum"], 7), s["n_can_5pp"] or "—", verdict(s)))

for mode in ("CHAM_NGUOC", "DO_TIEN"):
    sub = {k: v for k, v in A.items() if k[0] == mode}
    dump(sub, lambda k: k[2], ">>> A1.%s — GIAI NGUON x MIEN DICH  [%s]" % (mode, mode))

# ════════════════════════════════════════════════════════════════
# PHAN 2 — SCAN B: quet TOAN VU TRU (khong chon loc => khong thien lech)
# ════════════════════════════════════════════════════════════════
p("")
p("=" * 100)
p("PHAN 2 — SCAN B: QUET TOAN VU TRU (moi ngay x moi dai nguon hop le x moi giai)")
p("  KHONG qua bo chon cua miner => KHONG co thien lech chon mau.")
p("  Day la phep do that su tra loi 'giai nao mang tin hieu'.")
p("=" * 100)

W_START, W_END = "2025-08-08", "2026-08-06"   # 365 ngay
B = defaultdict(list)          # (tgt, prize) -> rows
B_wd = defaultdict(list)       # (tgt, wd, prize) -> rows
B_slot = defaultdict(list)     # (tgt, srcreg+off, prize) -> rows
B_mode = defaultdict(list)     # (mode, tgt, prize) -> rows
alldates = sorted(d for d in data.keys() if W_START <= d <= W_END)
for d in alldates:
    dt = datetime.strptime(d, "%Y-%m-%d")
    wd = WD[dt.weekday()]
    mode = "DO_TIEN" if d >= MINE_DATE else "CHAM_NGUOC"
    for tr in ("MB", "MT", "MN"):
        tt = target_tails(d, tr)
        T = len(tt)
        if T == 0: continue
        for sr, off, pks in src_cfgs(tr):
            sd = (dt + timedelta(days=off)).strftime("%Y-%m-%d")
            slot = "%s(D%s)" % (sr, off if off else "")
            for st, pr in data.get(sd, {}).get(sr, []):
                for pk in pks:
                    ts = set(ext_tails(pr, pk))
                    if not ts: continue
                    pb = p_nen(T, len(ts))
                    hit = 1 if any(t in tt for t in ts) else 0
                    rec = (d, hit, pb)
                    B[(tr, PK_L[pk])].append(rec)
                    B_wd[(tr, wd, PK_L[pk])].append(rec)
                    B_slot[(tr, slot, PK_L[pk])].append(rec)
                    B_mode[(mode, tr, PK_L[pk])].append(rec)

p("  Cua so quet: %s .. %s  (%d ngay co du lieu)" % (W_START, W_END, len(alldates)))
p("")
p(">>> B1. GIAI NGUON x MIEN DICH — toan cua so 365 ngay")
p("  " + "-" * 112)
p(HDR)
p("  " + "-" * 112)
b1 = []
for k, v in B.items():
    s = agg(v)
    if s: b1.append((k, s, verdict(s)))
b1.sort(key=lambda x: (x[0][0], -(x[1]["z_cum"] if x[1]["z_cum"] is not None else -99)))
for k, s, vd in b1:
    p("  %-6s %-4s %5d | %5d %5d | %6.1f %6.1f %+7.1f | %s %s | %8s | %s"
      % (k[1], k[0], s["n_ngay"], s["n_luot"], s["hit"], s["hit_rate"] * 100, s["nen"] * 100,
         s["chenh_pp"], fz(s["z_cum"], 7), fz(s["z_ind"], 7), s["n_can_5pp"] or "—", vd))

p("")
p(">>> B2. TACH CHAM NGUOC vs DO TIEN tren cung phep quet vu tru")
p("  " + "-" * 112)
p("  %-6s %-4s %-11s | %5s %5s | %6s %6s %7s | %7s | %8s | %s"
  % ("giai", "dich", "che do", "n", "hit", "hr%", "nen%", "chenh", "z_cum", "n_can5pp", "PHAN DINH"))
p("  " + "-" * 112)
for k in sorted(B_mode.keys(), key=lambda x: (x[1], x[2], x[0])):
    s = agg(B_mode[k])
    if not s: continue
    p("  %-6s %-4s %-11s | %5d %5d | %6.1f %6.1f %+7.1f | %s | %8s | %s"
      % (k[2], k[1], k[0], s["n_luot"], s["hit"], s["hit_rate"] * 100, s["nen"] * 100,
         s["chenh_pp"], fz(s["z_cum"], 7), s["n_can_5pp"] or "—", verdict(s)))

p("")
p(">>> B3. BUCKET (mien dich x THU) x GIAI NGUON — toan cua so")
p("  " + "-" * 112)
p("  %-6s %-4s %-3s | %5s %5s | %6s %6s %7s | %7s | %8s | %s"
  % ("giai", "dich", "thu", "n", "hit", "hr%", "nen%", "chenh", "z_cum", "n_can5pp", "PHAN DINH"))
p("  " + "-" * 112)
b3 = []
for k, v in B_wd.items():
    s = agg(v)
    if s: b3.append((k, s, verdict(s)))
b3.sort(key=lambda x: -(x[1]["z_cum"] if x[1]["z_cum"] is not None else -99))
for k, s, vd in b3:
    p("  %-6s %-4s %-3s | %5d %5d | %6.1f %6.1f %+7.1f | %s | %8s | %s"
      % (k[2], k[0], k[1], s["n_luot"], s["hit"], s["hit_rate"] * 100, s["nen"] * 100,
         s["chenh_pp"], fz(s["z_cum"], 7), s["n_can_5pp"] or "—", vd))

p("")
p(">>> B4. GIAI NGUON x KHE NGUON(mien+offset) x MIEN DICH — toan cua so")
p("  " + "-" * 112)
p("  %-6s %-4s %-9s | %5s %5s | %6s %6s %7s | %7s | %8s | %s"
  % ("giai", "dich", "khe", "n", "hit", "hr%", "nen%", "chenh", "z_cum", "n_can5pp", "PHAN DINH"))
p("  " + "-" * 112)
b4 = []
for k, v in B_slot.items():
    s = agg(v)
    if s: b4.append((k, s, verdict(s)))
b4.sort(key=lambda x: -(x[1]["z_cum"] if x[1]["z_cum"] is not None else -99))
for k, s, vd in b4:
    p("  %-6s %-4s %-9s | %5d %5d | %6.1f %6.1f %+7.1f | %s | %8s | %s"
      % (k[2], k[0], k[1], s["n_luot"], s["hit"], s["hit_rate"] * 100, s["nen"] * 100,
         s["chenh_pp"], fz(s["z_cum"], 7), s["n_can_5pp"] or "—", vd))

# ── TONG KET ──
p("")
p("=" * 100)
p("TONG KET — DEM PHAN DINH")
p("=" * 100)
def dem(rows, ten):
    c = defaultdict(int)
    for _, _, vd in rows: c[vd] += 1
    p("  %-42s %s" % (ten, dict(c)))
dem(b1, "B1 giai x mien (365 ngay, khong thien lech)")
dem(b3, "B3 giai x mien x thu")
dem(b4, "B4 giai x mien x khe nguon")

p("")
p("  SUC MANH THUC TE — B1:")
for k, s, vd in b1:
    thieu = (s["n_can_5pp"] - s["n_luot"]) if s["n_can_5pp"] else None
    p("     %-4s %-6s n=%-5d n_can=%-6s %s"
      % (k[0], k[1], s["n_luot"], s["n_can_5pp"] or "—",
         "DU SUC MANH" if (s["n_can_5pp"] and s["n_luot"] >= s["n_can_5pp"]) else "THIEU %s luot" % thieu))

con.close()

# ── ghi bang chung ──
def safe_write(path, text):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)
    with open(path, encoding="utf-8") as f:
        got = f.read()
    assert len(got) == len(text), "GHI LECH: %d != %d" % (len(got), len(text))
    return len(text)

txt = "\n".join(out) + "\n"
n1 = safe_write(os.path.join(EVID, "R4_prize_source_scan.txt"), txt)

def pack(rows, names):
    o = []
    for k, s, vd in rows:
        d = dict(zip(names, k)); d.update(s); d["phan_dinh"] = vd
        o.append(d)
    return o

js = {
    "ma": "R4",
    "db": DB,
    "rule_version": RULE_VER,
    "moc_do_tien": MINE_DATE,
    "cua_so_quet_B": [W_START, W_END, len(alldates)],
    "whitelist_nguon": {"MB": [PK_L[k] for k in SRC_MB], "MN_MT": [PK_L[k] for k in SRC_MNMT]},
    "kiem_chung_tai_lap": {"tong": len(eff), "khop": ok, "lech": mismatch, "khong_co_nguon": nosrc},
    "A_combo": [dict(che_do=k[0], dich=k[1], **(agg(v) or {})) for k, v in sorted(A_combo.items())],
    "A_giai": [dict(che_do=k[0], dich=k[1], giai=k[2], phan_dinh=verdict(agg(v)), **(agg(v) or {}))
               for k, v in sorted(A.items()) if agg(v)],
    "B1_giai_x_mien": pack(b1, ("dich", "giai")),
    "B2_theo_che_do": [dict(che_do=k[0], dich=k[1], giai=k[2], phan_dinh=verdict(agg(v)), **(agg(v) or {}))
                       for k, v in sorted(B_mode.items()) if agg(v)],
    "B3_bucket_thu": pack(b3, ("dich", "thu", "giai")),
    "B4_khe_nguon": pack(b4, ("dich", "khe", "giai")),
}
n2 = safe_write(os.path.join(EVID, "R4_scan.json"), json.dumps(js, ensure_ascii=False, indent=1))
print("\n[OK] R4_prize_source_scan.txt = %d chars ; R4_scan.json = %d chars" % (n1, n2))
