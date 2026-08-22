# -*- coding: utf-8 -*-
"""FU-419 — DUMP gói ngữ cảnh cho ba miền, dùng làm mốc TRƯỚC / SAU.

Chạy TRÊN VPS (nguồn production, RM-13 / RM-14: prompt thật phải dump từ hàm ĐANG SERVE).
Ghi ra tệp để so diff, và in SHA256 để chứng minh tái lập được (RM-11).
"""
import hashlib
import io
import os
import sys

sys.path.insert(0, "/root/Lottery_AI_Test/web/backend")
os.chdir("/root/Lottery_AI_Test/web/backend")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from gpt_analyzer import build_context_pack, PROMPT_VERSIONS  # noqa: E402

NHAN = sys.argv[1] if len(sys.argv) > 1 else "dump"
NGAY = sys.argv[2] if len(sys.argv) > 2 else "2026-08-24"
RA = f"/tmp/fu419_{NHAN}"
os.makedirs(RA, exist_ok=True)

print(f"CTX hien tai: {PROMPT_VERSIONS['context_pack']}")
for mien in ("MN", "MT", "MB"):
    goi = build_context_pack(mien, NGAY)
    duong = f"{RA}/{mien}.txt"
    with io.open(duong, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(goi)
    h = hashlib.sha256(goi.encode("utf-8")).hexdigest()[:16]
    dong_d1 = [l for l in goi.splitlines() if "D-1 cross-region tail pool" in l]
    print(f"{mien}: {len(goi)} ky tu · sha256 {h}")
    print(f"   dong D-1: {dong_d1[0][:110] if dong_d1 else '(KHONG CO DONG NAY)'}")

# tai lap: goi lai lan hai, phai ra cung SHA256
print("\nKIEM TAI LAP (goi lai lan hai, cung dau vao):")
for mien in ("MN", "MT", "MB"):
    a = hashlib.sha256(build_context_pack(mien, NGAY).encode("utf-8")).hexdigest()[:16]
    b = hashlib.sha256(io.open(f"{RA}/{mien}.txt", encoding="utf-8").read().encode("utf-8")).hexdigest()[:16]
    print(f"   {mien}: {'KHOP' if a == b else 'LECH'} ({a} vs {b})")
