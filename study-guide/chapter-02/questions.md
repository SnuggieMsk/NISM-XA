# Chapter 2: Time Value of Money — 100 MCQ Question Bank

> ⭐ **The most exam-critical bank in the guide.** Three tiers — 🟢 Easy (Recall), 🟡 Medium (Application), 🔴 Hard (Numerical & Scenario). Keep a spreadsheet open and check each answer with `=FV()`, `=PV()`, `=PMT()`, `=RATE()`. Remember the **25% negative marking**.

## 🟢 Tier 1 — Easy: Recall (Q1–Q35)

**Q1.** The time value of money concept states that:
A) All rupees are worth the same regardless of timing  B) A rupee today is worth more than a rupee tomorrow  C) A rupee tomorrow is worth more than a rupee today  D) Money loses value only when inflation is above 5%
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Money available today can be invested (opportunity cost), buys more (inflation), and is certain (risk).
A) Ignores all three reasons. C) Reverses the principle. D) Inflation is only one of three reasons, and it applies at any positive rate.
</details>

**Q2.** The formula for the future value of a lump sum is:
A) FV = PV × (1 + r × n)  B) FV = PV ÷ (1 + r)ⁿ  C) FV = PV × (1 + r)ⁿ  D) FV = PV × r × n
<details><summary>Answer & Explanation</summary>

**Correct: C)** — Compounding multiplies the present value by **(1 + r)ⁿ**.
A) Is the **simple interest** formula. B) Is present value (discounting). D) Computes only the interest under simple interest, not the future value.
</details>

**Q3.** Which of these is NOT one of the five TVM variables?
A) PMT  B) NPER  C) Inflation  D) RATE
<details><summary>Answer & Explanation</summary>

**Correct: C)** — The five variables are **PV, FV, RATE, NPER and PMT**. Inflation is used *around* TVM (to inflate goals or compute real returns) but is not one of the five.
A), B) and D) are all core variables.
</details>

**Q4.** In an ordinary annuity, payments occur:
A) At the beginning of each period  B) At the end of each period  C) Only once  D) At irregular intervals
<details><summary>Answer & Explanation</summary>

**Correct: B)** — An **ordinary annuity** pays at the **end** of each period; it is the default assumption.
A) Describes an annuity **due**. C) A single payment is a lump sum, not an annuity. D) Annuities require *regular* intervals and *equal* amounts.
</details>

**Q5.** The relationship between an annuity due and an ordinary annuity is:
A) Due = Ordinary ÷ (1 + r)  B) Due = Ordinary × (1 + r)  C) They are always equal  D) Due = Ordinary × n
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Each payment in an annuity due sits invested **one extra period**, so multiply by **(1 + r)**.
A) Divides, which would make it smaller. C) They are never equal for r > 0. D) Multiplying by n has no basis.
</details>

**Q6.** The present value of a perpetuity is:
A) PMT × r  B) PMT ÷ r  C) PMT × (1 + r)  D) PMT ÷ n
<details><summary>Answer & Explanation</summary>

**Correct: B)** — A perpetuity pays forever, so **PV = PMT ÷ r**.
A) Multiplies instead of dividing. C) Is the annuity-due adjustment. D) Perpetuities have no finite n.
</details>

**Q7.** The Rule of 72 estimates:
A) The effective annual rate  B) The number of years for money to double  C) The real rate of return  D) The EMI on a loan
<details><summary>Answer & Explanation</summary>

**Correct: B)** — **Years to double ≈ 72 ÷ annual rate (%)**.
A) EAR uses (1 + r/m)^m − 1. C) Real return uses the ratio formula. D) EMIs use the annuity PMT formula.
</details>

**Q8.** At 9% per annum, money approximately doubles in:
A) 6 years  B) 8 years  C) 12 years  D) 9 years
<details><summary>Answer & Explanation</summary>

**Correct: B)** — 72 ÷ 9 = **8 years**.
A) 6 years corresponds to 12%. C) 12 years corresponds to 6%. D) 9 years corresponds to 8% — note the easy-to-confuse pair: 8% → 9 years, 9% → 8 years.
</details>

**Q9.** Which compounding frequency produces the highest effective annual rate for a given nominal rate?
A) Annual  B) Half-yearly  C) Quarterly  D) Daily
<details><summary>Answer & Explanation</summary>

**Correct: D)** — The more often interest is credited, the sooner it starts earning interest itself, so **daily** gives the highest EAR.
A), B) and C) all compound less frequently. For a 12% nominal: annual 12.000%, half-yearly 12.360%, quarterly 12.551%, daily 12.747%.
</details>

**Q10.** The effective annual rate formula is:
A) (1 + r × m) − 1  B) (1 + r/m)^m − 1  C) (1 + r)^m − 1  D) r ÷ m
<details><summary>Answer & Explanation</summary>

**Correct: B)** — **EAR = (1 + r/m)^m − 1**: divide the nominal rate by the frequency, compound it m times, subtract 1.
A) Uses simple interest. C) Fails to divide the nominal rate by m, overstating the result badly. D) Gives the periodic rate, not the annual effective rate.
</details>

**Q11.** The real rate of return is calculated as:
A) Nominal − inflation  B) [(1 + nominal) ÷ (1 + inflation)] − 1  C) Nominal × inflation  D) Nominal ÷ inflation
<details><summary>Answer & Explanation</summary>

**Correct: B)** — The exact formula divides the growth factors.
A) The crude subtraction **overstates** the real return and is the most common distractor. C) and D) have no basis.
</details>

**Q12.** In Excel, money paid out should be entered as:
A) A positive number  B) A negative number  C) Zero  D) Either, it makes no difference
<details><summary>Answer & Explanation</summary>

**Correct: B)** — The sign convention is **outflows negative, inflows positive**.
A) Would misstate the direction of the cash flow. C) Zero would remove the cash flow entirely. D) It matters greatly — same-sign entries typically produce `#NUM!`.
</details>

**Q13.** Which Excel function solves for the periodic payment?
A) `=FV()`  B) `=PV()`  C) `=PMT()`  D) `=NPER()`
<details><summary>Answer & Explanation</summary>

**Correct: C)** — `=PMT(rate, nper, pv, [fv], [type])`.
A) Solves for future value. B) Solves for present value. D) Solves for the number of periods.
</details>

**Q14.** Simple interest differs from compound interest because simple interest:
A) Is earned on principal plus accumulated interest  B) Is earned on the principal only  C) Grows exponentially  D) Always produces a higher value
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Simple interest is computed on the **original principal only**, giving straight-line growth.
A) and C) describe compound interest. D) Compound interest always produces more for n > 1 and r > 0.
</details>

**Q15.** The FV of an ordinary annuity is:
A) PMT × [((1+r)ⁿ − 1) ÷ r]  B) PMT ÷ r  C) PMT × (1+r)ⁿ  D) PMT × n
<details><summary>Answer & Explanation</summary>

**Correct: A)** — The annuity factor is **[((1+r)ⁿ − 1) ÷ r]**.
B) Is a perpetuity. C) Compounds a single payment. D) Ignores interest completely — that is just the total contributed.
</details>

**Q16.** Which of the following is an annuity?
A) A one-time bonus of ₹5,00,000  B) A monthly SIP of ₹10,000 for 10 years  C) Irregular dividend payments  D) A lump-sum inheritance
<details><summary>Answer & Explanation</summary>

**Correct: B)** — An annuity requires **equal amounts at regular intervals** — a SIP fits exactly.
A) and D) are lump sums. C) Dividends vary in amount and timing, so they are not an annuity.
</details>

**Q17.** For a growing perpetuity, the formula PV = PMT₁ ÷ (r − g) requires:
A) g > r  B) g < r  C) g = r  D) g = 0
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Growth must be **less than** the discount rate, otherwise the denominator is zero or negative and the value is infinite/meaningless.
A) and C) break the formula. D) g = 0 is allowed but reduces it to an ordinary perpetuity — it is not a *requirement*.
</details>

**Q18.** When converting an annual rate to a monthly rate for TVM purposes, you should:
A) Multiply the annual rate by 12  B) Divide the annual rate by 12  C) Leave it unchanged  D) Divide by 365
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Use **r ÷ 12** for the monthly periodic rate, together with n = years × 12.
A) Multiplying inflates the rate twelve-fold. C) Mixing an annual rate with monthly periods is the classic error. D) 365 applies to daily compounding.
</details>

**Q19.** Discounting means:
A) Moving a cash flow forward in time  B) Moving a cash flow backward in time to find its present value  C) Reducing the interest rate  D) Applying a sales rebate
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Discounting divides by (1+r)ⁿ to bring a future amount **back** to today.
A) That is compounding. C) and D) confuse the financial meaning of "discount" with everyday usage.
</details>

**Q20.** Which statement about the nominal rate is correct when compounding frequency increases?
A) The nominal rate rises  B) The nominal rate stays the same while the effective rate rises  C) Both fall  D) The effective rate stays the same
<details><summary>Answer & Explanation</summary>

**Correct: B)** — The **stated/nominal** rate is unchanged; only the **effective** rate rises.
A) and C) misstate the direction. D) The effective rate is precisely what changes.
</details>

**Q21.** ₹1,00,000 at 10% simple interest for 20 years grows to:
A) ₹6,72,750  B) ₹3,00,000  C) ₹2,00,000  D) ₹1,10,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — FV = PV × (1 + r×n) = 1,00,000 × (1 + 0.10 × 20) = 1,00,000 × 3 = **₹3,00,000**.
A) ₹6,72,750 is the **compound** result. C) ₹2,00,000 would be 10 years of simple interest. D) ₹1,10,000 is one year only.
</details>

**Q22.** The PV of an ordinary annuity formula is:
A) PMT × [(1 − (1+r)⁻ⁿ) ÷ r]  B) PMT × [((1+r)ⁿ − 1) ÷ r]  C) PMT ÷ (r − g)  D) PMT × (1+r)
<details><summary>Answer & Explanation</summary>

**Correct: A)** — The PV annuity factor is **[(1 − (1+r)⁻ⁿ) ÷ r]**.
B) Is the **FV** annuity factor. C) Is a growing perpetuity. D) Is the annuity-due adjustment.
</details>

**Q23.** In the Excel `type` argument, `type = 1` means:
A) Ordinary annuity  B) Annuity due (payment at the beginning)  C) Simple interest  D) Continuous compounding
<details><summary>Answer & Explanation</summary>

**Correct: B)** — `type = 1` shifts payments to the **beginning** of each period.
A) `type = 0` is the ordinary annuity default. C) and D) are not controlled by `type`.
</details>

**Q24.** To find the rate given PV, FV and n, you use:
A) r = (FV ÷ PV)^(1/n) − 1  B) r = (FV − PV) ÷ n  C) r = FV ÷ PV  D) r = ln(FV ÷ PV)
<details><summary>Answer & Explanation</summary>

**Correct: A)** — Take the nth root of the growth multiple and subtract 1.
B) Computes an average rupee gain, not a rate. C) Gives the total multiple. D) Is part of the **NPER** formula, not the rate.
</details>

**Q25.** An investment doubles in 12 years. Using the Rule of 72, the approximate rate is:
A) 12%  B) 6%  C) 8%  D) 9%
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Rate ≈ 72 ÷ 12 = **6%**.
A) 12% doubles in 6 years. C) 8% doubles in 9 years. D) 9% doubles in 8 years.
</details>

**Q26.** Which of these is a use of the present value concept?
A) Deciding how much to invest today for a future goal  B) Calculating simple interest  C) Measuring inflation  D) Preparing a balance sheet
<details><summary>Answer & Explanation</summary>

**Correct: A)** — PV answers exactly the question "how much do I need **today**?"
B) Simple interest has its own formula. C) Inflation is measured by price indices. D) Balance sheets record current values, not discounted ones.
</details>

**Q27.** The formula n = ln(FV ÷ PV) ÷ ln(1 + r) solves for:
A) The rate  B) The number of periods  C) The payment  D) The present value
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Taking logs of FV = PV(1+r)ⁿ isolates **n**.
A) The rate uses the nth-root formula. C) and D) have their own formulas.
</details>

**Q28.** A nominal rate of 12% compounded quarterly gives a periodic rate of:
A) 12%  B) 4%  C) 3%  D) 1%
<details><summary>Answer & Explanation</summary>

**Correct: C)** — Quarterly means m = 4, so the periodic rate is 12% ÷ 4 = **3%**.
A) Is the annual nominal rate. B) 4% would be m = 3. D) 1% is the monthly rate (m = 12).
</details>

**Q29.** Which of the following will always be true for r > 0 and n > 1?
A) Compound value < simple value  B) Compound value > simple value  C) They are equal  D) It depends on inflation
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Compounding earns interest on interest, so it always exceeds simple interest beyond the first period.
A) Reverses it. C) They are equal only at n = 1. D) Inflation is irrelevant to this comparison.
</details>

**Q30.** The future cost of a goal is calculated as:
A) Today's cost ÷ (1 + inflation)ⁿ  B) Today's cost × (1 + inflation)ⁿ  C) Today's cost × inflation × n  D) Today's cost
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Goals must be inflated forward to the date they will be paid.
A) Discounts instead of inflating. C) Uses simple growth. D) Ignoring inflation is the single most damaging planning error.
</details>

**Q31.** Which Excel function converts a nominal rate to an effective rate?
A) `=NOMINAL()`  B) `=EFFECT()`  C) `=RATE()`  D) `=FV()`
<details><summary>Answer & Explanation</summary>

**Correct: B)** — `=EFFECT(nominal_rate, npery)`.
A) Does the reverse (effective → nominal). C) Solves for the periodic rate in a TVM problem. D) Computes future value.
</details>

**Q32.** In a SIP where the investment is made on the 1st of every month, the appropriate treatment is:
A) Ordinary annuity  B) Annuity due  C) Perpetuity  D) Lump sum
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Payment at the **beginning** of the period is an **annuity due**.
A) Would apply to end-of-month investment. C) A SIP has a finite term. D) A SIP is a series, not a single payment.
</details>

**Q33.** Continuous compounding of a 12% nominal rate gives an effective rate of approximately:
A) 12.00%  B) 12.68%  C) 12.75%  D) 13.50%
<details><summary>Answer & Explanation</summary>

**Correct: C)** — The limit is e^r − 1 = e^0.12 − 1 = 1.1275 − 1 = **12.75%**.
A) Is annual compounding. B) Is monthly compounding. D) Overstates it — continuous compounding is the *ceiling*, only marginally above daily (12.747%).
</details>

**Q34.** Which of these correctly describes the effect of a longer horizon on compounding?
A) The effect is linear  B) The effect accelerates — later years add much more than early years  C) The effect diminishes over time  D) There is no effect after 10 years
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Growth is exponential, so each successive year adds more in absolute terms than the last.
A) Linear growth describes simple interest. C) and D) contradict the exponential nature of compounding.
</details>

**Q35.** A `#NUM!` error in an Excel TVM formula usually means:
A) The rate is too high  B) All cash flows were entered with the same sign  C) The function name is misspelled  D) The file is corrupted
<details><summary>Answer & Explanation</summary>

**Correct: B)** — TVM functions require at least one cash flow of the **opposite sign**.
A) High rates compute fine. C) A misspelling gives `#NAME?`. D) Corruption would produce a different failure.
</details>

## 🟡 Tier 2 — Medium: Application (Q36–Q70)

**Q36.** ₹2,00,000 is invested for 7 years at 8% p.a. compounded annually. What is the future value?
A) ₹3,42,780  B) ₹3,12,000  C) ₹2,16,000  D) ₹4,00,000
<details><summary>Answer & Explanation</summary>

**Correct: A)** — FV = 2,00,000 × (1.08)⁷. (1.08)⁷ = **1.71382**. FV = 2,00,000 × 1.71382 = **₹3,42,764 ≈ ₹3,42,780**.
B) ₹3,12,000 applies simple interest (2,00,000 × 1.56). C) ₹2,16,000 is one year's growth. D) ₹4,00,000 would need about 10.5 years at 8%.
</details>

**Q37.** How much must be invested today to have ₹25,00,000 in 12 years at 10% p.a.?
A) ₹7,96,600  B) ₹12,50,000  C) ₹5,00,000  D) ₹10,00,000
<details><summary>Answer & Explanation</summary>

**Correct: A)** — PV = 25,00,000 ÷ (1.10)¹². (1.10)¹² = **3.13843**. PV = 25,00,000 ÷ 3.13843 = **₹7,96,575 ≈ ₹7,96,600**.
B) ₹12,50,000 simply halves the target. C) ₹5,00,000 is far too low (it would grow to only ₹15.7 lakh). D) ₹10,00,000 would grow to ₹31.4 lakh. Excel: `=PV(10%,12,0,-2500000)`.
</details>

**Q38.** ₹5,00,000 grows to ₹12,50,000 in 10 years. What is the CAGR?
A) 15.00%  B) 9.60%  C) 25.00%  D) 7.20%
<details><summary>Answer & Explanation</summary>

**Correct: B)** — r = (12,50,000 ÷ 5,00,000)^(1/10) − 1 = 2.5^0.1 − 1. ln(2.5) = 0.9163; ÷ 10 = 0.09163; e^0.09163 = 1.09596. r = **9.60% p.a.**
A) 15% would give about ₹20.2 lakh. C) 25% is the *total* gain divided by 10 years — a simple-interest style error. D) 7.20% gives only about ₹10 lakh.
</details>

**Q39.** ₹15,000 invested monthly for 20 years at 12% p.a. (monthly compounding) accumulates to approximately:
A) ₹36,00,000  B) ₹1,49,88,000  C) ₹75,00,000  D) ₹2,50,00,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — r = 0.12 ÷ 12 = **0.01**; n = 240. (1.01)²⁴⁰ = **10.8926**. FV = 15,000 × [(10.8926 − 1) ÷ 0.01] = 15,000 × **989.26** = **₹1,48,38,900 ≈ ₹1.49 crore**.
A) ₹36,00,000 is just the total contributed (15,000 × 240). C) ₹75,00,000 understates the compounding badly. D) ₹2.5 crore overstates it. Excel: `=FV(12%/12,240,-15000)`.
</details>

**Q40.** What is the effective annual rate of 10% nominal compounded quarterly?
A) 10.00%  B) 10.38%  C) 10.47%  D) 11.00%
<details><summary>Answer & Explanation</summary>

**Correct: B)** — EAR = (1 + 0.10/4)⁴ − 1 = (1.025)⁴ − 1 = 1.10381 − 1 = **10.38%**.
A) Is the nominal rate. C) 10.47% corresponds to monthly compounding. D) 11% overstates it. Excel: `=EFFECT(10%,4)`.
</details>

**Q41.** A nominal 9% is compounded monthly. What is the effective annual rate?
A) 9.00%  B) 9.38%  C) 9.20%  D) 9.75%
<details><summary>Answer & Explanation</summary>

**Correct: B)** — EAR = (1 + 0.09/12)¹² − 1 = (1.0075)¹² − 1 = 1.09381 − 1 = **9.38%**.
A) Is the nominal rate. C) 9.20% corresponds roughly to half-yearly compounding. D) 9.75% overstates it.
</details>

**Q42.** A nominal return of 11% with inflation at 6.5% gives a real return of:
A) 4.50%  B) 4.23%  C) 5.00%  D) 4.00%
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Real = (1.11 ÷ 1.065) − 1 = 1.042254 − 1 = **4.23%**.
A) 4.50% is the crude subtraction (11 − 6.5), which overstates the real return. C) and D) do not follow from the formula. **The exam almost always offers the subtraction as a distractor.**
</details>

**Q43.** A goal costs ₹12,00,000 today and is 8 years away. At 7% inflation, the future cost is:
A) ₹18,72,000  B) ₹20,61,700  C) ₹16,80,000  D) ₹24,00,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Future cost = 12,00,000 × (1.07)⁸. (1.07)⁸ = **1.71819**. = **₹20,61,828 ≈ ₹20,61,700**.
A) ₹18,72,000 applies simple inflation (12,00,000 × 1.56). C) ₹16,80,000 assumes only a 40% rise. D) ₹24,00,000 assumes doubling, which at 7% takes about 10.3 years.
</details>

**Q44.** An investor needs ₹40,00,000 in 15 years and expects 10% p.a. What monthly SIP is required?
A) ₹9,650  B) ₹22,200  C) ₹15,000  D) ₹31,000
<details><summary>Answer & Explanation</summary>

**Correct: A)** — r = 0.10 ÷ 12 = **0.008333**; n = 180. (1.008333)¹⁸⁰ = **4.4539**. Annuity factor = (4.4539 − 1) ÷ 0.008333 = **414.47**. PMT = 40,00,000 ÷ 414.47 = **₹9,651**.
B) ₹22,200 corresponds to a much lower assumed return. C) ₹15,000 would overshoot to about ₹62 lakh. D) ₹31,000 is close to 40,00,000 ÷ 180 (₹22,222) inflated — it ignores compounding. Excel: `=PMT(10%/12,180,0,4000000)`.
</details>

**Q45.** ₹8,000 is invested at the **beginning** of every month for 10 years at 12% p.a. What is the corpus?
A) ₹18,41,200  B) ₹18,59,600  C) ₹9,60,000  D) ₹16,00,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — This is an **annuity due**. Ordinary FV = 8,000 × [((1.01)¹²⁰ − 1) ÷ 0.01] = 8,000 × [(3.30039 − 1) ÷ 0.01] = 8,000 × **230.039** = ₹18,40,312. Annuity due = × 1.01 = **₹18,58,715 ≈ ₹18,59,600**.
A) ₹18,41,200 is the **ordinary** annuity value — it forgets the (1+r) adjustment. C) ₹9,60,000 is the total contributed. D) ₹16,00,000 understates the growth. Excel: `=FV(12%/12,120,-8000,0,1)`.
</details>

**Q46.** A pension of ₹50,000 per year is expected in perpetuity. At a 9% discount rate, its present value is:
A) ₹4,50,000  B) ₹5,55,556  C) ₹50,00,000  D) ₹9,00,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — PV = PMT ÷ r = 50,000 ÷ 0.09 = **₹5,55,556**.
A) ₹4,50,000 multiplies instead of dividing (50,000 × 9). C) ₹50,00,000 divides by 0.01. D) ₹9,00,000 has no basis.
</details>

**Q47.** A payment of ₹1,00,000 next year grows 5% a year forever. At a 10% discount rate, the present value is:
A) ₹10,00,000  B) ₹20,00,000  C) ₹6,66,667  D) Infinite
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Growing perpetuity: PV = PMT₁ ÷ (r − g) = 1,00,000 ÷ (0.10 − 0.05) = 1,00,000 ÷ 0.05 = **₹20,00,000**.
A) ₹10,00,000 ignores growth (uses r alone). C) ₹6,66,667 uses r + g. D) Infinite would apply only if g ≥ r. **Growth halves the effective discount rate here, doubling the value.**
</details>

**Q48.** How long will ₹3,00,000 take to become ₹9,00,000 at 12% p.a.?
A) 6.0 years  B) 9.69 years  C) 12.0 years  D) 8.0 years
<details><summary>Answer & Explanation</summary>

**Correct: B)** — n = ln(9,00,000 ÷ 3,00,000) ÷ ln(1.12) = ln(3) ÷ ln(1.12) = 1.0986 ÷ 0.11333 = **9.69 years**.
A) 6 years only doubles it (Rule of 72: 72 ÷ 12 = 6). C) and D) do not follow. **Sanity check: doubling takes 6 years, so tripling must take more — but less than 12.**
</details>

**Q49.** Two deposits offer 10% compounded annually and 9.8% compounded monthly. Which is better?
A) The 10% annual, since the headline rate is higher  B) The 9.8% monthly, because its EAR is about 10.25%  C) They are identical  D) Cannot be compared
<details><summary>Answer & Explanation</summary>

**Correct: B)** — EAR of 9.8% monthly = (1 + 0.098/12)¹² − 1 = (1.0081667)¹² − 1 = **10.25%**, which beats the 10.00% EAR of the annual option.
A) Comparing headline rates is exactly the trap. C) They differ by 0.25 percentage points. D) EAR is precisely the tool that makes them comparable.
</details>

**Q50.** An investor wants ₹75,00,000 in 18 years. She has ₹10,00,000 today earning 11%. What is the shortfall at the goal date?
A) ₹9,56,450  B) ₹10,58,000  C) Nil — she will exceed the goal  D) ₹65,43,550
<details><summary>Answer & Explanation</summary>

**Correct: A)** — Grow the existing corpus first: 10,00,000 × (1.11)¹⁸. (1.11)¹⁸ = **6.54355**, so the corpus reaches **₹65,43,550**. Shortfall = 75,00,000 − 65,43,550 = **₹9,56,450**.
B) ₹10,58,000 overstates the gap. C) She falls short, not over. D) ₹65,43,550 is the grown corpus itself, not the gap. *(Always compute the grown corpus first, then subtract from the target.)*
</details>

**Q51.** ₹20,000 a month for 25 years at 11% p.a. gives a corpus of approximately:
A) ₹60,00,000  B) ₹3,15,27,000  C) ₹1,50,00,000  D) ₹6,50,00,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — r = 0.0091667, n = 300. (1.0091667)³⁰⁰ = **15.4499**. Annuity factor = (15.4499 − 1) ÷ 0.0091667 = **1576.36**. FV = 20,000 × 1576.36 = **₹3,15,27,200**.
A) ₹60,00,000 is simply the total contributed (20,000 × 300). C) ₹1.5 crore understates the growth by half. D) ₹6.5 crore overstates it. **Over 25 years, ₹60 lakh of contributions becomes about ₹3.15 crore — roughly 81% of the corpus is return.**
</details>

**Q52.** Which is worth more today: ₹10,00,000 received in 5 years, or ₹6,00,000 received today, at an 8% discount rate?
A) The ₹10,00,000 in 5 years, worth about ₹6,80,600 today  B) The ₹6,00,000 today  C) They are equal  D) Cannot be determined
<details><summary>Answer & Explanation</summary>

**Correct: A)** — PV of ₹10,00,000 = 10,00,000 ÷ (1.08)⁵ = 10,00,000 ÷ **1.46933** = **₹6,80,583**, which exceeds ₹6,00,000.
B) Would be right only at a discount rate above about 10.8%. C) They differ by roughly ₹80,000. D) With PV, FV, n and r known, it is fully determinable.
</details>

**Q53.** An EMI is best described as which TVM concept?
A) The FV of an annuity  B) The PMT that makes the PV of payments equal the loan amount  C) A perpetuity  D) A lump sum
<details><summary>Answer & Explanation</summary>

**Correct: B)** — A loan is a **present value**; the EMI is the payment whose present value equals the loan amount: **PMT = PV × r(1+r)ⁿ ÷ [(1+r)ⁿ − 1]**.
A) Uses the FV form, appropriate for savings not loans. C) Loans have a finite term. D) An EMI is a series, not a single payment.
</details>

**Q54.** An investor's portfolio returns 14% nominal in a year with 5% inflation and pays 20% tax on gains. What is the post-tax real return?
A) 9.00%  B) 6.29%  C) 11.20%  D) 5.90%
<details><summary>Answer & Explanation</summary>

**Correct: D)** — Two steps, in this order. **Tax first:** post-tax nominal = 14% × (1 − 0.20) = **11.2%**. **Then deflate:** real = (1.112 ÷ 1.05) − 1 = 1.05905 − 1 = **5.90%**.
A) 9% subtracts inflation from the *pre-tax* return, ignoring tax altogether. B) 6.29% adjusts for inflation first and taxes afterwards — the wrong order. C) 11.2% is the post-tax nominal return, before inflation. **Always tax first, then deflate.**
</details>

**Q55.** ₹1,00,000 invested at 8% compounded half-yearly for 5 years gives:
A) ₹1,46,933  B) ₹1,48,024  C) ₹1,40,000  D) ₹1,60,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — m = 2, so the periodic rate is 4% and n = 10 periods. FV = 1,00,000 × (1.04)¹⁰ = 1,00,000 × **1.48024** = **₹1,48,024**.
A) ₹1,46,933 is **annual** compounding ((1.08)⁵). C) ₹1,40,000 is simple interest. D) ₹1,60,000 overstates it. **Note half-yearly beats annual by ₹1,091.**
</details>

**Q56.** A client will receive ₹5,00,000 a year for 12 years, first payment one year from now. At 9%, the present value is:
A) ₹60,00,000  B) ₹35,79,000  C) ₹45,00,000  D) ₹30,00,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — PV annuity = PMT × [(1 − (1.09)⁻¹²) ÷ 0.09]. (1.09)¹² = **2.81266**, so (1.09)⁻¹² = **0.35553**. Factor = (1 − 0.35553) ÷ 0.09 = 0.64447 ÷ 0.09 = **7.1608**. PV = 5,00,000 × 7.1608 = **₹35,80,400 ≈ ₹35,79,000**.
A) ₹60,00,000 is the undiscounted total (5,00,000 × 12). C) and D) do not follow from the factor.
</details>

**Q57.** If a SIP is switched from end-of-month to beginning-of-month, the corpus:
A) Falls  B) Rises by a factor of (1 + r)  C) Is unchanged  D) Doubles
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Every payment gains one extra period of compounding, so the whole series is multiplied by **(1 + r)**.
A) It rises, not falls. C) Timing genuinely matters. D) The uplift is one period's interest — typically well under 1% for monthly SIPs, not 100%.
</details>

**Q58.** A client has 25 years to retirement and can invest ₹12,000 a month at 12%. Approximately what corpus results?
A) ₹36,00,000  B) ₹2,25,00,000  C) ₹1,00,00,000  D) ₹5,00,00,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — r = 0.01, n = 300. (1.01)³⁰⁰ = **19.7885**. Factor = (19.7885 − 1) ÷ 0.01 = **1878.85**. FV = 12,000 × 1878.85 = **₹2,25,46,200**.
A) ₹36,00,000 is the total contributed. C) ₹1 crore understates it by half. D) ₹5 crore overstates it. **Roughly 84% of the corpus is return — the case for starting early in one number.**
</details>

**Q59.** A bank quotes 7.5% compounded quarterly on an FD. Inflation is 6% and the client's tax rate is 30%. The post-tax real return is approximately:
A) +1.5%  B) −0.6%  C) +0.9%  D) −2.0%
<details><summary>Answer & Explanation</summary>

**Correct: B)** — EAR = (1 + 0.075/4)⁴ − 1 = (1.01875)⁴ − 1 = **7.71%**. Post-tax = 7.71% × 0.70 = **5.40%**. Real = (1.0540 ÷ 1.06) − 1 = **−0.57% ≈ −0.6%**.
A) +1.5% ignores tax. C) +0.9% ignores either tax or inflation. D) −2.0% overstates the erosion. **The "safe" FD delivers a negative real return after tax — a core planning insight.**
</details>

**Q60.** An investment of ₹6,00,000 becomes ₹6,00,000 after 10 years in nominal terms, with inflation at 6%. What happened in real terms?
A) The investor broke even  B) The investor lost about 44% of purchasing power  C) The investor gained  D) Cannot be determined
<details><summary>Answer & Explanation</summary>

**Correct: B)** — In real terms the value is 6,00,000 ÷ (1.06)¹⁰ = 6,00,000 ÷ **1.79085** = **₹3,35,040** in today's money — a loss of about **44%** of purchasing power.
A) Nominal break-even is not real break-even. C) There is no gain at all. D) With the inflation rate given, it is fully determinable.
</details>

**Q61.** Which pair of inputs is internally consistent for a monthly SIP over 12 years at 10% p.a.?
A) r = 10%, n = 12  B) r = 0.10/12, n = 144  C) r = 0.10, n = 144  D) r = 0.10/12, n = 12
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Monthly rate = **0.10 ÷ 12** and monthly periods = 12 years × 12 = **144**. Both must be monthly.
A) Uses annual rate with 12 periods — that describes 12 *years* of annual compounding, not a monthly SIP. C) Mixes an annual rate with monthly periods — the classic error. D) Mixes a monthly rate with only 12 periods (i.e. one year).
</details>

**Q62.** A client needs ₹18,00,000 in 6 years and can earn 9%. She invests ₹6,00,000 today. What additional annual (year-end) investment is needed?
A) ₹1,05,500  B) ₹1,45,700  C) ₹3,00,000  D) ₹50,000
<details><summary>Answer & Explanation</summary>

**Correct: A)** — Three steps. **Grow the lump sum:** 6,00,000 × (1.09)⁶ = 6,00,000 × **1.67710** = **₹10,06,260**. **Find the gap:** 18,00,000 − 10,06,260 = **₹7,93,740**. **Annuitise it:** factor = ((1.09)⁶ − 1) ÷ 0.09 = 0.6771 ÷ 0.09 = **7.5233**; PMT = 7,93,740 ÷ 7.5233 = **₹1,05,504**.
B) ₹1,45,700 ignores the existing lump sum's growth. C) ₹3,00,000 is roughly the gap ÷ 6, ignoring returns. D) ₹50,000 falls far short. Excel: `=PMT(9%,6,0,-793740)`.
</details>

**Q63.** The PV of an annuity **falls** when:
A) The discount rate falls  B) The discount rate rises  C) The number of payments rises  D) The payment amount rises
<details><summary>Answer & Explanation</summary>

**Correct: B)** — A higher discount rate shrinks every future cash flow, so the present value falls.
A) A lower rate raises PV. C) More payments raise PV. D) Larger payments raise PV.
</details>

**Q64.** A client compares a lump sum of ₹25,00,000 today against ₹3,00,000 a year for 12 years. At 8%, which is better?
A) The annuity, worth about ₹22,60,000  B) The lump sum, since the annuity's PV is about ₹22,60,000  C) They are equal  D) The annuity, worth ₹36,00,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — PV of the annuity = 3,00,000 × [(1 − (1.08)⁻¹²) ÷ 0.08]. (1.08)¹² = **2.51817**, so (1.08)⁻¹² = **0.39711**. Factor = 0.60289 ÷ 0.08 = **7.5361**. PV = 3,00,000 × 7.5361 = **₹22,60,830**. The lump sum of ₹25,00,000 is worth more today.
A) Correctly values the annuity but draws the wrong conclusion. C) They differ by about ₹2.4 lakh. D) ₹36,00,000 is the *undiscounted* total, which ignores the time value entirely.
</details>

**Q65.** Doubling the investment horizon from 10 to 20 years at 12% multiplies the lump-sum corpus by approximately:
A) 2 times  B) 3.1 times  C) 1.5 times  D) 10 times
<details><summary>Answer & Explanation</summary>

**Correct: B)** — (1.12)¹⁰ = **3.1058**; (1.12)²⁰ = **9.6463**. Ratio = 9.6463 ÷ 3.1058 = **3.11 times**.
A) Doubling time does *not* double the corpus — that is the linear intuition compounding defeats. C) 1.5× badly understates it. D) 10× is the total multiple over 20 years, not the incremental effect.
</details>

**Q66.** An annuity due of ₹1,00,000 a year for 10 years at 10% has a present value of:
A) ₹6,14,460  B) ₹6,75,900  C) ₹10,00,000  D) ₹5,58,600
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Ordinary PV = 1,00,000 × [(1 − (1.10)⁻¹⁰) ÷ 0.10]. (1.10)¹⁰ = **2.59374**, so (1.10)⁻¹⁰ = **0.38554**. Factor = 0.61446 ÷ 0.10 = **6.14457**. Ordinary PV = **₹6,14,457**. Annuity due = × 1.10 = **₹6,75,903**.
A) ₹6,14,460 is the **ordinary** value, missing the (1+r) step. C) ₹10,00,000 is undiscounted. D) ₹5,58,600 over-discounts.
</details>

**Q67.** Which statement about compounding frequency is TRUE?
A) The benefit of higher frequency grows without limit  B) The benefit rises but with diminishing increments, approaching continuous compounding  C) Frequency has no effect  D) Annual compounding always gives the most
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Each increase in frequency adds less than the last, converging on **e^r − 1**.
A) The benefit is bounded by continuous compounding. C) Frequency clearly matters. D) Annual gives the *least*.
</details>

**Q68.** A goal is ₹30,00,000 in 10 years. The client can invest ₹15,000 a month. What return is needed (approximately)?
A) About 5%  B) About 9.9%  C) About 15%  D) About 2%
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Total contributed = 15,000 × 120 = ₹18,00,000, and the target is ₹30,00,000, so a moderate return is needed. Testing 10%: factor = ((1.008333)¹²⁰ − 1) ÷ 0.008333 = (2.70704 − 1) ÷ 0.008333 = **204.84**; FV = 15,000 × 204.84 = **₹30,72,600** — slightly above target, so the required rate is just under 10%, about **9.9%**.
A) 5% gives about ₹23.3 lakh. C) 15% gives about ₹41.8 lakh. D) 2% gives about ₹19.9 lakh. Excel: `=RATE(120,-15000,0,3000000)*12`.
</details>

**Q69.** A retiree wants ₹40,000 a month for 25 years from a corpus earning 8% p.a. What corpus is needed at retirement?
A) ₹1,20,00,000  B) ₹51,84,000  C) ₹2,40,00,000  D) ₹80,00,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — This is the **PV of an ordinary annuity**. r = 0.08 ÷ 12 = **0.0066667**; n = 300. (1.0066667)³⁰⁰ = **7.34018**, so the inverse is **0.13624**. Factor = (1 − 0.13624) ÷ 0.0066667 = 0.86376 ÷ 0.0066667 = **129.56**. Corpus = 40,000 × 129.56 = **₹51,82,400 ≈ ₹51,84,000**.
A) ₹1.2 crore is the undiscounted total (40,000 × 300). C) ₹2.4 crore doubles that. D) ₹80,00,000 overstates the requirement. **Note the corpus needed is far below the total withdrawn, because the balance keeps earning.**
</details>

**Q70.** In the standard goal calculation, the correct sequence is:
A) Find the SIP → inflate the goal → grow existing assets  B) Inflate the goal → grow existing assets → find the gap → solve for the SIP  C) Grow existing assets → find the SIP → inflate the goal  D) Find the gap → inflate the goal → solve for the SIP
<details><summary>Answer & Explanation</summary>

**Correct: B)** — You cannot size a SIP until you know the **gap**, and you cannot know the gap until the goal is inflated and existing assets are grown to the same date.
A), C) and D) all attempt to compute a later step before its inputs exist.
</details>

## 🔴 Tier 3 — Hard: Numerical & Scenario (Q71–Q100)

**Q71.** A client invests ₹3,00,000 today and ₹5,000 a month for 15 years, both earning 11% p.a. (monthly compounding). What is the total corpus?
A) ₹15,55,230  B) ₹38,37,480  C) ₹22,82,250  D) ₹12,00,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Compute the two components separately, then add.
**Lump sum:** r = 0.0091667, n = 180. (1.0091667)¹⁸⁰ = **5.1841**. FV = 3,00,000 × 5.1841 = **₹15,55,230**.
**SIP:** factor = (5.1841 − 1) ÷ 0.0091667 = 4.1841 ÷ 0.0091667 = **456.45**. FV = 5,000 × 456.45 = **₹22,82,250**.
**Total = 15,55,230 + 22,82,250 = ₹38,37,480.**
A) ₹15,55,230 is the lump-sum component alone. C) ₹22,82,250 is the SIP component alone. D) ₹12,00,000 is roughly the total SIP contributed (5,000 × 180 = ₹9,00,000) plus the initial ₹3,00,000, ignoring all growth. **Method: never mix a lump sum and an annuity in one formula — compute each and add.**
</details>

**Q72.** A client needs ₹1,00,00,000 in 20 years. She has ₹8,00,000 today and can invest monthly. Expected return 11% p.a. What monthly SIP fills the gap?
A) ₹3,341  B) ₹8,120  C) ₹11,600  D) ₹15,000
<details><summary>Answer & Explanation</summary>

**Correct: A)** — **Step 1 — grow what she has:** (1.0091667)²⁴⁰ = **8.9006**; 8,00,000 × 8.9006 = **₹71,20,480**. **Step 2 — gap:** 1,00,00,000 − 71,20,480 = **₹28,79,520**. **Step 3 — annuity factor:** (8.9006 − 1) ÷ 0.0091667 = 7.9006 ÷ 0.0091667 = **862.0**. **Step 4 — SIP:** 28,79,520 ÷ 862.0 = **₹3,341 a month**.
B) ₹8,120 ignores part of the existing corpus's growth. C) ₹11,600 is the SIP needed if she had *nothing* saved. D) ₹15,000 overstates it further. **Key insight: the ₹8 lakh already invested does over 70% of the work — the power of a 20-year head start.**
</details>

**Q73.** Two investors: A invests ₹10,000 a month from age 25 to 35 (10 years) then stops and lets it grow to 60. B invests ₹10,000 a month from 35 to 60 (25 years). Both earn 12% p.a. Who ends with more at 60?
A) B, because she invested for 25 years  B) A, despite investing for only 10 years  C) They are equal  D) Cannot be determined
<details><summary>Answer & Explanation</summary>

**Correct: B)** — **Investor A:** SIP for 120 months: factor = ((1.01)¹²⁰ − 1) ÷ 0.01 = (3.30039 − 1) ÷ 0.01 = **230.04**; corpus at 35 = 10,000 × 230.04 = **₹23,00,400**. This then grows untouched for 25 years: × (1.01)³⁰⁰ = × **19.7885** = **₹4,55,17,000**.
**Investor B:** SIP for 300 months: factor = (19.7885 − 1) ÷ 0.01 = **1878.85**; corpus = 10,000 × 1878.85 = **₹1,87,88,500**.
**A ends with ~₹4.55 crore from ₹12 lakh invested; B with ~₹1.88 crore from ₹30 lakh invested.**
A) Reverses the result. C) They differ by more than 2×. D) It is fully determinable. **This is the single most powerful illustration of compounding: time beats amount.**
</details>

**Q74.** A ₹50,00,000 home loan at 9% for 20 years. What is the EMI?
A) ₹44,986  B) ₹37,500  C) ₹52,000  D) ₹41,200
<details><summary>Answer & Explanation</summary>

**Correct: A)** — EMI = P × r(1+r)ⁿ ÷ [(1+r)ⁿ − 1]. r = 0.09 ÷ 12 = **0.0075**; n = 240. (1.0075)²⁴⁰ = **6.00915**. EMI = 50,00,000 × [0.0075 × 6.00915] ÷ [6.00915 − 1] = 50,00,000 × 0.04506862 ÷ 5.00915 = **₹44,986**.
B) ₹37,500 is merely the first month's interest (50,00,000 × 0.0075). C) ₹52,000 overstates it. D) ₹41,200 corresponds to a lower rate. Excel: `=PMT(9%/12,240,-5000000)`.
</details>

**Q75.** Using Q74's loan, what is the total amount repaid and the total interest?
A) ₹1,07,96,640 repaid; ₹57,96,640 interest  B) ₹50,00,000 repaid; nil interest  C) ₹90,00,000 repaid; ₹40,00,000 interest  D) ₹67,47,900 repaid; ₹17,47,900 interest
<details><summary>Answer & Explanation</summary>

**Correct: A)** — Total repaid = EMI × n = ₹44,986 × 240 = **₹1,07,96,640**. Interest = 1,07,96,640 − 50,00,000 = **₹57,96,640**.
B) Ignores interest entirely. C) and D) understate it. **The borrower pays more in interest than the original principal — which is why loan tenure is the most powerful lever in Chapter 4.**
</details>

**Q76.** A client can choose: (i) ₹20,00,000 today, or (ii) ₹2,50,000 a year for 15 years starting next year. At what discount rate are the two equal?
A) About 9.1%  B) About 12.5%  C) About 5%  D) About 15%
<details><summary>Answer & Explanation</summary>

**Correct: A)** — Find the rate at which the annuity's PV equals ₹20,00,000, i.e. an annuity factor of 20,00,000 ÷ 2,50,000 = **8.0**. Test rates: at 8%, factor = (1 − (1.08)⁻¹⁵) ÷ 0.08 = (1 − 0.31524) ÷ 0.08 = **8.559** (too high). At 9%: (1 − 0.27454) ÷ 0.09 = **8.061**. At 9.2%: ≈ **7.97**. The factor hits 8.0 at roughly **9.1%**.
B), C) and D) are all well away from the break-even. **Interpretation: if the client can earn more than about 9.1%, take the lump sum; if less, take the annuity.** Excel: `=RATE(15,2500000,-20000000)`.
</details>

**Q77.** A goal costs ₹15,00,000 today, is 10 years away, inflation is 6%, and the client has ₹4,00,000 earmarked earning 10%. What monthly SIP at 10% closes the gap?
A) ₹5,950  B) ₹8,050  C) ₹13,110  D) ₹3,200
<details><summary>Answer & Explanation</summary>

**Correct: B)** — The four-step template:
**Step 1 — inflate the goal:** 15,00,000 × (1.06)¹⁰ = 15,00,000 × **1.79085** = **₹26,86,275**.
**Step 2 — grow existing assets:** 4,00,000 × (1.10)¹⁰ = 4,00,000 × **2.59374** = **₹10,37,496**.
**Step 3 — gap:** 26,86,275 − 10,37,496 = **₹16,48,779**.
**Step 4 — solve for the SIP:** r = 0.008333, n = 120, (1.008333)¹²⁰ = **2.70704**; factor = (2.70704 − 1) ÷ 0.008333 = **204.84**. PMT = 16,48,779 ÷ 204.84 = **₹8,049**.

A) ₹5,950 understates it. C) ₹13,110 is the SIP needed if the existing ₹4,00,000 were ignored entirely. D) ₹3,200 is far too low. **This four-step method is the template for every goal caselet in the exam.**
</details>

**Q78.** An investor earns 15% in year 1, −10% in year 2 and 20% in year 3. What is the CAGR?
A) 8.33%  B) 7.49%  C) 24.20%  D) 6.00%
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Compound the growth factors, never average the percentages: 1.15 × 0.90 × 1.20 = **1.2420**. CAGR = (1.2420)^(1/3) − 1. ln(1.2420) = 0.21675; ÷ 3 = 0.07225; e^0.07225 = **1.07492**. CAGR = **7.49% p.a.**
A) 8.33% is the **arithmetic mean** ((15 − 10 + 20) ÷ 3), which always **overstates** the compounded result when returns vary. C) 24.20% is the *cumulative* 3-year gain misread as annual. D) 6% understates it. **Key point: geometric mean (CAGR) < arithmetic mean whenever returns are volatile — see Chapter 16.**
</details>

**Q79.** A client deposits ₹1,00,000 at the start of each year for 5 years at 10%. What is the value at the end of year 5?
A) ₹6,10,510  B) ₹6,71,561  C) ₹5,00,000  D) ₹5,52,560
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Beginning-of-year deposits form an **annuity due**. Ordinary FV = 1,00,000 × [((1.10)⁵ − 1) ÷ 0.10] = 1,00,000 × [(1.61051 − 1) ÷ 0.10] = 1,00,000 × **6.1051** = ₹6,10,510. Annuity due = × 1.10 = **₹6,71,561**.
A) ₹6,10,510 is the ordinary annuity value — the classic omission. C) ₹5,00,000 is the total deposited. D) ₹5,52,560 under-compounds. Excel: `=FV(10%,5,-100000,0,1)`.
</details>

**Q80.** A ₹10,00,000 investment must grow to ₹40,00,000. At 12% p.a., how long will it take?
A) 6.0 years  B) 12.2 years  C) 18.0 years  D) 9.7 years
<details><summary>Answer & Explanation</summary>

**Correct: B)** — n = ln(4) ÷ ln(1.12) = 1.38629 ÷ 0.113329 = **12.23 years**.
A) 6 years doubles it (Rule of 72). C) 18 years would take it to about ₹76.9 lakh. D) 9.7 years triples it. **Sanity check with the Rule of 72: doubling takes 6 years, and quadrupling is two doublings ≈ 12 years. ✓**
</details>

**Q81.** A client has ₹80,00,000 at retirement, wants ₹60,000 a month, and the corpus earns 7% p.a. How long will the money last?
A) About 12 years  B) About 21.5 years  C) Indefinitely  D) About 30 years
<details><summary>Answer & Explanation</summary>

**Correct: B)** — r = 0.07 ÷ 12 = **0.0058333**. **First check sustainability:** monthly interest on ₹80,00,000 = 80,00,000 × 0.0058333 = **₹46,667**, which is *less* than the ₹60,000 withdrawal — so the corpus **will** deplete.
**Then solve for NPER:** n = −ln(1 − (PV × r ÷ PMT)) ÷ ln(1 + r) = −ln(1 − (80,00,000 × 0.0058333 ÷ 60,000)) ÷ ln(1.0058333) = −ln(0.22222) ÷ 0.0058164 = 1.50408 ÷ 0.0058164 = **258.6 months ≈ 21.5 years**.
A) 12 years understates it. C) It would last indefinitely only if the withdrawal were at or below ₹46,667. D) 30 years overstates it. Excel: `=NPER(7%/12,60000,-8000000)`.
</details>

**Q82.** Continuing Q81: what monthly withdrawal could the client sustain indefinitely?
A) ₹46,667  B) ₹60,000  C) ₹80,000  D) ₹1,00,000
<details><summary>Answer & Explanation</summary>

**Correct: A)** — A **perpetuity**: withdraw only the interest earned. Monthly interest = 80,00,000 × (0.07 ÷ 12) = 80,00,000 × 0.0058333 = **₹46,667**.
B) ₹60,000 exceeds the interest earned and depletes the corpus (as Q81 showed). C) and D) deplete it far faster. **Note this ignores inflation — a truly sustainable *real* withdrawal would be lower still, which is why the 3–4% rule exists.**
</details>

**Q83.** ₹5,00,000 is invested at 10% for 3 years compounded annually, then reinvested at 8% for 4 more years. What is the final value?
A) ₹9,05,300  B) ₹6,65,500  C) ₹8,50,000  D) ₹10,00,000
<details><summary>Answer & Explanation</summary>

**Correct: A)** — **Phase 1:** 5,00,000 × (1.10)³ = 5,00,000 × **1.331** = **₹6,65,500**. **Phase 2:** 6,65,500 × (1.08)⁴ = 6,65,500 × **1.36049** = **₹9,05,406**.
B) ₹6,65,500 stops after phase 1. C) ₹8,50,000 understates phase 2. D) ₹10,00,000 overstates it. **Method: chain the phases — never average the two rates.**
</details>

**Q84.** In Q83, what single CAGR over the 7 years is equivalent?
A) 9.00%  B) 8.86%  C) 10.00%  D) 8.00%
<details><summary>Answer & Explanation</summary>

**Correct: B)** — CAGR = (9,05,406 ÷ 5,00,000)^(1/7) − 1 = (1.810812)^(1/7) − 1. ln(1.810812) = 0.59380; ÷ 7 = 0.084829; e^0.084829 = **1.08853**. CAGR = **8.85%**.
A) 9% is the simple average weighted wrongly. C) and D) are the two individual phase rates. **Note the CAGR (8.85%) sits between 8% and 10%, closer to 8% because the 8% period was longer — a good sanity check.**
</details>

**Q85.** A client wants ₹1,00,000 a month in today's terms at retirement in 20 years. Inflation is 6%. What monthly income will she need in the first year of retirement?
A) ₹2,00,000  B) ₹3,20,700  C) ₹1,60,000  D) ₹5,00,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Inflate: 1,00,000 × (1.06)²⁰ = 1,00,000 × **3.20714** = **₹3,20,714**.
A) ₹2,00,000 assumes only a doubling — at 6% doubling takes 12 years, so 20 years must give more. C) ₹1,60,000 badly understates it. D) ₹5,00,000 overstates it. **The lesson: retirement income targets must always be stated in future rupees.**
</details>

**Q86.** Continuing Q85: what corpus is needed at retirement to fund ₹3,20,714 a month for 25 years, if the corpus earns 8%?
A) ₹4,15,50,000  B) ₹9,62,00,000  C) ₹2,00,00,000  D) ₹1,50,00,000
<details><summary>Answer & Explanation</summary>

**Correct: A)** — PV of an ordinary annuity: r = 0.08 ÷ 12 = **0.0066667**, n = 300. From Q69 the factor is **129.56**. Corpus = 3,20,714 × 129.56 = **₹4,15,51,700**.
B) ₹9.62 crore is the undiscounted total (3,20,714 × 300). C) and D) are far too low. **Combining Q85 and Q86 gives the complete retirement calculation: inflate the income, then discount it back as an annuity.**
</details>

**Q87.** An investor is offered 8% compounded monthly or 8.2% compounded annually. Which is better and by how much in EAR terms?
A) 8% monthly, by about 0.10pp  B) 8.2% annual, by about 0.10pp  C) They are identical  D) 8% monthly, by about 1pp
<details><summary>Answer & Explanation</summary>

**Correct: A)** — EAR of 8% monthly = (1 + 0.08/12)¹² − 1 = (1.0066667)¹² − 1 = **8.30%**. The 8.2% annual option has an EAR of exactly **8.20%**. So 8% monthly wins by **0.10 percentage points**.
B) Reverses the winner. C) They differ by 0.10pp. D) Overstates the gap tenfold. **Never compare headline rates — always convert to EAR.**
</details>

**Q88.** A client saves ₹20,000 a month for 5 years, then ₹40,000 a month for the next 10 years, all at 11% p.a. What is the total corpus after 15 years?
A) ₹1,20,00,000  B) ₹1,34,05,000  C) ₹60,00,000  D) ₹85,00,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Split into two phases and value each.
**Phase 1 (₹20,000 × 60 months):** (1.0091667)⁶⁰ = **1.72804**; factor = (1.72804 − 1) ÷ 0.0091667 = **79.42**; value at year 5 = 20,000 × 79.42 = **₹15,88,400**. This then grows untouched for 10 more years: × (1.0091667)¹²⁰ = × **2.98529** = **₹47,42,000**.
**Phase 2 (₹40,000 × 120 months):** factor = (2.98529 − 1) ÷ 0.0091667 = **216.58**; value = 40,000 × 216.58 = **₹86,63,200**.
**Total = 47,42,000 + 86,63,200 = ₹1,34,05,200.**
A) ₹1,20,00,000 understates it. C) ₹60,00,000 is the total contributed (₹12L + ₹48L). D) ₹85,00,000 omits phase 1's carry-forward growth. **Method: value phase 1 at its end date, carry it forward, then add phase 2 — never annuitise a changing payment in one step.**
</details>

**Q89.** A ₹30,00,000 loan at 10% for 15 years. If the client prepays ₹5,00,000 at the end of year 5, what happens?
A) The EMI must rise  B) Either the EMI falls or the tenure shortens — the borrower usually chooses  C) Nothing changes  D) The interest rate falls
<details><summary>Answer & Explanation</summary>

**Correct: B)** — A prepayment reduces the outstanding principal. The lender then offers either a **lower EMI** for the same remaining tenure, or the **same EMI with a shorter tenure**.
A) A prepayment never forces a higher EMI. C) Reducing principal always reduces total interest. D) The contractual rate is unaffected. **Keeping the EMI and shortening the tenure saves far more interest — the key Chapter 4 insight.**
</details>

**Q90.** An investment grows from ₹6,00,000 to ₹7,50,000 in 18 months. What is the annualised return?
A) 25.00%  B) 16.05%  C) 16.67%  D) 12.50%
<details><summary>Answer & Explanation</summary>

**Correct: B)** — The holding-period return is 7,50,000 ÷ 6,00,000 = **1.25** over **1.5 years**. Annualised = 1.25^(1/1.5) − 1 = 1.25^0.6667 − 1. ln(1.25) = 0.22314; × 0.6667 = 0.14876; e^0.14876 = **1.16040**. Annualised = **16.04%**.
A) 25% is the total (un-annualised) return. C) 16.67% divides 25% by 1.5 — a simple-interest shortcut that overstates it. D) 12.5% halves the total return. **Annualising requires compounding, not division.**
</details>

**Q91.** Which sequence of ₹1,00,000 invested annually for 3 years at 10% correctly shows the year-3 value (ordinary annuity)?
A) 1,00,000×(1.10)³ + 1,00,000×(1.10)² + 1,00,000×(1.10)  B) 1,00,000×(1.10)² + 1,00,000×(1.10) + 1,00,000  C) 1,00,000×3×1.10  D) 1,00,000×(1.10)³
<details><summary>Answer & Explanation</summary>

**Correct: B)** — In an **ordinary** annuity the last payment arrives *at* the end of year 3 and earns nothing. The year-1 payment compounds for 2 years, year-2's for 1 year, year-3's for 0. Total = 1,21,000 + 1,10,000 + 1,00,000 = **₹3,31,000**.
A) Describes an **annuity due** (each payment gets one extra year). C) Ignores compounding. D) Compounds only one payment.
</details>

**Q92.** A client's SIP of ₹25,000 a month for 12 years returns 10% p.a. She then stops and lets it grow for 8 more years at 8%. Final value?
A) ₹1,25,00,000  B) ₹1,28,09,000  C) ₹69,00,000  D) ₹36,00,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Two phases.
**Accumulation:** r = 0.008333, n = 144. (1.008333)¹⁴⁴ = **3.30692**; factor = (3.30692 − 1) ÷ 0.008333 = **276.83**; corpus = 25,000 × 276.83 = **₹69,20,750**.
**Growth (no further contribution):** 69,20,750 × (1.08)⁸ = 69,20,750 × **1.85093** = **₹1,28,09,300**.
A) ₹1,25,00,000 is close but understates it. C) ₹69,00,000 stops after the accumulation phase. D) ₹36,00,000 is the total contributed (25,000 × 144). **Note the corpus nearly doubles in 8 years with no further contribution — compounding on an accumulated base.**
</details>

**Q93.** Inflation is 6% and a client's salary rises 8% a year. What is the real growth in purchasing power?
A) 2.00%  B) 1.89%  C) 14.00%  D) 0.75%
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Real growth = (1.08 ÷ 1.06) − 1 = 1.018868 − 1 = **1.89%**.
A) 2% is the crude subtraction, which overstates it. C) 14% adds them. D) 0.75% understates it. **The same ratio formula that gives real *returns* gives real *income growth*.**
</details>

**Q94.** A client can invest ₹10,00,000 today at 9% or receive ₹1,30,000 a year for 12 years. Which is better?
A) The lump sum, since the annuity's PV is about ₹9,30,000  B) The annuity, since its PV is about ₹9,30,000  C) They are equal  D) The annuity, worth ₹15,60,000
<details><summary>Answer & Explanation</summary>

**Correct: A)** — PV of the annuity = 1,30,000 × [(1 − (1.09)⁻¹²) ÷ 0.09] = 1,30,000 × **7.1607** = **₹9,30,891**, which is *less* than ₹10,00,000. So investing the lump sum is better.
B) Values it correctly but draws the wrong conclusion. C) They differ by about ₹69,000. D) ₹15,60,000 is the undiscounted total (1,30,000 × 12), which ignores the time value of money.
</details>

**Q95.** A ₹12,00,000 car loan at 11% for 5 years. What is the EMI and total interest?
A) EMI ₹26,092; interest ₹3,65,520  B) EMI ₹20,000; interest ₹1,00,000  C) EMI ₹30,000; interest ₹6,00,000  D) EMI ₹22,000; interest ₹1,20,000
<details><summary>Answer & Explanation</summary>

**Correct: A)** — r = 0.11 ÷ 12 = **0.0091667**, n = 60. (1.0091667)⁶⁰ = **1.72804**. EMI = 12,00,000 × [0.0091667 × 1.72804] ÷ [1.72804 − 1] = 12,00,000 × 0.01583999 ÷ 0.72804 = **₹26,102**. Total repaid = 26,102 × 60 = ₹15,66,120; interest = **₹3,66,120**.
B) ₹20,000 is roughly the principal ÷ 60, ignoring interest. C) Overstates both. D) Understates both. Excel: `=PMT(11%/12,60,-1200000)`.
</details>

**Q96.** An investor's ₹20,00,000 portfolio must double in real terms in 12 years. Inflation is 6%. What nominal return is required?
A) 6.0%  B) 12.25%  C) 18.0%  D) 8.0%
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Doubling in **real** terms in 12 years needs a real return of 2^(1/12) − 1 = **5.946%**. The required **nominal** return = (1 + real) × (1 + inflation) − 1 = 1.05946 × 1.06 − 1 = 1.12303 − 1 = **12.30%**.
A) 6% is inflation alone, giving zero real growth. C) 18% overstates it. D) 8% gives only about 1.9% real. **The formula runs both ways: nominal = (1 + real)(1 + inflation) − 1.**
</details>

**Q97.** A client invests ₹50,000 at the end of each quarter for 8 years at 10% p.a. compounded quarterly. What is the corpus?
A) ₹16,00,000  B) ₹24,03,000  C) ₹20,00,000  D) ₹30,00,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Quarterly rate = 0.10 ÷ 4 = **0.025**; n = 8 × 4 = **32**. (1.025)³² = **2.20376**. Factor = (2.20376 − 1) ÷ 0.025 = **48.15**. FV = 50,000 × 48.15 = **₹24,07,500 ≈ ₹24,03,000**.
A) ₹16,00,000 is the total contributed (50,000 × 32). C) and D) do not follow. **Note the period conversion: quarterly means divide the rate by 4 and multiply the years by 4.**
</details>

**Q98.** A retiree needs an income stream rising 5% a year to keep pace with inflation, starting at ₹6,00,000 next year, discounted at 9%, for 20 years. Which formula applies?
A) PMT ÷ r  B) The growing annuity formula: [PMT₁ ÷ (r − g)] × [1 − ((1+g)/(1+r))ⁿ]  C) PMT × (1+r)  D) PMT × n
<details><summary>Answer & Explanation</summary>

**Correct: B)** — A **finite** stream that **grows** at a constant rate needs the growing-annuity formula. Here PV = [6,00,000 ÷ 0.04] × [1 − (1.05/1.09)²⁰] = 1,50,00,000 × [1 − 0.47615] = 1,50,00,000 × 0.52385 = **₹78,57,750**.
A) Is a level perpetuity (infinite, no growth). C) Is the annuity-due adjustment. D) Ignores discounting and growth entirely.
</details>

**Q99.** A client is told "your investment grew 100% in 6 years, that's 16.7% a year." This is:
A) Correct  B) Wrong — the correct CAGR is about 12.25%  C) Wrong — the correct CAGR is about 20%  D) Correct only if compounding is annual
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Dividing the total gain by the number of years is a **simple-interest** error. The correct CAGR = 2^(1/6) − 1 = **12.25%**.
A) 16.7% (100 ÷ 6) ignores compounding. C) 20% overstates it. D) The error exists regardless of frequency. **Sanity check with the Rule of 72: doubling in 6 years implies about 72 ÷ 6 = 12% — matching 12.25%. ✓**
</details>

**Q100.** Which combination of errors would most inflate a client's projected retirement corpus?
A) Using an annuity due instead of ordinary, and inflating the goal  B) Ignoring inflation on the goal, using the arithmetic mean return instead of CAGR, and ignoring tax  C) Using CAGR and post-tax returns  D) Using monthly compounding correctly
<details><summary>Answer & Explanation</summary>

**Correct: B)** — All three errors push the same way: **ignoring inflation** understates what is needed, the **arithmetic mean** overstates the return achieved, and **ignoring tax** overstates what the client keeps. Together they can overstate readiness by a wide margin.
A) Inflating the goal is *correct* practice, and the annuity-due difference is small. C) Both are the correct, conservative choices. D) Correct method, no distortion. **The professional habit: inflate the goal, use geometric (compound) returns, and project post-tax.**
</details>

## 🧩 Worked Caselet — Exam-Style Practice

> **Attempt all five sub-questions before checking any answer.** Use a spreadsheet — this is exactly how the 2-mark caselets are set.

### Case: Planning Kavita's Retirement

Kavita is **34 years old** and plans to retire at **60**. Her current annual household expenses are **₹9,00,000**. She expects to live until **85**.

She has already accumulated **₹22,00,000** in an EPF and equity mutual fund portfolio.

**Assumptions:**
- Inflation before *and* after retirement: **6% p.a.**
- Return on the portfolio before retirement: **11% p.a.** (monthly compounding for SIPs)
- Return on the corpus after retirement: **8% p.a.**

---

**QC1.** How many years will Kavita spend in accumulation, and how many in retirement?
A) 26 years accumulating, 25 years retired  B) 34 years accumulating, 26 years retired  C) 26 years accumulating, 51 years retired  D) 25 years accumulating, 25 years retired
<details><summary>Answer & Explanation</summary>

**Correct: A)** — **Accumulation** = retirement age − current age = 60 − 34 = **26 years**. **Retirement** = life expectancy − retirement age = 85 − 60 = **25 years**.
B) 34 is her current age, not a period. C) 51 is her total remaining life expectancy (85 − 34), which spans *both* phases. D) Miscounts the accumulation phase. *(Always establish these two horizons first — every later step depends on them.)*
</details>

**QC2.** What will Kavita's annual expenses be in her first year of retirement?
A) ₹18,00,000  B) ₹40,93,000  C) ₹27,00,000  D) ₹9,00,000
<details><summary>Answer & Explanation</summary>

**Correct: B)** — Inflate for **26 years** at 6%: 9,00,000 × (1.06)²⁶. (1.06)²⁶ = **4.54938**. = **₹40,94,442 ≈ ₹40,93,000**.
A) ₹18,00,000 assumes a mere doubling — but at 6% money doubles in 12 years, so 26 years gives more than 4×. C) ₹27,00,000 assumes 3×. D) ₹9,00,000 ignores inflation entirely. **Rule of 72 check: 72 ÷ 6 = 12 years per doubling; 26 years ≈ 2.17 doublings ≈ 4.5×. ✓**
</details>

**QC3.** Ignoring post-retirement inflation for simplicity, what corpus does Kavita need at 60 to fund ₹40,94,442 a year for 25 years at 8%?
A) ₹10,23,61,050  B) ₹4,37,00,000  C) ₹2,00,00,000  D) ₹40,94,442
<details><summary>Answer & Explanation</summary>

**Correct: B)** — PV of a 25-year ordinary annuity at 8%: factor = (1 − (1.08)⁻²⁵) ÷ 0.08. (1.08)²⁵ = **6.84848**, so the inverse is **0.146018**. Factor = (1 − 0.146018) ÷ 0.08 = 0.853982 ÷ 0.08 = **10.6748**. Corpus = 40,94,442 × 10.6748 = **₹4,37,07,000**.
A) ₹10.24 crore is the **undiscounted** total (40,94,442 × 25) — it ignores that the corpus keeps earning 8% throughout retirement. C) ₹2 crore is far too low. D) Is one year's expense. **Note the corpus needed (₹4.37 cr) is well under half the total withdrawn (₹10.24 cr) — the balance does the rest.**
</details>

**QC4.** Kavita's existing ₹22,00,000 grows at 11% for 26 years. What will it be worth at 60?
A) ₹3,23,70,000  B) ₹1,50,00,000  C) ₹57,20,000  D) ₹5,00,00,000
<details><summary>Answer & Explanation</summary>

**Correct: A)** — FV = 22,00,000 × (1.11)²⁶. (1.11)²⁶ = **14.7138**. FV = **₹3,23,70,360**.
B) ₹1.5 crore understates it badly. C) ₹57,20,000 applies a mere 2.6× (roughly simple interest). D) ₹5 crore overstates it. **Rule of 72 check: at 11%, money doubles roughly every 6.5 years; 26 years ≈ 4 doublings ≈ 16×. ✓ The head start does most of the heavy lifting.**
</details>

**QC5.** Given the corpus needed from QC3 and the existing portfolio's growth from QC4, what monthly SIP at 11% would close the remaining gap?
A) About ₹6,900  B) About ₹25,000  C) No SIP is needed — the existing corpus is nearly sufficient  D) About ₹50,000
<details><summary>Answer & Explanation</summary>

**Correct: A)** — **Gap** = required corpus − grown existing corpus = ₹4,37,07,000 − ₹3,23,70,000 = **₹1,13,37,000**.
**SIP:** r = 0.11 ÷ 12 = **0.0091667**, n = 26 × 12 = **312**. (1.0091667)³¹² = **16.9846**. Annuity factor = (16.9846 − 1) ÷ 0.0091667 = 15.9846 ÷ 0.0091667 = **1743.8**. PMT = 1,13,37,000 ÷ 1743.8 = **₹6,502 a month**.

So roughly **₹6,500–6,900 a month** closes the gap — option **A)**.
B) and D) massively overstate the requirement. C) Is tempting but wrong: the existing corpus reaches ₹3.24 crore against a ₹4.37 crore requirement, a real shortfall of over ₹1.1 crore.

> ⚠️ **Important caveat the exam may probe:** this calculation **ignored post-retirement inflation**. Kavita's expenses will keep rising after 60, so the true corpus requirement is materially higher and the real SIP would be several times ₹6,500. Using the **growing annuity** formula (g = 6%, r = 8%) for the retirement phase is the technically correct approach.
</details>
