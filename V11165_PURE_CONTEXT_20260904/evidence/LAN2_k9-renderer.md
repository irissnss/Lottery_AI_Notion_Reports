# k9-renderer · tang=CODED_AND_TESTED_NOT_RUNTIME_PROVEN

## TOM TAT

GATE 9 hoan thanh ca ba viec, xuat du bon artifact yeu cau. Bo thu chin nhom A..I: 68 phep CHAY, 68 DAT, 0 TRUOT, 2 KHONG_CHAY_DUOC (co ly do tuong minh, khong tinh la dat).

VIEC 1 — RENDERER: artifacts/v11165_k9_renderer.py tach lam hai nua `thu_thap()` (cham DB, doc-only, moi truy van co chan as-of) va `render()` (HAM THUAN: khong DB, khong dong ho, khong bien moi truong). Sinh ba tang FACTS -> CONDITIONS -> CONTRACT. Payload MN 18.682 ky tu (official cung ngay: 50.464). Khong preselected basket, khong rank, khong boost, khong model-meta; bang full-universe 00->99 thu tu co dinh chi co/khong; moi CONDITION co nen dung `1-(1-b)^k` voi b DO LAI cho chinh mien x thu dang xet.

VIEC 2 — CONTAMINATION_GATE_V2: artifacts/v11165_k9_contam_v2.py, do tren DUMP THAT, phan loai tung lan khop (KHANG_DINH / PHU_DINH / DINH_NGHIA_HOP_DONG / SU_KIEN_GOC) thay vi dem chuoi. Hieu chuan hai chieu: ung vien 3/3 mien DAT voi o nhiem = 0; 57/57 payload official+shadow THAT deu TRUOT, trung binh 220 diem o nhiem moi payload, dinh du 9 nhom detector.

VIEC 3 — TEST SUITE: artifacts/v11165_k9_tests.py chay du A..I, trong do nhom E lam cong DO 6/6 lan giai lap vi pham.

Bo thu bat duoc MOT LOI THAT trong chinh ban ung vien: sai quy uoc thu khi tra mined_rules, lam TOAN BO tang dieu kien ra rong ma khong bao loi. Da sua, da chay lai. Production KHONG dinh loi nay (co bang chung ma nguon).

## BLOCKER

Chua dat READY_FOR_OWNER_SHADOW_DEPLOY vi BON viec, khong viec nao lam duoc trong phien nay:
(1) CHUA DANG KY PHEP DO TIEN. Muc tieu owner so 9 doi chung minh bang DO TIEN. Phien nay khong co bat ky thiet ke do nao duoc dang ky TRUOC (nguong, n-can tinh cho DUNG thuoc bach thu, moc chot) — theo RM-03 thieu cai nay thi cam ghi 'thang' ve sau.
(2) TANG 2 CHUA TACH TRONG/NGOAI CUA SO CHON. Nguon dieu kien la mined_rules, va mined_rule_effectiveness nam trong chinh cua so khai thac cua cac luat do. PRJ-SELECTION-WINDOW-001 muc 3 bat buoc tach va bao ca hai truoc khi ket luan. Chua lam => 23 truong hop KHAC_NEN_DUONG chua duoc dung lam can cu gi.
(3) OWNER LOCK dang chan: MODEL_ACTION=BLOCKED · POOL_VERDICT=HOLD · MT_PREREGISTRATION=NOT_READY_FOR_OWNER_LOCK. Bat mot lane shadow moi la hanh dong can owner chot, khong phai viec agent tu quyet.
(4) CHUA CO NHANH CONTROL DO DUOC. Bang lane ba tang khong luu van ban control nen khong the chay cong o nhiem tren doi chung; thieu no thi phep do A/B khong co ve doi chieu sach.
Ngoai ra ba tep deu la TEP MOI trong artifacts/, chua deploy, chua chay tren duong serve, chua goi provider — nen ke ca bon viec tren xong thi tang cao nhat dat duoc van phai qua mot buoc owner duyet.

## TRA LOI

SO PHEP CHAY / DAT / TRUOT TUNG NHOM (nhat ky day du: scratchpad/d30/_k9_run3.txt):

NHOM A · Matrix coverage — chay 7, dat 7, truot 0, khong chay duoc 1
 · 3 mien x 7 thu = 21 o render duoc het (phu du thu 0..6) DAT
 · truoc-va-sau khi mien ra truoc co ket qua => payload DOI (2/2 mien) DAT
 · renderer KHONG co tham so model => bat bien theo provider DAT
 · bucket RULE RONG: khong bucket that nao rong nen DUNG LAP tren DB tam (xoa 5 luat) -> 0 dieu kien, payload van sinh 15.065 ky tu DAT
 · bucket NHIEU RULE nhat (MT, thu 6, 5 luat) DAT
 · cutoff BIEN: created_at == cutoff thi DUOC lay (n=1 vs n=0 khi lui mot don vi phan giay) DAT
 · co payload OFFICIAL that de doi chieu (57) DAT
 · payload CONTROL: KHONG CHAY DUOC — bang lane ba tang chi luu so ky tu, khong luu van ban

NHOM B · Causal/as-of — chay 5, dat 5, truot 0
 · moi moc thoi gian nguon < cutoff, 6 to hop, 0 vi pham DAT
 · same-day mien ra truoc chi lay khi DA CO (cutoff som=0 ban ghi, cutoff muon=5) DAT
 · XOA ket qua ngay dich cua mien dich => CUNG payload byte DAT
 · xoa ca ba mien thi MT/MB DOI — ghi ro day la hanh vi DUNG (mat [F3] la mat dau vao hop le), khong phai loi DAT
 · DOI ket qua ngay dich cua mien dich => CUNG payload byte DAT

NHOM C · Full payload hashing — chay 5, dat 5, truot 0
 · 100% payload cuoi duoc bam DAT · 19 section noi lai == payload goc, 18.682 = 18.682 ky tu DAT
 · section hash cong lai tai lap duoc payload cuoi (root 29f9375db4af98b9) DAT
 · khong con duong noi them sau bam (0 ket qua cho prompt+= / payload+= / +_ctx_pack / sections.append) DAT

NHOM D · Forbidden content — chay 2, dat 2, truot 0
 · 21 o matrix deu sach, o nhiem=0 DAT
 · 57 payload official/shadow that => cong TRUOT het (TRUOT 57 · DAT 0) DAT

NHOM E · Negative tests — chay 9, dat 9, truot 0 (moi phep lam cong DO)
 · tien de: ban sach DAT (allow) · E1 bang xep hang model -> MODEL_RANKING+WR_WEIGHT+BOOST · E2 top-10 candidate -> BASKET+PRESELECTED_TOPK · E3 noi ctx_pack SAU diem bam -> HIDDEN_ADDITION+TOTAL_FINAL+WR_WEIGHT · E4 renderer bat bien voi selected_model (byte giong) va E4b payload co route -> MODEL_RANKING · E5 dung ket qua ngay dich -> PRESELECTED_TOPK · E6 menh lenh tro vao khoi da xoa -> ORPHAN_INSTRUCTION · khoi phuc nguyen trang (moi phep chi doi chuoi trong bo nho, khong ghi tep/DB)

NHOM F · Duplicate/herding — chay 9, dat 9, truot 0
 · section overlap dong DU LIEU = 0 DAT (dong khuon mau lap 38 cap duoc bao rieng, co y, khong tinh herding)
 · van tay bo ung vien khong lap (5 bo, 0 lap) · cung mot bo duoi hai ten = 0 · lineage trung = 0
 · do phu khong gian so 10/100 va DUOC CONG BO trong payload · order anchoring bang 00->99 du 100 muc dung thu tu
 · dieu kien in theo ID tang dan, KHONG theo suc manh (ids 2751..2755 tang, ty le 0.97/1.0/1.0/1.0/0.895 khong giam dan)

NHOM G · Output contract — chay 11, dat 11, truot 0, khong chay duoc 1
 · 10 ca validator dung het: hop le day du · JSON hong · thieu main_number · nhieu main_number · co truong 3 cang · condition_ref bia ra · secondary khong doc lap · arithmetic khong tinh lai duoc · khong co secondary (hop le) · muc_chac_chan sai
 · hop dong cam 3 cang bat buoc DAT
 · goi provider that: KHONG CHAY DUOC — luat cung cam. Nhom G kiem VALIDATOR, khong kiem hanh vi model.

NHOM H · Mutation — chay 13, dat 13, truot 0 (chi tiet o muc mutation_ledger)

NHOM I · Determinism — chay 7, dat 7, truot 0
 · cung facts => cung BYTES (5 lan) · xao tron thu tu khoa FACTS => cung BYTES · FACTS qua JSON canonical => cung BYTES
 · MA TRAN PYTHONHASHSEED x TZ x LOCALE: 20 to hop (seed 0/1/42/12345/random x TZ UTC / Asia/Ho_Chi_Minh / America/New_York, locale C / en_US.UTF-8 / vi_VN.UTF-8) => DUNG MOT bam a9184f6c... DAT
 · khong co ky tu CR trong payload · ghi/doc newline='' vong lai nguyen ven · ghi newline='\r\n' LAM DOI byte (19.261 vs 18.911) — bang chung phai bat buoc newline=''

TONG: chay 68 · dat 68 · truot 0 · khong chay duoc 2.

## PHAT HIEN
  - [PROVEN_DEFECT] Kho co HAI quy uoc thu nguoc nhau; ban ung vien dau tien lay nham bucket luat va hong AM hoan toan
  - [EXPECTED_BEHAVIOR] PRODUCTION KHONG dinh loi quy uoc thu — noi ro de khong ai doc nham thanh bao dong production
  - [PROVEN_DEFECT] Ban dau cua chinh CONTAMINATION_GATE_V2 co ba lop duong tinh gia — cung ho loi voi bo 5 dau mu V11160, chi nguoc chieu
  - [OPERATIONAL_IMPROVEMENT] Hieu chuan hai chieu cua cong: ung vien 3/3 DAT, 57/57 payload that TRUOT voi ~220 diem o nhiem moi ban
  - [INDETERMINATE] Ap nen DUNG cho bo k duoi lam phan lon dieu kien tro thanh KHONG_KHAC_NEN — ke ca cac ban ghi 100%
  - [OPERATIONAL_IMPROVEMENT] Do phu khong gian so cua tang dieu kien: 9-13/100 duoi, va duoc CONG BO ngay trong payload
  - [OPERATIONAL_IMPROVEMENT] Do phu van tay 100% theo CAU TRUC, khong phai theo lo trinh va
  - [NO_ANOMALY_FOUND] Hai phep KHONG CHAY DUOC — ghi thang, khong tinh la dat

## CHUA TRA LOI

1. PHEP DO TIEN — chua co. Muc tieu owner so 9 doi chung minh output tot hon bang DO TIEN. Phien nay khong do gi ve do trung, va cung khong duoc phep (cam goi provider). Cam doc bat ky con so nao trong bao cao nay thanh 'prompt moi tot hon'.

2. TACH TRONG/NGOAI CUA SO CHON cho TANG 2 — chua lam. mined_rule_effectiveness nam trong cua so khai thac cua chinh cac luat, nen 23/210 truong hop KHAC_NEN_DUONG chua co gia tri ket luan. Day la dieu PRJ-SELECTION-WINDOW-001 muc 3 bat buoc, va la viec ke tiep phai lam neu muon dung tang dieu kien nay lam can cu.

3. HANH VI MODEL THAT truoc payload nay — hoan toan chua biet. Khong goi provider nen khong biet model co tuan thu hop dong TANG 3 khong, co bia condition_ref khong, co tu tim danh sach so khong khi khong duoc dua san. Nhom G chi chung minh VALIDATOR bat duoc cac loi do NEU chung xay ra.

4. NHANH CONTROL — khong doi chieu duoc vi bang lane ba tang khong luu van ban control.

5. PHAM VI CHUA PHU cua renderer: hien chi lay CONDITION tu mined_rules. Cac nguon khac trong 35 producer co disposition TRANSLATE_TO_NEUTRAL_CONDITION (P23 evidence windows · P24 evidence source-prize · P25 boi canh soi cau · P26 convergence trap · P28 antitrap spend · P30 weekday scan · P34 MB rule stack) CHUA duoc chuyen thanh dieu kien trung tinh. Payload hien tai vi vay MONG hon official rat nhieu (18.682 vs 50.464 ky tu) — do mot phan la co y (bo AGGREGATED_NUMBER_SET), nhung mot phan la CHUA LAM, khong duoc nham hai thu voi nhau.

6. P29_D1_POOL_COUNT co disposition EXPOSE_VIA_REAL_QUERY_TOOL — nhung L6 da do duoc la KHONG co tool calling o bat ky model nao. Nen dung nghia disposition do hien KHONG THI HANH DUOC; phien nay bo han producer do khoi payload thay vi gia vo co tool.

7. CHUA do so token (VPS khong co tokenizer) — moi con so o day la KY TU va BYTE, khong phai token.