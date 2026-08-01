# Chapter 14: Introduction to Modern Portfolio Theory — Flashcards

Cover the answer, recall it, then check. **The two-security risk formula and the effect of correlation are near-certain exam marks — do the arithmetic out loud, don't just read it.**

**Q1.** Who developed Modern Portfolio Theory, in which paper and year, and what is the theory also called?
> **A:** **Harry Markowitz**, in *"Portfolio Selection"*, **Journal of Finance, 1952**; **Nobel Memorial Prize in Economic Sciences, 1990**. It is also called **mean-variance analysis / mean-variance optimisation (MVO)**.

**Q2.** State the single core insight of MPT in one sentence.
> **A:** A portfolio's **expected return is the weighted average** of its securities' returns, but its **risk is LESS than the weighted average** of their risks — because securities do not move perfectly together.

**Q3.** How does Markowitz diversification differ from naive diversification?
> **A:** Naive diversification just **owns many securities**. Markowitz diversification owns securities that **do not move together** — it uses **covariance/correlation**, not the count of holdings. Thirty IT stocks are *not* diversified.

**Q4.** List the five classic assumptions of MPT.
> **A:** (1) Each investment is a **probability distribution of returns** over a holding period; (2) investors **maximise one-period expected utility**, with **diminishing marginal utility of wealth**; (3) risk is estimated from the **variability of expected returns**; (4) decisions rest on **expected return and risk ONLY**; (5) for a given risk investors prefer **more return**, and for a given return **less risk** — i.e. all are **risk-averse**.

**Q5.** Name four additional working assumptions of MPT.
> **A:** A **single holding period**; **efficient markets** with freely available information; **no taxes or transaction costs**; **perfectly divisible assets**; and **rational investors with homogeneous expectations**.

**Q6.** Does MPT assume every investor has the same risk tolerance?
> **A:** **No.** It assumes every investor is **risk-averse**, but the **degree** differs — which is exactly why different investors choose **different points on the same efficient frontier**.

**Q7.** Define risk aversion.
> **A:** A preference for **certainty over uncertainty when the expected value is the same**. A risk-averse investor demands a **risk premium** — extra expected return — before accepting extra risk.

**Q8.** Given a certain ₹10,00,000 versus a coin toss paying ₹20,00,000 or ₹0, what does each investor type choose?
> **A:** Both have an expected value of ₹10 lakh. The **risk-averse** investor takes the **certain ₹10 lakh**; the **risk-neutral** investor is **indifferent** (he judges on expected return alone); the **risk-seeking** investor takes the **coin toss**.

**Q9.** What shape is each investor type's utility-of-wealth curve, and how does the certainty equivalent compare with the expected value?
> **A:** **Risk-averse → concave**, certainty equivalent **below** expected value. **Risk-neutral → straight line**, certainty equivalent **equal** to it. **Risk-seeking → convex**, certainty equivalent **above** it.

**Q10.** Why must MPT assume risk aversion for the theory to work?
> **A:** If investors were **risk-neutral**, nobody would care about σ, the efficient frontier would collapse to the **single highest-return asset**, and **diversification would be pointless**. Risk aversion is what makes portfolio construction a problem worth solving.

**Q11.** What is the formula for the expected return of an individual security from scenario probabilities?
> **A:** **E(R) = Σ pᵢ × Rᵢ** — each state's probability multiplied by its return, summed.

**Q12.** Boom (p = 0.25) gives 30%, Normal (p = 0.50) gives 12%, Recession (p = 0.25) gives −8%. What is E(R)?
> **A:** 0.25(30) + 0.50(12) + 0.25(−8) = 7.5 + 6.0 − 2.0 = **11.50%**.

**Q13.** State the variance formula for a single security, and explain why deviations are squared.
> **A:** **σ² = Σ pᵢ[Rᵢ − E(R)]²**. Deviations are squared because plain deviations **sum to zero** (pluses cancel minuses), and squaring also **penalises large misses more**. The **square root** then returns the answer to readable percentage points.

**Q14.** Using the data in Q12 (E(R) = 11.5%), what are the variance and standard deviation?
> **A:** 0.25(18.5)² + 0.50(0.5)² + 0.25(−19.5)² = 85.5625 + 0.125 + 95.0625 = **σ² = 180.75**, so **σ = √180.75 = 13.44%**.

**Q15.** Historical returns are 10%, −4%, 16%, 22%, 6%. Give the mean and both standard deviations, and say when each divisor is used.
> **A:** Mean = 50/5 = **10%**; squared deviations sum to **392**. **Population (÷ n):** 392/5 = 78.4 → **σ = 8.85%**. **Sample (÷ n−1):** 392/4 = 98 → **s = 9.90%**. Use **÷ n** for a whole population, **÷ (n−1)** for a *sample* of history — the usual case in finance.

**Q16.** What is the formula for the expected return of a portfolio?
> **A:** **E(R_p) = Σ wᵢ × E(Rᵢ)**, where the weights sum to 1. It is a **pure weighted average**.

**Q17.** ₹12,00,000 in equity expected to return 18% and ₹8,00,000 in debt expected to return 7%. What is E(R_p)?
> **A:** Weights are 0.60 and 0.40. E(R_p) = 0.60(18) + 0.40(7) = 10.8 + 2.8 = **13.60%** — a rupee gain of **₹2,72,000** on ₹20 lakh.

**Q18.** Does correlation affect a portfolio's expected RETURN?
> **A:** **No — never.** Return is always the weighted average. **Correlation affects RISK only.** This is one of the most common exam traps.

**Q19.** Define covariance, state its formula, and give its weakness.
> **A:** It measures **whether two securities move together**: **Cov(A,B) = Σ pᵢ[R_A − E(R_A)][R_B − E(R_B)]**. Its **sign** is meaningful, but its **magnitude is not comparable** across pairs because it carries the units of both securities.

**Q20.** Define correlation — formula, range, and how to convert it back into covariance.
> **A:** **ρ_AB = Cov(A,B) / (σ_A × σ_B)**, always between **−1 and +1**. Rearranged: **Cov(A,B) = ρ_AB × σ_A × σ_B**. *(ρ = 0.4, σ_A = 20%, σ_B = 15% → Cov = 0.4 × 300 = **120**.)*

**Q21.** What do ρ = +1, ρ = 0 and ρ = −1 each mean for diversification?
> **A:** **ρ = +1:** lockstep movement — **zero** diversification benefit. **ρ = 0:** independent — **substantial** benefit. **ρ = −1:** exact mirror images — **maximum** benefit, and risk can be driven to **zero**.

**Q22.** State the two-security portfolio risk formula, in both its forms.
> **A:** **σ_p = √(w₁²σ₁² + w₂²σ₂² + 2·w₁·w₂·σ₁·σ₂·ρ₁₂)** — or, using covariance, **σ_p = √(w₁²σ₁² + w₂²σ₂² + 2·w₁·w₂·Cov₁₂)**.

**Q23.** Which term in the two-security formula creates the diversification benefit, and why?
> **A:** The **third term, 2w₁w₂σ₁σ₂ρ**. It is the **only term containing ρ** and the **only term that can be negative** — the first two are squares and are always positive.

**Q24.** w₁ = 0.60, σ₁ = 20%; w₂ = 0.40, σ₂ = 5%; ρ = 0.30. Compute σ_p.
> **A:** 0.36(400) + 0.16(25) + 2(0.6)(0.4)(20)(5)(0.3) = 144 + 4 + 14.4 = **162.4**. **σ_p = √162.4 = 12.74%** — below the **14.00%** weighted average.

**Q25.** For the same two funds, what is σ_p when ρ = +1, ρ = 0 and ρ = −1?
> **A:** σ_p² = **148 + 48ρ**. **ρ = +1 → 196 → 14.00%** (exactly the weighted average). **ρ = 0 → 148 → 12.17%**. **ρ = −1 → 100 → 10.00%**.

**Q26.** Prove that ρ below +1 always reduces risk below the weighted average.
> **A:** At **ρ = +1** the formula collapses to **(w₁σ₁ + w₂σ₂)²**, so **σ_p equals the weighted average exactly**. Since ρ appears only in the third term and that term shrinks as ρ falls, **any ρ below +1 makes σ_p strictly smaller**. Hence **σ_p ≤ w₁σ₁ + w₂σ₂, with equality only at ρ = +1**.

**Q27.** When ρ = −1, what weights produce a zero-risk portfolio?
> **A:** **w₁ = σ₂/(σ₁ + σ₂)** and **w₂ = σ₁/(σ₁ + σ₂)**. *(With σ₁ = 20% and σ₂ = 5%: w₁ = 5/25 = **0.20**, w₂ = **0.80**, giving σ_p = **0%**.)*

**Q28.** State the three-security portfolio variance formula and count its terms.
> **A:** **σ_p² = w₁²σ₁² + w₂²σ₂² + w₃²σ₃² + 2w₁w₂σ₁σ₂ρ₁₂ + 2w₁w₃σ₁σ₃ρ₁₃ + 2w₂w₃σ₂σ₃ρ₂₃** — **three variance terms plus three covariance terms = six terms**.

**Q29.** For n securities, how many covariance pairs and total estimates are needed — and what is the lesson?
> **A:** **n(n − 1)/2** covariance pairs and **n(n + 3)/2** total estimates. For **n = 50**: **1,225 covariances and 1,325 estimates** — against only **50 variance terms**. The lesson: **portfolio risk is driven overwhelmingly by how holdings interact**, not by any single holding's volatility.

**Q30.** What shape does the two-asset risk/return curve take at different correlations?
> **A:** At **ρ = +1**, a **straight line** between the two assets. Below +1 it **bows leftward** — deeper as ρ falls. At **ρ = −1** it becomes **two straight lines meeting the vertical axis at σ = 0**.

**Q31.** What is the Minimum Variance Portfolio, and what is its two-asset weight formula?
> **A:** The **leftmost point** of the curve — the mix with the **lowest possible risk**. **w₁\* = (σ₂² − Cov₁₂) / (σ₁² + σ₂² − 2Cov₁₂)**.

**Q32.** Why can holding 100% of the SAFER asset be inefficient?
> **A:** Because a mix containing some of the riskier asset can have **both a higher return and a lower standard deviation**. *(Asset X: 16%/24%; Asset Y: 10%/14%; ρ = 0.2. The 20%-X mix returns **11.20%** with σ of **13.04%** — beating 100% Y's 10.00% and 14.00% on both counts.)*

**Q33.** Define the efficient frontier.
> **A:** The set of portfolios offering the **highest expected return for each level of risk** — equivalently the **lowest risk for each level of expected return**. It is **concave**, bending up and to the left.

**Q34.** State the dominance rule, and say what it means to lie below, on or above the frontier.
> **A:** P **dominates** Q if P offers the **same return with less risk**, the **same risk with more return**, or **more of both**. **Below/right → inefficient (dominated)**; **on → efficient**; **above/left → unattainable**.

**Q35.** What is the Global Minimum Variance Portfolio, and what lies below it?
> **A:** The **leftmost point** of the frontier — the lowest-risk portfolio obtainable from the asset set. Everything on the minimum-variance frontier **below** it is **inefficient** and is discarded; the efficient frontier is only the **upper half**.

**Q36.** Which portfolio on the efficient frontier is "the best"?
> **A:** **None in isolation — it depends on the investor's risk tolerance.** The optimum is where the investor's **highest attainable indifference curve is tangent to the frontier**.

**Q37.** What do indifference curves look like for a risk-averse investor, and what does a steeper curve mean?
> **A:** **Upward sloping and convex**. **Steeper = more risk-averse** — a lot of extra return is demanded for a little extra risk.

**Q38.** What happens to the frontier when a new low-correlation asset is added?
> **A:** It shifts **up and to the left** — a genuinely better risk-return menu. This is the theoretical case for adding **gold, REITs, InvITs or international equity** to an Indian portfolio.

**Q39.** List the main steps of the portfolio optimisation process.
> **A:** Define the **opportunity set** → estimate **returns, variances and covariances** → impose **constraints (Σw = 1, no short selling, mandate limits)** → **run the optimiser** → **trace the efficient frontier** → assess the client's **risk tolerance** → **select the optimal portfolio** → **monitor and rebalance**.

**Q40.** State the optimisation objective in its two equivalent forms, and the utility function used to pick one point.
> **A:** **Minimise σ_p²** for a required return, **or maximise E(R_p)** for a maximum risk — both trace the same frontier. To pick a single point: maximise **U = E(R) − ½ × A × σ²**, where **A is the risk-aversion coefficient**.

**Q41.** What effect do constraints such as "no short selling" have on the frontier?
> **A:** They push the achievable frontier **down and to the right**. That is not a flaw — an unconstrained "better" frontier requiring short sales or a 90% single-stock weight is **not investable** for a retail client.

**Q42.** Explain "garbage in, garbage out" in the MPT context.
> **A:** The mathematics is exact but the **inputs are forecasts**. The optimiser cannot tell a good estimate from a bad one and treats every input as certain truth, so a **precise-looking portfolio built on wrong inputs is still wrong**.

**Q43.** Which input error is most damaging, what nickname does MVO earn, and what is a "corner solution"?
> **A:** Errors in **expected returns** — far more damaging than errors in variances or covariances. Because the optimiser **over-weights assets whose returns were over-estimated**, MVO is called an **"estimation-error maximiser"**. A **corner solution** is its typical output when unconstrained: nearly everything piled into **two or three assets**, unstable and implausible.

**Q44.** What happens to correlations in a crisis, and why is variance itself criticised as a risk measure?
> **A:** Correlations **rise towards +1** as investors sell everything at once, so **diversification weakens exactly when it is needed most**. Variance is criticised because it treats **upside volatility as risk** and assumes **symmetric, normally distributed returns**, whereas real returns are **fat-tailed and skewed** — so σ **understates true downside risk**.

**Q45.** How do practitioners cope with MPT's estimation problems, and does diversification remove all risk?
> **A:** **Impose constraints**; optimise across **broad asset classes rather than individual stocks**; use **long-run forward-looking estimates**; apply **shrinkage, resampling or Black-Litterman**; **stress-test** with correlations at +1; and overlay **judgement**. Diversification removes only **unsystematic risk** — **systematic (market) risk always remains**.
