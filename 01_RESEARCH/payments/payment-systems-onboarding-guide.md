> **PRICING CROSS-REFERENCE:** All prices reference `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`. When in doubt, the canonical doc wins.

# PAYMENT INFRASTRUCTURE — PAGOPAR & BANCARD ONBOARDING
## Dra. Gabriella González Pane — Merchant Setup Guide

**Date:** June 2026
**Source:** pagopar.com, bancard.com.py, market research

---

## OVERVIEW

To accept card and digital payments from patients, Dra. GP needs:
1. **POS terminal** (for in-person card payments) — via Bancard
2. **QR code / link payments** (for WhatsApp and remote payments) — via Pagopar

**Both are required** for a modern private practice. Patients expect to pay by card, and Pagopar links can be sent via WhatsApp for advance payment or payment plans.

---

## BANCARD — POS TERMINAL

### What It Is
Bancard is the dominant card payment processor in Paraguay. They provide POS terminals for physical card acceptance (Visa, Mastercard, American Express, etc.).

### Onboarding Steps

**Step 1: Contact Bancard**
- Website: bancard.com.py
- Phone: (021) 417-8000
- Email: [typically available on website]
- Walk into any Itaú branch and ask for Bancard POS

**Step 2: Required Documents**
- [ ] RUC (tax ID for the business)
- [ ] CI of the business owner
- [ ] Proof of business address
- [ ] Bank account statement (for direct deposit of payments)
- [ ] EAS registration (or other company registration)

**Step 3: Choose POS Type**

| Type | Cost | Best For |
|------|------|---------|
| Traditional phone-line POS | Monthly rental ~Gs 100-150k | Fixed location |
| Mobile POS (GPRS/4G) | Monthly rental ~Gs 150-200k | Mobile/rural visits |
| Android POS app | Monthly fee ~Gs 80-120k | Low volume |

**Step 4: Wait for Installation**
- Typically 3-7 business days after document submission
- Bancard technician installs and trains on use

### Fees (2026 estimates)

| Fee Type | Rate |
|----------|------|
| Monthly rental | Gs 100,000-200,000 |
| Transaction fee (credit) | 3-4% of transaction |
| Transaction fee (debit) | 1-2% of transaction |
| Settlement | Next day to bank account |

**Important:** Fees vary by merchant category and volume. Negotiate after 3 months if high volume.

---

## PAGOPAR — QR PAYMENTS & LINKS

### What It Is
Pagopar is Paraguay's leading QR code and payment link processor. It allows:
- Generate QR codes for patients to scan and pay
- Send payment links via WhatsApp
- Receive payments without physical POS
- Subscription/Debit model for recurring payments

**From pagopar.com:**
> "las tarjetas y código QR, sin costos de mantenimiento"

**Key features:**
- No monthly maintenance fee (per website)
- Transaction fees apply per payment
- App ueno for generating QR codes
- Link de pago for sending payment links via chat

### Onboarding Steps

**Step 1: Register as Merchant**
- URL: pagopar.com
- Look for "Quiero cobrar" or "Registrarme"
- Or contact: pagopar.com/api (for developer integration)

**Step 2: Required Documents**
- [ ] RUC (tax ID)
- [ ] CI of business owner
- [ ] Bank account for deposits
- [ ] EAS or company registration

**Step 3: Setup**
- Create merchant account online
- Configure bank account for deposits
- Generate QR code or payment links
- Link to WhatsApp Business for easy sending

### Fees (2026 estimates)

| Fee Type | Rate |
|----------|------|
| Setup | Free (typically) |
| Monthly maintenance | Gs 0 (per website) |
| Transaction fee | 3-5% depending on amount |
| QR code generation | Free |
| Payment link | Free |

**Note:** Pagopar is particularly good for Dra. GP because payment links can be sent via WhatsApp — patients can pay before arriving or in installments.

---

## TIGO MONEY — ADDITIONAL RAIL

### What It Is
Tigo Money is a mobile money / e-wallet service popular in Paraguay. Many Paraguayans have Tigo Money accounts.

### How to Accept
- Register as a Tigo Money merchant
- Give patients your Tigo Money number
- They send payment to your number
- Funds transferred to bank account

**Advantage:** No POS needed, instant settlement
**Disadvantage:** Requires Tigo SIM and registration process

---

## COMPARISON TABLE

| Feature | Bancard POS | Pagopar QR | Tigo Money |
|---------|-------------|------------|------------|
| Setup cost | Low-Medium | Free-Low | Free |
| Monthly fee | Gs 100-200k | Gs 0 | Gs 0 |
| Transaction fee | 3-4% (credit) | 3-5% | 2-3% |
| Settlement time | Next day | Same day | Same day |
| Best for | In-person card | Remote/link payments | Mobile users |
| Hardware needed | POS terminal | Smartphone only | Smartphone only |
| QR code | No | Yes | Yes |

---

## RECOMMENDED SETUP FOR DRA. GP

### Phase 1: Immediate (Month 1)
- [ ] Open bank account for business (separate from personal)
- [ ] Apply for Bancard POS (traditional, phone-line)
- [ ] Register Pagopar merchant account
- [ ] Setup Pagopar QR code + test with 2-3 friends

### Phase 2: Optimize (Month 3)
- [ ] Review transaction volumes and fees
- [ ] Negotiate Bancard rates based on volume
- [ ] Add Tigo Money if patient demand exists
- [ ] Consider Pagopar Checkout for website (if website has booking)

### Cost Estimate (Monthly)

| Item | Cost (Gs) | Notes |
|------|-----------|-------|
| Bancard POS rental | 120,000 | Approximate |
| Pagopar (no monthly fee) | 0 | Transaction fees only |
| Tigo Money | 0 | No monthly fee |
| **Total monthly** | **~120,000** | ~$15 USD |

**Per-transaction cost example:**
- Patient pays Gs 400,000 for restoration
- Bancard fee (3.5%): Gs 14,000
- Net to Dra. GP: Gs 386,000

---

## STEP-BY-STEP CHECKLIST

### Bancard POS Setup
```
1. [ ] Gather documents: RUC, CI, proof of address, bank account
2. [ ] Visit nearest Itaú branch or Bancard office
3. [ ] Request POS terminal for professional services
4. [ ] Choose terminal type (phone-line recommended for office)
5. [ ] Sign merchant agreement
6. [ ] Wait 3-7 days for installation
7. [ ] Test with small transaction
```

### Pagopar Setup
```
1. [ ] Go to pagopar.com
2. [ ] Click "Quiero cobrar" or merchant registration
3. [ ] Fill business information
4. [ ] Upload RUC + CI
6. [ ] Configure bank account for deposits
7. [ ] Generate QR code
8. [ ] Test by sending link to personal phone
9. [ ] Connect to WhatsApp Business for easy access
```

---

## PAYMENT PLAN INTEGRATION

**For expensive treatments (Gs 1M+), offer payment plans:**

**Option A: Pagopar Link with installments**
- Send link for 50% deposit
- Patient pays remainder in 2-3 installments
- Each payment via Pagopar link

**Option B: Tigo Money transfers**
- Patient sends installments as they accumulate
- Record each payment in financial tracker

**Option C: Cash discount**
- 10% discount for full payment upfront
- Incentivizes immediate payment

---

## KEY CONTACTS

| Service | Contact | Notes |
|---------|---------|-------|
| Bancard | (021) 417-8000 / bancard.com.py | POS terminals |
| Pagopar | pagopar.com | QR + payment links |
| Tigo Money | tigo.com.py | Mobile payments |
| Itaú | itau.com.py | Bank account needed |

---

*Research completed: June 1, 2026*
*Recommended: Open business bank account first, then apply for both Bancard + Pagopar simultaneously*