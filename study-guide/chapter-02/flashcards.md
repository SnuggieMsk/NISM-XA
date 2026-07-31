# Chapter 2: Time Value of Money — Flashcards

Cover the answer, recall it, then check. **These formulas must be automatic — they reappear in Chapters 4, 9, 14 and 16.**

**Q1.** Why is a rupee today worth more than a rupee tomorrow?
> **A:** Three reasons — **opportunity cost** (it can be invested today), **inflation** (future rupees buy less), and **risk** (a future rupee may never arrive).

**Q2.** Name the five TVM variables.
> **A:** **PV, FV, r (rate per period), n (number of periods), PMT.** Give any four and the fifth is solvable.

**Q3.** State the future value of a lump sum.
> **A:** **FV = PV × (1 + r)ⁿ**

**Q4.** State the present value of a lump sum.
> **A:** **PV = FV ÷ (1 + r)ⁿ** — the same equation rearranged.

**Q5.** What is the #1 mistake in TVM calculations?
> **A:** **Period mismatch** — using an annual rate with a monthly number of periods. For monthly problems: r = annual ÷ 12 and n = years × 12.

**Q6.** State the formula for the rate of return (CAGR).
> **A:** **r = (FV ÷ PV)^(1/n) − 1**

**Q7.** State the formula for the number of periods.
> **A:** **n = ln(FV ÷ PV) ÷ ln(1 + r)**

**Q8.** State the Rule of 72 and use it: money doubled in 6 years — what was the rate?
> **A:** **Years to double ≈ 72 ÷ rate%.** Reversed: 72 ÷ 6 = **12% p.a.**

**Q9.** How long does money take to double at 8%? At 9%? At 6%?
> **A:** **9 years** at 8%; **8 years** at 9%; **12 years** at 6%.

**Q10.** Give the formula for compounding m times a year.
> **A:** **FV = PV × (1 + r/m)^(m×n)** — m = 1 annual, 2 half-yearly, 4 quarterly, 12 monthly, 365 daily.

**Q11.** State the Effective Annual Rate formula.
> **A:** **EAR = (1 + r/m)^m − 1** — the rate that, compounded once a year, gives the same result.

**Q12.** A nominal 12% compounded monthly gives what EAR?
> **A:** (1 + 0.12/12)¹² − 1 = (1.01)¹² − 1 = **12.683%**.

**Q13.** As compounding frequency rises, what happens to the nominal rate and to the effective rate?
> **A:** The **nominal rate stays the same**; only the **effective rate rises** — and by shrinking increments (annual→monthly adds 0.68pp; monthly→daily only 0.06pp).

**Q14.** What is an annuity?
> **A:** A series of **equal** cash flows at **regular** intervals — a SIP, an EMI, a pension, rent.

**Q15.** State the FV of an ordinary annuity.
> **A:** **FV = PMT × [((1 + r)ⁿ − 1) ÷ r]**

**Q16.** State the PV of an ordinary annuity.
> **A:** **PV = PMT × [(1 − (1 + r)⁻ⁿ) ÷ r]**

**Q17.** What is the difference between an ordinary annuity and an annuity due?
> **A:** **Ordinary** pays at the **end** of each period; **due** pays at the **beginning**. Each due payment is invested one extra period.

**Q18.** How do you convert an ordinary annuity value into an annuity due value?
> **A:** **Multiply by (1 + r).** This works for both PV and FV. The due value is **always higher**.

**Q19.** In Excel, what does the `type` argument do?
> **A:** `type = 0` → ordinary annuity (end of period, the default). `type = 1` → annuity due (beginning of period).

**Q20.** State the formula for PMT when you know the target FV.
> **A:** **PMT = FV × r ÷ [(1 + r)ⁿ − 1]**

**Q21.** State the formula for PMT when you know the PV (i.e. the EMI formula).
> **A:** **PMT = PV × r × (1+r)ⁿ ÷ [(1+r)ⁿ − 1]**

**Q22.** State the present value of a perpetuity.
> **A:** **PV = PMT ÷ r**

**Q23.** State the present value of a growing perpetuity, and its one condition.
> **A:** **PV = PMT₁ ÷ (r − g)**, valid only when **g < r**. If g ≥ r the value is infinite and the formula breaks.

**Q24.** ₹60,000 a year forever at an 8% discount rate — what is it worth today?
> **A:** 60,000 ÷ 0.08 = **₹7,50,000**.

**Q25.** State the real return formula.
> **A:** **Real = [(1 + nominal) ÷ (1 + inflation)] − 1** — *not* nominal minus inflation.

**Q26.** Nominal 9%, inflation 6%. What is the exact real return, and what does the crude method give?
> **A:** Exact = (1.09 ÷ 1.06) − 1 = **2.83%**. Crude subtraction gives 3%, which **overstates** it.

**Q27.** An FD yields 7%, inflation is 6%, tax is 30%. What is the post-tax real return?
> **A:** Post-tax nominal = 7% × 0.70 = 4.9%. Real = (1.049 ÷ 1.06) − 1 = **−1.04%** — the "safe" option loses purchasing power.

**Q28.** How do you convert today's goal cost into the amount actually needed?
> **A:** **Future cost = Today's cost × (1 + inflation)ⁿ.** Never target today's price.

**Q29.** State the four steps of the standard goal calculation.
> **A:** 1) **Inflate** the goal cost. 2) **Grow** the existing earmarked corpus. 3) Find the **gap**. 4) Solve for the **SIP** that fills the gap.

**Q30.** Difference between simple and compound interest, with the 20-year example?
> **A:** Simple earns on principal only (**FV = PV(1 + r×n)**); compound earns on principal *plus* accumulated interest. ₹1,00,000 at 10% for 20 years: simple **₹3,00,000**, compound **₹6,72,750**.

**Q31.** What is the Excel sign convention, and what does `#NUM!` usually mean?
> **A:** Money **paid out is negative**, money **received is positive**. `#NUM!` almost always means every value was entered with the **same sign**.

**Q32.** ₹10,000 a month for 15 years at 12% p.a. (monthly) — what is the corpus, and how much was contributed?
> **A:** r = 0.01, n = 180, (1.01)¹⁸⁰ = 5.9958. FV = 10,000 × 499.58 = **₹49,95,800**. Contributed = **₹18,00,000**; returns supplied nearly two-thirds.

**Q33.** Which Excel functions solve for each variable?
> **A:** `=FV()`, `=PV()`, `=PMT()`, `=RATE()`, `=NPER()`, plus `=EFFECT()` and `=NOMINAL()` for rate conversion.

**Q34.** ₹4,00,000 grows to ₹10,00,000 in 8 years. What is the CAGR?
> **A:** (10,00,000 ÷ 4,00,000)^(1/8) − 1 = 2.5^0.125 − 1 = **12.14% p.a.**

**Q35.** Why must you always compare deposit products on EAR rather than the headline rate?
> **A:** Two products can quote the same **nominal** rate but differ in **compounding frequency**, so their actual returns differ. Only the **effective** rate is comparable.

**Q36.** State the finite growing-annuity PV formula and where it's used.
> **A:** **PV = [PMT₁ ÷ (r − g)] × [1 − ((1+g)/(1+r))ⁿ]** — used for retirement income that must rise with inflation.

**Q37.** What are the five classic traps in this chapter?
> **A:** 1) Period mismatch. 2) Ordinary vs due confusion. 3) Real return by subtraction. 4) Forgetting to inflate the goal. 5) Comparing nominal instead of effective rates.

**Q38.** In one sentence, what is the whole chapter?
> **A:** Cash flows at different dates cannot be compared directly — move them along the time line by **compounding forward** ((1+r)ⁿ) or **discounting back** (÷(1+r)ⁿ).
