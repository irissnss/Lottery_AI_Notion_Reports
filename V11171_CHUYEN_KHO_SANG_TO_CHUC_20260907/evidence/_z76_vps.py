# -*- coding: utf-8 -*-
"""BANG KIEM THONG SUOT GITHUB — phia VPS. Khong ghi gi len remote."""
import subprocess, json, datetime
E = 'GIT_SSH_COMMAND="ssh -o BatchMode=yes -o ConnectTimeout=25" GIT_TERMINAL_PROMPT=0 '
def sh(c, t=90):
    try:
        r = subprocess.run(c, shell=True, capture_output=True, text=True, timeout=t)
        return r.returncode, (r.stdout + r.stderr).strip()
    except subprocess.TimeoutExpired:
        return 124, "QUA GIO"

KQ = []
def thu(ten, mong, cmd, dat=None):
    rc, o = sh(cmd)
    ok = dat(rc, o) if dat else (rc == 0)
    KQ.append({"ten": ten, "mong": mong, "dat": bool(ok), "rc": rc, "ra": o[:200].replace("\n", " | ")})
    print("  %s  %-50s %s" % ("✓" if ok else "✗", ten, "" if ok else "→ " + o[:100].replace("\n", " ")))

S = "git@github.com:%s/Lottery_AI_Test.git"
print("=" * 92)
print("  F · VPS → KHO RIENG qua SSH (deploy key)")
print("=" * 92)
thu("doc duong MOI (ls-remote)", "?", E + "git ls-remote " + S % "BaoBiTanPhat" + " HEAD")
thu("doc duong CU  (ls-remote)", "?", E + "git ls-remote " + S % "irissnss" + " HEAD")
thu("remote dang cau hinh tro to chuc moi", "phai dung",
    "git -C /root/Lottery_AI_Test remote get-url origin",
    dat=lambda rc, o: rc == 0 and "BaoBiTanPhat" in o)

print()
print("=" * 92)
print("  G · VPS co CAN GitHub de chay khong")
print("=" * 92)
rc, o = sh("crontab -l 2>/dev/null | grep -c 'git pull\\|git fetch'")
thu("0 cron nao git pull/fetch (crontab root)", "phai 0",
    "crontab -l 2>/dev/null | grep -c 'git pull\\|git fetch' || true",
    dat=lambda rc, o: o.strip() in ("0", ""))
thu("0 cron nao git pull/fetch (/etc/cron.d)", "phai 0",
    "grep -rl 'git pull\\|git fetch' /etc/cron.d 2>/dev/null | wc -l",
    dat=lambda rc, o: o.strip() == "0")
thu("service chay tu tep tren dia (khong tu git)", "phai dung",
    "systemctl show -p ExecStart --value lottery",
    dat=lambda rc, o: "/root/Lottery_AI_Test/venv/bin/python3" in o)
thu("service dang chay, khong restart", "phai NRestarts=0",
    "systemctl show -p NRestarts --value lottery", dat=lambda rc, o: o.strip() == "0")
thu("health 200", "phai 200",
    "curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8000/api/health",
    dat=lambda rc, o: o.strip().endswith("200"))

print()
print("=" * 92)
print("  H · DANH TINH khoa SSH cua VPS")
print("=" * 92)
rc, o = sh(E + "ssh -o StrictHostKeyChecking=no -T git@github.com")
print("  ", (o.split("\n")[0] if o else "(rong)")[:150])
KQ.append({"ten": "danh tinh SSH VPS", "mong": "-", "dat": True, "rc": rc,
           "ra": (o.split("\n")[0] if o else "")[:200]})

dat = sum(1 for k in KQ if k["dat"] and k["ten"] != "danh tinh SSH VPS")
tong = sum(1 for k in KQ if k["ten"] != "danh tinh SSH VPS")
print()
print("  TONG VPS: %d/%d DAT" % (dat, tong))
for k in KQ:
    if not k["dat"]:
        print("  ✗ %s\n      ra: %s" % (k["ten"], k["ra"]))
open("/root/Lottery_AI_Test/artifacts/v11171_matran_vps.json", "w", encoding="utf-8").write(
    json.dumps({"chay_luc": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "dat": dat, "tong": tong, "muc": KQ}, ensure_ascii=False, indent=1))
print("  da ghi artifacts/v11171_matran_vps.json")
