# -*- coding: utf-8 -*-
"""PL19c Q16 — ĐỌC LẠI kết luận thắng của RULES-FIRST (V10857, 26/07).

V10857 tuyên bố: "Official bundle BT gộp 3 miền: 20,0% (6/30) → 41,7% (10/24) — hơn GẤP ĐÔI"
và "LLM any-hit 48,6% → 66,9% (+18,3pp)".

Đo lại bằng thước mới: có NỀN theo ngày · có ĐỐI CHỨNG GIẢ · và MỞ RỘNG cửa sổ sau
tới hôm nay để xem "gấp đôi" có bền không.
"""
import collections
import datetime as dt
import hashlib
import json
import math
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")

# cổng tuổi dữ liệu (FU-303)
M = json.load(open("artifacts/live_sync/latest_manifest.json", encoding="utf-8"))
s0 = dt.datetime.fromisoformat(M["sync_completed_at"])
tuoi = (dt.datetime.now(s0.tzinfo) - s0).total_seconds() / 3600
print(f"[cong] DU_LIEU_TUOI cu={tuoi:.1f} gio")
if tuoi > 6:
    raise SystemExit("✗ dữ liệu cũ, dừng")

c = sqlite3.connect("file:data/lottery_ai.db?mode=ro", uri=True)
c.row_factory = sqlite3.Row


def duoi(reg, d, kho={}):
    k = (reg, d)
    if k in kho:
        return kho[k]
    out = set()
    for (pj,) in c.execute("SELECT prizes_json FROM lottery_results WHERE region=? AND date=?"
                           " AND prizes_json IS NOT NULL", (reg, d)):
        try:
            pr = json.loads(pj)
        except Exception:
            continue
        for v in (pr.values() if isinstance(pr, dict) else []):
            for x in (v if isinstance(v, list) else [v]):
                s = "".join(ch for ch in str(x) if ch.isdigit())
                if len(s) >= 2:
                    out.add(s[-2:])
    kho[k] = out
    return out


def bt(x):
    d = "".join(ch for ch in str(x or "") if ch.isdigit())
    return d[-2:] if len(d) >= 2 else None


def do(tu, den, nhan):
    """Trả (n, trúng, nền tích luỹ, trúng của số BỐC BỪA)."""
    n = k = 0
    nen = 0.0
    kg = 0
    for r in c.execute("""SELECT date, region, bach_thu FROM final_bundles
                          WHERE date >= ? AND date <= ? AND bach_thu IS NOT NULL
                          ORDER BY date""", (tu, den)):
        p = bt(r["bach_thu"])
        if not p:
            continue
        thuc = duoi(r["region"], r["date"])
        if not thuc:
            continue
        n += 1
        k += 1 if p in thuc else 0
        nen += len(thuc) / 100.0
        gia = f"{int(hashlib.md5(f'{r[0]}|{r[1]}|q16'.encode()).hexdigest()[:8],16)%100:02d}"
        kg += 1 if gia in thuc else 0
    return n, k, nen, kg


def z(k, n, p0):
    v = n * p0 * (1 - p0)
    return (k - n * p0) / math.sqrt(v) if v > 0 else 0.0


print()
print("=" * 96)
print("Q16-a — ĐO LẠI ĐÚNG HAI CỬA SỔ CỦA V10857, nhưng KÈM NỀN và ĐỐI CHỨNG")
print("=" * 96)
print(f"  {'cửa sổ':28} {'n':>4} {'trúng':>6} {'tỉ lệ':>8} {'NỀN':>7} {'z vs nền':>9} "
      f"{'bốc bừa':>8}")
print("  " + "-" * 82)
KQ = {}
for nhan, tu, den in (("TRƯỚC  08–17/07", "2026-07-08", "2026-07-17"),
                      ("SAU    18–25/07", "2026-07-18", "2026-07-25")):
    n, k, nen, kg = do(tu, den, nhan)
    p0 = nen / n if n else 0
    KQ[nhan] = (n, k, p0, kg)
    print(f"  {nhan:28} {n:>4} {k:>6} {k/n*100 if n else 0:>7.1f}% {p0*100:>6.1f}% "
          f"{z(k,n,p0):>+9.2f} {kg/n*100 if n else 0:>7.1f}%")

print()
print("  V10857 nói: 20,0% (6/30) → 41,7% (10/24) — 'hơn GẤP ĐÔI'")
print("  ⇒ nhưng V10857 KHÔNG so với nền của chính ngày đó, và KHÔNG có đối chứng.")

print()
print("=" * 96)
print("Q16-b — 'GẤP ĐÔI' CÓ BỀN KHÔNG? Mở rộng cửa sổ sau tới hôm nay")
print("=" * 96)
print(f"  {'cửa sổ':28} {'n':>4} {'trúng':>6} {'tỉ lệ':>8} {'NỀN':>7} {'z vs nền':>9} "
      f"{'bốc bừa':>8}")
print("  " + "-" * 82)
for nhan, tu, den in (("SAU  18/07 → 06/08", "2026-07-18", "2026-08-06"),
                      ("SAU  26/07 → 06/08", "2026-07-26", "2026-08-06"),
                      ("TRƯỚC 08/06 → 17/07", "2026-06-08", "2026-07-17")):
    n, k, nen, kg = do(tu, den, nhan)
    p0 = nen / n if n else 0
    print(f"  {nhan:28} {n:>4} {k:>6} {k/n*100 if n else 0:>7.1f}% {p0*100:>6.1f}% "
          f"{z(k,n,p0):>+9.2f} {kg/n*100 if n else 0:>7.1f}%")

print()
print("=" * 96)
print("Q16-c — MẪU CÓ ĐỦ ĐỂ NÓI 'GẤP ĐÔI' KHÔNG?")
print("=" * 96)
n1, k1, p1, _ = KQ["TRƯỚC  08–17/07"]
n2, k2, p2, _ = KQ["SAU    18–25/07"]
p = (k1 + k2) / (n1 + n2)
se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
zz = (k2 / n2 - k1 / n1) / se if se else 0
print(f"  so hai cửa sổ trực tiếp: {k1}/{n1} vs {k2}/{n2} → z = {zz:+.2f}")
print(f"  ngưỡng ý nghĩa thường dùng |z|≥1,96 · sau Bonferroni cho ~15 phép đo: |z|≥3,01")
print(f"  ⇒ {'ĐẠT' if abs(zz) >= 1.96 else 'KHÔNG ĐẠT'} ngay cả ở ngưỡng lỏng 1,96")
# công suất: cần bao nhiêu mẫu để phát hiện chênh 20pp
import statistics
print(f"\n  Để phát hiện chênh 20 điểm (20%→40%) với sức mạnh 80%, α=0,05:")
print(f"    cần khoảng n ≈ 82 lượt MỖI cửa sổ. V10857 có {n1} và {n2}.")
c.close()
