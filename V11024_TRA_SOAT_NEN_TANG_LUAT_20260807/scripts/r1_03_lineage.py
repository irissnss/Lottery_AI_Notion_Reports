"""R1 buoc 3 — TAI LAP CHUOI DAO LUAT + KIEM TEMPORAL + BANG LINEAGE 105 LUAT.

READ-ONLY tuyet doi: sqlite mo bang mode=ro. Khong ghi DB.
Xuat: evidence/R1_lineage.txt + evidence/R1_lineage.json
"""
import io, json, os, sqlite3, sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DB = os.path.join(ROOT, "data", "lottery_ai.db")
GRID = os.path.join(ROOT, "artifacts", "v105_55_safe_quality",
                    "v10636_mb_db_d1_to_mnmt_d_audit", "machine_readable")
PUB = os.path.join(ROOT, "artifacts", "public_repo",
                   "V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE", "machine_readable")
EV = os.path.join(ROOT, "artifacts", "v11024_audit", "evidence")
OUT_TXT = os.path.join(EV, "R1_lineage.txt")
OUT_JSON = os.path.join(EV, "R1_lineage.json")

buf = []
def p(*a):
    s = " ".join(str(x) for x in a)
    print(s); buf.append(s)

def jload(path):
    if not os.path.exists(path):
        return None
    with io.open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def safe_write(path, text):
    tmp = path + ".tmp"
    with io.open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)
    with io.open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert len(back) == len(text), "GHI HONG %s (%d != %d)" % (path, len(back), len(text))
    return len(back)

RESULT = {"ma": "R1", "do_luc": None, "mat_xich": [], "temporal": {}, "bang_lineage": []}

from datetime import datetime
RESULT["do_luc"] = datetime.now().isoformat(timespec="seconds")

# =====================================================================
# PHAN A — DEM THAT TREN DB
# =====================================================================
p("=" * 78)
p("R1 — KIEM CHUNG PIPELINE DAO LUAT (lineage 105 luat)")
p("Do luc:", RESULT["do_luc"], "| DB:", DB, "| size:", os.path.getsize(DB))
p("=" * 78)

con = sqlite3.connect("file:%s?mode=ro" % DB.replace("\\", "/"), uri=True)
con.row_factory = sqlite3.Row
cur = con.cursor()
def one(sql, args=()):
    return cur.execute(sql, args).fetchone()[0]

p("\n" + "-" * 78)
p("PHAN A — DEM THAT: mined_rules is_active=1")
p("-" * 78)
n_total = one("select count(*) from mined_rules")
n_active = one("select count(*) from mined_rules where is_active=1")
n_status_active = one("select count(*) from mined_rules where activation_status='active'")
n_shadow = one("select count(*) from mined_rules where activation_status='shadow'")
p("  mined_rules tong dong                : %d" % n_total)
p("  is_active = 1                        : %d   <== SO THAT" % n_active)
p("  is_active = 0                        : %d" % one("select count(*) from mined_rules where is_active=0"))
p("  activation_status = 'active'         : %d" % n_status_active)
p("  activation_status = 'shadow'         : %d" % n_shadow)
p("  KET LUAN: tai lieu ghi 105 -> DB dem duoc %d. %s"
  % (n_active, "KHOP" if n_active == 105 else "LECH"))
RESULT["so_luat_is_active_1"] = n_active
RESULT["so_luat_tong"] = n_total

r = cur.execute("select min(mined_at), max(mined_at), count(distinct source_run_id), "
                "min(rule_version), max(rule_version) from mined_rules").fetchone()
p("\n  mined_at                             : %s .. %s" % (r[0], r[1]))
p("  so source_run_id phan biet           : %d" % r[2])
p("  rule_version                         : %s" % r[3])
run_ids = [x[0] for x in cur.execute("select distinct source_run_id from mined_rules")]
p("  source_run_id                        : %s" % run_ids)
RESULT["mined_at_min"] = r[0]; RESULT["mined_at_max"] = r[1]
RESULT["rule_version"] = r[3]; RESULT["source_run_id"] = run_ids

# cau truc bucket
p("\n  cau truc bucket (21 bucket x top-5):")
bk = cur.execute("select target_region, target_weekday, count(*) n from mined_rules group by 1,2").fetchall()
p("     so bucket phan biet = %d ; moi bucket n = %s"
  % (len(bk), sorted(set(x["n"] for x in bk))))
RESULT["so_bucket"] = len(bk)
RESULT["n_moi_bucket"] = sorted(set(x["n"] for x in bk))

# lich su mining_log
p("\n  mining_log (nhip dao lai):")
try:
    rows = cur.execute("select run_date, n_buckets, n_rules_total, n_ready_strong, n_ready_caution, "
                       "coalesce(rule_version,''), coalesce(schedule_slot,''), status "
                       "from mining_log order by id desc limit 15").fetchall()
    for x in rows:
        p("     %s  buckets=%s rules=%s strong=%s caution=%s ver=%s slot=%s %s"
          % (x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]))
    p("     tong dong mining_log = %d" % one("select count(*) from mining_log"))
    RESULT["mining_log_rows"] = one("select count(*) from mining_log")
except Exception as e:
    p("     LOI doc mining_log: %s" % e)

# =====================================================================
# PHAN B — TAI LAP TUNG MAT XICH
# =====================================================================
p("\n" + "-" * 78)
p("PHAN B — TAI LAP CHUOI: 2387 + 784 + 1260 -> 3696 -> 268 -> 232 -> 28 -> 105")
p("-" * 78)

def mx(ten, tai_lieu, do_duoc, nguon, ghi_chu=""):
    khop = "KHOP" if (do_duoc is not None and str(do_duoc) == str(tai_lieu)) else \
           ("KHONG TAI LAP DUOC" if do_duoc is None else "LECH")
    p("\n  [%s] %s" % (khop, ten))
    p("      tai lieu ghi : %s" % tai_lieu)
    p("      do lai duoc  : %s" % (do_duoc if do_duoc is not None else "(khong tai lap duoc)"))
    p("      nguon do     : %s" % nguon)
    if ghi_chu:
        p("      ghi chu      : %s" % ghi_chu)
    RESULT["mat_xich"].append({"ten": ten, "tai_lieu": tai_lieu, "do_duoc": do_duoc,
                               "trang_thai": khop, "nguon": nguon, "ghi_chu": ghi_chu})

cross = jload(os.path.join(GRID, "V10636_CROSS_FULL_GRID.json"))
dig = jload(os.path.join(GRID, "V10636_DIG_FULL_GRID.json"))
lags = jload(os.path.join(GRID, "V10636_LAGS_FULL_GRID.json"))
ext = jload(os.path.join(GRID, "V10636_EXT_FULL_GRID.json"))

# --- mat xich 1: CROSS 2387 ---
if cross:
    n_cross = len(cross["all_combinations"])
    mx("V10636-CROSS cells", 2387, n_cross,
       "len(all_combinations) trong V10636_CROSS_FULL_GRID.json",
       "header total_combinations=%s" % cross.get("total_combinations"))
else:
    mx("V10636-CROSS cells", 2387, None, "V10636_CROSS_FULL_GRID.json khong ton tai")

# --- mat xich 2: DIG 784 ---
if dig:
    n_dig = len(dig["all_combinations"])
    mx("V10636-DIG cells", 784, n_dig,
       "len(all_combinations) trong V10636_DIG_FULL_GRID.json",
       "header total_combinations=%s ; count_bh_pass=%s (KHONG cell nao BH-pass)"
       % (dig.get("total_combinations"), dig.get("count_bh_pass")))
else:
    mx("V10636-DIG cells", 784, None, "V10636_DIG_FULL_GRID.json khong ton tai")

# --- mat xich 3: LAGS 1260 ---
n_lags_flat = None
lags_flat = []
if lags:
    for cell in lags["all_combinations"]:
        for wd, st in (cell.get("per_weekday") or {}).items():
            lags_flat.append({"source_prize": cell["source_prize"], "lag": cell["lag"],
                              "transform": cell["transform"], "target_weekday": wd,
                              "p_value": st.get("p_value"), "lift_pp": st.get("lift_pp")})
    n_lags_flat = len(lags_flat)
    mx("V10636-LAGS cells (flat)", 1260, n_lags_flat,
       "banh phang all_combinations(180 grid) x per_weekday(7) trong V10636_LAGS_FULL_GRID.json",
       "header total_grid_combinations=%s total_flat_cells=%s"
       % (lags.get("total_grid_combinations"), lags.get("total_flat_cells")))
else:
    mx("V10636-LAGS cells (flat)", 1260, None, "V10636_LAGS_FULL_GRID.json khong ton tai")

# --- mat xich 4: dedup 3696 ---
p("\n  >>> Thu tai lap con so 'dedup 3.696':")
tong_tho = (len(cross["all_combinations"]) if cross else 0) + \
           (len(dig["all_combinations"]) if dig else 0) + (n_lags_flat or 0)
p("      cong tho 3 nguon           : %d + %d + %d = %d"
  % (len(cross["all_combinations"]) if cross else 0,
     len(dig["all_combinations"]) if dig else 0, n_lags_flat or 0, tong_tho))
# thu dedup theo khoa tu nhien cua tung nguon
keys = set()
if cross:
    for c in cross["all_combinations"]:
        keys.add(("CROSS", c["source_region"], c["source_prize"], c["source_lag"],
                  c["target_region"], c["target_weekday"]))
if dig:
    for c in dig["all_combinations"]:
        keys.add(("MBSELF", "MB", c["source_prize"], "D-1", "MB", c["target_weekday"], c["transform"]))
for c in lags_flat:
    keys.add(("MBSELF", "MB", c["source_prize"], c["lag"], "MB", c["target_weekday"], c["transform"]))
p("      dedup theo khoa tu nhien   : %d" % len(keys))
# dedup bo transform (chi source/lag/target)
keys2 = set()
if cross:
    for c in cross["all_combinations"]:
        keys2.add((c["source_region"], c["source_prize"], c["source_lag"], c["target_region"], c["target_weekday"]))
if dig:
    for c in dig["all_combinations"]:
        keys2.add(("MB", c["source_prize"], "D-1", "MB", c["target_weekday"]))
for c in lags_flat:
    keys2.add(("MB", c["source_prize"], c["lag"], "MB", c["target_weekday"]))
p("      dedup bo 'transform'       : %d" % len(keys2))
cand = {"cong_tho": tong_tho, "dedup_khoa_tu_nhien": len(keys), "dedup_bo_transform": len(keys2)}
match = [k for k, v in cand.items() if v == 3696]
mx("Tong dedup", 3696, (3696 if match else None),
   "cong/dedup tu 3 tep FULL_GRID",
   "khong cong thuc nao ra 3696. Da thu: %s. Tep sinh ra so 3696 (script V10667) KHONG con trong kho."
   % json.dumps(cand) if not match else "cong thuc khop: %s" % match)
RESULT["dedup_thu"] = cand

# --- mat xich 5: 268 BH-pass ---
if cross:
    bh = [c for c in cross["all_combinations"] if c.get("bh_pass")]
    mx("BH-pass (FDR a=0.05) tu CROSS", 268, len(bh),
       "dem cell co bh_pass=true trong V10636_CROSS_FULL_GRID.all_combinations",
       "header count_bh_pass_05=%s ; DIG count_bh_pass=%s ; LAGS khong co truong bh_pass"
       % (cross.get("count_bh_pass_05"), dig.get("count_bh_pass") if dig else "?"))
else:
    bh = []
    mx("BH-pass tu CROSS", 268, None, "thieu tep CROSS")

# --- mat xich 6: temporal patch V10668 -> 232 ---
DRAW_ORDER = {"MN": 1, "MT": 2, "MB": 3}
def vi_pham(src_region, tgt_region, lag_days):
    """lag_days = 0 (cung ngay) va nguon xo SAU dich  ->  VI PHAM."""
    if lag_days is None:
        return None
    if int(lag_days) != 0:
        return False
    return DRAW_ORDER.get(src_region, 0) > DRAW_ORDER.get(tgt_region, 0)

if cross:
    vi_all = [c for c in cross["all_combinations"]
              if vi_pham(c["source_region"], c["target_region"], c.get("lag_days"))]
    vi_bh = [c for c in vi_all if c.get("bh_pass")]
    hop_le_bh = [c for c in bh if not vi_pham(c["source_region"], c["target_region"], c.get("lag_days"))]
    mx("Cell vi pham temporal trong CROSS", 266, len(vi_all),
       "tinh lai bang luat: lag_days==0 va DRAW_ORDER[src]>DRAW_ORDER[tgt], DRAW_ORDER=MN1<MT2<MB3")
    mx("BH-pass vi pham temporal", 36, len(vi_bh),
       "loc bh_pass=true trong tap vi pham vua tinh")
    mx("BH-pass hop le sau va V10668", 232, len(hop_le_bh),
       "268 BH-pass tru cac cell vi pham temporal")
    # doi chieu voi co temporal_violation da ghi san trong tep
    co_co = sum(1 for c in cross["all_combinations"] if c.get("temporal_violation"))
    p("\n      doi chieu co 'temporal_violation' da ghi san trong tep : %d "
      "(tinh lai duoc %d -> %s)" % (co_co, len(vi_all), "KHOP" if co_co == len(vi_all) else "LECH"))
    RESULT["cross_co_da_ghi_san"] = co_co
    # phan ra theo huong
    br = Counter("%s(D)->%s(D)" % (c["source_region"], c["target_region"]) for c in vi_all)
    p("      phan ra theo huong: %s" % dict(br))
    RESULT["vi_pham_theo_huong"] = dict(br)
else:
    vi_all = vi_bh = hop_le_bh = []

# --- mat xich 7: 28 rule forward audit ---
reg = jload(os.path.join(PUB, "V10668_FORWARD_AUDIT_REGISTRY_FIXED.json"))
if reg:
    n_reg = len(reg["rules"])
    mx("Forward audit registry FIXED", 28, n_reg,
       "len(rules) trong V10668_FORWARD_AUDIT_REGISTRY_FIXED.json",
       "header total_rules_registered=%s original_rules_count=%s invalid_dropped_count=%s"
       % (reg.get("total_rules_registered"), reg.get("original_rules_count"),
          reg.get("invalid_dropped_count")))
    # kiem temporal 28 rule nay
    vi_reg = [r for r in reg["rules"]
              if vi_pham(r["source_region"], r["target_region"], r.get("lag_days"))]
    p("\n      kiem temporal 28 rule: vi pham = %d" % len(vi_reg))
    # doi chieu direction_distribution
    dd_ghi = reg.get("direction_distribution") or {}
    dd_that = Counter("%s->%s" % (r["source_region"], r["target_region"]) for r in reg["rules"])
    p("      direction_distribution GHI TRONG TEP : %s (tong %d)"
      % (dict(dd_ghi), sum(dd_ghi.values())))
    p("      direction_distribution DEM LAI THAT  : %s (tong %d)"
      % (dict(dd_that), sum(dd_that.values())))
    p("      -> %s" % ("KHOP" if dict(dd_ghi) == dict(dd_that) else
                       "LECH: metadata direction_distribution CHUA duoc cap nhat sau va temporal"))
    RESULT["registry_direction_ghi"] = dict(dd_ghi)
    RESULT["registry_direction_that"] = dict(dd_that)
    RESULT["registry_temporal_vi_pham"] = len(vi_reg)
    # trang thai
    st = Counter(r.get("status") for r in reg["rules"])
    le = Counter(bool(r.get("live_eligible")) for r in reg["rules"])
    p("      status 28 rule    : %s" % dict(st))
    p("      live_eligible     : %s" % {str(k): v for k, v in le.items()})
    RESULT["registry_status"] = {str(k): v for k, v in st.items()}
    RESULT["registry_live_eligible"] = {str(k): v for k, v in le.items()}
    tgt_reg = Counter(r["target_region"] for r in reg["rules"])
    p("      target_region     : %s  (KHONG co rule target MB)" % dict(tgt_reg))
    RESULT["registry_target_region"] = dict(tgt_reg)
else:
    mx("Forward audit registry FIXED", 28, None, "tep registry khong ton tai")

# --- mat xich 8: 28 -> 105 ??? ---
p("\n  >>> MAT XICH CUOI: '28 rule forward audit -> 105 luat production'")
p("      Kiem xem 105 luat trong mined_rules co dan xuat tu 28 rule kia khong.")
# so khop theo (target_region, target_weekday, source_region, source_offset, prize)
prod = cur.execute(
    "select id,target_region,target_weekday,source_region,source_offset,source_station,"
    "prize_keys,production_tier,window_verdict,hr_12w,hr_16w,hit_rate_365,lift_365,n_365,"
    "score,composite_score,cumulative_rank_score,sample_quality,prediction_use,mined_at,"
    "rule_version,source_run_id,activation_status,is_active,owner_approved_at,source_weekday,"
    "source_station_slot,split_policy "
    "from mined_rules order by target_region, target_weekday, "
    "cumulative_rank_score desc").fetchall()
WDN = {0: "T2", 1: "T3", 2: "T4", 3: "T5", 4: "T6", 5: "T7", 6: "CN"}
prod_keys = set()
for r in prod:
    off = 0 if str(r["source_offset"]).upper() in ("D", "D0", "0") else -1
    prod_keys.add((r["target_region"], WDN.get(r["target_weekday"]), r["source_region"], off))
reg_keys = set()
if reg:
    for r in reg["rules"]:
        reg_keys.add((r["target_region"], r["target_weekday"], r["source_region"], -int(r["lag_days"])))
p("      khoa (tgt_region, tgt_wd, src_region, offset) — production : %d khoa" % len(prod_keys))
p("      khoa tuong tu — registry 28 rule                            : %d khoa" % len(reg_keys))
p("      giao nhau                                                   : %d khoa"
  % len(prod_keys & reg_keys))
p("      Ma luat: registry dung rule_id dang 'V10668_FA01_...' (chuoi);")
p("               mined_rules dung id INTEGER tu AUTOINCREMENT. KHONG co cot nao")
p("               trong mined_rules tro nguoc ve rule_id cua registry.")
cols = [d[1] for d in cur.execute("pragma table_info(mined_rules)")]
p("      cot cua mined_rules: %s" % cols)
p("      -> KHONG co cot lineage/parent/source_report/bh_rank/p_value.")
RESULT["mined_rules_cols"] = cols
RESULT["giao_khoa_prod_vs_registry"] = len(prod_keys & reg_keys)

mx("28 rule forward audit -> 105 luat production", "105", None,
   "khong co bang/cot nao noi 2 tap",
   "KHONG TAI LAP DUOC. Ly do: _seed_rules.main() chay 'DELETE FROM mined_rules' roi "
   "dao lai tu dau tu lottery_results (21 bucket x top-5 = 105). 105 luat hien tai co "
   "rule_version=%s, mined_at=%s, source_run_id=%s — tuc la san pham cua mot lan dao lai "
   "ngay 03/08/2026, KHONG phai hau due cua chuoi V10636 (02/06/2026)."
   % (RESULT.get("rule_version"), RESULT.get("mined_at_min"), RESULT.get("source_run_id")))

# =====================================================================
# PHAN C — KIEM TEMPORAL CAUSALITY TREN TOAN BO 105 LUAT PRODUCTION
# =====================================================================
p("\n" + "-" * 78)
p("PHAN C — TEMPORAL CAUSALITY TREN 105 LUAT PRODUCTION")
p("  Luat: thu tu xo MN(1) -> MT(2) -> MB(3). Vi pham khi offset=D (cung ngay)")
p("        va DRAW_ORDER[source] > DRAW_ORDER[target]. Offset duong (tuong lai) cung vi pham.")
p("-" * 78)

def parse_off(v):
    s = str(v or "D").strip().upper()
    if s in ("D", "D0", "0"):
        return 0
    if s.startswith("D"):
        try:
            return int(s[1:])
        except Exception:
            return None
    try:
        return int(s)
    except Exception:
        return None

vi_pham_prod = []
off_tuong_lai = []
sai_source_weekday = []
for r in prod:
    off = parse_off(r["source_offset"])
    if off is None:
        continue
    if off > 0:
        off_tuong_lai.append(r)
    if off == 0 and DRAW_ORDER.get(r["source_region"], 0) > DRAW_ORDER.get(r["target_region"], 0):
        vi_pham_prod.append(r)
    # kiem source_weekday = (target_weekday + off) % 7
    if r["source_weekday"] is not None:
        expect = (int(r["target_weekday"]) + off) % 7
        if int(r["source_weekday"]) != expect:
            sai_source_weekday.append((r["id"], r["target_weekday"], off, r["source_weekday"], expect))

p("\n  so luat kiem            : %d" % len(prod))
p("  VI PHAM temporal        : %d" % len(vi_pham_prod))
p("  offset duong (tuong lai): %d" % len(off_tuong_lai))
p("  source_weekday sai cong thuc (tw+off)%%7 : %d" % len(sai_source_weekday))
if sai_source_weekday:
    for x in sai_source_weekday[:20]:
        p("     rule#%s tw=%s off=%s source_weekday=%s (dung phai %s)" % x)
if vi_pham_prod:
    for r in vi_pham_prod:
        p("     VI PHAM rule#%s %s/wd%s <- %s(%s) %s" %
          (r["id"], r["target_region"], r["target_weekday"], r["source_region"],
           r["source_offset"], r["source_station"]))
p("\n  phan ra (target <- source, offset):")
comb = Counter((r["target_region"], r["source_region"], r["source_offset"]) for r in prod)
for (t, s, o), n in sorted(comb.items()):
    off = parse_off(o)
    v = "VI PHAM" if (off == 0 and DRAW_ORDER.get(s, 0) > DRAW_ORDER.get(t, 0)) else "hop le"
    p("     %-3s <- %-3s %-5s  n=%-3d  %s" % (t, s, o, n, v))
RESULT["temporal"] = {
    "so_luat_kiem": len(prod),
    "vi_pham": len(vi_pham_prod),
    "offset_tuong_lai": len(off_tuong_lai),
    "sai_source_weekday": len(sai_source_weekday),
    "chi_tiet_sai_source_weekday": sai_source_weekday[:50],
    "phan_ra": {"%s<-%s(%s)" % (t, s, o): n for (t, s, o), n in sorted(comb.items())},
}

# kiem them: source_station co that thuoc source_region khong (theo lottery_results)
p("\n  Kiem cheo: source_station co that thuoc source_region khong (doi chieu lottery_results)?")
st_region = defaultdict(set)
for x in cur.execute("select distinct station, region from lottery_results where station is not null"):
    st_region[x[0]].add(x[1])
lech_station = []
for r in prod:
    regs = st_region.get(r["source_station"])
    if regs is None:
        lech_station.append((r["id"], r["source_station"], r["source_region"], "KHONG CO TRONG lottery_results"))
    elif r["source_region"] not in regs:
        lech_station.append((r["id"], r["source_station"], r["source_region"], "that su thuoc %s" % sorted(regs)))
p("     so luat co source_station lech mien: %d" % len(lech_station))
for x in lech_station[:20]:
    p("       rule#%s station=%s khai src_region=%s -> %s" % x)
RESULT["temporal"]["station_lech_mien"] = len(lech_station)
RESULT["temporal"]["chi_tiet_station_lech"] = [list(x) for x in lech_station[:50]]

# =====================================================================
# PHAN D — BANG LINEAGE TUNG LUAT (DU 105 DONG)
# =====================================================================
p("\n" + "-" * 78)
p("PHAN D — BANG LINEAGE DAY DU %d LUAT" % len(prod))
p("-" * 78)

# so luot cham trong mined_rule_effectiveness cho tung rule_id
mre = {}
for x in cur.execute(
        "select rule_id, count(*) n, sum(hit_any) h, min(date) d1, max(date) d2 "
        "from mined_rule_effectiveness group by rule_id"):
    mre[x[0]] = {"n": x[1], "hit": x[2] or 0, "d1": x[3], "d2": x[4]}

hdr = ("%-5s | %-3s %-3s | %-26s | %-22s | %-18s | %-17s | %6s %6s | %-4s %5s %6s | %s"
       % ("rule", "mie", "thu", "nguon (dai · giai · offset)", "prize_keys",
          "production_tier", "window_verdict", "hr_12w", "hr_16w",
          "MRE", "luot", "trung%", "temporal"))
p("\n" + hdr)
p("-" * len(hdr))

so_co_mre = 0
tong_luot = 0
for r in prod:
    off = parse_off(r["source_offset"])
    tv = "HOP LE"
    if off is None:
        tv = "OFFSET LA?"
    elif off > 0:
        tv = "VI PHAM(tuong lai)"
    elif off == 0 and DRAW_ORDER.get(r["source_region"], 0) > DRAW_ORDER.get(r["target_region"], 0):
        tv = "VI PHAM"
    m = mre.get(r["id"])
    if m:
        so_co_mre += 1
        tong_luot += m["n"]
        mre_s, luot, tr = "CO", m["n"], (100.0 * m["hit"] / m["n"] if m["n"] else 0.0)
    else:
        mre_s, luot, tr = "KHONG", 0, 0.0
    nguon = "%s(%s) %s" % (r["source_region"], r["source_offset"], r["source_station"])
    line = ("%-5s | %-3s %-3s | %-26s | %-22s | %-18s | %-17s | %5.1f%% %5.1f%% | %-4s %5d %5.1f%% | %s"
            % (r["id"], r["target_region"], WDN.get(r["target_weekday"]), nguon[:26],
               (r["prize_keys"] or "")[:22], (r["production_tier"] or "")[:18],
               (r["window_verdict"] or "")[:17], 100.0 * (r["hr_12w"] or 0),
               100.0 * (r["hr_16w"] or 0), mre_s, luot, tr, tv))
    p(line)
    RESULT["bang_lineage"].append({
        "rule_id": r["id"],
        "bucket_mien": r["target_region"],
        "bucket_thu": WDN.get(r["target_weekday"]),
        "target_weekday_idx": r["target_weekday"],
        "source_station": r["source_station"],
        "source_region": r["source_region"],
        "source_offset": r["source_offset"],
        "source_weekday": r["source_weekday"],
        "source_station_slot": r["source_station_slot"],
        "prize_keys": r["prize_keys"],
        "production_tier": r["production_tier"],
        "prediction_use": r["prediction_use"],
        "window_verdict": r["window_verdict"],
        "hr_12w": r["hr_12w"], "hr_16w": r["hr_16w"],
        "hit_rate_365": r["hit_rate_365"], "lift_365": r["lift_365"], "n_365": r["n_365"],
        "score": r["score"], "composite_score": r["composite_score"],
        "cumulative_rank_score": r["cumulative_rank_score"],
        "sample_quality": r["sample_quality"], "split_policy": r["split_policy"],
        "co_trong_mined_rule_effectiveness": bool(m),
        "so_luot_da_cham": (m["n"] if m else 0),
        "so_luot_trung": (m["hit"] if m else 0),
        "ty_le_trung_pct": round(100.0 * m["hit"] / m["n"], 2) if m and m["n"] else None,
        "mre_khoang_ngay": ("%s..%s" % (m["d1"], m["d2"])) if m else None,
        "temporal_hop_le": (tv == "HOP LE"),
        "temporal_ghi_chu": tv,
        "mined_at": r["mined_at"], "rule_version": r["rule_version"],
        "source_run_id": r["source_run_id"],
        "activation_status": r["activation_status"], "is_active": r["is_active"],
        "owner_approved_at": r["owner_approved_at"],
        "lineage_v10636": "KHONG TRUY DUOC — mined_rules khong co cot lineage; "
                          "luat duoc DELETE+dao lai moi tuan",
    })

p("-" * len(hdr))
p("TONG: %d luat | co dong trong mined_rule_effectiveness: %d | KHONG co: %d | tong luot cham: %d"
  % (len(prod), so_co_mre, len(prod) - so_co_mre, tong_luot))
RESULT["so_luat_co_mre"] = so_co_mre
RESULT["so_luat_khong_mre"] = len(prod) - so_co_mre
RESULT["tong_luot_cham"] = tong_luot

# thong ke bo sung
p("\n  Thong ke bo sung:")
p("    so luot cham / luat: min=%d max=%d trung binh=%.1f"
  % (min((mre[r["id"]]["n"] for r in prod if r["id"] in mre), default=0),
     max((mre[r["id"]]["n"] for r in prod if r["id"] in mre), default=0),
     (tong_luot / so_co_mre) if so_co_mre else 0))
p("    owner_approved_at khong NULL: %d / %d"
  % (sum(1 for r in prod if r["owner_approved_at"]), len(prod)))
p("    window_verdict phan bo: %s" % dict(Counter(r["window_verdict"] for r in prod)))
p("    production_tier phan bo: %s" % dict(Counter(r["production_tier"] for r in prod)))
p("    prediction_use phan bo: %s" % dict(Counter(r["prediction_use"] for r in prod)))
p("    sample_quality phan bo: %s" % dict(Counter(r["sample_quality"] for r in prod)))
r2 = cur.execute("select min(hit_rate_365), max(hit_rate_365), min(lift_365), max(lift_365), "
                 "min(n_365), max(n_365) from mined_rules").fetchone()
p("    hit_rate_365 %.4f..%.4f | lift_365 %.3f..%.3f | n_365 %d..%d"
  % (r2[0], r2[1], r2[2], r2[3], r2[4], r2[5]))
RESULT["thong_ke"] = {
    "owner_approved_at_not_null": sum(1 for r in prod if r["owner_approved_at"]),
    "window_verdict": dict(Counter(r["window_verdict"] for r in prod)),
    "production_tier": dict(Counter(r["production_tier"] for r in prod)),
    "prediction_use": dict(Counter(r["prediction_use"] for r in prod)),
    "sample_quality": dict(Counter(r["sample_quality"] for r in prod)),
    "hit_rate_365_min": r2[0], "hit_rate_365_max": r2[1],
    "lift_365_min": r2[2], "lift_365_max": r2[3],
    "n_365_min": r2[4], "n_365_max": r2[5],
}

# MRE mo coi
mre_orphan = one("select count(distinct rule_id) from mined_rule_effectiveness "
                 "where rule_id not in (select id from mined_rules)")
mre_orphan_rows = one("select count(*) from mined_rule_effectiveness "
                      "where rule_id not in (select id from mined_rules)")
p("\n    mined_rule_effectiveness: %d dong / %d rule_id phan biet"
  % (one("select count(*) from mined_rule_effectiveness"),
     one("select count(distinct rule_id) from mined_rule_effectiveness")))
p("    trong do MO COI (rule_id khong con trong mined_rules): %d rule_id / %d dong"
  % (mre_orphan, mre_orphan_rows))
RESULT["mre_mo_coi_rule_id"] = mre_orphan
RESULT["mre_mo_coi_dong"] = mre_orphan_rows

# verified_bucket_rules
vbr_total = one("select count(*) from verified_bucket_rules")
vbr_join = one("select count(*) from verified_bucket_rules v join mined_rules m on m.id=v.source_rule_id")
p("\n    verified_bucket_rules: %d dong, promoted_version=%s, khop source_rule_id voi mined_rules: %d"
  % (vbr_total,
     [x[0] for x in cur.execute("select distinct promoted_version from verified_bucket_rules")],
     vbr_join))
RESULT["verified_bucket_rules_tong"] = vbr_total
RESULT["verified_bucket_rules_khop"] = vbr_join

con.close()

p("\n" + "=" * 78)
p("HET R1")
p("=" * 78)

txt = "\n".join(buf)
n1 = safe_write(OUT_TXT, txt)
n2 = safe_write(OUT_JSON, json.dumps(RESULT, ensure_ascii=False, indent=2))
print("\n[OK] ghi %s (%d ky tu)" % (OUT_TXT, n1))
print("[OK] ghi %s (%d ky tu)" % (OUT_JSON, n2))
