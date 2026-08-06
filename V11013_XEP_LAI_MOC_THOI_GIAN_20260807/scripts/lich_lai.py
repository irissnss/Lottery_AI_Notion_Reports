# -*- coding: utf-8 -*-
"""V11013 — TÍNH LẠI MỐC: câu hỏi LỚP (gộp) thay vì câu hỏi TỪNG LUẬT.

Owner 07/08: "cái gì mà đợi tới 24/12 hết năm kiểu này thôi chứ làm gì với dự án bé tẹo
này, làm tiếp đi nhưng cân đối thời gian hạn mốc tương đối ổn hơn đẹp hơn đi"

Owner đúng. Cổng cũ đòi n≥20 CHO MỖI LUẬT ⇒ 1 lượt/tuần/luật ⇒ 140 ngày.
Nhưng câu hỏi thật sự cần trả lời là câu hỏi LỚP: "cơ chế mined_rules có lợi thế đo
tiến không?" — câu đó GỘP ĐƯỢC across 105 luật, nên nhanh hơn ~20 lần.
"""
import datetime as dt
import json
import math
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")

M = json.load(open("artifacts/live_sync/latest_manifest.json", encoding="utf-8"))
s0 = dt.datetime.fromisoformat(M["sync_completed_at"])
tuoi = (dt.datetime.now(s0.tzinfo) - s0).total_seconds() / 3600
print(f"[cong] DU_LIEU_TUOI cu={tuoi:.1f} gio")

c = sqlite3.connect("file:data/lottery_ai.db?mode=ro", uri=True)
c.row_factory = sqlite3.Row
HN = dt.date(2026, 8, 7)

print()
print("=" * 92)
print("1. NHỊP TÍCH LUỸ THẬT — đo tiến gộp được bao nhiêu mỗi ngày?")
print("=" * 92)
r = c.execute("""SELECT COUNT(*) n, COUNT(DISTINCT e.date) nd, MIN(e.date) d0, MAX(e.date) d1
                 FROM mined_rule_effectiveness e JOIN mined_rules r ON r.id=e.rule_id
                 WHERE e.date > date(r.mined_at)""").fetchone()
nhip = r["n"] / r["nd"] if r["nd"] else 0
print(f"  hiện có {r['n']} dòng đo tiến trên {r['nd']} ngày ({r['d0']} → {r['d1']})")
print(f"  nhịp: **{nhip:.0f} dòng/ngày** (không phải 1 lượt/tuần — đó là nhịp TỪNG LUẬT)")

print()
print("=" * 92)
print("2. CẦN BAO NHIÊU MẪU? — phép thử McNemar theo cặp (luật thật vs luật giả)")
print("=" * 92)


def n_can_mcnemar(p_that, p_gia, power=0.80, alpha=0.05):
    """Số CẶP cần cho McNemar. Xấp xỉ: dùng tỉ lệ cặp bất đồng."""
    # cặp bất đồng: một bên trúng, bên kia trượt
    b = p_that * (1 - p_gia)      # thật trúng, giả trượt
    cc = (1 - p_that) * p_gia     # thật trượt, giả trúng
    pd = b + cc
    if pd <= 0:
        return None
    psi = b / pd                  # tỉ lệ nghiêng về "thật thắng"
    za = 1.959964                 # alpha 0.05 hai phía
    zb = 0.8416212                # power 0.80
    n_disc = ((za / 2 + zb * math.sqrt(psi * (1 - psi))) / (psi - 0.5)) ** 2
    return math.ceil(n_disc / pd)


# nền hiện tại: đo tiến luật thật 66,7% vs giả 64,4% (dịch ngày, 45 cặp)
print(f"  {'chênh muốn phát hiện':26} {'cặp cần':>9} {'ngày nữa':>10} {'ngày đạt':>12}")
print("  " + "-" * 62)
BASE = 0.644
for chenh in (0.15, 0.10, 0.075, 0.05):
    n = n_can_mcnemar(BASE + chenh, BASE)
    if not n:
        continue
    con = max(0, n - r["n"])
    ngay = math.ceil(con / nhip) if nhip else 0
    print(f"  +{chenh*100:>4.1f} điểm{'':13} {n:>9} {ngay:>10} {(HN+dt.timedelta(days=ngay)).strftime('%d/%m/%Y'):>12}")

print()
print("=" * 92)
print("3. SO HAI CÁCH THIẾT KẾ")
print("=" * 92)
print(f"""  CÁCH CŨ — hỏi TỪNG LUẬT ("luật #2316 có lợi thế không?")
    cổng n≥20 mỗi luật · mỗi luật chỉ chấm vào ĐÚNG THỨ của nó ⇒ 1 lượt/tuần
    ⇒ 20 tuần = 140 ngày ⇒ **24/12/2026**
    Dùng để: giữ luật A, bỏ luật B — tức TỈA từng luật.

  CÁCH MỚI — hỏi CẢ LỚP ("cơ chế mined_rules có lợi thế không?")
    gộp 105 luật ⇒ {nhip:.0f} dòng/ngày, nhanh hơn ~{nhip:.0f} lần
    Dùng để: GIỮ hay BỎ cả cơ chế — đúng câu hỏi FU-291 đang cần.

  ⇒ Câu hỏi đang chặn quyết định là câu hỏi LỚP, không phải câu hỏi từng luật.
     Nên KHÔNG cần chờ tới 24/12.""")

print()
print("=" * 92)
print("4. MỐC ĐỀ XUẤT MỚI")
print("=" * 92)
n10 = n_can_mcnemar(BASE + 0.10, BASE)
ngay10 = math.ceil(max(0, n10 - r["n"]) / nhip) if nhip else 0
d10 = HN + dt.timedelta(days=ngay10)
print(f"""  FU-286 CŨ : 24/12/2026 — hỏi từng luật, n≥20/luật
  FU-286 MỚI: **{d10.strftime('%d/%m/%Y')}** — hỏi cả lớp, đủ mẫu để phát hiện chênh 10 điểm
              ({n10} cặp, hiện có {r['n']}, cần thêm {max(0,n10-r['n'])} ≈ {ngay10} ngày)

  Nếu sau mốc đó lớp KHÔNG có lợi thế ⇒ bỏ cả cơ chế, KHỎI phải tỉa từng luật
  ⇒ câu hỏi 24/12 tự tan.
  Chỉ khi lớp CÓ lợi thế mới cần tỉa từng luật — lúc đó mới đặt mốc dài.""")
c.close()
