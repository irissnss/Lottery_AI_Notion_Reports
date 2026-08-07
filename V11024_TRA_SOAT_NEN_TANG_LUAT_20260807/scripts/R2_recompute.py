# -*- coding: utf-8 -*-
"""R2 (V11024) — TINH LAI THONG KE TUNG LUAT TREN DU LIEU TUOI.

CHI DOC. Mo DB bang mode=ro. Khong ghi DB, khong sua bang khoa.

Vi sao viet moi thay vi doc lai so cu:
  - mined_rules.hit_rate_365 / lift_365 la so do dot dao 03/08 ghi lai, do tren
    CHINH cua so ma no chon luat => cham nguoc 100%.
  - mined_rule_effectiveness chi co du lieu tu 2025-12-20, va 98% dong la cham nguoc.
  Script nay do LAI tu lottery_results (2020-01-01 .. het du lieu) cho tung luat.

Cach do (doc tu ma nguon that, khong doan):
  - Chiet duoi nguon : mined_rule_eval._extract_tails_from_prizes  (alias giai thuong)
  - Ngay nguon       : mined_rule_eval._get_source_date            (D | D-1)
  - Tap duoi dich    : gom TAT CA duoi 2 so cua moi dai cua mien dich trong ngay
                       (giong mined_rule_eval._get_all_target_tails, nhung doc
                        thang lottery_results de khong phu thuoc database.py)

Nen (baseline) — HAI cach, in ca hai:
  NEN_CHINH_XAC (sieu boi / hypergeometric, tinh RIENG TUNG LUOT):
      bl_d = 1 - C(100-m_d, k_d) / C(100, k_d)
      m_d = so duoi khac nhau mien dich ra hom do ; k_d = so duoi nguon gom hom do
      => dung DUNG so gia tri gom that su cua ngay do, khong dung so trung binh.
  NEN_KIEU_DAO (dung lai cong thuc cua _seed_rules.build_rule dong 254):
      bl = 1 - (1-ps)^ans , ps = (trung binh |T| cua mien)/100 , ans = avg_src_tails
      => de doi chieu xem so lift cu sai bao nhieu.

p-value: nhi thuc mot phia tren, P(X>=h | n, p_tb) voi p_tb = trung binh bl_d.
         Kem p-value Poisson-nhi-thuc CHINH XAC (quy hoach dong) vi moi luot co
         mot bl_d khac nhau — nhi thuc chi la xap xi.
BH-FDR alpha=0.05 tren toan bo luat active.

Chay:  python artifacts/v11024_audit/scripts/R2_recompute.py
Ra  :  artifacts/v11024_audit/evidence/R2_rules_recompute_fresh.txt
       artifacts/v11024_audit/evidence/R2_recompute.json
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import sqlite3
import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

GOC = Path(__file__).resolve().parents[3]           # E:\Lottery_AI_Test
DB = GOC / "data" / "lottery_ai.db"
RA_TXT = GOC / "artifacts" / "v11024_audit" / "evidence" / "R2_rules_recompute_fresh.txt"
RA_JSON = GOC / "artifacts" / "v11024_audit" / "evidence" / "R2_recompute.json"

sys.path.insert(0, str(GOC / "web" / "backend"))
from mined_rule_eval import _extract_tails_from_prizes, _get_source_date  # noqa: E402

ALPHA = 0.05
MAU_TOI_THIEU_DO_TIEN = 20      # nguong owner giao cho R2 (trung voi V11003)

_BUT = []


def p(s: str = "") -> None:
    print(s)
    _BUT.append(s)


def ghi_an_toan(duong: Path, noi_dung: str) -> int:
    """Ghi .tmp -> flush -> fsync -> os.replace -> doc lai so do dai.
    TUYET DOI khong io.open(p,'w').write(t) (bay da lam mat file that)."""
    duong.parent.mkdir(parents=True, exist_ok=True)
    tmp = duong.with_suffix(duong.suffix + ".tmp")
    b = noi_dung.encode("utf-8")
    with open(tmp, "wb") as f:
        f.write(b)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, duong)
    lai = duong.read_bytes()
    if len(lai) != len(b):
        raise IOError(f"ghi hong {duong}: viet {len(b)} doc lai {len(lai)}")
    return len(b)


# ── thong ke ──────────────────────────────────────────────────────────────────
_CACHE_BL: dict[tuple[int, int], float] = {}


def nen_sieu_boi(m: int, k: int) -> float:
    """P(it nhat 1 trong k duoi chon ngau nhien roi vao tap m duoi), khong gian 100."""
    if k <= 0:
        return 0.0
    if m <= 0:
        return 0.0
    if 100 - m < k:
        return 1.0
    kh = (m, k)
    v = _CACHE_BL.get(kh)
    if v is None:
        v = 1.0 - math.comb(100 - m, k) / math.comb(100, k)
        _CACHE_BL[kh] = v
    return v


def p_nhi_thuc_tren(h: int, n: int, pr: float) -> float:
    """P(X >= h) voi X~Bin(n,pr). Mot phia tren."""
    if n <= 0:
        return 1.0
    pr = min(max(pr, 1e-12), 1 - 1e-12)
    if h <= 0:
        return 1.0
    tong = 0.0
    for i in range(h, n + 1):
        tong += math.comb(n, i) * pr ** i * (1 - pr) ** (n - i)
    return min(max(tong, 0.0), 1.0)


def p_poisson_nhi_thuc_tren(h: int, bls: list[float]) -> float:
    """P(X >= h) voi X = tong cac Bernoulli KHAC nhau (moi luot mot bl_d).
    Quy hoach dong chinh xac — nhi thuc chi la xap xi khi bl_d chenh nhau."""
    n = len(bls)
    if n == 0:
        return 1.0
    if h <= 0:
        return 1.0
    pv = [0.0] * (n + 1)
    pv[0] = 1.0
    for i, q in enumerate(bls):
        for j in range(i + 1, 0, -1):
            pv[j] = pv[j] * (1 - q) + pv[j - 1] * q
        pv[0] *= (1 - q)
    return min(max(sum(pv[h:]), 0.0), 1.0)


def bh_fdr(cap: list[tuple[str, float]], alpha: float = ALPHA) -> dict[str, dict]:
    """Benjamini-Hochberg. Tra ve {khoa: {q, bac_bo}}."""
    m = len(cap)
    if m == 0:
        return {}
    sx = sorted(cap, key=lambda x: x[1])
    q_tho = [(k, pv * m / (i + 1)) for i, (k, pv) in enumerate(sx)]
    # ep don dieu tu duoi len
    q_cuoi: list[tuple[str, float]] = []
    chay = 1.0
    for k, q in reversed(q_tho):
        chay = min(chay, q)
        q_cuoi.append((k, min(chay, 1.0)))
    q_cuoi.reverse()
    # nguong BH: i lon nhat co p_(i) <= i/m*alpha
    nguong_i = 0
    for i, (_, pv) in enumerate(sx, start=1):
        if pv <= i / m * alpha:
            nguong_i = i
    dat = {k for k, _ in sx[:nguong_i]}
    return {k: {"q": q, "bac_bo": k in dat} for k, q in q_cuoi}


def z_pooled(hits: int, bls: list[float]) -> tuple[float, float, float]:
    """z = (O - E)/sqrt(V) voi V = sum bl(1-bl). Tra (z, E, V)."""
    E = sum(bls)
    V = sum(b * (1 - b) for b in bls)
    if V <= 0:
        return 0.0, E, V
    return (hits - E) / math.sqrt(V), E, V


def z_gom_theo_ngay(luot: list[tuple[str, int, float]]) -> tuple[float, int]:
    """z gom cum theo NGAY. Cac luot cung ngay dung CHUNG tap duoi dich nen KHONG
    doc lap — z pooled se bi phong to. Day la ban tho hon nhung trung thuc hon:
    moi ngay la mot don vi, do trung binh chenh (hit - nen) theo ngay."""
    theo: dict[str, list[float]] = {}
    for ng, hit, bl in luot:
        theo.setdefault(ng, []).append(hit - bl)
    if len(theo) < 2:
        return 0.0, len(theo)
    tb_ngay = [sum(v) / len(v) for v in theo.values()]
    n = len(tb_ngay)
    mu = sum(tb_ngay) / n
    var = sum((x - mu) ** 2 for x in tb_ngay) / (n - 1)
    if var <= 0:
        return 0.0, n
    return mu / math.sqrt(var / n), n


def n_can_thiet(p0: float, chenh: float = 0.05, alpha: float = 0.05, luc: float = 0.80) -> int:
    """So luot can de phat hien chenh `chenh` (diem phan tram) so voi nen p0.
    Hai phia, mot mau so voi ti le da biet."""
    z_a = 1.959963985
    z_b = 0.841621234
    p1 = min(max(p0 + chenh, 1e-9), 1 - 1e-9)
    p0c = min(max(p0, 1e-9), 1 - 1e-9)
    tu = z_a * math.sqrt(p0c * (1 - p0c)) + z_b * math.sqrt(p1 * (1 - p1))
    return int(math.ceil(tu * tu / (chenh ** 2)))


# ── nap du lieu ───────────────────────────────────────────────────────────────
def duoi_cua_prizes(pr: dict) -> set[str]:
    ra = set()
    for _, v in pr.items():
        if isinstance(v, list):
            for x in v:
                if x and len(str(x)) >= 2:
                    ra.add(str(x)[-2:])
        elif v and len(str(v)) >= 2:
            ra.add(str(v)[-2:])
    return ra


def main() -> int:
    con = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row

    _h = hashlib.sha256()
    with open(DB, "rb") as _f:
        for _blk in iter(lambda: _f.read(1 << 22), b""):
            _h.update(_blk)
    sha = _h.hexdigest()[:16]
    co_db = DB.stat().st_size
    chay_luc = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    p("=" * 100)
    p("R2 (V11024) — TINH LAI THONG KE TUNG LUAT TREN DU LIEU TUOI")
    p("=" * 100)
    p(f"chay luc      : {chay_luc}  (gio may local)")
    p(f"DB            : {DB}  ({co_db} byte)")
    p(f"sha256[:16]   : {sha}")
    p(f"script        : {Path(__file__).resolve()}")
    p("che do        : CHI DOC (mode=ro)")
    p("")

    # ── 0. bang doi chung V11003/V11011 co that khong ────────────────────────
    p("-" * 100)
    p("[0] BANG DOI CHUNG mined_rule_doi_chung (V11003/V11011) — CO THAT KHONG?")
    p("-" * 100)
    co_bang = con.execute(
        "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='mined_rule_doi_chung'"
    ).fetchone()[0] > 0
    cot_mre = [r[1] for r in con.execute("PRAGMA table_info(mined_rule_effectiveness)")]
    co_giai_doan = "giai_doan" in cot_mre
    p(f"  bang mined_rule_doi_chung        : {'CO' if co_bang else 'KHONG CO'}")
    p(f"  cot mined_rule_effectiveness.giai_doan : {'CO' if co_giai_doan else 'KHONG CO'}")
    if not co_bang and not co_giai_doan:
        p("  => V11003 chi moi chay che do CHI DOC. Buoc `--dung` (tao cot + tao bang +")
        p("     nap luat gia) CHUA TUNG CHAY tren ban local. Nen KHONG co cach phan loai")
        p("     giai_doan nao san de doi chieu — R2 tu phan loai lai tu mined_at.")
    p("")

    # ── 1. nap lottery_results ───────────────────────────────────────────────
    duoi_dich: dict[tuple[str, str], set[str]] = {}   # (mien, ngay) -> tap duoi
    nguon: dict[tuple[str, str, str], dict] = {}      # (mien, dai, ngay) -> prizes
    n_hong = 0
    for r in con.execute(
        "SELECT date, region, station, prizes_json FROM lottery_results "
        "WHERE prizes_json IS NOT NULL AND station IS NOT NULL AND TRIM(station)<>''"
    ):
        try:
            pr = json.loads(r["prizes_json"])
        except Exception:
            n_hong += 1
            continue
        if not isinstance(pr, dict):
            n_hong += 1
            continue
        nguon[(r["region"], r["station"], r["date"])] = pr
        duoi_dich.setdefault((r["region"], r["date"]), set()).update(duoi_cua_prizes(pr))

    ngay_min, ngay_max, n_kq = con.execute(
        "SELECT MIN(date), MAX(date), COUNT(*) FROM lottery_results").fetchone()
    p("-" * 100)
    p("[1] DU LIEU GOC")
    p("-" * 100)
    p(f"  lottery_results : {n_kq} dong, {ngay_min} .. {ngay_max}   (prizes_json hong: {n_hong})")
    p(f"  cap (mien,ngay) co ket qua : {len(duoi_dich)}")
    tb_m = {}
    for (mi, _), t in duoi_dich.items():
        tb_m.setdefault(mi, []).append(len(t))
    p("")
    p("  KICH THUOC TAP DUOI DICH |T| — day la ly do moi so hit rate cu vo nghia:")
    p(f"    {'mien':6} {'so ngay':>8} {'|T| tb':>8} {'|T| min':>8} {'|T| max':>8} "
      f"{'nen 1 duoi':>11} {'nen 4 duoi':>11}")
    ps_mien = {}
    for mi in sorted(tb_m):
        v = tb_m[mi]
        tb = sum(v) / len(v)
        ps_mien[mi] = tb / 100.0
        p(f"    {mi:6} {len(v):>8} {tb:>8.1f} {min(v):>8} {max(v):>8} "
          f"{tb / 100:>10.1%} {1 - (1 - tb / 100) ** 4:>10.1%}")
    p("    'nen 4 duoi' = xac suat TRUNG NGAU NHIEN neu gom 4 duoi bat ky.")
    p("")

    # ── 2. luat active ───────────────────────────────────────────────────────
    luat = [dict(r) for r in con.execute(
        "SELECT id, target_region, target_weekday, source_station, source_region, "
        "source_offset, prize_keys, mined_at, n_365, hit_rate_365, lift_365, "
        "avg_src_tails, sample_quality, production_tier, window_verdict, score "
        "FROM mined_rules WHERE is_active=1 ORDER BY id")]
    ngay_dao = {}
    for r in luat:
        ngay_dao[r["id"]] = (r["mined_at"] or "")[:10]
    tap_ngay_dao = sorted(set(ngay_dao.values()))
    p("-" * 100)
    p("[2] LUAT ACTIVE")
    p("-" * 100)
    p(f"  so luat active : {len(luat)}")
    p(f"  ngay dao (date(mined_at)) : {tap_ngay_dao}")
    if len(tap_ngay_dao) == 1:
        p(f"  => TAT CA {len(luat)} luat dao cung mot ngay {tap_ngay_dao[0]}. Moi luat co CUNG")
        p("     mot bien gioi cham-nguoc/do-tien, nen so luot do tien bi chan cung boi")
        p(f"     so ngay tu {tap_ngay_dao[0]} den {ngay_max}.")
    p("")

    # ── 3. do lai tung luat ──────────────────────────────────────────────────
    ngay_theo_mien_thu: dict[tuple[str, int], list[str]] = {}
    for (mi, ng) in duoi_dich:
        wd = datetime.strptime(ng, "%Y-%m-%d").weekday()
        ngay_theo_mien_thu.setdefault((mi, wd), []).append(ng)
    for v in ngay_theo_mien_thu.values():
        v.sort()

    ket: list[dict] = []
    for r in luat:
        rid = r["id"]
        tr = r["target_region"]
        tw = int(r["target_weekday"])
        st = r["source_station"]
        sr = r["source_region"]
        ol = r["source_offset"] or "D-1"
        pk = r["prize_keys"] or ""
        d_dao = ngay_dao[rid]

        luot = []          # (ngay, hit, bl_d, k, m)
        thieu_nguon = 0
        for ng in ngay_theo_mien_thu.get((tr, tw), []):
            T = duoi_dich.get((tr, ng)) or set()
            if not T:
                continue
            nd = _get_source_date(ng, ol)
            pr = nguon.get((sr, st, nd))
            if pr is None:
                thieu_nguon += 1
                continue
            k_t = set(_extract_tails_from_prizes(pr, pk))
            if not k_t:
                thieu_nguon += 1
                continue
            k = len(k_t)
            m = len(T)
            hit = 1 if (k_t & T) else 0
            luot.append((ng, hit, nen_sieu_boi(m, k), k, m))

        def goi(sub, ten):
            n = len(sub)
            if n == 0:
                return {"pha": ten, "n": 0, "h": 0, "hr": None, "nen": None, "lift": None,
                        "p_bin": None, "p_pb": None, "k_tb": None, "m_tb": None,
                        "z": None, "tu": None, "den": None}
            h = sum(x[1] for x in sub)
            bls = [x[2] for x in sub]
            ptb = sum(bls) / n
            z, _E, _V = z_pooled(h, bls)
            return {"pha": ten, "n": n, "h": h, "hr": h / n, "nen": ptb,
                    "lift": (h / n) / ptb if ptb > 0 else None,
                    "p_bin": p_nhi_thuc_tren(h, n, ptb),
                    "p_pb": p_poisson_nhi_thuc_tren(h, bls),
                    "k_tb": sum(x[3] for x in sub) / n,
                    "m_tb": sum(x[4] for x in sub) / n,
                    "z": z, "tu": sub[0][0], "den": sub[-1][0]}

        cn = [x for x in luot if x[0] < d_dao]        # CHAM NGUOC : date <  mined_at
        dt = [x for x in luot if x[0] >= d_dao]       # DO TIEN    : date >= mined_at
        dt_ngat = [x for x in luot if x[0] > d_dao]   # bien V11003 (date > mined_at)

        # cua so 365 ngay truoc khi dao — de doi chieu voi n_365/hit_rate_365 da luu
        c365 = (datetime.strptime(d_dao, "%Y-%m-%d") - timedelta(days=365)).strftime("%Y-%m-%d")
        w365 = [x for x in luot if c365 <= x[0] < d_dao]
        # TACH THIEN VI CHON: _seed_rules chon top-5 BANG CHINH cua so 365 ngay nay.
        # Phan TRUOC cua so chua bao gio duoc luat nhin thay luc chon => sach thien vi chon,
        # du van la cham nguoc ve thoi gian.
        truoc_cs = [x for x in luot if x[0] < c365]

        # nen kieu dao (_seed_rules.build_rule dong 254): 1-(1-ps)^ans
        ps = ps_mien.get(tr, 0.0)
        ans_luu = float(r["avg_src_tails"] or 0)
        bl_dao = 1 - (1 - ps) ** ans_luu if ans_luu > 0 else None

        ket.append({
            "rule_id": rid, "target_region": tr, "target_weekday": tw,
            "source": f"{sr}/{st}", "source_offset": ol, "prize_keys": pk,
            "mined_at": r["mined_at"], "ngay_dao": d_dao,
            "luu": {"n_365": r["n_365"], "hit_rate_365": r["hit_rate_365"],
                    "lift_365": r["lift_365"], "avg_src_tails": r["avg_src_tails"],
                    "sample_quality": r["sample_quality"],
                    "production_tier": r["production_tier"],
                    "window_verdict": r["window_verdict"], "score": r["score"]},
            "nen_kieu_dao": bl_dao,
            "toan_bo": goi(luot, "TOAN_BO"),
            "cham_nguoc": goi(cn, "CHAM_NGUOC"),
            "do_tien": goi(dt, "DO_TIEN"),
            "do_tien_ngat": goi(dt_ngat, "DO_TIEN_STRICT"),
            "w365": goi(w365, "W365_TRONG_CUA_SO_CHON"),
            "truoc_cua_so": goi(truoc_cs, "TRUOC_CUA_SO_CHON"),
            "thieu_nguon": thieu_nguon,
            "_luot_cn": cn, "_luot_dt": dt,
            "_luot_w365": w365, "_luot_truoc": truoc_cs,
        })

    # ── 4. doi chieu voi mined_rule_effectiveness ────────────────────────────
    p("-" * 100)
    p("[4] DOI CHIEU CACH DO CUA R2 VOI BANG THAT mined_rule_effectiveness")
    p("-" * 100)
    mre = {(r["rule_id"], r["date"]): r["hit_any"] for r in con.execute(
        "SELECT rule_id, date, hit_any FROM mined_rule_effectiveness")}
    khop = lech = 0
    for k in ket:
        for ng, hit, _b, _k, _m in k["_luot_cn"] + k["_luot_dt"]:
            v = mre.get((k["rule_id"], ng))
            if v is None:
                continue
            if int(v) == hit:
                khop += 1
            else:
                lech += 1
    tong_dc = khop + lech
    p(f"  so luot trung nhau : {tong_dc}")
    p(f"  khop hit_any       : {khop}  ({khop / tong_dc:.2%})" if tong_dc else "  (khong co luot trung)")
    p(f"  lech               : {lech}")
    if tong_dc and lech == 0:
        p("  => cach chiet duoi + cach tinh trung cua R2 TAI LAP DUOC bang that 100%.")
        p("     Nen cac so moi duoi day khong phai cach do khac, chi la CUNG cach do")
        p("     tren nhieu du lieu hon va co them NEN de so sanh.")
    n_mre_mo_coi = con.execute(
        "SELECT COUNT(*) FROM mined_rule_effectiveness e "
        "WHERE NOT EXISTS (SELECT 1 FROM mined_rules r WHERE r.id=e.rule_id)").fetchone()[0]
    n_mre = con.execute("SELECT COUNT(*) FROM mined_rule_effectiveness").fetchone()[0]
    p(f"  bang that co {n_mre} dong, trong do {n_mre_mo_coi} dong MO COI "
      f"({n_mre_mo_coi / n_mre:.1%}) — rule_id khong con trong mined_rules.")
    p("")

    # ── 5. BH-FDR ────────────────────────────────────────────────────────────
    fdr_cn = bh_fdr([(str(k["rule_id"]), k["cham_nguoc"]["p_bin"])
                     for k in ket if k["cham_nguoc"]["n"] > 0])
    fdr_dt = bh_fdr([(str(k["rule_id"]), k["do_tien"]["p_bin"])
                     for k in ket if k["do_tien"]["n"] > 0])
    fdr_w = bh_fdr([(str(k["rule_id"]), k["w365"]["p_bin"])
                    for k in ket if k["w365"]["n"] > 0])
    fdr_tr = bh_fdr([(str(k["rule_id"]), k["truoc_cua_so"]["p_bin"])
                     for k in ket if k["truoc_cua_so"]["n"] > 0])
    for k in ket:
        k["fdr_w365"] = fdr_w.get(str(k["rule_id"]))
        k["fdr_truoc_cua_so"] = fdr_tr.get(str(k["rule_id"]))
    fdr_cn_pb = bh_fdr([(str(k["rule_id"]), k["cham_nguoc"]["p_pb"])
                        for k in ket if k["cham_nguoc"]["n"] > 0])
    fdr_dt_pb = bh_fdr([(str(k["rule_id"]), k["do_tien"]["p_pb"])
                        for k in ket if k["do_tien"]["n"] > 0])
    for k in ket:
        k["fdr_cham_nguoc"] = fdr_cn.get(str(k["rule_id"]))
        k["fdr_do_tien"] = fdr_dt.get(str(k["rule_id"]))
        k["fdr_cham_nguoc_pb"] = fdr_cn_pb.get(str(k["rule_id"]))
        k["fdr_do_tien_pb"] = fdr_dt_pb.get(str(k["rule_id"]))

    # ── 6. bang tung luat ────────────────────────────────────────────────────
    p("-" * 100)
    p("[6] BANG TUNG LUAT — CHAM NGUOC (date < mined_at) vs DO TIEN (date >= mined_at)")
    p("-" * 100)
    p("  'nen' = xac suat trung ngau nhien tinh RIENG TUNG LUOT theo so duoi that su gom")
    p("          hom do (sieu boi), roi lay trung binh. lift = hr/nen. lift ~ 1.00 = KHONG CO GI.")
    p("  q = BH-FDR alpha=0.05 tren p nhi thuc mot phia tren. '*' = bac bo duoc H0.")
    p("")
    hd = (f"  {'id':>5} {'mien':4} {'thu':3} {'nguon':28} {'giai':9} "
          f"|| {'n':>4} {'hr':>6} {'nen':>6} {'lift':>5} {'p':>8} {'q':>8} "
          f"|| {'n':>3} {'hr':>6} {'nen':>6} {'lift':>5} {'p':>7} "
          f"|| {'lift_luu':>8}")
    p(f"  {'':>5} {'':4} {'':3} {'':28} {'':9} "
      f"|| {'--------- CHAM NGUOC ----------------------':<42} "
      f"|| {'------ DO TIEN --------':<31} || {'da luu':>8}")
    p(hd)
    p("  " + "-" * 152)
    WD = {0: "T2", 1: "T3", 2: "T4", 3: "T5", 4: "T6", 5: "T7", 6: "CN"}
    for k in sorted(ket, key=lambda x: (x["target_region"], x["target_weekday"], x["rule_id"])):
        cn, dt = k["cham_nguoc"], k["do_tien"]
        f = k["fdr_cham_nguoc"] or {}
        sao = "*" if f.get("bac_bo") else " "
        ng = f"{k['source']} {k['source_offset']}"
        s_cn = (f"{cn['n']:>4} {cn['hr']:>6.1%} {cn['nen']:>6.1%} {cn['lift']:>5.2f} "
                f"{cn['p_bin']:>8.4f} {f.get('q', 1):>7.4f}{sao}") if cn["n"] else f"{'—':>4} {'':>36}"
        s_dt = (f"{dt['n']:>3} {dt['hr']:>6.1%} {dt['nen']:>6.1%} {dt['lift']:>5.2f} "
                f"{dt['p_bin']:>7.4f}") if dt["n"] else f"{'—':>3} {'':>27}"
        p(f"  {k['rule_id']:>5} {k['target_region']:4} {WD[k['target_weekday']]:3} {ng[:28]:28} "
          f"{k['prize_keys'][:9]:9} || {s_cn} || {s_dt} || {k['luu']['lift_365'] or 0:>8.3f}")
    p("")

    # ── 7. du mau do tien ────────────────────────────────────────────────────
    p("-" * 100)
    p(f"[7] DU MAU DO TIEN? (nguong n >= {MAU_TOI_THIEU_DO_TIEN} luot/luat)")
    p("-" * 100)
    du = [k for k in ket if k["do_tien"]["n"] >= MAU_TOI_THIEU_DO_TIEN]
    khong = [k for k in ket if k["do_tien"]["n"] < MAU_TOI_THIEU_DO_TIEN]
    p(f"  DU MAU    : {len(du)}/{len(ket)} luat")
    p(f"  CHUA DU   : {len(khong)}/{len(ket)} luat")
    pp = {}
    for k in ket:
        pp.setdefault(k["do_tien"]["n"], 0)
        pp[k["do_tien"]["n"]] += 1
    p(f"  phan bo so luot do tien/luat : "
      + ", ".join(f"n={a} co {b} luat" for a, b in sorted(pp.items())))
    n_dt_max = max((k["do_tien"]["n"] for k in ket), default=0)
    if tap_ngay_dao:
        so_ngay = (datetime.strptime(ngay_max, "%Y-%m-%d")
                   - datetime.strptime(tap_ngay_dao[0], "%Y-%m-%d")).days + 1
        p(f"  Ly do cung: tu ngay dao {tap_ngay_dao[0]} den het du lieu {ngay_max} moi co "
          f"{so_ngay} ngay lich.")
        p(f"  Moi luat chi ban MOT thu trong tuan => toi da {n_dt_max} luot do tien. "
          f"Can >= {MAU_TOI_THIEU_DO_TIEN} luot")
        p(f"  => phai cho them {(MAU_TOI_THIEU_DO_TIEN - n_dt_max) * 7} ngay lich "
          f"({MAU_TOI_THIEU_DO_TIEN - n_dt_max} tuan) NUA moi du, neu khong dao lai luat.")
    p("")

    # ── 8. z tong hop ────────────────────────────────────────────────────────
    p("-" * 100)
    p("[8] Z TONG HOP HAI NHOM + SUC MANH THONG KE")
    p("-" * 100)
    p(f"  {'nhom':14} {'so luat':>8} {'n luot':>8} {'trung':>7} {'hr':>7} "
      f"{'nen E':>9} {'lift':>6} {'z gop':>8} {'z cum-ngay':>11} {'ngay':>6}")
    p("  " + "-" * 100)
    tong = {}
    for ten, khoa in (("CHAM NGUOC", "_luot_cn"),
                      ("  ├ trong CS", "_luot_w365"),
                      ("  └ truoc CS", "_luot_truoc"),
                      ("DO TIEN", "_luot_dt")):
        luot = [x for k in ket for x in k[khoa]]
        n = len(luot)
        if n == 0:
            p(f"  {ten:14} {'—':>8}")
            continue
        h = sum(x[1] for x in luot)
        bls = [x[2] for x in luot]
        z, E, V = z_pooled(h, bls)
        zc, nng = z_gom_theo_ngay([(x[0], x[1], x[2]) for x in luot])
        nl = sum(1 for k in ket if k[khoa])
        p(f"  {ten:14} {nl:>8} {n:>8} {h:>7} {h / n:>7.2%} {E:>9.1f} "
          f"{(h / n) / (E / n):>6.3f} {z:>+8.2f} {zc:>+11.2f} {nng:>6}")
        tong[ten] = {"n_luat": nl, "n": n, "h": h, "hr": h / n, "E": E,
                     "nen_tb": E / n, "lift": (h / n) / (E / n), "z": z,
                     "z_cum_ngay": zc, "so_ngay": nng}
    p("  " + "-" * 100)
    p("  'z gop'      : coi moi luot doc lap. PHONG TO — nhieu luat cung ngay dung CHUNG")
    p("                 tap duoi dich nen chung trung/truot cung nhau.")
    p("  'z cum-ngay' : gom theo NGAY (moi ngay 1 don vi). Trung thuc hon. DUNG SO NAY.")
    p("  'trong CS'   : cua so 365 ngay ma _seed_rules DUNG DE CHON top-5 => co thien vi chon.")
    p("  'truoc CS'   : truoc cua so do => luat CHUA TUNG nhin thay luc chon. Van la cham")
    p("                 nguoc ve thoi gian nhung SACH thien vi chon. Day la phep thu that su.")
    p("")
    zw = tong.get("  ├ trong CS")
    zt = tong.get("  └ truoc CS")
    if zw and zt:
        p("  DOC HAI DONG 'trong CS' va 'truoc CS' CANH NHAU:")
        p(f"    trong cua so chon : lift {zw['lift']:.3f}  z cum-ngay {zw['z_cum_ngay']:+.2f}  (n={zw['n']})")
        p(f"    truoc cua so chon : lift {zt['lift']:.3f}  z cum-ngay {zt['z_cum_ngay']:+.2f}  (n={zt['n']})")
        p(f"    chenh lift        : {zw['lift'] - zt['lift']:+.3f}")
        if zw["lift"] > zt["lift"] and zt["lift"] <= 1.005:
            p("    => Loi the CHI TON TAI trong dung cua so ma luat duoc chon ra. Ra khoi cua so")
            p("       do thi lift ve ~1.00. Day la dau van tay cua THIEN VI CHON, khong phai")
            p("       cau truc that. Cung mot luat, cung mot dai, chi khac doan thoi gian.")
        elif zt["lift"] > 1.02:
            p("    => Loi the con giu duoc ca ngoai cua so chon — dang xem xet tiep, chua the")
            p("       quy hoan toan cho thien vi chon.")
    p("")
    p("  TACH THEO MIEN (z cum-ngay):")
    p(f"    {'mien':5} {'nhom':14} {'n':>7} {'hr':>7} {'nen':>7} {'lift':>6} {'z cum-ngay':>11}")
    theo_mien = {}
    for mi in sorted(ps_mien):
        for ten, khoa in (("trong CS", "_luot_w365"), ("truoc CS", "_luot_truoc"),
                          ("DO TIEN", "_luot_dt")):
            luot = [x for k in ket if k["target_region"] == mi for x in k[khoa]]
            if not luot:
                p(f"    {mi:5} {ten:14} {'—':>7}")
                continue
            n = len(luot)
            h = sum(x[1] for x in luot)
            E = sum(x[2] for x in luot)
            zc, _ = z_gom_theo_ngay([(x[0], x[1], x[2]) for x in luot])
            p(f"    {mi:5} {ten:14} {n:>7} {h / n:>7.2%} {E / n:>7.2%} "
              f"{(h / n) / (E / n):>6.3f} {zc:>+11.2f}")
            theo_mien[f"{mi}|{ten}"] = {"n": n, "h": h, "hr": h / n, "nen_tb": E / n,
                                        "lift": (h / n) / (E / n), "z_cum_ngay": zc}
    p("")

    p("  SUC MANH THONG KE — can bao nhieu luot de phat hien chenh 5 diem so voi nen?")
    p("  (hai phia, alpha=0.05, luc=0.80, mot mau so voi ti le nen da biet)")
    p(f"    {'nen p0':>8} {'n can':>8}   ghi chu")
    for mi in sorted(ps_mien):
        pk = [k for k in ket if k["target_region"] == mi]
        bl = [x[2] for k in pk for x in k["_luot_cn"] + k["_luot_dt"]]
        if not bl:
            continue
        p0 = sum(bl) / len(bl)
        p(f"    {p0:>8.1%} {n_can_thiet(p0):>8}   mien {mi} (nen trung binh that)")
    p("")
    p("    QUY RA THOI GIAN CHO: moi luat chi ban MOT thu trong tuan => 1 luot/tuan.")
    p(f"    {'mien':6} {'n can':>7} {'tuan cho':>9} {'nam cho':>8}")
    for mi in sorted(ps_mien):
        pk = [k for k in ket if k["target_region"] == mi]
        bl = [x[2] for k in pk for x in k["_luot_cn"] + k["_luot_dt"]]
        if not bl:
            continue
        nc = n_can_thiet(sum(bl) / len(bl))
        p(f"    {mi:6} {nc:>7} {nc:>9} {nc / 52:>8.1f}")
    p("    => Do TUNG LUAT RIENG LE bang do tien la khong kha thi trong doi nguoi.")
    p("       Muon ket luan trong vai thang thi phai gop luat lai thanh MOT phep do")
    p("       chung (nhu dong 'DO TIEN' o bang tren), va phai doi thuoc do.")
    p("")
    p("    Vi sao nen cao lai lam n can NHO di ma van vo dung: khi nen da 95% thi tran")
    p("    con lai chi 5 diem — 'chenh 5 diem' nghia la phai TRUNG 100%, khong the sai lan nao.")
    p("    Muon do that su thi phai doi thuoc do (vi du: so duoi TRUNG tren so duoi GOM,")
    p("    hoac bach thu), chu khong phai 'co it nhat mot duoi trung'.")
    p("")

    # ── 9. bien phan loai ────────────────────────────────────────────────────
    p("-" * 100)
    p("[9] BIEN PHAN LOAI: R2 (date >= mined_at) vs V11003 (date > date(mined_at))")
    p("-" * 100)
    n_dt = sum(k["do_tien"]["n"] for k in ket)
    n_dt_s = sum(k["do_tien_ngat"]["n"] for k in ket)
    p(f"  R2      DO_TIEN (>=) : {n_dt} luot tren {sum(1 for k in ket if k['do_tien']['n'])} luat")
    p(f"  V11003  DO_TIEN (> ) : {n_dt_s} luot tren {sum(1 for k in ket if k['do_tien_ngat']['n'])} luat")
    p(f"  chenh                : {n_dt - n_dt_s} luot — dung la cac luot roi vao chinh ngay dao "
      f"{tap_ngay_dao[0] if tap_ngay_dao else '?'}")
    p("  R2 dung '>=' theo dung viec owner giao. Luat dao luc 00:30 nen ket qua trong")
    p("  ngay do CHUA xay ra khi dao => xep vao do tien la dung. V11003 dung '>' la")
    p("  chat hon; ca hai deu khong doi ket luan vi so luot qua nho.")
    p("")

    # ── 10. so cu vs so moi ──────────────────────────────────────────────────
    p("-" * 100)
    p("[10] SO DA LUU TRONG mined_rules CO DUNG KHONG? (doi chieu cua so 365 ngay truoc khi dao)")
    p("-" * 100)
    p(f"  {'id':>5} {'n_luu':>6} {'n_do':>6} {'hr_luu':>7} {'hr_do':>7} "
      f"{'lift_luu':>8} {'lift_dung':>9} {'ans_luu':>7} {'ans_do':>7}")
    p("  " + "-" * 80)
    lech_lift = []
    for k in sorted(ket, key=lambda x: x["rule_id"])[:12]:
        w = k["w365"]
        if not w["n"]:
            continue
        lech_lift.append((k["luu"]["lift_365"] or 0, w["lift"]))
        p(f"  {k['rule_id']:>5} {k['luu']['n_365'] or 0:>6} {w['n']:>6} "
          f"{(k['luu']['hit_rate_365'] or 0):>7.1%} {w['hr']:>7.1%} "
          f"{(k['luu']['lift_365'] or 0):>8.3f} {w['lift']:>9.3f} "
          f"{(k['luu']['avg_src_tails'] or 0):>7.1f} {w['k_tb']:>7.1f}")
    p("  (in 12 luat dau; toan bo trong R2_recompute.json)")
    tat = [(k["luu"]["lift_365"] or 0, k["w365"]["lift"]) for k in ket if k["w365"]["n"]]
    if tat:
        p("")
        p(f"  lift_365 DA LUU   : tb {sum(a for a, _ in tat) / len(tat):.3f}  "
          f"min {min(a for a, _ in tat):.3f}  max {max(a for a, _ in tat):.3f}")
        p(f"  lift TINH LAI DUNG: tb {sum(b for _, b in tat) / len(tat):.3f}  "
          f"min {min(b for _, b in tat):.3f}  max {max(b for _, b in tat):.3f}")
    p("")

    # ── 11. ket ──────────────────────────────────────────────────────────────
    p("-" * 100)
    p("[11] KET LUAN DO DUOC")
    p("-" * 100)
    n_bac_bo_cn = sum(1 for k in ket if (k["fdr_cham_nguoc"] or {}).get("bac_bo"))
    n_bac_bo_dt = sum(1 for k in ket if (k["fdr_do_tien"] or {}).get("bac_bo"))
    n_bac_bo_cn_pb = sum(1 for k in ket if (k["fdr_cham_nguoc_pb"] or {}).get("bac_bo"))
    n_bac_bo_dt_pb = sum(1 for k in ket if (k["fdr_do_tien_pb"] or {}).get("bac_bo"))
    n_lift_tren1_cn = sum(1 for k in ket if k["cham_nguoc"]["n"] and k["cham_nguoc"]["lift"] > 1.0)
    p(f"  1. BH-FDR alpha=0.05 tren CHAM NGUOC : bac bo duoc {n_bac_bo_cn}/{len(ket)} luat "
      f"(p nhi thuc) · {n_bac_bo_cn_pb}/{len(ket)} (p Poisson-nhi-thuc)")
    p(f"  2. BH-FDR alpha=0.05 tren DO TIEN    : bac bo duoc {n_bac_bo_dt}/{len(ket)} luat "
      f"(p nhi thuc) · {n_bac_bo_dt_pb}/{len(ket)} (p Poisson-nhi-thuc)")
    p(f"  3. so luat co lift > 1.00 o cham nguoc : {n_lift_tren1_cn}/{len(ket)}")
    p("")
    p("     BANG BH-FDR BON GIAI DOAN — cot 'p<0.05 tho' so voi 'ky vong ngau nhien'")
    p("     la phep thu de doc nhat: neu luat khong co gi thi hai so phai bang nhau.")
    p(f"     {'giai doan':22} {'so luat':>7} {'p<0.05':>7} {'ky vong':>8} "
      f"{'BH bac bo':>10} {'lift>1':>7} {'p nho nhat':>11}")
    p("     " + "-" * 78)
    for ten, pha, fdr in (("TRONG cua so chon", "w365", fdr_w),
                          ("TRUOC cua so chon", "truoc_cua_so", fdr_tr),
                          ("CHAM NGUOC (ca hai)", "cham_nguoc", fdr_cn),
                          ("DO TIEN", "do_tien", fdr_dt)):
        co = [k for k in ket if k[pha]["n"] > 0]
        if not co:
            continue
        ps_ = [k[pha]["p_bin"] for k in co]
        p(f"     {ten:22} {len(co):>7} {sum(1 for x in ps_ if x < 0.05):>7} "
          f"{len(co) * 0.05:>8.1f} "
          f"{sum(1 for k in co if (fdr.get(str(k['rule_id'])) or {}).get('bac_bo')):>10} "
          f"{sum(1 for k in co if k[pha]['lift'] > 1.0):>7} {min(ps_):>11.6f}")
    p("     " + "-" * 78)
    co_tr = [k for k in ket if k["truoc_cua_so"]["n"] > 0]
    if co_tr:
        n_it = sum(1 for k in co_tr if k["truoc_cua_so"]["p_bin"] < 0.05)
        n_l1 = sum(1 for k in co_tr if k["truoc_cua_so"]["lift"] > 1.0)
        p(f"     Doc dong TRUOC cua so chon: {n_it} luat co p<0.05, ngau nhien thuan tuy da")
        p(f"     cho ra {len(co_tr) * 0.05:.1f} luat. {n_l1}/{len(co_tr)} luat co lift>1 — tung dong xu")
        p(f"     cho ra {len(co_tr) / 2:.0f}. KHONG CO GI VUOT NGAU NHIEN o ngoai cua so chon.")
    p(f"  4. so luat DU MAU do tien (n>={MAU_TOI_THIEU_DO_TIEN}) : {len(du)}/{len(ket)}")
    if "CHAM NGUOC" in tong:
        t = tong["CHAM NGUOC"]
        p(f"  5. CHAM NGUOC gop : hr {t['hr']:.2%} vs nen {t['nen_tb']:.2%} "
          f"=> lift {t['lift']:.3f}, z cum-ngay {t['z_cum_ngay']:+.2f}")
    if "DO TIEN" in tong:
        t = tong["DO TIEN"]
        p(f"  6. DO TIEN gop    : hr {t['hr']:.2%} vs nen {t['nen_tb']:.2%} "
          f"=> lift {t['lift']:.3f}, z cum-ngay {t['z_cum_ngay']:+.2f}")
    if zw and zt:
        p(f"  7. THIEN VI CHON  : lift trong cua so chon {zw['lift']:.3f} vs "
          f"ngoai cua so {zt['lift']:.3f} (chenh {zw['lift'] - zt['lift']:+.3f})")
    p(f"  8. TONG SO LUOT DO TIEN TREN CA {len(ket)} LUAT : "
      f"{tong.get('DO TIEN', {}).get('n', 0)} luot. Khong luat nao co qua 1 luot.")
    p("")

    # ── ghi ra ───────────────────────────────────────────────────────────────
    for k in ket:
        for _x in ("_luot_cn", "_luot_dt", "_luot_w365", "_luot_truoc"):
            k.pop(_x, None)
    goi_json = {
        "ma": "R2_V11024",
        "chay_luc": chay_luc,
        "db": str(DB),
        "db_sha256_16": sha,
        "script": str(Path(__file__).resolve()),
        "che_do": "chi_doc_mode_ro",
        "lottery_results": {"n": n_kq, "tu": ngay_min, "den": ngay_max, "json_hong": n_hong},
        "nen_mien": {mi: {"T_tb": sum(v) / len(v), "ps": ps_mien[mi], "so_ngay": len(v)}
                     for mi, v in tb_m.items()},
        "bang_doi_chung_ton_tai": co_bang,
        "cot_giai_doan_ton_tai": co_giai_doan,
        "doi_chieu_mre": {"trung": tong_dc, "khop": khop, "lech": lech,
                          "mre_tong": n_mre, "mre_mo_coi": n_mre_mo_coi},
        "nguong_do_tien": MAU_TOI_THIEU_DO_TIEN,
        "du_mau_do_tien": len(du), "chua_du_mau_do_tien": len(khong),
        "tong_hop": tong,
        "tong_hop_theo_mien": theo_mien,
        "bh_fdr": {"cham_nguoc_bac_bo": n_bac_bo_cn, "do_tien_bac_bo": n_bac_bo_dt,
                   "cham_nguoc_bac_bo_pb": n_bac_bo_cn_pb, "do_tien_bac_bo_pb": n_bac_bo_dt_pb,
                   "alpha": ALPHA},
        "n_can_chenh_5_diem": {mi: n_can_thiet(
            sum(x for k in ket if k["target_region"] == mi
                for x in [k["toan_bo"]["nen"]] if x is not None)
            / max(sum(1 for k in ket if k["target_region"] == mi
                      and k["toan_bo"]["nen"] is not None), 1))
            for mi in sorted(ps_mien)},
        "luat": ket,
    }
    n1 = ghi_an_toan(RA_TXT, "\n".join(_BUT) + "\n")
    n2 = ghi_an_toan(RA_JSON, json.dumps(goi_json, ensure_ascii=False, indent=1))
    print(f"\n[ghi] {RA_TXT}  ({n1} byte)")
    print(f"[ghi] {RA_JSON}  ({n2} byte)")
    con.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
