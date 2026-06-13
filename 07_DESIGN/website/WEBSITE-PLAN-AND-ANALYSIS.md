# Plan Completo del Website — Dra. Gabriella González Pane
## Análisis, Arquitectura, e Implementación
### Junio 2026 | Sigue patrón paragu-ai-website

---

## RESUMEN EJECUTIVO

Dra. GP necesita un website profesional que:
1. Establezca su presencia privada (separado de Odontología 3)
2. Comunique su filosofía "odontología con criterio, no con prisa"
3. Capture pacientes de Asunción/Luque + expatriados
4. Funcione como herramienta de marketing automatizado
5. Cumpla con Ley 7593/2025 de Protección de Datos Paraguay

**Stack (replicando paragu-ai-website):** Next.js 15 + TypeScript + Tailwind CSS + Lucide React + Cloudflare Pages
**Lanzamiento:** 2 semanas desde aprobación final
**Costo:** Gs 0 si se hace con el equipo de AI Whisperers, dominio Gs 100-200k/año

---

## ANÁLISIS DEL STATE ACTUAL

### Contenido ya creado (excelente base)
- ✅ Home page content (`core-pages/home-page-content.md`)
- ✅ Philosophy page content
- ✅ Services page content (con precios referenciales)
- ✅ About page content
- ✅ Contact page content
- ✅ Second opinion page content
- ✅ Pricing page content
- ✅ Privacy policy (Ley 7593/2025)
- ✅ Terms of service
- ✅ First visit preparation
- ✅ Site config (site-config.json con colores, fonts, navigation)

### Faltante
- ❌ Blog/educational content (existente en otra carpeta, falta integrar)
- ❌ FAQ page
- ❌ Pre-launch landing page
- ❌ Implementation guide (cómo convertir markdown a Next.js)
- ❌ SEO/content calendar
- ❌ Image/photo specs
- ❌ Brand identity (logo, paleta extendida)

---

## ARQUITECTURA DE PÁGINAS

### Estructura Next.js (a construir)

```
app/
  layout.tsx              → SEO + fonts + nav + footer
  page.tsx                → Home (hero, problem, philosophy, services, who, contact)
  filosofia/page.tsx      → Philosophy (5 principles)
  servicios/page.tsx      → Services (6 categorías con precios)
  precios/page.tsx        → Pricing (tabla completa + disclaimer)
  segunda-opinion/page.tsx → Second opinion
  sobre-mi/page.tsx       → About Dra. GP
  contacto/page.tsx       → Contact form + WhatsApp CTA
  privacidad/page.tsx     → Privacy policy
  terminos/page.tsx       → Terms
  primera-visita/page.tsx → First visit preparation
  blog/
    page.tsx              → Blog index
    [slug]/page.tsx       → Individual posts
  faq/page.tsx            → FAQ page

components/
  nav.tsx                 → Header with mobile menu
  footer.tsx              → Footer with links + contact
  whatsapp-cta.tsx        → Reusable WhatsApp button
  service-card.tsx        → Service display
  price-table.tsx         → Pricing table
  testimonial.tsx         → Patient testimonial
  contact-form.tsx        → Form (email to Dra. GP)
  blog-card.tsx           → Blog post preview

lib/
  data.ts                 → ALL content (services, prices, FAQs, blog)
  utils.ts                → waLink(), formatGs(), etc.
  seo.ts                  → SEO metadata generator

public/
  favicon.svg
  og-image.jpg
  photos/
    dra-gp-hero.jpg
    dra-gp-portrait.jpg
    consultorio-1.jpg
    consultorio-2.jpg
    equipment-1.jpg
  icons/
    dental-icons.svg
```

---

## PÁGINAS Y CONTENIDO

### 1. HOME (`/`)
**Objetivo:** Capturar atención + comunicar filosofía + CTA
**Estructura:** 8 secciones (hero, problem, 3 pillars, services, who, trust, contact, footer)
**CTAs:** WhatsApp primario, segunda opinión secundario

### 2. FILOSOFÍA (`/filosofia`)
**Objetivo:** Diferenciador — lo que NO hacen otros dentistas
**Estructura:** Quote + 5 principios + "qué hago/no hago" + proceso de 5 pasos
**Tono:** Confesional, basado en 20 años

### 3. SERVICIOS (`/servicios`)
**Objetivo:** Mostrar todas las categorías con precios
**Estructura:** 6 categorías (Segunda opinión, Planificación, General, Estética, Rehabilitación, Complejos)
**Datos:** Precios con disclaimer, duración, qué incluye

### 4. PRECIOS (`/precios`)
**Objetivo:** Tabla completa de precios + planes de pago
**Estructura:** Tabla + Pagopar/Bancard info + planes de pago
**Tono:** Transparente, sin sorpresas

### 5. SEGUNDA OPINIÓN (`/segunda-opinion`)
**Objetivo:** Capturar el cliente escéptico
**Estructura:** Quién busca segunda opinión + proceso + precio
**Tono:** Independiente, "no vendo trabajo que no necesitás"

### 6. SOBRE MÍ (`/sobre-mi`)
**Objetivo:** Humanizar a Dra. GP
**Estructura:** Historia + credenciales + filosofía personal
**Tono:** Personal, vulnerable, autoridad

### 7. CONTACTO (`/contacto`)
**Objetivo:** Convertir visita → WhatsApp
**Estructura:** Form simple + WhatsApp CTA + ubicación + horarios
**Tono:** Accesible, rápido

### 8. BLOG (`/blog`)
**Objetivo:** SEO + autoridad + educación
**Estructura:** Artículos sobre casos comunes, decisiones de tratamiento
**Frecuencia:** 1-2 posts/mes
**Tono:** Educativo, sin jerga

### 9. FAQ (`/faq`)
**Objetivo:** Responder objeciones comunes
**Estructura:** 15-20 preguntas agrupadas por tema
**Tono:** Directo, amigable

### 10. TRANSACCIONALES (`/privacidad`, `/terminos`, `/primera-visita`)
**Objetivo:** Legal + reducir ansiedad del paciente
**Estructura:** Estándar legal + orientación práctica
**Tono:** Profesional, claro

---

## SEO Y CONTENIDO

### Keywords Target
**Local:**
- "dentista Asunción"
- "dentista Luque"
- "clínica dental Asunción"
- "odontólogo bilingüe Asunción"

**Intención:**
- "segunda opinión dental Paraguay"
- "dentista que no haga trabajo innecesario"
- "cuánto cuesta corona dental Paraguay"
- "mejor dentista Asunción"

**Expatriados:**
- "English speaking dentist Paraguay"
- "dentist for expats Asunción"
- "dental tourism Paraguay"

### SEO Plan
1. **On-page:** Cada página con meta title + description + H1 + alt text
2. **Schema markup:** LocalBusiness, Dentist, FAQ
3. **Sitemap.xml** + robots.txt
4. **Google Business Profile** (vinculado al sitio)
5. **Backlinks:** Directorios locales, COP, Doctoralia

### Content Calendar (12 semanas)
- Semana 1-2: Lanzamiento + posts fundacionales (5 posts)
- Semana 3-12: 1 post/semana, mix de educativo + casos
- 24 posts totales en Q1

---

## BRANDING

### Logo
- Pendiente diseño (no está creado)
- Espec: 2 versiones (horizontal + vertical) + favicon
- Estilo: Limpio, profesional, médico

### Colores (ya en site-config.json)
- Primary: #2D6A5E (verde dental profesional)
- Accent: #C4956A (warm terracotta)
- Background: #FDFCFA (off-white)
- Texto: #2C2C2C

### Typography
- Headings: Playfair Display (serif, autoridad)
- Body: Inter (sans-serif, claridad)

### Fotografía
Pendiente sesión de fotos:
- Dra. GP portrait (warm, sonriente, autoridad)
- Hero image (manos, modelo dental, NO silla dental)
- Consultorio (real o simulado, 3-5 fotos)
- Equipo (Valo light, autoclave, etc.)

---

## IMPLEMENTACIÓN — TIMELINE

### Semana 1: Foundation
- [ ] Diseño de logo (si se decide hacerlo)
- [ ] Sesión de fotos (3-4 horas con fotógrafo)
- [ ] Confirmar dominio (.com.py o .com)
- [ ] Setup repo `dra-gp-website` en GitHub

### Semana 2: Build
- [ ] Crear estructura Next.js 15 + Tailwind
- [ ] Implementar layout, nav, footer
- [ ] Implementar home + filosofía + servicios (Priority 1)
- [ ] Configurar WhatsApp CTAs y links
- [ ] Deploy preview (Cloudflare Pages staging)

### Semana 3: Polish
- [ ] Implementar páginas restantes
- [ ] SEO on-page + schema markup
- [ ] Privacy/Terms (legal review)
- [ ] QA + mobile testing

### Semana 4: Launch
- [ ] Domain setup + DNS
- [ ] Google Analytics + Search Console
- [ ] Google Business Profile link
- [ ] Producción deploy
- [ ] Anuncio en redes sociales

---

## INTEGRACIÓN CON PARAGU-AI-WEBSITE

### Patrón a Replicar
- Estructura Next.js 15 con App Router
- Static export (Cloudflare Pages)
- Tailwind CSS + Lucide React
- TypeScript estricto
- Components en `/components/`
- Data en `/lib/data.ts`
- `waLink()` utility en `/lib/utils.ts`

### Adaptaciones Necesarias
- Color scheme: usar el de Dra. GP (verde dental + terracotta)
- Footer dark: usar estilo similar
- Mobile drawer: mismo patrón
- Pricing/contact blocks: replicar estructura

### Beneficios
- Mantenimiento simple (markdown-driven)
- SEO optimizado (static export)
- Cloudflare CDN rápido
- Costo bajo (~$5/mes)
- Reutilizable por otros clientes (template)

---

## MÉTRICAS DE ÉXITO

### Mes 1
- [ ] Sitio en línea, SSL activo
- [ ] Google indexa todas las páginas
- [ ] 100+ visitas orgánicas
- [ ] 5+ consultas WhatsApp desde el sitio

### Mes 3
- [ ] 500+ visitas orgánicas/mes
- [ ] 20+ leads WhatsApp/mes
- [ ] Top 3 en Google para "dentista bilingüe Asunción"
- [ ] 5+ conversiones (consultas reales)

### Mes 6
- [ ] 1,000+ visitas/mes
- [ ] 30+ leads/mes
- [ ] 20+ pacientes convertidos totales
- [ ] Blog posiciona para 10+ keywords

---

## DECISIONES PENDIENTES

### Críticas
1. **Dominio:** `dra-gabriela-gonzalez.com.py` vs `dra-gp.com.py` vs otro
2. **Logo:** Diseñar nuevo o usar iniciales
3. **Fotos:** Sesión profesional vs fotos con celular
4. **WhatsApp Business:** Número dedicado vs actual
5. **Hosting:** Cloudflare Pages (gratis) vs Hostinger PY

### No Críticas
1. Idioma secundario: solo español o también inglés completo
2. Blog: arrancar con 5 posts o esperar
3. Tienda online: productos de higiene (no)
4. Reservas online: Calendly o solo WhatsApp

---

*Plan creado: 12 de Junio 2026*
*Para: Dra. Gabriella González Pane*
*Arquitecto: AI Whisperers / Equipo ParaguAI*
