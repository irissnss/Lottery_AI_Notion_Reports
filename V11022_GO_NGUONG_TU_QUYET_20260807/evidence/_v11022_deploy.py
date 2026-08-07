# -*- coding: utf-8 -*-
"""V11022 — deploy: SỐ THÀNH LỜI KỂ (L-A) + NGƯỠNG TỰ QUYẾT (L-B).

Owner 07/08 chốt "Làm ngay luôn đi em" cho L-A sau khi được trình đánh đổi (FU-284 thành đo
gộp ba biến). Một tệp: `gpt_analyzer.py`.

CỔNG TRƯỚC KHI RESTART — không đạt thì KHÔNG restart:
  1. tệp trên VPS biên dịch được
  2. gọi thẳng `build_context_pack` TRÊN VPS cho cả 3 miền, kiểm bằng chuỗi thật:
     rổ hợp nhất đã hết · khối kể sự kiện có mặt · ngưỡng tự quyết có mặt · rổ xếp hạng đã hết
  3. băm 4 bảng khoá TRƯỚC = SAU
  4. so PID trước/sau (tên service là `lottery`, KHÔNG phải `lottery-ai`)
"""
import hashlib
import io
import sys

import paramiko

sys.stdout.reconfigure(encoding="utf-8")

R = "/root/Lottery_AI_Test"
TEP = "web/backend/gpt_analyzer.py"
BANG_KHOA = ("predictions", "final_bundles", "lottery_results", "model_daily_eval")

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
cli.connect("14.225.224.89", username="root",
            key_filename=r"C:\Users\Admin\.ssh\id_ed25519", timeout=60)


def r(c, t=300):
    _i, o, e = cli.exec_command(c, timeout=t)
    return (o.read().decode("utf-8", "replace") + e.read().decode("utf-8", "replace")).strip()


def bam4():
    ra = {}
    for b in BANG_KHOA:
        ra[b] = r(f"cd {R} && sqlite3 data/lottery_ai.db "
                  f"\"SELECT COUNT(*)||'|'||COALESCE(MAX(rowid),0) FROM {b}\"")
    return ra


print("=" * 92)
print("  V11022 DEPLOY — GỠ ngưỡng tự quyết (L-B), giữ lời kể (L-A)")
print("=" * 92)

pid_truoc = r("systemctl show -p MainPID --value lottery")
bam_truoc = bam4()
print(f"  PID trước      : {pid_truoc}")
print(f"  4 bảng TRƯỚC   : {bam_truoc}")

# ── đẩy tệp ───────────────────────────────────────────────────────────────────
noi_dung = io.open(TEP, "rb").read()
md5_local = hashlib.md5(noi_dung).hexdigest()
sftp = cli.open_sftp()
r(f"cp -n {R}/{TEP} {R}/backups/gpt_analyzer.py.v11022_pre 2>/dev/null; "
  f"mkdir -p {R}/backups")
sftp.put(TEP, f"{R}/{TEP}")
sftp.close()
md5_vps = r(f"md5sum {R}/{TEP} | cut -d' ' -f1")
print(f"  md5 local/VPS  : {md5_local} / {md5_vps}  "
      f"{'✓ KHỚP' if md5_local == md5_vps else '✗ LỆCH'}")
if md5_local != md5_vps:
    print("  ✗ DỪNG — tệp lên không nguyên vẹn, KHÔNG restart")
    raise SystemExit(1)

# ── cổng 1: biên dịch ─────────────────────────────────────────────────────────
PY_VENV = "/root/Lottery_AI_Test/venv/bin/python3"   # ĐÚNG trình thông dịch service dùng
bd = r(f"cd {R} && {PY_VENV} -m py_compile {TEP} && echo OK")
print(f"  py_compile     : {bd[:60] or 'KHÔNG RA GÌ'}")
if "OK" not in bd:
    print("  ✗ DỪNG — không biên dịch được, KHÔNG restart")
    raise SystemExit(1)

# ── cổng 2: gọi thẳng build_context_pack TRÊN VPS ─────────────────────────────
KIEM = r'''
import io, os, sys, json
sys.path.insert(0, "/root/Lottery_AI_Test/web/backend")
os.chdir("/root/Lottery_AI_Test/web/backend")
_t = sys.stdout; sys.stdout = io.StringIO()
from gpt_analyzer import build_context_pack, PROMPT_VERSIONS
ra = {}
for m in ("MB", "MT", "MN"):
    cp = build_context_pack(m, "2026-08-07")
    ra[m] = {
        "ky_tu": len(cp),
        "ro_hop_nhat_da_het": "tro toi" not in cp and "tr\u1ecf t\u1edbi" not in cp,
        "ke_su_kien": "B\u1ed0I C\u1ea2NH SOI C\u1ea6U" in cp,
        "nguong_tu_quyet_DA_GO": "NG\u01af\u1ee0NG T\u1ef0 QUY\u1ebeT" not in cp,
        "khuyen_ra_it_DA_GO": "Ra \u00edt m\u00e0 ch\u1eafc" not in cp,
        "ro_xep_hang_da_het": "boost=" not in cp,
        "ep_chon_da_het": "B\u1eaeT BU\u1ed8C ch\u1ecdn t\u1eeb DANH S\u00c1CH" not in cp,
    }
ra["_ban"] = {k: PROMPT_VERSIONS[k] for k in
              ("system_prompt", "reasoning_rulebook", "context_pack", "prompt_bundle")}
sys.stdout = _t
print("@@@" + json.dumps(ra))
'''
sftp = cli.open_sftp()
with sftp.open(f"{R}/_v11016_kiem_tam.py", "w") as fh:
    fh.write(KIEM)
sftp.close()
out = r(f"cd {R} && {PY_VENV} _v11016_kiem_tam.py", t=600)
r(f"rm -f {R}/_v11016_kiem_tam.py")

import json
kq = None
for l in out.splitlines():
    if l.startswith("@@@"):
        kq = json.loads(l[3:])
if not kq:
    print("  ✗ DỪNG — không kiểm được prompt trên VPS:\n", out[-700:])
    raise SystemExit(1)

print(f"  phiên bản VPS  : " + " · ".join(f"{k}={v}" for k, v in kq["_ban"].items()))
dat = True
for m in ("MB", "MT", "MN"):
    x = kq[m]
    ok = all(v for k, v in x.items() if k != "ky_tu")
    dat = dat and ok
    print(f"    {m}: {x['ky_tu']:>6,} ký tự · " +
          " · ".join(f"{k}={v}" for k, v in x.items() if k != "ky_tu"))
if not dat:
    print("  ✗ DỪNG — prompt trên VPS không đúng như mong đợi, KHÔNG restart")
    raise SystemExit(1)
print("  ✓ Cổng prompt ĐẠT cả ba miền")

# ── restart ───────────────────────────────────────────────────────────────────
print()
print("  restart service `lottery` …")
r("systemctl restart lottery")
import time
time.sleep(8)
pid_sau = r("systemctl show -p MainPID --value lottery")
health = r("curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8000/api/health")
bam_sau = bam4()

print(f"  PID sau        : {pid_sau}  "
      f"{'✓ ĐÃ ĐỔI' if pid_sau != pid_truoc else '✗ KHÔNG ĐỔI — tiến trình cũ còn sống!'}")
print(f"  /api/health    : {health}")
print(f"  4 bảng SAU     : {bam_sau}")
giu = all(bam_truoc[b] == bam_sau[b] for b in BANG_KHOA)
print(f"  4 bảng khoá    : {'✓ Y HỆT' if giu else '✗ ĐÃ ĐỔI — kiểm tay ngay'}")

print()
print("=" * 92)
tot = (pid_sau != pid_truoc) and health == "200" and giu
print("  " + ("✓ DEPLOY ĐẠT" if tot else "✗ DEPLOY CÓ VẤN ĐỀ — xem lại"))
print(f"  Gỡ về: cp {R}/backups/gpt_analyzer.py.v11022_pre {R}/{TEP} && systemctl restart lottery")
print(f"  Gỡ về local: backups/v11022_pre/gpt_analyzer.py.pre "
      f"(md5 96f6073cadafa73fb1542fe6e9c8e0b6)")
print("=" * 92)
cli.close()
raise SystemExit(0 if tot else 1)
