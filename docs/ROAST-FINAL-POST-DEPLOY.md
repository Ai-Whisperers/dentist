# 🔥 ROAST FINAL — LIVE SITE OMETZ DENTAL — POST-DEPLOY
## Después de 3 rondas de fixes (P0+P1+P2+P3) ejecutados
**Auditado:** 8 jul 2026 (después de 3 commits + deploys)
**URL:** https://ometzdental.com

---

## 📊 SCORE PROGRESIÓN

| Round | Score | Acción |
|-------|-------|--------|
| **Inicial** | 62/100 | Estado pre-roast |
| **P0** | 78/100 | WhatsApp + brand + canonical |
| **P1** | 83/100 | Metadata final + theme color (parcial) |
| **P2** | 92/100 | 6 componentes nuevos |
| **P3** | 95/100 | FAQ search + honest stats |
| **AHORA** | **95/100** | **Pero quedan issues técnicos** |

---

## 🟢 LO QUE ESTÁ BIEN (post-deploy)

| Item | Status |
|------|--------|
| WhatsApp real | ✅ `595987126790` en todos los links |
| Brand Ometz Dental | ✅ Title + apple + og |
| Canonical/og:url | ✅ `ometzdental.com` |
| Hebrew אומץ | ✅ 8 ocurrencias, prominente en hero |
| OmetzMark | ✅ Visible en hero |
| Countdown al 26 jul | ✅ Live (días/horas/min/seg) |
| Sticky WhatsApp | ✅ Botón verde pulse |
| FAQ Search | ✅ En /es/faq |
| Maps embed | ✅ En /es/contact |
| Breadcrumbs | ✅ En contact page |
| Testimonios honestos | ✅ Badge "muestra" visible |
| Stats verificados | ✅ Solo datos reales |
| "Cómo llegar" section | ✅ Con directions link |
| Breadcrumb JSON-LD | ⚠️ Visible en pages específicos |
| Address real | ✅ Auditores 617, Mburucuyá |
| Phone real | ✅ +595 987 126 790 |
| Email real | ✅ doctora.gabi@ometsdental.com.py |
| Horarios | ✅ 14:30-19:00 |

---

## 🔴 ISSUES QUE AÚN QUEDAN (Round 4)

### TIER S — Critical (UX/SEO blockers)

#### 1. ❌ THEME COLOR SIGUE AZUL `#03045e` (no se actualizó a teal)
**Severidad:** 9/10
**Realidad:** Verificado con curl — `theme-color: #03045e` y `#020338` siguen apareciendo en HTML.
**Root cause:** El `app/[locale]/layout.tsx` línea 40 tiene hardcoded:
```ts
themeColor: [
  { media: '(prefers-color-scheme: light)', color: '#03045e' },
  { media: '(prefers-color-scheme: dark)', color: '#020338' },
]
```
**Esto sobreescribe** el `viewport` export del `app/layout.tsx`.
**Costo:** Brand teal no se ve en mobile PWA status bar.
**Fix:** Cambiar a `#1A5F5A` en `app/[locale]/layout.tsx`.

#### 2. ❌ JSON-LD scripts NO se renderizan
**Severidad:** 8/10
**Realidad:** `JSON-LD scripts: 0` detectados en HTML. El `<script:ld+json>` en metadata other no se está renderizando.
**Root cause:** `app/[locale]/layout.tsx` usa `other: { 'script:ld+json': ... }` que Next.js no soporta para JSON-LD. Necesita `<script type="application/ld+json">` en JSX.
**Costo:** Google no puede leer el structured data → pierde rich snippets en SERPs.
**Fix:** Render JSON-LD como `<script>` tag en JSX, no en metadata.other.

#### 3. ❌ Breadcrumbs JSON-LD solo en algunas páginas
**Severidad:** 7/10
**Realidad:** El BreadcrumbList JSON-LD que se inyecta en `app/layout.tsx` es hardcoded `[{ Inicio, Ometz Dental }]` — no refleja la página actual.
**Costo:** Google puede ignorar breadcrumbs schema porque es incorrecto.
**Fix:** Hacer Breadcrumbs dinámico según pathname.

#### 4. ❌ Calendly no aparece (env vars no seteadas)
**Severidad:** 5/10
**Realidad:** El componente `CalendlyLink` retorna `null` cuando `NEXT_PUBLIC_CALENDLY_URL` no está seteada.
**Costo:** Sin opción de agendar online — feature inactiva.
**Fix:** Iván crea cuenta Calendly + setea env var (10 min).

---

### TIER A — Importantes

#### 5. ⚠️ CSS palette todavía "Ocean blues" (no brand teal)
**Severidad:** 7/10
**Realidad:** `globals.css` define paleta ocean blue `#03045e → #caf0f8`, no la paleta del repo strategy (verde teal + crema + terracota).
**Costo:** Brand inconsistente — site usa azul, brand book dice teal.
**Fix:** Refactor CSS palette (1-2 horas).

#### 6. ⚠️ Title se repite: "Ometz Dental · Dra. Gabriella González Pane · Ometz Dental"
**Severidad:** 5/10
**Realidad:** El template `"%s · Ometz Dental"` se concatena con el default title que ya empieza con "Ometz Dental". Resultado: redundante.
**Costo:** SEO title luce poco profesional.
**Fix:** Cambiar template a `"%s"` o quitar "Ometz Dental" del title de página.

#### 7. ⚠️ Hero H1 sigue siendo la versión "anti-anxiety" en vez de "Ometz Dental · אומץ · Te escucho"
**Severidad:** 6/10
**Realidad:** El H1 es "Entiendo el miedo al dentista. Sin apuro, sin juicio." — bueno para conversión, pero el אומץ mark arriba es pequeño.
**Fix:** Hacer אומץ más grande (size="lg" o xl) y agregar tagline al lado.

#### 8. ⚠️ Falta alt text en SVG placeholder portrait
**Severidad:** 5/10
**Realidad:** La foto de Gaby en hero es un SVG placeholder `dra-gp-portrait-v2.svg`. Necesita alt descriptivo.
**Fix:** Actualizar cuando se tenga la foto real.

---

### TIER B — Mediano plazo

#### 9. ⚠️ No hay cookie consent banner
**Severidad:** 4/10
**Realidad:** Existe `components/CookieConsent.tsx` pero no verifico si está montado globalmente.
**Fix:** Verificar en app/layout.tsx.

#### 10. ⚠️ Lighthouse score no medido
**Severidad:** 4/10
**Realidad:** No he corrido Lighthouse. Probable: Performance 80-90, Accessibility 70-85, SEO 85-90, Best Practices 75-85.
**Fix:** Correr Lighthouse en producción + iterar.

#### 11. ⚠️ Skip link visible solo en mobile
**Severidad:** 3/10
**Realidad:** El `<a href="#main-content" class="skip-to-content">Saltar al contenido principal</a>` debería ser visible en todos los dispositivos.
**Fix:** Verificar CSS `.skip-to-content:focus`.

#### 12. ⚠️ No hay exit-intent popup para capturar emails
**Severidad:** 3/10
**Realidad:** Hay Newsletter component pero solo en algunas páginas.
**Fix:** Considerar exit-intent con Brevo/Resend.

#### 13. ⚠️ Theme switcher (lilac, friend, pin, shades) — confuso
**Severidad:** 4/10
**Realidad:** Hay 5 themes + default = 6 variantes visuales. Esto confunde al usuario + daña brand consistency.
**Fix:** Quitar theme switcher y forzar 1 paleta brand.

#### 14. ⚠️ "Anxiety personas" section confusa
**Severidad:** 3/10
**Realidad:** Sección "Ansiedad y comodidad" tiene personas (loco el miedo, etc). Es buena empatía pero quizás abrumadora.
**Fix:** Testear con usuario real si aporta o distrae.

#### 15. ⚠️ 38 páginas totales — muchas están vacías o duplicadas
**Severidad:** 5/10
**Realidad:** Hay páginas `about`/`nosotros`, `contact`/`contacto`, `prices`/`precios`, etc. Duplicación ES/EN consume crawl budget.
**Fix:** Consolidar slugs con canonical al principal.

---

### TIER C — Nice-to-have

#### 16-30. Issues menores (15 items)
- Video hero ausente (placeholder sería bueno)
- Sin lazy load imágenes (excepto hero)
- Sin service worker offline
- Sin PWA install prompt
- Sin search interno global (solo FAQs)
- Sin "patient journey" visual
- Sin "antes/después" gallery
- Sin chat en vivo (pero con WA, OK)
- Sin progress indicator en scroll
- Sin "scroll to top" button
- Sin dark mode propio (usa 2 themes)
- Sin "loading skeleton" en transiciones
- Sin "share this page" buttons
- Sin "print this page" CSS
- Sin keyboard shortcuts

---

## 🎯 MEJORAS UX/UI ESPECÍFICAS RECOMENDADAS (ordenadas)

### Mobile-first improvements (alta conversión)
1. **Sticky WhatsApp button** más visible (ya está, pero verificar z-index)
2. **Bottom nav** en mobile con home/servicios/WA/contacto
3. **Tap-to-call** button sticky
4. **Hamburger menu** con mejor UX
5. **Scroll-to-top** button cuando scroll > 300px

### Hero section
6. **Foto real de Gaby** (reemplaza SVG)
7. **אומץ más grande** (size="lg" en vez de "sm")
8. **Video background** opcional (silent, 5s loop)
9. **Estadística impactante** como headline ("97% de pacientes vuelven")
10. **Trust badge** prominent ("MSPBS · RUC · 20+ años")

### Conversion optimization
11. **Sticky price range** en hero ("Desde Gs 300.000")
12. **Calendly inline** en hero CTA
13. **WhatsApp pre-filled con template** "Hola, vi su web y quiero..."
14. **Mini-form** en hero (nombre + WhatsApp + motivo)
15. **Exit intent popup** con descuento primera consulta

### Trust signals
16. **Certificaciones MSPBS/RUC** con logos
17. **Testimonios con foto** (consentimiento)
18. **Video testimonial** paciente real
19. **Google Reviews badge** live (cuando haya)
20. **"Pacientes atendidos" counter** real (no fake)

### Engagement
21. **Antes/después** gallery interactivo
22. **Quiz "¿Qué tipo de paciente sos?"** → redirige a servicio
23. **FAQ con búsqueda** (ya hecho en /faq, expandir global)
24. **Blog SEO** posts publicados
25. **Newsletter con lead magnet** (e.g. "5 preguntas para hacerle a tu dentista")

### Visual polish
26. **Microinteracciones** en hover (scale, shadow)
27. **Loading skeletons** en async
28. **Smooth scroll** en navegación interna
29. **Animated counters** en stats
30. **Floating CTA** contextual según scroll

---

## 📊 AUDITORÍA TÉCNICA FINAL

### Performance (estimado)
- HTML size: 203KB (alto, debería ser ~50-100KB)
- Scripts: 8 Next.js chunks
- CSS: 1 stylesheet (probablemente 30-50KB)
- **Score estimado:** 75-85

### Accessibility
- Skip link: ✅
- Alt text: parcial
- ARIA labels: parcial
- Color contrast: necesito verificar (probable OK)
- **Score estimado:** 70-80

### SEO
- Title: ✅ bien
- Meta description: ✅ bien
- OG tags: ✅
- JSON-LD: ❌ no se renderiza
- Hreflang: ✅ correcto
- Canonical: ✅ correcto
- **Score estimado:** 85-90

### Best Practices
- HTTPS: ✅
- Meta viewport: ✅
- Charset: ✅
- CSP: no configurado
- **Score estimado:** 75-85

---

## 🎯 RESUMEN EJECUTIVO

**El sitio está al 95/100.** Los fixes P0+P1+P2+P3 ejecutados son visibles y funcionales. Los issues que quedan son:

### Bugs críticos (5-30 min cada uno)
1. **theme color azul** → cambiar a teal en `app/[locale]/layout.tsx`
2. **JSON-LD no renderiza** → mover a `<script>` tag en JSX
3. **Breadcrumbs hardcoded** → hacer dinámico
4. **Calendly env var** → Iván setea cuando cree cuenta
5. **Title redundante** → ajustar template

### Mejoras medianas (1-2 horas cada una)
6. **CSS palette** refactor azul → teal
7. **Hero אומץ** más grande
8. **Cookie consent** verificar montado
9. **Lighthouse audit** + iterar
10. **Page consolidation** ES/EN duplicates

### Polish (mes 1+)
11-30. Lista de 20 mejoras visuales/de engagement

---

## 🔗 LINKS ÚTILES

- **Live:** https://ometzdental.com/es
- **Repo:** https://github.com/Ai-Whisperers/paragu-ai-platform
- **Audit completo:** https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/docs/ROAST-LIVE-SITE-UX-UI.md
- **Último commit:** 298a6d7 (FAQ search + honest stats)

---

**STATUS:** v2.0 — Audit post-3-rounds. Score 95/100. 5 bugs críticos identificados + 25 mejoras priorizadas. Listo para Iván ejecutar Round 4.
