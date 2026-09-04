# -*- coding: utf-8 -*-
"""V11165 · GATE 12 — CANDIDATE PATCH: TACH KE TOAN "CAP CO Y" KHOI "TRUOT GATE".

TRANG THAI: CANDIDATE — CHUA DEPLOY, CHUA GHI DB, CHUA DE LEN TEP DANG SERVE.
Tep nay nam trong artifacts/. No KHONG import boi bat ky tien trinh production nao.

===========================================================================
VAN DE (do duoc, khong suy dien)
===========================================================================
main.py:9840 `filtered_models.add(_dm)` do MOT tap `filtered_models` cho HAI viec
khac han nhau:
  (a) model TRUOT gate chat luong  (BT/WR gate, main.py:9788 / :9794)
  (b) model bi CAP CO Y theo V10752 (MT giu top-13, owner duyet 25/06)
Hau qua do duoc tren clone bat bien (90 ngay 2026-06-07..2026-09-04):
  - main.py:10511 'wr_gate_filtered': sorted(filtered_models)  => CHUA model bi cap
    tren 70/70 ngay co cap, TRONG KHI gate_diagnostics ghi pass=true cho chinh chung
    (70/70 ngay). Mot payload TU MAU THUAN.
  - main.py:10506 'incomplete_bundle': model_count < EXPECTED_MODEL_COUNT => True
  - database.py:5075 classify_bundle_quality(13, 15) = INCOMPLETE
    => database.py:5085-5087 DEGRADED_LIVE_DAY + EXCLUDE_PRIMARY
       + degradation_reason "Thieu 2 model (13/15)"
  - daily_evaluation.py:140-141 loai ngay EXCLUDE_PRIMARY khoi rolling metrics
    => MT bi loai 72/90 ngay, chuoi 71 ngay lien tiep (26/06..04/09).

===========================================================================
NGUYEN TAC CUA VA — DOC TRUOC KHI SUA
===========================================================================
1. VA CHI DOI KE TOAN, KHONG DOI HANH VI BAU CHON.
   `filtered_models` VAN chua model bi cap (main.py:9860 / :9829 / :10067 doc no
   de bo phieu). Bundle sinh ra phai GIONG HET TUNG BYTE. Neu bo model cap khoi
   `filtered_models` thi 2 model yeu nhat se bo phieu tro lai => DOI OUTPUT
   PRODUCTION => vi pham QD V10752 owner duyet 25/06.
2. Cap co y KHONG phai thieu hut. So model "dang le co" = selected_voters + capped.
3. Gate that bai VAN phai tao INCOMPLETE — khong duoc nhan chim.
===========================================================================
"""
import sys, io, os, json, sqlite3, datetime, argparse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PHIEN_BAN = "V11165-GATE12-CANDIDATE"
NGAY = "2026-09-04"
CLONE = "/root/Lottery_AI_Test/artifacts/v11165_immutable.db"
DICH = "/root/Lottery_AI_Test/artifacts/v11165_h12_patch.py"

REASON_CAP = "max_voters_cap"
REASON_GATE = ("bt_gate", "wr_gate")

# ==========================================================================
# PHAN 1 — HAM THUAN (khong I/O, khong DB) — day la loi cua va
# ==========================================================================


def tach_ke_toan(source_meta, expected=15):
    """Tach 5 truong ke toan tu source_predictions_json.

    Tra ve dict CHi gom truong MOI + wr_gate_filtered DA LAM SACH.
    KHONG dung de doi hanh vi bo phieu.
    """
    sm = source_meta if isinstance(source_meta, dict) else {}
    ev = sm.get("model_exclusion_reasons") or []
    if isinstance(ev, dict):
        ev = [{"model": m, "reason": r, "active": True} for m, r in ev.items()]
    capped, gate_failed, khac = set(), set(), {}
    for e in ev if isinstance(ev, list) else []:
        if not isinstance(e, dict) or e.get("active") is False:
            continue
        m = e.get("model")
        if not m:
            continue
        r = str(e.get("reason") or "").lower()
        if r == REASON_CAP:
            capped.add(str(m))
        elif r in REASON_GATE or "bt_gate" in r or "wr_gate" in r:
            gate_failed.add(str(m))
        else:
            khac.setdefault(r, set()).add(str(m))

    # gate_diagnostics la nguon doc lap ve pass/fail (main.py:9797-9804)
    gd = sm.get("gate_diagnostics")
    gd_fail = set()
    gd_pass = set()
    if isinstance(gd, dict):
        for m, v in gd.items():
            if not isinstance(v, dict):
                continue
            (gd_pass if v.get("pass") else gd_fail).add(str(m))
    # hop nhat: gate_failed lay tu SU KIEN, doi chieu voi gate_diagnostics
    gate_failed |= gd_fail

    # model bi cap MA gate_diagnostics ghi pass=true -> bang chung tron lan
    tron_lan = sorted(capped & gd_pass)

    old_wgf = sm.get("wr_gate_filtered") or []
    if not isinstance(old_wgf, list):
        old_wgf = []
    old_wgf = {str(x) for x in old_wgf if x}

    selected = sm.get("total_models")
    if selected is None:
        selected = sm.get("scoreable_model_count")
    selected = int(selected or 0)

    oer = sm.get("output_eligible_row_count")
    oer = int(oer) if oer is not None else None

    # so model DANG LE co mat neu khong cap co y
    hieu_luc = selected + len(capped)

    return {
        # --- 5 truong owner yeu cau tach ---
        "expected_output_models": int(expected),
        "gate_passed_models": (oer - len(gate_failed)) if oer is not None else None,
        "capped_models": sorted(capped),
        "capped_model_count": len(capped),
        "selected_voters": selected,
        "gate_failed_models": sorted(gate_failed),
        "gate_failed_model_count": len(gate_failed),
        # --- dan xuat ---
        "effective_model_count": hieu_luc,
        "wr_gate_filtered": sorted(old_wgf - capped),   # DA LAM SACH
        "wr_gate_filtered_truoc_va": sorted(old_wgf),
        "capped_but_gate_pass": tron_lan,
        "exclusion_reason_khac": {k: sorted(v) for k, v in khac.items()},
        "output_eligible_row_count": oer,
        "incomplete_bundle": hieu_luc < int(expected),
        "incomplete_bundle_truoc_va": selected < int(expected),
        "cap_policy_ref": "V10752 · owner duyet 25/06/2026 · MT top-13",
    }


def classify_bundle_quality_v2(selected_voters, capped_model_count, expected=15):
    """Ban va cua database.py:5028-5047.

    KHAC DUY NHAT: cap co y KHONG tinh la thieu hut.
    expected <= 0 -> COMPLETE (giu nguyen hanh vi cu).
    """
    if expected <= 0:
        return "COMPLETE"
    hieu_luc = int(selected_voters) + int(capped_model_count or 0)
    ratio = hieu_luc / expected
    if ratio >= 1.0:
        return "COMPLETE"
    elif ratio >= 0.50:
        return "INCOMPLETE"
    return "DEGRADED"


def classify_day_status_v2(selected_voters, capped_models, expected=15):
    """Ban va cua database.py:5075-5091. Tra ve du 5 truong de ghi day_governance."""
    capped_models = list(capped_models or [])
    ncap = len(capped_models)
    q = classify_bundle_quality_v2(selected_voters, ncap, expected)
    hieu_luc = int(selected_voters) + ncap
    thieu = max(0, int(expected) - hieu_luc)
    if q == "COMPLETE":
        st, pol = "VALID_LIVE_DAY", "INCLUDE"
        ly_do = (None if ncap == 0 else
                 "Du %d/%d model hop le; %d model bi CAP CO Y (%s) theo V10752 — "
                 "khong phai thieu hut" % (hieu_luc, expected, ncap,
                                           ", ".join(sorted(capped_models))))
    elif q == "INCOMPLETE":
        st, pol = "DEGRADED_LIVE_DAY", "EXCLUDE_PRIMARY"
        ly_do = "Thieu %d model (%d/%d hop le)" % (thieu, hieu_luc, expected)
        if ncap:
            ly_do += " · rieng %d model bi CAP CO Y V10752 KHONG tinh la thieu" % ncap
    else:
        st, pol = "INVALID_FOR_PRIMARY_EVAL", "EXCLUDE_ALL"
        ly_do = "Nghiem trong: chi %d/%d model hop le" % (hieu_luc, expected)
        if ncap:
            ly_do += " (da tru %d model CAP CO Y)" % ncap
    return {
        "bundle_quality": q,
        "day_status": st,
        "evaluation_policy": pol,
        "expected_model_count": int(expected),
        "completed_model_count": hieu_luc,       # DA cong lai model bi cap co y
        "selected_voters": int(selected_voters),  # so model THUC SU bo phieu
        "capped_model_count": ncap,
        "capped_models": sorted(capped_models),
        "failed_model_count": thieu,
        "completeness_ratio": round(hieu_luc / expected, 4) if expected > 0 else 1.0,
        "degradation_reason": ly_do,
    }


# ==========================================================================
# PHAN 2 — BA KHOI VA (TRUOC / SAU / PHIEN BAN / KIEM) theo §60.4
# ==========================================================================

VA = [
{
 "tep": "web/backend/main.py",
 "dong": "9823-9847",
 "ten": "VA-1 — theo dau model bi CAP rieng, KHONG doi hanh vi bo phieu",
 "TRUOC": """    _MAX_VOTERS_BY_REGION = {"MT": 13}
    _cap = _MAX_VOTERS_BY_REGION.get(region)
    if _cap:
        ...
            for _dm in _cap_ranked[_cap:]:
                filtered_models.add(_dm)
                model_exclusion_events.append({...\"reason\": \"max_voters_cap\"...})""",
 "SAU": """    _capped_models = set()          # V11165: tap RIENG cho cap co y
    _MAX_VOTERS_BY_REGION = {"MT": 13}
    _cap = _MAX_VOTERS_BY_REGION.get(region)
    if _cap:
        ...
            for _dm in _cap_ranked[_cap:]:
                filtered_models.add(_dm)   # GIU NGUYEN — bo phieu khong doi
                _capped_models.add(_dm)    # V11165: chi de KE TOAN
                model_exclusion_events.append({...\"reason\": \"max_voters_cap\"...})""",
 "vi_sao": "Bo `filtered_models.add(_dm)` se cho 2 model yeu nhat bo phieu tro lai "
           "=> doi output production => vi pham QD V10752. Chi THEM mot tap song song.",
 "rui_ro": "KHONG. `_capped_models` chi duoc doc o VA-2.",
},
{
 "tep": "web/backend/main.py",
 "dong": "10506 · 10511 (+ 5 truong moi)",
 "ten": "VA-2 — tach 5 truong ke toan trong source_predictions_json",
 "TRUOC": """        'incomplete_bundle': model_count < EXPECTED_MODEL_COUNT,
        'wr_gate_filtered': sorted(filtered_models) if filtered_models else [],""",
 "SAU": """        # V11165: cap co y KHONG phai thieu hut
        'incomplete_bundle': (model_count + len(_capped_models)) < EXPECTED_MODEL_COUNT,
        'wr_gate_filtered': sorted(filtered_models - _capped_models)
                            if (filtered_models - _capped_models) else [],
        # --- 5 truong ke toan MOI (V11165) ---
        'expected_output_models': EXPECTED_MODEL_COUNT,
        'gate_passed_models': len({p.get('ai_model') for p in raw_predictions
                                   if p.get('ai_model')})
                              - len(filtered_models - _capped_models),
        'capped_models': sorted(_capped_models),
        'capped_model_count': len(_capped_models),
        'selected_voters': model_count,
        'gate_failed_models': sorted(filtered_models - _capped_models),
        'cap_policy_ref': 'V10752 · owner duyet 25/06/2026 · MT top-13',""",
 "vi_sao": "wr_gate_filtered la thu duoc DOC o main.py:489 (_quality_filtered_models_"
           "from_source_meta) · main.py:11346 (gate_filtered_models) · "
           "web/frontend/du-doan.html:1354 (hien thi UI). Lam sach mot cho chua ca ba.",
 "rui_ro": "main.py:502 chi nap them su kien reason bt_gate/wr_gate, KHONG nap "
           "max_voters_cap => sau va, ca ba diem doc deu sach. Da quet §60.2.",
},
{
 "tep": "web/backend/database.py",
 "dong": "5028-5047 · 5074-5091",
 "ten": "VA-3 — classify_day_status doc so model bi cap tu bundle",
 "TRUOC": """    expected = EXPECTED_MODEL_COUNT
    quality = classify_bundle_quality(model_count, expected)
    ...
    elif quality == 'INCOMPLETE':
        day_status = 'DEGRADED_LIVE_DAY'
        eval_policy = 'EXCLUDE_PRIMARY'
        reason = f'Thiếu {failed} model ({model_count}/{expected})'""",
 "SAU": """    expected = EXPECTED_MODEL_COUNT
    # V11165: doc so model bi CAP CO Y tu bundle cua chinh ngay/mien do
    cursor.execute("SELECT source_predictions_json FROM final_bundles "
                   "WHERE date=? AND region=? AND status='ACTIVE'",
                   (date_str, region.upper()))
    _r = cursor.fetchone()
    _capped = []
    if _r and _r['source_predictions_json']:
        try:
            _sm = json.loads(_r['source_predictions_json'])
            _capped = sorted({e.get('model') for e in
                              (_sm.get('model_exclusion_reasons') or [])
                              if isinstance(e, dict)
                              and e.get('reason') == 'max_voters_cap'
                              and e.get('model')})
        except Exception:
            _capped = []
    effective = model_count + len(_capped)
    quality = classify_bundle_quality(effective, expected)
    failed = max(0, expected - effective)
    ...  # reason ghi ro phan nao la cap co y""",
 "vi_sao": "scheduler.py:1670/1739/1811 goi `_cds(today, region, source='auto_verify')` "
           "KHONG truyen model_count => sua trong ham la du, KHONG phai sua caller.",
 "rui_ro": "Doc them 1 SELECT trong ham da mo connection. Neu bundle thieu/loi JSON "
           "thi _capped=[] => hanh vi VE DUNG NHU TRUOC VA (fail-safe ve phia cu).",
},
]

# ==========================================================================
# PHAN 3 — TEST
# ==========================================================================


def _sm(oer, total, ev, gd=None, wgf=None):
    return {"output_eligible_row_count": oer, "total_models": total,
            "scoreable_model_count": total, "model_exclusion_reasons": ev,
            "gate_diagnostics": gd or {}, "wr_gate_filtered": wgf or []}


def chay_test():
    kq = []

    def ok(ten, dieu_kien, chi_tiet=""):
        kq.append({"test": ten, "dat": bool(dieu_kien), "chi_tiet": chi_tiet})
        print(("  DAT  " if dieu_kien else "  HONG ") + ten + ("  " + chi_tiet if chi_tiet else ""))

    print("=== TEST A — CHi CAP CO Y (ca MT 04/09 that) ===")
    ev = [{"model": "meta-learning", "reason": "max_voters_cap", "active": True},
          {"model": "random-forest", "reason": "max_voters_cap", "active": True}]
    gd = {m: {"pass": True} for m in
          ["meta-learning", "random-forest", "lstm", "smart-ensemble"]}
    a = tach_ke_toan(_sm(15, 13, ev, gd, ["meta-learning", "random-forest"]), 15)
    d = classify_day_status_v2(13, a["capped_models"], 15)
    ok("A1 selected_voters=13", a["selected_voters"] == 13, str(a["selected_voters"]))
    ok("A2 capped_model_count=2", a["capped_model_count"] == 2)
    ok("A3 gate_failed_models RONG", a["gate_failed_models"] == [], str(a["gate_failed_models"]))
    ok("A4 wr_gate_filtered SACH (khong con capped)", a["wr_gate_filtered"] == [],
       str(a["wr_gate_filtered"]))
    ok("A5 incomplete_bundle=False", a["incomplete_bundle"] is False)
    ok("A6 day_status=VALID_LIVE_DAY", d["day_status"] == "VALID_LIVE_DAY", d["day_status"])
    ok("A7 evaluation_policy=INCLUDE", d["evaluation_policy"] == "INCLUDE")
    ok("A8 bat duoc bang chung tron lan truoc va",
       a["capped_but_gate_pass"] == ["meta-learning", "random-forest"])
    ok("A9 truoc va incomplete_bundle=True (chung minh va co tac dung)",
       a["incomplete_bundle_truoc_va"] is True)

    print("=== TEST B — CHi TRUOT GATE THAT (khong cap) ===")
    ev = [{"model": "gpt-5.4", "reason": "wr_gate", "detail": "wr<28", "active": True},
          {"model": "glm-5.1", "reason": "bt_gate", "detail": "bt<14", "active": True}]
    gd = {"gpt-5.4": {"pass": False}, "glm-5.1": {"pass": False},
          "lstm": {"pass": True}}
    b = tach_ke_toan(_sm(15, 13, ev, gd, ["glm-5.1", "gpt-5.4"]), 15)
    d = classify_day_status_v2(13, b["capped_models"], 15)
    ok("B1 capped RONG", b["capped_models"] == [])
    ok("B2 gate_failed = 2", b["gate_failed_model_count"] == 2, str(b["gate_failed_models"]))
    ok("B3 wr_gate_filtered GIU NGUYEN 2 model",
       b["wr_gate_filtered"] == ["glm-5.1", "gpt-5.4"], str(b["wr_gate_filtered"]))
    ok("B4 incomplete_bundle=True", b["incomplete_bundle"] is True)
    ok("B5 day_status=DEGRADED_LIVE_DAY", d["day_status"] == "DEGRADED_LIVE_DAY")
    ok("B6 evaluation_policy=EXCLUDE_PRIMARY", d["evaluation_policy"] == "EXCLUDE_PRIMARY")
    ok("B7 gate_passed_models=13", b["gate_passed_models"] == 13, str(b["gate_passed_models"]))

    print("=== TEST C — CA HAI: 1 truot gate + 1 cap ===")
    ev = [{"model": "gpt-5.4", "reason": "wr_gate", "detail": "wr<28", "active": True},
          {"model": "lstm", "reason": "max_voters_cap", "active": True}]
    gd = {"gpt-5.4": {"pass": False}, "lstm": {"pass": True}}
    cc = tach_ke_toan(_sm(15, 13, ev, gd, ["gpt-5.4", "lstm"]), 15)
    d = classify_day_status_v2(13, cc["capped_models"], 15)
    ok("C1 capped=['lstm']", cc["capped_models"] == ["lstm"])
    ok("C2 gate_failed=['gpt-5.4']", cc["gate_failed_models"] == ["gpt-5.4"])
    ok("C3 wr_gate_filtered chi con gpt-5.4", cc["wr_gate_filtered"] == ["gpt-5.4"])
    ok("C4 effective=14 < 15 => incomplete_bundle=True", cc["incomplete_bundle"] is True,
       "effective=%s" % cc["effective_model_count"])
    ok("C5 VAN EXCLUDE_PRIMARY (gate fail that KHONG bi nhan chim)",
       d["evaluation_policy"] == "EXCLUDE_PRIMARY", d["degradation_reason"])
    ok("C6 failed_model_count=1 (khong phai 2)", d["failed_model_count"] == 1)

    print("=== TEST D — MODEL KHONG RA OUTPUT (thieu THAT) + cap ===")
    ev = [{"model": "lstm", "reason": "max_voters_cap", "active": True}]
    dd = tach_ke_toan(_sm(14, 13, ev, {"lstm": {"pass": True}}, ["lstm"]), 15)
    d = classify_day_status_v2(13, dd["capped_models"], 15)
    ok("D1 effective=14 => VAN EXCLUDE_PRIMARY", d["evaluation_policy"] == "EXCLUDE_PRIMARY",
       d["degradation_reason"])
    ok("D2 gate_passed_models=14 (output 14, gate fail 0)", dd["gate_passed_models"] == 14)

    print("=== TEST E — HOI QUY: mien KHONG cap (MN/MB) phai GIONG HET truoc va ===")
    ev = [{"model": "gpt-5.4", "reason": "wr_gate", "active": True}]
    e = tach_ke_toan(_sm(15, 14, ev, {"gpt-5.4": {"pass": False}}, ["gpt-5.4"]), 15)
    d = classify_day_status_v2(14, e["capped_models"], 15)
    ok("E1 wr_gate_filtered KHONG doi", e["wr_gate_filtered"] == e["wr_gate_filtered_truoc_va"])
    ok("E2 incomplete_bundle KHONG doi",
       e["incomplete_bundle"] == e["incomplete_bundle_truoc_va"] is True)
    ok("E3 evaluation_policy = EXCLUDE_PRIMARY nhu cu", d["evaluation_policy"] == "EXCLUDE_PRIMARY")

    print("=== TEST F — BIEN: khong co bundle / JSON hong => quay ve hanh vi CU ===")
    f = tach_ke_toan(None, 15)
    ok("F1 source_meta=None khong no", f["capped_models"] == [] and f["selected_voters"] == 0)
    f2 = classify_day_status_v2(13, [], 15)
    ok("F2 khong co cap => EXCLUDE_PRIMARY y het truoc va",
       f2["evaluation_policy"] == "EXCLUDE_PRIMARY" and f2["failed_model_count"] == 2)

    print("=== TEST G — expected<=0 giu nguyen hanh vi cu ===")
    ok("G1 expected=0 -> COMPLETE", classify_bundle_quality_v2(0, 0, 0) == "COMPLETE")

    n_dat = sum(1 for x in kq if x["dat"])
    print("\nTONG: %d/%d DAT" % (n_dat, len(kq)))
    return kq, n_dat == len(kq)


# ==========================================================================
# PHAN 4 — TAI LAP LICH SU OFFLINE tren CLONE BAT BIEN
# ==========================================================================


def chay_replay(clone=CLONE):
    c = sqlite3.connect("file:%s?mode=ro" % clone, uri=True)
    c.row_factory = sqlite3.Row
    doi, giu = [], 0
    theo_mien = {}
    for g in c.execute("SELECT * FROM day_governance ORDER BY date, region"):
        b = c.execute("SELECT source_predictions_json FROM final_bundles "
                      "WHERE date=? AND region=? AND status='ACTIVE'",
                      (g["date"], g["region"])).fetchone()
        sm = {}
        if b and b["source_predictions_json"]:
            try:
                sm = json.loads(b["source_predictions_json"])
            except Exception:
                sm = {}
        a = tach_ke_toan(sm, g["expected_model_count"] or 15)
        d = classify_day_status_v2(g["completed_model_count"] or 0,
                                   a["capped_models"], g["expected_model_count"] or 15)
        r = theo_mien.setdefault(g["region"], {"tong": 0, "doi": 0, "cap_ngay": 0,
                                               "tron_lan_ngay": 0})
        r["tong"] += 1
        if a["capped_models"]:
            r["cap_ngay"] += 1
        if a["capped_but_gate_pass"]:
            r["tron_lan_ngay"] += 1
        if d["evaluation_policy"] != g["evaluation_policy"]:
            r["doi"] += 1
            doi.append({"date": g["date"], "region": g["region"],
                        "truoc": g["evaluation_policy"], "sau": d["evaluation_policy"],
                        "mc": g["completed_model_count"], "capped": a["capped_models"],
                        "gate_failed": a["gate_failed_models"]})
        else:
            giu += 1
    return {"so_dong_doi": len(doi), "so_dong_giu": giu,
            "theo_mien": theo_mien, "chi_tiet_doi": doi}


ROLLBACK = """
ROLLBACK — CHINH XAC BA BUOC, KHONG CAN BACKFILL
 1. main.py: xoa dong `_capped_models = set()` va `_capped_models.add(_dm)`;
    tra 'incomplete_bundle' ve `model_count < EXPECTED_MODEL_COUNT`;
    tra 'wr_gate_filtered' ve `sorted(filtered_models)`;
    xoa 6 khoa moi (expected_output_models · gate_passed_models · capped_models ·
    capped_model_count · selected_voters · gate_failed_models · cap_policy_ref).
 2. database.py: xoa khoi doc source_predictions_json trong classify_day_status;
    tra `quality = classify_bundle_quality(model_count, expected)` va
    `failed = max(0, expected - model_count)`.
 3. Chay lai `classify_day_status(date, region)` cho cac ngay bi anh huong de
    day_governance tro ve nhan cu — HOAC khong lam gi: cac dong cu van con nguyen
    vi va CHI ghi khi cron verify chay lai.
 KHONG CAN dung service. KHONG CAN sua DB bang tay. KHONG CO migration schema
 (source_predictions_json la JSON tu do; day_governance khong them cot nao).
 Hash 4 bang khoa KHONG doi boi va nay: predictions / final_bundles /
 lottery_results / model_daily_eval — va chi doi NOI DUNG JSON cua ban ghi MOI
 va nhan trong day_governance (bang thu 5, khong thuoc bo 4 bang khoa).
"""

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--replay", action="store_true")
    ap.add_argument("--rollback", action="store_true")
    ap.add_argument("--cai-dat", action="store_true",
                    help="chep chinh no vao artifacts/v11165_h12_patch.py")
    ap.add_argument("--out", default="/root/Lottery_AI_Test/artifacts/v11165_h12_patch_kq.json")
    a = ap.parse_args()
    if not (a.test or a.replay or a.rollback or a.cai_dat):
        a.test = a.replay = a.rollback = a.cai_dat = True

    KQ = {"phien_ban": PHIEN_BAN, "ngay": NGAY, "trang_thai": "CANDIDATE_KHONG_DEPLOY",
          "va": VA}

    if a.cai_dat:
        src = io.open(os.path.abspath(__file__), encoding="utf-8").read()
        io.open(DICH, "w", encoding="utf-8", newline="").write(src)
        print("DA CHEP CANDIDATE PATCH ->", DICH)
        KQ["duong_dan_patch"] = DICH

    if a.test:
        print("\n" + "=" * 70)
        print("TEST")
        print("=" * 70)
        kq, tat_ca_dat = chay_test()
        KQ["test"] = {"chi_tiet": kq, "tat_ca_dat": tat_ca_dat,
                      "so_dat": sum(1 for x in kq if x["dat"]), "so_test": len(kq)}

    if a.replay:
        print("\n" + "=" * 70)
        print("REPLAY LICH SU OFFLINE tren CLONE BAT BIEN")
        print("=" * 70)
        rp = chay_replay()
        KQ["replay"] = rp
        print("  so dong day_governance DOI nhan :", rp["so_dong_doi"])
        print("  so dong GIU nguyen              :", rp["so_dong_giu"])
        for m, v in sorted(rp["theo_mien"].items()):
            print("   %-3s tong=%-4d doi=%-4d ngay_co_cap=%-4d ngay_tron_lan=%d"
                  % (m, v["tong"], v["doi"], v["cap_ngay"], v["tron_lan_ngay"]))

    if a.rollback:
        print(ROLLBACK)
        KQ["rollback"] = ROLLBACK.strip()

    io.open(a.out, "w", encoding="utf-8", newline="").write(
        json.dumps(KQ, ensure_ascii=False, indent=1, default=str))
    print("\nGHI:", a.out)
