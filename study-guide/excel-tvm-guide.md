# 🧮 The Spreadsheet Guide — Every Calculation the X-A Exam Can Throw At You

> **Why this file exists.** The NISM test centre gives you a spreadsheet, not a financial calculator. Candidates lose marks not because they don't know the formula but because they fumble the *signs*, the *rate units*, or the *annuity-due switch* under time pressure. This guide makes those three things automatic.
>
> Everything here works identically in **Microsoft Excel**, **LibreOffice Calc**, **Google Sheets** and **WPS Spreadsheets**. The NISM test machine typically ships with LibreOffice Calc.

---

## Part 0 — The 90-second setup you do at the start of the exam

Before you attempt a single numerical question, build this in the spreadsheet. It takes a minute and it pays for itself on question three.

| Cell | Put this in | Why |
|------|-------------|-----|
| A1 | `rate` | label |
| B1 | *(leave blank)* | you'll type the periodic rate here |
| A2 | `nper` | label |
| B2 | *(blank)* | number of periods |
| A3 | `pmt` | label |
| B3 | *(blank)* | payment per period |
| A4 | `pv` | label |
| B4 | *(blank)* | present value |
| A5 | `fv` | label |
| B5 | *(blank)* | future value |
| A6 | `type` | label |
| B6 | `0` | 0 = end of period (ordinary), 1 = beginning (due) |

Then in **B8** put:

```
=FV(B1,B2,B3,B4,B6)
```

and in **B9**:

```
=PV(B1,B2,B3,B5,B6)
```

and in **B10**:

```
=PMT(B1,B2,B4,B5,B6)
```

and in **B11**:

```
=RATE(B2,B3,B4,B5,B6)
```

and in **B12**:

```
=NPER(B1,B3,B4,B5,B6)
```

Now every TVM question is: *fill in the four you know, read the one you don't.* You never retype a formula again.

> ⚠️ **The one trap in this setup:** a blank cell is read as `0`. If a question has no PMT, leaving B3 blank is correct. But if a question has no PV and you leave B4 from the *previous* question sitting there, your answer will be wrong and look plausible. **Clear B1:B6 between questions.** Select B1:B6 → `Delete`. Two keystrokes. Do it every single time.

---

## Part 1 — The sign convention (this is where most marks are lost)

Spreadsheets treat money as a **cash flow**, not a quantity. So:

- Money **leaving your pocket** → **negative**
- Money **coming into your pocket** → **positive**

That is the *entire* rule. Everything else follows.

### What that means in practice

| Situation | PV | PMT | FV |
|---|---|---|---|
| You invest ₹1,00,000 today and it grows | `-100000` (you paid it out) | 0 | *result comes out positive* |
| You save ₹5,000 a month towards a goal | 0 | `-5000` (you pay it out) | *result positive* |
| You take a ₹30,00,000 home loan | `30000000` (bank gave it to you) | *result negative* — you pay the EMI | 0 |
| You want ₹50,00,000 in 15 years, how much monthly? | 0 | *result negative* | `50000000` |

### The lazy shortcut that always works

If you don't want to think about signs at all, **wrap the formula in `ABS()`** and reason about the direction yourself:

```
=ABS(PMT(8%/12, 240, 3000000))
```

This returns the EMI as a clean positive number. The exam options are always positive rupee amounts, so `ABS()` costs you nothing and saves you from a minus-sign disaster.

> **But** — and this matters — `ABS()` only saves you when there is **one** outflow and **one** inflow. The moment a question has *both* a lump sum **and** a stream of payments (e.g. "you have ₹5 lakh today and will add ₹10,000 a month"), the signs of PV and PMT must **agree with each other** (both negative, if both are money you're putting in). Get that wrong and `ABS()` will happily return a confidently wrong number.

**The rule to memorise: PV and PMT flowing the same direction take the same sign.**

---

## Part 2 — The rate and period units (the second-biggest mark-loser)

**`rate` and `nper` must be in the same unit.** Always. No exceptions.

| The question says | rate | nper |
|---|---|---|
| 12% p.a., 5 years, **annual** compounding | `12%` | `5` |
| 12% p.a., 5 years, **monthly** compounding/payments | `12%/12` | `5*12` |
| 12% p.a., 5 years, **quarterly** | `12%/4` | `5*4` |
| 12% p.a., 5 years, **half-yearly** | `12%/2` | `5*2` |
| 9% p.a. on a 20-year home loan (EMI is monthly) | `9%/12` | `20*12` |

Write the arithmetic **into the formula** — `12%/12`, not `0.01`. It documents itself, and if you misread the tenure you fix one number instead of recomputing a decimal.

> 🎯 **Exam tip:** whenever a question mentions **EMI**, **SIP**, or **monthly**, your rate is divided by 12 and your nper is multiplied by 12. Make that reflexive.

---

## Part 3 — The core five functions

### `FV` — what will it grow to?

```
=FV(rate, nper, pmt, [pv], [type])
```

**Q: ₹2,00,000 invested for 8 years at 11% p.a. What is the maturity value?**

```
=FV(11%, 8, 0, -200000)          →  ₹4,60,910
```

**Q: ₹10,000 a month for 15 years at 12% p.a. What is the corpus?**

```
=FV(12%/12, 15*12, -10000, 0)    →  ₹49,95,800
```

**Q: Both — ₹5,00,000 today *plus* ₹10,000 a month, 15 years, 12%.**

```
=FV(12%/12, 15*12, -10000, -500000)   →  ₹79,93,700
```

*(Note both are negative — both are money you put in.)*

---

### `PV` — what is it worth today?

```
=PV(rate, nper, pmt, [fv], [type])
```

**Q: You need ₹40,00,000 in 12 years. At 9%, what lump sum today gets you there?**

```
=ABS(PV(9%, 12, 0, 4000000))     →  ₹14,22,140
```

**Q: A pension pays ₹30,000 a month for 20 years. At 8%, what is it worth today?**

```
=ABS(PV(8%/12, 20*12, 30000))    →  ₹35,86,630
```

---

### `PMT` — how much per period?

```
=PMT(rate, nper, pv, [fv], [type])
```

This is the **EMI function** and the **SIP function**. Same formula, different story.

**Q (EMI): ₹35,00,000 home loan, 9% p.a., 20 years. EMI?**

```
=ABS(PMT(9%/12, 20*12, 3500000))     →  ₹31,490
```

**Q (SIP): You need ₹1,00,00,000 in 18 years at 12%. Monthly SIP?**

```
=ABS(PMT(12%/12, 18*12, 0, 10000000)) →  ₹13,195
```

> Note where the target goes: for a **loan** the amount is `pv` (you have the money now, you owe it). For a **goal** the amount is `fv` (you don't have it, you want it later). Putting the goal in the wrong slot is the single most common SIP-question error.

---

### `RATE` — what return does this imply?

```
=RATE(nper, pmt, pv, [fv], [type])
```

**Q: ₹5,00,000 grows to ₹9,00,000 in 7 years. What is the CAGR?**

```
=RATE(7, 0, -500000, 900000)     →  8.76%
```

**Q: You pay ₹25,000 a month for 5 years and receive ₹20,00,000. What return is that?**

```
=RATE(5*12, -25000, 0, 2000000)  →  0.9356% per month
```

⚠️ **`RATE` returns the rate *per period*.** That answer is monthly. To annualise it the exam way:

```
=RATE(5*12, -25000, 0, 2000000)*12        →  11.23% nominal annual
=(1+RATE(5*12,-25000,0,2000000))^12-1     →  11.82% effective annual
```

Read the question: "annual rate" usually means the **nominal** (×12) figure; "effective annual return" means the **compounded** one.

> 💡 `RATE` is solved iteratively and occasionally returns `#NUM!` if it can't converge. Add a guess as the 6th argument: `=RATE(nper, pmt, pv, fv, type, 0.1)`.

---

### `NPER` — how long will it take?

```
=NPER(rate, pmt, pv, [fv], [type])
```

**Q: ₹3,00,000 at 10% p.a. — how long to double?**

```
=NPER(10%, 0, -300000, 600000)   →  7.27 years
```

*(Sanity check with the Rule of 72: 72 ÷ 10 = 7.2. Close. Good.)*

**Q: ₹8,00,000 credit-card debt at 18% p.a., paying ₹20,000 a month. How many months?**

```
=NPER(18%/12, -20000, 800000)    →  61.5 months  (≈ 5 years 2 months)
```

---

## Part 4 — Annuity due (the `type` argument)

The 5th argument of `FV`/`PV` and the 5th of `PMT` is `type`:

- `0` or omitted → **ordinary annuity** — payment at the **end** of each period
- `1` → **annuity due** — payment at the **beginning** of each period

**When is it due?** Rent, insurance premiums, lease payments, and *most SIPs* are paid at the **start** of the period. Loan EMIs are paid at the **end**.

**Q: ₹10,000 a month for 10 years at 12%, paid at the beginning of each month.**

```
=FV(12%/12, 10*12, -10000, 0, 1)    →  ₹23,23,391
=FV(12%/12, 10*12, -10000, 0, 0)    →  ₹23,00,387
```

The difference — **₹23,004** — is exactly **one period's interest** on the whole corpus: `23,00,387 × 1% = 23,004`. That is not a coincidence, it is the identity below.

> ✅ **The identity worth memorising:** `Annuity due = Ordinary annuity × (1 + r)`. If you forget the `type` argument entirely, you can still fix an ordinary-annuity answer by multiplying by `(1+r)`. This appears in the exam as a standalone conceptual question, so know it as a formula *and* as a spreadsheet switch.

---

## Part 5 — Rates: nominal, effective, and real

### Effective annual rate from a nominal rate

```
=EFFECT(nominal_rate, npery)
```

**Q: 12% p.a. compounded monthly — what is the effective rate?**

```
=EFFECT(12%, 12)            →  12.6825%
=(1+12%/12)^12-1            →  12.6825%   (same thing, done manually)
```

### Nominal from effective (the reverse)

```
=NOMINAL(effective_rate, npery)
```

**Q: You need an effective 15%. What nominal rate compounded quarterly delivers it?**

```
=NOMINAL(15%, 4)            →  14.2232%
```

### Real (inflation-adjusted) return — **the formula the exam actually wants**

```
=(1+nominal)/(1+inflation)-1
```

**Q: Investment returns 11%, inflation is 6%. Real return?**

```
=(1+11%)/(1+6%)-1           →  4.717%
```

⚠️ **Not 5%.** The exam deliberately offers 5% as a distractor for candidates who subtract. Subtracting is an approximation that is only acceptable when both numbers are small; NISM tests the exact formula.

### The goal calculation — inflate first, then discount

This is the classic 5-mark caselet, and it is always the same two steps.

**Q: A child's education costs ₹15,00,000 today. It is 12 years away, education inflation is 9%, and you can earn 12%. What monthly SIP is needed?**

**Step 1 — inflate the goal to what it will actually cost on the day:**
```
B1: =FV(9%, 12, 0, -1500000)            →  ₹42,18,997
```

**Step 2 — solve for the SIP that reaches *that* number at your nominal return:**
```
B2: =ABS(PMT(12%/12, 12*12, 0, B1))     →  ₹13,223
```

**Answer: about ₹13,220 a month.** Two cells, no algebra.

> ⚠️ **A warning about the "just use the real rate" shortcut.** You will see people compute `real = (1.12/1.09)−1 = 2.752%` and run `PMT` on today's ₹15,00,000. That gives about **₹8,890** — and it is *not* an alternative route to the same answer. It answers a **different question**: it is the *first* instalment of a SIP that you **escalate by 9% every year** (rising to roughly ₹22,940 by the final year). Both plans reach the goal; they are different products.
>
> **NISM asks for the level SIP.** Unless a question explicitly says the investment is "stepped up" or "increased annually with income", inflate the goal and use the **nominal** rate — Step 1 then Step 2, every time.

---

## Part 6 — Loans and amortisation

### The EMI

```
=ABS(PMT(annual_rate/12, years*12, loan_amount))
```

### How much of *this month's* EMI is interest vs principal?

```
=IPMT(rate, per, nper, pv)      ← interest portion of payment number `per`
=PPMT(rate, per, nper, pv)      ← principal portion of payment number `per`
```

**Q: ₹30,00,000 at 8.5% for 20 years. Split the 1st and the 120th EMI.**

```
=ABS(PMT (8.5%/12,      20*12, 3000000))   →  ₹26,035   the EMI itself
=ABS(IPMT(8.5%/12, 1,   20*12, 3000000))   →  ₹21,250   interest
=ABS(PPMT(8.5%/12, 1,   20*12, 3000000))   →  ₹4,785    principal
=ABS(IPMT(8.5%/12, 120, 20*12, 3000000))   →  ₹14,952   interest
=ABS(PPMT(8.5%/12, 120, 20*12, 3000000))   →  ₹11,083   principal
```

**Read that.** In month 1, **82%** of the EMI is interest. By month 120 it's still **57%**. That shifting mix is the whole point of an amortisation schedule and it's a standard conceptual question: *"In the early years of a home loan, the EMI consists mainly of ____."* Answer: **interest**.

`IPMT + PPMT = PMT` always. Use that as your check.

### Total interest paid over the life of a loan

```
=ABS(PMT(rate,nper,pv))*nper - pv
```

**Q: ₹30,00,000 at 8.5% for 20 years — total interest?**

```
=ABS(PMT(8.5%/12,240,3000000))*240 - 3000000   →  ₹32,48,000
```

You pay **more in interest than you borrowed**. This is the number that makes prepayment questions make sense.

### Outstanding balance after *k* payments

```
=ABS(FV(rate, k, PMT(rate,nper,pv), -pv))
```

Or, more readably, the PV of the remaining payments:

```
=ABS(PV(rate, nper-k, PMT(rate,nper,pv)))
```

**Q: ₹30,00,000 at 8.5% / 20 years. Outstanding after 5 years?**

```
=ABS(PV(8.5%/12, 240-60, ABS(PMT(8.5%/12,240,3000000))))   →  ₹26,43,800
```

After paying for a quarter of the tenure you've retired barely **12%** of the principal. That's the amortisation curve, and it's why prepaying **early** saves so much more than prepaying late.

### Cumulative interest / principal over a range

```
=CUMIPMT(rate, nper, pv, start_period, end_period, type)
=CUMPRINC(rate, nper, pv, start_period, end_period, type)
```

**Q: Interest paid in years 1–5 of that loan?**

```
=ABS(CUMIPMT(8.5%/12, 240, 3000000, 1, 60, 0))   →  ₹12,05,900
```

---

## Part 7 — Uneven cash flows: `NPV`, `IRR` and `XIRR`

Every function so far assumes **equal** payments. Real portfolios don't work that way.

### `NPV` — present value of an uneven stream

```
=NPV(rate, value1, value2, ...)
```

⚠️ **The single most misunderstood function in the whole exam.** Excel's `NPV` discounts the **first** value by one period — it assumes cash flows start at the **end of period 1**. So if you have an initial investment at **time 0**, it must sit *outside* the function:

```
=C0 + NPV(rate, C1:Cn)
```

where `C0` is negative (your outlay).

**Q: Invest ₹10,00,000 now; receive ₹3,00,000 / ₹4,00,000 / ₹5,00,000 over three years. At 10%, is it worth doing?**

```
A1: -1000000
A2:  300000
A3:  400000
A4:  500000

=A1 + NPV(10%, A2:A4)       →  ₹−21,037  → reject, NPV is negative
```

If you had written `=NPV(10%, A1:A4)` you'd get **−₹19,124** — wrong, because it discounts the time-0 outlay by a year it shouldn't.

### `IRR` — the rate that makes NPV zero

```
=IRR(values, [guess])
```

Values **must** include the time-0 outflow, and they **must** be evenly spaced.

```
=IRR(A1:A4)                 →  8.90%
```

Since IRR (8.90%) < required return (10%), reject — consistent with the negative NPV. **NPV and IRR always agree on accept/reject for a simple project.** That consistency is itself an exam question.

### `XIRR` — the one you'll actually use for a client portfolio

```
=XIRR(values, dates, [guess])
```

Real investments happen on **arbitrary dates**. `XIRR` handles that and returns an **annualised effective** rate.

```
        A                B
1   01-04-2021      -100000
2   15-09-2021       -50000
3   20-01-2023       -75000
4   31-03-2025       280000     ← final value, positive

=XIRR(B1:B4, A1:A4)         →  6.81% p.a.
```

> 🎯 **This is the function to know for the portfolio-evaluation chapters.** When a client asks "what return did I actually get on my SIP?", `XIRR` is the answer — it is the money-weighted return. Contrast it with **TWRR**, which strips out the timing of cash flows to measure the *manager's* skill. NISM asks you to distinguish the two: **XIRR/MWRR judges the investor's outcome; TWRR judges the manager.**

### `MIRR` — when reinvestment rate ≠ IRR

```
=MIRR(values, finance_rate, reinvest_rate)
```

Know that it exists and *why*: plain IRR implicitly assumes interim cash flows are reinvested at the IRR itself, which is often unrealistic. MIRR lets you set a realistic reinvestment rate. That "unrealistic reinvestment assumption" is IRR's standard textbook criticism.

---

## Part 8 — Returns: CAGR, absolute, annualised

| Measure | Formula | When to use |
|---|---|---|
| **Absolute return** | `=(End-Begin)/Begin` | Holding period ≤ 1 year, or when the question says "total return" |
| **CAGR** | `=(End/Begin)^(1/years)-1` | Holding period > 1 year, single in / single out |
| **Annualised (short period)** | `=(1+absolute)^(365/days)-1` | Converting a 4-month return to annual |
| **XIRR** | `=XIRR(...)` | Multiple, irregular cash flows |

**Q: ₹1,00,000 becomes ₹1,75,000 in 6 years. CAGR?**

```
=(175000/100000)^(1/6)-1    →  9.78%
```

**Q: 8% return earned over 5 months. Annualised?**

```
=(1+8%)^(12/5)-1            →  20.3%
```

### Holding-period return with income

```
=(End - Begin + Income)/Begin
```

A stock bought at ₹450, sold at ₹520, paying ₹12 dividend:
```
=(520-450+12)/450           →  18.22%
```

---

## Part 9 — Bonds

| Want | Function |
|---|---|
| Price from yield | `=PRICE(settlement, maturity, coupon, yld, redemption, frequency, [basis])` |
| Yield from price | `=YIELD(settlement, maturity, coupon, pr, redemption, frequency, [basis])` |
| Macaulay duration | `=DURATION(settlement, maturity, coupon, yld, frequency, [basis])` |
| Modified duration | `=MDURATION(settlement, maturity, coupon, yld, frequency, [basis])` |
| Accrued interest | `=ACCRINT(issue, first_interest, settlement, rate, par, frequency, [basis])` |

**Q: A bond maturing 31-Mar-2032, 7.5% coupon paid half-yearly, yielding 8%, settling 01-Apr-2025. Price per ₹100 face?**

```
=PRICE(DATE(2025,4,1), DATE(2032,3,31), 7.5%, 8%, 100, 2)   →  ₹97.35  (approx)
```

Yield (8%) > coupon (7.5%) → the bond trades at a **discount** (below ₹100). Always sanity-check that direction:

| Relationship | Bond trades at |
|---|---|
| Coupon > Yield | **Premium** (above par) |
| Coupon = Yield | **Par** |
| Coupon < Yield | **Discount** (below par) |

### The duration question, done without dates

Most exam bond questions give you duration directly and ask for the price change:

```
% price change ≈ −Modified duration × Δyield (in decimal)
```

**Q: Modified duration 6.2, yields rise 50 bps. Price impact?**

```
=-6.2 * 0.005               →  −3.1%
```

Also know:
```
Modified duration = Macaulay duration / (1 + y/n)
```
```
=DURATION(...)/(1+yld/frequency)
```

---

## Part 10 — Portfolio risk and return

### Expected return of a portfolio

```
=SUMPRODUCT(weights_range, returns_range)
```

Weights in `A1:A4`, expected returns in `B1:B4`:
```
=SUMPRODUCT(A1:A4, B1:B4)
```

### Standard deviation of a return series

```
=STDEV.S(range)      ← sample (use this for historical returns)
=STDEV.P(range)      ← population (use only if told it's the full population)
```

> In LibreOffice Calc these are `STDEV()` and `STDEVP()`. Both accept the Excel names too. **Use the sample version for historical return data** — that's the convention NISM follows.

### Covariance, correlation, beta

```
=COVARIANCE.S(range1, range2)
=CORREL(range1, range2)
=SLOPE(asset_returns, market_returns)      ← this IS beta
```

`SLOPE` is the fastest way to get beta from raw data. Equivalently:

```
Beta = Covariance(asset, market) / Variance(market)
     = Correlation × (σ_asset / σ_market)
```
```
=CORREL(A1:A60,B1:B60)*STDEV.S(A1:A60)/STDEV.S(B1:B60)
```

### Two-asset portfolio standard deviation

```
σp = √( w₁²σ₁² + w₂²σ₂² + 2·w₁·w₂·σ₁·σ₂·ρ )
```
```
=SQRT(w1^2*s1^2 + w2^2*s2^2 + 2*w1*w2*s1*s2*rho)
```

**Q: 60% in A (σ 18%), 40% in B (σ 12%), correlation 0.30.**

```
=SQRT(0.6^2*0.18^2 + 0.4^2*0.12^2 + 2*0.6*0.4*0.18*0.12*0.3)   →  13.07%
```

> 🎯 **The diversification point, in one number.** The weighted-average σ is `0.6×18 + 0.4×12 = 15.6%`. The actual portfolio σ is **13.07%**. That **2.53 percentage points of risk vanished for free** — purely because ρ < 1. This is the single most important idea in Modern Portfolio Theory, and the exam tests it as *"portfolio risk is less than the weighted average of individual risks whenever correlation is less than 1."* Only at **ρ = +1** does the gain disappear entirely.

### The performance ratios

| Ratio | Formula | Risk measure used | Answers |
|---|---|---|---|
| **Sharpe** | `=(Rp-Rf)/σp` | Total risk (σ) | Return per unit of **total** risk |
| **Treynor** | `=(Rp-Rf)/βp` | Market risk (β) | Return per unit of **market** risk |
| **Sortino** | `=(Rp-Rf)/downside_σ` | Downside deviation | Return per unit of **bad** volatility |
| **Jensen's Alpha** | `=Rp-(Rf+β*(Rm-Rf))` | — | Excess over what CAPM predicted |
| **Information Ratio** | `=(Rp-Rb)/tracking_error` | Tracking error | Skill vs the **benchmark** |

**Worked: Rp = 14%, Rf = 6%, σ = 11%, β = 1.2, Rm = 12%.**

```
Sharpe   =(14%-6%)/11%                    →  0.727
Treynor  =(14%-6%)/1.2                    →  0.0667  (i.e. 6.67%)
Alpha    =14%-(6%+1.2*(12%-6%))           →  0.8%
```

> **When to use which:** Sharpe for a **standalone** portfolio (total risk is what the client bears). Treynor for **one sleeve of an already-diversified** portfolio (only market risk is left). Alpha for **did the manager beat CAPM**. Information ratio for **did the manager beat the benchmark, consistently**.

---

## Part 11 — Goal Seek: solving backwards without algebra

Sometimes a question can't be inverted with a function. Goal Seek brute-forces it.

**Excel:** `Data → What-If Analysis → Goal Seek`
**LibreOffice Calc:** `Tools → Goal Seek`

Three boxes:
- **Set cell** — the formula cell whose result you want to fix
- **To value** — the number you want it to equal
- **By changing cell** — the input it's allowed to move

**Q: You can save ₹18,000 a month for 14 years. What return do you need to reach ₹75,00,000?**

```
B1: 10%                    (a guess — the rate)
B2: =FV(B1/12, 14*12, -18000, 0)
```
Goal Seek → Set cell `B2`, To value `7500000`, By changing cell `B1`. It returns roughly **11.6%**.

*(`RATE` would also solve this one. Goal Seek earns its keep on multi-step models — inflation-adjusted goals, blended portfolios, retirement corpus draw-downs — where no single function inverts.)*

---

## Part 12 — Formatting so you don't misread your own answer

Under time pressure, `1234567.891` gets misread as ₹12 lakh instead of ₹12.3 lakh. Two habits fix this:

**Round for display, never mid-calculation:**
```
=ROUND(ABS(PMT(9%/12,240,3500000)), 0)
```
Round **once, at the end**. Rounding an intermediate rate to 2 decimals and feeding it forward is a classic source of "my answer is close to option B but not exact."

**Convert to lakh / crore explicitly:**
```
=B2/100000    &" lakh"
=B2/10000000  &" crore"
```

> ⚠️ If your answer is *close to* an option but not exact, the cause is almost always (a) an intermediate rounding, (b) ordinary-vs-due, or (c) nominal-vs-effective rate. Check those three before assuming the option list is wrong.

---

## Part 13 — Function reference card

*(Print this. Everything above, compressed.)*

| Function | Signature | Returns |
|---|---|---|
| `FV` | `(rate, nper, pmt, [pv], [type])` | Future value |
| `PV` | `(rate, nper, pmt, [fv], [type])` | Present value |
| `PMT` | `(rate, nper, pv, [fv], [type])` | Payment per period (EMI / SIP) |
| `RATE` | `(nper, pmt, pv, [fv], [type], [guess])` | Rate **per period** |
| `NPER` | `(rate, pmt, pv, [fv], [type])` | Number of periods |
| `IPMT` | `(rate, per, nper, pv)` | Interest part of payment `per` |
| `PPMT` | `(rate, per, nper, pv)` | Principal part of payment `per` |
| `CUMIPMT` | `(rate, nper, pv, start, end, type)` | Cumulative interest |
| `CUMPRINC` | `(rate, nper, pv, start, end, type)` | Cumulative principal |
| `NPV` | `(rate, values...)` | PV of flows **starting at period 1** |
| `IRR` | `(values, [guess])` | IRR, evenly spaced flows |
| `XIRR` | `(values, dates, [guess])` | Annualised IRR, irregular dates |
| `MIRR` | `(values, finance_rate, reinvest_rate)` | IRR with an explicit reinvestment rate |
| `EFFECT` | `(nominal_rate, npery)` | Effective annual rate |
| `NOMINAL` | `(effective_rate, npery)` | Nominal annual rate |
| `PRICE` | `(settle, mat, coupon, yld, redemption, freq)` | Bond price per ₹100 |
| `YIELD` | `(settle, mat, coupon, pr, redemption, freq)` | Bond YTM |
| `DURATION` | `(settle, mat, coupon, yld, freq)` | Macaulay duration |
| `MDURATION` | `(settle, mat, coupon, yld, freq)` | Modified duration |
| `STDEV.S` | `(range)` | Sample standard deviation |
| `CORREL` | `(r1, r2)` | Correlation coefficient |
| `SLOPE` | `(y_range, x_range)` | Beta |
| `SUMPRODUCT` | `(r1, r2)` | Weighted average (portfolio return) |

---

## Part 14 — The ten errors that actually cost marks

Ranked by how often they bite.

1. **Rate not converted to the period.** `9%` where `9%/12` was needed. Every EMI and SIP question.
2. **`nper` not converted.** `20` where `20*12` was needed. Same questions, same failure.
3. **PV and PMT signs disagreeing** when both are contributions. `ABS()` hides this instead of fixing it.
4. **Goal amount in `pv` instead of `fv`.** A loan's amount is PV; a target corpus is FV.
5. **Forgetting `type=1`** on annuity-due questions. Answer is off by exactly a factor of `(1+r)`.
6. **Subtracting inflation** instead of `(1+n)/(1+i)-1`. The subtraction answer is always offered as a distractor.
7. **`RATE` read as annual** when it's per period. Multiply by 12, or compound it — read which one the question wants.
8. **Time-0 flow inside `NPV`.** Must be `=C0 + NPV(rate, C1:Cn)`.
9. **Stale cells.** Yesterday's `pv` still sitting in B4. Clear B1:B6 between every question.
10. **Rounding mid-calculation.** Round once, at the end, for display only.

---

## Part 15 — Drill set (do these until they take 30 seconds each)

Cover the answers.

| # | Question | Formula | Answer |
|---|---|---|---|
| 1 | ₹5,00,000 at 9% for 10 years, annual compounding | `=FV(9%,10,0,-500000)` | ₹11,83,682 |
| 2 | ₹5,00,000 at 9% for 10 years, monthly compounding | `=FV(9%/12,120,0,-500000)` | ₹12,25,680 |
| 3 | Monthly SIP for ₹50,00,000 in 12 years at 12% | `=ABS(PMT(12%/12,144,0,5000000))` | ₹15,671 |
| 4 | EMI on ₹45,00,000, 8.75%, 25 years | `=ABS(PMT(8.75%/12,300,4500000))` | ₹36,996 |
| 5 | Total interest on Q4 | `=36996*300-4500000` | ₹65,98,800 |
| 6 | ₹2,00,000 → ₹5,00,000 in 9 years. CAGR? | `=(500000/200000)^(1/9)-1` | 10.72% |
| 7 | Effective rate of 10% compounded quarterly | `=EFFECT(10%,4)` | 10.381% |
| 8 | Real return: 13% nominal, 7% inflation | `=(1+13%)/(1+7%)-1` | 5.607% |
| 9 | Years to triple ₹1,00,000 at 11% | `=NPER(11%,0,-100000,300000)` | 10.53 |
| 10 | ₹8,000/month, 20 years, 11%, paid at start | `=FV(11%/12,240,-8000,0,1)` | ₹69,88,600 |
| 11 | Sharpe: Rp 15%, Rf 6.5%, σ 13% | `=(15%-6.5%)/13%` | 0.654 |
| 12 | Alpha: Rp 15%, Rf 6.5%, β 1.15, Rm 12% | `=15%-(6.5%+1.15*(12%-6.5%))` | 2.175% |
| 13 | Price impact: MD 7.4, yields fall 40 bps | `=-7.4*-0.004` | +2.96% |
| 14 | 2-asset σ: 70/30, σ 20%/10%, ρ 0.2 | `=SQRT(.7^2*.2^2+.3^2*.1^2+2*.7*.3*.2*.1*.2)` | 14.89% |
| 15 | Outstanding on Q4's loan after 10 years | `=ABS(PV(8.75%/12,180,36996))` | ₹37,01,700 |

*(Answers are rounded; the exam's options will be far enough apart that rounding never changes which one you pick.)*

---

## One last thing

The spreadsheet is not the hard part — the hard part is **reading the question correctly**. Before you type anything, answer these three out loud:

1. **What am I solving for?** → picks the function
2. **What's the period?** → sets `rate` and `nper`
3. **Which way is the money moving?** → sets the signs

Do that and the spreadsheet is a typing exercise. Skip it and you'll get a confident, well-formatted, wrong answer.

**Good luck. 🎯**
