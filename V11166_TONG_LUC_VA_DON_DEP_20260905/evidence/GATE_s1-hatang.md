# s1-hatang · tang=EVIDENCE_COMPLETE

## TOM TAT

CONG 1 (ha tang & runtime) da do xong tren VPS that, chi doc. He DANG CHAY DUNG o tang ung dung: service PID 3370750 active 1 ngay 19h, NRestarts=0, 93/93 job cron dang bat deu ghi log trong 2 ngay, KHONG co job cron chet, scheduler_logs van ghi den 20:45 VN hom nay, DB quick_check=ok va page_count khop chinh xac kich thuoc tep, khong ro API key o bat ky log nao.

Nhung co BON van de vat ly that, hai cai da XAY RA HOM NAY:

1) KHONG CO BAT KY CO CHE BACKUP NAO. Khong cron backup, khong rclone/restic/borg/duplicity, /www/backup/database va /www/backup/site RONG tu 18/04. Moi ban DB ton tai deu nam tren CUNG mot dia /dev/vda1. Hong dia = mat sach 15.424 lottery_results + 14.282 predictions + 570 final_bundles + 253 bang.

2) HAI LAN OOM KILL THAT NGAY 05/09 (00:19:09 va 00:46:02), global_oom, may co 3.911 MB RAM va KHONG CO SWAP. Ca hai nan nhan la script python 2,6 GiB cua phien audit chay qua SSH. Service song sot, nhung no co MemoryMax=infinity, khong dat OOMScoreAdjust, RSS 726 MB (dinh 955 MB) — la ung vien lon nhat con lai neu lan sau khong co script 2,6 GiB.

3) MOT TIEN TRINH MO COI AN 99,7% CPU LIEN TUC 46,4 GIO (PID 3338582, _run__s5_mat2_ast.py cua phien V11164, bat dau 03/09 22:28:40). May chi co 2 vCPU — no an dung mot loi. syscr dung yen o 2.391, write_bytes=0 => quay vong CPU thuan, khong tien trien.

4) DIA 81%, con 7,44 GiB — va cau tra loi phai tach LAM HAI: neu chi tinh tang TU DONG (DB 4,81-5,64 MiB/ngay + MariaDB err 1,31 MiB/ngay + log app ~1 MiB/ngay = 7,3 MiB/ngay) thi con 1.043 NGAY. Neu giu nhip clone DB cua ba phien audit vua roi (3,23 GB trong 3 ngay) thi con 6,9 NGAY. Rui ro 7 ngay toi la CO, va no den tu THOI QUEN CLONE DB chu khong tu ung dung.

Xoa an toan duoc ~18,9 GB (chu yeu ba tar.gz thang 4/2026 nang 11,8 GB va cac ban DB cu), dua dia ve ~33%.

## VIEC CAN LAM

P0-1 · BACKUP · ai chan: OWNER (can duyet dich den ngoai may va chi phi) · o dau: chua co gi de sua — phai DUNG MOI. Toi thieu: mot job hang dem `sqlite3 lottery_ai.db ".backup"` roi day ra NGOAI /dev/vda1 (may khac / S3 / rclone). Hien khong cai rclone/restic/borg/duplicity. Ghi chu: day la viec duy nhat trong danh sach ma hau qua neu bo qua la KHONG THE DAO NGUOC.

P0-2 · OOM VA SWAP · ai chan: OWNER (them swap doi cham dia, phai chon sau khi don dia) · o dau: (a) tao swapfile 2-4 GB — nhung PHAI don dia truoc vi dang con 7,44 GiB; (b) dat OOMScoreAdjust duong cho cac script audit HOAC MemoryMax cho lottery.service de kernel khong bao gio chon main.py; (c) dat tran RAM cho script audit chay qua SSH. Ghi chu: bang chung hai lan OOM HET HAN 12/09 do journal chi giu 7 ngay — neu muon luu phai chep ra artifact TRUOC ngay do.

P1-3 · TIEN TRINH MO COI PID 3338582 · ai chan: KHONG AI, chi can mot lenh · o dau: `kill 3338582` tren VPS. Phien nay la phien SOI nen toi khong dung toi. No dang an mot trong hai loi vCPU lien tuc tu 03/09 22:28:40. Kiem tra truoc khi kill: `ps -o pid,etimes,pcpu -p 3338582`. Sau khi kill nen xoa /root/Lottery_AI_Test/artifacts/_run__s5_mat2_ast.py hoac sua RX_INS truoc khi chay lai.

P1-4 · DON DIA (~18,9 GB lay lai duoc) · ai chan: OWNER duyet xoa (cac tep >1 GB) · o dau: theo dung thu tu, tep to truoc:
  1. /root/vps_restore_incoming/vps_backup_20260417_233529.tar.gz — 6.456.663.503 B, 18/04/2026, la ban staging cua lan restore da hoan tat (may up 140 ngay ke tu do)
  2. /root/vps_backups/*.tar.gz (2 tep) — 5.381.815.306 B, 17/04/2026, da bi ban tren thay the
  3. artifacts/v11164_audit.db + artifacts/v11159_phan_tich.db — 1.622.364.160 B; lsattr xac nhan ca hai KHONG co co 'i', va da bi v11165_immutable.db (co 'i') thay the
  4. /root/sandbox_v10785 + /root/sandbox_v10793 — 1.577.594.274 B, 05-12/07
  5. /root/.cache/pip — 1.329.546.113 B, ghi lan cuoi 27/03, tai tao duoc
  6. backups/(4 ban DB 30-31/05) — 1.356.956.672 B
  7. /root/lottery_ai.db.pre_wal_20260814 — 707.284.992 B
  8. data/lottery_ai_BACKUP_pre_canon_views_20260530_100748.db — 330.563.584 B
  9. /var/log/btmp.1 — 151.477.632 B · web/backend/logs/optimizer_once.log — 124.454.530 B
  TUYET DOI KHONG XOA: data/lottery_ai.db (+wal/shm) · artifacts/v11165_immutable.db · backups/V11154_deploy_context_only_shadow/ (ban DB gan nhat lam duoc diem go ve, va hien la thu gan giong backup nhat ma he co) · venv/ · .git/ · web/ · docs/ · data/models/*.pkl · /var/log/journal

P1-5 · THEM PHEP DO DIA VAO CONG SUC KHOE · ai chan: khong ai · o dau: web/backend/_v10647_system_health.py (chay moi gio, cron '5 * * * *', hien 16 phep, 0 phep ve dia). Them shutil.disk_usage('/') voi nguong canh bao. Kem theo: mot bang luu lich su de lan sau co duong cong that thay vi phai suy tu mtime. Theo RM-15, cong moi phai kem thu chan that (gia lap dia day => deny/thoat khac 0).

P2-6 · INDEX scheduler_logs · ai chan: khong ai (them index la thao tac ghi DB => phien SUA, khong phai phien n

## PHAT HIEN
  [P0][PROVEN_DEFECT] KHONG CO CO CHE BACKUP NAO — toan bo du lieu nam tren mot dia duy nhat
  [P0][PROVEN_DEFECT] HAI LAN OOM KILL THAT ngay 05/09 — may 3.911 MB RAM, KHONG CO SWAP, service khong duoc bao ve
  [P1][PROVEN_DEFECT] Tien trinh mo coi an 99,7% CPU lien tuc 46,4 gio tren may chi co 2 vCPU
  [P1][OPERATIONAL_IMPROVEMENT] Dia 81% — 1.043 ngay neu chi tang tu dong, nhung 6,9 ngay neu giu nhip clone DB cua ba phien audit vua roi
  [P1][OPERATIONAL_IMPROVEMENT] Cong suc khoe chay moi gio co 16 phep va KHONG PHEP NAO ve dia — no khong nhin thay chinh thu dang o 81%
  [P2][PROVEN_DEFECT] scheduler_logs: 281.883 dong, 0 index, 10 diem doc trong ma dang serve — moi truy van la quet toan bang
  [P2][OPERATIONAL_IMPROVEMENT] MariaDB ghi 222 MB canh bao vo nghia va backend KHONG HE DUNG MySQL
  [P2][PROVEN_DEFECT] Khi dia day: KHONG CO du tru cua he tep, va journal la nan nhan dau tien — mat dung nang luc dieu tra ma FU-402 dung ra de co
  [P2][OPERATIONAL_IMPROVEMENT] 70.385 lan dang nhap SSH sai trong 6,9 ngay; cong 3306 va 21 mo ra 0.0.0.0
  [P3][OPERATIONAL_IMPROVEMENT] predictions: mot dang truy van bi quet toan bang 104 ms (2 diem doc), cac dang khac deu duoc index phuc vu tot
  [P3][OPERATIONAL_IMPROVEMENT] Khong co logrotate cho bat ky log ung dung nao — mot tep da 124 MB
  [P3][OPERATIONAL_IMPROVEMENT] Cron trung nhau va day dac — nhung phan lon la BACKSTOP CO CHU Y, khong phai loi sao chep
  [P3][NO_ANOMALY_FOUND] KHONG CO job cron nao chet — 93/93 job dang bat deu ghi log trong 2 ngay
  [P3][NO_ANOMALY_FOUND] Ba job scheduler 'im lau' KHONG PHAI job chet — ap dung RM-20, quet dang ky trong ma chu khong ket luan tu im lang
  [P3][NO_ANOMALY_FOUND] Khong ro API key o bat ky log nao; .env dat quyen dung va da gitignore
  [P3][NO_ANOMALY_FOUND] DB toan ven: quick_check ok, page_count khop chinh xac kich thuoc tep, freelist = 0
  [P3][NO_ANOMALY_FOUND] Khong co bang chung ro ri bo nho cua service TRONG cua so quan sat — nhung khong co chuoi RSS lich su de noi ve chan troi dai hon
  [P3][NO_ANOMALY_FOUND] Ngay 'tuong lai' va nam 2222/3262 trong scraper.log KHONG phai bat thuong — phan loai theo RM-09 thay vi dem chuoi tho
  [P3][INDETERMINATE] Ba nhan job trong scheduler_logs im 117-119 ngay — CHUA kiem duoc con dang ky hay khong