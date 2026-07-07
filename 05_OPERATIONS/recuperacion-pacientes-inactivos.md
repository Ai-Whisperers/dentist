# PLAN DE RECUPERACIÓN DE PACIENTES INACTIVOS
## Ometz Dental — Cómo reactivar pacientes que dejaron de venir

> **Cross-ref:** `09_TEMPLATES/recall-card-template.md` + `09_TEMPLATES/patient-retention-recovery-playbook.md` (legacy) + `08_WHATSAPP/templates/pedido-resenas-v1.md`

**Versión:** 1.0 — Julio 2026
**Para:** Gaby + asistente
**Filosofía:** "Te escucho." — también se aplica a quienes se fueron. Muchos no vuelven por una mala experiencia que podemos arreglar.

---

## POR QUÉ LOS PACIENTES DEJAN DE VENIR

### Razones comunes (en orden de frecuencia)

1. **Se olvidaron** (60% de los casos) — la profilaxis es cada 6 meses, fácil de olvidar
2. **Problemas económicos** (15%) — dejó de tener cobertura o dinero
3. **Mudanza** (10%) — se fue de Asunción o del barrio
4. **Mala experiencia** (8%) — dolor post-tratamiento, atención brusca, precio inesperado
5. **Problema de salud** (4%) — paciente enfermo, no puede salir
6. **Falleció** (2%) — delicado pero posible
7. **Otra razón** (1%) — innumerable

### Implicancia para el consultorio

- El **60% de los inactivos** se pueden recuperar con un simple recordatorio
- El **8% que se fue por mala experiencia** requiere estrategia más cuidadosa
- El **22% restante** no se va a recuperar (mudanza, fallecimiento, decisión)

**Tasa objetivo de recuperación:** 30-40% de pacientes inactivos al año.

---

## DEFINICIONES OPERATIVAS

### Paciente activo

- Última visita hace menos de 9 meses
- Tiene cita programada o viene al menos 1 vez/año

### Paciente inactivo

- Última visita hace 9-24 meses
- NO tiene cita programada

### Paciente perdido

- Última visita hace más de 24 meses
- Se considera "recuperable solo con esfuerzo alto"

---

## WORKFLOW DE RECUPERACIÓN

### FASE 1 — Identificación (mensual)

**Al inicio de cada mes, generar el listado de pacientes inactivos:**

```
Criterios:
- Última visita: 9-24 meses atrás
- NO tiene cita futura programada
- Tiene WhatsApp o teléfono registrado

Query de ejemplo (si tenés sistema):
- Filtrar pacientes por fecha_ultima_visita
- Filtrar por NO tener citas futuras
- Filtrar por tener teléfono/WhatsApp
```

**Cantidad esperada:** 10-30 pacientes/mes (depende del volumen).

### FASE 2 — Segmentación (antes de contactar)

Categorizar a los pacientes:

| Segmento | Característica | Acción |
|---|---|---|
| **A. Solo olvidó** | Última visita fue profilaxis o consulta simple | Mensaje recordatorio amable |
| **B. Tratamiento en curso** | Tenía plan incompleto | Mensaje personalizado sobre continuar |
| **C. Problema económico** | Comentó algo sobre precio en la última visita | Mensaje sobre opciones de pago |
| **D. Mala experiencia** | Dejó de venir después de un procedimiento invasivo | Mensaje empático + invitación a conversar |
| **E. Mudanza / fallecimiento** | Difícil de verificar sin preguntar | Mensaje neutral primero, evaluar respuesta |

### FASE 3 — Mensaje WhatsApp (segmentado)

#### Template A — Solo olvidó (profilaxis)

> "Hola [Nombre]! 👋 ¿Cómo estás? Soy [asistente] de Ometz Dental.
>
> Notamos que ya pasaron [X meses] desde tu última profilaxis. Es el momento ideal para tu próxima limpieza — ¡mantener la salud bucal es más fácil (y barato) que arreglarla después!
>
> Tenemos estos turnos disponibles: [opciones].
>
> ¿Querés que te reserve uno? Respondeme con el día que te queda mejor. ¡Saludos!"

**Timing:** Enviar el día 1 del mes, en horario diurno (10-12hs).

#### Template B — Tratamiento en curso

> "Hola [Nombre]! Soy [asistente] de Ometz Dental.
>
> La última vez que viniste, la Dra. [Gaby] te recomendó continuar con [tratamiento]. ¿Pudiste pensarlo? Si tenés dudas o querés conversar sobre opciones de pago, contame y coordinamos una llamada con ella.
>
> ¡Estamos para ayudarte! 💛"

#### Template C — Problema económico

> "Hola [Nombre]! Soy [asistente] de Ometz Dental.
>
> La última vez charlamos sobre [tratamiento] y querías pensarlo. Si el tema es el costo, tenemos opciones:
> - Pagopar: hasta 18 cuotas
> - Plan personalizado: 50% ahora + 50% en 60 días
> - 5% descuento pagando en efectivo
>
> ¿Querés que coordinemos? ¡No te preocupes, hay solución!"

#### Template D — Mala experiencia

> "Hola [Nombre]. Soy [asistente] de Ometz Dental.
>
> Hace [X meses] que no te vemos y nos preocupa. Si tuviste alguna incomodidad con el último procedimiento o algo no te gustó de la atención, queremos escucharte y mejorarlo.
>
> La Dra. González Pane quiere saber cómo te fue. ¿Puedo coordinar una llamada de 5 minutos con ella? Sin compromiso, solo para conversar.
>
> Tu opinión nos importa mucho."

#### Template E — Neutral (si no sabemos por qué se fue)

> "Hola [Nombre]! Hace un tiempo que no te vemos por Ometz Dental. ¿Todo bien? Si querés agendar tu próxima profilaxis o tenés alguna consulta, estamos disponibles.
>
> Saludos!"

### FASE 4 — Respuesta del paciente

#### Si responde "Sí, quiero turno"

1. Agendar
2. Confirmar 24h antes
3. Registrar en sistema

#### Si responde "No tengo dinero / Ahora no puedo"

1. Ofrecer opciones de financiamiento
2. Si insiste en que no: "Perfecto, te escribimos en unos meses. Cualquier urgencia, escribinos."
3. Marcar como "pausado" en el sistema

#### Si responde "Me fui a otro consultorio"

1. "¡Qué bueno que encontraste quien te atienda! Si alguna vez querés volver, acá estamos."
2. Marcar como "inactivo confirmado" en el sistema
3. NO insistir

#### Si responde "Tuve una mala experiencia"

1. **Disculparse** ("Lamento mucho lo que pasó")
2. **Ofrecer conversación** con Gaby
3. Si la queja es válida: ofrecer solución (revisión sin costo, descuento, etc.)
4. Si la queja es irreal o injusta: mantener el diálogo empático pero defender el trabajo

#### Si NO responde

1. Reenviar el mensaje 1 vez, 1 semana después, con tono más breve
2. Si no responde de nuevo: marcar como "inactivo confirmado" y archivar
3. Re-intentar en 6-12 meses (un recordatorio anual es suficiente)

---

## PROGRAMAS ESPECIALES DE RECUPERACIÓN

### Programa "Volvé a Ometz" (trimestral)

**Una vez por trimestre, campaña específica:**

- Mensaje masivo a todos los inactivos
- Oferta: 15% de descuento en profilaxis + limpieza
- Válido por 30 días
- Publicar también en redes sociales

**Mensaje:**

> "Hola! 👋 Hace [X] meses que no te vemos y queremos verte. Si agendás tu profilaxis este mes, tenés 15% de descuento (pagando en efectivo o transferencia). ¡Volvé a Ometz! Turnos disponibles: [link a agendar]."

### Programa "Traé a un amigo" (continuo)

- Si el paciente trae a un amigo referido, ambos tienen 10% de descuento en profilaxis
- El paciente inactivo que vuelve con un referido tiene descuento aún mayor (15%)

### Programa "Cumpleaños + regalo"

- A cada paciente inactivo, mensaje personalizado en su cumpleaños:

> "¡Feliz cumple, [Nombre]! 🎉 Desde Ometz Dental te deseamos un excelente día. Si querés venir a festejar con una profilaxis, te regalamos el flúor. Turnos disponibles toda la semana."

### Programa "Higiene escolar" (estacional, marzo)

- A los padres de pacientes niños/adolescentes inactivos:

> "Hola [Nombre]! Se vienen las clases y es buen momento para la profilaxis de los chicos. ¿Querés agendar? Tenemos turnos los sábados."

---

## MÉTRICAS DE RECUPERACIÓN

### Mensuales

| Métrica | Target |
|---|---|
| Pacientes inactivos contactados | 100% de los identificados |
| Tasa de respuesta al mensaje | >40% |
| Tasa de agendamiento (de los que respondieron) | >50% |
| Tasa de asistencia efectiva (de los agendados) | >70% |
| % de pacientes inactivos que vuelven | >25% del total contactado |

### Trimestrales

| Métrica | Target |
|---|---|
| Ingresos atribuibles a recuperación | >10% del revenue total |
| Pacientes recuperados que vuelven a hacerse activos | >50% |
| Reducción de la base de inactivos | <30% de la base total |

### Anual

| Métrica | Target |
|---|---|
| Tasa de retención de pacientes año a año | >60% |
| Pacientes activos al cierre del año | >70% del padrón |

---

## CASOS ESPECIALES

### Paciente que falleció

- **Si nos enteramos por un familiar:** "Lamento mucho. [Nombre] siempre fue un paciente muy querido. Si en algo podemos ayudar, estamos."
- **Si no nos enteramos pero el familiar nos escribe por una profilaxis pendiente:** explicar con mucho tacto la situación
- **Nunca** mandar mensajes masivos a pacientes sin chequear primero el estado (especialmente adultos mayores)

### Paciente que se mudó al exterior

- Mensaje breve: "Hola [Nombre]! Vimos que te mudaste. Si volvés a Asunción, acá estamos. ¡Éxitos en tu nueva etapa!"
- Marcar como "migró"

### Paciente con problemas de salud graves

- Si tiene cáncer, está hospitalizado, etc.: NO mandar mensajes de "vení a tu profilaxis"
- **Sí** mandar un mensaje empático: "Hola [Nombre]. Nos enteramos de tu situación. Si en algo podemos ayudar, aunque sea orientación, estamos. Fuerza y pronta recuperación."

### Paciente que era conflictivo

- Si el paciente era demandante, agresivo o problemático:
- **Evaluar** si vale la pena recuperarlo
- Si decidís no contactarlo: archivar silenciosamente
- **NO borrar del sistema** — puede haber historial legal relevante

---

## HERRAMIENTAS

### Sistema de gestión de pacientes (CRM)

Si Gaby adopta un CRM ligero, este flujo se automatiza:
- Alerta automática a 8 meses sin visita
- Mensajes pre-armados por segmento
- Tracking de respuestas y conversiones

### Planilla Excel (alternativa low-tech)

Columnas:

| Paciente | Última visita | Segmento | Fecha mensaje | Respuesta | Acción | Resultado | Notas |
|---|---|---|---|---|---|---|---|
| Juan Pérez | 2024-09-15 | A (olvidó) | 2026-07-01 | Sí | Agendó 15/7 | Vino | OK |
| María López | 2024-08-20 | D (mala exp.) | 2026-07-01 | No responde | Reenviar 8/7 | — | — |

**Owner:** Asistente actualiza semanalmente.

---

## NOTAS PARA GABY

1. **Recuperar pacientes es 5x más barato que conseguir nuevos.** Cada paciente inactivo recuperado es revenue sin costo de adquisición.

2. **No contactes pacientes que se fueron hace más de 24 meses sin un mensaje MUY bien pensado.** Es invasivo.

3. **Los pacientes que vuelven después de una queja son los más leales.** Si resolvés bien el problema, te van a recomendar más que uno que nunca se quejó.

4. **El "Volvé a Ometz" trimestral debe ser un evento.** No es solo mandar un mensaje. Es una mini-campaña con email + redes + carteles en el consultorio.

5. **El sistema debe ser sostenible.** No es un evento único. Es una rutina mensual de 1-2 horas.

---

*Versión 1.0 — 7 julio 2026.*
*Erebus (Ai-Whisperers).*
*Cross-ref: `09_TEMPLATES/recall-card-template.md` + `08_WHATSAPP/templates/pedido-resenas-v1.md` + `05_OPERATIONS/clinical-routines/monthly-financial-tracker.md`.*