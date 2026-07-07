# TRACKING SHEET — PROGRAMA DE REFERIDOS
## Ometz Dental — Cómo registrar y dar seguimiento
> **PRICING CROSS-REFERENCE:** Este documento no contiene precios. La referencia es `00_STRATEGIC/financial-pricing/canonical-pricing-reference-v2.md`. El campo `reciprocidad_nota` registra el "thank you" simbólico (no efectivo) — ver `04-referral-program-faq.md` para la política ética.
>
> **Cross-ref:** `01-list-target-colleagues-asuncion.md` + `02-outreach-script-colega.md` + `04-referral-program-faq.md`

**Versión:** 1.0 — Julio 2026

---

## OBJETIVO

Esta planilla permite a Gaby registrar cada contacto y referido en el programa de colegas. Sin registro, no hay forma de medir éxito ni de agradecer correctamente.

---

## HERRAMIENTA RECOMENDADA

**Google Sheets** (gratis, accesible desde cualquier dispositivo, backup automático en la nube).

**URL de la planilla (crear al lanzar):** `https://docs.google.com/spreadsheets/d/[ID]/edit`

**Hojas dentro del spreadsheet:**

1. **CONTACTOS** — registro de cada colega contactado
2. **REFERIDOS_RECIBIDOS** — pacientes que vienen referidos a Gaby
3. **REFERIDOS_ENVIADOS** — pacientes que Gaby deriva al colega
4. **THANK_YOU_LOG** — registro de agradecimientos enviados

---

## HOJA 1: CONTACTOS

### Schema (columnas)

| # | Columna | Tipo | Descripción | Ejemplo |
|---|---|---|---|---|
| A | ID | auto-increment | ID único | 001 |
| B | Nombre colega | texto | Nombre completo | Dr. Juan Pérez |
| C | Especialidad | enum | general / endo / ortho / perio / cirugia / impl / otro | endo |
| D | Sub-especialidad | texto | Detalle si aplica | Endodoncia microscópica |
| E | Consultorio | texto | Nombre del consultorio | Clínica XYZ |
| F | Zona Asunción | enum | Mburucuyá / Villa Morra / Carmelitas / Recoleta / San Roque / Otro | Villa Morra |
| G | Dirección | texto | Dirección completa | Av. Mariscal López 1234 |
| H | Teléfono | texto | Teléfono fijo | (021) 555-1234 |
| I | WhatsApp | texto | WhatsApp con prefijo | +595 981 123456 |
| J | Email | texto | Email profesional | juan.perez@clinica.com.py |
| K | Habla inglés | bool | Sí/No | Sí |
| L | Habla guaraní | bool | Sí/No | No |
| M | Origen del dato | enum | Doctoralia / referido / Google / FB / presencial / otro | Doctoralia |
| N | Fuente verificación | texto | URL o nombre del referente | doctoralia.com.py/dra-juan |
| O | Fecha primer contacto | fecha | Cuándo lo contactaste por primera vez | 2026-07-15 |
| P | Canal primer contacto | enum | WhatsApp / teléfono / presencial / email / LinkedIn | WhatsApp |
| Q | Status | enum | contactado / reunión / acuerdo / activo / inactivo | activo |
| R | Tipo de relación | enum | derivación mutua / solo recibe / solo deriva / colega bilingüe | derivación mutua |
| S | Fecha de acuerdo | fecha | Cuándo firmaron acuerdo verbal o escrito | 2026-07-20 |
| T | Pacientes referidos a Gaby (acumulado) | int | Counter | 3 |
| U | Pacientes derivados al colega (acumulado) | int | Counter | 5 |
| V | Ticket promedio de referidos | moneda Gs | Promedio | 800.000 |
| W | Última interacción | fecha | Última comunicación | 2026-09-10 |
| X | Próxima acción | texto | Qué sigue | Llamar el 15/10 |
| Y | Notas | texto largo | Observaciones | "Excelente endodoncista, muy puntual" |
| Z | Thank you enviado | bool | Si ya se le agradeció este año | TRUE |

---

## HOJA 2: REFERIDOS_RECIBIDOS

### Schema (columnas)

| # | Columna | Tipo | Descripción | Ejemplo |
|---|---|---|---|---|
| A | ID referido | auto | ID único | R-001 |
| B | Fecha del referido | fecha | Cuándo el colega derivó al paciente | 2026-08-05 |
| C | Nombre colega | texto | Quién derivó | Dr. Juan Pérez |
| D | Nombre paciente | texto | Paciente derivado | María López |
| E | CI paciente | texto | Cédula del paciente | 3.456.789 |
| F | Procedimiento principal | enum | profilaxis / restauración / corona / endo / otro | corona |
| G | Costo total | moneda Gs | Cuánto se cobró | 1.800.000 |
| H | ¿Se completó tratamiento? | bool | Sí/No | Sí |
| I | Fecha de completado | fecha | Cuándo terminó | 2026-09-15 |
| J | Thank you enviado al colega | bool | Sí/No | TRUE |
| K | Tipo thank you | enum | café / cena / libro / regalo / nota / nada | café |
| L | Notas | texto | Comentarios | "Paciente muy conforme, recomendó 2 amigos" |

---

## HOJA 3: REFERIDOS_ENVIADOS

### Schema (columnas)

| # | Columna | Tipo | Descripción | Ejemplo |
|---|---|---|---|---|
| A | ID derivado | auto | ID único | D-001 |
| B | Fecha | fecha | Cuándo Gaby derivó | 2026-08-10 |
| C | Paciente | texto | Nombre paciente | Carlos Gómez |
| D | Paciente ID | texto | ID interno del paciente | P-1234 |
| E | Colega destino | texto | A quién se derivó | Dra. Ana Martínez |
| F | Especialidad destino | texto | endo / ortho / cirugia / impl | endo |
| G | Motivo | texto | Por qué se derivó | Endodoncia en 36 |
| H | ¿El paciente fue? | bool | Sí/No | Sí |
| I | ¿Volvió a Ometz post-tratamiento? | bool | Sí/No | Sí |
| J | Fecha de retorno | fecha | Cuándo volvió a Ometz | 2026-09-05 |
| K | Procedimiento posterior en Ometz | texto | Qué se hizo en Ometz después | Restauración en 36 |
| L | Notas | texto | Comentarios | "Dra. Martínez rápida, paciente conforme" |

---

## HOJA 4: THANK_YOU_LOG

### Schema (columnas)

| # | Columna | Tipo | Descripción | Ejemplo |
|---|---|---|---|---|
| A | ID | auto | ID único | TY-001 |
| B | Fecha | fecha | Cuándo se envió/dio | 2026-09-15 |
| C | Colega | texto | Quién lo recibió | Dr. Juan Pérez |
| D | Tipo | enum | café / cena / libro / vino / detalle / nota pública / none | café |
| E | Ocasión | texto | Motivo del agradecimiento | Cerró caso de corona |
| F | Costo | moneda Gs | Cuánto costó | 50.000 |
| G | Notas | texto | Detalles | "Café en Café Yvy, charla de 30 min" |

---

## STATUS FLOW (ciclo de vida del colega)

```
contactado
   ↓ (primer mensaje, llamada o visita)
reunión
   ↓ (acordaron conversar presencialmente)
acuerdo
   ↓ (acordaron derivación mutua, verbal o escrito)
activo
   ↓ (al menos 1 referido/derivación en últimos 6 meses)
inactivo
   ↓ (sin contacto >6 meses o sin referidos)
```

**Reglas:**
- `contactado` → primer outreach (puede ser email/WhatsApp/llamada)
- `reunión` → quedaron para verse personalmente
- `acuerdo` → firmaron acuerdo (verbal o escrito) de derivación
- `activo` → está generando referidos o aceptando derivaciones
- `inactivo` → no hubo movimiento en 6 meses

---

## MÉTRICAS A TRACKEAR

### Mensuales (cierre de mes)

| Métrica | Cálculo | Target |
|---|---|---|
| Colegas contactados (mes) | Nuevos en status `contactado` | 5-10/mes |
| Reuniones realizadas | Conteo de reuniones | 2-5/mes |
| Acuerdos firmados | Conteo de acuerdos | 1-3/mes |
| Referidos recibidos (mes) | Conteo de referidos entrantes | 5+/mes |
| Derivaciones enviadas (mes) | Conteo de derivaciones salientes | 5+/mes |
| Thank you enviados | Conteo de agradecimientos | proporcional |

### Trimestrales

| Métrica | Target |
|---|---|
| Colegas activos totales | >15 |
| % de colegas activos que generaron al menos 1 referido | >60% |
| Ticket promedio de pacientes referidos | >Gs 700K |
| Pacientes referidos que vuelven al especialista y vuelven a Ometz | >70% |

---

## WORKFLOW OPERATIVO

### Cuando llega un paciente referido

```
1. Paciente llega y dice "me derivó el Dr. Pérez"
2. ANOTAR inmediatamente en columna de REFERIDOS_RECIBIDOS
   (no confiar en la memoria, escribir el mismo día)
3. En la consulta: preguntarle al paciente:
   - ¿Cómo conoció al Dr. Pérez?
   - ¿Qué le dijo específicamente?
4. Al final del tratamiento:
   - Mandar thank you al colega (WhatsApp breve + regalo si corresponde)
   - Anotar en THANK_YOU_LOG
5. A los 30 días: chequear si el paciente vuelve para control/seguimiento
```

### Cuando Gaby deriva un paciente

```
1. Anotar en REFERIDOS_ENVIADOS
2. Comunicar al paciente: "Te derivo con [colega] que es excelente en esto"
3. Coordinar con el colega (WhatsApp + envío de historia + radiografías)
4. A los 14 días: chequear si el paciente fue
5. Si fue: agradecer al colega (thank you)
6. Si no fue: ayudar al paciente a agendar
7. Cuando vuelve a Ometz: actualizar REFERIDOS_ENVIADOS con el procedimiento posterior
```

---

## POLÍTICA DE "THANK YOU" (NO comisión, sí agradecimiento)

### Cuándo agradecer

- Después de cada caso completado exitosamente
- Una vez al año (fin de año) para colegas activos (cena o regalo)
- En fechas especiales (cumpleaños del colega, día del odontólogo)

### Formas de agradecer

| Tipo | Costo aprox (Gs) | Cuándo apropiado |
|---|---|---|
| Mensaje WhatsApp personal | 0 | Después de cada caso |
| Tarjeta escrita a mano | 5.000 | Después de cada caso importante |
| Café / desayuno | 30.000-50.000 | Cuando se ven en persona |
| Libro técnico | 50.000-150.000 | Fin de año o caso muy especial |
| Cena en restaurante bueno | 200.000-400.000 | Una vez al año, fin de año |
| Detalle personalizado (vino, etc.) | 100.000-200.000 | Navidad o aniversario |
| Nota pública (en redes, con permiso) | 0 | Cuando el colega lo acepta |

### Lo que NO se hace

- ❌ Pago en efectivo por referido
- ❌ Pago disfrazado (regalos de valor alto cada vez)
- ❌ "Cuentas pendientes" con descuentos especiales
- ❌ Compartir el fee del tratamiento

---

## REVISIÓN MENSUAL DE LA PLANILLA

**Último día del mes, 30 min:**

```
[ ] Actualizar status de cada colega
[ ] Cerrar referidos del mes
[ ] Anotar thank you enviados
[ ] Identificar colegas inactivos (sin contacto >3 meses)
[ ] Decidir acciones para el mes siguiente:
    - ¿A cuántos colegas nuevos contactamos?
    - ¿A cuántos colegas inactivos reactivamos?
    - ¿Cuántos thank you hay que enviar?
[ ] Compartir resumen con Kiki (si participa en outreach)
[ ] Commit del spreadsheet (si usás git para versioning)
```

---

## NOTAS PARA GABY

1. **Sin tracking, no hay programa.** Es la diferencia entre "tengo contactos" y "tengo un programa que funciona".

2. **El thank you es lo más importante.** El colega que se siente valorado deriva más y mejor.

3. **No confundir cantidad con calidad.** 5 colegas activos > 50 contactos fríos.

4. **El sheet es propiedad de Ometz Dental.** Si alguna vez delegás esto a la asistente, ella solo registra — vos decidís las relaciones estratégicas.

5. **Backup mensual.** Aunque Google Sheets tiene backup automático, exportá a Excel una vez al mes por las dudas.

---

*Versión 1.0 — 7 julio 2026.*
*Erebus (Ai-Whisperers).*
*Cross-ref: `01-list-target-colleagues-asuncion.md` + `02-outreach-script-colega.md` + `04-referral-program-faq.md`.*