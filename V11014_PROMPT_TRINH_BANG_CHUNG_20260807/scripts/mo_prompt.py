# -*- coding: utf-8 -*-
"""V11014 — MỔ PROMPT THẬT: chỗ nào NHỒI SỐ, chỗ nào TRÙNG LẶP.

Owner 07/08: "prompt đang nhồi số vào ép agent model AI lấy số đó đâu có tự nhiên theo
tư duy phân tích, đâu khai thác được sức mạnh model AI, rồi các tầng điều nhồi tương
tượng na ná nhau liên tục"

Gọi THẲNG build_context_pack của production, đo từng khối: bao nhiêu ký tự, có bơm
DANH SÁCH SỐ không, có ra MỆNH LỆNH không, và khối nào trùng khối nào.
"""
import io
import re
import sys
import datetime as dt

sys.path.insert(0, "web/backend")
sys.stdout.reconfigure(encoding="utf-8")

import gpt_analyzer as G  # noqa: E402

MIEN = sys.argv[1] if len(sys.argv) > 1 else "MB"
NGAY = sys.argv[2] if len(sys.argv) > 2 else dt.date.today().isoformat()

print("=" * 100)
print(f"MỔ PROMPT THẬT — {MIEN} ngày {NGAY} (gọi thẳng hàm production)")
print("=" * 100)

ctx = G.build_context_pack(MIEN, NGAY)
print(f"\n  Gói ngữ cảnh: **{len(ctx):,} ký tự**")

# tách theo tiêu đề "### "
khoi = []
cur_ten, cur_noi = "(đầu gói)", []
for d in ctx.splitlines():
    if d.startswith("### "):
        khoi.append((cur_ten, "\n".join(cur_noi)))
        cur_ten, cur_noi = d[4:].strip(), []
    else:
        cur_noi.append(d)
khoi.append((cur_ten, "\n".join(cur_noi)))

SO2 = re.compile(r"(?<!\d)\d{2}(?!\d)")
LENH = re.compile(r"BẮT BUỘC|PHẢI |ƯU TIÊN|CẤM |KHÔNG ĐƯỢC|TUYỆT ĐỐI|CHỐT MẠNH|boost|\+1đ")

print()
print(f"  {'#':>2} {'khối':44} {'ký tự':>7} {'số 2cs':>7} {'mệnh lệnh':>10}  đánh giá")
print("  " + "-" * 96)
tong_so = tong_lenh = 0
bang = []
for i, (ten, noi) in enumerate(khoi, 1):
    if not noi.strip():
        continue
    n_so = len(SO2.findall(noi))
    n_lenh = len(LENH.findall(noi))
    tong_so += n_so
    tong_lenh += n_lenh
    dg = ""
    if n_lenh >= 3 and n_so >= 10:
        dg = "★ NHỒI SỐ + RA LỆNH"
    elif n_lenh >= 3:
        dg = "ra lệnh"
    elif n_so >= 20:
        dg = "nhiều số"
    bang.append((ten, len(noi), n_so, n_lenh, dg))
    print(f"  {i:>2} {ten[:44]:44} {len(noi):>7,} {n_so:>7} {n_lenh:>10}  {dg}")
print("  " + "-" * 96)
print(f"  {'':>2} {'TỔNG':44} {len(ctx):>7,} {tong_so:>7} {tong_lenh:>10}")

print()
print("=" * 100)
print("TRÙNG LẶP — khối nào trình LẠI cùng một bộ luật / cùng một tập số?")
print("=" * 100)


def tap_so(s):
    return set(SO2.findall(s))


for i in range(len(khoi)):
    for j in range(i + 1, len(khoi)):
        a, b = khoi[i], khoi[j]
        sa, sb = tap_so(a[1]), tap_so(b[1])
        if len(sa) < 5 or len(sb) < 5:
            continue
        chung = sa & sb
        ty = len(chung) / min(len(sa), len(sb))
        if ty >= 0.6:
            print(f"  {a[0][:40]:40} ↔ {b[0][:40]:40} trùng {ty*100:>3.0f}% "
                  f"({len(chung)}/{min(len(sa),len(sb))} số)")

print()
print("=" * 100)
print("BỐN KHỐI NẶNG NHẤT — trích nguyên văn 5 dòng đầu để owner nhìn tận mắt")
print("=" * 100)
for ten, dai, ns, nl, dg in sorted(bang, key=lambda x: -x[1])[:4]:
    noi = next(n for t2, n in khoi if t2 == ten)
    print(f"\n  ── {ten} ({dai:,} ký tự · {ns} số · {nl} mệnh lệnh) {dg}")
    for d in [x for x in noi.splitlines() if x.strip()][:5]:
        print(f"     {d[:104]}")
