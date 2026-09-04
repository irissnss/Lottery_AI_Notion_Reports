# g7-stdio · tang=EVIDENCE_COMPLETE · 7 phat hien

## TOM TAT

GATE 7 phan loai DUNG MOT nhan: LATENT_CODE_BUG_NOT_RUNTIME_INCIDENT — _safe_stdio_ctx co ba khiem khuyet tai lap duoc 4/4 lan, nhung KHONG co su co runtime nao ngay 04/09. Khiem khuyet nang nhat: probe `stream.write("")+flush()` khong day byte nao xuong fd nen KHONG phat hien duoc hong o tang fd (EPIPE / EBADF / AF_UNIX peer chet) — dung hinh dang fd1=fd2=socket:[76184038] cua service; trong ba ca do wrap khong chan duoc va print van nem dung lop loi ma no sinh ra de chan. Khiem khuyet thu hai: sys.stdout la toan cuc, ctx lai chay trong luong worker cua _start_timed_model_call, nen khi luot A thoat va tra stream hong ve thi luot B MAT BAO VE ngay trong vung ctx cua chinh no — tai lap bang chinh _start_timed_model_call (A='A_OK', B nem ValueError), va soft-continue 90s co that trong log 16:55:13. _restore_stdio CHI luu stream HONG (saved[idx] nam trong nhanh `if unusable:`) va tra lai dung doi tuong hong do — dung ve hanh vi nhung docstring dong 254 ghi nguoc lai. Nhanh hong TUNG dat duoc trong runtime that: 270 dong scheduler_logs mang "ValueError: I/O operation on closed file." tu 10/05 den 19/07/2026, cham dut sau khi V10800/V10826 tach cac job sang subprocess; ngay 04/09 la 0/0/0 tren ca ba nguon (journal 39.101 dong, scheduler_logs tu 01/08, prediction_trace). Ngoai pham vi cong nay toi do duoc mot khiem khuyet THAT dang song: stdout cua service bi dem khoi du PYTHONUNBUFFERED=1, log console toi journal tre trung vi +19.200s va toi da +84.900s, trong khi kenh DB day du va dung gio.

## TRA LOI CAU HOI

PHAN LOAI GATE 7 (dung MOT nhan): **LATENT_CODE_BUG_NOT_RUNTIME_INCIDENT**. Ba khiem khuyet ma nguon tai lap on dinh, nhung KHONG co su co runtime nao trong ngay 04/09.

**1. stdout/stderr nao bi hong — dieu kien nao lam `unusable` thanh True (scheduler.py:238-246)?**
PHAT HIEN duoc: (a) `stream is None` — T1; (b) `getattr(stream,"closed",False)==True` — T2 (file da .close()), T3 (StringIO da .close()); (c) `stream.write("")` hoac `stream.flush()` nem — T7 (write nem), T8 (flush nem).
BO SOT: moi hong o TANG fd trong khi doi tuong Python van "sach" — T4 pipe mat dau doc (EPIPE), T5 fd bi dong ngay duoi doi tuong (EBADF), T6 AF_UNIX SOCK_STREAM peer chet. Ly do co hoc: `write("")` khong day byte nao xuong fd va `flush()` voi bo dem rong khong sinh syscall, nen probe khong bao gio cham toi fd. T6 la DUNG hinh dang stdout production (fd1=fd2=socket:[76184038]).

**2. _restore_stdio dang LUU gi — stream lanh hay stream hong?**
CHI luu stream HONG. `saved[idx] = stream` nam TRONG nhanh `if unusable:` (dong 247-249), nen mot stream lanh khong bao gio duoc luu: T9 tra `saved_deu_None=[true,true]`. Ngoai ra probe khong lam ban stream lanh (`probe_ghi_them_gi=''`).

**3. restore tra ve stream lanh hay chinh stream HONG?**
Chinh stream HONG — T2/T3/T7/T8 deu cho `restore_tra_lai_dung_stream_HONG=true` va `print_sau_restore_no_loi` bang dung loi cu. Day la DUNG ve hanh vi: ctx khong duoc de lai bien doi toan cuc vinh vien. Nhung docstring dong 254 ("if originals were valid") noi NGUOC voi ma. Va co mot ro ri that: khi goc la `None`, `saved_out is None` khien restore bo qua, `_SafeNullWriter` o lai VINH VIEN (T1 + T17).

**4. Nhanh do co DAT DUOC trong service runtime khong? Co bang chung nao trong journal 04/09 khong?**
LICH SU: CO — 270 dong `scheduler_logs` mang "ValueError: I/O operation on closed file." tu 2026-05-10 12:01:21 den 2026-07-19 17:30:00 (UTC), traceback chi thang `scheduler.py:1851 print(...)`. Da cham dut sau khi V10800 (15/07) va V10826 tach Weekly Mining / weight optimizer / retrain sang **subprocess** co stdout rieng — tuc duoc vá bang cach ly tien trinh, KHONG phai bang `_safe_stdio_ctx`.
NGAY 04/09: KHONG co bang chung nao. journal 04/09 (10.854 dong) 0 hit; journalctl toan bo con luu (39.101 dong tu 2026-08-29) 0 hit cho ca ba chuoi 'closed file' / 'Broken pipe' / 'Bad file descriptor'; `scheduler_logs` tu 2026-08-01 den nay 0 dong; `prediction_trace` 04/09 (60 dong) 0 hit. Bo tro: journald NRestarts=0 khoi dong tu 2026-08-13 23:40:41 (peer socket chua tung chet), lottery NRestarts=0 PID 3370750 tu 01:08:40, fd0=/dev/null fd1=fd2=socket:[76184038], 791 dong `[SCHEDULER]` van phat qua stdout trong ngay.

**5. Hanh vi TRUOC/SAU fault** — xem bang o `bang_du_lieu`.

**6. Test co tai lap on dinh khong (>= 3 lan)?**
CO — chay 4 lan (1 + 3 lan lap qua `_g7_h_repeat.py`), moi truong load-bearing GIONG HET, `on_dinh=true`, `lech=[]`, sha rut gon `e9ad453dea1116d1`. Thu nghiem chuoi hai wrapper cung 4/4 giong het.

**TUAN THU LUAT CUNG:** khong dung cham tien trinh service (harness trich ma nguon roi exec trong tien trinh RIENG, khong import scheduler cua production); khong patch production; moi ket noi DB deu `mode=ro`.


## PHAT HIEN (tieu de)
  - [PROVEN_DEFECT] G7-F1 — Probe write('')+flush() khong phat hien duoc hong o TANG fd; dung hinh dang stdout cua production
  - [PROVEN_DEFECT] G7-F2 — sys.stdout toan cuc + ctx chay trong luong worker => dua luong lam MAT BAO VE giua chung
  - [PROVEN_DEFECT] G7-F3 — _restore_stdio CHI luu stream HONG, va ro ri sink vinh vien khi stream goc la None
  - [OPERATIONAL_IMPROVEMENT] G7-F4 — Docstring noi nguoc voi ma (hai cho)
  - [EXPECTED_BEHAVIOR] G7-F5 — Nhanh hong TUNG dat duoc trong runtime (270 dong, 05-07/2026) nhung ngay 04/09 la 0
  - [PROVEN_DEFECT] G7-F6 — stdout cua service bi DEM KHOI du PYTHONUNBUFFERED=1: log console toi journal tre toi 23 gio
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] G7-F7 — Co che ung vien cho ca hai: 9 module scheduler nap co lenh gan lai sys.stdout o MUC MODULE

## CHUA TRA LOI DUOC

**1. Khong chung minh duoc trong tien trinh 3370750 co HAI trong 9 module cung duoc nap.** Do la mat xich cuoi cua gia thuyet G7-F7. Chung minh se can noi soi `sys.modules` cua tien trinh song (gdb/py-spy attach hoac endpoint chan doan) — luat cong cam dung cham service. Cach do KHONG xam pham, de xuat cho phien sau: them mot endpoint admin chi doc tra ve `type(sys.stdout).__name__`, `sys.stdout.write_through`, `sys.stdout is sys.__stdout__` va danh sach 9 module trong `sys.modules` — mot lan goi la dong duoc.

**2. Chua phan biet duoc dut khoat "bo dem chua day" vs "bo dem da dong" cho phan duoi cua ngay 04/09.** Do tre da chung minh noi dung KHONG mat trong cac burst do duoc; nhung phan sau 16:53:48 den gio kiem (21:50) van chua xuat hien — co the la bo dem chua day, cung co the da dong im lang. Phep phan biet o muc 1 giai quyet luon ca cau nay.

**3. T16 (hong GIUA CHUNG sau `__enter__`) KHONG KET LUAN DUOC.** Lan chay cho `print_sau_khi_hong='KHONG NO'` trong khi T6 cung kieu hong lai nem `BrokenPipeError` — khac biet phu thuoc thoi diem RST toi noi, khong on dinh. Ghi INDETERMINATE, khong dung lam can cu. (Ve mat ma nguon thi hien nhien ctx khong the bao ve truong hop nay vi no chi kiem tra mot lan tai `__enter__`, nhung day la suy luan, khong phai do dac.)

**4. Cua so bang chung journal chi tu 2026-08-29** (39.101 dong, journald khoi dong 2026-08-13 nhung log chi con giu tu 29/08). Ket luan "0 su co" cho 04/09 la vung; ket luan "0 su co trong ca thang 8" chi dua vao `scheduler_logs` (co tu 2026-03-27) chu khong dua vao journal.

**5. Chua do duoc TAN SUAT thuc te cua ca dua luong G7-F2.** Da chung minh no XAY RA DUOC va scheduler CO chay chong luot (soft-continue 90s), nhung chua dem duoc bao nhieu lan hai `_safe_stdio_ctx` thuc su chong nhau trong mot ngay. Do se can dem-vet trong ma, tuc phai sua code — cam trong phien nay.

**6. Chua truy duoc vi sao 270 dong dung han o 2026-07-19.** Da chi ra rang V10800 (15/07) va V10826 tach ba job lon sang subprocess,