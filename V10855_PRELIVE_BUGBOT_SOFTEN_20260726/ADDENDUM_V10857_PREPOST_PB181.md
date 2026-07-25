# ADDENDUM V10857 (26/07 03:41) — ĐO PRE/POST PB-18.1: ĐƠN MODEL + OFFICIAL ĐỀU TĂNG MẠNH

Owner hỏi: "25/07 thế nào? official khá đúng không? đơn model khá hơn chưa từ thay đổi lớn? total có gì mới? sẵn sàng chưa?"

## Pre/post thay đổi lớn (08–17/07 PB-18.0 vs 18–25/07 PB-18.1)

| Thước | PRE | POST | Δ |
|---|---|---|---|
| LLM any-hit | 48.6% (102/210) | **66.9% (111/166)** | **+18.3pp** |
| ML any-hit | 49.2% (118/240) | **57.3% (110/192)** | +8.1pp |
| LLM tại MB | 41% | 62% | +21pp |
| LLM tại MT | 40% | 63% | +23pp |
| LLM tại MN | 64% | 75% | +11pp |
| **Official bundle BT gộp** | 20.0% (6/30) | **41.7% (10/24)** | **hơn gấp đôi** |

- 13/15 model TĂNG: gemini-2.5-flash +39.2pp (→79.2%) · gpt-5-mini +28.6 · xgboost +20 · gemini-2.5-pro +19.2 · lstm/smart-ml +15 · deepseek/sonnet +13.3. Đi ngang: meta-learning. **Giảm duy nhất: random-forest −11.7pp** → watch lean 28/07.
- 25/07: official 2/3 BT (MT 02✓ · MB 05✓ · MN 92✗); laneV2 MB [05,28] trúng cả 2 (28=đề); laneV3 MN 04✓ khi official trượt.
- Total mới đang xếp hàng đúng kỷ luật: M2s +9.5pp forward → đọc promote 28/07; điều kiện V3/rule-cond + what-if /choi MB (~01/08).
- Sẵn sàng: retrain CN 12/12 OK + optimizer xong 03:14 (marker) + self-check 11/11 + Bugbot 0 finding + UI dịu/nhất quán + sổ chống trôi. Git `ad356f8`.
