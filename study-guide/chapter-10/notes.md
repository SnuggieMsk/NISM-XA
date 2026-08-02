# Chapter 10: Understanding Derivatives — Short Notes

> **Module 3 · Investment Products (30 marks).**
> Conceptually the trickiest chapter, but the exam questions are mostly **definitional and payoff-based**. Master the **four rights-and-obligations combinations** for options and the **forward vs futures** table, and most questions answer themselves.

---

## 10.1 Basics of Derivatives

**A derivative is a contract whose value is DERIVED from an underlying asset.**

The derivative has no independent value — it is a claim whose worth depends entirely on what happens to something else.

**Underlyings can be:** equity shares, indices, interest rates, currencies, commodities, bonds — even weather or credit events.

### Why derivatives exist
1. **Risk transfer** — those who don't want a risk can pass it to those willing to bear it.
2. **Price discovery** — futures prices reveal market expectations.
3. **Leverage** — a large exposure for a small outlay (margin).
4. **Lower transaction costs** than trading the underlying.
5. **Market completion** — payoffs otherwise unavailable.

---

## 10.2 Underlying Concepts

| Term | Meaning |
|---|---|
| **Underlying** | The asset from which value is derived |
| **Spot price** | Today's price of the underlying |
| **Futures/forward price** | The agreed price for a future transaction |
| **Contract size / lot** | The standardised quantity per contract |
| **Expiry** | The date the contract ends (Indian equity derivatives: monthly, on a specified weekday) |
| **Margin** | Collateral deposited to cover potential loss |
| **Mark to market (MTM)** | Daily settlement of gains/losses to margin accounts |
| **Open interest** | Total number of contracts outstanding — a gauge of participation |
| **Basis** | **Spot price − Futures price** |
| **Cost of carry** | Interest, storage and insurance costs less income (e.g. dividends) from holding the underlying |

### The cost-of-carry relationship

$$\boxed{F = S \times e^{(r-q)T}} \quad \text{or approximately} \quad F = S \times (1 + r - q)^T$$

where **S** = spot, **r** = risk-free rate, **q** = income yield (dividends), **T** = time.

> 🧠 **Normally the futures price exceeds spot** (called **contango**) because holding the asset costs interest. When the futures price is **below** spot, the market is in **backwardation**. **At expiry, the futures price converges to the spot price** — this convergence is guaranteed by arbitrage.

---

## 10.3 ⭐ Types of Derivative Products

### 10.3.1 Forwards
A **customised, bilateral (OTC)** agreement to buy or sell an asset at a set price on a future date.

- ✅ Fully customisable in size, date and terms
- ❌ **Counterparty risk** — no guarantee the other side performs
- ❌ Illiquid; hard to exit before maturity
- Settlement occurs **only at maturity**

### 10.3.2 Futures
A **standardised, exchange-traded** forward.

| | **Forward** | **Futures** |
|---|---|---|
| **Traded** | OTC, bilateral | **Exchange** |
| **Terms** | Customised | **Standardised** (lot size, expiry) |
| **Counterparty risk** | **High** — rests with the other party | **Eliminated** — the clearing corporation is the CCP |
| **Margin** | Usually none | **Mandatory** (initial + MTM) |
| **Settlement** | At maturity only | **Daily mark to market** |
| **Liquidity** | Low | High |
| **Regulation** | Light | Fully regulated |

> ⚠️ **The single biggest difference: futures are guaranteed by the clearing corporation and settled daily; forwards are not.**

### 10.3.3 ⭐ Options

**An option gives the BUYER a RIGHT without an OBLIGATION. The SELLER (writer) has an OBLIGATION without a right.**

That asymmetry is the whole concept — and the source of most exam questions.

| | **Call option** | **Put option** |
|---|---|---|
| **Buyer has the right to** | **BUY** the underlying | **SELL** the underlying |
| **Buyer's view** | **Bullish** | **Bearish** |
| **Buyer pays** | Premium | Premium |
| **Buyer's maximum loss** | **The premium** | **The premium** |
| **Buyer's maximum gain** | **Unlimited** | Large but capped (the price can only fall to zero) |
| **Seller's view** | Neutral-to-bearish | Neutral-to-bullish |
| **Seller's maximum gain** | **The premium** | **The premium** |
| **Seller's maximum loss** | **Unlimited** | Large but capped |

> 🧠 **The four positions to know cold:**
> - **Long call** — bullish · pay premium · loss capped at premium · **unlimited** gain
> - **Long put** — bearish · pay premium · loss capped at premium · large gain
> - **Short call** — receive premium · gain capped at premium · **UNLIMITED loss** ⚠️
> - **Short put** — receive premium · gain capped at premium · large loss
>
> **Option sellers face far greater risk than buyers.** A buyer can lose only the premium; a **short call has theoretically unlimited loss**. This is why sellers must post margin and buyers need not.

#### Key option terms

| Term | Meaning |
|---|---|
| **Strike (exercise) price** | The price at which the option can be exercised |
| **Premium** | The price paid by the buyer to the seller |
| **European option** | Exercisable **only at expiry** — the Indian standard for index and stock options |
| **American option** | Exercisable **any time up to expiry** |
| **Intrinsic value** | The immediate exercise value — **never negative** |
| **Time value** | Premium − intrinsic value; **decays to zero at expiry** |

#### Moneyness

| | **Call** | **Put** |
|---|---|---|
| **In the money (ITM)** | Spot > Strike | Spot < Strike |
| **At the money (ATM)** | Spot = Strike | Spot = Strike |
| **Out of the money (OTM)** | Spot < Strike | Spot > Strike |

**Intrinsic value:** Call = **max(Spot − Strike, 0)**; Put = **max(Strike − Spot, 0)**.

#### Payoffs at expiry

- **Long call:** Payoff = max(S − K, 0) − Premium. **Break-even = Strike + Premium.**
- **Long put:** Payoff = max(K − S, 0) − Premium. **Break-even = Strike − Premium.**
- **Short call:** Premium − max(S − K, 0)
- **Short put:** Premium − max(K − S, 0)

**Worked example.** Buy a call, strike ₹1,000, premium ₹40.
- Break-even = 1,000 + 40 = **₹1,040**
- Spot at expiry ₹1,090 → intrinsic 90, profit = 90 − 40 = **+₹50**
- Spot ₹1,020 → intrinsic 20, profit = 20 − 40 = **−₹20** (a loss, though the option is ITM)
- Spot ₹950 → intrinsic 0, loss = **−₹40** (the full premium)

> ⚠️ **Classic trap:** an option can be **in the money and still lose money**, because the premium must be recovered first. ITM ≠ profitable.

### 10.3.4 Swaps
An agreement to **exchange cash flows** on specified dates.

- **Interest rate swap** — the most common: one party pays **fixed** and receives **floating**, the other the reverse. Used to convert floating-rate borrowing into fixed, or vice versa.
- **Currency swap** — exchange principal and interest in different currencies.
- Swaps are **OTC** instruments.

---

## 10.4 Structure of Derivative Markets

| | **OTC** | **Exchange traded** |
|---|---|---|
| **Contracts** | Customised | Standardised |
| **Counterparty risk** | Present | Eliminated by the CCP |
| **Transparency** | Low | High |
| **Regulation** | Lighter | Full |
| **Examples** | Forwards, swaps, exotic options | Futures, listed options |

---

## 10.5 ⭐ Purpose of Derivatives

### Hedging
**Reducing or eliminating an existing risk.** The hedger already has an exposure and uses a derivative to offset it.

- A farmer with a standing crop **sells futures** to lock in a price.
- An investor holding equity **buys index puts** to protect against a fall (a "protective put").
- An importer with a dollar payable **buys dollar futures** to fix the cost.

> 🧠 **A hedge is not designed to make money.** It converts an uncertain outcome into a certain one — and if the market moves favourably, the hedge gives up that gain. That is the price of certainty.

### Speculation
**Taking on risk to profit from an expected price move**, with no underlying exposure. Leverage magnifies both gains and losses. Speculators supply the liquidity hedgers need.

### Arbitrage
**Simultaneously buying and selling in two markets to lock in a risk-free profit** from a price difference. Example: if futures are priced above their fair cost-of-carry value, buy the spot and sell the future. Arbitrage keeps prices aligned and, by its own action, eliminates the mispricing it exploits.

> 🧠 **The three participants form an ecosystem:** hedgers **transfer** risk, speculators **absorb** it and supply liquidity, and arbitrageurs **keep prices correct**.

---

## 10.6 Costs, Benefits and Risks

**Benefits:** risk management, price discovery, leverage/capital efficiency, lower transaction costs, and the ability to take a view in either direction (including going short).

**Costs and risks:**

| Risk | Explanation |
|---|---|
| **Leverage risk** | A small margin controls a large exposure — losses can **exceed the initial outlay** |
| **Counterparty risk** | In OTC contracts (eliminated on exchange) |
| **Liquidity risk** | Far-month or deep OTM contracts may be thinly traded |
| **Basis risk** | The hedge and the exposure do not move perfectly together, so the hedge is imperfect |
| **Model/valuation risk** | Complex instruments may be mispriced |
| **Operational risk** | Margin calls, settlement failures, errors |

> ⚠️ **The defining danger:** unlike equity, where the maximum loss is the amount invested, a **derivative position can lose more than the margin deposited**. Daily MTM means losses are demanded in cash immediately.

---

## 10.7 Equity, Currency and Commodity Derivatives

| Segment | Underlying | Regulator | Examples |
|---|---|---|---|
| **Equity derivatives** | Indices and individual stocks | **SEBI** | Nifty and Bank Nifty futures & options, stock futures & options |
| **Currency derivatives** | Currency pairs | **SEBI and RBI jointly** | USD-INR, EUR-INR, GBP-INR, JPY-INR futures & options |
| **Commodity derivatives** | Metals, energy, agri | **SEBI** (since 2015, when FMC merged into SEBI) | Gold, silver, crude, cotton, guar |
| **Interest rate derivatives** | Government securities | SEBI / RBI | Interest rate futures |

**Indian equity derivatives:** European-style options, **monthly expiry**, **cash-settled** for indices; stock derivatives moved to **physical settlement**.

---

## 10.8 Derivative Strategies (introductory)

| Strategy | Construction | View |
|---|---|---|
| **Protective put** | Hold the stock + buy a put | Bullish but wants **downside insurance** |
| **Covered call** | Hold the stock + sell a call | Neutral to mildly bullish; earns premium, **caps upside** |
| **Long straddle** | Buy a call and a put at the **same strike** | Expects a **big move**, direction unknown |
| **Long strangle** | Buy an OTM call and an OTM put | Same view, cheaper, needs a bigger move |
| **Bull call spread** | Buy a lower-strike call, sell a higher-strike call | Moderately bullish; caps both cost and gain |
| **Bear put spread** | Buy a higher-strike put, sell a lower-strike put | Moderately bearish |

---

## ⚡ Quick Revision Sheet

| Concept | The one-line answer |
|---|---|
| Derivative | A contract whose value is **derived** from an underlying |
| Forward | **OTC, customised**, counterparty risk, settled at maturity |
| Futures | **Exchange-traded, standardised**, CCP-guaranteed, **daily MTM** |
| Option buyer | Has a **right, no obligation**; pays premium; **loss capped at premium** |
| Option seller | Has an **obligation, no right**; receives premium; **risk far greater** |
| Long call | Bullish; **unlimited** gain; loss = premium |
| Long put | Bearish; large gain; loss = premium |
| Short call | **UNLIMITED loss** ⚠️; gain = premium |
| Short put | Large loss; gain = premium |
| Call break-even | **Strike + Premium** |
| Put break-even | **Strike − Premium** |
| Call intrinsic value | max(Spot − Strike, 0) |
| Put intrinsic value | max(Strike − Spot, 0) |
| Time value | Premium − intrinsic; **decays to zero at expiry** |
| ITM call | Spot **>** Strike |
| ITM put | Spot **<** Strike |
| European option | Exercisable **only at expiry** (the Indian standard) |
| American option | Exercisable **any time** |
| Cost of carry | F = S × (1 + r − q)^T |
| Contango | Futures **above** spot (normal) |
| Backwardation | Futures **below** spot |
| At expiry | Futures price **converges to spot** |
| Basis | Spot − Futures |
| Hedging | **Reducing an existing** risk; gives up favourable moves |
| Speculation | Taking risk for profit, **no underlying exposure** |
| Arbitrage | **Risk-free** profit from a price difference in two markets |
| Swap | Exchange of **cash flows**; OTC |
| Interest rate swap | Fixed for floating |
| Key derivative danger | Losses can **exceed the margin deposited** |
| Basis risk | The hedge doesn't move perfectly with the exposure |
| Currency derivatives regulator | **SEBI and RBI jointly** |
| Commodity derivatives regulator | **SEBI** (FMC merged in 2015) |
| Protective put | Stock + long put = downside insurance |
| Covered call | Stock + short call = premium income, capped upside |
| Long straddle | Same-strike call + put; expects a **big move either way** |

> **Exam tip:** for any option question, first write down **(1) is it a call or a put, (2) am I the buyer or the seller?** Those two answers fix the rights, obligations, maximum gain and maximum loss immediately. Then apply the break-even formula.
