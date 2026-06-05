# DENTIST SITE — CONTENT ROAST & IMPROVEMENT PLAN
> Status: post-2026-06-05 audit
> Sources: client-profile-deep-dive.md, canonical-pricing-reference-v2.md, patient-faq-20-answers.md, 200-lesson competitive research

---

## 1. ROAST — WHAT'S WRONG / MISSING / MISALIGNED

### 🔴 CRITICAL (fix immediately)
1. **Pricing.json wrong on consultation** — shows Gs 150,000; canonical = Gs 300,000–450,000. Underselling by 50%+. Also missing tiers (standard, extended, complex planning).
2. **Stats.json uses unsupported vanity metric** — "2,000+ patients treated" not in client profile. She has ~130/month at current job, no career total documented. Fabricated metric risks credibility.
3. **Why-us copy ignores actual differentiators** — reasons.json says "premium materials" but never names the German resin she explicitly chose, never says "no overtreatment" in her voice, never mentions 20 years of complex cases ("me encantan los desastres").
4. **Testimonials.json lacks source/verification** — no Google Reviews badge, no referral attribution, no location diversity. 4 entries = thin. Competitive standard = 8–12.
5. **Site.json has inconsistent placeholders** — phone format changed mid-patch, address still "exact address pending", Saturday hours were "Closed" despite client saying she works Saturday mornings.
6. **FAQ.json misses 12 canonical questions** — patient-faq-20-answers.md exists but only ~8 of those 20 are represented. Missing: insurance nuance, root canals, extractions, crowns, emergencies, aesthetic limits, cancellation policy, what-if-I-don't-need-treatment.
7. **No About / Team page** — cannot show license, credentials, photo, story. Trust #121-134 in competitive research is completely missing.
8. **No Contact page with map** — address is placeholder, no Google Maps embed, no parking instructions.
9. **No Expat landing** — research shows expats are #1 pricing tier, but no dedicated EN CTA or landing content.
10. **No Second Opinion page** — it's the #1 differentiator and highest-conversion service, but no dedicated landing content.

### 🟡 HIGH (fix before launch)
11. **Hero CTA could be sharper** — "Agendar consulta" is generic. Should be benefit-linked: "Plan sin compromiso" or "Segunda opinión escrita".
12. **Reasons.json doesn't answer anxiety/sedation** — competitive research shows this is a top question; FAQ has it but home-pain cards don't address fear.
13. **Pricing.json missing corporate tiers** — canonical doc has full corporate tier matrix; site only shows individual pricing. B2B is a major revenue stream.
14. **No schema flags wired** — added schema flags in site.json but site-template may not render JSON-LD unless explicitly coded.
15. **Testimonials no service diversity** — all are consultation/second-opinion; no restoration, endo, or aesthetic stories despite 42 restorations in May alone.
16. **Missing "when we refer out" page** — competitive research #78 explicitly recommends this. Builds trust by showing honesty.
17. **No blog/index** — content strategy requires 12 educational posts; none started.
18. **Missing before/after policy** — competitive research warns against showing B/A without consent workflow. No policy page exists.
19. **Payment methods not visualized** — only text mentioned; competitive research says show logos/icons.
20. **No loyalty/referral program content** — client audio mentions this idea, repo has referral program plan, but no site content.

### 🟢 MEDIUM (polish)
21. **Tokens.json was generic Inter-only** — replaced with DM Serif Display + Inter, teal/gold palette. Good.
22. **Process.json could add timeline preview** — "24h response, 45–60 min visit, 1–3 days for written plan" helps set expectations.
23. **CTA.json not examined yet** — likely generic; should align with new default CTAs.
24. **No dark-mode-ready palette** — minor, competitive research #177.
25. **Hero badge "20+ years" is vague** — says 20+ but client has ~20 exactly. Should be precise once confirmed.

### 🟢 LOW / FUTURE
26. **Cookie consent off** — fine for now, but needed if using retargeting.
27. **Blog SEO not started** — long-term play, not pre-launch blocker.
28. **No heatmap tracking** — set up later via plausible events.

---

## 2. ROOT CAUSE CHAINS

### A. Pricing understatement → wrong revenue expectation
Symptom: `pricing.json` shows Gs 150,000 consultation
Why: Someone drafted placeholder pricing without reading canonical doc
Fix: Realign to authoritative pricing, add tiers, add disclaimer + WhatsApp CTA

### B. Weak trust → low conversion on second opinion
Symptom: Testimonials thin, stats unsupported, no About page
Why: Content copied from template examples, not grounded in client reality
Fix: Rewrite stats from verifiable data, add 4+ testimonials, build About page

### C. Expats not captured → premium segment ignored
Symptom: No expat landing, no EN-first CTA on hero, no English-intake form
Why: Content focused on ES default, competitive research not yet applied
Fix: Add EN-first hero slide, expat FAQ group, EN intake flow

### D. No differentiation → looks like every other dentist site
Symptom: Reasons.json reads like generic dental marketing
Why: Didn't import client's actual voice from client-profile-deep-dive.md
Fix: Rewrite pain cards in her exact language: "no paraguayizar", "materiales alemanes", "plan escrito antes de actuar"

---

## 3. IMPROVEMENT ROADMAP

### Sprint A: Fix incorrects (today)
- [x] Rewrite `pricing.json` with canonical prices + tiers
- [x] Rewrite `stats.json` from real client data
- [x] Rewrite `reasons.json` with client's actual voice
- [x] Add trust fields to `site.json`
- [x] Fix Saturday hours in `site.json`
- [x] Improve `hero.json` with trust badges and WhatsApp CTAs
- [ ] Update `testimonials.json` to 8–12 entries with source + verified + diversity
- [ ] Expand `faqs.json` to 20 questions matching canonical doc
- [ ] Fix phone/address placeholders or mark clearly as TBD

### Sprint B: Add missing pages (this week)
- [ ] Create `content/en/about.json`, `content/es/nosotros.json`
- [ ] Create `content/en/contact.json`, `content/es/contacto.json`
- [ ] Create `content/en/second-opinion.json`, `content/es/segunda-opinion.json`
- [ ] Create `content/en/expat.json`
- [ ] Create `content/en/blog.json`, `content/es/blog.json`

### Sprint C: SEO / Technical (next)
- [ ] JSON-LD LocalBusiness schema
- [ ] JSON-LD FAQPage per group
- [ ] JSON-LD Review aggregate
- [ ] hreflang tags
- [ ] sitemap + robots
- [ ] OpenGraph / Twitter per page
- [ ] alt-text strategy for all images

### Sprint D: Conversion (pre-launch)
- [ ] WhatsApp message templates per service
- [ ] Fixed mobile CTA bar
- [ ] PDF download offer after pricing
- [ ] Post-visit review request
- [ ] Referral capture in intake form

---

## 4. VERIFICATION CHECKLIST

Before any content ships:
- [ ] Every price in `content/` matches `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`
- [ ] Every FAQ answer matches `05_OPERATIONS/patient-communications/patient-faq-20-answers.md` tone
- [ ] No placeholder credit card / bank fields remain in forms
- [ ] No fake review stars or unsupported claims about volume
- [ ] All images have consent or are marked as placeholder
- [ ] Phone, address, RUC, MSPBS are either real or clearly marked pending

---

## 5. RECOMMENDATION

**Stop building pages until Sprint A is fully verified.** The current pricing.json alone undermines revenue by 50%+ if shipped. Fix foundations, then build on them.

**Priority order:**
1. Verify canonical pricing → update pricing.json
2. Rewrite reasons.json in Dra. GP's voice
3. Add 4 real testimonials (even if from colleagues/early patients)
4. Build About page with real credentials + photo
5. Build Second Opinion landing as first full page
6. Then launch.
