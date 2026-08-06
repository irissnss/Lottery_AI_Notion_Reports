# -*- coding: utf-8 -*-
"""V11001 — kiem prompt con sach gan/nong/lanh khong. CHI DOC.

So quyet dinh goi bo nay moi phien. Quet TOAN BO chuoi hang se gui cho model trong
gpt_analyzer.py; chi duoc con DUNG MOT dong nhac gan — cau G3 noi dung.
"""
from __future__ import annotations
import ast, io, os, re, sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

H = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(H, "gpt_analyzer.py"), encoding="utf-8").read()

MAU = r"\bGAN\b|\bCOLD\b|HOT zone|Hot/Warm|KB Gan|Cold number|SỐ SẮP ĐẾN CHU KỲ|GAN ĐÀI"
GIU = 'GAN cao KHÔNG có nghĩa "sắp ra" — chỉ là thông tin tham khảo'

con = set()
for n in ast.walk(ast.parse(src)):
    if isinstance(n, ast.Constant) and isinstance(n.value, str):
        for l in n.value.splitlines():
            if re.search(MAU, l):
                con.add(l.strip())

truot = []
print("  dong nhac gan/nong/lanh trong chuoi gui di: %d" % len(con))
for l in sorted(con):
    giu = GIU in l
    print("     %s %s" % ("GIU " if giu else "!!  ", l[:88]))
    if not giu:
        truot.append(l[:60])

# phien ban phai da tang
for cap in ("'system_prompt':       'SP-4.2'", "'context_pack':        'CTX-16.6'",
            "'prompt_bundle':       'PB-18.2'"):
    if cap not in src:
        truot.append("chua tang phien ban: %s" % cap.split("'")[3])

if truot:
    print("  X TRUOT:")
    for x in truot:
        print("     -", x)
    print("[cong] PROMPT_SACH=TRUOT")
    raise SystemExit(1)
print("  OK — chi con cau G3, va ba phien ban da tang")
print("[cong] PROMPT_SACH=DAT")
