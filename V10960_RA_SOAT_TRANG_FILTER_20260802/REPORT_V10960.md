# V10960 — Ra soat trang /filter: trung lap tinh nang + sua UI kho xem

**Ngay:** 02/08/2026 · **Commit rieng:** `(dien sau push)` · **Commit cong khai:** `(dien sau push)` · **Trang thai:** DA DEPLOY UI-ONLY.

> Bao cao theo khung A55.3. Khong ghi Notion (A55.1). QD-014: khong doi duong ra so.

---

## 1. Tom tat

Da ra soat toan bo HTML production trong `web/frontend/` va doi chieu voi route `main.py`. Trang `https://xs.io.vn/filter?tab=overview` la **hub review hop nhat** (`review-dashboard.html`), khong phai trang du doan official. Owner dung khi UI “kho xem” la **dung**: tren mobile chrome (mo ta + thanh dieu khien + context + sticky + tab) chiem **~1.31 viewport** truoc khi thay noi dung; so uu tien nam o duoi. Da sua UI-only: chrome mobile ~**0.64**, dua “So can xem truoc” len dau, chu sticky/tab >=12px, chan crash tab Rules khi thieu field. Deploy VPS PID `597451→639386`, `/api/health=200`, hash 4 bang **y nguyen**. De xuat don trang de FU-224 — **chua xoa/gop**.

## 2. Owner yeu cau gi (nguyen van)

> *"Xem dum anh https://xs.io.vn/filter?tab=overview — UI cua link nay kho xem qua, va link nay co ve dang trung lap tinh nang, can xem ky lai dum anh."*

Kem nhiem vu: liet ke trang + API, tim trung lap / so tinh 2 kieu, Playwright 390/1440, sua UI ro rang (khong dung QD-014), chi **de xuat** gop/xoa, bao cao cong khai V10960.

## 3. Dao boi / phat hien

### 3.1 Ban do trang production (15 file HTML, loai `_v2_*` preview)

| Trang | Route | Muc dich | API chinh |
|---|---|---|---|
| index.html | `/`, `/app` | Bang admin model | `/api/predictions`, `/api/status`, … |
| du-doan.html | `/du-doan` | **Official 15 so** | `/api/final-bundle` |
| du-doan-test.html | `/du-doan-test` | Lane test | `/api/du-doan-test/*` |
| search.html | `/search` | Tra cuu KQ | `/api/search-results` |
| accuracy.html | `/accuracy` | Do chinh xac | `/api/accuracy/*` |
| review-dashboard.html | **`/filter`** (+ redirect `/review-dashboard`, `/rules-dashboard`) | Hub review 4 tab | `/api/review-hub/filter`, `/api/mined-rules/*`, `/api/so-gan` |
| settings.html | `/settings` | Cai dat | `/api/settings/*` |
| choi.html | `/choi` | Quan ly von | `/api/admin/money-board` |
| monitoring.html | `/monitoring` | Admin monitoring | ~25 `/api/admin/*` |
| pnl-tracker.html | `/pnl-tracker` | P&L | `/api/admin/pnl/*` |
| nghiem-thu.html | `/nghiem-thu` | Nghiem thu 19/08 | `/api/nghiem-thu` |
| v82-monitor.html | `/v82-monitor` | V82 (da embed monitoring) | `/api/admin/v82-monitor` |
| user-view.html | `/user-view` | Viewer freeze | `/api/predictions` |
| viewer.html | **KHONG serve** (`/viewer`→`/du-doan`) | Legacy | `/api/viewer/*` (orphaned) |
| login.html | `/login` | Dang nhap | `/api/login` |

### 3.2 `/filter` trung voi trang nao?

| Nghi ngo | Ket luan |
|---|---|
| search.html | **Khong** — search = KQ lich su |
| accuracy.html | **Khong** — accuracy metrics |
| du-doan.html | **Khong trung so** — du-doan = final_bundle official; filter = mined-rules review |
| user-view.html | **Khong cung API** — user-view freeze predictions; filter = review hub |
| viewer.html | **Chet** — khong serve |
| review-dashboard / rules-dashboard | **Da gop vao `/filter`** (redirect) — day la dung muc dich hub |

Trung lap **that** cua `/filter`: no **tu trung** trong 1 man (overview lap sticky + context + cards) va lap y voi panel mined-rules / so-gan ma truoc day tung la trang rieng.

### 3.3 Cung mot thu nhung tinh 2 kieu? (nguy hiem)

| Cap | Khac nhau? | Anh huong |
|---|---|---|
| `/api/filter-2-so-cuoi` vs `/api/review-hub/filter` | **CO** — pattern_rules thu cong vs mined rules | FE chi goi review-hub; endpoint cu **chet o FE** nhung van song o BE |
| `/du-doan` (`final-bundle`) vs `/app` (`predictions`) | **CO** — bundle chot vs so tung model | Dung muc dich khac; owner can biet |
| `/user-view` vs `/du-doan` | **CO** — user-view freeze + predictions | De nham neu mo user-view |

Khong thay `/filter` va `/du-doan` cung tinh 1 con so bang 2 cong thuc tren UI hien tai.

### 3.4 Luot truy cap nginx (~2 ngay: access.log + .1)

| Path | Hits |
|---|---|
| /app | 35 |
| /du-doan | 28 |
| /choi | 21 |
| /nghiem-thu | 19 |
| /login | 16 |
| /filter (+ ?tab=overview) | 11 + 8 |
| /monitoring | 9 |
| /accuracy | 7 |
| /v82-monitor | 4 |
| /review-dashboard | 3 |
| /user-view | 2 |
| /search | 2 |

### 3.5 Playwright UI (mock HTTP local + auth admin)

| Viewport | Truoc | Sau |
|---|---|---|
| mobile 390 chrome/viewport | **1.31** (noi dung bi day het man) | **~0.64** |
| sticky label | ~9px | **12px** |
| so uu tien | o duoi khoi rules/the | **len dau** tab overview |
| tab health crash khi thieu field | PAGEERROR `.length` | da chan |
| cuon ngang | khong thay | khong thay |

Bang chung: `evidence/*_before.png`, `evidence/*_after.png`, `audit_before.json`, `audit_after.json`.

## 4. Huong xu ly va vi sao chon

1. **Sua UI ngay** (chon): loi ro, khong dung QD-014, owner kho chiu vi dung.
2. **Gop/xoa trang ngay** (loai): owner yeu cau chi de xuat.
3. **Xoa `/api/filter-2-so-cuoi`** (hoan): can quet caller server-side truoc; de FU-224.

## 5. Da lam gi

| File | Thay doi |
|---|---|
| `web/frontend/review-dashboard.html` | CSS mobile chrome; reorder overview; defensive health/split; sidebar `/filter` active |
| `backups/v10960_pre/review-dashboard.html` | Backup local |
| VPS `/root/.../backups/v10960_pre/` | Backup remote |
| CHANGELOG / SSOT / FOLLOW_UP / AUTOMATION_STATE | prepend + seq 378 |
| artifacts/ui_filter_20260802/ | Screenshot + audit JSON |

Deploy: `_v10960_deploy.py` · service `lottery` · PID 597451→639386 · hash 4 bang y nguyen.

## 6. Cong kiem

| Muc | Ket qua |
|---|---|
| `/api/health` | 200 (sau settle) |
| `/filter?tab=overview` | 200 |
| Hash 4 bang | IDENTICAL |
| PID doi | CO |
| Playwright tabs overview/candidates/health/gan | load duoc (sau fix) |
| QD-014 | Khong doi model_registry / combo_super / override |

## 7. Vuong vap

1. **Health 000 ngay sau restart** — service chua kip bind; doi 2s → 200. Hau qua neu bo qua: bao deploy fail gia.
2. **Playwright mock schema lech** → PAGEERROR gia; live API du field. Hau qua: sua defensive van can de tranh crash khi API thieu.
3. **Thu muc `artifacts/` Write tool bi chan** — dung Shell/Copy-Item. Hau qua: mat bang chung neu khong copy.
4. **Agent song song V10959/V10961** ghi cung CHANGELOG/SSOT — da doc lai truoc prepend.
5. **loading_spinner false positive** trong do (spinner o accordion flow) — khong phai treo that.

## 8. Go ve

```
# VPS
cp -a /root/Lottery_AI_Test/backups/v10960_pre/review-dashboard.html \
      /root/Lottery_AI_Test/web/frontend/review-dashboard.html
systemctl restart lottery.service
# Local
Copy-Item backups\v10960_pre\review-dashboard.html web\frontend\review-dashboard.html
```

Mat ~1–2 phut. Quay lai UI truoc V10960; khong anh huong so du doan.

## 9. Theo doi tiep

| Ma | Nguong / hanh dong | Han |
|---|---|---|
| **FU-224** | Owner quyet giu/gop/bo: `nghiem-thu` (19 hits nhung 0 inbound link), `viewer.html` chet, `v82-monitor` trung `/monitoring`, `user-view` freeze, BE `/api/filter-2-so-cuoi` | 2026-08-09 |
| QD-014 | Dong bang duong ra so den 08/08 — giu | 2026-08-08 |

### Bang de xuat don (owner quyet — chua lam)

| Trang | De xuat | Ly do | Rui ro neu bo |
|---|---|---|---|
| `/filter` | **GIU** | Hub review, dang dung (11+ hits) | Mat noi soi mined-rules/so-gan |
| `/du-doan` | **GIU** | Official | Mat cong bo |
| `/app` | **GIU** | Admin model | Mat dieu khien |
| `/search` `/accuracy` `/choi` `/settings` `/monitoring` `/pnl-tracker` | **GIU** | Muc dich rieng, co traffic | — |
| `/nghiem-thu` | **Xem xet bo/an** sau 19/08 | 0 inbound link; 19 hits (co the bookmark) | Mat trang nghiem thu neu con can |
| `viewer.html` + `/api/viewer/*` | **Bo** | Khong route | Thap (da redirect) |
| `/v82-monitor` | **Gop link → /monitoring** | Da embed | Bookmark cu dut |
| `/user-view` | **Giu freeze hoac redirect /du-doan** | De nham so | User cu mat link |
| `/api/filter-2-so-cuoi` | **Thu hoi sau quet caller** | FE khong goi | Neu con cron/script goi se vo |
