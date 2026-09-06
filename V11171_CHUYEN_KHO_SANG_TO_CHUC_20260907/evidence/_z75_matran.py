# -*- coding: utf-8 -*-
"""BANG KIEM THONG SUOT GITHUB — MOI TRUONG HOP, chay tu MAY LOCAL.

Khong ghi gi len remote: chi dung ls-remote va push --dry-run.
"""
import subprocess, sys, io, os, json, datetime
sys.stdout.reconfigure(encoding="utf-8")

CU, MOI = "irissnss", "BaoBiTanPhat"
RIENG, CONG = "Lottery_AI_Test", "Lottery_AI_Notion_Reports"
LOCAL_RIENG = r"E:\Lottery_AI_Test"
LOCAL_CONG = r"E:\Lottery_AI_Notion_Reports"
ENV = dict(os.environ, GIT_SSH_COMMAND="ssh -o BatchMode=yes -o ConnectTimeout=25",
           GIT_TERMINAL_PROMPT="0")

def chay(cmd, cwd=None, t=90):
    try:
        r = subprocess.run(cmd, shell=True, cwd=cwd, env=ENV,
                           capture_output=True, text=True, timeout=t)
        return r.returncode, (r.stdout + r.stderr).strip()
    except subprocess.TimeoutExpired:
        return 124, "QUA GIO"

KQ = []
def thu(nhom, ten, mong, cmd, cwd=None, dat=None):
    rc, out = chay(cmd, cwd)
    ok = dat(rc, out) if dat else (rc == 0)
    KQ.append({"nhom": nhom, "ten": ten, "mong": mong,
               "dat": bool(ok), "rc": rc, "ra": out[:200].replace("\n", " | ")})
    print("  %s  %-52s %s" % ("✓" if ok else "✗", ten, "" if ok else "→ " + out[:110].replace("\n", " ")))

S = "git@github.com:%s/%s.git"
H = "https://github.com/%s/%s.git"
RAW = "https://raw.githubusercontent.com/%s/%s/main/README.md"

print("=" * 96)
print("  A · LOCAL → KHO RIENG (private) qua SSH")
print("=" * 96)
thu("A", "doc duong MOI  (ls-remote)", "phai duoc", "git ls-remote %s HEAD" % (S % (MOI, RIENG)))
thu("A", "doc duong CU   (ls-remote, qua chuyen huong)", "phai duoc", "git ls-remote %s HEAD" % (S % (CU, RIENG)))
thu("A", "GHI thu (push --dry-run) tu thu muc lam viec", "phai duoc",
    "git push --dry-run origin HEAD", cwd=LOCAL_RIENG)
thu("A", "remote dang cau hinh tro dung to chuc moi", "phai dung",
    "git remote get-url origin", cwd=LOCAL_RIENG,
    dat=lambda rc, o: rc == 0 and MOI in o and CU not in o)

print()
print("=" * 96)
print("  B · LOCAL → KHO CONG KHAI (public) qua SSH")
print("=" * 96)
thu("B", "doc duong MOI  (ls-remote)", "phai duoc", "git ls-remote %s HEAD" % (S % (MOI, CONG)))
thu("B", "doc duong CU   (ls-remote, qua chuyen huong)", "phai duoc", "git ls-remote %s HEAD" % (S % (CU, CONG)))
thu("B", "GHI thu (push --dry-run) tu thu muc lam viec", "phai duoc",
    "git push --dry-run origin HEAD", cwd=LOCAL_CONG)
thu("B", "remote dang cau hinh tro dung to chuc moi", "phai dung",
    "git remote get-url origin", cwd=LOCAL_CONG,
    dat=lambda rc, o: rc == 0 and MOI in o and CU not in o)

print()
print("=" * 96)
print("  C · NGUOI NGOAI doc kho CONG KHAI (khong dang nhap) — bao cao phai xem duoc")
print("=" * 96)
thu("C", "HTTPS an danh, duong MOI", "phai duoc", "git ls-remote %s HEAD" % (H % (MOI, CONG)))
thu("C", "HTTPS an danh, duong CU", "phai duoc", "git ls-remote %s HEAD" % (H % (CU, CONG)))
thu("C", "raw.githubusercontent duong MOI", "phai 200",
    'curl -s -o /dev/null -w "%%{http_code}" ' + RAW % (MOI, CONG),
    dat=lambda rc, o: o.strip().endswith("200"))
thu("C", "raw.githubusercontent duong CU", "phai 200",
    'curl -s -o /dev/null -w "%%{http_code}" ' + RAW % (CU, CONG),
    dat=lambda rc, o: o.strip().endswith("200"))
thu("C", "trang web duong CU chuyen huong sang to chuc", "phai 301",
    'curl -s -o /dev/null -w "%%{http_code}|%%{redirect_url}" https://github.com/%s/%s' % (CU, CONG),
    dat=lambda rc, o: "301" in o and MOI in o)

print()
print("=" * 96)
print("  D · TINH RIENG TU cua kho RIENG con nguyen khong (phai bi TU CHOI)")
print("=" * 96)
thu("D", "HTTPS an danh doc kho RIENG duong MOI", "phai BI TU CHOI",
    "git ls-remote %s HEAD" % (H % (MOI, RIENG)), dat=lambda rc, o: rc != 0)
thu("D", "HTTPS an danh doc kho RIENG duong CU", "phai BI TU CHOI",
    "git ls-remote %s HEAD" % (H % (CU, RIENG)), dat=lambda rc, o: rc != 0)
thu("D", "raw kho RIENG (an danh)", "phai KHAC 200",
    'curl -s -o /dev/null -w "%%{http_code}" ' + RAW % (MOI, RIENG),
    dat=lambda rc, o: not o.strip().endswith("200"))

print()
print("=" * 96)
print("  E · DANH TINH KHOA SSH cua may local")
print("=" * 96)
rc, o = chay("ssh -o BatchMode=yes -o ConnectTimeout=25 -T git@github.com")
print("  ", o.split("\n")[0][:150] if o else "(rong)")
KQ.append({"nhom": "E", "ten": "danh tinh SSH local", "mong": "-", "dat": True, "rc": rc,
           "ra": o.split("\n")[0][:200] if o else ""})

dat = sum(1 for k in KQ if k["dat"] and k["nhom"] != "E")
tong = sum(1 for k in KQ if k["nhom"] != "E")
print()
print("=" * 96)
print("  TONG LOCAL: %d/%d DAT" % (dat, tong))
print("=" * 96)
for k in KQ:
    if not k["dat"]:
        print("  ✗ [%s] %s\n      mong: %s\n      ra  : %s" % (k["nhom"], k["ten"], k["mong"], k["ra"]))

io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "_matran_local.json"),
        "w", encoding="utf-8", newline="\n").write(
    json.dumps({"chay_luc": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "dat": dat, "tong": tong, "muc": KQ}, ensure_ascii=False, indent=1))
print("\n  da ghi _matran_local.json")
