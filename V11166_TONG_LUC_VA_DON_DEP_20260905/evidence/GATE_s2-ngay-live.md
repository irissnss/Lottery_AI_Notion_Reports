# s2-ngay-live · tang=EVIDENCE_COMPLETE

## TOM TAT

CONG 7 — CHAT LUONG DU DOAN. Do tren DB production (read-only), 570 bundle 28/02–05/09/2026, doi chieu voi NEN do lai tung ngay tu chinh du lieu (RM-21), khong muon hang so.

TRA LOI THANG: he du doan KHONG tot len — va o thuoc co n lon nhat thi da LOAI TRU duoc moi loi the dang ke. Tren 479 bundle LIVE (30/03–05/09, sau khi bo 91 bundle backfill), bach thu dat 31,7% trong khi boc ngau nhien dat 34,0% (z=-1,05). Thap hon nen o CA BA MIEN va CA NAM cua so 7/30/60/90/160 ngay — 20/20 o deu am hoac bang, khong mot o nao duong co y nghia. Xep hang TOP-10 cua TOTAL (4.520 o, n lon nhat trong phien) trung 34,51% vs nen 33,89%, KTC95 cua chenh lech [-0,73; +1,98] diem — tuc bac bo duoc moi loi the lon hon ~2 diem. Khong co xu huong len hay xuong (moi |z| < 0,8). Ket luan trung khop V11116 va V11164: VAN DUNG YEN.

Do tin cay cua phep do: cham lai bach thu bang dung quy tac cua ham dang serve khop 570/570 nhan da luu; lo2 khop 570/570; bt_hit tung model khop 14.144/14.146. He so thiet ke do lai CHO CHINH THUOC NAY = 0,964 (KHONG dung 2,92 cua RM-18 — do la thuoc khac).

BA PHAT HIEN NGOAI DU KIEN: (1) 91 bundle thang 02–03 la backfill tao 30/03 sau khi da biet ket qua, chung dat +9,8pp TREN nen trong khi phan LIVE duoi nen — chung dang nam chung mot bang voi so LIVE va lam dep lich su; (2) 32 nhan lo3 WIN trong DB la SAI (57 luu vs 25 that); (3) TOTAL co dau hieu THUA trung binh chinh cac model no gop lai (-2,08pp; 14/18 model ti le cao hon TOTAL).

## VIEC CAN LAM

P1 — TACH BACH 91 BUNDLE BACKFILL KHOI SO LIVE. Ai chan: owner (quyet dinh cach danh dau). O dau: bang final_bundles, hien khong co cot phan biet; moi script gop "toan lich su" deu bi nhiem. De xuat: them cot/nhan is_backfill hoac mot bang chan, VA sua cac script bao cao dang gop 180 ngay. Luu y: day la phien SOI, toi KHONG sua gi — chi neu.

P1 — CHAM LAI 32 NHAN lo3 TRONG DB. Ai chan: owner (vi phai GHI vao production DB, ma phien nay cam ghi). O dau: final_bundles.lo3_status, 32 dong thang 03/2026. Loi da va trong code tu V16.1 nhung du lieu cu chua bao gio duoc cham lai. Can chay lai verify voi station_results cho dung 32 dong do, hoac danh dau la khong dang tin.

P1 — RUT LAI moi con so lo3 lich su da tung cong bo (PRJ-RETRACTION-001). Ai chan: agent bao cao. O dau: bat ky bao cao nao tung dung "57 lan WIN lo3" hoac ti le lo3 gop toan lich su. Bon phan bat buoc: cho goc, nguyen van cau sai, dieu dung (25 WIN that, phep do tai lap duoc bang _s7g_fact.py), va quyet dinh nao da dua tren so sai.

P2 — DIEU TRA 78 CA GHI DE bach_thu vs ranked_numbers[0]. Ai chan: chua ai, can mot phien doc ma. O dau: duong ma chon top1 trong main.py + cho ghi ranked_numbers vao source_predictions_json. Cau hoi cu the: ranked_numbers duoc ghi TRUOC hay SAU khi ap gate/lane weight? Neu truoc, thi main_selection_reason dang mo ta sai va moi phan tich dua tren ranked_numbers deu do sai doi tuong.

P2 — DUNG DUA "cai tien +3pp" VAO KE HOACH bang thuoc bach thu. Ai chan: owner khi duyet ke hoach. Can 653 ngay (21,5 thang) moi nghiem thu duoc +3pp o muc GOP 3 mien. Chi tu +8pp tro len (92 ngay) moi do duoc trong mot quy. Thuoc TOP-10 nhay hon nhieu (KTC95 +-1,4pp o n hien co) — neu can do nhanh thi do tren top-10 chu dung do tren bach thu.

P2 — LAM RO KHAU GOP PHIEU CO CON GIA TRI KHONG. Ai chan: owner (day cham vao bo chon model production, §52 muc 13 cam dung). O dau: TOTAL -2,08pp so voi trung binh dau vao cua chinh no, 14/18 model cao hon TOTAL. Chua du manh de ket luan nhung du de dat cau hoi. De xuat: dung shadow (output_eligible=0) so "TOTAL hien tai" vs "boc ngau nhien 1 trong cac model", dang ky nguong TRUOC theo RM-03.

P3 — XAC MINH LAI CON SO DIA. Ai chan: chua ai. O dau: ban chup dau phien ghi 81%, do lai 42%. Truoc khi dung con so dia lam can cu (vi du tu choi tao clone DB), phai do lai.

P3 — combo-super: KHONG mo lai cau hoi cat/giu bang so hien co. n=18 quyet dinh doi, dau doi khi doi cua so. Muon ket luan phai cho tich du n, hoac doi thuoc. Nhac §59: neu co de xuat cat thi phai noi ro "bo co output_eligible" hay "dung han", va pool ML >= 4 / AI >= 3.

## PHAT HIEN
  [P1][NO_ANOMALY_FOUND] Bach thu KHONG vuot nen o bat ky mien nao, bat ky cua so nao — tai xac nhan V11116/V11164
  [P1][PROVEN_DEFECT] 91 bundle backfill (28/02–30/03) tao SAU khi da co ket qua, dat +9,8pp TREN nen, dang nam chung bang voi so LIVE
  [P1][PROVEN_DEFECT] 32 nhan lo3 WIN trong DB la SAI — lich su 3-cang dang phong dai 2,28 lan
  [P2][SUSPICIOUS_NEEDS_MORE_EVIDENCE] TOTAL co dau hieu THUA trung binh chinh cac model ma no gop lai — nhung chua du manh de ket luan
  [P2][NO_ANOMALY_FOUND] Xep hang TOP-10 cua TOTAL khong mang thong tin — bang dung boc 10 so ngau nhien, va lan nay n DU LON de ket luan
  [P2][SUSPICIOUS_NEEDS_MORE_EVIDENCE] 78 bundle: bach_thu cong bo KHAC ranked_numbers[0], nhung metadata van ghi main_selection_reason = 'max_ranked_score_after_gate_and_lane_weight'
  [P3][INDETERMINATE] combo-super: bo no ra thi 18/416 bundle doi top1, rong -2 (cuu 1, pha 3) — n qua nho, chua duoc phep ket luan
  [P3][NO_ANOMALY_FOUND] Khong co xu huong tot len hay xau di trong 30–90 ngay
  [P3][EXPECTED_BEHAVIOR] MB trung ca bach thu lan lo2 hom 05/09 nam tron trong nhieu — khong phai dau hieu
  [P3][SUSPICIOUS_NEEDS_MORE_EVIDENCE] Canh bao dia trong ban chup dau phien khong con dung khi do lai