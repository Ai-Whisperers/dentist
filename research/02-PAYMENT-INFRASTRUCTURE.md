# RESEARCH: PAYMENT INFRASTRUCTURE — PARAGUAY

**Last updated**: Mayo 31, 2026
**Sources**: Web search, Pagopar/Bancard public documentation

---

## 1. PAGOPAR — OVERVIEW

### What is Pagopar:
- Leading local payment platform in Paraguay
- Established player with strong local presence
- Offers multiple payment methods

### Payment Methods Supported (from Wix integration docs):
- Debit/credit card (Visa, Mastercard, American Express, etc.)
- QR payments
- WEPA
- Aquí Pago
- Pago Express
- Tigo Money
- Personal Pay
- Personal
- Giros Claro
- Zimple
- Wally
- PIX
- Bank transfers

### For Dental Practice Use:
- Can handle recurring payments (payment plans)
-woocommerce plugin available
- Works with small businesses

---

## 2. PAGOPAR FEES & COSTS

### What we found:
- Transaction fees exist but specific rates not publicly disclosed
- Requires merchant registration
- Settlement timeline: typically within days

### Key consideration for dental:
- For high-value procedures (Gs 400k-2M+), payment plans are critical
- Pagopar allows installment plans which enables:
  - Gs 2M procedure → 4x Gs 500k payments
  - Makes expensive treatments accessible to patients

### From Reddit discussion:
"Pagopar es la única pasarela de pago disponible" (Paraguay-specific)

---

## 3. BANCARD — OVERVIEW

### What is Bancard:
- Dominant card network in Paraguay
- 100,000+ merchants
- 40+ years of experience
- Strong POS terminal infrastructure

### Services:
- POS terminals (físicos)
- Online payments via API
- QR payments (dominant in Paraguay — 55% of contactless payments)
- App for merchants

### Key advantage:
- If patients have cards, Bancard terminal can accept payments immediately
- Most common for in-person payments

---

## 4. FEES COMPARISON

### From research (not complete, needs direct confirmation):

| Provider | Debit fees | Credit fees | Settlement |
|---|---|---|---|
| Pagopar | ~2-3%? | ~3-5%? | 2-5 days |
| Bancard | ~1.5-2%? | ~3-4%? | Same day? |

**NOTE**: These are estimates — need direct confirmation from providers.

### For Gs 550k restoration:
- If fee is 3%, merchant receives Gs 533.500
- If fee is 5%, merchant receives Gs 522.500
- Accepting cards still makes sense for high-value services

---

## 5. PAYMENT PLANS — CRITICAL FOR DENTAL

### Why payment plans matter:

From audio, patient couldn't pay Gs 2M+ upfront for complex procedures. Payment plans enable:
- Patient gets treatment now
- Dentist gets paid in full
- Small monthly payments become manageable

### How Pagopar handles installments:
- Can set up recurring payments
- 6, 12+ installments possible
- Interest rate depends on plan structure

### Recommendation:
- Offer 6-month interest-free payment plan for Gs 600k+
- Offer 12-month plan for Gs 1.2M+
- Partner with Pagopar for automatic collection

---

## 6. IMPLEMENTATION FOR DRA.'S PRACTICE

### Steps needed:

1. **Register as merchant with Pagopar**:
   - Need RUC (tax ID) — she has this or can get it
   - Business account setup
   - Agreement to terms

2. **Get Bancard POS terminal**:
   - Visit Bancard office or apply online
   - Terminal rental fee (typically Gs 50-100k/month)
   - Takes card payments immediately

3. **For online booking**:
   - Pagopar API integration with website
   - WhatsApp Business for appointments

### Equipment needed:
- Smartphone/tablet for Pagopar app (no POS needed for online)
- OR Bancard terminal (physical card payments)
- Both recommended

---

## 7. CASH FLOW CONSIDERATIONS

### For high-value dental work (Gs 1-5M):

| Scenario | Payment method | Timing |
|---|---|---|
| Full upfront | Cash/bank transfer | Immediate |
| 6 installments | Pagopar | 6 months |
| 12 installments | Pagopar | 12 months |
| Card in person | Bancard POS | Immediate |

### Recommendation:
- Accept cash/bank transfer for discount (2-5%)
- Accept Pagopar for installments (patient pays fee)
- Accept Bancard for card payments

---

## 8. DIGITAL PAYMENTS LANDSCAPE PARAGUAY

From research:
- "80% of card transactions in Paraguay already interoperable"
- QR payments growing rapidly
- Mobile payments becoming standard
- Cash still significant but declining

**Paraguay is NOT a cash-only market** — digital payments infrastructure is solid.

---

## 9. KEY FINDINGS FOR DRA.'S PRACTICE

1. **Pagopar is viable** for payment plans on dental procedures
2. **Bancard** provides immediate card acceptance
3. **Fees are reasonable** for high-value transactions (Gs 400k+)
4. **Payment plans ENABLE cases** that cash couldn't — critical for her complex cases
5. **No Stripe** in Paraguay — must use local providers
6. **Setup is straightforward** with RUC

---

## 10. NEXT STEPS

1. Contact Pagopar directly for merchant rates
2. Visit Bancard for POS terminal setup
3. Ask about specific installment structures for dental
4. Consider: Patient pays card fee for installments vs. Dra. absorbing cost

---

## 11. SOURCES

- https://www.cartdna.com/shopify-payment-methods/PagoPar
- https://support.wix.com/en/article/connecting-pagopar-as-a-payment-provider
- https://www.bancard.com.py/
- https://www.pasarelasdepagos.com/shop/ecommerce-paraguay/woocommerce-paraguay/bancard-woocommerce/
- https://www.reddit.com/r/Paraguay/comments/14njouw/pagopar_es_la_%C3%BAnica_pasarela_de_pago_disponible/