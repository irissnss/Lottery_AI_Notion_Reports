# V106.38-R8C — PHASE 0 VERIFY ĐẦY ĐỦ (GATE TRƯỚC PHASE 1) — PUBLIC-SAFE

> Public-safe. Không code riêng, dòng DB thô, API key, IP/đường dẫn server.
> Không claim *_FIXED / PROMOTED. Read-only. 0 thay đổi production. AI vẫn chạy.

- **Auditor**: Opus 4.7 | 2026-05-29
- **Tham chiếu**: cha `V106_38R8_..._PUBLIC_SAFE` (tổng truth); `V106_38R8B_PHASE0_STANDARDIZATION_DEPENDENCY_PUBLIC_SAFE` (Phase 0 + dependency).
- Trả lời 3 chỉ đạo: (1) làm rõ model — chưa gộp; (2) bản đồ đài × thứ đầy đủ; (3) verify trước gộp/xóa.

---

## 1. MODEL AI — LÀM RÕ (CHƯA GỘP)

Registry 41 model | DB 2026 có 48 model.

- **Đang chạy (28)**: 9 TOKEN output-eligible + 12 TOKEN shadow + 7 ML local free.
- **Đã loại / idle (13)**: status REMOVED, last seen ~April (minimax, nemotron, mistral-nemo, kimi-k2.6, arcee, llama-4, mistral-large-3, o3-deep-research, cohere-rerank...).
- **Orphan lịch sử (13)**: chạy Feb-Mar rồi bỏ, không còn trong registry (gpt-3.5/4o-mini/4.1/5.1/5.2, deepseek-chat, gemini-2.0-flash, claude-3-haiku, ensemble-2/3models, o4-mini...).
- **Key dùng chung theo provider**: google(5) · openrouter(21) · deepseek(3) · anthropic(2) · openai(2) · local(7, free).

**Đề xuất**: KHÔNG gộp tên/giá trị model. Registry (41) là SSOT định danh. Orphan/removed (26 tên) chỉ là dữ liệu lịch sử → giữ nguyên row cũ, không dùng để dự đoán nữa. Chỉ thống nhất TÊN CỘT `ai_model` qua VIEW, KHÔNG đổi tên model.

---

## 2. BẢN ĐỒ ĐÀI × THỨ ĐẦY ĐỦ (verified)

### MN
| Thứ | Đài |
|---|---|
| T2 | Cà Mau, **HCM**, Đồng Tháp |
| T3 | Bạc Liêu, Bến Tre, Vũng Tàu |
| T4 | Cần Thơ, Sóc Trăng, Đồng Nai |
| T5 | An Giang, Bình Thuận, Tây Ninh |
| T6 | Bình Dương, Trà Vinh, Vĩnh Long |
| T7 | Bình Phước, **HCM**, Hậu Giang, Long An |
| CN | Kiên Giang, Tiền Giang, Đà Lạt |

**⚠️ ĐÍNH CHÍNH theo DỮ LIỆU**: HCM (MN) chạy **T2 + T7 (Thứ Bảy)**, KHÔNG có Chủ Nhật trong ~10 tháng dữ liệu. CN của MN là Kiên Giang/Tiền Giang/Đà Lạt. Nếu là lịch cũ/khác, chủ hệ thống xác nhận giúp.

### MT
| Thứ | Đài |
|---|---|
| T2 | Phú Yên, **Thừa Thiên Huế** |
| T3 | Quảng Nam, Đắk Lắk |
| T4 | Khánh Hòa, Đà Nẵng |
| T5 | Bình Định, Quảng Bình, Quảng Trị |
| T6 | Gia Lai, Ninh Thuận |
| T7 | Quảng Ngãi, Đà Nẵng, Đắk Nông |
| CN | Khánh Hòa, Kon Tum, **Thừa Thiên Huế** |

Multi-thứ: Thừa Thiên Huế (T2,CN) · Đà Nẵng (T4,T7) · Khánh Hòa (T4,CN).

### MB
| T2 Hà Nội · T3 Quảng Ninh · T4 Bắc Ninh · T5 Hà Nội · T6 Hải Phòng · T7 Nam Định · CN Thái Bình |
Multi-thứ: Hà Nội (T2, T5).

### Quy ước per-slice
- 1 đài nhiều thứ = ô RIÊNG: `HCM-T2` ≠ `HCM-T7`; `Hà Nội-T2` ≠ `Hà Nội-T5`; `Thừa Thiên Huế-T2` ≠ `Thừa Thiên Huế-CN`.
- Tên canonical: **Thừa Thiên Huế** (gộp Huế), **Đắk Lắk** (gộp Đắc Lắc), **Đắk Nông** (gộp Đắc Nông), **HCM** (gộp TP. HCM).

---

## 3. VERIFY 4 CẶP "TRÙNG" — CHỈ 1 LÀ DUP THẬT

| Cặp | Quan hệ thật (verified) | Hành động đúng |
|---|---|---|
| experimental_preview_shadow ↔ mb_experimental_preview_shadow | A=3 miền(1893); B=CHỈ MB(203) | B là partition MB → verify row rồi fold, KHÔNG gộp mù |
| v101_region_source_pool_shadow ↔ v101_mn_cross_region_rule_shadow | A=3 miền(10170); B=CHỈ MN(3390 cùng date) | B là bản sao MN của A → verify rồi bỏ |
| tier2_replay_v2_shadow ↔ tier2_replay_shadow | v2(558 mới) vs v1(192 cũ) | cặp version → giữ v2, archive v1 |
| ai_prompt_context_audit_shadow ↔ ai_region_specialist_prompt_shadow_results | schema+row+region+date Y HỆT (75/75) | **DUP THẬT** → verify row rồi gộp 1 |

→ Chỉ **1 cặp là dup thật**; 2 cặp region-subset, 1 cặp version → "gộp" phải verify row-level, không làm mù.

---

## 4. rule_features — AN TOÀN XÓA
rows=0, code_refs=0 → SAFE sau backup. ✅

---

## 5. GATE QUA PHASE 1
- Model: rõ, không gộp ✅
- Station matrix: đầy đủ, verified ✅ (chờ xác nhận HCM T2/T7)
- rule_features: verified SAFE ✅
- Gộp 4 cặp: cần thêm 1 bước verify row-level (3/4 là subset/version) ⚠️
- Tên cột canonical: chờ chủ hệ thống duyệt → rồi làm VIEW (Phase 1)

**An toàn**: 0 production mutation, read-only. Gộp/xóa thật chỉ khi duyệt + backup + chỉ đổi cấu trúc không đổi SỐ.
