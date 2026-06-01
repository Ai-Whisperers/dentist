# Payment Infrastructure Research — Dra. Gabriella González Pane
## Paraguay Dental Practice Payment Systems

**Date:** June 2026  
**Context:** Strategic reposicionamiento from volume-based (insurance) to value-based private-pay model  
**Focus:** Pagopar, Bancard, installment capabilities, integration requirements

---

## 1. Pagopar — Merchant Overview

### What is Pagopar?

Pagopar is Paraguay's dominant online payment platform, now integrated into **Upay** (ueno bank). It provides a unified gateway accepting:

- **Cards:** Visa, Mastercard, Maestro, Credicard, Única débito, Union Pay, Elo, JCB, American Express, Discover, Diners Club, Credifielco, Cabal (local brands)
- **QR payments** and **billetera electrónica** (mobile wallets)
- **PIX** (Brazilian instant payment system)
- **Cash payments** via 3,000+ physical agency collection points (bocas de cobranza)
- **Bank transfers**

### Products Available

| Product | Use Case |
|---|---|
| **Pagopar Checkout** | E-commerce integration (API) |
| **Link de Pago** | Shareable payment link (WhatsApp, email, SMS) — ideal for consultorios |
| **Suscripciones** | Recurring debits (monthly treatment plans) |
| **CelPOS** | Turn your phone into a POS — no hardware needed |
| **POS hardware** | Physical terminal for in-person |

### How Link de Pago Works (Best Fit for Dental Consultorio)

1. Dentist generates a payment link from the Pagopar dashboard (or via API)
2. Link is shared to patient via WhatsApp, SMS, or email
3. Patient opens link, selects payment method (card, QR, cash at agency)
4. Payment confirmation is immediate; funds settle to merchant account
5. Dentist receives notification and records payment

**For a dental practice**, this means: no integrated e-commerce needed; simply generate links per procedure/treatment plan and send to patients.

### Fees (Pagopar)

> **Note:** Exact fee schedules require direct merchant application. Public sources indicate:

- **Card processing:** approximately **3.5–4.5% per transaction** depending on card type and plan tier
- **Cash at agency:** typically lower (~$10-15 PYG per transaction flat)
- **Settlement:** generally **T+1 to T+2** (next business day to two days)
- **No setup fee** for basic link/payment tools

### CelPOS — No Hardware Cost

Pagopar's **CelPOS** is a critical feature for a consultorio:
- Uses your existing Android/iOS phone as a POS
- Accepts contactless (NFC), QR, card tap
- No terminal rental cost
- Works for in-person visits where the patient is present

---

## 2. Payment Plans / Installments (Cuotas)

### Up to 12 Cuotas Sin Intereses

Pagopar partners with specific banks to offer **installment plans with 0 interest**:

| Bank | Max Cuotas |
|---|---|
| **Banco Familiar** | 12 cuotas sin interés |
| **Vision Banco** | 12 cuotas sin interés |
| **ueno bank** (via Upay) | 12 cuotas sin interés |

### How It Works for the Merchant

- The **merchant must be registered** in the Pagopar promo program to offer cuotas sin intereses
- The **interest/financing cost is absorbed by the bank**, not the merchant — under promotion terms
- The merchant receives the **full nominal amount** (no discount on principal)
- Not automatic — the customer must explicitly select the "cuotas" option at checkout

### For High-Value Dental Procedures (Gs 400k+)

A dental procedure of Gs 400,000 (~$50 USD) at 12 cuotas sin interés:
- Monthly payment: ~Gs 33,333 (~$4 USD/month)
- **No interest charged** to the patient
- Merchant receives full Gs 400k (minus standard processing fee ~3.5-4.5%)
- The bank subsidizes the "no interest" portion as a marketing cost

### Implementation for Treatment Plans

For a dental practice offering **ortho packages, implants, rehabilitation plans**:
1. Generate a payment link per treatment plan (e.g., Gs 3,200,000 for full rehabilitation)
2. Patient selects 12-cuota payment method
3. Pagopar processes the first installment immediately
4. Remaining 11 installments are charged to the card on a recurring basis (using Suscripciones)
5. Merchant sees full amount minus processing fee

---

## 3. Bancard — Alternative Analysis

### What is Bancard?

Bancard is Paraguay's dominant **card-acquiring network** (similar to First Data in the US). It provides:
- Physical POS terminals
- POS Android app (mobile POS)
- QR payments
- The largest merchant network in Paraguay

### Bancard Products

| Product | Description |
|---|---|
| **POS Terminal** | Hardware device; various models with printer, contactless |
| **POS Móvil App** | Mobile app turning phone into POS |
| **Bancard Pago Móvil** | Consumer-facing QR/payment app |
| **Portal de Comercios** | Merchant dashboard for sales tracking |

### Fees (Bancard)

> **Public information is limited** — requires direct inquiry. General market indicators:

- **Standard merchant fee:** approximately **3.5–4.0% per transaction**
- **Settlement:** typically **T+1** (next business day)
- **POS rental:** varies by terminal model; some promotions offer free rental with minimum volume
- **Setup:** requires merchant agreement, RUC, tax documentation

### Comparison: Bancard vs Pagopar for Dental Practice

| Factor | Pagopar / Upay | Bancard |
|---|---|---|
| **Setup complexity** | Low (online registration) | Medium (contract, documentation) |
| **Hardware required** | No (CelPOS uses phone) | POS terminal optional |
| **Online payments** | Full support (links, checkout) | Limited (QR only) |
| **In-person payments** | Yes (CelPOS NFC/QR) | Yes (POS terminal + app) |
| **Installments (cuotas)** | Up to 12 sin interés (bank promo) | Up to 12 (bank-deal dependent) |
| **Cash at agency** | Yes (3k+ bocas) | No |
| **Settlement speed** | T+1 to T+2 | T+1 |
| **Monthly fee** | Tiered plans (free tier available) | POS rental + per-transaction |
| **Best for** | Online-heavy, payment links, cuotas promotions | High-volume in-person card |
| **API / integrations** | Yes (Pagopar API) | Yes (Bancard API) |

### Recommendation for Dra. González

**Use both, but start with Pagopar** because:
1. CelPOS covers in-person card payments with zero hardware cost
2. Link de Pago enables WhatsApp payment requests (no website needed)
3. Cuotas sin intereses promotions through specific banks can be activated
4. Cash payment at agencies captures patients without bank access
5. Lower barrier to entry (online registration vs. terminal contract)

**Add Bancard** if:
- Patient volume requires physical POS with printer receipt
- Insurance reimbursements flow through card networks
- High-volume in-person transactions

---

## 4. Integration Requirements

### Pagopar Merchant Registration

Requirements for a dental consultorio to sign up:

1. **RUC** (Registro Único del Contribuyente) — Paraguayan tax ID
2. **Timbrado** — active invoice series authorization from SET
3. **Bank account** in Paraguay (for settlements)
4. **Business registration** (S.A., S.R.L., or similar legal entity)
5. **Contact details** and business profile in the Pagopar merchant portal

### Sign-up Process

1. Go to [pagopar.com/registro](https://www.pagopar.com/registro)
2. Select plan tier (has free tier for small merchants)
3. Submit RUC + business documentation
4. Receive merchant credentials (API key for integrations)
5. Configure payment methods and settlement account

### Is POS Terminal Required?

**No.** Pagopar's **CelPOS** is phone-based and free. Physical POS terminals (Bancard-style) are optional for high-volume practices.

### For a Dental-Specific Integration

- **Link de Pago** is the simplest: no coding, dashboard-generated
- **API integration** (Pagopar Checkout) for a future website with embedded payments
- Payment links can be **sent via WhatsApp** — no app required on patient side

---

## 5. Real-World Use — Dental Clinics in Paraguay

### Observed Patterns

From search results:
- **OdontosPY** (dental clinic Asunción) — advertises multiple payment methods including card (likely Bancard and/or Pagopar)
- Dental clinics in Paraguay typically advertise: Efectivo, Tarjeta de Crédito/Débito, Transferencia bancaria
- Promotional campaigns reference "cuotas sin interés" during holiday periods

### Market Reality

- **Cash remains dominant** in Paraguay for healthcare — especially for upper-middle-class patients who prefer not to finance
- **Card adoption is growing** among younger patients and expats/foreign patients
- **Cuotas sin interés** is a competitive differentiator — if Dra. González offers 12 cuotas and competitors don't, patients will choose her practice for high-value procedures
- Insurance patients typically pay via **insurance card (cobertura)** with direct billing — different flow from private pay

---

## 6. Financial Model Implications

### Private Pay Model with Pagopar

For a high-value procedure (e.g., full oral rehabilitation, Gs 8,000,000 = ~$1,000 USD):

| Scenario | Without Pagopar | With Pagopar Cuotas |
|---|---|---|
| Patient pays upfront | Gs 8,000,000 | — |
| Patient pays in 12 cuotas | N/A (patient can't or won't) | Gs 666,667/month |
| Merchant receives (after 4% fee) | Gs 7,680,000 | Gs 7,680,000 (minus same fee) |
| Patient cost | Full amount | Same after fees, no interest |
| Conversion rate | Lower for high-ticket | Higher — affordability unlocked |

### Cash Flow Consideration

- Pagopar settles to merchant account in T+1 to T+2
- For installment collections (Suscripciones), each monthly installment settles separately
- Dental practice needs to track installment payments per patient — recommend separate record system

---

## 7. Summary — Actionable Recommendations for Dra. González

### Immediate (Month 1)

1. **Register as Pagopar merchant** at pagopar.com/registro (use a consultant or staff member to handle documentation — RUC + Timbrado required)
2. **Activate CelPOS** on the practice phone — accept in-person card payments immediately, zero hardware cost
3. **Start using Link de Pago** for treatment plans: generate a link, send via WhatsApp to patients
4. **Apply for cuotas sin interés promotion** with Banco Familiar and/or Vision Banco (requires being an enrolled Pagopar merchant)

### Short-term (Month 2-3)

5. **Explore Pagopar Checkout API** if a simple patient portal or website is built later
6. **Consider adding Bancard POS** if volume of in-person card transactions grows significantly (terminal with receipt printer)
7. **Document payment options** clearly on patient communication: cash, card (with contactless), link de pago, cuotas

### High-Value Procedure Strategy

For cases exceeding Gs 2,000,000 (~$250 USD):
- Offer the **12-cuota sin interés** option explicitly
- Calculate monthly payment and include in treatment plan documentation
- Use Pagopar Link de Pago per procedure, not per visit

---

## Appendix: Key Links

| Resource | URL |
|---|---|
| Pagopar Registration | https://www.pagopar.com/registro |
| Pagopar Plans | https://www.pagopar.com/planes |
| Pagopar CelPOS | https://www.pagopar.com/celpos |
| Pagopar Link de Pago | https://www.pagopar.com/link-pago |
| Upay/Pagopar Integration | https://upay.com.py/pagopar/ |
| Bancard POS Info | https://www.bancard.com.py/pos |
| Bancard Soporte | https://www.bancard.com.py/soporte |

---

*Research compiled June 2026. Fee structures and promo terms subject to change — verify current rates directly with Pagopar/Bancard before merchant registration.*