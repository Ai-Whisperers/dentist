# SVG ASSETS MANIFEST — OMETZ DENTAL
## Inventario completo de archivos SVG listos para usar
**Versión:** 1.0 — Julio 2026
**Ubicación:** `07_DESIGN/brand-assets/svg/`

---

## 🎯 QUÉ ES ESTE DIRECTORIO

Aquí están **todos los archivos SVG** de la identidad visual de Ometz Dental listos para:
- Subir a Canva (importar como elemento)
- Descargar como PNG (vía CloudConvert, svgtopng.com)
- Usar directo en HTML/Tailwind
- Entregar a diseñador para refinar

> **Nota técnica:** estos SVG usan tipografía declarada como fallback (`'Montserrat', 'Inter', sans-serif`). Si el destinatario no tiene esas fuentes instaladas, el navegador/sistema usará el fallback. Para producción final, convertir texto a paths (en Illustrator: "Type > Create Outlines").

---

## 📐 LOGOS Y MARCA

| Archivo | Dimensiones | Uso |
|---------|-------------|-----|
| `logo-concept-1-ometz-protagonista.svg` | 600×360 px | Logo vertical principal |
| `logo-concept-1-horizontal.svg` | 800×200 px | Header web, email signature |
| `logo-favicon.svg` | 64×64 px | Favicon browser, app icon |
| `profile-picture.svg` | 500×500 px | Facebook, Messaging Business, GBP |
| `facebook-cover.svg` | 851×315 px | Portada de página Facebook |

### Variantes recomendadas para producción

- **Logo negativo (sobre fondo oscuro):** invertir colores manualmente
- **Logo blanco puro:** cambiar todos los fills a `#FFFFFF`
- **Logo negro puro:** cambiar todos los fills a `#000000`
- **Logo horizontal condensado:** width=400 height=100

---

## 💬 QUOTE CARDS (post estáticos)

| Archivo | Tema | Pillar |
|---------|------|--------|
| `quote-01-te-escucho.svg` | Te escucho. Antes de mirar tu boca, miro tu historia. | P3 voz |
| `quote-02-criterio.svg` | La odontología no empieza con una fresa. Empieza pensando. | P3 voz |
| `quote-03-segunda-opinion.svg` | Una segunda opinión no es desconfianza. Es sentido común. | P5 soft sell |

### Personalización rápida

Para cambiar el texto del quote:
1. Abrir el SVG en cualquier editor (Illustrator, Figma, Inkscape)
2. Editar el bloque `<text>` central
3. Exportar como PNG

---

## 🏥 SERVICIOS

| Archivo | Descripción |
|---------|-------------|
| `services-grid.svg` | Cuadrícula 4 servicios (rehabilitación / 2da opinión / operatoria / estética) |
| `hero-website.svg` | Hero del sitio web (con foto placeholder) |
| `messaging-catalog-consulta.svg` | Item catálogo WA — Consulta general |
| `messaging-catalog-segunda-opinion.svg` | Item catálogo WA — Segunda opinión |
| `messaging-catalog-blanqueamiento.svg` | Item catálogo WA — Blanqueamiento |

---

## 🎓 CARRUSELES EDUCATIVOS (5 slides)

| Archivo | Slide |
|---------|-------|
| `carrusel-01-portada-profilaxis.svg` | Portada: "¿Qué es la profilaxis?" |
| `carrusel-02-eliminar-placa.svg` | Slide 2: "Eliminar placa y sarro" |
| `carrusel-06-cierre-cta.svg` | Slide 6 (cierre): CTA Messaging |

**Para slides 3-5:** duplicar `carrusel-02-eliminar-placa.svg` y cambiar el número grande (1 → 2 → 3 → 4 → 5) y el texto correspondiente. Hay 3 slides más para completar el carrusel de profilaxis:
- Slide 3: Prevenir enfermedad periodontal
- Slide 4: Detectar lesiones tempranas
- Slide 5: Educación personalizada

---

## 🎯 PROMOS

| Archivo | Uso |
|---------|-----|
| `promo-template.svg` | Template base para cualquier promo — solo cambiar título, servicio, precio, validez |
| `dia-especial-madre.svg` | Día de la Madre (corazón rosa coral) |
| `story-promo-flash.svg` | Story 9:16 — promo flash 24h |

---

## 📸 CASOS CLÍNICOS

| Archivo | Uso |
|---------|-----|
| `antes-despues-template.svg` | Plantilla para antes/después con consentimiento |

**Reglas éticas:** nunca publicar sin consentimiento firmado + cara del paciente NO visible.

---

## 📇 IMPRESOS (carpeta `print/`)

| Archivo | Dimensiones físicas | Uso |
|---------|---------------------|-----|
| `print/business-card-front.svg` | 88.9 × 50.8 mm | Tarjeta de presentación (frente) |
| `print/business-card-back.svg` | 88.9 × 50.8 mm | Tarjeta de presentación (dorso con QR) |
| `print/signage-exterior.svg` | 60 × 40 cm | Cartel exterior del consultorio |
| `print/price-list-card.svg` | 85 × 55 mm | Tarjeta de precios para entregar |

### Cómo imprimir

1. **Exportar a PDF de alta calidad** (300 DPI mínimo).
2. En Illustrator: File > Save As > PDF > Quality: High.
3. En Inkscape: File > Save As > PDF.
4. **Validar antes de imprimir:**
   - Tamaños correctos con bleed 3mm
   - Colores en CMYK (no RGB)
   - Tipografías convertidas a outlines
   - QR codes regenerados (los actuales son placeholders)

---

## 🛠️ HERRAMIENTAS PARA CONVERTIR

| Necesidad | Herramienta gratis |
|-----------|---------------------|
| SVG a PNG | svgtopng.com, CloudConvert |
| SVG a PDF | Inkscape, svgtopdf.com |
| Editar SVG | Figma (gratis), Inkscape (gratis) |
| Generar QR real | qrcode-monkey.com |
| Optimizar SVG | svgoptimizer.com |

---

## 🎨 COLORES USADOS EN LOS SVG

```css
--teal: #1A5F5A;       /* Verde Teal Ometz */
--cream: #FAFAF8;      /* Crema Cálido */
--terracotta: #B8860B; /* Terracota Dorado */
--charcoal: #2D2D2D;   /* Carbón Suave */
--rose: #D88C7A;       /* Rosa Coral (acento fechas) */
```

---

## ✅ CHECKLIST ANTES DE USAR CADA SVG EN PRODUCCIÓN

- [ ] ¿Tipografía Montserrat convertida a outlines? (si no se va a servir como SVG)
- [ ] ¿Colores en CMYK para impreso?
- [ ] ¿Colores correctos en RGB para digital?
- [ ] ¿Tamaños de fuente legibles en mobile (≥14pt equivalente)?
- [ ] ¿אומץ se ve bien en el sistema destino (puede requerir fuente hebrea)?
- [ ] ¿Backup del archivo fuente (.svg) guardado en Drive?
- [ ] ¿PNG de respaldo exportado para Canva?

---

## 🔗 CRUZAR CON OTROS DOCUMENTOS

- `07_DESIGN/brand-assets/assets/character-templates.md` — sistema visual
- `07_DESIGN/brand-assets/moodboards-3-direcciones-visuales.md` — mood boards
- `07_DESIGN/brand-assets/logo-direccion-diseno.md` — dirección logo
- `07_DESIGN/brand-assets/direccion-fotografia.md` — fotos
- `06_MARKETING/facebook/52-posts-pre-armados-anuales.md` — copy

---

**STATUS:** v1.0 — 16 SVGs listos. Próximo: validar tipografía hebrea + convertir a PNG para Canva.