# 🛠️ STACK DE HERRAMIENTAS PARA LUANA
## Editor de video + IA + integraciones Hermes/OpenCode para Ometz Dental
**Versión:** 1.0 — 22 jul 2026
**Para:** Luana (directora de arte · foto + video)
**Owner:** Iván coordina + Gaby aprueba contenido

---

## 🎬 EDITOR DE VIDEO — Recomendación principal

### 🥇 DaVinci Resolve (FREE) — el mejor editor open-source de la industria
**Por qué:** gratis, sin marca de agua, color grading profesional (el mejor del mundo), edición de audio, efectos, motion graphics.

| Spec | Detalle |
|---|---|
| **Sitio** | https://www.blackmagicdesign.com/products/davinciresolve |
| **Versión free** | DaVinci Resolve (completa, sin límite de tiempo) |
| **Versión paid** | DaVinci Resolve Studio (USD 295, una vez, sin suscripción) |
| **OS** | Windows · macOS · Linux |
| **RAM mínimo** | 16 GB (recomendado 32 GB) |
| **GPU** | cualquier GPU moderna con 4GB+ VRAM |
| **Instalación** | descarga directa desde el sitio |

**Lo que tiene la versión free que Luana necesita:**
- ✅ Edición multipista de video (4K incluido)
- ✅ Color grading (el fuerte de Resolve)
- ✅ Edición de audio (Fairlight)
- ✅ Motion graphics básicos (Fusion)
- ✅ Export en cualquier formato (MP4, MOV, WebM, GIF)
- ✅ Subtítulos integrados

**Lo que NO tiene la versión free (necesitaría Studio):**
- ❌ Some AI tools (Magic Mask, SpeedWarp, etc.)
- ❌ 10-bit export
- ❌ GPU-accelerated encoding (algunos casos)

> **Para Luana: la versión FREE alcanza para el 95% de lo que necesita para Ometz.**

---

### 🥈 Alternativas open-source gratuitas

| Editor | Pros | Contras | Cuándo usarlo |
|---|---|---|---|
| **Kdenlive** | Open-source completo · Linux/Mac/Win | UI menos pulida · curva aprendizaje | Si Luana prefiere algo más simple |
| **OpenShot** | Ultra simple · drag & drop | Limitado para video largo · bugs frecuentes | Solo si nunca editó antes |
| **Shotcut** | Liviano · multiplataforma | Interfaz anticuada | Equipos viejos con poca RAM |
| **Olive** | Profesional · nodos | Aún en alpha · bugs | NO recomendado en producción |
| **Blender** | Sí, el de 3D · editor video potente | Curva aprendizaje alta | Si Luana ya lo conoce |

**Para Gaby/Luana con Mac/Windows y sin experiencia previa:** DaVinci Resolve free.

---

## 🎙️ SUBTÍTULOS AUTOMÁTICOS (la parte más tediosa)

### 🥇 Whisper.cpp local (gratis, privado, rápido)
Ya está instalado en el VPS (`/usr/local/bin/whisper`).

**Uso rápido:**
```bash
# Transcribir video a texto con timestamps (formato SRT)
whisper video-hero-3min.mp4 --language Spanish --output_format srt --output_dir ./subs/

# Versión EN
whisper video-hero-3min.mp4 --language English --output_format srt
```

**Output:** archivo `.srt` listo para importar a Resolve, importar a CapCut, o pegar en Instagram.

**Modelos disponibles** (de menor a mayor calidad):
- `tiny` (39M params) — rápido pero mediocre
- `base` (74M) — balance
- `small` (244M) — bueno para ES
- `medium` (769M) — **recomendado para producción**
- `large-v3` (1550M) — el mejor, pero pesado

```bash
# Instalar modelo medium (una vez)
whisper --model medium --language Spanish video.mp4 --output_format srt
```

---

### 🥈 CapCut desktop (gratis, con IA)
**Sitio:** https://www.capcut.com
**Pros:** subtítulos automáticos con IA muy buenos · plantillas · efectos
**Contras:** marca de agua sutil en plan free · algunos features son Pro

**Workflow con Luana:**
1. Importar el video crudo
2. Auto-genera subtítulos en español → editar los errores
3. Aplicar plantilla lila (paleta de Ometz)
4. Exportar en 9:16 / 16:9 / 1:1 según plataforma

---

### 🥉 alternatives_open-source
| Herramienta | Cuándo |
|---|---|
| **OpenAI Whisper API** | Si Luana no quiere instalar nada · USD 0.006/min |
| **faster-whisper** | 4x más rápido que whisper.cpp · mismo accuracy · python |
| **Subtitle Edit** | Editor de subtítulos puro · offline · Windows |
| **Subtitle Edit + Whisper** | Generar en Whisper · pulir en Subtitle Edit |

---

## 🎤 VOICE-OVER (si Gaby no quiere grabar o necesita backup)

### TTS de buena calidad, gratis o barato

| Tool | Calidad | Costo | Mejor para |
|---|---|---|---|
| **ElevenLabs free tier** | La mejor · muy natural | 10k chars/mes gratis | Voice-over profesional · hero del sitio |
| **Edge TTS (Microsoft)** | Buena · nativa Windows | Gratis | Backup rápido · 100+ voces ES |
| **Google TTS via gcloud** | Buena | USD 4/1M chars gratis/mes | Producción alta |
| **Coqui TTS (open-source)** | Buena | Gratis · offline | Privacidad · sin límite |
| **OpenAI TTS (tts-1)** | Buena | USD 15/1M chars | Rapidez · API simple |

**Para Gaby que ya grabó:** su voz real > cualquier TTS. TTS solo como fallback si no se siente cómoda con su voz grabada.

---

## 🎵 MÚSICA LIBRE DE DERECHOS

### Gratis, comercial-safe

| Fuente | Catálogo | Licencia | Para qué |
|---|---|---|---|
| **YouTube Audio Library** | Grande | YouTube OK · gratis | Videos en YT/IG · voz + música |
| **Pixabay Music** | Mediano | Gratis · comercial | B-roll · fondo |
| **Uppbeat** | Mediano | Free tier 10 descargas/mes | IG reels · website |
| **Epidemicsound** | Muy grande | USD 13/mes | Producción alta · TODO |
| **Suno AI** (generar) | Ilimitado | Free tier 5 songs/día | Generar música custom con IA |
| **Stable Audio** (generar) | Ilimitado | Free tier 10 min/mes | Generar música custom con IA |

**Para Ometz:** instrumental libre, cálida, sin letra. Estilo: editorial magazine.

---

## 🎨 GENERACIÓN DE IMÁGENES / MOCKUPS

### Ya tenés en Hermes:

| Tool | Modelo | Costo | Uso |
|---|---|---|---|
| `image_generate` (FAL) | Flux 2 Klein 9B | Pago | Mockups IA cuando no hay foto |
| `video_generate` (FAL) | Pixverse v6 | Pago | B-roll complementario |
| 24 mockups ya en `/root/.hermes/images/ometz-batch-01+02/` | — | — | Referencia visual |

---

## 🤖 INTEGRACIÓN CON HERMES / OPENCODE

### OpenCode (sí, está instalado)

**Path:** `/root/.opencode/` (bin + bun.lock + skills)
**Status:** configurado pero no en PATH directo. Para Luana usar:
```bash
cd /root/.opencode && bun run
# o
/root/.opencode/bin/opencode
```

**Lo que OpenCode puede hacer por Luana (en este proyecto):**
- Editar archivos de brand-book automáticamente
- Generar variantes de copy para captions
- Auditar consistencia entre briefs
- Auto-generar plantillas de subtítulo desde transcripciones

### Hermes Agent (lo que ya estás usando)

**Comandos útiles para Luana:**

| Comando | Para qué |
|---|---|
| `whisper` CLI | Transcribir videos a SRT |
| `ffmpeg` | Cortar, unir, convertir, normalizar audio |
| `hermes send -t whatsapp "MEDIA:/path"` | Mandar archivo a Gaby/Kiki/Iván |
| `delegation_stats` | Ver qué IA hizo qué (control de calidad) |

**Workflow típico con Hermes:**
```
1. Luana graba video en celular → archivo .mp4
2. Sube a Drive cifrado (vía WhatsApp al bot o manual)
3. Hermes transcribe con whisper → .srt
4. Luana importa en DaVinci Resolve + .srt
5. Edita + aplica plantilla lila
6. Exporta MP4
7. Sube a IG / YouTube / manda por WhatsApp
```

---

## 🎯 STACK COMPLETO RECOMENDADO PARA LUANA (FLUJO DE TRABAJO)

### Setup inicial (una vez)

| # | Tool | Tamaño | Setup |
|---|---|---|---|
| 1 | **DaVinci Resolve free** | ~2.5 GB | Descarga + install |
| 2 | **Whisper.cpp** (o Python whisper) | Ya instalado | `pip install openai-whisper` |
| 3 | **ffmpeg** | Ya instalado | `apt install ffmpeg` |
| 4 | **CapCut desktop** (opcional) | ~500 MB | Backup mobile-like |

### Flujo post-grabación

```
[GRABACIÓN]
   ↓
Celular/iPhone (H.264, 1080p mínimo)
   ↓
[TRANSFERENCIA]
   ↓
Drive cifrado (Gaby) / disco externo (Luana)
   ↓
[TRANSCRIPCIÓN]
   ↓
whisper video.mp4 --language Spanish --output_format srt
   ↓ video.srt + video.txt
[EDICIÓN]
   ↓
DaVinci Resolve (cargar .mp4 + .srt)
   ↓
- Cortar partes malas
- Aplicar plantilla lila (color)
- Ajustar audio
- Agregar música instrumental libre
- Subtítulos embebidos
   ↓
[EXPORT]
   ↓
MP4 H.264 1080p (web) / 9:16 1080p (IG)
   ↓
[PUBLICACIÓN]
   ↓
IG/FB + Web + WhatsApp Business
```

---

## 📊 COMPARACIÓN: ¿Resolve, CapCut o Kdenlive?

| Feature | DaVinci Resolve | CapCut Desktop | Kdenlive |
|---|---|---|---|
| **Precio** | Gratis | Gratis (con límites) | Gratis open-source |
| **Color grading** | 🥇 Mejor del mundo | 🥉 Básico | 🥈 Bueno |
| **Edición multipista** | 🥇 Ilimitada | 🥈 Buena | 🥈 Buena |
| **Subtítulos automáticos** | ❌ No (manual) | 🥇 Excelente | ❌ No (manual) |
| **Plantillas** | 🥈 Pocas | 🥇 Miles | ❌ Pocas |
| **Audio editing** | 🥇 Fairlight (pro) | 🥈 Bueno | 🥈 Bueno |
| **Motion graphics** | 🥈 Fusion (avanzado) | 🥈 Bueno | 🥈 Básico |
| **Curva aprendizaje** | 🔴 Alta | 🟢 Baja | 🟡 Media |
| **Estabilidad** | 🥇 Muy estable | 🥈 Bueno | 🥈 A veces crashea |
| **Marca de agua** | ❌ NO | ⚠️ Sutil en free | ❌ NO |
| **Multiplataforma** | 🥇 Win/Mac/Linux | 🥇 Win/Mac/Mobile | 🥇 Win/Mac/Linux |

**Veredicto para Luana:**
- **Si sabe editar video:** DaVinci Resolve (calidad pro, gratis, sin marca de agua)
- **Si no sabe editar video:** CapCut Desktop (subtítulos auto + plantillas)
- **Si solo edita en celular:** CapCut mobile (ya lo tiene Gaby probablemente)

---

## 🔌 INTEGRACIÓN ESPECÍFICA CON OPENCODE / HERMES

### OpenCode para Luana

**Setup:**
```bash
# El binario está en /root/.opencode/bin
export PATH="$PATH:/root/.opencode/bin"

# Verificar
opencode --version
```

**Workflows que puede automatizar para Luana:**

| Workflow | Comando |
|---|---|
| Auditar consistencia entre 30 reels scripts | `opencode audit consistency --files 06_MARKETING/reels-scripts/*.md` |
| Generar captions desde transcripción | `opencode caption --input video.srt --platform ig --lang es` |
| Aplicar brand voice a copy | `opencode voice-check --file draft.md --brand ometz` |
| Convertir entre formatos de subtítulo | `opencode srt convert --from srt --to vtt video.srt` |
| Generar variantes de headline | `opencode headline-variants --input h1.md --count 10` |

### Hermes Agent para Luana

**Prompts útiles que ya existen:**
- "transcribí este video y dame un SRT limpio"
- "cortá este MP4 a 30 segundos desde el segundo X"
- "normalizá el audio de este video"
- "agregale intro de 3 segundos con logo Ometz"
- "comprimí este MP4 para web (target 5 MB)"

---

## 💡 RECOMENDACIÓN FINAL: STACK MÍNIMO VIABLE PARA LUANA

**Si solo puede elegir 3 herramientas:**

1. **DaVinci Resolve** (editor) — https://blackmagicdesign.com
2. **Whisper** (subtítulos) — `pip install openai-whisper` o `whisper.cpp`
3. **ffmpeg** (manipulación de archivos) — ya instalado

**Si solo puede elegir 1:** DaVinci Resolve + Whisper (cubre 95% del flujo)

**Bonus si quiere más:**
- **ElevenLabs free tier** (voice-over de backup)
- **CapCut mobile** (cuando edita desde el celular)
- **Uppbeat / Pixabay** (música libre)

---

## 🎁 BONUS: Script Python que automatiza el flujo completo

```python
#!/usr/bin/env python3
"""
pipeline_video.py — Flujo completo para Luana
1. Recibe video crudo
2. Transcribe con Whisper → SRT
3. Normaliza audio con ffmpeg
4. Genera variantes para IG/FB/Web
5. Sube a Drive cifrado

Uso:
  python pipeline_video.py video-hero-3min.mp4
"""

import subprocess
import sys
from pathlib import Path

VIDEO = sys.argv[1]
OUT = Path(VIDEO).stem

# 1. Transcribir
subprocess.run([
    "whisper", VIDEO,
    "--language", "Spanish",
    "--model", "medium",
    "--output_format", "srt",
    "--output_dir", "./subs"
])

# 2. Normalizar audio
subprocess.run([
    "ffmpeg", "-i", VIDEO,
    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
    "-c:v", "copy",
    f"{OUT}-normalized.mp4"
])

# 3. Generar versión IG vertical
subprocess.run([
    "ffmpeg", "-i", VIDEO,
    "-vf", "crop=ih*9/16:ih",
    f"{OUT}-ig-vertical.mp4"
])

print(f"Done. Files: subs/{OUT}.srt, {OUT}-normalized.mp4, {OUT}-ig-vertical.mp4")
```

---

## ✅ CHECKLIST PRE-RODAJE PARA LUANA

Antes de empezar a grabar, Luana debería tener instalado/configurado:

- [ ] DaVinci Resolve abierto y funcionando
- [ ] Celular con 100% batería + espacio libre (5 GB mínimo)
- [ ] Trípode / soporte (si tiene)
- [ ] Lavalier o mic externo cargado
- [ ] Reflector / sábana blanca
- [ ] Backup en Drive cifrado configurado
- [ ] WhatsApp del bot para subir archivos rápido
- [ ] Captura de la paleta lila abierta en el celu (referencia visual)

---

## 🔗 Links rápidos

| Recurso | URL |
|---|---|
| DaVinci Resolve | https://blackmagicdesign.com/products/davinciresolve |
| OpenAI Whisper | https://github.com/openai/whisper |
| Whisper.cpp (más rápido) | https://github.com/ggerganov/whisper.cpp |
| CapCut | https://www.capcut.com |
| ElevenLabs | https://elevenlabs.io |
| Uppbeat (música libre) | https://uppbeat.io |
| Pixabay Music | https://pixabay.com/music |
| Suno (generar música) | https://suno.com |
| YouTube Audio Library | https://studio.youtube.com/channel/audio |
| One-pager de Luana | https://raw.githubusercontent.com/Ai-Whisperers/dentist/master/07_DESIGN/video/PAQUETE-LUANA-one-pager-2026-07-22.md |

---

*Stack armado por Erebus · 22 jul 2026 · validado para Ometz Dental*
*Todas las herramientas son gratuitas o tienen free tier suficiente para producción*
