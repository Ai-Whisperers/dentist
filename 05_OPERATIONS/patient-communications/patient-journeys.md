# Patient Journey Specifications — Dra. Gabriella González Pane (June 2026)

Three de-identified patient journeys mapped from first contact through recall. Each journey links existing templates to every touchpoint.

Cross-ref: all prices reference `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`.

---

## Journey A — Insurance-Dependent Patient

**Profile:** 34-year-old, employed in private sector with dental insurance, middle-income. Currency: Gs/month coverage limited to basic procedures. Pain point: long approval times, overtreatment pressure, limited time in-chair.

**Path:**

1. First contact — WhatsApp or Facebook. Uses `08_WHATSAPP/templates/whatsapp-setup-configuration-guide.md` for automated warm-reply.
2. Scheduling — `09_TEMPLATES/appointment-confirmation-card-template.md` confirms slot + documents needed (insurance card, ID).
3. Consultation — clinical intake using `05_OPERATIONS/patient-communications/patient-intake-form-legal.md` + privacy consent from `05_OPERATIONS/legal-compliance/patient-legal/privacy-policy.md`.
4. Treatment plan — `05_OPERATIONS/legal-compliance/practice-legal/legal-master-checklist.md` ensures required docs are in file before proceeding.
5. Payment — insurance reimbursement flow. Refer patient to `05_OPERATIONS/legal-compliance/practice-legal/invoice-template.md` for personal invoice copy.
6. Recall — `09_TEMPLATES/recall-card-template.md` at 6 months.

**Upsell path:** Offer second opinion on same condition via `07_DESIGN/website/service-pages/second-opinion-page-content.md` and quote as private add-on if patient wants to bypass insurance wait times.

---

## Journey B — Private Premium Patient

**Profile:** 38-year-old executive, no insurance, cash-capable, time-poor. Willing to pay Gs 400k–1M for speed + clarity. Expects concierge feel.

**Path:**

1. First contact — warm lead from referral or Google Business. Script in `05_OPERATIONS/patient-communications/patient-scripts-in-person-phone.md`.
2. Scheduling — priority slot offered in first reply. Confirmed via `09_TEMPLATES/appointment-confirmation-card-template.md`.
3. Consultation — premium intake; treatment planning session (Gs 800k standalone) documented in `00_STRATEGIC/strategic-context/three-strategic-options-analysis.md` Option A mechanics.
4. Treatment plan — signed PDF from `05_OPERATIONS/legal-compliance/practice-legal/legal-master-checklist.md`; proposal text from `00_STRATEGIC/financial-pricing/financial-model-projections-v2.md`.
5. Payment — Pagopar/Bancard. POS script from `03_LAUNCH/whatsapp-outreach/whatsapp-business-plan.md` and payment spec from `01_RESEARCH/payments/payment-systems-onboarding-guide.md`.
6. Recall — `09_TEMPLATES/recall-card-template.md` + add referral ask using `09_TEMPLATES/referral-card-template.md`.

**Differentiator:** “No overtreatment” narrative from `07_DESIGN/website/core-pages/philosophy-page-content.md` should be surfaced explicitly in the consultation room.

---

## Journey C — Exats / International Patient

**Profile:** 26–50-year-old foreign resident (US/EU), English-dominant, no Paraguayan insurance, expects international-standard care. Channels: Instagram, InterNations, expat groups, dentist search on Instagram.

**Path:**

1. First contact — Instagram profile via `07_DESIGN/brand-assets/social-media-profile-specs.md`; DM landing in `08_WHATSAPP/automation/whatsapp-operations-guide.md`. Start in English.
2. Scheduling — assistant confirms via WhatsApp in English or Spanish; timezone-aware booking window (morning slots for expats).
3. Consultation — bilingual intake. Use `05_OPERATIONS/patient-communications/new-patient-intake-form.md` + clarify international payment options upfront.
4. Treatment plan — pricing communication uses USD-equivalent Gs ranges; publish in English using `07_DESIGN/website/service-pages/services-page-content.md`.
5. Payment — Bancard/Pagopar international acceptance confirmed in `01_RESEARCH/payments/payment-infrastructure-analysis.md`. International dental tourism angle covered in `01_RESEARCH/community/dental-tourism-opportunity-analysis.md`.
6. Recall — automated 6-month WhatsApp in English/Spanish via `09_TEMPLATES/recall-card-template.md`. Offer Google review template from `03_LAUNCH/website-content/social-proof-trust-signals-content.md`.

**Key docs:** Expat landing page content from `03_LAUNCH/website-content/expat-landing-page-content.md` and community deep-dive from `01_RESEARCH/community/expat-community-deep-dive.md`.
