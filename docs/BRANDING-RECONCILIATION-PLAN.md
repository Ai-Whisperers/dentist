# RECONCILIACIÓN DE BRANDING — DRA-GABRIELA → OMETZ DENTAL
## Plan para corregir la inconsistencia legacy en el repo
**Versión:** 1.0 — 8 de julio 2026

---

## 🎯 PROPÓSITO

El repo tiene **inconsistencia de branding** entre dos marcas:

1. **LEGACY** ("Dra. Gabriela", "Odonto3") — vestigios del branding previo a la decisión de Ometz
2. **ACTUAL** ("Ometz Dental", אומץ, "Te escucho") — el branding estratégico decidido

El live site (`ometzdental.com/en`) usa slug `dra-gabriela-en` — contradice la decisión estratégica.

---

## 📊 INCONSISTENCIAS ENCONTRADAS (28 archivos)

### TIER 1 — Archivos que deben deprecarse o moverse

| Archivo | Acción | Por qué |
|---------|--------|---------|
| `00_STRATEGIC/ADN-Profesional-Dra-Gabriela-Gonzalez-Pane-EXTENDIDO.pdf` | Mover a ARCHIVE | Es de la era anterior a Ometz |
| `01_RESEARCH/competitive/competitor-research-dentist-lessons-202.md` | Renombrar o agregar header "Pre-Ometz" | Análisis con lupa de competencia anterior |
| `ARCHIVE/scrape-odontologia3.json` | Verificar que no esté contaminando otros archivos | Datos de la clínica previa |

### TIER 2 — Referencias en archivos actuales que NO son críticas

| Tipo | Cantidad | Acción |
|------|----------|--------|
| Mención "Dra. Gabriela" en docs históricos | ~28 | Cambiar a "Dra. Gaby" donde esté en copy activo |
| Mención "Odonto3" en docs históricos | ~5 | Mantener en docs legales/competitivos, deprecar de copy activo |

### TIER 3 — LIVE SITE INCONSISTENCIA

**Problema:** `ometzdental.com/en` carga, pero el deploy tiene:
- Slug: `dra-gabriela-en`
- Copy: "Dra. Gabriella González Pane"
- URL alias: `dra-gabriela.com.py`

**Esto contradice directamente `site-page-copy.md` que dice:**
- Headline: "Te escucho." (en ES) / "I listen." (en EN)
- Marca: "Ometz Dental · Dra. Gabriella González Pane"

---

## 🔧 PLAN DE EJECUCIÓN

### Fase 1 — Identificar todo lo legacy
- [x] Auditoría grep (completado 8 jul 2026)
- [ ] Listar cada archivo con referencia "dra-gabriela" o "Odonto3"

### Fase 2 — Mover archivos legacy
- [ ] Crear `ARCHIVE/legacy-brand-pre-ometz-jul-2026/`
- [ ] Mover archivos PDF + scrapes de la era anterior
- [ ] NO eliminar (compliance legal puede necesitarlos)

### Fase 3 — Actualizar copy en archivos activos
- [ ] Reemplazar "Dra. Gabriela" → "Dra. Gaby" en copy activo
- [ ] Verificar que cada cambio mantiene el contexto
- [ ] Commit por archivo (no masivo)

### Fase 4 — Recomendar fix del LIVE SITE

**Opciones para Iván (web dev):**

| Opción | Costo | Tiempo | Recomendación |
|--------|-------|--------|---------------|
| A. Reescribir JSONs content/es y content/en | 1-2 horas | Mismo día | ✅ Recomendado |
| B. Deploy sin tocar (dejar como está) | $0 | 0 | ❌ Peor opción |
| C. Redirigir /dra-gabriela-en → /en | 30 min | Mismo día | ⚪ Complemento |

**Acción recomendada:**
1. Reemplazar JSONs con copy de `site-page-copy.md`
2. Actualizar todas las referencias internas del slug
3. Hacer redirect 301 de `dra-gabriela-en` → `/en`

---

## 🚨 RIESGO SI NO SE ARREGLA

- Cliente busca "Ometz Dental" en Google → encuentra la web → ve "Dra. Gabriella" en copy → confusión
- Campaña de Meta Ads → usuario clickea → ve "Dra. Gabriela" → Ad dice "Ometz" → "¿qué es esto?"
- Tarjeta de presentación dice "Dra. Gabriella González Pane" pero el sitio dice "Ometz Dental"
- **Resultado:** pérdida de credibilidad y bote del 20-40% del tráfico

---

## 📋 CHECKLIST EJECUCIÓN

### P0 (esta semana)
- [ ] Mover archivos TIER 1 a `ARCHIVE/legacy-brand-pre-ometz-jul-2026/`
- [ ] Iván: actualizar JSONs content/es y content/en del live site
- [ ] Iván: hacer redirect 301 de dra-gabriela-en → /en

### P1 (semana 2)
- [ ] Actualizar archivos TIER 2 con el nombre correcto
- [ ] Verificar grep de "dra-gabriela" en master → solo en ARCHIVE + docs históricos

---

## 🔗 CRUZAR CON OTROS DOCUMENTOS

- `00_STRATEGIC/ADN-README.md`
- `config/variables-central.md`
- `06_MARKETING/site-page-copy.md`

---

**STATUS:** v1.0 — Plan completo. Fase 1-3 ejecución esta semana.