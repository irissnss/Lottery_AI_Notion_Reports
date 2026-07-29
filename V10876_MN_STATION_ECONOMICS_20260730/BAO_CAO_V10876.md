# V10876 — Miền Nam is not hopeless: it pays for three stations while one pays back

Owner, 30 July 00:03:

> MN thì chả có hiệu quả nào luôn sao em? Hãy phân tích MN luôn chứ em. Tất cả các vấn đề cần được
> ghi nhận, cập nhật đầy đủ để tránh lãng quên, cập nhật github report dùm anh luôn và tất cả cần
> đo lường và xử lý trong cùng 1 lượt 19/08 nha em.

> Thu về còn được x với số hit nữa nha em... Nhưng cái vấn đề này cần để "" cái anh vẫn xem 1/1 còn
> tính ổn định chắc chắn, còn số hit là con số may mắn hơn có tháng sẽ tăng trưởng và có tháng ổn
> định thì hay hơn nha em.

## 1. The accounting standard the owner locked

From now on every economic figure is reported in two layers.

**`1/1`** counts a hit once regardless of how many nháy it produced. This is the **stable measure
and the basis for decisions**.

**Nháy-multiplied** is reported only as luck upside and never used to justify a plan.

This matters more than it sounds. The gap between the two layers runs from 7 to 39 percentage
points. `/choi` Miền Bắc on both numbers reads **−28.7% at 1/1** but only −9.3% with nháy — enough
to make a losing plan look profitable.

## 2. What is actually wrong with Miền Nam

Miền Nam is not weak on numbers. It runs **3.13 stations a day** at 18 prize sets each, and the bet
is placed on **all** of them, so cost triples while usually only one station pays back.

Break-even per station is **18.4%** (18.000đ cost against 98.000đ payout).

De-herd pick hit rate per station over 90 days:

| Station | Hit rate | ROI at 1/1 if that station alone |
|---|---|---|
| Bình Thuận | 41.7% | +126.9% |
| Đà Lạt | 30.8% | +67.5% |
| Cần Thơ | 30.8% | +67.5% |
| TP.HCM, Bình Dương, Kiên Giang, Tiền Giang, Bến Tre | 23.1% | +25.6% |
| Tây Ninh | 16.7% | −9.3% |
| Trà Vinh, Hậu Giang, Long An, Đồng Tháp, Bạc Liêu, Vũng Tàu, Sóc Trăng, Đồng Nai | 15.4% | −16.2% |
| Vĩnh Long, Bình Phước, Cà Mau | 7.7% | −58.1% |
| **An Giang** | **0.0%** | −100.0% |

Seven stations sit below break-even and drag the whole region down.

**The fix, measured causally:** bet only the **two best-form stations from the trailing 21 days**,
with no lookahead. That gives **+15.7% at 1/1** against +8.5% for betting every station — close to
double.

## 3. Monthly stability, the measure the owner asked for

ROI at 1/1, de-herd single number, 50 points:

| Region | Plan | May | Jun | Jul | Total | Months positive |
|---|---|---|---|---|---|---|
| **Miền Trung** | **one best-form station** | **+29.6%** | **+27.0%** | **+50.2%** | **+36.1%** | **3 of 3** |
| Miền Nam | two best-form stations | +68.5% | +18.0% | −24.9% | +15.7% | 2 of 3 |
| Miền Nam | all stations (current) | +32.0% | +10.0% | −10.3% | +8.5% | 2 of 3 |
| Miền Trung | all stations (current) | +17.4% | −1.7% | +1.1% | +4.4% | 2 of 3 |
| Miền Bắc | single station | −48.1% | −27.4% | +12.6% | −18.3% | 1 of 3 |

**Miền Trung on one best-form station is the only plan positive in every month, and it is rising.**

## 4. Two of my earlier conclusions corrected

**Miền Bắc's +12.6% was a July-only effect.** Across three months Miền Bắc is **−18.3%** with only
one positive month, moving −48.1% → −27.4% → +12.6%. The recommendation from the previous session
rested on that single good month, so it drops from a play recommendation to watch-only.

**The Miền Trung first-number figure of +63.3% was the nháy version.** At 1/1 it is **+24.4%**,
against +18.4% for both numbers and +12.1% for the second number alone.

## 5. Official at 1/1

Miền Nam **−22.2%**, Miền Trung **−37.8%**, Miền Bắc **−49.9%**. Heavy loss in all three regions on
the stable measure.

## 6. Everything consolidated into one 19 August session

Per the owner's instruction that measurement and action happen in a single pass:

| # | Item | Evidence | Status |
|---|---|---|---|
| A | Close out the de-herd lane after 21 forward days | leading official with no region behind | forward 1 of 21 |
| B | Miền Trung: switch from two numbers to first number only | 1/1: +24.4% versus +18.4% | awaiting signature |
| C | **Miền Trung: bet only the best-form station** | positive 3 of 3 months, +36.1% | awaiting signature, strongest |
| D | Miền Nam: bet only the two best-form stations | +15.7% versus +8.5%, but July negative | awaiting signature |
| E | Miền Bắc: play or stop | 1 of 3 months positive, total −18.3% | needs more data |
| F | Miền Bắc: drop the first number | second number still −5.9% at 1/1, only reduces loss | deprioritised |
| G | Rebuild `rules_union` on a pre-draw timestamp | post-draw union inflates by ~12pp | required before any Total backtest |
| H | Build a `/choi` performance table per `method_label` | play advice must read the method of the day | not started |
| I | Restore the cost/latency table (dead since 6 May) and P&L summary (dead since 20 May) | | not started |
| J | Verdict on the two premium shadow models after 30 rows | running from 30 July | pending |

No runtime change was made. Evidence:
`artifacts/v10876_mn_station_economics/V10876_MN_STATION_ECONOMICS.json`.
