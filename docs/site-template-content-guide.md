# DENTIST SITE — CONTENT GUIDE (site-template driven)
> Source of truth for mapping `Ai-Whisperers/site-template` to the Dra. Gabriella González Pane website.
> All content below follows the template’s JSON schema, feature flags, and SEO rules.
> Last updated: June 5, 2026.

---

## 1. SITE CONFIG (required first)

`content/es/site.json`
`content/en/site.json`

**Required fields**
- `site.name`: Dra. Gabriella González Pane
- `site.slug`: dra-gabriela
- `site.url`: https://dra-gabriela.com.py
- `site.locale`: es-PY
- `site.metaDescription`: ~150 chars with target Spanish keywords

**Business fields**
- `business.phone`: +595 XXX XXX XXX
- `business.whatsapp`: 595XXXXXXXXX
- `business.whatsappMessage`: Hola Dra. GP, me gustaría agendar una consulta.
- `business.email`: email@dra-gabriela.com.py
- `business.address`: Luque, Paraguay — dirección exacta al confirmar
- `business.coordinates.lat/lng`: confirmar al confirmar dirección
- `business.currency`: PYG
- `business.ruc`: número E.A.S. cuando esté lista

**Feature flags (recommended)**
- bookingForm: true
- googleMapsEmbed: true
- testimonials: true
- stats: true
- reasons: true
- ctaBanner: true
- whatsapp integration via WhatsAppFloat always visible
- blog: true (Phase 2)
- ecommerce / giftCards / loyalty / clientPortal: false (unless we add services later)

---

## 2. BRAND TOKENS

`content/tokens.json`

**Palette direction from spec**
- Primary: deep teal or forest green
- Secondary: warm white / off-white
- Accent: warm terracotta or gold
- Text: dark charcoal
- No bright clinical blue

**Typography**
- Headings: authoritative serif or clean authoritative sans
- Body: highly readable sans-serif
- Examples: Inter + DM Serif Display, or Plus Jakarta Sans

---

## 3. NAVIGATION

**`content/es/site.json → navigation`**

1. Inicio → /es
2. Filosofía → /es/filosofia
3. Servicios → /es/servicios
4. Precios → /es/precios
5. Contacto → /es/contacto

More dropdown (optional)
- Segunda Opinión → /es/segunda-opinion
- Blog → /es/blog
- FAQ → /es/faq

---

## 4. HOMEPAGE

**`content/es/hero.json`** → title / subtitle / slides / CTAs
**`content/es/stats.json`** → 4 animated counters
**`content/es/reasons.json`** → 6 pain cards
**`content/es/services/index.json`** → service teaser cards
**`content/es/testimonials.json`** → 4 social proof cards
**`content/es/cta.json`** → 2 CTA banners
**`content/es/process.json`** → 3-step patient flow

**Hero copy direction**
- Slide 1 headline: Odontología con criterio. No con prisa.
- Slide 2 headline: Planificamos antes de actuar. No vendemos procedimientos innecesarios.
- Slide 3 headline: Segunda opinión honesta + plan escrito antes de cualquier tratamiento

**Stats direction**
- 20+ años experiencia
- +2.000 pacientes
- 100% bilingüe Español + English
- Por evaluación / casos documentados

**Reasons direction**
1. Te dijeron que necesitás un procedimiento y no estás seguro
2. Querés entender tu boca antes de gastar dinero
3. Buscás una odontóloga que te escuche y no te apresure
4. Preferís English a explicar todo de nuevo
5. Querés materiales premium, no lo más barato
6. Precisás un plan escrito antes de empezar

**Services teaser cards**
- Segunda Opinión
- Plan de Tratamiento Integral
- Odontología General Conservadora
- Casos Complejos / Rehabilitación Oral

**Process steps**
- Escribí por WhatsApp → Response within 24h
- Primera consulta de evaluación → Full assessment, no surprise treatment
- Recibís plan escrito → Clear options, pricing, timeline

---

## 5. SERVICES PAGE

**`content/es/services/index.json`**
**`content/es/services/categories/`**

Categories to create under `services/categories/`:
1. `segunda-opinion.json`
2. `planificacion-tratamiento.json`
3. `odontologia-general.json`
4. `estetica-dental.json`
5. `rehabilitacion-oral.json`

**Each category requires**
- `title`
- `description`
- `items[]` with:
  - `name`
  - `description`
  - `priceGs`
  - `duration`
  - `highlights[]`
  - `cta`

**Canonical pricing source**
- Always copy prices from `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`
- Show disclaimer: “Precios referenciales. Pueden variar según complejidad del caso.”

---

## 6. PRICING PAGE

**`content/es/pricing.json`** (optional, if not using services page only)

- Use the template’s pricing page pattern
- Show grouped tables: Consultas y Planificación | Procedimientos comunes
- Finance section: Pagopar | Bancard | Cash discount
- FAQ about pricing copied from surgical content FAQ

---

## 7. ABOUT PAGE

**Use `content/es/site.json → business` first**
- `business.name`
- phone, address, hours
- Support with narrative copy in page component

**Optional: team section**
- If team section is enabled, populate `content/_shared/team.json`
- Single member: Dra. Gabriella González Pane
- Keep tone personal, not CV

---

## 8. TESTIMONIALS

**`content/es/testimonials.json`**

Fields per item
- `name`
- `quote`
- `service`
- `rating`
- `color`
- `initials`
- `date`

**Target themes**
- Second opinion clarity
- English-speaking experience
- Conservative recommendation (“no me quiso hacer de más”)
- Written plan and transparency

---

## 9. FAQ

**`content/es/faqs.json`**

Group by
- General
- Precios
- Segundo Opinión
- Turnos y Horarios
- Expat / English

Already approved content exists in
- `05_OPERATIONS/patient-communications/patient-faq-20-answers.md`
- `07_DESIGN/website/core-pages/first-visit-preparation-page.md`

---

## 10. CONTENT MIGRATION MAP

| site-template JSON | Dentist source |
|---|---|
| `content/es/site.json` | `07_DESIGN/website/site-config.json` |
| `content/es/hero.json` | `07_DESIGN/website/core-pages/home-page-content.md` |
| `content/es/stats.json` | home page trust metrics |
| `content/es/reasons.json` | home page “problem” section |
| `content/es/services/index.json` + categories | `07_DESIGN/website/service-pages/services-page-content.md` |
| `content/es/testimonials.json` | post-launch Google review seeding |
| `content/es/process.json` | first visit / second opinion patient journey |
| `content/es/faqs.json` | `05_OPERATIONS/patient-communications/patient-faq-20-answers.md` |
| `content/es/cta.json` | home + contact CTAs |
| `content/es/before-after.json` | optional; use later for visual case studies |

---

## 11. SEO REQUIREMENTS

**Per-page contract**
- Spanish H1 invariant: `/` = Odontología con criterio. No con prisa. `/servicios` = Servicios `/precios` = Precios
- Canonical pricing block in footer or pricing notice on service pages
- JSON-LD: LocalBusiness + FAQPage
- Sitemap and robots available via template `app/sitemap.ts` and `app/robots.ts`

---

## 12. HUMAN TASKS / INPUTS NEEDED

- WhatsApp number confirmation
- Exact Luque address
- Dra. GP professional photos (hero, about)
- E.A.S. registration number
- Final pricing sign-off from canonical document
- 5–10 real testimonials post-launch
- Before/after case photos with consent
- Google Maps embed coordinates after address confirmation

---

## 13. IMPLEMENTATION ORDER

1. Confirm `site.json` business fields
2. Build Spanish hero + stats + reasons in JSON
3. Build services categories from canonical pricing
4. Import testimonials and FAQs from approved docs
5. Wire page routes: Home → Filosofía → Servicios → Precios → Contacto → Segunda Opinión
6. Validate with text review and placeholder audit before launch

---

*Guide written for one executable content pipeline under `site-template`.*
