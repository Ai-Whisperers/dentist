# MANUAL DEL ASISTENTE — OMETZ DENTAL
## Guía operativa para auxiliar / recepcionista

> **Versión:** 1.0 — Julio 2026
> **Para:** Asistente o recepcionista de Ometz Dental
> **Por:** Dra. Gabriella González Pane
> **Filosofía:** "Te escucho." — esta frase aplica también para el trato con el paciente en recepción y antes/después del sillón.

---

## BIENVENIDA

Sos parte de Ometz Dental. Este consultorio es especial porque la doctora trata a los pacientes como personas, no como dientes. Tu rol es hacer que esa filosofía se sienta desde el primer Messaging hasta la despedida.

**Lo que se espera de vos:**
- Cordialidad sin exageración (no gritar "¡BIENVENIDA!")
- Atención al detalle (recordar cómo se llama el paciente, sus preferencias)
- Cero juicio (el paciente puede tener la boca muy descuidada y NO es tu trabajo opinar)
- Puntualidad (si la cita es a las 15:00, el sillón está listo a las 14:55)
- Confidencialidad absoluta

---

## ROLES Y HORARIOS

### Si sos **asistente de sillón** (dentro del consultorio)

- **Llegás 30 min antes** del primer paciente
- **Te quedás 30 min después** del último paciente
- Apoyás a la doctora durante los procedimientos
- Esterilización y preparación de instrumental
- Manejo de la historia clínica (datos administrativos, no diagnóstico)

### Si sos **recepcionista** (frente al consultorio o virtual)

- Manejo de Messaging Business (responder consultas, agendar)
- Confirmación de citas (24h antes y 2h antes)
- Cobro y facturación (apoyo al contador)
- Atención al paciente en sala de espera
- Compra de insumos y materiales (cuando se te pida)

### Si hacés las dos cosas (lo más común al inicio)

- Turno cortado: 8-9 horas con 1 hora de almuerzo
- Agenda bien definida:受付 a la mañana + sillón a la tarde (o como se coordine)

---

## PROCEDIMIENTOS DIARIOS

### Apertura (30 minutos antes del primer paciente)

```
[ ] Verificar la puerta del consultorio está abierta (la doctora llega primero o juntas)
[ ] Encender la luz general y la lámpara del sillón
[ ] Encender la autoclave (si hay ciclo pendiente)
[ ] Llenar la escupidera con agua
[ ] Test de succión: succionar agua por 30 segundos
[ ] Test de pieza de mano: 10 segundos al alta velocidad con agua
[ ] Limpieza visual de superficies (sillón, mesada, lámpara) con solución
[ ] Verificar stock de EPP del día (guantes, mascarillas, gasas, algodón)
[ ] Bandeja de instrumentos del primer paciente lista
[ ] Computadora / sistema abierto y login
[ ] Teléfono Messaging Business abierto
```

### Durante la jornada

**Antes de cada paciente:**
1. Revisar la historia clínica del paciente en el sistema
2. Preparar bandeja con instrumental necesario
3. Verificar materiales específicos del procedimiento (resinas, anestésico, etc.)
4. Saludar al paciente en la recepción con nombre y apellido
5. Ofrecer agua, acomodar al paciente, preguntarle si tiene alguna urgencia

**Durante el procedimiento:**
- Pasar instrumental a la doctora cuando lo pida
- Aspirar saliva (sin tocar la lengua si podés evitarlo)
- Hablar con el paciente solo si la doctora lo inicia (respetar la concentración)
- Si el paciente tiene dolor o incomodidad, avisar inmediatamente a la doctora

**Después del paciente:**
1. Acompañar al paciente a la recepción
2. Entregar tarjeta de turno de pago si aplica
3. Procesar el cobro (efectivo, transferencia, POS, Pagopar)
4. Entregar tarjeta de recomendación (referral card) si el paciente está conforme
5. Programar próxima cita (si aplica)
6. **Iniciar protocolo de recall:** Messaging a las 48h preguntando cómo se siente
7. Limpieza y preparación para el siguiente paciente (10-15 min)

### Cierre (30 minutos después del último paciente)

```
[ ] Aspiración con solución enzimática (5-10 min)
[ ] Limpieza profunda del sillón
[ ] Limpieza de mesada y superficies con hipoclorito
[ ] Barrido y trapeado del piso
[ ] Instrumental usado → lavado → ultrasonido → empaque → autoclave (programar ciclo nocturno)
[ ] Contenedor de punzocortantes: verificar capacidad (cambiar si >75%)
[ ] Bolsa roja de residuos: cerrar si está >75%
[ ] Contar caja del día (efectivo + transacciones)
[ ] Anotar en el libro de caja: ingresos del día
[ ] Mensaje Messaging a la doctora con resumen del día
[ ] Cerrar puertas y ventanas
[ ] Activar alarma (si aplica)
```

---

## COMUNICACIÓN CON PACIENTES

### Messaging Business — Tono y tiempos

- **Tiempo de respuesta:** <30 minutos en horario laboral, <2 horas en fin de semana.
- **Tono:** cálido, profesional, breve. Sin abreviaciones, sin emojis excesivos.
- **NO usar:** "Estimado/a usuario/a", "Señor/a", formalidad excesiva. Sí usar el nombre.
- **SÍ usar:** "Hola [Nombre]!", "Gracias por escribir", "Te confirmo", "Pasame tu CI para registrarte".

### Respuestas rápidas pre-armadas (quick replies)

Las quick replies ya están configuradas en `08_MESSAGING/templates/quick-replies-PERSONALIZADO-gaby.md`. Las principales:

| Quick reply | Cuándo usarla |
|---|---|
| `saludo-inicial` | Primera respuesta a un paciente nuevo |
| `agendar-cita` | Cuando el paciente quiere agendar |
| `confirmar-24h` | 24h antes de la cita |
| `confirmar-2h` | 2h antes de la cita |
| `post-consulta-48h` | 48h después del procedimiento (preguntar cómo está) |
| `recordar-profilaxis-6m` | Cada 6 meses para recall |
| `pedir-resena` | 1 semana después de un procedimiento exitoso |
| `derivacion-colega` | Si el caso no lo trata Gaby |
| `agradecimiento` | Cuando el paciente agradece o recomienda |
| `objecion-precio` | Si el paciente duda por precio (ver objection library) |

### Manejo de objeciones comunes

| Objeción | Respuesta sugerida |
|---|---|
| "Es muy caro" | "Entiendo. ¿Querés que veamos opciones de pago en cuotas? Pagopar te permite hasta 12 cuotas." |
| "Tengo que pensarlo" | "Perfecto, tomátelo con calma. Cualquier duda me escribís." |
| "Mi seguro no cubre esto" | "Podés pedir reintegro a tu seguro igual, te emitimos factura con todos los datos." |
| "¿No tenés disponibilidad antes?" | "Lo siento, los turnos de la doctora están así esta semana. Te aviso si se libera algo." |
| "Vi otra clínica más barata" | "Sí, hay opciones más baratas. Acá lo que ofrecemos es [criterio / tiempo dedicado / materiales premium]." |

---

## BIOSEGURIDAD — Tu responsabilidad

Como asistente, sos responsable de:

- ✅ **Usar EPP completo** en todo momento dentro del consultorio
- ✅ **Cambiar guantes** entre pacientes (sin excepción)
- ✅ **Desechar correctamente** el material biocontaminado (bolsa roja, contenedor amarillo)
- ✅ **Lavar el instrumental** usado siguiendo el protocolo (no improvisar)
- ✅ **Esterilizar** todo lo que tocó sangre o mucosa del paciente
- ✅ **Reportar inmediatamente** cualquier pinchazo, corte o exposición a sangre

**Detalles del protocolo:** `05_OPERATIONS/clinical-routines/biosecurity-checklist-mspbs.md` — leer y entender completo antes del primer día.

### En caso de pinchazo accidental

```
1. LAVAR la herida con agua y jabón inmediatamente
2. AVISAR a la doctora
3. LLAMAR al Hospital de Clínicas (021) 000-000 - Infectología
4. IR al hospital en menos de 2 horas
5. REGISTRAR el incidente en el libro de accidentes
```

**No minimizar nunca un pinchazo.** El protocolo es para tu protección.

---

## CONFIDENCIALIDAD

**Lo que pasa en el consultorio es confidencial.** Esto incluye:

- Historias clínicas de pacientes (nombre, CI, diagnóstico, procedimiento)
- Información financiera de pacientes (cuánto pagan, cómo pagan)
- Conversaciones que escuches mientras la doctora atiende
- Fotos de pacientes (sin consentimiento explícito, no se comparten)
- Información personal de la doctora (su agenda, finanzas, planes)

**Lo que NO hacés:**
- ❌ Contar a nadie quién vino al consultorio (amigos, familia, otros pacientes)
- ❌ Sacar fotos del consultorio con pacientes visibles
- ❌ Llevar historias clínicas impresas a tu casa
- ❌ Comentar en redes sociales "trabajé con la doctora y atendió a X famoso"
- ❌ Hablar de un caso clínico con nadie, ni siquiera con otros miembros del equipo

**Si te preguntan algo:** "No puedo compartir información de pacientes. ¿Querés dejar tu mensaje y le digo a la doctora que te llame?"

---

## MANEJO DE EMERGENCIAS

### Emergencia durante procedimiento

1. **Mantener la calma.** Tu reacción afecta al paciente.
2. **Avisar a la doctora** si ves algo anómalo (sangrado excesivo, paciente pálido, etc.).
3. **No actuar por tu cuenta** salvo que la doctora te lo pida.
4. **Llamar al 141** (emergencias PY) si la doctora lo indica.

### Caída o desmayo de paciente

1. Asistir al paciente para que no se golpee.
2. Avisar a la doctora inmediatamente.
3. Si el paciente no responde, **llamar al 141**.
4. No dar agua ni comida hasta que la doctora lo indique.

### Falla de equipo durante procedimiento

1. Avisar a la doctora inmediatamente.
2. NO intentar arreglar nada vos misma (puede empeorar).
3. La doctora tiene el contacto del servicio técnico.

---

## RELACIÓN CON LA DOCTORA

### Qué SÍ hacer

- Llegar a horario
- Pedir feedback: "¿Hice algo bien hoy?" / "¿Qué puedo mejorar?"
- Anotar las preferencias de la doctora (cómo le gusta que le pasen el instrumental, qué materiales prefiere)
- Comunicar problemas antes de que escalen
- Ser honesta si no sabés hacer algo
- Sugerir mejoras que hayas visto

### Qué NO hacer

- Dar opiniones médicas a pacientes
- Decir "yo creo que..." sobre un diagnóstico o procedimiento
- Decidir vos sola un descuento o excepción de precio
- Hablar mal de la doctora a otros pacientes o personas
- Asumir permisos que no te dieron (cobrar de más, cambiar turnos, etc.)

### Si tenés un problema con la doctora

- Hablar directamente con ella, en privado, fuera del horario de pacientes.
- Si no se resuelve, escalar a Iván (el dueño).
- **Nunca** hablar mal de la doctora a un paciente.

---

## HERRAMIENTAS Y SISTEMAS

### Sistema de gestión de pacientes

- **Qué:** Software dental (a decidir: SAM, OdontoGram, Dentalink, etc. — la doctora está evaluando)
- **Tu rol:** cargar datos administrativos del paciente (nombre, CI, teléfono, obra social si tiene), NO diagnóstico
- **Backup:** semanal, en disco duro externo o nube

### Messaging Business

- **Tu rol:** responder consultas, agendar citas, confirmar turnos, enviar recordatorios
- **NO:** dar información médica, discutir precios sin consultar, responder quejas complejas (escalar a la doctora)

### Sistema de cobro

- **Efectivo:** guardar en caja fuerte, anotar en libro de caja
- **POS Bancard:** pasar tarjeta, dar comprobante
- **Pagopar:** enviar link de pago por Messaging
- **Transferencia:** confirmar recibido en el banco

### Inventario

- **Qué:** planilla con stock de EPP, materiales, instrumental
- **Tu rol:** anotar consumo diario, alertar cuando algo esté bajo del mínimo
- **Reposición:** semanal o cuando la doctora lo pida

---

## LO QUE LA DOCTORA ESPERA DE VOS EN 30 DÍAS

### Semana 1

- [ ] Leer este manual completo
- [ ] Leer el checklist de bioseguridad completo
- [ ] Conocer el sistema de gestión de pacientes
- [ ] Memorizar las quick replies de Messaging
- [ ] Saber dónde está cada cosa en el consultorio
- [ ] Hacer 1 prueba completa: abrir el consultorio, atender un paciente simulado, cerrarlo

### Semana 2

- [ ] Atender pacientes reales bajo supervisión directa de la doctora
- [ ] Cargar correctamente 5 historias clínicas
- [ ] Cobrar 5 pacientes (diferentes métodos de pago)
- [ ] Manejar 3 objeciones comunes sin escalación

### Semana 3

- [ ] Atender sola el sillón en procedimientos simples (profilaxis, blanqueamiento)
- [ ] Cerrar el consultorio sola 1 vez
- [ ] Reconocer cuándo escalar a la doctora

### Semana 4

- [ ] Operación autónoma del día a día
- [ ] Sugerir al menos 1 mejora concreta basada en lo observado
- [ ] Confirmar que querés quedarte (la doctora también te está evaluando)

---

## COMPENSACIÓN Y DERECHOS (lo básico en PY)

- **Salario mínimo PY (2026):** Gs 2.798.309/mes (~$370 USD)
- **Para asistente con experiencia:** Gs 2,5-3,5M/mes (~$320-450 USD) — verificar en `01_RESEARCH/procurement/paraguay-dental-labor-assistant-receptionist-costs.md`
- **Jornada:** 8 horas, con 1 hora de almuerzo
- **Beneficios legales (PY):**
  - Aguinaldo (13° sueldo) en junio y diciembre
  - Vacaciones: 12 días hábiles después de 1 año
  - IPS (seguro social): aporte patronal + obrero
  - Aporte a la caja de jubilaciones (IPS o privada)
- **Beneficios extra que puede ofrecer la doctora:**
  - Día libre el día de tu cumpleaños
  - Capacitación pagada (la doctora te puede enviar a un curso de auxiliar)
  - Uniforme proporcionado por la doctora

**Detalles legales están en el contrato laboral que vas a firmar.** Si no hay contrato escrito, NO aceptes el puesto — sin contrato no hay derechos laborales.

---

## MENSAJE FINAL

Este consultorio es chico al inicio (probablemente solo vos y la doctora al principio). Eso es una ventaja: vas a aprender TODO de cómo funciona una práctica privada bien hecha.

Si tenés dudas, preguntas, o simplemente no sabés qué hacer: **preguntá.** Es mejor preguntar y hacer bien, que asumir y hacer mal.

Bienvenida al equipo. 💛

---

*Versión 1.0 — 7 julio 2026.*
*Erebus (Ai-Whisperers).*
*Cross-ref: `05_OPERATIONS/clinical-routines/daily-weekly-monthly-routine.md` + `biosecurity-checklist-mspbs.md` + `legal-compliance/practice-legal/` (contrato laboral cuando se defina).*