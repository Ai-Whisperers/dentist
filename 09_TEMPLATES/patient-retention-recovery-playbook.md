# PATIENT RETENTION & RECOVERY PLAYBOOK — DRA. GP DENTAL
> AI research | June 2026 | Human adaptation advised

**Dental clinic operations** | Retention system | Source: Industry best practices

---

## Executive Summary

Two bottlenecks kill clinic revenue: no-shows and patients who never return
after initial treatment. This playbook gives a end-to-end system for both.
It mirrors what SaaS startups call "activation → retention → expansion"
but adapted for a one-location dental practice.

---

## 1. METRICS TO TRACK (baseline now, optimize continuously)

| Metric | Current (Jan-May) | Stage 1 target | Stage 2 target |
|--------|------------------|----------------|----------------|
| Show rate | 62.5% | 75% | 85% |
| Late arrivals | 38.5% | 25% | 15% |
| No-shows cancelled | 19.1% | 14% | 8% |
| Patients with 1→2 appointments | Baseline TBD | 50% | 65% |
| Reactivation rate (90d inactive) | TBD | 15% | 25% |
| Review rate | TBD | 25% of treated | 50% of treated |

Source for current: SAM export analysis (601 appointments, 342 patients).

---

## 2. NO-SHOW REDUCTION SYSTEM

### 3-Touch Reminder Sequence (automated via bot)

| Touch | Timing | Channel | Content |
|-------|--------|---------|---------|
| T1 | 7 days out | WhatsApp / SMS | Confirmación fácil: confirmá tu cita [date] respondiendo 1. Incluye mapa + link. |
| T2 | 24h before | WhatsApp + SMS | Recordatorio con hora + dirección. Solicita confirmación. "Si necesitás cancelar, avisanos para ceder el turno" |
| T3 | 3h before | WhatsApp only | Confirma que vas a llegar. Ofrece cambio de horario si ya no podés. |

Non-confirmations after T2 → assistant calls.
Non-confirmations after T3 → downgrade to standby slot or cancel; offer
waitlist if patient responds.

### Reschedule Policy
- No penalty for 24h advance notice
- After 24h: Gs 50,000 rebooking fee (not punitive — signals value of slot)
- Waive for first-time patients or if clinic-caused (doctor delay)
- Policy MUST be communicated in confirmation messages

Waitlist buffer:
- Fill cancellations from waitlist (people who asked for slots)
- Waitlist members get "slot opening" message: "Se liberó un turno [date/time] para [procedure] — lo reservo 2hs"

---

## 3. PATIENT REACTIVATION SYSTEM

### Inactivity Triggers

| Days inactive | Tag | Action |
|---------------|-----|--------|
| 60 | Watch | No action — monitor |
| 90 | Reactivate | Send reactivation message (appointment blueprint E) |
| 120 | Offer | Send discount/review offer |
| 180 | Recall | Assistant personal call |

### Advanced reactivation: segmented

Segment by last treatment type:
- **Cleaning only** → "Tu próxima profilaxis a los 6 meses — agendala ahora y evitá formación de sarro."
- **Restorative** (filling/crown) → "Control de la restauración — sin costo a los 6 meses."
- **Orthodontics** → "Control de brackets — recordá venir cada mes."
- **No treatment received** (consult only) → "Todavía no definiste tu tratamiento? Te ayudo a crear el plan."

---

## 4. FIRST-VISIT SYSTEM ("ACTIVATION")

Goal: Turn consultation into second appointment.

### Day 0 (consultation visit)
- Treatment plan presented verbally + on paper (take-home)
- Assistant schedules next step at front desk BEFORE patient leaves
- Patient receives WhatsApp summary: treatment plan + recommended next date
  + price range (Gs) for next step

### Day +1
- Bot: follow-up asking "¿Quedaron claras las recomendaciones de DraGP?"
  + link to Como cuidar tus dientes page
- Attach PDF with post-treatment care instructions

### Day +3
- Bot: "¿Podemos agendar tu próxima cita? Si querés, coordinamos por acá mismo."
- No-pressure scheduling; finishes in 3 taps intent

### Day +7
- Assistant call if not scheduled: check for questions + help find time

---

## 5. LOYALTY / REWARD MECHANICS

| Loyalty mechanic | Trigger | Reward | Cost |
|-----------------|---------|--------|------|
| Review discount | Google review left | 10% off next cleaning | Gs ~25k |
| Referral reward | New patient mentions referrer | Both get Gs 50k credit / 5% off | Gs 100k |
| Johnny-come-lately | 10-month no-show streak reactivated | Discounted control cleaning | Gs 15–25k |
| Family bundle | 2+ family members register | 15% group discount on cleanings | Volume gain |

Rewards break even when referral produces at least one additional paid visit.
With LTV of patient ~Gs 1.2M over 2 years, a Gs 100k acquisition cost is fine.

---

## 6. REVENUE EXPANSION ("UPSELL" WITHOUT PUSHY SALES)

At each appointment type, prescribe next step using conversational language
(not checkout aisle):

| Visit type | Logical next step | Timing |
|-----------|-------------------|--------|
| Cleaning → | Fluoride top-up or night guard | End of visit |
| Restorative → | Periodic control (3–6mo) | When placing restoration |
| Surgery (extraction) → | Implant discussion window | 4–6 weeks post-op |
| Orthodontics → | Whitening for special occasion | 6 months into treatment |

Key: do not sell at the moment of payment; plant proposal for next visit via
message 3–5 days later. Patient calmness = higher yes rate.

---

## 7. APPOINTMENT TYPES + LENGTH CONVENTION

Define these so scheduling is fast and predictable:

| Type | Duration | Buffer after | Typical fee |
|------|----------|-------------|-------------|
| Consulta / segunda opinión | 30 min | 15 min | Gs 450,000 |
| Limpieza + control | 45 min | 15 min | Gs 300,000 |
| Restauración simple | 60 min | 20 min | Gs 350,000+mat |
| Endodoncia | 90 min | 30 min | Gs 1.2M |
| Corona / implante | 120 min | 30 min | Gs 3.5M+ |
| Cirugía | 150+ min | 45 min | Gs variable |

Buffer enforces realistic calendar and protects next patient experience.

---

## 8. AUTOMATION RULES (Erebus rules)

1. **Never** send reminders before 8am or after 9pm (PY time).
2. **Never** ask for payment directly from bot — bot proposes, human confirms.
3. **Do not** automate treatment-price quotes in bot — too variable, creates trust risk.
4. **Never** cancel a slot automatically on non-confirmation — human asset.
5. **Always** confirm before/after identity consent before using in marketing.
6. **Never** auto-send clinical advice — bot routes to doctor for any pain/diagnosis.

---

## Human Tasks

| Task | Why |
|------|-----|
| Define cancel/reschedule policy (fee or grace) | Business decision |
| Set loyalty discount rate (referral, review) | Financial |
| Approve WhatsApp templates before launch | Brand voice |
| Create patient consent form language (for marketing use) | Legal |
| Write post-treatment care protocol (per procedure type) | Clinical quality |

---

*Sources: SAM export analysis (601 appointments), WhatsApp Business healthcare
best practices, dental clinic retention benchmarks.*
