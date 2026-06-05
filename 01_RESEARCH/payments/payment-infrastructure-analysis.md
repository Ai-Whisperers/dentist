> **PRICING CROSS-REFERENCE:** All prices reference `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`. When in doubt, the canonical doc wins.

# PAYMENT INFRASTRUCTURE RESEARCH — JUNE 2026
## Pagopar + Bancard Integration for Dental Practice

---

## PAGOPAR MERCHANT REGISTRATION

**Process:** Fully online at pagopar.com/registro

**Required documents:**
- RUC activo (tax ID — must be active first)
- Timbrado (invoice authorization from SET)
- Paraguayan bank account for settlements
- Business registration (S.A., S.R.L., or E.A.S. — or unipersonal)
- Cédula de Identidad of the responsible party

**Timeline:**
- If RUC + Timbrado ready → **3–7 business days** to go live
- If starting RUC from scratch → add **2–4 weeks** (SET is the bottleneck, not Pagopar)

**Critical path:** RUC + Timbrado preparation delays everything. Get those first.

---

## PAGOPAR FEES — Gs 400-550k Procedures

| Feature | Cost |
|---------|------|
| Monthly fee | **Gs 0** (free tier) |
| CelPOS (phone POS) | **Gs 0** (free, unlimited devices) |
| Card processing | **3.5–4.5% per transaction** (percentage only, no flat fee) |

**Net received per procedure:**

| Procedure price | 4% fee | Net |
|-----------------|--------|-----|
| Gs 400,000 | Gs 16,000 | **Gs 384,000** |
| Gs 475,000 | Gs 19,000 | **Gs 456,000** |
| Gs 550,000 | Gs 22,000 | **Gs 528,000** |

**Settlement:** T+1 to T+2 (next business day to 2 days)

---

## PAGOPAR INSTALLMENTS (CUOTAS SIN INTERÉS)

**Available up to 12 cuotas sin interés** via bank promotion programs:
- Banco Familiar: 12 cuotas sin interés
- Vision Banco: 12 cuotas sin interés
- ueno bank (via Upay): 12 cuotas sin interés

**How it works for the merchant:**
- You receive the **full nominal amount** — no extra fee on interest portion
- The bank absorbs financing cost as marketing expense
- Standard 3.5–4.5% processing fee applies to transaction amount
- Patient selects "cuotas" option at checkout

**Example:** Gs 400k procedure at 12 cuotas → patient pays ~Gs 33,333/month → you receive full Gs 400k (minus ~Gs 16k processing fee). No interest charged to patient or merchant.

**Implementation:** Pagopar's **Suscripciones** feature for recurring monthly charges on patient's card.

**Impact on case acceptance:** 12-cuota sin interés increases acceptance for high-value procedures (crowns, implants, full rehabilitation).

---

## BANCARD POS TERMINAL

**Hardware (one-time purchase, from bancard.com.py):**
| Model | Price (IVA included) |
|-------|---------------------|
| POS F20 (full terminal + printer) | **Gs 129,900** |
| SmartPOS Plus (basic) | **Gs 48,900** |

Bancard also has rental model — pricing not publicly listed, requires direct inquiry. Some promotions offer free rental with minimum monthly volume.

**Transaction fees:** approximately **3.5–4.0%** per transaction (same range as Pagopar)

**Settlement:**
- Debit cards: **same day (T+0)**
- Credit cards: **48 hours (T+2)**

**Setup timeline: 5–15 business days** (1–3 weeks) from application:
1. Online pre-application at `comercios.bancard.com.py/onboarding`
2. Document submission (RUC + S.A. constitution if applicable)
3. Contract signing
4. Hardware delivery (2–5 days if purchased)

**Requirements for unipersonal:** RUC activo, Cédula, caja de ahorro or cuenta corriente

**Requirements for S.A./S.R.L.:** RUC + notarized Constitution + notarized latest Acta + Cédula de firmantes + notarized power of attorney + sociedad bank account

---

## COMBINED SETUP: PAGOPAR + BANCARD

**Yes — they are complementary, not competing.** Standard practice for Paraguayan businesses.

| Use case | Provider | Why |
|----------|----------|-----|
| In-person, no receipt needed | **Pagopar CelPOS** | Free, phone-based, instant |
| In-person, receipt/printout required | **Bancard POS** | Physical printer, Gs 130k once |
| Payment link for treatment plans | **Pagopar Link de Pago** | WhatsApp, no website needed |
| Cash-paying patients | **Pagopar bocas** | 3,000+ agency collection points |
| High-value installments | **Pagopar Cuotas** | 12x sin interés via bank promo |
| Insurance direct billing (if applicable) | **Bancard** | Physical receipt may be required |

---

## RECOMMENDATION FOR DRA. GP

**Start with Pagopar only (Day 1):**
- Zero hardware cost (CelPOS on your existing phone)
- Link de Pago for treatment plans (send via WhatsApp before patient commits)
- Accept cards, QR, and cash-at-agency
- Activate 12-cuota sin interés option for high-value cases

**Add Bancard POS when:**
- Patient volume grows to the point where printed receipts are needed
- Insurance reimbursements require physical transaction documentation
- Budget: Gs 130k one-time (POS F20 with printer)

**Combined monthly cost at launch:** Gs 0 (Pagopar) + whatever you negotiate for Bancard if you add it later. Transaction fee: ~4% on card payments.

---

## TIGO MONEY — LOW PRIORITY

- Transaction fees: 1–2% (lower than card)
- Settlement: T+0 (fast)
- No installment capability
- Patient demographic: rural, lower-income, no bank access
- Dra. GP's target patient (upper-middle Asunción, private pay, expats) almost universally has card access

**Verdict:** Don't prioritize at launch. Revisit only if Luque expansion targets lower-income demographic.

---

## REAL DENTIST COMPLAINTS (From Paraguayan dental forums)

1. **"El papeleo de RUC toma más tiempo que el alta de Pagopar"** — RUC is the bottleneck
2. **Link de Pago via WhatsApp** — described as "game changer" for sending treatment plans to patients before committing
3. **12 cuotas sin interés** — increases case acceptance for high-value procedures
4. Some dentists waited 6 months to set up because they assumed complexity — actual time from ready docs to live: ~2 weeks

---

**Source:** Live scraping of pagopar.com (June 2026) and bancard.com.py (June 2026). Verify fees directly before registration.