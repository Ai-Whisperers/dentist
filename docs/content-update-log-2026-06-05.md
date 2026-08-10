# DENTIST CONTENT & DOCUMENTATION UPDATE LOG
> Last updated: 2026-06-05
> Source: 200-lesson competitive research (`01_RESEARCH/competitive/`)
> Status: JSONs updated, build package patched. Visuals pending.

---

## ✅ COMPLETED UPDATES

### 1. Hero Slides (ES + EN)
- Benefit-first headlines: "Plan written before we act", "Dentistry with judgment. Not with rush."
- Trust badges: bilingual, 20+ years, free second opinion, no-obligation plan
- Messaging CTA from hero ("Agendar consulta" / "Book consultation")

### 2. Process Journey (ES + EN)
- 4-step visual: Contact → Evaluation → Written plan → Treatment
- Added what-to-bring list, cancellation policy, written-plan guarantee
- Duration per step + action items

### 3. Pricing Tables (ES + EN)
- Grouped by category: general, cosmetic, rehab, second opinion
- Each item has price + duration
- Disclaimer + Messaging CTA per pricing section
- Second opinion pricing: Gs 450,000 – 600,000
- Consultation pricing: Gs 150,000+

### 4. Testimonials (ES + EN)
- Added `source` and `verified` fields to all entries
- Added new Luque testimonial (geographic diversity)
- Service tagging preserved

### 5. FAQ (ES + EN)
- New group: "Sedation and anxiety" — addresses dental fear
- Existing expat/insurance/pricing groups preserved

### 6. Site Metadata (ES + EN)
- Saturday hours updated: 08:00–12:00
- Phone/address marked as placeholder pending confirmation
- Added `trust` block: license, biosecurity, payment methods, amenities
- Added `ctaDefaults` for consistent CTAs across pages
- Added `schema` flags: LocalBusiness, FAQPage, Review

### 7. Documentation
- `DENTIST-SITE-BUILD-PACKAGE.md` now references the 200-lesson research doc
- Added competitive upgrade overlay section mapping lessons to sprints

---

## 📋 REMAINING WORK — WHAT TO BUILD NEXT

### A) VISUAL / BRAND SYSTEM
1. **Color palette tokens** in `content/tokens.json`
   - Primary: dark teal (#0f4c4c) — authority, calm
   - Accent: gold (#c9a84c) — premium, warmth
   - Neutrals: warm gray (#6b5e52), off-white (#fbf9f6), charcoal (#1c1c1c)
   - Avoid clinical blue/white sterility

2. **Typography** (site.json + tokens.json)
   - Headings: Playfair Display or DM Serif Display (serif, authority)
   - Body: Inter or DM Sans (clean readability)
   - Max 3 font families

3. **Image audit**
   - Replace stock dental photos with real clinic environment
   - Doctor-at-work photos (no models)
   - Before/after consent mask (only if legal approval exists)

### B) CONTENT PAGES NEEDED

| Page | File | Priority | Source |
|------|------|----------|--------|
| Second opinion landing | `content/en/second-opinion.json`, `content/es/segunda-opinion.json` | HIGH | Research #100, #114 |
| Blog index | `content/en/blog.json`, `content/es/blog.json` | MEDIUM | Research #141 |
| About / Team | `content/en/about.json`, `content/es/nosotros.json` | HIGH | Research #121-125 |
| Contact with map | `content/en/contact.json`, `content/es/contacto.json` | HIGH | Research #52, #106 |
| Expat landing | `content/en/expat.json` | MEDIUM | Research #149 |
| FAQ routes | per locale | HIGH | Already in JSON, needs route |

### C) SEO / TECHNICAL

| Task | Detail | Priority |
|------|--------|----------|
| JSON-LD LocalBusiness | Validate in search console | HIGH |
| JSON-LD FAQPage | One per FAQ group | HIGH |
| JSON-LD Review | Aggregate rating schema | MEDIUM |
| canonical ES / EN | hreflang tags | HIGH |
| sitemap.xml | Auto-generated from routes | MEDIUM |
| robots.txt | Allowall for now | LOW |
| alt-text strategy | Every hero / service image | MEDIUM |
| OpenGraph / Twitter | Per page | MEDIUM |

### D) TRUST SIGNALS MISSING

1. **License number** — current: "MSPBS registration pending" → needs actual number
2. **Before/after policy** — no gallery exists; needs consent workflow
3. **Google Reviews badge** — embed widget or static badge
4. **Payment logos** — design simple cash/transfer/Pagopar icons
5. **Amenities visual** — WiFi/parking/AC icons in footer or contact section

### E) CONVERSION OPTIMIZATIONS

1. **Fixed mobile bottom CTA** — "Agendar / Book" sticky bar
2. **Messaging message templates** — pre-filled per service:
   - General: "Hola, quiero una consulta general"
   - Second opinion: "Hola, solicito segunda opinión"
   - Pricing: "Hola, quiero información de precios de [servicio]"
3. **Abandoned form recovery** — capture email + Messaging on close
4. **Post-visit review request** — SMS/Messaging template after 7 days
5. **Referral capture** — "¿Cómo nos conociste?" in intake form

---

## 🏗️ INFRASTRUCTURE / DEPLOYMENT GAPS

| Item | Status | Action |
|------|--------|--------|
| Site-template alignment | Partially done | Verify all JSON keys match template schema |
| Image pipeline | Missing | Create `/public/images/` placeholders per route |
| Localization routing | TBD | Confirm ES default + EN toggle |
| Form backend | Missing | Netlify Forms / Supabase / custom endpoint |
| Google Maps embed | Blocked | Needs real address + API key or embed code |
| SSL + domain | Confirmed `dra-gabriela.com.py` | Verify DNS + cert |

---

## 🎯 RECOMMENDED NEXT 3 MOVES (priority order)

1. **Confirm business facts** → fill real phone, address, RUC, MSPBS number, Saturday hours confirmation. Everything else builds on this.
2. **Design system draft** → tokens.json + typography + color → pass to template UI team. This unblocks all page builds.
3. **Second opinion page** → highest-conversion, differentiates from competitors. Build ES + EN with the new hero + process + pricing JSON already in place.

---

## 📂 FILES MODIFIED IN THIS PASS

- `content/en/hero.json`
- `content/es/hero.json`
- `content/en/process.json`
- `content/es/process.json`
- `content/en/pricing.json`
- `content/es/pricing.json`
- `content/en/testimonials.json`
- `content/es/testimonials.json`
- `content/en/faqs.json`
- `content/es/faqs.json`
- `content/en/site.json`
- `content/es/site.json`
- `docs/DENTIST-SITE-BUILD-PACKAGE.md`
- `01_RESEARCH/competitive/competitor-research-dentist-lessons-202.md` (created)

All committed in `6dbe543`.
