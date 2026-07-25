# ADDENDUM V10856 (26/07 02:55→03:1x) — CSS NHẤT QUÁN CARD/CHỮ + SỔ TỔNG HỢP VẤN ĐỀ DỰ ĐOÁN

Owner: "card có cái dài ngắn đủ kiểu, chữ rơi rớt xuống dòng, chưa chuẩn chỉnh nhất quán" + "tổng hợp toàn bộ các vấn đề về dự đoán đừng để trôi".

## 1. CSS nhất quán (deploy md5 14/14, marker đo lường nguyên, hệ 11/11)

- Card trong lưới: **cao đều theo hàng** (stretch + flex column, phần cuối card dồn đáy) + được phép co (`min-width:0` — hết tràn ngang).
- Chữ/token dài (tên method/model): **gãy dòng gọn trong khung** (`overflow-wrap:anywhere` cho heading/card/bảng/ref/warn-strip); badge không tràn; hàng nhãn–giá trị có gap, giá trị dồn phải.
- Phần tinh chỉnh từng màn hình cụ thể: chờ mắt owner + ảnh chụp trong đợt Plan giao diện (đã có backlog UI-audit V10855).

## 2. Sổ tổng hợp dự đoán — `docs/TONG_HOP_VAN_DE_DU_DOAN_20260726.md`

| Nhóm | Nội dung chính |
|---|---|
| A. Chờ đọc theo lịch | A1 M2s promote **28/07** (+9.5pp qua 25/07; ngưỡng +5pp n≥30) · A2 PB-18.1 trial 28/07 · A3 rule-cond skim 28/07 + ngưỡng 04–11/08 (selector thoái hoá H-A4a∧H-B2a 75/75) · A4 what-if /choi MB **~01/08** (day-1 thuận: laneV2/V3 05✓, /choi gate) · A5 lean roster 28/07 |
| B. Theo dõi hằng ngày | Verdict động /choi (7d) · AE-MB no-edge (chờ A4) · AE-MT giữ (54.5%) · MT provider 500 watch 26/07 · MB-ML trũng 35% · đồng-thuận-sai → catalog · MN T7 = design |
| C. Hạ tầng học tập | Retrain CN 26/07 **12/12 OK** · optimizer verify sáng 26/07 · miner T2 28/07 · chuỗi tối đủ · self-check/contract/drift PASS |
| D. Nguyên tắc khoá | Không sửa official giữa trial; ngưỡng + chữ ký + 1 quyết định; anti-herd giữ hygiene; /choi luôn hiển thị số + cảnh báo; bucket-first; không git-pull VPS |
| E. Đã đóng | V10809 per-số · Qwen revert · V10841 live-verify 3/3 · drift audit · MB gate-block hiển thị |

Playbook §5 đã thêm mốc: 26/07 optimizer · **28/07 ĐỌC LỚN** · ~01/08 what-if. Git private `df561ae`.
