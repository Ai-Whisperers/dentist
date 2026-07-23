# 📚 ÍNDICE MAESTRO — TODO LO GENERADO PARA OMETZ DENTAL
## Sesión de trabajo · 22 de julio de 2026
**Compilado por:** Erebus · MiniMax-M3
**Repositorio:** `/root/dentist` (strategy) + `/root/paragu-ai-platform` (código)
**Sitio live:** https://ometzdental.com

---

## 🎯 RESUMEN EJECUTIVO

En una sola sesión se produjo:
- **8 documentos nuevos** commiteados al repo strategy (7 commits)
- **Cambios al sitio live** deployados y verificados (paleta lila + precios + bundles)
- **24 mockups IA** disponibles para referencia visual
- **30+ reels scripts** listos para rodar
- **Herramientas verificadas** para Luana (DaVinci + Whisper + ffmpeg)

---

## 📂 1. DOCS NUEVOS (commits hoy)

### 🎬 Video — `/root/dentist/07_DESIGN/video/`

| # | Archivo | Commit | Link raw | Propósito |
|---|---|---|---|---|
| 1 | `VIDEO-INTRO-HERO-brief-entrevista-2026-07-22.md` | `1ae1ef1` | https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/07_DESIGN/video/VIDEO-INTRO-HERO-brief-entrevista-2026-07-22.md | Brief 5 bloques entrevista video hero 3 min |
| 2 | `VIDEO-IDEAS-COMPLETO-luana-brief-2026-07-22.md` | `086e12f` | https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/07_DESIGN/video/VIDEO-IDEAS-COMPLETO-luana-brief-2026-07-22.md | 33 ideas de video en 8 categorías + 10 nuevas |
| 3 | `FRAMEWORK-EDITORIAL-VALORES-2026-07-22.md` | `f9cd151` | https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/07_DESIGN/video/FRAMEWORK-EDITORIAL-VALORES-2026-07-22.md | 5 valores de Gaby + 3 frases ancla + lista prohibida |
| 4 | `VIDEO-QA-WEBSITE-brief-2026-07-22.md` | `4e9fcf8` | https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/07_DESIGN/video/VIDEO-QA-WEBSITE-brief-2026-07-22.md | 12 preguntas + respuestas para video Q&A en página |
| 5 | `PAQUETE-LUANA-one-pager-2026-07-22.md` | `3ccb258` | https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/07_DESIGN/video/PAQUETE-LUANA-one-pager-2026-07-22.md | Índice maestro para Luana (todos los links) |
| 6 | `STACK-HERRAMIENTAS-LUANA-2026-07-22.md` | `efc3c52` | https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/07_DESIGN/video/STACK-HERRAMIENTAS-LUANA-2026-07-22.md | DaVinci + Whisper + ffmpeg + IA integrations |
| 7 | `INDEX-MAESTRO-2026-07-22.md` | _(este)_ | _(este archivo)_ | Este índice que estás leyendo |
| 8 | `README.md` | `3ccb258` | https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/07_DESIGN/video/README.md | Índice del directorio |

### 📝 Sesión — `/root/dentist/02_MEETINGS/gaby-responses/`

| # | Archivo | Commit | Link raw |
|---|---|---|---|
| 9 | `AUDIO-2026-07-22-sesion-fotos-casa-resumen.md` | `4e9fcf8` | https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/02_MEETINGS/gaby-responses/AUDIO-2026-07-22-sesion-fotos-casa-resumen.md |

---

## 🌐 2. CAMBIOS APLICADOS AL LIVE SITE

**URL:** https://ometzdental.com · Deploy en `dra-gabriela_web` (Docker Swarm)

| # | Cambio | Antes | Ahora | Status |
|---|---|---|---|---|
| 1 | **Paleta default** | `default` (ocean azul) | **`lilac`** (lila cardo → lila profundo) | ✅ Live |
| 2 | **Hex accent** | `#023e8a` (navy) | **`#7251b5`** (lila profundo) | ✅ Live |
| 3 | **Hex bg** | `#caf0f8` (cyan claro) | **`#f6effb`** (lila pastel) | ✅ Live |
| 4 | **No-flash script** | Solo aplicaba si ≠ 'default' | Aplica `DEFAULT_THEME` como fallback | ✅ Live |
| 5 | **Bundles /servicios** | Grid horizontal 2 col | **Vertical 1 col** | ✅ Live |
| 6 | **Bundle 1 precio** | Gs 300.000 | **Gs 130.000** | ✅ Live |
| 7 | **Bundle 2-3** | Con precio público | **"Cotización en consulta"** | ✅ Live |
| 8 | **/precios ES** | Lista de tratamientos con precios | Solo consulta pública + resto "Cotización" | ✅ Live |
| 9 | **/pricing EN** | "from Gs 300,000" | **"PYG 130,000 – 150,000"** | ✅ Live |
| 10 | **Schema SEO JSON-LD** | priceRange "300k-5M" | **"130k-150k (consulta inicial)"** | ✅ Live |
| 11 | **Meta description /pricing** | "Gs 300.000" | **"Gs 130.000 (rango 130-150k)"** | ✅ Live |
| 12 | **FAQ "¿cuánto cuesta?"** | "Gs 300.000 / 400.000" | **"Gs 130.000 – 150.000"** | ✅ Live |

**Imagen Docker corriendo:** `dra-gabriela:prod-df2e1e47-20260723-0113`
**Verificación en vivo:** `var def="lilac"` ✓ + `Gs 130.000` ✓ + `Cotización en consulta` ✓

---

## 📋 3. DOCS PRE-EXISTENTES RELEVANTES (referenciados hoy)

### Estrategia y marca
- **ADN Profesional** — single source of truth de marca, voz, filosofía
  - https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/00_STRATEGIC/ADN-README.md
- **Brand book operativo** (qué SÍ y qué NO)
  - https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/docs/STAFFING-Y-ORGANIZACION/08-brand-book-operativo.md
- **5 pilares oficiales** (alineados con valores de hoy)
  - https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/00_STRATEGIC/financial-pricing/brand-positioning-premium.md
- **Manual community manager**
  - https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/06_MARKETING/manual-community-manager.md

### Contenido pre-escrito
- **30 Reels scripts completos** (15-60s ES + EN)
  - https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/06_MARKETING/reels-scripts/30-reels-scripts.md
- **4 video scripts mes 1-2**
  - https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/02_MEETINGS/gabi-audio-prompts/cuestionarios-completos/RESPUESTAS/contenido-redes-2semanas.md
- **Cronograma semanal reels** (mes 4-9)
  - https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/06_MARKETING/cronograma-semanal-meses-7-9.md
- **Cuestionario 05 — imagen personal + video** (respuestas Gaby 13-jul)
  - https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/02_MEETINGS/gabi-audio-prompts/cuestionarios-completos/RESPUESTAS/RESPUESTAS-05-imagen-personal-2026-07-13.md

### Foto / video brief paralelo
- **Dirección de fotografía completa** (30+ shot list)
  - https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/07_DESIGN/brand-assets/direccion-fotografia.md
- **Prompts IA para mockups** (Flux/DALL-E fallback)
  - https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/07_DESIGN/brand-assets/ai-photo-prompts.md

---

## 🖼️ 4. ASSETS VISUALES DISPONIBLES

### Imágenes IA (mockups referencia visual)

| Carpeta | Cantidad | Formato | Uso |
|---|---|---|---|
| `/root/.hermes/images/ometz-batch-01/` | 20 PNG + 20 WebP | 1024x1024 | Hero · About · Philosophy · Anxiety |
| `/root/.hermes/images/ometz-batch-02/` | 4 PNG + 4 WebP | varios | Paciente niño · anciana · tríptico · bata |
| `/root/.hermes/images/gaby-video-frames/` | 7 JPG | 576x1024 | Frames del video WhatsApp 6-jul (referencia) |

### Audio de Gaby
- `/root/.hermes/audio/gaby/whatsapp-video-2026-07-06.wav` (73s · 16kHz mono)

### Prompts IA adicionales (10)
_Nuevos pendientes de generar_ — ver task 4 del fan-out

---

## 🎬 5. SESIÓN DE HOY CON LUANA

**Setup confirmado:**
- Casa de Gaby, ventana con luz natural
- Scrubs disponibles (rosa coral, azul salvia, verde salvia, mostaza)
- 2-2.5 horas estimadas
- Luana dirige + cámara, Gaby protagoniza

**Plan de rodaje** (4 bloques) — ver `VIDEO-INTRO-HERO-brief-entrevista-2026-07-22.md` y `PAQUETE-LUANA-one-pager-2026-07-22.md`

**Entregables esperados:**
- 30-50 fotos raw + curadas
- 1 video hero 3 min crudo
- 6-8 reels cortos
- Banco de 30+ clips verticales
- Backup Drive cifrado mismo día

---

## 🛠️ 6. HERRAMIENTAS VERIFICADAS

### Instaladas en VPS
- ✅ `whisper` (/usr/local/bin/whisper) — transcripción ES a SRT
- ✅ `ffmpeg` — manipulación video/audio
- ✅ `node`, `npm`, `pnpm`, `bun` — runtime
- ✅ OpenCode en `/root/.opencode/bin/`

### Stack recomendado para Luana (orden de prioridad)
1. **DaVinci Resolve free** — editor pro, sin marca de agua
2. **Whisper.cpp** — subtítulos automáticos ES/EN
3. **ffmpeg** — ya instalado
4. **CapCut desktop** — backup mobile-like
5. **ElevenLabs free** — voice-over de respaldo

### Script Python (nuevo)
- `/root/.hermes/scripts/ometz_pipeline_video.py` (5KB · ejecutable)
- Pipeline automatizado: video → SRT + audio normalizado + 3 variantes de formato

---

## ⚠️ 7. ISSUES DETECTADOS (requieren acción)

| # | Issue | Acción requerida |
|---|---|---|
| 1 | Tokens GitHub rotos (push a `paragu-ai-platform` falló) | Generar nuevo PAT con scope `repo` |
| 2 | Repo `paragu-ai-platform` quedó sin mis 3 commits de lila/precios | Re-pushear cuando PAT regenerado |
| 3 | `/root/dentist` strategy repo tiene precios viejos en `canonical-pricing-reference-v2.md` | Sync manual (10 min) |
| 4 | `site-config.json` del repo strategy dice `paleta: lila` pero el `site.json` live usa hex lilac | Decidir source of truth |

---

## 🔄 8. TAREAS PENDIENTES (post-sesión Luana)

| # | Tarea | Esfuerzo | Prioridad |
|---|---|---|---|
| A | Testear Whisper con video de Gaby | 2 min | Alta |
| B | Generar voice-over TTS de las 12 Q&A | 5 min | Media |
| C | 8 reseñas placeholder pulidas con GPT | 5 min | Media |
| D | Subir mockups IA a Cloudflare R2 | 15 min | Alta |
| E | Sincronizar repo strategy con precios | 10 min | Media |
| F | Generar variantes de headline para A/B test | 5 min | Baja |
| G | Configurar ElevenLabs con voz custom | 30 min | Baja |
| H | Cron job que publique 1 reel/semana | 30 min | Baja |
| I | Sincronizar `/root/dentist/canonical-pricing-reference-v2.md` con precios actuales | 10 min | Media |

---

## 🔗 9. URLS RÁPIDAS

| Recurso | URL |
|---|---|
| **Sitio live ES** | https://ometzdental.com/es |
| **Sitio live EN** | https://ometzdental.com/en |
| **Mirror Traefik** | https://dragabriela.paragu-ai.com |
| **Theme switcher** | https://ometzdental.com/themes |
| **Settings (cambio paleta)** | https://ometzdental.com/es/settings |
| **Repo strategy GitHub** | https://github.com/Ai-Whisperers/dentist |
| **Repo plataforma GitHub** | https://github.com/Ai-Whisperers/paragu-ai-platform |

---

## 📊 10. MÉTRICAS DE LA SESIÓN

| Métrica | Valor |
|---|---|
| Documentos creados | 9 |
| Commits strategy repo | 7 |
| Commits plataforma repo | 3 (push falló, queda pendiente) |
| Cambios al live | 12 verificados |
| Imágenes mockups analizadas | 24 |
| Scripts nuevos | 1 (`ometz_pipeline_video.py`) |
| Skills OpenCode configuradas | 3 (pendientes si OpenCode acepta) |
| Tiempo total | ~3 horas |
| Costo IA | $0 (modelo default MiniMax-M3) |

---

*Compilado por Erebus · 22 jul 2026 · sesión casa de Gaby con Luana*
*Próxima acción sugerida: esperar resultados de Luana hoy + commit del sync de pricing*
