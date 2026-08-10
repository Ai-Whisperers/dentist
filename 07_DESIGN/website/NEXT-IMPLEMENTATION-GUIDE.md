# Guía de Implementación Next.js — Dra. GP Website
## Paso a Paso para Construir el Sitio
### Sigue patrón paragu-ai-website | Junio 2026

---

## PRERREQUISITOS

node --version   # 18+ required
npm --version    # 9+ required

## PASO 1: Crear el proyecto

npx create-next-app@latest dra-gp-website --typescript --tailwind --app --no-src-dir
cd dra-gp-website
npm install lucide-react

## PASO 2: Configurar Tailwind

Reemplazar tailwind.config.ts con la configuración de Dra. GP:

colors:
  primary.DEFAULT: #2D6A5E
  primary.dark: #1E4A43
  primary.light: #4A9A8C
  accent.DEFAULT: #C4956A
  accent.dark: #A67B52
  bg.DEFAULT: #FDFCFA
  bg.secondary: #F5F0E8

fontFamily:
  heading: Playfair Display, Georgia, serif
  sans: Inter, system-ui, sans-serif

## PASO 3: Crear lib/utils.ts

export const MESSAGING = "[PLACEHOLDER: +595 XXX XXX XXX]"
export const MESSAGING_PREFILLED = "Hola Dra. GP, me gustaria agendar una consulta."

export function waLink(message: string = MESSAGING_PREFILLED): string {
  return tel:+ + MESSAGING + ?text= + encodeURIComponent(message)
}

export function formatGs(amount: number): string {
  return Gs + amount.toLocaleString(es-PY)
}

## PASO 4: Crear lib/data.ts

CONTENIDO COMPLETO - servicios, precios, contacto, filosofia, FAQs - todo en un solo archivo

## PASO 5: Crear componentes

### components/nav.tsx
Header con logo + links + Messaging CTA

### components/footer.tsx
Footer dark con 3 columnas + Messaging

### components/messaging-cta.tsx
Boton reutilizable para CTAs

### components/service-card.tsx
Card de servicio con icono + descripcion

## PASO 6: Crear app/page.tsx (Home)

Usar la estructura del home-page-content.md como guia.
Hero + Problema + 3 Pilares + Servicios + Who + Trust + Contact

## PASO 7: Crear las otras páginas

Copiar estructura, usar lib/data.ts para contenido.

## PASO 8: SEO

En app/layout.tsx:
  metadata.title.default: Dra. GP — Odontología con Criterio en Asuncion
  metadata.description: Second opinions, treatment planning, and quality dental care.
  metadata.keywords: dentista Asuncion, segunda opinion dental, dentista bilingue
  metadata.robots: index: true, follow: true

## PASO 9: Deploy

# Cloudflare Pages
npm run build
# Configurar Cloudflare Pages con build output
# Connect domain
# Enable HTTPS

## PASO 10: Post-launch

- [ ] Google Search Console
- [ ] Google Business Profile link
- [ ] Sitemap submit
- [ ] Analytics 4 setup

---

## ARCHIVOS DE CONTENIDO LISTOS

Todo el contenido ya está escrito y guardado en:
- /07_DESIGN/website/core-pages/
- /07_DESIGN/website/service-pages/
- /07_DESIGN/website/transactional-pages/

Solo hay que convertir el markdown a TypeScript/JSX.

---

*Guia: 12 de Junio 2026*
