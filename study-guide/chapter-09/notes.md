# Chapter 9: Investing in Fixed Income Securities — Short Notes

> **Module 3 · Investment Products (30 marks).**
> ⭐ The hardest maths in the paper sits here: **bond pricing, yield measures and duration**. Chapter 2's TVM formulas are the foundation — a bond is simply an annuity (the coupons) plus a lump sum (the redemption).

---

## 9.1 The Debt Market and Its Role

Debt lets **governments and corporates borrow** from many lenders at once.

| Borrower | Why they issue debt |
|---|---|
| **Government** | Fund the fiscal deficit, infrastructure, and manage liquidity |
| **Corporates** | Fund expansion without diluting ownership; interest is **tax-deductible**, unlike dividends |

**Why debt rather than equity, from the issuer's side:** no dilution of control, a **known** cost, and interest is deductible for tax. The cost is a **fixed obligation** that must be met regardless of profitability.

---

## 9.2 The Bond Market Ecosystem

| Participant | Role |
|---|---|
| **Issuers** | Government, PSUs, corporates, banks, NBFCs |
| **Investors** | Banks, insurers, pension funds, mutual funds, FPIs, retail |
| **Intermediaries** | Merchant bankers, brokers, primary dealers |
| **Credit rating agencies** | Assess default risk (CRISIL, ICRA, CARE, India Ratings) |
| **Debenture trustees** | Protect bondholders' interests; enforce security |
| **Regulators** | **RBI** — G-secs and money market; **SEBI** — corporate bonds and listing |

> ⚠️ **Split jurisdiction:** government securities and the money market sit with the **RBI**; **corporate bonds** and their listing sit with **SEBI**.

---

## 9.3 ⭐ Risks in Fixed Income

| Risk | What it is |
|---|---|
| **Interest rate risk** | Bond prices fall when rates rise. The **biggest** risk for a high-quality bond |
| **Call risk** | The issuer redeems early (when rates fall), forcing reinvestment at lower rates |
| **Reinvestment risk** | Coupons must be reinvested at whatever rate then prevails — a risk that **rates fall** |
| **Credit risk** | The issuer may not pay. Three sub-types: **downgrade risk** (rating cut), **spread/basis risk** (credit spreads widen), **default risk** (non-payment) |
| **Liquidity risk** | Cannot sell at a fair price; wide spreads, especially in corporate bonds |
| **Exchange rate risk** | For foreign-currency bonds, adverse currency movement |
| **Inflation (purchasing power) risk** | Fixed coupons buy less as prices rise |
| **Volatility risk** | Relevant to bonds with embedded options — higher volatility raises option value |
| **Political / legal risk** | Changes in law, tax or regulation affecting the bond |
| **Event risk** | A specific event — merger, restructuring, disaster — impairing the issuer |

> 🧠 **Interest rate risk and reinvestment risk pull in opposite directions.** If rates rise, your bond's *price* falls (bad) but you reinvest coupons at *higher* rates (good). This offsetting is exactly what **duration** captures — see 9.7.

---

## 9.4 ⭐ Bond Pricing

### 9.4.1 Par value
The **face value** repaid at maturity — typically ₹100 or ₹1,000 for corporate bonds and ₹100 for G-secs. **The coupon is always calculated on the face value, never on the market price.**

### 9.4.2 The pricing principle

**A bond's price is the present value of all its future cash flows**, discounted at the required yield:

$$\boxed{P = \sum_{t=1}^{n}\frac{C}{(1+y)^t} + \frac{F}{(1+y)^n}}$$

Equivalently, using the annuity formula from Chapter 2:

$$\boxed{P = C \times \frac{1-(1+y)^{-n}}{y} + \frac{F}{(1+y)^n}}$$

where **C** = coupon per period, **F** = face value, **y** = required yield per period, **n** = number of periods.

**Worked example:** a ₹1,000 face value bond, 8% annual coupon, 5 years to maturity, required yield 10%.
- Coupon = ₹80 a year; annuity factor = [1 − (1.10)⁻⁵] ÷ 0.10 = (1 − 0.62092) ÷ 0.10 = **3.7908**
- PV of coupons = 80 × 3.7908 = **₹303.26**
- PV of redemption = 1,000 ÷ (1.10)⁵ = 1,000 ÷ 1.61051 = **₹620.92**
- **Price = 303.26 + 620.92 = ₹924.18**

### 9.4.3 Pricing variants

| Bond type | Adjustment |
|---|---|
| **Annual coupon** | As above |
| **Semi-annual coupon** | **Halve the coupon and the yield; double the periods.** A 10% coupon, 6 years, 12% yield → C = 5% of face, y = 6%, n = 12 |
| **Zero-coupon bond** | No coupons: **P = F ÷ (1+y)ⁿ**. Always issued/trades at a **discount** |
| **Between coupon dates** | Price includes **accrued interest**. **Dirty price = clean price + accrued interest** |
| **Perpetual bond** | No maturity: **P = C ÷ y** — a perpetuity |

### 9.4.4 ⭐ The Price–Yield Relationship

$$\textbf{Price and yield move in OPPOSITE directions.}$$

| Condition | Bond trades at |
|---|---|
| **Coupon rate > required yield** | **Premium** (price > face value) |
| **Coupon rate = required yield** | **Par** (price = face value) |
| **Coupon rate < required yield** | **Discount** (price < face value) |

> 🧠 **The intuition:** if a bond pays 8% while the market demands 10%, nobody will pay full price for it. Its price must fall until the *total* return to a buyer equals 10%. In the example above, ₹924.18 is exactly the price at which an 8% coupon delivers a 10% yield.

**The relationship is convex, not a straight line** — prices rise more when yields fall than they fall when yields rise by the same amount. This is **convexity**, and it is favourable to the bondholder.

**Pricing matrix:** a grid of bond prices across different yields and maturities, used to value illiquid bonds by reference to comparable traded ones.

### 9.4.5 Perpetual bonds
No maturity date; the price is simply **C ÷ y**. In India these are often **AT-1 bonds** issued by banks — which carry **write-down risk** and are considerably riskier than ordinary bonds despite the steady coupon.

---

## 9.5 ⭐ Yield Measures

| Measure | Formula / meaning | Limitation |
|---|---|---|
| **Coupon rate** | Coupon ÷ **Face value** | Fixed; ignores the price you paid |
| **Current yield** | **Annual coupon ÷ Market price** | Ignores capital gain/loss at maturity and the timing of cash flows |
| **Yield to Maturity (YTM)** | The single discount rate that makes the PV of all cash flows equal the market price | Assumes **all coupons are reinvested at the YTM** and the bond is **held to maturity** |
| **Effective yield** | Yield adjusted for **compounding within the year** | — |
| **Yield to Call (YTC)** | YTM calculated to the **call date and call price** | Relevant only for callable bonds |
| **Yield to Put (YTP)** | YTM calculated to the **put date and put price** | Relevant only for puttable bonds |

### The relationships — a favourite exam question

| Bond trading at | Relationship |
|---|---|
| **Discount** | Coupon rate **<** Current yield **<** YTM |
| **Par** | Coupon rate **=** Current yield **=** YTM |
| **Premium** | Coupon rate **>** Current yield **>** YTM |

> 🧠 **Why:** a discount bond gives you a **capital gain** at maturity (you paid less than face value), which YTM counts but current yield ignores — so YTM is highest. A premium bond delivers a **capital loss** at maturity, so YTM is lowest.

**YTM's two big assumptions:** (1) every coupon is reinvested at the YTM itself — rarely true, which is **reinvestment risk**; and (2) the bond is held to maturity.

**Yield to Worst:** for a bond with multiple call dates, the lowest of all possible yields — the conservative measure.

---

## 9.6 The Yield Curve

The **yield curve** plots yield against maturity for bonds of the same credit quality (usually government securities).

| Shape | Appearance | Typical interpretation |
|---|---|---|
| **Normal (upward sloping)** | Long yields > short yields | Healthy expansion; investors demand a **term premium** for locking money away longer |
| **Flat** | Similar across maturities | Transition or uncertainty |
| **Inverted** | Short yields > long yields | Market expects **rate cuts / slowdown**; historically a recession signal |
| **Humped** | Peaks in the middle | Mixed expectations |

**Theories explaining the shape:**
- **Expectations theory** — long rates reflect expected future short rates.
- **Liquidity preference theory** — investors demand a premium for longer maturities, so the curve is normally upward sloping.
- **Market segmentation theory** — different investors have fixed maturity preferences (insurers want long, banks want short), so supply and demand at each segment set that segment's rate.

**Uses:** benchmark pricing for corporate bonds (which trade at a spread over the curve), signalling the economic outlook, and informing portfolio positioning.

---

## 9.7 ⭐ Duration

**Duration measures a bond's price sensitivity to interest rate changes** — and, equivalently, the weighted-average time to receive its cash flows.

### Macaulay duration
The weighted average time (in years) to receive the bond's cash flows, weighted by the present value of each.

### Modified duration
The practical measure:

$$\boxed{\text{Modified Duration} = \frac{\text{Macaulay Duration}}{1 + y}}$$

$$\boxed{\%\ \Delta P \approx -\text{Modified Duration} \times \Delta y}$$

**Example:** a bond with modified duration **6.2** when yields rise **0.75%** (75 basis points):
% change ≈ −6.2 × 0.0075 = **−4.65%**. A ₹10,00,000 holding loses about **₹46,500**.

### What drives duration

| Factor | Effect on duration |
|---|---|
| **Longer maturity** | **Higher** duration (more sensitive) |
| **Higher coupon** | **Lower** duration (more value arrives sooner) |
| **Higher yield** | Lower duration |
| **Zero-coupon bond** | Duration = **maturity exactly** (the only cash flow is at the end) |

> 🧠 **Two facts to memorise:**
> 1. **A zero-coupon bond's Macaulay duration equals its maturity** — the single most-tested duration fact.
> 2. **Longer duration = more interest rate risk.** If you expect rates to **fall**, go **long** duration; if you expect rates to **rise**, go **short** duration.

**Convexity** is the second-order effect — the curvature of the price–yield relationship. Duration alone underestimates the price rise when yields fall and overestimates the fall when yields rise; convexity corrects for this, and **positive convexity benefits the bondholder**.

---

## 9.8 The Money Market

Short-term debt: **maturity up to one year**, regulated by the **RBI**.

### 9.8.1 Participants
**Demand side:** banks (managing reserves), corporates (short-term funding). **Supply side:** banks with surplus, mutual funds (liquid schemes), insurers, the RBI. **Intermediaries:** primary dealers, brokers.

### 9.8.2 Instruments

| Instrument | Issuer | Tenor | Notes |
|---|---|---|---|
| **Treasury bills (T-bills)** | Government of India | **91, 182, 364 days** | **Zero-coupon**, issued at a discount, redeemed at face value. Risk-free |
| **Cash Management Bills** | Government | Under 91 days | For temporary cash mismatches |
| **Certificates of Deposit (CDs)** | Banks and select FIs | 7 days–1 year | Negotiable term deposits |
| **Commercial Paper (CP)** | Corporates, PDs, FIs | 7 days–1 year | **Unsecured** promissory note; needs a credit rating |
| **Call money** | Banks | **Overnight** | Inter-bank; rate is the "call rate" |
| **Notice money** | Banks | 2–14 days | — |
| **Term money** | Banks | 15 days–1 year | — |
| **Repo / Reverse repo** | Banks, RBI | Short | Sale with an agreement to repurchase — effectively collateralised borrowing |
| **TREPS / CBLO** | Market participants | Short | Tri-party repo, centrally cleared |

> 🧠 **Repo vs reverse repo, from the RBI's perspective:** in a **repo**, banks borrow from the RBI against securities (the **repo rate**). In a **reverse repo**, banks lend to the RBI (the **reverse repo rate**). The repo rate is the RBI's main policy rate.

---

## 9.9 The Government Debt Market

**Participants:** the **RBI** (as the government's debt manager and banker), **primary dealers** (obliged to bid at auctions), banks (holding G-secs for SLR), insurers, pension funds, mutual funds, FPIs and retail (via **RBI Retail Direct**).

### Instruments

| Instrument | Notes |
|---|---|
| **Dated G-secs** | Fixed-coupon bonds, typically 5–40 years; **coupon paid half-yearly** |
| **Treasury bills** | 91/182/364 days, zero-coupon |
| **State Development Loans (SDLs)** | Issued by state governments; slightly higher yield than central G-secs |
| **Floating Rate Bonds** | Coupon resets against a benchmark |
| **Inflation Indexed Bonds** | Principal or coupon linked to an inflation index |
| **Sovereign Gold Bonds** | Gold-linked, with an additional fixed interest rate |
| **Savings (Taxable) Bonds** | Retail-oriented government savings instruments |
| **STRIPS** | Coupons and principal separated and traded as individual zero-coupon securities |

G-secs are sold through **RBI auctions** and carry **no credit risk** in domestic currency.

---

## 9.10 The Corporate Debt Market

**Participants:** issuers (corporates, NBFCs, banks), investors (mutual funds, insurers, pension funds, FPIs, HNIs), and intermediaries (merchant bankers, arrangers, rating agencies, **debenture trustees**).

### Instruments

| Instrument | Notes |
|---|---|
| **Company/corporate deposits** | Unsecured deposits with a company; **not DICGC-insured** — credit risk sits with the company |
| **Bonds and debentures** | Secured or unsecured; convertible or non-convertible (NCDs) |
| **Infrastructure bonds** | Issued to fund infrastructure |
| **Inflation-indexed bonds** | Return linked to inflation |
| **Perpetual/AT-1 bonds** | No maturity; bank capital instruments with **write-down risk** |
| **Masala bonds** | **Rupee-denominated** bonds issued **outside India** — the issuer bears no currency risk; the investor does |

**Debentures may be:** secured/unsecured, convertible (fully or partly) / non-convertible, redeemable/perpetual.

---

## 9.11 Small Savings and Bank Deposits

### Bank deposits
- **Savings, current, fixed (FD) and recurring (RD)** deposits.
- **Interest rates on FDs** are set by each bank and vary with tenor; senior citizens typically receive an additional 0.25–0.75%.
- **DICGC insurance covers up to ₹5 lakh** per depositor per bank (principal + interest), across all branches.
- Premature withdrawal usually carries a penalty.

### Floating Rate Savings Bonds, 2020 (Taxable)
- Issued by the Government of India; **7-year** tenor.
- Interest **resets half-yearly**, pegged at **NSC rate + 0.35%**.
- Interest is **fully taxable**; not tradable.

### ⭐ Small savings schemes — the comparison table

| Scheme | Tenor | Key features | Tax |
|---|---|---|---|
| **PPF** | **15 years** (extendable in 5-year blocks) | Min ₹500, **max ₹1.5 lakh a year**; loan and partial withdrawal facilities | **EEE** — exempt at all three stages |
| **Senior Citizens' Savings Scheme (SCSS)** | **5 years** (+3 extension) | Age **60+** (or 55+ on superannuation); **max ₹30 lakh**; **quarterly** interest | Interest **taxable**; 80C on deposit |
| **National Savings Certificate (NSC)** | **5 years** | Interest **compounded annually but payable at maturity**; reinvested interest also qualifies for 80C | Interest taxable |
| **Kisan Vikas Patra (KVP)** | Until the amount **doubles** (period set by the prevailing rate) | No maximum limit; **no 80C benefit** | Interest taxable |
| **Sukanya Samriddhi Account (SSA)** | Until the girl turns 21 | For a **girl child under 10**; deposits for 15 years; **max ₹1.5 lakh a year** | **EEE** |
| **Post Office MIS** | 5 years | **Monthly** interest payout | Interest taxable |
| **Post Office Time/Recurring Deposits** | 1–5 years | Similar to bank deposits | Taxable |

> ⚠️ **Most-tested facts:** **PPF and SSA are EEE.** **PPF is 15 years with a ₹1.5 lakh annual cap.** **SCSS is for 60+, capped at ₹30 lakh, paying quarterly.** **KVP doubles your money and gets NO 80C benefit.**

---

## ⚡ Quick Revision Sheet

| Concept | The one-line answer |
|---|---|
| Bond price | **PV of all future cash flows** at the required yield |
| Bond price formula | C × [(1 − (1+y)⁻ⁿ) ÷ y] + F ÷ (1+y)ⁿ |
| Semi-annual bonds | **Halve** C and y, **double** n |
| Zero-coupon bond | P = F ÷ (1+y)ⁿ; always at a discount |
| Perpetual bond | P = C ÷ y |
| Dirty price | Clean price **+ accrued interest** |
| Price and yield | Move **inversely**; the curve is **convex** |
| Coupon > yield | Trades at a **premium** |
| Coupon < yield | Trades at a **discount** |
| Current yield | Coupon ÷ **market price** |
| YTM | The rate equating PV of cash flows to price |
| YTM's assumptions | Coupons reinvested **at the YTM**; held to maturity |
| Discount bond ordering | Coupon < Current yield < **YTM** |
| Premium bond ordering | Coupon > Current yield > **YTM** |
| Modified duration | Macaulay ÷ (1 + y) |
| Price change | ≈ **−Modified duration × Δy** |
| Zero-coupon duration | **= its maturity** |
| Higher coupon | **Lower** duration |
| Longer maturity | **Higher** duration |
| Expect rates to fall | Go **long** duration |
| Convexity | Second-order effect; **benefits the bondholder** |
| Normal yield curve | Upward sloping — term premium |
| Inverted curve | Short > long; signals expected **rate cuts / slowdown** |
| T-bill tenors | **91, 182, 364 days**; zero-coupon |
| Commercial paper | **Unsecured** corporate short-term note; needs a rating |
| Call money | **Overnight** inter-bank |
| Repo rate | Rate at which **banks borrow from the RBI** |
| G-sec coupon frequency | **Half-yearly** |
| DICGC cover | **₹5 lakh** per depositor per bank |
| PPF | **15 years**, ₹1.5 lakh cap, **EEE** |
| SCSS | Age **60+**, ₹30 lakh cap, **quarterly** interest |
| NSC | 5 years; interest compounded but paid at maturity |
| KVP | Doubles the money; **no 80C** |
| SSA | Girl under 10; **EEE**; ₹1.5 lakh cap |
| Floating Rate Savings Bond | 7 years; **NSC + 0.35%**, reset half-yearly; taxable |
| Masala bond | **Rupee-denominated**, issued **outside India** |
| Regulator split | **RBI** — G-secs & money market; **SEBI** — corporate bonds |

> **Exam tip:** almost every bond question reduces to one of three tasks — **price it** (discount the cash flows), **compare coupon with yield** (premium/par/discount), or **apply duration** (% price change ≈ −MD × Δy). Identify which one is being asked before computing.
