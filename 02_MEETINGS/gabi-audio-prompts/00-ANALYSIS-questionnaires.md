# 🔍 Análisis crítico de los 3 cuestionarios
## Cuestionarios para Dra. GP — revisión 22 junio 2026 (v2)
**Audiencia:** Ivan, Kiki — para entender qué funciona y qué no de los cuestionarios que le estamos pidiendo a Gaby

> 🆕 v2 (22 jun): **NINGUNO de los cuestionarios del repo ha sido respondido por Gaby al 22 de junio 2026.** Son todos templates esperando input. Los campos `___` están todos vacíos. La paciente sigue pendiente de llenar Sección 1 del validacion-cliente-dra-gp.md.
>
> **Lo que SÍ sabemos (del audio espontáneo del 22 jun) está en:** `02_MEETINGS/gabi-audio-prompts/CONTEXTO-PREVIO-22JUN.md`. NO preguntes eso de nuevo.

---

## Resumen ejecutivo

El repo tiene **3 cuestionarios principales** + el de validación del sitio + el de audio que agregué. En total le estamos pidiendo a Gaby que conteste **~80 preguntas** repartidas en 5 documentos distintos, con instrucciones contradictorias y sin priorización.

**Esto es insostenible para una persona que acaba de tener una reunión difícil con su jefe.** Le estamos pidiendo que se siente a llenar planillas cuando lo que necesita es claridad sobre su futuro inmediato.

**Recomendación operativa:** consolidar todo en un solo cuestionario único de **15 preguntas**, dividido en **3 partes según urgencia**, y mandarle SOLO la parte que aplica en el momento correcto.

---

## Cuestionario 1: `07_DESIGN/website/validacion-cliente-dra-gp.md` (23 preguntas)

### Qué es
El cuestionario principal del sitio web. Bloqueado en Sección 1 (datos de contacto) desde hace 30+ días.

### Qué tiene bien
- Estructura clara por secciones (5 secciones)
- Preguntas con opciones de múltiple choice
- Tiene prioridad marcada: Sección 1 es URGENTE
- Está en el idioma correcto (español)
- Tiene un README inicial con instrucciones

### Qué tiene mal

| Problema | Impacto | Solución propuesta |
|---|---|---|
| **23 preguntas totales** cuando solo 6 son bloqueantes (Sección 1) | La abruma. No contesta nada. | Crear MVQ (ya hecho en `validacion-minima-viable.md`) |
| **Sección 1 — Pregunta 3** asume dirección actual = "Odontología 3, Asunción" — pero el plan es salir de O3 | Confuso. Publica dirección que no va a tener. | Cambiar el default a "no publicar" con opción de agregar |
| **Sección 1 — Pregunta 5** pregunta por MSPBS pero no aclara que es un dato legal que debe estar vigente | Gaby puede dar un número viejo sin saber | Agregar nota: "verificá que esté vigente — este dato es legal" |
| **Sección 2 — Pregunta 7 (precios)** lista 11 procedimientos pero el `canonical-pricing-reference-v2.md` tiene 30+ | Incompleto. Si cambia un precio no listado, queda desactualizado. | Agregar nota: "si hay precios adicionales que querés publicar, agregalos" |
| **Sección 3 — Pregunta 12 (fotos)** dice "necesito sacarme fotos — ¿pueden ayudarme?" pero no hay un plan concreto | Gaby marca la opción y queda esperando | Agregar contacto del fotógrafo o un "Te paso 3 opciones de fotógrafo esta semana" |
| **Sección 4 — Pregunta 17 (dominio)** da `dra-gabriela.com.py` como opción pero ese dominio NO está comprado todavía | Gaby marca esa opción y queda esperando acción de nuestra parte | Aclarar: "este dominio hay que comprarlo. ¿Querés que lo compre yo? Cuesta Gs 100-200k/año" |
| **Sección 4 — Pregunta 22 (Roque: Opción A o B)** | Asume que la decisión está tomada. Pero Gaby está en pleno proceso. | Cambiar a "Por ahora ¿cómo pensás seguir?" con opciones más suaves |
| **No tiene opción de "no sé"** en preguntas críticas | Gaby se bloquea si no sabe | Agregar "no sé" como opción válida en todas las preguntas |
| **No tiene audio-friendly** | Si Gaby está cansada de escribir, no tiene alternativa | Mi versión en `gabi-audio-prompts/06-cuestionario-del-sitio-validacion.md` cubre esto (ya hecho) |

### Veredicto
**El cuestionario está bien estructurado pero es demasiado largo para el momento actual.** Gaby está en medio de una transición emocional + profesional. Lo que necesita es el MVQ (6 preguntas) AHORA, y el cuestionario completo DESPUÉS (cuando esté más estable).

---

## Cuestionario 2: `09_TEMPLATES/questionnaire-business-setup.md` (10 secciones, 30+ preguntas)

### Qué es
Cuestionario para datos legales, fiscales, operativos. Cubre EAS, RUC, pagos, habilitación, MSPBS, COP, etc.

### Qué tiene bien
- Muy completo
- Cubre lo que el sitio necesita (EAS, RUC, Timbrado)
- Tiene preguntas sobre seguro de responsabilidad civil profesional (que es crítico y no estaba en el otro)
- Tiene sección de TIMING (cuándo lanzar) que es muy útil

### Qué tiene mal

| Problema | Impacto | Solución propuesta |
|---|---|---|
| **Asume que Gaby ya tiene EAS, RUC, Timbrado, COP, etc.** | Falso. Todo está en ❓ en `client-personal-data-checklist.md` | Mover esto a una Fase 2 (post-reunión, post-EAS) |
| **Sección 4 "Seguro médico (cómo manejás)"** pregunta si seguís atendiendo por algún seguro. La respuesta es "sí, en O3" — pero ¿qué pasa después? | Asume que el modelo "dual" es permanente. No es necesariamente así. | Cambiar pregunta a: "Si en algún momento dejás O3, ¿querés atender prepagas en tu consultorio propio? (sí/no/depende)" |
| **Sección 8 "TIMING"** pregunta "cuándo querés lanzar el sitio" sin considerar la decisión de Roque | Si la reunión sale mal, el lanzamiento se atrasa 3-6 meses | Agregar: "¿Depende del resultado de la reunión con Roque? (sí/no)" |
| **Sección 9 "METAS"** pregunta "ticket promedio por consulta" — eso ya está definido en canonical-pricing | Redundante. Confuso. | Sacar. Ya está en el canonical pricing. |
| **Sección 10 "PRESUPUESTO"** pregunta quién financia — pero el audio dice Gaby tiene poco ahorro | Gaby responde "yo" y se queda con ansiedad | Agregar opción: "Mixto — yo + crédito /帮我 un conocido" |
| **No tiene audio-friendly** | Mismo problema que el cuestionario 1 | Hacer una versión audio |

### Veredicto
**El cuestionario es para DESPUÉS de la reunión con Roque, no antes.** Ahora mismo es overwhelming. Hay que pasarlo cuando se defina la situación con O3.

---

## Cuestionario 3: `09_TEMPLATES/questionnaire-website-content.md` (10 secciones, 50+ preguntas)

### Qué es
Cuestionario para cerrar todos los placeholders del contenido del sitio web. Cubre sobre vos, servicios, testimonios, blog, FAQ, integraciones.

### Qué tiene bien
- Cubre la página "Sobre mí" en detalle (preguntas filosóficas)
- Tiene sección de testimonios con foto/video/expats
- Tiene lista de 7 artículos de blog priorizados
- Pregunta sobre integraciones (Google Business Profile, Calendly, newsletter)

### Qué tiene mal

| Problema | Impacto | Solución propuesta |
|---|---|---|
| **Sección 4 "Sobre vos" Pregunta 1:** "¿Algo específico que te motivó a dejar Odontología 3?" | **PELIGROSO.** Si Gaby contesta esto, queda por escrito la intención de irse. Si llega a manos de Roque, es prueba de "traición". | Cambiar a: "¿Qué te motivó a buscar tu propia práctica?" (sin nombrar O3) |
| **Sección 8 Blog — Artículo 1 sugerido: "Por qué dejé el seguro médico después de 13 años"** | **MUY EXPLÍCITO.** El título solo ya es una declaración de guerra contra Roque. | Cambiar a algo más suave: "Por qué elegí la práctica privada" o "Mi filosofía: criterio sobre prisa" |
| **Sección 7 Testimonios** — no aclara el protocolo legal de consentimientos | Gaby puede pedir testimonios sin formulario de consentimiento, y después hay problema legal | Agregar nota: "antes de publicar, necesitamos el formulario firmado" (formulario en `05_OPERATIONS/legal-compliance/patient-legal/`) |
| **Sección 5 Servicios** — pregunta "Tratás niños? (sí/no/derivar)" pero el sitio no tiene página de niños | Gaby contesta "derivar" y el sitio igual no refleja eso | Sincronizar con las páginas de servicios que existen |
| **50+ preguntas en total** | No las va a contestar todas | Priorizar las 10 más críticas (las de Sección 1, 2, 5, 7) |
| **No menciona que el sitio está live** | Gaby no sabe que ya está publicado. Contesta como si fuera teórico. | Agregar al inicio: "ATENCIÓN: el sitio YA está live en dragabriela.paragu-ai.com. Tus respuestas actualizan lo que ya existe." |
| **No tiene audio-friendly** | Mismo problema | Mi versión en `gabi-audio-prompts/06-...` ya cubre esto |

### Veredicto
**El cuestionario es importante pero peligroso en este momento.** Las preguntas filosóficas (Sección 4) y el título del primer artículo (Sección 8) son riesgos legales si caen en malas manos. **Mover a Fase 2.**

---

## Cuestionario 4: `09_TEMPLATES/questionnaire-images-and-photos.md` (7 secciones, 30+ preguntas)

### Qué es
Cuestionario sobre assets visuales: fotos, logo, iconografía, redes sociales.

### Qué tiene bien
- Checklist concreto de qué fotos sacar del consultorio
- Cubre logo, marca, colores
- Tiene protocolo para casos antes/después (con/sin consentimiento)
- Prioriza los assets (🔴 crítico / 🟡 importante / 🟢 nice-to-have)

### Qué tiene mal

| Problema | Impacto | Solución propuesta |
|---|---|---|
| **Sección 7 "ASSETS LEGALES"** — pregunta si tiene CI, RUC, MSPBS, EAS, Timbrado | **REPETIDO** — esto ya está en `client-personal-data-checklist.md` y en `questionnaire-business-setup.md` | Sacar de este cuestionario. Está duplicado 3 veces. |
| **Sección 4 "Paleta de colores"** — da colores hardcoded (#2D6A5E, #C4956A, #FDFCFA) | Si Gaby quiere cambiar, no sabe cómo | Agregar opción "ver paleta en `07_DESIGN/brand-assets/` y decir si te gusta" |
| **Sección 6 "Redes sociales"** pregunta si quiere crear LinkedIn — pero LinkedIn no es prioridad para una práctica local | Distrae | Sacar LinkedIn. Es B2B. La clienta es B2C + expats. |
| **No menciona la decisión crítica: usar su foto o no** | En Paraguay, dentistas mujeres que usan su foto en el sitio web se exponen a一些问题 | Agregar: "¿Querés que tu foto aparezca en el sitio? (sí/no/depende del contexto)" — esta es una decisión seria. |
| **No tiene audio-friendly** | Mismo problema | — |

### Veredicto
**Es el cuestionario más operacional, pero también bloqueado por Sección 7 (legal) que está duplicado.** Hay que sacar la Sección 7 y mandarlo cuando haya consultorio confirmado.

---

## Plan de acción — consolidar en 3 cuestionarios priorizados

### CUESTIONARIO A — "HOY" (5 min) — Para destrabar el sitio
- **Origen:** MVQ que ya creé en `07_DESIGN/website/validacion-minima-viable.md`
- **Preguntas:** 6 (WhatsApp, teléfono, dirección, RUC, MSPBS, email)
- **Cuándo:** Una vez que Gaby esté lista para que el sitio esté público
- **Quién la manda:** Kiki por WhatsApp
- **Output:** Sitio actualizado con datos reales, rebuild, deploy

### CUESTIONARIO B — "DESPUÉS DE LA REUNIÓN CON ROQUE" (15 min) — El consolidado único
- **Origen:** Mezcla de `validacion-cliente-dra-gp.md` + `questionnaire-business-setup.md` + `questionnaire-website-content.md` (sin las preguntas peligrosas)
- **Preguntas:** 15 (reducido de 80+)
- **Estructura:**
  - **B1 — Datos del consultorio propio (5 preguntas):** dirección, EAS, RUC, Timbrado, MSPBS
  - **B2 — Contenido del sitio sin riesgos legales (5 preguntas):** nombre, bio corta SIN mencionar O3, servicios, horarios, contacto
  - **B3 — Operación y timing (5 preguntas):** cuándo lanzar, soft vs hard launch, presupuesto marketing, equipo, dependientes
- **Cuándo:** 1-2 semanas después de la reunión con Roque
- **Quién la manda:** Kiki por email (no WhatsApp — es muy largo)
- **Output:** Sitio completo + plan de lanzamiento

### CUESTIONARIO C — "FASE 2 — Cuando el consultorio esté operativo" (30 min) — El operacional
- **Origen:** `questionnaire-images-and-photos.md` (sin Sección 7 legal) + testimonios + blog + integraciones
- **Preguntas:** 20
- **Cuándo:** Cuando Gaby ya tenga consultorio abierto y esté atendiendo
- **Output:** Fotos profesionales cargadas, testimonios publicados, blog con 3 posts iniciales, redes activas

### Lo que se ELIMINA de los cuestionarios actuales
- ❌ `questionnaire-website-content.md` Sección 4 Pregunta 1 (motivación para dejar O3) — DEMASIADO explícito
- ❌ `questionnaire-website-content.md` Sección 8 artículo "Por qué dejé el seguro médico después de 13 años" — DEMASIADO explícito
- ❌ `questionnaire-business-setup.md` Sección 9 METAS (redundante con canonical pricing)
- ❌ `questionnaire-images-and-photos.md` Sección 7 ASSETS LEGALES (duplicado 3 veces)
- ❌ `questionnaire-images-and-photos.md` Sección 6 LinkedIn (no es prioridad)

---

## Preguntas pendientes de aclarar con Gaby — basadas en los cuestionarios

Estas NO están en ningún cuestionario actual y deberíamos preguntar:

### Operacionales
1. **¿Tenés formulario de consentimiento de uso de imagen firmado para casos antes/después?** (Si no, hay que crearlo antes de cualquier publicación)
2. **¿Tu número de WhatsApp actual es personal o querés uno dedicado para la práctica?**
3. **¿Querés que tu foto personal esté en el sitio web, o preferís mantener el anonimato?**
4. **¿Tenés sello profesional?** (Necesario para recetas y constancias)

### Legales-financieras
5. **¿Tenés o podés conseguir un seguro de responsabilidad civil profesional?** (Crítico para práctica privada)
6. **¿Tenés un contador que pueda ayudarte con el EAS y el timbrado?**
7. **¿El RUC lo vas a sacar a tu nombre personal o a nombre de la EAS?**
8. **¿Tu cédula está vigente? ¿Cuándo vence?**

### Decisiones de marca
9. **¿Querés atender con tu nombre completo o crear una marca comercial?** (Dra. Gabriella vs "Clínica Dental [Nombre]")
10. **¿Querés tener una marca que se pueda vender después o una práctica de "una socia"?
11. **¿La marca es solo vos o va a haber otros dentistas associés?**
12. **¿Querés que el sitio mencione explícitamente "ex-Odontología 3" o no?**

### Timing y operación
13. **¿Cuántas horas por semana querés dedicar a la práctica privada vs O3?**
14. **¿Querés atención los fines de semana?**
15. **¿Querés atención a domicilio o solo en consultorio?**

### Financieras (no preguntar en cuestionario — sensible)
16. **¿Cuál es tu capital inicial disponible para la práctica?**
17. **¿Tenés línea de crédito pre-aprobada?**
18. **¿Hay algún ingreso pasivo o dependencia que te ate financieramente?**

---

## Resumen ejecutivo

| Cuestionario | Estado actual | Acción |
|---|---|---|
| `validacion-cliente-dra-gp.md` (23 preguntas) | OK estructura, overwhelming largo | Reemplazar con MVQ (ya hecho) + Consolidado B |
| `questionnaire-business-setup.md` (30+ preguntas) | Aplica Fase 2 | Reemplazar con Consolidado B (sección B1) |
| `questionnaire-website-content.md` (50+ preguntas) | Tiene 2 preguntas peligrosas | Eliminar Sección 4 Pregunta 1 y Sección 8 artículo 1; consolidar |
| `questionnaire-images-and-photos.md` (30+ preguntas) | Duplicado legal en Sección 7 | Sacar Sección 7; consolidar a Fase 2 |

**Total de archivos a modificar:** 3
**Total de preguntas eliminadas (peligrosas o redundantes):** 5
**Total de archivos NUEVOS a crear:**
- `validacion-minima-viable.md` (ya hecho)
- Cuestionario B consolidado (PENDIENTE)
- Cuestionario C operacional (PENDIENTE)

**¿Sigo con B y C?** Si decís que sí, los armo ahora.

---

*Volver al [README principal](../../README.md) | [Hoja de la reunión](../../02_MEETINGS/client-prep/roque-meeting/00-ONE-PAGE-CHEAT-SHEET.md)*
