# Chapter 16: Portfolio Performance Measurement and Evaluation — Flashcards

Cover the answer, recall it, then check. **Every formula here is a potential mark. Say the formula out loud, then say what goes in the DENOMINATOR and WHY.**

**Q1.** What are the two parameters that together define portfolio performance?
> **A:** **Return AND risk.** A return figure on its own is meaningless — 18% earned with 30 diversified large-caps is not the same performance as 18% earned with four leveraged micro-caps on borrowed money.

**Q2.** State the Holding Period Return formula, and apply it: 1,000 shares bought at ₹250, sold nine months later at ₹278, dividend ₹6 per share.
> **A:** **HPR = (Ending value − Beginning value + Income) ÷ Beginning value.** Here = (2,78,000 − 2,50,000 + 6,000) ÷ 2,50,000 = **13.6%** for nine months. Annualised = (1.136)^(12/9) − 1 = **18.53%**. Never omit the income term.

**Q3.** Define TWRR and MWRR.
> **A:** **TWRR** — break the period at every cash flow, compute each sub-period's return and **chain them geometrically**: (1+R₁)(1+R₂)… − 1. **MWRR** — the **IRR** of all the cash flows, so periods with more money invested dominate. A client's SIP **XIRR** is an MWRR; a factsheet CAGR is a TWRR.

**Q4.** ⭐ WHY does TWRR measure manager skill?
> **A:** Because it **neutralises the effect of client cash flows**. The manager decides what to buy, but the **client** decides when to add or withdraw money. Chaining percentage sub-period returns makes the rupee amount in each slice irrelevant, so TWRR grades only what the manager controls — which is why **SEBI mandates TWRR for PMS performance disclosure**.

**Q5.** A PMS starts at ₹10 lakh, grows to ₹12 lakh in H1, the client adds ₹10 lakh, and it ends the year at ₹19.8 lakh. Compute TWRR and describe MWRR.
> **A:** H1 = **+20%**; H2 = (19.8 − 22)/22 = **−10%**. **TWRR = (1.20 × 0.90) − 1 = +8%.** But ₹20 lakh went in and only ₹19.8 lakh came out, so the **MWRR is about −1.3%**. The manager delivered +8%; the client's own timing (adding ₹10 lakh just before the fall) destroyed the outcome.

**Q6.** When are TWRR and MWRR identical, and which is larger when?
> **A:** Identical when there are **no cash flows** during the period. **MWRR > TWRR** if the client added money **before a strong** period (good timing); **MWRR < TWRR** if money was added before a weak one.

**Q7.** State AMR and GMR, the relationship between them, and apply both to returns of +25%, −10%, +15%.
> **A:** **AMR = (R₁+…+Rₙ)/n = 10.00%.** **GMR = [(1+R₁)…(1+Rₙ)]^(1/n) − 1 = (1.29375)^(1/3) − 1 = 8.96%.** **AMR ≥ GMR always** — equal only when every return is identical — and the gap **widens with volatility**, roughly **GMR ≈ AMR − σ²/2**. Only the GMR reproduces the ending value: ₹10,00,000 × 1.0896³ = **₹12,93,750**.

**Q8.** Returns of +50% then −50%. What do AMR and GMR say, and which is true?
> **A:** AMR = **0%**, implying break-even. Reality: ₹1,00,000 → ₹1,50,000 → **₹75,000**. **GMR = √(1.50 × 0.50) − 1 = −13.40% p.a.** Percentage gains and losses are **not symmetric** — a 50% loss needs a 100% gain to recover.

**Q9.** When should you use AMR, and when GMR?
> **A:** **AMR** for estimating the **next single period's** expected return (it is the unbiased single-period estimate). **GMR (= CAGR)** for reporting **realised multi-period** performance and comparing track records. *"Arithmetic is what you hoped for; geometric is what you got."*

**Q10.** List the deductions that turn a gross return into a net return, and apply them: a ₹50 lakh PMS earns 15% gross, with a 2% fixed fee, a 20% performance fee above a 10% hurdle, and ₹25,000 of other costs.
> **A:** Deductions: management fee / **TER**, **performance fee**, brokerage, **STT** and stamp duty, custody and fund accounting, **18% GST** on fees, exit load. Here: gross gain ₹7,50,000; fixed fee ₹1,00,000; performance fee 20% × (7,50,000 − 5,00,000) = ₹50,000; other ₹25,000 → costs **₹1,75,000**. Net gain **₹5,75,000 = 11.50%** — costs ate **3.5 percentage points**.

**Q11.** Give the Indian tax treatment for equity and debt mutual funds, and explain why a fund cannot publish a post-tax return.
> **A:** Listed equity / equity MF: **STCG 20%** (held ≤ 12 months); **LTCG 12.5%** (held > 12 months) on gains above **₹1.25 lakh** per financial year. Debt funds bought on/after 1 Apr 2023: **slab rate**, whatever the holding period. Tax is **investor-specific** — it depends on the client's slab, holding period and use of the exemption — so published returns are always **pre-tax**.

**Q12.** State the CAGR formula, apply it to ₹5,00,000 growing to ₹11,00,000 in 7 years, and give its two weaknesses.
> **A:** **CAGR = (EV ÷ BV)^(1/n) − 1** = (2.20)^(1/7) − 1 = **11.92% p.a.** Weakness 1: it **hides the path completely** — it says nothing about volatility. Weakness 2: being **point-to-point** it is **start-date sensitive**; the professional fix is **rolling returns**.

**Q13.** How do you annualise a return, how do you annualise risk, and why do they differ?
> **A:** Return: **(1 + periodic return)^(periods per year) − 1** — compound, never multiply (4% quarterly → **16.99%**). Risk: **σ_annual = σ_periodic × √(periods per year)** (4% monthly σ → 4 × √12 = **13.86%**; 1% daily → **15.87%**). They differ because returns are assumed **independent**, so **variances add** over time — variance grows with **t**, so σ grows with **√t**.

**Q14.** What is SEBI's rule on displaying mutual fund returns for short periods?
> **A:** Periods of **less than one year must be shown in absolute terms**; **one year and above** must be shown as **CAGR**. Annualising a 6% quarterly gain into 26.2% is exactly what the rule prevents.

**Q15.** Define cash drag, give the adjustment formula, and apply it to a fund holding 10% cash at 4% with 90% in equity returning 15%.
> **A:** Cash drag is the return lost by holding **uninvested cash in a rising market**. **Adjusted return = (Rp − w_cash × R_cash) ÷ (1 − w_cash)**. Reported = (0.90 × 15) + (0.10 × 4) = **13.9%**; **cash drag = 1.1 percentage points**; adjusted = (13.9 − 0.4) ÷ 0.90 = **15.0%** — exactly the equity return, isolating the manager's selection.

**Q16.** Distinguish beta return from alpha return.
> **A:** **Beta return** is what you earn simply for **market exposure** — buyable for a few basis points via an index fund. **Alpha return** is what you earn **above** what that exposure justified — the only thing an active fee should be buying. *"Beta is rented; alpha is earned."*

**Q17.** ⭐ State Jensen's Alpha, compute it for Rp = 16%, Rf = 6.5%, β = 1.20, Rm = 13%, and name the classic mistake.
> **A:** **α = Rp − [Rf + β(Rm − Rf)]**. Required = 6.5 + (1.20 × 6.5) = **14.30%** → **α = 16 − 14.30 = +1.70%**. The fund beat the index by 3 points, but 1.3 of those were merely **bought with beta**. The classic mistake: treating alpha as **Rp − Rm**, which ignores the risk taken. The two coincide **only when β = 1**.

**Q18.** How is portfolio return computed, and what does the same rule NOT apply to?
> **A:** **Rp = Σ wᵢRᵢ** — a straight **weighted average**, using **market-value weights at the start** of the period, with Σwᵢ = 1. It does **not** apply to **risk**: portfolio σ is almost always **below** the weighted average of the component σs, because correlations are below +1.

**Q19.** Distinguish total risk from downside risk, give the downside deviation formula, and apply both to returns of 0%, 3%, 20%, 18%, 19% with MAR 6%.
> **A:** **σ** treats a +15% surprise and a −15% surprise as equally risky; **downside deviation = √[Σ(min(Rᵢ − MAR, 0))² ÷ n]** counts only **shortfalls**, but **every period still counts in n**. Mean = 12%. σ: (144+81+64+36+49)/5 = 74.8 → **σ = 8.65%**. Downside: shortfalls 6 and 3 → (36+9)/5 = 9 → **downside deviation = 3.00%**. Most of this fund's volatility was **upside**.

**Q20.** Name four downside-risk measures other than downside deviation.
> **A:** **Maximum drawdown** (largest peak-to-trough fall — ₹52 lakh peak to ₹36.40 lakh trough = **30%**), **Value at Risk** (loss not exceeded at a stated confidence over a stated horizon), **semi-variance**, and the **downside capture ratio** (fund's fall ÷ benchmark's fall; below 100% is good).

**Q21.** State the volatility probability bands and apply them to a fund with 12% expected return and 18% σ.
> **A:** Mean **±1σ ≈ 68%**, **±2σ ≈ 95%**, **±3σ ≈ 99.7%**. So 68% of years fall between **−6% and +30%**, and 95% between **−24% and +48%**. On ₹20 lakh, a −24% year is a **₹4,80,000** paper loss — the number the client must see *before* investing. Real markets have **fat tails**, so σ understates true extremes.

**Q22.** Define tracking error, distinguish it from tracking difference, and explain why it is NOT underperformance.
> **A:** **Tracking error = the standard deviation of the ACTIVE return** (portfolio − benchmark). **Tracking difference** is the simple **return gap**. SEBI requires both to be disclosed for index funds/ETFs and caps equity index fund/ETF tracking error at **2%** on rolling one-year data. A fund that beats its index by **exactly 4% every quarter** has a **tracking error of zero** — TE measures the **variability** of the gap, not its sign or size.

**Q23.** ⭐ Contrast systematic and unsystematic risk, and say which one is rewarded and why.
> **A:** **Systematic** = market-wide (RBI rates, inflation, GDP, oil, currency, policy), **non-diversifiable**, measured by **beta**, and **rewarded**. **Unsystematic** = company-specific (fraud, recall, strike, litigation), **diversifiable**, and **NOT rewarded** — the market will not pay a premium for a risk you could remove for free by diversifying. **σ²ᵢ = β²σ²ₘ + σ²ₑ.** Most specific risk disappears within roughly **20–30 well-spread** stocks.

**Q24.** What does R² tell you, and why does it matter for beta?
> **A:** The **proportion of the portfolio's variance explained by the market**. Above ~95% is essentially an index fund; **below about 70% means a lot of non-market risk**, which makes **beta, Jensen's alpha and the Treynor ratio unreliable** for that fund.

**Q25.** State the beta formula, compute β for σᵢ = 24%, σₘ = 16%, ρ = 0.80, and say how portfolio beta is found.
> **A:** **β = Cov(i,m) ÷ Var(m) = ρ × (σᵢ ÷ σₘ)** = 0.80 × (24 ÷ 16) = **1.20** — a 10% market rise implies a 12% rise. **Portfolio beta IS the simple weighted average** of component betas (0.40×1.40 + 0.35×0.90 + 0.25×0.60 = **1.025**) — unlike portfolio standard deviation, which is not.

**Q26.** Why is liquidity risk not captured by standard deviation?
> **A:** Illiquid assets are **valued infrequently**, which smooths reported returns and makes measured σ **artificially low** — "volatility smoothing". Never call a real-estate, unlisted or thin small-cap portfolio low-risk because its σ looks small. SEBI's responses include **stress testing** for mid/small-cap schemes and **side-pocketing** for credit-impaired securities.

**Q27.** What are the components of credit risk, and how is it compensated?
> **A:** **Default risk** (issuer fails to pay), **downgrade risk** (rating falls and the price drops immediately), and **credit spread risk** (spreads widen market-wide). Rated by **CRISIL, ICRA, CARE, India Ratings, Brickwork** on a scale from **AAA** down through **BBB** (lowest investment grade) to **D** (default). Compensation is the **credit spread** over a same-maturity G-Sec. Because losses are sudden and one-sided, **σ badly understates credit risk**.

**Q28.** State the Sharpe ratio, and apply it: Rf 6%; Fund A returns 16% with σ 20%; Fund B returns 12% with σ 10%.
> **A:** **Sharpe = (Rp − Rf) ÷ σp** — excess return per unit of **TOTAL risk**. A: 10/20 = **0.50**. B: 6/10 = **0.60**. **Fund B wins** despite the lower return. Proof: borrow at 6% to hold twice as much of B — σ becomes 20% (matching A) and the return becomes (2 × 12) − 6 = **18%**, beating A's 16% at identical risk.

**Q29.** State the Treynor ratio and say when it is the right measure.
> **A:** **Treynor = (Rp − Rf) ÷ βp** — excess return per unit of **SYSTEMATIC risk**. Use it when the fund is **one sleeve of an already diversified portfolio**, because that fund's specific risk has already been diversified away at the total-portfolio level, so charging for it would be wrong.

**Q30.** ⭐ Rf = 6%, σₘ = 16%. Fund X: 15% return, σ 25%, β 1.00. Fund Y: 13% return, σ 14%, β 0.80. Compute both ratios and interpret the disagreement.
> **A:** X: Sharpe 9/25 = **0.36**, Treynor 9/1.00 = **9.00**. Y: Sharpe 7/14 = **0.50**, Treynor 7/0.80 = **8.75**. They **disagree** → **the fund that ranks better on Treynor than on Sharpe is poorly diversified**. X's specific risk = √(25² − 16²) = **19.2%** and its **R² is only 41%**, versus Y's 5.7% and **84%**. Choose **Y** for a whole-portfolio client; **X** only as a small satellite. **If the two rankings agree, both portfolios are well diversified.**

**Q31.** State the Sortino ratio, explain why it exists, and apply it to the fund in Q19.
> **A:** **Sortino = (Rp − MAR) ÷ downside deviation.** It exists because investors do not experience an unexpectedly **large gain** as risk — penalising a manager for **upside** volatility is illogical. With MAR = Rf = 6%: **Sharpe = 6/8.65 = 0.69** but **Sortino = 6/3.00 = 2.00**. Always check the two funds use the **same MAR** before comparing.

**Q32.** State the Information Ratio and use it to separate two managers who both beat the benchmark by 3.0%, one with 3% tracking error and one with 12%.
> **A:** **IR = (Rp − Rb) ÷ Tracking Error = alpha ÷ tracking error** — it measures **skill AND consistency**. First manager **IR = 1.00**; second **IR = 0.25**. The same result achieved with **four times the active risk** is far more likely to be **luck** than repeatable skill. Rough bands: **0.5 good, 0.75 very good, 1.0 exceptional**. A **negative IR** means you paid an active fee for a worse-than-index result.

**Q33.** State M², compute it for a fund returning 21% with σ 25% (Rf 6%, market 14% with σ 15%), and verify it.
> **A:** **M² = Rf + (Sharpe × σₘ)** and **M² alpha = M² − Rm**. Sharpe = 15/25 = **0.60** → **M² = 6 + (0.60 × 15) = 15.0%**, so **M² alpha = +1.0 point**. Verify by risk-matching: hold **60%** in the fund and **40%** in T-bills → σ = 0.6 × 25 = **15%** (the market's risk) and return = (0.6 × 21) + (0.4 × 6) = **15.0%** ✓. M² **always ranks funds identically to Sharpe** — it adds interpretability, not information.

**Q34.** Give the seven characteristics of a good benchmark.
> **A:** **SAMURAI** — **S**pecified in advance, **A**ppropriate (right asset class, style and market cap), **M**easurable, **U**nambiguous, **R**eflective of current investment opinion, **A**ccountable (the manager owns it), **I**nvestable.

**Q35.** What is the difference between PRI and TRI, and what has SEBI mandated?
> **A:** A **Price Return Index ignores dividends**; a **Total Return Index reinvests them**. Benchmarking a fund against a PRI flatters it by roughly the dividend yield every year, so **SEBI has mandated TRI benchmarking for mutual funds**, along with a **two-tier structure** — a **Tier-1** benchmark for the scheme category and an optional **Tier-2** for the manager's style.

**Q36.** How do you build a customised benchmark, and what does 65% NIFTY 50 TRI at 15% plus 35% bond index at 7% produce?
> **A:** Blend the indices in the portfolio's **strategic** asset-allocation weights, specified **in advance in the IPS**, using **total-return** versions and rebalancing on the policy schedule. Here: (0.65 × 15) + (0.35 × 7) = 9.75 + 2.45 = **12.20%** — a far fairer test than comparing a balanced portfolio to the NIFTY's 15%.

**Q37.** Name six benchmarking errors.
> **A:** **Style/category mismatch** (a mid-cap fund against the NIFTY 50 measures the mid-cap premium, not skill); using **PRI instead of TRI**; choosing the benchmark **after the fact** ("benchmark shopping"); **cherry-picked start dates** (fix: rolling returns); **too short a period**; and **ignoring risk** or comparing a **gross** fund return to a **net** benchmark. Also: non-investable benchmarks, survivorship bias and style drift.

**Q38.** What is managers' universe analysis, and what are its main weaknesses?
> **A:** **Quartile ranking** a fund against the universe of **same-mandate** funds. Weaknesses: **survivorship bias** (failed funds leave the sample, lifting the average), the universe is **not investable**, it is **not risk-adjusted** (the top quartile in a bull market is often just the highest-beta quartile), shifting composition, loose category definitions, small samples and self-selection bias.

**Q39.** Can a fund be top-quartile among peers and still have failed the client?
> **A:** **Yes** — if the whole category underperformed its index, the best of a bad group still lost to a cheap index fund. Peer analysis and benchmark analysis are **complements, not substitutes**; always look at both.

**Q40.** State the performance attribution identity and the allocation and selection formulas.
> **A:** **Active return = Allocation + Selection + Interaction.** **Allocation = Σ (wₚ − w_b) × (R_b,sector − R_b,total)** — *"which buckets"*. **Selection = Σ w_b × (Rₚ,sector − R_b,sector)** — *"what's inside the bucket"*. **Interaction = Σ (wₚ − w_b) × (Rₚ,sector − R_b,sector)**.

**Q41.** Benchmark: 60% equity @12%, 40% debt @7%. Portfolio: 75% equity @14%, 25% debt @6.5%. Decompose the active return.
> **A:** Benchmark **10.00%**, portfolio **12.125%**, active **+2.125%**. **Allocation** = (0.15 × 2) + (−0.15 × −3) = **+0.75%**. **Selection** = (0.60 × 2) + (0.40 × −0.5) = **+1.00%**. **Interaction** = (0.15 × 2) + (−0.15 × −0.5) = **+0.375%**. Total **2.125%** ✓ — mostly **selection**, and the only negative contribution came from **debt security selection**.

**Q42.** Distinguish market timing from selectivity, and name the models that test timing.
> **A:** **Market timing** = varying **portfolio beta / market exposure** ahead of market moves. **Selectivity** = picking better securities within that exposure (= Jensen's alpha). Timing is tested by **Treynor–Mazuy** (adds a squared market-return term) and **Henriksson–Merton** (a dual-beta model). Evidence of successful timing is consistently **poor**.

**Q43.** ⭐ Define net selectivity, give the formula, and apply it: Rp 18%, σp 22%, β 1.10, Rf 6%, Rm 13%, σₘ 16%.
> **A:** **Net selectivity = Rp − [Rf + (σp ÷ σₘ) × (Rm − Rf)]** — Jensen's alpha **minus the return required for imperfect diversification**, because it charges the manager for **total** risk instead of just beta. CAPM required = 6 + 1.10 × 7 = **13.70%** → **alpha = +4.30%**. Total-risk required = 6 + (22/16) × 7 = **15.625%** → **net selectivity = 18 − 15.625 = +2.375%**. The **1.925%** difference was mere compensation for being **under-diversified**.

**Q44.** When does net selectivity equal Jensen's alpha, and what does a negative net selectivity alongside a positive alpha mean?
> **A:** They are equal when **σp/σₘ = β** — the portfolio is **perfectly diversified**. **Negative net selectivity with positive alpha** diagnoses a manager whose apparent outperformance came from **concentration, not skill**.

**Q45.** How do you combine a foreign-currency return with a local-market return, and what does a 12% USD return become in rupees if the rate moves from ₹83 to ₹87.15, or from ₹83 to ₹80.51?
> **A:** **Multiply, never add: Return in INR = (1 + R_local) × (1 + R_currency) − 1.** At ₹87.15: currency return = (87.15/83) − 1 = **+5.0%** → INR return = 1.12 × 1.05 − 1 = **17.60%** (not 17% — the extra 0.6% is the cross term). At ₹80.51: currency = **−3.0%** → 1.12 × 0.97 − 1 = **8.64%**. A **rise** in the INR/USD rate is **rupee depreciation**, which is a **gain** for the Indian investor.
