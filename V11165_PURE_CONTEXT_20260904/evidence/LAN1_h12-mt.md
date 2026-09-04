# h1-evidence · tang=CODED_AND_TESTED_NOT_RUNTIME_PROVEN

## TOM TAT

GATE 12 xong tren clone bat bien, khong ghi gi ngoai artifacts/. Ba con so V11164 duoc do lai: "MT bi EXCLUDE_PRIMARY 72/90 (80,0%)" TAI LAP DUOC, "71 ngay lien tiep" TAI LAP DUOC (26/06..04/09), nhung "it nhat 46/72 quy cho cap" KHONG TAI LAP DUOC — so dung la 45 ngay cap giai thich tron ven (hoac 70 ngay co cap tham gia), can rut lai theo PRJ-RETRACTION-001. Goc loi o main.py:9840: cap co y V10752 duoc do CHUNG tap `filtered_models` voi model truot gate, nen main.py:10511 xuat `wr_gate_filtered` chua chinh hai model ma `gate_diagnostics` ghi pass=true — tu mau thuan tren 70/70 ngay co cap. Hau qua nang nhat vua do duoc: rolling WR/TOP1 cua MT dang TRE 71 NGAY — thuoc goi la "7 luot gan nhat" tinh tren cac luot 19/06..25/06 tai thoi diem 04/09. Sua ke toan xong thi 45 ngay MT doi tu EXCLUDE_PRIMARY sang INCLUDE va so cua MT XAU DI ro rang: wr7 14,3% -> 0,0%, wr14 14,3% -> 0,0%, wrALL 15,1% -> 10,9%, top1_7 57,1% -> 28,6%, top1_14 57,1% -> 21,4%. Phat hien phu quan trong: MB bi loai 73/90 ngay — CAO HON MT — nhung hoan toan do gate fail that, khong lien quan cap, la mot viec RIENG. Candidate patch (3 khoi VA, tep moi trong artifacts/) qua 30/30 test va replay offline 566 dong day_governance: doi dung 45 dong, ca 45 deu la MT, MN/MB doi 0 dong.

## TRA LOI

VIEC 1 — TAI LAP LICH SU (clone bat bien, cua so 90 ngay lich 2026-06-07..2026-09-04, du 90/90 ngay co dong day_governance):

1) Bao nhieu ngay MT bi EXCLUDE_PRIMARY? — 72 ngay (80,0%). Cong them 1 ngay EXCLUDE_ALL (2026-08-28, chi 6/15 model) thi tong bi loai khoi primary eval la 73/90 = 81,1%. Truy van: SELECT COUNT(*) FROM day_governance WHERE region='MT' AND date BETWEEN '2026-06-07' AND '2026-09-04' AND evaluation_policy='EXCLUDE_PRIMARY'.

2) Bao nhieu do CAP co y, bao nhieu do nguyen nhan KHAC?
   - 45 ngay: cap giai thich TRON VEN phan thieu (sua ke toan xong -> INCLUDE).
   - 25 ngay: HON HOP, cap co tham gia nhung con nguyen nhan khac (sua xong VAN EXCLUDE).
   - 3 ngay: khong lien quan cap.
   - Tong ngay co cap tham gia: 70.
   Nguyen nhan KHAC, liet ke tung cai (dem theo ngay, mot ngay co the co nhieu nguyen nhan):
   - GATE FAIL THAT (bt_gate hoac wr_gate, MT min_bt=14 min_wr=28 tai main.py:9753): 20 ngay
   - empty_or_invalid (model tra ve rong/khong hop le): 6 ngay
   - duplicate (dong du doan trung): 3 ngay
   - THIEU DONG DU DOAN (output_eligible_row_count < expected, model khong ra output): 2 ngay
   - policy_exclude: 0 ngay · strength_gate: 0 ngay
   Model bi cap trong 90 ngay: meta-learning 44 ngay · lstm 39 · claude-sonnet-4-6 13 · smart-ensemble 10 · gpt-5.4 5 · gemini-2.5-pro 3 · random-forest 2 · gemini-2.5-flash 2 · claude-opus-4-6 2. Phan bo so model bi cap moi ngay: 0 model 20 ngay · 1 model 20 ngay · 2 model 50 ngay.

3) Co that "71 ngay LIEN TIEP" khong? — CO, TAI LAP DUOC chinh xac: 2026-06-26 .. 2026-09-04 = 71 ngay lien tiep bi loai khoi primary eval, khong ngat ngay nao. Ngay MT VALID cuoi cung la 2026-06-25. NHUNG phai noi ro mot chi tiet V11164 khong noi: chuoi 71 ngay nay gom 70 ngay EXCLUDE_PRIMARY + 1 ngay EXCLUDE_ALL (28/08). Neu chi dem EXCLUDE_PRIMARY thuan thi chuoi bi ngat o 28/08 va chuoi dai nhat con 63 ngay (26/06..27/08). Con so V11164 KHONG tai lap duoc la "it nhat 46/72": do lai ra 45 (cap giai thich tron ven) hoac 70 (cap co tham gia) — khong dinh nghia nao ra 46.

4) So sanh MN va MB cung thuoc:
   - MT: EXCLUDE_PRIMARY 72 + EXCLUDE_ALL 1 = 81,1% · chuoi dai nhat 71 ngay · 70 ngay co cap
   - MN: EXCLUDE_PRIMARY 10 = 11,1% · chuoi dai nhat 1 ngay · 0 ngay co cap
   - MB: EXCLUDE_PRIMARY 73 = 81,1% · chuoi dai nhat 42 ngay (19/07..29/08) · 0 ngay co cap
   Ket qua bat ngo: MB bi loai NHIEU HON MT ve so ngay tuyet doi, nhung 71/73 ngay la do GATE FAIL THAT chu khong phai cap. Day la mot van de RIENG, nam ngoai pham vi va nay.

5) Anh huong dinh luong neu ke toan dung (do tren clone, khong uoc luong; tai lap nguyen van daily_evaluation.py:130-144 · :155-166 · :200-217 · cua so 7/14/9999 tai :366-372):
   MT: wr7 14,3% -> 0,0% (-14,3pp) · wr14 14,3% -> 0,0% (-14,3pp) · wrALL 15,1% -> 10,9% (-4,2pp) · top1_7 57,1% -> 28,6% · top1_14 57,1% -> 21,4% · so luot duoc dem 86 -> 110 · DO TRE cua thuoc 71 ngay -> 0 ngay.
   MN (khong ngay nao doi nhan): wrALL 19,4% -> 18,1%, so luot 144 -> 127.
   MB (khong ngay nao doi nhan): wrALL 5,0% -> 3,0%, so luot 40 -> 33.
   MN/MB doi chi vi LIMIT 270 gop ba mien (daily_evaluation.py:143) — hieu ung phu bat buoc phai bao cho owner.

VIEC 2 — CANDIDATE PATCH (tep MOI, khong de len tep dang serve):
   Cho SINH cac truong, quet ra file:dong that:
   - main.py:9823-9847 — khoi V10752 cap, dong 9840 `filtered_models.add(_dm)` la GOC LOI
   - main.py:10482 `'total_models': model_count` (= selected_voters)
   - main.py:10485 `'output_eligible_row_count'`
   - main.py:10487-10491 `'quality_filtered_model_count'` / `'quality_filtered_models'`
   - main.py:10506 `'incomplete_bundle': model_count < EXPECTED_MODEL_COUNT`
   - main.py:10511 `'wr_gate_filtered': sorted(filtered_models)`
   - main.py:10512 `'gate_diagnostics'` · :10513 `'model_exclusion_reasons'`
   - database.py:5028-5047 classify_bundle_quality · :5074-5091 classify_day_status · :5095-5115 INSERT day_governance
   - daily_evaluation.py:130-144 noi tieu thu (loai ngay EXCLUDE khoi metrics)
   Tach truong theo dung yeu cau, kiem tren du lieu THAT 04/09 MT: expected_output_models=15 · gate_passed_models=15 · capped_models=['meta-learning','random-forest'] (2) · selected_voters=13 · gate_failed_models=[] (RONG dung nhu de bai) · wr_gate_filtered=[] · incomplete_bundle=false · day_status VALID_LIVE_DAY · evaluation_policy INCLUDE.
   Luat da thi hanh: cap co y KHONG tao incomplete_bundle · KHONG tao EXCLUDE_PRIMARY · wr_gate_filtered KHONG chua capped models.

VIEC 3 — TEST + IMPACT + ROLLBACK:
   - Test: 30/30 DAT. A (chi cap) · B (chi truot gate that) · C (ca hai) · D (model khong ra output + cap) · E (hoi quy MN/MB khong doi) · F (bien: khong co bundle / JSON hong -> quay ve hanh vi CU) · G (expected<=0).
   - Historical offline reconstruction: ap patch len 566 dong day_governance tren clone -> doi 45 dong, giu 521. MT doi 45, MN doi 0, MB doi 0.
   - Impact: xem muc 5 tren.
   - Rollback: ba buoc, khong can dung service, khong can sua DB tay, khong co migration schema (chi tiet trong v11165_h12_patch.py --rollback).
   - OWNER_DEPLOY_PACKET: 4 cau hoi can owner ky, cai gi KHONG doi, cai gi DOI, thu tu deploy 4 buoc, 4 rui ro da biet, 4 cong kiem sau deploy — day du tron

## PHAT HIEN
  - [PROVEN_DEFECT] main.py:9840 do CAP CO Y va TRUOT GATE vao chung mot tap — payload tu mau thuan 70/70 ngay
  - [PROVEN_DEFECT] Cap co y bi ke toan thanh THIEU MODEL, sinh DEGRADED_LIVE_DAY + EXCLUDE_PRIMARY cho 45 ngay MT
  - [PROVEN_DEFECT] Rolling WR/TOP1 cua MT dang TRE 71 NGAY — 'rolling 7 luot gan nhat' that ra la du lieu thang 6
  - [PROVEN_DEFECT] daily_evaluation.py:143 dung LIMIT 270 GOP CA BA MIEN — mot mien doi governance keo lech so cua hai mien kia
  - [PROVEN_DEFECT] Hai be mat cong bo hai nhan nguoc nhau cho cung mot ngay/mien
  - [PROVEN_DEFECT] Con so '46/72 quy truc tiep cho ke toan cap' cua V11164 KHONG TAI LAP DUOC — phai rut lai
  - [PROVEN_DEFECT] MB bi EXCLUDE_PRIMARY 73/90 ngay — CAO HON MT — va hoan toan KHONG do cap
  - [INDETERMINATE] Bon tep shadow tu dinh nghia lai DEGRADED_LIVE_DAY bang nguong cung 'm >= 15', khong doc day_governance
  - [PROVEN_DEFECT] TU RUT LAI trong phien: con so mau thuan 'MT 78 / MN 19 / MB 60 ngay' cua buoc O la SAI (RM-21)
  - [OPERATIONAL_IMPROVEMENT] Candidate patch: 3 khoi VA, 30/30 test DAT, replay offline doi dung 45 dong, MN/MB khong doi dong nao

## DAU VAO LAN SAU

## Lan song 2 CAN biet tu gate 12

**1. Ba con so V11164 phai rut lai / bo sung ngay trong bao cao cong khai (PRJ-RETRACTION-001, du 4 phan):**
- Cho goc: bao cao cong khai V11164, muc ke toan MT. Nguyen van cau sai: *"it nhat 46/72 quy truc tiep cho ke toan cap"*. Dieu dung: **45** ngay cap giai thich tron ven (= so ngay doi nhan), hoac **70** ngay co cap tham gia. Phep do tai lap: `python artifacts/v11165_h12_patch.py --replay` tren clone sha256 c3c2f56...
- Bo sung cho "72/90": con **1 ngay EXCLUDE_ALL (28/08)** nen tong bi loai khoi primary eval la **73/90 = 81,1%**.
- Bo sung cho "71 ngay lien tiep": chuoi do **gom ca ngay EXCLUDE_ALL**; chuoi EXCLUDE_PRIMARY **thuan** chi 63 ngay.
- Quyet dinh nao dua tren so sai: chua tim thay quyet dinh nao chi dua vao "46/72" — can lan song 2 xac nhan truoc khi dong RL moi.
- Rut lai NOI BO trong phien nay: con so buoc O ("MT 78 / MN 19 / MB 60 ngay mau thuan") SAI do RM-21, **cam dung**; so dung o v11165_h12_p_mauthuan2.json.

**2. Con so ChOT de dung lai, khong phai do lai:**
- MT 90 ngay: 72 EXCLUDE_PRIMARY + 1 EXCLUDE_ALL · 45 cap-tron-ven · 25 hon hop · 3 khong lien quan · 70 ngay co cap · chuoi 71 ngay (26/06..04/09) · MT VALID cuoi cung 25/06
- MN: 10 (11,1%) · MB: 73 (81,1%), chuoi 42 ngay, 71 ngay gate-fail-that, 0 cap
- Tron lan: 70/70 · 70/70 · 69 ngay du 15 output ma gov INCOMPLETE
- Tac dong MT: wr7 14,3->0,0 · wr14 14,3->0,0 · wrALL 15,1->10,9 · top1_7 57,1->28,6 · top1_14 57,1->21,4 · do tre 71->0 ngay

**3. BA VIEC MOI phat sinh, chua mo, can owner quyet:**
- **V-A (nang):** `daily_evaluation.py:143` `LIMIT days_back*3` gop ba mien -> mot mien doi governance keo lech wrALL cua hai mien kia (MN 19,4->18,1 · MB 5,0->3,0 du 0 ngay doi nhan). Phai sua CUNG LUC voi va gate 12, neu khong owner se thay MB tut ma khong hieu vi sao.
- **V-B (nang, hoan toan rieng):** MB bi loai 73/90 ngay do gate fail that — nhieu hon ca MT. Rolling metrics MB dang tinh tren 40 luot.
- **V-C (vua):** bon tep `_materialize_*_shadow.py` tu dinh nghia DEGRADED_LIVE_DAY bang `m >= 15`, khong doc day_governance -> se lech sau va.

**4. Va gate 12 moi lam 3/4 ho loi (RM-07):** VA-1/VA-2/VA-3 xong; **con `main.py:596` `non_scoreable_count`** trong `_build_official_publish_metadata` lam cung phep tinh ma chua duoc va (VA-4). Khong duoc bao "xong" khi chua co VA-4.

**5. Canh bao ky vong cho owner (nguong: chi tien khong lui):** sua ke toan lam so MT **xau di**, khong dep len. Neu lan song 2 trinh con so MT thi phai kem cau nay, nếu khong owner se doc thanh "sua xong te hon".

**6. Ky thuat da tra gia de biet:**
- `filtered_models

## CHUA TRA LOI

1. **Muc do lech cua bon tep shadow sau khi va** — _materialize_tier2_replay_v2_shadow.py:170 · _materialize_corrected_rescue_replay_shadow.py:247 · _materialize_single_vote_rescue_replay_shadow.py:151 · _materialize_strength_skip_calibration_replay_shadow.py:160 co logic DEGRADED_LIVE_DAY rieng bang nguong cung `m >= 15`, khong doc day_governance. Sau va chung se lech. Chua chay de do so ngay lech vi phai goi ham materialize (co duong ghi DB) — dung theo BLOCKED_BY_SIDE_EFFECT_UNCERTAINTY.

2. **UI tang 5 van KHONG DO DUOC** — viewer-freeze 2026-06-07 (da ghi o V11164). web/frontend/du-doan.html:1352-1354 se doi cach hien "model bi loc chat luong" sau va, nhung khong quan sat duoc thuc te tren UI. Chi suy tu ma nguon, khong tu nang thanh PROVEN.

3. **`_build_official_publish_metadata` (main.py:596) van tinh `non_scoreable_count = len(output_models) - scoreable_count` rieng** — day la cho thu ba lam cung phep tinh, khong doc `_capped_models`. Va gate 12 KHONG cham vao no. Chua do duoc hau qua vi phai goi ham do voi DB production. Da ghi vao OWNER_DEPLOY_PACKET muc rui_ro R4 va can mot VA-4 rieng — cho nay dung nghia la va HIEN TAI moi lam 3/4 ho loi, phai noi thang chu khong bao "xong".

4. **Vi sao V11164 ra con so 46** — chua truy duoc dinh nghia goc nao cho ra 46 (thu 3 dinh nghia: 45 / 70 / 45). Theo RM-11 phai tim dinh nghia goc truoc khi sua, nhung khong doc duoc script sinh ra con so do trong pham vi gate nay. Ghi INDETERMINATE ve NGUYEN NHAN, con ve TINH DUNG SAI thi da du bang chung: 46 khong tai lap duoc.

5. **MB 73/90 ngay bi loai do gate fail that** — do duoc so ngay va nguyen nhan, NHUNG chua tra loi duoc cau "nguong MB min_bt=12 min_wr=26 co qua sau khong". Do la cau hoi ve chinh sach, can nen + suc manh mau + quyet dinh owner, ngoai pham vi gate 12.

6. **Chua do duoc anh huong len bang `du_doan_test_selected_voters` va lane thi nghiem** — main.py:11844/11883/11908 co truong ten `selected_voters` NHUNG thuoc lane test, khac ngu nghia voi truong `sel