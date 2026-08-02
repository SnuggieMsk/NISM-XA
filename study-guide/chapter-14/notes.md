# Chapter 14: Introduction to Modern Portfolio Theory — Short Notes

> **Module 5 · Portfolio Construction, Performance Monitoring and Evaluation (20 marks).**
> This is the most **numerical** chapter in the syllabus. Almost every mark comes from four things: the **expected-return weighted average**, the **two-security risk formula**, the **role of correlation**, and the **efficient frontier**. Learn the formulas by *using* them, not by staring at them.

---

## 14.1 The Framework — What Markowitz Actually Discovered

**Harry Markowitz** published *"Portfolio Selection"* in the **Journal of Finance in 1952** and won the **Nobel Memorial Prize in Economic Sciences in 1990** (shared with Merton Miller and William Sharpe). He is called the **father of Modern Portfolio Theory (MPT)**.

Before 1952, investing advice was: *"find good securities."* Markowitz's insight was that **a security cannot be judged on its own** — only by what it does **to the portfolio**.

### 🔑 The one idea that matters

> **The expected return of a portfolio IS the weighted average of the securities' returns.**
> **The RISK of a portfolio is NOT the weighted average of the securities' risks — it is almost always LESS.**

That asymmetry is the entire theory. Return adds up in a straight line; risk does not — because when one holding falls, another may be rising, and the two partially cancel.

**The rupee illustration.** You hold ₹5 lakh in an equity fund and ₹5 lakh in a liquid fund.
- Expected return: if equity is expected to return **14%** and liquid **6%**, the portfolio expects **10%** — exactly halfway. Straight-line.
- Risk: if equity's standard deviation is **20%** and liquid's is **2%**, the portfolio's risk is **NOT** 11%. Because the two barely move together, it works out **below** 11%. That shortfall is the **free lunch of diversification**.

### MPT vs naive diversification

| | **Naive diversification** | **Markowitz (MPT) diversification** |
|---|---|---|
| Rule | "Own many securities" | "Own securities that **do not move together**" |
| Input used | Number of holdings | **Covariance / correlation** between holdings |
| 30 IT stocks? | Looks diversified | **Not diversified** — correlations near +1 |
| Measurement | None | Quantified — risk is computed, not guessed |

> 🧠 **Memory hook — "It's not how many, it's how different."**
> Thirty Nifty IT stocks are one bet wearing thirty costumes. One IT stock + one FMCG stock + one G-Sec is three bets.

---

## 14.2 ⭐ Assumptions of Modern Portfolio Theory

MPT is a *model*, and models rest on assumptions. These are directly examinable.

| # | Assumption | Plain meaning |
|---|---|---|
| 1 | Investors see each investment as a **probability distribution of expected returns** over a holding period | You do not "know" the return; you know the odds |
| 2 | Investors **maximise expected utility** for one period, and their utility curves show **diminishing marginal utility of wealth** | The tenth lakh gives you less pleasure than the first |
| 3 | Investors measure risk by the **variability (variance / standard deviation) of expected returns** | Risk = volatility, nothing else |
| 4 | Decisions are based **solely on expected return and risk** — utility is a function of **E(R) and σ only** | Two numbers per portfolio; nothing else enters |
| 5 | For a given **risk**, investors prefer **more return**; for a given **return**, investors prefer **less risk** | All investors are **risk-averse** |

Additional working assumptions usually stated alongside these:

- **Single holding period** — the model is static, not multi-period
- **Markets are efficient** and information is freely available
- **No taxes and no transaction costs**
- **Assets are perfectly divisible** (you can hold any fraction)
- **Investors are rational** and have **homogeneous expectations** about returns, variances and covariances

> ⚠️ **Exam trap.** MPT does **not** assume that all investors have the *same* risk tolerance. It assumes all are **risk-averse** — but *how* risk-averse differs, which is exactly why different investors pick **different points on the same efficient frontier**.

> ⚠️ **Second trap.** MPT assumes risk is fully captured by **variance**. It does **not** distinguish upside volatility from downside volatility — a criticism that later produced the Sortino ratio and downside-risk measures (Chapter 16).

---

## 14.3 ⭐ Risk Aversion — Three Investor Types

**Risk aversion** is the preference for **certainty over uncertainty when the expected value is the same**. A risk-averse investor demands **extra expected return** — a **risk premium** — before accepting extra risk.

### The classic fair-gamble test

Offer a client a choice:
- **Option A:** ₹10,00,000 in cash, guaranteed.
- **Option B:** a coin toss — **heads ₹20,00,000, tails ₹0**.

Both have an **expected value of ₹10,00,000** (0.5 × 20,00,000 + 0.5 × 0). The choice reveals everything:

| Investor type | Chooses | Behaviour | Real-world example |
|---|---|---|---|
| **Risk-averse** | **Option A** (the certain ₹10 lakh) | Rejects a fair gamble; needs a **risk premium** to accept risk | Most investors; prefers an FD to a penny stock at the same expected return |
| **Risk-neutral** | **Indifferent** | Judges **only by expected return**; risk simply does not enter the decision | A theoretical benchmark; a very large, well-diversified institution behaves close to this |
| **Risk-seeking (risk-loving)** | **Option B** (the coin toss) | Accepts a fair — even an **unfair** — gamble for the chance of a big payoff | The lottery ticket buyer; a punter in deep out-of-the-money options |

### How each type looks on paper

| | **Risk-averse** | **Risk-neutral** | **Risk-seeking** |
|---|---|---|---|
| Utility of wealth curve | **Concave** (diminishing marginal utility) | **Straight line** | **Convex** (increasing marginal utility) |
| Indifference curves in E(R)–σ space | **Upward sloping**, convex | **Horizontal** | **Downward sloping** |
| Requires a risk premium? | **Yes** | No — accepts the risk-free rate | **Pays** a premium for risk |
| Certainty equivalent vs expected value | **Below** expected value | **Equal** to expected value | **Above** expected value |

> 🧠 **Memory hook — "AVERSE Asks, NEUTRAL Nods, SEEKER Pays."**
> The averse investor **asks for more return**; the neutral investor **nods at the expected value**; the seeker will **pay** (accept a lower expected return) for a shot at a big win.

**Why MPT assumes risk aversion.** If investors were risk-neutral, nobody would care about σ, the efficient frontier would collapse to a single point (the highest-return asset), and diversification would be pointless. **Risk aversion is what makes portfolio construction a problem worth solving.**

**The evidence for it in India:** equities have historically returned more than G-Secs over long periods. That gap — the **equity risk premium** — exists precisely *because* investors are risk-averse and must be paid to hold volatile assets. If the 10-year G-Sec yields **6.5%** and an investor requires **13%** from equity, the **equity risk premium** demanded is **6.5 percentage points**.

> ⚠️ Risk aversion does **not** mean "avoids all risk". A risk-averse investor happily buys equity — but only at a price that offers **compensation** for the risk. Avoiding risk entirely is a *separate* behaviour, and it carries its own (inflation) risk.

---

## 14.4 The Building Blocks — Return and Risk of ONE Security

### (a) Expected return of a security

When you have **probabilities of scenarios**:

> ### **E(R) = Σ pᵢ × Rᵢ**
> *(probability of each state × the return in that state, summed)*

**Why:** it is the average outcome you would get if the scenario "lottery" were run thousands of times. It is the centre of the distribution.

**Worked example — Infosys-like stock, one year ahead:**

| State of economy | Probability (pᵢ) | Return (Rᵢ) | pᵢ × Rᵢ |
|---|---|---|---|
| Boom | 0.25 | +30% | 7.50 |
| Normal | 0.50 | +12% | 6.00 |
| Recession | 0.25 | −8% | −2.00 |
| | **1.00** | | **E(R) = 11.50%** |

**On ₹4,00,000 invested, the expected gain is 11.5% × ₹4,00,000 = ₹46,000.**

When you have **past returns instead of probabilities**, use the simple average:

> ### **R̄ = (R₁ + R₂ + … + Rₙ) / n**

**Worked example.** Five years of returns: **10%, −4%, 16%, 22%, 6%**. Sum = 50%. **R̄ = 50 / 5 = 10%.**

### (b) Variance and standard deviation of a security

> ### **σ² = Σ pᵢ × [Rᵢ − E(R)]²**   and   **σ = √σ²**

**Why square the deviations?** Because plain deviations sum to **zero** — the pluses cancel the minuses. Squaring makes every deviation positive *and* penalises large misses much more than small ones. Squaring, however, leaves the answer in "percent-squared", which means nothing to a human — so we take the **square root** to get the **standard deviation**, back in **percentage points**.

**Worked example — same stock as above, E(R) = 11.5%:**

| State | pᵢ | Rᵢ | Rᵢ − E(R) | [Rᵢ − E(R)]² | pᵢ × [Rᵢ − E(R)]² |
|---|---|---|---|---|---|
| Boom | 0.25 | 30% | +18.5 | 342.25 | 85.5625 |
| Normal | 0.50 | 12% | +0.5 | 0.25 | 0.1250 |
| Recession | 0.25 | −8% | −19.5 | 380.25 | 95.0625 |
| | | | | **σ² =** | **180.75 (%²)** |

**σ = √180.75 = 13.44%.**

**Reading it in rupees.** With E(R) = 11.5% and σ = 13.44%, on a ₹4,00,000 holding the "normal" one-year band (roughly ±1σ, about two-thirds of outcomes if returns were normally distributed) is **−1.94% to +24.94%**, i.e. roughly **₹3,92,240 to ₹4,99,760**.

**From historical data**, the same idea with two possible divisors:

| Basis | Formula | When used |
|---|---|---|
| **Population** | σ² = Σ(Rᵢ − R̄)² / **n** | The data is the whole universe of outcomes |
| **Sample** | s² = Σ(Rᵢ − R̄)² / **(n − 1)** | The data is a *sample* drawn from a larger history (the usual case in finance) |

**Worked example.** Returns **10%, −4%, 16%, 22%, 6%**, mean **10%**.
Deviations: 0, −14, +6, +12, −4. Squares: 0, 196, 36, 144, 16. **Sum = 392.**
- **Population:** 392 / 5 = 78.4 → **σ = 8.85%**
- **Sample:** 392 / 4 = 98 → **s = 9.90%**

> ⚠️ **Exam trap.** If a question gives past returns and does not say which basis, look at the options — one will match ÷n and one will match ÷(n−1). NISM questions most often state the basis; when they do not, ÷(n−1) is the statistically correct treatment for a *sample* of history.

---

## 14.5 ⭐ Covariance and Correlation — The Heart of the Chapter

Two securities can each be volatile, yet a portfolio of the two can be calm — **if they move differently**. Covariance and correlation measure exactly that.

### Covariance

> ### **Cov(A,B) = Σ pᵢ × [R_Aᵢ − E(R_A)] × [R_Bᵢ − E(R_B)]**

**Read the formula as a story:** in each scenario, ask *"was A above its average? was B above its average?"*
- Both above, or both below → the product is **positive**
- One above while the other is below → the product is **negative**

Add those up and you learn whether the pair **tends to move together (+)** or **in opposite directions (−)**.

**The problem with covariance:** its size is meaningless. A covariance of **+150** tells you the direction but nothing about the strength, because it is measured in the units of both securities multiplied together.

### Correlation — covariance made readable

> ### **ρ_AB = Cov(A,B) / (σ_A × σ_B)**   and therefore   **Cov(A,B) = ρ_AB × σ_A × σ_B**

Dividing by both standard deviations strips out the scale and leaves a pure number between **−1 and +1**.

| Correlation ρ | Name | What it means | Diversification benefit |
|---|---|---|---|
| **+1.0** | Perfect positive | They move in lockstep, same direction | **ZERO** — none at all |
| **+0.5** | Moderate positive | Usually move together, not always | Some |
| **0** | Uncorrelated | Independent — no relationship | Substantial |
| **−0.5** | Moderate negative | Usually move in opposite directions | Large |
| **−1.0** | Perfect negative | Exact mirror images | **MAXIMUM** — risk can be driven to **zero** |

**Worked example — computing both.** Three **equally likely** scenarios (p = 1/3 each):

| Scenario | Stock A | Stock B | A − Ā | B − B̄ | Product |
|---|---|---|---|---|---|
| 1 | 18% | 4% | +8 | −4 | −32 |
| 2 | 10% | 8% | 0 | 0 | 0 |
| 3 | 2% | 12% | −8 | +4 | −32 |
| **Mean** | **10%** | **8%** | | | |

**Cov(A,B) = (1/3)(−32) + (1/3)(0) + (1/3)(−32) = −64/3 = −21.33**
σ_A = √[(64 + 0 + 64)/3] = √42.67 = **6.53%**
σ_B = √[(16 + 0 + 16)/3] = √10.67 = **3.27%**
**ρ = −21.33 / (6.53 × 3.27) = −21.33 / 21.33 = −1.00** → **perfect negative correlation.**

> 🧠 **Memory hook — "Covariance has a direction, correlation has a dial."**
> Covariance only tells you the **sign**. Correlation puts that sign on a fixed **−1 to +1 dial** so any two pairs can be compared.

> ⚠️ **Correlation is NOT causation, and it is NOT constant.** Indian equity–debt correlation is usually low, but in a global risk-off event both can fall together as foreign investors sell everything. **Correlations tend to rise towards +1 in a crisis — exactly when you needed them low.** This is the single most important practical limitation of MPT.

---

## 14.6 ⭐⭐ Portfolio Return and Portfolio Risk

### (a) Expected return of a portfolio — a simple weighted average

> ### **E(R_p) = w₁E(R₁) + w₂E(R₂) + … + wₙE(Rₙ)**   where **Σwᵢ = 1**

**Worked example.** Ms Iyer has **₹20,00,000**: **₹12,00,000** in an equity fund expected to return **18%**, and **₹8,00,000** in a short-duration debt fund expected to return **7%**.
- w_equity = 12/20 = **0.60**; w_debt = 8/20 = **0.40**
- **E(R_p) = 0.60 × 18 + 0.40 × 7 = 10.8 + 2.8 = 13.6%**
- Expected gain in rupees = 13.6% × ₹20,00,000 = **₹2,72,000**

Three assets work identically. **₹5L equity @ 15% + ₹3L debt @ 8% + ₹2L gold @ 10%** on a ₹10L portfolio:
**E(R_p) = 0.5(15) + 0.3(8) + 0.2(10) = 7.5 + 2.4 + 2.0 = 11.9%.**

> ⚠️ **Exam trap.** Return is *always* a straight weighted average — **correlation has NO effect on portfolio return.** Candidates who "adjust" the return for correlation lose the mark. Correlation affects **risk only**.

### (b) ⭐ Risk of a TWO-security portfolio

> ### **σ_p = √( w₁²σ₁² + w₂²σ₂² + 2·w₁·w₂·σ₁·σ₂·ρ₁₂ )**
>
> Equivalently, since Cov₁₂ = ρ₁₂σ₁σ₂:
> ### **σ_p = √( w₁²σ₁² + w₂²σ₂² + 2·w₁·w₂·Cov₁₂ )**

**Decode the three terms:**

| Term | What it is | Can it be negative? |
|---|---|---|
| **w₁²σ₁²** | Security 1's own risk contribution | Never |
| **w₂²σ₂²** | Security 2's own risk contribution | Never |
| **2w₁w₂σ₁σ₂ρ** | The **interaction** term | **YES — whenever ρ < 0** |

**Only the third term contains ρ, and it is the only term that can shrink the total.** That is the whole mechanism of diversification in one sentence.

### 🔬 The master worked example (memorise this one)

Mr Rao invests **₹6,00,000 in an equity fund** and **₹4,00,000 in a debt fund** (total ₹10,00,000):

| | Equity fund | Debt fund |
|---|---|---|
| Weight | **0.60** | **0.40** |
| Expected return | 15% | 8% |
| Standard deviation σ | **20%** | **5%** |

**Expected return:** E(R_p) = 0.6(15) + 0.4(8) = 9 + 3.2 = **12.2%** — *and this stays 12.2% no matter what ρ is.*

**Fixed parts of the risk calculation:**
- w₁²σ₁² = 0.36 × 400 = **144**
- w₂²σ₂² = 0.16 × 25 = **4**
- 2w₁w₂σ₁σ₂ = 2 × 0.6 × 0.4 × 20 × 5 = 0.48 × 100 = **48** → the interaction term is **48ρ**

So **σ_p² = 148 + 48ρ**. Now turn the correlation dial:

| ρ | σ_p² = 148 + 48ρ | **σ_p** | Versus the 14% weighted average |
|---|---|---|---|
| **+1.0** | 196 | **14.00%** | **No benefit** — exactly the weighted average |
| +0.5 | 172 | 13.11% | −0.89 pp |
| **+0.3** | 162.4 | **12.74%** | −1.26 pp |
| **0** | 148 | **12.17%** | −1.83 pp |
| −0.5 | 124 | 11.14% | −2.86 pp |
| **−1.0** | 100 | **10.00%** | **−4.00 pp — the maximum** |

**Weighted average of the standard deviations** = 0.6(20) + 0.4(5) = **14.00%**.

### 🔑 Why correlation below +1 reduces risk — the proof in two lines

At **ρ = +1** the formula collapses:
σ_p² = w₁²σ₁² + w₂²σ₂² + 2w₁w₂σ₁σ₂ = **(w₁σ₁ + w₂σ₂)²**, so **σ_p = w₁σ₁ + w₂σ₂ = the weighted average.**

Since ρ appears only in the third term and that term rises and falls with ρ, **any ρ below +1 makes σ_p² smaller — so σ_p is strictly LESS than the weighted average.**

> ### **σ_p ≤ w₁σ₁ + w₂σ₂, with equality ONLY when ρ = +1.**

> 🧠 **Memory hook — "Return is a straight line, risk is a curve that bends left."**
> Plot the two-asset portfolios: at ρ = +1 you get a **straight line** joining the two assets. As ρ falls, the line **bows leftward** (less risk for the same return). At ρ = −1 it bends all the way to the **vertical axis — zero risk**.

### The zero-risk case (ρ = −1)

When **ρ = −1**, risk can be eliminated completely with the right weights:

> ### **w₁ = σ₂ / (σ₁ + σ₂)** and **w₂ = σ₁ / (σ₁ + σ₂)**

**Check it on Mr Rao's funds** (σ₁ = 20, σ₂ = 5): w₁ = 5/25 = **0.20**, w₂ = 20/25 = **0.80**.
σ_p² = 0.04(400) + 0.64(25) + 2(0.2)(0.8)(20)(5)(−1) = 16 + 16 − 32 = **0**. **σ_p = 0%.** Riskless.

> ⚠️ **In the real world ρ = −1 never occurs between two risky assets.** It is a teaching limit, not a strategy. Real Indian pairs sit roughly between +0.2 and +0.9. That is still enough to matter enormously.

### (c) ⭐ Risk of a THREE-security portfolio

Every **pair** now contributes an interaction term:

> ### **σ_p² = w₁²σ₁² + w₂²σ₂² + w₃²σ₃² + 2w₁w₂σ₁σ₂ρ₁₂ + 2w₁w₃σ₁σ₃ρ₁₃ + 2w₂w₃σ₂σ₃ρ₂₃**

**Three variance terms + three covariance terms = six terms.**

**Worked example.** A ₹10 lakh portfolio:

| Asset | Weight | σ | Correlations |
|---|---|---|---|
| Equity (A) | 0.40 | 20% | ρ_AB = 0.5 |
| Corporate bond (B) | 0.35 | 12% | ρ_AC = 0.2 |
| Gold ETF (C) | 0.25 | 8% | ρ_BC = 0.4 |

| Term | Arithmetic | Value |
|---|---|---|
| w_A²σ_A² | 0.16 × 400 | 64.00 |
| w_B²σ_B² | 0.1225 × 144 | 17.64 |
| w_C²σ_C² | 0.0625 × 64 | 4.00 |
| 2w_Aw_Bσ_Aσ_Bρ_AB | 2(0.40)(0.35)(20)(12)(0.5) | 33.60 |
| 2w_Aw_Cσ_Aσ_Cρ_AC | 2(0.40)(0.25)(20)(8)(0.2) | 6.40 |
| 2w_Bw_Cσ_Bσ_Cρ_BC | 2(0.35)(0.25)(12)(8)(0.4) | 6.72 |
| | **σ_p² =** | **132.36** |

**σ_p = √132.36 = 11.50%**, against a weighted average of 0.4(20) + 0.35(12) + 0.25(8) = **14.20%**. Diversification saved **2.70 percentage points**.

### How the arithmetic explodes with n

| Securities (n) | Variance terms | Covariance pairs = n(n−1)/2 | Total terms | Total estimates needed = n(n+3)/2 |
|---|---|---|---|---|
| 2 | 2 | 1 | 3 | 5 |
| 3 | 3 | 3 | 6 | 9 |
| 10 | 10 | **45** | 55 | **65** |
| 50 | 50 | **1,225** | 1,275 | **1,325** |
| 100 | 100 | **4,950** | 5,050 | **5,150** |

*(Total estimates = n expected returns + n variances + n(n−1)/2 covariances.)*

> 🧠 **The lesson buried in that table:** with 50 securities there are **1,225 covariance terms but only 50 variance terms**. **Portfolio risk is driven overwhelmingly by how securities interact, not by their individual volatilities.** That is why an adviser worries about *correlation* far more than about any single stock's beta.

---

## 14.7 The Two-Security Risk/Return Graph

Plot **standard deviation on the X-axis** and **expected return on the Y-axis**. Every possible mix of two securities is one point; joining them traces a curve.

**Worked frontier.** Asset X: E(R) = **16%**, σ = **24%**. Asset Y: E(R) = **10%**, σ = **14%**. **ρ = 0.2** (so Cov = 0.2 × 24 × 14 = **67.2**).

| Weight in X | E(R_p) | σ_p | Efficient? |
|---|---|---|---|
| 0% (all Y) | 10.00% | 14.00% | **NO — dominated** |
| **20%** | **11.20%** | **13.04%** | **Minimum Variance Portfolio** |
| 40% | 12.40% | 13.96% | Yes |
| 60% | 13.60% | 16.46% | Yes |
| 80% | 14.80% | 19.95% | Yes |
| 100% (all X) | 16.00% | 24.00% | Yes (the top end) |

**Read the table carefully — this is the exam's favourite trick.** The **20% X / 80% Y** mix has **higher return (11.20% vs 10.00%) AND lower risk (13.04% vs 14.00%)** than holding Y alone. **Holding 100% of the safer asset is therefore an INEFFICIENT choice.** Even the 40% mix (12.40% return, 13.96% risk) beats it on both counts.

### The shape of the curve, by correlation

| ρ | Shape of the two-asset curve |
|---|---|
| **+1** | A **straight line** joining the two assets — no bend, no benefit |
| **Between −1 and +1** | A **curve bowing to the left** — the lower ρ, the deeper the bow |
| **−1** | **Two straight lines** meeting the vertical axis at **σ = 0** |

**The Minimum Variance Portfolio (MVP)** is the **leftmost point** of the curve — the mix with the lowest possible risk. For two assets:

> ### **w₁* = (σ₂² − Cov₁₂) / (σ₁² + σ₂² − 2·Cov₁₂)**

**Check it on X and Y:** w_X* = (196 − 67.2) / (576 + 196 − 134.4) = 128.8 / 637.6 = **0.202 ≈ 20%** ✓ — matching the table.

> ⚠️ One of MPT's most counter-intuitive results: **adding a small slice of a risky asset to a safe portfolio can LOWER total risk.** A 100%-debt investor who adds 5–10% equity may end up with *less* volatility and *more* return. Advisers use this to move ultra-conservative clients off zero equity.

---

## 14.8 ⭐ The Efficient Frontier

With many securities the two-asset curves fill an area — the **feasible (attainable) set**. Its upper-left boundary is the **efficient frontier**.

> ### **The efficient frontier is the set of portfolios that offer the HIGHEST expected return for each level of risk — equivalently, the LOWEST risk for each level of expected return.**

**Also called** the *Markowitz efficient frontier* or the *efficient set*.

### The dominance rule that builds it

Portfolio **P dominates** portfolio **Q** if P has:
- **the same return with less risk**, or
- **the same risk with more return**, or
- **more return AND less risk**.

Every portfolio that is dominated by something is thrown away. What survives is the frontier.

| Where a portfolio sits | Status |
|---|---|
| **On** the efficient frontier | **Efficient** — nothing beats it on both measures |
| **Below / to the right** of it | **Inefficient** — dominated; you can do better on risk, return or both |
| **Above / to the left** of it | **Unattainable** — no such portfolio exists with the given assets |

### Key properties to memorise

1. It is **concave** — it bends upward and to the left. (It can never be convex, because you could then combine two frontier portfolios and beat it.)
2. Its **leftmost point is the Global Minimum Variance Portfolio (GMVP)** — the lowest-risk portfolio obtainable from the asset set.
3. **Everything on the minimum-variance frontier BELOW the GMVP is inefficient** and is discarded. The efficient frontier is only the **upper half**.
4. The frontier is built **without knowing anything about the investor** — it depends only on the assets' returns, variances and covariances.
5. **Adding a new asset with low correlation shifts the frontier up and to the left** — a genuine improvement in the risk-return menu. (This is the theoretical case for adding gold, REITs, InvITs or international equity to an Indian portfolio.)
6. As the number of securities rises, **unsystematic (diversifiable) risk falls towards zero, but systematic (market) risk remains** — the frontier can never reach the vertical axis with risky assets alone.

### Choosing YOUR point on the frontier

The frontier tells you the **menu**; the investor's **risk tolerance** picks the **dish**.

- A risk-averse investor's **indifference curves** are **upward sloping and convex** — each curve joins portfolios giving equal satisfaction.
- **The steeper the curves, the more risk-averse** the investor (a lot of extra return is needed for a little extra risk).
- The **optimal portfolio** is where the investor's **highest attainable indifference curve is tangent to the efficient frontier**.

| Client | Where on the frontier | Typical Indian mix |
|---|---|---|
| 62-year-old retiree, income need | Near the **GMVP** (left end) | Mostly debt funds and G-Secs, small equity slice |
| 35-year-old professional, 20-year goal | **Middle to upper** | Balanced equity/debt |
| 28-year-old with surplus income, high tolerance | **Upper right** | Predominantly equity |

> 🧠 **Memory hook — "The frontier is the menu; risk tolerance is the appetite."**
> Two clients looking at the *same* frontier correctly choose *different* portfolios. Neither is wrong.

> ⚠️ **Exam trap.** The efficient frontier is **not one portfolio** — it is a **whole set of portfolios**, all equally "efficient". Questions asking "which portfolio on the efficient frontier is best?" have the answer "**it depends on the investor's risk tolerance**".

---

## 14.9 The Portfolio Optimisation Process

**Mean-variance optimisation (MVO)** is the mechanical procedure that produces the frontier.

| Step | What happens |
|---|---|
| **1. Define the opportunity set** | List the asset classes or securities the client may hold |
| **2. Estimate the inputs** | For each: **expected return** and **standard deviation**; for each pair: **covariance / correlation**. These are the "capital market expectations" |
| **3. Impose constraints** | **Σwᵢ = 1** (budget constraint); often **wᵢ ≥ 0** (no short selling); plus mandate/regulatory limits such as "max 10% in one stock" or "min 25% in debt" |
| **4. Run the optimiser** | Quadratic programming (or Excel Solver) minimises σ_p² for each target return |
| **5. Trace the efficient frontier** | Repeat step 4 across return levels and join the points |
| **6. Measure the client's risk tolerance** | Risk profiling — capacity *and* willingness |
| **7. Select the optimal portfolio** | The tangency of the client's indifference curve with the frontier |
| **8. Monitor and rebalance** | Inputs change; drift changes weights; revisit periodically |

**The objective function** can be written either way — they give the same frontier:
- **Minimise** σ_p² subject to a required E(R_p), **or**
- **Maximise** E(R_p) subject to a maximum σ_p

A common utility form used to pick the single best point is **U = E(R) − ½ × A × σ²**, where **A is the risk-aversion coefficient** (higher A = more risk-averse). The portfolio with the highest U is that investor's optimum. *Example:* with A = 3, a portfolio with E(R) = 12% and σ = 20% gives U = 0.12 − 0.5(3)(0.04) = 0.12 − 0.06 = **0.06, i.e. a 6% certainty equivalent**.

> ⚠️ Constraints **always** push the achievable frontier **down and to the right** compared with an unconstrained one. That is not a flaw — a "better" unconstrained frontier that requires short-selling or a 90% single-stock position is not investable for a retail client.

---

## 14.10 ⭐ Estimation Issues — "Garbage In, Garbage Out"

MPT's mathematics is exact. Its **inputs are guesses about the future**. That is the gap that matters in practice.

| Issue | What goes wrong | Why it matters |
|---|---|---|
| **Garbage in, garbage out** | The optimiser cannot tell a good estimate from a bad one; it treats every input as certain truth | A precise-looking portfolio built on wrong inputs is still wrong |
| **History ≠ future** | Inputs are usually estimated from past returns; regimes change (rate cycles, reforms, global shocks) | A fund's past 5-year return is a poor forecast of the next 5 |
| **Expected returns are the weakest link** | E(R) is far harder to estimate than σ, and the optimiser is **most sensitive** to it | Errors in expected returns damage the result far more than errors in variances or covariances |
| **Error maximisation** | The optimiser systematically **over-weights** assets whose returns were over-estimated and under-weights those under-estimated | MVO has been described as an **"estimation-error maximiser"** |
| **Corner solutions** | Unconstrained optimisers dump almost everything into two or three assets | The "optimal" portfolio looks absurd and is unstable |
| **Instability** | A tiny change in one expected return can swing the weights dramatically | Re-running the model monthly would trigger constant, costly churn |
| **Unstable correlations** | Correlations are not fixed; they **rise towards +1 in crises** | Diversification fails exactly when it is needed most |
| **Estimation error compounds with n** | n(n+3)/2 estimates — **1,325 for 50 securities** | More assets means more inputs, each carrying error |
| **Non-normal returns** | Real returns are **fat-tailed and skewed**; σ assumes symmetry | Variance **understates** true downside risk |
| **Variance treats upside as risk** | A 30% gain adds to σ exactly like a 30% loss | Investors do not experience upside as "risk" |
| **Real-world frictions ignored** | No taxes, no transaction costs, no liquidity limits, single period | Indian STCG/LTCG, exit loads and STT are all real drags |
| **Ignores non-traded wealth** | Human capital, a business, real estate, EPF | A client's total risk picture is bigger than the securities portfolio |

### How practitioners cope

- **Impose sensible constraints** (caps and floors per asset class) — the simplest and most effective fix
- **Optimise across broad ASSET CLASSES, not individual stocks** — fewer, more stable inputs
- **Use long-run, forward-looking estimates** rather than the last three years
- **Shrinkage estimators, resampling, and the Black-Litterman model**, which blends market-implied returns with the adviser's views
- **Stress-test** by re-running with correlations pushed towards +1
- **Apply judgement** — the model informs the decision; it does not make it

> 🧠 **Memory hook — "The maths is exact; the inputs are opinions."**
> Never present an optimiser output as a precise answer. **Two decimal places of false precision is the most common misuse of MPT.**

> ⚠️ **Exam trap.** "Estimation issues" does **not** mean MPT is useless. The examinable position is: MPT is the **correct conceptual framework** (diversify on correlation, not count), but its **numerical outputs must be treated with caution and constrained by judgement**.

---

## ⚡ Quick Revision Sheet

| Concept | The one-line answer |
|---|---|
| Father of MPT | **Harry Markowitz**, paper *"Portfolio Selection"*, **1952**; **Nobel Prize 1990** |
| The core insight | **Portfolio return = weighted average; portfolio RISK is LESS than the weighted average** |
| Also called | **Mean-variance analysis / mean-variance optimisation (MVO)** |
| Risk measured by | **Variance / standard deviation** of returns |
| All investors are assumed | **Risk-averse** (but with *differing degrees* of aversion) |
| Decisions based on | **Expected return and risk ONLY**, over a **single period** |
| Risk-averse investor | Rejects a fair gamble; demands a **risk premium**; **concave** utility curve |
| Risk-neutral investor | **Indifferent** to risk; decides on **expected return alone**; **straight-line** utility |
| Risk-seeking investor | **Accepts** a fair or unfair gamble; **convex** utility curve |
| Expected return of a security | **E(R) = Σ pᵢRᵢ** |
| Variance of a security | **σ² = Σ pᵢ[Rᵢ − E(R)]²**; **σ = √σ²** |
| Historical variance | ÷ **n** (population) or ÷ **(n − 1)** (sample) |
| Expected return of a portfolio | **E(R_p) = Σ wᵢE(Rᵢ)** — a pure **weighted average** |
| Does correlation affect portfolio RETURN? | **NO** — return is always the weighted average |
| Covariance | **Cov = Σ pᵢ[R_A − E(R_A)][R_B − E(R_B)]**; sign matters, size does not |
| Correlation | **ρ = Cov / (σ_A σ_B)**, always between **−1 and +1** |
| Covariance from correlation | **Cov = ρ × σ_A × σ_B** |
| Two-security risk | **σ_p = √(w₁²σ₁² + w₂²σ₂² + 2w₁w₂σ₁σ₂ρ)** |
| Three-security risk | Add **w₃²σ₃²** plus **all THREE** covariance terms (**6 terms in total**) |
| ρ = +1 | **σ_p = w₁σ₁ + w₂σ₂** exactly — **no diversification benefit** |
| ρ < +1 | **σ_p < weighted average** — benefit exists, and grows as ρ falls |
| ρ = −1 | Risk can be reduced to **ZERO** with **w₁ = σ₂/(σ₁+σ₂)** |
| Why diversification works | Only the **third (covariance) term** contains ρ, and only that term can shrink the total |
| Shape at ρ = +1 | A **straight line**; below +1 the curve **bows leftward** |
| Minimum Variance Portfolio | The **leftmost** point; **w₁\* = (σ₂² − Cov)/(σ₁² + σ₂² − 2Cov)** |
| Efficient frontier | **Highest return for each risk level / lowest risk for each return level** |
| Shape of the frontier | **Concave**, bending up and to the left |
| Global Minimum Variance Portfolio | The **leftmost point** of the frontier; everything **below** it is **inefficient** |
| Below the frontier | **Inefficient (dominated)** |
| Above the frontier | **Unattainable** |
| Which frontier portfolio is "best"? | **Depends on the investor's risk tolerance** — tangency with the indifference curve |
| Indifference curves (risk-averse) | **Upward sloping and convex**; **steeper = more risk-averse** |
| Adding a low-correlation asset | Shifts the frontier **up and to the left** |
| Diversification removes | **Unsystematic risk only** — **systematic (market) risk remains** |
| Number of covariance pairs | **n(n − 1)/2** — **1,225** for 50 securities |
| Total inputs needed | **n(n + 3)/2** — **1,325** for 50 securities |
| Budget constraint | **Σwᵢ = 1** |
| Optimisation objective | Minimise σ_p² for a target return, **or** maximise return for a target risk |
| Utility form | **U = E(R) − ½Aσ²**; higher **A** = more risk-averse |
| Biggest practical weakness | **Garbage in, garbage out** — inputs are estimates |
| Most damaging input error | Errors in **expected returns** |
| MVO nickname | **"Estimation-error maximiser"** |
| Correlations in a crisis | **Rise towards +1** — diversification fails when most needed |
| Practical fixes | **Constraints, asset-class level inputs, shrinkage, resampling, Black-Litterman, judgement** |

> **Exam tip:** if a numerical question gives you two standard deviations, two weights and a correlation, write down **σ_p² = w₁²σ₁² + w₂²σ₂² + 2w₁w₂σ₁σ₂ρ** first and fill it in mechanically — then **remember to take the square root**. Forgetting the final √ is the single most common way candidates lose these marks, and the distractor for the un-square-rooted variance is almost always one of the four options.
