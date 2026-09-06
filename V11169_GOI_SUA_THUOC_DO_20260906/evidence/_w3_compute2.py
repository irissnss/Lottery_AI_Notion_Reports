# -*- coding: utf-8 -*-
"""V11169 CONG 3 — phan 2: truoc/sau THEO TUNG MIEN cho ca bon thuoc (bach thu, lo2, lo3, top-10),
so sanh GOP-KHONG-LOC (hien trang) vs LOAI-91-BACKFILL (de xuat). Doc lai artifact da co, khong
ket noi VPS lai."""
import json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
BASE = r"C:\Users\Admin\AppData\Local\Temp\claude\e--Lottery-AI-Test\c8d5eaf3-f941-4919-aee1-0af70dea23fd\scratchpad\d30"
RAW = json.load(io.open(BASE + r"\v11169_w3_thuoc_raw.json", encoding="utf-8"))
F = json.load(io.open(BASE + r"\v11166_s7_fact.json", encoding="utf-8"))
ROWS = F["rows"]
BF_IDS = set(r["id"] for r in RAW["muc_A_backfill"]["danh_sach"])
for r in ROWS:
    r["_backfill"] = r["id"] in BF_IDS

def st3(r):
    return "WIN" if r["lo3_hit_tinh_lai"] else "LOSE"
def st2(r):
    if r["lo2_k"] == 0:
        return "N/A"
    return "WIN" if r["lo2_hits_tinh_lai"] == r["lo2_k"] else ("PARTIAL" if r["lo2_hits_tinh_lai"] else "LOSE")

def bo_thuoc(rows):
    co = [r for r in rows if r["co_ket_qua"]]
    n = len(co)
    if n == 0:
        return None
    bt_hit = sum(r["bt_hit_tinh_lai"] for r in co)
    # NEN dung: D2/100 (xem _w3_compute.py) -- KHONG phai 1/D2
    bt_nen = sum(r["D2"] / 100.0 for r in co if r["D2"]) / n * 100
    lo3_co = [r for r in co if r["lo3"]]
    lo3_hit_that = sum(1 for r in lo3_co if st3(r) == "WIN")
    lo3_hit_luu = sum(1 for r in lo3_co if r["lo3_status_luu"] == "WIN")
    top10_hit = sum(r["top10_hit"] for r in co if r["n_ranked"] >= 10)
    n_top10 = sum(1 for r in co if r["n_ranked"] >= 10) * 10
    return {
        "n_bundle": n,
        "bach_thu_pct_luu": round(100.0 * sum(1 for r in co if r["bt_status_luu"] == "WIN") / n, 2),
        "bach_thu_pct_tinh_lai": round(100.0 * bt_hit / n, 2),
        "bach_thu_nen_pct": round(bt_nen, 2),
        "lo3_n": len(lo3_co),
        "lo3_pct_nhan_luu": round(100.0 * lo3_hit_luu / len(lo3_co), 2) if lo3_co else None,
        "lo3_pct_that": round(100.0 * lo3_hit_that / len(lo3_co), 2) if lo3_co else None,
        "lo2_pct_luu_WIN": round(100.0 * sum(1 for r in co if r["lo2_status_luu"] == "WIN") / n, 2),
        "lo2_pct_tinh_lai_WIN": round(100.0 * sum(1 for r in co if st2(r) == "WIN") / n, 2),
        "top10_o": n_top10, "top10_hit": top10_hit,
        "top10_pct": round(100.0 * top10_hit / n_top10, 2) if n_top10 else None,
    }

out = {}
for reg in ("MN", "MT", "MB", None):
    rs_all = [r for r in ROWS if (reg is None or r["region"] == reg)]
    rs_live = [r for r in rs_all if not r["_backfill"]]
    key = reg or "GOP_3_MIEN"
    out[key] = {"TRUOC_gop_khong_loc_ca_lich_su": bo_thuoc(rs_all),
                "SAU_loai_91_backfill_chi_live": bo_thuoc(rs_live)}

print(json.dumps(out, ensure_ascii=False, indent=1))
p = BASE + r"\v11169_w3_truoc_sau_mien.json"
io.open(p, "w", encoding="utf-8", newline="").write(json.dumps(out, ensure_ascii=False, indent=1))
print("-> ghi", p)
