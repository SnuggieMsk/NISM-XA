# Chapter 2: Time Value of Money — Short Notes

> **Module 1 · Personal Financial Planning (37 marks).**
> ⭐ **This is the single most important chapter in the syllabus.** Its formulas reappear in Chapter 4 (EMIs), Chapter 9 (bond pricing), Chapter 14 (expected returns), Chapter 16 (CAGR, annualising) and in almost every caselet. Master this and you have effectively pre-answered a large slice of the paper.

---

## 2.1 The Core Idea

**A rupee today is worth more than a rupee tomorrow.**

Three reasons:

1. **Opportunity cost** — money in hand can be invested and earn a return.
2. **Inflation** — future rupees buy less.
3. **Risk/uncertainty** — a promised future rupee might never arrive.

Because of this, you can never simply add or compare cash flows that occur at different dates. You must first move them all to a **common point in time**.

> 🧠 **The one mental model:** think of a **time line**. Money moved *forward* in time is **compounded** (multiplied by (1+r)ⁿ). Money moved *backward* is **discounted** (divided by (1+r)ⁿ). That's the entire chapter.

```
        discount ←────────────────────── compound
   |--------|--------|--------|--------|--------|
   0        1        2        3        4        5   (periods)
   PV                                            FV
```

---

## 2.2 The Five Variables

Every TVM problem has **five** variables. Give me any four and I can solve for the fifth.

| Symbol | Name | Meaning |
|---|---|---|
| **PV** | Present Value | Value today |
| **FV** | Future Value | Value at a future date |
| **r** (or `RATE`) | Rate per period | Interest/return **per period** |
| **n** (or `NPER`) | Number of periods | Total compounding periods |
| **PMT** | Payment | The equal cash flow each period |

> ⚠️ **The #1 exam error:** mixing an *annual* rate with a *monthly* number of periods. **r and n must always use the same period.** For monthly problems: `r = annual rate ÷ 12` and `n = years × 12`.

### Sign convention (matters in Excel)
Money you **pay out** is **negative**; money you **receive** is **positive**. If a spreadsheet returns `#NUM!`, it is almost always because every value was entered with the same sign.

---

## 2.2.1 & 2.2.2 Future Value and Present Value

### Future Value of a lump sum

$$\boxed{FV = PV \times (1 + r)^n}$$

**Example:** ₹1,00,000 invested for 10 years at 9%.
FV = 1,00,000 × (1.09)¹⁰ = 1,00,000 × 2.3674 = **₹2,36,740**.

### Present Value of a lump sum

$$\boxed{PV = \frac{FV}{(1 + r)^n}}$$

**Example:** how much do I need today to have ₹50,00,000 in 15 years at 10%?
PV = 50,00,000 ÷ (1.10)¹⁵ = 50,00,000 ÷ 4.1772 = **₹11,96,970**.

> These two are the **same equation rearranged**. Learn one and you know both.

### Simple vs compound interest

| | Simple interest | Compound interest |
|---|---|---|
| **Interest earned on** | Principal only | Principal **+ accumulated interest** |
| **Formula** | FV = PV × (1 + r×n) | FV = PV × (1+r)ⁿ |
| **Growth shape** | Straight line | Accelerating curve |

**₹1,00,000 at 10% for 20 years:** simple → ₹3,00,000; compound → **₹6,72,750**. The gap *is* the value of compounding.

---

## 2.2.3 Rate of Return

Rearranging FV = PV(1+r)ⁿ:

$$\boxed{r = \left(\frac{FV}{PV}\right)^{1/n} - 1}$$

This is the **CAGR** (Compound Annual Growth Rate) — the single smoothed annual rate that takes PV to FV.

**Example:** ₹4,00,000 grows to ₹10,00,000 in 8 years.
r = (10,00,000 ÷ 4,00,000)^(1/8) − 1 = (2.5)^0.125 − 1 = 1.1214 − 1 = **12.14% p.a.**

> Excel: `=RATE(8,0,-400000,1000000)`.

---

## 2.2.5 Number of Periods

$$\boxed{n = \frac{\ln(FV / PV)}{\ln(1 + r)}}$$

**Example:** how long for ₹5,00,000 to become ₹15,00,000 at 11%?
n = ln(3) ÷ ln(1.11) = 1.0986 ÷ 0.10436 = **10.53 years**.

### 🔑 The Rule of 72 (memorise this)

$$\textbf{Years to double} \approx \frac{72}{\text{annual rate (\%)}}$$

| Rate | Doubling time |
|---|---|
| 6% | 12 years |
| 8% | 9 years |
| 9% | 8 years |
| 12% | 6 years |

Use it in reverse too: if money doubled in 6 years, the rate was ≈ 72 ÷ 6 = **12%**. It's an approximation, but exam-fast and usually within a few months.

---

## 2.3 Compounding Frequency

Interest may be credited more than once a year. More frequent compounding = **more interest**, because interest starts earning interest sooner.

$$\boxed{FV = PV \times \left(1 + \frac{r}{m}\right)^{m \times n}}$$

where **m** = compoundings per year (annual 1, half-yearly 2, quarterly 4, monthly 12, daily 365).

### Effective Annual Rate (EAR)

The rate that, compounded **once a year**, gives the same result:

$$\boxed{EAR = \left(1 + \frac{r}{m}\right)^{m} - 1}$$

**₹1,00,000 at a nominal 12% for 1 year:**

| Frequency | m | EAR | Value after 1 year |
|---|---|---|---|
| Annual | 1 | 12.000% | ₹1,12,000 |
| Half-yearly | 2 | 12.360% | ₹1,12,360 |
| Quarterly | 4 | 12.551% | ₹1,12,551 |
| Monthly | 12 | 12.683% | ₹1,12,683 |
| Daily | 365 | 12.747% | ₹1,12,747 |

> ⚠️ **Exam trap:** the **nominal** (stated) rate is the same 12% throughout — only the **effective** rate changes. Always compare products on **EAR**, never on the headline rate.
>
> Note the gains shrink as m rises: annual→monthly adds 0.68 percentage points; monthly→daily adds only 0.06. The limit (continuous compounding) is e^r − 1 = 12.75%.

---

## 2.2.6 Annuities

An **annuity** is a series of **equal** cash flows at **regular** intervals — a SIP, an EMI, a pension, rent.

### Ordinary annuity (payment at the END of each period)

This is the default. Most EMIs and SIPs are treated this way.

$$\boxed{FV_{\text{ordinary}} = PMT \times \frac{(1+r)^n - 1}{r}}$$

$$\boxed{PV_{\text{ordinary}} = PMT \times \frac{1 - (1+r)^{-n}}{r}}$$

**Example (FV):** ₹10,000 a month for 15 years at 12% p.a. compounded monthly.
r = 0.12 ÷ 12 = **0.01**; n = 15 × 12 = **180**.
(1.01)¹⁸⁰ = **5.9958**.
FV = 10,000 × [(5.9958 − 1) ÷ 0.01] = 10,000 × **499.58** = **₹49,95,800**.

*(Total invested = ₹18,00,000. Returns contributed ₹31,95,800 — nearly two-thirds of the corpus.)*

### Annuity due (payment at the BEGINNING of each period)

Each payment sits invested for **one extra period**, so simply multiply by (1+r):

$$\boxed{FV_{\text{due}} = FV_{\text{ordinary}} \times (1 + r)}$$
$$\boxed{PV_{\text{due}} = PV_{\text{ordinary}} \times (1 + r)}$$

Using the example above: FV_due = 49,95,800 × 1.01 = **₹50,45,758** — about ₹50,000 more, purely from timing.

> 🧠 **Memory hook:** "**Due** means you pay **first**" → money works longer → the value is **always higher**. In Excel this is the `type` argument: **0 = ordinary (end)**, **1 = due (beginning)**.

### 2.2.4 Solving for PMT

Rearranging the FV annuity formula:

$$\boxed{PMT = \frac{FV \times r}{(1+r)^n - 1}}$$

**Example:** to accumulate ₹1,00,00,000 in 20 years at 11% p.a. (monthly):
r = 0.0091667, n = 240, (1.0091667)²⁴⁰ = **8.9006**.
PMT = (1,00,00,000 × 0.0091667) ÷ (8.9006 − 1) = 91,667 ÷ 7.9006 = **₹11,602 a month**.

And from the **PV** side (this is the **EMI** formula — see Chapter 4):

$$\boxed{PMT = \frac{PV \times r}{1 - (1+r)^{-n}} = PV \times \frac{r(1+r)^n}{(1+r)^n - 1}}$$

---

## 2.2.7 Perpetuity

A perpetuity is an annuity that **never ends**.

$$\boxed{PV_{\text{perpetuity}} = \frac{PMT}{r}}$$

**Example:** ₹60,000 a year forever, discount rate 8% → PV = 60,000 ÷ 0.08 = **₹7,50,000**.

### Growing perpetuity

If the payment grows at a constant rate **g** (and g < r):

$$\boxed{PV = \frac{PMT_1}{r - g}}$$

**Example:** ₹60,000 next year growing 4% a year forever, discounted at 8%:
PV = 60,000 ÷ (0.08 − 0.04) = **₹15,00,000**.

> ⚠️ If **g ≥ r** the formula breaks (the value is infinite) — a favourite trick question.

### Growing annuity (finite)

$$PV = \frac{PMT_1}{r-g}\left[1 - \left(\frac{1+g}{1+r}\right)^n\right]$$

Useful for retirement income that must rise with inflation.

---

## 2.4 Real vs Nominal Return

The **nominal** return is what the statement shows. The **real** return is what your money will actually buy.

$$\boxed{\text{Real return} = \frac{1 + \text{nominal}}{1 + \text{inflation}} - 1}$$

**Example:** nominal 9%, inflation 6%.
Real = (1.09 ÷ 1.06) − 1 = 1.02830 − 1 = **2.83%**.

> ⚠️ The rough answer (9 − 6 = 3%) **overstates** it. The exam frequently offers the crude subtraction as a distractor — use the exact formula.

**Why it matters:** an FD at 7% with inflation at 6% delivers a real return of only (1.07 ÷ 1.06) − 1 = **0.94%**. Before tax. After 30% tax the nominal becomes 4.9%, and the real return is (1.049 ÷ 1.06) − 1 = **−1.04%** — the "safe" investment is quietly *losing* purchasing power.

### Inflating a goal

$$\text{Future cost} = \text{Today's cost} \times (1 + \text{inflation})^n$$

Always cost goals in **future rupees** before computing what to invest.

---

## 2.5 Putting It Together — the standard goal calculation

Every goal caselet follows the same four steps:

1. **Inflate the goal** to its future cost: `Cost × (1 + i)ⁿ`
2. **Grow what you already have**: `Existing × (1 + r)ⁿ`
3. **Find the gap**: step 1 − step 2
4. **Solve for the SIP** that fills the gap: `PMT = Gap × r ÷ [(1+r)ⁿ − 1]`

**Worked example.** Goal: education costing ₹20,00,000 today, needed in 10 years. Inflation 7%. Existing earmarked corpus ₹5,00,000. Expected return 11% p.a. (monthly compounding).

1. Future cost = 20,00,000 × (1.07)¹⁰ = 20,00,000 × 1.9672 = **₹39,34,400**
2. Existing grows = 5,00,000 × (1.11)¹⁰ = 5,00,000 × 2.8394 = **₹14,19,700**
3. Gap = 39,34,400 − 14,19,700 = **₹25,14,700**
4. r = 0.0091667, n = 120, (1.0091667)¹²⁰ = 2.9853
 PMT = (25,14,700 × 0.0091667) ÷ 1.9853 = 23,051 ÷ 1.9853 = **₹11,611 a month**

---

## 📊 Excel / Calc Functions (the test machine has a spreadsheet!)

| Need | Function |
|---|---|
| Future value | `=FV(rate, nper, pmt, [pv], [type])` |
| Present value | `=PV(rate, nper, pmt, [fv], [type])` |
| Payment | `=PMT(rate, nper, pv, [fv], [type])` |
| Rate | `=RATE(nper, pmt, pv, [fv], [type])` |
| Periods | `=NPER(rate, pmt, pv, [fv], [type])` |
| Effective rate | `=EFFECT(nominal_rate, npery)` |
| Nominal rate | `=NOMINAL(effect_rate, npery)` |

**Rules:** use the **per-period** rate; enter outflows as **negative**; `type` = 0 (end) or 1 (beginning).

---

## ⚡ Quick Revision Sheet

| Need | Formula |
|---|---|
| FV of lump sum | PV × (1+r)ⁿ |
| PV of lump sum | FV ÷ (1+r)ⁿ |
| Rate / CAGR | (FV ÷ PV)^(1/n) − 1 |
| Periods | ln(FV÷PV) ÷ ln(1+r) |
| Rule of 72 | Years to double ≈ 72 ÷ rate% |
| Non-annual compounding | PV × (1 + r/m)^(m×n) |
| Effective annual rate | (1 + r/m)^m − 1 |
| FV of ordinary annuity | PMT × [((1+r)ⁿ − 1) ÷ r] |
| PV of ordinary annuity | PMT × [(1 − (1+r)⁻ⁿ) ÷ r] |
| Annuity **due** | Ordinary × (1+r) |
| PMT from FV | FV × r ÷ [(1+r)ⁿ − 1] |
| PMT from PV (EMI) | PV × r × (1+r)ⁿ ÷ [(1+r)ⁿ − 1] |
| Perpetuity | PMT ÷ r |
| Growing perpetuity | PMT₁ ÷ (r − g), needs g < r |
| Real return | [(1+nominal) ÷ (1+inflation)] − 1 |
| Future cost of a goal | Cost × (1 + inflation)ⁿ |

### The five traps that cost marks

1. **Period mismatch** — annual rate with monthly periods. Convert *both*.
2. **Ordinary vs due** — "beginning of month" means multiply by (1+r).
3. **Real return by subtraction** — use the division formula.
4. **Forgetting to inflate the goal** — today's cost is never the target.
5. **Nominal vs effective** — compare products on EAR.

> **Exam tip:** Module 1 is 37 marks and this chapter underpins most of it. If you have limited revision time, spend it here.
