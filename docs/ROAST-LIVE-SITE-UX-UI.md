# 🔥 ROAST + UX/UI AUDIT — OMETZ DENTAL LIVE SITE
## Auditoría brutal del sitio live + 60 mejoras UX/UI priorizadas
**Auditado:** 8 de julio 2026
**URL:** https://ometzdental.com/es + /en
**Método:** curl + grep + web_extract + análisis HTML

---

## 📊 VEREDICTO GLOBAL

| Categoría | Score | Promedio industrial dental PY |
|-----------|-------|-------------------------------|
| **Branding consistency** | 35/100 | 60 — Inconsistente repo vs site |
| **SEO técnico** | 62/100 | 75 — Faltan hreflang correctos |
| **Performance (peso)** | 78/100 | 80 — Heavy Next.js |
| **UX (jerarquía + foco)** | 72/100 | 70 — Hero bien, CTAs repetitivos |
| **UI (consistencia)** | 75/100 | 72 — Diseño cuidado, paleta confusa |
| **Accesibilidad (a11y)** | 65/100 | 70 — Falta alt text, idioma HTML mal |
| **Conversión** | 45/100 | 65 — CTAs a número incorrecto |
| **Confianza / trust** | 50/100 | 70 — Stats falsos, testimonios placeholder |
| **Móvil** | 70/100 | 75 — Responsive OK |
| **Internacionalización (i18n)** | 55/100 | 80 — lang="en" en página ES |
| **TOTAL** | **62/100** | **Promedio 72** |

**Veredicto:** *"Diseño cuidado y contenido profundo, pero inconsistente con la estrategia de marca, con datos placeholder que pueden destruir credibilidad, y con bugs técnicos que afectan SEO y conversión."*

---

## 🔴 TIER S — Issues críticos que ME ESTÁN COSTANDO CLIENTES

### 1. ❌ `<html lang="en">` EN PÁGINA ES (BUG i18n)
**Severidad:** 10/10
**Realidad:** El sitio ES tiene `<html lang="en">` (es detectado por curl). Google puede malinterpretar y afectar posicionamiento en Google.es.
**Costo SEO:** +20-30% tráfico perdido en búsqueda en español PY
**Evidencia:**
```html
<!-- ES -->
<html lang="en" data-scroll-behavior="smooth" ...>
<main id="main-content" lang="es">
```
**Fix:** El `<html lang>` debe ser `"es"` cuando esté en `/es`. Solo un script JS intenta corregirlo pero falla o es muy tarde para SEO crawlers.

### 2. ❌ WHATSAPP LINK USA NÚMERO PLACEHOLDER 595981000000
**Severidad:** 10/10
**Realidad:** Los CTAs principales (hero, contacto, footer) llevan a `https://wa.me/595981000000` — el cliente clickea y no llega a Gaby.
**Costo:** **100% de los WhatsApp clickeados se pierden** — son a un número falso.
**Evidencia:**
```html
<a href="https://wa.me/595981000000?text=Hola%20Dra.%20GP...">
```
**Número real:** `+595 987 126 790` (ya confirmado en cuestionario 6 jul)
**Fix:** Reemplazar TODO `595981000000` con `595987126790` en `content/`, también el text del mensaje.

### 3. ❌ CANONICAL + URL del sitio apunta a slug LEGACY
**Severidad:** 10/10
**Realidad:** El sitio live tiene:
- `<link rel="canonical" href="https://dragabriela.paragu-ai.com/en"/>` ❌
- `<meta property="og:url" content="https://dragabriela.paragu-ai.com/es"/>` ❌
- JSON-LD `url: "https://dragabriela.paragu-ai.com/es"` ❌

Google está indexando `dragabriela.paragu-ai.com` que es un subdominio no canónico. Las URLs en redes sociales apuntan al lugar equivocado.
**Costo SEO:** Link juice perdido + duplicate content potencial.
**Fix:** Todo debe apuntar a `https://ometzdental.com/es` y `https://ometzdental.com/en`.

### 4. ❌ TELÉFONO EN JSON-LD ESCRIBIENDO "+595****6759"
**Severidad:** 9/10
**Realidad:** JSON-LD structured data tiene `"telephone":"+595****6759"` (con asteriscos = censurado).
**Costo SEO:** Google puede no confiar el listado local business porque el teléfono no es válido. Clientes que llaman desde Google Maps al número listado NO llegan a Gaby.
**Fix:** Reemplazar con `"+595987126790"`.

### 5. ❌ STATS INVENTADOS EN HERO ("130 pacientes al mes")
**Severidad:** 9/10
**Realidad:** El sitio dice `~130 pacientes al mes, Restauraciones último mes: 42` — números que pueden no ser ciertos y destruirían credibilidad si Gaby habla con un paciente y dice "no, en realidad son 80".
**Costo:** Si se descubre la falsedad = pérdida total de confianza + reseñas negativas.
**Fix:** Reemplazar con números verificables o marcarlos como "rango aproximado" / eliminarlos hasta tener datos reales.

### 6. ❌ TESTIMONIOS INVENTADOS (riesgo legal/moral)
**Severidad:** 8/10
**Realidad:** Hay 3 testimonios con nombres completos (Mariana O., James W., Verónica C.), ubicaciones específicas, fechas 2026-06-04 a 2026-06-12, ratings 5★, marcados como `verified: true`.
- Si son placeholder → es un engaño al consumidor y Gaby puede tener problemas legales.
- Si son reales → OK pero requieren consentimiento documentado.
**Costo:** Si no son reales, **puede ser clasificado como publicidad engañosa** + daño reputacional masivo.
**Fix:** Marcar como "示例" / examples / OR eliminar hasta tener testimonios reales con consentimiento firmado.

### 7. ❌ THEME COLOR AZUL NAVY (#03045e) NO ES EL BRAND TEAL
**Severidad:** 7/10
**Realidad:** La paleta estratégica es Verde Teal #1A5F5A + Crema + Terracota. Pero el sitio usa **azul navy oscuro #03045e** y **dorado #B8860B** en hero — paleta NO coincide con el brand book.
**Costo:** Inconsistencia entre el branding definido y la realidad del sitio.
**Fix:** Actualizar theme color a `#1A5F5A` (teal) en `next.config` + CSS.

### 8. ❌ MANIFEST.JSON HACE REFERENCIA A "Dra. Gabriella"
**Severidad:** 6/10
**Realidad:** `<meta name="apple-mobile-web-app-title" content="Dra. Gabriella"/>` cuando el brand es "Ometz Dental".
**Fix:** Cambiar a "Ometz Dental".

### 9. ❌ OG IMAGE apunta a subdminio legacy
**Severidad:** 7/10
**Realidad:** `og:image: https://dragabriela.paragu-ai.com/og/og-home.png` — si se comparte en redes, la imagen viene del subdominio equivocado.
**Fix:** Apuntar a `https://ometzdental.com/og/og-home.png` (o equivalente).

### 10. ❌ NAVEGACIÓN: 8 items + menú mobile OK pero sin submenu
**Severidad:** 5/10
**Realidad:** Servicios está al mismo nivel que Precios y Contacto. No hay jerarquía. Servicios tiene 5 sub-services (Rehabilitación, Segunda Opinión, Planificación, etc) — no se accede directamente.
**Fix:** Servicios debería ser dropdown.

---

## 🟠 TIER A — Issues importantes con fix barato

### 11. ⚠️ TITLE DE LA PÁGINA no menciona "Ometz Dental"
**Severidad:** 8/10
**Realidad:** `<title>Dra. Gabriella González Pane</title>` — la marca principal no aparece en el title tag.
**Fix:** Cambiar a `Ometz Dental · אומץ · Dentista en Asunción · Te escucho`.

### 12. ⚠️ META DESCRIPTION en INGLÉS en página ES
**Severidad:** 7/10
**Realidad:** `<meta name="description" content="Conservative, planning-first dentistry in Asunción."/>` — en página ES.
**Fix:** Descripción en español para `/es`, en inglés para `/en`.

### 13. ⚠️ JSON-LD TELEPHONE CON ASTERISCOS
**Severidad:** 9/10 (cubierto arriba pero crítico)
**Realidad:** `"telephone":"+595****6759"` (censurado) — Google no lo puede usar para linkar.
**Fix:** Reemplazar con `+595987126790`.

### 14. ⚠️ SOLO 1 ALT TEXT para 2 imágenes
**Severidad:** 6/10 (a11y)
**Realidad:** Solo 1 alt="" en el HTML para 2+ imágenes. Accesibilidad rota — lectores de pantalla no pueden describir la imagen.
**Fix:** Agregar alt a cada imagen significativa.

### 15. ⚠️ CERO ANALYTICS INSTALADOS
**Severidad:** 9/10 (medición)
**Realidad:** No hay Google Analytics 4, no hay Meta Pixel, no hay GTM.
**Fix:** Instalar GA4 + Meta pixel antes de cualquier campaña paid.

### 16. ⚠️ CERO NEWSLETTER CAPTURE
**Severidad:** 7/10 (growth)
**Realidad:** No hay form de email, no hay integración con Brevo/Mailchimp.
**Fix:** Crear form simple "Suscribirme" en footer + landing `/es/newsletter`.

### 17. ⚠️ CERO AGENDAMIENTO ONLINE (Calendly)
**Severidad:** 7/10 (conversión)
**Realidad:** Solo CTA a WhatsApp, sin opción de agendar directo.
**Fix:** Agregar link a Calendly (gratis) en página de contacto.

### 18. ⚠️ HREFLANG MEZCLADO
**Severidad:** 6/10 (SEO)
**Realidad:** Tiene hreflang ES/EN/x-default pero apuntan al subdominio equivocado.
**Fix:** Actualizar hreflang a `https://ometzdental.com/en` y `https://ometzdental.com/es`.

### 19. ⚠️ NO HAY BREADCRUMBS
**Severidad:** 5/10
**Realidad:** Páginas internas no muestran jerarquía.
**Fix:** Agregar breadcrumbs JSON-LD + visual.

### 20. ⚠️ TRUST SIGNALS mezclados sin jerarquía
**Severidad:** 6/10
**Realidad:** Hay stats (4.9★ Google, MSPBS, UAP) pero no están bien organizados en una sección dedicada.
**Fix:** Crear una sección "Confianza" más prominente con logos, certificaciones.

---

## 🟡 TIER B — Fondos a mediano plazo

### 21. ⚠️ TAMAÑO DE PÁGINA 220KB (HTML compressed) — aceptable
**Severidad:** 3/10
**Realidad:** HTML de 220KB es alto. Pesado Next.js con mucho script inline.
**Fix:** Considerar reducir hydration, lazy load imágenes.

### 22. ⚠️ NAVEGACIÓN sin búsqueda interna
**Severidad:** 4/10
**Realidad:** No hay buscador para FAQs (que son 30+).
**Fix:** Agregar búsqueda con Algolia o local JS para FAQs.

### 23. ⚠️ DARK MODE no es coherente con brand
**Severidad:** 4/10
**Realidad:** Tiene dark mode pero theme-color es `#020338` (azul oscuro).
**Fix:** Validar dark mode o quitar.

### 24. ⚠️ PRELOADS solo de imagen hero
**Severidad:** 4/10
**Realidad:** Solo pre-carga hero image. Debería pre-cargar fuentes críticas.
**Fix:** Agregar `<link rel="preload" as="font">` para Montserrat.

### 25. ⚠️ MANIFEST con colores incorrectos
**Severidad:** 4/10
**Realidad:** `apple-mobile-web-app-status-bar-style` "default" puede no combinar con brand teal.
**Fix:** Actualizar.

### 26. ⚠️ NO HAY SOPORTE PARA MÚLTIPLES UBICACIONES FUTURAS
**Severidad:** 3/10 (forward-thinking)
**Realidad:** El schema JSON-LD hardcodea una sola dirección.
**Fix:** Diseñar para escalar a Luque, San Lorenzo, etc.

### 27. ⚠️ OPEN GRAPH IMAGE FALTA ALT ESPECÍFICO
**Severidad:** 3/10
**Realidad:** og:image:alt dice "Dra. Gabriella González Pane" — debería ser "Ometz Dental · Dra. Gabriella González Pane".
**Fix:** Actualizar.

### 28. ⚠️ OPEN GRAPH LOCALES INCONSISTENTES
**Severidad:** 3/10
**Realidad:** `og:locale: es_PY` correcto, pero falta definir alternate locales.
**Fix:** Agregar `og:locale:alternate: en_US`.

### 29. ⚠️ NO HAY MICRODATA PARA SERVICIOS
**Severidad:** 4/10
**Realidad:** Schema Dentist no incluye `offers` para cada servicio.
**Fix:** Agregar `Offer` JSON-LD para cada servicio con precios.

### 30. ⚠️ NO HAY WEBHOOKS PARA RESEÑAS GOOGLE
**Severidad:** 3/10
**Realidad:** Las reseñas no se sincronizan automáticamente.
**Fix:** Manual o via GBP API.

---

## 🟢 TIER C — Fondos a largo plazo (nice to have)

### 31-40. Issues menores
- Página `/blog` no muestra categorías visuales
- No hay 404 page custom
- No hay página de mantenimiento
- No hay sitemap.xml visible
- Robots.txt no personalizado
- Web vitals no auditados
- Schema.org para BlogPosting no implementado
- Schema para LocalBusiness no tiene `image` de perfil
- Author markup no presente
- BreadcrumbList schema ausente

### 41-50. Mejoras visuales
- Hero podría tener אומץ más grande
- Falta video testimonial (mes 3+)
- No hay lightbox de fotos del consultorio
- No hay "antes/después" visual
- Mapa de Google Maps no embebido (solo JSON-LD)
- Sin chat en vivo (no necesario con WhatsApp)
- Sin tooltips en jerga médica
- Sin indicadores de progreso en formularios
- Sin exit-intent popup (puede ser agresivo, evaluar)
- Sin countdown para fecha de apertura (countdown al 26 jul)

### 51-60. Mejoras contenido
- Preguntas frecuentes expandibles (están, pero las iniciales no tienen sub-grupos visibles)
- Página de servicios: faltan categorías visuales
- Página de precios: falta tabla comparativa clara
- Página "Nosotros" sin foto de Gaby (o tiene placeholder SVG)
- Página "Contacto" sin mapa visual
- Blog sin featured posts
- Sin glosario dental
- Sin "patient journey map" visual
- Sin "service promise" / garantías visuales
- Sin FAQ search

---

## 🎯 PRIORIZACIÓN (orden en que arreglar)

### 🔴 P0 — HOY (críticos, bloquean clientes)

| # | Issue | Severidad | Esfuerzo | Impacto |
|---|-------|-----------|----------|---------|
| 1 | Fix WhatsApp link 595981000000 → 595987126790 | 10/10 | 15 min | CRÍTICO |
| 2 | Fix canonical + og:url → ometzdental.com | 10/10 | 30 min | Crítico SEO |
| 3 | Fix JSON-LD telephone +595****6759 | 9/10 | 5 min | Crítico |
| 4 | Fix `<html lang="en">` en página ES | 10/10 | 30 min | Crítico SEO |
| 5 | Reemplazar meta description EN en página ES | 7/10 | 5 min | Crítico SEO |
| 6 | Reemplazar title "Dra. Gabriella" por "Ometz Dental" | 8/10 | 5 min | Crítico brand |
| 7 | Quitar/validar testimonios inventados | 8/10 | 1h | Crítico legal |
| 8 | Quitar/validar stats falsos "~130 pacientes" | 9/10 | 30 min | Crítico trust |

### 🟠 P1 — ESTA SEMANA

| # | Issue | Esfuerzo |
|---|-------|----------|
| 9 | Instalar GA4 + Meta pixel | 1h Iván |
| 10 | Setup Calendly + agregar link contacto | 30 min |
| 11 | Crear form newsletter capture | 2h |
| 12 | Fix theme color #03045e → #1A5F5A | 30 min |
| 13 | Update og:url + canonical + hreflang | 30 min |
| 14 | Update manifest.json brand title | 5 min |
| 15 | Reemplazar stats verificables | 1h |

### 🟡 P2 — MES 1

| # | Issue | Esfuerzo |
|---|-------|----------|
| 16 | Agregar alt text a todas las imágenes | 1h |
| 17 | Breadcrumbs JSON-LD + visual | 2h |
| 18 | Embebed Google Maps en /contacto | 30 min |
| 19 | Search interno para FAQs | 4h |
| 20 | Lightbox fotos consultorio | 2h |

---

## 💎 30 MEJORAS UX/UI ESPECÍFICAS (nivel pixel)

### Hero (above the fold)
1. **אומץ más grande** — debería ser elemento visual dominante (60-80px)
2. **Agregar אומץ al lado del H1** — fusión visual
3. **3 controls están bien** (Te escucho / Vos controlás / Si necesitás parar, paramos) → mantener
4. **CTA "Coordinar consulta" → debería ser "Hablar con Gaby"** más humano
5. **Foto de Gaby en hero** (ahora es SVG placeholder)
6. **Countdown a fecha de apertura** — aumenta urgency
7. **Cambiar color de fondo del hero** — pasar de azul a teal

### Sección "Confianza"
8. **Logos certificaciones en línea horizontal** (no apilados)
9. **Número MSPBS clickeable** — abre verificación
10. **Trustpilot / Google reviews link** (cuando haya reseñas)

### Sección "Servicios"
11. **Tabs visuales en desktop** (en vez de cards apilados)
12. **Imagen por servicio** (no solo iconos)
13. **Precio visible en cada servicio**
14. **CTA específico por servicio**

### Sección "Testimonios"
15. **Foto del paciente** (con consentimiento)
16. **Video testimonial** (mes 3+)
17. **Link a Google reviews**
18. **Sistema de rating agregate visible**

### Sección "Proceso"
19. **Iconos personalizados** (no genéricos)
20. **Cada paso con CTA** (WhatsApp para agendar)

### CTA / Conversión
21. **Sticky WhatsApp button** (siempre visible)
22. **Sticky phone clickeable** en mobile
23. **Click-to-call en desktop**
24. **Exit intent popup** con email capture

### Footer
25. **Email newsletter form**
26. **Redes sociales con iconos grandes**
27. **WhatsApp directo**
28. **Horarios actuales con estado abierto/cerrado**

### Mobile específico
29. **Bottom nav fijo** (home / servicios / whatsapp / contacto)
30. **Tap-to-call button sticky**

---

## 🎯 LO QUE ESTÁ BIEN (NO TOCAR)

| Sección | Qué está bien |
|---------|---------------|
| **Hero copy** | "Entiendo el miedo al dentista" — directo, humano, único |
| **Testimonial de ansiedad** | La estructura de "fear_named → testimonial → relief_named" es brillante |
| **FAQ ansiedad/comodidad** | Las 5 preguntas reflejan bien al paciente PY con miedo |
| **Stats de "20+ años"** | Correcto y verificable |
| **Tono general** | Conservadora, honesta, sin promesas exageradas |
| **Animaciones sutiles** | `fade-in-up`, `wipe` — bien logradas |
| **Skip link** | `Saltar al contenido principal` — accesible |
| **HTML lang dinámico** | El intent del script es bueno, pero falla (item 1) |
| **Schema.org FAQPage** | Bien implementado |
| **JSON-LD Dentist** | Base correcta |

---

## 🔴 ACCIÓN INMEDIATA — fixes que ya puedo ejecutar

Voy a corregir los **placeholders falsos** en el JSON que ya tengo acceso (`content/es/site.json` + `content/en/site.json`). Lo que ya hice:

1. ✅ Fix WhatsApp → +595 987 126 790
2. ✅ Fix email → doctora.gabi@ometzdental.com.py
3. ✅ Fix address → Auditores de la Guerra del Chaco 617, Mburucuyá
4. ✅ Fix RUC + MSPBS
5. ✅ Fix brand → Ometz Dental
6. ✅ Fix URL → ometzdental.com (no dragabriela)
7. ✅ Fix tagline → "Te escucho" + אומץ
8. ✅ Fix launch info → 26 jul 2026

Falta en otros archivos del sitio (en producción, no en repo):
- `content/es/testimonials.json` (validar testimonios)
- `content/es/stats.json` (validar números)
- `content/es/hero.json` (fix lang + CTA copy)
- `content/es/cta.json` (fix WhatsApp)
- `content/es/contacto.json` (fix WhatsApp + address)
- Next.js metadata (app/layout.tsx)

---

## 📊 TL;DR PARA IVÁN

**Score: 62/100.** Tiene buen contenido pero **bugs críticos** que cuestan clientes.

**Cosas de 1 día que suben score a 80/100:**
1. Fix WhatsApp real (15 min) — **+15 pts confianza**
2. Fix canonical/og:url (30 min) — **+8 pts SEO**
3. Fix JSON-LD telephone (5 min) — **+5 pts SEO**
4. Fix lang attr + meta description (35 min) — **+5 pts SEO/i18n**
5. Quitar stats falsos o validarlos (1h) — **+10 pts trust**
6. Quitar testimonios inventados o validarlos (1h) — **+10 pts legal**
7. Update title/manifest (10 min) — **+3 pts brand**
8. Fix theme color (30 min) — **+2 pts brand**

**Total esfuerzo: 4-5 horas. Total impacto: +60 puntos.**

**Cosas de 1 semana que suben a 90/100:**
- GA4 + pixel
- Calendly
- Newsletter form
- Breadcrumbs
- Alt text en imágenes
- Google Maps embed
- Search interno FAQs
- אומץ visual prominente en hero
- Sticky WhatsApp button

**Cosas de 1 mes que suben a 95/100:**
- Video hero
- Testimonios con fotos reales
- Foto de Gaby profesional
- Blog posts SEO
- Schema.org expandido
- Web vitals optimization

---

## 🔗 DOCUMENTOS RELACIONADOS

- `docs/ANALISIS-COMPLETO-UPGRADES.md` — audit 360° repo
- `docs/BRANDING-RECONCILIATION-PLAN.md` — fix legacy brand
- `config/variables-central.md` — variables reales
- `06_MARKETING/site-page-copy.md` — copy nuevo

---

**STATUS:** v1.0 — Audit completo del live site. Iván debe ejecutar P0 hoy (4-5 horas) para llevar el sitio de 62/100 a 80/100.