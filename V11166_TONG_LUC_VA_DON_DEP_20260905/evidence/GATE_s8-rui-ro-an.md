# s8-rui-ro-an · tang=PARTIAL

## TOM TAT

CONG 8 — RUI RO CHUA AI THEO DOI. Dao 16 phat hien: 3 P0, 6 P1, 5 P2, 2 P3. Trong do 9/16 KHONG XUAT HIEN trong bat ky so quan tri nao (quet 8 so: FOLLOW_UP_TRACKER, CURRENT_TRUTH_SSOT, AUTOMATION_STATE, AUTOMATION_HISTORY, CHANGELOG, DECISION_LOG, CHANGELOG_GOVERNANCE_LEDGER, 6 ACTIVE_ROADMAP).

BA VIEC P0 — deu la rui ro ha tang, khong phai rui ro thuat toan:
1) KHONG CO BAT KY SAO LUU NAO NGOAI MAY. crontab khong co dong backup/rsync/scp/rclone nao; khong cai rclone/restic/borg; cron aaPanel chi co 1 viec la gia han SSL. Ba ban sao toan may cuoi cung (11,8 GB, ngay 17/04) vua bi don dep xoa luc 21:04 HOM NAY. Moi ban lottery_ai.db con lai deu nam tren cung o /dev/vda1.
2) SSH mo cho root bang MAT KHAU ra Internet, root co mat khau dung duoc ($5$ SHA-256), fail2ban inactive, 49.517 lan 'Failed password' trong auth.log hien tai, dang bi do lien tuc (3 IP trong 3 phut luc do).
3) KHONG CO SWAP tren may 3.911 MB, OOM-killer da ban 6 lan/30 ngay (hai lan rang sang 05/09, moi lan giet mot python3 ~2,7 GB), service lottery tung dat dinh VmPeak 2,79 GB voi MemoryMax=infinity va OOMScoreAdjust=0.

DIEM MU LON NHAT — cau tra loi cho "ai se biet?": KHONG AI. Bang system_alerts co dung 9 dong trong ca doi, ngung ghi tu 11/05 (117 ngay), 8/9 con treo ke ca mot dong CRITICAL tu 25/04 (133 ngay). Chi co MOT diem ghi (scheduler.py:6854) va no chi bat mot tinh huong hep. Khong su kien ha tang nao — day dia, OOM, do mat khau, het quota — co duong di den bat ky mat canh bao nao. O dia da len 81% ma khong co cron nao kiem, khong co ma nao doc dung luong dia (grep shutil.disk_usage/statvfs/free_space tren web/backend/*.py = RONG).

DA KIEM VA SACH (ghi lai de khoi do lai): gia thuyet lech ten bien LLM_CONTEXT_ONLY_V2 la SAI — gpt_analyzer.py:911 doc dung ten unit dat; ba cong an toan cua owner deu mac dinh dung chieu an toan; chung chi TLS con 57 ngay va certbot chay dung; nguon cao ket qua co du phong 3 trang; 0 nguon ngau nhien trong 4 tep serve chinh; cua so van hanh 190 ngay x 3 mien = 570 bundle, THIEU 0.

Production nguyen ven: neo558 a82c508d3569abda, predictions 14282, final_bundles 570, lottery_results 15424, model_daily_eval 14146 — trung khop moc V11165 GATE 0. PID 3370750 khong doi, NRestarts 0, health 200.

## VIEC CAN LAM

Sap theo muc do. Cong 8 la phien SOI nen day la DE XUAT, chua lam gi.

P0 — ba viec, deu can owner quyet vi deu dung den ha tang may san xuat:
1. [S8-01] Dung mot duong sao luu DB ra NGOAI may. Ai chan: owner (can quyet dich den va chi phi
   luu tru). O dau: crontab tren VPS + mot dich luu tru ngoai. Toi thieu: ban nen (sqlite3 .backup,
   khong copy tep dang WAL) hang ngay, giu 7-14 ban, kem kiem tra phuc hoi thu. Luu y o dia chi
   con 23 G nen ban nen phai nen va day di ngay, khong tich tren may.
2. [S8-02] Dong duong do mat khau SSH. Ai chan: owner (vi doi cach dang nhap cua chinh owner).
   O dau: /etc/ssh/sshd_config. Ba buoc doc lap nhau, lam duoc tung buoc: bat fail2ban (re nhat,
   khong doi thoi quen); PasswordAuthentication no sau khi da xac nhan khoa cong khai vao duoc;
   PermitRootLogin prohibit-password. Kem: xem lai vi sao ufw dang mo 21/tcp (FTP mat khau ro).
3. [S8-03] Them swap va dat tran bo nho cho service. Ai chan: owner. O dau: swapfile 2-4 G +
   MemoryMax cho lottery.service + OOMScoreAdjust am de service khong bi chon lam nan nhan.
   Truoc khi dat MemoryMax phai do dinh that (VmPeak hien 2,79 G) keo dat thap qua lai tu giet.

P1 — sau viec:
4. [S8-05] Hoi sinh kenh canh bao. Ai chan: khong ai, la viec ky thuat. O dau: scheduler.py:6854
   la diem ghi duy nhat — can them cac loai canh bao dia/RAM/OOM/quota. Va xu 8 dong dang treo,
   trong do co mot CRITICAL tu 25/04 (ROW_DEFICIT 14/21 dong) chua ai doc.
5. [S8-04] Them cong kiem dia (nguong 80%) noi vao S8-05. Ai chan: khong ai. O dau: cron + ma.
6. [S8-06] Dong bo docs len VPS hoac quyet dinh tuong minh la KHONG dong bo. Ai chan: owner —
   day la cau hoi thiet ke, khong phai loi: neu docs chi song o repo local thi phai ghi ro dieu do
   o mot cho, keo lan sau lai co agent doc ban tren VPS va tin. O dau: docs/ tren VPS + git VPS.
7. [S8-07] Xoa hoac doi ten web/backend/.env. Ai chan: owner (vi trong do co khoa that, phai xac
   nhan la khoa cu truoc khi xoa). O dau: /root/Lottery_AI_Test/web/backend/.env. Kem: sua bon
   script dang goi load_dotenv() tran cho tro dung env_loader.load_project_env().
8. [S8-08] Cap khoa rieng cho it nhat model OFFICIAL gpt-oss-120b, hoac chap nhan rui ro va ghi
   vao so. Ai chan: owner (chi phi + tai khoan). O dau: .env goc hoac app_settings.
9. [S8-09] Ra soat 15 bang im ma van duoc doc: hoac bat writer chay lai, hoac gan nhan "du lieu
   tinh den ngay X" o panel, hoac go diem doc. Ai chan: khong ai cho phan gan nhan. O dau: main.py.

P2 — nam viec:
10. [S8-10] Dung muc theo doi bien an toan cho MT (mien mong nhat, hien khong co muc nao).
    Va xem lai AI_MODEL_HARD_TIMEOUT_SEC 300 giay so voi bien MT thuc te.
11. [S8-11] Them logrotate cho scraper.log, prediction_trace.jsonl va /www/server/data/*.err.
    Rieng tep .err 222 MB: tim vi sao co ket noi MariaDB moi 10 giay roi ngat khong xac thuc.
12. [S8-12] Quyet dinh co con can aaPanel/MariaDB/FTP khong. Ai chan: owner. Neu khong dung thi
    tat di se tra lai khoang 213 MB RAM cho c

## PHAT HIEN
  [P0][PROVEN_DEFECT] S8-01 — KHONG CO BAN SAO LUU NAO NGOAI MAY, va ba ban sao toan may cuoi cung vua bi xoa hom nay
  [P0][PROVEN_DEFECT] S8-02 — SSH mo cho root bang mat khau, khong fail2ban, dang bi do mat khau lien tuc
  [P0][PROVEN_DEFECT] S8-03 — Khong co swap, OOM-killer da ban 6 lan trong 30 ngay, service khong duoc bao ve
  [P1][PROVEN_DEFECT] S8-04 — KHONG CO BAT KY CO CHE THEO DOI O DIA; o dia da len 81% ma khong co may nao biet
  [P1][PROVEN_DEFECT] S8-05 — KENH CANH BAO DA CHET: system_alerts im 117 ngay, 8/9 canh bao con treo, co ca mot CRITICAL 133 ngay
  [P1][PROVEN_DEFECT] S8-06 — Tai lieu quan tri TREN CHINH MAY SAN XUAT cu 27 den 96 ngay; git tren VPS dung tu 15/06
  [P1][PROVEN_DEFECT] S8-07 — HAI tep .env voi BA khoa API khac nhau; ban cu nam dung trong thu muc lam viec cua service
  [P1][OPERATIONAL_IMPROVEMENT] S8-08 — 14 model OpenRouter dung CHUNG mot khoa; 21 bien khoa rieng khai bao trong ma deu rong
  [P1][PROVEN_DEFECT] S8-09 — 15 bang im tren 30 ngay VAN DUOC MA DANG SERVE DOC; cung ho RM-20 nhung nhieu hon 14 ca so voi ban goc
  [P2][PROVEN_DEFECT] S8-10 — Bien an toan 2 phut cua MT DA TUNG BI VUOT: bundle chot 16:57:32, cach moc dong bang 28 giay
  [P2][OPERATIONAL_IMPROVEMENT] S8-11 — Log khong xoay vong o ca hai phia; mot tep loi 222 MB sinh ra tu chinh canh bao cua he
  [P2][OPERATIONAL_IMPROVEMENT] S8-12 — Ca mot he sinh thai aaPanel/MariaDB chay tren may, khong phuc vu du an, tren dung cai may hay OOM
  [P2][OPERATIONAL_IMPROVEMENT] S8-13 — Script deploy nam san tren may san xuat, ngoai tam voi cua cong deploy
  [P2][PROVEN_DEFECT] S8-14 — Chay lai mot ngay KHONG ra ket qua nhu cu: LSTM va meta-learner huan luyen khong gieo hat
  [P3][EXPECTED_BEHAVIOR] S8-15 — Canh bao db_env_drift chay lien tuc 140 ngay, 828 lan, khong ai dong lai
  [P3][NO_ANOMALY_FOUND] S8-16 — Lo hong lich su ket qua deu giai thich duoc; cua so van hanh KHONG thieu mot bundle nao