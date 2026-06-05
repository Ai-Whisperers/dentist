# WHATSAPP BUSINESS AUTOMATION BLUEPRINT — DRA. GP DENTAL
> AI research + Telegram voice input (Kiki transcription) | June 2026
> Human creative review advised

**Dentist clinic** | Patient ops automation | Source: Industry best practices + market

---

## Executive Summary

WhatsApp automation doesn't replace human touch — it scales it. For Dra. GP's
clinic, WhatsApp is the operating system for patient relationship: all
scheduling, reminders, reactivation, and support flows through it.

This blueprint gives you production-ready message templates and sequence logic
Kiki 2026-06-05 transcription + pinterest + playbook.  Use Copy-Bot + Erebus to
refine into the actual bot.

---

## 1. WHATSAPP CONTACT STRATEGY

### Phone Number Structure
- Use **new, clinic-branded number** — separate from Dra. GP's personal line
- Display it everywhere: GBP, website, business cards, social, QR in clinic
- Default behavior: every inbound message gives clinic name + first name

### Auto-Reply Rules
- **Working hours**: Instant acknowledgment — "Tu mensaje fue recibido. Te respondo en minutos mientras estoy en consulta."
- **After hours**: "Estamos fuera de horario. Te respondo mañana a las 9hs. Si es urgencia, llamá al [emergency number]."

### Greeting Menu (first contact)
```
Dra. Gabriella González Pane — Clínica Dental
🦷 Segunda opinión | Planificación | Estética

👋 Hola! Soy el asistente de DraGP.
Elegí una opción:
1. Agendar segunda opinión
2. Consulta general / limpieza
3. Urgencia dental
4. Hablar con persona
5. Precios / planes de pago
```

---

## 2. CORE SEQUENCES

### A. Appointment scheduling flow

```
[PATIENT] → "Quiero turno"
[BOT]     → "Perfecto! Decime:
               1. Segunda opinión / planificación (primera vez)
               2. Limpieza / control
               3. Endodoncia / implante / corona
               4. Urgencia (dolor, fractura)
               O escribime qué necesitás."

[PATIENT] → selects option
[BOT]     → "Excelente. Decime:
               - Tu nombre
               - Tu teléfono (si no es este)
               - Día que preferís (lun–sáb)"
               [collect in structured message]

[BOT]     → "Listo! Te confirmo:
               Servicio: [X]
               Fecha: [Y]
               Hora: [Z]
               Doctora: Dra. Gabriella González Pane
               Dirección: [clinic address]

               Confirmás? (Sí / No / Cambiar horario)"
```

**What actually happens at confirmation:**
- Assistant receives Woocommerce-like order → manually enters in SAM
- Bot sends calendar .ics or simple text reminder 24h before
- Bot requests insurance / prep before appointment (if applicable)

---

### B. Pre-appointment prep sequence (24h before)

```
[HOUR-BEFORE-BOT] → "🦷 Recordatorio: Tenés tu cita mañana [day] a las [time].
                     Dirección: [address]
                     Traé: CI, turno o constancia de obra social (si aplica)
                     WhatsApp: [clinic number]
                     Llegada 10 min antes para formulario.

                     Confirmá asistencia respondiendo 1."
```

If no reply → assistant calls. Standard missed-appointment protection.

---

### C. Post-appointment follow-up (4h after)

```
[POST-BOT] → "Hola [name]! Espero que tu visita de hoy haya sido cómoda.

              ¿Podemos ayudarte con algo más?
              - Dudas sobre cuidados post-tratamiento
              - Próxima cita (recordá: planificación sin costo para clientes)
              - Presupuesto para tratamiento recomendado

              Te respondo cuando quieras."
```

Trigger: 4h after appointment end time, not from clock.

---

### D. Review request sequence (48h after)

```
[REVIEW-BOT] → "Hola [name]! ¿Cómo fue tu experiencia en la clínica hoy?

               Tu opinión nos ayuda a crecer.
               Dejanos 1 minuto: [Google link]
               (Y te regalamos 10% off en tu próxima limpieza)

               Gracias!"
```

Incentive mechanic: 10% off next cleaning. Tied to review left (assistant
verifies before applying discount). Rule on validity: 30 days.

---

### E. Reactivation sequence (90 days of no-contact)

```
[REACT-BOT 90d] → "Hola [name]! Hace [X] meses que no nos vemos.

                   Te extrañamos 🦷

                   Te regalo una revisión gratuita (valor Gs 300,000)
                   para chequear el estado de tu tratamiento.

                   Agenda en 1 mensaje: [link / respondé 'revisión']"

[REACT-BOT 180d] → "Hola [name]! [Service] listo para retomar.
                     ¿Venís este mes? Te reservo el horario que prefieras
                     junto con DraGP directo."
```

Stops automatically after patient replies or books.

---

### F. Crisis / complaint automation

```
[IF patient says "queja" / "mal" / "enojado"]:
[BOT] → "Disculpa por la experiencia. Te atiende DraGP o mi supervisor/a
        personal para resolverlo ahora. Podemos llamarte al [number]?"
→ Assistant immediately picks up
→ Bot also sends apology + assistant's direct number
```

Never leave complaints in chat limbo. Humans own negative sentiment.

---

## 3. BOT PERSONALITY (Telegram / WhatsApp voice input + AI)

### Voice
- Warm, professional, NOT medical-robot
- Uses "vos" (Paraguayan Spanish) — casual but not slang
- Healthcare context: empathetic understatement

### Example responses by sentiment
```
Patient: "tengo un dolor de muelas terrible"
Bot:    "Te entiendo — vamos a priorizar eso. Dame tu nombre y teléfono
         para destinarte una atención de urgencia con la Doctora hoy o
         mañana a primera hora."

Patient: "no puedo ir mañana, es muy lejos"
Bot:    "Entiendo. Te ofrezco la opción de reagendar para después de tu
         horario — los sábados hasta las 14hs suelen funcionar para
         pacientes de fuera. ¿Te sirve?"

Patient: "cuánto cuesta un implante"
Bot:    "El costo depende del tipo de implante + la corona, y si se combina
         con otros tratamientos. Te armo un presupuesto personalizado
         en menos de 24hs — podés pasar por la clínica o te lo envío
         por acá. Decime cómo lo querés recibir."
```

Never quote fixed prices for implants in automation — price variance is too
wide. Reference USD-pricing guide when ready; human reviews specific quote.

---

## 4. FLOW MAP

```
                  Inbound patient
                       |
                       v
            ┌──────────────────────┐
            │   Greeting + menu    │
            └─────────┬────────────┘
                      |
          ┌───────────┼────────────┐
          |           |            |
       Schedule   Pre-existing   Random
          |         patient         |
          v           |            v
   Collect info   Pull record   Answer Qs /
   + confirm       + prep        Triaging
          |           |            |
          v           v            v
    Manual SAM    Assist         Handoff
    entry +       continues       to human
    calendar
          |
          v
  Reminder sequences (24h, 4h post, review q at 48h,
  reactivation at 90d, 180d)
```

---

## 5. LAUNCH CHECKLIST

- [ ] WhatsApp Business API approved + number active
- [ ] Bot personality confirmed (Copy-Bot drafts)
- [ ] Greeting menu + 5 intent categories
- [ ] SMS backup for reminders (in case WA fails)
- [ ] Google Calendar as visible public calendar
- [ ] Review request incentive configured (10% off tracked in spreadsheet)
- [ ] Complaint escalation SOP written + shared with assistant

---

## Human Tasks

| Task | Why human required |
|------|--------------------|
| Approve greeting menu copy (preserves brand voice) | Brand voice |
| Set penalty price incentives (review discount rate) | Financial policy |
| Confirm emergency number escalation chain | Clinical safety |
| Approve WhatsApp number + business registration | Legal/business registration |
| Train assistant on bot handoff (when bot stops) | Training |

---

*Sources: AI-transcribed voice input (Kiki 2026-06-05), competitive audit,
standard WhatsApp Business healthcare best practices.*
