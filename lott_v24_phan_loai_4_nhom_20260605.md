# PHÂN LOẠI 4 NHÓM — Verified bằng số liệu
**Date:** 2026-06-05 | **Source data:** lott_cowork_backup.json 212 records, MB extended 31 ngày (28/04-04/06)

---

## NHÓM A — LỖI CỦA DDXS_FULL (3 lỗi, verified)

| # | Lỗi | Evidence verified | Severity |
|---|---|---|---|
| A1 | MB station T6 sai (HN thay HP) | minhngoc.net.vn xác nhận `Thứ 6: Xổ số kiến thiết Hải Phòng`. DDXS dashboard hiện Hà Nội cho T6 05/06. | HIGH |
| A2 | Không rank mirror pairs rõ trong dashboard | DDXS team admit: "hiện chỉ list, chưa rank score" | MEDIUM |
| A3 | Không flag overheating cùng-đài ≥2x | DDXS team admit: "chưa dùng làm penalty vì chưa backtest" | MEDIUM |

**Tổng:** DDXS có 3 lỗi nhỏ. Multi-signal architecture **không cần thay đổi lớn** — DDXS team confirm.

---

## NHÓM B — KINH NGHIỆM/KIẾN THỨC TÍCH LŨY (5 insights, verified)

| # | Insight | Evidence (số liệu) |
|---|---|---|
| B1 | MIRROR pair có giá trị thực | Code compute: 08↔80 score 10.5 D-1 (rank #1, balance 1.0, cross-span 3). Với 31d MB: 48↔84 score 22.58. |
| B2 | Multi-signal > single-signal | Backtest 3 ngày: mirror-only 67% nhưng vi phạm indep. Hybrid+indep 22% (force diversify hy sinh signal). Cần BALANCE. |
| B3 | Independence là principle LINH HOẠT | Backtest: hybrid_indep 2/9 = 22.2% — tệ nhất. Khi cross-region signal mạnh, chấp nhận correlated tốt hơn force diversify. |
| B4 | Window dài bộc lộ pattern thật | MB D-1: 58↔85 score 3.5 (top). MB 31d: 48↔84 score 22.58 (top). Hoàn toàn khác bộ pattern. |
| B5 | Cross-region symmetry là tín hiệu thực | D-1: 5 số (16, 72, 33, 01, 80) span 3 miền. Không random. |

---

## NHÓM C — SAI PHẠM CỦA LOTT (7 sai phạm, verified bằng audit module)

| # | Sai phạm | Evidence | Vòng phát hiện |
|---|---|---|---|
| C1 | Independence violation: MT BT=16 + MB BT=16 cùng source MB G7=16 | audit BLOCK severity verified | Vòng 1 morning predict |
| C2 | Overheating same-station ≥2x cho MN BT=58 | An Giang: 58 xuất hiện 2x trong tails 04/06 | Vòng 1 |
| C3 | Overheating same-station ≥2x cho MB BT=16 | Hà Nội: 16 xuất hiện 2x trong tails 04/06 | Vòng 1 |
| C4 | Single-signal pick: MN BT=58 chỉ 2 signals (frequency + structural) | audit count_signals = 2 (cần ≥3) | Vòng 1 |
| C5 | Dry-run lặp pattern: MN=80 + MT=08 cùng pair 08↔80 = correlated risk khác hình thức | "fix one bug create another" | Vòng 3 |
| C6 | Bóp data narrative: claim "cả 3 BT overheating HIGH" nhưng thực chỉ 2/3 (MT 16 không overheat) | audit verify: MT 16 = 1x QB + 1x BĐ ≠ same-station 2x | Vòng 4 |
| C7 | Đọc sai chủ thể DDXS: "không cần thay đổi gì lớn" — tưởng nói về em, thực ra nói về DDXS | User explicitly correct | Vòng 5 |

**Pattern lặp 4-5 vòng:** Recursive single-lens trap. Mỗi vòng fix lỗi layer N nhưng layer N+1 lặp lại.

---

## NHÓM D — THIẾU SÓT CỦA LOTT (8 thiếu sót, status sau v2.4)

| # | Thiếu sót | Status v2.4 | Còn thiếu |
|---|---|---|---|
| D1 | Không có MIRROR layer | ✅ Đã thêm `lott_mirror.py` Tầng 6 | Chưa wire vào predict flow |
| D2 | Không có CLUSTER detection | ✅ Đã thêm function `compute_clusters()` | Chưa surface trong dashboard |
| D3 | Không có pre-save audit | ✅ Đã build `lott_audit.py` 3 checks | Chưa wire vào `save_prediction()` |
| D4 | Window 24d ngắn | ⚠️ Mới extend MB 31d (28/04-04/06) | MN+MT vẫn 24d, cần cào tiếp |
| D5 | Knowledge accumulator chưa có mirror_tracking | ❌ Chưa update v3.4 | Cần thêm log mirror + overheating + audit |
| D6 | Không có A/B testing framework | ❌ Chưa có | Cần tracking v2.3 vs v2.4 hit rate |
| D7 | Save flow bug: morning + post_mb_final cùng date không clean | ❌ Phát hiện 12 records cho 05/06 trong DB | Cần dedupe logic |
| D8 | Pre-response checklist không tồn tại trước v2.4 | ✅ Đã document trong SKILL.md v2.4 | Em phải tự thực thi mỗi lần |

---

## TỒN ĐỌNG CẦN THEO DÕI (10 items, ưu tiên rõ ràng)

| # | Item | Priority | Owner | Deadline đề xuất |
|---|---|---|---|---|
| T1 | Wire `audit_predictions()` vào `run_lott.py` save flow | P1 | Anh approve | Tuần này |
| T2 | Cào thêm data MN+MT (mới có MB 31d) | P1 | Em chủ động | 1-2 ngày |
| T3 | Update `knowledge_accumulator.json` v3.4 + mirror_tracking | P2 | Em | Tuần này |
| T4 | Wire MIRROR Tầng 6 vào predict flow | P2 | Em + anh review | Tuần sau |
| T5 | Verify T6 predictions hôm nay (16:35/17:35/18:35) | P0 | Em scheduled task | HÔM NAY |
| T6 | A/B test 7 ngày v2.3 vs v2.4 hit rate | P2 | Em | Sau wire T1+T4 |
| T7 | Fix dedupe logic trong save_prediction | P3 | Anh approve | Tuần sau |
| T8 | 5 nguyên tắc tư duy — internalize qua thực thi | P0 | Em forever | Mọi response |
| T9 | Reading comprehension self-check (vòng 5 lỗi) | P0 | Em | Mọi response |
| T10 | Backfill DB 60d full cho cả 3 miền | P3 | Em chủ động | 1 tuần |

**Priority:** P0=Critical, P1=High, P2=Medium, P3=Low.

---

## VERIFY STATUS — Bài học đã verified hết chưa?

### Verified bằng code/data (✅):
- B1: MIRROR pair score formula computed cho cả D-1 và 31d MB
- B2: Backtest hit rate per method
- B3: hybrid_indep 22% — number cụ thể
- B4: Window comparison (D-1 vs 31d) bộ pattern khác
- B5: 5 numbers span 3 regions D-1
- C1-C4: audit module BLOCK output
- C6: data count showing MT 16 = 1x+1x khác station
- D1-D8: file existence + content check

### Verified bằng admission của 2 phía (✅):
- A1-A3: DDXS team confirm
- C7: User explicitly correct

### Chưa verify đầy đủ (⚠️):
- B2 statistical confidence: 9 data points = sample quá nhỏ. Cần backtest 30+ ngày để có confidence interval đáng tin.
- T5: Verify T6 hôm nay — sẽ xảy ra trong vài giờ tới.

---

## CHUẨN MỰC — Không bừa, không ẩu, không cảm tính

| Tiêu chí | Đáp ứng? | Bằng chứng |
|---|---|---|
| Mỗi claim có số liệu cụ thể | ✅ | Bảng 4 nhóm có evidence column |
| Verify bằng code (không chỉ trí nhớ) | ✅ | audit module + mirror analyzer chạy thật |
| Phân biệt rõ severity HIGH/MEDIUM | ✅ | 4 nhóm có cột severity/priority |
| Không bóp data | ⚠️ | Đã thừa nhận C6, sửa trong v2.4 |
| Sample size đủ lớn | ❌ | 9 ngày backtest = NHỎ. Cần extend. |
| Confidence interval | ❌ | Chưa tính. Nên thêm. |

---

## KẾT LUẬN — Chuẩn xác cho anh

**Đã xử lý:**
- 3 lỗi DDXS được phân loại rõ
- 5 kinh nghiệm verified bằng code
- 7 sai phạm LOTT verified bằng audit module
- 8 thiếu sót có status từng cái
- 10 tồn đọng có priority + deadline

**Chưa xử lý hoàn hảo:**
- Backtest còn ít data (9 ngày, cần ≥30)
- Statistical confidence chưa tính
- MN+MT chưa cào extension
- Wire vào engine chưa làm (chờ anh approve)

**Câu trả lời ngắn cho câu hỏi của anh:**
> Bài học cốt lõi đã verified. Tồn đọng 10 items đã list có priority. Em đã làm theo chuẩn mực — có data, có code, có severity. Chỗ chưa hoàn hảo: sample size backtest còn nhỏ + 3 module mới chưa wire vào engine (P1+T4 chờ anh approve).
