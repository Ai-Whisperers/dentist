# 🎙️ Audio Processor — Cómo proceso tus audios

**Para:** Erebus, Kiki, o cualquier IA que procese los audios de Gaby

**Objetivo:** cuando Gaby mande un audio respondiendo a un cuestionario, este documento te dice exactamente qué buscar y qué hacer.

---

## 🔍 Lo que tenés que hacer cuando recibís un audio de Gaby

### Paso 1: Identificar qué cuestionario es

Si Gaby dice cualquiera de estas frases, sabés qué cuestionario es:

- "Pregunta uno, WhatsApp..." → Cuestionario A (5 min, 6 datos)
- "Bloque B1, pregunta uno, EAS..." → Cuestionario B bloque B1
- "Bloque B2, pregunta uno, bio corta..." → Cuestionario B bloque B2
- "Bloque B3, pregunta uno, fecha de apertura..." → Cuestionario B bloque B3
- "Bloque C1..." → Cuestionario C bloque C1 (fotos)
- "Bloque C2..." → Cuestionario C bloque C2 (testimonios)
- "Bloque C3..." → Cuestionario C bloque C3 (redes)
- "Bloque C4..." → Cuestionario C bloque C4 (integraciones)

Si no identificás el cuestionario, preguntá: "Gaby, ¿esto es del cuestionario A, B o C?"

---

### Paso 2: Extraer los datos clave

Para cada cuestionario, buscá las keywords específicas. Ejemplos:

#### Cuestionario A (5 min)

| Pregunta | Keywords a buscar | Datos a extraer |
|----------|------------------|-----------------|
| 1 - WhatsApp | "número", "WhatsApp", "Tigo", "Personal", "chip" | Número o fecha tentativa |
| 2 - Dirección | "calle", "dirección", "Mburucuyá", "Asunción", "entre" | Calle exacta o "pendiente" |
| 3 - Email | "email", "correo", "gmail", "hotmail" | Email o "pendiente" |
| 4 - RUC | "RUC", "ruc", "tributario" | Número de RUC o "no tengo" |
| 5 - MSPBS | "MSPBS", "ministerio", "salud", "habilitación" | Número MSPBS o "no tengo" |
| 6 - Horario | "horario", "días", "lunes", "martes", "viernes" | Días y horarios |

#### Cuestionario B (post-reunión)

- **B1:** EAS, RUC, Timbrado, contador, banco
- **B2:** bio, servicios, inglés, foto, bio larga
- **B3:** fecha apertura, soft/hard launch, días, urgencias, seguro

#### Cuestionario C (fase 2)

- **C1:** fotos, scrubs, consultorio, antes/después
- **C2:** testimonios, video, foto, inglés, consentimiento
- **C3:** Facebook, Instagram, blog, LinkedIn, newsletter
- **C4:** Pagopar, Bancard, agenda online, Analytics, formulario

---

### Paso 3: Identificar "no sé" o "pendiente"

Si Gaby dice "no sé", "todavía no", "pendiente", "no sé qué es", "no aplica", "no sé exacto, pero calculo que":

**Anotar como "pendiente"** en la planilla. NO inventar. NO asumir. NO completar con valores por defecto.

**Si podés, dar feedback útil:**
- "Si no sabés qué es la EAS, te explico: [explicación]"
- "Si no tenés RUC, no urge para la web. Bloquea solo facturar."

---

### Paso 4: Armar la planilla de seguimiento

Después de procesar el audio, creá un archivo en `/tmp/gaby-respuestas-[fecha].md` con esta estructura:

```markdown
# Respuestas de Gaby — Cuestionario [A/B/C] — [fecha]

## Datos extraídos

| # | Pregunta | Respuesta | Status |
|---|----------|-----------|--------|
| 1 | WhatsApp | [dato] | ✅ / 🟡 / ❌ |
| 2 | Dirección | [dato] | ✅ / 🟡 / ❌ |
| ... | ... | ... | ... |

## Datos pendientes (Gaby dijo "no sé" o "todavía no")

- [Pendiente 1]
- [Pendiente 2]

## Lo que está bloqueado

- [Bloqueo 1]
- [Bloqueo 2]

## Próximos pasos

1. [Paso 1]
2. [Paso 2]
3. [Paso 3]
```

---

### Paso 5: Confirmar con Gaby

Mandá la planilla a Kiki para que se la muestre a Gaby:

> "Gaby, esto es lo que entendí de tu audio. Decime si está bien o si me equivoqué en algo."

NO asumas que lo que entendiste es lo que Gaby dijo. SIEMPRE confirmá.

---

## 🚨 Errores comunes al procesar audios

### ❌ NO HACER:
- No completar con valores por defecto ("si no dijo, asumo que la calle es Mburucuyá, Asunción")
- No asumir intenciones ("seguro quiso decir que sí")
- No saltar pasos de confirmación
- No hacer 2 preguntas a la vez ("me dijo su WhatsApp y también su email? no, mejor pregunto")

### ✅ SÍ HACER:
- Preguntar si no se entendió
- Confirmar dato por dato
- Resumir lo que entendiste al final
- Dar feedback útil de lo que Gaby no sabe

---

## 📚 Glosario de términos odontológicos que Gaby puede usar

Si en el audio Gaby usa estos términos, sabé qué quiere decir:

- **Endodoncia** = tratamiento de conducto (NO lo hace, deriva)
- **Operatoria** = restauraciones (caries, composites)
- **Prótesis** = coronas, puentes, dentaduras
- **PSI** = Prótesis Sobre Implante (SÍ lo hace, aunque el implante lo ponga otro)
- **Profilaxis** = limpieza dental
- **Curetaje** = limpieza profunda de encías
- **Blanqueamiento** = aclarar el color de los dientes
- **Incrustación (inlay/onlay/overlay)** = restauración hecha en laboratorio
- **Carilla (veneer)** = carilla estética (NO la hace a pacientes jóvenes, solo en casos indicados)
- **Perno** = perno que se pone dentro de un diente endodonciado
- **Rehabilitación oral** = reconstrucción completa de la boca (su servicio estrella)
- **Segunda opinión** = evaluación de un plan propuesto por otro dentista (su diferenciador)
- **Planificación integral** = armar el plan completo de tratamiento
- **OPG** = radiografía panorámica
- **TAC/CBCT** = tomografía computarizada (3D)

---

## 💡 Tips para procesar audios de Gaby

1. **Es paraguaya, usa "vos".** No corrijas.
2. **Habla rápido, con muletillas.** Filtrá "eh", "mm", "tipo", "fla" (por "flor", creo).
3. **Se ríe sola.** Eso es OK, no es que se esté riendo de vos.
4. **Se corrige a sí misma.** Si dice algo y después lo cambia, tomá la versión corregida.
5. **Dice "Kiri" o "Patricia" como chiste familiar.** NO son nombres comerciales, ignoralos.
6. **Dice "Patricia" cuando habla en 3ra persona de su "alter ego".** Es un chiste, no es real.
7. **Odia las IAs que la marean.** Sé simple, sé claro, sé breve.
8. **No le gustan los archivos largos.** Si tenés que darle un archivo, asegurate que sea necesario.

---

*Este archivo es para uso interno de Erebus/Kiki. NO es para Gaby.*
