# Chapter 8: Investing in Stocks — Short Notes

> **Module 3 · Investment Products (30 marks).**
> ⭐ The **valuation ratios** in 8.5.4 are guaranteed exam marks — learn each formula, what it means, and when it fails. Fundamental vs technical analysis is the other reliable question source.

---

## 8.1 Equity as an Investment

Buying a share makes you a **part-owner** of a business. Your return comes from two sources:

$$\textbf{Total Return} = \textbf{Capital Appreciation} + \textbf{Dividend Yield}$$

**Why equity works over the long run:** a company's earnings tend to grow with the economy and with inflation, so equity is a claim on a **growing, inflation-linked stream of profits** — unlike a bond, whose coupon is fixed in nominal terms.

**The cost:** ownership is a **residual** claim. Shareholders are paid last, dividends are discretionary, and the capital can be lost entirely.

---

## 8.2 Diversification of Risk

Diversification reduces risk **without necessarily reducing expected return** — the closest thing to a free lunch in investing. It works because assets do not move in perfect lock-step.

### Two dimensions

| | **Cross-sectional diversification** | **Time-series diversification** |
|---|---|---|
| **Meaning** | Spreading across **many securities, sectors and asset classes at one point in time** | Spreading **entry across time** |
| **Reduces** | Company- and sector-specific risk | The risk of investing everything at a bad price |
| **In practice** | A diversified portfolio | **SIP / rupee-cost averaging** |

> ⚠️ **Critical limit:** diversification eliminates **unsystematic** (company/sector-specific) risk but **cannot eliminate systematic (market) risk**. When the whole market falls, diversification does not save you. Beyond roughly 15–25 well-chosen, low-correlation stocks, additional names add little.
>
> And remember Chapter 7's trap: **20 banking stocks are not diversified.** Diversification requires **low correlation**, not merely a high count.

---

## 8.3 Risks of Equity Investment

| Risk | What it is | Diversifiable? |
|---|---|---|
| **Market risk** | The whole market falls — recessions, rate shocks, geopolitics | ❌ **No** (systematic) |
| **Sector-specific risk** | A sector suffers — regulation, commodity prices, technology shifts | ✅ Yes, across sectors |
| **Company-specific risk** | One firm fails — fraud, product failure, management error | ✅ Yes, across companies |
| **Transactional risk** | Execution and settlement problems, bad fills, operational error | Partly, via good practice |
| **Liquidity risk** | Cannot exit at a fair price; wide spreads in small-caps | Partly, via avoiding illiquid names |

> 🧠 **Systematic (market) risk is compensated** — you are paid a risk premium for bearing it because you cannot avoid it. **Unsystematic risk is not compensated**, because you could have diversified it away for free. This idea underpins CAPM and beta in Chapters 14 and 16.

---

## 8.4 Overview of the Equity Market

- **Primary market** — IPOs, FPOs, rights issues (Chapter 6)
- **Secondary market** — NSE, BSE, T+1 settlement
- **Segments by size** — large-cap, mid-cap, small-cap (SEBI defines these by market-cap rank: **1–100 large, 101–250 mid, 251 onwards small**)
- **Indices** — Nifty 50, Sensex; free-float market-cap weighted

---

## 8.5 Equity Research and Stock Selection

### 8.5.1 Fundamental Analysis

Estimating a security's **intrinsic value** from the underlying business — earnings, assets, growth, management, industry — and comparing it with the market price.

$$\text{If Intrinsic Value} > \text{Market Price} \Rightarrow \text{potentially undervalued (buy)}$$

#### Top-down vs bottom-up

| | **Top-down** | **Bottom-up** |
|---|---|---|
| **Starts with** | The **economy** | The **company** |
| **Then** | Economy → industry → company | Company merits, largely regardless of macro |
| **Suits** | Cyclical and macro-driven sectors | Stock-pickers seeking mispriced individual firms |

#### Buy-side vs sell-side research

| | **Sell-side** | **Buy-side** |
|---|---|---|
| **Works for** | Brokers, investment banks | Mutual funds, insurers, PMS, pension funds |
| **Research is** | **Published** to clients, often with buy/hold/sell recommendations | **Internal and proprietary** |
| **Paid via** | Brokerage/commissions | The employer's own returns |
| **Conflict** | May face pressure from banking relationships | Fewer external conflicts |

#### Sector classification
Grouping companies by business activity (banking, IT, FMCG, pharma, auto) so that peers can be compared and sector exposures measured.

### 8.5.2 The Stock Analysis Process — E → I → C

**1. Economy analysis** — GDP growth, inflation, interest rates, fiscal and monetary policy, currency, commodity prices, the global cycle.

**2. Industry/sector analysis** — industry life cycle (pioneering → expansion → maturity → decline), competitive intensity, regulation, entry barriers, pricing power, input costs.

**3. Company analysis** — two halves:

- **Quantitative:** revenue and profit growth, margins, return on equity, debt levels, cash flow quality, working capital.
- **Qualitative:** management quality and integrity, business model, competitive advantage ("moat"), corporate governance, related-party transactions, promoter pledging.

### 8.5.3 Fundamentals-Driven Models (absolute valuation)

#### Discounted Cash Flow (DCF)

The value of a business is the **present value of its future cash flows**:

$$\boxed{\text{Value} = \sum_{t=1}^{n} \frac{CF_t}{(1+r)^t} + \frac{\text{Terminal Value}}{(1+r)^n}}$$

**Terminal value** (Gordon growth): $TV = \dfrac{CF_{n+1}}{r-g}$, requiring **g < r**.

- ✅ Theoretically the soundest method — it values the business on its own merits.
- ❌ **Extremely sensitive** to assumptions about growth (g) and discount rate (r). Small changes swing the answer wildly, and the terminal value often dominates. *"Garbage in, gospel out."*

#### Dividend Discount Model
A DCF variant using dividends: $P_0 = \dfrac{D_1}{r-g}$. Works only for stable dividend payers.

#### Asset-based valuation
Value = **net assets** (assets − liabilities), i.e. book value. Useful for asset-heavy or liquidating businesses; poor for service or brand-driven companies whose value is intangible.

### 8.5.4 ⭐ Market-Driven Models — Relative Valuation

Relative valuation compares a company with **peers or its own history** using multiples. Faster and more intuitive than DCF, but it only tells you whether a stock is cheap **relative to something else** — if the whole sector is overvalued, relative valuation will not reveal it.

| Ratio | Formula | What it says | Watch out for |
|---|---|---|---|
| **P/E** | Price ÷ Earnings per share | What you pay per ₹1 of earnings | **Meaningless if earnings are negative**; distorted by one-off items |
| **P/B** | Price ÷ Book value per share | Price relative to net assets | Best for **banks and financials**; poor for asset-light firms |
| **P/S** | Price ÷ Sales per share | Price per ₹1 of revenue | Useful for **loss-making** or early-stage firms; **ignores profitability entirely** |
| **PEG** | P/E ÷ Earnings growth rate (%) | P/E adjusted for growth | **PEG < 1** often suggests good value; depends on a reliable growth estimate |
| **EV/EBITDA** | Enterprise Value ÷ EBITDA | Whole-firm value vs operating cash earnings | **Capital-structure neutral**, so it compares differently-leveraged firms fairly |
| **EBIT/EV** | EBIT ÷ Enterprise Value | The "earnings yield" of the whole firm | The inverse of an EV multiple |
| **EV/Sales** | Enterprise Value ÷ Sales | Whole-firm value per ₹1 of revenue | For loss-makers; ignores margins |
| **Dividend yield** | Dividend per share ÷ Price | Cash income return | A **high yield can signal a falling price**, not generosity |
| **Earnings yield** | EPS ÷ Price (the inverse of P/E) | Earnings return on the price paid | Comparable with bond yields |

**Enterprise Value:** $EV = \text{Market Cap} + \text{Debt} - \text{Cash}$ — what it would cost to buy the whole business including its debts.

#### EVA and MVA

- **EVA (Economic Value Added)** = Net Operating Profit After Tax − (Capital × Cost of Capital). **Positive EVA means the firm earned more than its cost of capital** — genuine value creation, not just accounting profit.
- **MVA (Market Value Added)** = Market Value of the firm − Capital Invested. The market's verdict on cumulative value creation.

#### Industry-specific metrics
Because standard ratios do not fit every sector: **banks** — Net Interest Margin, Gross/Net NPA, CASA ratio, capital adequacy; **telecom** — ARPU, subscriber count; **retail** — same-store sales growth, sales per square foot; **hotels** — occupancy, average room rate; **IT** — utilisation, attrition, billing rates.

### 8.6 Combining Relative and DCF Approaches
Best practice uses **both**: DCF anchors value in the business's own economics; relative multiples sanity-check that answer against what the market pays for comparable firms. When the two diverge sharply, the assumptions deserve re-examination.

---

## 8.7 Technical Analysis

**Technical analysis studies price and volume history to forecast future price movements** — it ignores intrinsic value entirely.

### 8.7.1 Assumptions
1. **The market discounts everything** — all information is already in the price.
2. **Prices move in trends** — and a trend is more likely to continue than to reverse.
3. **History repeats itself** — because human psychology is consistent, price patterns recur.

### 8.7.2 Technical vs Fundamental Analysis

| | **Fundamental** | **Technical** |
|---|---|---|
| **Studies** | Financial statements, economy, industry, management | **Price and volume charts** |
| **Answers** | **What** to buy | **When** to buy or sell |
| **Horizon** | Long term | Short to medium term |
| **Basis** | Intrinsic value | Market psychology and trends |
| **Data** | Fundamentals, released periodically | Price/volume, continuous |

> 🧠 **The clean way to remember it: fundamental analysis tells you WHAT to buy; technical analysis tells you WHEN.** Many practitioners use both.

### 8.7.3 Advantages of technical analysis
Applicable to any traded instrument; timing-focused; provides clear entry, exit and stop-loss levels; works when fundamental data is unavailable or stale; captures sentiment that fundamentals miss.

### 8.7.4 Technical rules and indicators

| Tool | What it does |
|---|---|
| **Support** | A price level where buying has historically emerged, halting a fall |
| **Resistance** | A level where selling has historically emerged, capping a rise |
| **Trendline** | A line joining successive highs or lows, defining the trend |
| **Moving average** | Smooths price to reveal the trend; crossovers signal changes |
| **RSI** | Relative Strength Index (0–100); conventionally **>70 overbought, <30 oversold** |
| **MACD** | Moving Average Convergence Divergence — momentum via the relationship between two moving averages |
| **Bollinger Bands** | Bands set a number of standard deviations around a moving average, showing relative volatility |
| **Volume** | Confirms a move — a price break on **high volume** is more credible |
| **Chart patterns** | Head-and-shoulders, double top/bottom, triangles, flags |
| **Candlesticks** | Doji, hammer, engulfing patterns signalling potential reversals |

> ⚠️ **Once support is broken it often becomes resistance** (and vice versa) — a classic exam point.

### 8.7.5 Fixed income and technical analysis
Technical analysis can be applied to **bond yields and prices**, and to interest-rate futures, though fundamental drivers (monetary policy, inflation, credit) dominate more than in equity.

---

## 8.8 Qualitative Evaluation and Corporate Governance

Numbers describe the past; **quality of management and governance determines whether the future resembles it.**

**What a stock picker examines:**

- **Board composition** — genuinely independent directors, relevant expertise
- **Promoter holding and pledging** — high **pledged shares** are a serious red flag (forced selling risk)
- **Related-party transactions** — potential siphoning of value
- **Auditor quality** — and any **auditor resignation**, a major warning sign
- **Disclosure quality** — clear, consistent, timely reporting
- **Capital allocation record** — has management reinvested wisely, or built empires?
- **Minority shareholder treatment** — dividend policy, fairness in group restructurings
- **Accounting aggressiveness** — revenue recognition, related-party receivables, frequent "exceptional items"

> ⚠️ **Governance red flags to memorise:** frequent **auditor changes or resignations**, high **promoter pledging**, large **related-party transactions**, repeated restatements, opaque group structures, and a persistent gap between **reported profit and operating cash flow**.

---

## ⚡ Quick Revision Sheet

| Concept | The one-line answer |
|---|---|
| Equity total return | Capital appreciation + dividend yield |
| Cross-sectional diversification | Across **securities/sectors** at one time |
| Time-series diversification | Across **time** — i.e. a SIP |
| Diversification eliminates | **Unsystematic** risk only |
| Systematic risk | Market-wide, **undiversifiable**, and **compensated** |
| Unsystematic risk | Company/sector-specific, diversifiable, **not compensated** |
| SEBI cap definitions | 1–100 large, 101–250 mid, 251+ small |
| Fundamental analysis | Estimates **intrinsic value** |
| Technical analysis | Studies **price and volume** |
| The clean split | Fundamental = **what** to buy; technical = **when** |
| Top-down | Economy → industry → company |
| Bottom-up | Company first |
| Sell-side research | Brokers/banks, **published** |
| Buy-side research | Funds/institutions, **internal** |
| E → I → C | Economy → Industry → Company |
| DCF | PV of future cash flows + terminal value |
| DCF's weakness | Extreme sensitivity to **g** and **r** |
| Terminal value | CF ÷ (r − g), needs **g < r** |
| P/E | Price ÷ EPS; **useless if earnings are negative** |
| P/B | Price ÷ book; best for **banks/financials** |
| P/S | For **loss-making** firms; ignores profitability |
| PEG | P/E ÷ growth; **< 1** often signals value |
| EV | Market cap + debt − cash |
| EV/EBITDA | **Capital-structure neutral** comparison |
| Earnings yield | EPS ÷ Price — the inverse of P/E |
| High dividend yield warning | May reflect a **falling price**, not generosity |
| EVA | NOPAT − (Capital × Cost of Capital); **positive = real value creation** |
| MVA | Market value − capital invested |
| Bank metrics | NIM, Gross/Net NPA, CASA, capital adequacy |
| Technical assumptions | Market discounts everything; prices trend; history repeats |
| RSI thresholds | **>70 overbought, <30 oversold** |
| Broken support | Often becomes **resistance** |
| Governance red flags | Auditor resignation, **promoter pledging**, related-party deals, profit–cash flow gap |

> **Exam tip:** for any valuation-ratio question, ask **"what is in the denominator, and can it be negative or distorted?"** That single question explains why P/E fails for loss-makers, why P/B suits banks, and why P/S is used for early-stage companies.
