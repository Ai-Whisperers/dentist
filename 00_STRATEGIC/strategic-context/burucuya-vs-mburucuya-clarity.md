# 📍 Aclaración: Burucuyá (Luque) vs Mburucuyá (Asunción)

**Para:** Kiki, Ivan, Dra. GP — y cualquiera que abra el repo
**Fecha:** 22 junio 2026
**Por qué:** Hay DOS barrios con nombres parecidos. Confundirlos =错误的 plan.

---

## TL;DR (30 segundos)

- **Burucuyá** = barrio de **LUQUE**, donde la **amiga odontóloga** de Gaby tiene el consultorio que ella mencionó en el audio (viernes).
- **Mburucuyá** = barrio de **ASUNCIÓN**, donde la **Dra. Mariana Brescia** tiene la Clínica Mburucuyá (investigada en el repo, pendiente de contacto).

**Son dos lugares diferentes en dos ciudades diferentes.** Luque y Asunción están pegadas pero NO son lo mismo.

---

## Mapa conceptual

```
ASUNCIÓN (Capital)
├── Mburucuyá (barrio nororiental)
│   └── Clínica Mburucuyá (Dra. Mariana Brescia) — Mariela pendiente
│       📍 Auditores del Chaco 617
│       📞 +595 981 181896
│       📊 Calificación 6.5/10 (research)
│
LUQUE (ciudad vecina, ~30 min de Asunción)
├── Burucuyá (barrio residencial)
│   └── Consultorio de la AMIGA de Gaby — viernes
│       📍 Pendiente confirmar dirección
│       📞 Pendiente confirmar nombre y contacto
│       📊 Audio: habilitación pendiente, día viernes
│
├── Centro Luque (varias opciones investigadas)
│   ├── Clasipar #1596372 — Gs 3.675M/mes
│   ├── Oficentro Luque — Gs 5M/mes
│   └── Zona Comercial — Gs 4-5M/mes
│
└── Laurelty
    └── Beatriz Oviedo (SkyOne) — Gs 1.7M/mes
```

---

## Lo que dijo Gaby en el audio (junio 2026)

Sobre la amiga:

> *"yo ya tengo consultorio en Barrio Burucuyá, que es de mi amiga, que ya tengo seguro que ella me va a prestar su consultorio o alquilar, no hablamos bien, pero ya tengo un lugar los viernes"*

**Datos confirmados por el audio:**
- Barrio: **Burucuyá**
- Ciudad: **Luque** (implícito por "ya tengo consultorio en Barrio Burucuyá" + "Luque es una ciudad que está en crecimiento realmente" + "la clínica Luque me queda a cinco minutos de mi casa")
- Día: **Viernes**
- Relación: **amiga odontóloga** (le presta o alquila)
- Estado: **seguro pero no formalizado** ("ya tengo seguro que ella me va a prestar")

**Lo que NO dijo el audio:**
- Nombre de la amiga
- Dirección exacta
- Habilitación MSPBS
- Si tiene equipo o está vacío
- Cuánto cobraría

**Lo que hay que hacer:** mandar un mensaje de WhatsApp a la amiga para confirmar los 4 datos básicos. Hay una plantilla lista en `00-WHATSAPP-MESSAGE-AMIGA-BURUCUYA.md` (al final de este doc).

---

## Lo que hay en el repo actual sobre Mburucuyá (Asunción)

| Archivo | Qué dice | Estado |
|---|---|---|
| `01_RESEARCH/locations/clinica-mburucuya-full-report.md` | 502 líneas, investigación completa de Clínica Mburucuyá (Mariana Brescia) | Documento canónico. La dirección es Asunción, no Luque. |
| `09_TEMPLATES/follow-up-mburucuya.md` | Mensaje de WhatsApp para Mariana | Asume que ya consiguió el espacio. **Incorrecto: todavía está pendiente.** |
| `luque-space-shortlist-3-priorities.md` Opción 4 | "Clínica Mburucuya (Mariana Brecia)" — **mal escrita como "Brecia" en vez de "Brescia"** | Error tipográfico. Además, confunde ubicación (dice "Barrio Mburucuya, Asunción (not Luque — verify with Mariana)" — la verificación pendiente). |
| `01_RESEARCH/procurement/RESEARCH-GAPS-ANALYSIS.md` | Análisis de gaps | Sin cambios. |
| `01_RESEARCH/locations/asuncion-central-rental-market-report.md` | Datos del mercado de Asunción | Sin cambios. |
| `01_RESEARCH/locations/asuncion-metro-rental-landscape.md` | Asunción + área metropolitana | Sin cambios. |

**Conclusión sobre Mburucuyá (Asunción):** la investigación está bien hecha y es útil. **Pero NO es la opción de la amiga de Gaby.** Es una opción alternativa que requiere contactar a Mariana.

---

## Lo que NO existe en el repo (y debería existir)

- ❌ Un archivo específico para "Burucuyá (Luque) — amiga de Gaby"
- ❌ Una nota que diga "esto NO es lo mismo que Mburucuyá"
- ❌ Un mensaje de WhatsApp listo para la amiga
- ❌ Una confirmación de habilitación MSPBS
- ❌ Un plan de "qué hago en Mburucuyá vs qué hago en Burucuyá"

---

## DECISIÓN OPERATIVA (qué hacer con esto)

| Acción | Prioridad | Quién |
|---|---|---|
| Renombrar `09_TEMPLATES/follow-up-mburucuya.md` a `09_TEMPLATES/follow-up-MBURUCUYA-mariana-asuncion.md` | 🟡 media | Ivan/Erebus (en próximo commit) |
| Crear `09_TEMPLATES/follow-up-BURUCUYA-amiga-luque.md` (mensaje nuevo) | 🔴 alta | Ivan/Erebus (en próximo commit) |
| Corregir "Brecia" → "Brescia" en `luque-space-shortlist-3-priorities.md` | 🟡 media | Ivan/Erebus |
| Confirmar dirección y habilitación con la amiga | 🔴 alta | Gaby |
| Llamar a Mariana Brescia para consultar espacio | 🟡 media | Gaby (esta semana) |

---

## El mensaje de WhatsApp para la amiga (borrador)

Gaby puede copiar y pegar esto (adaptar el nombre):

> Hola [NOMBRE]! ¿Cómo andás?
>
> Te escribo porque quiero contarte algo importante. Estoy planeando abrir mi propio consultorio odontológico en Luque, y me gustaría mucho poder usar tu espacio un día a la semana para atender pacientes particulares míos.
>
> Antes de avanzar, te quería preguntar algunas cosas concretas:
>
> 1. **¿Tenés habilitación MSPBS vigente?** (Sí / No / No sé)
> 2. **¿Qué equipo tenés?** (sillón, autoclave, RX, etc.)
> 3. **¿Cuánto me cobrarías por el uso?** (gratis, costo simbólico, alquiler mensual, % de facturación — lo que sea)
> 4. **¿Qué día podría usar?** (¿viernes te sirve? ¿es fijo o rotativo?)
> 5. **¿Cómo funcionaría la coexistencia?** (yo atiendo cuando vos no, ¿o atendemos juntas en distintas sillas?)
>
> Si tenés 10 min esta semana te llamo y lo charlamos. Sino me contestás por acá y listo 🙏
>
> Gracias!
>
> Gaby

---

*Volver al [README principal](../00-index.md) | [Plan B de Luque](../../ARCHIVE/legacy-roque-jun-2026/phase1-june2026/luque-space-shortlist-3-priorities.md) | [Hoja de la reunión](../../ARCHIVE/legacy-roque-jun-2026/roque-meeting/00-ONE-PAGE-CHEAT-SHEET.md)*
