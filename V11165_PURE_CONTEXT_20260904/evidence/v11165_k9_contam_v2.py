# -*- coding: utf-8 -*-
"""V11165 · GATE 9 · VIEC 2 — CONTAMINATION_GATE_V2 (UNG VIEN, CHUA DEPLOY)

Thay bo 5 dau MU CAU TRUC cua V11160 (`_dau_o_nhiem` gpt_analyzer.py:6712), bo do bao
0/5 "sach" trong khi payload that con `weight=` 33/33 luot, `Best MB model` 11/33,
`AI token models 14d WR` 11/33.

BA KHAC BIET CAN BAN so voi bo cu
  1. DO TREN DUMP THAT, khong dem chuoi tren MA NGUON. Dau vao la chuoi payload da dump
     tu ham dang serve (RM-14), khong phai tep .py.
  2. PHAN LOAI, KHONG DEM CHUOI THO (RM-09 · §60.3). Moi lan khop deu di qua bo phan loai
     ngu canh: KHANG_DINH / PHU_DINH / DINH_NGHIA_HOP_DONG. Chi KHANG_DINH moi tinh la
     o nhiem. Mot dong "CẤM viện dẫn tỉ lệ thắng" KHONG phai o nhiem — no la LUAT CAM.
  3. CO DETECTOR CAU TRUC, khong chi tu khoa. Ro so chon san bi bat bang HINH DANG
     (mot dong co >=3 duoi hai chu so, tap con thuc su cua 00-99, nam duoi mot tieu de),
     nen doi ten khoi hay doi nhan KHONG lam no tang hinh — day dung la cach
     `_V10768_HERD_SECTION_KEYS` da bo sot "### 🔴 MB HARD MODE" hai lan.

DANH SACH BAT-BUOC-VANG-MAT lay tu 35 producer cua lan song 1
(artifacts/v11165_h4_set_to_condition.json), theo REGIME:
  PURE_CONTEXT     : moi producer disposition DROP_* / BLOCK_* PHAI VANG
  OFFICIAL_LEGACY  : khong cam gi — dung de CHUNG MINH cong khong mu (phai TRUOT)

Dung:
    from v11165_k9_contam_v2 import quet, REGIME
    bc = quet(payload_text, regime="PURE_CONTEXT")
    bc["dat"]  -> True/False
"""
import re, json, unicodedata

GATE_VERSION = "V11165_K9_CONTAM_V2"

# --------------------------------------------------------------------- phan loai ngu canh
DAU_PHU_DINH = [
    "không", "khong", "cấm", "cam ", "tuyệt đối không", "không được", "không có",
    "không chứa", "không phải", "chưa", "loại bỏ", "đã gỡ", "không dùng", "no ",
]
DAU_HOP_DONG = [
    "hợp đồng", "ràng buộc", "contract", "schema", "trường bắt buộc", "trả về",
    "giới hạn của tài liệu",
]


def _bochu(s):
    """Bo dau tieng Viet + ha chu thuong — de mot mau bat duoc ca ban co dau va khong dau."""
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if unicodedata.category(ch) != "Mn")
    return s.replace("đ", "d").replace("Đ", "D").lower()


def _phan_loai(cau):
    """RM-09: tra ve KHANG_DINH | PHU_DINH | DINH_NGHIA_HOP_DONG cho MOT cau chua no."""
    c = _bochu(cau)
    if any(_bochu(x) in c for x in DAU_HOP_DONG) and any(_bochu(x) in c for x in DAU_PHU_DINH):
        return "DINH_NGHIA_HOP_DONG"
    if any(_bochu(x) in c for x in DAU_PHU_DINH):
        return "PHU_DINH"
    return "KHANG_DINH"


def _cau_chua(text, vt):
    """Lay cau/dong chua vi tri vt — de phan loai theo NGU CANH chu khong theo tu don."""
    d0 = text.rfind("\n", 0, vt) + 1
    d1 = text.find("\n", vt)
    if d1 < 0:
        d1 = len(text)
    return text[d0:d1]


# --------------------------------------------------------------------- detector tu khoa
# moi detector: (ma, nhom, [mau regex tren ban DA BO DAU], mo ta)
DETECTOR = [
    ("D01", "MODEL_RANKING", [
        r"hieu suat theo model", r"model ranking", r"best\s+(mb|mn|mt)\s+model",
        r"bang xep hang model", r"xep hang model", r"models co win_rate",
        r"(gpt|claude|gemini|grok|deepseek|llama|qwen|mistral|sonnet|opus|haiku)[-\w.]*\s*[:\(]?\s*\d+([.,]\d+)?\s*%",
    ], "bang xep hang / hieu suat theo ten model"),
    ("D02", "WR_WEIGHT", [
        r"win\s*rate", r"\bwr\b", r"win_rate", r"weight\s*=", r"trong so\s*[:=]",
        r"\d+d\s*wr", r"hit\s*rate\s*[:=]", r"do tin cay weights",
    ], "ti le thang / trong so"),
    ("D03", "TOTAL_FINAL", [
        r"\btotal\b", r"\bfinal\b", r"tong diem", r"diem cuoi", r"diem tong",
    ], "diem tong / diem cuoi"),
    ("D04", "RECENT_WINNING_OUTPUT", [
        r"so da trung gan day", r"lich su du doan cua ban", r"digit sum \(winning\)",
        r"final_bundle", r"bach_thu", r"→\s*win\b", r"->\s*win\b",
        r"status\s*=\s*(win|lose|partial)", r"trung:\s*\[",
    ], "ket qua/du doan cu cua chinh he thong"),
    ("D05_TU", "PRESELECTED_TOPK", [
        r"de xuat python", r"top\s*\d+\s*goi y", r"shortlist", r"tong candidates",
        r"so nen tranh", r"top-?k", r"danh sach chot", r"so chot",
    ], "ro so chon san — bat bang tu khoa"),
    ("D06", "BOOST_PREFER_AVOID", [
        r"boost\s*=", r"boost\s*[:x]", r"uu tien", r"nen chon", r"khong nen chon",
        r"nen tranh", r"loai khoi reasoning", r"trong so cao", r"uu tien tuyet doi",
        r"hay thay doi chien luoc", r"giam ky vong",
    ], "menh lenh uu tien / tranh"),
    ("D09", "CONTRADICTION", [], "hai cau trong cung prompt bao nguoc nhau"),
    ("D10", "MODEL_META_KHAC", [
        r"gan cao", r"\bhot\b", r"overdue", r"sap ve", r"hot by gap", r"cold\b",
        r"just_hit", r"over_hot", r"consensus_level", r"model_count",
    ], "khoi meta/nhan da bi owner bac"),
]

# cap mau NGUOC NHAU — PRJ_PROMPT_CONTRADICTS
CAP_MAU_THUAN = [
    (r"gan cao khong co nghia sap ra", r"overdue \(sap ve\)|sap ve\)|so sap den chu ky ve",
     "phu dinh 'gan => sap ra' nhung van in nhan '(sap ve)'"),
    (r"overdue", r"hot by gap",
     "gap DAI => se ra  vs  gap NGAN => dang nong — hai chieu nguoc nhau"),
    (r"moi luot xo (la )?doc lap|moi ky xo doc lap|su kien doc lap",
     r"just_hit|over_hot|da het luot|den han",
     "khang dinh doc lap nhung van dung tien de 'da het luot'"),
]

# 35 producer lan song 1 — nhan hien thi de nhan dien tren DUMP, kem disposition
# nguon: artifacts/v11165_h4_set_to_condition.json (gate H4, lan song 1)
PRODUCER = [
    ("P01_TOP5_GOI_Y", "RENDER_FULL_UNIVERSE_SYMMETRICALLY", [r"top 5 goi y"]),
    ("P02_GAN_CAO", "DROP_UNSUPPORTED", [r"gan cao"]),
    ("P03_HOT", "DROP_UNSUPPORTED", [r"🔥\s*hot:", r"\bhot:\s*\d\d"]),
    ("P04_TANG", "TRANSLATE_TO_NEUTRAL_CONDITION", [r"📈\s*tang:"]),
    ("P05_DOW_HAY_RA", "DROP_DUPLICATE", [r"hay ra:"]),
    ("P06_DO_TIN_CAY_WEIGHTS", "DROP_MODEL_META", [r"do tin cay weights"]),
    ("P07_DE_XUAT_PYTHON", "BLOCK_ORACLE", [r"de xuat python", r"tong candidates"]),
    ("P08_SO_NEN_TRANH", "DROP_UNSUPPORTED", [r"so nen tranh"]),
    ("P09_MIRROR_PAIRS", "RENDER_FULL_UNIVERSE_SYMMETRICALLY", [r"mirror pairs", r"dao guong"]),
    ("P10_LICH_SU_DU_DOAN_CUA_BAN", "DROP_MODEL_META",
     [r"lich su du doan cua ban", r"wr hien tai"]),
    ("P11_OVERDUE_SAP_VE", "DROP_UNSUPPORTED", [r"overdue", r"sap ve"]),
    ("P12_HOT_BY_GAP", "DROP_UNSUPPORTED", [r"hot by gap"]),
    ("P13_DIGIT_SUM_WINNING", "DROP_MODEL_META", [r"digit sum \(winning\)"]),
    ("P14_TOP_POSITIONS", "RENDER_FULL_UNIVERSE_SYMMETRICALLY", [r"top positions"]),
    ("P15_CAP_DOI", "TRANSLATE_TO_NEUTRAL_CONDITION",
     [r"cap doi hay di cung", r"significant_pairs"]),
    ("P16_KET_QUA_NGAY_TRUOC", "KEEP_RAW_FACT", [r"ket qua ngay truoc"]),
    ("P17_LICH_SU_DAI", "KEEP_RAW_FACT", [r"\(3 ky gan nhat\)"]),
    ("P18_KB_PATTERN_DAI", "BLOCK_AMBIGUOUS", [r"knowledge base", r"top tails\(freq\)"]),
    ("P19_KB_DOW", "BLOCK_AMBIGUOUS", [r"dow pattern"]),
    ("P20_TAN_SUAT_DUOI_5_GIAI", "DROP_DUPLICATE", [r"tan suat duoi \(5 giai"]),
    ("P21_MINED_RULES", "TRANSLATE_TO_NEUTRAL_CONDITION", [r"mined rules"]),
    ("P22_RULE_TAILS", "DROP_DUPLICATE", [r"rule tails", r"cross-region:"]),
    ("P23_EVIDENCE_WINDOWS", "TRANSLATE_TO_NEUTRAL_CONDITION", [r"windows:\s*1w"]),
    ("P24_EVIDENCE_SOURCE_PRIZE", "TRANSLATE_TO_NEUTRAL_CONDITION", [r"\[top\]\s*m[bnt]\("]),
    ("P25_BOI_CANH_SOI_CAU", "TRANSLATE_TO_NEUTRAL_CONDITION", [r"boi canh soi cau"]),
    ("P26_CONVERGENCE_TRAP", "TRANSLATE_TO_NEUTRAL_CONDITION", [r"convergence trap"]),
    ("P27_SHADOW_BLOCKS", "DROP_DUPLICATE", [r"block 2 — source-prize", r"source-prize direction"]),
    ("P28_ANTITRAP_SPEND", "TRANSLATE_TO_NEUTRAL_CONDITION", [r"chua bi tieu o mien ra truoc"]),
    ("P29_D1_POOL_COUNT", "EXPOSE_VIA_REAL_QUERY_TOOL", [r"d-1 cross-region tail pool"]),
    ("P30_WEEKDAY_SCAN_LIVINGNESS", "TRANSLATE_TO_NEUTRAL_CONDITION",
     [r"song manh", r"huong dan ai"]),
    ("P31_PHASE11_MODEL_META", "DROP_MODEL_META",
     [r"hieu suat gan day", r"so da trung gan day"]),
    ("P32_PHASE14A_MODEL_RANKING", "DROP_MODEL_META", [r"hieu suat theo model"]),
    ("P33_LANE_TEST_D1_BUNDLE", "SHADOW_HYPOTHESIS_ONLY",
     [r"d-1 final_bundle", r"union pool", r"predictions_per_model_lag1"]),
    ("P34_MB_RULE_STACK_PROD_MANUAL", "TRANSLATE_TO_NEUTRAL_CONDITION", [r"mb rule stack"]),
    ("P35_MB_HARD_MODE_MODEL_META", "DROP_MODEL_META", [r"mb hard mode"]),
]

REGIME = {
    # regime -> (nhom detector BAT BUOC PHAI VANG, disposition producer PHAI VANG)
    "PURE_CONTEXT": (
        ["MODEL_RANKING", "WR_WEIGHT", "TOTAL_FINAL", "RECENT_WINNING_OUTPUT",
         "PRESELECTED_TOPK", "BOOST_PREFER_AVOID", "CONTRADICTION", "MODEL_META_KHAC",
         "ORPHAN_INSTRUCTION", "HIDDEN_ADDITION", "BASKET"],
        ["DROP_UNSUPPORTED", "DROP_DUPLICATE", "DROP_MODEL_META",
         "BLOCK_ORACLE", "BLOCK_AMBIGUOUS", "SHADOW_HYPOTHESIS_ONLY"],
    ),
    "OFFICIAL_LEGACY": ([], []),
}


# --------------------------------------------------------------------- detector cau truc
RE_TIEU_DE = re.compile(r"^[#\s]*[^\n]{0,120}[:：]\s*$|^#{1,6}\s+\S|^[🎯🔥⏳📈📅⛔🔴🟢📊🏆📋🚨💡↗️🥶♨️]", re.M)
RE_DUOI = re.compile(r"(?<![\d])\d{2}(?![\d])")


RE_SO_DAI = re.compile(r"\d{3,}")
# moc thoi gian KHONG PHAI danh sach duoi. "2026-09-04T16:39:39.159644+07:00" tung bi doc
# thanh sau duoi (09 04 16 39 07 00) va lam cong bao o nhiem gia o ca MT lan MB.
RE_MOC_TG = re.compile(
    r"\d{4}-\d{2}-\d{2}(?:[T ]\d{1,2}:\d{2}(?::\d{2})?(?:\.\d+)?)?(?:[+-]\d{2}:?\d{2}|Z)?"
    r"|\d{1,2}:\d{2}(?::\d{2})?(?:\.\d+)?"
    r"|[+-]\d{2}:\d{2}")


def _bo_moc_tg(d):
    return RE_MOC_TG.sub(" ", d)


def _la_chuyen_vi_su_kien(d, rieng):
    """Phan biet RO SO CHON SAN voi RENDER CUA SU KIEN GOC — theo XUAT XU, khong theo nhan.

    Mot dong la CHUYEN VI CUA SU KIEN GOC khi moi duoi tren dong deu SUY RA DUOC tu chinh
    dong do:
      (a) dong co mui ten dan xuat `→`/`->` va ve phai la tap con cua {2 chu so cuoi cua
          cac so o ve trai}  — vd "Giải tư  06742, 49522  → đuôi: 42, 22";
      (b) hoac moi duoi deu la hau to cua mot so DAI hon co mat tren cung dong.

    Vi sao dung XUAT XU: de giau mot ro so chon san qua phep kiem nay, ke viet prompt buoc
    phai in ca so nguon sinh ra dung nhung duoi ay — luc do no DA LA su kien goc that.
    Nhan/tieu de KHONG duoc dung lam can cu (do la cho `_V10768_HERD_SECTION_KEYS` da bo
    sot "### 🔴 MB HARD MODE" hai lan).
    """
    for mt in ("→", "->"):
        if mt in d:
            trai, phai = d.split(mt, 1)
            so_trai = RE_SO_DAI.findall(trai) + RE_DUOI.findall(trai)
            if so_trai:
                hau_to = set(x[-2:] for x in so_trai)
                phai_duoi = set(RE_DUOI.findall(phai))
                if phai_duoi and phai_duoi <= hau_to:
                    return True
    dai = RE_SO_DAI.findall(d)
    if dai:
        hau_to = set(x[-2:] for x in dai)
        if set(rieng) <= hau_to:
            return True
    return False


def _bat_ro_so(text):
    """DETECTOR CAU TRUC: mot dong liet ke >=3 duoi hai chu so, va tap ay la TAP CON THUC SU
    cua 00-99 => day la RO SO DA CHON SAN. Doi ten khoi khong lam no tang hinh.

    Bo qua: bang FULL-UNIVERSE (>=95 duoi khac nhau) · dong khong phai liet ke ·
    dong la CHUYEN VI CUA SU KIEN GOC (xem `_la_chuyen_vi_su_kien`).
    Moi lan bo qua VAN duoc ghi vao bien ban voi phan_loai rieng — cam im lang tra ve 0,
    do dung la loi cua bo 5 dau V11160.
    """
    ra = []
    for i, dong in enumerate(text.split("\n")):
        d = dong.strip()
        if not d or len(d) < 6:
            continue
        d_so = _bo_moc_tg(d)          # gat moc thoi gian TRUOC khi bat duoi
        so = RE_DUOI.findall(d_so)
        if len(so) < 3:
            continue
        rieng = sorted(set(so))
        if len(rieng) >= 95:          # bang full-universe — doi xung, khong phai ro chon san
            continue
        # phai co dau hieu LIET KE (dau phay / gach dau dong) chu khong phai cau van
        if d.count(",") + d.count("·") + d.count("|") < 2:
            continue
        pl = "SU_KIEN_GOC" if _la_chuyen_vi_su_kien(d_so, rieng) else _phan_loai(d)
        ra.append({"dong": i + 1, "n_duoi_rieng": len(rieng), "trich": d[:160],
                   "phan_loai": pl})
    return ra


# tu ra lenh (ban DA BO DAU) va tu chi KHOI — menh lenh mo coi phai co CA HAI
RE_DONG_TU = re.compile(r"\b(dung|su dung|tham khao|xem|theo|ket hop|doc|ap dung|dua vao)\b")
RE_TU_KHOI = re.compile(r"\b(du lieu|khoi|bang|muc|phan|section|tang|danh sach)\b")
# ten khoi viet HOA: it nhat HAI tu hoa lien tiep — mot tu hoa don le hau het la tu chuc nang
# ("KHONG", "CAM", "PHAI") va tung lam detector bao gia tren chinh ban ung vien.
RE_TEN_HOA = re.compile(r"\b[A-ZÀ-ỸĐ][A-ZÀ-ỸĐ0-9/]{1,}(?:\s+[A-ZÀ-ỸĐ][A-ZÀ-ỸĐ0-9/]{1,}){1,7}\b")
RE_MA_KHOI = re.compile(r"\[([A-ZĐ][\w\-Đ]{0,14})\]")


def _bat_menh_lenh_mo_coi(text):
    """PRJ_PROMPT_DANGLING: menh lenh tro vao mot KHOI KHONG CO trong chinh payload.

    HAI DANG THAM CHIEU, xu rieng:
      · dang 1 — MA KHOI trong ngoac vuong: `[F2]`, `[C07]`. Moi ma duoc VIEN DAN phai
        cung la ma duoc DINH NGHIA (co dong tieu de mo dau bang ma do).
      · dang 2 — TEN KHOI viet hoa sau MOT dong tu ra lenh VA mot tu chi khoi
        (vd "Sử dụng dữ liệu GAN ĐÀI", "tham khảo khối HOT/COLD").
        Doi HAI dieu kien la co chu dich: ban truoc chi doi dong tu, nen no bao gia ngay
        tren cau "bạn tự cân nhắc dùng hay bỏ" cua chinh ban ung vien.
    """
    dong = text.split("\n")
    dinh_nghia, nhan = set(), set()
    for d in dong:
        s = d.strip()
        if not s:
            continue
        m = RE_MA_KHOI.match(s)
        if m:
            dinh_nghia.add(m.group(1))
        if RE_TIEU_DE.match(s) or s.startswith("[") or s.startswith("#"):
            nhan.add(_bochu(re.sub(r"[^\w\sÀ-ỹ]", " ", s)).strip())
    nhan_gop = " || ".join(sorted(nhan))
    mo_coi = []
    for i, d in enumerate(dong):
        s = d.strip()
        if RE_MA_KHOI.match(s):        # dong DINH NGHIA khoi thi khong phai vien dan
            vien = set(RE_MA_KHOI.findall(s[s.index("]") + 1:]))
        else:
            vien = set(RE_MA_KHOI.findall(s))
        for ma in sorted(vien):
            if ma not in dinh_nghia:
                mo_coi.append({"dong": i + 1, "tro_toi": "[%s]" % ma, "dang": "MA_KHOI",
                               "trich": s[:160], "phan_loai": _phan_loai(d)})
        dn = _bochu(d)
        if not (RE_DONG_TU.search(dn) and RE_TU_KHOI.search(dn)):
            continue
        for m in RE_TEN_HOA.finditer(d):
            ten = m.group(0).strip(" .,:;")
            if len(ten) < 6:
                continue
            if _bochu(ten) in nhan_gop:
                continue
            mo_coi.append({"dong": i + 1, "tro_toi": ten[:80], "dang": "TEN_HOA",
                           "trich": s[:160], "phan_loai": _phan_loai(d)})
    return mo_coi


def _bat_them_an(payload_gui, payload_da_bam):
    """HIDDEN_ADDITION: phan van ban duoc NOI THEM sau diem bam van tay.

    Day chinh la lo hong V11165 L5 do duoc: van tay runtime chi phu 39,8-48,1% payload,
    thieu 26.478-35.315 ky tu MOI LUOT. Cong nay bat duoc 100% phan thua.
    """
    if payload_da_bam is None:
        return {"do_duoc": False, "ly_do": "khong truyen payload_da_bam"}
    if payload_gui.startswith(payload_da_bam):
        thua = payload_gui[len(payload_da_bam):]
    else:
        thua = None
    return {
        "do_duoc": True,
        "ky_tu_gui": len(payload_gui),
        "ky_tu_da_bam": len(payload_da_bam),
        "ky_tu_thua": (len(thua) if thua is not None else
                       len(payload_gui) - len(payload_da_bam)),
        "la_hau_to": thua is not None,
        "do_phu_pct_x100": (len(payload_da_bam) * 10000 // len(payload_gui)) if payload_gui else 0,
        "trich_thua": (thua[:400] if thua else None),
    }


# --------------------------------------------------------------------- cong chinh
def quet(payload, regime="PURE_CONTEXT", payload_da_bam=None, nhan=None):
    """Quet MOT payload that. Tra ve bien ban day du, khong chi con so."""
    if regime not in REGIME:
        raise ValueError("regime la, phai thuoc %s" % list(REGIME))
    nhom_cam, disp_cam = REGIME[regime]
    p = _bochu(payload)
    bien_ban = {
        "gate": GATE_VERSION, "regime": regime, "nhan": nhan,
        "ky_tu": len(payload), "byte": len(payload.encode("utf-8")),
        "phat_hien": [], "producer_co_mat": [], "tom_tat": {},
    }

    # --- detector tu khoa, CO PHAN LOAI (RM-09) ---
    for ma, nhom, maus, mo_ta in DETECTOR:
        for mau in maus:
            for m in re.finditer(mau, p):
                cau = _cau_chua(payload, m.start())
                pl = _phan_loai(cau)
                bien_ban["phat_hien"].append({
                    "ma": ma, "nhom": nhom, "mau": mau, "mo_ta": mo_ta,
                    "vi_tri": m.start(), "trich": cau.strip()[:160], "phan_loai": pl,
                    "tinh_la_o_nhiem": bool(pl == "KHANG_DINH" and nhom in nhom_cam),
                })

    # --- mau thuan trong cung payload (PRJ_PROMPT_CONTRADICTS) ---
    # HAI VE deu phai la KHANG_DINH moi la mau thuan that. Mot ve nam trong cau PHU DINH
    # ("Không có cơ chế 'đến hạn phải ra'") la LUAT CAM, khong phai mau thuan — day chinh
    # la loi duong tinh gia bat duoc khi hieu chuan ban dau tren ung vien.
    for a, b, mo_ta in CAP_MAU_THUAN:
        cap = None
        for ma_ in re.finditer(a, p):
            cau_a = _cau_chua(payload, ma_.start())
            if _phan_loai(cau_a) != "KHANG_DINH":
                continue
            for mb_ in re.finditer(b, p):
                cau_b = _cau_chua(payload, mb_.start())
                if _phan_loai(cau_b) != "KHANG_DINH":
                    continue
                if cau_a.strip() == cau_b.strip():
                    continue          # cung MOT cau thi khong the nguoc voi chinh no
                cap = (ma_, cau_a, cau_b)
                break
            if cap:
                break
        if cap:
            ma_, cau_a, cau_b = cap
            bien_ban["phat_hien"].append({
                "ma": "D09", "nhom": "CONTRADICTION", "mau": "%s  <>  %s" % (a, b),
                "mo_ta": mo_ta, "vi_tri": ma_.start(),
                "trich": cau_a.strip()[:110] + "  ||  " + cau_b.strip()[:110],
                "phan_loai": "KHANG_DINH",
                "tinh_la_o_nhiem": "CONTRADICTION" in nhom_cam,
            })

    # --- detector cau truc: ro so chon san ---
    for r in _bat_ro_so(payload):
        bien_ban["phat_hien"].append({
            "ma": "D05_CT", "nhom": "BASKET", "mau": "cau truc: >=3 duoi, tap con thuc su",
            "mo_ta": "ro so da chon san (bat bang hinh dang, khong bang ten khoi)",
            "vi_tri": r["dong"], "trich": r["trich"], "phan_loai": r["phan_loai"],
            "n_duoi_rieng": r["n_duoi_rieng"],
            "tinh_la_o_nhiem": bool(r["phan_loai"] == "KHANG_DINH" and "BASKET" in nhom_cam),
        })

    # --- menh lenh mo coi ---
    for r in _bat_menh_lenh_mo_coi(payload):
        bien_ban["phat_hien"].append({
            "ma": "D07", "nhom": "ORPHAN_INSTRUCTION",
            "mau": "menh lenh tro vao khoi khong co trong payload",
            "mo_ta": "PRJ_PROMPT_DANGLING (%s)" % r["dang"], "vi_tri": r["dong"],
            "trich": r["trich"], "tro_toi": r["tro_toi"], "phan_loai": r["phan_loai"],
            "tinh_la_o_nhiem": bool(r["phan_loai"] == "KHANG_DINH"
                                    and "ORPHAN_INSTRUCTION" in nhom_cam),
        })

    # --- them an sau diem bam ---
    ta = _bat_them_an(payload, payload_da_bam)
    bien_ban["them_an"] = ta
    if ta.get("do_duoc") and ta.get("ky_tu_thua", 0) > 0:
        bien_ban["phat_hien"].append({
            "ma": "D08", "nhom": "HIDDEN_ADDITION",
            "mau": "payload_gui != payload_da_bam",
            "mo_ta": "co %d ky tu duoc noi SAU diem bam van tay" % ta["ky_tu_thua"],
            "vi_tri": ta["ky_tu_da_bam"], "trich": (ta.get("trich_thua") or "")[:160],
            "phan_loai": "KHANG_DINH",
            "tinh_la_o_nhiem": "HIDDEN_ADDITION" in nhom_cam,
        })

    # --- doi chieu 35 producer ---
    for pid, disp, maus in PRODUCER:
        vt = None
        for mau in maus:
            m = re.search(mau, p)
            if m:
                vt = m.start()
                break
        if vt is None:
            continue
        cau = _cau_chua(payload, vt)
        pl = _phan_loai(cau)
        bien_ban["producer_co_mat"].append({
            "producer_id": pid, "disposition": disp, "vi_tri": vt,
            "trich": cau.strip()[:140], "phan_loai": pl,
            "vi_pham": bool(disp in disp_cam and pl == "KHANG_DINH"),
        })

    # --- tong hop ---
    on = [x for x in bien_ban["phat_hien"] if x["tinh_la_o_nhiem"]]
    pd = [x for x in bien_ban["phat_hien"] if x["phan_loai"] == "PHU_DINH"]
    hd = [x for x in bien_ban["phat_hien"] if x["phan_loai"] == "DINH_NGHIA_HOP_DONG"]
    sg = [x for x in bien_ban["phat_hien"] if x["phan_loai"] == "SU_KIEN_GOC"]
    vp_prod = [x for x in bien_ban["producer_co_mat"] if x["vi_pham"]]
    theo_nhom = {}
    for x in on:
        theo_nhom[x["nhom"]] = theo_nhom.get(x["nhom"], 0) + 1
    bien_ban["tom_tat"] = {
        "tong_lan_khop": len(bien_ban["phat_hien"]),
        "o_nhiem_KHANG_DINH": len(on),
        "bo_qua_PHU_DINH": len(pd),
        "bo_qua_HOP_DONG": len(hd),
        "bo_qua_SU_KIEN_GOC": len(sg),
        "o_nhiem_theo_nhom": dict(sorted(theo_nhom.items())),
        "producer_co_mat": len(bien_ban["producer_co_mat"]),
        "producer_vi_pham": [x["producer_id"] for x in vp_prod],
    }
    bien_ban["dat"] = bool(not on and not vp_prod)
    bien_ban["ly_do_truot"] = ([x["ma"] + ":" + x["nhom"] for x in on[:20]]
                               + ["PRODUCER:" + x["producer_id"] for x in vp_prod[:20]])
    return bien_ban


def in_gon(bc):
    t = bc["tom_tat"]
    return ("[%s] %s · %s · %d ky tu · o nhiem=%d "
            "(bo qua: phu dinh=%d, hop dong=%d, su kien goc=%d) · producer vi pham=%d · %s"
            % (bc["gate"], bc.get("nhan") or "-", bc["regime"], bc["ky_tu"],
               t["o_nhiem_KHANG_DINH"], t["bo_qua_PHU_DINH"], t["bo_qua_HOP_DONG"],
               t["bo_qua_SU_KIEN_GOC"], len(t["producer_vi_pham"]),
               "DAT" if bc["dat"] else "TRUOT"))


if __name__ == "__main__":
    import sys, io, argparse
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("tep")
    ap.add_argument("--regime", default="PURE_CONTEXT")
    a = ap.parse_args()
    s = io.open(a.tep, encoding="utf-8").read()
    bc = quet(s, regime=a.regime, nhan=a.tep)
    print(in_gon(bc))
    print(json.dumps(bc["tom_tat"], ensure_ascii=False, indent=1))
