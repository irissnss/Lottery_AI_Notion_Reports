# -*- coding: utf-8 -*-
"""V11017 — deploy: bảng đo BẦY ĐÀN (phép đo CƠ CHẾ của V11016) + API + panel + cron.

Ba tệp: `_v11017_bay_dan_shadow.py` (mới) · `main.py` (thêm 1 endpoint admin) ·
`monitoring.html` (thêm 1 panel, đăng ký ở CẢ HAI chỗ theo §52B).

CỔNG TRƯỚC KHI RESTART — không đạt thì KHÔNG restart:
  1. ba tệp lên đủ, md5 khớp
  2. `compute()` chạy được TRÊN VPS và ghi ra dòng
  3. `view()` trả về đúng cấu trúc, cờ an toàn đủ 4
  4. băm 4 bảng khoá TRƯỚC = SAU
  5. so PID trước/sau · `/api/health`=200 · endpoint admin **=401** khi không đăng nhập
"""
import hashlib
import io
import json
import sys
import time

import paramiko

sys.stdout.reconfigure(encoding="utf-8")

R = "/root/Lottery_AI_Test"
PY_VENV = f"{R}/venv/bin/python3"
TEP = ["web/backend/_v11017_bay_dan_shadow.py",
       "web/backend/main.py",
       "web/frontend/monitoring.html"]
BANG_KHOA = ("predictions", "final_bundles", "lottery_results", "model_daily_eval")
CRON = ("5 19 * * * cd /root/Lottery_AI_Test/web/backend && "
        "/root/Lottery_AI_Test/venv/bin/python3 _v11017_bay_dan_shadow.py "
        ">> /root/Lottery_AI_Test/logs/v11017_bay_dan.log 2>&1")

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
cli.connect("14.225.224.89", username="root",
            key_filename=r"C:\Users\Admin\.ssh\id_ed25519", timeout=60)


def r(c, t=300):
    _i, o, e = cli.exec_command(c, timeout=t)
    return (o.read().decode("utf-8", "replace") + e.read().decode("utf-8", "replace")).strip()


def bam4():
    return {b: r(f"cd {R} && sqlite3 data/lottery_ai.db "
                 f"\"SELECT COUNT(*)||'|'||COALESCE(MAX(rowid),0) FROM {b}\"")
            for b in BANG_KHOA}


print("=" * 92)
print("  V11017 DEPLOY — bảng đo BẦY ĐÀN + API + panel + cron")
print("=" * 92)
pid_truoc = r("systemctl show -p MainPID --value lottery")
bam_truoc = bam4()
print(f"  PID trước    : {pid_truoc}")
print(f"  4 bảng TRƯỚC : {bam_truoc}")

# ── cổng 1: đẩy ba tệp, so md5 ────────────────────────────────────────────────
sftp = cli.open_sftp()
r(f"mkdir -p {R}/backups {R}/logs")
for f in TEP:
    # `cp -n`: KHÔNG ghi đè bản sao lưu nếu đã có. Chạy deploy lần hai mà ghi đè là
    # bản "pre" thành bản đã deploy — mất luôn đường gỡ về.
    r(f"cp -n {R}/{f} {R}/backups/$(basename {f}).v11017_pre 2>/dev/null")
    sftp.put(f, f"{R}/{f}")
sftp.close()
lech = []
for f in TEP:
    a = hashlib.md5(io.open(f, "rb").read()).hexdigest()
    b = r(f"md5sum {R}/{f} | cut -d' ' -f1")
    print(f"  md5 {f.split('/')[-1]:<28} {'✓ KHỚP' if a == b else '✗ LỆCH'}")
    if a != b:
        lech.append(f)
if lech:
    print("  ✗ DỪNG — tệp lên không nguyên vẹn:", lech)
    raise SystemExit(1)

bd = r(f"cd {R} && {PY_VENV} -m py_compile web/backend/main.py "
       f"web/backend/_v11017_bay_dan_shadow.py && echo OK")
print(f"  py_compile   : {bd[:50] or 'KHÔNG RA GÌ'}")
if "OK" not in bd:
    print("  ✗ DỪNG — không biên dịch được")
    raise SystemExit(1)

# ── cổng 2+3: chạy compute() và view() TRÊN VPS ───────────────────────────────
out = r(f"cd {R}/web/backend && {PY_VENV} -c \""
        f"import json,sys,io; _t=sys.stdout; sys.stdout=io.StringIO(); "
        f"import _v11017_bay_dan_shadow as M; c=M.compute(); v=M.view(); "
        f"sys.stdout=_t; "
        f"print('@@@'+json.dumps({{'compute':c,'ok':v.get('success'),"
        f"'an_toan':v.get('an_toan'),'nen_n':v['nen']['n'],'nen_tb':v['nen']['trung_binh'],"
        f"'sau_n':v['sau_v11016']['n'],'ket':v.get('ket_luan')}}))\"", t=600)
kq = None
for l in out.splitlines():
    if l.startswith("@@@"):
        kq = json.loads(l[3:])
if not kq or not kq.get("ok"):
    print("  ✗ DỪNG — compute/view lỗi trên VPS:\n", out[-800:])
    raise SystemExit(1)
print(f"  compute()    : ghi {kq['compute']['so_dong']} dòng "
      f"({kq['compute']['tu_ngay']} → {kq['compute']['den_ngay']})")
print(f"  view()       : nền n={kq['nen_n']} tb={kq['nen_tb']:.3f} · "
      f"sau n={kq['sau_n']} · kết luận={kq['ket']}")
an = kq.get("an_toan") or {}
du_co = (an.get("output_eligible") == 0 and an.get("diagnostic_only") == 1
         and an.get("owner_approved") == 0 and an.get("shadow_only") == 1)
print(f"  cờ an toàn   : {an} {'✓ ĐỦ 4' if du_co else '✗ THIẾU'}")
if not du_co or kq["compute"]["so_dong"] < 30:
    print("  ✗ DỪNG — cờ an toàn thiếu hoặc ghi quá ít dòng")
    raise SystemExit(1)

# ── cron ──────────────────────────────────────────────────────────────────────
co_cron = r("crontab -l 2>/dev/null | grep -c '_v11017_bay_dan_shadow'")
if co_cron.strip() == "0":
    r(f"(crontab -l 2>/dev/null; echo '{CRON}') | crontab -")
n_cron = r("crontab -l 2>/dev/null | grep -c '_v11017_bay_dan_shadow'")
tong_cron = r("crontab -l 2>/dev/null | grep -vc '^#\\|^$'")
print(f"  cron         : {n_cron} dòng (19:05 mỗi ngày, sau khi MB chốt 17:58) · "
      f"tổng crontab {tong_cron}")

# ── restart ───────────────────────────────────────────────────────────────────
print()
print("  restart service `lottery` …")
r("systemctl restart lottery")
time.sleep(9)
pid_sau = r("systemctl show -p MainPID --value lottery")
health = r("curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8000/api/health")
admin = r("curl -s -o /dev/null -w '%{http_code}' "
          "http://127.0.0.1:8000/api/admin/bay-dan-shadow")
nostore = r("curl -s -D- -o /dev/null http://127.0.0.1:8000/api/admin/bay-dan-shadow "
            "| grep -ci 'cache-control: no-store'")
bam_sau = bam4()

print(f"  PID sau      : {pid_sau}  "
      f"{'✓ ĐÃ ĐỔI' if pid_sau != pid_truoc else '✗ KHÔNG ĐỔI — tiến trình cũ còn sống!'}")
print(f"  /api/health  : {health}")
print(f"  endpoint admin (chưa đăng nhập): {admin}  "
      f"{'✓ đúng 401' if admin == '401' else '✗ PHẢI là 401'}")
print(f"  4 bảng SAU   : {bam_sau}")
giu = all(bam_truoc[b] == bam_sau[b] for b in BANG_KHOA)
print(f"  4 bảng khoá  : {'✓ Y HỆT' if giu else '✗ ĐÃ ĐỔI — kiểm tay ngay'}")

print()
print("=" * 92)
tot = (pid_sau != pid_truoc) and health == "200" and admin == "401" and giu
print("  " + ("✓ DEPLOY ĐẠT" if tot else "✗ DEPLOY CÓ VẤN ĐỀ — xem lại"))
print(f"  Gỡ về: for f in {' '.join(x.split('/')[-1] for x in TEP)}; do "
      f"cp {R}/backups/$f.v11017_pre <đúng đường dẫn>; done && systemctl restart lottery")
print(f"  Gỡ cron: crontab -l | grep -v _v11017_bay_dan_shadow | crontab -")
print("=" * 92)
cli.close()
raise SystemExit(0 if tot else 1)
