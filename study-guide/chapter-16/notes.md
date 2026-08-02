# Chapter 16: Portfolio Performance Measurement and Evaluation — Short Notes

> **Module 5 · Portfolio Construction, Performance Monitoring and Evaluation (20 marks).**
> The single most **formula-dense and numerical** chapter in the syllabus. Almost every mark comes from being able to (a) pick the *right* return measure, (b) pick the *right* risk measure, and (c) divide one by the other correctly. There are roughly a dozen formulas here. Learn each one with its **worked example and its "when do I use this?" rule** — the exam tests the *choice* of measure at least as often as the arithmetic.

---

## 16.1 Parameters to Define Performance — Risk AND Return

### 🔑 The one idea that governs the whole chapter

> **A return figure on its own is meaningless. Performance is a two-dimensional quantity: return earned, and risk taken to earn it.**

Two funds both returned **18%** last year. Fund A did it holding 30 large-cap stocks; Fund B did it holding 4 micro-caps on borrowed money. They did **not** perform equally. The only defensible comparison divides return by risk — which is exactly what the Sharpe, Treynor, Sortino, Information and M² ratios do.

A complete performance evaluation answers **four** questions:

| # | Question | Tool |
|---|---|---|
| 1 | **How much** did the portfolio earn? | HPR, TWRR, CAGR, portfolio return |
| 2 | **How much risk** was taken? | Standard deviation, beta, downside deviation, tracking error |
| 3 | Was the return **worth** the risk? | Sharpe, Treynor, Sortino, Information Ratio, M², alpha |
| 4 | **Where** did the return come from? | Benchmarking, peer analysis, attribution |

> ⚠️ **Exam trap.** "Which fund performed better?" is *never* answered by the higher raw return alone in this chapter. If the question gives you a standard deviation or a beta, it wants a **risk-adjusted** answer.

Three further principles run through the chapter:

- **Compare like with like.** A mid-cap fund is measured against a mid-cap index, not the NIFTY 50.
- **Measure over a full market cycle.** One year of returns tells you almost nothing; **3, 5 and 10-year** figures and **rolling returns** tell you a lot.
- **Measure what the manager controls.** Client cash flows are not the manager's decision — which is the entire reason TWRR exists.

---

## 16.2 Rate of Return Measures

### 16.2.1 ⭐ Holding Period Return (HPR)

The simplest and most fundamental measure — the **total return over however long you held the asset**, with no annualising.

> **HPR = (Ending value − Beginning value + Income received) ÷ Beginning value**

Income means dividends, interest or coupons received during the period. Never leave it out.

**Worked example.** Mrs Iyer buys **1,000 shares at ₹250** each = **₹2,50,000**. Nine months later she sells at **₹278** and has received a dividend of **₹6 per share**.

- Ending value = 1,000 × ₹278 = **₹2,78,000**
- Income = 1,000 × ₹6 = **₹6,000**
- HPR = (2,78,000 − 2,50,000 + 6,000) ÷ 2,50,000 = 34,000 ÷ 2,50,000 = **13.6%**

That 13.6% is for **nine months**, not a year. To make it comparable to a one-year figure:

- Annualised = (1.136)^(12/9) − 1 = (1.136)^1.3333 − 1 = **18.53%**

> 🧠 **Memory hook — HPR is "everything that came back, over what went in."** Price change **plus** income, all divided by the opening value.

> ⚠️ **Trap.** HPR is a **holding-period** number. Never call a 9-month 13.6% an "annual return of 13.6%", and never present a 3-month figure annualised in a client document — SEBI requires mutual fund returns for periods of **less than one year to be shown in absolute terms**, and for **one year and above as CAGR**.

---

### 16.2.2 ⭐⭐ TWRR versus MWRR — the most important distinction in the chapter

Both measure the return of the *same* portfolio over the *same* period. They give different answers whenever **money went in or out** during the period.

| | **Time-Weighted Rate of Return (TWRR)** | **Money-Weighted Rate of Return (MWRR)** |
|---|---|---|
| **What it is** | The **geometric chaining** of the returns of each sub-period between cash flows | The **IRR** of all the cash flows — the discount rate that equates inflows and outflows |
| **Effect of cash flows** | **Neutralised** — each sub-period gets equal weight regardless of how much money was in it | **Fully captured** — periods with more money in them dominate the answer |
| **What it measures** | **The manager's skill** | **The investor's actual experience** |
| **Who should use it** | Managers, regulators, ratings agencies, anyone **comparing** managers | An individual client asking "what did *my* money earn?" |
| **Indian usage** | **Mandatory for PMS performance disclosure (SEBI)**; the basis of published mutual fund returns | The number in a client's own SIP/XIRR statement |

### 🔑 WHY TWRR measures manager skill

> **The manager decides what to buy. The client decides when to put money in and take it out. A performance measure that credits or blames the manager for the client's timing is measuring the wrong person.**

TWRR breaks the period at every cash flow, computes a clean return for each slice, and multiplies the slices together. Because each slice is a *percentage*, the **rupee amount in the portfolio during that slice becomes irrelevant** — the cash flow's distorting effect is removed. That is why SEBI requires PMS and mutual fund performance to be reported on a **TWRR** basis: a manager who runs the identical strategy for two clients must show the identical performance, even if one client added ₹1 crore at the worst possible moment.

**Worked example — the same year, two very different answers.**

Mr Nair starts a discretionary PMS with **₹10,00,000** on 1 April.

| Date | Event | Value |
|---|---|---|
| 1 Apr | Invests | ₹10,00,000 |
| 30 Sep | Portfolio has grown | **₹12,00,000** (+20% in H1) |
| 1 Oct | Mr Nair adds **₹10,00,000** | ₹22,00,000 |
| 31 Mar | Portfolio has fallen | **₹19,80,000** (−10% in H2) |

**TWRR:**
- Sub-period 1 return = (12,00,000 − 10,00,000) ÷ 10,00,000 = **+20%**
- Sub-period 2 return = (19,80,000 − 22,00,000) ÷ 22,00,000 = **−10%**
- TWRR = (1.20 × 0.90) − 1 = 1.08 − 1 = **+8% for the year**

**MWRR:**
- Total put in = ₹10,00,000 + ₹10,00,000 = **₹20,00,000**; total value at the end = **₹19,80,000**
- The client is **₹20,000 poorer**. The MWRR (the IRR of −10,00,000 at t=0, −10,00,000 at t=0.5 and +19,80,000 at t=1) is approximately **−1.3% per annum**.

**Reconciling the two:** the manager genuinely delivered **+8%**. But Mr Nair had ₹10 lakh working during the good half and **₹22 lakh** working during the bad half. His *own timing* destroyed his outcome.

> 🧠 **Memory hook — "TWRR judges the driver; MWRR judges the journey."**
> The driver (manager) is graded on driving. The journey (your actual outcome) also depends on when *you* got in and out of the car.

> ⚠️ **Trap.** TWRR = MWRR **only when there are no cash flows** during the period. If a question says "no contributions or withdrawals were made", the two are identical and the distinction is a red herring.

> ⚠️ **Trap.** MWRR > TWRR when the client added money **before** a strong period (good timing). MWRR < TWRR when the client added money **before** a weak period (bad timing). Work out the direction from the timing, not by guessing.

**Where you meet each in Indian practice:** the **XIRR** on a client's SIP statement is an MWRR. The **CAGR shown on a fund factsheet** is derived from NAVs and is therefore a TWRR.

---

### 16.2.3 ⭐⭐ Arithmetic Mean Return (AMR) versus Geometric Mean Return (GMR)

> **AMR = (R₁ + R₂ + … + Rₙ) ÷ n** — the simple average.
> **GMR = [(1+R₁)(1+R₂)…(1+Rₙ)]^(1/n) − 1** — the compounded average.

**Worked example.** A fund returns **+25%**, **−10%**, **+15%** over three years on ₹10,00,000.

| Year | Return | Value at year end |
|---|---|---|
| 1 | +25% | ₹12,50,000 |
| 2 | −10% | ₹11,25,000 |
| 3 | +15% | **₹12,93,750** |

- **AMR** = (25 − 10 + 15) ÷ 3 = **10.00%**
- **GMR** = (1.25 × 0.90 × 1.15)^(1/3) − 1 = (1.29375)^(1/3) − 1 = **8.96%**

**Check which one is true:** ₹10,00,000 × (1.0896)³ = ₹12,93,750 ✓. ₹10,00,000 × (1.10)³ = ₹13,31,000 ✗ — the AMR **overstates** what actually happened by over ₹37,000.

### 🔑 The rule you must memorise

> **AMR ≥ GMR, always. They are equal only when every period's return is identical. The gap widens as volatility rises.**

A good approximation: **GMR ≈ AMR − σ²/2**.

**Why the inequality exists — the arithmetic of losses.** A 50% loss needs a **100%** gain to get back to level. Percentage gains and losses are not symmetric, so simply averaging them overstates the compounded outcome.

**The extreme illustration.** Returns of **+50%** and **−50%**:

- AMR = (50 − 50) ÷ 2 = **0%** — implying you broke even
- Reality: ₹1,00,000 → ₹1,50,000 → **₹75,000**. You lost a quarter of your money.
- GMR = √(1.50 × 0.50) − 1 = √0.75 − 1 = **−13.40% per annum**

| Volatility of the return series | AMR | GMR | Gap |
|---|---|---|---|
| +10%, +10% (zero volatility) | 10.0% | **10.0%** | **0** |
| +20%, 0% | 10.0% | **9.54%** | 0.46 pp |
| +50%, −30% | 10.0% | **2.47%** | 7.53 pp |
| +90%, −70% | 10.0% | **−24.50%** | 34.5 pp |

> 🧠 **Memory hook — "Arithmetic is what you hoped for; geometric is what you got."**
> The gap between them **is** the cost of volatility.

**When to use which:**

| Use | Measure |
|---|---|
| Reporting **past, realised** multi-period performance | **GMR** (= CAGR) — it is the only one that reproduces the ending value |
| Estimating **next period's expected** return from history | **AMR** — it is the unbiased estimate of a single period |
| Comparing funds' long-run track records | **GMR** |

> ⚠️ **Trap.** A fund advertising its "average annual return" using an arithmetic mean over a volatile period is inflating its record. The honest number is the **CAGR / GMR**.

---

### 16.2.4 Gross Return versus Net Return

> **Net return = Gross return − all fees, expenses and costs**

| Deduction | Where it bites |
|---|---|
| **Management / advisory fee** | The largest single item in most products |
| **TER** (mutual funds) | Bundles management fee, marketing, registrar, trustee, audit |
| **Performance / incentive fee** | PMS and AIFs — subject to hurdle and high watermark |
| **Brokerage and transaction costs** | Rise with portfolio turnover |
| **STT, stamp duty, exchange charges** | Statutory transaction costs |
| **Custody, fund accounting** | PMS and AIF |
| **GST on fees** | **18%** on the advisory/management fee |
| **Exit load** | On early redemption |

**Worked example — a ₹50,00,000 PMS.** Gross return for the year is **15%**.

- Gross gain = 15% × ₹50,00,000 = **₹7,50,000**
- Fixed fee 2% of assets = **₹1,00,000**
- Performance fee 20% of the return above a 10% hurdle = 20% × (₹7,50,000 − ₹5,00,000) = **₹50,000**
- Brokerage, custody and other costs = **₹25,000**
- **Total costs = ₹1,75,000**
- Net gain = ₹7,50,000 − ₹1,75,000 = **₹5,75,000** → **net return 11.50%**

**A 15% gross return became an 11.5% net return — costs consumed 3.5 percentage points, nearly a quarter of the gross gain.**

> ⚠️ **Trap.** SEBI requires PMS performance to be disclosed **net of all fees and expenses**. Comparing one manager's gross return to another's net return is a classic benchmarking error.

---

### 16.2.5 Pre-tax versus Post-tax Return

The client spends **post-tax** rupees. Two investments with identical pre-tax returns can differ enormously after tax.

> **Post-tax return = Pre-tax return × (1 − marginal tax rate)** — for fully taxable income such as interest.

**Worked example.** Mr Bose is in the **30%** slab and compares two options for ₹10,00,000 over one year:

| Option | Pre-tax return | Tax treatment | Post-tax return |
|---|---|---|---|
| Bank FD @ **7.5%** | ₹75,000 | Slab rate **30%** → tax ₹22,500 | **₹52,500 = 5.25%** |
| Equity fund, held **> 12 months**, gain **7.5%** | ₹75,000 | LTCG at **12.5%** above the **₹1.25 lakh** annual exemption → **nil** here, as the gain is within the exemption | **₹75,000 = 7.50%** |

The equity route delivers **7.50%** versus the FD's **5.25%** — a **2.25 percentage point** advantage created entirely by the tax code, not by the market.

**The rates you should know for Indian portfolios:**

| Asset | Short term | Long term |
|---|---|---|
| **Listed equity / equity mutual funds** | **20%** if held **≤ 12 months** | **12.5%** if held **> 12 months**, on gains above **₹1.25 lakh** per financial year |
| **Debt mutual funds** bought on/after 1 Apr 2023 | **Slab rate** | **Slab rate** — no special long-term rate |
| **Bank FD / bond interest** | **Slab rate** | **Slab rate** |

> 🧠 **Memory hook — three layers, in order: GROSS → NET (minus fees) → POST-TAX (minus tax).** Only the last one is the client's real return.

> ⚠️ **Trap.** Tax is **investor-specific** — it depends on the client's slab, holding period and use of the exemption. A fund can never publish a single "post-tax return" for everybody, which is exactly why published returns are pre-tax.

---

### 16.2.6 ⭐ CAGR — Compound Annual Growth Rate

> **CAGR = (Ending value ÷ Beginning value)^(1/n) − 1**, where **n = number of YEARS**

CAGR is simply the GMR expressed from two endpoints. It is the **smoothed constant annual rate** that would take you from the start value to the end value.

**Worked example.** ₹5,00,000 invested in 2018 is worth **₹11,00,000** after **7 years**.

- CAGR = (11,00,000 ÷ 5,00,000)^(1/7) − 1 = (2.20)^(1/7) − 1 = **11.92% p.a.**

**Check:** ₹5,00,000 × (1.1192)⁷ ≈ ₹11,00,000 ✓

**Second example — n need not be a whole number.** ₹8,00,000 grows to ₹9,80,000 in **30 months** (2.5 years):

- CAGR = (9,80,000 ÷ 8,00,000)^(1/2.5) − 1 = (1.225)^0.4 − 1 = **8.46% p.a.**

> ⚠️ **Trap — CAGR hides the path completely.** A fund that went +60%, −30%, +25% and a fund that went +14%, +14%, +14% can have almost the same CAGR and utterly different risk. **CAGR says nothing about volatility.** This is precisely why the chapter then adds risk measures.

> ⚠️ **Trap — CAGR is point-to-point and therefore start-date sensitive.** Choosing a market bottom as the start date flatters any fund. The professional fix is **rolling returns**: compute the 3-year CAGR starting from *every* day in the period and look at the distribution, not one lucky window.

---

### 16.2.7 Annualising Returns (and Risk)

**Annualising a return** — always **compound**, never multiply:

> **Annualised return = (1 + periodic return)^(number of periods per year) − 1**

| Given | Working | Annualised |
|---|---|---|
| **4% in a quarter** | (1.04)⁴ − 1 | **16.99%** (not 16%) |
| **1.2% in a month** | (1.012)¹² − 1 | **15.39%** (not 14.4%) |
| **13.6% in 9 months** | (1.136)^(12/9) − 1 | **18.53%** |
| **0.05% in a day** | (1.0005)²⁵² − 1 | **13.42%** |

**Annualising risk** — volatility scales with the **square root of time**:

> **σ_annual = σ_periodic × √(number of periods per year)**

| Given | Working | Annualised σ |
|---|---|---|
| Monthly σ = **4%** | 4 × √12 = 4 × 3.464 | **13.86%** |
| Daily σ = **1%** | 1 × √252 | **15.87%** |
| Quarterly σ = **7%** | 7 × √4 | **14.00%** |

**Why √t and not t?** Returns in successive periods are assumed **independent**. Variances (not standard deviations) add up over time, so variance scales with **t** and standard deviation with **√t**.

> ⚠️ **Trap.** Because return grows roughly with **t** but risk only with **√t**, the *reward-to-risk* ratio improves with the horizon. This is the mathematical basis of "equities are less risky over long horizons."

> ⚠️ **Trap.** Never annualise a return from a period **shorter than one year** for client-facing disclosure. A 6% quarterly gain annualises to 26.2% — a number no one should be shown as an expectation. SEBI's rule: **< 1 year → absolute; ≥ 1 year → CAGR.**

---

### 16.2.8 Cash Drag and Cash-Drag-Adjusted Return

**Cash drag** is the reduction in portfolio return caused by holding uninvested cash in a rising market. Every fund holds some cash — for redemptions, for pending deployment, for tactical reasons — and that cash earns a money-market rate rather than the asset-class return.

> **Cash-drag-adjusted return = (R_portfolio − w_cash × R_cash) ÷ (1 − w_cash)**

This strips the cash out and shows **what the invested portion actually earned** — the fairest measure of the manager's security selection.

**Worked example.** A ₹100 crore equity fund holds **10% in cash** earning **4%**; the **90%** invested in equities returns **15%**.

- Reported portfolio return = (0.90 × 15%) + (0.10 × 4%) = 13.5% + 0.4% = **13.9%**
- **Cash drag = 15% − 13.9% = 1.1 percentage points**
- Cash-drag-adjusted return = (13.9% − 0.10 × 4%) ÷ 0.90 = 13.5 ÷ 0.90 = **15.0%** ✓ — exactly the equity return, as it must be

> 🧠 **Memory hook — "Cash is a 100% weight in the wrong asset."** In a bull market it drags; in a crash it cushions. Cash drag is therefore a *cost of liquidity*, not automatically a mistake.

> ⚠️ **Trap.** Cash drag is only a drag when the market **rises**. If equities fell 15%, the same 10% cash would have *added* about 1.9 percentage points. That is why some cash is deliberate defence and evaluating it requires knowing the market's direction.

---

### 16.2.9 ⭐⭐ Alpha and Beta Return

A portfolio's return splits into two economically different parts:

| Component | What it is | How you get it | What it is worth paying for |
|---|---|---|---|
| **Beta return** | The return earned simply for **being exposed to the market** | Buy an index fund | Almost nothing — a few basis points |
| **Alpha return** | The return **above** what that market exposure alone would justify | Genuine manager skill | This is what an active fee buys |

> **Expected return under CAPM: E(Rp) = Rf + β(Rm − Rf)**
> **Jensen's Alpha, α = Rp − [Rf + β(Rm − Rf)]**

**Worked example.** A fund returned **16%**. The risk-free rate (364-day T-bill) is **6.5%**, the NIFTY 50 TRI returned **13%**, and the fund's beta is **1.20**.

- Market risk premium = 13% − 6.5% = **6.5%**
- Return the fund *should* have earned for that risk = 6.5% + (1.20 × 6.5%) = 6.5% + 7.8% = **14.30%**
- **Alpha = 16% − 14.30% = +1.70%**

The fund beat the index by 3 percentage points (16 vs 13), but **1.3 of those points were bought, not earned** — simply by running a beta of 1.2 in a rising market. The **genuine skill contribution is 1.70%**.

**A second example where the raw comparison misleads completely.** A conservative fund returned **11%** while the market returned **12%** — it "underperformed". But its beta was **0.70** and Rf is **6%**.

- Required = 6 + 0.70 × (12 − 6) = 6 + 4.2 = **10.20%**
- **Alpha = 11 − 10.20 = +0.80%** — the fund actually **added value**, taking far less risk than the index.

> 🧠 **Memory hook — "Beta is rented; alpha is earned."**

> ⚠️ **Trap — the most common alpha error in the exam.** **Alpha is NOT (Rp − Rm).** Simple excess return over the benchmark ignores the risk taken to get it. Alpha subtracts the **beta-adjusted** required return. Only when β = 1 do the two coincide.

> ⚠️ **Trap.** Alpha is only meaningful if the **benchmark and beta are appropriate**. A mid-cap fund measured with a beta against the NIFTY 50 will show a spurious alpha that is really just the mid-cap premium.

---

### 16.2.10 Portfolio Return

For a portfolio held over a single period with fixed weights:

> **Rp = w₁R₁ + w₂R₂ + … + wₙRₙ** — the **weighted average** of the component returns, with **Σwᵢ = 1**

**Worked example.** Ms D'Souza's ₹1,00,00,000 portfolio:

| Asset | Amount | Weight | Return | Contribution |
|---|---|---|---|---|
| Equity funds | ₹60,00,000 | 0.60 | 14.0% | 8.40% |
| Debt funds | ₹30,00,000 | 0.30 | 7.5% | 2.25% |
| Gold ETF | ₹10,00,000 | 0.10 | 9.0% | 0.90% |
| **Portfolio** | **₹1,00,00,000** | **1.00** | | **11.55%** |

Cross-check in rupees: ₹8,40,000 + ₹2,25,000 + ₹90,000 = **₹11,55,000** on ₹1 crore = **11.55%** ✓

> ⚠️ **Trap.** The weighted-average rule works for **return**. It does **NOT** work for **risk** — portfolio standard deviation is almost always *less* than the weighted average of the component standard deviations (Chapter 14). Return adds in a straight line; risk does not.

> ⚠️ **Trap.** Weights must be **market-value weights at the start of the period**, not cost weights and not end weights.

---

## 16.3 Risk Measures

### 16.3.1 ⭐ Total Risk and Downside Risk

**Total risk** is measured by **standard deviation (σ)** — the dispersion of returns around their mean. It treats a **+15% surprise and a −15% surprise as equally "risky"**, because both are deviations.

**Downside risk** measures only the outcomes an investor actually fears — returns **below a target** (the Minimum Acceptable Return, or MAR, which may be 0%, the risk-free rate, or a required return).

> **Downside deviation = √[ Σ (min(Rᵢ − MAR, 0))² ÷ n ]**
> Only shortfalls enter the sum; every period still counts in **n**.

**Worked example.** Five annual returns for a fund: **0%, 3%, 20%, 18%, 19%**. Mean = **12%**. Take **MAR = 6%**.

*Total risk (standard deviation):*
- Deviations from the 12% mean: −12, −9, +8, +6, +7
- Squares: 144 + 81 + 64 + 36 + 49 = **374**; ÷ 5 = 74.8
- **σ = √74.8 = 8.65%**

*Downside deviation (MAR = 6%):*
- Only two years fell short: 0% (shortfall **6**) and 3% (shortfall **3**)
- Squares: 36 + 9 = **45**; ÷ 5 = 9
- **Downside deviation = √9 = 3.00%**

Total risk **8.65%**, downside risk only **3.00%** — because most of this fund's volatility was **upside**. An investor who dislikes losses but is perfectly happy with big gains should judge it on 3.00%, not 8.65%.

**Other downside measures worth knowing:**

| Measure | Definition | Example |
|---|---|---|
| **Semi-variance / semi-deviation** | Variance computed using only below-mean returns | The square of downside deviation |
| **Maximum drawdown (MDD)** | Largest peak-to-trough fall | Portfolio peaks at ₹52 lakh, troughs at ₹36.40 lakh → MDD = 15.6/52 = **30%** |
| **Value at Risk (VaR)** | The loss that will not be exceeded with a stated confidence over a stated horizon | "95% one-day VaR is ₹2 lakh" → on **19 days out of 20** the loss stays under ₹2 lakh |
| **Downside capture ratio** | Fund's return in falling markets ÷ benchmark's | Benchmark −3%, fund −2.4% → **80%** — good |
| **Upside capture ratio** | Fund's return in rising markets ÷ benchmark's | Benchmark +4%, fund +4.4% → **110%** — good |

> 🧠 **Memory hook — "Standard deviation punishes good surprises too."** Downside measures fix that.

---

### 16.3.2 Portfolio Risk versus Individual Risk

A security's own standard deviation tells you almost nothing about what it does to a portfolio.

> **A security's contribution to portfolio risk is its COVARIANCE with the rest of the portfolio — not its own standard deviation.**

A very volatile asset that moves **against** the portfolio (negative covariance) can **reduce** total portfolio risk. Gold in an Indian equity portfolio is the standard illustration: volatile on its own, stabilising in combination.

This is why the relevant risk measure changes with context:

| Context | Right risk measure |
|---|---|
| The asset is held **alone**, or is the client's whole portfolio | **Total risk (σ)** |
| The asset is **one holding inside a diversified portfolio** | **Systematic risk (β)** / covariance |

---

### 16.3.3 Market Risk

**Market risk** is the risk that the entire market falls — the portion of risk that **cannot be diversified away** because it affects every security to some degree. Its Indian drivers: RBI policy rate changes, inflation, GDP growth, the fiscal deficit, FPI flows, crude oil prices, the rupee, global risk sentiment, elections and Union Budget announcements.

It is measured by **beta**, and it is the risk for which investors are **compensated**.

---

### 16.3.4 Interpreting Volatility

Standard deviation only becomes useful when you convert it into a statement about likely outcomes. Assuming returns are approximately normally distributed:

| Range | Probability |
|---|---|
| Mean **± 1σ** | about **68%** |
| Mean **± 2σ** | about **95%** |
| Mean **± 3σ** | about **99.7%** |

**Worked example.** A fund has an expected return of **12%** and σ of **18%**.

- **68%** of years should land between **12 − 18 = −6%** and **12 + 18 = +30%**
- **95%** of years should land between **12 − 36 = −24%** and **12 + 48 = +48%**
- On ₹20,00,000, a −24% year is a paper loss of **₹4,80,000** — the number to put in front of the client *before* investing

Typical annualised standard deviations you can use for sanity-checking:

| Asset class | Indicative annual σ |
|---|---|
| Liquid / overnight funds | very low, ~0–1% |
| Short-duration debt | low single digits |
| Gilt / long-duration debt | mid single digits |
| Large-cap equity | mid-to-high teens |
| Mid- and small-cap equity | materially higher than large-cap |

> ⚠️ **Trap.** Real market returns have **fat tails** — extreme moves happen far more often than a normal distribution predicts (March 2020 is the obvious Indian example). Standard deviation therefore **understates** true tail risk.

> ⚠️ **Trap.** σ is computed from **past** returns and is not a forecast. It is also **regime-dependent** — volatility clusters, and periods of calm are routinely followed by periods of stress.

---

### 16.3.5 ⭐ Tracking Error

> **Tracking Error = the standard deviation of the ACTIVE RETURN (portfolio return − benchmark return) over a series of periods**

It answers: **how tightly does this portfolio hug its benchmark?**

**Worked example.** Four quarters of active return: **+4%, 0%, +4%, 0%**.

- Mean active return = 8 ÷ 4 = **+2%**
- Deviations from the mean: +2, −2, +2, −2 → squares 4, 4, 4, 4 = **16**; ÷ 4 = 4
- **Tracking error = √4 = 2.0%**

**What tracking error tells you:**

| Tracking error | Interpretation |
|---|---|
| **Near zero** | A pure index fund / ETF |
| **Low (roughly 1–3%)** | Closet indexing or a tightly benchmarked large-cap fund |
| **Moderate (roughly 4–7%)** | A genuinely active but benchmark-aware fund |
| **High (8%+)** | High-conviction, concentrated or unconstrained fund |

> ⚠️ **Trap.** **Tracking error is not "underperformance."** A fund that beats its index by exactly 4% every single quarter has a **tracking error of ZERO** — the active return never varies — while delivering huge outperformance. Tracking error measures the **variability** of the gap, not its sign or its size.

> ⚠️ **Trap — tracking error vs tracking difference.** **Tracking difference** is the simple *return gap* (fund return minus index return). **Tracking error** is the *standard deviation* of that gap. SEBI requires index funds and ETFs to disclose **both**, and caps the tracking error of equity index funds and ETFs (measured on rolling one-year data) at **2%**.

**Why an index fund cannot have zero tracking error:** the TER, cash held for redemptions, index rebalancing costs, brokerage, STT and dividend-reinvestment timing all create small, unavoidable gaps.

Tracking error is also the **denominator of the Information Ratio** — its second and more important exam role.

---

### 16.3.6 ⭐⭐ Systematic and Unsystematic Risk

> **Total risk = Systematic risk + Unsystematic risk**
> In variance terms: **σ²ᵢ = β²σ²ₘ + σ²ₑ**

| | **Systematic risk** | **Unsystematic risk** |
|---|---|---|
| **Other names** | Market risk, non-diversifiable risk | Specific, unique, residual, diversifiable, idiosyncratic risk |
| **Source** | Economy-wide: RBI rates, inflation, GDP, currency, oil, policy, war, global sentiment | Company- or sector-specific: a fraud, a product recall, a plant fire, a promoter pledge, a regulatory ban, a strike, litigation |
| **Affects** | **All** securities, to differing degrees | **One** company or sector |
| **Can diversification remove it?** | **NO** | **YES** |
| **Measured by** | **Beta (β)** | Residual standard deviation |
| **Is it rewarded?** | **YES** — investors are paid a premium for bearing it | **NO** — the market does not pay you for a risk you could have removed for free |

### 🔑 Why unsystematic risk is not rewarded

> **The market only pays you for risk you cannot avoid. Since specific risk can be eliminated at nearly zero cost by diversifying, no rational investor would pay a premium for a security merely because it carries a lot of it.**

**How much diversification is enough?** Adding stocks reduces specific risk quickly at first and then with diminishing returns. Most of the benefit in a broad equity portfolio arrives within roughly **20–30 well-spread stocks**; beyond that the curve flattens against the floor of systematic risk. What matters more than the count is that the holdings are **genuinely different** — 30 Indian banking stocks are not diversified.

**R² tells you how well diversified a portfolio is:** it is the proportion of the portfolio's variance explained by the market.

| R² | Meaning |
|---|---|
| **95–100%** | Essentially an index fund — beta and alpha figures are highly reliable |
| **70–95%** | A typical diversified active fund |
| **Below ~70%** | A lot of non-market risk — **beta, alpha and Treynor become unreliable** for this fund |

---

### 16.3.7 ⭐⭐ Beta

> **β = Cov(Rᵢ, Rₘ) ÷ Var(Rₘ) = ρᵢₘ × (σᵢ ÷ σₘ)**

Beta measures **sensitivity to market movements** — how much the security or portfolio moves for a 1% move in the market.

**Worked example.** A stock has σ = **24%**, the market has σ = **16%**, and their correlation is **0.80**.

- **β = 0.80 × (24 ÷ 16) = 0.80 × 1.50 = 1.20**

If the NIFTY rises **10%**, this stock is expected to rise **12%**. If the NIFTY falls **10%**, it is expected to fall **12%**.

| Beta | Meaning | Typical Indian example |
|---|---|---|
| **β = 1.0** | Moves with the market | An index fund; the market itself, by definition |
| **β > 1.0** | **Aggressive** — amplifies the market | Cyclicals, capital goods, metals, high-beta NBFCs |
| **0 < β < 1** | **Defensive** — damped | FMCG, pharma, utilities |
| **β = 0** | Uncorrelated with the market | Treasury bills / cash |
| **β < 0** | Moves opposite the market | Rare; gold is sometimes weakly negative to equities |

**Portfolio beta = the weighted average of the component betas** (unlike portfolio σ, this *is* a simple weighted average).

**Worked example.**

| Holding | Weight | Beta | Contribution |
|---|---|---|---|
| Cyclical fund | 0.40 | 1.40 | 0.560 |
| Large-cap fund | 0.35 | 0.90 | 0.315 |
| FMCG fund | 0.25 | 0.60 | 0.150 |
| **Portfolio** | **1.00** | | **β = 1.025** |

**Using beta to forecast:** if the market is expected to return 12% with Rf at 6%, this portfolio's CAPM expected return is 6 + 1.025 × 6 = **12.15%**.

> ⚠️ **Trap.** Beta is estimated by **regression on past data** and is unstable — it changes as the portfolio changes and as market conditions change. It is also only reliable when **R² is high**.

> ⚠️ **Trap.** Beta captures **only systematic risk**. A single stock with β = 0.8 is **not** less risky than a diversified portfolio with β = 1.0 — the stock also carries huge specific risk that beta simply does not see.

---

### 16.3.8 Liquidity Risk

**The risk that a holding cannot be sold quickly at a fair price.** It shows up as:

- **Wide bid-ask spreads** and high **impact cost** — the price moves against you as you trade
- Small-cap and micro-cap equities, unlisted securities, real estate, and lower-rated corporate bonds are the most exposed
- Liquidity **evaporates exactly when it is most needed** — in a market panic, buyers disappear

**Indian regulatory responses you should know:**
- SEBI requires **stress testing and liquidity disclosures** for mid-cap and small-cap equity mutual fund schemes
- **Side-pocketing** (segregated portfolios) allows an illiquid, credit-impaired security to be ring-fenced so that redeeming investors cannot unfairly transfer the loss to those who stay
- Debt schemes must hold minimum liquid assets and are subject to **potential risk class** and liquidity-ratio norms
- **Swing pricing** for open-ended debt schemes in stressed conditions

> ⚠️ **Trap.** Liquidity risk is **not captured by standard deviation**. Illiquid assets are valued infrequently, which makes their measured volatility look artificially *low* — a phenomenon called **volatility smoothing**. Never conclude that a real-estate or unlisted portfolio is "low risk" because its reported σ is small.

---

### 16.3.9 Credit Risk

**The risk that a borrower fails to pay interest or principal on time — or is downgraded.** Relevant to every debt holding.

| Element | Detail |
|---|---|
| **Default risk** | The issuer does not pay |
| **Downgrade risk** | The rating falls, the price falls immediately even if no default occurs |
| **Credit spread risk** | Spreads over G-Secs widen market-wide, hurting all corporate bonds |
| **Rating agencies in India** | **CRISIL, ICRA, CARE, India Ratings, Brickwork** |
| **Rating scale** | **AAA** (highest safety) → AA → A → BBB (lowest **investment grade**) → BB and below (**speculative**) → **D** (default) |
| **Compensation** | The **credit spread** — the extra yield over a same-maturity G-Sec |

Indian episodes worth remembering as illustrations: the IL&FS and DHFL defaults showed how quickly an AAA rating can collapse and how credit and liquidity risk arrive together.

> ⚠️ **Trap.** A high-yield debt fund's *reported* return looks excellent right up to the moment of default. Credit risk is **asymmetric and non-normal** — small steady gains, then a sudden large loss — so σ badly understates it.

---

## 16.4 ⭐⭐ Risk-Adjusted Return Measures

The heart of the chapter. All five follow the same logic: **excess return divided by a measure of risk.** What changes is *which* risk goes in the denominator.

| Ratio | Formula | Risk in the denominator | Higher is better? |
|---|---|---|---|
| **Sharpe** | (Rp − Rf) ÷ **σp** | **Total** risk | Yes |
| **Treynor** | (Rp − Rf) ÷ **βp** | **Systematic** risk only | Yes |
| **Sortino** | (Rp − MAR) ÷ **downside deviation** | **Downside** risk only | Yes |
| **Information Ratio** | (Rp − Rb) ÷ **Tracking Error** | **Active/relative** risk | Yes |
| **M²** | Rf + (Sharpe × **σm**) | Restated at **market** risk | Yes — and read as a **%** |

---

### 16.4.1 Sharpe Ratio

> **Sharpe Ratio = (Rp − Rf) ÷ σp**

**Excess return per unit of TOTAL risk.** Developed by **William Sharpe**. It is the most widely used risk-adjusted measure in the world.

**Worked example — why higher return can mean worse performance.** Risk-free rate = **6%**.

| Fund | Return | σ | Sharpe |
|---|---|---|---|
| **Fund A** | 16% | 20% | (16 − 6) ÷ 20 = **0.50** |
| **Fund B** | 12% | 10% | (12 − 6) ÷ 10 = **0.60** |

**Fund B wins**, despite returning 4 percentage points less. Per unit of risk taken, B delivered more.

**The intuition that makes this concrete:** you could **lever** Fund B to match Fund A's risk. Borrow at 6% to hold **twice** as much of B: σ becomes 2 × 10 = **20%** (matching A) and return becomes (2 × 12) − (1 × 6) = **18%** — better than A's 16% at identical risk. That is what the higher Sharpe ratio is telling you.

> ⚠️ **Trap.** Sharpe ratios are **only comparable between funds measured over the same period with the same Rf**. Never compare a Sharpe ratio from a bull market with one from a bear market.

> ⚠️ **Trap.** If (Rp − Rf) is **negative**, the Sharpe ratio becomes meaningless for ranking — a *riskier* fund with the same negative excess return will show a *less negative* Sharpe, wrongly appearing better.

---

### 16.4.2 Treynor Ratio

> **Treynor Ratio = (Rp − Rf) ÷ βp**

**Excess return per unit of SYSTEMATIC risk.** Developed by **Jack Treynor**.

The logic: if the portfolio is **one component of an already well-diversified overall portfolio**, its unsystematic risk has *already been diversified away* at the total-portfolio level. Charging that fund for risk that no longer exists would be wrong. So the denominator uses **beta only**.

**Worked example.** Rf = **6%**.

| Fund | Return | Beta | Treynor |
|---|---|---|---|
| **Fund P** | 15% | 1.20 | (15 − 6) ÷ 1.20 = **7.50** |
| **Fund Q** | 11% | 0.50 | (11 − 6) ÷ 0.50 = **10.00** |

**Fund Q wins** — it produced 5 points of excess return while taking only half the market's risk.

> 🧠 **Memory hook — read the units.** Sharpe's answer is a pure number ("0.60"). Treynor's answer is **in percentage points per unit of beta** ("10.00" means 10 percentage points of excess return per 1.0 of beta).

---

### 16.4.3 ⭐⭐ Sharpe versus Treynor — the classic comparison

| | **Sharpe** | **Treynor** |
|---|---|---|
| **Denominator** | σ — **total** risk | β — **systematic** risk |
| **Assumes the portfolio is** | The investor's **entire** wealth | **One sub-portfolio** inside a bigger diversified whole |
| **Penalises poor diversification?** | **YES** | **NO** |
| **Use when** | Judging a **standalone** portfolio, or comparing whole portfolios | Judging a **fund that will be one of many** a client holds |
| **Works when the portfolio is undiversified?** | **YES** | **NO** — beta ignores the specific risk being carried |

### 🔑 The disagreement test — the favourite exam question

> **If two funds rank the SAME on Sharpe and Treynor, both are well diversified.**
> **If a fund ranks BETTER on Treynor than on Sharpe, it is carrying a lot of UNSYSTEMATIC risk — i.e. it is poorly diversified.**

**Worked example.** Rf = **6%**, market σ = **16%**.

| Fund | Return | σ | β | **Sharpe** | **Treynor** |
|---|---|---|---|---|---|
| **Fund X** | 15% | 25% | 1.00 | 9 ÷ 25 = **0.36** | 9 ÷ 1.00 = **9.00** |
| **Fund Y** | 13% | 14% | 0.80 | 7 ÷ 14 = **0.50** | 7 ÷ 0.80 = **8.75** |

**They disagree.** Y is better on Sharpe; X is better on Treynor. **Why?**

- Fund X's systematic risk = β × σm = 1.00 × 16 = **16%**, yet its total σ is **25%**. Its **specific risk = √(25² − 16²) = √369 = 19.2%**, and its **R² is only 256/625 = 41%**.
- Fund Y's systematic risk = 0.80 × 16 = **12.8%** against a total σ of **14%**. Its specific risk is only **√(196 − 163.8) = 5.7%**, and its **R² is 84%**.

**Fund X is badly diversified.** Sharpe sees that and penalises it; Treynor is blind to it. So:

- For a client putting **everything** into one of them → choose **Y** (use Sharpe)
- For a client adding a **small satellite sleeve** to an already diversified portfolio → **X**'s specific risk will wash out, so **X** on Treynor is defensible

> ⚠️ **Trap.** For a **well-diversified** portfolio the two measures give the **same ranking**. The exam only makes them disagree when it wants you to spot **poor diversification**.

---

### 16.4.4 Sortino Ratio

> **Sortino Ratio = (Rp − MAR) ÷ Downside deviation**

Identical to Sharpe except the denominator counts **only the bad volatility**. The target (MAR) may be **0%**, the **risk-free rate**, or a client's **required return** — you must state which.

**Why it exists:** investors do not experience an unexpectedly *large gain* as risk. Penalising a manager for upside volatility is illogical, and it particularly misjudges strategies with **asymmetric** return profiles.

**Worked example — using the same fund as §16.3.1.** Returns **0%, 3%, 20%, 18%, 19%**; mean **12%**; **Rf = MAR = 6%**; σ = **8.65%**; downside deviation = **3.00%**.

- **Sharpe = (12 − 6) ÷ 8.65 = 0.69**
- **Sortino = (12 − 6) ÷ 3.00 = 2.00**

The Sortino ratio is nearly **three times** the Sharpe ratio, because most of this fund's volatility was **upside** volatility that hurt nobody.

> 🧠 **Memory hook — "Sortino is Sharpe with the good news removed from the denominator."**

> ⚠️ **Trap.** Sortino is **always ≥ Sharpe** in practice, because downside deviation ≤ total σ. Do not read a high Sortino as proof of skill — check that the MAR used is the same before comparing two funds.

---

### 16.4.5 Information Ratio (Appraisal Ratio)

> **Information Ratio = (Rp − Rb) ÷ Tracking Error = Active return ÷ Active risk = Alpha ÷ Tracking Error**

This is the **manager-skill ratio**: it asks how much **excess return over the benchmark** the manager produced **per unit of the benchmark-relative risk taken to get it** — and, crucially, **how consistently**.

**Worked example.** A fund returned **16%** against a benchmark of **12.5%**, with a tracking error of **5%**.

- Active return = 16 − 12.5 = **3.5%**
- **IR = 3.5 ÷ 5 = 0.70**

**Now compare two managers with identical outperformance:**

| Manager | Active return | Tracking error | IR | Reading |
|---|---|---|---|---|
| **Manager 1** | +3.0% | 3.0% | **1.00** | Steady, repeatable outperformance |
| **Manager 2** | +3.0% | 12.0% | **0.25** | Same result, achieved by huge bets — far more likely to be luck |

Rough industry convention for interpreting the IR:

| IR | Reading |
|---|---|
| **0.50** | Good |
| **0.75** | Very good |
| **1.00** | Exceptional — and rare |

> 🧠 **Memory hook — "Sharpe is versus cash; Information Ratio is versus the benchmark."** Sharpe subtracts **Rf** and divides by **total** σ. IR subtracts **Rb** and divides by **tracking error**.

> ⚠️ **Trap.** A **negative IR** means the manager underperformed the benchmark — you paid an active fee for a worse-than-index result. A **near-zero tracking error with near-zero active return** is a **closet index fund** charging active fees.

---

### 16.4.6 M² — the Modigliani and Modigliani Measure

> **M² = Rf + [(Rp − Rf) ÷ σp] × σm = Rf + (Sharpe ratio of the portfolio × σm)**
> **M² alpha = M² − Rm**

M² takes the Sharpe ratio's information and expresses it as a **percentage return** — the return the portfolio *would have earned* if it had been geared up or down to exactly the **market's level of risk**. That makes it directly comparable to the index return, which is far more intuitive for a client than "0.60 versus 0.50".

**Worked example.** Fund return **21%**, fund σ **25%**; **Rf = 6%**; market return **14%**, market σ **15%**.

- Fund Sharpe = (21 − 6) ÷ 25 = **0.60**
- **M² = 6 + (0.60 × 15) = 6 + 9 = 15.0%**
- **M² alpha = 15.0 − 14.0 = +1.0 percentage point**

**Proof by construction — how the "risk-matching" actually works.** To bring the fund's 25% volatility down to the market's 15%, hold **60%** in the fund and **40%** in T-bills (0.60 × 25 = 15% ✓).

- That blend returns (0.60 × 21%) + (0.40 × 6%) = 12.6 + 2.4 = **15.0%** ✓ — exactly M².
- At **identical risk** to the index, the fund's strategy delivers **15%** against the index's **14%**. It genuinely added **1 percentage point**.

> 🧠 **Memory hook — "M² is the Sharpe ratio translated into rupees a client can understand."** Same ranking as Sharpe, always — but expressed as a return, not a ratio.

> ⚠️ **Trap.** M² and Sharpe **always rank funds identically** (M² is a positive linear transformation of Sharpe). M² adds interpretability, not new information.

---

### Choosing the right measure — the decision table

| The situation | Use | Because |
|---|---|---|
| The portfolio is the client's **entire** wealth | **Sharpe** | Total risk is what the client actually bears |
| The fund is **one sleeve** of a diversified portfolio | **Treynor** | Specific risk is diversified away elsewhere |
| The client cares about **losses**, not volatility | **Sortino** | Only downside deviation is penalised |
| Judging an **active manager against a benchmark** | **Information Ratio** | Measures skill and consistency net of the index |
| Explaining risk-adjusted performance to a **client in plain %** | **M²** | Restates Sharpe as a comparable return |
| Asking "did the manager beat what their risk level required?" | **Jensen's Alpha** | Excess over the CAPM-required return |

---

## 16.5 Performance Evaluation — Benchmarking and Peer Group Analysis

### 16.5.1 Characteristics of a Good Benchmark Index

A benchmark that fails any of these produces a meaningless comparison.

| Characteristic | What it requires |
|---|---|
| **Specified in advance** | Chosen **before** the period, never selected afterwards to flatter the result |
| **Appropriate** | Matches the portfolio's **asset class, style, market-cap and geography** |
| **Measurable** | Its return can be calculated regularly and independently |
| **Unambiguous** | Constituents and weights are clearly identifiable |
| **Reflective of current investment opinion** | The manager actually knows and has views on its constituents |
| **Accountable / owned** | The manager accepts it as the standard for their work |
| **Investable** | It is possible to hold the index passively as an alternative |

> 🧠 **Memory hook — SAMURAI**: **S**pecified in advance, **A**ppropriate, **M**easurable, **U**nambiguous, **R**eflective of current investment opinion, **A**ccountable, **I**nvestable.

**Practical index requirements:** transparent published rules, adequate **liquidity** in the constituents, low **turnover** (so replication is cheap), a long published history, wide acceptance, and a **Total Return** version.

**Indian benchmarks you should recognise:**

| Portfolio | Typical benchmark |
|---|---|
| Large-cap equity | **NIFTY 50 TRI** or **BSE SENSEX TRI** |
| Diversified / multi-cap | **NIFTY 500 TRI** |
| Mid-cap | **NIFTY Midcap 150 TRI** |
| Small-cap | **NIFTY Smallcap 250 TRI** |
| Debt | **CRISIL** bond index family |
| Liquid | **NIFTY / CRISIL Liquid Fund Index** |
| Gold | Domestic price of physical gold |

> ⚠️ **Trap — PRI versus TRI.** A **Price Return Index (PRI)** ignores dividends; a **Total Return Index (TRI)** reinvests them. Benchmarking a fund (which receives dividends) against a **PRI** artificially flatters the fund by roughly the dividend yield each year. **SEBI has mandated that mutual funds benchmark against TRI**, precisely to stop this.

**SEBI's two-tier benchmark structure for mutual funds:** a **Tier-1 benchmark** reflecting the **scheme category** (so all funds in a category are comparable) and an optional **Tier-2 benchmark** reflecting the **manager's particular strategy or style**.

---

### 16.5.2 Customised (Blended) Benchmarks

When no single index matches the mandate — the usual case for a multi-asset client portfolio — you construct a **blended benchmark** by weighting indices in the portfolio's **strategic asset allocation** proportions.

**Worked example.** A balanced client portfolio with a strategic allocation of **65% equity / 35% debt**. Over the year the NIFTY 50 TRI returned **15%** and the chosen CRISIL bond index returned **7%**.

- **Benchmark return = (0.65 × 15%) + (0.35 × 7%) = 9.75% + 2.45% = 12.20%**

If the portfolio returned **12.9%**, the active return is **+0.70%** — a far more honest verdict than "it lagged the NIFTY's 15%", which would have compared a balanced portfolio to a pure equity index.

**Rules for building one:** use the **strategic** (long-run policy) weights, not the current actual weights; **rebalance** the benchmark on the same schedule as the policy; specify it **in advance and in the IPS**; and use **total return** versions of each index.

---

### 16.5.3 ⭐ Benchmarking Errors

| Error | What goes wrong |
|---|---|
| **Style / category mismatch** | A small-cap fund compared to the NIFTY 50 — you measure the **small-cap premium**, not skill |
| **Using a PRI instead of a TRI** | Fund looks better by roughly the dividend yield every year |
| **Choosing the benchmark after the fact** | "Benchmark shopping" — picking whichever index the fund happened to beat |
| **Cherry-picked start and end dates** | Point-to-point returns from a market bottom flatter any fund. Fix: **rolling returns** |
| **Too short a period** | One year is noise. Judge over a **full market cycle**, 3–5 years or more |
| **Ignoring risk** | Comparing raw returns of a β = 1.4 fund and a β = 0.7 fund |
| **Gross versus net mismatch** | Fund's gross return against an index; the index has no fees, so the fund must be shown **net** |
| **A non-investable benchmark** | If you cannot buy it, it is not a fair alternative |
| **Ignoring the cash/currency position** | A fund holding 15% cash is not running the index's risk |
| **Survivorship bias in the comparison set** | Dead funds vanish, so the surviving average looks better than reality |
| **Composition drift** | The fund's style changes but the benchmark does not (or the index is reconstituted and history is restated) |

---

### 16.5.4 Managers' Universe Analysis (Peer Group Analysis)

Comparing a fund against the **universe of funds with the same mandate**, usually via **quartile rankings** — top quartile, second quartile, and so on. It answers "how did this manager do against everyone else facing the same opportunity set?"

**Strengths:** it captures conditions the index cannot (if every large-cap manager lost 12% in a crash, a −10% result is strong); it reflects real, achievable, **net-of-cost** outcomes; and quartile rankings are intuitive for clients.

**Weaknesses — all examinable:**

| Weakness | Why it distorts |
|---|---|
| **Survivorship bias** | Poor funds are merged or wound up and leave the universe, lifting the apparent average |
| **The universe is not investable** | You cannot buy "the median manager" |
| **Not risk-adjusted** | The top quartile in a bull market is often just the highest-beta quartile |
| **Composition changes** | The peer group's membership shifts over time, so rankings are not comparable across periods |
| **Category definitions are loose** | Funds classified alike may run very different mandates |
| **Small samples** | With 15 funds in a category, quartile boundaries are statistically fragile |
| **Self-selection / reporting bias** | Voluntary databases attract good records |

> ⚠️ **Trap.** Peer analysis and benchmark analysis are **complements, not substitutes**. A fund can be **top quartile among peers and still below its index** if the whole category underperformed. Always look at both.

---

## 16.6 ⭐⭐ Performance Attribution Analysis

**Attribution decomposes the difference between the portfolio's return and the benchmark's return into the specific decisions that caused it.** It converts "we beat the index by 2.1%" into "we beat it because of X, despite Y" — which is what tells you whether the result is repeatable.

### 16.6.1 & 16.6.2 Asset/Sector Allocation and Selection

> **Total active return = Allocation effect + Selection effect + Interaction effect**

> **Allocation = Σ (wₚ − w_b) × (R_b,sector − R_b,total)** — was the manager overweight the sectors that did well?
> **Selection = Σ w_b × (Rₚ,sector − R_b,sector)** — inside each sector, did the manager pick better stocks?
> **Interaction = Σ (wₚ − w_b) × (Rₚ,sector − R_b,sector)** — the joint effect of over-weighting a sector *and* picking well in it

**Full worked example.**

| | **Benchmark weight** | **Benchmark return** | **Portfolio weight** | **Portfolio return** |
|---|---|---|---|---|
| **Equity** | 60% | 12.0% | 75% | 14.0% |
| **Debt** | 40% | 7.0% | 25% | 6.5% |

- **Benchmark return** = (0.60 × 12) + (0.40 × 7) = 7.2 + 2.8 = **10.00%**
- **Portfolio return** = (0.75 × 14) + (0.25 × 6.5) = 10.5 + 1.625 = **12.125%**
- **Total active return = +2.125%**

**Allocation effect** (weight difference × the sector's benchmark return relative to the total benchmark):
- Equity: (0.75 − 0.60) × (12 − 10) = 0.15 × 2 = **+0.30%**
- Debt: (0.25 − 0.40) × (7 − 10) = (−0.15) × (−3) = **+0.45%**
- **Allocation total = +0.75%** — the manager was overweight the better-performing asset and underweight the weaker one. Both bets paid.

**Selection effect** (benchmark weight × the return difference within each sector):
- Equity: 0.60 × (14 − 12) = **+1.20%**
- Debt: 0.40 × (6.5 − 7) = **−0.20%**
- **Selection total = +1.00%** — excellent stock picking in equity, slightly poor in debt.

**Interaction effect:**
- Equity: 0.15 × (14 − 12) = **+0.30%**
- Debt: (−0.15) × (6.5 − 7) = **+0.075%**
- **Interaction total = +0.375%**

**Check: 0.75 + 1.00 + 0.375 = 2.125%** ✓ — exactly the active return.

**The two-term simplification** (used when interaction is folded into selection by using *portfolio* weights):
- Selection = (0.75 × 2) + (0.25 × −0.5) = 1.5 − 0.125 = **+1.375%**
- Allocation **+0.75%** + Selection **+1.375%** = **2.125%** ✓ — the same total.

**What the manager should be told:** the outperformance was **roughly two-thirds selection and one-third allocation**, and the *only* negative contribution came from **debt security selection** — a specific, actionable finding no headline return figure could deliver.

> 🧠 **Memory hook — "Allocation is which buckets; Selection is what's inside the bucket."**

> ⚠️ **Trap.** Positive allocation with negative selection (or the reverse) is common and is exactly what makes attribution useful — a manager may be a good asset allocator and a poor stock picker, and should then run a portfolio of index funds with an active allocation overlay.

---

### 16.6.3 Market Timing versus Selectivity

| | **Market timing** | **Selectivity (stock picking)** |
|---|---|---|
| **The decision** | Vary **market exposure / portfolio beta** ahead of market moves | Choose **which securities** to hold within the exposure |
| **Successful version** | Raise beta before rallies; cut beta or hold cash before falls | Hold securities that outperform their sector or the index |
| **Evidence of it** | The portfolio's beta or equity weight **changes systematically ahead of** market moves | Consistent positive alpha with a stable beta |
| **How it is tested** | **Treynor–Mazuy** (adds a squared market-return term to the regression) and **Henriksson–Merton** (dual-beta model) | Jensen's alpha; selection effect in attribution |
| **Reliability** | Consistently poor — very few managers time markets successfully | More commonly demonstrated, though still difficult |

**Fama's decomposition of total excess return** ties the whole chapter together:

> **Rp − Rf = [Return for systematic risk: β(Rm − Rf)] + [Selectivity: Jensen's alpha]**
> and **Selectivity = Net selectivity + Return required for imperfect diversification**

---

### 16.6.4 ⭐ Net Selectivity

Jensen's alpha rewards a manager for *all* return above the **CAPM** requirement. But CAPM only charges for **systematic** risk. If the manager also took a lot of **avoidable specific risk**, part of that "alpha" is merely compensation for the risk of being under-diversified — not skill.

**Net selectivity strips that part out** by charging the manager for **total** risk instead of just beta:

> **Net selectivity = Rp − [Rf + (σp ÷ σm) × (Rm − Rf)]**
> **Net selectivity = Jensen's alpha − Return required for imperfect diversification**

**Worked example.** Rp = **18%**, σp = **22%**, β = **1.10**; Rf = **6%**, Rm = **13%**, σm = **16%**.

1. **CAPM required return** = 6 + 1.10 × (13 − 6) = 6 + 7.7 = **13.70%**
2. **Jensen's alpha (gross selectivity)** = 18 − 13.70 = **+4.30%**
3. **Return required if we charge for TOTAL risk** = 6 + (22 ÷ 16) × 7 = 6 + (1.375 × 7) = 6 + 9.625 = **15.625%**
4. **Cost of imperfect diversification** = 15.625 − 13.70 = **1.925%**
5. **Net selectivity = 18 − 15.625 = +2.375%** (and indeed 4.30 − 1.925 = **2.375%** ✓)

**Reading it:** of the manager's **4.30%** headline alpha, **1.925 percentage points were simply payment for carrying undiversified risk the client could have removed for free**. The **genuine, skill-based contribution is 2.375%** — still positive, so this manager passes the harder test.

> ⚠️ **Trap.** **Net selectivity can be negative while Jensen's alpha is positive.** That is precisely the diagnosis of a manager whose "outperformance" came from concentration, not skill. If **σp/σm = β** the portfolio is perfectly correlated with the market (fully diversified) and **net selectivity = alpha**.

---

### 16.6.5 Local Currency versus Foreign Currency Returns

When an Indian client invests abroad, the rupee return has **two** components — and they **compound**, they do not add.

> **Return in INR = (1 + Local currency return) × (1 + Currency return) − 1**
> **Currency return = (Closing INR/USD ÷ Opening INR/USD) − 1** — a *rise* in the INR/USD rate is **rupee depreciation**, which is a **gain** for the Indian investor

**Worked example 1 — rupee depreciates.** Mr Shah invests **₹10,00,000** in a US equity fund when the rate is **₹83/USD**. The fund returns **12% in USD** and the rupee ends at **₹87.15/USD**.

- Currency return = (87.15 ÷ 83) − 1 = **+5.0%**
- **Return in INR = (1.12 × 1.05) − 1 = 1.176 − 1 = 17.60%**
- His ₹10,00,000 becomes **₹11,76,000**

Note that **12% + 5% = 17%**, but the true answer is **17.6%**. The extra **0.6%** is the cross term (0.12 × 0.05).

**Worked example 2 — rupee appreciates.** Same 12% USD return, but the rupee strengthens from ₹83 to **₹80.51/USD**.

- Currency return = (80.51 ÷ 83) − 1 = **−3.0%**
- **Return in INR = (1.12 × 0.97) − 1 = 1.0864 − 1 = 8.64%**

A 12% dollar gain became an **8.64%** rupee gain. **The currency can consume a third of the return.**

> 🧠 **Memory hook — a weak rupee is a tailwind for an Indian investor holding foreign assets.**

> ⚠️ **Trap — never simply add the two returns.** For small numbers adding is a fair approximation, but the exam usually chooses figures where the cross term is visible, and the "just added" figure is offered as a distractor.

**In practice:** performance should be attributed separately to the **local-market decision** and the **currency decision**, since a manager may be skilled at one and not the other, and currency exposure can be hedged independently (at a cost roughly equal to the interest-rate differential).

---

## ⚡ Quick Revision Sheet

| Concept | The one-line answer |
|---|---|
| Performance is defined by | **Return AND risk** together — never return alone |
| Holding Period Return | **(End − Begin + Income) ÷ Begin** |
| TWRR | Geometric chaining of sub-period returns; **cash flows neutralised** |
| MWRR | The **IRR** of the cash flows; cash-flow timing fully counted |
| TWRR measures | **The manager's skill** — SEBI's required basis for PMS disclosure |
| MWRR measures | **The investor's actual experience** (a client's XIRR) |
| TWRR = MWRR when | There are **no cash flows** during the period |
| MWRR > TWRR when | The client added money **before a strong** period |
| AMR | Simple average of periodic returns |
| GMR | **[(1+R₁)…(1+Rₙ)]^(1/n) − 1** — the compounded average |
| The inequality | **AMR ≥ GMR always**; equal only if all returns are identical |
| Gap widens with | **Volatility** — approximately **GMR ≈ AMR − σ²/2** |
| +50% then −50% | AMR **0%**; GMR **−13.4%**; ₹1,00,000 → **₹75,000** |
| Use AMR for | Estimating the **next single period's** expected return |
| Use GMR for | Reporting **realised multi-period** performance |
| Net return | Gross **minus** fees, TER, brokerage, STT, custody, **18% GST**, exit load |
| Post-tax | Net **minus tax** — investor-specific, so never published by the fund |
| Equity taxation | STCG **20%** (≤12 m); LTCG **12.5%** above **₹1.25 lakh** (>12 m) |
| Debt fund taxation (bought on/after 1 Apr 2023) | **Slab rate**, whatever the holding period |
| CAGR | **(EV ÷ BV)^(1/n) − 1** — the GMR from two endpoints |
| CAGR's weakness | **Hides the path entirely** — says nothing about volatility; start-date sensitive |
| Fix for start-date sensitivity | **Rolling returns** |
| Annualising a return | **(1 + r)^periods − 1** — compound, never multiply |
| Annualising risk | **σ × √periods** — 4% monthly → **13.86%**; 1% daily → **15.87%** |
| Why √t | **Variances add** over time, so standard deviation grows with **√t** |
| SEBI return-display rule | **< 1 year → absolute**; **≥ 1 year → CAGR** |
| Cash drag | Return lost by holding uninvested cash **in a rising market** |
| Cash-drag-adjusted return | **(Rp − w_cash × R_cash) ÷ (1 − w_cash)** |
| Beta return | The return earned merely for **market exposure** — cheap to buy |
| Alpha (Jensen's) | **Rp − [Rf + β(Rm − Rf)]** — value added over the CAPM requirement |
| Alpha is NOT | **Rp − Rm** — that ignores the beta taken |
| Portfolio return | **Σ wᵢRᵢ** — a **weighted average** (risk is not) |
| Total risk | **Standard deviation** — punishes upside and downside equally |
| Downside deviation | **√[Σ(shortfalls below MAR)² ÷ n]** |
| Maximum drawdown | Largest **peak-to-trough** fall |
| VaR | Loss not exceeded at a stated **confidence** over a stated **horizon** |
| Volatility bands | **±1σ ≈ 68%**, **±2σ ≈ 95%**, **±3σ ≈ 99.7%** |
| σ's blind spots | **Fat tails**, liquidity risk, credit risk, backward-looking |
| Tracking error | **Standard deviation of the ACTIVE return** (portfolio − benchmark) |
| Tracking difference | The simple **return gap**; tracking error is its **volatility** |
| SEBI TE cap | **2%** for equity index funds/ETFs on rolling one-year data |
| Tracking error is NOT | Underperformance — consistent outperformance has low TE |
| Total risk = | **Systematic + Unsystematic**; **σ²ᵢ = β²σ²ₘ + σ²ₑ** |
| Systematic risk | Market-wide, **non-diversifiable**, measured by **β**, and **rewarded** |
| Unsystematic risk | Company-specific, **diversifiable**, and **NOT rewarded** |
| Diversification benefit | Most specific risk gone within roughly **20–30 well-spread** stocks |
| R² | Share of variance explained by the market; **low R² → β, α, Treynor unreliable** |
| Beta formula | **Cov(i,m) ÷ Var(m) = ρ × σᵢ ÷ σₘ** |
| Beta example | ρ 0.80, σᵢ 24%, σₘ 16% → **β = 1.20** |
| Portfolio beta | **Weighted average** of component betas |
| Liquidity risk | Cannot sell at a fair price; **not captured by σ** (volatility smoothing) |
| Credit risk | Default/downgrade; **AAA → D**; compensated by the **credit spread** |
| **Sharpe** | **(Rp − Rf) ÷ σp** — excess return per unit of **TOTAL** risk |
| **Treynor** | **(Rp − Rf) ÷ βp** — excess return per unit of **SYSTEMATIC** risk |
| Sharpe vs Treynor | Sharpe for a **standalone** portfolio; Treynor for a **sub-portfolio** in a diversified whole |
| If they disagree | Better on **Treynor** than Sharpe → **poorly diversified** (high specific risk) |
| If they agree | The portfolio is **well diversified** |
| **Sortino** | **(Rp − MAR) ÷ downside deviation** — penalises **only bad** volatility |
| **Information Ratio** | **(Rp − Rb) ÷ Tracking Error = alpha ÷ TE** — skill **and consistency** |
| IR benchmarks | **0.5 good, 0.75 very good, 1.0 exceptional** |
| **M²** | **Rf + (Sharpe × σₘ)** — Sharpe restated as a **return %** |
| M² alpha | **M² − Rm** |
| M² ranking | **Always identical to Sharpe** — it adds interpretability, not information |
| Good benchmark (SAMURAI) | **S**pecified in advance, **A**ppropriate, **M**easurable, **U**nambiguous, **R**eflective, **A**ccountable, **I**nvestable |
| PRI vs TRI | PRI **omits dividends**; SEBI mandates **TRI** benchmarking for mutual funds |
| SEBI benchmark tiers | **Tier 1** = category index; **Tier 2** = manager's style |
| Customised benchmark | Blend indices in the **strategic** asset-allocation weights |
| Blended example | 65% NIFTY TRI @15% + 35% bond index @7% = **12.2%** |
| Benchmarking errors | Style mismatch, PRI not TRI, after-the-fact choice, cherry-picked dates, too-short period, ignoring risk, gross vs net, non-investable, survivorship bias |
| Peer/universe analysis | Quartile ranking against same-mandate funds |
| Peer analysis weaknesses | **Survivorship bias**, not investable, **not risk-adjusted**, shifting composition, small samples |
| Attribution identity | **Active return = Allocation + Selection + Interaction** |
| Allocation effect | **Σ (wₚ − w_b) × (R_b,sector − R_b,total)** — "which buckets" |
| Selection effect | **Σ w_b × (Rₚ,sector − R_b,sector)** — "what's inside the bucket" |
| Market timing | Varying **beta / market exposure**; tested by **Treynor–Mazuy** and **Henriksson–Merton** |
| Selectivity | Security picking = **Jensen's alpha** |
| Net selectivity | **Rp − [Rf + (σp ÷ σₘ)(Rm − Rf)]** = alpha **minus** the cost of imperfect diversification |
| Net selectivity = alpha when | **σp/σₘ = β** — the portfolio is fully diversified |
| Foreign currency return | **(1 + R_local) × (1 + R_currency) − 1** — **multiply, never add** |
| Rupee depreciation | A **gain** for an Indian holder of foreign assets |

> **Exam tip:** in every numerical question, first ask **"which risk is in the denominator?"** — σ (Sharpe), β (Treynor), downside deviation (Sortino) or tracking error (Information Ratio). Getting that one choice right is worth more marks than the arithmetic. The three highest-frequency traps are: **alpha is not simply Rp − Rm**; **AMR always exceeds GMR and the gap is the cost of volatility**; and **foreign-currency returns multiply rather than add**.
