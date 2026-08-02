# Chapter 10: Understanding Derivatives — Flashcards

Cover the answer, recall it, then check. **The four option positions and the forward-vs-futures table carry the most marks.**

**Q1.** Define a derivative.
> **A:** A **contract whose value is derived from an underlying asset** — it has no independent value of its own.

**Q2.** Name five purposes derivatives serve.
> **A:** **Risk transfer**, **price discovery**, **leverage**, **lower transaction costs** than trading the underlying, and **market completion** (payoffs otherwise unavailable).

**Q3.** Give five differences between a forward and a future.
> **A:** **Forward** — OTC, customised, counterparty risk, no margin, settled only at maturity. **Future** — exchange-traded, standardised, **CCP-guaranteed**, margined, **daily mark to market**.

**Q4.** What is the single biggest difference between forwards and futures?
> **A:** **Futures are guaranteed by the clearing corporation and settled daily; forwards are not** — a forward leaves you exposed to the other party's default.

**Q5.** State the fundamental asymmetry of options.
> **A:** The **buyer has a RIGHT without an OBLIGATION**; the **seller (writer) has an OBLIGATION without a right**. That asymmetry is the whole concept.

**Q6.** What does a call buyer have the right to do, and what is their view?
> **A:** The right to **BUY** the underlying at the strike price. The view is **bullish**.

**Q7.** What does a put buyer have the right to do, and what is their view?
> **A:** The right to **SELL** the underlying at the strike price. The view is **bearish**.

**Q8.** State maximum gain and loss for a LONG CALL.
> **A:** Maximum loss = **the premium**. Maximum gain = **unlimited** (the price can rise without limit).

**Q9.** State maximum gain and loss for a SHORT CALL.
> **A:** Maximum gain = **the premium**. Maximum loss = **UNLIMITED** ⚠️ — the riskiest of the four basic positions.

**Q10.** State maximum gain and loss for a LONG PUT.
> **A:** Maximum loss = **the premium**. Maximum gain is large but **capped**, because the underlying can only fall to zero.

**Q11.** State maximum gain and loss for a SHORT PUT.
> **A:** Maximum gain = **the premium**. Maximum loss is large but capped (underlying falling to zero).

**Q12.** Why must option sellers post margin while buyers need not?
> **A:** Because a **buyer's loss is capped at the premium already paid**, while a **seller's loss can be unlimited** (short call) or very large (short put). The margin secures that open-ended obligation.

**Q13.** State the break-even for a long call and a long put.
> **A:** **Long call break-even = Strike + Premium.** **Long put break-even = Strike − Premium.**

**Q14.** State the intrinsic value formulas.
> **A:** **Call = max(Spot − Strike, 0).** **Put = max(Strike − Spot, 0).** Intrinsic value is **never negative**.

**Q15.** What is time value, and what happens to it?
> **A:** **Time value = Premium − Intrinsic value.** It **decays to zero at expiry**, when the premium equals intrinsic value exactly.

**Q16.** Define moneyness for calls and puts.
> **A:** **Call:** ITM when Spot > Strike; OTM when Spot < Strike. **Put:** ITM when Spot < Strike; OTM when Spot > Strike. **ATM** when Spot = Strike for both.

**Q17.** Can an option be in the money and still lose money? Explain.
> **A:** **Yes.** A call with strike ₹1,000 bought for ₹40 with spot at ₹1,020 has intrinsic value ₹20 but cost ₹40 — a **₹20 loss** despite being ITM. **The premium must be recovered first: ITM ≠ profitable.**

**Q18.** Distinguish European from American options, and state the Indian standard.
> **A:** **European** — exercisable **only at expiry**. **American** — exercisable **any time up to expiry**. Indian index and stock options are **European**.

**Q19.** State the cost-of-carry relationship.
> **A:** **F = S × (1 + r − q)^T** (or F = S × e^((r−q)T)), where r is the risk-free rate and q the income yield (e.g. dividends).

**Q20.** What are contango and backwardation?
> **A:** **Contango** — futures price **above** spot (the normal state, reflecting carrying cost). **Backwardation** — futures price **below** spot.

**Q21.** What happens to the futures price at expiry, and why?
> **A:** It **converges to the spot price** — enforced by **arbitrage**, since any gap could be captured risk-free at that moment.

**Q22.** Define basis.
> **A:** **Basis = Spot price − Futures price.**

**Q23.** What is a swap, and what is the most common type?
> **A:** An agreement to **exchange cash flows** on specified dates. The most common is the **interest rate swap** — one party pays **fixed** and receives **floating**, the other the reverse. Swaps are **OTC**.

**Q24.** Define hedging, and state what it costs.
> **A:** **Reducing or eliminating an EXISTING risk** using a derivative. Its cost: it **converts uncertainty into certainty**, so a favourable market move is given up. A hedge is not designed to make money.

**Q25.** Give three examples of hedging.
> **A:** A **farmer sells futures** to lock in a crop price; an **investor buys index puts** to protect a portfolio; an **importer buys currency futures** to fix a payable.

**Q26.** Define speculation and arbitrage.
> **A:** **Speculation** — taking on risk to profit from an expected move, with **no underlying exposure**. **Arbitrage** — simultaneously buying and selling in two markets to lock in a **risk-free** profit from a price difference.

**Q27.** How do the three participant types form an ecosystem?
> **A:** **Hedgers transfer** risk, **speculators absorb** it and supply liquidity, and **arbitrageurs keep prices correct** — and by acting, eliminate the mispricing they exploit.

**Q28.** What is the defining danger of derivatives compared with equity?
> **A:** With equity your maximum loss is the amount invested. With a derivative, **losses can EXCEED the margin deposited** — and daily MTM demands those losses in cash immediately.

**Q29.** What is basis risk?
> **A:** The risk that the **hedge and the exposure do not move perfectly together**, leaving the hedge imperfect.

**Q30.** Name the main risks of derivatives.
> **A:** **Leverage risk**, **counterparty risk** (OTC), **liquidity risk**, **basis risk**, **model/valuation risk** and **operational risk**.

**Q31.** Who regulates equity, currency and commodity derivatives in India?
> **A:** **Equity — SEBI.** **Currency — SEBI and RBI jointly.** **Commodity — SEBI** (since the FMC merged into SEBI in **2015**).

**Q32.** What is mark to market, and open interest?
> **A:** **MTM** is the **daily settlement** of gains and losses to margin accounts. **Open interest** is the total number of contracts outstanding — a gauge of participation.

**Q33.** Describe a protective put and a covered call.
> **A:** **Protective put** = hold the stock **+ buy a put** — bullish but wants **downside insurance**. **Covered call** = hold the stock **+ sell a call** — earns premium but **caps the upside**.

**Q34.** Describe a long straddle and what view it expresses.
> **A:** **Buy a call AND a put at the same strike.** It profits from a **big move in either direction** — the view is on **volatility**, not direction.

**Q35.** A call with strike ₹1,000 costs ₹40. Give the profit at spot prices of ₹1,090, ₹1,020 and ₹950.
> **A:** **₹1,090:** intrinsic 90 − premium 40 = **+₹50**. **₹1,020:** intrinsic 20 − 40 = **−₹20**. **₹950:** intrinsic 0 − 40 = **−₹40** (the full premium). Break-even is **₹1,040**.

**Q36.** What two questions should you ask first in any option problem?
> **A:** **(1) Is it a call or a put? (2) Am I the buyer or the seller?** Those two answers fix the rights, obligations, maximum gain and maximum loss immediately.

**Q37.** What are the settlement conventions for Indian equity derivatives?
> **A:** **European-style** options, **monthly expiry**, **cash-settled** for indices, with **physical settlement** for stock derivatives.

**Q38.** Why does leverage make derivatives dangerous for retail investors?
> **A:** A **small margin controls a large exposure**, so a modest adverse move in the underlying can wipe out — and exceed — the entire amount deposited, with **margin calls demanded in cash the same day**.
