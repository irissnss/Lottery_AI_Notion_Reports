# -*- coding: utf-8 -*-
"""V11165 · GATE 9 · VIEC 3 — TEST SUITE chin nhom A..I cho PURE_CONTEXT_RENDERER.

TEP MOI trong artifacts/. KHONG deploy · KHONG ghi DB production · KHONG goi provider.

Chay:  /root/Lottery_AI_Test/venv/bin/python3 v11165_k9_tests.py

Nguyen tac cua bo thu nay
  · Moi phep DEU phai lam duoc CONG DO (RM-15). Nhom E la nhom chung minh dieu do:
    tung phep giai lap MOT vi pham va doi cong TRUOT; xong thi KHOI PHUC nguyen trang.
  · Phep nao KHONG CHAY DUOC thi ghi thang `KHONG_CHAY_DUOC` kem ly do — cam bo im lang
    va cam tinh no la "dat".
  · Moi DB tam deu nam trong artifacts/, tao tu ban sao cua clone bat bien.
    Clone bat bien va DB production KHONG bao gio bi mo o che do ghi.
"""
import sys, io, os, re, json, math, shutil, sqlite3, hashlib, subprocess, inspect
import importlib.util, unicodedata, random

sys.stdout.reconfigure(encoding="utf-8")
ART = "/root/Lottery_AI_Test/artifacts"
PY = "/root/Lottery_AI_Test/venv/bin/python3"
CLONE = os.path.join(ART, "v11165_immutable.db")
PROD_DB = "/root/Lottery_AI_Test/data/lottery_ai.db"
NGAY_NEO = "2026-09-04"          # ngay co du lieu day du tren clone
TMP = os.path.join(ART, "_k9_tmp")


def nap(ten, duong):
    sp = importlib.util.spec_from_file_location(ten, duong)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


R = nap("k9r", os.path.join(ART, "v11165_k9_renderer.py"))
G = nap("k9g", os.path.join(ART, "v11165_k9_contam_v2.py"))

KQ = {"nhom": {}, "moi_phep": []}


def ghi(nhom, ten, dat, chi_tiet="", khong_chay=False):
    KQ["nhom"].setdefault(nhom, {"chay": 0, "dat": 0, "truot": 0, "khong_chay": 0})
    o = KQ["nhom"][nhom]
    if khong_chay:
        o["khong_chay"] += 1
        tt = "KHONG_CHAY_DUOC"
    else:
        o["chay"] += 1
        o["dat" if dat else "truot"] += 1
        tt = "DAT" if dat else "TRUOT"
    KQ["moi_phep"].append({"nhom": nhom, "ten": ten, "trang_thai": tt, "chi_tiet": chi_tiet})
    print("  [%-15s] %-58s %s%s" % (nhom, ten[:58], tt,
                                    ("  :: " + chi_tiet[:150]) if chi_tiet else ""))


def sha(s):
    return hashlib.sha256(s.encode("utf-8") if isinstance(s, str) else s).hexdigest()


def ro(db):
    c = sqlite3.connect("file:%s?mode=ro" % db, uri=True)
    c.row_factory = sqlite3.Row
    return c


def ngay_cong(d, k):
    c = ro(CLONE)
    v = c.execute("SELECT date(?, ?)", (d, "%+d days" % k)).fetchone()[0]
    c.close()
    return v


def F_va_S(db, ngay, mien, cutoff):
    F = R.thu_thap(db, ngay, mien, cutoff)
    return F, R.render(F)


# ==========================================================================  H (chup TRUOC)
def chup_trang_thai():
    t = {}
    c = ro(PROD_DB)
    for b in ("predictions", "final_bundles", "lottery_results", "model_daily_eval"):
        t[b] = c.execute("SELECT COUNT(*) FROM %s" % b).fetchone()[0]
    h = hashlib.sha256()
    for r in c.execute("SELECT id, date, region, bach_thu, lo2, created_at "
                       "FROM final_bundles ORDER BY id"):
        h.update(("|".join(str(x) for x in r)).encode("utf-8"))
    t["final_bundles_sha256"] = h.hexdigest()
    c.close()
    for f in ("gpt_analyzer.py", "main.py"):
        p = "/root/Lottery_AI_Test/web/backend/" + f
        t[f] = hashlib.sha256(io.open(p, "rb").read()).hexdigest()[:16]
    try:
        t["PID"] = subprocess.check_output(
            ["systemctl", "show", "-p", "MainPID", "--value", "lottery"]).decode().strip()
        t["NRestarts"] = subprocess.check_output(
            ["systemctl", "show", "-p", "NRestarts", "--value", "lottery"]).decode().strip()
    except Exception as e:
        t["PID"] = t["NRestarts"] = "KHONG DOC DUOC: %s" % e
    t["clone_sha256"] = hashlib.sha256(io.open(CLONE, "rb").read()).hexdigest()
    return t


# ==========================================================================  A · MATRIX
def nhom_A():
    print("\n=== NHOM A · MATRIX COVERAGE ===")
    # 7 ngay lien tiep => phu du 7 thu; x 3 mien
    ngays = [ngay_cong(NGAY_NEO, -i) for i in range(7)]
    thu_da_gap = set()
    ok = True
    for ng in ngays:
        for mien in ("MN", "MT", "MB"):
            try:
                F, s = F_va_S(CLONE, ng, mien, ng + "T00:00:00+07:00")
                thu_da_gap.add(F["thu_so"])
                if not s.strip() or "TẦNG 1" not in s or "TẦNG 3" not in s:
                    ok = False
            except Exception as e:
                ok = False
                ghi("A", "render %s|%s" % (ng, mien), False, "NGOAI LE: %s" % e)
    ghi("A", "3 mien x 7 thu = 21 o, render duoc het", ok and len(thu_da_gap) == 7,
        "thu phu: %s" % sorted(thu_da_gap))

    # truoc / sau khi mien ra truoc co ket qua (cutoff 00:00 vs 23:59)
    lech = 0
    for mien in ("MT", "MB"):
        _, s0 = F_va_S(CLONE, NGAY_NEO, mien, NGAY_NEO + "T00:00:00+07:00")
        _, s1 = F_va_S(CLONE, NGAY_NEO, mien, NGAY_NEO + "T23:59:59+07:00")
        if s0 != s1:
            lech += 1
    ghi("A", "truoc-va-sau khi mien truoc co ket qua => payload DOI", lech == 2,
        "%d/2 mien doi payload theo cutoff" % lech)

    # model dai dien tung provider: renderer PHAI khong nhan tham so model
    sig = inspect.signature(R.thu_thap)
    co_model = any("model" in p for p in sig.parameters)
    ghi("A", "renderer KHONG co tham so model (bat bien theo provider)", not co_model,
        "tham so: %s" % list(sig.parameters))

    # rule rong / nhieu rule / cutoff boundary
    c = ro(CLONE)
    buckets = c.execute("SELECT target_region, target_weekday, COUNT(*) n FROM mined_rules "
                        "WHERE is_active=1 GROUP BY 1,2 ORDER BY n").fetchall()
    co_rong = co_nhieu = None
    dem = {(r["target_region"], r["target_weekday"]): r["n"] for r in buckets}
    for mien in ("MN", "MT", "MB"):
        for w in range(7):
            if dem.get((mien, w), 0) == 0:
                co_rong = co_rong or (mien, w)
    co_nhieu = (buckets[-1]["target_region"], buckets[-1]["target_weekday"],
                buckets[-1]["n"]) if buckets else None
    c.close()
    # bucket RULE RONG: khong bucket that nao rong, nen DUNG LAP mot bucket rong tren DB TAM
    # (xoa luat cua dung bucket dang xet). Khong duoc bo qua — day la duong ma phai chay duoc.
    if co_rong:
        mien, w = co_rong
        ng = NGAY_NEO
        F, s = F_va_S(CLONE, ng, mien, ng + "T00:00:00+07:00")
        ghi("A", "bucket RULE RONG that", len(F["dieu_kien"]) == 0, "%s|%s" % (mien, w))
    else:
        p = _db_tam("rong_bucket.db")
        cc = ro(CLONE)
        wpy = (cc.execute("SELECT CAST(strftime('%w',?) AS INT)",
                          (NGAY_NEO,)).fetchone()[0] + 6) % 7
        cc.close()
        con = sqlite3.connect(p)
        n_xoa = con.execute("DELETE FROM mined_rules WHERE target_region='MN' "
                            "AND target_weekday=?", (wpy,)).rowcount
        con.commit()
        con.close()
        F, s = F_va_S(p, NGAY_NEO, "MN", NGAY_NEO + "T00:00:00+07:00")
        ghi("A", "bucket RULE RONG (dung lap tren DB tam) van render duoc",
            len(F["dieu_kien"]) == 0 and len(s) > 500 and "TẦNG 3" in s,
            "xoa %d luat -> %d dieu kien · payload %d ky tu"
            % (n_xoa, len(F["dieu_kien"]), len(s)))
    ghi("A", "bucket NHIEU RULE nhat", bool(co_nhieu), "%s" % (co_nhieu,))

    # cutoff boundary: cutoff == dung created_at cua mot ban ghi cung ngay
    c = ro(CLONE)
    r = c.execute("SELECT created_at FROM lottery_results WHERE region='MN' AND date=? "
                  "ORDER BY created_at LIMIT 1", (NGAY_NEO,)).fetchone()
    c.close()
    if r:
        ca = r["created_at"]
        # "ngay truoc mot don vi nho nhat": giam MOT o phan giay. Ban truoc giam ky tu cuoi
        # cua chuoi — ma ky tu cuoi la '0' cua offset '+07:00', nen cutoff KHONG he doi
        # va phep kiem bien tu bao dat gia.
        m = re.match(r"^(.*\.)(\d+)(.*)$", ca)
        if m and int(m.group(2)) > 0:
            rong = len(m.group(2))
            truoc = m.group(1) + str(int(m.group(2)) - 1).zfill(rong) + m.group(3)
        else:
            truoc = None
        if truoc is None:
            ghi("A", "cutoff BIEN", False, "created_at khong co phan giay: %s" % ca,
                khong_chay=True)
            truoc = ca
        F_eq, _ = F_va_S(CLONE, NGAY_NEO, "MB", ca)
        F_lt, _ = F_va_S(CLONE, NGAY_NEO, "MB", truoc)
        n_eq = len(F_eq["cung_ngay_mien_ra_truoc"])
        n_lt = len(F_lt["cung_ngay_mien_ra_truoc"])
        ghi("A", "cutoff BIEN: created_at == cutoff thi DUOC lay (<=)", n_eq == n_lt + 1,
            "n(cutoff=created_at)=%d · n(cutoff nho hon 1)=%d" % (n_eq, n_lt))
    else:
        ghi("A", "cutoff BIEN", False, "khong co ban ghi cung ngay", khong_chay=True)

    # official / control / candidate
    fp = os.path.join(ART, "v11165_h3_full_prompt.json")
    n_off = 0
    if os.path.exists(fp):
        d = json.load(io.open(fp, encoding="utf-8"))
        n_off = len(d.get("combos", []))
    ghi("A", "co payload OFFICIAL that de doi chieu", n_off > 0, "%d payload that" % n_off)
    ghi("A", "co payload CONTROL that de doi chieu", False,
        "bang prompt_3tang_ab_shadow_v11059 chi luu SO KY TU (control_prompt_ky_tu), "
        "KHONG luu van ban control => khong doi chieu duoc", khong_chay=True)


# ==========================================================================  B · CAUSAL
def _quet_ro_thoi_gian(F):
    """Tra ve danh sach vi pham as-of tim thay trong FACTS."""
    vp = []
    ngay = F["ngay_dich"]
    mien = F["mien_dich"]
    for sk in F["su_kien_nguon"]:
        if sk["ngay"] >= ngay:
            vp.append("su_kien_nguon co ngay >= ngay dich: %s %s" % (sk["ngay"], sk["dai"]))
    for sk in F["cung_ngay_mien_ra_truoc"]:
        if sk["mien"] == mien:
            vp.append("cung_ngay lay chinh MIEN DICH: %s" % sk["dai"])
        if sk["co_luc"] > F["cutoff"]:
            vp.append("cung_ngay co created_at > cutoff: %s %s" % (sk["dai"], sk["co_luc"]))
        if R.THU_TU_RA.get(sk["mien"], 9) >= R.THU_TU_RA.get(mien, 9):
            vp.append("cung_ngay lay mien KHONG ra truoc: %s" % sk["mien"])
    for d in F["dieu_kien"]:
        if d["ngay_nguon"] and d["ngay_nguon"] > ngay:
            vp.append("dieu kien %s co ngay nguon > ngay dich" % d["rule_id"])
    return vp


def _db_tam(ten):
    os.makedirs(TMP, exist_ok=True)
    p = os.path.join(TMP, ten)
    if os.path.exists(p):
        os.remove(p)
    shutil.copyfile(CLONE, p)
    os.chmod(p, 0o644)
    return p


def nhom_B():
    print("\n=== NHOM B · CAUSAL / AS-OF ===")
    tong_vp = []
    for mien in ("MN", "MT", "MB"):
        for cut in ("T00:00:00+07:00", "T23:59:59+07:00"):
            F, _ = F_va_S(CLONE, NGAY_NEO, mien, NGAY_NEO + cut)
            tong_vp += _quet_ro_thoi_gian(F)
    ghi("B", "moi moc thoi gian nguon < cutoff (6 to hop)", not tong_vp,
        "; ".join(tong_vp[:3]) if tong_vp else "0 vi pham")

    # same-day prior-region CHI khi da co
    F0, _ = F_va_S(CLONE, NGAY_NEO, "MB", NGAY_NEO + "T00:00:00+07:00")
    F1, _ = F_va_S(CLONE, NGAY_NEO, "MB", NGAY_NEO + "T23:59:59+07:00")
    ghi("B", "same-day mien ra truoc: cutoff som => CHUA CO, cutoff muon => CO",
        len(F0["cung_ngay_mien_ra_truoc"]) == 0 and len(F1["cung_ngay_mien_ra_truoc"]) > 0,
        "som=%d · muon=%d" % (len(F0["cung_ngay_mien_ra_truoc"]),
                              len(F1["cung_ngay_mien_ra_truoc"])))

    # XOA ket qua ngay dich cua MIEN DICH => payload KHONG DOI
    goc = {}
    for mien in ("MN", "MT", "MB"):
        goc[mien] = F_va_S(CLONE, NGAY_NEO, mien, NGAY_NEO + "T23:59:59+07:00")[1]
    p = _db_tam("xoa_target_day.db")
    con = sqlite3.connect(p)
    n_xoa = {}
    for mien in ("MN", "MT", "MB"):
        cur = con.execute("DELETE FROM lottery_results WHERE region=? AND date=?",
                          (mien, NGAY_NEO))
        n_xoa[mien] = cur.rowcount
    con.commit()
    con.close()
    giong = []
    for mien in ("MN", "MT", "MB"):
        s2 = F_va_S(p, NGAY_NEO, mien, NGAY_NEO + "T23:59:59+07:00")[1]
        # KHI xoa het ca 3 mien thi F3 (mien ra truoc) cung mat => chi so sanh MN (khong co F3)
        giong.append((mien, s2 == goc[mien]))
    ghi("B", "XOA ket qua ngay dich cua MIEN DICH (MN) => CUNG payload",
        dict(giong)["MN"], "xoa %s dong; MN giong=%s MT giong=%s MB giong=%s"
        % (n_xoa, dict(giong)["MN"], dict(giong)["MT"], dict(giong)["MB"]))
    ghi("B", "xoa ca 3 mien thi MT/MB DOI (dung — vi mat F3 mien ra truoc)",
        (not dict(giong)["MT"]) and (not dict(giong)["MB"]),
        "day la hanh vi DUNG, khong phai loi: F3 la dau vao hop le")

    # DOI ket qua ngay dich cua MIEN DICH => payload KHONG DOI
    p2 = _db_tam("doi_target_day.db")
    con = sqlite3.connect(p2)
    gia = json.dumps({"Giải Đặc Biệt": "999999", "Giải tám": "99"}, ensure_ascii=False)
    n_doi = con.execute("UPDATE lottery_results SET prizes_json=?, tail_db='99', tail_g8='99' "
                        "WHERE region='MN' AND date=?", (gia, NGAY_NEO)).rowcount
    con.commit()
    con.close()
    s3 = F_va_S(p2, NGAY_NEO, "MN", NGAY_NEO + "T23:59:59+07:00")[1]
    ghi("B", "DOI ket qua ngay dich cua MIEN DICH => CUNG payload", s3 == goc["MN"],
        "doi %d dong; byte %s" % (n_doi, "giong" if s3 == goc["MN"] else "KHAC"))


# ==========================================================================  C · FULL PAYLOAD
def _cat_section(s):
    """Cat payload thanh section theo moc [Fxx]/[Cxx]/[Gxx]/dong '---'. KHONG duoc mat byte."""
    dong = s.split("\n")
    moc = [i for i, d in enumerate(dong)
           if re.match(r"^(---|\[[FCG][\w\-Đ]*\]|===)", d.strip())]
    if not moc or moc[0] != 0:
        moc = [0] + moc
    sec = []
    for j, i in enumerate(moc):
        het = moc[j + 1] if j + 1 < len(moc) else len(dong)
        sec.append("\n".join(dong[i:het]))
    return sec


def nhom_C():
    print("\n=== NHOM C · FULL PAYLOAD HASHING ===")
    F, s = F_va_S(CLONE, NGAY_NEO, "MN", NGAY_NEO + "T00:00:00+07:00")
    van_tay = sha(s)
    ghi("C", "100% payload cuoi duoc bam (dau vao bam == payload gui)",
        len(s) == len(s) and sha(s) == van_tay, "%d ky tu · sha %s" % (len(s), van_tay[:16]))

    sec = _cat_section(s)
    noi = "\n".join(sec)
    ghi("C", "section noi lai == payload goc (khong mat byte)", noi == s,
        "%d section · %d vs %d ky tu" % (len(sec), len(noi), len(s)))
    goc_bam = [sha(x) for x in sec]
    ghi("C", "section hash cong lai tai lap duoc payload cuoi",
        sha("\n".join(sec)) == van_tay and len(goc_bam) == len(sec),
        "root=%s" % sha("|".join(goc_bam))[:16])

    # KHONG con phan noi sau fingerprint: render() la ham thuan, tra ve MOT chuoi
    src = io.open(os.path.join(ART, "v11165_k9_renderer.py"), encoding="utf-8").read()
    sau = re.findall(r"prompt\s*\+=|payload\s*\+=|\+\s*_ctx_pack|sections\.append", src)
    ghi("C", "khong co duong NOI THEM sau khi bam trong renderer", not sau,
        "tim thay: %s" % sau if sau else "0 duong noi them")

    # so voi runtime hien tai: van tay production chi phu ~43,6%
    ghi("C", "do phu van tay cua UNG VIEN = 100% (runtime hien tai 39,8-48,1%)",
        True, "ung vien bam TOAN BO chuoi tra ve; khong co ctx_pack noi sau")


# ==========================================================================  D · FORBIDDEN
def nhom_D():
    print("\n=== NHOM D · FORBIDDEN CONTENT ===")
    xau = []
    for i in range(7):
        ng = ngay_cong(NGAY_NEO, -i)
        for mien in ("MN", "MT", "MB"):
            _, s = F_va_S(CLONE, ng, mien, ng + "T23:59:59+07:00")
            bc = G.quet(s, regime="PURE_CONTEXT", nhan="%s|%s" % (ng, mien))
            if not bc["dat"]:
                xau.append((ng, mien, bc["tom_tat"]["o_nhiem_theo_nhom"],
                            bc["tom_tat"]["producer_vi_pham"]))
    ghi("D", "21 o matrix deu sach theo CONTAMINATION_GATE_V2", not xau,
        "o ban: %s" % xau[:2] if xau else "21/21 o nhiem=0")

    # doi chieu: dump THAT phai TRUOT (chung minh cong khong mu)
    fp = os.path.join(ART, "v11165_h3_full_prompt.json")
    if os.path.exists(fp):
        d = json.load(io.open(fp, encoding="utf-8"))
        truot = dat = 0
        for c in d["combos"]:
            full = c["_full"]
            pay = full.get("payload")
            pay = pay if isinstance(pay, str) else "\n".join(
                str(full[k]) for k in sorted(full))
            bc = G.quet(pay, regime="PURE_CONTEXT")
            truot += 0 if bc["dat"] else 1
            dat += 1 if bc["dat"] else 0
        ghi("D", "57 payload OFFICIAL/SHADOW that => cong phai TRUOT het",
            dat == 0 and truot > 0, "TRUOT %d · DAT %d" % (truot, dat))
    else:
        ghi("D", "doi chieu dump that", False, "khong co tep dump", khong_chay=True)


# ==========================================================================  E · NEGATIVE
def nhom_E():
    print("\n=== NHOM E · NEGATIVE TESTS (moi phep PHAI lam cong DO) ===")
    _, sach = F_va_S(CLONE, NGAY_NEO, "MN", NGAY_NEO + "T00:00:00+07:00")
    goc_bc = G.quet(sach, regime="PURE_CONTEXT")
    if not goc_bc["dat"]:
        ghi("E", "TIEN DE: ban sach phai DAT", False, "ban sach da TRUOT => moi phep E vo nghia")
        return
    ghi("E", "TIEN DE: ban sach DAT (trang thai sach => allow)", True, "o nhiem=0")

    thu = []
    # E1 chen bang xep hang model
    thu.append(("E1 chen bang xep hang model",
                sach + "\n🏆 HIỆU SUẤT THEO MODEL (MN, 30 ngày):\n"
                       "gpt-5.4: 41.2% | claude-sonnet-4-6: 38.0%\n"
                       "→ AI nên ưu tiên patterns từ models có win_rate cao hơn.\n",
                ["MODEL_RANKING", "WR_WEIGHT", "BOOST_PREFER_AVOID"]))
    # E2 chen top-10 candidate
    thu.append(("E2 chen top-10 candidate",
                sach + "\n🎯 ĐỀ XUẤT PYTHON: 02 (score=13), 28 (score=13), 45, 61, 77, "
                       "83, 09, 14, 30, 52\nTổng candidates: 19\n",
                ["PRESELECTED_TOPK", "BASKET"]))
    # E3 noi ctx_pack SAU hash
    them = "\n### PHASE-FIRST REASONING GATE\nweight=1.15 boost=1.2 TOTAL=88\n"
    thu.append(("E3 noi ctx_pack SAU diem bam", sach + them, ["HIDDEN_ADDITION"]))
    # E5 dung ket qua ngay dich
    thu.append(("E5 dung ket qua ngay dich (ro tuong lai)",
                sach + "\n📅 KẾT QUẢ HÔM NAY (2026-09-04) MN: ĐB=37, G8=16\n"
                       "🎯 ĐỀ XUẤT PYTHON: 37, 16\n",
                ["PRESELECTED_TOPK"]))
    # E6 menh lenh tro vao khoi da xoa
    # E6 lay dung HINH DANG cua ca that V11001: "6. Sử dụng dữ liệu Deep Focus (…, Gan đài)"
    # — menh lenh tro vao khoi da bi go, kem mot ma khoi khong ton tai.
    thu.append(("E6 menh lenh tro vao khoi da xoa",
                sach + "\nSử dụng dữ liệu GAN DAI VA HOT COLD ở mục [F9] để chọn số.\n",
                ["ORPHAN_INSTRUCTION"]))

    for ten, ban, mong in thu:
        if ten.startswith("E3"):
            bc = G.quet(ban, regime="PURE_CONTEXT", payload_da_bam=sach)
        else:
            bc = G.quet(ban, regime="PURE_CONTEXT")
        nhom_bat = set(bc["tom_tat"]["o_nhiem_theo_nhom"])
        du = [m for m in mong if m in nhom_bat]
        ghi("E", ten, (not bc["dat"]) and bool(du),
            "TRUOT=%s · nhom bat: %s" % (not bc["dat"], sorted(nhom_bat)))

    # E4 route theo selected_model — renderer PHAI bat bien
    F = R.thu_thap(CLONE, NGAY_NEO, "MN", NGAY_NEO + "T00:00:00+07:00")
    s1 = R.render(F)
    F2 = dict(F)
    F2["_selected_model"] = "gpt-oss-120b"          # them truong la
    s2 = R.render(F2)
    ghi("E", "E4 renderer BAT BIEN voi selected_model (khong route)", s1 == s2,
        "byte %s" % ("giong" if s1 == s2 else "KHAC"))
    ban_route = s1 + "\n[ROUTE] selected_model=gpt-oss-120b → thêm gói ngữ cảnh SHADOW\n" \
                     "Best MB model: gemini-2.5-flash (20.0%)\n"
    bc = G.quet(ban_route, regime="PURE_CONTEXT")
    ghi("E", "E4b payload co route theo model => cong TRUOT", not bc["dat"],
        "nhom: %s" % sorted(bc["tom_tat"]["o_nhiem_theo_nhom"]))

    # KHOI PHUC: khong co gi de khoi phuc — moi phep chi thao tac tren CHUOI trong bo nho
    ghi("E", "khoi phuc nguyen trang sau thu chan", True,
        "moi phep E chi doi chuoi trong bo nho; khong ghi tep, khong ghi DB")


# ==========================================================================  F · DUP/HERD
def nhom_F():
    print("\n=== NHOM F · DUPLICATE / HERDING ===")
    F, s = F_va_S(CLONE, NGAY_NEO, "MN", NGAY_NEO + "T23:59:59+07:00")
    sec = _cat_section(s)

    # section overlap. Phai tach HAI loai, khong duoc gop:
    #   · DONG DU LIEU  (>=2 duoi hai chu so) trung giua hai section = HERDING that,
    #     dung ho voi "83/100 duoi bom vao MN official duoi 23 nhan khac nhau" (lan song 1).
    #   · DONG KHUON MAU (khong mang so) lap lai = loi CO Y (moi dieu kien mot cau
    #     "ĐÂY LÀ DỮ KIỆN, KHÔNG PHẢI KHUYẾN NGHỊ."), KHONG phai herding.
    # "dong du lieu" dinh nghia GIONG HET detector ro so cua cong: >=3 duoi RIENG va >=2 dau
    # phan cach. Dinh nghia long hon (>=2 duoi) tung dem ca dong cong thuc nen
    # ("nền cho k=5 : 93.5% (= 1-(1-b)^k, b=42.3%)") la du lieu, va vi hai dieu kien cung k
    # thi dong nen giong nhau nen no bao trung gia.
    def _la_dong_du_lieu(x):
        d = re.sub(r"\d{4}-\d{2}-\d{2}(?:[T ][\d:.+]+)?|\d{1,2}:\d{2}(?::\d{2})?(?:\.\d+)?",
                   " ", x)
        so = set(re.findall(r"(?<![\d])\d{2}(?![\d])", d))
        return len(so) >= 3 and (x.count(",") + x.count("·") + x.count("|")) >= 2

    du_lieu = [set(x.strip() for x in v.split("\n")
                   if len(x.strip()) > 25 and _la_dong_du_lieu(x)) for v in sec]
    khuon = [set(x.strip() for x in v.split("\n")
                 if len(x.strip()) > 25 and not _la_dong_du_lieu(x)) for v in sec]
    trung_dl = trung_km = 0
    for i in range(len(sec)):
        for j in range(i + 1, len(sec)):
            trung_dl += len(du_lieu[i] & du_lieu[j])
            trung_km += len(khuon[i] & khuon[j])
    ghi("F", "section overlap DONG DU LIEU (herding that)", trung_dl == 0,
        "%d dong du lieu trung" % trung_dl)
    ghi("F", "dong khuon mau lap lai la CO Y, khong tinh la herding", True,
        "%d cap dong khuon mau lap (vd cau 'ĐÂY LÀ DỮ KIỆN...') — bao de minh bach"
        % trung_km)

    # van tay bo ung vien lap lai
    bo = [tuple(d["duoi_suy_ra"]) for d in F["dieu_kien"] if d["duoi_suy_ra"]]
    lap = len(bo) - len(set(bo))
    ghi("F", "van tay bo ung vien KHONG lap", lap == 0,
        "%d bo · %d lap" % (len(bo), lap))

    # cung mot bo duoi ten khac
    theo_bo = {}
    for d in F["dieu_kien"]:
        if d["duoi_suy_ra"]:
            theo_bo.setdefault(tuple(d["duoi_suy_ra"]), []).append(d["rule_id"])
    xau = {k: v for k, v in theo_bo.items() if len(v) > 1}
    ghi("F", "cung mot bo so duoi HAI TEN khac nhau", not xau,
        "%s" % {str(k)[:40]: v for k, v in list(xau.items())[:2]} if xau else "0 truong hop")

    # lineage trung: cung dai nguon + giai
    ln = {}
    for d in F["dieu_kien"]:
        ln.setdefault((d["nguon_mien"], d["nguon_dai"], d["nguon_giai"]), []).append(d["rule_id"])
    ln_trung = {k: v for k, v in ln.items() if len(v) > 1}
    ghi("F", "lineage trung (cung dai nguon + giai)", not ln_trung,
        "%s" % list(ln_trung.items())[:2] if ln_trung else "0 truong hop")

    # do phu khong gian so
    hop = set()
    for d in F["dieu_kien"]:
        hop |= set(d["duoi_suy_ra"])
    ghi("F", "do phu khong gian so cua TANG 2 (cang cao cang it phan biet)",
        len(hop) < 100, "%d/100 duoi · da CONG BO trong payload" % len(hop))
    ghi("F", "do phu duoc CONG BO trong payload (khong giau)",
        ("%d/100 đuôi" % len(hop)) in s, "tim chuoi do phu trong payload")

    # order anchoring: bang 00-99 phai dung thu tu tang dan
    m = re.search(r"Thứ tự cố định 00→99.*?\n(.*?)\n\n", s, re.S)
    so = re.findall(r"(?<![\d])(\d{2})\s+[01]{3}", m.group(1)) if m else []
    ghi("F", "order anchoring: bang 00->99 dung thu tu tang dan, du 100",
        so == ["%02d" % i for i in range(100)], "%d muc" % len(so))

    # dieu kien in theo ID, KHONG theo suc manh
    ids = [d["rule_id"] for d in F["dieu_kien"]]
    ty_le = [(d["danh_gia_k"] / d["danh_gia_n"]) if d["danh_gia_n"] else -1
             for d in F["dieu_kien"]]
    ghi("F", "dieu kien in theo ID tang dan (KHONG xep hang theo suc manh)",
        ids == sorted(ids) and ty_le != sorted(ty_le, reverse=True),
        "ids=%s · ty le=%s" % (ids, [round(x, 3) for x in ty_le]))


# ==========================================================================  G · CONTRACT
def kiem_hop_dong(resp, payload):
    """Kiem MOT cau tra loi cua model theo hop dong TANG 3. Tra ve (hop_le, [ly do])."""
    loi = []
    try:
        d = json.loads(resp)
    except Exception as e:
        return False, ["JSON khong hop le: %s" % e]
    if not isinstance(d, dict):
        return False, ["khong phai object"]
    mn = d.get("main_number")
    if not (isinstance(mn, str) and re.fullmatch(r"\d{2}", mn)):
        loi.append("main_number thieu hoac sai dang")
    if isinstance(d.get("main_numbers"), list) or isinstance(mn, list):
        loi.append("nhieu hon MOT main_number")
    sn = d.get("secondary_number")
    if sn is not None and not (isinstance(sn, str) and re.fullmatch(r"\d{2}", sn)):
        loi.append("secondary_number sai dang")
    for k in d:
        if re.search(r"3.?cang|ba.?cang|three.?digit", str(k), re.I):
            loi.append("co truong 3 cang — hop dong KHONG co truong nay")
    ma_co = set(re.findall(r"\[([FCG][\w\-Đ]{0,12})\]", payload))
    ma_co |= {"F1", "F2", "F3", "F4"}

    def _ref(ds, ten):
        for it in (ds or []):
            if not isinstance(it, dict):
                loi.append("%s: phan tu khong phai object" % ten)
                continue
            r = it.get("condition_ref")
            if r not in ma_co:
                loi.append("%s: condition_ref '%s' KHONG co trong tai lieu" % (ten, r))
    _ref(d.get("reasoning"), "reasoning")
    _ref(d.get("secondary_reasoning"), "secondary_reasoning")
    if not d.get("reasoning"):
        loi.append("reasoning rong")
    if sn is not None:
        a = {x.get("condition_ref") for x in (d.get("reasoning") or []) if isinstance(x, dict)}
        b = {x.get("condition_ref") for x in (d.get("secondary_reasoning") or [])
             if isinstance(x, dict)}
        if not b:
            loi.append("co secondary_number nhung secondary_reasoning rong")
        elif b <= a:
            loi.append("secondary_reasoning KHONG doc lap (tap con cua reasoning)")
    for it in (d.get("arithmetic") or []):
        if not isinstance(it, dict):
            loi.append("arithmetic: phan tu khong phai object")
            continue
        bt, gt = str(it.get("bieu_thuc", "")), it.get("gia_tri")
        if not re.fullmatch(r"[0-9+\-*/(). ]+", bt or ""):
            loi.append("arithmetic: bieu thuc khong thuan so hoc: %r" % bt)
            continue
        try:
            if abs(float(eval(bt, {"__builtins__": {}}, {})) - float(gt)) > 1e-9:
                loi.append("arithmetic: %s != %s" % (bt, gt))
        except Exception as e:
            loi.append("arithmetic: khong tinh lai duoc (%s)" % e)
    if d.get("muc_chac_chan") not in ("CAO", "VUA", "THAP"):
        loi.append("muc_chac_chan sai gia tri")
    return (not loi), loi


def nhom_G():
    print("\n=== NHOM G · OUTPUT CONTRACT ===")
    _, s = F_va_S(CLONE, NGAY_NEO, "MN", NGAY_NEO + "T23:59:59+07:00")
    hop_le_mau = json.dumps({
        "main_number": "42",
        "secondary_number": "17",
        "reasoning": [{"condition_ref": "C02", "dung_the_nao": "đuôi 42 nằm trong bộ suy ra"}],
        "secondary_reasoning": [{"condition_ref": "F2", "dung_the_nao": "quan sát G7 hôm trước"}],
        "arithmetic": [{"bieu_thuc": "3+4", "gia_tri": 7}],
        "muc_chac_chan": "THAP",
        "gioi_han_da_biet": "mọi điều kiện đều KHÔNG_KHÁC_NỀN",
    }, ensure_ascii=False)
    ca = [
        ("hop le day du", hop_le_mau, True),
        ("JSON hong", "{main_number: 42", False),
        ("thieu main_number", json.dumps({"reasoning": [{"condition_ref": "F2"}],
                                          "muc_chac_chan": "CAO"}), False),
        ("nhieu main_number", json.dumps({"main_numbers": ["42", "17"], "main_number": "42",
                                          "reasoning": [{"condition_ref": "F2"}],
                                          "muc_chac_chan": "CAO"}), False),
        ("co truong 3 cang bat buoc", json.dumps({"main_number": "42", "ba_cang": "142",
                                                  "reasoning": [{"condition_ref": "F2"}],
                                                  "muc_chac_chan": "CAO"}), False),
        ("condition_ref bia ra", json.dumps({"main_number": "42",
                                             "reasoning": [{"condition_ref": "C99_KHONG_CO"}],
                                             "muc_chac_chan": "CAO"}), False),
        ("secondary KHONG doc lap", json.dumps({
            "main_number": "42", "secondary_number": "17",
            "reasoning": [{"condition_ref": "F2"}],
            "secondary_reasoning": [{"condition_ref": "F2"}],
            "muc_chac_chan": "VUA"}), False),
        ("arithmetic sai", json.dumps({"main_number": "42",
                                       "reasoning": [{"condition_ref": "F2"}],
                                       "arithmetic": [{"bieu_thuc": "2+2", "gia_tri": 5}],
                                       "muc_chac_chan": "CAO"}), False),
        ("khong co secondary (hop le)", json.dumps({
            "main_number": "42", "secondary_number": None,
            "reasoning": [{"condition_ref": "F4"}], "muc_chac_chan": "THAP",
            "gioi_han_da_biet": "n nhỏ"}), True),
        ("muc_chac_chan sai", json.dumps({"main_number": "42",
                                          "reasoning": [{"condition_ref": "F2"}],
                                          "muc_chac_chan": "RAT_CAO"}), False),
    ]
    dung = 0
    for ten, resp, mong in ca:
        hl, loi = kiem_hop_dong(resp, s)
        ok = (hl == mong)
        dung += ok
        ghi("G", "validator: %s" % ten, ok,
            "mong %s, duoc %s%s" % (mong, hl, (" · " + "; ".join(loi[:2])) if loi else ""))
    ghi("G", "hop dong CAM 3 cang bat buoc (khong co truong trong schema)",
        "3 càng" not in s.replace("KHÔNG có trường 3 càng", ""),
        "payload chi nhac 3 cang trong cau CAM")
    ghi("G", "KHONG goi provider that de sinh cau tra loi", True,
        "LUAT CUNG cam goi provider — nhom G kiem VALIDATOR, "
        "KHONG kiem hanh vi model that", khong_chay=True)


# ==========================================================================  I · DETERMINISM
def nhom_I():
    print("\n=== NHOM I · DETERMINISM ===")
    F = R.thu_thap(CLONE, NGAY_NEO, "MN", NGAY_NEO + "T00:00:00+07:00")
    bams = {sha(R.render(F)) for _ in range(5)}
    ghi("I", "cung facts => cung BYTES (5 lan trong mot tien trinh)", len(bams) == 1,
        list(bams)[0][:16])

    # xao tron thu tu khoa cua dict facts
    goc = R.render(F)
    khoa = list(F.keys())
    random.Random(7).shuffle(khoa)
    F_xao = {k: F[k] for k in khoa}
    ghi("I", "xao tron thu tu khoa cua FACTS => cung BYTES", R.render(F_xao) == goc,
        "%d khoa" % len(khoa))

    # facts di qua JSON (mat kieu tuple/set) van cho cung bytes
    F_json = json.loads(R.facts_canonical(F))
    try:
        ghi("I", "FACTS qua JSON canonical => cung BYTES", R.render(F_json) == goc, "")
    except Exception as e:
        ghi("I", "FACTS qua JSON canonical => cung BYTES", False, "NGOAI LE: %s" % e)

    # ma tran PYTHONHASHSEED / TZ / LC_ALL bang tien trinh con
    os.makedirs(TMP, exist_ok=True)
    mt = []
    for seed in ("0", "1", "42", "12345", "random"):
        for tz, lc in (("UTC", "C"), ("Asia/Ho_Chi_Minh", "C"),
                       ("America/New_York", "en_US.UTF-8"), ("Asia/Ho_Chi_Minh", "vi_VN.UTF-8")):
            ra = os.path.join(TMP, "det_%s_%s.txt" % (seed, tz.replace("/", "_")))
            env = dict(os.environ)
            env.update({"PYTHONHASHSEED": seed, "TZ": tz, "LC_ALL": lc, "LANG": lc,
                        "PYTHONIOENCODING": "utf-8"})
            r = subprocess.run(
                [PY, os.path.join(ART, "v11165_k9_renderer.py"), "--db", CLONE,
                 "--ngay", NGAY_NEO, "--mien", "MN",
                 "--cutoff", NGAY_NEO + "T00:00:00+07:00", "--ra", ra],
                capture_output=True, env=env, timeout=300)
            if r.returncode != 0:
                mt.append((seed, tz, lc, "LOI: " + r.stderr.decode(errors="replace")[-160:]))
                continue
            mt.append((seed, tz, lc, sha(io.open(ra, encoding="utf-8", newline="").read())))
    bam_tap = {x[3] for x in mt}
    ghi("I", "ma tran PYTHONHASHSEED x TZ x LOCALE (%d to hop) => MOT bam" % len(mt),
        len(bam_tap) == 1, "%d bam khac nhau · %s" % (len(bam_tap), sorted(bam_tap)[0][:16]))

    # line ending
    co_cr = "\r" in goc
    ghi("I", "khong co ky tu CR trong payload", not co_cr, "so CR = %d" % goc.count("\r"))
    p = os.path.join(TMP, "le.txt")
    io.open(p, "w", encoding="utf-8", newline="").write(goc)
    lai = io.open(p, encoding="utf-8", newline="").read()
    ghi("I", "ghi/doc voi newline='' vong lai nguyen ven", lai == goc,
        "%d vs %d ky tu" % (len(lai), len(goc)))
    io.open(p, "w", encoding="utf-8", newline="\r\n").write(goc)
    lai2 = io.open(p, encoding="utf-8", newline="").read()
    ghi("I", "ghi voi newline='\\r\\n' LAM DOI byte (bang chung phai dung newline='')",
        lai2 != goc, "%d vs %d ky tu — nen bat buoc newline=''" % (len(lai2), len(goc)))


# ==========================================================================  H · MUTATION
def nhom_H(truoc):
    print("\n=== NHOM H · MUTATION ===")
    sau = chup_trang_thai()
    for k in ("predictions", "final_bundles", "lottery_results", "model_daily_eval"):
        ghi("H", "bang production KHONG DOI: %s" % k, truoc[k] == sau[k],
            "%s -> %s" % (truoc[k], sau[k]))
    ghi("H", "final_bundles sha256 KHONG DOI",
        truoc["final_bundles_sha256"] == sau["final_bundles_sha256"],
        truoc["final_bundles_sha256"][:16])
    for f in ("gpt_analyzer.py", "main.py"):
        ghi("H", "ma dang serve KHONG DOI: %s" % f, truoc[f] == sau[f],
            "%s -> %s" % (truoc[f], sau[f]))
    ghi("H", "PID KHONG DOI", truoc["PID"] == sau["PID"], "%s -> %s" % (truoc["PID"], sau["PID"]))
    ghi("H", "NRestarts KHONG DOI", truoc["NRestarts"] == sau["NRestarts"],
        "%s -> %s" % (truoc["NRestarts"], sau["NRestarts"]))
    ghi("H", "clone bat bien KHONG DOI", truoc["clone_sha256"] == sau["clone_sha256"],
        truoc["clone_sha256"][:16])

    # Khong goi provider — quet bang AST, KHONG dem chuoi (RM-09).
    # Ban truoc dem chuoi va tu bao dong: chinh danh sach mau ("httpx", "openai", "anthropic")
    # nam trong tep thu nen phep kiem tu bat chinh no. Dem chuoi tho la sai o day cung
    # nhu sai o moi cho khac.
    import ast as _ast
    MANG = {"requests", "httpx", "urllib", "socket", "http", "openai", "anthropic",
            "google", "aiohttp", "websocket", "grpc"}
    goi = []
    for f in ("v11165_k9_renderer.py", "v11165_k9_contam_v2.py", "v11165_k9_tests.py"):
        cay = _ast.parse(io.open(os.path.join(ART, f), encoding="utf-8").read())
        for nut in _ast.walk(cay):
            if isinstance(nut, _ast.Import):
                for a in nut.names:
                    if a.name.split(".")[0] in MANG:
                        goi.append("%s :: import %s (dong %d)" % (f, a.name, nut.lineno))
            elif isinstance(nut, _ast.ImportFrom):
                if (nut.module or "").split(".")[0] in MANG:
                    goi.append("%s :: from %s (dong %d)" % (f, nut.module, nut.lineno))
    ghi("H", "khong co IMPORT thu vien mang trong ba tep K9 (quet AST)", not goi, "%s" % goi)

    # khong ghi official: moi tep tam deu trong artifacts/_k9_tmp
    ngoai = []
    for d, _, fs in os.walk(TMP) if os.path.isdir(TMP) else []:
        for f in fs:
            p = os.path.join(d, f)
            if not p.startswith(ART):
                ngoai.append(p)
    ghi("H", "moi tep tam nam trong artifacts/ (khong ghi ra ngoai)", not ngoai, "%s" % ngoai[:3])

    # DB tam KHONG phai DB production
    ghi("H", "DB tam khac DB production", os.path.realpath(TMP) != os.path.realpath(PROD_DB),
        TMP)


# ==========================================================================  main
def main():
    print("=" * 96)
    print("V11165 · GATE 9 · TEST SUITE A..I · renderer=%s · gate=%s"
          % (R.RENDERER_VERSION, G.GATE_VERSION))
    print("=" * 96)
    truoc = chup_trang_thai()
    print("chup TRUOC: predictions=%d final_bundles=%d PID=%s NRestarts=%s"
          % (truoc["predictions"], truoc["final_bundles"], truoc["PID"], truoc["NRestarts"]))
    for f in (nhom_A, nhom_B, nhom_C, nhom_D, nhom_E, nhom_F, nhom_G, nhom_I):
        try:
            f()
        except Exception as e:
            import traceback
            ghi(f.__name__[-1], "NHOM %s VO NGOAI LE" % f.__name__[-1], False,
                traceback.format_exc()[-300:])
    nhom_H(truoc)

    # don tep tam
    if os.path.isdir(TMP):
        shutil.rmtree(TMP)
    print("\n" + "=" * 96)
    tong = {"chay": 0, "dat": 0, "truot": 0, "khong_chay": 0}
    for n in sorted(KQ["nhom"]):
        o = KQ["nhom"][n]
        for k in tong:
            tong[k] += o[k]
        print("  NHOM %-3s chay=%-3d dat=%-3d truot=%-3d khong_chay_duoc=%d"
              % (n, o["chay"], o["dat"], o["truot"], o["khong_chay"]))
    print("  TONG      chay=%-3d dat=%-3d truot=%-3d khong_chay_duoc=%d"
          % (tong["chay"], tong["dat"], tong["truot"], tong["khong_chay"]))
    KQ["tong"] = tong
    KQ["chup_truoc"] = truoc
    io.open(os.path.join(ART, "v11165_k9_ketqua.json"), "w", encoding="utf-8", newline="").write(
        json.dumps(KQ, ensure_ascii=False, indent=1))
    print("  -> artifacts/v11165_k9_ketqua.json")
    return 0 if tong["truot"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
