# 🔢 Financial Maths Primer — every formula in the NISM X-A syllabus

> **One page to rule the numerical half of the exam.**
> Module 1 alone is **37 marks** and is almost entirely arithmetic. Modules 3 and 5 add bond pricing, option payoffs and risk-adjusted returns. Everything numerical in the paper is on this page.

**How to use it:** don't read this once. Work each example with a spreadsheet open until you can reproduce it without looking. Then use the Quick Reference at the end as your revision sheet.

---

## 0. The two habits that prevent most lost marks

**Habit 1 — convert the period first.** Before touching a formula, ask: *is this annual or monthly?*

| If the question says | Then r = | And n = |
|---|---|---|
| 12% a year, 5 years, **annual** | 0.12 | 5 |
| 12% a year, 5 years, **monthly** | 0.12 ÷ 12 = **0.01** | 5 × 12 = **60** |
| 12% a year, 6 years, **half-yearly** | 0.12 ÷ 2 = **0.06** | 6 × 2 = **12** |
| 10% a year, 8 years, **quarterly** | 0.10 ÷ 4 = **0.025** | 8 × 4 = **32** |

> ⚠️ Mixing an annual rate with monthly periods is the single most common error in the whole paper. **r and n must always describe the same period.**

**Habit 2 — read what is actually being asked.** Distractors are built from the *near misses*:

| Asked for | Common distractor offered |
|---|---|
| The EMI | The **first month's interest**, or principal ÷ n |
| The corpus | The **total contributed** (ignoring returns) |
| The interest paid | The **total repaid** (including principal) |
| The gap/shortfall | The **grown corpus** itself |
| The real return | Nominal **minus** inflation (crude subtraction) |
| CAGR | Total gain ÷ years (simple-interest thinking) |

---

## 1. Time Value of Money — the engine (Chapter 2)

Everything below is one equation rearranged five ways.

$$FV = PV \times (1+r)^n$$

| Solve for | Formula | Excel |
|---|---|---|
| **Future value** | FV = PV × (1+r)ⁿ | `=FV(rate,nper,pmt,pv,type)` |
| **Present value** | PV = FV ÷ (1+r)ⁿ | `=PV(rate,nper,pmt,fv,type)` |
| **Rate (CAGR)** | r = (FV ÷ PV)^(1/n) − 1 | `=RATE(nper,pmt,pv,fv)` |
| **Periods** | n = ln(FV ÷ PV) ÷ ln(1+r) | `=NPER(rate,pmt,pv,fv)` |

**Worked:** ₹4,00,000 grows to ₹10,00,000 in 8 years.
r = (10,00,000 ÷ 4,00,000)^(1/8) − 1 = 2.5^0.125 − 1 = 1.1214 − 1 = **12.14% p.a.**

### The Rule of 72

$$\text{Years to double} \approx \frac{72}{\text{rate }\%}$$

| Rate | Doubles in | Rate | Doubles in |
|---|---|---|---|
| 6% | 12 years | 9% | 8 years |
| 7.2% | 10 years | 12% | 6 years |
| 8% | 9 years | 18% | 4 years |

Use it **in reverse** as a sanity check: "money quadrupled in 12 years" = two doublings = 6 years each ≈ 12% p.a.

### Simple vs compound

| | Formula | ₹1,00,000 at 10% for 20 years |
|---|---|---|
| Simple | FV = PV(1 + r×n) | **₹3,00,000** |
| Compound | FV = PV(1+r)ⁿ | **₹6,72,750** |

---

## 2. Compounding frequency and effective rates

$$FV = PV \times \left(1 + \frac{r}{m}\right)^{m \times n} \qquad EAR = \left(1 + \frac{r}{m}\right)^{m} - 1$$

**A nominal 12%, one year, ₹1,00,000:**

| Frequency | m | EAR | Value |
|---|---|---|---|
| Annual | 1 | 12.000% | ₹1,12,000 |
| Half-yearly | 2 | 12.360% | ₹1,12,360 |
| Quarterly | 4 | 12.551% | ₹1,12,551 |
| Monthly | 12 | 12.683% | ₹1,12,683 |
| Daily | 365 | 12.747% | ₹1,12,747 |
| Continuous | ∞ | 12.750% (e^r − 1) | ₹1,12,750 |

> 🧠 The **nominal rate never changes** — only the effective rate rises, and by shrinking amounts. **Always compare deposits on EAR.** Excel: `=EFFECT(nominal, periods)` and `=NOMINAL(effective, periods)`.

---

## 3. Annuities — regular payments (Chapter 2)

An **annuity** = equal cash flows at equal intervals (a SIP, an EMI, a pension).

$$FV_{ord} = PMT \times \frac{(1+r)^n - 1}{r} \qquad PV_{ord} = PMT \times \frac{1 - (1+r)^{-n}}{r}$$

$$\boxed{\text{Annuity DUE} = \text{Annuity ORDINARY} \times (1+r)}$$

**Ordinary** = paid at the **end** of each period (the default). **Due** = paid at the **beginning**, so every payment earns one extra period → always worth more.

**Worked (FV):** ₹10,000 a month, 15 years, 12% p.a. monthly.
r = 0.01, n = 180, (1.01)¹⁸⁰ = **5.9958**
FV = 10,000 × [(5.9958 − 1) ÷ 0.01] = 10,000 × **499.58** = **₹49,95,800**
*(Contributed ₹18,00,000 — so returns supplied ₹31,95,800, nearly two-thirds.)*

### Solving for the payment

| You know | Formula | Excel |
|---|---|---|
| The **target corpus** (FV) | PMT = FV × r ÷ [(1+r)ⁿ − 1] | `=PMT(rate,nper,0,fv)` |
| The **loan amount** (PV) — the EMI | PMT = PV × r(1+r)ⁿ ÷ [(1+r)ⁿ − 1] | `=PMT(rate,nper,-pv)` |

### Perpetuity

$$PV = \frac{PMT}{r} \qquad\text{growing: } PV = \frac{PMT_1}{r-g}\ \ (\text{needs } g<r)$$

₹60,000 a year forever at 8% → 60,000 ÷ 0.08 = **₹7,50,000**.
Growing at 4% → 60,000 ÷ (0.08 − 0.04) = **₹15,00,000**.

---

## 4. Inflation and real returns

$$\boxed{\text{Real return} = \frac{1 + \text{nominal}}{1 + \text{inflation}} - 1} \qquad \text{Future cost} = \text{Today's cost} \times (1+i)^n$$

**Nominal 9%, inflation 6%:** (1.09 ÷ 1.06) − 1 = **2.83%** — *not* 3%.

**The post-tax reality check.** An FD at 7%, inflation 6%, tax 30%:
- Post-tax nominal = 7% × 0.70 = **4.9%**
- Real = (1.049 ÷ 1.06) − 1 = **−1.04%**

The "safe" investment **loses purchasing power**. Always compute in this order: **tax first, then deflate.**

Reversed, to find the nominal return a goal needs:
$$\text{Nominal} = (1+\text{real})(1+\text{inflation}) - 1$$

---

## 5. ⭐ The four-step goal calculation

Every goal caselet in the exam is this, and only this:

| Step | Do | Formula |
|---|---|---|
| **1** | Inflate the goal to its future cost | Cost × (1 + i)ⁿ |
| **2** | Grow what is already earmarked | Existing × (1 + r)ⁿ |
| **3** | Find the gap | Step 1 − Step 2 |
| **4** | Annuitise the gap | PMT = Gap × r ÷ [(1+r)ⁿ − 1] |

**Worked.** Education costing ₹20,00,000 today, needed in 10 years, inflation 7%. Already saved ₹5,00,000. Expected return 11% p.a. (monthly).

1. Future cost = 20,00,000 × (1.07)¹⁰ = 20,00,000 × 1.9672 = **₹39,34,400**
2. Existing grows = 5,00,000 × (1.11)¹⁰ = 5,00,000 × 2.8394 = **₹14,19,700**
3. Gap = **₹25,14,700**
4. r = 0.0091667, n = 120, (1.0091667)¹²⁰ = 2.9853
   PMT = (25,14,700 × 0.0091667) ÷ 1.9853 = **₹11,611 a month**

---

## 6. Loans and amortisation (Chapter 4)

$$EMI = P \times \frac{r(1+r)^n}{(1+r)^n - 1} \qquad \text{Total interest} = (EMI \times n) - P$$

**Worked:** ₹40,00,000 at 9% for 20 years. r = 0.0075, n = 240, (1.0075)²⁴⁰ = **6.00915**
EMI = 40,00,000 × (0.0075 × 6.00915) ÷ 5.00915 = **₹35,989**
Total interest = (35,989 × 240) − 40,00,000 = **₹46,37,360** — more than the loan itself.

### The amortisation split each month

| Component | Formula |
|---|---|
| Interest | Outstanding balance × monthly rate |
| Principal | EMI − interest |
| New balance | Old balance − principal repaid |

**Month 1 of the loan above:** interest = 40,00,000 × 0.0075 = **₹30,000**; principal = 35,989 − 30,000 = **₹5,989**.
**83% of the first EMI is interest** — which is why early prepayment saves so much, and why a borrower halfway through a 20-year loan has repaid only about a third of the principal.

### Outstanding balance at any point
$$\text{Outstanding} = EMI \times \frac{1 - (1+r)^{-m}}{r} \quad (m = \text{months remaining})$$

### Prepay or invest?
Compare the **loan rate** with the **post-tax expected return**. Repaying is a **risk-free, tax-free return equal to the interest rate**. A certain 11% beats an expected 10%.

---

## 7. Financial position ratios (Chapter 3)

| Ratio | Formula | Healthy | Unit |
|---|---|---|---|
| Savings | Savings ÷ Gross income | ≥ 20% | % |
| Expenses | Expenses ÷ Gross income | ≤ 80% | % |
| Leverage | Total liabilities ÷ Total assets | < 0.5 | decimal |
| Solvency | Net worth ÷ Total assets | > 0.5 | decimal |
| Liquidity | Liquid assets ÷ **Monthly** expenses | 3–6 | **months** |
| Financial assets | Financial assets ÷ Total assets | higher | % |
| Debt-to-income | Total EMIs ÷ Gross income | < 35–40% | % |

**Three self-checks that catch most errors:**
1. Savings % + Expenses % = **100**
2. Solvency + Leverage = **1**
3. Liquidity is in **months** — a percentage-looking answer means you divided by the wrong thing

> ⚠️ If given **annual** expenses, divide by 12 before computing liquidity. And **equity and PPF are not liquid assets.**

---

## 8. Bond maths (Chapter 9)

$$P = C \times \frac{1-(1+y)^{-n}}{y} + \frac{F}{(1+y)^n}$$

A bond is just an **annuity (the coupons) plus a lump sum (the redemption)**.

| Situation | Adjustment |
|---|---|
| Semi-annual | **Halve** C and y, **double** n |
| Zero-coupon | P = F ÷ (1+y)ⁿ |
| Perpetual | P = C ÷ y |
| Between coupons | Dirty price = clean price + accrued interest |

**Worked:** ₹1,000 face, 8% annual coupon, 5 years, required yield 10%.
Annuity factor = (1 − 1.10⁻⁵) ÷ 0.10 = **3.7908**; PV of coupons = 80 × 3.7908 = ₹303.26
PV of redemption = 1,000 ÷ 1.61051 = ₹620.92 → **Price ₹924.18** (a discount, because 8% < 10%).

### Price, coupon and yield

| Coupon vs required yield | Price | Ordering |
|---|---|---|
| Coupon **>** yield | **Premium** | Coupon > Current yield > YTM |
| Coupon **=** yield | **Par** | All three equal |
| Coupon **<** yield | **Discount** | Coupon < Current yield < **YTM** |

**Current yield** = annual coupon ÷ **market price**. **YTM** = the rate equating PV of all cash flows to price (assumes coupons reinvested at the YTM and held to maturity).

**Approximate YTM** (handy when no calculator function is allowed):
$$YTM \approx \frac{C + (F-P)/n}{(F+P)/2}$$

### Duration
$$\text{Modified duration} = \frac{\text{Macaulay duration}}{1+y} \qquad \boxed{\%\Delta P \approx -\text{MD} \times \Delta y}$$

- **A zero-coupon bond's Macaulay duration = its maturity.** (Most-tested duration fact.)
- Longer maturity → **higher** duration. Higher coupon → **lower** duration.
- Expect rates to **fall** → go **long** duration.

**Worked:** MD 6.2, yields rise 0.75% → −6.2 × 0.0075 = **−4.65%**. On ₹10,00,000 that is a **₹46,500** loss.

---

## 9. Equity valuation (Chapter 8)

| Ratio | Formula | Breaks when |
|---|---|---|
| P/E | Price ÷ EPS | Earnings are **negative** |
| Earnings yield | EPS ÷ Price (= 1 ÷ P/E) | — |
| P/B | Price ÷ Book value per share | Assets are intangible |
| P/S | Price ÷ Sales per share | Ignores profitability entirely |
| PEG | P/E ÷ growth % | Growth forecast is unreliable (**<1** = attractive) |
| EV | Market cap + Debt − Cash | — |
| EV/EBITDA | EV ÷ EBITDA | — (capital-structure neutral) |
| Dividend yield | DPS ÷ Price | A **falling price** inflates it |
| EVA | NOPAT − (Capital × Cost of capital) | — (positive = real value created) |

**DCF:** Value = Σ CFₜ ÷ (1+r)ᵗ + TV ÷ (1+r)ⁿ, where **TV = CF ÷ (r − g)** and **g must be < r**.

---

## 10. Option payoffs (Chapter 10)

| Position | Max gain | Max loss | Break-even |
|---|---|---|---|
| **Long call** | Unlimited | Premium | **Strike + Premium** |
| **Long put** | Large (capped) | Premium | **Strike − Premium** |
| **Short call** | Premium | **UNLIMITED** ⚠️ | Strike + Premium |
| **Short put** | Premium | Large (capped) | Strike − Premium |

**Intrinsic value:** Call = max(Spot − Strike, 0) · Put = max(Strike − Spot, 0). **Time value** = Premium − Intrinsic, and it decays to **zero** at expiry.

**Futures fair value:** F = S × (1 + r − q)^T. Normally **F > S** (contango), and **F converges to S at expiry**.

> ⚠️ **ITM ≠ profitable.** A call struck at ₹1,000 bought for ₹40 with spot at ₹1,020 has ₹20 of intrinsic value but **loses ₹20** — the premium must be recovered first.

---

## 11. Portfolio risk and return (Chapters 14 & 16)

### Expected return and risk

$$E(R_p) = \sum w_i R_i \qquad \sigma_p = \sqrt{w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\sigma_1\sigma_2\rho_{12}}$$

Portfolio **return** is a simple weighted average. Portfolio **risk is not** — it is lower than the weighted average whenever **ρ < 1**. That gap is the entire benefit of diversification.

### Return measures

| Measure | Formula | Use |
|---|---|---|
| Holding period return | (End − Start + Income) ÷ Start | Single period |
| CAGR / geometric mean | (End ÷ Start)^(1/n) − 1 | **Compounded** growth |
| Arithmetic mean | Simple average of returns | **Always ≥ GMR**; gap widens with volatility |
| Annualising | (1 + HPR)^(1/years) − 1 | Converting a part-year return |
| TWRR | Chain-links sub-period returns | Measures the **manager** (removes client cash flows) |
| MWRR | The IRR of all cash flows | Measures the **investor's** actual experience |

### Risk-adjusted measures

| Measure | Formula | Divides by |
|---|---|---|
| **Sharpe** | (Rp − Rf) ÷ σp | **Total** risk |
| **Treynor** | (Rp − Rf) ÷ βp | **Systematic** risk |
| **Sortino** | (Rp − Rf) ÷ downside deviation | **Downside** risk only |
| **Information ratio** | Alpha ÷ Tracking error | Active risk |
| **Alpha (Jensen)** | Rp − [Rf + β(Rm − Rf)] | — |

**CAPM:** Required return = Rf + β × (Rm − Rf).

> 🧠 **Sharpe vs Treynor:** use **Sharpe** for a whole portfolio (total risk matters), **Treynor** for one sleeve of an already-diversified portfolio (only its systematic contribution matters).

---

## 📋 Quick Reference — everything on one screen

| # | Need | Formula |
|---|---|---|
| 1 | Future value | PV × (1+r)ⁿ |
| 2 | Present value | FV ÷ (1+r)ⁿ |
| 3 | CAGR / rate | (FV÷PV)^(1/n) − 1 |
| 4 | Periods | ln(FV÷PV) ÷ ln(1+r) |
| 5 | Rule of 72 | Years to double ≈ 72 ÷ rate% |
| 6 | Non-annual compounding | PV × (1 + r/m)^(mn) |
| 7 | Effective annual rate | (1 + r/m)^m − 1 |
| 8 | FV of annuity | PMT × [((1+r)ⁿ − 1) ÷ r] |
| 9 | PV of annuity | PMT × [(1 − (1+r)⁻ⁿ) ÷ r] |
| 10 | Annuity due | Ordinary × (1+r) |
| 11 | PMT from target | FV × r ÷ [(1+r)ⁿ − 1] |
| 12 | EMI | P × r(1+r)ⁿ ÷ [(1+r)ⁿ − 1] |
| 13 | Total interest | (EMI × n) − P |
| 14 | Monthly interest | Outstanding × r |
| 15 | Outstanding balance | PV of remaining EMIs |
| 16 | Perpetuity | PMT ÷ r |
| 17 | Growing perpetuity | PMT₁ ÷ (r − g), g < r |
| 18 | Real return | [(1+nom) ÷ (1+inf)] − 1 |
| 19 | Future goal cost | Cost × (1 + i)ⁿ |
| 20 | Nominal from real | (1+real)(1+inf) − 1 |
| 21 | Savings ratio | Savings ÷ Income |
| 22 | Solvency ratio | Net worth ÷ Assets |
| 23 | Leverage ratio | Liabilities ÷ Assets |
| 24 | Liquidity ratio | Liquid ÷ **Monthly** expenses |
| 25 | Debt-to-income | EMIs ÷ Income |
| 26 | Bond price | C×[(1−(1+y)⁻ⁿ)÷y] + F÷(1+y)ⁿ |
| 27 | Current yield | Coupon ÷ Market price |
| 28 | Approx YTM | [C + (F−P)/n] ÷ [(F+P)/2] |
| 29 | Modified duration | Macaulay ÷ (1+y) |
| 30 | Bond price change | ≈ −MD × Δy |
| 31 | Enterprise value | Mkt cap + Debt − Cash |
| 32 | Earnings yield | EPS ÷ Price |
| 33 | PEG | P/E ÷ growth% |
| 34 | EVA | NOPAT − (Capital × WACC) |
| 35 | DCF terminal value | CF ÷ (r − g) |
| 36 | Call break-even | Strike + Premium |
| 37 | Put break-even | Strike − Premium |
| 38 | Call intrinsic | max(Spot − Strike, 0) |
| 39 | Futures fair value | S × (1 + r − q)^T |
| 40 | Portfolio return | Σ wᵢRᵢ |
| 41 | Two-asset risk | √(w₁²σ₁² + w₂²σ₂² + 2w₁w₂σ₁σ₂ρ) |
| 42 | CAPM | Rf + β(Rm − Rf) |
| 43 | Sharpe | (Rp − Rf) ÷ σ |
| 44 | Treynor | (Rp − Rf) ÷ β |
| 45 | Alpha | Rp − [Rf + β(Rm − Rf)] |
| 46 | Information ratio | Alpha ÷ Tracking error |
| 47 | NAV | (Assets − Liabilities) ÷ Units |

---

## The five traps that cost the most marks

1. **Period mismatch** — annual rate with monthly periods. Convert *both*.
2. **Forgetting to inflate the goal** — today's cost is never the target.
3. **Real return by subtraction** — use the division formula; and **tax before deflating**.
4. **Ordinary vs due** — "beginning of the period" means × (1+r).
5. **Answering the wrong quantity** — total repaid instead of interest, contributions instead of corpus, the grown corpus instead of the gap.

> **In the exam:** the test machine has a spreadsheet. Before you start, type `=PMT(`, `=FV(`, `=PV(`, `=RATE(` once each to confirm they work. Then convert every rate to its per-period value **before** you touch a formula.
