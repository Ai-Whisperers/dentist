# CONVERSATION FLOWS — DECISION TREE
## Dra. Gabriella González Pane — WhatsApp Channel
**Version:** 1.0 — June 2026
**Purpose:** Visual decision tree for Hermes agent — every possible path through a conversation.

---

## MASTER FLOW CHART

```
INCOMING MESSAGE
       ↓
[HERMES RECEIVES]
       ↓
┌──────┴───────┐
CLASSIFY       CHECK CRM
       ↓                ↓
NEW CONTACT? ──→ Lookup by phone
       │                │
       ├─ YES ──→ [WELCOME] → Gather info → Classify intent
       │
       └─ NO ──→ Check name
                    │
       ┌────────────┴───────────┐
       ↓                         ↓
  KNOWN PATIENT              UNKNOWN CONTACT
       ↓                         ↓
  [EXISTING_PATIENT_FLOW]    [NEW_CONTACT_FLOW]
```

---

## BRANCH 1: NEW CONTACT — FIRST TIME MESSAGING

```
NEW CONTACT MESSAGE RECEIVED
         ↓
[Check: Is phone in CRM?]
         ↓
    NO — New contact
         ↓
[Classify: PRICING / APPOINTMENT / SECOND_OPINION / OTHER]
         ↓
┌────────┴────────┬──────────────┐
↓                 ↓              ↓
PRICING          APPOINTMENT    SECOND_OPINION
    ↓                 ↓              ↓
[Send P1]      [Send A1]      [Send S1]
    ↓                 ↓              ↓
[Wait reply]   [Wait reply]   [Tag HOT_LEAD]
    ↓                 ↓              ↓
┌─┴─┐          ┌─┴─┐         [Alert Dra. GP]
│   │          │   │         [Wait reply]
│   └──────────┴─┘ │         [Send S3 on book]
│                  │
┌─┴────────────────┴─┐
↓                     ↓
BOOKED               NO REPLY
    ↓                     ↓
[Confirm Appt]    [Wait 48h]
    ↓                     ↓
[Log CRM]         [Send F1]
    ↓                     ↓
[Reminder in 24h]     [No reply again?]
                           [Log as cold lead]
```

---

## BRANCH 2: EXISTING PATIENT MESSAGING

```
KNOWN PATIENT MESSAGE
         ↓
[Lookup in CRM: Last visit, Treatment, Notes]
         ↓
[Classify: SCHEDULING / QUESTION / COMPLAINT / PAIN]
         ↓
┌────────┴────────┐
↓                 ↓
CLINICAL QUESTION  SCHEDULING/OTHER
    ↓                 ↓
[Escalate to Dra. GP]  [Respond per template]
    ↓                     ↓
[Dra. GP responds]  [Log CRM]
    ↓                     ↓
[Agent relays]         [Wait reply]
```

---

## BRANCH 3: URGENT DENTAL PROBLEM

```
URGENT MESSAGE DETECTED
(pain, bleeding, swelling, trauma)
         ↓
[Immediate alert to Dra. GP — priority]
         ↓
[Send U1 (urgent acknowledgment)]
         ↓
[Collect: What, Where, Severity, Duration]
         ↓
┌─────────────────┐
↓                 ↓
SEVERE (9-10)    MODERATE (4-8)
    ↓                 ↓
[Tell patient to  [Assess — can wait?]
  call NOW]           ↓
    ↓            YES — CAN WAIT
YES — GO NOW         ↓
    ↓         [Send self-care instructions]
[Provide urgent    [Alert Dra. GP]
  clinic contact]   [Dra. GP responds within 30 min]
    ↓
[Dra. GP takes over]
```

---

## BRANCH 4: REFERRAL MENTIONED

```
USER SAYS: "[NAME] me recomendó" / "me dijo que te contacte"
         ↓
[Lookup referrer in CRM]
         ↓
┌──────────┴──────────┐
↓                     ↓
FOUND (active referrer)  NOT FOUND
    ↓                     ↓
[Log: Referral from X]  [Log: Unknown source]
    ↓                     ↓
[Send R1 (referral) + W3] [Send W3 as new contact]
    ↓                     ↓
[Classify intent]         [Classify intent]
    ↓                     ↓
[Normal flow]             [Normal flow]
```

---

## BRANCH 5: PRICING INQUIRY PATH

```
PRICING INQUIRY RECEIVED
         ↓
[Check: Is this from known patient?]
         ↓
    YES ──→ [Send E3 (existing patient pricing)]
         ↓
     NO
         ↓
[Send P1 (standard pricing card)]
         ↓
[Wait 5 min — if no reply]
         ↓
[Send P2 (second opinion hook)]
         ↓
[Wait 24h]
         ↓
[Send A1 (appointment suggestion)]
         ↓
[Wait 48h]
         ↓
[Send follow-up F1]
         ↓
[No response → Log COLD_LEAD in CRM]
```

---

## BRANCH 6: APPOINTMENT BOOKING PATH

```
APPOINTMENT REQUEST RECEIVED
         ↓
[Send A1 (gathering info + slots)]
         ↓
[User responds: Name + preferred time]
         ↓
[Check: Time available in calendar?]
         ↓
    YES ──→ [Send A2 (CONFIRM)]
    NO
         ↓
[Send: "Ese horario ya no está disponible. Te ofrezco: [ALTERNATIVES]"]
         ↓
[User picks new time]
         ↓
[Confirm]
         ↓
[Send A2]
         ↓
[24h before: Send A3 (reminder)]
         ↓
[After appointment: Send E1 (follow-up)]
```

---

## BRANCH 7: SECOND OPINION PATH

```
SECOND OPINION REQUEST RECEIVED
         ↓
[Tag: HOT_LEAD]
         ↓
[Alert: Notify Dra. GP immediately]
         ↓
[Send S1 (second opinion intro)]
         ↓
[Wait for response]
         ↓
[User describes their situation]
         ↓
[Collect: What's the treatment? When was it recommended? X-rays?]
         ↓
[Send S3 (if time selected) or S2 (follow-up)]
         ↓
[Appointment confirmed]
         ↓
[POST-APPOINTMENT]
         ↓
[If treatment needed: Send S4]
[If no treatment / conservative: Send S5]
         ↓
[Log outcome in CRM]
         ↓
[If treatment accepted: Start treatment flow]
[If not: Keep in CRM for follow-up]
```

---

## BRANCH 8: COMPLAINT PATH

```
COMPLAINT RECEIVED
         ↓
[Do NOT try to solve]
         ↓
[Send ESC3 (acknowledge + promise response)]
         ↓
[Log: COMPLAINT — ESCALATED]
         ↓
[Alert Dra. GP immediately]
         ↓
[Dra. GP responds personally within 2h]
         ↓
[If resolved: Close in CRM]
[If not: Follow up until resolved]
```

---

## BRANCH 9: WORK/EMPLOYMENT INQUIRY

```
WORK INQUIRY RECEIVED
         ↓
[Send B1 (not hiring)]
         ↓
[Log as WORK — no action]
```

---

## BRANCH 10: SPAM / UNSOLICITED

```
SPAM / GIBBERISH RECEIVED
         ↓
[Do NOT respond]
         ↓
[Block sender if repeat]
         ↓
[Log as SPAM]
```

---

## APPOINTMENT CANCELLATION FLOW

```
CANCEL REQUEST RECEIVED
         ↓
[Check: When is the appointment?]
         ↓
MORE THAN 24h AWAY ──→ [Send A6 (cancel confirmation)]
         │                        ↓
         │                   [Free calendar slot]
         │                        ↓
         │                   [Offer new time?]
         │                        ↓
         │                   [If yes → appointment flow]
         │                        ↓
         │                   [Log as CANCELLED]
         │
LESS THAN 24h AWAY ──→ [Send: "Para cancelar con menos de 24h de anticipación, ]
                          necesito saber la razón. ¿Hubo algún problema?"
         ↓
[If emergency/valid reason: Accept cancellation]
[If no reason: Note in CRM — "no-show risk for future"]
         ↓
[Log cancellation]
```

---

## ESCALATION DECISION MATRIX

```
MESSAGE RECEIVED → CLASSIFIED AS
         ↓
┌─────────────────────────┐
│URGENT? → YES          │→ Always escalate immediately
│Pain 9-10 / Bleeding /  │
│Trauma / Swelling        │
└─────────────────────────┘
         ↓ NO
┌─────────────────────────┐
│CLINICAL QUESTION?      │→ Always escalate to Dra. GP
│Diagnosis / Treatment /   │
│Symptoms beyond agent    │
│knowledge scope          │
└─────────────────────────┘
         ↓ NO
┌─────────────────────────┐
│COMPLAINT?               │→ Always escalate
│Dissatisfaction /        │
│Negative experience      │
└─────────────────────────┘
         ↓ NO
┌─────────────────────────┐
│SECOND OPINION?          │→ Always tag HOT_LEAD
│Already classified as    │→ Always notify Dra. GP
│SECOND_OPINION           │
└─────────────────────────┘
         ↓ NO
┌─────────────────────────┐
│REFERRAL + HIGH VALUE?   │→ Notify Dra. GP
│New contact from         │
│known referrer           │
└─────────────────────────┘
         ↓ NO
┌─────────────────────────┐
│EXISTING PATIENT +       │→ Escalate to Dra. GP
│CLINICAL UPDATE?         │
│Pain after treatment /   │
│Complication report      │
└─────────────────────────┘
         ↓ NO
         → Handle with templates
```

---

## FOLLOW-UP TIMING RULES

| Trigger | Wait Time | Message |
|---------|-----------|---------|
| Pricing inquiry, no reply | 48h | F1 (follow-up) |
| Appointment request, no reply | 4h | A1 reminder |
| Second opinion, no reply | 24h | S2 (gentle follow-up) |
| Post-treatment, no reply | 48h | E1 (care check) |
| Referral, did not book | 72h | OUT2 (re-engagement) |
| Cold lead (after 1 attempt) | 1 week | OUT1 (re-engagement) |
| Recall (6-month cleaning) | 6 months | E3 |
| Birthday | Day of | E5 |
| No response after 3 attempts | — | Log as cold_lead, stop |

---

## TIMING EXCEPTIONS

- **URGENT messages** → Immediate, no wait
- **HOT_LEAD (second opinion)** → Response within 30 min always
- **COMPLAINT** → Response within 2 hours always
- **EXISTING PATIENT with pain** → Response within 15 min

---

## LOGGING REQUIREMENTS PER FLOW

Every transition in every flow logs:

```
[STEP] → [TIMESTAMP] → [CLASSIFICATION] → [ACTION] → [NEXT_WAIT]
```

Example:
```
A1_SENT → 2026-06-01 10:30 → APPOINTMENT_REQUEST → Offered slots → Awaiting reply → 4h
USER_REPLY → 2026-06-01 11:45 → APPOINTMENT_REQUEST → Provided name + preferred time → Confirming slot
A2_SENT → 2026-06-01 11:46 → APPOINTMENT_CONFIRMED → Slot [DATE/TIME] confirmed → Calendar updated
```

---

## DECISION TREE SUMMARY CARD

| IF message contains... | AND sender is... | THEN classify as... | AND use template... |
|---|---|---|---|
| "cuánto cuesta" / "precios" / "costo" | New | PRICING | P1 |
| "quiero agendar" / "turno" / "cita" | New | APPOINTMENT | A1 |
| "second opinion" / "me dijeron que necesito" / "¿es necesario?" | New | SECOND_OPINION | S1 |
| "me dérivó" / "me recomendó" | New | REFERRAL | R1 |
| "dolor" / "urgencia" / "no puedo" / "sangre" | Any | URGENT | U1 |
| "no estoy conforme" / "mal resultado" / "problema" | Existing | COMPLAINT | ESC3 |
| "tengo una pregunta sobre mi tratamiento" | Existing + clinical | CLINICAL | ESC2 |
| "hola" + new phone | New | UNKNOWN | W1 |
| "trabajo" / "empleo" / "busco trabajo" | Any | WORK | B1 |

---

**END OF DECISION TREE**

All flows documented. Agent uses this as reference for every classification decision.