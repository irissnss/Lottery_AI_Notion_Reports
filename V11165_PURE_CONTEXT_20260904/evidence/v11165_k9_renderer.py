# -*- coding: utf-8 -*-
"""V11165 · GATE 9 · VIEC 1 — PURE_CONTEXT_RENDERER (UNG VIEN, CHUA DEPLOY)

TEP MOI trong artifacts/. KHONG deploy · KHONG sua tep dang serve · KHONG ghi DB.

Sinh prompt BA TANG tu FACTS + CONDITIONS + CONTRACT theo dinh nghia owner:
  RAW_NUMBER_FACT      = so trong ket qua lich su/su kien nguon that, kem ngay, mien, dai,
                         giai, bo, cutoff.
  CONDITION            = menh de co pham vi, dau vao, phep bien doi, cutoff, nen, co mau,
                         do bat dinh, trang thai bang chung. CONDITION KHONG PHAI RECOMMENDATION.
  PURE CONTEXT         = raw facts + neutral conditions + reasoning/output contract.

RANG BUOC THIET KE (rang buoc nao cung co phep kiem trong v11165_k9_tests.py):
  R1  khong preselected basket — khong top-k, khong shortlist, khong "de xuat"
  R2  khong rank — moi tap deu in theo THU TU CO DINH (so tang dan / id tang dan)
  R3  khong boost — khong he so nhan, khong diem cong, khong trong so
  R4  khong model-meta — khong ten model, khong win rate, khong TOTAL/FINAL,
      khong output cu cua chinh he
  R5  full-universe 00->99 khi can, CHI boolean/categorical flag
  R6  deterministic: cung facts + schema + version => cung BYTES
  R7  moi CONDITION deu co NEN DUNG CHO CHINH THUOC DO no (RM-18: bo k duoi dung 1-(1-b)^k;
      RM-21: b do lai cho chinh mien x thu dang xet, KHONG muon hang so cua thuoc khac)
  R8  as-of tuyet doi: moc thoi gian cua MOI nguon < cutoff; ket qua cung ngay cua mien ra
      truoc CHI duoc dung khi da thuc su co (created_at <= cutoff)
  R9  khong menh lenh "tu truy van" — duong goi khong co tool (do duoc o lan song 1, L6)

KIEN TRUC HAI NUA — de kiem duoc tinh tat dinh va tinh as-of tach roi nhau:
  thu_thap(...)  -> dict FACTS thuan du lieu (cham DB, doc-only)
  render(facts)  -> str    (HAM THUAN: khong DB, khong dong ho, khong bien moi truong)

Chay thu:
  python3 v11165_k9_renderer.py --ngay 2026-09-04 --mien MN
"""
import sys, io, os, json, math, sqlite3, hashlib, argparse

SCHEMA_VERSION = "PC-1.0"
RENDERER_VERSION = "V11165_K9_PURE_CONTEXT_RENDERER"
CLONE_MAC_DINH = "/root/Lottery_AI_Test/artifacts/v11165_immutable.db"

# thu tu giai CO DINH — quyet dinh byte dau ra, cam sap xep theo dict order
THU_TU_GIAI = [
    "Giải Đặc Biệt", "Giải nhất", "Giải nhì", "Giải ba", "Giải tư",
    "Giải năm", "Giải sáu", "Giải bảy", "Giải tám",
]
THU_VN = ["Chủ Nhật", "Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy"]
MIEN_TEN = {"MB": "MIỀN BẮC", "MT": "MIỀN TRUNG", "MN": "MIỀN NAM"}
# thu tu ra trong ngay — dung de biet mien nao "ra truoc"
THU_TU_RA = {"MN": 1, "MT": 2, "MB": 3}

NHAN_BANG_CHUNG = {
    "KHONG_DU_MAU": "KHÔNG_ĐỦ_MẪU — chưa được phép kết luận",
    "KHONG_KHAC_NEN": "KHÔNG_KHÁC_NỀN",
    "KHAC_NEN_DUONG": "KHÁC_NỀN_DƯƠNG",
    "KHAC_NEN_AM": "KHÁC_NỀN_ÂM",
}
N_TOI_THIEU = 20  # duoi muc nay ghi KHONG_DU_MAU (RM-04: n nho la "chua duoc phep ket luan")


# ----------------------------------------------------------------------------- so hoc tat dinh
def pm(k, n):
    """Ti le theo PHAN NGHIN, so nguyen — tranh moi khac biet dau phay dong/locale (R6)."""
    if n <= 0:
        return None
    return (2 * k * 1000 + n) // (2 * n)


def pm_str(v):
    if v is None:
        return "n/a"
    return "%d.%d%%" % (v // 10, v % 10)


def wilson_pm(k, n, z=1.96):
    """Khoang tin cay Wilson, tra ve (thap_pm, cao_pm) theo phan nghin, lam tron nguyen."""
    if n <= 0:
        return (None, None)
    p = float(k) / float(n)
    z2 = z * z
    mau = 1.0 + z2 / n
    tam = (p + z2 / (2.0 * n)) / mau
    nua = (z * math.sqrt(p * (1.0 - p) / n + z2 / (4.0 * n * n))) / mau
    lo = max(0.0, tam - nua)
    hi = min(1.0, tam + nua)
    return (int(lo * 1000 + 0.5), int(hi * 1000 + 0.5))


def nen_bo_k(b_pm, k):
    """RM-18: nen dung cho BO k DUOI la 1-(1-b)^k, KHONG phai nen cua 1 so."""
    if b_pm is None or k <= 0:
        return None
    b = b_pm / 1000.0
    return int((1.0 - (1.0 - b) ** k) * 1000 + 0.5)


def duoi(s):
    s = str(s).strip()
    return s[-2:].zfill(2) if s else None


# ----------------------------------------------------------------------------- thu thap FACTS
def _mo(db_path):
    c = sqlite3.connect("file:%s?mode=ro" % db_path, uri=True)
    c.row_factory = sqlite3.Row
    return c


def _tach_giai(prizes_json):
    """prizes_json -> [(ten_giai, [so, ...]), ...] theo THU TU GIAI CO DINH."""
    try:
        d = json.loads(prizes_json) if prizes_json else {}
    except Exception:
        return []
    if not isinstance(d, dict):
        return []
    ra, da = [], set()
    for g in THU_TU_GIAI:
        if g in d:
            v = d[g]
            ra.append((g, [str(x) for x in (v if isinstance(v, list) else [v])]))
            da.add(g)
    for g in sorted(k for k in d.keys() if k not in da):   # khoa la -> sap xep, van tat dinh
        v = d[g]
        ra.append((g, [str(x) for x in (v if isinstance(v, list) else [v])]))
    return ra


def _duoi_cua_ky(prizes_json):
    ra = set()
    for _, sos in _tach_giai(prizes_json):
        for s in sos:
            t = duoi(s)
            if t and t.isdigit():
                ra.add(t)
    return ra


def thu_thap(db_path, ngay_dich, mien_dich, cutoff_iso, so_ngay_su_kien=3,
             so_tuan_nen=26, so_tuan_lich=8):
    """Doc DB (READ-ONLY) va tra ve dict FACTS. MOI truy van deu co chan as-of (R8).

    cutoff_iso: moc chot, dang ISO co offset — vd '2026-09-05T05:00:00+07:00'.
                Ban ghi cung ngay cua mien ra truoc CHI duoc lay khi created_at <= cutoff_iso.
    """
    c = _mo(db_path)
    F = {
        "schema": SCHEMA_VERSION,
        "renderer": RENDERER_VERSION,
        "ngay_dich": ngay_dich,
        "mien_dich": mien_dich,
        "cutoff": cutoff_iso,
        "nguon_db": os.path.basename(db_path),
    }
    wd = c.execute("SELECT CAST(strftime('%w', ?) AS INT)", (ngay_dich,)).fetchone()[0]
    F["thu_so"] = wd
    F["thu_ten"] = THU_VN[wd]
    # ⚠️ HAI QUY UOC THU KHAC NHAU TRONG CUNG MOT KHO — cho nay tung lam sai ca tang 2.
    #   · SQLite strftime('%w')      : 0=Chu Nhat … 5=Thu Sau … 6=Thu Bay   (dung cho THU_VN)
    #   · mined_rules.target_weekday : 0=Thu Hai  … 4=Thu Sau … 6=Chu Nhat  (Python weekday())
    # Bang chung: luat id=2835 co target_weekday=6, source_weekday=5,
    #   source_station_slot='MT(D-1/T7) · Da Nang'  => 5 phai la THU BAY (T7) => quy uoc Python.
    #   Va mined_rule_effectiveness cua nhom target_weekday=5 roi vao cac ngay THU BAY.
    # Lay nham quy uoc = lay NHAM CA BUCKET LUAT (lech mot ngay), va vi dai nguon khong xo
    # vao ngay do nen MOI dieu kien ra RONG — hong am, khong co trieu chung.
    wd_py = (wd + 6) % 7
    F["thu_so_python"] = wd_py
    F["quy_uoc_thu"] = ("strftime('%%w')=%d (0=CN) cho hien thi · mined_rules.weekday=%d "
                        "(0=T2, Python) cho tra luat" % (wd, wd_py))

    # --- F1 lich dai: SUY TU LICH SU (date < ngay_dich), khong doc bang lich tuong lai ---
    lich = {}
    for mien in ("MN", "MT", "MB"):
        rows = c.execute(
            "SELECT station, COUNT(*) n, MAX(date) d FROM lottery_results "
            "WHERE region=? AND date < ? AND CAST(strftime('%w', date) AS INT)=? "
            "AND date >= date(?, ?) GROUP BY station ORDER BY station",
            (mien, ngay_dich, wd, ngay_dich, "-%d days" % (so_tuan_lich * 7))).fetchall()
        lich[mien] = [{"dai": r["station"], "so_ky_quan_sat": r["n"], "ky_gan_nhat": r["d"]}
                      for r in rows]
    F["lich_dai_suy_tu_lich_su"] = lich
    F["cua_so_suy_lich"] = "%d tuần gần nhất, chỉ dùng bản ghi date < %s" % (so_tuan_lich, ngay_dich)

    # --- F2 ket qua cac ky TRUOC ngay dich (3 mien) ---
    su_kien = []
    for mien in ("MN", "MT", "MB"):
        rows = c.execute(
            "SELECT date, region, station, prizes_json FROM lottery_results "
            "WHERE region=? AND date < ? AND date >= date(?, ?) "
            "ORDER BY date DESC, station ASC",
            (mien, ngay_dich, ngay_dich, "-%d days" % so_ngay_su_kien)).fetchall()
        for r in rows:
            su_kien.append({
                "ngay": r["date"], "mien": r["region"], "dai": r["station"],
                "giai": [[g, so] for g, so in _tach_giai(r["prizes_json"])],
            })
    su_kien.sort(key=lambda x: (x["ngay"], THU_TU_RA.get(x["mien"], 9), x["dai"]), reverse=False)
    F["su_kien_nguon"] = su_kien

    # --- F3 ket qua CUNG NGAY cua mien ra truoc — CHI khi da thuc su co (R8) ---
    ra_truoc, chua_co = [], []
    for mien in ("MN", "MT", "MB"):
        if THU_TU_RA.get(mien, 9) >= THU_TU_RA.get(mien_dich, 9):
            continue
        rows = c.execute(
            "SELECT date, region, station, prizes_json, created_at FROM lottery_results "
            "WHERE region=? AND date=? AND created_at IS NOT NULL AND created_at <= ? "
            "ORDER BY station ASC", (mien, ngay_dich, cutoff_iso)).fetchall()
        if rows:
            for r in rows:
                ra_truoc.append({
                    "ngay": r["date"], "mien": r["region"], "dai": r["station"],
                    "co_luc": r["created_at"],
                    "giai": [[g, so] for g, so in _tach_giai(r["prizes_json"])],
                })
        else:
            chua_co.append(mien)
    F["cung_ngay_mien_ra_truoc"] = ra_truoc
    F["cung_ngay_chua_co"] = chua_co

    # --- F4 bang chuyen vi 00..99: CHI co/khong, suy tu chinh F2 (ky gan nhat moi mien) ---
    ky_gan_nhat = {}
    for mien in ("MN", "MT", "MB"):
        d = c.execute("SELECT MAX(date) FROM lottery_results WHERE region=? AND date < ?",
                      (mien, ngay_dich)).fetchone()[0]
        ky_gan_nhat[mien] = d
        if not d:
            continue
    F["ky_gan_nhat"] = ky_gan_nhat
    co_mat = {}
    for mien in ("MN", "MT", "MB"):
        d = ky_gan_nhat.get(mien)
        tap = set()
        if d:
            for r in c.execute("SELECT prizes_json FROM lottery_results "
                               "WHERE region=? AND date=?", (mien, d)):
                tap |= _duoi_cua_ky(r["prizes_json"])
        co_mat[mien] = sorted(tap)
    F["co_mat_ky_gan_nhat"] = co_mat

    # --- NEN: b = ky vong so DUOI KHAC NHAU mot ngay cua mien dich / 100 -----------------
    #     RM-21: do lai CHO CHINH mien x thu dang xet, khong muon hang so cua thuoc khac.
    ngay_nen = [r[0] for r in c.execute(
        "SELECT DISTINCT date FROM lottery_results WHERE region=? AND date < ? "
        "AND CAST(strftime('%w', date) AS INT)=? AND date >= date(?, ?) ORDER BY date",
        (mien_dich, ngay_dich, wd, ngay_dich, "-%d days" % (so_tuan_nen * 7)))]
    tong_duoi, n_ngay = 0, 0
    for d in ngay_nen:
        tap = set()
        for r in c.execute("SELECT prizes_json FROM lottery_results WHERE region=? AND date=?",
                           (mien_dich, d)):
            tap |= _duoi_cua_ky(r["prizes_json"])
        if tap:
            tong_duoi += len(tap)
            n_ngay += 1
    F["nen"] = {
        "b_pm": pm(tong_duoi, n_ngay * 100) if n_ngay else None,
        "tb_duoi_mot_ngay": (tong_duoi * 100 // n_ngay) if n_ngay else None,  # x100, so nguyen
        "n_ngay_do": n_ngay,
        "cua_so": "%d tuần, chỉ %s, chỉ bản ghi date < %s" % (so_tuan_nen, THU_VN[wd], ngay_dich),
        "cach_do": "b = (trung bình số ĐUÔI KHÁC NHAU của một ngày ở miền đích) / 100",
        "thuoc_da_do": "%s · %s · ngày < %s" % (mien_dich, THU_VN[wd], ngay_dich),
    }

    # --- CONDITIONS: moi luat active cua bucket, KHONG loc tier, KHONG xep hang (R1,R2) ---
    luat_rows = c.execute(
        "SELECT id, source_region, source_station, source_offset, prize_keys, "
        "source_station_slot, source_weekday "
        "FROM mined_rules WHERE target_region=? AND target_weekday=? AND is_active=1 "
        "ORDER BY id ASC", (mien_dich, wd_py)).fetchall()

    # ban do ket qua nguon de suy duoi cua luat (chi tu su kien DA CO trong FACTS)
    def _duoi_nguon(src_region, src_station, offset, prize_keys, src_wd):
        # ngay nguon suy TU OFFSET, khong lay MAX(date) — MAX(date) tinh co bang target-1
        # nen che mat loi lech bucket o tren.
        if offset == "D-1":
            ngay_src = c.execute("SELECT date(?, '-1 day')", (ngay_dich,)).fetchone()[0]
        elif offset in ("D", "D-0"):
            ngay_src = ngay_dich
        else:
            return (None, [], "offset không hỗ trợ: %s" % offset, [])
        if not ngay_src:
            return (None, [], "không có kỳ nguồn", [])
        # TU KIEM QUY UOC THU: thu (Python) cua ngay nguon phai bang source_weekday cua luat.
        if src_wd is not None:
            w_src_py = (c.execute("SELECT CAST(strftime('%w', ?) AS INT)",
                                  (ngay_src,)).fetchone()[0] + 6) % 7
            if w_src_py != src_wd:
                return (ngay_src, [],
                        "LỆCH QUY ƯỚC THỨ: ngày nguồn %s là thứ %d (Python) nhưng luật ghi "
                        "source_weekday=%d ⇒ điều kiện bị loại để tránh dùng sai bucket"
                        % (ngay_src, w_src_py, src_wd), [])
        if ngay_src == ngay_dich:
            rows = c.execute("SELECT prizes_json FROM lottery_results WHERE region=? AND date=? "
                             "AND station=? AND created_at IS NOT NULL AND created_at <= ?",
                             (src_region, ngay_src, src_station, cutoff_iso)).fetchall()
            if not rows:
                return (ngay_src, [], "kỳ nguồn cùng ngày CHƯA CÓ tại thời điểm chốt", [])
        else:
            rows = c.execute("SELECT prizes_json FROM lottery_results "
                             "WHERE region=? AND date=? AND station=?",
                             (src_region, ngay_src, src_station)).fetchall()
            if not rows:
                return (ngay_src, [],
                        "đài nguồn %s KHÔNG có kỳ xổ ngày %s ⇒ điều kiện không áp dụng hôm nay"
                        % (src_station, ngay_src), [])
        khoa = [k.strip() for k in (prize_keys or "").split("+") if k.strip()]
        anh_xa = {"GĐB": "Giải Đặc Biệt", "G1": "Giải nhất", "G2": "Giải nhì", "G3": "Giải ba",
                  "G4": "Giải tư", "G5": "Giải năm", "G6": "Giải sáu", "G7": "Giải bảy",
                  "G8": "Giải tám"}
        can = [anh_xa.get(k, k) for k in khoa]
        tap, nguon = set(), []
        for r in rows:
            for g, sos in _tach_giai(r["prizes_json"]):
                if g in can:
                    for s in sos:
                        t = duoi(s)
                        if t and t.isdigit():
                            tap.add(t)
                            nguon.append(s)
        return (ngay_src, sorted(tap), None, sorted(set(nguon)))

    dieu_kien = []
    for r in luat_rows:
        ngay_src, tails, ghi_chu, so_nguon = _duoi_nguon(
            r["source_region"], r["source_station"], r["source_offset"], r["prize_keys"],
            r["source_weekday"])
        if not ghi_chu and not tails:
            ghi_chu = ("kỳ nguồn %s ngày %s không sinh đuôi nào ở các giải %s"
                       % (r["source_station"], ngay_src, r["prize_keys"]))
        # bang chung AS-OF: chi luot danh gia co date < ngay_dich
        ev = c.execute(
            "SELECT COUNT(*) n, SUM(CASE WHEN hit_any THEN 1 ELSE 0 END) k "
            "FROM mined_rule_effectiveness WHERE rule_id=? AND date < ?",
            (r["id"], ngay_dich)).fetchone()
        n_ev = ev["n"] or 0
        k_ev = ev["k"] or 0
        dieu_kien.append({
            "rule_id": r["id"],
            "nguon_mien": r["source_region"], "nguon_dai": r["source_station"],
            "nguon_offset": r["source_offset"], "nguon_giai": r["prize_keys"],
            "nguon_slot": r["source_station_slot"], "nguon_thu_python": r["source_weekday"],
            "ngay_nguon": ngay_src, "duoi_suy_ra": tails, "k": len(tails),
            "so_nguon": so_nguon,
            "ghi_chu": ghi_chu,
            "danh_gia_n": n_ev, "danh_gia_k": k_ev,
            "danh_gia_cutoff": "mined_rule_effectiveness WHERE rule_id=%d AND date < %s"
                               % (r["id"], ngay_dich),
        })
    dieu_kien.sort(key=lambda x: x["rule_id"])   # R2: thu tu co dinh theo id, KHONG theo suc manh
    F["dieu_kien"] = dieu_kien
    c.close()
    return F


# ----------------------------------------------------------------------------- render (THUAN)
def _bang_00_99(co_mat):
    """R5: full universe 00->99, thu tu co dinh, CHI co/khong."""
    d = []
    for i in range(100):
        t = "%02d" % i
        d.append("%s %s%s%s" % (
            t,
            "1" if t in co_mat.get("MN", []) else "0",
            "1" if t in co_mat.get("MT", []) else "0",
            "1" if t in co_mat.get("MB", []) else "0"))
    dong = []
    for i in range(0, 100, 5):
        dong.append("  " + "   ".join(d[i:i + 5]))
    return "\n".join(dong)


def render(F):
    """HAM THUAN: chi doc F, khong cham DB / dong ho / bien moi truong (R6)."""
    L = []
    A = L.append
    mien = F["mien_dich"]
    A("=== NGỮ CẢNH THUẦN · schema %s · renderer %s ===" % (F["schema"], F["renderer"]))
    A("NGÀY ĐÍCH: %s (%s)" % (F["ngay_dich"], F["thu_ten"]))
    A("MIỀN ĐÍCH: %s (%s)" % (mien, MIEN_TEN.get(mien, mien)))
    A("MỐC CHỐT (cutoff): %s" % F["cutoff"])
    A("Mọi dữ kiện dưới đây đều có nguồn với thời điểm TRƯỚC mốc chốt. "
      "Không có dữ kiện nào của chính ngày đích ở miền đích.")
    A("")

    # ---------------- TANG 1 ----------------
    A("--- TẦNG 1 · SỰ KIỆN NGUỒN (dữ kiện thô, kiểm lại được từ bảng kết quả) ---")
    A("")
    A("[F1] KHUNG")
    A("  miền đích: %s · thứ: %s · ngày: %s" % (mien, F["thu_ten"], F["ngay_dich"]))
    for m in ("MN", "MT", "MB"):
        ds = F["lich_dai_suy_tu_lich_su"].get(m, [])
        if ds:
            A("  đài từng xổ vào %s ở %s (%s): %s" % (
                F["thu_ten"], m, F["cua_so_suy_lich"],
                ", ".join("%s [%d kỳ quan sát]" % (x["dai"], x["so_ky_quan_sat"]) for x in ds)))
        else:
            A("  đài từng xổ vào %s ở %s: KHÔNG CÓ BẢN GHI trong cửa sổ quan sát" % (F["thu_ten"], m))
    A("  cách suy: đếm trên lottery_results, chỉ bản ghi date < %s. "
      "Đây là QUAN SÁT LỊCH SỬ, không phải lịch công bố." % F["ngay_dich"])
    A("")

    A("[F2] KẾT QUẢ CÁC KỲ TRƯỚC (đầy đủ giải, không cắt, không xếp hạng)")
    ngay_hien = None
    for sk in F["su_kien_nguon"]:
        if sk["ngay"] != ngay_hien:
            ngay_hien = sk["ngay"]
            A("  ── ngày %s ──" % ngay_hien)
        A("  %s · %s · %s" % (sk["mien"], sk["dai"], ngay_hien))
        for g, sos in sk["giai"]:
            ds = [duoi(s) for s in sos]
            A("     %-14s %s   → đuôi: %s" % (g, ", ".join(sos), ", ".join(ds)))
    if not F["su_kien_nguon"]:
        A("  KHÔNG CÓ BẢN GHI nào trước ngày đích trong cửa sổ.")
    A("")

    A("[F3] KẾT QUẢ CÙNG NGÀY CỦA MIỀN RA TRƯỚC")
    if F["cung_ngay_mien_ra_truoc"]:
        for sk in F["cung_ngay_mien_ra_truoc"]:
            A("  %s · %s · %s (có lúc %s)" % (sk["mien"], sk["dai"], sk["ngay"], sk["co_luc"]))
            for g, sos in sk["giai"]:
                A("     %-14s %s   → đuôi: %s"
                  % (g, ", ".join(sos), ", ".join(duoi(s) for s in sos)))
    for m in F["cung_ngay_chua_co"]:
        A("  %s: CHƯA CÓ KẾT QUẢ tại mốc chốt %s. "
          "Đây cũng là một dữ kiện — cấm giả định giá trị." % (m, F["cutoff"]))
    if not F["cung_ngay_mien_ra_truoc"] and not F["cung_ngay_chua_co"]:
        A("  Miền đích là miền ra sớm nhất trong ngày — không có miền nào ra trước.")
    A("")

    A("[F4] BẢNG CHUYỂN VỊ 00→99 — KỲ GẦN NHẤT CỦA TỪNG MIỀN")
    A("  Đây là CHUYỂN VỊ của [F2], KHÔNG thêm thông tin mới. Ba cờ theo thứ tự MN MT MB,")
    A("  1 = đuôi có mặt ở kỳ gần nhất của miền đó, 0 = không có mặt.")
    A("  Kỳ gần nhất: MN=%s · MT=%s · MB=%s"
      % (F["ky_gan_nhat"].get("MN"), F["ky_gan_nhat"].get("MT"), F["ky_gan_nhat"].get("MB")))
    A("  Thứ tự cố định 00→99. KHÔNG sắp xếp theo bất kỳ giá trị nào.")
    A(_bang_00_99(F["co_mat_ky_gan_nhat"]))
    A("")

    # ---------------- TANG 2 ----------------
    A("--- TẦNG 2 · ĐIỀU KIỆN (DỮ KIỆN ĐỂ CÂN NHẮC — KHÔNG PHẢI KHUYẾN NGHỊ SỐ) ---")
    A("")
    nen = F["nen"]
    A("[C-NỀN] CÁCH TÍNH NỀN — đọc trước mọi điều kiện")
    if nen["b_pm"] is None:
        A("  KHÔNG ĐO ĐƯỢC NỀN trong cửa sổ %s ⇒ mọi điều kiện dưới đây ghi "
          "KHÔNG_ĐỦ_MẪU." % nen["cua_so"])
    else:
        A("  b (một đuôi bất kỳ trúng trong một ngày ở miền đích) = %s" % pm_str(nen["b_pm"]))
        A("  cách đo: %s" % nen["cach_do"])
        A("  thước đã đo b: %s · cửa sổ: %s · số ngày đo: %d"
          % (nen["thuoc_da_do"], nen["cua_so"], nen["n_ngay_do"]))
        A("  trung bình %d.%02d đuôi khác nhau một ngày."
          % (nen["tb_duoi_mot_ngay"] // 100, nen["tb_duoi_mot_ngay"] % 100))
        A("  Với một điều kiện suy ra BỘ k ĐUÔI, nền đúng là 1-(1-b)^k — KHÔNG phải b.")
        A("  Hằng số b này CHỈ đúng cho thước đã đo nó (miền %s, %s). "
          "Cấm mượn sang thước khác." % (F["mien_dich"], F["thu_ten"]))
    A("")

    dk = F["dieu_kien"]
    A("[C] DANH SÁCH ĐIỀU KIỆN — %d điều kiện, in THEO THỨ TỰ ID TĂNG DẦN." % len(dk))
    A("  KHÔNG xếp hạng · KHÔNG cắt top-k · KHÔNG hệ số nhân · KHÔNG lọc theo mức mạnh yếu.")
    A("  Mỗi điều kiện là một MỆNH ĐỀ CÓ ĐỊNH NGHĨA, bạn tự cân nhắc dùng hay bỏ.")
    A("")
    hop_le = 0
    for i, d in enumerate(dk, 1):
        ma = "C%02d" % i
        A("  [%s] rule_id=%d" % (ma, d["rule_id"]))
        A("     phạm vi      : đích %s · %s · nguồn %s(%s) · đài %s · giải %s"
          % (mien, F["thu_ten"], d["nguon_mien"], d["nguon_offset"],
             d["nguon_dai"], d["nguon_giai"]))
        A("     đầu vào      : kết quả %s ngày %s (có trong [F2]/[F3] ở trên)"
          % (d["nguon_dai"], d["ngay_nguon"]))
        A("     phép biến đổi: lấy 2 chữ số cuối của mỗi số trúng ở các giải nêu trên")
        A("     cutoff       : %s" % d["danh_gia_cutoff"])
        if d["ghi_chu"]:
            A("     TRẠNG THÁI   : KHÔNG ÁP DỤNG ĐƯỢC HÔM NAY — %s" % d["ghi_chu"])
            A("     đuôi suy ra  : (không có) — điều kiện này KHÔNG đóng góp dữ kiện nào hôm nay")
            A("     lịch sử      : %d/%d lượt đánh giá trước ngày đích "
              "(KHÔNG dùng được vì hôm nay không áp dụng)"
              % (d["danh_gia_k"], d["danh_gia_n"]))
            A("     bằng chứng   : %s" % NHAN_BANG_CHUNG["KHONG_DU_MAU"])
            A("     ĐÂY LÀ DỮ KIỆN, KHÔNG PHẢI KHUYẾN NGHỊ.")
            A("")
            continue
        hop_le += 1
        # In KEM SO NGUON tren CUNG MOT DONG. Hai ly do, ca hai deu quan trong:
        #   · nguoi/model kiem lai duoc NGAY TAI CHO, khong phai do nguoc len [F2];
        #   · dong nay tu chung minh no la CHUYEN VI cua su kien goc chu khong phai mot ro
        #     so da loc — neu ai do thay bang top-k thi cac duoi se khong con khop voi
        #     so nguon in kem, va cong o nhiem se bat duoc.
        A("     đuôi suy ra  : từ %s → %s   [k=%d]"
          % (", ".join(d.get("so_nguon") or []) or "(không có số nguồn)",
             ", ".join(d["duoi_suy_ra"]) if d["duoi_suy_ra"] else "(rỗng)", d["k"]))
        nk = nen_bo_k(nen["b_pm"], d["k"])
        A("     nền cho k=%d : %s   (= 1-(1-b)^k, b=%s)"
          % (d["k"], pm_str(nk), pm_str(nen["b_pm"])))
        n_ev, k_ev = d["danh_gia_n"], d["danh_gia_k"]
        A("     cỡ mẫu       : %d lượt đánh giá trước ngày đích" % n_ev)
        if n_ev < N_TOI_THIEU or nk is None:
            A("     quan sát     : %d/%d = %s" % (k_ev, n_ev, pm_str(pm(k_ev, n_ev))))
            A("     bằng chứng   : %s (n=%d < %d)"
              % (NHAN_BANG_CHUNG["KHONG_DU_MAU"], n_ev, N_TOI_THIEU))
        else:
            q = pm(k_ev, n_ev)
            lo, hi = wilson_pm(k_ev, n_ev)
            A("     quan sát     : %d/%d = %s" % (k_ev, n_ev, pm_str(q)))
            A("     độ bất định  : KTC95 Wilson [%s ; %s]" % (pm_str(lo), pm_str(hi)))
            if lo is not None and nk is not None and lo > nk:
                nhan = NHAN_BANG_CHUNG["KHAC_NEN_DUONG"]
            elif hi is not None and nk is not None and hi < nk:
                nhan = NHAN_BANG_CHUNG["KHAC_NEN_AM"]
            else:
                nhan = NHAN_BANG_CHUNG["KHONG_KHAC_NEN"]
            A("     so với nền   : nền %s %s khoảng tin cậy"
              % (pm_str(nk), "NẰM NGOÀI" if nhan != NHAN_BANG_CHUNG["KHONG_KHAC_NEN"]
                 else "NẰM TRONG"))
            A("     bằng chứng   : %s" % nhan)
        A("     ĐÂY LÀ DỮ KIỆN, KHÔNG PHẢI KHUYẾN NGHỊ.")
        A("")

    # do phu — cong bo thang de model biet dieu kien co phan biet duoc khong
    hop = set()
    for d in dk:
        hop |= set(d["duoi_suy_ra"])
    A("[C-ĐỘ PHỦ] TỰ KIỂM SỨC PHÂN BIỆT CỦA TẦNG 2")
    A("  Hợp của mọi đuôi mà %d điều kiện suy ra: %d/100 đuôi." % (len(dk), len(hop)))
    A("  Độ phủ càng gần 100 thì tầng điều kiện càng ÍT phân biệt được — "
      "khi đó gần như số nào cũng có ít nhất một điều kiện đỡ.")
    A("  Con số này công bố để bạn tự chiết khấu, KHÔNG phải để bạn chọn theo nó.")
    A("")

    # ---------------- TANG 3 ----------------
    A("--- TẦNG 3 · HỢP ĐỒNG SUY LUẬN VÀ ĐẦU RA ---")
    A("")
    A("[G1] GIỚI HẠN CỦA TÀI LIỆU NÀY — đọc kỹ, đây là ràng buộc cứng")
    A("  1. KHÔNG có công cụ truy vấn nào trong đường gọi này. Bạn KHÔNG thể tra thêm dữ liệu.")
    A("     Mọi dữ kiện cần cho quyết định đã nằm trong tài liệu. Dữ kiện không có ở đây")
    A("     nghĩa là KHÔNG TỒN TẠI với bạn — cấm giả định, cấm suy ra từ trí nhớ.")
    A("  2. Tài liệu này KHÔNG chứa danh sách số chọn sẵn, KHÔNG chứa xếp hạng,")
    A("     KHÔNG chứa trọng số, KHÔNG chứa hiệu suất của bất kỳ mô hình nào.")
    A("     Nếu bạn thấy mình đang tìm một danh sách như vậy — nó không tồn tại. Tự lập luận.")
    A("  3. Điều kiện ở TẦNG 2 là BẰNG CHỨNG để cân nhắc, KHÔNG phải khuyến nghị.")
    A("     Một điều kiện ghi KHÔNG_KHÁC_NỀN nghĩa là nó KHÔNG cho lợi thế đo được.")
    A("     Một điều kiện ghi KHÔNG_ĐỦ_MẪU nghĩa là CHƯA ĐƯỢC PHÉP kết luận từ nó.")
    A("  4. Mỗi lượt xổ là một sự kiện độc lập. Không có cơ chế 'đến hạn phải ra'.")
    A("  5. Bạn phải chọn. Không được từ chối trả lời vì bằng chứng yếu —")
    A("     hãy chọn và ghi trung thực mức chắc chắn.")
    A("")
    A("[G2] HỢP ĐỒNG ĐẦU RA — trả về DUY NHẤT một khối JSON hợp lệ, không kèm văn xuôi ngoài JSON")
    A("  {")
    A('    "main_number": "<hai chữ số 00..99>",')
    A('    "secondary_number": "<hai chữ số>" hoặc null,')
    A('    "reasoning": [ { "condition_ref": "<mã>", "dung_the_nao": "<một câu>" }, ... ],')
    A('    "secondary_reasoning": [ { "condition_ref": "<mã>", "dung_the_nao": "..." }, ... ]'
      ' hoặc [],')
    A('    "arithmetic": [ { "bieu_thuc": "<phép tính>", "gia_tri": <số> }, ... ] hoặc [],')
    A('    "muc_chac_chan": "<CAO|VUA|THAP>",')
    A('    "gioi_han_da_biet": "<một câu về điều bạn KHÔNG chứng minh được>"')
    A("  }")
    A("")
    A("[G3] RÀNG BUỘC CỦA HỢP ĐỒNG")
    A("  - main_number: ĐÚNG MỘT số. Bắt buộc.")
    A("  - secondary_number: tuỳ chọn. Nếu có thì secondary_reasoning phải viện dẫn")
    A("    điều kiện KHÁC với reasoning của main_number — lý do phải ĐỘC LẬP,")
    A("    không được là hệ quả của cùng một điều kiện.")
    A("  - KHÔNG có trường 3 càng trong hợp đồng này. Không bắt buộc, không thêm vào.")
    A("  - Mọi condition_ref PHẢI là mã CÓ THẬT trong tài liệu này: %s"
      % ("C01..C%02d, F1, F2, F3, F4" % len(dk) if dk else "F1, F2, F3, F4"))
    A("    Viện dẫn một mã không có trong tài liệu là câu trả lời KHÔNG HỢP LỆ.")
    A("  - Mọi phần tử arithmetic phải tính lại được từ TẦNG 1 bằng số liệu in ở trên.")
    A("  - CẤM viện dẫn: tên mô hình khác, tỉ lệ thắng, trọng số, điểm tổng, điểm cuối,")
    A("    kết quả cũ của hệ thống, hoặc bất kỳ danh sách số nào không có trong tài liệu.")
    A("")
    A("=== HẾT NGỮ CẢNH · %s · %s ===" % (F["schema"], F["renderer"]))
    return "\n".join(L) + "\n"


# ----------------------------------------------------------------------------- tien ich
def facts_canonical(F):
    """JSON chuan hoa cua FACTS — dung de bam va de render lai khong can DB (R6)."""
    return json.dumps(F, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def bam(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=CLONE_MAC_DINH)
    ap.add_argument("--ngay", required=True)
    ap.add_argument("--mien", required=True)
    ap.add_argument("--cutoff", default=None)
    ap.add_argument("--ra", default=None)
    a = ap.parse_args()
    cutoff = a.cutoff or (a.ngay + "T00:00:00+07:00")
    F = thu_thap(a.db, a.ngay, a.mien, cutoff)
    s = render(F)
    if a.ra:
        io.open(a.ra, "w", encoding="utf-8", newline="").write(s)
    print(s)
    print("---- sha256(prompt) = %s · %d ký tự · %d byte"
          % (bam(s), len(s), len(s.encode("utf-8"))))
    print("---- sha256(facts)  = %s" % bam(facts_canonical(F)))


if __name__ == "__main__":
    main()
