# h13-lineage · tang=EVIDENCE_COMPLETE

## TOM TAT

Cong 13 do xong tren 567 bundle / 189 ngay (28/02–04/09/2026), toan bo tren clone bat bien read-only; DB production + code + PID 3370750 khong doi mot byte. Phat hien chinh da duoc chung minh: `consensus_level` dem voter THO, khong khu trung huyet thong — 268/567 bundle (47,3%) dang mang nhan cao hon su that, trong do 200 bundle tut thang tu `strong` xuong `weak`; so nguon doc lap trung binh chi 3,07 chu khong phai 5,32 voter. Nhan sai nay KHONG nam trong noi bo: no di thang ra trang cong khai `du-doan.html:1413` roi thanh nhan "Rat manh / Dong thuan cao" cho nguoi dung, va `consensus_level` nam trong danh sach cho phep khach xem (`main.py:6409`). MT nang nhat (68,8% doi nhan, chi 2,35 nguon doc lap), MN nhe nhat (27,5%). Phat hien thu hai: `scheduler.py:3078-3079` ghi hai truong ten `meta_numbers`/`lstm_numbers` nhung thuc te chua output cua BAT KY hai model ML nao duoc chon dong — sai nhan 382/623 dong (61,3%); chinh toi da sap bay nay o luot do dau (ra 53,7%), sua anh xa theo vi tri thi ra 99,4%. Nguoc lai, combo-super goi lai model KHONG phai defect: do that cho thay lan goi lai cho ket qua KHAC 86,8% voi AI va 42,0% voi ML, tuc no la luot lay mau moi that chu khong phai chep lai phieu cu. Comparator trong so lineage-aware doi top-1 toi 59,0% bundle nen TUYET DOI khong duoc dua vao production; tin hieu ket qua cua no chi la tham do — gop lai p=0,0399 nhung tach ra thi dev p=0,4731 va MN dung bang 0 (13 doi 13), tuc chua du dieu kien ket luan.

## TRA LOI

VIEC 1 — lop do moi da dung xong, tinh cho tung bundle va luu trong v11165_h13_sensitivity.json / v11165_h13_final.json (khoa `tung_bundle`): raw_voter_count, independent_source_count (ca STRICT indS lan LOOSE indL), independence_groups (liet ke tung nhom), parent_source_ids, resampled_model_ids, roots_hop, consensus_level_raw, consensus_level_independent. Khong dung parent_output_hashes ma dung thang OUTPUT THAT (main_numbers cua cha so voi ban sao trong analysis_text cua con) — bam se chi cho biet giong/khac, con so that cho biet giong bao nhieu va khac cho nao, manh hon.

VIEC 2 — phan loai voter, quet ra bang AST tu model_registry.MODEL_REGISTRY va combo_super.ML_MODELS/AI_MODELS (khong import module production, khong doan ten, thoa RM-10): DIRECT_BASE_ML = 4 model ML (NO_TOKEN|ML_PREDICTOR); DIRECT_BASE_AI = 39 model TOKEN|GENERATOR; ENSEMBLE_REUSE_PARENT = smart-ensemble / smart-ml / combo-no-token (NO_TOKEN|ENSEMBLE); COMBO_RESAMPLE_SAME_MODEL = combo-super (TOKEN|ENSEMBLE). Cha me lay THEO TUNG NGAY-MIEN tu DB chu khong ap tinh: smart-ensemble.models_used 623/623 dong, smart-ml 621, combo-no-token 627, combo-super.dual_pool_v596 572 + bu 60 tu ml_models_actual/ai_models, chi 6 dong thieu han. Dieu nay quan trong: smart-ensemble KHONG phai 'LSTM + Meta' nhu registry va display_name 'Smart Meta+LSTM' mo ta — no la TOP-2 DONG theo BT rate, va bo {lstm,meta} that su chi chiem 228/623 dong. Day la mot lech DOC_SAID vs CODE_DID.

VIEC 3(a) output hien tai: 567 bundle, 189 ngay, 28/02–04/09/2026, ti le WIN bach thu 191/567 = 33,7% (MN 42,3% · MT 37,6% · MB 21,2%).
VIEC 3(b) nhan consensus lineage-aware, KHONG doi diem: 268/567 bundle doi nhan (47,3%) theo STRICT, 247 (43,6%) theo LOOSE. Chi tiet o bang chinh.
VIEC 3(c) comparator trong so lineage-aware, do RIENG va KHONG dua vao production: do duoc tren 322/567 bundle, 190 bundle (59,0%) doi top-1.

CAU HOI 1 — bao nhieu bundle doi nhan consensus? 268/567 = 47,3% (STRICT), 247/567 = 43,6% (LOOSE). Nang nhat la 200 bundle tut hai bac strong->weak. Theo mien: MT 130/189 (68,8%), MB 86/189 (45,5%), MN 52/189 (27,5%).
CAU HOI 2 — bao nhieu doi top-1 neu ap weighting? 190/322 bundle do duoc = 59,0%. Theo mien: MT 90/128 (70,3%), MB 56/101 (55,4%), MN 44/93 (47,3%).

TACH TRONG/NGOAI CUA SO CHON (PRJ-SELECTION-WINDOW-001) — bao ca hai, khong gop: moc tach 2026-06-02 (trung vi ngay). Doi nhan: dev 155/285 (54,4%) vs holdout 113/282 (40,1%) — hieu ung co o CA HAI ben, khong phai san pham cua cach chon cua so. Doi top-1: dev 78/124 (62,9%) vs holdout 112/198 (56,6%). Tin hieu ket qua thi NGUOC LAI — dev p=0,4731 (khong co gi) va holdout p=0,0581 (van khong qua nguong), tuc con so gop p=0,0399 khong song sot khi tach.

LOC RO RI (bo 1 va 2 cua PRJ-SELECTION-WINDOW-001): 27/567 bundle co it nhat mot ban ghi voter tao SAU moc dung bundle; bo ca 27 di thi ket qua gan nhu khong doi (253/540 = 46,9% so voi 47,3%), nen ket luan khong dua tren du lieu ro nguoc.

NEN RIENG TUNG MIEN (RM-18) va HANG SO DO LAI (RM-21): moi mien co bang rieng trong bang chinh; VIF do lai cho dung thuoc nay (bundle doi top-1, cum theo ngay) ra DEFF=1,025, KHONG muon 2,92 cua RM-18 cung khong muon 0,889 cua V11057.

KHONG doi selector, khong dua comparator vao production, khong goi combo-super la defect — dung nhu de bai rang buoc.

## PHAT HIEN
  - [PROVEN_DEFECT] consensus_level dem voter THO — 268/567 bundle mang nhan cao hon su that, va nhan do ra toi nguoi dung
  - [PROVEN_DEFECT] smart-ensemble ghi hai truong SAI TEN: 'meta_numbers'/'lstm_numbers' thuc ra chua output cua hai model khac — 382/623 dong (61,3%)
  - [EXPECTED_BEHAVIOR] combo-super goi lai model KHONG phai defect — do that chung minh no la luot lay mau MOI, khong phai chep lai phieu cu
  - [EXPLORATORY_PREDICTIVE_SIGNAL] Comparator trong so lineage-aware doi top-1 toi 59% bundle — tin hieu ket qua CHUA DU dieu kien ket luan, cam dua vao production
  - [INDETERMINATE] Menh de Gate 0 'output_counterfactual_rank = 0/17121' can noi lai cho dung: BANG DO KHONG TON TAI
  - [OPERATIONAL_IMPROVEMENT] Hai tep lottery_ai.db RONG 0 BYTE nam dung cho duong dan tuong doi se tro toi

## DAU VAO LAN SAU

1. HAI CON SO PHAI MANG SANG, dung tron lan: voter THO trung binh 5,32 vs nguon DOC LAP 3,07
   (STRICT) / 3,60 (LOOSE). Moi phat bieu ve "bao nhieu model dong thuan" tu day tro di phai noi
   ro dang dung thuoc nao.

2. CAM MUON HANG SO — VIF do duoc o cong nay la DEFF = 1,025 (ICC 0,1181, cum theo ngay, co cum
   tb 1,211) va no CHI dung cho thuoc "bundle doi top-1 duoi comparator lineage-aware". Khong
   duoc mang sang thuoc khac. Ly do co cum chi 1,211 la vi chi ~1,2 bundle moi ngay bi doi
   top-1 — thuoc nao co ca 3 mien moi ngay se co co cum 3 va DEFF khac han.

3. QUY UOC BAT BUOC KHI DOC analysis_text CUA smart-ensemble: hai truong `meta_numbers` va
   `lstm_numbers` KHONG dang tin theo ten. Phai anh xa theo VI TRI:
   models_used[0] -> meta_numbers, models_used[1] -> lstm_numbers. Tin ten se ra 53,7% thay vi
   99,4% — lech du lon de dao nguoc ket luan "smart-ensemble co doc lap khong". Toi da sap bay
   nay o luot do dau; ghi lai de lan song 2 khong sap lai.

4. NGUON CHA ME TUNG NGAY DA CO SAN TRONG DB, khong phai suy tu ten (RM-10):
   predictions.analysis_text.models_used (smart-ensemble 623 · smart-ml 621 · combo-no-token 627)
   va predictions.analysis_text.dual_pool_v596.selected_ml/selected_ai (combo-super 572,
   bu 60 bang ml_models_actual+ai_models, con 6 dong thieu han). Dung
   artifacts/v11165_h13_parent_map.json de khoi tinh lai.

5. LECH DOC_SAID vs CODE_DID CHUA XU (§62 bat buoc bao, chua sua trong phien nay):
   model_registry.py:815-833 ghi smart-ensemble display_name 'Smart Meta+LSTM' va wr_note
   'LSTM + Meta-Learning ensemble', nhung code chon TOP-2 DONG theo BT rate — bo {lstm,meta}
   that su chi chiem 228/623 dong. Tai lieu dang mo ta mot hanh vi khong con dung.

6. CHO CAN QUYET DINH CUA OWNER (toi KHONG tu quyet): sua nhan consensus_level la viec DOI SO
   NGUOI DUNG NHIN THAY — 507 bundle 'Dong thuan cao / Rat manh' se thanh 261-280. Day la thay
   doi UI/san pham, khong phai va ky thuat, nen phai co owner lock truoc. Ba lua chon toi thay:
   (a) giu nguyen diem, chi doi NHAN + hien ca hai con so (raw/doc lap);
   (b) them truong moi ben canh, khong dong truong cu;
   (c) khong doi gi, chi ghi vao tai lieu.
   Toi nghieng ve (a) hoac (b) vi diem so KHONG doi ⇒ khong dung toi bo chon production.

7. CAM DUA COMPARATOR (c) VAO PRODUCTION. No doi top-1 toi 59% bundle. Tin hieu ket qua khong
   song sot khi tach dev/holdout va MN dung bang 0 (13 doi 13). Neu lan song 2 muon theo duoi,
   phai DANG KY NGUONG TRUOC (RM-03) va do tien, khong duoc dung lai so cua phien nay lam can cu.

8. SUA CACH VIET CUA GATE 0: 'output_c

## CHUA TRA LOI

1. KHONG chung minh duoc nhan consensus HIEN LEN THAT tren trinh duyet nguoi dung. Toi chi
   chung minh duoc chuoi doc trong TEP DANG PHUC VU (du-doan.html:1413 -> :1467-1468 -> :1552 ->
   :1666-1673, tep bam 76599f6ad1cfed8a trung byte giua local va VPS, duoc phuc vu tai
   main.py:15972 boi PID 3370750). Viewer-freeze 2026-06-07 van chan tang 5 dung nhu V11164 da
   ghi. Vay day la CODE_DID muc tep, KHONG phai RUNTIME_PROVEN muc render. Cam nang tang.

2. KHONG tra loi duoc "quy uoc nao MOI DUNG" giua STRICT va LOOSE. Do that cho thay combo-super
   la nguon BAN doc lap (AI khac 86,8%, ML khac 42,0%), tuc su that nam GIUA hai quy uoc. Toi
   bao cao ca hai (268 vs 247 bundle doi nhan) thay vi chon bua mot cai. Muon dinh luong dung
   phan doc lap con lai can mot phep do tuong quan co dieu kien tren luot API, chua lam.

3. KHONG dinh luong duoc 4 model ML co THAT SU doc lap voi nhau khong. Toi coi chung la 4 nguyen
   tu vi de bai ghi "independent ML", nhung ca bon dung chung mot duong _run_free_model_prediction
   va cung mot bo dac trung dau vao. Neu chung tuong quan manh thi con so 3,07 nguon doc lap VAN
   CON CAO HON su that. Tuc ket luan cua toi la phia BAO THU — sai lech neu co thi theo huong
   nhe di, khong phai nang len.

4. KHONG ket luan duoc comparator (c) co cai thien ket qua hay khong. Gop lai p=0,0399 nhung
   dev p=0,4731, holdout p=0,0581, MN dung bang 0 (13 doi 13). Khong dang ky nguong truoc (RM-03)
   va luat chia diem do chinh toi thiet ke sau khi nhin du lieu. Ghi dung: EXPLORATORY_PREDICTIVE_SIGNAL,
   KHONG phai PREDICTIVE_IMPROVEMENT_PROVEN.

5. KHONG do duoc comparator (c) tren 245/567 bundle (43,2%) vi thieu score_breakdown hoac bi cat
   components[:8]. Con so 59,0% doi top-1 chi dung cho 322 bundle do duoc, KHONG duoc suy ra ca kho.

6. KHONG truy duoc cha me cua 6/638 dong combo-super (thieu ca dual_pool_v596 lan ml_models_actual),
   va 6/190 bundle doi top-1 khong tra duoc ket qua thang/thua tu model_daily_eval.

7. KHONG kiem tra