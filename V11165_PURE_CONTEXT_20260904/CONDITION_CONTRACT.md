# CONDITION_CONTRACT — V11165 · Gate 5

**Quy tac chuyen BO SO thanh DIEU KIEN.** Ngay 2026-09-05 · lan song 2 · `SCOPE: RIENG — Lottery_AI_Test`

> **Tang verdict: `CODED_AND_TESTED_NOT_RUNTIME_PROVEN`**
> Day la BAN HOP DONG + BANG DOI CHIEU 35 dong + cac phep do nen. KHONG sua ma dang serve, KHONG deploy, KHONG co phep do tien nao chung minh bo bot bo so lam tang do trung. Muc tieu owner #9 doi DO TIEN — chua co.
> 
> CAM doc thanh `DEPLOYED` · `RUNTIME_PROVEN` · `OFFICIAL_CLEAN` · `PREDICTIVE_IMPROVEMENT_PROVEN`.

## 0. Ban nay la gi, va KHONG phai gi

Ban nay **khong sua mot dong ma nao dang serve**. No lam ba viec:

1. Dinh nghia **hop dong `CONDITION_CONTRACT`** — bo truong bat buoc de mot dieu kien duoc phep di vao prompt.
2. **Do nen** cho tung thuoc ma cac dieu kien se dung — vi khong co nen thi khong dieu kien nao hop le (nguyen tac 6).
3. Ap **muoi hai nguyen tac chuyen doi** cho **tung** trong **35 producer** da kiem ke o lan song 1, ra **bang doi chieu 35 dong**.

Dieu ban nay **KHONG** lam: khong chung minh rang bo bot bo so se lam **tang do trung**. Muc tieu owner so 9 doi **do tien** — chua co phep do nao. Moi so trong ban nay la so **mo ta cau truc va nen**, khong phai so **du bao**.

## 1. Nguon do — tai lap duoc

| muc | gia tri |
|---|---|
| clone bat bien | `/root/Lottery_AI_Test/artifacts/v11165_immutable.db` |
| sha256 | `c3c2f5688f0abbfc34b6fcdf9a0ef689cc509b0d4f9839b19e00ceb6efebb6e2` |
| kiem lai trong phien | **KHOP** |
| che do mo | `sqlite3 mode=ro (uri=True) — CHI DOC` |
| kiem ke lan song 1 | `v11165_h4_set_to_condition.json` (35 producer) |
| dump prompt that | 6 tep `v11165_h4_prompt_<MIEN>_<REGIME>.txt` |
| script do lan song 2 | `_k5b_nen.py` · `_k5c_k_va_khoi.py` · `_k5d_nen_khop.py` · `_k5e_minedat.py` · `_k5h_boi.py` |

Kich thuoc prompt that do lai tren dump (RM-14 — do tren dump tu ham dang serve, khong doc tai lieu):

| dump | ky tu | dong |
|---|---:|---:|
| `MB_OFFICIAL_LEGACY` | 55.178 | 1.098 |
| `MB_SHADOW_CONTEXT_ONLY` | 58.124 | 1.144 |
| `MN_OFFICIAL_LEGACY` | 50.464 | 1.013 |
| `MN_SHADOW_CONTEXT_ONLY` | 53.877 | 1.066 |
| `MT_OFFICIAL_LEGACY` | 51.487 | 1.038 |
| `MT_SHADOW_CONTEXT_ONLY` | 54.571 | 1.086 |

## 2. Hop dong CONDITION_CONTRACT — 24 truong bat buoc

Mot dieu kien **thieu bat ky truong nao** thi **khong duoc vao prompt**. Truong khong ap dung thi ghi `null` **kem ly do**, cam bo trong.

| # | truong | phai chua gi |
|---:|---|---|
| 1 | `condition_id` | ma on dinh, khong tai dung cho viec khac |
| 2 | `condition_version` | doi noi dung => tang version; phep do cu gan voi version cu |
| 3 | `condition_family` | RAW · UNIVERSE · STAT · RULE · SPEND · TOOL · SHADOW |
| 4 | `scope_region` | MN / MT / MB — cam de trong roi ngam hieu 'moi mien' |
| 5 | `scope_weekday` | thu nao; `moi thu` phai ghi ro |
| 6 | `scope_station_set` | **dai nao**; neu da cat bot phai ghi cat bao nhieu va theo tieu chi gi |
| 7 | `scope_prize_set` | **giai nao**; nhu tren |
| 8 | `source_lag` | D / D-1 / D-2 / n tuan |
| 9 | `as_of` | **cutoff that trong SQL**, khong phai y dinh. `date('now')` KHONG phai cutoff |
| 10 | `source_event_ids` | id ban ghi goc — de truy nguoc |
| 11 | `raw_observations` | quan sat tho TRUOC moi phep bien doi |
| 12 | `predicate_definition` | menh de, dang van ban, khong phai ten khoi |
| 13 | `transform_definition` | **tung** phep union/sort/top-k/boost/chia nhom — ke du |
| 14 | `candidate_binding_mode` | FULL_UNIVERSE_SYMMETRIC · RAW_EVENT_NARRATIVE · RULE_PROPOSITION · REAL_QUERY_TOOL · CANDIDATE_NEGATIVE · SHADOW_ONLY |
| 15 | `observed_value` | **nguyen van dong trong prompt that**, khong dien giai lai |
| 16 | `expected_baseline` | nen do **cho chinh thuoc nay** (RM-21). `null` chi khi that su khong co khai niem nen |
| 17 | `sample_n` | n that, kem don vi (luot / ngay / tuan) |
| 18 | `effect_size` | hieu so voi nen, **tach TRONG/NGOAI cua so chon** |
| 19 | `uncertainty` | KTC + **design effect do cho chinh thuoc nay** |
| 20 | `evidence_status` | mot nhan tu vung dong (muc 3) |
| 21 | `independence_group` | lineage goc — de nguyen tac 9 dem dung |
| 22 | `availability_at_prediction_time` | co ton tai truoc cutoff cua mien dich khong |
| 23 | `known_limitations` | ke that; day la cho ghi dieu chua chung minh duoc |
| 24 | `source_hash` | hash ma nguon sinh ra no |

## 3. `evidence_status` — tu vung DONG

| nhan | nghia | so dieu kien |
|---|---|---:|
| `RAW_FACT` | Su kien xo so that, co ngay/mien/dai/giai/cutoff. Khong phai suy dien. | 2 |
| `MECHANICALLY_DERIVED` | Phep dem/phep bien doi tat dinh tu RAW_FACT, trinh bay doi xung toan 00-99. Khong khang dinh gi ve tuong lai. | 3 |
| `HYPOTHESIS_ONLY` | Gia thuyet chua co phep do tien nao ung ho. Duoc phep xuat hien nhu DU KIEN, CAM dung lam can cu uu tien. | 5 |
| `RETROSPECTIVE_ONLY` | Chi co bang chung TRONG cua so da chon ra chinh no. Do tien ngoai cua so hien n=20/mien tren 4 ngay => CHUA DUOC PHEP KET LUAN (RM-04). | 6 |
| `UNAVAILABLE` | Khong the phuc vu bang prompt tinh — can real query tool, ma lan song 1 do duoc la KHONG model nao bat tool. | 1 |
| `PROSPECTIVE_PENDING` | (chua dieu kien nao dat nhan nay) | 0 |
| `PROSPECTIVE_SUPPORTED` | (chua dieu kien nao dat nhan nay) | 0 |
| `REJECTED` | (chua dieu kien nao dat nhan nay) | 0 |

> 🔴 **Khong dieu kien nao dat `PROSPECTIVE_SUPPORTED`.** Do la ket qua, khong phai thieu sot cua ban kiem ke: chua co phep do tien nao du mau cho bat ky dieu kien nao trong 17 dieu kien.

## 4. NEN — do rieng cho tung thuoc (nguyen tac 6 + RM-21)

Nguyen tac 6 cam dung con so ma khong noi nen. Nhung **nen cua thuoc nao thi chi dung cho thuoc do** (RM-21). Duoi day la nen do that tren clone bat bien, cua so **W180 ket thuc 2026-09-04**:

| thuoc | MN | MT | MB |
|---|---:|---:|---:|
| so duoi khac nhau / ngay | 43.0 | 35.1 | 23.7 |
| so dai / ngay | 3.1 | 2.4 | 1.0 |
| **T1** bach thu (1 duoi co mat) | **0.4298** | **0.3509** | **0.2374** |
| **T3** duoi trung DB | 0.0312 | 0.0241 | 0.0100 |
| **T4** duoi trung G8 | 0.0309 | 0.0239 | 0.0100 |
| **T5** ca hai duoi cua mot cap | 0.1841 | 0.1246 | 0.0548 |

**T2 — bo k duoi, TRUNG = it nhat mot duoi co mat** (day la thuoc ma phan lon khoi trong prompt dang dung ma khong khai):

| k | MN nen dung | MN `1-(1-b)^k` | MT nen dung | MT `1-(1-b)^k` | MB nen dung | MB `1-(1-b)^k` |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 0.6756 | 0.6749 | 0.5773 | 0.5787 | 0.4201 | 0.4185 |
| 3 | 0.8158 | 0.8146 | 0.7238 | 0.7266 | 0.5603 | 0.5566 |
| 4 | 0.8958 | 0.8943 | 0.8190 | 0.8225 | 0.6676 | 0.6619 |
| 5 | 0.9412 | 0.9397 | 0.8811 | 0.8848 | 0.7494 | 0.7422 |
| 8 | 0.9897 | 0.9888 | 0.9660 | 0.9685 | 0.8946 | 0.8857 |
| 11 | 0.9983 | 0.9979 | 0.9903 | 0.9914 | 0.9570 | 0.9493 |
| 16 | 0.9999 | 0.9999 | 0.9988 | 0.9990 | 0.9910 | 0.9869 |

**Doc bang nay the nao — ba dieu:**

1. **Nen RAT CAO.** Voi MN, mot bo **5 duoi** co nen **94,1%**. Nghia la mot khoi in `5W(35d):215/235=91%` dang bao mot con so **THAP HON** nen cua chinh no.
2. **`1-(1-b)^k` du dung**, sai so |lech| ≤ 0,9pp tren moi k va moi mien da do. RM-18 cho phep dung cong thuc nay — nhung **phai dung `b` cua dung mien**.
3. 🔴 **Cam muon nen giua cac mien.** MN `b=0,4298` · MB `b=0,2374` — **gan gap doi**. MB chi co **mot dai**, MN co **3.1 dai/ngay**. Ap nen MN cho MB la `RM-21_VIOLATION`.

## 5. Phep thu quyet dinh — con so prompt DANG IN, doi chieu nen khop

Thuoc: mot luot danh gia luat sinh `k` duoi; TRUNG = it nhat mot duoi co mat trong tap duoi cua (mien, ngay). Nen **khop tung dong**: `1 − C(100−D, k) / C(100, k)` voi `D` la so duoi khac nhau cua chinh mien-ngay do, `k` la `tails_count` cua chinh luot do.

**k that do duoc** (W42 ket thuc 04/09): MN **3,96** · MT **3,70** · MB **2,52**.

| mien | prompt IN (nguyen van dump 04/09) | nen khop do duoc | doc lai |
|---|---|---:|---|
| MN | `6W(42d):265/288=92%` (official L567) | **0,844** | hon nen ~7,5pp — va la **so tu cham** (trong cua so da dao ra chinh cac luat do) |
| MT | — | **0,741** | |
| MB | `6W(42d):250/384=65%` (official L593) | **0,473** | con so **trong nhu that bai** that ra **hon nen ~10pp** |

> 🔴 **Ca hai chieu deu bi doc sai khi thieu nen.** MN `92%` doc len nhu «gan chac chan» trong khi nen da la 84%. MB `57%` doc len nhu «hong» trong khi nen chi 47%. Day chinh la dieu nguyen tac 6 cam: *«Cam dung 83% neu nen cua bo do da 86%»*.

### 5.1 Hieu chinh so sanh boi — 12 dong `100.0%` dang gia bao nhieu

Prompt MN official in **12 dong** dang `🔥[TOP] MB(D-1/CN) · Thai Binh G1+G7: 6/6=100.0%` (L569–L586) nhu bang chung manh nhat. Do tren clone, cua so 42 ngay, o co `n≥3`:

| mien | o duoc quet | o du tuyen `n≥3` | o dat 100% **quan sat** | o dat 100% **ky vong duoi nen** |
|---|---:|---:|---:|---:|
| MN | 53 | 51 | **32** | **25.00** |
| MT | 58 | 54 | **23** | **16.04** |
| MB | 78 | 74 | **4** | **3.55** |

> **MB: quan sat 4 o dat 100%, ky vong duoi nen 3,55.** Gan nhu khong con du gi. **MN: 32 so voi 25.** Cac dong `6/6=100.0%` la dieu may rui **gan nhu chac chan** sinh ra khi quet 51 o roi in 12 dong cao nhat.

Cau **«12 tuan gan nhat trung 12/12 · 16 tuan trung 16/16»** (dump MN L695–L699, **lap 4 lan trong mot khoi**):

| mien | nen khop tb | P(mot luat dat 12/12) | ky vong so luat dat 12/12 **trong 105 luat** |
|---|---:|---:|---:|
| MN | 0.8378 | 0.1195 | **12.6** |
| MT | 0.7273 | 0.0219 | **2.3** |
| MB | 0.4711 | 0.0001 | **0.0** |

> Voi MN, **12,6 luat trong 105** dat `12/12` **hoan toan do may rui**. Cau «12/12 · 16/16» khong phai bang chung; no la dieu phai xay ra.

## 6. Tach TRONG / NGOAI cua so chon (`PRJ-SELECTION-WINDOW-001`)

**Dinh nghia dung:** ca **105** luat trong `mined_rules` deu co `mined_at = 2026-08-31T00:30`, `rule_version = v2026W36`, `is_active = 1`. Nghia la:

- **TRONG cua so chon** = luot danh gia co `date ≤ 2026-08-31` — du lieu do **da tham gia dao ra chinh cac luat nay**. Day la **tu cham**.
- **NGOAI cua so chon** = `date > 2026-08-31`, tuc **01/09–04/09 = 4 ngay**.

| mien | cua so | TRONG: hieu so voi nen | NGOAI: hieu so voi nen | NGOAI: n | NGOAI: z cum | NGOAI: KTC95 |
|---|---|---:|---:|---:|---:|---|
| MN | W180 | **+7.24 pp** | **-3.09 pp** | 20 (4 ngay) | -0.258 | [-26.58; 20.39] |
| MT | W180 | **+10.72 pp** | **-3.73 pp** | 20 (4 ngay) | -0.645 | [-15.08; 7.61] |
| MB | W180 | **+17.40 pp** | **-15.09 pp** | 20 (4 ngay) | -1.147 | [-40.87; 10.69] |

**Doc dung — ba cau, khong duoc bo cau nao:**

1. **TRONG cua so chon:** luat hon nen **+7,24 / +10,72 / +17,40 pp** (MN/MT/MB), z cum theo ngay 6,6–7,0. Nhung day la **diem tu cham** — cac luat duoc chon ra **vi** trong nhu the.
2. **NGOAI cua so chon:** diem uoc luong **AM o ca ba mien** (−3,09 / −3,73 / −15,09 pp), z cum −0,26 / −0,65 / −1,15, **KTC95 deu chua so 0**.
3. 🔴 **Nhung n = 20 luot / mien tren 4 NGAY.** Theo `RM-04` day la **«CHUA DUOC PHEP KET LUAN»**, **khong phai** «luat yeu». Cam viet «do tien cho thay luat khong hieu qua» — mau chua du de noi cau do theo ca hai huong.

Day la lan **thu hai** cung mot hinh: `RM-18` do duoc luat hon nen **+7,5 / +13,8 / +20,7 diem** *trong* cua so chon va **dung bang 0** ngoai cua so. Phep do o ban nay dung **thuoc khac** (hit_any cua bo k duoi so voi nen khop) va ra **cung mot hinh**.

> ⚠️ **Cố ý trích MỘT cửa sổ** (`PRJ-SELECTION-WINDOW-001` · RM-18). Phiên này **không** tuyên bố
> hiệu quả của luật khai mỏ, nên cả bốn vế — **trong cửa sổ chọn · ngoài cửa sổ chọn · trong mẫu ·
> ngoài mẫu** — đều để trống có chủ ý. Bộ đủ nằm ở **RM-18/V11030** (**+7,5 / +13,8 / +20,7 điểm
> TRONG cửa sổ chọn, ĐÚNG BẰNG 0 ngoài cửa sổ**) và **V11073** (**+9,9% trong mẫu → −1,6% ngoài
> mẫu**). Đo bổ sung của phiên này: **n = 20/miền trên 4 ngày** ⇒ **RM-04, chưa được phép kết
> luận**; KTC95 đều chứa 0. Báo một vế là giấu mất nửa sự thật.
**Gioi han phai ghi:** **2.421/5.035** luot danh gia co `rule_id` **khong con** trong `mined_rules` (luat the he truoc da bi xoa) — khong tach duoc trong/ngoai cho nhung luot do. Da tach rieng nhan `KHONG_RO_mined_at`, **khong gop** vao ket luan tren.

## 7. Muoi hai nguyen tac — va so producer vi pham tung cai

| ma | nguyen tac | so producer vi pham |
|---|---|---:|
| **NT-01** | Raw fact chi duoc xuat hien khi co du: ngay · mien · dai · giai · bo · lag · cutoff. | **4** |
| **NT-02** | CAM lay raw facts roi union/sort/top-k/boost/to nong/chia fresh-spent/de xuat-tranh ma van goi la 'ngu canh thuan'. | **26** |
| **NT-03** | Condition gan voi candidate cu the: HOAC doi xung toan bo 00-99, HOAC candidate do model tu suy tu raw facts, HOAC co real query tool. CAM chi dua top ung vien. | **14** |
| **NT-04** | Neu trinh full-universe 00-99: khong rank · khong sort theo score · thu tu co dinh 00->99 · chi boolean/categorical · khong tong diem bi mat · khong to mau/emoji tao uu tien · PHAI kiem token budget. | **0** |
| **NT-05** | Neu bao model 'truy van': phai co tool THAT. Lan song 1 do duoc: KHONG model nao bat tool => moi cau 'hay tu truy van DB' deu PHAI BO. | **1** |
| **NT-06** | Moi condition phai noi muc bang chung: nen dung theo mien/thu/bo dai · n · retrospective hay prospective · uncertainty. Cam dung '83%' neu nen cua bo do da 86%. | **31** |
| **NT-07** | Condition KHONG duoc ra lenh (uu tien/boost/tranh/bat buoc chon/chot manh) neu chua co policy Owner-locked va prospective evidence. | **13** |
| **NT-08** | Same-day prior-region: chi dua khi ket qua THAT da ton tai truoc cutoff cua mien dich; trinh bay la raw event; KHONG tu gan FULL_SPENT/FRESH neu gia thuyet do chua duoc do. | **1** |
| **NT-09** | Convergence: dem independent station/source groups; khong dem cung lineage nhieu lan; khong tu suy 'nhieu nguon = tot'; trinh bay correlation/herding risk. | **5** |
| **NT-10** | Model performance/rank/weight: DROP khoi LLM prompt hoan toan. | **6** |
| **NT-11** | ML output: khong bom candidate shortlist cua ML vao LLM roi goi la hai nguon doc lap. | **2** |
| **NT-12** | 3-cang: khong dua vao output contract tung model; downstream van la prefix + final BT dung lane. | **0** |

**Hai nguyen tac co so 0 — va vi sao, ghi ro chu khong de trong:**

- **NT-04** (luat render doi xung 00-99): **0** vi **khong producer nao hien dang render full-universe**. Do khong phai «da dat» — do la «chua co cai gi de vi pham». NT-04 la luat cho **ban moi**, ap cho `C-UNIV-01/02/03`.
- **NT-12** (3-cang): **0** vi 35 producer nay deu thuoc ho **bo so / meta**; duong 3-cang duoc xu o lane rieng (V11162). Khong co nghia la 3-cang sach — **chua kiem trong gate nay**.

🔴 **Nguyen tac bi vi pham nhieu nhat: `NT-06` — 31/35 producer.** Do la nguyen tac «phai noi muc bang chung». Noi cach khac: **31 trong 35 nguon bom so vao prompt khong kem nen, khong kem n, khong noi retrospective hay prospective.** Lan song 1 dem doc lap ra cung mot hinh: **chi 1/35 co nen tuong minh**.

## 8. Lineage goc — vi sao «nhieu nguon cung tro» khong phai «nhieu bang chung»

| lineage | nghia | so producer |
|---|---|---:|
| `L1_LOTTERY_EVENTS` | Ket qua xo so THAT (lottery_results / source_data). Nguon doc lap DUY NHAT. | 17 |
| `L2_SYSTEM_PREDICTIONS` | Bang `predictions` — du doan cua CHINH he. KHONG doc lap voi L1, va la vong lap tu tang cuong. | 6 |
| `L3_SYSTEM_OUTPUT` | Bang `final_bundles` — output DA CONG BO cua chinh he. | 1 |
| `L4_MINED_RULES` | mined_rules / mined_rule_effectiveness / rule_engine — DAO TU L1 va DA CHON LOC. KHONG doc lap voi L1; hai luat cung tro mot duoi KHONG phai hai nguon. | 8 |
| `L5_MB_RULES` | mined_rules_mb_daily / mb_rule_context — cung ho L4, rieng MB. | 1 |
| `L6_FROZEN_KB_FILE` | _knowledge_base.json — dan xuat tu L1 nhung DONG BANG tu 2026-04-26 00:45:54. | 2 |

> **`L4_MINED_RULES` dao ra tu `L1_LOTTERY_EVENTS`.** Bon luat cung tro mot duoi **khong phai bon nguon doc lap**. Dump MN 04/09 chung minh truc tiep: bon su kien sinh ra `CONV×4` cho duoi `08` (L694–L700) deu la **«dai Ha Noi (MB) ngay 03/09»** — **mot dai, mot ngay, bon cach cat giai**. Tuong tu, `nguon ung ho=3/3 [MN(D-1)+MT(D-1)+MB(D-1)]` dem ba mien nhu ba nguon, trong khi ca ba deu di qua **cung bo luat L4**.

## 9. BANG DOI CHIEU 35 DONG

`disposition` lay **nguyen** tu tu vung dong cua lan song 1. `condition_id` chi co khi producer duoc **giu duoi dang dieu kien**.

| # | producer | disposition | condition_id | lineage | ung vien -> | NT vi pham |
|---:|---|---|---|---|---|---|
| 1 | `P01_TOP5_GOI_Y` | `RENDER_FULL_UNIVERSE_SYMMETRICALLY` | **`C-UNIV-01`** | `L1_LOTTERY_EVENTS` | 5 | NT-02 NT-03 NT-06 |
| 2 | `P02_GAN_CAO` | `DROP_UNSUPPORTED` | — | `L1_LOTTERY_EVENTS` | 3 | NT-02 NT-03 NT-06 NT-07 |
| 3 | `P03_HOT` | `DROP_UNSUPPORTED` | — | `L1_LOTTERY_EVENTS` | 8 | NT-02 NT-03 NT-06 |
| 4 | `P04_TANG` | `TRANSLATE_TO_NEUTRAL_CONDITION` | **`C-STAT-01`** | `L1_LOTTERY_EVENTS` | 5 | NT-02 NT-03 NT-06 |
| 5 | `P05_DOW_HAY_RA` | `DROP_DUPLICATE` | — | `L1_LOTTERY_EVENTS` | 3 | NT-02 NT-03 NT-06 |
| 6 | `P06_DO_TIN_CAY_WEIGHTS` | `DROP_MODEL_META` | — | `L2_SYSTEM_PREDICTIONS` | 0 | NT-06 NT-07 NT-10 |
| 7 | `P07_DE_XUAT_PYTHON` | `BLOCK_ORACLE` | — | `L1_LOTTERY_EVENTS` | 2 | NT-02 NT-03 NT-06 NT-07 NT-11 |
| 8 | `P08_SO_NEN_TRANH` | `DROP_UNSUPPORTED` | — | `L1_LOTTERY_EVENTS` | 11 | NT-02 NT-03 NT-06 NT-07 |
| 9 | `P09_MIRROR_PAIRS` | `RENDER_FULL_UNIVERSE_SYMMETRICALLY` | **`C-UNIV-02`** | `L1_LOTTERY_EVENTS` | 10 | NT-02 NT-03 NT-06 |
| 10 | `P10_LICH_SU_DU_DOAN_CUA_BAN` | `DROP_MODEL_META` | — | `L2_SYSTEM_PREDICTIONS` | 7 luot x <=2 so + top5 | NT-02 NT-06 NT-10 |
| 11 | `P11_OVERDUE_SAP_VE` | `DROP_UNSUPPORTED` | — | `L1_LOTTERY_EVENTS` | 5 | NT-02 NT-03 NT-06 NT-07 |
| 12 | `P12_HOT_BY_GAP` | `DROP_UNSUPPORTED` | — | `L1_LOTTERY_EVENTS` | 5 | NT-02 NT-03 NT-06 |
| 13 | `P13_DIGIT_SUM_WINNING` | `DROP_MODEL_META` | — | `L2_SYSTEM_PREDICTIONS` | 5 | NT-02 NT-06 NT-10 |
| 14 | `P14_TOP_POSITIONS` | `RENDER_FULL_UNIVERSE_SYMMETRICALLY` | **`C-UNIV-03`** | `L1_LOTTERY_EVENTS` | 6 | NT-02 NT-03 NT-06 |
| 15 | `P15_CAP_DOI` | `TRANSLATE_TO_NEUTRAL_CONDITION` | **`C-STAT-02`** | `L1_LOTTERY_EVENTS` | 10 | NT-02 NT-03 NT-06 NT-07 |
| 16 | `P16_KET_QUA_NGAY_TRUOC` | `KEEP_RAW_FACT` | **`C-RAW-01`** | `L1_LOTTERY_EVENTS` | 6 | NT-01 |
| 17 | `P17_LICH_SU_DAI` | `KEEP_RAW_FACT` | **`C-RAW-02`** | `L1_LOTTERY_EVENTS` | 4 dai x 3 ky x (2 raw + 3 top) | NT-01 NT-02 |
| 18 | `P18_KB_PATTERN_DAI` | `BLOCK_AMBIGUOUS` | — | `L6_FROZEN_KB_FILE` | 4 dai x 17 = <=68 | NT-01 NT-02 NT-06 |
| 19 | `P19_KB_DOW` | `BLOCK_AMBIGUOUS` | — | `L6_FROZEN_KB_FILE` | 14 | NT-01 NT-02 NT-06 |
| 20 | `P20_TAN_SUAT_DUOI_5_GIAI` | `DROP_DUPLICATE` | — | `L1_LOTTERY_EVENTS` | 5 x so dai | NT-02 NT-03 |
| 21 | `P21_MINED_RULES` | `TRANSLATE_TO_NEUTRAL_CONDITION` | **`C-RULE-01`** | `L4_MINED_RULES` | 5 | NT-06 |
| 22 | `P22_RULE_TAILS` | `DROP_DUPLICATE` | — | `L4_MINED_RULES` | 8 | NT-02 NT-03 NT-06 NT-07 NT-09 |
| 23 | `P23_EVIDENCE_WINDOWS` | `TRANSLATE_TO_NEUTRAL_CONDITION` | **`C-RULE-02`** | `L4_MINED_RULES` | 0 | NT-06 |
| 24 | `P24_EVIDENCE_SOURCE_PRIZE` | `TRANSLATE_TO_NEUTRAL_CONDITION` | **`C-RULE-03`** | `L4_MINED_RULES` | 18 | NT-02 NT-06 NT-07 |
| 25 | `P25_BOI_CANH_SOI_CAU` | `TRANSLATE_TO_NEUTRAL_CONDITION` | **`C-RULE-04`** | `L4_MINED_RULES` | union tails cua moi luat active (do 04/09 MN: 16 duoi rieng) | NT-02 NT-06 |
| 26 | `P26_CONVERGENCE_TRAP` | `TRANSLATE_TO_NEUTRAL_CONDITION` | **`C-RULE-05`** | `L4_MINED_RULES` | moi duoi co conv>=3 (04/09 MN: 4) | NT-06 NT-09 |
| 27 | `P27_SHADOW_BLOCKS` | `DROP_DUPLICATE` | — | `L4_MINED_RULES` | 10 | NT-02 NT-06 NT-09 |
| 28 | `P28_ANTITRAP_SPEND` | `TRANSLATE_TO_NEUTRAL_CONDITION` | **`C-SPEND-01`** | `L1_LOTTERY_EVENTS` | 10 | NT-02 NT-06 NT-07 NT-08 NT-09 |
| 29 | `P29_D1_POOL_COUNT` | `EXPOSE_VIA_REAL_QUERY_TOOL` | **`C-TOOL-01`** | `L1_LOTTERY_EVENTS` | 0 | NT-05 |
| 30 | `P30_WEEKDAY_SCAN_LIVINGNESS` | `TRANSLATE_TO_NEUTRAL_CONDITION` | **`C-RULE-06`** | `L4_MINED_RULES` | <=5+5+4+3 nhan nguon | NT-02 NT-06 NT-07 |
| 31 | `P31_PHASE11_MODEL_META` | `DROP_MODEL_META` | — | `L2_SYSTEM_PREDICTIONS` | 8 | NT-06 NT-10 |
| 32 | `P32_PHASE14A_MODEL_RANKING` | `DROP_MODEL_META` | — | `L2_SYSTEM_PREDICTIONS` | 0 | NT-06 NT-07 NT-10 |
| 33 | `P33_LANE_TEST_D1_BUNDLE` | `SHADOW_HYPOTHESIS_ONLY` | **`C-SHADOW-01`** | `L3_SYSTEM_OUTPUT` | 2 (bundle) + 71 (D-2 pool) + 8 dong tin hieu | NT-02 NT-06 NT-07 NT-09 |
| 34 | `P34_MB_RULE_STACK_PROD_MANUAL` | `TRANSLATE_TO_NEUTRAL_CONDITION` | **`C-RULE-07`** | `L5_MB_RULES` | 14 | NT-02 NT-06 NT-07 |
| 35 | `P35_MB_HARD_MODE_MODEL_META` | `DROP_MODEL_META` | — | `L2_SYSTEM_PREDICTIONS` | 0 | NT-06 NT-10 NT-11 |

**Tong hop disposition:**

| disposition | so producer |
|---|---:|
| `TRANSLATE_TO_NEUTRAL_CONDITION` | 10 |
| `DROP_MODEL_META` | 6 |
| `DROP_UNSUPPORTED` | 5 |
| `DROP_DUPLICATE` | 4 |
| `RENDER_FULL_UNIVERSE_SYMMETRICALLY` | 3 |
| `KEEP_RAW_FACT` | 2 |
| `BLOCK_AMBIGUOUS` | 2 |
| `BLOCK_ORACLE` | 1 |
| `EXPOSE_VIA_REAL_QUERY_TOOL` | 1 |
| `SHADOW_HYPOTHESIS_ONLY` | 1 |
| **TONG** | **35** |

=> **17 producer sinh ra dieu kien** · **18 producer bi DROP hoac BLOCK** · **17 dieu kien** duoc dinh nghia (mot so dieu kien gop nhieu producer).

## 10. LY DO BO — tung producer bi DROP / BLOCK

**`P02_GAN_CAO`** — `DROP_UNSUPPORTED`  
DROP_UNSUPPORTED — gia thuyet 'gan cao => sap ra' DA bi do va bac: V11001 do 6,5 nam, gan 10-18 ngay MN +0,97 MT +0,59 MB +0,55, khong huong nao |z|>2. Con la ban sao y niem cua P11. Va no MAU THUAN voi chinh SYSTEM_PROMPT §5 ('GAN cao KHONG co nghia sap ra').

**`P03_HOT`** — `DROP_UNSUPPORTED`  
DROP_UNSUPPORTED — khong nen, khong n, khong bang chung ngoai mau; trung ho voi P08 va P12. Owner 06/08 nguyen van: 'cai anh khong thich nhat la gan, cold, hot no cha tich su gi'.

**`P05_DOW_HAY_RA`** — `DROP_DUPLICATE`  
DROP_DUPLICATE — noi CUNG MOT viec tren CUNG MOT truc (mien x thu) voi P19_KB_DOW, nhung hai bo so KHAC HAN (P05: 85,74,02 tu 60 ngay live; P19: 28,53,69,98,70 tu tep dong bang). Hai cau ve cung mot dai luong bao khac nhau = PRJ_PROMPT_CONTRADICTS. Giu P05 lam nguon, bo ca hai ban hien tai, tai sinh qua C-UNIV-01 (cot theo thu).

**`P06_DO_TIN_CAY_WEIGHTS`** — `DROP_MODEL_META`  
DROP_MODEL_META — NT-10 bo tuyet doi. Ngoai ra nhan noi nguoc voi so: nhan la 'DO TIN CAY' trong khi Lift = -24,5% (AM).

**`P07_DE_XUAT_PYTHON`** — `BLOCK_ORACLE`  
BLOCK_ORACLE — day la vi pham truc tiep nhat voi muc tieu owner #3 va #8. Prompt dua san DAP AN dung dang hop dong dau ra (main_number + secondary_number, kem score) roi HAI menh lenh ep model theo: SYSTEM_PROMPT §5b 'Neu Python metrics va phan tich thu cong mau thuan -> uu tien Python metrics' (gpt_analyzer.py:337-341) va metrics_calculator.py:635 'Day la tinh toan Python, AI nen uu tien'. Model khong con 'tu chon'. CAM tai sinh duoi dang condition — day la RECOMMENDATION, khong phai CONDITION.

**`P08_SO_NEN_TRANH`** — `DROP_UNSUPPORTED`  
DROP_UNSUPPORTED — JUST_HIT/OVER_HOT dua tren tien de 'da het luot' (metrics_calculator.py:495) — nguy bien con bac. 'expected' chi la dong nhat 1/100, KHONG phai nen cua bo k duoi (RM-18). Mau thuan voi V11007 ('moi luot xo doc lap').

**`P10_LICH_SU_DU_DOAN_CUA_BAN`** — `DROP_MODEL_META`  
DROP_MODEL_META — bom WR cua CHINH model + lich su thang/thua vao CA HAI regime, ke ca lane 'ngu canh thuan'. Muc tieu owner #5 cam dung win rate de day LLM. Kem khe ho cau truc: gpt_analyzer.py:2461-2467 chi 'ORDER BY date DESC LIMIT 7', KHONG co 'date < target_date' (lan song 1 do: LATENT, chua ACTIVE — xem DC-01).

**`P11_OVERDUE_SAP_VE`** — `DROP_UNSUPPORTED`  
DROP_UNSUPPORTED — nhan '(sap ve)' KHANG DINH dung dieu ma SYSTEM_PROMPT §5 PHU DINH ('GAN cao KHONG co nghia sap ra') => PRJ_PROMPT_CONTRADICTS trong CUNG MOT prompt. Va no ke NGUOC voi dong lien ke P12 ('HOT BY GAP': gap NGAN => dang nong). Bang chung ngoai mau CO va AM (V11001).

**`P12_HOT_BY_GAP`** — `DROP_UNSUPPORTED`  
DROP_UNSUPPORTED — hai dong LIEN TIEP bao NGUOC nhau voi P11 tren CUNG mot phep do gap. Model chon dong nao la ngau nhien => phep do mat nghia (PRJ_PROMPT_CONTRADICTS).

**`P13_DIGIT_SUM_WINNING`** — `DROP_MODEL_META`  
DROP_MODEL_META — vong lap tu tang cuong: he chon so -> so do thang -> dac trung cua no duoc bom lai vao prompt -> he lai chon so giong the. Nhan '(winning)' doc tu nhien la 'cac ky xo trung'; that ra la 'du doan THANG cua chinh he' (feature_engineering.py:131-135 loc status='WIN' tren bang predictions).

**`P18_KB_PATTERN_DAI`** — `BLOCK_AMBIGUOUS`  
BLOCK_AMBIGUOUS — nguon DONG BANG tu 2026-04-26 00:45:54 (131 ngay truoc ngay do 04/09) nhung VAN DUOC DOC MOI LUOT. Nhan 'gan' noi SAI ve chinh no. Va no MAU THUAN TRUC TIEP voi P17 trong CUNG MOT PROMPT: L494-497 (live) noi Binh Duong DB gan nhat = 58(28/08) 30(21/08) 15(14/08); L512-515 (KB) noi 'DB gan: 50->60->87'. RM-20 nguoc lai: day KHONG phai bang chet — day la NGUON CHET ma VAN DUOC DOC. Nguy hiem hon bang chet. Chi duoc mo lai khi tep duoc sinh lai co neo ngay va co cutoff theo date_str.

**`P19_KB_DOW`** — `BLOCK_AMBIGUOUS`  
BLOCK_AMBIGUOUS — cung tep dong bang voi P18. Cung truc (mien x thu) voi P05 nhung BO SO KHAC HAN => hai cau trong cung prompt bao nguoc nhau.

**`P20_TAN_SUAT_DUOI_5_GIAI`** — `DROP_DUPLICATE`  
DROP_DUPLICATE — lap lai chinh cac dong DB/G8/G7 NGAY PHIA TREN no trong cung prompt, o dang da dem va da cat top-5. Du lieu tho da co san => model tu tinh duoc (NT-03 loi ra thu hai). Bo khoi dem, giu du lieu tho.

**`P22_RULE_TAILS`** — `DROP_DUPLICATE`  
DROP_DUPLICATE — Jaccard 0,846 voi P24 (do 04/09 MN). Va RULEBOOK §11 (gpt_analyzer.py:633-639) ra lenh tuong minh: 'STRONG (>=3 rules): nen co trong top-2' va 'KHONG tu tao so moi neu Rule Tails da co goi y manh' — cau sau CAM model tao so ngoai ro, tuc chan dung dieu muc tieu owner #2 doi hoi. Noi dung con lai da nam trong C-RULE-04.

**`P27_SHADOW_BLOCKS`** — `DROP_DUPLICATE`  
DROP_DUPLICATE — Block 2 la ban rut gon cua P24, in lai lan hai trong cung prompt; Block 1 trung P21; Block 3 da rut danh sach chi con dem. Tieu de khoi tu ghi 'tham khao nhung KHONG thay the evidence tren' (L672) nhung noi dung CHINH LA evidence tren. 5 dong '100.0% (n=2..5)' dat canh nhau, khong nen, khong hieu chinh boi. Giu MOT ban duy nhat: C-RULE-03.

**`P31_PHASE11_MODEL_META`** — `DROP_MODEL_META`  
DROP_MODEL_META — NT-10. DA duoc go o CONTEXT_ONLY_V2 (gate `not _ctx_only` tai gpt_analyzer.py:2990-2991 · 3006), xac nhan tren dump 04/09 vang mat o ca 3 mien. Con lai o regime OFFICIAL_LEGACY => phai go not.

**`P32_PHASE14A_MODEL_RANKING`** — `DROP_MODEL_META`  
DROP_MODEL_META — NT-10. Dong '-> AI nen uu tien patterns tu models co win_rate cao hon' la menh lenh bat chuoc nhau, mau thuan voi chinh RULEBOOK §22/§23 chong bay dan trong CUNG prompt. DA go o CONTEXT_ONLY_V2, con o OFFICIAL_LEGACY.

**`P35_MB_HARD_MODE_MODEL_META`** — `DROP_MODEL_META`  
DROP_MODEL_META — NT-10. Dong 'ML MANH HON AI CHO MB: ... -> Tham khao ML output neu co' vi pham CA NT-10 CA NT-11. Lot luoi vi `_V10768_HERD_SECTION_KEYS` (gpt_analyzer.py:4598) chi 4 chuoi va khop header '### ', con header nay la '### MB HARD MODE'. Do tren dump 04/09: ca ba chuoi 'Best MB model' · 'AI token models 14d' · 'ML/ensemble models 14d' DEU CO MAT trong MB|SHADOW_CONTEXT_ONLY — tuc lane duoc goi la 'ngu canh thuan'.

## 11. MUOI BAY DIEU KIEN SINH RA

Chi tiet day du 24 truong moi dieu kien nam trong `artifacts/v11165_k5_condition_contract.json`. Duoi day la ban tom tat + **gioi han phai doc**.

### `C-RAW-01` — Ket qua ngay truoc — DAY DU dai va giai

| | |
|---|---|
| ho | `RAW` |
| sinh tu | `P16_KET_QUA_NGAY_TRUOC` |
| `evidence_status` | **`RAW_FACT`** |
| `candidate_binding_mode` | `KHONG GAN — model tu doc` |
| `independence_group` | `L1_LOTTERY_EVENTS` |
| `as_of` | date < date_str — DA CO |
| `availability_at_prediction_time` | CO — D-1 luon co truoc cutoff cua moi mien |

**`transform_definition`:** KHONG BIEN DOI. Bo `[:3]` va bo loc 2 giai.

**`observed_value`:** ban than ket qua

**`known_limitations`:**

- Ban hien tai cat khong doi xung (3 dai / 2 giai). Cat la MOT DANG LOC (NT-02). Phai render du, HOAC noi ro da cat bao nhieu va theo tieu chi gi.

### `C-RAW-02` — Lich su dai — cac ky gan nhat, RAW

| | |
|---|---|
| ho | `RAW` |
| sinh tu | `P17_LICH_SU_DAI` |
| `evidence_status` | **`RAW_FACT`** |
| `candidate_binding_mode` | `KHONG GAN` |
| `independence_group` | `L1_LOTTERY_EVENTS` |
| `as_of` | date < date_str — DA CO |
| `availability_at_prediction_time` | CO |

**`transform_definition`:** GIU phan raw. BO phan `top=36(2)` — do la Counter da cat top-3, tuc AGGREGATED_NUMBER_SET tra hinh (NT-02).

**`observed_value`:** ket qua that

**`known_limitations`:**

- Phai loai HAN P18/P19 khoi prompt truoc khi giu khoi nay, neu khong hai khoi noi nguoc nhau ve cung mot dai (do 04/09 MN: L494-497 vs L512-515).

### `C-UNIV-01` — Bang duoi 00-99 — tan suat va khoang vang, DOI XUNG

| | |
|---|---|
| ho | `UNIVERSE` |
| sinh tu | `P01_TOP5_GOI_Y` · `P04_TANG` · `P05_DOW_HAY_RA` |
| `evidence_status` | **`MECHANICALLY_DERIVED`** |
| `candidate_binding_mode` | `FULL_UNIVERSE_SYMMETRIC — moi duoi 00-99 deu co mot dong` |
| `independence_group` | `L1_LOTTERY_EVENTS` |
| `as_of` | date < date_str — DA CO (statistical_analyzer.py:71) |
| `availability_at_prediction_time` | CO |

**`transform_definition`:** KHONG sort · KHONG top-k · KHONG score tong hop · KHONG emoji. Thu tu CO DINH 00->99. Cot la SO DEM tho va co/khong.

**`observed_value`:** dem tho moi duoi

**`known_limitations`:**

- THAY THE ban hien tai cua P01 (top-5 co diem `74.2pt`), P04 (top-5 TANG) va P05 (top-3 theo thu co boost `(+1.4)`) — ba khoi deu cat universe 100 xuong 3-5 va deu xep hang.
- NGAN SACH TOKEN (NT-04, do that): 100 dong x (2 ky tu duoi + m cot) — m=4 cot la 1.200 ky tu, cong tieu de ~1.320. Prompt that 04/09: MN 50.464 / MT 51.487 / MB 55.178 ky tu. Bang doi xung 4 cot ton 2,6% prompt MN. Ba khoi bi thay the dang chiem nhieu hon the.
- Nen T1 do tren W180 ket thuc 2026-09-04: MN 0,4298 · MT 0,3509 · MB 0,2374. RM-21: con so nay chi dung cho thuoc 'duoi co mat trong tap duoi cua mien-ngay', CAM muon sang thuoc khac.

### `C-UNIV-02` — Co dao guong tren toan 00-99

| | |
|---|---|
| ho | `UNIVERSE` |
| sinh tu | `P09_MIRROR_PAIRS` |
| `evidence_status` | **`MECHANICALLY_DERIVED`** |
| `candidate_binding_mode` | `FULL_UNIVERSE_SYMMETRIC (cot boolean trong C-UNIV-01)` |
| `independence_group` | `L1_LOTTERY_EVENTS` |
| `as_of` | theo source_data — DA CO |
| `availability_at_prediction_time` | CO |

**`transform_definition`:** KHONG lay `pairs[:5]`. Ban hien tai phat hien 25 cap roi in 5 — va in HAI LAN o hai dong lien tiep voi hai do dai khac nhau (3 cap va 5 cap).

**`observed_value`:** boolean moi duoi

**`known_limitations`:**

- Nen T5 (ca hai duoi cua mot cap deu co trong ngay) do W180: se in trong bang_nen_do_duoc. Chua co phep do tien nao => evidence_status MECHANICALLY_DERIVED chu KHONG phai PROSPECTIVE_SUPPORTED.

### `C-UNIV-03` — Duoi x giai — bang doi xung, khong xep hang

| | |
|---|---|
| ho | `UNIVERSE` |
| sinh tu | `P14_TOP_POSITIONS` · `P20_TAN_SUAT_DUOI_5_GIAI` |
| `evidence_status` | **`MECHANICALLY_DERIVED`** |
| `candidate_binding_mode` | `FULL_UNIVERSE_SYMMETRIC` |
| `independence_group` | `L1_LOTTERY_EVENTS` |
| `as_of` | date < date_str — DA CO |
| `availability_at_prediction_time` | CO |

**`transform_definition`:** KHONG `top_3[:2]` va KHONG `[:3 giai dau]`. Bo `conc=11%` neu khong kem nen cua chinh truc do.

**`observed_value`:** dem tho

**`known_limitations`:**

- P20 bi gop vao day va BO ban dem rieng: ban hien tai cua P20 lap lai chinh cac dong DB/G8/G7 NGAY PHIA TREN no trong cung prompt.
- Nen T3 (duoi o DB) do W180: MN 0,0312 · MT 0,0241 · MB 0,0100. MB dung 0,01 vi MB chi co MOT dai — day la vi du ro nhat vi sao CAM muon nen giua cac mien (RM-21).

### `C-STAT-01` — Xu huong tan suat — do doc, toan universe

| | |
|---|---|
| ho | `STAT` |
| sinh tu | `P04_TANG` |
| `evidence_status` | **`HYPOTHESIS_ONLY`** |
| `candidate_binding_mode` | `FULL_UNIVERSE_SYMMETRIC` |
| `independence_group` | `L1_LOTTERY_EVENTS` |
| `as_of` | DA CO |
| `availability_at_prediction_time` | CO |

**`transform_definition`:** KHONG lay trending_up[:5]. Cot 'do doc' cho ca 100 duoi trong C-UNIV-01.

**`observed_value`:** do doc moi duoi

**`known_limitations`:**

- evidence_status = HYPOTHESIS_ONLY. Duoc phep xuat hien nhu DU KIEN. CAM dat nhan 'TANG' co ham y du bao, va CAM xep hang theo no.

### `C-STAT-02` — Dong xuat hien cap duoi — kem hieu chinh 4.950 phep so

| | |
|---|---|
| ho | `STAT` |
| sinh tu | `P15_CAP_DOI` |
| `evidence_status` | **`HYPOTHESIS_ONLY`** |
| `candidate_binding_mode` | `CHI duoc trinh khi kem ca ba muc tren; neu khong => DROP` |
| `independence_group` | `L1_LOTTERY_EVENTS` |
| `as_of` | DA CO |
| `availability_at_prediction_time` | CO |

**`transform_definition`:** Ban hien tai quet 4.950 cap roi in top-5 theo tan suat, KHONG hieu chinh. Ban moi PHAI kem: (i) nen T5; (ii) so phep so da quet = 4.950; (iii) nguong sau hieu chinh Bonferroni hoac FDR.

**`observed_value`:** frequency: 41.7 (vi du that 04/09 MN, cap (23,78) count=25)

**`known_limitations`:**

- SYSTEM_PROMPT §5d ra lenh 'Neu co -> secondary_number NEN la so di cung' — tuc bo so nay ep TRUC TIEP vao truong secondary_number cua dau ra. Menh lenh do vi pham NT-07 va PHAI go cung luc, neu khong day van la RECOMMENDATION doi lot CONDITION.

### `C-RULE-01` — Menh de luat — kem nen khop va tach TRONG/NGOAI cua so chon

| | |
|---|---|
| ho | `RULE` |
| sinh tu | `P21_MINED_RULES` |
| `evidence_status` | **`RETROSPECTIVE_ONLY`** |
| `candidate_binding_mode` | `RULE_PROPOSITION — trinh menh de, KHONG trinh danh sach so chot` |
| `independence_group` | `L4_MINED_RULES` |
| `as_of` | BAN HIEN TAI KHONG NEO theo date_str — chi loc `is_active` va tier, khong co dieu kien thoi gian. PHAI them `AND mined_at <= date_str`. |
| `availability_at_prediction_time` | CO cho luat; NHUNG mined_at cua ca 105 luat deu la 2026-08-31T00:30 (rule_version v2026W36) — nghia la moi luot truoc 31/08 la TU CHAM. |

**`transform_definition`:** Ban hien tai: sort theo cumulative_rank_score DESC roi LIMIT 5 tu 105 luat active. Giu duoc, NHUNG phai ghi ro da chon 5 tu bao nhieu va theo tieu chi gi.

**`observed_value`:** hit_any do lai tren clone, W42 ket thuc 04/09: MN 258/281=91,8% · MT 258/306=84,3% · MB 242/374=64,7%

**`known_limitations`:**

- PRJ-SELECTION-WINDOW-001: NGOAI cua so chon chi co n=20/mien tren 4 NGAY (01/09-04/09, ke tu lan dao lai gan nhat). RM-04: n nho la 'CHUA DUOC PHEP KET LUAN', KHONG phai 'yeu'. Diem uoc luong AM o ca ba mien va KTC95 deu chua so 0.
- 2.421/5.035 luot danh gia co rule_id KHONG con trong mined_rules (luat the he truoc da bi xoa) => khong tach duoc trong/ngoai cho nhung luot do. Da tach rieng nhan KHONG_RO_mined_at, khong gop vao ket luan.
- Khoi nay la khoi DUY NHAT trong ~30 khoi co kem NEN va co doan TU PHU DINH (L554-L555 tren dump MN official 04/09). No la KHUON MAU — nhung xem C-RULE-02 va C-RULE-03 de biet doan tu phu dinh do KHONG PHU toi cac dong nguy hiem nhat.

### `C-RULE-02` — Ti le hit_any theo cua so — CAM in tran khong nen

| | |
|---|---|
| ho | `RULE` |
| sinh tu | `P23_EVIDENCE_WINDOWS` |
| `evidence_status` | **`RETROSPECTIVE_ONLY`** |
| `candidate_binding_mode` | `KHONG GAN CANDIDATE — day la chi so ve KHO LUAT, khong phai ve so nao` |
| `independence_group` | `L4_MINED_RULES` |
| `as_of` | date<=date_str — DA CO |
| `availability_at_prediction_time` | CO |

**`transform_definition`:** giu nguyen phep dem, NHUNG bat buoc in kem nen khop va k trung binh.

**`observed_value`:** NGUYEN VAN tren dump 04/09 — MN official L567: 'Windows: 1W(7d):37/42=88% | 2W(14d):75/85=88% | 3W(21d):118/131=90% | 4W(28d):164/182=90% | 5W(35d):215/235=91% | 6W(42d):265/288=92%'; MB official L593: '1W(7d):24/42=57% | ... | 6W(42d):250/384=65%'

**`known_limitations`:**

- 🔴 KHUYET NGHIEM TRONG VE PHAM VI DOAN CANH BAO: doan tu phu dinh (L554-L555) noi 'cac moc HR 4W/12W/16W O TREN' — tuc no chi phu cac dong MINED RULES (L548-L552). Dong Windows (L567) va bang Source-Prize (L569-L586) nam DUOI doan canh bao va KHONG duoc no phu. Chinh 12 dong '100.0%' la cho CAN canh bao nhat lai khong co.
- Cach dem 'it nhat mot trong k duoi' co nen RAT CAO — day dung la dieu L555 canh bao, nhung L555 chi noi ve HR cua luat, khong noi ve dong Windows nay.

### `C-RULE-03` — Nguon x giai — kem nen VA hieu chinh so sanh boi

| | |
|---|---|
| ho | `RULE` |
| sinh tu | `P24_EVIDENCE_SOURCE_PRIZE` · `P27_SHADOW_BLOCKS` |
| `evidence_status` | **`RETROSPECTIVE_ONLY`** |
| `candidate_binding_mode` | `KHONG GAN CANDIDATE` |
| `independence_group` | `L4_MINED_RULES` |
| `as_of` | date>=_dt42 AND date<=date_str — DA CO |
| `availability_at_prediction_time` | CO |

**`transform_definition`:** Ban hien tai: GROUP BY ... HAVING evals>=3 ORDER BY hr DESC LIMIT 10 (+LIMIT 8 theo thu). Ban moi PHAI kem so o da quet va ky vong duoi nen.

**`observed_value`:** NGUYEN VAN dump MN official L569-L586: 12 dong dang '🔥[TOP] MB(D-1/CN) · Thai Binh G1+G7: 6/6=100.0%'

**`known_limitations`:**

- Cau '12 tuan gan nhat trung 12/12 · 16 tuan trung 16/16' (dump MN L695-L699, lap 4 lan) duoi nen khop MN 0,8378 co P=0,1195 moi luat. Voi 105 luat, KY VONG 12,6 luat dat 12/12 hoan toan do may rui. MT: 2,3 luat. MB: 0,0 luat.
- P27 (Block 2) bi DROP_DUPLICATE va gop vao day: no in lai chinh bang nay lan thu hai trong cung prompt, voi n nho hon (n=2..5) va khong nen.

### `C-RULE-04` — Boi canh soi cau — ke su kien nguon, KHONG xep hang

| | |
|---|---|
| ho | `RULE` |
| sinh tu | `P25_BOI_CANH_SOI_CAU` · `P22_RULE_TAILS` |
| `evidence_status` | **`RETROSPECTIVE_ONLY`** |
| `candidate_binding_mode` | `RAW_EVENT_NARRATIVE — model tu rut duoi tu su kien` |
| `independence_group` | `L4_MINED_RULES` |
| `as_of` | bo luat ma dai nguon chua co ket qua — DA CO |
| `availability_at_prediction_time` | CO |

**`transform_definition`:** 🔴 PHAI SUA: ban hien tai thu tu cac cau VAN theo cumulative_rank_score DESC. Doi sang thu tu TRUNG TINH (theo ngay roi theo ten dai, ABC).

**`observed_value`:** NGUYEN VAN dump MN L694: '1) thu Nam 03/09, dai Ha Noi (MB) ra o G7 cac duoi: 08 44 71 73.'

**`known_limitations`:**

- Tieu de tu khai 'KHONG co danh sach so chot san' (L691) — nhung moi cau VAN liet ke duoi tuong minh va thu tu VAN theo xep hang; hop cac cau lai duoc dung bo so cu. V11016 doi HINH THUC, khong doi BAN CHAT. Sua thu tu la dieu kien BAT BUOC de khoi nay hop le.
- Dong 'Luat noi cho nay voi hom nay co ho so: 12 tuan gan nhat trung 12/12 · 16 tuan trung 16/16' duoc lap 4 lan trong mot khoi — do la SO TU CHAM lap lai, xem C-RULE-03.
- P22 (RULE TAILS) bi DROP_DUPLICATE va gop vao day: Jaccard 0,846 voi C-RULE-03.

### `C-RULE-05` — Hoi tu nhieu luat = RUI RO BAY DAN, khong phai tin hieu manh

| | |
|---|---|
| ho | `RULE` |
| sinh tu | `P26_CONVERGENCE_TRAP` |
| `evidence_status` | **`HYPOTHESIS_ONLY`** |
| `candidate_binding_mode` | `CANDIDATE_NEGATIVE — day la bo so de CAN NHAC TRANH, khong phai de chon` |
| `independence_group` | `L4_MINED_RULES` |
| `as_of` | theo date_str — DA CO |
| `availability_at_prediction_time` | CO |

**`transform_definition`:** giu; nhung PHAI dem theo NHOM NGUON DOC LAP, khong dem theo so luat.

**`observed_value`:** dump MN L592-L595: '⛔ 08: CONV×4 — TRAP RISK'

**`known_limitations`:**

- 🔴 Dong L600 'Historical: CONV×3 herding scenarios co win rate THAP HON average' — khong n, khong nen, khong nguon. RM-11 cam dung lam can cu. RULEBOOK §23 muc 8 lap lai y het.
- NT-09: 'CONV×4' dem BON LUAT, ma bon luat do deu thuoc lineage L4_MINED_RULES, va L4 dao ra tu L1. Bon luat cung tro mot duoi KHONG phai bon nguon doc lap. Dump MN L694-L700 cho thay ro: ca 4 su kien deu la 'dai Ha Noi (MB) ngay 03/09' — MOT dai, MOT ngay, bon cach cat giai.
- ✅ DIEU DA DUNG (giu nguyen, lam khuon mau): dump MN L685 'Luu y: duoi duoc nhieu luat cung chi => MOI model cung thay => rui ro bay dan cao hon, khong phai tin hieu manh hon.' Day la NT-09 duoc thi hanh dung o mot cho.

### `C-RULE-06` — Do song cua nguon theo tuan — kem nen, BO menh lenh

| | |
|---|---|
| ho | `RULE` |
| sinh tu | `P30_WEEKDAY_SCAN_LIVINGNESS` |
| `evidence_status` | **`RETROSPECTIVE_ONLY`** |
| `candidate_binding_mode` | `KHONG GAN CANDIDATE` |
| `independence_group` | `L4_MINED_RULES` |
| `as_of` | moc tinh tu date_str — DA CO |
| `availability_at_prediction_time` | CO |

**`transform_definition`:** giu phep dem; BO phan 4 bac va BO toan bo huong dan.

**`observed_value`:** dump MN L649: '🔥 SONG MANH (>=6/8w): MB(D-1/T5) · Ha Noi/G6+G7(8/8), ...'

**`known_limitations`:**

- 🔴 Menh lenh PHAI GO (NT-07), nguyen van dump MN L652-L655: '• SONG MANH -> trong so CAO, uu tien tuyet doi · • SONG YEU -> SUPPORT, dung xac nhan · • SUY GIAM -> canh bao, giam confidence · • CHET -> LOAI khoi reasoning'. Va L980 (RULEBOOK §19) lap lai y het — GO MOT CHO KHONG DU (§60.1).
- 'uu tien tuyet doi' tren mau 2-8 tuan, khong nen, khong hieu chinh boi.
- 🔴 NHAN 'SONG MANH' GAN NHU LA MAC DINH O MN. Tinh duoi nen khop: mot nguon HOAN TOAN KHONG CO TIN HIEU van dat >=6/8 tuan voi xac suat MN 88,5% · MT 65,6% · MB 11,2% (Binomial(8,p), p = nen khop W42 cua mien do). CUNG MOT NGUONG 6/8 mang y nghia khac han o ba mien, ma prompt dung chung mot nguong cho ca ba. O MN, 'SONG MANH' gan nhu khong loai duoc gi; o MB no la nhan hiem.

### `C-RULE-07` — Kho luat MB — kem nen, bo nhan vong doi

| | |
|---|---|
| ho | `RULE` |
| sinh tu | `P34_MB_RULE_STACK_PROD_MANUAL` |
| `evidence_status` | **`RETROSPECTIVE_ONLY`** |
| `candidate_binding_mode` | `RULE_PROPOSITION` |
| `independence_group` | `L5_MB_RULES` |
| `as_of` | snapshot_date moi nhat cua mined_rules_mb_daily — KHONG neo theo date_str. PHAI sua. |
| `availability_at_prediction_time` | CO |

**`transform_definition`:** PRODUCTION top-6 theo mb_rank + MANUAL top-8 — giu, nhung ghi ro chon tu 35 va tu 77.

**`observed_value`:** dump MB official L576-L577: '⚠️ MB(D-1/T5) · Ha Noi: rank=113.40 | legacy=58.00 | 12W=91.7%(L1) | 16W=87.5%(L2) | 4W=100.0%(L3) | READY_WITH_CAUTION | loi the +28.1%/nen (n=51)'

**`known_limitations`:**

- 🔴 MAU THUAN GIO TRONG CUNG PROMPT (PRJ_PROMPT_CONTRADICTS): doctrine ghi 'Thu tu xo: MN(16:10) -> MT(17:10) -> MB(18:15)' trong khi Phase 19 LOP 13 cua CUNG prompt ghi 'MN xo xong 16:36, MT xo xong 17:36, MB xo xong 18:36'. Ca hai deu KHAC moc khoa trong docs/MOC_FINAL_TOTAL_OUTPUT.md (MN 15:40 · MT 16:55 · MB 17:55). BA con so cho MOT dai luong.
- Khoi nay BAT tren OFFICIAL MB qua MB_PROMPT_DOCTRINE_ENABLE=1 trong .env (KHONG co trong /proc/<PID>/environ vi vao qua dotenv). Doc environ cua tien trinh roi ket luan 'doctrine TAT' la do SAI NGUON (RM-13).
- MB-PROD-DYN8W tu khai 'dang DRIVE score o /du-doan official' — tuc cung mot bo luat vua cham diem vua duoc ke lai cho LLM. Do KHONG phai hai nguon (NT-11 mo rong).

### `C-SPEND-01` — Mien ra truoc da ra duoi nao — RAW EVENT, khong xep hang

| | |
|---|---|
| ho | `SPEND` |
| sinh tu | `P28_ANTITRAP_SPEND` · `P29_D1_POOL_COUNT` |
| `evidence_status` | **`HYPOTHESIS_ONLY`** |
| `candidate_binding_mode` | `FULL_UNIVERSE_SYMMETRIC (mot cot boolean trong C-UNIV-01)` |
| `independence_group` | `L1_LOTTERY_EVENTS` |
| `as_of` | CO — chi dua khi ket qua THAT da ton tai truoc cutoff cua mien dich |
| `availability_at_prediction_time` | CO cho MT/MB; KHONG AP DUNG cho MN (MN xo truoc) |

**`transform_definition`:** 🔴 PHAI GO: phan chia FRESH / PARTIAL_SPENT / FULL_SPENT va thu tu theo boost DESC. Chi giu SU KIEN: duoi nao da ra o dau, luc may gio.

**`observed_value`:** dump MN L662-L663: '- D-1 cross-region tail pool: 76 distinct tails' + '- Chua bi tieu o mien ra truoc (du kien, khong phai khuyen nghi): 18 (da tieu: FRESH 0/0 CONV×2, nguon ung ho=3/3 [MN(D-1)+MT(D-1)+MB(D-1)]); ...'

**`known_limitations`:**

- 🔴 NHAN NOI NGUOC VOI NOI DUNG (NT-07): dong tu khai 'du kien, khong phai khuyen nghi' (L663) nhung NAM DONG NGAY DUOI la menh lenh tuong minh, nguyen van L665-L668: 'DECISION RULE: spend count is a SOFT negative prior... The more prior same-day regions already emitted a tail, the LOWER its priority for main_number.' va 'MAIN PICK PRIORITY: prefer tails that are BOTH structurally supported AND less spent... rank by anti-trap purity: FRESH > PARTIAL_SPENT > FULL_SPENT.' Nhan noi khong khuyen nghi, cau ke tiep XEP HANG DE CHON.
- NT-08: FRESH/FULL_SPENT la NHAN GIA THUYET tu gan, chua co phep do tien. Phai go nhan, giu su kien.
- NT-09: 'nguon ung ho=3/3 [MN(D-1)+MT(D-1)+MB(D-1)]' dem BA MIEN nhu ba nguon doc lap. Ba miennay deu thuoc lineage L1 va deu di qua CUNG bo luat L4 de duoc goi la 'ung ho'. Dem 3/3 la dem cung lineage ba lan.
- P29 gop vao day: V11105/FU-419 DA SUA dung huong (bo `sorted(d1_union)[:12]` von luon la 12 duoi NHO NHAT, chi in so dem 76). Day la KHUON MAU DUNG DA CO SAN trong chinh kho nay. Nhung so dem ma khong co duong tra cuu thi model KHONG the dung => xem C-TOOL-01.

### `C-TOOL-01` — Truy van pool duoi D-1 — CAN TOOL THAT, chua co

| | |
|---|---|
| ho | `TOOL` |
| sinh tu | `P29_D1_POOL_COUNT` |
| `evidence_status` | **`UNAVAILABLE`** |
| `candidate_binding_mode` | `REAL_QUERY_TOOL` |
| `independence_group` | `L1_LOTTERY_EVENTS` |
| `as_of` | CO |
| `availability_at_prediction_time` | 🔴 KHONG — chua co tool |

**`transform_definition`:** khong bien doi — day la duong TRA CUU, khong phai khoi van ban

**`observed_value`:** dump MN L662: '- D-1 cross-region tail pool: 76 distinct tails'

**`known_limitations`:**

- 🔴 CHAN CUNG (NT-05): lan song 1 do duoc — grep 5 mau tool-calling tren TOAN BO web/backend = 0 dong. KHONG model nao bat tool calling. Vi vay MOI cau trong prompt bao model 'tu truy van DB' deu KHONG THI HANH DUOC va PHAI BO ngay, truoc khi noi den viec dung tool.
- evidence_status = UNAVAILABLE. Dieu kien nay KHONG duoc phep xuat hien trong prompt cho toi khi co tool that. Day la cho ma muc tieu owner #6 va #7 gap nhau: hoac co tool that, hoac bi loai khoi prompt — khong co lua chon thu ba.
- Cho den khi co tool: hoac (a) render doi xung toan 00-99 mot cot boolean 'co trong pool D-1' trong C-UNIV-01 (ton them 200 ky tu, do duoc), hoac (b) bo han. CAM giu cau so dem tran ma khong cho duong tra.

### `C-SHADOW-01` — Lag-1 spillover tu bundle D-1 — CHI lane shadow, HYPOTHESIS_ONLY

| | |
|---|---|
| ho | `SHADOW` |
| sinh tu | `P33_LANE_TEST_D1_BUNDLE` |
| `evidence_status` | **`HYPOTHESIS_ONLY`** |
| `candidate_binding_mode` | `SHADOW_ONLY — CAM xuat hien o official` |
| `independence_group` | `L3_SYSTEM_OUTPUT` |
| `as_of` | CO cho D-1/D-2 |
| `availability_at_prediction_time` | CO |

**`transform_definition`:** 🔴 giu top-8 tin hieu lag-1 sap theo Δpp DESC — PHAI bo xep hang va PHAI gop 6/8 dong cung ho `predictions_per_model_lag1` lai lam MOT.

**`observed_value`:** '- **D-1 final_bundle** (2026-09-03, MN): BT=`10` status=LOSE lo2=`[10, 15]`' + '- **MN D-2 union pool** ...: 71 [00, 01, 02, ...]' + '• predictions_per_model_lag1 Δpp=15.0 n_lose=50 boost=1.15 (90d)'

**`known_limitations`:**

- 🔴 MAU THUAN NOI TAI CUA THIET KE: day la cho DUY NHAT tim thay co duong bom NGUOC output tang TOTAL (final_bundles) vao dau vao LLM. No CHI o lane shadow — nhung lane shadow chinh la lane duoc goi la 'ngu canh thuan'. Lane sach nhat lai la lane duy nhat an output cua chinh he.
- Menh lenh '-> BT=LOSE uu tien xem nhu lag-1 / cross-spillover candidate trong reasoning' la menh lenh dua tren OUTPUT CUA CHINH HE (NT-07 + NT-11).
- '71 [00, 01, 02, ...]' liet ke tuong minh 71/100 duoi. Liet ke 71% universe roi goi la 'pool' van la AGGREGATED_NUMBER_SET (NT-02).
- evidence_status = HYPOTHESIS_ONLY. Duoc phep TON TAI o lane shadow de DO, nhung CAM dua vao official truoc khi co prospective evidence.

## 12. Dieu DA DUNG SAN trong kho — ba khuon mau, dung dung lai tu dau

Gate nay tim ra ba cho ma chinh kho nay **da lam dung**, va chung la khuon mau cho 17 dieu kien:

1. **Doan tu phu dinh** — dump MN official **L554–L555**: *«cac moc HR 4W/12W/16W o tren deu do TRONG cua so da dao ra chinh cac luat do, nen la diem tu cham. Do tien ngoai cua so hien ngang bang luat gia»* va *«HR dem ‹tuan do co IT NHAT MOT so trung›. Nen cua phep dem ay rat cao»*. Day **dung la** nguyen tac 6.
   🔴 **Nhung pham vi cua no sai:** no noi *«o tren»*, tuc chi phu L548–L552. Dong `Windows:` (L567) va **12 dong `100.0%`** (L569–L586) nam **DUOI** doan canh bao va **khong duoc no phu**. **Cho can canh bao nhat lai khong co.**
2. **Dem hoi tu la RUI RO, khong phai tin hieu** — dump MN **L685**: *«Luu y: duoi duoc nhieu luat cung chi ⇒ MOI model cung thay ⇒ rui ro bay dan cao hon, khong phai tin hieu manh hon.»* Day **dung la** nguyen tac 9.
3. **Bo danh sach thien lech, giu so dem** — `V11105/FU-419` da bo `sorted(d1_union)[:12]` (von **luon la 12 duoi NHO NHAT** — mot thien lech thuan tuy do sap xep) va chi in `76 distinct tails`. Day **dung la** nguyen tac 2. *(Nhung xem `C-TOOL-01`: so dem ma khong co duong tra cuu thi model khong dung duoc.)*

## 13. Nhung dieu ban nay KHONG chung minh duoc

| dieu | trang thai |
|---|---|
| Bo bot bo so lam **tang do trung** | **CHUA DO** — muc tieu owner #9 doi do tien; khong co phep do nao trong gate nay |
| Luat co hieu qua **ngoai** cua so chon | **CHUA DUOC PHEP KET LUAN** — n=20/mien tren 4 ngay (`RM-04`) |
| 17 dieu kien nay **hop le hon** ban hien tai | **CHUA DO** — moi la thiet ke tren giay, chua co ban chay |
| Danh sach 35 producer **da du** | **KHONG CHAC** — lan song 1 ghi `DC-03` pham vi chua phu; `P34` da bi bo sot mot vong vi gate nam trong `.env` |
| 3-cang sach | **CHUA KIEM** trong gate nay (NT-12 = 0 vi khong co du lieu, khong phai vi da dat) |

## 14. Thu tu thi hanh — cai gi phai di truoc

Ba dieu duoi day **phai xong truoc** khi bat ky phep do «ngu canh thuan» nao co nghia. Neu do truoc khi sua, ta lai do mot thay doi **lam nua voi** — dung loi `§60.1` da mac o V11001.

1. 🔴 **Sua THUOC truoc khi do.** Lan song 1 do duoc: van tay `runtime_prompt_sha256` chi phu **39,81–48,07%** payload (tb 43,59%), bat **2/11** phep dot bien; bo 5 dau o nhiem (`_dau_o_nhiem` gpt_analyzer.py:6712) bao **0/5 «sach»** trong khi payload that con `weight=` (33/33 luot) va `Best MB model` (11/33). **Cong mu thi moi ket luan sau do vo nghia.**
2. 🔴 **Go menh lenh cung luc voi go du lieu.** Bang o muc 10 cho thay **13/35** producer di kem menh lenh (`NT-07`). Go so ma giu menh lenh trỏ vao no la `A58_VIOLATION_HALF_DONE` — dung loi V11001 da mac.
3. 🔴 **Bo moi cau bao model «tu truy van»** truoc khi noi den tool. Lan song 1 do: **0 dong** tool-calling tren toan `web/backend`. Moi menh lenh «tu truy van DB» hien la **khong thi hanh duoc** (`NT-05`).

---

**Artifact:** `/root/Lottery_AI_Test/artifacts/v11165_k5_condition_contract.json` · `v11165_k5_baseline.json` · `v11165_k5_nen_khop.json` · `v11165_k5_boi.json` · `v11165_k5_k_va_khoi.json` · `v11165_k5_minedat.json`

**TanPhatAI can lam:** cap nhat so `FOLLOW_UP_TRACKER` cho ba viec chan o muc 14 (sua van tay prompt · go menh lenh cung luc voi go du lieu · bo cau «tu truy van» khi khong co tool); theo doi rang **khong dieu kien nao trong 17 dieu kien dat `PROSPECTIVE_SUPPORTED`**, nen moi de xuat «bat» bat ky dieu kien nao vao official deu phai qua do tien truoc. Phien nay **code KHONG di truoc tai lieu** — khong sua mot dong ma nao dang serve, chi doc clone bat bien va ghi artifact moi.
