# -*- coding: utf-8 -*-
"""V11169 CONG 3 — tinh lai chinh xac hai danh sach tu artifact san co (v11166_s7_fact.json,
doc that tu DB production read-only ngay 05/09/2026, script nguon _s7g_fact.py).
KHONG ket noi lai VPS, KHONG ghi gi — chi doc lai JSON da co de lam danh sach chinh xac cho goi
de xuat. RM-11: moi so o day tai lap duoc bang chinh script nay + artifact di kem.
"""
import json, io, sys, datetime
sys.stdout.reconfigure(encoding="utf-8")
BASE = r"C:\Users\Admin\AppData\Local\Temp\claude\e--Lottery-AI-Test\c8d5eaf3-f941-4919-aee1-0af70dea23fd\scratchpad\d30"
F = json.load(io.open(BASE + r"\v11166_s7_fact.json", encoding="utf-8"))
ROWS = F["rows"]
KQD = F["ket_qua_dau"]  # (date|region) -> gio ket qua dau tien ve (MIN created_at cua lottery_results)


def la_backfill(r):
    a = KQD.get("%s|%s" % (r["date"], r["region"]))
    if not a or not r["created_at"]:
        return False
    return (datetime.datetime.fromisoformat(r["created_at"]) >
            datetime.datetime.fromisoformat(a).replace(tzinfo=None))


for r in ROWS:
    r["_backfill"] = la_backfill(r)

BF = [r for r in ROWS if r["_backfill"]]
LIVE = [r for r in ROWS if r["co_ket_qua"] and not r["_backfill"]]

print("=" * 90)
print("MUC A — BACKFILL")
print("=" * 90)
print("tong bundle backfill (created_at > gio ket qua dau tien ve):", len(BF))
mien = {}
for r in BF:
    mien[r["region"]] = mien.get(r["region"], 0) + 1
print("theo mien:", mien)
ngay_bf = sorted(set(r["date"] for r in BF))
print("khoang ngay:", ngay_bf[0], "->", ngay_bf[-1], "| so ngay khac nhau:", len(ngay_bf))
tao_luc = sorted(set(r["created_at"] for r in BF))
print("cac moc created_at khac nhau:", tao_luc)

# so sanh bach thu: backfill vs live (dung chinh du lieu, khong hang so ngoai)
def bt_rate(rows):
    co = [r for r in rows if r["co_ket_qua"]]
    if not co:
        return None
    hit = sum(r["bt_hit_tinh_lai"] for r in co)
    # NEN dung: xac suat 1 so chon co dinh (uniform 00-99) trung 1 trong D2 duoi that = D2/100
    nen = sum(r["D2"] / 100.0 for r in co if r["D2"])
    return {"n": len(co), "hit": hit, "ti_le_pct": 100.0 * hit / len(co),
            "nen_tb_pct": 100.0 * nen / len(co), "chenh_pp": 100.0 * hit / len(co) - 100.0 * nen / len(co)}

print("\nbach thu BACKFILL:", bt_rate(BF))
print("bach thu LIVE (loai backfill):", bt_rate(LIVE))
print("bach thu GOP CA HAI (nguyen trang hien tai, KHONG loc):", bt_rate(ROWS))

print("\nDANH SACH DAY DU 91 BUNDLE (id,date,region,bach_thu,lo3,bt_hit_tinh_lai,created_at):")
bf_list = []
for r in sorted(BF, key=lambda x: (x["date"], x["region"])):
    row = {"id": r["id"], "date": r["date"], "region": r["region"], "bach_thu": r["bach_thu"],
           "lo3": r["lo3"], "bt_status_luu": r["bt_status_luu"],
           "bt_hit_tinh_lai": r["bt_hit_tinh_lai"], "created_at": r["created_at"],
           "gio_ket_qua_dau": KQD.get("%s|%s" % (r["date"], r["region"]))}
    bf_list.append(row)
for row in bf_list:
    print(row)

print("\n" + "=" * 90)
print("MUC B — 32 NHAN LO3 SAI")
print("=" * 90)
def st3(r):
    return "WIN" if r["lo3_hit_tinh_lai"] else "LOSE"

co_lo3 = [r for r in ROWS if r["co_ket_qua"] and r["lo3"]]
sai = [r for r in co_lo3 if st3(r) != r["lo3_status_luu"]]
print("tong dong co lo3 va co ket qua:", len(co_lo3))
print("so dong SAI (nhan luu != tinh lai theo dung quy tac dang serve):", len(sai))
luu_win = sum(1 for r in co_lo3 if r["lo3_status_luu"] == "WIN")
that_win = sum(1 for r in co_lo3 if st3(r) == "WIN")
print("lo3_status_luu == WIN (nhan da luu):", luu_win)
print("tinh lai == WIN (that):", that_win)
print("ti le phong dai:", round(luu_win / that_win, 4) if that_win else None)

print("\nDANH SACH DAY DU 32 DONG SAI:")
sai_list = []
for r in sorted(sai, key=lambda x: (x["date"], x["region"])):
    row = {"id": r["id"], "date": r["date"], "region": r["region"], "lo3": r["lo3"],
           "bach_thu": r["bach_thu"], "nhan_luu": r["lo3_status_luu"], "that": st3(r),
           "created_at": r["created_at"], "la_backfill": r["_backfill"],
           "lo3_khop_2so_voi_bt": (r["lo3"][-2:] == r["bach_thu"] if r["lo3"] and r["bach_thu"] else None)}
    sai_list.append(row)
for row in sai_list:
    print(row)

# co bao nhieu trong 32 dong SAI la backfill?
sai_bf = sum(1 for r in sai if r["_backfill"])
print("\ntrong 32 dong sai, so dong thuoc backfill (created_at > ket qua dau):", sai_bf,
      "/ tong", len(sai))
sai_ngoai_bf = [r for r in sai if not r["_backfill"]]
print("dong SAI ma KHONG phai backfill (neu co, la dau hieu writer con loi o live):",
      len(sai_ngoai_bf))
for r in sai_ngoai_bf:
    print("  NGOAI-BACKFILL:", {"id": r["id"], "date": r["date"], "region": r["region"],
                                 "lo3": r["lo3"], "created_at": r["created_at"]})

# tat ca 32 dong co dung mot moc created_at (backfill run) khong?
created_set = sorted(set(r["created_at"] for r in sai))
print("\ncac moc created_at cua 32 dong sai:", created_set)

# anh huong: neu sua thi ti le lo3 lich su tu bao nhieu xuong bao nhieu
def lo3_rate(rows):
    co = [r for r in rows if r["co_ket_qua"] and r["lo3"]]
    if not co:
        return None
    win_luu = sum(1 for r in co if r["lo3_status_luu"] == "WIN")
    win_that = sum(1 for r in co if st3(r) == "WIN")
    return {"n": len(co), "WIN_theo_nhan_luu": win_luu, "WIN_that": win_that,
            "ti_le_luu_pct": 100.0 * win_luu / len(co), "ti_le_that_pct": 100.0 * win_that / len(co)}

print("\nTOAN BO LICH SU (570 bundle):", lo3_rate(ROWS))
print("CHI LIVE (loai 91 backfill):", lo3_rate(LIVE))
print("CHI BACKFILL (91):", lo3_rate(BF))

out = {
    "nguon": "v11166_s7_fact.json (dump production DB read-only 05/09/2026, script goc "
             "_s7g_fact.py; quy tac trung doc tu database.py:4849/4886, main.py:6574)",
    "muc_A_backfill": {
        "tong_so": len(BF), "theo_mien": mien, "khoang_ngay": [ngay_bf[0], ngay_bf[-1]],
        "cac_moc_created_at": tao_luc,
        "bach_thu_backfill": bt_rate(BF), "bach_thu_live": bt_rate(LIVE),
        "bach_thu_gop_khong_loc": bt_rate(ROWS),
        "danh_sach": bf_list,
    },
    "muc_B_lo3_sai": {
        "tong_dong_co_lo3": len(co_lo3), "so_dong_sai": len(sai),
        "luu_WIN": luu_win, "that_WIN": that_win,
        "ti_le_phong_dai": round(luu_win / that_win, 4) if that_win else None,
        "danh_sach": sai_list,
        "so_dong_sai_la_backfill": sai_bf,
        "so_dong_sai_ngoai_backfill": len(sai_ngoai_bf),
        "cac_moc_created_at_cua_32_dong": created_set,
        "lo3_rate_toan_bo": lo3_rate(ROWS), "lo3_rate_live": lo3_rate(LIVE),
        "lo3_rate_backfill": lo3_rate(BF),
    },
}
p = BASE + r"\v11169_w3_thuoc_raw.json"
io.open(p, "w", encoding="utf-8", newline="").write(json.dumps(out, ensure_ascii=False, indent=1, default=str))
print("\n-> ghi", p)
