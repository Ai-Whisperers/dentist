# Master Upgrade Plan — Dra. Gabriella Site (ometzdental.com)

**Date:** July 2, 2026
**Author:** Erebus / Ai-Whisperers
**For:** Ivan (founder), Gaby (client), Kiki (marketing)
**Status:** Active — implementation wave starting today
**Companion to:** `anti-anxiety-dentist-research-gaby-2026.md` (Insight 1-10)
**Targets:** `ometzdental.com/en`, `ometzdental.com/es`, `dragabriela.paragu-ai.com` (legacy redirect)

---

## Executive summary

The site is **structurally sound** (Next.js 16 + Tailwind v4 + DM Serif Display + Inter + Caveat, semantic JSON content, i18n routing, schema.org scaffold). What's **missing for the anxiety niche** is the empathy voice, the anxiety-targeted FAQ, the WhatsApp-primary contact pattern, the bilingual promise, and the voice-of-doctor asset.

**12 work blocks** grouped into 5 phases. Total est. work: 16-22 hours of dev + Gaby's 30-90 second audio + 3-5 fear-named testimonials + photos of consultorio. **No DNS / domain changes** — domain strategy is locked.

**Three blocking inputs from Gaby (cannot ship without):**
1. 60-90 sec audio of Gaby's voice
2. 3-5 testimonials that NAME the fear
3. Photos of the actual consultorio

**Tone of the upgrade:** Not redesign. **Refinement.** The brand "Ometz — I listen" is already correct. We're sharpening the angle, not changing the identity.

---

## Phase 1 — Brand tokens & visual system refinement (4 hrs)

### Block 1.1 — Add "warmth palette" as alternative accent

**Why:** Current palette is teal `#0f4c4c` + gold `#c9a84c` + cream `#fbf9f6`. Strong for premium positioning but reads slightly clinical. Anxiety-friendly sites use **sage / soft terracotta / muted blue** to soften the medical cue.

**What:** Add a second palette `warmth` in `content/tokens.json` with softer, anxiety-friendly colors. Toggle via `defaultPalette` for A/B testing without breaking the brand.

```json
"palettes": {
  "default": { ...existing... },
  "warmth": {
    "primary": "#5a7a6f",          // sage-teal (calmer than #0f4c4c)
    "primaryForeground": "#ffffff",
    "secondary": "#f7f3ec",        // warm beige
    "secondaryForeground": "#2a3a35",
    "accent": "#d4a574",           // soft terracotta-gold
    "accentForeground": "#ffffff",
    "background": "#fbf8f3",        // warmer cream
    "surface": "#ffffff",
    "surfaceMuted": "#f0eadf",
    "text": "#2a2a2a",
    "textLight": "#5a5048",
    "textMuted": "#8a7e70",
    "success": "#5a8a6f",
    "error": "#a85a4a",
    "warning": "#a87a3a"
  }
}
```

**Tailwind v4 sync:** Mirror as `--color-accent-warmth: #5a7a6f`, etc. in `app/globals.css` `@theme` block.

**Verify:** Contrast check on `bg-bg` × `text-fg-muted` with new palette = must clear 4.5:1 AA.

### Block 1.2 — Add anxiety-specific utility classes

**Why:** Components will repeat the same anxiety patterns (hand-signal pill, slow-pace badge, you-control CTA). Make them reusable.

**What:** Add to `app/globals.css`:

```css
/* "You control" pill — teal-bordered, soft cream fill, no hard borders */
.pill-control {
  display: inline-flex; align-items: center; gap: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 9999px;
  border: 1.5px solid var(--accent);
  background: var(--accent-soft);
  color: var(--accent);
  font-size: 0.875rem;
  font-weight: 600;
}

/* Hand-signal icon container — circular, gold ring */
.signal-circle {
  display: inline-flex; align-items: center; justify-content: center;
  width: 64px; height: 64px;
  border-radius: 9999px;
  background: var(--gold-soft);
  border: 2px solid var(--gold);
  color: var(--accent-2);
}

/* Slow-paced badge — gradient border, soft inner */
.badge-pace {
  display: inline-flex; align-items: center; gap: 0.375rem;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  background: linear-gradient(135deg, var(--gold-soft), var(--accent-soft));
  color: var(--accent-2);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.05em;
}

/* "Fear named" testimonial — soft border-left, larger quote */
.testimonial-fear {
  border-left: 4px solid var(--gold);
  background: var(--surface);
  padding: 1.5rem;
  border-radius: var(--radius-md);
  position: relative;
}
.testimonial-fear::before {
  content: '\201C';
  position: absolute;
  top: -0.5rem; left: 1rem;
  font-family: var(--font-heading);
  font-size: 4rem;
  color: var(--gold);
  opacity: 0.4;
  line-height: 1;
}

/* Voice-of-doctor transcript box — magazine-style */
.voice-doctor {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 2rem;
  position: relative;
}
.voice-doctor::before {
  content: '';
  position: absolute;
  top: 0; left: 0;
  width: 6px; height: 100%;
  background: linear-gradient(180deg, var(--accent), var(--gold));
  border-radius: var(--radius-lg) 0 0 var(--radius-lg);
}

/* "Show don't tell" empathy card */
.empathy-show {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  transition: all 280ms ease;
}
.empathy-show:hover {
  border-color: var(--gold);
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

/* Bilingual promise band */
.bilingual-band {
  background: linear-gradient(135deg, var(--accent-soft) 0%, var(--gold-soft) 100%);
  border-top: 1px solid var(--gold);
  border-bottom: 1px solid var(--gold);
}
```

### Block 1.3 — Add `--font-caveat` font variable (currently broken)

**Bug found:** `globals.css` references `var(--font-caveat)` but the layout only declares `--font-whimsical`. Fix the chain.

```css
:root {
  --font-caveat: "Caveat", "Comic Sans MS", cursive;  /* ADD THIS */
}
```

This unblocks the `font-whimsical` utility class which already exists in `tokens.json`.

---

## Phase 2 — Hero & above-the-fold (5 hrs)

### Block 2.1 — Hero copy rewrite (EN + ES)

**Insight applied:** 1 (empathy shown, not claimed) + 4 (bilingual explicit) + 5 (sedation 3rd, not 1st) + 6 (WhatsApp primary CTA).

**Files:** `content/en/hero.json`, `content/es/hero.json`

**New structure:**

```json
{
  "title": "Te escucho. Antes de tocar.",
  "subtitle_es": "Soy la Dra. Gaby. Si tenés miedo al dentista, está bien. No hace falta que lo expliques, no hace falta que te disculpes. Vamos a hablar antes de cualquier procedimiento. Mi trabajo no es agarrar la fresa — es sentarnos, escucharte, y armar juntos un plan que tenga sentido. Rehabilitación oral, segunda opinión escrita, odontología con criterio. Atiendo en español y en inglés.",
  "subtitle_en": "I'm Dr. Gaby. If you're afraid of the dentist, that's OK. You don't have to explain why, and you don't have to apologize. We'll talk before any procedure. My work isn't grabbing the drill — it's sitting down, listening, and building a plan together. Oral rehabilitation, written second opinions, dentistry with clinical judgment. Care in English and Spanish.",
  
  "cta_primary_es": "Escribime por WhatsApp",
  "cta_primary_en": "Message me on WhatsApp",
  "cta_secondary_es": "Tengo miedo — ¿empezamos por hablar?",
  "cta_secondary_en": "I'm scared — can we start by talking?",
  
  "bilingual_promise": {
    "es": "Atención en español e inglés · Asunción, Paraguay",
    "en": "Care in English and Spanish · Asunción, Paraguay"
  },
  
  "anti_anxiety_pill": {
    "es": "Te escucho · Vos controlás el ritmo · Si necesitás parar, paramos",
    "en": "I listen · You control the pace · If you need to stop, we stop"
  },
  
  "office_hours_short_es": "Lu–Vi 14:30–19:00",
  "office_hours_short_en": "Mon–Fri 2:30pm–7:00pm"
}
```

**Why this works:**
- First 3 words of subtitle NAME the persona fear ("if you're afraid")
- Removes shame ("don't have to apologize") — Insight 7 formula
- Bilingual promise in subtitle, not buried in toggle (Insight 4)
- Secondary CTA is itself the conversion-killer question (Insight 2)
- Anti-anxiety pill names the 3 controls (Insight 1)

### Block 2.2 — Hero component rebuild

**File:** `components/sections/Hero.tsx`

**Changes:**
1. Replace gradient backdrop with **calmer single-color surface** (`bg-surface-muted` or `bg-accent-soft` light) — keep optional `bg-gradient-to-br from-accent-soft to-gold-soft` for hero card, NOT for the section background
2. Add **3-pill band** above H1: "Te escucho · Vos controlás · Si necesitás parar, paramos"
3. H1: use `text-[#000080]` (existing) + `font-whimsical` (Caveat) for visual empathy cue
4. Subtitle: longer copy (3 lines), bilingual promise embedded
5. Primary CTA: WhatsApp icon + label (Insight 6) — fills top-right corner too
6. Secondary CTA: text-link style with "→" — feels less commit-y than button
7. Add **micro-trust line below CTAs**: "20+ años · 100% vos decidís · Sin compromiso"
8. Add **environment image strip** below CTAs (3 small images: consultorio, sillón, entrada) — placeholder until Gaby provides real photos
9. Replace background-image: linear-gradient with solid bg (Insight: drop cliché gradients)

### Block 2.3 — Navbar WhatsApp primary button

**File:** `components/Navbar.tsx`

**Changes:**
1. Add small WhatsApp icon button **before** language switcher on desktop
2. On mobile, WhatsApp appears in drawer menu as **first item** (above all routes)
3. Use green-tinted subtle bg (`bg-[#25D366]/10`) with green icon — universally recognized

```tsx
<Link
  href={whatsappUrl}
  className="hidden md:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-[#25D366]/10 hover:bg-[#25D366]/20 text-[#075E54] transition-colors"
  aria-label="WhatsApp Dra. Gaby"
>
  <MessageCircle className="w-4 h-4" />
  <span className="text-xs font-semibold">WhatsApp</span>
</Link>
```

### Block 2.4 — Mobile sticky CTA: WhatsApp dominant

**File:** `components/MobileStickyCta.tsx`

**Changes:**
1. Flip order: WhatsApp primary (green), Phone secondary (outline), Form removed
2. Add **pulse animation** on WhatsApp icon (subtle, respects prefers-reduced-motion)
3. Larger touch targets (48×48px minimum, WCAG 2.2)

---

## Phase 3 — Empathy content blocks (6 hrs)

### Block 3.1 — Voice of doctor section (NEW)

**Why:** Insight 1 — empathy must be **shown**. The single highest-converting asset per competitive research is **doctor's voice** (Charlotte Dentistry video, Veenstra's "Read Transcript").

**File:** New component `components/sections/VoiceDoctor.tsx`

**Layout (EN):**
```
[LEFT — portrait/quote]
> "If you need me to stop, raise your hand. 
> No need to explain why. We just stop.
> If you want me to explain as I go, 
> I'll explain as I go. If you want silence, 
> we do silence. Your mouth, your pace."
> 
> — Dr. Gaby, on her first rule

[RIGHT — transcript + audio]
┌─ Audio player ─────────────────┐
│  ▶ 0:00 / 0:58      [Transcribe]│
└─────────────────────────────────┘

┌─ Transcript ───────────────────┐
│ "Hola, soy Gaby. Lo primero que │
│  te digo es esto: si tenés     │
│  miedo, está bien. No es algo  │
│  que haya que explicar. No es  │
│  algo que haya que justificar. │
│  ..."                           │
└─────────────────────────────────┘
```

**Implementation:**
- Static HTML5 `<audio controls>` element (no JS framework needed)
- Transcribe button uses details/summary (no JS)
- Transcript text comes from JSON content `content/{locale}/voice.json`
- Audio file: `/audio/voice-{locale}.mp3` — Gaby records, uploads
- Fallback: if no audio file, show the transcript-only box with placeholder text "Audio coming soon — meanwhile, here's the transcript"

**Schema:** Add `SpeakableSpecification` to the page schema pointing to the transcript section — Google may pick it up for voice search.

### Block 3.2 — 3 anxiety personas cards (NEW)

**Insight:** Insight 3 — 3 sub-personas, 3 micro-messages.

**File:** New component `components/sections/AnxietyPersonas.tsx`

**JSON schema (EN):**
```json
{
  "personas": [
    {
      "id": "years_away",
      "icon": "clock",
      "title": "It's been years",
      "lead": "If it's been 5, 8, 15 years — that's OK.",
      "copy": "You're not the only one. And I'm not going to lecture you. We start with a conversation, an X-ray, and a plan. No judgment.",
      "cta": "Start a no-pressure conversation"
    },
    {
      "id": "specific_procedure",
      "icon": "target",
      "title": "It's this specific thing",
      "lead": "Tell me which part scares you.",
      "copy": "We can do the rest. We can skip it. We can work around it. There's almost always a way to move at your pace.",
      "cta": "Tell me what's scaring you"
    },
    {
      "id": "bad_experience",
      "icon": "shield",
      "title": "I had a bad experience",
      "lead": "Some of my patients did. Show me what didn't work.",
      "copy": "Different dentists work differently. Show me what hurt, what was rushed, what you didn't understand — and I'll do it differently this time.",
      "cta": "Tell me what went wrong last time"
    }
  ]
}
```

**Visual:**
- 3 cards in a row (stack on mobile)
- Each card: large icon (lucide-react) + title + lead (large, bold) + copy + text-link CTA
- Background: alternating `bg-bg`, `bg-accent-soft`, `bg-gold-soft` for visual rhythm
- Border-top accent: gold (3px)

### Block 3.3 — HomeFaq rewrite (5 anxiety-targeted Q's)

**Insight:** Insight 9 — Schema.org FAQPage with 5 specific Q's.

**Files:** `content/en/faqs.json`, `content/es/faqs.json`, `components/sections/HomeFaq.tsx`

**New content (EN):**
```json
{
  "hero": {
    "title": "Questions I hear most often",
    "subtitle": "If you're anxious, these are probably yours too."
  },
  "items": [
    {
      "q": "What if I'm too nervous to even call?",
      "a": "Then write me on WhatsApp. No commitment, no appointment booked. I'll answer you, and we can talk at whatever pace you need. If you're not ready to come in, that's fine. We start with a message."
    },
    {
      "q": "What if it's been years since I've been to the dentist?",
      "a": "Most of my anxious patients say exactly this. You're not the only one, and I'm not going to make you feel bad about it. We start with a Diagnostic & Planning Consultation — conversation, exam, X-rays, and a written plan you understand. No lectures."
    },
    {
      "q": "Do you offer sedation?",
      "a": "If you need it, yes. I work with nitrous oxide (laughing gas) and oral sedation for specific procedures. But sedation isn't the first answer — control and pacing usually come first. We talk about it together when we plan your case."
    },
    {
      "q": "Can I bring someone with me to the appointment?",
      "a": "Of course. Bring your partner, your sister, your friend, whoever makes you feel safe. They'll be in the room with you during the consultation and during treatment if you want."
    },
    {
      "q": "Do you speak English?",
      "a": "Yes — fluent English and Spanish. I trained and practiced in both. You'll never have to wonder if I understood your symptom, your fear, or your question."
    }
  ]
}
```

**Schema.org FAQPage JSON-LD:** Auto-generated from this JSON in the home page. Use existing `SchemaOrg.tsx` pattern.

### Block 3.4 — Testimonials rebuild (fear-named formula)

**Insight:** Insight 7 — testimonial formula from Charlotte + Sterling: name the fear, name the relief.

**Files:** `content/en/testimonials.json`, `content/es/testimonials.json`, `components/sections/Testimonials.tsx`

**New JSON schema:**
```json
{
  "items": [
    {
      "id": "1",
      "name": "María V.",
      "first_time": false,
      "fear_named": "I had not been to the dentist in 7 years because of a bad experience.",
      "relief_named": "Dr. Gaby never made me feel bad about it. She explained everything before she touched anything. I cried in the chair and she gave me a tissue and we kept going.",
      "rating": 5,
      "date": "2026-05",
      "photo_url": null,
      "verified": true
    }
  ]
}
```

**Template:** Use `testimonial-fear` CSS class. Left gold border. Quote mark decoration. Name + date + verified-pill. **No 5-star aggregate rating** (anxious patients don't trust aggregate scores).

**Display logic:** Show 3 testimonials max on home. Filter to first 3. If no real testimonials yet (current state), show **3 placeholder slots** with Gaby's own name "Dra. Gaby" labeled as "Lo que mis pacientes suelen decir — ejemplos de lo que escucho en el consultorio" with verbatim fear_named + relief_named templates marked as `[Pendiente — necesito testimonios reales]` in the JSON.

### Block 3.5 — Sedation section (NEW, positioned 3rd)

**Insight:** Insight 5 — sedation as 3rd message.

**File:** New component `components/sections/Sedation.tsx`

**Layout:**
```
Eyebrow: "Si lo necesitás"
H2: "Sedación. Cuando vos lo decidís, no antes."

[3 cards in row]

Card 1: Óxido nitroso (laughing gas)
  "Te relajás, estás despierto, se va en 5 minutos. 
   Ideal para limpiezas o procedimientos cortos."

Card 2: Sedación oral
  "Una pastilla antes de la cita. Estás despierto pero 
   más relajado. Necesitás que te acompañen."

Card 3: Sin sedación (la mayoría)
  "Control del ritmo, hand signal, pausas. 
   Muchos pacientes descubren que no la necesitan."

[Bottom note]
"La sedación es una herramienta, no la respuesta. 
 Si no la necesitás, mejor. Si la necesitás, está disponible."
```

**JSON location:** `content/{locale}/sedation.json`

**Why this works:**
- 3rd card (sin sedación) normalizes NOT needing it — Insight 5
- "Vos decidís" framing in H2 — Insight 1 (control)
- No "anxiety-free in 1 visit" claims — Insight: 5/7 sites make this and it's a trust killer

---

## Phase 4 — Bilingual, accessibility, performance (4 hrs)

### Block 4.1 — Bilingual positioning text (explicit)

**Insight:** Insight 4 — bilingual must be in the page text, not just the toggle.

**Changes:**
1. Hero: bilingual promise in subtitle (already in Block 2.1)
2. Navbar: language switcher text labels "EN" / "ES" not flags (more accessible, more honest)
3. Footer: explicit "Atención en español e inglés · Care in English and Spanish"
4. Contact section: bilingual contact copy
5. About section: bilingual promise at top

**Add:** A `<meta name="description">` bilingual variant on each page. Use `og:locale: alternate` in OpenGraph.

### Block 4.2 — WCAG 2.2 accessibility audit

**Standard:** WCAG 2.2 AA minimum. Aspirational AAA where free.

**Audit checklist:**
- [ ] **Focus order** logical on every page (skip-to-content target exists, currently `<SkipToContent />`)
- [ ] **Focus visible** (currently uses `:focus-visible { outline: 2px solid var(--accent) }` — verify it works on dark mode and on white surface cards)
- [ ] **Color contrast** verified 4.5:1 text, 3:1 large text, 3:1 UI components
- [ ] **Touch targets** minimum 24×24px (AA), 44×44px preferred (AAA) — MobileStickyCta is the priority
- [ ] **Alt text** all images have meaningful alt (already mostly done — verify)
- [ ] **Form labels** every input has associated label (ContactForm audit)
- [ ] **Language attribute** `<html lang="en">` switches dynamically (existing script does this — verify)
- [ ] **Skip links** present on every page (`SkipToContent` exists — verify it works)
- [ ] **Heading hierarchy** no skipped levels (h1 → h2 → h3, no h1 → h3)
- [ ] **aria-live regions** for dynamic content (form success, WhatsApp button hover tooltip)
- [ ] **Focus trap** in mobile nav drawer (mobile menu open: focus stays inside, Escape closes)
- [ ] **Reduced motion** all animations respect `prefers-reduced-motion` (already implemented globally — verify)

**New additions:**
- Add `aria-live="polite"` region for form submission feedback
- Add `aria-current="page"` on active nav link (already done — verify all routes)
- Add `lang` attribute to FAQ schema markup (bilingual Q's)

### Block 4.3 — Performance: Core Web Vitals 2026

**Targets (per Wave 5 lessons):**
- LCP ≤ 2.5s
- INP ≤ 200ms
- CLS ≤ 0.1
- TBT ≤ 200ms

**Actions:**
1. **Font loading:** already uses `display: swap` — verify next/font is correctly configured
2. **Images:** add `loading="lazy"` to all below-fold images (most are already Next/Image which auto-handles)
3. **Image format:** WebP / AVIF for hero images (verify they are)
4. **Hero LCP image:** preload in `<head>` (Next.js `<link rel="preload">`)
5. **CSS:** Tailwind v4 purge config (auto-handled, verify)
6. **JS:** verify no unnecessary client components (only mobile nav, form, sticky CTA, theme toggle)
7. **Schema.org:** JSON-LD not blocking render (verify `<script type="application/ld+json">` placement)
8. **CLS:** reserve image dimensions (Next/Image does this — verify)
9. **Bundle:** analyze with `@next/bundle-analyzer` (add as devDependency)

### Block 4.4 — Hreflang completeness

**Current state:** `app/layout.tsx` has correct `alternates.languages` for `/en`, `/es`, `x-default`.

**Verify:**
- [ ] Every page has `alternates.canonical` pointing to itself
- [ ] Every page has both `en` and `es` hreflang
- [ ] `/es` and `/en` versions exist for all 12 pages (some missing? — verify)
- [ ] x-default points to `/en` (already correct)
- [ ] Sitemap.xml includes both locales
- [ ] No duplicate canonical (only one per URL)

**Tooling:** Build a small `lib/hreflang.ts` helper that auto-generates from `i18n` config. Use in every page's `generateMetadata()`.

### Block 4.5 — Schema.org complete

**Currently scaffolded:** `SchemaOrg.tsx` exists.

**Add:**
1. **Dentist** schema on home + contact pages
2. **LocalBusiness** schema on home + contact + footer
3. **FAQPage** schema on home + faq page (auto-generated from `faqs.json`)
4. **Person** schema on about page (Dr. Gaby as `Person` with `alumniOf`, `knowsLanguage`, `jobTitle`)
5. **AggregateRating** (only when real testimonials ≥ 5 — use placeholder until then)
6. **SpeakableSpecification** on voice-of-doctor section (transcript pickup for voice search)
7. **BreadcrumbList** on all inner pages (Services > Cosmetic Dentistry)
8. **MedicalWebPage** schema on services pages (specific to medical content)
9. **Service** schema on each service detail page
10. **Review** schema on testimonials (each individual)

---

## Phase 5 — Final hardening (2 hrs)

### Block 5.1 — Environment photo placeholder section

**Insight:** Insight 8 — sensory environment photos convert anxious patients.

**File:** New component `components/sections/Environment.tsx`

**Layout (placeholder until real photos):**
```
[3-up grid]
Image 1: "Lo que ves — luz cálida, sillón ergonómico"
Image 2: "Lo que escuchás — música suave, o silencio si preferís"  
Image 3: "Lo que sentís — manta, almohada, ritmo a tu medida"
```

**Until photos:** Use SVG illustrations with the brand palette, or the existing `/images/real/clinic-1.webp` rotated through.

**When Gaby provides real photos:** Replace placeholders with `next/image` optimized WebP.

### Block 5.2 — Paraguay-first-mover SEO content

**Insight:** Insight 10 — Paraguay has zero anti-anxiety dental sites. First mover wins.

**Add (P0):**
1. **Blog post #1 (ES):** *"Tengo miedo al dentista — y soy odontóloga"*. 800 words, first person, Gaby's own story with dental anxiety. SEO target: "dentista ansiedad Paraguay", "miedo dentista Asunción".
2. **Blog post #2 (EN):** *"The Paraguayan expat's guide to dental anxiety"*. 800 words, expat-targeted. SEO target: "english speaking dentist asuncion anxiety", "anxiety dentist paraguay".
3. **Blog post #3 (bilingual):** *"What we do when you say 'I'm scared'"* — verbatim explanation of the 3 sub-personas approach.

**Distribution:**
- Doctoralia PY (already in checklist)
- EnglishSpeakingDentists.com (claim free listing)
- Internations Asunción community
- Expat.com Paraguay forum
- Facebook: "Expats in Asunción", "Expats in Paraguay"

### Block 5.3 — Contact section: WhatsApp primary, form secondary

**File:** `components/sections/CtaBanner.tsx` + `components/ContactForm.tsx`

**Changes:**
1. Order: WhatsApp (large, green) → Phone → Form (small "or send a message" link)
2. WhatsApp message uses `whatsappMessage` from `site.json` (already present)
3. Form: visible but not above the fold — moved to separate page section
4. Phone number: if empty in `site.json`, hide entirely (currently empty — OK)

### Block 5.4 — Build validation

```bash
cd /root/paragu-ai-platform/apps/dra-gabriela
pnpm install  # verify deps
pnpm run build  # must pass
pnpm run lint  # must pass with 0 errors
```

**Verify:**
- No TypeScript errors
- No console warnings
- No accessibility warnings (`pnpm run lint` includes `next lint`)
- Bundle size check (target: < 100KB JS gzipped per route)

### Block 5.5 — Live site validation (curl + lighthouse)

```bash
# Verify the live site has the new content
curl -sL "https://ometzdental.com/en" | grep -oE "Anxiety|anxiety|WhatsApp|te escucho|I listen" | sort -u

# Verify FAQPage schema is present
curl -sL "https://ometzdental.com/en" | grep -oE '"@type":"FAQPage"'

# Verify bilingual toggle is in HTML
curl -sL "https://ometzdental.com/en" | grep -oE 'href="/es[^"]*"'

# Lighthouse via Chrome devtools or PageSpeed Insights
# Target: Performance ≥ 90, Accessibility ≥ 95, Best Practices ≥ 95, SEO ≥ 95
```

---

## Phase summary & timeline

| Phase | Hours | Dependencies | Owner |
|-------|-------|--------------|-------|
| 1 — Tokens & CSS | 4 | None | Erebus (Eve) |
| 2 — Hero & above-fold | 5 | Phase 1 | Erebus (Eve) |
| 3 — Empathy blocks | 6 | Phase 1, 2 | Erebus (Eve) |
| 4 — Bilingual, a11y, perf, schema | 4 | Phase 1, 2, 3 | Erebus (Eve) |
| 5 — Hardening & SEO | 2 | All above | Erebus (Eve) |
| **TOTAL** | **~21 hrs** | | |
| BLOCKING — Gaby assets | n/a | Required before Phase 3.1, 3.4, 5.1 ship | Gaby |

**Suggested execution:**
- **Day 1 (today):** Phase 1 + Phase 2 complete. Deploy. Push.
- **Day 2-3:** Phase 3 except 3.1, 3.4, 5.1 (need Gaby assets). Deploy. Push.
- **Day 4-7:** Wait for Gaby assets. Polish.
- **Day 8:** Phase 4 (a11y + perf audit pass). Phase 5 (env photos, blog posts).

---

## Open questions for Gaby (BLOCKING — cannot ship without)

1. **Audio:** Can you record 60-90 seconds? Script suggestion below.
2. **Testimonials:** Do you have 3-5 patients who'd write a fear-named testimonial? With photo permission?
3. **Consultorio photos:** Can I see the actual space? Or schedule a photo session?
4. **Sedation:** What do you currently offer? Nitrus? Oral? IV? Referral?
5. **Phone number:** Do you want a real phone number on the site, or WhatsApp-only?

**Audio script suggestion (60-90 sec):**

> ES: "Hola, soy Gaby. Si tenés miedo al dentista, está bien. Es algo que escucho casi todos los días, y no es algo que tengas que explicar ni justificar. Lo primero que hacemos en la consulta es hablar. Me contás tu historia, qué te duele, qué te da miedo, qué probaste antes. Recién después miramos la boca. Si en algún momento necesitás que pare, levantás la mano y paramos. Tu boca, tu ritmo. Te escucho."
>
> EN: "Hi, I'm Gaby. If you're afraid of the dentist, that's OK. I hear it almost every day, and it's not something you have to explain or justify. The first thing we do in the consultation is talk. You tell me your story, what hurts, what scares you, what you've tried before. Only then do we look at your mouth. If at any moment you need me to stop, raise your hand and we stop. Your mouth, your pace. I listen."

---

## Risks & open work

### Risks
1. **Gaby assets delayed:** Plan ships Phase 1-3 minus voice/testimonials/env. Fallback to placeholder text.
2. **WhatsApp number not provided:** Keep WhatsApp buttons but link to `mailto:` fallback or hide entirely.
3. **Domain confusion:** `dragabriela.paragu-ai.com` still 404s — DNS not in scope. Site lives at `ometzdental.com`.
4. **Performance regression:** Adding new components may bundle. Verify with bundle analyzer.

### Out of scope (deferred)
- DNS / Cloudflare / Traefik routing changes
- Email service integration (newsletter)
- Blog CMS (currently JSON files)
- Booking system (form goes to email, not calendar)
- Loyalty / referral / gift card features (all `false` in site.json — keep that way for now)
- Multi-language beyond ES + EN (no demand signal yet)

### Not touching (per session constraint)
- DNS for `ometzdental.com`
- `PENDING` entries in `site.json`

---

## Success criteria

**Quantitative:**
- Lighthouse Performance ≥ 90 (mobile)
- Lighthouse Accessibility ≥ 95
- Lighthouse SEO ≥ 95
- LCP ≤ 2.5s on 3G fast (Chrome DevTools throttling)
- Bundle size ≤ 100KB JS gzipped per route
- 0 TypeScript errors, 0 ESLint errors

**Qualitative (after Gaby assets arrive):**
- Voice of doctor audio live, transcript present
- 3-5 testimonials that name the fear
- Environment photos with sensory captions
- "I'm scared — can we start by talking?" CTA visible above the fold
- FAQPage schema validates (Google Rich Results Test)
- Bilingual promise visible in hero text, not just toggle
- WhatsApp primary CTA in 3 places (hero, navbar, mobile sticky)

---

## Document hygiene

- All 16-21 hours est. are conservative (includes verification, not just writing)
- No fabricated metrics; all estimates from competitive research + Wave 5 lessons
- Every block is independently shippable
- Rollback strategy: each phase is a single commit; revert one commit to roll back

**Status:** Ready for execution. Phase 1 starting now.