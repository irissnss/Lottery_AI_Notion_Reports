# -*- coding: utf-8 -*-
"""V11016 — đo TRƯỚC/SAU bằng CÙNG MỘT THƯỚC, chạy trong đúng thư mục thật (có DB).

Bản TRƯỚC được nạp thành module tạm `_v11016_pre_gpt` đặt cạnh bản thật rồi XOÁ ngay sau khi
đo — không để lại tệp lạ trong kho. CHỈ ĐỌC, không ghi bảng nào.
"""
import importlib
import io
import os
import re
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")
BE = os.path.join(os.getcwd(), "web", "backend")
PRE = os.path.join(os.getcwd(), "backups", "v11016_pre", "gpt_analyzer.py.pre")
TAM = os.path.join(BE, "_v11016_pre_gpt.py")
os.chdir(BE)
sys.path.insert(0, BE)

SO = re.compile(r"(?<!\d)\d{2}(?!\d)")
LENH = re.compile(r"BẮT BUỘC|PHẢI |CẤM |KHÔNG ĐƯỢC|ƯU TIÊN TUYỆT ĐỐI|BUỘC PHẢI|MANDATE")
MIEN = ("MB", "MT", "MN")
NGAY = "2026-08-07"


def tach_khoi(cp):
    ra, ten, buf = [], None, []
    for l in cp.splitlines():
        if l.startswith("### "):
            if ten:
                ra.append((ten, "\n".join(buf)))
            ten, buf = l[4:].strip()[:44], []
        else:
            buf.append(l)
    if ten:
        ra.append((ten, "\n".join(buf)))
    return ra


def do(cp):
    kh = [(t, set(SO.findall(b))) for t, b in tach_khoi(cp)]
    kh = [(t, s) for t, s in kh if len(s) >= 3]
    cap = 0
    for i in range(len(kh)):
        for j in range(i + 1, len(kh)):
            a, b = kh[i][1], kh[j][1]
            if len(a & b) / max(min(len(a), len(b)), 1) >= 0.60:
                cap += 1
    return {"ký tự": len(cp), "khối": len(tach_khoi(cp)), "số hai chữ số": len(SO.findall(cp)),
            "mệnh lệnh": len(LENH.findall(cp)), "cặp khối trùng ≥60%": cap,
            "dòng ≥6 số một dòng": sum(1 for l in cp.splitlines() if len(SO.findall(l)) >= 6)}


def gom(mod):
    _t = sys.stdout
    sys.stdout = io.StringIO()
    try:
        return {m: mod.build_context_pack(m, NGAY) for m in MIEN}
    finally:
        sys.stdout = _t


try:
    shutil.copy2(PRE, TAM)
    truoc = gom(importlib.import_module("_v11016_pre_gpt"))
    sau = gom(importlib.import_module("gpt_analyzer"))
finally:
    if os.path.exists(TAM):
        os.remove(TAM)
    for c in (os.path.join(BE, "__pycache__", "_v11016_pre_gpt.cpython-311.pyc"),):
        if os.path.exists(c):
            os.remove(c)

print("=" * 100)
print("  CÙNG MỘT THƯỚC, HAI BẢN — trước V11016 (PB-19.0) vs sau V11016 (PB-20.0)")
print("=" * 100)
for m in MIEN:
    a, b = do(truoc[m]), do(sau[m])
    print(f"\n  ── {m} " + "─" * 88)
    print(f"     {'chỉ số':<26} {'TRƯỚC':>9} {'SAU':>9} {'đổi':>9}")
    for k in a:
        print(f"     {k:<26} {a[k]:>9,} {b[k]:>9,} {b[k] - a[k]:>+9,}")

print()
print("  " + "=" * 96)
print("  RỔ SỐ DỌN SẴN — dòng đưa ≥6 đuôi cùng lúc (thứ owner gọi là «bộ số định sẵn»)")
print("  " + "=" * 96)
for nhan, goi in (("TRƯỚC", truoc), ("SAU  ", sau)):
    xau = [l.strip() for l in goi["MB"].splitlines() if len(SO.findall(l)) >= 6]
    print(f"\n  {nhan} — MB có {len(xau)} dòng:")
    for l in xau[:6]:
        print(f"     {l[:104]}")
