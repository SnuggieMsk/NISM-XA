# Chapter 15: Portfolio Construction Process — Short Notes

> **Module 5 · Portfolio Construction, Performance Monitoring and Evaluation (20 marks).**
> Chapter 14 gave you the *mathematics* of a portfolio. This chapter gives you the *process* — how a real Investment Adviser turns a real person's messy life into a written plan. It is the most heavily examined chapter in Module 5 because it is what an IA actually does for a living. Two things dominate the marks: the **Investment Policy Statement (IPS)** and the **strategic-versus-tactical asset allocation** distinction. Learn those cold.

---

## 15.1 ⭐ Why the Asset Allocation Decision Matters More Than Anything Else

**Asset allocation** is the decision of **how to divide a portfolio across asset classes** — equity, debt, cash, gold, real estate, and alternatives — *before* deciding which particular security to buy inside each class.

Most beginners believe investing is about picking winners. The evidence says otherwise.

### The three decisions an investor makes

| Decision | Example | How much it explains |
|---|---|---|
| **1. Asset allocation** | "60% equity, 30% debt, 10% gold" | **The overwhelming majority of return variability** |
| **2. Security selection** | "HDFC Bank rather than ICICI Bank" | A small residual |
| **3. Market timing** | "Move to cash now, back in later" | A small — and usually **negative** — residual |

### 🔑 The empirical support (15.16.1) — memorise these three studies

| Study | What it examined | Headline finding |
|---|---|---|
| **Brinson, Hood & Beebower (1986)** | 91 large US pension plans, 1974–1983 | Asset allocation policy explained **93.6%** of the variation in quarterly returns |
| **Brinson, Singer & Beebower (1991)** | 82 pension plans, 1977–1987 | Confirmed the result — approximately **91.5%** |
| **Ibbotson & Kaplan (2000)** | Mutual funds and pension funds | Refined it: **~90%** of return variability **over time**, **~40%** of variation **across funds**, and **~100%** of the **level** of return |

> 🧠 **Memory hook — "90 / 40 / 100."**
> **90%** of *why your portfolio wobbled over time* = asset allocation.
> **40%** of *why your portfolio differs from your neighbour's* = asset allocation.
> **100%** of the *level* of long-run return = asset allocation (before costs).

> ⚠️ **The single most common exam trap in this chapter.** The Brinson result is about the **variability (variance) of returns over time**, *not* "93.6% of the return". Candidates who read it as "asset allocation gives you 93.6% of your money" get the follow-up question wrong. Ibbotson & Kaplan wrote their paper specifically to correct that misreading — the title is literally *"Does Asset Allocation Policy Explain 40, 90, or 100 Percent of Performance?"*

### Why it works out this way

1. **Asset classes behave very differently from each other, but securities inside a class behave alike.** Two large-cap Indian banks move together far more than equity and G-Secs do. So switching from Bank A to Bank B changes little; switching from equity to G-Secs changes everything.
2. **Risk is set at the asset-class level.** A 90% equity portfolio is a high-risk portfolio regardless of which stocks are in it.
3. **Selection and timing are zero-sum before costs and negative after them.** For every adviser who buys, another sells. After brokerage, STT, stamp duty, impact cost and taxes, the average active rupee must underperform the average passive rupee.

**The practical consequence for an IA:** spend your effort on getting the **allocation** right for the client's goals, horizon and risk profile. That is where the value is. Fine-tuning the choice between two well-run flexi-cap funds is a rounding error by comparison.

---

## 15.2 ⭐ Correlation Across Asset Classes and Securities

Chapter 14 proved that portfolio risk falls when holdings do **not** move together. Correlation (**ρ**) is the number that measures "moving together."

**ρ always lies between −1 and +1.**

| ρ | Meaning | Diversification benefit |
|---|---|---|
| **+1** | Perfectly together | **None** — portfolio risk is the plain weighted average |
| **+0.5 to +0.9** | Strongly together | Small |
| **0** | Unrelated | Substantial |
| **−0.5** | Usually opposite | Large |
| **−1** | Perfectly opposite | **Risk can be driven to zero** with the right weights |

### Correlation across Indian asset classes — the shape you must know

*(Illustrative, to fix the pattern in your mind — the exam tests the ranking, not decimals.)*

| Pair | Typical correlation | Why |
|---|---|---|
| Two large-cap Indian equity funds | **Very high, near +0.9** | They hold largely the same Nifty names |
| Large-cap equity vs mid-cap equity | **High** | Same economy, same risk appetite cycle |
| Indian equity vs Indian corporate debt | **Low, sometimes slightly negative** | Driven by earnings vs by interest rates |
| Indian equity vs gold | **Low to negative** | Gold is a **safe haven** — it tends to rise in panics |
| Indian equity vs US equity (in ₹) | **Moderate, and rises in crises** | Global risk appetite is common, but the ₹/$ move adds a cushion |
| G-Secs vs corporate bonds | **High** | Both driven mainly by the level of rates |

> 🧠 **Memory hook — "Different engines, different correlations."**
> Equity is powered by **corporate earnings**. Debt is powered by **interest rates**. Gold is powered by **fear and the dollar**. Real estate is powered by **local supply and rental yields**. Because the engines differ, the vehicles do not arrive together — and that is the whole point of multi-asset investing.

### Worked example — what correlation is worth in rupees

Ms Iyer invests **₹10,00,000**: **60% equity** (σ = **18%**) and **40% debt** (σ = **5%**). Correlation **ρ = 0.15**.

**Step 1 — the naive (wrong) risk estimate, the weighted average:**
0.60 × 18 + 0.40 × 5 = 10.8 + 2.0 = **12.80%**

**Step 2 — the true portfolio risk:**
σ_p = √(w₁²σ₁² + w₂²σ₂² + 2w₁w₂σ₁σ₂ρ)
= √(0.36 × 324 + 0.16 × 25 + 2 × 0.60 × 0.40 × 18 × 5 × 0.15)
= √(116.64 + 4.00 + 6.48)
= √127.12 = **11.27%**

**The diversification benefit is 12.80 − 11.27 = 1.53 percentage points of risk, obtained for free** — no return was given up, because portfolio *return* is always the exact weighted average (Chapter 14).

### ⚠️ Three warnings about correlation that the exam loves

1. **Correlation is not stable.** It is estimated from history and it changes.
2. **Correlations rise towards +1 in a crisis.** In October 2008 and again in March 2020, almost everything risky fell together. **Diversification fails precisely when it is most needed.** This is why an emergency fund in cash — an asset with essentially zero correlation to anything — is non-negotiable.
3. **Correlation measures direction, not magnitude.** Two assets can have ρ = +0.9 while one is five times as volatile as the other. **Covariance** carries the magnitude; **correlation** is covariance standardised.

---

## 15.3 ⭐ The Steps in the Portfolio Construction Process

The process is a **loop, not a line** — it ends by feeding back into itself.

| # | Step | What happens |
|---|---|---|
| **1** | **Understand the client** | Data gathering: goals, income, expenses, assets, liabilities, insurance, tax status, family |
| **2** | **Analyse the financial position** | Net worth statement, cash-flow statement, ratios, emergency fund, insurance adequacy |
| **3** | **Determine objectives and constraints** | Return objective, risk objective; liquidity, horizon, tax, legal, unique needs |
| **4** | **Write the Investment Policy Statement** | The whole of steps 1–3 committed to paper and signed |
| **5** | **Form capital market expectations** | Forecast risk, return and correlation for each asset class |
| **6** | **Set the strategic asset allocation** | Combine (3) and (5) into the long-term policy mix |
| **7** | **Select products and securities** | Funds, stocks, bonds, schemes — inside each asset class |
| **8** | **Execute** | Implement, minimising cost, tax and market impact |
| **9** | **Monitor and evaluate** | Measure against the benchmark; watch the client's circumstances |
| **10** | **Rebalance and revise** | Restore target weights; update the IPS on any life event — then return to step 1 |

> 🧠 **Memory hook — "Plan, Predict, Position, Police."**
> **Plan** the client (steps 1–4) → **Predict** the markets (step 5) → **Position** the money (steps 6–8) → **Police** it forever (steps 9–10).

> ⚠️ **Exam trap.** The **client** comes before the **market**. Capital market expectations (step 5) are formed *after* the IPS (step 4), never before. An adviser who starts with "what looks cheap right now" has inverted the entire process — and, under the **SEBI (Investment Advisers) Regulations, 2013**, has also skipped the mandatory risk profiling and suitability assessment.

---

## 15.4 ⭐⭐ The Investment Policy Statement (IPS)

### What it is

**The IPS is the written document that governs the relationship between the client and the adviser and sets out how the portfolio will be managed.** It is the portfolio's constitution: a statement of *what we are trying to achieve, what we may and may not do, and how we will know whether it is working*.

It is written **at the start**, **jointly**, and **signed by both parties**.

### 15.4.1 Need and importance of an IPS

| Reason | Why it matters in practice |
|---|---|
| **Clarity of purpose** | Forces vague wishes ("I want good returns") into measurable objectives ("₹1.5 crore by 2038 for my daughter's education") |
| **Discipline in a panic** | When the Nifty falls 25%, the IPS is the document that says *we planned for this; the plan has not changed* |
| **Protects against emotion** | Rules written in calm conditions are obeyed in frightening ones — this is the IPS's single greatest value |
| **A yardstick for evaluation** | Specifies the **benchmark** in advance, so performance can be judged honestly |
| **Continuity** | If the adviser leaves, dies or is replaced, the successor knows exactly what was intended |
| **Reduces disputes** | Both parties agreed and signed; misunderstandings about mandate and risk are avoided |
| **Regulatory and compliance record** | Evidence that risk profiling and **suitability** were assessed, as SEBI requires of a Registered Investment Adviser |
| **Manages expectations** | The client sees, in advance, the range of outcomes — including the bad ones |

> 🧠 **Memory hook — "The IPS is a seatbelt, not a steering wheel."**
> It does not tell the car where to go on any given day. It stops the passenger being thrown through the windscreen when the market brakes hard.

### 15.4.2 ⭐ Constituents of an IPS

| Section | Contents |
|---|---|
| **1. Client description / background** | Who the client is, family, occupation, wealth, current holdings, the purpose of the portfolio |
| **2. Purpose and scope of the IPS** | Why the document exists and what it covers |
| **3. Duties and responsibilities** | Of the **adviser**, the **client**, the **custodian**, the **auditor**; who may give instructions |
| **4. Investment objectives** | The **return objective** and the **risk objective** — stated explicitly |
| **5. Investment constraints** | **Liquidity, time horizon, tax, legal & regulatory, unique circumstances** |
| **6. Investment guidelines** | Permitted and prohibited asset classes and instruments; use of leverage, derivatives, unlisted or illiquid assets; **exposure limits** |
| **7. Strategic asset allocation** | The long-term target weights, with **permitted bands** around each |
| **8. Benchmark and evaluation** | The benchmark for each asset class and for the portfolio as a whole; how often performance is reviewed |
| **9. Rebalancing policy** | Method (calendar / threshold), tolerance bands, who initiates |
| **10. Review procedure** | How often the IPS itself is revisited, and which events force an immediate revision |
| **11. Appendices** | Fee schedule, risk profile output, list of existing holdings, communication protocol |

> 🧠 **Memory hook for the objectives-and-constraints core — "RRTTLLU."**
> **R**eturn · **R**isk · **T**ime horizon · **T**axes · **L**iquidity · **L**egal & regulatory · **U**nique circumstances.
> The first two **R**s are the **objectives**; the remaining five are the **constraints**.

> ⚠️ **Exam trap.** An IPS does **not** contain a list of specific stocks to buy, nor a market forecast, nor a promised return. It contains **objectives, constraints, guidelines, allocation targets and review procedures**. Anything that would have to be rewritten every month does not belong in it.

### When must the IPS be revised?

Not on market moves — on **life events**:

- Marriage, divorce, birth of a child, death in the family
- Job loss, promotion, business sale, inheritance, windfall
- Serious illness or disability
- A goal being achieved, abandoned, brought forward or postponed
- A material change in tax law or in the regulations applying to the client
- The client's own risk tolerance genuinely and durably changing

> ⚠️ **A 20% market fall is NOT a reason to rewrite the IPS.** It is precisely the situation the IPS was written for. Rewriting the plan because the plan is being tested is the most expensive mistake in personal finance.

---

## 15.5 ⭐ Investment Objectives — Return and Risk

An objective must be **specific, measurable and achievable**. "Beat inflation comfortably" is not an objective; it is a mood.

### 15.5.1 The return objective

Distinguish two things:

| | **Required return** | **Desired return** |
|---|---|---|
| Meaning | What the client **must** earn to meet essential goals | What the client **would like** to earn |
| Nature | A **need** | A **want** |
| If unattainable | The goal, the horizon or the saving rate must change | It can simply be abandoned |

A return objective should always state **four things**: the number, whether it is **nominal or real**, whether **pre-tax or post-tax**, and whether it is measured as a **total return** (income + capital gain).

### 🔑 Worked example — computing a required return

Mr Sharma, aged 60, retires with a corpus of **₹1,00,00,000**. He needs **₹4,00,000** a year to live on, rising with inflation. Assume **inflation 6%** and total costs (adviser fee + fund expenses) of **1%**.

**Step 1 — the spending rate:** 4,00,000 ÷ 1,00,00,000 = **4.0%**

**Step 2 — the additive approximation (quick, used in exams):**
4.0% + 6.0% + 1.0% = **11.0%**

**Step 3 — the exact multiplicative calculation:**
(1.04 × 1.06 × 1.01) − 1 = 1.113424 − 1 = **11.34%**

**Step 4 — the adviser's judgement.** An 11.34% *nominal, post-cost* return needs a portfolio with a heavy equity weight, which a 60-year-old drawing an income may not be able to tolerate. The honest conversation is: **reduce the withdrawal to ₹3,00,000, work part-time, or accept a higher risk of running out.** Stating the required return is what makes that conversation possible — that is the value of the arithmetic.

> ⚠️ **Exam trap.** Costs must be **added** to the required return, not ignored. A 1% fee does not reduce the target — it raises the gross return the portfolio must earn.

### 15.5.2 The risk objective — ability versus willingness

| | **Ability to take risk** (risk **capacity**) | **Willingness to take risk** (risk **tolerance/attitude**) |
|---|---|---|
| Nature | **Objective, financial, measurable** | **Subjective, psychological** |
| Determined by | Wealth relative to goals, **time horizon**, stability and security of income, size and urgency of liabilities, insurance cover, number of dependants | Personality, past experience of loss, financial literacy, temperament |
| How assessed | Financial statements and cash-flow analysis | **Risk-profiling questionnaire**, conversation |
| Can it be changed? | Only slowly — by saving more or earning more | Can be raised through **education** |

### ⭐ The conflict rule — heavily examined

| Situation | What the adviser does |
|---|---|
| **Ability HIGH, willingness LOW** | Educate the client about long-run asset behaviour — but if the anxiety is genuine, **follow the lower (willingness)**. A client who abandons a plan in a crash is worse off than one who never took the risk. |
| **Ability LOW, willingness HIGH** | **Follow the lower (ability).** Never let a client take risk their finances cannot survive, however enthusiastic they are. This is where the adviser must be firmest. |
| **Both aligned** | Straightforward — set the allocation accordingly |

> 🧠 **Memory hook — "The lower of the two governs; the adviser may educate, never override."**
> But the two errors are not symmetric: overriding low **willingness** produces a panicked client; overriding low **ability** produces a ruined one.

**How a risk objective is stated:**

- **Absolute:** "The portfolio's annual standard deviation should not exceed **10%**", or "a loss greater than **₹8,00,000** in any 12-month period is unacceptable."
- **Relative:** "Tracking error against the benchmark should not exceed **4%** a year."

### Worked example — turning a rupee loss limit into a risk number

Mr Sharma says a loss of more than **₹8,00,000 on ₹1,00,00,000** — that is **8%** — in any one year would be unacceptable. Expected return is **11%**.

Using the normal approximation, an outcome **two standard deviations below the mean** is roughly a 1-in-40 event:
11% − 2σ = −8% → 2σ = 19% → **σ = 9.5%**

**So the portfolio's standard deviation must be about 9.5% or lower** — which, on the risk numbers in section 15.2, points to an allocation of roughly **50% equity / 50% debt**, not 80% equity. The client's own sentence has just chosen his asset allocation for him.

---

## 15.6 ⭐ Investment Constraints

Five constraints, always in the same order in an IPS. Objectives say what you *want*; constraints say what you are *allowed* to do.

### 15.6.1 Liquidity constraint

**The need for cash — planned or unplanned — that the portfolio must be able to meet without selling at a bad price.**

| Type | Examples |
|---|---|
| **Planned, near-term** | School fee in April, wedding next winter, a car purchase, an insurance premium |
| **Unplanned** | Medical emergency, job loss, urgent family need |
| **Ongoing** | A retiree's monthly withdrawal; a charitable trust's annual disbursement |

- Meet it with **cash, liquid funds, overnight funds, ultra-short duration funds, sweep-in deposits** — never with equity.
- The universal baseline: an **emergency fund of 3 to 6 months' expenses** (6 to 12 months if income is irregular — a business owner, a professional on contract, a single earner).
- **Illiquid holdings raise the liquidity constraint:** physical real estate, unlisted shares, PPF (15-year), ELSS (**3-year lock-in**), NPS (essentially until 60), and Sovereign Gold Bonds (8-year tenor, exit permitted from year 5 on coupon dates) cannot be relied upon for emergencies.

> ⚠️ **Exam trap.** Liquidity is about **converting to cash quickly at a fair price**, not about whether an asset is "safe". A ₹50 lakh flat is a low-risk asset with **terrible** liquidity. A liquid fund is a modest-return asset with **excellent** liquidity.

### 15.6.2 Time horizon constraint

**How long the money can stay invested before it is needed.**

| Horizon | Typical suitable allocation |
|---|---|
| **Under 1 year** | Liquid / overnight / ultra-short funds; **no equity at all** |
| **1–3 years** | Short-duration debt, arbitrage funds, small equity if any |
| **3–5 years** | Balanced / hybrid, moderate equity |
| **5–10 years** | Equity-oriented |
| **Over 10 years** | Predominantly equity |

- Horizons may be **single-stage** (one goal, one date) or **multi-stage** (education in 8 years, then retirement in 25 — each leg gets its own allocation).
- **Longer horizon ⇒ higher ability to take risk**, because there is time to recover from a fall and because equity's *annualised* return becomes far less variable as the period lengthens.
- The horizon shortens by one year every year. **A goal 3 years away must be de-risked whether or not markets are attractive.**

### 15.6.3 Tax constraint

Tax turns a gross return into the only number the client can spend.

| Item | Position (India, FY 2024-25 onwards) |
|---|---|
| **Listed equity / equity mutual funds — short term** (held ≤ 12 months) | **20%** under Section 111A |
| **Listed equity / equity mutual funds — long term** (held > 12 months) | **12.5%** under Section 112A, on gains **above ₹1,25,000** a year |
| **Debt mutual funds bought on or after 1 April 2023** | Gains taxed at the investor's **slab rate**, with **no long-term benefit** |
| **Bank fixed deposit interest** | Taxed at the investor's **slab rate**, and **TDS applies** |
| **Dividends** | Taxed at the investor's **slab rate** in the investor's hands |
| **PPF / EPF (within limits) / Sukanya Samriddhi** | **EEE** — exempt at contribution, accrual and withdrawal |

**What the constraint means for construction:**

- Prefer **growth options over dividend/IDCW options** — dividends are taxed at slab rates as received, while growth defers the tax until you choose to sell.
- Prefer **holding through the long-term threshold** rather than trading around it.
- Use the **₹1.25 lakh annual LTCG exemption** deliberately — realise and immediately reinvest gains each year ("tax harvesting").
- Locate tax-inefficient assets inside **tax-exempt or tax-deferred wrappers** (EPF, PPF, NPS) and tax-efficient assets in the taxable account.
- Remember that **rebalancing has a tax cost**, which is why bands exist (see 15.13).

> 🧠 **Memory hook — "It is not what you earn; it is what you keep."** A 12% pre-tax return taxed at 30% leaves 8.4%. A 10% return taxed at 12.5% leaves 8.75%. **The lower gross return wins.**

### 15.6.4 Legal and regulatory constraint

Rules imposed from outside that the client cannot choose to ignore.

| Client type | Constraint |
|---|---|
| **Charitable and religious trusts** | Must invest only in modes permitted under **Section 11(5) of the Income-tax Act**; the trust deed may narrow this further |
| **Provident funds / EPFO** | Must follow the pattern of investment notified by the Government; EPFO's equity exposure is a limited share of incremental flows |
| **Insurance companies** | **IRDAI** prescribes minimum holdings in Government and other approved securities and minimum exposure to the housing and infrastructure sectors |
| **NPS subscribers** | **PFRDA** caps equity (asset class **E**) at **75%** under Active Choice, with the cap tapering for older subscribers; alternative assets (**A**) are capped at **5%** |
| **Mutual funds** | **SEBI** single-issuer, single-sector and single-group caps (see 15.7) |
| **Non-resident Indians** | **FEMA**: NRIs may not invest in certain instruments (for example, **PPF and Sukanya Samriddhi cannot be newly opened**); repatriation limits apply; agricultural land cannot be purchased |
| **Residents investing abroad** | **RBI's Liberalised Remittance Scheme** — up to **USD 2,50,000 per financial year** per resident individual |
| **Insiders and employees of listed companies** | **SEBI (Prohibition of Insider Trading) Regulations, 2015** — trading windows, pre-clearance, and a **minimum six-month holding** to avoid contra-trade |
| **Company directors, bank employees, government servants** | Employer codes of conduct restricting or requiring disclosure of trades |

> ⚠️ **Exam trap.** A legal/regulatory constraint applies **regardless of what the client wants and regardless of suitability.** If a trust deed forbids equity, no amount of risk capacity permits equity. Contrast this with a *unique preference*, which is the client's own choice and can be relaxed by the client.

### 15.6.5 Unique circumstances and preferences

Everything specific to this client that does not fit elsewhere:

- **Ethical, religious or ESG restrictions** (see 15.8)
- **Concentrated holdings** — employer ESOPs, a family business stake, ancestral property, an inherited holding the client refuses to sell for sentimental reasons
- **A dependant with special needs**, requiring a permanent income stream and a trust structure
- **A promise or commitment** — funding a sibling's education, supporting parents
- **Assets the client will not sell** — the ancestral house, gold held for a daughter's wedding
- **Health status** and life expectancy
- **A desire for direct control**, or a refusal to hold particular instruments (for example, "no derivatives", "no unlisted shares")

---

## 15.7 ⭐ Exposure Limits — to Securities, Sectors, Entities and Asset Classes

**An exposure limit is a written ceiling on how much of the portfolio may sit in any one thing.** Its purpose is to control **concentration risk** — the risk that one failure destroys the portfolio.

### Why limits are written into the IPS *in advance*

Concentration feels wonderful while it is working. Nobody sets a limit on their best-performing stock voluntarily; the limit must exist **before** the position becomes a favourite. That is exactly the same logic as the IPS itself.

### The four levels at which limits are set

| Level | Typical form in a client IPS |
|---|---|
| **Single security / issuer** | "No more than **10%** of the equity portfolio in any one stock" |
| **Sector / industry** | "No more than **25%** of the equity portfolio in any one sector" |
| **Entity / group / counterparty** | "No more than **20%** with any one AMC, group or issuer" |
| **Asset class** | "Equity **60% ± 10 percentage points**; gold not more than **15%**" |

### SEBI's own exposure limits for mutual funds — the regulatory template

These are the limits an IA should be able to recognise, because they show what a regulator considers prudent.

| Limit | Level |
|---|---|
| Equity of a **single company** | **10% of NAV** (index funds and sector/thematic funds exempt) |
| **Debt of a single issuer** | **10% of NAV**, extendable to **12%** with prior approval of the trustees and the AMC board |
| **Single sector** (debt) | **20% of NAV**, with limited additional headroom for housing finance |
| **Single group** (debt) | **20% of NAV**, extendable to **25%** with trustee approval |
| **Voting rights** | All schemes of a mutual fund together may not hold more than **10% of a company's paid-up capital carrying voting rights** |
| **Government securities, T-bills and TREPS** | **Exempt** from single-issuer limits — sovereign risk |

> 🧠 **Memory hook — "Ten for one, twenty for many."**
> **10%** is the recurring cap on any **single** name; **20%** is the recurring cap on any **single sector or group**.

### Worked example — an exposure limit doing its job

Mrs Rao's portfolio is **₹50,00,000**, with a **10% single-stock cap** and a **25% single-sector cap** written into her IPS.

- Her employer's stock, received as ESOPs, is worth **₹18,00,000** = **36%** of the portfolio. **Cap = 10% × ₹50,00,000 = ₹5,00,000.** She is **₹13,00,000 over the limit.**
- Worse, she also holds ₹4,00,000 in two banking funds. Since her employer is a bank, her **financial-sector exposure is ₹22,00,000 = 44%**, against a 25% cap of **₹12,50,000**.
- **Compounding the problem: her salary comes from the same company.** Her **human capital** and her **financial capital** are exposed to the same single event. If the employer fails, she loses her job and her savings in the same week.

**The adviser's plan:** unwind the ESOP position in **stages over three financial years** to spread the capital-gains tax across three ₹1.25 lakh LTCG exemptions, staying mindful of insider-trading trading windows, and redirect every new SIP rupee away from financials until the sector weight is inside the band.

> ⚠️ **Exam trap.** Exposure limits apply to the client's **whole balance sheet**, not just the advised portfolio. Employer stock, the family business and the salary itself are all exposure. This is a favourite scenario question.

---

## 15.8 ⭐ Unique Needs — Sustainable and Ethical Investing

### 15.8.1 Sustainable investing (ESG)

**Sustainable investing incorporates Environmental, Social and Governance factors alongside financial factors in investment decisions.**

| Pillar | What it covers |
|---|---|
| **E — Environmental** | Carbon emissions, energy and water use, waste, pollution, biodiversity, climate transition risk |
| **S — Social** | Labour practices, workplace safety, diversity, human rights, product safety, community relations, data privacy |
| **G — Governance** | Board independence and composition, executive pay, shareholder rights, audit quality, **related-party transactions**, promoter pledging, minority-shareholder treatment |

> 🧠 **In India, the "G" has historically mattered most.** Almost every large Indian investor loss of the last two decades — Satyam, IL&FS, Yes Bank, and others — was a **governance** failure, not an environmental or social one. Promoter share pledging, related-party transactions and aggressive accounting are governance red flags an IA should look for.

**The six main ESG approaches:**

| Approach | What it does |
|---|---|
| **Negative / exclusionary screening** | Remove whole industries or companies (tobacco, weapons, thermal coal) |
| **Positive / best-in-class screening** | Keep the highest-rated companies **within** each sector |
| **ESG integration** | Build ESG factors into ordinary financial analysis and valuation |
| **Thematic investing** | Target a theme — renewable energy, water, clean transport |
| **Impact investing** | Seek a **measurable** social or environmental outcome alongside a return |
| **Active ownership / stewardship** | Vote the shares and engage with management to change behaviour |

**The Indian regulatory framework:**

- **BRSR — Business Responsibility and Sustainability Report.** SEBI requires the **top 1,000 listed companies by market capitalisation** to file a BRSR with their annual report, giving investors standardised ESG disclosure. A subset, **BRSR Core**, carries assurance requirements that are being phased in from the largest companies downward.
- **Stewardship Code.** SEBI requires mutual funds and AIFs to adopt a stewardship code — a formal policy on voting and engagement with investee companies.
- **ESG mutual fund schemes.** SEBI permits a mutual fund to run **more than one ESG scheme**, provided each follows a **distinct ESG strategy** (exclusion, integration, best-in-class, impact, sustainable objectives, transition). Such a scheme must invest a **minimum of 80% of total assets** in securities that follow its stated ESG strategy, and must disclose its approach and its voting record.
- Globally, the **UN Principles for Responsible Investment (UN PRI)** — six voluntary principles — is the main signatory framework.

**Arguments for and against:**

| For | Against |
|---|---|
| ESG failures are **real financial risks** that show up in the share price | The **investable universe narrows**, which mathematically cannot improve the efficient frontier |
| Good governance is empirically linked to durable returns | **Sector bias** — excluding energy and metals creates unintended factor bets |
| Clients increasingly want their money to reflect their values | **Greenwashing** and inconsistent third-party ESG ratings |
| Regulation and carbon pricing make ESG risks financially material | Higher expense ratios and **tracking error** against a broad index |

### 15.8.2 Ethical investing

**Ethical investing selects or excludes investments on moral, religious or personal grounds — regardless of whether doing so improves the financial outcome.**

| | **Sustainable / ESG investing** | **Ethical / values-based investing** |
|---|---|---|
| **Primary driver** | ESG factors as **financially material risks and opportunities** | **Values** — moral, religious or personal conviction |
| **Would the investor accept a lower return?** | Usually argues no return sacrifice is required | **Yes, explicitly** — the value comes first |
| **Typical method** | Integration, best-in-class, engagement | **Exclusion** ("sin stocks") |
| **In the IPS** | Recorded under **unique needs and preferences** | Recorded under **unique needs and preferences** |

**Commonly excluded "sin" sectors:** tobacco, alcohol, gambling, weapons and defence, adult entertainment, and — for some investors — conventional interest-based lending.

**Shariah-compliant investing** is the best-known religious framework in India:

- Prohibits **riba** (interest), so conventional banks, NBFCs and insurers are excluded
- Prohibits businesses in alcohol, pork, gambling, tobacco and conventional finance
- Applies **financial screens** — limits on the company's debt, interest income and receivables relative to size
- Requires **purification** — donating the impermissible portion of income to charity
- Indian implementations include the **Nifty50 Shariah, Nifty500 Shariah and BSE 500 Shariah indices**, and a small number of Shariah-compliant equity funds

> ⚠️ **Exam trap — the adviser's duty.** An ethical restriction is the **client's choice**, and the adviser must **implement it and record it in the IPS**. But the adviser must also **disclose the consequence**: a narrower universe, likely sector bias, higher tracking error and possibly higher cost. Silently ignoring the restriction, or accepting it without explaining its cost, are both failures of the fiduciary duty.

---

## 15.9 Assessing the Needs and Requirements of the Investor

### What must be gathered

| Category | Information |
|---|---|
| **Personal** | Age, health, marital status, dependants, occupation, employment stability, residential status (resident / NRI) |
| **Goals** | What, how much (in today's rupees), when, and **priority** — essential, important or aspirational |
| **Income** | Salary, business income, rent, interest, expected increments, expected inheritance |
| **Expenses** | Regular household spending, EMIs, insurance premiums, lifestyle commitments |
| **Assets** | Bank balances, deposits, mutual funds, shares, EPF/PPF/NPS, gold, property, business interests |
| **Liabilities** | Home loan, car loan, personal loan, credit-card balances, loans against securities |
| **Protection** | Life cover, health cover, disability and critical-illness cover |
| **Tax** | Slab, regime chosen, existing deductions, capital-loss carry-forwards |
| **Attitude** | Risk-profiling questionnaire result, past behaviour in falling markets, investment knowledge |

### 🔑 The essential principle — goals must be inflated

A goal expressed in today's rupees is not the amount that will be needed.

**Example.** Ms Banerjee's daughter is 4. College will cost **₹15,00,000** in today's money and begins in **14 years**. Education inflation is **8%**.

**Future cost = 15,00,000 × (1.08)¹⁴ = 15,00,000 × 2.9372 = ₹44,05,800**

The goal is not ₹15 lakh. **It is roughly ₹44 lakh** — nearly three times as much. Every goal in an IPS must be stated at its **future, inflated value**, or the plan is guaranteed to fall short.

### The order of operations — protection before investment

An adviser must not build an investment portfolio on an unprotected balance sheet:

1. **Emergency fund** — 3 to 6 months' expenses in liquid form
2. **Health insurance** — for the whole family, adequate for the city they live in
3. **Term life insurance** — if anyone depends on the client's income
4. **Repay expensive debt** — a 40% credit-card rate cannot be beaten by any portfolio
5. **Then** invest for goals

> 🧠 **Memory hook — "Fix the roof before buying the furniture."** One uninsured hospitalisation can undo a decade of SIPs.

---

## 15.10 Analysing the Financial Position of the Investor

Two statements and a handful of ratios.

### The two statements

| Statement | Formula | What it tells you |
|---|---|---|
| **Net worth statement** | **Assets − Liabilities** | The client's financial position at a **point in time** (a stock) |
| **Cash-flow statement** | **Inflows − Outflows** | What is available to invest **over a period** (a flow) |

**The cash-flow statement matters more for a young client** (net worth is small, savings capacity is everything). **The net worth statement matters more for a retiree** (there is no more income; the corpus is everything).

### The ratios an IA computes

| Ratio | Formula | Healthy level |
|---|---|---|
| **Savings ratio** | Savings ÷ Gross income | The higher the better; **20%+** is a common goal |
| **Basic liquidity ratio** | Liquid assets ÷ Monthly expenses | **3 to 6** months |
| **Debt-to-income ratio** | Total EMIs ÷ Monthly income | Below about **40%**; housing EMI alone below about 30% |
| **Solvency ratio** | Net worth ÷ Total assets | The higher the better — it shows how much is truly owned |
| **Debt-to-asset ratio** | Total liabilities ÷ Total assets | The lower the better |

### Worked example

Mr Menon, 38. Monthly income **₹1,80,000**; monthly expenses **₹1,05,000**; EMIs **₹55,000** (included in expenses). Assets: liquid **₹4,00,000**; mutual funds **₹22,00,000**; EPF **₹14,00,000**; flat **₹85,00,000**. Liabilities: home loan **₹48,00,000**.

| Measure | Calculation | Result | Verdict |
|---|---|---|---|
| **Net worth** | (4 + 22 + 14 + 85) − 48 = 125 − 48 | **₹77,00,000** | Sound |
| **Monthly surplus** | 1,80,000 − 1,05,000 | **₹75,000** | Strong saving capacity |
| **Savings ratio** | 75,000 ÷ 1,80,000 | **41.7%** | Excellent |
| **Basic liquidity ratio** | 4,00,000 ÷ 1,05,000 | **3.8 months** | Adequate; push towards 6 |
| **Debt-to-income** | 55,000 ÷ 1,80,000 | **30.6%** | Comfortable |
| **Solvency ratio** | 77,00,000 ÷ 1,25,00,000 | **61.6%** | Healthy |

**Reading it:** Mr Menon has a **high ability to take risk** — long horizon, large surplus, manageable debt, adequate liquidity. Notice, though, that **the flat is ₹85 lakh of a ₹1.25 crore asset base — 68% in one illiquid, undiversified asset.** His financial portfolio should therefore be built to *offset* that concentration, not to duplicate it: he should be underweight real estate and REITs, and there is no case for a second property.

---

## 15.11 ⭐ Psychographic Analysis of the Investor

Two people with identical finances can need completely different portfolios, because they will *behave* differently. Psychographic models classify **behaviour**, not wealth.

### 15.11.1 The Barnewall two-way model

| Type | Who they are | Behaviour |
|---|---|---|
| **Passive investor** | Wealth acquired **passively** — inheritance, or a salaried professional career (doctors, lawyers, corporate executives) | **More risk-averse**; **security is the priority**; will accept lower returns for safety. *The larger group.* |
| **Active investor** | Wealth **earned by their own risk-taking** — entrepreneurs, business owners | **Higher risk tolerance**; want **control** and involvement; often over-concentrated in what they know |

> 🧠 **Memory hook.** It is not about how they invest — it is about **how they got the money**. Someone who built a factory is comfortable betting on a factory. Someone who inherited a portfolio is terrified of losing it.

### 15.11.2 ⭐⭐ The Bailard, Biehl and Kaiser (BB&K) five-way model

The BB&K model plots investors on **two axes**:

- **Level of confidence:** **confident** ←→ **anxious**
- **Method of action:** **careful** ←→ **impetuous**

| Type | Confidence | Method | Behaviour | How to advise |
|---|---|---|---|---|
| **Adventurer** | **Confident** | **Impetuous** | Willing to make big, concentrated bets; entrepreneurial; dislikes advice; volatile | **The hardest client.** Insist on written exposure limits |
| **Celebrity** | **Anxious** | **Impetuous** | Wants to be where the action is; follows fashions and tips; **has no opinions of their own** | **Most receptive to advice** — and most in need of it |
| **Individualist** | **Confident** | **Careful** | Does their own homework; independent; rational; long-term | **The easiest client to advise** |
| **Guardian** | **Anxious** | **Careful** | Preserves wealth; avoids risk; often older or newly retired | Emphasise capital protection and steady income |
| **Straight Arrow** | **Middle** | **Middle** | The average, balanced investor — sits at the centre of both axes | A standard balanced approach |

> 🧠 **Memory hook — "A CIGS."**
> **A**dventurer · **C**elebrity · **I**ndividualist · **G**uardian · **S**traight Arrow.
> And the two extremes: the **Individualist** is the **easiest** to advise; the **Adventurer** is the **hardest**. The **Celebrity** is the one who most *needs* an adviser, because they act boldly on other people's opinions.

> ⚠️ **Exam trap.** Do not confuse **Adventurer** with **Celebrity**. Both act impetuously — but the **Adventurer is confident** and acts on **their own** convictions, while the **Celebrity is anxious** and acts on **someone else's**.

---

## 15.12 ⭐ Life-Cycle Analysis of the Investor

Risk capacity is largely a function of **where the client is in life**, because that determines the **horizon** and the ratio of **human capital** (future earnings) to **financial capital** (accumulated savings).

### The four-phase model

| Phase | Typical age | Financial position | Risk capacity | Portfolio emphasis |
|---|---|---|---|---|
| **Accumulation** | **25–40** | Low net worth, often **high debt** (home loan), long horizon, **human capital >> financial capital** | **Highest** | **Growth — equity-heavy**; SIPs; term and health cover essential |
| **Consolidation** | **40–55** | Income comfortably exceeds expenses; net worth growing fast; peak earning years | **Moderate to high** | Balance **growth with preservation**; begin diversifying; maximise contributions |
| **Spending** | **Retirement onward** | Living **off** the portfolio; no new human capital | **Lower — but not zero** | **Income and preservation**, with enough equity to beat 25 years of inflation |
| **Gifting** | Overlaps spending | Assets exceed anything the client can spend | Depends on the **beneficiary's** horizon, not the client's | **Estate planning**, trusts, charitable giving, wealth transfer |

### The human-capital insight that explains the whole model

A 28-year-old has a small portfolio and **decades of future salary** ahead. That future salary behaves like a **bond** — a long stream of relatively predictable payments. Since the largest asset on his balance sheet is already bond-like, the *financial* portfolio should tilt heavily to **equity** to balance it.

A 68-year-old has **no human capital left**. Her financial portfolio is now her entire balance sheet, so it must contain its own bond component. **The allocation glides down not because equity became riskier, but because the bond-like asset outside the portfolio disappeared.**

> ⚠️ **The counter-example that is always tested.** Someone whose income is *itself* equity-like — a commission-only salesperson, a business owner, an employee paid largely in ESOPs — has **bond-like human capital replaced by equity-like human capital**, and should hold **less** equity than their age alone suggests.

### Rules of thumb — and why they are only that

- **Equity % = 100 − age.** A 35-year-old holds 65% equity.
- Longer lifespans have led some to use **110 − age** or **120 − age**.

> ⚠️ **Exam trap.** These are **rules of thumb, not rules.** They ignore goals, wealth, liabilities, income stability and willingness to take risk. A 30-year-old saving for a house deposit due in two years should hold **almost no equity**, whatever "100 − age" says. The **goal's horizon**, not the investor's age, drives the allocation for that goal.

### The alternative life-stage framing

| Stage | Dominant financial need |
|---|---|
| **Young unmarried** | Build the emergency fund; start SIPs; buy health cover; repay education loans |
| **Young married** | Term insurance the moment there is a dependant; joint goals; home purchase planning |
| **Married with young children** | Education corpus; larger term cover; home loan; still equity-heavy |
| **Married with older children** | Peak expenses and peak income; education goals approaching — begin de-risking those legs |
| **Pre-retirement (about 5 years out)** | Shift the retirement corpus decisively toward debt; clear all loans; plan health cover for retirement |
| **Retirement** | Income generation, capital preservation, inflation protection, estate planning |

---

## 15.13 ⭐ Forecasting Risk and Return of Asset Classes (Capital Market Expectations)

Chapter 14's optimiser needs three inputs for every asset class: **expected return**, **expected risk (standard deviation)** and **expected correlation**. Producing them is called forming **capital market expectations**.

### The four methods

| Method | How it works | Weakness |
|---|---|---|
| **Historical / statistical** | Take long-run averages of past returns, volatility and correlation | The past need not repeat; the answer depends heavily on the **period chosen**; structural change (India's inflation and rate regime today is not that of 1995) |
| **Building-block / risk-premium** | Start with the risk-free rate and **add a premium** for each risk borne | Requires judgement on each premium |
| **Discounted cash flow / fundamental** | Derive the return implied by today's valuations and expected cash flows | Sensitive to growth and terminal-value assumptions |
| **Survey and judgement** | Ask experienced practitioners and economists | Subjective; prone to herding and to recency |

### 🔑 The building-block method in practice

**For debt — the easy one.**
> **For a bond portfolio held to maturity, the current yield to maturity (YTM) is the single best estimate of the return.**

Expected return = **nominal risk-free rate + term premium + credit premium + liquidity premium**

*Example:* 91-day T-bill **6.5%** + term premium **0.5%** (for a 10-year G-Sec) + AAA credit spread **0.6%** = **7.6%** expected return on a AAA corporate bond portfolio.

**For equity — the Grinold–Kroner style decomposition.**

Expected return ≈ **dividend yield + expected inflation + real earnings growth + change in valuation (P/E)**

*Example, illustrative:*

| Component | Value |
|---|---|
| Dividend yield | **1.2%** |
| Expected inflation | **5.0%** |
| Real earnings growth | **6.5%** |
| Expected change in valuation (P/E already above average) | **−0.5%** |
| **Expected equity return** | **12.2%** |

**The blended portfolio expectation.** With 60% equity at 12.2% and 40% debt at 7.4%:
E(R_p) = 0.60 × 12.2 + 0.40 × 7.4 = 7.32 + 2.96 = **10.28%**

> 🧠 **Memory hook.** Equity return = **what you are paid now (dividend) + what the business grows (earnings) + what the market decides to pay for it (P/E)**. Only the first two are real; the third is sentiment, and over long periods it averages out to roughly nothing.

### ⚠️ The problems with forecasting — directly examinable

| Problem | Explanation |
|---|---|
| **Regime change / non-stationarity** | The economic environment shifts; India's structurally lower inflation and interest rates make 1990s data misleading |
| **Limited data** | Reliable Indian market history is short — the Nifty 50 was launched in **1996** |
| **Survivorship bias** | Failed companies and closed funds vanish from the data, flattering historical returns |
| **Data-mining / period selection** | Choosing a start date that supports the conclusion you wanted |
| **Ex-post vs ex-ante** | What actually happened is not what was expected — a decade of good luck looks like a high expected return |
| **Asynchronous data** | Prices of illiquid assets (real estate, unlisted holdings) are stale, which **understates their true volatility and correlation** |
| **Psychological bias** | Overconfidence, anchoring, and **recency** — extrapolating the last three years indefinitely |
| **Errors compound in the optimiser** | Chapter 14's lesson: mean-variance optimisation is an **"estimation-error maximiser"**, and **errors in expected returns do the most damage** |

**The practical response:** forecast at the **asset-class level rather than the security level**, use **long histories tempered by judgement**, impose **constraints** on the optimiser, and **be humble** — present ranges, not point estimates.

---

## 15.14 ⭐ Benchmarking the Client's Portfolio

**A benchmark is the standard against which the portfolio's performance is judged.** Without one, "12% this year" is meaningless — it could be brilliant or dreadful.

### 15.14.1 ⭐ The seven properties of a valid benchmark — SAMURAI

| Letter | Property | Meaning |
|---|---|---|
| **S** | **Specified in advance** | Chosen **before** the period begins — never selected afterwards to flatter the result |
| **A** | **Appropriate** | Consistent with the manager's style — a small-cap fund is not judged against the Nifty 50 |
| **M** | **Measurable** | Its return can be computed readily and frequently |
| **U** | **Unambiguous** | Constituents and their weights are clearly identifiable |
| **R** | **Reflective of current investment opinions** | The manager knows and has views on the securities in it |
| **A** | **Accountable** | The manager accepts it as the yardstick and is accountable to it |
| **I** | **Investable** | It could be held passively as an alternative to active management |

> 🧠 **Memory hook — "SAMURAI."** Seven letters, seven tests. If a proposed benchmark fails even one, it is not a valid benchmark.

### Indian benchmarks by asset class

| Asset class / style | Common benchmark |
|---|---|
| Large-cap equity | **Nifty 50 TRI**, **BSE Sensex TRI**, Nifty 100 TRI |
| Broad / flexi-cap equity | **Nifty 500 TRI**, BSE 500 TRI |
| Mid cap | **Nifty Midcap 150 TRI** |
| Small cap | **Nifty Smallcap 250 TRI** |
| Debt — short duration | **CRISIL Short Term Bond Fund Index** |
| Debt — medium/long | **CRISIL Composite Bond Fund Index** |
| Liquid | **CRISIL Liquid Fund Index** |
| Gilt | **Nifty All Duration G-Sec Index** |
| Hybrid (aggressive) | **CRISIL Hybrid 35+65 — Aggressive Index** |
| Gold | **Domestic price of physical gold** |

### ⭐ Two SEBI rules on benchmarks you must know

1. **Total Return Index (TRI).** Since **1 February 2018**, SEBI has required mutual funds to benchmark against the **Total Return variant** of an index, which includes **dividends reinvested**. A price index ignores dividends and therefore understates the index's true return — comparing a fund (which receives dividends) to a price index was systematically flattering.
2. **The two-tier benchmark structure.** SEBI requires mutual fund schemes to disclose performance against:
   - **Tier 1 — a broad market index** reflecting the scheme's **category**, uniform across the industry, so that all funds in a category are comparable; and
   - **Tier 2 — an optional index** reflecting the particular **strategy or style** the fund manager follows.

### Constructing a benchmark for a multi-asset client portfolio

A single index cannot benchmark a portfolio holding several asset classes. The answer is a **customised (blended) benchmark**, weighted by the **strategic asset allocation**.

**Worked example.** Mr Desai's IPS specifies **60% equity, 30% debt, 10% gold**. His blended benchmark is:
**60% Nifty 500 TRI + 30% CRISIL Composite Bond Fund Index + 10% domestic gold price.**

Over the year: Nifty 500 TRI **+18.0%**, bond index **+7.5%**, gold **+12.0%**. His portfolio returned **15.10%**.

**Benchmark return = (0.60 × 18.0) + (0.30 × 7.5) + (0.10 × 12.0)**
= 10.80 + 2.25 + 1.20 = **14.25%**

**Outperformance = 15.10 − 14.25 = +0.85 percentage points.**

> ⚠️ **Exam trap.** A client who compares a 60:30:10 portfolio to the **Nifty 50** in a strong equity year will always feel cheated, and in a crash will feel like a genius. **The benchmark must mirror the strategic asset allocation**, otherwise the comparison measures the *allocation decision the client already agreed to*, not the adviser's work.

### Other benchmarking approaches

| Approach | Use |
|---|---|
| **Peer-group / managers' universe** | Rank against comparable funds. Suffers from **survivorship bias** and is not investable — it fails the SAMURAI "I" test |
| **Absolute / goal-based** | "Inflation + 4%", or "8% a year". Simple and client-friendly, but **not investable** and can be unachievable in a bad market |
| **Liability-relative** | Benchmark to the cost of the liability being funded — the natural choice for a retirement or education goal |

---

## 15.15 ⭐⭐ The Asset Allocation Decision — Strategic versus Tactical

### 15.15.1 Strategic Asset Allocation (SAA)

**The long-term target mix of asset classes, derived from the client's objectives, constraints and long-run capital market expectations.** It is the **policy portfolio** — the portfolio you would hold if you had no view whatsoever about what markets will do next.

- Set for the **long term** (typically five years or more)
- Reviewed **infrequently** — annually, or when the **client's** circumstances change
- Expressed as **targets with permitted bands**: "Equity 60%, permitted range 50–70%"
- **This is the decision that explains ~90% of return variability** (section 15.1)

### 15.15.2 Tactical Asset Allocation (TAA)

**Deliberate, temporary deviations from the strategic weights, to exploit a perceived short-term mispricing.**

- Horizon of **months, not years**
- Must stay **within the bands set in the IPS**
- It is a form of **market timing** — and it must be **funded from the strategic weights, then reversed**

### ⭐ The comparison table — learn this

| | **Strategic Asset Allocation** | **Tactical Asset Allocation** |
|---|---|---|
| **Horizon** | **Long term** — 5 years and beyond | **Short term** — months to about a year |
| **Driven by** | The **client**: goals, risk profile, constraints | The **market**: valuation, momentum, macro views |
| **Inputs** | **Long-run** expected returns, risks, correlations | **Short-run** forecasts and relative value |
| **Frequency of change** | Rare — on life events or an annual review | Frequent — as views change |
| **Purpose** | Deliver the **required return at acceptable risk** | Add **incremental return (alpha)** |
| **Nature** | **Passive with respect to the market** | **Active** — a market-timing bet |
| **Risk if wrong** | The client **misses their goals** | **Underperformance, extra costs and taxes** |
| **Share of return variability** | **The overwhelming majority** | **Small** |
| **Constrained by** | The IPS itself | The **bands** in the IPS |

> 🧠 **Memory hook — "Strategic is about the CLIENT; Tactical is about the MARKET."**
> If the reason for a change is something that happened in the client's *life*, it is strategic. If the reason is something that happened in the *market*, it is tactical.

**Worked example.** Mr Desai's SAA is **60% equity (band 50–70%)**, 30% debt, 10% gold, on a corpus of **₹80,00,000**.

- His adviser judges Indian mid-caps to be expensively valued and moves equity from 60% to **52%** — from ₹48,00,000 to **₹41,60,000** — parking **₹6,40,000** in a short-duration debt fund.
- This is **TAA**: it is temporary, market-driven, **within the 50–70% band**, and it must be reversed once the view plays out or is proved wrong.
- If instead Mr Desai retires and his adviser reduces equity from 60% to 40% permanently, that is a **change of SAA**, requiring the **IPS to be rewritten**.

> ⚠️ **Exam trap.** Any move **outside the IPS band** is not tactical asset allocation — it is a **breach of the IPS**. TAA lives inside the bands by definition.

### 15.15.3 The other asset allocation approaches

| Approach | How it works | Best in | Worst in |
|---|---|---|---|
| **Buy and hold** | Set the weights once and never rebalance; the winner's weight drifts upward | **Strongly trending** markets | Risk rises silently over time |
| **Constant mix (constant weight)** | Rebalance back to fixed target weights — **sell winners, buy losers** | **Oscillating, mean-reverting** markets | Persistent trends |
| **Constant Proportion Portfolio Insurance (CPPI)** | Equity = **m × (Assets − Floor)** — **buy winners, sell losers** | **Strongly trending** markets | Whipsawing, choppy markets |
| **Dynamic asset allocation** | Rules-based shifting driven by a valuation signal (P/E, P/B, yield gap) — the engine inside a **Balanced Advantage Fund** | Valuation-driven cycles | Model failure; signal lag |
| **Integrated asset allocation** | Continuously considers **both** capital market conditions **and** the investor's changing circumstances | Comprehensive | Complex and costly |
| **Life-cycle / target-date** | An automatic **glide path** reducing equity as the target date nears | Retirement saving | Ignores individual circumstances |

**CPPI worked example.** Floor **₹80,00,000**, multiplier **m = 3**, current assets **₹1,00,00,000**.
- Cushion = 1,00,00,000 − 80,00,000 = **₹20,00,000**. Equity = 3 × 20,00,000 = **₹60,00,000**.
- Equity falls 20% to ₹48,00,000, so total assets = 48 + 40 = **₹88,00,000**. New cushion = **₹8,00,000**. New equity target = 3 × 8,00,000 = **₹24,00,000** — so **sell ₹24,00,000 of equity**.
- As assets approach the floor the cushion approaches zero and equity is reduced to nothing — that is the "insurance".

> 🧠 **The clean contrast to remember:** **Constant mix buys the falling asset. CPPI sells it.** Constant mix is contrarian; CPPI is momentum-following. Buy-and-hold sits between them and does nothing.

---

## 15.16 ⭐ Portfolio Construction Principles

Having fixed the asset allocation, the adviser must populate each class.

### 15.16.1 Selecting the equity portfolio

**Two ways in:**

| | **Top-down** | **Bottom-up** |
|---|---|---|
| Starting point | **Economy** → sector → stock | The **individual company** |
| Relies on | Macro forecasts, sector rotation | Company fundamentals, valuation |
| Typical user | Multi-asset and sector-rotation managers | Value and stock-picking managers |

**The size buckets — SEBI/AMFI definitions, memorise these:**

| Category | Definition by full market capitalisation |
|---|---|
| **Large cap** | **1st to 100th** company |
| **Mid cap** | **101st to 250th** company |
| **Small cap** | **251st company onwards** |

*AMFI publishes the list every six months, and it binds all mutual funds.*

**Style buckets:** **value**, **growth**, **blend**, **GARP** (growth at a reasonable price), **quality**, **momentum**, **dividend yield**.

**The core-satellite approach — the standard IA recommendation:**

| Sleeve | Typical share | What it holds | Purpose |
|---|---|---|---|
| **Core** | **70–80%** | Broad index funds / ETFs, large-cap and flexi-cap funds | Low cost, low tracking error, delivers the market return reliably |
| **Satellite** | **20–30%** | Mid- and small-cap, sectoral, thematic, international, active concentrated funds | Seeks alpha; small enough that a failure is survivable |

**Other equity principles:**

- **Adequate but not excessive diversification.** Most of the diversifiable risk is removed by about **20 to 30 well-chosen, genuinely different stocks**. Beyond that, extra names add cost and monitoring burden without materially cutting risk — and eventually produce "diworsification", a closet index fund at active fees.
- **Cap single-stock and single-sector exposure** (section 15.7).
- **Check overlap.** Three "different" large-cap funds may hold the same top 15 Nifty names — that is one fund with three expense ratios.
- **Mind liquidity and impact cost** in small caps: exiting a small-cap position in a falling market can cost several percent.
- **Prefer direct plans** — the expense-ratio saving compounds. An IA, being fee-only, has no reason to recommend otherwise.

### 15.16.2 Selecting the debt portfolio

**Every debt decision reduces to three variables:**

| Variable | Risk taken | How it is expressed |
|---|---|---|
| **Duration** | **Interest-rate risk** | Modified duration in years |
| **Credit quality** | **Default / credit risk** | AAA, AA, A, below investment grade |
| **Liquidity** | **Liquidity risk** | Ease of exit at a fair price |

> 🔑 **The rule an IA should apply:** for a *retail* client, **debt exists to reduce risk, not to chase return.** Take risk in the equity sleeve, where you are paid for it. Reaching for an extra 1.5% yield by buying low-rated credit converts the "safe" part of the portfolio into a hidden equity-like bet — as several Indian credit-risk funds demonstrated painfully in 2018–2020.

**The interest-rate arithmetic — memorise the relationship:**

> **Approximate % price change ≈ − Modified Duration × Change in yield (in %)**

*Example:* a debt portfolio of **₹20,00,000** with modified duration **6**. Yields rise **0.50%**.
Price change ≈ −6 × 0.50 = **−3.0%** → a loss of **₹60,000**.
Cut duration to **2** and the same rate move costs −2 × 0.50 = **−1.0%** → **₹20,000**. **The duration decision is three times more consequential than the rate move itself.**

**Passive and active debt strategies:**

| Strategy | Description |
|---|---|
| **Buy and hold** | Hold to maturity; the **YTM at purchase is the return**, if there is no default |
| **Laddering** | Spread maturities evenly across years — produces **regular natural liquidity** and averages out reinvestment risk |
| **Bullet** | Concentrate maturities at a **single point** — used to fund a known dated liability |
| **Barbell** | Hold **short and long** maturities with nothing in the middle — high convexity, needs active management |
| **Immunisation** | **Match the portfolio's duration to the investment horizon**, so that price risk and reinvestment risk offset each other |
| **Cash-flow matching (dedication)** | Match bond cash flows **directly** to the timing of liabilities |
| **Active duration management** | Lengthen duration when rates are expected to fall, shorten when they are expected to rise |
| **Credit / spread strategies** | Take credit risk when spreads are wide; move up in quality when they are tight |
| **Roll-down** | Buy a bond on a steep part of the yield curve and profit as it "rolls down" to a lower yield with the passage of time |

> 🧠 **Memory hook — "Rates down, prices up."** Bond prices and yields move in **opposite** directions, and **longer duration means a bigger swing**. When you expect rate cuts, go **long** duration; when you expect rate rises, go **short**.

**Matching the fund category to the horizon:**

| Horizon | Category |
|---|---|
| Days to weeks | **Overnight, liquid** |
| 3–6 months | **Ultra-short duration, money market** |
| 6 months – 1 year | **Low duration** |
| 1–3 years | **Short duration, corporate bond** |
| 3 years+ | **Medium/long duration, gilt, dynamic bond** |
| A fixed future date | **Target maturity fund**, or a **G-Sec held to maturity** |

### 15.16.3 Selecting the hybrid portfolio

A hybrid fund holds more than one asset class **inside a single scheme**, so the rebalancing happens internally.

| SEBI hybrid category | Equity exposure | Suited to |
|---|---|---|
| **Conservative hybrid** | **10–25%** equity, rest debt | Retirees needing a small growth kicker |
| **Balanced hybrid** | **40–60%** equity | Moderate investors *(a fund house may offer either balanced or aggressive hybrid, not both)* |
| **Aggressive hybrid** | **65–80%** equity, **20–35%** debt | First-time equity investors; automatic rebalancing |
| **Dynamic asset allocation / Balanced Advantage** | **0–100%**, model-driven | Investors who want valuation-based allocation done for them |
| **Multi-asset allocation** | At least **three** asset classes, **minimum 10% in each** | One-stop diversification including gold |
| **Arbitrage** | Minimum **65%** equity, fully hedged | Short-horizon money seeking equity taxation |
| **Equity savings** | Minimum **65%** equity (largely hedged) and minimum **10%** debt | Lower-volatility equity exposure |

**The two real advantages of a hybrid fund:**

1. **Rebalancing inside the scheme triggers no tax for the investor.** If the client rebalances between a separate equity fund and a debt fund, every switch is a redemption and a taxable event. Inside a hybrid fund, the manager rebalances and the investor's units are untouched.
2. **It removes behavioural risk.** The client never sees the equity sleeve fall 30% in isolation, and so is far less likely to sell at the bottom.

**The disadvantage:** the client loses control of the allocation, and the equity and debt sleeves may each be mediocre.

> ⚠️ **Exam trap on taxation.** A scheme is taxed as an **equity** scheme if it holds a **minimum of 65% in Indian equities**. This is exactly why aggressive hybrid, arbitrage and equity savings funds are all built around the **65%** line — the tax boundary drives the product design.

### 15.16.4 Other portfolios

| Asset | Vehicles in India | Role and cautions |
|---|---|---|
| **Gold** | **Gold ETFs**, gold savings funds, **Sovereign Gold Bonds** (8-year tenor, early exit from year 5), digital gold, jewellery | Inflation and currency hedge; **low to negative correlation with equity**; typically **5–10%**. Jewellery is a poor investment — making charges and purity loss |
| **Real estate** | Physical property, **REITs**, fractional ownership | Large ticket, **illiquid**, high transaction cost, no price transparency. **REITs** are SEBI-regulated, exchange-traded and must distribute the large majority of their net distributable cash flows to unitholders |
| **Infrastructure** | **InvITs** | Similar structure to REITs, for operating infrastructure assets |
| **International equity** | Feeder funds, international FoFs, direct investing under the **LRS** | Diversifies country and currency risk; the **LRS limit is USD 2,50,000 per financial year** per resident individual; SEBI applies industry-wide caps on mutual fund overseas investment |
| **Alternatives** | **AIFs** (Category I, II, III), PMS | High minimums (**₹1 crore** for AIFs, **₹50 lakh** for PMS), illiquid, complex — suitable only for large, sophisticated portfolios |
| **Structured products / derivatives** | Market-linked debentures, options | Generally unsuitable for retail clients; must be explicitly permitted in the IPS if used at all |

---

## 15.17 ⭐⭐ Rebalancing the Portfolio

### What rebalancing is

**Rebalancing is the act of restoring the portfolio to its strategic target weights after market movements have caused them to drift.**

It is **inherently contrarian**: it forces you to **sell what has gone up and buy what has gone down** — the opposite of what instinct demands, which is precisely why it must be written into the IPS in advance.

### Why drift is dangerous

Consider a **60:40** portfolio left alone through a long bull market. Equity compounds faster, so after five strong years the mix might be **78:22**. The client has not decided to take more risk — but they now have far more of it. **The next crash will hurt in a way the IPS never sanctioned.**

> 🧠 **Memory hook — "Rebalancing is a risk-control tool, not a return-enhancement tool."**
> If a question asks for the **primary** purpose of rebalancing, the answer is **keeping risk at the level the client agreed to**. Any return benefit is a by-product.

### 15.17.1 The three methods

| Method | Rule | Advantages | Disadvantages |
|---|---|---|---|
| **Calendar rebalancing** | Rebalance on fixed dates — monthly, quarterly, half-yearly, **annually** | **Simple**, predictable, easy to administer; annual timing can be aligned with tax planning | Ignores what happens **between** dates; may trade when the drift is trivial, and may fail to act during a crash |
| **Percentage-of-portfolio / threshold (tolerance band)** | Rebalance only when a class drifts **outside its band** — e.g. ±5 percentage points, or ±20% of the target weight | **Responsive to actual risk**; trades only when it matters | Requires **continuous monitoring**; can trigger frequent trades in a volatile market |
| **Combination (calendar-and-threshold)** | **Check** on a fixed calendar, but **act only if** the drift is outside the band | Captures most of the benefit at much of the lower cost; **the practical standard** | Slightly more complex to explain |

### 🔑 Worked example — rebalancing arithmetic

Mr Nair's IPS: **60% equity / 40% debt**, corpus **₹40,00,000**, tolerance band **±5 percentage points**.

**Start of year:** Equity **₹24,00,000**; Debt **₹16,00,000**.

**End of year:** equity returned **+30%**, debt **+7%**.

| | Value | Weight |
|---|---|---|
| Equity | 24,00,000 × 1.30 = **₹31,20,000** | 31,20,000 ÷ 48,32,000 = **64.57%** |
| Debt | 16,00,000 × 1.07 = **₹17,12,000** | **35.43%** |
| **Total** | **₹48,32,000** | 100% |

**Step 1 — has the band been breached?** Drift = 64.57 − 60.00 = **4.57 percentage points**, which is **inside** the ±5 point band. Under a **pure threshold** rule, **no action is taken**.

**Step 2 — if the rule were calendar (annual), what trade is required?**
- Target equity = 60% × 48,32,000 = **₹28,99,200**
- Equity to sell = 31,20,000 − 28,99,200 = **₹2,20,800**
- New debt = 17,12,000 + 2,20,800 = **₹19,32,800** = exactly **40%** ✓

**Step 3 — the cost.** Suppose the ₹2,20,800 of units sold had a cost of **₹1,60,000**, giving a long-term capital gain of **₹60,800**. This is **below the ₹1,25,000 annual LTCG exemption**, so the tax is **nil** — provided the client has not already used the exemption elsewhere. **This is why an adviser rebalances with the tax calendar in mind, not just the market.**

> ⚠️ **Exam trap.** Note the two rules gave **different answers** on the same facts. Read the question carefully: **threshold** rules ask "is the drift outside the band?"; **calendar** rules ask "is it the review date?".

### 15.17.2 ⭐ Benefits of rebalancing

| Benefit | Explanation |
|---|---|
| **Keeps risk at the intended level** | **The primary reason.** Without it, the risky asset's weight — and the portfolio's risk — creeps upward |
| **Imposes discipline** | It mechanically **sells high and buys low**, removing emotion from the decision |
| **Enforces the IPS** | It is how the strategic asset allocation is actually maintained, rather than merely written down |
| **May add a "rebalancing bonus"** | In **volatile, mean-reverting** markets, systematically trimming winners and topping up losers earns a small excess return over buy-and-hold |
| **Creates a natural review point** | The rebalancing date is a good moment to re-examine goals, fund quality and costs |
| **Removes the need to forecast** | The rule acts; the adviser does not have to predict a top or a bottom |

### 🔑 Proving the rebalancing bonus — and its limits

A ₹10,00,000 portfolio, **50% equity / 50% debt**. Debt returns **0%** throughout (to isolate the effect).

**Scenario A — an oscillating market.** Equity **+40%** in year 1, then **−28.57%** in year 2, ending exactly where it started.

| | **Buy and hold** | **Constant mix (rebalanced annually)** |
|---|---|---|
| Start | Equity 5.00 / Debt 5.00 | Equity 5.00 / Debt 5.00 |
| End of Yr 1 | Equity 7.00 / Debt 5.00 = **₹12.00 L** | Equity 7.00 / Debt 5.00 = ₹12.00 L → **rebalance to 6.00 / 6.00** |
| End of Yr 2 | Equity 7.00 × 0.7143 = 5.00 / Debt 5.00 = **₹10.00 L** | Equity 6.00 × 0.7143 = 4.29 / Debt 6.00 = **₹10.29 L** |

**Rebalancing wins by about ₹28,600** — it sold equity at the top and bought it back cheaper.

**Scenario B — a strongly trending market.** Equity **+30%** in year 1 and **+30%** again in year 2.

| | **Buy and hold** | **Constant mix** |
|---|---|---|
| End of Yr 1 | Equity 6.50 / Debt 5.00 = **₹11.50 L** | ₹11.50 L → **rebalance to 5.75 / 5.75** |
| End of Yr 2 | Equity 8.45 / Debt 5.00 = **₹13.45 L** | Equity 7.475 / Debt 5.75 = **₹13.225 L** |

**Buy and hold wins by about ₹22,500** — rebalancing kept selling an asset that never stopped rising.

> 🧠 **The honest conclusion.** **Rebalancing is not a money machine.** It helps in choppy markets and hurts in trending ones. Its dependable benefit is **risk control**, and that is how it should be sold to a client.

### 15.17.3 ⭐ Difficulties and costs of rebalancing

| Difficulty | Detail |
|---|---|
| **Transaction costs** | Brokerage, **STT**, stamp duty, exchange and regulatory charges, GST, **bid-ask spread and impact cost**, and mutual fund **exit loads** |
| **Taxes** | Every sale is a **taxable event**. Selling equity held under 12 months attracts **20% STCG**; long-term gains above **₹1.25 lakh** attract **12.5%**. Debt funds bought on or after 1 April 2023 are taxed at **slab rates** |
| **Behavioural resistance** | Clients hate selling their best performer and buying their worst. This is **regret aversion** meeting the **disposition effect**, and it is the hardest practical obstacle |
| **Underperformance in trending markets** | Demonstrated in Scenario B above — rebalancing systematically trims a persistent winner |
| **Illiquid and locked assets** | **PPF, EPF, NPS, ELSS (3-year lock-in), Sovereign Gold Bonds, physical real estate, unlisted shares** and endowment policies simply **cannot be rebalanced** on demand |
| **Indivisibility** | Property cannot be sold in 4.57% slices |
| **Choosing the band** | Too narrow ⇒ excessive trading and cost; too wide ⇒ risk drifts too far. Bands should be **wider for volatile and illiquid classes** |
| **Monitoring effort** | Threshold rebalancing requires continuous valuation of the whole portfolio |
| **Timing the trade** | Selling into a falling market can worsen the price obtained — impact cost is highest exactly when rebalancing is most needed |

### 🔑 How a good adviser reduces the cost of rebalancing

| Technique | Why it works |
|---|---|
| **Rebalance with new money** | Direct **fresh SIP instalments and lump sums into the underweight class** — this rebalances with **zero selling, zero tax and zero exit load** |
| **Rebalance with withdrawals** | For a retiree, **draw the income from the overweight class**, achieving the same effect |
| **Use dividends and coupons** | Redirect income to the underweight asset rather than reinvesting it in place |
| **Rebalance inside tax-sheltered accounts first** | Switching between asset classes **within NPS or EPF** triggers no tax event |
| **Use hybrid / multi-asset funds** | The manager rebalances internally with **no tax consequence for the investor** |
| **Harvest gains inside the ₹1.25 lakh exemption** | Realise long-term gains up to the exemption each year and reinvest — resetting the cost base at no tax cost |
| **Widen the bands for volatile and illiquid assets** | Fewer, larger trades cost less than many small ones |
| **Prefer switches within the same fund house** | Often cheaper and operationally simpler than exit-and-re-enter |

---

## ⚡ Quick Revision Sheet

| Concept | The one-line answer |
|---|---|
| The single most important investment decision | **Asset allocation** — not security selection or timing |
| Brinson, Hood & Beebower (1986) | Asset allocation explained **93.6%** of the **variation in quarterly returns** of 91 US pension plans |
| Brinson, Singer & Beebower (1991) | Confirmed at approximately **91.5%** |
| Ibbotson & Kaplan (2000) | **~90%** of variability over time, **~40%** across funds, **~100%** of the return level |
| What Brinson measured | **Variability of returns**, **not** the amount of return — the classic misreading |
| Range of correlation | **−1 to +1** |
| ρ = +1 | **No** diversification benefit |
| ρ = −1 | Risk can be reduced to **zero** |
| Equity vs gold correlation | **Low to negative** — gold is a **safe haven** |
| Correlation in a crisis | **Rises towards +1** — diversification fails when most needed |
| Two-security risk formula | **σ_p = √(w₁²σ₁² + w₂²σ₂² + 2w₁w₂σ₁σ₂ρ)** |
| First step in portfolio construction | **Understand the client** — never the market |
| IPS | The **written document** governing the client–adviser relationship and the portfolio |
| Greatest value of an IPS | **Discipline in a crisis** — it stops emotional decisions |
| RRTTLLU | **R**eturn, **R**isk (objectives) · **T**ime horizon, **T**axes, **L**iquidity, **L**egal, **U**nique (constraints) |
| Two investment objectives | **Return objective** and **risk objective** |
| Required vs desired return | **Required = must have** (a need); **desired = would like** (a want) |
| Required return calculation | Spending rate **+ inflation + costs** (additive), or **(1+s)(1+i)(1+c) − 1** exactly |
| Ability to take risk | **Objective** — wealth, horizon, income stability, liabilities |
| Willingness to take risk | **Subjective** — psychology and experience |
| When ability and willingness conflict | **The LOWER of the two governs**; the adviser may **educate but not override** |
| Five investment constraints | **Liquidity, time horizon, tax, legal & regulatory, unique circumstances** |
| Emergency fund | **3–6 months' expenses** (6–12 if income is irregular) |
| Liquidity means | Convertible to cash **quickly at a fair price** — not "safe" |
| Longer horizon ⇒ | **Higher** ability to take risk |
| Equity LTCG | **12.5%** above **₹1.25 lakh** a year, holding period **> 12 months** |
| Equity STCG | **20%**, holding period **≤ 12 months** |
| Debt funds bought on/after 1 Apr 2023 | Taxed at the **investor's slab rate** |
| Legal vs unique constraint | **Legal is imposed from outside**; **unique is the client's own choice** |
| LRS limit | **USD 2,50,000** per financial year per resident individual |
| NPS Active Choice equity cap | **75%**, tapering after age 50; alternatives (**A**) capped at **5%** |
| Purpose of exposure limits | Control **concentration risk** |
| SEBI MF single-company equity limit | **10% of NAV** (index and sector funds exempt) |
| SEBI MF single-issuer debt limit | **10% of NAV**, extendable to **12%** with board and trustee approval |
| SEBI MF single-sector debt limit | **20% of NAV** |
| SEBI MF voting-rights limit | **10%** of a company's paid-up capital across all schemes |
| Exposure limits apply to | The client's **whole balance sheet** — including ESOPs and the family business |
| ESG | **E**nvironmental, **S**ocial, **G**overnance |
| Which pillar matters most in India | **Governance** — most Indian investor losses were governance failures |
| BRSR | SEBI's sustainability report, required of the **top 1,000 listed companies by market cap** |
| SEBI ESG scheme rule | Minimum **80% of total assets** in securities following the stated ESG strategy |
| ESG vs ethical investing | ESG treats factors as **financially material**; ethical investing puts **values first** and accepts a possible return sacrifice |
| Sin stocks | Tobacco, alcohol, gambling, weapons, adult entertainment |
| Shariah investing | No **riba** (interest); excludes conventional banks and NBFCs; financial screens plus **purification** |
| Adviser's duty on ethical screens | **Implement it, record it in the IPS, and disclose the cost** (narrower universe, sector bias, tracking error) |
| Goals must be | **Inflated to their future value** before planning |
| Order of financial planning | **Emergency fund → health cover → term cover → repay costly debt → invest** |
| Net worth | **Assets − Liabilities** (a stock, at a point in time) |
| Cash flow | **Inflows − Outflows** (a flow, over a period) |
| Basic liquidity ratio | Liquid assets ÷ monthly expenses; target **3–6** |
| Debt-to-income ratio | EMIs ÷ income; below about **40%** |
| Barnewall model | **Passive** (inherited/salaried, risk-averse) vs **Active** (self-made entrepreneurs, risk-tolerant) |
| BB&K axes | **Confident ↔ anxious** and **careful ↔ impetuous** |
| BB&K five types | **Adventurer, Celebrity, Individualist, Guardian, Straight Arrow** |
| Adventurer | **Confident + impetuous** — big concentrated bets; **hardest to advise** |
| Celebrity | **Anxious + impetuous** — follows fashions; **most receptive to advice** |
| Individualist | **Confident + careful** — does own research; **easiest to advise** |
| Guardian | **Anxious + careful** — preserves capital; often older |
| Straight Arrow | The **average, balanced** investor at the centre |
| Four life-cycle phases | **Accumulation → Consolidation → Spending → Gifting** |
| Accumulation phase | **Highest** risk capacity — long horizon, human capital >> financial capital |
| Spending phase | Income and preservation, but **still needs equity** to beat inflation |
| Why equity falls with age | The **bond-like human capital outside the portfolio disappears** |
| Equity rule of thumb | **100 − age** (also 110 or 120 − age) — a rule of thumb, **never a rule** |
| Best estimate of a hold-to-maturity bond return | The **current YTM** |
| Equity return building blocks | **Dividend yield + inflation + real earnings growth ± change in P/E** |
| Biggest forecasting problems | **Regime change, short data history, survivorship bias, recency, ex-post ≠ ex-ante** |
| Stale prices on illiquid assets | **Understate** true volatility and correlation |
| SAMURAI | **S**pecified in advance, **A**ppropriate, **M**easurable, **U**nambiguous, **R**eflective of opinions, **A**ccountable, **I**nvestable |
| Benchmark basis for mutual funds | **Total Return Index (TRI)** — mandated by SEBI from **1 February 2018** |
| SEBI two-tier benchmark | **Tier 1** = broad category index; **Tier 2** = optional style/strategy index |
| Multi-asset client benchmark | A **blended benchmark weighted by the strategic asset allocation** |
| Why peer-group benchmarks fail SAMURAI | They are **not investable** and suffer **survivorship bias** |
| Strategic asset allocation | The **long-term policy mix** set by the **client's** goals and constraints |
| Tactical asset allocation | **Short-term deviations within the IPS bands** driven by **market** views |
| The clean SAA/TAA test | Life event ⇒ **strategic**; market event ⇒ **tactical** |
| Moving outside the band is | A **breach of the IPS**, not tactical allocation |
| Buy and hold | Weights **drift**; best in trending markets |
| Constant mix | Rebalance to fixed weights — **buys losers**; best in **oscillating** markets |
| CPPI | Equity = **m × (Assets − Floor)** — **sells losers**; best in **trending** markets |
| Dynamic asset allocation | Rules/valuation-driven — the engine in a **Balanced Advantage Fund** |
| Large / mid / small cap | **1–100 / 101–250 / 251 onwards** by full market capitalisation |
| Core-satellite | **Low-cost broad core (70–80%)** plus **alpha-seeking satellites (20–30%)** |
| Adequate equity diversification | Roughly **20–30 genuinely different stocks** |
| Three debt decisions | **Duration, credit quality, liquidity** |
| Bond price rule | **% price change ≈ − modified duration × change in yield** |
| Laddering | Maturities spread evenly — natural liquidity, averaged reinvestment risk |
| Barbell | **Short + long** only, nothing in the middle |
| Bullet | Maturities concentrated at **one date** |
| Immunisation | **Match duration to the horizon** so price and reinvestment risk offset |
| Aggressive hybrid | **65–80%** equity, **20–35%** debt |
| Conservative hybrid | **10–25%** equity |
| Multi-asset allocation fund | At least **three** asset classes, **minimum 10% each** |
| Equity taxation threshold for a scheme | Minimum **65%** in Indian equities |
| Key hybrid advantage | Internal rebalancing is **not a taxable event for the investor** |
| Typical gold allocation | **5–10%**; SGB tenor **8 years**, exit permitted from year **5** |
| AIF / PMS minimums | **₹1 crore** / **₹50 lakh** |
| Rebalancing | Restoring the portfolio to its **strategic target weights** |
| Primary purpose of rebalancing | **Risk control** — not higher returns |
| Rebalancing is inherently | **Contrarian** — sell winners, buy losers |
| Three rebalancing methods | **Calendar**, **percentage-of-portfolio (threshold/band)**, and a **combination** |
| Rebalancing bonus arises in | **Volatile, mean-reverting** markets |
| Rebalancing hurts in | **Strongly trending** markets |
| Main rebalancing difficulties | **Transaction costs, taxes, behavioural resistance, illiquid/locked assets, trending markets** |
| The cheapest way to rebalance | **Direct new contributions and withdrawals** to and from the underweight/overweight class |
| Assets that cannot be rebalanced | **PPF, EPF, NPS, ELSS in lock-in, SGBs, physical property, unlisted shares** |

> **Exam tip:** three question types account for most of the marks in this chapter. **First**, "which of these is a constraint / which is an objective" — run **RRTTLLU** and remember that only the two **R**s are objectives. **Second**, "strategic or tactical" — ask whether the trigger was a change in the **client's life** (strategic) or a change in the **market** (tactical). **Third**, "ability versus willingness" — the answer is almost always that **the lower of the two governs**, and that the adviser **educates rather than overrides**. Get those three reflexes right and the rest of the chapter is straightforward recall.
